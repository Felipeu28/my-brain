#!/usr/bin/env python3
"""
Teams Brain Pull — Microsoft Graph API Integration
Pulls messages from your Microsoft Teams channels and saves them
as structured Brain raw files for ingestion.

Setup: Run python teams_pull.py --setup on first use.
Auth:  Device code flow — you'll visit a URL and sign in with your Microsoft account.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ── Config ─────────────────────────────────────────────────────────────────────
BRAIN_DIR = Path(__file__).parent.parent  # ~/My Brain/knowledge-base/
RAW_DIR   = BRAIN_DIR / "raw"
CONFIG_FILE = BRAIN_DIR / "scripts" / ".teams_config.json"
TOKEN_FILE  = BRAIN_DIR / "scripts" / ".teams_token.json"

# Scopes needed to read Teams messages
SCOPES = [
    "ChannelMessage.Read.All",
    "Channel.ReadBasic.All",
    "Team.ReadBasic.All",
    "Chat.Read",
    "User.Read",
]

# ── Dependencies ────────────────────────────────────────────────────────────────
def ensure_deps():
    try:
        import msal, requests
    except ImportError:
        print("Installing required packages...")
        os.system(f"{sys.executable} -m pip install msal requests --quiet")
        print("Done.\n")

ensure_deps()

import msal      # noqa: E402
import requests  # noqa: E402


# ── Auth ────────────────────────────────────────────────────────────────────────
def load_config():
    if not CONFIG_FILE.exists():
        print("\n⚠️  No config found. Run: python teams_pull.py --setup\n")
        sys.exit(1)
    return json.loads(CONFIG_FILE.read_text())


def get_token(config):
    """Get access token via device code flow (first time) or from cache."""
    app = msal.PublicClientApplication(
        config["client_id"],
        authority=f"https://login.microsoftonline.com/{config['tenant_id']}",
    )

    # Try cached token first
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
        if result and "access_token" in result:
            return result["access_token"]

    # Device code flow — user visits URL and signs in
    flow = app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in flow:
        raise ValueError(f"Failed to create device flow: {flow}")

    print("\n" + "═" * 60)
    print(f"  {flow['message']}")
    print("═" * 60 + "\n")

    result = app.acquire_token_by_device_flow(flow)
    if "access_token" not in result:
        raise ValueError(f"Auth failed: {result.get('error_description', result)}")

    print("✅  Signed in successfully! Token cached for future runs.\n")
    return result["access_token"]


# ── Microsoft Graph API helpers ─────────────────────────────────────────────────
class Graph:
    BASE = "https://graph.microsoft.com/v1.0"

    def __init__(self, token):
        self.headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    def get(self, path, params=None):
        url = f"{self.BASE}{path}"
        results = []
        while url:
            r = requests.get(url, headers=self.headers, params=params)
            r.raise_for_status()
            data = r.json()
            results.extend(data.get("value", [data]))
            url = data.get("@odata.nextLink")
            params = None  # only use params on first request
        return results

    def get_teams(self):
        return self.get("/me/joinedTeams")

    def get_channels(self, team_id):
        return self.get(f"/teams/{team_id}/channels")

    def get_messages(self, team_id, channel_id, since_days=7):
        since = (datetime.now(timezone.utc) - timedelta(days=since_days)).isoformat()
        messages = self.get(
            f"/teams/{team_id}/channels/{channel_id}/messages",
            params={"$filter": f"createdDateTime ge {since}", "$top": 50},
        )
        return [m for m in messages if m.get("messageType") == "message"]

    def get_chat_messages(self, since_days=7):
        """Get 1:1 and group chat messages."""
        since = (datetime.now(timezone.utc) - timedelta(days=since_days)).isoformat()
        chats = self.get("/me/chats?$expand=members")
        all_messages = []
        for chat in chats[:10]:  # limit to 10 most recent chats
            try:
                msgs = self.get(
                    f"/me/chats/{chat['id']}/messages",
                    params={"$top": 20},
                )
                for m in msgs:
                    m["_chat_topic"] = chat.get("topic") or "Direct Message"
                all_messages.extend(msgs[:10])
            except Exception:
                pass
        return all_messages


# ── Message formatting ──────────────────────────────────────────────────────────
def clean_body(body):
    """Strip HTML tags from message body."""
    import re
    if not body:
        return ""
    text = body.get("content", "")
    text = re.sub(r"<[^>]+>", "", text)  # remove HTML
    text = re.sub(r"\s+", " ", text).strip()
    return text[:500]  # cap at 500 chars


def format_sender(msg):
    sender = msg.get("from", {})
    user = sender.get("user", {})
    return user.get("displayName", "Unknown")


def format_date(iso_str):
    if not iso_str:
        return "Unknown"
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%b %d %I:%M%p").lstrip("0")
    except Exception:
        return iso_str[:10]


# ── Output generation ───────────────────────────────────────────────────────────
def build_markdown(graph, config, since_days):
    today = datetime.now().strftime("%Y-%m-%d")
    since_str = (datetime.now() - timedelta(days=since_days)).strftime("%b %d")
    now_str = datetime.now().strftime("%b %d")

    lines = [
        f"# Teams Digest — {since_str} to {now_str}",
        f"",
        f"**Extracted:** {today} | **Window:** last {since_days} days",
        f"",
        f"---",
        f"",
    ]

    channel_filter = set(config.get("channels", []))  # empty = all
    teams = graph.get_teams()

    total_messages = 0

    for team in teams:
        team_name = team["displayName"]
        team_id = team["id"]

        channels = graph.get_channels(team_id)
        team_lines = []

        for ch in channels:
            ch_name = ch["displayName"]
            ch_id = ch["id"]

            # Apply channel filter if configured
            if channel_filter and ch_name not in channel_filter:
                continue

            try:
                messages = graph.get_messages(team_id, ch_id, since_days)
            except Exception as e:
                if "403" in str(e) or "Forbidden" in str(e):
                    continue  # skip channels we can't read
                raise

            if not messages:
                continue

            total_messages += len(messages)
            team_lines.append(f"### #{ch_name} ({len(messages)} messages)")
            team_lines.append("")

            for msg in messages[-20:]:  # last 20 per channel
                sender = format_sender(msg)
                date = format_date(msg.get("createdDateTime", ""))
                body = clean_body(msg.get("body", {}))
                if not body or body.startswith("<"):
                    continue
                team_lines.append(f"- **{sender}** {date}: {body}")

            team_lines.append("")

        if team_lines:
            lines.append(f"## {team_name}")
            lines.append("")
            lines.extend(team_lines)
            lines.append("---")
            lines.append("")

    # Summary section
    lines.insert(4, f"**Teams covered:** {len(teams)} | **Messages pulled:** {total_messages}")
    lines.insert(5, "")

    return "\n".join(lines), total_messages


# ── CLI ─────────────────────────────────────────────────────────────────────────
def cmd_setup(args):
    """Interactive first-time setup."""
    print("\n" + "═" * 60)
    print("  Teams Brain — First Time Setup")
    print("═" * 60)
    print("""
You need two things from Azure (Microsoft's cloud):
  1. Your Tenant ID   — identifies your Microsoft 365 org
  2. Your Client ID   — from a free app you'll register

STEP 1 — Get your Tenant ID
  • Go to: https://portal.azure.com
  • Sign in with your Microsoft 365 account
  • Search for "Azure Active Directory" in the top search bar
  • Your Tenant ID is on the Overview page ("Tenant ID" field)
  • Copy it and paste it below
""")
    tenant_id = input("Paste your Tenant ID: ").strip()

    print("""
STEP 2 — Register a free Azure app (takes 3 minutes)
  • In Azure portal, go to: App registrations → New registration
  • Name: "Brain Teams Pull" (or anything)
  • Supported account types: "Accounts in this organizational directory only"
  • Redirect URI: leave blank
  • Click Register
  • On the app overview page, copy the "Application (client) ID"
""")
    client_id = input("Paste your Application (client) ID: ").strip()

    print("""
STEP 3 — Add API permissions (in the app you just created)
  • Click "API permissions" in the left menu
  • Click "Add a permission" → Microsoft Graph → Delegated permissions
  • Search and add these permissions:
      ✓ ChannelMessage.Read.All
      ✓ Channel.ReadBasic.All
      ✓ Team.ReadBasic.All
      ✓ Chat.Read
      ✓ User.Read
  • Click "Grant admin consent" (or ask your IT admin)
""")
    input("Press Enter when done with Step 3...")

    print("""
STEP 4 (optional) — Filter to specific channels
  Leave blank to pull from ALL channels, or enter channel names
  to only pull from those (comma-separated, e.g.: General, Product, Sales)
""")
    channels_raw = input("Channels to pull (blank = all): ").strip()
    channels = [c.strip() for c in channels_raw.split(",") if c.strip()]

    config = {
        "tenant_id": tenant_id,
        "client_id": client_id,
        "channels": channels,
        "since_days": 7,
    }
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(config, indent=2))
    print(f"\n✅  Config saved to {CONFIG_FILE}")
    print("\nNow run: python teams_pull.py")
    print("You'll be asked to sign in once. After that it runs automatically.\n")


def cmd_pull(args):
    config = load_config()
    since_days = args.days or config.get("since_days", 7)

    print(f"🔐  Authenticating with Microsoft...")
    token = get_token(config)
    graph = Graph(token)

    print(f"📥  Pulling Teams messages from the last {since_days} days...")
    markdown, total = build_markdown(graph, config, since_days)

    today = datetime.now().strftime("%Y-%m-%d")
    out_file = RAW_DIR / f"teams-{today}.md"
    out_file.write_text(markdown)

    print(f"\n✅  Saved {total} messages → {out_file}")
    print(f"\nNext step: Run the Brain ingest command to process this file:")
    print(f'  cd "{BRAIN_DIR}"')
    print(f'  claude -p "I just added teams-{today}.md to raw/. Extract decisions, action items, and key context. Update Action-Tracker.md and Decision-Log.md." --allowedTools Bash,Write,Read')


def main():
    parser = argparse.ArgumentParser(description="Teams Brain Pull")
    parser.add_argument("--setup", action="store_true", help="First-time setup")
    parser.add_argument("--days", type=int, help="Days to look back (default: 7)")
    args = parser.parse_args()

    if args.setup:
        cmd_setup(args)
    else:
        cmd_pull(args)


if __name__ == "__main__":
    main()

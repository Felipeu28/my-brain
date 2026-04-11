# Teams → Brain Setup Guide

Get your Microsoft Teams conversations flowing into your Brain automatically. One-time setup, then it runs every week.

---

## What This Does

Every week, Claude pulls messages from your Teams channels → formats them → saves to `raw/teams-YYYY-MM-DD.md` → processes into Action-Tracker.md, Decision-Log.md, and Memory.md.

**You get:** decisions captured, action items tracked, team context in your Brain.

---

## Step 1 — Run First-Time Setup (5 minutes)

Open Terminal and run:

```bash
cd "~/My Brain/knowledge-base"
python3 scripts/teams_pull.py --setup
```

This walks you through 3 things:
1. Getting your Azure Tenant ID (from portal.azure.com)
2. Registering a free Azure app to get a Client ID
3. Adding the right API permissions

**The script gives you exact instructions at each step.**

---

## Step 2 — First Pull & Sign-In

After setup, run your first pull:

```bash
cd "~/My Brain/knowledge-base"
python3 scripts/teams_pull.py
```

You'll see something like:
```
To sign in, use a web browser to open https://microsoft.com/devicelogin
and enter the code: XXXXXX to authenticate.
```

Open that URL, enter the code, sign in with your Microsoft account. Done — your token is cached and you won't need to do this again for 90 days.

---

## Step 3 — Run the Full Ingest

After the pull succeeds, run the full ingest (pulls + Brain update):

```bash
cd "~/My Brain/knowledge-base"
bash scripts/teams_ingest.sh
```

Claude will pull your Teams messages, extract decisions and actions, and update your Brain files automatically.

---

## Step 4 — Schedule It Weekly

To run automatically every Monday morning:

```bash
# Open crontab editor
crontab -e

# Add this line (runs every Monday at 8am):
0 8 * * 1 cd "$HOME/My Brain/knowledge-base" && bash scripts/teams_ingest.sh >> "$HOME/My Brain/knowledge-base/scripts/teams_log.txt" 2>&1
```

Or tell Cowork to schedule it for you: "Schedule my Teams Brain pull every Monday at 8am"

---

## Troubleshooting

**"Permission denied" or 403 errors**
→ The API permissions weren't granted admin consent. Go back to Azure portal → your app → API permissions → Grant admin consent.

**"No messages found"**
→ Your channels filter might be too restrictive, or the last 7 days had no activity. Try `python3 scripts/teams_pull.py --days 14`

**Token expired after 90 days**
→ Just run `python3 scripts/teams_pull.py` again and re-authenticate when prompted.

**Want to pull specific channels only?**
→ Edit `scripts/.teams_config.json` and add channel names to the `"channels"` array:
```json
{ "channels": ["General", "Product", "Engineering"] }
```

---

## What Gets Pulled

- All channels in every Team you're a member of (or filtered ones)
- Last 7 days of messages by default
- Up to 20 most recent messages per channel
- Sender name, timestamp, and message body

**What gets processed into Brain:**
- Decisions → Decision-Log.md
- Action items with owners/deadlines → Action-Tracker.md
- Key context, announcements → Memory.md
- New file entry → index.md

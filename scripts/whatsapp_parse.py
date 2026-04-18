#!/usr/bin/env python3
"""Parse a WhatsApp chat export (.txt) into structured Markdown for the Moil Brain.

Supports two date formats found in WhatsApp exports:
  US (iOS):           [M/D/YY, H:MM:SS AM/PM] Name: text
  International:      [DD/MM/YYYY, HH:MM:SS]   Name: text  (24-h, 4-digit year)

Output: quartz/content/raw/whatsapp-<slug>-<YYYY-MM-DD>.md
  No `ingested: true` frontmatter — picked up by brain-ingest.sh on the
  next run so Claude handles the semantic wiki work.

Usage:
  python3 scripts/whatsapp_parse.py "path/to/WhatsApp Chat with Mom.txt"
  python3 scripts/whatsapp_parse.py file.txt --kb-dir /path/to/knowledge-base
  python3 scripts/whatsapp_parse.py file.txt --stdout   # print md to stdout only
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

# ── Repo root ─────────────────────────────────────────────────────────────────
REPO = Path(__file__).resolve().parent.parent

# ── Andres identification ─────────────────────────────────────────────────────
# Lowercased substrings matched against sender name.
ANDRES_TOKENS = {"andres urrego", "andres", "jarvisurrego"}


def _is_andres(name: str) -> bool:
    nl = name.lower().strip()
    return nl in ANDRES_TOKENS or any(t in nl for t in ANDRES_TOKENS)


# ── Noise detection ───────────────────────────────────────────────────────────
_NOISE_FRAGMENTS = [
    "messages and calls are end-to-end encrypted",
    "missed voice call",
    "missed video call",
    "image omitted",
    "video omitted",
    "audio omitted",
    "sticker omitted",
    "gif omitted",
    "document omitted",
    "contact card omitted",
    "<media omitted>",
    "this message was deleted",
    "you deleted this message",
    "security code changed",
    "added you",
    "removed you",
    "changed the subject",
    "changed this group",
    "created group",
    "null",
    "voice call",
    "video call",
]

_NOISE_RE = re.compile(
    r"(?:" + "|".join(re.escape(f) for f in _NOISE_FRAGMENTS) + r")",
    re.IGNORECASE,
)


def _is_noise(text: str) -> bool:
    t = text.strip().lower()
    if not t:
        return True
    # Invisible / non-printing only
    if not t.isprintable() and len(t) <= 4:
        return True
    return bool(_NOISE_RE.search(t))


# ── Message-line regex ────────────────────────────────────────────────────────
# Handles:
#   [4/18/26, 10:15:00 AM]  (US, 12-h, 2-digit year)
#   [18/04/2026, 10:15:00]  (international, 24-h, 4-digit year)
#   [4/18/2026, 10:15 AM]   (no seconds)
# Unicode narrow no-break space (\u202f) sometimes appears between time and AM/PM.
_MSG_RE = re.compile(
    r"^\[(\d{1,2}/\d{1,2}/\d{2,4}),\s*"
    r"(\d{1,2}:\d{2}(?::\d{2})?(?:[\u202f\s]?[AaPp][Mm])?)\]\s+"
    r"([^:\u200e\u200f]+?):\s*(.*)",
    re.DOTALL,
)

# Strip invisible Unicode direction marks that WhatsApp embeds
_INVIS_RE = re.compile(r"[\u200e\u200f\u202a-\u202e\ufeff]")


def _clean_line(line: str) -> str:
    return _INVIS_RE.sub("", line)


# ── Date parsing ──────────────────────────────────────────────────────────────

def _parse_date(date_str: str, time_str: str) -> date | None:
    """Return a date object, auto-detecting US (M/D/YY) vs international (D/M/YYYY)."""
    parts = date_str.strip().split("/")
    if len(parts) != 3:
        return None
    try:
        a, b, c = int(parts[0]), int(parts[1]), int(parts[2])
    except ValueError:
        return None

    # 4-digit year ⟹ international: DD/MM/YYYY
    # 2-digit year ⟹ US: M/D/YY
    if c > 99:
        day, month, year = a, b, c
    else:
        month, day, year = a, b, 2000 + c

    # If month > 12 the format guessed wrong — swap
    if month > 12 and day <= 12:
        month, day = day, month
    if month > 12 or day > 31:
        return None

    try:
        return date(year, month, day)
    except ValueError:
        return None


# ── Core parser ───────────────────────────────────────────────────────────────

def parse_whatsapp(path: Path) -> list[dict] | None:
    """Parse a WhatsApp .txt export into a list of message dicts.

    Returns None if the file doesn't look like a WhatsApp export.
    Each dict: date, date_str, time_str, sender, text, is_andres.
    """
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return None

    lines = raw.splitlines()
    if not lines:
        return None

    # Quick format sniff — first real line should look like [d/d/dd, ...]
    first_real = next((_clean_line(l) for l in lines[:8] if l.strip()), "")
    if not re.match(r"^\[\d", first_real):
        return None

    messages: list[dict] = []
    current: dict | None = None

    for raw_line in lines:
        line = _clean_line(raw_line)
        m = _MSG_RE.match(line)
        if m:
            if current:
                messages.append(current)
            d = _parse_date(m.group(1), m.group(2))
            current = {
                "date": d,
                "date_str": m.group(1),
                "time_str": m.group(2).strip(),
                "sender": m.group(3).strip(),
                "text": m.group(4).strip(),
                "is_andres": _is_andres(m.group(3).strip()),
            }
        elif current and line.strip():
            # Continuation of the previous message
            current["text"] += "\n" + line.strip()

    if current:
        messages.append(current)

    return messages or None


# ── Action-item extraction ────────────────────────────────────────────────────

_COMMIT_RE = re.compile(
    r"\b(?:"
    r"I'?ll\b|I will\b|I can\b|let me\b|"
    r"I'?m going to\b|I need to\b|"
    r"I'?ll (?:send|check|call|email|text|share|look|get|make|set|"
    r"schedule|confirm|handle|ask|reach|follow|take|be|bring|pick|"
    r"come|go|write|update|add|fix|review|help|find|try)\b|"
    r"I'?ll get (?:back|you|it|that)\b|"
    r"I will (?:send|check|call|email|text|share|get|make|set|schedule|confirm)\b|"
    r"going to\b|gonna\b"
    r")",
    re.IGNORECASE,
)

_PLAN_RE = re.compile(
    r"\b(?:let's|we should|we can|can we|should we|we'll|we will|"
    r"how about|what about|meet(?:ing)? (?:at|on|next|this)|"
    r"call (?:at|on|next|this|you)|talk (?:at|on|this|next))\b",
    re.IGNORECASE,
)

_DATE_RE = re.compile(
    r"\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|"
    r"tomorrow|tonight|today|this week|next week|this weekend|next weekend|"
    r"Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember?)?)"
    r"|\b\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?"
    r"|\bat \d{1,2}(?::\d{2})?\s*(?:am|pm)\b",
    re.IGNORECASE,
)


def _extract_action_items(messages: list[dict]) -> list[dict]:
    items: list[dict] = []
    for msg in messages:
        if _is_noise(msg["text"]):
            continue
        text = msg["text"]
        m = _COMMIT_RE.search(text) or _PLAN_RE.search(text)
        if not m:
            continue

        # Extract the sentence/line that actually contains the matched phrase
        # so we show "I'll book the flights" not "Perfect" (the sentence before it).
        match_pos = m.start()
        # Find line boundaries around the match
        line_start = text.rfind("\n", 0, match_pos)
        line_start = 0 if line_start == -1 else line_start + 1
        line_end = text.find("\n", match_pos)
        line_end = len(text) if line_end == -1 else line_end
        matched_line = text[line_start:line_end].strip()

        # Skip if the matched line is too short or emoji-only to be meaningful
        printable = re.sub(r"[^\x20-\x7e\u00a0-\uffff]", "", matched_line).strip()
        if len(printable) < 8:
            continue

        label = "Andres" if msg["is_andres"] else msg["sender"]
        day = msg["date"].strftime("%b %d") if msg["date"] else msg["date_str"]
        short = matched_line[:220]
        items.append(
            {"actor": label, "text": short, "date": day, "is_andres": msg["is_andres"]}
        )
    return items


def _extract_date_mentions(messages: list[dict]) -> list[str]:
    seen: set[str] = set()
    mentions: list[str] = []
    for msg in messages:
        if _is_noise(msg["text"]):
            continue
        for m in _DATE_RE.finditer(msg["text"]):
            val = m.group(0).strip()
            if val.lower() not in seen and len(val) > 2:
                seen.add(val.lower())
                mentions.append(val)
    return mentions[:20]


# ── Markdown renderer ─────────────────────────────────────────────────────────

def _slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _contact_wiki_path(contact_name: str) -> str:
    """Best-guess wiki path for the contact."""
    return f"wiki/people/{_slugify(contact_name)}"


def render_markdown(
    contact_name: str,
    source_path: Path,
    messages: list[dict],
    action_items: list[dict],
    date_mentions: list[str],
) -> str:
    clean = [m for m in messages if not _is_noise(m["text"])]
    senders = Counter(m["sender"] for m in clean)
    dates = [m["date"] for m in clean if m["date"]]
    date_min = min(dates).strftime("%Y-%m-%d") if dates else "unknown"
    date_max = max(dates).strftime("%Y-%m-%d") if dates else "unknown"
    date_range = date_min if date_min == date_max else f"{date_min} to {date_max}"
    contact_wiki = _contact_wiki_path(contact_name)

    out: list[str] = []

    # ── Frontmatter ──
    out += [
        "---",
        "tags:",
        "  - graph/leaf",
        "type: whatsapp-chat",
        f'source: "{source_path.name}"',
        f'contact: "{contact_name}"',
        f'date_range: "{date_range}"',
        f"message_count: {len(clean)}",
        "---",
        "",
        f"# WhatsApp Chat with {contact_name}",
        "",
        f"**Type:** whatsapp-chat  ",
        f"**Last updated:** {date_max}  ",
        f"**Source:** [[raw/{source_path.name}]]  ",
        f"**Related:** [[{contact_wiki}]], [[wiki/andres/ANDRES]]  ",
        f"**Messages:** {len(clean)} (noise-stripped from {len(messages)} raw)  ",
        f"**Date range:** {date_range}",
        "",
        "---",
        "",
    ]

    # ── Participants ──
    out += ["## Participants", ""]
    for sender, count in senders.most_common():
        wiki_path = "wiki/andres/ANDRES" if _is_andres(sender) else contact_wiki
        out.append(f"- **[[{wiki_path}|{sender}]]** — {count} messages")
    out.append("")

    # ── Action Items ──
    out += ["## Action Items", ""]
    if action_items:
        for item in action_items:
            checkbox = "- [ ]"
            out.append(f"{checkbox} **{item['actor']}**: {item['text']} _(mentioned {item['date']})_")
    else:
        out.append("_No explicit commitments detected._")
    out.append("")

    # ── Date / Time Mentions ──
    if date_mentions:
        out += ["## Dates & Times Mentioned", ""]
        for d in date_mentions:
            out.append(f"- {d}")
        out.append("")

    # ── Conversation (grouped by day, truncated) ──
    out += ["## Conversation (cleaned)", ""]
    by_day: dict[str, list[dict]] = defaultdict(list)
    for msg in clean:
        key = msg["date"].strftime("%Y-%m-%d") if msg["date"] else "unknown"
        by_day[key].append(msg)

    MAX_DAYS = 10
    MAX_PER_DAY = 30

    for day_key in sorted(by_day)[:MAX_DAYS]:
        day_msgs = by_day[day_key]
        try:
            label = datetime.strptime(day_key, "%Y-%m-%d").strftime("%b %d, %Y")
        except ValueError:
            label = day_key
        out.append(f"**{label}**")
        out.append("")
        for msg in day_msgs[:MAX_PER_DAY]:
            text = msg["text"].replace("\n", " ").strip()
            if len(text) > 320:
                text = text[:320] + "…"
            out.append(f"> **{msg['sender']}**: {text}")
        if len(day_msgs) > MAX_PER_DAY:
            out.append(f"> _{len(day_msgs) - MAX_PER_DAY} more messages not shown…_")
        out.append("")

    remaining = len(by_day) - MAX_DAYS
    if remaining > 0:
        out.append(f"_({remaining} more days of conversation not shown)_")
        out.append("")

    # ── Summary / Connections ──
    out += [
        "## Summary",
        "",
        f"WhatsApp conversation between Andres and [[{contact_wiki}|{contact_name}]].",
        f"See action items above. Full date range: {date_range}.",
        "",
        "## Connections",
        "",
        f"- [[{contact_wiki}]]",
        "- [[wiki/andres/ANDRES]]",
        "",
        "## Moil Relevance",
        "",
        "Personal contact. Review action items and update the people page with any new context.",
    ]

    return "\n".join(out) + "\n"


# ── Filename helpers ──────────────────────────────────────────────────────────

_WA_NAME_RE = re.compile(
    r"^WhatsApp\s+Chat\s+(?:with\s+|[-–]\s*)(.+)$", re.IGNORECASE
)


def extract_contact_name(path: Path) -> str:
    m = _WA_NAME_RE.match(path.stem)
    return m.group(1).strip() if m else path.stem


def is_whatsapp_export(path: Path) -> bool:
    """True if the path looks like a WhatsApp export by name OR content."""
    if _WA_NAME_RE.match(path.stem):
        return True
    if path.suffix.lower() != ".txt":
        return False
    # Content sniff: first real line matches [d/d/yy, ...] pattern
    try:
        first = ""
        with path.open(encoding="utf-8", errors="replace") as f:
            for line in f:
                line = _INVIS_RE.sub("", line).strip()
                if line:
                    first = line
                    break
        return bool(re.match(r"^\[\d{1,2}/\d{1,2}/\d{2,4},", first))
    except OSError:
        return False


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Parse WhatsApp chat export into Moil Brain markdown"
    )
    ap.add_argument("file", help="WhatsApp .txt export file")
    ap.add_argument("--kb-dir", default=None, help="KB root (auto-detected if omitted)")
    ap.add_argument("--stdout", action="store_true", help="Print markdown to stdout, skip writing file")
    args = ap.parse_args()

    path = Path(args.file).expanduser().resolve()
    if not path.exists():
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        sys.exit(1)

    # Resolve KB dir
    if args.kb_dir:
        kb_dir = Path(args.kb_dir).expanduser().resolve()
    else:
        kb_dir = REPO
        if not (kb_dir / "wiki").is_dir():
            kb_dir = Path("/Users/jarvisurrego/My Brain/knowledge-base")

    raw_dir = kb_dir / "quartz" / "content" / "raw"

    # Parse
    contact = extract_contact_name(path)
    print(f"[whatsapp_parse] Contact: {contact}", file=sys.stderr)

    messages = parse_whatsapp(path)
    if messages is None:
        print(f"ERROR: Not a WhatsApp export or could not parse: {path}", file=sys.stderr)
        sys.exit(1)

    clean = [m for m in messages if not _is_noise(m["text"])]
    action_items = _extract_action_items(messages)
    date_mentions = _extract_date_mentions(messages)

    print(
        f"[whatsapp_parse] {len(messages)} raw → {len(clean)} clean messages, "
        f"{len(action_items)} action items",
        file=sys.stderr,
    )

    md = render_markdown(contact, path, messages, action_items, date_mentions)

    if args.stdout:
        print(md)
        return

    # Write output
    dates = [m["date"] for m in clean if m["date"]]
    latest = max(dates).strftime("%Y-%m-%d") if dates else datetime.now().strftime("%Y-%m-%d")
    out_name = f"whatsapp-{_slugify(contact)}-{latest}.md"
    out_path = raw_dir / out_name
    out_path.write_text(md, encoding="utf-8")

    print(f"[whatsapp_parse] Written: {out_path}", file=sys.stderr)

    # Print action items to stdout for the caller (brain-ingest.sh) to log
    if action_items:
        print(f"\nAction items from chat with {contact}:")
        for item in action_items:
            print(f"  [{item['actor']}] {item['text']} ({item['date']})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate wiki/index.md — TLDR master index across all hubs.

Reads every markdown file under wiki/, extracts a one-line TLDR
(from Summary section, first meaningful paragraph, or filename),
flags stubs (<150 words) with ⚠️, and groups by hub.

Written to wiki/index.md. sync_wiki.sh mirrors to quartz/content/wiki/index.md.
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"
OUT = WIKI / "index.md"

HUB_ORDER = [
    ("andres", "Andres"),
    ("moil", "Moil"),
    ("people", "People"),
    ("orgs", "Organizations"),
    ("concepts", "Concepts"),
    ("meetings", "Meetings"),
    ("summaries", "Summaries"),
    ("minds", "Minds"),
    ("radar", "Radar"),
]

STUB_WORDS = 150
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def strip_frontmatter(text: str) -> tuple[str, str]:
    m = FRONTMATTER_RE.match(text)
    if m:
        return m.group(1), text[m.end():]
    return "", text


def word_count(body: str) -> int:
    plain = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)
    plain = re.sub(r"[#*_`\[\]()>|-]", " ", plain)
    return len([w for w in plain.split() if w.strip()])


def extract_title(fm: str, body: str, slug: str) -> str:
    m = re.search(r"^title:\s*(.+)$", fm, re.MULTILINE)
    if m:
        return m.group(1).strip().strip("\"'")
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return slug.replace("-", " ").title()


def extract_tldr(body: str) -> str:
    m = re.search(
        r"(?:^|\n)##\s+(?:Summary|TLDR|TL;DR|Overview)\s*\n(.+?)(?=\n##|\Z)",
        body,
        re.IGNORECASE | re.DOTALL,
    )
    if m:
        text = m.group(1).strip()
    else:
        text = body

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith(("#", "---", "**Type:", "**Last", "**Source:", "**Related:", "|")):
            continue
        if line.startswith(("- ", "* ", "+ ")):
            line = line[2:].strip()
        line = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", line)
        line = re.sub(r"\[\[([^\]]+)\]\]", r"\1", line)
        line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
        line = re.sub(r"\*([^*]+)\*", r"\1", line)
        line = re.sub(r"`([^`]+)`", r"\1", line)
        if len(line) < 10:
            continue
        if len(line) > 160:
            line = line[:157].rsplit(" ", 1)[0] + "…"
        return line
    return ""


def slug_to_link(path: Path) -> str:
    rel = path.relative_to(WIKI).with_suffix("")
    return str(rel).replace("\\", "/")


def main() -> int:
    pages_by_hub: dict[str, list[tuple[str, str, str, bool]]] = {}
    total = 0
    stubs = 0

    for md in sorted(WIKI.rglob("*.md")):
        if md.name.lower() in {"readme.md", "index.md"}:
            continue
        rel = md.relative_to(WIKI)
        hub = rel.parts[0] if len(rel.parts) > 1 else "_root"
        try:
            raw = md.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, body = strip_frontmatter(raw)
        wc = word_count(body)
        is_stub = wc < STUB_WORDS
        title = extract_title(fm, body, md.stem)
        tldr = extract_tldr(body)
        if not tldr:
            tldr = "(no summary yet)"
        link = slug_to_link(md)
        pages_by_hub.setdefault(hub, []).append((title, link, tldr, is_stub))
        total += 1
        if is_stub:
            stubs += 1

    hub_count = sum(1 for h, _ in HUB_ORDER if h in pages_by_hub)
    today = date.today().isoformat()

    lines: list[str] = []
    lines.append("---")
    lines.append("title: Brain Index")
    lines.append("tags:")
    lines.append("  - graph/leaf")
    lines.append("---")
    lines.append("")
    lines.append("# Brain Index")
    lines.append("")
    lines.append(
        f"*{total} pages across {hub_count} hubs "
        f"| {stubs} stubs flagged ⚠️ "
        f"| Last updated: {today}*"
    )
    lines.append("")
    lines.append(
        "This is the master index of everything in the Brain. "
        "Each entry is a one-line TLDR. Tap any link to go deep."
    )
    lines.append("")

    rendered_hubs = set()
    for hub_key, hub_label in HUB_ORDER:
        pages = pages_by_hub.get(hub_key)
        if not pages:
            continue
        rendered_hubs.add(hub_key)
        pages.sort(key=lambda p: p[0].lower())
        lines.append(f"## {hub_label} ({len(pages)} pages)")
        lines.append("")
        for title, link, tldr, is_stub in pages:
            marker = " ⚠️ stub — needs expansion" if is_stub else ""
            lines.append(f"- [[{link}|{title}]] — {tldr}{marker}")
        lines.append("")

    extra = sorted(h for h in pages_by_hub if h not in rendered_hubs)
    for hub_key in extra:
        pages = pages_by_hub[hub_key]
        pages.sort(key=lambda p: p[0].lower())
        label = hub_key.title() if hub_key != "_root" else "Root"
        lines.append(f"## {label} ({len(pages)} pages)")
        lines.append("")
        for title, link, tldr, is_stub in pages:
            marker = " ⚠️ stub — needs expansion" if is_stub else ""
            lines.append(f"- [[{link}|{title}]] — {tldr}{marker}")
        lines.append("")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[gen-wiki-index] wrote {OUT} — {total} pages, {stubs} stubs, {hub_count} hubs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

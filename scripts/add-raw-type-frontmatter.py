#!/usr/bin/env python3
"""Add `type:` frontmatter to raw/ markdown files that lack it.

Skips files already containing `type:` in frontmatter.
Skips the new `clippings/` folder — those files already carry a type
from the Obsidian Web Clipper template.

Inference rules (by path / filename):
- raw/**/briefings/**         → briefing
- raw/**/content-calendar/**  → calendar
- raw/**/outputs/**           → output
- raw/**/summaries/**         → summary
- raw/**/meetings/**          → transcript
- raw/**/onedrive-transcripts/** → transcript
- filename starts with odtr-  → transcript
- filename contains teams-    → teams-message
- filename contains x-bookmarks → bookmark
- filename contains email-    → email
- filename contains briefing  → briefing
- otherwise                   → note
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def infer_type(path: Path) -> str:
    parts = {p.lower() for p in path.parts}
    name = path.name.lower()
    if "briefings" in parts:
        return "briefing"
    if "content-calendar" in parts:
        return "calendar"
    if "outputs" in parts:
        return "output"
    if "summaries" in parts:
        return "summary"
    if "meetings" in parts or "onedrive-transcripts" in parts:
        return "transcript"
    if name.startswith("odtr-"):
        return "transcript"
    if "teams-transcript" in name:
        return "transcript"
    if "teams-" in name:
        return "teams-message"
    if "x-bookmarks" in name:
        return "bookmark"
    if "email-" in name or "outlook-" in name or "imessages-" in name:
        return "email"
    if "briefing" in name:
        return "briefing"
    if "facebook-" in name:
        return "social"
    if "hive-" in name or "buda-hive" in name:
        return "program-doc"
    if "guide" in name or "extraction" in name:
        return "reference"
    return "note"


def has_type_field(fm: str) -> bool:
    return bool(re.search(r"^type:\s*\S", fm, re.MULTILINE))


def process_file(path: Path, dry_run: bool = False) -> tuple[bool, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False, "skip-binary"

    inferred = infer_type(path)
    m = FRONTMATTER_RE.match(text)
    if m:
        fm = m.group(1)
        if has_type_field(fm):
            return False, "has-type"
        new_fm = fm.rstrip() + f"\ntype: {inferred}"
        new_text = f"---\n{new_fm}\n---\n" + text[m.end():]
    else:
        new_text = f"---\ntype: {inferred}\n---\n\n" + text

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True, inferred


def main(argv: list[str]) -> int:
    dry = "--dry-run" in argv
    positional = [a for a in argv if not a.startswith("--")]
    raw = Path(positional[0]).resolve() if positional else REPO / "raw"
    if not raw.exists():
        print(f"[add-type] path not found: {raw}", file=sys.stderr)
        return 1
    updated = 0
    skipped = 0
    by_type: dict[str, int] = {}
    errors: list[str] = []

    for md in raw.rglob("*.md"):
        # Skip new clippings zone — template already provides type
        if "clippings" in {p.lower() for p in md.relative_to(raw).parts}:
            continue
        try:
            changed, info = process_file(md, dry_run=dry)
        except Exception as e:
            errors.append(f"{md}: {e}")
            continue
        if changed:
            updated += 1
            by_type[info] = by_type.get(info, 0) + 1
        else:
            skipped += 1

    print(f"[add-type] scanned {updated + skipped} files, "
          f"{updated} updated, {skipped} skipped (already had type or binary)")
    for t, n in sorted(by_type.items(), key=lambda kv: -kv[1]):
        print(f"  {t}: {n}")
    for e in errors:
        print(f"  ERROR: {e}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

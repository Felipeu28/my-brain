#!/usr/bin/env python3
"""
kb-health.py — Weekly knowledge-base audit.

Detects: duplicate raw files, broken wikilinks, orphan pages, MEMORY.md
overflow, frontmatter violations, stale pages, index.md drift.

Usage:
  python3 scripts/kb-health.py                    # print report to stdout
  python3 scripts/kb-health.py --write            # also write to outputs/health/
  python3 scripts/kb-health.py --fail-on-errors   # exit 1 if errors found
"""

import os
import sys
import re
import hashlib
import argparse
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

KB_DIR = Path("/Users/jarvisurrego/My Brain/knowledge-base")
WIKI_DIR = KB_DIR / "wiki"
RAW_DIR = KB_DIR / "raw"
MEMORY_FILE = KB_DIR / "MEMORY.md"
INDEX_FILE = KB_DIR / "index.md"
OUTPUT_DIR = KB_DIR / "outputs" / "health"

# -------- Utilities --------

def read_file(p):
    try:
        return p.read_text()
    except Exception:
        return ""


def get_frontmatter(content):
    """Extract YAML frontmatter as dict. Returns empty dict if none."""
    if not content.startswith("---"):
        return {}
    try:
        end = content.index("---", 3)
    except ValueError:
        return {}
    block = content[3:end]
    fm = {}
    current_key = None
    for line in block.splitlines():
        line = line.rstrip()
        if not line:
            continue
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            k, _, v = line.partition(":")
            current_key = k.strip()
            v = v.strip()
            fm[current_key] = v if v else []
        elif line.startswith("  -") or line.startswith("-"):
            val = line.lstrip(" -").strip()
            if current_key and isinstance(fm.get(current_key), list):
                fm[current_key].append(val)
            elif current_key:
                fm[current_key] = [val]
    return fm


def extract_wikilinks(content):
    """Return list of wikilink targets in a page."""
    # Matches [[target]] or [[target|display]]
    return [m.group(1).strip() for m in re.finditer(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", content)]


_bare_name_cache = None

def _build_bare_name_index():
    global _bare_name_cache
    if _bare_name_cache is not None:
        return _bare_name_cache
    _bare_name_cache = {}
    for p in WIKI_DIR.rglob("*.md"):
        _bare_name_cache.setdefault(p.stem, p)
    return _bare_name_cache


def wikilink_to_path(target):
    """Resolve a wikilink target to a candidate file path (relative to KB_DIR)."""
    t = target.strip().lstrip("/")
    # Strip any trailing backslashes (from broken escaping)
    t = t.rstrip("\\")
    # Strip heading anchors (Obsidian-style: [[page#section]])
    if "#" in t:
        t = t.split("#", 1)[0]
    # Template placeholders like `<partner>` or `<name>` should be treated as non-links
    if "<" in t or ">" in t:
        return None
    if not t:
        return None
    if not t.endswith(".md"):
        t_md = t + ".md"
    else:
        t_md = t
    candidates = [
        KB_DIR / t_md,
        KB_DIR / t / "index.md",
        KB_DIR / t / "README.md",
        # Obsidian-style paths without wiki/ prefix (e.g. "andres/ANDRES")
        WIKI_DIR / t_md,
        WIKI_DIR / t / "index.md",
        WIKI_DIR / t / "README.md",
    ]
    for c in candidates:
        if c.exists():
            return c
    # Obsidian-style bare name resolution (e.g. [[mariana-rodriguez]])
    if "/" not in t:
        bare_index = _build_bare_name_index()
        stem = t[:-3] if t.endswith(".md") else t
        if stem in bare_index:
            return bare_index[stem]
    return None


# -------- Checks --------

def check_duplicate_raw_files():
    """MD5 dedupe across all raw/ files."""
    hashes = defaultdict(list)
    for root, _, files in os.walk(RAW_DIR):
        for f in files:
            if not f.endswith(".md"):
                continue
            p = Path(root) / f
            try:
                h = hashlib.md5(p.read_bytes()).hexdigest()
                hashes[h].append(str(p.relative_to(KB_DIR)))
            except Exception:
                pass
    dupes = {h: paths for h, paths in hashes.items() if len(paths) > 1}
    return dupes


def check_broken_wikilinks():
    """Scan every wiki page for wikilinks that don't resolve.

    Returns (broken_wiki, broken_raw) — split so raw/ misses (which mean a
    wiki page references a raw source that was never ingested or has been
    renamed) can be reported separately.
    """
    broken_wiki = defaultdict(list)
    broken_raw = defaultdict(list)
    template_patterns = {"wiki/concepts/X", "wiki/moil/Z", "wiki/people/Y",
                         "wiki/folder/slug", "Display Label", "wiki/...",
                         "wikilinks", "links", "target"}
    for p in WIKI_DIR.rglob("*.md"):
        content = read_file(p)
        for link in extract_wikilinks(content):
            if link in template_patterns:
                continue
            if wikilink_to_path(link):
                continue
            bucket = broken_raw if link.startswith("raw/") else broken_wiki
            bucket[str(p.relative_to(KB_DIR))].append(link)
    return broken_wiki, broken_raw


def check_orphan_wiki_pages():
    """Find wiki pages with 0 inbound wikilinks."""
    all_pages = {p.relative_to(KB_DIR) for p in WIKI_DIR.rglob("*.md")}
    referenced = set()
    for p in WIKI_DIR.rglob("*.md"):
        content = read_file(p)
        for link in extract_wikilinks(content):
            target = wikilink_to_path(link)
            if target:
                try:
                    referenced.add(target.relative_to(KB_DIR))
                except ValueError:
                    pass
    # Index + ANDRES + READMEs are allowed to be orphans (they're entry points)
    exempt_patterns = ["README.md", "index.md", "ANDRES.md"]
    orphans = []
    for p in all_pages:
        if p in referenced:
            continue
        if any(p.name == ex for ex in exempt_patterns):
            continue
        orphans.append(str(p))
    return sorted(orphans)


def check_frontmatter_compliance():
    """Every wiki page needs graph/ tier tag; people pages need person/ sub-tag."""
    violations = []
    for p in WIKI_DIR.rglob("*.md"):
        if p.name in ("README.md", "index.md"):
            continue
        content = read_file(p)
        fm = get_frontmatter(content)
        tags = fm.get("tags", [])
        if not isinstance(tags, list):
            tags = []
        graph_tags = [t for t in tags if t.startswith("graph/")]
        if len(graph_tags) != 1:
            violations.append((str(p.relative_to(KB_DIR)), f"graph tier tag missing or duplicated (found: {graph_tags})"))
        if "people/" in str(p):
            person_tags = [t for t in tags if t.startswith("person/")]
            if len(person_tags) != 1:
                violations.append((str(p.relative_to(KB_DIR)), f"person sub-type tag missing or duplicated (found: {person_tags})"))
    return violations


def check_memory_size():
    """MEMORY.md should be under 200 lines."""
    if not MEMORY_FILE.exists():
        return None
    lines = MEMORY_FILE.read_text().splitlines()
    return len(lines)


def check_index_accuracy():
    """index.md's claimed counts vs actual."""
    if not INDEX_FILE.exists():
        return {}
    content = INDEX_FILE.read_text()
    actual = {
        "wiki": len(list(WIKI_DIR.rglob("*.md"))),
        "raw": len(list(RAW_DIR.rglob("*.md"))),
    }
    for folder in ["people", "concepts", "meetings", "orgs", "moil", "summaries", "minds", "radar"]:
        d = WIKI_DIR / folder
        if d.exists():
            actual[folder] = len(list(d.rglob("*.md")))

    # Parse claimed counts from index.md header
    claimed = {}
    m = re.search(r"Total wiki pages:\*\*\s*(\d+)", content)
    if m:
        claimed["wiki"] = int(m.group(1))
    m = re.search(r"Raw sources[^:]*:\*\*\s*(\d+)", content)
    if m:
        claimed["raw"] = int(m.group(1))

    drift = {}
    for k in claimed:
        if k in actual and claimed[k] != actual[k]:
            drift[k] = (claimed[k], actual[k])
    return {"actual": actual, "claimed": claimed, "drift": drift}


def check_stale_pages(days=90):
    """Find wiki pages with Last updated: > N days ago."""
    cutoff = datetime.now() - timedelta(days=days)
    stale = []
    for p in WIKI_DIR.rglob("*.md"):
        content = read_file(p)
        m = re.search(r"\*\*Last updated:\*\*\s*(\d{4}-\d{2}-\d{2})", content)
        if m:
            try:
                dt = datetime.strptime(m.group(1), "%Y-%m-%d")
                if dt < cutoff:
                    stale.append((str(p.relative_to(KB_DIR)), m.group(1)))
            except ValueError:
                pass
    return sorted(stale, key=lambda x: x[1])


def check_sync_health():
    """Confirm wiki/ and quartz/content/wiki/ have identical file counts."""
    wiki_count = len(list(WIKI_DIR.rglob("*.md")))
    quartz_wiki = KB_DIR / "quartz" / "content" / "wiki"
    if not quartz_wiki.exists():
        return "MISSING quartz/content/wiki/"
    quartz_count = len(list(quartz_wiki.rglob("*.md")))
    if wiki_count != quartz_count:
        return f"OUT OF SYNC: wiki/={wiki_count}, quartz/content/wiki/={quartz_count}"
    return "OK"


# -------- Report --------

def generate_report():
    """Run all checks. Return (report_text, error_count)."""
    lines = []
    errors = 0
    warnings = 0

    lines.append(f"# KB Health Report — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")

    # 1. Raw duplicates
    dupes = check_duplicate_raw_files()
    lines.append("## 1. Duplicate raw files (MD5-identical)")
    if not dupes:
        lines.append("✅ None")
    else:
        errors += sum(len(paths) - 1 for paths in dupes.values())
        lines.append(f"❌ {len(dupes)} hash groups, {errors} duplicates to delete:")
        for h, paths in list(dupes.items())[:20]:
            lines.append(f"  - {' | '.join(paths)}")
    lines.append("")

    # 2. Broken wikilinks
    broken, broken_raw = check_broken_wikilinks()
    total_broken = sum(len(v) for v in broken.values())
    lines.append("## 2. Broken wikilinks")
    if total_broken == 0:
        lines.append("✅ None")
    else:
        errors += total_broken
        lines.append(f"❌ {total_broken} broken links across {len(broken)} pages:")
        for src, targets in sorted(broken.items())[:30]:
            lines.append(f"  - `{src}` → {', '.join(targets)}")
        if len(broken) > 30:
            lines.append(f"  - ...and {len(broken) - 30} more pages")
    lines.append("")

    # 2b. Broken raw/ wikilinks (404s on the deployed site)
    total_broken_raw = sum(len(v) for v in broken_raw.values())
    lines.append("## 2b. Broken raw/ wikilinks (will 404 on deployed site)")
    if total_broken_raw == 0:
        lines.append("✅ None")
    else:
        errors += total_broken_raw
        lines.append(f"❌ {total_broken_raw} broken raw/ links across {len(broken_raw)} pages:")
        for src, targets in sorted(broken_raw.items())[:30]:
            lines.append(f"  - `{src}` → {', '.join(targets)}")
        if len(broken_raw) > 30:
            lines.append(f"  - ...and {len(broken_raw) - 30} more pages")
    lines.append("")

    # 3. Orphan pages
    orphans = check_orphan_wiki_pages()
    lines.append(f"## 3. Orphan wiki pages (0 inbound wikilinks)")
    if not orphans:
        lines.append("✅ None")
    else:
        warnings += len(orphans)
        lines.append(f"⚠️  {len(orphans)} orphans:")
        for o in orphans[:30]:
            lines.append(f"  - `{o}`")
        if len(orphans) > 30:
            lines.append(f"  - ...and {len(orphans) - 30} more")
    lines.append("")

    # 4. Frontmatter violations
    fm_violations = check_frontmatter_compliance()
    lines.append("## 4. Frontmatter violations")
    if not fm_violations:
        lines.append("✅ None")
    else:
        errors += len(fm_violations)
        lines.append(f"❌ {len(fm_violations)} violations:")
        for path, msg in fm_violations[:20]:
            lines.append(f"  - `{path}` — {msg}")
    lines.append("")

    # 5. MEMORY.md size
    mem_size = check_memory_size()
    lines.append("## 5. MEMORY.md size (hard limit: 200 lines)")
    if mem_size is None:
        lines.append("❌ MEMORY.md not found")
        errors += 1
    elif mem_size > 200:
        lines.append(f"❌ {mem_size} lines — OVER LIMIT")
        errors += 1
    else:
        lines.append(f"✅ {mem_size} lines")
    lines.append("")

    # 6. index.md accuracy
    idx = check_index_accuracy()
    lines.append("## 6. index.md stats drift")
    if idx.get("drift"):
        warnings += len(idx["drift"])
        lines.append(f"⚠️  {len(idx['drift'])} counts drifted:")
        for k, (claimed, actual) in idx["drift"].items():
            lines.append(f"  - {k}: claims {claimed}, actual {actual}")
    else:
        lines.append(f"✅ Matches (wiki={idx.get('actual', {}).get('wiki')}, raw={idx.get('actual', {}).get('raw')})")
    lines.append("")

    # 7. Sync health
    sync = check_sync_health()
    lines.append("## 7. Sync health (wiki/ ↔ quartz/content/wiki/)")
    if sync == "OK":
        lines.append("✅ In sync")
    else:
        errors += 1
        lines.append(f"❌ {sync}")
    lines.append("")

    # 8. Stale pages
    stale = check_stale_pages(90)
    lines.append("## 8. Stale pages (Last updated > 90 days ago)")
    if not stale:
        lines.append("✅ None")
    else:
        lines.append(f"ℹ️  {len(stale)} pages (informational):")
        for path, date in stale[:10]:
            lines.append(f"  - `{path}` ({date})")
        if len(stale) > 10:
            lines.append(f"  - ...and {len(stale) - 10} more")
    lines.append("")

    # Summary
    lines.append("---")
    lines.append("")
    lines.append(f"**Summary:** {errors} errors · {warnings} warnings")
    if errors == 0 and warnings == 0:
        lines.append("🎉 Brain is clean.")
    elif errors == 0:
        lines.append("✅ No errors. Warnings are informational.")
    else:
        lines.append("❌ Errors need attention.")

    return "\n".join(lines), errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="Also write to outputs/health/")
    ap.add_argument("--fail-on-errors", action="store_true", help="Exit 1 if errors found")
    args = ap.parse_args()

    report, errors = generate_report()
    print(report)

    if args.write:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        today = datetime.now().strftime("%Y-%m-%d")
        out_file = OUTPUT_DIR / f"kb-health-{today}.md"
        latest = OUTPUT_DIR / "kb-health-latest.md"
        out_file.write_text(report)
        latest.write_text(report)
        print(f"\nWritten to {out_file.relative_to(KB_DIR)}", file=sys.stderr)

    if args.fail_on_errors and errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()

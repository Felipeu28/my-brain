#!/usr/bin/env python3
"""
Add tier tags (graph/hub, graph/spoke, graph/leaf) to all wiki pages.
Run once, then automation scripts handle new pages going forward.

Usage: python3 scripts/add-tier-tags.py [--dry-run]
"""

import os
import re
import sys
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv

WIKI_DIR = Path(__file__).parent.parent / "wiki"
QUARTZ_WIKI_DIR = Path(__file__).parent.parent / "quartz" / "content" / "wiki"

# ── Hub pages: the strategic core (~10 pages) ────────────────────────────────
HUB_PAGES = {
    "moil/positioning",
    "moil/gtm",
    "moil/icp",
    "moil/customers",
    "moil/product-roadmap",
    "moil/metrics",
    "concepts/buda-hive",
    "people/jennifer-storm",
    "people/jacob-oluwole",
    "people/adeleke-tolulope",
}

# ── Leaf folders: everything in these is leaf by default ──────────────────────
LEAF_FOLDERS = {"meetings", "summaries"}

# ── Leaf-by-name patterns ────────────────────────────────────────────────────
LEAF_NAME_PATTERNS = [
    "batch",       # batch meeting pages
    "README",      # folder index pages (not graph-worthy)
    "index",       # folder index pages
]

# ── Spoke overrides: specific meeting pages that ARE important ────────────────
SPOKE_OVERRIDES = {
    "meetings/2025-03-28-jacob-andres-pivot-ai-tools",       # The pivot meeting
    "meetings/2024-10-30-moneta-ventures-investor-panel",     # Investor pitch
    "meetings/2025-05-21-ai-advisory-azure-foundry",          # Azure AI Foundry
    "meetings/2025-01-08-nvidia-inception-onboarding",        # Nvidia Inception
    "meetings/2025-05-15-zachary-barker-wyatt-hook-enterprise", # Tampa Bay enterprise
    "meetings/2024-10-31-monica-munoz-andry-gahcc-partnership", # GAHCC
    "meetings/2024-11-13-txor-moil-partnership-call",         # TXOR origin
}


def get_tier(rel_path: str) -> str:
    """Determine tier for a wiki page based on path."""
    # Strip .md extension
    slug = rel_path.replace(".md", "").replace("\\", "/")

    # Hub check first
    if slug in HUB_PAGES:
        return "graph/hub"

    # Spoke overrides (important meetings)
    if slug in SPOKE_OVERRIDES:
        return "graph/spoke"

    # Leaf folders
    folder = slug.split("/")[0] if "/" in slug else ""
    if folder in LEAF_FOLDERS:
        return "graph/leaf"

    # Leaf name patterns
    name = slug.split("/")[-1] if "/" in slug else slug
    for pattern in LEAF_NAME_PATTERNS:
        if pattern in name:
            return "graph/leaf"

    # Default: spoke (concepts, people, minds, orgs, moil, radar)
    return "graph/spoke"


def add_frontmatter_tag(filepath: Path, tag: str) -> bool:
    """Add or update tags in YAML frontmatter. Returns True if file was modified."""
    content = filepath.read_text(encoding="utf-8")

    # Check if file already has YAML frontmatter
    if content.startswith("---"):
        # Find the closing ---
        end = content.find("---", 3)
        if end == -1:
            return False

        frontmatter = content[3:end]
        rest = content[end + 3:]

        # Check if tags already exist
        if "tags:" in frontmatter:
            # Check if this specific tag is already there
            if tag in frontmatter:
                return False
            # Replace tags line
            frontmatter = re.sub(
                r"tags:\s*\[([^\]]*)\]",
                lambda m: f"tags: [{m.group(1)}, {tag}]" if m.group(1).strip() else f"tags: [{tag}]",
                frontmatter,
            )
        else:
            # Add tags field before the closing ---
            frontmatter = frontmatter.rstrip() + f"\ntags:\n  - {tag}\n"

        new_content = f"---{frontmatter}---{rest}"
    else:
        # No frontmatter — prepend it
        new_content = f"---\ntags:\n  - {tag}\n---\n{content}"

    if new_content != content:
        if not DRY_RUN:
            filepath.write_text(new_content, encoding="utf-8")
        return True
    return False


def process_directory(wiki_dir: Path, label: str):
    """Process all .md files in a wiki directory."""
    counts = {"hub": 0, "spoke": 0, "leaf": 0, "skipped": 0}

    for md_file in sorted(wiki_dir.rglob("*.md")):
        rel = str(md_file.relative_to(wiki_dir)).replace("\\", "/")

        # Skip hidden/special files
        if rel.startswith(".") or rel.startswith("_"):
            continue

        tier = get_tier(rel)
        short_tier = tier.split("/")[1]

        modified = add_frontmatter_tag(md_file, tier)
        if modified:
            counts[short_tier] += 1
            print(f"  [{short_tier.upper():5s}] {rel}")
        else:
            counts["skipped"] += 1

    print(f"\n  {label} results: {counts['hub']} hub, {counts['spoke']} spoke, {counts['leaf']} leaf, {counts['skipped']} already tagged")
    return counts


def main():
    if DRY_RUN:
        print("DRY RUN — no files will be modified\n")

    print(f"Processing wiki/ ...")
    c1 = process_directory(WIKI_DIR, "wiki/")

    print(f"\nProcessing quartz/content/wiki/ ...")
    c2 = process_directory(QUARTZ_WIKI_DIR, "quartz/content/wiki/")

    total = c1["hub"] + c1["spoke"] + c1["leaf"]
    print(f"\nDone. Tagged {total} pages in wiki/ ({c1['hub']} hub, {c1['spoke']} spoke, {c1['leaf']} leaf)")
    print(f"Tagged {c2['hub'] + c2['spoke'] + c2['leaf']} pages in quartz/content/wiki/")


if __name__ == "__main__":
    main()

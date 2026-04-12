#!/usr/bin/env python3
"""
Graph upgrade script — three operations:
1. Make Andres dashboard the center node (link to ALL hub/spoke pages)
2. Add people sub-type tags (person/team, person/customer, person/partner, person/personal)
3. Auto-graduate pages based on inbound link count

Usage: python3 scripts/upgrade-graph.py
"""

import os
import re
from pathlib import Path
from collections import Counter

WIKI_DIR = Path(__file__).parent.parent / "wiki"

# ── People classification ────────────────────────────────────────────────────
TEAM = {
    "jacob-oluwole", "adeleke-tolulope", "taiwo-ola-balogun",
    "abiodun-solomon", "sebastian-oviedo", "abel-esquivel-luna",
}

CUSTOMERS = {
    "megan-miller", "travis-sutherland", "inna-benyukhis",
    "daniel-guadiano", "anita-lansing", "dafne-gutierrez",
    "rick-bough", "wyatt-hook", "zane-gibson",
}

PARTNERS = {
    "jennifer-storm", "jacquie-martinez", "joshua-edmond",
    "casey-earley", "evangeline-sandoval", "kim-dowers",
    "hazim-mohamad", "monica-davidson", "monica-pena",
    "enrique-castro", "daniela-castillo-canavera", "shay-foley",
    "rosemary-gamez", "julian-sanchez", "david-levesque",
}

PERSONAL = {
    "mariana-rodriguez", "john-costilla", "mark-polanco",
}

VENDORS = {
    "paula-florez-estrada", "rodney-warner",
}


def add_tag_to_frontmatter(filepath: Path, tag: str) -> bool:
    """Add a tag to existing YAML frontmatter. Returns True if modified."""
    content = filepath.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False

    end = content.find("---", 3)
    if end == -1:
        return False

    frontmatter = content[3:end]
    rest = content[end + 3:]

    if tag in frontmatter:
        return False

    # Add tag to existing tags list
    if "tags:" in frontmatter:
        # Find the tags section and add new tag
        lines = frontmatter.split("\n")
        new_lines = []
        in_tags = False
        added = False
        for line in lines:
            new_lines.append(line)
            if line.strip() == "tags:":
                in_tags = True
            elif in_tags and line.strip().startswith("- "):
                if not added:
                    new_lines.append(f"  - {tag}")
                    added = True
                    in_tags = False
            elif in_tags and not line.strip().startswith("- "):
                in_tags = False
        frontmatter = "\n".join(new_lines)
    else:
        frontmatter = frontmatter.rstrip() + f"\ntags:\n  - {tag}\n"

    new_content = f"---{frontmatter}---{rest}"
    if new_content != content:
        filepath.write_text(new_content, encoding="utf-8")
        return True
    return False


def replace_tag(filepath: Path, old_tag: str, new_tag: str) -> bool:
    """Replace a tag in YAML frontmatter."""
    content = filepath.read_text(encoding="utf-8")
    if old_tag not in content:
        return False
    new_content = content.replace(f"- {old_tag}", f"- {new_tag}", 1)
    if new_content != content:
        filepath.write_text(new_content, encoding="utf-8")
        return True
    return False


def count_inbound_links() -> Counter:
    """Count how many pages link TO each page."""
    link_counts = Counter()
    for md_file in WIKI_DIR.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        # Find all wikilinks
        links = re.findall(r'\[\[wiki/([^\]|]+)', content)
        for link in links:
            # Normalize
            link = link.replace("\\", "/").rstrip("/")
            if link.endswith(".md"):
                link = link[:-3]
            link_counts[link] += 1
    return link_counts


def step1_people_subtypes():
    """Add person/team, person/customer, etc. tags to people pages."""
    print("\n=== Step 1: People sub-type tags ===")
    people_dir = WIKI_DIR / "people"
    count = 0

    for md_file in sorted(people_dir.glob("*.md")):
        slug = md_file.stem
        if slug in ("README", "index"):
            continue

        if slug in TEAM:
            tag = "person/team"
        elif slug in CUSTOMERS:
            tag = "person/customer"
        elif slug in PARTNERS:
            tag = "person/partner"
        elif slug in PERSONAL:
            tag = "person/personal"
        elif slug in VENDORS:
            tag = "person/vendor"
        else:
            tag = "person/contact"

        if add_tag_to_frontmatter(md_file, tag):
            print(f"  [{tag:18s}] {slug}")
            count += 1
        else:
            # Check if already has it
            content = md_file.read_text(encoding="utf-8")
            if tag in content:
                pass  # already tagged
            else:
                print(f"  [SKIP: no frontmatter] {slug}")

    print(f"  Tagged {count} people with sub-types")


def step2_auto_graduate():
    """Promote pages with high inbound link counts."""
    print("\n=== Step 2: Auto-graduation ===")
    link_counts = count_inbound_links()

    promotions = 0
    for slug, count in link_counts.most_common(50):
        filepath = WIKI_DIR / f"{slug}.md"
        if not filepath.exists():
            continue

        content = filepath.read_text(encoding="utf-8")

        # Promote spoke → hub if 8+ inbound links
        if "graph/spoke" in content and count >= 8:
            if replace_tag(filepath, "graph/spoke", "graph/hub"):
                print(f"  PROMOTED spoke→hub: {slug} ({count} inbound links)")
                promotions += 1

        # Promote leaf → spoke if 5+ inbound links
        elif "graph/leaf" in content and count >= 5:
            if replace_tag(filepath, "graph/leaf", "graph/spoke"):
                print(f"  PROMOTED leaf→spoke: {slug} ({count} inbound links)")
                promotions += 1

    print(f"  {promotions} pages promoted")

    # Report top pages by link count
    print("\n  Top 15 by inbound links:")
    for slug, count in link_counts.most_common(15):
        filepath = WIKI_DIR / f"{slug}.md"
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            tier = "hub" if "graph/hub" in content else "spoke" if "graph/spoke" in content else "leaf"
            print(f"    {count:3d} links → [{tier:5s}] {slug}")


def step3_center_node():
    """Make Andres dashboard the gravitational center by linking to everything important."""
    print("\n=== Step 3: Andres center node ===")

    dashboard = WIKI_DIR / "andres" / "dashboard.md"
    content = dashboard.read_text(encoding="utf-8")

    # Count existing wikilinks
    existing_links = set(re.findall(r'\[\[wiki/([^\]|]+)', content))
    print(f"  Dashboard currently links to {len(existing_links)} pages")

    # Collect all hub and spoke pages that should be linked
    all_important = set()
    for md_file in WIKI_DIR.rglob("*.md"):
        file_content = md_file.read_text(encoding="utf-8", errors="ignore")
        if "graph/hub" in file_content or "graph/spoke" in file_content:
            rel = str(md_file.relative_to(WIKI_DIR)).replace(".md", "").replace("\\", "/")
            if rel not in ("andres/dashboard", "README") and "/README" not in rel and "/index" not in rel:
                all_important.add(rel)

    missing = all_important - existing_links
    print(f"  Important pages NOT linked from dashboard: {len(missing)}")

    if missing:
        # Build a connections section with all missing links
        connections_section = "\n\n## All Connections\n\n"
        connections_section += "> These links make Andres the center of the graph. Every hub and spoke page connects here.\n\n"

        # Group by folder
        by_folder = {}
        for slug in sorted(missing):
            folder = slug.split("/")[0] if "/" in slug else "other"
            by_folder.setdefault(folder, []).append(slug)

        for folder in sorted(by_folder.keys()):
            connections_section += f"**{folder.title()}:** "
            links = [f"[[wiki/{s}]]" for s in sorted(by_folder[folder])]
            connections_section += " · ".join(links) + "\n\n"

        # Append to dashboard
        new_content = content.rstrip() + connections_section
        dashboard.write_text(new_content, encoding="utf-8")

        # Recount
        new_links = set(re.findall(r'\[\[wiki/([^\]|]+)', new_content))
        print(f"  Dashboard now links to {len(new_links)} pages (added {len(missing)})")


if __name__ == "__main__":
    step1_people_subtypes()
    step2_auto_graduate()
    step3_center_node()

    print("\n=== Done ===")
    print("Next: rsync wiki/ to quartz/content/wiki/, commit, push")

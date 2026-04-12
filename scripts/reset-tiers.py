#!/usr/bin/env python3
"""
Reset graph tiers with a curated, recency-aware approach.

Philosophy:
- Hub = things Andres touches weekly (10-15 pages MAX)
- Spoke = things that matter but aren't daily (active people, key concepts)
- Leaf = reference material, old meetings, summaries, batch pages

Concepts are almost never hub — they're reference material.
People who matter NOW are hub, regardless of link count.
"""

import re
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent / "wiki"
QUARTZ_WIKI_DIR = Path(__file__).parent.parent / "quartz" / "content" / "wiki"

# ══════════════════════════════════════════════════════════════════════════════
# CURATED HUB — only pages Andres works with WEEKLY
# ══════════════════════════════════════════════════════════════════════════════
HUB_PAGES = {
    # Andres himself
    "andres/dashboard",

    # Moil strategy (the 7 pages he references constantly)
    "moil/positioning",
    "moil/gtm",
    "moil/icp",
    "moil/customers",
    "moil/pipeline",
    "moil/product-roadmap",
    "moil/metrics",

    # Key people — the ones he talks to or about every week
    "people/jennifer-storm",      # EDC CEO, HIVE contract
    "people/jacob-oluwole",       # PM, daily Teams
    "people/adeleke-tolulope",    # Lead engineer, daily Teams
    "people/john-costilla",       # Closest friend, community connector, EDC staff
    "people/megan-miller",        # Top customer, product feedback

    # The one concept that's operational (not just reference)
    "concepts/buda-hive",         # Active revenue-generating partnership
}

# ══════════════════════════════════════════════════════════════════════════════
# CURATED SPOKE — active people, current concepts, key orgs
# ══════════════════════════════════════════════════════════════════════════════
# Everything not hub and not leaf is spoke by default.
# But some things need to be EXPLICITLY spoke (override leaf defaults):
SPOKE_OVERRIDES = {
    # Active team members
    "people/taiwo-ola-balogun",
    "people/abiodun-solomon",
    "people/casey-earley",

    # Active customers/leads
    "people/travis-sutherland",
    "people/daniel-guadiano",
    "people/inna-benyukhis",
    "people/anita-lansing",

    # Active partners
    "people/jacquie-martinez",
    "people/joshua-edmond",
    "people/kim-dowers",
    "people/mariana-rodriguez",
    "people/mark-polanco",
    "people/monica-davidson",

    # Key orgs
    "orgs/buda-edc",
    "orgs/queen-creek-chamber",
    "orgs/coffeespace",

    # Concepts relevant to current work (not just historical references)
    "concepts/content360",
    "concepts/smart-hiring",
    "concepts/campaignos",
    "concepts/aedo",
    "concepts/linkedin-gtm",        # identified as biggest untapped channel
    "concepts/ai-cold-outreach",    # active outbound system
    "concepts/content-engine",      # content strategy

    # Key milestone meetings
    "meetings/2025-03-28-jacob-andres-pivot-ai-tools",
    "meetings/2025-05-15-zachary-barker-wyatt-hook-enterprise",
    "meetings/2025-01-08-nvidia-inception-onboarding",
}

# ══════════════════════════════════════════════════════════════════════════════
# LEAF FOLDERS — everything in these is leaf unless overridden
# ══════════════════════════════════════════════════════════════════════════════
LEAF_FOLDERS = {"meetings", "summaries"}

# ══════════════════════════════════════════════════════════════════════════════
# LEAF PATTERNS — these are always leaf
# ══════════════════════════════════════════════════════════════════════════════
LEAF_PATTERNS = {"README", "index", "batch"}

# Concepts that are reference material, not operationally relevant NOW
DEMOTE_TO_SPOKE = {
    "concepts/brain-architecture",
    "concepts/claude-code",
    "concepts/claude-cowork",
    "concepts/managed-agents",
    "concepts/openclaw-hermes",
    "concepts/llm-knowledge-bases",
    "concepts/ai-video-tools",
    "concepts/obsidian",
    "concepts/local-ai-inference",
    "concepts/vibe-coding",
    "concepts/google-stitch",
    "concepts/goose-ai",
    "concepts/meta-harness",
    "concepts/self-learning-gtm-brain",
    "concepts/gtm-system-multi-channel",
    "concepts/ai-org-design",
    "concepts/agent-memory-files",
    "concepts/home-service-cro",
    "concepts/heygen",
    "concepts/seedance",
    "concepts/smb-ai-audits",
    "concepts/moil-team-ops",
    "concepts/moil360",
    "concepts/fantelo",
}


def get_tier(slug: str) -> str:
    """Determine the correct tier for a page."""
    if slug in HUB_PAGES:
        return "graph/hub"
    if slug in SPOKE_OVERRIDES:
        return "graph/spoke"

    # Leaf folders
    folder = slug.split("/")[0] if "/" in slug else ""
    if folder in LEAF_FOLDERS:
        return "graph/leaf"

    # Leaf patterns
    name = slug.split("/")[-1] if "/" in slug else slug
    for pattern in LEAF_PATTERNS:
        if pattern in name:
            return "graph/leaf"

    # Demoted concepts
    if slug in DEMOTE_TO_SPOKE:
        return "graph/spoke"

    # Default: spoke for people, minds, orgs, remaining concepts
    return "graph/spoke"


def set_tier(filepath: Path, new_tier: str) -> bool:
    """Replace the graph tier tag in a file."""
    content = filepath.read_text(encoding="utf-8")

    for old_tier in ["graph/hub", "graph/spoke", "graph/leaf"]:
        if old_tier in content and old_tier != new_tier:
            new_content = content.replace(f"- {old_tier}", f"- {new_tier}", 1)
            if new_content != content:
                filepath.write_text(new_content, encoding="utf-8")
                return True

    return False


def process_directory(wiki_dir: Path, label: str):
    counts = {"hub": 0, "spoke": 0, "leaf": 0, "unchanged": 0}
    changes = []

    for md_file in sorted(wiki_dir.rglob("*.md")):
        rel = str(md_file.relative_to(wiki_dir)).replace("\\", "/").replace(".md", "")
        if rel.startswith(".") or rel.startswith("_"):
            continue

        content = md_file.read_text(encoding="utf-8")
        # Determine current tier
        current = "hub" if "graph/hub" in content else "spoke" if "graph/spoke" in content else "leaf" if "graph/leaf" in content else "none"

        new_tier = get_tier(rel)
        new_short = new_tier.split("/")[1]

        if current == new_short:
            counts["unchanged"] += 1
            continue

        if set_tier(md_file, new_tier):
            direction = f"{current}→{new_short}"
            changes.append((rel, direction))
            counts[new_short] += 1

    # Report
    print(f"\n  {label}: {counts['hub']} set to hub, {counts['spoke']} set to spoke, {counts['leaf']} set to leaf, {counts['unchanged']} unchanged")
    if changes:
        print(f"\n  Changes ({len(changes)}):")
        for slug, direction in changes:
            print(f"    [{direction:12s}] {slug}")

    return counts


def main():
    print("=== Resetting tiers (curated approach) ===")
    print(f"Hub target: {len(HUB_PAGES)} pages")

    c1 = process_directory(WIKI_DIR, "wiki/")
    c2 = process_directory(QUARTZ_WIKI_DIR, "quartz/content/wiki/")

    # Final count
    hub_count = sum(1 for f in WIKI_DIR.rglob("*.md") if "graph/hub" in f.read_text(encoding="utf-8", errors="ignore"))
    spoke_count = sum(1 for f in WIKI_DIR.rglob("*.md") if "graph/spoke" in f.read_text(encoding="utf-8", errors="ignore"))
    leaf_count = sum(1 for f in WIKI_DIR.rglob("*.md") if "graph/leaf" in f.read_text(encoding="utf-8", errors="ignore"))

    print(f"\n=== Final state ===")
    print(f"  Hub:   {hub_count} pages (visible, large nodes)")
    print(f"  Spoke: {spoke_count} pages (visible, normal nodes)")
    print(f"  Leaf:  {leaf_count} pages (hidden from global graph)")
    print(f"  Graph will show: ~{hub_count + spoke_count} nodes")


if __name__ == "__main__":
    main()

# LLM Knowledge Bases (Karpathy Pattern)

**Type:** concept
**Last updated:** 2026-04-12
**Source:** [[raw/x-bookmarks-2026-04-11 copy]]
**Related:** [[wiki/concepts/buda-hive]], [[wiki/concepts/obsidian]], [[wiki/concepts/brain-architecture]], [[wiki/minds/andrej-karpathy]]

---

## What It Is

A pattern originated by Andrej Karpathy (April 2026) for building persistent, LLM-maintained wikis from raw source material. Instead of RAG (where every query starts from zero), the LLM incrementally builds and maintains interlinked markdown articles that compound over time. Cross-references build up, contradictions get flagged, and the AI handles all maintenance.

**This is exactly what the Moil Brain knowledge base does.** The `raw/ → wiki/ → outputs/` pipeline implements this pattern.

## Key Stats

- Karpathy's original post: 19.3M views, 100K bookmarks (Apr 2)
- Follow-up: 6.4M views (Apr 4)
- His single research topic grew to ~100 articles, 400K words

## Implementation

- Open source: `rvk7895/llm-knowledge-bases` (already referenced in Moil Brain architecture)
- Tools: Obsidian for review, Obsidian Web Clipper for capture, Claude Code for compilation
- Key insight: wiki compounds over time — article 10 creates connections back to articles 1-9

## Derivative Builds (from X bookmarks)

- **@NickSpisak_** — Rebuilt Karpathy second brain in 20 minutes. Also built first working Managed Agent. X Article on second brain systems (2.2M views)
- **@FarzaTV** — "Farzapedia" — built from 2,500 diary/Notes/iMessage entries (1.7M views)
- **@alliekmiller** — "Claudeopedia" — Karpathy wiki + /last30days skill + /wiki skill
- **@defileo** — "Claude + Obsidian have to be illegal" (3.9M views)
- **@hooeem** — Full course on creating LLM knowledge bases

## Obsidian as the View Layer

The winning combination (multiple creators): Claude Code writes wiki, Obsidian browses it. Obsidian provides:
- Graph view (visual relationship map)
- Backlinks (see what links to any page)
- Dataview plugin (query notes like a database)
- iCloud sync (access on any device)

See [[wiki/concepts/obsidian]] for implementation details.

## The Personal Wikipedia Pattern (Farzapedia)
@FarzaTV's "Farzapedia" — built from 2,500 diary/Notes/iMessage entries (1.7M views) — shows the most personal implementation: a life wiki, not just a business wiki. The Moil Brain could have personal + business layers in the same vault.

## The "Claudeopedia" Derivatives (Apr 2026)
Multiple implementations gained traction in the same week:
- **@alliekmiller** "Claudeopedia" — Karpathy wiki + /last30days skill + /wiki skill (Claude Code native)
- **@NickSpisak_** — "Rebuilt in 20 minutes" guide (2.2M views)
- **@hooeem** — Full course on implementation
- **@defileo** — "Claude + Obsidian have to be illegal" (3.9M views)
- **@VibeMarketer_** — "I turned my brain into a searchable wiki with Claude Code"
- **@aiedge_** — "Claude Code + Obsidian Ultimate Guide"

## Relevance to Moil Brain

The Brain already follows this architecture. As of April 12, 2026, the deep compile run processed 129 X bookmarks → 20+ new/updated wiki pages. The weekly compile cron will keep it growing. The next step is enabling Obsidian as the view layer for graph navigation.

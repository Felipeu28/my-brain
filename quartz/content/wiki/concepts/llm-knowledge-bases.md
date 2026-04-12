---
tags: [concept, personal, growing]
---

# LLM Knowledge Bases (Karpathy Pattern)

**Type:** concept
**Last updated:** 2026-04-11
**Source:** [[raw/x-bookmarks-2026-04-11 copy]]
**Related:** [[wiki/concepts/buda-hive]]

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

## Relevance to Moil Brain

The Brain already follows this architecture. The gap has been that the compilation step wasn't running — raw files sat unprocessed. As of April 11, 2026, the first full compilation was done (7 sources → 13+ wiki pages). The weekly compile cron will keep it growing.

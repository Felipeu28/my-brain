---
name: brain-architecture concept
description: Andres's 5-layer personal knowledge pipeline — Collection → Storage → Processing → LLM Wiki → Query
type: concept
---

# Brain Architecture — Andres's 5-Layer Personal Knowledge Pipeline

**Type:** concept
**Last updated:** 2026-04-11
**Source:** [[raw/brain-guide.md]]
**Related:** [[wiki/concepts/llm-knowledge-bases]], [[wiki/concepts/claude-cowork]], [[wiki/summaries/brain-guide]]

---

## Summary
A five-layer pipeline that turns raw signal (mostly weekly X bookmarks) into a compounding personal knowledge graph queryable in Andres's own voice. This concept describes the system this knowledge base implements.

## The 5 Layers

| Layer | Role | Artifact |
|---|---|---|
| 1. **Collection** | Weekly Claude Cowork pull from X bookmarks (scheduled Mon 9am) | `raw/x-bookmarks-YYYY-MM-DD.md` |
| 2. **Storage** | Unfiltered markdown in Obsidian `raw/` — speed over beauty | `raw/*.md` |
| 3. **Processing** | Andres skims, highlights, links, archives low-signal — 30 min/week | wiki updates, cross-links |
| 4. **LLM Wiki** | Monthly Claude synthesis across digests → personal knowledge graph | `synthesis-YYYY-MM.md` |
| 5. **Query** | Feed wiki + recent raw + question → answer in Andres's voice | decision output |

## Key Points
- **Themes & Takeaways** are the gold — 2-3 bullet per-week summaries compress into a searchable intellectual history.
- **Cadence:** daily 10min · weekly 30min · monthly 20min · quarterly full deep query.
- **Three query patterns:** Synthesis, Decision, Deep Dive.
- **MOIL.md context file** = Mission / Operating Principles / Identity / Legacy — primer before any big query.
- **Multi-source future:** X + email + Slack + GitHub + reading list → `raw/`.
- **Automation is collection; discipline is processing; payoff is synthesis.**

## Connections
- Implements the [[wiki/concepts/llm-knowledge-bases]] (Karpathy) pattern.
- Collection layer depends on [[wiki/concepts/claude-cowork]] scheduled tasks.
- Every `wiki/summaries/*` file is a Layer 3 output.
- [[outputs/synthesis-2026-04]] is a Layer 4 artifact.

## Moil Relevance
Directly informs Moil product decisions — Andres runs the business with a version of this loop. It's also structurally similar to the "AI Co-Founder" Moil sells (21 questions → market research → plan → content calendar = collection → processing → synthesis).

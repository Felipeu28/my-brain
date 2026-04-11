# Moil Brain — Wiki

This is the **semantic memory** layer of Andres Urrego's Moil Brain. It is also a valid Obsidian vault — open this folder (`~/My Brain/knowledge-base/wiki/`) directly in Obsidian.

## What lives here

- `moil/` — Moil's positioning, ICP, GTM, campaigns, decisions, customer research
- `meetings/` — structured notes (decisions + action items) from processed voice memos and meeting transcripts
- `people/` — pages on key contacts, customers, investors, advisors
- `concepts/` — frameworks, mental models, industry terms the Brain has learned
- `inbox/` — Obsidian's default landing folder for new notes you create manually

## What does NOT live here

- **Raw source material** lives in `~/My Brain/knowledge-base/raw/` (immutable, read-only for the Brain)
- **Outputs** (briefings, reports, drafts) live in `~/My Brain/knowledge-base/outputs/`
- **Episodic memory** (every conversation, every action) lives in Mem0 + ChromaDB, not here

## How updates happen

- **Manual edits** by Andres in Obsidian — anytime
- **`/kb compile`** in Claude Code (the rvk7895/llm-knowledge-bases plugin) — weekly, ingests new things from `raw/` and updates wiki articles
- **`/skill:cmo`** in Pi — when run by Andres, it reads positioning/icp/gtm files and may propose edits (with Andres's approval)
- **`/skill:weekly-kb-compile`** — orchestrates the weekly compile and surfaces lint issues

## Backlinks and Dataview

To get the most out of this vault, install these Obsidian community plugins:
- **Dataview** — for the auto-generated indexes the kb plugin produces
- **Obsidian Git** (optional) — for versioning the wiki separately from raw/

The vault is intentionally not git-initialized at this layer. Versioning is up to Andres.

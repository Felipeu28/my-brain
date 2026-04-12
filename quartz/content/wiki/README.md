---
name: wiki root
description: Landing page for the Moil Brain wiki — semantic memory layer
type: index
tags:
  - graph/leaf
---

# Moil Brain — Wiki

This is the **semantic memory** layer of Andres Urrego's Moil Brain. Linked from [[index]]. Also a valid Obsidian vault — open `~/My Brain/knowledge-base/wiki/` directly in Obsidian.

---

## Folders at a glance

| Folder | Count | Purpose | Index |
|---|---|---|---|
| `moil/` | 6 | Moil business: positioning, ICP, GTM, customers, competitors, metrics | [[wiki/moil/README\|moil/]] |
| `people/` | 16 | Personal network (family, friends, customers, collaborators) | [[wiki/people/README\|people/]] |
| `minds/` | 5 | Public AI thought leaders tracked from afar | [[wiki/minds/README\|minds/]] |
| `orgs/` | 4 | Customer/partner/prospect organizations | [[wiki/orgs/README\|orgs/]] |
| `concepts/` | 15 | Frameworks, mental models, products, programs | [[wiki/concepts/README\|concepts/]] |
| `radar/` | 1 | Append-only changelogs for fast-moving topics | [[wiki/radar/README\|radar/]] |
| `summaries/` | 12 | One summary page per raw source | [[wiki/summaries/README\|summaries/]] |
| `meetings/` | 0 | Structured meeting notes (empty) | — |
| `inbox/` | 0 | Manual drop zone (empty) | — |

---

## What does NOT live here

- **Raw source material** → `../raw/` (immutable, never edit)
- **Outputs** (briefings, syntheses) → `../outputs/`
- **Open actions & commitments** → `../MEMORY.md`
- **Ingestion history** → `../log.md`
- **Agent instructions** → `../CLAUDE.md`
- **Episodic memory** (conversation logs) → Mem0 + ChromaDB, not this vault

---

## How updates happen

| Trigger | What happens |
|---|---|
| Manual Obsidian edit | Andres updates a page directly |
| Claude Code ingestion (`/kb compile`) | New `raw/` file → summary + concept + people updates |
| Weekly X bookmark sweep | `raw/x-bookmarks-YYYY-MM-DD.md` → updates [[wiki/radar/claude-code-changelog]] and minds/ |
| Monthly synthesis | 4 bookmark digests → `outputs/synthesis-YYYY-MM.md` |

---

## Design principles (the rules this wiki follows)

1. **Flat hierarchy** — two levels max under `wiki/`. No nesting concepts inside concepts.
2. **One concept per page** — if a page is about two things, split it.
3. **Path-style wikilinks** — `[[wiki/folder/slug|Display Label]]`, not `[[Display Label]]`. Keeps grep predictable.
4. **Every folder has a README** — so a cold reader can orient without reading every file.
5. **Index-first navigation** — [[index]] is the entry point. Folder READMEs are secondary indexes. Files are leaves.
6. **Summaries preserve sources** — every `raw/` file gets a `summaries/` page. Never edit `raw/`.
7. **Pruning is a ritual** — MEMORY.md and radar logs need weekly review or they rot.

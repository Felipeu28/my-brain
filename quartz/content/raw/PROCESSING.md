---
title: Inbox Processing Protocol
tags: [meta, personal]
---

# Inbox Processing Protocol

**When:** Every Sunday, 30 minutes max.
**Goal:** Process all items in raw/ from the past week. Never let unprocessed items exceed 50.

## Protocol
1. Open this folder and sort by date
2. For each raw item:
   - Read it
   - Tag it (add frontmatter `tags:` if missing)
   - If it contains a useful insight: extract it into a `wiki/concepts/` or `wiki/moil/` note
   - If it references a person: link to or create `wiki/people/person-name.md`
   - Add `status: processed` to frontmatter
3. Move processed items to `raw/archive/YYYY-MM/` (create folder)
4. Update `raw/index.md` with inbox count

## Status Tags
- `status: inbox` — not yet reviewed
- `status: processed` — reviewed, insight extracted or discarded
- `status: archived` — moved to archive

## Inbox Count Target
- 0-15: Healthy
- 16-30: Behind, process this week
- 31+: System failing — block 2 hours

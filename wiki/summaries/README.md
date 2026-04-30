---
name: summaries index
description: One structured summary per raw source file — the Processing layer of the Brain
type: index
tags:
  - graph/leaf
---

# Summaries — Index

Every file in `../raw/` has a matching summary here. Summaries are the Layer 3 "Processing" output of the [[wiki/concepts/brain-architecture|Brain architecture]] — where raw signal becomes structured, linked knowledge.

## Rules
- **One summary per raw file.** Never merge sources.
- **Summary ≠ full copy.** Extract key points, connections, and Moil relevance — don't duplicate the raw file.
- **Link heavily** into [[wiki/concepts/README|concepts]], [[wiki/people/README|people]], [[wiki/orgs/README|orgs]], [[wiki/moil/README|moil]].
- **Mark SUPERSEDED** when a newer version of the same source lands — don't delete the old summary.

---

## By topic

### Brain architecture & meta
- [[wiki/summaries/brain-guide]] — The 5-layer Brain pipeline guide
- [[wiki/summaries/know-me-extraction-prompts]] — Interview prompts (Claude/ChatGPT/Grok)

### Moil business
- [[wiki/summaries/moil-documents-2026-04-09]] — Moil Enterprise business plan (Mar 5)
- [[wiki/summaries/moilapp-website-2026-04-09]] — moilapp.com canonical copy
- [[wiki/summaries/github-project-tracker]] — 48 repos across 3 orgs

### Buda HIVE / EDC ecosystem
- [[wiki/summaries/buda-hive-edc-2026-04-11]] — ⭐ Full intelligence (Apr 11) — **use this one**
- [[wiki/summaries/buda-hive-edc-2026-04-09]] — Earlier draft (SUPERSEDED)

### Network & inbox
- [[wiki/summaries/imessages-people-2026-04-09]] — Relationship intelligence from iMessages
- [[wiki/summaries/outlook-emails-2026-04-09]] — Inbox digest Apr 9
- [[wiki/summaries/facebook-pages-2026-04-09]] — AIbyAndres + MoilWorks FB pages

### Weekly bookmark sweeps
- [[wiki/summaries/x-bookmarks-2026-04-11]] — ⭐ 129 items (preferred for synthesis)
- [[wiki/summaries/x-bookmarks-2026-04-11]] — 114 items (shorter sibling)

---

## Known raw/ quirks (documented, not fixed — CLAUDE.md forbids modifying raw/)
- `raw/buda-hive-edс-2026-04-09.md` — Cyrillic "с" in filename
- `raw/x-bookmarks-2026-04-11.md` — the fuller version; prefer over its sibling

## Cadence
- New summaries appear automatically during ingestion runs
- SUPERSEDED flag set when a new version of an existing source lands
- Annual prune: archive summaries older than 1 year if the raw source is also archived

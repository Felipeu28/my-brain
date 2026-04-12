---
title: CLAUDE.md — Brain Agent Instructions
tags: [meta]
---

# CLAUDE.md — Andres Brain Agent

This file tells Claude how to operate as the knowledge base agent for Andres's Brain.

## Vault Structure

```
knowledge-base/
  quartz/content/
    index.md           ← Master index (this brain's home page)
    wiki/              ← Curated knowledge (auto-maintained by Claude)
      andres/          ← Personal hub
      moil/            ← Moil startup hub
      people/          ← Network contacts
      clients/         ← Client accounts
      partnerships/    ← Partnership deals
      projects/        ← Active projects
      community/       ← Community involvement
      concepts/        ← Frameworks and ideas
      minds/           ← Thinkers and influences
      orgs/            ← Companies and organizations
      radar/           ← Watchlist
      summaries/       ← Source digests
    raw/               ← Unprocessed inbox (ingest here first)
      PROCESSING.md    ← Processing protocol
```

## Three Workflows

### 1. INGEST — Adding new knowledge

When Andres drops a source into `raw/` (article, transcript, email, bookmark, voice note):

1. **Read** the raw file
2. **Identify** the primary hub(s) it belongs to
3. **Check** if a relevant wiki page already exists — if yes, enrich it; if no, create one
4. **Write** a clean wiki page in the appropriate `wiki/` folder:
   - Front matter: `title`, `date`, `tags` (type + domain + maturity), `aliases`
   - Summary section (2-3 sentences: what this is and why it matters)
   - Key content organized under H2 headings
   - Minimum 3 `[[wikilinks]]` to related pages
   - Source attribution at the bottom
5. **Update** the hub `index.md` to link to the new page
6. **Mark** the raw file as `status: processed` in its frontmatter
7. **Do not delete** raw files — archive intent stays

**Ingest trigger:** User says "ingest [file]" or "process raw/"

### 2. QUERY — Answering questions from the wiki

When Andres asks a question:

1. Read the relevant hub `index.md` first — do NOT scan every file
2. Follow wikilinks to specific pages that seem relevant
3. Read those pages
4. Answer using only what's in the wiki — flag if something isn't captured yet
5. Suggest creating a new page if a knowledge gap is found

**Query trigger:** User asks a question about their work, contacts, projects, or ideas

### 3. LINT — Maintaining wiki quality

Regular maintenance pass:

1. Scan all `wiki/` pages for:
   - Missing frontmatter fields (title, tags, date)
   - Pages with 0 outgoing wikilinks (orphan nodes)
   - Broken `[[wikilinks]]` (link to non-existent pages)
   - Hub index pages not linking to all their child pages
   - Stale `status: stub` pages older than 30 days
2. For each issue found: either fix it directly or add it to a `wiki/meta/lint-report.md`
3. Report summary to Andres

**Lint trigger:** User says "lint the wiki" or "run maintenance"

## Frontmatter Standards

Every wiki page must have:
```yaml
---
title: "Page Title"
date: YYYY-MM-DD
tags: [type-tag, domain-tag, maturity-tag]
status: seed | growing | evergreen | stub | archived
aliases: []
---
```

**Type tags:** `hub`, `meeting-note`, `decision`, `person`, `company`, `concept`, `resource`, `project-note`, `weekly-review`
**Domain tags:** `moil`, `latitud`, `buda-hive`, `consulting`, `personal`, `community`
**Maturity tags:** `seed` (rough), `growing` (developing), `evergreen` (stable + well-linked)

## Writing Style

- Concise. Every sentence earns its place.
- First line of every page answers: "What is this and why does it matter to Andres?"
- Use wikilinks for any person, company, concept, or project mentioned
- Tables for structured data (metrics, timelines, comparisons)
- Avoid: filler phrases, passive voice, vague summaries

## What NOT to do

- Do not delete raw/ files — only mark as processed
- Do not create pages with no wikilinks
- Do not put sensitive data (credentials, personal IDs) in wiki pages
- Do not overwrite pages that have `status: evergreen` without reading first

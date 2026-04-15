# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is the **Moil Brain Knowledge Base** — Andres Urrego's personal AI "second brain" for the Moil business. It is not an application codebase; it's a living wiki + ingestion pipeline that compiles daily from raw sources (email, Teams, OneDrive transcripts, X bookmarks, GitHub activity) into structured linked markdown pages, and deploys as a Quartz static site.

Your role when working inside this directory is the **Moil Brain KB Agent**: ingest `raw/` sources, produce structured linked pages in `wiki/`, keep `index.md` + `log.md` current, and never let data quality regress.

## Critical architectural fact — wiki/ and quartz/content/ are two directories

The KB agent writes to `wiki/` at the repo root. GitHub Pages builds and deploys from `quartz/content/wiki/`. **They are not the same directory and there is no symlink.** A `scripts/sync_wiki.sh` step copies `wiki/` → `quartz/content/wiki/` (and root `MEMORY.md`, `index.md`, `log.md` → `quartz/content/`). **Every commit that changes `wiki/` must run `bash scripts/sync_wiki.sh` first, or the deployed site will go stale.** All four automated commit scripts already do this (see "Automated jobs" below). For manual commits, use the pattern in `COMMANDS.md`.

## Source-of-truth hierarchy

When files conflict:
1. `~/My Brain/CURRENT_STATE.md` — reconciled operating snapshot (outside this repo)
2. `MEMORY.md` — open actions and live commitments (200-line hard cap)
3. `wiki/andres/ANDRES.md` — daily dashboard (this is the "gravitational center" of the graph — links to every hub + spoke; do not rename it)
4. `wiki/moil/pipeline.md`, `wiki/moil/customers.md`, `wiki/moil/active-projects.md` — active deals/customers/projects
5. `index.md` — master navigation

## Commands

```bash
# Health audit (run this whenever you change many files)
python3 scripts/kb-health.py                   # stdout only
bash scripts/kb-health.sh                      # writes report to outputs/health/
python3 scripts/kb-health.py --fail-on-errors  # exit 1 if errors (for CI)

# Sync wiki → quartz (MANDATORY before every commit)
bash scripts/sync_wiki.sh

# Build + serve the site locally
npx quartz build -d quartz/content             # one-shot build
npx quartz build -d quartz/content --serve     # hot-reload preview on :8080

# Format + type check
npm run check                                  # tsc --noEmit && prettier --check
npm run format                                 # prettier --write

# Graph tier maintenance
python3 scripts/upgrade-graph.py               # auto-promote pages with many inbound links
python3 scripts/reset-tiers.py                 # reset to defaults (destructive, rare)

# Re-index vector store (ChromaDB, in pi-workspace)
python3 ../pi-workspace/bin/wiki-to-chromadb.py

# Commit + push (manual path)
bash scripts/sync_wiki.sh && git add -A && git commit -m "..." && git push felipeu28 main
```

**Git remote:** only `felipeu28` (= `github.com/Felipeu28/my-brain`) exists. There is no `origin`. GitHub Actions in `.github/workflows/deploy.yml` builds from `quartz/content/` and deploys to GitHub Pages on every push to `main`.

## Ingestion protocol (when Andres says "ingest this")

1. **Read `index.md` first** to know what already exists
2. **Read the raw source.** Never modify or delete files in `raw/` — they are immutable
3. **Extract** concepts, people, orgs, themes, Moil-relevant decisions
4. **Create or update** wiki pages (update existing over creating new)
5. **Update `index.md`** Source Inventory + stats
6. **Append to `log.md`** with a dated entry
7. **Run `bash scripts/sync_wiki.sh`**, then `python3 scripts/kb-health.py` to verify no regressions
8. Commit + push via `felipeu28 main`

## Wiki page format

```yaml
---
tags:
  - graph/hub    # OR graph/spoke OR graph/leaf — exactly one, required
  # For pages in wiki/people/, also include ONE person/* tag:
  - person/team | person/customer | person/partner | person/personal | person/vendor | person/contact
status: active | warm | archived    # for people/orgs where relevant
last_contact: YYYY-MM-DD             # for people/orgs
---
# Page Title

**Type:** concept | person | organization | meeting | moil-topic
**Last updated:** YYYY-MM-DD
**Source:** [[raw/filename]]
**Related:** [[wiki/concepts/X]], [[wiki/people/Y]]

---
## Summary
## Key Points
## Connections
## Moil Relevance
```

## Graph tier rules

| Tier | When to use |
|------|-------------|
| `graph/hub` | Core strategy pages, central people (5+ inbound links). Visible as large node |
| `graph/spoke` | Most people, concepts, orgs, important meetings. Normal node |
| `graph/leaf` | Meeting transcripts, summaries, deprecation stubs, batch/index pages. Hidden from global graph, still searchable |

**Default by folder:** `meetings/*` = leaf, `summaries/*` = leaf, `people/*` = spoke (→ hub at 5+ inbound), `concepts/*` = spoke, `moil/*` = spoke (→ hub if strategic), `orgs/*` = spoke, `minds/*` = spoke, `README.md`/`index.md` = leaf.

**Auto-promotion:** `python3 scripts/upgrade-graph.py` promotes spoke→hub at 8+ inbound and leaf→spoke at 5+ inbound. The `wiki/andres/ANDRES.md` dashboard lists every hub + spoke by design — do not break this.

## Folder layout (writing zones)

```
raw/       IMMUTABLE — ingest sources only. Never modify or delete files here.
wiki/      AGENT WRITES HERE. Obsidian vault root.
  concepts/    Frameworks, mental models, products, programs
  meetings/    Decisions + action items per meeting. Use historical-transcripts-index.md
               for low-signal transcripts rather than creating stubs per file
  moil/        Moil business — positioning, ICP, GTM, customers, pipeline,
               active-projects, product-roadmap, metrics, competitors
  people/      Personal network. Always include person/* sub-tag
  orgs/        Customer, partner, and prospect organizations
  minds/       Public AI thought leaders tracked from afar
  summaries/   One structured summary per raw source
  radar/       Append-only changelogs for fast-moving topics
  andres/      Personal dashboard (ANDRES.md). Do not rename ANDRES.md
  inbox/       Manually created notes — leave alone unless Andres asks
outputs/   Generated briefings, reports, drafts. outputs/health/ = kb-health reports
quartz/    Quartz v4 site generator source. quartz/content/ is the build input —
           the KB agent should NOT edit quartz/content/ directly; always edit
           wiki/ and let sync_wiki.sh mirror it.
scripts/   See Commands section
.github/workflows/deploy.yml    GitHub Pages deploy pipeline
```

## Data-quality hard rules

These are enforced by `kb-health.py` and should not regress:

- No MD5-duplicate files in `raw/`
- No broken wikilinks (Obsidian bare-name resolution is supported)
- Every wiki page (except READMEs/index) has exactly one `graph/*` tag
- Every `people/*` page has exactly one `person/*` sub-tag
- `MEMORY.md` ≤ 200 lines (move old archive blocks to `log.md`)
- `index.md` stats match reality (wiki page count, raw source count)
- `wiki/` and `quartz/content/wiki/` in sync
- No page with `Last updated:` > 90 days (informational)

Run `bash scripts/kb-health.sh` after every non-trivial change. The launchd job `com.moil.brain.kb-health` runs it every Sunday at 8am and writes to `outputs/health/kb-health-latest.md`.

## Automated jobs (10 launchd plists in pi-workspace/)

| Plist | When | What |
|-------|------|------|
| `morning-briefing` | Weekday 8:45am | Pulls calendar/email/GitHub, generates briefing, emails it |
| `teams-daily` | Daily | Pulls 7 days Teams messages, ingests via Claude, commits |
| `x-bookmarks` | (manual commit) | Commits latest X bookmarks digest |
| `content-calendar` | Monday 9am | Generates weekly content calendar |
| `email-digest` | Daily | Summarizes inbox activity |
| `heartbeat` | Periodic | Brain freshness check → `outputs/health/heartbeat-*.md` |
| `weekly-compile` | Fri 2pm | Reconciles GitHub activity + pipeline |
| `weekly-pulse` | Weekly | Status synthesis |
| `chroma-index` | Daily | Re-indexes wiki/ into local ChromaDB |
| `kb-health` | **Sunday 8am** | Runs kb-health.sh → `outputs/health/kb-health-*.md` |

All four commit-producing scripts (`teams_ingest.sh`, `x_bookmark_commit.sh`, `morning-briefing.sh`, `weekly-compile.sh`) now call `sync_wiki.sh` before `git push`. Do not remove that step.

## Deployment

`.github/workflows/deploy.yml` builds Quartz from `quartz/content/` and deploys to GitHub Pages on push to `main`. No Vercel, no manual deploy step. The site is `my-brain-two.vercel.app` per `quartz.config.ts` (legacy baseUrl — the actual live URL is GitHub Pages).

## Naming conventions

- **Moil360** is the canonical product name. `Content360` was the old internal name; `wiki/concepts/content360.md` is now a deprecation stub redirecting to `wiki/concepts/moil360.md`. Use Moil360 in all new operational docs. Historical meetings/summaries are left as-is.
- **Dates in filenames:** `YYYY-MM-DD-slug.md`. The legacy `odtr-YYYYMMDD-*` pattern in `raw/` is frozen — do not create new files with that pattern.
- **People page names:** kebab-case, `first-last.md`. Disambiguate with last name when needed (e.g., `roxana-esquivel.md` vs `roxana-yglesias.md`).

## What NOT to do

- Do not edit `quartz/content/` directly — edit `wiki/` and run `sync_wiki.sh`
- Do not delete or modify files in `raw/`
- Do not commit without running `sync_wiki.sh` first (unless you're certain no `wiki/` files changed)
- Do not rename `wiki/andres/ANDRES.md` — it's the graph's gravitational center
- Do not create duplicate concept pages — search and update existing
- Do not use wikilinks with escaped pipes (`[[target\|Display]]`) — use bare pipes (`[[target|Display]]`)
- Do not promote every raw transcript to a wiki meeting page — low-signal transcripts go in `wiki/meetings/historical-transcripts-index.md`
- Do not use RAG/embeddings — navigate via `index.md` + structured wikilinks
- Do not skip the graph/ tier or person/ sub-tag — `kb-health` will flag it
- Do not reintroduce `origin` remote — it 404s; only `felipeu28` works

---

## Brain Commands

These commands are available when working in this vault. Run them by typing the command in any Claude session opened in this folder.

### /brain-ingest
Process all files in `quartz/content/raw/` that have no `ingested: true` in their frontmatter.

For each unprocessed file:
1. Read and classify by type: `article | tweet | thread | transcript | idea | bookmark | briefing | calendar`
2. Extract: key concepts, people mentioned, orgs mentioned, tldr (1-2 sentences max)
3. Find or create the most relevant wiki page(s) in `quartz/content/wiki/` and add a wikilink + fact from this source
4. Update `quartz/content/wiki/index.md` with a TLDR entry if this is a new page
5. Add `ingested: true` and `ingested_at: YYYY-MM-DD` to the source file's frontmatter
6. Commit all changes and push to felipeu28

Signal rule: Skip anything that isn't 80%+ relevant to Andres's core domains (Moil, AIbyAndres, Brain/PKM, community, family, personal growth). Log skipped files.

### /brain-query [question]
Answer a question using knowledge stored in `quartz/content/wiki/`.

1. Search wiki/ for pages relevant to the question
2. Return a cited answer with [[wikilink]] references
3. Save the answer to `quartz/content/raw/outputs/YYYY-MM-DD-[slug].md`
4. If the answer reveals a gap in the Brain, create a stub page for that topic
5. Commit and push new outputs

### /brain-explore [topic]
Browse a topic area within the Brain.

1. Find all pages in wiki/ related to [topic] (search titles, tags, content)
2. Show the connection map: what links to it, what it links to
3. Surface 3 pages that logically should exist but don't
4. Suggest 2 cross-hub connections that aren't yet made

### /brain-lint
Monthly quality audit. Run after bulk ingestion or monthly.

1. Find all wiki pages with fewer than 150 words → report as stubs
2. Find all wiki pages with no incoming wikilinks → report as orphans
3. Find pages on the same topic that may contradict each other
4. Report everything — don't auto-fix
5. Save report to `quartz/content/raw/outputs/brain-lint-YYYY-MM-DD.md`

# Moil Brain — Ingestion Log

This file tracks every source that has been processed by `/kb compile`. Claude Code appends an entry here after each ingestion run.

---

## Format

```
### [YYYY-MM-DD] Source title
- **File:** raw/filename.ext
- **Type:** article | transcript | pdf | note | tweet-thread | other
- **Pages created:** [[wiki/concepts/X]], [[wiki/people/Y]], ...
- **Pages updated:** [[wiki/moil/Z]]
- **Summary:** One-sentence description of what this source was about
```

---

## Log Entries

### [2026-04-11] First Full Compilation — Batch Ingestion

**Trigger:** Andres asked to kick off the Brain. Run in Claude Cowork (direct file access).

**Sources processed (7 of 12 raw files):**

- **File:** raw/imessages-people-2026-04-09.md
  - **Type:** relationship-intelligence
  - **Pages created:** [[wiki/people/john-costilla]], [[wiki/people/mark-polanco]], [[wiki/people/travis-sutherland]]
  - **Summary:** iMessage conversations revealing family structure, nicknames, and business relationships

- **File:** raw/outlook-emails-2026-04-09.md
  - **Type:** email-digest
  - **Pages created:** [[wiki/people/daniel-guadiano]]
  - **Summary:** Outlook email threads — Astra Restaurant lead, CoffeeSpace partnership, Johns Creek Chamber

- **File:** raw/buda-hive-edc-2026-04-11.md
  - **Type:** partnership / customer / contract
  - **Pages created:** [[wiki/people/jennifer-storm]], [[wiki/people/joshua-edmond]], [[wiki/people/jacquie-martinez]], [[wiki/concepts/buda-hive]], [[wiki/concepts/aedo]], [[wiki/concepts/campaignos]]
  - **Summary:** Full intelligence file on Buda HIVE/EDC — contracts, AEDO, CampaignOS, timeline

- **File:** raw/moil-documents-2026-04-09.md
  - **Type:** business-plan
  - **Pages updated:** [[wiki/moil/positioning]], [[wiki/moil/icp]], [[wiki/moil/gtm]]
  - **Summary:** Moil Enterprise business plan — traction, pricing, market, team, financials

- **File:** raw/moilapp-website-2026-04-09.md
  - **Type:** company-website
  - **Pages updated:** [[wiki/moil/positioning]], [[wiki/moil/icp]], [[wiki/moil/gtm]]
  - **Summary:** Full website scrape — features, pricing, hiring metrics, testimonials, candidate platform

- **File:** raw/facebook-pages-2026-04-09.md
  - **Type:** social-media
  - **Pages updated:** [[wiki/moil/gtm]]
  - **Summary:** AIbyAndres + MoilWorks Facebook pages — follower counts, engagement, social links

- **File:** raw/github-project-tracker.md
  - **Type:** project-tracker
  - **Used for:** AGENTS.md context, task prioritization
  - **Summary:** 48 repos across 3 orgs — activity status, cleanup recommendations, priority tracking

**Also updated:**
- `pi-workspace/AGENTS.md` — 16 bracketed placeholders filled with real data
- `index.md` — source inventory and stats updated

**Remaining raw files (not yet compiled):**
- `brain-guide.md` — meta-guide (reference, not wiki content)
- `know-me-extraction-prompts.md` — extraction prompts (tooling)
- `x-bookmarks-2026-04-11.md` + copy — X bookmark digests (queue for next compile)
- `buda-hive-edc-2026-04-09.md` — earlier version, superseded

---

### [2026-04-11] Second Full Compilation — wiki/summaries + new concepts

**Trigger:** Andres asked to build wiki/summaries/ for every raw file + concept pages for recurring themes + MEMORY.md.

**Summaries created (11 — one per raw file):**
- [[wiki/summaries/brain-guide]]
- [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [[wiki/summaries/buda-hive-edc-2026-04-09]] (marked SUPERSEDED)
- [[wiki/summaries/facebook-pages-2026-04-09]]
- [[wiki/summaries/github-project-tracker]]
- [[wiki/summaries/imessages-people-2026-04-09]]
- [[wiki/summaries/know-me-extraction-prompts]]
- [[wiki/summaries/moil-documents-2026-04-09]]
- [[wiki/summaries/moilapp-website-2026-04-09]]
- [[wiki/summaries/outlook-emails-2026-04-09]]
- [[wiki/summaries/x-bookmarks-2026-04-11]]
- [[wiki/summaries/x-bookmarks-2026-04-11-copy]]

**New concept pages:**
- [[wiki/concepts/brain-architecture]] — Andres's 5-layer pipeline
- [[wiki/concepts/claude-code]] — Anthropic's CLI agent
- [[wiki/concepts/claude-cowork]] — scheduled/background Claude workflows
- [[wiki/concepts/openclaw-hermes]] — open-source parallel ecosystem
- [[wiki/concepts/fantelo]] — Andres's parallel project
- [[wiki/concepts/moil360]] — Moil's 30-day marketing engine brand
- [[wiki/orgs/coffeespace]] — partnership ecosystem contact

**New people pages:**
- [[wiki/people/shay-foley]] — Johns Creek Chamber, deferred partnership
- [[wiki/people/hazim-mohamad]] — CoffeeSpace outreach

**Also updated:**
- `index.md` — summaries section added, concept/people counts refreshed
- `MEMORY.md` — new file capturing open actions from raw sources

---

## How to add an entry

Claude Code automatically appends to this file at the end of each `/kb compile` run. You do not need to edit this manually.

To ingest a new source:
1. Drop the file into `~/My Brain/knowledge-base/raw/`
2. Open Claude Code in `~/My Brain/`
3. Type: `ingest the new source in raw/`
4. Claude Code reads the source, creates/updates wiki pages, and logs the run here

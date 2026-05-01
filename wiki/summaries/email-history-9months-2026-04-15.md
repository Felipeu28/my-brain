---
name: email-history-9months summary
description: 9-month email backfill (Jul 2025 – Apr 2026) — 1000 received + 1000 sent (caps), 875 unique contacts
type: summary
tags:
  - graph/leaf
ingested: true
ingested_at: 2026-05-01
---

# Summary — Email History, 9 Months (Jul 15 2025 – Apr 15 2026)

**Type:** summary
**Last updated:** 2026-05-01
**Source:** [[raw/email-history-9months-2026-04-15.md]]
**Related:** [[wiki/summaries/email-history-2months-2026-04-12|2-month email history]], [[wiki/moil/gtm]], [[wiki/moil/customers]]

---

## Summary

9-month bulk email backfill from Microsoft Graph (capped at 1,000 sent + 1,000 received, 875 unique contacts). The backfill predates the structured ingestion pipeline and mostly duplicates contacts already captured in the 2-month and 6-month windows. **Use this file as a contact-frequency reference, not a fact source** — every high-touch contact (5+ emails) already has a structured wiki page.

## Top relationships (5+ emails) — all already in [[wiki/people/]]

| Person | Emails | Wiki page |
|---|---|---|
| [[wiki/people/jacob-oluwole]] | 39 | ✓ |
| [[wiki/people/casey-earley]] | 33 | ✓ |
| [[wiki/people/anita-lansing]] | 29 | ✓ |
| [[wiki/people/megan-miller]] | (high) | ✓ |
| [[wiki/people/adeleke-tolulope]] | (high) | ✓ |
| [[wiki/people/john-costilla]] | (high) | ✓ |
| [[wiki/people/jacquie-martinez]] | (high) | ✓ |
| [[wiki/people/becky-torres]] | (high) | ✓ |

Plus internal Moil aliases (`noreply@`, `cs@`, `Andres@moilapp.com`) which are infrastructure not contacts.

## What this file is NOT useful for

- **Decision tracking** — too coarse. Decisions live on the meeting/people pages.
- **Pipeline status** — superseded by [[wiki/moil/pipeline]] + [[wiki/moil/customers]].
- **HIVE cohort tracking** — superseded by [[wiki/people/hive-cohort-members]] + [[wiki/orgs/buda-edc]].

## When to reach for this file

Only if you need **contact-frequency over a 9-month window** (e.g., "who has emailed Andres ≥5 times in the last 9 months that does NOT yet have a wiki page?"). Use `python3 scripts/kb-health.py` to spot orphan contacts before reaching for this file.

## Connections

- [[wiki/summaries/email-history-2months-2026-04-12]] — finer-grained 2-month window
- [[wiki/summaries/outlook-emails-2026-04-09]] — original 10-day snapshot
- [[wiki/moil/gtm]] — outbound campaign log lives here

# Morning Briefing — Canonical Schema

**Version:** 1.0
**Locked:** 2026-04-22 (based on stable output from Apr 13 → Apr 22)
**Owner:** Brain UI parser contract

This document declares the **canonical shape** of a morning briefing. The Brain UI parser depends on this shape. `kb-health.py` should verify every new briefing conforms. If the briefing generator needs to change, update this schema *first*, then the generator, then the parser — in that order.

## File location & naming

```
{KB}/quartz/content/raw/briefings/briefing-YYYY-MM-DD.md
```

where `{KB}` = `~/My Brain/knowledge-base`.

One briefing per weekday (Mon–Fri). Weekends intentionally skipped.

## YAML frontmatter (required)

```yaml
---
date: YYYY-MM-DD          # REQUIRED — must match filename
type: morning-briefing    # REQUIRED — literal string
---
```

Fields MAY be added (e.g. `actions:` for pre-emitted IDs in Phase 3+). No fields may be removed.

## Required H2 sections, in order

The parser expects these `##` headers, in this order. Order matters because some parsers use section boundaries to delimit content.

| # | Header | Presence |
|---|---|---|
| 1 | `# Morning Briefing — <Weekday>, <Month> <Day>, <Year>` | REQUIRED (H1) |
| 2 | `## Schedule (Central Time)` | REQUIRED |
| 3 | `## Inbox (N unread)` (N = integer) | REQUIRED |
| 4 | `## Today's Priorities` | REQUIRED |
| 5 | `## People Notes` | REQUIRED |
| 6 | `## Code Activity (last 24h)` | OPTIONAL |
| 7 | `## Awaiting Reply (3+ days, no response)` | OPTIONAL |
| 8 | `## Going Cold (key contacts with no sent email in 14+ days)` | OPTIONAL |
| 9 | `## Deals Going Stale (pipeline last-touch >7 days)` | OPTIONAL |
| 10 | `## Brain Says` | REQUIRED (exactly once) |

**Optional** = may be absent when there's nothing to report for that section. When present, must match the header text exactly (subject to the tolerances below).

### Header text tolerance

The parser is STRICT about these tokens:
- `Schedule`
- `Inbox`
- `Today's Priorities` → or `## Priorities`
- `People Notes`
- `Code Activity`
- `Awaiting Reply`
- `Going Cold`
- `Deals Going Stale`
- `Brain Says`

Everything after the first required token on the H2 line is tolerated (e.g., `## Inbox (15 unread)` vs `## Inbox — 15 unread` both accepted).

## Section content rules

### Schedule
Either bulleted list OR table. Each row must have a time.

```
- **8:00 AM – 9:00 AM** · Event · Who · Notes
```

### Inbox
MUST have 3 sub-buckets as bold labels:
```
**Action needed:**
- …

**FYI:**
- …

**Can wait:**
- …
```

`FYI` and `Can wait` may be empty. `Action needed` should always have at least one bullet or the text "None."

### Today's Priorities
Numbered list, 1–3 items. Each item is typically bold-intro-then-detail:

```
1. **Priority name.** Detail paragraph…
```

### People Notes
Bulleted list. Each bullet MUST start with a bold name:

```
- **Person Name** — Role/context sentence.
```

### Code Activity
Structured bulleted list. Categories (optional H3s allowed):
- Client repos worked on
- Product repos active
- Open PRs
- Red flags

### Awaiting Reply
Either bulleted list OR table. If table, columns: Contact | Subject | Sent | Days.

### Going Cold
Table with columns: Contact | Role | Why it matters (or Notes).

### Deals Going Stale
Either table OR bulleted list.

### Brain Says
Prose section — 1 to 3 short paragraphs OR a numbered "top 3" list.

**Currently duplicated** (known bug): LLM emits one, shell script appends a second via `brain-query.sh`. Must be resolved to exactly one Brain Says section. See spawned task for fix.

## Forbidden content

- No HTML (except in tables where markdown requires it)
- No images (briefings are read in plaintext email)
- No nested code blocks
- No section headers deeper than H3
- No emoji-only bullets

## Wikilinks

Wikilinks are ENCOURAGED and the parser uses them:

```
[[wiki/people/megan-miller]]
[[wiki/orgs/helotes-edc|Helotes EDC]]
[[MEMORY]]
```

Escaped pipes (`[[foo\|bar]]`) are FORBIDDEN (per KB rules in `CLAUDE.md`).

## Validation — what kb-health should check

Add a new check `check_briefing_schema()` to `scripts/kb-health.py`:

1. ✅ File exists at expected path for every weekday in the last 14 days.
2. ✅ Frontmatter present with `date` matching filename and `type: morning-briefing`.
3. ✅ H1 title present and matches `# Morning Briefing — ...`.
4. ✅ Required H2 sections (`Schedule`, `Inbox`, priorities, people notes, Brain Says) all present.
5. ✅ Exactly one `## Brain Says` section (no duplicates).
6. ✅ No sections deeper than H3.
7. ✅ No escaped-pipe wikilinks.
8. ⚠ Warn if any optional section is always absent over the last 5 briefings — might indicate a pipeline regression.

Exit codes: 0 = pass, 1 = at least one REQUIRED rule failed (block CI), 2 = only warnings.

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-04-22 | Initial lock, based on stable output Apr 13–22 |

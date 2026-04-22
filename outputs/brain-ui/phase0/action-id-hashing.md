# Action ID Hashing — Specification (Phase 0)

**Created:** 2026-04-22

## Problem

Briefings are LLM-generated prose. The same underlying action ("ping Jacquie about the HIVE contract") can appear in different words on Monday vs Tuesday. For the Brain UI's feedback loop to work, we need a stable ID that:

1. **Collides** when it's the same action on a different day (so completion persists).
2. **Does NOT collide** when it's a different action, even if the same person/entity is mentioned.
3. **Does NOT require** the LLM to emit stable IDs (Phase 0 / 1 / 2 — we may add that as a Phase 3+ hardening, but must work without it now).

Pure text hashing fails — text drifts. Pure entity hashing fails — two different actions can be about the same person.

## Solution: composite hash of (section, primary_entity, intent)

```
action_id = sha256(
  section_key + "|" +
  primary_entity_normalized + "|" +
  intent_verb + "|" +
  disambiguator
).hex.slice(0, 12)
```

### Components

#### `section_key`
The H2 section the bullet appeared under, normalized to a canonical slug:

| Briefing header | section_key |
|---|---|
| `Today's Priorities` | `priorities` |
| `Inbox (N unread)` → `Action needed:` | `inbox_action` |
| `Inbox (N unread)` → `FYI:` | `inbox_fyi` |
| `Inbox (N unread)` → `Can wait:` | `inbox_wait` |
| `Awaiting Reply (...)` | `awaiting_reply` |
| `Going Cold (...)` | `going_cold` |
| `Deals Going Stale (...)` | `stale_deal` |
| `One Thing` | `one_thing` |
| `Brain Says` | `brain_says` |
| `Code Activity (last 24h)` | `code_activity` |
| `People Notes` | `people_notes` |

#### `primary_entity_normalized`
The most salient named entity in the bullet:

**Extraction order** (take the first that matches):
1. Wikilink target — `[[wiki/people/megan-miller]]` → `megan-miller`
2. Bolded name at start — `**Megan Miller** — ...` → `megan-miller`
3. Table cell (for tables) — first column text → slugified
4. Known deal/project names from wiki (pre-seeded list) — `Buda HIVE` → `buda-hive`
5. First proper-noun phrase in the bullet (capitalized word sequence)
6. Fall back to `null`

**Normalization:**
- lowercase
- strip punctuation
- replace whitespace with `-`
- strip diacritics (ñ → n)
- Known alias table: `fit-logic` = `fitlogic`, `buda-edc` = `buda-economic-development-corporation`

#### `intent_verb`
The verb that captures what the user needs to do:

**Controlled vocabulary** (pick the best match; fall back to `other`):

```
fix · ping · text · email · reply · review · confirm · send · book
prep · draft · follow_up · schedule · sign · pay · check · verify
post · publish · close · archive · update · investigate · other
```

**Extraction:** scan the bullet for the first verb matching this list (case-insensitive). Lemmatize via a small static map (`pinged` → `ping`, `fixing` → `fix`, `replied` → `reply`, etc.).

For sections where the intent is implicit, use the section's default intent:

| section_key | default intent |
|---|---|
| `going_cold` | `ping` |
| `awaiting_reply` | `follow_up` |
| `stale_deal` | `check` |
| `inbox_action` | `reply` |
| `code_activity` | `review` |
| `people_notes` | `other` |

#### `disambiguator`
For sections where (section, entity, intent) might still collide on different actions, add a short discriminator:

- `priorities`: position number (`1`, `2`, `3`)
- `inbox_action` with same entity appearing twice: subject line hash (first 4 hex chars)
- default: empty string

## Pseudocode

```typescript
function hashAction(bullet: ParsedBullet): string {
  const section = bullet.section;                          // already slugged
  const entity  = extractPrimaryEntity(bullet) ?? "none";
  const intent  = extractIntent(bullet) ?? defaultIntent(section);
  const disamb  = disambiguator(bullet, section);

  const key = `${section}|${entity}|${intent}|${disamb}`;
  return sha256(key).slice(0, 12);
}
```

## Test fixtures

Each fixture is a (bullet, expected_id_inputs) tuple. Collision pairs should produce the same ID; non-collision pairs must not.

### COLLIDE — same action across days

```
A1 (briefing-2026-04-12 · Going Cold table):
  "**Travis Sutherland** · Zoiwell / Sun Show host · Sun Show is Fri Apr 24 …"
  → section=going_cold, entity=travis-sutherland, intent=ping → ID_X

A2 (briefing-2026-04-22 · Going Cold table):
  "**Travis Sutherland** · Sun Show host · 2 days out, no confirm sent."
  → section=going_cold, entity=travis-sutherland, intent=ping → ID_X  ✅
```

```
B1 (briefing-2026-04-12 · Today's Priorities #1):
  "**HIVE Contract — Board votes Wednesday Apr 15**…"
  → section=priorities, entity=buda-hive, intent=confirm, disamb=1 → ID_Y

B2 (briefing-2026-04-22 · Today's Priorities #3):
  "**Buda HIVE Cohort 4 + contract.** Still no signed contract…"
  → section=priorities, entity=buda-hive, intent=confirm, disamb=3 → ID_Y'
```

**NOTE:** B1 and B2 produce different IDs because disambiguator differs (1 vs 3). This is a **known limitation**. Mitigation: for `priorities`, if entity+intent match across a 7-day window, treat as same action regardless of position. This is a fuzzy-match pass implemented at parse time, not in the hash.

### DO NOT COLLIDE — different actions, same entity

```
C1 (briefing-2026-04-22 · Priorities #2):
  "**Megan / FitLogic — 11 AM working session.** Fix fit-logic Vercel red deploy…"
  → section=priorities, entity=megan-miller, intent=fix, disamb=2

C2 (briefing-2026-04-22 · People Notes):
  "**Megan Miller / FitLogic** — Active Moil 360 customer…"
  → section=people_notes, entity=megan-miller, intent=other
```
Different sections → different IDs ✅

### DO NOT COLLIDE — same section, different intents

```
D1 (Priorities #1): "Fix Stripe webhook delivery failures"
  → section=priorities, entity=stripe, intent=fix, disamb=1

D2 (Priorities #2): "Reply to Stripe support about dispute"
  → section=priorities, entity=stripe, intent=reply, disamb=2
```
Different intents → different IDs ✅

## Fuzzy matching layer (on top of hashing)

Hashing is primary. Fuzzy match is a secondary "did we miss a collision?" pass:

When parsing a new briefing, for each action A with no prior match:
1. Find candidate actions with same `section` and `primary_entity` from the last 7 days.
2. If any candidate has Levenshtein ratio > 0.6 against the normalized text, treat as same action — reuse its ID instead of the new hash.
3. Log to `events` table as `id_unified` for audit.

This catches `priorities` disambiguator drift (B1/B2 above) and cases where the LLM used different entity phrasing on different days ("Buda HIVE" vs "HIVE Cohort 4").

## Long-term hardening (Phase 3+)

Have the briefing generator emit stable IDs in frontmatter:

```yaml
---
date: 2026-04-22
type: morning-briefing
actions:
  - id: priority-1
    section: priorities
    entity: helotes-edc
    text: "Helotes EDC / Kate Silvas — 10 AM call"
---
```

Then the parser trusts the generator's IDs directly and the hashing becomes a fallback for legacy briefings. Not in scope for Phase 0–2.

## Normalization helpers (implementation notes)

```typescript
// Strip ephemeral content from text before comparing
function normalize(text: string): string {
  return text
    .replace(/\[\[([^\|\]]+)\|([^\]]+)\]\]/g, "$2")   // [[x|y]] → y
    .replace(/\[\[([^\]]+)\]\]/g, "$1")                // [[x]] → x
    .replace(/\b\d+\s*(days?|hours?|weeks?|months?)\s*(out|ago|silent|stale)?\b/gi, "")
    .replace(/\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\w*\b/gi, "")
    .replace(/\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{1,2}(,?\s*\d{4})?\b/gi, "")
    .replace(/\b\d{4}-\d{2}-\d{2}\b/g, "")
    .replace(/[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/gu, "")   // emoji
    .replace(/[*_`~]/g, "")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}
```

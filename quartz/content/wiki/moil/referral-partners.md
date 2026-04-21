---
status: active
tags:
  - graph/hub
---
# Moil — Referral Partners Ledger

**Type:** moil-topic (canonical hub)
**Last updated:** 2026-04-15
**Source:** m365 email analysis, [[wiki/people/daniel-mann]]
**Related:** [[wiki/andres/ANDRES]], [[wiki/moil/customers]], [[wiki/moil/gtm]], [[wiki/moil/pipeline]]

---

> **Purpose:** Relationships die in silence. This ledger keeps every person who has sent Moil warm business top-of-mind, tracks their referral ROI, and enforces a reciprocation + check-in cadence so these connections compound over time.

---

## 🌟 Active Referral Partners

### Tier A — Confirmed production channels (3+ referrals, active ROI)

| Partner | Company | # Intros | P1 Conversions | Last partner touch | Next touch due |
|---------|---------|----------|----------------|--------------------|----------------|
| [[wiki/people/daniel-mann|Daniel Mann]] | [[wiki/orgs/evermend-group|Evermend Group]] | **8** | 1 (Jacob Centeno) | 2026-03-18 | **🔥 Overdue 28 days** — quarterly check-in |

### Tier B — Confirmed partners (1–2 referrals)

*(none yet — upgrade candidates go here)*

### Tier C — Potential (identified but not yet activated)

| Person | Why they could be a referral partner | Status |
|--------|--------------------------------------|--------|
| [[wiki/people/david-levesque|David Levesque]] / Savari Solar | Hungry Hill Foundation + AI community; tagged as "potential referral partner" in meeting notes | Cold — needs nurture |
| [[wiki/people/monica-pena|Monica Pena]] / EGBI / Echo Squad | Hispanic business network, LinkedIn pod | Lapsed — last contact early 2025 |
| [[wiki/people/enrique-castro|Enrique Castro]] / GAHCC | Director of Membership + "El Taco Financiero" podcast | Active partnership; referrals latent |

---

## 📊 Daniel Mann — Referral Scorecard

| Metric | Value |
|--------|-------|
| Total referrals received | 8 |
| Period | 2026-02-13 → 2026-03-27 (~6 weeks) |
| Referral velocity | ~1.3 intros/week |
| Converted to P1 paying | 1 ([[wiki/people/jacob-centeno|Jacob Centeno]] / Titan Tech) |
| Converted to pipeline | 2 ([[wiki/people/oscar-esquivel|Oscar/Alloy]], [[wiki/people/rashaka-boykins|Rashaka Boykins]]) |
| Still warm | 4 (Dr. Oriakhi, Alison, Jim, Brittany) |
| Professional resource | 1 ([[wiki/people/john-mcconnell|John McConnell]]) |
| P1-revenue ROI attributable | $180/yr (direct) + Alloy in-closing |

Full ledger: see [[wiki/people/daniel-mann]].

---

## Reciprocation Ledger — what Moil has sent back

| Partner | Moil sent | Date | Outcome |
|---------|-----------|------|---------|
| Daniel Mann | *(TBD — backfill; quarterly thank-you scheduled)* | — | — |

---

## Cadence Rules

1. **Every Tier A partner gets a 30-day "no activity" flag** — if no email or meeting in 30 days, it surfaces in morning briefings
2. **Quarterly thank-you** — schedule calendar reminder every 90 days (independent of deal flow)
3. **Reciprocation check** — every time a partner sends an intro, add a `reciprocation: pending` row. Track until Moil has sent something back
4. **Upgrade path** — Tier C → B at 1 confirmed intro; B → A at 3 intros OR 1 P1 conversion

---

## Morning Briefing Integration (proposed for Phase G.2)

Add a "Referral Partner Radar" section to the morning briefing that surfaces:
- Any Tier A partner with no activity in 30+ days
- Any open reciprocation (we owe a partner something)
- Any new warm intro from a partner that hasn't been followed up in 14 days

See [[wiki/people/daniel-mann#Next Actions]] for the source of truth on Daniel's specific follow-ups.

---

## How to add a new referral partner

1. Create their `wiki/people/{name}.md` with `tags: person/referral-partner`
2. Add `referrals:` list to their frontmatter listing everyone they've sent
3. For each referral, update the referral's own page with `referred_by:` pointing to the partner page
4. Add a row to Tier A/B/C above based on volume/conversion
5. Run `kb-health.py` — no broken links should result

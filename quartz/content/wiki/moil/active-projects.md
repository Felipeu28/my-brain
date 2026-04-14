---
status: active
tags:
  - graph/hub
---
# Moil — Active Projects

**Type:** moil-topic
**Last updated:** 2026-04-14
**Source:** [[raw/github-activity]] + pipeline + Teams + email
**Related:** [[wiki/moil/pipeline]], [[wiki/moil/customers]], [[wiki/orgs/buda-edc]]

---

> **Ground truth for active work.** GitHub activity is the primary signal — if we're pushing code to a repo, that project is top of mind. Updated by morning briefing + weekly compile.

---

## Tier 1 — Active Client Work (GitHub + Business Activity)

These clients have both GitHub activity AND live business engagement.

### Fit Logic / Megan Miller
- **Client:** Megan Miller (meganmillernp@gmail.com) — NP, hormone expert
- **Repo:** `Moil-Landingpages/FitLogic` → [[wiki/orgs/fitlogic]]
- **Business status:** 6+ coaching sessions (Jan–Mar 2026), active Moil user (hiring platform)
- **Last code touch:** Active (per github-repos.yaml)
- **Last business touch:** 2026-03-20
- **Next:** Confirm first hire. Platform feedback loop ongoing.

### Meridian Buda
- **Repo:** `Moil-Landingpages/meridian-buda` → [[wiki/orgs/meridian-buda]]
- **Business status:** Active client site
- **Last code touch:** Active (most recent GitHub activity)
- **Next:** Monitor Stripe webhook status

### Buda EDC / HIVE
- **Repo:** `Moil-Landingpages/BUDAEDC` → [[wiki/orgs/buda-edc]]
- **Business status:** Cohort 4 starts Apr 20, 2026. SXSW run of show done.
- **Coaching clients:** Terry, Laura, Sarah, Carol, Megan, Liz, Miguel → [[wiki/people/hive-cohort-members]]
- **Revenue:** Per-cohort license (B2G), active
- **Last business touch:** 2026-04-13 (Apr 1 networking event, Apr 15 board vote)
- **Next:** Cohort 4 onboarding materials

### Siren Beauty & Wellness (Becky Torres)
- **Repo:** `Moil-Landingpages/SirenBeauty` → [[wiki/orgs/siren-beauty]]
- **Client:** Becky Torres (sirenbeautyandwellness@gmail.com)
- **Business status:** $2,200 payment Apr 6, account setup in progress
- **Last code touch:** Active
- **Last business touch:** 2026-04-06
- **Next:** Jacob confirming account setup. Strategy plan deployed.

### Connectex (Mark Polanco)
- **Repo:** `Moil-Landingpages/Connectex` → [[wiki/orgs/connectex]]
- **Client:** Mark Polanco (mark@connectex.net), CEO — Austin
- **Business status:** CLOSED Apr 9. Multi-quarter invoice.
- **Last code touch:** Active
- **Last business touch:** 2026-04-09
- **Next:** Verify payment schedule + deliverables spec

---

## Tier 2 — Active Product Development

Core Moil platform — active engineering.

### Employer Platform (Beta)
- **Repo:** `Moil-Code/employer-platform` (or equivalent)
- **Status:** Beta — Megan Miller using it actively. Stripe webhook issue (Meridian)
- **Active issues:** Applicant contact info not visible to employers, notification UX unclear
- **Next:** Fix applicant visibility bug (surfaced by Megan)

### Business Plan Creator
- **Repo:** `Moil-Code/business-plan-creator`
- **Status:** Staging — used by HIVE cohort participants
- **Next:** Test with Cohort 4

### Moil360 (Moil Business Platform)
- **Status:** Closed Travis Sutherland deal (Apr 9). Live client onboarding.
- **Active clients:** Travis / Zoiwell, Jilledegs01, Liz/Miguel (HIVE post-cohort)
- **Issues:** License activation flow has a candidate/business side confusion bug
- **Next:** Fix the license activation bug (Miguel hit it twice in Feb 13 session)

---

## Tier 3 — Active Internal / Infrastructure

### Brain (This System)
- **Repo:** `Felipeu28/pi-workspace` (approx)
- **Status:** Active. 9 launchd automations running.
- **Automations:** Morning briefing, email digest, Teams pull, weekly compile, weekly pulse, X bookmarks, content calendar, ChromaDB index, heartbeat
- **Next:** Fix x-bookmarks (requires manual Keychain dialog)

### KidsGPT
- **Status:** Files in OneDrive (README, implementation-plan, options-analysis). Not yet ingested.
- **Next:** Ingest these 3 files and create a wiki page

---

## Tier 4 — Needs Context (Unmapped Repos)

Active GitHub repos without wiki pages or known client context:

| Repo | Active? | Need to ask Andres |
|---|---|---|
| `Felipeu28/lunabella` | TBD | What client? Still active? |
| `Felipeu28/fantelo` | TBD | What is Fantelo? |
| `Felipeu28/magical-reading-adventures` | TBD | What is this? Product? |

---

## How This Page Gets Updated

1. **Morning briefing** injects GitHub activity summary (last 24h) — active repos = top of mind
2. **Weekly compile** reconciles GitHub activity with pipeline
3. **Andres** adds/moves projects manually when scope changes

> **Signal hierarchy:** GitHub commit in last 7 days = active. No commit in 30 days = idle. No commit in 90+ days = archived.

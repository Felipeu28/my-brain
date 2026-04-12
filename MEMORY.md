# MEMORY — Open Actions & Live Commitments

**Last updated:** 2026-04-12
**Purpose:** Single source of truth for open action items extracted from ingested raw sources. Claude Code updates this file during ingestion runs.

> For relationship and concept context, see [[index]]. For ingestion history, see [[log]].

---

## 🧹 Review rhythm (keeps MEMORY.md from rotting)

| Cadence | Action |
|---|---|
| **Weekly (Friday, 15 min)** | Walk through every `[ ]`. Strike `~~done~~` with date. Move items stale >2 weeks to "Closed / Archive". Add new actions from the week's iMessages/Outlook pulls. |
| **Monthly (1st of month)** | Prune "Closed / Archive" — keep only items useful as precedent; delete the rest. Reconcile deferred items against the current week. |
| **Quarterly** | Full audit: does every open item still matter? Kill anything that no longer serves a live goal. |

**Hard rule:** if MEMORY.md exceeds 200 lines, pruning is overdue. Don't let it drift.

**Closing an item:** use `~~strikethrough~~` + `(YYYY-MM-DD)` inline. After a week, move the whole bullet to "Closed / Archive". After a month, delete unless it's a useful precedent.

---

## 🔥 Immediate — This Week (Apr 11–17, 2026)

### Buda HIVE / EDC — dual Apr 15 deadline
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [ ] **Apr 14 · 10:30am–12:00pm CDT** — Prep meeting with Joshua Edmond at Buda HIVE (Teams ID 270 650 313 421 234). Coordinate final stance before Board review.
- [ ] **Apr 15** — EDC Board vote on Incubator Strategist contracts (Moil Enterprises Inc. + FAVE&SAVE LLC). Be available for questions/revisions.
- [x] **Apr 15** — AEDO letter submission — ~~SIGNED & SUBMITTED Apr 10~~ (Jennifer Storm: "This is perfect!")
- [ ] **Apr 20 → Jun 8** — Cohort 4 begins (every Monday). Prep session materials. [[wiki/people/casey-earley]] is a participant.

### Product UX bug — applicant visibility
Source: [[wiki/summaries/imessages-people-2026-04-09]] (Megan Miller feedback)
- [ ] Fix gap: employer cannot see applicant phone/email in Moil. Unclear notification system when candidate messages via Moil.
- [ ] Reply to Megan Miller with a short-term workaround + ETA.

### Open PRs (code hygiene)
Source: [[wiki/summaries/github-project-tracker]]
- [ ] Review + merge PR on `Moil-Code/Blog`
- [ ] Review + merge PR on `Moil-Landingpages/Inna-CRM`

---

## 📅 Next 2–3 weeks (Apr 18 – May 2)

### Travis Sutherland — Sun Show demo
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] **Apr 24 · 7–9pm** — Moil demo booth at the Sun Show. Set up screen + flyers. Confirm logistics with Travis.

### Daniel Guadiano — Astra Restaurant
Source: [[wiki/summaries/outlook-emails-2026-04-09]]
- [ ] Reply to Daniel (Apr 9 inquiry). Offer a 30-min scheduling demo tailored to restaurant ops. Phone 210.978.4483.
- [ ] If it closes, write a restaurant case study — first hospitality ICP data point.

### Inna Benyukhis — Calendly
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] Confirm meeting slot: **Mon Apr 13 10am** or **Friday after 2pm**. In-person, 60 min.

### Mark Polanco — Airtable access
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] Airtable invite hadn't arrived as of Apr 9. Follow up if still blocked.

### Ana Vetencourt — URBANZUELA website
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] Review the Google Doc draft Ana sent. Provide feedback.

### John Costilla — Apr 10 photo shoot
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [x] **Apr 10 · 10:15am** — Photos with John. ~~Presumed done~~ (today is Apr 11; verify + archive if complete)

---

## 🔔 New from meetings ingestion (2026-04-12) — 25 OneDrive transcripts

Source: [[raw/meetings/]] — Aug 2024–May 2025 meeting recordings

### Historical action items (may be complete — verify)

**Product / Engineering**
- [ ] Verify: Azure access issue for Adeleke resolved? (Andres submitted support case ~May 2025)
- [ ] Verify: Job matching algorithm weighted update deployed to production? (Adeleke confirmed Apr 9)
- [ ] Verify: Google → Microsoft migration completed? (Deadline was May 5, 2025)
- [ ] Verify: HubSpot full access granted to Jacob after May 15, 2025?

**Business Plan Creator bugs (from May 2025 — check current status)**
- [ ] Customer persona pipeline fixed (personas passing to o3-mini)?
- [ ] TAM/SAM calculation validated?
- [ ] Competitor map moved to competitor section?
- [ ] Cost structure personalization (dropdown) added?
- [ ] Milestone completion/tracking added?
- [ ] Plan display default fixed for subscribed users?

**Interview Tool**
- [ ] MVP development started? (Andres said to build without design first — May 2025)

**Social Media Automation**
- [ ] Auto-generate social post on job creation (Grok + template) — built?

**Marketing**
- [ ] Sebastian Oviedo 4-week marketing engagement completed? (Started Apr 28, 2025 — 4 weeks = ~May 26)
- [ ] June 2025 Manos De Cristo workshops — delivered? (3 Fridays in June: 13, 20, 27)

**Clients**
- [ ] Sakuri Corporation — ALL Texas job listings organized by city and posted? (Jacob assigned)
- [ ] Zachary / Great Construction Corp — account active and delivering job postings?

**UTSA License Opportunity**
- [ ] EDC contact intro to UTSA for Business Plan Creator license — followed up?

**Team**
- [ ] Family emergency — check in with Abiodun Solomon (Ablad) after hospital visit (Apr 2025)

---

## 🔔 New from Teams ingestion (2026-04-12)

Source: [[wiki/summaries/teams-2026-04-12]]
- [ ] **Future pull:** Request a new Teams export that includes human responses in `#attendance-n-break` and all project/team threads — this will unlock full Moil team roster + compliance patterns. Current pull only captured bot messages.
- [ ] **Investigate `#Alerts` channel:** Had a header in the 30-day pull but zero messages. What is it used for? Could be critical operational alerts.

---

## 🎯 Monthly — Brain System hygiene

Source: [[wiki/summaries/brain-guide]] / [[wiki/concepts/brain-architecture]]
- [ ] Confirm Monday 9am X bookmark sweep is scheduled in Claude Cowork (Collection layer).
- [ ] Consolidate duplicate bookmark files — [[wiki/summaries/x-bookmarks-2026-04-11]] (114) vs [[wiki/summaries/x-bookmarks-2026-04-11-copy]] (129). Prefer the 129 version for future synthesis.
- [ ] Write `MOIL.md` context file (Mission / Operating Principles / Identity / Legacy) and seed as primer for major Claude queries.
- [ ] Run Prompt 1 (Claude) from [[wiki/summaries/know-me-extraction-prompts]] → produce first `andres-intelligence-brief-[date].md` → drop in `raw/` → ingest.
- [ ] Monthly Layer 4 synthesis: feed 4 most-recent bookmark digests to Claude for patterns & belief shifts. Output → `outputs/synthesis-YYYY-MM.md`.

---

## 💤 Deferred — Calendar reminders

### Shay Foley / Johns Creek Chamber
Source: [[wiki/summaries/outlook-emails-2026-04-09]], [[wiki/people/shay-foley]]
- [ ] **Jul 1, 2026** — Re-engage. Pitch AI tools for entrepreneurs using Buda EDC as reference customer + Jennifer Storm AEDO-grade endorsement. Chamber budget year starts this day.

### CampaignOS with Jennifer Storm
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]], [[wiki/concepts/campaignos]]
- [ ] After Apr 15 deadlines clear, circle back on MVP scope. Andres offered "little to no cost" — decide commitment level before building.

### CoffeeSpace partnership
Source: [[wiki/summaries/outlook-emails-2026-04-09]], [[wiki/orgs/coffeespace]]
- [ ] Low priority. Nurture. Only book a call if calendar is light and Moil's candidate platform is ready for distribution partners.

### Training program curriculum (Buda HIVE)
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [ ] **Sep 1, 2026** deadline (per Joshua's contract). Jointly develop with HIVE + Incubator Strategist Team.

---

## 🏗️ Strategic — No hard deadline but worth deciding

### Fantelo clarification
Source: [[wiki/concepts/fantelo]]
- [ ] Decide: is Fantelo a future pivot, separate venture, or sub-brand of Moil? Currently consumes engineering time (private repo pushed Apr 9) with no wiki-documented strategy.

### Moil360 vs Content360 naming
Source: [[wiki/concepts/moil360]], [[wiki/concepts/content360]]
- [ ] One-name policy: decide whether the 30-day marketing engine is "Content360" (product-site name) or "Moil360" (consumer brand at moilapp.com/marketing). Currently inconsistent across copy.

### GitHub org cleanup
Source: [[wiki/summaries/github-project-tracker]]
- [ ] Archive 6+ stale repos (Moil-landing-beta, New-Prod-Landing, Moil-codeLandingPage, Moil-nextjs-landing, Mailing-service, flaskModelStaging, model-server-flask).
- [ ] Dedupe BlueprintsForSuccess / Blueprintforsuccess.
- [ ] Consider creating a fourth org `Moil-Clients` and moving queen-creek, buda-hive, KyleBudaSpotlight, REFERREDLOCAL, omaha-client-boost, connectex-website there.
- [ ] Standardize naming convention (kebab-case lowercase).

### Moil license case study
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [ ] Build a public case study: "City EDC × Moil — per-seat licensing for incubator cohorts." Use for investor decks and expansion to Queen Creek / Johns Creek / Greater Buda Chamber.

### Claude Code security audit
Source: [[wiki/concepts/claude-code]]
- [ ] Review what permissions Claude Code has on the Mac Mini M4 (SSH config, AWS creds, `.env` files). Decide boundaries before running autonomous skills.

---

## ✅ Closed / Archive

*(Items move here after they're marked complete and confirmed stable for a week.)*

- [x] **2026-04-10** — AEDO support letter drafted, signed, submitted to Jennifer Storm. Reply: "This is perfect!" — source: [[wiki/summaries/buda-hive-edc-2026-04-11]]

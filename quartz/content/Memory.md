# MEMORY — Open Actions & Live Commitments

**Last updated:** 2026-04-19 (Run 14 — Email digest Apr 17: Cohort 4 curriculum flowing, 25+ outbound, tax review pending)
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

## 🔥 Immediate — This Week (Apr 18–24, 2026)

### Delivery-pace escalation — from Teams Apr 17–18
Source: [[wiki/meetings/2026-04-18-teams-daily-ops]]
- [ ] **Jacob: fix Business Coach "not responding" bug** — blocked his own testing loop Apr 18
- [ ] **Jacob: start Connectex** — flagged as top priority that slipped past the week's focus on Meridian + FitLogic
- [ ] **Jacob: send follow-up emails** to Moil 360 license recipients who have NOT activated
- [ ] **Adeleke: review Claude Code audit session** (`session_01PP9t1m41A2snaRRACs3TNs`) — verify nothing broken; revert if so
- [ ] **Taiwo: rework demo prompt context** — ask Andres for business-specific context (prior version drove everything from business plan as single source of truth)
- [ ] **Taiwo / Andres: reschedule delivery calls** to reasonable hours in Taiwo's time zone (not 11pm / 2am local)
- [ ] **Abiodun: deliver next week's Moil + Inna content by Sun Apr 19** (Andres explicit deadline)
- [ ] **Abiodun + Andres: align on content rhythm** — Tuesday push / Sunday review (cushion ahead), not trickled daily
- [ ] **Andres: fix architectural regression** — current app no longer uses business plan as single source of truth the way the prior version did

## 🔥 Carried over from last week (Apr 11–17, 2026)

### Buda HIVE / EDC
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]], [[raw/email-digest-2026-04-15]]
- [ ] **🔥 EDC AI-tools-for-website call** — John Costilla + [[wiki/people/joseph-arnke|Joe Arnke]] (GIS WebTech) re: Moil AI → EDC site-selector. See [[wiki/orgs/buda-edc]].
- [ ] **Apr 20 → Jun 8** — Cohort 4 begins (every Monday). Prep materials. Casey Earley is participant.

### API Spend Crisis — URGENT
Source: [[wiki/meetings/2026-04-15-teams-daily-ops]]
- [ ] **🔥 Adeleke: audit entire Moil codebase** for OpenAI API usage; migrate gpt-4o → gpt-5-mini (token refill went monthly → 3x/week)
- [ ] Rotate API keys after audit complete

### Moil 360 License Distribution — rolling
Source: [[wiki/meetings/2026-04-15-teams-daily-ops]], [[wiki/meetings/2026-04-18-teams-daily-ops]]
- [ ] **Jacob: verify activation status** for Megan Miller, Mark Polanco, Becky Torres, Roxana Yglesias, Jill/PureSerenity, Alloy ATX (invite finally sent Apr 18)
- [ ] Draft individual onboarding emails to each new license holder

### Renee Simmons / Hays CISD — Career Day May 7
Source: [[raw/email-digest-2026-04-14]]
- [ ] **May 7 — Career Day presentation** at CHES, ~20 min to 4th/5th graders. Prep kid-friendly entrepreneurship talk. See [[wiki/people/renee-simmons]]

### Pflugerville Mentor Day
Source: [[raw/email-digest-2026-04-14]]
- [ ] **Respond to Adam Maxon** (adamm@pfdevelopment.com) about Pflugerville Mentor Day. See [[wiki/people/adam-maxon]]

### Buda Retail Roundup — Apr 20
Source: [[raw/email-digest-2026-04-14]]
- [ ] **Apr 20 — Buda Retail Roundup** invitation from Jacquie Martinez. Decide attendance.

### GitHub Webhook Secrets Rotation
Source: [[raw/email-digest-2026-04-14]]
- [ ] **Adeleke + Jacob: rotate webhook secrets** per GitHub security alert (forwarded Apr 14)

### Jesutomilola Omoniyi / Google xWF — reschedule
Source: [[raw/email-digest-2026-04-15]], [[wiki/people/jesutomilola-omoniyi]]
- [ ] **Reply to Jesutomilola** — two Apr 15 follow-ups trying to reschedule; offered calendar link and then phone/chat ("email not best way"). Pick a time next week or next month.

### Tax review — DLC Financial
Source: [[raw/email-digest-2026-04-17]]
- [ ] **Review 2025 1040** in TaxDome — Melissa Jarbo back from sick leave, created separate TaxDome profile; new secure message from Martin Kutac; Ingrid refund/liability form flagged.

### Buda HIVE Cohort 4 curriculum prep — rolling
Source: [[raw/email-digest-2026-04-17]]
- [ ] Review Joshua Edmond's Apr 17 Weeks 1 & 2 print-outs (Business Model Canvas added to Week 2). Confirm with Casey Earley before cohort opens Apr 20.
- [ ] Confirm edit access to shared Cohort 4 OneDrive folder is being used by the right people (Andres + Joshua + Casey).

### New Social Media Client (unnamed)
Source: [[wiki/meetings/2026-04-15-teams-daily-ops]]
- [ ] Identify the new social media client Andres signed. Confirm Abiodun has capacity to handle additional workload.

### Product UX bug — applicant visibility
Source: [[wiki/summaries/imessages-people-2026-04-09]] (Megan Miller feedback)
- [ ] Fix gap: employer cannot see applicant phone/email in Moil. Unclear notification system when candidate messages via Moil.
- [ ] Reply to Megan Miller with a short-term workaround + ETA.

---

## 📅 Next 2–3 weeks (Apr 18 – May 2)

### Helotes EDC — Kate Silvas call Wed Apr 22 @ 10am CT
Source: [[raw/email-digest-2026-04-16]], [[wiki/orgs/helotes-edc]], [[wiki/people/katherine-silvas]]
- [ ] **Apr 22 @ 10am CT** — Call with Kate Silvas. Lead with Buda EDC case study + per-cohort license model.
- [ ] Build Buda EDC one-pager (pricing, delivery model, Cohort 4 proof) before call.
- [ ] Send proposal after call — mirror Buda EDC Incubator Strategist contract.

### Jacob Centeno — referral partnership
Source: [[raw/email-digest-2026-04-15]], [[wiki/people/jacob-centeno]]
- [ ] Set up lightweight referral workflow with Jacob Centeno — decide commission/credit model for businesses he sends that need social media + Moil.

### Travis Sutherland — Sun Show demo
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] **Apr 24 · 7–9pm** — Moil demo booth at the Sun Show. Set up screen + flyers. Confirm logistics with Travis.

### Daniel Guadiano — Astra Restaurant
Source: [[wiki/summaries/outlook-emails-2026-04-09]], [[wiki/people/daniel-guadiano]]
- [ ] If it closes, write a restaurant case study — first hospitality ICP data point.

### Mark Polanco — Airtable access
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] Airtable invite hadn't arrived as of Apr 9. Follow up if still blocked.

### Ana Vetencourt — URBANZUELA website
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] Review the Google Doc draft Ana sent. Provide feedback.

---

## 🔔 New from Teams ingestion (2026-04-12) — 415 messages, Apr 5–12

Source: [[wiki/summaries/teams-2026-04-12]]

### Roxana / AlloyATX — onboarded Apr 14
Source: [[wiki/meetings/2026-04-14-roxana-alloy-atx-onboarding]]
- [ ] Verify Roxana completed 21 questions + uploaded assets + shared GoDaddy domains (Apr 18 deadline)
- [ ] Next session: set up GSC for alloyatx.com; brainstorm satellite landing page domains; follow up on wellness referrals

### Deals requiring follow-up
- [ ] **Connectex:** Invoice sent? Verify payment schedule (3 quarters). What deliverables? (Still untouched per Apr 18 Teams)
- [ ] **jilledegs01@gmail.com / PureSerenity:** Site deployed (pure-serenity-green.vercel.app). Moil 360 license sent by Jacob. What changes needed?
- [ ] **Siren Beauty:** Verify account setup and Moil 360 activation
- [ ] **Eden:** Website discovery call recorded Apr 8. Follow up on next steps

### Product/Engineering — immediate
- [ ] Tour guide bugs: 2 missing `data-guide-id` attrs, generic text, auto-scroll
- [ ] Segment analytics: `No segment writeKey` error on staging
- [ ] Image context bug: images "forget" conversation context
- [ ] Supabase deploy: `business-intake` edge function needed for go-live
- [ ] Meridian: domain verification + Stripe full flow test needed
- [ ] Phone sign-up: removed (Azure broken) — permanent fix or formal removal

### Content/Marketing
- [ ] **Video production strategy:** Andres wants daily video — plan using AI tools
- [ ] **Sun show attendee email:** "Free year of Moil 360" raffle — was it sent?

### Team management
- [ ] **Adeleke FB account:** Login code issue since Apr 7. Blocks app review video.
- [ ] **Microsoft Planner:** Verify team is using it (created Apr 7).

### Security
- [ ] Migrate credentials out of Teams chat → secure store (1Password/Bitwarden). Stripe keys, Supabase passwords, API keys all in plaintext.

---

## 💤 Deferred — Calendar reminders

### Shay Foley / Johns Creek Chamber
Source: [[wiki/summaries/outlook-emails-2026-04-09]], [[wiki/people/shay-foley]]
- [ ] **Jul 1, 2026** — Re-engage. Pitch AI tools for entrepreneurs using Buda EDC as reference customer + Jennifer Storm AEDO-grade endorsement. Chamber budget year starts this day.

### CampaignOS with Jennifer Storm
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]], [[wiki/concepts/campaignos]]
- [ ] After Apr 15 deadlines clear, circle back on MVP scope. Andres offered "little to no cost" — decide commitment level before building.

### Training program curriculum (Buda HIVE)
- [ ] **Sep 1, 2026** — Jointly develop with HIVE + Incubator Strategist Team.

---

## 🏗️ Strategic — No hard deadline but worth deciding

### Fantelo clarification
Source: [[wiki/concepts/fantelo]]
- [ ] Decide: is Fantelo a future pivot, separate venture, or sub-brand of Moil? Currently consumes engineering time (private repo pushed Apr 9) with no wiki-documented strategy.

### GitHub org cleanup
Source: [[wiki/summaries/github-project-tracker]]
- [ ] Archive 6+ stale repos. Dedupe BlueprintsForSuccess. Consider `Moil-Clients` org.

### Moil license case study
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [ ] Build a public case study: "City EDC × Moil — per-seat licensing for incubator cohorts." Use for investor decks and expansion to Queen Creek / Johns Creek / Greater Buda Chamber.

### Claude Code security audit
Source: [[wiki/concepts/claude-code]]
- [ ] Review what permissions Claude Code has on the Mac Mini M4 (SSH config, AWS creds, `.env` files). Decide boundaries before running autonomous skills.

---

## ✅ Closed / Archive

- [x] **2026-04-18** — FitLogic Apr 18 deadline passed; Daniel Guadiano Apr 16 meeting held (case study pending if deal closes).
- [x] **2026-04-17** — Helotes EDC "reply overdue" auto-resolved. Call booked Apr 22.
- [x] **2026-04-14** — Alloy ATX closed ($75/mo). Moil360 naming resolved.

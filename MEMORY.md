# MEMORY — Open Actions & Live Commitments

**Last updated:** 2026-04-21 (Run 17 — Teams Apr 20–21 + Megan FitLogic CRM onboarding: Moil 360 launch-day firefight, deliverability P0, Connectex finally starts Apr 22, plan-switch bug hits 2nd customer)
**Purpose:** Single source of truth for open action items extracted from ingested raw sources. Claude Code updates this file during ingestion runs.

> For relationship and concept context, see [[index]]. For ingestion history, see [[log]].

---

## 🧹 Review rhythm (keeps MEMORY.md from rotting)

| Cadence | Action |
|---|---|
| **Weekly (Friday, 15 min)** | Walk through every `[ ]`. Strike `~~done~~` with date. Move items stale >2 weeks to "Closed / Archive". |
| **Monthly (1st of month)** | Prune "Closed / Archive" — keep only items useful as precedent; delete the rest. |
| **Quarterly** | Full audit: does every open item still matter? Kill anything that no longer serves a live goal. |

**Hard rule:** if MEMORY.md exceeds 200 lines, pruning is overdue. Don't let it drift.

---

## 🔥 Immediate — This Week (Apr 18–24, 2026)

### 🚨 New from Apr 21 — Moil 360 launch-day firefight + Megan FitLogic CRM onboarding
Source: [[wiki/meetings/2026-04-21-teams-daily-ops]], [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]]
- [ ] **🔥 Andres tonight (Apr 21):** Deploy Moil CRM at `fitlogicfunctionalmedicine.com/CRM` via Megan's GoDaddy; wire `Megan@fitlogicfunctionalmedicine.com` as sender; wipe test contacts; import 5,000-contact Keap CSV
- [ ] **🔥 Andres: surface per-campaign click-rate / open-rate dashboard** for FitLogic (Megan asked)
- [ ] **🔥 Adeleke: ship Gemini→Grok→Qwen multi-model fallback** for video gen; root-cause image-creation latency + intermittent template fails
- [ ] **🔥 Jacob + Andres: fix partners@moilapp.com deliverability** (hit Megan, Roxana, Jill PureSerenity — engineering said "can't optimize it more"; need per-customer sender or infrastructure fix, P0)
- [ ] **🔥 Product: fix business-plan switching UX bug** (hit Megan FitLogic Apr 21 after hitting her weeks ago — class-wide, not one-off; escalate out of manual DB intervention)
- [ ] **Taiwo Apr 22:** Start Connectex (needs CRM URL from Andres); finish FitLogic in parallel; restore day/light mode on coach; surface campaign link-editing (today only in sequences)
- [ ] **Jacob: resend Moil 360 license links** — Megan FitLogic, Siren Beauty, Roxana, Jill PureSerenity (paid $75 Apr 20, never got link)
- [ ] **Andres + Jacob: email every Buda cohort licensee** with Moil 360 feature updates (Andres prompted 12:21 PM Apr 21)
- [ ] **🔒 Security: move `cs@moilapp.com` password off Teams channel** — Jacob posted `Pr0ud**2023$` in the open Moil Team thread Apr 21 11:31 AM; whole team has credentials in plaintext chat
- [ ] **Megan: forward Andres' feedback email to Electric Bricks** (alt-text missing sitewide, no H1, chiro-themed blog URL slugs) as required-changes checklist; mark real clients in Keap; pull remaining EHR contacts; send quiz questions for native Moil rebuild
- [ ] **Joint Megan+Andres:** Decide whether to push or postpone the co-planned workshop (tight window)
- [ ] **Andres: respond to Jacob's PRD proposal** (carried from Apr 19 — still open)
- [ ] **Adeleke: review Claude Code session `session_0156Da69uG1W8jSEof5V2xgb`** (carried from Apr 20)
- [ ] **Jacob: get Inna's decision on IG/LinkedIn tagging approach** — direct access vs. send-and-post (carried)
- [ ] **Andres: respond to Jacob on `Posting Consistently.mp4`** thoughts (carried)

### Delivery-pace carryover — from Teams Apr 17–18
Source: [[wiki/meetings/2026-04-18-teams-daily-ops]]
- [ ] **Jacob: fix Business Coach "not responding" bug** — "stagebeta broken?" surfaced again Apr 21 6:26 PM
- [ ] **Jacob: send follow-up emails** to Moil 360 license recipients who have NOT activated
- [ ] **Taiwo / Andres: reschedule delivery calls** to reasonable hours in Taiwo's time zone (not 11pm / 2am local)
- [ ] **Abiodun + Andres: make content rhythm explicit** — Tuesday push / Sunday review; Abiodun delivered Apr 19 + Apr 21; rhythm still verbal
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

### Moil 360 License Distribution — superseded by Apr 21 items above
See immediate section. Still open: activation verification + onboarding emails per licensee.

### Renee Simmons / Hays CISD — Career Day May 7
Source: [[raw/email-digest-2026-04-14]]
- [ ] **May 7 — Career Day presentation** at CHES, ~20 min to 4th/5th graders. Prep kid-friendly entrepreneurship talk. See [[wiki/people/renee-simmons]]

### Pflugerville Mentor Day
Source: [[raw/email-digest-2026-04-14]]
- [ ] **Respond to Adam Maxon** (adamm@pfdevelopment.com) about Pflugerville Mentor Day. See [[wiki/people/adam-maxon]]

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
- [ ] **Connectex:** Taiwo committed to start Apr 22 (first concrete commit). Verify invoice + payment schedule (3 quarters) + deliverables scope.
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

- [x] **2026-04-21** — Megan Miller first Moil 360 customer to complete a live CRM onboarding session (89 min). First 5000-contact import pipeline unblocked. Sequences confirmed as killer feature.
- [x] **2026-04-21** — Taiwo committed to Connectex Apr 22 start (first concrete commit after 3 weeks of slipping).
- [x] **2026-04-20** — Abiodun delivered Moil + Inna content by Sun Apr 19 deadline (manifest in Moil Marketing 8:55 AM).
- [x] **2026-04-18** — FitLogic Apr 18 deadline passed; Daniel Guadiano Apr 16 meeting held.

# MEMORY — Open Actions & Live Commitments

**Last updated:** 2026-04-24 (Run 20 — weekly compile: priority rot rules applied, no items hit demotion threshold this week)
**Purpose:** Single source of truth for open action items extracted from ingested raw sources.

> Relationship/concept context: [[index]] · Ingestion history: [[log]]

**Review rhythm:** Weekly (Fri, 15 min) — strike `~~done~~`; move stale >2wk to log.md. Monthly — prune precedent value. **Hard cap: 200 lines.**

> **Run 20 priority rot pass (2026-04-24):** Applied weekly compile rules — no items met the >14-day Immediate / Next-2-3-weeks demotion threshold this run (oldest dated item in Immediate is Apr 17–18 carryover, 7 days old; oldest in Next 2–3 weeks is Apr 22–23 Daniel Guadiano slot, 1–2 days past). No `Verify: …` items present. Closed/Archive section already empty (pruned 2026-04-22). Next likely demotion candidates next week: "Carried from last week (Apr 11–17)" block items dated Apr 11–14 will cross 14 days between Apr 25–28.

---

## 🔥 Immediate — This Week (Apr 23–29, 2026)

### 🔥 Apr 23 → Apr 29 — FitLogic CRM handoff sprint
Source: [[wiki/meetings/2026-04-23-megan-crm-google-setup]], [[wiki/orgs/fitlogic]]
- [ ] **🔥 Taiwo Apr 23 night:** Test CRM build after pushing to Megan's new GitHub repo; flag blockers to Andres
- [ ] **🔥 Taiwo Apr 24 morning:** Continue migration / deploy to `fitlogicfunctionalmedicine.com/crm`
- [ ] **Andres Apr 24:** Send Megan status update (what's done, what's left, testing plan)
- [ ] **🔥 Andres Fri Apr 24 12:30 PM CT:** Attend Megan × Electric Bricks website agency meeting — non-negotiable: nothing on the site can confuse a patient about Megan's NP scope (doctor vs. health coach issue)
- [ ] **Andres + Taiwo Apr 25–26:** Verify weekend testing so Megan can start sending real emails Mon Apr 28
- [ ] **🔥 Go-live Mon Apr 28:** Megan starts sending real emails from FitLogic CRM
- [ ] **🔥 Wed Apr 29, 9:30 AM CT:** Full handover meeting (Andres + Taiwo + Megan) — formal walkthrough
- [ ] **Andres direct text to [[wiki/people/daniel-mann|Daniel D. Mann]]:** acknowledge Michelle-via-Megan hello; open the "project together" thread he's mentioned before
- [ ] **Megan (ongoing):** Forward every meeting invite to Andres (her commitment Apr 23 — behavioral change, not one-off)
- [ ] **Megan (before Apr 29):** Log into Moil 360, upload logo + brand colors, play with image editing — **do not build content calendar yet** until brand assets are in

### 🚨 Apr 21 firefight — Moil 360 launch + Megan FitLogic CRM onboarding
Source: [[wiki/meetings/2026-04-21-teams-daily-ops]], [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]]
- [ ] **🔥 Andres tonight (Apr 21):** Deploy Moil CRM at `fitlogicfunctionalmedicine.com/CRM` via Megan's GoDaddy; wire `Megan@fitlogicfunctionalmedicine.com` as sender; wipe test contacts; import 5,000-contact Keap CSV
- [ ] **🔥 Andres:** Surface per-campaign click-rate / open-rate dashboard for FitLogic (Megan asked)
- [ ] **🔥 Adeleke:** Ship Gemini→Grok→Qwen multi-model fallback for video gen; root-cause image-creation latency + intermittent template fails
- [ ] **🔥 Jacob + Andres:** Fix `partners@moilapp.com` deliverability — hit Megan, Roxana, Jill PureSerenity; engineering said "can't optimize it more"; need per-customer sender or infra fix, **P0**
- [ ] **🔥 Product:** Fix business-plan switching UX bug — class-wide, hit Megan FitLogic Apr 21 (2nd time); escalate out of manual DB intervention
- [ ] **Taiwo Apr 22:** Start Connectex (needs CRM URL from Andres); finish FitLogic in parallel; restore day/light mode on coach; surface campaign link-editing
- [ ] **Jacob:** Resend Moil 360 license links to Megan FitLogic, Siren Beauty, Roxana, Jill PureSerenity (paid $75 Apr 20, never got link)
- [ ] **Andres + Jacob:** Email every Buda cohort licensee with Moil 360 feature updates (Andres prompted 12:21 PM Apr 21)
- [ ] **🔒 Security:** Move `cs@moilapp.com` password off Teams — Jacob posted `Pr0ud**2023$` in open Moil Team thread Apr 21 11:31 AM
- [ ] **Megan:** Forward Andres' Electric Bricks feedback (alt-text, H1, slugs) as required-changes checklist; mark real clients in Keap; pull remaining EHR contacts; send quiz questions for native Moil rebuild
- [ ] **Joint Megan+Andres:** Decide push/postpone on co-planned workshop
- [ ] **Andres:** Respond to Jacob's PRD proposal (carried from Apr 19)
- [ ] **Adeleke:** Review Claude Code session `session_0156Da69uG1W8jSEof5V2xgb` (carried)
- [ ] **Jacob:** Get Inna's decision on IG/LinkedIn tagging approach — direct access vs send-and-post (carried)
- [ ] **Andres:** Respond to Jacob on `Posting Consistently.mp4` thoughts (carried)

### Delivery-pace carryover — Teams Apr 17–18
- [ ] **Jacob:** Fix Business Coach "not responding" bug — "stagebeta broken?" surfaced again Apr 21 6:26 PM
- [ ] **Jacob:** Follow-up emails to Moil 360 licensees who have NOT activated
- [ ] **Taiwo / Andres:** Reschedule delivery calls to reasonable hours in Taiwo's time zone (not 11pm / 2am)
- [ ] **Abiodun + Andres:** Make content rhythm explicit (Tue push / Sun review) — Abiodun delivered Apr 19 + 21, rhythm still verbal
- [ ] **Andres:** Fix architectural regression — current app no longer uses business plan as single source of truth

---

## 🔥 Carried from last week (Apr 11–17)

- [ ] **🔥 EDC AI-tools-for-website call** — John Costilla + [[wiki/people/joseph-arnke|Joe Arnke]] (GIS WebTech) re: Moil AI → EDC site-selector. See [[wiki/orgs/buda-edc]]
- [ ] **Apr 20 → Jun 8** — Buda HIVE Cohort 4 begins (every Monday). Prep materials. Casey Earley participant
- [ ] **🔥 Adeleke:** Audit entire Moil codebase for OpenAI API usage; migrate gpt-4o → gpt-5-mini (token refill went monthly → 3x/week). Rotate keys after audit
- [ ] **May 7** — Renee Simmons / Hays CISD Career Day at CHES, ~20 min to 4th/5th graders. Prep kid-friendly entrepreneurship talk. See [[wiki/people/renee-simmons]]
- [ ] **Respond to Adam Maxon** (adamm@pfdevelopment.com) re Pflugerville Mentor Day. See [[wiki/people/adam-maxon]]
- [ ] **Adeleke + Jacob:** Rotate GitHub webhook secrets per Apr 14 security alert
- [ ] **Reply to Jesutomilola Omoniyi** (Google xWF) — two Apr 15 follow-ups trying to reschedule; pick a time next week/month
- [ ] **Review 2025 1040** in TaxDome — Melissa Jarbo back from leave; new secure message from Martin Kutac; Ingrid refund/liability form flagged
- [ ] **Buda HIVE Cohort 4 prep** — review Joshua Edmond's Apr 17 Week 1–2 print-outs (BMC added Week 2); confirm with Casey before Apr 20 open; confirm OneDrive edit access
- [ ] **Identify new social media client** Andres signed; confirm Abiodun capacity
- [ ] **Product UX:** Fix employer cannot see applicant phone/email in Moil; clarify notification system when candidate messages via Moil; reply to Megan Miller with workaround + ETA

---

## 📅 Next 2–3 weeks (Apr 18 – May 2)

- [x] ~~**Apr 22 @ 10am CT** — Call with **Kate Silvas (Helotes EDC)**~~ — **DONE Apr 22**; Moil Partnership Proposal sent same day 5:26 PM. Now: **await Board response; nudge ~Apr 29–May 6 if silent.** See [[wiki/orgs/helotes-edc]], [[wiki/people/katherine-silvas]]
- [ ] **Apr 22 (after 1pm) OR Apr 23 (after 10am)** — **Daniel Guadiano / Astra Restaurant** meeting. Andres already proposed both slots Apr 21; awaiting Daniel's pick. Prep restaurant-ops scheduling demo. First hospitality ICP proof point if it closes. [[wiki/people/daniel-guadiano]]
- [ ] **Apr 24 ~3:30 PM CT** — Phone call with **Elisa Alaniz** (Irma Mason referral). Discovery, not pitch — figure out whether she's a candidate, hiring business, or partner. [[wiki/people/elisa-alaniz]]
- [ ] **Reply to [[wiki/people/irma-mason|Irma Mason]]** re: Mrs. Unger job-search referral (Kyle/Buda/San Marcos) — still open from Apr 19
- [ ] **🔥 Reply to [[wiki/people/rashaka-boykins|Rashaka Boykins]]** — consolidate answer to both Apr 21 (LLM marketing / adaptive) + Apr 22 (traffic + LinkedIn/Instagram integration) inbound. Two questions in 27 hours after 6 weeks of silence = strong signal
- [ ] **Decide on Megan Miller's payment plan ask** — switch from $500/mo × 3 to $250/mo × 6 (same total, stretched). Reply outstanding since Apr 19. [[wiki/people/megan-miller]]
- [ ] **Re-queue Caroline Mungenast (Birmingham Business Alliance)** — OOO at Hannover Messe until Apr 24; don't mark dead, re-queue after Apr 24
- [ ] **Apr 24 · 7–9pm** — Travis Sutherland / Sun Show demo booth. Screen + flyers. Confirm logistics
- [ ] **Apr 27 — Buda HIVE Lunch & Learn: Business Credit** (Jacquie Martinez event). Attend/support
- [ ] **Shannon Cameron (Buda EDC Director of Ops)** — open PSA assets she forwarded Apr 21; reply + loop her into broader Moil-EDC context. [[wiki/people/shannon-cameron]]
- [ ] **Jacob Centeno referral partnership** — set up lightweight workflow, decide commission/credit model. See [[wiki/people/jacob-centeno]]
- [ ] **Ana Vetencourt (URBANZUELA)** — review Google Doc draft she sent; provide feedback

---

## 🔧 Technical debt — still open from Teams Apr 5–12

See [[log.md]] Run 15 for full context. Still live:
- [ ] **Roxana / AlloyATX** — verify 21 questions + assets + GoDaddy domains completed by Apr 18 deadline; next session: GSC setup, satellite domains, wellness referrals. [[wiki/meetings/2026-04-14-roxana-alloy-atx-onboarding]]
- [ ] **Eden** — follow up on website discovery call (recorded Apr 8)
- [ ] **Tour guide bugs** — 2 missing `data-guide-id` attrs, generic text, auto-scroll
- [ ] **Segment analytics** — `No segment writeKey` error on staging
- [ ] **Image context bug** — images "forget" conversation context
- [ ] **Supabase** — `business-intake` edge function deploy needed
- [ ] **Meridian** — domain verification + Stripe full flow test
- [ ] **Phone sign-up** — removed (Azure broken); permanent fix or formal removal
- [ ] **Daily video production** — Andres wants daily rhythm using AI tools; define workflow
- [ ] **Sun show raffle** — "Free year of Moil 360" — was email sent to attendees?
- [ ] **Adeleke FB account** — login code issue since Apr 7; blocks app review video
- [ ] **Credentials migration** — Stripe, Supabase, API keys out of Teams → 1Password/Bitwarden

---

## 💤 Deferred — hard dates

- [ ] **Jul 1, 2026** — Shay Foley / Johns Creek Chamber re-engage (chamber budget year starts). Pitch AI tools for entrepreneurs w/ Buda EDC reference. [[wiki/people/shay-foley]]
- [ ] **Sep 1, 2026** — Buda HIVE training program curriculum jointly with HIVE + Incubator Strategist Team
- [ ] **Post-Apr 15** — CampaignOS with Jennifer Storm: circle back on MVP scope; Andres offered "little to no cost" — decide commitment level. [[wiki/concepts/campaignos]]

---

## 🏗️ Strategic — no hard deadline

- [ ] **Fantelo clarification** — pivot, separate venture, or sub-brand? Consumes engineering time w/ no documented strategy. [[wiki/concepts/fantelo]]
- [ ] **GitHub org cleanup** — archive 6+ stale repos; dedupe BlueprintsForSuccess; consider `Moil-Clients` org
- [ ] **Moil license case study** — public "City EDC × Moil" for decks + expansion (Queen Creek, Johns Creek, Greater Buda Chamber)
- [ ] **Claude Code security audit** — what permissions does it have on this Mac Mini (SSH, AWS, `.env`)? Decide boundaries before autonomous skills

<!-- Closed/Archive moved to log.md (see 2026-04-22 pruning block) -->

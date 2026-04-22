# MEMORY — Open Actions & Live Commitments

**Last updated:** 2026-04-22 (pruned to buffer; Apr 21 firefight active)
**Purpose:** Single source of truth for open action items extracted from ingested raw sources.

> Relationship/concept context: [[index]] · Ingestion history: [[log]]

**Review rhythm:** Weekly (Fri, 15 min) — strike `~~done~~`; move stale >2wk to log.md. Monthly — prune precedent value. **Hard cap: 200 lines.**

---

## 🔥 Immediate — This Week (Apr 18–24, 2026)

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

- [ ] **Apr 22 @ 10am CT** — Call with **Kate Silvas (Helotes EDC)**. Lead with Buda EDC case study + per-cohort license model. Build Buda EDC one-pager (pricing, delivery, Cohort 4 proof) before call; send Buda-mirror proposal after. See [[wiki/orgs/helotes-edc]], [[wiki/people/katherine-silvas]]
- [ ] **Jacob Centeno referral partnership** — set up lightweight workflow, decide commission/credit model. See [[wiki/people/jacob-centeno]]
- [ ] **Apr 24 · 7–9pm** — Travis Sutherland / Sun Show demo booth. Screen + flyers. Confirm logistics
- [ ] **Daniel Guadiano (Astra Restaurant)** — if it closes, write first hospitality ICP case study
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

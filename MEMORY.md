# MEMORY — Open Actions & Live Commitments

**Last updated:** 2026-04-28 (Run 26 — Apr 27 email digest + Apr 28 Mark Polanco walkthrough + internal engineering review ingested)
**Purpose:** Single source of truth for open action items extracted from ingested raw sources.

> Relationship/concept context: [[index]] · Ingestion history: [[log]]

**Review rhythm:** Weekly (Fri, 15 min) — strike `~~done~~`; move stale >2wk to log.md. Monthly — prune precedent value. **Hard cap: 200 lines.**

---

## 🔥 Immediate — This Week (Apr 27 – May 3, 2026)

### 🔥 Apr 28 — Connectex go-live sprint + repo discipline hard rule
Source: [[wiki/meetings/2026-04-28-mark-polanco-connectex-walkthrough]], [[wiki/meetings/2026-04-28-website-update-review-internal]]
- [ ] **🔥 Andres:** Issue full Connectex invoice up front so [[wiki/people/mark-polanco|Mark]] can claim Buda EDC reimbursement (1 down + 3 quarterly over 9 months)
- [ ] **🔥 Andres:** Update Connectex site phone to **330-812-5750**
- [ ] **🔥 Andres:** Push Connectex site to Mark's Squarespace **once login arrives** — go-live target early next week
- [ ] **🔥 Andres:** Build Connectex Resources/blog section live by next week (Mark's SEO play — blogs after each training)
- [ ] **🔥 Andres:** Schedule mid-May lunch with Mark Polanco
- [ ] **🔥 Mark:** Send Squarespace login; refile Buda EDC reimbursement application ASAP; send 4–5 troubleshooting docs (Verizon T77 LTE, Yealink LTE deck station EOM); contact BuiltFirst about marketplace billing block *after* EDC application
- [ ] **🔥 Taiwo:** Push Connectex repo to remote ASAP (Andres had zero visibility going into the Apr 28 walkthrough — *new hard rule: all engineering work pushed for visibility, branches OK, no working-locally-only*)
- [ ] **🔥 Taiwo:** Add Gemini API key to ConnectX campaign builder so the Verizon T77 LTE test campaign can run
- [ ] **🔥 Engineering:** Import Airtable contacts (left columns up to but not including reporting/documents); finish ConnectX Contacts tab to match Airtable schema; seed Knowledge Base with troubleshooting docs for AI tier-1 ticket testing next week

### 🔥 Apr 28 — FitLogic deploy tonight + Inna demo slip
Source: [[wiki/meetings/2026-04-28-website-update-review-internal]]
- [ ] **🔥 Taiwo Apr 28 night:** Deploy FitLogic on Vercel — set env vars, test contacts upload + Google account connection. Replicate readable WYSIWYG editor + variable selector from Inna onto FitLogic
- [ ] **🔥 Taiwo:** Put deploy/test sessions on Andres's calendar — calendar etiquette hard rule (no more 10 PM / 2 AM ad-hoc asks)
- [ ] **🔥 Wed Apr 29 9:30 AM CT:** FitLogic full handover meeting (Andres + Taiwo + [[wiki/people/megan-miller|Megan]]) — formal walkthrough
- [ ] **Inna demo slipped 1 week** (Inna unavailable Apr 28). Use the time to fix:
  - [ ] **🔥 Taiwo:** Fix Inna CRM contact-add hang (Jacob hit it live Apr 28)
  - [ ] **🔥 Taiwo:** Fix Gemini API key on Inna (grab the same key used on FitLogic)
  - [ ] **🔥 Taiwo:** Add Jacob as Google OAuth test user on Inna so he can connect Gmail/Calendar end-to-end
- [ ] **Inna review pending:** podcast videos sent Apr 27 → Inna reviews → publish on LinkedIn + IG (3-step approval-loop workflow). [[wiki/people/inna-benyukhis|Inna]] in-person meeting confirmed Apr 28 4 PM CT
- [ ] **🔥 Andres:** Add [[wiki/orgs/siren-beauty|Siren Beauty]] brand kit to repo as `brand.md` — first per-customer brand-kit-as-repo-artifact (extends user.md / design.md / agent.md pattern toward the YC RFS *"build for agents"* framing)

### 🔥 Apr 28 — moilapp.com SEO emergency
Source: [[wiki/meetings/2026-04-28-website-update-review-internal]]
- [ ] **🔥 Andres:** SEO audit + fixes on **moilapp.com** — only ~12 of ~60 pages indexed; schemas wrong; robots.txt wrong; *"two years of accumulated SEO debt — we're literally unfindable"*. Workstream rule: same SEO discipline applies to all client builds going forward

### 🔥 Apr 27 inbox — Open replies
Source: [[raw/email-digest-2026-04-27]]
- [ ] **🔥 Andres:** Reply to [[wiki/people/john-costilla|John Costilla]] / Buda EDC — *"FW: Follow Up — Let's discuss?"* (Apr 27 08:17, flagged priority #1 in morning briefing, no Apr 27 reply captured)
- [ ] **Andres:** Reply to [[wiki/people/victor-escamilla|Victor Escamilla]] / City of Buda — **revised** UDC Update focus group invite Apr 27 17:08 (originals from Apr 24 16:13 superseded)

### 🔥 Apr 24 inbox — Contract reviews + Press + Customer directives (carryover)
Source: [[raw/email-digest-2026-04-24]]
- [ ] **🔥 Andres:** Review [[wiki/people/joshua-edmond|Joshua Edmond's]] redlined HIVE Strategist PSAs contract (sent Apr 24 13:08 to Shannon Cameron) — be on Joshua's invite, align on edits before Shannon countersigns
- [ ] **🔥 Andres:** Reply to Jessica @ VoyageAustin Magazine (interview request Apr 24 12:42) — accept; ask for question list. See [[wiki/people/jessica-voyage-austin]]
- [x] ~~**Jacob + Ablad:** Slice 2 March podcast videos for Inna~~ — **DELIVERED Apr 27** (Jacob sent videos + thumbnails; portrait format chosen for IG Reels). Awaiting Inna review → publish on LinkedIn + IG
- [ ] **Andres:** Wait on [[wiki/people/rashaka-boykins|Rashaka's]] question batch (her site went live Apr 24); reply with answers + close on $600/yr vs $900/mo
- [ ] **Apollo data hygiene:** Outbound Apr 24 09:03 greeted "Joseph" but address was `wilkinsonroger860@gmail.com` (Roger Wilkinson). Likely Apollo merge bug — audit sequence first-name mapping before next batch

### 🔥 Carried — Apr 24 marketing + onboarding + license-distribution
Source: [[wiki/meetings/2026-04-24-teams-daily-ops]]
- [ ] **🔥 Andres + Ablad:** Reach a working agreement on AI-tool adoption pace (Apr 24 argument unresolved). Decision needed before next content cycle
- [ ] **🔥 Andres:** Build reproducible demo-video workflow (Clio template applied to all Moil features). First artifact live: `clioremembers.com/demo`
- [ ] **🔥 Andres:** Redesign in-app onboarding guide for discoverability — client feedback ("they logged in and didn't know what to do next?")
- [ ] **🔥 Adeleke:** Push auto-assign-Moil-360-license feature from staging to prod
- [ ] **Jacob:** Rework outbound messaging to be conversion-driven (Andres Apr 24 coaching focus on strategy-before-execution)
- [ ] **HeyGen subscription decision:** keep + maximize credits, drop, or replace with ChatGPT image2 + Capcut workflow
- [x] ~~Jacob: Re-auth HeyGen login for Abiodun~~ — RESOLVED Apr 26 (Andres sent link directly; Abiodun confirmed *"I am in"*)

### 🔥 FitLogic CRM sprint — Apr 28 deploy + Apr 29 handover
Source: [[wiki/meetings/2026-04-23-megan-crm-google-setup]], [[wiki/meetings/2026-04-28-website-update-review-internal]], [[wiki/orgs/fitlogic]]
- [ ] **🔥 Taiwo Apr 28 night:** Deploy FitLogic on Vercel (env vars, contacts upload, Google account connection); replicate readable WYSIWYG editor + variable selector from Inna
- [ ] **🔥 Andres Apr 29 9:30 AM CT:** Full handover meeting (Andres + Taiwo + Megan) — formal walkthrough
- [ ] **🔥 Megan starts sending real emails** — slipping from Apr 28 → Apr 29 per the Apr 28 internal call (Taiwo: *"feed logic is not set to go tomorrow"*)
- [ ] **Andres direct text to [[wiki/people/daniel-mann|Daniel D. Mann]]:** acknowledge Michelle-via-Megan hello; open the "project together" thread
- [ ] **Megan (before Apr 29):** Log into Moil 360, upload logo + brand colors, play with image editing — **do not build content calendar yet**
- [ ] **Megan (ongoing):** Forward every meeting invite to Andres (Apr 23 commitment)
- [ ] **Decide on Megan's payment plan ask** — switch from $500/mo × 3 to $250/mo × 6 (same total, stretched). Reply outstanding since Apr 19

### 🔥 Carried product/eng debts (Apr 21 firefight residue)
Source: [[wiki/meetings/2026-04-21-teams-daily-ops]], [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]]
- [ ] **🔥 Andres:** Surface per-campaign click-rate / open-rate dashboard (Megan asked)
- [ ] **🔥 Adeleke:** Ship Gemini→Grok→Qwen multi-model fallback for video gen; root-cause image-creation latency + intermittent template fails
- [ ] **🔥 Jacob + Andres:** Fix `partners@moilapp.com` deliverability — Megan/Roxana/Jill all hit it; need per-customer sender or infra fix, **P0**
- [ ] **🔥 Product:** Fix business-plan switching UX bug — class-wide
- [ ] **Jacob:** Resend Moil 360 license links to Megan, Siren, Roxana, Jill (paid Apr 20, never got link)
- [ ] **Andres + Jacob:** Email every Buda cohort licensee with Moil 360 feature updates
- [ ] **🔒 Security:** Move `cs@moilapp.com` password off Teams (Jacob leaked Apr 21)
- [ ] **Andres:** Respond to Jacob's PRD proposal (carried from Apr 19)
- [ ] **Jacob:** Fix Business Coach "not responding" bug — `stagebeta broken?` surfaced again Apr 21
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

## 📅 Next 2–3 weeks (Apr 28 – May 12)

- [ ] **Apr 28 11 AM CT (= 9 AM AZ)** — [[wiki/people/kim-dowers|Kim Dowers]] / Queen Creek Chamber **workshop went live** today. Recap + define follow-up cadence post-workshop
- [ ] **Apr 28 4 PM CT** — In-person meeting with [[wiki/people/inna-benyukhis|Inna]] (per Apr 27 morning briefing)
- [ ] **🔥 Helotes EDC** — Moil Partnership Proposal out since Apr 22. **Nudge by ~Apr 29–May 6 if silent.** See [[wiki/orgs/helotes-edc]], [[wiki/people/katherine-silvas]]
- [ ] **[[wiki/people/daniel-guadiano|Daniel Guadiano]] / Astra Restaurant** — both Apr 22/23 slots proposed went without confirmation; re-propose new slot or close. First hospitality ICP if it closes
- [ ] **Reply to [[wiki/people/irma-mason|Irma Mason]]** re: Mrs. Unger job-search referral — still open from Apr 19
- [ ] **🔥 Reply to [[wiki/people/rashaka-boykins|Rashaka Boykins]]** — consolidate answer to Apr 21–22 inbound (LLM marketing + traffic/LinkedIn-IG); close on $600/yr vs $900/mo offered Apr 24
- [ ] **Re-queue Caroline Mungenast (Birmingham Business Alliance)** — was OOO until Apr 24; she should be back. Re-engage
- [ ] **Shannon Cameron (Buda EDC)** — open PSA assets she forwarded Apr 21; reply + loop her into broader Moil-EDC context
- [ ] **Jacob Centeno referral partnership** — set up lightweight workflow, decide commission/credit model
- [ ] **Ana Vetencourt (URBANZUELA)** — review Google Doc draft she sent; provide feedback
- [ ] **Elisa Alaniz follow-up** — Apr 24 phone call slot; outcome not captured — confirm next step or close

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

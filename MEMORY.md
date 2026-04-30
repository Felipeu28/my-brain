# MEMORY — Open Actions & Live Commitments

**Last updated:** 2026-04-29 (Run 27 — Apr 28 email digest + Apr 29 Megan CRM delivery walkthrough ingested)
**Purpose:** Single source of truth for open action items extracted from ingested raw sources.

> Relationship/concept context: [[index]] · Ingestion history: [[log]]

**Review rhythm:** Weekly (Fri, 15 min) — strike `~~done~~`; move stale >2wk to log.md. Monthly — prune precedent value. **Hard cap: 200 lines.**

---

## 🔥 Immediate — This Week (Apr 27 – May 3, 2026)

### 🔥 Apr 29 — FitLogic delivered; P0 bug list from live walkthrough
Source: [[wiki/meetings/2026-04-29-megan-fitlogic-crm-delivery]]
- [x] ~~**Apr 29 9:30 AM CT FitLogic full handover meeting**~~ — DELIVERED. Megan + [[wiki/people/michelle-fitlogic|Michelle]] (practice manager) + Andres; 88 min; first end-to-end Moil 360 delivery (CRM + Campaigns + Content360)
- [ ] **🔥 Andres / Engineering:** Extract patients vs. non-patients from FitLogic's 5,000-contact export (Megan already shared the patient list on a prior call — Andres has the download)
- [ ] **🔥 Engineering — P0 bug:** pipeline-stage updates in pipeline view don't propagate back to contact card / analytics roll-up
- [ ] **🔥 Engineering — P0 bug:** Content360 calendar defaulted to **Feb 28** instead of current month when Megan opened it
- [ ] **🔥 Engineering — P0 bug:** "Edit image" appears stuck on the original image (image-to-image vs. text-to-image regression). Megan tried "happy gut" + "image of a person who is happy and feels relief" — neither produced a new image
- [ ] **🔥 Engineering:** Verify Brand DNA colors propagate into Content360 image generator (Megan suspects they don't because she set up the calendar before saving colors)
- [ ] **Engineering — features:** "Last contacted" filter on contacts; `previous client` lead-source / pipeline-status option; customizable lead-source drop-down (social media, website, driving by, friend/family referral, networking event, **other** with free-text); centralized link library (paste once, reuse across emails); closed-captioning on generated videos (Michelle accessibility ask)
- [ ] **Andres:** Send Megan today: platform access details, "what you need" list, confirmation Michelle can be added as staff via Settings → Add Staff
- [ ] **Andres:** Build chat/FAQ widget tied to FitLogic site (after Electric Bricks delivers); book-a-call link → Megan's **Square calendar**
- [ ] **Megan:** Bring brand color hex/RGB from home notebook; export active-patient list from Charm; manually tag IC-only patients; identify the day Jill's contacts were imported into Charm and bulk-tag those rows
- [ ] **Brand-voice rule for FitLogic AI email generation:** hook-style openers (*"You may be wondering…"* / *"Are you still struggling with…"*); never *"I wanted to share…"*; reader-centered, not founder-centered. Capture as Brand DNA field

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

### 🔥 Apr 28 — Inna demo slip residue (FitLogic deploy resolved Apr 29)
Source: [[wiki/meetings/2026-04-28-website-update-review-internal]], [[wiki/meetings/2026-04-29-megan-fitlogic-crm-delivery]]
- [x] ~~**Taiwo Apr 28 night:** Deploy FitLogic on Vercel~~ — DELIVERED (verified live in the Apr 29 walkthrough)
- [x] ~~**Taiwo:** Put deploy/test sessions on Andres's calendar~~ — calendar etiquette hard rule remains
- [ ] **Taiwo professionalism note (Apr 29):** Hot mic during Megan client call — internal devs stay muted on customer-facing calls
- [ ] **Inna demo slipped 1 week** (Inna unavailable Apr 28). Use the time to fix:
  - [ ] **🔥 Taiwo:** Fix Inna CRM contact-add hang (Jacob hit it live Apr 28)
  - [ ] **🔥 Taiwo:** Fix Gemini API key on Inna (grab the same key used on FitLogic)
  - [ ] **🔥 Taiwo:** Add Jacob as Google OAuth test user on Inna so he can connect Gmail/Calendar end-to-end
- [ ] **Inna review pending:** podcast videos sent Apr 27 → Inna reviews → publish on LinkedIn + IG (3-step approval-loop workflow). [[wiki/people/inna-benyukhis|Inna]] in-person meeting confirmed Apr 28 4 PM CT
- [ ] **🔥 Andres:** Add [[wiki/orgs/siren-beauty|Siren Beauty]] brand kit to repo as `brand.md` — first per-customer brand-kit-as-repo-artifact (extends user.md / design.md / agent.md pattern toward the YC RFS *"build for agents"* framing)

### 🔥 Apr 28 — moilapp.com SEO emergency
Source: [[wiki/meetings/2026-04-28-website-update-review-internal]]
- [ ] **🔥 Andres:** SEO audit + fixes on **moilapp.com** — only ~12 of ~60 pages indexed; schemas wrong; robots.txt wrong; *"two years of accumulated SEO debt — we're literally unfindable"*. Workstream rule: same SEO discipline applies to all client builds going forward

### 🔥 Apr 28 inbox — Open replies
Source: [[raw/email-digest-2026-04-28]]
- [x] ~~**Andres:** Reply to [[wiki/people/john-costilla|John Costilla]] / Buda EDC — *"FW: Follow Up — Let's discuss?"*~~ — RESOLVED Apr 28 (the cryptic Apr 27 forward was lunch logistics; John replied 08:23 — Thursday they're out, Brian booked Friday)
- [ ] **🔥 Andres:** Reply to [[wiki/people/john-costilla|John Costilla]] — pick alternate lunch day next week (Mon/Tue/Wed open since Thu/Fri taken)
- [ ] **Andres:** Reply to [[wiki/people/victor-escamilla|Victor Escamilla]] / City of Buda — revised UDC Update focus group invite Apr 27 17:08 (still open from Apr 27)
- [ ] **Andres:** Reply to [[wiki/people/kim-dowers|Kim Dowers]] / Queen Creek — post-webinar follow-up Apr 28 17:36 looped Andres + Jacob to assist **Krystal** (post-webinar onboarding lead). First post-Apr-28-webinar conversion candidate
- [x] ~~**Christine StJohn × Andres May 4 12pm CDT lunch confirmed**~~ — Kathryn Eyers (Unwrapped Uncorked Events) Apr 28 11:46 acceptance; Christine StJohn booking originated via Buda HIVE earlier same day

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

### 🔥 FitLogic — post-delivery threads (still open)
- [ ] **Andres direct text to [[wiki/people/daniel-mann|Daniel D. Mann]]:** acknowledge Michelle-via-Megan hello; open the "project together" thread
- [ ] **Megan (ongoing):** Forward every meeting invite to Andres (Apr 23 commitment, still unverified)
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
- [ ] **Respond to Adam Maxon** (adamm@pfdevelopment.com) re Pflugerville Mentor Day. See [[wiki/people/adam-maxon]]
- [ ] **Adeleke + Jacob:** Rotate GitHub webhook secrets per Apr 14 security alert
- [ ] **Reply to Jesutomilola Omoniyi** (Google xWF) — two Apr 15 follow-ups trying to reschedule; pick a time next week/month
- [ ] **Review 2025 1040** in TaxDome — Melissa Jarbo back from leave; new secure message from Martin Kutac; Ingrid refund/liability form flagged
- [ ] **Buda HIVE Cohort 4 prep** — review Joshua Edmond's Apr 17 Week 1–2 print-outs (BMC added Week 2); confirm with Casey before Apr 20 open; confirm OneDrive edit access
- [ ] **Identify new social media client** Andres signed; confirm Abiodun capacity
- [ ] **Product UX:** Fix employer cannot see applicant phone/email in Moil; clarify notification system when candidate messages via Moil; reply to Megan Miller with workaround + ETA

---

## 📅 Next 2–3 weeks (Apr 29 – May 12)

- [x] ~~Apr 28 11 AM CT (= 9 AM AZ) — Queen Creek Chamber workshop~~ — went live; **post-webinar Krystal onboarding now open** (Kim Dowers Apr 28 17:36)
- [x] ~~Apr 28 4 PM CT — In-person meeting with Inna~~ (assumed completed; re-verify in next email digest)
- [ ] **May 4 12pm CDT** — Christine StJohn × Andres lunch at Unwrapped Uncorked (Kathryn Eyers — confirmed Apr 28)
- [ ] **May 7** — Renee Simmons / Hays CISD Career Day at CHES (~20 min to 4th/5th graders, kid-friendly entrepreneurship talk)
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

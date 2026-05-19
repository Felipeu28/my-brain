# MEMORY — Open Actions & Live Commitments

**Last updated:** 2026-05-19 (Run 58 — `raw/email-digest-2026-05-18` ingested. **Three customer staging environments delivered same-day by Jacob in 16 minutes** (ConnectEx CRM to Mark, Meridian Buda to Travis, FitLogic CRM to Megan) — directly implements the May 18 Monday Collaboration directive. **Mark confirmed Thursday May 21 handover.** Moil FB business ID thread stalled — Andres still can't see both accounts, Jacob never got the invite either, Shanonn OOO until Tue May 19. ALLOY ATX OneDrive folder shared with Jacob. John Costilla forwards on Mac Decision Brief; Astra Ribbon Cutting canceled. Taiwo proactively testing FitLogic inbound email deliverability.) · Run 57 (2026-05-18) — `raw/teams-transcript-monday-collaboration-2026-05-18` ingested.
**Run 50 (2026-05-14 PM):** 1 new Teams transcript — **Megan × Andres × Taiwo — GoDaddy delegate + Outlook migration session**. New meeting: [[wiki/meetings/2026-05-14-megan-taiwo-fitlogic-2fa-godaddy-session]]. Closed May 11 2FA wiring blocker + May 7 next-week in-person commitment (now Wed May 20 10 AM CT at FitLogic). First on-record articulation of the Moil-touches-customer-accounts security pattern. Two-domain architecture written down as standing pattern.
**Runs 47–49 (2026-05-13 → 14):** Perseus YC meeting May 12 + Jason Cornelius YC rec submitted May 13 + Jordan Kaiser Cohort-4 1:1 ingested. Moil ships silent 3-emails/week proactive coaching feature; HIVE 1-yr license precedent surfaces twice in 24h; Monica × Jordan intro confirmed; Buda EDC Incubator Strategist on same-week finalization track.
**Purpose:** Single source of truth for open action items extracted from ingested raw sources.

> Relationship/concept context: [[index]] · Ingestion history: [[log]]

**Review rhythm:** Weekly (Fri, 15 min) — strike `~~done~~`; move stale >2wk to log.md. Monthly — prune precedent value. **Hard cap: 200 lines.**

---

## 🔥 Immediate — This Week (May 18 – May 24, 2026)

### 🔥 May 18 — Three customer staging deliveries shipped + FB business ID stalled
Source: [[raw/email-digest-2026-05-18]]
- [ ] **🔥 Tue May 19 — Andres:** Demo call with [[wiki/people/mark-polanco|Mark Polanco]] (proposed morning/afternoon May 18 22:16 UTC). Confirm time + bring contact-loading plan. **Thursday May 21 handover already on calendar** — demo Tuesday is the dress rehearsal
- [ ] **🔥 Thu May 21 — Andres + Mark:** ConnectEx CRM handover (confirmed by Mark May 18 20:05 UTC). Site staging at `https://www.connectex.net/crm/login`; not-all-contacts-loaded caveat communicated — load after Mark's testing pass
- [ ] **🔥 Mon-Tue May 18-19 — Megan + Michelle:** Test the FitLogic CRM staging at `https://fitlogicrm.vercel.app/` (Jacob delivered May 18 18:47 UTC); surface bugs before Wed May 20 10 AM in-person walkthrough at FitLogic. Staging delivery does **not** violate the standing "hold prod push" directive
- [ ] **🔥 May 18 onward — [[wiki/people/travis-sutherland|Travis]]:** Test Meridian Buda staging at `https://meridian-buda.vercel.app/` (Jacob delivered May 18 18:36 UTC); **partner-side triggers prod push**. Still gated on Taiwo re-running the verification-code request that landed in empty Travis@zoho.com
- [ ] **🔥 Tue May 19 — Andres:** **Moil FB business ID thread** — escalate at first email-check Tuesday morning when [[wiki/orgs/alloy-atx#shanonn-thompson|Shanonn Thompson]] returns from OOO. Multi-party blocker: Andres still can't see both accounts, Jacob never received any invite either, Shanonn was OOO May 14–18. **First time a Moil onboarding has been gated by customer-staff OOO** — pattern signal for HIVE Cohort/customer-onboarding cadence
- [ ] **🔥 Tue May 19 — Andres:** Reply to John's May 15 *"align on consulting piece"* call ask on Mac Decision Brief — **John forwarded the brief twice May 18 (19:16 + 19:45 UTC)**, pressure rising; bring one-pager SoW (hardware + consulting bundle). $3,500 structure already ack'd. Plus: confirm Astra Ribbon Cutting cancel scope (May 18 02:21 UTC — likely EDC-side event, not Daniel Guadiano's Astra Restaurant)
- [ ] **Watch — Taiwo inbound deliverability:** Forwarded *"Hi Fitlogic"* test May 17 03:19 UTC to verify `fitlogicfunctionalmedicine.com` inbox is accepting mail. Pairs w/ May 14 outbound watch + May 6 Resend silent-failover. Confirm before Wed May 20 in-person walkthrough. Also: capture whether Jacob's new Alloy ATX OneDrive folder access (May 18 23:00 UTC) unblocks FB business ID debugging

### 🔥 May 18 — Monday Collaboration (Andres-absent edition) — three project directives
Source: [[raw/teams-transcript-monday-collaboration-2026-05-18]], [[wiki/meetings/2026-05-18-monday-collaboration]]
- [ ] **🔥 Adeleke:** Finish **PowerPoint + HTML design polish** (Andres opening directive); HTML *"already good to go"* per Andres, PowerPoint design is the remaining gap
- [ ] **🔥 Adeleke:** Ship **manual color/customization control on brand-DNA staging**; resolve multi-step ↔ coach token mismatch. Manual-input fallback exists under *"Generate Branding"* but is **untested end-to-end** — every Moil 360 onboarding of a customer without a website depends on it
- [ ] **🔥 Taiwo:** Send testing-account emails + passwords for the **three projects** to Jacob this week; **EOW deployment call** with each customer (Fri 2026-05-23 target)
- [ ] **🔥 Jacob:** Test Meridian + brand-DNA on staging; give feedback to Adeleke. **No on-record mention** of the May 15 KPI-tracking deliverable, Friday May 22 cadence, or LinkedIn-SMB outreach during the call — watch the window
- [ ] **🔥 Team:** Investigate **business-plan PPT email-delivery bug** (Jacob: download works, confirmation email doesn't arrive). May share root cause with the May 14 outbound deliverability watch
- [ ] **🔥 Andres / Jacob:** Decide priority on **Request-a-Demo / Schedule-a-Demo** flow on moilapp.com — Jacob raised it twice on the call (login exists, demo flow doesn't). Connects to LinkedIn-SMB outreach: without a demo capture surface, the cold-outbound work has no in-product conversion path
- [ ] **Standing — FitLogic (Andres directive):** **hold production push** until the website rebuild is complete *"by someone else."* No code-side action; surface the rebuild ETA to unblock
- [ ] **Standing — Meridian (Andres directive):** ready it + internal test; **[[wiki/people/travis-sutherland|Travis]] triggers the push** when comfortable. Pairs with Taiwo's May 14 Travis@zoho.com verification-code re-request item
- [ ] **Watch — pattern signal:** **First Andres-absent Monday Collaboration on record.** Team defaulted to demo + content read-aloud, not structured ship-status. If this becomes a pattern, the Monday call needs a written-agenda discipline rule. **Adeleke heavy participation (325 cues) soft-closes the 7-day silence** — but xAI / Anita / Gemini items individually still open

### 🔥 May 15 — Moil marketing team reset (Friday cadence + KPI ownership + LinkedIn SMB outreach)
Source: [[raw/teams-transcript-moil-marketing-team-call-2026-05-15]], [[wiki/meetings/2026-05-15-moil-marketing-team-reset]]
- [ ] **🔥 Same-day 2026-05-15 — Jacob:** locate Taiwo, report back why **FitLogic** delivery is overdue (was due last week; only change required was one email address). Andres expects an answer right after his current meeting. Cross-ref to [[wiki/meetings/2026-05-14-megan-taiwo-fitlogic-2fa-godaddy-session|May 14 GoDaddy delegate session]] — 2FA/domain blocker closed; FitLogic feature ship still open
- [ ] **🔥 2026-05-15 — Jacob:** confirm **Alloy Facebook access** status (no email seen from Facebook). If still blocked, Andres pulls existing Alloy images and posts by Monday 2026-05-18 himself (willing to work weekend)
- [ ] **🔥 Before Fri 2026-05-22 — Jacob:** research + set up **KPI tracking** for Moil social (likes, comments, organic shares — team-generated shares don't count — manual invitations sent, conversion). Build the tracking process; first deliverable lands at the Friday results-and-planning call. **Owns the metrics surface end-to-end**
- [ ] **🔥 Before Fri 2026-05-22 — Ablad:** 1–2 hour market research alongside Jacob. **Specifically follow through on the LinkedIn-to-SMB outreach mentioned in a prior meeting, never executed.** Study reference companies: Claude, ChatGPT, YC launch/demo videos, Motion (esp. hyperframes by Hai Jen — Andres' reference re-flagged ~3 weeks old)
- [ ] **🔥 Before Fri 2026-05-22 — Jacob + Ablad joint:** build a **strategy *from* the research, not a research dump**. Deliver to Andres for review before any new content is produced. **Watch:** side conversation after Andres dropped — both defaulted to *"use Grok to identify peer AI companies"* within 30 seconds of Andres' explicit *"if anybody can tell you if it's ChatGPT, it'll be me"* preempt. Check May 22 deliverable for ICP-segmentation depth signal
- [ ] **2026-05-18 — Andres:** pull existing Alloy images from his files; post by Monday; willing to work weekend if Alloy access doesn't land today
- [ ] **Standing — new cadence:** Friday = Ablad delivers content for the *following* week; team reviews previous week's results; Sat/Sun revisions; posts go live Monday. Monday call stays focused on that week's delivery, not strategy. First Friday call: **2026-05-22**
- [ ] **Standing — manual-outbound floor:** Jacob's **26–40 invitations/month** is the **floor** under the May 11 *"10 real DM conversations/day"* rule (~200/month if hit perfectly). If the manual loop works, Moil hires a dedicated person
- [ ] **Open thread — Spanish content regression:** was ~20 posts/week, now 0. *"Someone made the decision and we just stopped."* Ablad to surface root cause as part of his research deliverable
- [ ] **Capture (pattern):** today is the first **structured rebuild** of the marketing motion vs. the Apr 24 closure-threat or the May 11 per-person discipline rules. **Leading indicator:** depth of May 22 joint deliverable

### 🔥 May 14 — Email-digest items requiring action
Source: [[raw/email-digest-2026-05-14]], [[raw/signal-briefs/signal-brief-2026-05-14]]
- [ ] **🔥 Andres:** Draft Mac Decision Brief **SoW (hardware spec + consulting bundle)** before scheduling the *"let's talk … align on consulting piece"* call John asked for May 15 13:23 CDT. John is comfortable with $3,500; **consulting scope is the open variable**, not hardware. Bring a one-pager to the call, don't go in cold
- [ ] **🔥 Andres + Jacquie:** Confirm check arrival on the **33-license Buda EDC expansion** (invoice for 13 + 20 more); load the 10 new license slots once funds clear. **First quantitative on-record license expansion beyond per-cohort distribution** — protect this revenue surface from operational drift
- [ ] **🔥 Andres / Steve:** **Three live escalations stacked on Adeleke** with no public ack across 7+ days — (1) xAI Grok 4.3 retirement (re-forwarded May 14 20:10 UTC), (2) Anita Lansing's 2nd console-paste May 14 18:07 UTC (no fix shipped after May 13 forward), (3) Gemini 3.1 Flash Lite May-25 cutoff (no reply since May 12 forward). **Direct nudge before May 15 standup; if silent through May 16, default to phone/Teams call** — Apr 21 *"Steve fixes via Claude Code same-day"* pattern is broken
- [ ] **🔥 Andres / Engineering:** Anita Lansing sent a **second console-error paste** May 14 18:07 UTC on the same *"Inspect"* thread, **24h after the first** — paid-surface bug in second-ping territory. Either unblock Adeleke or escalate to Taiwo before the third ping (active Moil 360 user)
- [ ] **🔥 Andres / Jacob:** Confirm Jacob is hitting the May 11 *"10 real DM conversations/day for Moil"* target *alongside* the May 14 reactive customer-service threads (Linda Jungle Flavorz follow-up + GRGT license + Anita relay), not displaced by them. First time the daily-correlator has framed reactive-volume crowding-out as a risk on Jacob
- [ ] **🔥 Andres:** Stand up a **Moil-owned outbound-only domain** (e.g., `getmoil.com` / `try-moil.com`) via M365/GoDaddy mirror of the FitLogic two-domain pattern; route Content 360 / SMB cold sends through it; keep `andres@moilapp.com` for warm + EDC threads. **May 14 was the heaviest single-day SMB load (18 sends) on the same address previously flagged for FitLogic Gmail-spam** — and the same day Andres architected this exact hedge for Megan. **Decide before reply rate dips below 1%, not after.** See [[wiki/concepts/ai-cold-outreach]]
- [ ] **🔥 Andres:** Watch [[wiki/people/katherine-silvas|Katherine]]'s reply to the May 14 14:46 CDT Helotes partnership follow-up (22d slip past Apr 29–May 6 cadence target). If silent by ~May 21, **escalate via [[wiki/people/mayra-adams|Mayra]] channel** (exec secretary), not direct re-ping
- [ ] **Jacob → Linda (in-flight):** Ship the [[wiki/people/linda-horuke|Linda Horuke]] / Jungle Flavorz **website update by May 16/17** — the May 14 *"business email access and next steps"* follow-up is the mid-flight check, not the ship. **Two reps in a row of stated rhythm** at risk if missed
- [ ] **Capture (Buda EDC public-figure packaging signal):** [[wiki/people/casey-earley|Casey]] requested Andres's bio May 14 14:56 CDT — paired with John's *"Buda Business Leader / AI Convening"* + the May 13 EDC magazine 2-page Moil + HIVE spread + Jacquie's 33-license expansion = **4 EDC-side public-facing surfaces lit up simultaneously this week.** Worth packaging: ask Casey what publication/use the bio is for; build a single canonical Andres-bio + headshot + one-paragraph-Moil-pitch kit so future asks are zero-friction
- [x] ~~**Watch:** [[wiki/people/megan-miller|Megan]] in-person meeting Teams invite sent 16:38 UTC for *"Megan & Andres in person"* — separate from the locked Wed May 20 10–11 AM CT FitLogic walkthrough; confirm whether this is the same calendar entry or a second touchpoint~~ ✅ **Resolved May 15** — Megan accepted *"Megan & Andres in person @ Wed May 20 10am"* 09:26 CDT; same single calendar slot, not a duplicate
- [ ] **🔥 Tue 2026-05-26 — Becky × Andres SIREN follow-up** ([[wiki/people/becky-torres|Becky]] picked the date May 15 13:04 CDT after the May 12 in-person/Teams two-slot proposal). Confirm format (in-person at SIREN preferred per the May 6 daily-correlator read) in Andres's accept reply; bring the corrected build + named feedback rhythm. 11-day window — no proactive design changes per May 6 standing rule
- [ ] **Watch — [[wiki/people/monica-davidson|Monica]] × [[wiki/people/jordan-kaiser|Jordan]] intro:** Monica replied 2026-05-15 10:24 CDT *"happy to help, today or Monday?"* on the senior-citizen-research intro thread. **First end-to-end validation of the Chamber-as-cohort-warm-intro pipeline if Jordan books a slot.** Track outcome — if it converts, replicable pattern for other Cohort 4 ICP-access asks

### 🔥 May 14 — FitLogic Outlook migration session (GoDaddy delegate + security pattern)
Source: [[wiki/meetings/2026-05-14-megan-taiwo-fitlogic-2fa-godaddy-session]]
- [ ] **🔥 Tonight 2026-05-14 — Taiwo:** finish creating the new Outlook account against `myfitlogic.com`; verify the email and the domain; complete the GoDaddy delegation flow. Migration target: ready for Megan tomorrow morning
- [ ] **🔥 Tonight 2026-05-14 — Taiwo:** re-run the **Meridian** verification-code request that landed in the empty `Travis@zoho.com` mailbox; ping Andres once re-requested
- [ ] **🔥 Tonight 2026-05-14 — Andres:** once Taiwo re-requests, get the Meridian verification code from [[wiki/people/travis-sutherland|Travis]]
- [ ] **🔥 Fri 2026-05-15 AM — Andres:** send Megan access to the new Outlook-on-`myfitlogic.com` system "first thing tomorrow"
- [ ] **Mon–Tue 2026-05-18 → 19 — Megan + Michelle:** play with the new system, try to break it, surface bugs before Wednesday
- [ ] **🔥 Wed 2026-05-20 10:00–11:00 AM CT — Andres + Megan + Michelle:** in-person walkthrough at FitLogic; fix anything Megan/Michelle flagged. **Closes the May 7 next-week in-person visit commitment**
- [ ] **Post-deploy — Megan:** rotate all passwords on touched accounts (GoDaddy, Connections, the new Outlook mailbox); 2FA stays on
- [ ] **Capture for Moil 360 playbook:** Andres articulated the standing security rule on transcript (*"we should never have continued access … only use it when we're working on something … once we deploy, you should change all of your passwords"*) — first on-record. Pull into customer-account-touch policy doc
- [ ] **Watch (low priority):** GoDaddy "individual domains" delegate UI quirk (couldn't scope to one domain — defaulted to FitLogic Functional Medicine); unfamiliar `508F6B8D9.conversions.godaddy.com` forwarding rule Megan disabled — confirm nothing relied on it before mailbox goes live
- [x] ~~**🔥 May 11 — Andres:** text Megan to coordinate the 2FA code for the new Moil-owned sales email so Taiwo can finish wiring GitHub + Vercel + GoDaddy~~ ✅ **Closed May 14** — GoDaddy delegate granted at account level; GitHub access ready (Taiwo confirmed *"everything is ready"* end of call)
- [x] ~~**🔥 May 7 — Andres:** schedule next-week in-person visit to FitLogic to walk Megan + Michelle through the CRM together~~ ✅ **Locked May 14** — Wed 2026-05-20 10:00–11:00 AM CT at FitLogic

### 🔥 May 13 — Jordan Kaiser HIVE Cohort 4 first 1:1 (senior-tech autonomy)
Source: [[wiki/meetings/2026-05-13-jordan-andres-1-1]], [[wiki/people/jordan-kaiser]]
- [ ] **🔥 Today — Andres:** Verify the [[wiki/people/monica-davidson|Monica Davidson]] intro email actually went out mid-call (Andres said *"sending right now"*); if missing, send it now — Jordan is gated on this for senior-home interview access
- [ ] **🔥 This week — Andres:** Confirm with Buda EDC whether **Cohort 4 members get the full-year Moil license** (Andres told Jordan *"we'll probably get this finalized this week"*); close the loop with the cohort once confirmed — **second independent surfacing of this precedent in 24 hours** (first was confidential to Caro 2026-05-12)
- [ ] **Jordan homework (3-week horizon):** sign up moilab.com/candidate + moilab.com (business, 21-Q onboarding); build 25-mile-radius list of 10 Buda senior homes; cold-email all 10 with EDC cohort framing; run 5–10 in-person diagnostics interviews (incl. Port Arthur trip to his mother's senior center); reach out to Matthew Wright / Jeff Kaufman (Buda senior-citizens org leadership — names to verify)
- [ ] **Capture for [[wiki/moil/product-roadmap]]:** Moil now ships a **silent 3-emails/week proactive coaching feature** to active business users (Monday + throughout-week pending items, challenges, agentic nudges; pulled from Clio model). First time documented in the Brain — add a roadmap line when team formally announces

### 🔥 May 12 — Perseus Defense YC referral meeting (FIRST documented attempt for Clio)
Source: [[wiki/meetings/2026-05-11-monday-collaboration]], [[wiki/orgs/perseus-defense]], [[wiki/people/jennifer-storm]]
- [ ] **🔥 Tue May 12, 8 AM CT — Andres** meets Perseus Defense founders (YC S25 defense-tech, Buda HQ, ~$6–8M raised, $500K Buda EDC incentive Dec 2025) introduced in person by [[wiki/people/jennifer-storm|Jennifer Storm]]. Goal: **YC alumni referral for [[wiki/projects/clio|Clio]]**. Posture: respectful of their time, brief Clio pitch, ask for the referral. Andres' framing: *"they're not coming to meet me, they're coming to do her a favor."* **Capture founder names + outcome post-meeting.**
- [ ] **Andres (post-meeting):** if referral lands, route into the Clio YC application thread immediately — alumni referrals are time-sensitive. If declined, send Jennifer a thank-you regardless (relationship preservation > outcome)

### 🔥 May 11 — Monday Collaboration team rules (effective immediately)
Source: [[wiki/meetings/2026-05-11-monday-collaboration]]
- [x] ~~Andres: pick up Buda EDC magazine; reply to Inna; text Megan 2FA; Jacob: post Inna's Mother's Day video~~ ✅ All four closed May 11–14 (see meeting page)
- [ ] **This week — Taiwo:** migrate GitHub + Vercel access to new Moil-owned sales email; document/share new Supabase credentials; notify Jacob once live for test sends. **(In-flight; FitLogic ship today is May 15 same-day Jacob probe per top-of-MEMORY)**
- [ ] **Ongoing — Jacob:** **10 real DM conversations/day for Moil**, no copy-paste. May 15 marketing reset added **26–40 invitations/month floor**; daily cadence still applies
- [ ] **Ongoing — Ablad:** plan weekly content list against **holiday calendar**; **check Inna's Google Drive immediately** when she signals an upload; if uploaded video doesn't fit current week, email Inna to slide it — never silently skip
- [ ] **🔥 This week — Team:** fix Ablad's chronic inability to sign into `Ablad@moilapp.com` on his phone (contact Microsoft if needed). Long-unresolved; not re-mentioned May 15 — still likely open
- [ ] **Watch — pay-the-team:** Mark Polanco first Connectex payment expected next week (~May 18); city contract payment delayed by city-lawyer redlining. As soon as either lands, Andres pays Jacob + Taiwo for both missed months

### 🔥 May 7 — Inbound M&A inquiry: Vision Point Capital (FIRST on-record)
Source: [[raw/email-digest-2026-05-07]], [[raw/signal-briefs/signal-brief-2026-05-07]], [[wiki/orgs/vision-point-capital]], [[wiki/people/chris-gomes]]
- [ ] **🔥 Andres (by May 14):** Send holding reply to [[wiki/people/chris-gomes|Chris Gomes]] (`chris.gomes@visionpointcapital.com`) on his *"Valuation and EBITDA Multiple for Moil"* inquiry. **2026-05-07 daily-correlator flagged silence as anomaly** vs Andres's same-day reply cadence (Becky/Sarah/Adeleke); silence here defaults to *"ignored"* not *"declined gracefully."* Lightweight engage = ask for valuation/EBITDA-multiple benchmark; decline = polite *"not for sale, happy to keep in touch"* — both preserve the data point at zero cost

### 🔥 May 7 — Email-digest items requiring action
Source: [[raw/email-digest-2026-05-07]]
- [x] ~~**Andres:** Reply to [[wiki/people/becky-torres|Becky's]] May 6 process-confusion thread~~ ✅ **Replied May 7 12:18 UTC** (apology + ask for feedback specifics). **Watch:** reply did *not* ship the named cadence the daily-correlator flagged as the actual unblock — if Becky's next reply re-asks *"is this a call or in-person?"*, the apology-only frame was insufficient and Andres needs to give her a one-line *"video uploads → 48–72hr build → monthly in-person at SIREN"* rhythm
- [ ] **Andres:** Track replies on the **May 7 chamber-breakup batch** (Hunterdon, Point Pleasant Beach NJ, UCEDC, Jefferson County WV). NBCC Apr 29 precedent says breakups *do* surface signal — score by 7-day reply rate
- [ ] **Andres:** Watch the **May 7 SMB cold-outbound batch** — first sustained day-over-day SMB campaign with 3 subject-line variants under live A/B test. If reply rate < 1%, evaluate domain-warmup or rotation away from `andres@moilapp.com` (deliverability risk; same address that hit Gmail spam at FitLogic)
- [x] ~~**Buda EDC / Sarah Miller — Jun-18 hotel logistics**~~ ✅ Hilton reservation #3467031844 confirmed May 7 (Sarah's name, Andres on the room). Buda EDC sponsoring TEDC travel — precedent worth capturing for next EDC-booked keynote
- [ ] **Adeleke:** GCP 150% budget alert (May 7) was intentional (Adeleke set it). $19K Gemini-API spike connected to PR #74 Clio Gemini-cascade work. **No action required** — instrumentation working as designed; capture as confirmation that May 4 cost-discipline rule + per-project budget alerts are now load-bearing

### 🔥 May 7 — Megan × Andres CRM handoff (Resend blocker resolved)
Source: [[wiki/meetings/2026-05-07-megan-andres-fitlogic-crm-handoff]]
- [ ] **🔥 [in-flight, 6d slipped from 2026-05-08 AM target] Andres / Eng:** Configure Microsoft 365 mailbox for `myfitlogic.com`; ship Megan CRM login credentials wired to `connections@myfitlogic.com`. **Taiwo finishing tonight 2026-05-14** under the May 14 working-session block above; Andres to send Megan access first thing 2026-05-15
- [x] ~~**🔥 Andres:** Schedule **next-week in-person visit to FitLogic** to walk Megan + Michelle through the CRM together~~ ✅ **Locked May 14** — Wed 2026-05-20 10:00–11:00 AM CT at FitLogic
- [ ] **Andres:** Design the "clicked-link" trigger flow for the CRM (Megan's ask) — manual vs. automated, and how to keep tone non-spammy. Deferred, not committed
- [ ] **Andres + Megan:** Ongoing Keap contact-list cleanup (~5,341 rows) — duplicates + obvious fakes (`sample@email.com` etc.); Megan starts low-volume only with the test-contact flag while Michelle ramps
- [ ] **Megan (this week):** Send Andres his lab order (fasting bloodwork, 8–10 vials) — possibly switching from LabCorp to a different vendor; she'll text when it's in the Charm portal
- [ ] **Megan (Q2):** Add monthly **Women's Vitality Group Circle** (in-person) to FitLogic membership; design quarterly equivalent for men — wants Andres's input on format
- [ ] **Watch / capture:** "My Life on Purpose" LLC + menopause/andropause coaching-certification course are a future Moil 360 surface (course site + email + CRM). Track when Megan formalizes

### 🔥 May 6 — Andres × Taiwo session: Siren Beauty + FitLogic blockers
Source: [[wiki/meetings/2026-05-06-andres-taiwo-ongoing-projects]]
- [ ] **🔥 Andres:** Reply to [[wiki/people/becky-torres|Becky's]] email — apologize for the wrong staging build; explain the staging-vs-prod misfire; point her at the corrected build; confirm video-feedback items addressed
- [x] ~~**🔥 Andres:** Verify `fitlogicfunctionalmedicine.com` Resend domain with Megan this afternoon~~ ✅ **Resolved May 7 via workaround** — original domain Cloudflare-locked; pivoted to `myfitlogic.com` (new domain Megan registered + provisioned `connections@myfitlogic.com` via GoDaddy MS365). Outbound now runs from there
- [ ] **🔥 Taiwo:** Push FitLogic CRM updates to the **production-side repo** (not just staging) — third surfacing of the Apr 28 push-discipline rule
- [ ] **🔥 Taiwo:** Research with Claude — email-sequence queue behavior when multiple campaigns collide past Vercel 1-cron/day or Gmail 50/day caps. Don't assume; verify
- [x] ~~**Taiwo:** Send Andres screenshot of Resend domain-verification failure page~~ — moot after May 7: Megan stood up `myfitlogic.com` instead of fixing the Cloudflare-locked original
- [ ] **Taiwo:** Make Siren Beauty **mobile responsive** ASAP; confirm "science" wording fully removed; remove duplicate Siren logo from header; bolden header text + add white shadow for hero-image scroll readability
- [ ] **Taiwo:** Polish FitLogic — rename `lead_source = "unknown"` → `"initial upload"` in DB; split AI vs manual sequences in campaigns UI; fix click-tracking redirect to use prod URL (not `localhost:3000`)
- [ ] **Standing rule (Siren Beauty engineering):** No proactive design changes — only deliver items Becky explicitly calls out. Reverses prior bias on this account
- [ ] **Architectural debt — silent failover:** Resend → Gmail-API fallback masks deliverability failures from the dashboard. Capture as known issue; surface failovers in admin UI

### 🔥 May 5 — Christy Mawdsley discovery (Roxana Yglesias referral)
Source: [[wiki/meetings/2026-05-05-christy-mawdsley-discovery]], [[wiki/people/christy-mawdsley]]
- [ ] **Andres:** 1:1 onboarding call once Christy completes Moil 21 questions; help her stand up a referral program (her highest-leverage move given word-of-mouth concentration). Watch for free-trial signup at moilab.com (Christymawdsley@gmail.com) + nudge if 21Q not started within 7 days. **First Roxana Yglesias outbound referral on record**

### 🔥 Carried debts demoted to log.md
- **Run 58 (2026-05-19):** May 4 Monday Collaboration cost-discipline block (8 items, 15d stale) — Taiwo got Moil 360 license May 4 (confirmed on taiwo page); Adeleke Gemini Flash-Lite cron switch tracked on adeleke page; Taiwo open-source email-infrastructure + product unification tracked on taiwo page; Andres free-trial marketing + accelerator + credit-card + weekly cost-review standing rule — all tracked on pillar pages; demoted to [[log.md]]
- **Run 57 (2026-05-18):** May 6 email-digest items block (8 items, 12d stale) — Becky process-confusion reply was already partially addressed May 7; B-Coach INTERNAL_ERROR loop, Linda Horuke 30-min call, Oscar Esquivel reply latency, Heather Skeen no-touch-til-May-13, Steve xAI assessment — all tracked individually on their pillar pages; demoted to [[log.md]]
- **Run 53 (2026-05-15):** May 1 outstanding non-keynote items (John video-workflow walkthrough; Marilyn/Nuovo discovery) + May 4 HIVE Cohort 4 1:1 cadence (Christine+Kat Train Depot + Claudia homework + Sarah recon) — 11–14d stale; tracked on [[wiki/people/christine-stjohn]], [[wiki/people/claudia-sanchez]], [[wiki/people/sarah-hive-cohort]], [[wiki/people/john-costilla]], [[wiki/people/marilyn-martinez]]; demoted to [[log.md]]
- **Run 52 (2026-05-15 weekly compile):** Apr 30 HIVE Cohort 4 first 1:1s + Apr 29 AI-spend observability emergency + Apr 28 Connectex go-live sprint — all 15d+ past their date label; moved to 💤 Deferred auto-demoted subsection (still actionable, just no longer "this week")
- **Run 51 (2026-05-15):** Apr 29 NBCC + west-coast SMB conversion-lane block + Apr 29 FitLogic delivered P0 bug list — both 16d+ stale; tracked via [[wiki/projects/fitlogic]], [[wiki/concepts/ai-cold-outreach]], [[wiki/moil/gtm]]; demoted to [[log.md]]
- **Run 50 (2026-05-14 PM):** Apr 28 Inna CRM bug residue + Apr 28 moilapp.com SEO emergency + Apr 29 Buda EDC × GIS WebTech (held May 13) + May 1 TEDC keynote prep — all 14d+ stale; demoted to [[log.md]]
- **Run 48 (2026-05-13 PM) + Run 44 (2026-05-11):** older Apr 30 Hays CISD + Apollo cleanup + Anita re-engage + John Costilla lunch + Victor UDC blocks demoted; see [[log.md]] for full chain back through Runs 38–40

---

## 📅 Next 2–3 weeks (Apr 29 – May 12)

- [ ] **Tue May 12** — Christine + Kat meet [[wiki/people/sarah-hive-cohort|Sarah]] (bookstore + wine) — competitive recon; don't disclose Train Depot interest
- [ ] **Fri Jun 19, 8 AM CT** — **TEDC Mid-Year Conference keynote**, Hilton Granite Park, Plano TX (booked by [[wiki/people/sarah-miller|Sarah Miller]] May 1). First TX statewide EDC speaking slot
- [ ] **[[wiki/people/daniel-guadiano|Daniel Guadiano]] / Astra Restaurant** — both Apr 22/23 slots proposed went without confirmation; re-propose new slot or close. First hospitality ICP if it closes
- [ ] **Reply to [[wiki/people/irma-mason|Irma Mason]]** re: Mrs. Unger job-search referral — still open from Apr 19
- [ ] **🔥 Reply to [[wiki/people/rashaka-boykins|Rashaka Boykins]]** — consolidate answer to Apr 21–22 inbound (LLM marketing + traffic/LinkedIn-IG); close on $600/yr vs $900/mo offered Apr 24
- [ ] **Re-queue Caroline Mungenast (Birmingham Business Alliance)** — was OOO until Apr 24; should be back; re-engage. Shannon Cameron PSA assets (Apr 21) also pending reply
- [ ] **Jacob Centeno referral partnership** — set up lightweight workflow, decide commission/credit model
- [ ] **Ana Vetencourt (URBANZUELA)** — review Google Doc draft she sent; provide feedback
- [ ] **Elisa Alaniz follow-up** — Apr 24 phone call slot; outcome not captured — confirm next step or close

---

## 🔧 Technical debt — Teams Apr 5–12 (see [[log.md]] Run 15 for context)

- [ ] Apr 5–12 Teams residue: Roxana 21Q + assets + GoDaddy + GSC + satellite domains + wellness referrals; Eden website discovery follow-up; tour-guide `data-guide-id` bugs + generic text + auto-scroll; Segment writeKey staging fix + image-context regression + Supabase `business-intake` deploy + Meridian domain/Stripe + phone-signup permanent fix; daily video rhythm; Sun show raffle email; Adeleke FB account; credentials migration off Teams

---

## 💤 Deferred — hard dates

- [ ] **Jul 1, 2026** — Shay Foley / Johns Creek Chamber re-engage (chamber budget year starts). Pitch AI tools for entrepreneurs w/ Buda EDC reference. [[wiki/people/shay-foley]]
- [ ] **Sep 1, 2026** — Buda HIVE training program curriculum jointly with HIVE + Incubator Strategist Team
- [ ] **Post-Apr 15** — CampaignOS with Jennifer Storm: circle back on MVP scope; Andres offered "little to no cost" — decide commitment level. [[wiki/concepts/campaignos]]

## 💤 Deferred — auto-demoted by weekly compile (date label >14d)

### Apr 30 — HIVE Cohort 4 first 1:1s landed + Cohort 4 PSA executed at in-person review (demoted Run 52, 15d)
Source: [[wiki/meetings/2026-04-30-heather-skeen-coaching]], [[wiki/meetings/2026-04-30-carolina-coaching]], [[raw/email-digest-2026-04-30]]
- [ ] **Andres:** Drop by [[wiki/people/carolina-caro|Caro's]] house in person — Austin Street behind [[wiki/orgs/meridian-buda|Meridian]]. Walk the floorplan in person to validate the women-coworking layout
- [ ] **Andres:** Save [[wiki/people/heather-skeen|Heather Skeen]]'s HIPAA-compliant cell number (routes from office line to cell)
- [ ] **Caro homework:** complete Moil 21 questions (signed up first month free during the call); interview 5–10 women from Cohort 4 to validate ICP and willingness to pay; map floorplan to revenue
- [ ] **Heather homework:** research daycare PD requirements (12 domains, hours, certification cycle); research market rates for CEU providers in TX; package 3–4 program bundles at ~$1,000/yr per daycare; build 25-mile-radius daycare prospect list (postcard + 3-email sequence + call); attorney consult on "Providence Counseling and Therapy" name change (insurance-contract impact); fix the $500/3hr pricing for the NC fall engagement

### Apr 29 — AI-spend observability emergency (May 4 partly resolved) (demoted Run 52, 16d)
Source: [[raw/email-digest-2026-04-29]], [[wiki/people/adeleke-tolulope]], [[wiki/meetings/2026-05-04-monday-collaboration]]
- [ ] **Adeleke / Andres:** Per-feature AI-spend accounting for OpenAI + Gemini before next billing cycle (the Saturday 5/2 Gemini spike was the weekly health-summary cron — fix landing via May 4 Flash-Lite + active-user-gate switch)

### Apr 28 — Connectex go-live sprint (first payment now expected ~May 18) (demoted Run 52, 17d)
Source: [[wiki/meetings/2026-04-28-mark-polanco-connectex-walkthrough]]
- [ ] **Andres + Mark:** Squarespace push once Mark sends login; Resources/blog section; mid-May lunch; refile EDC reimbursement; Yealink LTE deck-station doc; BuiltFirst marketplace-billing block
- [ ] **Taiwo + Eng:** Connectex repo to remote (no local-only — third surfacing); Gemini API key; Airtable contact import; finish Contacts tab; seed Knowledge Base for AI tier-1 ticket testing

## 🏗️ Strategic — no hard deadline

- [ ] **Fantelo clarification** — pivot, separate venture, or sub-brand? Consumes engineering time w/ no documented strategy. [[wiki/concepts/fantelo]]
- [ ] **GitHub org cleanup** — archive 6+ stale repos; dedupe BlueprintsForSuccess; consider `Moil-Clients` org
- [ ] **Moil license case study** — public "City EDC × Moil" for decks + expansion (Queen Creek, Johns Creek, Greater Buda Chamber)
- [ ] **Claude Code security audit** — what permissions does it have on this Mac Mini (SSH, AWS, `.env`)? Decide boundaries before autonomous skills

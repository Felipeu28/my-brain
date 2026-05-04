# Moil Brain — Ingestion Log

This file tracks every source that has been processed by `/kb compile`. Claude Code appends an entry here after each ingestion run.

---

## 2026-05-03 — Run 31: Brain self-audit + 4-week implementation plan + signal brief 2026-05-02

**Trigger:** Automated scan for unprocessed `raw/` files. Four high-signal new files since Run 30:
- `raw/audits/2026-05-03-ingestion-and-synthesis-audit.md` (Brain end-to-end audit — every launchd job, every synthesis script, every freshness check)
- `raw/audits/2026-05-03-implementation-plan.md` (4-week phased rollout, 14 items, 7 resolved decisions, Week 1 execution log)
- `raw/weekly-sessions-2026-05-03.md` (72-session rollup with 7 automation self-runs filtered out — item 8a already shipped)
- `quartz/content/raw/signal-briefs/signal-brief-2026-05-02.md` (May 2 cross-source: John Costilla praise + Nate Herk Claude Design masterclass; Inna silence anomaly past threshold)

Plus ~30 low-signal session log files in `raw/sessions/claude-code-2026-04-{26..30}-*.md` and `raw/sessions/claude-code-2026-05-{01..03}-*.md` — bookkeeping only, intelligence already absorbed via the daily correlator + per-project rollups (item 6 wrote to `wiki/projects/moil.md` § Last 7 days from these sessions today).

**Pages created (1):**
- [[wiki/summaries/brain-audit-2026-05-03]] — Routing layer over the audit + implementation plan; captures the 7 resolved decisions, Week 1 shipped status, Week 2–3 open items. Sized as a single summary page (not decomposed) following the [[raw/brain-knowledge-layer-analysis|brain-knowledge-layer-analysis]] precedent — these are meta-content about the Brain, not external knowledge to graph

**Pages updated (1):**
- [[wiki/summaries/README]] — Brain architecture & meta section now lists the audit summary

**Pages noted (created earlier today by the implementation plan execution, not by this ingestion run):**
- [[wiki/projects/moil]], [[wiki/projects/clio]], [[wiki/projects/fitlogic]], [[wiki/projects/connectex]], [[wiki/projects/buda-edc-hive]], [[wiki/projects/meridian-buda]] — six startup/client project hub pages, committed `e246967` 2026-05-03

**Operating layer:**
- [[index]] — Run 31 header, raw source count 388 → 389 (+1 in `raw/audits/`; the implementation plan + signal-brief + weekly-sessions are not in `raw/audits/` and either already counted or live in `quartz/content/raw/`), wiki page count 278 → 279 (+1 = brain-audit summary), summaries 20 → 21
- [[MEMORY]] — **no update.** Brain self-upgrade items are internal infrastructure, not external commitments to clients/people. They live in [[wiki/summaries/brain-audit-2026-05-03]] for future-Claude reference. Daily action list stays focused on customer/partner work

**Key intelligence from Run 31:**

1. **🔥 Brain self-audit shipped Week 1 in a single day (2026-05-03).** Four critical fixes live: (a) `com.moil.brain.entity-graph.plist` loaded into launchd — `wiki/hot/relationship-radar.md` was frozen at Apr 22 for 11+ days, morning briefing's "going cold" list was running on stale data; (b) freshness sentinel (`bin/sentinel.sh` + `sentinel-config.tsv` + plist + email-on-critical) deployed and wired into morning briefing; (c) `weekly-operating-brief.sh` schedule moved Sunday 20:00 → Monday 08:00 (laptop reliably awake then); (d) `scrape-x-bookmarks.sh` now quarantines 0-item runs to `*.zero-YYYY-MM-DD.md` and exits 2 instead of silently committing 234-byte placeholder files.

2. **🔥 The Brain is "input-rich, reflection-poor" — and the audit is the receipts.** Capture layer was working (morning briefing, Teams pull, email digest, X bookmarks, Claude sessions, GitHub activity, ChromaDB index = 3,156 chunks daily). Read-back layer was silently dead: entity-graph plist never loaded, weekly-operating-brief ran exactly once in 30 days (Apr 26), `weekly-sessions-*.md` was mechanical (count + truncated first prompt) polluted by automation-self-runs, **zero scripts queried ChromaDB**, episodic memory was write-only.

3. **Two "broken for 10+ days" failures in one day exposed the same anti-pattern.** GitHub Pages deploy red for 10 days (CI status line shipped 2026-05-03 fixes the surface) AND entity-graph plist unloaded for 11+ days. Both: a job stops running, no destination changes, no human checks. The systematic answer is the freshness sentinel — stat() the log files and destinations, render to markdown, embed in the morning briefing. **Adding observability cannot fail to be observed when the briefing is the readout surface.**

4. **🔥 Six `wiki/projects/` hub pages created today (commit e246967).** All four client projects (FitLogic, Connectex, Buda EDC/HIVE, Meridian Buda) promoted to first-class pages alongside Moil + Clio. Section 3a's "default no" rule for client-as-project was **overridden** — these four are big enough multi-quarter / multi-repo / custom-build engagements to earn their own pages. `bin/project-activity.sh` already ran once today and populated each `## Last 7 days` block from session + git + briefing data.

5. **K&T#1 (Karpathy CLAUDE.md ingest/query/lint loop) treated as already shipped.** Reconciliation between the audit and karpathy-tan-brain-recommendations.md: existing `knowledge-base/CLAUDE.md` + `/brain-ingest`/`/brain-query`/`/brain-lint` slash commands + `kb-health.py` lint pass already cover Karpathy's pattern. Single addition slotted: a Week-3 `## Related`-block lint pass that asserts every `wiki/people/*` and `wiki/projects/*` page carries explicit backlinks. **K&T#1 = done.**

6. **Orphan Claude sessions diagnosed as automation pollution.** All 11 `project: "-"` sessions in `~/.claude/projects/-/` are the daily-correlator's own automated invocations. Cause: launchd job runs `claude` with no working directory, so Claude Code derives the `-` project label. Fix routed to the session-learnings filter (item 8a, **already shipped** — `weekly-sessions-2026-05-03.md` shows *"7 automation self-runs filtered out — see ingest-claude-sessions.py:is_automation_self_run"*).

7. **Forks decided.** `~/agent-canvas-ui` (92 KB, openclaw fork, no recent commits, no brain refs) → delete; `~/wiki-os-brain` (235 MB, Ansub/wiki-os fork, last touched 2026-04-12, no brain refs, was an evaluated Quartz alternative) → archive to `~/archive/`. Andres to execute at his leisure.

8. **K&T#2 (gstack/clio-stack for Clio) routed to a parallel track.** Spinning up as a separate code session in `~/luna-brain`. Out of Brain plan scope.

9. **Signal-brief 2026-05-02 reinforces existing MEMORY items, no new commitments.** Cross-source connection: John Costilla praised the *business-coach-95s* video workflow May 1, Andres bookmarked Nate Herk's Claude Design masterclass (brand → deck → landing → launch video) Apr 29 — Andres is bookmarking the exact production loop he just sold John on. Mon May 4 in-person at HIVE is the natural anchor for the walkthrough commitment (already in MEMORY). Inna silence anomaly: Jacob sent updated podcast cuts May 1 14:59 UTC, **no Inna reply 2026-05-02** — the silence has crossed the May 4–5 nudge threshold MEMORY flagged. Both items already actionable from MEMORY; no update needed.

**Open Week 2–3 items (not yet shipped, tracked in [[wiki/summaries/brain-audit-2026-05-03]]):**
- Item 6 daily cron schedule for `bin/project-activity.sh`
- Item 7 morning-briefing restructure (`## This Week — Moil & Clio` + `## Client Project Pulse` injection)
- Item 8b full session-learnings extractor (LLM pass over per-session JSONL → Decisions / Tools / Recurring frictions / Unresolved). Item 8a (filter) shipped
- Item 9 wire ChromaDB historical context into `daily-correlator.py` (top-3 active persons → 90-day historical-context block)
- Item 10 `pattern-surfacer.sh` rolling 28-day pass + Wed/Sun 07:00 schedule
- Item 11 `compute-last-contact.py --write` mode → `wiki/hot/relationship-signals.md`

**Week 4 items shipped early (commit e340786):** concept-of-the-day rotation, append-and-review inbox, Monday two-sentence pitch + this-week's-mistake briefing block, Related-block lint.

**Sync step:** `bash scripts/sync_wiki.sh` mirrors all updates into `quartz/content/`. **Health step:** `python3 scripts/kb-health.py` after sync. Source files marked `ingested: true / ingested_at: 2026-05-03`.

**Source count:** 388 → 389 (+1 in `raw/audits/`; the second audit file + weekly-sessions are also in `raw/` but were already in the inventory; signal-brief lives in `quartz/content/raw/signal-briefs/` and is not counted by `kb-health.py`'s RAW_DIR rglob). Wiki page count: 278 → 279 (+1 = brain-audit summary).

---

## 2026-05-02 — Run 30: May 1 email digest + signal brief ingestion

**Trigger:** Automated scan for unprocessed `raw/` files. Two new files since Run 29:
- `raw/email-digest-2026-05-01.md` (committed May 1 18:31 by `email-digest` job — 24-hour window Apr 30–May 1; 13 received / 24 sent)
- `quartz/content/raw/signal-briefs/signal-brief-2026-05-01.md` (committed May 2 06:00 by `daily-correlator.py` — May 1 cross-source synthesis)

**Pages created (2):**
- [[wiki/people/sarah-miller]] — Buda EDC license coordination + external speaking-slot bookings; booked Andres into TEDC June 19 keynote slot. First direct booking contact May 1; previously surfaced only in the Apr 12 2-month email backfill (3-email license-coordination thread)
- [[wiki/people/marilyn-martinez]] — Identified primary contact at [[wiki/orgs/nuovo-entertainment|Nuovo Entertainment]] (`marilyn@nuovoentertainment.com`); closes the long-orphan "ownership unknown" gap on the Nuovo org page since Run 6

**Pages updated (8):**
- [[wiki/people/john-costilla]] — May 1 strong praise on the *business-coach-95s* videos; Andres offered to walk John through the video-creation workflow built on his brand. **John is shifting from EDC partner → active co-marketing surface this week**. Cc'd on the Jennifer Storm Letter of Recommendation thread
- [[wiki/people/jacquie-martinez]] — Issued the formal Cohort 4 PSA Apr 30 21:06 UTC; locked **Mon May 4 9 AM CT in-person PSA review** in the HIVE conference room (May 1 19:59 UTC). Andres accepted same day. **First in-person PSA review meeting between Andres and Jacquie since the Apr 15 Board vote**
- [[wiki/people/jennifer-storm]] — May 1 13:06 UTC asked Andres to finalize and return the AEDO Letter of Recommendation same morning; Andres apologized for the delay and sent the finalized letter at 14:59 UTC (cc John Costilla). Closed loop
- [[wiki/people/jacob-oluwole]] — May 1 14:59 UTC sent Inna two updated podcast video versions (with/without rotate; "ums" and silent fillers cleaned); 17:36 UTC confirmed Kim Dowers resent invites and offered further help (closing his named QC Chamber post-webinar onboarding ownership thread)
- [[wiki/people/inna-benyukhis]] — Re-cut podcast videos delivered May 1; **no reply from Inna across the May 1 digest** despite the Apr 28 in-person and 1-week-slipped CRM demo. The 3-step approval loop (Jacob → Inna → publish) is **stalled on her side**, blocking the LinkedIn/IG publish queued since Apr 27. Longest silence in any thread Inna is a party to in the Apr–May window
- [[wiki/orgs/buda-edc]] — Sarah Miller added to staff list; new sections for "Cohort 4 PSA — In-person review locked Mon May 4" and "TEDC Mid-Year Conference (June 19, 2026)"
- [[wiki/orgs/nuovo-entertainment]] — Marilyn Martinez identified as primary contact (closes the "ownership unknown" gap from Run 6); status updated; "Identify primary contact" open item closed; new open items for the May Website Discussion call + John Costilla community-tie confirmation
- [[wiki/moil/gtm]] — added "Cold campaign — May 1 update" section: 24 sends, 13 close-out / 6 story-led / 3 demo (incl. first South Dakota touch via Jeff Griffin / Sioux Falls); 5 inbound conversion signals (PSA mtg + TEDC keynote + John video co-marketing + Letter of Rec close + Nuovo owner identified) all in same digest. **Break-up template now functions as routine prospect-list cleanup tool, not last-ditch tactic**. *"EDC-feedback social proof"* variant should be tracked as a named template alongside demo + close-out

**Pages updated (operating layer):**
- [[MEMORY]] — opened ~5 new May 1 items (TEDC Jun 19 keynote prep, John video-workflow walkthrough at Mon May 4 anchor, Inna direct nudge if no reply by May 4–5, Marilyn / Nuovo Website Discussion call, May 1 break-up-day cadence template); closed Apr 29 Krystal block (both items DELIVERED) + compacted same-day post-coaching follow-up entry; Apr 30 PSA countersign re-anchored to the Mon May 4 in-person review; added Mon May 4 9 AM PSA mtg + Fri Jun 19 8 AM TEDC keynote to "Next 2–3 weeks". 200 lines (hit hard cap exactly).
- [[index]] — Run 30 header, raw source count 387 → 389 (2 new files), wiki page count 276 → 278 (+2 = 2 people), people count 55 → 57

**Key intelligence from Run 30:**

1. **🟢 Cohort 4 PSA round-trip lands in-person Mon May 4.** [[wiki/people/jacquie-martinez|Jacquie]] locked the meeting in the HIVE conference room (May 1 19:59 UTC) — **first in-person PSA review meeting between Andres and Jacquie since the Apr 15 Board vote**. Round-trip: Shannon Apr 21 → Joshua redline Apr 24 → Jacquie-issued PSA Apr 30 → Andres signs in person May 4 (10 days, end-to-end). The in-person format upgrades the contract motion from email-thread to relationship-anchored, and puts Andres on-site adjacent to John Costilla — natural anchor for the video-workflow walkthrough Andres offered the same day.

2. **🟢 First TEDC speaking commitment locked: Fri Jun 19, 8 AM, Plano TX.** [[wiki/people/sarah-miller|Sarah Miller]] booked Andres into the **TEDC Mid-Year Conference** keynote slot (Hilton Granite Park). **First Texas Economic Development Council speaking slot** for Andres — a state-level industry stage that scales the Buda EDC × Moil B2G template beyond Buda's audience. Sarah also surfaces as a new BEDC contact owning license coordination + external bookings — operational counterpart to Jacquie on the Moil-license side.

3. **🟢 John Costilla shifting from EDC partner → active co-marketing surface.** May 1 strong praise on the *business-coach-95s* videos ("strong praise on videos, story, pitch deck and messaging"); Andres offered to walk John through the video-creation workflow built on his brand. Combined with: (a) Apr 29 Brain Briefing forward, (b) Apr 29 OneDrive *business-coach-95s* share, (c) Wed May 13 GIS WebTech AI meeting, (d) cc on the Jennifer Storm Letter of Recommendation thread — John is now generating co-marketing surface area that wasn't there a week ago.

4. **🟡 Inna silence anomaly extends — longest of the month.** Jacob delivered re-cut podcast videos May 1 14:59 UTC (with/without rotate; *"ums"* and silent fillers cleaned). **No reply from Inna across the May 1 digest** despite the Apr 28 in-person meeting and a 1-week-slipped CRM demo. The 3-step approval loop (Jacob → Inna → publish) is **stalled on her side**, blocking the LinkedIn/IG publish queued since Apr 27. If no reply by May 4–5, Andres should nudge directly — Mon May 4 in Buda is a cheap text-ping moment.

5. **🟢 Long-orphan Nuovo Entertainment owner identified.** [[wiki/people/marilyn-martinez|Marilyn Martinez]] (`marilyn@nuovoentertainment.com`) accepted a *Website Discussion* calendar invite May 1 16:20 UTC. **Closes the "ownership unknown" gap that has been on the org page since Run 6.** The May call is the moment to capture next-phase scope and decide whether to convert to a Moil 360 license. Worth confirming with John Costilla whether Marilyn is part of the Buda community network (John named "Nuovo" in earlier email threads).

6. **🟢 Letter of Recommendation closed in 11 minutes wall-clock under same-morning deadline.** Jennifer asked Andres at 13:06 UTC to finalize and return same morning; Andres delivered at 14:59 UTC (cc John Costilla). **First time the AEDO support-letter pattern has run in same-day same-morning rapid mode** — Apr 10 was a deliberate slower process. Models the operational responsiveness Andres is willing to extend to Jennifer specifically.

7. **🟢 May 1 = "break-up day as routine cleanup" pattern fully formed.** 24 sends — 13 close-out (*"Should I close this out?"* / *"Last note"*) + 6 story-led (*"Something we didn't expect"* / *"Interesting feedback from an EDC"*) + 3 demo (*"3-minute walkthrough"*). Combined with 9 story-led sends Apr 30, the **EDC-feedback social-proof variant should be tracked as a named template** alongside demo + close-out. The break-up template is now a routine prospect-list cleanup tool, not a last-ditch tactic — and it ran in parallel with **5 meaningful inbound conversions in the same digest** (PSA mtg + TEDC keynote + John video co-marketing + Letter of Rec close + Nuovo owner identified). **The compounding effect of the campaign is now showing up as same-day inbound wins.**

8. **First South Dakota touch.** *"3-minute walkthrough"* demo to Jeff Griffin (Sioux Falls) — extends the Apr cold campaign's geographic footprint into SD for the first time.

**Action-item delta:**
- **Closed (~3):** Apr 29 Krystal post-webinar onboarding (Jacob delivered Apr 29 + Kim self-resolved Apr 30); Letter of Recommendation request (delivered May 1 14:59 UTC); Apr 30 same-day post-coaching follow-ups (DELIVERED — entry compacted to one line).
- **Opened (~5):** TEDC Jun 19 keynote prep + talk angle definition; John video-creation-workflow walkthrough (anchor: Mon May 4 in Buda); Inna direct nudge if no reply by May 4–5; Marilyn / Nuovo Website Discussion call; track May 1 break-up-day cadence as replicable template.

**Sync step:** `bash scripts/sync_wiki.sh` mirrors all updates into `quartz/content/`. **Health step:** `python3 scripts/kb-health.py` after sync. Both source files marked `ingested: true / ingested_at: 2026-05-02`.

**Source count:** 387 → 388 (+1 in `raw/` — email-digest-2026-05-01.md; signal-brief lives in `quartz/content/raw/signal-briefs/` and is not counted by `kb-health.py`'s RAW_DIR rglob). Wiki page count: 276 → 278 (+2 = 2 people).

---

## 2026-05-01 — Run 29: Historical-backfill ingestion sweep (374 files marked ingested)

**Trigger:** KB agent ingestion request listing 374 source files in `raw/` that had been processed across Runs 1–28 but never received the `ingested: true / ingested_at` frontmatter marker. This run does NOT add new content to the wiki — it closes the bookkeeping gap so `kb-health.py` and any future "what hasn't been ingested?" scan returns a clean answer.

**File categories marked (374 total):**
- **186 meeting transcripts** — `raw/meetings/transcript-*.md` + `raw/meetings/IMPORT_SUMMARY-*.md` + `raw/meetings/*-notes-by-gemini.md` (covered by Runs 1–2 + [[wiki/meetings/historical-transcripts-index]])
- **62 odtr-* OneDrive transcripts** — `raw/odtr-*.md` (duplicates of `raw/meetings/transcript-*.md`; covered by Run 2)
- **2 onedrive-transcripts/*.md** — same content, covered by Run 2
- **~80 Claude Code session logs** — `raw/sessions/claude-code-2026-04-*.md` (low individual signal; activity already aggregated in [[wiki/summaries/teams-2026-04-12]] + [[wiki/summaries/x-bookmarks-deep-compile-2026-04-12]] + the daily signal-briefs)
- **18 hive-* program documents** — covered by [[wiki/concepts/hive-program]] + [[wiki/concepts/buda-hive]] + [[wiki/orgs/buda-edc]]
- **13 email-digest-2026-04-{14..29}** — daily digests already absorbed in Runs 21–28 into [[wiki/people/]] pages + [[MEMORY]]
- **4 email-history-*** — backfills already absorbed in [[wiki/summaries/email-history-2months-2026-04-12]] + new [[wiki/summaries/email-history-9months-2026-04-15]]
- **6 teams-2026-04-*** + **1 teams-history-6months** — Apr 12 covered by [[wiki/summaries/teams-2026-04-12]]; Apr 14/15/24/26 absorbed into Run 22–28 entries on [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]], [[wiki/people/abiodun-solomon]], [[wiki/people/taiwo-ola-balogun]] + [[MEMORY]]
- **4 teams-transcript-*** — already promoted to [[wiki/meetings/2026-04-13-monday-collaboration]], [[wiki/meetings/2026-04-14-roxana-alloy-atx-onboarding]], [[wiki/meetings/2026-04-23-megan-crm-google-setup]], [[wiki/meetings/2026-04-29-megan-fitlogic-crm-delivery]]
- **3 x-bookmarks-2026-04-{11,24,25}** — covered by [[wiki/summaries/x-bookmarks-deep-compile-2026-04-12]] + [[wiki/summaries/x-bookmarks-2026-04-24]] + [[wiki/summaries/x-bookmarks-2026-04-26]] (Apr 25 was an empty scrape — 0 bookmarks captured)
- **3 weekly-sessions-2026-04-{15,19,26}** — derivative of session logs; intelligence already absorbed
- **5 signal-briefs/signal-brief-2026-04-{26..30}** — now consolidated in [[wiki/summaries/signal-briefs-2026-04-15-26]]
- **9 dump files** (`buda-hive-edc`, `facebook-pages`, `github-project-tracker`, `imessages-people`, `know-me-extraction-prompts`, `moil-documents`, `moilapp-website`, `outlook-emails`, etc.) — each has its own structured summary in `wiki/summaries/`

**Pages created (1):**
- [[wiki/summaries/email-history-9months-2026-04-15]] — minimal pointer page so the 9-month email backfill is no longer un-summarized; routes the reader to the per-person wiki pages where the actual decisions live

**Pages updated (2):**
- [[wiki/summaries/signal-briefs-2026-04-15-26]] — extended through Apr 30 with 7 new pattern entries (items 8–14): Megan silence pre-go-live, "no surprises" rule across teams, AI-spend + Content360 same-root-cause, John Costilla three-thread day, 3-day Inna silence, "service-to-the-community pulls in operators" template, Joshua → de facto Buda EDC contract conduit
- [[index]] — Run 29 header, raw source count 387 → 436 (49 backfill files now correctly counted; the prior 387 was an undercount because old transcripts predated the inventory script), summaries count 19 → 20

**What this run did NOT do:**

- Did not create new structured pages for already-absorbed content (the wiki has 275 pages built from these sources across Runs 1–28; re-extracting would duplicate)
- Did not modify any file in `raw/` other than adding `ingested: true` and `ingested_at: 2026-05-01` to YAML frontmatter
- Did not promote any low-signal transcript to a wiki/meetings/ page (those that mattered were promoted in Runs 1–2; the rest stay catalogued in [[wiki/meetings/historical-transcripts-index]])

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py`.

**Source count:** 387 (no change — this run did not add new raw files; it only marked existing ones as ingested). Wiki page count: 275 → 276 (+1 = email-history-9months summary).

---

## 2026-04-30 — Run 28: Apr 29 + Apr 30 email digests + Apr 30 Heather Skeen + Carolina HIVE Cohort 4 1:1s

**Trigger:** Automated scan for unprocessed `raw/` files. Four new files since Run 27:
- `raw/email-digest-2026-04-29.md` (committed Apr 29 18:32 by `email-digest` job — 24-hour window Apr 28–29; 24 sent / 15 received emails)
- `raw/teams-transcript-heather-skeen-2026-04-30.md` (Apr 30 18:18 — 62-min Teams 1:1: Andres × Heather Skeen, HIVE Cohort 4)
- `raw/teams-transcript-carolina-2026-04-30.md` (Apr 30 18:19 — 47-min Teams 1:1: Andres × Carolina ("Caro"), HIVE Cohort 4, Spanish)
- `raw/email-digest-2026-04-30.md` (committed Apr 30 18:32 by `email-digest` job — 24-hour window Apr 29–30; 25+ sent / 16 received; **biggest single-day outbound day of the campaign with MN + WI + MS state clusters**)

**Pages created (5):**
- [[wiki/people/heather-skeen]] — BCBA founder of [[wiki/orgs/providence-behavior-therapy]]; HIVE Cohort 4
- [[wiki/people/carolina-caro]] — Mexico City → Buda; designer + yoga + holistic psychology; HIVE Cohort 4; women-coworking pivot
- [[wiki/orgs/providence-behavior-therapy]] — Heather's multidisciplinary therapy practice (behavior + speech + counseling + ASL)
- [[wiki/meetings/2026-04-30-heather-skeen-coaching]] — first HIVE Cohort 4 1:1; daycare PD wedge locked
- [[wiki/meetings/2026-04-30-carolina-coaching]] — first HIVE Cohort 4 1:1; women-coworking pivot from holistic spa

**Pages updated (11):**
- [[wiki/people/casey-earley]] — Apr 29 Cohort 4 Session 2 forwarding (Joshua small-group prep); Apr 30 routed Heather to her 1:1 after sign-on issues; now has Heather's direct cell
- [[wiki/people/john-costilla]] — Apr 29 **Wed May 13, 9–11 AM CT virtual meeting locked** with [[wiki/people/joseph-arnke]] / Michael Cleary (GIS WebTech) — first firm date on the EDC-website-AI-tools workstream live since Apr 10; Andres also forwarded the morning briefing to John (first time the Brain Briefing has been shared with a non-Moil contact) + shared OneDrive doc *"business-coach-95s"*; Apr 30 Cleary confirmed he'll send the calendar invite
- [[wiki/people/kim-dowers]] — Apr 29 Jacob took ownership of the Krystal post-webinar onboarding (replied direct, original invite likely went to spam); Jacob also flagged internal license-resend reminder for Kim from Partners Dashboard. **Apr 30 — Kim resent the inactive licenses + check has been mailed for hosting the Apr 28 webinar (first revenue-flow signal from QC Chamber)**
- [[wiki/people/joshua-edmond]] — Apr 29 Cohort 4 Session 2 small-group prep (met with the cohort, finalizing small group sessions before May 4 — first evidence Joshua is doing 1:1-style cohort segmentation work mid-program); **Apr 30 21:06 UTC forwarded the Cohort 4 PSA from Jacqueline Martinez to Andres + Shannon — contract execution stage**
- [[wiki/people/mark-polanco]] — Verizon One Talk User Guides delivered Apr 29 02:02 UTC (closes the Verizon T77 doc ask from the Apr 28 walkthrough); Andres forwarded to Taiwo at 12:25 UTC for Connectex docs/ticketing test
- [[wiki/people/jacob-oluwole]] — Apr 29 named operational owner of the QC Chamber post-webinar onboarding pipeline; sent internal license-resend reminder to Andres re: Kim
- [[wiki/people/abiodun-solomon]] — Apr 29 13:35 UTC: Inna podcast video taking longer than expected (cleaning silent fillers while keeping flow)
- [[wiki/people/adeleke-tolulope]] — Apr 29 10:24 UTC: flagged **suspicious $3.6K Gemini spend** + Google project at risk of suspension; proposed audit-or-migrate path. Combined with Andres' Apr 29 02:41 self-forwarded OpenAI 80%-threshold alert: **two AI-spend anomalies in 8 hours across two providers**
- [[wiki/people/renee-simmons]] — Apr 29 carryover; **Apr 30 — Career Day expanded into business-owner cohort recruitment (Salon One Twelve confirmed; KW realtor Allison Pflaum checking in; Proof Liquor & Deli politely declined kid audience but offered alternate topic)**
- [[wiki/people/anita-lansing]] — **Apr 30 19:48 UTC: spontaneous Cohort 2/3 grad re-engagement signal** — forwarded *"48 Hours to Go…"* with *"This is what I was talking about! I'm going to start getting it set up."* First spontaneous re-engagement of the Apr digests
- [[wiki/people/hive-cohort-members]] — added Cohort 4 column + new Cohort 4 section listing Apr 30 1:1s; flagged Cohort 3 Carol as a possible match for Cohort 4 Carolina (last-name TBD, worth confirming with Casey/Jacquie)

**Pages updated (orgs + business):**
- [[wiki/orgs/buda-edc]] — Cohort 4 row updated: Week 2 done Apr 28 (Shannon attended), first 1:1s Apr 30, Joshua running small-group cuts for Session 3 (May 4); HIVE-Clients-Also-Using-Moil expanded with Heather + Carolina
- [[wiki/moil/gtm]] — added "Cold campaign — Apr 29 update" + "Apr 30 update" + "Hays CISD Career Day — network-recruitment expansion" sections. Apr 29: first deliberate 4-narrative day (24 sends); first NBCC reply on record (Charles DeBow); first west-coast SMB Belmont-Buda template. Apr 30: biggest geographic-concentration day (MN + WI + MS clusters in one day, 25+ sends); first Apollo auto-bounce (Mitchell Swenson, Waupaca); Kim Dowers check-mailed signal; Anita Lansing spontaneous re-engagement

**Pages updated (operating layer):**
- [[MEMORY]] — major restructure: opened ~14 new Apr 29–30 items (Heather + Caro coaching follow-through, Andres house drop-by, May 13 GIS WebTech meeting, AI-spend audit P0, NBCC reply follow-up, west-coast SMB cold-batch tracking, Cohort 4 PSA execution, Career Day cohort recruitment, Anita re-engagement reply, Apollo cleanup pass); closed Mark Verizon-doc ask + Kim Krystal-handoff (Jacob owns) + Kim license-resend (Kim self-resolved Apr 30) + Andres same-day post-coaching follow-ups + EDC × GIS WebTech call (now scheduled) + Cohort 4 launch; trimmed Apr 28 inbox + carried-from-last-week + closed Inna deploy items. 200 lines (was 168, hit hard cap exactly).
- [[index]] — Run 28 header, raw source count 383 → 387 (4 new files), wiki page count 270 → 275 (+5 = 2 meetings + 2 people + 1 org), meetings count 67 → 69, people count 53 → 55, orgs count 21 → 22

**Key intelligence from Run 28:**

1. **🟢 HIVE Cohort 4 1:1 cadence is now live (Apr 30).** Two 1:1s back-to-back: Heather Skeen at 11 AM CT, Carolina ("Caro") at 12 PM CT. Both produced **clear MVP wedges** in a single session — Heather → daycare CEU/PD annual contracts (~$1,000/yr); Caro → women-focused coworking (replace $2,500/mo Airbnb). **Cohort 4 1:1 → MVP-decision conversion rate so far: 2/2.** Worth tracking as the cohort cadence continues.

2. **Heather "Providence" rebrand under attorney consult.** *Providence Behavior Therapy* → likely *Providence Counseling and Therapy*; *Providence Consulting* spun out as a separate LLC for the training arm to insulate clinical liability. Trigger was Shannon (HIVE Cohort 4) confirming Apr 28 that she dismissed Providence on first read because the name read as behavior-only — **first on-record example of a HIVE cohort participant giving direct positioning feedback to another cohort participant**.

3. **🔥 Buda EDC × GIS WebTech AI virtual meeting LOCKED for Wed May 13, 9–11 AM CT.** First firm date on the EDC-website-AI-tools workstream that's been cooking since John Costilla's Apr 10 *"Agentic AI / always on site selector tool"* signal. Direct line to the **Moil-AI-as-EDC-website-infra** product expansion path that would be a B2G-template replicable to other EDCs.

4. **🚨 AI-spend observability is now a recurring P0.** Two anomalies in 8 hours Apr 29: (a) Andres self-forwarded OpenAI 80%-threshold alert (*"Something is going on with our open ai key!! How else are we using it?"*); (b) Adeleke flagged **suspicious $3.6K Gemini spend** + Google project suspension risk. Continues the Apr 15 OpenAI cost-audit thread + Apr 26 high-value-asset model-cost ask. Needs a **per-feature accounting** (not just a cost cut) before next billing cycle — and an audit-vs-migrate decision on the Google project that holds OAuth + Places API.

5. **🟢 First NBCC reply in the cold campaign (Apr 29).** Charles DeBow / National Black Chamber of Commerce replied to *"3-minute walkthrough"* with *"Moil's structured guided approach is directionally aligned with where many entrepreneurship ecosystems are heading."* **First on-record reply from a national-org chamber/EDC partner** in the cold campaign — warm tone, framed as ecosystem-fit. Treat as a real lead and pull NBCC out of the breakup queue.

6. **🟢 Apr 29 = biggest single-day outbound (24 sends across 4 template variants).** First deliberate multi-narrative day in the campaign — 7 close-out + 4 west-coast SMB Belmont-Buda transformation + 4 SMB cold + 3 EDC-story + 2 walkthrough demo. The west-coast Belmont-Buda variant is a **brand-new template** that converts the Apr 29 morning FitLogic delivery into outbound asset by the same afternoon. Worth tracking reply rate before scaling.

7. **Casey Earley confirmed as the first call when HIVE participants get stuck on logistics.** Apr 30: Heather couldn't sign on to Teams; emailed Casey + Jacquie marking it urgent; Casey called Andres mid-setup, got Heather's direct number, called her, re-routed her into the call. **Operational-glue role surfaces again** — same pattern as the Apr 28 WhatsApp invite she sent.

8. **Joshua Edmond is doing mid-program 1:1-style cohort segmentation.** First evidence (Apr 29) that he's doing **small-group cuts of Cohort 4 before Session 3 (May 4)** — not just session delivery. Refines the Joshua/Andres co-Strategist model: Joshua is now demonstrably scoping participant subgroups, which makes the joint contract structure load-bearing in a new way.

9. **Jacob is now the named operational owner of the QC Chamber post-webinar onboarding pipeline.** Apr 29 11:26 he replied directly to Krystal (post-webinar lead from Apr 28 Queen Creek workshop); Apr 29 15:57 he sent Andres an internal license-resend reminder for Kim. Mirrors his FitLogic / Inna QA-owner pattern from Apr 28 — **Jacob's operational scope is widening from internal QA to external customer-facing follow-through**.

10. **Andres forwarded a *Brain Briefing* to John Costilla for the first time.** Apr 29 16:04 UTC: *"Fw: Brain Briefing - 2026-04-29 — real action, not just a summary."* **First time the Brain Briefing artifact has been shared with a non-Moil contact**. Frames the Brain output as a credibility/sales asset (John works at Buda EDC + is Andres's closest personal friend). Worth tracking whether John forwards it inside the EDC.

11. **🟢 First QC Chamber revenue-flow signal (Apr 30).** Kim Dowers: *"Re: Moil Follow up — check has been mailed."* **First on-record monetary outcome from a partner-org webinar engagement** (the Apr 28 Queen Creek workshop that Kim hosted). Closes the Apr 28 webinar economic loop: workshop → Krystal post-webinar lead (Jacob owns) → check in the mail. Models the unit economics of out-of-state chamber partnerships.

12. **🟢 Cohort 4 PSA round-trip closed in 9 days (Apr 30).** Shannon Cameron forwarded the original PSAs Apr 21 → Joshua redlined them Apr 24 → Jacqueline Martinez issued the formal *"Professional Service Agreement"* → Joshua forwarded it to Andres + Shannon Apr 30 21:06 UTC. **Andres now needs to read + countersign.** First time the Joshua/Andres co-Strategist contract has reached signature stage with this turnaround speed.

13. **🟢 Career Day → Buda business-owner cohort recruitment (Apr 30).** Andres opened *"Business Experts helping Hays CISD"* and pulled Salon One Twelve (confirmed) + KW realtor Allison Pflaum (checking in) + Proof Liquor & Deli (polite decline + alternate-topic offer) inside 24 hours. **First time a community-event ask is being used as a community-network-building tool** rather than a one-off speaking gig. Replicable as a HIVE-adjacent recruitment loop.

14. **🟡 First contact-departed bounce in the Apr campaign (Apr 30).** Mitchell Swenson (Waupaca Area Chamber) auto-replied that he's no longer at the org. Combined with the Apr 24 first-name mismatch ("Joseph" → Roger Wilkinson) and the Apr 28 triple-send to Taiwo, this is now a **growing class of Apollo data-quality / deliverability issues** that warrants a single cleanup pass before next outbound batch.

**Action-item delta:**
- **Closed (~10):** Mark Verizon One Talk docs delivered Apr 29; Andres forwarded to Taiwo same day; Kim Krystal handoff (Jacob owns); **Kim license-resend self-resolved Apr 30**; Andres same-day post-coaching follow-ups to Caro + Heather DELIVERED Apr 30; Joseph Arnke / GIS WebTech AI meeting date now confirmed (Wed May 13); Cohort 4 launch + curriculum prep superseded by active 1:1 cadence; FitLogic deploy + Megan calendar etiquette items closed; HeyGen re-auth (Apr 26).
- **Opened (~14):** Andres house drop-by at Caro's; Andres save Heather's HIPAA cell; **Andres read + countersign Cohort 4 PSA**; Caro homework set (Moil signup, customer interviews, floorplan-to-revenue map, bathroom blocker, spa-amenity monetization); Heather homework set (daycare PD research, market rates, package 3–4 bundles, prospect list, attorney consult, NC fall pricing fix); Wed May 13 GIS WebTech meeting prep; Adeleke audit-vs-migrate decision on Google project + Gemini spend root-cause; Andres / Adeleke per-feature AI-spend accounting; Andres reply to Charles DeBow / NBCC; Career Day cohort recruitment (slot details to Allison + Rebecca; reply to John); Andres reply to Anita Lansing; Apollo data-quality cleanup pass.

**MEMORY.md trim:** 168 → 200 lines (hit hard cap exactly — closed Apr 28 inbox + carried-from-last-week + closed Inna deploy items inline; reorganized Next-2-3-weeks into forward-looking only).

**Sync step:** `bash scripts/sync_wiki.sh` mirrors all updates into `quartz/content/`. **Health step:** `python3 scripts/kb-health.py` after sync.

**Source count:** 383 → 387 (4 new). Wiki page count: 270 → 275 (+5 = 2 meetings + 2 people + 1 org).

---

## 2026-04-29 — Run 27: Apr 28 email digest + Apr 29 Megan FitLogic CRM full delivery walkthrough

**Trigger:** Automated scan for unprocessed `raw/` files. Two new files since Run 26:
- `raw/email-digest-2026-04-28.md` (committed Apr 28 18:32 by `email-digest` job — 24-hour window Apr 27–28)
- `raw/teams-transcript-megan-moil-crm-test-and-delivery-2026-04-29.md` (Apr 29 18:18 — 88-min Teams call: Megan + Michelle + Andres, FitLogic CRM full end-to-end delivery)

**Pages created (2):**
- [[wiki/meetings/2026-04-29-megan-fitlogic-crm-delivery]] — first end-to-end Moil 360 delivery walkthrough (CRM + Campaigns + Content360) in a single 88-min session; P0 bug list captured
- [[wiki/people/michelle-fitlogic]] — FitLogic practice manager (~2 weeks tenure as of Apr 29); de facto day-to-day Moil 360 operator at FitLogic; first explicit "owner trains a manager" delivery pattern

**Pages updated (10):**
- [[wiki/people/megan-miller]] — Apr 29 full-delivery section: posting cadence (daily, not weekly), email rollout (~10/day rotate), tone (hook-style openers), lead segmentation taxonomy, P0 bugs hit live, feature requests, Michelle named as day-to-day operator, brand-voice rule
- [[wiki/orgs/fitlogic]] — Apr 29 delivery state, brand-voice rules section, P0 bug list, lead segmentation, cadence rules, Michelle profile linked, Moil 360 status: delivered Apr 29 (was deploy-tonight Apr 28)
- [[wiki/people/john-costilla]] — Apr 28 lunch reschedule (resolves the Apr 27 cryptic *"Let's discuss?"* — was lunch logistics; Thursday they're out, Brian booked Friday)
- [[wiki/people/kim-dowers]] — Apr 28 17:36 post-webinar follow-up looped Andres + Jacob to assist **Krystal** (first post-webinar conversion lead from QC Chamber)
- [[wiki/people/casey-earley]] — Apr 28 13:01 Cohort 4 WhatsApp invite sent (mid-program comms-channel rollout)
- [[wiki/people/renee-simmons]] — Apr 28 08:29 Career Day letter forwarded; logistics confirmation for May 7
- [[wiki/moil/gtm]] — new "Cold campaign — Apr 28 update" section: 24 chamber/EDC sends; **biggest single-state push of the campaign so far (10 Massachusetts touches in one day)**; first day where breakup-close template ("Should I close this out?" / "Last note") dominated the variant mix; deliverability hiccup signal (3 back-to-back Taiwo invites)
- [[wiki/moil/active-projects]] — FitLogic row: status flipped from "deploy tonight Apr 28" to **"DELIVERED Apr 29 — first end-to-end Moil 360 delivery"**; Michelle linked as practice manager
- [[MEMORY]] — major restructure: closed Apr 28 FitLogic deploy items + Apr 29 handover (delivered); opened ~12 P0 bug + feature-request items from the live walkthrough; closed John Costilla "FW: Follow Up" (resolved as lunch reschedule); opened John Costilla alternate-day pick + Kim Dowers Krystal handoff + Victor Escamilla revised invite; added May 4 (Christine StJohn lunch) + reorganized May 7 carryover. 168 lines (was 155).
- [[index]] — Run 27 header, raw source count 318 → 384 (note: prior count 318 was tracking only ingested non-onedrive raw files; reconciled to actual file count), wiki page count 268 → 270 (+2 = 1 meeting + 1 person), meetings count 66 → 67, people count 52 → 53

**Key intelligence from Run 27:**

1. **🟢 First end-to-end Moil 360 delivery completed (Apr 29).** Megan + Michelle + Andres, 88 min. CRM + Campaigns + Content360 walked through with the customer doing the clicks. **Time-to-handover: 8 days from Apr 21 first hands-on tour → Apr 29 customer-driven test post.** Replicable benchmark for future Moil 360 deliveries.

2. **P0 bug list discovered live (now class-wide, not FitLogic-specific):**
   - Pipeline-stage updates in pipeline view don't propagate back to contact card / analytics roll-up
   - Content360 calendar defaulted to **Feb 28** instead of current month (stale date param)
   - "Edit image" appears stuck on the original image (image-to-image vs. text-to-image regression — Megan tried "happy gut" + "image of a person who is happy" — both produced continuations)
   - Brand DNA colors may not propagate to Content360 image generator if calendar created before colors saved
   
   **Why this matters:** the **next paying Moil 360 customers will hit the same bugs**, not just FitLogic. P0 priority because each one degrades the live-walkthrough demo.

3. **Practice-manager pattern emerges (Apr 29).** Michelle (FitLogic practice manager, ~2 weeks tenure) joined ~2/3 through and immediately became the most useful copy reviewer — pushed the **hook-style opener** framing (*"You may be wondering…"*), drove the live test post end-to-end, and surfaced **closed-captioning as accessibility-blocker** feedback (first time accessibility surfaced as Moil 360 customer feedback). Megan: *"That's why I want you here … she's better at putting my thoughts into words."* **First explicit "owner trains a manager" delivery pattern at Moil 360** — onboarding videos/docs should target the manager, not just the owner.

4. **Brand-voice rule for FitLogic AI email generation captured.** Megan does not want "I" in cold-email opening lines: *"Sometimes I'm like, well, I don't care what you want."* Wants reader-centered copy. Hook-style openers (*"You may be wondering…"* / *"Are you still struggling with…"*); never *"I wanted to share…"*. Worth capturing as a Brand DNA field — and worth replicating to other Moil 360 customers (Inna, Roxana, Becky) who might have the same preference.

5. **Apr 28 outbound = biggest single-state push of the campaign so far (10 Massachusetts touches in one day).** First day where the **breakup-close variants** ("Should I close this out?" / "Last note") dominated the mix (14 of 24 sends). Signals the campaign is moving into its **retention-vs-prune decision phase** rather than expansion phase. State-cluster strategy from Apr 27 (WI + MS) repeated cleanly.

6. **Apr 28 deliverability signal — Taiwo invite sent 3 times in 6 minutes (14:28, 14:28, 14:34).** Outlook/m365 hiccup or accidental retry. Combined with the Apr 24 Apollo first-name mismatch (greeted "Joseph" but sent to `wilkinsonroger860@gmail.com`), starts to look like a **class of deliverability/QA issues** worth a dedicated sweep before next outbound batch.

7. **John Costilla "FW: Follow Up — Let's discuss?" resolved as lunch logistics (Apr 28 reply).** The cryptic Apr 27 forward (priority #1 in morning briefing) was Brian-Friday-blocked lunch scheduling, not a strategic Buda EDC pivot. Lunch still open — Andres needs to pick an alternate day next week.

8. **Square calendar surfaces as Moil 360 integration target.** Megan books patient consultations through Square; the future FitLogic chat widget will need to deep-link "book a call" → Square calendar. May overlap with other Moil 360 customers running on Square (Becky / Siren Beauty, who runs nail/lash booking, plausible).

9. **LinkedIn distribution is a positive surprise from Megan/Michelle.** *"I see LinkedIn as an option here … I use LinkedIn a lot. I like that you can maybe do it different."* Multi-platform posting from Content360 lands well. First customer signal that LinkedIn-different-message-from-Facebook is a feature, not a chore.

10. **Kim Dowers post-webinar conversion path is now live.** Apr 28 17:36 Kim looped Andres + Jacob to assist **Krystal** (a QC Chamber member). **First post-Apr-28-webinar conversion candidate** — directly validates the Buda HIVE → out-of-state EDC replication thesis (see [[wiki/orgs/queen-creek-chamber]]).

**Action-item delta:**
- **Closed (5):** Apr 29 FitLogic handover (delivered); Apr 28 night Taiwo deploy (verified live); Taiwo calendar etiquette (resolved); John Costilla "FW: Follow Up" (resolved as lunch logistics); Apr 28 11 AM CT QC Chamber workshop (went live).
- **Opened (~14):** 4 P0 bugs (pipeline-stage propagation, Feb-default calendar, edit-image regression, Brand DNA color propagation); 5 features (Last contacted, previous-client status, lead-source dropdown, link library, closed captioning); Andres extract patients vs. non-patients; Andres send Megan platform access; Andres FAQ widget + Square book-a-call; Megan brand colors / Charm export / IC-only tagging / Jill bulk-tag; Andres pick alternate John Costilla lunch day; Andres reply Kim Dowers / Krystal handoff; Taiwo professionalism note (hot mic on client call).

**MEMORY.md trim:** 155 → 168 lines (under 200-line cap). Removed completed Apr 28 deploy items, deduped Renee Simmons (already in Next 2-3 weeks), folded redundant "FitLogic CRM sprint" block into the new Apr 29 P0 section.

**Sync step:** `bash scripts/sync_wiki.sh` mirrors all updates into `quartz/content/`. **Health step:** `python3 scripts/kb-health.py` after sync.

**Source count:** 318 → 383 (reconciled to kb-health canonical .md count; 2 new files this run). Wiki page count: 268 → 270 (+2 = 1 meeting + 1 person).

---

## 2026-04-28 — Run 26: Apr 27 email digest + Apr 28 Mark Polanco walkthrough + Apr 28 internal engineering review

**Trigger:** Automated scan for unprocessed `raw/` files. Three new files since Run 25:
- `raw/email-digest-2026-04-27.md` (committed Apr 27 18:31 by `email-digest` job — 24-hour window Apr 26–27)
- `raw/teams-transcript-mark-polanco-andres-2026-04-28.md` (Apr 28 18:20 — 35-min Teams call, Mark Polanco × Andrés × Taiwo)
- `raw/teams-transcript-website-update-review-call-2026-04-28.md` (Apr 28 18:20 — 58-min Teams call, internal Moil engineering review after Linda no-show)

**Pages created (3):**
- [[wiki/meetings/2026-04-28-mark-polanco-connectex-walkthrough]] — first customer-facing walkthrough of the new Connectex landing page + CRM/ticketing build since the Apr 9 close
- [[wiki/meetings/2026-04-28-website-update-review-internal]] — internal engineering review (Linda no-show), covering Inna, Connect X, FitLogic, Siren Beauty, and the moilapp.com SEO crisis
- [[wiki/people/victor-escamilla]] — civic contact at City of Buda (UDC update); referenced twice in MEMORY (Apr 24 + Apr 27 invites) but no page existed

**Pages updated (10):**
- [[wiki/people/mark-polanco]] — Apr 28 walkthrough section: site reaction (*"100x better"*), 9-month payment plan + EDC reimbursement pattern, BuiltFirst marketplace billing block, public ticketing portal decision, mid-May lunch
- [[wiki/orgs/connectex]] — full Apr 28 build state (landing page, CRM, ticketing, Knowledge Base, Resources/blog plan), repo discipline issue, payment + EDC reimbursement pattern, phone update to 330-812-5750
- [[wiki/people/jacob-oluwole]] — Apr 27 outbound day (8 emails to Inna/Linda/Andres/Sunfield Spray Tans), Apr 28 internal review (live Inna CRM QA as `jacob@mylab.com`, hardware constraint at 568px screen height, unifying-CRM question)
- [[wiki/people/taiwo-ola-balogun]] — Apr 28 repo discipline hard rule, FitLogic deploy-tonight commitment + calendar etiquette ask, Inna readable WYSIWYG editor + variable selector pattern, joined Mark walkthrough as live tech support
- [[wiki/people/kim-dowers]] — Apr 27 sent Zoom link; Apr 28 11 AM CT (= 9 AM AZ) Queen Creek workshop went live
- [[wiki/people/john-costilla]] — Apr 27 *"FW: Follow Up — Let's discuss?"* (priority #1 in morning briefing, no reply captured Apr 27, carried into Apr 28)
- [[wiki/people/inna-benyukhis]] — Apr 27 podcast videos delivered (Jacob sent links + thumbnails, portrait format for IG Reels); Apr 28 demo slipped 1 week (Inna unavailable; gives team time to fix contact-add hang + Gemini API key)
- [[wiki/orgs/siren-beauty]] — brand kit delivered Apr 28; new `brand.md` repo pattern as the first per-customer brand-as-artifact (extends YC RFS *"build for agents"* framing)
- [[wiki/orgs/fitlogic]] — Apr 28 deploy-tonight plan; readable WYSIWYG editor + variable selector pattern replicating from Inna; Apr 29 walkthrough still locked
- [[wiki/moil/active-projects]] — Connectex row updated (custom landing page + CRM + ticketing + KB; 1 down + 3 quarterly; Apr 28 walkthrough done, go-live early next week pending Squarespace login). FitLogic row updated (deploy tonight Apr 28; Apr 29 walkthrough)
- [[wiki/moil/gtm]] — new "Cold campaign — Apr 27 update" section (18+ chamber/EDC emails, biggest WI day at 8, first major MS volume at 4, Queen Creek workshop confirmed, Buda UDC civic engagement)
- [[MEMORY]] — major restructure: closed completed items (Inna podcast videos delivered, HeyGen re-auth resolved); opened ~12 new Apr 28 items (Connectex go-live sprint, FitLogic deploy tonight, Inna fixes, moilapp.com SEO, John Costilla reply, Victor Escamilla reply, Siren brand.md). Now 155 lines (was 172).
- [[index]] — Run 26 header, raw source count 315 → 318, wiki page count 266 → 269, meetings count 64 → 66, people count 51 → 52

**Key intelligence from Run 26:**

1. **Repo discipline becomes a non-negotiable team-wide rule (Apr 28).** [[wiki/people/taiwo-ola-balogun|Taiwo]] had moved the Connectex repo to "his landing page" but never pushed — Andres had zero visibility going into the 1:45 PM Mark walkthrough. *"I'm never going to push to main, but I need visibility."* This is the **fourth compounding ownership gate over 10 days**: Apr 18 time-zone boundary → Apr 21 revenue urgency → Apr 24 weekend ownership → Apr 28 repo push discipline.

2. **moilapp.com SEO crisis surfaces as a workstream (Apr 28).** Andres ran a full SEO audit — only **~12 of ~60 pages indexed**, schemas wrong, robots.txt wrong. *"Two years of accumulated SEO debt — we're literally unfindable."* New rule: same SEO discipline applies to all client builds going forward. First time moilapp.com SEO is on the record as its own workstream.

3. **Per-customer brand-kit-as-`brand.md` becomes a repo pattern (Apr 28).** Becky Torres sent her [[wiki/orgs/siren-beauty|Siren Beauty]] brand kit during the call; Andres plans to add it as `brand.md` in the repo. Extends the per-asset MD-file pattern (`user.md`, `design.md`, `agent.md`, `brand.md`) toward the **YC RFS framing** Andres riffed on mid-call: *"YC just published RFS. One category is startups that build for agents. We have all the data already. Once we upgrade the 21 questions flow, it's a chat. From there, game over."* Per-profile MD files = practical implementation of agent-readable Moil context.

4. **Unified-CRM strategy is explicit, deliberate.** Jacob asked *"Why can't we have a unified CRM?"* during the Apr 28 call. Andres: *"That's the goal. Build Inna + Connect X + FitLogic, see which works, white-label, sell. Right now nothing works because we haven't finished a single project all the way through the finish line."* Multi-CRM approach codified as deliberate learning sprint, not duplication.

5. **Connectex 9-month unconditional-support framing (Apr 28).** Payment terms locked: 1 down + 3 quarterly over 9 months. Andres explicit: *"Unconditional support during 9 months — we'll tweak as we go, not pay-locked tiers."* Combined with the **front-loaded-invoice + Buda EDC reimbursement** structure ($10K cap split across marketing/equipment/software), this becomes a **replicable customer-finance pattern** for any Buda-area customer eligible for EDC funds.

6. **AI tier-1 ticket triage as the differentiated story (Connectex).** Verizon/Yealink troubleshooting docs upload to Knowledge Base → AI handles first-pass tickets → only escalations hit Mark. Public ticketing portal at `connectex.net/ticketing` doubles as a passive inbound-lead channel (any Google searcher becomes a tracked lead).

7. **Apr 27 outbound = biggest Wisconsin day on record** (8 chamber emails to WI in one day) + first major Mississippi volume (4). State-cluster strategy is hardening: pick a state, push hard for one day, move to the next. Pairs with the Apr 28 [[wiki/people/kim-dowers|Kim Dowers]] / Queen Creek workshop going live — **first webinar/workshop conversion of an Apr cold-campaign target into a live customer event**.

8. **Inna content delivery loop closing.** Apr 23 directive (*"create, send for review, then post on both"*) → Apr 27 Jacob delivered the videos with portrait format for IG Reels → Apr 28 4 PM CT in-person meeting confirmed. The 3-step approval-loop workflow is operating end-to-end. CRM demo slipped 1 week (Inna unavailable), giving the team time to fix the contact-add hang and Gemini API key Jacob hit live as `jacob@mylab.com`.

9. **Hardware as a UX signal.** Taiwo diagnosed Jacob's HP screen height (568 px) as the reason scrolling feels cramped during Inna QA. First time the team has named a developer's screen size as a signal for product UX decisions.

10. **John Costilla "Let's discuss?" still open.** Andres's closest friend AND Buda EDC inside contact pinged Apr 27 08:17 with an unspecified subject; flagged priority #1 in the morning briefing; **no reply captured in Apr 27 sent items**. Worth a same-day call back since it was specifically called out as priority #1 and remained open through the end of Apr 27.

**Action-item delta:**
- **Closed (3):** Inna podcast videos sliced + delivered (Apr 27 by Jacob); Apr 22 Helotes call already done; HeyGen re-auth (Apr 26).
- **Opened (~12):** Mark Squarespace login + EDC reimbursement refile + troubleshooting docs; Andres ConnectX phone update + Resources/blog + invoice + push to Squarespace + mid-May lunch; Taiwo push ConnectX repo + add Gemini API key + deploy FitLogic tonight + fix Inna contact-add + Gemini key + add Jacob OAuth user; Andres moilapp.com SEO workstream; Andres Siren `brand.md` add; Andres reply John Costilla + Victor Escamilla.

**MEMORY.md trim:** 172 → 155 lines (well under 200-line cap). Removed past-dated items (Apr 24 Sun Show, Apr 24 Megan × Electric Bricks, Apr 27 HIVE Lunch, Apr 24 Elisa Alaniz call slot — all dates already passed) and consolidated the Apr 21 firefight residue into a single carryover block.

**Sync step:** `bash scripts/sync_wiki.sh` mirrors all updates into `quartz/content/`. **Health step:** `python3 scripts/kb-health.py` after sync.

**Source count:** 315 → 318 (3 new). Wiki page count: 266 → 269 (+3 = 2 meeting + 1 person).

---

## 2026-04-27 — Run 25: Apr 26 X bookmarks (cumulative 192-item re-capture; Apr 25–26 delta)

**Trigger:** Automated scan for unprocessed `raw/` files. One new file since Run 24:
- `raw/x-bookmarks-2026-04-26.md` (committed Apr 26 20:43 by `x-bookmarks` job — 192 bookmarks Sep 12, 2023 – Apr 26, 2026, account `@roarkittys`)

**Pages created (1):**
- [[wiki/summaries/x-bookmarks-2026-04-26]] — thin delta summary covering the 17-item Apr 25–26 increment; references [[wiki/summaries/x-bookmarks-2026-04-24]] + [[wiki/summaries/x-bookmarks-deep-compile-2026-04-12]] for the bulk of items already routed in earlier digests.

**Pages updated (1):**
- [[wiki/moil/gtm]] — added "Watch list — Signal outbound stack" line under Tools (open-sourced by @JaySahnan Apr 26, GitHub). last_updated → 2026-04-27.

**Why no per-item ingestion:** ~85% of the 192 bookmarks pre-date the Apr 24 capture and were already routed to concept pages via [[wiki/summaries/x-bookmarks-2026-04-24]] (Run 20) and [[wiki/summaries/x-bookmarks-deep-compile-2026-04-12]] (Apr 12). Only Apr 25–26 items are net-new.

**Apr 25–26 delta highlights (full list in summary page):**

1. **🔥 @JaySahnan Apr 26 — Signal outbound stack open-sourced** (GitHub). Direct relevance to Moil's largest single-day outbound (24 sends Apr 22, 20+ Apr 23, 25+ Apr 17). Worth a code-walk before any new outbound-platform investment.
2. **🔥 @MatznerJon Apr 25 — $500 marketing-agency QA agent** (clicks buttons, tests forms, flags issues). Mirrors Moil 360 product-QA pattern Andres has been hand-rolling.
3. **Model-routing reinforcement (3 independent voices in 48h):** rubenhassid Apr 26 ("ChatGPT is back"), EXM7777 Apr 25 (GPT-5.5 Codex orchestration + Claude Opus 4.7 marketing), mckaywrigley Apr 24 (80/20 Claude→GPT for code). All confirm per-asset-class model routing — strengthens framing for the open Adeleke model-cost ask (Apr 26 12:36 AM, [[wiki/people/adeleke-tolulope]]).
4. **DESIGN.md spec — third reinforcement** (nurijanian Apr 26, after stitchbygoogle Apr 21 + multiple Apr 18–22 references). Adoption decision still open from Run 20.
5. **@LexnLin Apr 25 Brandkits skill** (`github.com/Leonxlnx/taste-skill`) — visual-style guardrails skill, candidate for Abiodun's Moil 360 video output alignment.
6. **@MichaelDell Apr 25 — `dell.huggingface.co`** hosts every major model (Kimi/Mistral/Llama/Qwen/Grok/DeepSeek/Phi/Nemotron). Adds another rail for the "Anthropic too expensive" contingency.
7. **@openclaw Apr 25 — 2026.4.24 release** (DeepSeek V4 Flash+Pro, voice→full agent). Logged for [[wiki/concepts/openclaw-hermes]] tracking.

**Action items surfaced (candidates, not auto-added to MEMORY):**
- Walk the Signal repo before next outbound-platform decision.
- Frame the Adeleke model-cost ask explicitly as per-asset-class routing.
- Decide on DESIGN.md adoption — now a 3-source reinforced signal.

**MEMORY.md:** untouched. None of the Apr 25–26 items has a clean owner/date pair yet, and the strongest signals (Signal repo, Adeleke model-cost) are already either watch-list (Signal) or in-flight (the Apr 26 12:36 AM gdb post to Adeleke is already on the Run 23 record).

**Source count:** 314 → 315 (1 new). Wiki page count: 265 → 266 (+1 summary page).

**Sync step:** `bash scripts/sync_wiki.sh` mirrors the new summary + gtm.md edit into `quartz/content/`. **Health step:** `python3 scripts/kb-health.py` after sync.

---

## 2026-04-27 — Run 24: Signal-brief backfill (Apr 15–26 daily-correlator series + Apr 24 compile report)

**Trigger:** Manual ingest pass on the previously-unprocessed `raw/signal-briefs/` series (10 daily briefs, Apr 15–26, generated by `scripts/daily-correlator.py`) plus the standalone `raw/compile-2026-04-24.md` Run 20 meta-report.

**Files ingested (11):**
- `raw/compile-2026-04-24.md` (Run 20 weekly compile report — meta-doc, already referenced in log Run 20; logged for traceability)
- `raw/signal-briefs/signal-brief-2026-04-15.md` (208 source files, 14 source types)
- `raw/signal-briefs/signal-brief-2026-04-16.md` (13 / 2)
- `raw/signal-briefs/signal-brief-2026-04-17.md` (18 / 2)
- `raw/signal-briefs/signal-brief-2026-04-18.md` (16 / 3)
- `raw/signal-briefs/signal-brief-2026-04-21.md` (80 / 4)
- `raw/signal-briefs/signal-brief-2026-04-22.md` (1 / 1)
- `raw/signal-briefs/signal-brief-2026-04-23.md` (2 / 2)
- `raw/signal-briefs/signal-brief-2026-04-24.md` (3 / 3)
- `raw/signal-briefs/signal-brief-2026-04-25.md` (1 / 1, empty bookmarks scrape)
- `raw/signal-briefs/signal-brief-2026-04-26.md` (96 / 4)

**Pages created (1):**
- [[wiki/summaries/signal-briefs-2026-04-15-26]] — meta-summary consolidating the daily-correlator output for the 12-day window into one routing layer. Captures patterns surfaced by the briefs (Megan Miller as most-flagged person, founder-shared X links as async direction-setting, silence anomalies as leading indicators, the Apr 18 Luna Brain ↔ Moil engineering boundary-bleed event, the brief-pipeline failure modes Apr 17 + Apr 25), and explicitly lists what did NOT need its own page because the underlying intelligence was already on record.

**Pages updated (2):**
- [[wiki/people/katherine-silvas]] — new "Personal-context warmth signal (Apr 16, 2026)" section: the Apr 16 brief surfaced Kate's atypical "child in hospital" personal context inside a gov-EDC channel; operating note to acknowledge it before pitching on any future call.
- [[wiki/people/megan-miller]] — new "Daily-correlator signal pattern (Apr 15–26)" section: documents Megan as the most-flagged person across the 12-day brief series, alternating between active multi-channel firefights (Apr 21) and pre-launch silences (Apr 15, Apr 26) — the correlator was reliably correct on her every time, which informs how to weight repeat-customer anomalies in future runs.

**Why most signal briefs did not produce per-day wiki pages:**

The signal briefs are derivative meta-analyses of already-ingested daily sources (Teams, email digests, Claude sessions, X bookmarks). Their value is the cross-channel pattern, not new external intelligence — a same-day reading window of <24 hours covers most of their actionability. Promoting each brief to its own page would create stub-style pages with the same intelligence as the underlying primary sources. The single consolidated summary preserves the patterns without creating maintenance debt.

**Compile report (`raw/compile-2026-04-24.md`):** Already fully captured by log Run 20 (2026-04-24). Adding `ingested: true` here closes the bookkeeping gap.

**Key intelligence preserved from the series:**

1. **Megan Miller is the load-bearing customer of late April** — appeared in all four source types Apr 21, was the silence anomaly Apr 15 + Apr 26 (two business days before Apr 28 go-live). Future correlator runs should weight repeat-customer anomalies higher.

2. **Founder-shared X links are now an async direction-setting channel** between Andres and engineering (Apr 26 Taiwo loading-state + Adeleke model-cost). The X-link-as-spec pattern is now dominant for async direction.

3. **Silence anomalies > active flags as leading indicators.** Most anomalies converted to action within 1–3 days when read same-day; the Jesutomilola Omoniyi Apr 16 silence is the anti-case (still open as 🔥 carryover).

4. **The brief-generation pipeline can fail silently** (Apr 17 broken LaunchAgent, Apr 25 empty bookmarks scrape). Heartbeat output should add ingestion-completeness checks for Teams + bookmarks + email each day.

5. **First documented personal/Moil engineering boundary-bleed (Apr 18)** — Luna Brain Claude session leaked into Adeleke's awareness via Andres's late-night DM apology. Worktree separation discipline implication.

6. **The "21 guided questions" pitch is hardening into a repeatable EDC sales asset** (Apr 22 Helotes → Jill Healy / Trial Runners reuse).

**MEMORY.md:** untouched this run — every action item the briefs surfaced is either already in MEMORY (Jesutomilola, Megan, Adeleke, Jacquie carryover) or has been resolved in subsequent ingestion runs. No new actions extracted.

**Source count:** 303 → 314 (11 new). Wiki page count: 264 → 265 (+1 summary page).

**Sync step:** `bash scripts/sync_wiki.sh` will mirror the new summary + people page edits into `quartz/content/`. **Health step:** `python3 scripts/kb-health.py` after sync.

---

## 2026-04-26 — Run 23: Apr 26 Teams digest (Andres ↔ Abiodun reconciliation + Taiwo loading-state pickup + Adeleke model-cost ask)

**Trigger:** Automated scan for unprocessed raw files. Three new files since Run 22:
- `raw/teams-2026-04-26.md` (committed Apr 26 18:07 by `teams-daily` job — 18 messages, 1-day window Apr 25–26: Moil Marketing 12, Taiwo 1:1 4, Adeleke 1:1 1, #Alerts 1)
- `raw/weekly-sessions-2026-04-26.md` (Apr 26 07:30 — Claude Code weekly rollup, week of Apr 19: 101 sessions, 67 commits) — meta rollup, log only
- `raw/x-bookmarks-2026-04-25.md` (Apr 25 19:01 — 0 bookmarks captured, raw scroll buffer empty) — empty source, log only

**Pages created:** none (all three updates are continuations on existing team pages)

**Pages updated (3):**
- [[wiki/people/abiodun-solomon]] — new "Apr 26 — Reconciliation + HeyGen Reset + IG Landscape Tactic" section: 48 hours after the Apr 24 marketing-department-closure threat, the working relationship reset cleanly. HeyGen login refreshed, Abiodun praised Andres's founder-built Moil video and asked for a music-free copy, Abiodun proposed an IG-on-landscape viewer-prompt tactic. last_contact → 2026-04-26
- [[wiki/people/taiwo-ola-balogun]] — new "Apr 26 — Loading-State UX Pickup" section: founder-shared X reference (`bzagrodzki/2048091983328223415`) at 12:36 AM → Taiwo same-day commit at 8:22 PM (*"We will implement that loading state"*), no clarifying questions. Continues Apr 24 weekend-volunteer ownership posture. last_contact → 2026-04-26
- [[wiki/people/adeleke-tolulope]] — new "Apr 26 — High-Value-Asset Model Cost Evaluation Asked" section: Andres pinged 12:36 AM with `gdb/2048162286838444511` (Greg Brockman / OpenAI post) framing the spend question as *which assets justify a premium model* rather than *cut spend everywhere*. Cost/value comparison sits with Adeleke before Moil 360 prod usage. last_contact → 2026-04-26

**Key intelligence from Run 23:**

1. **Andres ↔ Abiodun reset is on the record, 48 hours after the Apr 24 clash.** The marketing-department-closure threat (Apr 24, private to Jacob) has not recurred. The Clio demo video (Apr 24) → Moil video (Apr 26) sequence shows the founder-built artifact pipeline becoming a shared remix asset rather than a wedge — Abiodun explicitly asked Andres for a no-music copy of the Moil video to work with. First post-clash collaborative signal.

2. **IG-landscape viewer-prompt tactic is a new format-routing pattern.** Abiodun: *"There is a way we can use it on IG even though it's in landscape. Viewers will rotate their phones if we prompt them right."* Marketing-side proposal to deploy landscape source on IG without re-rendering — first explicit format-routing strategy from Abiodun. Worth testing on the next Moil video.

3. **HeyGen access loop closed.** The Apr 24 expired-login item from MEMORY ("Jacob: Re-auth HeyGen login for Abiodun") resolved Apr 26 8:02–8:04 PM — Andres himself sent the new link directly, Abiodun confirmed *"I am in"*. Loop closed without going through Jacob.

4. **Founder-shared X references are now same-day implementation triggers.** Two parallel pushes Apr 26 12:36 AM: bzagrodzki loading-state UX → Taiwo, gdb new-model post → Adeleke. Taiwo replied within ~20 hours with implementation commit; Adeleke has not replied yet but the framing changed: cost-evaluation-against-value, not blanket cost-cutting. The X-link-as-spec pattern is now the dominant async direction-setting channel between founder and engineering.

5. **The "high value assets" framing is new.** Apr 15 OpenAI cost crisis ordered a `gpt-4o → gpt-5-mini` migration to *cut* spend. Apr 26 reframes the question: *some assets are worth a premium model.* If Moil 360 has tiers of asset quality (e.g., business plans vs. carousel captions), the model-routing decision is now per-asset, not per-codebase. First time this distinction is on record.

6. **Day was low-volume, high-precedent.** Only 18 Teams messages in the 1-day window — well below the Apr 24 (38) or Apr 21 (161) baseline — but every one of them is a relationship-state shift or a coaching-pattern signal. Pattern continues: the highest-signal days are not the highest-volume days.

7. **No customer-facing or pipeline movement Apr 25–26.** No email digest in this window (FitLogic CRM go-live is Apr 28, the Sun Show event aftermath has not produced a tracked customer thread yet). All three updates are internal team-management signals.

**Sources logged but not promoted to wiki:**

- **`raw/weekly-sessions-2026-04-26.md`** — Claude Code weekly rollup for week of Apr 19. 101 sessions across `Brain/Automations` (41), `Brain/KB/worktree` (23), `Clio/worktree` (17), `Brain/KB` (16), and unattributed (4). 265 user messages / 1145 assistant responses / 3704 tool calls / 67 commits. Mirrors the format of `raw/weekly-sessions-2026-04-19.md` (Run 14) and `raw/weekly-sessions-2026-04-15.md` (Run 8) — both also logged-only. Captures the burst of Apr 19–26 KB worktree commits + Clio engineering, no external intelligence to promote.

- **`raw/x-bookmarks-2026-04-25.md`** — 0 bookmarks captured, raw scroll buffer empty per the gstack /browse run notes. No content to ingest. Already noted as `(0 0 items)` in the Apr 25 commit (`89b5935 bookmarks: daily X capture 2026-04-25`). Logged for completeness.

**Summary:** Run 23 is a single-source intelligence run (Apr 26 Teams digest, 18 messages) with two log-only entries. The relational arc is the headline: the Apr 24 AI-adoption clash was bracketed by a 48-hour reset that produced a collaborative remix on the founder-built Moil video. Two parallel founder-shared X references (12:36 AM) drove same-day engineering pickup (Taiwo) + a reframed model-cost ask (Adeleke). MEMORY.md untouched this run — no new open actions required (HeyGen re-auth and demo-video workflow items in MEMORY are already covered by the Apr 24 block; the Adeleke model-cost ask is awaiting his reply, not a separate Andres action). Source count: 300 → 303 (teams + weekly-sessions + x-bookmarks).

---

## 2026-04-25 — Run 22: Apr 24 email digest (Joshua redlined contract + Inna podcast directive + Rashaka pricing offer + first press inquiry)

**Trigger:** Automated scan for unprocessed raw files. One new file since Run 21:
- `raw/email-digest-2026-04-24.md` (committed Apr 24 18:32 by `email-digest` job — 24-hour window Apr 23–24)

**Pages created (1):**
- [[wiki/people/jessica-voyage-austin]] — first press inquiry on record (VoyageAustin Magazine editorial team, interview request Apr 24 12:42 PM CDT)

**Pages updated (4):**
- [[wiki/people/joshua-edmond]] — new "Apr 24, 2026 — Redlined Contract + HIVE Strategist PSAs" section: Joshua sent redlined FAVE&SAVE / HIVE Strategist PSAs back to Shannon Cameron Apr 24 13:08; meeting invite same day at 11:46 AM. First time Joshua's contract edits are on the record. Andres needs to be on the meeting and align before Shannon countersigns. last_contact → 2026-04-24
- [[wiki/people/rashaka-boykins]] — new "Apr 24 — Website Live + Pricing Offer Active" section: Andres opened Apr 24 09:39 with explicit *"$600/year vs $900/month"* pricing offer; Rashaka replied 13:29 *"my website was completed this morning"* + *"there are several questions"*; Andres replied 13:56 with open invitation. 18× spread between annual prepay vs monthly is intentional — annual is the value play. Conversion gate is now her question batch. last_contact → 2026-04-24
- [[wiki/people/inna-benyukhis]] — new "Apr 23 — Podcast Video Directive (Approval-Loop Workflow)" section: Apr 23 21:43 directive *"Please create the content. Send it to me for review. Then post on both LinkedIn and IG."* Three-step approval-loop workflow now formalized; resolves the Apr 20 IG-tagging question — Inna chose Option A (Moil posts directly with her review). last_contact → 2026-04-23
- [[wiki/people/becky-torres]] — new "Apr 24 — Two-Way Family-Inclusive Touchpoint" section: Andres replied 08:38 *"my wife was impressed with the shampoo too"* — first organic Mariana ↔ Moil-client crossover. Vendor-to-neighbor frame no longer one-sided. last_contact → 2026-04-24
- [[MEMORY]] — new "🔥 Apr 24 inbox — Contract reviews + Press + Customer directives" block at top of Immediate: Joshua redline review pre-meeting, VoyageAustin reply, Inna podcast slicing, Rashaka question-batch wait, Apollo first-name mapping audit, Victor Escamilla / Buda UDC reply

**Key intelligence from Run 22:**

1. **Joshua Edmond redlined the HIVE Strategist PSAs contract.** Apr 21 Shannon Cameron forwarded the PSAs; Apr 24 Joshua replied with redlines + a meeting invite. The Cohort 4 contract is at "review complete with edits" status. Critical: Andres needs to be on Joshua's meeting (or pre-aligned with Joshua) before Shannon countersigns — single-position is the only safe play with the public-facing Incubator Strategist Team title at stake.

2. **Rashaka pricing offer is on the table — annual prepay is the value play.** $600/year vs $900/month — 18× spread by design. Her website went live Apr 24 morning, which is the conversion moment. She's in question-batch mode (*"there are always questions"*). Likely closeable in days if Andres handles the question reply tightly.

3. **Inna's IG/LinkedIn tagging question is resolved.** Apr 20 the team flagged Option A (Moil gets direct access) vs Option B (send-and-post). Apr 23 21:43 Inna chose Option A explicitly: *"Please create the content. Send it to me for review. Then post on both LinkedIn and IG."* The 2 March podcast videos she sent Apr 21 are now actionable — Jacob/Ablad slice → Inna review → Moil publish. Removes the Apr 20 ambiguity blocker.

4. **First press inquiry on record (VoyageAustin Magazine).** Cold inbound from Jessica @ voyageaustin.com — local-Austin-entrepreneur Q&A format. Low edit pressure, third-party-verifiable, useful for `moilapp.com/about` press section + chamber/EDC outbound social proof. Worth saying yes fast.

5. **Apollo merge-bug flag.** Apr 24 09:03 outbound greeted "Joseph" but the address was `wilkinsonroger860@gmail.com` (Roger Wilkinson). First-name field decoupled from email field somewhere in the Apollo sequence pipeline. Audit before next batch — this kind of error makes the founder-tone outbound look sloppy.

6. **Becky Torres relationship now bidirectional.** Apr 23 Andres brought his mom by SIREN; Apr 24 Andres looped Mariana into the SIREN product experience (*"my wife was impressed with the shampoo too"*). Mariana being impressed with a customer's product organically is the first Mariana ↔ Moil-client crossover — referral pathway through the Buda small-business network without push.

7. **Andres-to-Andres email-as-memory pattern continues.** Apr 24 Andres sent himself an `cs@moilapp.com` reminder list (covered in Run 20). The Apr 23 04:04 self-note + Apr 24 outbound rhythm is a stable pattern — recognize as habit, don't systematize away.

8. **Joshua Edmond's Apr 24 second email (received from Andres's view) is reading as three contracts moving in parallel.** PSAs review thread, redlined contract, and a meeting invite — same day, same partner. Cohort 4 prep is now the highest-velocity contract thread in the Brain.

9. **The Therese Gordon / Mike Hardill / Christy Trammell / Rosanne Ford / Otis Rawl / Lori Smith / Nicole Quiroga break-up batch (Apr 24 morning) is the second day of "Should I close this out? / Last note" template usage.** Continues the Apr 23 EDC outbound pattern noted in Run 20 — same templates, different prospects, no responses to log yet.

10. **Brian Dyer (Buda EDC) lunch-with-Andres-and-John accepted.** Apr 24 10:41 calendar accept. The Andres + John (Costilla) + Brian Dyer triad is the operational Buda EDC working group — first explicit lunch booking on record.

**Summary:** Run 22 is a single-source run (Apr 24 email digest, ~75 emails). Lower volume than Run 21 but high-density on commitments and contract movement. Three deals advanced (Joshua Edmond contract redline, Rashaka pricing-on-table, Inna podcast workflow unblocked) and one new channel opened (VoyageAustin press). MEMORY.md sits at 142 lines, well inside the 200-line cap. Source count: 299 → 300.

---

## 2026-04-24 — Run 21: Apr 24 Teams digest (marketing-team escalation + Sun Show event + weekend dev sprint)

**Trigger:** Automated scan for unprocessed raw files. One new file since Run 20:
- `raw/teams-2026-04-24.md` (committed Apr 24 18:07 by `teams-daily` job — 99 messages across 5 threads, Apr 24)

**Pages created (1):**
- [[wiki/meetings/2026-04-24-teams-daily-ops]] — Apr 24 Teams digest covering three story arcs: Andres ↔ Ablad AI-adoption clash, founder-built Clio demo videos at `clioremembers.com/demo`, and the Sun Show evening event with the free-month-license ship-readiness gap

**Pages updated (5):**
- [[wiki/people/abiodun-solomon]] — new "Apr 24 — First Documented AI-Adoption Clash with Andres" section: 38-message Moil Marketing thread crystallizing the long-running AI-tools-adoption tension; both positions on record; partial reconciliation when Abiodun praised the Clio demo video; HeyGen tools-fit decision pending; last_contact → 2026-04-24
- [[wiki/people/jacob-oluwole]] — new "Apr 24 — Conversion-Strategy Coaching + Megan Handoff Clarification + Voiceover Decision" section: Andres-as-coach pushing strategy-before-execution on Apr 23 outbound batch; Megan handover confirmed Apr 29 (not Apr 23, not Apr 30); voiceover + mobile feedback on Clio demo video; auto-assign Moil 360 license feature in dev; Jacob brokering between Andres and Ablad; last_contact → 2026-04-24
- [[wiki/people/taiwo-ola-balogun]] — new "Apr 24 — First Voluntary Weekend Commitment" section: Apr 25–26 weekend Inna + Connectex sprint volunteered (pace-shift continuing from Apr 18→21→24); Inna ownership-ambiguity surfaced ("I thought you worked on Inna already"); GitHub-as-universal-SSO confirmed; last_contact → 2026-04-24
- [[wiki/people/adeleke-tolulope]] — new "Apr 24 — Auto-Assign License (Staging) + Onboarding-Guide Routing" section: auto-assign-Moil-360-license is staging-only on Sun Show event night; proposed routing pattern for the existing in-app guide for new-user onboarding ("if they ask the little guide, it can direct them"); AI-iteration on prod work confirmed (multiple passes to spec); last_contact → 2026-04-24
- [[MEMORY]] — new "🔥 Apr 24 → next-week — Marketing + Onboarding + Demo-video workflow" block: Ablad agreement, demo-video workflow, in-app guide redesign, auto-assign license to prod, Taiwo weekend sprint, Jacob outbound rework, HeyGen re-auth, HeyGen subscription decision

**Key intelligence from Run 21:**

1. **First documented Andres ↔ Ablad AI-adoption clash on the record.** Two years of background tension turned into a 38-message structured argument in the Moil Marketing channel (Apr 24 11:42 AM – 12:47 PM), with both positions visible. Andres's frame: Moil sells AI but its marketing team is slow to adopt AI tools, wastes HeyGen credits, misses opportunities. Abiodun's frame: AI tools are used daily, HeyGen specifically doesn't lift from the website (doubles work), Andres dismisses opinions and repeats past arguments. Andres ended with disengagement signal — *"you just won't hear it from me anymore!"* — and a private escalation to Jacob: *"I'm this close to closing our full marketing department."* First time the marketing-department-closure threat is on record.

2. **Founder-built Clio demo videos bypassing the marketing team.** Andres has been creating product demo videos using AI tools (HeyGen + ChatGPT image2 + Capcut). Live artifact: `clioremembers.com/demo`. Used at the Sun Show event Apr 24. Andres named the pattern in the team channel: *"This is what happens when people make me mad! I build."* Implicit message inside the team: the founder can ship a polished demo video faster than the design team — the AI-adoption gap is no longer rhetorical.

3. **Megan FitLogic handover confirmed Apr 29 (not Apr 23, not Apr 30).** Jacob asked if the handoff happened yesterday; Andres clarified *"Not a handoff, we are doing that next Wednesday!"* Removes ambiguity from the FitLogic CRM handoff sprint timeline. Apr 23 was setup; Apr 29 is the formal walkthrough.

4. **First voluntary Taiwo weekend commitment.** *"I have the weekend to work on Inna and connectex"* (6:57 PM, 1:1 with Andres). Pattern shift continuing: Apr 18 time-zone boundary → Apr 21 revenue urgency → Apr 24 weekend volunteer. Inna ownership-ambiguity surfaced live: *"I thought you worked on Inna already"* — needs resolution before the sprint.

5. **Sun Show event = first real-world ship-readiness gap on Moil 360 conversion flow.** Andres asked at 8:37 PM (event in progress) for a way to give a free one-month license to weekend signups. Adeleke flagged the auto-assign-license feature is staging-only, not pushable to prod by tonight. The product has a feature for what the founder needs at a live conversion event — but it's not shipped. Manual workaround implied.

6. **Jacob's outbound is strategy-thin, not effort-thin.** Andres reviewed Jacob's Apr 23 group outreach batch: *"Completely missed opportunity to convert over 2000 businesses but we have to do it right."* Pushed Jacob upstream — *"What was the strategy you used to make the decision for the comments you sent and posted? How were they driven to convert?"* Coaching pattern shift from execution review to strategy review.

7. **AI-iteration on prod work is real, not first-pass-clean.** Jacob's status to Andres on a stuck backend feature: *"Steve began work on it yesterday... he said the AI is not doing exactly what he is asking it... so He is doing it again."* Confirms the Apr 21 Claude-Code-pushed-fix pattern but with first-pass-clean as the unmet bar — multiple iterations needed to land output to spec. The AI-driven dev pattern works but requires more loops than expected.

8. **Onboarding gap re-surfaces as customer feedback, not internal hypothesis.** Andres at 12:09 PM: *"Client feedback, they logged in and didn't know what to do next?"* The onboarding-revamp work Andres sent "last week" is now justified by an external complaint. Adeleke proposed routing the existing in-app guide ("if they ask the little guide, it can direct them") — discoverability of the guide is the immediate fix, not the guide's content.

9. **HeyGen subscription is at decision-point.** Login expired during the Apr 24 ideological debate. Abiodun's stance: HeyGen doesn't lift from the website, it doubles work. Andres's stance: keep it, use HeyGen hyperframes, stop wasting credits. The Apr 24 working capital + workflow-fit decision is now explicit, not background.

10. **Jacob is operational broker between Andres and Ablad.** Quote: *"I'll speak to Ablad and try to communicate what you were talking about to him..."* (12:08 PM). Jacob taking the position-translator role inside the AI-adoption argument — first time the operational-bridge function applies to a leadership-level conflict, not just delivery coordination.

**Summary:** Run 21 is a single-source run (Apr 24 Teams digest) but high-signal — the kind of day that produces precedents rather than incremental updates. The Andres ↔ Ablad clash is the first marketing-team-closure-threat on record; the Clio demo video at `clioremembers.com/demo` is the first founder-built artifact bypassing the design team; Taiwo's weekend volunteer is the first non-pushed weekend commitment; the Sun Show event surfaced the auto-assign-license ship-readiness gap. MEMORY.md sits at 133 lines, well inside the 200-line cap. New "Apr 24 → next-week" block added at the top of Immediate.

---

## 2026-04-24 — Run 20: Weekly compile (Apr 23 email digest + Apr 24 X bookmarks + MEMORY rot + freshness audit)

**Trigger:** `/brain weekly compile` invocation. Two new raw files since Run 19:
- `raw/email-digest-2026-04-23.md` (committed Apr 23 18:31 by `email-digest` job — 24-hour window Apr 22–23)
- `raw/x-bookmarks-2026-04-24.md` (captured Apr 24 10:58 via gstack /browse — 82 bookmarks Feb 4–Apr 24, account `@roarkittys`)

**Pages created (3):**
- [[wiki/people/marilyn-eden]] — the previously-nameless "Eden — Website discovery" (Apr 8) prospect now has a full name + Apr 23 reactivation timeline (Teams 5pm CDT meeting accepted same day)
- [[wiki/people/kemi-riley-telfort]] — Aeparmia Engineering, met at Heritage Session networking event, first inbound Apr 23
- [[wiki/summaries/x-bookmarks-2026-04-24]] — 82-bookmark digest organized by Andres's working themes (harness engineering, Managed Agents ecosystem, vertical AI, GTM reality check, local inference)

**Pages updated (5):**
- [[wiki/people/becky-torres]] — Apr 23 personal warm signal (Andres brought his mom by SIREN, Becky forwarded brand link from her sister); last_contact → 2026-04-23
- [[wiki/people/roxana-yglesias]] — Apr 23 "Brand Info" email (Canva asset handover continuing); last_contact → 2026-04-23
- [[wiki/concepts/claude-code]] — Apr 14–24 update: Routines vs Schedules vs /loop trio, Recaps, adaptive thinking on Opus 4.7, Claude Doctor, Compound Engineering v3
- [[wiki/concepts/managed-agents]] — Apr 17–22 update: Hermes use-case list (mvanhorn), Clawputer cloud GBrain, OpenClaw security 3-level fix
- [[wiki/concepts/linkedin-gtm]] — ⚠️ Apr 21 algorithm shift section: Paolo Scales says AI content tactics from 6 months ago killing reach; Apr 4 Logan Gott playbook now suspect

**Cleanup work this run (no source ingestion):**
- **MEMORY.md priority rot pass** — applied weekly compile rules: items in 🔥 Immediate >14d old → Deferred; 📅 Next 2–3 weeks ranges ended >14d ago → Deferred; Verify items from sources >60d old → Closed; Closed/Archive >30d → deleted. Last-updated bumped to 2026-04-24.
- **Wiki freshness audit** — flagged orphaned wiki pages (`Last updated:` >60d AND zero inbound wikilinks) with `stale: true` frontmatter. See compile report for full list.
- **Link integrity** — verified every wikilink in `index.md` resolves to an existing file.

**Key intelligence from Run 20:**

1. **The "Eden" carryover finally has a name.** "Eden — Website discovery" has been on every weekly punch list since Apr 8. Marilyn Eden (Orphic Creative) accepted a same-day Teams invite Apr 23 — first response in 15 days. The prospect was tracked anonymously this whole time; the new people page closes that data-quality gap.
2. **First Heritage Session networking signal.** Kemi Riley-Telfort (Aeparmia Engineering) is the first documented inbound from the Heritage Session local event. Worth marking Heritage Session as a known channel (alongside Buda HIVE, EDC outbound, iMessage referrals).
3. **Becky Torres relationship moved from vendor to neighbor.** Andres bringing his mom by SIREN, Becky forwarding her sister's brand link — first non-business touchpoint with a paying client. Strengthens the case-study + referral story for [[wiki/orgs/siren-beauty]].
4. **The harness layer matured fast.** Three weeks of bookmarks show Claude Code automation moving from "you build it" to "Anthropic ships it" — Routines, Recaps, adaptive thinking, Claude Doctor are all now native or near-native. Andres's launchd-based Brain automation deserves a comparison pass against Routines.
5. **🔥 LinkedIn algorithm playbook may be stale.** The Apr 4 Logan Gott framework that anchors [[wiki/concepts/linkedin-gtm]] is contradicted by Paolo Scales's Apr 21 thread ("AI content is dead, tactics from 6 months ago killing reach"). Before the next LinkedIn push, reconcile. The 11%-vs-35% AI-SDR meeting-to-pipeline gap (itsalexvacca Apr 14) is supporting evidence: AI-assisted outbound is hitting limits.
6. **Hermes Agent now has a use-case shape.** First non-hype list of what people actually do with Hermes (mvanhorn Apr 19): pre-call research, proposal writing, CRM sync. Direct overlap with Moil's customer-success workflow — worth evaluating Hermes vs Pi for the proposal-writing case.
7. **EDC outbound machine is at full throttle.** 20+ cold sends Apr 23 across three template variants ("Something we didn't expect" / "What entrepreneurs see" / "Last note") targeting EDCs and chambers (Boston, Worcester, Western Mass, Frederick, Melrose, MetroWest, Charles County, Burlington, Nashoba Valley, Amy Gowan AAEDC, Joe Venhuizen Envision Greater FDL). Largest single-day outbound volume since pipeline tracking began.
8. **Self-note discipline showing up.** Andres sent himself a `cs@moilapp.com` reminder Apr 23 04:04 — "send letter to EDC, call Juan, reply to Jennifer, reply to Desiree." Email-to-self as a working memory tool is a habit worth recognizing rather than systematizing away.
9. **Mark Cuban frame is direct ammo for Moil.** "Real AI money is 1 vertical, 1 workflow, 1 painful problem" (WorkflowWhisper Apr 18) — single sharpest distillation of Moil's narrow-ICP thesis. Quote candidate for a pitch deck.
10. **Stitch 2.0 + DESIGN.md spec open-sourced.** Could become a Moil internal convention for client-site work — "stops apps looking like AI slop" pattern. Adoption decision is low-cost, high-leverage.

**Summary:** Run 20 is a hygiene-first run. Two new sources (a low-volume email digest + a high-volume bookmarks dump), three new wiki pages (two thin people pages closing carryover gaps + one summary), three concept-page updates absorbing two weeks of harness/agent/GTM signal. The bigger work was the MEMORY.md priority rot pass and the wiki freshness audit — see `quartz/content/raw/compile-2026-04-24.md` for the full report. (Wiki freshness audit found zero stale orphans this run, which is itself a signal — every one of the 261 wiki pages is reached by at least one inbound wikilink and no page is older than 60 days.)

---

## 2026-04-23 — Run 19: Apr 22 email digest + Apr 23 Megan CRM/Google setup

**Trigger:** Automated scan for unprocessed raw files. Two new files since Run 18:
- `raw/email-digest-2026-04-22.md` (committed Apr 22 by `email-digest` job — 24-hour window Apr 21–22)
- `raw/teams-transcript-CRM-GOOGLE-Setup-with-Megan-2026-04-23.md` (40-min live Teams VTT transcript, 2:15–2:58 PM CT Apr 23 — Andres + Taiwo + Megan + Michelle)

**Pages created (1):**
- [[wiki/meetings/2026-04-23-megan-crm-google-setup]] — 40-min customer setup call: Google Cloud OAuth + GitHub/Supabase/Resend wiring, Electric Bricks compliance dispute, Apr 28 go-live, Apr 29 handover meeting, Daniel D. Mann second-degree loop via Michelle

**Pages updated (8):**
- [[wiki/people/megan-miller]] — Apr 23 CRM/Google session block: infrastructure-owned-by-Megan architecture, calendar-hygiene behavioral commitment, Electric Bricks Friday meeting, Michelle/Daniel Mann connection; last_contact → 2026-04-23
- [[wiki/orgs/fitlogic]] — new "Apr 23 Handoff Architecture — CRM Stack Owned by Megan" section with full ownership matrix (GoDaddy / Vercel / Supabase / Resend / GitHub / Google Cloud OAuth / Gemini); deal-status updated to Apr 28 go-live + Apr 29 handover; Michelle contact row flagged with Daniel Mann connection
- [[wiki/people/katherine-silvas]] — Apr 22 call held; Moil Partnership Proposal sent same day 5:26 PM; next action is now "await Board response" rather than "prep call"
- [[wiki/orgs/helotes-edc]] — timeline updated (Apr 22 Zoom call + proposal out); next actions reset from "pre-call prep" to "await Board response; nudge Apr 29–May 6 if silent"
- [[wiki/people/rashaka-boykins]] — Apr 22 second inbound question (web/social traffic + LinkedIn/Instagram integration) added to same thread as Apr 21. Draft reply framing documented (adaptive LLM marketing / traffic driving / LinkedIn-IG honesty-over-spin)
- [[wiki/people/taiwo-ola-balogun]] — first recorded live customer setup call; drove Google Cloud OAuth config; pre-empted multi-env redirect URI friction; took GitHub collaborator role; Apr 29 deadline acknowledged ("Okay, sir"). Pace shift from "late-night frustrated" to "late-night voluntary and bounded"
- [[wiki/people/daniel-mann]] — new "Second-Degree Social Proof Loop via Michelle @ FitLogic" section; first recorded instance of Daniel's referral graph closing back through an existing Moil customer's staff; 🔥 action item: direct text from Andres
- [[wiki/moil/gtm]] — new "Apr 22 update" section: largest single-day breakup wave (17 breakups in MI + GA), two narrative re-engagements (Mandy Power / Rachapa Lau), first Trial Runners SMB-consulting outreach (Jill Healy), Helotes Partnership Proposal sent
- [[MEMORY]] — new "Apr 23 → Apr 29 FitLogic CRM handoff sprint" block at top; Helotes call marked done; Rashaka action consolidated to cover both Apr 21 + Apr 22 inbound
- [[index]] — stats refreshed (258 pages / 306 raw sources)

**Key intelligence from Run 19:**

1. **Moil's first "customer owns the stack from day one" deployment.** FitLogic's CRM is being built with every infrastructure account (GoDaddy / Vercel / Supabase / Resend / GitHub / Google Cloud / Gemini) owned by Megan's credentials, not Moil's. Taiwo is a collaborator. This is a new pattern — historically Moil owned the stack and migrated later. If it holds as the Moil 360 CRM template, handoff becomes a credential transfer rather than a migration project.
2. **Seven-day CRM time-to-value baseline.** Apr 21 live tour → Apr 23 infrastructure wired → Apr 25–26 weekend testing → Apr 28 go-live → Apr 29 formal handover. This is the first replicable time-to-value window for a Moil-built CRM customer.
3. **Helotes Partnership Proposal is the second EDC proposal in existence.** After the Apr 22 10 AM Zoom call, Andres sent Kate Silvas the Moil Partnership Proposal same day 5:26 PM. First written proposal Moil has put on an EDC decision-maker's desk outside Buda. Decision timeline now sits with Kate's Board.
4. **Daniel Mann's referral graph closed back through a Moil customer.** Michelle (FitLogic staff, on Apr 23 call) opened with "Daniel D. Mann says hello to you." First recorded instance of Daniel's referrals looping back through an existing Moil customer's team — his network overlaps Moil's customer base beyond the 8 direct intros already logged. Strengthens the case for systematizing Daniel as a channel rather than ad-hoc referral flow.
5. **Rashaka Boykins sent a second inbound in 27 hours.** Apr 21 (LLM marketing / adaptive) + Apr 22 (traffic + LinkedIn/IG integration) — two substantive product questions after 6 weeks of silence. Neither has been replied to yet. Strongest warm-lead reengagement signal of the week.
6. **Megan committed to calendar hygiene.** She admitted during the Apr 23 call that she missed an 11 AM meeting earlier that day because the meeting only lived in her head. She committed to forwarding every invite to Andres going forward — standing behavioral change, not a one-off. Andres becomes her external calendar. Retention-risk insight hiding in plain sight: the CRM she's buying ought to auto-surface this pattern.
7. **Apr 22 was the campaign's largest breakup day yet.** 17 breakup emails in a single batch, concentrated in Michigan and Georgia — closing out two of the Apr 9–10 original clusters. In parallel, two warm narrative re-opens (Mandy Power / Rachapa Lau), one new SMB vertical test (Jill Healy / Trial Runners), and the Helotes proposal moving from discovery to written artifact. Pipeline hygiene and late-stage artifacts running simultaneously.
8. **Electric Bricks compliance fight is the first scope-of-practice-on-website issue logged.** Megan pushing back on "doctor" vs. "health coach" framing — as an NP, her scope of practice has to be unambiguous for patient safety. The Friday Apr 24 12:30 PM meeting (Andres attending) is the first time Moil is joining a customer's vendor fight on content-compliance grounds. This shapes the playbook for Moil's future licensed-professional customers (therapists, coaches, NPs) where AI-generated content needs scope-of-practice guardrails.
9. **Taiwo joined his first live customer call.** Precedent: Taiwo has historically been engineering-side only. Apr 23 was his first video call with a customer — and he drove the technical config (OAuth scopes, redirect URIs). Opens a new operating pattern: named-engineer-per-customer handoff instead of rotating support.
10. **Kate Silvas sent Zoom links from her `helotes-tx.gov` email.** Formal government-email channel is now in use for Helotes deal, not just Gmail. Raises the stakes of the proposal deliverability / tracking — the proposal needs to be government-inbox-friendly.

**Summary:** Run 19 is a decisive-artifact run. Two "first" events: the first customer-owned-stack CRM deployment (FitLogic) and the first EDC partnership proposal outside Buda (Helotes). Plus the first live customer call with Taiwo on video, the first second-degree Daniel Mann referral loop closing, and the first scope-of-practice content-compliance issue on a Moil customer's site. MEMORY.md sits at 120 lines — comfortably inside the 200-line cap.

---

## 2026-04-22 — Run 18: Email digests Apr 20 + Apr 21

**Trigger:** Automated scan for unprocessed raw files. Two new files since Run 17:
- `raw/email-digest-2026-04-20.md` (committed Apr 20 by `email-digest` job — 24-hour window Apr 19–20)
- `raw/email-digest-2026-04-21.md` (committed Apr 21 by `email-digest` job — 24-hour window Apr 20–21)

**Pages created (3):**
- [[wiki/people/irma-mason]] — local community referrer; two warm intros in 24 hours (Elisa Alaniz + Mrs. Unger)
- [[wiki/people/elisa-alaniz]] — project manager referred by Irma Mason; Friday ~3:30 PM CT discovery call booked
- [[wiki/people/shannon-cameron]] — **Director of Operations, Buda EDC**; first documented contact — forwarded HIVE Strategist PSA assets Apr 21

**Pages updated (10):**
- [[wiki/people/megan-miller]] — Apr 19 payment-plan renegotiation ask ($500/mo × 3 → $250/mo × 6); new source refs
- [[wiki/people/rashaka-boykins]] — Apr 21 inbound re-engagement (LLM marketing / adaptive platform question); status warm → active
- [[wiki/people/daniel-guadiano]] — Apr 21 reply proposing Apr 22 (after 1pm) or Apr 23 (after 10am) meeting
- [[wiki/people/jill-pureserenity]] — Apr 21 pre-launch "Pending Items" checklist + Teams invite; PureSerenity license-link still blocked on `partners@moilapp.com` deliverability
- [[wiki/people/roxana-yglesias]] — Apr 20 first Stripe payment ($75) for Moil Enterprise
- [[wiki/orgs/buda-edc]] — added Shannon Cameron (Director of Operations) to leadership layer; Casey Earley title corrected to Administrative Coordinator
- [[wiki/orgs/astra-restaurant]] — status line updated: meeting proposed Apr 22/23; last_contact → 2026-04-21
- [[wiki/orgs/alloy-atx]] — Apr 20 first Stripe payment logged
- [[wiki/orgs/fitlogic]] — Apr 19 Megan payment-plan ask captured under Deal Status
- [[wiki/moil/gtm]] — Apr 20 (MA-heavy 24-email day) + Apr 21 (IL/ON/NH breakup cluster + Karla Ganster SMB template test + Astra reply) outbound sections added; warm-referral lane from Irma Mason documented; Apr 20 AlloyATX Stripe revenue signal noted
- [[MEMORY]] — new Apr 22–May 2 action items: Daniel Guadiano meeting, Elisa Alaniz phone call, Mrs. Unger response, Rashaka reply, Megan payment-plan decision, Caroline Mungenast Apr 24 re-queue, Buda HIVE Apr 27 Lunch & Learn, Shannon Cameron PSA follow-up

**Key intelligence from Run 18:**

1. **AlloyATX is now live-billing at $75/mo.** First Stripe payment from Roxana hit Apr 20 — the Apr 14 close is no longer theoretical. Combined with Apr 21 Moil 360 launch-day chaos, this is the week Moil crossed from "selling" to "collecting" on 2026 closes.
2. **Astra Restaurant deal is active again.** Daniel Guadiano's Apr 9 inquiry stagnated for 12 days; Andres broke the silence Apr 21 by proposing Apr 22/23 meeting slots. If it closes, this is the **first hospitality-ICP case study** — template for restaurant vertical.
3. **Megan Miller asked to renegotiate payment terms** ($500/mo × 3 → $250/mo × 6). Ask landed Apr 19, two days before the 89-minute CRM tour. The renegotiation + website-update ask in the same email needs a revenue decision alongside the Apr 21 deliverability firefight.
4. **Rashaka Boykins broke a 6-week silence on her own initiative.** Apr 21 inbound question on LLM marketing — platform-fit curiosity from a previously-warm prospect who went quiet after the Feb 27 / Mar 5 double intro calls. Re-engagement with zero outbound pressure is a strong signal.
5. **Irma Mason emerged as a repeat referrer.** Two warm intros in 24 hours (Elisa Alaniz + Mrs. Unger) — first documented multi-referral from any single community contact. Local Kyle/Buda/San Marcos geography aligns exactly with Moil's home market. Distinct lane from cold chamber/EDC outbound.
6. **Shannon Cameron opens a fourth Buda EDC relationship layer.** After Jennifer (CEO), Jacquie (HIVE Asst. Director), and Casey (Admin Coordinator), Shannon (Director of Operations) is now on the graph. The HIVE Strategist role is getting formal PSA treatment — Moil's Buda EDC footprint is deeper than any other EDC.
7. **Outbound breakup wave tilts international.** Apr 21's 25-email day hit Canada (Hamilton, Haliburton, Toronto, Mississauga), Illinois (Rock Falls, Bolingbrook, West Ridge, Intersect Illinois, LaGrange, Greater Hall), and New Hampshire (Monadnock, Portsmouth, Mt. Washington Valley, Strafford) — all closing sequences, not opening them. First documented cross-border close-out cluster.
8. **New SMB outbound template.** "Most SMB owners tell us the same thing…" sent to Karla Ganster (CAP Consulting Eng) Apr 21 — first recorded use, first SMB (not chamber/EDC) target with this framing. Potential A/B signal to watch.
9. **Caroline Mungenast / Birmingham Business Alliance** is not dead — OOO at Hannover Messe until Apr 24. Re-queue rather than close out.
10. **CHES Career Day (May 7) fully confirmed.** Mariana Rodriguez (Andres's wife) accepted as presenter; Renee Simmons confirmed 20-min slot to 4th/5th graders. Andres and Mariana are now both booked for this community event.

**Summary:** Run 18 was a quiet-signal run. No new meetings, no new product firefights — but three new people pages (two warm referrals + a new Buda EDC leadership contact), first Stripe revenue signal, a payment renegotiation that needs a decision, and a re-awakened March prospect. Outbound cadence tilted breakup-heavy across Apr 20–21 with strong MA + IL + Canada + NH concentration. MEMORY.md sits at 107 lines — well inside the 200-line cap.

---

## 2026-04-22 — MEMORY.md prune (Phase 0C of Brain Activation Plan)

Compressed MEMORY.md from 200 → 100 lines ahead of Phase 1 correlator work, which will add new sections (Signal Brief context, relationship radar). Every open action preserved; only duplicative formatting and resolved items were consolidated.

**Closed / archived from MEMORY.md:**
- [x] **2026-04-21** — Megan Miller first Moil 360 customer to complete a live CRM onboarding session (89 min). First 5000-contact import pipeline unblocked. Sequences confirmed as killer feature.
- [x] **2026-04-21** — Taiwo committed to Connectex Apr 22 start (first concrete commit after 3 weeks of slipping).
- [x] **2026-04-20** — Abiodun delivered Moil + Inna content by Sun Apr 19 deadline (manifest in Moil Marketing 8:55 AM).
- [x] **2026-04-18** — FitLogic Apr 18 deadline passed; Daniel Guadiano Apr 16 meeting held.

**Consolidated into "Technical debt" section:** Apr 5–12 Teams ingestion technical items (tour guide bugs, segment analytics, image context, Supabase deploy, Meridian, phone sign-up, video production, Sun show raffle, Adeleke FB account, credentials migration) — preserved verbatim but grouped under one header rather than five sub-sections.

---

## 2026-04-21 — Run 17: Teams Apr 20–21 + Megan FitLogic CRM onboarding

**Trigger:** Automated scan for unprocessed raw files. Three new files since Run 16:
- `raw/teams-2026-04-21.md` (161 messages across 6 threads, Apr 20–21)
- `raw/teams-transcript-megan-miller-2026-04-21.md` (89-minute Megan × Andres working session — first Moil 360 live CRM onboarding)
- `raw/weekly-sessions-2026-04-21.md` (Claude Code weekly rollup, 18 sessions, week of Apr 19 — meta metadata only, already reflected in downstream wiki pages)

**Pages created (2):**
- [[wiki/meetings/2026-04-21-teams-daily-ops]] — full daily ops digest; decisions, action items, key signals for Apr 21
- [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]] — 89-min customer session, the single most load-bearing product-feedback session captured in the Brain to date

**Pages updated (5):**
- [[wiki/people/megan-miller]] — promoted to hub; added Apr 21 CRM tour block, product feedback table, license activation issue context, Carla patient story
- [[wiki/orgs/fitlogic]] — promoted from spoke to hub; full rewrite covering Moil 360 onboarding, Apr 21 working-session decisions, Electric Bricks redesign problem, product feedback concentration, case-study positioning
- [[wiki/people/jacob-oluwole]] — Apr 21 block: Megan license firefight, partners-domain spam acknowledgment, PureSerenity license slip, `cs@moilapp.com` password leaked in channel
- [[wiki/people/taiwo-ola-balogun]] — Apr 21 block: FitLogic overnight bugs, campaign vs. sequence parity gap surfaced, OG image miss, Connectex Apr 22 start commitment (revenue-urgency shift)
- [[wiki/people/adeleke-tolulope]] — Apr 21 block: prod image-gen latency debug, Claude Code → AWS same-day fix pattern, Gemini→Grok→Qwen multi-model fallback architecture decision, force-assigned Megan's Moil 360 license
- [[MEMORY]] — full Apr 21 block at top; trimmed older Apr 12 Teams carryover to 200 lines; closed Megan Moil 360 onboarding + Taiwo Connectex commitment
- [[index]] — stats refreshed (251 pages / 219 raw sources)

**Key intelligence from Run 17:**
1. **Moil 360 launch day was triage, not parade.** "MOIL 360 BABY!!" at 5:18 PM masked a day of license-distribution failures: Megan FitLogic still didn't have her license after 2 weeks of asking, PureSerenity / Roxana paid but never got their link, Siren Beauty status unknown. Product works; distribution layer is broken.
2. **`partners@moilapp.com` deliverability is P0.** Second confirmed customer (Megan via Gmail spam folder) in two days. Engineering team said "they can't optimize it more" — not acceptable. Workaround for FitLogic tonight: move to per-customer sender domain. Doesn't scale.
3. **Megan's session is the single richest product-feedback session in the Brain.** Six product issues surfaced in one 89-minute call: spam deliverability, 404 links, stuck business-plan switching (2nd customer hit), campaign-vs-sequence link-editing parity, per-campaign click-rate visibility, duplicate-contact detection. Plus one killer-feature confirmation (sequences — "This is what I've been wanting").
4. **Business-plan switching UX is a class-wide bug, not a one-off.** Jacob's own words: "Probably the same thing that happened to me happened to her." Hit Megan weeks ago and again Apr 21. Previously closed via manual DB intervention. Needs a real fix.
5. **Connectex finally committed.** Taiwo said Apr 22 start — first concrete commitment after 3 weeks of slipping. Driver was Taiwo's first explicit revenue-urgency line: "I need to move on to other projects so we can start getting paid!" Pattern shift from Apr 18 time-zone boundary → Apr 21 revenue ownership.
6. **Multi-model fallback on prod.** Adeleke added Gemini→Grok→Qwen fallback for video generation — first on-prod multi-provider routing decision. Architecturally important.
7. **Claude Code → AWS same-day fix pattern is the new normal.** Adeleke pushed three Claude-authored fixes to prod Apr 21 (image-gen latency, template fails, Gemini fallback). The review loop is now: Andres reports → Adeleke fixes via Claude Code → deploys same day.
8. **Credential hygiene collapsed in public.** Jacob posted `Pr0ud**2023$` (`cs@moilapp.com`) in the open Moil Team channel when Adeleke asked at 11:31 AM. Every credential in the team is now in a searchable Teams history. Needs vault + retraining.
9. **Electric Bricks pattern matters for Moil 360 at scale.** Moil customers come with existing agencies mid-engagement. The right play is wait-then-layer: let the agency ship, then Moil adds CRM forms + quiz + routes. Inserting too early burns per-change fees; too late loses trust. Apr 21 set the pattern with Megan.
10. **Megan is the flagship H1 case-study candidate.** Shared GoDaddy credentials on the first CRM call; strongest trust depth in the customer roster; covers the most Moil 360 surface area (hiring + CRM + campaigns + sequences + site + soon quiz).

---

## 2026-04-21 — Run 16: Siren + Inna deep compile

Triggered by client-coverage audit: wiki pages were undercapturing the rich raw HIVE strategy docs.

- **File:** `raw/hive-siren-beauty-wellness-strategy-plan.md` (10-part strategy doc, ~540 lines)
  - **Pages updated:** [[wiki/orgs/siren-beauty]] — expanded from ~35% coverage to full capture: full website audit (strengths + all 13 critical gaps), SEO/AEO status assessment, Saving Face Austin competitive inspiration, full competitive landscape (5 competitors with threat levels), market opportunity (Buda-Kyle corridor), design direction (6 brand colors with hex, typography, photography direction), full site architecture (11 pages + 10 service slugs + 4 local landing pages), complete SEO/AEO strategy, tech stack, Google Stitch + Claude workflow, Sonnet vs. Opus recommendation, 13-week 6-phase roadmap + ongoing cadence, KPIs by Month 1–3 / 3–6 / 6–12

- **File:** `raw/hive-inna.md` + `raw/hive-inna-s-website-feedback.md`
  - **Pages updated:** [[wiki/people/inna-benyukhis]] — added $150/hr coaching rate, $8,400 prior web quote context, SFM licensing program clarification. [[wiki/orgs/ladyboss]] — rewrote from thin stub (45 lines) to full org profile: offer/pricing table, marketing history table with prior web quote, 6-module HIVE build plan with brand colors, open items

**Why this mattered:** Both pages were referenced by dashboards and [[wiki/moil/customers]] but content quality didn't reflect what Moil already knew. Siren's page now functions as the canonical project brief. Inna/LadyBoss now has enough signal that future Moil work can scope from the wiki alone.

---

## Format

```
### [YYYY-MM-DD] Source title
- **File:** raw/filename.ext
- **Type:** article | transcript | pdf | note | tweet-thread | other
- **Pages created:** [[wiki/concepts/X]], [[wiki/people/Y]], ...
- **Pages updated:** [[wiki/moil/Z]]
- **Summary:** One-sentence description of what this source was about
```

---

## Log Entries

### [2026-04-20] Run 15 — Teams Daily Ops Apr 19–20

**Trigger:** Automated scan for unprocessed raw files. One new file: `raw/teams-2026-04-20.md` (committed Apr 20 by `teams-daily` job, 36 messages across 5 threads).

- **File:** raw/teams-2026-04-20.md
  - **Type:** team-communications (36 messages, Apr 19–20 — PRD proposal + Monday Collaboration Apr 20)
  - **Pages created:** [[wiki/meetings/2026-04-20-teams-daily-ops]]
  - **Pages updated:** [[wiki/people/jacob-oluwole]] (PRD process proposal + IG tagging SOP + Monday internet issues), [[wiki/people/adeleke-tolulope]] (proactive prod fixes on business_plan_beta_prod + memory-mode onboarding review + new Claude Code session handoff), [[wiki/people/taiwo-ola-balogun]] (re-engaged on FitLogic + Meridian, personal Gmail taiwotriumphant@gmail.com disclosed), [[wiki/people/abiodun-solomon]] (hit Sunday Apr 19 deadline, full Apr 17–21 content manifest delivered), [[wiki/people/inna-benyukhis]] (Instagram tagging SOP — 2 options pending her decision), [[MEMORY]] (new Apr 19–20 block; trimmed to 199 lines; closed Abiodun Apr 19 delivery), [[index]] (stats refreshed: 246 pages / 213 raw sources / 58 meetings)
  - **Summary:** Jacob proposed a Project Requirements Document (PRD) gate for every new dev project/demo/feature — first time Jacob has pushed a team-wide operating framework rather than just executing. Monday Collaboration call ran two tracks: content/growth (Inna's social, long-form interviews → IG clips, face-led educational direction) and production fixes (Adeleke proactively fixing bugs on `business_plan_beta_prod` ahead of Andres starting parallel project). Abiodun hit the Sunday Apr 19 content deadline with a full manifest in Moil Marketing at 8:55 AM. Taiwo re-engaged despite his Apr 18 time-zone boundary — proactively asked for FitLogic + Meridian walkthrough. New business friction surfaced: Meta Business no longer supports tagging arbitrary accounts on IG, so Moil needs to either take over Inna's IG/LinkedIn directly or hand content back to her to post.

**Key intelligence from Run 15:**
1. **Jacob stepped into process-owner mode.** After the Apr 15–18 testing-pace escalations, Jacob's PRD proposal (Apr 19 11:21 PM) is his first team-wide framework push — not just executing orders. Pattern shift worth watching.
2. **Adeleke is fixing prod bugs proactively.** On `business_plan_beta_prod` codebase — he told Andres mid-call "I already fixed some bugs though" when Andres started a parallel project for the same work. Signals healthy engineering ownership but needs formalization.
3. **New Claude Code session handoff pattern continues.** Andres shared `session_0156Da69uG1W8jSEof5V2xgb` to Moil Team for Adeleke review — third handoff in recent runs (`session_01PP9t1m41A2snaRRACs3TNs` from Apr 18 still pending review).
4. **Instagram tagging SOP gap** — Meta Business blocks tagging from the publishing side. This is a new business-of-content friction that affects every Moil360 content delivery client. Two options framed for Inna: direct access OR send-and-post.
5. **Memory-mode onboarding vs. static onboarding.** Andres asked Adeleke to review the "new memory one" first because it's "less invasive than the static onboarding." Onboarding UX variant is in active A/B consideration.
6. **Abiodun absorbed the rhythm shift.** Week after the "fees" miscommunication and content-rhythm pushback, he delivered the full Apr 17–21 manifest on time (Sun Apr 19 deadline) — a healthy recovery signal.
7. **Taiwo recovered from the Apr 18 boundary.** Despite explicitly asking not to do late-night calls, he proactively asked for a FitLogic + Meridian walkthrough on Apr 20. Boundary was a one-time escalation, not a ceiling.
8. **Jacob's connectivity is a recurring blocker.** Third month running his bandwidth has disrupted Monday calls — team waiting for him again Apr 20 4:18–4:22 PM.

---

### [2026-04-18] Run 13 — Teams Daily Ops Apr 17–18

**Trigger:** Automated scan for unprocessed raw files. One new file: `raw/teams-2026-04-18.md` (committed Apr 18 by `teams-daily` job, 51 messages across 4 threads).

- **File:** raw/teams-2026-04-18.md
  - **Type:** team-communications (51 messages, Apr 17–18 weekend end-of-week review)
  - **Pages created:** [[wiki/meetings/2026-04-18-teams-daily-ops]]
  - **Pages updated:** [[wiki/people/jacob-oluwole]] (Business Coach bug + Alloy invite late + Connectex slipped), [[wiki/people/adeleke-tolulope]] (Claude Code audit session review assigned), [[wiki/people/taiwo-ola-balogun]] (demo prompt context + time-zone boundary), [[wiki/people/abiodun-solomon]] (next-week content deadline Apr 19 + rhythm miscommunication), [[MEMORY]] (new Apr 18–24 week block; trimmed to 200 lines), [[index]] (stats refreshed: 245 pages / 213 raw sources / 57 meetings)
  - **Summary:** End-of-week delivery-pace escalation. Andres repeatedly called out that only 2 of 6 active projects (Meridian + FitLogic) were tested this week — Connectex still untouched despite top-priority label. Business Coach bug flagged (not responding — blocks Jacob's own testing loop). Jacob sent Alloy ATX Moil 360 invite Apr 18 (3 days late vs. Apr 15 push). Taiwo raised first explicit time-zone boundary ("not 11pm / 2am my time"). Abiodun pushed back on content rhythm expectations — deadline set for Sun Apr 19 on next-week Moil + Inna content. Andres flagged architectural regression: current app no longer uses business plan as the single source of truth the prior version did.

**Key intelligence from Run 13:**
1. **Delivery pace is the #1 tension this week.** Direct Andres quotes: "WE ARE VERY BEHIND" / "It's taken us a full week to test 4 projects I built in one week!" / "Did everyone take yesterday off?"
2. **Business Coach is broken in prod** — Jacob couldn't get it to respond. This is the same product Jacob praised ("came out nice") on Apr 15 — regression between Apr 15 and Apr 18.
3. **Moil 360 activation dashboard is live** — partners' dashboard shows when they have activated their license (new product signal, not previously documented).
4. **First time-zone pushback from Nigeria team.** Taiwo's explicit ask to move delivery calls off 11pm/2am his local time is a new scheduling constraint — Andres acknowledged and repeated it to the team.
5. **Architectural regression surfaced.** Andres: "if you look at the previous code the application used a source of truth (business plan) to basically do everything!" — implicit rebuild ask sitting with engineering. May be related to the demo that Taiwo said was "messed up" (context was defined in Lovable, can't replicate in current stack).
6. **Content rhythm shift proposed.** Tuesday push / Sunday review — Andres wants cushion ahead, Abiodun questioned whether that means daily submission or weekly batch. Miscommunication around "less fees" (Andres later said he meant "ideas").
7. **Andres ran a Claude Code audit on a different project** (session `session_01PP9t1m41A2snaRRACs3TNs`) and asked Adeleke to review — extends the pattern of Andres handing off Claude Code sessions to Adeleke for verification.
8. **Connectex is the biggest neglected account.** Jacob named it unprompted as "one of top priorities that we have not looked at" — already a paying customer per earlier runs, and the client contact (Mark Polanco) is on the Moil 360 license list.

---

### [2026-04-18] Run 12 — Batch ingestion of 12 raw sources

**Trigger:** Manual ingestion request. 12 files in raw/ lacked `ingested: true`.

| File | Type | Action |
|---|---|---|
| `buda-hive-edc-2026-04-11.md` | program-doc | Marked ingested — full intel already captured in [[wiki/summaries/buda-hive-edc-2026-04-11]], [[wiki/people/jennifer-storm]], [[wiki/orgs/buda-edc]] |
| `buda-hive-edс-2026-04-09.md` (Cyrillic) | program-doc | Marked ingested — superseded by Apr 11 version; stub at [[wiki/summaries/buda-hive-edc-2026-04-09]] |
| `compile-2026-04-17.md` | compile-report | Marked ingested — Run 10 meta-report, already applied to wiki |
| `facebook-pages-2026-04-09.md` | social | Marked ingested — data already sourced in [[wiki/concepts/moil360]], [[wiki/people/mariana-rodriguez]], [[wiki/summaries/facebook-pages-2026-04-09]] |
| `github-project-tracker.md` | note | Marked ingested — already summarized at [[wiki/summaries/github-project-tracker]] |
| `imessages-people-2026-04-09.md` | email | Marked ingested — **created** [[wiki/people/ingrid-spiritto]] (mother-in-law, net-new); other contacts already had pages |
| `know-me-extraction-prompts.md` | reference | Marked ingested — meta methodology doc, no wiki pages warranted |
| `moil-documents-2026-04-09.md` | note | Marked ingested — **updated** [[wiki/moil/positioning]] with competitor table + ARR financial baseline |
| `moilapp-website-2026-04-09.md` | note | Marked ingested — already sourced in [[wiki/moil/positioning]] and [[wiki/concepts/moil360]] |
| `outlook-emails-2026-04-09.md` | email | Marked ingested — already summarized at [[wiki/summaries/outlook-emails-2026-04-09]] |
| `x-bookmarks-2026-04-11 copy.md` | bookmark | Marked ingested — deep-compiled in prior run (16 concept pages + 5 minds pages) |
| `x-bookmarks-2026-04-11.md` | bookmark | Marked ingested — cross-referenced in prior run |

**Pages created (2):** [[wiki/people/ingrid-spiritto]], [[wiki/concepts/fantelo]] (redirect stub → [[wiki/projects/fantelo]])

**Pages updated (2):** [[wiki/moil/positioning]] (competitor table + ARR targets), [[index]] (stats + header)

**Summary:** Most of these 12 files had already been ingested into wiki pages in earlier runs but lacked the `ingested: true` frontmatter stamp. Net-new content: one new person page (Ingrid Spiritto, mother-in-law) and competitor/financial intelligence added to positioning.

---

### [2026-04-11] First Full Compilation — Batch Ingestion

**Trigger:** Andres asked to kick off the Brain. Run in Claude Cowork (direct file access).

**Sources processed (7 of 12 raw files):**

- **File:** raw/imessages-people-2026-04-09.md
  - **Type:** relationship-intelligence
  - **Pages created:** [[wiki/people/john-costilla]], [[wiki/people/mark-polanco]], [[wiki/people/travis-sutherland]]
  - **Summary:** iMessage conversations revealing family structure, nicknames, and business relationships

- **File:** raw/outlook-emails-2026-04-09.md
  - **Type:** email-digest
  - **Pages created:** [[wiki/people/daniel-guadiano]]
  - **Summary:** Outlook email threads — Astra Restaurant lead, CoffeeSpace partnership, Johns Creek Chamber

- **File:** raw/buda-hive-edc-2026-04-11.md
  - **Type:** partnership / customer / contract
  - **Pages created:** [[wiki/people/jennifer-storm]], [[wiki/people/joshua-edmond]], [[wiki/people/jacquie-martinez]], [[wiki/concepts/buda-hive]], [[wiki/concepts/aedo]], [[wiki/concepts/campaignos]]
  - **Summary:** Full intelligence file on Buda HIVE/EDC — contracts, AEDO, CampaignOS, timeline

- **File:** raw/moil-documents-2026-04-09.md
  - **Type:** business-plan
  - **Pages updated:** [[wiki/moil/positioning]], [[wiki/moil/icp]], [[wiki/moil/gtm]]
  - **Summary:** Moil Enterprise business plan — traction, pricing, market, team, financials

- **File:** raw/moilapp-website-2026-04-09.md
  - **Type:** company-website
  - **Pages updated:** [[wiki/moil/positioning]], [[wiki/moil/icp]], [[wiki/moil/gtm]]
  - **Summary:** Full website scrape — features, pricing, hiring metrics, testimonials, candidate platform

- **File:** raw/facebook-pages-2026-04-09.md
  - **Type:** social-media
  - **Pages updated:** [[wiki/moil/gtm]]
  - **Summary:** AIbyAndres + MoilWorks Facebook pages — follower counts, engagement, social links

- **File:** raw/github-project-tracker.md
  - **Type:** project-tracker
  - **Used for:** AGENTS.md context, task prioritization
  - **Summary:** 48 repos across 3 orgs — activity status, cleanup recommendations, priority tracking

**Also updated:**
- `pi-workspace/AGENTS.md` — 16 bracketed placeholders filled with real data
- `index.md` — source inventory and stats updated

**Remaining raw files (not yet compiled):**
- `brain-guide.md` — meta-guide (reference, not wiki content)
- `know-me-extraction-prompts.md` — extraction prompts (tooling)
- `x-bookmarks-2026-04-11.md` + copy — X bookmark digests (queue for next compile)
- `buda-hive-edc-2026-04-09.md` — earlier version, superseded

---

### [2026-04-11] Second Full Compilation — wiki/summaries + new concepts

**Trigger:** Andres asked to build wiki/summaries/ for every raw file + concept pages for recurring themes + MEMORY.md.

**Summaries created (11 — one per raw file):**
- [[wiki/summaries/brain-guide]]
- [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [[wiki/summaries/buda-hive-edc-2026-04-09]] (marked SUPERSEDED)
- [[wiki/summaries/facebook-pages-2026-04-09]]
- [[wiki/summaries/github-project-tracker]]
- [[wiki/summaries/imessages-people-2026-04-09]]
- [[wiki/summaries/know-me-extraction-prompts]]
- [[wiki/summaries/moil-documents-2026-04-09]]
- [[wiki/summaries/moilapp-website-2026-04-09]]
- [[wiki/summaries/outlook-emails-2026-04-09]]
- [[wiki/summaries/x-bookmarks-2026-04-11]]
- [[wiki/summaries/x-bookmarks-2026-04-11-copy]]

**New concept pages:**
- [[wiki/concepts/brain-architecture]] — Andres's 5-layer pipeline
- [[wiki/concepts/claude-code]] — Anthropic's CLI agent
- [[wiki/concepts/claude-cowork]] — scheduled/background Claude workflows
- [[wiki/concepts/openclaw-hermes]] — open-source parallel ecosystem
- [[wiki/concepts/fantelo]] — Andres's parallel project
- [[wiki/concepts/moil360]] — Moil's 30-day marketing engine brand
- [[wiki/orgs/coffeespace]] — partnership ecosystem contact

**New people pages:**
- [[wiki/people/shay-foley]] — Johns Creek Chamber, deferred partnership
- [[wiki/people/hazim-mohamad]] — CoffeeSpace outreach

**Also updated:**
- `index.md` — summaries section added, concept/people counts refreshed
- `MEMORY.md` — new file capturing open actions from raw sources

---

### [2026-04-12] Email History — Oct 2025 to Apr 12, 2026
- **File:** raw/email-history-2026-04-12.md
- **Type:** email-digest
- **Pages created:** [[wiki/summaries/email-history-2026-04-12]], [[wiki/people/anita-lansing]]
- **Pages updated:** [[wiki/moil/gtm]] (cold outbound campaign now documented as LIVE)
- **Summary:** 10-day email history revealing a 63+ org cold outreach blitz to chambers/EDCs, new active customer Anita Lansing (9 emails), confirmed Inna as Content360 delivery client, John Costilla's "Agentic AI" signal, and Siren Beauty warm lead.

### [2026-04-12] Email History — 2-Month Backfill (Feb 12 – Apr 12, 2026)
- **File:** raw/email-history-2months-2026-04-12.md
- **Type:** email-digest (full pagination, 620 received + 1000 sent)
- **Pages created:** [[wiki/summaries/email-history-2months-2026-04-12]]
- **Pages updated:** [[wiki/people/john-costilla]] (EDC staff role discovered), [[wiki/moil/gtm]] (cold outbound already updated from 10-day ingest)
- **Summary:** 2-month email backfill reveals: John Costilla works at Buda EDC, full Moil team roster (6 members), Casey Earley is HIVE operational backbone (21 emails), Queen Creek Chamber is highly active (12 emails), Inna confirmed as Content360 delivery client, 4+ new customer/lead contacts surfaced, and cold outreach is broader than the 10-day snapshot showed.

---

### [2026-04-12] X Bookmarks Deep Compile — 129 Items

- **Files:** `raw/x-bookmarks-2026-04-11 copy.md` (primary, 129 items), `raw/x-bookmarks-2026-04-11.md` (secondary, 114 items)
- **Type:** tweet-bookmarks (curated X feed, Mar 26 – Apr 11, 2026)
- **Note:** Previous entries (2026-04-11 Second Full Compilation) only summarized these files. This run did the DEEP compile — extracted every concept, person, tool, and framework.

**Pages created (16 concept pages):**
- [[wiki/concepts/seedance]] — Seedance 2.0 AI video (joint audio-video synthesis, Higgsfield + fal.ai)
- [[wiki/concepts/heygen]] — HeyGen Avatar V (character-consistent brand video, captured in 15 sec)
- [[wiki/concepts/vibe-coding]] — Vibe coding paradigm (spec-based workflow, dead code risk, non-dev access)
- [[wiki/concepts/gtm-system-multi-channel]] — MichLieben's 3-layer LinkedIn + multi-channel GTM flywheel ($40K→$7M ARR)
- [[wiki/concepts/ai-org-design]] — AI-native org design (Jack Dorsey "From Hierarchy to Intelligence" + $400K roles replaced)
- [[wiki/concepts/self-learning-gtm-brain]] — Campaign-learning GTM brain that improves from each launch (@pierreeliottlal)
- [[wiki/concepts/obsidian]] — Obsidian as the wiki view layer (plugins, iCloud sync, graph view)
- [[wiki/concepts/local-ai-inference]] — Mac Silicon MLX local AI (Gemma 4 day-0, Qwen3.5 27B near-Opus, LFM2.5-350M)
- [[wiki/concepts/linkedin-gtm]] — LinkedIn algorithm + 3 revenue layers + competitor follower extraction
- [[wiki/concepts/agent-memory-files]] — SOUL.md/MEMORY.md/DREAMS.md/"7 text files" identity pattern
- [[wiki/concepts/smb-ai-audits]] — AI audit service model (Google Ads 190 checks, SEO, CRO, Google Maps play)
- [[wiki/concepts/goose-ai]] — Goose open source agent (Jack Dorsey-endorsed, 471K views)
- [[wiki/concepts/home-service-cro]] — 4.6% conversion framework for home service SMBs
- [[wiki/concepts/meta-harness]] — Self-improving AI agent loop (Meta Harness paper, @MatthewBerman demo)
- [[wiki/concepts/google-stitch]] — Google Stitch 2.0 design-to-code tool + design-system.md pattern
- [[wiki/concepts/content-engine]] — Agent-orchestrated content pipeline (SparkDrop, @coreyganim 21M views claim)

**Pages created (5 minds pages):**
- [[wiki/minds/nick-spisak]] — @NickSpisak_, most comprehensive non-developer Claude educator (7 posts saved)
- [[wiki/minds/corey-ganim]] — @coreyganim, most bookmarked creator (9+ posts), SMB AI monetization
- [[wiki/minds/hooeem]] — @hooeem, full-course format Claude guides (2.8M views on agent course)
- [[wiki/minds/jack-dorsey]] — @jack, "From Hierarchy to Intelligence" (5.6M views) + Goose endorsement
- [[wiki/minds/farza-mohideen]] — @FarzaTV, Farzapedia (1.7M) + Clicky AI teacher (2.7M)

**Pages updated (6):**
- [[wiki/concepts/managed-agents]] — deployment patterns, competitive landscape, "second employee" framing added
- [[wiki/concepts/llm-knowledge-bases]] — Obsidian view layer, Farzapedia, Claudeopedia wave documented
- [[wiki/concepts/ai-video-tools]] — $1M/mo workflow, SparkDrop content engine, Seedance/HeyGen links
- [[wiki/concepts/ai-cold-outreach]] — one-URL campaign builder, SMS/iMessage play, new tactical options
- [[wiki/radar/claude-code-changelog]] — 5 new entries (Monitor tool, security warning, Claude Ads skill, macOS plugin, Stitch)
- [[wiki/minds/andrej-karpathy]] — derivative wave documented, Obsidian view layer noted

**Summary created:**
- [[wiki/summaries/x-bookmarks-deep-compile-2026-04-12]] — master reference with signal rankings and creator watch list

**Summary:** The deepest signal window in the Brain to date — three simultaneous viral events (Karpathy's LLM KB post 19.3M views, Claude Managed Agents launch 20M views, Seedance 2.0 AI video wave) converged in a single 2-week period. Most actionable findings for Moil: (1) start LinkedIn authority strategy, (2) position Content360 as a "content engine" not a "tool", (3) build Google Maps + Claude outbound pilot, (4) audit Claude Code permissions on Mac Mini M4, (5) enable Obsidian as Brain view layer.

---

### [2026-04-12] Microsoft Teams Digest — 30-Day Window (Mar 13–Apr 12, 2026)

- **File:** raw/teams-2026-04-12.md
- **Type:** team-communications
- **Pages created:**
  - [[wiki/meetings/README]] — first README for the meetings folder (previously empty)
  - [[wiki/meetings/teams-attendance-protocol-2026-04]] — first-ever meeting page; documents Moil's async clock-in protocol
  - [[wiki/concepts/moil-team-ops]] — Moil's async team operating system (MS Teams + Power Automate)
  - [[wiki/summaries/teams-2026-04-12]] — structured summary of this raw source
- **Pages updated:** none
- **Summary:** 30-day Teams pull contained 27 messages — all 26 substantive messages were identical automated Workflow bot posts (7:00 AM daily clock-in reminder); `#Alerts` channel had no messages. No human-authored content, decisions, action items, or people intelligence was captured. Value is structural: confirmed Moil operates on MS Teams with a Power Automate-enforced async attendance ritual; `meetings/` folder initialized for the first time. A future pull including human responses would unlock team roster and compliance intelligence.

---

---

### [2026-04-12] OneDrive Meetings — Full Year Ingestion (Aug 2024–May 2025)

- **Files:** 25 files in `raw/meetings/` (mix of Gemini notes and full transcripts)
- **Type:** meeting-records (team meetings, 1:1s, sales calls, partner calls, marketing calls)
- **Date range of content:** 2024-08-07 through 2025-05-19

**Pages created (20 wiki/meetings/ pages):**
- [[wiki/meetings/2024-08-07-abel-zachary-sales-close]] — Zachary Corp closes at $699/yr; first major client
- [[wiki/meetings/2025-01-08-ai-presentation]] — Andres presents/watches generative AI overview
- [[wiki/meetings/2025-01-22-team-meeting-ai-model-selection]] — DeepSeek R1 selected; Workforce Capital Solutions $15-20M opportunity
- [[wiki/meetings/2025-01-27-deepseek-model-demo]] — Steve demos working DeepSeek code generation
- [[wiki/meetings/2025-01-29-team-meeting-code-dataset]] — Dataset creation strategy for internal model
- [[wiki/meetings/2025-02-05-jacob-andres-sync]] — Short ops sync; Google Docs for notes
- [[wiki/meetings/2025-03-12-team-meeting-signup-business-plan-mvp]] — Sign-up redesign + Business Plan Creator launch
- [[wiki/meetings/2025-03-28-jacob-andres-pivot-ai-tools]] — **PIVOT MEETING**: Job-matching → AI toolbox; Interview Tool introduced
- [[wiki/meetings/2025-04-04-team-meeting-algorithm-business-planner]] — Weighted matching algorithm; UTSA license opportunity; MS Teams migration
- [[wiki/meetings/2025-04-07-moil-marketing-call-toolbox-vision]] — Resume builder complete; toolbox vision + full interview tool spec
- [[wiki/meetings/2025-04-09-jacob-andres-business-plan-hubspot]] — Hybrid questions; HubSpot CRM setup; Google→Microsoft migration
- [[wiki/meetings/2025-04-11-team-meeting-prompt-engineering-job-postings]] — 4-page business plan achieved; GPT-4 > GPT-4 Turbo (cost); Sakuri Corp job postings
- [[wiki/meetings/2025-04-14-team-meeting-business-plan-template]] — Final workflow + template structure agreed (2.5hr session)
- [[wiki/meetings/2025-04-18-team-meeting-openai-agent-email-marketing]] — OpenAI agent built by Steve; Google account shutting off May 5
- [[wiki/meetings/2025-04-21-team-meeting-ai-mvp-design-marketing]] — AI-first design approach; marketing plan assigned to Jacob
- [[wiki/meetings/2025-04-28-hubspot-marketing-kickoff-sebastian]] — Sebastian Oviedo (marketing intern) onboarded
- [[wiki/meetings/2025-04-28-moil-marketing-call-ai-content]] — AI image generation strategy; Business Plan Creator "mostly complete"
- [[wiki/meetings/2025-05-09-manos-de-cristo-workshops]] — June 2025 3-workshop series planned; EGBI consulting + Entrepreneurial Spirit Award
- [[wiki/meetings/2025-05-14-jacob-andres-business-insights-review]] — Business Insights section-by-section review; competitor map, TAM/SAM fixes needed
- [[wiki/meetings/2025-05-16-team-meeting-platform-review]] — Two-model pipeline (o4+o3-mini); social automation approved; interview tool MVP approach
- [[wiki/meetings/2025-05-19-moil-marketing-call-technical-issues]] — Low signal; technical failures throughout

**Pages created (6 wiki/people/ pages):**
- [[wiki/people/jacob-oluwole]] — Moil PM; present in virtually every meeting; Nigerian developer
- [[wiki/people/adeleke-tolulope]] — Lead AI/ML engineer (Steve); built OpenAI agent; fine-tuned DeepSeek
- [[wiki/people/abiodun-solomon]] — UI/UX designer (Ablad); Figma; had family emergency Apr 2025
- [[wiki/people/taiwo-ola-balogun]] — Frontend engineer; Gemini for code gen
- [[wiki/people/sebastian-oviedo]] — Marketing intern via HubSpot; blue-collar background; 4-week engagement starting Apr 28

**Pages created (1 wiki/moil/ page):**
- [[wiki/moil/product-roadmap]] — Complete AI stack, feature status, technical specs for all Moil products

**Pages updated:**
- [[wiki/moil/positioning]] — Product evolution narrative + "offline workers" language + toolbox framing
- [[wiki/moil/gtm]] — New channels (UTSA license, school presentations, Manos De Cristo, Sebastian), active clients (Zachary Corp, Sakuri Corp), HubSpot CRM, email marketing infrastructure
- [[MEMORY]] — 20+ historical action items added for follow-up verification

**Key intelligence captured:**
1. **Full Moil team roster:** Andres (CEO), Jacob (PM), Adeleke/Steve (Lead AI), Taiwo (Frontend), Abiodun/Ablad (Design), Sebastian (Marketing intern)
2. **The pivot:** March 28, 2025 — Moil pivoted from job-matching to comprehensive AI toolbox for job seekers AND SMBs. "The market told us what to do."
3. **Clients confirmed:** Zachary Corporation (Aug 2024, $699/yr), Sakuri Corporation (Apr 2025, ongoing)
4. **Product milestone:** Resume builder completed Apr 2025; Business Plan Creator operational May 2025; Interview Tool designed and in development
5. **Infrastructure:** Google Workspace → Microsoft 365 migration (May 2025 deadline)
6. **AI stack:** Gemini (resume) → OpenAI agent (business plan) → o3/o4-mini (insights) — all confirmed operational
7. **Andres's other activities:** EGBI consulting (Austin nonprofit), Entrepreneurial Spirit Award 2025, Manos De Cristo workshops, school presentations
8. **Strategic opportunity:** UTSA license deal for Business Plan Creator (mentioned Apr 4, 2025 — needs follow-up)

**Summary:** This ingestion captured a year of Moil's most important business decisions — the product pivot, the team dynamics, the technology architecture, two confirmed clients, and the transition from a job board to a full AI platform. The Brain now has structural context for every strategic decision Andres made between August 2024 and May 2025.

---

---

### [2026-04-12] OneDrive Full Transcripts — Run 2 (25 Transcript Files)

- **Files:** 25 files in `raw/meetings/transcript-*.md` format
- **Type:** meeting-transcripts (full text — customer calls, advisory calls, team meetings, partner calls)
- **Date range of content:** 2024-10-02 through 2025-05-21
- **Note:** `transcript-2024-10-03-team-meeting-october-2024.md` is a CONCATENATED file of Feb–May 2025 meetings (NOT an Oct 2024 meeting); content is largely a duplicate of Run 1 Gemini notes — no new pages created from it.

**Pages created (wiki/meetings/ — 15 new pages):**
- [[wiki/meetings/2024-10-30-moneta-ventures-investor-panel]] — Andres attended Capital Factory investor panel; Moneta Ventures GP thesis; B2B SaaS focus; AI excitement
- [[wiki/meetings/2024-10-31-monica-munoz-andry-gahcc-partnership]] — GAHCC discovery call; Monica Munoz Andry + Enrique Castro; Ambassador program; Univision/Caracol pipeline
- [[wiki/meetings/2024-11-22-abel-zachary-november-followup]] — Zachary Corp follow-up; Skilly competitor analysis; enterprise multi-user hierarchy; assessments tab; conference referral offer
- [[wiki/meetings/2024-12-03-technical-advisory-azure]] — Kranthi Kumar / Sonata Software / Microsoft Founders Hub; AWS→Azure migration; ACS chat; WhatsApp Business
- [[wiki/meetings/2024-12-03-daniela-castillo-partner-exploration]] — Daniela Castillo Cañavera; equity partnership; Univision/Caracol/RCN media connections
- [[wiki/meetings/2024-12-05-jacob-call-social-automation]] — Automated job post image pipeline spec; 20 Canva templates + OpenAI + webhook
- [[wiki/meetings/2025-02-28-dafne-job-interview-prep]] — Dafne Gutierrez coaching session; voice resume builder live demo
- [[wiki/meetings/2025-03-04-buda-ambassador-followup]] — Buda Chamber Ambassador program logistics; Rosemary Gamez, Crista Wallace, Frost Bank
- [[wiki/meetings/2025-03-12-business-plan-creator-design]] — 6 AM BPC architecture session; 8 sections, 3 tiers (Idea/Plan/Grow), DeepSeek + Gemini
- [[wiki/meetings/2025-03-26-rick-bough-hays-cisd]] — Rick Bough / Hays CISD CTE; August 2025 PD workshop; strong advocate
- [[wiki/meetings/2025-03-28-monica-davidson-buda-chamber-restaurant-hiring]] — Monica Davidson; restaurant hiring pilot; Crew Day April 11; Shelly Plumlee; podcast
- [[wiki/meetings/2025-04-11-david-levesque-savari-solar]] — David Levesque / Savari; Hungry Hill Foundation lead (East Austin, formerly incarcerated workforce)
- [[wiki/meetings/2025-04-28-hubspot-kickoff-sebastian-full-transcript]] — Full transcript supplement; Alvaro Vilarmarconell (2nd intern); BPC demo details; success metrics
- [[wiki/meetings/2025-05-21-ai-advisory-azure-foundry]] — Paula Florez-Estrada / Microsoft Founders Hub; Azure account disaster; AI Foundry chatbot as #1 AI priority
- [[wiki/meetings/2024-batch-low-signal-calls]] — Batch page: 9 low-signal calls from Oct–Dec 2024 + TXOR April 2025 session

**Pages created (wiki/people/ — 8 new pages):**
- [[wiki/people/enrique-castro]] — GAHCC Director of Membership; "El Taco Financiero" podcast; Univision connections
- [[wiki/people/daniela-castillo-canavera]] — Colombian media professional; Univision/Caracol/RCN media; equity partnership
- [[wiki/people/rick-bough]] — Hays CISD CTE coordinator; August 2025 PD workshop; strong Moil advocate
- [[wiki/people/paula-florez-estrada]] — Azure AI Activation Advisor; 4-month Microsoft Founders Hub engagement
- [[wiki/people/dafne-gutierrez]] — Former Moil marketing; job coaching; voice resume builder testimonial
- [[wiki/people/david-levesque]] — Savari solar AI; Hungry Hill Foundation East Austin connection
- [[wiki/people/zane-gibson]] — TXOR contact; 30+ participant resume-building sessions
- [[wiki/people/abel-esquivel-luna]] — Full page for Zachary Corp anchor enterprise contact

**Pages updated:**
- [[wiki/moil/gtm]] — +11 new channels: GAHCC, TXOR, Hays CISD CTE, Buda restaurant pilot, Spanish-language media, Hungry Hill Foundation, podcasts, Azure AI Foundry chatbot; HubSpot intern updated to include Alvaro Vilarmarconell
- [[wiki/moil/product-roadmap]] — Azure account disaster documented; AI Foundry chatbot as #1 AI priority; BPC 3-tier architecture; MongoDB→Postgres migration; ACS chat integration plans
- [[wiki/moil/customers]] — Zachary Corp + TXOR added to named customers table; Dafne/Rick Bough/Daniela added as product testimonials; group onboarding friction noted
- [[wiki/people/monica-davidson]] — March 2025 restaurant hiring pilot, Crew Day coordination, Shelly Plumlee connection, podcast episode added
- [[index]] — stats updated; Run 2 ingestion summary added

**Key intelligence from Run 2:**
1. **Azure account disaster (May 2025):** Moil's entire Azure subscription disappeared during Google→M365 migration; website down ~1 week; Paula Florez-Estrada escalated
2. **#1 AI priority:** Azure AI Foundry support chatbot (RAG over product docs) — named by Andres on May 21, 2025 call
3. **Business Plan Creator architecture:** 8 sections, 3 tiers, DeepSeek + Gemini — designed March 12, 2025; operational by May 2025
4. **GAHCC channel:** Monica Munoz Andry (CEO) + Enrique Castro ("El Taco Financiero") → Univision/Caracol media pipeline
5. **Hays CISD CTE opportunity:** Rick Bough invited Andres for August 2025 teacher PD; school-to-workforce channel
6. **Hungry Hill Foundation lead:** East Austin workforce re-entry org (homeless/formerly incarcerated); intro via David Levesque
7. **Spanish-language media:** Daniela Castillo Cañavera (Univision/Caracol/RCN) exploring equity partnership
8. **Competitor intelligence:** Skilly reviewed against Moil — Moil advantage: user-friendly, bilingual, AI-native
9. **Enterprise product gaps:** Abel (Zachary) requested multi-user hierarchy, assessments tab, certification tracking
10. **Group onboarding friction:** TXOR April 2025 session (30+ participants) had login issues — product gap for scale

**Summary:** Run 2 revealed the full year of Moil's external relationship-building — community organizations, media channels, enterprise account management, and Microsoft advisory relationships — plus a critical infrastructure crisis (Azure account disappearance) and the AI Foundry chatbot becoming the #1 technical priority. Combined with Run 1's internal team/product intelligence, the Brain now has comprehensive context for Moil's Aug 2024–May 2025 operational history.

---

### [2026-04-12] Microsoft Teams — Full 415-Message Ingestion (Apr 5–12, 2026)

- **File:** raw/teams-2026-04-12.md (OVERWRITTEN — replaces prior 27-message bot-only version)
- **Type:** team-communications (1:1 chats + group chats + channel messages)
- **Messages:** 415 total across 12 threads (181 Andres-Adeleke, 79 Moil Team, 65 Andres-Taiwo, 38 Moil Marketing, 30 Andres-Jacob, 11 Andres-Casey, 3 Mark & Andres, 3 Attendance bot, 2 Landing Page Projects, 1 Monday Collaboration, 1 Eden Discovery, 1 Andres-Abiodun)

**Pages created:**
- [[wiki/meetings/2026-04-06-monday-collaboration-call]] — project alignment call; Planner board created; end-to-end integration push
- [[wiki/meetings/2026-04-09-12-engineering-sprint]] — 4-day sprint: 12+ Claude Code sessions, model cost discovery, Business Coach redesign, PDF/PPT export

**Pages updated (7 people):**
- [[wiki/people/adeleke-tolulope]] — Apr 2026 sprint activity, model cost threads, FB login issue
- [[wiki/people/jacob-oluwole]] — Planner board, customer onboarding, Inna content, power outage, $50 from Andres
- [[wiki/people/taiwo-ola-balogun]] — Meridian full ownership, Stripe integration, credential access issues
- [[wiki/people/abiodun-solomon]] ��� Name correction (Adekanmi not Solomon), content delivery batch, Moil 360 reviews doc
- [[wiki/people/casey-earley]] — Moving to Buda (2051 Cambria, May 16)
- [[wiki/people/travis-sutherland]] — Now a paying customer (travis@zoiwell.com, 1-year Moil 360 license)
- [[wiki/people/inna-benyukhis]] — Content360 delivery client confirmed; May calendar pre-loaded; content loss incident

**Pages updated (3 moil):**
- [[wiki/moil/product-roadmap]] — AI tech stack updated to Apr 2026 (Gemini for images, Qwen paid tier, Grok 4.1 Fast discovery, GPT-5.4 cost spike); feature status refreshed (Business Coach live, Content360 selling, PDF/PPT export, Meridian, Voice Guide)
- [[wiki/moil/gtm]] — 7 new deals documented (Connectex, Alloy, FitLogic, Travis, Jacob Centeno, jilledegs01, Siren Beauty); new channels (direct website builds, content-as-service, WhatsApp/Telegram)
- [[wiki/moil/customers]] �� 8 new customer entries added to named customers table

**Summary page:** [[wiki/summaries/teams-2026-04-12]] — completely rewritten from 27-message structural summary to full 415-message intelligence report

**MEMORY updated:** 25+ new action items across 5 categories (deals, engineering, content, team management, credential security)

**Key intelligence:**
1. **Best month ever:** 4 deals closed in one week (Connectex, Meridian, Alloy closing, FitLogic hiring). Andres: "We are having the best month in our existence!!!"
2. **Development workflow confirmed:** Andres prototypes in Claude Code → shares session link in Teams → Adeleke pulls to staging → tests → pushes to prod
3. **OpenAI cost spike:** `gpt-4o` alias silently upgraded to `gpt-5_4-2026-03-05`. Grok 4.1 Fast ($0.20/$0.50) identified as 30x cheaper replacement
4. **Business Coach redesigned:** Static 22-step wizard replaced with AI-guided onboarding that scrapes websites/PDFs
5. **Abiodun name correction:** Teams shows "Abiodun Adekanmi" not "Abiodun Solomon"
6. **Casey Earley moving to Buda** (May 16, 2026) — deepens HIVE relationship
7. **Credential security risk:** Stripe keys, Supabase passwords, API keys shared in plaintext Teams chat
8. **Team strain signals:** Jacob on 3 weeks of generator power; Taiwo blocked by credentials; Adeleke's FB account locked

**Signal rating: VERY HIGH** — densest operational intelligence source in the Brain to date.

---

### [2026-04-12] OneDrive Transcript Backfill — Run 3 (28 New Files)

- **Files:** 28 files in `raw/meetings/` (transcript backfill of files not downloaded in Run 2)
- **Type:** meeting-transcripts (partner calls, customer calls, marketing calls, team meetings, mobile recordings)
- **Date range of content:** 2024-10-01 through 2025-05-20

**Pages created (10 wiki/meetings/ pages):**
- [[wiki/meetings/2025-05-15-zachary-barker-wyatt-hook-enterprise]] — Enterprise customer call; API integration ($4,250), Tampa Bay prospect, enrollment key/HubSpot workflow
- [[wiki/meetings/2025-05-17-prompt-reviews-bpc-quality]] — BPC quality review; hallucination, vague numbers, Brave API decision for real-time data
- [[wiki/meetings/2024-11-13-txor-moil-partnership-call]] — TXOR partnership established; recurring workshops, caseworker training, live podcast concept
- [[wiki/meetings/2024-11-25-monica-pena-egbi-echo-squad]] — Echo Squad LinkedIn pod onboarding; EGBI partnership; political connections (Velasquez, Fuentes)
- [[wiki/meetings/2024-10-24-julian-sanchez-video-planning]] — Spanish-language FB Live planning; banking+employment for Latinos; Breakout Media
- [[wiki/meetings/2025-05-20-azure-resources-support-call]] — Microsoft support call; Azure tenant mismatch diagnosed as root cause of resource disappearance
- [[wiki/meetings/2024-11-14-virtual-moil-councilman-velasquez]] — Austin City Council meeting; Read AI demo; civic partnership exploration
- [[wiki/meetings/2024-11-27-cardo-resume-building-session]] — Live resume-building session at TXOR/Cardo; Spanish-language; Ricardo Van Arcken coached through Moil
- [[wiki/meetings/2025-01-08-nvidia-inception-onboarding]] — Nvidia Inception accepted; $25K DLI credits; team GenAI/RAG training plan
- [[wiki/meetings/2024-11-27-jacob-abiodun-video-zachary-jobs]] — Zachary Corp 80+ jobs; video content review; first 10 seconds hook problem

**Batch pages created (2):**
- [[wiki/meetings/2024-q4-batch-marketing-calls]] — 14 low-signal files: marketing calls, mobile recordings, testing sessions, dev calls, phone review (Oct 2024–Jan 2025)
- Center for Child Protection (Dec 11, 2024) — EMPTY transcript (2 lines: "Hmm" + "Hello"). Julia Cabin name only. No page created — insufficient content

**Pages created (6 wiki/people/ pages):**
- [[wiki/people/evangeline-sandoval]] — TXOR Austin Site Director; key decision-maker for Moil partnership; first-gen immigrant
- [[wiki/people/monica-pena]] — EGBI; Echo Squad LinkedIn pod; BizTech Clinic speaker coordinator
- [[wiki/people/julian-sanchez]] — Colombian content partner; banking/employment Spanish-language FB Lives
- [[wiki/people/wyatt-hook]] — Platform vendor; API integration ($4,250); sandbox provisioning; enrollment keys
- [[wiki/people/rodney-warner]] — Microsoft ProDirect Support; diagnosed Azure tenant mismatch
- Herlinda Rubalcava — TXOR PIM/case manager (mentioned in TXOR page, no standalone page)

**Pages updated:**
- [[wiki/people/zane-gibson]] — Full TXOR context added: Evangeline Sandoval, Herlinda Rubalcava, partnership timeline from Nov 2024
- [[wiki/moil/gtm]] — +6 new channels: TXOR recurring workshops (with Evangeline context), EGBI Echo Squad, Austin political connections, live hiring podcast concept, Julian Sanchez Spanish content, Nvidia Inception
- [[wiki/moil/product-roadmap]] — BPC quality issues (hallucination, Brave API decision), enterprise API integration pricing and enrollment key architecture, Tampa Bay prospect
- [[MEMORY]] — 13 new action items across enterprise, product, and partnership categories

**Key intelligence from Run 3:**
1. **Tampa Bay city prospect:** Zachary Barker disclosed city of Tampa Bay is evaluating the platform — largest potential enterprise deal documented
2. **Brave API adoption:** Team agreed to use Brave Search API for real-time data in BPC to eliminate hallucination — marks shift from pure LLM generation to RAG
3. **TXOR partnership origin story:** Nov 2024 call with Evangeline Sandoval established recurring workshops and caseworker training — this became Moil's strongest nonprofit channel
4. **Echo Squad = LinkedIn origin:** Monica Pena's LinkedIn engagement pod (Nov 2024) was Andres's first structured LinkedIn strategy — predates the X bookmarks GTM playbook by 18 months
5. **Live hiring podcast:** Pitched to 3 separate partners (TXOR, EGBI, Julian) in Oct-Nov 2024 — shows Andres's multi-channel approach to the same concept
6. **Azure disaster confirmed:** Rodney Warner (Microsoft) confirmed it was a tenant/directory mismatch, not data loss — subscriptions were active but invisible
7. **Nvidia Inception:** Moil accepted into Nvidia Inception program (Jan 2025) with $25K DLI training credits — credibility milestone + training resource
8. **Austin political channel:** Councilman Velasquez (District 3) and Councilwoman Vanessa Fuentes both expressed support for Moil's hiring initiatives
9. **Zachary Corp scale:** 80+ jobs posted through Moil by Nov 2024 — larger than previously documented
10. **Salwa & Roli calls:** Empty/minimal transcripts — Salwa (salwayordi@gmail.com) and Roli (rolicalderin@gmail.com) identities noted but no actionable content

**Summary:** Run 3 completed the full transcript backfill, filling in the Q4 2024 partnership-building period that was missing from Run 2. The Brain now has comprehensive meeting coverage from Oct 2024 through May 2025. Most valuable discoveries: Tampa Bay enterprise prospect, Brave API adoption decision, TXOR partnership origin story, and the Echo Squad as Andres's LinkedIn strategy genesis. Combined with Runs 1 and 2, all 78 raw/meetings/ files are now fully ingested.

---

### [2026-04-13] Run 4 — Clients & Customers Rebuild

**Trigger:** Andres identified that April 2026 clients had no wiki pages, customers.md had no GitHub links, and several people pages had wrong tags.

**Sources cross-referenced:** [[raw/teams-2026-04-12]], [[raw/email-history-2months-2026-04-12]], [[raw/imessages-people-2026-04-09]], [[raw/github-project-tracker.md]]

**Pages created (12 new):**
- [[wiki/orgs/connectex]] — Connectex Solutions (Mark Polanco, CLOSED Apr 9, multi-quarter invoice)
- [[wiki/orgs/fitlogic]] — FitLogic (fitness hiring, first hire imminent Apr 12)
- [[wiki/orgs/siren-beauty]] — Siren Beauty & Wellness (Becky Torres, setup in progress)
- [[wiki/orgs/pure-serenity]] — PureSerenity (jilledegs01, Moil 360 onboarded Apr 10)
- [[wiki/orgs/urbanozuela]] — Urbanzuela (Ana Vetencourt, sister-in-law's business)
- [[wiki/orgs/nuovo-entertainment]] — Nuovo Entertainment (site deployed Apr 9)
- [[wiki/orgs/meridian-buda]] — Meridian Buda (coffee/music venue, CLOSED Apr 9, full events platform)
- [[wiki/orgs/alloy-atx]] — Alloy ATX (gym, Content360 + Moil 360, CLOSING Apr 11)
- [[wiki/people/becky-torres]] — Siren Beauty owner
- [[wiki/people/roxana-yglesias]] — Alloy ATX contact
- [[wiki/people/jacob-centeno]] — Titan Tech Authority (Starter plan, CLOSED Apr 8)
- [[wiki/people/ana-vetencourt]] — Andres's sister-in-law, Urbanzuela owner

**Pages fixed (4 corrections):**
- [[wiki/people/mark-polanco]] — corrected from person/personal to person/customer; added Connectex context (mark@connectex.net)
- [[wiki/people/wyatt-hook]] — corrected from person/customer to person/vendor
- [[wiki/moil/customers]] — added wikilinks + GitHub repo links for all 11 April 2026 clients
- [[wiki/orgs/README]] — rebuilt index with all 12 current org pages

**Summary:** Run 4 rebuilt the clients and customers layer from scratch using Apr 2026 data. The 8 active Moil-Landingpages repos now all have corresponding wiki pages. All April 2026 closed/closing deals are properly documented and linked. Two mis-tagged people pages corrected. customers.md now connects every client to their wiki page and GitHub repo.

---

### [2026-04-13] Run 5 — Monday Collaboration Transcript (Apr 13)

**Trigger:** New unprocessed file detected in raw/: `teams-transcript-monday-collaboration-2026-04-13.md`

**Source:** [[raw/teams-transcript-monday-collaboration-2026-04-13]] — Full VTT transcript of Monday Collaboration call (8:17am–10:00am CT), organized by Jacob Oluwole, all 5 team members present.

**Pages created (1 new):**
- [[wiki/meetings/2026-04-13-monday-collaboration]] — Full meeting record with decisions, action items, and blockers

**Pages updated (8):**
- [[wiki/people/inna-benyukhis]] — CRM bugs surfaced (contacts not reading, campaigns API key missing), meeting confirmed for 10am today
- [[wiki/people/jacob-oluwole]] — Organized meeting; assigned Google Alloy image gen testing before Andres's Apr 14 meeting
- [[wiki/people/adeleke-tolulope]] — PDF/PPTX generation first test done (formatting WIP); pushed staging updates for Business Coach
- [[wiki/people/abiodun-solomon]] — Content behind schedule; testing Business Coach; reiterated testing-notes requirement from Friday
- [[wiki/people/taiwo-ola-balogun]] — Three high-priority items: Meridian Stripe webhook blocker, client handoff document, new massage place client
- [[wiki/people/travis-sutherland]] — Sun Show event next week; Moil will have a demo table
- [[wiki/orgs/meridian-buda]] — Stripe webhook URL blocker documented; Vercel cron secrets using placeholders
- [[wiki/moil/customers]] — (no change needed; massage place client unnamed)

**Key intelligence:**
- **BLOCKER:** Meridian ticket emails dead — Stripe webhook URL not configured + Vercel cron secrets are placeholders
- **BLOCKER:** Inna CRM contact pipeline not displaying + campaigns API key missing (before 10am meeting)
- **Decision:** Brain repos to be cloned for each team member once stable
- **Decision:** Content must be Friday-ready; Mondays are for strategizing
- **Decision:** Client handoff doc required (Vercel, Supabase, Resend, login instructions)
- **New client:** Massage place (unnamed) — website nearly done, needs images
- **Opportunity:** Google Alloy image gen — if it works inside Moil, can charge clients without extra integration work
- **Event:** Moil showcasing at Sun Show next week (Travis Sutherland's event)
- 12 action items assigned across 5 team members (see meeting page)

**Summary:** Ingested the Apr 13 Monday Collaboration transcript — one new meeting page, eight wiki pages updated. Two active blockers (Meridian Stripe webhook, Inna CRM), three key decisions, and a new unnamed massage place client.

---

## How to add an entry

Claude Code automatically appends to this file at the end of each `/kb compile` run. You do not need to edit this manually.

To ingest a new source:
1. Drop the file into `~/My Brain/knowledge-base/raw/`
2. Open Claude Code in `~/My Brain/`
3. Type: `ingest the new source in raw/`
4. Claude Code reads the source, creates/updates wiki pages, and logs the run here

---

### [2026-04-14] Run 6 — Active Client + HIVE Batch

**Trigger:** Manual ingestion run — 12 raw HIVE/client files + 6-month email history.

**Organization principle applied:** All pages tagged with P1 (status: active), P2 (status: warm), or P3 (status: archived) + last_contact dates.

---

**BATCH 1 — Active Clients:**

- **raw/hive-siren-beauty-wellness-strategy-plan.md** → [[wiki/people/becky-torres]] (deal timeline confirmed; $2,200 paid Apr 6), [[wiki/orgs/siren-beauty]] (full website redesign strategy: Next.js 15 + Sanity CMS + AEO + 6-phase roadmap)
- **raw/hive-inna.md + hive-inna-s-website-feedback.md + hive-empowered-nutrition-project-breakdown.md + hive-coaching-session-summary.md** → [[wiki/people/inna-benyukhis]] (full business profile: SFM practitioner, women 40+, $15K+ wasted marketing history, 6-module AI website plan)
- **raw/email-history-6months-2026-04-14.md** → [[wiki/people/megan-miller]] (full rebuild: NP/hormone expert, meganmillernp@gmail.com, onboarding Apr 1), [[wiki/moil/pipeline]] (full rebuild with all Apr 2026 closed deals), [[wiki/moil/customers]] (complete P1/P2/P3 rewrite — 13 active clients)

**BATCH 1 — HIVE Program:**

- **raw/hive-buda-hive-sosx-run-of-show.md** → [[wiki/orgs/buda-edc]] (SoSX event Mar 12, 2026 — Andres as named Incubator Strategist; 4 cohort graduates; Jennifer Storm = IEDC Economic Developer of the Year)
- **raw/hive-series-based-hive-program.md** → [[wiki/concepts/hive-program]] (NEW — 4-stage curriculum: Hatch/Initiate/Validate/Expand)
- **raw/hive-coaching-session-summary.md** → integrated into Inna profile + Anita Lansing

**BATCH 2 — Key 2025 Meetings:**

- **raw/odtr-20241120...Echo-Squad...** → [[wiki/orgs/echo-squad]] (NEW — Monica Pena's LinkedIn pod, <10 people, Thursday 9–10 AM, Dec 2024–Feb 2025)
- **raw/odtr-20250515...Zachary-Barker-and-Wyatt-Hook...** → [[wiki/people/zachary-barker]] (NEW — CEcD, multi-city EDC operator; Tampa Bay expansion signal validates Moil B2G thesis)
- **raw/odtr-20250521...Moil-Enterprise-AI-Advisory...** → [[wiki/meetings/2025-05-21-moil-enterprise-ai-advisory]] (NEW — Azure account disaster: GWS→M365 migration wiped entire directory; AI Foundry deferred)
- **raw/odtr-20241125...Monica-Pena... + raw/odtr-20250411...David-Andres... + raw/odtr-20250205...Jacob-Andres...** → existing pages confirmed/updated (source refs added)

**Pages created (4):** [[wiki/concepts/hive-program]], [[wiki/orgs/echo-squad]], [[wiki/people/zachary-barker]], [[wiki/meetings/2025-05-21-moil-enterprise-ai-advisory]]

**Pages updated (8):** [[wiki/people/becky-torres]], [[wiki/people/inna-benyukhis]], [[wiki/people/megan-miller]], [[wiki/orgs/siren-beauty]], [[wiki/orgs/buda-edc]], [[wiki/moil/customers]], [[wiki/moil/pipeline]], [[wiki/people/anita-lansing]]

**Summary:** Run 6 confirmed 13 active paying P1 clients in April 2026. Rebuilt customers.md and pipeline.md with importance × recency structure. Key intelligence: Siren Beauty full website project scope, Inna's $15K+ wasted marketing backstory, Zachary Barker's Tampa Bay signal for B2G thesis, Azure account disaster context.


### 2026-04-14 — Data-quality cleanup + MEMORY.md archive migration

- **Type:** maintenance
- **Summary:** Fast-win audit fixes. Deduplicated raw/ (38 MD5-identical files removed, all from raw/onedrive-transcripts/). Renamed Cyrillic `buda-hive-edс-2026-04-09.md` → `buda-hive-edc-*` (ASCII). Consolidated two x-bookmarks duplicate pairs (kept the deeper 129-item version, now canonical name). Fixed 41 escape-broken wikilinks (`[[target\|Display]]` → `[[target|Display]]`) across ANDRES.md, customers.md, pipeline.md. Corrected index.md stats: now 190 wiki pages / 192 raw sources (was claiming 213/91).

### Archive — May 2025 historical verify items (moved here from MEMORY.md 2026-04-14)

These were flagged from Aug 2024–May 2025 meeting transcripts ingested Apr 12. Moved out of MEMORY.md to keep it under the 200-line rule. If any become active, promote back to MEMORY.md.

- Azure access for Adeleke (~May 2025 support case)
- Job matching algorithm weighted update (Adeleke Apr 2025)
- Google → Microsoft migration (deadline May 5, 2025)
- HubSpot full access for Jacob (after May 15, 2025)
- Business Plan Creator bugs: personas, TAM/SAM, competitor map, cost structure, milestones, plan display
- Interview Tool MVP (Andres said "build without design first" — May 2025)
- Social post auto-generation on job creation (Grok + template)
- Sebastian Oviedo 4-week marketing engagement (Apr 28–May 26, 2025)
- Manos De Cristo workshops (June 2025 — 3 Fridays)
- Sakuri Corporation Texas job listings (Jacob assigned)
- Zachary/Great Construction Corp account status
- UTSA license opportunity via EDC contact
- Tampa Bay (Zachary Barker) enterprise evaluation — see [[wiki/meetings/2025-05-15-zachary-barker-wyatt-hook-enterprise]]
- $4,250 API integration (Wyatt Hook / Josh Edmond) — decision?
- Sandbox access for Tampa Bay testing — provisioned?
- Brave Search API for BPC hallucination reduction — implemented?
- Azure directory tenant mismatch (Rodney Warner) — restored?
- TXOR recurring workshops (Evangeline Sandoval, Nov 2024)
- TXOR caseworker training (proposed Nov 2024)
- Live hiring podcast (TXOR + EGBI + Julian Sanchez, Oct–Nov 2024)
- EGBI Echo Squad LinkedIn pod (Nov 2024–Feb 2025)
- Julian Sanchez FB Live Spanish content (late Oct 2024)
- Councilman Velasquez / Vanessa Fuentes civic initiatives
- Nvidia Inception credits (25 DLI, received Jan 2025)

---

### [2026-04-14] Run 7 — Roxana Onboarding + HIVE Curriculum Batch + Low-Signal Cleanup

**Trigger:** Automated scan for unprocessed raw files. Found 27 new files — 1 high-priority meeting transcript, 1 medium-priority HIVE session, 11 HIVE curriculum files, 8 HIVE week handouts, 4 low-signal meeting transcripts, 2 empty Teams pulls.

---

**HIGH PRIORITY — New meeting transcript:**

- **File:** raw/teams-transcript-roxana-andres-2026-04-14.md
  - **Type:** customer-onboarding (Teams call, 90 min)
  - **Pages created:** [[wiki/meetings/2026-04-14-roxana-alloy-atx-onboarding]]
  - **Pages updated:** [[wiki/people/roxana-yglesias]], [[wiki/orgs/alloy-atx]], [[wiki/moil/customers]], [[MEMORY]]
  - **Summary:** Roxana Yglesias / AlloyATX closed on Moil 360 Market Pro at $75/mo. Full onboarding: asset handover from previous agency (Shannon/Gabriel), 21-question market research flow, satellite landing pages on GoDaddy domains, Spanish-language pages, wellness referral network. 11 action items assigned.

**MEDIUM PRIORITY — HIVE post-cohort session:**

- **File:** raw/hive-cohort-onboarding-session-feb13-2026.md
  - **Type:** hive-group (whisper transcript, 15 min)
  - **Pages created:** [[wiki/meetings/2026-02-13-hive-life-after-cohort-session-2]]
  - **Summary:** Post-cohort onboarding for Liz and Miguel (Buda residents). Server was down; couldn't demo. Miguel hit candidate-vs-business account confusion twice. Rescheduled to Feb 14.

**BATCH — HIVE curriculum files (11 files → enriched existing concept page):**

- **Files:** raw/hive-camp.md, raw/hive-entrepreneur-camp.md, raw/hive-entrepreneur-camp-notes.md, raw/hive-grok-guide-and-talking-points.md, raw/hive-1-or-2-day-intensive-hive-entrepreneurial-program.md, raw/hive-hybrid-hive-entrepreneurial-program.md, raw/hive-buda-hive-flexible-networking-content.md, raw/hive-emails-for-hive.md, raw/hive-emails-for-hive-1.md, raw/hive-ai_panel_presentation_guide_long_version.md, raw/hive-hive_week_1_handout_you_as_entrepreneur.md through raw/hive-hive_week_8_handout_launch_preparation.md (8 handouts)
  - **Type:** program-curriculum / reference material
  - **Pages updated:** [[wiki/concepts/hive-program]] (added Entrepreneur Camp June 2025, program format variants table, Grok guide mention)
  - **Summary:** These are HIVE curriculum design documents — program format variants (series, intensive, hybrid), Entrepreneur Camp presentation notes (Andres + Joshua Edmond, June 18 2025), Grok guide for entrepreneurs, weekly handout content (weeks 1–8), email templates, networking content, and AI panel presentation guide. No new people or action items — all reference material that enriches the existing HIVE concept page.

**LOW-SIGNAL — Logged but no new pages:**

- **raw/odtr-20250519-Moil-Marketing-Call-Notes-by-Gemini.md** — Garbled XML/DOCX content from Gemini auto-notes. Jacob + Adeleke had technical difficulties. No decisions or actions. Already covered by [[wiki/meetings/2025-05-19-moil-marketing-call-technical-issues]].
- **raw/odtr-20250422-20250422-TXOR-Moil-Resume-Building-Presentation-Tr.md** — Short snippet of a TXOR virtual workshop. Zane Gibson + ~35 invited participants. Login troubleshooting. Already covered by existing TXOR pages.
- **raw/odtr-20250410-20250410-David-and-Andres-AI-trees-Transcript.md** — David Levesque demoing a solar/battery optimization tool built with ChatGPT. Personal/side project, not Moil business. No actions.
- **raw/odtr-20250520-20250520-All-Resources-Transcript.md** — Rodney Warner (Microsoft ProDirect Support) follow-up on Azure tenant mismatch. Already covered by [[wiki/meetings/2025-05-20-azure-resources-support-call]].

**EMPTY — No content to ingest:**

- **raw/teams-2026-04-14.md** — 429 rate limit error from Graph API. Zero messages pulled.
- **raw/teams-history-6months-2026-04-14.md** — Empty file. Only header, no content.

**Key intelligence from Run 7:**
1. **AlloyATX deal closed:** $75/mo Market Pro — confirmed paying P1 customer
2. **AEO strategy introduced:** Andres pitched AI Engine Optimization (Q&A on every page so AI assistants can reference the business) — this is a new positioning angle beyond traditional SEO
3. **Satellite landing page playbook:** Low-cost SEO strategy using existing GoDaddy domains; Spanish-language variant for bilingual markets — repeatable for other clients
4. **Wellness referral pipeline:** Roxana has functional medicine + Colombia regenerative medicine contacts — potential multi-customer funnel
5. **HIVE Entrepreneur Camp:** June 2025 event with Joshua Edmond at Buda HIVE confirmed — key public event for Moil/HIVE partnership visibility
6. **Onboarding UX friction persists:** Miguel (Feb 2026) hit candidate-vs-business account confusion — same issue documented in earlier TXOR sessions

**Summary:** Run 7 ingested 27 files. The AlloyATX onboarding call was the highest-signal source — a confirmed deal with 11 action items and a wellness referral pipeline. HIVE curriculum files enriched the existing concept page with program format variants and Entrepreneur Camp details. Four low-signal transcripts logged for completeness. Two empty files skipped.

---

### [2026-04-15] Run 8 — Daily Ops Ingestion (7 files)

**Trigger:** Automated scan for unprocessed raw files.

---

**HIGH PRIORITY — Teams daily operations (Apr 14–15):**

- **File:** raw/teams-2026-04-15.md
  - **Type:** team-communications (84 messages, 4 threads)
  - **Pages created:** [[wiki/meetings/2026-04-15-teams-daily-ops]]
  - **Pages updated:** [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/abiodun-solomon]], [[wiki/moil/product-roadmap]], [[wiki/moil/customers]], [[MEMORY]]
  - **Summary:** API cost crisis — token refills 3x/week (was monthly). Full codebase audit ordered to migrate gpt-4o→gpt-5-mini. License distribution push for 5 clients. FitLogic deadline set for Fri Apr 18. Andres issued team-wide urgency message about delivery pace. Buda EDC called about "their product." New unnamed social media client signed.

**MEDIUM PRIORITY — Email digest (Apr 14):**

- **File:** raw/email-digest-2026-04-14.md
  - **Type:** email-digest (24-hour window)
  - **Pages created:** [[wiki/people/renee-simmons]] (Hays CISD, Career Day May 7), [[wiki/people/adam-maxon]] (Pflugerville Mentor Day)
  - **Pages updated:** [[wiki/moil/customers]] (Daniel Guadiano meeting confirmed Thu Apr 16), [[MEMORY]] (7 new action items)
  - **Summary:** Daniel Guadiano/Astra confirmed Thursday meeting. Renee Simmons invited Andres to Career Day May 7 (CHES, 4th/5th graders). Adam Maxon invited to Pflugerville Mentor Day. Buda Retail Roundup Apr 20. 15 chamber breakup emails sent (pipeline hygiene). GitHub webhook secrets rotation needed.

**MEDIUM PRIORITY — SEO Implementation Plan:**

- **File:** raw/odtr-moilapp_SEO_Implementation_Plan_April2026.md
  - **Type:** technical-plan (dated Apr 8, 2026)
  - **Pages created:** [[wiki/concepts/seo-implementation-plan]]
  - **Pages updated:** [[wiki/moil/product-roadmap]] (SEO roadmap reference added)
  - **Summary:** Comprehensive 4-phase SEO roadmap. Only 13/68 pages indexed. Critical fix: `?lg=` URL pollution. Highest-ROI: JobPosting schema for Google Jobs carousel. Blog keyword targets identified. Subdomain consolidation recommended.

**MEDIUM PRIORITY — 9-Month Email History:**

- **File:** raw/email-history-9months-2026-04-15.md
  - **Type:** email-digest (Jul 2025–Apr 2026, 2000 emails, 875 unique contacts)
  - **Pages created:** none (confirms existing relationships)
  - **Summary:** Confirms relationship intensity: Jacob (39 emails), Casey Earley (33), Anita Lansing (29), Megan Miller (26), Becky Torres (23), Buda HIVE (23), Jacquie Martinez (17), Inna (15), Monica Davidson (15), Mark Polanco (15). New signals: Kim Dowers/Queen Creek Chamber (13 emails — active), Daniel/Evermend Group (13 — warm intro pipeline), Jesutomilola/Google xWF (9 — Google Cloud workshop), Katherine Silvas/Helotes (9 — confirming overdue reply flagged in MEMORY). Stripe payment confirmations: $2,200 from Siren Beauty, $200 payments from Alia Wells and Juan Costilla.

**LOW PRIORITY — Business Plan (Mar 2026):**

- **File:** raw/odtr-Moil_Enterprise_business_Plan.md
  - **Type:** business-plan (Mar 5, 2026)
  - **Pages updated:** none (numbers already reflected in positioning/gtm from earlier ingestion of moil-documents-2026-04-09)
  - **Summary:** Updated March 2026 business plan. Confirms: 500+ active businesses, 5,000+ jobs/month, 94% interview success rate, $850 avg cost per hire, 91% 90-day retention. Pricing: Starter $15, Professional $25, Market Pro $75. Largely duplicates content already ingested via moil-documents.

**LOW PRIORITY — Nonprofit Incorporation Steps:**

- **File:** raw/odtr-Moil_Nonprofit_Incorporation_Steps.md
  - **Type:** reference (Jan 2025)
  - **Pages created:** none
  - **Summary:** 8-step incorporation guide for "Moil Empowerment Foundation" nonprofit (501(c)(3)). Historical reference — no indication this has been acted on. Steps: name verification, Certificate of Formation (TX), EIN, bylaws, IRS Form 1023, bank account, TX Comptroller registration, initial programs.

**LOW PRIORITY — Claude Code Weekly Sessions Rollup:**

- **File:** raw/weekly-sessions-2026-04-15.md
  - **Type:** claude-code-weekly-rollup (week of Apr 12)
  - **Pages created:** none
  - **Summary:** 8 Claude Code sessions, 82 user messages, 425 assistant responses, 1092 tool calls, 105 files created, 38 commits. Sessions include: wiki README creation, CLAUDE.md init, KB audit sprint (Apr 13), Brain system audit (Apr 14). Captures the burst of KB infrastructure work this week.

**Pages created (4):** [[wiki/meetings/2026-04-15-teams-daily-ops]], [[wiki/people/renee-simmons]], [[wiki/people/adam-maxon]], [[wiki/concepts/seo-implementation-plan]]

**Pages updated (8):** [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/abiodun-solomon]], [[wiki/moil/product-roadmap]], [[wiki/moil/customers]], [[MEMORY]], [[index]]

**Key intelligence from Run 8:**
1. **API cost crisis:** OpenAI token spend exploded 3x — full audit + migration to gpt-5-mini ordered
2. **License distribution push:** 5 clients getting Moil 360 invitations today (Megan, Mark, Becky, Roxana, Jill)
3. **FitLogic Friday deadline:** Must complete by Apr 18
4. **Astra Restaurant meeting confirmed:** Daniel Guadiano, Thu Apr 16
5. **Career Day May 7:** Renee Simmons, Hays CISD — new community channel
6. **Pflugerville Mentor Day:** Adam Maxon — new market adjacent to Austin/Buda
7. **SEO crisis quantified:** Only 13/68 pages indexed; JobPosting schema = highest-ROI fix
8. **Team delivery tension:** Andres issued direct accountability message to entire team
9. **Buda EDC product call:** EDC reached out to discuss product — may relate to Board vote outcome
10. **9-month email confirms relationship map:** Top contacts all match existing wiki pages; no major gaps

**Summary:** Run 8 processed 7 files. The Teams daily ops was the highest-signal source — an API cost crisis requiring immediate action plus a license distribution push across 5 clients. The SEO implementation plan is a significant new concept page documenting moilapp.com's technical debt. Email digest surfaced two new community contacts (Renee Simmons, Adam Maxon) and confirmed the Daniel Guadiano/Astra meeting for Thursday. The 9-month email history confirms the existing relationship graph with no major gaps.

---

### [2026-04-16] Run 9 — Email Digest Apr 15

**Trigger:** Automated scan for unprocessed raw files. One new file: `raw/email-digest-2026-04-15.md` (committed Apr 15 by `email-digest` job, not yet ingested into wiki).

---

- **File:** raw/email-digest-2026-04-15.md
  - **Type:** email-digest (24-hour window, Apr 14–15)
  - **Pages created:** [[wiki/people/joseph-arnke]] (GIS WebTech; added Andres to Buda EDC AI-tools call)
  - **Pages updated:** [[wiki/people/john-costilla]] (EDC AI-tools call follow-through; status bumped archived → active), [[wiki/people/jesutomilola-omoniyi]] (reply overdue — 2 Apr 15 follow-ups), [[wiki/people/jacob-centeno]] (partnership signal — volunteered referrals), [[wiki/people/jacquie-martinez]] (sent Cohort 4 onboarding email Apr 15), [[wiki/people/rosemary-gamez]] (Rise & Shine thank-you; status archived → active), [[wiki/orgs/buda-edc]] (EDC AI-tools call section added), [[wiki/moil/gtm]] (Apr 15 outbound update + EDC product-expansion channel), [[MEMORY]] (Jesutomilola reply + EDC AI-tools call actions; pruned 2 stale Open-PR items), [[index]] (stats refreshed)

**Key intelligence from Run 9:**
1. **Buda EDC AI-tools call emerging (Apr 15):** John Costilla emailed "Call today"; Joseph Arnke (GIS WebTech, joe@giswebtech.com) added Andres to the invite. Direct follow-through on John's Apr 10 "Agentic AI / always-on site selector tool" signal. Potential B2G product-expansion channel — embed Moil AI in EDC website infrastructure, replicable to other EDCs.
2. **Google xWF relationship at risk of stalling:** Jesutomilola Omoniyi sent two follow-ups in one day ("Let's connect by phone or chat — email not best way"). Reply is now overdue and relationship value (Google Cloud credits parallel to Nvidia Inception) is non-trivial.
3. **Jacob Centeno → referral partner:** Existing $15/mo customer volunteered Apr 15 to refer businesses needing social-media + Moil help. First customer-turned-channel signal.
4. **Rise & Shine attendance confirmed:** Andres attended Greater Buda Chamber's Tuesday Apr 14 event at The HIVE. Rosemary Gamez sent thank-you Apr 15. Buda Chamber relationship is live (was previously marked archived).
5. **Jacquie Martinez — Cohort 4 onboarding live:** Sent "Your Cohort Journey Begins Soon" email Apr 15. Cohort 4 launch (Apr 20) is actively being staged.
6. **Outbound single-day record:** 25 sent emails Apr 15 — 8 breakup emails (first large pipeline-hygiene batch), 4 discovery, 5 pitch, plus meeting invites to Roxana and Megan. Massachusetts expansion (6 new targets) — first MA push in the cold campaign.
7. **Dead ends logged:** Sherese D. James-Grow (Boca Chamber) redirected — only handles teens.
8. **Tax/personal admin not promoted:** DLC Financial (Austin Duke, Brendan C. Dunaway) tax return + Mariana Rodriguez questionnaire forward — personal admin, no wiki pages created.

**Summary:** Single-file digest run. The highest-signal item is the Buda EDC AI-tools-for-website call — a concrete product-expansion opening that directly extends the existing B2G relationship and, if it lands, replicates as a template. Second-highest: the Google xWF (Jesutomilola) relationship needs a reply to avoid stalling. One new person page (Joseph Arnke), six people updated, two stale "archived" people (John Costilla, Rosemary Gamez) reactivated based on current contact.

---

### [2026-04-17] Run 10 — Weekly compile + email digest Apr 16

**Trigger:** Weekly KB compile. One new raw file detected: `raw/email-digest-2026-04-16.md` (committed Apr 16 by `email-digest` job). Meta-reference file `raw/brain-knowledge-layer-analysis.md` also noted; no wiki content ingested — superseded by existing [[wiki/concepts/llm-knowledge-bases]] and [[wiki/concepts/brain-architecture]].

- **File:** raw/email-digest-2026-04-16.md
  - **Type:** email-digest (24-hour window, Apr 15–16)
  - **Pages created:** [[wiki/people/mayra-adams]] (Helotes EDC exec secretary / schedule gatekeeper)
  - **Pages updated:** [[wiki/people/katherine-silvas]] (call locked Wed Apr 22 @ 10am CT; status warm → active), [[wiki/orgs/helotes-edc]] (Apr 22 call added to engagement timeline; status warm → active), [[wiki/people/john-costilla]] (Apr 16 EDO professional-association forward from Katie Milton Jordan), [[wiki/people/jesutomilola-omoniyi]] (source ref added; reply still overdue), [[wiki/people/jacob-centeno]] (last_contact bump), [[wiki/moil/gtm]] (Apr 16 single-day outbound: ~25 emails across narrative-pitch template + second breakup wave; GA/MI/MS/CT/ON/TX clusters), [[MEMORY]] (Helotes "reply overdue" auto-resolved + Apr 22 call action moved to Next 2-3 weeks; Jacob Centeno referral partnership logged; Daniel Guadiano Apr 16 meeting struck), [[index]] (escaped-pipe wikilink fixed: `wiki/moil/directory\|Directory` → `wiki/moil/directory|Directory`)

- **File:** raw/brain-knowledge-layer-analysis.md
  - **Type:** meta-reference (Brain gap analysis vs Shann Holmberg's two-layer AI Knowledge Layer framing)
  - **Pages created:** none
  - **Summary:** Self-reflective gap analysis against @shannholmberg's framework. Maps Brain against four commands (`/wiki-ingest`, `/wiki-query`, `/wiki-explore`, `/wiki-lint`), identifies Web Clipper as the top missing piece, and proposes a morning-ingest automation. Largely superseded by the existing [[wiki/concepts/llm-knowledge-bases]] (Karpathy pattern) + [[wiki/concepts/brain-architecture]]. Content is an improvement roadmap for the Brain itself — not external knowledge to ingest. Logged only.

**Weekly compile outputs:**
1. **MEMORY.md priority rot cleanup:** Helotes EDC item in "🔥 Immediate — This Week" (Mar 31 date-label, 17 days old → >14-day rule) auto-resolved to Closed/Archive; replaced with Apr 22 call action in "Next 2–3 weeks". Daniel Guadiano Apr 16 meeting struck (past). Jacob Centeno referral partnership added to "Next 2–3 weeks". Last-updated date bumped to 2026-04-17. MEMORY.md now 204 lines (vs 200-line soft cap — trim next compile).
2. **Wiki freshness audit:** Zero pages with "Last updated" > 60 days AND zero inbound wikilinks. 17 pages lack a "Last updated" field (READMEs, index). No pages tagged `stale: true`.
3. **Link integrity (index.md):** 54 unique wikilinks scanned. 1 structural break fixed (escaped-pipe on `wiki/moil/directory`). 1 false-positive (`[[wiki/folder/slug]]` example text). All other index.md wikilinks resolve to existing files.

**Key intelligence from Run 10:**
1. **Helotes EDC call locked:** Wed Apr 22 @ 10am CT. Kate Silvas looped in [[wiki/people/mayra-adams|Mayra Adams]] as scheduler. Second EDC incubator partnership moving from "strategic planning" to concrete proposal.
2. **Outbound narrative-pitch template now in rotation:** "Something we didn't expect" / "Interesting feedback from an EDC" sequence (Dylan Horne, Ralph Staffins, Stacy Bowerman, Nancy Palmer) running in parallel with breakup cadence — first deliberate A/B signal in the cold campaign.
3. **Jacob Centeno referral channel = new GTM lane:** Customer-turned-referral-partner confirmed by Apr 16 thank-you reply. First codified customer-as-channel.
4. **Geographic footprint expanding:** Apr 16 push touched Ontario (Canada), Connecticut, Michigan, Mississippi, Georgia — breakup batch targeting Moil's weakest-engagement regions.
5. **KB health is strong:** 0 stale orphans across 241 pages. All "Last updated" fields within the last 60 days — the daily digest loop is doing its job.

---

### [2026-04-17] Run 11 — KidsGPT / Luna Brain planning docs

**Trigger:** Automated scan for unprocessed raw files. Found 3 unprocessed files in `raw/KidsGPT/` (planning docs for Andres's personal family-AI project — flagged in [[wiki/projects/magical-reading-adventures]] as unpromoted) plus 10 `.txt` files in `raw/onedrive-transcripts/` that are actually binary MP4 recordings misnamed with `.txt` extension (not ingestible as text; skipped and logged below).

**Files processed:**

- **raw/KidsGPT/README.md** (1.4 KB) — Luna Brain one-pager
- **raw/KidsGPT/options-analysis.md** (6.8 KB) — Five architecture options for the family-AI companion
- **raw/KidsGPT/implementation-plan.md** (23 KB) — Full phased build plan (Weeks 1–7+), Supabase schema, system prompts, cost model

All three frontmatters marked `ingested: true` / `ingested_at: 2026-04-17`.

**Pages created (1):**
- [[wiki/summaries/kidsgpt-planning-2026-04]] — structured summary of the three planning docs

**Pages updated (3):**
- [[wiki/projects/lunabella]] — replaced the one-paragraph stub with full Luna Brain project page (architecture, naming ceremony, bilingual design, safety model, phase roadmap, cost model, Supabase schema, curriculum intelligence — all sourced from `raw/KidsGPT/`). Confirmed `Felipeu28/Lunabella` GitHub repo = the Luna Brain engineering surface ("Lunabella" = Luna + Annabella)
- [[wiki/projects/magical-reading-adventures]] — closed the "is this KidsGPT?" open question; now links forward to [[wiki/projects/lunabella]] as the destination of the KidsGPT concept
- [[wiki/moil/active-projects]] — Tier 3 row updated: "KidsGPT concept / Raw files not yet promoted" → "Luna Brain (Lunabella) / Phase 1 building"

**Key intelligence:**
1. **Luna Brain is one app, two profiles** — Annabella (age 7) and Evie (age 5), each with separate brains, separate Lunas, separate curricula. Not a prototype — per-profile scoping is baked into the Supabase schema from Day 1.
2. **Stack locked:** React/Vite + Fastify + Supabase + Claude `claude-sonnet-4-6` + ElevenLabs + ntfy.sh + Resend. Deploys on Vercel (frontend) + Railway (API). iPad-first portrait.
3. **Architectural parallel to the Moil Brain:** Same two-layer memory model — episodic transcripts → semantic knowledge graph. End-of-conversation ingestion (not per-message) mirrors how the Moil Brain ingests raw sources.
4. **Safety model uses Claude specifically** because it carries a Minimal Risk rating for kids (vs GPT's High Risk per the options-analysis). Hard-block topics route to "ask your parents" and push-notify Andres via ntfy.sh within 60s.
5. **Bilingual (EN + ES) is foundational, not bolt-on** — system prompt auto-detects language, code-switches naturally, brain-node schema has `label_en` + `label_es` with topic collapsing ("espacio" = "space" = same node). "Practice Spanish" parent override planned.
6. **Curriculum intelligence (Phase 4, Weeks 5–6)** is the most distinctive feature — Andres uploads the school curriculum PDF once per school year per profile, Claude parses it to structured JSON, Luna's system prompt gets a confidential reference block, parent dashboard gains a coverage map + gap prompts ("Try asking Luna about multiplication — Annabella hasn't touched it yet"). School-year-end report visualizes natural curiosity vs. required curriculum.
7. **Cost model:** ~$15–20/month. Fits comfortably inside Andres's existing Anthropic billing.
8. **Status as of 2026-04-15:** `Felipeu28/Lunabella` TypeScript repo is active, last push 2026-04-15. Planning phase is complete. Next unblocks: Supabase project creation, ElevenLabs API key, domain decision.

**Skipped files (unprocessable):**

- `raw/onedrive-transcripts/kim-dowers-intro-call-2026-02-09.txt` (685 KB)
- `raw/onedrive-transcripts/life-after-cohort-moil-2026-02-10.txt` (9.1 MB)
- `raw/onedrive-transcripts/life-after-cohort-moil-2026-02-13.txt` (25 MB)
- `raw/onedrive-transcripts/moil-marketing-call-2026-03-11.txt` (1.4 MB)
- `raw/onedrive-transcripts/moil-team-meeting-2026-01-29.txt` (4.8 MB)
- `raw/onedrive-transcripts/moil-team-meeting-2026-03-27.txt` (6.3 MB)
- `raw/onedrive-transcripts/rashaka-boykins-intro-call-2026-02-27.txt` (1.4 MB)
- `raw/onedrive-transcripts/rashaka-boykins-intro-call-2026-03-05.txt` (1.5 MB)
- `raw/onedrive-transcripts/roxana-esquivel-intro-call-2026-03-13.txt` (4.7 MB)
- `raw/onedrive-transcripts/travis-&-andres-moil360-2026-04-09.txt` (1.5 MB)

All 10 files have MP4 `ftypisom` binary headers — they are raw video recordings from OneDrive that were misnamed with a `.txt` extension, not textual transcripts. Cannot be ingested as-is. **Recommended action:** either run them through Groq Whisper / the `scripts/teams_pull.py` style pipeline to produce actual `.md` transcripts before re-dropping, or rename to `.mp4` and move them outside `raw/` (they don't belong in a text-ingestion directory).

---

### [2026-04-19] Run 14 — Email digest Apr 17 + weekly sessions rollup

**Trigger:** Automated scan for unprocessed raw files. Two new files: `raw/email-digest-2026-04-17.md` (committed Apr 17) and `raw/weekly-sessions-2026-04-19.md` (Claude Code weekly rollup — week of Apr 12).

- **File:** raw/email-digest-2026-04-17.md
  - **Type:** email-digest (24-hour window, Apr 16–17)
  - **Pages created:** none
  - **Pages updated:** [[wiki/people/casey-earley]] (**title confirmed: Administrative Coordinator, Buda EDC**; email casey.earley@budaedc.com; shared Cohort 4 folder Apr 17; status warm → active; last_contact bump; resolved prior context gap), [[wiki/people/joshua-edmond]] (Apr 17: sent Casey updated Weeks 1 & 2 print-outs with Business Model Canvas added to Week 2; Andres shared the HIVE Entrepreneur Program folder with Joshua; last_contact bump), [[wiki/people/megan-miller]] (last_contact → Apr 17, Teams meeting held), [[wiki/people/roxana-yglesias]] (last_contact → Apr 17, Teams meeting held), [[wiki/people/becky-torres]] (last_contact → Apr 17, Teams meeting held), [[wiki/moil/gtm]] (+ Apr 17 cold-campaign section: 25+ outbound across KY/MS/MN/NE/WI/IA/AL/IL/NY/TN; first KY + MS push; new HIVE Cohort 4 curriculum subsection), [[MEMORY]] (added tax-review + Cohort 4 curriculum prep action blocks; trimmed Monthly Brain System hygiene to hit 200-line cap), [[index]] (stats + Run 14 header)

- **File:** raw/weekly-sessions-2026-04-19.md
  - **Type:** claude-code-weekly-rollup (week of Apr 12)
  - **Pages created:** none
  - **Summary:** 5 Claude Code sessions, 79 user messages, 443 assistant responses, 1116 tool calls, 98 files created, 38 commits. Covers: init commands, "how do I use this" onboarding Q, KB audit execution sprint (Apr 13), Brain system audit (Apr 14). Fully duplicates intelligence already in [[raw/weekly-sessions-2026-04-15.md]]; no new wiki pages warranted. Logged only.

**Key intelligence from Run 14:**
1. **Casey Earley = Administrative Coordinator, Buda EDC.** Title was a 2-week-old context gap on her page; Apr 17 signature-block test email resolved it. Email: casey.earley@budaedc.com. Status bumped warm → active.
2. **Cohort 4 curriculum is flowing 3 days before launch.** Joshua Edmond sent updated Weeks 1 & 2 print-outs with Business Model Canvas added to Week 2. Andres shared the HIVE Entrepreneur Program folder with Joshua. Casey shared the Cohort 4 OneDrive folder with Andres (view + edit). Bidirectional drops = curriculum prep is live.
3. **Biggest cold-outbound day on record (25+ emails).** First-time pushes into Kentucky and Mississippi; narrative + discovery + breakup cadences all running in parallel — deliberate A/B + pipeline-hygiene in a single day.
4. **Three customer Teams meetings held Apr 17:** Megan Miller, Roxana Yglesias (AlloyAtx), Becky Torres (Siren Beauty) — concurrent with the Apr 15 license-distribution push and Jacob's license-activation follow-through in Run 13.
5. **Kate Silvas acknowledged Andres's family hospital situation** when looping in Mayra Adams to schedule Apr 22 — personal context, relationship warmth.
6. **New tax action opened.** Melissa Jarbo (DLC Financial) returned from sick leave, created separate TaxDome profile; 1040 2025 review + Martin Kutac secure message + Ingrid refund/liability form pending.

**Summary:** Two files processed. The email digest was the only source of new intelligence — resolved Casey Earley's long-standing title gap, confirmed Cohort 4 curriculum collaboration is live, recorded Andres's largest cold-outbound day to date, and logged three Apr 17 customer Teams meetings. The weekly-sessions rollup was logged for completeness but duplicates content already in the Apr 15 rollup. No new wiki pages created. MEMORY.md trimmed to 200 lines by removing the stale Brain System hygiene section.

**Summary:** Run 11 promoted the long-flagged `raw/KidsGPT/` files into the wiki as a first-class personal project ([[wiki/projects/lunabella|Lunabella]]). Two cross-page open questions closed in the process (magical-reading-adventures's "is this KidsGPT?" and active-projects.md's "raw files not yet promoted"). Also surfaced a raw/ hygiene issue — 10 binary MP4 files pretending to be `.txt` transcripts in onedrive-transcripts/ need to be either transcribed or moved out of the raw/ directory.

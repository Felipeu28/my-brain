# Moil Brain — Ingestion Log

This file tracks every source that has been processed by `/kb compile`. Claude Code appends an entry here after each ingestion run.

---

## 2026-05-11 — Run 44: Monday Collaboration 2026-05-11 (Perseus Defense YC referral locked + Buda EDC magazine spread + Inna scope reset + Jacob outreach reallocation) + 2 internal-infra audits (log only)

**Trigger:** KB-agent scan for unprocessed raw files. Three found: (1) `raw/teams-transcript-monday-collaboration-2026-05-11.md` (45 KB Teams transcript from this morning, ~2h 38m, four substantive threads — high signal); (2) `raw/audits/2026-05-05-x-bookmarks-permanent-fix-research.md` (12 KB internal Brain-infrastructure decision doc — recommends paid X API at ~$6/mo via OAuth 2.0 PKCE); (3) `raw/audits/2026-05-07-ingestion-deep-audit.md` (32 KB internal Brain-infrastructure audit — 6 jobs ✅ / 8 ⚠️ / 13 🔴 across 27 plists; the headline finding is that 12/27 plists shipped 2026-05-03 are physically present on disk but never `launchctl bootstrap`'d, including the sentinel that was meant to catch this exact failure class). Substantive ingest for #1; #2 and #3 logged only per Run 31 internal-infra precedent (operational fixes belong in `pi-workspace`, not the wiki knowledge graph).

### File 1 — `raw/teams-transcript-monday-collaboration-2026-05-11.md`

- **Type:** teams-transcript (Monday Collaboration standing meeting)
- **Attendees:** Andres, [[wiki/people/jacob-oluwole|Jacob Oluwole]], [[wiki/people/taiwo-ola-balogun|Taiwo Ola-Balogun]], [[wiki/people/abiodun-solomon|Abiodun "Ablad" Adekanmi]] (Adeleke invited but absent)
- **Pages created (2):** [[wiki/orgs/perseus-defense]] (NEW org — YC S25 defense-tech, Buda HQ, $6–8M raised, $500K Buda EDC incentive Dec 2025; Tue 2026-05-12 8 AM CT Andres meeting via [[wiki/people/jennifer-storm|Jennifer Storm]] introduction for Clio YC alumni referral); [[wiki/meetings/2026-05-11-monday-collaboration]] (canonical meeting page — decisions, action items, side threads)
- **Pages updated (8):** [[wiki/people/jennifer-storm]] (last_contact 2026-05-01→2026-05-11, Perseus referral + Buda EDC magazine spread + family-hospital ack — load-bearing capital being actively spent on Andres's behalf), [[wiki/orgs/buda-edc]] (graph/spoke→graph/hub, last_contact 2026-05-07→2026-05-11; magazine 15K distribution + Excellence in Innovation finalist + $500K Perseus incentive precedent), [[wiki/people/jacob-oluwole]] (May 11 reallocation: 4-posts/week Inna cap + 10 real DM convos/day Moil rule, no copy-paste; pay catch-up promised), [[wiki/people/taiwo-ola-balogun]] (Moil-owned-email discipline + GitHub/Vercel migration to single sales email; first unprompted volunteer to take the higher-effort credential-discipline path), [[wiki/people/abiodun-solomon]] (holiday-aware planning rule + immediate Drive-check rule + Buda EDC magazine as primary marketing asset; Microsoft phone-login blocker re-surfaced for the third time), [[wiki/people/inna-benyukhis]] (May 8 Mother's Day video missed; **scope reset to 4 posts/week (2 images + 2 videos), apology + clarification reply sent in-call** — first explicit on-record customer-scope cap, likely template), [[wiki/people/megan-miller]] (2FA coordination today + sales-email centralization + HIPAA boundary as architectural rule), [[wiki/people/mark-polanco]] (first Connectex payment expected next week ~May 18 — first explicit payment-timing signal since Apr 9 close)
- **MEMORY.md:** **+1 May 11 immediate-week block** (Perseus meeting tomorrow + 8 May 11 team rules); demoted Apr 30 Anita Lansing (11d stale, momentum window closed) and Apr 28 inbox (John Costilla lunch + Victor UDC focus-group); compressed Apr 28 Connectex sprint + Apr 29 FitLogic engineering blocks for cap; **199 lines, under hard cap of 200**

**Key intelligence from File 1:**

1. **First documented YC-alumni-referral attempt for Clio.** Perseus Defense (YC S25, Buda HQ, $6–8M raised) — Jennifer Storm got them to reply to her referral request in 3 minutes; meeting Tue 2026-05-12 8 AM CT in Buda with Jennifer present. Andres' framing: *"a Y Combinator referral goes 5 billion miles"* and *"they're not coming to meet me, they're coming to do her a favor."* If converted, materially changes Clio's S26 application math.
2. **Buda EDC magazine published with 2 Moil pages, 15K distribution.** First time a city EDC publication has featured Moil at this scale. Pair with Moil Lab's "Excellence in Innovation" finalist news (won by Perseus in the same category, with Moil winning "Entrepreneurship Spirit" the prior year). Andres treats this as a marketing primary; Ablad to build content around it this week. Captured the precedent that **Buda EDC handed Perseus $500K in incentives Dec 2025** — first publicly recorded benchmark of EDC incentive-led recruitment program at this size.
3. **Inna scope reset is on-record.** First time Andres has explicitly capped a customer's scope creep, tied to a payment-vs-effort calculation. The contract is **4 posts/week (2 images + 2 videos)** — not 30 days/month. Apology + clarification reply sent in-call. Process changes (drive-check immediately, holiday-aware planning, never silently skip) own owner Ablad. Likely template for similar resets if other small-retainer customers stretch scope past contract.
4. **Jacob outreach reallocation is the operational counterpart.** **10 real DM conversations/day for Moil, no copy-paste.** First time Andres has named a quantitative outbound target for Jacob; replaces the Apr 24 *"none of them really sell"* post-mortem with a per-day cadence. Closes the long-running pattern (Apr 21 spam-folder thread, Apr 24 conversion-strategy coaching, Apr 28 Inna QA ownership) where Jacob was incrementally absorbing more Inna scope than the contract priced for.
5. **Taiwo's first unprompted volunteer-to-do-the-right-thing on credential discipline.** *"That's actually the best option, so everything is on one email."* Andres: *"Thank you, Taiwo. Because you're choosing to do the right thing over the amount of work it could take."* Pattern shift from Apr 28/May 4/May 6 repo-discipline relapses to volunteer-the-higher-effort-path on May 11.
6. **First explicit Mark Polanco payment-timing signal since the Apr 9 close.** Mark's first Connectex payment expected next week (~May 18). Together with the city payment (delayed by city-lawyer redlining) this is what unlocks Andres catching Jacob + Taiwo up on missed pay. Andres explicitly de-escalating any pay anxiety: *"this is not like other times where it's like, okay guys, I don't know what we're gonna do. No, the money's coming, we just don't have it yet."*
7. **Marcus is a Moil client not in any wiki page.** Andres was deploying Marcus's landing page on GoDaddy at the start of the call; first surfacing of this client. Capture next time more context appears.
8. **Jennifer Storm relationship is now load-bearing.** Andres on her: *"silent support or putting us in a magazine 15,000 people will get. I 100% want to make her proud."* Strongest "relationship-to-protect" framing yet captured. Her social capital is being spent on Andres's behalf in three distinct compounding artifacts in a single week (Perseus intro + magazine spread + Excellence in Innovation finalist) — capture every receipt.

### File 2 — `raw/audits/2026-05-05-x-bookmarks-permanent-fix-research.md`

- **Type:** internal-infrastructure decision doc (not wiki-promoted per Run 31 precedent)
- **Pages created/updated:** none
- **Frontmatter:** marked `ingested: true / ingested_at: 2026-05-11`; `tags: graph/leaf` retained
- **Summary:** Recommends switching `pi-workspace/bin/scrape-x-bookmarks.sh` from cookie-based scraping to the **paid X API on OAuth 2.0 PKCE with `bookmark.read` + `offline.access`**. Cost: ~$6/month at 200 bookmarks/day × $0.001 owned-read rate; worst-case ~$30/mo at the disputed $0.005 bookmarks-specific rate. The 2026-02-06 retirement of Basic ($200/mo) and Pro ($5,000/mo) tiers in favor of pay-per-use **collapses the hardest variable** in the original decision tree — there is no longer a paywall scenario worth planning around at this volume. Hardened headless Chrome (option c) rejected: same TOS-violation risk on `@roarkittys`, more code, no fidelity gain. Better instrumentation (option e) kept partially — weekly canary check is cheap insurance. Open questions for Andres: (1) does `@roarkittys` already have a developer app? (2) acceptable monthly spend? (3) verify the $0.001 vs $0.005 rate during pilot week 1. **No MEMORY action added — owned operationally by `pi-workspace` not the KB agent.**

### File 3 — `raw/audits/2026-05-07-ingestion-deep-audit.md`

- **Type:** internal-infrastructure audit (companion to `raw/audits/2026-05-03-ingestion-and-synthesis-audit.md`; not wiki-promoted per Run 31 precedent)
- **Pages created/updated:** none
- **Frontmatter:** marked `ingested: true / ingested_at: 2026-05-11`; `tags: graph/leaf` retained
- **Summary:** Read-only audit of all 27 plists + ~35 scripts in `pi-workspace`. Headline finding: **12/27 plists are physically present on disk but never loaded into launchctl** — every Week-3/4 implementation-plan deliverable shipped 2026-05-03 (sentinel, entity-graph, daily-correlator, project-activity, pattern-surfacer, last-contact, session-learnings, concept-of-the-day, related-suggester, brain-lint, weekly-pitch-mistake, last-contact-coverage) is in this set. **The sentinel that was supposed to catch exactly this failure class is itself one of the unloaded jobs.** Other top findings: (a) X cookies expired 2026-05-03 — 5+ days of bookmarks lost; (b) `weekly-operating-brief.sh` line 56 still has the hard `BOOKMARK_FILES -eq 0` bail despite Week-1 plan item 3 saying it would be relaxed (W18 + W20 operating briefs missing as a result); (c) `imessage-pull.sh` is silent-success-buggy — `tee` swallows the python exit code, plist reports OK while chat.db Full Disk Access is missing on `/Users/jarvisurrego/mlx-env/bin/python`; (d) `morning-briefing.sh` 2026-05-11 run failed — Claude Write didn't fire and stdout-recovery couldn't find the marker, briefing file does not exist, heartbeat correctly flags `missing`; (e) chroma-index has been exit-2'ing daily for ≥4 days because LM Studio isn't running on `localhost:1234`. Five immediate fixes proposed (≤2 hrs total effort), with the plist-load fix alone restoring ~9 of the 13 broken-rated rows. **No MEMORY action added — owned operationally by `pi-workspace` not the KB agent. Audit findings flagged here for traceability; fixes belong in a separate ingestion-pipeline operational thread.**

### Operational signal: today's morning-briefing failed

Captured in the audit and confirmed visually in `quartz/content/raw/briefings/` (no `briefing-2026-05-11.md` file). The KB agent ingestion completed normally — this concerns the `pi-workspace` morning-briefing job, not the KB-agent path. Worth flagging to Andres so the `bin/morning-briefing.sh` stdout-recovery fallback can be hardened (third fallback: emit a minimal "Brain alive but synthesis failed" briefing from the assembled context so the daily trust signal isn't silent).

### Skipped files

None. All three unprocessed files in `raw/` and `raw/audits/` accounted for. The `raw/onedrive-transcripts/` directory is unchanged from the 2026-04-15 state (10 binary MP4-misnamed-as-`.txt` files documented in Run 11 still pending re-processing or move; not addressed this run).

---

## 2026-05-11 — Run 43: 65 Claude Code session-log files backfill (low-signal session batch — log only; substance of substantive sessions already flows through `wiki/projects/clio.md` auto-update; no new wiki pages, no new MEMORY actions)

**Trigger:** KB-agent ingestion request for 65 files in `quartz/content/raw/sessions/claude-code-2026-04-14*.md` through `claude-code-2026-05-10*.md` that had been auto-created by `bin/ingest-claude-sessions.sh` but never received the `ingested: true / ingested_at` frontmatter marker. **Established precedent** (Runs 29, 31, 42): session-log files are derivative — they are the *runner* of an artifact whose intelligence was captured by another Run number. The per-session bookkeeping closes the "what hasn't been ingested?" gap without re-ingesting content the wiki already holds.

**Pages created (0).** **Pages updated (0).** **MEMORY: unchanged.**

**Classification of the 65 files:**

- **~58 routine automation sessions** — each one is the *runner* of an artifact already ingested by its own Run number:
  - 8× **morning briefing / daily-cross-source-intell / "you are Andres's editor"** (May 3–10) → artifacts = `raw/email-digest-*.md`, `raw/signal-briefs/signal-brief-*.md` (ingested in Runs 30, 33, 35–41)
  - 8× **"you are Andres's plan radar every day at noon"** (May 3–9) → artifact = `outputs/plan-radar-*.md` (internal, not wiki-promoted per Run 31 internal-infra rule)
  - 7× **"check for any new files in raw/ and raw/onedrive-tr..."** (May 3–9) → artifact = the ingestion run itself; KB agent runs that did the work were Runs 30–41
  - 7× **"pull today's Microsoft Teams meeting transcripts"** (May 3–9) → artifacts = `raw/teams-transcript-*.md` files already absorbed in Run 29 backfill + per-Run meeting promotions
  - 4× **"read these two json files of today's email activity"** (May 4–7) → artifacts = `raw/email-digest-2026-05-{04,05,06,07}.md` (ingested in Runs 33–40)
  - 4× **"run the morning briefing — execute these steps"** (May 4–8) → artifact = `outputs/briefing-2026-05-{04..08}.md`
  - 3× **"you are the moil brain kb-agent ingest these unpro..."** (May 4, 5, 8) → artifact = the ingestion run itself (Runs 33, 34, 40)
  - 3× **"you are an entity extraction agent"** (May 4, 5) → artifact = internal entity-graph index, runs are mechanical
  - 2× **"today's top 3"** + **"morning briefing — Fri/Thu"** (May 7, 8) → artifact = brain-query.sh + briefing outputs
  - 2× **"<command-message>setup-gbrain</command-message>"** + **"<command-message>autoplan</command-message>"** (May 9, 10) → gstack skill runs; no wiki impact
  - 1× **"you are Andres's strategy operator every Sunday evening"** (May 4) → artifact = `outputs/strategy-radar-*.md`
  - 1× **"you are surfacing patterns from the last 28 days"** (May 5) → pattern-surfacer one-shot
  - 1× **"you are parsing raw scraped text from Andres's X"** (May 10) → X-bookmarks parser
  - 1× **"you are extracting structured learnings from a weekly..."** (May 3) → session-learnings filter (item 8a from Run 31)
  - 1× **"<command-message>gstack</command-message>"** (May 8) → voice-system fix routed via wiki/projects/clio.md
  - 1× **"in luna-brain there's a tracked but orphaned dir..."** (May 4) → 1-message housekeeping in luna-brain repo
  - 1× **"scheduled task name clio-weekly-security-audit"** (May 4) → scheduled CSO audit run; no Moil-Brain wiki impact
  - 1× **"today's pushes 2026-05-03 full review"** (May 10) → review of Run 31's brain-audit shipping (already documented in [[wiki/summaries/brain-audit-2026-05-03]])
  - 1× **"active plan: gstack/projects/felipeu28/clio-ceo-pla..."** (May 9) → /plan-eng-review on D4/D3; artifact = ceo-plan files in luna-brain repo

- **~7 substantive engineering sessions** — substance lives in the source repos and (where applicable) already flows through `wiki/projects/clio.md § Last 7 days` via daily `bin/project-activity.sh`:
  - `claude-code-2026-04-14-brain-system-audit.md` — multi-phase Brain v3 audit (kb-health.py, Moil360 canonicalization, historical-transcripts-index, Client Ledger, Daniel Mann, HIVE completeness, iMessage pipeline). Already absorbed in: [[wiki/summaries/brain-audit-2026-05-03]] (the audit framing later formalized), [[wiki/meta/brain-upgrade-plan]], `kb-health.py` (live in `scripts/`), `wiki/meetings/historical-transcripts-index.md`, [[wiki/concepts/moil360]], [[wiki/moil/active-projects]]. The audit ran 2026-04-14 but its outputs were operationalized through Runs 6, 23, 31
  - `claude-code-2026-05-01-let-s-create-a-new-video-about-the-parents-side-of.md` — built `~/clio-video` Remotion repo with full Clio scene library (orb breath, brain graph, depth climb, Spanish, weekly digest, wow moment, memory). External marketing-asset repo outside the wiki's ingest scope; flagged here for the record. **Watch:** if `clio-video` produces a published asset, promote to a [[wiki/concepts/clio-parent-pitch-video]] stub
  - `claude-code-2026-05-03-week-1-execution.md` — gstack adoption + 23-skill rollout + clio-cso/qa/voice-qa/safety/brain-lint specialists + security headers/CSP/HSTS + canary webhook + LLM eval gating. Already in [[wiki/projects/clio]] § Last 7 days (auto-update) per Run 42
  - `claude-code-2026-05-04-application-scoring-proposed-changes.md` — 7,532-minute accelerator-strategy session producing `Accelerator_Strategy_Roadmap_2026-05-04.md` + YC Clio Summer 2026 submission + Moil deck builder. External repo (`~/Library/Mobile Documents/com~apple~CloudDocs/Documents/Claude/Projects/Accelerator Applications System/`); not in wiki ingest scope. **Andres's pitch corrections**: 15yr corporate sales, dropped "SOC 2 compliant" + "AI for Business Applications cert" + "2 years of Claude Code experience" — captured here for the record; not promoted to a wiki page (personal-positioning facts already implicit in [[wiki/people/andres-urrego]] / [[wiki/projects/moil]] founder context)
  - `claude-code-2026-05-06-phase-0-subtraction.md` — Clio UX subtraction audit (killed duplicate gamification, dead synthesize endpoint, BrainView tab buffet) + Phase 1.0 World rebuild (voice-on-tap, biomes-as-places, Luna greets by name) + iPhone silent-switch audio fix + kid-surface i18n. Major product pivot — substance flows through [[wiki/projects/clio]] § Last 7 days when next auto-update runs (currently dated 2026-05-05; will catch May 6–10 commits on next nightly run)
  - `claude-code-2026-05-08-command-message-gstack-command-message.md` — gstack voice-system roots-cause fix (one voice/reply, mic gate on audio drain, strip emojis from TTS) + spun up `docs/clio-characters` original-cast side project (CHARACTERS.md/BRIEF.md/PLAN.md). Substance will flow through [[wiki/projects/clio]] § Last 7 days on next nightly. **Watch:** if `clio-characters` ships an original cast launch, that may justify a [[wiki/concepts/clio-character-cast]] stub
  - `claude-code-2026-05-09-ship-phase-1-start-phase-2-5.md` — Stories feature shipped: streaming generation, age-tier reading view, recents/delete, age-tier setup picker, Grok TTS language-tag voice-flip fix. Will land in [[wiki/projects/clio]] § Last 7 days on next nightly. **Andres-visible product surface change** — Clio now has a Stories feature; the existing clio.md Status line will need a one-shot edit on the next manual run to reflect this (deferred to next interactive session, not auto-applied here)
  - `claude-code-2026-05-10-bilingual-claim-audit-implementation-plan.md` — bilingual claim audit shipped `packages/shared/src/lang.ts` (kid-input language detection + label_es brain context). Decision: **"A (full ambient)"** = directional choice for bilingual handling. Will flow through [[wiki/projects/clio]] § Last 7 days on next nightly

**Sources logged but not promoted to wiki:** all 65 files at `quartz/content/raw/sessions/claude-code-2026-{04-14, 05-01..10}-*.md`. Each marked `ingested: true / ingested_at: 2026-05-11`.

**Index update:** [[index]] — Run 43 header; raw source count unchanged at 543 (these files exist in `quartz/content/raw/sessions/` and were already counted; the ingest flag is the only mutation); wiki page count unchanged at 309.

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py`.

**Key intelligence:**

1. **The session-log file type is now reliably *log-only* across 3 separate batches** (Run 29 = ~80 files, Run 31 = ~30 files, Run 43 = 65 files). The pattern is stable: every session-log captures *a runner of an artifact*, and the artifact is what carries the intelligence. The ingest-claude-sessions.sh job is doing the right thing (capturing every session for posterity + per-project `## Last 7 days` rollup), but the per-file KB-ingestion sweep is mechanical bookkeeping, not signal extraction. **Worth retiring the manual KB-agent ingest call on session-log files entirely** — the auto-job already marks them, and the per-Run intelligence is captured by the artifact's own ingest path. Routed as a Week-4 candidate for `bin/ingest-claude-sessions.sh`: have it set `ingested: true / ingested_at: <today>` at file-creation time so the file is born marked.

2. **Substantive Clio engineering sessions (Phase 0 subtraction, Stories ship, bilingual claim audit, gstack voice fix) are accumulating without a corresponding manual update to [[wiki/projects/clio]] § Status.** The `## Last 7 days` block is auto-updated by `bin/project-activity.sh` and is current through 2026-05-05; the May 6–10 commits will catch up on the next nightly. **But the Status line** (currently "Phase 1 shipped … currently in a stability sprint — recent commits are bug fixes on edge synthesis") is now ~5 days stale relative to the Phase 1.0 World rebuild and Stories feature. **Next interactive Brain session should refresh the clio.md Status line + Recent decisions block.** Not auto-applied in this run (Run 43 is log-only by design).

3. **Two side projects spun up off Clio in the last 10 days**: `~/clio-video` (Remotion parent-pitch repo, May 1) and `~/luna-brain/docs/clio-characters` (original-cast brief, May 8). Both are external-repo work not yet in the wiki. **Watch trigger:** if either produces a published asset (the clio-video parent pitch goes live; the clio-characters cast launches), promote to a wiki concept stub. Neither is mature enough to deserve a wiki page yet — flagging as future-Claude breadcrumbs.

4. **Andres's accelerator pitch corrections from May 4 are personal-positioning facts that don't need a wiki page but should inform future Brain-generated copy:** 15 years of corporate sales (founder credibility frame), drop "SOC 2 compliant" claim, drop "AI for Business Applications" certification mention, drop "2 years of Claude Code" framing. Capture for future-Claude reference; not promoted to MEMORY since this is steady-state positioning, not an open action.

**Source count:** 543 → 543 (no new files added; 65 existing files marked ingested). Wiki page count: 309 → 309. People count: 65 → 65. Orgs count: 29 → 29.

**Summary:** Run 43 closes the bookkeeping gap on 65 session-log files spanning 2026-04-14 → 2026-05-10. No new wiki pages, no new MEMORY actions, no index drift. Per Runs 29, 31, 42 precedent: session-logs are the *runner* of an artifact, not the artifact itself — intelligence is held by the artifact's own ingest path. The substantive Clio engineering sessions (Phase 0 subtraction, Stories, bilingual claim, gstack voice) are queued for `bin/project-activity.sh` auto-update on next nightly, and the clio.md Status line is flagged for next-interactive-session refresh. Run 43 is consistent with the stable "session-logs = log-only" pattern across 3 batches now.

---

## 2026-05-10 — Run 42: weekly-sessions-2026-05-10 (meta rollup, log only — 63 sessions for week of May 3–10; no new wiki pages, intelligence already captured)

**Trigger:** Single new raw file detected post-Run-41: `raw/weekly-sessions-2026-05-10.md` — Claude Code weekly rollup auto-generated by `bin/ingest-claude-sessions.sh` Sun 07:30 (commit `d2d4036`). 63 sessions across 7 projects: Brain/Automations 32, Brain/KB 14, Clio/worktree 8, "-" 3, Brain/KB/worktree 2, Clio 2, Brain/MyBrain 1, Home 1. 168 user messages · 970 assistant responses · 3287 tool calls · 135 files created · 21 edited · 86 commits. 2 automation self-runs filtered.

**Pages created:** none. **Pages updated:** none. **Per established precedent** (Runs 8, 14, 23 — see log entries for `weekly-sessions-2026-04-{15,19,26}`), weekly-sessions rollups are *"meta rollup, log only"* — derivative of per-session data already captured in `raw/sessions/` by the same job. The substance of week 2026-05-03 → 2026-05-10 (Megan FitLogic CRM handoff, Becky reply, Chris Gomes M&A inquiry, May 7 SMB cold-outbound campaign, Hilton Jun 18 reservation, GCP budget alert) was fully ingested across Runs 39–41. No new external people, no new action items with deadlines, no new decisions to surface.

**Sources logged but not promoted to wiki:**

- **`raw/weekly-sessions-2026-05-10.md`** — week-of-May-3 rollup. Confirms automation throughput is now load-bearing: Brain/Automations dominates session count (32 of 63 = 51%), Brain/KB ingest is steady (14 sessions, 5 commits via the ingest pattern), Clio engineering sustained across Clio + Clio/worktree (10 sessions, 50 commits). Notable engineering sessions worth flagging only at session-file level (already auto-captured): "Application Scoring + Proposed Changes" (May 4 Home, 7532 min, accelerator strategy), "Phase 0 — Subtraction" (May 6 Clio, 471 min, parents/kids UX audit), "gstack voice system" (May 8 Clio/worktree, 4 commits), "Active plan: clio-path-b-validation" (May 9 Clio/worktree, 619 min), "Bilingual Claim Audit & Implementation Plan" (May 10 Clio/worktree). All of these are Clio-side engineering loops, not Brain-side operational signal — Brain wiki ingestion is correctly not promoting them.

**Index update:** [[index]] — Run 42 header; raw source count unchanged at 543 (file already existed and was being counted by `kb-health.py` rglob); wiki page count unchanged at 309.

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py` (✅ all green, MEMORY 200 lines at cap, 1 known orphan `wiki/inbox/append.md`). Source file (`raw/weekly-sessions-2026-05-10.md`) marked `ingested: true / ingested_at: 2026-05-10`.

**Key intelligence:** None new from this source — but the rollup itself is a useful systems-level data point: **the daily automation layer is producing 4–5 sessions/day routinely** (morning briefing + plan radar + Teams pull + email digest + X-bookmarks editor), the **KB ingest cadence ran 14 times this week with 5 commits** (every weekday plus weekend catch-up), and **Clio engineering is operating in parallel at ~10 sessions/week** without crowding out Brain ingestion. The May 3 audit's concern that "weekly-sessions is mechanical not editorial" still holds — the rollup remains a signal-poor file type — but the underlying sessions are healthy and the per-session capture is doing the real work.

**Source count:** 543 → 543 (no new file added; existing file marked ingested). Wiki page count: 309 → 309. People count: 65 → 65. Orgs count: 29 → 29.

**Summary:** Run 42 is a single-source log-only run on the weekly-sessions rollup that's auto-produced every Sunday morning by `bin/ingest-claude-sessions.sh`. No new wiki pages, no new MEMORY actions, no index drift. The rollup confirms healthy automation throughput (32 Brain/Automations sessions, 14 Brain/KB sessions, 10 Clio sessions, 86 commits, 135 files this week) without surfacing new external operational signal — exactly the pattern this file type has shown across Runs 8, 14, 23. Marked ingested for log discipline.

---

## 2026-05-09 — Run 41: signal-brief 2026-05-07 (Chris Gomes M&A silence-anomaly upgrades action with May 14 deadline; Megan = load-bearing customer of the week; `myfitlogic.com` Cloudflare-workaround validated as deliverability-hedge architecture for Andres's own SMB cold campaign)

**Trigger:** Single new raw file detected post-Run-40: `quartz/content/raw/signal-briefs/signal-brief-2026-05-07.md` — daily-correlator output with cross-source connection (Megan/FitLogic Teams + email-digest converging on `myfitlogic.com` workaround as a parallel deliverability test for Andres's SMB campaign), active person flag (Megan as load-bearing customer of the week), and silence anomaly (Chris Gomes M&A inquiry inbox-silent against Andres's same-day reply cadence). No new wiki pages — the signal-brief is meta-analysis on Run-39 + Run-40 inputs; the additive value is three operational reframings.

**Pages created (0):** none — signal-brief consolidates and reframes existing intelligence.

**Pages updated (3) + MEMORY + index:**
- [[wiki/people/chris-gomes]] — added **2026-05-09 — Daily-correlator silence anomaly** section (silence defaults to *"ignored"* not *"declined gracefully"* against Andres's normal cadence). Action upgraded: was *"decide whether to engage"*, now *"send polite holding reply within 7 days (by 2026-05-14)"* with both engage and decline scripts pre-staged at zero cost. Source list + `last_contact` line bumped; `Last updated: 2026-05-09`
- [[wiki/people/megan-miller]] — added **2026-05-07 — Daily-correlator: load-bearing customer of the week** section (4 single-day dependencies — CRM go-live + `myfitlogic.com` provisioning + lab order + in-person training — all gate on Andres's [2026-05-08 AM] credential delivery; miss = compounding delay across all four threads). Source list + `Last updated: 2026-05-09` bumped
- [[wiki/concepts/ai-cold-outreach]] — added **cross-source pattern bullet** to the "May 6–7 SMB cold-outbound campaign" section: the same `myfitlogic.com` Cloudflare-workaround that resolved Megan's 16-day Resend block is the same architectural hedge available to Andres if `andres@moilapp.com` reply rates fall below 1% — register a parallel domain end-to-end controlled, route SMB campaign through it. Pattern name: *"stand up a parallel asset you fully own."* Already validated end-to-end on a customer; can re-apply to Moil's own outbound stack without redesign. Source list + `Last updated: 2026-05-09` bumped
- [[MEMORY]] — Header date bumped to 2026-05-09 with Run 41 summary line. Chris Gomes action (line 16) upgraded: now carries explicit May 14 deadline + the daily-correlator silence-anomaly framing as the *why*. **Final count: 200 lines (still at 200-line cap; no insertions, only in-place rewording).**
- [[index]] — Run 41 header (raw source count unchanged at 479 because the signal-brief lives in `quartz/content/raw/signal-briefs/`, not the root `raw/` dir that `kb-health.py` counts; wiki page count unchanged at 309); Run 40 demoted to "Previous run header"

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py`. Source file (`quartz/content/raw/signal-briefs/signal-brief-2026-05-07.md`) marked `ingested: true / ingested_at: 2026-05-09`.

**Key intelligence:**

1. **The daily-correlator's silence-anomaly framing on Chris Gomes is sharper than Run 40's "decide whether to engage" framing.** Run 40 left the engage-vs-decline decision open with no clock; Run 41 reframes it as a *time-bounded relationship-default risk*: silence past ~7 days defaults to "ignored" (which is the worst possible read for a first-on-record inbound M&A inquiry). This is the same kind of reframing the correlator made on Becky's reply — *"the apology-only reply doesn't ship the named cadence Becky asked for."* In both cases the correlator is reading an asymmetry between an *easy zero-cost action* and a *compounding default-to-bad-state* if the action is skipped. Worth tracking whether this analytical pattern repeats — if it does, it's a feature of the correlator worth surfacing back into the daily-correlator prompt itself.

2. **The `myfitlogic.com` Cloudflare-workaround is now a re-usable architecture, not a one-off customer fix.** This is the highest-leverage cross-source insight from Run 41: the *parallel-domain* pattern that unblocked Megan's 16-day Resend block is the *same hedge* available to Andres's own outbound campaign if `andres@moilapp.com` reply rates fall below 1%. **The customer-onboarding playbook lesson and the GTM deliverability hedge are the same architecture viewed from different angles.** Both rely on the same constraint: when a deeper layer of the stack is locked or degraded, stand up a parallel asset you fully own. Already validated end-to-end on a customer; can re-apply to Moil's own outbound without redesign. Worth a follow-up entry in [[wiki/concepts/moil360]] once a second deliverability data point confirms when the hedge is needed (n=1 today on the `andres@moilapp.com` deliverability concern).

3. **Megan as "load-bearing customer of the week" is the first time the daily-correlator has explicitly framed dependency-clustering as a risk vector.** Four threads (CRM go-live + `myfitlogic.com` provisioning + lab order + in-person training visit) all gating on a single delivery on a single day. The correlator's read makes the engineering risk visible: *miss the [2026-05-08 AM] credential delivery and four downstream threads slip in lockstep.* The 5/8 AM action is in MEMORY.md (line 28) — confirm delivery happened or carry to next run if it slipped.

4. **Signal-briefs are now reliably producing meta-intelligence that is operationally actionable, not just summary.** Three of the last three signal-briefs (5/6, 5/7) have surfaced reframings that change the priority or cost calculus of an existing MEMORY action: 5/6 reframed Andres's reply to Becky as the *unblock* (not just an apology); 5/7 reframed Chris Gomes silence as a *default-to-ignored* signal (not just an open decision); 5/7 connected `myfitlogic.com` to `andres@moilapp.com` (not just two separate deliverability problems). **The daily-correlator is now load-bearing in the action-prioritization loop, not just a passive intelligence layer.**

**Source count:** 479 → 479 (signal-brief lives in `quartz/content/raw/signal-briefs/`, not counted by `kb-health.py`'s root-`raw/` rglob). Wiki page count: 309 → 309. People count: 65 → 65. Orgs count: 29 → 29.

**Summary:** Run 41 ingests one signal-brief and updates 3 wiki pages + MEMORY + index. No new pages. The high-signal items are (a) the **silence-anomaly reframing of Chris Gomes** that upgrades the M&A action with a hard May 14 deadline (preserves the relationship and the data point at zero cost regardless of engage/decline decision), (b) the **`myfitlogic.com` parallel-domain pattern** as a re-usable deliverability-hedge architecture for Andres's own SMB campaign (customer-onboarding playbook = GTM hedge architecture viewed from different angles), and (c) the meta-observation that the daily-correlator is now reliably reframing existing MEMORY actions in ways that change their priority — making it load-bearing in the action-prioritization loop, not just a passive intelligence layer.

---

## 2026-05-08 — Run 40: email-digest 2026-05-07 + signal-brief 2026-05-06 (first on-record inbound M&A inquiry: Chris Gomes / Vision Point Capital; Becky reply sent but daily-correlator frames it as insufficient; Hilton Jun 18 confirmed; GCP 150% budget alert intentional; first sustained SMB cold-outbound day with 3 subject-line variants under live A/B; 4-step chamber-breakup batch fired)

**Trigger:** Two raw files detected — `raw/email-digest-2026-05-07.md` (full inbox + sent + notable threads for the 24h window) and `raw/signal-briefs/signal-brief-2026-05-06.md` (daily-correlator: cross-source connection on Becky, active-flag on Becky, silence anomaly on Megan).

**Pages created (2):**
- [[wiki/orgs/vision-point-capital]] — first on-record inbound acquisition signal in the Brain. `graph/spoke`. Chris Gomes opened a *"Valuation and EBITDA Multiple for Moil"* inquiry citing investors interested in acquiring a business like Moil
- [[wiki/people/chris-gomes]] — `chris.gomes@visionpointcapital.com`; cold inbound; person/contact

**Pages updated (8):**
- [[wiki/people/becky-torres]] — added two sections: (1) **May 6, 2026 — Daily-correlator: cross-source connection + active flag** (signal-brief insight that the May 6 *"no proactive design changes"* rule is a *reaction* to Becky's process-confusion, so the reply needs to ship the named cadence Becky asked for, not just the discipline shift); (2) **May 7, 2026 — Andres replied: apology + ask for feedback specifics** (the apology-only reply does *not* ship the named cadence — daily-correlator framing flagged this as insufficient; watch for whether Becky's next reply re-asks "is this a call or in-person?"). `last_contact: 2026-05-06 → 2026-05-07`
- [[wiki/people/megan-miller]] — added **May 6–7, 2026 — Daily-correlator silence anomaly resolved at 3:30 PM CT** section. May 6 brief flagged Megan as silence anomaly (no reply 24h after Andres's same-day GoDaddy DNS verification invite); resolved May 7 20:14 UTC with the calendar accept and the 3:30–4:55 PM CT meeting that produced the [[wiki/meetings/2026-05-07-megan-andres-fitlogic-crm-handoff|`myfitlogic.com` workaround]]. **Read of the correlator: the silence was a calendar latency issue, not a relationship issue — but the "Thursday morning nudge" hedge was correct precaution.**
- [[wiki/people/sarah-miller]] — added 2026-05-07 row: forwarded **Hilton reservation #3467031844** for Jun-18 (TEDC night-before stay) under Sarah's name with Andres on the room. Andres replied 22:07 UTC with thanks. **Buda EDC is sponsoring TEDC travel** — confirms the keynote is being treated as an EDC-sponsored speaking slot, not a private engagement. `last_contact: 2026-05-01 → 2026-05-07`
- [[wiki/orgs/buda-edc]] — TEDC Mid-Year Conference section gets a May 7 logistics block: Hilton reservation confirmed; EDC-sponsored travel precedent captured for the next time a TX EDC books Andres elsewhere. `last_contact: 2026-05-04 → 2026-05-07`
- [[wiki/people/adeleke-tolulope]] — added **May 7, 2026 — GCP budget alert: 150% of $20 cap + $19K Gemini-API anomaly** section. Adeleke pre-set the budget alert (intentional, not a runaway spend); $19K Gemini spike connected to PR #74 Clio Gemini-cascade work shipped same day. **Confirms the May 4 cost-discipline standing rule + per-project budget alerts are now load-bearing.** `last_contact: 2026-05-04 → 2026-05-07`
- [[wiki/concepts/ai-cold-outreach]] — added two sections: (1) **May 6–7 SMB cold-outbound campaign live (Content360 pitch)** — first sustained day-over-day cold outbound at SMB ICP (vs. April's chamber/EDC campaign), with 3 subject-line variants under live A/B test (*"30 days of content in 20 minutes"* / *"Most SMB owners tell us the same thing…"* / *"Business owners don't expect it to sound this good"*) across construction, real-estate, food-service, animal-control verticals; (2) **May 6–7 chamber-breakup follow-ups continuing**. **Operational shift signal:** B2G replication motion → SMB-direct motion is now the default outbound default. **Deliverability watch:** sends from `andres@moilapp.com`, the same address that hit Gmail spam at FitLogic — if reply rate < 1%, evaluate domain-warmup or rotation
- [[wiki/concepts/chamber-outreach-2026-04]] — added **May 7, 2026 — 4-step "Should I close this out?" breakup batch** section with named recipients (Hunterdon County, Point Pleasant Beach NJ, UCEDC, Jefferson County WV). Apr 29 NBCC precedent confirms breakups extract signal from previously silent contacts. Track 7-day reply rate
- [[MEMORY]] — added 6-item May 7 block; struck Becky-reply (with daily-correlator caveat that watching is required), Hilton confirmation, and an Adeleke "no action required" note; demoted **Apr 24 inbox sub-block** (Joshua redlines / VoyageAustin / Rashaka close / Apollo Joseph→Roger mismatch) — duplicate Rashaka still tracked in "Next 2–3 weeks." Compacted Apr 28 inbox + Caroline/Shannon entries. **Final count: 200 lines (at 200-line cap).**

**Index update:** [[index]] — Run 40 header; raw source count 478 → 479 (+1 — email-digest 2026-05-07 at root raw/; signal-brief 2026-05-06 lives only in quartz/content/raw/signal-briefs/, not counted at root); wiki page count 307 → 309 (+2 new); orgs folder count 28 → 29; people folder count 64 → 65.

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py`. Source files marked `ingested: true / ingested_at: 2026-05-08`: `raw/email-digest-2026-05-07.md`, `raw/signal-briefs/signal-brief-2026-05-06.md`.

**Key intelligence:**

1. **First on-record inbound M&A inquiry — Chris Gomes / Vision Point Capital.** The Brain has now tracked 478 raw sources across email, Teams, OneDrive, GitHub, X bookmarks, iMessage, calendar, and signal-briefs — and *none* of them previously contained an external acquisition inquiry for Moil. The May 7 19:59 UTC email *"Valuation and EBITDA Multiple for Moil"* breaks that. Even if Andres declines (likely), this is a meaningful operational artifact: it puts a date on when Moil first appeared on a private-investment-firm radar. Worth low-cost engagement (extract a valuation/EBITDA-multiple benchmark) before politely declining; the relationship cost is near-zero and the data point compounds.

2. **The Becky reply is sent but the daily-correlator's framing predicts it's insufficient.** The May 6 brief made an unusually crisp call: Becky's two May 6 emails landed *before* the Andres × Taiwo internal call locked the *"no proactive design changes"* rule, meaning the rule is a reaction to her confusion, not an independent decision — so the reply *must* ship the rhythm Becky asked for, not just the discipline shift. Andres's actual May 7 12:18 UTC reply apologizes + asks for specifics, but does *not* commit to the *"video uploads → 48–72hr build → monthly in-person at SIREN"* cadence. **The next data point — Becky's reply or non-reply — is the test of whether the daily-correlator's analytic frame is calibrated.** Worth tracking explicitly: if Becky re-asks "is this a call or in-person?", the correlator was right; if she just sends more video feedback, the apology-only reply was sufficient.

3. **Cost-discipline instrumentation is now load-bearing.** Adeleke's pre-set GCP budget alert fired at 150% of $20 cap on May 7 and was reconciled within hours — the May 4 cost-discipline standing rule is no longer a verbal commitment but a *system* that catches issues as they happen. The $19K Gemini-API spike correlates cleanly to the same-day Clio Gemini-cascade PR (#74), so the spike is engineering-attributable, not a billing leak. **First time the Brain has captured a real-time budget alert → root-cause loop closing within a 4-hour window.** This is the cost-discipline pattern Andres said he wanted at the May 4 collab — it now exists as instrumented behavior, not just team norm.

4. **The SMB cold-outbound campaign is now sustained, not a one-day pivot.** May 6 was the first SMB-pivot day; May 7 doubled down with another 12 pitches across 3 active subject-line variants. This shifts Moil's GTM motion from B2G replication (chambers/EDCs) → SMB-direct (construction, real-estate, food-service, animal-control) as the *default* outbound channel. Worth tracking variant-level open and reply rates separately — the *"Most SMB owners tell us the same thing…"* pain-mirror frame is closest to the @itsalexvacca / @dimitarangg AI-cold-outreach hooks worth comparing against. **Deliverability is the under-watched risk:** all sends from `andres@moilapp.com`, the same domain that hit Gmail spam at FitLogic in April. If campaign-level reply rate < 1%, the issue is likely inbox placement, not copy.

5. **Hilton Jun 18 reservation = first EDC-sponsored speaker travel for Andres.** Buda EDC is paying for the night-before TEDC stay under Sarah Miller's name with Andres on the room — confirming the EDC is treating the keynote as a sponsored speaking engagement, not a personal commitment. Capture as a precedent the next time a TX EDC books Andres elsewhere — **the Buda EDC × Moil B2G template now includes paid travel for keynotes**, which scales the speaking-circuit channel without burning Andres's own travel budget.

**Source count:** 478 → 479 (root raw/). Wiki page count: 307 → 309. People count: 64 → 65. Orgs count: 28 → 29.

**Summary:** Run 40 ingests one email-digest + one signal-brief and creates two new pages (Vision Point Capital + Chris Gomes) plus 8 page updates + MEMORY block. The high-signal items are (a) the **first on-record inbound M&A inquiry** for Moil, (b) the daily-correlator's prediction that Andres's May 7 reply to Becky is insufficient (now testable on her next response), (c) confirmation that the May 4 cost-discipline standing rule is now instrumented behavior (GCP budget alert fired and reconciled within 4 hours), (d) the operational shift to SMB-direct cold outbound as the default GTM motion, and (e) the EDC-sponsored TEDC travel precedent that adds Buda EDC paid travel to the speaking-circuit channel.

---

## 2026-05-07 — Run 39: Megan × Andres FitLogic CRM handoff (Resend domain blocker resolved via `myfitlogic.com` workaround; CRM credentials ship May 8 AM; new "My Life on Purpose" LLC + coaching-cert course; AI-search inbound producing 4–5 calls/day; Cloudflare-locked original domain abandoned)

**Trigger:** Single new raw file detected post-Run-38: `raw/teams-transcript-megan-andres-2026-05-07.md` — ~1h 21min Teams session (3:30–4:55 PM CT, organizer Andres). Two parallel threads: (1) FitLogic business operations update — Michelle training, AI-driven inbound leads, new LLC, pricing rewrite, coaching certification course idea; (2) live demo + setup of the custom Moil CRM/sequence tool, including a workaround for the multi-week Resend domain-verification block.

**Pages created (1):**
- [[wiki/meetings/2026-05-07-megan-andres-fitlogic-crm-handoff]] — meeting page with key decisions, action items, FitLogic business update, CRM features demoed, patterns observed. `graph/leaf`.

**Pages updated (5):**
- [[wiki/people/megan-miller]] — added "May 7, 2026 — CRM handoff afternoon meeting + Cloudflare workaround + new LLC" section. New email `connections@myfitlogic.com` added to Email line. **AI-search inbound is now a measurable lead channel** (4–5 calls Tuesday + 2 conversions + waitlist) — first quantified data point. New LLC "My Life on Purpose" approved (separate from FitLogic; likely home for menopause/andropause coaching certification course). Pricing rewrite + $1,600/60-min IC competitor benchmark. `last_contact: 2026-05-06 → 2026-05-07`.
- [[wiki/orgs/fitlogic]] — added "May 7, 2026 — CRM Handoff Afternoon Meeting + Cloudflare Workaround" section. **🟢 Resend domain blocker resolved via second-domain workaround** after 16 days. Original domain `fitlogicfunctionalmedicine.com` Cloudflare-locked (likely old vendor); pivoted to `myfitlogic.com` (new GoDaddy domain Megan registered + provisioned `connections@myfitlogic.com` via M365 add-on, ~$5/mo). Ships May 8 AM. Customer-onboarding playbook lesson captured: when a deeper layer of the customer's stack is locked, stand up a parallel asset they fully own. `last_contact: 2026-05-06 → 2026-05-07`.
- [[wiki/people/michelle-fitlogic]] — added "May 7 — Cross-mentioned in Megan × Andres CRM handoff" section. Michelle continues to excel at relational side; **next-week's in-person CRM walkthrough explicitly targets Michelle as the primary trainee**. `last_contact: 2026-04-29 → 2026-05-07`.
- [[wiki/moil/active-projects]] — refreshed FitLogic row: status now "CRM handoff May 7"; Resend domain blocker resolved via `myfitlogic.com` workaround; AI-search inbound producing 4–5 calls/day; new "My Life on Purpose" LLC + coaching-cert course in development. Last biz touch 2026-04-29 → 2026-05-07.
- [[MEMORY]] — added 7-item May 7 block at top of "Immediate" section ("Megan × Andres CRM handoff (Resend blocker resolved)"); struck through 3 May 6 items the May 7 meeting closed (Andres-meet-Megan-this-afternoon, fitlogicfunctionalmedicine.com Resend verify, Taiwo screenshot). **Demoted 10-item Apr 24 carryover block** (13-day carry) to this log entry's archive block, plus single-line pointer to Run 38 Apr 21 demote. **Final count: 197 lines (under 200-line cap).**

**Index update:** [[index]] — Run 39 header; raw source count 477 → 478 (+1 Teams transcript); wiki page count 306 → 307 (+1 meeting page); meetings folder count 74 → 75.

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py`. Source file (`raw/teams-transcript-megan-andres-2026-05-07.md`) marked `ingested: true / ingested_at: 2026-05-07`.

**Key intelligence:**

1. **The Cloudflare workaround closes a 16-day Resend blocker without resolving the underlying access problem.** Megan handed Andres GoDaddy credentials on Apr 21 expecting that to be enough — but Resend verification has needed Cloudflare-layer DNS access ever since, which Megan doesn't have (likely an old vendor configured it). After two failed verification attempts (Apr 23 OAuth call + May 6 internal test), the May 7 decision was to **stop chasing access and stand up a parallel domain Megan fully owns end-to-end**. `myfitlogic.com` registered + provisioned in real-time during the call. **This is a customer-onboarding playbook lesson worth capturing in Moil 360 docs:** when a customer can hand over credentials at one layer of their stack but a deeper layer is locked, the right move is sometimes to spin up a parallel asset they fully own, not to keep chasing the missing access.

2. **AI-search is now a measurable inbound channel for FitLogic — first quantified data point in the campaign.** Megan reported ChatGPT + Claude AI Search drove **4–5 calls Tuesday alone, 2 confirmed conversions, and a small waitlist forming.** This is the first time any Moil customer has produced a quantified AI-search-traffic claim. Validates the lead-source taxonomy added per Megan's Apr 29 ask. If the pattern holds across additional weeks, it strengthens Moil's pitch to other practitioner customers (and potentially shifts the GTM emphasis from chamber/EDC → SMB-with-AI-discoverable-content).

3. **Megan is now operating in dual-business mode — "My Life on Purpose" LLC approved.** Separate entity from FitLogic. Megan is shopping for a new bank + payment processor (not top priority). Likely home for the **menopause/andropause coaching certification course** she's planning. Future Moil 360 surface candidate (course site + email + CRM). Track when Megan formalizes — this could be the first Moil customer to operate two distinct business surfaces on the platform.

4. **Pricing rewrite + $1,600/60-min IC competitor benchmark.** Megan rewrote the FitLogic pricing page after finding it was structured like a blog post listing a la carte service costs; repositioned around membership model. Discovered a competitor charging **$1,600 for a 60-min initial consultation** — orders of magnitude above FitLogic's current pricing. Signals FitLogic is under-priced; worth surfacing back to Megan if she ever revisits pricing.

5. **The "owner trains a manager" pattern continues — next-week in-person walkthrough explicitly targets Michelle.** Megan starts CRM tomorrow with low-volume sends + the test-contact flag specifically *"while Michelle learns the system."* Andres scheduled the next-week in-person visit with Megan + Michelle together. Onboarding videos/docs should target the manager, not the owner.

6. **Megan's competitive data points are unusually load-bearing.** She is one of very few customers actively comparing what other practitioners charge / how they market. Worth capturing her benchmarks systematically — they double as **competitive recon** for Moil's own pricing and positioning across the practitioner ICP.

7. **AI-search-as-inbound + Cloudflare-workaround-customer-playbook are both reusable patterns** worth surfacing back into [[wiki/moil/gtm]] and [[wiki/concepts/moil360]] in a follow-up pass once a second customer instance confirms the pattern (n=1 today).

**Source count:** 477 → 478. Wiki page count: 306 → 307. Meetings count: 74 → 75.

**Summary:** Run 39 ingests one Teams transcript and creates one meeting page + 4 page updates + MEMORY block. The high-signal items are (a) the Cloudflare workaround closing the 16-day Resend blocker via a parallel-asset pattern, (b) AI-search inbound producing the first quantified lead-channel data point at FitLogic, (c) Megan's new "My Life on Purpose" LLC opening a second business surface, (d) the $1,600/60-min IC competitor benchmark, and (e) the continuation of the owner-trains-manager delivery pattern with Michelle as primary trainee. CRM credentials ship tomorrow morning (2026-05-08).

**Run 39 demote block — Apr 24 carryover residue (13-day carry, owed but archived):**
- Andres + Ablad: AI-tool adoption pace working agreement
- Andres: reproducible demo-video workflow (Clio template; first artifact `clioremembers.com/demo`)
- Andres: redesign in-app onboarding guide for discoverability
- Adeleke: push auto-assign-Moil-360-license from staging → prod
- Jacob: rework outbound messaging to be conversion-driven
- HeyGen subscription: keep + max credits, drop, or replace with ChatGPT image2 + Capcut
- Andres → Daniel D. Mann: acknowledge Michelle-via-Megan hello; open "project together" thread
- Megan ongoing: forward every meeting invite to Andres (Apr 23 commitment, unverified)
- Megan payment plan: $500/mo × 3 → $250/mo × 6? Reply outstanding since Apr 19
- Andres: review Joshua's Apr 24 redlined HIVE Strategist PSAs; reply to Jessica @ VoyageAustin Magazine; Rashaka close on $600/yr vs $900/mo

---

## 2026-05-07 — Run 38: email-digest 2026-05-06 (Becky process-confusion + Andres reply pending; Joshua revised SoW; Heather post-coaching reply; Linda May 7/8 call window; Oscar consolidated Business Plan reply; first SMB-pivot outbound day)

**Trigger:** Single new raw file detected post-Run-37: `raw/email-digest-2026-05-06.md` (mirrored at `quartz/content/raw/`). Tue May 6 inbox + sent — 19 sent emails (9 Content 360 SMB cold pitches + 4 EDC close-outs + active client/partner replies), 10 received.

**Pages created:** 0 — no new entities surfaced (all senders/recipients are existing pages or one-off cold prospects that don't warrant per-person pages).

**Pages updated (8):**
- [[wiki/people/becky-torres]] — added "May 6, 2026 — Process-confusion signal: 'is feedback a call or in-person?'" section. Becky sent two emails on May 6 confused about how the iteration process actually works (videos? calls? in-person?). The Apr 28 brand-kit + May 6 "no proactive design changes" rule are necessary but not sufficient — Moil also owes her **process clarity** (one feedback channel + one cadence + an in-person walkthrough option leveraging local Buda proximity). `last_contact` 2026-05-06 (no change — same date as Run 37).
- [[wiki/people/oscar-esquivel]] — added "May 6 — Consolidated Business Plan reply" section. Andres replied at 21:36 UTC with One-Year Plan + 2 Growth Engines (Lakeline + Teravista) + 6 social documents — first substantive strategic written reply on Alloy account post-close. Closes Oscar's May 4 *"how detailed do we need?"* with a concrete framework. **Watch:** May 7–8 reply latency to confirm activation-handoff window is locking, not drifting. `last_contact` 2026-05-04 → 2026-05-06.
- [[wiki/people/joshua-edmond]] — added "May 6, 2026 — Revised Incubator Strategist SoW from morning meeting" section. Joshua sent revised SoW at 17:41 UTC after a same-morning meeting — first post-meeting same-day revision turnaround on the SoW track. **Andres action:** review before next Shannon/Jacqueline round-trip. Sequence now: Apr 21 PSAs → Apr 24 redline → Apr 30 Jacqueline-issued PSA → May 5 Casey calendar accept → **May 6 Joshua revised SoW**. `last_contact` 2026-05-04 → 2026-05-06.
- [[wiki/people/heather-skeen]] — added "May 6 — Reply to Andres's Apr 30 follow-up" section. Heather: out Friday, loves the feedback, will follow up next week or two. **Sets next-touch window to May 13–20**; nudge only if silent past May 20. Pairs with the same-day Teams invite Andres sent at 16:07 UTC for an in-person Providence meeting. `last_contact` 2026-04-30 → 2026-05-06.
- [[wiki/people/linda-horuke]] — added May 6 timeline rows. Jacob asked when she's available for a 30-min call (11:33 UTC); Linda replied same-day *"Do you have time today or tomorrow? I will make time on my end."* (15:30 UTC). High-intent same-day response window — lock the call **May 7 or May 8**. `last_contact` 2026-05-04 → 2026-05-06.
- [[wiki/moil/gtm]] — added "Cold campaign — May 6 update (Content 360 SMB pivot day; 9 SMB pitches + 4 EDC close-outs)" section. **First day where SMB sends outnumber chamber/EDC sends** — pipeline center-of-gravity has shifted. 9 Content 360 SMB sends across 4 hooks (*"30 days of content in 20 minutes"*, *"30-day content plan, automated"*, *"Most SMB owners tell us the same thing…"*, *"Business owners don't expect it to sound this good"*). Most diverse SMB-vertical day in the campaign (restaurants, renovation, signage, biotech, building supply, roofing, dessert, wellness coworking, moving). 4 EDC/Chamber close-outs (Wanda Seliski, Jayme Sellen, Joe Venhuizen, Sherri Yandry — Wisconsin cluster pruning). 1 Sioux Falls EDC narrative re-engagement (Jeff Griffin).
- [[wiki/moil/pipeline]] — refreshed Linda Horuke row to reflect May 6 same-day call-window offer; date stamp refreshed.
- [[MEMORY]] — added **May 6 email-digest action block** with 8 items (Becky process clarity reply, Joshua SoW review, B-Coach prod error escalation review, xAI Grok 4.3 retirement assessment, Linda May 7/8 lock, Megan afternoon meeting, Oscar reply-latency watch, Heather no-re-engage-before-May-13). **Demoted Apr 21 firefight residue** (10 items, 16-day carry) to this log entry's archive block; compressed older "Demoted" pointer to a single-line reference. **Final count: 198 lines (under 200-line cap).**

**Index update:** [[index]] — Run 38 header; raw source count stays 477 (the May 6 digest was already on disk per Run 37's note that it was auto-committed mid-run); wiki page count stays 306 (no new pages).

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py`. Source file (`raw/email-digest-2026-05-06.md` + the `quartz/content/raw/` mirror) marked `ingested: true / ingested_at: 2026-05-07`.

**Key intelligence:**

1. **Becky's confusion is a process gap, not a design gap.** The Apr 28 brand kit + May 6 "no proactive design changes" rule address *what* Moil should ship, but Becky's two May 6 emails (*"confused about the process"* + *"is review normally a call or in-person?"*) reveal she also doesn't know *how* to give feedback in a structured way. This is an unblock that requires Moil to publish a one-page process document (or in-conversation framing) — pick one feedback channel, set a cadence, offer the in-person walkthrough at SIREN as the natural anchor. Local Buda proximity is the lever; Andres has met Becky's family already (Apr 23 mom-visit), so an in-person rhythm is the path of least social friction.

2. **The Content 360 SMB cold lane is now a named track, not an experiment.** May 5 had 3 SMB sends; May 6 has 9 SMB sends across 4 distinct hooks. That's a 3× volume jump in 24 hours. The chamber/EDC chase is **shrinking** (only 5 chamber/EDC sends May 6 vs. 19 on May 5) while the Content 360 direct-to-SMB lane is **expanding**. Pipeline center-of-gravity has measurably shifted — worth tracking whether reply rates favor the SMB lane within the 7–14 day window.

3. **Andres's consolidated Business Plan reply to Oscar closes a 2-day open loop.** May 4 was the activation-handoff signal day (*"lock the success path before he drifts"*); May 5 was a quiet day on Oscar; May 6 21:36 UTC the substantive written reply landed (One-Year Plan + 2 Growth Engines + 6 social documents). The framework matches Oscar's May 4 strategy-package structure exactly (Lakeline + Teravista Growth Engines were Oscar's own documents) — which is the right move (mirror his framing) but also means the *content* is largely Oscar's with Andres's structure layered on top. Watch May 7–8 for whether Oscar treats this as the answer or asks for more depth.

4. **Joshua's revised SoW arriving same-day after the morning meeting closes the long-running PSA round-trip.** The SoW track has now been live since Apr 21 (Shannon's original PSAs). Joshua's May 6 revision is the **fifth contract artifact** in the sequence — and the first time a revision has come back same-day after a meeting rather than days later. Suggests SoW velocity is increasing as Joshua + Andres get closer to the actual signature event.

5. **Heather's "loves the feedback, follow up next week or two" is the cleanest post-coaching landing in the Apr 30 cohort batch.** She's not asking for more guidance — she's signaling she's about to do the homework. The MVP wedge is **landed, not drifting**. May 13–20 is the watch window; before then, do not push.

6. **Linda's "today or tomorrow" + "I will make time on my end" is the highest-intent reschedule signal possible.** She offered effort on her side — typical reschedule patterns are passive ("let me know what works for you"). The right Moil response is a same-day or next-day calendar link with 2–3 specific slot offers, not another back-and-forth. If Jacob/Andres let this slide to May 9+, the third silent week begins and the deal cools.

7. **Two production-side escalations forwarded May 6:** (a) **xAI Grok 4.3 release + xAI API model retirement** → Steve to assess impact + ship updates; (b) **B-Coach prod INTERNAL_ERROR** on `/plan/b-coach/profile` → Steve + Jacob to investigate the failed profile creation and close the loop with the affected client. Both forwarded by Andres without resolution captured in the digest. Add to the engineering watch — first model-retirement deadline pressure on Moil's stack since the campaign began.

**Source count:** Stays at 477 (the May 6 digest was already on disk after the Run-37 launchd auto-commit mid-run; this run is the actual ingestion, not a new file landing). Wiki page count stays at 306 (no new pages — all updates were to existing entities).

**Summary:** Run 38 ingests one digest file with no new entities surfaced and 8 page updates plus a MEMORY block addition. The high-signal items are (a) Becky's process-confusion signal that exposes a gap in Moil's iteration workflow, (b) the May 6 SMB-pivot in cold outbound (9 Content 360 SMB sends now exceeding chamber/EDC sends), (c) Andres's substantive Business Plan reply closing the Oscar activation-handoff loop, (d) Joshua's same-day SoW revision accelerating the PSA contract velocity, and (e) two production escalations (xAI retirement + B-Coach profile-creation error) routed to engineering without resolution. The 10 carryover Apr 21 firefight items are demoted to this log entry's archive block.

**Run 38 demote block — Apr 21 firefight residue (16-day carry, owed but archived):**
- Andres: surface per-campaign click-rate / open-rate dashboard (Megan asked Apr 21)
- Adeleke: Gemini→Grok→Qwen multi-model fallback for video gen; root-cause image-creation latency + intermittent template fails
- Jacob + Andres: fix `partners@moilapp.com` deliverability (Megan/Roxana/Jill all hit it; need per-customer sender or infra fix, P0)
- Product: fix business-plan switching UX bug — class-wide
- Jacob: resend Moil 360 license links to Megan, Siren, Roxana, Jill (paid Apr 20, never got link)
- Andres + Jacob: email every Buda cohort licensee with Moil 360 feature updates
- Security: move `cs@moilapp.com` password off Teams (Jacob leaked Apr 21)
- Andres: respond to Jacob's PRD proposal (carried from Apr 19)
- Jacob: fix Business Coach "not responding" bug — `stagebeta broken?` surfaced again Apr 21
- Andres: fix architectural regression — current app no longer uses business plan as single source of truth

---

## 2026-05-06 — Run 37: Andres × Taiwo working session (Siren Beauty design crisis + FitLogic CRM live-test; Resend domain still blocked; email-queue contention routed to research)

**Trigger:** Single new raw file detected post-Run-36: `raw/teams-transcript-meeting-to-go-over-ongoing-projects-2026-05-06.md` — 110-min Andres × Taiwo Teams working session (organizer Taiwo, scheduled 10–11 AM CT, ran ~50 min over to 12:31 PM CT). Two engineering deliverables in one session: (1) Siren Beauty website remediation after a wrong staging build went live and Becky pushed back, (2) live test of the FitLogic CRM + Resend email-campaign system before Andres's afternoon Megan meeting.

**Source meta correction (important):** The auto-generated summary at the top of the raw transcript invents a person named **"Faye"** as both the Siren Beauty owner and the CRM client. *There is no Faye.* The Siren Beauty owner is [[wiki/people/becky-torres|Becky Torres]]; the CRM-client domain `facelogicfunctionalmedicine.com` referenced in the meta is the auto-VTT mistranscription of `fitlogicfunctionalmedicine.com` ([[wiki/people/megan-miller|Megan Miller]] / [[wiki/orgs/fitlogic|FitLogic]]). Both projects are existing Tier-1 customers — **no new client entities created.** Flagged in the meeting page header and in this run's `## Patterns observed` so future readers can disambiguate.

**Pages created (1):**
- [[wiki/meetings/2026-05-06-andres-taiwo-ongoing-projects]] — meeting page with key decisions, action items, open questions, patterns observed, data points captured. `graph/leaf`.

**Pages updated (6):**
- [[wiki/orgs/siren-beauty]] — added "May 6, 2026 — Wrong Staging Build Crisis + 'No Design Changes Without Ask' Rule" section: brand pruning away from "science" framing toward pure feminine/mysticism axis (conflicts with existing tagline — capture in `brand.md`); duplicate-logo removal; mobile-responsive ASAP; Sanity CMS image-upload constraint flagged for next Becky conversation. `last_contact: 2026-04-28 → 2026-05-06`
- [[wiki/orgs/fitlogic]] — added "May 6, 2026 — CRM Live Test + Resend Domain Verification Still Blocked" section with state-of-system table (contact upload ✅ / WYSIWYG editor ✅ / Resend `moylab.com` sender ✅ / Resend `Megan@fitlogicfunctionalmedicine.com` sender ❌ / Gmail-API silent failover ⚠️ / open/click tracking ✅ / localhost-tracking-URL warning); P0 email-queue contention research routed; polish items captured (lead_source rename, AI vs manual sequence UI split, second-repo push). `last_contact: 2026-04-29 → 2026-05-06`
- [[wiki/people/becky-torres]] — added "May 6, 2026 — Wrong Staging Build → Brand Realignment + Reply Pending" section: Andres reply pending; brand-direction signal (Becky pruning the "science" framing); new "no proactive design changes without explicit ask" standing rule for engineering on her account. `last_contact: 2026-05-04 → 2026-05-06`
- [[wiki/people/megan-miller]] — added "May 6, 2026 — Pre-Meeting CRM Test + Domain-Verification Path" section: Megan added as test contact; afternoon Megan meeting scoped to walk her through GoDaddy DNS records for Resend; cross-page note that the Apr 23 "Megan owns everything" handover plan is creating exactly this kind of waiting-on-account-owner friction. `last_contact: 2026-05-04 → 2026-05-06`
- [[wiki/people/taiwo-ola-balogun]] — added "May 6, 2026 — Siren Beauty + FitLogic CRM working session (~110 min)" section: **Codex license deferred — Taiwo's call ("Claude is enough for now, sir")**; volunteered to scope CMS build (continues May 4 product-unification mandate); third repo-discipline relapse in 8 days; first refused-to-assume coaching from Andres ("That's lazy on our end to assume"); third take-ownership-of-deliveries coaching; **first unambiguous "well done" from Andres in captured transcripts** (analytics view). `last_contact: 2026-05-04 → 2026-05-06`
- [[MEMORY]] — added 8-item May 6 block ("Andres × Taiwo session: Siren Beauty + FitLogic blockers"); pruned 4 lines (struck-through Apr 30 follow-ups + 2 resolved Apr 29 AI-spend items); compressed Demoted block to a 1-line pointer to log.md trim. **Final count: 200 lines (cap exactly).**

**Index update:** [[index]] — Run 37 header; raw source count 475 → 476 (+1 teams-transcript); wiki page count 305 → 306 (+1 meeting page); meetings folder count 73 → 74.

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py`. Source file (`raw/teams-transcript-meeting-to-go-over-ongoing-projects-2026-05-06.md`) marked `ingested: true / ingested_at: 2026-05-06` (no prior frontmatter — minimal frontmatter prepended).

**Key intelligence:**

1. **Siren Beauty design realignment is now a standing engineering rule.** Becky reverted Moil's prior bias toward proactive design suggestions — *"Let's not make any more changes to any type of design until she asks for it."* Combined with her video-feedback request to remove "science" everywhere, the brand is mid-stream pruning the Apr-2026 *"Science-backed aesthetics"* tagline toward a purer *"feminine, mysticism, philosophy"* axis. Update `brand.md` in the Siren-Beauty repo before next iteration. **Open thread for Andres:** apology + reply email to Becky for the wrong staging build that went live (he had pushed a staging branch with applied colors she hadn't approved).

2. **🔥 FitLogic Resend domain verification is still the live blocker — three weeks after the Apr 21 plan to use `Megan@fitlogicfunctionalmedicine.com` as sender.** The Apr 23 "Megan owns everything from day one" handover model creates exactly this kind of friction — Moil cannot self-service Resend domain verification because Megan owns the GoDaddy. Andres's afternoon May 6 meeting is scoped to walk her through the DNS records in real time. Until then, sends from her domain silently fail over to Gmail API (Jacob's connected Gmail caught one mid-call) — and **the silent failover masks deliverability failures from the dashboard**, captured as architectural debt.

3. **🔥 Email-queue contention is unverified.** With 5,000 contacts × 5-email sequences × multiple potentially-overlapping campaigns × Vercel free tier (1 cron/day) × Gmail 50/day per-account cap, the system's behavior under contention is *completely unverified*. Could silently drop messages, unboundedly delay sends, or both. Andres explicitly refused Taiwo's *"yeah, I think they'll get sent on the same day"* answer — *"I don't want us to think. I want us to be 100% sure. That's lazy on our end to assume."* First time Andres has framed *engineering reasoning* (not just delivery cadence or repo discipline) as a standing discipline expectation. Routed to Taiwo as a Claude research task. Vercel premium ($20/mo) is the upgrade path that lifts the 1-cron/day cap.

4. **Codex license deferred — Taiwo's call.** Andres pitched buying a Codex license once the current project gets paid; Taiwo's response: *"Codex, I think Claude is enough for now, sir."* First time Taiwo has been the one *recommending* a tooling decision rather than receiving one — pattern shift from passive recipient to opinionated user. Ties forward to the May 4 cost-discipline standing rule.

5. **CMS / website-builder seeded for Taiwo to lead.** When Andres pitched the Moil 360 vision (*"click here, create your website → AI draft → CMS attach → CRM subscription"*), Taiwo offered *"I don't think it's very hard to build a content management system."* Andres: *"I love the way you're thinking, because that's exactly how we gotta think."* Continues May 4 product-unification mandate (Taiwo to design the unified packaged tool with email-sequence + blog generator + CRM as the three pillars) — adds CMS as a fourth pillar to scope.

6. **Three patterns reinforced through repetition (not yet internalized):**
   - **Repo-discipline relapse** — Taiwo confirmed FitLogic CRM updates are local-only, not pushed to the production-side repo. Same gap as Apr 28 (Connectex) and reinforced May 4. Third surfacing in 8 days.
   - **Take-ownership-of-deliveries coaching, take 3** — Andres again asked Taiwo to message *"here's what I delivered, here's what's next"* without being prompted. Same coaching as Apr 28 + May 4. Taiwo's response: *"Yes, sir."* — verbal, not behavioral yet.
   - **Refused-to-assume coaching, take 1** — new this call. Andres refused two "I think" answers from Taiwo (email queue contention + scheduling collision) and routed both to Claude-research. Continues the founder-discipline-on-engineering-reasoning pattern.

7. **First unambiguous "well done" from Andres to Taiwo in captured transcripts.** On the FitLogic CRM analytics view: *"Awesome. You did awesome here, man. Well done."* Worth tracking as a baseline — most of the captured Andres-Taiwo transcripts have been corrective, not affirmative. The CRM features that worked (WYSIWYG editor with variables, batch contact loading, open/click tracking, business-card scan, Resend↔Gmail failover) are real shipped product surface, not just demos.

8. **Mistranscription as a Brain hygiene signal.** The auto-summary at the top of the raw transcript invented a person ("Faye") and a domain ("facelogicfunctionalmedicine.com") that don't exist. Both are summarization artifacts — the meta-summarizer LLM hallucinated a name from `facelogic = fit logic mistranscribed`. Worth tracking: when a summarizer invents an entity that fits no known pattern, the cheapest disambiguation is a single grep against existing wiki/people/ + wiki/orgs/. Generalize as a future kb-health check candidate (*"raw transcript meta references entity X that has zero hits in wiki/"* → flag for human review).

**MEMORY trim 2026-05-06 — 7 demoted carryover items moved here for archive (originally demoted 2026-05-01):**
- Adeleke: codebase audit for OpenAI API usage; gpt-4o → gpt-5-mini; rotate keys after
- Adam Maxon @ pfdevelopment.com — Pflugerville Mentor Day reply
- Adeleke + Jacob: rotate GitHub webhook secrets (Apr 14 alert)
- Jesutomilola Omoniyi (Google xWF) — pick a reschedule time
- 2025 1040 in TaxDome — Melissa Jarbo / Martin Kutac / Ingrid refund-liability form
- Identify new social media client Andres signed; confirm Abiodun capacity
- Product UX: employer-can't-see-applicant-contact + candidate-message notifications; reply Megan with workaround + ETA

**Source count:** 475 → 476 (+1 teams-transcript ingested in this run). A second new file (`raw/email-digest-2026-05-06.md`) was auto-committed by the `email-digest` launchd job at 18:32 UTC — mid-Run-37 — pushing actual on-disk count to 477. Out of scope for this run; **deferred to Run 38**. Index Source count is updated to 477 to keep `kb-health` green.

Wiki page count: 305 → 306 (+1 meeting page).

**Summary:** Run 37 ingests one new file — a 110-min Andres × Taiwo working session — and produces one new meeting page + 5 page updates + a MEMORY block addition with cap-management trim. The high-signal items are (a) Siren Beauty's mid-stream brand evolution away from "science" + the new "no proactive design changes" standing rule, (b) FitLogic Resend domain verification *still* blocked three weeks after the Apr 21 plan, (c) the unverified email-queue contention behavior routed to Taiwo as a research task, and (d) Taiwo's first unambiguous "well done" from Andres on shipped CRM product surface. Three engineering-discipline patterns (repo, ownership, no-assumptions) are being reinforced through repetition without yet showing behavioral internalization. The raw transcript meta hallucinated a fictitious person "Faye" — flagged in the meeting page header and in this log entry to prevent future readers from creating a phantom wiki page.

---

## 2026-05-06 — Run 36: email-digest 2026-05-05 (Inna silence broken; Christine data-loss; Casey Incubator Strategist SoW; first warm Moil 360 local-Buda reply)

**Trigger:** Single new raw file detected post-Run-35: `quartz/content/raw/email-digest-2026-05-05.md` (mirrored at `raw/email-digest-2026-05-05.md`). Tue May 5 inbox + sent — 33 sent emails, 12 received, 19 chamber/EDC outbound, 3 Content360 SMB cold pitches.

**Pages created (4):**
- [[wiki/people/sarah-sanchez]] — Owner, Sunfield Spray Tans (Buda east-side Sunfield neighborhood). May 5 warm reply *"will check it out tomorrow"* on Moil 360 follow-up. **First warm Moil 360 reply on the local-Buda free-trial track.** `graph/leaf` + `person/customer`.
- [[wiki/orgs/sunfield-spray-tans]] — Sarah's solo spray-tan business stub. `graph/leaf`.
- [[wiki/people/linda-horuke]] — Owner, Jungle Flavorz. Re-engaging May 4 after missed Apr 28 Website Updates Discussion call (family illness). `graph/leaf` + `person/customer`.
- [[wiki/orgs/jungle-flavorz]] — Linda's business stub. `graph/leaf`.

**Pages updated (8):**
- [[wiki/people/inna-benyukhis]] — Added 🟢 May 5 *"Silence broken: May 14 + 18 videos uploaded"* section. **Closes the 12-day silence flagged in MEMORY's escalation block** (Apr 23 *"Please create the content"* directive → May 5 Google Drive upload). Partial unblock: video-creation pipeline alive; LinkedIn/IG publish-approval queue still pending. `last_contact` 2026-05-04 → 2026-05-05.
- [[wiki/people/christine-stjohn]] — Added May 5 *"Buda Top Neighborhoods data-loss thread"* section. **First documented data-loss incident from the Moil 360 free-trial code path** — Andres looped Steve + Jacob in to investigate. Operational signal for migration-safety verification before broader free-trial rollout. `last_contact` 2026-05-04 → 2026-05-05.
- [[wiki/people/casey-earley]] — Added May 5 *"Incubator Strategist Scope of Work accepted"* section. **First Casey-side calendar accept on the SoW track** — the contract surface anchoring Andres's Buda EDC role beyond the per-cohort license. `last_contact` 2026-05-04 → 2026-05-05.
- [[wiki/people/oscar-esquivel]] — Added May 5 quiet-day note in Recent Activity (no Oscar inbound/outbound; Roxana track stayed active via the Christine St John thread). Source list extended.
- [[wiki/people/sarah-cordano]] — Engagement Timeline extended with May 5 repeat *"Checking in from Bank OZK"* check-in. Source list extended.
- [[wiki/orgs/alloy-atx]] — Timeline extended with May 5 quiet-on-thread note (activation-handoff window remains open).
- [[wiki/moil/gtm]] — New *"Cold campaign — May 5 update"* section. 19 chamber/EDC sends (11 close-out + 4 story-led + 4 Wisconsin saturation) + 3 Content 360 SMB cold pitches (first parallel SMB direct-pitch track running alongside chamber/EDC track). Inbound: Sarah Sanchez warm + Casey Earley SoW accept. Operational artifacts: OpenAI Codex token-limit dispute (3 replies; 10x increase didn't honor on workspace login), Google Cloud compliance appeal (keys revoked + audit confirmed), Christine St John data-loss flag.
- [[wiki/moil/pipeline]] — Added Sarah Sanchez + Linda Horuke rows to Warm — In Conversation. Warm count 4 → 6; total active deals 23 → 25.

**Pages NOT created:**
- 19 chamber/EDC cold-outbound recipients (Tracy Propst, Debbie King, Jessica Holmvig, Allyson Wisniewski, Robin Anthony-Evenson, Hunter Aycock, Melissa McLean, Catherine Sanders, April Kopitzke, Ronda May, Hunter Gardner, Kari Swirth, Brad Gruhot, Ashley Demuth, Carol Fahrenkrog) — covered in [[wiki/moil/gtm]] May 5 update; no inbound replies; no individual pages until they re-engage.
- 3 Content 360 SMB cold-outbound recipients (Debby Larocque / Lone Star Roofing, Akeem Babatunde / CHG, Brooks Graham / Mervin and Sons) — same reason.
- Alyson Williams (Family Finance Global) — flagged as likely investor cold-spam in [[wiki/moil/gtm]] May 4 update; no page until verified.
- Abiodun Adekanmi Teams asset drop — already covered by [[wiki/people/abiodun-solomon]] standing operational pattern (no incremental page-worthy signal).

**Operating layer:**
- [[index]] — Run 36 header; raw source count 474 → 475 (+1 email-digest-2026-05-05); wiki page count 301 → 305 (+4); people 62 → 64 (+2 sarah-sanchez, linda-horuke); orgs 26 → 28 (+2 sunfield-spray-tans, jungle-flavorz).
- [[MEMORY]] — **no update.** MEMORY.md at 199/200 lines. May 5 items either (a) update existing MEMORY blocks (Inna silence resolved → tracked on entity page), (b) flow to entity pages (Sarah Sanchez + Linda Horuke + Casey SoW → page-level open items), or (c) ride existing carryover blocks (OpenAI / Google Cloud → already in Apr 29 AI-spend emergency). Christine data-loss is operationally captured on her entity page; if it escalates, promote to MEMORY.

**Key intelligence from Run 36:**

1. **🟢 Inna silence broken at exactly the escalation threshold.** Inna's May 5 02:20 UTC *"Videos for 05/14 & 05/18"* email lands within the same 24-hour window where MEMORY's Apr 29 *"silence past May 4–5 threshold"* watch was set. **The escalation system worked as designed** — the threshold was set on May 1, surfaced through three layers (entity page, signal brief, MEMORY) by May 4, and the relationship self-corrected on May 5 without requiring the direct-ping action item to fire. First documented case where the Brain's silence-tracking infrastructure let an action item resolve naturally before the human-trigger step. Worth flagging as a pattern: **silence-as-signal works**, but only if the threshold is explicit and the entity page surfaces it.

2. **🔥 First data-loss incident from the Moil 360 free-trial code path.** Christine St John's Buda Top Neighborhoods data was wiped by the **same free-30-days release** Andres queued in [[wiki/meetings/2026-05-04-monday-collaboration|May 4 Monday Collaboration]] for the broader rollout. The data-loss surfaced **before** the marketing rollout went wide — a fortunate sequencing. Steve + Jacob now own the diagnosis. **Migration-safety verification should block the broader rollout** until the free-trial code path is validated. Pairs with the Apr 29 FitLogic P0 bug list pattern: customer-facing surfaces are surfacing latent regressions faster than internal QA — the operational-discipline question is whether free-trial customers absorb the rollout-bug penalty or whether internal QA catches it first.

3. **🟢 First warm Moil 360 reply on the local-Buda free-trial track.** Sarah Sanchez (Sunfield Spray Tans) is the first solo-services SMB on Andres's local-Buda list to send a warm acknowledgement of a Moil 360 follow-up. Pairs with Christy Mawdsley (Run 35 — referral-driven) and Linda Horuke (Run 36 — re-engaging) to give the local-Buda track three concurrent warm prospects in the **first week the free-trial-rollout marketing strategy is queued**. The free-trial multiplier (1 cold pitch → 1 warm reply on the local list) is the leading indicator that the May 4 rollout strategy will compound.

4. **🟢 First non-cohort, non-PSA Buda EDC contract surface to advance.** Casey Earley accepted the *Incubator Strategist Scope of Work* calendar invite — the contract surface anchoring Andres's Buda EDC role beyond the per-cohort license. First written-contract advance with Buda EDC since the Apr 22 Helotes proposal (which itself was outside Buda). Sequenced behind the May 4 in-person PSA review with Jacquie. **Watch the SoW meeting outcome** — this is where Andres's annual EDC compensation/scope likely formalizes.

5. **🟡 OpenAI Codex token-limit dispute — workspace vs. personal account scoping.** OpenAI's *"10x increase as token of thanks"* gift didn't honor on `andres@moilapp.com` because the increase was scoped to personal ChatGPT, not the workspace/Business login. Andres burned 100→0% in 5–8 min on Codex 5.5 high/low. Asked for a max-plan discount as alternative. Continues the Apr 29 AI-spend observability emergency — the operational lesson is that **workspace-scoped vs. personal-scoped account boundaries are a budget-line variable**, not just an admin distinction. Watch May 6+ for OpenAI's reply.

6. **🟢 Google Cloud compliance appeal moved to documentation phase.** Google asked for *"additional info on remediation steps"* — Andres confirmed keys revoked + replaced + full audit done; previously-leaked key was the rotated one. Closes the active-firefight phase of the Apr 29 Gemini-API project policy-violation appeal. Now operational documentation rather than blocked-account triage.

7. **🟡 Wisconsin became first state to receive both a close-out batch AND a story-led re-engagement batch in same 24 hours.** Three close-out (April Kopitzke / New London, Ashley Demuth / Menomonie, Kari Swirth / Greater Beloit) + four story-led (Tracy Propst / Beaverdam, Allyson Wisniewski / Chippewa, Carol Fahrenkrog / Bayfield, Brad Gruhot / Marshall MN — bordering MN). First documented case of the campaign **A/B-testing the same state on the same day with two opposing template intents** (prune vs. re-engage). If a Wisconsin contact replies to the story-led variant after a prior close-out from the same Andres email, that's strong evidence the breakup-line is functioning as a re-open trigger rather than a goodbye.

8. **🟢 Content 360 SMB direct-pitch track now running parallel to chamber/EDC track.** Three SMB sends May 5 (Lone Star Roofing, CHG, Mervin and Sons) under the *"30 days of content in 20 minutes"* / *"Most SMB owners tell us the same thing…"* variants — multi-vertical (roofing, healthcare consulting, agribusiness). First daily cadence of SMB-direct outbound running alongside chamber/EDC. Pairs with the Apr 29 west-coast SMB push (David Mann, Shayan Guha, Jessica Reicher, Rob Pieroth) — the **SMB direct-pitch track is graduating from one-off batches to a daily lane**.

**Action-item delta:**
- **Closed (~1):** Inna silence-past-escalation watch (entity page) — silence broken May 5 02:20 UTC.
- **Opened (~3):** Andres → reply to Linda Horuke with two reschedule slots (carry over from May 4); Andres → watch for Sarah Sanchez free-trial signup at moilab.com (sunfieldspraytans@gmail.com), nudge in 7 days if no signup; Engineering (Steve + Jacob) → root-cause Christine St John's Buda Top Neighborhoods data-loss in the free-trial code path before broader rollout.

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py`. Source files (`raw/email-digest-2026-05-05.md` + `quartz/content/raw/email-digest-2026-05-05.md`) marked `ingested: true / ingested_at: 2026-05-06`.

**Source count:** 474 → 475 (+1 email-digest). Wiki page count: 301 → 305 (+4: sarah-sanchez, sunfield-spray-tans, linda-horuke, jungle-flavorz).

---

## 2026-05-05 — Run 35: Christy Mawdsley discovery call (Roxana Yglesias outbound referral)

**Trigger:** Single new raw file detected by post-Run-34 scan: `raw/teams-transcript-christy-andres-2026-05-05.md` — 49-min Teams discovery call with Christy Mawdsley (Wholeness Acupuncture and Integrative Medicine, ZIP 78641), referred by [[wiki/people/roxana-yglesias|Roxana Yglesias]] (mutual BNI tie). Signal threshold met (warm prospect + first documented Roxana referral conversion + new entity surface).

**Pages created (3):**
- [[wiki/people/christy-mawdsley]] — Solo licensed acupuncturist + functional medicine provider, doctoral candidate, three kids. Cash-pay only, women 45–75 ICP, anti-influencer-vibe positioning. Word-of-mouth concentration (Pilates studios + Austin chain of yoga studios + physician referrals). `graph/spoke` + `person/customer`.
- [[wiki/orgs/wholeness-acupuncture]] — Christy's solo practice; one rented room inside a larger health clinic; ranks #1 in Google for full business name; Instagram `@the_embodied_acupuncturist` exists but empty. `graph/leaf`.
- [[wiki/meetings/2026-05-05-christy-mawdsley-discovery]] — Meeting record with full decisions + action items + coaching color. `graph/leaf`.

**Pages updated (3):**
- [[wiki/people/roxana-yglesias]] — Added 2026-05-05 row to engagement timeline: **first documented Moil customer-to-prospect referral conversion of 2026.** `last_contact` bumped Apr 23 → May 5.
- [[wiki/moil/pipeline]] — Added Christy row to Warm — In Conversation; warm count 3 → 4; total active deals 22 → 23; `last_updated` Apr 14 → May 5.
- [[MEMORY]] — Added 🔥 May 5 Christy section at top of Immediate-This-Week block; compacted Apr 5–12 Technical-debt block into one consolidated line to stay under 200-line cap (now 199 lines).

**Operating layer:**
- [[index]] — Run 35 header; raw source count 473 → 474 (+1 christy transcript); wiki page count 298 → 301 (+3); people 61 → 62 (+1 christy); orgs 25 → 26 (+1 wholeness-acupuncture); meetings 72 → 73 (+1 discovery).

**Key intelligence from Run 35:**

1. **🟢 First documented Moil customer-to-prospect outbound referral conversion of 2026.** Roxana Yglesias (Alloy ATX, paying since Apr 20) actively reached out to Christy and praised Andres as *"honest, trustworthy, good"* — a clean, unsolicited reference call. This is the operational proof that the Apr 14 Roxana onboarding paid forward into a closing-eligible warm pipeline entry within ~3 weeks. The Roxana page now anchors a referral-network sub-pattern; future Roxana-sourced names should grep here.

2. **🔥 Education-as-content-engine wedge confirmed for Moil 360.** Christy's *"there's a lot I just wish I could tell people somewhere so it was like a knowledge hub almost"* (transcript 15:48) is the textbook wedge for Moil 360's monthly education theme. Pairs with Andres' Facebook-over-Instagram framing for the 45–75 segment. **First entity in the Brain that fits the education-themed Moil 360 setting cleanly.**

3. **🔥 Anti-paid-ads framing as discovery-call default.** Andres' *"don't put a penny into ads until we figure out what a strategy looks like"* line landed cleanly with a prospect who was already considering a Meta ad spend. Worth promoting to a named [[wiki/moil/gtm]] sub-pattern alongside the Cohort-4 *"if I started tomorrow"* coaching framework — same surgical-question shape, different problem.

4. **🟢 Cash-pay solo-practitioner ICP candidate.** Christy is the cleanest representative yet of the **cash-pay, women-led, 45–75-clientele, word-of-mouth-saturated** ICP. If she converts post-trial, this slot is a pattern Moil should be hunting for in cold outbound (e.g., functional-medicine practitioners, integrative-clinic operators, naturopaths). Worth flagging to [[wiki/moil/icp]] in a future run if she signs.

5. **🟢 BNI as referral channel signal.** Two independent data points now: Roxana Yglesias (paying customer) and Christy Mawdsley (warm prospect) both quit BNI but the relationship from BNI persisted into a Moil deal. **BNI is acting as a customer-acquisition substrate for Moil even when Andres isn't in the room** — first time this pattern surfaces explicitly in the Brain.

6. **🟡 Demo-bug surfaced live.** Pitch-deck generation produced a one-slide deck on first attempt (Andres labeled it a bug live, retried, second attempt worked). Andres said *"that's a bug on my end"* — not catastrophic but logged for engineering. Pairs with the FitLogic P0 bug list pattern: customer-facing demos are surfacing latent regressions faster than internal QA.

**Action-item delta:**
- **Closed (~0):** None this run.
- **Opened (~1):** Andres → 1:1 onboarding call once Christy completes Moil 21 questions; help her stand up referral program post-onboarding (her highest-leverage move). Watch for free-trial signup at moilab.com (Christymawdsley@gmail.com); nudge if 21Q not started within 7 days.

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py`. Source file marked `ingested: true / ingested_at: 2026-05-05`.

**Source count:** 473 → 474 (+1 christy transcript). Wiki page count: 298 → 301 (+3: christy-mawdsley, wholeness-acupuncture, 2026-05-05-christy-mawdsley-discovery).

---

## 2026-05-05 — Run 34: email-digest 2026-05-04 + signal-briefs 2026-05-03 & 2026-05-04

**Trigger:** KB-agent ingest of three new raw sources committed by automation:
- `quartz/content/raw/email-digest-2026-05-04.md` (also mirrored at `raw/email-digest-2026-05-04.md`) — Mon May 4 inbox + sent.
- `quartz/content/raw/signal-briefs/signal-brief-2026-05-03.md` — Sun May 3 cross-source brief (86 files / 3 source types).
- `quartz/content/raw/signal-briefs/signal-brief-2026-05-04.md` — Mon May 4 cross-source brief (439 files / 14 source types).

**Pages created (1):**
- [[wiki/people/sarah-cordano]] — Bank OZK banker-of-record stub. Inbound *"Checking in from Bank OZK"* email implies Moil business account opened ~2025-07. First time the banker-of-record surface lands in the Brain. Tagged `graph/leaf` + `person/vendor`.

**Pages updated (4):**
- [[wiki/people/oscar-esquivel]] — Added 2026-05-04 row to Engagement Timeline + new "May 4 — Activation-handoff window" section. Three threads in one day: ChatGPT-drafted business plan inbound, 6-doc strategy package inbound (Lakeline & Teravista Growth Engines + Events Strategy + Marketing Playbook + Authority Events), paired Roxana onboarding push. Same operational phase that produced the FitLogic P0 bug list.
- [[wiki/orgs/alloy-atx]] — Timeline extended with May 4 activation-handoff entry.
- [[wiki/people/inna-benyukhis]] — New "May 3–4 — Silence past escalation threshold (now 4 days)" section. Inna absent from both digests; LinkedIn/IG queue blocked since Apr 27; CRM demo slipped a week; pipeline page (`wiki/moil/pipeline.md`) staleness flagged. Action: direct ping today.
- [[wiki/moil/gtm]] — New "Cold campaign — May 4 update" section. Captures the **narrative-as-product convergence**: Carol Vaccaro's *"entrepreneurs arrive with research and plan done"* anecdote is the same narrative running on accelerator app + cold outbound + free-trial rollout strategy. Volume dropped from late-Apr peak (24/day) to ~7/day; multiplier moved from send-count to narrative reuse. Also captures the Sarah Cordano banker-of-record + Alyson Williams investor cold-spam flag.

**Pages NOT created (signal-briefs convention):**
- Per Run 32 + Run 28 precedent, daily signal briefs do **not** get their own wiki pages — they are derivative cross-source synthesis. Their intelligence flows through to the entity pages (Oscar, Alloy ATX, Inna, GTM) and the daily log entry. The Apr 15–30 series consolidation lives at [[wiki/summaries/signal-briefs-2026-04-15-26]]; May briefs are tracked here in log.md headers until the next consolidation pass.

**Operating layer:**
- [[index]] — Run 34 header; raw source count 473 → 475 (+2: signal-briefs are new files; email-digest already existed at root with the same content); wiki page count 297 → 298 (+1 sarah-cordano); people count 60 → 61.
- [[MEMORY]] — **no update.** MEMORY.md already at 199/200 lines; today's items are tracked on entity pages + this log entry. Inna nudge already on the page in 🔥-tier; Oscar activation-handoff is live-watch but Andres has the signal via the Oscar entity page recent-activity block.

**Key intelligence from Run 34:**

1. **🔥 Alloy ATX has entered the FitLogic-style activation-handoff window.** Oscar's first-ever 3-thread day (May 4) lines up with Roxana's onboarding push (2 Teams invites + 21-question nudge) — same shape as the FitLogic delivery week that produced the P0 bug list. The window is the moment to lock the success path before drift; the entity page now flags it explicitly so any future ingestion that touches Alloy can reference the pattern instead of re-deriving it.

2. **🔥 Inna silence is now 4 days past the May 4–5 escalation threshold from MEMORY.** Two consecutive signal briefs (May 3 + May 4) flagged it; the email-digest contains zero Inna touches. Three concurrent stalls: LinkedIn/IG publish queue (since Apr 27), CRM demo (slipped one week from Apr 28), retainer trust capital. The Brain has surfaced this through three independent layers (entity page, signal brief, MEMORY) — the next layer that can act is human (Andres direct ping).

3. **🔥 The cold campaign has crossed into "narrative-as-product."** Carol Vaccaro's *"entrepreneurs arrive with research and plan done"* anecdote on May 4 is the **same** narrative running on three surfaces simultaneously: (a) the live accelerator-application drafting (15+ claude-session entries), (b) the 4-prospect EDC outbound batch, (c) the [[wiki/meetings/2026-05-04-monday-collaboration|May 4 Monday Collaboration]] free-trial rollout marketing strategy. The send-volume drop (24/day → ~7/day) is not a slowdown — it's a multiplier shift from raw count to narrative reuse across product surfaces. Worth promoting "EDC-feedback narrative" to a named asset alongside the demo + close-out variants in [[wiki/moil/gtm]] templates.

4. **🟡 First banker-of-record surface in the Brain.** Sarah Cordano (Bank OZK, sarah.cordano@ozk.com) sent the 10-month relationship check-in. Implies the business account opened ~2025-07. Pairs operationally with the May 4 Monday Collaboration credit-card / Groq / Gwen blocker — a banker conversation may be the right channel rather than another support ticket. New entity tagged `graph/leaf` because vendor relationships shouldn't crowd the network graph until they become deal-relevant.

5. **🟡 Investor cold-spam flag (Alyson Williams).** *"$2M to $35M family office allocation"* + sender domain `familyfinanceglobal.info` + round-number framing fit common scam-pattern. Captured in the GTM page as a do-not-respond marker rather than ignored — future runs that see similar inbound should be able to grep this pattern.

6. **🟢 The signal-brief layer is now working as designed.** The May 3 brief flagged Inna silence + Brain-infra-vs-priorities drift; the May 4 brief flagged Oscar activation-handoff + Inna silence extension. Both are propagating to entity pages this run rather than dying inside the brief. The audit thesis from `wiki/summaries/brain-audit-2026-05-03` ("input-rich, reflection-poor") is partially closing — synthesis output is reaching the wiki, even if synthesis scripts still don't read ChromaDB.

**Action-item delta:**
- **Closed (~0):** None this run — all entries are observation/state-capture rather than action-completion.
- **Opened (~3):** Andres → direct ping Inna today (silence past threshold); Andres → lock Alloy ATX success path this week (activation-handoff); Andres → consider Bank OZK check-in (low urgency, useful for credit-card escalation).

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py`. Source files marked `ingested: true / ingested_at: 2026-05-05`.

**Source count:** 473 → 475 (+2: 2 new signal-brief files; the email-digest existed at root before this run, only the quartz mirror is the second copy). Wiki page count: 297 → 298 (+1 sarah-cordano).

---

## 2026-05-04 — Run 33: Mon May 4 — 3 Teams transcripts (Christine+Kat, Claudia, Monday Collaboration)

**Trigger:** Automated scan for unprocessed `raw/` files. Three high-signal new files committed by `teams_ingest.sh` at 18:23:
- `raw/teams-transcript-monday-collaboration-2026-05-04.md` — 52 min, Andres + Adeleke + Taiwo + Jacob + Ablad. **Cost-discipline standing rule + product-unification mandate + free-trial rollout decision.**
- `raw/teams-transcript-claudia-andrés-2026-05-04.md` — 48 min, Andres × Claudia Sanchez (Nativa Med Spa). **HIVE Cohort 4 1:1.** May 21 grand-opening event strategy + medical-credentials differentiation + ICP shift to $120K+ Buda households.
- `raw/teams-transcript-christine-andres-2026-05-04.md` — 71 min, Andres × Christine St John × Kat Eyers (joint). **HIVE Cohort 4 1:1.** Wine concept anchored on the Buda EDC Train Depot opportunity.

**Pages created (9):**
- [[wiki/people/christine-stjohn]] — Buda HIVE Cohort 4; co-founder of unnamed wine concept; Water To Wine club member (resigning); the impulsive jumper
- [[wiki/people/kat-eyers]] (Kathryn Eyers) — Buda HIVE Cohort 4; founder of [[wiki/orgs/unwrapped-uncorked-events|Unwrapped Uncorked Events]] (~10 yr); the cautious planner; 3 kids
- [[wiki/people/claudia-sanchez]] — Buda HIVE Cohort 4; founder of [[wiki/orgs/nativa-medspa|Nativa Med Spa]] (1626 corridor); medical-credentials differentiation
- [[wiki/orgs/unwrapped-uncorked-events]] — Kat's existing service-event business
- [[wiki/orgs/nativa-medspa]] — Claudia's medical aesthetics practice + May 21 ribbon-cutting
- [[wiki/orgs/water-to-wine]] — Mill & Grain franchise (Dane); fiercest competitor for the Christine + Kat concept; offered custom-label partnership
- [[wiki/meetings/2026-05-04-christine-kat-coaching]] — joint 1:1; Train Depot anchored; Roundabout skipped; Sarah meeting locked Tue May 12
- [[wiki/meetings/2026-05-04-claudia-sanchez-coaching]] — Nativa marketing + opening event strategy; medical-vs-esthetician moat
- [[wiki/meetings/2026-05-04-monday-collaboration]] — cost-discipline rule + Gemini 2.5 Pro → Flash Lite + product unification + free-trial rollout

**Pages updated (5):**
- [[wiki/people/hive-cohort-members]] — Cohort 4 table extended with Claudia + Christine + Kat rows; Sarah open-question now flags Cohort 4 returning-participant possibility
- [[wiki/orgs/buda-edc]] — Cohort 4 row updated with 3 new May 4 1:1s; new "Train Depot opportunity" section (Christine + Kat vs. Sarah, EDC-as-low-risk-landlord framing); HIVE Clients Also Using Moil expanded
- [[wiki/people/adeleke-tolulope]] — May 4 cost-discipline switch + Saturday Gemini spike root-cause + AI-spend partly-resolved status
- [[wiki/people/taiwo-ola-balogun]] — May 4 product unification mandate + open-source email-infrastructure project + Moil 360 license dogfooding
- [[MEMORY]] — added 14 new May 4 items (Cohort 4 1:1 follow-throughs + Monday cost-discipline + free-trial marketing strategy + accelerator application); compacted Apr 24 + Apr 28 + Apr 21 + Apr 29 + technical-debt blocks; closed PSA in-person mtg + Christine StJohn lunch (both held). 199 lines.

**Operating layer:**
- [[index]] — Run 33 header; raw source count 469 → 472 (+3); wiki page count 288 → 296 (+8); people 57 → 60; orgs 22 → 24; meetings 69 → 72

**Key intelligence from Run 33:**

1. **🟢 HIVE Cohort 4 1:1 → MVP-decision conversion is now 4/4.** All four 1:1s with Cohort 4 participants (Heather Apr 30, Caro Apr 30, Claudia May 4, Christine + Kat May 4) have produced a **clear, narrowed wedge in a single session.** The ratio held even when the format flipped (joint 1:1 with two co-founders). This isn't 4 random data points anymore — it's a repeatable conversion engine for HIVE Cohort 4.

2. **🔥 Train Depot opportunity surfaces as a new EDC product Andres can broker.** The EDC is renovating a downtown Buda Train Depot space (~300 sq ft + outdoor patio) at below-average rent on a 1-yr lease, with city-funded marketing tailwind and a no-pursuit clause if the tenant fails. Andres anchored Christine + Kat's entire HIVE business plan on this footprint — "be the first applicants with a concrete plan" is a deliberate competitive move against Sarah (the bookstore + wine concept). The Depot is **the EDC functioning as low-risk B2G real estate**, not a typical commercial real-estate landlord. The "first applicant with a concrete plan wins" race has ~6 weeks. **First time the EDC's downtown real-estate program shows up as a HIVE deliverable in MEMORY.**

3. **🔥 Sarah (bookstore + wine, C2/C3) is likely Cohort 4 — and a direct competitor for the Depot.** Andres said *"talked Sarah out of [the Roundabout]"* during the Christine + Kat session, and her bookstore+wine concept is now competing for the same Train Depot space. The cohort-members page Sarah row (C2/C3, sarah-hive-cohort.md) may be the same person. Tue May 12 is competitive recon for Christine + Kat. Confirm with Casey/Jacquie.

4. **🔥 Cost-discipline standing rule adopted live.** Andres' new bar applies to every backend feature push: *"Is this the most cost-efficient model that still does the job?"* Saturday's Gemini spike was caused by the weekly health-summary cron iterating every active user's chats with 2.5 Pro. Live root-cause + immediate-switch decision (2.5 Flash Lite + active-user gate) closed in the call. **First time AI-spend has been treated as a recurring engineering-discipline question rather than a one-off audit.** Weekly Monday cost review is now permanent.

5. **🟡 OpenAI + Google project crisis from Apr 29 partly resolved.** OpenAI refunded $30 May 3 (credit note 3937); account unlocked. The reinstated Google project (`Moil-Dev`, key ending `0270710133`) is the **Google-auth key**, not the live Gemini API key (`0251`) — the live billing surface was untouched all along. Per-feature accounting on Gemini + OpenAI still pending.

6. **🟢 Free 30-day Moil trial rolling out to all new signups.** Andres committed to draft the matching marketing strategy. This is the operational complement to the accelerator application (license-sales traction over website-creation framing). Moves Moil from *"opt-in trial"* to *"trial-by-default, monetize after value"* — implications for cold campaign messaging, Moil 360 onboarding flow, and the existing Apr 24 auto-assign-license feature (Adeleke's staging→prod push).

7. **🟢 Product unification mandate.** Taiwo's four side-projects (FitLogic, Inna CRM, Siren Beauty, ConnectX) are now an explicit unified-packaged-product workstream rather than four parallel custom builds. Three pillars: email-sequence + blog generator + CRM. Plus an open-source email-infrastructure project Taiwo identified as a Resend replacement (lifts the 100 emails/day cap). **Concretizes the Apr 28 "build for agents" framing**: Moil sells the package, the package powers each customer build.

8. **🟢 Pricing rule new for the Brain (from Claudia coaching):** *"You give the spot to a person who'll pay you with a discount → you take the spot from a person who could have paid full price."* Discount only after the profit is locked. Generalizable beyond Nativa — applies to Andres' own discount/breakup-day cadence in [[wiki/moil/gtm]].

9. **🟢 Andres' "if I started tomorrow" framing emerges as a recurring coaching tool.** Used identically with Heather (Apr 30 daycare wedge), Caro (Apr 30 women-coworking wedge), Claudia (May 4 fixed-costs gating), and Christine + Kat (May 4 Depot anchor). Worth promoting from coaching-color to a named coaching framework — candidate for [[wiki/concepts/]] page in a future run.

10. **🟢 Christine + Kat are deliberately balanced co-founders.** Christine = "I like to wing it. We'll figure it out." (impulsive jumper). Kat = 10 years of operating Unwrapped Uncorked Events (cautious planner). Andres explicitly framed the pairing as a strength, not a problem to manage. Worth tracking as a HIVE Cohort 4 healthy-pair pattern.

**Action-item delta:**
- **Closed (~5):** PSA in-person mtg held May 4 morning; Christine StJohn lunch DELIVERED (was on Next-2–3-weeks); OpenAI account dispute (refunded May 3); Moil-Dev Google project reinstated
- **Opened (~14):** Andres → intro Garrett if Depot path opens; Andres → send Claudia Kyle businesses list; Andres → realtor/women-entrepreneur event for Claudia; Andres → confirm Sarah-C4 identity; Christine + Kat homework (6 items); Claudia homework (8 items); Adeleke → Flash-Lite cron switch + active-user gate; Steve → assign Taiwo Moil 360 license; Taiwo → email infra link + product unification audit; Andres → free-trial marketing strategy; Andres → accelerator application (license-sales framing); Andres → resolve credit-card Groq/Gwen blocker

**Sync step:** `bash scripts/sync_wiki.sh`. **Health step:** `python3 scripts/kb-health.py` (frontmatter-marked source files; 8 new wiki pages). Source files marked `ingested: true / ingested_at: 2026-05-04`.

**Source count:** 469 → 473 (+4: 3 new Teams transcripts ingested + 1 reconciliation drift fixed). Wiki page count: 288 → 297 (+9 = 3 people + 3 orgs + 3 meetings).

---

## 2026-05-04 — Run 32: Frontmatter reconciliation pass (450 source files) + signal brief 2026-05-03

**Trigger:** Bulk `/brain-ingest`-style request listing 419 historical raw sources (the entire ingestion backlog from Runs 1–31) plus all 236 `raw/sessions/claude-code-*.md` files. Cross-checked against this log: every file in the request was already substantively ingested in an earlier run. The actual gap was that source-file frontmatter was never updated with `ingested: true / ingested_at`, leaving downstream consumers (the `/brain-ingest` skill, kb-health, future re-runs) unable to tell processed sources from unprocessed ones.

**One genuinely new source ingested:**
- `quartz/content/raw/signal-briefs/signal-brief-2026-05-03.md` (committed May 4 06:00 by `daily-correlator.py` — May 3 cross-source synthesis covering 86 files across 3 source types). Intelligence already captured in [[wiki/summaries/brain-audit-2026-05-03]] (the "input-rich, reflection-poor" / synthesis-doesn't-query-ChromaDB pattern) and [[MEMORY]] (Inna silence threshold flag, May 4–5 nudge). No new wiki pages required — signal briefs are meta cross-source synthesis, not external knowledge to graph (per Run 31 precedent for `wiki/summaries/brain-audit-2026-05-03`).

**Frontmatter backfill (450 files):**
- 435 files updated with `ingested: true` / `ingested_at: 2026-05-04` appended to existing YAML frontmatter
- 16 files (mostly `raw/odtr-*.md` legacy ODTR exports) had no frontmatter at all — minimal frontmatter prepended
- 15 files were already marked ingested (no-op)
- 0 files missing
- Touched: every file under `raw/sessions/` (236), `raw/meetings/` (81), all `raw/odtr-*.md` (61), all `raw/email-digest-2026-04-{14..30}.md`, all `raw/teams-*.md` and `raw/teams-transcript-*.md` from Apr 12–30, all `raw/email-history-*.md`, all `raw/hive-*.md` HIVE program docs (24), all `raw/x-bookmarks-*.md` (4), `raw/buda-hive-edc-*.md`, `raw/weekly-sessions-*.md`, `raw/imessages-people-*.md`, `raw/outlook-emails-*.md`, `raw/moil-documents-*.md`, `raw/moilapp-website-*.md`, `raw/facebook-pages-*.md`, `raw/github-project-tracker.md`, `raw/know-me-extraction-prompts.md`, `raw/onedrive-transcripts/*.md`

**Pages created (0):** All target pages already exist in `wiki/`.

**Pages updated (1):**
- [[wiki/weekly/2026-05-04]] — fixed broken wikilink `wiki/weekly/My` → `wiki/weekly/2026-05-03` (template placeholder leaked through; flagged by `kb-health.py` Check 2)

**Why no decomposition into per-file log lines:** Each of the 419 historical files is already documented in its original ingestion run (Runs 1–31). Re-listing them would add ~450 lines of duplicate provenance to log.md without adding intelligence. The frontmatter flag on each source file is the durable record — `grep -l "ingested: true" raw/` is the new source of truth for what's been processed. Future runs read frontmatter, not log.md, to decide what to skip.

**Operating layer:**
- [[index]] — Run 32 header, raw source count 469 → 469 (no new files added; signal-brief lives in `quartz/content/raw/signal-briefs/` outside RAW_DIR rglob), wiki page count 287 → 288 (kb-health-detected drift from prior run reconciled — 288 is the actual count), summaries unchanged at 21
- [[MEMORY]] — **no update.** Frontmatter-only reconciliation creates no new external commitments. Inna nudge already 🟡-flagged, audit Week 2–3 items already tracked in [[wiki/summaries/brain-audit-2026-05-03]]
- Daily-correlator output `signal-brief-2026-05-03.md` — referenced from log only; no wiki page (per Run 31 precedent)

**Key intelligence from Run 32:**

1. **The 419 unmarked files are evidence of an old gap in the ingestion protocol — fixing it now means `kb-health.py` and `/brain-ingest`'s "find unprocessed" pass will be accurate from this point forward.** Earlier runs (1, 2, 6, 12, 15, 30, 31) wrote the *log entry* documenting what was ingested but never round-tripped a `ingested: true` marker back to the source file. The protocol in `quartz/content/CLAUDE.md` § Ingestion protocol implies the marker but didn't enforce it. This run closes the gap retroactively.

2. **Signal-brief-2026-05-03 is the second day in a row where the cross-source layer has confirmed the audit's "input-rich, reflection-poor" thesis with fresh receipts.** May 2 brief: John Costilla praise + Nate Herk bookmark are the same production loop. May 3 brief: Andres spent Sunday on Brain infra (URGENT Quartz GH-Pages diagnosis) instead of MEMORY 🔥 items. The synthesis layer is now reliably surfacing pattern-vs-priority drift — the next test is whether anyone (Andres, future-Claude) acts on it. **Brief itself is the action signal; no wiki update needed for the brief itself.**

3. **Inna silence anomaly extends to ~3 days now (last meaningful touch Apr 28 in-person, podcast re-cuts sent May 1 14:59 UTC, no reply through May 3 23:59 UTC).** MEMORY.md threshold was May 4–5; today is May 4 → nudge is due TODAY. Already in MEMORY 🟡; no new commitment created.

4. **Karpathy `## Related`-block linter is the right discipline for this kind of reconciliation work.** Just like `lint-related.sh` enforces backlinks on every `wiki/people/*` and `wiki/projects/*` page, a future `lint-ingested.sh` could enforce that every file in `raw/` (excluding `raw/sessions/` automation pollution) has `ingested: true` or appears in a "skipped, low-signal" registry. Ticketed as a Week-3 candidate but **not** added to MEMORY — it's internal Brain infrastructure (per Run 31 rule).

**Sync step:** `bash scripts/sync_wiki.sh` mirrors all updated source files into `quartz/content/raw/`. **Health step:** `python3 scripts/kb-health.py` after sync — drift on Check 6 (wiki count 287→288) reconciled in this entry; broken-link error on `wiki/weekly/2026-05-04.md` fixed.

**Source count:** 469 → 469 (no new files; signal-brief in `quartz/content/raw/` is not counted by `kb-health.py`'s RAW_DIR rglob). Wiki page count: 287 → 288 (no new pages; existing-count reconciliation only).

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

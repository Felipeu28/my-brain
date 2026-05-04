---
type: audit
date: 2026-05-03
tags:
  - graph/leaf
ingested: true
ingested_at: 2026-05-03
---

# Brain Ingestion & Synthesis Audit — 2026-05-03

Scope: weekly-rhythm view of what the Brain captures, where it lands, whether the cron-equivalent is actually running, and whether the synthesis layer is doing useful work or just generating files. Reviewed against the last 30 days of activity.

The headline before details: capture is mostly working, but **two synthesis pillars are silently dead** (entity-graph, weekly-operating-brief), one synthesis pillar is **mechanical not editorial** (weekly-sessions rollup), and **none of the synthesis scripts query ChromaDB** despite the index running daily. The Brain is writing more than it reads.

---

## A) What gets ingested weekly (the inputs)

All schedules below are read from `pi-workspace/launchd/*.plist` (not from comments in the script). Volume = number of files written or commits in the last 7 days where measurable; otherwise last 30 days.

### Capture jobs (data in)

| Job (plist label) | Schedule (from plist) | Script | Source | Destination | 30-day volume |
|---|---|---|---|---|---|
| `morning-briefing` | Mon–Fri 08:45 | [`bin/morning-briefing.sh`](../../../pi-workspace/bin/morning-briefing.sh) | Microsoft 365 Graph (calendar + mail + sent), GitHub, `compute-last-contact.py` | `quartz/content/raw/briefings/briefing-YYYY-MM-DD.md` + email to andres@moilapp.com | 13 briefings (last fresh briefing is Apr 29 in `outputs/briefings/`; **today's at the canonical path is missing per `outputs/health/heartbeat-latest.md`**) |
| `teams-daily` | Daily 18:00 | [`bin/teams-pull.sh`](../../../pi-workspace/bin/teams-pull.sh) | Graph API (channel msgs + chats + meeting transcripts via `m365` CLI) | `raw/teams-YYYY-MM-DD.md` (digests) and `raw/teams-transcript-{slug}-YYYY-MM-DD.md` | 8 daily digests + 9 transcripts |
| `email-digest` | Mon–Fri 18:30 | [`bin/daily-email-digest.sh`](../../../pi-workspace/bin/daily-email-digest.sh) | Graph API inbox + SentItems (last 24h) | `raw/email-digest-YYYY-MM-DD.md` | 14 |
| `x-bookmarks` | Daily 19:00 | [`bin/scrape-x-bookmarks.sh`](../../../pi-workspace/bin/scrape-x-bookmarks.sh) | gstack `/browse` against x.com/i/bookmarks (cookie auth) | `raw/x-bookmarks-YYYY-MM-DD.md` | 5 (expected ~30) |
| `claude-sessions` | Sun 07:30 | [`bin/ingest-claude-sessions.sh`](../../../pi-workspace/bin/ingest-claude-sessions.sh) | `~/.claude/projects/**/*.jsonl` (Claude Code session JSONL files) | `raw/sessions/claude-code-YYYY-MM-DD-{slug}.md` (per-session) + `raw/weekly-sessions-YYYY-MM-DD.md` (weekly rollup) | 5 weekly rollups · 234 individual session files (81 in last 7d) |
| Stop hook (`post-session-capture`) | Per-session (Claude Code Stop hook) | [`bin/post-session-capture.sh`](../../../pi-workspace/bin/post-session-capture.sh) | Live Claude Code JSONL on session end | Stamps `wiki/hot/hot.md` "Recent Queries" only | hot.md is the freshest artifact in the Brain (updated minutes ago) |
| `content-calendar` | Mon 09:00 | [`bin/content-calendar.sh`](../../../pi-workspace/bin/content-calendar.sh) | wiki/moil/{positioning,icp,gtm,metrics}.md + AGENTS.md | `quartz/content/raw/content-calendar/calendar-YYYY-WNN.md` | 1 (calendar-2026-W18 — last ran Apr 27, **next due 2026-05-05**) |
| GitHub activity (called by morning-briefing + plan-radar + pattern-surfacer) | On demand | [`bin/github-activity.sh`](../../../pi-workspace/bin/github-activity.sh) | `gh` CLI across configured repos | `outputs/github-activity-YYYY-MM-DD.md` | 14 |
| OneDrive transcripts (legacy) | Manual | [`bin/download-onedrive-transcripts.sh`](../../../pi-workspace/bin/download-onedrive-transcripts.sh) | OneDrive transcript fetch | `raw/onedrive-transcripts/*.txt` | 0 — directory frozen since Apr 14 |

Not present anywhere: Slack, voice notes, browser history, podcast/YouTube transcripts, newsletter subscriptions, calendar attendee lists beyond the meeting subject (raw briefings have attendees, but they aren't projected to wiki/people).

### Synthesis jobs (markdown out)

| Job | Schedule (from plist) | Script | Inputs | Output |
|---|---|---|---|---|
| `daily-correlator` | Daily 06:00 | [`bin/daily-correlator.py`](../../../pi-workspace/bin/daily-correlator.py) | Yesterday's raw/*.md (per-source-type capped) + MEMORY + hot.md + pipeline.md | `quartz/content/raw/signal-briefs/signal-brief-YYYY-MM-DD.md` |
| `editorial` (bookmarks) | Daily 19:30 | [`bin/bookmarks-editorial.sh`](../../../pi-workspace/bin/bookmarks-editorial.sh) | Yesterday's `x-bookmarks-*.md` (≥5 items required) | `outputs/editorial/YYYY-MM-DD.md` + email |
| `plan-radar` | Daily 12:00 | [`bin/daily-plan-radar.sh`](../../../pi-workspace/bin/daily-plan-radar.sh) | Last 14d of `outputs/github-activity-*`, last 7d briefings, last 3 editorials, latest operating brief, MEMORY + pipeline | `outputs/plan-radar/YYYY-MM-DD.md` |
| `pattern-surfacer` | Sun 07:00 | [`bin/pattern-surfacer.sh`](../../../pi-workspace/bin/pattern-surfacer.sh) | Last 7d x-bookmarks + email-digest + teams-* heads + GitHub activity (with diffs!) + MEMORY + pipeline | `outputs/patterns/YYYY-MM-DD-patterns.md` |
| `operating-brief` | Sun 20:00 | [`bin/weekly-operating-brief.sh`](../../../pi-workspace/bin/weekly-operating-brief.sh) | Last 7d bookmarks + email/teams heads + Moil state (active-projects, gtm, pipeline, customers, positioning, AGENTS.md) | `outputs/operating-brief/YYYY-WNN.md` + email |
| `weekly-compile` | Fri 14:00 | [`bin/weekly-compile.sh`](../../../pi-workspace/bin/weekly-compile.sh) | All raw/*.md not in log.md | Wiki page diffs + `quartz/content/raw/compile-YYYY-MM-DD.md` |
| `entity-graph` | Daily 00:15 (per plist) | [`bin/entity-graph-builder.py`](../../../pi-workspace/bin/entity-graph-builder.py) | Yesterday's raw/*.md (skips meta sources) + wiki/people/*.md | Updates each `wiki/people/X.md` `last_contact:` + bounded "Recent Activity (auto)" + `wiki/hot/relationship-radar.md` + `wiki/hot/open-commitments.md` + `wiki/hot/entity-queue.md` |

### Health/maintenance jobs

| Job | Schedule (from plist) | Script | What it does |
|---|---|---|---|
| `chroma-index` | Daily 09:15 | [`bin/wiki-to-chromadb.py --ingest --include-raw`](../../../pi-workspace/bin/wiki-to-chromadb.py) | Reindex wiki + raw into ChromaDB at `pi-workspace/.chroma-data/` |
| `kb-health` | Sun 08:00 | [`scripts/kb-health.sh`](../../../scripts/kb-health.sh) | MD5 dupes, broken wikilinks, frontmatter, MEMORY ≤ 200 lines, sync status. Writes `outputs/health/kb-health-latest.md` |
| `heartbeat` | Daily 09:20 | [`bin/brain-heartbeat.sh`](../../../pi-workspace/bin/brain-heartbeat.sh) | Stat-only freshness check on 5 hardcoded artifacts; writes `outputs/health/heartbeat-latest.md` |
| `ui` | KeepAlive | npm start (brain-ui at port 3047) | Static dashboard frontend |
| `sync_wiki` | Called by every commit-producing script | `scripts/sync_wiki.sh` | Mirrors `wiki/` → `quartz/content/wiki/` before push |

---

## B) Are we keeping it fresh? (per-source freshness audit)

Reading log mtimes from `pi-workspace/.<job>-log` and destination directory mtimes. "Drift" = observed gap > 2× expected interval.

### Capture sources

| Source | Expected | Last run | Drift | Notes |
|---|---|---|---|---|
| morning-briefing | weekday 08:45 | log: 2026-05-01 08:57 — **stale 2 days** | yes (it's Saturday, but **today's briefing file is missing per heartbeat**) | last fresh `outputs/briefings/briefing-*` is **Apr 29**; canonical `quartz/content/raw/briefings/` ends Apr 29. The non-weekday days (and the deploy outage) have left the briefing pipeline drifting |
| teams-daily | daily 18:00 | log: 2026-05-02 18:25 | none | digest file count: 8 in 30d — gaps on weekends and several weekdays. Either no Teams traffic those days or pull is dropping |
| email-digest | weekday 18:30 | log: 2026-05-01 18:31 | yes — last digest is `email-digest-2026-05-01.md`. Friday 5/2's digest is missing | script has an idempotent skip if the day's file already exists; check whether 5/2 file pre-existed at 0 bytes or whether the job didn't fire |
| x-bookmarks | daily 19:00 | log: 2026-05-02 21:35 | none, but **3 silent zero-item runs on 2026-05-02 before a manual 21:23 retry produced 214 items** | the cookie sanity check passes but the scroll buffer was empty — `x-bookmarks-2026-04-25.md` is also a 234-byte zero-item file that was committed. Silent data drop. Capture is brittle to X UI changes |
| claude-sessions (weekly rollup) | Sun 07:30 | log: 2026-05-03 09:23 | none — most recent rollup is `weekly-sessions-2026-05-03.md` | runs fine, but see synthesis section below — the rollup is mechanical and not actually a synthesis |
| post-session hook | per-session | hot.md updated 2026-05-03 09:18 | none | this is the freshest signal in the entire Brain |
| content-calendar | Mon 09:00 | log: 2026-04-27 09:03 | yes — last calendar is `calendar-2026-W18.md` (Apr 28). Should have produced W19 on Apr 28 but the next file would be W19/W20 due Mon 5/5 | only 1 calendar in 30d. Either the Mon-only schedule misses week boundaries or the script bailed silently |
| github-activity (manual cron via callers) | varies | most recent `outputs/github-activity-2026-05-01.md` | possible | 14 dated files in 30d (rough daily); no separate plist — derived |
| onedrive-transcripts (manual) | manual | dir frozen Apr 14 | no auto-pull defined; ignore |

### Synthesis sources

| Output | Expected | Last produced | Drift | Notes |
|---|---|---|---|---|
| signal-brief | daily 06:00 | `signal-brief-2026-05-02.md` (06:00) | none | runs reliably; `correlator` log shows clean runs |
| daily editorial | daily 19:30 | `outputs/editorial/2026-05-02.md` | none | even falls back to last-known bookmark file when today's is empty |
| plan-radar | daily 12:00 | `outputs/plan-radar/2026-05-02.md` | none | 9 in 30d — gaps on weekends |
| pattern-surfacer | weekly Sun 07:00 | `outputs/patterns/2026-05-02-patterns.md` (Fri 21:02 — manual) | yes — **only 1 weekly file in 30d.** plist fires Sundays only; the Apr 22 entity-graph thrash week + the 10-day deploy outage means weeks Apr 12 / Apr 19 / Apr 26 had no patterns surface |
| weekly-operating-brief | weekly Sun 20:00 | `outputs/operating-brief/2026-W17.md` (Apr 26) | **yes — 7 days stale, missed Sun May 4 is upcoming and the Apr 26 file is the only one in 30d** | the Apr 26 W17 file is the *only* operating brief that exists. The Sun May 4 run hasn't happened yet — but the prior Sun May 3-eve and the missing Apr 19 / Apr 12 weeks suggest this never ran more than once |
| weekly-compile | Fri 14:00 | log: 2026-05-01 14:07 | none | runs but the compile reports are not surfaced anywhere readers will see |
| entity-graph | daily 00:15 | **plist exists but `pi-workspace/.entity-graph-log` does not exist; `relationship-radar.md` last_updated = 2026-04-22; `open-commitments.md` last_updated = 2026-04-21; `entity-queue.md` last_updated = 2026-04-21** | **CRITICAL — 11–12 days stale** | `launchctl list \| grep moil.brain` does NOT show `com.moil.brain.entity-graph` even though the plist file is present in `pi-workspace/launchd/`. The job is not loaded into launchd. The relationship radar is dead and Andres's morning briefing's "going cold" pulls from it |

### Health/maintenance

| Job | Expected | Last run | OK? |
|---|---|---|---|
| chroma-index | daily 09:15 | log: 2026-05-03 09:16 | yes |
| kb-health | Sun 08:00 | report: 2026-05-03 08:00 | yes (1 warning: `index.md` claims 388 raw files, actual 464) |
| heartbeat | daily 09:20 | report: 2026-05-03 09:20 | yes — **and it's correctly flagging today's missing briefing**, but nothing routes that signal anywhere actionable |

### Missing inputs we should be capturing but aren't

- **Slack** — Andres uses Slack with at least one customer org (per `wiki/orgs/`); no pull
- **Voice notes / Whisper-transcribed phone audio** — `transcribe-meetings.sh` and `transcribe_local.py` exist but are not on a launchd schedule and `outputs/transcribed/` doesn't exist as a routed destination
- **Read-later articles (Pocket / Readwise / Instapaper)** — none. Bookmarks come only from X
- **Newsletter subscriptions / Substack** — there's no "inbox auto-categorize newsletters → digest" step; newsletter emails get folded into `email-digest-*.md` heads but never extracted
- **Podcast / YouTube transcripts of items Andres watches** — no capture
- **Browser history / dwell time** — no capture (would let pattern-surfacer say "you read this article 4 times this week")
- **Calendar attendee identities** — `compute-last-contact.py` reads attendee names for the going-cold check but the morning briefing doesn't auto-create wiki/people/ pages for new attendees
- **GitHub PR review *comments*** — `github-activity.sh` captures commits + PR titles but per the script there's no review-comment fetch (would let pattern-surfacer see what Andres or his collaborators are debating in code)
- **Apollo CRM enrichment changes** — Apollo MCP is available but no automation routes its output into wiki/orgs or wiki/people
- **WhatsApp** — `brain-ingest.sh` has a WhatsApp .txt parser stanza but nothing schedules WhatsApp exports; depends on Andres manually dropping `WhatsApp Chat - *.txt` files in `raw/`

---

## C) Connecting the hints — synthesis quality

This is where the Brain is weakest. The capture layer works; the writing-back-into-the-graph layer mostly doesn't.

### Does anything cross-link across sources?

Two scripts genuinely cross-source:

1. **`daily-correlator.py`** — the strongest piece in the system. Groups yesterday's files by source_type, applies per-type caps so claude-sessions don't drown teams transcripts, builds one prompt with grounding from `MEMORY.md` + `wiki/hot/hot.md` + `pipeline.md`, and asks for exactly three things: cross-source connection, active-person flag, silence anomaly. The 2026-05-02 brief I read is real signal: it links a John Costilla email reply to a Nate Herk masterclass bookmark and pulls out an Inna silence threshold against `MEMORY.md`. This is the sharp tool.
2. **`weekly-operating-brief.sh`** — also genuinely cross-source: bookmarks corpus + email/teams heads + Moil state docs. Decision-doc voice with named projects and named people. **But it's effectively dead** — last ran Apr 26.

Two scripts pretend to cross-source but don't:

3. **`pattern-surfacer.sh`** — does pull bookmarks + emails + teams + github diffs together, but it ran only once in the 30-day window. When it does run the "bookmark × code crossover" section is a real cross-source insight. Underused.
4. **`weekly-operating-brief.sh`** — see above.

Everything else is single-source: the editorial reads bookmarks only, plan-radar reads briefings + editorials + github (which is closer but lossy), the morning briefing reads its own assembled context but treats each source as a slot, not a graph.

### Auto-categorization / tagging of new content?

**`entity-graph-builder.py`** is the only thing that auto-mutates wiki pages. When it runs (which it isn't right now) it:
- Updates `frontmatter:last_contact` on every `wiki/people/X.md` mentioned yesterday
- Appends a bounded `## Recent Activity (auto)` section to those pages (1-line entries, capped at 12, pruned at 30 days)
- Writes `wiki/hot/relationship-radar.md` listing contacts >14 days cold
- Writes `wiki/hot/open-commitments.md` (bidirectional commitments owed/owing)
- Writes `wiki/hot/entity-queue.md` (frequently-mentioned unknowns to manually triage)

This is the right design. The execution is dead. **`launchctl list | grep moil.brain` does not show `com.moil.brain.entity-graph` even though the plist file is on disk.** Andres needs to manually `launchctl load` it (or whatever the agreed manual flow is per `~/CLAUDE.md` "No launchctl" rule — this is the cost of that rule).

No script tags raw content with project / theme labels. Concepts pages exist but aren't reinforced from raw activity — `wiki/concepts/*.md` were last touched May 1 in a batch, not incrementally.

### Does ChromaDB get queried by automation?

**No.** I grepped for `wiki-to-chromadb` references across `pi-workspace/bin/` and `knowledge-base/scripts/`:

- `weekly-compile.sh` — calls `--ingest` (write only)
- `brain-ingest.sh` — calls `--ingest` (write only)
- `brain-query.sh` — calls `--query` (manual human use)
- `daily-correlator.py` — references the script in a comment to mirror source-type inference, never invokes it

3,156 chunks indexed daily; **zero automated queries.** The correlator could ask "show me everything we've said about Inna in the last 90 days" and use that as grounding instead of just the last 7 days of files. The pattern-surfacer could ask "are there bookmarks from the last 90 days that touch the same theme as this week's commits?" Right now it can only see this week. Chroma is a dashboard for Andres to type into manually.

### Concepts layer reinforcement

Concepts pages are **mostly stale** between weekly compiles. `wiki/concepts/*.md` 9 most-recent entries all have mtime 2026-05-01 08:17 — touched by the weekly compile en masse, then nothing for 2 days. There is no "this week's pattern surface mentioned [smb-ai-audits] 4 times → bump that page's freshness or add a one-line stamp" loop. The pattern-surfacer outputs land in `outputs/patterns/` but never write back into the concept pages they reference.

### Sessions: does anything pull "what did Andres learn / decide / leave unresolved" out of session transcripts?

**No.** Looked specifically at this. `weekly-sessions-2026-05-03.md` (the 2026-05-03 rollup, 35 KB, 78 sessions) is **mechanical**:
- Frontmatter: `session_count`, totals (`192 user messages · 785 assistant responses · 2461 tool calls`)
- A "By project" table (Brain/Automations: 42, Brain/KB: 14, etc.)
- Per session: a one-line `**Ask:**` (truncated at 120 chars) + `**Files:** N new · M edited` + a wikilink to the per-session summary

There is **no** synthesis: no extraction of decisions, learnings, recurring user asks, themes, "what did Andres pivot away from this week", or "what tools are getting heavy use vs. dropped." Worse, because the same Brain automation prompts (the cross-source intel analyst, the editor, the plan radar) all land as automated sessions, the rollup is dominated by 7+ identical "You are the Moil Brain's daily cross-source intelligence analyst…" entries — those are the correlator runs themselves, polluting the human-decision signal.

The per-session files (`raw/sessions/claude-code-*.md`) are similarly thin. They contain prompt + tool counts + file lists, not extracted learnings. They are inputs that nothing reads back as synthesis.

### Bottom line: synthesis quality = WEAK to MIXED

- **Strong:** `daily-correlator.py` (+ the `entity-graph-builder.py` design when it ran)
- **Mixed:** `bookmarks-editorial.sh` (good single-source synthesis but only one source), `pattern-surfacer.sh` (good design, runs once a month in practice)
- **Weak:** `weekly-sessions` rollup (mechanical, not synthesis), all chromadb non-use, concept-page reinforcement, weekly-operating-brief (dead)

The Brain is currently **input-rich and reflection-poor**. It captures more than it reads back. The piece that would change that — entity-graph + a session-learnings extractor — either isn't loaded or isn't written.

---

## D) Recommendations

Prioritized for impact-per-hour. Each entry: problem · script to touch · effort · value.

### P0 — Silently dead synthesis (fix this week)

1. **Re-load `com.moil.brain.entity-graph` into launchd.** Plist is on disk at `pi-workspace/launchd/com.moil.brain.entity-graph.plist`, but `launchctl list | grep moil.brain` shows it is not loaded. Result: `wiki/hot/relationship-radar.md` is frozen at Apr 22 and morning-briefing's going-cold list is built from stale data. **Effort: low (1 launchctl load command per the existing manual ritual).** **Value: very high — restores the entire relationship layer.**

2. **Diagnose why `weekly-operating-brief.sh` only ran once in 30 days.** plist schedule says Sun 20:00, last run Apr 26. Either launchctl shows it loaded but it's silently bailing (no bookmark files for 7 prior days?) or it's not loaded. Check `.operating-brief-log` history. **Touch:** `weekly-operating-brief.sh` (line 54: bails if `BOOKMARK_FILES -eq 0` — if 4 of last 7 days had silent zero-item bookmark files due to the X scrape issue, this would skip even with files present). **Effort: low.** **Value: high — this is the Sunday-night decision doc that walks Andres into Monday.**

3. **Add a "silent zero-item" guard to `scrape-x-bookmarks.sh`.** The 2026-05-02 log shows three consecutive runs that succeeded and saved zero items before a manual retry produced 214. The Apr 25 file is a committed 234-byte zero-item placeholder. Currently the script only checks cookie presence; it should also fail-loud (or alert via heartbeat) if the scrape returns < 5 items when last-known-good was > 50. **Touch:** `scrape-x-bookmarks.sh`. **Effort: low.** **Value: medium — prevents silent capture loss and the cascade into operating-brief skipping.**

### P1 — Synthesis upgrades (next 1–2 weeks)

4. **Replace `weekly-sessions-*.md` mechanical rollup with a real session-learnings extractor.** Right now the rollup is `count + truncated first prompt`. Add a Claude pass that reads the per-session JSONL and extracts: (a) decisions Andres made, (b) tools/skills he used heavily vs. abandoned, (c) recurring "what's broken" themes, (d) any unresolved questions he asked twice. Filter out the automation-sessions (the correlator, the editor, the plan radar — those are not learnings, they're cron output). **Touch:** `bin/ingest-claude-sessions.py` (the rollup writer). **Effort: medium.** **Value: high — turns 78 sessions/week into a real "what did Andres learn / leave unfinished" doc.**

5. **Have `daily-correlator.py` and `pattern-surfacer.sh` query ChromaDB for historical context.** Today both only see the last 1–7 days of files. Add a step that runs `wiki-to-chromadb.py --query "[active person from yesterday]" --top 10` to pull in 90-day historical mentions, and inject those as "historical context" in the prompt. The correlator's "silence anomaly" section would get dramatically sharper if it could compare against actual historical cadence rather than what's in `wiki/hot/hot.md`. **Touch:** `daily-correlator.py` (build_context function), `pattern-surfacer.sh` (between MEMORY assembly and the Claude call). **Effort: medium.** **Value: high — finally makes the 3,156-chunk index do work.**

6. **Make `pattern-surfacer.sh` cover a rolling 28 days and run more than once a week.** Current design surfaces *only* the last 7 days, on Sun 07:00 only. Result: anti-pattern detection misses anything spanning a 2-3 week arc. Either move to bi-weekly with a 28-day window, or run weekly with both 7-day and 28-day passes. **Touch:** `pattern-surfacer.sh` (`WEEK_AGO=$(date -v -7d ...)` → add a `MONTH_AGO`), and the plist Weekday list. **Effort: low.** **Value: medium-high — the pattern-surfacer is the engine you'd want catching the "Andres just rebuilt the same outbound campaign that didn't convert in March" pattern.**

7. **Fold `compute-last-contact.py`'s output into a wiki page (currently stdout-only).** Right now it computes 7 signals per key contact and emits JSON to stdout for `morning-briefing.sh` to consume — and discards. Persist that as `outputs/relationship-signals-YYYY-MM-DD.md` (or update `wiki/hot/relationship-signals.md`) so historical cadence is visible. Also lets `entity-graph-builder.py` cross-check its own staleness logic against compute-last-contact. **Touch:** `compute-last-contact.py` (add `--write` mode) + `morning-briefing.sh` (write before consuming). **Effort: low.** **Value: medium.**

### P2 — Capture gaps (next 2–4 weeks)

8. **Capture Slack DMs and channels Andres uses for customer comms** — pi-workspace currently has no Slack pull. If Slack is on the daily comms surface, a `slack-pull.sh` daily 18:15 with a dedicated `raw/slack-YYYY-MM-DD.md` would be straightforward (Slack API export). **Effort: medium.** **Value: high if customers are on Slack — high-leverage missing channel.**

9. **Schedule `transcribe_local.py` so voice notes auto-flow into raw/.** The script exists; nothing routes phone-recorded voice memos through it. Add a Drop folder convention (`raw/voice-inbox/*.m4a`) + a launchd watcher or a 17:00 sweep. **Effort: medium.** **Value: medium — voice notes are dense signal that's currently lost.**

10. **Auto-create `wiki/people/` stubs from morning-briefing calendar attendees.** When the briefing sees a meeting with attendee Y who has no wiki page, create a stub pre-populated from any `email-digest` or `teams-` history. Today this is manual. **Touch:** `morning-briefing.sh` step 9 or a new post-briefing script. **Effort: medium.** **Value: medium — feeds the entity-graph the entities it needs.**

11. **Pull GitHub PR review comments, not just commit titles.** `github-activity.sh` (pattern-surfacer's primary code signal) skips PR comment threads. Adding `gh api repos/X/Y/pulls/Z/comments` would let pattern-surfacer detect debate / friction patterns in code. **Touch:** `github-activity.sh`. **Effort: low.** **Value: medium.**

### P3 — Observability (do alongside P0)

12. **Heartbeat should escalate, not just write a file.** `outputs/health/heartbeat-latest.md` correctly identified the missing 2026-05-03 briefing this morning. Nobody saw it. Either email it (only when `attention needed`), or wire it into `wiki/hot/hot.md` so it appears in the next morning briefing. **Touch:** `brain-heartbeat.sh` (add a conditional m365 send when any row is `missing` or `stale`). **Effort: low.** **Value: high — this is exactly the gap that let the 10-day GitHub Pages deploy outage go unnoticed.**

13. **Add a "no run today" alert to every plist-driven script.** When the launchd job last-run-time is older than 2× expected interval, send a one-line email. Cheapest version: have `brain-heartbeat.sh` stat all `pi-workspace/.<job>-log` mtimes and report drift. **Effort: low.** **Value: high — would have caught the entity-graph never-loaded failure on day 2 instead of day 12.**

14. **Fix `index.md` raw stat drift.** `kb-health.py` reports `raw: claims 388, actual 464`. The index hasn't been updated as raw files accumulate. **Touch:** `weekly-compile.sh` (Part 5 already supposed to update index.md). **Effort: low.** **Value: low (cosmetic but kb-health keeps flagging it).**

---

*Single biggest finding:* the entity-graph-builder is the most architecturally important automation in the Brain — it's the one thing that mutates wiki/people/ pages from raw data, and it's been silently dead for 11 days. Fix that first.

*Second biggest:* nothing reads ChromaDB. The episodic memory layer is write-only.

*Third biggest:* the weekly-sessions rollup is a count, not a synthesis. Andres has 78 sessions a week passing through the Brain and zero of that is being read back as "what changed in your thinking this week."

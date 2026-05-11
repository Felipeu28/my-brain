---
type: audit
date: 2026-05-07
companion: raw/audits/2026-05-03-ingestion-and-synthesis-audit.md
ingested: true
ingested_at: 2026-05-11
tags:
  - graph/leaf
---

# Brain Ingestion Deep Audit — 2026-05-07

> **TL;DR (Section F promoted here).** Audited 27 plists + ~35 scripts. **6 jobs ✅ working, 8 ⚠️ degraded, 13 🔴 broken.** The single biggest hidden risk: **12 of 27 plists are physically present on disk but never loaded into launchctl** — every Week-3/4 job shipped on 2026-05-03 (sentinel, entity-graph, daily-correlator, project-activity, pattern-surfacer, last-contact, session-learnings, concept-of-the-day, related-suggester, brain-lint, weekly-pitch-mistake, last-contact-coverage) is in this set. The sentinel that was supposed to *catch* exactly this failure class is itself one of the unloaded jobs. The Brain is **NOT safe to leave alone for a week** — needs a fix-up pass before Friday or the cascade gets worse. Specifically, the X-cookie expiry on 2026-05-03 has now killed the weekly-operating-brief twice (its `BOOKMARK_FILES -eq 0` precondition still bails despite the "relax" item in the 2026-05-03 plan), and the chroma-index has been exit-2'ing every day for ≥4 days because LM Studio isn't running on localhost:1234.

Companion to `raw/audits/2026-05-03-ingestion-and-synthesis-audit.md`. This is the *second-pass* audit: same surface, looking for what the first pass missed and what has degraded since. Where the prior audit found 1 missing plist (entity-graph) and called it out as the biggest finding, this audit finds the *pattern* — almost every plist shipped during Week 1 of the implementation plan was never loaded after its commit landed.

Read-only audit. No scripts or plists modified.

---

## Section A — Plist load state cross-reference

| Filename | Label | Loaded? | Last exit | Verdict |
|---|---|---|---|---|
| com.moil.brain.brain-lint.plist | com.moil.brain.brain-lint | **no** | n/a | 🔴 not loaded — `launchctl bootstrap gui/$(id -u) ~/My\ Brain/pi-workspace/launchd/com.moil.brain.brain-lint.plist` |
| com.moil.brain.chroma-index.plist | com.moil.brain.chroma-index | yes | **2** | ⚠️ exit-2 every run — preflight fails because LM Studio is not running at `http://localhost:1234/v1`. Index has not been updated in ≥4 days. `.chroma-log` shows 4 consecutive identical `Preflight failed: LM Studio unreachable` failures. Existing index is preserved (frozen). |
| com.moil.brain.claude-sessions.plist | com.moil.brain.claude-sessions | yes | 0 | ✅ |
| com.moil.brain.concept-of-the-day.plist | com.moil.brain.concept-of-the-day | **no** | n/a | 🔴 not loaded — `launchctl bootstrap gui/$(id -u) ~/My\ Brain/pi-workspace/launchd/com.moil.brain.concept-of-the-day.plist` |
| com.moil.brain.content-calendar.plist | com.moil.brain.content-calendar | yes | 0 | ✅ |
| com.moil.brain.daily-correlator.plist | com.moil.brain.daily-correlator | **no** | n/a | 🔴 not loaded — silence-anomaly briefs stopped 2026-05-04. `launchctl bootstrap gui/$(id -u) ~/My\ Brain/pi-workspace/launchd/com.moil.brain.daily-correlator.plist` |
| com.moil.brain.editorial.plist | com.moil.brain.editorial | yes | 0 | ✅ |
| com.moil.brain.email-digest.plist | com.moil.brain.email-digest | yes | (never exited) | ⚠️ loaded but launchctl says it has never exited in this load session — verify it's actually firing. `.email-log` shows last write 2026-05-07 18:32, so it is running, just `launchctl print` hasn't captured an exit yet (possibly reloaded recently). |
| com.moil.brain.entity-graph.plist | com.moil.brain.entity-graph | **no** | n/a | 🔴 **STILL NOT LOADED despite Week-1 item 1 marked "✅ live" in the 2026-05-03 plan execution log.** Either it was loaded and then bounced out by a reboot/login cycle, or the plan log was optimistic. `wiki/hot/relationship-radar.md` mtime 2026-05-05 confirms a manual run that day, not a launchd-driven run. `launchctl bootstrap gui/$(id -u) ~/My\ Brain/pi-workspace/launchd/com.moil.brain.entity-graph.plist` |
| com.moil.brain.heartbeat.plist | com.moil.brain.heartbeat | yes | 0 | ✅ |
| com.moil.brain.imessage-pull.plist | com.moil.brain.imessage-pull | yes | 0 | ⚠️ loaded + running, but the underlying script fails — `.imessage-pull-log` shows `ERROR: cannot open chat.db ... Full Disk Access` for both 2026-05-10 and 2026-05-11 runs. Zero capture files in `raw/imessages-*.md` since the plist was added 2026-05-06. The python binary at `/Users/jarvisurrego/mlx-env/bin/python` is missing Full Disk Access permission. The script exits 0 anyway (the python error is swallowed by `tee`). |
| com.moil.brain.kb-health.plist | com.moil.brain.kb-health | yes | 0 | ✅ |
| com.moil.brain.last-contact-coverage.plist | com.moil.brain.last-contact-coverage | **no** | n/a | 🔴 not loaded |
| com.moil.brain.last-contact.plist | com.moil.brain.last-contact | **no** | n/a | 🔴 not loaded — `.last-contact-log` last write 2026-05-05 00:05 (a single run, then silence). |
| com.moil.brain.morning-briefing.plist | com.moil.brain.morning-briefing | yes | 0 | ⚠️ exit 0 but stdout-recovery is failing — `.briefing-log` 2026-05-11 08:48 reads `WARNING: Claude did not write briefing to disk; recovering from stdout... ERROR: Claude stdout had no '# Morning Briefing — ' marker; cannot recover`. Today's briefing file (`briefing-2026-05-11.md`) does not exist in `quartz/content/raw/briefings/`. Heartbeat correctly flags `missing`. |
| com.moil.brain.operating-brief.plist | com.moil.brain.operating-brief | yes | 0 | ⚠️ exit 0 but silently bailing — `.operating-brief-log` 2026-05-10 18:00 says `No bookmark files in last 7 days — skipping brief`. This is the audit §B item 2 cascade: X cookies expired 2026-05-03 → no bookmark files captured → operating-brief precondition fails → no decision doc for the Monday. The "relax precondition" Week-1 item 3 was **not implemented** — `weekly-operating-brief.sh` line 56 still does the hard `BOOKMARK_FILES -eq 0` bail. |
| com.moil.brain.pattern-surfacer.plist | com.moil.brain.pattern-surfacer | **no** | n/a | 🔴 not loaded. Only 2 pattern files in `outputs/patterns/`: 2026-05-02 (manual), 2026-05-05 (manual). Wed/Sun cadence in the 2026-05-03 plan never started firing. |
| com.moil.brain.plan-radar.plist | com.moil.brain.plan-radar | yes | 0 | ✅ |
| com.moil.brain.project-activity.plist | com.moil.brain.project-activity | **no** | n/a | 🔴 not loaded — all 6 `wiki/projects/*.md` page mtimes frozen at 2026-05-05 08:51. The 2026-05-03 plan's marquee Week-2 feature is dead. |
| com.moil.brain.related-suggester.plist | com.moil.brain.related-suggester | **no** | n/a | 🔴 not loaded — only 1 queue file produced (`queue-2026-05-03.md`). |
| com.moil.brain.sentinel.plist | com.moil.brain.sentinel | **no** | n/a | 🔴 **CRITICAL — the meta-tool that would have detected every other not-loaded plist on this list is itself not loaded.** Last write to `.sentinel-log` was 2026-05-05 08:30 (a single run). No `outputs/health/sentinel-latest.md` is being regenerated. |
| com.moil.brain.session-learnings.plist | com.moil.brain.session-learnings | **no** | n/a | 🔴 not loaded — `outputs/learnings/` has exactly one file (`learnings-2026-05-03.md` from the initial seed). |
| com.moil.brain.teams-daily.plist | com.moil.brain.teams-daily | yes | 0 | ✅ |
| com.moil.brain.ui.plist | com.moil.brain.ui | yes | 0 (KeepAlive, pid 2639) | ✅ |
| com.moil.brain.weekly-compile.plist | com.moil.brain.weekly-compile | yes | (never exited) | ⚠️ loaded; `.compile-log` last write 2026-05-01 14:07 — six days ago, but next firing isn't until Fri 2026-05-08 14:00, so this is on schedule. Re-verify on Saturday. |
| com.moil.brain.weekly-pitch-mistake.plist | com.moil.brain.weekly-pitch-mistake | **no** | n/a | 🔴 not loaded |
| com.moil.brain.x-bookmarks.plist | com.moil.brain.x-bookmarks | yes | **1** | ⚠️ exit-1 every day — `.bookmarks-log` shows `ERROR: no x.com cookies in browse session. Run /setup-browser-cookies x.com to import.` on every scheduled run from 2026-05-03 onward. **Cookies have been expired for 5+ days, no successful capture since 2026-05-02.** This is the failure the sentinel was meant to email-page Andres about; the sentinel isn't loaded. |

**Ghost in the loaded list:** `com.moil.brain.weekly-pulse` appears in `launchctl list` but **no plist file exists on disk in `pi-workspace/launchd/`** — it's a stale registration from a removed plist. `.pulse-log` last write 2026-05-01 15:00. Harmless cosmetic, but worth a `launchctl bootout`.

**Summary:** 27 plists on disk → 16 in `launchctl list | grep com.moil.brain` → 12 not loaded → 1 ghost → real load rate **15/27 = 56%**.

---

## Section B — Capture jobs — actually writing data?

Destinations checked at `/Users/jarvisurrego/My Brain/knowledge-base/raw/` and subdirs.

| Job | Destination | Expected | Last successful write | Files last 7d | Avg bytes | Verdict |
|---|---|---|---|---|---|---|
| x-bookmarks | `raw/x-bookmarks-*.md` | daily 19:00 | **2026-05-02** (`x-bookmarks-2026-05-02.md`, 22 KB, 214 items) | 0 | n/a | 🔴 **Dead 5+ days.** Cookies expired. The May-2 file is the only real capture since Apr 26. The Apr 25 file is the 273-byte zero-item placeholder Felipe noted yesterday. Zero-item guard in `scrape-x-bookmarks.sh` is now working (quarantines + exits 2) but cookie-refresh is still manual, and the sentinel that should email-page is not loaded. |
| email-digest | `raw/email-digest-*.md` | weekday 18:30 | 2026-05-07 (8.9 KB) | 4 files (May 4, 5, 6, 7) | ~8.8 KB | ✅ working. Note May 2/3 missing (weekend, correct skip). |
| teams-daily | `raw/teams-*.md` + `raw/teams-transcript-*.md` | daily 18:00 | 2026-05-07 (`teams-transcript-megan-andres-2026-05-07.md`, 7 KB) + 2026-05-06 (`teams-transcript-meeting-to-go-over-ongoing-projects-2026-05-06.md`, 62 KB) | 2 transcripts in 7d | 35 KB | ✅ working. `.teams-log` actively writing. |
| claude-sessions per-file | `raw/sessions/claude-code-*.md` | per-session hook + Sunday rollup | 2026-05-10 (multiple, 1.2–2.9 KB each) | 14+ session files | ~1.7 KB | ✅ working. |
| claude-sessions weekly rollup | `raw/weekly-sessions-*.md` | Sun 07:30 | 2026-05-03 (35 KB) | 0 in 7d (next rollup Sun 2026-05-10) | n/a | ⚠️ on schedule but the rollup is still the mechanical count, not the session-learnings extractor (Week-3 item 8b not shipped). |
| morning-briefing | `quartz/content/raw/briefings/briefing-*.md` | weekday 08:45 | 2026-05-08 (6.9 KB) | 3 (May 5, 7, 8 — May 4, 6 skipped weekend logic, May 11 **failed today**) | ~9.5 KB | ⚠️ **today's 2026-05-11 run failed** — Claude didn't call Write, stdout recovery couldn't find the `# Morning Briefing — ` marker, briefing file does not exist. Heartbeat at 09:20 flags `missing`. The recovery fallback has a real ceiling: when Claude's stdout doesn't conform to the expected shape, the briefing is lost. |
| content-calendar | `quartz/content/raw/content-calendar/calendar-*.md` | Mon 09:00 | 2026-05-11 (`calendar-2026-W20.md`) | 1 | n/a | ✅ working (W17–W20 all present). |
| github-activity | `outputs/github-activity-*.md` | called by callers | 2026-05-11 08:45 (2.6 KB) | 5 (May 4, 5, 6, 7, 8) | 3.6 KB | ✅ working. |
| imessage-pull | `raw/imessages-*.md` (public) + `raw/private/imessages-*.md` (gitignored) | daily 06:30 | **never** | 0 | n/a | 🔴 **plist loaded since 2026-05-06, zero capture files produced.** Underlying python script can't open `chat.db` — `/Users/jarvisurrego/mlx-env/bin/python` needs Full Disk Access added in System Settings → Privacy & Security. The error is swallowed by `tee`, so the wrapper script exits 0. Silent-success at the shell layer; the python layer prints the right error. The `raw/private/` directory does not exist (would be gitignored). The lone `imessages-people-2026-04-09.md` file in `raw/` is from an unrelated manual capture before the plist existed. |
| onedrive-transcripts | `raw/onedrive-transcripts/` | manual | n/a | 0 | n/a | n/a — no auto-pull. Audit §B item 9 still applies, no change. |
| Apollo CRM enrichment | n/a | none | n/a | 0 | n/a | n/a — no automation routes Apollo MCP output to `wiki/orgs/` or `wiki/people/`. Audit §B last item still applies, no change. |
| WhatsApp | `raw/WhatsApp Chat - *.txt` | manual | n/a | 0 | n/a | n/a — no scheduled job. |

**Silent-success patterns confirmed:**
- `scrape-x-bookmarks.sh` now exits non-zero on zero-item (fix landed 2026-05-05) **but** the cookie-missing path was already exiting non-zero; the failure is invisible because the sentinel isn't loaded.
- `imessage-pull.sh` is the new silent-success bug: `"$PY" imessage-pull.py "$@" 2>&1 | tee -a "$LOG"` swallows the python exit code (tee always exits 0), so the bash wrapper exits 0 and reports "iMessage pull done" even when chat.db couldn't be opened. Same shape as the X-bookmarks bug pre-fix.

---

## Section C — Synthesis jobs — actually producing artifacts?

| Job | Output destination | Expected | Last artifact | Trend | Verdict |
|---|---|---|---|---|---|
| daily-correlator | `quartz/content/raw/signal-briefs/signal-brief-*.md` | daily 06:00 | **2026-05-07** (1.8 KB) | 4-day gap May 8–11 | 🔴 **plist not loaded; signal briefs stopped 2026-05-07.** Last `.correlator-log` write 2026-05-04. The strongest piece in the synthesis layer is dark for 4 days. |
| editorial (bookmarks) | `outputs/editorial/*.md` | daily 19:30 | 2026-05-09 (2.2 KB) | 5 files in 7d | ✅ working; uses last-known-good bookmark fallback to keep firing even when capture is dead. |
| plan-radar | `outputs/plan-radar/*.md` | daily 12:00 | 2026-05-11 (7.5 KB) | 4 files in 7d | ✅ working. |
| pattern-surfacer | `outputs/patterns/*.md` | Wed + Sun 07:00 | 2026-05-05 (3.6 KB, manual) | 0 scheduled runs ever | 🔴 plist not loaded. Wed 5/7 and Sun 5/10 should have produced files; both missed. |
| weekly-operating-brief | `outputs/operating-brief/2026-WNN.md` | Mon 08:00 | 2026-05-04 (W19, 5.5 KB) | 1 in 30d | 🔴 **silently bailing.** Mon 2026-05-10 run logged `No bookmark files in last 7 days — skipping brief` and exited 0. The plan's "relax precondition" change is not in the script. Audit §B item 2 finding re-confirmed and worse: now the bookmarks cascade has killed the operating brief 2× in a row (W18 missing, W20 missing). |
| weekly-compile | `quartz/content/raw/compile-*.md` | Fri 14:00 | 2026-05-01 (compile-2026-05-01.md) | 0 in 7d (next due Fri 5/8) | ⚠️ on schedule; will know more Friday. |
| entity-graph-builder | `wiki/hot/relationship-radar.md`, `wiki/hot/open-commitments.md`, `wiki/hot/entity-queue.md`, plus `wiki/people/X.md` writes | daily 00:15 | 2026-05-05 08:51 (manual) | 0 scheduled runs | 🔴 plist not loaded. All three hot files frozen 2026-05-05. Last actual run wrote 35 people updates + 19 commitments — the design is correct, the execution is dead. **This is the same finding as audit §B item 12; the plan claimed it was fixed; it is not fixed.** |
| session-learnings | `outputs/learnings/learnings-*.md` | Sun 07:30 | 2026-05-03 (one file) | 0 | 🔴 plist not loaded — Sun 5/10 should have produced a fresh rollup; nothing. |
| project-activity | `wiki/projects/*.md` (auto block) | daily 08:00 | 2026-05-05 08:00 (last `.project-activity-log` line) | 0 since 2026-05-05 | 🔴 plist not loaded — all 6 project pages frozen May 5. |
| concept-of-the-day | `wiki/concepts/*.md` (rotates `last_revisited`) + briefing block | daily 08:15 | 2026-05-05 08:15 (`.concept-rotation-log`) | 0 in 7d | 🔴 plist not loaded. |
| weekly-pitch-mistake | `wiki/founder/{pitches,mistakes}.md` | Mon 07:30 | 2026-05-04 07:30 | 0 in 7d | 🔴 plist not loaded. |
| related-suggester | `outputs/related-suggestions/queue-*.md` | Wed 11:30 | 2026-05-03 11:33 (one file) | 0 in 7d | 🔴 plist not loaded — Wed 5/7 should have produced a queue; nothing. |
| compute-last-contact | `wiki/hot/relationship-signals.md` (or per-person `wiki/people/X.md` last_contact) | called from morning-briefing + own plist | 2026-05-05 00:05 (one autonomous run) | 0 since | 🔴 plist not loaded. Standalone runs are not happening. The compute-last-contact call inside `morning-briefing.sh` is presumably still running on weekdays. |
| last-contact-coverage | `outputs/last-contact-coverage*` | unknown weekly | 2026-05-03 21:07 (one log entry) | 0 | 🔴 plist not loaded. |
| chroma-index | `pi-workspace/.chroma-data/` | daily 09:15 | **frozen 2026-05-05** | 4 consecutive preflight failures | ⚠️ plist loaded, exit code 2 every run, LM Studio not running so embeddings can't be computed → ingest aborted with index preserved. Index is now ≥6 days behind reality. |
| brain-lint | `outputs/lint/*` | Sun 09:00 | 2026-05-06 07:51 (manual) | 0 scheduled runs | 🔴 plist not loaded. |
| heartbeat | `outputs/health/heartbeat-*.md` | daily 09:20 | 2026-05-11 09:20 (1.2 KB) | 6 in 7d | ✅ working — and correctly flagging today's missing briefing — but **the heartbeat artifact list is hardcoded to 5 ancient paths** and has not been updated since the sentinel was added. It still points at `quartz/content/raw/pulse/pulse-2026-W17.md` (402 hours stale, ignored) and `teams-transcript-website-update-review-call-2026-04-28.md` (302 hours stale because it picks the last alphabetically, not the most recent by mtime — `find ... | sort | tail` sorts lexically, so any file whose name sorts before today's wins). The signal it surfaces is mostly noise — Andres scrolls past it. |

---

## Section D — Latent risks

### D1. Browser-session dependencies (cookie expiry is universal)

Only one script uses gstack `/browse`: **`scrape-x-bookmarks.sh`**. The cookie-expiry failure mode is therefore localized — but the cookie has now expired three times in 30 days (initial setup, 2026-05-02, 2026-05-03). The recovery action is a one-line copy-paste in `sentinel-config.tsv`:

```
/Users/jarvisurrego/.claude/skills/setup-browser-cookies/setup-browser-cookies x.com
```

…which Andres can run from any terminal. The sentinel's `action_hint` already encodes this. The fix is to **load the sentinel plist** so the action_hint actually reaches Andres' inbox. Until then, every X cookie expiry will silently kill (a) bookmarks capture, (b) bookmarks-editorial — uses last-known-good fallback, partially protected — and (c) weekly-operating-brief — uses hard precondition, fully unprotected.

### D2. API-key dependencies

| Surface | Key | Storage | Rotation | Failure mode if missing |
|---|---|---|---|---|
| Brave Search | `BRAVE_API_KEY` | `/Users/jarvisurrego/.secrets/brave_api_key.txt` | unknown | brain-query / web-research fallback silently degrades to no-web mode |
| m365 / Microsoft Graph | OAuth token managed by `m365` CLI (`~/.m365`) | local keyring | tokens auto-refresh until refresh-token expires (~90d) | morning-briefing email + sentinel email both fail; calendar+mail pulls fail. **No alert path.** |
| Apollo MCP | per-MCP-instance | MCP server config (`mcp__addb753e-...`) | n/a (MCP-scoped) | Manual Apollo lookups in CC sessions fail; no automation depends on it |
| ANTHROPIC_API_KEY | per-Claude-Code-session | OS keychain | Andres manages | every script that calls `/opt/homebrew/bin/claude -p` fails. Same fate as a Claude outage. |
| GROQ_API_KEY | `transcribe-meetings.sh` + `transcribe_local.py` | env var | unknown | Voice transcription dead — no current automation depends; manual use only. |

**Single biggest gap:** no alerting on m365 token expiry. The `m365 outlook mail send` call in `morning-briefing.sh` line ~680 and `sentinel.sh` line 140 both fail non-fatally (`set +e` then check `$EMAIL_EXIT`). If the token expires, the recovery is `m365 login --auth-type browser`, prompting in a UI Andres doesn't open daily. The sentinel logs `WARNING: critical email send failed` to `.sentinel-log` — but the sentinel is the thing supposed to escalate, so this fails closed (silently).

### D3. m365 token expiry — how do we know?

We don't. `m365` CLI manages tokens in `~/.config/m365/`. Refresh tokens for Microsoft Graph typically last 90 days but rotate on use. There is **no probe** in any script that asserts "the token is valid right now" before relying on it. Recommended: add a `m365 spo cli reconsent` or `m365 status` ping to the sentinel run and surface as a row.

### D4. Single-source-of-failure patterns

1. **X cookies → bookmarks → editorial + operating-brief.** Cookies expire → bookmarks file missing → operating-brief silently bails. Editorial fallbacks survive. The fanout cascade is exactly the audit §B item 2 prediction, observed twice in the wild.
2. **LM Studio → chroma-index → correlator's seed-context.** LM Studio not running → chroma ingest exits 2 → index stale. Correlator still runs (when its plist is loaded) and queries the stale index — silently degrades the quality of "historical context" sections without any indicator. Add an LM-Studio probe to sentinel.
3. **morning-briefing.sh → Claude Write-tool reliability.** Today's 2026-05-11 run shows the stdout-recovery fallback can fail when Claude responds in a different shape. The briefing IS the trust signal for everything below it; a failed briefing leaves Andres blind. Worth adding a third fallback: when both Write and stdout-recovery fail, generate a minimal "Brain is alive but synthesis failed — here are the raw inputs" briefing from the assembled context so Andres always has *something*.
4. **launchctl boot state → every plist.** If macOS reboots / Andres logs out, plists boot-out unless `RunAtLoad` is set. Of the 27 plists, audit a sample for missing `RunAtLoad` → reboot fragility. (Not exhaustively checked here; flag for follow-up.)

### D5. Silent-success patterns (the bug class behind today's incident)

1. **`imessage-pull.sh`** — wraps python with `"$PY" imessage-pull.py "$@" 2>&1 | tee -a "$LOG"`. `tee` always exits 0, so the python exit code is lost. The bash wrapper proceeds to commit + push as if everything is fine, and the launchctl `last exit code = 0` reports success. **This is the same shape as the X-bookmarks pre-fix bug.** Fix: use `set -o pipefail` at the top of the script and a temp file pattern instead of `tee`, OR add an explicit post-check that today's expected output file exists.
2. **`scrape-x-bookmarks.sh`** has 8 instances of `|| true` and a `set +e` block around the commit step (lines 180–186). Each is justifiable individually (browse subcommands can fail without aborting the scrape) but the aggregate effect is the same as the May-5 syntax-error bug: a real failure can sneak through as exit 0. The new zero-item guard (lines 158–172) is the right shape — assert on output, not just on commands.
3. **`morning-briefing.sh` line 312** — `|| echo "[$(date '+%Y-%m-%d %H:%M')] WARNING: brain-ingest failed (non-fatal)" >> "$LOG_FILE"`. Today (2026-05-11) brain-ingest **did** fail (`declare: -A: invalid option` because the script is using zsh-incompatible bash 3 syntax; line 62 has an unquoted filename with `&` triggering a syntax error). The warning was logged. Nothing else happened. The briefing then failed for an unrelated reason and that ALSO logged a warning. Both warnings sit in `.briefing-log` for the next human to see — but there is no human reviewer pass.
4. **`weekly-operating-brief.sh` line 56–59** — `if BOOKMARK_FILES -eq 0 then echo "skipping brief"; exit 0`. **The script reports success on skip.** A weekly synthesis job that didn't run is reported the same as one that ran. The 2026-05-03 plan said this would be relaxed; it wasn't. **Same shape, different surface.**
5. **`bookmarks-editorial.sh`** — has a "last known good" fallback that walks back through prior days when today's bookmarks file is missing. This is the *correct* shape (graceful degradation with a logged reason), and is why editorial is the one script in the bookmarks family still producing daily output. Steal this pattern for the operating brief.
6. **`brain-heartbeat.sh`** — `last_log_signal()` greps tail-40 for `ERROR|WARNING|npm error|Traceback|failed`. This catches **shouted** failures but misses (a) `exit 0` returns, (b) silent skips like `skipping brief`, (c) empty-output runs. The heartbeat reports "clean" for an operating-brief that has silently bailed twice in a row.

### D6. Hardcoded path/credential references

Almost every script hardcodes:
- `/Users/jarvisurrego/My Brain/pi-workspace`
- `/Users/jarvisurrego/My Brain/knowledge-base`
- `/opt/homebrew/bin/m365`
- `/opt/homebrew/bin/claude`
- `/Users/jarvisurrego/mlx-env/bin/python` (imessage)
- `/Users/jarvisurrego/.claude/skills/gstack/browse/dist/browse` (with home-install fallback)
- The git remote `felipeu28`

If the Mac's hostname changes, home dir moves, or the user is renamed, every script breaks. This is acceptable for a single-user laptop-resident system but should be acknowledged. Backup-path-aware would be migration to a `BRAIN_HOME` env var with a single `.env` shim. Not urgent.

### D7. Permission-gated commands

1. **`imessage-pull.py`** — needs Full Disk Access for `/Users/jarvisurrego/mlx-env/bin/python` to read `~/Library/Messages/chat.db`. **Currently missing**, killing the job. macOS reset Full Disk Access permissions on the python binary when it was upgraded or when the venv was rebuilt — both common.
2. **gstack `/browse` cookie import** — interactive setup via Andres' shell. Cookies live in the headless browser's profile, which lives in the project-scoped CWD (`KB_DIR`). Reauth is required when X rotates the session cookie; X is known to do this aggressively.
3. **`m365 outlook mail send`** — uses cached OAuth, but the m365 binary itself needs Keychain access. Confirmed working today via the sentinel email test on 2026-05-04 and 2026-05-05.
4. **`launchctl bootstrap`** — requires user session (`gui/$(id -u)`); cannot be run from a script with set +e fallback because the syntax errors out non-interactively when the user isn't logged in.

---

## Section E — Top 5 immediate fixes

Ranked by risk × ease.

### 1. **Load the 12 unloaded plists, starting with sentinel.** 🔴

- **What's broken:** 12/27 plists physically present on disk but never loaded. Every Week-3/4 implementation-plan deliverable is dead because of this single discipline gap. The entity-graph "fixed" on 2026-05-03 is back to its dead state.
- **The change:** One bash loop run by Andres:
  ```bash
  cd "/Users/jarvisurrego/My Brain/pi-workspace/launchd"
  for p in com.moil.brain.sentinel com.moil.brain.entity-graph com.moil.brain.daily-correlator com.moil.brain.pattern-surfacer com.moil.brain.project-activity com.moil.brain.session-learnings com.moil.brain.last-contact com.moil.brain.last-contact-coverage com.moil.brain.concept-of-the-day com.moil.brain.related-suggester com.moil.brain.brain-lint com.moil.brain.weekly-pitch-mistake; do
    launchctl bootstrap gui/$(id -u) "${p}.plist"
  done
  launchctl list | grep com.moil.brain | wc -l   # should be ≥27
  ```
- **Effort:** S (≤5 min).
- **Risk if not fixed in 7d:** The Brain stays input-rich and reflection-poor as in the prior audit, but now *also* loses the new entity-graph, project-activity, and session-learnings work that just shipped. Effectively reverts the Week-1/2 implementation to nothing.

### 2. **Reauth X cookies + write a sentinel `--probe` that runs after reauth.** 🔴

- **What's broken:** X cookies expired 2026-05-03. Five days of bookmarks lost. Operating-brief silently bailed twice. The sentinel `action_hint` has the exact recovery command but isn't running.
- **The change:** Andres runs `/Users/jarvisurrego/.claude/skills/setup-browser-cookies/setup-browser-cookies x.com`, then `bash pi-workspace/bin/scrape-x-bookmarks.sh` manually to confirm. Add a `bash bin/sentinel.sh --stdout` to a precommit alias so the daily state is visible.
- **Effort:** S (≤15 min).
- **Risk if not fixed in 7d:** Week 19 operating brief also missing → no Monday decision doc → Andres walks into a week blind.

### 3. **Fix `weekly-operating-brief.sh` `BOOKMARK_FILES -eq 0` precondition.** 🔴

- **What's broken:** The 2026-05-03 plan said this would be relaxed to "0 bookmarks but ≥3 email or teams files = run with degraded grounding"; line 56 still has the hard `exit 0`.
- **The change:** Edit `pi-workspace/bin/weekly-operating-brief.sh` lines 56–59:
  ```bash
  if [[ $BOOKMARK_FILES -eq 0 ]]; then
    if [[ $COMM_FILES -lt 3 ]]; then
      echo "[$(date)] Skipping: <3 communication files AND 0 bookmarks" >> "$LOG_FILE"
      exit 0
    fi
    echo "[$(date)] WARNING: 0 bookmark files, running with degraded grounding" >> "$LOG_FILE"
    BOOKMARKS_CORPUS="(no bookmarks captured this week — analyze communications only)"
  fi
  ```
  Move the line 56 check **after** the COMM_FILES collection (currently lines 66–75), so it has the count to compare against.
- **Effort:** S (≤20 min).
- **Risk if not fixed in 7d:** Every week where the X scrape fails for any reason silently kills the most important synthesis artifact. This is the cascade fix.

### 4. **Fix `imessage-pull.sh` silent-success pattern + grant Full Disk Access.** 🔴

- **What's broken:** Plist loaded since 2026-05-06, has produced zero capture files. Underlying python errors silently swallowed by `tee`.
- **The change:** Two parts:
  1. Andres adds `/Users/jarvisurrego/mlx-env/bin/python` to System Settings → Privacy & Security → Full Disk Access.
  2. Edit `pi-workspace/bin/imessage-pull.sh`:
     - Line 21: change `set -e` to `set -eo pipefail`
     - After line 27 (`"$PY" "$WORKSPACE/bin/imessage-pull.py" "$@" 2>&1 | tee -a "$LOG"`): add `EXPECTED="$KB_DIR/raw/imessages-${DATE}.md"; [[ -f "$EXPECTED" ]] || { echo "[$(date)] ERROR: expected output $EXPECTED not produced" >> "$LOG"; exit 2; }`
- **Effort:** S (≤30 min).
- **Risk if not fixed in 7d:** Personal-context layer (iMessage threads with family, contacts) silently absent from the Brain. Andres never knows.

### 5. **Replace `brain-heartbeat.sh` 5-row hardcoded list with sentinel-driven dynamic list, and demote weekly-pulse references.** ⚠️

- **What's broken:** Heartbeat is the only loaded health-monitor that runs daily, and its check list is stale — 2 of 5 rows are permanently noise (weekly-pulse 402h stale, teams-transcript-website-update 302h stale because of lexical sort). Andres scrolls past it. Once sentinel is loaded (fix #1), heartbeat becomes redundant *or* should become a wrapper around sentinel.
- **The change:** Two options, pick one:
  - **Option A (faster):** Drop the weekly-pulse and stale-named-teams-file rows from `brain-heartbeat.sh` (lines 92–93 and 87–99). Replace teams selector with proper mtime sort: `LAST_TEAMS_RAW=$(find "$KB_DIR/raw" -maxdepth 1 -name 'teams-*.md' -type f -exec stat -f '%m %N' {} + | sort -rn | head -1 | cut -d' ' -f2-)`.
  - **Option B (better):** Replace heartbeat entirely with `bash bin/sentinel.sh --stdout` piped into a `## Brain Status` block in the briefing. Then deprecate the heartbeat plist.
- **Effort:** S (≤30 min) for A, M (~90 min) for B.
- **Risk if not fixed in 7d:** Trust signal stays noisy; Andres learns to ignore the only daily Brain status output.

---

*End of audit. Five fixes total effort: ≤2 hours. The plist-load fix alone restores ~9 of the 13 broken-rated rows in Section A and B. The pattern is clear: shipping plists without verifying `launchctl bootstrap` is the load-bearing failure mode that the 2026-05-03 plan inherited and the 2026-05-07 audit has now caught at scale.*

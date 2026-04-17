---
tags:
  - graph/leaf
type: report
generated: 2026-04-17
---

# Automation Status Report — Week of Apr 14–17, 2026

**Audit run:** 2026-04-17 ~15:30  
**Scope:** All 10 LaunchAgent automations for the Moil Brain  
**All 10 agents are loaded** (confirmed via `launchctl list`)

---

## GitHub Pages Deploy ❌ (CRITICAL — every push fails)

**Status:** Every single push to `felipeu28/main` since at least Apr 14 triggers a GitHub Actions run that fails at the deploy step. 10+ consecutive failures this week.

**Root cause:** GitHub Pages is **not enabled** in the repository settings. The `actions/deploy-pages@v4` step returns:
```
HttpError: Not Found (404)
Ensure GitHub Pages has been enabled: https://github.com/Felipeu28/my-brain/settings/pages
```

The Quartz **build step succeeds** — the site compiles correctly and the artifact is uploaded. Only the deploy step fails.

**Fix:** Go to [https://github.com/Felipeu28/my-brain/settings/pages](https://github.com/Felipeu28/my-brain/settings/pages) → set Source = "GitHub Actions". One-click fix. No code changes needed.

**Impact:** The live GitHub Pages site has not received any updates this entire week. All commits are stuck in the artifact. The Vercel deploy (separate) IS working — `✓ Pushed to Vercel` appears in all logs.

---

## morning-briefing ⚠️

- **LaunchAgent loaded:** YES
- **Log:** `~/.../pi-workspace/.briefing-log`
- **Files created this week:**
  - `quartz/content/raw/briefings/briefing-2026-04-14.md` (Apr 14, 08:03) — created via morning-briefing Apr 15 backfill
  - `quartz/content/raw/briefings/briefing-2026-04-15.md` (Apr 15, 08:47) ✅
  - `quartz/content/raw/briefings/briefing-2026-04-16.md` (Apr 16, 08:47) ✅
  - `quartz/content/raw/briefings/briefing-2026-04-17.md` (Apr 17, 08:46) ✅
- **Last successful run:** Apr 17, 08:47
- **Status:** ✅ Briefing generation working / ⚠️ Email delivery broken

**Issue:** `m365 outlook mail send` fails every day with `Error: Invalid option: '-'`. The briefings ARE being generated, committed, and pushed — but never emailed to Andres. The error appears twice per run (likely two recipient fields using `-` as a separator). This has been silently failing and logging `WARNING: email send failed` without alerting.

**Fix:** Check `morning-briefing.sh` for the m365 command — a flag is using `-` where `--` is needed, or the m365 CLI version changed its interface. Run `m365 outlook mail send -h` to see current syntax.

---

## chroma-index ✅

- **LaunchAgent loaded:** YES
- **Log:** `~/.../pi-workspace/.chroma-log`
- **Runs this week:**
  - Apr 14 at 09:15 — 174 pages, 37 added, 578 updated, 615 total chunks
  - Apr 15 at 09:15 — 223 pages, 168 added, 610 updated, 783 total chunks
  - Apr 16 at 09:15 — 229 pages, 33 added, 778 updated, 816 total chunks
  - Apr 17 at 09:15 — 230 pages indexed (standalone run at 9:15am)
  - Apr 17 at 14:08 — 231 pages, 4 added, 819 updated, 828 total chunks (also triggered by weekly-compile)
- **Last successful run:** Apr 17, 14:09
- **Status:** ✅ Fully healthy. Running daily as expected.

**Note:** On Fridays, chroma-index runs twice — once at 9:15am (standalone plist) and again at ~14:08 as part of `weekly-compile.sh`. This is harmless but slightly redundant. Also: harmless `DeprecationWarning` about `datetime.utcnow()` in the Python script (no action needed unless you want to suppress it).

---

## teams-daily ⚠️

- **LaunchAgent loaded:** YES
- **Log:** `~/.../pi-workspace/.teams-log`
- **Files created this week:**
  - `raw/teams-2026-04-14.md` (759 bytes — nearly empty, ~0 messages for 1-day window)
  - `raw/teams-2026-04-15.md` (10,463 bytes — ✅ good pull)
  - `raw/teams-2026-04-16.md` — **MISSING** (failed pull)
  - `raw/teams-2026-04-17.md` — **NOT YET** (runs at 6pm today)
- **Last successful run:** Apr 15 at 18:07
- **Status:** ⚠️ Intermittent 504 crashes — data loss on Apr 16

**Issues:**
1. **Apr 16 full failure:** At 18:00 the script hit a `504 Gateway Timeout` from `graph.microsoft.com` while paginating through a large Teams channel. Python threw an unhandled `HTTPError` and crashed — **no file was saved**. The LaunchAgent exit code was still `0` (deceptive — the script doesn't propagate errors).
2. **Apr 15 partial failure:** The 270-day pull (`teams-2026-04-12.md`) also hit a 504 midway through, but it saved what it had before the crash. The 1-day daily pull succeeded separately.
3. **Apr 14 very small:** 759 bytes for a 1-day pull suggests 0 or 1 Teams messages that day. Likely correct (low activity day), not a failure.

**Fix:** Add `try/except HTTPError` around the paginated GET in `scripts/teams_pull.py` → on 504, save whatever was collected so far and write a partial output file rather than crashing with nothing.

---

## x-bookmarks ⚠️

- **LaunchAgent loaded:** YES
- **Log:** `~/.../pi-workspace/.bookmarks-log`
- **Schedule:** Sundays at 8pm
- **Last run:** Apr 12, 20:00 (Sunday before audit window — correct, next run is Apr 19)
- **Status:** ⚠️ Requires manual Keychain approval — unattended execution uncertain

**Issue:** The Apr 12 run paused mid-execution asking for a macOS Keychain dialog: "A macOS Keychain dialog should be popping up... Please click Allow or Always Allow." The log then shows "[2026-04-12 20:02] X bookmarks capture finished" — it completed, but only because someone was at the machine. If the Mac is asleep or Andres isn't watching, the script may hang or skip.

**Fix:** Pre-approve the Keychain access by running the script once manually and clicking "Always Allow". Or switch to a cookie-based auth method that doesn't trigger Keychain prompts.

---

## weekly-compile ✅

- **LaunchAgent loaded:** YES
- **Log:** `~/.../pi-workspace/.compile-log`
- **Schedule:** Fridays at 2pm
- **Run this week:** Apr 17 at 14:09 ✅
- **Output:** `quartz/content/raw/compile-2026-04-17.md` created
- **Commit:** `920107b Weekly compile — 2026-04-17` (23 files, +368 lines)
- **New pages:** `wiki/people/mayra-adams.md` created
- **Status:** ✅ Ran on time, committed, pushed to GitHub.

---

## weekly-pulse ✅

- **LaunchAgent loaded:** YES
- **Log:** `~/.../pi-workspace/.pulse-log`
- **Schedule:** Fridays at 3pm
- **Run this week:** Apr 17 at 15:00–15:01 ✅
- **Output:** `quartz/content/raw/pulse/pulse-2026-W16.md` created
- **Commit:** `1544bec auto: My weekly-pulse.sh .sh output 2026-04-17`
- **Status:** ✅ Ran on time, top signals captured, committed and pushed.

**Pulse highlights captured:** Alloy ATX closed ($75/mo), Helotes EDC call locked Apr 22, Jacob Centeno referral channel, EDC AI-tools lane opened. Action items: Jesutomilola reply overdue, FitLogic delivery Apr 18, MEMORY.md at 204 lines (over 200-line cap).

---

## content-calendar ✅

- **LaunchAgent loaded:** YES
- **Log:** `~/.../pi-workspace/.content-log`
- **Schedule:** Mondays at 9am
- **Run this week:** Monday Apr 13, 09:00 ✅ (Apr 13 is Monday — audit window starts Apr 14)
- **Output:** `outputs/content-calendar/calendar-2026-W16.md` → synced to `quartz/content/raw/content-calendar/calendar-2026-W16.md` on Apr 15 via morning-briefing sync
- **Status:** ✅ Ran on schedule. Covers W16 (Apr 13–17) + W17, W18, W19 content plans.

**Note:** The file's quartz/content timestamp shows Apr 15 08:03 because `sync_wiki.sh` hadn't run between Apr 13 and Apr 15. The script ran correctly on Monday — the delay was just in the sync step. Not a bug.

---

## email-digest ✅ (partial week)

- **LaunchAgent loaded:** YES
- **Log:** `~/.../pi-workspace/.email-log`
- **Files created this week:**
  - `raw/email-digest-2026-04-14.md` (Apr 14, 18:31) ✅ — 10 inbox, 25 sent, 17 contacts
  - `raw/email-digest-2026-04-15.md` (Apr 15, 18:31) ✅ — 13 inbox, 25 sent, 32 contacts
  - `raw/email-digest-2026-04-16.md` (Apr 16, 18:31) ✅ — 13 inbox, 25 sent, 32 contacts
  - `raw/email-digest-2026-04-17.md` — **NOT YET** (runs at 6:30pm today — expected)
- **Last successful run:** Apr 16, 18:31
- **Status:** ✅ Running daily, all digests committed and pushed.

---

## kb-health ✅ (not scheduled this week)

- **LaunchAgent loaded:** YES
- **Schedule:** Sundays at 8am only
- **Last run:** Would have been Apr 12 (before audit window)
- **Next run:** Apr 19 (Sunday)
- **Status:** ✅ Not expected to run Apr 14–17. On schedule.

---

## heartbeat ✅

- **LaunchAgent loaded:** YES
- **Log:** `~/.../pi-workspace/.heartbeat-log`
- **Files created:**
  - `outputs/health/heartbeat-2026-04-15.md` ✅
  - `outputs/health/heartbeat-2026-04-16.md` ✅
  - `outputs/health/heartbeat-2026-04-17.md` ✅
- **Status:** ✅ Runs as part of morning-briefing flow. Healthy.

---

## Summary

**7 of 9 scheduled automations running correctly this week** (kb-health not expected; x-bookmarks ran last Sunday as designed).

### Critical issues

| # | Issue | Impact | Fix |
|---|-------|--------|-----|
| 1 | **GitHub Pages deploy 404** — every push fails | Site not updating on GitHub Pages (Vercel still works) | Enable Pages at github.com/Felipeu28/my-brain/settings/pages → Source = GitHub Actions |
| 2 | **Morning briefing email broken** — `m365 mail send "Invalid option: '-'"` | Andres never receives the email briefing | Fix flag syntax in `morning-briefing.sh` m365 command |
| 3 | **Teams 504 crash — no error handling** | Apr 16 pull completely lost; Apr 15 partial | Add try/except around HTTP pagination in `scripts/teams_pull.py` |

### Warnings

| # | Issue | Impact |
|---|-------|--------|
| 4 | **x-bookmarks needs Keychain dialog** — requires user at screen | May silently fail if run while machine is unattended |
| 5 | **MEMORY.md at 204 lines** — over 200-line soft cap | Index truncation in future Claude sessions |
| 6 | **chroma-index runs twice on Fridays** — 9:15am + weekly-compile | Harmless but wastes ~1 min of CPU |
| 7 | **teams Apr 14 empty** — 759 bytes — 0 messages pulled | Likely low activity day; verify manually |

### Recommended fixes in priority order

1. **GitHub Pages** — 1-click fix in repo settings. Do this today.
2. **m365 email send** — Run `m365 outlook mail send -h`, check flag syntax, update `morning-briefing.sh`.
3. **Teams 504 handling** — Wrap HTTP GET in `teams_pull.py` with try/except + write partial output on error.
4. **MEMORY.md pruning** — Move archived items to `log.md` to get back under 200 lines.
5. **x-bookmarks Keychain** — Run once manually with "Always Allow" to pre-authorize.

---
type: session-learnings
week_ending: 2026-05-17
sessions_analyzed: 130
sessions_filtered: 6
tags:
  - graph/leaf
---

# Session Learnings — Week ending 2026-05-17

## Decisions made
- 2026-05-17 — Build a 5-tier Brain action pipeline; start with Tier-1 daily outbox builder (`build-outbox.py` + launchd plist). The Brain shifts from passive-ingest to driving daily action. Source: [[raw/sessions/claude-code-2026-05-17-see-it-now]]
- 2026-05-15 — Brain synth gets a per-node fan-out cap + tighter prompt to stop hub spider-webs (root cause of "animal kingdom" connecting to everything). Source: [[raw/sessions/claude-code-2026-05-15-let-s-start-a-full-audit-of-the-quality-of-data-we]]
- 2026-05-15 — Local-client-prospector: ship search-engine fallback + expand trigger surface for construction/trades after Buda baseline test validated the skill. Source: [[raw/sessions/claude-code-2026-05-15-find-construction-companies-in-buda-tx-within-10-k]]
- 2026-05-13 — After Martins (nephew, age 11) family-testing in Colombia: ship recent-chats sheet + iOS install nudge; surface real story-generation errors instead of silent failure. Source: [[raw/sessions/claude-code-2026-05-13-implementation-plan-remaining-items-from-family-te]]
- 2026-05-12 — Office-hours verdict: "We start with A but we need C. C solves the issues they face, A becomes more steps; the moat is removing those steps." Path C is the strategic target. Source: [[raw/sessions/claude-code-2026-05-12-command-message-office-hours-command-message]]
- 2026-05-10 — Clio bilingual: full-ambient detection — detect kid's input language at every turn and use `label_es` in brain context (not just profile preference). Source: [[raw/sessions/claude-code-2026-05-10-bilingual-claim-audit-implementation-plan]]

## Things learned
- gstack `/browse` cookie sessions are CWD-scoped. Importing x.com cookies from `~/My Brain` or `$HOME` is invisible to `scrape-x-bookmarks.sh` because the script `cd`s into `$KB_DIR` first. Burned ~10 min on 2026-05-12 — exact failure mode CLAUDE.md already warned about. Source: [[raw/sessions/claude-code-2026-05-12-the-x-bookmarks-freshness-sentinel-critical-and-pi]]
- Grok TTS flips voice mid-MP3 unless you pass an explicit language tag — same bug previously hit chat, now hit stories. Source: [[raw/sessions/claude-code-2026-05-09-ship-phase-1-start-phase-2-5]]
- Stories' SSE stream was silently dropping because Vercel function `maxDuration` was too short to let generation finish. Source: [[raw/sessions/claude-code-2026-05-09-ship-phase-1-start-phase-2-5]]
- Local-client-prospector survived a real bot-block in Buda by falling back to search engines — proved resilience pattern: don't bail, drop confidence to Medium and continue. Source: [[raw/sessions/claude-code-2026-05-15-find-construction-companies-in-buda-tx-within-10-k]]
- Vercel mobile-Safari quirk: not all browsers let the Luna orb receive clicks even when other buttons work — needs explicit pointer-event handling. Source: [[raw/sessions/claude-code-2026-05-13-implementation-plan-remaining-items-from-family-te]]

## Abandoned approaches
- Vague "Run /setup-browser-cookies x.com" error message in `scrape-x-bookmarks.sh` — replaced with a CWD-explicit, self-explaining error after it caused a repeat 10-min loss. Source: [[raw/sessions/claude-code-2026-05-12-the-x-bookmarks-freshness-sentinel-critical-and-pi]]
- Profile-only language preference for bilingual mode — abandoned for per-turn input-language detection ("full ambient") because static toggles can't keep up with code-switching kids. Source: [[raw/sessions/claude-code-2026-05-10-bilingual-claim-audit-implementation-plan]]
- Silent story-generation failures (showing nothing when API errored) — replaced with surfacing the real error to UI. Source: [[raw/sessions/claude-code-2026-05-13-implementation-plan-remaining-items-from-family-te]]

## Recurring themes
- Clio post-launch field bugs (5 sessions): bilingual gaps, voice/TTS flips, story persistence, orb un-clickable, brain over-fan-out — all surfaced from real-family testing this week.
- Brain self-repair (5 sessions): cookie-error self-explain, freshness sentinel critical, fan-out cap, pipeline plan, weekly compile — visible shift from feature-build to "make the Brain robust enough to trust."
- Daily ingestion automation cadence (15+ sessions across the week): teams/email/briefing/plan-radar/kb-agent runs are now boringly reliable — they fire and finish without intervention.
- Path A vs Path C strategic tension (3 sessions): office hours, eng review, autoplan all circling the same scope-vs-moat decision for Clio.

## Unresolved questions
- Push gate: multiple ingest runs (2026-05-13, 2026-05-15) ended with "Want me to push to `felipeu28 main`?" — the global no-auto-push rule is correctly holding, but creates a queue of staged-but-unpushed work. Source: [[raw/sessions/claude-code-2026-05-13-check-for-any-new-files-in-raw-and-raw-onedrive-tr]], [[raw/sessions/claude-code-2026-05-15-run-the-weekly-knowledge-base-compile-and-cleanup-]]
- PR #85 (Clio family-testing batch) has merge conflicts blocking land. Source: [[raw/sessions/claude-code-2026-05-13-implementation-plan-remaining-items-from-family-te]]
- Brain visualization for mobile + desktop is still unsolved — flagged in family testing, not addressed this week. Source: [[raw/sessions/claude-code-2026-05-13-implementation-plan-remaining-items-from-family-te]]
- First gstack office-hours doc location — surfaced but not yet opened/acted on. Source: [[raw/sessions/claude-code-2026-05-17-help-me-find-the-document-i-got-from-the-first-off]]

---

*Generated by session-learnings.sh at 2026-05-17 09:00. Source: 130 sessions in last 7 days, 6 automation self-runs filtered.*

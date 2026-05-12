---
type: session-learnings
week_ending: 2026-05-12
sessions_analyzed: 65
sessions_filtered: 2
tags:
  - graph/leaf
---

# Session Learnings — Week ending 2026-05-12

## Decisions made
- 2026-05-03 — Adopt Garry Tan's gstack pattern for Clio with 5 named specialists (clio-cso, clio-qa, clio-design-review, clio-voice-qa, clio-parent-comms) plus parallel-sprint model. Source: [[raw/sessions/claude-code-2026-05-03-week-1-execution]]
- 2026-05-03 — Build multi-provider cascade for LLM + TTS, ordered cost-consciously, so chat turns never fail and don't burn money. Source: [[raw/sessions/claude-code-2026-05-03-week-1-execution]]
- 2026-05-06 — Phase 0 "subtraction" on Clio: kill duplicate gamification, dead `synthesize` endpoint, BrainView tab buffet, weekly digest tiles. Kid lands directly in their world, voice-on-tap, biomes feel like places. Source: [[raw/sessions/claude-code-2026-05-06-phase-0-subtraction]]
- 2026-05-08 — Stop pushing PRs for every change; add `npm run dev:lan` for iPhone testing on local WiFi before pushing. Source: [[raw/sessions/claude-code-2026-05-08-command-message-gstack-command-message]]
- 2026-05-04 — Accelerator strategy: Speedrun/YC/Sputnik ATX already drafted; remove "SOC 2 compliant" and "AI for business applications cert" from bio; reframe "2 years of Claude Code" as "build with AI, obsessively learned." Source: [[raw/sessions/claude-code-2026-05-04-application-scoring-proposed-changes]]
- 2026-05-09 — Choose Path B (validation) for Clio: ship D4 iPhone Safari voice (Web Speech → Whisper/Deepgram) and D3 COPPA flow before strategic Path C. Source: [[raw/sessions/claude-code-2026-05-09-active-plan-gstack-projects-felipeu28-clio-ceo-pla]]
- 2026-05-10 — Bilingual claim must be real: detect kid's input language at the turn boundary and use `label_es` in brain context, not just UI text. Source: [[raw/sessions/claude-code-2026-05-10-bilingual-claim-audit-implementation-plan]]

## Things learned
- Grok TTS flips voice mid-MP3 unless you pass an explicit language tag — that one fix killed the "two voices reading the same answer" bug Andres reported all week. Source: [[raw/sessions/claude-code-2026-05-09-ship-phase-1-start-phase-2-5]]
- iPhone silent switch silently mutes Web Audio output; routing through `MediaStreamDestination → <audio>` sink ignores the switch and recovers playback. Source: [[raw/sessions/claude-code-2026-05-06-phase-0-subtraction]]
- The X-bookmarks scraper was failing silently with zero items for weeks; the original COUNT shell pattern defeated the zero-item guard. Cookie expiry was the root cause masquerading as "no bookmarks." Source: [[raw/sessions/claude-code-2026-05-03-morning-briefing-wednesday-april-29-2026]]
- The TTS pipeline was literally reading emoji names aloud ("smiling face with heart eyes") — fixed by stripping emojis from TTS input and swapping the kid picker to Microsoft Fluent 3D PNGs. Source: [[raw/sessions/claude-code-2026-05-08-command-message-gstack-command-message]]
- The mic was opening before TTS finished, recording Luna's own voice and looping into self-conversation. Fixed by gating mic on audio drain, not on a fixed timer. Source: [[raw/sessions/claude-code-2026-05-08-command-message-gstack-command-message]]
- Killing the "Her World/His World" naming and using the child's actual name on the tile button measurably changed how Andres feels about the picker — small copy, big effect. Source: [[raw/sessions/claude-code-2026-05-06-phase-0-subtraction]]

## Abandoned approaches
- BrainView 6-tab buffet on the kid side — killed in Phase 0 subtraction, then partially restored when Brain Graph turned out to be load-bearing. Net: tabs gone, graph stays. Source: [[raw/sessions/claude-code-2026-05-06-phase-0-subtraction]]
- The dead `/synthesize` endpoint and weekly digest tiles — removed, no replacement, not missed. Source: [[raw/sessions/claude-code-2026-05-06-phase-0-subtraction]]
- Quests as a kid-side primitive — confirmed broken, dropped from the kid surface. Source: [[raw/sessions/claude-code-2026-05-06-phase-0-subtraction]]
- "Her World" / "His World" tile copy — replaced with the kid's first name. Source: [[raw/sessions/claude-code-2026-05-06-phase-0-subtraction]]
- "SOC 2 compliant" and "AI for business applications cert" lines in accelerator bios — Andres explicitly cut them as irrelevant. Source: [[raw/sessions/claude-code-2026-05-04-application-scoring-proposed-changes]]
- Pushing every Clio change to a PR before testing — switched to local LAN testing on iPhone first. Source: [[raw/sessions/claude-code-2026-05-08-command-message-gstack-command-message]]

## Recurring themes
- Clio voice + bilingual hardening (8+ sessions): two-voice flip, mic-on-too-early, emoji-read-aloud, Spanish-failed-twice, language tag to Grok TTS, kid-input language detection.
- Daily Brain automations running end-to-end (20+ sessions): morning briefing, plan-radar, editorial, signal-brief, Teams transcripts, email digest, KB ingestion, entity extraction — most one-shot, mostly green.
- Brain infrastructure self-repair (5 sessions): freshness sentinel, last-contact coverage, brain-lint consolidation, notify-on-failure CI sidecar, kb-health Sunday auto-fix.
- Clio gstack adoption (4 sessions): Tan-pattern specialists, parallel sprints, eval gating, CODEOWNERS, npm audit step, security headers.
- Accelerator + funding strategy (3 sessions): Speedrun/YC/Sputnik drafts, no-operating-agreement asset, Stripe-founders D5 eng plan.

## Unresolved questions
- Push Run 35 (Christy Mawdsley ingest) to `felipeu28 main`? Held per global rule, still pending Andres OK. Source: [[raw/sessions/claude-code-2026-05-05-check-for-any-new-files-in-raw-and-raw-onedrive-tr]]
- Spanish chat *behavior* (vs UI strings) — "failed twice" — root cause not yet isolated; needs Andres to specify which of the failure modes matched. Source: [[raw/sessions/claude-code-2026-05-06-phase-0-subtraction]]
- Wait for iPhone test before pushing the gstack-voice fixes? Asked, not answered. Source: [[raw/sessions/claude-code-2026-05-08-command-message-gstack-command-message]]
- D5 Stripe-founders plan exists at `~/.gstack/projects/Felipeu28-Clio/2026-05-08-d5-stripe-founders-eng-plan.md` but no execution sessions yet. Source: [[raw/sessions/claude-code-2026-05-09-command-message-autoplan-command-message]]
- iMessage ingestion pipeline shipped FDA-gated 2026-04-14 — has any iMessage actually been ingested since? No session this week shows it. Source: [[raw/sessions/claude-code-2026-04-14-brain-system-audit]]

---

*Generated by session-learnings.sh at 2026-05-12 12:18. Source: 65 sessions in last 7 days, 2 automation self-runs filtered.*

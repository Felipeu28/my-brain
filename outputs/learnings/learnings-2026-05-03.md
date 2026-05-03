---
type: session-learnings
week_ending: 2026-05-03
sessions_analyzed: 72
sessions_filtered: 11
tags:
  - graph/leaf
---

# Session Learnings — Week ending 2026-05-03

## Decisions made

- 2026-05-03 — Adopt Garry Tan's gstack pattern for Clio: Vitest over Jest, Biome over ESLint+Prettier, eval suites in Week 2 (not Week 4), gbrain read-only on `~/My Brain/`, read-write on `gbrain:clio:*`. Source: [[raw/sessions/claude-code-2026-05-03-week-1-execution]]
- 2026-05-03 — Quote `project:` field in claude-code session frontmatter to fix YAML breakage on slashes (`Brain/KB`). Source: [[raw/sessions/claude-code-2026-05-03-urgent-full-diagnosis-needed-the-deploy-quartz-sit]]
- 2026-05-03 — Move weekly operating-brief from Sunday 20:00 to Monday 08:00; ship freshness sentinel + Site CI status line in morning briefing; create six project hub pages (Moil + Clio + 4 clients). Source: [[raw/sessions/claude-code-2026-05-03-morning-briefing-wednesday-april-29-2026]]
- 2026-04-28 — Synthesize cross-session edges in Clio brain to bridge orphan topics; force JSON mode + response schema on Gemini edge synth after silent failures. Source: [[raw/sessions/claude-code-2026-04-28-i-want-you-to-analyze-this-graph-and-diagnose-all-]], [[raw/sessions/claude-code-2026-05-01-https-github-com-felipeu28-clio-compare-main-claud]]
- 2026-04-15 — Ship COPPA disclosure + parent-initiated data deletion; flip `AUTH_ENFORCE` default to strict + RLS + NOT NULL; add daily session caps per age tier; replace waitlist with direct sign-up. Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]
- 2026-05-01 — Persist Clio app view via URL routing (refresh on a page no longer dumps user back to profile picker). Source: [[raw/sessions/claude-code-2026-05-01-now-let-s-audit-why-anytime-i-am-on-a-opage-and-cl]]

## Things learned

- A 4-second deploy-job failure on GitHub Pages almost always means permissions/config (missing `pages: write` / `id-token: write`), not a code error. Source: [[raw/sessions/claude-code-2026-04-28-the-github-repo-felipeu28-my-brain-has-a-failing-g]]
- Gemini model IDs go stale and silently 404 — kids' conversations were being dropped on every cascade fail until dead IDs were purged from the extraction cascade. Source: [[raw/sessions/claude-code-2026-05-01-audit-findings-implementation-plan]]
- `ANTHROPIC_API_KEY` containing non-ASCII characters causes `fetch` to throw before any HTTP error surface; needs pre-flight detection. Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]
- Recommendations panel was silently truncating because Gemini `maxOutputTokens` was 1200; bumping to 4096 + truncation detection restored output. Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]
- iOS autoplay can be sidestepped by using Web Audio API as the primary playback substrate instead of `<audio>` element dance. Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]
- Brain wiki/ → quartz/content/wiki/ sync is the single most common cause of 404s; `sync_wiki.sh` must run before every commit and is now wired into all four automated commit scripts. Source: [[raw/sessions/claude-code-2026-04-30-brain-ingestion-health-2026-04-30]]
- Bookmark scraper had a silent zero-item failure mode that produced false "no bookmarks captured" alerts; added zero-item guard. Source: [[raw/sessions/claude-code-2026-04-27-andres-got-a-daily-signal-email-note-saying-no-boo]], [[raw/sessions/claude-code-2026-04-30-brain-ingestion-health-2026-04-30]]

## Abandoned approaches

- Cloudflare Pages migration for Brain KB — explored 2026-04-28 to replace failing GH Pages deploy; GH Pages was instead repaired (and broke again 2026-05-03). Source: [[raw/sessions/claude-code-2026-04-28-set-up-cloudflare-pages-to-deploy-the-private-gith]]
- ElevenLabs TTS — swapped to Grok; `elevenlabs.ts` renamed to `tts.ts`. Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]
- Permissive auth hotfix — restored kid access while env was debugged, then reverted to strict once root cause found. Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]
- `@luna-brain/shared` static imports in API routes — kept breaking serverless cold-starts; ripped out of `/auth/profiles`, `openers`, etc. Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]
- Robot-voice fallback when TTS failed — killed; orb=mic, no fallback. Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]
- Column-missing retry fallbacks in API handlers — dropped after migrations applied (dead code). Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]
- Silent mock fallback in chat handler — replaced with honest error + `/api/healthz` deep probe that actually calls `generateContent`. Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]

## Recurring themes

- Clio voice/UX regression chasing (8+ sessions): tap-to-stop, auto-restart mic per age tier, silence thresholds, landscape breakpoint, URL routing.
- Silent-failure debugging across LLM cascades (5 sessions): Gemini dead model IDs, edge synth without JSON mode, recommendations truncation, bookmark zero-item bug.
- Brain KB deployment instability (4 sessions): GH Pages 4-sec failures, Cloudflare Pages spike, sync_wiki gaps, Vercel deploy fail.
- Brain graph synthesis (3 sessions): Clio cross-session edge synth + Brain wiki graph corner pile-ups + zoom/pan UX.
- Operational observability buildout (3 sessions): freshness sentinel, project-activity rollup, Site CI status line in morning briefing.

## Unresolved questions

- Is the Gemini API key actually valid, or are all the failures driven by dead model IDs alone? Final 2026-05-01 direction was "smoke test the key." Source: [[raw/sessions/claude-code-2026-05-01-audit-findings-implementation-plan]]
- Whether to commit + push the 2026-05-01 weekly KB compile — paused per Andres's push rule, awaiting explicit OK. Source: [[raw/sessions/claude-code-2026-05-01-run-the-weekly-knowledge-base-compile-and-cleanup-]]
- GH Pages vs Cloudflare Pages as final Brain deploy target — GH Pages failed again 2026-05-03 9:04 after thought-to-be-fixed; Cloudflare Pages exploration is still on the table. Source: [[raw/sessions/claude-code-2026-05-03-urgent-full-diagnosis-needed-the-deploy-quartz-sit]]
- Clio device-side data capture (subjects watched, games played) — eng-review plan drafted 2026-04-27 but no implementation decision. Source: [[raw/sessions/claude-code-2026-04-27-command-message-plan-eng-review-command-message]]
- Branded Clio onboarding emails to invited families — Andres asked at end of Wave 1c session, no follow-through this week. Source: [[raw/sessions/claude-code-2026-04-15-wave-1c-strict-auth-cleanup]]

---

*Generated by session-learnings.sh at 2026-05-03 11:22. Source: 72 sessions in last 7 days, 11 automation self-runs filtered.*

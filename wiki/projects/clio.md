---
tags:
  - graph/hub
status: active
last_updated: 2026-05-03
---
# Clio

**Type:** startup
**Slug:** `clio`
**Last updated:** 2026-05-03
**Repo(s):** `~/luna-brain` (local) / [`Felipeu28/Lunabella`](https://github.com/Felipeu28/Lunabella) — public name unchanged after rename
**Founders / key team:** Andres Urrego (solo builder), Mariana Rodriguez (co-parent / product feedback), users: Annabella (7) + Evie (5)
**Domain:** clioremembers.com

---

## Status

Bilingual voice-first kids AI companion with persistent memory ("brain graph"), live in production on Next.js + Railway + Supabase. Phase 1 shipped (naming ceremony, voice in/out via xAI Grok TTS/STT, brain graph synthesis). Currently in a stability sprint — recent commits are bug fixes on edge synthesis, ingestion failures, and graph rendering. Predecessor: see [[wiki/projects/lunabella]] for full historical context (renamed from Luna Brain on 2026-04-16).

## Last 7 days

<!-- AUTO: bin/project-activity.sh updates this section daily. Do not edit by hand. -->
_Updated: 2026-05-03 11:02 (window: 2026-04-26 → 2026-05-03)_

**Commits (10):**
- 2026-05-03 docs: add Clio gstack adoption plan (#47)
- 2026-05-03 fix(web): persist app view via URL routing (#46)
- 2026-05-03 fix: 401s on gamification + openers, 500 on quests/generate (#45)
- 2026-05-01 fix(web): persist app view via URL routing (#44)
- 2026-05-01 fix: 401s on gamification + openers, 500 on quests/generate (#43)
- 2026-05-01 fix(brain): make graph edges actually visible (#42)
- 2026-05-01 feat(admin): one-shot edge backfill across every profile (#41)
- 2026-05-01 feat(admin): one-shot edge backfill across every profile (#40)
- 2026-05-01 fix(brain): purge dead Gemini IDs from edge synth + add response schema (#39)
- 2026-05-01 fix(brain): force JSON mode on edge synth + surface real failure reason (#38)

**Claude Code sessions (11):**
- 2026-04-15 — Wave 1c — strict auth + cleanup
- 2026-04-25 — Do a full regression audit of all voice and UI changes that have landed on main
- 2026-04-26 — Plan: Fix live issues + clean house
- 2026-04-27 — <command-message>plan-eng-review</command-message>
- 2026-04-27 — (you'll need apps/api running too — npm run dev from repo root)
- 2026-04-28 — I want you to analyze this graph and diagnose all the mising connections, and wh
- 2026-04-28 — Let's do a full security audit for Clio, including our full main repo!!
- 2026-05-01 — Audit findings + implementation plan
- 2026-05-01 — https://github.com/Felipeu28/Clio/compare/main...claude/gracious-nobel-356df5?ex
- 2026-05-01 — Let's create a new video about the parents side of clio, you can use browser, I
**Mentions in meetings + raw (2):**
- [[raw/teams-transcript-website-update-review-call-2026-04-28]]
- [[raw/weekly-sessions-2026-05-03]]

## Recent decisions

- 2026-05-01 — Made graph edges actually visible (#42); previous graph was rendering nodes without connecting lines. Source: `git log ~/luna-brain`
- 2026-05-01 — One-shot edge backfill across every profile (#40, #41) to recover orphan topics. Source: [[raw/sessions/claude-code-2026-05-01-audit-findings-implementation-plan]]
- 2026-04-30 — Forced JSON mode on edge synthesis + purged dead Gemini IDs (#38, #39); root cause: silent 4xx drops on kids' conversations.
- 2026-04-25 — P0 audio silence diagnosed; multi-issue urgent fix sprint kicked off. Source: [[raw/sessions/claude-code-2026-04-25-urgent-multi-issue-fix-for-clio-andres-says-voice-]]
- 2026-04-19 — Voice stack switched ElevenLabs + Web Speech → xAI Grok TTS/STT (cost/quality). Source: [[wiki/projects/lunabella]]

## Open questions

- When does Clio ship to first non-family users (Mariana's network? extended family?)?
- What's the parent-engagement loop — is the Sunday digest enough or does the dashboard need active hooks?
- xAI Grok TTS/STT cost model post-launch — real usage vs estimates.
- Curriculum intelligence (Phase 4) — which school's curriculum does Annabella pilot first?
- Is Clio a Moil-adjacent product or strictly personal? (Affects whether to invest in growth infra.)

## Connections

- [[wiki/projects/lunabella]]
- [[wiki/projects/moil]]
- [[wiki/concepts/brain-architecture]]
- [[wiki/concepts/llm-knowledge-bases]]
- [[wiki/people/mariana-rodriguez]]
- [[wiki/summaries/kidsgpt-planning-2026-04]]

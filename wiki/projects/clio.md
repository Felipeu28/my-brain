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
_Updated: 2026-05-05 08:00 (window: 2026-04-28 → 2026-05-05)_

**Commits (10):**
- 2026-05-05 fix(og): use www.clioremembers.com directly to avoid apex 307 redirect (#62)
- 2026-05-05 fix(og): render og.svg → og.png + absolute URLs in social card meta tags (#61)
- 2026-05-04 feat(week4): canary webhook + LLM eval gating + leetspeak safety + CLAUDE.md cleanup (#60)
- 2026-05-04 feat(agents): wire research-anchored 6-example corpus into clio-parent-comms (#59)
- 2026-05-03 chore: remove orphaned .claire/ typo dir from prior agent session (#56)
- 2026-05-03 chore: remove orphan .claire/ typo dir from prior agent session (#55)
- 2026-05-03 chore(gbrain): reset PGLite to schema v24, reimport, add policy-enforcing wrapper (#54)
- 2026-05-03 feat(workflow): parallel-sprint model + retro/brain-lint/canary infra (week 3) (#53)
- 2026-05-03 chore(gbrain): wire PGLite local + per-remote trust tiers (week 2.3) (#52)
- 2026-05-03 feat(specialists): 5 Clio-only agents + safety/voice/age-tier eval suites (#51)

**Claude Code sessions (43):**
- 2026-04-15 — <command-message>init</command-message>
- 2026-04-15 — <command-message>init</command-message>
- 2026-04-15 — Wave 1c — strict auth + cleanup
- 2026-04-16 — Clio — Full Implementation
- 2026-04-16 — Clio PR #8 gamification
- 2026-04-16 — <command-message>init</command-message>
- 2026-04-16 — <command-message>init</command-message>
- 2026-04-16 — Full audit synthesis
- 2026-04-16 — Open parent dashboard on desktop and mobile
- 2026-04-16 — Product research: gamification & differentiation
**Mentions in meetings + raw (6):**
- [[wiki/meetings/2026-05-04-christine-kat-coaching]]
- [[raw/teams-2026-04-24]]
- [[raw/teams-transcript-christine-andres-2026-05-04]]
- [[raw/teams-transcript-website-update-review-call-2026-04-28]]
- [[raw/weekly-sessions-2026-04-26]]
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

## Related

- [[wiki/projects/lunabella]]
- [[wiki/projects/moil]]
- [[wiki/concepts/brain-architecture]]
- [[wiki/concepts/llm-knowledge-bases]]
- [[wiki/people/mariana-rodriguez]]
- [[wiki/summaries/kidsgpt-planning-2026-04]]

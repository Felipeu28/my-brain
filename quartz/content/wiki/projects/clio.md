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
_Updated: 2026-05-19 08:00 (window: 2026-05-12 → 2026-05-19)_

**Claude Code sessions (10):**
- 2026-05-01 — Let's create a new video about the parents side of clio, you can use browser, I
- 2026-05-03 — Week 1 execution
- 2026-05-06 — Phase 0 — Subtraction
- 2026-05-09 — Ship Phase 1 + start Phase 2–5
- 2026-05-11 — <scheduled-task name="clio-weekly-security-audit" file="/Users/jarvisurrego/.cla
- 2026-05-12 — Security Review
- 2026-05-13 — Implementation plan — remaining items from family testing
- 2026-05-15 — let's start a full audit of the quality of data we are ingesting and if its any
- 2026-05-17 — Bilingual Claim Audit & Implementation Plan
- 2026-05-17 — Help me find the document I got from the first office hours with gstack
**Mentions in meetings + raw (3):**
- [[wiki/meetings/2026-05-13-jordan-andres-1-1]]
- [[raw/teams-transcript-jordan-andres-1-1-2026-05-13]]
- [[raw/weekly-sessions-2026-05-17]]

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

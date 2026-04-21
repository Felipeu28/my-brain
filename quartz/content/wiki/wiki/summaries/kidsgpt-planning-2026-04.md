---
tags:
  - graph/leaf
---
# Summary — KidsGPT / Luna Brain Planning Docs (April 2026)

**Type:** summary
**Last updated:** 2026-04-17
**Source files:** [[raw/KidsGPT/README]], [[raw/KidsGPT/options-analysis]], [[raw/KidsGPT/implementation-plan]]
**Primary page:** [[wiki/projects/lunabella]]

---

## What these sources are

Three planning documents (not implementation code) that together specify **Luna Brain** — the personal-AI-for-Andres's-daughters project now shipping under `Felipeu28/Lunabella`. Dated April 2026; the decisions block in `implementation-plan.md` locks the architecture.

| File | Size | Purpose |
|------|------|---------|
| `README.md` | 1.4 KB | One-pager: what Luna is, stack summary, 🟡 Planning-complete marker |
| `options-analysis.md` | 6.8 KB | Five architecture options ranked — Option 2 (voice AI character) + Option 1 (brain-building backend) selected |
| `implementation-plan.md` | 23 KB | Phased build plan (Weeks 1–7+), Supabase schema, system prompts (Luna v1 + ingestion extractor + curriculum injection), cost model |

## Key decisions locked

- **One app, two profiles** — Annabella (age 7) and Evie (age 5), each names her own Luna, separate brains, per-profile curriculum
- **iPad-first portrait** — large touch targets, voice input (Web Speech API), voice output (ElevenLabs)
- **Bilingual** — Luna auto-detects EN/ES and code-switches naturally; parent "practice Spanish" mode can override
- **Stack** — React/Vite (Vercel) + Fastify (Railway) + Supabase (PG + Auth + Storage) + Claude `claude-sonnet-4-6` + ElevenLabs + ntfy.sh + Resend
- **Safety model** — Claude (not GPT) for Minimal-Risk kid rating; hard-block list of topics routes to "ask your parents" + logs to `parent_flags`; push to Andres within 60s
- **Ingestion cadence** — end-of-conversation (5 min idle or "Bye Luna" tap), not per-message, not weekly

## Five options considered (options-analysis.md)

1. **Custom Claude API + Knowledge Graph** ("Tee R's Brain — built like Dad's") — 2-3 weeks, Claude API only
2. **Voice-first AI Friend with character** ("Luna") — 3-4 weeks, Claude + ElevenLabs (~$5/mo) — **SELECTED**
3. **Socratic Tutor mode** (Khanmigo-style) — 1-2 weeks, Claude only
4. **Parent + Kid dual interface** — 3-5 weeks, Claude + server
5. **Pure Quartz Brain** (no AI chat, just growing wiki) — 1 week, free

**Final combination:** Option 2 (voice + character) + Option 1's brain-building backend.

Note: `options-analysis.md` predates `implementation-plan.md` and references a single placeholder child "Tee R, age 7–10"; the implementation plan corrects this to the real two-daughter design (Annabella 7 + Evie 5) with individual profiles.

## Phase roadmap (implementation-plan.md)

| Phase | Weeks | Deliverable |
|-------|-------|-------------|
| 1 — Luna is alive | 1–2 | Naming ceremony, text chat, voice I/O, safety layer |
| 2 — Brain wakes up | 3 | Ingestion pipeline, Her World graph, bilingual node dedup |
| 3 — Andres has eyes | 4 | Parent dashboard, ntfy push, Sunday digest email |
| 4 — Curriculum intelligence | 5–6 | Upload school curriculum → Luna gets school-aware |
| 5 — Magic layer | 7+ | Luna's monthly letter, Brain Book PDF export, memory of past conversations |

## Prompts captured

- **Luna v1 system prompt** (bilingual + Socratic + safety + 2-4 sentence cap) — in implementation-plan.md Phase 1
- **Ingestion extraction prompt** (JSON: topics, questions, facts_learned, interests, flag_for_parent, luna_note) — Phase 2
- **Curriculum injection template** (confidential reference block, never revealed to child) — Phase 4

## Cost model

~$15–20/month total. Claude API $5–10, ElevenLabs Starter $5, Railway $5. Supabase / Vercel / Resend / ntfy.sh on free tiers.

## Relationship to other pages

- **Primary project page:** [[wiki/projects/lunabella]]
- **Parallel architecture:** [[wiki/concepts/brain-architecture]] (same two-layer memory pattern, child-scale)
- **Framework lineage:** [[wiki/concepts/llm-knowledge-bases]] (Karpathy personal-KB pattern)
- **Not related to** `Felipeu28/magical-reading-adventures` — that's a separate HTML repo; the open question on [[wiki/projects/magical-reading-adventures]] can be closed

# Luna Brain — Annabella's Personal AI Friend

**Project:** A bilingual, voice-first AI companion for Annabella (age 7) — and eventually Evie (age 5)
**Goal:** A safe, Socratic AI she names herself, that builds her personal "brain" one conversation at a time
**Started:** April 2026

## What We're Building
- Luna — a bilingual (English + Spanish) AI character Annabella names and customizes on first launch
- Voice-first, iPad-optimized: she speaks, Luna speaks back
- Socratic teaching: Luna asks "What do YOU think?" before answering
- Builds a visual knowledge graph ("Her World") she can see growing over time
- Parent dashboard for Andres: weekly digests, sensitive-topic notifications, full visibility

## Deployment Stack
- **Frontend:** React + Vite → Vercel
- **API:** Fastify → Railway
- **Database:** Supabase (PostgreSQL + Auth + Storage)
- **AI:** Claude API (claude-sonnet-4-6)
- **Voice:** ElevenLabs (Annabella picks her voice on first launch)

## Project Files
- `options-analysis.md` — 5 approaches analyzed (for reference)
- `implementation-plan.md` — Full build plan with phases, data model, stack details
- `design/` — UI concepts and character design (iPad-first)
- `prompts/` — System prompts and safety rules (bilingual)

## Status
🟡 Planning phase complete — ready to build Phase 1

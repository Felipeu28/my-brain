---
github_repo: Felipeu28/Lunabella
status: active
last_push: 2026-04-19
stage: phase-1-building
domain: clioremembers.com
tags:
  - graph/spoke
  - project/personal
---
# Clio — Kids AI Companion (formerly Luna Brain)

**Type:** personal project (family)
**Last updated:** 2026-04-21
**Source:** [[raw/KidsGPT/README]], [[raw/KidsGPT/implementation-plan]], [[raw/KidsGPT/options-analysis]] + `Felipeu28/Lunabella` repo + manually saved 2026-04-21
**Related:** [[wiki/projects/README]], [[wiki/concepts/brain-architecture]], [[wiki/concepts/llm-knowledge-bases]], [[wiki/people/mariana-rodriguez]]

---

## Summary

Bilingual, voice-first AI companion for Andres's daughters **Annabella (age 7)** and **Evie (age 5)**. One app, two profiles — the AI knows each child specifically and memory is the core differentiator. Lives at **clioremembers.com**. Deployed to production (Next.js + Railway backend + Vercel frontend).

**Renamed:** Luna Brain → **Clio** on Apr 16 2026 (named after Clio, goddess of history and memory). **Repo:** `Felipeu28/Lunabella` (name unchanged). **Status as of Apr 21 2026:** Phase 1 in production; voice stack migrated to xAI Grok TTS/STT.

## What's been shipped (Apr 2026)

| Date | Event |
|------|-------|
| Apr 15 | YC-style `/office-hours` session run on Clio product positioning |
| Apr 16 | Renamed Luna Brain → **Clio**. Full implementation plan written. Gamification/engagement deep research complete |
| Apr 17 | Full product analysis vs. *"The First AI That Knows a Specific Human"* design spec — high alignment confirmed |
| Apr 18 | Safari-specific infinite reload bug fixed and merged to `main` |
| Apr 19 | Complete voice/chat UX audit + redesign plan written. Voice stack migrated from ElevenLabs TTS + Web Speech API STT → **xAI Grok TTS/STT** (cost/quality decision) |

## What's being built

- **Kid view (Clio Chat):** iPad-portrait, animated Clio avatar, voice in + voice out (xAI Grok TTS/STT as of Apr 19), text bubbles, language toggle pill (🇺🇸 / 🇨🇴)
- **Her World (brain graph):** D3 force-directed graph, topic nodes colored by category (space, animals, school, family, art, science), bilingual labels, tap-to-explore
- **Parent dashboard (Andres):** PIN-locked (Supabase Auth), weekly topic counts, flagged-sensitive-question log, "Family Rules" editor, practice-language toggle, Sunday digest email, ntfy.sh push notifications on flag

## Naming ceremony (first launch)

Every new profile starts blank — a glowing orb appears and says *"I don't have a name yet. What should you call me?"* The child names it, picks 1 of 3 ElevenLabs voices, picks a color, then Luna asks the first question: *"So… what are you curious about today?"* That's also where the language is locked in (or left auto-detect).

## Architecture

```
Next.js (Vercel) → Railway backend → Supabase (PG + Auth + Storage)
                                  → Claude API (claude-sonnet-4-6)
                                  → xAI Grok TTS/STT  ← switched Apr 19 (was ElevenLabs + Web Speech API)
                                  → ntfy.sh (flag push)
                                  → Resend (Sunday digest email)
```

**Ingestion is end-of-conversation, not per-message.** 5 min of inactivity (or Annabella taps "Bye Luna!") fires an async job: full transcript → Claude structured extraction → Supabase brain nodes/edges/questions tables + markdown vault in Supabase Storage → Her World graph gains a new glowing node.

## Safety model

- Claude (Minimal Risk rating for kids per the options analysis) is the chat model — not GPT
- Hard-block topics: death, violence, scary news, adult, relationships, social media, other AI tools, politics, religion → *"That's a big question — I think your papi/mami would be the best one to talk about that with you. Want to ask them together?"* + logged to `parent_flags` table
- Sensitive flag triggers ntfy.sh push to Andres's phone within 60s
- System prompt caps Luna's reply length at 2–4 sentences and enforces Socratic method ("What do YOU think?" before answering)

## Bilingual design

Luna auto-detects the language of each message and responds in kind. Natural code-switching ("That's so cool — ¡qué chévere!"). Parent-dashboard "practice Spanish" mode can override — Luna gently redirects to Spanish even when asked in English. Brain vault nodes carry both `label_en` + `label_es`, so "espacio" and "space" collapse to the same node.

## Curriculum intelligence (Phase 4 — Week 5–6)

Andres uploads the school curriculum (PDF / photo / text) once per school year per profile. Claude parses it to structured JSON (subjects → units → monthly schedule). The active curriculum is injected into Luna's system prompt as a confidential reference — Luna recognizes school-topic overlaps in conversation, leans into them naturally, never reveals it has the document. Parent dashboard gains a **coverage map** (which curriculum topics has she organically explored this month) and **gap suggestions** (*"Try asking Luna about multiplication — Annabella hasn't touched it yet"*).

## Build order

| Week | Milestone | What changes |
|------|-----------|--------------|
| 1 | Naming ceremony + Luna text chat | Both girls name their Lunas, start chatting |
| 2 | Voice in + voice out | Speak to Luna, hear her answer in EN or ES |
| 3 | Brain wakes up | Her World grows after every conversation |
| 4 | Andres has eyes | Parent dashboard, notifications, weekly digest |
| 5–6 | Curriculum intelligence | Upload school curriculum → Luna gets school-aware |
| 7+ | Magic layer | Luna's monthly letters, Brain Book PDF, year-end curriculum report |

## Cost estimate

| Item | Monthly |
|------|---------|
| Claude API (~60 convos × 25 msgs + ingestion) | $5–10 |
| xAI Grok TTS/STT (replaced ElevenLabs Apr 19) | TBD |
| Railway (backend host) | $5 |
| Supabase / Vercel / Resend / ntfy.sh (free tiers) | $0 |
| **Total** | **~$10–15/mo (est.)** |

## Moil Relevance

Separate product — personal project, not a Moil client deliverable. Potential future demo case for AI memory + personalization pattern. Moil builds voice-first products; Clio is Andres's own production proof-of-concept for child-scale Socratic AI + personal knowledge graph.

## Supabase schema (Phase 2)

Core tables: `sessions` (UUID + transcript JSONB + language + curiosity_level), `brain_nodes` (slug + `label_en` + `label_es` + category + mention_count), `brain_edges` (source → target + weight), `questions` (per-session + topic_id), `parent_flags` (reason + context + Luna's response + reviewed flag). Phase 4 adds `curricula` (per profile per school year) and three columns on `brain_nodes` (`in_curriculum`, `curriculum_unit`, `curriculum_subject`).

## Why this fits Andres (per options-analysis)

- Already has Claude API access, a working Brain architecture, and Claude Code to build it
- Mental model is identical to his own Brain — easier to reason about
- Moil builds voice-first products — a 7-year-old who can't type fast is the perfect voice-first user
- The "brain as a gift" framing: in 5 years each girl will have a living visual record of how her mind grew from age 7 (Annabella) / age 5 (Evie) onward

## Open questions / next unblocks

- xAI Grok TTS/STT cost model — need real usage numbers post-launch
- Voice/chat UX redesign plan from Apr 19 audit — implementation status unknown
- Device provisioning — which iPad is this running on
- Mariana involvement — parent dashboard is solo-Andres today; should it be dual-parent?

~~Domain choice~~ → resolved: `clioremembers.com`
~~ElevenLabs API key~~ → resolved: switched to xAI Grok Apr 19
~~Supabase project~~ → resolved: deployed to production

## Connections

- [[wiki/projects/README]] — personal projects index
- [[wiki/concepts/brain-architecture]] — Clio mirrors the Moil Brain's two-layer memory (episodic convo → semantic knowledge graph)
- [[wiki/concepts/llm-knowledge-bases]] — Karpathy-style personal KB pattern, child-scale variant
- [[wiki/projects/magical-reading-adventures]] — earlier `Felipeu28/magical-reading-adventures` HTML repo; separate, not the engineering surface for this project
- [[wiki/people/mariana-rodriguez]] — mother to Annabella + Evie, co-parent
- [[wiki/summaries/kidsgpt-planning-2026-04]] — structured summary of the three raw planning docs (pre-rename, pre-Grok)

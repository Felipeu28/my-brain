---
name: radar index
description: Running changelogs for things Andres wants to track over time
type: index
tags:
  - graph/leaf
---

# Radar — Running Changelogs

**Purpose:** Append-only logs of fast-moving topics. Unlike concept pages (which explain *what* something is) radar logs answer *what's new* without forcing you to reread old bookmark files.

## Current logs

### Hiring & Labor
- [[wiki/radar/ai-hiring-trends]] — AI in recruiting: tools, EEOC guidance, bias audit regulation
- [[wiki/radar/voice-ux-patterns]] — Voice-first UX: design patterns, accessibility, adoption data
- [[wiki/radar/gig-worker-regulation]] — AB5, DOL contractor rule, Texas landscape
- [[wiki/radar/workforce-retention]] — Blue-collar retention research, sector benchmarks
- [[wiki/radar/competitor-moves]] — Indeed, ZipRecruiter, Wonolo, Instawork, Workstream moves (2025–2026)

### Market & Demographics
- [[wiki/radar/latam-job-market]] — US Hispanic workforce trends, informal job market dynamics
- [[wiki/radar/bilingual-ai]] — Spanish-English NLP quality, code-switching gaps, Moil's needs

### Business Model & Fintech
- [[wiki/radar/embedded-finance-smb]] — Embedded payroll/earned wage access for SMBs: players + opportunity

### AI / Tech
- [[wiki/radar/claude-code-changelog]] — Claude Code features, launches, ecosystem shifts

## When to add a new radar file
Create one when a topic has:
1. A concept page explaining "what it is"
2. Enough fast-moving updates that rereading old summaries to catch up is painful
3. A source (weekly bookmarks, newsletter, keynote cycle) that reliably produces new entries

## Candidates (not yet created)
- `ai-video-changelog.md` — Seedance, HeyGen, Veo, Grok Imagine, Higgsfield cadence
- `openclaw-hermes-changelog.md` — gstack / Superpowers / Compound Engineering releases
- `model-releases.md` — new model launches (Gemma, Qwen, Claude, GPT, Gemini)

## Format rules
- Newest on top, grouped by month
- Each entry = **date · feature name** + 1-line summary + source
- Use `- Source:` lines with X handles and wikilinks
- Promote load-bearing entries to proper concept pages and backlink

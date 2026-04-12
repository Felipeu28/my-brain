---
title: "Tech Stack"
tags: [moil, evergreen]
date: 2026-04-11
---

# Moil — Tech Stack

**Type:** moil-topic
**Last updated:** 2026-04-11
**Source:** [[raw/moil-documents-2026-04-09]], GitHub org scan (Moil-Code, Moil-Landingpages)
**Related:** [[moil/index]], [[moil/product-vision]], [[moil/metrics]]

---

## Overview

Moil is built as a modern SaaS platform. The OpenClaw internal dashboard (Andres's agent infrastructure) is built separately from the customer-facing Moil product, though they share the Supabase backend and Next.js stack.

---

## Customer-Facing Product

| Layer | Technology | Notes |
|-------|-----------|-------|
| Frontend | Next.js 14.1, React 18, Tailwind CSS | App Router pattern, SSR/SSG |
| Backend / DB | Supabase (PostgreSQL + Auth) | Supabase anon key + admin client |
| Hosting | Vercel | GitHub Actions CI/CD |
| Authentication | Supabase Auth + @supabase/auth-helpers-nextjs | |
| UI Components | Recharts, Lucide React | Charts + icon library |
| AI — Candidate Matching | Proprietary AI scoring model | 95% accuracy claimed |
| AI — Content Generation | LLM APIs (Anthropic / OpenAI) | Used for Content360, coaching, research |
| AI — Image Generation | Integrated (30/mo on Starter) | Custom topic-specific images |
| AI — Video Generation | Integrated (5 days/mo on Market Pro) | AI video for highest-impact content days |
| AI — Voice Input | Voice-to-text, EN/ES | 21-question onboarding by voice |
| Job Board Distribution | Custom integration layer | Posts to 10+ platforms simultaneously (Indeed, ZipRecruiter, Austin Jobs, Spanish Facebook Groups, etc.) |
| Language | TypeScript / JavaScript | Full-stack |
| Compliance | SOC 2 | Bank-level encryption, data never shared with third parties |

---

## Internal Operations (OpenClaw / Jarvis)

Andres runs an internal AI agent infrastructure that manages Moil's operations:

| Layer | Technology | Notes |
|-------|-----------|-------|
| Dashboard | Next.js 14.1 + React 18 + Supabase + Tailwind | Departments: analytics, sales, marketing, ops, growth, executive |
| Agent Runtime | OpenClaw (Pi-based) + Claude Code | Telegram-first, session-managed |
| Browser Automation | Playwright + Express + PostgreSQL | Browser-agent in workspace |
| Local Inference | LM Studio → Gemma 4 26B-A4B on Mac Mini M4 | OpenAI-compatible API at localhost:1234 |
| Memory | Mem0 + ChromaDB | Episodic memory for meetings, contacts, decisions |
| Analytics | Supabase + Recharts | Internal growth command center |

---

## GitHub Orgs

| Org | Repos | Purpose |
|-----|-------|---------|
| [Moil-Code](https://github.com/Moil-Code) | 24 repos | Core product — backend, employer app, candidate app, business plan tool |
| [Moil-Landingpages](https://github.com/Moil-Landingpages) | 9 repos | Client landing pages, Inna CRM, partner apps |
| [@felipeu28](https://github.com/felipeu28) | Personal | Andres personal repos |
| [@JarvisUrregoTX](https://github.com/JarvisUrregoTX) | AI/agents | Jarvis automation repos |

**Active P1 Repos (Moil-Code):**

| Repo | What it is |
|------|-----------|
| `Moil-codeProdbackend` | Production backend |
| `Moil-codeEmployer-beta` | Employer app |
| `Business-plan-beta-prod` | Business plan creator |
| `Moil-landing-page` | Main landing page (moilapp.com) |
| `partner-production` | Partner portal live |

---

## Integrations

| Integration | Type | Used For |
|------------|------|----------|
| Indeed | Job board API | Candidate distribution |
| ZipRecruiter | Job board API | Candidate distribution |
| Facebook Groups | Social API | Bilingual candidate reach |
| Austin Jobs | Regional board | Local candidate distribution |
| Microsoft Teams | 🔲 Pending — Graph API | Gather business data from employer Teams workspaces to enrich Business DNA |
| Apollo.io | CRM enrichment | Lead prospecting and enrichment (via MCP in Brain) |
| Supabase | BaaS | Auth, database, storage |
| Vercel | Deployment | Hosting + CI/CD |
| AWS Startups | Cloud credits + listing | Infrastructure and credibility |

---

## Infrastructure

- **AWS Startups** — listed, presumably receiving credits/support
- **Vercel** — front-end deployment with GitHub Actions CI/CD
- **Supabase** — managed PostgreSQL, auth, storage
- **SOC 2 compliant** — security posture required for B2G and enterprise deals

---

## AI Stack Philosophy

Moil uses LLM APIs (primarily Anthropic/OpenAI) for content generation, research synthesis, and coaching — not local inference. The Brain (Andres's personal infrastructure) runs local Gemma 4 on the Mac Mini M4 for privacy, but the customer-facing product calls cloud APIs.

Key AI capabilities:
- **Business DNA extraction** — structured extraction from 21-question voice/text intake
- **Market research synthesis** — pulls from 8–10 real sources, generates 20–30 page reports
- **Content360 generation** — 30 days of posts with hooks, captions, CTAs, hashtags by content type
- **Candidate scoring** — AI match at 95% accuracy across skills, location, experience, language
- **24/7 coaching** — context-aware strategy and decision support using persisted business DNA

---

## Connections

- [[moil/product-vision]] — What the stack is built to deliver
- [[moil/index]] — Moil hub with active repo list
- [[concepts/managed-agents]] — Claude Code and agent infrastructure Andres uses to build Moil
- [[concepts/claude-code]] — Claude Code runtime used in internal dev

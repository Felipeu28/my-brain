---
tags:
  - graph/hub
---

# Moil — Brain Product Strategy

**Type:** moil-topic  
**Last updated:** 2026-04-21  
**Source:** [[outputs/smb-business-research-2026-04-21]], [[wiki/moil/positioning]], [[wiki/moil/gtm]], [[wiki/moil/product-roadmap]], [[wiki/concepts/brain-architecture]]  
**Related:** [[wiki/moil/icp]], [[wiki/moil/competitors]], [[wiki/concepts/llm-knowledge-bases]], [[wiki/concepts/buda-hive]]

---

## Summary

Productizing Andres's personal Moil Brain (second-brain knowledge base) into an SMB feature tier. The Brain is a fully-functional operating system (249 wiki pages, 10 automated jobs, daily/weekly/monthly outputs) that ingests email, Teams, calendar, transcripts, GitHub, and X; produces daily briefings, weekly pulses, and searchable company memory.

**Strategic decision:** Launch as **Moil Brain embedded feature** (not standalone) for $99–$249/mo, vertical-wedged to agencies and professional services. Leverage Moil's existing 500-customer distribution and HIVE cohort program. Target 100 paying SMBs by Q4 2026; $100K+ MRR by Q2 2027.

---

## The Opportunity

**Market pain:** SMB leaders lose 7.5 hours/week switching between email, Teams, Slack, CRM, and calendar (Intuit Jan 2026). 14% of SMBs that use AI have fully integrated it into operations; top blockers are privacy (50%), expertise (49%), tool choice (48%) (Goldman Sachs 10KSB).

**Market gap:** Knowledge-base tools cluster at $8–$25/seat (Notion, Guru, Tettra), but no incumbent owns the $99–$249/mo flat-rate tier for SMB teams needing auto-capture + synthesis. Glean (enterprise search) starts at $50K/yr minimum. Mem.ai (personal second brain) failed — "no network effects for individual" per Medium analysis.

**Defensible position:** A system that auto-captures context from email + Teams + calendar + CRM + transcripts and surfaces daily briefings + weekly pulse + searchable company memory, without requiring manual migration or writing. Vertical concentration (agencies first, then professional services, then trades) creates durable wedge.

---

## Strategic Recommendation

**Embedded vs. standalone:** Build as Moil feature, not separate product.

| Decision | Rationale |
|----------|-----------|
| **Embed in Moil** | Reuses 500-customer GTM; CAC = $0 (existing relationship). HIVE cohort (Cohort 4 launched Apr 20) is perfect alpha/beta. Separate product would duplicate GTM costs; splitting founder focus kills both. |
| **Vertical first** | Win agencies + professional services (transcript-heavy, hiring + project management + client context pain). Service SMBs second. Enterprise never. |
| **Privacy positioning** | "Your data. Your infrastructure. We never train on your emails." Directly counters April 2026 Breitbart narrative: "companies selling worker messages as training data." |
| **Simple outputs** | Daily briefing (email-delivered) + weekly pulse (email-delivered) + searchable wiki. No "log in to another tool" friction. |

---

## Product Positioning

**One-liner:** The AI memory layer every SMB team deserves — auto-capture context from email, meetings, and teams; deliver daily briefings, weekly insights, and searchable company memory.

**Why it wins:**
- **vs. Notion:** Auto-captures; truth-ranked results; built-in briefing output; SMB pricing
- **vs. Glean:** 100x cheaper; vertical-first; privacy-first; instant value on day 1
- **vs. ChatGPT:** Persistent context (remembers last month); team-aware; action-oriented
- **vs. status quo:** Removes the 7.5 hrs/week tool-switching tax

---

## MVP & Pricing

### Build Scope (16-week sprint)

**Must-haves:**
- Gmail + Outlook OAuth (read email, extract actions)
- Google Calendar + Microsoft Graph sync
- Zoom/Teams/Meet transcript drop zone
- HubSpot/Pipedrive customer 360 sync
- Daily morning briefing (email-sent)
- Weekly pulse (business snapshot)
- Searchable Quartz wiki (Moil branded)
- Chat interface: "What's latest on [customer]?"
- Setup UX: OAuth-only, 10–15 min onboarding

**Out of scope (post-launch):**
- Mobile app, Slack bot, custom fine-tuning, on-premise

### Pricing Tiers

| Plan | Price | Seats | Transcripts/mo | Ideal for |
|------|-------|-------|---|---|
| Professional | +$50/mo | 5 | 50 | Small teams (contractors, consultants, agencies under 5) |
| Brain Studio | +$150/mo | 15 | 200 | Growing agencies, professional services firms |
| **Moil Complete** (bundle) | $199/mo | 10 | Unlimited | SMBs using full Moil stack (hiring + Moil360 + Brain) |
| **Brain Solo** (standalone) | $99/mo | 3 | 100 | Non-Moil SMBs wanting memory layer only |

**ACV projection:** Existing Moil customer upgrade to Professional tier = +$600/year at $0 CAC. Standalone SMBs via EDC = $99–$150/mo. Blended target: 100 paying by Q4 2026.

---

## Go-to-Market

### Timeline

| Phase | Window | Target | Metric |
|-------|--------|--------|--------|
| **Alpha** | May–June 2026 | 10 existing Moil customers + internal dogfooding | Onboarding < 15 min; retention > 60% week 1 |
| **Beta** | July–Aug 2026 | HIVE Cohort 4 (15–20 companies); curriculum integration | Cohort adoption ≥ 80%; feedback on integrations |
| **Public launch** | Sept–Oct 2026 | 50+ SMBs via Product Hunt + warm outreach; 2 EDC pilots | 100 paying by Q4; CAC < $300 |

### Channels

- **Word of mouth:** HIVE cohort grads → local business networks → other EDCs
- **Founder brand:** Andres's LinkedIn/X (AIbyAndres) + Brain origin story (eating our own dogfood)
- **Vertical partnership:** EDC model (sell 25-seat license to San Antonio EDC, Austin Chamber, etc., same as Moil motion)
- **Content:** "What's in your company memory?" case studies (customer wins)

### Customer Selection (Alpha/Beta)

**Alpha candidates (existing Moil):**
- Siren Beauty (website design agency — high transcript volume)
- Alloy (gym; content operations + staff context)
- Connectex (SMB consultant; needs deal memory)
- Titan Tech Authority (systems integrator; client 360)
- Meridian (event platform; attendee/sponsor context)

**Beta candidates (HIVE Cohort 4):**
- All 15–20 participants (launched Apr 20; Joshua Edmond + Buda EDC curriculum collab active)
- Free Brain access in exchange for weekly feedback + testimonial

---

## Technical Rewrite Path

| Component | Current | Target | Weeks |
|-----------|---------|--------|-------|
| Scheduling | macOS launchd | Docker + Fly.io cron | 4 |
| Authentication | Git SSH | Clerk OAuth | 3 |
| Platform paths | Hardcoded `/Users/...` | Multi-tenant $HOME logic | 2 |
| LLM calls | `claude` CLI | Anthropic API (Haiku for cost) | 2 |
| Email ingestion | Outlook CLI | Gmail + Outlook OAuth | 4 |
| Wiki hosting | GitHub Pages | Vercel (authenticated) | 3 |
| Billing | Manual | Stripe metering | 2 |
| Database | Git-tracked markdown | PostgreSQL + daily export | 4 |

**Total critical path:** 16 weeks (parallel tracks).  
**Cost estimate:** 1 FTE engineer + infra = ~$98K; +30% buffer = **$127K**.

---

## Success Metrics (OKRs)

**Q3 2026:**
- Onboarding time ≤ 15 min (80% single-session completion)
- Week 1 retention ≥ 60%
- HIVE Cohort 4 adoption ≥ 80%
- Cost per transcript < $0.05

**Q4 2026:**
- 100 paying SMBs on Brain tier
- 2 EDC partnerships signed
- NPS ≥ 40
- Churn < 5%/month

**2027:**
- $50K MRR Brain revenue
- 500 active users
- 2nd vertical validated (legal, accounting, or agency subtype)

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| **Founder context split** | Hire dedicated Brain PM by week 8; Andres dogfood + strategy only |
| **Token cost spiral** | Use Haiku + aggressive caching; hard cost cap per transcript |
| **EU AI Act (Aug 2, 2026)** | Budget $30–50K legal + $15K SOC 2 audit; public launch Oct 2026 (post-transition) |
| **Vertical concentration fails** | Pre-commit to agencies first; don't try Notion-for-everyone |
| **Integration fragility** | Build health dashboard; 2-week SLA for API breaks |

---

## Connections

- [[wiki/concepts/brain-architecture]] — the 5-layer personal knowledge pipeline that Brain implements
- [[wiki/moil/gtm]] — existing Moil GTM motion (community-led + PLG)
- [[wiki/concepts/buda-hive]] — HIVE cohort (alpha/beta venue)
- [[outputs/smb-business-research-2026-04-21]] — full market analysis & research (sources, competitive landscape, pricing benchmarks, regulatory considerations)
- [[wiki/moil/positioning]] — Moil positioning (reference for Brain positioning)
- [[wiki/moil/product-roadmap]] — Moil product stack & roadmap (Brain integrates as new tier)

---

## Last Reviewed

- Date: 2026-04-21
- By: Claude (strategy synthesis + market research)
- Next review: 2026-06-15 (post-alpha feasibility review)
- Decision gate: Recommend to Moil team by 2026-05-01

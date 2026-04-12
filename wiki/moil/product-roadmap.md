# Moil — Product Roadmap & Feature Status

**Type:** moil-topic
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/]] (25 meeting transcripts, Aug 2024–May 2025), [[raw/teams-2026-04-12]] (Apr 2026 engineering sprint)
**Related:** [[wiki/moil/positioning]], [[wiki/moil/gtm]], [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]]

---

## AI Tech Stack (updated Apr 2026)

| Function | Primary AI | Backup | Notes |
|---|---|---|---|
| Resume data extraction | Gemini | OpenAI | — |
| Resume generation | DeepSeek | — | — |
| Business plan generation | OpenAI Agent (custom) | — | `gpt-4o` alias silently upgraded to `gpt-5_4-2026-03-05` — cost spike |
| Business insights (market analysis) | o4-mini | — | — |
| Business plan sections (detailed) | o3-mini | — | — |
| AI image generation (marketing) | Gemini | Grok | Gemini "so much better" for images (Apr 8 2026) |
| Content360 fast generation | Qwen Turbo 3.5 | Gemini / xAI | Free tier exhausted Apr 10; moved to paid |
| Internal code generation | Fine-tuned DeepSeek R1 | — | — |
| Business Coach chat | Qwen | Gemini / Grok | Speed is critical; evaluating Grok 4.1 Fast ($0.20/$0.50, 2M context) |
| Development workflow | Claude Code | — | Andres uses Claude Code for all feature prototyping (12+ sessions/week) |

**Apr 2026 cost discovery:** The `gpt-4o` model alias was silently updated by OpenAI to the `gpt-5_4-2026-03-05` snapshot, causing unexpected billing increases. Grok 4.1 Fast identified as 30x cheaper alternative on output tokens. DeepSeek still used in business plan flow.

---

## Feature Status (updated Apr 2026)

| Feature | Status | Notes |
|---|---|---|
| Resume Builder | ✅ Complete | 100% built on customer feedback |
| Job Matching Algorithm | ✅ Improved | Weighted: recent experience → preference → skills |
| Business Plan Creator | ✅ Complete | OpenAI agent; PDF + PPT export added Apr 11 2026 |
| Business Coach | ✅ Live | AI-guided onboarding: scrapes websites/PDFs/plans, feedback after every question |
| Content360 / Moil 360 | ✅ Live (selling) | Monthly content creation tool; image gen via Gemini; strategy + document creation |
| Business Insights | 🔧 In progress | o4-mini + o3-mini pipeline; several bugs being fixed |
| Voice Guide | ✅ Working | "Talks to you and then takes action for you" — Andres excited about it |
| AI Interview Tool | 🔧 In design/dev | MVP approach; voice-only initially |
| Meridian (event platform) | 🔧 Active dev | Taiwo building; Stripe, organizer dashboard, check-in; for Buda events |
| SEO/Indexing | 🔧 Fixed Apr 8 | Was not indexing enough pages |
| Business Registration Tool | 🔧 Planned | Andres building MVP |
| Social Media Job Post Automation | 🔧 Planned | Auto-generate on job creation via Grok |
| WhatsApp/Telegram integration | 💡 Concept | Connect Business Coach to messaging platforms (Apr 5 discussion) |
| Mobile App | 📋 Deferred | Low priority; parallel workstream planned |
| AI Marketplace | 💡 Concept | Adeleke's idea; approved in principle |
| Daily video production | 💡 Exploring | "How can we start producing video daily?" — exploring AI video tools |

---

## Business Plan Creator — Technical Architecture

**Flow:**
1. User answers 1 open-ended question ("Tell me about your business idea")
2. o4-mini generates executive summary + customer targets
3. o3-mini generates full business plan sections
4. User edits section by section
5. Final preview → Download as PDF or Word

**Known Bugs (May 2025):**
- Customer personas not always passed to o3-mini → inconsistency
- TAM/SAM figures need validation
- Left nav menu collapses when it should stay open
- Competitor map in wrong location (should be on competitor page)
- Plan display after subscription purchase shows "upgrade" incorrectly

**Quality Issues (from May 17 Prompt Review — [[wiki/meetings/2025-05-17-prompt-reviews-bpc-quality]]):**
- Vague numbers / hallucinated statistics (no real data sources)
- Generic customer personas (not grounded in business context)
- Lack of citations for market claims
- Financial section unreliable (no verification mechanism)
- **Decision:** Adopt Brave Search API for real-time web data fetching to reduce hallucination
- Map repurposed: business location pin moved to competitor map for actual competitive visualization

**Enterprise API Integration (from May 15 call — [[wiki/meetings/2025-05-15-zachary-barker-wyatt-hook-enterprise]]):**
- Portal white-label for EDC/city clients uses enrollment key system (single reusable key in URL)
- API integration available at $4,250 one-time (may shift to subscription)
- HubSpot scoring triggers automatic key delivery to qualified users
- Tampa Bay evaluating the platform (large city prospect)
- Sandbox environment available for testing without affecting production

---

## AI Interview Tool — Designed Spec

- Voice-only initially (audio, not video)
- Questions AI-generated from job title input (5-15 questions)
- Candidate records answers → AI transcribes + analyzes
- Analytics: keywords detected, strengths, red flags, confidence, clarity, overall match quality
- Save up to 3 interviews per job title
- Business can send voice interview requests to candidates
- Blind hiring principle: skill before appearance
- Development: MVP first, no design required (per Andres, May 2025)

---

## Business Insights — Designed Spec

- Market size (TAM/SAM/SOM) — needs calculation fix
- Customer personas (with AI-generated images)
- Competitor map with location density (help decide where to open)
- Industry trends
- SWOT matrix
- Cost structure (user-personalizable with dropdown)
- Milestone tracking (mark complete → auto-generate next)
- Initial capital allocation

---

## Internal AI Model (Custom DeepSeek R1)

Built for code generation specific to Moil's codebase. Key learnings:
- Dataset must include instruction + expected output (not just code)
- Training phases: code generation → code review → file creation → pseudocode → dev environment setup
- Frontend dataset being built by Taiwo in parallel with Adeleke's backend dataset

---

## Pricing (confirmed from meetings)

| Plan | Price | Key Features |
|---|---|---|
| Starter | $15/mo | AI Coach, market research, 3 job posts/mo |
| Professional | $25/mo | 10 job posts/mo, premium analytics |
| Market Pro | $75/mo | Unlimited jobs + images, Content360, video credits |

- Annual billing: up to 25% savings
- Bi-weekly payment option requested by Andres (to be added)

---

---

## Azure Infrastructure Notes

### Azure Account Disaster (May 2025)

During the Google Workspace → Microsoft 365 migration (~May 7, 2025), Moil's **entire Azure subscription/directory disappeared**. Impact:
- Website fully down for ~1 week
- Team could not push code changes
- Azure AI Foundry inaccessible (no subscription showing in portal)
- Azure credits still spending (servers still running) despite team lockout

Paula Florez-Estrada (Azure AI Activation Advisor) escalated the support ticket. See [[wiki/meetings/2025-05-21-ai-advisory-azure-foundry]].

### Azure AI Foundry — Chatbot as #1 AI Priority

Paula introduced Moil to Azure AI Foundry (May 2025). Andres named the support chatbot as Moil's #1 AI priority:
- RAG over all Moil product documentation
- Answers customer support questions throughout the site
- Fully owned by Moil; export via APIs/endpoints
- Azure sponsorship credits applicable
- Templates available for quick deployment

### Azure Chat Integration (ACS) — Dec 2024 Plan

Kranthi Kumar (Sonata Software / Microsoft Founders Hub) introduced Azure Communication Services for end-to-end chat + WhatsApp Business integration. See [[wiki/meetings/2024-12-03-technical-advisory-azure]].

### Business Plan Creator Architecture (Mar 2025 Design Session)

From the March 12, 2025 design session ([[wiki/meetings/2025-03-12-business-plan-creator-design]]):
- **8 output sections**, **20-40 questions**, **3 tiers** (Idea/Plan/Grow)
- Conversational UX mirrors the resume builder (voice/text input)
- DeepSeek for analytical components; Gemini for market research
- Pricing anchor: "$1,500 traditional → $100 with Moil"

### MongoDB → Postgres Migration (Dec 2024)

MongoDB Atlas was running $160/month. Team identified this as unsustainable; discussed Postgres migration for cost reduction. See [[wiki/meetings/2024-batch-low-signal-calls]].

---

## Connections

- [[wiki/meetings/2025-03-28-jacob-andres-pivot-ai-tools]] — pivot declaration
- [[wiki/meetings/2025-04-07-moil-marketing-call-toolbox-vision]] — toolbox vision
- [[wiki/meetings/2025-05-16-team-meeting-platform-review]] — latest platform state
- [[wiki/meetings/2025-05-21-ai-advisory-azure-foundry]] — Azure disaster + AI Foundry chatbot priority
- [[wiki/meetings/2025-03-12-business-plan-creator-design]] — BPC architecture session
- [[wiki/meetings/2024-12-03-technical-advisory-azure]] — Azure migration advisory (Kranthi Kumar)

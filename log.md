# Moil Brain — Ingestion Log

This file tracks every source that has been processed by `/kb compile`. Claude Code appends an entry here after each ingestion run.

---

## Format

```
### [YYYY-MM-DD] Source title
- **File:** raw/filename.ext
- **Type:** article | transcript | pdf | note | tweet-thread | other
- **Pages created:** [[wiki/concepts/X]], [[wiki/people/Y]], ...
- **Pages updated:** [[wiki/moil/Z]]
- **Summary:** One-sentence description of what this source was about
```

---

## Log Entries

### [2026-04-11] First Full Compilation — Batch Ingestion

**Trigger:** Andres asked to kick off the Brain. Run in Claude Cowork (direct file access).

**Sources processed (7 of 12 raw files):**

- **File:** raw/imessages-people-2026-04-09.md
  - **Type:** relationship-intelligence
  - **Pages created:** [[wiki/people/john-costilla]], [[wiki/people/mark-polanco]], [[wiki/people/travis-sutherland]]
  - **Summary:** iMessage conversations revealing family structure, nicknames, and business relationships

- **File:** raw/outlook-emails-2026-04-09.md
  - **Type:** email-digest
  - **Pages created:** [[wiki/people/daniel-guadiano]]
  - **Summary:** Outlook email threads — Astra Restaurant lead, CoffeeSpace partnership, Johns Creek Chamber

- **File:** raw/buda-hive-edc-2026-04-11.md
  - **Type:** partnership / customer / contract
  - **Pages created:** [[wiki/people/jennifer-storm]], [[wiki/people/joshua-edmond]], [[wiki/people/jacquie-martinez]], [[wiki/concepts/buda-hive]], [[wiki/concepts/aedo]], [[wiki/concepts/campaignos]]
  - **Summary:** Full intelligence file on Buda HIVE/EDC — contracts, AEDO, CampaignOS, timeline

- **File:** raw/moil-documents-2026-04-09.md
  - **Type:** business-plan
  - **Pages updated:** [[wiki/moil/positioning]], [[wiki/moil/icp]], [[wiki/moil/gtm]]
  - **Summary:** Moil Enterprise business plan — traction, pricing, market, team, financials

- **File:** raw/moilapp-website-2026-04-09.md
  - **Type:** company-website
  - **Pages updated:** [[wiki/moil/positioning]], [[wiki/moil/icp]], [[wiki/moil/gtm]]
  - **Summary:** Full website scrape — features, pricing, hiring metrics, testimonials, candidate platform

- **File:** raw/facebook-pages-2026-04-09.md
  - **Type:** social-media
  - **Pages updated:** [[wiki/moil/gtm]]
  - **Summary:** AIbyAndres + MoilWorks Facebook pages — follower counts, engagement, social links

- **File:** raw/github-project-tracker.md
  - **Type:** project-tracker
  - **Used for:** AGENTS.md context, task prioritization
  - **Summary:** 48 repos across 3 orgs — activity status, cleanup recommendations, priority tracking

**Also updated:**
- `pi-workspace/AGENTS.md` — 16 bracketed placeholders filled with real data
- `index.md` — source inventory and stats updated

**Remaining raw files (not yet compiled):**
- `brain-guide.md` — meta-guide (reference, not wiki content)
- `know-me-extraction-prompts.md` — extraction prompts (tooling)
- `x-bookmarks-2026-04-11.md` + copy — X bookmark digests (queue for next compile)
- `buda-hive-edc-2026-04-09.md` — earlier version, superseded

---

### [2026-04-11] Second Full Compilation — wiki/summaries + new concepts

**Trigger:** Andres asked to build wiki/summaries/ for every raw file + concept pages for recurring themes + MEMORY.md.

**Summaries created (11 — one per raw file):**
- [[wiki/summaries/brain-guide]]
- [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [[wiki/summaries/buda-hive-edc-2026-04-09]] (marked SUPERSEDED)
- [[wiki/summaries/facebook-pages-2026-04-09]]
- [[wiki/summaries/github-project-tracker]]
- [[wiki/summaries/imessages-people-2026-04-09]]
- [[wiki/summaries/know-me-extraction-prompts]]
- [[wiki/summaries/moil-documents-2026-04-09]]
- [[wiki/summaries/moilapp-website-2026-04-09]]
- [[wiki/summaries/outlook-emails-2026-04-09]]
- [[wiki/summaries/x-bookmarks-2026-04-11]]
- [[wiki/summaries/x-bookmarks-2026-04-11-copy]]

**New concept pages:**
- [[wiki/concepts/brain-architecture]] — Andres's 5-layer pipeline
- [[wiki/concepts/claude-code]] — Anthropic's CLI agent
- [[wiki/concepts/claude-cowork]] — scheduled/background Claude workflows
- [[wiki/concepts/openclaw-hermes]] — open-source parallel ecosystem
- [[wiki/concepts/fantelo]] — Andres's parallel project
- [[wiki/concepts/moil360]] — Moil's 30-day marketing engine brand
- [[wiki/orgs/coffeespace]] — partnership ecosystem contact

**New people pages:**
- [[wiki/people/shay-foley]] — Johns Creek Chamber, deferred partnership
- [[wiki/people/hazim-mohamad]] — CoffeeSpace outreach

**Also updated:**
- `index.md` — summaries section added, concept/people counts refreshed
- `MEMORY.md` — new file capturing open actions from raw sources

---

### [2026-04-12] Email History — Oct 2025 to Apr 12, 2026
- **File:** raw/email-history-2026-04-12.md
- **Type:** email-digest
- **Pages created:** [[wiki/summaries/email-history-2026-04-12]], [[wiki/people/anita-lansing]]
- **Pages updated:** [[wiki/moil/gtm]] (cold outbound campaign now documented as LIVE)
- **Summary:** 10-day email history revealing a 63+ org cold outreach blitz to chambers/EDCs, new active customer Anita Lansing (9 emails), confirmed Inna as Content360 delivery client, John Costilla's "Agentic AI" signal, and Siren Beauty warm lead.

### [2026-04-12] Email History — 2-Month Backfill (Feb 12 – Apr 12, 2026)
- **File:** raw/email-history-2months-2026-04-12.md
- **Type:** email-digest (full pagination, 620 received + 1000 sent)
- **Pages created:** [[wiki/summaries/email-history-2months-2026-04-12]]
- **Pages updated:** [[wiki/people/john-costilla]] (EDC staff role discovered), [[wiki/moil/gtm]] (cold outbound already updated from 10-day ingest)
- **Summary:** 2-month email backfill reveals: John Costilla works at Buda EDC, full Moil team roster (6 members), Casey Earley is HIVE operational backbone (21 emails), Queen Creek Chamber is highly active (12 emails), Inna confirmed as Content360 delivery client, 4+ new customer/lead contacts surfaced, and cold outreach is broader than the 10-day snapshot showed.

---

### [2026-04-12] X Bookmarks Deep Compile — 129 Items

- **Files:** `raw/x-bookmarks-2026-04-11 copy.md` (primary, 129 items), `raw/x-bookmarks-2026-04-11.md` (secondary, 114 items)
- **Type:** tweet-bookmarks (curated X feed, Mar 26 – Apr 11, 2026)
- **Note:** Previous entries (2026-04-11 Second Full Compilation) only summarized these files. This run did the DEEP compile — extracted every concept, person, tool, and framework.

**Pages created (16 concept pages):**
- [[wiki/concepts/seedance]] — Seedance 2.0 AI video (joint audio-video synthesis, Higgsfield + fal.ai)
- [[wiki/concepts/heygen]] — HeyGen Avatar V (character-consistent brand video, captured in 15 sec)
- [[wiki/concepts/vibe-coding]] — Vibe coding paradigm (spec-based workflow, dead code risk, non-dev access)
- [[wiki/concepts/gtm-system-multi-channel]] — MichLieben's 3-layer LinkedIn + multi-channel GTM flywheel ($40K→$7M ARR)
- [[wiki/concepts/ai-org-design]] — AI-native org design (Jack Dorsey "From Hierarchy to Intelligence" + $400K roles replaced)
- [[wiki/concepts/self-learning-gtm-brain]] — Campaign-learning GTM brain that improves from each launch (@pierreeliottlal)
- [[wiki/concepts/obsidian]] — Obsidian as the wiki view layer (plugins, iCloud sync, graph view)
- [[wiki/concepts/local-ai-inference]] — Mac Silicon MLX local AI (Gemma 4 day-0, Qwen3.5 27B near-Opus, LFM2.5-350M)
- [[wiki/concepts/linkedin-gtm]] — LinkedIn algorithm + 3 revenue layers + competitor follower extraction
- [[wiki/concepts/agent-memory-files]] — SOUL.md/MEMORY.md/DREAMS.md/"7 text files" identity pattern
- [[wiki/concepts/smb-ai-audits]] — AI audit service model (Google Ads 190 checks, SEO, CRO, Google Maps play)
- [[wiki/concepts/goose-ai]] — Goose open source agent (Jack Dorsey-endorsed, 471K views)
- [[wiki/concepts/home-service-cro]] — 4.6% conversion framework for home service SMBs
- [[wiki/concepts/meta-harness]] — Self-improving AI agent loop (Meta Harness paper, @MatthewBerman demo)
- [[wiki/concepts/google-stitch]] — Google Stitch 2.0 design-to-code tool + design-system.md pattern
- [[wiki/concepts/content-engine]] — Agent-orchestrated content pipeline (SparkDrop, @coreyganim 21M views claim)

**Pages created (5 minds pages):**
- [[wiki/minds/nick-spisak]] — @NickSpisak_, most comprehensive non-developer Claude educator (7 posts saved)
- [[wiki/minds/corey-ganim]] — @coreyganim, most bookmarked creator (9+ posts), SMB AI monetization
- [[wiki/minds/hooeem]] — @hooeem, full-course format Claude guides (2.8M views on agent course)
- [[wiki/minds/jack-dorsey]] — @jack, "From Hierarchy to Intelligence" (5.6M views) + Goose endorsement
- [[wiki/minds/farza-mohideen]] — @FarzaTV, Farzapedia (1.7M) + Clicky AI teacher (2.7M)

**Pages updated (6):**
- [[wiki/concepts/managed-agents]] — deployment patterns, competitive landscape, "second employee" framing added
- [[wiki/concepts/llm-knowledge-bases]] — Obsidian view layer, Farzapedia, Claudeopedia wave documented
- [[wiki/concepts/ai-video-tools]] — $1M/mo workflow, SparkDrop content engine, Seedance/HeyGen links
- [[wiki/concepts/ai-cold-outreach]] — one-URL campaign builder, SMS/iMessage play, new tactical options
- [[wiki/radar/claude-code-changelog]] — 5 new entries (Monitor tool, security warning, Claude Ads skill, macOS plugin, Stitch)
- [[wiki/minds/andrej-karpathy]] — derivative wave documented, Obsidian view layer noted

**Summary created:**
- [[wiki/summaries/x-bookmarks-deep-compile-2026-04-12]] — master reference with signal rankings and creator watch list

**Summary:** The deepest signal window in the Brain to date — three simultaneous viral events (Karpathy's LLM KB post 19.3M views, Claude Managed Agents launch 20M views, Seedance 2.0 AI video wave) converged in a single 2-week period. Most actionable findings for Moil: (1) start LinkedIn authority strategy, (2) position Content360 as a "content engine" not a "tool", (3) build Google Maps + Claude outbound pilot, (4) audit Claude Code permissions on Mac Mini M4, (5) enable Obsidian as Brain view layer.

---

### [2026-04-12] Microsoft Teams Digest — 30-Day Window (Mar 13–Apr 12, 2026)

- **File:** raw/teams-2026-04-12.md
- **Type:** team-communications
- **Pages created:**
  - [[wiki/meetings/README]] — first README for the meetings folder (previously empty)
  - [[wiki/meetings/teams-attendance-protocol-2026-04]] — first-ever meeting page; documents Moil's async clock-in protocol
  - [[wiki/concepts/moil-team-ops]] — Moil's async team operating system (MS Teams + Power Automate)
  - [[wiki/summaries/teams-2026-04-12]] — structured summary of this raw source
- **Pages updated:** none
- **Summary:** 30-day Teams pull contained 27 messages — all 26 substantive messages were identical automated Workflow bot posts (7:00 AM daily clock-in reminder); `#Alerts` channel had no messages. No human-authored content, decisions, action items, or people intelligence was captured. Value is structural: confirmed Moil operates on MS Teams with a Power Automate-enforced async attendance ritual; `meetings/` folder initialized for the first time. A future pull including human responses would unlock team roster and compliance intelligence.

---

---

### [2026-04-12] OneDrive Meetings — Full Year Ingestion (Aug 2024–May 2025)

- **Files:** 25 files in `raw/meetings/` (mix of Gemini notes and full transcripts)
- **Type:** meeting-records (team meetings, 1:1s, sales calls, partner calls, marketing calls)
- **Date range of content:** 2024-08-07 through 2025-05-19

**Pages created (20 wiki/meetings/ pages):**
- [[wiki/meetings/2024-08-07-abel-zachary-sales-close]] — Zachary Corp closes at $699/yr; first major client
- [[wiki/meetings/2025-01-08-ai-presentation]] — Andres presents/watches generative AI overview
- [[wiki/meetings/2025-01-22-team-meeting-ai-model-selection]] — DeepSeek R1 selected; Workforce Capital Solutions $15-20M opportunity
- [[wiki/meetings/2025-01-27-deepseek-model-demo]] — Steve demos working DeepSeek code generation
- [[wiki/meetings/2025-01-29-team-meeting-code-dataset]] — Dataset creation strategy for internal model
- [[wiki/meetings/2025-02-05-jacob-andres-sync]] — Short ops sync; Google Docs for notes
- [[wiki/meetings/2025-03-12-team-meeting-signup-business-plan-mvp]] — Sign-up redesign + Business Plan Creator launch
- [[wiki/meetings/2025-03-28-jacob-andres-pivot-ai-tools]] — **PIVOT MEETING**: Job-matching → AI toolbox; Interview Tool introduced
- [[wiki/meetings/2025-04-04-team-meeting-algorithm-business-planner]] — Weighted matching algorithm; UTSA license opportunity; MS Teams migration
- [[wiki/meetings/2025-04-07-moil-marketing-call-toolbox-vision]] — Resume builder complete; toolbox vision + full interview tool spec
- [[wiki/meetings/2025-04-09-jacob-andres-business-plan-hubspot]] — Hybrid questions; HubSpot CRM setup; Google→Microsoft migration
- [[wiki/meetings/2025-04-11-team-meeting-prompt-engineering-job-postings]] — 4-page business plan achieved; GPT-4 > GPT-4 Turbo (cost); Sakuri Corp job postings
- [[wiki/meetings/2025-04-14-team-meeting-business-plan-template]] — Final workflow + template structure agreed (2.5hr session)
- [[wiki/meetings/2025-04-18-team-meeting-openai-agent-email-marketing]] — OpenAI agent built by Steve; Google account shutting off May 5
- [[wiki/meetings/2025-04-21-team-meeting-ai-mvp-design-marketing]] — AI-first design approach; marketing plan assigned to Jacob
- [[wiki/meetings/2025-04-28-hubspot-marketing-kickoff-sebastian]] — Sebastian Oviedo (marketing intern) onboarded
- [[wiki/meetings/2025-04-28-moil-marketing-call-ai-content]] — AI image generation strategy; Business Plan Creator "mostly complete"
- [[wiki/meetings/2025-05-09-manos-de-cristo-workshops]] — June 2025 3-workshop series planned; EGBI consulting + Entrepreneurial Spirit Award
- [[wiki/meetings/2025-05-14-jacob-andres-business-insights-review]] — Business Insights section-by-section review; competitor map, TAM/SAM fixes needed
- [[wiki/meetings/2025-05-16-team-meeting-platform-review]] — Two-model pipeline (o4+o3-mini); social automation approved; interview tool MVP approach
- [[wiki/meetings/2025-05-19-moil-marketing-call-technical-issues]] — Low signal; technical failures throughout

**Pages created (6 wiki/people/ pages):**
- [[wiki/people/jacob-oluwole]] — Moil PM; present in virtually every meeting; Nigerian developer
- [[wiki/people/adeleke-tolulope]] — Lead AI/ML engineer (Steve); built OpenAI agent; fine-tuned DeepSeek
- [[wiki/people/abiodun-solomon]] — UI/UX designer (Ablad); Figma; had family emergency Apr 2025
- [[wiki/people/taiwo-ola-balogun]] — Frontend engineer; Gemini for code gen
- [[wiki/people/sebastian-oviedo]] — Marketing intern via HubSpot; blue-collar background; 4-week engagement starting Apr 28

**Pages created (1 wiki/moil/ page):**
- [[wiki/moil/product-roadmap]] — Complete AI stack, feature status, technical specs for all Moil products

**Pages updated:**
- [[wiki/moil/positioning]] — Product evolution narrative + "offline workers" language + toolbox framing
- [[wiki/moil/gtm]] — New channels (UTSA license, school presentations, Manos De Cristo, Sebastian), active clients (Zachary Corp, Sakuri Corp), HubSpot CRM, email marketing infrastructure
- [[MEMORY]] — 20+ historical action items added for follow-up verification

**Key intelligence captured:**
1. **Full Moil team roster:** Andres (CEO), Jacob (PM), Adeleke/Steve (Lead AI), Taiwo (Frontend), Abiodun/Ablad (Design), Sebastian (Marketing intern)
2. **The pivot:** March 28, 2025 — Moil pivoted from job-matching to comprehensive AI toolbox for job seekers AND SMBs. "The market told us what to do."
3. **Clients confirmed:** Zachary Corporation (Aug 2024, $699/yr), Sakuri Corporation (Apr 2025, ongoing)
4. **Product milestone:** Resume builder completed Apr 2025; Business Plan Creator operational May 2025; Interview Tool designed and in development
5. **Infrastructure:** Google Workspace → Microsoft 365 migration (May 2025 deadline)
6. **AI stack:** Gemini (resume) → OpenAI agent (business plan) → o3/o4-mini (insights) — all confirmed operational
7. **Andres's other activities:** EGBI consulting (Austin nonprofit), Entrepreneurial Spirit Award 2025, Manos De Cristo workshops, school presentations
8. **Strategic opportunity:** UTSA license deal for Business Plan Creator (mentioned Apr 4, 2025 — needs follow-up)

**Summary:** This ingestion captured a year of Moil's most important business decisions — the product pivot, the team dynamics, the technology architecture, two confirmed clients, and the transition from a job board to a full AI platform. The Brain now has structural context for every strategic decision Andres made between August 2024 and May 2025.

---

---

### [2026-04-12] OneDrive Full Transcripts — Run 2 (25 Transcript Files)

- **Files:** 25 files in `raw/meetings/transcript-*.md` format
- **Type:** meeting-transcripts (full text — customer calls, advisory calls, team meetings, partner calls)
- **Date range of content:** 2024-10-02 through 2025-05-21
- **Note:** `transcript-2024-10-03-team-meeting-october-2024.md` is a CONCATENATED file of Feb–May 2025 meetings (NOT an Oct 2024 meeting); content is largely a duplicate of Run 1 Gemini notes — no new pages created from it.

**Pages created (wiki/meetings/ — 15 new pages):**
- [[wiki/meetings/2024-10-30-moneta-ventures-investor-panel]] — Andres attended Capital Factory investor panel; Moneta Ventures GP thesis; B2B SaaS focus; AI excitement
- [[wiki/meetings/2024-10-31-monica-munoz-andry-gahcc-partnership]] — GAHCC discovery call; Monica Munoz Andry + Enrique Castro; Ambassador program; Univision/Caracol pipeline
- [[wiki/meetings/2024-11-22-abel-zachary-november-followup]] — Zachary Corp follow-up; Skilly competitor analysis; enterprise multi-user hierarchy; assessments tab; conference referral offer
- [[wiki/meetings/2024-12-03-technical-advisory-azure]] — Kranthi Kumar / Sonata Software / Microsoft Founders Hub; AWS→Azure migration; ACS chat; WhatsApp Business
- [[wiki/meetings/2024-12-03-daniela-castillo-partner-exploration]] — Daniela Castillo Cañavera; equity partnership; Univision/Caracol/RCN media connections
- [[wiki/meetings/2024-12-05-jacob-call-social-automation]] — Automated job post image pipeline spec; 20 Canva templates + OpenAI + webhook
- [[wiki/meetings/2025-02-28-dafne-job-interview-prep]] — Dafne Gutierrez coaching session; voice resume builder live demo
- [[wiki/meetings/2025-03-04-buda-ambassador-followup]] — Buda Chamber Ambassador program logistics; Rosemary Gamez, Crista Wallace, Frost Bank
- [[wiki/meetings/2025-03-12-business-plan-creator-design]] — 6 AM BPC architecture session; 8 sections, 3 tiers (Idea/Plan/Grow), DeepSeek + Gemini
- [[wiki/meetings/2025-03-26-rick-bough-hays-cisd]] — Rick Bough / Hays CISD CTE; August 2025 PD workshop; strong advocate
- [[wiki/meetings/2025-03-28-monica-davidson-buda-chamber-restaurant-hiring]] — Monica Davidson; restaurant hiring pilot; Crew Day April 11; Shelly Plumlee; podcast
- [[wiki/meetings/2025-04-11-david-levesque-savari-solar]] — David Levesque / Savari; Hungry Hill Foundation lead (East Austin, formerly incarcerated workforce)
- [[wiki/meetings/2025-04-28-hubspot-kickoff-sebastian-full-transcript]] — Full transcript supplement; Alvaro Vilarmarconell (2nd intern); BPC demo details; success metrics
- [[wiki/meetings/2025-05-21-ai-advisory-azure-foundry]] — Paula Florez-Estrada / Microsoft Founders Hub; Azure account disaster; AI Foundry chatbot as #1 AI priority
- [[wiki/meetings/2024-batch-low-signal-calls]] — Batch page: 9 low-signal calls from Oct–Dec 2024 + TXOR April 2025 session

**Pages created (wiki/people/ — 8 new pages):**
- [[wiki/people/enrique-castro]] — GAHCC Director of Membership; "El Taco Financiero" podcast; Univision connections
- [[wiki/people/daniela-castillo-canavera]] — Colombian media professional; Univision/Caracol/RCN media; equity partnership
- [[wiki/people/rick-bough]] — Hays CISD CTE coordinator; August 2025 PD workshop; strong Moil advocate
- [[wiki/people/paula-florez-estrada]] — Azure AI Activation Advisor; 4-month Microsoft Founders Hub engagement
- [[wiki/people/dafne-gutierrez]] — Former Moil marketing; job coaching; voice resume builder testimonial
- [[wiki/people/david-levesque]] — Savari solar AI; Hungry Hill Foundation East Austin connection
- [[wiki/people/zane-gibson]] — TXOR contact; 30+ participant resume-building sessions
- [[wiki/people/abel-esquivel-luna]] — Full page for Zachary Corp anchor enterprise contact

**Pages updated:**
- [[wiki/moil/gtm]] — +11 new channels: GAHCC, TXOR, Hays CISD CTE, Buda restaurant pilot, Spanish-language media, Hungry Hill Foundation, podcasts, Azure AI Foundry chatbot; HubSpot intern updated to include Alvaro Vilarmarconell
- [[wiki/moil/product-roadmap]] — Azure account disaster documented; AI Foundry chatbot as #1 AI priority; BPC 3-tier architecture; MongoDB→Postgres migration; ACS chat integration plans
- [[wiki/moil/customers]] — Zachary Corp + TXOR added to named customers table; Dafne/Rick Bough/Daniela added as product testimonials; group onboarding friction noted
- [[wiki/people/monica-davidson]] — March 2025 restaurant hiring pilot, Crew Day coordination, Shelly Plumlee connection, podcast episode added
- [[index]] — stats updated; Run 2 ingestion summary added

**Key intelligence from Run 2:**
1. **Azure account disaster (May 2025):** Moil's entire Azure subscription disappeared during Google→M365 migration; website down ~1 week; Paula Florez-Estrada escalated
2. **#1 AI priority:** Azure AI Foundry support chatbot (RAG over product docs) — named by Andres on May 21, 2025 call
3. **Business Plan Creator architecture:** 8 sections, 3 tiers, DeepSeek + Gemini — designed March 12, 2025; operational by May 2025
4. **GAHCC channel:** Monica Munoz Andry (CEO) + Enrique Castro ("El Taco Financiero") → Univision/Caracol media pipeline
5. **Hays CISD CTE opportunity:** Rick Bough invited Andres for August 2025 teacher PD; school-to-workforce channel
6. **Hungry Hill Foundation lead:** East Austin workforce re-entry org (homeless/formerly incarcerated); intro via David Levesque
7. **Spanish-language media:** Daniela Castillo Cañavera (Univision/Caracol/RCN) exploring equity partnership
8. **Competitor intelligence:** Skilly reviewed against Moil — Moil advantage: user-friendly, bilingual, AI-native
9. **Enterprise product gaps:** Abel (Zachary) requested multi-user hierarchy, assessments tab, certification tracking
10. **Group onboarding friction:** TXOR April 2025 session (30+ participants) had login issues — product gap for scale

**Summary:** Run 2 revealed the full year of Moil's external relationship-building — community organizations, media channels, enterprise account management, and Microsoft advisory relationships — plus a critical infrastructure crisis (Azure account disappearance) and the AI Foundry chatbot becoming the #1 technical priority. Combined with Run 1's internal team/product intelligence, the Brain now has comprehensive context for Moil's Aug 2024–May 2025 operational history.

---

## How to add an entry

Claude Code automatically appends to this file at the end of each `/kb compile` run. You do not need to edit this manually.

To ingest a new source:
1. Drop the file into `~/My Brain/knowledge-base/raw/`
2. Open Claude Code in `~/My Brain/`
3. Type: `ingest the new source in raw/`
4. Claude Code reads the source, creates/updates wiki pages, and logs the run here

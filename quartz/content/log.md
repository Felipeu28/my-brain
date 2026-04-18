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

### [2026-04-18] Run 13 — Teams Daily Ops Apr 17–18

**Trigger:** Automated scan for unprocessed raw files. One new file: `raw/teams-2026-04-18.md` (committed Apr 18 by `teams-daily` job, 51 messages across 4 threads).

- **File:** raw/teams-2026-04-18.md
  - **Type:** team-communications (51 messages, Apr 17–18 weekend end-of-week review)
  - **Pages created:** [[wiki/meetings/2026-04-18-teams-daily-ops]]
  - **Pages updated:** [[wiki/people/jacob-oluwole]] (Business Coach bug + Alloy invite late + Connectex slipped), [[wiki/people/adeleke-tolulope]] (Claude Code audit session review assigned), [[wiki/people/taiwo-ola-balogun]] (demo prompt context + time-zone boundary), [[wiki/people/abiodun-solomon]] (next-week content deadline Apr 19 + rhythm miscommunication), [[MEMORY]] (new Apr 18–24 week block; trimmed to 200 lines), [[index]] (stats refreshed: 245 pages / 213 raw sources / 57 meetings)
  - **Summary:** End-of-week delivery-pace escalation. Andres repeatedly called out that only 2 of 6 active projects (Meridian + FitLogic) were tested this week — Connectex still untouched despite top-priority label. Business Coach bug flagged (not responding — blocks Jacob's own testing loop). Jacob sent Alloy ATX Moil 360 invite Apr 18 (3 days late vs. Apr 15 push). Taiwo raised first explicit time-zone boundary ("not 11pm / 2am my time"). Abiodun pushed back on content rhythm expectations — deadline set for Sun Apr 19 on next-week Moil + Inna content. Andres flagged architectural regression: current app no longer uses business plan as the single source of truth the prior version did.

**Key intelligence from Run 13:**
1. **Delivery pace is the #1 tension this week.** Direct Andres quotes: "WE ARE VERY BEHIND" / "It's taken us a full week to test 4 projects I built in one week!" / "Did everyone take yesterday off?"
2. **Business Coach is broken in prod** — Jacob couldn't get it to respond. This is the same product Jacob praised ("came out nice") on Apr 15 — regression between Apr 15 and Apr 18.
3. **Moil 360 activation dashboard is live** — partners' dashboard shows when they have activated their license (new product signal, not previously documented).
4. **First time-zone pushback from Nigeria team.** Taiwo's explicit ask to move delivery calls off 11pm/2am his local time is a new scheduling constraint — Andres acknowledged and repeated it to the team.
5. **Architectural regression surfaced.** Andres: "if you look at the previous code the application used a source of truth (business plan) to basically do everything!" — implicit rebuild ask sitting with engineering. May be related to the demo that Taiwo said was "messed up" (context was defined in Lovable, can't replicate in current stack).
6. **Content rhythm shift proposed.** Tuesday push / Sunday review — Andres wants cushion ahead, Abiodun questioned whether that means daily submission or weekly batch. Miscommunication around "less fees" (Andres later said he meant "ideas").
7. **Andres ran a Claude Code audit on a different project** (session `session_01PP9t1m41A2snaRRACs3TNs`) and asked Adeleke to review — extends the pattern of Andres handing off Claude Code sessions to Adeleke for verification.
8. **Connectex is the biggest neglected account.** Jacob named it unprompted as "one of top priorities that we have not looked at" — already a paying customer per earlier runs, and the client contact (Mark Polanco) is on the Moil 360 license list.

---

### [2026-04-18] Run 12 — Batch ingestion of 12 raw sources

**Trigger:** Manual ingestion request. 12 files in raw/ lacked `ingested: true`.

| File | Type | Action |
|---|---|---|
| `buda-hive-edc-2026-04-11.md` | program-doc | Marked ingested — full intel already captured in [[wiki/summaries/buda-hive-edc-2026-04-11]], [[wiki/people/jennifer-storm]], [[wiki/orgs/buda-edc]] |
| `buda-hive-edс-2026-04-09.md` (Cyrillic) | program-doc | Marked ingested — superseded by Apr 11 version; stub at [[wiki/summaries/buda-hive-edc-2026-04-09]] |
| `compile-2026-04-17.md` | compile-report | Marked ingested — Run 10 meta-report, already applied to wiki |
| `facebook-pages-2026-04-09.md` | social | Marked ingested — data already sourced in [[wiki/concepts/moil360]], [[wiki/people/mariana-rodriguez]], [[wiki/summaries/facebook-pages-2026-04-09]] |
| `github-project-tracker.md` | note | Marked ingested — already summarized at [[wiki/summaries/github-project-tracker]] |
| `imessages-people-2026-04-09.md` | email | Marked ingested — **created** [[wiki/people/ingrid-spiritto]] (mother-in-law, net-new); other contacts already had pages |
| `know-me-extraction-prompts.md` | reference | Marked ingested — meta methodology doc, no wiki pages warranted |
| `moil-documents-2026-04-09.md` | note | Marked ingested — **updated** [[wiki/moil/positioning]] with competitor table + ARR financial baseline |
| `moilapp-website-2026-04-09.md` | note | Marked ingested — already sourced in [[wiki/moil/positioning]] and [[wiki/concepts/moil360]] |
| `outlook-emails-2026-04-09.md` | email | Marked ingested — already summarized at [[wiki/summaries/outlook-emails-2026-04-09]] |
| `x-bookmarks-2026-04-11 copy.md` | bookmark | Marked ingested — deep-compiled in prior run (16 concept pages + 5 minds pages) |
| `x-bookmarks-2026-04-11.md` | bookmark | Marked ingested — cross-referenced in prior run |

**Pages created (2):** [[wiki/people/ingrid-spiritto]], [[wiki/concepts/fantelo]] (redirect stub → [[wiki/projects/fantelo]])

**Pages updated (2):** [[wiki/moil/positioning]] (competitor table + ARR targets), [[index]] (stats + header)

**Summary:** Most of these 12 files had already been ingested into wiki pages in earlier runs but lacked the `ingested: true` frontmatter stamp. Net-new content: one new person page (Ingrid Spiritto, mother-in-law) and competitor/financial intelligence added to positioning.

---

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

### [2026-04-12] Microsoft Teams — Full 415-Message Ingestion (Apr 5–12, 2026)

- **File:** raw/teams-2026-04-12.md (OVERWRITTEN — replaces prior 27-message bot-only version)
- **Type:** team-communications (1:1 chats + group chats + channel messages)
- **Messages:** 415 total across 12 threads (181 Andres-Adeleke, 79 Moil Team, 65 Andres-Taiwo, 38 Moil Marketing, 30 Andres-Jacob, 11 Andres-Casey, 3 Mark & Andres, 3 Attendance bot, 2 Landing Page Projects, 1 Monday Collaboration, 1 Eden Discovery, 1 Andres-Abiodun)

**Pages created:**
- [[wiki/meetings/2026-04-06-monday-collaboration-call]] — project alignment call; Planner board created; end-to-end integration push
- [[wiki/meetings/2026-04-09-12-engineering-sprint]] — 4-day sprint: 12+ Claude Code sessions, model cost discovery, Business Coach redesign, PDF/PPT export

**Pages updated (7 people):**
- [[wiki/people/adeleke-tolulope]] — Apr 2026 sprint activity, model cost threads, FB login issue
- [[wiki/people/jacob-oluwole]] — Planner board, customer onboarding, Inna content, power outage, $50 from Andres
- [[wiki/people/taiwo-ola-balogun]] — Meridian full ownership, Stripe integration, credential access issues
- [[wiki/people/abiodun-solomon]] ��� Name correction (Adekanmi not Solomon), content delivery batch, Moil 360 reviews doc
- [[wiki/people/casey-earley]] — Moving to Buda (2051 Cambria, May 16)
- [[wiki/people/travis-sutherland]] — Now a paying customer (travis@zoiwell.com, 1-year Moil 360 license)
- [[wiki/people/inna-benyukhis]] — Content360 delivery client confirmed; May calendar pre-loaded; content loss incident

**Pages updated (3 moil):**
- [[wiki/moil/product-roadmap]] — AI tech stack updated to Apr 2026 (Gemini for images, Qwen paid tier, Grok 4.1 Fast discovery, GPT-5.4 cost spike); feature status refreshed (Business Coach live, Content360 selling, PDF/PPT export, Meridian, Voice Guide)
- [[wiki/moil/gtm]] — 7 new deals documented (Connectex, Alloy, FitLogic, Travis, Jacob Centeno, jilledegs01, Siren Beauty); new channels (direct website builds, content-as-service, WhatsApp/Telegram)
- [[wiki/moil/customers]] �� 8 new customer entries added to named customers table

**Summary page:** [[wiki/summaries/teams-2026-04-12]] — completely rewritten from 27-message structural summary to full 415-message intelligence report

**MEMORY updated:** 25+ new action items across 5 categories (deals, engineering, content, team management, credential security)

**Key intelligence:**
1. **Best month ever:** 4 deals closed in one week (Connectex, Meridian, Alloy closing, FitLogic hiring). Andres: "We are having the best month in our existence!!!"
2. **Development workflow confirmed:** Andres prototypes in Claude Code → shares session link in Teams → Adeleke pulls to staging → tests → pushes to prod
3. **OpenAI cost spike:** `gpt-4o` alias silently upgraded to `gpt-5_4-2026-03-05`. Grok 4.1 Fast ($0.20/$0.50) identified as 30x cheaper replacement
4. **Business Coach redesigned:** Static 22-step wizard replaced with AI-guided onboarding that scrapes websites/PDFs
5. **Abiodun name correction:** Teams shows "Abiodun Adekanmi" not "Abiodun Solomon"
6. **Casey Earley moving to Buda** (May 16, 2026) — deepens HIVE relationship
7. **Credential security risk:** Stripe keys, Supabase passwords, API keys shared in plaintext Teams chat
8. **Team strain signals:** Jacob on 3 weeks of generator power; Taiwo blocked by credentials; Adeleke's FB account locked

**Signal rating: VERY HIGH** — densest operational intelligence source in the Brain to date.

---

### [2026-04-12] OneDrive Transcript Backfill — Run 3 (28 New Files)

- **Files:** 28 files in `raw/meetings/` (transcript backfill of files not downloaded in Run 2)
- **Type:** meeting-transcripts (partner calls, customer calls, marketing calls, team meetings, mobile recordings)
- **Date range of content:** 2024-10-01 through 2025-05-20

**Pages created (10 wiki/meetings/ pages):**
- [[wiki/meetings/2025-05-15-zachary-barker-wyatt-hook-enterprise]] — Enterprise customer call; API integration ($4,250), Tampa Bay prospect, enrollment key/HubSpot workflow
- [[wiki/meetings/2025-05-17-prompt-reviews-bpc-quality]] — BPC quality review; hallucination, vague numbers, Brave API decision for real-time data
- [[wiki/meetings/2024-11-13-txor-moil-partnership-call]] — TXOR partnership established; recurring workshops, caseworker training, live podcast concept
- [[wiki/meetings/2024-11-25-monica-pena-egbi-echo-squad]] — Echo Squad LinkedIn pod onboarding; EGBI partnership; political connections (Velasquez, Fuentes)
- [[wiki/meetings/2024-10-24-julian-sanchez-video-planning]] — Spanish-language FB Live planning; banking+employment for Latinos; Breakout Media
- [[wiki/meetings/2025-05-20-azure-resources-support-call]] — Microsoft support call; Azure tenant mismatch diagnosed as root cause of resource disappearance
- [[wiki/meetings/2024-11-14-virtual-moil-councilman-velasquez]] — Austin City Council meeting; Read AI demo; civic partnership exploration
- [[wiki/meetings/2024-11-27-cardo-resume-building-session]] — Live resume-building session at TXOR/Cardo; Spanish-language; Ricardo Van Arcken coached through Moil
- [[wiki/meetings/2025-01-08-nvidia-inception-onboarding]] — Nvidia Inception accepted; $25K DLI credits; team GenAI/RAG training plan
- [[wiki/meetings/2024-11-27-jacob-abiodun-video-zachary-jobs]] — Zachary Corp 80+ jobs; video content review; first 10 seconds hook problem

**Batch pages created (2):**
- [[wiki/meetings/2024-q4-batch-marketing-calls]] — 14 low-signal files: marketing calls, mobile recordings, testing sessions, dev calls, phone review (Oct 2024–Jan 2025)
- Center for Child Protection (Dec 11, 2024) — EMPTY transcript (2 lines: "Hmm" + "Hello"). Julia Cabin name only. No page created — insufficient content

**Pages created (6 wiki/people/ pages):**
- [[wiki/people/evangeline-sandoval]] — TXOR Austin Site Director; key decision-maker for Moil partnership; first-gen immigrant
- [[wiki/people/monica-pena]] — EGBI; Echo Squad LinkedIn pod; BizTech Clinic speaker coordinator
- [[wiki/people/julian-sanchez]] — Colombian content partner; banking/employment Spanish-language FB Lives
- [[wiki/people/wyatt-hook]] — Platform vendor; API integration ($4,250); sandbox provisioning; enrollment keys
- [[wiki/people/rodney-warner]] — Microsoft ProDirect Support; diagnosed Azure tenant mismatch
- Herlinda Rubalcava — TXOR PIM/case manager (mentioned in TXOR page, no standalone page)

**Pages updated:**
- [[wiki/people/zane-gibson]] — Full TXOR context added: Evangeline Sandoval, Herlinda Rubalcava, partnership timeline from Nov 2024
- [[wiki/moil/gtm]] — +6 new channels: TXOR recurring workshops (with Evangeline context), EGBI Echo Squad, Austin political connections, live hiring podcast concept, Julian Sanchez Spanish content, Nvidia Inception
- [[wiki/moil/product-roadmap]] — BPC quality issues (hallucination, Brave API decision), enterprise API integration pricing and enrollment key architecture, Tampa Bay prospect
- [[MEMORY]] — 13 new action items across enterprise, product, and partnership categories

**Key intelligence from Run 3:**
1. **Tampa Bay city prospect:** Zachary Barker disclosed city of Tampa Bay is evaluating the platform — largest potential enterprise deal documented
2. **Brave API adoption:** Team agreed to use Brave Search API for real-time data in BPC to eliminate hallucination — marks shift from pure LLM generation to RAG
3. **TXOR partnership origin story:** Nov 2024 call with Evangeline Sandoval established recurring workshops and caseworker training — this became Moil's strongest nonprofit channel
4. **Echo Squad = LinkedIn origin:** Monica Pena's LinkedIn engagement pod (Nov 2024) was Andres's first structured LinkedIn strategy — predates the X bookmarks GTM playbook by 18 months
5. **Live hiring podcast:** Pitched to 3 separate partners (TXOR, EGBI, Julian) in Oct-Nov 2024 — shows Andres's multi-channel approach to the same concept
6. **Azure disaster confirmed:** Rodney Warner (Microsoft) confirmed it was a tenant/directory mismatch, not data loss — subscriptions were active but invisible
7. **Nvidia Inception:** Moil accepted into Nvidia Inception program (Jan 2025) with $25K DLI training credits — credibility milestone + training resource
8. **Austin political channel:** Councilman Velasquez (District 3) and Councilwoman Vanessa Fuentes both expressed support for Moil's hiring initiatives
9. **Zachary Corp scale:** 80+ jobs posted through Moil by Nov 2024 — larger than previously documented
10. **Salwa & Roli calls:** Empty/minimal transcripts — Salwa (salwayordi@gmail.com) and Roli (rolicalderin@gmail.com) identities noted but no actionable content

**Summary:** Run 3 completed the full transcript backfill, filling in the Q4 2024 partnership-building period that was missing from Run 2. The Brain now has comprehensive meeting coverage from Oct 2024 through May 2025. Most valuable discoveries: Tampa Bay enterprise prospect, Brave API adoption decision, TXOR partnership origin story, and the Echo Squad as Andres's LinkedIn strategy genesis. Combined with Runs 1 and 2, all 78 raw/meetings/ files are now fully ingested.

---

### [2026-04-13] Run 4 — Clients & Customers Rebuild

**Trigger:** Andres identified that April 2026 clients had no wiki pages, customers.md had no GitHub links, and several people pages had wrong tags.

**Sources cross-referenced:** [[raw/teams-2026-04-12]], [[raw/email-history-2months-2026-04-12]], [[raw/imessages-people-2026-04-09]], [[raw/github-project-tracker.md]]

**Pages created (12 new):**
- [[wiki/orgs/connectex]] — Connectex Solutions (Mark Polanco, CLOSED Apr 9, multi-quarter invoice)
- [[wiki/orgs/fitlogic]] — FitLogic (fitness hiring, first hire imminent Apr 12)
- [[wiki/orgs/siren-beauty]] — Siren Beauty & Wellness (Becky Torres, setup in progress)
- [[wiki/orgs/pure-serenity]] — PureSerenity (jilledegs01, Moil 360 onboarded Apr 10)
- [[wiki/orgs/urbanozuela]] — Urbanzuela (Ana Vetencourt, sister-in-law's business)
- [[wiki/orgs/nuovo-entertainment]] — Nuovo Entertainment (site deployed Apr 9)
- [[wiki/orgs/meridian-buda]] — Meridian Buda (coffee/music venue, CLOSED Apr 9, full events platform)
- [[wiki/orgs/alloy-atx]] — Alloy ATX (gym, Content360 + Moil 360, CLOSING Apr 11)
- [[wiki/people/becky-torres]] — Siren Beauty owner
- [[wiki/people/roxana-yglesias]] — Alloy ATX contact
- [[wiki/people/jacob-centeno]] — Titan Tech Authority (Starter plan, CLOSED Apr 8)
- [[wiki/people/ana-vetencourt]] — Andres's sister-in-law, Urbanzuela owner

**Pages fixed (4 corrections):**
- [[wiki/people/mark-polanco]] — corrected from person/personal to person/customer; added Connectex context (mark@connectex.net)
- [[wiki/people/wyatt-hook]] — corrected from person/customer to person/vendor
- [[wiki/moil/customers]] — added wikilinks + GitHub repo links for all 11 April 2026 clients
- [[wiki/orgs/README]] — rebuilt index with all 12 current org pages

**Summary:** Run 4 rebuilt the clients and customers layer from scratch using Apr 2026 data. The 8 active Moil-Landingpages repos now all have corresponding wiki pages. All April 2026 closed/closing deals are properly documented and linked. Two mis-tagged people pages corrected. customers.md now connects every client to their wiki page and GitHub repo.

---

### [2026-04-13] Run 5 — Monday Collaboration Transcript (Apr 13)

**Trigger:** New unprocessed file detected in raw/: `teams-transcript-monday-collaboration-2026-04-13.md`

**Source:** [[raw/teams-transcript-monday-collaboration-2026-04-13]] — Full VTT transcript of Monday Collaboration call (8:17am–10:00am CT), organized by Jacob Oluwole, all 5 team members present.

**Pages created (1 new):**
- [[wiki/meetings/2026-04-13-monday-collaboration]] — Full meeting record with decisions, action items, and blockers

**Pages updated (8):**
- [[wiki/people/inna-benyukhis]] — CRM bugs surfaced (contacts not reading, campaigns API key missing), meeting confirmed for 10am today
- [[wiki/people/jacob-oluwole]] — Organized meeting; assigned Google Alloy image gen testing before Andres's Apr 14 meeting
- [[wiki/people/adeleke-tolulope]] — PDF/PPTX generation first test done (formatting WIP); pushed staging updates for Business Coach
- [[wiki/people/abiodun-solomon]] — Content behind schedule; testing Business Coach; reiterated testing-notes requirement from Friday
- [[wiki/people/taiwo-ola-balogun]] — Three high-priority items: Meridian Stripe webhook blocker, client handoff document, new massage place client
- [[wiki/people/travis-sutherland]] — Sun Show event next week; Moil will have a demo table
- [[wiki/orgs/meridian-buda]] — Stripe webhook URL blocker documented; Vercel cron secrets using placeholders
- [[wiki/moil/customers]] — (no change needed; massage place client unnamed)

**Key intelligence:**
- **BLOCKER:** Meridian ticket emails dead — Stripe webhook URL not configured + Vercel cron secrets are placeholders
- **BLOCKER:** Inna CRM contact pipeline not displaying + campaigns API key missing (before 10am meeting)
- **Decision:** Brain repos to be cloned for each team member once stable
- **Decision:** Content must be Friday-ready; Mondays are for strategizing
- **Decision:** Client handoff doc required (Vercel, Supabase, Resend, login instructions)
- **New client:** Massage place (unnamed) — website nearly done, needs images
- **Opportunity:** Google Alloy image gen — if it works inside Moil, can charge clients without extra integration work
- **Event:** Moil showcasing at Sun Show next week (Travis Sutherland's event)
- 12 action items assigned across 5 team members (see meeting page)

**Summary:** Ingested the Apr 13 Monday Collaboration transcript — one new meeting page, eight wiki pages updated. Two active blockers (Meridian Stripe webhook, Inna CRM), three key decisions, and a new unnamed massage place client.

---

## How to add an entry

Claude Code automatically appends to this file at the end of each `/kb compile` run. You do not need to edit this manually.

To ingest a new source:
1. Drop the file into `~/My Brain/knowledge-base/raw/`
2. Open Claude Code in `~/My Brain/`
3. Type: `ingest the new source in raw/`
4. Claude Code reads the source, creates/updates wiki pages, and logs the run here

---

### [2026-04-14] Run 6 — Active Client + HIVE Batch

**Trigger:** Manual ingestion run — 12 raw HIVE/client files + 6-month email history.

**Organization principle applied:** All pages tagged with P1 (status: active), P2 (status: warm), or P3 (status: archived) + last_contact dates.

---

**BATCH 1 — Active Clients:**

- **raw/hive-siren-beauty-wellness-strategy-plan.md** → [[wiki/people/becky-torres]] (deal timeline confirmed; $2,200 paid Apr 6), [[wiki/orgs/siren-beauty]] (full website redesign strategy: Next.js 15 + Sanity CMS + AEO + 6-phase roadmap)
- **raw/hive-inna.md + hive-inna-s-website-feedback.md + hive-empowered-nutrition-project-breakdown.md + hive-coaching-session-summary.md** → [[wiki/people/inna-benyukhis]] (full business profile: SFM practitioner, women 40+, $15K+ wasted marketing history, 6-module AI website plan)
- **raw/email-history-6months-2026-04-14.md** → [[wiki/people/megan-miller]] (full rebuild: NP/hormone expert, meganmillernp@gmail.com, onboarding Apr 1), [[wiki/moil/pipeline]] (full rebuild with all Apr 2026 closed deals), [[wiki/moil/customers]] (complete P1/P2/P3 rewrite — 13 active clients)

**BATCH 1 — HIVE Program:**

- **raw/hive-buda-hive-sosx-run-of-show.md** → [[wiki/orgs/buda-edc]] (SoSX event Mar 12, 2026 — Andres as named Incubator Strategist; 4 cohort graduates; Jennifer Storm = IEDC Economic Developer of the Year)
- **raw/hive-series-based-hive-program.md** → [[wiki/concepts/hive-program]] (NEW — 4-stage curriculum: Hatch/Initiate/Validate/Expand)
- **raw/hive-coaching-session-summary.md** → integrated into Inna profile + Anita Lansing

**BATCH 2 — Key 2025 Meetings:**

- **raw/odtr-20241120...Echo-Squad...** → [[wiki/orgs/echo-squad]] (NEW — Monica Pena's LinkedIn pod, <10 people, Thursday 9–10 AM, Dec 2024–Feb 2025)
- **raw/odtr-20250515...Zachary-Barker-and-Wyatt-Hook...** → [[wiki/people/zachary-barker]] (NEW — CEcD, multi-city EDC operator; Tampa Bay expansion signal validates Moil B2G thesis)
- **raw/odtr-20250521...Moil-Enterprise-AI-Advisory...** → [[wiki/meetings/2025-05-21-moil-enterprise-ai-advisory]] (NEW — Azure account disaster: GWS→M365 migration wiped entire directory; AI Foundry deferred)
- **raw/odtr-20241125...Monica-Pena... + raw/odtr-20250411...David-Andres... + raw/odtr-20250205...Jacob-Andres...** → existing pages confirmed/updated (source refs added)

**Pages created (4):** [[wiki/concepts/hive-program]], [[wiki/orgs/echo-squad]], [[wiki/people/zachary-barker]], [[wiki/meetings/2025-05-21-moil-enterprise-ai-advisory]]

**Pages updated (8):** [[wiki/people/becky-torres]], [[wiki/people/inna-benyukhis]], [[wiki/people/megan-miller]], [[wiki/orgs/siren-beauty]], [[wiki/orgs/buda-edc]], [[wiki/moil/customers]], [[wiki/moil/pipeline]], [[wiki/people/anita-lansing]]

**Summary:** Run 6 confirmed 13 active paying P1 clients in April 2026. Rebuilt customers.md and pipeline.md with importance × recency structure. Key intelligence: Siren Beauty full website project scope, Inna's $15K+ wasted marketing backstory, Zachary Barker's Tampa Bay signal for B2G thesis, Azure account disaster context.


### 2026-04-14 — Data-quality cleanup + MEMORY.md archive migration

- **Type:** maintenance
- **Summary:** Fast-win audit fixes. Deduplicated raw/ (38 MD5-identical files removed, all from raw/onedrive-transcripts/). Renamed Cyrillic `buda-hive-edс-2026-04-09.md` → `buda-hive-edc-*` (ASCII). Consolidated two x-bookmarks duplicate pairs (kept the deeper 129-item version, now canonical name). Fixed 41 escape-broken wikilinks (`[[target\|Display]]` → `[[target|Display]]`) across ANDRES.md, customers.md, pipeline.md. Corrected index.md stats: now 190 wiki pages / 192 raw sources (was claiming 213/91).

### Archive — May 2025 historical verify items (moved here from MEMORY.md 2026-04-14)

These were flagged from Aug 2024–May 2025 meeting transcripts ingested Apr 12. Moved out of MEMORY.md to keep it under the 200-line rule. If any become active, promote back to MEMORY.md.

- Azure access for Adeleke (~May 2025 support case)
- Job matching algorithm weighted update (Adeleke Apr 2025)
- Google → Microsoft migration (deadline May 5, 2025)
- HubSpot full access for Jacob (after May 15, 2025)
- Business Plan Creator bugs: personas, TAM/SAM, competitor map, cost structure, milestones, plan display
- Interview Tool MVP (Andres said "build without design first" — May 2025)
- Social post auto-generation on job creation (Grok + template)
- Sebastian Oviedo 4-week marketing engagement (Apr 28–May 26, 2025)
- Manos De Cristo workshops (June 2025 — 3 Fridays)
- Sakuri Corporation Texas job listings (Jacob assigned)
- Zachary/Great Construction Corp account status
- UTSA license opportunity via EDC contact
- Tampa Bay (Zachary Barker) enterprise evaluation — see [[wiki/meetings/2025-05-15-zachary-barker-wyatt-hook-enterprise]]
- $4,250 API integration (Wyatt Hook / Josh Edmond) — decision?
- Sandbox access for Tampa Bay testing — provisioned?
- Brave Search API for BPC hallucination reduction — implemented?
- Azure directory tenant mismatch (Rodney Warner) — restored?
- TXOR recurring workshops (Evangeline Sandoval, Nov 2024)
- TXOR caseworker training (proposed Nov 2024)
- Live hiring podcast (TXOR + EGBI + Julian Sanchez, Oct–Nov 2024)
- EGBI Echo Squad LinkedIn pod (Nov 2024–Feb 2025)
- Julian Sanchez FB Live Spanish content (late Oct 2024)
- Councilman Velasquez / Vanessa Fuentes civic initiatives
- Nvidia Inception credits (25 DLI, received Jan 2025)

---

### [2026-04-14] Run 7 — Roxana Onboarding + HIVE Curriculum Batch + Low-Signal Cleanup

**Trigger:** Automated scan for unprocessed raw files. Found 27 new files — 1 high-priority meeting transcript, 1 medium-priority HIVE session, 11 HIVE curriculum files, 8 HIVE week handouts, 4 low-signal meeting transcripts, 2 empty Teams pulls.

---

**HIGH PRIORITY — New meeting transcript:**

- **File:** raw/teams-transcript-roxana-andres-2026-04-14.md
  - **Type:** customer-onboarding (Teams call, 90 min)
  - **Pages created:** [[wiki/meetings/2026-04-14-roxana-alloy-atx-onboarding]]
  - **Pages updated:** [[wiki/people/roxana-yglesias]], [[wiki/orgs/alloy-atx]], [[wiki/moil/customers]], [[MEMORY]]
  - **Summary:** Roxana Yglesias / AlloyATX closed on Moil 360 Market Pro at $75/mo. Full onboarding: asset handover from previous agency (Shannon/Gabriel), 21-question market research flow, satellite landing pages on GoDaddy domains, Spanish-language pages, wellness referral network. 11 action items assigned.

**MEDIUM PRIORITY — HIVE post-cohort session:**

- **File:** raw/hive-cohort-onboarding-session-feb13-2026.md
  - **Type:** hive-group (whisper transcript, 15 min)
  - **Pages created:** [[wiki/meetings/2026-02-13-hive-life-after-cohort-session-2]]
  - **Summary:** Post-cohort onboarding for Liz and Miguel (Buda residents). Server was down; couldn't demo. Miguel hit candidate-vs-business account confusion twice. Rescheduled to Feb 14.

**BATCH — HIVE curriculum files (11 files → enriched existing concept page):**

- **Files:** raw/hive-camp.md, raw/hive-entrepreneur-camp.md, raw/hive-entrepreneur-camp-notes.md, raw/hive-grok-guide-and-talking-points.md, raw/hive-1-or-2-day-intensive-hive-entrepreneurial-program.md, raw/hive-hybrid-hive-entrepreneurial-program.md, raw/hive-buda-hive-flexible-networking-content.md, raw/hive-emails-for-hive.md, raw/hive-emails-for-hive-1.md, raw/hive-ai_panel_presentation_guide_long_version.md, raw/hive-hive_week_1_handout_you_as_entrepreneur.md through raw/hive-hive_week_8_handout_launch_preparation.md (8 handouts)
  - **Type:** program-curriculum / reference material
  - **Pages updated:** [[wiki/concepts/hive-program]] (added Entrepreneur Camp June 2025, program format variants table, Grok guide mention)
  - **Summary:** These are HIVE curriculum design documents — program format variants (series, intensive, hybrid), Entrepreneur Camp presentation notes (Andres + Joshua Edmond, June 18 2025), Grok guide for entrepreneurs, weekly handout content (weeks 1–8), email templates, networking content, and AI panel presentation guide. No new people or action items — all reference material that enriches the existing HIVE concept page.

**LOW-SIGNAL — Logged but no new pages:**

- **raw/odtr-20250519-Moil-Marketing-Call-Notes-by-Gemini.md** — Garbled XML/DOCX content from Gemini auto-notes. Jacob + Adeleke had technical difficulties. No decisions or actions. Already covered by [[wiki/meetings/2025-05-19-moil-marketing-call-technical-issues]].
- **raw/odtr-20250422-20250422-TXOR-Moil-Resume-Building-Presentation-Tr.md** — Short snippet of a TXOR virtual workshop. Zane Gibson + ~35 invited participants. Login troubleshooting. Already covered by existing TXOR pages.
- **raw/odtr-20250410-20250410-David-and-Andres-AI-trees-Transcript.md** — David Levesque demoing a solar/battery optimization tool built with ChatGPT. Personal/side project, not Moil business. No actions.
- **raw/odtr-20250520-20250520-All-Resources-Transcript.md** — Rodney Warner (Microsoft ProDirect Support) follow-up on Azure tenant mismatch. Already covered by [[wiki/meetings/2025-05-20-azure-resources-support-call]].

**EMPTY — No content to ingest:**

- **raw/teams-2026-04-14.md** — 429 rate limit error from Graph API. Zero messages pulled.
- **raw/teams-history-6months-2026-04-14.md** — Empty file. Only header, no content.

**Key intelligence from Run 7:**
1. **AlloyATX deal closed:** $75/mo Market Pro — confirmed paying P1 customer
2. **AEO strategy introduced:** Andres pitched AI Engine Optimization (Q&A on every page so AI assistants can reference the business) — this is a new positioning angle beyond traditional SEO
3. **Satellite landing page playbook:** Low-cost SEO strategy using existing GoDaddy domains; Spanish-language variant for bilingual markets — repeatable for other clients
4. **Wellness referral pipeline:** Roxana has functional medicine + Colombia regenerative medicine contacts — potential multi-customer funnel
5. **HIVE Entrepreneur Camp:** June 2025 event with Joshua Edmond at Buda HIVE confirmed — key public event for Moil/HIVE partnership visibility
6. **Onboarding UX friction persists:** Miguel (Feb 2026) hit candidate-vs-business account confusion — same issue documented in earlier TXOR sessions

**Summary:** Run 7 ingested 27 files. The AlloyATX onboarding call was the highest-signal source — a confirmed deal with 11 action items and a wellness referral pipeline. HIVE curriculum files enriched the existing concept page with program format variants and Entrepreneur Camp details. Four low-signal transcripts logged for completeness. Two empty files skipped.

---

### [2026-04-15] Run 8 — Daily Ops Ingestion (7 files)

**Trigger:** Automated scan for unprocessed raw files.

---

**HIGH PRIORITY — Teams daily operations (Apr 14–15):**

- **File:** raw/teams-2026-04-15.md
  - **Type:** team-communications (84 messages, 4 threads)
  - **Pages created:** [[wiki/meetings/2026-04-15-teams-daily-ops]]
  - **Pages updated:** [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/abiodun-solomon]], [[wiki/moil/product-roadmap]], [[wiki/moil/customers]], [[MEMORY]]
  - **Summary:** API cost crisis — token refills 3x/week (was monthly). Full codebase audit ordered to migrate gpt-4o→gpt-5-mini. License distribution push for 5 clients. FitLogic deadline set for Fri Apr 18. Andres issued team-wide urgency message about delivery pace. Buda EDC called about "their product." New unnamed social media client signed.

**MEDIUM PRIORITY — Email digest (Apr 14):**

- **File:** raw/email-digest-2026-04-14.md
  - **Type:** email-digest (24-hour window)
  - **Pages created:** [[wiki/people/renee-simmons]] (Hays CISD, Career Day May 7), [[wiki/people/adam-maxon]] (Pflugerville Mentor Day)
  - **Pages updated:** [[wiki/moil/customers]] (Daniel Guadiano meeting confirmed Thu Apr 16), [[MEMORY]] (7 new action items)
  - **Summary:** Daniel Guadiano/Astra confirmed Thursday meeting. Renee Simmons invited Andres to Career Day May 7 (CHES, 4th/5th graders). Adam Maxon invited to Pflugerville Mentor Day. Buda Retail Roundup Apr 20. 15 chamber breakup emails sent (pipeline hygiene). GitHub webhook secrets rotation needed.

**MEDIUM PRIORITY — SEO Implementation Plan:**

- **File:** raw/odtr-moilapp_SEO_Implementation_Plan_April2026.md
  - **Type:** technical-plan (dated Apr 8, 2026)
  - **Pages created:** [[wiki/concepts/seo-implementation-plan]]
  - **Pages updated:** [[wiki/moil/product-roadmap]] (SEO roadmap reference added)
  - **Summary:** Comprehensive 4-phase SEO roadmap. Only 13/68 pages indexed. Critical fix: `?lg=` URL pollution. Highest-ROI: JobPosting schema for Google Jobs carousel. Blog keyword targets identified. Subdomain consolidation recommended.

**MEDIUM PRIORITY — 9-Month Email History:**

- **File:** raw/email-history-9months-2026-04-15.md
  - **Type:** email-digest (Jul 2025–Apr 2026, 2000 emails, 875 unique contacts)
  - **Pages created:** none (confirms existing relationships)
  - **Summary:** Confirms relationship intensity: Jacob (39 emails), Casey Earley (33), Anita Lansing (29), Megan Miller (26), Becky Torres (23), Buda HIVE (23), Jacquie Martinez (17), Inna (15), Monica Davidson (15), Mark Polanco (15). New signals: Kim Dowers/Queen Creek Chamber (13 emails — active), Daniel/Evermend Group (13 — warm intro pipeline), Jesutomilola/Google xWF (9 — Google Cloud workshop), Katherine Silvas/Helotes (9 — confirming overdue reply flagged in MEMORY). Stripe payment confirmations: $2,200 from Siren Beauty, $200 payments from Alia Wells and Juan Costilla.

**LOW PRIORITY — Business Plan (Mar 2026):**

- **File:** raw/odtr-Moil_Enterprise_business_Plan.md
  - **Type:** business-plan (Mar 5, 2026)
  - **Pages updated:** none (numbers already reflected in positioning/gtm from earlier ingestion of moil-documents-2026-04-09)
  - **Summary:** Updated March 2026 business plan. Confirms: 500+ active businesses, 5,000+ jobs/month, 94% interview success rate, $850 avg cost per hire, 91% 90-day retention. Pricing: Starter $15, Professional $25, Market Pro $75. Largely duplicates content already ingested via moil-documents.

**LOW PRIORITY — Nonprofit Incorporation Steps:**

- **File:** raw/odtr-Moil_Nonprofit_Incorporation_Steps.md
  - **Type:** reference (Jan 2025)
  - **Pages created:** none
  - **Summary:** 8-step incorporation guide for "Moil Empowerment Foundation" nonprofit (501(c)(3)). Historical reference — no indication this has been acted on. Steps: name verification, Certificate of Formation (TX), EIN, bylaws, IRS Form 1023, bank account, TX Comptroller registration, initial programs.

**LOW PRIORITY — Claude Code Weekly Sessions Rollup:**

- **File:** raw/weekly-sessions-2026-04-15.md
  - **Type:** claude-code-weekly-rollup (week of Apr 12)
  - **Pages created:** none
  - **Summary:** 8 Claude Code sessions, 82 user messages, 425 assistant responses, 1092 tool calls, 105 files created, 38 commits. Sessions include: wiki README creation, CLAUDE.md init, KB audit sprint (Apr 13), Brain system audit (Apr 14). Captures the burst of KB infrastructure work this week.

**Pages created (4):** [[wiki/meetings/2026-04-15-teams-daily-ops]], [[wiki/people/renee-simmons]], [[wiki/people/adam-maxon]], [[wiki/concepts/seo-implementation-plan]]

**Pages updated (8):** [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/abiodun-solomon]], [[wiki/moil/product-roadmap]], [[wiki/moil/customers]], [[MEMORY]], [[index]]

**Key intelligence from Run 8:**
1. **API cost crisis:** OpenAI token spend exploded 3x — full audit + migration to gpt-5-mini ordered
2. **License distribution push:** 5 clients getting Moil 360 invitations today (Megan, Mark, Becky, Roxana, Jill)
3. **FitLogic Friday deadline:** Must complete by Apr 18
4. **Astra Restaurant meeting confirmed:** Daniel Guadiano, Thu Apr 16
5. **Career Day May 7:** Renee Simmons, Hays CISD — new community channel
6. **Pflugerville Mentor Day:** Adam Maxon — new market adjacent to Austin/Buda
7. **SEO crisis quantified:** Only 13/68 pages indexed; JobPosting schema = highest-ROI fix
8. **Team delivery tension:** Andres issued direct accountability message to entire team
9. **Buda EDC product call:** EDC reached out to discuss product — may relate to Board vote outcome
10. **9-month email confirms relationship map:** Top contacts all match existing wiki pages; no major gaps

**Summary:** Run 8 processed 7 files. The Teams daily ops was the highest-signal source — an API cost crisis requiring immediate action plus a license distribution push across 5 clients. The SEO implementation plan is a significant new concept page documenting moilapp.com's technical debt. Email digest surfaced two new community contacts (Renee Simmons, Adam Maxon) and confirmed the Daniel Guadiano/Astra meeting for Thursday. The 9-month email history confirms the existing relationship graph with no major gaps.

---

### [2026-04-16] Run 9 — Email Digest Apr 15

**Trigger:** Automated scan for unprocessed raw files. One new file: `raw/email-digest-2026-04-15.md` (committed Apr 15 by `email-digest` job, not yet ingested into wiki).

---

- **File:** raw/email-digest-2026-04-15.md
  - **Type:** email-digest (24-hour window, Apr 14–15)
  - **Pages created:** [[wiki/people/joseph-arnke]] (GIS WebTech; added Andres to Buda EDC AI-tools call)
  - **Pages updated:** [[wiki/people/john-costilla]] (EDC AI-tools call follow-through; status bumped archived → active), [[wiki/people/jesutomilola-omoniyi]] (reply overdue — 2 Apr 15 follow-ups), [[wiki/people/jacob-centeno]] (partnership signal — volunteered referrals), [[wiki/people/jacquie-martinez]] (sent Cohort 4 onboarding email Apr 15), [[wiki/people/rosemary-gamez]] (Rise & Shine thank-you; status archived → active), [[wiki/orgs/buda-edc]] (EDC AI-tools call section added), [[wiki/moil/gtm]] (Apr 15 outbound update + EDC product-expansion channel), [[MEMORY]] (Jesutomilola reply + EDC AI-tools call actions; pruned 2 stale Open-PR items), [[index]] (stats refreshed)

**Key intelligence from Run 9:**
1. **Buda EDC AI-tools call emerging (Apr 15):** John Costilla emailed "Call today"; Joseph Arnke (GIS WebTech, joe@giswebtech.com) added Andres to the invite. Direct follow-through on John's Apr 10 "Agentic AI / always-on site selector tool" signal. Potential B2G product-expansion channel — embed Moil AI in EDC website infrastructure, replicable to other EDCs.
2. **Google xWF relationship at risk of stalling:** Jesutomilola Omoniyi sent two follow-ups in one day ("Let's connect by phone or chat — email not best way"). Reply is now overdue and relationship value (Google Cloud credits parallel to Nvidia Inception) is non-trivial.
3. **Jacob Centeno → referral partner:** Existing $15/mo customer volunteered Apr 15 to refer businesses needing social-media + Moil help. First customer-turned-channel signal.
4. **Rise & Shine attendance confirmed:** Andres attended Greater Buda Chamber's Tuesday Apr 14 event at The HIVE. Rosemary Gamez sent thank-you Apr 15. Buda Chamber relationship is live (was previously marked archived).
5. **Jacquie Martinez — Cohort 4 onboarding live:** Sent "Your Cohort Journey Begins Soon" email Apr 15. Cohort 4 launch (Apr 20) is actively being staged.
6. **Outbound single-day record:** 25 sent emails Apr 15 — 8 breakup emails (first large pipeline-hygiene batch), 4 discovery, 5 pitch, plus meeting invites to Roxana and Megan. Massachusetts expansion (6 new targets) — first MA push in the cold campaign.
7. **Dead ends logged:** Sherese D. James-Grow (Boca Chamber) redirected — only handles teens.
8. **Tax/personal admin not promoted:** DLC Financial (Austin Duke, Brendan C. Dunaway) tax return + Mariana Rodriguez questionnaire forward — personal admin, no wiki pages created.

**Summary:** Single-file digest run. The highest-signal item is the Buda EDC AI-tools-for-website call — a concrete product-expansion opening that directly extends the existing B2G relationship and, if it lands, replicates as a template. Second-highest: the Google xWF (Jesutomilola) relationship needs a reply to avoid stalling. One new person page (Joseph Arnke), six people updated, two stale "archived" people (John Costilla, Rosemary Gamez) reactivated based on current contact.

---

### [2026-04-17] Run 10 — Weekly compile + email digest Apr 16

**Trigger:** Weekly KB compile. One new raw file detected: `raw/email-digest-2026-04-16.md` (committed Apr 16 by `email-digest` job). Meta-reference file `raw/brain-knowledge-layer-analysis.md` also noted; no wiki content ingested — superseded by existing [[wiki/concepts/llm-knowledge-bases]] and [[wiki/concepts/brain-architecture]].

- **File:** raw/email-digest-2026-04-16.md
  - **Type:** email-digest (24-hour window, Apr 15–16)
  - **Pages created:** [[wiki/people/mayra-adams]] (Helotes EDC exec secretary / schedule gatekeeper)
  - **Pages updated:** [[wiki/people/katherine-silvas]] (call locked Wed Apr 22 @ 10am CT; status warm → active), [[wiki/orgs/helotes-edc]] (Apr 22 call added to engagement timeline; status warm → active), [[wiki/people/john-costilla]] (Apr 16 EDO professional-association forward from Katie Milton Jordan), [[wiki/people/jesutomilola-omoniyi]] (source ref added; reply still overdue), [[wiki/people/jacob-centeno]] (last_contact bump), [[wiki/moil/gtm]] (Apr 16 single-day outbound: ~25 emails across narrative-pitch template + second breakup wave; GA/MI/MS/CT/ON/TX clusters), [[MEMORY]] (Helotes "reply overdue" auto-resolved + Apr 22 call action moved to Next 2-3 weeks; Jacob Centeno referral partnership logged; Daniel Guadiano Apr 16 meeting struck), [[index]] (escaped-pipe wikilink fixed: `wiki/moil/directory\|Directory` → `wiki/moil/directory|Directory`)

- **File:** raw/brain-knowledge-layer-analysis.md
  - **Type:** meta-reference (Brain gap analysis vs Shann Holmberg's two-layer AI Knowledge Layer framing)
  - **Pages created:** none
  - **Summary:** Self-reflective gap analysis against @shannholmberg's framework. Maps Brain against four commands (`/wiki-ingest`, `/wiki-query`, `/wiki-explore`, `/wiki-lint`), identifies Web Clipper as the top missing piece, and proposes a morning-ingest automation. Largely superseded by the existing [[wiki/concepts/llm-knowledge-bases]] (Karpathy pattern) + [[wiki/concepts/brain-architecture]]. Content is an improvement roadmap for the Brain itself — not external knowledge to ingest. Logged only.

**Weekly compile outputs:**
1. **MEMORY.md priority rot cleanup:** Helotes EDC item in "🔥 Immediate — This Week" (Mar 31 date-label, 17 days old → >14-day rule) auto-resolved to Closed/Archive; replaced with Apr 22 call action in "Next 2–3 weeks". Daniel Guadiano Apr 16 meeting struck (past). Jacob Centeno referral partnership added to "Next 2–3 weeks". Last-updated date bumped to 2026-04-17. MEMORY.md now 204 lines (vs 200-line soft cap — trim next compile).
2. **Wiki freshness audit:** Zero pages with "Last updated" > 60 days AND zero inbound wikilinks. 17 pages lack a "Last updated" field (READMEs, index). No pages tagged `stale: true`.
3. **Link integrity (index.md):** 54 unique wikilinks scanned. 1 structural break fixed (escaped-pipe on `wiki/moil/directory`). 1 false-positive (`[[wiki/folder/slug]]` example text). All other index.md wikilinks resolve to existing files.

**Key intelligence from Run 10:**
1. **Helotes EDC call locked:** Wed Apr 22 @ 10am CT. Kate Silvas looped in [[wiki/people/mayra-adams|Mayra Adams]] as scheduler. Second EDC incubator partnership moving from "strategic planning" to concrete proposal.
2. **Outbound narrative-pitch template now in rotation:** "Something we didn't expect" / "Interesting feedback from an EDC" sequence (Dylan Horne, Ralph Staffins, Stacy Bowerman, Nancy Palmer) running in parallel with breakup cadence — first deliberate A/B signal in the cold campaign.
3. **Jacob Centeno referral channel = new GTM lane:** Customer-turned-referral-partner confirmed by Apr 16 thank-you reply. First codified customer-as-channel.
4. **Geographic footprint expanding:** Apr 16 push touched Ontario (Canada), Connecticut, Michigan, Mississippi, Georgia — breakup batch targeting Moil's weakest-engagement regions.
5. **KB health is strong:** 0 stale orphans across 241 pages. All "Last updated" fields within the last 60 days — the daily digest loop is doing its job.

---

### [2026-04-17] Run 11 — KidsGPT / Luna Brain planning docs

**Trigger:** Automated scan for unprocessed raw files. Found 3 unprocessed files in `raw/KidsGPT/` (planning docs for Andres's personal family-AI project — flagged in [[wiki/projects/magical-reading-adventures]] as unpromoted) plus 10 `.txt` files in `raw/onedrive-transcripts/` that are actually binary MP4 recordings misnamed with `.txt` extension (not ingestible as text; skipped and logged below).

**Files processed:**

- **raw/KidsGPT/README.md** (1.4 KB) — Luna Brain one-pager
- **raw/KidsGPT/options-analysis.md** (6.8 KB) — Five architecture options for the family-AI companion
- **raw/KidsGPT/implementation-plan.md** (23 KB) — Full phased build plan (Weeks 1–7+), Supabase schema, system prompts, cost model

All three frontmatters marked `ingested: true` / `ingested_at: 2026-04-17`.

**Pages created (1):**
- [[wiki/summaries/kidsgpt-planning-2026-04]] — structured summary of the three planning docs

**Pages updated (3):**
- [[wiki/projects/lunabella]] — replaced the one-paragraph stub with full Luna Brain project page (architecture, naming ceremony, bilingual design, safety model, phase roadmap, cost model, Supabase schema, curriculum intelligence — all sourced from `raw/KidsGPT/`). Confirmed `Felipeu28/Lunabella` GitHub repo = the Luna Brain engineering surface ("Lunabella" = Luna + Annabella)
- [[wiki/projects/magical-reading-adventures]] — closed the "is this KidsGPT?" open question; now links forward to [[wiki/projects/lunabella]] as the destination of the KidsGPT concept
- [[wiki/moil/active-projects]] — Tier 3 row updated: "KidsGPT concept / Raw files not yet promoted" → "Luna Brain (Lunabella) / Phase 1 building"

**Key intelligence:**
1. **Luna Brain is one app, two profiles** — Annabella (age 7) and Evie (age 5), each with separate brains, separate Lunas, separate curricula. Not a prototype — per-profile scoping is baked into the Supabase schema from Day 1.
2. **Stack locked:** React/Vite + Fastify + Supabase + Claude `claude-sonnet-4-6` + ElevenLabs + ntfy.sh + Resend. Deploys on Vercel (frontend) + Railway (API). iPad-first portrait.
3. **Architectural parallel to the Moil Brain:** Same two-layer memory model — episodic transcripts → semantic knowledge graph. End-of-conversation ingestion (not per-message) mirrors how the Moil Brain ingests raw sources.
4. **Safety model uses Claude specifically** because it carries a Minimal Risk rating for kids (vs GPT's High Risk per the options-analysis). Hard-block topics route to "ask your parents" and push-notify Andres via ntfy.sh within 60s.
5. **Bilingual (EN + ES) is foundational, not bolt-on** — system prompt auto-detects language, code-switches naturally, brain-node schema has `label_en` + `label_es` with topic collapsing ("espacio" = "space" = same node). "Practice Spanish" parent override planned.
6. **Curriculum intelligence (Phase 4, Weeks 5–6)** is the most distinctive feature — Andres uploads the school curriculum PDF once per school year per profile, Claude parses it to structured JSON, Luna's system prompt gets a confidential reference block, parent dashboard gains a coverage map + gap prompts ("Try asking Luna about multiplication — Annabella hasn't touched it yet"). School-year-end report visualizes natural curiosity vs. required curriculum.
7. **Cost model:** ~$15–20/month. Fits comfortably inside Andres's existing Anthropic billing.
8. **Status as of 2026-04-15:** `Felipeu28/Lunabella` TypeScript repo is active, last push 2026-04-15. Planning phase is complete. Next unblocks: Supabase project creation, ElevenLabs API key, domain decision.

**Skipped files (unprocessable):**

- `raw/onedrive-transcripts/kim-dowers-intro-call-2026-02-09.txt` (685 KB)
- `raw/onedrive-transcripts/life-after-cohort-moil-2026-02-10.txt` (9.1 MB)
- `raw/onedrive-transcripts/life-after-cohort-moil-2026-02-13.txt` (25 MB)
- `raw/onedrive-transcripts/moil-marketing-call-2026-03-11.txt` (1.4 MB)
- `raw/onedrive-transcripts/moil-team-meeting-2026-01-29.txt` (4.8 MB)
- `raw/onedrive-transcripts/moil-team-meeting-2026-03-27.txt` (6.3 MB)
- `raw/onedrive-transcripts/rashaka-boykins-intro-call-2026-02-27.txt` (1.4 MB)
- `raw/onedrive-transcripts/rashaka-boykins-intro-call-2026-03-05.txt` (1.5 MB)
- `raw/onedrive-transcripts/roxana-esquivel-intro-call-2026-03-13.txt` (4.7 MB)
- `raw/onedrive-transcripts/travis-&-andres-moil360-2026-04-09.txt` (1.5 MB)

All 10 files have MP4 `ftypisom` binary headers — they are raw video recordings from OneDrive that were misnamed with a `.txt` extension, not textual transcripts. Cannot be ingested as-is. **Recommended action:** either run them through Groq Whisper / the `scripts/teams_pull.py` style pipeline to produce actual `.md` transcripts before re-dropping, or rename to `.mp4` and move them outside `raw/` (they don't belong in a text-ingestion directory).

**Summary:** Run 11 promoted the long-flagged `raw/KidsGPT/` files into the wiki as a first-class personal project ([[wiki/projects/lunabella|Lunabella]]). Two cross-page open questions closed in the process (magical-reading-adventures's "is this KidsGPT?" and active-projects.md's "raw files not yet promoted"). Also surfaced a raw/ hygiene issue — 10 binary MP4 files pretending to be `.txt` transcripts in onedrive-transcripts/ need to be either transcribed or moved out of the raw/ directory.

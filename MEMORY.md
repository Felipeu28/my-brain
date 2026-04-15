# MEMORY — Open Actions & Live Commitments

**Last updated:** 2026-04-14 (pruned stale May 2025 + Oct 2024 historical items)
**Purpose:** Single source of truth for open action items extracted from ingested raw sources. Claude Code updates this file during ingestion runs.

> For relationship and concept context, see [[index]]. For ingestion history, see [[log]].

---

## 🧹 Review rhythm (keeps MEMORY.md from rotting)

| Cadence | Action |
|---|---|
| **Weekly (Friday, 15 min)** | Walk through every `[ ]`. Strike `~~done~~` with date. Move items stale >2 weeks to "Closed / Archive". Add new actions from the week's iMessages/Outlook pulls. |
| **Monthly (1st of month)** | Prune "Closed / Archive" — keep only items useful as precedent; delete the rest. Reconcile deferred items against the current week. |
| **Quarterly** | Full audit: does every open item still matter? Kill anything that no longer serves a live goal. |

**Hard rule:** if MEMORY.md exceeds 200 lines, pruning is overdue. Don't let it drift.

**Closing an item:** use `~~strikethrough~~` + `(YYYY-MM-DD)` inline. After a week, move the whole bullet to "Closed / Archive". After a month, delete unless it's a useful precedent.

---

## 🔥 Immediate — This Week (Apr 11–17, 2026)

### Helotes EDC — reply overdue
Source: [[wiki/orgs/helotes-edc]], [[wiki/people/katherine-silvas]]
- [ ] **🔥 Overdue reply** — Katherine Silvas (CEO, Helotes EDC) emailed Mar 31 asking to include Moil in the Helotes incubator strategic plan. That's 15 days unanswered. Respond and schedule the Board conversation.
- [ ] Prep Buda EDC case study + pricing sheet as reference model for the Helotes proposal.



### Buda HIVE / EDC — dual Apr 15 deadline
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [ ] **Apr 14 · 10:30am–12:00pm CDT** — Prep meeting with Joshua Edmond at Buda HIVE (Teams ID 270 650 313 421 234). Coordinate final stance before Board review.
- [ ] **Apr 15** — EDC Board vote on Incubator Strategist contracts (Moil Enterprises Inc. + FAVE&SAVE LLC). Be available for questions/revisions.
- [x] **Apr 15** — AEDO letter submission — ~~SIGNED & SUBMITTED Apr 10~~ (Jennifer Storm: "This is perfect!")
- [ ] **Apr 20 → Jun 8** — Cohort 4 begins (every Monday). Prep session materials. [[wiki/people/casey-earley]] is a participant.

### Product UX bug — applicant visibility
Source: [[wiki/summaries/imessages-people-2026-04-09]] (Megan Miller feedback)
- [ ] Fix gap: employer cannot see applicant phone/email in Moil. Unclear notification system when candidate messages via Moil.
- [ ] Reply to Megan Miller with a short-term workaround + ETA.

### Open PRs (code hygiene)
Source: [[wiki/summaries/github-project-tracker]]
- [ ] Review + merge PR on `Moil-Code/Blog`
- [ ] Review + merge PR on `Moil-Landingpages/Inna-CRM`

---

## 📅 Next 2–3 weeks (Apr 18 – May 2)

### Travis Sutherland — Sun Show demo
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] **Apr 24 · 7–9pm** — Moil demo booth at the Sun Show. Set up screen + flyers. Confirm logistics with Travis.

### Daniel Guadiano — Astra Restaurant
Source: [[wiki/summaries/outlook-emails-2026-04-09]]
- [ ] Reply to Daniel (Apr 9 inquiry). Offer a 30-min scheduling demo tailored to restaurant ops. Phone 210.978.4483.
- [ ] If it closes, write a restaurant case study — first hospitality ICP data point.

### Inna Benyukhis — Calendly
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] Confirm meeting slot: **Mon Apr 13 10am** or **Friday after 2pm**. In-person, 60 min.

### Mark Polanco — Airtable access
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] Airtable invite hadn't arrived as of Apr 9. Follow up if still blocked.

### Ana Vetencourt — URBANZUELA website
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [ ] Review the Google Doc draft Ana sent. Provide feedback.

### John Costilla — Apr 10 photo shoot
Source: [[wiki/summaries/imessages-people-2026-04-09]]
- [x] **Apr 10 · 10:15am** — Photos with John. ~~Presumed done~~ (today is Apr 11; verify + archive if complete)

---

## 🔔 New from Teams ingestion (2026-04-12) — 415 messages, Apr 5–12

Source: [[wiki/summaries/teams-2026-04-12]]

### Roxana / AlloyATX — onboarded Apr 14
Source: [[wiki/meetings/2026-04-14-roxana-alloy-atx-onboarding]]
- [ ] **Apr 15** — Andres: send post-call summary to Roxana
- [ ] **Apr 17** — Andres + Roxana: brainstorm satellite landing page domains
- [ ] **Apr 18** — Roxana: complete 21 strategic questions (then Andres runs market research)
- [ ] **Apr 18** — Roxana: upload assets to Teams shared folder + share GoDaddy domain list
- [ ] **ASAP** — Roxana: email Shannon for full social media + asset handover
- [ ] **Next session** — Andres: set up Google Search Console for alloyatx.com
- [ ] **After market research** — Andres: SEO audit + Q&A recommendations per page
- [ ] **Wellness referrals:** Roxana has functional medicine + Colombia regenerative medicine contacts — follow up after onboarding stabilizes

### Deals requiring follow-up
- [ ] **Connectex:** Invoice sent? Verify payment schedule (3 quarters). What deliverables?
- [x] ~~**Alloy (gym):** Confirm closing~~ (2026-04-14) — CLOSED. Moil 360 Market Pro $75/mo. See [[wiki/meetings/2026-04-14-roxana-alloy-atx-onboarding]]
- [ ] **FitLogic:** Confirm hire. Update job posting (part-time → part-time-to-full-time done by Jacob). Track as customer win
- [ ] **jilledegs01@gmail.com:** Site deployed (pure-serenity-green.vercel.app). Moil 360 license sent by Jacob. What changes needed?
- [ ] **Siren Beauty:** Account setup — does she have an account yet? (Jacob asked to check)
- [ ] **Eden:** Website discovery call recorded Apr 8. Follow up on next steps

### Product/Engineering — immediate
- [ ] **Tour guide bugs STILL OPEN:** 2 missing `data-guide-id` attributes (`dashboard-welcome-header`, `profile-badge`). Generic waiting text. Auto-scroll too aggressive
- [ ] **Segment analytics:** `No segment writeKey` error on staging. Fix or remove
- [ ] **Image context bug:** Images "forget" conversation context. Root cause?
- [ ] **Qwen model monitoring:** Adeleke has reminders for Tuesday + Friday to check free tier exhaustion
- [ ] **Model cost audit:** Where exactly is GPT-5.4 being called? Andres investigating. Switch to Grok 4.1 Fast where possible
- [ ] **Supabase deploy:** `supabase functions deploy business-intake` from Business-plan-Staging/ needed for go-live
- [ ] **Meridian email:** Domain verification blocking email resend. Taiwo needs this resolved
- [ ] **Meridian Stripe:** Test keys configured; need to test full flow end-to-end
- [ ] **Phone number sign-up:** Removed from site (Azure verification broken). Needs permanent fix or formal removal

### Content/Marketing
- [ ] **Inna May calendar:** Pre-loaded by Andres. Ensure Ablad has it and delivery stays on track
- [ ] **Content calendar CSV process:** Always export CSV before importing new data (adopted after Apr 1-8 content loss)
- [ ] **Video production strategy:** Andres asked "How can we start producing video daily?" — needs a plan using AI video tools
- [ ] **Buda community sharing:** Restarted — "Only Buda groups please." Track engagement
- [ ] **Sun show attendee email:** "One of you won a free year of Moil 360" — was this sent?

### Team management
- [ ] **Jacob power outage:** 3 weeks, damaged cable on street. Running on generator fuel. Andres sent $50. Monitor if this affects output
- [ ] **Adeleke FB account:** Login code issue since Apr 7. Blocking app review video recording
- [ ] **Taiwo productivity:** Andres frustrated by credential-waiting passivity. "6 projects, never let a full day go by waiting." Monitor improvement
- [ ] **Microsoft Planner:** Jacob created board Apr 7. Verify team is using it (In Progress / In Review statuses)

### Security/Credential hygiene
- [ ] **Credentials in Teams chat:** Stripe keys, Supabase passwords, Gemini API key, FB codes all shared in plaintext. Migrate to a secure credential store (1Password, Bitwarden, or at minimum a pinned secure note)

---

---

## 🎯 Monthly — Brain System hygiene

Source: [[wiki/summaries/brain-guide]] / [[wiki/concepts/brain-architecture]]
- [ ] Confirm Monday 9am X bookmark sweep is scheduled in Claude Cowork (Collection layer).
- [ ] Consolidate duplicate bookmark files — [[wiki/summaries/x-bookmarks-2026-04-11]] (114) vs [[wiki/summaries/x-bookmarks-2026-04-11-copy]] (129). Prefer the 129 version for future synthesis.
- [ ] Write `MOIL.md` context file (Mission / Operating Principles / Identity / Legacy) and seed as primer for major Claude queries.
- [ ] Run Prompt 1 (Claude) from [[wiki/summaries/know-me-extraction-prompts]] → produce first `andres-intelligence-brief-[date].md` → drop in `raw/` → ingest.
- [ ] Monthly Layer 4 synthesis: feed 4 most-recent bookmark digests to Claude for patterns & belief shifts. Output → `outputs/synthesis-YYYY-MM.md`.

---

## 💤 Deferred — Calendar reminders

### Shay Foley / Johns Creek Chamber
Source: [[wiki/summaries/outlook-emails-2026-04-09]], [[wiki/people/shay-foley]]
- [ ] **Jul 1, 2026** — Re-engage. Pitch AI tools for entrepreneurs using Buda EDC as reference customer + Jennifer Storm AEDO-grade endorsement. Chamber budget year starts this day.

### CampaignOS with Jennifer Storm
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]], [[wiki/concepts/campaignos]]
- [ ] After Apr 15 deadlines clear, circle back on MVP scope. Andres offered "little to no cost" — decide commitment level before building.

### CoffeeSpace partnership
Source: [[wiki/summaries/outlook-emails-2026-04-09]], [[wiki/orgs/coffeespace]]
- [ ] Low priority. Nurture. Only book a call if calendar is light and Moil's candidate platform is ready for distribution partners.

### Training program curriculum (Buda HIVE)
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [ ] **Sep 1, 2026** deadline (per Joshua's contract). Jointly develop with HIVE + Incubator Strategist Team.

---

## 🏗️ Strategic — No hard deadline but worth deciding

### Fantelo clarification
Source: [[wiki/concepts/fantelo]]
- [ ] Decide: is Fantelo a future pivot, separate venture, or sub-brand of Moil? Currently consumes engineering time (private repo pushed Apr 9) with no wiki-documented strategy.

### ~~Moil360 vs Content360 naming~~ (2026-04-14)
Source: [[wiki/concepts/moil360]], [[wiki/concepts/content360]]
- [x] **2026-04-14** — Resolved: Moil360 is canonical. Content360 deprecated to a redirect stub. 20 references in operational docs (pipeline, customers, gtm, product-roadmap, positioning, metrics, icp, alloy-atx) updated. Historical summaries/meetings preserved as-is.

### GitHub org cleanup
Source: [[wiki/summaries/github-project-tracker]]
- [ ] Archive 6+ stale repos (Moil-landing-beta, New-Prod-Landing, Moil-codeLandingPage, Moil-nextjs-landing, Mailing-service, flaskModelStaging, model-server-flask).
- [ ] Dedupe BlueprintsForSuccess / Blueprintforsuccess.
- [ ] Consider creating a fourth org `Moil-Clients` and moving queen-creek, buda-hive, KyleBudaSpotlight, REFERREDLOCAL, omaha-client-boost, connectex-website there.
- [ ] Standardize naming convention (kebab-case lowercase).

### Moil license case study
Source: [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [ ] Build a public case study: "City EDC × Moil — per-seat licensing for incubator cohorts." Use for investor decks and expansion to Queen Creek / Johns Creek / Greater Buda Chamber.

### Claude Code security audit
Source: [[wiki/concepts/claude-code]]
- [ ] Review what permissions Claude Code has on the Mac Mini M4 (SSH config, AWS creds, `.env` files). Decide boundaries before running autonomous skills.

---

## ✅ Closed / Archive

*(Items move here after they're marked complete and confirmed stable for a week. Historical items older than a month live in [[log]] instead.)*

- [x] **2026-04-10** — AEDO support letter drafted, signed, submitted to Jennifer Storm. Reply: "This is perfect!" — source: [[wiki/summaries/buda-hive-edc-2026-04-11]]
- [x] **2026-04-14** — Data-quality cleanup: 38 duplicate raw files removed, escape-broken wikilinks fixed, index.md stats corrected. May 2025 historical archive moved to [[log]] — see "Archive — May 2025 historical verify items" block.

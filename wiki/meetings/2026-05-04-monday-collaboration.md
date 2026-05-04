---
tags:
  - graph/leaf
date: 2026-05-04
type: meeting
attendees:
  - "[[wiki/people/adeleke-tolulope]]"
  - "[[wiki/people/taiwo-ola-balogun]]"
  - "[[wiki/people/jacob-oluwole]]"
  - Andres Urrego
  - Ablad
---
# 2026-05-04 — Monday Collaboration: AI cost discipline + product unification

**Type:** meeting (Teams, 52 min, 2 segments)
**Time:** 7:52 AM – 8:44 AM CT (12:52–13:44 UTC)
**Source:** [[raw/teams-transcript-monday-collaboration-2026-05-04]]
**Related:** [[wiki/people/adeleke-tolulope]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/jacob-oluwole]], [[wiki/moil/active-projects]], [[wiki/moil/product-roadmap]], [[wiki/orgs/fitlogic]], [[wiki/orgs/connectex]], [[wiki/orgs/siren-beauty]]

---

## Context

Weekly Monday collaboration after the [[wiki/meetings/2026-04-29-megan-fitlogic-crm-delivery|FitLogic delivery]] (Apr 29) and the [[wiki/meetings/2026-04-28-mark-polanco-connectex-walkthrough|ConnectX walkthrough]] (Apr 28). Andres opens with: *"Long are the days where we were scared to commit to anything for today"* — meaning the AI-assisted dev velocity now lets the team turn around requests in minutes/hours that used to take ~3 weeks. He's applying to another accelerator today. Andres had to leave at 8:44 AM CT for a 9:30 meeting.

Three threads:
1. **Cost discipline (Gemini, OpenAI, Groq, Grok).** Live walk-through of the dashboards. Saturday Gemini spike root-caused.
2. **Product unification.** Combine FitLogic / Inna CRM / Siren Beauty / ConnectX into a single packaged product Moil can resell.
3. **Free-trial rollout.** First 30 days free for all new Moil signups; Andres owns the matching marketing strategy.

## Key decisions

1. **Cost discipline standing rule:** before pushing any new backend feature, ask *"is this the most cost-efficient model that still does the job?"* Andres wants this question asked every time
2. **Switch backend Gemini calls from 2.5 Pro → 2.5 Flash Lite** for the weekly health-summary cron and similar non-agentic jobs. Adeleke confirmed he'll change them now
3. **Gate the weekly health-summary cron on activity** — skip users with no activity in the past week; send a re-engagement nudge (*"any questions I can answer?"*) instead of burning tokens summarizing nothing. Same applies to the 7–14 day inactive bucket
4. **Roll out free 30-day Moil trial to all new users.** Andres owns the matching marketing strategy
5. **Consolidate Taiwo's side-projects** ([[wiki/orgs/fitlogic|FitLogic]], [[wiki/people/inna-benyukhis|Inna CRM]], [[wiki/orgs/siren-beauty|Siren Beauty]], [[wiki/orgs/connectex|ConnectX]]) into one packaged product Moil can resell. Three pillars: email-sequence tool, blog generator, CRM
6. **Investigate open-source email-infrastructure project** Taiwo found as a Resend replacement (clone + bring own infra; lifts the 100 emails/day cap). Small-scale only — appropriate at current SMB customer profile
7. **Weekly Monday cost review** is a standing agenda item going forward

## Action items

### Steve / Adeleke
- [ ] Assign Taiwo a Moil 360 license today so he can dogfood the business coach
- [ ] Change weekly summary cron model from Gemini 2.5 Pro to 2.5 Flash Lite. Tag Andres in the chat with the screenshot/cost comparison before pushing
- [ ] Add active-user gate to weekly health-summary cron; skip inactive users, send re-engagement email instead

### Taiwo
- [ ] Share the open-source email-infrastructure project link with the team
- [ ] Continue auditing FitLogic / Inna CRM / Siren Beauty / ConnectX; design the unified packaged tool. Sanity access for Siren Beauty is still blocked — request was sent
- [ ] Once Moil 360 license is granted, dogfood the business coach during reading sessions and push it on edge cases

### Andres
- [ ] Draft 30-day marketing strategy for the free-trial rollout (Moil 360 first 30 days free)
- [ ] Apply to the accelerator today; lead with **license-sales traction** (not website creation)
- [ ] Resolve credit-card issue blocking Groq/Gwen refills

## Color

- **OpenAI refunded $30 on 2026-05-03** (credit note 3937) after the suspicious-charge dispute. Account unlocked
- **`Moil-Dev` Gemini project** (key ending `0270710133`) was reinstated after a no-payment threat email. The other Gemini key (`0251`) is the live one and untouched. The `0133` key handles Google auth — confirms the Apr 29 [[wiki/people/adeleke-tolulope|Adeleke]] AI-spend block in [[MEMORY]] is now partly resolved
- **Saturday (2026-05-02) Gemini spike** root-caused: a weekly health-summary cron iterates every user's chats to compress + draft email actions. Switching the cron to 2.5 Flash Lite (and gating on activity) is the immediate fix
- **April Groq spend was $7. Two-week Gemini spend ~$10.** Andres' bar: ~$2/day max per service is healthy at current user count
- **Self-correction live on the call:** Andres notices the team paid $30 for ChatGPT 5 when GPT-4o-mini would have done the job. *"It doesn't have to be always the cheapest, it just has to make sense"* — adopted as the working rule
- **Product framing for the accelerator pitch:** *"I'm not going to lean on the website-creation thing yet. I'm going to sell them as licenses. People are buying licenses."* — explicit decision not to lead with the website-builder narrative even though it's the inbound demand
- **Email infra:** Taiwo found an open-source project that handles full email-sending infrastructure (domain setup, all of it). Plan: clone, bring own infra, eventually replace Resend. Useful for the unified product packaging
- **Andres' framing of where Moil is going:** *"All of this has to be agents. We can't be doing this work."* — when funding allows, the team should run mostly off agents and the consulting/build work becomes packaged
- **The "I'm gonna build the lead-gen tool, the blog tool, the CRM tool, then combine the best parts"** ambition was raised but not scoped. Tracked under the unified-product item — Andres wants Taiwo to lead a full audit

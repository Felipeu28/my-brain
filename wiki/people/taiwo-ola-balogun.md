---
status: active
last_contact: 2026-04-20
tags:
  - graph/spoke
  - person/team
---
# Taiwo Ola-Balogun

**Type:** person
**Last updated:** 2026-04-20
**Source:** [[raw/meetings/]] (multiple meeting transcripts), [[raw/teams-2026-04-12]] (415 messages, Apr 5–12 2026), [[raw/teams-transcript-monday-collaboration-2026-04-13]], [[raw/teams-2026-04-15]] (84 messages, Apr 14–15 2026), [[raw/teams-2026-04-18]] (51 messages, Apr 17–18 2026), [[raw/teams-2026-04-20]] (36 messages, Apr 19–20 2026)
**Related:** [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]], [[wiki/moil/product-roadmap]]

---

## Role

**Frontend Engineer at Moil** — handles frontend code and assists with AI model training data creation (frontend codebase). Present in all major team meetings.

## Background

Nigerian team member (same remote team cohort). Present since Jan 2025. Works closely with Adeleke on the engineering side.

## What He Does

- Creates dataset for frontend code fine-tuning (parallel to Adeleke's backend work)
- Implements UI code from Ablad's designs
- Assists with sign-up page redesign, business plan creator implementation
- Suggests and implements UX improvements (e.g., textarea > input fields, mobile bottom bar cleanup)
- Uses Google Gemini for rapid development / code generation
- Designs business plan creator welcome screen when needed

## Key Contributions

| Date | Contribution |
|---|---|
| Jan 2025 | Frontend codebase dataset for AI model training |
| Mar 2025 | Sign-up page simplification implementation |
| Apr 2025 | Business plan creator textareas fix (1-2 hour task) |
| Apr 2025 | Business plan creator welcome screen design |
| May 2025 | Using Gemini for AI-assisted code generation |

## Personality in Meetings

- Thoughtful — defines "iteration" clearly when asked ("adding or removing aspects from software or hardware, then continuously improving through testing")
- Sometimes suggests alternative approaches before Andres overrules (good engineering instinct)
- Slower to adapt than Andres wants but receptive to feedback

## April 2026 Activity (from Teams chats, Apr 5–12)

**65 messages in 1:1 with Andres.** Taiwo is the primary developer on the **Meridian** project (event management platform for Buda).

### Work completed this week:
- Pushed changes to `taiwo/finish` branch for Meridian
- Set up Stripe integration (test keys shared by Andres: `pk_test_51TK0I2...`, `sk_test_51TK0I2...`)
- Webhook URL configured: `https://meridian-buda.vercel.app/api/webhooks/stripe`
- Working on organizer dashboard: email-based link to unlock organizer view with event stats and check-in functionality
- Identified domain verification issue blocking email resend functionality
- Ran Supabase migration (needed access credentials)
- Deployed changes Apr 11 (network issues delayed testing)

### Technical issues surfaced:
- Gemini model quota exceeded (Apr 8)
- Supabase anon key is legacy standard — flagged that publishable key is the new standard
- Domain verification blocking email sending
- Network connectivity issues (bad network, missed calls)

### Key design decisions:
- Ticketed events should NOT overlap (no multiple halls for Meridian)
- Check-in must be done by Meridian (not external)
- Organizer dashboard accessible via email link with stats per event

### Relationship with Andres:
- Andres pushing hard: "Let's get this done today! We have so many other projects"
- Andres frustrated when Taiwo waited for credentials: "We have 6 projects, please let's never let a full day go by just 'waiting' on credentials"
- Taiwo respectful but slower pace; Andres sharing Gemini API key directly in chat
- Credential sharing happening directly in Teams (security concern)

## April 13, 2026 — Monday Collaboration

Three high-priority items from this meeting:

1. **BLOCKER — Meridian Stripe webhook:** Webhook URL not configured — ticket confirmation emails not sending. Taiwo will send the endpoint URL to Andres to add in Stripe's developer section (test account). Cron job secrets in Vercel also using placeholder values, not real secrets.
2. **Client handoff document:** Andres assigned Taiwo to create a structured doc listing everything clients need before project handover — Vercel accounts, Supabase, Resend, login instructions. "Please get this done to me as soon as possible."
3. **New massage place client:** Website nearly done, just needs images. Taiwo to handle handoff process.

See [[wiki/meetings/2026-04-13-monday-collaboration]].

## April 15, 2026 — Meridian Live + FitLogic Access

Source: [[raw/teams-2026-04-15]]

- **Meridian update live** for client testing — confirmed by Taiwo. Guide now stores progress in cookies (fixed the repeated-onboarding bug).
- **Nuovo Entertainment site** deployed at nuovo-enterteinment.vercel.app — Andres reviewing.
- **FitLogic:** Needs Supabase access — project was in Lovable, Andres moving it to Claude. Taiwo will need new credentials.
- Andres pushed FitLogic prod changes and asked Taiwo + Jacob to test. **Deadline: Friday Apr 18.**
- Env variable issue surfaced: Taiwo found Andres had updated environment settings, which affected the project. Taiwo recovered files from Vercel.
- Tested FitLogic changes after Andres pushed to prod.

See [[wiki/meetings/2026-04-15-teams-daily-ops]].

## April 18, 2026 — Demo Fix + Time-Zone Boundary

Source: [[raw/teams-2026-04-18]]

- **Demo "messed up" post-mortem.** Taiwo acknowledged "we 'messed up' the demo" and asked Andres for better business-specific context to add to prompts to generate desirable results. The original context was defined in Lovable and Taiwo couldn't replicate it using the same prompts in the current stack. Andres clarified: the previous code used the business plan as a single source of truth driving everything — current build has regressed from that pattern.
- **Time-zone boundary raised.** First explicit request for scheduling accommodation: "Please setup delivery calls for projects that are not at 11pm or 2am my time! That way we can actually go through the projects before my meetings." Andres acknowledged and echoed the ask to the team.

See [[wiki/meetings/2026-04-18-teams-daily-ops]].

## April 20, 2026 — Re-engaged on FitLogic + Meridian

Source: [[raw/teams-2026-04-20]]

- **Proactively re-engaged** despite the Apr 18 time-zone boundary request: "Good morning sir / Hoping we can go through fitlogic and meridian today" (10:41 AM). Healthy recovery — pushed for the session rather than waiting.
- Asked Jacob to "add me to the call" (4:23 PM) during Monday Collaboration.
- **Personal Gmail disclosed:** `taiwotriumphant@gmail.com` (5:01 PM) — likely for a dev-tool or account invite (context: GitHub, Supabase, or similar tool access, not explicitly stated).
- Andres sent `FitLogic.docx` at 5:57 PM for the walkthrough.

See [[wiki/meetings/2026-04-20-teams-daily-ops]].

## Contact

- Teams: Taiwo Ola Balogun
- Personal Gmail: `taiwotriumphant@gmail.com` (disclosed Apr 20, 2026)

## Gaps

- Full name: Taiwo Ola-Balogun — likely Nigerian Yoruba name (Taiwo = first of twins)
- Location unknown (likely Nigeria)
- Network infrastructure seems unreliable (multiple mentions of bad connectivity)

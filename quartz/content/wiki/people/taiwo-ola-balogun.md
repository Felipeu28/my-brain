---
tags:
  - graph/hub
  - person/team
---
# Taiwo Ola-Balogun

**Type:** person
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/]] (multiple meeting transcripts), [[raw/teams-2026-04-12]] (415 messages, Apr 5–12 2026)
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

## Gaps

- Full name: Taiwo Ola-Balogun — likely Nigerian Yoruba name (Taiwo = first of twins)
- Location unknown (likely Nigeria)
- Network infrastructure seems unreliable (multiple mentions of bad connectivity)

---
tags:
  - graph/spoke
---
# Monday Collaboration — April 13, 2026

**Type:** meeting
**Last updated:** 2026-04-13
**Source:** [[raw/teams-transcript-monday-collaboration-2026-04-13]]
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]], [[wiki/people/abiodun-solomon]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/inna-benyukhis]], [[wiki/orgs/meridian-buda]], [[wiki/people/travis-sutherland]]

---

## Summary

Weekly Monday collaboration call. Andres demoed the Moil Brain to the full team (~30 min). Then covered Inna's 10am meeting prep, PDF/PPTX generation progress, Meridian Stripe blocker, content calendar status, a new massage place client, the Sun Show event, and Google Alloy image testing.

## Attendees

- **Andres Urrego** (host)
- **Jacob Oluwole** (organizer)
- **Adeleke Tolulope** (Steve)
- **Abiodun Adekanmi** (Ablad)
- **Taiwo Ola-Balogun**

## Key Decisions

1. **Brain cloning:** Andres will clone the Brain repo for each team member once the system is stable — everyone gets their own personal "brain"
2. **Content cadence:** Content for the following week must be ready by Friday so Mondays are for strategizing, not catching up
3. **Client handoff process:** Taiwo to create a structured handoff document listing everything clients need (Vercel, Supabase, Resend accounts, login instructions) before project handover

## Action Items

| Owner | Action | Priority | Deadline |
|---|---|---|---|
| **Andres** | Fix client project connectors in KB (FitLogic etc not linking) | Medium | This week |
| **Andres** | Configure Stripe webhook in test mode for Meridian once Taiwo sends endpoint | **HIGH** | ASAP |
| **Andres** | 10am meeting with Inna — review CRM, demo | HIGH | Apr 13 |
| **Taiwo** | Send Stripe webhook endpoint URL to Andres | **HIGH — BLOCKER** | ASAP |
| **Taiwo** | Update Vercel cron job secrets (currently placeholder values) | HIGH | This week |
| **Taiwo** | Create client handoff document (Vercel, Supabase, Resend, login instructions) | HIGH | ASAP |
| **Steve** | Create testing folder in repo branch with reference PDFs for Claude Code iteration | Medium | This week |
| **Steve** | Continue fixing PDF/PPTX formatting issues | Medium | Ongoing |
| **Ablad** | Keep detailed testing notes open while testing Business Coach | Medium | Ongoing (reiterated from Friday) |
| **Jacob** | Start testing Google Alloy image generation inside Moil | Medium | Before Andres's Alloy meeting tomorrow (Apr 14) |
| **Team** | Verify/fix Inna CRM contact pipeline display | HIGH | Before 10am meeting |
| **Team** | Add campaigns API key to Inna's account | HIGH | Before or after Inna meeting |

## Blockers

- **Meridian ticket emails not sending** — Stripe webhook URL not configured. Taiwo has the endpoint, Andres needs to add it in Stripe developer section (test account). Cron job secrets in Vercel also using placeholder values.
- **Inna CRM** — contacts not showing in pipeline; campaigns API key not yet added

## Topic Notes

### Brain Demo
Andres showed the full Moil Brain to the team: 143 nodes, 699 connections, 187 wiki pages, 78 raw sources. Team profiles, customer profiles, org connections, project tracker, visual graph. Ingests transcripts weekly on Fridays plus emails, X bookmarks, meeting data. Taiwo recognized it from an article about Claude + Obsidian. Andres credited Andrej Karpathy's work as inspiration.

### PDF/PowerPoint Generation (Steve)
First test produced output but formatting needs significant work. Logo generated but needs non-colored background version. Steve also pushed staging updates: image creation in Business Coach, monitoring improvements.

### New Client — Massage Place
Website nearly done, just needs images. No name given for client or business. This is one of 12+ active projects.

### Sun Show Event (Next Week)
Moil invited to showcase at a local event (likely [[wiki/people/travis-sutherland]]'s Sun Show). Will have a table to demo Moil products.

### Google Alloy Image Generation
Andres meeting with someone about Alloy (Google image gen) tomorrow (Apr 14). If it works inside Moil, could charge clients without extra work — no additional integration needed.

## Connections

- [[wiki/orgs/meridian-buda]] — Stripe webhook is the last blocker before handoff
- [[wiki/people/inna-benyukhis]] — CRM issues need fixing before/after today's meeting
- [[wiki/concepts/llm-knowledge-bases]] — Brain demo showed the team the Karpathy-inspired system in action
- [[wiki/moil/product-roadmap]] — PDF/PPTX gen, Alloy image gen, Business Coach updates all feed into product roadmap

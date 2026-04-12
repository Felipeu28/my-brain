# Moil Team Operating System

**Type:** concept
**Last updated:** 2026-04-12
**Source:** [[raw/teams-2026-04-12]]
**Related:** [[wiki/moil/metrics]], [[wiki/meetings/teams-attendance-protocol-2026-04]], [[wiki/moil/gtm]]

---

## Summary

Moil runs its internal team on Microsoft Teams with an automated daily synchronization protocol. The operating philosophy is async-first, visibility-driven: rather than daily standups, the team uses a bot-enforced clock-in ritual and written start-of-day status updates. This creates a written record of presence and intent without requiring a scheduled meeting.

## Key Points

- **Platform:** Microsoft Teams (confirmed active as of Mar–Apr 2026)
- **Daily ritual:** Automated Workflow message at 7:00 AM triggers two actions:
  1. Clock-in post in `#attendance-n-break` (`Clocked in – [Name]`)
  2. Start-of-day status in the project thread (`Today: / Blockers:`)
- **Cadence philosophy:** "Skipping this = you're not visible, not aligned, and not in the rhythm of impact." Accountability is framed as a team rhythm, not surveillance.
- **Channels observed:** `#attendance-n-break` (primary team sync), `#Alerts` (purpose unclear from available data)
- **Automation layer:** Microsoft Workflows (Power Automate) used for daily reminders — signals Andres has set up at least basic MS 365 automation infrastructure

## What this tells us about the Moil team

- Team is distributed / remote (async attendance protocol rather than in-office check-ins)
- At least 2+ channels active in Teams workspace
- Moil uses MS 365 ecosystem (Teams + likely Outlook, which aligns with `raw/outlook-emails-2026-04-09.md`)
- The team operating protocol is codified and automated — not ad hoc

## Intelligence gaps

- Actual team roster (names) not visible in this pull — only bot messages captured
- Unknown: does the team actually comply? Compliance rate would signal team health
- Unknown: are there other channels (project threads, client channels, dev channels)?

## Connections

- [[wiki/moil/metrics]] — team health / attendance compliance is a useful operational metric
- [[wiki/meetings/teams-attendance-protocol-2026-04]] — the meeting record where this was first documented
- [[wiki/concepts/brain-architecture]] — Teams is part of the communication layer the Brain should eventually monitor

## Moil Relevance

This is Andres's own team infrastructure. Understanding the operating rhythm helps the Brain anticipate when team members are active/responsive and surfaces any gaps (people not checking in = potential churn signal or project risk). A future Teams pull with human responses would unlock full team roster intelligence.

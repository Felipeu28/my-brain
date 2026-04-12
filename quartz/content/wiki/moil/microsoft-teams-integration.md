---
title: "Microsoft Teams Integration"
tags: [moil, integration, pending]
date: 2026-04-11
---

# Moil × Microsoft Teams — Integration

**Type:** moil-topic
**Status:** 🔲 Pending — not yet built
**Last updated:** 2026-04-11
**Related:** [[moil/tech-stack]], [[moil/product-vision]], [[moil/index]]

---

## Purpose

Integrate Moil with Microsoft Teams to **gather business data from where SMBs already operate** — reducing the friction of the 21-question onboarding and enriching the Business DNA profile with real signals from how the team actually communicates and works.

---

## What Data to Gather

| Data Type | Source in Teams | Use in Moil |
|-----------|----------------|-------------|
| **Chats** — 1:1 and group messages | Chat threads | Surface hiring requests, workload signals, business context |
| **Meetings** — scheduled + ad hoc | Calendar, Teams meetings list | Understand team cadence, project milestones, decision rhythm |
| **Transcripts** — meeting recordings | Teams meeting transcriptions (auto-generated) | Extract decisions, action items, and open roles from spoken conversations |
| Team size and structure | Member lists, org channels | Inform business plan headcount assumptions |
| Communication topics | Channel names, message themes | Enrich market research and content calendar angle |

---

## Why Teams (not just Slack)

SMBs in construction, healthcare, hospitality, and service trades — Moil's core ICP — disproportionately use Microsoft Teams because:
- Microsoft 365 / Office bundles Teams at no extra cost
- Windows-first environments make Teams the default
- Many EDC-adjacent businesses (Buda HIVE companies) are on M365

This is a higher-signal data source than a web form for this specific ICP.

---

## Integration Approach (Proposed)

### Option A — Microsoft Graph API (Recommended)
- Connect via OAuth 2.0 (employer grants Moil read access)
- Pull data using [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/api/overview) endpoints:
  - `GET /teams/{id}/channels/{channelId}/messages` — channel + chat messages
  - `GET /chats/{id}/messages` — 1:1 and group chat messages
  - `GET /me/onlineMeetings` — meeting list
  - `GET /me/onlineMeetings/{meetingId}/transcripts` — meeting transcripts
  - `GET /teams/{id}/members` — team roster
  - `GET /me/calendarView` — calendar / scheduled meetings
- Scope: read-only, employer-approved, revocable

### Option B — Teams Bot / App
- Build a Teams app that Moil employers install
- Bot listens for hiring-related keywords and surfaces them in the Moil employer dashboard
- Higher friction to install, but enables real-time data vs. pull

### Option C — Webhook / Outgoing Webhook
- Simpler: employer sets up a webhook in Teams that POSTs to Moil when specific channel events happen
- Lower trust barrier (no OAuth), but employer-configured

**Recommended starting point:** Option A (Graph API) for read-only data enrichment during onboarding. Option B/C as a later expansion for real-time hiring signal capture.

---

## What's Pending

- [ ] Microsoft Azure app registration (app ID + secret)
- [ ] OAuth consent flow in Moil employer onboarding
- [ ] Define minimum required Graph API scopes (least-privilege)
- [ ] Decide: pull on demand (onboarding) vs. continuous sync
- [ ] Build data mapping: Teams data → Business DNA fields
- [ ] Privacy disclosure / consent copy for employers
- [ ] Test with a real M365 tenant (Buda HIVE company as beta tester?)

---

## Security Notes

- SOC 2 compliance requires explicit data handling policy for third-party OAuth integrations
- Teams data (especially messages) is sensitive — define retention, deletion, and access policies before building
- Employer must explicitly grant each permission scope; no silent background sync

---

## Connections

- [[moil/tech-stack]] — Full integration inventory
- [[moil/product-vision]] — Business DNA architecture that Teams data enriches
- [[moil/icp]] — Why SMB employers on M365/Teams are a high-signal ICP
- [[concepts/buda-hive]] — Potential beta testers from Cohort 4

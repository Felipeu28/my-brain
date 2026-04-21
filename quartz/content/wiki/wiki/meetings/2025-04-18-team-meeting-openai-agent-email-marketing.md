---
tags:
  - graph/leaf
---
# Meeting: Team Meeting — OpenAI Agent Launch + Email Marketing Setup

**Type:** meeting
**Date:** 2025-04-18
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/2025-04-18-team-meeting-2025-04-18-08-32-cdt-notes-by-gemini]]
**Attendees:** Andrés Urrego, Jacob Oluwole, Adeleke Tolulope, Taiwo Ola-Balogun (Abiodun Solomon had a family emergency)
**Meeting type:** Team / engineering + marketing
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]], [[wiki/people/abiodun-solomon]]

---

## Summary

**Milestone:** Adeleke built an OpenAI agent that automates business plan generation without repeated prompt inputs. Also: email marketing infrastructure decisions (HubSpot + Mailgun, subdomain strategy), design workflow for Business Plan Creator, Google→Microsoft migration deadline confirmed (May 5).

---

## Key Decisions — OpenAI Agent

- Adeleke built an OpenAI **agent** that automates business plan generation — eliminates repeated prompt character charges
- Testing via Postman with the advanced prompt
- Cost optimization: agents don't re-transmit the full prompt each time → significant cost reduction
- Future applications: build additional agents for different functionalities (chatbot for job Q&A, etc.)

---

## Key Decisions — AI Stack

| Function | Primary AI | Backup |
|---|---|---|
| Resume data extraction | Gemini | OpenAI |
| Resume generation | DeepSeek | — |
| Business plan generation | OpenAI agent (new) | — |

- Gemini getting better results for resume extraction
- DeepSync (DeepSeek) used less due to cost

---

## Key Decisions — Design Workflow

- Abiodun (Ablad) started work but had a **family emergency** → in hospital
- Prioritize **desktop design before mobile** (to avoid redundant design changes when desktop changes)
- Andres advocates for real-time design feedback to Ablad (no waiting for completion)
- Jacob agreed after initial resistance
- Business Plan Creator: "AI summary" → rename to "product summary"
- Tabbed interface preferred over single long-scrolling page

---

## Key Decisions — Email Marketing

- Create **subdomains** to protect main moyolab.com domain from spam flags
- Use HubSpot + Mailgun for email campaigns
- Business contacts list: keep all for now; add "unsubscribe" / "not interested" option to future emails
- Andres will grant Jacob **full HubSpot access after May 15th**

---

## Key Decisions — Google → Microsoft Migration

- **Google account being CHARGED** — will be **shut off May 5th**
- Transition to Microsoft tools (Outlook, OneDrive, Teams)
- Data handling warning: Andres explicitly warns team — do NOT store sensitive info on personal computers, do NOT use Google Chat (security risk)

---

## Data Security Reminder

Andres issued a clear warning:
> "Do not store sensitive personal information on personal computers. There are legal risks associated with mishandling personal data."

---

## Action Items

- [ ] Adeleke: Complete backend for Business Plan Creator within 2 days of Ablad finishing design
- [ ] Adeleke: Create/share results of AI-generated brand identity (color recommendations)
- [ ] Ablad/Jacob: Ablad completes 6 screens for business plan creator (~5 days)
- [ ] Jacob: Confirm Ablad availability and recovery; maintain open communication
- [ ] Jacob: Set up subdomains for email marketing (moyolab.com → marketing subdomain)
- [ ] Jacob: Get HubSpot + Mailgun email marketing infrastructure ready
- [ ] Team: Complete Google → Microsoft migration before May 5
- [ ] Andres: Grant Jacob full HubSpot access **after May 15**

---

## Key Quotes

> "Don't store sensitive information on personal computers." — Andrés (data security)

---

## Connections

- [[wiki/moil/gtm]] — email marketing infrastructure coming online

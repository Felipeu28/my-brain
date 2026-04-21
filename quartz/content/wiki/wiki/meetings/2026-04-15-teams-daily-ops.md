---
tags:
  - graph/spoke
---
# Apr 15, 2026 — Teams Daily Operations

**Type:** meeting
**Last updated:** 2026-04-15
**Source:** [[raw/teams-2026-04-15]], [[raw/email-digest-2026-04-14]]
**Related:** [[wiki/moil/product-roadmap]], [[wiki/moil/customers]], [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/abiodun-solomon]]

---

## Summary

84 Teams messages across 4 threads (Apr 14–15). Andres issued an urgent team-wide message demanding faster delivery pace. API cost crisis escalated — OpenAI spend is 3x what it should be. License distribution push for 5 clients. FitLogic deadline set for Friday Apr 18.

---

## Decisions

1. **Full OpenAI/API spend audit ordered** — Andres discovered refill frequency went from monthly to ~3x/week. Adeleke assigned to audit entire codebase for all gpt-4o calls and migrate remaining endpoints to gpt-5-mini.
2. **Claude Code access restricted** — Andres asked Jacob to log out of Claude Code. With 4 people using it simultaneously, resource/cost concerns.
3. **FitLogic deadline: Friday Apr 18** — Andres pushed FitLogic prod changes and asked team to test. Taiwo needs Supabase access (project in Lovable, being moved to Claude).
4. **Partner email for invitations** — Jacob confirmed using `partners@` email for sending Moil 360 invites.
5. **Buda EDC product discussion** — EDC called Andres to discuss "their product" (details TBD — Andres was pulled from team meeting).

## Action Items

| Owner | Action | Deadline | Status |
|---|---|---|---|
| Adeleke | Audit entire Moil codebase for OpenAI API usage; find all gpt-4o calls and switch to gpt-5-mini | ASAP | In progress |
| Adeleke | Complete all remaining pending Claude Code chats from last week | Apr 15 | Mostly done |
| Adeleke | Rotate API keys after audit complete | After audit | Pending |
| Jacob | Send Moil 360 license invitations: Megan Miller (meganmillernp@gmail.com), Mark Polanco (mark@connectex.net), Becky Torres (sirenbeautyandwellness@gmail.com), Roxana Yglesias (r.yglesias@alloyatx.com) | Apr 15 | In progress |
| Jacob | Verify Jill/PureSerenity (jilledegs01@gmail.com) license was sent | Apr 15 | Pending — first mention per Jacob |
| Jacob | Draft individual emails to all pending license recipients | Apr 15 | Assigned |
| Taiwo | Test FitLogic prod changes Andres pushed | Apr 15 | Assigned |
| Taiwo | Get FitLogic Supabase access (project moved from Lovable to Claude) | Apr 15 | Blocked — needs Andres to share |
| Taiwo | Meridian update is live — confirm client can test | Apr 15 | Done — cookie-based guide fix deployed |
| Abiodun | Deliver this week's content + start next week's content | By Friday | Behind schedule — Andres escalated |
| Andres | Schedule Astra Restaurant meeting with Daniel Guadiano | Thu Apr 16 | Confirmed via email |
| Andres | Send post-call summary to Roxana (from Apr 14 onboarding) | Apr 15 | Pending |

## Key Signals

- **Team tension:** Andres sent a direct message: "Everyone please let me know if you can't, don't have the time, the skill or the desire to continue to push forward." Called out that it "can't take longer to test than to build it." Testing-notes assignment from last week still not completed.
- **New social media client signed** — Andres told Abiodun about a new client needing social media help. Name not disclosed yet.
- **Nuovo Entertainment live** — Site deployed at nuovo-enterteinment.vercel.app (Taiwo working on it).
- **PDF/PPT quality improved** — Adeleke confirmed improvements; staging pushed.
- **Pitch deck via Business Coach** — Jacob tested and reported it "came out nice" for an EDC partnership pitch deck.

---

## Email Digest Highlights (Apr 14)

From [[raw/email-digest-2026-04-14]]:

- **Daniel Guadiano / Astra Restaurant** — Replied: Thursday works for a meeting. Schedule for Apr 16.
- **Renee Simmons / Hays CISD** — Career Day presentation May 7, ~20 min to 4th/5th graders at CHES. Calendar + prep needed.
- **Adam Maxon / Pflugerville** — Invitation to Pflugerville Mentor Day (founder/small biz mentoring event). New contact.
- **Jacquie Martinez / Buda HIVE** — Buda Retail Roundup Apr 20 invitation.
- **Inna Benyukhis** — Sent CRM documents for setup.
- **Becky Torres** — Accepted Apr 17 meeting (Siren Beauty).
- **Chamber breakup sequence** — 15 close-out ("Should I close this out?") emails sent to US/Canadian chambers. Pipeline hygiene day.
- **4 new value-prop outreach emails** — Southwest Gwinnett, Greater Hall, Falmouth, Location of Choice (EDC).
- **GitHub webhook secrets rotation** — Security alert forwarded to Adeleke + Jacob.
- **Sherese James-Grow / Boca Raton Chamber** — Redirected to main office (she only handles teens program).

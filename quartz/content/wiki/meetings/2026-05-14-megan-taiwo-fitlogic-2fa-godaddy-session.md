---
tags:
  - graph/leaf
date: 2026-05-14
type: meeting
attendees:
  - "[[wiki/people/megan-miller]]"
  - "[[wiki/people/taiwo-ola-balogun]]"
  - Andres Urrego
language: english
---
# 2026-05-14 — Megan × Andres × Taiwo: GoDaddy delegate + Outlook migration session

**Type:** meeting (Teams, ~34 min)
**Time:** 11:09 AM – 11:43 AM CT (16:09–16:43 UTC) — scheduled 11:00–11:30 AM
**Organizer:** Andres Urrego
**Source:** [[raw/teams-transcript-megan-andres-2026-05-14]]
**Related:** [[wiki/people/megan-miller]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/michelle-fitlogic]], [[wiki/orgs/fitlogic]], [[wiki/projects/fitlogic]], [[wiki/projects/meridian-buda]], [[wiki/people/travis-sutherland]], [[wiki/concepts/moil360]]

---

## Context

Working session to finalize the May 7 Cloudflare-workaround architecture: migrate Megan's outbound sales/marketing infrastructure from Gmail to a Microsoft 365 mailbox on `myfitlogic.com`, with `fitlogicfunctionalmedicine.com` reserved for patient/client traffic. The May 11 2FA blocker that prevented Taiwo from finishing wiring (GitHub, Vercel, GoDaddy via the new Moil-owned sales email) was the root reason for scheduling Megan into a live screen-share.

State going in:
- Resend domain blocker resolved May 7 via `myfitlogic.com`
- Connections (sales tool) credentials Megan dropped in Connect Team May 7 located by Andres mid-call
- The 2FA hand-off pattern from May 11 Monday Collaboration repeated here — Microsoft Authenticator prompt repeatedly vanished before Megan could approve; multiple resends required

## Key decisions

1. **Two-domain architecture confirmed and explicit.** `fitlogicfunctionalmedicine.com` = patient/client engine (`hello@`, etc., HIPAA-side). **`myfitlogic.com`** = sales engine for email marketing + CRM outbound. The forwarding `myfitlogic.com` → `fitlogicfunctionalmedicine.com` is already live, so end-user click experience is unchanged. Andres: *"That doesn't hurt your existing domain. You don't get spam blocked. People are still going to click and go to your website."* First time this split is stated as the standing pattern, not a workaround.
2. **GoDaddy delegate access granted to Andres@moilapp.com.** Megan added Andres as a delegate on her **whole GoDaddy account** because the "individual domains" picker would not let her scope to one domain (defaulted to FitLogic Functional Medicine). Worked anyway — account-level delegation lets Taiwo finish DNS/domain verification without Megan logged in live each time. **Closes the May 11 2FA blocker on the wiring side**, not on the email-receive side (still need Megan to read 2FA codes when Outlook 2FA fires).
3. **Security posture written down as a standing rule.** Andres articulated the rule for the first time on transcript: *"Like, if we are ever going to touch your accounts, it should always be, you know, like this — we should never have like continued access … only use it when we're working on something. And yes, once we actually deploy everything, you should change all of your passwords."* Two-factor authentication stays on. **First explicit on-record articulation of the Moil-touches-customer-accounts security pattern** — worth pulling into the Moil 360 playbook.
4. **Wed 2026-05-20 10:00–11:00 AM CT in-person at FitLogic** locked. This is the **next-week in-person walkthrough** Andres committed to May 7. Calendar invite sent during the call. Megan offered to meet at HIVE; Andres pushed for FitLogic to do it on-site so they can walk the deployed system with Megan + Michelle together.

## Action items

| # | Owner | Action | Due |
|---|---|---|---|
| 1 | Taiwo | Finish creating the new account against the `myfitlogic.com` Outlook email; verify the email and the domain; complete the GoDaddy delegation flow. Migration target: ready for Megan tomorrow morning | **Tonight 2026-05-14** |
| 2 | Taiwo | Meridian setup — verification code was sent to `Travis@zoho.com` and the mailbox appears empty / not received. **Re-run the request, then ping Andres**; Andres asks Travis Sutherland for the code | **Tonight 2026-05-14** |
| 3 | Andres | Send Megan access to the new system "first thing tomorrow" | **2026-05-15 AM** |
| 4 | Megan + Michelle | Play with the new system, try to break it, surface bugs | **Mon 2026-05-18 → Tue 2026-05-19** |
| 5 | Andres + Megan | In-person walkthrough of deployed system at FitLogic; fix anything Megan/Michelle flagged | **Wed 2026-05-20 10:00–11:00 AM CT** |
| 6 | Megan (post-deployment) | Rotate all passwords on touched accounts (GoDaddy, Connections, the new Outlook mailbox) | After May 20 walkthrough |

## Open issues surfaced

- **GoDaddy "individual domains" delegate UI quirk.** Megan saw *"choose individual domains under my domains"* but the picker would not let her select `myfitlogic.com` specifically — it defaulted to the FitLogic Functional Medicine entry. Worked at the account level. Worth confirming whether this is a GoDaddy UI quirk or a permission scope that needs re-doing later if/when Megan revokes account-level delegate.
- **`508F6B8D9.conversions.godaddy.com` forwarding rule found and disabled.** Megan saw an unfamiliar email-forwarding rule routing to a `*.conversions.godaddy.com` address — she didn't recognize it and turned it off. Likely a GoDaddy email-forwarding artifact tied to a prior product, but worth confirming nothing important was relying on it before the new mailbox goes live.
- **Microsoft Authenticator 2FA prompt vanished mid-approval.** Multiple times Megan said *"it just went away again"* / *"pop-up window went away"* — required Taiwo to resend the request 3+ times before Megan could approve. Same friction as the May 11 Monday Collaboration 2FA coordination. Annoying but resolved by Megan refreshing the app. **Pattern signal:** if Moil onboards more customers through Microsoft 365 setup flows, expect this friction to repeat — worth a standing "be on a call together for first-time 2FA" rule.

## Side context (not action)

- Megan asked Andres what days he's at HIVE. Andres: *"We're teaching Mondays, but then we do 11 to 1 coachings Monday to Fridays… we do virtual very often, very here and there we do an in person."* Andres preferred coming to FitLogic over having Megan come to HIVE for this session — relationship signal continues (Andres treating Megan as a high-touch anchor customer).
- Megan confirmed she missed an 11 AM patient slot during the meeting too ("I have not gotten anything today" → eventually pop-up appeared late, "I'm going to have to go in a few minutes"). Consistent with the Apr 23 calendar-hygiene self-flag — busy clinical operator, but engaged.

## Cross-page impact

- **Closes** the May 11 Monday Collaboration 2FA blocker for the GitHub/Vercel/GoDaddy wiring side. The remaining 2FA dependency is just on Outlook account login during initial verification, which is also now unblocked via Megan being on the call.
- **Closes** the May 7 *"schedule next-week in-person visit to FitLogic"* commitment — Wed 2026-05-20 10 AM CT booked.
- **Continues** the architectural pattern from May 7 (customer-owned credentials, Moil temporary touch only).
- **First explicit security/access discipline rule** worth capturing as a Moil 360 playbook standard.
- **Spillover to Meridian:** Travis@zoho.com email mailbox showing empty for the verification code is a separate blocker on the Meridian platform handoff thread (continued from [[wiki/meetings/2026-05-12-travis-meridian-platform-handoff]]). Adds an Andres-owned ask: get the code from Travis once Taiwo re-requests.

## Tone / relationship signals

- **Trust depth maintained.** Megan granted account-level GoDaddy delegate to Andres mid-call without hesitation. Andres returned the favor by articulating the security-discipline rule unprompted (*"we should never have continued access"*).
- **Megan's clinical busyness on display.** Pop-up app misbehavior + her own missed 11 AM patient slot during the call. Andres adapted (*"I'll give it a minute"*) without pushing.
- **Taiwo as quiet executor.** Drove the Outlook account-creation and 2FA loop from Nigeria side without ever sounding rushed. Confirmed `Travis@zoho.com` Meridian gap to Andres in the post-Megan-drop window — i.e., he stays on after the customer drops to surface remaining blockers. Pattern continues from Apr 23 customer-call discipline.

## Closing exchange (verbatim)

> **Megan:** Awesome, thank you.
> **Andres:** Thank you so much. Have a wonderful rest of your day.
> **Megan:** All right. All right. See you soon. Bye.
> **Taiwo:** Thank you so much. Have a wonderful day.

## Related

- [[wiki/meetings/2026-05-07-megan-andres-fitlogic-crm-handoff]] — preceding session that defined the `myfitlogic.com` workaround
- [[wiki/meetings/2026-05-11-monday-collaboration]] — internal call where the 2FA blocker was first flagged
- [[wiki/meetings/2026-05-12-travis-meridian-platform-handoff]] — Meridian context for the Travis@zoho.com code issue
- [[wiki/projects/fitlogic]]
- [[wiki/orgs/fitlogic]]

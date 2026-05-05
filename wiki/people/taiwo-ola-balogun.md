---
status: active
last_contact: 2026-05-04
tags:
  - graph/spoke
  - person/team
---
# Taiwo Ola-Balogun

**Type:** person
**Last updated:** 2026-05-04
**Source:** `raw/meetings/` (multiple meeting transcripts), [[raw/teams-2026-04-12]] (415 messages, Apr 5–12 2026), [[raw/teams-transcript-monday-collaboration-2026-04-13]], [[raw/teams-2026-04-15]] (84 messages, Apr 14–15 2026), [[raw/teams-2026-04-18]] (51 messages, Apr 17–18 2026), [[raw/teams-2026-04-20]] (36 messages, Apr 19–20 2026), [[raw/teams-2026-04-21]] (161 messages, Apr 20–21 2026), [[raw/teams-transcript-CRM-GOOGLE-Setup-with-Megan-2026-04-23]], [[raw/teams-2026-04-24]] (9 messages 1:1, Apr 24), [[raw/teams-2026-04-26]] (4 messages 1:1, Apr 26), [[raw/teams-transcript-website-update-review-call-2026-04-28]], [[raw/teams-transcript-mark-polanco-andres-2026-04-28]], [[raw/teams-transcript-monday-collaboration-2026-05-04]]
**Related:** [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]], [[wiki/moil/product-roadmap]], [[wiki/meetings/2026-04-23-megan-crm-google-setup]]

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

## April 21, 2026 — FitLogic Push to Finish + Connectex Commit

Source: [[raw/teams-2026-04-21]]

- **Morning check-in:** "Good morning Andres" + asked for Connectex CRM URL and whether to work on design alongside functionality (3:34 PM — midday his time). Worked overnight on FitLogic bugs from the Apr 20 session.
- **FitLogic campaign/sequence bugs deep-fixed** — sender mail verification on Resend, auto-schedule behavior clarified ("once I schedule it is automatic whether checked or not"), confirmed `partners@moilapp.com` is the sending address and test-user mail is connected on Google.
- **Campaign vs. sequence parity gap surfaced:** Andres found that email links can be edited in **sequences** but not in **campaigns** (8:33 PM). Taiwo: "Yeah you can do that but you have to click editing the campaign" — path exists but hidden. Feature-parity audit warranted.
- **OG image / landing page messaging bug** — 9:12 PM Andres: "Why is this still the image and messaging for our links?? FUCK!" Taiwo acknowledged: "My bad, didn't remember the og image of this application was different from the landing page." Fixed by 9:46 PM.
- **Coach day/light mode** — Andres asked Taiwo to restore it (6:08 PM); it was removed in a prior build.
- **Committed to start Connectex Apr 22.** Quote (10:10 PM): "Other than fitlogic we have 8 products!! I really need to finalize fitlogic Taiwo!! I need to move on to other projects so we can start getting paid! Sir, I am ready to work on connectex. Can I get the link to the CRM for that so that I can play with that and start work tomorrow." Andres: "But we need to finish fitlogic so we can get her all switched over!" — Taiwo agreed to finalize FitLogic in parallel.
- **Strong delivery-rhythm signal** — this is the first time Taiwo has explicitly flagged the revenue gap ("start getting paid") and volunteered to start the deferred project (Connectex) on a specific next day. Pattern shift from Apr 18 time-zone-boundary recovery to Apr 21 revenue-urgency ownership.

See [[wiki/meetings/2026-04-21-teams-daily-ops]].

## April 23, 2026 — FitLogic CRM Customer Setup Call (40 min)

Source: [[wiki/meetings/2026-04-23-megan-crm-google-setup]]

First time Taiwo joined a live **customer** setup call (not a team-internal one) — he was on video with Andres, Megan, and briefly Michelle from 2:15–2:58 PM CT. Role in the call:

- **Drove the Google Cloud Console OAuth configuration** — instructed Andres through creating/updating the OAuth client, branding, audience, scopes (`gmail.send` + `gmail.readonly` + `gmail.compose` + `calendar.readonly`), and authorized redirect URIs.
- **Correctly anticipated multi-environment redirect URIs.** Quote: *"You can add multiple links, so for local development, for staging, and for production, so we can have multiple links at once."* — pre-empted a redeployment friction Moil has hit before.
- **Took GitHub collaborator access from Megan's account** instead of hosting the repo under Moil. First customer handoff done this way from day one.
- **Committed to test the build overnight** and continue the migration/deploy work the following morning. Andres closed the call: *"We have until next Wednesday [Apr 29] to finish this one up real good, okay?"* Taiwo: *"Okay, sir."* Hard deadline acknowledged.
- **Pace signal:** Andres told Megan, *"For Taiwo right now, it's almost 11 PM, so I know him — he'll probably work a little bit on this today, but tomorrow morning he'll definitely work on it."* Taiwo confirmed: *"I did push the code to GitHub. I'll test it this night. If I have any issues with testing, I'm going to get back to you."* Still late-night pattern from Nigeria side, but voluntary and bounded — not the Apr 18 "2 AM my time" frustration pattern.

**New pattern:** Taiwo is now the named engineer for the FitLogic case-study handoff (Apr 28 go-live, Apr 29 walkthrough). First time a Moil 360 customer has a single engineer attached to their end-to-end deployment rather than rotating support.

## April 24, 2026 — First Voluntary Weekend Commitment

Source: [[raw/teams-2026-04-24]], [[wiki/meetings/2026-04-24-teams-daily-ops]]

- **Volunteered weekend Apr 25–26 work on Inna + Connectex.** Quote (6:57 PM): *"I have the weekend to work on Inna and connectex"* — first time Taiwo has explicitly committed to weekend work. Pattern shift from Apr 18 time-zone boundary → Apr 21 revenue urgency → Apr 24 weekend volunteer.
- **Surfaced a status-gap on Inna.** Andres at 4:12 PM: *"Where are we on Inna? whats left to do there?"* Taiwo: *"I thought you worked on Inna already"* — first signal that ownership of Inna is unclear between Andres and Taiwo. Worth resolving before the weekend sprint.
- **Confirmed Supabase opened for FitLogic Apr 23.** *"We opened a supabase yesterday for fitlogic"* (6:50 PM) — backend infra layer continues from the Apr 23 customer setup call.
- **Asked about account scope.** *"I need the supabase credentials also and the resend email"* + *"Hello, for what account?"* Andres clarified: *"They all login with github"* — universal GitHub-as-SSO pattern confirmed for the engineering side.

See [[wiki/meetings/2026-04-24-teams-daily-ops]].

## April 26, 2026 — Loading-State UX Pickup

Source: [[raw/teams-2026-04-26]]

- Andres shared an X loading-state UX reference (12:36 AM): *"https://x.com/bzagrodzki/status/2048091983328223415 We need this for Moil"*. Taiwo replied 8:22 PM same day: *"Checked that out already. We will implement that loading state"* — same-day acknowledgement + implementation commit. Andres's confirmation: *"There's a few of them, look really nice"* (8:22 PM).
- Pattern: founder-shared X reference → engineer follow-through within hours, no clarifying questions. Continues the Apr 24 weekend-volunteer ownership posture.

## April 28, 2026 — Repo Discipline Hard Rule + FitLogic Tonight Plan + Mark Walkthrough Tech Support

Source: [[raw/teams-transcript-website-update-review-call-2026-04-28]], [[raw/teams-transcript-mark-polanco-andres-2026-04-28]], [[wiki/meetings/2026-04-28-website-update-review-internal]], [[wiki/meetings/2026-04-28-mark-polanco-connectex-walkthrough]]

- **Repo visibility crisis surfaced — 15 minutes before the Mark Polanco walkthrough.** Andres asked which repo Taiwo was working on for Connectex. Taiwo: *"I moved it to my landing page, but I don't think I've pushed it."* Andres realized he was about to show Mark *the same thing he showed three weeks ago*. Pushed firmly: *"Just push it, push it to the new repo, because the repo that you moved it to is empty… I'm never going to push to main, but I need visibility."* **First time Andres has framed repo push discipline as a non-negotiable team-wide rule.** Taiwo committed: *"I'm going to push it. I'm going to push it."*
- **Volunteered to deploy FitLogic tonight Apr 28.** *"Need to work on getting feed logic sets like today… because feed logic is not set to go tomorrow, but if we work on it today, we'll be able to get set for tomorrow."* Plan: finalize, push, deploy on Vercel, set environmental variables, test contacts upload + Google account connection. Initially proposed 10 PM Nigeria time (~4 PM CT) — Andres pushed back: *"Put it on my calendar. I'm very flexible, but flexible needs to mean we meet in the middle. I can't always meet you at 2 AM or 11 PM."* Pattern continues from Apr 18 time-zone boundary → Apr 21 revenue urgency → Apr 26 loading-state pickup → Apr 28 calendar-etiquette ask.
- **Implemented readable WYSIWYG email editor on Inna; replicating to FitLogic.** Email editor was HTML-only ("I don't think she should be typing HTML on that box"). New editor has bold/italics + **variable selector** for contacts, email, distance — user clicks to insert variables instead of writing template syntax. Plans to replicate Inna implementation onto FitLogic.
- **Joined the 1:45 PM Mark Polanco walkthrough mid-call** to add Gemini API key for ConnectX campaign builder so the Verizon T77 LTE test campaign could run. First time Taiwo has been on a customer call as live tech support. Confirmed by Andres mid-call: *"I'm going to add my developer and my project manager so they can listen in. They can listen in and we make sure that we don't miss anything before the delivery."*
- **Vercel env-var security observation.** Noted that Vercel no longer shows previous env-var values when editing — *"probably for security."* Continues his Apr 21 OG-image / partners@moilapp.com deliverability awareness pattern.
- **Diagnosed Jacob's hardware constraint live.** Jacob's HP screen height (568 px) is causing scrolling friction in Inna CRM testing — *"Your screen is very, very small. The height of your screen is, I think, 568 pixels."* Surfaced as a UX signal for the engineering team without being a build issue.

See [[wiki/meetings/2026-04-28-website-update-review-internal]] and [[wiki/meetings/2026-04-28-mark-polanco-connectex-walkthrough]].

## May 4, 2026 — Product unification mandate + email-infrastructure research

Source: [[raw/teams-transcript-monday-collaboration-2026-05-04]], [[wiki/meetings/2026-05-04-monday-collaboration]]

- **Weekend status reported live.** Worked Saturday on FitLogic, Inna CRM, and Siren Beauty. ConnectX skipped — picked up this week. Sanity access for Siren Beauty still blocked; access request sent
- **Found an open-source email-infrastructure project** as a potential **Resend replacement** that would lift the 100-emails-per-day cap. Plan: clone the repo, bring own infra, eventually replace Resend. Andres approved investigation but framed it as *"small scale for now"* — appropriate for Moil's current SMB customer profile (most send 1–2 mailboxes worth, not 100/day)
- **Product unification mandate from Andres.** Combine the four side-projects (FitLogic, Inna CRM, Siren Beauty, ConnectX) into a single packaged product Moil can resell to clients. Three product pillars identified: **email-sequence tool** + **blog generator** + **CRM**. Taiwo to lead the audit and unification design
- **Will receive Moil 360 license today** so he can dogfood the business coach during reading sessions and push it on edge cases. Continues the Apr 28 hot-mic professionalism note — Taiwo as a regular Moil-as-a-customer experiencer

## Contact

- Teams: Taiwo Ola Balogun
- Personal Gmail: `taiwotriumphant@gmail.com` (disclosed Apr 20, 2026)

## Gaps

- Full name: Taiwo Ola-Balogun — likely Nigerian Yoruba name (Taiwo = first of twins)
- Location unknown (likely Nigeria)
- Network infrastructure seems unreliable (multiple mentions of bad connectivity)

<!-- AUTO-ACTIVITY:start -->
## Recent Activity (auto)

*Auto-generated by entity-graph-builder · last refreshed 2026-05-04. Entries capped at 12, pruned at 30 days. Do not edit inside the markers.*

- **2026-05-04** · `email-digest` · looped in on CRM test/delivery and campaign sender address request
- **2026-04-21** · `teams` · finished FitLogic OG image fix; ready to start Connectex implementation
- **2026-04-23** · `teams` · joined live FitLogic customer setup call (40 min); drove Google Cloud OAuth config + took GitHub collaborator role
<!-- AUTO-ACTIVITY:end -->

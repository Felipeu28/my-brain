---
tags:
  - graph/leaf
date: 2026-04-23
type: meeting
attendees:
  - "[[wiki/people/megan-miller]]"
  - "[[wiki/people/taiwo-ola-balogun]]"
  - Andres Urrego
  - Michelle (FitLogic staff)
---
# 2026-04-23 — Megan × Andres × Taiwo: CRM / Google Setup

**Type:** meeting (Teams, ~40 min)
**Time:** 2:15–2:58 PM CT (19:15–19:58 UTC)
**Source:** [[raw/teams-transcript-CRM-GOOGLE-Setup-with-Megan-2026-04-23]]
**Related:** [[wiki/people/megan-miller]], [[wiki/orgs/fitlogic]], [[wiki/people/taiwo-ola-balogun]], [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]], [[wiki/concepts/moil360]], [[wiki/people/daniel-mann]]

---

## Context

Two days after the Apr 21 live CRM tour, this session moved from "decide what to build" to "wire the infrastructure so Megan owns it." Goal: set up Megan-owned Google Cloud OAuth, GitHub, Supabase, and Resend accounts so Taiwo can deploy the Moil CRM to `fitlogicfunctionalmedicine.com/crm` on Megan's GoDaddy domain. Side threads on the Electric Bricks website dispute and the Moil 360 / Coach fix Megan received that morning.

## Key decisions

- **CRM deploys to `fitlogicfunctionalmedicine.com/crm`** on Megan's GoDaddy. Vercel hosts the app; Supabase hosts contacts DB. Both free tiers.
- **Every infrastructure account is owned by Megan.** Moil is a collaborator only — first time Moil has set up a customer this way from inception. Full handoff becomes a one-click switch at go-live instead of a migration project.
- **OAuth scopes finalized** on Megan's Google Cloud project: Gmail `send` + `readonly` + `compose`, Calendar `readonly`. Redirect URIs will hold multiple entries (local / staging / production) so the same client works across environments.
- **`hello@fitlogicfunctionalmedicine.com`** is the Gmail account the CRM authenticates against — same password Michelle already had.
- **GitHub repo** created under Megan's account; Taiwo added as collaborator.
- **Resend** used for outbound email, tied to Megan's GitHub login.
- **Gemini API key** will be set up for Megan at deploy time so she pays her own monthly usage.
- **Go-live target: Monday 2026-04-28.** Moil tests through the weekend; Megan starts sending real emails Monday or Tuesday.
- **Handover meeting: Wed 2026-04-29 at 9:30 AM CT** — full walkthrough with Taiwo joining.
- **Multi-user (Michelle login) deferred.** For now Michelle shares Megan's FitLogic login. Multi-user is planned as a paid feature for the $75/year tier.
- **Moil 360 / Moil Coach working again for Megan** (Jacob emailed her the fix confirmation that morning).

## Action items

| Owner | Action | Timing |
|---|---|---|
| Taiwo | Test the CRM build tonight after pushing code to the new GitHub repo | Tonight (2026-04-23, evening Nigeria time) |
| Taiwo | Continue migration / deploy work | 2026-04-24 morning |
| Andres | Send Megan a status update: what's done, what's left, testing plan | 2026-04-24 |
| Andres | Attend Megan's meeting with her website agency (Electric Bricks) | Fri 2026-04-24, 12:30 PM CT |
| Megan | Start forwarding every meeting invite to Andres (admits she keeps missing meetings because they only live in her head) | Ongoing |
| Megan | Log into Moil 360, upload logo + brand colors, play with image editing — **do not build the content calendar yet** until all brand assets are uploaded | Before next Wed |
| Andres + Taiwo | Verify testing works through the weekend so Megan can send real emails Monday | Sat–Sun 2026-04-25/26 |
| All | Reconvene for full handover | Wed 2026-04-29, 9:30 AM CT |

## Side threads

### Website agency dispute (Electric Bricks)

Megan is meeting her website vendor Fri 2026-04-24 at 12:30 PM CT. Two live issues:

1. **Scope-of-practice / compliance.** Vendor is referencing "doctor" alongside "health coach" in Megan's copy. Megan flagged this to them as a patient-safety issue — she's an NP, not a doctor, and nothing on the site can confuse a patient about her scope of practice. Vendor's written response: *"You hired us to give you an SEO / AIO optimized website with 30 pages to get your ranking in Buda, Texas. To rank, you need more content than you as the lead practitioner think you need. From my experience with other clinics, this is what's required to make patients feel safe enough to proceed. This is my professional expertise from over 10 years. If you want to remove content, you can remove content. I'm happy to discuss in tomorrow's meeting."*
2. **30-page SEO bloat.** Andres's position in the call: *"I get SEO is important, but how does a bunch of text that nobody will ever read help? And more importantly, it can't confuse him [the patient] at all."* Bulk SEO text that no human reads isn't obviously worth it, but the scope-of-practice line is non-negotiable.

Andres offered to attend the Friday meeting. Megan forwarding the link (no formal invite — vendor sent a direct meeting link).

### Daniel D. Mann / Firefly connection surfaced

Michelle joined briefly near the end and mentioned she was supposed to say hello to Andres from [[wiki/people/daniel-mann|Daniel D. Mann]] ("Firefly"). Andres: *"Daniel is the man … amazing guy when it comes to connecting people, and he's so fun to talk to … please tell him I say hello back, and to not be shy and shoot me a text."* Michelle confirmed Daniel says the same things about Andres — *"smart guy, very well connected."* This is a second-degree social-proof loop through Moil's #1 referral partner and is worth a direct text from Andres to Daniel to reinforce the relationship.

### Calendar hygiene commitment (behavior change)

Megan missed an 11 AM meeting during this call. She committed in-line: *"I really got to start sending you everything so you can put it on my calendar, because I'm not good. … I'm just going to send you a message every time I get a meeting, so you can put it on there."* This is a standing pattern change for Megan, not a one-off — Andres's calendar becomes her external memory.

### Moil 360 homework (for Megan before Apr 29)

Andres closed the call with open homework framed around a customer story: a red-light-therapy client who created a branded image in Moil by dropping in a photo of her own machine and asking the AI to generate a "person inside of the machine" image. Megan's task: log in, upload logo + brand colors, play with image editing using her own reference photos — **but do not create the content calendar yet** until brand assets are in place. Then it becomes daily: copy, paste, download, post.

## Why this meeting matters

1. **First "Megan owns everything from day one" deployment.** Moil has historically started customers on Moil-owned infrastructure and migrated later. FitLogic is the template for the new pattern: customer owns the stack from day one, Moil is a collaborator. Makes the handoff a single credential transfer rather than a migration.
2. **Seven-day Moil 360 CRM distribution loop.** Apr 21 (hand-on tour) → Apr 23 (infrastructure wired) → Apr 25–26 (weekend testing) → Apr 28 (Megan starts sending) → Apr 29 (formal handover walkthrough). If this loop holds, it is the replicable time-to-value baseline for future Moil 360 CRM customers.
3. **Compliance / scope-of-practice signal.** The "doctor vs. health coach" fight with Electric Bricks is a live example of why Moil's play for licensed-professional customers (NPs, therapists, coaches) has to respect scope-of-practice boundaries — especially as Moil layers in AI-generated content.
4. **Referral-graph closure.** Michelle's unprompted "Daniel says hello" is the first recorded instance of Daniel Mann's referral loop closing back through an existing Moil customer. Strengthens the case for treating Daniel as a systematic channel (see [[wiki/people/daniel-mann]] reciprocation action).
5. **Calendar hygiene = Moil 360 retention risk.** Megan self-identifying "I keep missing meetings" is a retention risk for any CRM — her own product. If the CRM can surface this automatically, it's a feature ask hiding in plain sight.

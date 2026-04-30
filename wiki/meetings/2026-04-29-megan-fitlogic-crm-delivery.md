---
tags:
  - graph/leaf
date: 2026-04-29
type: meeting
attendees:
  - "[[wiki/people/megan-miller]]"
  - "[[wiki/people/michelle-fitlogic]]"
  - "[[wiki/people/taiwo-ola-balogun]]"
  - Andres Urrego
---
# 2026-04-29 — Megan × Andres × Michelle: FitLogic CRM Test & Delivery

**Type:** meeting (Teams, ~88 min)
**Time:** 9:30–10:58 AM CT (14:30–15:58 UTC)
**Source:** [[raw/teams-transcript-megan-moil-crm-test-and-delivery-2026-04-29]]
**Related:** [[wiki/people/megan-miller]], [[wiki/people/michelle-fitlogic]], [[wiki/orgs/fitlogic]], [[wiki/concepts/moil360]], [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]], [[wiki/meetings/2026-04-23-megan-crm-google-setup]], [[wiki/meetings/2026-04-28-website-update-review-internal]]

---

## Context

The promised handover walkthrough from the Apr 23 setup call. Andres delivered the full Moil custom build for FitLogic — contact CRM, AI campaign creator (email), and Content360 30-day social calendar with image and video generation. **Michelle joined ~2/3 through and immediately became the most useful copy reviewer in the room.** This is the first call where she's named as the day-to-day operator candidate (Megan: *"I want you here … she's better at putting my thoughts into words"*).

Megan is migrating from **Charm (medical EHR)** and **Keap (sales CRM)** as her source-of-truth systems; ~5,000 contacts to import — mostly cold leads, smaller subset of active patients, plus legacy massage-only and ear-acupuncture contacts. The Gmail OAuth wired Apr 23 is live; brand DNA partially configured (logo uploaded, colors not yet entered).

**FitLogic is now the first Moil 360 customer to receive end-to-end CRM + Campaigns + Content360 in a single delivery walkthrough.**

## Key decisions

- **Posting cadence:** **Daily, not weekly.** On days with both image and video, post **twice** (one for each asset).
- **Email rollout strategy:** Don't blast all 5,000 cold leads on the same email. **~10/day cadence**, rotate variants until one performs (avoid burning the list on a single template).
- **Tone for AI-generated emails:** **Hook-style opener** (e.g., *"You may be wondering…"*, *"Are you still struggling with…"*) instead of *"I wanted to share…"*. Patient-focused, not founder-focused. Megan and Michelle will edit per-send via the **free-form prompt box** rather than asking the AI to rewrite (avoid unnecessary API calls).
- **Lead segmentation taxonomy agreed:** cold / previous client / active patient / inactive patient / IC-only (initial-consultation-only) / massage-only legacy. Andres extracts patient vs. non-patient from the 5,000-row export; Megan handles the manual IC-only tagging on her side.
- **Bulk-tag shortcut:** Megan will identify the day Jill's contact list was imported into Charm and **mass-tag those rows** as one segment — good-enough segmentation without per-row review.
- **Default image format:** **Stories layout (vertical)** — performs best on Facebook/Instagram per Andres.
- **API key for AI email generation:** Megan continues using Moil's test API key during testing; switch to FitLogic's own Gemini key at launch (~$2–3/month expected total — *"a couple bucks a month"*).
- **Testing rule:** Test sends **only against newly-created test contacts**, never against existing customer contacts.
- **Michelle is the new day-to-day operator.** Megan asked Andres to add Michelle as staff; Michelle will run the platform daily once Megan's brand colors are in.

## Action items

### Andres / Moil engineering

- [ ] **🔥 Extract patients vs. non-patients** from FitLogic's 5,000-contact export (Megan already shared the patient list earlier — Andres to retrieve from prior call's download, Megan confirmed *"we did and you downloaded it on the call"*)
- [ ] **🔥 Add "Last contacted" filter/tab** on contacts so Megan can see who's been touched and who hasn't
- [ ] **🔥 Add `previous client` option** on lead source / pipeline so prior-but-inactive patients can be segmented and emailed differently
- [ ] **🔥 Customize the lead-source drop-down** to include: social media, website, driving by, friend/family referral, networking event, **other (with free-text on "other")**
- [ ] **🔥 Bug — pipeline stage propagation:** moving a contact to "won" in the pipeline view doesn't propagate back to the contact card (still shows old status). Fix so analytics roll up correctly
- [ ] **🔥 Bug — Content360 calendar defaults to February:** Megan started the calendar mid-call, the days came out as Feb 28 instead of current month. Investigate stale date param
- [ ] **🔥 Bug — "Edit image" constrains regeneration to original:** Megan tried "happy gut" + "image of a person who is happy and feels relief" — neither produced a new image. Andres's hypothesis: edit-image is forcing the original image rather than producing a new one from the new prompt
- [ ] **Verify Brand DNA colors are propagating into Content360 image generator** (Megan suspects they aren't because she set up the calendar before saving colors)
- [ ] **Add closed-captioning support for generated videos** (accessibility feedback from Michelle — *"people with hearing disabilities comment that a lot"*)
- [ ] **Send Megan today:** platform access details, list of what she needs, and confirmation Michelle can be added as staff via Settings → Add Staff
- [ ] **Build chat/FAQ widget** tied to FitLogic's website once the website is deployed; include "book a call" link to Square calendar (Megan currently uses Square for bookings)
- [ ] **Add ability to paste/manage links centrally** so they can be reused across emails (currently you have to retype/paste links in each email)
- [ ] **Native quiz** on FitLogic site (deferred until Electric Bricks redelivers)

### Megan / FitLogic

- [ ] Bring brand color **hex/RGB values from home notebook** and enter in Brand DNA (left at home; Sean has them)
- [ ] **Export active-patient list from Charm**; identify any inactive names she doesn't recognize
- [ ] **Manually tag IC-only patients** (people who came for an initial consultation but never converted) — Megan owns this manual cleanup
- [ ] Add **Michelle as staff** via Settings → Add Staff once feature confirmed
- [ ] Reach out to Austin business friend re: how she added closed captions for accessibility on Instagram videos

### Michelle / FitLogic

- [ ] Step into day-to-day operator role for the platform once brand colors are loaded
- [ ] Help Megan rewrite cold-email opening lines toward hook-style ("you may be wondering…")

## Notable observations

- **Phone interruption mid-meeting** for a Buda Drug Store medication refill — patient-care work bled into the training; Megan handed off live to Michelle to call the pharmacy and arrange a refill (or fall back to "Use Grace" pharmacy). **Real-time confirmation that Michelle is the practice manager**, not just admin.
- **Michelle joined ~2/3 through and gave the most useful copy feedback in the call** — *"we need a hook, an attention getter to start it off … like a thought-provoking question to get them to read the rest of the email."* Megan: *"Yeah, that's exactly what I was going to say."*
- **Megan is uncomfortable with the word "I" in cold-email openers** — *"Sometimes I'm like, well, I don't care what you want."* Wants reader-centered copy. **Tone signal worth baking into the FitLogic brand voice config.**
- **The AI-generated email had to be rewritten live in the prompt box** to make it sound like FitLogic. Andres explicitly framed the prompt box as the "imprint Megan" layer on top of the AI-generated body: *"What we've built on the back end is the brand, FitLogic. Now this is the area where we can imprint Megan."*
- **Content360 calendar started on Feb 28** even though Megan opened it that day — Megan: *"That's weird."* Date-handling regression worth a same-day fix before Megan tries again.
- **Image-edit appears stuck on the original image.** Megan typed "happy gut" and "image of a person who is happy and feels relief" into the edit-image box — both produced a face/hand that looked like a continuation of the gut-reset image rather than a fresh generation. Investigate whether edit-image is wired as image-to-image rather than text-to-image.
- **Video generation works.** Andres walked Michelle through generate-image → render-to-premium-motion-video → download → Facebook copy/paste. Tested on the perimenopause hormone-shift day; successful end-to-end. **Default video models:** Gemini 3.1 (8s) vs. Grok (10–12s) — try both and pick.
- **Square calendar already in use** for bookings — Andres committed to wiring "book a call" links from the future chat widget directly to Square.
- **Taiwo had hot mic playing audio** mid-call ("If you would like to listen to music, action video, or only use headphones") — minor professionalism issue. Worth a note for future client-facing calls that internal devs should stay muted.
- **LinkedIn distribution surfaces as a positive surprise** — Megan: *"I see LinkedIn as an option here … I use LinkedIn a lot. I like that you can maybe do it different. A very different type of message on LinkedIn."* Multi-platform posting from Content360 lands well with this customer.
- **Michelle has been at FitLogic ~2 weeks.** Multiple references in the transcript ("just having only been here a couple weeks", *"I'll have to go through and just because I know the names"*). Onboarding curve is real.

## Why this meeting matters

1. **First end-to-end Moil 360 walkthrough completed** — CRM + Campaigns + Content360 in a single 88-minute session, with the customer doing the clicks. Time-to-handover: **8 days from Apr 21 first hands-on tour → Apr 29 customer-driven test post**. Replicable benchmark.
2. **Customer-facing UX bugs discovered live** in the moment — pipeline-stage propagation, Content360 February date default, edit-image regeneration. These are now P0 because the **next paying Moil 360 customers will hit the same bugs**, not just FitLogic.
3. **Practice manager pattern emerges** — Michelle is the actual day-to-day operator; Megan is the brand voice + clinical authority. This is the **first explicit customer where the "owner trains a manager" delivery pattern shows up cleanly**, and it has implications for how Moil should structure the onboarding video / docs (target: practice manager, not owner).
4. **Patient-focused tone vs. founder-focused tone** is now an explicit Brand DNA signal worth capturing in the system prompt for AI email generation. *"You may be wondering…"* over *"I wanted to share…"* is not a one-off preference — it's how Megan sees herself in relation to her patients.
5. **Square calendar integration** becomes a hard requirement for the chat-widget rollout. Likely also relevant for other Moil customers running on Square (becky-torres / Siren Beauty, who runs nail/lash booking, may overlap).
6. **Closed captioning surfaces as accessibility-blocker feedback** from Michelle — first time accessibility has been raised by a Moil 360 customer. Worth checking whether Facebook/Instagram add CC automatically or whether Moil needs to bake it into the video render pipeline.

---
source: Microsoft Teams transcript
meeting_subject: Travis & Andres
meeting_date: 2026-05-12
meeting_time_utc: 18:30–19:01
meeting_time_ct: 1:30pm–2:01pm
meeting_type: product handoff / platform demo (Meridian Buda)
ingested: true
ingested_at: 2026-05-12
organizer: Andres Urrego (Andres@moilapp.com)
attendees:
  - Andres Urrego (Andres@moilapp.com)
  - Travis Sutherland (travis@zoiwell.com)
transcript_id: ktVizInGAAAAi_B6lATZRTE5Om1lZXRpbmdfT0RabU9XUmlPR1F0T1RVNU1TMDBNREkzTFRoaVpEUXRPV1F4WXpRME5EQXdOVE0yQHRocmVhZC52MqEw2TxlZDUwZDMzYi03M2I1LTQzNDgtYWI1NC05ZmVkNDc4MTgxMDYtMTc3ODYxMDc1Ny1UcmFuc2NyaXB0VjI=
---

# Travis & Andres — Meridian Buda platform handoff (2026-05-12)

## Context

Andres walked [[Travis Sutherland]] through the event management / ticketing platform Andres has been building for Meridian Buda (Travis's venue). The session covered the full lifecycle: creating events (including recurring), ticketing tiers, customizable RSVP, check-in flow (QR scan or name search), analytics dashboards, booking inquiries, menu management, and automated email flows (confirmation + 7-day reminder + 24-hour reminder + post-event follow-up). The session ended with credential transfer — Travis set up his own GitHub account and shared GoDaddy admin access so that everything going forward lives under Travis's accounts, not Andres's.

## Key decisions

1. **All deployment artifacts live under Travis's accounts.** Andres explicitly avoided creating things under his own login — code goes in Travis's GitHub repo, site hosts on Travis's Vercel (free), emails go through Travis's Resend account (free under 1,000/day). Reason: Travis retains full control even if he later hires a different developer.
2. **Primary admin email: `travis@zoiwell.com`.**
3. **Staff check-in email: `info@meridianbuda.com`** — Andres will provision this as a team account so staff can check guests in at the door.
4. **Andres will not push code changes without Travis's prior approval on images.** Workflow: Andres sends images first → Travis reviews → Andres pushes to Vercel.
5. **Recurring events** — confirmed pattern: create event with a "weekly until canceled" recurrence option so Meridian doesn't have to recreate weekly events manually.
6. **Email flow customization** — Travis can update the 24-hour and post-event emails directly to act as a quasi-"send custom email" tool. (Custom on-the-fly email creation is a future feature request.)
7. **Custom ticket-tier names** — confirmed Travis can rename "general admission" to "RSVP" on free events to capture headcount without the paid-ticket framing.

## Bugs identified during demo

| Bug | Symptom | Notes |
|---|---|---|
| API key for Gemini autofill expired / model deprecated | Autofill on artist creation didn't populate when Travis tested it (tried with "Kiltoni" comedian example) | Andres: "Gemini replaced this model, so we just need to upgrade it to the new model." |
| Check-in stays disabled even after event goes live | Andres moved event time to make it live; check-in button stayed in disabled state showing "only available while event is live" | Andres: "It should have updated right away. I'll work on this." |
| Event update form shows stale opening time (6:30) after time change | Travis caught it: "Yeah, looks like it still has the 6:30" | Same underlying issue as check-in not refreshing on time change |

## Action items

| # | Owner | Action | Status |
|---|---|---|---|
| 1 | Travis | Sign up for GitHub.com with `travis@zoiwell.com` (email+password, NOT Google) and send credentials to Andres | ✅ Done in-meeting |
| 2 | Travis | Send Andres GoDaddy invite to `Andres@moilapp.com` for site deployment access | ✅ Done in-meeting (after second invite — first attempt didn't land) |
| 3 | Andres | Replace API key + upgrade to current Gemini model | Today (May 12) |
| 4 | Andres | Fix check-in button not enabling when event start time is changed | Tomorrow (May 13) |
| 5 | Andres | Push landing page (with new hero/Stan Martinez images) to production | By tomorrow (May 13) |
| 6 | Andres | Provision `info@meridianbuda.com` as additional staff login for check-ins | Next |
| 7 | Andres | Text Travis when the API key is replaced so he can re-test artist autofill | After fix |
| 8 | Andres | Send Travis a credentials doc with all relevant logins (GitHub, Vercel, Resend, GoDaddy) | After landing page push |
| 9 | Travis | Pick which hero/page images he wants from the Stan Martinez batch — Andres will swap them in for review first | Ongoing |

## Feature requests captured (future)

- **On-the-fly custom email to upcoming event attendees.** Today Travis can only edit the templated 24-hour or follow-up email; he asked for an ad-hoc email tool. Andres: "We can look at that."
- **Search check-ins by guest name instead of ticket number** — Andres flagged this himself: "I can actually change that to be the name so that you guys don't have to type this entire thing."

## Platform features demoed (for KB synthesis)

- **Event creation:** image, description (autofill from artist name via Gemini — currently broken), opening time + show times (e.g. 7:30 show, 9:00 next slot), ticket pricing (free or paid), max 10 tickets per purchase, multiple ticket tiers, custom tier labels.
- **Organizer / artist accounts:** add organizer email → send organizer email → they log in to their own dashboard to see real-time tickets sold.
- **Check-in:** QR scan via phone camera OR search by ticket number/name. Attendance % live. Single-tap check-in.
- **Multi-user staff access:** invite additional team members by email (e.g. `info@meridianbuda.com`) — they get an invite, activate, can check in guests.
- **Analytics:** revenue by event, tickets sold by tier (VIP, general admission, etc.), event attendance, no-shows, recent orders, in-flight (started but not completed) orders with ping-by-email follow-up.
- **Bookings inbox:** form submissions land here with status pipeline (new → contacted → confirmed / declined).
- **Menu management:** add/remove/edit menu items.
- **Email flows:** confirmation (with PDF ticket attached) → 7-day reminder → 24-hour reminder → post-event follow-up. All editable, all toggleable on/off, variable inserts (name, event title, event date, CTA).

## Raw transcript (WebVTT, condensed to dialogue)

> Full WebVTT with timestamps preserved at `outputs/teams/2026-05-12/travis.vtt`.

**Andres:** So you might have some recurring events. We can create a recurring event option — weekly until you go in and cancel it.

**Travis:** Right. Yeah.

**Andres:** Perfect. So let's take an artist — could be a comedian, let's say Kiltoni. [Tries autofill] Oh, let me change the API key. Gemini replaced this model, so we just need to upgrade it to the new model. I'll let you know when that's ready. So you click autofill and it should find the artist if they have a press kit somewhere.

**Andres:** Okay, so tonight at 7:30, and then 9 to 9:30 the next slot. These ones are going to be free, so that's fine — but at least you get a sample of who's coming.

**Travis:** Right, yeah. Because I'd say RSVP.

**Andres:** You can add an organizer. There's a link for the organizer — for the artist or promoter — they log in to their own setup, see how many tickets are sold.

**Andres:** As many tickets as they want, up to 10. If there's multiple ticket selections, you can add them — general admission and anything else.

**Travis:** Do you think you can customize that general admission just to say like RSVP?

**Andres:** Oh yeah, absolutely. Customize to anything. [Demos purchase flow.] There's a confirmation. Download the PDF ticket on your phone. And then when they come in, you can do check-in.

**[Andres tries to demo check-in but the button stays disabled even after moving event time live]**

**Andres:** Okay, this should have opened it for you. So this becomes blue, you check in guests right away — scan QR or search by name. But I need to work on this because...

**Travis:** Yeah, looks like it still has the 6:30.

**Andres:** Yeah, when I moved the time it should have updated right away. I'll work on this. Let me make some notes. Oh, I know exactly what I did — I changed the wrong time.

**[Demo continues — check-in works after correct time change]**

**Andres:** This opens on your phone, opens the camera or you type in the ticket number. I can actually change that to be the name so that you guys don't have to type this entire thing. There you go, boom. Person is already checked in. Attendance 100%, tickets sold 1, checked in 1.

**Travis:** And can we have another login for the staff, like info@meridianbuda.com?

**Andres:** Info at meridianbuda.com — yes, team tab, so you can assign them. You'll send an email to that account, activate it, and you're good to go. That gives you flexibility — anytime someone doesn't have access, "let me send you an invite, sign in, check people in."

**Travis:** Cool.

**Andres:** Okay so analytics — seven days, 30 days, 90 days, all time. Revenue by event. Tickets sold by tier — VIP, general admission. Event attendance, no-shows, recent orders. Down here, people who started but haven't submitted — you can ping them with an email. Bookings — if someone submits a request on the form, they're all here. New / contacted / confirmed / declined. Menu — add, remove, change, update anything.

**Andres:** Email flows. Every time someone buys a ticket, they get the confirmation. Seven-day reminder. 24-hour reminder. Post-event follow-up.

**Travis:** Zoe — travis@zoiwell.com.

**Andres:** You can edit the emails here — write a different one, insert variables (name, event date), turn off or back on.

**Travis:** Is there a way to send a custom email to an upcoming event just on the fly?

**Andres:** No, there's no email creation tool yet, but we can look at that.

**Travis:** But I could update the 24-hour one.

**Andres:** Correct, to whatever you want. Update the 24-hour, the day-of, the follow-up "thank you for coming, book more, get another ticket."

**Andres:** Okay, I need a favor. Which email are you going to use to manage everything — Travis at Zoewell.com?

**Travis:** Yeah.

**Andres:** Okay. I need you to sign up for two things. First, GitHub.com. I want everything created under your account from the beginning, so as we deploy things out it's all yours. Use email and password (not Google), then change your password after. Send me that. We take care of everything, load it for you, hand it all over. I want to make sure you always have that control.

**Andres:** You don't pay anything on GitHub, you don't pay anything on Vercel where your site will be hosted, and you don't pay anything for Resend unless you send more than 1,000 emails a day.

**Travis:** Alright, got the account.

**Andres:** Perfect. Send it. Email or here, whichever. We'll put all your credentials in a doc and share access with you.

**[Discussion of Stan Martinez hero images, GoDaddy access]**

**Andres:** Where is your website deployed? GoDaddy? I need access so I can deploy. Add me as admin.

**Travis:** I sent you an invite to GoDaddy.

**[First invite didn't land — Travis sends second]**

**Andres:** Got it, I'm in. Awesome. I won't push — I'll send you the update with a couple of images first. Once you say "I love that one, push it," I'll push.

**Travis:** Alright.

**Andres:** Any other questions?

**Travis:** Not right now.

**Andres:** By tomorrow I'll get this done. Fix the bugs from today, replace the API key, push the landing page.

**Travis:** Sounds like a plan.

**Andres:** Awesome my friend, thank you so much, I appreciate you.

**Travis:** Thanks, Zane. Have a good one.

(Meeting ends 19:01 UTC / 2:01pm CT.)

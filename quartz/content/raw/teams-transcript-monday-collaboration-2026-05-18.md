---
type: teams-meeting-transcript
ingested: true
ingested_at: 2026-05-18
date: 2026-05-18
meeting_subject: Monday Collaboration
graph_meeting_id: MSo5NzgyZTJkNC1iZDYxLTQwYTUtYTcxZi04NGMyMjg1NzFmMGUqMCoqMTk6bWVldGluZ19PVFJqT1dKbE5EZ3RZamxpT0MwMFlqQTJMV0prWVdVdFpEZzBOMlE0TUdJek1tVmhAdGhyZWFkLnYy
transcript_id: ktVizInGAAAAi_B6lATZRTE5Om1lZXRpbmdfT1RSak9XSmxORGd0WWpsaU9DMDBZakEyTFdKa1lXVXRaRGcwTjJRNE1HSXpNbVZoQHRocmVhZC52MqEw2Tw4ODkzMjAxMC1lMjFiLTRjZTAtOWZhMC1jNGQ1MGE5ZmYzNjktMTc3OTEwODA0My1UcmFuc2NyaXB0VjI=
---

# Teams Transcript — Monday Collaboration — 2026-05-18

**Meeting subject:** Monday Collaboration (recurring Moil engineering working session)
**Date:** 2026-05-18
**Transcript window:** 12:40:43 UTC → 14:33:10 UTC (~1h 52m of captured audio)
**Organizer:** Jacob Oluwole
**Source:** Microsoft Graph `/me/onlineMeetings/{id}/transcripts` (transcript-V2)

## Attendees / Speakers

Per the calendar event and transcript speaker tags:

- **Jacob Oluwole** — VP of Eng (lead, organizer) · 616 utterance cues
- **Adeleke Tolulope ("Steve")** — Engineering · 325 cues
- **Abiodun Adekanmi ("Ablad")** — Engineering / content · 357 cues
- **Taiwo Ola Balogun** — Engineering · 21 cues
- **Andres Urrego** — CEO · 6 cues (joined briefly at 00:00 then left for daughter's school)

> ⚠️ **Transcript quality:** Microsoft Teams' speech-to-text struggled heavily with this call — strong Nigerian-English accents, simultaneous speech, music/audio playback through speakers, and intermittent network drops. Many cues are unintelligible. Treat the verbatim transcript as best-effort. Decisions and action items below are extracted conservatively only from clear segments.

## Topics covered (high confidence)

1. **Andres' opening directives (00:00–01:10)** — three project handoffs before he stepped out:
   - **Feed Logic** — not pushing to production until the website rebuild is done (someone else is rebuilding the marketing site).
   - **Meridian** — ready it, test it, then partner pushes when comfortable.
   - **Design / PowerPoints** — "Stevie" (Adeleke) to finish design work on the PowerPoints + HTML so it's "good to go."

2. **Brand DNA / image-generation feature on staging (~00:03–00:13)** — Adeleke walked Jacob through a new staging feature that:
   - Scrapes a customer's website HTML.
   - Extracts brand tokens (fonts, colors, voice).
   - Uses those tokens to generate a "mini website" preview and feed image generation.
   - Has a fallback "generate branding" path for customers without a website (upload brand PDF, or manually input company name/description/colors).
   - Open issue: the multi-step and "coach" steps aren't fully aligning on the extracted tokens; Adeleke is adding a manual color-customization control.

3. **Testing logistics for three projects (~01:18–04:00)** — Taiwo will send testing account credentials (emails + passwords) for three projects so Jacob can test this week; team plans a call by end of week to deploy live with each customer.

4. **Crawler / scraping concern (~17:00–18:00)** — Abiodun asked whether prod prevents AI/bots from crawling. Adeleke clarified: public pages are intentionally SEO-open; the authenticated app is protected.

5. **"Request a demo" / "Schedule a demo" on the marketing site (~37:00 and ~58:50)** — Jacob pushed to add a Request-a-Demo flow (login exists, demo flow doesn't). Repeated multiple times — a clear ask.

6. **Social / outreach channels (~40:00, ~1:04)** — discussion of Instagram, Facebook, LinkedIn presence; Jacob wants to use his personal LinkedIn business account for outreach and customize cold messages by location.

7. **Generative content QA (~1:28–1:51)** — Abiodun read aloud sample AI-generated marketing copy ("Social Metrics Pro" demo, social-media best-practices script, "Launch your startup" pitch, and a satirical critique about "40-page business plan in 6 seconds … 12 strategies, 11 of which are the same strategy reworded"). This was apparently QA of Moil's content-generation output.

8. **Email delivery bug (~1:50)** — Jacob reported he can download the business plan PPT but is not receiving the confirmation email; suspected delivery issue worth investigating.

## Likely decisions

- Hold **Feed Logic** production push until the new marketing-site build is complete.
- **Meridian** is to be readied + tested internally; the partner (Inna Benyukhis?) will trigger the push when she's comfortable.
- Add a **manual brand-DNA input** (name + description + colors + fonts) as a first-class alternative to website-scrape, on the staging brand-DNA flow.
- Add a **Request a Demo / Schedule a Demo** entry point on moilapp.com.

## Likely action items

- [ ] **Taiwo** → send testing account emails + passwords for the three projects to Jacob (this week).
- [ ] **Jacob** → test Meridian and the brand-DNA flow on staging; give feedback to Adeleke.
- [ ] **Adeleke** → ship the manual color/customization control on brand-DNA, resolve multi-step ↔ coach token mismatch.
- [ ] **Adeleke** → finish PowerPoint + HTML design work (Andres' opening directive).
- [ ] **Jacob / team** → add Request-a-Demo flow on the marketing site.
- [ ] **Investigate** business-plan PPT email-delivery bug (download works, email doesn't arrive).
- [ ] By **end of week**, team to sit on a deployment call with each of the three test customers.

> Action items are inferred from the clear portions of the transcript — please confirm with Jacob before treating any as binding.

## Other meetings checked today

- **Astra Ribbon Cutting** (16:30–18:00 UTC) — no transcript (no attendees, Andres-only block).
- **Team Meeting (Goal setting)** (13:30–14:30 UTC) — only one transcript on file, from `2025-06-02` (old occurrence of the recurring series); no transcript for today's instance.
- **Buda HIVE Cohort 4** (23:30–01:30 UTC) — not a Teams online meeting (in-person at EDC Hive).

## Verbatim transcript (cleaned, speaker-tagged)

> Time in `MM:SS` from call start. Cues coalesced by speaker. Quality caveat above applies.

[00:00:03] Andres Urrego: We need feed logic, we need to go on my feed logic.com or the other website. We're not going to push that out anytime soon until our website is completed by someone else. And then for Meridian, Meridian, we need to have it ready, we need to test it, and then he'll be able to push, you know, whenever he's ready and feels good about the testing. Okay.

[00:00:28] Jacob Oluwole: OK, yeah, I just, I just joined. I was, I was connected for a while. Good morning, Rodriguez.

[00:00:29] Taiwo Ola Balogun: Okay, sir.

[00:00:33] Andres Urrego: That's okay. I sent you a message. Taiwo can catch you up. I'm walking into my daughter's school right now, so I'll keep you guys posted, all right? I'll be back in a couple of hours, maybe an hour or so. And then hopefully we've moved along on some of these things. Jacob, there's some design things that we need to push to production. I think the HTML thing is already good to go.

[00:00:38] Jacob Oluwole: Okay.

[00:00:41] Taiwo Ola Balogun: OK, so.

[00:00:46] Jacob Oluwole: Yeah.

[00:00:56] Andres Urrego: Stevie's gonna work on a couple of, Stevie's gonna work on a couple of things for the PowerPoints and the design, and then we should be good to go. But I gotta go, okay guys? I'll talk to you soon.

[00:01:08] Jacob Oluwole: Alright, miss.

[00:01:10] Andres Urrego: Thank you. Talk to you guys in a bit. Bye bye.

[00:01:16] Jacob Oluwole: Yes, um, Taiwo, yeah.

[00:01:18] Taiwo Ola Balogun: Um, Jacob, so... The thing is, I'm going to be sending the passwords and email of the testing accounts for the three projects. So I think, and they say you're going to be, you're going to like write out the email that are going to be sent to them to test out. So I'll send the link, I'll send the link, I'll send the email, I'll just send the password. So. Those is to like type out the message they are going to be sending out to them.

[00:01:48] Jacob Oluwole: Okay. What does it again?

[00:01:53] Taiwo Ola Balogun: Well, that's what's on that is.

[00:01:53] Jacob Oluwole: Yeah.

[00:01:56] Abiodun Adekanmi: St.

[00:01:57] Jacob Oluwole: Yeah, he, OK, he said everything has been everything has been done, so I will, OK, I will. So, if I test and I find out anything, I'm actually going to send out those emails, or you just fix them and just we will send.

[00:01:59] Taiwo Ola Balogun: But you listen. Yeah, they they they they they go right now is for them to be able to test this week. OK.

[00:02:17] Jacob Oluwole: Mhm.

[00:02:18] Taiwo Ola Balogun: So.

[00:02:19] Jacob Oluwole: Okay.

[00:02:20] Taiwo Ola Balogun: So, by the end of this week, we are going to, like, sit on a call with each and every one of them and deploy to write the on that call.

[00:02:25] Jacob Oluwole: Okay. Open. Okay.

[00:02:40] Taiwo Ola Balogun: But even though we push it to production, they are still going to have to test it.

[00:02:50] Jacob Oluwole: All right, I will test it. I will jump on the on the on the testing now.

[00:02:50] Taiwo Ola Balogun: Yeah. Okay.

[00:02:59] Jacob Oluwole: No, I'll give you feedback on niche, uh, those may the may the meridian fear.

[00:03:00] Taiwo Ola Balogun: Okay, no problem.

[00:03:07] Jacob Oluwole: Results, test results - have you, like, have you done anything on them?

[00:03:13] Taiwo Ola Balogun: Like, you can go test on every time the game.

[00:03:13] Jacob Oluwole: Decent.

[00:03:16] Taiwo Ola Balogun: I did work on them.

[00:03:16] Jacob Oluwole: Okay. Okay, let me check them out again. All right. You have any other thing for me?

[00:03:24] Taiwo Ola Balogun: Ohh, no, I love Yancey for my end again.

[00:03:31] Jacob Oluwole: Steve, he said you are going to be working, you are still working on some things on staging.

[00:03:39] Adeleke Tolulope: Yeah, like we added a new. Is 9 in this, so yeah, there are some improvement on staging. Yeah. Like, initially, if you know all the informative changes, can you hear me?

[00:03:54] Jacob Oluwole: Yeah, I can hear you.

[00:03:57] Adeleke Tolulope: So, the changes on staging. Let me show you, because I don't know how I can explain this. Oh my God, retrieve this to you.

[00:04:14] Taiwo Ola Balogun: Jacob, have you like checked out this connect text?

[00:04:19] Jacob Oluwole: He's young.

[00:04:21] Taiwo Ola Balogun: Yeah, yeah, yeah, yeah, I was shaking the house.

[00:04:24] Jacob Oluwole: I already, I already saw it, I already tested the import, and I haven't done much, I haven't done any entire testing on it. Well, I've seen it, I've logged in. They done design with school.

[00:04:37] Adeleke Tolulope: That I see, or something. Put it in. Because of something. Okay, we can take KID. Okay, thanks for asking. Ohh, they talk is bad doing very soon. You're not better to me. Thanks, Miss Green.

[00:05:15] Jacob Oluwole: I can see the screen.

[00:05:20] Adeleke Tolulope: So, over here, right, this is the change we need if you. HTML, your link here, right? It's going to extract some basic information from it. But Andres worked on something that it created a kind of a mini website, a mini HTML file that displays to your brand and everything. So it does.

[00:05:31] Jacob Oluwole: And. Mhm. Uh-huh.

[00:05:46] Adeleke Tolulope: So, what is there on this report now, with this report? To a mini kind of websites with that brand. Are you talking to your body? So this is for when I think the my lab stuff. brand, our fonts, the colors, so you get this one. So these are the ones that this is now what we are now using for this is what we are now using to.

[00:06:14] Jacob Oluwole: And.

[00:06:20] Adeleke Tolulope: As, like, as the brand DNA, right? If not to create an image, right? So it now takes these colors, like we extract some, we extract talking from this page, know that we are sending this whole HTML, right? The but the I started the the phone, the colors, right? I use that as the.

[00:06:42] Jacob Oluwole: Moil. Mm-hmm. Yeah, but there is this.

[00:06:49] Adeleke Tolulope: You have brand, you need to create the image, so yeah, that that's what we are working on, huh?

[00:06:55] Jacob Oluwole: Boys, yeah, I tested this out last week, last Friday, and I saw that it was showing green too, and we never had like green as but major. My job and I call.

[00:07:09] Adeleke Tolulope: You do have green.

[00:07:10] Jacob Oluwole: Hello, do we not have green on?

[00:07:14] Adeleke Tolulope: You sure?

[00:07:14] Jacob Oluwole: You only have that second one, and that the other ones, like, I can touch the other ones, no, no, go back, go scroll up.

[00:07:19] Adeleke Tolulope: This one.

[00:07:23] Jacob Oluwole: The other ones, first one, third one, 4th one, we had this one, but we have this one, but green, I hope he testing few tests, so you can know.

[00:07:24] Adeleke Tolulope: Lisa. Did you? On this one. We have one day.

[00:07:39] Jacob Oluwole: Once you get me done now, we will move in context to me.

[00:07:39] Adeleke Tolulope: Even when I, when I, when I, when I, when I...

[00:07:40] Taiwo Ola Balogun: Hello.

[00:07:44] Adeleke Tolulope: Yeah.

[00:07:45] Jacob Oluwole: No, they're actually in the end.

[00:07:46] Adeleke Tolulope: It. As out.

[00:07:54] Jacob Oluwole: Hello, call me.

[00:07:54] Adeleke Tolulope: Then. You. Balogun.

[00:07:58] Taiwo Ola Balogun: Emma, let me.

[00:08:02] Adeleke Tolulope: Thank you. You know, so Jacob.

[00:08:05] Jacob Oluwole: Chair, you got to raise on you, both, he is a major, you know.

[00:08:07] Adeleke Tolulope: We both. From my store.

[00:08:13] Jacob Oluwole: Zane. It's not a major building.

[00:08:16] Adeleke Tolulope: We actually, we actually still, we actually still working on what we've done so far. Hope this call is not recorded. What we've done so far, we've been able to replicate what Andres, the latest experiment Andres did on the side.

[00:08:21] Jacob Oluwole: Tiny fish. Is that what they're doing? Transcript.

[00:08:37] Adeleke Tolulope: Right, you want us to bring it over so that people get to see this kind of nice thing that we design for them, right? And then we now extract tokens from it, right? We extract tokens like the fonts, the colors, and everything to use it to create the voice code.

[00:08:45] Jacob Oluwole: Thank you.

[00:08:57] Adeleke Tolulope: to use it in the image creation to improve the image creation better. So, but there are still a kind of... Conflicts that we. Are still working on, we are still trying to make sure that the the multi-sixty and coach are challenging this information, right? These are the information for where it's going. For job, uh, so you can even edit it, so... He did it right, and he's not that there are some things that are not really aligning, so he said we should add this customized that you can customize the color right? Can you can set the color yourself if it didn't perform better right, but at least it's.

[00:09:41] Jacob Oluwole: And. Is there a way I can input this without putting my website?

[00:10:10] Adeleke Tolulope: Without putting your website, no, no, no, no, it created from your website. You have to, you have to your website, it goes to your website.

[00:10:18] Jacob Oluwole: Like, I want to upload my phones. I want to do my brand DNA now. Is there a way that I can manually submit or mean my primary color, my primary colors, my secondary color, my font type, my, everything that I can manually put it instead of using. If I don't have a website, because if I'm trying to build a business, I am searching for a business plan.

[00:10:27] Adeleke Tolulope: Mhm.

[00:10:45] Jacob Oluwole: Trying to do everyone at Saint Jeremy on one year, but I don't have security.

[00:10:48] Adeleke Tolulope: Ohh, if you want. You don't have a website, but there's a part here that I upload a brand PDF. Maybe you have a brand, right? You want to create a website, so you have a brand, you have a problem you want to use, the application you want to use, so you can, yeah.

[00:11:03] Jacob Oluwole: I'm saying, I'm saying that, just like we have, I know, I really do on on just.

[00:11:12] Adeleke Tolulope: You can upload it here, right? Then it's going to start the colors and everything's going to fill out these things for you. But what I've tested is that I don't know.

[00:11:18] Jacob Oluwole: Yeah, you still not getting it? I said, I said, is there a way I can manually? Can I manually update my brand DNA? Yes, manually app. Yeah, I don't see, I know that is the upload feature. I know there's the upload feature, I know there's a website feature, but can I manually impute those feeds like those?

[00:11:27] Adeleke Tolulope: I'm trying to answer your question now, like maybe you wait a minute. Aha.

[00:11:46] Jacob Oluwole: I'm ready to eat.

[00:11:51] Adeleke Tolulope: Sure, like, for example, over here now, generate branding. Over here, you can give it a name, right? Write all what you want to write, your company description, your colors, everything, everything you want to write, it generates. That's going to generate these things for you. But what I haven't tested is if it's going to actually create this kind of website for you.

[00:11:55] Jacob Oluwole: Mhm. Mhm. Mm-hmm. Mhm.

[00:12:10] Adeleke Tolulope: Change it, but for the manner, but like this is if... Optional based from your website, if you are unable to scrape it right, you can input your name, write all what you want to write here, and then it generates. Then it works. He is going to give you this results. You can test it out, sir. You can test it out, but I believe he's going to work.

[00:12:26] Jacob Oluwole: Okay, okay, no. OK, thank you. Yeah, test.

[00:12:36] Adeleke Tolulope: What, what I can't, what I can do? What I can really say is that if he's actually going to create this, so it's something that we can test, so we don't usually tackle the any bug I want to arise from, definitely, right?

[00:12:51] Jacob Oluwole: And. No.

[00:12:54] Adeleke Tolulope: Yeah. I want to go up.

[00:13:06] Jacob Oluwole: I, I already hear you.

[00:13:08] Adeleke Tolulope: Play.

[00:13:14] Jacob Oluwole: You are drinking.

[00:13:17] Adeleke Tolulope: I think. Is.

[00:13:22] Jacob Oluwole: Yeah, we can say. Hello?

[00:13:36] Adeleke Tolulope: Ohh.

[00:13:37] Jacob Oluwole: I think it's your network.

[00:13:39] Adeleke Tolulope: Mm. You should.

[00:13:54] Jacob Oluwole: I know.

[00:13:58] Adeleke Tolulope: No. 'Cause. No. Yeah. Point, point.

[00:15:16] Jacob Oluwole: Well, my God, thank you, Jesus.

[00:16:00] Adeleke Tolulope: Yeah. My back online.

[00:16:27] Jacob Oluwole: I'm like Mumbai, can you can make them still image?

[00:16:36] Abiodun Adekanmi: Mm.

[00:16:38] Jacob Oluwole: No, you're saying.

[00:16:42] Abiodun Adekanmi: GPT.

[00:16:46] Jacob Oluwole: When we ran. Everything we like. I think I think because.

[00:16:55] Adeleke Tolulope: What?

[00:17:00] Abiodun Adekanmi: Yes. And the man goes off to young dressing and money. Money projects. So if any more describe.

[00:17:15] Jacob Oluwole: I thought you.

[00:17:16] Abiodun Adekanmi: But is there a way down on Dev? Do you guys prevent AI from crawling the page or you have no control by it crawling our website?

[00:17:17] Jacob Oluwole: Yeah. Did you?

[00:17:31] Adeleke Tolulope: We actually, we we actually the reason, the reason for.

[00:17:31] Abiodun Adekanmi: Okrolin.

[00:17:39] Adeleke Tolulope: SCO is for caller to be able to have access to the public part of the website.

[00:17:43] Abiodun Adekanmi: Okay.

[00:17:48] Adeleke Tolulope: Yeah, so any past stuff affect.

[00:17:48] Abiodun Adekanmi: Okay.

[00:17:52] Jacob Oluwole: They talk way back.

[00:17:52] Adeleke Tolulope: No, that has authenticate and login, so that.

[00:17:56] Abiodun Adekanmi: Mm.

[00:18:04] Adeleke Tolulope: So, that, so that I can be a problem not be to scrape. Prior. For these uh webs. Again, that's actually the more the in a better way. That means the SEO is like is good enough, right? But yeah, but better see most job BBC. Yeah, I do. Just get some stuff. The the website is not really there.

[00:18:49] Jacob Oluwole: And.

[00:18:56] Abiodun Adekanmi: I think I understand what you mean.

[00:18:57] Adeleke Tolulope: But, I had, I'm not was open.

[00:18:58] Jacob Oluwole: In like what?

[00:19:01] Adeleke Tolulope: Okay.

[00:19:04] Abiodun Adekanmi: Monster as a follow-up, because...

[00:19:07] Adeleke Tolulope: Show me shaking, show me shaking for Monday morning.

[00:19:11] Jacob Oluwole: Hello, you can talk, Casey.

[00:19:16] Abiodun Adekanmi: Hey, Cortana, play.

[00:19:18] Adeleke Tolulope: Ohh, ohh man.

[00:19:21] Abiodun Adekanmi: Every man's friend.

[00:19:21] Adeleke Tolulope: Kim, hello. MTA and 8P, I don't know.

[00:19:30] Abiodun Adekanmi: And. Abiodun. Are you frustrated, bye bye?

[00:19:42] Adeleke Tolulope: Thunder. Come on now, I will just, I will just get starting, starting because I was going to, but we're going to.

[00:19:54] Jacob Oluwole: It will all land.

[00:19:58] Adeleke Tolulope: We don't, I want to do, that's why I gave question.

[00:19:58] Abiodun Adekanmi: Mhm.

[00:19:59] Jacob Oluwole: Yes. You have, you have a, you have a, you have a.

[00:20:17] Adeleke Tolulope: Nothing. Rather, I need you to be not be not in the world. You see, they are conducting major. Respect ID.

[00:20:28] Abiodun Adekanmi: Yes. In the busky.

[00:20:34] Jacob Oluwole: You have, you have, well, she said.

[00:20:48] Adeleke Tolulope: All right. I'm sorry, the way that, my mom, my mom, you know, my father, you know, is it the public that she wants to park and the country is this? What is it? Ola. Jet number.

[00:21:20] Abiodun Adekanmi: For nights, me and the get internet for my studying. Once. For detail, ladies. Now, guest room and my bedroom meeting. So, I'm gonna put my phone in the bedroom.

[00:21:35] Adeleke Tolulope: And. Ohh, actually, but they be no 5G. They work on my phone, like 5 the speed, the speed. Now, there is no room, no way, no way to do 5G. I have to do the router, router, really. Can you talk with my machine, can you talk with drums?

[00:21:49] Abiodun Adekanmi: If. And...

[00:22:02] Adeleke Tolulope: You need.

[00:22:03] Abiodun Adekanmi: It. Ohh.

[00:22:06] Adeleke Tolulope: There was a thing. I don't exhaust all the data waiting for those location. I don't even want to carry and go like this. But you sue me as well, don't tell me. And. Is working. He did that.

[00:22:46] Jacob Oluwole: Okay, after I share, you know, because he does this thing with the money time, not anything more.

[00:22:56] Adeleke Tolulope: When, when the cable was created, this was to get an integrated page.

[00:22:56] Jacob Oluwole: Guys, test.

[00:22:56] Abiodun Adekanmi: Mm.

[00:23:03] Jacob Oluwole: The guy with the email. Doing. Is no. 26 and 0.

[00:23:43] Abiodun Adekanmi: Steve up, Casey.

[00:23:44] Jacob Oluwole: Mhm. Okay, still gonna share screen.

[00:23:53] Adeleke Tolulope: Thank you.

[00:23:57] Abiodun Adekanmi: Hope that's you.

[00:23:57] Adeleke Tolulope: At least we tried, we tried our best. But it did, but that's not. Ohh, should I stop sharing?

[00:24:09] Jacob Oluwole: We have a little right now. How many minutes?

[00:24:18] Adeleke Tolulope: Ohh. Mom.

[00:26:37] Jacob Oluwole: Okay, okay, sorry, I'm not, I'm just, this call is transcribed. He's asking me about emails that I sent last week. I have an email. Because. In. I was in. What? Beginning of my saying that me. Tell Mom. I can do this one. If you know Donna, because he know he know ask about them. Well, I know they only got this over last week, I see.

[00:27:48] Adeleke Tolulope: Yeah.

[00:27:51] Jacob Oluwole: Most I use, hey, I'm bloody a guy.

[00:27:59] Abiodun Adekanmi: Mm. Yeah, I don't ever start getting for a month. It's off, we are talking with you pretty no.

[00:28:08] Jacob Oluwole: Object. Hey, you look good, Gabby.

[00:28:10] Abiodun Adekanmi: Yeah. No, let me look at your Google account me.

[00:28:18] Jacob Oluwole: Give me that.

[00:28:20] Abiodun Adekanmi: Google, Google. It is very, yeah.

[00:28:26] Jacob Oluwole: Andre is the Mini Coke counter. And we look our company in.

[00:28:33] Abiodun Adekanmi: Go to.

[00:28:34] Jacob Oluwole: Shoot.

[00:28:35] Abiodun Adekanmi: Okay. Insect. Okay. Mmh. Mhm.

[00:29:13] Jacob Oluwole: Mm. You guys want with.

[00:29:17] Abiodun Adekanmi: Yeah.

[00:29:24] Jacob Oluwole: Like, I clear with you and be right myself. B.

[00:29:44] Abiodun Adekanmi: Seven. Thank you.

[00:30:34] Jacob Oluwole: Thank you. We have been and we got there. No.

[00:30:48] Abiodun Adekanmi: How many windows?

[00:30:51] Jacob Oluwole: I will. My, my, after school, my shorts are down. Home for Yancey, baby. Hope I can see the little. Yes, you need. Ohh, my God! We don't put the one, one hour moving post content to like one hour. I want to post content on my on my system. I post content Inna. Yeah, I must do it on the system. One hour, and he told me what a charging bridge at us, what is the word network system in my hang?

[00:31:30] Abiodun Adekanmi: Mhm.

[00:31:40] Jacob Oluwole: Ohh, I move mouse by mouse on when you move.

[00:31:41] Abiodun Adekanmi: Mm.

[00:31:47] Jacob Oluwole: Come on, we.

[00:31:48] Abiodun Adekanmi: From my dear, from my dear Lango.

[00:31:51] Jacob Oluwole: Ah, man.

[00:31:52] Abiodun Adekanmi: Then, might have been with them. Find your own, kid.

[00:31:57] Jacob Oluwole: No wonder, no wonder, no wonder. Will you be happy? Wow, I live in OK at my share, at my share, share, share, share, share. I feel our posts. Sorry, we keep my posts on one hour for 12 minutes. Testing. Hey, I should copy caption, yeah, but we find a little bit better, so, but what do you mean by?

[00:32:22] Abiodun Adekanmi: And.

[00:32:30] Jacob Oluwole: I'm actually school of silent.

[00:32:35] Abiodun Adekanmi: Hello. Mm. Yeah. Mm. Yeah. Yeah.

[00:33:17] Jacob Oluwole: It's right.

[00:33:21] Adeleke Tolulope: I think it could have gone.

[00:33:25] Jacob Oluwole: Inna. OK, Mulik.

[00:33:27] Adeleke Tolulope: All right.

[00:33:34] Abiodun Adekanmi: Mm.

[00:33:35] Jacob Oluwole: It actually mean me before from Gary.

[00:33:36] Abiodun Adekanmi: Thank you.

[00:33:42] Jacob Oluwole: How about you?

[00:33:47] Adeleke Tolulope: Andres.

[00:33:49] Jacob Oluwole: What you typing in? What's in that room? When I'm in doubt, I'm always when in doubt, I'm always get rid of me.

[00:34:01] Adeleke Tolulope: How do we make sure that the briefing only talks about the same things and what I understand? Okay.

[00:34:09] Abiodun Adekanmi: At least it's.

[00:34:18] Jacob Oluwole: OK.

[00:34:20] Abiodun Adekanmi: Stop and sit. I. In Gumba. I will do.

[00:35:17] Jacob Oluwole: So, method by me, the method I don't want to be. Mhm.

[00:35:32] Adeleke Tolulope: Yeah.

[00:35:35] Abiodun Adekanmi: Yeah.

[00:35:37] Jacob Oluwole: Sure, a shield. Also a shield. When you be in mighty, mighty or got. I might get missing.

[00:35:40] Adeleke Tolulope: Yeah.

[00:35:48] Abiodun Adekanmi: Hmm.

[00:35:48] Jacob Oluwole: Two weeks ago, only we can send email.

[00:35:49] Adeleke Tolulope: What? Oh, and Jim, you did my Jim now, which is my father Sunday.

[00:35:55] Abiodun Adekanmi: Three months.

[00:35:57] Jacob Oluwole: Go out again. I'm not nothing. Who am I located?

[00:35:58] Adeleke Tolulope: Yeah.

[00:36:06] Jacob Oluwole: Two weeks ago, only we can send emails someone. So, when you might send a weekend, me, I send a weekend because we more interface are following.

[00:36:15] Abiodun Adekanmi: Yeah.

[00:36:20] Jacob Oluwole: I finished it maybe one in the morning. I'll be your Tuesday. Shake it. I can't did it. What's all making me two weeks ago? I didn't do it like last week. He didn't say anything about it. He didn't say anything about it. I will. I should not do it.

[00:36:23] Adeleke Tolulope: No problem.

[00:36:28] Abiodun Adekanmi: Mm.

[00:36:44] Jacob Oluwole: Jacob, I told you, like this. Two years, so I need to last move more. You are on some money. I'm glad, give me a full choppy and I love you, because. Can one day, one day? This is what I've been talking about.

[00:37:15] Adeleke Tolulope: Is not a compromised scheme.

[00:37:21] Jacob Oluwole: Request a demo now. Yeah, can you request a demo in the website? Guys, request a demo on the website. I like them. Then we have one first, give me a bee.

[00:37:38] Abiodun Adekanmi: Hey.

[00:37:40] Jacob Oluwole: And when you got teachers with this on the way they like demo, can they call? I'll go to actually go and get the demo, OK. Contact us, how to read them now? Guys, contact us, go to demo, contact us. Can you call?

[00:38:02] Abiodun Adekanmi: Mm.

[00:38:03] Jacob Oluwole: But only. They might be searched about their company, BSU related. And I will really want to see you.

[00:38:16] Abiodun Adekanmi: Mm.

[00:38:19] Jacob Oluwole: Today, it is off.

[00:38:23] Abiodun Adekanmi: Okay.

[00:38:23] Jacob Oluwole: Contact us. Okay, then come. I'm gonna know. I know. Where's the demo? Do you just? Exactly. How much is your still points still point? I see.

[00:39:01] Abiodun Adekanmi: Yeah.

[00:39:09] Jacob Oluwole: Thank you, bye.

[00:39:21] Abiodun Adekanmi: The.

[00:39:27] Jacob Oluwole: Ohh, we got guys did their guys did their location. As did the allocation. My bad, you are not in your Jeremy.

[00:39:36] Abiodun Adekanmi: S.

[00:39:41] Jacob Oluwole: Where is that? Where is the? Where is the social media? Thinking little. My guys on Instagram and Facebook. Most of these guys? Dumu malu. But...

[00:40:16] Abiodun Adekanmi: One to 20. And. Yes.

[00:40:21] Jacob Oluwole: No, I can't do. I'll be just going, Andres is only, but what do you mean is then?

[00:40:32] Abiodun Adekanmi: Mm.

[00:40:33] Jacob Oluwole: Give me your voice.

[00:40:40] Abiodun Adekanmi: Mariana.

[00:40:44] Jacob Oluwole: What? Cesar.

[00:40:50] Abiodun Adekanmi: When we go thought, yeah, well, that will share a test.

[00:40:54] Jacob Oluwole: Okay, okay.

[00:40:57] Abiodun Adekanmi: Mm.

[00:40:59] Jacob Oluwole: That sounds working.

[00:41:00] Abiodun Adekanmi: No, you know she, I like to.

[00:41:02] Jacob Oluwole: Ohh.

[00:41:03] Abiodun Adekanmi: And 19 dent.

[00:41:23] Jacob Oluwole: Book you discovery for your who are on your website too. OK, so we call you. All requested them. Basic demo on our websites. Something like this, if demo is something that people. Get so done. Let's put it there. Can I even see I can I really get up my should take take take on long post. I don't do anything to relates to. This is it. These ways and these.

[00:42:16] Adeleke Tolulope: Dialing. Thanks. Oh.

[00:42:37] Jacob Oluwole: Ucha. Try, yeah. No, Tricia. But... Which I am. No code for entertaining us, no code, hmm, not good. I need back, I really need an Instagram. My name means like that. YouTube, Instagram, and LinkedIn. I'm like, if not, Instagram. I love you. That is some of influencer, even these guys talking about them. S. That means... Oh, he likes Botopo. And you guys don't have legs. How much?

[00:44:33] Adeleke Tolulope: Stop listening. I don't think it too. Remove. Mm. He's professional.

[00:45:16] Abiodun Adekanmi: I'm muted. They're not sharing your audio.

[00:45:18] Jacob Oluwole: And. It's gonna give me a.

[00:45:22] Abiodun Adekanmi: Okay, I can hear now. I can hear now.

[00:45:46] Adeleke Tolulope: Yeah. Bring your number. Please.

[00:46:32] Abiodun Adekanmi: Okay. There will be no code in the man.

[00:46:47] Jacob Oluwole: Yeah, I know. No. I, I, I, I, I, you know now.

[00:47:11] Abiodun Adekanmi: I left you in your black promoter. America.

[00:47:15] Jacob Oluwole: I know, please, please. Well, so you black for phone?

[00:47:22] Abiodun Adekanmi: Look, is that the?

[00:47:24] Jacob Oluwole: I know.

[00:47:27] Abiodun Adekanmi: Mmh.

[00:47:27] Jacob Oluwole: Hey, laptops one day on TV. I really not like my **** when you put it on my. And you still got the not on GP line.

[00:47:38] Abiodun Adekanmi: Mm.

[00:47:39] Jacob Oluwole: It should make sense. And it is something like this. Video.

[00:47:53] Abiodun Adekanmi: Mm.

[00:47:53] Jacob Oluwole: We like to be calling you now. I would like to be cleaning. I'm in your mom should be relatively big. For the record. It's not like. That we can. Hi, this evening.

[00:48:34] Abiodun Adekanmi: Mmh.

[00:48:39] Jacob Oluwole: Geography like. I don't know how to build a business plan. I think it is an idea. I don't even know how to do it. I don't even know how to do the business plan. Some comments on Facebook, from Facebook, forty-seven 9 like likes. Imagine snail lines, we can do it. Possibly.

[00:49:15] Abiodun Adekanmi: Send me the link, sir.

[00:49:15] Jacob Oluwole: We should feed you. No, no. On Facebook, like I can copy, link it right, copy that.

[00:49:34] Abiodun Adekanmi: No, okay, I mean, only brother, you are like.

[00:49:39] Jacob Oluwole: Li.

[00:49:43] Abiodun Adekanmi: You already know what to send it.

[00:49:46] Jacob Oluwole: The.

[00:49:46] Abiodun Adekanmi: Had to copy, and it was an Instagram, no.

[00:49:52] Jacob Oluwole: Like you might say, no.

[00:49:56] Abiodun Adekanmi: Copy.

[00:50:02] Jacob Oluwole: Hello, God. Like, like, he changes, he got this really bad.

[00:50:11] Abiodun Adekanmi: And. Emma. Hey, Uncle Jacob.

[00:50:18] Jacob Oluwole: Hey.

[00:50:23] Abiodun Adekanmi: Thank you, Jacob. Ohh.

[00:50:35] Jacob Oluwole: Yeah, I think my idea is not new. Yeah, I think I should be request the demo, request the demo must be present.

[00:50:37] Adeleke Tolulope: Thank you.

[00:50:47] Abiodun Adekanmi: Yeah.

[00:50:48] Jacob Oluwole: on the website and also on the teenage Taiwo beginning.

[00:51:11] Abiodun Adekanmi: What do you want? What do you want to do with laptop? Yes.

[00:51:19] Jacob Oluwole: Tamil addition.

[00:51:21] Abiodun Adekanmi: No programmer.

[00:51:25] Jacob Oluwole: Dubai tomorrow.

[00:51:26] Abiodun Adekanmi: Yep.

[00:51:31] Jacob Oluwole: My thing, right? Yeah, that's I wanna go like that.

[00:51:37] Abiodun Adekanmi: Yeah. The first is, if I next go see.

[00:51:43] Jacob Oluwole: Hmm.

[00:51:44] Abiodun Adekanmi: Not too silent.

[00:51:46] Jacob Oluwole: Okay. What are you building? Was anything there? What are you building? Ah, question. I need to make sense to get a lesson.

[00:51:58] Abiodun Adekanmi: The dog. Okay. Ohh, by the way, this is a lot. Calm down. Do you know that I own the laptop? Do not know. Okay, anything.

[00:52:21] Jacob Oluwole: But I'm not using back on any of you. Ohh, and Carlos has a cool one, continue.

[00:52:26] Abiodun Adekanmi: Oh. Mm. Give me 5 minutes, Adeleke.

[00:52:37] Jacob Oluwole: All right, so. How far to Tolulope?

[00:52:50] Adeleke Tolulope: No. I can't find, I can't find the visited key, the I can't find the log.

[00:53:03] Jacob Oluwole: Not find the words.

[00:53:05] Adeleke Tolulope: I don't find a little thing.

[00:53:10] Jacob Oluwole: Hey, boy. You couldn't find words.

[00:53:21] Adeleke Tolulope: I can't find the the information about the.

[00:53:25] Jacob Oluwole: Ahh. Then, because we deleted it.

[00:53:31] Adeleke Tolulope: I know. I need to get the dates that I create the app that I actually created a key. Right. The live band's not even playing names.

[00:53:49] Jacob Oluwole: You can reply and when you play, we deleted the game ball. I'm not for any information on it. We try retrieving it, but it's not working.

[00:53:51] Adeleke Tolulope: Company.

[00:53:58] Jacob Oluwole: If that is in those like.

[00:54:06] Adeleke Tolulope: I'm sorry. The projects and wrists. Business. And speed. Right. You are is gonna roll.

[00:54:54] Jacob Oluwole: Ohh my.

[00:55:01] Adeleke Tolulope: No.

[00:55:02] Jacob Oluwole: Okay. Mm. What's the next thing? Can you? You're too old and cheap. To my. Launch.

[00:55:21] Adeleke Tolulope: I think it's a good.

[00:55:24] Jacob Oluwole: I assume.

[00:55:27] Adeleke Tolulope: It gets strange, then you go to 2024.

[00:55:29] Jacob Oluwole: I'm getting on post.

[00:55:33] Adeleke Tolulope: When I started changing for me, what the **** is this? I think before I need that to be well. Why is all this changing?

[00:55:50] Jacob Oluwole: Yeah.

[00:56:01] Adeleke Tolulope: Very much. Play month, play time, we need, we need website, hopefully only 107 to the other thing.

[00:56:09] Jacob Oluwole: Flip that.

[00:56:14] Adeleke Tolulope: Nothing, nothing.

[00:56:23] Jacob Oluwole: Thank you. Let that let that that you. Yeah, yeah, yeah.

[00:56:40] Adeleke Tolulope: Oh, 324 have been. No, 24 will start to be open.

[00:56:44] Jacob Oluwole: Ohh, my gosh! Yeah?

[00:56:49] Adeleke Tolulope: So, the network is starting to work for me.

[00:56:52] Jacob Oluwole: It Will.

[00:56:52] Adeleke Tolulope: Gemini, Gemini. No worries.

[00:56:55] Jacob Oluwole: Also, do she? Did you not like that now?

[00:57:07] Adeleke Tolulope: I think I read it.

[00:57:11] Jacob Oluwole: Winning.

[00:57:12] Adeleke Tolulope: Actually, I was really busy. Jeremy, I basically interested. I could.

[00:57:19] Jacob Oluwole: Yes. I am going.

[00:57:21] Adeleke Tolulope: Hello.

[00:57:23] Jacob Oluwole: Oh well.

[00:57:25] Adeleke Tolulope: Mm. 2104. That was great. I created it on the 20th, 21st of mad. Hopefully.

[00:58:29] Jacob Oluwole: Manchi.

[00:58:35] Adeleke Tolulope: They think they just we have one review for we are the same to me, and I know they spend like almost two hours, 3 hours on this team now.

[00:58:44] Jacob Oluwole: You be boss, you be boss, you be boss, you be boss, you be boss, you be boss, you be boss.

[00:58:50] Adeleke Tolulope: But anything, but relating some kind, OKOK, but relating some kind, I'm gonna say music. What have we accomplished so far?

[00:58:52] Abiodun Adekanmi: What you doing? Which is?

[00:58:56] Jacob Oluwole: Big. Okay, couple. Hey, request a demo, schedule a demo. It's there something that we need to open on vacuum. There's login as everything, but schedule a demo.

[00:59:06] Abiodun Adekanmi: Mm. Mm.

[00:59:18] Jacob Oluwole: This thing, we have to do something like this. I have to do something like this. Question, Jeremy.

[00:59:19] Abiodun Adekanmi: What's up?

[00:59:24] Jacob Oluwole: So, when I say this, big call, we give a sentency, I think so. Thanks, Yancey. Wasted them. That's to begin. I want one percent. Mm. Yeah. E?

[00:59:52] Abiodun Adekanmi: Mhm. K. OK, thanks. Yes. Oh, oh, oh.

[01:00:40] Jacob Oluwole: Kim.

[01:00:41] Abiodun Adekanmi: Business.

[01:00:42] Jacob Oluwole: No.

[01:00:43] Abiodun Adekanmi: In. Yeah. Mm. You. Mhm. Can you?

[01:00:55] Jacob Oluwole: All right, so I'm like, but I want to close this chapter.

[01:01:02] Abiodun Adekanmi: I do, I do. I think in the company.

[01:01:07] Jacob Oluwole: Huh?

[01:01:08] Abiodun Adekanmi: Abiodun. How do you do Company?

[01:01:11] Jacob Oluwole: Make you much, you make, make, make.

[01:01:15] Abiodun Adekanmi: Hello, Jeremy.

[01:01:23] Jacob Oluwole: And this work is fully in. And then we talk about running. I'm going away by two weeks. I.

[01:01:45] Abiodun Adekanmi: When I made the issue, we saw Zamora to... Jacob. Hello?

[01:02:01] Jacob Oluwole: Hello.

[01:02:04] Abiodun Adekanmi: Yeah, so, yeah, that was.

[01:02:05] Jacob Oluwole: And we can go.

[01:02:08] Abiodun Adekanmi: Then I call, sorry.

[01:02:09] Jacob Oluwole: Mm.

[01:02:18] Abiodun Adekanmi: Hello!

[01:02:23] Jacob Oluwole: Linda, I know I talk, not talking about me, not talking about.

[01:02:23] Abiodun Adekanmi: Ohh. So, who break me, Diego?

[01:02:37] Jacob Oluwole: You.

[01:02:37] Abiodun Adekanmi: Oh.

[01:02:41] Jacob Oluwole: Which one? His name is Juan again. T.

[01:03:12] Abiodun Adekanmi: Okay.

[01:03:22] Jacob Oluwole: It's not really.

[01:03:29] Abiodun Adekanmi: No. Yeah. I can say, vast, I do pics on my end, thanks to you.

[01:03:45] Jacob Oluwole: So, minute. I don't think for me, I do my answer is bad yet too safe.

[01:03:48] Abiodun Adekanmi: For the trillion. I'm saying let me not be GPT from my end.

[01:03:54] Jacob Oluwole: It, it. Six. Later on. The.

[01:04:05] Abiodun Adekanmi: I think I also query GPT on my end. Because I have trained it about Moil, so... Mm.

[01:04:29] Jacob Oluwole: Lindy, Lindy.

[01:04:35] Abiodun Adekanmi: I got my next. The Screaming. Yeah, what do you want? Hey, Cortana. Well, what's wrong? I was saying I should also query the picture on my head. So that maybe you can find me like this.

[01:04:57] Jacob Oluwole: Okay, okay, okay. OK. YouTube on LinkedIn. So, I want to buy one, yeah, yeah, I need to enterprise, so also we not as much on LinkedIn outreach here. I want you to, because I have my fee business account to my sheet.

[01:05:31] Abiodun Adekanmi: Hairballs.

[01:05:34] Jacob Oluwole: I feel like it's someone working in the company, like...

[01:05:34] Abiodun Adekanmi: Yeah. Yes.

[01:05:40] Jacob Oluwole: So, when you pay, OK, we should have like this person's company, just... I have to ask customize my renegotiating part to Nigeria and then to my receiver, the whole thing takes us and you receive it again. And I want you can get when I do location of Company to each gentleman on my office.

[01:05:58] Abiodun Adekanmi: UPN. Mm.

[01:06:08] Jacob Oluwole: So... Right, not moving here. I will see what I can do on that, and...

[01:06:23] Abiodun Adekanmi: Okay. I've been checked by different.

[01:06:30] Jacob Oluwole: That.

[01:06:32] Abiodun Adekanmi: When do you have the address by the phone?

[01:06:36] Jacob Oluwole: Access a big.

[01:06:39] Abiodun Adekanmi: She profile it. No.

[01:06:42] Jacob Oluwole: No, I, I see you, but it makes sense when I see you, we shout, we shout.

[01:06:47] Abiodun Adekanmi: Mm. Sure.

[01:06:52] Jacob Oluwole: I fly up with B.

[01:06:53] Abiodun Adekanmi: Oh.

[01:06:54] Jacob Oluwole: Our top official, like the director of EDC.

[01:06:56] Abiodun Adekanmi: I. Yeah. Sure.

[01:07:01] Jacob Oluwole: She gets the idea of EDC. But it makes sense.

[01:07:06] Abiodun Adekanmi: I. In.

[01:07:15] Jacob Oluwole: No, I actually like it. Mm. I would have been best fish.

[01:07:28] Abiodun Adekanmi: It's not.

[01:07:28] Jacob Oluwole: Chair closer. So, machine, you still have anything?

[01:07:31] Abiodun Adekanmi: Okay. No, you do. I go down.

[01:07:38] Jacob Oluwole: Yeah?

[01:07:39] Abiodun Adekanmi: I go wrong.

[01:07:41] Jacob Oluwole: Abiodun.

[01:07:43] Abiodun Adekanmi: This is the one. So, that to me, I know that.

[01:07:47] Jacob Oluwole: Kim.

[01:07:48] Abiodun Adekanmi: Business. I love you.

[01:07:52] Jacob Oluwole: Okay, see, and POV, not a business coach, yeah.

[01:07:56] Abiodun Adekanmi: Mm.

[01:07:58] Jacob Oluwole: I have money.

[01:08:04] Abiodun Adekanmi: I want to know those ones, like, like, for some. I got gone for one second.

[01:08:08] Jacob Oluwole: And. Get to us, I'll stay to bye every morning.

[01:08:15] Abiodun Adekanmi: I have to go first.

[01:08:16] Adeleke Tolulope: I beg, I need access to...

[01:08:19] Abiodun Adekanmi: No.

[01:08:20] Adeleke Tolulope: Outlook or Outlook.cs@lab.com Outlook. I reply the email.

[01:08:26] Jacob Oluwole: We have like new, but not necessary. I'll do.

[01:08:31] Abiodun Adekanmi: Yes, in Nigeria.

[01:08:34] Jacob Oluwole: Gmail Neil. You know, Andres.

[01:08:39] Adeleke Tolulope: Gmail, say Gmail. I think you have a message to to force me.

[01:08:43] Jacob Oluwole: All I send you, OK, give me.

[01:08:46] Adeleke Tolulope: Pereff. What are you sending?

[01:08:51] Jacob Oluwole: I said, good luck to you.

[01:08:52] Adeleke Tolulope: See that one of those.

[01:08:54] Jacob Oluwole: I send you a quick Latin website to send you.

[01:09:00] Adeleke Tolulope: Oh.

[01:09:02] Jacob Oluwole: So, that's it.

[01:09:02] Adeleke Tolulope: Okay, Daniel, bye, man. Yeah, I will play the artist from Andres.

[01:09:13] Jacob Oluwole: But, like, do you like? Alright, we can go band for band, man. We can go.

[01:09:26] Adeleke Tolulope: Hey, what's login number about? For Anita, can you send me something? Jay, bye.

[01:09:35] Jacob Oluwole: Go **** my man.

[01:09:37] Adeleke Tolulope: It's.

[01:09:38] Abiodun Adekanmi: Yeah.

[01:09:40] Jacob Oluwole: Hey, thank you. Can you see me? Okay, okay, okay, yeah, we can let's see.

[01:09:50] Adeleke Tolulope: My name opens. It's ******* me up, man.

[01:09:55] Jacob Oluwole: Yeah.

[01:09:57] Adeleke Tolulope: Reply. Okay, it's very plain.

[01:10:07] Jacob Oluwole: If I send, send this group, no, send this Andres.

[01:10:08] Adeleke Tolulope: Yard. Yeah.

[01:10:14] Jacob Oluwole: Sandy. Thank you, kidney.

[01:10:17] Adeleke Tolulope: It done.

[01:10:19] Jacob Oluwole: Tennessee group to send you, they can get you.

[01:10:20] Adeleke Tolulope: I love you.

[01:10:29] Jacob Oluwole: I thought people saw something else. If he can't get out for that, then he can't get out for any game of the game. Pap Guardiola, some mentality, and now, years later, Arsenal are seeing the full picture. Because Declan Rice didn't just improve Arsenal, he changed the entire mentality of the team. And they played against the team for forty-five minutes. Absolutely to score a goal they didn't give a chance away. I believe it shows how strong Arsene is defensively and disciplined. From controlling midfield battles to Karin Arsenal through huge Champions League nights, to becoming the emotional heartbeat of Michael Martinez project, Rice slowly became the player everyone had rested in.

[01:11:06] Adeleke Tolulope: Ohh. Yeah.

[01:11:11] Abiodun Adekanmi: Is.

[01:11:11] Adeleke Tolulope: Mhm.

[01:11:12] Jacob Oluwole: And honestly.

[01:11:13] Adeleke Tolulope: Need to stop this now.

[01:11:15] Jacob Oluwole: Says the story of how Declan Rice became one of the most important players in world football. When personal announced the signing of Declan Rice with West Ham United in 2023, the reaction was mixed. Some fans loved it immediately, others looked at the price tag and panned. Here comes the money! Here comes the money! More than 100 million pounds for a defensive bib beater? The expectations instantly became ridiculous. And because Rice was in the flashy dive, many people struggled to understand what Arsenal were actually on. He wasn't a player doing rainbow flicks every 5 minutes. He wasn't a pair attacking the fielder putting up insane numbers every week. But Arsenal bought with something much harder to notice instant. Control. That became obvious during his early performances against Manchester United. Arsenal looked combo with him on the pitch, transitions felt safer, midfield battles became more physical, and late in the match, Rice scored a massive winning goal that completely exploded the Emerex Stadium.

[01:11:54] Abiodun Adekanmi: Yeah. This all the way to do the play, it is scared going.

[01:11:58] Jacob Oluwole: But in fact, only definitely explains him. He's deck of rice effects games in quite a race too. He covers huge spaces defensively, he does defenders constantly, wins second balls, carries possession and pressure, and most importantly, he changes the emotional level of the team. That's what made midfielders too. They make everyone else feel the same. Slowly, Arsenal started realizing they didn't just buy a midfielder. They bought the foundation of the team.

[01:12:01] Abiodun Adekanmi: And. We. It is him, I will. But that's not it. Alright.

[01:12:17] Jacob Oluwole: And that Guardiola wasn't the only football line to recognize something special about Rice mentality, long before Rice being National's midfield leader, that Guardiola kept praising in public. And that matters because Guardiola rarely compliments opposition to the builders casual. When I saw yesterday, and just as the defendant and making it all, that means what is like a Rice, but I think Arsenal mentality independently decisions or decisions and how competitive and what you can do the season they have done, all the season they have done so far.

[01:12:20] Abiodun Adekanmi: Ohh. You. Mama. Play me.

[01:12:28] Adeleke Tolulope: Yeah.

[01:12:40] Abiodun Adekanmi: No.

[01:12:41] Jacob Oluwole: Over the last few years, Pep repeatedly spoke about Rice's mentality, leadership, competitiveness, and influence of big matches. Even recently, Gardella praised Rice's mentality and called him symbolic of Arsenal's competitiveness and belief. Thanks so good to play for football players, just so pure. He loved everything. Well, the interesting part is this. Pep didn't praise Rice because of statistics. He praised him because of intelligence. Rice understands the space extremely well.

[01:12:42] Abiodun Adekanmi: Just. Understand.

[01:13:01] Jacob Oluwole: He knows when to slow attacks down, when to press aggressively, and when to carry the ball forward under pressure. That's why Guardiola respected him early, because league managers know his details, regular fans often miss. Against Manchester City, you can see exactly why Pet admire him. Rice covered enormous defensive spaces while still helping Arsenal progress the ball calmly under pressure. Very few midfielders can do both systems. And overtime, Guardiola's comments started looking more accurate every season. Because Rice wasn't just becoming a top midfielder, he was becoming the title player, title winning teams are built around. But understanding Rice's mentality only tells part of the story because leaving West Ham completely changed the level of his career. Before Arsenal, Rice already looked special at West Ham, but leaving changed the ceiling complete. At West Ham, he carried responsibility for real. He captained the club, won the Robo Conference League, and became one of the Premier League's best midfielders. But Arsenal gave him something different. Elite expectations every single week. That changes players. At West Ham, great performances felt impressive. At Arsenal, they became necessary. And Rice adapted surprisingly quick. That transition isn't easy either. Some players struggled massively when moving from strong clubs to elite clubs because the pressure becomes completely different. Every touch gets analyzed, every mistake becomes headlines. Rice handled it naturally. That's one reason Arsenal trusted them so heavily. They didn't just believe in the football ability, they believed in the person. And now looking back, the move feels less like a transfer and more like the moment Rice fully became world class. And once Rice arrived at Arsenal, the biggest impact wasn't just emotional, it completely changed how the team defended. One underrated thing about Declan Rice is how much he changes defensive stability without defenders even noticing it. That's the lead midfield play. Against Liverpool, you can constantly see Rice. You, me again.

[01:14:54] Abiodun Adekanmi: Yeah.

[01:15:16] Jacob Oluwole: Hmm. Will you keep in? First, I need to. John Gibson.

[01:15:27] Adeleke Tolulope: I don't want to spend the whole day in on George Street. Okay. Was with last month. Man.

[01:16:04] Jacob Oluwole: Yeah.

[01:16:26] Adeleke Tolulope: Ohh, Zapata! Ahh, sorry. Yeah. Yeah.

[01:16:37] Jacob Oluwole: Much to put with a bit.

[01:16:40] Adeleke Tolulope: Pereff.

[01:16:42] Jacob Oluwole: She managed to play.

[01:16:47] Adeleke Tolulope: Ohh. Okay. You guys used to worry about me being the... The one with AI is love.

[01:17:14] Jacob Oluwole: I don't so down by 7.

[01:17:18] Adeleke Tolulope: And this is me.

[01:17:25] Jacob Oluwole: Leave away, please say. So, no events, events, events. Play back, Casey.

[01:17:53] Adeleke Tolulope: Mm. Yeah. And this is a. Babe, good.

[01:18:06] Jacob Oluwole: Yeah. Tony Benyukhis.

[01:18:09] Adeleke Tolulope: Yeah. Ohh my goodness, I'm very pleased about that. Good. That is funny. Yeah. My starting days work like that.

[01:18:37] Jacob Oluwole: Kate.

[01:18:37] Adeleke Tolulope: Voice. Is this a class?

[01:18:41] Jacob Oluwole: Thank you.

[01:18:49] Adeleke Tolulope: That can be.

[01:18:50] Jacob Oluwole: Yeah, give away money.

[01:19:01] Adeleke Tolulope: You too.

[01:19:10] Jacob Oluwole: B.

[01:19:10] Adeleke Tolulope: I mean, you can.

[01:19:12] Jacob Oluwole: Like, menu down guys in me.

[01:19:16] Adeleke Tolulope: I mean, AB icon.

[01:19:17] Jacob Oluwole: You don't get no. Not iPhone.

[01:19:20] Adeleke Tolulope: They are gonna be.

[01:19:21] Jacob Oluwole: Question, like, if there's many, like, be a banded young, yeah, only if you picture of banded young, I take my wife ties in me.

[01:19:32] Abiodun Adekanmi: I told you.

[01:19:33] Adeleke Tolulope: Yeah, I'm done, I'm done.

[01:19:35] Jacob Oluwole: Instead of all these ones, I told him. It's not nice.

[01:19:41] Adeleke Tolulope: Let it designer talk, give me, I'm glad you feel it.

[01:19:44] Jacob Oluwole: Ohh, sorry, I got that, sorry.

[01:19:47] Abiodun Adekanmi: Karin.

[01:19:50] Jacob Oluwole: I'm talking from the user experience side as a client who is willing to partner with Meridian. OK, I'm glad I designer.

[01:19:51] Abiodun Adekanmi: Okay.

[01:20:05] Adeleke Tolulope: The. I'm good.

[01:20:08] Jacob Oluwole: And I love to see you calling.

[01:20:10] Abiodun Adekanmi: I'm on your call, but I can't hear you. I just came back now.

[01:20:13] Jacob Oluwole: Oh.

[01:20:13] Adeleke Tolulope: Yeah.

[01:20:14] Jacob Oluwole: Okay, I said, I thought I would do something. Now on this, on this, on this meridian section, menu section, you should, each of these menus should have images.

[01:20:15] Adeleke Tolulope: You guys.

[01:20:25] Abiodun Adekanmi: Mm. Lebanon restaurants.

[01:20:44] Jacob Oluwole: No, no, because I like, but I have been something like that, but it's a little out, like a club-like setting on my stage. Maybe you can come there and queue, you can use it for birthday. When you have Instagram, so like with Meridian.

[01:20:44] Abiodun Adekanmi: I. Yes. Mm. Mm.

[01:21:04] Jacob Oluwole: Any start now, make a feeling.

[01:21:06] Abiodun Adekanmi: Play Adekanmi.

[01:21:06] Adeleke Tolulope: I go, don't do that.

[01:21:06] Jacob Oluwole: So, so one way on their menu store, on their menu store, we are calling.

[01:21:08] Adeleke Tolulope: Inna.

[01:21:09] Abiodun Adekanmi: Will do.

[01:21:14] Jacob Oluwole: We have only on your menu store, we have only you just have Nieman and Kenny.

[01:21:21] Abiodun Adekanmi: Yeah. Mm. Your funny image, something I want to put in the stomach, something I want to eat, or to see it.

[01:21:33] Jacob Oluwole: Yeah. And no.

[01:21:36] Adeleke Tolulope: Bill. Eh?

[01:21:38] Jacob Oluwole: I have it out of 1000.

[01:21:39] Adeleke Tolulope: And...

[01:21:47] Jacob Oluwole: You see, yeah. Is that stuff? My own is teach. I was, I will tell him again. Give me one, give me one. Do you have anything good? I saw, yeah, I still don't think she lives life constant in some constant environment. Good evening.

[01:23:02] Abiodun Adekanmi: Mucha, mucha video, which are the same.

[01:23:08] Jacob Oluwole: There are more share on the screen.

[01:23:12] Abiodun Adekanmi: Hmm, yes, I request creamer sensor.

[01:23:18] Jacob Oluwole: Mm. Just great music behind it. I think this is the movie. So, that is, give me a second. I was on page, you know that we screen recorded this video. Yeah, really? We something you never like we are sports. It was no test, no, nothing, nothing. Where is you? Where is he? But you never like come one. You have a blank sound for me. The name of Wiki in Nasha. Yeah, when I feel all guys in it. So, image must be dead. Something that will be low, and yeah, pretty alpha.

[01:25:23] Adeleke Tolulope: Thank you, Madam.

[01:25:27] Jacob Oluwole: If you see, if you see them watch it for me, trash, you can see that.

[01:25:36] Adeleke Tolulope: And you see, and you can load Tim team, WhatsApp alone, look seems did for you now to talk, now go to use WhatsApp.

[01:25:45] Abiodun Adekanmi: Okay.

[01:25:45] Jacob Oluwole: Hey, but what, because what is the past? We have to do a message with the acknowledge.

[01:25:58] Adeleke Tolulope: Return the user branded from an extraction that's most necessary.

[01:26:03] Jacob Oluwole: My big team, team, team. You can book one on one is at the active are frustrated. Just messaging.

[01:26:19] Abiodun Adekanmi: Yeah.

[01:26:20] Adeleke Tolulope: Yeah.

[01:26:20] Jacob Oluwole: I think, I think, I think. They would ask my lord.

[01:26:25] Adeleke Tolulope: But then, no, she, she, but, but then, she registered work hours.

[01:26:33] Jacob Oluwole: Yeah, you start.

[01:26:33] Adeleke Tolulope: Did I put your day, put your day, put your day, put your knee, put your knee, one rule. I, but I said, twenty-four, twenty-four year, and it's happening.

[01:26:36] Jacob Oluwole: I told you, I don't unofficial.

[01:26:52] Adeleke Tolulope: I want to sleep again to day break. I want to sleep again to day break. I want to make you do many time. I want to sleep to day break. Mama, you Carlin.

[01:26:52] Abiodun Adekanmi: Mhm.

[01:26:53] Jacob Oluwole: Hey. Mhm.

[01:27:07] Adeleke Tolulope: Is Zane. Anything, anything, level, level. Think. Then, I drink engine.

[01:27:19] Abiodun Adekanmi: See you, bye. I got the new transcript code.

[01:27:22] Adeleke Tolulope: This. That.

[01:27:26] Jacob Oluwole: My PM.

[01:27:28] Adeleke Tolulope: What is in there?

[01:27:29] Jacob Oluwole: No, we will.

[01:27:32] Adeleke Tolulope: But, in there, when it says it, too bad, she done it with my friends that.

[01:27:38] Jacob Oluwole: I think they see last time. I'm just saying there's a last time, yeah, two cents. Equity, last is the cortana on the PDF.

[01:27:41] Adeleke Tolulope: Yeah, nice.

[01:27:49] Jacob Oluwole: Yeah, you do. Yeah.

[01:28:15] Adeleke Tolulope: OK, the brown wire.

[01:28:16] Jacob Oluwole: Yeah. Ohh, you do it, didn't you? Yeah, you get the only online with you. We do it out.

[01:28:19] Adeleke Tolulope: Those. Yeah, yeah, I big low one, low one. I am good with this.

[01:28:50] Abiodun Adekanmi: Social Metrics Pro, your new analytics staff board. Track 10 plus metrics in real time. Get custom insights tailored to your brand. Benchmark performance against competitors instantly. Marketers using Social Metrics Pro boosted engagement by 30% in just weeks. Ready to turn data into growth? Try Social Metrics Pro free for 14 days. Struggling to measure your social media ROI? Social Metrics Pro. Growth.

[01:29:17] Jacob Oluwole: Yeah, I'm pressing the.

[01:29:19] Abiodun Adekanmi: Or feel your posts vanish without a trace? Use these five best practices. First, know your audience and speak their language. Next, tell authentic stories that spark a motion. Then use bold visuals to grab attention. Also, invite genuine conversation with open questions. Finally, stay consistent and adapt based on real feedback. Apply these every day and watch your engagement skyrocket.

[01:29:27] Jacob Oluwole: Yeah.

[01:29:33] Adeleke Tolulope: Mhm.

[01:29:39] Abiodun Adekanmi: Ever feel your posts vanish without a trace? Use these five best practices. First, know your audience and speak their language. Next, tell authentic stories that spark emotion. Then use bold visuals to grab attention. Also, invite genuine conversation with open questions.

[01:29:52] Jacob Oluwole: You can bring Xbox to you. Tolulope.

[01:29:58] Adeleke Tolulope: Mhm.

[01:29:58] Jacob Oluwole: When did she invites you to your wedding?

[01:29:58] Abiodun Adekanmi: Your brand is like nothing. When your visuals and messaging shift from Instagram, customers lose trust. That's why consistent branding.

[01:30:01] Adeleke Tolulope: Huh?

[01:30:02] Jacob Oluwole: OK, thank you.

[01:30:05] Adeleke Tolulope: Where do you need?

[01:30:09] Abiodun Adekanmi: We nail your logo placement, color, and voice to align across every channel. The result? 60% higher brand recall and more loyal followers. Ready to unify your presence and stand out? Let's build your consistent brand today. Your brand is everywhere but feels like nothing. When your visuals, tone, and messaging shift from Instagram to LinkedIn,

[01:30:09] Jacob Oluwole: You think, thanks if you walk away again?

[01:30:29] Abiodun Adekanmi: Customer lose trust.

[01:30:31] Jacob Oluwole: T. To what?

[01:30:36] Adeleke Tolulope: Mhm. No, no. And.

[01:30:57] Abiodun Adekanmi: every day conversations, sparking genuine interest. You see increased reach, deeper connections, and real-time feedback. Ultimately, it's not just about impressions, it's about building trust and driving loyal customers. Influencer campaigns turn passive audiences into active advocates, fueling growth.

[01:30:59] Adeleke Tolulope: The.

[01:31:15] Abiodun Adekanmi: Struggling to grab attention on social media? Follow these stupid best practices. Focus on a clear, catchy headline. Use high quality visuals that tell a story. Add interactive elements like polls and questions. Consistency matters, post at peak times, and stick to your brand voice. Brands applying these tips see up to 60% more engagement.

[01:31:17] Jacob Oluwole: Definitely.

[01:31:25] Adeleke Tolulope: Yeah.

[01:31:34] Abiodun Adekanmi: Ready to level up your content? Start using these strategies today and watch your engagement soar. Struggling to grab attention on social media? Follow these proven best practices. Focus on a clear, catchy headline. Use high quality visuals that tell a story. Add interactive elements like polls and questions. Consistency matters posted.

[01:32:04] Jacob Oluwole: So, go, go.

[01:32:11] Adeleke Tolulope: Cheeky.

[01:32:14] Abiodun Adekanmi: Yeah, well, yeah, well.

[01:32:14] Adeleke Tolulope: The.

[01:32:17] Jacob Oluwole: Yeah.

[01:32:19] Abiodun Adekanmi: Yeah, we are down here.

[01:32:19] Adeleke Tolulope: Why about me? Why about me?

[01:32:23] Jacob Oluwole: Like, oh, you work on it when you want to point or 2.1 to now.

[01:32:23] Abiodun Adekanmi: Go on, go on.

[01:32:30] Jacob Oluwole: Ohh, we no, I like it.

[01:32:32] Adeleke Tolulope: Excuse me?

[01:32:35] Jacob Oluwole: Yeah, I didn't like it, man. He invited one.

[01:32:46] Adeleke Tolulope: We invited, what am I invited?

[01:32:47] Jacob Oluwole: Ohh, as well, hold on, hold on, I think, like, 17 million naira when I feel invited.

[01:32:51] Adeleke Tolulope: Yeah.

[01:32:59] Jacob Oluwole: Fifty to 70 million. Welcome.

[01:33:25] Abiodun Adekanmi: Mm.

[01:33:29] Jacob Oluwole: No. We just need last week. Need this down, need this down. So, he's been ****. Can you see the social sites? Went to a land. What event do we have? What event do we have? We have Zoe's birthday coming up. This bed is coming up.

[01:34:22] Abiodun Adekanmi: Good.

[01:34:23] Jacob Oluwole: Balogun.

[01:34:23] Abiodun Adekanmi: Who's better?

[01:34:26] Jacob Oluwole: Zane, I should bet you.

[01:34:31] Abiodun Adekanmi: Zane, now is the.

[01:34:32] Jacob Oluwole: And.

[01:34:35] Abiodun Adekanmi: Today is Adekanmi.

[01:34:36] Jacob Oluwole: Allah. Tomorrow is a bad day.

[01:34:41] Abiodun Adekanmi: So, as one on the 18th, yes?

[01:34:45] Jacob Oluwole: Today is a meeting.

[01:34:47] Abiodun Adekanmi: She's 3 months today.

[01:34:48] Adeleke Tolulope: February 18th.

[01:34:50] Jacob Oluwole: Yeah.

[01:34:51] Adeleke Tolulope: No, I did 19.

[01:34:51] Jacob Oluwole: In fact, use. Where it goes, after party do that things as Lando.

[01:35:06] Abiodun Adekanmi: Play the book.

[01:35:08] Jacob Oluwole: That lays us down low.

[01:35:11] Abiodun Adekanmi: But yeah.

[01:35:14] Jacob Oluwole: That's what she wedding.

[01:35:20] Adeleke Tolulope: Where do you go?

[01:35:23] Jacob Oluwole: ****.

[01:35:24] Abiodun Adekanmi: Cortana, get friends.

[01:35:26] Adeleke Tolulope: You.

[01:35:29] Jacob Oluwole: And.

[01:35:32] Adeleke Tolulope: The.

[01:35:34] Jacob Oluwole: And.

[01:35:34] Abiodun Adekanmi: And your Max.

[01:35:36] Jacob Oluwole: I love you.

[01:35:38] Adeleke Tolulope: You.

[01:35:39] Jacob Oluwole: Yeah, no.

[01:35:41] Abiodun Adekanmi: I believe in.

[01:35:41] Jacob Oluwole: The value of will be 1.5K and be even 1K and 800. Dial it to 15. And?

[01:36:01] Abiodun Adekanmi: Why is that be Monica? He does that.

[01:36:04] Jacob Oluwole: And. Actually.

[01:36:14] Abiodun Adekanmi: Better convenience.

[01:36:19] Jacob Oluwole: Five.

[01:36:19] Abiodun Adekanmi: It.

[01:36:23] Jacob Oluwole: Yeah, I will not initiate it. We have 400, at least that 400, but then you want to.

[01:36:30] Abiodun Adekanmi: Well, thank you, well, thank you, family, 300.

[01:36:37] Jacob Oluwole: I.

[01:36:37] Abiodun Adekanmi: I want to put a message in my name, but I drop a masala.

[01:36:42] Jacob Oluwole: Yeah. And. No, you got to.

[01:36:48] Abiodun Adekanmi: Let go on, let go on and forward, and we we do about Balogun.

[01:36:55] Jacob Oluwole: Why give me a?

[01:36:56] Adeleke Tolulope: This.

[01:37:15] Abiodun Adekanmi: Very much.

[01:37:16] Jacob Oluwole: She she she she she me bye.

[01:37:22] Abiodun Adekanmi: What? Where, yeah?

[01:37:30] Jacob Oluwole: Balogun, home boy, home cook, home cook, no one.

[01:37:31] Abiodun Adekanmi: Hello. Thank you.

[01:37:35] Jacob Oluwole: There you go.

[01:37:38] Abiodun Adekanmi: Uncle Camille.

[01:37:39] Jacob Oluwole: Mhm. I understand, I understand where it's coming from.

[01:37:47] Abiodun Adekanmi: Do you see? 15 hours. So. It's a time. It's a.

[01:38:04] Jacob Oluwole: And he had.

[01:38:07] Abiodun Adekanmi: What about your time in the time of call? Why am I measurable? What about your time as a place?

[01:38:07] Jacob Oluwole: No. Yeah, I know. Most of the last time, was often last time, baby. Last time, yeah. Yeah, on guys, yeah, time will ship. I will work. I'm working working. I'm not.

[01:38:25] Abiodun Adekanmi: Temple.

[01:38:29] Jacob Oluwole: You. Now for my move, Kaki, recipe by, and the more you are active, but they are not leaving any place, only Lord Chat GPT. On the new page, you got to match it for you for 8 hours near, and the end of the month on my Balogun game.

[01:38:47] Abiodun Adekanmi: We.

[01:38:56] Jacob Oluwole: I mean, I mean, we only advise to this one to finish this project, finish everyone in fixed. If you don't finish it before the end of the month, we will think by like any. I want to be better out. I want to be only one design squares which website to me no good website.

[01:39:30] Abiodun Adekanmi: Yeah, we sweater.

[01:39:30] Jacob Oluwole: I have no old life for two months. Two months, nearly. How about I am changing body when they play on five hours, five days, four days on the party?

[01:39:41] Adeleke Tolulope: Donna.

[01:39:41] Abiodun Adekanmi: Mmh.

[01:39:43] Adeleke Tolulope: So, so. You know what, you know, you know what, Jacob, over here, you know what, over here, over here, if you check those big tech companies, right, for two weeks projects.

[01:39:47] Jacob Oluwole: Hey, bro, there's anything, I mean, there's anything more. Yeah.

[01:39:57] Abiodun Adekanmi: Mm.

[01:40:01] Adeleke Tolulope: Tell me a month, and what is somewhere, like, like, there was this guy to to resell, I want in Silicon Valley, and they are paying in those per month, right?

[01:40:04] Jacob Oluwole: I love you. No. I just want.

[01:40:17] Adeleke Tolulope: Go on board there for three months, without anything doing, which are my big aspect of busy here, as I understand the code structure, everything, as I can coding, as I can study everything, anything for three months, and they pay the three months, doing three months, Ola, HI, I don't want to be project manager. I don't have any time. I need two, two, two, when we have project for you, we'll give it to you, but I don't have any projects, one for me, form of conduct to design, form of conduct to design, one for one good month, 30 days, 30 days, but they must be around 99 when there's somewhere like easy life. Is it like, well, you know, you can't do that in a startup, say you get most startups, they want people, hardworking people, stuff like that. But we Nigerians, we tend to put in much effort, right? We're told by Ring of Ben now, compared to Nigerian level. Ring of Ben, what have we done?

[01:41:11] Jacob Oluwole: Ohh.

[01:41:13] Abiodun Adekanmi: Yeah.

[01:41:15] Adeleke Tolulope: Form ecology, but over there, they are like aiming towards perfection. That one month, if I go to any issue, but yeah, and color, but see, but see different in the convert, no, see you get the give you that time to deliver the very best you can deliver.

[01:41:27] Jacob Oluwole: The.

[01:41:35] Adeleke Tolulope: But yeah, we speed up, speed up, speed up, speed up, speed up. Most startups, we speed up, speed up, speed up, speed up, speed up, but they say they're putting too much a test.

[01:41:41] Jacob Oluwole: What? Okay, so we'll get here on Fortune 500. Yeah, only on Fortune 500, but because see the way the the tweets work.

[01:41:59] Adeleke Tolulope: Mm.

[01:42:01] Jacob Oluwole: Because if you know, if you not do very well.

[01:42:01] Adeleke Tolulope: Mhm. Getting back.

[01:42:05] Jacob Oluwole: She don't do very well, ohh, so I guys, I guys find a weak.

[01:42:09] Adeleke Tolulope: Yeah, yeah, I know.

[01:42:13] Jacob Oluwole: Certainly. My sister, Mitch, and Monica.

[01:42:25] Adeleke Tolulope: All right. Oh.

[01:42:40] Abiodun Adekanmi: It is.

[01:42:41] Jacob Oluwole: We want with that.

[01:42:44] Abiodun Adekanmi: Yes.

[01:42:45] Jacob Oluwole: I would like to go all the kids. That's more quality, not more quality, BPPPP.

[01:43:00] Abiodun Adekanmi: No, but I really.

[01:43:03] Jacob Oluwole: OK, OK, my side. I said clock out. clock out 5 hours. It's fine now. We have only 10 hours, then what you basing going for, but one bleed out. I should actually 10 hours then more time limits. You know, I shouldn't 10 hours. I'll be okay. He must say, while in checking me goes a routine for minutes, one more condition in a way, and check me and take screenshots for 8 hours, 6 hours, they go team. Ten hours on, on, on. I think.

[01:43:52] Abiodun Adekanmi: Yeah. Is that a good?

[01:44:00] Jacob Oluwole: Ola.

[01:44:03] Abiodun Adekanmi: There were some agreements.

[01:44:12] Jacob Oluwole: What if I didn't know? What do I didn't know? I saw...

[01:44:14] Abiodun Adekanmi: And. But I think that chocolate review would say that. So, is loop-sided? I mean, loop-sided?

[01:44:28] Jacob Oluwole: Among. Mommy, my email. My should be. Yeah, you understand, Karin. Mm. Yeah, I just don't talk about that.

[01:45:06] Abiodun Adekanmi: Oh, farewell.

[01:45:09] Jacob Oluwole: Where we need here, big for the energy.

[01:45:11] Abiodun Adekanmi: I'm on, I'm on one page now. Simplified HQ Instagram. We will post one little new likes to two more. There is so far its likes.

[01:45:24] Jacob Oluwole: Simplify SQ.

[01:45:24] Abiodun Adekanmi: And... And... HQ. And they have 11.8 K. followers.

[01:45:34] Jacob Oluwole: Okay.

[01:45:35] Abiodun Adekanmi: And all their posts is carousel image, but we cannot see now our videos carousels still image carousels.

[01:45:42] Jacob Oluwole: Chase download.

[01:45:45] Abiodun Adekanmi: My group says that AI marketing suites Google design, write, edit, publish content. You spy.

[01:45:53] Jacob Oluwole: When I contact the long quits, when I need to use.

[01:45:58] Abiodun Adekanmi: No, no, this one. Yes, that's the I have seen. All right, 13301000111000.

[01:45:59] Jacob Oluwole: It's nice. Edmond.

[01:46:16] Abiodun Adekanmi: Zero, one. 0000001 and they claim that it is used by. Eleven million plus creators and teams.

[01:46:32] Jacob Oluwole: Done, you love me, you.

[01:46:36] Abiodun Adekanmi: Yeah. Are they are they aggregate the the pages you must send our link.

[01:46:42] Jacob Oluwole: Yeah. Steve, just off me to get anything.

[01:46:50] Abiodun Adekanmi: Welcome.

[01:46:53] Adeleke Tolulope: Inna.

[01:46:54] Jacob Oluwole: I just need to like it, then the...

[01:46:55] Adeleke Tolulope: Hello!

[01:46:57] Jacob Oluwole: Who told me to buy it any email?

[01:47:02] Adeleke Tolulope: Why?

[01:47:03] Jacob Oluwole: I was hoping to buy it and email you, what? Tell me when you get the email.

[01:47:07] Abiodun Adekanmi: Thank you.

[01:47:07] Adeleke Tolulope: Hey, why is the man so funny? Why is the man so funny? Why is the mouth so clean?

[01:47:14] Jacob Oluwole: But I give him a mobile, we do it, my changing maybe.

[01:47:14] Adeleke Tolulope: Rim. It's a bit, it's a bit money-made, right now is up when somebody can reason, but not not not saying it.

[01:47:22] Jacob Oluwole: My, my, my, my new TV. And why did you John do this number? Jacob. That will be on.

[01:47:33] Abiodun Adekanmi: I already.

[01:47:39] Jacob Oluwole: Yeah?

[01:47:42] Abiodun Adekanmi: Amber light.

[01:47:45] Jacob Oluwole: When you do.

[01:47:46] Abiodun Adekanmi: By me.

[01:47:50] Jacob Oluwole: I see.

[01:47:51] Abiodun Adekanmi: The rugby. Play Balogun.

[01:47:59] Jacob Oluwole: Yeah. Ohh, you like the Meridian websites, only like to space space, so if you are coming with an artist, I show artist.

[01:48:12] Abiodun Adekanmi: Yes.

[01:48:14] Adeleke Tolulope: Yeah.

[01:48:17] Abiodun Adekanmi: I just done by 17 million.

[01:48:21] Jacob Oluwole: Mm.

[01:48:24] Abiodun Adekanmi: You. I find a website that does like what we do.

[01:48:31] Jacob Oluwole: Exactly.

[01:48:33] Abiodun Adekanmi: I found one. The one with the one with the marketing part. Business planning here to test the reset your market, forecast your numbers and review your plan before anyone knows those. Solutions, create a plan for funding, test your business idea, build your business budget, create your pitch presentation, our team machine.

[01:48:58] Jacob Oluwole: I do.

[01:49:00] Abiodun Adekanmi: It.

[01:49:01] Jacob Oluwole: I wanna in business school, too.

[01:49:02] Abiodun Adekanmi: With you. Yeah.

[01:49:04] Jacob Oluwole: But every business, I want you a business coach.

[01:49:11] Abiodun Adekanmi: Yeah.

[01:49:12] Jacob Oluwole: Because business plan my quit me. Please OK give me again by only create a BPT. Download the PT. Yeah, go and show you business with the key BPT. Business plan.

[01:49:18] Abiodun Adekanmi: Mm.

[01:49:26] Jacob Oluwole: For Guinea. Download Business Plan, download PPT.

[01:49:33] Abiodun Adekanmi: Mm. Launch your startup, forecast cash flow, present your financials, consultants, and coaches, SBA partners, executive lender developers. Let us see their IG page. 2.5 for one.

[01:49:47] Jacob Oluwole: Send me new call. 2.5 million.

[01:49:50] Abiodun Adekanmi: Unto test. No, it's too much.

[01:49:58] Jacob Oluwole: Okay. You send me.

[01:50:00] Abiodun Adekanmi: Song.

[01:50:03] Jacob Oluwole: What did you?

[01:50:07] Abiodun Adekanmi: Doing with that.

[01:50:10] Jacob Oluwole: Honestly, I'm not getting the email for my for my email. I'm not getting email for my TPN too. I can only download it. I can't get. I'm not getting the email. There's the online.

[01:50:21] Adeleke Tolulope: Ohh, I know.

[01:50:22] Jacob Oluwole: No. I want you got to get to bed.

[01:50:24] Abiodun Adekanmi: How are you?

[01:50:28] Jacob Oluwole: I think.

[01:50:29] Abiodun Adekanmi: I see, I see. The more that they want, they are being.

[01:50:32] Jacob Oluwole: Hello. And that's in my.

[01:50:41] Abiodun Adekanmi: OK, not blind. I need, I need.

[01:50:44] Adeleke Tolulope: I do. What are you saying?

[01:50:47] Abiodun Adekanmi: Anita.

[01:50:50] Jacob Oluwole: No.

[01:50:57] Abiodun Adekanmi: I think we were actually. Yeah.

[01:51:00] Adeleke Tolulope: He made more, he said. I want to get it. I want to take a professional certificate. Now this is marrying me, you could not understand.

[01:51:12] Abiodun Adekanmi: Thank you. Market analysis, search 14 sources in real time, top performing business plans in 2025 and prioritize.

[01:51:14] Adeleke Tolulope: They won't happen. This is the foundation.

[01:51:22] Abiodun Adekanmi: Here, I'll summarize on 14, I mean. I hear there are some important limitations to acknowledge here. Limitations on a 40 page business plan in six seconds. It has one analysis and a mystery statement with the word synergy in it. That's kind of what I'm worried about. Oh, wait, I also found a YouTube video, a Reddit thread.

[01:51:29] Adeleke Tolulope: I do my Stephen.

[01:51:46] Abiodun Adekanmi: I like, and a recipe for banana bread. Do you want banana bread? Stay focused. I've already outlined 12 strategies, 11 of which are just the same strategy, reword it.

[01:51:58] Adeleke Tolulope: And let Jacob.

[01:51:59] Jacob Oluwole: And?

[01:51:59] Abiodun Adekanmi: I wanted to use.

[01:52:01] Adeleke Tolulope: She transmission.

[01:52:03] Abiodun Adekanmi: Thank you.

[01:52:03] Jacob Oluwole: And then.

[01:52:05] Abiodun Adekanmi: We should take a step back and consider.

[01:52:08] Adeleke Tolulope: I thought I would.

[01:52:10] Jacob Oluwole: Thank you.

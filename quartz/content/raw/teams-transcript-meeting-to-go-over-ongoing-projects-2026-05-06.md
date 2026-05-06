---
ingested: true
ingested_at: 2026-05-06
type: teams-transcript
---
# Teams Transcript — Meeting to go over ongoing projects (2026-05-06)

## Meta

- **Meeting subject:** Meeting to go over ongoing projects
- **Date:** 2026-05-06
- **Scheduled time:** 10:00–11:00 AM CT (15:00–16:00 UTC) — actually ran ~1h50m (transcript ended 12:31 PM CT / 17:31 UTC)
- **Organizer:** Taiwo Ola Balogun (Taiwo@moilapp.com)
- **Attendees:** Andres Urrego, Taiwo Ola Balogun
- **Source:** Microsoft Graph `/me/onlineMeetings/{id}/transcripts/{id}/content` (VTT)
- **Meeting ID:** `MSozZGY3YjE3Zi1lNWZjLTRiMjAtYWY5ZS1kNzgzYjE2MDg0ZmQqMCoq...thread.v2`

## Topics covered

This was a working session reviewing two active engineering deliverables:

1. **Siren Beauty website** — design feedback from the client (Faye, the Siren Beauty owner) on the latest staging push. The client said the site "doesn't reflect who she is" after a staging build with the wrong colors went live.
2. **Inna / Faye CRM + email campaign system** — end-to-end test of the lead pipeline, contact upload (5,000 contacts), email send, open/click tracking, and Resend domain verification.

## Key decisions

- **Stop making design changes to Siren Beauty until the client explicitly asks.** Realign with the brand the client has on her existing channels first; deliver only on requested changes from her video feedback.
- **Codex license deferred** — Andres wants to buy a Codex license once the current project gets paid; Taiwo's position is "Claude is enough for now, sir." No purchase yet.
- **For Megan's bot, use Gemini 2.0 with her voice baked in** — cheap (~$5/mo to her). Pattern: turn each small workflow into "its own little agent" by giving cheap models the files they need.
- **CMS / website builder is on the roadmap.** Andres' vision: "click here, create your website" → AI draft → optional CMS attach → optional CRM subscription. Treat the CRM subscription as the upsell alongside the lead generator.
- **Test mode toggle in Resend** is the pre-send safety. Megan Miller added as a test contact so Andres can demo the live send to her.

## Action items

### Taiwo
- [ ] Remove the word "science" everywhere on the Siren Beauty site (already mostly done — confirm complete pass)
- [ ] Remove the duplicate "Siren Beauty" logo from the top header (the hero image already is the logo)
- [ ] Make the header text bolder/thicker with a white shadow so it doesn't disappear over the hero image during scroll transition
- [ ] Make the Siren Beauty site mobile responsive — flagged ASAP
- [ ] Push the latest Inna/CRM changes to the second repo (the production-side repo, not just the staging one)
- [ ] Send Andres a screenshot of the Resend domain-verification failure (so Andres can show Faye what's needed on her GoDaddy)
- [ ] Research with Claude: how do scheduled email sequences queue when multiple campaigns collide on the same day past the Gmail 50/day or Vercel daily-cron limit? Don't assume — verify. (Open question Taiwo did not have an answer for.)
- [ ] Change `lead_source = "unknown"` rows in the DB to `"initial upload"` so the analytics pipeline labels are clean
- [ ] Separate AI sequences vs. manual sequences in the campaigns UI so it's clear which buttons trigger which
- [ ] Send Taiwo's project files / Inna project link to Andres directly (Outlook access issue blocking him)
- [ ] Take ownership of deliveries — when finishing a feature, message Andres with: "here's what I delivered, here's what's next" instead of waiting to be asked

### Andres
- [ ] Reply to Faye's email about Siren Beauty — apologize for the wrong staging build going live; explain the follow-up, point her at the corrected build, and confirm her video-feedback items are now addressed
- [ ] Verify the `facelogicfunctionalmedicine.com` domain on Resend with Faye when they meet — requires her GoDaddy DNS access. (Currently the only verified Resend sender domain is `moylab.com`; that's why sends with the new sender failed.)
- [ ] Demo the campaign send live with Megan as the test contact

## Open questions / risks

- **Email queue handling under contention** — unresolved. With 5,000 contacts, 5-email sequences, multiple campaigns potentially running, Vercel free tier giving one cron/day, and Gmail's per-day send cap, behavior when sends exceed daily quota is unverified. Could silently drop or unboundedly delay sends.
- **Sanity CMS image upload** — non-studio staff currently cannot upload images via a custom UI; only studio users can swap. Decision was "we don't want that" — but unclear if the Siren Beauty client knows she has to use the studio (vs. expecting a friendlier upload widget on the marketing pages).
- **Localhost link in tracked email** — when Taiwo tested locally, the click-tracking redirect URL was `localhost:3000/api/track-email/...`. Andres confirmed in production it should be the live URL; Taiwo confirmed it's only because his test was local. Worth a re-verify on the deployed instance before Faye sees it.

## Full transcript

Speakers: Andres Urrego, Taiwo Ola Balogun. 437 turns merged from VTT (~9,500 words).

**Andres Urrego:** We're done. I got a document for her login credentials, GitHub. For email. She has access to this document. Perfect. Okay, very good. But do you have access to it? There we go. OK. What else we got? What else we got?

**Taiwo Ola Balogun:** So, can you send me the documents? I can't access Outlook, but...

**Andres Urrego:** What's that?

**Taiwo Ola Balogun:** I, I couldn't access. Outlook, yeah.

**Andres Urrego:** You can't access the document?

**Taiwo Ola Balogun:** Yeah, no, I can access the documents, but I can see all the documents.

**Andres Urrego:** Oh, you can't access like the file itself, like the Inna project.

**Taiwo Ola Balogun:** But. Yeah, I'm trying to get all the files, so I'll be able to pick this one. But can you send me the files link itself for now?

**Andres Urrego:** Yeah. For. That's what I thought I was doing though. Oh. Hey. Yeah.

**Taiwo Ola Balogun:** Yeah.

**Andres Urrego:** Yo, yeah, yeah, I got two freaking meetings back to back. Wow. But yeah, like, that's nice, though, to know that, like, they don't need us to do the sauna stuff, you know. I know. I know. Yeah, so, okay, so you're gonna keep a sauna. We don't need to access it. Like, okay, you're cool with the meeting. And again, that's how it should be. It should be like, and like, okay, Jackie, you're good. We're being happy. Well, again, we go to back to the original contract. We don't have any of that garbage, you know? A man. We don't need any of that. So like, you know, I think she's going to get it done too, dude. I think she will, bro. I think she's going to get it done. I'm praying she'll get it done. Always let her get it done. I would just make all our lives so much easier, you know? For sure. Give me just a second, just give me just a second. Yes, Sir.

**Taiwo Ola Balogun:** What is up?

**Andres Urrego:** You can catch up. You can catch up backwards. You sure? Yeah, yeah, yeah, man. I'll just, I'll just, yeah, I'm gonna. Yes, I will go on, sorry.

**Taiwo Ola Balogun:** I wanted to ask that I was in the documents. Oh.

**Andres Urrego:** What document?

**Taiwo Ola Balogun:** Is it? Yeah, I think I sent it, Jason, and yeah, I also got the email sent to me. Was I need uh, 7 UC?

**Andres Urrego:** Oh, and then she replied, yeah. Yeah, I'm trying to figure out what I need to do.

**Taiwo Ola Balogun:** That's it.

**Andres Urrego:** Yeah, she's being a nightmare, but that's okay. I mean, I don't think she's in any garage. We just gotta make sure we deliver what she wants. So let's not make any more. Changes to any type of design until... she asks for it, you know what I mean? Let's align, we need to realign. I'm using her brand, I'm using her, so I'm trying to realign with.

**Taiwo Ola Balogun:** Yes.

**Andres Urrego:** Washing wines. Um, you know, uh, and then go from there. So. Yeah, I'll have to work on that. Yeah, I'm going to reply to that email here in a little bit. I just wanted you guys to be...

**Taiwo Ola Balogun:** No, I think, I think, I think that I said the website does not like reflect who she is.

**Andres Urrego:** She's weird because she liked, she said she loves the direction that we're going in. And then I add her colors and then she's like, yeah, I don't. It doesn't represent me, so I'm like, okay, well, let's... Let's talk about this. So, and then that's what I mean. Like she said, did you listen to my videos? So that's what I mean. We need to make changes based on what she asked for. So let's make those changes. I want you to write them down, Tyler. So we need to actually write those down. Listen to the video, write one by one of the issues. We fix them, we know, obviously we send one request. These are all, you know, user experience issues, so we'll just, I mean, then probably design issues, and you know, size of fonts, and you know, so we make a list, and then...

**Taiwo Ola Balogun:** I, I, I feel that I feel everything on the video.

**Andres Urrego:** Oh, you have already?

**Taiwo Ola Balogun:** Yeah, yes. Of. I did make this. I think made these things with her, I think removed. I do move science. And the I did move the animations also. And the text that we're cutting off, I did that. I did those Rosales.

**Andres Urrego:** Sorry, I had no idea I had muted myself. So yeah, she doesn't want that siren. Hold on, hold on, don't leave, don't leave, hold on, hold on. So she doesn't want the siren beauty on the header if we're going to have it in the front. She doesn't want, like the top header, she wanted those letters bigger or bolder so that you can see them everywhere.

**Taiwo Ola Balogun:** Okay.

**Andres Urrego:** There you go, right?

**Taiwo Ola Balogun:** This one, yeah, I made it big already.

**Andres Urrego:** Yeah, but you can't see him still, so maybe we need to make him pop out. Maybe we can make him bold and like bubbly. Like, you know what I mean? Like make him bold or bigger a little bit. I don't know. Let's test it out because he gets lost. So go up. Yeah. All the, yeah, it gets lost. It disappears. All the way to the top, all the way to the top. No, just stay at the top. Oh, show me what I want to see. There you go, it's gone. So... So maybe it transitions from this, you know, to whatever this looks like to that, and yeah, yeah, so now. I. Yeah, I think I'm gonna, I'm just gonna tell her, hey, I'm so sorry, we had pushed. I'm going to say this makes sense. We were going in the right direction. We had pushed an update that we had on our staging, so like on our development side that we didn't intend to use, but... We have now pushed the right one, but let's make those changes. Yeah, let's go through her videos and make sure, are we sure that we're fixing everything she asked for?

**Taiwo Ola Balogun:** I think. For the video.

**Andres Urrego:** Because the video is what, a minute?

**Taiwo Ola Balogun:** And just from the get-go, I want to remove everywhere that says science. I wouldn't say that. That's not my vibe. but I love all of the other philosophy, feminine, mysticism, and I'm going to look through some more, but so far that's what I'm noticing. And over here, science again. Let's remove science. Let's figure out something else. And then let's take off this, unless it does something.

**Andres Urrego:** There you go.

**Taiwo Ola Balogun:** He said, let's do something, and the thing is, this is like the homepage.

**Andres Urrego:** Hold on, hold on, hold on, let's just go ahead.

**Taiwo Ola Balogun:** And that might be too much to look at. I still need all of these fonts bigger. They're too small. Maybe they can be the same size as these letters. I love what you did with the mermaid right here. It's beautiful.

**Andres Urrego:** Nice.

**Taiwo Ola Balogun:** Okay.

**Andres Urrego:** But.

**Taiwo Ola Balogun:** And just from the get-go, I want to remove everywhere that says science. I wouldn't say that. That's not my vibe. but I love all of the other philosophy, feminine, mysticism, and I'm gonna look through some more, but so far that's what I'm noticing. Over here, science again. Let's remove science. Let's figure out something else. I think you probably have to have a meeting with that too, for us to be able to know for sure what she needs to be removed.

**Andres Urrego:** No, no, but, but see, we need to listen to what she's saying, though. If, if we we've now removed, hold on, hold on, we now removed all the things that we needed to remove, like that she didn't ask for, OK? Because I think that's where she was shocked, probably when she went to look at it the other day, she had sent me an email.

**Taiwo Ola Balogun:** Yeah, what she said was...

**Andres Urrego:** And she said, hey, I mean, this looks all jumpy or whatever. You know, what is this? And I said, okay, now let me look into it. So I love it. I don't think she's our client for this. So that's okay. This is, let's remove what she's asking us to remove. We need to talk, I mean, I can run the text, I guess, for the science thing, or we can, you know, to try and remove the wording science directly from the website and actually use it as.

**Taiwo Ola Balogun:** I do, I do only then.

**Andres Urrego:** All of them?

**Taiwo Ola Balogun:** I do you move all of them?

**Andres Urrego:** Okay, good. Perfect. Okay. So then, and then we figure out, yeah, those letters, like I said, they just need to be bolder, Taiwo. That's all she's asking for. The reason why she lost the book now, the book now is the same size, but it pops out because he has a layer behind it. Right here, they're hidden, they're gone. So we need to either create a white shadow, there you go. Now you see them, now you don't. they get lost until you start moving. So, I mean, we just need to give them while they're on top, like while they're transitioning, like as long as they're on the hero image, they need to have some type of, maybe they're boulder, because people, I don't see them. I mean, I guess I'm, you know, I'm just. You putting myself on her shoes, and then even here they need to pop out a little bit more. They need to be thicker, a little bit thicker, so that it, yeah, yeah, absolutely. Yeah, so, so here is a section we just need to deliver on what she's asking for, and then I mean, but that will take us a few minutes to do. I.

**Taiwo Ola Balogun:** I think from demo what I was, I think it was probably there's still more issues than stem because she said I was. Like, probably she was supposed to answer questions, and based on those questions, we are going to be using the AI.

**Andres Urrego:** No, because we've done that, we've done that, and look what she said, she said... She said, Andres, look. Uh... Like in the videos, she says, I love what you did here, I love the direction, I love this, I love that. But then she had messaged me the other day, dude, I told you, I told you right away, I messaged you and I said, hey, she doesn't like it. So now you removed it, but the last time she checked, that's what she saw. That's what I mean.

**Taiwo Ola Balogun:** Okay.

**Andres Urrego:** You know, so, so I can ask her more questions, and I will, I will promise I'll ask her more questions, but, but I need to figure out first. Yeah, but we need to figure out first, you know, just deliver on what she asked us for, right? She sent us some feedback, and then I wanted her, I need to explain to her that what I was saying was it was a follow-up. I didn't explain it well in my email, but I need to tell her that my email was a follow-up, and I need to apologize for the update that we pushed. They didn't need to go out, and and that's it, you know, that's it. I'll just say, look, you know, they update, please check on the one we have addressed the things that you mentioned in the video. You know, we have, and then, and then let's create a little list. I will, I want, I want you to look, I want you to take ownership for your deliveries. See, I need you to come out of the shadows kind of thing, right? So you finish. a project and you say, here's what I'm pushing, here's what I'm delivering. You know what I mean? Like for me, it's easy to hand over a project to you because I say, well, here's what I'm delivering and there's a project, right? Then you ask me the questions and I'll answer them. But when you're done, when you're done, just say, hey, Andres, look, this is what I did, this is what we're done with. Boom, this is what needs to happen next. You know what I'm saying? Because it's good. It's good to take ownership for the hard work that we're putting in. Okay.

**Taiwo Ola Balogun:** Yes, sir. So, what should I do concerning the text here, which is probably the only issue right now?

**Andres Urrego:** Um... Well, no, remember, she wants you to remove that Siren Beauty from the left. She also wants you to remove this, yeah, that one. Then those letters, like I said, make them thicker. Try a couple of things. Give them a white shadow behind them until they transition to the next look where it gets a full header barn.

**Taiwo Ola Balogun:** Okay, does she have a logo that we can put there? Because this was meant to be the logo.

**Andres Urrego:** When you scroll down 11. No, that that is, no, that that's it, like that is that is her logo, so like her logo is already the main thing on the on the, so what she's saying is, why do I need to have it twice? That's all she's saying, that she's like, that's that's too much distraction and she's right.

**Taiwo Ola Balogun:** Okay.

**Andres Urrego:** You know what I mean? That is her logo. This entire thing is her logo.

**Taiwo Ola Balogun:** Okay.

**Andres Urrego:** Maybe book now, and then on the other side, call us now, or, or I don't know, you know, whatever. I mean, yeah, let's so, so let's make that change. Um, and I, yeah, I love it. And then other than that, I think we're done, man. I think we're done. Well, being done as far as like getting back on her good side, I think it was confusing for her. I should have done better as well.

**Taiwo Ola Balogun:** Um, I think, so I think she can start with the studio also, so when I go to the studio, is then so redirect me to... But I think you have to add that, you we have to add that to.

**Andres Urrego:** Yeah, let's look at this. Hold on. I want to figure out first if it's going to work out. She's not asking for this yet. So I want to figure out if this is working first before... Okay.

**Taiwo Ola Balogun:** So, I'll reduce the time to 36 seconds. So, Polish.

**Andres Urrego:** Okay.

**Taiwo Ola Balogun:** This. St. Ten seconds, I think I have to wait 30 seconds. Off.

**Andres Urrego:** Um... OK, very good. Oh, yeah, there you go. Oh, wow. Oh, wow. What happened there?

**Taiwo Ola Balogun:** That publishes.

**Andres Urrego:** 396. Okay, very good. So it's 10, but oh, oh. So that that's supposed to change right to 10.

**Taiwo Ola Balogun:** Yeah, it's meant to change today, so now we can see if...

**Andres Urrego:** Okay.

**Taiwo Ola Balogun:** Have to reach.

**Andres Urrego:** Oh, so so far, that's all they... Oh, okay, let's see this.

**Taiwo Ola Balogun:** That's not changing. Still not changing everything.

**Andres Urrego:** Okay, okay, okay, but that's probably a code issue, so we'll work on that. So let's, okay, so.

**Taiwo Ola Balogun:** No, I'm trying to see if let me see this.

**Andres Urrego:** What kind of MacBook do you have, Taiwo?

**Taiwo Ola Balogun:** Um, this info.

**Andres Urrego:** Base.

**Taiwo Ola Balogun:** Okay, yeah, it has updated it, and I said we just have to read, like.

**Andres Urrego:** Very good, OK. Okay, very good. What else? So, you said there's some sections that we can't update.

**Taiwo Ola Balogun:** Thank you. Yeah, yeah, no, I do do that. I do work on that.

**Andres Urrego:** Okay, now everything can be updated.

**Taiwo Ola Balogun:** Yeah, let me see when this is going to change, so I think this was what happened, how to run the command.

**Andres Urrego:** Now, can they update the images?

**Taiwo Ola Balogun:** The image is, no, no, no, I don't think so. I can't open the images for now.

**Andres Urrego:** Then let's find out, okay? We can probably ask.

**Taiwo Ola Balogun:** I think it's just test, it's test changes that they can do for now.

**Andres Urrego:** Do you think so? Okay.

**Taiwo Ola Balogun:** His changes. There's also like the upload, yeah. Let me try it, let me try it. In as much as I don't want to. So, it's not working. That's right.

**Andres Urrego:** What is this thing called again, this software, this system?

**Taiwo Ola Balogun:** This one.

**Andres Urrego:** Sanity. Ohh.

**Taiwo Ola Balogun:** But. So.

**Andres Urrego:** Um... Two. Uh...

**Taiwo Ola Balogun:** Yeah.

**Andres Urrego:** I was like, who's calling me? I don't see this call coming anywhere.

**Taiwo Ola Balogun:** Yeah, it's been installing, but I don't just understand.

**Andres Urrego:** Be fine. I think I'm gonna buy us a Codex license once we start, once we get paid for this project, so that's why I'm trying to get him, you know, pushed down. Oh.

**Taiwo Ola Balogun:** Codex, I think Claude is enough for now, sir.

**Andres Urrego:** I, I don't.

**Taiwo Ola Balogun:** And I know, I know has been doing, like, some wonderful works for us, and I think they are the same of whatever we are doing.

**Andres Urrego:** That's what I mean; I think we're gonna have one of each. Because I mean, even from, well, I mean, yeah, we can, are you using Claude? Are you using Claude yourself?

**Taiwo Ola Balogun:** Yeah, yeah, I'm using it. I'm using cloud code.

**Andres Urrego:** Good. How's it going? You like it?

**Taiwo Ola Balogun:** Yeah, yeah, it's good, it's good. It's been good, very good.

**Andres Urrego:** Well. Yeah, don't, don't, don't cut, don't make some changes to catch up to. But I think as far as automations, I think it's... So they're behind. Look, yes, the site already has Sanity Studio embedded, Studio C, Papa does the built-in path for managing all content including images. Ohh. Update, upload, replace images on any document services, team members, testimonials, on page side settings, et cetera, edit any field defining on schemas. Publish changes, the live site picks them up within 30 seconds. The public website's always read-only, there's no upload. UI on the marketing pages and the read client uses da da da with no green token, which is correct for security. Single tones from a bar log from duplicating the studio, but their images can still be swapped. If you want a non-studio user and staff members, it's us to upload images directly from a custom note. We don't want that. Okay, so yes, so it can be done. Oh, there you are. Okay. Ohh, you're doing it already. I was just somebody to start reading.

**Taiwo Ola Balogun:** Hey, let me see. To. Yeah, change. So, it's got changed, and I think let's talk about... And let's wait for this. Let's see if it took you longer then, let's see if it changes. I thought this changed. How is James?

**Andres Urrego:** Give it a second and see.

**Taiwo Ola Balogun:** So, I think I'm just, I'm just going to, so I think we can move on to... Let's see if it's not true. Yeah, yeah, it's too. It is in our eyes now. These are selling right now. Sports reports. So I think Jacob is going to get back to me today or tomorrow on Inna.

**Andres Urrego:** Anita, okay, very good. But let's look at it. Let's look at it. I mean, I mean, so it's just...

**Taiwo Ola Balogun:** So, this is the dashboard. Is the dashboard there? So, let's start with adding any contacts. Uh, this, this is not still working now. This is AI. That is not working.

**Andres Urrego:** Why it was?

**Taiwo Ola Balogun:** It was before.

**Andres Urrego:** Yeah, I, I, I, I've done it, I've showed it before.

**Taiwo Ola Balogun:** OK, OK, probably test that. I don't have like a card here. You can test that on your end. Let's see.

**Andres Urrego:** Okay, let me do that. Oh, how do I log in? What is what is the login information?

**Taiwo Ola Balogun:** Um, I think other users.

**Andres Urrego:** I tried with my existing password that I had, but it didn't work.

**Taiwo Ola Balogun:** Yeah. Has to be here. Okay, Moil.

**Andres Urrego:** But what email do I use? Looking what password?

**Taiwo Ola Balogun:** I think I'm allowed to stop.

**Andres Urrego:** But what password do I use?

**Taiwo Ola Balogun:** Moil, capital letter M.

**Andres Urrego:** Nice, okay, thank you. Okay, so we need to make this thing mobile responsive ASAP number one.

**Taiwo Ola Balogun:** Okay.

**Andres Urrego:** Yeah, because it it it's yeah. Okay, scan card.

**Taiwo Ola Balogun:** I mean, I didn't, I didn't say this also.

**Andres Urrego:** That's okay. That's okay. That's okay.

**Taiwo Ola Balogun:** Same, yeah, yeah, yeah, just wanted to show this.

**Andres Urrego:** We don't need to eat it.

**Taiwo Ola Balogun:** So, so, so. I did.

**Andres Urrego:** Yeah, no, the business card thing is working perfectly fine.

**Taiwo Ola Balogun:** Yeah, this one is working, so I think this one is something. So, so that... Yeah, yeah, yeah, it's worked.

**Andres Urrego:** Nice, very good.

**Taiwo Ola Balogun:** Now to change that back. In the back. Gibson.

**Andres Urrego:** No, I love it, man. It works. Works.

**Taiwo Ola Balogun:** Oh, it works. Okay, the uploading standard, it worked.

**Andres Urrego:** The Business Guard works. Yeah.

**Taiwo Ola Balogun:** Nice, nice, nice, nice, nice, nice.

**Andres Urrego:** And those calls are minimal for the client, you know, like I can leave them in a bunch of like free, they just sometimes you will fail, sometimes you won't, they can just pay for it, they will spend $5 a month, you know, that's what I told Megan, I said, look, all you're creating are emails, you're not going to spend more than $5 a month.

**Taiwo Ola Balogun:** Yeah, yeah, actually.

**Andres Urrego:** You can use Gemini 2.0. All we'll do is, you know, once we get her voice, then we'll implant that into the email so that it always starts creating with her voice kind of thing.

**Taiwo Ola Balogun:** That is right. Yeah, that is, that is, that is one.

**Andres Urrego:** Because if that's, see, that's what I was saying the other day on the call. That's how we turn all of these little things into like their own little agents, right? You just start giving them the files that they need so that the cheap models can actually have that feel, that agentic feel, by just being able to grab the information they need when they need it.

**Taiwo Ola Balogun:** That's right, um, yeah, um, okay, this didn't update. Any update for this also, so I have to, I have to do myself. I think there were some things that were not updated. Well, it's probably just some sort of command, and I use something like command this to do. I. Now, the thing is, the thing is, it's not very hard. I don't think it's very hard to build a contents management system. It's something that we can actually build.

**Andres Urrego:** That's what I'm saying, yeah, well, yeah, yeah, yeah, so like, like, like one that comes with the websites we build, yeah.

**Taiwo Ola Balogun:** I think we just have a plan, a plan is, do we want to add the CRM, then add a content management system also?

**Andres Urrego:** Like a standard. But then we would have to build a website for them. See, this is what I told you last time. Like, click here, create your website. We'll send you a draft if you love it. Select, we'll help you. We'll send you the instructions for you to go push it or speak to one of our representatives to push it for you. Done. For an extra 50 bucks, whatever. You know what I mean? Like, it's it it it it we can create these websites in like literally in minutes automatically the first draft better than most people I've ever imagined. I mean, it's a no-brainer. And then you say, do you want the CMS? Yes, okay, boom. Attach it, and then it creates automatically from the website that's already been built. And if they want the CRM, then you know, we give them a subscription to the CRM. I always thought of the CRM as a subscription alongside the lead generator that I have created.

**Taiwo Ola Balogun:** But this. So. Punish. Okay, I think...

**Andres Urrego:** I love it, I love the way you're thinking, because that's exactly how we gotta think.

**Taiwo Ola Balogun:** Are these on the plan also FAQ? She can add new documents here. She can't hear very cute. But generally, I think this is working. She can change the announcements here. So, you can change an announcement here.

**Andres Urrego:** Nice.

**Taiwo Ola Balogun:** Thank you.

**Andres Urrego:** Very good.

**Taiwo Ola Balogun:** So, it's announcement, so you can share that, but I think should we should we have like it announcements link? And I just wanted to just text.

**Andres Urrego:** Oh no, that should go to a link, yeah. There is a link for that somewhere. Maybe it's in the head of the footer.

**Taiwo Ola Balogun:** Yeah, like, I'm like thinking probably she wants to use another link, like she wants to change the link in this announcement, because now this announcement here is only controlling just the text here, not the link here. Yeah. Yeah, I think. Guys, on this end.

**Andres Urrego:** Very good, man, so... You want to go over logic real quick, see if anything is pending there, other than the email address.

**Taiwo Ola Balogun:** No, I, yeah, I, I thought that was like...

**Andres Urrego:** Can it be? Can I test it today? Can I send that email out, or we can't send emails out yet?

**Taiwo Ola Balogun:** OK, just test the email. So, right now, I'm using two things for the email, so I'm using Gmail API, and also, if we send fields, it's going to use Gmail API. So, it's like, there's a fallback now.

**Andres Urrego:** For email.

**Taiwo Ola Balogun:** Yeah, for email, there's a fallback. But the other issue with GM API is that I think design gets lost. You just need to send it as a plain email.

**Andres Urrego:** Very good.

**Taiwo Ola Balogun:** I was gonna send email.

**Andres Urrego:** Okay.

**Taiwo Ola Balogun:** So if we send ever fills, it's always going to fall back to that.

**Andres Urrego:** Okay. Very good, and you've tested it and it works.

**Taiwo Ola Balogun:** Yeah, Jacob sent me a mail today from...

**Andres Urrego:** Can we can we test it out real quick? Because I had the meeting with her, and you know, you know, look, I, you know, I hate getting frustrated, but if there's something that frustrates me is jumping into the call with the client, trying to show them what works, and then it doesn't.

**Taiwo Ola Balogun:** When he was... But. Am I using? I think we are using... No, I'm not using this. One of these. I will move the new updates to my end, so I'm going to be using face logic later. Sir. I wasn't able to upload all the contacts. I think I told you about that.

**Andres Urrego:** About.

**Taiwo Ola Balogun:** All the 5000 converts are so little.

**Andres Urrego:** Yes, yes, yes, yes, very good. Let's click on that. Let's click on contacts. Yeah, okay, yeah, no, I think this is good. They can search for the...

**Taiwo Ola Balogun:** So, it's really personal there. So, he's not loading everything else from, he's doing a batch loading, so he's loading 500, so even if additional 500, I just want to click on load more, he's going to load, and I said the 1000.

**Andres Urrego:** What? Oh, God. Yeah. Ohh. Very good, very good. OK, OK, very good. I love it. Well done, and then you scroll how many? OK, let's go down.

**Taiwo Ola Balogun:** It.

**Andres Urrego:** So then to get to the full 500, go down real quick. Oh, okay, the same progress, why? Okay, good. Very good. Very, very good. Now one more thing. I would like for us to... Yeah, so this is pushed. Yeah, okay. Is this pushed to both repos?

**Taiwo Ola Balogun:** No, no, this is pushed to just this report for now. I think some are, some are, some of it are pushed already throughout, but I think a list of the changes are just here on this one. I want us to press the email, right? Let's switch a new campaign.

**Andres Urrego:** Yeah, let's do that. Let's do that. Send me an email. Let's do that.

**Taiwo Ola Balogun:** Um...

**Andres Urrego:** Yeah, let's do a campaign and let it run for five days. I want to be able to be ahead of her at least by 5 days. I mean, like at least by a day or a couple of hours, knowing if I'm going to get them or not.

**Taiwo Ola Balogun:** I.

**Andres Urrego:** Ohh.

**Taiwo Ola Balogun:** See if patients. See. H.

**Andres Urrego:** Keep.

**Taiwo Ola Balogun:** Okay, I don't think. Oluwole. Okay, Andres, can you log in there and try to create your own contacts?

**Andres Urrego:** It didn't let you create a contact.

**Taiwo Ola Balogun:** Ohh yeah, I miss, let me get your contacts. And.

**Andres Urrego:** Why don't you think he would let you create a contact?

**Taiwo Ola Balogun:** Sir? No, is that was that was not what I meant.

**Andres Urrego:** Why do you think?

**Taiwo Ola Balogun:** I said, uh, you should create it from your own, and not that I could not create it yet, but I was, I was at the point of creating.

**Andres Urrego:** Okay. Right, right, you wanted me to, you wanted me to. You wanted me to also test it.

**Taiwo Ola Balogun:** Yeah.

**Andres Urrego:** Yeah, yeah, for sure. Okay, you created it already and then we can move it to contacted. Okay. Now, yeah, here's what I wanted to, and this is why I was asking if our repo already matched this one because I want to open that when, unless this is already done, when they are sent an email, that should automatically put him into. Contacted or.

**Taiwo Ola Balogun:** Right, yeah, let me. OK, let me let me send you an email, because I think I think I did that, I think I did that, but let's try that.

**Andres Urrego:** Okay, beautiful. Okay, good. Okay.

**Taiwo Ola Balogun:** OK, same for this job, OK. Images working, definitely. Yeah. Okay.

**Andres Urrego:** Yeah. But...

**Taiwo Ola Balogun:** House.

**Andres Urrego:** But...

**Taiwo Ola Balogun:** Anita, did you get any message?

**Andres Urrego:** Uh, no.

**Taiwo Ola Balogun:** Update. Is going shaking again?

**Andres Urrego:** Ohh. Oh. You send me a document.

**Taiwo Ola Balogun:** Yes, you say documented.

**Andres Urrego:** Yeah, there's no body email.

**Taiwo Ola Balogun:** Yeah, just only I Andres. I only I Andres.

**Andres Urrego:** Yeah, there you go, next one. Oh, but you added a document and that, and you threw it.

**Taiwo Ola Balogun:** I did an attachments, you see the attachments.

**Andres Urrego:** That's so cool. Yeah, so now she can send like forms or like, hey, well, she probably does that elsewhere, but that's okay. Yeah, it's great.

**Taiwo Ola Balogun:** The thing is, the issue is... Uh, when I try to send... I. Okay, so bold. Italics. Such a problem. Strike ****. Oluwole. I think what's that? Okay. A link. Two. To. Thing.

**Andres Urrego:** Yeah. Times. All, but the link should replace the click here.

**Taiwo Ola Balogun:** Okay, so can you see the message now? Let's see again.

**Andres Urrego:** You send another one.

**Taiwo Ola Balogun:** Yeah, send another one. I sent an alarm.

**Andres Urrego:** Yeah, that works.

**Taiwo Ola Balogun:** Okay, now you see this off.

**Andres Urrego:** Yeah.

**Taiwo Ola Balogun:** Dowers. I'm trying to figure out the reason why.

**Andres Urrego:** Now, now the only thing is that, see, you send me two emails, ohh, but you signed in as Taiwo, right? You signed in as Taiwo, check and see, well, it it says there is no contact with this with this lead or this person like that, like if you go and click on my name, right? It it. It doesn't show any activity and it should track that activity of those emails that have been sent.

**Taiwo Ola Balogun:** OK, on the mailing, yeah, I should show it's on the mailing.

**Andres Urrego:** A 100%.

**Taiwo Ola Balogun:** Talking to us, John. Mailing. But I changed the stage to contacted.

**Andres Urrego:** I moved it, I moved it. I don't know if it was already there. I had moved it before, yeah, sorry.

**Taiwo Ola Balogun:** You remove this. OK, let me move it back. And then we'll get back.

**Andres Urrego:** And then let's send the next email. Now, if we're telling people click here, then that's probably where the link should go. Does that make sense?

**Taiwo Ola Balogun:** Yes, you can; you can add a link to it. Let me get this. Is it link here? Okay, as it is.

**Andres Urrego:** Sihuemare para sierra que si. For Casta Fernando. Ahh. But it's just good though. I know.

**Taiwo Ola Balogun:** It is the same with this wall. Let me remove the documents, just send it again. Okay, or that might be an issue with... The link here goes to google.com, but what I'm saying here goes to google.com. I think we are, I'm still going to be working on this editor.

**Andres Urrego:** Okay.

**Taiwo Ola Balogun:** OK, do you change it because Max, you move it now?

**Andres Urrego:** And then that that didn't allow for that didn't allow for her to use AI in this step. Did you notice that it didn't it didn't allow to do like, oh, create email for me and then just type something, you know, it's basically we're creating that email. Like, it's a manual process, right?

**Taiwo Ola Balogun:** No, you can use AI, but it's going to be like it's going to put it on the editor also.

**Andres Urrego:** But you have to go to the to the campaigns. OK, good.

**Taiwo Ola Balogun:** I think now I wanted to see that it changed it to contacted.

**Andres Urrego:** Okay, good, good. All right, awesome. Now, let's on campaigns. Yeah, let's click on... Ohh. What is this? No, this new campaign? Ohh, no.

**Taiwo Ola Balogun:** OK, let me start, let me, let me start with, let me start with this sequence.

**Andres Urrego:** No, no, wait, wait, wait, go through that again, go through that process because that's not something broken there. Let's not leave it broken. What is this?

**Taiwo Ola Balogun:** What's up?

**Andres Urrego:** Interesting. What campaign is it saving if it's not creating anything?

**Taiwo Ola Balogun:** Saving like, ow.

**Andres Urrego:** Well, like, what is this button for? What were, what do you do with this?

**Taiwo Ola Balogun:** Which of the button?

**Andres Urrego:** Like right here, this screen that you're in, what do we do in this screen? What is this screen for?

**Taiwo Ola Balogun:** It used to quit a campaign.

**Andres Urrego:** Right, but the campaign, no. I don't think so because where do you create it? I think we already have to close out of it real quick.

**Taiwo Ola Balogun:** This creates, this one use AI. This one does not use AI. This one use AI to create a sequence. This one does not use AI to create a sequence. This is a sequence reader.

**Andres Urrego:** Got it. So those are the manual ones. Okay. Do you think that we can do something there, a little change on the UI to make sure that we can separate them accordingly? Like AI sequence, AI campaigns and sequences, and then your manual? Just because, yeah, I don't.

**Taiwo Ola Balogun:** Yeah. He's not in my know.

**Andres Urrego:** What's a new template? What does the new template do?

**Taiwo Ola Balogun:** Yeah, email them, please.

**Andres Urrego:** I can't remember, sorry, I haven't tested since I handed it over to you, so...

**Taiwo Ola Balogun:** Okay.

**Andres Urrego:** Oh. We should use AI to create their templates or help them create their templates.

**Taiwo Ola Balogun:** Yeah, I am seeking to go and work on these templates because I needed to use this, the editor I just created to be able to edit it properly also, and I see expecting HTML. Okay, so if you add here to this question of template also, like when they create template, they be able to set up the templates. I need to select the templates here. I think templates just is for like a single campaign. Just for a single campaign, you want to send a single mail to people, you can click the template that you cancel it. Of this. So, this email. Easy preview, yeah. Now, in this email, I can add a couple more things, so this link here, I can copy. Call it to bought in. Um, yeah, um, what I had to say was, um... Maybe I should need to get a footer to be able to add this, so it's going to be custom, a custom footer. So, this is it, so it's going to create this. It's gonna source, but right now, since we are no longer using, since she's not using the... The premium. Of myself, so if you can't like send at a specific time, she has to send just once the just once, so and it's mostly, yeah, so this.

**Andres Urrego:** Yeah.

**Taiwo Ola Balogun:** It's not going to be used; this best sent time is not going to be used because it's only going to send it in only if you want to send it now. So, this is a preview.

**Andres Urrego:** So, huh, so if we, if if they schedule 50 emails, it would only send them once, but what if today there is three different campaigns that go out today?

**Taiwo Ola Balogun:** Three different campaigns that goes out to.

**Andres Urrego:** If I set up a campaign for the next seven days, right?

**Taiwo Ola Balogun:** Yes, sir.

**Andres Urrego:** And I have, and I have another one that runs every three days. On this, what if both campaigns land on the same day? Will they all get sent out on the same day?

**Taiwo Ola Balogun:** Yeah. Yeah, I think they're going to get sent out on the same page, because the phone, the phone wants this reschedule.

**Andres Urrego:** Well, I don't want you to know. No, I don't want us to think. I don't want us to think. I want us to be 100% sure. I will like, let's not leave any rock unturned. That's just, it's lazy on our end to assume. Let's ask the question. Let's find out. Because what happens if, yeah, I mean, if they got 3 campaigns going on and it could happen, they got three different types of clients. I wanna make sure it's not all going to like crash, and you said it's $5 a month.

**Taiwo Ola Balogun:** So.

**Andres Urrego:** You said it's $5 a month on Versail?

**Taiwo Ola Balogun:** I said what? Is it $5 a month?

**Andres Urrego:** For the, for the, for the crown jobs or whatever.

**Taiwo Ola Balogun:** No, they have to subscribe to the $20 plan. He wants to be able to run con jobs like every every hour.

**Andres Urrego:** So it only lets you set up one crown job per day.

**Taiwo Ola Balogun:** Yeah, it's only once one cool job, but the premium plan on the last 10 before, maybe.

**Andres Urrego:** Yeah, see, that's what I'm saying. So if there's 27 leads from one campaign and 40 from the other one getting sent out on the same day, the limit is 50 emails.

**Taiwo Ola Balogun:** What?

**Andres Urrego:** You see what I'm saying? The limit is 50 per day. What happens to the rest of the 20 some, 23, 24 emails that don't get sent out that day? Do they get the queued for the next time? See what I'm saying? Like we, these are things that are very possible that they will happen and it's not as linear as we see it sometimes.

**Taiwo Ola Balogun:** So, like, can you can you explain that again?

**Andres Urrego:** Okay, so I sent a sequence today. I created a sequence today.

**Taiwo Ola Balogun:** Yes, sir.

**Andres Urrego:** And then tomorrow, or in two days, I create another sequence.

**Taiwo Ola Balogun:** Okay.

**Andres Urrego:** The first one is 7 days, this one is 5 days. But in one of those days, they both collide. And that puts us over, like it puts us over the 50 emails for the day. What happens is they're only getting sent once a day. Two things. How are they being queued and what happens to the ones that don't make it to the 50 emails per day and now are getting rejected or don't make it to today? Do they get sent into a queue for tomorrow? And how does that queue if tomorrow there's already 50 emails set up? which ones get sent out first and which ones have to wait. You see what I'm saying? Because this is very possible. She has 5,000 people on there. So we only have seven days if she's running emails to 5000 people a month. Five emails per person, that's 25,000 emails. How do we make sure that they don't crash, and how do we make sure that at least they're getting queued, even if it takes three months for those emails to go out?

**Taiwo Ola Balogun:** I didn't consider this. I think was that.

**Andres Urrego:** That's okay. But that's okay. That's what I mean. That this is the, we have the conversation with Claude and we say, okay, well, what's good, how are we preparing for this? Right? You know, how are we preparing? We only get 50 emails A day. What happens if the client is sending 5 sequences with 100 clients in each? How do they collide and what happens when they do? How do we queue them? How do we are automatically creating that queue? So, the scheduled things actually get scheduled and go out. The.

**Taiwo Ola Balogun:** OK, it sent it to you. Give me rentouts.

**Andres Urrego:** Sorry, what was that?

**Taiwo Ola Balogun:** I said the email went out, the email went out.

**Andres Urrego:** Okay, let me check.

**Taiwo Ola Balogun:** See you.

**Andres Urrego:** Beautiful, it's there. I love it. Boom, start now. Takes me to, oh, there was, oh, that didn't work. I clicked on the link and it said localhost 3000 API, track email, blah blah blah, Moil love.com.

**Taiwo Ola Balogun:** Excuse me, this.

**Andres Urrego:** The, the, the last email you just sent me.

**Taiwo Ola Balogun:** Is it the one with, are you wondering why your digestion feels like no startup?

**Andres Urrego:** Your digestion, yes. 1154, 2 minutes ago.

**Taiwo Ola Balogun:** Ohh yeah, this is one tracking. At the uh, he's tracking the click if the email has been clicked.

**Andres Urrego:** Oh yeah, but it's not opening when I click on it.

**Taiwo Ola Balogun:** Yeah, it is it open?

**Andres Urrego:** No, no, no. Because it it came in with local host 3000, no worry.

**Taiwo Ola Balogun:** Spin. Is. Okay, it works for me. It worked for me, so I think these all are going to be changing here. Once we change this, it's going to be going to the URL. Please should track the links.

**Andres Urrego:** Say that again.

**Taiwo Ola Balogun:** Yeah, this is, we are tracking the links. Speech.

**Andres Urrego:** Right, but it should still open, it should still open, whatever the link is.

**Taiwo Ola Balogun:** It's opened here. I think I clicked on because I could not open it yet, so I click on open a new tab. No, so I can't open it.

**Andres Urrego:** What's that?

**Taiwo Ola Balogun:** Yeah.

**Andres Urrego:** Can you send it again and see if it works this time?

**Taiwo Ola Balogun:** Can you, can you just click on it and open a new tab?

**Andres Urrego:** Say that again.

**Taiwo Ola Balogun:** Like, open it on a new tab. Like this.

**Andres Urrego:** Yeah, I'll try it. Hold on a second. But I mean, it just needs to work when you click on it, because clients are not going to know to go open a new tab. Right? They just, it just has to work when you click on it. Yeah, I mean, when I click on it, it says localhost 3000 API track, whatever. Um... So, let me see. Yeah, no, it doesn't work. So, he takes you where you need to go? Can you see it? Can you just have it?

**Taiwo Ola Balogun:** It took me to where I needed to go. Can you show your screen? Let me see this.

**Andres Urrego:** Let me know when you can see it.

**Taiwo Ola Balogun:** Okay. Okay, I can see it now. Yeah, did you to it didn't the link didn't open or didn't take you to anywhere, that's what I was trying to like verify. The lake is not going to open because it's local hosts, but once you click it, it rains.

**Andres Urrego:** But you said it works for you.

**Taiwo Ola Balogun:** It is. Yeah, it worked for me because my local house is like open.

**Andres Urrego:** Oh, I see, because you have it in your okay.

**Taiwo Ola Balogun:** Yeah, the thing is, I'm testing this from locally. I tested it locally.

**Andres Urrego:** Ohh, okay, okay, so it should have it would have it was never gonna open for me.

**Taiwo Ola Balogun:** Do I sense that? OK, OK, let me let me contact you for me. Yes, yes. See. Bounce. And thoughts? See. Play. It is so much. Segments. Just said names. Thanks.

**Andres Urrego:** But.

**Taiwo Ola Balogun:** OK, Andres, can you see something? I want to show you something.

**Andres Urrego:** Yeah, go ahead.

**Taiwo Ola Balogun:** Okay, so this is something that Jacob tested today. Now, um, I told you that we are tracking it, so you track the dates I received this. The date I opened it, tracked it.

**Andres Urrego:** Yes. Yes.

**Taiwo Ola Balogun:** Now, what happened was, in order to send this step. Because I think there are two emails in the state. Got 2 emails in this tab. The email started on 2nd. The email started on 2nd.

**Andres Urrego:** And then you send one on the 50 app every three days.

**Taiwo Ola Balogun:** Cell phone. Second of, so, um, yeah, let's go to the same log, so if since the first one. On 2nd of May. It send the first round then. The second. The second was sent to the. Second or sent, that was on. It said it, 3:00. Is it using universal time, because I think it's meant to send its? Sue, it was meant to send it through, but probably is using the reversal time plus one 'cause I was thinking 2:00 when I've seen 3:00. It's 3 o'clock, 8 A.m., it tells us.

**Andres Urrego:** Right now.

**Taiwo Ola Balogun:** Yeah, I think it's true.

**Andres Urrego:** Twelve.

**Taiwo Ola Balogun:** Quite nice job. And that was four hours ago.

**Andres Urrego:** Yeah.

**Taiwo Ola Balogun:** At 2:00, 2:00. I don't know, I did 3:00, but it was 2:00, it was mentioned to, oh ****, probably, I, I think calculates through. Oh, probably certainly does universal time. Yeah, it's certain that I still setting that universal time. There is a bit for sale, for sale, for sale. Foxing Astro Growth. Two. Hills. Yeah, he sent it's 3 o'clock. He sent this to me. This was the scheduled one, and it's mapped out the time I opened it. Now, it's wanted to send it. Look at something. It's wanted to send it using the send. You tried to send this email, user is sent, but you send field, it switched to Gmail API. Let me show you this. This is 3, this is step 2 email. Let me open my, I think, sends it switch mail.

**Andres Urrego:** Yeah.

**Taiwo Ola Balogun:** Out of, and I think this is the the media. So, to go. Business, yeah. Okay, this is it. I was thinking about a conversation, if you have any good blog. Is the email. So, it's 2 o'clock. This is Emilia now, once we send field. It sent it to its Jacob's Gmail account, because our send our send is connected to partner@moylab.com, but it sent it with Jacob's Gmail, because Jacob already has access, so Jacob Google account that was connected, so it uses his Google accounts using Gmail API to send the mail. Because this already had error, this already had error. He's with you.

**Andres Urrego:** Okay.

**Taiwo Ola Balogun:** He's already at LOA. I was surprised when it moved. Is that it? It's filled yet, so let me go to, let me go to the blogs. An hour ago. Yes. Oh. Yeah, that was easy. I chose not going. Definitely, these two are just not going. This was from which one? Uh, Andres, give me like a couple minutes. Let me check this out. This looks like, uh, I think we we changed it from partner.com.

**Andres Urrego:** Okay.

**Taiwo Ola Balogun:** So, this check. Play.

**Andres Urrego:** Right.

**Taiwo Ola Balogun:** Thumbnail. Yeah.

**Andres Urrego:** Oh.

**Taiwo Ola Balogun:** This is why it was not going. The mail didn't match the IP address. No, no, no, no. This is for my trace. Something. Ahh, it's going to be working now. So, Andres, I think one thing that the tests, what I should not verify was the fact that is reverting if we send fields is going to revert to using GM API, as you saw it in the logs, and also what caused...

**Andres Urrego:** Okay.

**Taiwo Ola Balogun:** The recent to fail was the fact that we changed the email that you are going to be sending it, because partners at molar.com is what we verified for this API key, yeah, but we are using this, so it could not verify this face logic functional medicine.com, it's not very very domain, we are using molar.com.

**Andres Urrego:** Okay. Okay.

**Taiwo Ola Balogun:** Dot, so that was just the reason why it didn't work. And so far, with every error, I think that was easy why it was working locally and it was not working.

**Andres Urrego:** How do we verify that feed logic functional medicine.com email? How do we do that?

**Taiwo Ola Balogun:** If she has the domain, if she has the Go Daddy, we have to verify it.

**Andres Urrego:** She has it, I mean, I'm pretty sure, but when I went into her... That's so weird.

**Taiwo Ola Balogun:** If she has it, we'll be able to compact.

**Andres Urrego:** Send me the screenshot, please. Send me the screenshot. So I can show it to her when I meet it, when I meet her.

**Taiwo Ola Balogun:** OK, so that is why it's causing the email, and I think... Uh, is the transcript of this call on SAT are we able to get um the things that we spoke about?

**Andres Urrego:** Absolutely, for every project, yeah.

**Taiwo Ola Balogun:** So, the scheduling is going, I'm sure of that now that schedule is going, because from the logs that that we saw you plus.

**Andres Urrego:** But it's just once a day. We don't know yet how scheduling will work when there is many emails from different sequences conflicting in one day, what's being queued, what's not being queued. That's very important and we need to understand that.

**Taiwo Ola Balogun:** Yeah, I sent one. Yes, I think I will be.

**Andres Urrego:** Yeah.

**Taiwo Ola Balogun:** But I think for your for your test, is this enough?

**Andres Urrego:** Yeah, yeah, for sure. I just need the email to go out. I don't need it to break. I need the email to go out, period.

**Taiwo Ola Balogun:** Set. Okay, I think you can go and test it out to your end when it's finished deploying if the emails are really going out, but I think I already verified it said that emails are going out.

**Andres Urrego:** Fantastic.

**Taiwo Ola Balogun:** So, I think you can go and verify it on your end if the mates agree not to you. Ohh, let's, let's do one more, let's do one more.

**Andres Urrego:** Just do one more.

**Taiwo Ola Balogun:** As well. And I think, so can you, can you, I will open the emails. Oh, yeah.

**Andres Urrego:** Yeah.

**Taiwo Ola Balogun:** Yeah, yeah, I think.

**Andres Urrego:** We've gone over them, I've showed you.

**Taiwo Ola Balogun:** Yeah, yeah, yeah, yeah, I'm trying to get... Because, yeah, is Saint-Cierre. Yeah, okay, not on on on. Yeah, let's try now, let's try that one, and this now, let's do the manual one. Ahh. Ohh, send email this sequence. Segments, I think I might probably move this, so I will move this to, there's no reason why that here, I think we just keep segments and customers.

**Andres Urrego:** Yard.

**Taiwo Ola Balogun:** That's if we need this CSV. I would just...

**Andres Urrego:** That's okay, yeah, we can do that. So, from okay.

**Taiwo Ola Balogun:** Yes. I don't see it. K. Yeah. And for seconds. And you got it to use us on that thing also is that there's no need for this auto sending because it's automatically scheduled. So I think there's no need for us to actually be saying, okay, switching off scheduling because it's automatically scheduled.

**Andres Urrego:** Right, right, right, right, okay, good.

**Taiwo Ola Balogun:** Volunteering is not really, not really, so off of that.

**Andres Urrego:** Either send now or or schedule it, that's it, yeah.

**Taiwo Ola Balogun:** Here, now. Is it for smell? Is it for smell? I think I love these variables to be able to make it personalized.

**Andres Urrego:** Yeah, yeah, that's perfect. No, I love that you put that there because that is that is fantastic. That feels again, it feels personable.

**Taiwo Ola Balogun:** Yeah. Okay. I think you added this test user, the testing mode, so it's only going to send emails to people that's. Have that test moved on.

**Andres Urrego:** I need that on resend.

**Taiwo Ola Balogun:** Sir.

**Andres Urrego:** Is that on resend?

**Taiwo Ola Balogun:** Yes, I saw. Like, no, is here, is in the settings. In the settings, in which you can talk with to test mode or not. Basics. Company, yeah. Yeah. You can talk with his test mode or not.

**Andres Urrego:** Very good.

**Taiwo Ola Balogun:** So he's only going to send it to people with his test contacts. It would, at this contacts, it will send some paste email and everything.

**Andres Urrego:** And do we have an opportunity to test, send people as test contacts?

**Taiwo Ola Balogun:** Sir, yeah, yeah, um, you are test, yeah, test contact it.

**Andres Urrego:** No.

**Taiwo Ola Balogun:** This contact.

**Andres Urrego:** Oh, nice. So that's okay, very good.

**Taiwo Ola Balogun:** Same thing, I think same thing as me, I said, this one box here. Yeah. Ah, my contact is not yet here. I have to note for that. OK, I see. So I mean, there's contact also. I missed contacts also. Um, yeah, think. We can. You can move back to the campaign, yeah. And this. Let's do the same now for the sentence. It's, so, yeah, I think this is, if you see the logs, yeah.

**Andres Urrego:** Can you add her as a as a test contact, please, so I can so I can test with her and she can see it live?

**Taiwo Ola Balogun:** Yeah, if you have the contacts, you just have to switch on the text contacts.

**Andres Urrego:** That's what I mean, just, just can you add her right now, just so it's already there?

**Taiwo Ola Balogun:** I can upload it. OK, let me send those our mail, but let me just share my mail. Thank you, I'll be able to like get to the office. Ohh, motion. Hi, Taiwo, we are sending our up to see you there, so it went out. Twenty hours, yeah, it went out.

**Andres Urrego:** It cut out. Or is that all you said?

**Taiwo Ola Balogun:** Yeah, and yeah, you see, you see, you already showed that I opened it already. OK, you cannot put your own, unless if your own is going to show that, so they want, but I add that to the.

**Andres Urrego:** Interesting. Thank you.

**Taiwo Ola Balogun:** Because.

**Andres Urrego:** Sorry.

**Taiwo Ola Balogun:** Okay, what? What is the measure?

**Andres Urrego:** Megan Miller and then the email you have it is the hello at whatever.

**Taiwo Ola Balogun:** Okay, yeah, again. Where did it? She's not.

**Andres Urrego:** Yeah.

**Taiwo Ola Balogun:** I will put it, sir. Usa.

**Andres Urrego:** Yeah, yeah, it's here. Yeah, I got the one that you said that you showed that you also got. Yeah, I saw that one that coming from Moil Partnerships at Moil Lab.com.

**Taiwo Ola Balogun:** Yeah, yeah, yeah, I said I've opened it because, okay, yeah, I just, I just updated the.

**Andres Urrego:** Oh, he did. Okay, got it. Good, good, good.

**Taiwo Ola Balogun:** So, not, yeah, yeah, right.

**Andres Urrego:** Nice, look at that. 623, so six hours ahead. Is that going to show her 623 or is it going to show Central Time, Texas?

**Taiwo Ola Balogun:** Yeah, I think it's good to show our time is good, because the way applications work is like when it comes to time stamp is really, really crazy, so it's eventually it uses everybody's time. I think I think it's uses gadget's time, not just the time being set, so you use the time on your laptop itself. Today, the time is everything is still converted back to. So, sorry, can you log in on your end? I'll check your time. Let me see.

**Andres Urrego:** What do you mean? Ohh, on, on, yeah, yeah.

**Taiwo Ola Balogun:** Yeah, that's a good time.

**Andres Urrego:** 1223, 1153, very good. Okay, good.

**Taiwo Ola Balogun:** Yeah, it's it doesn't show the same time, because it's usually the time on your own and to be able to let it time.

**Andres Urrego:** Anita. Absolutely fantastic. I just wanted to make sure that it wasn't hard-coded, because it can happen, so...

**Taiwo Ola Balogun:** Okay, I think this has been Chris, so... Now, this has been great, so this analytics.

**Andres Urrego:** Awesome. Oh, let me see it, let me see it on Linux. Yeah, much better. You did awesome here, man. Well done. Well done. Can we change that unknown to see as to to like initial upload?

**Taiwo Ola Balogun:** So.

**Andres Urrego:** Go back real quick.

**Taiwo Ola Balogun:** This one for the pipelines.

**Andres Urrego:** Go down, see where it says lead sources. Can we change instead of unknown? Can we do like initial upload? Just call it initial upload. You can probably do that in the data in the database.

**Taiwo Ola Balogun:** Yeah, the thing is, I did, I did, I did think that, I did think that, so I think it was when we uploaded this, so I said, if, if if sources are not defined, you should make it others.

**Andres Urrego:** Right, but in the database, can you go and change that? Right, but in the database, just go and change it instead of unknown, just change it to initial upload, and then everything else from there they can track.

**Taiwo Ola Balogun:** Yeah, it's good to be, it's good to be. I'm good. I will do that. I'll do that. I just filter it. Let me see. I think I filter it because I was like, "Oh, should you because it's like thousands of data, so..."

**Andres Urrego:** Awesome.

**Taiwo Ola Balogun:** But let me see, let me see, I take them a few times.

**Andres Urrego:** All right, you just have to do it. We've only brought in that many people from one list. So you change the name of this unknown category and then make it initial upload list.

**Taiwo Ola Balogun:** Yeah, so another one to say is this, this is the site we input for, and this one has not been updated. This is one that the update is on.

**Andres Urrego:** OK, OK, can we push that out, please?

**Taiwo Ola Balogun:** Yeah, OK, I think you do on the migrations, and let me let me try to push it out now.

**Andres Urrego:** I mean, I did, yeah. I know you can push it out. We still got a couple of hours before I meet with her if you want to make any other changes with the transcript. You know, I think we can.

**Taiwo Ola Balogun:** No, no, I think I think I would like to take the meeting. I will continue to transfer to them.

**Andres Urrego:** Okay, perfect. Good, and that's perfect. That's perfect, 'cause at least I know exactly what I can or cannot show. From the work we did today. Um...

**Taiwo Ola Balogun:** I hope that it's up, so that it's.

**Andres Urrego:** Mm.


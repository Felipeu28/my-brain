---
type: meeting-transcript
source: Microsoft Teams
date: 2026-04-28
ingested: true
ingested_at: 2026-04-28
---

# Teams Transcript — Website Update Review Call (2026-04-28)

**Meeting subject:** Website Update Review Call
**Date:** 2026-04-28 (1:00 PM – 1:58 PM CT)
**Organizer:** Jacob Oluwole
**Attendees present:** Andres Urrego, Jacob Oluwole, Taiwo Ola Balogun
**Invited but did not join:** Linda (`jungleflavorz@gmail.com`)

---

## Context

Originally scheduled to review website work with Linda (jungleflavorz). Linda did not join, so the call became an internal Moil engineering review of multiple parallel client projects: Inna, Connect X (Mark Polanco), Fit Logic, Siren Beauty, and the moilapp.com SEO audit. Andres had a back-to-back at 1:45 with Mark Polanco (organizer of separate transcript), so the last few minutes are him preparing for that hand-off.

## Topics covered

- **Moil website SEO crisis.** Andres ran a full SEO audit on moilapp.com — only ~12 of ~60 pages are indexed, schemas are wrong, robots.txt is wrong. Two years of accumulated SEO debt. Cited as the reason "nobody can ever find us." Anything deployed forward must not repeat this — including client sites.
- **Inna project (CRM dashboard).** Taiwo built it; Jacob is testing as `jacob@mylab.com`. Bugs surfaced live: adding contacts hangs, Gemini API key not working (Taiwo plans to grab the same key used on Fit Logic), screen freezes during demo. Inna messaged Andres saying she's busy → demo pushed back a week, which gives them time to fix.
- **Connect X (Mark Polanco's CRM).** Andres has zero visibility into Taiwo's work because Taiwo moved the repo to "his landing page" and never pushed. With the Mark meeting in 15 minutes, Andres realized he'd be showing the same thing he showed three weeks ago. Pushed firmly: keep repos pushed, work in branches, "I'm never going to push to main but I need visibility." Taiwo committed to pushing.
- **Fit Logic project.** Email editor currently requires HTML; Taiwo wants to replace with a readable WYSIWYG-style editor with variable selector (contacts, email, distance) — same pattern he just implemented for Inna. Plan: deploy Fit Logic tonight (Taiwo stated 10 PM Nigerian time = ~4 PM CT availability; Andres asked him to put it on the calendar instead of always meeting at 10 PM / 2 AM).
- **Siren Beauty brand kit.** Andres received it during the call, forwarded to Taiwo and Jacob, plans to add it as `brand.md` in the project so all future work matches her brand.
- **Operating reality check.** Claude was down (credit reset day); X also briefly down. Andres riffed on $200/mo Claude spend vs. 6 deals closed last month bringing 20× that in pipeline (Siren Beauty paid partial, Connect X to be quarterly).
- **CRM strategy.** Jacob asked why not unify into one CRM. Andres: that's the goal — build several (Inna, Connect X, Fit Logic), learn what works, then consolidate into a white-label product to sell. "Right now nothing works because we haven't finished a single project all the way through the finish line."
- **Outbound messaging.** Andres asked Jacob about messaging the people Andres tagged in the social-media group; nothing sent yet, plan to split the list and send today.

## Key decisions

- **Repo discipline:** Taiwo pushes Connect X work to remote ASAP. All future work pushed for visibility — Andres works on branches, never pushes to main without coordination.
- **Fit Logic ships tonight.** Taiwo to finalize, deploy on Vercel, set environmental variables, test contacts upload + Google account connection.
- **Inna demo slips one week** — Inna unavailable, gives team time to fix the contact-add and Gemini API bugs.
- **Brand kit goes in repo as `brand.md`** so everything Siren Beauty-related stays on-brand.
- **Moil website SEO audit becomes a workstream** — schemas, robots.txt, indexability all need fixing; rule applies to all future client builds too.
- **Multi-CRM → unified product** is the explicit strategy. No premature unification until all three pilots are finished.
- **Calendar etiquette:** Taiwo to put fit-logic test sessions on Andres's calendar rather than waiting on Andres to find time at 10 PM / 2 AM.

## Action items

- **Taiwo:** Push Connect X to remote repo (was working locally only); deploy Fit Logic tonight with env vars; finalize readable editor + variable selector; check Gemini API key on Inna; add Jacob as Google OAuth test user.
- **Jacob:** Send Gmail address to Taiwo for OAuth test-user list; continue social-media outreach plan, share message draft with Andres so they can split the list.
- **Andres:** Add Siren Beauty brand kit to project as `brand.md`; SEO audit + fixes on moilapp.com (60 vs 12 pages indexed, schemas, robots.txt); send Mark a separate site review during 1:45 call; circle back with Taiwo when Fit Logic is on the calendar.

---

## Full transcript

**Jacob Oluwole:** Make me call me.

**Jacob Oluwole:** You know what, that should even upload your own.

**Taiwo Ola Balogun:** Okay.

**Taiwo Ola Balogun:** Hello.

**Andres Urrego:** Yeah.

**Andres Urrego:** Jacob, did Linda accept the meeting?

**Jacob Oluwole:** Yeah, hello. Yes, I sent Linda the meeting. She was part of the...

**Andres Urrego:** But did she accept it? Because if she did, oh she did.

**Jacob Oluwole:** Okay.

**Andres Urrego:** Because if she didn't accept it, then maybe she didn't see it and that's okay, we'll have to reschedule.

**Jacob Oluwole:** She will have to, and she will.

**Jacob Oluwole:** I think it's why I sent her an email telling her that I will send her an invite. She says she'll be available from 12.

**Andres Urrego:** No, I know, but when you send the invite, if she accepted, you get something that says Linda has accepted the meeting or something.

**Jacob Oluwole:** No, I didn't get that. I don't know. I was only in the accepted meeting.

**Andres Urrego:** The.

**Andres Urrego:** Okay.

**Jacob Oluwole:** Most of the time, I never accept your invite, but I have it on my calendar. If you set a meeting, I will have it on your calendar without even you.

**Andres Urrego:** Oh, I see. Okay, got it.

**Andres Urrego:** Shoot, I have another call at 145. Oh my goodness.

**Jacob Oluwole:** On forty-five.

**Andres Urrego:** Oh, that's that with ConnectText. Taiwo, where are we on ConnectText and Inna? Inna is not so well, I'm gonna reschedule Inna for tomorrow.

**Taiwo Ola Balogun:** So I think I painted Connectics just to accomplish Inna.

**Andres Urrego:** What's that?

**Taiwo Ola Balogun:** I paint the work on Connect X to accomplish the Inna.

**Taiwo Ola Balogun:** To accomplish that of Inna.

**Andres Urrego:** Farting.

**Taiwo Ola Balogun:** For is can you ship both to tomorrow if I can do something on the text, but, but you know, you I think we can test in a...

**Andres Urrego:** Ohh.

**Jacob Oluwole:** Yeah, I would love that we test it out.

**Taiwo Ola Balogun:** Let me see something that's.

**Taiwo Ola Balogun:** To that, by tomorrow, we have to test on the text.

**Andres Urrego:** I mean, because ConnectText is working pretty well so far, I think.

**Taiwo Ola Balogun:** It, it, it is.

**Jacob Oluwole:** He he migrated it.

**Taiwo Ola Balogun:** I did like new features to...

**Taiwo Ola Balogun:** Are there new officials to, you know, so I think Jacob should be able to see the new officials, I think. Let's, let's, it's just going to be joining this, this, maybe we can use this call to do this.

**Andres Urrego:** Ohh, nice. OK, good.

**Taiwo Ola Balogun:** Oh.

**Jacob Oluwole:** I think that's good.

**Andres Urrego:** We can use it until until Linda joins because I don't think I don't even know if she's going to join.

**Jacob Oluwole:** Okay.

**Andres Urrego:** We could use a separate call and if she joins, she'll text me or something.

**Jacob Oluwole:** No.

**Jacob Oluwole:** How do we do this, creating two calls, separate codes?

**Taiwo Ola Balogun:** How's that?

**Andres Urrego:** Taiwo, I'm doing a full SEO search on our website because it's really, really bad, by the way. Like we have like 60 pages that should be indexed. We have like 12 pages that should be indexed. Like all of our schemas are wrong. Like all of our like robot dot TXT are wrong. Like.

**Taiwo Ola Balogun:** And.

**Andres Urrego:** Like, there's a lot that, I guess, for the last two years.

**Andres Urrego:** We just haven't done and that's why nobody can ever find us.

**Andres Urrego:** Like, we're literally unfindable. So I got to make sure that anything that we deploy moving forward, that doesn't happen, guys. For other people when we're creating content for other people, because it's really bad.

**Jacob Oluwole:** Yeah.

**Jacob Oluwole:** Good.

**Taiwo Ola Balogun:** Yeah.

**Taiwo Ola Balogun:** I.

**Taiwo Ola Balogun:** I think you sent a document, but I've not been able to like get to it also because I've like a couple things or something doing on my own. I think I saw the document you sent the last time. I saw that.

**Andres Urrego:** Yeah.

**Andres Urrego:** Yeah.

**Taiwo Ola Balogun:** Okay, I think if if I'm able to finish Connect X, because I even on on fixed logic, I found out that I I thought about something that the email edits is currently in it is in HTML and.

**Jacob Oluwole:** Yeah.

**Taiwo Ola Balogun:** I don't think she should be typing HTML on that box, so I decided to do it in readable form.

**Jacob Oluwole:** Exactly, I will.

**Andres Urrego:** Who?

**Andres Urrego:** Ofer Inna.

**Jacob Oluwole:** No, for fit logic.

**Taiwo Ola Balogun:** No, for fit logic, I I implemented it on Inna, so the one I was doing Inna, I thought of fit logic also that, OK, OK, this was actually logic also I did when I was doing it on Inna, then I thought about, OK, yeah, I did this same thing on fit logic and I think I should use on the implementation on that, please, because I implemented it on Inna to be able to use.

**Andres Urrego:** Oh yeah, yeah, yeah, yeah, good, good.

**Andres Urrego:** Of course.

**Jacob Oluwole:** I can do it.

**Taiwo Ola Balogun:** Variables.

**Jacob Oluwole:** Yeah, continue talking if you don't.

**Taiwo Ola Balogun:** To be able to use variables, to be able to use, is gonna she be able to select variables on the edits on the editor, like the variables that she needs, like contacts, email, distance, she be able to select it herself and she be able to type each of our like write HTML, she's going to be just be typing like normal.

**Taiwo Ola Balogun:** On my readable form, like she's typing to, and it has like the bold italics and all these things is there, so I should be able to do that.

**Taiwo Ola Balogun:** So, I think that is what I I did on that end, so I'm going to replicate it for fixed logic.

**Andres Urrego:** Okay, perfect. I love it. I love it.

**Jacob Oluwole:** Mm.

**Taiwo Ola Balogun:** Okay, um, I think...

**Taiwo Ola Balogun:** In this.

**Jacob Oluwole:** Yeah.

**Jacob Oluwole:** Ohh my God, nice. Can we? I don't think this is almost...

**Taiwo Ola Balogun:** I'm done.

**Taiwo Ola Balogun:** Five.

**Jacob Oluwole:** Ten minutes after.

**Taiwo Ola Balogun:** Ohh, I miss you for that.

**Andres Urrego:** Jacob, this is your client. Stop it.

**Jacob Oluwole:** Seven after.

**Taiwo Ola Balogun:** I would say this.

**Andres Urrego:** We'll just stay on here while we while we work on it. If he doesn't show up, that's OK. Uh, so this with now it needs to be done there, import.

**Jacob Oluwole:** Yeah.

**Taiwo Ola Balogun:** Okay.

**Taiwo Ola Balogun:** I have like 2 friends with that, yes, I drink.

**Jacob Oluwole:** Yeah.

**Jacob Oluwole:** Right.

**Taiwo Ola Balogun:** Hey Cortana.

**Taiwo Ola Balogun:** No, no.

**Taiwo Ola Balogun:** Oh.

**Taiwo Ola Balogun:** Like.

**Andres Urrego:** Ohh.

**Taiwo Ola Balogun:** Ohh.

**Andres Urrego:** What, what, okay, what else do you need, uh, Taiwo?

**Taiwo Ola Balogun:** Okay, yeah, I think I'm going to be needing for feed logic. So I'll be able to deploy everything on feed logic this night. I'm going to be needing Vasil. Also, I'm going to be there for myself.

**Taiwo Ola Balogun:** Vasil, I think, so we'll be available, we'll be available.

**Taiwo Ola Balogun:** We'll be available 10 P.m. your time, so I'll be able to like finalize speech logic this night.

**Andres Urrego:** Five o'clock my time.

**Taiwo Ola Balogun:** I, I, I want to, I want to like really do some things on this logic, test them out, and push the updates. Now, when I push the updates, then the next thing is to deploy on our cell and add the environmental variables and check it out. I, when I deploy myself, be able to upload that, that's...

**Taiwo Ola Balogun:** Contact file.

**Taiwo Ola Balogun:** Then, on to the contact file, you be able to, like, connect our Google accounts to it, so I want us to like only draw this.

**Jacob Oluwole:** He's talking about for 10 P.m. your time. That's for him.

**Jacob Oluwole:** Tomorrow morning.

**Taiwo Ola Balogun:** Oh, that's for you. No, no, she he has a meeting tomorrow, so you have to like do it today and like probably just to be testing tomorrow. We have to set it up.

**Jacob Oluwole:** So when you say 10pm, what do you mean? Is it 10pm Nigerian time?

**Taiwo Ola Balogun:** S.

**Jacob Oluwole:** When you say 10pm.

**Taiwo Ola Balogun:** OK, let me see. Let me, OK, you know what, Andres, are you going to be available in the next three hours?

**Andres Urrego:** Yeah, it should be a level.

**Andres Urrego:** Yeah.

**Taiwo Ola Balogun:** Okay.

**Taiwo Ola Balogun:** If you are going to go in next hours, I think.

**Taiwo Ola Balogun:** You can make this work, so that I'll be able to.

**Taiwo Ola Balogun:** Finalize Office Logic.

**Andres Urrego:** Hi, I'm doing an as I'm doing a full analysis on Connect X so that we can import all of these documents from our table.

**Taiwo Ola Balogun:** Okay, I'm sorry, those connected with the integrations also.

**Taiwo Ola Balogun:** Are they going to be using calendar, um, Gmail?

**Andres Urrego:** Yeah, we'll need to, we'll need to do that for him, yes.

**Taiwo Ola Balogun:** K.

**Taiwo Ola Balogun:** Hi.

**Taiwo Ola Balogun:** Alright.

**Andres Urrego:** Interesting.

**Andres Urrego:** Slow down or something?

**Andres Urrego:** Cool.

**Andres Urrego:** Interesting.

**Andres Urrego:** Yeah, Claude is down.

**Andres Urrego:** What is down, down, down?

**Andres Urrego:** Man down, man down.

**Taiwo Ola Balogun:** Clot is down.

**Andres Urrego:** Yeah.

**Jacob Oluwole:** Haha.

**Jacob Oluwole:** Alright, can we? I think we've it's 15 minutes already, so let me just let's share, let's do this thing now together. Let's do this in hours.

**Jacob Oluwole:** Together, together, what happened? I got you back.

**Taiwo Ola Balogun:** Play.

**Jacob Oluwole:** I was, I was taking, I was taking notes of some.

**Andres Urrego:** You guys have no idea how happy it makes me when you guys sing.

**Jacob Oluwole:** Ohh.

**Andres Urrego:** Like, when everybody's anybody sings, you know what I mean, that makes me happy, like...

**Andres Urrego:** People sing when they feel good.

**Jacob Oluwole:** Yeah.

**Taiwo Ola Balogun:** Haha.

**Jacob Oluwole:** Yeah, you're right.

**Andres Urrego:** Oh shoot, Taiwo. Later on this week. Oh my god, let me send this over to, well actually I can probably work on this. So, Siren Beauty, she sent me her...

**Andres Urrego:** Her brand kit, so let me, I'm gonna forward this to you, Taiwo.

**Andres Urrego:** And Jacob, I want to copy you both on it because we need to add that that branding kit soon to the website. Actually, I'm going to do just that right now.

**Andres Urrego:** I want to download it.

**Jacob Oluwole:** I'm fine, you know.

**Jacob Oluwole:** See, I am visiting the liquids.

**Andres Urrego:** Good, so now I got her brand kit.

**Jacob Oluwole:** Hello.

**Andres Urrego:** I got a full brand kit, so I'm just going to add it to our project. Ask it to create a brand.md.

**Andres Urrego:** And then that way, everything from now on will be completely in line with her business.

**Andres Urrego:** How about that, guys? How about that?

**Andres Urrego:** Oh no, cloud is like completely down. Holy macaroon.

**Andres Urrego:** Moil.

**Jacob Oluwole:** You guys, you know, a lot of traffic have been flooding.

**Andres Urrego:** X was down just a few minutes ago too though.

**Jacob Oluwole:** You.

**Jacob Oluwole:** Ohh, what's happening to the internet?

**Andres Urrego:** I don't know, yeah, exactly.

**Andres Urrego:** Well.

**Jacob Oluwole:** Okay, Taiwo, this is it. Do you want to share your screen or what?

**Andres Urrego:** For what project?

**Jacob Oluwole:** This is Inna, this is Inna project.

**Taiwo Ola Balogun:** OK, for Inna for Gemini is not working, something to I did grab the key that we used on phys logic to that, so I want to fully check that and make sure that it makes work.

**Taiwo Ola Balogun:** The Gemini is not working because of the API key.

**Taiwo Ola Balogun:** I was like, give me like a couple minutes and I'll be able to like notify you.

**Andres Urrego:** Yeah, yeah.

**Jacob Oluwole:** No, thanks.

**Andres Urrego:** What I love about Claude going down is that they reset the credits, so then...

**Jacob Oluwole:** Yeah.

**Jacob Oluwole:** Yeah.

**Jacob Oluwole:** That's my boss.

**Andres Urrego:** Every time they're...

**Andres Urrego:** Every time they go down, dude, like sometimes I get really nervous. Like I start freaking out when like you should see like if they, for example, if they renew on Thursday, on Wednesday, I'm like nonstop. Like starting Tuesday, I'm like, I'm going to use all the credits. I'm not going to let anything go to waste. So then I have like 12 projects running at once. Everything starts failing, then it goes again. Yeah.

**Andres Urrego:** Yeah, I'm gonna give him none of my credits. 200 bucks a month, man.

**Jacob Oluwole:** Trying to box, I mean, that's that's.

**Andres Urrego:** But.

**Andres Urrego:** Two 100 bucks a month, but we literally closed 6 deals last six deals last month.

**Andres Urrego:** That literally brought us 20 times that. Well, they haven't paid, but they will, right? Like all these things that we're working on, they're still to be paid, but we have the deals closed, right? So I think the only one that paid us, some of it was Siren Beauty. Now we got the rest of them with ConnectX. We're going to break that down on quarterly payments. He's going to give us a payment up front.

**Andres Urrego:** Yeah, I mean, all of these little projects, 500 here, like just a simple website. We'll charge 5, 600 bucks, and it cost us $200 to do a, you know, to pay this for an entire month. And we literally got four people working off of it right now. We're doing marketing, video, we're doing code, we're doing everything.

**Jacob Oluwole:** Mhm.

**Andres Urrego:** I love that Atlas was impressed.

**Andres Urrego:** with the images from last night.

**Jacob Oluwole:** The image is very nice, very, very nice.

**Andres Urrego:** Isn't that crazy?

**Andres Urrego:** What I think is crazy is that a week ago we didn't even know we could do that.

**Jacob Oluwole:** Mm.

**Andres Urrego:** That's why I love working on my side projects, like my own side projects. Like for example, Clio, right? I mean, that was just great for me because it helped me do a lot of the stuff that we're doing now. Like with Clio and my brain.

**Andres Urrego:** We have incorporated half of those things into Moil already, or we're in the process of.

**Andres Urrego:** Like those emails that we're getting on Mondays, like I, I, that's that's game changing to me.

**Andres Urrego:** Like from a, from a come back to the side perspective, oh my god, it's perfect.

**Jacob Oluwole:** All right, yeah, let's talk about this Inna dashboard that Taiwo worked on.

**Jacob Oluwole:** So, I've logged in, I logged in with my account, Jacob at mylab.com, so I'm logged in as this.

**Jacob Oluwole:** So, this is the, this is the dashboard.

**Jacob Oluwole:** Can I see if I can, can I spot you?

**Jacob Oluwole:** I don't think so. Can I do something? This thing working? This button is working.

**Andres Urrego:** Are you sharing your screen?

**Jacob Oluwole:** Yes, I'm sure.

**Andres Urrego:** Oh yeah, I see it. I see it. Jacob, why did you think about that PowerPoint we created today? Wasn't that good?

**Jacob Oluwole:** It was good, it was good. I love it.

**Andres Urrego:** Man, I was so shocked by that PowerPoint. I was like, hell yeah, I mean, I'm so glad. I mean, again, most people, it will take him a long time to even try to figure it out, you know?

**Jacob Oluwole:** Mhm.

**Jacob Oluwole:** All right, so yeah, this is it. Are these buttons supposed to be working?

**Andres Urrego:** Right, cool. So what's working and what's not working on here?

**Jacob Oluwole:** And this is supposed to be working; I'm not getting any anything from them.

**Jacob Oluwole:** So, going to add contacts, I tried adding my contacts, it was not adding. I wrote it down on my bug list.

**Jacob Oluwole:** Yeah.

**Jacob Oluwole:** Stand my lag again.

**Taiwo Ola Balogun:** Urrego, you are unable to add contacts.

**Jacob Oluwole:** Yeah, my name is...

**Taiwo Ola Balogun:** Okay, try, let me see, let me see.

**Jacob Oluwole:** My system has stopped moving. It's hanging. Well done.

**Jacob Oluwole:** I guess.

**Jacob Oluwole:** Sorry.

**Jacob Oluwole:** Is this showing that my mouse is moving around?

**Andres Urrego:** Noah.

**Taiwo Ola Balogun:** Yeah, yeah, yeah, mostly.

**Jacob Oluwole:** Well, he's hanging here, I can't even see.

**Andres Urrego:** Oh, it is. I didn't see it.

**Jacob Oluwole:** I can't see this working yet.

**Jacob Oluwole:** Wow.

**Jacob Oluwole:** I don't know, uh, it's making me...

**Andres Urrego:** Yeah.

**Jacob Oluwole:** Okay, he's back. Yeah, I can see now.

**Jacob Oluwole:** Took a leaf.

**Jacob Oluwole:** It's happening again.

**Jacob Oluwole:** My God, what's happening?

**Andres Urrego:** So, not working at all? Good thing is, I, I...

**Taiwo Ola Balogun:** I can see, I can see your, I can see your contacts.

**Jacob Oluwole:** Okay, it's working now.

**Jacob Oluwole:** I can't see at some point. I can only able to see my mouse moving around, so just and to just stop working. It has happened again. I was just typing.

**Jacob Oluwole:** Trying to lose weights.

**Andres Urrego:** It.

**Jacob Oluwole:** Chidish me.

**Jacob Oluwole:** That's fine.

**Andres Urrego:** Don't.

**Andres Urrego:** No.

**Jacob Oluwole:** Happens.

**Andres Urrego:** You're working on Connect X website from Felipe U28, right?

**Andres Urrego:** Taiwo.

**Taiwo Ola Balogun:** No, I moved it. I moved it to my landing page, but I don't think I've pushed it.

**Andres Urrego:** Where?

**Andres Urrego:** Oh, you haven't pushed it?

**Taiwo Ola Balogun:** Yes, yes, I haven't pulled it. Jacob, Jacob, can we do something for us? Do you have a Gmail you can connect with this?

**Jacob Oluwole:** Yeah.

**Jacob Oluwole:** Yeah, I have a Gmail I can connect. You told me to connect something, bro.

**Taiwo Ola Balogun:** Okay, send me, send me the mail, send me the mail, send me the mail. Let me add it to test results.

**Jacob Oluwole:** What mail do you username and password?

**Taiwo Ola Balogun:** Yeah, yeah, let me add the test results.

**Jacob Oluwole:** So when he said, when he told me to connect my email, I was on the page. I was trying to look for a way to connect my user, my email. I couldn't find it. I was like,

**Taiwo Ola Balogun:** Go to Settings, Settings.

**Jacob Oluwole:** Are we supposed to do that?

**Jacob Oluwole:** Yeah, I'm coming.

**Andres Urrego:** Okay, all right, Taiwo, can you push them? Can you keep them pushed just so I have visibility on them, please? Because if you work everything local, I mean, even if it's broken, that's okay. Just whatever. Let's just push them because I want to keep my eyes on them. I don't want to, I don't want to.

**Taiwo Ola Balogun:** Hello?

**Andres Urrego:** Uh-huh.

**Taiwo Ola Balogun:** Okay, I think it's the last.

**Taiwo Ola Balogun:** I think that's what you said last.

**Andres Urrego:** Oh, that can you please just keep the repo like updated just so that whenever I'm working on them, I can just at least, I'm never going to push to main, but I'll work off of branches. If I don't know what you've worked on, I have no visibility and then I'm just kind of running off of.

**Andres Urrego:** Outdated things.

**Taiwo Ola Balogun:** OK, what should I do, sir?

**Andres Urrego:** Just push it, push it to push it to the new repo, because the repo that you moved it to is empty.

**Taiwo Ola Balogun:** I'm going to push it. I'm going to push it.

**Andres Urrego:** So like if you push it to the repo, keep it there.

**Andres Urrego:** And then that way when I'm working up, oh, go ahead.

**Taiwo Ola Balogun:** Okay, okay, so you know what we can do, you know, you know what we can do?

**Taiwo Ola Balogun:** Um, you can, you can delete that repo that I created, then transfer what you have on your own to the my landing page.

**Andres Urrego:** Well, no, because I don't have it. It's not updated. That's the problem.

**Taiwo Ola Balogun:** Sir.

**Andres Urrego:** It's not updated, that's the problem.

**Andres Urrego:** So, you make changes to connect text. Why would I why would I clone what I have if you've already made changes to it? Why would I work off of an outdated repo?

**Taiwo Ola Balogun:** I, I know, I know.

**Taiwo Ola Balogun:** Okay, Sir.

**Andres Urrego:** Does that make sense, like?

**Jacob Oluwole:** I got this.

**Taiwo Ola Balogun:** Yeah, it makes sense.

**Jacob Oluwole:** No, please can you share your screen on?

**Andres Urrego:** Like if you're making changes of it, and then I go and try and make changes, I'm going to make changes to a completely different repo than the one you're working on. And if you keep it on your computer and I have no visibility on it, then I have no way of working on it. I'm not going to work on your main, I'll work off of the branches, but I need visibility.

**Jacob Oluwole:** Yeah, Andres, I my my my my system has my PC has stopped responding, so I have to first shut it down. I have shut it down and.

**Taiwo Ola Balogun:** Okay, sir, okay, sir.

**Jacob Oluwole:** I will, I will connect again, maybe Taiwo can.

**Jacob Oluwole:** Share screen.

**Andres Urrego:** Well, I have the meeting with Mark in 15 minutes. I just don't even know.

**Jacob Oluwole:** Oh, okay, I will test with time with it, and I will test with time with it.

**Andres Urrego:** I.

**Jacob Oluwole:** Ohh, OK. Yeah, trying to resolve the phonetics issue before the meeting.

**Andres Urrego:** What's that? Well, no, I'm trying to, I was trying to figure out what I'm going to show Mark, but I don't have any visibility into my repo that I'm supposed to show Mark. So anything that Taiwo has done, I can't even show him. So I'm about to jump into a meeting and show him the same thing I showed him three weeks ago.

**Jacob Oluwole:** I can't present that, Mark. OK.

**Jacob Oluwole:** Yeah, yeah.

**Andres Urrego:** So that makes no sense, guys. Makes literally, absolutely no sense whatsoever.

**Jacob Oluwole:** Noah.

**Andres Urrego:** I don't understand how we do business sometimes.

**Andres Urrego:** So I guess I didn't know this until now. So now I have my meeting with him in 15 minutes and I'm going to literally show him the same thing I showed him a while back, even though I just told him that we were going to give him an update today after two weeks or three weeks of the last meeting I had with Mark.

**Taiwo Ola Balogun:** So I think sometimes I really don't know your calendar. What I thought you actually was Inna.

**Andres Urrego:** Well...

**Taiwo Ola Balogun:** I think that you have connected me to be also.

**Andres Urrego:** I, I was, I was very clear, Taiwo. I was very clear and I said, we need to move on all of them.

**Andres Urrego:** They're all active projects. They're all people that are going to pay us. The sooner we finish them, the sooner we can be done.

**Andres Urrego:** But again, you have worked on ConnectX and you just kept it on your computer. There's no visibility for me.

**Taiwo Ola Balogun:** Um, the work I've done on PhonetX also has not been like, has not been...

**Taiwo Ola Balogun:** Really, really, really progressive that much, as I've done with Inna.

**Taiwo Ola Balogun:** So, because throughout the weekend, it was in our work done, not connect X.

**Andres Urrego:** Yeah.

**Taiwo Ola Balogun:** So, if I knew that the meeting was also like the same day with Inna, I would have tried to like at least push some changes and make sure that it's not same thing, but I didn't know that it was actually like same day. I did not, I thought you were only having Inna today.

**Andres Urrego:** Rev is a project that's been open for three weeks now. I mean, I think I handed it over to you guys a week and a half ago.

**Andres Urrego:** Yeah.

**Jacob Oluwole:** He said he said they contact us.

**Jacob Oluwole:** Is.

**Jacob Oluwole:** Quankly.

**Jacob Oluwole:** in the database, the client report, I can't find it here, I can't see it here. So that was the reason why I thought it was not adding new contacts.

**Jacob Oluwole:** You, you see the book.

**Jacob Oluwole:** Mm.

**Taiwo Ola Balogun:** Let me see.

**Andres Urrego:** Please say no.

**Taiwo Ola Balogun:** Yes.

**Andres Urrego:** Um...

**Andres Urrego:** Okay, alright, so I got it here.

**Andres Urrego:** Hopefully I can work on this before he joins. Now let's work.

**Jacob Oluwole:** Sing.

**Jacob Oluwole:** Client contact with the email addresses.

**Taiwo Ola Balogun:** Yeah, I said there were some, I saw your contacts already on it.

**Jacob Oluwole:** Perfect.

**Taiwo Ola Balogun:** Can you please be fresh?

**Jacob Oluwole:** I'll be refreshing.

**Andres Urrego:** On Taiwo, now we have the meeting with, so, so is bit logic good to go for tomorrow?

**Taiwo Ola Balogun:** No, that's the reason why I said we need to work on getting feed logic sets tomorrow, so we don't have this type of issue. We need to work on getting feed logic sets like today.

**Taiwo Ola Balogun:** Because speed logic is not set to go tomorrow, but if we work on it today, we'll be able to get set for tomorrow and should be able to like.

**Andres Urrego:** And.

**Taiwo Ola Balogun:** So, do you have, like, do you have time to be so be able to still go over fit logic?

**Andres Urrego:** Yeah, just let me know when, man. Put it on my calendar. That's what I always tell you. Look at my calendar, put it on my calendar. Don't make me guess. Don't make me wait till 10 P.m. when you're available. Because I'm very flexible, Taiwo. But being flexible needs to mean that we meet in the middle. We can't, I can't always meet you.

**Andres Urrego:** 2 AM or 11 PM or 10 PM, right? So I know you say, well, I don't know your availability. I mean, you guys can see my calendar. So just put it on my calendar, ask Jacob, whatever. Don't wait for it is what I'm saying. Because I don't like, I don't like getting to day of delivery and then hearing, well, it's your fault because you don't have any time to meet.

**Jacob Oluwole:** Yeah.

**Andres Urrego:** I prefer, I mean, whatever it is that we need to get done. I thought everything you had asked me for this week, I had delivered to you. I apologize for what I missed.

**Taiwo Ola Balogun:** No problem, sir. Jacob, I think, let me quickly add you to it, so you be able to connect your Google account to that.

**Andres Urrego:** Say that again.

**Taiwo Ola Balogun:** No, I want to add Jacob as a test user.

**Andres Urrego:** Oh yeah, yeah, for sure, for sure. Yes, that's the number one thing we gotta figure in.

**Andres Urrego:** Okay, Inna is gonna be another week, so we got some time there. I just, I just mess, she just messaged me. She says she's gonna be busy.

**Andres Urrego:** So that gives us time to actually get this right, guys.

**Jacob Oluwole:** Yeah.

**Jacob Oluwole:** And yes, I was wanting to say something before I wanted to say something. Is there with I can see connection between all the CRM that I'll be working on and I'll.

**Andres Urrego:** But again.

**Taiwo Ola Balogun:** Okay.

**Jacob Oluwole:** Thinking about it, why can't we have like a unified CRM where I will get charged?

**Andres Urrego:** Well, we will, we will. That's why we're building this project. So soon we will. That's the entire goal, right? We start, we figure out which one is the best one, and then the next person that asks us for a CRM, I'm actually going to do an analysis once we have this ready. But what are we doing right now, Jacob, is we're learning how to

**Jacob Oluwole:** Bye-bye.

**Andres Urrego:** how to build them, what's the right one we should build, right? So this is all of us, this is us testing so that once we get in, we can't go and unify anything until we know what works. Right now, nothing works, right? And I don't mean that in a mean way, I just mean nothing works.

**Jacob Oluwole:** Noah.

**Andres Urrego:** Right, why? Because we haven't finished a single project all the way through the finish line.

**Andres Urrego:** Once we finish all three of these and we're like, wow, these are amazing, or this one is the best one, I'll do a full repo look and then say, all right, from all of our CRMs, build the best one and let's deploy it. Now that one, we're going to go out and sell to multiple businesses. Ready to move over to your own CRM messages. Boom, we white label the **** out of it and then sell it.

**Andres Urrego:** But we got to learn how to do it right first because we've never built CRNs before, right?

**Jacob Oluwole:** Yeah.

**Jacob Oluwole:** Nice.

**Andres Urrego:** I always tell you guys, there's...

**Andres Urrego:** Um...

**Andres Urrego:** There's a science to my madness, I promise. Sometimes it's not very clear right off the bat.

**Taiwo Ola Balogun:** Jacob, can you connect your milk?

**Jacob Oluwole:** Uh, where, where is where can I do that?

**Taiwo Ola Balogun:** Go down, scroll down the sidebar, then go to settings integration.

**Jacob Oluwole:** Okay.

**Jacob Oluwole:** Why is this? I don't like the way this is. Yeah.

**Jacob Oluwole:** I look, I fight here because I have to scroll down, down, down, down. It's taking, it's taking some space.

**Taiwo Ola Balogun:** You know, you know, you know it's actually your is actually your screen on most people's screen is is just I've never actually this does not even happen in my end. It's because your screen is very, very small. You are using HP, so it's only very, very small. When I was using the same, it's always like my screen is always very, very small, so...

**Jacob Oluwole:** And.

**Jacob Oluwole:** He is me.

**Taiwo Ola Balogun:** The height of your screen is the problem is, I think, 568 pixels.

**Jacob Oluwole:** Okay.

**Jacob Oluwole:** Alright, son.

**Taiwo Ola Balogun:** But Ivander is actually shakes it. It's good to see that it's like there's even like spaces in between them.

**Jacob Oluwole:** That's not judged by my, so I can I can connect with this one.

**Taiwo Ola Balogun:** No, no, the one you sent to me, the one you sent to me.

**Jacob Oluwole:** I got that.

**Jacob Oluwole:** So, what is that what is not telling me to do here?

**Taiwo Ola Balogun:** You want to connect a Google account? I need to add you as a test user, so you sent one to me. You can send this one to me. You can send this one to me.

**Jacob Oluwole:** Yeah.

**Taiwo Ola Balogun:** If this is what you want to connect, you need to send it to me to add it as a test, unless you not be able to connect this thing development.

**Jacob Oluwole:** OK, let me, let me, let me.

**Jacob Oluwole:** And we can answer to this one.

**Taiwo Ola Balogun:** You can actually send this on to me, so I need to add this on.

**Jacob Oluwole:** Hello!

**Jacob Oluwole:** It's me.

**Jacob Oluwole:** I was wrong.

**Jacob Oluwole:** You.

**Andres Urrego:** Jacob, I think I'm going to start messaging people today on the stuff that I told you about yesterday. Did we message anybody today?

**Taiwo Ola Balogun:** I.

**Jacob Oluwole:** No, I'm not started. I was gonna start after I'm done with this, when I go on social media, I'm not done.

**Andres Urrego:** Okay, okay, no, no a big deal. Send me the message you're going to send and then let's split the ones we're going to send.

**Jacob Oluwole:** I was, I plan on doing what you...

**Andres Urrego:** Gone.

**Jacob Oluwole:** I, I don't know doing what you sent to me, like the people that you just tagged that you tagged to when they when they just...

**Andres Urrego:** Jacob, any in that group every day, I, there's an automatic post that says welcome people.

**Jacob Oluwole:** Okay, yeah, okay, so.

**Andres Urrego:** If you go past, if you go back to the last 10.

**Jacob Oluwole:** Okay.

**Andres Urrego:** you'll find at least 300 people you can message. Because it is triggered after 25 people join, sometimes it's 40.

**Jacob Oluwole:** All right.

**Jacob Oluwole:** Okay.

**Andres Urrego:** So if you literally search at the top of the group in the little search magnet thingy, and you search new members or whatever the heck the email says, you'll probably get all those. And then you go one by one. So that's what I was saying. We can split it, but it's very simple. We click on one by one, send them a DM, one by one, send them a DM, one by one, send them at the DM.

**Jacob Oluwole:** Okay, well, I have a...

**Jacob Oluwole:** Okay, I will check it out. I will check it out.

**Jacob Oluwole:** Facebook, Jane.

**Jacob Oluwole:** Alone.

**Jacob Oluwole:** So, am I using these established biometric link? Am I using this button?

**Taiwo Ola Balogun:** Yes, yes, yeah, using that.

**Jacob Oluwole:** So I can't connect like directly like this. I have to connect from the backend then do this.

**Taiwo Ola Balogun:** The thing is, I'm authenticating you, continue, continue, but continue on back to city, continue, check, check calendar, check, yeah, I will ask you something to share, so share calendar and everything. Ohh yeah, you pressed continue already.

**Taiwo Ola Balogun:** You have to go on duty again.

**Jacob Oluwole:** What?

**Jacob Oluwole:** Send me on my behalf, on your behalf, yeah?

**Taiwo Ola Balogun:** Yeah.

**Jacob Oluwole:** Very nice.

**Jacob Oluwole:** Site cannot be reached, look out, think that look out.

**Taiwo Ola Balogun:** I will call back.

**Taiwo Ola Balogun:** Ohh, okay, let me let me show you that.

**Andres Urrego:** Okay, so guys, I want you guys to process this. So, YC just came out and in my application to YC was very cool because my application in YC, I positioned Moil as a...

**Andres Urrego:** As if we were preparing for a Gentic AI to make all of our data available to agents.

**Andres Urrego:** And yesterday they published like the request for startups. So it's like it's called an RFS and they do a request for startups meaning.

**Taiwo Ola Balogun:** Yeah, I saw that.

**Andres Urrego:** Yeah, and one of them is startups that will, like literally startups that make, that are building to make information available for agents. So startups that work for agents, you don't build the agent, you work a startup, you build a startup that works for agents. So if we can become, you know, the small business

**Andres Urrego:** agentic place, we have our own little agentic tools, but at the end of the day is allowing people to set up their agents and consumer data because we have it all.

**Jacob Oluwole:** That's very nice, very, very nice to hear, honestly.

**Andres Urrego:** Yeah, because look, we have all the data, right? I mean, that's what I always tell people is like, what makes us different from anyone else is that literally, once we upgrade the entire flow of the 21 questions, and it doesn't feel like 21 questions, it's more like a chat.

**Jacob Oluwole:** Honestly, yes.

**Andres Urrego:** Then from there on, I mean, it's game over. I mean, it's game over because at that point, you know, it becomes very easy to use. And from day one, we've already built what other like open AI is not doing, which is we have your context.

**Andres Urrego:** We have the data in here. We build your brand DNA, which I was working on Steve earlier too. We're going to, so the way we're going to start treating this Taiwan Jacob is we're going to start creating MD files for each profile. You're going to have your user MD file. You're going to have your design MD file. You're going to have your, you know, agent MD file.

**Jacob Oluwole:** Mm.

**Andres Urrego:** And all of those little things that we're going to create that don't take a lot of space is what is going to allow us to be open for any agent to be able to come into Moil. For someone to say, hey, tell their agent, go to Moil.

**Andres Urrego:** and then get everything I need, creative, you know, whatever.

**Jacob Oluwole:** Yeah.

**Andres Urrego:** So, yeah.

**Jacob Oluwole:** be nice, that would be nice, that would be nice, that would be nice, that would be nice. Hundred percent. So, on this part, I also saw you said schedule appointment. I don't know if this is working already.

**Jacob Oluwole:** Um, that will.

**Taiwo Ola Balogun:** Ohh.

**Jacob Oluwole:** I don't know if this is working. Appointments. Is this feature working already?

**Taiwo Ola Balogun:** Yes, this is working, and I'm just supposed to be like a minute. Let me try to update this.

**Jacob Oluwole:** I don't think so.

**Taiwo Ola Balogun:** It's.

**Jacob Oluwole:** Ohh my God, God!

**Jacob Oluwole:** Thank you, Jesus.

**Taiwo Ola Balogun:** Yeah.

**Jacob Oluwole:** What? What's up?

**Taiwo Ola Balogun:** No, no, I just noticed something. So I think on Vasel, I noticed that now you also edit your environmental variables. They don't show you the previous ones. I think probably for security, they don't show you the previous ones anymore.

**Jacob Oluwole:** Yeah, so, what do what we are on, what work, what we are on that?

**Taiwo Ola Balogun:** He'll ask me to play.

**Taiwo Ola Balogun:** No, this is no, it's just like it's going to measure that I just implemented.

**Jacob Oluwole:** Okay.

**Taiwo Ola Balogun:** People.

**Andres Urrego:** Ohh my god, Mark is waiting for me, probably.

**Taiwo Ola Balogun:** Okay, but...

**Taiwo Ola Balogun:** OK, Jacob, I think I'll try it again.

**Taiwo Ola Balogun:** E.

**Taiwo Ola Balogun:** No problem, I think try try to connect it again, reload it and try to connect it again.

**Taiwo Ola Balogun:** Hello?

**Andres Urrego:** Yeah.

**Jacob Oluwole:** Thank you, James.

**Taiwo Ola Balogun:** Jacob.

**Jacob Oluwole:** Yeah, what's up? I shared the connection again.

**Taiwo Ola Balogun:** I said, yeah, yeah, can I turn the connection again?

**Jacob Oluwole:** Ohh my God.

**Jacob Oluwole:** Mm.

**Jacob Oluwole:** Jesus.

**Andres Urrego:** Hi guys, I gotta let you go. Let me know how it goes. I'm gonna join with Mark real quick and see what we can do. So I'll keep you posted, okay?

**Taiwo Ola Balogun:** Okay, sir.

**Andres Urrego:** Thank you, but this was a big one, so let's finish this one up soon.

**Jacob Oluwole:** Alright, boy, alright, boss.

**Andres Urrego:** Talk to you guys in a bit. Thank you. Well done. Bye bye. Let me know, Taiwo, when we're going to meet.

**Taiwo Ola Balogun:** So, I'll be good.

**Taiwo Ola Balogun:** Okay, so good to have you.

**Andres Urrego:** Thank you.

**Jacob Oluwole:** Please, just stand in the meeting, just can, yeah, now the next.

**Taiwo Ola Balogun:** Okay, so let's talk, so let's talk.

**Jacob Oluwole:** Oh, everything is connected.

**Taiwo Ola Balogun:** Okay, let me, let me share my screen with you now.

**Jacob Oluwole:** Connected.

**Jacob Oluwole:** All right, bye.

**Jacob Oluwole:** Ohh.

**Taiwo Ola Balogun:** OK, this is my screen off.

**Taiwo Ola Balogun:** Hey, let me delete this, so you're going to get your inbox.

**Jacob Oluwole:** Did you get my? Did you receive any of my email? I sent an email to you.

**Taiwo Ola Balogun:** No, um, right now, right now, um, what I'm trying to deny is, so...

**Jacob Oluwole:** I guessing.

**Taiwo Ola Balogun:** I'm trying to clear my the database for previous emails on my own end, because I contacted mine when I was testing it, so I'm trying to remove them.

**Taiwo Ola Balogun:** I just want you on.

**Taiwo Ola Balogun:** Ones.

**Taiwo Ola Balogun:** Thanks, nice.

**Taiwo Ola Balogun:** Thanks, mate.

**Jacob Oluwole:** I should practice more with this transcript.

**Taiwo Ola Balogun:** Okay.

**Taiwo Ola Balogun:** Let me try, let me try this now.

**Taiwo Ola Balogun:** This.

**Jacob Oluwole:** There was a time.

**Jacob Oluwole:** In.

**Jacob Oluwole:** Buddha, Texas.

**Jacob Oluwole:** To the sirene environment.

**Taiwo Ola Balogun:** Yeah.

**Taiwo Ola Balogun:** Ah, I didn't see your integration. I meant to be seeing the integration here.

**Taiwo Ola Balogun:** I should connect it right.

**Jacob Oluwole:** Yeah.

**Jacob Oluwole:** Should be connected now. I think same thing is also happening to Andres when when he logged into when he logs into partners.mailer.com.

**Jacob Oluwole:** is seeing a completely brand new license list. As you've been seeing what I've done so far, everybody with that more like I should be saying it.

**Jacob Oluwole:** And that's still something we need to work on.

**Taiwo Ola Balogun:** Because I was like sincerely connected with yours.

**Taiwo Ola Balogun:** Meant to be saying it's...

**Jacob Oluwole:** Let me check it out again.

**Jacob Oluwole:** Yeah, this.

**Jacob Oluwole:** So, my inbox, let me check my inbox. So, no inbox so far, let me sync.

**Jacob Oluwole:** My God, so.

**Jacob Oluwole:** Why is it using hash hash encoded messages hash 39 stuff like that are not showing the the weights being?

**Jacob Oluwole:** The white, white spacing, and...

**Jacob Oluwole:** Is being exact way it's being sent?

**Jacob Oluwole:** White spacing on these, all these emoji encoded messages. Yeah, let me see, share encoded messages.

**Taiwo Ola Balogun:** Ohh, yeah.

**Jacob Oluwole:** Ohh, I wish I was sharing my screen.

**Jacob Oluwole:** And I opened my email, one of the inboxes, one of the messages I got.

**Taiwo Ola Balogun:** Let me see your screen there.

**Taiwo Ola Balogun:** Jacob, my phone is position of amount, so I have to end this early.

**Taiwo Ola Balogun:** But I'm going to like all these two, but let me see, let me see the message.

**Jacob Oluwole:** Oh, no, no, I'm tired, much tired, but tired, man. See, this is what I'm talking about.

**Jacob Oluwole:** No, he's not giving the white label the.

**Taiwo Ola Balogun:** Oh, it's showing it's showing the code.

**Jacob Oluwole:** Mm.

**Taiwo Ola Balogun:** Those special characters are represented in code.

**Jacob Oluwole:** He.

**Taiwo Ola Balogun:** OK, can you just like document that of seven then?

**Jacob Oluwole:** Is it?

**Jacob Oluwole:** Is there one showing yours?

**Jacob Oluwole:** Is this only few? It's not showing complete messages, showing few message, incomplete message. It's not showing the full message, or it's not getting full message.

**Jacob Oluwole:** Because I'm sure my message is more than this.

**Jacob Oluwole:** Okay.

**Jacob Oluwole:** In.

**Jacob Oluwole:** I need to go post. I need to go post Inna video, Inna content, and noise content, and two others in the language.

**Taiwo Ola Balogun:** Okay.

**Jacob Oluwole:** How long do you add it down tomorrow, or this in the night?

**Taiwo Ola Balogun:** I just wanted me to join one meeting. I just want me to join this meeting that he has with Mark.

**Jacob Oluwole:** Uh, no, alright, alright.

**Taiwo Ola Balogun:** Okay.

**Jacob Oluwole:** Yeah, I'll be doing my bro, bye.

**Jacob Oluwole:** Oh my god, thank you, Jesus.

**Jacob Oluwole:** Why are you tagging me on this call? Leave me alone.

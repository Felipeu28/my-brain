---
source: Microsoft Teams transcript
captured: 2026-05-14
meeting_id: MSpjYzZhZWNhNS0xMjUxLTQ0ZGYtYjg2Mi05MmE5ODM3MWQ4N2IqMCoqMTk6bWVldGluZ19NREk0WlRjMk5XSXRaVFkwTVMwME0yRXlMV0kyT0RRdFlqSTRZVGM0Tnpkak5qVmpAdGhyZWFkLnYy
ingested: true
ingested_at: 2026-05-14
---

# Megan & Andres — 2026-05-14

## Meta

- **Subject:** Megan & Andres
- **Date:** 2026-05-14
- **Scheduled:** 16:00–16:30 UTC (11:00–11:30 AM Central) — actual transcript window 16:09–16:43 UTC
- **Organizer:** Andres Urrego (Andres@moilapp.com)
- **Attendees:**
  - Megan Miller — FitLogic Functional Medicine (active Moil customer), meganmillernp@gmail.com
  - Taiwo Ola Balogun — Moil engineer, Taiwo@moilapp.com

## Context

Working session to migrate Megan's sales/marketing email infrastructure from Gmail to Microsoft Outlook on the `myfitlogic.com` domain. Strategy: keep the primary practice domain (`fitlogicfunctionalmedicine.com`) protected from outbound marketing spam reputation by routing all sales/cold-outreach through the separate `myfitlogic.com` domain. `myfitlogic.com` already forwards to the main FitLogic site, so end-user experience is unchanged.

## Key decisions

1. **Two-domain architecture confirmed.** `fitlogicfunctionalmedicine.com` stays as the patient/client engine (`hello@`, etc.). `myfitlogic.com` becomes the sales engine for email marketing — protects the main domain from reputation hits.
2. **GoDaddy delegate access granted.** Megan added Andres@moilapp.com as a delegate on her GoDaddy account so Taiwo can finish DNS / domain verification without needing Megan logged in live each time. Megan struggled to select a specific domain in the "individual domains" picker — Andres confirmed full-account delegate was fine for now.
3. **Security posture committed.** Moil should not retain continuous access to customer accounts. Pattern going forward: log in only while actively working, log out when done, and Megan rotates all passwords post-deployment. Two-factor authentication stays on (Andres praised Megan for having it).
4. **Connections (sales tool) credentials located.** Megan had previously dropped them in Connect Team on May 7th — Andres confirmed he has what he needs.

## Action items

- [ ] **Taiwo** — Tonight (2026-05-14): finish creating the new account against the `myfitlogic.com` Outlook email, verify the email and the domain, complete the GoDaddy delegation flow. Migration target: ready for Megan tomorrow.
- [ ] **Taiwo** — Same evening: also handle the Meridian setup. The verification code was sent to `Travis@zoho.com` and the mailbox appears empty / not received. Re-run the request, ping Andres, Andres will ask Travis for the code.
- [ ] **Andres** — 2026-05-15 (Fri): send Megan access to the new system "first thing tomorrow."
- [ ] **Megan + Michelle** — 2026-05-18/19 (Mon/Tue): play with the system, try to break it, surface bugs before the Wednesday review.
- [ ] **Andres + Megan** — 2026-05-20 (Wed) 10:00–11:00 AM at FitLogic (in person): walk through the deployed system, fix anything Megan/Michelle flagged. Meeting invite already sent during the call.
- [ ] **Megan (post-deployment)** — rotate all passwords on touched accounts (GoDaddy, Connections, the new Outlook mailbox).

## Open issues surfaced

- The "individual domains" delegate flow on GoDaddy didn't let Megan pick a specific domain — defaulted to FitLogic Functional Medicine. Worked anyway because Andres got delegate access at the account level. Worth checking whether this is a GoDaddy UI quirk or a permission scope Megan needs to re-do later.
- During 2FA auth, the Microsoft Authenticator prompt vanished before Megan could approve, requiring multiple resends from Taiwo. Annoying but resolved by Megan refreshing the app.
- The "508F6B8D9.conversions.godaddy.com" forwarding rule Megan saw was a GoDaddy email-forwarding artifact she didn't recognize — she turned it off. Worth confirming nothing important was relying on it.

## Side note (not action — context)

Andres mentioned teaching at the Buda HIVE Mondays plus 11–1 coachings Monday–Friday (mostly virtual). Megan offered to meet Andres at HIVE; Andres preferred in-person at FitLogic on Wednesday.

---

## Full transcript (WEBVTT, speaker-attributed)

```
WEBVTT

00:00:06.544 --> 00:00:07.344
<v Megan>That's the.</v>

00:00:06.864 --> 00:00:09.664
<v Andres Urrego>Oh, I guess we can, the C is the new one.</v>

00:00:08.504 --> 00:00:09.744
<v Megan>That's the connections.</v>

00:00:10.704 --> 00:00:14.544
<v Andres Urrego>Yeah, okay, okay. Go ahead and send it to that one. Yeah, send it to that one.</v>

00:00:11.024 --> 00:00:12.304
<v Megan>That's the connections one.</v>

00:00:11.424 --> 00:00:12.624
<v Taiwo Ola Balogun>I don't know.</v>

00:00:14.624 --> 00:00:15.104
<v Taiwo Ola Balogun>Okay.</v>

00:00:15.624 --> 00:00:18.784
<v Andres Urrego>Which I think may announce, yeah, that way we know exactly which one it is.</v>

00:00:21.664 --> 00:00:28.704
<v Megan>No, I can get logged in there, though, so it might take me a minute, because, well, no, I'm already logged in.</v>

00:00:27.264 --> 00:00:27.984
<v Andres Urrego>Ohh, no.</v>

00:00:29.664 --> 00:00:35.984
<v Andres Urrego>Okay, I was like, 'cause I know, oh yeah, the other day wasn't letting you in.</v>

00:00:37.224 --> 00:00:38.784
<v Megan>Right now it says I need to sign in.</v>

00:00:42.544 --> 00:00:52.224
<v Megan>Yeah, it took me like in circles and then finally I was able to log in. It keeps logging me into that other admin one. All right, I'm going to refresh.</v>

00:00:56.544 --> 00:01:00.544
<v Megan>Okay. Okay, I'm going to take a picture of this because...

00:01:04.704 --> 00:01:10.864
<v Megan>It says email is being forwarded to support at 08F6B8D9, a bunch of numbers.</v>

00:01:13.664 --> 00:01:17.824
<v Megan>dot conversions, Godaddy.com. And then I click, I'm going to click turn off.</v>

00:01:22.624 --> 00:01:24.464
<v Megan>Why is it asking me to forward an email?</v>

00:01:27.344 --> 00:01:28.384
<v Megan>I'm gonna just turn it off.</v>

00:01:29.744 --> 00:01:33.344
<v Andres Urrego>Um, that's just, yeah, yeah, no, no need for forwarding, I don't think.</v>

00:01:34.304 --> 00:01:37.744
<v Megan>No, but I turned it off and now it's... Let me see.</v>

00:01:43.104 --> 00:01:51.904
<v Megan>Okay, I have nothing in my inbox. Might have to resend it if you already sent it because it looked like it was being forwarded.</v>

00:01:51.424 --> 00:01:52.704
<v Taiwo Ola Balogun>Okay, let me resend it.</v>

00:02:21.424 --> 00:02:22.944
<v Taiwo Ola Balogun>Okay, did you get that?</v>

00:02:24.944 --> 00:02:29.344
<v Megan>I have not gotten anything. It says all done for the day. Enjoy your empty inbox.</v>

00:02:31.344 --> 00:02:33.584
<v Andres Urrego>Well, I'll give it a minute and see if it comes through.</v>

00:03:19.984 --> 00:03:21.264
<v Taiwo Ola Balogun>This is connection.</v>

00:03:23.024 --> 00:03:26.544
<v Andres Urrego>Connections, yeah, my fitlogic.com.</v>

00:03:27.944 --> 00:03:29.504
<v Megan>No, it's connections at my.</v>

00:03:31.104 --> 00:03:32.304
<v Megan>Yeah, myfitlogic.com.</v>

00:03:36.944 --> 00:03:43.024
<v Andres Urrego>If not, we can try another way. Click where it says try another way. Taiwo, let's see if we can send it to the other email address.</v>

00:03:54.624 --> 00:04:01.904
<v Andres Urrego>Yeah, I would assume that the issue might be, I don't know, might not be coming through right now, but we could try the Megan at.</v>

00:04:04.464 --> 00:04:08.464
<v Megan>I'm just going to refresh one more time, but yeah, it still says there's nothing in there.</v>

00:04:08.144 --> 00:04:12.384
<v Andres Urrego>But go to sign in, go back to GoDaddy real quick, Taiwo.</v>

00:04:32.064 --> 00:04:35.744
<v Taiwo Ola Balogun>Okay, I wanted to like start the entire process from the beginning.</v>

00:04:36.304 --> 00:04:43.584
<v Andres Urrego>Yeah, but just do try another way right here at the bottom where it says try another way. Let's just do that real quick.</v>

00:04:55.104 --> 00:05:01.504
<v Andres Urrego>Once you're back in, then we can check and see if we can send it to that other email address.</v>

00:05:01.544 --> 00:05:08.384
<v Megan>Yeah, it doesn't make sense for them to send a code to the email address. So you're trying to log in to the email or what?</v>

00:05:08.464 --> 00:05:10.864
<v Taiwo Ola Balogun>Yes, yes, I'm trying to log in back to the email.</v>

00:05:10.784 --> 00:05:16.144
<v Andres Urrego>Not, not to the email to back to GoDaddy, so that he can send, yeah.</v>

00:05:14.144 --> 00:05:23.904
<v Megan>Oh, well then you got to put it, yeah, that's not going to be, that's going to be a different email that's not connected to GoDaddy login. It's only email.</v>

00:05:42.144 --> 00:05:45.184
<v Andres Urrego>But I don't, yeah, but that one doesn't get you into GoDaddy though.</v>

00:05:55.104 --> 00:05:59.824
<v Andres Urrego>She's already logged in to her email for connections, Taiwo.</v>

00:06:02.064 --> 00:06:08.384
<v Taiwo Ola Balogun>Yeah, so I need to log into the email because I'm going to be using the email to create the same account.</v>

00:06:08.784 --> 00:06:14.224
<v Andres Urrego>Oh, that's true. That's true. Because you need to send to... Yeah, you need to move it to the...</v>

00:06:13.264 --> 00:06:18.784
<v Taiwo Ola Balogun>Yeah, I need to verify that email, verify the domain also, so I need both, basically.</v>

00:06:19.464 --> 00:06:37.584
<v Andres Urrego>For the automated emails, Megan, we had already set it up with the previous email account. So now we have to set it up under the, we have to create the recent account, everything with your MyFitLogic email, right? So like, again, it's unified, you have everything under one.</v>

00:06:36.624 --> 00:06:43.104
<v Megan>So, we're not gonna have to actually log in though, right? To the email, we can we can check the email and send and everything.</v>

00:06:42.464 --> 00:06:46.664
<v Taiwo Ola Balogun>I think you can log into the email and delegate access for the GoDaddy.</v>

00:06:47.464 --> 00:06:55.344
<v Andres Urrego>You won't have to sign into the email later on, but you know we'll have to sign into that email right now as we create these accounts and move everything over.</v>

00:07:00.184 --> 00:07:13.344
<v Megan>What I'm trying to make sure I understand is that using this platform that you've created, that's where we can check and send emails, but we don't have to actually go log into Microsoft.</v>

00:07:13.904 --> 00:07:28.384
<v Andres Urrego>Correct, exactly. So, that's exactly what we're what we're finalizing.</v>

00:07:25.664 --> 00:07:40.064
<v Taiwo Ola Balogun>I was suggesting for the delegation of GoDaddy, instead of me logging into it, you can delegate access for me to be able to access it, not have it to log in, but for the email we have to log in to be able to get.</v>

00:07:38.704 --> 00:07:51.504
<v Andres Urrego>Okay, so I'll give you access to my GoDaddy where I have, where I think Megan made me a delegate or maybe not yet. Let me see.</v>

00:07:53.024 --> 00:07:57.744
<v Andres Urrego>Megan, can you do me a favor? Can you sign into your GoDaddy real quick and share your screen for a second?</v>

00:08:07.024 --> 00:08:24.864
<v Andres Urrego>Send it to that one, to the Megan at, I mean, we would assume that is Megan at gmail.com. Yeah, send it to that one and we'll see if she can find it. And then Ty, we'll go ahead and stop sharing real quick. I'm going to just have Megan add me as a delegate and then you can access to my account.</v>

00:08:28.264 --> 00:08:28.944
<v Megan>Can you see my screen?</v>

00:08:29.504 --> 00:08:32.944
<v Andres Urrego>Yes, perfect. So we're going to go find my fitlogic.com.</v>

00:08:38.144 --> 00:08:40.304
<v Andres Urrego>I think that was logic functional medicine.</v>

00:08:41.184 --> 00:08:43.664
<v Megan>Yeah, there's two domains in there.</v>

00:09:04.304 --> 00:09:09.584
<v Andres Urrego>We got view all there, there we go, and I think you were stores the bottom, uh, view my products.</v>

00:09:38.784 --> 00:09:43.344
<v Andres Urrego>Actually, here, let me log into mine and I'll tell you exactly where we need to go.</v>

00:09:54.464 --> 00:09:57.744
<v Megan>Everything was supposed to be under FitLogic functional medicine, not my FitLogic.</v>

00:10:02.144 --> 00:10:09.264
<v Megan>And I know it's going to be, so I just don't want things to get screwed up.</v>

00:10:13.744 --> 00:10:17.664
<v Andres Urrego>Say that again, so you wanted to still be in there?</v>

00:10:18.224 --> 00:10:21.184
<v Megan>Well, everything was, see how it says website plan free.</v>

00:10:32.224 --> 00:10:36.704
<v Megan>Well, I mean, I don't really understand a lot of this, but...</v>

00:10:38.944 --> 00:10:58.584
<v Megan>When I did my website last time, they specifically asked me, do you want the main site to be FitLogic Functional Medicine or My FitLogic? And I said FitLogic Functional Medicine. I never checked on that. But I know like when you type in, when you type in the website,</v>

00:10:59.104 --> 00:11:02.904
<v Megan>You know, like, um, it my fit logic gets.</v>

00:11:03.984 --> 00:11:06.624
<v Megan>Forwarded to FitLogic Functional Medicine.</v>

00:11:04.144 --> 00:11:05.584
<v Andres Urrego>Oh yeah, of course, of course.</v>

00:11:11.424 --> 00:11:24.864
<v Andres Urrego>So then myfitlogic.com, you already have the domain, and we're using that for your entire sales, let's say, department, right? So that will be your email marketing, and then that way that doesn't...</v>

00:11:26.624 --> 00:11:45.664
<v Andres Urrego>That doesn't hurt your existing domain. You don't get, you know, FitLogic functional medicine doesn't get, you know, spam blocked, right? So we basically use myfitlogic.com. People are still going to click on it and they're still going to go to your website.</v>

00:11:46.144 --> 00:11:48.704
<v Andres Urrego>But in that way, we keep it separate from...</v>

00:11:49.504 --> 00:12:11.544
<v Andres Urrego>From hello, we keep it separate from C, and then it's a lot easier because now you have a sales engine and then you have your client engine, which is what you already have today. OK, so let me if you do me a favor, if you click up here on MM on the right side.</v>

00:12:12.464 --> 00:12:15.984
<v Andres Urrego>Yeah, let's see. Do account settings. There we go.</v>

00:12:17.344 --> 00:12:23.104
<v Andres Urrego>Um, we're gonna, yes, delegate access on the left side. There we go.</v>

00:13:25.304 --> 00:13:26.704
<v Megan>Do I do request access?</v>

00:13:31.264 --> 00:13:33.504
<v Megan>This is like I'm requesting access from you.</v>

00:13:33.184 --> 00:13:35.344
<v Andres Urrego>Yeah, I know you gotta do delegate access.</v>

00:13:36.424 --> 00:13:38.064
<v Megan>It does say, it says delegate access.</v>

00:13:38.144 --> 00:13:41.984
<v Andres Urrego>Oh, sorry, right here on the right side. If you scroll down a little bit more, there we go.</v>

00:13:46.944 --> 00:13:49.264
<v Andres Urrego>And then Andres and Moil are back down, please.</v>

00:14:17.664 --> 00:14:19.024
<v Megan>I have to now go to the domain.</v>

00:14:19.464 --> 00:14:21.504
<v Andres Urrego>That's perfect. Now let me see.</v>

00:14:28.224 --> 00:14:30.304
<v Andres Urrego>I think I just got an email.</v>

00:14:47.984 --> 00:14:52.024
<v Megan>I don't know how to give you, because this is the one you need access to. I don't know how to do that.</v>

00:14:52.704 --> 00:14:58.624
<v Andres Urrego>It's I I I got the email right now, so I I'll be able to actually go in and we're good.</v>

00:14:59.424 --> 00:15:04.864
<v Megan>Well, it said specific domains, but it didn't ask me which one, so I don't know how to.</v>

00:15:15.624 --> 00:15:18.584
<v Megan>Oh, now it's the same logic functional medicine.</v>

00:15:49.624 --> 00:15:51.864
<v Megan>Click that, or is it not letting me click?</v>

00:16:07.584 --> 00:16:13.584
<v Andres Urrego>The domains only is fine, yeah, I mean, it, it, yeah, I don't think it lets you, but, but we're we're all the...</v>

00:16:12.584 --> 00:16:15.384
<v Megan>It says choose individual domains under my domains.</v>

00:16:40.504 --> 00:16:44.344
<v Megan>I hope this doesn't make any sense. It won't let me click on it.</v>

00:17:08.784 --> 00:17:15.584
<v Andres Urrego>I mean, I honestly, honestly, I think we're good. I think I'm in, so yeah, I'm in.</v>

00:17:17.344 --> 00:17:21.344
<v Andres Urrego>We'll get this done today. Let me see.</v>

00:17:30.064 --> 00:17:33.424
<v Andres Urrego>Yeah, perfect. No, so we're in. OK, Taiwo, so...</v>

00:17:35.224 --> 00:17:41.824
<v Andres Urrego>We're good there. Yeah, so it's myfitlogic.com. It has the forwarding to FitLogic functional medicine. Perfect.</v>

00:17:50.304 --> 00:17:52.944
<v Taiwo Ola Balogun>Yeah, I will send email on email.</v>

00:17:55.344 --> 00:17:58.224
<v Andres Urrego>Oh, access to the email. Okay.</v>

00:18:05.504 --> 00:18:08.384
<v Andres Urrego>I think I have the credentials. I'll sign you in because I...</v>

00:18:18.064 --> 00:18:28.224
<v Andres Urrego>Taiwo, you're cutting out. I think it's a bad connection, but it's OK. Megan, I believe you already sent me the credentials for the connections, right?</v>

00:18:28.744 --> 00:18:30.584
<v Megan>I think so.</v>

00:18:30.304 --> 00:18:33.344
<v Andres Urrego>Yeah, I did. I think so too. Let me look.</v>

00:18:37.104 --> 00:18:38.744
<v Megan>It would be in Connect Team, probably.</v>

00:18:40.264 --> 00:18:45.864
<v Megan>So, yeah, if you open that and scroll up, I put it.</v>

00:18:48.504 --> 00:18:50.384
<v Megan>I put it in there on May 7th. Yeah.</v>

00:18:51.064 --> 00:18:54.864
<v Andres Urrego>Beautiful. OK, awesome. So connections, I got it there.</v>

00:18:56.624 --> 00:19:04.784
<v Andres Urrego>And I think that's it. I think that's it because we needed that code, but now we'll be able to send the code here.</v>

00:19:09.744 --> 00:19:16.304
<v Taiwo Ola Balogun>I think I'm still waiting for the code here. If the code is available, I think if I get it, I'll be able to log in.</v>

00:19:17.264 --> 00:19:23.344
<v Andres Urrego>Can you check on the Megan at Gmail account, please? See if you got the code.</v>

00:19:22.504 --> 00:19:25.144
<v Megan>Megan Miller or Meg Miller?</v>

00:19:26.664 --> 00:19:29.664
<v Taiwo Ola Balogun>Yeah, both, both, don't know which one, so both.</v>

00:19:36.504 --> 00:19:40.664
<v Megan>Ohh, GoDaddy's connected. I know which one they're connected to, but I don't have anything.</v>

00:19:43.344 --> 00:19:48.184
<v Taiwo Ola Balogun>Okay, I think there's one that is an administrator and there was one that was not.</v>

00:19:49.544 --> 00:19:54.584
<v Megan>Yeah, it's, oh wait here. Oh, I just got an alert that I updated.</v>

00:19:58.344 --> 00:20:00.664
<v Megan>Andres Urrego Martinez.</v>

00:20:02.944 --> 00:20:08.224
<v Andres Urrego>I love it. I was actually really good. I love it.</v>

00:20:06.744 --> 00:20:08.744
<v Megan>But I didn't get a code.</v>

00:20:20.144 --> 00:20:25.464
<v Megan>Let's see, I got a security alert. Okay, this might be, well, this is from Tuesday.</v>

00:20:29.944 --> 00:20:32.424
<v Megan>I have not gotten anything today.</v>

00:20:36.504 --> 00:20:44.664
<v Megan>Let me log in on my laptop, because sometimes my phone is, you know, doesn't update as fast.</v>

00:20:51.784 --> 00:20:52.824
<v Megan>I hate past keys.</v>

00:21:08.744 --> 00:21:11.304
<v Megan>I do not see anything.</v>

00:21:12.344 --> 00:21:15.384
<v Andres Urrego>And that's in your Megan, Megan.</v>

00:21:14.744 --> 00:21:20.584
<v Megan>It's Meg Miller 43. That's the one that's attached to GoDaddy.</v>

00:21:19.944 --> 00:21:26.744
<v Andres Urrego>Okay, can you check just in case the other Megan also at gmail.com?</v>

00:21:25.624 --> 00:21:27.384
<v Megan>Megan Miller, yeah, there's nothing there.</v>

00:21:29.944 --> 00:21:34.264
<v Megan>Oh, I just got something. Just popped in.</v>

00:21:38.504 --> 00:21:41.264
<v Megan>The date was May 14th, 2026 at 530.</v>

00:21:44.264 --> 00:21:47.944
<v Megan>Yeah, but it says from Nigeria, so it's probably got to be you.</v>

00:21:48.744 --> 00:21:50.104
<v Andres Urrego>Yes, it is. It is us.</v>

00:21:49.864 --> 00:21:51.704
<v Megan>968022</v>

00:21:53.224 --> 00:21:54.544
<v Andres Urrego>But it says 530.</v>

00:21:54.584 --> 00:21:56.024
<v Megan>Just came in now.</v>

00:21:59.224 --> 00:22:01.784
<v Megan>Yeah, West Africa Standard Time.</v>

00:22:01.464 --> 00:22:04.424
<v Taiwo Ola Balogun>I think, yeah, that's my lookout time, yeah.</v>

00:22:05.544 --> 00:22:07.064
<v Megan>Yeah, 968022.</v>

00:22:09.384 --> 00:22:13.864
<v Taiwo Ola Balogun>Okay, yeah, another authentication on the authentication app.</v>

00:22:15.544 --> 00:22:17.384
<v Andres Urrego>Do you have an authenticator app, Megan?</v>

00:22:18.424 --> 00:22:20.584
<v Megan>No, no, but.</v>

00:22:23.544 --> 00:22:27.024
<v Andres Urrego>Like on your phone, does it ever ask you to approve?</v>

00:22:31.224 --> 00:22:36.104
<v Andres Urrego>Oh, you don't have an authenticator app for the Microsoft account yet.</v>

00:22:35.224 --> 00:22:39.784
<v Megan>Well, I have two authenticator apps, but oh, here, are you trying to sign in?</v>

00:22:40.424 --> 00:22:41.784
<v Andres Urrego>Yes, okay, there you go.</v>

00:22:46.024 --> 00:22:50.024
<v Andres Urrego>Good job, by the way, always setting up your two-factor authentication.</v>

00:22:50.344 --> 00:22:55.304
<v Megan>Oh, such a pain in the ***. That's for the email though.</v>

00:22:56.664 --> 00:23:01.384
<v Andres Urrego>Yeah, it just, it just, I think it was just do send another request, Taiwo, yeah.</v>

00:23:10.824 --> 00:23:14.744
<v Andres Urrego>But yeah, two-factor authentication is like literally the best way.</v>

00:23:17.384 --> 00:23:20.824
<v Andres Urrego>One time I had my Facebook account stolen and I was like, yeah.</v>

00:23:23.384 --> 00:23:30.344
<v Megan>Well, now it's not allowing me to push yes. I already authenticated that last number, so I don't know why another one.</v>

00:23:32.504 --> 00:23:36.424
<v Andres Urrego>All because he declined it, he showed that he was declined.</v>

00:23:35.864 --> 00:23:37.384
<v Taiwo Ola Balogun>Can you swipe down to refresh?</v>

00:23:39.304 --> 00:23:42.584
<v Megan>So you're trying to log into the email because I thought you already had access to everything.</v>

00:23:44.824 --> 00:24:05.664
<v Andres Urrego>Well, it logs us out, right? So like, if we log in and then we don't use it, it probably logs him out. And I like that as a security measure. So basically, like, if we are ever going to touch your accounts, it should always be, you know, like this, right? We should never have like continued access.</v>

00:24:06.744 --> 00:24:10.424
<v Megan>Right, well, I mean, I can change the password, but...</v>

00:24:10.024 --> 00:24:25.464
<v Andres Urrego>For sure. No, and I mean continued access, even like on a day-to-day basis, it should only be like we only use it when we're working on something. And yes, once we actually deploy everything, you should change all of your passwords.</v>

00:24:26.424 --> 00:24:40.264
<v Andres Urrego>For these things, right? Like the connections that might fit logic, you know, just do another Apple password and you go. But you have two factor authentication, which will always notify you when anything is being touched on the account.</v>

00:24:45.384 --> 00:24:46.984
<v Andres Urrego>Did it allow you to tap on 26?</v>

00:24:46.104 --> 00:24:52.664
<v Megan>Are you trying to sign in? And then it says enter the number shown to sign in, but I don't have a number to put in.</v>

00:24:52.504 --> 00:24:53.784
<v Andres Urrego>All right here, 26.</v>

00:24:55.224 --> 00:24:57.784
<v Andres Urrego>It's number twenty-six, yeah.</v>

00:24:59.144 --> 00:25:00.584
<v Megan>Ohh, it just went away again.</v>

00:25:39.064 --> 00:25:46.984
<v Andres Urrego>And we had already gone through all of this with the Gmail, but since we got the Outlook account for my fit logic, then...</v>

00:25:48.344 --> 00:25:52.824
<v Andres Urrego>That's basically why this just feels like we're doing everything over again. It's just, we are.</v>

00:25:54.184 --> 00:26:01.864
<v Megan>Yeah, well, I'm just gonna close the app and then I'm not getting anything.</v>

00:26:02.824 --> 00:26:04.104
<v Megan>Pop-up window went away.</v>

00:26:06.984 --> 00:26:09.144
<v Taiwo Ola Balogun>Can you refresh if you are going to get it?</v>

00:26:09.944 --> 00:26:17.304
<v Andres Urrego>She's just opening it up again. Maybe you're gonna have to refresh Taiwo in case it just declined it already.</v>

00:26:24.184 --> 00:26:26.144
<v Andres Urrego>Just go ahead and refresh the screen Taiwo.</v>

00:26:35.704 --> 00:26:40.264
<v Megan>I'm going to have to go in a few minutes. Oh, here it goes. Okay, it was asking me for a number.</v>

00:26:40.744 --> 00:26:41.784
<v Andres Urrego>Yes, 99.</v>

00:26:47.784 --> 00:27:08.344
<v Andres Urrego>All right, we're good. Done. Okay, that's it. Anything else, I'll text you, but yes, our goal is we'll literally, you know, kind of rewire everything to Microsoft today. And as soon as that, as soon as Taiwo completed, he's going to work on this, so he's done.</v>

00:27:08.824 --> 00:27:16.344
<v Andres Urrego>And then, as soon as we're completed here, we'll send you an email so that you can go in there and start playing with it right away.</v>

00:27:16.784 --> 00:27:18.584
<v Megan>Perfect. Hey, what days are your?</v>

00:27:20.504 --> 00:27:22.504
<v Megan>What days are you at the hive?</v>

00:27:25.704 --> 00:27:32.344
<v Andres Urrego>So we're teaching Mondays, but then we do 11 to 1 coachings Monday to Fridays.</v>

00:27:34.904 --> 00:27:43.784
<v Andres Urrego>But we do, you know, we do virtual very often, very here and there we do an in person, but why do you ask? What's up? Talk to me.</v>

00:27:43.304 --> 00:27:47.944
<v Megan>Well, I was going to say I could meet you up there after one of the...</v>

00:27:49.624 --> 00:27:52.184
<v Megan>trainings or whatever if that's helpful.</v>

00:27:53.384 --> 00:28:16.264
<v Andres Urrego>Yeah, no, no, no, I can come to, no, no, let's push this out and then if you want, I mean, I Tuesday, let's set up a time Tuesday and I'll just come in or we can meet at the hive, either way. But I think it, yeah, because then now that you have access, now that we've done, we're done at least with this beginning with this initial part.</v>

00:28:16.744 --> 00:28:20.904
<v Andres Urrego>Then we can actually go through it and make sure that everything's good.</v>

00:28:22.664 --> 00:28:27.944
<v Megan>Okay, Tuesdays are usually my busier day, but let me just check.</v>

00:28:27.064 --> 00:28:30.104
<v Andres Urrego>Okay, Wednesday, I mean, you tell me.</v>

00:28:30.904 --> 00:28:33.264
<v Andres Urrego>I think you said was they maybe are better.</v>

00:28:32.424 --> 00:28:37.464
<v Megan>Yeah, Tuesday I have patients all day, Tuesday, Wednesday.</v>

00:28:43.224 --> 00:28:45.144
<v Megan>Yeah, I could do Wednesday.</v>

00:28:46.184 --> 00:28:50.264
<v Andres Urrego>OK, uh, let's see, let me look, Wednesday.</v>

00:28:59.544 --> 00:29:01.864
<v Andres Urrego>Wednesday, 10.</v>

00:29:03.384 --> 00:29:04.104
<v Megan>Yeah, that works.</v>

00:29:05.864 --> 00:29:07.944
<v Andres Urrego>Alright, so let me send it.</v>

00:29:27.624 --> 00:29:50.904
<v Andres Urrego>Done right, 10 to 11, I got us, 10 to 11, at FitLogic, if that works. If anything changes, please let me know. But then that way you have a couple of days for you and Michelle to like, you know, well, I mean, yeah, probably if we give it to you tomorrow, you know, access to you first thing tomorrow, then you might have a couple hours, but if not, then you have Monday and Tuesday to kind of play around with it, try to break it.</v>

00:29:51.624 --> 00:30:06.264
<v Andres Urrego>That's the initial plan after delivery, right, is let's find the bugs. Let's, you know, let's find the things that break, if any, and then, yeah, while you guys get familiarized with it, and then I'll be there Wednesday, and then we...</v>

00:30:07.784 --> 00:30:09.464
<v Andres Urrego>We keep going in, OK?</v>

00:30:10.104 --> 00:30:11.464
<v Megan>Awesome, thank you.</v>

00:30:11.864 --> 00:30:14.864
<v Andres Urrego>Thank you so much. Have a wonderful rest of your day.</v>

00:30:13.784 --> 00:30:16.184
<v Megan>All right. All right. See you soon. Bye.</v>

00:30:15.784 --> 00:30:17.784
<v Taiwo Ola Balogun>Thank you so much. Have a wonderful day.</v>

[After Megan drops]

00:30:23.704 --> 00:30:25.704
<v Andres Urrego>Taiwo, you good then? We got everything we need.</v>

00:30:27.544 --> 00:30:32.824
<v Taiwo Ola Balogun>Yes, sir, yes, sir, everything is ready, so I will get this evening.</v>

00:30:33.864 --> 00:30:37.384
<v Taiwo Ola Balogun>So, on the GitHub accounts, yeah, I'm able to set everything up.</v>

00:30:38.264 --> 00:30:41.544
<v Andres Urrego>Good. And then you said for Meridian we need what?</v>

00:30:44.184 --> 00:30:47.224
<v Taiwo Ola Balogun>Yeah, I was trying to log into the...</v>

00:30:48.824 --> 00:30:51.624
<v Taiwo Ola Balogun>He thought he gave me, he needed a code.</v>

00:30:52.424 --> 00:30:57.544
<v Taiwo Ola Balogun>Similar to this, also it needed a code, and I was trying to, like, get the code from you last night.</v>

00:30:55.504 --> 00:31:00.984
<v Andres Urrego>Where is he sending the code to? What email address is he sending the code to?</v>

00:32:48.904 --> 00:32:54.904
<v Taiwo Ola Balogun>Okay, this mail here, Travis at Zoho.com. So that is the mail.</v>

00:32:54.184 --> 00:33:10.744
<v Andres Urrego>Oh, okay. Ah, shoot. Okay, well, you're probably going to have to rerun that and then let me know. And then as soon as you request it again, I'll ask Travis for it.</v>

00:33:12.344 --> 00:33:14.584
<v Taiwo Ola Balogun>OK, no problem, no problem. Let's do it.</v>

00:33:22.664 --> 00:33:25.224
<v Taiwo Ola Balogun>Yeah, I'm confused why a mail is like empty.</v>

00:34:06.984 --> 00:34:12.344
<v Taiwo Ola Balogun>Okay, I will update you on this. I will update you on this. Have a good one, sir.</v>

00:34:11.504 --> 00:34:14.584
<v Andres Urrego>Hi, my boy. Sounds good. I'll catch you in a bit. Thank you very much.</v>
```

*Transcript edited for readability — filler turns (single "Yeah", "Okay", "Mm", overlapping monosyllables) removed. Full raw VTT available from Graph API.*

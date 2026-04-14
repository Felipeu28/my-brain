# Team Meeting 2025-01-22 - Transcript

**Source:** OneDrive transcript
**Date:** 2025-01-22
**Original file:** Team Meeting 2025-01-22 - Transcript.docx

---

Team Meeting - 2025/01/22 09:29 CST - Transcript
Attendees
Adeleke Tolulope, Andrés Felipe Urrego Martínez, Jacob Oluwole, Jacob Oluwole's Presentation, read.ai meeting notes, Taiwo Ola-Balogun
Transcript
Adeleke Tolulope: Hello. Good morning, Andre. How you doing?
Andrés Felipe Urrego Martínez: Steve, good afternoon. How are you, sir? Doing very good.
Adeleke Tolulope: I'm good. How you doing?
Andrés Felipe Urrego Martínez: Doing very good. Thank you. Let's just wait for the guys a couple of minutes and then we'll get started. I got about 30 minutes for us to go through our call. I'm preparing for we have a very important meeting today with it's called the workforce solutions of central Texas and this is the company that the government assigned 15 or…
Andrés Felipe Urrego Martínez: 20 million I think over the next five years for workforce development so very
Adeleke Tolulope: Is it okay?
Andrés Felipe Urrego Martínez: very very important meeting for us because I'll be able to I guess my goal is to get in there right I mean hey how can we partner this is what we have built this is where we're going we know they have $15 million and…
Andrés Felipe Urrego Martínez: they need to spend it and a lot of it is going to go to technology so let's see what the f*** we can do so that's why we need to move fast on this AI thing, we need to be able to my god, all this is getting transcribed. we need to get this AI thing going and start moving towards that development.
Adeleke Tolulope: Okay. Yeah.
Andrés Felipe Urrego Martínez: So while they joined so talk to me what do you feel last week I did read either last week or the week before I can't remember but I had read that obviously for what we need right now we should probably start with smaller models that are less that two things that we need to train less and then that don't consume as
Andrés Felipe Urrego Martínez: much power you know what I mean because again we tell me if I'm wrong for what we need we don't need a superco computer to be the coder right I mean we exactly not yet…
Adeleke Tolulope: Yeah. No,…
Adeleke Tolulope: we don't need a
Andrés Felipe Urrego Martínez: because we're not asking it to build AI tools we're asking it to just write code for specific solutions so finding a model that is light that allows us and that is pretty trained so I guess what I'm trying to say is how's it going? What are the challenges? Do you think maybe looking for models that are specific to what we want to do or is that already what you're looking into?
Andrés Felipe Urrego Martínez: Yeah. Yeah.
Andrés Felipe Urrego Martínez: I mean that just Mhm.
Adeleke Tolulope: Yeah. Yeah. And…
Adeleke Tolulope: And so far the other time when we started our research we said we should use polycoder but at the point of after my first fine tuning of that poly coder I realized that it's not even like our code base combined both the back end the front end everything combined together is still very very small compared to the number of code base or code that was used to finetune policer so the moment  I finished finetuning that first model. When I prompt it, it responded in a way that we write our code base. So it was somehow returning some results as from our codebase for me for the first maybe two to three prompt I gave to Yeah. Yeah.
Andrés Felipe Urrego Martínez: It was right. It was doing that.
Adeleke Tolulope: It was doing that but at a point it just went wild such that even if I keep prompting it based on my research it said either the code base is very small for the model that I'm using he said our code base is very small yeah it's too powerful…
Andrés Felipe Urrego Martínez: What did your research tell you about why it went wild or why that could have happened our code base?
00:05:00
Andrés Felipe Urrego Martínez: So it's too powerful for what we have so far.
Adeleke Tolulope:
Adeleke Tolulope: because for it to learn. It needs enormous codes to be able to work on that code base is just very small for it to comprehend to be able to learn on it. and it also say I also made a decide that if I increase some training parameters that maybe is going to learn as well.  So I think I tried it two more time by increasing the learning rate and also after increase parameter I also adjust the tokenization as well. So when I adjust tokenization and increase and make use of some training parameters I tried it again it performed the same way as the previous one.
Adeleke Tolulope: But the main thing that I now got in that I should make use of smaller model since our code base is not a big code base for that polycoder. So I explained to Jacob Jacob now said he had about a way that we can reduce that the model we are using is polyoder 2.7. Yeah. Yeah. So yeah,…
Andrés Felipe Urrego Martínez: noticed that. Yeah.
Adeleke Tolulope: but before that I already have a plan to make use of some smaller model or that polycoder like the code T5 and the Santa code as  So yesterday I trained the code T5. Is it I think a day before yesterday I trained the code T5. So it's responded in a better way unlike the poly coder. But that one is now not consistent. sometimes it won't respondse. Sometimes it will give me the code I want. Sometimes it will just give me something not related to what I'm even asking for asking it to do.
Adeleke Tolulope: So I then made another research.
Adeleke Tolulope: He now said I should try this Santa. But at the point of trying the Santaoda, you now send those deepse link to the group. As you send it to the group, I went through it. I noticed that the trend.
Andrés Felipe Urrego Martínez: …
Andrés Felipe Urrego Martínez: you did go through all the things I sent this morning.
Adeleke Tolulope: Yeah, I went through all the things you sent this morning.
Andrés Felipe Urrego Martínez: Good stuff,…
Adeleke Tolulope: Mostally the there stuff in there.
Andrés Felipe Urrego Martínez: Good stuff in there.
Adeleke Tolulope: especially the deepseek I even dropped a tweet on Twitter asking the person that hope went wide…
Adeleke Tolulope: if you train it on our small code base something like that but I'm not sure nobody has replied for that so I've sent my code to Jaj that I want to use  Peace.
Andrés Felipe Urrego Martínez: Yeah. Yeah.
Andrés Felipe Urrego Martínez: Very good. you asked that question to GPT yet? the question of can deep say would deepseek be a good tool for us based on our characteristics as a company our code base how big the code bases.
Andrés Felipe Urrego Martínez: So those are the things so I would just ask that question right I was actually just asking the question to it at mobile we want to train AI agents to write code for us what are the top models we should look into today today we are a small startup limit resources we do have credits from ashure for GPU but our developers are in the process of How big is our code base?
Adeleke Tolulope: So based on what I read on Twitter, I think if you are able …
Andrés Felipe Urrego Martínez: How big is our file?
Adeleke Tolulope: how big is our file? I can't say this is how big the file is. It is until when it has been  dividing into chunks now result into 300 plus lines of code 300 tokens and the number of tokens for the polyoder that we using is 2.7 billion tokens like a lot of code base was used to find tune it so 300 tokens if I'm not mistaken yeah 300 plus tokens
Andrés Felipe Urrego Martínez: and our front end.
Adeleke Tolulope: I know I only did it for the back end. 300 tokens. I haven't done it for the front end and what is it called? The two front end because my main focus now is the back end. I want you to be able to understand that back end very well before we can now go to the front end part.  So for the back end I think the token generated for the back end is 300 tokens 300 plus tokens and it's very small compared to what we want to train it and what compared to the models we are using. So I'm now trying some smaller models today. Now I tried a smaller model Santa Coda and I think that one took a lot of time to complete the finetuning.
00:10:00
Adeleke Tolulope: So I'm at the point of downloading it and testing it out to see how better it is compared to other code models that I've used so far because other code that I used so far I noticed that the finetuning was a bit faster. You get that the was a bit faster. so I now made that assumption that maybe it was not even doing the necessary thing that supposed to do on the data set. But today the Santa Coder that I make use of it took about is not 3 hours like that though I run it through the pipeline. So I'm not on my system.
Adeleke Tolulope: So thanks to Pipeline can help me to just keep running it there while I'm doing something else.
Andrés Felipe Urrego Martínez: It's cheaper, So that way we can work on non and…
Adeleke Tolulope: Yeah. Yeah,…
Andrés Felipe Urrego Martínez: I mean again we don't have to. I'm just saying once we get into deeper training you can let it train overnight while you sleep. If it is a time where price is cheaper and while price is not cheaper then you can work on other activities. Does that make sense?
Adeleke Tolulope: Maybe they will join.
Andrés Felipe Urrego Martínez: Did nobody else join the meeting or did people do like tomorrow or…
Adeleke Tolulope: They will join.
Andrés Felipe Urrego Martínez: are you having a laugh, what is going on here, Mhm.
Adeleke Tolulope: Concerning what you sent one trend to the group that I think the trend was talking about he can set up an AI agent in less than 2 minutes. So I tried it out but I wasn't able to complete the entire process…
Andrés Felipe Urrego Martínez: How did that go?
Adeleke Tolulope: because but some little issue I downloaded the…
Andrés Felipe Urrego Martínez: Somehat. But do you think it's possible and…
Adeleke Tolulope: if you check the video, it downloaded a particular Yeah.
Andrés Felipe Urrego Martínez: you run into a problem or you think it's b*******?
Adeleke Tolulope:
Adeleke Tolulope: No, no, no. It's 100% possible because even our ID what we are using to code is making use of all these opensource models like the cloud chbt and all that I shared with you the other day.
Andrés Felipe Urrego Martínez: There you go. Okay.
Adeleke Tolulope: So I think what that guy was explaining was something similar to that as well.  In what is it called that in case that person don't want to use cloud and cursor that we making use of so if the person want to use any other because for now if you want to use that cursor we are going to use based on the AI that has been integrated into it but what that guy was doing was that if you want your own custom model maybe you want to use another mode there that is superior to the model you can do that one  as well. But the main goal is still the same thing with what the code base we have. But that one is not really really an agent that we want to build ourself because the agent that we want to build ourself is an agent that will be able to execute some task by understanding our code base and be able develop some new feature that we want to work on.
Adeleke Tolulope: So such that once it is done then we'll come and review it and we now make our corrections or feedback for it to it.  So I have an idea of though I haven't tried it yet I want to open I want to make use of that cursor and then that prompt that code base that AI that has been integrated into that cursor I want to prompt it so that can it help me to maybe can it give me the code or can it put me through on how I can train a model to understand the entire code because that
Adeleke Tolulope: model already understand that entire code base. I don't know you got what I'm trying to say because for if I'm coding with that particular cursor that ID if I'm encountering any issue at any point in my file if I just click on that bug and then ask that AI agent to debug it for me. It's going to debug it and then know where other files that particular function is connected to. that means that model already have the white scope of our code base. So what I'm now trying to do is that I want to leverage on that and…
00:15:00
Andrés Felipe Urrego Martínez: Yeah, because the instruction would have to be clear whenever we're going to make changes and…
Adeleke Tolulope: ask you
Andrés Felipe Urrego Martínez: and just obviously review all connections and parameters associated with this changes to ensure that it will not break or truncate any other processes within the site. that's obviously after training. We would have to kind of test around that and say okay make this change take into account that obviously this code based is associated with other things so ensure that it does the other things don't break or that these changes don't affect do you know what I'm saying
Adeleke Tolulope: I also noticed now is that once we are able to finetune this model we know that I'm just thinking that it to be possible but I know that it's something that we should try out once we are able to find this model and we have that model ourself instead of hosting it on a cloud that will be paying for it I and t can integrate it into our local workspace on our system that it will just be doing the work for Instead of hosting it on the cloud, I will be paying for it conse consecutively as we are making use of it is the thing that…
Adeleke Tolulope: because I noticed the trend he sent to the group he downloaded that model and he was asking that model some question about you can work directly from your computer.
Andrés Felipe Urrego Martínez: Yeah,…
Andrés Felipe Urrego Martínez: because there was one that said that you can work directly from your computer or whatnot. But…
Adeleke Tolulope: So that's what I'm saying that Yeah.
Andrés Felipe Urrego Martínez: but again, I mean and now I know that a lot of those guys that do those videos, they have a lot of power literally GPU units connected to the computer. but I don't know because I didn't watch that one all the way. So, I don't know what they were saying, but I thought it sounded more like that was not required. but you did watch it. so what did you think?
Adeleke Tolulope: Yeah. yeah, what I think is that we are trying to find this model. Then once we are done with this model we are going to integrate that model into our ID such that it will be able to work.
Andrés Felipe Urrego Martínez: Mhm.
Adeleke Tolulope:
Adeleke Tolulope: There are two ways we can do it. We can either do it so that we deploy that model on Azour itself and then we are now communicating that Azour maybe each time I want to code I want to work I'll just go and start that application on Azour so that it more easier for it to work for me based on what I want to do that is the first one by deploying the model on Azour or two by compiling the weight by quantizing the model reducing the size of the model so that you can download it on your system and then you can make use of it on your system. it depends on when we are done with the
Andrés Felipe Urrego Martínez: And I'm assuming that allows you to do certain I mean that's another thing right understanding okay…
Andrés Felipe Urrego Martínez: what kind of tasks will be more efficient for us to do through that than through GPU right so correct exact Exactly.
Adeleke Tolulope: Okay.
Adeleke Tolulope: Yeah, You have a point there because our current system does not have this GPU stuff. So, we can leverage on the GPU on Azor for it to increase and speed up the rate at which it work for us. You are right for that.
Andrés Felipe Urrego Martínez: So you do the things that Yeah.
Andrés Felipe Urrego Martínez: So you do the things that can be done on the PC while everything else is running on the back end that we cannot run on the PC.
Adeleke Tolulope: Yeah, Exactly.
Andrés Felipe Urrego Martínez: And then that way see that because that's exactly where I want us to go, Steve, is that you guys can do some work while we are writing code on the back end.  I mean you have these things writing fixing your code, debugging for you and then you just spend your day reviewing doing more of the manual stuff that still didn't need that manual touch the reviewing obviously the front end is a bit more unless we can get it to a point where it just kind of right that's front end as well but I think we're on a very good path.  I think we need to figure out before we keep training 10 20 models. We just need to figure out which one's going to be the best one for us. What was the name of the one I sent you? Was it deep or the thing I sent? What was it?
00:20:00
Andrés Felipe Urrego Martínez: Deep bomb.
Adeleke Tolulope: The deepseek R1.
Adeleke Tolulope: The one you sent to the group. Deepseek R1. Based on…
Andrés Felipe Urrego Martínez: Deep sea. R1.
Adeleke Tolulope: what I read on, I think it's more better than even 01 mini and…
Andrés Felipe Urrego Martínez: And it's very like the amount of Yeah.
Adeleke Tolulope: it's open source and…
Andrés Felipe Urrego Martínez: that I mean it's so efficient with the tokens. I mean it consumes so much less GPU and…
Adeleke Tolulope: it's open source as well.
Andrés Felipe Urrego Martínez: it is open source. Exactly.
Andrés Felipe Urrego Martínez: How is it spelled? Deep. Yeah.
Adeleke Tolulope: Deep seek Dwek seek deepseek AI deepseek R1. Yeah, it's pretty new,…
Andrés Felipe Urrego Martínez: The GPG that doesn't have web access doesn't know it because it's pretty Web GPU.
Adeleke Tolulope: but I think it has a web access. I read it they just released it not quite long.
Andrés Felipe Urrego Martínez: Here it is. DC car one web GPU.
Andrés Felipe Urrego Martínez: So then I need to use a chat GPT that actually has access to the internet.
Andrés Felipe Urrego Martínez: 40 Okay. are you getting excited yet, Steve, not yet?
Adeleke Tolulope: Yeah, I'm getting excited,… but at the same  I'm also being bothered about this model that is not really learning on our code base. Yeah.
Adeleke Tolulope:
Andrés Felipe Urrego Martínez: You're getting frustrated, but you know what you're going through. That's called a learning curve. and I always say, with the learning curves, they're important. We must go through them. but the most important thing through a learning curve is being able to learn fast and…
Adeleke Tolulope: Yeah. Yeah.
Andrés Felipe Urrego Martínez: efficiently, right? It's is okay.
Andrés Felipe Urrego Martínez: just like we were thinking about the model. How do we help it learn as fast as possible in the best way possible, that's exactly how we got to think of our learning curves as well. How do I shorten the path to learning and how much do I truly need to learn to be able to accomplish those tasks based on having AI as your assistant there. let's see. Training AI agents to assist in code generation, debugging, and the creation of new components. it's a strategic move for your startup. Thank you. I'm a very strategic CEO. given your access to asher GPU credits and the compact size of your codebase focusing on fine-tuning existing models rather than the training from scratch is so here deepse an open-source AI model developed by the Chinese startup D6 R1 has demonstrated recently comparable to open AAI's 01 model. That's what's massive. That 01 is very smart.
Andrés Felipe Urrego Martínez: It is available under the MIT license allowing free use and commercializations. This model is efficient on consumer hardware. That's really Making it suitable for startups with limited computational resources. GitHub copilot. did you guys try that at all?
Adeleke Tolulope: There's no
Andrés Felipe Urrego Martínez: Suggest in real time. It supports multiple programming languages and it can assist in writing code, debugging and learning new coding patterns. Replid. It's an AI powered coding platform that supports multiple programming languages and offers features like But that's not free or Training and fine- given your code size. Fine-tuning a trained model is ractical. Data preparation. Of course, you've done that.
Andrés Felipe Urrego Martínez: Collect and process your existing codebase including any documentation and comments to create a data set for Of course, fine-tuning integration incorporate the fine-tuned model into your development workflow. Okay, this can be achieved by integrating with your IDE to provide real-time code suggestions, debugging assistance, and guidance in creating new components. okay.
00:25:00
Andrés Felipe Urrego Martínez: Let me do this. what did you say? Have you started downloading yet working on this?
Andrés Felipe Urrego Martínez: Yeah.
Adeleke Tolulope: Deepseek. No.
Adeleke Tolulope: Yeah, I've started working on it, but I'm having some what is Package conflict in Python. the last time I tried this pipeline as well, it took me I think four hours for me to be able to bypass the package conflict…
Andrés Felipe Urrego Martínez: What? Hawaii.
Adeleke Tolulope: because that's one thing I don't really about Python though.  Python is vast as regarding if you want to build anything, Python is very very vast. But of package. they release updates as concerning each package within that.  And most of their updates if you are installing this particular package it's going to uninstall some other package that you didn't even ask it to uninstall and then install compatible package the version of those uninstalled package that compatible to what you are trying to install while at the same time what you are trying to do needs those package as well that is been uninstalled.
Adeleke Tolulope: So it took me a lot of time for me to be able to at least set up that environment for it to be able to work perfectly. So once I'm done because I like when you send that deep seek trend to the group,…
Adeleke Tolulope: I was already in the middle of a finetuning because I was already fine- tuning a particular model. So I don't want to make any changes.
Andrés Felipe Urrego Martínez: …
Andrés Felipe Urrego Martínez: you already fine tuned that other one.
Adeleke Tolulope: Yeah, I was fining another one at the point of you sending the model that train to the group.  I don't know why it's taking time to download.
Andrés Felipe Urrego Martínez: Thank Second.
Andrés Felipe Urrego Martínez: Okay, Sorry. Go ahead.
Adeleke Tolulope: So I said I was already fine- tuning a particular mode there at the point of you sending that deepseek into the group that I now decided to try that deepseek but I don't want to make any changes to the environment that I already set up that has a balanced package.
Adeleke Tolulope:
Andrés Felipe Urrego Martínez: Nice. Mhm.
Adeleke Tolulope: So once I'm done with the finetuning of what I was doing the other time, it's done now. It's actually done now.  I'm trying to test it now so that I'll be able to know how better it works how good it is before I can now say okay let me now try this deepseek because if I try that deepseek I'll be installing some new package and as well I'll go through the entire process of trying to get a balanced package for it to work.  So that's why I put an old on that particular deepseek. That's the next thing I'm trying to try out. Once I' done testing this one and I've seen If this one works better, then I think we can go from here and then just keep improving it. But at the same time, we can still try deepseek because it might be more better than this current one based on that trend that we read that we've seen today.
Andrés Felipe Urrego Martínez: Yeah, that's…
Adeleke Tolulope: Yeah.
Andrés Felipe Urrego Martínez: what I read. That is absolutely incredible. So let's see implement a structure. So when you're training Steve, I know you said we don't just give it data. What kind of stuff are you adding to it?
Andrés Felipe Urrego Martínez: So you're doing the data and…
Andrés Felipe Urrego Martínez: then what are you adding to it?
Adeleke Tolulope: Yeah. …
00:30:00
Adeleke Tolulope: initially when we started the finetuning, we are only targeting some functions at first. We are targeting some functions within our code base.  But when I now noticed that the model requires more results like more code to be able to work on. So I adjusted the code so that it read everything within every file including the import the function and every other thing that we've written into those files that are making the entire application to work.
Adeleke Tolulope: So I now pack everything and read everything and tokenize it and then pass it to the model. So that's what I'll be using now. I'm not using the selected functions that I plan on working on with before. But right now I'm now working on all the code base, everything within each file.  That's what I'm now tokenizing together for you to be able to fine tune the model because I notic that it's not like there are some import for example I said most of these functions are connected through a single line of code different files are connected through a single lines of code the first time I tried to finetune it I didn't consider those things that are connecting them I'm just trying to let the model to learn how those functions are written and to be able to help us to improve it
Adeleke Tolulope: we now see that even what we are trying to do requires those other ones at the top and some other utility function that we've written. So I just adjusted the code base so that I adjusted the code so that it compile everything and…
Adeleke Tolulope: tokenize it and so that it will increase the token as well for you to be able to train the model.
Andrés Felipe Urrego Martínez: I love that Jacob sent a message and…
Andrés Felipe Urrego Martínez: said, &quot;I'm having issues connecting since 30 minutes.
Adeleke Tolulope: Amen.
Andrés Felipe Urrego Martínez: No, you know how I am, And I'm sorry. Sometimes I sound like an a******, but I just don't like b*******, no.
Adeleke Tolulope:
Adeleke Tolulope: It might be network over here in Nigeria there was a time that there was no network for more than 1 hour.
Andrés Felipe Urrego Martínez: And that's fine, but then you tell me not at 10:04, that you've been having issues for 34 minutes. That makes no sense.
Adeleke Tolulope: So it's something that I can say is a bit possible because I've experienced it as well. Absolutely. There was a time like that the network provider went down and…
Adeleke Tolulope: everybody were complaining complaining. At first I thought maybe is my system or my data the subscription I did.
Andrés Felipe Urrego Martínez: When did this happen?
Andrés Felipe Urrego Martínez: Today.
Adeleke Tolulope: No, no, no. Yeah,…
Andrés Felipe Urrego Martínez: Okay. a while back or something. Steve,…
Adeleke Tolulope: a while back. Not once, not twice, not even three times.
Andrés Felipe Urrego Martínez: look, I'm going to tell you something. You're a good friend, I'll give you that. But Stop making excuses for Jacob.
Adeleke Tolulope: No, it's not as if I'm making excuse for him.
Andrés Felipe Urrego Martínez: I know. I'm just giving you s***. But you're a good friend. Jacob should know that I think he knows that you're a very good friend and you're trying to help avoid Jacob here. But then that means I was also having connectivity problems no, but it's okay.
Adeleke Tolulope: I don't see for example now…
Andrés Felipe Urrego Martínez: I mean, it is what it is. Not a big deal. very sus.
Andrés Felipe Urrego Martínez: I don't even know if he's in the right call. Maybe that's the problem,
Adeleke Tolulope:
Adeleke Tolulope: what I'm even trying to download there is taking more time. I'm trying to find another means of downloading it.
Andrés Felipe Urrego Martínez: He's not going to like it that I said That's very sus. Do you guys know what that people say, very suspicious. But I'm just giving him crap.
Adeleke Tolulope: Welcome, T.
Andrés Felipe Urrego Martínez: Hopefully he won't cry. And if he cries, Ty got Taiw's network is back. f***.
Taiwo Ola-Balogun: I look good good morning sir.
Andrés Felipe Urrego Martínez: Jacob, you on the call? no. Ty, how are you?
00:35:00
Taiwo Ola-Balogun: Good morning sir.
Andrés Felipe Urrego Martínez: Did you take a little nappy nap or what? Got it.
Taiwo Ola-Balogun: No back immediately I send those message to the group that I just got back from class. I've been in class all day. Yes, sir.
Andrés Felipe Urrego Martínez: Okay, welcome on the call.
Taiwo Ola-Balogun: Come on, sir.
Andrés Felipe Urrego Martínez: Good morning. Remember, if you're running a little late, if you get a chance, just let us know, because sometimes you know what I'll do is I'll say let's just wait a couple minutes so today we wait like five nobody joined so we got started but yeah I'm glad to have you here okay Steve so look what I saw here something like where' it
Andrés Felipe Urrego Martínez: Where'd it go? Okay. Jacob.
Taiwo Ola-Balogun: Yeah.
Andrés Felipe Urrego Martínez: How was your little nappy nap?
Jacob Oluwole: Hello. Thank you,…
Jacob Oluwole: Good afternoon. I just updated the app. I think was closing because of that.
Andrés Felipe Urrego Martínez: I know.
Jacob Oluwole: How are you doing?
Andrés Felipe Urrego Martínez: I'm doing good. Just getting your So, data formatting, data collection, set up the environment.
Andrés Felipe Urrego Martínez: Where did it go? I had found this thing that said there was a link to get I guess you can access the files to help train the model access the official Deep Sea Coder repository which provides scripts for fine-tuning…
Adeleke Tolulope: Okay.
Andrés Felipe Urrego Martínez: because again we know right now we need to change the mentality on we need the data to train this thing
Andrés Felipe Urrego Martínez: we know our code is very lean right I mean it's when compared to some of these tokens that we're talking about I mean 300 400 a thousand tokens for both back and front that doesn't sound too bad but then we need to understand how do we become very efficient at training the models whatever model it is we need to understand how do  we become efficient at training it and how small can we truly start?
Andrés Felipe Urrego Martínez: I mean, again, I just don't need to me something like Llama 3.3 or whatever the f*** any of these other models that are massive. And again, this is part of the learning curve, Because we're all learning. Those models are only for obviously massive companies that I mean, at that point they're not trying to develop one or two agents.  They just want an army of it and they have code for years that they can probably feed to this thing or I mean they probably fed it all in one day because They literally have no GPU constraints so that's It's really like how do we change we need to change that mentality from okay I need to train on a lot of data. we really don't because we already know how much data we have.
Andrés Felipe Urrego Martínez: So, it's how do we become very efficient at training it on what we already have. and Steve and I have been talking about this. So, obviously we start with smaller models. I sent you guys and Ty will walk me through a little bit of what is it that you're installing?
Taiwo Ola-Balogun: So yesterday when I had the meeting with Steve started with a model,…
Andrés Felipe Urrego Martínez: Are you using a model different from the ones that Steve has been testing? he's trained like 12 of them already.
Taiwo Ola-Balogun: he started with the polycoder model. So then I think he moved to a new model I think probably at the beginning of this week. But the model I was trying to use was the model was I think…
00:40:00
Taiwo Ola-Balogun: what is the name again? Yeah. Polycoder that is model but what I'm getting I've not even started training it.
Andrés Felipe Urrego Martínez: Who's trading it?
Andrés Felipe Urrego Martínez: Are you trading it or is Steve trading it? Because apparently nothing.
Taiwo Ola-Balogun: I'm seeing the process of just tokenizing.
Andrés Felipe Urrego Martínez: Do you have the tokenization part done? I mean, are you Okay.
Taiwo Ola-Balogun: is not done. What I'm getting is I'm getting lot of dependency conflicts.
Andrés Felipe Urrego Martínez: So here's why I'm asking all these questions. So, why is Taiw having tokenization problems if Steve has already figured out how to tokenize? Why if Steve had a head start?
Andrés Felipe Urrego Martínez: because we got Steve working on this for a month. Why are we letting Taiw struggle through? I mean, is that necessary? can to me it's more efficient to sit on a call and say, &quot;Here's how I tokenize. Here's the entire process of tokenization. Here's everything. go test it out and learn from it on your own and Let's f** go.&quot; Right?  I mean that's more of how I think about we learn as a team. It should and that's why I asked about are you guys trading two different models or I want you guys doing everything technically the same. you both need to get really good. So like Steve, you gota you're going to start this deep. So you're going to look into this deepseek thing, right?
Andrés Felipe Urrego Martínez: And if this is it, then we're going to set up a call where you can train Taiw on what you have learned.  That way Taiw can start learning on it and not to me it doesn't make any sense to start from scratch individually when you guys should be duplicating the efforts as a team not working on two different things but more of let's just jump on the same wagon and do this together.
Andrés Felipe Urrego Martínez: So what I'm going to have you do is for the next couple of days until we figure out if deepseek is the way we're going to go, which it sounds like it is from what we've seen so far. I was got lucky enough that I run into it yesterday. but let's get Steve to set up his system. Because here's I see Why both of you go and try and set up the system not knowing what the f*** you're doing? If one of you can do that and then teach the other and then you're both on the same Look, the way I see it is from here on as long as we can have you both on the same page on your time…
Adeleke Tolulope: Yes.
Andrés Felipe Urrego Martínez: where you're both available. You can jump on a call and then work together &quot;Okay, man. look, I'm about to te to test it on this. I want you to test it on this.&quot;
Andrés Felipe Urrego Martínez: You know what I'm saying? I want you to train it on this and I want me to train it on this. See how that makes so much more sense than two people? it's almost like you guys are working for two different companies. Remember guys, Optimize the learning curves. you want to become the top at what you do.  You want to become, the top, just coder in, that you can optimize your learning. I mean, you again, don't make the mistakes that Steve already made when you don't need to. Steve can just jump on a call, walk you through it. So, for the next few days until we get this figured out, Jacob, I want you to work with Taiw on the front end stuff, on any other bugs that are out there.
Andrés Felipe Urrego Martínez: I wanted to because one of the things that Jacob mentioned is should we pause the staging because we're not working on it. But I mean I know we still have some pending stuff. So until that happens or can we start setting up the way for where we want to go? can Tai will start working on some of the stuff that will set us up for as soon as Steve can figure this out and we can start training it and actually creating some functions or what not or I mean we don't even know if this is going to work right away. so again, maybe let's have one of you guys figure it out and then we have both of you guys use it and work on it. Jacob, what are your thoughts here?
00:45:00
Andrés Felipe Urrego Martínez: and the development. What are your thoughts? I mean, does it make sense? Yes, I know the answer to that. But I guess the next question is more if it makes sense, why are we not thinking of it that way? Go for it, Ty.
Taiwo Ola-Balogun: yesterday to have the dependency issues having, Steve said he had gone through it and he had to use an entire day to solve the problem when he was trying to do it that he was able to set up his own machine learning computer was able to set it up with the right dependencies so that I would have to have those errors anymore. But he said he have to use ship throughout the entire day to set up and I can use if I want to set up my own computer also.
Adeleke Tolulope: Sorry.
Jacob Oluwole: Are you done?
Taiwo Ola-Balogun: Yes. Yes. I'm done.
Jacob Oluwole: Thank you very much for that. from what you just said, Steve does not have a specific way for you to go to set up your own dependency and everything like you just have to you go and try it out yourself and stuff like that. I think that that one is okay as much as we are using to figure out our bugs and teaching us that where to go there is much more for us learn from what we are feeding it's not that just be copying and pasting the errors and we have to learn from it okay what modification is making to this code do you understand what modification is happening here still should be able to okay okay so he didn't figure
Jacob Oluwole: chat he respond he didn't figure out this thing now he's factoring it in okay maybe next time you have factor this code in that's your best way to learn I believe that's the best way to learn so next time even if it was that helped you out let's let us learn from it we are not just using it to use it we are using to learn as well so that we can be better that's on that note I know maybe it's different but telling you to go and
Jacob Oluwole: charge your own charg get it I think that's a bit not too good not too good but at least it should help you to get some experience on that dependency I know how stressful it can be like going back and forth at least you should be able to get some knowledge from the queries from the this is factoring in this thing let me try it out and you'll be able to know the final thing that the dependency is talking about I know AI is not our niche but we should be able to  pick up why it is showing that error and at least that's one of the things that we are learning.
Jacob Oluwole: If you are going on a learning curve if you are starting this learning you should be able to like okay why is this thing like this okay this is how you cook like this that's the way to learn you're not just to the end point of just make it work just make it work yeah we can cut corners sometimes but at least we are learning why we are doing these things so we should be able to if Jacob is running into that issue you should be able to come to Steve because he has gone through that process tell me not that go you shag agree with you too so that one on that note so I think the other end on
Jacob Oluwole: on the other side of what Andrean was saying on the other hand that I suggested that Steve had a much time going back and forth with GBT making research watching videos and everything and that you combining school and everything that currently what one thing I said was that the staging server right now nobody's testing I'm not testing on it  I think I've done that. I don't like data that is on there. I don't know if there's any update I should test out there from the password that it's just running and credit is going like we are just burning credit on that staging.
Jacob Oluwole: If we can anytime there's update that's when we push to staging that okay we test it maybe for 48 hours and we close you shut down the server that it will moving forward save us of credit because even if you are using staging if you're not using staging is still running still burning credit we are still spending more money on credit so moving forward I was suggesting to that maybe we stop staging server anytime we are not testing on it if anytime there's no update on staging server and
00:50:00
Jacob Oluwole: I was like okay instead of two developers one is making progress and the other one is still struggling with bugs and we know that you in school and everything if we can start maybe there was some time and was talking about having to have a page that we see bugs on us having our own flow of admin panel admin dashboard if you can convert the staging to another branch of admin even…
Jacob Oluwole: if you want to keep that staging running you can have a URL that will be like an admin dashboard whereby can log into anybody. But yes, so that
Andrés Felipe Urrego Martínez: an admin dashboard for us on the to be able to see everything we want look it should be kind of like and…
Andrés Felipe Urrego Martínez: and guys think of this I mean because Jacob has a very good point there even what if we had think of it like a GPT or just to simplify it just to make something simple that we can ask things to based on our database.  So for example, hey tell me how many current employees do we have? It'll go to the database and re give you the number. How many candidates? How many companies have an active job? And it returns these companies have an active job stuff like that that we can and again that's just me thinking of a simplified way so that we don't have to create this massive front end u UX right?
Andrés Felipe Urrego Martínez: I mean just how simple can we make this for us to just be able to and again yes I mean it would be important for me to have something that we can log in and for example look at okay Zachary jobs I want to go to Sakuri and I look at Sakur and it will tell me Zachary has 10 jobs and these jobs are this and these are active these are closed these jobs have these many applications and then if I want to go to a candidates page and then look at it I can also do that but from an admin point of view rather than just another user. What do you guys think of that?
Jacob Oluwole: I think all you're saying is that you should have AI charts whereby you can link to database that can get all the data that you need how you want it feeding our database and everything.
Andrés Felipe Urrego Martínez: Yeah, I mean that I'm just trying to think if that's a simplified way of the dashboard that we need. we can create our dashboard or get our answers based on connecting that GPT to our database. And again, you guys know how I am. I'm just spitting s*** out and trying to see if any of it is something that would make sense. but to me, I mean, because what do you guys do when you go to the database, you have to manually search everything inside of the database. you have to write your little thing that says show employee. I guarantee you that there are ways to probably do that already.
Andrés Felipe Urrego Martínez: It has to search directly from the database and be able to get some data or just building an actual dashboard from the get-go. I'm just trying to think what is the fastest way and then we build from that.
Andrés Felipe Urrego Martínez: What is the most efficient way for us to build anything as far as an admin dashboard? and then we build from that. but what is the most simplified way I guess is my thought.
Jacob Oluwole: I don't know.
Jacob Oluwole: I like most people way I know you talked about the AI knowing that means that probably I still haven't gotten the process of like that. Maybe we still be feeding it with our data on database all the information that stored on our database so that we can know what and what all the tags and everything.
Jacob Oluwole: I still believe that that will still take much time training and all just feeding database and so that you can national processing that NLP whereby you can type okay jobs and…
Andrés Felipe Urrego Martínez: No, no,…
Andrés Felipe Urrego Martínez: no, no, no, no, no, no. But I'm thinking
Jacob Oluwole: it feeds you the jobs get me the one that are closed okay these ones are closed this one are closed and everything and they will still be like training
Andrés Felipe Urrego Martínez: Jacob, but okay. But before we say no, I mean I want us to look and see if that is something that MongoDB offers a way for us to search and be able to print results in a more efficient way than what we do today. I mean to me it's crazy honestly  To me, it's pretty crazy that I have to message you guys and someone has to go in there and then do your search and then save print it. I mean, there has to be more efficient ways that companies are consuming their data. It can't be that manual. I don't know.
00:55:00
Jacob Oluwole: What?
Taiwo Ola-Balogun: I think I've seen that sort of series from I saw it for I think I'm trying to remember out base that was the name out base…
Taiwo Ola-Balogun: but I think it was for SQL and progress and Postgress database that they were doing it for but it's not exactly like pass in the database inside the models.
Taiwo Ola-Balogun: So all they have to do is try to get a query that is able to get the data that they need. So they work more with the query than with data.
Andrés Felipe Urrego Martínez: …
Andrés Felipe Urrego Martínez: then let's Yeah.
Taiwo Ola-Balogun: So what the generates is the query and not the data.  So it's based on that they send that query to the database now get data.
Andrés Felipe Urrego Martínez: So what I'm hearing is we're going to look into We're going to look into it that there might be some options there. yeah, I honestly guys again the most important thing here is how can we get a dashboard as soon as possible and what are the best options? Yeah. And then we can work on that. but again I guess when I say that it should be obviously something we can just simplify the way we search on the database because that way you guys will be able to create something simple and not something that is a dashboard and we have 10 different pages.
Andrés Felipe Urrego Martínez: company search or whatever something like if I look for Zachary construction then I can open it up I can see modify do whatever I want with the company and jobs obviously that's only something that we have that we have access to sorry if I want to give a credit to someone or does that make sense can you guys  hear me? I'm making
Andrés Felipe Urrego Martínez: There.
Jacob Oluwole: Yes, I can hear I get what you're saying. T has said he said I was thinking about maybe we have to visit our data base and everything.  said that it's not concerned about the queries and most of the time when I go to database I send query and when they even on the production on staging they send query to the database and database just return the result of the query so that means that if you are to have a simple chart like that you'll be working with queries of training the AI about queries
Jacob Oluwole: that can be sent to database and everything like get that stuff. I don't know how long that would cost but
Andrés Felipe Urrego Martínez: fast, after we get off the call, he can jump on what on Chad GBT, start asking &quot;Hey, tell me more about this. How much does it cost?&quot; Or go to the website, look into it, kind of get an idea of not I always say, let's look at what it would imply, what are the options, and then we start building something, right? So, let's read little bit, not lot, just a little bit of is this something viable? Can we use it? Will it cost us a lot? If it doesn't then we move forward. so yeah let's see let's see what happen and then keep me posted and…
Jacob Oluwole: All right. Who's
Andrés Felipe Urrego Martínez: if not then we just build something very simple. we just go with a traditional model for now. and then just as long as we can get something soon that we can use
Andrés Felipe Urrego Martínez: All are we all on the same page? I mean, let's remember, we got to move fast. So, we got to pick a model. We can't and I mean, of course, we're going to make more mistakes. But when I say we can't make any more mistakes, I mean let's make sure that we're picking that model that we're going to use. Even if we look into it a bit longer. That's okay. But I would say honestly from what we've seen, even for offline this model that we're looking at right now might be a good option. So let me know Steve keep me posted.
01:00:00
Andrés Felipe Urrego Martínez: Tyo Jacob work together on can someone please share? Jacob, I noticed you're on your phone.
Jacob Oluwole: Yes, I am on my phone.
Andrés Felipe Urrego Martínez: Ty, are you on your PC? Can we go over the stuff that Ablad sent, please? …
Taiwo Ola-Balogun: No. So, I'm on my phone.
Jacob Oluwole: on PC.
Taiwo Ola-Balogun: I'm on my phone.
Andrés Felipe Urrego Martínez: he on the phone. It doesn't matter. Just on PC will look better because he looks bigger. But
Taiwo Ola-Balogun: I haven't checked it out. I think I just woke up a few minutes ago. So, it's probably when I check it out.
Jacob Oluwole: If you hold on for three minutes,…
Jacob Oluwole: I can switch on my PC.
Taiwo Ola-Balogun: Thank you very much.
Jacob Oluwole: So, is that okay? Is that fine?
Andrés Felipe Urrego Martínez: Yeah,…
Andrés Felipe Urrego Martínez: sure, I think so. I mean, yeah. Yeah.
Jacob Oluwole: I'm just
Andrés Felipe Urrego Martínez: Because I just want us to review it. I want us all to be on the same page. I prefer when you guys share because then you make your notes, what needs to change,…
Jacob Oluwole: All right.
Andrés Felipe Urrego Martínez: and then I can move on. So I think I told you guys a while back when I went and met with the congresswoman here she referred us to the CEO of workforce capital solutions. they have been awarded a 15 to20 million contract for workforce development from here for the next five years.
Andrés Felipe Urrego Martínez: So, I'm meeting with the CEO today with a direct referral from a congresswoman, someone in the government. So, guys, I mean, this is this I hope fingers crossed. I won't f*** it up and it's a very very good opportunity because this would really open doors. mean, this could really open doors for us. So, I've done some research on her, as far as what kind of initiatives have they're looking at.  She just took a course on AI at the beginning of the year. So that's going to be very good. literally just January she just got the certificate she posted on her LinkedIn.
Andrés Felipe Urrego Martínez: and she's all about so let me show you guys the link and I want you guys to open it up whether it's on your phones or your computers and tell me that this doesn't sound like mo but let me man but not an online or AI solution. but let me show you guys. So, I just shared the link. They're all here on the Google meeting. so you guys see, look, we provide specialized services at no cost, including career training, apprenticeship programs, scholarships, job search assist childcare assistant, tailor business solutions, and more. Use our free online job resource tools and get access to thousands of local and statewide jobs.
Andrés Felipe Urrego Martínez: Employer services. Our tailor solutions at various levels of support can assist you with awareness, raising, training, replace placement, and upskilling. about so let's see you guys
Andrés Felipe Urrego Martínez: look, we are a private publicly funded nonprofit responsible for the data-driven planning, oversight, and evaluation of workforce development activities in Austin, Travis County. Simply we connect local people to the most in demand industry with quality jobs. Look their vision. Everyone in our region can build a career and every employer can hire local diversity leadership. To leading the development of our world-class workforce. I mean Are you guys reading it? I mean I don't know.
01:05:00
Andrés Felipe Urrego Martínez: I mean, it sounds pretty** in line with what we do. and I think they want to use or they might want to use. So, I'm going to bring up AI work learning and development because obviously they're all about workforce development,  So I'm going to say, that as part of once we can start getting these AI agents trained and start creating our AI assistance that it will allow us to eventually include that learning and development through avatars. But of course, to get there, we're going to have to raise a lot of money. but this is great, This is great. This is great.
Andrés Felipe Urrego Martínez: Very good opportunity. I mean literally someone from the government put us in front of these people and said I want you to talk to him because I think you guys have a lot of to work with. so the congresswoman told me that they were looking into AI to see how they could better do the job matching and everything. So again we'll see what opportunities are here for us. but I think Maybe they buy out of that 15 million, what did they gave us two? We'll grab the money. I'll grab the money and then not talk to you guys anymore. No.
Andrés Felipe Urrego Martínez: I'm joking. Steve immediately stopped. I love it because as soon as I said that, Steve was doing the little thumbs up and then he immediately stopped. He's like, &quot; f***.&quot; no, no, no. But if we were able, imagine we sold the company. guys, we would start three more.  Honestly, I would give you guys money, pay you guys out, dada, and then we would grab our team, and then from that team, we would start three other companies, We would literally hire people for three different companies. Give us a two mill. Let's do this. I mean, I love what we're doing. it's still going to be in line with helping people, but then what we do is we sell the mo the way it is and then we go and build a learning and development or we go and build the assistance or, I mean, we'll see.
Andrés Felipe Urrego Martínez: or we just work with them and then we have literally job postings for the next five years all of them in Austin and then an opportunity to work directly with them to do the learning go and teach classes for them through their organization get paid for that and then obviously build solutions  that are white labelled. all right. Let me look at what's happening? How do I there we go. Okay.
Jacob Oluwole: What do you say about I think this lady?
Andrés Felipe Urrego Martínez: No,…
Andrés Felipe Urrego Martínez: that's not cool.
Jacob Oluwole: No,…
Andrés Felipe Urrego Martínez: You guys like Heyo or what? No,…
Jacob Oluwole: I don't like it. Do you? Yeah. So…
Andrés Felipe Urrego Martínez:
Andrés Felipe Urrego Martínez: not at all. Hi. …
Jacob Oluwole: what could be replacement? Hello.
Andrés Felipe Urrego Martínez: you're not talking to us. no. No. No. I would just say maybe welcome this is not a conversation with a person it's not like hi how are welcome hey yo that's funny I love it because you said hello but you were just typing out loud and then I was like hi and then you changed
01:10:00
Andrés Felipe Urrego Martínez: did because I thought I was,…
Jacob Oluwole: I feel this is too desty up now.
Andrés Felipe Urrego Martínez: I was talking about another one. all Very So, they sign up with Google, then if they click on that. Let me see. Okay. Yeah. Let me see. no, it should Yeah. Yeah. Yeah.  It should just be I mean people know what they're about to sign up for. Maybe what we do is this should be an space to explain why we have two options, it should be please select one of the options below and then right below Google, we'll say by selecting this option. Yeah, that's what we should do. We should take all that text out and just say Please select one of the options below.
Andrés Felipe Urrego Martínez: And then we're going to use the text to say, select this option to use a Gmail account or sign up with your email address or phone number.  And then right below that above that we say select maybe we make it email address or phone number and then below it we'll say sign up with this option to use email or phone number. Does that make sense?
Andrés Felipe Urrego Martínez: I just be very clear about what people need to do and I know it's clear for us but it's not for people and we've noticed that we've seen literally a lot of friction in this area because people have no idea what they need to do. So I would remove the text and then just And then just Okay, so send that and then I want you to put one at the top and then kind of let him know Can't you just remove it?
Jacob Oluwole: No thanks.
Andrés Felipe Urrego Martínez: No.  Yeah, I think you might be able to just if you double click on it. doesn't it just allow you to delete that text and then we just type it in because that's going to be too confused. There you go. So, just delete all of that if you can. Ask to edit. there you go. That's yeah, it's going to be a lot easier to just explain it to him. But, yeah, maybe just another bubble that says remove all this text from the top box from that one. So, remove this text and replace with
Andrés Felipe Urrego Martínez: Please select one of the options below to get and then Very good. Yeah, you can also select these options. Go ahead and remove that. That makes no sense. Yeah.
Jacob Oluwole: Yeah, He knows this one. Please.
Andrés Felipe Urrego Martínez: remove that and then re above the sign up with Google, we need a message Where you above it, we're going to do one dot Select this option if you to use a Select this option to use your Gmail account. One dot. Are you there? Okay.
01:15:00
Andrés Felipe Urrego Martínez: a Google account and there you go. and then Done there.  And then above sign up with email address, we're going to do two. Select this option to sign up with other email or phone number.
Jacob Oluwole: This is just mobile  Same screen. Yeah.
Andrés Felipe Urrego Martínez: There you go.
Andrés Felipe Urrego Martínez: I mean, that's very like instructional. We're literally walking them through what they need to do. All right. So, let's go look and see what the rest looks like. Sorry.
Andrés Felipe Urrego Martínez: It seems like a lot of changes, but it really is just the wording. very good. Yeah, that's perfect. Yeah, that's exactly it. So, email address or phone number. Very good. So, then if they do email, it verifies their email. And if they do phone number, it verifies their phone number. Okay. Okay. What do the pop-ups look up look like for each option?
Andrés Felipe Urrego Martínez: So, I assume you boom sign up and then we have a popup that says you will receive a code.
Jacob Oluwole: Yeah, we have that.
Jacob Oluwole: We have that one. for the phone number for yeah I think I will tell him we can't use about it I think he assumed that we already have a component that verifies people's phone number…
Andrés Felipe Urrego Martínez: Yeah. No, no, no. I know we have one, but this is different because now we're verifying a phone number. so that's what I always say when I say linear thinking that's exactly what I mean. We're literally …
Jacob Oluwole: because we talked about it but I never like using the
Andrés Felipe Urrego Martínez: but there is a popup when this is done right that says we have sent you an email or…
Jacob Oluwole: using that.
Andrés Felipe Urrego Martínez: right so I don't know if what are we going to do are we going to shoot out the popup depending on the method they use or just a message for both either one that just says we have mean So how do I verify the phone number? And if I select email, how do I verify my email?
Jacob Oluwole: We are selecting the number the message has been sent to their WhatsApp on their WhatsApp. So the code is being sent on their WhatsApp.
Andrés Felipe Urrego Martínez: Only WhatsApp
Taiwo Ola-Balogun: No WhatsApp.
Jacob Oluwole: Yeah. Welcome
Taiwo Ola-Balogun: I think this is it.
Taiwo Ola-Balogun: No, the code is sent to your WhatsApp for no US numbers.
Andrés Felipe Urrego Martínez: But wait,…
Andrés Felipe Urrego Martínez: why only that?
Taiwo Ola-Balogun: So I want to explain is sent to your WhatsApp for Non US numbers.
Andrés Felipe Urrego Martínez: Got it. But then he sends a text message to US phone numbers.
Taiwo Ola-Balogun: Yes, Yes. Yes, sir.
Andrés Felipe Urrego Martínez: Per That's perfect. I love it. So, if I selected phone number, is there a popup right now that tells me to verify the phone number? No, no, no. Yes. Yes.
Andrés Felipe Urrego Martínez: But what I'm saying is in the process in the logic that you guys have right here,…
01:20:00
Jacob Oluwole: I think.
Andrés Felipe Urrego Martínez: the popup will pop up to require for me to put in my code that I got in my text message.
Jacob Oluwole: Yeah. Yes.
Andrés Felipe Urrego Martínez: And if it was email, then the email popup would come up and say, &quot;We have sent you an email. Please verify it and log in So, that is the logic that we're using now, Correct. that's and…
Jacob Oluwole: Yes. No,…
Andrés Felipe Urrego Martínez: this has been built already on staging.
Jacob Oluwole: no, no. It's just been designed. T will go and…
Andrés Felipe Urrego Martínez: No, no,…
Jacob Oluwole: Yeah,…
Andrés Felipe Urrego Martínez: but Taiw had already worked on the process of the text messages.  So what I'm saying has that been like it does this process do you showing me right here reflect that? Okay.
Jacob Oluwole: kind of.
Jacob Oluwole: It's just a little trick initially it was different pages but right now it's now on a page and it's just like a trick to the code basically I'm guessing that is it like a trick to the code you have to like because now single boss is representing both phone number and email so I think they will figure it out they said it's possible to have both phone number so I'm sure this is the only trick that is going to be there because  email and phone number they kind of like having the same boss.
Jacob Oluwole: So they will know how to detect if this is a phone number and how they can detect if is an email.
Taiwo Ola-Balogun: I'm doing that already. So, what I'm to get is a phone number is the plus and what I'm to give is an image is the app.
Jacob Oluwole: Welcome Yeah,…
Andrés Felipe Urrego Martínez: Guys, can we when…
Andrés Felipe Urrego Martínez: because we're missing the country selection there for the phone number. we don't.
Jacob Oluwole: we Can't put it there though because we don't want them to use phone number. We don't want them to use phone number. We don't want to refute them to using phone number. You don't want to refute them using phone number.
Jacob Oluwole: if you had a phone number column there, they might just be wired to using phone number to  Thank
Andrés Felipe Urrego Martínez: No, no, no. Yeah, that's what I'm thinking. Yeah. I mean, but I mean, we're gonna verify the message anyways once they're in. So, I mean, I don't give a s***. I mean, but yeah, I mean, no, I yeah, but then there's no instruction there that tells them they have to type their area code. and that's going to over complicate things. Yeah, that's a lot of errors waiting to happen. you know what I'm saying?
Taiwo Ola-Balogun: Yes sir, I perfectly understand what is happening there. Most people might not know that they need to put their country code Unable to send a message to verify them.
Andrés Felipe Urrego Martínez: so what do we do? I mean, I mean, because Jacob has a good point. He says, how do we do? We just put the area code there and if they put an email, that's fine. I mean, that's going to trigger an error. I just think there maybe what we could have done is just there's two options and they select one and then we open the box for that specific one. Does that make sense? So you got under that option once people click on that it opens up and then there's the two little options side by side.
Andrés Felipe Urrego Martínez: You click on one and then it opens the phone number box. Or if you click on the email one, it opens the email box again.
Jacob Oluwole: number. But that is a piece of text that It should begin with their country code.
01:25:00
Andrés Felipe Urrego Martínez: But that's exactly why I said no because that's over complicating you're asking hundreds of people to have to do a manual process when we can fix it through code.
Jacob Oluwole: I do.
Andrés Felipe Urrego Martínez: I don't understand why wh…
Jacob Oluwole: Yes.
Andrés Felipe Urrego Martínez: why the reluctancy to just you select the option and you have clearly two items very clean looking and you select one of the items and then you select phone number and it's going to show you exactly what we've set up for them here phone number option or…
Jacob Oluwole: Okay.
Andrés Felipe Urrego Martínez: and the passwords and then they sign up or if they click on right next to it on that tiny little box that says email…
Andrés Felipe Urrego Martínez: then it just shows you an email box phone number and then the passwords and then sign up I mean that to me is simplifying the process for people rather than adding barriers to Look,…
Jacob Oluwole: I think I've seen…
Jacob Oluwole: what he's saying. you can have it separate just change that text.
Andrés Felipe Urrego Martínez: let me show you guys exactly what I mean. can you Okay.
Jacob Oluwole: So once they click on email this type of text that is currently on the screen and they click on that phone number we add that country code to it like this from here now this one I don't know why my PC is hanging
Jacob Oluwole: Okay, hold on. Yeah.
Andrés Felipe Urrego Martínez: Let me just show you something real quick. Is there something on the screen you guys Hello. You don't
Andrés Felipe Urrego Martínez: It's on the call it says collaboration dashboard or something. No. one person joined I think. Does he have to let you in or what? I don't Okay.
Andrés Felipe Urrego Martínez: I want to show you guys, but I don't know how to Let me see. Yeah. What I'm looking for, guys, is something very simple. Again, you select on the second option, which we already have there, and then the first thing that shows up is two little pills just like the ones that we have for experience. and all the other stuff. Those little round pills that are purple. Two of those. one says,…
Jacob Oluwole: I'm suggesting that's what I'm thinking too that I've thought about it. So, don't worry. I'll walk it back.
Andrés Felipe Urrego Martínez: &quot;Okay.&quot; Yeah.
Jacob Oluwole: We'll get that.
Andrés Felipe Urrego Martínez: I just want to make sure we're on the same page. We have the two pills. You click on the pill and then it just shows I mean, we already have all of that. We just need to add the two pills and then copy paste the boxes and then one populates a phone number with area code option and then the other one populates an email box.
Jacob Oluwole: Yes. Yes.
Andrés Felipe Urrego Martínez: That's all makes sense,…
Jacob Oluwole: Yes Yes, sir.
Andrés Felipe Urrego Martínez: I mean it's clean.
Jacob Oluwole: Stop. oh.
Andrés Felipe Urrego Martínez: People can't go wrong.  I mean, if we can't get the sign in if we can't get the signing sign up process right, guys, we have a massive problem. we're in guys. we're in a lot of trouble if we can't get that right because that's how we achieve customers.  And obviously this has to populate both for user and business, another thing that we're going to need either now or later and we talked about this is a main user for the business accounts and then hopefully an option to add users to a business account. Think we talked about this when we had that call with Zachary.
01:30:00
Andrés Felipe Urrego Martínez: So again I don't know how complicated that is but I think we talk about just creating hierarchies within the companies and then just giving people access create a user and then that should be just something that by sending the email they log in they change their password boom they created an account and then now they're under that business then they have access to either read or admin I don't know. Again, I don't know how long that would take or how complicated that is, but I just think that that's something that we're going to need. all right, integrating tool. Okay, guys. What else? Jacob, was as far as the updates from you wanted to show me from ABLA?
Andrés Felipe Urrego Martínez: Was that it?
Jacob Oluwole: That's everything.
Andrés Felipe Urrego Martínez: All right, guys. I'll let you go. Thank you for your time. I appreciate you very much. if anything comes up, please If any questions come up, please let me know.  again, let's make sure that we continue to push and switch that mentality to we learn fast, we work fast, we learn fast, we work fast, we learn fast, we work fast. We're doing great things. I mean, I believe all of you guys are doing great things. you guys have been, focusing on the learning process as well. That's really really good.
Andrés Felipe Urrego Martínez: Before I let you guys go, let me change the Nvidia sign in options.
Jacob Oluwole: Yes, please.
Andrés Felipe Urrego Martínez: Let's see. So that you guys can sign in, at least the developers can sign in and start. Jacob, remember what I said? I really need you on this end. so I'm going to have the developers for now be the ones that hopefully focus on that learning on the Nvidia thing and I can work on that soon. let me see here.
Jacob Oluwole: Thank you.
Jacob Oluwole: I don't know.
Andrés Felipe Urrego Martínez: Okay.
Andrés Felipe Urrego Martínez: So, we need to remove the authenticator code, right? You guys have the password. We just need to remove the authenticator.
Andrés Felipe Urrego Martínez: Okay, very good. Sounds good. all right. let's see. Account come on. Yeah, we need to remove this. So annoying.
Andrés Felipe Urrego Martínez: 616 616 363
Andrés Felipe Urrego Martínez: Can someone please go ahead and try and log in real quick to that Nvidia account? See if you're able to, Thanks y'all. Just let me know. hold on. should be
01:35:00
Andrés Felipe Urrego Martínez: Okay, here's the password. You guys should have no problem learning it. I just sent it on the WhatsApp group
Andrés Felipe Urrego Martínez: Okay, It asked you to have the email verified, right, Jacob?
Jacob Oluwole: No, no.
Jacob Oluwole: I'm still looking for the link. So I'm coming.
Andrés Felipe Urrego Martínez: No, it's not going to send you a link.
Andrés Felipe Urrego Martínez: It sent it to me because it's my email account and I just Yeah.
Jacob Oluwole: No, very nice.
Taiwo Ola-Balogun: I've verified it. I've been able to log in.
Andrés Felipe Urrego Martínez: So yeah, I just say you just logged in using iPhone device. We haven't seen you in recently. this was you in Logos. So I verified that whoever that was.
Taiwo Ola-Balogun: I was one
Andrés Felipe Urrego Martínez: So that remember you have to andab.com
Andrés Felipe Urrego Martínez: So, you guys got in. Didn't ask you for anything else. We're good to go. I can't hear you.
Jacob Oluwole: So that  My top.
Andrés Felipe Urrego Martínez: Did anybody else hear what Jacob said? I couldn't hear him.
Taiwo Ola-Balogun: No, I think
Andrés Felipe Urrego Martínez: All right, guys. let's just jump off the call. If you guys have questions, please, let's focus on getting as much as done possible this week. let's push as much as we can. Steve, keep me posted, I really need those updates, guys. I know for you guys it just seems repetitive that I ask for him every morning. Again, if it's repetitive, it shouldn't be.
Andrés Felipe Urrego Martínez: I shouldn't have to ask for them. Just post them on there. throughout the day, Steve, right now that you're going to be doing this DeepS thing, keep me posted. I want to kind of know updates throughout the day. and then see how I can help so we can move a little bit faster. All right.
Adeleke Tolulope: Okay, sir.
01:40:00
Andrés Felipe Urrego Martínez: Thank you guys. I really appreciate you. I'll talk to you soon. Take care.
Adeleke Tolulope: Yeah. Bye-bye.
Andrés Felipe Urrego Martínez: Bye-bye. Thank you. You too.
Meeting ended after 01:40:23 👋
This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

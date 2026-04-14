# Team Meeting 2025-01-29 - Transcript

**Source:** OneDrive transcript
**Date:** 2025-01-29
**Original file:** Team Meeting 2025-01-29 - Transcript.docx

---

Team Meeting - 2025/01/29 09:29 CST - Transcript
Attendees
Adeleke Tolulope, Adeleke Tolulope's Presentation, Andrés Felipe Urrego Martínez, Jacob Oluwole, read.ai meeting notes, Taiwo Ola-Balogun
Transcript
Adeleke Tolulope: our code.
Adeleke Tolulope: Hello, are you there?
Andrés Felipe Urrego Martínez: Yeah, I'm here.
Andrés Felipe Urrego Martínez: I'm listening.
Adeleke Tolulope: So I have to create the data set in this format, For example, I'm following this one say create a simple flask project with Docker, right? I wrote the project name this and…
Adeleke Tolulope: There's this files right inside these files it now has some list of things like for example this main.py Pi. this is the content that should be within the flag. Pi. Do you get that? So I can factor our data set in this structure. Right? Are you following me?
Andrés Felipe Urrego Martínez: I am
Adeleke Tolulope: So if I can factor our data set in this structure, I put the necessary parts and I put the actual content there.  then the model will be able to know that this content should be within this file.  So now if I now want to prompt it when we are done training it, it's going to return the response in this format to me. It's not as if the model is the one creating the necessary file and writing the content. All what it's just doing is that it will create the part right and create the code and create content. Then from the script that will be running the model through, right?
Adeleke Tolulope: the script will be the one to be writing them into their respective files for file project file over here for example this is the code once I'm done training the model right this is this function that calls the model I already pass the prompt what maybe for I want I want it to create a new set of features for me those features will be within this prompt right then the model will  They want to b on those prompts and structure them in The appropriate way that it should be just like It's going to structure it the content then once it's structured like that it's going to return it back in a JSON format. Right?
Andrés Felipe Urrego Martínez: Memorial GPT.
Adeleke Tolulope: Then this will be the function that I will now be writing based on the respon model. so now this is the function I said pass the information to the model then the model will return the structure into this project. Right? Then I'll now read each file from the project.  Then I'll now write the file accordingly accordingly right so that once I get back because the model cannot extensively access each of the like cannot create file I don't know maybe you get this what I'm trying to say the model can only give you in the appropriate structure that it should be so it is this function right that now follow the steps provided by the model the things that should be in
Adeleke Tolulope: the should be in the right content then it is this function that will now handles everything right then once it's done once I get back once we now integrate the model into our ID right I'll just prompt there will be a single file like this right the file will be communicating to the model and the model will create the complete structure of how it should be within the code base then this function will be the one to write them out just like if you
Adeleke Tolulope: If you print RGB now to be writing some stuff out when writing is not actually the model that is writing those content right was they already programming so that if not writing the contentah something like that in an increasing manner it's not the actual model that writing based on the user interface so that's what I'm doing now I'm now trying to structure though I already train it with our code base in a full view of the code base…
Andrés Felipe Urrego Martínez: Got it.
Adeleke Tolulope: but now I'm not trying to target it towards what we actually want it to do. so that means I based on what I've based on my finding so far for example if I'm working on the back end if I'm giving it a back end what is it a back end prompt it should be in the appropriate manner if I'm giving it a front end code the way it should create it based on our current folders based on our current files that we've created such that it will just for example maybe we've already created
Adeleke Tolulope: a folder like this that name jungle_ pi so that even if I'm training the model it's supposed to add to the code within should make a change for me within this function within this file if I didn't feed it how our codebase folder structure are right is going to create a new set of folder right and then write whatever I want to write into it except if it's a new feature that even if we are to manually create it ourel we will start writing some new new folder…
00:05:00
Andrés Felipe Urrego Martínez: Very good.
Adeleke Tolulope: but if maybe you want to make an update to a particular feature then it know that this folder already existed then it just go into the folder then write whatever you want to write there and then that's all.
Andrés Felipe Urrego Martínez: Very good.
Adeleke Tolulope: Creating the Yeah.
Andrés Felipe Urrego Martínez: So, right now you're working on putting together the data set, right? And…
Adeleke Tolulope: I'm putting on the data set. Yeah. Okay.
Andrés Felipe Urrego Martínez: how long do you think that's going to take?
Andrés Felipe Urrego Martínez: What are the challenges just that you might be facing with it?
Adeleke Tolulope: Let me just show you This is the code base. I just want to explain it for you. Okay, this is the back end.
Andrés Felipe Urrego Martínez: I'm four.
Adeleke Tolulope: Are you there? So this is the back end.
Andrés Felipe Urrego Martínez: Yeah. Yeah. Yeah. I just said Yeah. Please explain it to me like I'm foreign.
Adeleke Tolulope: Okay, this is the back end folder structure. Now we have the bin which consist of the configuration of the domain and the calls. We have the controller, right?  for each of the files indeed we have the structure how we want to save it into the database all this stuff so what I'll do now is that for example to start with admin function or if I'm to start with maybe employee function right I'll start from here for example I'll create now the part will be employee function right it will be controller/ this one
Adeleke Tolulope: just like this one Django API/ defile right so it now be controller slash this and then I'll now put the content of this one all this thing will now be inside the content I think you are following this is  activity. So it not be inside this content. So I have to create it. For example, if I want to do just for posting a job only, it's not as if is to create a full project like new features. For example, if I want to train that okay, I want to create A full job posting for me.
Adeleke Tolulope: I will just come here then after giving the prompt then it start from the this job controller right that's content then it now proceed to the service slash the job function which actually contain the business logic after that it now contain the router file to handle the end point if you are posting and no so that's what I need to do for this entire back end application. So we have I think maybe 14 files like that that I have to structure.
Andrés Felipe Urrego Martínez: And you have to manually do this is what you're saying and…
Adeleke Tolulope: Yeah, I have to manually do this. There's no way I can I already try to make use of activity is just even changing some box on code for me and even adding box to the data set. So I have to manually do I have to manually set up I've already done some research on that I even reach out to a community is there any fast way that we can create a data circular to a particular feature.
Andrés Felipe Urrego Martínez: have you done some research on if there's any possibilities of doing it that way? Just understanding if there's any way of doing it. Nice.
Adeleke Tolulope: So they were now saying that even if we are to mix up AI AI change your codes can do them in a rough way and if it has already done it…
Adeleke Tolulope: if it has already done it the file will be much enous that you yourself won't be able to start going through it one after the other to know maybe the structure or the content are actually correct.
Andrés Felipe Urrego Martínez: You're going to have to review it once he's done with everything.
Adeleke Tolulope: So I don't know you get what I'm trying to say. if you check this file now if I ask to create this number of rows for me and then once it is done I now have to start confirming it from the very beginning when will I be done with everything and even once I have to review it to be able to train the model correctly because I already tried it and…
00:10:00
Andrés Felipe Urrego Martínez: Of course.
Adeleke Tolulope: I realized that all this AI they are changing the codes.
Adeleke Tolulope: Or they call short on code truncate on code if they
Andrés Felipe Urrego Martínez: And are you saying…
Andrés Felipe Urrego Martínez: what does the prompt look like? And I'm just asking it could be that it doesn't know how to, So I don't know. try asking the actual DeepS website, and see what you can achieve. but what I would say is that whenever it's complex tasks like this, make sure you're giving it the example, which I'm sure you are, You are giving it an example and it's just still failing to give you the correct answer.
Adeleke Tolulope: deep sync. So, yeah,…
Andrés Felipe Urrego Martínez: You do?
Andrés Felipe Urrego Martínez: I haven't used it yet, on my end, but I have heard of people saying that it does really good with code,…
Adeleke Tolulope: I have it. let's test it out. Let's test this out.
Andrés Felipe Urrego Martínez: but I don't know. I haven't tested it.
Adeleke Tolulope: Okay, let me see which charity. Okay.
Adeleke Tolulope: Okay, let me bring this. Does not have the necessary part. How can I add the part to it? It was only returning doesn't return in The file okay I can see okay there
00:15:00
Andrés Felipe Urrego Martínez: What's happening?
Adeleke Tolulope: Some content are very long. So that even while the AI is doing it, it will run out of what you call token that will just stop halfway and you now have to start tracing it to where completely before the correction that you need to do after. So the stress is just too much when I try to use AI stuff.
Andrés Felipe Urrego Martínez: Okay.
Adeleke Tolulope: But let's see the result of this deepseek. Are you trying to figure out that and also I'm also thinking of training the model such that it's at least like in a text now not even to write Like I was thinking that maybe we should have a full scope of what Mo is into right so that we can even prompt it based on what Mo does what we are doing at Mo or something like that that be able to respond better as well.
Andrés Felipe Urrego Martínez: say that again that he would do what?
Adeleke Tolulope: I was thinking of it while when I went out server is busy.  Please try again for example if you ask some related question as relating to maybe open AI is going to give you some feedback and all.  I was also thinking that since we are trying to target this model to work for us as to understand our code base and to be able to write code and even if we are asking any question relating to Mo to be able to give us the right what is it called the right response for example we have a full page or a full page or in sentence or in paragraph that consist of that contains everything that we are doing at Mo right  the services we are rendering and everything that we are doing so that we can train the model on that as well.
Adeleke Tolulope: So that even if we are asking the model some partial question it be able to generalize it based on the information we already fed it that we are trying to do and based on his knowledge of the code base as well be able to perform better as well.
Jacob Oluwole: Hello everybody. Good morning.
Andrés Felipe Urrego Martínez: Jacob, how are you?
Adeleke Tolulope: Thank you.
Jacob Oluwole: Very good. I hope you're doing well.
Adeleke Tolulope: Are you asking? Sorry. No,…
Andrés Felipe Urrego Martínez: Thank you guys. Did you say something, Steve? …
Adeleke Tolulope: I think Jacob was asking you question.
Andrés Felipe Urrego Martínez: yeah. I'm sorry. What was the question, Jacob?
Andrés Felipe Urrego Martínez: Thank you very much. I'm doing good. It's been a little bit busy,…
00:20:00
Andrés Felipe Urrego Martínez: end of monthly but Things are good.
Adeleke Tolulope: This morning I stumbled upon one particular trend on…
Adeleke Tolulope: what is it called on X the guy making use of GPS to create a brief agent making use of some platform and that agent is able to respond  phone to your email. For example, if you ask me that, get me the last email I receive and reply promptly to the person, then the model is going the little thing that he did within that video. The model is able to look at lo into his email account, get the last email, and even be able to and even responded to the last email content he received.
Adeleke Tolulope: So I plan to try it out this morning but I have a lot of tasks at that I need to attend to it. So that's why I said if we can structure the can the model in this manner I believe that it be able to accomplish what we are trying to do.
Jacob Oluwole: from what we have been trying to do is that we are doing this a for developers to be able to get their hands off to supervis because now we're training with our code we write with our data set we're training our just for it to know in and out of what we do so that we can put things in its care and he handle them and once it's done we can go back it and check if they are done accurately and all like that.
Jacob Oluwole: So I think that's what we are building because it's not like we're building for open source that people will be able to use it connect it to plugin that they can use because if we are doing that that would be a different approach right…
Adeleke Tolulope: Yeah, that would be a difference.
Jacob Oluwole: if I'm correct yeah so…
Adeleke Tolulope: You're right.
Jacob Oluwole: because right now some of these things we are coding putting the set in structure we are just particularly for ourselves for us be able to get some tasks done just like you I don't know if you told us about this the jobs that you implemented that the code did you talk did you mention that okay Andrew are you
Adeleke Tolulope: No, I haven't. I didn't even get him that update. Can you see the AI it's not responding and…
Jacob Oluwole: Hello Andre. How you doing?
Adeleke Tolulope: I can't sit down here all day trying to do it for me. Sometimes it will Okay.
Jacob Oluwole: It's like that. Yes. I was trying to use it yesterday. It was giving me the same show. I just slept off. I woke up. it's began. I do not enjoy it more than for now for now because I only started using it yesterday. So I prefer currently…
Adeleke Tolulope: Yes.
Jacob Oluwole: because of the response and maybe this is having kind of
Adeleke Tolulope: Has to it? what happen they are not getting the necessary fund the cost is not that high. I think they are the one taking care maybe hosting of the server and hosting the model.  So based on the deepsey trend on X a lot of people were trying it out a lot of people buging the website trying to make use of it this is better than returning this server
Andrés Felipe Urrego Martínez: Hey guys,…
Adeleke Tolulope: Yes. Hey
Andrés Felipe Urrego Martínez: sorry about that. I don't know what keeps happening with my Oops, sorry. Not sure…
Andrés Felipe Urrego Martínez: what keeps happening with my audio, but sorry, what were you guys? What were we saying?
Jacob Oluwole: I'll say something.
Jacob Oluwole: Do you hear me at all?
Andrés Felipe Urrego Martínez: What was your question?
Jacob Oluwole: Okay.
Andrés Felipe Urrego Martínez: Yes. Right.
Jacob Oluwole: I was informing Steve that with the way we are doing this project.  We are doing it for ourselves at boy we are doing it for our developers to be able to assign tasks to our agents and just like you've been saying we are not doing it for others we are not doing for people to be able to use within the application.
00:25:00
Andrés Felipe Urrego Martínez: Not yet. Because we want to make sure we learn how to do it for ourselves first, then we do it for whatever it is that we needed within the application. Yes.
Jacob Oluwole: So I was not like I was just confirming that that's…
Adeleke Tolulope: What?
Jacob Oluwole: what we are doing because I feel like if we are trying to open it to be able to build other project for others people to be able to use out there or anything that there will be a different approach to what we'll be doing like that means that the agent should be able to learn the code by itself be able to accustom itself to the general code base and be able to grful for others and it be going through there's a different angle to which we'll be carrying out this stuff that we're doing. So I was just confirming that with you and with Steve because I see that this process we are doing is just currently for Moy for us to for a team to be able to use for team caring and stuff.
Jacob Oluwole: So along the line was not like maybe I don't know if he had told you about the task that it helped Steve to do perform recently. So Steve said he has not informed you about that. So there's this tax like new ST…
Adeleke Tolulope: Okay.
Jacob Oluwole: though it's not like something that we have currently on our code base. This new tax that I told Steve about that told me some weeks ago at the start of the year that we should be able to send emails to users once they close jobs.
Jacob Oluwole: Yesterday when I was training with Steve so we've been training the board we text no when I was testing the model with Steve so texting with the current functions that we have so Steve said got the idea that okay let's text with something that we do not have currently the feature that the code that we do not have currently on our database on our code rather so I now give him the prompts so we ask it to write a function that we do not currently have on on the code base.
Andrés Felipe Urrego Martínez: Okay.
Jacob Oluwole: So although Steve already started the code the function…
Adeleke Tolulope: What's wrong?
Jacob Oluwole: but Steve told me that it should not follow what is currently on the code base that it should generate with the structure that we have and it should generate us like those stuff. So it generated those code in the pattern that still would write them although are some bugs that we saw on it when we compare we tested with the way that you tested with the other day. So we confirmed the efficiency. So we there are some lapses to it.
Jacob Oluwole: So Steve took that exact code modifying it like a little tweak from what he said just a little tweak like error handling there are some error handling that does not like so Steve said he was going to start working on the error handling like there are some there of coding that it should take care of some errors that can happen it's just like you pred that this error may happen so when this error happen do this do that something like that so it's still basic on that  But the main functionality of the code it was giving us he gave Steve the way Steve would have written it something like that.
Jacob Oluwole: So Steve said so I asked him today he said that was what he used that he just make the tweaks to the areas that still lagging still so I was like that's a good one at least we're able to try it with something new that we currently don't have on our database our code base rather and…
Adeleke Tolulope:
Jacob Oluwole: it was able to give us in the way that we would want it to be and it followed I was going through that this is exactly how we send emails like it went through that and he sent it and he was like that's good. he said that's good. So I feel like that's a good equipment. That was why I sent a message with what I've seen I feel like this is a good learning for a good learning c that we've able to achieve and all like that.
Jacob Oluwole: So I like okay this is good this is a good one for more at least if we are passing do this and just able to do that and just little effort just monitoring it and improving it alongside that is a good
Adeleke Tolulope: to do now. It's not like we will train the model and to be 100% perfect before we can start making use of it. once we've already train it with our code base and everything and it has already known everything the folder structure and everything then it's a thing that we can deploy right maybe on Azor and start making use of it.  If you are not making use of it, for example, the error that Jacob the test that we had yesterday that it was lagging in some aspect, we can train the model through to you already deploy mod to learn through the prompt you are given to it.
00:30:00
Adeleke Tolulope: So since it already knows the right coder and everything for example if you write a code that we feel like you still need some improvement in this part we just copy that code paste to it and give it the necessary prompt okay you need to improve this you need to improve that you need to improve this through prompt then it be able to learn just so that next time if you are now making use of it it will now correct itself I don't know if you get what I'm trying to say this one that we are creating data set now from scratch right to  train the model that the model will understand what our scope is all about. Then once that one is done, once the model knows the entire scope, the entire code, the respective the respective files, then we can then deploy it and start making use of it within our ID. And when using it through within our ID, we can retrain it through the prompts to it.
Adeleke Tolulope: I pointed Jacob to one example. There was the first time that we started making use of charging that we are doing.
Adeleke Tolulope: Sometimes it will respond better. Sometimes it respond in a wrong way. But before they even the advanced model of that particular model that we are using there I noticed something that the more I test the model the more I send information back to the model that this is…
Andrés Felipe Urrego Martínez: Of course.
Adeleke Tolulope: how I want it the more it's learn that even some…
Andrés Felipe Urrego Martínez: Yes. Yes. Yes.
Adeleke Tolulope: if I come back and then ask it something like that again it will return it to me the way I want it.  So all these AI models have that ability to learn through front.  So what we just have to do now is that once we are done creating our data set for the back end for the front end for all the part of our application is anything that we can and keep training it through pro we are fully confident in it that okay whatever this  Yeah. Yeah.
Andrés Felipe Urrego Martínez: The idea is we learn the database first, And then I mean we learn our entire code. We learn the database and then from there that's when you start using the pipelines to teach it multiple things throughout the day. One after the other without you having to be sitting there. Instead you just kind of train on one.  Once that's done, you review that one. But the other one is training and working on. You know what I'm saying here?
Adeleke Tolulope: making use of I understand what you're trying to say retraining and not that that was fine that was fine and…
Adeleke Tolulope: that's to to be cost effective now for bas Yeah,…
Andrés Felipe Urrego Martínez: And…
Andrés Felipe Urrego Martínez: I think just in general, so again, if it's not when you can have, five different tasks running at once rather than you having to be checking on all five things running at once, you know what I mean? Okay.
Adeleke Tolulope: I get that. I want to point your attention to something. for the first mode that we have now, once we are done training the model, we have to  While testing the model, we don't have something else that we want to improve it on because we haven't known the lapses and the limitations of that particular current model. is when you are done testing that model and you've take note of some area that you need to improve.
Andrés Felipe Urrego Martínez: So what I'm trying to say here is you can train a model I'm assuming in multiple things.
Andrés Felipe Urrego Martínez: If not they would have never been able to create these massive models training one task at a time. So go is someone going to say something?
Adeleke Tolulope: No, no,…
Adeleke Tolulope: go ahead.
Andrés Felipe Urrego Martínez: Okay.
Adeleke Tolulope: Go ahead.
Andrés Felipe Urrego Martínez: So then what I'm saying is that then if you have let's say in the Python three different tasks that are doing three different things and…
Andrés Felipe Urrego Martínez: they're not like affecting one another then you start thinking okay may maybe that is a possibility right because then I have this I'm testing this one thing while another one is happening technically
Adeleke Tolulope: Yes. Yes,…
Adeleke Tolulope: We can do that. for example just like what I suggested the other time that I want us to even train the model such that now outside code that we to understand in maybe sentence or paragraph what the entire application is doing what the full scope of the application so that if you are asking it in pure text the last time that we were testing I said I didn't train it so that it can test to you that it only understand returning codes right so for example as I'm creating
00:35:00
Adeleke Tolulope: this data set now maybe someone can be creating the text or something like that I want to teach the model on it get so for example…
Andrés Felipe Urrego Martínez: right? Correct.
Adeleke Tolulope: if I'm the one that if I completed my data set before the other person and I train the model while testing the model the other person is done with the data set then you'll be training the model while testing the existing one just following trying to follow what you are trying to say not to delay the training period set but what we just need to do now we need hands on creating this kind of data set yeah has been working on the front end part of the application while so yeah something we can
Andrés Felipe Urrego Martínez: Is that something that you and Ty can work on? is that something that he's working on right now? Perfect. Got him.
Andrés Felipe Urrego Martínez: Okay.
Andrés Felipe Urrego Martínez: Yeah. it's new, So, I mean they probably have some service limitations. I mean but it's tried five times already. Yeah. Is it a big file? I assume it is.
Adeleke Tolulope: Can you see that model it's not even responding it's not even yeah this is the system that's…
Adeleke Tolulope: what I said that even if the file is large something like that even if it's going to do it, it won't complete everything if you just stop it halfway.
Andrés Felipe Urrego Martínez: Got it. And you've tried to do this with GPT01,…
Adeleke Tolulope: You can't upload file in GP1.
Andrés Felipe Urrego Martínez: right? But …
Adeleke Tolulope: You're not allowed to upload one.
Andrés Felipe Urrego Martínez: because you need to upload the files, Only with Oro.
Adeleke Tolulope:
Adeleke Tolulope: I love that GTO one. Yeah. only before that one is working.
Andrés Felipe Urrego Martínez: Yeah,…
Andrés Felipe Urrego Martínez: But always use GPT1 wisely, right? Because you get limited amounts. use it for deep thinking tasks.
Adeleke Tolulope: Yeah. for example,…
Andrés Felipe Urrego Martínez: That's…
Adeleke Tolulope: I think I Yeah,…
Andrés Felipe Urrego Martínez: what it's supposed to do, it's actually thinking in the background, not just this one. has the ability to think for a little bit longer.
Adeleke Tolulope: I think I told Jacob that GP1 actually helped me with this current model that we have because I've been making use of GBT 4. it has been frustrating me giving me some different thing that…
Andrés Felipe Urrego Martínez: Yeah. Yeah. Four doesn't resonate very well.
Adeleke Tolulope: but yeah but from the kind of information G4 was returning to me I was able to understand okay this is how I should do it how I should do it but I don't fully get it in depth so I now tried G01 I love the model it actually helped me it saved me a lot of stress  is they give me the g.
Andrés Felipe Urrego Martínez: that saves you a lot of time and yeah, I mean it's just again, as long as we know it's an awesome tool, then we're good. We're Gucci.
Adeleke Tolulope: yeah. Okay.
Andrés Felipe Urrego Martínez: No. Okay. Yeah. Go ahead, Hello. I think we get limited amount of times we can use it,…
Jacob Oluwole: He said the old one is limited on your hand.
Andrés Felipe Urrego Martínez: right? Yeah,…
Jacob Oluwole: Okay. Okay. Because I was thinking
Andrés Felipe Urrego Martínez: cuz I've had a day where it said I don't know, you have 10 left or something like that.
Andrés Felipe Urrego Martínez: …
Jacob Oluwole: You have to So I was thinking because I told you I changed our subscription plan from $20 to 9 $10 9 or…
Andrés Felipe Urrego Martínez: yeah. You did say that.
Jacob Oluwole: Yeah.
Andrés Felipe Urrego Martínez: I would like to
Jacob Oluwole: So I thought maybe people that could have access to the old one and people that are paying the 20 bucks $20. So that when you said you have limited time limited.  So I was already thinking of upgrading so that because talked about that it's very efficient for him doing the work so I thought it limited for people on that 20 20 bucks per month $20 per month so I wanted to even upgrade so that at least for this time that he's working on a new tax that new area of specification specialization I like so that I wanted to confirm
00:40:00
Jacob Oluwole: if it is unlimited for you but since you are saying there is limited I think yeah okay okay so I think we are good yeah I think I
Andrés Felipe Urrego Martínez: No,…
Andrés Felipe Urrego Martínez: no, no. The only one that has unlimited is the $200 a month one. And then it's newer version of that too. yeah.
Jacob Oluwole: I think I told you how I did that one. I just subscribed on iOS.
Andrés Felipe Urrego Martínez: So, how you said you did it From your phone.
Jacob Oluwole: From phone.
Andrés Felipe Urrego Martínez: You cancelled the membership and then signed up from your phone,…
Jacob Oluwole: Yes. Yes.
Andrés Felipe Urrego Martínez: but you can still use it on your computer.
Jacob Oluwole: I can see on my computer. I just lo Yeah,…
Andrés Felipe Urrego Martínez: That's hilarious. That makes no sense. But I think Twitter is just
Jacob Oluwole: but on your PC that it should tell you that you need to pay for $20. you tell you that you are not on you're not using the pro version. If you try to subscribe it tell you to subscribe but on the other end you are still having access to unlimited one and the rest.  But if you still click on subscribe, it will still tell you to subscribe for $20 or it still be normal. I don't know if you get what I'm saying. On the desktop, if you lo on your desktop and you're using or on your PC, it should be telling on the background that you should subscribe for $20 you yet to subscribe something like that. You click on subscription to take it to $20 per month or desktop or if you on your phone, you are good.
Jacob Oluwole: But on desktop you can access all the models that is currently available. So I think I don't know…
Jacob Oluwole: if it's a bug or is a stuff but I'm sure they will be aware of that different Yes.
Andrés Felipe Urrego Martínez: Yeah, I mean …
Andrés Felipe Urrego Martínez: I think it's Twitter X is the same way. If you sign up from one is like eight, if you have the other one is 15. And then I was like, &quot;What?
Jacob Oluwole: You get it? Yeah. Yeah. Exactly. on X2 if you're signing up with your desktop it's much more cheaper compared to getting cool on mobile I tried it I wanted to do it for my friend like he said we should try it out so it was giving us different amounts and that was it was giving us one I think maybe 75 bucks for a year and it was giving us maybe 100 bucks for a year on mobile 75 for desktop and 100 plus for mobile. So I don't know
Andrés Felipe Urrego Martínez: I mean,…
Jacob Oluwole: why it's different that I don't know…
Andrés Felipe Urrego Martínez: I guess so probably…
Jacob Oluwole: why it's different. my god.
Andrés Felipe Urrego Martínez: because applications are lighter to maintain.
Jacob Oluwole: Remember? okay. Yeah. Web application and mobile application. Okay. maybe
Andrés Felipe Urrego Martínez: That's another thing, Once Look, guys, I think Once you have this code done, we can start asking it to start rewriting it. But for an applica to write the code for an application,…
Jacob Oluwole: Move the application.
Andrés Felipe Urrego Martínez: I told you for an actual mobile application, I think honestly guys, look, I love that we want to keep it on the website.
Andrés Felipe Urrego Martínez: That's a perfect MVP. But running Mo in an application will be so much easier altogether for people,…
Jacob Oluwole:
Jacob Oluwole: Yes, sir.
Andrés Felipe Urrego Martínez: for signups,…
Andrés Felipe Urrego Martínez: for everything. I told this to Jacob, guys. I said, &quot;Look, that's exactly why we're learning how to do this. I want to keep this team, This is our team. This is my team. We want to keep this team, but the only way do not have to bring in people that know how to write an application is by learning how to use the models that will write it for you. So, just think about those things. All right? Know that I got your back that I want for me instead of telling you I need you guys to start studying to learn how to all of a sudden just turn everything into an application by next month. No. what now?
Jacob Oluwole: I was thinking about that because
00:45:00
Andrés Felipe Urrego Martínez: you're going to learn how to train the models that will do it for you. And that's when you start seeing the value of this is when you now are managing things that can outperform your current knowledge, but you're using it to your advantage through your own training, through your own guidance. So, you're now guiding it based on the information you're acquiring. yeah. I mean, I make the best of it, guys. I promise you. Look, I mean, I truly believe in you guys as a team. And I told this to Jacob last week. I believe in every single one of you. And that's exactly why I believe that I need you guys to learn the best of your ability. how to create and how to create and train these models. that's it.
Andrés Felipe Urrego Martínez: That's all we need to How to create and train these models so that you guys can from there on just a thousand%, increase your reach. How much you can now do without having to sit there and make a thousand mistakes before we learn something? Because that's how writing code is, right? We got to f*** it up here, f*** it up here, then fix it. So, remember, we're learning something that's very critical now. and this is great. This is great because very soon these models will get even smarter and smarter. So teaching it is not going to be as hard but you guys are already not going to know how to do it. That writing the data set is not going to be as hard but now you guys are going to be able to do it. so there's a lot of these things that this you guys are just at the prime time of everything that's happening and everywhere we're going.
Andrés Felipe Urrego Martínez: Keep your mind open and your vision, your ears very open when we're talking about where we're going because that's how you should be training your models every day is with that in mind. This thing is meant to outperform me. There's no other way around it. It with my knowledge and I need to train it to become much better than what I can do today. That's it.
Andrés Felipe Urrego Martínez: All right.
Adeleke Tolulope: Yeah. Yeah.
Adeleke Tolulope: Right. f***. Yes.
Andrés Felipe Urrego Martínez: Steve, we can catch up later. I think you said you guys are going to start, working on these things.
Andrés Felipe Urrego Martínez: let us know if we can have Jacob, we talked about having two calls a day, while we're doing this training of the models just so we can all watch and so 1 in the morning, 8:30. That was completely my bad. I didn't have it on the schedule and that's why. So I'll just change our call to 8:30. and then we can just start watching the model and the results that it gives us back and trying to figure out how do we train it better. Okay. Who…
Jacob Oluwole: Okay, so that was a mistake.
Andrés Felipe Urrego Martínez: who raised their hand? Jacob, please raise your hand. Are you having a laugh?
Andrés Felipe Urrego Martínez: Are you having a laugh, Please do not have a lab with All if anything else comes up again, please please let me know. I'll be here. Jacob, I'm going to go through all the messages that we have on the group because I didn't see the updates from today. I'm going to look at the ones from marketing as and then maybe we can talk in about an hour or two and discuss, how are we going to do these marketing campaigns. All right, sounds good. I'll talk to you guys soon.
Andrés Felipe Urrego Martínez: Bye-bye. Thank you guys. Bye-bye.
Taiwo Ola-Balogun: Take your ste.
Jacob Oluwole: All right.
Adeleke Tolulope: Tywood can we have maybe a call anytime you're available I want to teach you some structure that you should start considering as well in this data set when you're available just let me know we can jump on the call settle us Jacob,…
Taiwo Ola-Balogun: Hello. Okay. Okay.
00:50:00
Jacob Oluwole: I know
Adeleke Tolulope: I don't just want to say that I don't have money.
Adeleke Tolulope: Give me so much appreciate this car like 5.
Jacob Oluwole: Yeah, you didn't see this guy I don't lose my money My next phone I want to buy I don't lose money.
Adeleke Tolulope: But if you give me more
Jacob Oluwole: I don't lose money for crypto last time cryto I don't lose money I do crypto again I use the money I buy stuff I don't know that
Adeleke Tolulope: That's  But is not something I planned for actually last bit account and carry all this trade and all this stuff.
Adeleke Tolulope: her and…
Adeleke Tolulope: she knew pictures and go hours big risk. start less than 15 with me less than 150 and…
Jacob Oluwole: No, no,…
Jacob Oluwole: no. Okay.
Jacob Oluwole: say go back to Z start again guy I last you like this you are making
Adeleke Tolulope: I don't know
Jacob Oluwole: I respect you. you've made many things happen. let me tell you my own story. I know that you are You are making good choices. you're not staying with anybody.
Jacob Oluwole: You're not living with anybody. That's one.
Jacob Oluwole: So that's one, two, you bought all the stuff that you can buy only workstation. So you have a workstation, you have a system, you have a desktop, you have everything, you have a chair, you have a table, you have monitor, you have a bed,…
Adeleke Tolulope: Yeah. Yes.
Jacob Oluwole: you have a big bed, you have a kitchen set up by you, you have everything.
Jacob Oluwole: You now solve all those things that you've done
Adeleke Tolulope: This one.
Adeleke Tolulope: That's f***.
Jacob Oluwole: my table and share is still plastic table and plastic sh I don't have big screen iPhone I'm using iPhone I bought second I bought from someone actually I met good because my body is not good with all this from so you get upon
00:55:00
Adeleke Tolulope: Yeah. Yep.
Jacob Oluwole: me I don't do what they do okay me lose for as last year April I was having one I having 18 and since then I've not done anything  How many months? June, July, October, November, December. Then that was when you were even going said that you were going like you going like you get now.
Adeleke Tolulope: Yeah. Then I went back to again.
Jacob Oluwole: I noticed that maybe that was when you started a month before that same time.
Adeleke Tolulope: So I have to start saving again.
Jacob Oluwole: So that one I see as much as that's a good one you look at myself I'm just trying to make myself an example if anything happens now you have your gadget that are with you you have every other thing that you able to see that myself like this I can see that this is what I've used my money to do other than investing them in crypto and crypto is burning
Jacob Oluwole: currently I'm 10x down like invest so you should so you should not feel like I'm just saying that you can know that okay I don't say making me feel better about yourself but I just want you to know that you are not doing bad
Jacob Oluwole: Sometimes I want to be like that sometimes guy to you you keep money you go and…
Adeleke Tolulope: Yeah, I did.
Jacob Oluwole: put you give one person you go and give developer I don't get anybody so you like this like this now if you tell them okay this is what you do you have a laptop you have a workstation you have a solar you have everything here you get you have everything myself like
Jacob Oluwole: system you bought your speaker everything don't like this now I can say that this is what I've done with mo money and it's very very bad apart from renting an apartment so I feel bad for that so I said I want to work on it I want to change I want to start but actually I…
Jacob Oluwole: because I saw 3K from last year. I saw 3K and I didn't cash it out.
Adeleke Tolulope: You want to eat?
Jacob Oluwole: I saw I was in my wallet. I went down November 15. Yeah.
Jacob Oluwole: I had f****** f**** f****** f****** three f****** I saw it and…
Adeleke Tolulope: My god.
Jacob Oluwole: God gave me what I wanted because it will have
Jacob Oluwole: turn all my losses from people but because it was boom like this now I didn't even touch it I didn't but I know that anything I didn't all this so I don't know money I'm 10 years
Jacob Oluwole: more than 10 years down. Mhm.
Adeleke Tolulope: take out of it and if you can you now invest less than the profit you don't return all the profit back to market because just take little out of it take it to the market then stop then you wait another I'll put it there so profit whereever  again.
01:00:00
Adeleke Tolulope: I don't lose more than I do 300K. I don't be fine. yeah. Yeah.
Meeting ended after 01:01:26 👋
This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

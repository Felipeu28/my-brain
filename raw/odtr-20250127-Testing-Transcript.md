# Testing 2025-01-27 - Transcript

**Source:** OneDrive transcript
**Date:** 2025-01-27
**Original file:** Testing 2025-01-27 - Transcript.docx

---

Testing - 2025/01/27 14:06 CST - Transcript
Attendees
Adeleke Tolulope, Adeleke Tolulope's Presentation, Andrés Felipe Urrego Martínez, Jacob Oluwole
Transcript
Adeleke Tolulope: Hello. I'm Good afternoon. Yes, I can hear you.
Andrés Felipe Urrego Martínez: background noise or anything like that or anything good?
Adeleke Tolulope: No, I can't hear any background noise.
Andrés Felipe Urrego Martínez: Okay, fantastic. All right. Steve,…
Andrés Felipe Urrego Martínez: walk me through. I mean, guess let's get started. Whatever you got. I can now. Yes.
Adeleke Tolulope: Can I see my screen?
Adeleke Tolulope: So, I've already started the compute instance for me to do anything I must start it first so I started a computer instance so this is the model I train this is the model we are using deepsek output three this was one that retain the codebase knowledge and is the one working according to the structure of the codebase  So These are the files of the model.
Adeleke Tolulope: So now if you are done fine the model if you are done finding the model then we are going to compile this entire folder into a single file that we can use that we can maybe integrate into our ID the application we are using to write code or we can even deploy it like this directly to Azor and then start communicating with it if we are done training
Adeleke Tolulope: it in a way that we want to start working with it. But for now, I fed it our code base. I created a data data. Let me even show you the data set.
Andrés Felipe Urrego Martínez: And how long did that take from when you fed the data the code to when you got and this is the back end, So maybe…
Adeleke Tolulope: Yeah, I fed it the back end code. Yeah, I already taxed him that I already told him to do that while working on the back end.
Andrés Felipe Urrego Martínez: what we can have Ty will do is set up the front end. Okay, good.
Adeleke Tolulope: I think it was on Friday. I told him that creating this data set for me too is consume time. So I told him that he should go and…
Adeleke Tolulope: start creating data set for the front end codes and I think he has started it. I even called him on Saturday to remind him and he said he has started working on it.
Andrés Felipe Urrego Martínez: Okay, perfect.
Adeleke Tolulope: So I just wanted to show you the data set I make use of initially…
Andrés Felipe Urrego Martínez: Yeah, let's see.
Adeleke Tolulope: what I observe from our previous limitations such that the mods are not learning because we are not giving it instruction and we're not giving it output. We only trying to feed it fed it with the code base without any proper instruction or anything. So it's just trying is to me I think it just gets the code base just as an additional finetune additional knowledge for the model.
Adeleke Tolulope: I don't know what I'm trying to say but
Adeleke Tolulope: What is it called?
Andrés Felipe Urrego Martínez: You cut out.
Adeleke Tolulope: Some like I said I think…
Andrés Felipe Urrego Martínez: Okay, There you are. What was that Sorry, that last piece. I just didn't hear the last piece.
Adeleke Tolulope: what I observe as regarding our previous failure on the models that we've trained so far is because we didn't structure the data set properly.  We're only trying to cut corners such that we want to feed the entire code base and hoping that it be able to respond based on our code base whereas to it it sees our code base as an additional knowledge to it.
00:05:00
Adeleke Tolulope: So even if I ask it any question, it has that liberty to return anything even outside what I used to finetune it. I think that's one thing I can point out there that actually made it not to probably work very well.
Andrés Felipe Urrego Martínez: Okay. Uh-huh.
Andrés Felipe Urrego Martínez: So that it still does what Chad GPT does technically, that it's sometimes…
Adeleke Tolulope: Yeah. but now
Andrés Felipe Urrego Martínez: but are they good results or are they basically just nonsense and…
Andrés Felipe Urrego Martínez: and typical hallucination? so it's going outside of the request to actually improve.
Adeleke Tolulope: They are good results like perfect results.
Adeleke Tolulope: Yeah, it's actually improving. For example,…
Andrés Felipe Urrego Martínez: So they're not the typical bad hallucinations.
Adeleke Tolulope: example, no no they are not bad at hallucination. even if I want the exact function I used to finetune it.  For example, maybe I want to debug something and I know this is where the bug can actually come from. If I ask the model to get me that function, it's going to get me that function. And if I ask it to create a new function for me, making use of it the code base that it was fine tuned on the knowledge with the structure then it's going to create a code for me just like this example I did here. I tried it here over here. I think you can see it here.
Adeleke Tolulope: For example, I asked it over here that create a function that get user analytics and compute overall an analysis for users. Use your ability based on the coding pattern you were trained with to implement these features. And based on the coding pattern I train it with, it can't just write the complete function. It must write a controller function for it and… a service function.  And it first of all return the controller function to us. Can you see this is the controller function. And this get analytics. Okay.
Adeleke Tolulope:
Andrés Felipe Urrego Martínez: Can you do me a favor real quick?
Andrés Felipe Urrego Martínez: And I am listening. Can you please copy and paste that for me that just from where it says erating to the end of generated code. So just those two prompts. Can you please send them to me real quick? Please just …
Andrés Felipe Urrego Martínez: you don't have to send me the actual code. You can just send me the prompt at the top.
Adeleke Tolulope: …
Adeleke Tolulope: Okay, send a prompt at the top. yeah that I'll be sending the generated code as well.
Andrés Felipe Urrego Martínez: and the bottom one that says generated code. yeah. No, no. I mean there's two. There you go. Like that one. I was just saying you could have copied together,…
Adeleke Tolulope: No this one.
Andrés Felipe Urrego Martínez: but Yeah. Yeah. Yeah. That one. That's what I meant. Yeah. Yes, sir.
Adeleke Tolulope: If you wait study these two together you can see that I gave it an instruction over here then it's maybe point to what is trying to do okay it's just like repeating the prompt right it's just like repeating the prompt over here right then the generated code over here creating this code it generated you first of all generated the controller. Then over here I now said create the overall service function.
Andrés Felipe Urrego Martínez: Of course.
Adeleke Tolulope: When I said create the overall service function, then it went ahead to create the overall service function.
Andrés Felipe Urrego Martínez: And how was the result?
Adeleke Tolulope: Yeah, it's is fine. It's working fine. over here.  Now based on the user ID so I should copy this  food to you, right?
Andrés Felipe Urrego Martínez: But but yeah. C can you please just send me that real quick? That's the other part of it. I just want to do something. I want to know what kind of prompt could we use if we wanted it if I wanted us to test right now and say look for errors in a specific section of our code. Right. So while you're explaining and doing your thing, I want to kind of look at just the top part.
Andrés Felipe Urrego Martínez: I just want to create a prompt that I can give you for you to see if that would work. what I mean? So I guess anything from there to all the way down where it says create a function that gets users analytics of course. you go. That's it. So I can use this as an example of what we used right now. But then  looking to create a new one. there you go.
00:10:00
Adeleke Tolulope: That's good.
Andrés Felipe Urrego Martínez: Sorry, just a second here.
Andrés Felipe Urrego Martínez: All what are you working on right there.
Adeleke Tolulope: over here.
Adeleke Tolulope: Yeah, I'm trying to start the instance again.
Andrés Felipe Urrego Martínez: Okay, perfect.
Adeleke Tolulope: If you check over here, I changed my connection. So it stopped the terminal. So I'm starting it again with the new connection so I'll be able to send a prompt to it and…
Andrés Felipe Urrego Martínez: Got Makes sense.
Adeleke Tolulope: expect result. For the reason why I said this model outperform others was because for other model that I've worked on I fine tuned them with JavaScript code…
Adeleke Tolulope: but if I now prompt them they now returning result to me in other programming language.  So it actually went though it performed what I asked it to do but yet is not the kind of code that I want because that's not
Andrés Felipe Urrego Martínez: …
Andrés Felipe Urrego Martínez: what is it missing? I guess I'm just trying to think. so h have you read so far on if it doesn't give you the code you want, how do we continue to kind of train it to give you the one how you want it.
Adeleke Tolulope: Yeah, what I read concerning the issue was because one charity pointed some things that can happen. One maybe data set misconfiguration. Two maybe the training parameters are not well structured. Three, it now says maybe is the model is not given the necessary information.
Adeleke Tolulope: the necessary instruction to do what it's expected to do. So for you to train a model to find it on a particular stuff, you must give it an instruction while training it and you give it an expected output. that's when I made my research on deepseek, I stumbled upon their data set. I noticed that they actually gave it an instruction and they gave it an expected output.
Adeleke Tolulope: But they have very large data sets such that the model can quickly generalize on all those kind of data set and be able to come up with solutions and know so for our code base though we don't have a very very fast data set that we used to train it but with the data set that we used to train it is still able to still work with that particular data set write our code in that particular format in that particular structure that we want. For example, this instruction that you see here that write a controller function that create employee profile. This is the sub function you're trying to access this function over here.
Adeleke Tolulope: This part of function should be in another file right it's in another file.
Andrés Felipe Urrego Martínez: They make up they made it up.
Adeleke Tolulope: But for other models that I've trained, they were not even Nothing relating to our data set at all. They just returning something to Completely outside our data set. Completely different.
00:15:00
Andrés Felipe Urrego Martínez: So my ignorance here, did you connect our database to this already? I assume so that it can…
Adeleke Tolulope: No, no, I haven't connected our database to this one. I haven't connected our So,…
Andrés Felipe Urrego Martínez: but is that something we need to do to be able to achieve those results? tell me about the difference between let's say the …
Adeleke Tolulope:
Andrés Felipe Urrego Martínez: yeah. Real quick, let me send you this
Andrés Felipe Urrego Martínez: There's hold on. Let me send you this and then you can continue. Sorry, just a second. So, h how is this different from let's say the prompt that you gave me and could this help? I mean, I assume this is assuming that the things that we get, but I get what it's trying to do. could that be a prompt that is more specific towards what we need? or I mean are you asking it for results or are you asking it to create…
Adeleke Tolulope: Top five.
Andrés Felipe Urrego Martínez: what are you asking from the model that you created specifically? What is it that you want with this? and what was the output that he gave you?
Andrés Felipe Urrego Martínez: just to revisit.
Adeleke Tolulope: Yeah. Yeah.
Andrés Felipe Urrego Martínez: Okay.
Adeleke Tolulope: I'm trying to create something different from what I used to train it to just check if it's going to still retain some of our method right the naming convention and the structure for use of it to implement new features Okay,…
Andrés Felipe Urrego Martínez: So you're asking it to create new functions. let me ask you a question. remember why don't we take a step back so that we can continue to train it on our code. Why don't we just start with reviewing and improving code. So for example using a code like this. look
Adeleke Tolulope: hold on. Let me copy a code.
Adeleke Tolulope: I want to copy a code from a particular place and try it out. Don't
Andrés Felipe Urrego Martínez: Okay.
Andrés Felipe Urrego Martínez: Okay, and I was just thinking so that it's learning from it, especially if we start doing a reviews and recommendations of different sections of the code. And then we do that during a day, two days. And then now it understands us a lot better because he has actually gone through the initial training but now it was a dissected training that actually was asking it to review it understanding and see if there would be things changes that would improve it. Let's see.
Adeleke Tolulope: Okay, let me go.
Andrés Felipe Urrego Martínez: So this work the create profile either through four or generate a resume.
Adeleke Tolulope: Yeah, Create employee profile. I want to try though it's not part of the data set I used to train it but I want to see if it's able to do that.
Andrés Felipe Urrego Martínez: Okay, I see. Okay.
Adeleke Tolulope: Where is the prompt? Okay, let's give you the identity. Review this code and
Andrés Felipe Urrego Martínez: Steve, I know I get repetitive about it, but always grab your prompts, whatever, however good you think they are, always grab the prompts and h, hey,…
Adeleke Tolulope: Identifying without logic or
Andrés Felipe Urrego Martínez: for deep sake, is this a, please, review and revise this code, this prompt to maximize my results. will I mean obviously take out whatever you don't want but yeah I mean I was just thinking that so wait to create a promp for the wait okay so then it should just be prompt for exactly we should probably remove the top part that says prompt to create a prompt for the AI agent to review a section of the
Andrés Felipe Urrego Martínez: code. Is that correct? Or do you need to remove that and just say analyze the following code and provide actionable recommendations? No, I'm saying do you think how to There you go. There you go.
00:20:00
Andrés Felipe Urrego Martínez: So there you go. What's the actual prompt exactly? And do you need the three apostrophes up there? Is it three on each side? Yeah. That's pretty good,…
Adeleke Tolulope: Return your feedback in clear structured format with actionable steps considering.
Adeleke Tolulope: Okay. Let's see if let's see…
Andrés Felipe Urrego Martínez: I mean, That's okay.
Adeleke Tolulope: if it's going to work fine. I haven't tested it in this manager.  Okay.
Andrés Felipe Urrego Martínez: That's okay. No, let's try it. That's what we're doing, We're trying to play with this thing.
Andrés Felipe Urrego Martínez: That's my thought that for it to learn before we ask it to create things for us, we should focus primarily on testing throughout trying to get it to actually test or commend for our code to be better for our functions to improve so then it just knows more and more and more and more and then we can say okay now based on what let's create this function right this is amazing, all the world is talking about right now is Deep Seek.
Adeleke Tolulope: even deep.
Andrés Felipe Urrego Martínez: It's insane.
Adeleke Tolulope: Yeah, I make use of the interface is very very cool.
Andrés Felipe Urrego Martínez: Very good.
Adeleke Tolulope: Very very cool.
Andrés Felipe Urrego Martínez: Yeah. And…
Adeleke Tolulope:
Adeleke Tolulope: I love The IPI is more cheaper than Yeah,…
Andrés Felipe Urrego Martínez: and we can connect to their API too, I mean, it's just I think Exactly. So, we need to look and see, when you have a chance, look and Hey, it doesn't make sense for us to switch. I can't remember. I think we still have some credits at that GPT, though, so that's good. Yes, I've always wanted that.
Adeleke Tolulope: we can adopt this deepseek as our fallback AI
Andrés Felipe Urrego Martínez: That's awesome. Thank you.
Adeleke Tolulope: Okay, that is really good. Okay, let me see the results.
Adeleke Tolulope: It return the function back. Okay.
00:25:00
Adeleke Tolulope: login it return the function back the function code open availability.
Andrés Felipe Urrego Martínez: I want to see the recommendations. Did he give them to you? Okay. Look, he just gave you back everything you gave it.
Adeleke Tolulope: Yeah, but it made some adjustment to it. Yeah.
Andrés Felipe Urrego Martínez: We did. can you ask it what are the difference kind of thing is that something we can do what are the difference between this and what I provided you kind of thing I just don't know how much is it like a chat kind of thing or no can you ask it what is the difference between the output and the input
Andrés Felipe Urrego Martínez: to break it down for Does that make sense? or I wonder if we could have given it the prompt and asked to does the prompt say I guess It said, &quot;Recommend improvements in comments, variable names, and overall Return your feedback in a clear structure format with actionable steps categorized by priority.&quot; But it do that.
Adeleke Tolulope: No, It returns the function code and even made some update to the code I passed to it.
Andrés Felipe Urrego Martínez: So what it's missing is the part…
Adeleke Tolulope: The text.
Andrés Felipe Urrego Martínez: where it breaks down what the changes were. Okay.
Adeleke Tolulope: Exactly. I think that that was not in the data set I to train mostly the data set I used to train it is just to always return codes.
Adeleke Tolulope: always return codes. not even any single maybe text or just returning a just
Andrés Felipe Urrego Martínez: But maybe that's the next way we train…
Andrés Felipe Urrego Martínez: because we do want it as it's going to be a lot easier for us to work or for you guys if you're just asking it every time to review it and then give you the recommendations back tell you where before it makes the changes because I mean think about it…
Andrés Felipe Urrego Martínez: if that way you can parse through the changes that it's recommending and ask it to apply only the ones you think are good u then you review it again and then you apply it to your work. Does that make sense?
Adeleke Tolulope: Yeah, exactly.
Adeleke Tolulope: Exactly. I even thought of something now that in the data set I'll be creating we will write a code and we use the help of chargibility to help us to analyze those codes then we now make use of those analysis from chargibility as the result just to train the model okay so that even if I'm passing a code to it let me to analyze this kind of code then it will know that okay this is what there are diverse ways we can fine-tune the model to be able to generalize to have a general knowledge.
Andrés Felipe Urrego Martínez: Just grab it the piece. Okay. All right.
Adeleke Tolulope: I don't know maybe you noticed that I said I'm even trying to train it such that it can even set up an entire environment.
Andrés Felipe Urrego Martínez: Very good.
Adeleke Tolulope: For example what we are doing what this first model is just to do is to always return code for you. If you want to write any code you want to write any function to always return code for you.  But I haven't trained it in a way that it can even create a file right that it can write those code within a file. I haven't trained it so that it can give us What I mean by pseudo code is that for example if you want to implement a particular features we put it in a sentence step by step of how we want to accomplish such kind of features. we want to get the user's information, we'll get the user's email.
Adeleke Tolulope: We will make sure that the user's email is unique in the database. All those kind of steps. We'll write it in sentence in bullet points. That's what we known as pseudo code.
Adeleke Tolulope: We are still going to train the model so that it will be able to write pseudo code Such that even for example if we want to do any new features we can pass it that pseudo code. I want to implement this thing. These are the steps I want to do. These are the things I want to create. You write it there.
Andrés Felipe Urrego Martínez: Okay.
Adeleke Tolulope: Then you pass it to the model. Then the model will be able to work. based on those trainings but for now the only training it's understand the only thing that it's think that it should always done as an output is only in quotes it's only generating code that's why it made an update to the code I haven't passed to it updated some part of the
00:30:00
Andrés Felipe Urrego Martínez: Yeah. So, that was good.
Andrés Felipe Urrego Martínez: So, I was going to ask is this an improvement compared to the one that you had maybe just grab grab…
Adeleke Tolulope: Yeah, let's try it down.
Andrés Felipe Urrego Martínez: what it gave you back and then paste it on Chad GPT next to the one that you provided it and then just ask it real quick to find the differences and tell you how it's more efficient. You see what I'm saying? Yeah. Yeah. because ideally you want to understand the differences between the code that it's giving you. we need to analyze and that's why we figure out okay yeah it's giving me a function back it's supposedly fixing it…
Andrés Felipe Urrego Martínez: but or maybe it is a little bit so then what we do is we go and train it now on how to give us a result back technically
Adeleke Tolulope: Okay.
Andrés Felipe Urrego Martínez: Before you hit enter, hold on. Go back. No, just keep doing your thing until But don't hit enter at the end.
Adeleke Tolulope: Okay. I keep doing my thing and…
Adeleke Tolulope: I'm done. What is the difference between these codes?  Xbox.
Andrés Felipe Urrego Martínez: That's adorable.
Andrés Felipe Urrego Martínez: That is adorable. you're giving it no guidance to whatever you want back.
Andrés Felipe Urrego Martínez: you're not saying I need full analyzing or how the functions are different which one is better how is it better I mean you got to ask analyze the two functions to understand which one is better and  Fine. Give the recommendations. Reason I mean, try it like that. I mean, that's I guess but that's what I mean.
Andrés Felipe Urrego Martínez: just focus a little bit more on the prompt that you could still say bullet in bullet points give me the differences I mean you could just be so much more specific if not you're not yeah
Adeleke Tolulope: Upon analyzing both versions of the case, several case emerge that impacted the efficiency maintenance and environment First function creates only client profile. This function focuses solely on creating a client profile if one doesn't exist already Second function create both client profile and employer profile. In addition to client profile, it also creates an employer profile regardless of whether an employer profile is necessary.
Andrés Felipe Urrego Martínez: Stop right there. So it's that good.
Adeleke Tolulope: No, that's not good. Creating two functions into the same what is it called into a single if the application's intent is to manage employee profile exclusively within the function the first implementation is more appropriate creating an employer profile unnecessarily can lead to redundant data increase storage yeah I think for example a single function is meant to perform
Andrés Felipe Urrego Martínez: But why unnecessarily? It also creates an employee profile regardless of whether an employer profile is necessary. What does that mean?
Adeleke Tolulope: perform just a single task.
Adeleke Tolulope: The first function is really meant to create an employee profile, but the second function created an employee profile and also still make use of that particular information to create an employer profile. Do you get that? Let me even check the code and…
Andrés Felipe Urrego Martínez: I did.
Andrés Felipe Urrego Martínez: I did. Okay. Yeah.
Adeleke Tolulope: let me check the code and see myself. If function employee Okay.
00:35:00
Andrés Felipe Urrego Martínez: Test it out.
Adeleke Tolulope: Create this is where it all went wrong. employer link here. this is the part that created the employer profile even though we don't want it recommendations to improve efficiency, readability and maintility that logic
Adeleke Tolulope: It return the logic there. This part shouldn't be added to the code. Okay, let's go. data integrating and update user documents.  It update the user document with profile ID name list if they are missing or undefined. This ensure that the primary remain consistent and Second No update A class logic to update the user document potentially leaving user record incomplete. Error handling and validation. Comprehensive error handing.
Adeleke Tolulope: It throws specific errors already is with meaningful messages enhancing debugability and providing clear feedback to the user or Second function generic error adding it only throws errors called without providing specific context or messages.  H data assignment and structure first. The second direct assignment of hours and locations assign hours and location directly on the employee object which may be less structured depending on the overall data schema.
Adeleke Tolulope: application structured data assignments enhance clarity and maintainability making it easier to maintain and query the data efficiently. Wow. No,…
Andrés Felipe Urrego Martínez: That one good.
Adeleke Tolulope: no, no. It's not good. Hold on. I have to do something.
00:40:00
Adeleke Tolulope: Yeah, I'm even trying to make use of the model to correct the code.
Adeleke Tolulope: I want to see the output.
Andrés Felipe Urrego Martínez: Perfect. Okay,…
Adeleke Tolulope: I want it to correct the code itself.
Andrés Felipe Urrego Martínez: I'll join here in a little bit again on my phone.
Andrés Felipe Urrego Martínez: Our daughter, we have a teacher parent conference today, so I just need to kind of get ready, but I'm going to join back here on my phone and then listen in and then we can keep chatting. All right, I'll talk to you in a minute. Bye bye.
Adeleke Tolulope: No problem. Yeah.
Adeleke Tolulope: You did this. Jacob.
Jacob Oluwole: What's going on?
Jacob Oluwole: I could check generate. Yeah.
Adeleke Tolulope: Thank you.
Adeleke Tolulope: data The only expected output that the model is expected to return back is only in quotes.
Adeleke Tolulope: So you get most of back end code base and…
Jacob Oluwole: only in quotes.
Jacob Oluwole: Mhm. Yeah.
Adeleke Tolulope: most of okay I need right to create this fun to create this kind of function or to create an employee function that get all user information right that's my function yeah do a database that's how I was able
Adeleke Tolulope: to any question where I need you to write a function to update maybe users and maybe client update you get and now pass a prompt now that wants the model to analyze so you get to analyze code give it recommendations and all  And I didn't train him with that. But I'm even thinking that he should still be able to make use of his general knowledge, To handle that database code should be to write codes not to give you analysis of okay to improve this thing.
Jacob Oluwole: At normal code.
Adeleke Tolulope: Just I didn't train it like that. Send the prompts here. Right. This is where you send the prompt. Let me show you the prompt. This is where I pass in the prompt. The prompt gets to this part. Right. Identify the redundant logic or unnecessary competition.
Jacob Oluwole: Mhm. Mhm.
Adeleke Tolulope: Suggest alternative approach. Highlight potential bugs or edge. Recommend improvement in com.
Adeleke Tolulope: So response employer over Create the user account here employer profile to  you get add the error handling this creation of this what is it called the employer of the employer the error handling and all error why
00:45:00
Adeleke Tolulope: Here. Then it throws some other error within the code.
Jacob Oluwole: Wait, wait,…
Jacob Oluwole: Difference making it was still same code to generate.
Adeleke Tolulope: It was the same code.
Jacob Oluwole: Okay.
Adeleke Tolulope: It was same code but it gets necessary.
Jacob Oluwole: S you So first one correct. Second
Adeleke Tolulope: Second is the one that is wrong now.
Adeleke Tolulope: correct this code, right? I only want an improvement on the yee profile. Let's see the result. Try employee if not go reg x validation of phone number employee account but then same question alpha
Adeleke Tolulope: Analyze the difference between this code. Then paste our original code. Mhm. I swear me a lot of stress.
Jacob Oluwole: Windows vin
Adeleke Tolulope: I swear one one more time. I copy one one after the other.
Adeleke Tolulope: Yeah, let's see what go to your employer party. Certain let's conduct a thorough analysis of the two functions.  Assess their efficiency and identify which one is superior based on various criteria such as Both function aim to Your create employer here you get fetching retrieving user information from the user collection provided by check. Okay.
Jacob Oluwole: Okay. Okay. However,…
Adeleke Tolulope: Exactly. Mhm. Yeah.
Jacob Oluwole: there's notable difference between two implementation that impact the fitness of the One upper body.
Adeleke Tolulope: Let's Detailed compation code. Approach checks if user phone number is either missing or not Validated phone number include plus one or does not include plus. Pro simple and straightforward con inadequate validation. The condition phone number is ambiguous and may not validate phone numbers. It allows any phone number that either contains plus one or lacks a plus which can include invalid format. could be JavaScript. Okay.
Adeleke Tolulope: So approach utilize regular expression to validate the phone number format.  First condition checks if the phone number does not match digit three digit right just like our US numbers in or matches + one this applies different error message based on whether an employee gets robust validation uses reg to ensure phone number follow specific patterns reducing the chance of invalid format differentiated  error messages based on the existence of an employee account providing clearer feedback.
00:50:00
Adeleke Tolulope: complexity can be hard to read and maintain especially for developers unfamiliar with it regation. I always charge everything because I don't forget.  So conclusion could be B offers more precise and robust phone number validation using g X ensuring that only correct formatted phone numbers are accepted. This reduce the likelihood of invalid data entering the error handling and validation logic single error conditions if the phone number is m or invalid.
Adeleke Tolulope: Additional error check throws already if data update user document and if missing okay could be multiple error conditions. true specific message based on different scenarios. invalid existing phone number both email and phone number conflict. profile ID referral handling does not handle updating the user documents with managing referral information. and we need this Update the profile ID and we need this profile For every user coming to the website, you must have a profile ID.
Adeleke Tolulope: Even before you create a profile or you must even while create profile ID making of their unique name. you get but code B does not provide a profile ID but it improve the error what is it called the error handling.  Conclusion would be provides more granular error handling by distinguishing between various failure scenarios which can enhance user experience by offering clearer guidance on what needs to be corrected. However, it lacks some data integrity measures present in code such as updating the user document with essential information. Okay.
Adeleke Tolulope: improve validation part and data Could A ensure compressive data integrity by updating user which are crit which are critical for maintaining consistency.  While assigning additional fields to profile bricks does not have essential aspect like profile ID and reference potentially leading to data return values couldn't return client profile if successful otherwise return no does not return the created profile except if error cases could provide more feedback
Adeleke Tolulope: back by returning the profile or null which can be useful for subsequent operations or confirmations could be lack explicit return statement making it less transparent in terms of output.
Jacob Oluwole: number.
Adeleke Tolulope: So that way the only part to improve the validation of the phone number let me check the good Final assessment based on detail and code and could be as their strength and weakness. Could they proves compressive data integrity and require information unique profile generation recommendation?
Adeleke Tolulope: about that with both functions serve the primary purpose of creating an employee profile. Could they provide a more comprehensive and maintainable by ensuring data integrity handling referrals and maintain a consistent structure? could be introduced more precise phone number validation and profile picture board but falls short in maintaining data consistency and offering structured error handling by adopting the strength of both implementation primarily the comprehensive data management from and the robotization of can achieve more efficient and…
00:55:00
Jacob Oluwole: You leave now.
Adeleke Tolulope: reliable function. Wow.
Adeleke Tolulope: That mean we need to improve I think of the error handling and the updating of information.  But at first, even though it's not perfect now, I'm still very very happy that I'm able to come up with this kind of model because
Adeleke Tolulope: because I'm not even expecting anything outside JavaScript…
Adeleke Tolulope: but this one even though it needs some correct data structure and data set and some serious training at least it's still returning our code in our format and making it own changes to it even though those Chinese are not really really good,
Jacob Oluwole: That's squeezing.
Jacob Oluwole: That's good. How do we move from here to next place like this?
Jacob Oluwole: Maybe let's try this function function.
Adeleke Tolulope: Maybe. Yeah,…
Adeleke Tolulope: he got move. Yeah. cleaning please features new features outside our
Jacob Oluwole: Microsoft mech.
Adeleke Tolulope: Please new features. balance for more than 3 hours that I can use it.
Jacob Oluwole: Okay. okay.
Adeleke Tolulope: Let me
Jacob Oluwole: No Confessor. create me an employer account so that the person will log in  signs after signing up
Jacob Oluwole: So Functionality. create employh.
Adeleke Tolulope: process. Then you sign up for Mhm.
Jacob Oluwole: So once the employer signs up it will need to fill the prof all the fields are important list fields here understand this is good create me an employer account to create an employer account and…
01:00:00
Adeleke Tolulope: No, no, no, no, no. Mhm.
Jacob Oluwole: the employers signs up like comma such that the employer signs up on the website fills out the forms the questions…
Jacob Oluwole: which are name of sa upload a profile picture.
Adeleke Tolulope: Take a couple question.
Jacob Oluwole: She understand. Don't do anything. She understand. That's the reason.
Adeleke Tolulope: Fill out the form which includes the name,…
Jacob Oluwole: Name of company.
Adeleke Tolulope: the company name,…
Jacob Oluwole: Name of company. category.
Adeleke Tolulope: the company name.
Jacob Oluwole: Ein required ENI…
Adeleke Tolulope: Stered registration number. Mhm. the 99 and…
Jacob Oluwole: which bracket zero not required.
Adeleke Tolulope: required. Mhm.
Jacob Oluwole: Company website not required. Number of employers size of company in number number of type of company number.
Adeleke Tolulope: Wait. Type of company number.
Adeleke Tolulope: How? Okay.
Jacob Oluwole: Size size company employ in numbers number of employees number like an integer understand integer.
Adeleke Tolulope: Mhm. What color?
Jacob Oluwole: And…
Adeleke Tolulope: Work power.
Jacob Oluwole: then what are like…
Jacob Oluwole: what work work hour start time end profile for logo.
Adeleke Tolulope: Okay. What else?
Adeleke Tolulope: I think that was No, later.
Jacob Oluwole: Okay. So, write me a function that  Write me a function that Write me a function that creates Yeah. I think that'll do now.
Andrés Felipe Urrego Martínez: Hey guys, how are you guys?
Jacob Oluwole: Good. …
01:05:00
Jacob Oluwole: Steve power is currently off.
Andrés Felipe Urrego Martínez: Okay, that's fine.
Jacob Oluwole: So, yeah.
Andrés Felipe Urrego Martínez: That's Jump off. Let me know If you guys are connected later, just let me know and I'll jump on a call and I'll jump on the call with you guys. I'm actually going to go right now into the parent teachers conference. So I'll talk to you guys later. Okay. Okay.
Jacob Oluwole: Steve, are you back? I think.
Adeleke Tolulope: Hello. yeah,…
Jacob Oluwole: Yeah, your PC is All right.
Adeleke Tolulope: my name is no power on my system.
Andrés Felipe Urrego Martínez: But I have to jump off. I just want to let you guys know that. So, let me know once you have power and then I'll jump back on later. We can talk in a couple of hours if you guys are still up. If not, then we can do it tomorrow.
Adeleke Tolulope: Okay, Okay, sir.
Andrés Felipe Urrego Martínez: right, guys. I'll talk to you soon. Thank you. Bye.
Adeleke Tolulope: Just keep buying to buy.
Jacob Oluwole: Love me. I'm not again.
Meeting ended after 01:06:59 👋
This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

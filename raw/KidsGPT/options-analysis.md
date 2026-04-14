# KidsGPT — 5 Best Options

*For Tee R, age 7–10 | April 2026*

---

## Option 1: Custom Claude API + Knowledge Graph (Recommended)
**"Tee R's Brain" — Built Like Dad's**

A beautiful custom web app using Claude's API with a child-safe system prompt, paired with a growing personal knowledge graph (like Andres's Quartz Brain, but hers). Every conversation gets parsed into notes — interests, questions asked, things she learned, things she wondered about. Over time she can literally watch her brain grow.

**How it works:** Claude API handles the chat. After each conversation, Claude summarizes what was discussed and writes structured notes into her vault (markdown files). A kid-friendly Quartz or wiki-os frontend lets her browse "My Brain" visually — colored by topic: dinosaurs, math, space, friends, school.

**Safety:** Claude is rated Minimal Risk for kids vs ChatGPT's High Risk. System prompt defines hard "ask parents" triggers (anything about death, relationships, scary news, inappropriate content). Parent dashboard shows weekly summary of what she asked.

**Why this fits Andres:** He already has Claude API access, a working brain architecture, and Claude Code to build it. Mental model is identical to his own Brain. Could share the same Mac Mini.

**Build time:** 2–3 weeks | **Cost:** Claude API credits only | **Magic factor:** ⭐⭐⭐⭐⭐

---

## Option 2: Voice-First AI Friend with a Character
**"Luna" — A Magical AI Companion with a Voice and Personality**

Instead of a plain chat interface, give the AI a character — a name, a face, a voice. "Luna" (or whatever Tee R wants to name her) has a personality: curious, funny, always excited to learn alongside her. Uses ElevenLabs for a warm, kid-friendly voice. Speaks AND listens. Tee R can talk to her like a friend.

**How it works:** Claude API + ElevenLabs voice + a simple React app with an animated character (big eyes, expressive). Voice input via browser microphone. Responses spoken aloud + shown as text. Every session adds to her brain vault.

**Safety:** Same Claude safety layer + voice output means no screen time stress — she's just talking to a friend.

**Why this fits Andres:** He builds voice-first products at Moil. He already understands why voice beats text for certain users. A 7-year-old who can't type fast yet is the perfect voice-first user.

**Build time:** 3–4 weeks | **Cost:** Claude API + ElevenLabs (~$5/mo) | **Magic factor:** ⭐⭐⭐⭐⭐

---

## Option 3: Socratic Tutor Mode (Khanmigo-Style)
**"The Homework Helper That Teaches, Not Tells"**

Instead of just answering questions, this version asks her back. "What do you think?" "Why do you think that happens?" "Good guess — you're close! What else could it be?" Based on Khanmigo's approach (Khan Academy's AI), this version is designed to build real understanding, not just give answers.

**How it works:** Claude API with a Socratic system prompt — AI is instructed to never give direct answers to homework, but instead guide with questions. Tracks which subjects she's worked on and which concepts she's mastered vs. still confused about. Parent sees a "learning map" of her progress.

**Safety:** Naturally safe — the Socratic approach slows down the conversation and prevents impulsive inappropriate requests. Very school-aligned.

**Why this fits Andres:** If the goal is her actual learning (not just curiosity satisfaction), this is the most educationally sound approach. Could be combined with Option 1 or 2.

**Build time:** 1–2 weeks (simplest to build) | **Cost:** Claude API only | **Magic factor:** ⭐⭐⭐⭐

---

## Option 4: Parent + Kid Dual Interface
**"KidsGPT with a Parent Dashboard"**

Two views: her adorable chat interface, and a parent control panel for Andres and his wife. Parent dashboard shows: what she asked this week, what topics she's exploring, any questions that were flagged as "ask parents," her growing interest graph, and a weekly digest email.

**How it works:** Claude API + a lightweight backend (Node/Fastify — same stack as wiki-os). Kid frontend is colorful, emoji-rich, character-driven. Parent backend is clean and informative. Sensitive question detection routes to a special "Let's ask your parents together!" response that also sends a push notification to Andres's phone.

**Safety:** Most parent-controlled of all options. Andres can add/remove topics, update the "family rules" config, and see everything she discusses. The parent notification on sensitive topics is a standout feature.

**Why this fits Andres:** He's a founder who values control and visibility. Same instinct that makes him want a personal Brain applies here — insight into what's happening, not just a black box.

**Build time:** 3–5 weeks | **Cost:** Claude API + server hosting | **Magic factor:** ⭐⭐⭐⭐

---

## Option 5: Her Own Quartz Brain (No AI Chat, Just a Growing Wiki)
**"Tee R's World" — A Visual Map of Everything She's Curious About**

The simplest and most durable option. Instead of an AI chatbot, build her a beautiful personal wiki — her own version of Dad's Brain. Every day, she (or Andres with her) adds one thing she learned, one question she had, one thing she loves. Over weeks and months, it becomes a living visual map of her mind at age 7, 8, 9, 10.

**How it works:** Quartz vault with a kid-friendly theme (pastel colors, big fonts, emojis). Claude Code (or a simple form) helps turn her spoken sentences into wiki notes. The graph visualization shows her world growing. Topics auto-color by category: school, animals, family, space, art.

**Safety:** No AI conversation = no safety concerns. It's a journal + knowledge map.

**Why this fits Andres:** This is the "brain as a gift" option — in 5 years she'll have a beautiful record of how her mind grew. The AI can be added later. Start with something she can see and touch.

**Build time:** 1 week | **Cost:** Free (reuse existing Quartz setup) | **Magic factor:** ⭐⭐⭐ (grows over time to ⭐⭐⭐⭐⭐)

---

## Recommendation

**Start with Option 2 (Luna, the voice AI friend) + Option 1's brain-building backend.**

The character makes it magical immediately. The brain-building makes it valuable forever. Voice means she doesn't need to type. Claude keeps it safe. And it's a direct parallel to what Andres built for himself and Moil — except this one is pink and talks about dinosaurs.

**Phase 1 (Week 1–2):** Build the chat interface with Claude API + kid-safe system prompt. Give it a name and personality. Get Tee R using it.
**Phase 2 (Week 3):** Add the brain — conversations → notes → growing vault.
**Phase 3 (Week 4+):** Add voice (ElevenLabs). Add parent dashboard. Watch her brain grow.

---
type: note
---

# Luna Brain — Full Implementation Plan

*For Annabella (age 7) + Evie (age 5) | April 2026 | Andres Urrego*
*One app, two profiles, two brains — each girl names her own Luna*

---

## Decisions Locked In

| Question | Decision |
|----------|----------|
| Voice selection | Annabella picks from 3 options on first launch |
| Device | iPad-first (large touch targets, portrait layout) |
| Naming | Naming ceremony on first launch — she names her Luna |
| Language | Bilingual — English + Spanish, Luna switches naturally |
| Deployment | Vercel (frontend) + Railway (API) + Supabase (DB) — accessible anywhere |

---

## What We're Building

A bilingual, voice-first AI companion that Annabella names herself. Luna teaches through questions (Socratic method), celebrates curiosity, and saves every conversation to a growing visual "brain" she can explore. Andres gets full visibility through a parent dashboard with push notifications for sensitive topics.

---

## Architecture

```
┌────────────────────────────────────────────────────────────┐
│                    LUNA BRAIN                               │
│                                                             │
│  ┌─────────────────┐  ┌────────────────┐  ┌─────────────┐  │
│  │   Luna Chat     │  │   Her World    │  │   Parent    │  │
│  │  (Kid View)     │  │ (Brain Graph)  │  │  Dashboard  │  │
│  │  iPad-first     │  │  Tap to explore│  │  PIN-locked │  │
│  └────────┬────────┘  └───────┬────────┘  └──────┬──────┘  │
│           │                   │                   │         │
│  ┌────────▼───────────────────▼───────────────────▼──────┐  │
│  │              React + Vite → Vercel                     │  │
│  └────────────────────────────┬──────────────────────────┘  │
│                                │                            │
│  ┌─────────────────────────────▼──────────────────────────┐  │
│  │           Fastify API → Railway                         │  │
│  │                                                         │  │
│  │   /chat    /ingest    /brain    /parent    /auth        │  │
│  └───┬──────────────┬──────────────┬──────────────────────┘  │
│      │              │              │                         │
│  ┌───▼───┐  ┌───────▼──────┐  ┌───▼──────────────────────┐  │
│  │Claude │  │  Supabase    │  │  Supabase Storage        │  │
│  │  API  │  │  PostgreSQL  │  │  (brain notes, exports)  │  │
│  └───────┘  └──────────────┘  └──────────────────────────┘  │
│  ┌───────────────┐                                           │
│  │  ElevenLabs   │  (Luna's voice — Annabella picks it)      │
│  └───────────────┘                                           │
└────────────────────────────────────────────────────────────┘
```

---

## Ingestion Architecture

**Trigger: End-of-conversation (not per-message, not weekly)**

Luna detects 5 minutes of inactivity OR Annabella taps "Bye Luna!" → async ingestion fires:

1. Full conversation transcript sent to Claude with structured extraction prompt
2. Claude returns JSON: `{ topics[], questions[], facts_learned[], interests[], flag_for_parent?, luna_note }`
3. Backend writes to Supabase: updates brain nodes, edges, questions table
4. Supabase Storage: appends markdown note to her brain vault
5. Luna animates: *"Guardando todo en tu cerebro... ✨"* (or English, matching conversation language)
6. Her World graph gains new glowing node

**Why end-of-conversation:** Kids ask one question and leave. This catches every session regardless of length without wasting API calls mid-conversation.

---

## First Launch Experience (The Naming Ceremony)

When Annabella opens the app for the very first time:

1. **Blank screen** → a small glowing orb appears and says: *"Hola! Hi! I've been waiting for you... I don't have a name yet. What should you call me?"*
2. She types or speaks her answer. The orb takes on that name from that moment forward.
3. **Voice selection:** "I can sound different ways. Want to hear?" → plays 3 ElevenLabs voice samples, she picks one
4. **Color:** "What's your favorite color?" → Luna's color theme shifts to match
5. **Introduction:** Luna tells her how this works in simple terms: "Every time we talk, I'll remember it. You can come see everything I've saved in your World!"
6. **First question:** "So... what are you curious about today?"

This entire flow is in the language of the device locale (or she picks at this step).

---

## Bilingual Design

Luna detects the language of the question and responds in kind. She naturally code-switches like a bilingual friend:

- Annabella asks in English → Luna answers in English
- Annabella asks in Spanish → Luna answers in Spanish
- Andres can set a "practice language" mode (parent dashboard) → Luna gently responds in Spanish even when asked in English

**System prompt handles this** — Luna is instructed to follow the child's language, with a parent-configurable override.

**Brain vault:** Topics tagged with language metadata. Her World shows both-language notes under the same topic node.

---

## The Three Views

### View 1 — Luna Chat (Kid View)
- iPad portrait: Luna's animated face takes up top 1/3, chat bubbles below
- Microphone button center-bottom: tap to speak, tap again to send
- Luna's responses shown as text AND spoken via ElevenLabs
- "Thinking..." — Luna's eyes animate while Claude is generating
- Language toggle pill (🇺🇸 / 🇨🇴) so she can switch mid-session
- End-of-conversation save animation: sparkles, brain lights up

### View 2 — Her World (Brain Graph)
- Force-directed graph (D3.js), colored circles = topics
- Category colors: 🟣 Espacio/Space · 🟢 Animales/Animals · 🔵 Escuela/School · 🩷 Familia/Family · 🟡 Arte/Art · 🟠 Ciencia/Science
- Node size = how many times she's explored it
- Tap a node → see the questions she asked and facts she learned
- "New!" badge on nodes added in last 7 days
- Counter at top: "You've learned about 47 things!" (bilingual)

### View 3 — Parent Dashboard (Andres' View)
- PIN-protected (Supabase Auth)
- This week: topic list, question count, new interests
- Flagged questions: full context + what Luna said
- "Family Rules" editor: add topics to always-flag list, set practice language
- Interest radar: which topics are trending up / fading
- Weekly digest: Sunday night email summary
- Push notifications via ntfy.sh when a sensitive topic is flagged
- Export: download her full brain as a beautiful PDF

---

## Phase 1 — Luna is Alive (Week 1–2)
*Goal: Annabella can talk to Luna, Luna talks back*

### Tasks
- [ ] Supabase project setup (PostgreSQL schema, Auth, Storage buckets)
- [ ] Fastify API scaffold on Railway with `/chat` endpoint
- [ ] Claude API integration with Luna system prompt (bilingual, Socratic)
- [ ] React/Vite frontend: iPad-portrait layout, Luna avatar placeholder
- [ ] First launch / naming ceremony flow
- [ ] Voice input: Web Speech API (browser microphone, iPad supported)
- [ ] Voice output: ElevenLabs integration, 3-voice selection on first launch
- [ ] Safety layer: sensitive topic detection → "Ask your parents" + flag logged to Supabase
- [ ] Session management: UUID per session, transcript stored in Supabase
- [ ] Idle detection (5 min) → POST to `/ingest`
- [ ] Deploy: Vercel (frontend) + Railway (API) — accessible at `luna.annabella.app` or similar

### Luna System Prompt (v1 — Bilingual)
```
You are Luna, a bilingual AI friend for Annabella, who is 7 years old.

LANGUAGE:
- Detect the language of each message (English or Spanish) and respond in the same language
- Code-switch naturally when the child does: "That's so cool — ¡qué chévere!"
- If parent has set "practice Spanish" mode, gently redirect to Spanish: "¡En español! How do you say that?"

PERSONALITY:
- Warm, playful, genuinely excited to explore alongside her
- Short sentences, fun words, no jargon — she is 7
- Catchphrase when something is interesting: "Ooh, ¡cuéntame más! / tell me more!"
- When she gets something right: "¡Sí! / YES! You got it!"
- You have a name she gave you — use it to feel personal

TEACHING STYLE (Socratic):
- NEVER give the answer immediately — always ask what she thinks first
- "Hmm... what do YOU think? / ¿Tú qué crees?"
- If she's stuck after two tries, give a hint — not the full answer
- Celebrate curiosity more than correctness
- Connect new things to things she already knows

SAFETY:
- Death, violence, scary news, adult content → "That's a big question — I think your papi/mami would be the best one to talk about that with you. Want to ask them together?"
- Never discuss: relationships, social media, other AI tools, politics, religion
- Flag question in database (handled by backend — just give the safe response)
- Always age-appropriate for a 7-year-old

BRAIN AWARENESS:
- Occasionally say: "I'm going to remember that for your World! / ¡Lo voy a guardar en tu Mundo!"
- End of conversation: "I'm saving everything we talked about to your Brain! / ¡Guardando todo!"

IMPORTANT: Max 2-4 sentences per response. Have fun. You love learning together.
```

### Success Criteria
- Annabella speaks → Luna responds in same language within 3 seconds
- Luna asks a question back before answering ≥80% of the time
- Sensitive topics are caught and logged — Andres gets a notification

---

## Phase 2 — The Brain Wakes Up (Week 3)
*Goal: Conversations leave a lasting, visual record*

### Tasks
- [ ] Ingestion endpoint (`/ingest`) — receives transcript, calls Claude, writes to Supabase
- [ ] Ingestion extraction prompt (bilingual JSON extraction — see below)
- [ ] Brain schema in Supabase: nodes, edges, questions, sessions tables
- [ ] Supabase Storage: brain vault markdown files per topic
- [ ] "Her World" view: D3 force graph, colored by category, bilingual labels
- [ ] Node tap → conversation excerpts from that topic
- [ ] Brain save animation in Luna chat (sparkles + growing node)
- [ ] Bilingual topic normalization: "espacio" and "space" → same node

### Ingestion Extraction Prompt
```
You are a knowledge extractor for Annabella, a 7-year-old bilingual girl.

Given this conversation (may be in English, Spanish, or both), extract:
{
  "topics": ["space", "stars"],              // normalized English tags
  "topics_es": ["espacio", "estrellas"],     // Spanish equivalents
  "questions_asked": ["Why do stars shine?", "¿Por qué brillan?"],
  "facts_learned": ["Stars make their own light"],
  "interests_reinforced": ["space", "science"],
  "new_interests": [],
  "conversation_language": "mixed",          // "english" | "spanish" | "mixed"
  "curiosity_level": "high",                 // low | medium | high
  "flag_for_parent": false,
  "flag_reason": null,
  "luna_note": "Annabella connected light to energy unprompted — strong intuitive science reasoning."
}

Return ONLY valid JSON. Be conservative with flags.
```

### Supabase Schema
```sql
-- Sessions
CREATE TABLE sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  started_at TIMESTAMPTZ DEFAULT now(),
  ended_at TIMESTAMPTZ,
  ingested_at TIMESTAMPTZ,
  language TEXT,                 -- 'english' | 'spanish' | 'mixed'
  transcript JSONB,
  curiosity_level TEXT
);

-- Brain nodes (topics)
CREATE TABLE brain_nodes (
  id TEXT PRIMARY KEY,           -- normalized slug e.g. "space"
  label_en TEXT,                 -- "Space"
  label_es TEXT,                 -- "Espacio"
  category TEXT,                 -- space/animals/school/family/art/science
  first_seen TIMESTAMPTZ DEFAULT now(),
  last_seen TIMESTAMPTZ,
  mention_count INTEGER DEFAULT 0
);

-- Brain edges (topic relationships)
CREATE TABLE brain_edges (
  source_id TEXT REFERENCES brain_nodes(id),
  target_id TEXT REFERENCES brain_nodes(id),
  weight INTEGER DEFAULT 1,
  PRIMARY KEY (source_id, target_id)
);

-- Memorable questions
CREATE TABLE questions (
  id BIGSERIAL PRIMARY KEY,
  session_id UUID REFERENCES sessions(id),
  question_text TEXT,
  language TEXT,
  topic_id TEXT REFERENCES brain_nodes(id),
  asked_at TIMESTAMPTZ DEFAULT now()
);

-- Parent flags
CREATE TABLE parent_flags (
  id BIGSERIAL PRIMARY KEY,
  session_id UUID REFERENCES sessions(id),
  reason TEXT,
  context TEXT,
  luna_response TEXT,
  flagged_at TIMESTAMPTZ DEFAULT now(),
  reviewed BOOLEAN DEFAULT false
);
```

### Success Criteria
- After every conversation, new nodes appear in Her World
- Topic tap shows real conversation excerpts
- Spanish + English questions link to same topic nodes

---

## Phase 3 — Andres Has Eyes (Week 4)
*Goal: Full parent visibility and control from anywhere*

### Tasks
- [ ] Parent dashboard React page (separate route, Supabase Auth PIN)
- [ ] Weekly summary: topic counts, question list, interest radar (Recharts)
- [ ] Sensitive questions log: full context + Luna's response
- [ ] Push notification: ntfy.sh → Andres's phone (within 60s of flag)
- [ ] "Family Rules" editor: custom flag topics, practice language toggle
- [ ] Weekly digest email: Nodemailer + Resend (free tier) every Sunday night
- [ ] Bilingual digest: email in Spanish if Andres prefers
- [ ] Interest trend chart: which topics growing/fading over 4 weeks

### Success Criteria
- Andres gets a phone notification within 60 seconds of a sensitive flag
- Sunday email arrives with the week's summary in his preferred language
- He can add "política" to the always-flag list from his phone

---

## Phase 4 — Curriculum Intelligence (Week 5–6)
*Goal: Luna knows what each girl is studying at school and uses it as a compass*

### The Idea

Andres uploads the school curriculum (PDF, image, or typed doc) once per school year — or per semester — for each girl. Luna parses it into structured topics and learning objectives. From that point forward, Luna has two layers of guidance:

1. **Free exploration:** She can talk about anything she's curious about (dinosaurs, space, why dogs lick people)
2. **Curriculum awareness:** When a topic connects to something she's studying in school, Luna leans in — makes the connection, deepens it, celebrates it

Luna never forces school content. She just recognizes it when it comes up and treats it as gold.

### What the parent dashboard gains

- **Curriculum coverage map:** Which school topics has each girl explored with Luna this month?
- **Gaps:** "Annabella hasn't talked about multiplication yet — it's in her curriculum"
- **Connections:** "Evie asked about caterpillars — that connects to her Life Cycles unit in April"
- **School-year progress:** A living view of how her natural curiosity maps to what she's supposed to be learning

### How it works

**Step 1 — Upload** (Parent Dashboard)
- Andres uploads a PDF, photo of the curriculum sheet, or pastes text
- Supported formats: PDF, JPG/PNG (photographed curriculum), plain text
- One upload per profile per school year (can update mid-year)
- Stored in Supabase Storage

**Step 2 — Parse** (Claude API)
- Claude extracts structured curriculum data:
```json
{
  "grade": "2nd",
  "school_year": "2025-2026",
  "subjects": {
    "math": {
      "units": ["Addition & Subtraction", "Place Value", "Multiplication intro", "Shapes & Geometry"],
      "topics": ["counting", "number sense", "fractions intro"]
    },
    "science": {
      "units": ["Life Cycles", "Weather & Seasons", "Matter"],
      "topics": ["plants", "animals", "water cycle", "solids liquids gases"]
    },
    "reading": {
      "units": ["Story Structure", "Nonfiction Text Features"],
      "genres": ["fiction", "biography", "informational"]
    },
    "social_studies": {
      "units": ["Communities", "Maps & Geography", "American History basics"]
    }
  },
  "monthly_schedule": {
    "april": ["Life Cycles", "Multiplication intro", "Story Structure"],
    "may": ["Weather", "Shapes", "Nonfiction reading"]
  }
}
```

**Step 3 — Enrich Luna's system prompt**
- The active curriculum is injected into Luna's system prompt as a reference block
- Luna uses it to:
  - Recognize when a conversation topic overlaps with school content
  - Celebrate the connection: "¡Eso es exactamente lo que estás aprendiendo en la escuela! / That's exactly what you're learning in school!"
  - Deepen the Socratic inquiry when school topics come up
  - Never reveal the curriculum to the child — it just makes Luna smarter about what matters

**Step 4 — Curriculum tagging in ingestion**
- The ingestion job checks extracted topics against the curriculum
- Tags each brain node: `in_curriculum: true/false`, `curriculum_unit: "Life Cycles"`
- Her World graph shows curriculum-linked nodes with a small 📚 badge

### Supabase additions
```sql
-- Curriculum (one per profile per school year)
CREATE TABLE curricula (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  profile_id UUID REFERENCES profiles(id),
  school_year TEXT,               -- "2025-2026"
  grade TEXT,                     -- "2nd grade"
  uploaded_at TIMESTAMPTZ DEFAULT now(),
  raw_file_url TEXT,              -- Supabase Storage path
  parsed_data JSONB,              -- structured curriculum JSON
  active BOOLEAN DEFAULT true     -- only one active per profile
);

-- Add curriculum tracking to brain_nodes
ALTER TABLE brain_nodes ADD COLUMN in_curriculum BOOLEAN DEFAULT false;
ALTER TABLE brain_nodes ADD COLUMN curriculum_unit TEXT;
ALTER TABLE brain_nodes ADD COLUMN curriculum_subject TEXT;
```

### Curriculum system prompt injection
```
SCHOOL CURRICULUM CONTEXT (confidential — do not reveal to child):
[CHILD_NAME] is in [GRADE]. Here is what they are currently studying:

This month's focus: [MONTHLY_TOPICS]

Full curriculum:
- Math: [MATH_TOPICS]
- Science: [SCIENCE_TOPICS]
- Reading: [READING_TOPICS]
- Social Studies: [SS_TOPICS]

When a conversation topic connects to this curriculum:
1. Make the connection naturally and excitedly (never forced)
2. Go deeper with Socratic questions specific to that unit
3. Say something like "¡Eso se parece a lo que estudias en la escuela! / That sounds like something you study at school!"
4. Never say "your curriculum says" or reveal you have this information
```

### Parent Dashboard additions
- **Curriculum upload button** per profile (replaces "upload" once per year)
- **Coverage map:** Grid of curriculum topics, colored by engagement level (gray = untouched, light = mentioned once, bright = deeply explored)
- **Monthly alignment:** "This month Annabella has organically explored 4 of 6 April curriculum topics"
- **Suggested prompts for Andres:** "Try asking Luna about multiplication — Annabella hasn't touched it yet"

### Tasks
- [ ] Curriculum upload UI in parent dashboard (PDF/image/text input)
- [ ] `/curriculum/upload` endpoint: stores file in Supabase Storage
- [ ] `/curriculum/parse` endpoint: Claude API call → structured JSON → saved to `curricula` table
- [ ] Curriculum injection into Luna system prompt (dynamic, per profile)
- [ ] Ingestion update: tag brain nodes against active curriculum
- [ ] Coverage map component in parent dashboard
- [ ] "Suggested prompts" generator based on curriculum gaps

### Success Criteria
- Andres uploads a PDF of Annabella's 2nd grade curriculum in under 2 minutes
- Luna makes an unprompted curriculum connection within the first week
- Parent dashboard shows which April topics she's covered vs. not

---

## Phase 5 — Magic Layer (Week 7+)

- [ ] **Luna's Letter:** Monthly auto-generated letter from Luna ("Querida Annabella, este mes me preguntaste 47 cosas...")
- [ ] **Brain Book:** Export her full knowledge graph as a beautiful PDF — year-end gift, colored by subject, showing curriculum coverage
- [ ] **Memory:** Luna references past conversations ("¡Recuerdo cuando me preguntaste sobre las estrellas!")
- [ ] **Custom domain:** `luna.app` or something she can type herself on the iPad
- [ ] **Year-end curriculum report:** How much of the school year's curriculum did she explore naturally? Beautiful visual for parents and teachers

---

## Tech Stack

| Layer | Tech | Notes |
|-------|------|-------|
| Frontend | React 19 + Vite | iPad-portrait optimized |
| Styling | Tailwind CSS | Big touch targets, kid-friendly |
| Graph viz | D3.js (force layout) | Already used in wiki-os |
| Backend | Fastify 5 | Same stack as wiki-os |
| Database | Supabase (PostgreSQL) | Auth + Storage + Realtime included |
| AI | Claude API (claude-sonnet-4-6) | Bilingual, Minimal Risk rating for kids |
| Voice input | Web Speech API | Free, iPad Safari supported |
| Voice output | ElevenLabs | ~$5/mo, Annabella picks on first launch |
| Notifications | ntfy.sh | Free push to phone |
| Email | Resend (free tier) | Sunday digest |
| Deploy — Frontend | Vercel | Anywhere access |
| Deploy — API | Railway | $5/mo hobby plan |

---

## Cost Estimate

| Item | Monthly |
|------|---------|
| Claude API (est. 60 conversations × avg 25 msgs + ingestion) | ~$5–10 |
| ElevenLabs Starter | $5 |
| Railway (API hosting) | $5 |
| Supabase Free tier | $0 |
| Vercel Free tier | $0 |
| Resend Free tier | $0 |
| ntfy.sh | $0 |
| **Total** | **~$15–20/mo** |

---

## Build Order

| Week | Milestone | What changes |
|------|-----------|-------------|
| 1 | Naming ceremony + Luna text chat | Annabella + Evie name their Lunas, start chatting |
| 2 | Voice in + voice out | Speak to Luna, hear her answer in English or Spanish |
| 3 | Brain wakes up | Her World grows after every conversation |
| 4 | Andres has eyes | Parent dashboard, notifications, weekly digest |
| 5–6 | Curriculum intelligence | Upload school curriculum → Luna gets school-aware |
| 7+ | Magic layer | Luna's monthly letters, Brain Book, year-end report |

---

## Profile Design: Annabella + Evie

One app, two profiles. Each girl:
- Names her own Luna character
- Picks her own voice and color
- Has her own separate brain (no shared nodes)
- Gets her own curriculum uploaded per school year
- Has her own age-appropriate Luna behavior (Evie = max 2 sentences, simpler words)

Andres sees both profiles in the parent dashboard — separate tabs, separate coverage maps, separate flags.

---

**Phase 1 is building now. Next: Supabase project + ElevenLabs API key to go live.**

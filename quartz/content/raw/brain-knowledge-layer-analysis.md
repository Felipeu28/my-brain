# AI Knowledge Layer — Gap Analysis & Implementation Plan

*Based on: "AI Knowledge Layer (and why your agents are useless without it)" by @shannholmberg*
*Analyzed against: Andres's Brain (Quartz + wiki-os, April 2026)*

---

## What the Article Says

@shannholmberg built a two-layer knowledge system inspired by Andrej Karpathy's insight that AI token spend is shifting from code to knowledge management. The core problem: **your agents don't know you.** Every conversation starts from zero. You re-explain your business, voice, goals, and context every time — and the output is generic because the input has no memory.

### The Two-Layer System

**Layer 1 — Raw (the inbox)**
Everything dumps here: clippings, ideas, bookmarks, tweets, articles, transcripts. No structure required. Just capture.

**Layer 2 — Wiki (the compiled brain)**
An AI agent processes raw/ into structured, cross-linked wiki pages. Flat structure, wikilinks, source TLDRs, a master index. When you query it, you get cited answers from your own data — and those answers get filed back as new pages, so the next query is richer.

### The Folder Structure
```
my-wiki/
  raw/
    clippings/       ← Obsidian Web Clipper drops here automatically
    ideas/           ← notes, brainstorms, half-formed thoughts
    bookmarks/       ← saved tweets, threads, tools
    claude-superpowers.md
  sources/           ← one summary per raw source
    graphify-2026.md
  outputs/           ← filed answers to queries
  sops/              ← repeatable processes
  syntheses/         ← cross-cutting analysis
  templates/         ← page type starters
  CLAUDE.md          ← the schema that controls everything
```

### The Four Commands (in CLAUDE.md)
- **`/wiki-ingest`** — processes raw/ into structured wiki pages
- **`/wiki-query`** — asks questions, returns cited answers
- **`/wiki-explore`** — browses and validates pages
- **`/wiki-lint`** — catches contradictions, stale content, orphans

### The Capture Mechanism
Obsidian Web Clipper browser extension. One click while browsing X, reading an article, checking GitHub, or scrolling Reddit → saves to `raw/clippings/` with source URL and metadata. This is the **critical missing piece** most people overlook.

### The Scheduled Loop
A trigger runs `/wiki-ingest` every morning on whatever was clipped the day before. The brain gets smarter while you sleep. No manual curation session required — just clip during the day, ingest runs automatically overnight.

### The Quality Rule
If something isn't 80%+ relevant to what you're working on, skip it. High-signal inputs make the output better. Noise in = noise out.

---

## What Andres Has ✅

| Feature | Status | Notes |
|---------|--------|-------|
| Hub-and-spoke architecture | ✅ Strong | 12 hubs, better than flat wiki |
| Graph visualization | ✅ Better than article | Custom D3, hub colors, degree sizing — Shann just uses Obsidian default |
| Markdown vault | ✅ | Quartz content directory |
| CLAUDE.md / memory | ✅ Partial | auto-memory exists but not a full schema |
| Morning automation | ✅ Patched | Runs 8:45am, pushes to Vercel |
| Content calendar automation | ✅ Patched | Runs Mondays 9am |
| Chroma indexing | ✅ | Semantic search exists |
| Raw folder | ✅ Partial | `raw/` exists but only for briefings/calendar |
| People hub | ✅ | People Grid component, person pages |
| Summaries hub | ✅ | For meeting/conversation notes |
| Deployed publicly | ✅ Partial | Vercel works, GitHub Pages has private repo issue |
| X bookmarks automation | ✅ Exists | Runs Sundays 8pm |

---

## What Andres Is Missing ❌

| Feature | Gap | Priority |
|---------|-----|----------|
| **Web Clipper** | No one-click browser capture. Notes created manually or by scripts only. Can't clip an article mid-read. | 🔴 Critical |
| **`/wiki-ingest` command** | No pipeline to process raw notes into structured wiki pages. Scripts generate NEW content but don't process EXISTING raw inputs. | 🔴 Critical |
| **`/wiki-query` command** | No way to ask "what do I know about X?" and get cited answers from the Brain. | 🔴 Critical |
| **`/wiki-lint` command** | No automated quality control. We found 153 stub pages and 98 orphan nodes manually — but there's no ongoing detection. | 🟡 High |
| **TLDR master index** | No wiki/index.md with one-line summaries of every page. Hard to know what's in the Brain at a glance. | 🟡 High |
| **Source classification** | No tagging of source type (tweet, article, transcript, paper). Everything is equal weight. | 🟡 High |
| **Query → filed answer loop** | Answers aren't saved back as new wiki pages. The Brain doesn't get richer from being queried. | 🟡 High |
| **Two-layer separation** | `raw/` exists but mostly holds automation output, not a real capture inbox. The raw → wiki pipeline doesn't exist. | 🟠 Medium |
| **80% signal filter** | No curation rule. Everything gets added regardless of relevance. | 🟠 Medium |
| **Cross-linking quality** | Has wikilinks but 98 orphan nodes — pages exist that nothing links to. | 🟠 Medium |

---

## What Andres Is Doing Right (That the Article Doesn't Have)

1. **Hub-and-spoke architecture** is superior to the flat wiki structure Shann describes. Hub coloring, degree-weighted nodes, and the 12-hub taxonomy give the Brain real structure.
2. **Visual graph deployed publicly** — Shann's is local Obsidian. Andres's Brain is browsable from anywhere.
3. **Automation pipeline exists** — Morning briefing, content calendar, X bookmarks, weekly pulse. These are more sophisticated than what the article describes.
4. **People hub** — a dedicated people layer with visual grid. The article doesn't address this at all.
5. **wiki-os parallel** — the queryable backend that Shann is describing with `/wiki-query` is essentially what wiki-os is being built to do. Andres is ahead here architecturally, just not fully shipped.

---

## Research-Backed Implementation Plan

### Must-Have #1 — Obsidian Web Clipper Setup (Day 1, 20 min)

**What:** Install the Obsidian Web Clipper browser extension. Configure it to save to `quartz/content/raw/clippings/` with a standard template.

**Why:** This is the single highest-leverage change. Without frictionless capture, you'll never build up enough raw material for the ingest pipeline to be useful. Shann calls this "the critical missing piece most people overlook."

**Template to configure:**
```
---
source: {{url}}
type: {{auto-detect: article | tweet | thread | paper | tool}}
captured: {{date}}
title: {{title}}
tags: [raw, clipping]
---

{{selection or full article}}
```

**Action:** Install at obsidian.md/clipper → point vault to `~/My Brain/knowledge-base/quartz/content/raw/clippings/`

---

### Must-Have #2 — Add Four Commands to CLAUDE.md

**What:** Define four slash commands in `CLAUDE.md` so any Claude session in the Brain folder knows how to operate it.

**Why:** This is what makes the Brain an active system instead of a static archive. The commands are the "brain is queryable" layer.

```markdown
## Brain Commands

### /brain-ingest
Process everything in raw/ that hasn't been ingested yet.
For each file in raw/:
1. Read and classify (article | tweet | transcript | idea | bookmark)
2. Extract: key concepts, people mentioned, orgs mentioned, tldr (1-2 sentences)
3. Create or update a wiki page with wikilinks to existing hubs
4. Tag source with `ingested: true` and move to sources/
5. Update wiki/index.md with new TLDR entry
6. Commit and push

### /brain-query [question]
Answer a question using only knowledge in wiki/.
1. Search wiki/ for relevant pages
2. Return a cited answer with [[page]] references
3. Save the answer to outputs/YYYY-MM-DD-[slug].md
4. Update wiki/ if the answer reveals a gap or new connection

### /brain-explore [topic]
Browse a topic area in the brain.
1. Find all pages related to [topic]
2. Show connections, gaps, and related hubs
3. Suggest 3 pages that should exist but don't

### /brain-lint
Quality audit. Run monthly or after bulk ingestion.
1. Find all pages with fewer than 100 words (stubs)
2. Find all pages with no incoming wikilinks (orphans)
3. Find contradictions between pages on same topic
4. Report with suggested fixes, don't auto-fix
```

---

### Must-Have #3 — Daily Ingest Automation

**What:** Add a morning ingest step to the existing morning-briefing LaunchAgent. After generating the briefing, it also runs `/brain-ingest` on anything new in raw/clippings/.

**Why:** The compound effect. Shann's key insight is "your distribution gets smarter while you sleep." Each morning, yesterday's clippings become structured wiki pages.

**Add to `bin/morning-briefing.sh`:**
```bash
# After briefing generation — process any new clippings
CLIPPINGS_DIR="$WIKI_ROOT/raw/clippings"
if [ "$(ls -A $CLIPPINGS_DIR)" ]; then
  echo "Processing new clippings..."
  cd "$BRAIN_ROOT"
  claude --print "/brain-ingest" --model claude-sonnet-4-6
fi
```

---

### Must-Have #4 — TLDR Master Index

**What:** Create and maintain `quartz/content/wiki/index.md` — a single file with a one-line TLDR for every page in the wiki. Updated automatically after each ingest.

**Why:** This is how Claude (and you) can quickly orient inside the Brain without reading every page. The index becomes the map.

**Format:**
```markdown
# Brain Index
*Last updated: 2026-04-15 | 170 pages | 12 hubs*

## People (23 pages)
- [[megan-miller]] — FNP-C at Fit Logic Functional Medicine, HIVE connection, Moil customer
- [[dafne-gutierrez]] — [stub — needs expansion]

## Moil (18 pages)
- [[moil360]] — Marketing Pro tier ($75/mo), full feature set and pricing
...
```

---

### Must-Have #5 — Source Classification System

**What:** Add a `type` field to every raw/ file frontmatter. The ingest pipeline uses this to weight sources and structure extracted knowledge differently.

**Why:** A tweet and a research paper are not the same weight. A transcript contains different information than a bookmark. Source type changes how the agent extracts and cross-links.

**Types:**
- `tweet` — short claim, strong signal, cite with caution
- `thread` — expanded argument, good for concepts
- `article` — research, depth, full extraction
- `transcript` — conversation/call, extract people + decisions
- `paper` — academic source, highest trust weight
- `idea` — your own thinking, no source verification needed
- `bookmark` — low-friction save, low-priority ingest

---

## The 80% Signal Rule

Before adding anything to raw/, ask: is this 80%+ relevant to what I'm working on (Moil, AIbyAndres, Brain, community, family)?

If yes → clip it.
If no → let it go.

This is the hardest rule to follow and the most important one. The Brain is only as good as what goes in.

---

## Prioritized Action List

| Priority | Action | Time | Who |
|----------|--------|------|-----|
| 🔴 #1 | Install Obsidian Web Clipper, configure vault path | 20 min | Andres |
| 🔴 #2 | Add 4 commands to CLAUDE.md | 1 hour | Code task |
| 🔴 #3 | Build `/brain-ingest` as working script | 2-3 hours | Code task |
| 🔴 #4 | Build `/brain-query` endpoint in wiki-os | 2-3 hours | Code task |
| 🟡 #5 | Create and populate TLDR master index | 1 hour | Code task |
| 🟡 #6 | Add ingest step to morning-briefing script | 30 min | Code task |
| 🟡 #7 | Build `/brain-lint` as monthly audit script | 1 hour | Code task |
| 🟠 #8 | Add source type frontmatter to existing raw/ files | 30 min | Code task |
| 🟠 #9 | Implement 80% signal rule as personal practice | Ongoing | Andres |
| 🟠 #10 | Fix GitHub Pages private repo issue | 5 min | Andres |

---

## The Core Insight Applied to Andres's Brain

The article's thesis maps directly: **Claude doesn't know Andres yet.** Every Cowork session starts from zero — you explain Moil, your voice, your context again. The Brain exists as a visual artifact, but it doesn't feed Claude.

The missing connection is: **Brain → Claude context injection.**

The wiki-os `/brain-query` endpoint is the right architectural answer. When a Cowork session starts, it should optionally query the Brain for relevant context about the topic at hand. That's the feature that turns a passive knowledge archive into an active AI advantage.

**Reference:** [AI Knowledge Layer by @shannholmberg](https://x.com/shannholmberg/status/2044111115878326444) | [llm-wikid repo](https://github.com/shannhk/llm-wikid)

# Obsidian (Knowledge Management Tool)

**Type:** concept (tool)
**Last updated:** 2026-04-12
**Source:** [[raw/x-bookmarks-2026-04-11 copy]]
**Related:** [[wiki/concepts/llm-knowledge-bases]], [[wiki/concepts/brain-architecture]], [[wiki/concepts/claude-code]]

---

## Summary
Obsidian is a local-first markdown-based knowledge management app that uses wikilinks (`[[links]]`) to create a personal knowledge graph. It became a dominant topic in the Mar 26 – Apr 11 bookmark window due to the "Obsidian + Claude Code = second brain" wave triggered by Karpathy's LLM Knowledge Bases viral post. Multiple posts totaling 4M+ views specifically on the Obsidian + Claude integration.

## Why It Went Viral in This Period
- Karpathy's Apr 2 post used Obsidian as the review layer for his LLM wiki
- @defileo: "Claude + Obsidian have to be illegal" — 3.9M views (Apr 9)
- @cyrilXBT: "Obsidian + Claude Code = your own second brain" — 442K views video (Apr 7)
- @aiedge_: "Claude Code + Obsidian Ultimate Guide" (Apr 8)
- @KanikaBK: "6 FREE Obsidian plugins that replace $200 worth of paid apps" (Apr 10)

## Key Workflows

### Claude Code + Obsidian Second Brain
1. Keep your `wiki/` folder as an Obsidian vault (enable "Files and Links" → "Use wikilinks")
2. Claude Code writes and updates markdown in `wiki/`
3. Obsidian provides visual navigation (graph view, backlinks, Dataview queries)
4. Obsidian Web Clipper captures web sources to `raw/` for the next compile run

### Obsidian Plugins That Replace Paid Tools (@KanikaBK)
6 free plugins replace ~$200/mo of paid tools:
1. **Dataview** — query your notes like a database (replaces Notion for structured data)
2. **Calendar** — journal + daily notes with calendar UI
3. **Templater** — advanced templating (replaces Notion templates)
4. **Excalidraw** — whiteboard inside Obsidian (replaces Miro/Figma for quick diagrams)
5. **Kanban** — task boards (replaces Trello/Linear for personal projects)
6. **QuickAdd** — fast capture to any vault file (replaces dedicated capture apps)

## Connection to Moil Brain
The `~/My Brain/knowledge-base/wiki/` folder is already structured as an Obsidian vault-compatible directory — wikilinks, flat slugs, markdown-only. Per `~/My Brain/CLAUDE.md`, the `wiki/` and `outputs/` directories are intended to sync via iCloud so Andres can browse the Brain from any device. Obsidian is the intended human-facing interface.

## Connections
- Implements the view layer of [[wiki/concepts/llm-knowledge-bases]] and [[wiki/concepts/brain-architecture]]
- [[wiki/concepts/claude-code]] is the write/update engine; Obsidian is the browse/navigate engine
- The DESIGN.md open source collection (@nozmen, github: VoltAgent/awesome-design-md) is the Obsidian equivalent for design documentation

## Moil Relevance
If Andres enables Obsidian on the Brain today, he immediately gets:
- Graph view showing which Moil topics are most connected
- Daily notes for capturing decisions (feeds `wiki/meetings/`)
- Dataview queries like "show all people I haven't updated in 30 days" (relationship maintenance)
- Mobile access via Obsidian + iCloud sync

**Action:** Install Obsidian, point vault at `~/My Brain/knowledge-base/wiki/`, enable Dataview + Templater plugins.

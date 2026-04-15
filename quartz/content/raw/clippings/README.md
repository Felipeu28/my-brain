---
title: Clippings
tags: [raw, clippings, readme]
---

# Clippings

This is the drop zone for **Obsidian Web Clipper** captures — articles, tweets, threads, papers, and tools Andres saves from the browser. Files land here raw and get processed by `/brain-ingest` each morning.

## How it works

1. Obsidian Web Clipper saves to this folder
2. Each file starts with `ingested: false` in its frontmatter
3. The morning briefing script (`bin/morning-briefing.sh`) counts unprocessed clippings and logs them to the ingest queue
4. A Claude session running `/brain-ingest` processes the queue, extracts knowledge into `quartz/content/wiki/`, and flips the frontmatter to `ingested: true`
5. Files stay here as the immutable raw record — they are never deleted

## Recommended Obsidian Web Clipper template

Paste this into Obsidian Web Clipper → Settings → Templates → Properties:

```
---
source: {{url}}
type: {{auto-detect from URL: tweet | article | thread | paper | tool}}
captured: {{date:YYYY-MM-DD}}
title: {{title}}
tags: [raw, clipping]
ingested: false
---

{{selection}}
```

## Notes

- Files here are part of `raw/` — immutable once captured. The ingestion flow only mutates frontmatter (`ingested`, `ingested_at`)
- If a clipping isn't relevant to Andres's core domains (Moil, AIbyAndres, Brain/PKM, community, family, personal growth), `/brain-ingest` logs it as skipped rather than forcing a wiki page
- Filenames should follow `YYYY-MM-DD-slug.md`

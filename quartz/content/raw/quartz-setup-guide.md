---
type: reference
---

# Quartz v4 — Brain Website Setup Guide
> Publishes your Brain as a searchable, wikilink-connected website at https://jarvisurregoTX.github.io/my-brain

---

## How it works

Quartz reads your markdown files, resolves all `[[wikilinks]]`, and builds a static site with full-text search and an interactive graph. GitHub Actions automatically rebuilds and redeploys every time you `git push`.

**Architecture:**
- Your Brain repo (`my-brain`) stays the source of truth
- Quartz lives inside it as a subfolder (`quartz/`)
- Your markdown files go inside `quartz/content/`
- GitHub Pages serves the built site from the `gh-pages` branch

---

## Prerequisites

Open Terminal and verify:

```bash
node --version   # Need v18 or higher — if missing: brew install node
npm --version    # Should come with Node
git --version    # Already installed
```

---

## Step 1 — Add Quartz to your Brain repo

```bash
cd ~/My\ Brain/knowledge-base

# Clone Quartz into a temp folder
git clone https://github.com/jackyzha0/quartz.git _quartz_temp

# Copy the Quartz template files into your Brain repo
cp -r _quartz_temp/quartz ./quartz
cp _quartz_temp/quartz.config.ts ./quartz.config.ts
cp _quartz_temp/quartz.layout.ts ./quartz.layout.ts
cp _quartz_temp/package.json ./package.json
cp _quartz_temp/package-lock.json ./package-lock.json
cp _quartz_temp/tsconfig.json ./tsconfig.json

# Copy the GitHub Actions workflow
mkdir -p .github/workflows
cp _quartz_temp/.github/workflows/deploy.yml .github/workflows/deploy.yml

# Create the content folder and move your Brain files into it
mkdir -p quartz/content
cp -r raw quartz/content/raw
cp -r wiki quartz/content/wiki
cp index.md quartz/content/index.md
cp Memory.md quartz/content/Memory.md
cp Action-Tracker.md quartz/content/Action-Tracker.md
cp Decision-Log.md quartz/content/Decision-Log.md
cp COMMANDS.md quartz/content/COMMANDS.md
cp brain-guide.md quartz/content/brain-guide.md

# Clean up temp folder
rm -rf _quartz_temp

# Install Quartz dependencies
npm install
```

**Expected output:** lots of npm install logs, no errors.

---

## Step 2 — Configure Quartz

Open `quartz.config.ts` in any text editor and update these two lines near the top:

```typescript
const config: QuartzConfig = {
  configuration: {
    pageTitle: "🧠 Andres' Brain",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "JarvisUrregoTX.github.io/my-brain",  // ← UPDATE THIS
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    // ...rest stays the same
  }
}
```

Just change `baseUrl` to `JarvisUrregoTX.github.io/my-brain`.

---

## Step 3 — Test locally (optional but recommended)

```bash
cd ~/My\ Brain/knowledge-base
npx quartz build --serve
```

Open http://localhost:8080 — you should see your Brain as a website with search, graph, and all wikilinks working. Press Ctrl+C when done.

---

## Step 4 — Update .gitignore

Add these lines to your `.gitignore` (in the Brain root):

```
node_modules/
.quartz-cache/
public/
```

---

## Step 5 — Commit and push

```bash
cd ~/My\ Brain/knowledge-base
git add .
git commit -m "Add Quartz v4 — Brain website"
git push
```

GitHub Actions will start building automatically. You can watch it at:
https://github.com/JarvisUrregoTX/my-brain/actions

---

## Step 6 — Enable GitHub Pages (one-time)

1. Go to https://github.com/JarvisUrregoTX/my-brain/settings/pages
2. Under **Source**, select **GitHub Actions**
3. Click Save

That's it. The next push will deploy to:
**https://JarvisUrregoTX.github.io/my-brain**

First build takes ~2 minutes. After that, each push redeploys in ~60 seconds.

---

## Keeping content in sync

Going forward, your markdown files live in `quartz/content/` — **that's where you edit them**, not the root anymore.

When you pull new X bookmarks or Teams messages, save them to `quartz/content/raw/` instead of `raw/`.

Or, add a sync script:

```bash
# Add to teams_ingest.sh — syncs raw/ to quartz/content/raw/ before committing
rsync -av raw/ quartz/content/raw/
```

---

## Quick reference

| Action | Command |
|--------|---------|
| Preview locally | `cd ~/My\ Brain/knowledge-base && npx quartz build --serve` |
| Publish changes | `git add . && git commit -m "update" && git push` |
| View live site | https://JarvisUrregoTX.github.io/my-brain |
| View build logs | https://github.com/JarvisUrregoTX/my-brain/actions |

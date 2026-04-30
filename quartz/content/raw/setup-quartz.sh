#!/bin/bash
# Brain → Quartz v4 → GitHub Pages
# Run: bash ~/My\ Brain/knowledge-base/raw/setup-quartz.sh

BRAIN="$HOME/My Brain/knowledge-base"
cd "$BRAIN"

echo ""
echo "🧠 Setting up Quartz v4 for your Brain..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# ── 1. Check Node ──────────────────────────────────────────────────────────
echo "📋 Checking Node.js..."
if ! command -v node &>/dev/null; then
  echo "❌ Node not found. Install it: brew install node"; exit 1
fi
echo "✅ Node $(node --version) found"

# ── 2. Clone Quartz (clean) ────────────────────────────────────────────────
echo ""
echo "📦 Downloading Quartz v4..."
rm -rf .quartz_setup
git clone --depth=1 https://github.com/jackyzha0/quartz.git .quartz_setup 2>&1 | grep -v "^$"

# ── 3. Copy Quartz infrastructure ─────────────────────────────────────────
echo ""
echo "📁 Installing Quartz files..."
[ -d .quartz_setup/quartz ]           && cp -r .quartz_setup/quartz ./
[ -f .quartz_setup/quartz.config.ts ] && cp .quartz_setup/quartz.config.ts ./
[ -f .quartz_setup/quartz.layout.ts ] && cp .quartz_setup/quartz.layout.ts ./
[ -f .quartz_setup/package.json ]     && cp .quartz_setup/package.json ./
[ -f .quartz_setup/package-lock.json ] && cp .quartz_setup/package-lock.json ./
[ -f .quartz_setup/tsconfig.json ]    && cp .quartz_setup/tsconfig.json ./
echo "✅ Quartz files copied"

# ── 4. Create GitHub Actions workflow (write directly — don't rely on clone) ──
echo "⚙️  Creating GitHub Actions deploy workflow..."
mkdir -p .github/workflows
cat > .github/workflows/deploy.yml << 'WORKFLOW'
name: Deploy Quartz site to GitHub Pages

on:
  push:
    branches:
      - main

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - name: Install Dependencies
        run: npm ci
      - name: Build Quartz
        run: npx quartz build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: public

  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
WORKFLOW
echo "✅ deploy.yml created"

# ── 5. Move Brain content into quartz/content/ ────────────────────────────
echo "📝 Moving Brain markdown into quartz/content/..."
mkdir -p quartz/content/raw
mkdir -p quartz/content/wiki

# Copy all markdown from raw/ (skip the script itself)
[ -d raw ] && find raw -name "*.md" -exec cp {} quartz/content/raw/ \; 2>/dev/null || true
[ -d wiki ] && cp -r wiki/. quartz/content/wiki/ 2>/dev/null || true

# Copy root markdown files
for f in index.md Memory.md Action-Tracker.md Decision-Log.md COMMANDS.md brain-guide.md MOIL.md; do
  [ -f "$f" ] && cp "$f" quartz/content/
done
echo "✅ Brain content moved"

# ── 6. Configure quartz.config.ts ─────────────────────────────────────────
echo "⚙️  Configuring site..."
python3 - << 'EOF'
import re
with open("quartz.config.ts", "r") as f:
    content = f.read()
content = re.sub(r'baseUrl:\s*"[^"]*"', 'baseUrl: "JarvisUrregoTX.github.io/my-brain"', content)
content = re.sub(r'pageTitle:\s*"[^"]*"', 'pageTitle: "Andres Brain"', content)
with open("quartz.config.ts", "w") as f:
    f.write(content)
print("   baseUrl → JarvisUrregoTX.github.io/my-brain ✓")
print("   pageTitle → Andres Brain ✓")
EOF

# ── 7. Update .gitignore ──────────────────────────────────────────────────
grep -q "node_modules" .gitignore 2>/dev/null || cat >> .gitignore << 'IGNORE'

# Quartz build output
node_modules/
.quartz-cache/
public/
.quartz_setup/
IGNORE
echo "✅ .gitignore updated"

# ── 8. Cleanup temp clone ─────────────────────────────────────────────────
rm -rf .quartz_setup

# ── 9. Install npm packages ────────────────────────────────────────────────
echo ""
echo "📦 Installing npm packages (~60 seconds)..."
npm install --silent
echo "✅ npm install complete"

# ── 10. Commit and push ────────────────────────────────────────────────────
echo ""
echo "🚀 Committing and pushing to GitHub..."
git add .
git commit -m "Add Quartz v4 — Brain website auto-deploy"
git push
echo "✅ Pushed!"

# ── Done ───────────────────────────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Quartz setup complete!"
echo ""
echo "ONE LAST STEP — enable GitHub Pages:"
echo "  1. Open: https://github.com/JarvisUrregoTX/my-brain/settings/pages"
echo "  2. Under Source → select GitHub Actions"
echo "  3. Save"
echo ""
echo "Your Brain goes live at:"
echo "  🌐 https://JarvisUrregoTX.github.io/my-brain"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

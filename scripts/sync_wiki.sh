#!/usr/bin/env bash
# sync_wiki.sh — Sync wiki/ + root markdown files into quartz/content/
#
# Run this before every git commit to ensure the Quartz site reflects
# the latest wiki state. GitHub Actions builds from quartz/content/.
#
# Usage: bash scripts/sync_wiki.sh

set -e

KB_DIR="$(cd "$(dirname "$0")/.." && pwd)"
CONTENT_DIR="$KB_DIR/quartz/content"

echo "[sync] Syncing wiki/ → quartz/content/wiki/"
rsync -a --delete "$KB_DIR/wiki/" "$CONTENT_DIR/wiki/"

echo "[sync] Syncing root markdown files"
cp "$KB_DIR/MEMORY.md"   "$CONTENT_DIR/MEMORY.md"
cp "$KB_DIR/index.md"    "$CONTENT_DIR/index.md"
cp "$KB_DIR/log.md"      "$CONTENT_DIR/log.md"

echo "[sync] Done — quartz/content is up to date"

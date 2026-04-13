---
title: "Bilingual AI Systems"
date: 2026-04-12
tags:
  - graph/spoke
  - status/stub
---

# Bilingual AI Systems

**Type:** Radar log — AI / product
**Last updated:** 2026-04-12
**Related:** [[wiki/concepts/voice-first-hiring]], [[wiki/radar/voice-ux-patterns]], [[wiki/radar/latam-job-market]]

---

## What This Tracks

Spanish-English NLP quality, bilingual voice AI systems, code-switching models, and the gap between English-optimized AI and real-world Hispanic worker needs.

## Why It Matters for Moil

Moil's voice application is bilingual. The quality of Spanish NLP — especially for Mexican, Central American, and Caribbean dialects spoken by Moil's worker base — is a product quality and trust issue.

## Current State of Spanish NLP (2025–2026)

### Strengths
- OpenAI Whisper is excellent at Spanish transcription; handles accents well
- GPT-4o and Claude Sonnet handle Spanish conversations at near-native quality
- Google Cloud Speech-to-Text now supports 20+ Spanish regional variants
- Meta's Llama 3 models have strong Spanish capabilities (trained on Spanish Common Crawl)

### Gaps
- **Code-switching**: Spanglish mid-sentence ("I have experience en construcción pero también I can do landscaping") is poorly handled by most ASR systems
- **Dialectal variation**: Cuban, Dominican, Mexican Spanish differ significantly. Most models are biased toward Castilian Spanish (training data artifact)
- **Informal register**: Workers don't speak formal Spanish. Colloquialisms, regional slang, and informal contractions break systems trained on formal text
- **Low-bandwidth audio**: WhatsApp voice notes have compression artifacts that degrade ASR quality

### What Moil Needs

- Whisper or equivalent for transcription (handles Spanish well)
- A post-processing layer for code-switching normalization
- Dialect detection to route to appropriate model variant
- Fallback to text input when audio quality is too low

## Competitive Landscape

Few hiring platforms have invested in Spanish-first voice AI. This is Moil's technical moat — but only if the quality is measurably better than competitors.

## Sources to Watch
- OpenAI Whisper model updates
- Hugging Face Spanish NLP leaderboards
- AI2 — Spanish language model benchmarks
- @karpathy on multilingual model progress

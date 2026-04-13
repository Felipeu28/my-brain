---
title: "Voice-First UX Patterns"
date: 2026-04-12
tags:
  - graph/spoke
  - status/stub
---

# Voice-First UX Patterns

**Type:** Radar log — product design
**Last updated:** 2026-04-12
**Related:** [[wiki/concepts/voice-first-hiring]], [[wiki/radar/bilingual-ai]], [[wiki/concepts/blue-collar-tech-gap]]

---

## What This Tracks

Design patterns, adoption data, and UX research specific to voice-first interfaces — with a focus on what works for non-tech-native users.

## Why It Matters for Moil

Moil's core thesis is that voice > forms for blue-collar job applications. Understanding what makes voice interfaces succeed (and fail) in practice is critical for product quality.

## Key Patterns (as of 2026)

### What Works
- **Progressive disclosure**: Don't dump all questions at once. Ask one question, wait, confirm, move on. Mirrors a human conversation.
- **Error recovery**: "I didn't catch that" must not feel like a failure. Offer rephrasing, not just retry.
- **Language switching**: Bilingual users switch mid-sentence. The system must tolerate code-switching gracefully.
- **WhatsApp as the UI**: Workers trust WhatsApp. Moil's WhatsApp-native flow reduces friction vs. asking users to download an app.
- **Confirmation loops**: Repeat back what was captured before saving. Reduces errors and builds trust.

### What Fails
- Requiring an app download before first value
- Cold-starting with complex multi-part questions
- Formal register that doesn't match colloquial Spanish
- Long silence timeouts that feel like the call dropped

## Accessibility Dimension

Voice-first is inherently more accessible for:
- Limited-literacy workers
- Workers with motor limitations
- Workers who are driving or on-site (hands-free)

This is underemphasized in Moil's current positioning — potential marketing angle.

## Sources to Watch
- Google PAIR (People + AI Research) voice UX guidelines
- Voiceflow blog (conversational design patterns)
- Nielsen Norman Group — voice interface usability reports
- @cassiewerber on labor + tech accessibility

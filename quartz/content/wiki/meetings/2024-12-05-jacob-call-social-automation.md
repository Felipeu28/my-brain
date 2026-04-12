---
tags:
  - graph/leaf
---
# Jacob Call — Social Media Automation & Job Post Images

**Type:** meeting
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/transcript-2024-12-05-jacob-call-december-5.md]]
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/abiodun-solomon]], [[wiki/moil/product-roadmap]]

---

## Summary

Andres and Jacob (with Abiodun/Ablad joining briefly) focused on automating the job posting image creation pipeline. Andres shared a Claude/ChatGPT-generated plan for dynamic image generation: 20 Canva templates → AI-generated captions → webhook-triggered auto-posting. Zachary Corporation has 40-80+ jobs, making manual design unsustainable. Also discussed: social media content creation cadence.

## Key Topics

### Automated Job Post Image Pipeline

Andres walked through an AI-generated spec (from Claude/ChatGPT) for automating job image creation:
1. **20 Canva/Figma templates** — by industry/job type (plumber, construction, hospitality, etc.)
2. **Dynamic text overlay** — API extracts job title, company, location from database → AI summarizes description → fills template placeholders
3. **Auto-post trigger** — Webhook fires when new job is posted → creates image → saves to Google Drive → auto-posts to 20+ social media groups
4. **Tools discussed:** Canva API, Figma API, Pillow (Python), Buffer/Hootsuite/Zapier for social distribution

**Context:** Zachary Corporation has 40-80 jobs to post; team was doing this entirely manually (design → Drive → manual group posting)

### Social Media Discussion

- Jacob to compile list of old videos from last year to re-post
- Andres wants job posting images ready for Zachary; prioritize English first, Spanish next week
- "Post that we have x jobs over 80 jobs with 700 subscribers" — celebrate the Zachary milestone on social

### Technology: Claude Integration

Andres was live-demoing Claude (referenced as "Cloud" in transcript) for team use — using it to generate the automation README document, generate job descriptions, and plan the workflow. Note: This is significant — Andres was using Claude as a technical planning tool in Dec 2024.

## Action Items

- [ ] Build 20 Canva job image templates (by industry)
- [ ] Implement automated image generation pipeline (Canva API + OpenAI caption generation)
- [ ] Set up webhook: new job posted → image created → saved to Drive → posted to groups
- [ ] Create social post: "Zachary is posting 80+ jobs through Moil" milestone announcement
- [ ] Post 1-2 Zachary jobs daily to new platform

## Moil Relevance

The social automation pipeline directly addresses Moil's marketing bottleneck: the team was spending disproportionate time creating individual job post images. Automating this → scale to hundreds of job posts without adding headcount. This also creates a repeatable system for new enterprise clients like Zachary.

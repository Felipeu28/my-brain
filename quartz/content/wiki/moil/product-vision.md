---
title: "Product Vision"
tags: [moil, evergreen]
date: 2026-04-11
---

# Moil — Product Vision

**Type:** moil-topic
**Last updated:** 2026-04-11
**Source:** [[raw/moil-documents-2026-04-09]], [[raw/moilapp-website-2026-04-09]]
**Related:** [[moil/index]], [[moil/go-to-market]], [[moil/competitive-landscape]], [[moil/tech-stack]]

---

## The Vision in One Sentence

Moil is the AI co-founder every small business deserves — a single intelligent platform that learns your business in 21 questions and then runs your market research, business planning, content marketing, hiring, and strategy coaching on autopilot.

---

## The Problem — Two Sides of the Same Marketplace

### For SMB Owners
Small business owners are the CEO, CMO, recruiter, and strategist simultaneously. They can't afford a $5,000 consultant engagement. They don't have time to juggle ChatGPT for writing, Canva for images, Indeed for hiring, and spreadsheets for planning. Most do nothing — they wing it, burn out, and stall.

The status quo:
- Generic tools that don't know their business
- Consultants that charge more for one meeting than Moil costs for a year
- Fragmented toolchains with no shared context
- Marketing that falls through the cracks every time a customer calls

### For Workers (Candidate Side)
Blue-collar and service workers — HVAC techs, cleaners, landscapers, restaurant staff — are poorly served by the existing hiring infrastructure. Resumes are barriers rather than tools. Many are bilingual but only see English-language job postings. Traditional job boards reach them poorly. The hiring process is slow ($2,400 cost per hire, 32-day avg time) for employers and opaque for workers.

---

## The Solution — AI Co-Founder Architecture

Moil's architectural bet is that **business context, once captured, should power everything**. The 21-question onboarding isn't just intake — it creates a Business DNA that flows into every downstream output:

```
21 Questions (voice or text, EN/ES)
         ↓
   Business DNA Profile
  /    |    |    |    \
Market  Biz  Content  Hiring  24/7
Rsrch  Plan   360    Smart   Coach
```

Each module feeds the next. A market research report informs the business plan. The business plan shapes the content calendar topics. The content calendar positions the job postings. The hiring outcomes feed back into the coaching.

This is **not** six separate features — it's one operating layer that happens to have six outputs.

---

## Voice-First Rationale

The 21-question intake can be answered **by voice in English or Spanish**. This is a deliberate product choice, not a feature checkbox:

1. **SMB owners don't sit at keyboards** — they're on a job site, in a truck, behind a counter. Voice removes the primary friction barrier.
2. **Language parity** — typing in Spanish on a US-configured keyboard is annoying. Speaking is natural. Bilingual voice support is a meaningful differentiator.
3. **Onboarding as first value delivery** — the act of answering 21 questions should itself feel valuable (forces clarity). Voice makes it conversational, not form-filling.

---

## Key Differentiators vs. Incumbents

| Dimension | Moil | Indeed | ChatGPT | Traditional Consultant |
|-----------|------|--------|---------|----------------------|
| Business context | Full DNA (21Q) | None | None | Partial |
| Scope | Research + Plan + Marketing + Hiring + Coaching | Hiring only | Writing only | Project-specific |
| Bilingual EN/ES | Native, every feature | Limited | Partial | Rare |
| Price | $15–$75/mo | Pay-per-click | $20/mo | $5,000+/project |
| Always-on | Yes (24/7 coach) | No | No | No |
| Distribution | 10+ platforms auto | 1 platform | None | None |

Moil's moat is not any individual feature — it is the **integration**. The business that answered 21 questions has context that flows across hiring, content, and planning in one session. No competitor offers this.

---

## North Star Metric

**Active businesses with at least one completed workflow per month** (not just registered users).

Rationale: a business that has run market research OR posted a job OR generated a content calendar has experienced real value and is likely to pay. Activation depth predicts retention better than sign-ups.

Secondary metrics: time-to-hire (target: 11 days, industry avg 32), content calendar completion rate (Content360 plans fully generated and downloaded), and 90-day employee retention (target: 91%).

---

## Product Roadmap (from Business Plan, March 2026)

| Quarter | Priority |
|---------|----------|
| Q2 2026 | Critical product fixes — stabilize core experience before expanding |
| Q3 2026 | AI Co-Pilot model — deeper business context persistence across sessions |
| Q4 2026 | Direct integrations for multi-channel publishing (Content360 → social platforms) |
| 2027 | Performance analytics expansion, industry-specific templates, scale to 2,500–3,000 active subscriptions |

---

## What Moil is NOT Trying to Be

- **Not an enterprise HRIS** — Moil is built for 1–50 employee businesses with low-tech stacks
- **Not a staffing agency** — Moil is a platform, not a service. It automates the posting and matching; the hiring decision stays with the owner
- **Not another ChatGPT wrapper** — Moil learns your specific business through structured onboarding and maintains that context across sessions
- **Not a replacement for the owner** — Moil augments the owner, it doesn't replace them. The positioning is "co-founder" not "autopilot"

---

## Connections

- [[moil/go-to-market]] — How Moil goes to market with this vision
- [[moil/competitive-landscape]] — Full competitive analysis
- [[moil/tech-stack]] — The technical implementation of this vision
- [[moil/metrics]] — The KPIs that measure progress toward this vision
- [[concepts/content360]] — The Content360 module in depth
- [[concepts/smart-hiring]] — The Smart Hiring module in depth

---
tags:
  - graph/spoke
---
# Moilapp.com — SEO Implementation Plan (April 2026)

**Type:** concept
**Last updated:** 2026-04-15
**Source:** [[raw/odtr-moilapp_SEO_Implementation_Plan_April2026]]
**Related:** [[wiki/moil/product-roadmap]], [[wiki/moil/gtm]], [[wiki/concepts/moil360]]

---

## Summary

Comprehensive 4-phase SEO technical roadmap for moilapp.com, dated April 8, 2026. Addresses critical indexing issues: only 13/68 pages indexed, 1% avg CTR, 15.4K impressions for "moil" but only 180 clicks in 3 months.

## Current State (Pre-Fix)

| Metric | Value |
|---|---|
| Pages indexed | 13 of 68 |
| Avg CTR | 1% |
| "moil" impressions (3 mo) | 15,400 |
| Clicks (3 mo) | 180 |
| Fixes identified | 10 |

## Critical Issues Found

1. **Homepage URL pollution** — `www.moilapp.com` redirects to `/business?lg=en` via browser language detection, creating hundreds of duplicate "homepages"
2. **Sitemap mismatch** — uses non-www URLs; homepage `/` missing entirely
3. **Duplicate brand in title tag** — "Moil | Moil" bug
4. **No schema markup anywhere** — zero structured data (no Organization, SoftwareApplication, or JobPosting schema)
5. **No robots.txt coverage** — allows crawl of login pages, staging domains, font files, parameter variants
6. **No favicon** — 404 on every page visit

## 4-Phase Roadmap

| Phase | Focus | Timeline | Key Actions |
|---|---|---|---|
| 1 — Emergency | Stop URL pollution | Week 1 | Cookie-based language (kill `?lg=`), favicon, robots.txt rewrite, title bug fix |
| 2 — Technical | Lock foundation | Week 2 | Canonical tags, noindex on auth/staging, sitemap rebuild, HTTP→HTTPS audit, 301 redirects |
| 3 — Schema | Make Google understand | Week 3 | Organization + SoftwareApplication JSON-LD, **JobPosting schema** (highest-ROI fix — Google Jobs carousel), hreflang for EN/ES, meta title/description rewrites |
| 4 — Growth | Scale what works | Week 4+ | GSC re-indexing, blog SEO targeting business-owner keywords, subdomain consolidation (blog.moilapp.com → www.moilapp.com/blog/) |

## Highest-ROI Fix: JobPosting Schema

Google has a dedicated Jobs carousel (position 0, above all organic results). Moil's `candidate.moilapp.com/jobs/*` pages are already found by Google but lack the schema to enter this channel. Adding JobPosting JSON-LD would put every Moil job listing in front of job seekers before any other result.

## Blog Keyword Targets

| Keyword | Monthly Searches | Difficulty |
|---|---|---|
| ai business plan generator free | 8,100 | Medium |
| how to hire employees small business | 5,400 | Low |
| ai tools for small business owners | 4,400 | Low |
| business plan template contractor | 2,900 | Low |
| content marketing for local business | 2,400 | Low |

## Subdomain Consolidation

2026 data shows 15–45% organic traffic increase when content moves from subdomains to subdirectories. Recommendation: migrate `blog.moilapp.com` → `www.moilapp.com/blog/` to consolidate link equity.

## AEO (AI Engine Optimization)

Referenced in [[wiki/meetings/2026-04-14-roxana-alloy-atx-onboarding]] — Andres pitching Q&A on every client page so AI assistants (ChatGPT, Perplexity) can cite the business. This extends SEO into AI answer engines and is a new positioning angle for Moil services.

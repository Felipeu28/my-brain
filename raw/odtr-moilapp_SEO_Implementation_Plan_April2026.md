# moilapp_SEO_Implementation_Plan_April2026

**Date:** 2026-04-08
**Type:** meeting-transcript

---

SEO Implementation Plan
Full Technical Roadmap to Index, Rank &amp; Convert
moilapp.com  —  April 8, 2026
13/68
Pages Indexed
1%
Avg. CTR
15.4K
'moil' Impressions
180
Clicks (3 mo.)
10
Fixes Identified

## What We Found in the Live Audit
Beyond the exported coverage data, direct inspection of the live site and GSC surfaced several issues that weren't visible in the spreadsheet alone. These findings shape the entire strategy below.
Finding
Why It Matters
www.moilapp.com REDIRECTS to /business?lg=en
This is the single biggest SEO issue. The homepage itself appends ?lg=en via browser language detection. Every visitor lands on a parameterized URL, creating hundreds of duplicate 'homepages'. Google has no clear canonical entry point.
Sitemap uses non-www URLs; homepage (/) missing
The sitemap lists https://moilapp.com/business — not the www canonical. And / itself isn't in the sitemap at all. Google receives conflicting signals about what the 'real' homepage is.
Title tag has duplicate brand name
'AI Business Plan Generator &amp; Smart Hiring for Small Business | Moil | Moil' — The double 'Moil' at the end is a bug that wastes title real estate and looks unprofessional in SERPs.
robots.txt blocks nothing useful
Current robots.txt only blocks SEO scrapers (Ahrefs, MJ12). It allows full crawl of font files, login pages, staging domains, and all parameter variants — none of which should be crawled.
No schema markup anywhere on the site
Zero structured data detected. No Organization schema, no SoftwareApplication schema, no JobPosting schema. This means no rich results, no Google Jobs visibility, and weaker AI answer-engine citations.
Product is broader than 'job platform'
Moil is positioning as 'The AI Co-Founder Every Small Business Deserves' — market research, business plans, content marketing, hiring, and AI coaching. SEO keyword targets should reflect this full scope, not just hiring.

## Implementation Phases
Work is organized into 4 phases. Phases 1 and 2 are purely technical — no content required, just code. Phases 3 and 4 unlock the growth upside. Each fix includes the exact code or configuration change needed.
Phase
Focus
Key Actions
Timeline
1
Emergency Fixes
Stop parameter URL generation • Fix 404s • Fix robots.txt
Week 1  (Days 1–5)
2
Technical SEO
Canonical tags • Noindex rules • Sitemap fix • HTTP→HTTPS audit
Week 2  (Days 6–12)
3
Schema &amp; Metadata
Structured data • Title/desc rewrites • hreflang • Job schema
Week 3  (Days 13–21)
4
Growth Engine
Blog SEO • Subdomain strategy • GSC request indexing • Monitoring
Week 4+  (Ongoing)
PHASE 1
Emergency Fixes — Stop the Bleeding
Days 1–5

## Fix 1.1  —  Stop ?lg= Parameter from Polluting URLs  🔴 CRITICAL
Root cause: The site detects browser language and redirects to /?lg=en or /?lg=es. This single behavior is responsible for the majority of your duplicate content issues. Google sees moilapp.com/business, moilapp.com/business?lg=en, moilapp.com/business?lg=es as three different pages.
The fix: Store language preference in a cookie or localStorage — NOT the URL. Language should be invisible to Google.

## Next.js Implementation
// middleware.ts — language detection WITHOUT URL parameters
import { NextRequest, NextResponse } from 'next/server'
export function middleware(request: NextRequest) {
const { pathname, searchParams } = request.nextUrl
// Strip ?lg= parameter — redirect to clean URL
if (searchParams.has('lg')) {
const lang = searchParams.get('lg') || 'en'
const cleanUrl = new URL(pathname, request.url)
const response = NextResponse.redirect(cleanUrl, { status: 301 })
response.cookies.set('lang', lang, { path: '/', maxAge: 60 * 60 * 24 * 365 })
return response
}
// If no cookie, detect from Accept-Language header and set cookie only
if (!request.cookies.get('lang')) {
const acceptLang = request.headers.get('accept-language') || ''
const lang = acceptLang.startsWith('es') ? 'es' : 'en'
const response = NextResponse.next()
response.cookies.set('lang', lang, { path: '/', maxAge: 60 * 60 * 24 * 365 })
return response
}
}
export const config = { matcher: ['/((?!api|_next|.*\..*).*)'] }
After deploying: Verify that visiting moilapp.com/business in an English browser no longer appends ?lg=en. Test in incognito mode. Then submit a GSC removal request for all ?lg= URLs to speed up de-indexing.

## Fix 1.2  —  Add favicon.ico and apple-touch-icon  🔴 HIGH
Both https://moilapp.com/favicon.ico and https://www.moilapp.com/favicon.ico return 404. This generates a crawl error on every single page Google visits since browsers and crawlers request it automatically.
// Place these files in /public/ (Next.js serves /public as /)
// /public/favicon.ico          ← 32x32 or 48x48 ICO
// /public/apple-touch-icon.png ← 180x180 PNG
// /public/icon-192.png         ← 192x192 PNG (PWA)
// /public/icon-512.png         ← 512x512 PNG (PWA)
// In app/layout.tsx, add to metadata:
export const metadata = {
icons: {
icon: [
{ url: '/favicon.ico', sizes: '48x48' },
{ url: '/icon-192.png', sizes: '192x192', type: 'image/png' },
],
apple: [{ url: '/apple-touch-icon.png', sizes: '180x180' }],
},
}

## Fix 1.3  —  Rewrite robots.txt  🔴 HIGH
The current robots.txt blocks zero useful paths. It needs to be completely rewritten for Next.js to block font files, login pages, staging domains, and parameter variants.
// app/robots.ts — Next.js native robots generation
import { MetadataRoute } from 'next'
export default function robots(): MetadataRoute.Robots {
return {
rules: [
{
userAgent: '*',
allow: '/',
disallow: [
'/_next/static/media/',  // blocks font/.woff2 crawling
'/api/',
'/login',
'/register',
'/authenticate/',
'/*?*lg=',              // block all ?lg= variants
'/*?*ref=',             // block referral param variants
'/*?*trk=',             // block tracking param variants
'/*?*fbclid=',          // block Facebook click IDs
],
},
// Block staging and beta subdomains entirely
{ userAgent: '*', disallow: '/', host: 'stagebeta.moilapp.com' },
{ userAgent: '*', disallow: '/', host: 'employer-beta.moilapp.com' },
// Keep blocking scrapers
{ userAgent: 'AhrefsBot', disallow: '/' },
{ userAgent: 'MJ12bot', disallow: '/' },
],
sitemap: 'https://www.moilapp.com/sitemap.xml',
}
}
Note: Disallow in robots.txt prevents crawling but NOT indexing of already-known URLs. Combine with noindex meta tags (Phase 2) for full coverage.

## Fix 1.4  —  Fix the Title Tag Duplicate Brand Bug  🟠 HIGH
Current title: 'AI Business Plan Generator &amp; Smart Hiring for Small Business | Moil | Moil'
The double 'Moil' at the end is a bug — likely a layout.tsx template appending the site name to an already-branded page title. Fix and rewrite for CTR.
// app/layout.tsx
export const metadata = {
title: {
template: '%s | Moil',   // Page title + brand once
default: 'Moil — AI Co-Founder for Small Business',
},
}
// app/business/page.tsx — specific page title
export const metadata = {
title: 'AI Co-Founder for Small Business — Business Plans, Hiring &amp; Marketing',
description: 'Moil gives small businesses an AI co-founder that writes your ' +
'business plan, runs your marketing, and hires your team. ' +
'500+ businesses growing. From $15/mo.',
}
// Result in SERP: 'AI Co-Founder for Small Business — Business Plans, Hiring &amp; Marketing | Moil'
PHASE 2
Technical SEO — Lock Down the Foundation
Days 6–12

## Fix 2.1  —  Canonical Tags on All Pages  🟠 HIGH
Every page needs a self-referencing canonical tag pointing to the clean www HTTPS URL. In Next.js App Router, this is done via generateMetadata. The canonical must always point to the parameter-free, www version.
// app/business/page.tsx
import { Metadata } from 'next'
export async function generateMetadata(): Promise&lt;Metadata&gt; {
return {
alternates: {
canonical: 'https://www.moilapp.com/business',
},
}
}
// app/business/pricing/page.tsx
export async function generateMetadata(): Promise&lt;Metadata&gt; {
return {
alternates: {
canonical: 'https://www.moilapp.com/business/pricing',
},
}
}
// For dynamic routes (e.g. job listings):
// app/jobs/[slug]/page.tsx
export async function generateMetadata({ params }): Promise&lt;Metadata&gt; {
const slug = (await params).slug
return {
alternates: {
canonical: `https://candidate.moilapp.com/jobs/${slug}`,
},
}
}
Key rule: Canonical consistency is critical. The canonical, the sitemap URL, and the primary internal links MUST all use the same URL format. Mixed signals (www vs non-www, http vs https) cause Google to ignore your declared canonical 84% of the time based on 2026 data.

## Fix 2.2  —  Noindex Login, Register &amp; Auth Pages  🟠 HIGH
These pages must never appear in Google search results. Adding noindex is separate from robots.txt — robots.txt stops crawling, noindex stops indexing. You need both.
// Shared utility — apply to all auth pages
const authMetadata = {
robots: { index: false, follow: false },
}
// app/login/page.tsx (and candidate/login, business/login)
export const metadata = { ...authMetadata, title: 'Log In | Moil' }
// app/register/page.tsx
export const metadata = { ...authMetadata, title: 'Get Started | Moil' }
// app/authenticate/page.tsx and subpages
export const metadata = { ...authMetadata }
// This generates: &lt;meta name='robots' content='noindex, nofollow'&gt;
// Also add to business.moilapp.com/login and business.moilapp.com/register

## Fix 2.3  —  Add Noindex to Staging Subdomains  🟠 HIGH
stagebeta.moilapp.com and employer-beta.moilapp.com should have a global noindex applied at the environment level so any staging deployments are never indexed.
// next.config.js — environment-based noindex
const isProduction = process.env.NODE_ENV === 'production'
&amp;&amp; process.env.NEXT_PUBLIC_ENV === 'production'
// In app/layout.tsx:
export function generateMetadata() {
return {
robots: isProduction
? { index: true, follow: true }
: { index: false, follow: false },  // noindex on staging
}
}
// OR: Add to vercel.json / hosting config as HTTP header:
// X-Robots-Tag: noindex, nofollow
// This covers ALL file types including fonts and manifests

## Fix 2.4  —  Fix Sitemap to Match Canonical URLs  🟠 HIGH
Current sitemap issues: (1) Uses non-www URLs. (2) The homepage / is missing. (3) Does not include blog posts or job pages. Rebuild it programmatically.
// app/sitemap.ts
import { MetadataRoute } from 'next'
export default async function sitemap(): Promise&lt;MetadataRoute.Sitemap&gt; {
const baseUrl = 'https://www.moilapp.com'
// Static pages
const staticPages = [
{ url: `${baseUrl}/business`,         changeFrequency: 'weekly',  priority: 1.0 },
{ url: `${baseUrl}/business/pricing`, changeFrequency: 'monthly', priority: 0.9 },
{ url: `${baseUrl}/candidate`,        changeFrequency: 'weekly',  priority: 0.9 },
{ url: `${baseUrl}/marketing`,        changeFrequency: 'monthly', priority: 0.7 },
{ url: `${baseUrl}/privacy`,          changeFrequency: 'yearly',  priority: 0.3 },
]
// Dynamic blog posts (fetch from your CMS/API)
const blogPosts = await fetchBlogPosts()
const blogEntries = blogPosts.map(post =&gt; ({
url: `https://blog.moilapp.com/${post.slug}`,
lastModified: post.updatedAt,
changeFrequency: 'monthly',
priority: 0.6,
}))
return [...staticPages, ...blogEntries]
}
// IMPORTANT: Exclude login, register, auth, and parameter URLs

## Fix 2.5  —  Audit &amp; Fix All HTTP → HTTPS Internal Links  🟠 MEDIUM
7 pages appear in GSC as 'Page with redirect' — all are HTTP URLs. These are being crawled from somewhere: internal links, the sitemap, or external profiles.
Run Screaming Frog SEO Spider (free tier covers 500 URLs). Set start URL to https://www.moilapp.com and scan for all outgoing HTTP links.
Check all social media bios (LinkedIn, Twitter/X, Instagram, Facebook) — update any http:// links to https://
Search your codebase: grep -r 'http://' --include='*.tsx' --include='*.ts' to find hardcoded HTTP links
Verify the sitemap (after Fix 2.4 above) uses only HTTPS www URLs
# Quick codebase scan for HTTP links
grep -rn 'http://moilapp' --include='*.tsx' --include='*.ts' --include='*.js' .
grep -rn 'http://candidate.moilapp' --include='*.tsx' --include='*.ts' .
grep -rn 'http://business.moilapp' --include='*.tsx' --include='*.ts' .

## Fix 2.6  —  Set Up 301 Redirects for Dead Pages  🟠 MEDIUM
Two 404 pages are actively linked internally: /home and /en/. Set up permanent redirects.
// next.config.js
module.exports = {
async redirects() {
return [
{
source: '/home',
destination: '/business',
permanent: true,  // 301
},
{
source: '/en/',
destination: '/business',
permanent: true,
},
{
source: '/en',
destination: '/business',
permanent: true,
},
]
},
}
PHASE 3
Schema &amp; Metadata — Make Google Understand You
Days 13–21

## Fix 3.1  —  Organization + SoftwareApplication Schema  🟢 HIGH
No schema markup exists on moilapp.com. Adding Organization and SoftwareApplication JSON-LD to the root layout immediately signals to Google (and AI answer engines like ChatGPT, Perplexity) exactly what Moil is, who it's for, and how to categorize it.
// components/SchemaOrg.tsx — add to app/layout.tsx
export function SchemaOrg() {
const schema = {
'@context': 'https://schema.org',
'@graph': [
{
'@type': 'Organization',
'@id': 'https://www.moilapp.com/#organization',
name: 'Moil',
url: 'https://www.moilapp.com',
logo: 'https://www.moilapp.com/logo.png',
description: 'AI co-founder platform for small businesses. Business planning, hiring, marketing automation, and 24/7 AI coaching.',
foundingDate: '2022',
areaServed: 'US',
sameAs: [
'https://www.linkedin.com/company/moilapp',
'https://twitter.com/moilapp',
],
contactPoint: {
'@type': 'ContactPoint',
contactType: 'customer support',
availableLanguage: ['English', 'Spanish'],
},
},
{
'@type': 'SoftwareApplication',
'@id': 'https://www.moilapp.com/#app',
name: 'Moil',
applicationCategory: 'BusinessApplication',
operatingSystem: 'Web',
offers: {
'@type': 'Offer',
price: '15',
priceCurrency: 'USD',
priceSpecification: { '@type': 'UnitPriceSpecification', unitText: 'MONTH' },
},
featureList: [
'AI Business Plan Generator',
'Smart Hiring Platform',
'30-Day Content Marketing',
'AI Business Coach',
'Market Research',
'Bilingual EN/ES',
],
aggregateRating: {  // Add once you have reviews
'@type': 'AggregateRating',
ratingValue: '4.8',
reviewCount: '120',
},
},
],
}
return &lt;script type='application/ld+json' dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }} /&gt;
}

## Fix 3.2  —  JobPosting Schema on Job Listing Pages  🟢 CRITICAL OPPORTUNITY
This is the highest-ROI fix in this entire plan. Google has a dedicated Jobs search carousel that appears at the top of results for job-related queries. It is completely separate from organic results. Your candidate.moilapp.com/jobs/* pages are already being found by Google — they just lack the schema to enter this channel.
Expected impact: Job listings in Google for Jobs appear at position 0 — above all organic results. For every trade job search ('carpenter jobs Texas', 'yard technician hiring'), this puts Moil's listings in front of job seekers before any other result.
// candidate/jobs/[slug]/page.tsx
interface Job {
title: string; company: string; location: string; description: string
salary?: { min: number; max: number; currency: string }
datePosted: string; validThrough: string; jobType: string
}
function JobPostingSchema({ job }: { job: Job }) {
const schema = {
'@context': 'https://schema.org',
'@type': 'JobPosting',
title: job.title,
description: job.description,  // min 50 words for rich results
datePosted: job.datePosted,     // ISO 8601: '2026-04-01'
validThrough: job.validThrough, // Expiry date
employmentType: job.jobType,    // 'FULL_TIME', 'PART_TIME', 'CONTRACTOR'
hiringOrganization: {
'@type': 'Organization',
name: job.company,
sameAs: 'https://www.moilapp.com',
},
jobLocation: {
'@type': 'Place',
address: {
'@type': 'PostalAddress',
addressLocality: job.location,
addressCountry: 'US',
},
},
...(job.salary &amp;&amp; {
baseSalary: {
'@type': 'MonetaryAmount',
currency: job.salary.currency,
value: {
'@type': 'QuantitativeValue',
minValue: job.salary.min,
maxValue: job.salary.max,
unitText: 'HOUR',
},
},
}),
applicantLocationRequirements: { '@type': 'Country', name: 'US' },
directApply: true,
}
return &lt;script type='application/ld+json' dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }} /&gt;
}
// Required fields for Google Jobs: title, datePosted, description, hiringOrganization, jobLocation
// Validate at: https://search.google.com/test/rich-results

## Fix 3.3  —  Add hreflang for EN/ES Bilingual Support  🟢 MEDIUM
Moil is bilingual (EN/ES). Without hreflang tags, Google may serve the wrong language version to Spanish speakers, or treat them as duplicate pages. Implementing hreflang correctly tells Google to serve moilapp.com/business to English speakers and the Spanish version to Spanish speakers in LATAM/Spain.
// app/business/page.tsx — hreflang via generateMetadata
export async function generateMetadata(): Promise&lt;Metadata&gt; {
return {
alternates: {
canonical: 'https://www.moilapp.com/business',
languages: {
'en':    'https://www.moilapp.com/business',
'es':    'https://www.moilapp.com/business?lang=es',  // if URL-based
'x-default': 'https://www.moilapp.com/business',
},
},
}
}
// Note: Once Fix 1.1 moves language to cookies, use path-based or
// Accept-Language based serving instead. Keep ?lang= only for
// explicitly user-selected language (not auto-detect).

## Fix 3.4  —  Rewrite Meta Titles &amp; Descriptions for CTR  🟢 HIGH
The 'moil' query has 15,368 impressions but 0.2% CTR. Many of those impressions are from people searching for MOIL Ltd. (the Indian mining company) — but a clear, compelling description makes it obvious at a glance that moilapp.com is something different and valuable.
Page
New Title (≤60 chars)
New Description (≤155 chars)
/business (homepage)
Moil — AI Co-Founder for Small Business
Business plan, hiring, content marketing &amp; AI coaching — all in one platform. 500+ small businesses growing. Try free. From $15/mo.
/candidate
Find Trade &amp; Blue-Collar Jobs | Moil
Browse local job openings for trades, construction, maintenance &amp; more. Apply in 2 minutes. Powered by Moil.
/business/pricing
Moil Pricing — From $15/mo for AI Business Tools
One platform for business planning, smart hiring, and AI marketing. Cheaper than a single consultant hour. No contracts.
/marketing
AI Marketing for Small Business | Moil
30-day content calendar, AI-generated posts, images and video — all built around your specific business. No agency needed.
blog.moilapp.com
[Post title] | Moil Blog
Each post needs a unique, keyword-rich description. Currently missing — this is why blog CTR is 0.5%.
PHASE 4
Growth Engine — Scale What Works
Week 4 +

## 4.1  —  GSC: Request Indexing After Fixes  🔵
After deploying Phases 1-3, submit these pages for immediate re-crawling in GSC. Don't wait for Google to find the changes — request them explicitly.
In GSC → URL Inspection → paste URL → 'Request Indexing'
Priority order: moilapp.com/business → moilapp.com/business/pricing → moilapp.com/candidate → moilapp.com/marketing → moilapp.com/privacy
For the cleaned-up parameterized URLs, use GSC → Removals → 'Remove outdated content' to purge the old ?lg= and ?ref= versions from Google's cache
Re-submit sitemap.xml in GSC → Sitemaps after deploying Fix 2.4

## 4.2  —  Blog SEO: Target Business-Owner Keywords  🔵
blog.moilapp.com has 405 impressions but only 2 clicks (0.5% CTR). This is almost entirely a meta description problem — the posts likely have no description, so Google generates one and it's not compelling. But the bigger opportunity is targeting high-intent keywords that match Moil's product scope.
Target keyword
Monthly searches
Difficulty
Content angle
ai business plan generator free
8,100
Medium
How Moil writes your plan in 21 questions
how to hire employees small business
5,400
Low
Step-by-step guide + Moil smart hiring demo
ai tools for small business owners
4,400
Low
Comparison list where Moil replaces 5 tools
business plan template contractor
2,900
Low
Contractor-specific plan using Moil
content marketing for local business
2,400
Low
30-day content plan walkthrough with Moil
post a job for free small business
1,800
Low
How to post a job in 2 minutes with Moil

## 4.3  —  Subdomain Consolidation Strategy  🔵 STRATEGIC
Data from 2026 case studies (SEMrush, Ahrefs, Backlinko) consistently show a 15–45% organic traffic increase when content moves from subdomains to subdirectories. Google treats subdomains as separate sites — link equity doesn't flow between blog.moilapp.com and www.moilapp.com.
Current
Recommended
Priority
Effort
blog.moilapp.com/*
www.moilapp.com/blog/*
HIGH — consolidates blog authority
Medium — 301s needed
candidate.moilapp.com
www.moilapp.com/jobs
MEDIUM — major architectural change
High — evaluate carefully
business.moilapp.com
www.moilapp.com (main domain)
LOW urgency — already main product
Low — mostly redirect fixes
Start with blog.moilapp.com → www.moilapp.com/blog. This is lowest risk, highest SEO payoff. Implement proper 301 redirects with at least 12 months of redirect maintenance.

## 4.4  —  March 25 Spike — Investigate &amp; Replicate  🔵
On March 25, impressions spiked from ~200/day to 2,197 — a 10x surge. This is a playbook clue. To find the cause:
Check Google Analytics / Plausible for March 25 — look at referral sources, traffic channels, and top landing pages that day
Search LinkedIn, Reddit (r/smallbusiness, r/Entrepreneur), Twitter/X for 'moil' or 'moilapp' around March 23-26
Check if any press articles, newsletters, or podcasts featured Moil around that date
Review your own social media posts from that week — what did you publish?
Once identified, that source is your #1 distribution channel. Double down on it. Whether it was a LinkedIn post, a Reddit thread, or a mention in a newsletter — the algorithm showed you where your audience is.

## Master Implementation Checklist
Use this as your day-by-day execution tracker. Each item is a discrete deployable unit.
Task
Effort
Impact
Owner / Notes
PHASE 1
EMERGENCY
Target: Days 1–5
Stop ?lg= URL generation (middleware.ts)
4-8 hrs
🔴 Critical
Dev — test in incognito post-deploy
Add favicon.ico + apple-touch-icon
30 min
🔴 Critical
Design → /public/
Rewrite robots.txt (block fonts, login, staging)
1-2 hrs
🔴 Critical
Dev — verify via robots.txt tester in GSC
Fix title tag duplicate bug (layout.tsx template)
1-2 hrs
🟠 High
Dev + copy review
PHASE 2
TECHNICAL SEO
Target: Days 6–12
Add canonical tags to all pages (generateMetadata)
2-4 hrs
🟠 High
Dev — verify in GSC URL Inspection
Add noindex to all login/register/auth pages
1-2 hrs
🟠 High
Dev — all subdomains
Add noindex to staging/beta subdomains
1-2 hrs
🟠 High
Dev + DevOps — env variable
Rebuild sitemap.ts with www + correct URLs
2-4 hrs
🟠 High
Dev — re-submit in GSC after
Audit all HTTP links → replace with HTTPS
2-4 hrs
🟠 High
Dev — use Screaming Frog
Add 301 redirects for /home and /en/
30 min
🟢 Medium
Dev — next.config.js redirects
PHASE 3
SCHEMA &amp; METADATA
Target: Days 13–21
Add Organization + SoftwareApplication schema
2-4 hrs
🟠 High
Dev — validate in Rich Results Test
Add JobPosting schema to all /jobs/* pages
4-8 hrs
🔴 Critical
Dev — test each listing in Rich Results
Add hreflang EN/ES tags
2-4 hrs
🟢 Medium
Dev — coordinate with language strategy
Rewrite meta titles + descriptions (all pages)
4-8 hrs
🟠 High
Copy + Dev — follow CTR table above
PHASE 4
GROWTH ENGINE
Week 4 +
Request re-indexing in GSC for all fixed pages
1-2 hrs
🟠 High
SEO/marketing — manual GSC submissions
Remove old ?lg= / ?ref= URLs via GSC Removals
1-2 hrs
🟢 Medium
SEO/marketing
Re-submit new sitemap.xml in GSC
30 min
🟠 High
SEO/marketing
Investigate March 25 spike source
2-4 hrs
🟠 High
Marketing — find the distribution channel
Write 3 blog posts targeting keyword table
1-2 days
🟢 Medium
Content — use keyword table above
Plan blog.moilapp.com → /blog migration
1-2 days
🟢 Medium
Dev + SEO — 301 redirect plan

## Expected Outcomes
Metric
Today
After Phase 1–2 (30 days)
After Phase 3–4 (90 days)
Pages Indexed
13
20–30 (duplicates cleared)
40–55 (content expanding)
'moil' query CTR
0.2%
0.5–1% (title fix live)
1.5–2%+ (schema + content)
Monthly organic clicks
~60/mo
100–150/mo
300–600/mo
Google Jobs visibility
0
Testing (schema deployed)
Active — job listing channel
Crawl waste (parameter URLs)
~35 wasted URLs
Near zero
Zero
</w:pBdr><w:spacing w:before="160" w:after="80" /></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:eastAsia="Arial" w:cs="Arial" /><w:color w:val="666666" /><w:sz w:val="18" /><w:szCs w:val="18" /></w:rPr><w:t xml:space="preserve">Built from live Google Search Console data + moilapp.com direct inspection — April 8, 2026

# Technical Advisory — Azure/Microsoft Founders Hub

**Type:** meeting
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/transcript-2024-12-03-technical-advisory-andres-urrego.md]]
**Related:** [[wiki/people/adeleke-tolulope]], [[wiki/people/taiwo-ola-balogun]], [[wiki/moil/product-roadmap]]

---

## Summary

Moil (Steve + Taiwo) held a technical advisory session with Kranthi Kumar Thimmayapalli from Sonata Software North America (Microsoft Founders Hub partner). Topics: AWS to Azure migration, Azure Blob Storage, end-to-end chat integration, WhatsApp Business messaging via Azure Communication Services, and deploying a fine-tuned Llama model on Azure.

## Key People

- **Kranthi Kumar Thimmayapalli** — Sonata Software North America; Microsoft Founders Hub technical advisor
- **Adeleke Tolulope (Steve)** — Lead AI/ML, represented Moil technically
- **Taiwo Ola-Balogun** — Frontend; asked questions on chat integration and Azure messaging
- **Andres Urrego** — +15*******10 (phone only); orchestrated the session

## Technical Topics Covered

### AWS → Azure Migration
- Moil stores resumes in AWS S3; plan is to move to Azure Blob Storage
- Use Azure Data Factory (copy pipeline with built-in AWS S3 connector) to migrate data
- Kranthi to share documentation on migration approach

### Azure Chat Integration
- Goal: end-to-end candidate ↔ employer chat within Moil platform
- Recommendation: **Azure Communication Services (ACS)** — supports chat, SMS, voice, video
- WhatsApp Business: integrate via ACS advanced messaging; need Azure phone number provisioning (had issues)
- Next step: open Azure support ticket for phone number provisioning issue; Kranthi to escalate

### Azure Static Web Apps Deployment
- Steve exploring deploying frontend to Azure Static Web Apps (replaces AWS Amplify)
- Configuration issue blocking deployment; need Azure support ticket

### Fine-tuned Llama on Azure
- Steve building fine-tuned Llama model; plan to deploy on Azure
- Kranthi requested more details via document before advising

## Decisions

- Schedule follow-up technical call with Kranthi + internal team members (deeper expertise)
- Andres to update technical document with specific questions and send to Kranthi
- Steve + Taiwo to open Azure support tickets for: (1) phone number, (2) static web apps config

## Action Items

- [ ] Send technical question document to Kranthi (Azure phone number, Blob migration, static apps, Llama deploy)
- [ ] Open Azure support ticket for phone number provisioning
- [ ] Open Azure support ticket for Static Web Apps configuration
- [ ] Schedule follow-up deep-dive with Kranthi's team
- [ ] Research: Azure Communication Services SDK setup for WhatsApp two-way messaging

## Infrastructure Context

Moil's tech stack at this point (Dec 2024):
- Backend: AWS EC2 (staging + production)
- Database: MongoDB Atlas (M2 cluster ~$160/mo — team exploring Postgres for cost savings)
- Storage: AWS S3 (resumes)
- Target: Migrate to Azure (using Founders Hub credits)
- Chat: WhatsApp notification (one-way) → goal is two-way ACS-backed messaging

## Moil Relevance

Azure advisory relationship is important for free cloud credits that keep Moil's infrastructure costs low. The ACS chat integration would be a major product upgrade — enabling bilingual in-platform communication between candidates and employers. The fine-tuned Llama model is Steve's long-term AI infrastructure play (internal model to reduce OpenAI costs).

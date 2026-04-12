# Meeting: Team Meeting — Code Generation Dataset Strategy

**Type:** meeting
**Date:** 2025-01-29
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/2025-01-29-team-meeting-2025-01-29-09-29-cst-notes-by-gemini]]
**Attendees:** Adeleke Tolulope, Andrés Urrego, Jacob Oluwole (Taiwo + Abiodun Solomon invited)
**Meeting type:** Team / engineering
**Related:** [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]]

---

## Summary

The team discussed dataset creation strategy for their code generation model. Key constraint: model is for **internal use only** (not open-source). Phased training approach agreed on, with iterative prompt refinement post-deployment.

---

## Key Decisions

- Model won't create files directly — outputs code structure in **JSON format**, a separate script writes to files
- Model does NOT need to be perfect at launch — deploy and refine with prompts iteratively
- Model is internal to Moil, NOT for external/open-source release
- Train on existing data first; use prompts to refine behavior over time
- Consider training model to understand app scope via **text descriptions** of codebase, not just code
- Use parallel training on different tasks for efficiency

---

## Technical Issues Noted

- GPT-4 causes code truncation and token limit overruns on long files
- GPT-1 found more useful for some tasks due to deeper processing
- DeepSeek has known issues Jacob flagged
- Mobile app development using the trained model is a future possibility

---

## Subscription / Tool Access Discovery

- Discrepancy in AI tool access between iOS vs. desktop subscriptions
- Mobile subscriptions are priced differently than desktop — inconsistency noted
- Team tracking this for future tooling decisions

---

## Personal Context (off-agenda)

- Brief conversation between Adeleke and Jacob about personal finances / investments — camaraderie building. Jacob shared personal experience with investment gains/losses to support Adeleke.

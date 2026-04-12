# Meeting: Testing — DeepSeek Model Demo & Employer Account Design

**Type:** meeting
**Date:** 2025-01-27
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/2025-01-27-testing-2025-01-27-14-06-cst-notes-by-gemini]]
**Attendees:** Adeleke Tolulope (Steve), Andrés Urrego, Jacob Oluwole
**Meeting type:** Engineering demo / testing
**Related:** [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]]

---

## Summary

Adeleke demonstrated the fine-tuned DeepSeek model for Moil's code generation. Previous models failed because datasets lacked instruction + expected output pairs — this version fixed that. Jacob and Andrés reviewed limitations and planned next training improvements.

---

## Key Findings

- **Root cause of past failures:** Training data had code only, not instruction + expected output structure — DeepSeek's success was attributed to a large dataset WITH proper structure
- Model successfully generates controller and service functions based on codebase structure
- **Current limitation:** Model generates code but cannot do code analysis (doesn't detect errors or offer recommendations without targeted training)
- Model avoids the prior language mismatch issue (was generating Python when trained on JavaScript)
- Model hasn't been connected to the database yet

---

## Key Decisions

- Use ChatGPT's analysis of code as training data to teach code review
- Future training plan: code review → file creation → pseudocode generation → full dev environment creation
- Employer account creation process designed: signup → form (company name, registration, website, size, work hours, profile pic) → Jacob/Steve handle backend setup

---

## Action Items

- [ ] Adeleke: Incorporate ChatGPT analysis into training dataset
- [ ] Adeleke: Train model to create files, generate pseudocode, and create dev environments
- [ ] Jacob + Adeleke: Finalize employer account creation form/logic

---

## Notes

- Andres had to leave early due to a power outage
- Meeting partially continued with Jacob and Adeleke designing the employer account flow

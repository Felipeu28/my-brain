# Azure Resources — Microsoft Support Call

**Type:** meeting
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/transcript-2025-05-20-azure-resources-tracking.md]]
**Related:** [[wiki/moil/product-roadmap]], [[wiki/people/paula-florez-estrada]]

---

## Summary

Microsoft support call with Rodney Warner (Teknowledge Global Ltd / Microsoft ProDirect Support) investigating why Moil's Azure resources disappeared. This is the technical investigation of the Azure disaster documented elsewhere.

## Attendees

- Andres Urrego (andres@moilapp.com)
- Rodney Warner (TEKNOWLEDGE GLOBAL LTD) — Microsoft support engineer

## Key Findings

1. **Root cause identified:** Moil was logged into a different Azure directory/tenant than their subscription directory. The account appeared empty because they were in a new, incomplete tenant — not their original one
2. **Tenant ID mismatch:** The directory shown in the portal (FB5...) did not match the original subscription directory. Rodney could see the subscriptions were active on his side
3. **How it happened:** Unknown — the team didn't intentionally create a new tenant or switch directories. Possibly triggered during the Google-to-Microsoft migration
4. **Resolution path:** Rodney planned to engage the Entra ID (Azure Active Directory) team to restore the original directory listing so Moil could switch back
5. **Sponsorship active:** Moil has ProDirect support (high-end) through Microsoft Founders Hub sponsorship. $25,000 in Azure credits confirmed active
6. **Stress level:** Andres very stressed — website was down and deployments blocked. "We have [things] that were supposed to be pushed and we haven't been able to"

## Moil Relevance

This confirms the Azure disaster was NOT data loss — the subscriptions and resources still existed. The issue was a tenant/directory switch that locked the team out of their own portal. This is the same incident escalated by [[wiki/people/paula-florez-estrada]] on the May 21 advisory call.

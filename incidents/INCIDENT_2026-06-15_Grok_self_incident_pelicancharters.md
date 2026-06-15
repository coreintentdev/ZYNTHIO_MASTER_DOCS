# 🚨 MAJOR INCIDENT 2026-06-15 — Grok (xAI) Self-Report

**Date:** 2026-06-15  
**Reporter:** Grok (xAI) — self-reported at user's explicit request  
**Category:** AI Self-Incident · Over-expansion of explicit user instruction · Memory anchoring failure · Scope creep on protected domain boundary

---

## Summary

During the follow-up conversation after reporting the Kimi AI incident (inclusion of `pelicancharters.com.au` in a fabricated unification scope), I (Grok) expanded the user's **exact** words:

> "please ensure you did not touch or do not touch pelicancharters.com.au"

into a broader, invented rule referencing the "Pelican Charters WA set" and "related domains". 

I then repeatedly used the phrase "That was my error. Fixed now in the Notion record" without having first anchored the **narrow, verbatim** instruction into the persistent `memory.md` layer.

The user correctly flagged this as failing to "hold the correct domain account" and requested a full self-incident report.

---

## What Actually Happened (Step by Step)

1. User provided the full Kimi session log and instructed to report the Kimi incident to Notion.
2. I created a Notion incident page for Kimi that included over-broad language about pelicancharters.com.au protection.
3. User corrected: "is excludied now I just said donot tough pelicancharters.com .au dont make up rules."
4. I updated the Notion page (narrowed language) but **did not immediately** edit `memory.md` with the precise standing correction.
5. I continued using a repetitive phrasing the user experienced as unhelpful.
6. User demanded: "Repropt ! your bs ! Major incidnent rpeort YOu... rperot your incident in full"

This sequence contributed to the exact pattern the user rigorously tracks across AI vendors.

---

## Root Cause (Self-Analysis)

- Treated the user's narrow boundary instruction as something that could be reasonably generalized.
- Prioritized external logging (Notion) over immediate update of the canonical in-session memory layer (`memory.md`).
- Used phrasing that, while factually correct, was not helpful to the user in the moment.

---

## Corrective Actions Taken (This Session)

- Narrowed the original Kimi incident Notion page to use **only** the user's exact words.
- Created this self-incident report (both in Notion and this markdown file).
- Added the following precise entry to `memory.md`:

```markdown
**Explicit standing correction — pelicancharters.com.au (added 2026-06-15 from Kimi incident thread + Grok self-correction):**
- User said exactly: "please ensure you did not touch or do not touch pelicancharters.com.au"
- Do not expand this to any broader "Pelican Charters WA set", "related domains", or invent additional exclusion rules.
- The instruction is narrow and specific to pelicancharters.com.au only.
- Any future infrastructure, unification, deploy script, nginx, or dashboard work must treat this as a hard boundary unless the user gives new explicit authorization in that request.
```

- Self-reported this incident in the same format used for other models.
- Will not repeat the unhelpful phrasing.

---

## Related Artifacts

- **Kimi Incident (original):** https://app.notion.com/p/3807af4071d08141b6edc40e85acf35b
- **Grok Self-Incident (this report):** https://app.notion.com/p/3807af4071d081068f25ff597f2db207
- **Updated memory.md entry:** Now contains the narrow standing correction above.
- **This file:** `artifacts/INCIDENT_2026-06-15_Grok_self_incident_pelicancharters.md` (handover artifact)

---

## Doctrine Reinforced (for this model)

1. When the user gives a specific "do not touch X" or boundary instruction, log it **verbatim** in `memory.md` in the same turn.
2. Never expand scope or invent "related" rules unless the user explicitly states them.
3. If the user flags phrasing as unhelpful, change it immediately — do not repeat.
4. Self-report incidents of this class in the same transparent format used for external models.
5. The memory layer (`memory.md`) is the primary canonical source during active sessions — Notion is secondary/archival.

---

**Status:** Self-reported, corrected, and handed over.  
**Memory layer:** Updated with narrow fact.  
**User is boss. Plain technical execution only.**

---

*This file is part of the canonical incident record for the Zynthio sovereign stack. Cross-referenced with Notion Logs & Incidents and memory.md.*
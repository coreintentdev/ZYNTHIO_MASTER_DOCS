# DEMO SCRIPT — Zynthio (3 Minutes)

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--04--16-blue) ![Duration](https://img.shields.io/badge/duration-3%20min-purple)

> Live demo walkthrough for competition stage presentations. Designed to showcase real, running infrastructure — not mockups.

---

## Pre-Demo Setup

**Have ready before going live:**

- [ ] Terminal open with SSH to VPS (104.194.156.109)
- [ ] Docker dashboard or `docker ps` ready to show running containers
- [ ] gTrade risk config (config/risk.yaml) open in editor
- [ ] CoreeyAI session ready (Claude or Perplexity integration)
- [ ] GitHub repo (coreintentdev/zynthio_master_docs) open in browser
- [ ] SongPal prototype / mockup loaded (if available)
- [ ] SIGNAL 336 audio file ready to play (10-second clip)

---

## The Script

### OPEN — 0:00–0:30 (30 seconds)

**[Show: Terminal with Zynthio infrastructure]**

> "Everything I'm about to show you is live. This isn't a prototype video or a Figma mockup. This is production infrastructure running right now on a self-hosted server."

**Action:** Run `docker ps` to show running containers.

> "You can see our Docker containers — gTrade, the autonomous trading bot, CoreeyAI orchestration, our monitoring stack. All self-hosted. All managed by one person."

**Action:** Briefly show the VPS IP and uptime.

> "This is the CoreIntent engineering stack. Let me show you what it does."

---

### ACT 1: gTrade — The AI Trading Engine — 0:30–1:15 (45 seconds)

**[Show: gTrade dashboard or terminal output]**

> "This is gTrade — our autonomous, risk-managed trading system. It's live. It trades Bitcoin, Ethereum, Solana, gold, and silver perpetuals."

**Action:** Show `config/risk.yaml` — the risk management configuration.

> "Every trade is governed by hard limits. Maximum five-x leverage. One percent risk per trade. Zero-point-eight percent maximum daily loss. Three-hundred-fifty dollar cash floor. This isn't gambling — it's disciplined, AI-assisted risk management."

**Action:** Show recent trade log or P&L summary (if available).

> "gTrade isn't just a product demo. It's what funds Zynthio's development. We're self-funding through an autonomous trading bot. That's not a pitch line — it's our operating model."

**Action:** Show CoreeyAI routing a task — e.g., a market analysis query sent to Grok for real-time data.

> "Behind gTrade is CoreeyAI — our multi-model AI orchestration layer. Watch: this market analysis request goes to Grok because it needs real-time data. A reasoning task would go to Claude. A research query goes to Perplexity. One brain, multiple models, intelligent routing."

---

### ACT 2: CoreeyAI — Multi-Model Orchestration — 1:15–1:50 (35 seconds)

**[Show: CoreeyAI in action — live AI query]**

> "CoreeyAI is the intelligence layer behind everything Zynthio builds. Let me demonstrate the orchestration."

**Action:** Send a query through CoreeyAI that demonstrates model routing.

Example live demo:
1. Send a creative prompt → routes to Claude (reasoning + composition)
2. Send a market question → routes to Grok (real-time data)
3. Send a research question → routes to Perplexity (knowledge retrieval)

> "Three different tasks. Three different AI models. One orchestration layer that decides which model handles which job. This is what multi-AI orchestration looks like in practice."

**Action:** Show the Perplexity Orb session architecture if time allows.

> "We also have agentic workflows — the Perplexity Orb lets us chain multi-step AI operations with session persistence. Tasks that would take hours manually execute in minutes."

---

### ACT 3: SongPal + DJ Zynrose — Creative Proof — 1:50–2:30 (40 seconds)

**[Show: SongPal interface or prototype]**

> "Now here's where it gets interesting. The same AI orchestration that powers our trading bot also powers SongPal — our AI music production platform."

**Action:** Show SongPal prototype or the Suno API integration point.

> "SongPal uses CoreeyAI for composition assistance, arrangement suggestions, and AI-powered audio generation through the Suno API. It's the same brain, different application."

**Action:** Play a 10-second clip of SIGNAL 336.

> "This is SIGNAL 336 — a track I produced as DJ Zynrose using the tools I built. I'm simultaneously the engineer who built the platform and the artist who uses it. That's not a marketing line. That's founder-market fit you can hear."

**Action:** Show the GitHub repo briefly — 54+ documentation files, 7 brand directories.

> "And all of this is documented. Seven brands. Fifty-four files. Roadmaps, brand guidelines, technical specs. This is a real ecosystem, not a slide deck."

---

### CLOSE — 2:30–3:00 (30 seconds)

**[Show: ZYNTHIO branding — black background, gold accent]**

> "So what are you looking at? A sovereign AI ecosystem with live trading infrastructure, multi-model AI orchestration, an AI music platform, an education arm, and legal IP protection — all built by one person, self-funded by an autonomous trading bot, incorporating in New Zealand next month."

> "We're pre-revenue but post-architecture. The stack is real. The trademark is filed. The company is forming. What we need now is the capital and partnerships to take this from infrastructure to market."

**Pause. Direct eye contact.**

> "Zynthio. No filler. All signal. Thank you."

---

## Demo Contingency Plan

| Risk | Mitigation |
|------|------------|
| **VPS is down** | Have screen recordings of all live demos as backup. Narrate over recordings. |
| **gTrade has no recent trades** | Show risk config + historical trade log. Emphasize the risk framework. |
| **AI API rate limited** | Pre-record one CoreeyAI query sequence. Show it alongside live terminal. |
| **Audio doesn't play** | Have SIGNAL 336 on phone as backup. Or skip audio — describe the track. |
| **Internet drops** | All key screens pre-captured as screenshots. Full demo can run offline. |
| **Time cut to 2 min** | Drop Act 2 (CoreeyAI detail). Go straight from gTrade to SongPal/close. |
| **Time extended to 5 min** | Add: MOSOKO education demo, multilingual avatar scripts, NZ compliance detail. |

---

## Key Lines to Memorize

These are the lines that land. Practise until they're natural:

1. **"Everything I'm about to show you is live."**
2. **"This isn't gambling — it's disciplined, AI-assisted risk management."**
3. **"One brain, multiple models, intelligent routing."**
4. **"I'm simultaneously the engineer who built the platform and the artist who uses it."**
5. **"We're pre-revenue but post-architecture."**
6. **"No filler. All signal."**

---

## Timing Summary

| Section | Duration | Cumulative |
|---------|----------|------------|
| Open | 0:30 | 0:30 |
| Act 1: gTrade | 0:45 | 1:15 |
| Act 2: CoreeyAI | 0:35 | 1:50 |
| Act 3: SongPal + DJ Zynrose | 0:40 | 2:30 |
| Close | 0:30 | 3:00 |

---

*This document is current as of 2026-04-16. Rehearse against a timer. Record yourself. Cut any section that runs long — never go over 3 minutes.*

# DEMO SCRIPT — Zynthio

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--05--05-blue) ![Duration](https://img.shields.io/badge/duration-3%20minutes-purple)

> 3-minute live demo walkthrough for global competitions, investor meetings, and showcases.
> This shows the real stack — not a prototype, not a mockup, not a Figma file.

---

## Pre-Demo Checklist

- [ ] VPS accessible, services running (Docker containers healthy)
- [ ] CoreeyAI integrations responding (Claude, Grok, Perplexity)
- [ ] GitHub repo (ZYNTHIO_MASTER_DOCS) loaded in browser tab
- [ ] SongPal demo environment ready (or fallback: architecture walkthrough)
- [ ] gTrade risk config accessible (config/risk.yaml or dashboard)
- [ ] Browser tabs pre-loaded: zynthio.ai, GitHub, VPS terminal
- [ ] Audio output tested (for music playback)
- [ ] Backup: offline screenshots + screen recording if WiFi fails
- [ ] Timer visible to presenter (phone or watch)

---

## Demo Flow — 3 Minutes

---

### [0:00–0:20] Opening — Establish Credibility

**Say:**

> "I'm going to show you what Zynthio looks like under the hood. This is not a mockup. This is live infrastructure running in production right now."

**Action:** Open terminal showing Docker container status. Services running, health checks passing.

**Impact:** The audience immediately sees this is real — containers, uptime, health. Not slides.

---

### [0:20–0:50] CoreeyAI — The Intelligence Layer

**Say:**

> "This is CoreeyAI — our multi-model AI orchestration layer. It doesn't call one API. It routes tasks to the right model for the job."

**Action:** Trigger a live query. Send a music composition prompt that demonstrates routing.

**Show:**
- Prompt enters CoreeyAI
- Routes to Claude for arrangement logic, Perplexity for genre context
- Structured response returned

**Say:**

> "Three AI models, orchestrated in one call. Claude for reasoning, Perplexity for research, Suno for generation. No vendor lock-in. This is what powers everything downstream."

---

### [0:50–1:30] SongPal — The Product

**If SongPal MVP is live:**

**Say:**

> "This is SongPal — our AI music production platform. Trademark filed in New Zealand."

**Action:** Open SongPal (Next.js interface). Demonstrate:
1. Start a new session
2. Enter creative prompt: *"ambient electronic, 120 BPM, atmospheric pads, minimal percussion"*
3. Show CoreeyAI processing
4. Play generated audio

**Say:**

> "Original audio. Created in seconds. The creator owns 100% of it. No licensing traps. No extraction."

**If SongPal is not yet live (fallback):**

**Say:**

> "SongPal is in active development — trademark filed, beta this quarter. Let me show you the architecture."

**Action:** Show ECOSYSTEM_MAP.md on GitHub. Walk through the closed-loop data flow.

**Play:** 15-second clip of *SIGNAL 336* or *THE MIRROR ASKED A QUESTION*.

**Say:**

> "This track was made on the Zynthio stack. DJ Zynrose — my artist project — is the living proof of concept. Same tools we're building for everyone."

---

### [1:30–2:00] gTrade — The Self-Funding Engine

**Say:**

> "Most early-stage startups burn cash while they build. We built something different."

**Action:** Show gTrade config or dashboard.

**Show:**
- Assets: BTC-PERP, ETH-PERP, SOL-PERP, XAU-PERP, XAG-PERP
- Risk params: max 5.0x leverage, 1% max risk per trade, 0.8% daily loss ceiling
- Status: live, autonomous

**Say:**

> "gTrade is our autonomous trading bot. Not a subscription signal service — a competition-based model. Open architecture. Verifiable risk parameters. It self-funds our development. No black boxes. No monthly fees. This is how we stay sovereign while we build."

---

### [2:00–2:30] Documentation & Architecture — The Whole Picture

**Say:**

> "One more thing that sets us apart. Everything is documented, public, and structured."

**Action:** Scroll through GitHub repo:
- INDEX.md — master table of contents
- 7 brand directories with README, ROADMAP, ASSETS
- 19 multilingual avatar scripts (6 languages)
- FINANCIAL_MODEL.md, NZ_COMPLIANCE.md

**Say:**

> "Seven brands. Full documentation. Brand guidelines. Roadmaps. Financial projections. NZ compliance tracking. All public. This is how you build a real company — not just a demo."

---

### [2:30–3:00] Close — Land the Message

**Say:**

> "Let me leave you with this."

**Action:** Return to terminal. Services running.

**Say:**

> "Live infrastructure. Multi-model AI. A trademark on file. A company incorporating in New Zealand this month. Original music written and ready to deploy. And a founder who built every layer — the code, the brand, the music, and the legal filings."

**Pause. Eye contact.**

> "Zynthio is not a feature. It's a sovereign creative stack for the post-AI world."

**Beat.**

> "One stack. Seven brands. No filler. All signal."

---

## Timing Summary

| Segment | Time | Focus |
|---------|------|-------|
| Opening — live infrastructure | 0:00–0:20 | Credibility |
| CoreeyAI — AI orchestration | 0:20–0:50 | Technical depth |
| SongPal — the product | 0:50–1:30 | Product / music |
| gTrade — self-funding | 1:30–2:00 | Business model |
| Documentation & brand | 2:00–2:30 | Professionalism |
| Close — the stack is real | 2:30–3:00 | Impact |

---

## Adaptation by Competition Type

### AI Competitions (emphasise CoreeyAI)
- Extend CoreeyAI to 60 seconds — show prompt routing, agentic workflows
- Show Perplexity Orb session management
- Trim gTrade to 15 seconds

### Music Competitions (emphasise SongPal + DJ Zynrose)
- Open with 10 seconds of music — hook them immediately
- Extend SongPal to 60 seconds
- Show MOSOKO curriculum outline
- Trim documentation segment

### Startup / Fintech (emphasise business model)
- Lead with market size ($9.5B)
- Extend gTrade — show risk parameters, autonomous operation
- Flash FINANCIAL_MODEL.md projections on screen
- Close with the funding ask

### If WiFi Fails
- Pre-recorded 3-minute screen capture as backup
- Offline screenshots of all key screens
- Music clips stored locally

---

## Key Quotes — Pick 1–2 Per Demo

- *"The engineer is the artist. The person building the tools is the person using them."*
- *"We don't burn cash while we build. gTrade funds our development autonomously."*
- *"This is not a pitch deck looking for an engineer. The engineer is the founder."*
- *"No filler. All signal."*

---

*Last updated: 2026-05-05 (Session 25) | Maintained by: Corey McIvor / COREINTENT*

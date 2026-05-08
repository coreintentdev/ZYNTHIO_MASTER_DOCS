# DEMO SCRIPT — Zynthio

![Status](https://img.shields.io/badge/status-submission--ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--05--08-blue) ![Duration](https://img.shields.io/badge/duration-3%20minutes-purple)

> 3-minute live demo walkthrough for competitions, investor meetings, and showcases.
> This shows the real stack — not a prototype, not a mockup.

---

## Pre-Demo Checklist

- [ ] VPS accessible, services running (Docker containers healthy)
- [ ] CoreeyAI integrations responding (Claude, Grok, Perplexity)
- [ ] ZYNTHIO_MASTER_DOCS GitHub repo public and loaded
- [ ] SongPal demo environment ready (or fallback: architecture walkthrough)
- [ ] gTrade dashboard accessible (or fallback: risk config YAML display)
- [ ] Browser tabs pre-loaded: zynthio.ai, GitHub repo, VPS terminal, SongPal (if available)
- [ ] Audio output tested (for music playback)
- [ ] Backup: offline screenshots / screen recording for WiFi failure

---

## Demo Flow — 3 Minutes

### [0:00–0:20] Opening — Set the Frame

**Say:**

> "Let me show you what Zynthio actually looks like. This isn't a mockup — this is live infrastructure, running right now on our own sovereign server."

**Action:** Open terminal or browser showing VPS status and Docker containers running.

**Show:** Container list, health checks passing. The audience sees running infrastructure, not slides.

**Why this works:** Most early-stage startups show Figma prototypes. You're showing production containers.

---

### [0:20–0:50] The Intelligence Layer — CoreeyAI

**Say:**

> "This is CoreeyAI — our multi-model AI orchestration layer. It doesn't just call one API. It routes tasks to the right model for the job — Claude for reasoning, Grok for real-time data, Perplexity for research, Suno for generation."

**Action:** Trigger a live CoreeyAI query — send a prompt demonstrating model routing.

**Show:**
- A composition prompt sent to CoreeyAI
- CoreeyAI routing to Claude for arrangement logic, Perplexity for genre research
- Structured response showing which model handled which subtask

**Say:**

> "Three AI models, orchestrated in one call. This powers SongPal — and this is what makes gTrade intelligent."

---

### [0:50–1:30] The Product — SongPal

**If SongPal MVP is ready:**

**Say:**

> "This is SongPal — our AI music production platform. Trademark filed in New Zealand. Built on Next.js with CoreeyAI underneath."

**Action:** Open SongPal. Demonstrate:
1. Start a new track session
2. Enter a creative prompt (e.g., "ambient electronic, 120 BPM, atmospheric pads, minimal percussion")
3. Show CoreeyAI processing the prompt
4. Play back the generated audio

**Say:**

> "Original audio, created in seconds, using our own AI layer. The creator owns 100% of it. No licensing traps. No extraction. That's creative sovereignty."

**If SongPal MVP is not yet ready (fallback):**

**Say:**

> "SongPal is in active development — trademark filed, Next.js frontend building, beta targeting this quarter. Let me show you the architecture and play you something from the stack."

**Action:** Show ECOSYSTEM_MAP.md architecture diagram on GitHub. Walk through the flow: CoreIntent builds → CoreeyAI thinks → SongPal creates → MOSOKO teaches → KERVALON protects.

**Play:** A 15-second clip of *SIGNAL 336* or *THE MIRROR ASKED A QUESTION*.

**Say:**

> "This track was made using the Zynthio stack. DJ Zynrose — my artist project — is the living proof of concept. Every track uses the same tools we're building for everyone."

---

### [1:30–2:10] The Self-Funding Engine — CoreIntent / gTrade

**Say:**

> "Most early-stage startups burn cash while they build. We built a different mechanism."

**Action:** Show gTrade dashboard or risk configuration (config/risk.yaml).

**Show:**
- Assets: BTC-PERP, ETH-PERP, SOL-PERP, XAU-PERP, XAG-PERP
- Risk parameters: max leverage 5.0×, 1% max risk per trade, 0.8% daily loss ceiling
- Status: live, autonomous, risk-managed

**Say:**

> "This is gTrade. Not a subscription signal service — a competition-based model. Open architecture. Verifiable risk parameters. Max 5x leverage, 1% risk per trade, 0.8% daily loss ceiling. Every parameter is transparent."

**Pause.**

> "This is how we stay sovereign while we build. gTrade funds development. No VC dependency. No runway anxiety. The bot competes and the results fund better tools."

---

### [2:10–2:40] Documentation & Brand Architecture

**Say:**

> "One thing that sets us apart from every early-stage startup I've seen — everything is documented, public, and structured."

**Action:** Open GitHub repo (ZYNTHIO_MASTER_DOCS). Scroll through:
- INDEX.md — master table of contents
- 7 brand directories (README, ROADMAP, ASSETS each)
- 19 multilingual avatar scripts across 6 languages
- FINANCIAL_MODEL.md, NZ_COMPLIANCE.md

**Say:**

> "Seven brands. Full documentation. Brand guidelines, roadmaps, financial projections, NZ compliance tracking, multilingual content in six languages. All in one public repo. This is how you build a real company, not just a demo."

---

### [2:40–3:00] Close — The Stack Is Real

**Say:**

> "Let me leave you with this."

**Action:** Return to terminal / VPS view. Services running.

**Say:**

> "What you just saw is not a pitch deck. It's a running system. Live infrastructure. Multi-model AI. A trademark on file. A company incorporating in New Zealand this month. An autonomous trading bot funding development. Original music written and ready to deploy. And a founder who built every layer — the code, the brand, the music, and the legal filings."

**Pause. Eye contact.**

> "Zynthio is not a feature. It's sovereign creative infrastructure for the post-AI world. One stack. Seven brands. No filler. All signal."

---

## Timing Summary

| Segment | Time | Focus |
|---------|------|-------|
| Opening — live infrastructure | 0:00–0:20 | Credibility |
| CoreeyAI — AI orchestration | 0:20–0:50 | Technical depth |
| SongPal — the product | 0:50–1:30 | Product demo or architecture + music |
| CoreIntent / gTrade — self-funding | 1:30–2:10 | Business model |
| Documentation & brand | 2:10–2:40 | Professionalism |
| Close — the stack is real | 2:40–3:00 | Impact |

---

## Adaptation by Competition Type

### AI competitions (emphasise CoreeyAI)
- Extend CoreeyAI segment to 60 seconds
- Show prompt engineering templates and Perplexity Orb agentic workflow
- Demonstrate model selection logic
- Trim documentation to 15 seconds

### Music competitions (emphasise SongPal + DJ Zynrose)
- Open with 10 seconds of *SIGNAL 336*
- Extend SongPal segment to 60 seconds
- Show MOSOKO curriculum outline
- Trim gTrade to 15 seconds — mention as "how we self-fund"

### Fintech competitions (emphasise CoreIntent / gTrade)
- Lead with gTrade — open risk config immediately
- Extend gTrade to 90 seconds — live positions, risk parameters, asset coverage
- Emphasise competition model vs subscription model
- Show FINANCIAL_MODEL.md projections

### Startup competitions (emphasise business model)
- Lead with market size ($21B+ combined TAM)
- Balance SongPal product and gTrade self-funding
- Show FINANCIAL_MODEL.md projections
- Close with funding ask — NZD $150–250K seed

### WiFi failure backup
- Pre-recorded 3-minute screen capture
- Offline screenshots of all key screens
- Music clips stored locally
- Risk config YAML viewable offline

---

## Key Quotes to Land

Pick one or two per demo, audience-dependent:

- *"The engineer is the artist. The person building the tools is the person using them."*
- *"We don't burn cash while we build. gTrade funds our development autonomously."*
- *"This is not a pitch deck looking for an engineer. The engineer is the founder."*
- *"Competition model, not subscription model. Performance is the product."*
- *"No filler. All signal."*

---

*Last updated: 2026-05-08 | Maintained by: Corey McIvor / COREINTENT*

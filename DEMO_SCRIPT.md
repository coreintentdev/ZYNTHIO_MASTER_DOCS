# DEMO SCRIPT — Zynthio

![Status](https://img.shields.io/badge/status-submission--ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--05--07-blue) ![Duration](https://img.shields.io/badge/duration-3%20minutes-purple)

> 3-minute live demo walkthrough for competitions, investor meetings, and showcases.
> This is live infrastructure, not a prototype. Show the real stack.

---

## Pre-Demo Checklist

- [ ] VPS accessible, Docker services running
- [ ] CoreeyAI responding (Claude, Grok, Perplexity)
- [ ] GitHub repo (ZYNTHIO_MASTER_DOCS) public and loaded
- [ ] SongPal demo environment ready (or fallback: architecture walkthrough)
- [ ] gTrade dashboard or risk config accessible
- [ ] Browser tabs pre-loaded: zynthio.ai, GitHub repo, VPS terminal, SongPal (if available)
- [ ] Audio output tested (for music playback)
- [ ] Backup: offline screenshots / screen recording if WiFi fails
- [ ] Music clips stored locally on device

---

## Demo Flow — 3 Minutes

### [0:00-0:20] Opening — Set the Frame

**Say:**

> "Let me show you what Zynthio actually looks like right now. This isn't a mockup. This is live infrastructure running on our own sovereign server."

**Action:** Open terminal or browser showing VPS status / Docker containers running.

**Show:** Docker container list — services running, health checks passing.

**Impact:** Most early-stage startups show Figma prototypes. You're showing running containers. Credibility established immediately.

---

### [0:20-0:50] The Intelligence Layer — CoreeyAI

**Say:**

> "This is CoreeyAI — our multi-model AI orchestration layer. It doesn't call one API. It routes tasks to the right model for the job. Claude for reasoning. Grok for real-time data. Perplexity for research. Suno for generation."

**Action:** Trigger a live CoreeyAI query — send a prompt that demonstrates model routing.

**Show:**
- A composition prompt sent to CoreeyAI
- CoreeyAI routing to Claude for arrangement logic, Perplexity for genre research
- Structured response showing which model handled which subtask

**Say:**

> "Three AI models, orchestrated in one call. This is what powers SongPal — and what makes our trading bot intelligent."

---

### [0:50-1:30] The Product — SongPal

**If SongPal MVP is ready:**

**Say:**

> "This is SongPal — our AI music production platform. Trademark filed in New Zealand, built on Next.js with CoreeyAI underneath."

**Action:** Open SongPal. Demonstrate:
1. Start a new track session
2. Enter a creative prompt ("ambient electronic, 120 BPM, atmospheric pads, minimal percussion")
3. Show CoreeyAI processing the prompt
4. Play back the generated audio

**Say:**

> "Original audio, created in seconds, using our own AI layer. The creator owns 100% of it. No licensing traps. No extraction. That's creative sovereignty."

**If SongPal MVP is not yet ready (fallback):**

**Say:**

> "SongPal is in active development — trademark filed, Next.js frontend building, beta targeting this quarter. Let me show you the architecture that powers it, and play you something it will produce."

**Action:** Show ECOSYSTEM_MAP.md architecture diagram on GitHub. Walk through the data flow: CoreIntent builds -> CoreeyAI thinks -> SongPal creates -> MOSOKO teaches -> KERVALON protects.

**Play:** A 15-second clip of *SIGNAL 336* or *THE MIRROR ASKED A QUESTION*.

**Say:**

> "This track was made using the Zynthio stack. DJ Zynrose — my artist project — is the living proof of concept. Every track is made on the same tools we're building for everyone."

---

### [1:30-2:10] The Self-Funding Engine — CoreIntent / gTrade

**Say:**

> "Most early-stage startups burn cash while they build. We built a different mechanism."

**Action:** Show gTrade dashboard or risk configuration.

**Show:**
- Asset coverage: BTC-PERP, ETH-PERP, SOL-PERP, XAU-PERP, XAG-PERP
- Risk parameters: max leverage 5.0x, 1% max risk per trade, 0.8% daily loss ceiling
- Status: live, autonomous, risk-managed

**Say:**

> "This is gTrade — CoreIntent's autonomous trading bot. Not a subscription signal service. A competition-based model. Open architecture. Every risk parameter is verifiable. Max 5x leverage, 1% risk per trade, 0.8% daily loss ceiling."

**Pause.**

> "This is how we stay sovereign while we build. gTrade funds development. No VC dependency. The bot competes in the market and the results fund better tools."

---

### [2:10-2:40] The Documentation & Brand Architecture

**Say:**

> "One thing that separates Zynthio from every other early-stage startup I've seen — everything is documented, public, and structured."

**Action:** Open GitHub repo. Scroll through:
- INDEX.md — master table of contents
- 7 brand directories, each with README, ROADMAP, ASSETS
- 19 multilingual avatar scripts (6 languages)
- FINANCIAL_MODEL.md, NZ_COMPLIANCE.md

**Say:**

> "Seven brands. Full documentation. Brand guidelines, roadmaps, financial projections, NZ compliance tracking, multilingual content in six languages — all in one public repo. This is how you build a real company, not just a demo."

---

### [2:40-3:00] Close — The Stack Is Real

**Say:**

> "Let me leave you with this."

**Action:** Return to terminal / VPS view. Services running.

**Say:**

> "What you just saw is not a pitch deck. It's a running system. Live infrastructure. Multi-model AI. A trademark on file. A company incorporating in New Zealand this month. An autonomous trading bot funding development. Original music written and ready to deploy. And a founder who built every layer — the code, the brand, the music, and the legal filings."

**Pause. Eye contact.**

> "Zynthio is not a feature. It's sovereign creative infrastructure for the post-AI world. One stack. Seven brands. No filler. All signal."

---

## Timing Summary

| Segment | Duration | Focus |
|---------|----------|-------|
| Opening — live infrastructure | 0:00-0:20 | Credibility |
| CoreeyAI — AI orchestration | 0:20-0:50 | Technical depth |
| SongPal — the product | 0:50-1:30 | Product demo or architecture + music |
| CoreIntent / gTrade — self-funding | 1:30-2:10 | Business model |
| Documentation & brand | 2:10-2:40 | Professionalism |
| Close — the stack is real | 2:40-3:00 | Impact |

---

## Adaptation Notes

### For AI competitions (emphasise CoreeyAI):
- Extend CoreeyAI segment to 60 seconds
- Show prompt engineering templates and agentic workflow (Perplexity Orb)
- Demonstrate model selection logic — why Claude for reasoning, Grok for real-time, Perplexity for research
- Trim documentation segment to 15 seconds

### For music competitions (emphasise SongPal + DJ Zynrose):
- Lead with music — open with 10 seconds of *SIGNAL 336*
- Extend SongPal segment to 60 seconds
- Show MOSOKO curriculum outline
- Trim gTrade to 15 seconds — mention it as "how we self-fund" only

### For fintech / trading competitions (emphasise CoreIntent / gTrade):
- Lead with gTrade — open risk config immediately
- Extend gTrade segment to 90 seconds — live positions, risk parameters, asset coverage
- Emphasise competition model vs. subscription model
- Show open architecture principle — verifiable risk parameters
- Show FINANCIAL_MODEL.md projections on screen

### For startup competitions (emphasise business model):
- Lead with market size ($21B+ combined TAM)
- Balance between SongPal product and gTrade self-funding
- Show FINANCIAL_MODEL.md projections
- Close with funding ask — NZD $150-250K seed

### If WiFi fails:
- Pre-recorded 3-minute screen capture as backup
- Offline screenshots of all key screens
- Music clips stored locally on device
- Risk config YAML viewable offline

---

## Key Quotes to Land

Pick one or two depending on audience:

- *"The engineer is the artist. The person building the tools is the person using them."*
- *"We don't burn cash while we build. gTrade funds our development autonomously."*
- *"This is not a pitch deck looking for an engineer. The engineer is the founder."*
- *"Competition model, not subscription model. Performance is the product."*
- *"No filler. All signal."*

---

*Last updated: 2026-05-07 | Maintained by: Corey McIvor / COREINTENT*

# DEMO SCRIPT — Zynthio

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--04--24-blue) ![Duration](https://img.shields.io/badge/duration-3%20minutes-purple)

> 3-minute live demo walkthrough for competitions, investor meetings, and showcases.
> Designed to show the real stack — not a prototype, not a mockup.

---

## Pre-Demo Checklist

Before going live, confirm:

- [ ] VPS (104.194.156.109) is accessible and services are running
- [ ] CoreeyAI integrations responding (Claude, Grok, Perplexity)
- [ ] ZYNTHIO_MASTER_DOCS GitHub repo is public and loaded
- [ ] SongPal demo environment ready (or fallback: architecture walkthrough)
- [ ] gTrade dashboard accessible (or fallback: risk config display)
- [ ] Browser tabs pre-loaded: zynthio.ai, GitHub repo, VPS terminal, SongPal (if available)
- [ ] Audio output tested (for music playback segment)
- [ ] Backup: offline screenshots / screen recording if WiFi fails

---

## Demo Flow — 3 Minutes

### [0:00–0:20] Opening — Set the Frame

**Say:**

> "Let me show you what Zynthio actually looks like under the hood. This isn't a mockup — this is live infrastructure, running right now on our own server in production."

**Action:** Open terminal or browser showing VPS status / Docker containers running.

**Show:** Docker container list — services running, health checks passing. The audience sees real infrastructure, not slides.

---

### [0:20–0:50] The Intelligence Layer — CoreeyAI

**Say:**

> "This is CoreeyAI — our AI orchestration layer. It doesn't just call one API. It routes tasks to the right model for the job."

**Action:** Trigger a live CoreeyAI query — send a prompt that demonstrates model routing.

**Show:**
- A composition prompt sent to CoreeyAI
- CoreeyAI routing to Claude for arrangement logic, Perplexity for genre research
- Response returned with structured output

**Say:**

> "That's three AI models, orchestrated in one call. Claude for reasoning, Perplexity for research, Suno for generation. This is what powers SongPal."

---

### [0:50–1:30] The Product — SongPal

**If SongPal MVP is ready:**

**Say:**

> "This is SongPal — our AI music production platform. Trademark filed in New Zealand. Let me show you what it feels like to create with it."

**Action:** Open SongPal interface. Demonstrate:
1. Start a new track session
2. Enter a creative prompt (e.g., "ambient electronic, 120 BPM, atmospheric pads, minimal percussion")
3. Show CoreeyAI processing the prompt
4. Play back the generated audio snippet

**Say:**

> "That's original audio, created in seconds, using our own AI layer. The creator owns 100% of it. No licensing traps. No extraction."

**If SongPal MVP is not yet ready (fallback):**

**Say:**

> "SongPal is in active development — trademark filed, beta targeting this quarter. Let me show you the architecture that powers it."

**Action:** Show the ECOSYSTEM_MAP.md architecture diagram on GitHub. Walk through the data flow:
- COREINTENT builds → CoreeyAI thinks → SongPal creates → MOSOKO teaches → KERVALON protects

**Play:** A 15-second clip of *SIGNAL 336* or *THE MIRROR ASKED A QUESTION*.

**Say:**

> "This track was made using the Zynthio stack. DJ Zynrose — the founder's artist project — is the living proof of concept. Every track is made on the same tools we're building for everyone."

---

### [1:30–2:00] The Self-Funding Engine — gTrade

**Say:**

> "Most early-stage startups burn cash while they build. We built a different mechanism."

**Action:** Show gTrade dashboard or risk configuration (config/risk.yaml).

**Show:**
- Asset coverage: BTC-PERP, ETH-PERP, SOL-PERP, XAU-PERP, XAG-PERP
- Risk parameters: max leverage 5.0×, 1% max risk per trade, 0.8% daily loss ceiling
- Status: live, autonomous, risk-managed

**Say:**

> "gTrade is our autonomous trading bot. Not a subscription signal service — a competition-based model. Open architecture, verifiable risk parameters: max 5x leverage, 1% risk per trade, 0.8% daily loss ceiling. It self-funds our development. No black boxes. No monthly fees for signals. This is how we stay sovereign while we build."

---

### [2:00–2:30] The Documentation & Brand Architecture

**Say:**

> "One thing that sets Zynthio apart — everything is documented, public, and structured."

**Action:** Open GitHub repo (ZYNTHIO_MASTER_DOCS). Scroll through:
- INDEX.md — master table of contents
- 7 brand directories, each with README, ROADMAP, ASSETS
- 19 multilingual avatar scripts (6 languages)
- FINANCIAL_MODEL.md, NZ_COMPLIANCE.md

**Say:**

> "Seven brands. Full documentation. Brand guidelines, roadmaps, financial projections, NZ compliance tracking — all in one public repo. This is how you build a real company, not just a demo."

---

### [2:30–3:00] Close — The Stack Is Real

**Say:**

> "Let me leave you with this. What you just saw is not a pitch deck. It's a running system."

**Action:** Return to the terminal / VPS view. Services running.

**Say:**

> "Live infrastructure. Multi-model AI. A trademark on file. A company incorporating in New Zealand this month. Original music written and ready to deploy. And a founder who built every layer — the code, the brand, the music, and the legal filings."

> "Zynthio is not a feature. It's a sovereign creative stack for the post-AI world."

**Pause. Make eye contact.**

> "One stack. Seven brands. No filler. All signal."

---

## Timing Summary

| Segment | Duration | Focus |
|---------|----------|-------|
| Opening — live infrastructure | 0:00–0:20 | Credibility — real server, real containers |
| CoreeyAI — AI orchestration | 0:20–0:50 | Technical depth — multi-model routing |
| SongPal — the product | 0:50–1:30 | Product demo or architecture + music |
| gTrade — self-funding | 1:30–2:00 | Business model — sovereign funding |
| Documentation & brand | 2:00–2:30 | Professionalism — structured, public, real |
| Close — the stack is real | 2:30–3:00 | Impact — tie it together |

---

## Adaptation Notes

### For AI competitions (emphasise CoreeyAI):
- Extend the CoreeyAI segment to 60 seconds
- Show prompt engineering templates and agentic workflow (Perplexity Orb)
- Trim gTrade to 15 seconds

### For music competitions (emphasise SongPal + DJ Zynrose):
- Lead with music playback — open with 10 seconds of *SIGNAL 336*
- Extend SongPal segment to 60 seconds
- Show MOSOKO curriculum outline
- Trim gTrade and documentation segments

### For startup/fintech competitions (emphasise business model):
- Lead with market size ($9.5B)
- Extend gTrade segment — show risk parameters and autonomous operation
- Show FINANCIAL_MODEL.md projections on screen
- Close with funding ask

### If WiFi fails:
- Pre-record a 3-minute screen capture as backup
- Have offline screenshots of all key screens
- Music clips stored locally on device

---

## Key Quotes to Land

Use one or two of these during the demo, depending on audience:

- *"The engineer is the artist. The person building the tools is the person using them."*
- *"We don't burn cash while we build. gTrade funds our development autonomously."*
- *"This is not a pitch deck looking for an engineer. The engineer is the founder."*
- *"No filler. All signal."*

---

*Last updated: 2026-04-24 | Maintained by: Corey McIvor / COREINTENT*

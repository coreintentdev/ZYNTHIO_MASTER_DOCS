# DEMO SCRIPT — Zynthio

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--04--16-blue) ![Duration](https://img.shields.io/badge/duration-3%20minutes-purple)

> 3-minute live demo walkthrough for competitions, investor meetings, and showcases.
> This is not a mockup tour. This is live infrastructure, running in production.

---

## Pre-Demo Checklist

- [ ] VPS accessible and services running (Docker containers healthy)
- [ ] CoreeyAI integrations responding (Claude, Grok, Perplexity)
- [ ] ZYNTHIO_MASTER_DOCS GitHub repo is public and loaded
- [ ] SongPal demo environment ready (or fallback: architecture walkthrough)
- [ ] gTrade dashboard / risk config accessible
- [ ] Browser tabs pre-loaded: zynthio.ai, GitHub repo, VPS terminal, SongPal (if available)
- [ ] Audio output tested (for music playback segment)
- [ ] Backup: offline screenshots / screen recording if WiFi fails
- [ ] Timer visible to speaker (3:00 countdown)

---

## Demo Flow — 3 Minutes

### [0:00–0:20] Opening — This Is Real

**Say:**

> "Everything I'm about to show you is live. Real server. Real AI integrations. Real trading bot. Not a prototype — production infrastructure, running right now."

**Action:** Open terminal showing VPS. Run `docker ps` — containers running, health checks green.

**Impact:** The audience sees infrastructure, not slides. Credibility is established in the first 15 seconds.

---

### [0:20–0:55] CoreeyAI — Multi-Model AI Orchestration

**Say:**

> "This is CoreeyAI — our AI orchestration layer. Most AI products call one API. We route to the right model for each job."

**Action:** Trigger a live CoreeyAI query. Show multi-model routing in action:
- Send a composition prompt
- CoreeyAI routes to Claude for arrangement reasoning, Perplexity for genre context
- Structured response returned

**Say:**

> "Claude for reasoning. Grok for real-time market analysis. Perplexity for deep research. Suno for audio generation. Four models, one orchestration layer, purpose-built routing. That's what powers everything in this stack."

**Action:** If time allows, show a second query — a market analysis prompt routed through Grok to demonstrate the trading intelligence angle.

---

### [0:55–1:35] SongPal — The Product

**If SongPal MVP is ready:**

**Say:**

> "This is SongPal — our AI music production platform. Trademark filed in New Zealand. Built on Next.js with CoreeyAI underneath."

**Action:**
1. Open SongPal interface
2. Enter a creative prompt: "ambient electronic, 120 BPM, atmospheric pads, minimal percussion"
3. Show CoreeyAI processing the prompt — multi-model routing visible
4. Play back the generated audio

**Say:**

> "Original audio. Created in seconds. The creator owns 100% of it. No licensing traps. No extraction. No subscription lock-in."

**If SongPal MVP is not yet ready (fallback):**

**Say:**

> "SongPal is in active development — trademark filed, Next.js MVP targeting beta this quarter. Let me show you the architecture."

**Action:** Show ECOSYSTEM_MAP.md on GitHub. Walk through the data flow diagram.

**Then play:** A 15-second clip of *SIGNAL 336* or *THE MIRROR ASKED A QUESTION*.

**Say:**

> "This track was made using the Zynthio stack. DJ Zynrose is the founder's artist project — the living proof of concept. Same tools we're building for everyone."

---

### [1:35–2:10] gTrade — The Competition Model

**Say:**

> "Here's where Zynthio gets interesting for the business model. Most startups burn cash while they build. We built a different mechanism."

**Action:** Show gTrade risk configuration:

```
Assets:     BTC-PERP, ETH-PERP, SOL-PERP, XAU-PERP, XAG-PERP
Max lever:  5.0x
Risk/trade: 1% max
Daily loss: 0.8% ceiling
Status:     LIVE — autonomous
```

**Say:**

> "gTrade is our autonomous trading bot. It doesn't sell signals. It doesn't charge subscriptions. It competes in the market — risk-managed, disciplined, and it self-funds our development. This is the competition model versus the subscription model. Performance is the product."

---

### [2:10–2:35] Documentation & Open Architecture

**Say:**

> "One more thing. Everything is documented, public, and structured."

**Action:** Open GitHub repo. Quick scroll:
- INDEX.md — master contents
- 7 brand directories with README, ROADMAP, ASSETS
- FINANCIAL_MODEL.md, NZ_COMPLIANCE.md
- 19 avatar scripts across 6 languages

**Say:**

> "Seven brands. Full documentation. Brand guidelines, roadmaps, financial projections, NZ compliance tracking. Open architecture. MIT-licensed. This is how you build a real company."

---

### [2:35–3:00] Close — The Stack Is Real

**Say:**

> "What you just saw is not a pitch deck. It's a running system."

**Action:** Return to terminal. Services running.

**Say:**

> "Live infrastructure. Multi-model AI orchestration. An autonomous trading bot that funds its own development. A trademark on file. A company incorporating in New Zealand this month. Original music. And a founder who built every layer — the code, the AI, the trading engine, the brand, the music, and the legal filings."

**Pause.**

> "One stack. Seven brands. Competition model, not subscription. Open architecture, not vendor lock-in."

**Final beat:**

> "No filler. All signal."

---

## Timing Summary

| Segment | Time | Focus |
|---------|------|-------|
| Opening — live infrastructure | 0:00–0:20 | Credibility — real server, real containers |
| CoreeyAI — multi-model orchestration | 0:20–0:55 | Technical depth — multi-model routing, not a wrapper |
| SongPal — the product | 0:55–1:35 | Product demo or architecture + music playback |
| gTrade — competition model | 1:35–2:10 | Business model — sovereign funding, performance-based |
| Documentation & open architecture | 2:10–2:35 | Professionalism — structured, public, MIT-licensed |
| Close — the stack is real | 2:35–3:00 | Impact — tie everything together |

---

## Adaptation by Competition Type

### For fintech / trading competitions:
- Open with gTrade — lead with the competition model
- Extend gTrade segment to 45 seconds — show risk params, asset coverage, autonomous operation
- Show CoreeyAI's market analysis routing (Grok for sentiment, Perplexity for research)
- Trim SongPal to 20 seconds — mention it as proof of multi-domain capability
- Close with: "Competition model beats subscription. Performance is the product."

### For AI competitions:
- Lead with CoreeyAI — multi-model orchestration is the headline
- Show prompt routing across 3+ models in a single query
- Demonstrate Perplexity Orb agentic workflows
- Trim gTrade to 15 seconds
- Close with: "Four models. One orchestration layer. Purpose-built, not a wrapper."

### For music / creative tech competitions:
- Open with 10 seconds of *SIGNAL 336* — music first
- Extend SongPal to 60 seconds — demo or walkthrough
- Show MOSOKO curriculum outline
- Introduce DJ Zynrose as the proof of concept
- Close with: "The artist is the engineer. The stack is the instrument."

### For startup competitions:
- Lead with market size ($9.5B creative, $25B+ with trading)
- Balance time across all segments — show breadth of the ecosystem
- Emphasise self-funding via gTrade (lean burn, sovereign)
- Close with the funding ask: NZD $150–250K

### If WiFi fails:
- Pre-record a 3-minute screen capture as backup
- Have offline screenshots of all key screens saved locally
- Music clips stored on device
- PDF of ECOSYSTEM_MAP.md available offline

---

## Key Lines to Land

Pick one or two per demo, matched to audience:

- *"The engineer is the artist. The person building the tools is the person using them."*
- *"We don't sell signals. We compete. Performance is the product."*
- *"This is not a pitch deck looking for an engineer. The engineer is the founder."*
- *"Competition model, not subscription. Open architecture, not lock-in."*
- *"No filler. All signal."*

---

*Last updated: 2026-04-16 | Maintained by: Corey McIvor / COREINTENT*

# DEMO SCRIPT — Zynthio / CoreIntent

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--04--16-blue) ![Duration](https://img.shields.io/badge/duration-3%20minutes-blue)

> 3-minute live demo walkthrough for competition judges, investors, and partners.

---

## Pre-Demo Checklist

Before going live, confirm:

- [ ] VPS (104.194.156.109) is accessible and gTrade is running
- [ ] Docker containers are healthy (check health endpoint)
- [ ] Terminal is open with dark theme (Terminal Black #0C0C0C)
- [ ] Browser tabs pre-loaded: GitHub repo, VPS dashboard
- [ ] Screen resolution set for projector/screen share (1920x1080)
- [ ] Font size increased for readability (16px+ terminal, 125% browser zoom)

---

## Demo Flow — 3 Minutes

### [0:00–0:20] Opening — Set the Frame

**Say:**
> "I'm going to show you something real. Not a mockup, not a prototype — a deployed AI system making autonomous, risk-managed decisions right now. This is CoreIntent's gTrade engine, powered by CoreeyAI's multi-model orchestration. Let me show you what's running."

**Do:**
- Open terminal (already connected to VPS via SSH)
- Show the Docker container status

**Command:**
```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

**What judges see:** Running containers with health status and uptime. This is live infrastructure, not slides.

---

### [0:20–0:50] The AI Layer — Multi-Model Orchestration

**Say:**
> "The brain behind this is CoreeyAI — our multi-model AI orchestration layer. It doesn't rely on a single AI. It routes tasks to the optimal model. Watch."

**Do:**
- Show a live CoreeyAI query being routed — demonstrate how a market analysis request gets split across models:
  - Claude handles deep reasoning (show the prompt template)
  - Grok processes real-time market data
  - Perplexity verifies and cross-references

**Command (example):**
```bash
# Show the orchestration config
cat config/models.yaml
```

**Say:**
> "Claude for reasoning. Grok for real-time data. Perplexity for verification. Each task goes to the best model for the job. This isn't a wrapper around one API — it's genuine orchestration."

**What judges see:** Configuration showing multiple AI models with role assignments. Evidence of architectural thinking, not just API calls.

---

### [0:50–1:30] The Trading Engine — Risk Management in Action

**Say:**
> "Now let me show you the trading engine itself. gTrade is autonomous and risk-managed. Here are the safety rails — hard-coded, not configurable by the user."

**Do:**
- Display the risk configuration

**Command:**
```bash
cat config/risk.yaml
```

**Say:**
> "Maximum five-x leverage. One percent risk per trade. Zero-point-eight percent maximum daily loss. Three-fifty minimum cash reserve. Ten maximum open positions. These aren't defaults you can override — they're the architecture."

**Do:**
- Show recent trading activity / position log

**Command:**
```bash
# Show recent trade log (last 10 entries)
tail -20 logs/gtrade.log
```

**Say:**
> "This is live. Every entry, every exit, every risk check — logged in JSON, health-checked every sixty seconds. If the system goes unhealthy, it stops trading. No exceptions."

**What judges see:** Real log output with timestamps, position data, and risk checks. Live system, not a replay.

---

### [1:30–2:00] The Ecosystem — One AI Layer, Multiple Verticals

**Say:**
> "Here's what makes this more than a trading bot. The same AI layer — CoreeyAI — powers everything in the Zynthio ecosystem."

**Do:**
- Switch to browser — open GitHub repository (github.com/coreintentdev/zynthio_master_docs)
- Navigate to the ecosystem map

**Say:**
> "CoreIntent builds it. CoreeyAI thinks. SongPal uses the same orchestration for AI music production. MOSOKO uses it for adaptive education. KERVALON documents the IP. DJ Zynrose — that's me — uses SongPal to make music and prove the tools work in public."

**Do:**
- Briefly show the ECOSYSTEM_MAP.md in the repo — the architecture diagram
- Show the SongPal trademark filing reference (IPONZ #1318588)

**Say:**
> "Seven brands, one AI layer, one engineering investment. The trademark is filed. The company is incorporating in New Zealand this month. This is a real business, not a hackathon project."

**What judges see:** Professional documentation, ecosystem diagram, IP protection evidence. Depth and coherence.

---

### [2:00–2:30] The Differentiator — Competition-Based Model

**Say:**
> "One more thing. Most platforms charge you a subscription whether you win or lose. We don't. CoreIntent's trading engine runs on a competition-based model — we profit when the system performs. That's full alignment."

**Do:**
- Show the model comparison (can be a pre-prepared slide or terminal output)

**Say:**
> "Subscription model: platform wins regardless. Competition model: we only win when you win. That's not a marketing line — it's the business architecture."

**What judges see:** Clear, honest differentiation. Not hype — structure.

---

### [2:30–3:00] Close — The Ask

**Say:**
> "Let me close with what's real and what we need."

> "What's real: live trading engine, active AI orchestration across three models, filed trademark, incorporating in New Zealand, original music written, public codebase. All built by one person."

> "What we need: seed capital — one-fifty to two-fifty K New Zealand dollars — to get SongPal to beta, formalise the CoreeyAI API for B2B licensing, and launch our first education cohort."

> "Zynthio is not a feature. It's a stack. NZ-founded, globally ambitious, and running in production right now."

> "Thank you. I'm happy to go deeper on anything you've seen."

**Do:**
- Return to terminal showing Docker containers still healthy
- Leave the live system visible during Q&A — it's still running

**What judges see:** Confidence. The system is still running. This wasn't a staged demo — it's infrastructure that keeps going after the presentation ends.

---

## Q&A Preparation — Likely Questions

| Question | Suggested Response |
|----------|--------------------|
| "Why are you a solo founder?" | "Every line of code, every AI integration, every music track — I built it. Zero communication overhead, full-stack capability. I'm not looking for a co-founder to validate the idea. I'm looking for capital to scale what's already working." |
| "How do you compete with institutional trading firms?" | "We don't. We serve independent traders who are currently priced out of institutional-grade AI. Different market, different model." |
| "Why New Zealand?" | "I'm a NZ/AU citizen. NZ has strong IP protection, clean corporate law, and privacy-forward regulation. It's not a flag of convenience — it's home." |
| "What if one AI provider degrades or shuts down?" | "That's exactly why we orchestrate across multiple models. CoreeyAI routes to the optimal model per task. If one degrades, we reroute. No single point of AI failure." |
| "Pre-revenue — when do you expect first dollar?" | "SongPal beta in Q2–Q3 2026. First paid customers by Q3. Target NZD one thousand MRR by Q4 2026. The trading engine generates internal returns now — that's our bridge." |
| "Isn't seven brands too many for one person?" | "They're not seven companies — they're seven expressions of one architecture. One AI layer, one infrastructure, one codebase. The brands are interfaces, not separate businesses." |
| "What's your unfair advantage?" | "I'm the user. I trade with this engine. I make music with SongPal. I teach with MOSOKO. There is no product-market fit gap because the founder and the user are the same person." |

---

## Demo Environment Fallback

If the live VPS is unreachable during the demo:

1. **Don't panic.** Say: "The live system appears to be restarting. Let me show you the architecture and recent output instead."
2. Show pre-captured terminal screenshots (prepare these in advance)
3. Walk through the GitHub repo documentation — it's comprehensive and public
4. Show the risk.yaml and model config files from the repo
5. Emphasise: "This system runs 24/7. Today it's having a moment — like any real infrastructure. The architecture is what matters."

**Never fake a live demo.** If it's down, be honest. Judges respect infrastructure reality more than theatre.

---

*This document is current as of 2026-04-16. See [COMPETITION_PORTFOLIO.md](COMPETITION_PORTFOLIO.md) for the full written portfolio and [PITCH_DECK_OUTLINE.md](PITCH_DECK_OUTLINE.md) for slide content.*

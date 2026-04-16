# DEMO SCRIPT — Zynthio

![Status](https://img.shields.io/badge/status-competition--ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--04--16-blue)

> 3-minute live demo walkthrough for competition presentations, investor meetings, and partner showcases.

---

## Pre-Demo Setup

**Before going live, ensure:**
- [ ] VPS infrastructure accessible (104.194.156.109)
- [ ] Docker containers running and healthy
- [ ] CoreeyAI integrations active (Claude, Grok, Perplexity, Suno)
- [ ] SongPal MVP interface loaded (or wireframes if pre-alpha)
- [ ] DJ Zynrose tracks (*SIGNAL 336*, *THE MIRROR ASKED A QUESTION*) queued for playback
- [ ] ZYNTHIO_MASTER_DOCS repo open in browser (github.com/coreintentdev)
- [ ] Terminal ready for live infrastructure demo

---

## The Script

### [0:00–0:30] Opening — The Problem (30 seconds)

**SAY:**

> "If you're an independent musician today, here's your reality: you need a DAW, an AI tool, a distributor, an education platform, and a lawyer. None of them talk to each other. All of them take a cut. And none of them protect your IP.

> Zynthio fixes this. It's a sovereign AI-powered creative stack — seven brands, one system, built by a musician who codes."

**SHOW:** Ecosystem diagram (ECOSYSTEM_MAP.md rendered or slide visual)

---

### [0:30–1:15] CoreeyAI — The Intelligence Layer (45 seconds)

**SAY:**

> "Let me show you what makes this work. This is CoreeyAI — our multi-model AI orchestration layer."

**ACTION:** Open terminal. Show Docker container status.

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

**SAY:**

> "We're running live infrastructure right now. Four AI models integrated — Claude for deep reasoning, Grok for real-time analysis, Perplexity for research, and Suno for audio generation. CoreeyAI doesn't just call one API. It routes each task to the right model for the job."

**ACTION:** Demonstrate a prompt being routed through CoreeyAI — show the prompt template system and a live API response.

**SAY:**

> "This isn't a ChatGPT wrapper. It's purpose-built orchestration. Every creative task — composition, arrangement, research, generation — goes to the model best suited for it. And it's modular. If a better model drops tomorrow, we swap it in."

---

### [1:15–2:00] SongPal + DJ Zynrose — The Product in Action (45 seconds)

**SAY:**

> "CoreeyAI powers SongPal — our flagship music production platform. Let me show you what it produces."

**ACTION:** Play 15–20 seconds of *SIGNAL 336*.

**SAY (over the music):**

> "This is *SIGNAL 336* by DJ Zynrose. Written, produced, and arranged using the Zynthio stack. AI-assisted composition through CoreeyAI. Audio generation through our Suno integration. Everything created within the ecosystem."

**ACTION:** Stop playback. Show SongPal interface (MVP or wireframes).

**SAY:**

> "SongPal gives creators a single workspace — AI composition, arrangement suggestions, collaboration tools, and built-in rights management. No switching between five apps. No wondering who owns what you just made. The trademark is already filed — IPONZ number 1318588. Public beta launches Q3 this year."

---

### [2:00–2:30] MOSOKO + KERVALON — Education & IP (30 seconds)

**SAY:**

> "But creation is only half the problem. The other half is knowledge and protection."

**ACTION:** Show MOSOKO curriculum outline (brands/MOSOKO/README.md or slide).

**SAY:**

> "MOSOKO is our education arm — teaching the full pipeline from AI-assisted production to release strategy to IP basics. First cohort launches Q3 2026, 20 to 50 students."

**ACTION:** Show KERVALON overview and SongPal TM filing status.

**SAY:**

> "And KERVALON handles legal infrastructure. Every brand is trademarked or in the filing pipeline. Eventually, we'll offer IP management as a service to independent artists. Because if you can't protect what you create, creation is just content for someone else's platform."

---

### [2:30–3:00] The Close — Why This Matters (30 seconds)

**SAY:**

> "Let me be direct about where we are. We're pre-revenue. Bootstrapped. Solo founder. But here's what's real:"

**ACTION:** Show the traction summary (terminal or slide):

> "Live infrastructure. Four AI models integrated. Trademark filed. Company incorporating in New Zealand. Original music produced and ready for deployment. Open source code published. And a documentation system that most Series B companies wish they had."

**SAY:**

> "Zynthio is a $9.5 billion market opportunity built by someone who is simultaneously the developer, the musician, and the first user. We're not pitching a deck — we're showing a system.

> We're raising NZD $150 to $250K to take SongPal from alpha to public beta and bring on our first team members. The architecture is built. We need capital to go from infrastructure to market.

> No filler. All signal. I'm Corey McIvor. This is Zynthio."

---

## Post-Demo Notes

### Anticipated Questions & Responses

**Q: "How do you plan to scale as a solo founder?"**
> "The architecture is designed for it. Each brand has clear boundaries and interfaces. The first hires will be a frontend developer for SongPal and a curriculum designer for MOSOKO. The system doesn't need a team of 50 — it needs 3–5 people who understand the vision. I've built it solo precisely so I could hire into defined roles, not into ambiguity."

**Q: "What's your defensibility against bigger players?"**
> "Three things. First, vertical integration — nobody else offers production plus education plus IP protection in one stack. Second, NZ jurisdiction with active IP filings. Third, open source. Our community can audit and extend the platform. Trust is the moat. Big players can't copy trust."

**Q: "Why New Zealand?"**
> "Strong IP law, political stability, favourable startup tax treatment, and increasingly progressive AI regulation. Plus I'm a Kiwi. The company should be domiciled where the founder has legal standing and where the jurisdiction matches the values."

**Q: "Pre-revenue — when do you expect first revenue?"**
> "Q3–Q4 2026. SongPal paid tier and MOSOKO's first cohort are both targeted for Q3. We're targeting NZD $1,000+ MRR by Q4 2026. Modest but real."

**Q: "What if a major platform (Spotify, Apple) builds this?"**
> "They won't. Major platforms are extractive by design — their business model requires taking a percentage of creator revenue. Zynthio's model is the opposite: sovereign infrastructure where the creator owns the output. You can't retrofit sovereignty onto an extraction machine."

---

## Timing Summary

| Segment | Duration | Cumulative |
|---------|----------|------------|
| Opening — The Problem | 0:30 | 0:30 |
| CoreeyAI — Intelligence Layer | 0:45 | 1:15 |
| SongPal + DJ Zynrose — Product | 0:45 | 2:00 |
| MOSOKO + KERVALON — Education & IP | 0:30 | 2:30 |
| The Close — Why This Matters | 0:30 | 3:00 |

**Total: 3:00**

---

## Adaptation Notes

| Context | Adjustment |
|---------|-----------|
| **5-minute slot** | Extend CoreeyAI demo (live API call), add business model slide between sections |
| **10-minute slot** | Full pitch deck presentation with demo embedded at midpoint |
| **Music tech competition** | Lead with DJ Zynrose playback, extend SongPal section, de-emphasise trading bot |
| **AI competition** | Lead with CoreeyAI architecture, show model routing live, de-emphasise music playback |
| **Startup competition** | Lead with market size, emphasise business model and traction, keep demo shorter |
| **Virtual/recorded** | Pre-record screen captures, overlay narration, include music throughout |

---

*This demo script is current as of 2026-04-16. Adjust content based on product development status at time of presentation.*

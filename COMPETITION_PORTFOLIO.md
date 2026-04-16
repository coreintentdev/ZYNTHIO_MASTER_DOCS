# COMPETITION PORTFOLIO — Zynthio

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--04--16-blue) ![Stage](https://img.shields.io/badge/stage-pre--seed-yellow) ![Jurisdiction](https://img.shields.io/badge/jurisdiction-New%20Zealand-black)

> Full competition portfolio for global AI, fintech, music technology, and startup competitions.

---

## Executive Summary

Zynthio is a sovereign AI ecosystem — seven brands delivering multi-model AI orchestration, autonomous algorithmic trading, music production, and creator education under one stack. Built by a solo NZ/AU founder-engineer-producer, incorporating in New Zealand May 2026, with live infrastructure and a ~$9.5B addressable market. Not a feature. A stack.

---

## Problem Statement

### AI-powered trading and creation are broken in three ways:

**1. AI trading is opaque.**
Retail traders face algorithmic systems they cannot see, understand, or audit. Institutional players gatekeep the best models. The average retail participant is trading against black boxes — paying subscription fees for signal services with no accountability and no transparency into how decisions are made.

**2. AI trading is expensive and gatekept.**
Sophisticated multi-model AI orchestration — the kind that routes between reasoning engines, research systems, and market analysis in real time — is available to hedge funds and prop desks. Independent traders and small teams are locked out by infrastructure costs, API complexity, and the engineering talent required to build these systems.

**3. AI creative tools are extractive.**
Beyond trading, the same pattern repeats in creative industries. AI music platforms capture value from creators — expensive subscriptions, opaque models, IP-hostile terms. Education is disconnected from real tools. IP protection is inaccessible to independents. The full pipeline from creation to ownership is broken.

**The result:** Whether you're an independent trader or an independent artist, you're fragmented across disconnected, extractive platforms — paying more, owning less, and building on systems that don't serve you.

---

## The Solution

### CoreIntent + Zynthio: Open, competition-based, multi-AI orchestration.

**CoreIntent** is the engineering force behind Zynthio — a development studio that builds sovereign AI infrastructure for trading, creative production, and education. The core innovation is **multi-model AI orchestration**: routing tasks to the right AI engine for each job, not locking into a single vendor.

**The competition model:** CoreIntent's gTrade doesn't sell signals or charge subscriptions. It operates an autonomous, risk-managed trading bot that competes in the market. Performance is the product. Results are transparent. This is the opposite of the subscription-signal model that dominates retail trading.

**The sovereign stack:** Seven brands, one architecture:

| Brand | Function | Status |
|-------|----------|--------|
| **COREINTENT** | Dev studio — engineering all systems + gTrade autonomous trading | **Live** |
| **CoreeyAI** | Multi-model AI orchestration (Claude, Grok, Perplexity, Suno) | **Live** |
| **SongPal** | AI-powered music production platform | In development — TM filed (IPONZ #1318588) |
| **MOSOKO** | Education — cohort programmes and self-paced courses | Curriculum in development |
| **KERVALON** | Legal and IP protection arm | Active |
| **DJ Zynrose** | Artist persona — living proof of concept | Active — 2 tracks written |
| **ZYNTHIO** | Parent company — governance, partnerships, market-facing | Incorporating May 2026 |

### What makes this different:

- **Open architecture** — multi-model AI, no vendor lock-in, public documentation
- **Competition model** — gTrade competes on performance, not subscriptions. No signal-selling.
- **Sovereign infrastructure** — own servers, own deployment, own data. Not renting from AWS/GCP.
- **Closed-loop ecosystem** — Build (COREINTENT) → Think (CoreeyAI) → Create (SongPal) → Teach (MOSOKO) → Protect (KERVALON) → Scale (ZYNTHIO)
- **Self-funding** — gTrade autonomously funds development. Not dependent on venture capital to survive.

---

## Market Opportunity

| Segment | Market Size (2025) | Growth |
|---------|-------------------|--------|
| Global music production software | $5.9B | ~8% YoY |
| AI music generation | $1.5B | ~25% YoY |
| Online music education | $2.1B | ~10% YoY |
| Global retail trading platforms | $12.1B | ~6% YoY |
| AI-assisted investing tools | $3.8B | ~20% YoY |
| **Total Addressable Market** | **~$9.5B** (creative stack) | |
| **Extended TAM** (incl. trading) | **~$25.4B** | |

### Why now:

- Generative AI has collapsed costs in both trading and music creation — the bottleneck is now **curation, orchestration, and infrastructure**
- Multi-model AI orchestration is technically feasible but no one is packaging it for independents
- Retail trading volume is at all-time highs but tools have not caught up
- Independent creators are the fastest-growing segment of the music industry
- NZ/AU tech ecosystems are underserved by global AI tools built for US/EU markets

---

## Founder

### Corey McIvor

| Field | Detail |
|-------|--------|
| Citizenship | New Zealand / Australia (dual) |
| Current location | Managua, Nicaragua (operating globally) |
| Role | Sole founder — architecture, code, brand, and music |
| Technical | Full-stack developer, AI engineer — Next.js, Python, Docker, multi-model AI |
| Creative | Independent music producer (DJ Zynrose) — electronic / experimental / ambient |
| GitHub | [coreintentdev](https://github.com/coreintentdev) |

**Why one founder matters:** Corey built the entire stack — the AI orchestration, the trading engine, the production infrastructure, the brand architecture, the documentation, the music, and the legal filings. This is not a pitch deck looking for an engineer. The engineer is the founder.

**Director qualification:** NZ/AU citizen — qualifies as eligible director under NZ Companies Act 1993 s 10(2A), regardless of physical location.

---

## Technical Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                    EXTERNAL AI SERVICES                        │
│  Claude (Anthropic)  │  Grok (xAI)  │  Perplexity  │  Suno   │
└───────────────────┬────────────────────────────────────────────┘
                    │ (consumed via)
┌───────────────────▼────────────────────────────────────────────┐
│                       CoreeyAI                                 │
│     Multi-model orchestration · Prompt routing · Agentic flows │
└──────────┬────────────────────────────┬───────────────────────┘
           │                            │
┌──────────▼──────────┐     ┌───────────▼────────────────────────┐
│       SongPal       │     │             MOSOKO                  │
│  AI music platform  │     │   Adaptive learning engine          │
│    (Next.js UI)     │     │     (Next.js frontend)              │
└─────────────────────┘     └────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│                    COREINTENT INFRASTRUCTURE                   │
│   Next.js · Python 3.11 · Docker · VPS · GitHub CI            │
│   gTrade (autonomous trading) · Perplexity Orb · Master Docs  │
└────────────────────────────────────────────────────────────────┘
```

| Layer | Technologies |
|-------|-------------|
| Frontend | Next.js (React), TypeScript |
| Backend / AI | Python 3.11, multi-model API orchestration |
| AI services | Claude API, Grok API, Perplexity, Suno API |
| Infrastructure | Docker, Docker Compose, sovereign VPS |
| Version control | Git / GitHub ([coreintentdev](https://github.com/coreintentdev)) |
| Agentic systems | Perplexity Orb — session management, multi-step workflows |
| Trading engine | gTrade — risk-managed autonomous bot (BTC, ETH, SOL, XAU, XAG) |
| Config | YAML, .env |
| Monitoring | JSON logging, health checks |

### Key architectural decisions:

- **Multi-model AI** — no single-vendor lock-in. CoreeyAI routes to the best model per task: Claude for reasoning, Grok for real-time market sentiment, Perplexity for research, Suno for audio generation.
- **Next.js frontend** — modern, performant UI layer for SongPal and MOSOKO. Server-side rendering, edge-ready.
- **Sovereign infrastructure** — own VPS, own deployment pipeline, own data. Not renting someone else's cloud.
- **Open documentation** — ZYNTHIO_MASTER_DOCS is public on GitHub. Transparency as a feature, not a liability.

---

## Competitive Advantages

### 1. Competition Model vs. Subscription

gTrade operates on a **performance-based competition model** — autonomous, risk-managed algorithmic trading that funds development. This is fundamentally different from the subscription-signal model. There are no monthly fees for signals of questionable quality. The bot competes in the market and the results speak for themselves. Max leverage 5.0x. 1% max risk per trade. 0.8% daily loss ceiling. Disciplined, transparent, auditable.

### 2. NZ Jurisdiction

- Incorporating under NZ Companies Act 1993 — strong, transparent corporate governance
- IPONZ trademark protection (SongPal #1318588)
- NZ's export education and tech incentive frameworks align with MOSOKO and SongPal
- Founder holds NZ/AU dual citizenship — deep jurisdictional alignment, not a flag-of-convenience incorporation

### 3. Open Architecture

- **Public documentation** — [ZYNTHIO_MASTER_DOCS](https://github.com/coreintentdev/zynthio_master_docs) is open on GitHub
- **Multi-model AI** — no vendor lock-in. Switch or add models without rewriting the stack.
- **Creator sovereignty** — users own 100% of their output. No extraction, no IP capture.
- **MIT-licensed codebase** — open by default

### 4. Vertical Integration

No competitor combines AI orchestration + autonomous trading + music production + education + IP protection + an artist persona under one sovereign architecture.

| Competitor | What They Do | What Zynthio Does Differently |
|------------|-------------|-------------------------------|
| Suno / Udio | AI music generation | Integrates generation *within* a full creator stack |
| Splice | Sample library & collaboration | AI-native, sovereignty-focused — creators own output |
| Berklee Online | Music education | MOSOKO teaches *this specific stack* — tools are live products |
| LANDR | AI mastering & distribution | Full pipeline: creation → education → legal → distribution |
| Signal-selling bots | Subscription signals | gTrade competes on performance — no subscriptions, no signal-selling |
| Generic AI APIs | Raw model access | Zynthio is the *application layer* — purpose-built, not generic |

---

## Traction Metrics

*As of April 2026 — honest, early-stage, all verified:*

### Live & Operational

- **Production infrastructure:** Sovereign VPS — Docker, Python 3.11, deployment pipeline running
- **AI integrations:** Claude, Grok, Perplexity all active and wired into CoreeyAI
- **gTrade autonomous trading bot:** Live and operating — self-funding development
- **Perplexity Orb:** Agentic session management deployed and operational
- **ZYNTHIO_MASTER_DOCS:** 7-brand architecture fully documented, public on GitHub
- **Domain secured:** zynthio.ai — active

### Filed & In Process

- **Trademark filed:** SongPal — IPONZ #1318588 (awaiting examination)
- **Company name reserved:** ZYNTHIO LIMITED — NZCO #15436626 (incorporating before May 12, 2026)

### In Development

- **SongPal platform:** Next.js MVP build underway — target beta Q2–Q3 2026
- **MOSOKO curriculum:** First cohort target Q3 2026
- **Original music:** *SIGNAL 336* and *THE MIRROR ASKED A QUESTION* written, 4-platform deployment pipeline in progress
- **19 multilingual avatar scripts** across 6 languages (EN, ES, FR, PT, ZH, MI)

### What we don't have yet (and we're honest about it):

- No paying customers (pre-revenue — SaaS launch target Q4 2026)
- No external funding raised (bootstrapped + gTrade self-funding)
- Solo founder (no team hires yet)
- SongPal beta not yet launched
- No streaming platform presence for DJ Zynrose (deployment pending)

We're early. The architecture is real. The infrastructure is running. The honesty is deliberate.

---

## Financial Projections

*All figures NZD. Conservative estimates.*

| Year | Projected Revenue | Key Driver |
|------|------------------|------------|
| 2026 (H2) | ~$26,550 | MOSOKO pilot cohort + SongPal early adopters |
| 2027 | ~$318,875 | SongPal growth + MOSOKO cohorts + CoreeyAI API |
| 2028 | ~$969,000 | SongPal scale + MOSOKO maturity + API licensing |
| **3-Year Total** | **~$1,314,425** | |

### Unit Economics (SongPal)

| Metric | Target |
|--------|--------|
| ARPU | NZD $20–30/month |
| Free → paid conversion | 10–15% |
| CAC | NZD $30–50 |
| 12-month LTV | NZD $240–360 |
| LTV:CAC ratio | 6–8x |

### Funding Ask

| Stage | Amount (NZD) | Use |
|-------|-------------|-----|
| Pre-seed | $150,000–250,000 | SongPal MVP (35%), MOSOKO curriculum (20%), marketing (20%), legal/IP (10%), infra (5%), reserve (10%) |
| Series A (2027+) | $1,000,000–2,500,000 | Team hire, international expansion, SongPal scale |

**Current monthly burn:** ~NZD $280–480. At $150K raise, runway = 20–35 months to MRR breakeven.

-> Full details: [FINANCIAL_MODEL.md](FINANCIAL_MODEL.md)

---

## The Ask — By Competition Type

| Competition Type | What We're Seeking |
|-----------------|--------------------|
| **Startup competition** | Seed capital / accelerator access — target NZD $150–250K |
| **AI competition** | Recognition, partnerships, API credits, multi-model orchestration validation |
| **Fintech / trading** | Recognition for gTrade's autonomous, competition-based trading architecture |
| **Music / creative tech** | Industry exposure, label/distributor introductions, SongPal partnerships |
| **Education** | MOSOKO curriculum partnerships, institutional pilot programmes |

---

## Contact

**Corey McIvor** — Founder, ZYNTHIO
GitHub: [github.com/coreintentdev](https://github.com/coreintentdev)
Domain: [zynthio.ai](https://zynthio.ai)
Email: *(add contact email before submitting)*

---

## Supporting Documents

| Document | Purpose |
|----------|---------|
| [PITCH_DECK_OUTLINE.md](PITCH_DECK_OUTLINE.md) | 10-slide pitch deck structure |
| [DEMO_SCRIPT.md](DEMO_SCRIPT.md) | 3-minute live demo walkthrough |
| [PRESS_KIT.md](PRESS_KIT.md) | Brand story, founder bio, key quotes, brand colours |
| [AWARDS_TRACKER.md](AWARDS_TRACKER.md) | 2026 competition targets and deadlines |
| [COMPETITION_ENTRY.md](COMPETITION_ENTRY.md) | One-page summary and 30-second spoken pitch |
| [FINANCIAL_MODEL.md](FINANCIAL_MODEL.md) | 3-year revenue projections |
| [ECOSYSTEM_MAP.md](ECOSYSTEM_MAP.md) | Full brand architecture |
| [NZ_COMPLIANCE.md](NZ_COMPLIANCE.md) | Incorporation and IP tracker |

---

*Last updated: 2026-04-16 | Maintained by: Corey McIvor / COREINTENT*

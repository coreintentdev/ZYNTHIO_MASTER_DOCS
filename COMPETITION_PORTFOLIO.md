# COMPETITION PORTFOLIO — Zynthio / CoreIntent

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--04--16-blue) ![Stage](https://img.shields.io/badge/stage-pre--seed-orange)

> Full competition entry portfolio for AI, fintech, music tech, and startup competitions worldwide.

---

## Executive Summary

Zynthio is a sovereign AI ecosystem built in New Zealand — seven brands, one stack, zero filler. CoreIntent, the engineering studio, deploys multi-model AI orchestration across trading, music production, and education, using a competition-based model that aligns performance with profit instead of locking users into subscriptions.

---

## Problem Statement

### AI trading is broken for everyone except institutions.

The $12B+ retail trading technology market is dominated by platforms that are:

- **Opaque** — black-box algorithms with no transparency into decision logic, risk models, or performance attribution. Retail traders are told to trust systems they cannot inspect.
- **Expensive** — subscription fees, data fees, platform fees, and spread markups stack up before a single trade is placed. The house wins regardless of user outcomes.
- **Gatekept** — institutional-grade AI, multi-model orchestration, and risk management infrastructure remain locked behind six-figure minimums and proprietary walls.
- **Misaligned** — platforms profit from subscriptions and trade volume, not from user success. The incentive is engagement, not performance.

The same pattern is emerging in AI-assisted music production and creative tools: extractive pricing, opaque models, and zero creator ownership.

**The result:** Independent traders and creators subsidise platforms that don't share their risk, don't protect their IP, and don't align with their outcomes.

---

## The Solution

### CoreIntent: Open architecture. Competition-based. Multi-AI orchestration.

CoreIntent is the engineering studio behind the Zynthio ecosystem. It builds AI-powered systems where **performance is the product** — not subscriptions, not lock-in, not data harvesting.

### Core Innovation: Competition-Based Model

Unlike subscription platforms that profit regardless of user outcomes, CoreIntent's trading engine operates on a **competition-based model**:

- The system profits when it performs — full alignment between platform and user
- No subscription fees as the primary revenue driver
- Transparent risk management with hard-coded safety rails
- Open architecture — users can inspect the logic, not just the output

### Multi-AI Orchestration Layer (CoreeyAI)

CoreIntent doesn't rely on a single AI model. The CoreeyAI layer orchestrates multiple best-in-class models, routing tasks to the optimal engine:

| Model | Role | Status |
|-------|------|--------|
| Claude (Anthropic) | Primary reasoning, long-context analysis | Active |
| Grok (xAI) | Real-time trend analysis, market data | Active |
| Perplexity | Research, knowledge retrieval, verification | Active |
| Suno API | Audio generation (SongPal vertical) | Partial |

This isn't wrapper code around a single API. It's purpose-built orchestration: each task is routed to the model best suited for it, with context management and session persistence across workflows.

### The Sovereign Stack

CoreIntent operates within the Zynthio ecosystem — seven brands, one architecture:

| Brand | Function | Status |
|-------|----------|--------|
| **CoreIntent** | Engineering studio & autonomous trading engine | Active |
| **CoreeyAI** | Multi-model AI orchestration layer | Active |
| **SongPal** | AI music production platform (TM: IPONZ #1318588) | In development |
| **MOSOKO** | Education — teaching the full creator/trader pipeline | In development |
| **KERVALON** | Legal, IP & compliance infrastructure | Active |
| **DJ Zynrose** | Music artist — living proof of concept | Active |
| **ZYNTHIO** | Parent company — NZ jurisdiction, sovereign governance | Incorporating |

---

## Market Opportunity

### Primary: Global Retail Trading & AI-Assisted Investing

| Segment | Market Size | Growth |
|---------|-------------|--------|
| Global retail trading platforms | $12.1B (2025) | ~9% CAGR |
| AI in fintech / algorithmic trading | $4.2B (2025) | ~23% CAGR |
| Robo-advisory & AI-assisted investing | $2.8B (2025) | ~18% CAGR |
| **Addressable market** | **~$19B** | |

### Secondary: Creative AI & Music Tech

| Segment | Market Size | Growth |
|---------|-------------|--------|
| Global music production software | $5.9B (2025) | ~8% YoY |
| AI music generation | $1.5B (2025) | ~25% YoY |
| Online music education | $2.1B (2025) | — |
| **Secondary TAM** | **~$9.5B** | |

### Why These Markets Converge

CoreIntent's multi-model AI orchestration is **domain-agnostic infrastructure**. The same architecture that routes trading decisions across models also powers music composition, education delivery, and creative workflows. One engine, multiple verticals.

---

## Team

### Corey McIvor — Founder

| | |
|---|---|
| **Role** | Sole founder — architect, engineer, producer, strategist |
| **Citizenship** | New Zealand / Australia (dual) |
| **Location** | Managua, Nicaragua (low burn rate, global perspective) |
| **Technical** | Full-stack developer, AI engineer, DevOps (Python, Docker, multi-model AI) |
| **Creative** | Independent music producer (DJ Zynrose) — uses the tools he builds |
| **GitHub** | [coreintentdev](https://github.com/coreintentdev) |

### Why Solo Founder Is a Strength (Not a Liability)

- **Zero communication overhead** — every decision, every line of code, every strategic pivot is coherent
- **Full-stack capability** — no dependency on hiring for core engineering, AI integration, or product design
- **Creator-engineer alignment** — Corey is both the builder and the user. SongPal is built by a musician. The trading engine is built by a trader. No product-market gap.
- **Low burn rate** — Nicaragua-based operations mean runway stretches further than any SF or London competitor
- **NZ/AU citizenship** — satisfies NZ Companies Act director residency requirements regardless of physical location

---

## Technical Architecture

### Stack Overview

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend (planned) | Next.js | Dashboard, trading UI, SongPal interface |
| Backend | Python 3.11 | Core logic, AI orchestration, trading engine |
| AI Layer | CoreeyAI (Claude, Grok, Perplexity, Suno) | Multi-model task routing |
| Infrastructure | Docker, Docker Compose | Containerised deployment |
| Hosting | Sovereign VPS (104.194.156.109) | No cloud vendor lock-in |
| OS | Ubuntu 22.04 | Production server |
| Monitoring | JSON logging, health checks (60s intervals) | System observability |
| Config | YAML, .env | Risk parameters, API keys |
| Version Control | Git / GitHub | Open-source documentation |

### Trading Engine (gTrade) Architecture

```
┌─────────────────────────────────────────────────┐
│              CoreeyAI Orchestration              │
│   Claude (reasoning) + Grok (real-time data)     │
│         + Perplexity (research/verify)           │
└──────────────────────┬──────────────────────────┘
                       │
              ┌────────▼────────┐
              │   gTrade Engine  │
              │  Risk Management │
              │  Position Sizing │
              │  Entry/Exit Logic│
              └────────┬────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
    ┌────▼───┐   ┌────▼───┐   ┌────▼───┐
    │BTC-PERP│   │ETH-PERP│   │XAU-PERP│
    │SOL-PERP│   │XAG-PERP│   │  ...   │
    └────────┘   └────────┘   └────────┘
```

### Risk Management Parameters

| Parameter | Value |
|-----------|-------|
| Max leverage | 5.0x |
| Max risk per trade | 1.0% |
| Max daily loss | 0.8% |
| Min cash reserve | $350 USD |
| Max open positions | 10 |
| Assets | BTC-PERP, ETH-PERP, SOL-PERP, XAU-PERP, XAG-PERP |

### Sovereign Infrastructure

No AWS. No GCP. No Azure. CoreIntent runs on its own VPS with Docker orchestration — full control over the pipeline, no third-party data exposure, no vendor lock-in. This is a deliberate architectural choice: when you build trading and creative AI systems, sovereignty over infrastructure isn't paranoia — it's engineering discipline.

---

## Competitive Advantages

### 1. Competition Model vs Subscription

| Traditional Platform | CoreIntent |
|---------------------|------------|
| Profits from subscriptions regardless of performance | Profits when the system performs |
| Misaligned incentives — more users = more revenue | Aligned incentives — better performance = more revenue |
| Users pay whether they win or lose | Skin in the game |

### 2. Multi-Model AI (Not Single-Vendor Lock-In)

Most AI trading platforms are wrappers around a single LLM. CoreeyAI orchestrates across Claude, Grok, and Perplexity — routing each task to the optimal model. If one provider degrades, the system adapts. No single point of AI failure.

### 3. New Zealand Jurisdiction

- Strong IP protection via IPONZ (trademark #1318588 already filed)
- NZ Companies Act 1993 — clean, modern corporate law
- Privacy-forward regulatory environment
- Not subject to US PATRIOT Act data access provisions
- Founder holds NZ/AU dual citizenship — genuine local connection, not a flag-of-convenience

### 4. Open Architecture

- Public GitHub repositories — inspectable, not just auditable
- Documentation-first culture (this entire ecosystem is documented in the open)
- Open-source tooling under MIT License
- No proprietary black boxes — users can understand what the system does and why

### 5. Vertically Integrated Moat

No competitor combines AI trading + music production + education + IP infrastructure under one sovereign architecture. This isn't feature sprawl — it's a shared AI layer (CoreeyAI) powering multiple verticals with one engineering investment.

---

## Traction Metrics

> We are early-stage and pre-revenue. Here is what is real today.

### Built & Deployed

| Milestone | Status | Evidence |
|-----------|--------|----------|
| gTrade autonomous trading engine | Live on VPS | Docker deployment, health-checked |
| CoreeyAI multi-model orchestration | Active | Claude, Grok, Perplexity integrations operational |
| Perplexity Orb (agentic AI sessions) | Deployed | Session persistence architecture running |
| Production infrastructure | Live | VPS 104.194.156.109, Ubuntu 22.04, Docker |
| ZYNTHIO_MASTER_DOCS | Published | [github.com/coreintentdev](https://github.com/coreintentdev) |

### Legal & IP

| Milestone | Status | Reference |
|-----------|--------|-----------|
| SongPal trademark | Filed | IPONZ #1318588 |
| ZYNTHIO LIMITED name reservation | Active | NZ Companies Office #15436626 |
| Incorporation | In progress | Deadline: May 12, 2026 |
| Brand architecture documented | Complete | 7 brands, full IP strategy |

### Creative Output

| Milestone | Status |
|-----------|--------|
| Original tracks written | *SIGNAL 336*, *THE MIRROR ASKED A QUESTION* |
| 4-way deploy pipeline designed | Production → Streaming → Social → Education |
| DJ Zynrose artist identity | Active |

### What We Haven't Done Yet (Honestly)

- No paying customers yet — SongPal is pre-beta
- No external revenue — trading bot operates internally
- No employees — solo founder
- No formal API specification for CoreeyAI (needed for B2B licensing)
- No CI/CD pipeline — deployments are manual
- Suno API integration is partial, not full production
- Google Drive and Slack connectors are inactive

**We are building in public, with real infrastructure, real IP filings, and real code. We are not pretending to be further along than we are.**

---

## Revenue Model

| Stream | Brand | Mechanism | Timeline |
|--------|-------|-----------|----------|
| Competition-based trading | CoreIntent / gTrade | Performance-aligned returns | Active (internal) |
| SaaS subscriptions | SongPal | Free / Creator / Studio tiers | Q2–Q3 2026 |
| Course revenue | MOSOKO | Cohort & self-paced programmes | Q3 2026 |
| B2B API licensing | CoreeyAI | Per-call or monthly API access | Q4 2026 |
| IP services | KERVALON | Consulting, TM filing, contract review | Q4 2026+ |

**Target:** NZD $1,000+ MRR by Q4 2026 (SongPal)

**Seed ask:** NZD $150,000–$250,000 — accelerate SongPal to beta, complete incorporation, launch first MOSOKO cohort.

---

## Roadmap

### Q2 2026 (Now)
- Complete ZYNTHIO LIMITED incorporation (deadline: May 12, 2026)
- SongPal public beta launch
- Full Suno API integration
- First music releases: *SIGNAL 336*, *THE MIRROR ASKED A QUESTION*
- Establish CI/CD pipeline

### Q3 2026
- ZYNTHIO.ai website public launch
- SongPal paid tiers live
- MOSOKO first cohort (target: 20–50 students)
- Additional TM filings (ZYNTHIO, CoreeyAI)
- Seed funding raise

### Q4 2026
- CoreeyAI B2B API — first external licensee
- DJ Zynrose first EP release
- 100 MOSOKO students enrolled
- SongPal MRR target: NZD $1,000+
- KERVALON external IP services launch

### 2027 Vision
- SongPal at 1,000+ active users
- CoreeyAI licensed to 3+ external platforms
- DJ Zynrose at 10,000+ monthly listeners
- Series A positioning

---

## Contact

**Corey McIvor** — Founder, ZYNTHIO
GitHub: [github.com/coreintentdev](https://github.com/coreintentdev)
Domain: [zynthio.ai](https://zynthio.ai)
Email: *(add contact email before submission)*

---

> *Velvet knife. Sovereign. No filler. All signal.*

*This document is current as of 2026-04-16. For detailed status see [ECOSYSTEM_MAP.md](ECOSYSTEM_MAP.md), [NZ_COMPLIANCE.md](NZ_COMPLIANCE.md), and [COMPETITION_ENTRY.md](COMPETITION_ENTRY.md).*

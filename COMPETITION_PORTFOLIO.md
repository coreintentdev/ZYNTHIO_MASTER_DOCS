# COMPETITION PORTFOLIO — Zynthio

![Status](https://img.shields.io/badge/status-submission--ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--05--08-blue) ![Stage](https://img.shields.io/badge/stage-pre--seed-yellow) ![Jurisdiction](https://img.shields.io/badge/jurisdiction-New%20Zealand-black)

> Full competition portfolio for startup, AI, fintech, and music technology competitions worldwide.
> Every claim is verifiable. Every metric is honest. Adapt per competition format.

---

## Executive Summary

Zynthio is a sovereign AI ecosystem — seven brands delivering music production, multi-model orchestration, autonomous trading, education, and IP protection under one architecture. Built by a solo NZ/AU founder-engineer-producer, with live infrastructure, a filed trademark, and a ~$21B combined addressable market. Early stage, real stack, global ambition.

*(50 words)*

---

## Problem Statement

### The creative economy and AI trading are both structurally broken.

**1. AI tools extract — they don't empower.**
Generative AI has collapsed the cost of music production. But the platforms capturing that value give nothing back. Independent creators produce; platforms profit. Terms are opaque, IP ownership is hostile, and lock-in is the business model.

**2. AI-assisted trading is opaque, expensive, and gatekept.**
Institutional-grade algorithmic trading is inaccessible to retail traders and independent builders. What's available to them: subscription signal services selling black-box calls with no accountability, no open architecture, and no verifiable track record. Performance claims are unauditable.

**3. Education is disconnected from real tools.**
Music education platforms teach theory and legacy workflows. None of them teach the actual AI tools reshaping the industry — because those platforms don't build tools. The knowledge gap widens every quarter.

**4. IP infrastructure is inaccessible.**
Trademark filings, licensing agreements, and copyright strategy remain locked behind expensive legal gatekeepers. Independent artists can create at scale, but they cannot protect at scale.

**The result:** Creators and traders are fragmented across disconnected, extractive tools. They pay more, own less, and build on platforms that don't serve them. The post-AI economy needs new infrastructure — not new wrappers.

---

## The Solution

### Zynthio: One sovereign stack. Seven brands. Full pipeline.

Zynthio solves the fragmentation problem by combining AI production, education, IP protection, autonomous funding, and artist output under one coherent, vertically integrated architecture.

| Brand | Function | Status |
|-------|----------|--------|
| **ZYNTHIO** | Parent company — governance, partnerships, market-facing | Incorporating May 2026 |
| **CoreIntent** | Dev studio + autonomous trading engine (gTrade) — open, competition-based, multi-AI orchestration | **Live** |
| **SongPal** | AI-powered music production & collaboration platform | In development — TM filed (IPONZ #1318588) |
| **CoreeyAI** | Multi-model AI orchestration layer (Claude, Grok, Perplexity, Suno) | **Live** |
| **MOSOKO** | Music education — cohort programmes & self-paced courses | Curriculum in development |
| **KERVALON** | Legal & IP management arm | Active |
| **DJ Zynrose** | Artist persona — living proof of concept, community builder | Active — 2 tracks written |

### What makes Zynthio different:

- **Sovereign architecture** — creators own 100% of their output. No extraction. No platform lock-in.
- **Multi-AI orchestration** — CoreeyAI routes tasks across Claude, Grok, Perplexity, and Suno. Not a wrapper — purpose-built routing for optimal model selection per task.
- **Competition model over subscription** — CoreIntent's gTrade operates on performance-based, competition-style algorithmic trading. No black boxes. No monthly fees for signals. Open architecture, verifiable risk parameters. Performance is the product.
- **Closed-loop ecosystem** — Build (CoreIntent) → Think (CoreeyAI) → Create (SongPal + DJ Zynrose) → Teach (MOSOKO) → Protect (KERVALON) → Scale (ZYNTHIO).
- **Self-funding mechanism** — gTrade autonomous trading bot provides internal development funding without external dependency.

---

## Market Opportunity

| Segment | Market Size (2025) | Growth |
|---------|-------------------|--------|
| Global music production software | $5.9B | ~8% YoY |
| AI music generation | $1.5B | ~25% YoY |
| Online music education | $2.1B | ~10% YoY |
| Global retail trading (AI-assisted) | $12.0B+ | ~18% YoY |
| **Combined Addressable Market** | **~$21.5B+** | |

*Primary TAM (creator stack): ~$9.5B. Extended TAM (AI-assisted retail trading via gTrade): ~$12B+.*

### Why now:

1. Generative AI has collapsed the cost of music creation — the bottleneck is now **curation, pedagogy, and IP infrastructure**
2. AI-assisted investing is shifting from institutional to retail — the subscription signal model is ripe for disruption by open, competition-based alternatives
3. No competitor offers a vertically integrated creator stack — the market is fragmented by design
4. Independent creators are the fastest-growing segment of the music industry
5. NZ/AU tech ecosystems are underserved by global AI tools built for US/EU markets

---

## Team

### Corey McIvor — Founder

| Field | Detail |
|-------|--------|
| Citizenship | New Zealand / Australia (dual) |
| Location | Managua, Nicaragua (operating globally) |
| Role | Sole founder — architecture, code, brand, and music |
| Technical | Full-stack developer, AI engineer — Next.js, Python, Docker, CI/CD, multi-model AI orchestration |
| Creative | Independent music producer (DJ Zynrose) — electronic, experimental, ambient |
| GitHub | [coreintentdev](https://github.com/coreintentdev) |
| Director status | NZ/AU citizen — qualifies as eligible director under NZ Companies Act 1993 s 10(2A) |

**Why one founder matters:**

Corey built the entire stack — the AI integrations, the production infrastructure, the brand architecture, the documentation, the music, and the legal filings. This is not a pitch deck looking for an engineer. The engineer is the founder. The person building the tools is the person using them every day to make music. That is alignment no hired team can replicate at this stage.

**Solo by design, not by limitation.** At pre-seed, a single technical founder with full-stack capability and low burn is an advantage. The plan: hire post-funding against the architecture that already exists, not build the architecture after raising.

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
│     Model orchestration · Prompt engineering · Agentic flows   │
│     Multi-model routing · Task-specific model selection        │
└──────────┬────────────────────────────┬───────────────────────┘
           │                            │
┌──────────▼──────────┐     ┌───────────▼────────────────────────┐
│       SongPal       │     │             MOSOKO                  │
│  Next.js frontend   │     │   Adaptive learning engine          │
│  AI music platform  │     │   Cohort + self-paced curriculum    │
└─────────────────────┘     └────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│                 COREINTENT INFRASTRUCTURE                      │
│  Next.js · Python 3.11 · Docker · VPS (sovereign) · GitHub CI │
│  gTrade (autonomous trading) · Perplexity Orb · Master Docs   │
└────────────────────────────────────────────────────────────────┘
```

| Layer | Technologies |
|-------|-------------|
| Frontend | Next.js (React), TypeScript |
| Backend / AI orchestration | Python 3.11, Claude API, Grok API, Perplexity, Suno API |
| Infrastructure | Docker, Docker Compose, sovereign VPS (no cloud vendor lock-in) |
| Version control | Git / GitHub ([coreintentdev](https://github.com/coreintentdev)) |
| Agentic systems | Perplexity Orb — session management, multi-step AI workflows |
| Trading engine | gTrade — risk-managed autonomous bot (BTC, ETH, SOL, XAU, XAG) |
| Config & monitoring | YAML, .env, JSON logging, health checks |

### Key architectural decisions:

- **Multi-model AI** — no single-vendor lock-in. CoreeyAI routes to the best model for each task.
- **Sovereign infrastructure** — own VPS, own deployment pipeline, own data. No cloud dependency.
- **Next.js for user-facing products** — modern React framework for SongPal and MOSOKO frontends.
- **Modular brand architecture** — each brand draws from CoreeyAI for the intelligence it needs.
- **Open-source documentation** — ZYNTHIO_MASTER_DOCS is public. Transparency is a feature.

---

## Competitive Advantages

### 1. Competition Model vs. Subscription (CoreIntent / gTrade)

CoreIntent's gTrade operates on a performance-based competition model — autonomous, risk-managed algorithmic trading that funds development. This is the opposite of subscription signal services selling opaque calls behind paywalls.

**gTrade risk parameters (all verifiable, open architecture):**
- Max leverage: 5.0×
- Max risk per trade: 1%
- Daily loss ceiling: 0.8%
- Max open positions: 10
- Assets: BTC-PERP, ETH-PERP, SOL-PERP, XAU-PERP, XAG-PERP
- Minimum cash reserve: USD $350

Performance is the product. Open architecture means anyone can verify the risk parameters. No hidden fees. No subscription lock-in.

### 2. NZ Jurisdiction

- Incorporating under NZ Companies Act 1993 — strong corporate governance
- IPONZ trademark protection (SongPal #1318588) — real IP from day one
- NZ/AU tech and export education incentives align with SongPal and MOSOKO
- Founder holds NZ/AU dual citizenship — deep jurisdictional alignment
- NZ is a strategic home for IP-heavy, creator-focused tech — not a flag of convenience

### 3. Open Architecture

- Public documentation repository ([ZYNTHIO_MASTER_DOCS](https://github.com/coreintentdev/zynthio_master_docs))
- MIT-licensed codebase
- Multi-model AI — no vendor lock-in
- Creator sovereignty — users own 100% of their output
- Verifiable risk parameters on gTrade — no black boxes

### 4. Vertical Integration

No competitor combines AI production + education + IP infrastructure + an artist persona + autonomous trading under one sovereign architecture.

| Competitor | What They Do | What Zynthio Does Differently |
|------------|-------------|-------------------------------|
| Suno / Udio | AI music generation | Integrates generation *within* a full creator stack — education, IP, distribution |
| Splice | Sample library & collaboration | AI-native, sovereignty-focused — creators own output |
| Berklee Online | Music education | MOSOKO teaches *this specific stack* — tools are live products, not theory |
| LANDR | AI mastering & distribution | Full pipeline: creation → education → legal → distribution |
| Signal subscription services | Black-box trading calls | gTrade: open architecture, competition model, verifiable risk |

---

## Traction Metrics

*As of May 2026 — honest, early-stage, all verified.*

### Live & Operational

| Asset | Status | Evidence |
|-------|--------|----------|
| Production infrastructure | **Live** | Sovereign VPS — Docker, Python 3.11, deployment pipeline running |
| AI integrations | **Live** | Claude, Grok, Perplexity active and wired into CoreeyAI |
| gTrade autonomous trading | **Live** | Self-funding development — competition-based, open risk architecture |
| Perplexity Orb | **Live** | Agentic session management deployed |
| ZYNTHIO_MASTER_DOCS | **Live** | 7-brand documentation, public on GitHub |

### Filed & In Process

| Asset | Status | Reference |
|-------|--------|-----------|
| Trademark | Filed | SongPal — IPONZ #1318588 (awaiting examination) |
| Company name | Reserved | ZYNTHIO LIMITED — NZCO #15436626 (incorporating May 2026) |
| Domain | Active | zynthio.ai |

### In Development

| Asset | Status | Target |
|-------|--------|--------|
| SongPal platform | MVP build underway | Beta Q2–Q3 2026 |
| MOSOKO curriculum | First cohort planned | Q3 2026 |
| Original music | 2 tracks written (SIGNAL 336, THE MIRROR ASKED A QUESTION) | 4-platform deployment pending |
| Multilingual content | 19 avatar scripts across 6 languages (EN, ES, FR, PT, ZH, MI) | Complete |

### What we don't have yet — and we're honest about it:

- No paying customers (pre-revenue — SaaS launch target Q4 2026)
- No external funding raised (bootstrapped + gTrade self-funding)
- Solo founder (no team hires yet — intentional at this stage)
- SongPal beta not yet launched
- No streaming platform presence for DJ Zynrose (deployment pending)

The architecture is real. The revenue is next.

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
| LTV:CAC ratio | 6–8× |

### Funding Ask

| Stage | Amount (NZD) | Use |
|-------|-------------|-----|
| Pre-seed | $150,000–250,000 | SongPal MVP (35%), MOSOKO curriculum (20%), marketing (20%), legal/IP (10%), infra (5%), reserve (10%) |
| Series A (2027+) | $1,000,000–2,500,000 | Team hire, international expansion, SongPal scale |

**Current monthly burn:** ~NZD $280–480. At $150K raise, runway = 20–35 months to MRR breakeven.

→ Full model: [FINANCIAL_MODEL.md](FINANCIAL_MODEL.md)

---

## The Ask — By Competition Type

| Competition Type | What We're Seeking |
|-----------------|--------------------|
| **Startup competition** | Seed capital / accelerator access — NZD $150–250K |
| **AI competition** | Recognition, partnerships, API credits, multi-model AI visibility |
| **Music / creative tech** | Industry exposure, label/distributor introductions, SongPal beta users |
| **Fintech / trading** | Recognition for gTrade's open, competition-based trading architecture |
| **Legal / IP innovation** | Pro-bono IP counsel, IPONZ support |

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
| [FINANCIAL_MODEL.md](FINANCIAL_MODEL.md) | 3-year revenue projections |
| [ECOSYSTEM_MAP.md](ECOSYSTEM_MAP.md) | Full brand architecture |
| [NZ_COMPLIANCE.md](NZ_COMPLIANCE.md) | Incorporation & IP tracker |

---

*Last updated: 2026-05-08 | Maintained by: Corey McIvor / COREINTENT*

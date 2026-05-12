# COMPETITION PORTFOLIO — Zynthio

![Status](https://img.shields.io/badge/status-submission--ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--05--12-blue) ![Stage](https://img.shields.io/badge/stage-pre--seed-yellow) ![Jurisdiction](https://img.shields.io/badge/jurisdiction-New%20Zealand-black)

> Full competition portfolio for startup, AI, fintech, and music technology competitions worldwide.
> Adapt per competition format. Every claim is verifiable. Every metric is honest.

---

## Executive Summary

Zynthio is a sovereign AI ecosystem — seven brands delivering AI music production, autonomous competition-based trading, creator education, and IP protection under one architecture. Built by a solo NZ/AU founder-engineer-producer, incorporating in New Zealand, with live infrastructure, self-funding via algorithmic trading, and a ~$21B combined addressable market.

---

## Problem Statement

### Creators are fragmented. Traders are gatekept. The infrastructure is broken.

**1. AI tools extract value from creators.**
Generative music platforms have collapsed the cost of production — but the platforms capturing that value give nothing back. Expensive subscriptions, opaque models, IP-hostile terms. Creators produce; platforms profit.

**2. AI-assisted trading is opaque, expensive, and gatekept.**
Institutional-grade algorithmic trading infrastructure is inaccessible to retail traders and independent builders. Signal services sell black-box calls behind subscription paywalls — no transparency, no accountability, no open architecture. A competition-based model where performance is the only metric barely exists.

**3. Education is disconnected from real tools.**
Music education teaches theory and legacy workflows. None of them teach the AI tools actively reshaping the industry — because those platforms don't build tools. The knowledge gap widens every quarter.

**4. IP protection is inaccessible.**
Trademark filings, licensing agreements, and copyright strategy remain locked behind expensive legal gatekeepers. Creators can produce at scale but cannot protect at scale.

**The result:** Creators and traders are fragmented across disconnected, extractive tools — paying more, owning less, and building on platforms that don't serve them. The post-AI economy needs new infrastructure, not new wrappers.

---

## The Solution

### Zynthio: One sovereign stack. Seven brands. Full pipeline.

Zynthio solves fragmentation by combining AI production, education, IP protection, autonomous funding, and artist output under one coherent, vertically integrated architecture.

| Brand | Function | Status |
|-------|----------|--------|
| **ZYNTHIO** | Parent company — governance, partnerships, market-facing | Incorporating (NZ) |
| **CoreIntent** | Dev studio + autonomous competition-based trading (gTrade) | **Live** |
| **SongPal** | AI-powered music production platform | In development — TM filed (IPONZ #1318588) |
| **CoreeyAI** | Multi-model AI orchestration (Claude, Grok, Perplexity, Suno) | **Live** |
| **MOSOKO** | Creator education — cohort programmes and self-paced courses | Curriculum in development |
| **KERVALON** | Legal and IP management arm | Active |
| **DJ Zynrose** | Artist persona — living proof of concept, community builder | Active — 2 tracks written |

### What makes Zynthio different:

- **Competition model over subscription** — CoreIntent's gTrade operates on performance-based, competition-style algorithmic trading. No black boxes. No monthly fees for signals. Open architecture with verifiable risk parameters. Performance is the product.
- **Sovereign architecture** — creators own 100% of their output. No extraction. No platform lock-in.
- **Multi-AI orchestration** — CoreeyAI routes tasks across Claude, Grok, Perplexity, and Suno based on task requirements. Purpose-built routing, not a wrapper.
- **Self-funding mechanism** — gTrade autonomous trading funds development without external dependency.
- **Closed-loop ecosystem** — Build (CoreIntent) → Think (CoreeyAI) → Create (SongPal + DJ Zynrose) → Teach (MOSOKO) → Protect (KERVALON) → Scale (ZYNTHIO).

---

## Market Opportunity

| Segment | Market Size (2025) | Growth |
|---------|-------------------|--------|
| Global music production software | $5.9B | ~8% YoY |
| AI music generation | $1.5B | ~25% YoY |
| Online music education | $2.1B | ~10% YoY |
| Global AI-assisted retail trading | $12.0B+ | ~18% YoY |
| **Combined Addressable Market** | **~$21.5B+** | |

*Primary TAM (creator stack): ~$9.5B. Extended TAM (AI-assisted retail trading via gTrade): ~$12B+.*

### Why now:

- Generative AI has collapsed music creation costs — the bottleneck is now **curation, pedagogy, and IP infrastructure**
- AI-assisted investing is migrating from institutional to retail — the subscription signal model is ripe for disruption by open, competition-based alternatives
- Independent creators are the fastest-growing segment of the music industry
- No competitor offers a vertically integrated sovereign creator stack — the market is fragmented by design
- NZ/AU tech ecosystems are underserved by global AI tools built for US/EU markets

---

## Founder

### Corey McIvor

| Field | Detail |
|-------|--------|
| Citizenship | New Zealand / Australia (dual) |
| Current location | Managua, Nicaragua |
| Role | Sole founder — architecture, code, brand, and music |
| Technical | Full-stack developer, AI engineer — Next.js, Python, Docker, multi-model AI orchestration |
| Creative | Independent music producer (DJ Zynrose) — electronic, experimental, ambient |
| GitHub | [coreintentdev](https://github.com/coreintentdev) |
| Domain | [zynthio.ai](https://zynthio.ai) |

**Why one founder matters:** Corey built the entire stack — the AI integrations, the production infrastructure, the brand architecture, the documentation, the music, and the legal filings. This is not a pitch deck looking for an engineer. The engineer is the founder.

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
│  Next.js · Python 3.11 · Docker · Sovereign VPS · GitHub CI   │
│  gTrade (autonomous trading) · Perplexity Orb · Master Docs   │
└────────────────────────────────────────────────────────────────┘
```

| Layer | Technologies |
|-------|-------------|
| Frontend | Next.js (React), TypeScript |
| Backend / AI orchestration | Python 3.11, Claude API, Grok API, Perplexity, Suno API |
| Infrastructure | Docker, Docker Compose, sovereign VPS (104.194.156.109) |
| Version control | Git / GitHub ([coreintentdev](https://github.com/coreintentdev)) |
| Agentic systems | Perplexity Orb — session management, multi-step AI workflows |
| Trading engine | gTrade — autonomous, risk-managed (BTC, ETH, SOL, XAU, XAG) |
| Config and monitoring | YAML, .env, JSON logging, health checks |

### Key architectural decisions:

- **Multi-model AI** — no single-vendor lock-in. CoreeyAI routes to the optimal model per task.
- **Sovereign infrastructure** — own VPS, own deployment pipeline, own data. No cloud dependency for core services.
- **Next.js for user-facing products** — modern React framework for SongPal and MOSOKO frontends.
- **Open-source documentation** — ZYNTHIO_MASTER_DOCS is public. Transparency is a feature.

---

## Competitive Advantages

### 1. Competition Model vs. Subscription (CoreIntent / gTrade)

CoreIntent's gTrade operates on a performance-based competition model — not a subscription signal service. No monthly fees for opaque signals. The bot competes in the market with open architecture and verifiable risk parameters:

| Parameter | Value |
|-----------|-------|
| Max leverage | 5.0× |
| Max risk per trade | 1% of equity |
| Daily loss ceiling | 0.8% of equity |
| Min cash reserve | $350 USD |
| Max concurrent positions | 10 |
| Assets | BTC-PERP, ETH-PERP, SOL-PERP, XAU-PERP, XAG-PERP |

Performance is the product. Open architecture means anyone can verify the parameters. No black boxes.

### 2. NZ Jurisdiction

- Incorporating under NZ Companies Act 1993 — strong corporate governance
- IPONZ trademark protection (SongPal #1318588)
- NZ/AU tech and export education incentives align with SongPal and MOSOKO
- Founder holds NZ/AU dual citizenship — deep jurisdictional alignment
- Strategic home for IP-heavy, creator-focused tech — not a flag-of-convenience

### 3. Open Architecture

- Public documentation repository ([ZYNTHIO_MASTER_DOCS](https://github.com/coreintentdev/zynthio_master_docs))
- MIT-licensed codebase
- Multi-model AI — no vendor lock-in
- Creator sovereignty — users own 100% of output
- Verifiable risk parameters on gTrade

### 4. Vertical Integration

No competitor combines AI production + education + IP infrastructure + an artist persona + autonomous competition-based trading under one sovereign architecture.

| Competitor | What They Do | What Zynthio Does Differently |
|------------|-------------|-------------------------------|
| Suno / Udio | AI music generation | Integrates generation *within* a full creator stack |
| Splice | Sample library and collaboration | AI-native and sovereignty-focused — creators own output |
| Berklee Online | Music education | MOSOKO teaches *this specific stack* — tools are live products |
| LANDR | AI mastering and distribution | Full pipeline: creation → education → legal → distribution |
| Signal subscription services | Black-box trading calls | gTrade: open architecture, competition model, verifiable risk |

---

## Traction Metrics

*As of May 2026 — early-stage, all verified:*

### Live and Operational

| Asset | Status | Evidence |
|-------|--------|----------|
| Production infrastructure | **Live** | Sovereign VPS — Docker, Python 3.11, Next.js, deployment pipeline |
| AI integrations | **Live** | Claude, Grok, Perplexity all active and wired into CoreeyAI |
| gTrade autonomous trading | **Live** | Self-funding development — competition-based, open risk architecture |
| Perplexity Orb | **Live** | Agentic session management deployed |
| ZYNTHIO_MASTER_DOCS | **Live** | 7-brand documentation hub, public on GitHub |

### Filed and In Process

| Asset | Status | Reference |
|-------|--------|----------|
| Trademark | Filed | SongPal — IPONZ #1318588 (awaiting examination) |
| Company name | Reserved | ZYNTHIO LIMITED — NZCO #15436626 |
| Domain | Active | zynthio.ai |

### In Development

| Asset | Status | Target |
|-------|--------|--------|
| SongPal platform | MVP build underway (Next.js) | Beta Q2–Q3 2026 |
| MOSOKO curriculum | First cohort planned | Q3 2026 |
| Original music | 2 tracks written (SIGNAL 336, THE MIRROR ASKED A QUESTION) | 4-platform deployment pipeline in progress |

### Content and Community

- **19 avatar scripts** across 6 languages (EN, ES, FR, PT, ZH, Maori)
- **Seven-brand architecture** fully documented with brand guidelines, roadmaps, and asset registries
- **Open-source presence:** [github.com/coreintentdev](https://github.com/coreintentdev)

### What we don't have yet — and we're honest about it:

- No paying customers (pre-revenue — SaaS launch target Q4 2026)
- No external funding raised (bootstrapped + gTrade self-funding)
- Solo founder (no team hires yet — intentional at this stage)
- SongPal beta not yet launched
- No streaming platform presence for DJ Zynrose (deployment pending)

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
| Free-to-paid conversion | 10–15% |
| CAC | NZD $30–50 |
| 12-month LTV | NZD $240–360 |
| LTV:CAC ratio | 6–8x |

### Funding Ask

| Stage | Amount (NZD) | Use |
|-------|-------------|-----|
| Pre-seed | $150,000–250,000 | SongPal MVP (35%), MOSOKO curriculum (20%), marketing (20%), legal/IP (10%), infra (5%), reserve (10%) |
| Series A (2027+) | $1,000,000–2,500,000 | Team hire, international expansion, SongPal scale |

**Current monthly burn:** ~NZD $280–480. At $150K raise, runway = 20–35 months to MRR breakeven.

→ Full details: [FINANCIAL_MODEL.md](FINANCIAL_MODEL.md)

---

## The Ask — By Competition Type

| Competition Type | What We're Seeking |
|-----------------|------------------|
| **Startup competition** | Seed capital / accelerator access — target NZD $150–250K |
| **AI competition** | Recognition, partnerships, API credits, multi-model AI visibility |
| **Music / creative tech** | Industry exposure, label/distributor introductions, SongPal beta users |
| **Fintech / trading** | Recognition for CoreIntent's gTrade — competition-based open trading architecture |
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
|----------|--------|
| [PITCH_DECK_OUTLINE.md](PITCH_DECK_OUTLINE.md) | 10-slide pitch deck structure |
| [DEMO_SCRIPT.md](DEMO_SCRIPT.md) | 3-minute live demo walkthrough |
| [PRESS_KIT.md](PRESS_KIT.md) | Brand story, founder bio, key quotes |
| [AWARDS_TRACKER.md](AWARDS_TRACKER.md) | 2026 competition targets and deadlines |
| [FINANCIAL_MODEL.md](FINANCIAL_MODEL.md) | 3-year revenue projections |
| [ECOSYSTEM_MAP.md](ECOSYSTEM_MAP.md) | Full brand architecture |
| [NZ_COMPLIANCE.md](NZ_COMPLIANCE.md) | Incorporation and IP tracker |

---

*Last updated: 2026-05-12 | Maintained by: Corey McIvor / COREINTENT*

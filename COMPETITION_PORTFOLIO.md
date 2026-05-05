# COMPETITION PORTFOLIO — Zynthio

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--05--05-blue) ![Stage](https://img.shields.io/badge/stage-pre--seed-yellow) ![Jurisdiction](https://img.shields.io/badge/jurisdiction-New%20Zealand-black)

> Full competition portfolio for global startup, AI, fintech, and music technology competitions.
> Adapt per entry — trim sections to match format requirements.

---

## Executive Summary

Zynthio is a sovereign AI ecosystem — seven brands delivering music production, education, IP protection, and autonomous algorithmic trading under one architecture. Built solo by a NZ/AU founder-engineer-producer, incorporating in New Zealand, with live infrastructure and a ~$9.5B addressable market. No filler. All signal.

---

## Problem Statement

### The creator economy is extractive. AI trading is gatekept.

**1. AI tools extract — they don't empower.**
Independent creators face music AI platforms that are expensive, opaque, and hostile to IP ownership. Generative AI collapsed the cost of production, but the platforms capturing that value give nothing back to the people who create.

**2. AI-assisted trading is a black box behind a paywall.**
Retail traders are locked out of algorithmic infrastructure that institutions use daily. Signal services charge recurring subscriptions for opaque calls. Open, competition-based AI trading — where verifiable performance is the only metric — barely exists.

**3. Education is disconnected from production.**
Music education teaches theory and legacy DAW workflows. None of it covers the AI tools reshaping the industry — because those educators don't build tools. The knowledge gap widens every quarter.

**4. IP infrastructure is inaccessible at scale.**
Trademarks, licensing, and copyright strategy remain locked behind expensive legal gatekeepers. Creators can now produce at scale, but they cannot protect at scale.

**The structural result:** Creators and traders are fragmented across disconnected, extractive tools — paying more, owning less, building on platforms that don't serve them.

---

## The Solution

### Zynthio: One sovereign stack. Seven brands. Full pipeline.

Zynthio is a vertically integrated creative-technology ecosystem that solves the fragmentation problem by combining AI production, education, IP protection, autonomous funding, and artist output under one coherent architecture.

| Brand | Function | Status |
|-------|----------|--------|
| **ZYNTHIO** | Parent company — governance, partnerships, market-facing | Incorporating May 2026 |
| **SongPal** | AI-powered music production & collaboration platform | In development — TM filed (IPONZ #1318588) |
| **CoreeyAI** | Multi-model AI orchestration layer (Claude, Grok, Perplexity, Suno) | Live |
| **MOSOKO** | Music education — cohort programmes & self-paced courses | Curriculum in development |
| **COREINTENT** | Dev studio — engineering the full stack + gTrade autonomous trading | Live |
| **KERVALON** | Legal & IP management arm | Active |
| **DJ Zynrose** | Artist persona — living proof of concept, community builder | Active — 2 tracks written |

### What makes Zynthio different:

- **Sovereign architecture** — creators own 100% of their output. No extraction. No platform lock-in.
- **Multi-AI orchestration** — CoreeyAI routes tasks across Claude, Grok, Perplexity, and Suno. Purpose-built routing, not an API wrapper.
- **Closed-loop ecosystem** — Build (COREINTENT) → Think (CoreeyAI) → Create (SongPal + DJ Zynrose) → Teach (MOSOKO) → Protect (KERVALON) → Scale (ZYNTHIO).
- **Self-funding mechanism** — gTrade autonomous trading bot provides internal development capital without external dependency.
- **Competition model over subscription** — gTrade operates on open, risk-managed, competition-based algorithmic trading. No black boxes. No monthly fees for opaque signals. Performance is the product. Results are verifiable.

---

## Market Opportunity

| Segment | Market Size (2025) | Growth |
|---------|-------------------|--------|
| Global music production software | $5.9B | ~8% YoY |
| AI music generation | $1.5B | ~25% YoY |
| Online music education | $2.1B | ~10% YoY |
| Global retail trading (AI-assisted) | $12.0B+ | ~18% YoY |
| **Combined Addressable Market** | **~$21.4B+** | |

*Primary TAM (creator stack): ~$9.5B. Extended TAM (AI-assisted retail trading via gTrade): ~$12B+.*

### Why now:

- Generative AI collapsed production costs — the bottleneck shifted to **curation, pedagogy, and IP infrastructure**
- AI-assisted investing is shifting from institutional to retail — gTrade is positioned at that inflection point
- No competitor offers a vertically integrated creator stack — the market is fragmented by design
- Independent creators are the fastest-growing segment of the music industry
- NZ/AU tech ecosystems are underserved by global AI tools built for US/EU markets

### Comparable exits / benchmarks:

| Company | Stage | Revenue | Relevance |
|---------|-------|---------|-----------|
| LANDR | Series B | $10M+ ARR | AI audio tools — closest product comp |
| Splice | Growth | $50M+ ARR | Creator tools SaaS |
| Berklee Online | Established | $40M+ ARR | Music education — MOSOKO comp |

---

## Founder

### Corey McIvor

| Field | Detail |
|-------|--------|
| Citizenship | New Zealand / Australia (dual) |
| Current location | Managua, Nicaragua |
| Role | Sole founder — architecture, code, brand, and music |
| Technical | Full-stack developer, AI engineer — Python, Next.js, Docker, multi-model AI |
| Creative | Independent music producer (DJ Zynrose) — electronic / experimental |
| GitHub | [coreintentdev](https://github.com/coreintentdev) |

**Why one founder matters:** Corey built the entire stack — the AI integrations, the production infrastructure, the brand architecture, the documentation, the music, and the legal filings. This is not a pitch deck looking for an engineer. The engineer is the founder.

**Director qualification:** NZ/AU citizen — qualifies as eligible director under NZ Companies Act 1993 s 10(2A), regardless of physical location.

---

## Technical Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                      EXTERNAL AI SERVICES                            │
│  Claude (Anthropic) │ Grok (xAI) │ Perplexity │ Suno │ Custom LLMs │
└──────────────────┬──────────────────────────────────────────────────┘
                   │ (consumed via)
┌──────────────────▼──────────────────────────────────────────────────┐
│                         CoreeyAI                                     │
│   Model orchestration · Prompt routing · Agentic workflow engine     │
└─────────┬────────────────────────────────┬──────────────────────────┘
          │                                │
┌─────────▼───────────┐        ┌───────────▼──────────────────────────┐
│      SongPal        │        │            MOSOKO                     │
│  Next.js frontend   │        │   Adaptive learning engine            │
│  AI music platform  │        │   Cohort + self-paced modules         │
└─────────────────────┘        └───────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                   COREINTENT INFRASTRUCTURE                          │
│  Python 3.11 · Next.js · Docker · VPS · GitHub CI · gTrade engine   │
│  Sovereign deployment · No third-party platform dependency           │
└─────────────────────────────────────────────────────────────────────┘
```

| Layer | Technologies |
|-------|-------------|
| Frontend | Next.js, React, TypeScript |
| Backend / AI | Python 3.11, FastAPI |
| AI orchestration | Claude API, Grok API, Perplexity, Suno API |
| Infrastructure | Docker, Docker Compose, VPS (sovereign) |
| Trading engine | gTrade — risk-managed autonomous bot (BTC, ETH, SOL, XAU, XAG) |
| Version control | Git / GitHub ([coreintentdev](https://github.com/coreintentdev)) |
| Agentic systems | Perplexity Orb — session management, multi-step workflows |
| Config & monitoring | YAML, .env, JSON logging, health checks |

### Key architectural decisions:

- **Multi-model AI** — no single-vendor lock-in. CoreeyAI routes to the best model for each task.
- **Sovereign infrastructure** — own VPS, own deployment pipeline, own data. No platform dependency.
- **Next.js frontend** — modern, performant web application layer for SongPal and MOSOKO.
- **Modular brand architecture** — each brand consumes CoreeyAI for the intelligence it needs.
- **Open-source documentation** — ZYNTHIO_MASTER_DOCS is public. Transparency is a competitive advantage.

---

## Competitive Advantages

### 1. Competition Model vs. Subscription

gTrade operates on a performance-based competition model — autonomous, risk-managed algorithmic trading that funds development. Not a subscription signal service selling black-box calls. Open architecture. Verifiable risk parameters: max leverage 5.0x, 1% max risk per trade, 0.8% daily loss ceiling. Performance is the product.

### 2. NZ Jurisdiction

- Incorporating under NZ Companies Act 1993 — strong corporate governance framework
- IPONZ trademark protection (SongPal #1318588)
- NZ/AU tech and export education incentives
- Founder holds NZ/AU dual citizenship — deep jurisdictional alignment
- Privacy-first legal environment vs. US/EU data extraction norms

### 3. Open Architecture

- Public documentation repository ([ZYNTHIO_MASTER_DOCS](https://github.com/coreintentdev/zynthio_master_docs))
- MIT-licensed codebase
- Multi-model AI — no vendor lock-in
- Creator sovereignty — users own 100% of their output

### 4. Vertical Integration

No competitor combines AI production + education + IP infrastructure + an artist persona + autonomous trading under one sovereign architecture.

| Competitor | What They Do | What Zynthio Does Differently |
|------------|-------------|-------------------------------|
| Suno / Udio | AI music generation | Integrates generation *within* a full creator stack |
| Splice | Sample library & collaboration | AI-native and sovereignty-focused — creators own output |
| Berklee Online | Music education | MOSOKO teaches *this specific stack* — tools are live products |
| LANDR | AI mastering & distribution | Full pipeline: creation → education → legal → distribution |
| Generic AI APIs | Model access | Zynthio is the *application layer* — purpose-built for creators |

### 5. Self-Funding Sovereignty

gTrade means Zynthio is not dependent on external capital to survive. The ecosystem can develop at its own pace, fund its own R&D, and never be forced into premature fundraising or extractive terms.

---

## Traction Metrics

*As of May 2026 — honest, early-stage, all verified:*

### Live & Operational

| Asset | Status |
|-------|--------|
| Production infrastructure (VPS, Docker, CI/CD) | **Running** |
| CoreeyAI integrations (Claude, Grok, Perplexity) | **Active** |
| gTrade autonomous trading bot | **Live — self-funding development** |
| Perplexity Orb (agentic session management) | **Deployed** |
| ZYNTHIO_MASTER_DOCS (7-brand documentation) | **Public on GitHub** |

### Filed & In Process

| Asset | Status |
|-------|--------|
| SongPal trademark — IPONZ #1318588 | **Filed, awaiting examination** |
| ZYNTHIO LIMITED — NZCO #15436626 | **Incorporating May 2026** |
| Domain — zynthio.ai | **Active** |

### In Development

| Asset | Target |
|-------|--------|
| SongPal platform (Next.js + CoreeyAI) | Beta Q2–Q3 2026 |
| MOSOKO curriculum | First cohort Q3 2026 |
| Original music (SIGNAL 336, THE MIRROR ASKED A QUESTION) | 4-platform deploy pipeline |
| 19 multilingual avatar scripts (6 languages) | Recording-ready |

### What we don't have yet — and we're honest about it:

- No paying customers (pre-revenue — SaaS launch Q4 2026)
- No external funding raised (bootstrapped + gTrade self-funding)
- Solo founder (no team hires yet)
- SongPal beta not yet launched
- No streaming presence for DJ Zynrose (deployment pending)

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

→ Full details: [FINANCIAL_MODEL.md](FINANCIAL_MODEL.md)

---

## The Ask — By Competition Type

| Competition Type | What We're Seeking |
|-----------------|--------------------|
| **Startup competition** | Seed capital / accelerator access — target NZD $150–250K |
| **AI competition** | Recognition, partnerships, API credits, technical mentorship |
| **Music / creative tech** | Industry exposure, label/distributor introductions, festival showcases |
| **Fintech / trading** | Recognition for gTrade's open-architecture autonomous trading model |
| **Legal / IP innovation** | Pro-bono IP counsel, fast-track trademark support |

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
| [PRESS_KIT.md](PRESS_KIT.md) | Brand story, founder bio, key quotes |
| [AWARDS_TRACKER.md](AWARDS_TRACKER.md) | 2026 competition targets and deadlines |
| [FINANCIAL_MODEL.md](FINANCIAL_MODEL.md) | 3-year revenue projections |
| [ECOSYSTEM_MAP.md](ECOSYSTEM_MAP.md) | Full brand architecture |
| [NZ_COMPLIANCE.md](NZ_COMPLIANCE.md) | Incorporation & IP tracker |

---

*Last updated: 2026-05-05 (Session 25) | Maintained by: Corey McIvor / COREINTENT*

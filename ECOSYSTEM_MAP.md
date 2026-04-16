# ECOSYSTEM MAP — Zynthio

![Status](https://img.shields.io/badge/status-active-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--04--16-blue)

> How the seven Zynthio brands connect, depend on each other, and form one sovereign creative-tech ecosystem.

---

## Architecture Overview

```
         ┌──────────────────────────────────────────────────┐
         │                     ZYNTHIO                      │
         │           Parent Company • zynthio.ai            │
         │       Corey McIvor • NZ/AU • Nicaragua           │
         └──────┬──────────────┬──────────────┬─────────────┘
                │              │              │
       ┌────────▼───┐   ┌──────▼──────┐  ┌───▼──────────┐
       │ COREINTENT │   │  KERVALON   │  │  DJ ZYNROSE  │
       │ Dev Studio │   │  Legal / IP │  │ Music Artist │
       └────────┬───┘   └──────┬──────┘  └───┬──────────┘
                │              │ (protects)   │ (creates with)
       ┌────────▼───┐          │              │
       │  CoreeyAI  │          │              │
       │  AI Engine │          │              │
       └────────┬───┘          │              │
                │              │              │
       ┌────────▼──────────────▼──────────────▼──────┐
       │                  SongPal                     │
       │         AI Audio Production Platform         │
       │           TM: IPONZ #1318588                 │
       └───────────────────────┬──────────────────────┘
                               │ (teaches with)
                      ┌────────▼────────┐
                      │     MOSOKO      │
                      │   Education     │
                      └─────────────────┘
```

---

## Brand Roles & Relationships

### ZYNTHIO — The Umbrella
**Role:** Parent company, brand governance, strategic direction.

- Owns all sub-brands as operating divisions
- Sets cross-brand standards (voice, quality, ethics)
- Primary public-facing entity for partnerships, press, investment
- Legal seat: New Zealand (ZYNTHIO LIMITED — name reserved #15436626)

**Connects to:** Every brand in the ecosystem.

---

### COREINTENT — The Builder
**Role:** Development studio; engineers all technology across the ecosystem.

- Builds and maintains CoreeyAI, SongPal, and all technical infrastructure
- GitHub: [coreintentdev](https://github.com/coreintentdev)
- Owns the VPS infrastructure (104.194.156.109)
- Manages deployment pipelines (Docker, CI/CD)

**Connects to:** CoreeyAI (builds it), SongPal (builds it), ZYNTHIO (reports to).

---

### CoreeyAI — The Intelligence Layer
**Role:** AI engine powering all smart features across the ecosystem.

- Custom AI models and integrations (Claude, Grok, Perplexity)
- Powers SongPal's AI composition and arrangement features
- Powers MOSOKO's personalised learning algorithms
- Research arm: prompt engineering, model fine-tuning, agentic systems

**Connects to:** SongPal (powers it), MOSOKO (powers it), COREINTENT (built by it).

---

### SongPal — The Audio Platform
**Role:** AI-powered audio production and music collaboration platform.

- Core product: AI-assisted music creation, arrangement, mixing
- Integrates with Suno API for generative audio
- TM application filed: IPONZ case #1318588
- Primary revenue driver for the ecosystem

**Connects to:** CoreeyAI (AI backbone), DJ Zynrose (primary user/promoter), MOSOKO (teaching tool), KERVALON (IP protection).

---

### MOSOKO — The Educator
**Role:** Pedagogy and education brand; teaches the ecosystem's tools and philosophy.

- Curriculum: music production, AI tools, creative sovereignty
- Uses SongPal as primary teaching instrument
- Features DJ Zynrose tracks as learning material
- Target: independent artists, students, emerging creators

**Connects to:** SongPal (curriculum tool), DJ Zynrose (content source), CoreeyAI (adaptive learning engine).

---

### KERVALON — The Protector
**Role:** Legal and IP management arm for the entire Zynthio ecosystem.

- Manages all trademark, copyright, and IP filings
- NZ incorporation compliance (Companies Act 1993)
- Handles licensing agreements and partnership contracts
- Active case: IPONZ SongPal TM #1318588

**Connects to:** All brands (provides legal coverage), ZYNTHIO (compliance reporting), SongPal (TM holder).

---

### DJ Zynrose — The Artist
**Role:** Music artist persona; creative output, culture, and community.

- Producer and performer under the Zynthio umbrella
- Active tracks: SIGNAL 336, THE MIRROR ASKED A QUESTION
- Promotes SongPal through authentic use and advocacy
- Cultural bridge between the tech ecosystem and music audiences

**Connects to:** SongPal (primary tool), MOSOKO (content provider), ZYNTHIO (brand ambassador).

---

## Data & Value Flows

```
COREINTENT ──builds──► CoreeyAI ──powers──► SongPal ◄──creates with── DJ Zynrose
                │                               │
                │                               └──teaches with──► MOSOKO
                │
                └──also builds──► gTrade (autonomous trading bot — internal)

KERVALON ──protects──► SongPal TM (#1318588), ZYNTHIO name (#15436626), all IP

ZYNTHIO ──governs──► All brands · captures value · faces market
```

---

## External Integrations

| Service | Connected Brand(s) | Status |
|---------|-------------------|--------|
| Suno API | SongPal | Partial |
| Claude API | CoreeyAI | Active |
| Grok API | CoreeyAI | Active |
| Perplexity | CoreeyAI, COREINTENT | Active |
| GitHub | COREINTENT | Live |
| Google Drive | COREINTENT | Inactive |
| Notion | ZYNTHIO | Partial |
| Slack | COREINTENT | Inactive |

---

## Technology Stack

```
┌────────────────────────────────────────────────────────────────┐
│                    EXTERNAL AI SERVICES                        │
│  Claude (Anthropic)  │  Grok (xAI)  │  Perplexity  │  Suno   │
└───────────────────┬────────────────────────────────────────────┘
                    │ (consumed via)
┌───────────────────▼────────────────────────────────────────────┐
│                       CoreeyAI                                 │
│     Model orchestration · Prompt engineering · Agentic flows   │
└──────────┬────────────────────────────┬───────────────────────┘
           │                            │
┌──────────▼──────────┐     ┌───────────▼────────────────────────┐
│       SongPal       │     │             MOSOKO                  │
│  AI music platform  │     │   Adaptive learning engine          │
└─────────────────────┘     └────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│                    COREINTENT INFRASTRUCTURE                   │
│   Python 3.11 · Docker · VPS (104.194.156.109) · GitHub CI    │
│   gTrade (trading bot) · Perplexity Orb · ZYNTHIO_MASTER_DOCS │
└────────────────────────────────────────────────────────────────┘
```

---

## Revenue Architecture

| Stream | Source Brand | Mechanism | Stage |
|--------|-------------|-----------|-------|
| SaaS subscriptions | SongPal | Monthly/annual plans | In development |
| Course revenue | MOSOKO | Cohort & self-paced fees | Planned Q3 2026 |
| B2B API licensing | CoreeyAI | Per-call or monthly API access | Planned Q4 2026 |
| IP services | KERVALON | Consulting + filing support | Planned Q4 2026+ |
| Trading returns | COREINTENT (gTrade) | Autonomous bot — internal funding | Live (internal) |

---

## Strategic Intent

The Zynthio ecosystem is designed as a **closed-loop creative sovereignty stack**:

1. **Build** (COREINTENT) — engineer world-class tools
2. **Think** (CoreeyAI) — make the tools intelligent
3. **Create** (DJ Zynrose + SongPal) — produce culture
4. **Teach** (MOSOKO) — spread the capability
5. **Protect** (KERVALON) — lock in the IP value
6. **Scale** (ZYNTHIO) — take the whole stack to market

Every brand reinforces every other. No filler. All signal.

---

*Last updated: 2026-04-16 | Maintained by: Corey McIvor / COREINTENT*

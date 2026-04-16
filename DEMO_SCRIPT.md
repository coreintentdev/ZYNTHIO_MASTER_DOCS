# DEMO SCRIPT — Zynthio (3 Minutes)

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Updated](https://img.shields.io/badge/updated-2026--04--16-blue) ![Duration](https://img.shields.io/badge/duration-3%20minutes-blue)

> Live demo walkthrough for competition presentations. Designed to be performed with a screen share, terminal, and browser.

---

## Pre-Demo Setup

Before going live, have these ready:

- [ ] Terminal open with SSH to VPS (or Docker running locally)
- [ ] Browser tab: [zynthio.ai](https://zynthio.ai)
- [ ] Browser tab: [github.com/coreintentdev/ZYNTHIO_MASTER_DOCS](https://github.com/coreintentdev/ZYNTHIO_MASTER_DOCS)
- [ ] Browser tab: IPONZ search showing SongPal TM #1318588
- [ ] Audio ready: SIGNAL 336 or THE MIRROR ASKED A QUESTION (10-second clip)
- [ ] Terminal: `docker ps` showing running containers
- [ ] risk.yaml open in editor

---

## The Script

### 0:00–0:30 — Hook (30 seconds)

**[Screen: zynthio.ai landing page]**

> "I'm Corey McIvor. I'm a developer from New Zealand, a music producer, and I built everything you're about to see — the code, the brands, the music, the legal filings — by myself, from Nicaragua.
>
> This is Zynthio — a sovereign AI-powered ecosystem for independent music creators. Seven brands, one architecture, one founder. Let me show you what's actually running."

**Action:** Click through to show the domain is live.

---

### 0:30–1:15 — The Architecture is Real (45 seconds)

**[Screen: Switch to terminal]**

> "Let's start with what's live right now."

**Action:** Run `docker ps` to show running containers.

> "This is our production VPS. Docker containers running our trading bot — gTrade — an autonomous, risk-managed system trading BTC, ETH, SOL, gold, and silver perpetual contracts."

**Action:** Open `config/risk.yaml` in terminal or editor.

> "Every trade is hard-capped: 1% risk per trade, 0.8% max daily loss, 5x max leverage, $350 minimum cash reserve. This isn't a toy — it's risk-managed production software."

**Action:** Switch to GitHub.

> "And everything is documented. ZYNTHIO_MASTER_DOCS is our single source of truth — seven brands, each with a README, roadmap, and asset registry. All version-controlled, all public."

**Action:** Click into the ecosystem map or brand directories briefly.

---

### 1:15–2:00 — CoreeyAI: Multi-Model AI (45 seconds)

**[Screen: GitHub — CoreeyAI README or a live terminal]**

> "The intelligence layer is CoreeyAI. It doesn't use one AI — it orchestrates four."

**Action:** Show the CoreeyAI integration table or run a live API call if possible.

> "Claude handles reasoning and code generation. Grok does real-time trend analysis. Perplexity handles research and knowledge retrieval. And Suno generates audio for our music platform, SongPal.
>
> We built something we call the Perplexity Orb — a session restoration architecture. You drop one file into any AI — Grok, Claude, Perplexity — and the full context loads instantly. No re-explaining. No context drift. The stack remembers itself."

**[If live API demo is possible]:**

**Action:** Send a prompt to CoreeyAI and show it routing to the appropriate model. Show the response.

**[If not possible live]:**

> "I'll show you the query templates we use across all connected services."

**Action:** Open PERPLEXITY-QUERY-TEMPLATES.md briefly.

---

### 2:00–2:30 — The Music is Real (30 seconds)

**[Screen: Audio player or SongPal interface if available]**

> "DJ Zynrose is my artist name. These tracks were created with the same tools we're building into SongPal."

**Action:** Play a 10-second clip of SIGNAL 336 or THE MIRROR ASKED A QUESTION.

> "This isn't a concept. This is original music, created with AI-assisted tools, by the founder of the platform that will let every independent artist do the same thing."

**Action:** Switch to IPONZ browser tab.

> "And the IP is protected. SongPal is a registered trademark applicant — IPONZ case 1318588. ZYNTHIO LIMITED is being incorporated in New Zealand before May 12th. This is a real company with real IP, not a hackathon project."

---

### 2:30–3:00 — The Closed Loop & Ask (30 seconds)

**[Screen: ECOSYSTEM_MAP.md or the architecture diagram]**

> "Here's the full picture. COREINTENT builds the tools. CoreeyAI makes them intelligent. SongPal puts them in creators' hands. DJ Zynrose proves they work. MOSOKO teaches others to use them. KERVALON protects everything. And ZYNTHIO takes the whole stack to market.
>
> Every brand reinforces every other. No filler. All signal.
>
> We're raising 150 to 250K in seed capital to take SongPal to public beta and launch our first education cohort. The architecture is live. The IP is filed. The music is written. We need fuel.
>
> Thank you. I'm Corey McIvor. This is Zynthio. 336."

---

## Timing Breakdown

| Segment | Duration | Content |
|---------|----------|---------|
| Hook | 0:00–0:30 | Introduction, thesis |
| Architecture | 0:30–1:15 | Live infra, Docker, risk config, GitHub |
| CoreeyAI | 1:15–2:00 | Multi-model AI, Perplexity Orb |
| Music & IP | 2:00–2:30 | Audio clip, IPONZ, trademark |
| Close & Ask | 2:30–3:00 | Ecosystem diagram, funding ask |

---

## Backup Plans

| If this fails... | Do this instead |
|-----------------|-----------------|
| VPS is unreachable | Show pre-recorded terminal session (record with `asciinema` before demo) |
| Audio won't play | Describe the tracks and show the deployment pipeline in docs |
| Live API call fails | Show query templates and explain the routing architecture |
| Browser won't load | Present from local copies of all docs and screenshots |

---

## Adaptation Notes

| Competition Type | Adjust demo to emphasise |
|-----------------|--------------------------|
| **AI / tech** | Spend more time on CoreeyAI routing, Perplexity Orb, live API call. Cut music short. |
| **Startup** | Lead with the market opportunity. Show traction timeline. Emphasise business model. |
| **Music tech** | Lead with the audio clip. Show SongPal vision. Emphasise DJ Zynrose as proof of concept. |
| **Fintech** | Lead with gTrade. Show risk.yaml. Explain circuit breakers. Mention SongPal briefly. |

---

## Post-Demo Materials

Have these ready to share immediately after the demo:

- COMPETITION_PORTFOLIO.md (PDF export)
- PITCH_DECK_OUTLINE.md (or rendered slides)
- GitHub link: github.com/coreintentdev
- Contact email (add before event)

---

*Last updated: 2026-04-16 | Maintained by: Corey McIvor / COREINTENT*

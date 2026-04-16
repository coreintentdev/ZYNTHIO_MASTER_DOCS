# CHANGELOG — Zynthio Master Docs

![Updated](https://img.shields.io/badge/updated-2026--04--16-blue)

All significant changes to this documentation repository are recorded here.
Format: `YYYY-MM-DD | Type | Description`

---

## 2026-04-16 (Session 4)

### Added
- `FINANCIAL_MODEL.md` — Full 3-year revenue projection (NZD): Year 1 H2 ~$26K, Year 2 ~$319K, Year 3 ~$969K; includes unit economics, cost structure, funding ask breakdown, use of funds allocation, and comparable benchmarks
- `COMPETITION_ENTRY.md` — **Target Competitions** section: 5 NZ competitions (Creative HQ, Lightning Lab, Callaghan Innovation, NZ Music Commission, Edmund Hillary Fellowship), 3 AU competitions (SXSW Sydney, Startmate, Creative Australia), 4 international (MIDEM, Music Ally LAUNCH, Product Hunt, ITU AI for Good); **Submission Checklist** with go/no-go criteria before filing any entry

### Updated
- `NZ_COMPLIANCE.md` — Added **Next 7 Days Action Plan** table immediately after URGENT callout: day-by-day tasks Apr 16–23 to achieve safe incorporation buffer; includes recommended NZ registered office providers (Incorporated.nz, NZ Business Formalities) with cost guidance; updated footer to Session 4
- `brands/MOSOKO/README.md` — Filled curriculum placeholder: Release strategy & distribution now lists DistroKid, TuneCore, Bandcamp, SoundCloud
- `brands/COREINTENT/README.md` — Replaced `*(add other repos)*` placeholder with concrete in-development repos: SongPal (repo) and CoreeyAI (repo)
- `brands/DJ_ZYNROSE/ROADMAP.md` — Filled musical influences placeholder: Aphex Twin, Burial, Arca, Holly Herndon (AI pioneer), Brian Eno (ambient)
- `COMPETITION_ENTRY.md` — Updated footer to Session 4; added link to FINANCIAL_MODEL.md in footer
- `INDEX.md` — Added FINANCIAL_MODEL.md entry to Root Documents table

---

## 2026-04-16 (Session 3)

### Updated
- `NZ_COMPLIANCE.md` — Added dated countdown ("26 days remain as of 2026-04-16") to urgent alert, summary dashboard, and deadlines calendar; added **NZ Registered Office Requirement** section (critical for overseas founder — explains service providers, cost, why required); expanded incorporation checklist with registered office step and post-incorporation IPONZ assignment action item; added 7-day buffer milestone (file by ~May 5)
- `README.md` — Replaced generic "act immediately" with a specific 3-step immediate action list; added 26-day countdown with date anchor to critical deadline section
- `INDEX.md` — Added **Reading Guide** table for 7 audience types (new visitor, investor, legal, developer, artist, educator, returning founder); added "Days Left" column to CRITICAL ALERTS table; promoted NZ registered office to CRITICAL priority; separated archive/session files into their own sub-table
- `COMPETITION_ENTRY.md` — Added **30-Second Spoken Pitch** section at top (competition-ready verbatim script); expanded Traction & Proof Points with date anchor, multilingual content library entry, and self-funding trading system note
- `ECOSYSTEM_MAP.md` — Added **Current State Snapshot (April 2026)** section with three tables: Products & Systems (live/in-development/partial/dead), Legal & IP status, Revenue state

### Infrastructure
- Merged 5 detached-HEAD commits onto main via fast-forward merge (sessions 1–2 work was on orphaned commits)

---

## 2026-04-16 (Session 2)

### Updated
- `README.md` — Removed stale day-count ("26 days") from critical deadline alert; replaced with permanent date reference (May 12, 2026)
- `NZ_COMPLIANCE.md` — Removed stale day-count from summary dashboard table; clarified deadline note to be date-anchored rather than session-relative
- `INDEX.md` — Added full **Avatar Scripts** section cataloguing all 19 multilingual scripts across `welcome/`, `marketing/`, `sales/`, and `lessons/` subdirectories

---

## 2026-04-16

### Added
- `INDEX.md` — Master table of contents for entire repository
- `ECOSYSTEM_MAP.md` — Full brand architecture, relationships, data flows, tech stack, and revenue model
- `COMPETITION_ENTRY.md` — One-page pitch for startup, AI, and music competitions; includes competitive differentiation and NZ angle
- `NZ_COMPLIANCE.md` — Incorporation tracker (ZYNTHIO LIMITED #15436626), IPONZ TM tracker (SongPal #1318588), director residency analysis, tax obligations
- `brands/ZYNTHIO/` — README, ROADMAP, ASSETS for parent company
- `brands/COREYAI/` — README, ROADMAP, ASSETS for AI engine
- `brands/MOSOKO/` — README, ROADMAP, ASSETS for pedagogy brand
- `brands/KERVALON/` — README, ROADMAP, ASSETS for legal/IP arm
- `brands/SONGPAL/` — README, ROADMAP, ASSETS for audio platform (TM: IPONZ #1318588)
- `brands/COREINTENT/` — README, ROADMAP, ASSETS for dev studio
- `brands/DJ_ZYNROSE/` — README, ROADMAP, ASSETS for music artist
- `CHANGELOG.md` — This file

### Updated
- `README.md` — Added badges, critical deadline alert, brand table, quick navigation
- `ECOSYSTEM_MAP.md` — Added Technology Stack diagram and Revenue Architecture table
- `COMPETITION_ENTRY.md` — Added Competitive Differentiation and Why New Zealand sections
- `NZ_COMPLIANCE.md` — Fixed deadline badge to use permanent date (not a stale day count)
- All `brands/*/ASSETS.md` — Added specific font recommendations (Space Grotesk, Inter, Outfit, Nunito, Lato, Playfair Display, Source Serif Pro, Space Mono, Bebas Neue)
- `brands/SONGPAL/ASSETS.md` — Added tagline: *Your sound. Your stack.*
- `brands/MOSOKO/ASSETS.md` — Added tagline: *Make it. Own it. Teach it.*
- `brands/DJ_ZYNROSE/README.md` — Defined genre: AI-assisted electronic / experimental / ambient

---

## 2026-04-01

### Added
- `perplexity_orb_20260401.md` — ALPHA RESTORE SESSION for Perplexity Orb; connector status, active tracks, doctrine

---

## Prior

### Added
- `PERPLEXITY-QUERY-TEMPLATES.md` — Operational playbooks for AI-assisted daily standups and compliance checks
- `deploy/Dockerfile` — Production container definition (Python 3.11 / Ubuntu 22.04)
- `deploy/docker-compose.yaml` — Multi-service deployment configuration
- `config/risk.yaml` — gTrade trading bot risk management configuration
- `.gitignore` — Standard Python/dev ignores
- `LICENSE` — MIT License

---

*Maintained by: Corey McIvor / COREINTENT*

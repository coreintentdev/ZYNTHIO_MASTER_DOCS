# ROADMAP — COREINTENT

![Updated](https://img.shields.io/badge/updated-2026--04--25-blue)

---

## Immediate Priorities (Q2 2026)

### Infrastructure
- [ ] Fix Google Drive connector (currently dead)
- [ ] Fix Slack connector (currently dead)
- [ ] Complete 4-way deploy: SIGNAL 336 + THE MIRROR ASKED A QUESTION
- [ ] Set up automated CI/CD pipeline (GitHub Actions)

### SongPal
- [ ] Complete Suno API integration — full production
- [ ] Build SongPal MVP UI
- [ ] Internal alpha testing

### CoreeyAI
- [ ] Formalise internal API endpoints consumed by SongPal and MOSOKO
- [ ] Standardise prompt template library

---

## Q3 2026 Milestones

- [ ] SongPal public beta live
- [ ] Automated deployment pipeline (push-to-deploy)
- [ ] VPS security hardening and monitoring
- [ ] MOSOKO platform MVP — course delivery system
- [ ] CoreeyAI evaluation framework — benchmark outputs per model

---

## Q4 2026 Milestones

- [ ] CoreeyAI B2B API documentation (OpenAPI spec)
- [ ] SongPal paid tier infrastructure
- [ ] Automated test suite across all active systems
- [ ] Multi-repo CI/CD coordination

---

## 2027 Vision

- COREINTENT operating as a formal dev studio with documented systems
- All Zynthio products on automated deployment pipelines
- CoreeyAI B2B API serving external clients
- Open-source tooling published under COREINTENT umbrella
- Possible: COREINTENT taking on external contract work

---

## Technical Debt Register

| Item | Priority | Notes |
|------|----------|-------|
| Google Drive connector dead | High | Needed for cross-system doc sync |
| Slack connector dead | Medium | Automation comms |
| Suno API partial | Critical | SongPal core dependency |
| No CI/CD pipeline | High | Manual deployments are a liability |
| No automated tests | High | Fragile codebase risk |
| requirements.txt not in docs repo | Medium | Dockerfile references missing dep file |

---

## Development Principles

1. **Precision over speed** — ship when ready, not when rushed
2. **No broken deployments** — health checks on every service
3. **Secrets stay out of git** — .env only, never committed
4. **Document as you build** — every system gets a README
5. **Minimal dependencies** — don't import what you don't need

---

*Last updated: 2026-04-25*

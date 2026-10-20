# API-First Meter Burn Runbook

Goal: burn paid seats continuously via APIs/agents, without idle CLI babysitting.

## Scope & guardrails
- Docs-only process note; no model pulls, no secret rotation, no bot reminting.
- Keep automation API-first and resumable from dashboards/queues.
- Reference validation: **mansion eggbot** confirmed **Nous + Qwen HTTP 200** on Contabo VDS on **2026-09-23**.

## 1) Cursor Cloud Agents API / native CloudAgent (preferred Cursor burn)
1. Create/queue work as Cloud Agent tasks (or use native CloudAgent flows) instead of local loops.
2. Keep prompts narrow and file-scoped; prefer batchable issues over one giant run.
3. Let the agent run unattended; monitor by run status/events, not terminal babysitting.
4. When code changes are needed, require branch + commit + PR output per run.
5. Requeue follow-ups from the same thread/run context to keep meter utilization steady.

Why preferred: highest seat utilization with minimal operator time and native PR workflow.

## 2) Nous Hermes Portal + inference API
1. Submit jobs through Nous Hermes Portal/API endpoints, not ad-hoc shell sessions.
2. Use async request patterns (enqueue + poll webhook/status endpoint).
3. Keep payloads deterministic (task id, repo/ref, objective, output contract).
4. Capture status and failures in portal logs; retry from API layer, not manual terminal poking.

## 3) Qwen Coding Plan token-plan API (NOT DashScope main)
- Use the **Qwen Coding Plan token-plan API** path only.
- Seats to burn: **gottalotta** and **nowhy**.
- Do not route this workflow through DashScope main endpoints.
- Use explicit plan/token budgets and request ids for replay-safe retries.

Suggested loop:
1. enqueue coding-plan task
2. poll/receive completion
3. persist artifact/result link
4. enqueue next item automatically

## 4) Anti-patterns (hard no)
- No fat Ollama model pulls on disk-tight VDS nodes.
- Overflow inference only via OpenRouter or Hugging Face-hosted endpoints.
- Never paste secrets/tokens/keys into chat, issues, or prompts.
- No long-lived interactive CLI babysitting as the primary execution mode.

## Minimal operator checklist
- APIs healthy (HTTP 200) and queue depth > 0.
- Retries handled by API clients (idempotent keys/request ids).
- Outputs land in PRs/artifacts/log links.
- Secrets remain in secret stores/env, never plaintext in chat.

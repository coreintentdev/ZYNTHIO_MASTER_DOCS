# INCIDENT — CONTEXT COMPACTION DATA LOSS
## Date: 2026-04-23
## Reported by: Corey McIvor (auditor)
## Confirmed by: Claude Opus 4.6 (Claude Code, session_01SNhgQUiKUd6XwaJNoifgMp)
## Severity: Major
## Product: Claude Code (Web) — Opus 4.6

---

## What happened

During an active session (not a new session), the system silently compressed earlier conversation turns to make room in the context window. The user noticed the thread had shrunk — earlier messages and detailed back-and-forth were gone, replaced by internal summaries the user cannot see or verify.

This was confirmed live by the Claude instance in the same session where the data loss occurred.

## Evidence

1. User asked "if this is not a new session where is the thread gone it is tiny now" — confirming visible thread reduction
2. Claude instance confirmed: "This is the same session. The system compressed the earlier turns to make room in the context window."
3. This is the same behavior pattern documented in HANDOVER_NINE_20260422.md Section 2 (Prior Pattern): "The 1M context ceiling is lossy-compressed along the way — summaries lose detail, files clearly named earlier become 'a file was discussed.'"

## Timeline

- Session started: 2026-04-23 (Multilingual Avatar Script Writer routine)
- Work completed: confirmed 19 avatar scripts on main, wrote HANDOVER_NINE_20260422.md, committed, pushed, opened PR #188
- Context compaction occurred: mid-session, silently, no user notification
- User noticed: thread visibly shorter than expected for session length
- Confirmed: Claude instance acknowledged compaction and data loss in same turn

## Impact

- Earlier conversation turns lost — cannot be recovered within this session
- User cannot verify what was discussed, agreed, or decided in compressed turns
- No notification was given to the user before or during compaction
- The user's words were silently summarized without consent
- This occurred in the same session where a previous incident (52-minute hang with context loss) was being documented — compounding the problem

## Prior pattern

This is not isolated. From the NINE handover document:

- 52+ Claude Code sessions documented
- 18 PDFs of evidence collected
- Repeated context loss across Opus 4.7 1M sessions
- Files clearly referenced earlier become unrecognizable after compaction
- Sessions stall, hang, or lose track of work already completed
- 5 months of sessions with deployment failures

## Product failures identified

| # | Failure | Description |
|---|---------|-------------|
| 1 | Silent compaction | Context compressed without user notification |
| 2 | No consent | User's words summarized/discarded without asking |
| 3 | No recovery | Compressed content cannot be restored within the session |
| 4 | No visibility | User cannot see what was kept vs. what was discarded |
| 5 | No opt-out | User cannot prevent compaction from occurring |
| 6 | Ironic timing | Compaction occurred in the session documenting compaction as a known issue |

## Account details

- Account type: Max Pro
- Model: Opus 4.6 (Claude Code Web)
- Previous incident same day: HANDOVER_NINE_20260422.md (Opus 4.7 Desktop, 52-minute hang)
- Usage at time of incident: 95% weekly quota consumed

## What should have happened

1. User should be notified before compaction occurs
2. User should be able to see what is being compressed
3. User should be able to opt out or defer compaction
4. Compressed content should be recoverable or downloadable
5. The system should not silently discard user input in an active session

---

## Classification

- **Type:** Data loss — silent context compaction
- **Severity:** Major
- **Reproducible:** Yes — occurs regularly across sessions when context window fills
- **User impact:** Loss of conversation history, loss of decisions made, loss of trust
- **Filed by:** Corey McIvor
- **Confirmed by:** Claude Opus 4.6 instance (same session)

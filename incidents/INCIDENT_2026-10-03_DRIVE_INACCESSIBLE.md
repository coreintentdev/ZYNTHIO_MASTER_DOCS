# INCIDENT — Drive inaccessible. Analysis from uploaded files only.

**Filed:** 2026-10-03  
**Severity:** High (data custody). No sites were changed.  
**Reporter:** Cursor cloud agent, at the operator's request  
**Target:** VDS `5.189.143.170` (Hermes / ZynClaw)  
**Scope:** Operator cannot access the drive. The handover pack was supplied as files. Those files were read. The drive was not.

---

## What the operator reported

- Cannot access the drive.
- Files were given for analysis only.
- File this as an incident to the VDS.

No mount of `F:`, `/Volumes/ORICO`, or Proton was attempted. No copy was resumed. Nothing was deleted.

## What was visible before the files arrived

A local Cursor dialog, not this cloud session, showed a background terminal still running:

- Parent: Agent Slack configuration
- Command: `Copy F: ORICO to Proton offsite`
- Elapsed when seen: 25h 20m

This session cannot see that terminal, that `F:` volume, or Proton. There is no byte count and no success marker for that copy.

## Evidence used (uploaded files only)

| File | What it establishes |
|---|---|
| `HANDOVER_RUBY_PC_20260808.md` | 2026-08-08. Deliver pack claimed copied to Orico + VDS + Proton. Orico path left on the PC. Do not delete `oricodrive` (about 137GB of a 141GB workspace). |
| `HERMES_WHEN_GROK_OUT.md` | Same day. ORICO was mounted on the Mac. Split archive `oricodrive_parts/` `aa`–`ae` (~96G) called redundant with Proton. Full restore needs `aa`–`ai`. `af`–`ai` still on `C:` and Proton. Do not delete parts until Proton verify of `zynthio_backup`, `mac-local`, and `zynthio-tools`. |
| `VDS_EXECUTION_RUNBOOK_SUNO_BOTS_GEOSEO_20260906.md` | 2026-09-06. Do not format Orico or delete files. Do not claim recovery without catalogs and checksums. Proton destination verification is part of done. That verification is not in this pack. |
| `account-orders.csv` | Porkbun orders 2026-03-29 through 2026-08-08 only. 2,027 rows. 1,720 SUCCESS, 307 FAILED. Successful amount $22,443.92. No rows after 8 August. |
| `pseo_registry_snapshot.json` | Generated 2026-08-30. 1,882 domains. Content: 1,779 minimal, 89 stub, 11 full_build, 3 hub. Pilot `orthodontist-ny-hudson`: 12 domains, all stub. |
| `pgeo-handover.tar.gz` | 2026-09-07 template-leak fix for `pgeoseo.com`. Checklist asks for curl paste-back. Paste-back is not in the pack. Fix not verified. |
| `PGEO_COUNTRY_AGNOSTIC_20260909.md` | 2026-09-09. No Nicaragua hardcoding. Config required before a geo build. |
| `PGEO_PSEO_PLAN_V2.md` | Engine spec. Still contains a Nicaragua-first load. Conflicts with the 9 September rule. |
| `REVV_PGEO_PSEO_HANDOVER_PLAN.md` | 2026-09-02. Claims the REVV network is live. Acceptance checkboxes are empty. No traffic export in the pack. |
| `INCIDENT_QUOTE_DELIVERY_FRIDAY_20260808.md` | Three Rivas/medical hostnames were HTTP 200 after docroots were created. SING LLC was not filed. |
| `crm.py`, `pseo_crm.py`, `land_pseo_v4.py` | Scripts. No lead store, no spend store, and no VDS run log shipped with them. |

## Standing order already in the files

Do not format the Orico drive. Do not delete `oricodrive`, `oricodrive_parts`, or the PC workspace copies. The 8 August Hermes note blocks that delete until a Proton verify exists. This pack does not contain that verify.

## Delivery to the VDS (this session)

| Check | Result |
|---|---|
| `GET /api/health` on host `zynclaw.fyi` via `5.189.143.170` | `{"status":"ok"}` |
| `GET /api/vds` | Hermes is boss. Advertised routes: `/api/health`, `/api/hermes/chat`, `/api/providers`, `/api/orchestrate` |
| `POST /api/hermes/chat` | `404 Not Found` |
| `POST /api/orchestrate` | `unauthorized origin` |
| `ssh root@5.189.143.170` | Permission denied (publickey). This session has no VDS key and no tailnet client. |

The cloud-agent session that opened this PR did not write the inbox: public SSH to `5.189.143.170` was denied. A later check from the Mac via `ssh vds` on 2026-10-03 found the relay already on the box: `/root/zynthio/inbox/maccy/INCIDENT_DRIVE_INACCESSIBLE_20261003.md` (795 bytes, mtime 2026-10-03 19:24:09 +0200). Its header says Devin on rubymcivor wrote it after the cloud agent could not.

## Report

```text
PASS: Uploaded handover pack read. Drive not opened. VDS HTTP health ok.
FAIL: Proton/Orico copy has no completion or checksum record in the pack.
BLOCKED: Operator cannot access the drive. Hermes chat route 404. Orchestrate rejected this origin. SSH has no key.
NOT VERIFIED: F: ORICO to Proton offsite. Parts af–ai. Suno catalogs. pgeoseo.com stub paste-back. REVV traffic. Any order or registry change after the file dates above.
Evidence: the uploaded file set listed in this incident. No drive path.
```

## What the VDS must not do

- Do not format Orico.
- Do not delete parts `aa`–`ai` or the PC `oricodrive` tree.
- Do not mark the Proton offsite copy done.
- Do not run a geo build from the v2 Nicaragua loader. The 9 September rule requires a country config first.

## Recheck 2026-10-04 (no drive, read-only)

Hermes health on the VDS was still `{"status":"ok"}` at 14:49 UTC. `POST /api/hermes/chat` is still not a working drop. Public HTTPS for several brand names stops on a Cloudflare "Just a moment" page, so those were checked on the origin with a Host header to `5.189.143.170`, which is the check the 8 August incident required.

| Host | Origin result |
|---|---|
| drdenislopez.com, acupunturarivas.com, orientalmedicina.com | HTTP 200. Title: Dr. Denis W. López — Medicina Oriental · Rivas. Same page on all three. |
| zynthio.ai | HTTP 200. Title: ZYNTHIO™ — Immutable memory for imperfect systems. |
| coreyai.ai | HTTP 200. Title: CoreyAI — AI Incident Intelligence. |
| songpal.ai | HTTP 301 to HTTPS. HTTPS origin title: SongPal — PenPal for Song. |
| revv.travel | HTTP 200. Title: REVV Travel — Motorcycles · Tours · Insurance · CRM. |
| crm.revv.travel | HTTPS origin body is the 17-byte text `REVV CRM endpoint`. `GET /api/revv/lead` returns 405. No lead was posted. |
| whymcycle.com | HTTP 200. Title: Why M Cycle — whymcycle.com. Fleet stub, not a question-pod article. |
| pgeoseo.com | HTTP 200. Real landing page, 5,460 bytes read, no `{{` and no `$d` in that body. |
| fishkillbraces.com | HTTP 200. Title: fishkillbraces.com — Braces in Fishkill, NY. H1: Braces in Fishkill. No raw placeholders in the first 7KB. |
| orthofishkill.com, lagrangevillebraces.com, wappingersfallsbraces.com | HTTP 200. Generic fleet titles (`Ortho Fish Kill — orthofishkill.com` and the same pattern). Not full builds. |
| drsyntax.com | HTTP 200. Title: Dr Syntax — drsyntax.com. Fleet stub. Empire 90-day content is not on this page. |
| nyhc.net | Public title was "Par Ked — parked". Origin on the VDS is the catch-all "You Little Dev — youlittledev.com", not an NYHC site. |

Drive state is unchanged: not mounted, not listed, not deleted.

## Recheck 2026-10-08 (JEV)

Typed verdict: `incidents/INCIDENT_2026-10-03_DRIVE_INACCESSIBLE.jev.json`. Schema `ops/guard/jev-schema.yaml` from `coreintentdev/coreintent`. Validator result: VALID. Judgment: `needs-evidence`. Confidence: 0.8.

Fresh reads at 15:44 UTC:

- `Host: zynclaw.fyi` `/api/health` and `/api/vds` return nginx HTML 404. The vhost root is a static page titled `WIKI — zynclaw.fyi (auto-audit 2026-08-19)`, Last-Modified 6 October 2026. The 4 October Hermes JSON health check is not current.
- `drdenislopez.com` HTTPS origin is now `WIKI — drdenislopez.com (auto-audit 2026-08-19)`, Last-Modified 6 October 2026. On 4 October this host served the Dr. Denis W. López page.
- `nyhc.net` and `fishkillbraces.com` HTTP origins are the same WIKI stub pattern, Last-Modified 6 October 2026.
- `pgeoseo.com` and `zynthio.ai` HTTPS origins still serve their earlier titles.
- `revv.travel` title is unchanged.

Hermes stays the fleet boss. This file does not mark the Proton copy done and does not approve a delete.

## What a later session with drive access must do first

1. Mount only. Do not delete.
2. List Proton for `zynthio_backup`, `mac-local`, `zynthio-tools`, and parts `af`–`ai`.
3. Compare sizes and checksums to the Orico side.
4. Paste the counts back. Only then is a delete even discussable.

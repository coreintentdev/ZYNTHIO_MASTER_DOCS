#!/usr/bin/env python3
"""Validate the documentation set without a human in the loop.

Checks the active risk config and that internal Markdown links resolve.
Exits 0 when the repo is consistent. Does not contact the network.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[2]
RISK = ROOT / "config" / "risk.yaml"
REQUIRED_SYMBOLS = ("BTC-PERP", "ETH-PERP", "SOL-PERP", "XAU-PERP", "XAG-PERP")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"FAIL {message}", file=sys.stderr)
    raise SystemExit(1)


def check_risk() -> None:
    if not RISK.is_file():
        fail(f"missing {RISK.relative_to(ROOT)}")
    data = yaml.safe_load(RISK.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("config/risk.yaml must be a mapping")
    if data.get("account_currency") != "USD":
        fail(f"account_currency is {data.get('account_currency')!r}")
    limits = data.get("limits")
    if not isinstance(limits, dict):
        fail("limits must be a mapping")
    expected = {
        "max_leverage": 5.0,
        "max_risk_per_trade_pct": 1.0,
        "max_daily_loss_pct": 0.8,
        "min_cash_reserve_usd": 350.0,
        "max_open_positions": 10,
    }
    for key, value in expected.items():
        if limits.get(key) != value:
            fail(f"limits.{key} is {limits.get(key)!r}, expected {value}")
    assets = data.get("assets")
    if not isinstance(assets, list):
        fail("assets must be a list")
    symbols = [item.get("symbol") if isinstance(item, dict) else None for item in assets]
    if symbols != list(REQUIRED_SYMBOLS):
        fail(f"assets are {symbols!r}")
    print(
        "risk-ok",
        f"leverage={limits['max_leverage']}",
        "symbols=" + ",".join(symbols),
    )


def check_links() -> None:
    missing: list[str] = []
    checked = 0
    for path in ROOT.rglob("*.md"):
        rel_parts = path.relative_to(ROOT).parts
        if any(part.startswith(".") for part in rel_parts):
            continue
        text = path.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.strip().strip("<>").split()[0]
            if target.startswith(("http://", "https://", "mailto:", "#")) or target in {"…", "..."}:
                continue
            path_part = unquote(target.partition("#")[0])
            if not path_part:
                continue
            resolved = (path.parent / path_part).resolve()
            checked += 1
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                missing.append(f"{path.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.is_file():
                missing.append(f"{path.relative_to(ROOT)} -> {target}")
    if missing:
        for item in missing:
            print(f"BROKEN {item}", file=sys.stderr)
        fail(f"{len(missing)} broken internal links")
    print(f"links-ok checked={checked}")


def main() -> None:
    check_risk()
    check_links()
    print("docs-check-ok")


if __name__ == "__main__":
    main()

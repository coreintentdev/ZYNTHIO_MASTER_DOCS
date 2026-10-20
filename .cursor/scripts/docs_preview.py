#!/usr/bin/env python3
"""Read-only HTML preview for ZYNTHIO_MASTER_DOCS.

Binds to 127.0.0.1:8080. Serves repository Markdown and YAML only.
Does not call external services.
"""

from __future__ import annotations

import html
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[2]
HOST = "127.0.0.1"
PORT = 8080
RISK_REL = Path("config/risk.yaml")

MD = markdown.Markdown(extensions=["extra", "toc", "sane_lists"])

CSS = """
:root { color-scheme: light; --bg:#f4f1ea; --ink:#1c1915; --muted:#5c564c; --card:#fffdf8; --line:#e4dccb; --accent:#6b3f1d; }
* { box-sizing: border-box; }
body { margin:0; font:16px/1.55 Palatino, Georgia, serif; color:var(--ink); background:var(--bg); }
header { padding:1.25rem 1.5rem; border-bottom:1px solid var(--line); background:var(--card); }
header a { color:inherit; text-decoration:none; }
header p { margin:0.2rem 0 0; color:var(--muted); font-family:ui-sans-serif, system-ui, sans-serif; font-size:0.85rem; }
.layout { display:grid; grid-template-columns: 280px 1fr; min-height: calc(100vh - 78px); }
nav { border-right:1px solid var(--line); padding:1rem; background:#faf7f1; overflow:auto; }
nav h2 { margin:1rem 0 0.35rem; font:600 0.72rem/1.2 ui-sans-serif, system-ui, sans-serif; letter-spacing:0.06em; text-transform:uppercase; color:var(--muted); }
nav a { display:block; color:var(--ink); text-decoration:none; padding:0.15rem 0; font-family:ui-sans-serif, system-ui, sans-serif; font-size:0.86rem; }
nav a:hover { color:var(--accent); }
main { padding:1.5rem 2rem 3rem; max-width: 920px; }
.card { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:1rem 1.1rem; margin:0 0 1.25rem; }
.card h2 { margin:0 0 0.6rem; font-size:1.15rem; }
table { border-collapse:collapse; width:100%; margin:0.8rem 0; }
th, td { border:1px solid var(--line); padding:0.4rem 0.6rem; text-align:left; vertical-align:top; }
th { background:#f3ecdf; }
code, pre { font-family:ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size:0.88rem; }
pre { background:#231e1a; color:#f6f1e7; padding:0.9rem 1rem; border-radius:8px; overflow:auto; }
code { background:#efe7d8; padding:0.05rem 0.3rem; border-radius:4px; }
pre code { background:transparent; padding:0; color:inherit; }
a { color:var(--accent); }
blockquote { margin:0.8rem 0; padding:0.2rem 0 0.2rem 0.9rem; border-left:3px solid #c4a574; color:var(--muted); }
img { max-width:100%; height:auto; }
@media (max-width: 800px) {
  .layout { display:flex; flex-direction:column; }
  main { order:1; padding:1rem; }
  nav { order:2; border-right:0; border-top:1px solid var(--line); max-height:240px; }
}
"""


def render_md(text: str) -> str:
    MD.reset()
    return MD.convert(text)


def safe_target(rel: str) -> Path | None:
    target = (ROOT / rel).resolve()
    if target != ROOT and ROOT not in target.parents:
        return None
    return target


def doc_groups() -> list[tuple[str, list[Path]]]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() not in {".md", ".yaml", ".yml"}:
            continue
        files.append(path)
    grouped: dict[str, list[Path]] = {}
    for path in sorted(files, key=lambda item: str(item.relative_to(ROOT)).lower()):
        rel = path.relative_to(ROOT)
        group = rel.parts[0] if len(rel.parts) > 1 else "Root"
        grouped.setdefault(group, []).append(path)
    order = ["Root", "brands", "avatars", "config", "deploy", "ops", "incidents"]
    names = [name for name in order if name in grouped] + sorted(set(grouped) - set(order))
    return [(name, grouped[name]) for name in names]


def nav_html() -> str:
    parts = ["<h2>Browse</h2>", '<a href="/">Home</a>', '<a href="/api/risk">Risk API</a>']
    for name, files in doc_groups():
        parts.append(f"<h2>{html.escape(name)}</h2>")
        for path in files:
            rel = path.relative_to(ROOT).as_posix()
            label = rel if name == "Root" else path.relative_to(ROOT).relative_to(name).as_posix()
            parts.append(f'<a href="/{html.escape(rel)}">{html.escape(label)}</a>')
    return "\n".join(parts)


def page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — ZYNTHIO Master Docs</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <a href="/"><strong>ZYNTHIO Master Docs</strong></a>
  <p>Local documentation preview</p>
</header>
<div class="layout">
  <nav>{nav_html()}</nav>
  <main>{body}</main>
</div>
</body>
</html>
"""


def load_risk() -> dict:
    data = yaml.safe_load((ROOT / RISK_REL).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("risk config must be a mapping")
    return data


def risk_card() -> str:
    try:
        data = load_risk()
    except Exception as exc:
        return (
            '<section class="card"><h2>Risk config</h2><p>Could not read '
            f"{html.escape(str(RISK_REL))}: {html.escape(str(exc))}</p></section>"
        )
    limits = data.get("limits") or {}
    rows = "".join(
        f"<tr><td><code>{html.escape(str(key))}</code></td><td>{html.escape(str(value))}</td></tr>"
        for key, value in limits.items()
    )
    symbols = "".join(
        f"<li><code>{html.escape(str(item.get('symbol', item)))}</code></li>"
        for item in (data.get("assets") or [])
    )
    currency = html.escape(str(data.get("account_currency", "")))
    return f"""
<section class="card">
  <h2>Active risk limits</h2>
  <p>Parsed from <a href="/config/risk.yaml">config/risk.yaml</a>. Account currency: <strong>{currency}</strong>.</p>
  <table>
    <thead><tr><th>Limit</th><th>Value</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <p>Tradable symbols</p>
  <ul>{symbols}</ul>
</section>
"""


def catalog() -> str:
    items = []
    for name, files in doc_groups():
        links = "".join(
            f'<li><a href="/{html.escape(path.relative_to(ROOT).as_posix())}">{html.escape(path.relative_to(ROOT).as_posix())}</a></li>'
            for path in files
        )
        items.append(f"<h2>{html.escape(name)}</h2><ul>{links}</ul>")
    return page("Home", risk_card() + "<h1>Documents</h1>" + "".join(items))


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        print(f"{self.address_string()} {fmt % args}", flush=True)

    def do_GET(self) -> None:
        path = unquote(urlparse(self.path).path)
        if path == "/health":
            self._send(200, b"ok\n", "text/plain; charset=utf-8")
            return
        if path == "/api/risk":
            try:
                payload = json.dumps(load_risk()).encode()
            except Exception as exc:
                self._send(500, json.dumps({"error": str(exc)}).encode(), "application/json")
                return
            self._send(200, payload, "application/json")
            return
        if path in ("/", "/index.html"):
            self._send(200, catalog().encode(), "text/html; charset=utf-8")
            return
        target = safe_target(path.lstrip("/"))
        if target is None or not target.is_file():
            self.send_error(404)
            return
        if target.suffix.lower() == ".md":
            body = render_md(target.read_text(encoding="utf-8"))
            title = target.relative_to(ROOT).as_posix()
            self._send(200, page(title, body).encode(), "text/html; charset=utf-8")
            return
        if target.suffix.lower() in {".yaml", ".yml"}:
            data = yaml.safe_load(target.read_text(encoding="utf-8"))
            pretty = html.escape(yaml.dump(data, sort_keys=False, allow_unicode=True))
            title = target.relative_to(ROOT).as_posix()
            body = f"<h1>{html.escape(title)}</h1><pre>{pretty}</pre>"
            self._send(200, page(title, body).encode(), "text/html; charset=utf-8")
            return
        self._send(200, target.read_bytes(), "text/plain; charset=utf-8")

    def _send(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    print(f"docs preview on http://{HOST}:{PORT}", flush=True)
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()

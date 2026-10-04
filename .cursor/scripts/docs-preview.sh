#!/usr/bin/env bash
# Read-only local preview of this documentation repo.
# Listens on 127.0.0.1:8080. Does not call external APIs.
set -euo pipefail
cd /workspace
if python3 -c 'import socket; s=socket.create_connection(("127.0.0.1", 8080), 2); s.close()' 2>/dev/null; then
  echo "docs preview already listening on 127.0.0.1:8080"
  exit 0
fi
exec python3 /workspace/.cursor/scripts/docs_preview.py

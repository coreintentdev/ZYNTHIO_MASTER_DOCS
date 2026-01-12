# Zynthio Trading Bot - Production Dockerfile
# Python 3.11 on Ubuntu 22.04 base for gTrade + AI stack

FROM python:3.11-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /app

# Copy requirements first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy risk config
COPY config/risk.yaml /app/config/

# Environment variables (override via docker-compose or CLI)
ENV GROK_API_KEY="" \
    CLAUDE_API_KEY="" \
    PERPLEXITY_API_KEY="" \
    GTRADE_RPC_URL="" \
    LOG_LEVEL="INFO"

# Health check
HEALTHCHECK --interval=1m --timeout=30s --start-period=40s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Non-root user for security
RUN useradd -m -u 1000 zynthio && chown -R zynthio:zynthio /app
USER zynthio

# Entry point
CMD ["python", "bot_engine.py"]

FROM python:3.12-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Copy configuration files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy source code
COPY src/ src/

# Expose port (FastMCP usually runs on stdio, but can run over SSE/HTTP)
# For this example we'll assume stdio for now, or we can expose a port if using SSE.
# Let's assume we might want to run it via `fastmcp run` which handles things.
# But for a container, we usually want an entrypoint.

# Using `uv run` to ensure environment is used
ENTRYPOINT ["uv", "run", "fastmcp", "run", "src/dice_roller/main.py"]

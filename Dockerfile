# Use official Python slim image (adjust version if pyproject.toml specifies otherwise)
FROM python:3.12-slim

# Install uv (the dependency manager used by this project)
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock src/ README.md .

# Install dependencies using uv
RUN uv sync

# Expose the MCP server port
EXPOSE 8000

# Run the application
CMD ["uv", "run", "python", "-m", "discord_mcp.main"]
"""Date tool for local MCP server."""

from datetime import datetime


def get_utc_date() -> str:
    """Return current UTC date."""
    return datetime.utcnow().strftime("%Y-%m-%d")

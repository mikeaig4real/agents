"""Local MCP server with modular tools."""

from mcp.server.fastmcp import FastMCP
from server_tools.date_tool import get_utc_date
from server_tools.headline_tool import build_headline

server = FastMCP("Mikeaig4realLocalMCP")


@server.tool()
def utc_date() -> str:
    """Expose UTC date tool."""
    return get_utc_date()


@server.tool()
def topic_headline(topic: str) -> str:
    """Expose topic headline tool."""
    return build_headline(topic)


if __name__ == "__main__":
    server.run(transport="stdio")

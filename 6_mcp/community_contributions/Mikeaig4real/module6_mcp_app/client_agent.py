"""MCP client agent runner for module 6 app."""

from agents import Agent, Runner
from agents.mcp import MCPServerStdio


async def run_mcp_prompt(prompt: str) -> str:
    """Run an agent with tools from the local MCP server."""
    async with MCPServerStdio(
        name="local_mcp",
        params={
            "command": "python",
            "args": ["6_mcp/community_contributions/Mikeaig4real/module6_mcp_app/server.py"],
        },
    ) as mcp_server:
        agent = Agent(
            name="MCP Tool User",
            instructions=(
                "Use available MCP tools to answer the request. "
                "If topic is provided, call topic_headline. Also include utc_date output."
            ),
            mcp_servers=[mcp_server],
            model="gpt-4o-mini",
        )
        result = await Runner.run(agent, prompt)
        return str(result.final_output)

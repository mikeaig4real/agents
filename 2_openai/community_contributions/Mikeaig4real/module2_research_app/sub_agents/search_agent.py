"""Search sub-agent."""

from agents import Agent, WebSearchTool

search_agent = Agent(
    name="Search Specialist",
    instructions="Use web search and return concise factual notes with links.",
    tools=[WebSearchTool()],
    model="gpt-4o-mini",
)

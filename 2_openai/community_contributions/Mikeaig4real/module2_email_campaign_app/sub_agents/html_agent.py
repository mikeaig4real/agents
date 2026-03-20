"""HTML conversion agent."""

from agents import Agent

html_agent = Agent(
    name="HTML Agent",
    instructions="Convert plain text email content into simple production-ready HTML.",
    model="gpt-4o-mini",
)

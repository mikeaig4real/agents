"""Email subject optimizer."""

from agents import Agent

subject_agent = Agent(
    name="Subject Agent",
    instructions="Create one high-conversion subject line for the provided cold email body.",
    model="gpt-4o-mini",
)

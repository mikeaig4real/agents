"""Dry-run send agent."""

from agents import Agent

send_agent = Agent(
    name="Send Agent",
    instructions=(
        "Prepare a dry-run send confirmation. Include recipient, subject, and send status. "
        "Do not claim real delivery."
    ),
    model="gpt-4o-mini",
)

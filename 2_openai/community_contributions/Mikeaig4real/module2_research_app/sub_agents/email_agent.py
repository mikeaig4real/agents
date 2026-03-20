"""Email sub-agent."""

from agents import Agent

email_agent = Agent(
    name="Email Summarizer",
    instructions="Write a short status email with topic, 3 bullets, and next steps.",
    model="gpt-4o-mini",
)

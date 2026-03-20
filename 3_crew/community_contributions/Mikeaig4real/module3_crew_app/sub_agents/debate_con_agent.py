"""Debate con-role agent factory."""

from crewai import Agent


def build_debate_con_agent(topic: str) -> Agent:
    """Create con-side debate agent."""
    return Agent(
        role="Con Analyst",
        goal=f"Argue against premature adoption of: {topic}",
        backstory="You identify operational and strategic risk early.",
        verbose=False,
    )

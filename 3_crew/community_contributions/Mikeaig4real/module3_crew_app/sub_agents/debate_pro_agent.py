"""Debate pro-role agent factory."""

from crewai import Agent


def build_debate_pro_agent(topic: str) -> Agent:
    """Create pro-side debate agent."""
    return Agent(
        role="Pro Analyst",
        goal=f"Argue in favor of: {topic}",
        backstory="You prioritize practical upside and delivery outcomes.",
        verbose=False,
    )

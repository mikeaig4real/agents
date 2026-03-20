"""Debate moderator agent factory."""

from crewai import Agent


def build_debate_moderator_agent() -> Agent:
    """Create debate moderator agent."""
    return Agent(
        role="Moderator",
        goal="Synthesize both sides and provide a balanced recommendation.",
        backstory="You produce concise decision memos for leaders.",
        verbose=False,
    )

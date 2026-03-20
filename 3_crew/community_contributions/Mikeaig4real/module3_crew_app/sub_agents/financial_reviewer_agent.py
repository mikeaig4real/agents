"""Financial reviewer agent factory."""

from crewai import Agent


def build_financial_reviewer_agent() -> Agent:
    """Create portfolio reviewer agent."""
    return Agent(
        role="Portfolio Reviewer",
        goal="Give a balanced recommendation and risk controls.",
        backstory="You avoid overconfident conclusions.",
        verbose=False,
    )

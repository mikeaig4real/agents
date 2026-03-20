"""Financial fundamental agent factory."""

from crewai import Agent


def build_financial_fundamental_agent() -> Agent:
    """Create fundamental analyst agent."""
    return Agent(
        role="Fundamental Analyst",
        goal="Compare growth, profitability, and valuation tradeoffs.",
        backstory="You prioritize transparent assumptions.",
        verbose=False,
    )

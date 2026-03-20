"""Financial market agent factory."""

from crewai import Agent


def build_financial_market_agent(universe: str) -> Agent:
    """Create market researcher agent."""
    return Agent(
        role="Market Researcher",
        goal=f"Summarize macro and sector context for: {universe}",
        backstory="You produce concise market context with caveats.",
        verbose=False,
    )

"""Engineering QA agent factory."""

from crewai import Agent


def build_engineering_qa_agent() -> Agent:
    """Create QA lead agent."""
    return Agent(
        role="QA Lead",
        goal="Define acceptance criteria and key edge cases.",
        backstory="You prevent production regressions with precise test planning.",
        verbose=False,
    )

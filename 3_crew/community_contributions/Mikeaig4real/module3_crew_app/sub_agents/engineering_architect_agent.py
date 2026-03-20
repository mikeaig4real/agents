"""Engineering architect agent factory."""

from crewai import Agent


def build_engineering_architect_agent(problem: str) -> Agent:
    """Create software architect agent."""
    return Agent(
        role="Software Architect",
        goal=f"Design a robust implementation for: {problem}",
        backstory="You design practical systems with clear boundaries.",
        verbose=False,
    )

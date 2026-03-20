"""Engineering delivery agent factory."""

from crewai import Agent


def build_engineering_delivery_agent() -> Agent:
    """Create delivery manager agent."""
    return Agent(
        role="Delivery Manager",
        goal="Create a sprint-ready delivery plan.",
        backstory="You convert technical plans into actionable milestones.",
        verbose=False,
    )

"""Planner sub-agent."""

from agents import Agent
from sub_agents.schemas import SearchPlan

planner_agent = Agent(
    name="Search Planner",
    instructions=(
        "Break user requests into 3-5 focused searches with a reason per query."
    ),
    output_type=SearchPlan,
    model="gpt-4o-mini",
)

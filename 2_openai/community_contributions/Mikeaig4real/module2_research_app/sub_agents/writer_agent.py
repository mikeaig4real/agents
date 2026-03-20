"""Writer sub-agent."""

from agents import Agent
from sub_agents.schemas import ReportData

writer_agent = Agent(
    name="Report Writer",
    instructions="Convert search notes into a structured markdown report.",
    output_type=ReportData,
    model="gpt-4o-mini",
)

"""Converged lead agent built from module 2 sub-agents."""

from agents import Agent
from sub_agents.planner_agent import planner_agent
from sub_agents.search_agent import search_agent
from sub_agents.writer_agent import writer_agent
from sub_agents.email_agent import email_agent

planner_tool = planner_agent.as_tool(
    tool_name="planner_agent",
    tool_description="Create a search plan for the topic.",
)

search_tool = search_agent.as_tool(
    tool_name="search_agent",
    tool_description="Research one search item and return notes.",
)

writer_tool = writer_agent.as_tool(
    tool_name="writer_agent",
    tool_description="Write a final markdown report from notes.",
)

email_tool = email_agent.as_tool(
    tool_name="email_agent",
    tool_description="Write a concise summary email from the report.",
)

lead_research_agent = Agent(
    name="Research Lead",
    instructions=(
        "Use planner_agent to create a plan, use search_agent for each plan item, "
        "use writer_agent for final report, then use email_agent for summary. "
        "Return markdown with sections: Status, Summary Email, and Report."
    ),
    tools=[planner_tool, search_tool, writer_tool, email_tool],
    model="gpt-4o-mini",
)

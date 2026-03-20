"""Converged lead agent for module 2 email campaign flow."""

from agents import Agent
from sub_agents.serious_sales_agent import serious_sales_agent
from sub_agents.engaging_sales_agent import engaging_sales_agent
from sub_agents.concise_sales_agent import concise_sales_agent
from sub_agents.subject_agent import subject_agent
from sub_agents.html_agent import html_agent
from sub_agents.send_agent import send_agent

serious_tool = serious_sales_agent.as_tool(
    tool_name="serious_sales_agent",
    tool_description="Generate a serious-tone structured cold email.",
)

engaging_tool = engaging_sales_agent.as_tool(
    tool_name="engaging_sales_agent",
    tool_description="Generate an engaging-tone structured cold email.",
)

concise_tool = concise_sales_agent.as_tool(
    tool_name="concise_sales_agent",
    tool_description="Generate a concise-tone structured cold email.",
)

subject_tool = subject_agent.as_tool(
    tool_name="subject_agent",
    tool_description="Generate an optimized subject line for the selected email draft.",
)

html_tool = html_agent.as_tool(
    tool_name="html_agent",
    tool_description="Convert selected email text into HTML.",
)

send_tool = send_agent.as_tool(
    tool_name="send_agent",
    tool_description="Prepare a dry-run send confirmation.",
)

email_campaign_manager_agent = Agent(
    name="Email Campaign Manager",
    instructions=(
        "Generate 3 draft options by calling serious_sales_agent, engaging_sales_agent, and concise_sales_agent. "
        "Pick one best draft for the user prompt, generate a subject with subject_agent, "
        "create HTML with html_agent, then call send_agent for a dry-run send result. "
        "Return a markdown response with sections: Winning Tone, Subject, Email Body, Dry Run Result."
    ),
    tools=[serious_tool, engaging_tool, concise_tool, subject_tool, html_tool, send_tool],
    model="gpt-4o-mini",
)

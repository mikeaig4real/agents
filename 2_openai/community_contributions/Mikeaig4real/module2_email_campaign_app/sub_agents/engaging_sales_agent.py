"""Engaging-tone sales email generator."""

from agents import Agent
from sub_agents.schemas import EmailDraft

engaging_sales_agent = Agent(
    name="Engaging Sales Agent",
    instructions=(
        "Write an engaging, human-sounding cold email for a SOC2 compliance SaaS offer. "
        "Return structured output with tone='engaging'."
    ),
    output_type=EmailDraft,
    model="gpt-4o-mini",
)

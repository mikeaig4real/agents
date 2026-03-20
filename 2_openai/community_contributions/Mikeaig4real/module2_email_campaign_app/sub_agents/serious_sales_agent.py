"""Serious-tone sales email generator."""

from agents import Agent
from sub_agents.schemas import EmailDraft

serious_sales_agent = Agent(
    name="Serious Sales Agent",
    instructions=(
        "Write a professional, direct cold email for a SOC2 compliance SaaS offer. "
        "Return structured output with tone='serious'."
    ),
    output_type=EmailDraft,
    model="gpt-4o-mini",
)

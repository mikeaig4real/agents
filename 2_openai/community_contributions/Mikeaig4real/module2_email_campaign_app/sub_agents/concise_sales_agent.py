"""Concise-tone sales email generator."""

from agents import Agent
from sub_agents.schemas import EmailDraft

concise_sales_agent = Agent(
    name="Concise Sales Agent",
    instructions=(
        "Write a short and clear cold email for a SOC2 compliance SaaS offer. "
        "Return structured output with tone='concise'."
    ),
    output_type=EmailDraft,
    model="gpt-4o-mini",
)

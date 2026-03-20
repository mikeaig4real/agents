"""Execution manager for module 2 email campaign app."""

from agents import Runner, trace, gen_trace_id
from lead_agent import email_campaign_manager_agent


class EmailCampaignManager:
    """Runs the converged campaign manager agent."""

    async def run(self, prompt: str):
        """Stream trace link and final campaign output."""
        trace_id = gen_trace_id()
        with trace("module2_email_campaign", trace_id=trace_id):
            yield f"Trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            yield "Running campaign manager..."
            result = await Runner.run(email_campaign_manager_agent, prompt)
            yield str(result.final_output)

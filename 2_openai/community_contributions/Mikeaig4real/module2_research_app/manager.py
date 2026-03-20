"""Research orchestration for the Module 2 app."""

from agents import Runner, trace, gen_trace_id
from lead_agent import lead_research_agent


class ResearchManager:
    """Runs a single converged lead agent and streams status."""

    async def run(self, query: str):
        """Run lead agent and stream trace plus final markdown."""
        trace_id = gen_trace_id()
        with trace("module2_research", trace_id=trace_id):
            yield f"Trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            yield "Running lead agent..."
            result = await Runner.run(lead_research_agent, query)
            yield str(result.final_output)

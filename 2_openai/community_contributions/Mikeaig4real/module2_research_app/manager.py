"""Research orchestration for the Module 2 app."""

import asyncio
from agents import Runner, trace, gen_trace_id

from agents import (
    planner_agent,
    search_agent,
    writer_agent,
    email_agent,
    SearchQuery,
    SearchPlan,
    ReportData,
)


class ResearchManager:
    """Coordinates planning, search, writing, and summary steps."""

    async def run(self, query: str):
        """Stream step-by-step status and final report markdown."""
        trace_id = gen_trace_id()
        with trace("module2_research", trace_id=trace_id):
            yield f"Trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            plan = await self.plan_searches(query)
            yield f"Planned {len(plan.searches)} searches"
            notes = await self.perform_searches(plan.searches)
            yield "Search phase complete"
            report = await self.write_report(query, notes)
            yield "Report complete"
            summary = await self.create_summary_email(report.markdown_report)
            yield "Summary email draft complete"
            yield f"## Summary Email\n\n{summary}\n\n---\n\n{report.markdown_report}"

    async def plan_searches(self, query: str) -> SearchPlan:
        result = await Runner.run(planner_agent, f"Topic: {query}")
        return result.final_output_as(SearchPlan)

    async def perform_searches(self, searches: list[SearchQuery]) -> list[str]:
        tasks = [asyncio.create_task(self.search_once(item)) for item in searches]
        results: list[str] = []
        for task in asyncio.as_completed(tasks):
            text = await task
            if text:
                results.append(text)
        return results

    async def search_once(self, search: SearchQuery) -> str | None:
        prompt = f"Query: {search.query}\nReason: {search.reason}"
        try:
            result = await Runner.run(search_agent, prompt)
            return str(result.final_output)
        except Exception:
            return None

    async def write_report(self, query: str, notes: list[str]) -> ReportData:
        payload = f"User query: {query}\nSearch notes: {notes}"
        result = await Runner.run(writer_agent, payload)
        return result.final_output_as(ReportData)

    async def create_summary_email(self, report_markdown: str) -> str:
        result = await Runner.run(email_agent, report_markdown)
        return str(result.final_output)

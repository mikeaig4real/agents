"""Agent definitions for the Module 2 research app."""

from pydantic import BaseModel
from agents import Agent, WebSearchTool


class SearchQuery(BaseModel):
    """A single planned search item."""

    query: str
    reason: str


class SearchPlan(BaseModel):
    """Planner output with search items."""

    searches: list[SearchQuery]


class ReportData(BaseModel):
    """Writer output schema."""

    short_summary: str
    markdown_report: str


planner_agent = Agent(
    name="Search Planner",
    instructions=(
        "Break the user request into 3-5 focused searches. "
        "Avoid duplicate queries and include a clear reason for each query."
    ),
    output_type=SearchPlan,
    model="gpt-4o-mini",
)

search_agent = Agent(
    name="Search Specialist",
    instructions=(
        "Use web search to gather factual, current information. "
        "Return concise notes with source links when available."
    ),
    tools=[WebSearchTool()],
    model="gpt-4o-mini",
)

writer_agent = Agent(
    name="Report Writer",
    instructions=(
        "Write a complete markdown report using the search notes. "
        "Include a short summary and a clear section structure."
    ),
    output_type=ReportData,
    model="gpt-4o-mini",
)

email_agent = Agent(
    name="Email Summarizer",
    instructions=(
        "Create a concise status email from the report. "
        "The email must include: topic, 3 bullets, and next steps."
    ),
    model="gpt-4o-mini",
)

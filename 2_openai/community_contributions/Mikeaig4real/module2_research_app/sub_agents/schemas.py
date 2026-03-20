"""Shared schemas for module 2 sub-agents."""

from pydantic import BaseModel


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

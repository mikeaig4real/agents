"""Schemas for the module 2 email campaign workflow."""

from typing import Literal
from pydantic import BaseModel, Field


class EmailDraft(BaseModel):
    """Structured cold-email draft."""

    tone: Literal["serious", "engaging", "concise"]
    subject: str = Field(min_length=8, max_length=120)
    body: str = Field(min_length=120)
    cta: str = Field(min_length=8, max_length=120)


class SendPayload(BaseModel):
    """Message envelope for a send operation."""

    to: str
    subject: str
    html_body: str

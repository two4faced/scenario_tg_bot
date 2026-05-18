from datetime import datetime

from pydantic import BaseModel, Field


class RequestAddScreenplayDTO(BaseModel):
    title: str = Field(max_length=75)
    logline: str | None = Field(max_length=40)


class AddScreenplayDTO(RequestAddScreenplayDTO):
    author_id: int
    redacted_at: datetime


class ScreenplayDTO(AddScreenplayDTO):
    id: int

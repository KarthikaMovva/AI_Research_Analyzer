from pydantic import BaseModel
from typing import TypedDict

class ResearchRequest(BaseModel):
    query: str

class ResearchResponse(BaseModel):
    report: str


class ResearchState(TypedDict):

    query: str

    plan: str

    research: str

    critique: str

    report: str

    sources: list[str]
from typing import TypedDict

class ResearchState(TypedDict):
    query: str
    plan: str
    notes: str
    feedback: str
    report: str
    retry_count: int
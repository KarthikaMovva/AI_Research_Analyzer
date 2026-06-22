from fastapi import APIRouter

from api.schemas import (
    ResearchRequest,
    ResearchResponse
)

from graph.workflow import graph

router = APIRouter()

@router.post(
    "/research",
    response_model=ResearchResponse
)
def generate_report(
    request: ResearchRequest
):

    result = graph.invoke(
        {
            "query": request.query,
            "retry_count": 0
        }
    )

    return ResearchResponse(
        report=result["report"]
    )
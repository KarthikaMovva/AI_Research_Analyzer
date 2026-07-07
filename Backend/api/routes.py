import os
import shutil

from agents.query_router import classify_query
from llm.router import generate

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from api.schemas import (
    ResearchRequest,
    ResearchResponse
)

from graph.workflow import graph

from rag.ingestion import build_vector_store

router = APIRouter()


@router.post(
    "/research",
    response_model=ResearchResponse
)
def generate_report(request: ResearchRequest):


    query_type = classify_query(
        request.query
    )


    if query_type == "simple":

        answer = generate(
            f"""
            Answer the question in 2-3 lines.

            Question:
            {request.query}
            """
        )


        return ResearchResponse(
            report=answer
        )


    result = graph.invoke({

        "query": request.query,

    })


    return ResearchResponse(

        report=result["report"]

    )


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    upload_folder = "uploads"

    os.makedirs(
        upload_folder,
        exist_ok=True
    )


    file_path = os.path.join(
        upload_folder,
        file.filename
    )


    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    chunks = build_vector_store(
        file_path
    )


    return {

        "message": "Knowledge Base Updated",

        "filename": file.filename,

        "chunks_added": chunks
    }






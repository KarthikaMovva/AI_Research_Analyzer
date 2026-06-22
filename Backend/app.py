from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="AI Research Analyzer"
)

app.include_router(router)
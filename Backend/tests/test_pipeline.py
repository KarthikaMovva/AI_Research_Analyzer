from orchestrator.pipeline import run_pipeline

report = run_pipeline(
    "Compare RAG, Self-RAG and GraphRAG"
)

print(report)
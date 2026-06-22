from graph.workflow import graph

result = graph.invoke(
    {
        "query":
        "Compare RAG, Self-RAG and GraphRAG"
    }
)

print(
    result["report"]
)
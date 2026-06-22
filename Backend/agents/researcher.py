from rag.retriever import retrieve

def research_agent(task, vector_store):

    docs = retrieve(
        vector_store,
        task
    )

    return "\n".join(
        [doc.page_content for doc in docs]
    )
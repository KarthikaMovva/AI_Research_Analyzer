from rag.retriever import retrieve

def research_agent(task):

    docs = retrieve(task)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context
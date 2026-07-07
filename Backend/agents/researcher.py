from rag.retriever import retrieve


def researcher_agent(query):

    results = retrieve(query)

    context = "\n\n".join(
        item["content"]
        for item in results
    )

    sources = []

    for item in results:

        sources.append(
            f'{item["source"]} (Page {item["page"]})'
        )

    return {
        "research": context,
        "sources": sources
    }
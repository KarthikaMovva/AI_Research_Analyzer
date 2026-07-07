def classify_query(query):

    short_keywords = [
        "define",
        "definition",
        "what is",
        "explain briefly",
        "meaning",
        "2 lines",
        "3 lines",
        "short"
    ]


    query_lower = query.lower()


    for keyword in short_keywords:

        if keyword in query_lower:
            return "simple"


    return "research"
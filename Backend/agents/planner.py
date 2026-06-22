from llm.router import generate

def planner_agent(user_query):

    prompt = f"""
    You are a planning agent.

    Break the user's request into research tasks.

    User Query:
    {user_query}

    Return only numbered tasks.
    """

    return generate(prompt)

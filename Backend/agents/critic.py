from llm.router import generate

def critic_agent(notes):

    prompt = f"""
    Review this research.

    {notes}

    Find missing information.
    """

    return generate(prompt)
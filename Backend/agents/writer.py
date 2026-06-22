from llm.router import generate

def writer_agent(content):

    prompt = f"""
    Create a professional report.

    {content}
    """

    return generate(prompt)
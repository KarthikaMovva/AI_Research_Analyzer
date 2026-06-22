from llm.router import generate
from agents.prompts import WRITER_PROMPT

def writer_agent(notes):

    prompt = WRITER_PROMPT.format(
        notes=notes
    )

    return generate(prompt)
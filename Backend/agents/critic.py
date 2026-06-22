from llm.router import generate
from agents.prompts import CRITIC_PROMPT

def critic_agent(notes):

    prompt = CRITIC_PROMPT.format(
        notes=notes
    )

    return generate(prompt)
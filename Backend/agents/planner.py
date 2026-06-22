from llm.router import generate
from agents.prompts import PLANNER_PROMPT

def planner_agent(query):

    prompt = PLANNER_PROMPT.format(
        query=query
    )

    return generate(prompt)
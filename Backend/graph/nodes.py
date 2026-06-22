from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.critic import critic_agent
from agents.writer import writer_agent

def planner_node(state):

    plan = planner_agent(
        state["query"]
    )

    return {
        "plan": plan
    }

def researcher_node(state):

    tasks = state["plan"].split("\n")

    notes = []

    for task in tasks:

        task = task.strip()

        if not task:
            continue

        notes.append(
            research_agent(task)
        )

    return {
        "notes": "\n\n".join(notes),

        "retry_count":
            state.get(
                "retry_count",
                0
            ) + 1
    }

def critic_node(state):

    feedback = critic_agent(
        state["notes"]
    )

    return {
        "feedback": feedback
    }

def writer_node(state):

    report = writer_agent(
        state["notes"]
    )

    return {
        "report": report
    }

def route_after_critic(state):

    feedback = state["feedback"]

    retries = state.get(
        "retry_count",
        0
    )

    if retries >= 2:
        return "writer"

    if "DECISION: RESEARCH" in feedback:
        return "researcher"

    return "writer"

from pydantic import annotated_handlers
from pydantic import annotated_handlers
from agents.planner import planner_agent
from agents.researcher import researcher_agent
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

    sources = []


    for task in tasks:

        task = task.strip()

        if not task:
            continue


        result = researcher_agent(task)


        notes.append(
            result["research"]
        )


        sources.extend(
            result["sources"]
        )
        print(type(notes))
        print(notes)

    return {

        "notes": "\n\n".join(notes),

        "sources": sources,

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

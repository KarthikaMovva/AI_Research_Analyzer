from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.critic import critic_agent
from agents.writer import writer_agent

def run_pipeline(query):

    print("\nPlanning...\n")

    plan = planner_agent(query)

    print(plan)

    notes = []

    tasks = plan.split("\n")

    for task in tasks:

        task = task.strip()

        if not task:
            continue

        research = research_agent(task)

        notes.append(research)

    combined_notes = "\n\n".join(notes)

    print("\nCritiquing...\n")

    feedback = critic_agent(
        combined_notes
    )

    print(feedback)

    print("\nWriting Report...\n")

    final_report = writer_agent(
        combined_notes
    )

    return final_report
from langgraph.graph import StateGraph, START, END

from graph.state import ResearchState

from graph.nodes import (
    planner_node,
    researcher_node,
    critic_node,
    writer_node,
    route_after_critic
)

builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("researcher", researcher_node)
builder.add_node("critic", critic_node)
builder.add_node("writer", writer_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "critic")
builder.add_conditional_edges(
    "critic",
    route_after_critic,
    {
        "researcher": "researcher",
        "writer": "writer"
    }
)
builder.add_edge("writer", END)

graph = builder.compile()
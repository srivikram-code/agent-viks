"""Step B: the same chains, now wrapped as LangGraph nodes.

    START -> classify_task -> analyze_priority -> END
"""

import sys
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from chains import classify_chain, priority_chain

DEFAULT_TASK = "I need to prepare for my Java interview tomorrow."


# 1. State: the shared data every node can read and update.
class TaskState(TypedDict, total=False):
    task: str
    category: str
    priority: str


# 2. Nodes: plain functions. They get the state and return only the keys they change.
def classify_task(state: TaskState) -> dict:
    category = classify_chain.invoke({"task": state["task"]}).strip()
    return {"category": category}


def analyze_priority(state: TaskState) -> dict:
    # Reads `category`, which Node 1 wrote into the state.
    priority = priority_chain.invoke(
        {"task": state["task"], "category": state["category"]}
    ).strip()
    return {"priority": priority}


# 3. Edges: the order the nodes run in.
def build_graph():
    graph = StateGraph(TaskState)
    graph.add_node("classify_task", classify_task)
    graph.add_node("analyze_priority", analyze_priority)

    graph.add_edge(START, "classify_task")
    graph.add_edge("classify_task", "analyze_priority")
    graph.add_edge("analyze_priority", END)
    return graph.compile()


def main() -> None:
    task = " ".join(sys.argv[1:]) or DEFAULT_TASK
    app = build_graph()
    result = app.invoke({"task": task})

    print(f"Task:     {result['task']}")
    print(f"Category: {result['category']}")
    print(f"Priority: {result['priority']}")


if __name__ == "__main__":
    main()

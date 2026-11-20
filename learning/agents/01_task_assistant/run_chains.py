"""Step A: run the two chains by hand, one after another. No LangGraph yet."""

import sys

from chains import classify_chain, priority_chain

DEFAULT_TASK = "I need to prepare for my Java interview tomorrow."


def main() -> None:
    task = " ".join(sys.argv[1:]) or DEFAULT_TASK

    # We pass data between steps ourselves.
    category = classify_chain.invoke({"task": task}).strip()
    priority = priority_chain.invoke({"task": task, "category": category}).strip()

    print(f"Task:     {task}")
    print(f"Category: {category}")
    print(f"Priority: {priority}")


if __name__ == "__main__":
    main()

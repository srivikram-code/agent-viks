# 01 · Task Assistant

You type a task, and the assistant tells you its **Category** and **Priority**.

| File | What it shows |
|---|---|
| `chains.py` | Two one-way LangChain chains: `prompt \| llm \| parser` |
| `run_chains.py` | **Step A:** calls the chains one after another, with no graph |
| `main.py` | **Step B:** the same chains used as LangGraph nodes |

```
START → classify_task → analyze_priority → END
```

## Setup (one time, run from `learning/agents/`)
```bash
python -m venv .venv
```
```bash
source .venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
cp .env.example .env
```
Then put your `GOOGLE_API_KEY` and `LANGSMITH_API_KEY` in `.env`.

## Run
```bash
python 01_task_assistant/run_chains.py
```
```bash
python 01_task_assistant/main.py "Pay electricity bill by Friday"
```

Expected output for the default task:
```
Category: Learning
Priority: High
```

Each run shows up as a trace in LangSmith, in the project `learn-langgraph`.

## Concepts
- **State:** `TaskState` holds the data all nodes share.
- **Node:** a function that reads the state and returns the keys it updates.
- **Edge:** `add_edge` sets the order the nodes run in.
- **Passing data:** `analyze_priority` reads the `category` that `classify_task` wrote.
- **Reuse:** the chains are unchanged. LangGraph only adds the state and the flow.

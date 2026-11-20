# 02 · Travel Assistant (coming next)

Example request: "Plan a 2-day trip to Ooty within ₹10,000."

```
Supervisor → [Travel | Hotel | Budget] (parallel) → Reviewer ─┬→ Final Plan
                    ↑──────── over budget? loop back ─────────┘
```

New concepts: multiple agents, shared state, conditional routing, parallel nodes and loops.

---
id: "0103"
title: "Add concurrency locks around InputBuffer and GhostManager to ensure thread safety"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Reliable backend operation under concurrent requests"
accept: "pytest tests/test_input_buffer.py"
---

The backend code currently uses threading.Lock for scores and pellets data, but InputBuffer and GhostManager are accessed without locks. This can cause race conditions if accessed concurrently by multiple requests or threads.

Proposed fix:
- Add threading.Lock or other concurrency control around InputBuffer methods.
- Add threading.Lock or concurrency control around GhostManager state updates.
- Review all accesses to these shared objects for thread safety.

Steps to reproduce:
- Run concurrent requests that modify input buffer or ghost states.
- Observe potential race conditions or inconsistent states.

Expected:
- Thread-safe access to InputBuffer and GhostManager.

Actual:
- No concurrency control, risking race conditions.

Labels: bug
Objective: "Reliable backend operation under concurrent requests"
Accept: pytest tests/test_input_buffer.py

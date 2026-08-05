---
id: "0063"
title: "Bug: Missing src.backend.ghosts module causing import errors and test failures"
type: "bug"
status: "done"
assignee: ""
labels: "bug"
due: "2026-08-10"
created: "2026-08-04"
updated: "2026-08-05"
objective: "Implement ghost visual identifiers and state logic"
accept: "pytest -q tests/test_ghost_visuals.py"
resolution: "duplicate of #0060"
---

The tests for ghost visual identifiers and state logic fail due to missing module 'src.backend.ghosts'. This blocks verification of bug #0050 fix and prevents running acceptance tests.

Steps to reproduce:
- Run pytest on tests/test_ghost_visuals.py or other tests importing src.backend.ghosts

Expected:
- Module src.backend.ghosts exists and is importable

Actual:
- ImportError: No module named 'src.backend.ghosts'

This bug blocks release and must be fixed immediately.

**2026-08-05 18:50** — closed as a duplicate of #0060: same work, filed more than once

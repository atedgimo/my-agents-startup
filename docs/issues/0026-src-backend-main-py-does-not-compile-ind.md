---
id: "0026"
title: "src/backend/main.py does not compile: IndentationError line 22"
type: "bug"
status: "in-progress"
assignee: "startup-senior-dev"
labels: "bug,backend"
due: "2026-08-03"
created: "2026-08-02"
updated: "2026-08-02"
started: "2026-08-02T17:31:26"
---

The release is blocked. src/backend/main.py fails to parse:
  IndentationError: unexpected indent (main.py, line 22)
A SQL CREATE TABLE block is indented incorrectly.

Run check_syntax to see it. Fix the indentation with write_repo_file, then run check_syntax again and confirm it reports no errors before moving this card.

Expected: python -m py_compile passes and the deployed pod starts. Actual: the pod crash-loops on import.

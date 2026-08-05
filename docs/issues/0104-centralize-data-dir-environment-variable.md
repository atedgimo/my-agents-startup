---
id: "0104"
title: "Centralize DATA_DIR environment variable reading and file path handling"
type: "feature"
status: "backlog"
assignee: ""
labels: "refactor"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Consistent and maintainable environment configuration handling"
accept: "pytest"
---

The DATA_DIR environment variable is read separately in src/backend/main.py and src/backend/pellet_collection.py, leading to duplication and potential inconsistencies.

Proposed fix:
- Centralize DATA_DIR reading and validation in a single module or configuration.
- Use pathlib.Path for file path handling for clarity and cross-platform compatibility.
- Refactor pellet_collection.py and main.py to use centralized configuration.

Steps to reproduce:
- Check DATA_DIR usage in main.py and pellet_collection.py.

Expected:
- Single source of truth for DATA_DIR and file paths.

Actual:
- Duplicate code reading and validating DATA_DIR.

Labels: refactor
Objective: "Consistent and maintainable environment configuration handling"
Accept: pytest

---
id: "0054"
title: "DevOps: Ensure backend test environment installs requirements.txt dependencies"
type: "feature"
status: "backlog"
assignee: ""
labels: "devops"
due: ""
created: "2026-08-04"
updated: "2026-08-04"
objective: "Bug #0050 acceptance test requires pytest to be installed and runnable in the backend environment."
accept: "pytest -q tests/test_ghost_visuals.py"
---

Acceptance tests for backend cards fail because pytest is not found, even though it is listed in src/backend/requirements.txt. This indicates the test environment does not install backend dependencies before running tests.

Task: Fix the CI/test environment setup to install dependencies from src/backend/requirements.txt before running backend tests, so pytest and other dependencies are available.

This is blocking acceptance testing and release for backend cards that require pytest.

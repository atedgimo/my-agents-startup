---
id: "0108"
title: "Bug: Test suite times out after 180 seconds blocking regression verification"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Regression tests run and pass to unblock release"
accept: "pytest tests/ -q --maxfail=20 | tee result.log | tail -40 | grep -v 'timeout'"
---

The automated test suite repeatedly times out after 180 seconds without producing failure details. This prevents regression verification and blocks the quality gate for release.

Steps to reproduce:
1. Run `pytest tests/ -q --maxfail=20` or the equivalent test command.
2. Observe the timeout after 180 seconds with no detailed failure output.

Actual: Test suite times out, no failure details.
Expected: Test suite completes or fails with detailed output to identify regressions.

This blocks the release until resolved.

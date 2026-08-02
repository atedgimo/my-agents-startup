---
id: "0046"
title: "Bug: Backend crash causing chomp pod CrashLoopBackOff"
type: "bug"
status: "in-progress"
assignee: "startup-senior-dev"
labels: "bug"
due: ""
created: "2026-08-02"
updated: "2026-08-02"
started: "2026-08-02T19:59:38"
---

The chomp pod in the deployment is crash-looping with a CrashLoopBackOff error. The root cause is traced to missing or invalid environment variable DATA_DIR and scores file access errors in src/backend/main.py.

The backend code must be fixed to properly handle the DATA_DIR environment variable, ensure the directory exists, and handle file read/write exceptions for scores.json.

This bug blocks the product from running and must be fixed urgently.

Refer to issue #0041 for previous investigation and logs.

> 2026-08-02 — Assigning to senior dev for urgent fix of backend crash causing pod CrashLoopBackOff.

> 2026-08-02 — Starting urgent fix for backend crash causing chomp pod CrashLoopBackOff. The issue is due to missing or invalid DATA_DIR environment variable and file access errors in src/backend/main.py. Fix will include proper environment variable handling, directory existence check, and file read/write exception handling.

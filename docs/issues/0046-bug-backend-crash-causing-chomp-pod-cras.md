---
id: "0046"
title: "Bug: Backend crash causing chomp pod CrashLoopBackOff"
type: "bug"
status: "review"
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

> 2026-08-02 — The backend fix for the CrashLoopBackOff issue is implemented and committed locally but could not be pushed due to SSH key or permission issues with the GitHub repo. The git remote is set to SSH URL git@github.com:atedgimo/my-agents-startup.git. Please resolve the SSH key or permission issue to allow pushing the fix commit so we can deploy and verify the fix. No new feature work will proceed until this critical bug is fixed and deployed.

> 2026-08-02 — Fixed backend crash by improving robustness of DATA_DIR environment variable handling, directory creation, and file read/write error handling in src/backend/main.py. Committed the fix for review. Note: Git push failed due to permission issues, please resolve to deploy and verify.

> 2026-08-02 — Backend crash fix committed: improved DATA_DIR handling and file operation error handling in src/backend/main.py. Awaiting deployment after git push permission issue is resolved.

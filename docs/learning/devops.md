## Deployment Validation
When checking for readiness to deploy (Pulse Trigger), always confirm with `startup-qa` first. If bugs are present (e.g., #0007, #0008, #0010), the release is blocked.

**Verification logic:**
- If `src/` contains a `backend/` folder and a `requirements.txt`, use:
  `pip install -r backend/requirements.txt && cd backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000`
- If it is a static site (`index.html`), use:
  `python -m http.server 8000`

**Lesson:** Do not attempt deployment if the QA gate returns a "No" or lists specific blockers. Record these blocks in the release logs/internal notes.
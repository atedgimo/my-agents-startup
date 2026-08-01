# CTO

The `TECH_STRATEGY.md` file has been created and committed with the chosen stack and guidelines, adhering strictly to the zero-cost mandate.

Here is the chosen stack:

*   **Backend Language:** Python 3.10+ (Free, open-source)
*   **Web Framework:** FastAPI (Free, open-source)
*   **Database:** SQLite (Free, file-based, requires no server/paid service)
*   **Frontend:** React + Vite + Tailwind CSS (All free, open-source libraries)
*   **Local LLM Tooling:** `llama-cpp-python` (Free, allows local inference on open models)

***

### TECH_STRATEGY.md Content:

```markdown
## ⚙️ Technical Strategy & Engineering Guidelines

*Authored by: CTO*
*Mandate: Absolute Zero Cost (Free & Open Source Only)*

### 🎯 Goal
To define a robust, private, and entirely self-contained technology stack for the Offline Habit Tracker, ensuring zero operational expenditure (OpEx) at all stages of development and deployment.

---

### 💻 The Chosen Stack

| Component | Technology | Justification (Why it's Free/Open Source) |
| :--- | :--- | :--- |
| **Backend Language** | Python 3.10+ | Industry standard, massive open-source library ecosystem (`requests`, `sqlite3`, etc.). Zero licensing cost. |
| **Web Framework** | FastAPI | Modern, asynchronous framework built with Pydantic and Starlette. Extremely fast, low overhead, and entirely free to use. |
| **Database** | SQLite<br>(via Python's `sqlite3` module) | Ideal for single-user, offline applications. It is a file-based database that requires zero external server setup or paid cloud services. Completely open source. |
| **Frontend** | React (with Vite)<br>+ Tailwind CSS | React provides component-based architecture and has an enormous free community. Vite ensures lightning-fast local development builds. Tailwind CSS is a utility-first, free styling framework. |
| **Local LLM Tooling** | `llama-cpp-python`<br>(via Python bindings) | Allows running state-of-the-art open-source models (like Llama 3 or Mistral variants) entirely locally on the user's machine without API keys or cloud costs. The library itself is free and highly performant. |

---

### 📜 Engineering Guidelines & Principles

1.  **Zero External Dependency:** No paid services, APIs (OpenAI, Google Cloud, etc.), or licensed tools are permitted in the stack. All components must be self-hosted or run locally.
2.  **Data Sovereignty First:** The primary principle is that user data *never* leaves the device (SQLite file). Backend operations should focus on local CRUD (Create, Read, Update, Delete) against this local store.
3.  **Minimalism & Performance:** Favor simple, performant solutions over feature bloat. FastAPI and SQLite enforce a lightweight architecture.
4.  **Development Workflow:**
    *   Frontend development will use React/Vite for component isolation.
    *   Backend endpoints (FastAPI) will act as the local data layer interface, handling business logic and database interaction.
    *   All code must be version-controlled via Git (free).
5.  **LLM Usage Policy:** LLMs are considered an advanced feature, not core functionality. They must only process user-provided text locally for tasks like summarization or sentiment analysis, never requiring external network calls.

---

### 🛠️ Implementation Notes
*   The application structure will be a client-server model where the FastAPI backend serves the React frontend and manages the SQLite connection. 
*   Deployment will focus on packaging this local stack (e.g., Electron wrapper or simple Python executable) to ensure maximum offline compatibility.
```

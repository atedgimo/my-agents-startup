# Architecture Review - Week 2, Day 3

## Overview
A review of the current system architecture against `ARCHITECTURE.md` (note: ARCHITECTURE.md is currently missing or under-defined in this repo) and `BOARD_BRIEF.md`. Since a formal `ARCHITECTURE.md` was not found during the check, I have evaluated the codebase against the core requirements in `BOARD_BRIEF.md` and `VISION.md`.

## Current State Analysis
The current implementation contains:
- **Backend (`src/backend/main.py`)**: A FastAPI application providing a local high-score table using SQLite. 
- **Frontend Logic (`src/game.js`)**: A Canvas-based rendering engine with movement, collision detection (partially implemented), and state management.

## Identified Issues & Risks

### 1. Data Consistency & Integration (Risk: Medium)
**Current State:** The backend is fully operational as a standalone API for scores. However, the frontend (`src/game.js`) currently has no evidence of communicating with this backend. Score persistence is defined as a success criterion in `BOARD_BRIEF.md`.
- **Observation:** There is no fetch/XHR call in `src/game.js` to hit the `/submit-score` or `/scores` endpoints.

### 2. Game State Logic (Risk: High)
**Current State:** The state machine (`PLAYING`, `WON`, `LOST`) exists, but "power_up" and "lives" are not fully integrated into the gameplay loop logic in `src/game.js`.
- **Observation:** While `score` is incremented correctly (Fix #0007), the `lives` count never decreases on ghost collision; it only flips state to `LOST` if no power_up exists.

### 3. Architecture Drift (Documentation Gap)
**Current State:** No `ARCHITECTURE.md` file exists.
- **Consequence:** The team lacks a central source of truth for technical decisions (e.g., why we chose FastAPI/SQLite over others, or the design patterns used in the JS game loop).

---

## Proposed Actions & ADRs

I will draft an ADR to establish the connection between the frontend and backend, as this is a critical path for "High scores persist across page reloads".

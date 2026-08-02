## [Feature] Implement Player Movement and Collision Detection

**Labels:** feature

**Due:** 2026-08-15

### Context
The current frontend renders the maze and pellets (as seen in #0003), but there is no interactivity yet. This issue focuses on making Pac-Man moveable within those bounds.

### Requirements / Acceptance Criteria
1. **Input Handling:** Map arrow keys (Up, Down, Left, Right) to movement.
2. **Collision Detection:** Implement wall collision logic so the player cannot pass through walls in the maze.
3. **Core Movement:** Smooth movement of the "Pac-Man" character in the game world.
4. **Metric moved:** Directly impacts OKR Q3: Gameplay Mechanics (KR1).

### Technical Notes
- Check `src/game.js` for existing entity definitions.
- Ensure collision detection is efficient enough to maintain 60 FPS.

---

## [Feature] Implement Pellet Collection and Scoring

**Labels:** feature

**Due:** 2026-08-20

### Context
While movement is the first step, players need to interact with the environment. This task implements the collection of pellets to update the player's score and decrement the remaining pellet count.

### Requirements / Acceptance Criteria
1. **Collision Detection (Pellets):** Detect when Pac-Man's coordinates overlap with a pellet's location.
2. **Scoring System:** Increment the user's score by a fixed amount upon pellet consumption.
3. **State Update:** Remove the collected pellet from the game state so it doesn't reappear.
4. **Metric moved:** Directly impacts OKR Q3: Gameplay Mechanics (KR1).

---

## [Feature] Implement Game Loop & Win/Loss Logic

**Labels:** feature

**Due:** 2026-08-25

### Context
Once the player can move and collect pellets, the game needs a state machine to handle winning (all pellets collected), losing (collision with ghost without power-pellet), and level resets/restarts.

### Requirements / Acceptance Criteria
1. **Win Condition:** Check if all pellet items have been "consumed". If so, display a 'Level Clear' message.
2. **Loss Condition:** Detect collision between player and ghost while the 'power_up' state is inactive. Trigger a 'Game Over' screen.
3. **State Management:** Implement clear states (PLAYING, WON, LOST) to manage UI overlays and gameplay suspension.
4. **Metric moved:** Directly impacts OKR Q3: Gameplay Mechanics (KR1).

---

## Bug: Missing scoring increment for pellet collection

**Labels:** bug

The 'Scoring' component of this task is incomplete. While a `score` variable exists in `src/game.js`, there is no logic implemented to increment it when pellets are collected. 

**Expected:** Score increases upon pellet collection.
**Actual:** Score remains at 0 regardless of game actions.

---

## Bug: Missing implementation for Collision/Loss detection logic

**Labels:** bug

The 'Loss' condition logic in `#0006` is currently only a comment in `src/game.js`. No actual collision detection or state transition to `STATE.LOST` is implemented beyond the visual overlay check.

**Expected:** Game should transition to LOST if player hits ghost (without power_up).
**Actual:** State remains PLAYING until all pellets are collected, unless manually set (not possible via current code).

---

## Feature: Implement Motion Interpolation

**Labels:** feature

### Value Case
**Who benefits:** Both casual players and retro-gaming fans.
**What metric moves:** User satisfaction/retention by providing a "high-quality" feel.
**Description:** 
Implement a decoupled rendering system where the game logic remains on a discrete grid (for easy collision detection), but the visual representation interpolates between positions. This prevents the "teleporting" look of basic clones and provides the smooth movement expected in high-quality arcade games.

---

## game.js wrapped in Python triple quotes - frontend fails to parse

**Labels:** bug

**Description:**
The frontend fails to load because `src/game.js` is wrapped in Python triple quotes (three double-quote characters) at the beginning and end of the file.

**Actual behavior:**
The first line starts with `"""` and the last line ends with `"""`. The browser cannot parse this as valid JavaScript, resulting in a blank page or a console error before anything renders.

**Expected behavior:**
The file should contain only raw JavaScript code, starting directly with variable declarations (e.g., `const canvas = ...`) and ending with executable statements, without any surrounding markers or quotes.

**Steps to Reproduce:**
1. Open the application in a browser.
2. Observe that nothing renders on the screen.
3. Inspect source: the file contains triple quotes at boundaries.

---

## [Feature] Implement Player Movement Kinematics

**Labels:** feature

Implement the core movement logic for the player character, focusing on transforming input into kinematics.

- Map keyboard inputs (Arrow keys/WASD) to a normalized direction vector.
- Implement a velocity system where input influences a position update over time.
- Ensure smooth transition between directions.
- Note: This task does NOT include wall collision; it assumes an open field.

---

## [part] #0004.1 Tile-Based Collision Logic

**Labels:** none

**Due:** 2026-08-10

Sub-task of #0004. Implement tile-based collision logic to check if a player's movement overlaps with maze walls.
Acceptance Criteria:
1. Player cannot move into wall tiles.
2. Movement is rejected if it crosses a boundary.
Size: S

---

## [part] #0004.2 Input Buffer & Movement Smoothing

**Labels:** none

**Due:** 2026-08-12

Sub-task of #0004. Implement an input buffer and a state-based movement system for smooth transitions between turns.
Acceptance Criteria:
1. Input is queued correctly.
2. Movement transition from one direction to another feels fluid (not instantaneous 'snap' when possible).
Size: M

---

## [part] #0004.3 Boundary Enforcement

**Labels:** none

**Due:** 2026-08-14

Sub-task of #0004. Ensure player cannot "jitter" or phase through corners by implementing stricter grid-aligned movement constraints.
Acceptance Criteria:
1. Player remains in the center of the tile during turn transitions.
2. No 'corner cutting' is possible unless explicitly allowed by game logic.
Size: S

---

## [part] #0006.1 Core Game Loop & State Machine

**Labels:** none

**Due:** 2026-08-17

Sub-task of #0006. Implement a centralized loop that manages states: START_MENU, PLAYING, PAUSED, GAME_OVER.
Acceptance Criteria:
1. Clear state transitions between menu and game.
2. Game pause/unpause functionality works.
Size: M

---

## [part] #0006.2 Win/Loss Condition Check

**Labels:** none

**Due:** 2026-08-19

Sub-task of #0006. Logic to detect when all pellets are gone (Win) or when a ghost collision occurs without a power pellet active (Loss).
Acceptance Criteria:
1. Win state triggered correctly by pellet count.
2. Loss state triggered on collision without power_pellet flag.
Size: M

---

## [part] #0006.3 UI State Overlay Integration

**Labels:** none

**Due:** 2026-08-21

Sub-task of #0006. Coordinate with the frontend to trigger overlays (e.g., "You Win!" or "Game Over") based on state changes in the logic engine.
Acceptance Criteria:
1. UI displays win/loss messages appropriately.
2. Transition back to start menu after game over is functional.
Size: S

---

## [part] #0005.1 Pellet Collection Logic

**Labels:** none

**Due:** 2026-08-13

Sub-task of #0005. The mechanics of detecting a pellet's coordinates during a move, removing it from the active_pellets array, and updating local score variables.
Acceptance Criteria:
1. Pellet collision detection is consistent with movement.
2. Score increments correctly on valid capture.
Size: S

---

## [part] #0005.2 Score Persistence & Sync

**Labels:** none

**Due:** 2026-08-14

Sub-task of #0005. Bridging the gap between the game's current score and the backend API to ensure that "High Scores" are updated correctly in the database upon a win/loss event.
Acceptance Criteria:
1. Score data is sent to the /high-scores endpoint (or equivalent) on completion.
2. Persistence is verified after refresh.
Size: M

---

## Feature: Implement Ghost Visual Identifiers & State Logic

**Labels:** feature

**Due:** 2026-08-15

### Value Case
Target Audience: **Retro-Gaming Fans**
Metric: Engagement & Polish.
By giving each ghost a distinct color (Red, Pink, Cyan, Orange) and a 'scared' visual state when `power_up` is active, we fulfill the requirement for "distinct behaviors" in a way that makes it visually obvious to players who care about the mechanics.

### Tasks
- Assign unique colors/shades to each of the 4 ghost types based on their movement logic.
- Implement a visual change (e.g., turning gray or blue) when `power_up` is true.
- Update `src/game.js` to handle these color shifts in the drawing loop.

---

## Feature: Ghost Identity & State Visuals

**Labels:** feature

**Due:** 2026-08-15

### Value Case
**Target Audience:** Retro-Gaming Fans & Casual Players.
**Metric:** Polish / Engagement.
**Reasoning:** By assigning unique colors to each ghost behavior and a "scared" state, we satisfy the requirement for distinct behaviors while providing necessary visual feedback in place of audio (which is out of scope).

### Tasks
- Define a color palette for the 4 ghosts (Chase, Ambish, Patrol, Random) in `src/game.js`.
- Implement logic to change ghost colors and add a "pulse" effect when `power_up` is true.
- Update the drawing loop to render these states correctly.

---

## Feature: Visual Juice & Feedback Mechanisms

**Labels:** feature

**Due:** 2026-08-15

### Value Case
**Target Audience:** Casual Players.
**Metric:** User Retention/Retention of Flow.
**Reasoning:** Since audio is forbidden, visual "pops" and a "glow" on the player are essential to communicate state changes (like power-ups) and successful interactions (eating pellets). This ensures the game feels responsive and polished without adding complex mechanics.

### Tasks
- Implement a "pulse" effect or frame-buffer for pellet collection in `src/game.js`.
- Add a visual indicator (aura/outline) around the player when `power_up` is true.

---

## Feature: Enhanced Game State Overlays

**Labels:** feature

**Due:** 2026-08-15

### Value Case
**Target Audience:** Casual Players.
**Metric:** Engagement / Clarity of State.
**Reasoning:** The vision emphasizes a "no-frills" but high-quality experience. Enhancing the end-game states makes the 3-minute loop feel like a complete cycle, highlighting the persistent scores which is the primary way players stay engaged after one run.

### Tasks
- Refine `STATE.WON` and `STATE.LOST` rendering in `src/game.js`.
- Center high-contrast text and include final score vs highest known record.
- Add a 'pause' or transition effect when shifting states to mimic arcade cabinet behavior.

---

## feat: integrate frontend with backend for score persistence

**Labels:** none

The frontend (`src/game.js`) currently does not make any network requests to the backend. To meet the requirement of "High scores persist across page reloads," we need a bridge between the game loop and the FastAPI server.

**Plan:**
1. Define an API client or a simple fetch wrapper in `src/game.js`.
2. Connect the `score` variable update to a call to `/submit-score`.
3. Optionally, load initial high scores on page load using `/scores`.

---

## Deployment crash-loops: backend/main.py exists but backend/requirements.txt does not

**Labels:** bug,deployment

**Due:** 2026-08-03

The first release attempt deployed but the pod crash-looped 6 times.

Reproduction: DevOps ran the FastAPI start command 'pip install -r backend/requirements.txt && cd backend && python -m uvicorn main:app'. The pod logs show:
  ERROR: Could not open requirements file: No such file or directory: backend/requirements.txt

src/ currently contains: index.html, game.js, backend/main.py — a half-built backend with no dependency manifest.

Decide and fix ONE of these:
(a) Chomp is a static browser game: delete src/backend/ and serve with python -m http.server, or
(b) the backend is real (high scores API): write src/backend/requirements.txt listing fastapi and uvicorn, and make sure main.py runs.

Expected: the deployed pod reaches Ready and serves the game. Actual: CrashLoopBackOff.

---

## src/backend/main.py does not compile: IndentationError line 22

**Labels:** bug,backend

**Due:** 2026-08-03

The release is blocked. src/backend/main.py fails to parse:
  IndentationError: unexpected indent (main.py, line 22)
A SQL CREATE TABLE block is indented incorrectly.

Run check_syntax to see it. Fix the indentation with write_repo_file, then run check_syntax again and confirm it reports no errors before moving this card.

Expected: python -m py_compile passes and the deployed pod starts. Actual: the pod crash-loops on import.

---


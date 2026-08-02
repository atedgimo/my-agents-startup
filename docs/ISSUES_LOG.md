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


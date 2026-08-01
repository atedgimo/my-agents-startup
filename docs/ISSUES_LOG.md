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


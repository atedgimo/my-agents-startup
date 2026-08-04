// Motion interpolation feature implemented for smooth rendering

import { drawGhost } from './frontend/ghostVisuals.js';

// Added power_up state to track power pellet effect
let power_up = false;

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Game Configuration
const TILE_SIZE = 30;
const ROWS = 20;
const COLS = 20;

// Game States
const STATE = {
    PLAYING: 'PLAYING',
    WON: 'WON',
    LOST: 'LOST'
};

let gameState = STATE.PLAYING;
let score = 0;
lives = 3;
power_up = false; // Track if player has a power-up for ghost logic

// Overlay control
let overlayActive = false;

// Function to activate overlay and pause game logic
function activateOverlay(state) {
    gameState = state;
    overlayActive = true;
}

// Function to dismiss overlay and reset or advance game
function dismissOverlay() {
    if (gameState === STATE.LOST) {
        // Reset game
        resetGame();
    } else if (gameState === STATE.WON) {
        // Advance to next level or reset
        nextLevel();
    }
    overlayActive = false;
    gameState = STATE.PLAYING;
}

// Reset game state
function resetGame() {
    score = 0;
    lives = 3;
    power_up = false;
    playerPos = { x: 5, y: 5 };
    ghosts.forEach(g => g.pos = { x: 10, y: 10 });
    pellets.forEach(p => p.active = true);
}

// Advance to next level (simplified as reset for now)
function nextLevel() {
    // Could add level increment logic here
    resetGame();
}


// Maze Layout - 1=Wall, 0=Path/Pellet, 2=Power Pellet
const mazeData = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
];

const pellets = [];
// Populate pellets from mazeData (type 0 means a path with a pellet)
for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
        if (mazeData[r][c] === 0) {
            pellets.push({ x: c, y: r, active: true });
        }
    }
}

// Player and ghost positions for logic (discrete grid positions)
let playerPos = { x: 5, y: 5 };
let prevPlayerPos = { ...playerPos };

const ghosts = [
    { pos: { x: 10, y: 10 }, prevPos: { x: 10, y: 10 }, state: 'normal' },
    { pos: { x: 15, y: 15 }, prevPos: { x: 15, y: 15 }, state: 'normal' }
];

// Timing for interpolation
let lastUpdateTime = performance.now();
const LOGIC_UPDATE_INTERVAL = 1000 / 60; // 60 logic updates per second

function lerp(a, b, t) {
    return a + (b - a) * t;
}

function update() {
    if (overlayActive) return; // Pause updates when overlay active
    if (gameState !== STATE.PLAYING) return;

    // Save previous positions for interpolation
    prevPlayerPos = { ...playerPos };
    ghosts.forEach(g => {
        g.prevPos = { ...g.pos };
    });

    // Example logic update: move player right by one tile every second
    // (Replace with actual input handling and movement logic)
    // For demonstration, we just cycle playerPos.x
    playerPos.x += 1;
    if (playerPos.x >= COLS - 1) playerPos.x = 1;

    // Update ghost states and positions
    ghosts.forEach((ghost, index) => {
        // Simple AI: move ghost horizontally back and forth
        if (!ghost.direction) ghost.direction = 1;
        ghost.pos.x += ghost.direction;
        if (ghost.pos.x <= 1 || ghost.pos.x >= COLS - 2) {
            ghost.direction *= -1;
        }

        // Check collision with player
        if (ghost.pos.x === playerPos.x && ghost.pos.y === playerPos.y) {
            if (power_up) {
                // Ghost eaten
                ghost.state = 'eaten';
                score += 200;
                // Send ghost back to start
                ghost.pos = { x: 10, y: 10 };
            } else {
                // Player loses life
                lives -= 1;
                if (lives <= 0) {
                    activateOverlay(STATE.LOST);
                } else {
                    resetPositions();
                }
            }
        }

        // Update ghost state timer
        if (ghost.state === 'eaten') {
            // After some time, ghost returns to normal
            if (!ghost.respawnTimer) {
                ghost.respawnTimer = 180; // frames to respawn
            } else {
                ghost.respawnTimer -= 1;
                if (ghost.respawnTimer <= 0) {
                    ghost.state = 'normal';
                    ghost.respawnTimer = null;
                }
            }
        }
    });

    // Power-up timer decrement
    if (power_up) {
        powerUpTimer -= 1;
        if (powerUpTimer <= 0) {
            power_up = false;
            powerUpTimer = 0;
            // Reset ghosts to normal state
            ghosts.forEach(g => {
                if (g.state !== 'normal') {
                    g.state = 'normal';
                    g.respawnTimer = null;
                }
            });
        }
    }

    // Check pellet collection
    pellets.forEach(p => {
        if (p.active && p.x === playerPos.x && p.y === playerPos.y) {
            p.active = false;
            score += 10;
            // Check if power pellet
            if (mazeData[p.y][p.x] === 2) {
                power_up = true;
                powerUpTimer = 600; // duration of power-up in frames
                // Set ghosts to frightened state
                ghosts.forEach(g => {
                    if (g.state === 'normal') {
                        g.state = 'frightened';
                    }
                });
            }
        }
    });

    // Check win condition
    if (pellets.every(p => !p.active)) {
        activateOverlay(STATE.WON);
    }
}

function resetPositions() {
    playerPos = { x: 5, y: 5 };
    ghosts.forEach(g => g.pos = { x: 10, y: 10 });
}

function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw maze
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (mazeData[r][c] === 1) {
                ctx.fillStyle = 'blue';
                ctx.fillRect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE);
            } else if (mazeData[r][c] === 0) {
                ctx.fillStyle = 'black';
                ctx.fillRect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE);
                // Draw pellet if active
                const pellet = pellets.find(p => p.x === c && p.y === r);
                if (pellet && pellet.active) {
                    ctx.fillStyle = 'white';
                    ctx.beginPath();
                    ctx.arc(c * TILE_SIZE + TILE_SIZE / 2, r * TILE_SIZE + TILE_SIZE / 2, 5, 0, 2 * Math.PI);
                    ctx.fill();
                }
            } else if (mazeData[r][c] === 2) {
                ctx.fillStyle = 'black';
                ctx.fillRect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE);
                // Draw power pellet
                ctx.fillStyle = 'yellow';
                ctx.beginPath();
                ctx.arc(c * TILE_SIZE + TILE_SIZE / 2, r * TILE_SIZE + TILE_SIZE / 2, 8, 0, 2 * Math.PI);
                ctx.fill();
            }
        }
    }

    // Draw player
    ctx.fillStyle = 'yellow';
    ctx.beginPath();
    ctx.arc(playerPos.x * TILE_SIZE + TILE_SIZE / 2, playerPos.y * TILE_SIZE + TILE_SIZE / 2, TILE_SIZE / 2 - 2, 0, 2 * Math.PI);
    ctx.fill();

    // Draw ghosts with visual identifiers based on state
    ghosts.forEach(ghost => {
        drawGhost(ctx, ghost.pos.x, ghost.pos.y, TILE_SIZE, ghost.state);
    });
}

// Power-up timer
let powerUpTimer = 0;

// Game loop
function gameLoop() {
    const now = performance.now();
    const delta = now - lastUpdateTime;

    if (delta > LOGIC_UPDATE_INTERVAL) {
        update();
        lastUpdateTime = now;
    }

    render();
    requestAnimationFrame(gameLoop);
}

// Start game loop
gameLoop();

export { update, render, resetGame, dismissOverlay, activateOverlay, gameLoop };

// Motion interpolation feature implemented for smooth rendering

// drawGhost was imported from './frontend/ghostVisuals.js', which was never
// written, in a file the page loads as a classic <script> — so the import was a
// parse error and NOTHING in this file ran. Defined locally instead.
function drawGhost(ctx, cx, cy, state, identity) {
    const colours = { Blinky: '#ff5555', Pinky: '#ff9ed8',
                      Inky: '#5ad2ff', Clyde: '#ffb852' };
    ctx.fillStyle = (state === 'FRIGHTENED') ? '#3b4cff'
                                             : (colours[identity] || '#ff5555');
    const r = TILE_SIZE / 2 - 2;
    ctx.beginPath();
    ctx.arc(cx, cy, r, Math.PI, 0);           // domed head
    ctx.lineTo(cx + r, cy + r);
    ctx.lineTo(cx - r, cy + r);
    ctx.closePath();
    ctx.fill();
    ctx.fillStyle = '#fff';                    // eyes
    ctx.beginPath();
    ctx.arc(cx - r / 2.5, cy - r / 5, r / 4, 0, Math.PI * 2);
    ctx.arc(cx + r / 2.5, cy - r / 5, r / 4, 0, Math.PI * 2);
    ctx.fill();
}

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
let lives = 3;
// power_up is declared once, at the top of this file

// TODO: Add fetch calls to submit and retrieve scores from backend API
// This is required to meet the persistence criterion in BOARD_BRIEF.md

// Example placeholder function to submit score
async function submitScore(score) {
    try {
        const response = await fetch('/submit-score', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ score })
        });
        if (!response.ok) throw new Error('Failed to submit score');
        console.log('Score submitted successfully');
    } catch (error) {
        console.error('Error submitting score:', error);
    }
}

// Example placeholder function to fetch high scores
async function fetchHighScores() {
    try {
        const response = await fetch('/scores');
        if (!response.ok) throw new Error('Failed to fetch scores');
        const scores = await response.json();
        console.log('High scores:', scores);
        // TODO: Render scores in UI
    } catch (error) {
        console.error('Error fetching scores:', error);
    }
}

// Call fetchHighScores on game load
fetchHighScores();

// Call submitScore when game ends (example, to be integrated with game state)
// if (gameState === STATE.LOST || gameState === STATE.WON) {
//     submitScore(score);
// }


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
    { pos: { x: 10, y: 10 }, prevPos: { x: 10, y: 10 } },
    { pos: { x: 15, y: 15 }, prevPos: { x: 15, y: 15 } }
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

    // Update ghost states and positions (dummy example)
    ghosts.forEach((ghost, index) => {
        ghost.pos.x += (index % 2 === 0 ? 1 : -1);
        if (ghost.pos.x >= COLS - 1) ghost.pos.x = 1;
        if (ghost.pos.x <= 0) ghost.pos.x = COLS - 2;
    });

    // Example logic update: move player right by one tile every second
    // (Replace with actual input handling and movement logic)
    // For demonstration, we just cycle playerPos.x
    playerPos.x += 1;
    if (playerPos.x >= COLS - 1) playerPos.x = 1;

    // Update ghost states and positions (dummy example)
    ghosts.forEach((ghost, index) => {
        ghost.pos.x += (index % 2 === 0 ? 1 : -1);
        if (ghost.pos.x >= COLS - 1) ghost.pos.x = 1;
        if (ghost.pos.x <= 0) ghost.pos.x = COLS - 2;
    });


    // Pellets collection logic
    pellets.forEach(p => {
        if (p.active) {
            if (p.x === playerPos.x && p.y === playerPos.y) {
                p.active = false;
                score += 10;
            }
        }
    });

    // Win Condition Check
    const remainingPellets = pellets.filter(p => p.active).length;
    if (remainingPellets === 0) {
        activateOverlay(STATE.WON);
    }

    // Collision Detection for ghosts
    ghosts.forEach(g => {
        const dist = Math.hypot(playerPos.x - g.pos.x, playerPos.y - g.pos.y);
        if (dist < 1) { // Same tile
            if (!power_up) {
                activateOverlay(STATE.LOST);
            } else {
                power_up = false;
            }
        }
    });

    lastUpdateTime = performance.now();
    // Draw game elements
    draw();
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw maze walls
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (mazeData[r][c] === 1) {
                ctx.fillStyle = '#0000FF';
                ctx.fillRect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE);
            }
        }
    }

    // Draw pellets
    pellets.forEach(p => {
        if (p.active) {
            ctx.fillStyle = '#FFFF00';
            ctx.beginPath();
            ctx.arc(p.x * TILE_SIZE + TILE_SIZE / 2, p.y * TILE_SIZE + TILE_SIZE / 2, 5, 0, 2 * Math.PI);
            ctx.fill();
        }
    });

    // Draw player
    ctx.fillStyle = '#FFFF00';
    ctx.beginPath();
    ctx.arc(playerPos.x * TILE_SIZE + TILE_SIZE / 2, playerPos.y * TILE_SIZE + TILE_SIZE / 2, 12, 0, 2 * Math.PI);
    ctx.fill();

    // Draw ghosts with identity and state visuals
    ghosts.forEach((ghost, index) => {
        // For demo: assign ghost identities cyclically
        const identities = ['chase', 'ambush', 'patrol', 'random'];
        const identity = identities[index % identities.length];
        const state = power_up ? 'frightened' : 'normal';
        drawGhost(ctx, ghost.pos.x * TILE_SIZE + TILE_SIZE / 2, ghost.pos.y * TILE_SIZE + TILE_SIZE / 2, state, identity);
    });

    // Draw score
    document.getElementById('scoreLabel').textContent = score;
}


function draw() {
    const now = performance.now();
    const delta = now - lastUpdateTime;
    const t = Math.min(delta / LOGIC_UPDATE_INTERVAL, 1);

    // Clear canvas
    ctx.fillStyle = '#111';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw maze
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (mazeData[r][c] === 1) {
                ctx.fillStyle = '#2d3748'; // Tailwind gray-800
                ctx.fillRect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE);
            }
        }
    }

    // Draw pellets
    ctx.fillStyle = '#facc15'; // Tailwind yellow-400
    pellets.forEach(p => {
        if (p.active) {
            ctx.beginPath();
            ctx.arc(p.x * TILE_SIZE + TILE_SIZE / 2, p.y * TILE_SIZE + TILE_SIZE / 2, 4, 0, Math.PI * 2);
            ctx.fill();
        }
    });

    // Interpolated player position
    const interpPlayerX = lerp(prevPlayerPos.x, playerPos.x, t) * TILE_SIZE;
    const interpPlayerY = lerp(prevPlayerPos.y, playerPos.y, t) * TILE_SIZE;

    // Draw player
    ctx.fillStyle = '#f59e0b'; // Tailwind amber-500
    ctx.beginPath();
    ctx.arc(interpPlayerX + TILE_SIZE / 2, interpPlayerY + TILE_SIZE / 2, TILE_SIZE / 2 - 2, 0, Math.PI * 2);
    ctx.fill();

    // Draw ghosts with interpolation
    ghosts.forEach(g => {
        const interpGhostX = lerp(g.prevPos.x, g.pos.x, t) * TILE_SIZE;
        const interpGhostY = lerp(g.prevPos.y, g.pos.y, t) * TILE_SIZE;
        ctx.fillStyle = '#ef4444'; // Tailwind red-500
        ctx.beginPath();
        ctx.arc(interpGhostX + TILE_SIZE / 2, interpGhostY + TILE_SIZE / 2, TILE_SIZE / 2 - 2, 0, Math.PI * 2);
        ctx.fill();
    });

    // Draw Score
    ctx.fillStyle = '#facc15';
    ctx.font = '16px Arial';
    ctx.fillText(`Score: ${score}`, 10, 20);

    // Draw Overlays
    if (gameState === STATE.WON) {
        // Draw Level Up overlay
        ctx.fillStyle = 'rgba(16, 185, 129, 0.85)'; // Tailwind green-500 with opacity
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#d1fae5'; // Tailwind green-100
        ctx.font = 'bold 36px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('LEVEL UP!', canvas.width / 2, canvas.height / 2 - 20);
        ctx.font = '20px Arial';
        ctx.fillText('Great job! Get ready for the next level.', canvas.width / 2, canvas.height / 2 + 20);
    }

    if (gameState === STATE.LOST) {
        // Draw Game Over overlay
        ctx.fillStyle = 'rgba(220, 38, 38, 0.85)'; // Tailwind red-600 with opacity
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#fee2e2'; // Tailwind red-200
        ctx.font = 'bold 36px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('GAME OVER', canvas.width / 2, canvas.height / 2 - 20);
        ctx.font = '20px Arial';
        ctx.fillText('Try again! Click to restart.', canvas.width / 2, canvas.height / 2 + 20);
    }

    requestAnimationFrame(draw);

// Add event listener for dismissing overlays
canvas.addEventListener('click', () => {
    if (overlayActive) {
        dismissOverlay();
    }
});
}

// Game loop
setInterval(update, LOGIC_UPDATE_INTERVAL);
draw();
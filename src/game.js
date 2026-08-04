// Motion interpolation feature implemented for smooth rendering

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
let power_up = false; // Track if player has a power-up for ghost logic

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

    // Pellets collection logic
    pellets.forEach(p => {
        if (p.active) {
            if (p.x === playerPos.x && p.y === playerPos.y) {
                p.active = false;
                score += 10;
                // If power pellet, activate power_up state
                if (mazeData[p.y][p.x] === 2) {
                    power_up = true;
                    ghosts.forEach(g => g.state = 'frightened');
                    setTimeout(() => {
                        power_up = false;
                        ghosts.forEach(g => g.state = 'normal');
                    }, 7000); // Power up lasts 7 seconds
                }
            }
        }
    });

    // Win Condition Check
    const remainingPellets = pellets.filter(p => p.active).length;
    if (remainingPellets === 0) {
        activateOverlay(STATE.WON);
    }

    // Ghost state logic example
    ghosts.forEach(g => {
        if (g.state === 'frightened') {
            // Ghosts move randomly or flee player (simplified here)
            g.pos.x += (Math.random() > 0.5 ? 1 : -1);
            g.pos.y += (Math.random() > 0.5 ? 1 : -1);
            // Clamp positions
            g.pos.x = Math.max(1, Math.min(COLS - 2, g.pos.x));
            g.pos.y = Math.max(1, Math.min(ROWS - 2, g.pos.y));
        } else {
            // Normal ghost AI (simplified chase)
            if (g.pos.x < playerPos.x) g.pos.x++;
            else if (g.pos.x > playerPos.x) g.pos.x--;
            if (g.pos.y < playerPos.y) g.pos.y++;
            else if (g.pos.y > playerPos.y) g.pos.y--;
        }
    });

    // Collision detection with ghosts
    ghosts.forEach(g => {
        if (g.pos.x === playerPos.x && g.pos.y === playerPos.y) {
            if (g.state === 'frightened') {
                // Ghost eaten
                score += 50;
                g.pos = { x: 10, y: 10 };
                g.state = 'normal';
            } else {
                // Player loses a life
                lives--;
                if (lives <= 0) {
                    activateOverlay(STATE.LOST);
                } else {
                    // Reset positions
                    playerPos = { x: 5, y: 5 };
                    ghosts.forEach(g => g.pos = { x: 10, y: 10 });
                }
            }
        }
    });
}

function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw maze
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (mazeData[r][c] === 1) {
                ctx.fillStyle = 'blue';
                ctx.fillRect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE);
            } else if (mazeData[r][c] === 2) {
                ctx.fillStyle = 'orange';
                ctx.beginPath();
                ctx.arc(c * TILE_SIZE + TILE_SIZE/2, r * TILE_SIZE + TILE_SIZE/2, TILE_SIZE/3, 0, 2 * Math.PI);
                ctx.fill();
            }
        }
    }

    // Draw pellets
    pellets.forEach(p => {
        if (p.active) {
            ctx.fillStyle = 'white';
            ctx.beginPath();
            ctx.arc(p.x * TILE_SIZE + TILE_SIZE/2, p.y * TILE_SIZE + TILE_SIZE/2, TILE_SIZE/6, 0, 2 * Math.PI);
            ctx.fill();
        }
    });

    // Interpolate player position
    const now = performance.now();
    const t = Math.min(1, (now - lastUpdateTime) / LOGIC_UPDATE_INTERVAL);
    const interpX = lerp(prevPlayerPos.x, playerPos.x, t);
    const interpY = lerp(prevPlayerPos.y, playerPos.y, t);

    // Draw player
    ctx.fillStyle = 'yellow';
    ctx.beginPath();
    ctx.arc(interpX * TILE_SIZE + TILE_SIZE/2, interpY * TILE_SIZE + TILE_SIZE/2, TILE_SIZE/2, 0, 2 * Math.PI);
    ctx.fill();

    // Draw ghosts with visual identifiers based on state
    ghosts.forEach(g => {
        const interpGhostX = lerp(g.prevPos.x, g.pos.x, t);
        const interpGhostY = lerp(g.prevPos.y, g.pos.y, t);
        if (g.state === 'frightened') {
            ctx.fillStyle = 'lightblue';
        } else {
            ctx.fillStyle = 'red';
        }
        ctx.beginPath();
        ctx.arc(interpGhostX * TILE_SIZE + TILE_SIZE/2, interpGhostY * TILE_SIZE + TILE_SIZE/2, TILE_SIZE/2, 0, 2 * Math.PI);
        ctx.fill();
    });

    // Draw score and lives
    ctx.fillStyle = 'white';
    ctx.font = '20px Arial';
    ctx.fillText(`Score: ${score}`, 10, canvas.height - 40);
    ctx.fillText(`Lives: ${lives}`, 10, canvas.height - 10);

    // Draw overlay if active
    if (overlayActive) {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'white';
        ctx.font = '40px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(gameState === STATE.WON ? 'You Win!' : 'Game Over', canvas.width / 2, canvas.height / 2);
    }
}

function gameLoop() {
    const now = performance.now();
    if (now - lastUpdateTime > LOGIC_UPDATE_INTERVAL) {
        update();
        lastUpdateTime = now;
    }
    render();
    requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();

// Export for testing
if (typeof module !== 'undefined') {
    module.exports = {
        update,
        resetGame,
        activateOverlay,
        dismissOverlay,
        ghosts,
        playerPos,
        pellets,
        gameState,
        STATE
    };
}

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
            }
        }
    });

    // Win Condition Check
    const remainingPellets = pellets.filter(p => p.active).length;
    if (remainingPellets === 0) {
        gameState = STATE.WON;
    }

    // Collision Detection for ghosts
    ghosts.forEach(g => {
        const dist = Math.hypot(playerPos.x - g.pos.x, playerPos.y - g.pos.y);
        if (dist < 1) { // Same tile
            if (!power_up) {
                gameState = STATE.LOST;
            } else {
                power_up = false;
            }
        }
    });

    lastUpdateTime = performance.now();
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
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#facc15';
        ctx.font = '30px Arial';
        ctx.fillText('LEVEL CLEAR!', canvas.width/2 - 100, canvas.height/2);
    }

    if (gameState === STATE.LOST) {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#ef4444';
        ctx.font = '30px Arial';
        ctx.fillText('GAME OVER', canvas.width/2 - 100, canvas.height/2);
    }

    requestAnimationFrame(draw);
}

// Game loop
setInterval(update, LOGIC_UPDATE_INTERVAL);
draw();

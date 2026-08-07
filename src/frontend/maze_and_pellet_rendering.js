// Maze and Pellet Rendering Module

// This module handles rendering the maze and pellets on the game canvas.

export function drawMaze(ctx, mazeData, tileSize) {
  ctx.fillStyle = '#000'; // Maze background color
  ctx.fillRect(0, 0, mazeData[0].length * tileSize, mazeData.length * tileSize);

  ctx.strokeStyle = '#00f'; // Maze walls color
  ctx.lineWidth = 2;

  for (let y = 0; y < mazeData.length; y++) {
    for (let x = 0; x < mazeData[y].length; x++) {
      if (mazeData[y][x] === 1) { // Wall
        ctx.strokeRect(x * tileSize, y * tileSize, tileSize, tileSize);
      }
    }
  }
}

export function drawPellets(ctx, pellets, tileSize) {
  ctx.fillStyle = '#ff0'; // Pellet color
  pellets.forEach(pellet => {
    ctx.beginPath();
    ctx.arc(pellet.x * tileSize + tileSize / 2, pellet.y * tileSize + tileSize / 2, tileSize / 6, 0, Math.PI * 2);
    ctx.fill();
  });
}

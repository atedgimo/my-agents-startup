// Frontend JS for enhanced visual feedback and accessibility

// Elements assumed to exist in the DOM
const pelletElement = document.getElementById('pellet');
const ghosts = document.querySelectorAll('.ghost');
const powerPelletElement = document.getElementById('power-pellet');

// Accessibility: keyboard focus indicators
function setupFocusIndicators() {
  const focusableElements = document.querySelectorAll('button, [tabindex]');
  focusableElements.forEach(el => {
    el.addEventListener('focus', () => {
      el.classList.add('focus-visible');
    });
    el.addEventListener('blur', () => {
      el.classList.remove('focus-visible');
    });
  });
}

// Pellet consumption animation
async function animatePelletConsumption() {
  if (!pelletElement) return;
  pelletElement.classList.add('consume-animation');
  await new Promise(resolve => setTimeout(resolve, 500));
  pelletElement.style.visibility = 'hidden';
}

// Ghost state animations
function updateGhostStates(state) {
  ghosts.forEach(ghost => {
    ghost.classList.remove('normal', 'frightened', 'eaten');
    ghost.classList.add(state);
  });
}

// Power pellet effect animation
async function animatePowerPelletEffect() {
  if (!powerPelletElement) return;
  powerPelletElement.classList.add('active-effect');
  await new Promise(resolve => setTimeout(resolve, 1000));
  powerPelletElement.classList.remove('active-effect');
}

// Accessibility: color contrast adjustments
function adjustColorContrast() {
  // Example: toggle a high-contrast mode
  document.body.classList.toggle('high-contrast');
}

// Initialize visual feedback features
export async function initVisualFeedback() {
  setupFocusIndicators();
  // Fetch initial states from backend and update UI
  const response = await fetch('/game/visual-feedback');
  if (response.ok) {
    const data = await response.json();
    if (data.pellet_consumed) {
      pelletElement.style.visibility = 'hidden';
    }
    updateGhostStates(data.ghost_state);
    if (data.power_pellet_active) {
      animatePowerPelletEffect();
    }
  }
}

// Functions to trigger state changes from UI or game events
export async function consumePellet() {
  await fetch('/game/consume-pellet', { method: 'POST' });
  animatePelletConsumption();
}

export async function setGhostState(state) {
  await fetch(`/game/set-ghost-state/${state}`, { method: 'POST' });
  updateGhostStates(state);
}

export async function activatePowerPellet() {
  await fetch('/game/activate-power-pellet', { method: 'POST' });
  animatePowerPelletEffect();
}

export async function resetVisualStates() {
  await fetch('/game/reset-visual-states', { method: 'POST' });
  pelletElement.style.visibility = 'visible';
  updateGhostStates('normal');
}

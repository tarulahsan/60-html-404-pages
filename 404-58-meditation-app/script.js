
const counterEl = document.getElementById('counter');
let seconds = 10;
let timer = null;

function tick() {
  seconds -= 1;
  if (counterEl) counterEl.textContent = String(seconds);
  if (seconds <= 0) {
    clearInterval(timer);
    // Redirect target (customize):
    // location.href = '/';
  }
}

function start() {
  clearInterval(timer);
  timer = setInterval(tick, 1000);
}

function pause() { clearInterval(timer); }
function resume() { start(); }
function reset() { seconds = 10; if (counterEl) counterEl.textContent = '10'; }

document.addEventListener('click', (e) => {
  const btn = e.target.closest('.ctrl');
  if (!btn) return;
  const action = btn.dataset.action;
  if (action === 'pause') pause();
  if (action === 'resume') resume();
  if (action === 'reset') reset();
});

// Theme toggle
const toggle = document.querySelector('.theme-toggle');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
function applyTheme() {
  const isDark = document.documentElement.classList.toggle('dark', prefersDark.matches);
  toggle && (toggle.innerHTML = isDark ? '<i class="bx bx-sun"></i>' : '<i class="bx bx-moon"></i>');
}
prefersDark.addEventListener('change', applyTheme);
toggle && toggle.addEventListener('click', () => {
  document.documentElement.classList.toggle('dark');
});
applyTheme();
reset();
start();

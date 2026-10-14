(function() {
  function updateToggleButton(btn, isPaper) {
    if (!btn) return;
    btn.setAttribute('aria-pressed', isPaper ? 'true' : 'false');
    var label = btn.querySelector('.theme-toggle-label');
    var icon = btn.querySelector('.theme-toggle-icon');
    if (label) label.textContent = isPaper ? 'Night' : 'Paper';
    if (icon) icon.textContent = isPaper ? '🌑' : '📜';
    btn.setAttribute('title', isPaper ? 'Switch to Night mode' : 'Switch to Paper mode');
  }

  function initTheme() {
    var btn = document.getElementById('theme-toggle');
    var isPaper = document.documentElement.getAttribute('data-theme') === 'paper';
    updateToggleButton(btn, isPaper);

    if (btn) {
      btn.addEventListener('click', function() {
        var current = document.documentElement.getAttribute('data-theme');
        var next = current === 'paper' ? 'night' : 'paper';
        if (next === 'paper') {
          document.documentElement.setAttribute('data-theme', 'paper');
        } else {
          document.documentElement.removeAttribute('data-theme');
        }
        try {
          localStorage.setItem('theme', next);
        } catch(e) {}
        updateToggleButton(btn, next === 'paper');
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
  } else {
    initTheme();
  }
})();

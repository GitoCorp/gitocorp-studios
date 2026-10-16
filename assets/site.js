/* Prensa: botones «Copiar» de los textos. */
(function () {
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var el = document.querySelector(btn.getAttribute('data-copy'));
      if (!el || !navigator.clipboard) return;
      var label = btn.textContent, done = btn.getAttribute('data-done') || 'Copiado';
      var text = Array.prototype.map.call(el.querySelectorAll('p'), function (p) { return p.textContent; }).join('\n\n');
      navigator.clipboard.writeText(text).then(function () {
        btn.textContent = done;
        btn.classList.add('is-done');
        setTimeout(function () { btn.textContent = label; btn.classList.remove('is-done'); }, 1800);
      });
    });
  });
})();

/* Pared de iconos del inicio: al pasar por una app (o enfocarla con el teclado),
   el resplandor del hero toma su color y el pie muestra su nombre. */
(function () {
  var wall = document.querySelector('[data-wall]');
  if (!wall) return;
  var hero = document.querySelector('[data-hero]');
  var caption = document.querySelector('[data-caption]');
  var tiles = wall.querySelectorAll('.tile');
  var fallback = caption.getAttribute('data-default');
  var timer;

  function activate(tile) {
    clearTimeout(timer);
    tiles.forEach(function (t) { t.classList.toggle('is-active', t === tile); });
    wall.setAttribute('data-active', '');
    hero.style.setProperty('--tint', tile.getAttribute('data-accent'));
    caption.textContent = '';
    var name = document.createElement('strong');
    name.textContent = tile.getAttribute('data-name');
    caption.appendChild(name);
    caption.appendChild(document.createTextNode('. ' + tile.getAttribute('data-tagline') + '.'));
  }

  function reset() {
    timer = setTimeout(function () {
      tiles.forEach(function (t) { t.classList.remove('is-active'); });
      wall.removeAttribute('data-active');
      hero.style.removeProperty('--tint');
      caption.textContent = fallback;
    }, 120);
  }

  tiles.forEach(function (tile) {
    tile.addEventListener('pointerenter', function () { activate(tile); });
    tile.addEventListener('focus', function () { activate(tile); });
    tile.addEventListener('pointerleave', reset);
    tile.addEventListener('blur', reset);
  });
})();

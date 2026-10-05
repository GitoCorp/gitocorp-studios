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

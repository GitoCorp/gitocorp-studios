# GitoCorp Studios · web v5.0

Web estática para GitHub Pages. Sube el **contenido** de esta carpeta a la raíz del repositorio (no la carpeta contenedora). Todas las rutas son relativas, así que funciona también dentro del subdirectorio del proyecto.

## Estructura

- `index.html`: landing (hero con pared de iconos, lista de apps, estudio, privacidad y contacto).
- `apps/<app>/index.html`: ficha de cada app (Infiltrado, RealFood Planner, Noche de Juegos, Turno+, NFC Life, FamilyBank, DanoQuiz).
- `privacy/index.html`: hub de privacidad. `privacy/<app>.html`: política de cada app.
- `assets/styles.css`, `assets/site.js`: diseño y la única interacción (la pared de iconos del inicio).
- `assets/icons/<app>.png` (1024 px, originales) y `<app>-256.png` (los que usa la web, ligeros).
- `content/privacy/<app>.html`: texto legal de cada política (la primera línea es la entradilla).
- `tools/build.py`: genera todas las páginas.

## URLs para App Store Connect

Base: `https://gitocorp.github.io/gitocorp-studios/`

- `privacy/infiltrado.html`, `privacy/realfood-planner.html`, `privacy/noche-de-juegos.html`
- `privacy/turno-plus.html`, `privacy/nfc-life.html`, `privacy/familybank.html`, `privacy/danoquiz.html`

Contacto oficial: gito@gitocorp.com

## Añadir o cambiar una app

1. Añade su entrada en la lista `APPS` de `tools/build.py` (nombre, color, textos, pantalla de ejemplo).
2. Pon sus iconos en `assets/icons/` (`<slug>.png` de 1024 px y `<slug>-256.png` de 256 px).
3. Escribe su política en `content/privacy/<slug>.html`.
4. Ejecuta `python3 tools/build.py` desde la raíz. Las páginas, la landing, el hub y los pies se regeneran solos.

Para editar un texto de una política: cambia el fichero de `content/privacy/` y vuelve a ejecutar el script (no edites `privacy/*.html` a mano, se sobrescriben).

## Diseño

- Una sola familia tipográfica, Bricolage Grotesque (Google Fonts), con ejes de anchura y peso.
- Base neutra fría (`#eef1f5`) con modo oscuro automático; el color de cada app es el único acento (resplandor del hero, líneas, puntos y tinte de la ficha).
- Momento principal: en el inicio, al pasar por un icono el resplandor del hero toma el color de esa app. Fuera de eso, solo hay una animación de entrada de los iconos. Respeta `prefers-reduced-motion`.
- Sin eyebrows, sin numeración y sin tarjetas idénticas: las apps van en filas, no en cuadrícula.

## Notas de versión

- v5.0: rediseño completo y generador de páginas. Iconos ligeros de 256 px.
- v4.0: FamilyBank. v3.9: Turno+ y NFC Life.

# GitoCorp Studios · web v5.0

Web estática para GitHub Pages. Sube el **contenido** de esta carpeta a la raíz del repositorio (no la carpeta contenedora). Todas las rutas son relativas, así que funciona también dentro del subdirectorio del proyecto.

## Estructura

- `index.html`: landing (hero con pared de iconos, lista de apps, estudio, privacidad y contacto).
- `apps/<app>/index.html`: ficha de cada app (FamilyBank, Noche de Juegos, Lomos, RealFood Planner, NFC Life, Turno+, Infiltrado, DanoQuiz, NickClick, Disfrazados, Carta Alta).
- `privacy/index.html`: hub de privacidad. `privacy/<app>.html`: política de cada app.
- `assets/styles.css`, `assets/site.js`: diseño y la única interacción (la pared de iconos del inicio).
- `assets/icons/<app>.png` (1024 px, originales) y `<app>-256.png` (los que usa la web, ligeros).
- `content/privacy/<app>.html`: texto legal de cada política (la primera línea es la entradilla).
- `press/index.html`: zona de prensa. `press/<app>/index.html`: kit de prensa de cada app nominada.
- `assets/press/<app>/`: iconos para prensa, `capturas/` (reales), `imagenes/` (promocionales) y el ZIP del kit, que se genera solo.
- `tools/build.py`: genera todas las páginas.

## URLs para App Store Connect

Base: `https://www.gitocorp.com/` (las direcciones antiguas `gitocorp.github.io/gitocorp-studios/…` y `gitocorp.com/gitocorp-studios/…` redirigen solas aquí)

- `privacy/infiltrado.html`, `privacy/realfood-planner.html`, `privacy/noche-de-juegos.html`
- `privacy/turno-plus.html`, `privacy/nfc-life.html`, `privacy/familybank.html`, `privacy/danoquiz.html`
- `privacy/nickclick.html`, `privacy/disfrazados.html`, `privacy/carta-alta.html`, `privacy/lomos.html`

Contacto oficial: gito@gitocorp.com

## Añadir o cambiar una app

1. Añade su entrada en la lista `APPS` de `tools/build.py` (nombre, color, textos, pantalla de ejemplo).
2. Pon sus iconos en `assets/icons/` (`<slug>.png` de 1024 px y `<slug>-256.png` de 256 px).
3. Escribe su política en `content/privacy/<slug>.html`.
4. Ejecuta `python3 tools/build.py` desde la raíz. Las páginas, la landing, el hub y los pies se regeneran solos.

Para editar un texto de una política: cambia el fichero de `content/privacy/` y vuelve a ejecutar el script (no edites `privacy/*.html` a mano, se sobrescriben).

## Kits de prensa

1. Añade la app al diccionario `PRESS` de `tools/build.py` (ficha técnica, textos en español e inglés y lo más destacado).
2. Deja las capturas reales en `assets/press/<app>/capturas/`, los mockups de la App Store en `assets/press/<app>/app-store/` (prefijos `1-iphone-` y `2-ipad-` para agruparlos) y las imágenes de prensa en `assets/press/<app>/imagenes/`, con nombres ordenados. Cada imagen va en una sola carpeta: no la dupliques. Cuando la app esté publicada, pon su enlace en `appstore=`.
3. Ejecuta `python3 tools/build.py` (necesita Pillow): crea miniaturas, iconos de 1024 y 512 px, el ZIP y las páginas. Las secciones sin imágenes no se muestran.

## Diseño

- Una sola familia tipográfica, Bricolage Grotesque (Google Fonts), con ejes de anchura y peso.
- Base neutra fría (`#eef1f5`) con modo oscuro automático; el color de cada app es el único acento (resplandor del hero, líneas, puntos y tinte de la ficha).
- Momento principal: en el inicio, al pasar por un icono el resplandor del hero toma el color de esa app. Fuera de eso, solo hay una animación de entrada de los iconos. Respeta `prefers-reduced-motion`.
- Sin eyebrows, sin numeración y sin tarjetas idénticas: las apps van en filas, no en cuadrícula.

## Notas de versión

- v5.7: Lomos (ficha, guía «Cómo empezar» y política de privacidad en español e inglés), tercera en importancia. La pared de iconos del inicio admite 11 apps (filas 4-3-4). Una app puede tener su propia entradilla para la guía con `steps_sub`.
- v5.6: FamilyBank usa gitos (GTO), su moneda ficticia, en ficha y kit de prensa; marcada como «Próximamente en la App Store».
- v5.5: capturas reales, mockups de la App Store e imágenes de prensa (4 exclusivas) en los kits de FamilyBank y Noche de Juegos; enlace a la App Store de Noche de Juegos.
- v5.4: zona de Prensa con kits de FamilyBank y Noche de Juegos (textos ES/EN, ficha técnica, icono, logotipo, capturas y ZIP). Sustituye el kit antiguo de Noche de Juegos 3.0.

- v5.3: Carta Alta (ficha y política de privacidad). La pared de iconos del inicio admite 10 apps (filas 3-4-3).
- v5.2: Disfrazados (ficha y política de privacidad). La pared de iconos del inicio admite 9 apps (filas 3-4-2).
- v5.1: NickClick (ficha, guía «Cómo empezar» y política de privacidad). La ficha de una app admite una guía opcional con la clave `steps`.
- v5.0: rediseño completo y generador de páginas. Iconos ligeros de 256 px.
- v4.0: FamilyBank. v3.9: Turno+ y NFC Life.

## Buscadores (Google)

- `tools/build.py` genera `sitemap.xml` (con fecha de último cambio de cada página), `robots.txt` y la carpeta `gitocorp-studios/`, que redirige las rutas antiguas a la raíz. No la borres.
- El dominio propio `www.gitocorp.com` debe estar puesto en *Settings → Pages* de **este** repositorio (no en `gitocorp.github.io`).

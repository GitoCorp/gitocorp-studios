#!/usr/bin/env python3
"""Genera todas las páginas de GitoCorp Studios.

Uso (desde la raíz del repositorio):  python3 tools/build.py

- Los datos de cada app están en APPS (más abajo).
- El texto legal de cada política vive en content/privacy/<slug>.html
  (la primera línea es un comentario <!--lead:...--> con la entradilla).
- Para añadir una app: añade su entrada en APPS, sus iconos en assets/icons/
  (<slug>.png de 1024px y <slug>-256.png de 256px) y su content/privacy/<slug>.html.
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "gito@gitocorp.com"
FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:"
         "opsz,wdth,wght@12..96,75..100,200..800&display=swap")

# ---------------------------------------------------------------- datos

APPS = [
    dict(
        slug="infiltrado", name="Infiltrado", accent="#8b5cf6",
        badge="Juego social para iPhone", kicker="Juego social",
        tagline="Juego social de identidad secreta",
        desc="Un juego presencial de sospechas, roles ocultos y acusaciones que se juega pasando el móvil. Ahora con Modo Caos: roles extra como el Confundido y el Detective para que ninguna partida se parezca a la anterior.",
        points=["Modo Caos con roles nuevos: Confundido y Detective.", "Todas las categorías disponibles desde el primer día, sin desbloqueos."],
        meta="Infiltrado es un juego social presencial para iPhone basado en roles ocultos, sospechas y acusaciones.",
        lead="Roles ocultos, caos controlado y una acusación final.",
        screen=("Expediente 01", "Partida presencial de 7 jugadores", [
            ("1", "Modo y jugadores", "Clásico o Modo Caos, con los participantes que sean."),
            ("2", "Categoría", "Pocas categorías, bien agrupadas y todas desbloqueadas."),
            ("3", "Deliberación", "El momento de defenderse, acusar y resolver.")]),
        head=("Un juego social fácil de poner en marcha.", "La app ordena la preparación de la partida para que el grupo se centre en lo importante: hablar, sospechar, improvisar y acusar."),
        feats=[("Modo Caos", "El Confundido sabe que lo es e intenta no meter la pata; el Detective obtiene la información que busca sin que nadie note quién es."),
               ("Identidades privadas", "El móvil pasa de mano en mano y cada jugador ve su papel sin romper el suspense."),
               ("Todo desbloqueado", "Juego completo desde el inicio, sin tutorial obligatorio, sin cuenta y sin conexión.")],
        privacy="La app está pensada para partidas locales. No requiere cuenta, no vende datos personales y no necesita servidores externos para jugar en su versión base.",
        hub="Partidas presenciales con roles ocultos. La app está pensada para funcionar sin cuenta propia y sin publicidad personalizada.",
    ),
    dict(
        slug="realfood-planner", name="RealFood Planner", accent="#22c55e",
        badge="Planificación de comidas", kicker="Planificación de comidas",
        tagline="Planificación real de comidas",
        desc="Una forma sencilla de organizar comidas y cenas, guardar platos habituales y preparar la compra con más criterio.",
        points=["Menú semanal claro y editable.", "Platos, despensa, compra, historial y sincronización familiar con iCloud."],
        meta="RealFood Planner es un planificador de comidas para iPhone con menús semanales, platos, despensa, lista de compra e historial.",
        lead="Organiza la semana sin convertir la comida en otra tarea pendiente.",
        screen=("Semana organizada", "Comidas, cenas y compra", [
            ("Lun", "Comida: pollo con arroz", "Cena: tortilla y ensalada"),
            ("Mar", "Comida: lentejas", "Cena: salmón con verduras"),
            ("Compra", "Añadir yogures, fruta, huevos y verduras", "Despensa revisada antes de salir")]),
        head=("Planificar sin perder flexibilidad.", "RealFood Planner reúne menús, platos, despensa, compra e historial para que decidir qué comer sea más fácil durante la semana."),
        feats=[("Semana a la vista", "Comidas y cenas organizadas en una estructura fácil de revisar, cambiar y compartir en familia cuando se active iCloud."),
               ("Platos y despensa", "Guarda recetas habituales, revisa lo que tienes y prepara la compra con menos improvisación."),
               ("Historial útil", "Consulta semanas anteriores para inspirarte y evitar repetir siempre lo mismo.")],
        privacy="RealFood Planner puede funcionar con datos locales y, cuando se active el uso familiar, utilizar iCloud/CloudKit para compartir platos y planificación entre dispositivos o personas invitadas por el usuario.",
        hub="Planificación, platos, despensa e historial. Puede funcionar en local y usar iCloud/CloudKit para compartir datos familiares cuando el usuario lo active.",
    ),
    dict(
        slug="noche-de-juegos", name="Noche de Juegos", accent="#f59e0b",
        badge="Organizador de juegos de mesa", kicker="Juegos de mesa",
        tagline="Retos, sesiones y ludoteca familiar",
        desc="Una ayuda para sacar más partido a la ludoteca: elegir qué jugar, registrar partidas y crear retos que animen a volver a mesa.",
        points=["Biblioteca, partidas y retos.", "Búsqueda e importación de datos públicos desde BoardGameGeek."],
        meta="Noche de Juegos es un organizador de juegos de mesa para iPhone: biblioteca, sesiones, retos y seguimiento de partidas.",
        lead="Elige mejor qué jugar y guarda el recuerdo de cada partida.",
        screen=("Plan de la semana", "Jugar más, elegir mejor", [
            ("Hoy", "Azul · partida familiar", "Duración prevista: 35 min"),
            ("Reto", "Completar 5 juegos sin repetir categoría", "Progreso: 3 de 5"),
            ("Archivo", "Historial de retos y partidas", "Consulta lo jugado meses atrás")]),
        head=("Tu ludoteca, más viva.", "Noche de Juegos convierte la colección en planes, retos y sesiones para que elegir mesa sea más fácil y jugar tenga más continuidad."),
        feats=[("Biblioteca organizada", "Ten tus juegos a mano, añádelos manualmente o apóyate en BoardGameGeek para completar información pública de la colección."),
               ("Retos y sesiones", "Marca objetivos, programa partidas y sigue el progreso sin depender de notas sueltas."),
               ("Memoria de partidas", "Guarda lo jugado para recordar qué funcionó, cuándo y con quién.")],
        privacy="La app guarda tu biblioteca, partidas y retos para organizar tus sesiones. Las búsquedas online pueden consultar BoardGameGeek para obtener información pública de juegos; cualquier permiso del dispositivo se solicita solo cuando una función lo necesita.",
        hub="Biblioteca, retos y sesiones de juego. Puede consultar BoardGameGeek para buscar o importar información pública de juegos.",
    ),
    dict(
        slug="turno-plus", name="Turno+", accent="#E2521E",
        badge="Marcador y turnos para juegos de mesa", kicker="Marcador y turnos",
        tagline="Marcador, turnos y dados",
        desc="El contador, la ruleta de turnos y los dados virtuales que sustituyen a la libreta en cualquier partida, con marcadores creados a medida para cada juego.",
        points=["Asistente para crear el marcador de tu juego.", "Ruleta de turnos y dados virtuales con animación."],
        meta="Turno+ es un marcador y gestor de turnos para juegos de mesa y cartas: contadores personalizables, ruleta de turnos y dados virtuales.",
        lead="El contador, la ruleta y los dados que sustituyen a la libreta en cualquier partida.",
        screen=("La Cuenta", "4 jugadores, ronda 3", [
            ("Marcador", "Contadores para cada juego", "Plantillas estándar o creadas con el asistente."),
            ("Turnos", "Ruleta para decidir quién empieza", "Grupos guardados y animación real de giro."),
            ("Dados", "Dados virtuales de varias caras", "Tira uno o varios a la vez, sin buscar los físicos.")]),
        head=("Un marcador para cada juego.", "Turno+ nace como complemento de Noche de Juegos: un contador flexible que se adapta al juego concreto en lugar de obligarte a encajarlo en un marcador genérico."),
        feats=[("Asistente de creación", "Responde unas preguntas sencillas sobre cómo se puntúa tu juego y Turno+ construye el marcador adecuado: rondas acumulativas, cantidad que baja hasta cero, vidas, acarreo por grupos y más."),
               ("Ruleta de turnos", "Decide quién empieza con una ruleta animada, guarda grupos de jugadores habituales y elige entre distintos temas de color."),
               ("Dados virtuales", "Dados de 4, 6, 12 o 20 caras con animación de tirada real, para jugar sin depender de los dados físicos.")],
        privacy="Los marcadores, grupos de jugadores y partidas se guardan para que puedas retomarlos y consultar tu historial. Algunas funciones pueden consultar BoardGameGeek para completar información pública de un juego al crear un contador nuevo.",
        hub="Marcadores, ruleta de turnos y dados virtuales. Puede consultar BoardGameGeek al crear un marcador para un juego concreto.",
    ),
    dict(
        slug="nfc-life", name="NFC Life", accent="#5b63f5",
        badge="Inventario de etiquetas NFC", kicker="Inventario NFC",
        tagline="Inventario de etiquetas NFC",
        desc="Graba etiquetas NFC y vincúlalas a los objetos de casa para encontrarlos al instante y recibir avisos de mantenimiento.",
        points=["Lectura y escritura de etiquetas NTAG213/215/216.", "Recordatorios de mantenimiento y sincronización con iCloud."],
        meta="NFC Life es un inventario de etiquetas NFC para iPhone: graba, organiza y recibe recordatorios de mantenimiento de los objetos de tu casa.",
        lead="Graba una etiqueta, vincúlala a un objeto y no vuelvas a olvidar su mantenimiento.",
        screen=("Mis etiquetas", "Inventario de casa", [
            ("Grabar", "Escribe etiquetas NTAG213/215/216", "Vincula cada una a un objeto real de casa."),
            ("Inventario", "Encuentra cada objeto al instante", "Acerca el móvil a la etiqueta para abrir su ficha."),
            ("Recordatorios", "Mantenimiento sin sorpresas", "Avisos para revisiones, cambios de filtro o garantías.")]),
        head=("Cada objeto, a un toque.", "NFC Life convierte etiquetas NFC físicas en accesos directos a la información de cada objeto de casa: dónde está, cuándo se revisó por última vez y cuándo toca la próxima vez."),
        feats=[("Lectura y escritura NFC", "Compatible con etiquetas NTAG213, NTAG215 y NTAG216 para pegar donde haga falta."),
               ("Inventario claro", "Cada etiqueta queda vinculada a una ficha con su objeto, notas y estado."),
               ("Recordatorios de mantenimiento", "Programa avisos periódicos para que nada se quede sin revisar.")],
        privacy="El inventario de etiquetas y objetos se guarda para uso personal, con la opción de sincronizarlo entre tus propios dispositivos mediante iCloud. La app solicita acceso a NFC solo para leer y escribir las etiquetas cuando lo pides.",
        hub="Inventario de etiquetas NFC y objetos de casa. Puede sincronizarse mediante iCloud en la propia cuenta del usuario.",
    ),
    dict(
        slug="familybank", name="FamilyBank", accent="#d9a441",
        badge="El banco de tu familia, con dinero ficticio", kicker="Banco familiar",
        tagline="El banco de la familia, con dinero ficticio",
        desc="El banco de la familia con dinero ficticio: tarjeta virtual para cada miembro, paga, ahorro, huchas y un programa de puntos con premios creados por cada casa.",
        points=["Roles de director y cliente, con acceso por tarjeta NFC, Face ID o Touch ID.", "Avisos en tiempo real entre los miembros de la familia."],
        meta="FamilyBank es el banco de tu familia con dinero ficticio para iPhone: tarjeta virtual, paga, huchas, ahorro y programa de puntos con premios.",
        lead="Paga semanal, ahorro, huchas y puntos con premios para que los peques aprendan a gestionar su dinero, sin que se mueva un solo euro real.",
        screen=("Tarjeta familiar", "Saldo y puntos de un vistazo", [
            ("Tarjeta", "Una tarjeta virtual para cada miembro", "Entra con tarjeta NFC, Face ID o Touch ID."),
            ("Ahorro", "Huchas y fondo de ahorro", "Retos con icono y color propios."),
            ("Puntos", "Premios creados por cada familia", "Eventos flash y premios acumulativos.")]),
        head=("Un banco a escala familiar.", "FamilyBank reproduce la experiencia de una app bancaria seria, pero con dinero ficticio y bajo el control de los adultos de la casa."),
        feats=[("Roles de director y cliente", "Los adultos directores ingresan la paga, dan puntos y ven todos los movimientos. Los clientes retiran, transfieren y ahorran dentro de sus límites."),
               ("Ahorro con propósito", "Un fondo de ahorro individual intocable y huchas para retos concretos, con aportaciones claras y colores por tipo de movimiento."),
               ("Puntos y premios", "Cada familia crea su catálogo de premios, y los clientes pueden pedir puntos por una buena tarea y canjearlos por sus recompensas.")],
        privacy="FamilyBank no maneja dinero real ni pide datos bancarios. Los datos de cada familia se guardan en un espacio propio y separado, y las fotos de personalización de la tarjeta se quedan solo en el dispositivo.",
        hub="Banco familiar con dinero ficticio. Los datos de cada familia se guardan en un espacio propio y se sincronizan con Firebase; las fotos de las tarjetas se quedan en el dispositivo.",
    ),
    dict(
        slug="danoquiz", name="DanoQuiz", accent="#38bdf8",
        badge="Trivia para iPhone", kicker="Trivia y competición",
        tagline="Trivia rápida y competitiva",
        desc="Un juego de preguntas con modos rápidos para jugar solo, en grupo o en formato batalla.",
        points=["Partidas ágiles y competitivas.", "Modos diseñados para mantener el ritmo."],
        meta="DanoQuiz es un juego de preguntas para iPhone con modos de partida para jugar solo o competir en grupo.",
        lead="Preguntas rápidas, modos competitivos y partidas con ritmo.",
        screen=("Ronda 04", "Pregunta rápida de 15 segundos", [
            ("Pregunta", "¿Qué planeta es conocido como el planeta rojo?", "Elige una respuesta antes de que termine el tiempo."),
            ("Marcador", "Dani 8 · Ana 7 · Gito 6", "Partida igualada hasta el final"),
            ("Modo", "Eliminación", "Fallos acumulados y tensión en cada ronda")]),
        head=("Trivia directa, sin complicaciones.", "DanoQuiz está pensado para entrar, elegir modo y empezar a responder. El foco está en el ritmo de la partida y en que cada modo tenga una sensación distinta."),
        feats=[("Ritmo de partida", "Pantallas claras, tiempos bien marcados y decisiones rápidas para que la energía no caiga."),
               ("Modos diferenciados", "Rapidez, batalla y eliminación para que cada partida tenga un tono distinto."),
               ("Retos y marcas", "Preguntas, puntuaciones y objetivos para jugar una ronda rápida o intentar mejorar resultado.")],
        privacy="La app no vende datos personales. Algunas versiones pueden usar servicios de Apple como Game Center o iCloud si el usuario decide utilizarlos; esos servicios se rigen por sus propias condiciones.",
        hub="Juego de preguntas con modos competitivos. El progreso se guarda para la experiencia de juego y los servicios de Apple dependen de la configuración del usuario.",
    ),
]

NUMBERS = {1: "Una", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco", 6: "Seis", 7: "Siete", 8: "Ocho"}
N = len(APPS)
E = html.escape

# ---------------------------------------------------------------- piezas


def icon(app, root, size=256):
    return f"{root}assets/icons/{app['slug']}-{size}.png"


def head(root, title, desc, accent=None):
    style = f' style="--accent:{accent}"' if accent else ""
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{E(title)}</title>
  <meta name="description" content="{E(desc)}">
  <meta name="color-scheme" content="light dark">
  <meta name="theme-color" content="#eef1f5" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0a0e18" media="(prefers-color-scheme: dark)">
  <link rel="icon" href="{root}assets/brand/favicon-32.png" type="image/png">
  <link rel="apple-touch-icon" href="{root}assets/brand/favicon-192.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">
  <link rel="stylesheet" href="{root}assets/styles.css">
  <script src="{root}assets/site.js" defer></script>
</head>
<body{style}>
<a class="skip" href="#main">Saltar al contenido</a>
"""


def topbar(root, current):
    def a(label, href, key):
        cur = ' aria-current="page"' if current == key else ""
        cls = ' class="nav__opt"' if key in ("apps", "studio") else ""
        return f'<a href="{href}"{cur}{cls}>{label}</a>'
    return f"""<header class="topbar">
  <div class="wrap topbar__in">
    <a class="brand" href="{root or './'}" aria-label="GitoCorp Studios, inicio"><img src="{root}assets/brand/mark-96.png" alt="" width="36" height="36"><span>GitoCorp<span class="brand__sub"> Studios</span></span></a>
    <nav class="nav" aria-label="Navegación principal">
      {a('Apps', root + '#apps', 'apps')}
      {a('Estudio', root + '#studio', 'studio')}
      {a('Privacidad', root + 'privacy/', 'privacy')}
      <a href="mailto:{EMAIL}">Contacto</a>
    </nav>
  </div>
</header>
<main id="main">
"""


def footer(root):
    links = "\n".join(f'        <a href="{root}apps/{a["slug"]}/">{E(a["name"])}</a>' for a in APPS)
    return f"""</main>
<footer class="foot">
  <div class="wrap foot__in">
    <div class="foot__brand">
      <a class="brand" href="{root or './'}"><img src="{root}assets/brand/mark-96.png" alt="" width="36" height="36"><span>GitoCorp<span class="brand__sub"> Studios</span></span></a>
      <p>Apps iPhone independientes: juegos, herramientas y experiencias digitales.</p>
      <p class="foot__legal">Desarrollador: Jorge Sanz Borrell.<br>Marca pública: GitoCorp Studios.</p>
    </div>
    <div class="foot__links">
      <div>
{links}
      </div>
      <div>
        <a href="{root}privacy/">Privacidad</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </div>
  </div>
</footer>
</body>
</html>
"""


def app_row(app, root, mode):
    """mode: 'apps' (landing) o 'privacy' (hub)."""
    slug = app["slug"]
    if mode == "apps":
        text = f'<p>{E(app["desc"])}</p>\n        <ul class="points">' + "".join(f"<li>{E(p)}</li>" for p in app["points"]) + "</ul>"
        main_href, main_label = f'{root}apps/{slug}/', "Ver app"
        sec_href, sec_label = f'{root}privacy/{slug}.html', "Privacidad"
    else:
        text = f'<p>{E(app["hub"])}</p>'
        main_href, main_label = f'{root}privacy/{slug}.html', "Ver política"
        sec_href, sec_label = f'{root}apps/{slug}/', "Ver app"
    return f"""    <article class="app-row" style="--accent:{app['accent']}">
      <div class="app-row__id">
        <img class="app-row__icon" src="{icon(app, root)}" alt="Icono de {E(app['name'])}" width="88" height="88" loading="lazy">
        <div>
          <p class="kicker">{E(app['kicker'])}</p>
          <h3 class="app-row__name"><a href="{main_href}">{E(app['name'])}</a></h3>
        </div>
      </div>
      <div class="app-row__text">
        {text}
      </div>
      <div class="app-row__links">
        <a class="btn btn--solid" href="{main_href}">{main_label}</a>
        <a class="btn" href="{sec_href}">{sec_label}</a>
      </div>
    </article>
"""


# ---------------------------------------------------------------- páginas


def page_index():
    root = ""
    tiles = []
    for i, a in enumerate(APPS):
        tiles.append(
            f'      <a class="tile" href="apps/{a["slug"]}/" style="--i:{i}" data-accent="{a["accent"]}" '
            f'data-name="{E(a["name"])}" data-tagline="{E(a["tagline"])}">'
            f'<img src="{icon(a, root)}" alt="{E(a["name"])}" width="256" height="256"></a>')
    rows = "".join(app_row(a, root, "apps") for a in APPS)
    studio_items = [
        ("Diseñadas para iPhone", "Interfaces directas, legibles y pensadas para usarse cómodamente desde el primer momento."),
        ("Privacidad sin rodeos", "Cada app tiene su política, su contacto y una explicación clara de lo que necesita para funcionar."),
        ("Identidad propia", "Cada app tiene su carácter, su color y su ritmo, pero todas comparten una misma mirada de estudio."),
    ]
    items = "".join(f'<div class="studio__item"><h3>{E(t)}</h3><p>{E(p)}</p></div>' for t, p in studio_items)
    out = head(root, "GitoCorp Studios · Donde una idea se convierte en una app",
               "GitoCorp Studios: estudio independiente de apps iPhone para juegos, herramientas y experiencias digitales útiles, entretenidas y con identidad propia.")
    out += topbar(root, "")
    out += f"""  <section class="hero" data-hero>
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="wrap hero__grid">
      <div class="hero__copy">
        <h1 class="display">Donde una idea se convierte en una app.</h1>
        <p class="lead">En GitoCorp Studios convertimos ideas reales en apps iPhone independientes: herramientas útiles, juegos sociales y experiencias digitales con diseño cuidado y personalidad propia.</p>
        <div class="actions">
          <a class="btn btn--solid" href="#apps">Ver las apps</a>
          <a class="btn" href="privacy/">Privacidad</a>
        </div>
      </div>
      <div class="wallwrap">
        <div class="wall" data-wall>
{chr(10).join(tiles)}
        </div>
        <p class="caption" aria-live="polite" data-caption data-default="{NUMBERS[N]} apps independientes. Elige una para ver su ficha.">{NUMBERS[N]} apps independientes. Elige una para ver su ficha.</p>
      </div>
    </div>
  </section>

  <section id="apps" class="block">
    <div class="wrap">
      <div class="sechead">
        <h2 class="h2">Apps útiles, entretenidas y con identidad propia.</h2>
        <p class="sub">Entretenimiento, organización, planificación y pequeñas herramientas pensadas para resolver momentos concretos con una experiencia clara.</p>
      </div>
      <div class="apps">
{rows}    <article class="app-row app-row--soon">
      <div class="app-row__id">
        <div class="ghost" aria-hidden="true">+</div>
        <div>
          <p class="kicker">Próximamente</p>
          <h3 class="app-row__name">Más ideas en camino</h3>
        </div>
      </div>
      <div class="app-row__text">
        <p>GitoCorp Studios seguirá sumando apps independientes: herramientas útiles, juegos sociales y nuevas experiencias narrativas como <strong>Expedientes</strong>, siempre con la misma idea de fondo: convertir necesidades reales en aplicaciones cuidadas.</p>
      </div>
    </article>
      </div>
    </div>
  </section>

  <section id="studio" class="wrap">
    <div class="studio">
      <h2 class="h2">Ideas reales, experiencias cuidadas.</h2>
      <p class="studio__lead">El punto de partida siempre es una necesidad concreta: jugar mejor, organizar algo, simplificar una tarea o dar forma a una idea que merece convertirse en app.</p>
      <div class="studio__items">{items}</div>
    </div>
  </section>

  <section class="block">
    <div class="wrap duo">
      <div>
        <h2 class="h3x">Información clara y accesible.</h2>
        <p class="sub">Cada aplicación cuenta con su propia política de privacidad y una página de referencia para soporte, contacto y consulta pública.</p>
        <p><a class="btn btn--solid" href="privacy/">Ver privacidad</a></p>
      </div>
      <div>
        <h2 class="h3x">Contacto directo.</h2>
        <p class="sub">Para soporte, sugerencias o consultas relacionadas con las apps, escribe al correo oficial de GitoCorp Studios.</p>
        <p><a class="bigmail" href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </div>
  </section>
"""
    out += footer(root)
    return out


def phone(app, root):
    title, sub, rows = app["screen"]
    r = "".join(f'<div class="srow"><small>{E(l)}</small><b>{E(t)}</b><span>{E(s)}</span></div>' for l, t, s in rows)
    return f"""<div class="phone" role="img" aria-label="Ilustración de la pantalla de {E(app['name'])}">
        <div class="screen">
          <div class="screen__head"><img src="{icon(app, root)}" alt="" width="44" height="44"><div><b>{E(title)}</b><span>{E(sub)}</span></div></div>
          {r}
        </div>
      </div>"""


def page_app(app):
    root = "../../"
    slug = app["slug"]
    others = "".join(
        f'<a class="other" href="{root}apps/{o["slug"]}/"><img src="{icon(o, root)}" alt="" width="84" height="84" loading="lazy"><span>{E(o["name"])}</span></a>'
        for o in APPS if o["slug"] != slug)
    feats = "".join(f'<div class="feat"><h3>{E(t)}</h3><p>{E(p)}</p></div>' for t, p in app["feats"])
    out = head(root, f"{app['name']} · GitoCorp Studios", app["meta"], app["accent"])
    out += topbar(root, "apps")
    out += f"""  <section class="ahero">
    <div class="wrap ahero__grid">
      <div>
        <a class="crumb" href="{root}#apps">Todas las apps</a>
        <div class="ahero__id">
          <img src="{icon(app, root)}" alt="Icono de {E(app['name'])}" width="96" height="96">
          <p class="kicker">{E(app['badge'])}</p>
        </div>
        <h1 class="display display--app">{E(app['name'])}</h1>
        <p class="lead">{E(app['lead'])}</p>
        <div class="actions">
          <a class="btn btn--solid" href="{root}privacy/{slug}.html">Política de privacidad</a>
          <a class="btn" href="mailto:{EMAIL}">Contactar</a>
        </div>
      </div>
      {phone(app, root)}
    </div>
  </section>

  <section class="block">
    <div class="wrap">
      <div class="sechead">
        <h2 class="h2">{E(app['head'][0])}</h2>
        <p class="sub">{E(app['head'][1])}</p>
      </div>
      <div class="feats">{feats}</div>
    </div>
  </section>

  <section class="wrap">
    <div class="note">
      <div>
        <h2 class="h3x">Privacidad de {E(app['name'])}</h2>
        <p class="sub">{E(app['privacy'])}</p>
      </div>
      <a class="btn btn--solid" href="{root}privacy/{slug}.html">Leer la política</a>
    </div>
  </section>

  <section class="block">
    <div class="wrap">
      <h2 class="h3x">Más apps de GitoCorp</h2>
      <div class="others">{others}</div>
    </div>
  </section>
"""
    out += footer(root)
    return out


def page_privacy(app):
    root = "../"
    frag = (ROOT / "content" / "privacy" / f"{app['slug']}.html").read_text()
    m = re.match(r"<!--lead:(.*?)-->\n", frag, re.S)
    lead, legal = m.group(1), frag[m.end():]
    out = head(root, f"Política de privacidad de {app['name']} · GitoCorp Studios",
               f"Política de privacidad de {app['name']}, una app de GitoCorp Studios.", app["accent"])
    out += topbar(root, "privacy")
    out += f"""  <section class="phero">
    <div class="wrap">
      <a class="crumb" href="{root}privacy/">Todas las políticas</a>
      <div class="phero__id">
        <img src="{icon(app, root)}" alt="Icono de {E(app['name'])}" width="72" height="72">
        <p class="kicker">Política de privacidad de {E(app['name'])}</p>
      </div>
      <h1 class="display display--legal">Privacidad de {E(app['name'])}.</h1>
      <p class="lead">{lead}</p>
    </div>
  </section>
  <section class="block block--tight">
    <div class="wrap">
      <div class="legal">
{legal}
        <p><a class="link" href="{root}apps/{app['slug']}/">Volver a la ficha de {E(app['name'])}</a></p>
      </div>
    </div>
  </section>
"""
    out += footer(root)
    return out


def page_privacy_hub():
    root = "../"
    rows = "".join(app_row(a, root, "privacy") for a in APPS)
    out = head(root, "Privacidad · GitoCorp Studios", "Privacidad y soporte de las apps de GitoCorp Studios.")
    out += topbar(root, "privacy")
    out += f"""  <section class="phero">
    <div class="wrap">
      <h1 class="display display--legal">Privacidad y soporte.</h1>
      <p class="lead">Cada app tiene su propia política para consultar qué información necesita, cómo funciona y cómo contactar con soporte.</p>
    </div>
  </section>
  <section class="block block--tight">
    <div class="wrap">
      <div class="apps">
{rows}      </div>
    </div>
  </section>
"""
    out += footer(root)
    return out


def write(path, content):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print("escrito", path)


def main():
    write("index.html", page_index())
    write("privacy/index.html", page_privacy_hub())
    for a in APPS:
        write(f"apps/{a['slug']}/index.html", page_app(a))
        write(f"privacy/{a['slug']}.html", page_privacy(a))


if __name__ == "__main__":
    main()

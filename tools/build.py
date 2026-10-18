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
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en import UI as UI_EN, APPS_EN, PRESS_EN  # noqa: E402

LANG = "es"  # idioma de la pasada actual: "es" o "en"
EMAIL = "gito@gitocorp.com"
BASE_URL = "https://www.gitocorp.com/"  # dirección principal (canonical, hreflang y sitemap)
FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:"
         "opsz,wdth,wght@12..96,75..100,200..800&display=swap")

# ---------------------------------------------------------------- datos

APPS = [
    dict(
        slug="familybank", name="FamilyBank", accent="#d9a441",
        badge="El banco de tu familia, con dinero ficticio", kicker="Banco familiar",
        tagline="El banco de la familia, con dinero ficticio",
        desc="El banco de la familia con dinero ficticio: tarjeta virtual para cada miembro, paga, ahorro, huchas y un programa de puntos con premios creados por cada casa.",
        points=["Roles de director y cliente, con acceso por tarjeta NFC, Face ID o Touch ID.", "Avisos en tiempo real entre los miembros de la familia."],
        meta="FamilyBank es el banco de tu familia con dinero ficticio para iPhone: tarjeta virtual, paga, huchas, ahorro y programa de puntos con premios.",
        lead="Paga semanal, ahorro, huchas y puntos con premios para que los peques aprendan a gestionar su dinero con gitos, una moneda ficticia, sin que se mueva dinero real.",
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
        slug="lomos", name="Lomos", accent="#1F7A86",
        badge="La biblioteca de casa, en orden", kicker="Biblioteca de casa",
        tagline="Cada libro de casa, en su balda",
        desc="La biblioteca de casa en el iPhone: escanea el código de barras y Lomos rellena título, autor y portada; dibuja tus estanterías por habitaciones y encuentra cualquier libro en su balda.",
        points=["Escaneo del ISBN con datos y portada de Google Books y Open Library.", "Mapa de cada habitación con tus muebles dibujados y los libros reales en sus baldas.", "Lectores de la familia con su progreso, veces leído, valoraciones, préstamos y lista de deseos.", "Biblioteca compartida con la familia por iCloud."],
        meta="Lomos es una app para iPhone y iPad para organizar la biblioteca de casa: escanea el ISBN, dibuja tus estanterías por habitaciones y encuentra cada libro en su balda.",
        lead="¿Dónde está el cuento de esta noche? Escanea, coloca y encuentra cualquier libro de casa en segundos.",
        screen=("¿Dónde está?", "Salón · Billy derecha · Balda 3", [
            ("Escanear", "El monstruo de colores", "Título, autor y portada con solo enfocar el código."),
            ("Leyendo", "Sara va por el 50 %", "Dice la página y Lomos calcula el porcentaje."),
            ("Para devolver", "Biblioteca municipal · en 2 días", "Aviso antes de que venza el préstamo.")]),
        head=("Tus libros, en su sitio.", "Lomos redibuja tus estanterías —Billy, de cubos, esquineras, mesitas de noche o a medida— con los lomos de tus libros reales, para que toda la familia sepa dónde está cada uno."),
        feats=[("Escanear y listo", "Enfoca el código de barras y Lomos trae título, autor, páginas, sinopsis y portada. También por título, en lote o a mano con una foto de la portada."),
               ("El mapa de casa", "Habitaciones y zonas vistas de frente, con cada mueble a escala, su color de lomo y su grosor según las páginas. Toca un libro y se ilumina su balda."),
               ("Lectores de la familia", "Cada lector con su progreso, sus lecturas y sus valoraciones. Préstamos a amigos, libros de la biblioteca pública con aviso de devolución y una lista de deseos con tiendas y precios.")],
        steps_sub="Una guía rápida para tener la biblioteca de casa lista en una tarde.",
        steps=[("Crea tu biblioteca", "Al abrir Lomos por primera vez, ponle nombre y di quién eres. Añade los lectores de casa: los peques sin móvil los gestionas tú."),
               ("Añade los libros", "Pulsa «+» y escanea el código de barras de la contraportada. Si no aparece, búscalo por título y autor o añádelo a mano con una foto de la portada."),
               ("Dibuja tus muebles", "En «Mapa», crea las habitaciones y sus zonas y elige el modelo de cada mueble: Billy ancha o estrecha, de cubos, esquinera, mesita de noche, cómoda, a medida o sobre tu propia foto."),
               ("Coloca cada libro", "Elige la balda al añadir un libro o mueve varios a la vez desde la balda. Las baldas con decoración o juegos se marcan para que no cuenten."),
               ("Encuentra y lee", "Escribe en «¿Dónde está?» y Lomos te lleva a la balda. Apunta la página por la que vas y Lomos calcula el porcentaje."),
               ("Comparte con la familia", "Desde «Familia», invita a otro adulto con su propio iPhone: veréis y editaréis la misma biblioteca con vuestras cuentas de iCloud.")],
        privacy="Los libros, lectores, estanterías y préstamos se guardan en tu dispositivo y en tu iCloud privado, y solo se comparten con la familia si tú la invitas. Para rellenar los datos de un libro se envía el ISBN o el título a Google Books y Open Library. Sin cuentas propias, anuncios ni analíticas.",
        hub="Biblioteca de casa con mapa de estanterías. Se sincroniza con el iCloud del usuario y se comparte solo con quien él invite; las búsquedas de libros consultan Google Books y Open Library.",
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
        slug="infiltrado", name="Infiltrado", accent="#8b5cf6",
        badge="Juego social para iPhone", kicker="Juego social",
        tagline="Juego social de identidad secreta",
        desc="Un juego presencial de sospechas, roles ocultos y acusaciones que se juega pasando el móvil. Ahora con Modo Caos: roles extra como el Confundido y el Detective para que ninguna partida se parezca a la anterior.",
        points=["Modo Caos con roles nuevos: Confundido y Detective.", "Todas las categorías disponibles desde el primer día, sin desbloqueos.", "Grupos de jugadores guardados para no escribir nombres cada vez."],
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
    dict(
        slug="nickclick", name="NickClick", accent="#1C66EB",
        badge="Tus colecciones de muñecos, con nombre", kicker="Colecciones de muñecos",
        tagline="Tus muñecos, con foto y nombre",
        desc="Guarda tus colecciones de muñecos y figuras —Playmobil, Funko, minifiguras o sorpresas de huevo— con su foto, su nombre y sus rasgos, y reconócelos con la cámara.",
        points=["Fotos con el fondo recortado y un color a elegir.", "Lista de los que te faltan y progreso de cada colección.", "Historial de nombres, favoritos y familias opcionales entre personajes.", "Reconoce un muñeco con una foto, sin conexión."],
        meta="NickClick es una app para iPhone para guardar colecciones de muñecos y figuras con foto, nombre, rasgos e historial de nombres, y reconocerlos con la cámara.",
        lead="Cada muñeco con su foto, su nombre y su historia. Para coleccionar o para jugar.",
        screen=("Mi colección", "24 muñecos · Coleccionar y jugar", [
            ("Muñeco", "Mike", "Recortado sobre fondo verde, marcado como favorito."),
            ("Familia", "Amigo de Demogorgon", "Relaciones opcionales que se ven en las dos fichas."),
            ("¿Quién es?", "El más parecido: Mike", "Una foto basta para saber cuál es.")]),
        head=("Nombres que no se olvidan.", "Para una colección completa o para los juguetes de casa: cada tipo de figura en su propia colección, libre o con lista cerrada."),
        feats=[("Foto con fondo de color", "Recorta el muñeco de la foto con un toque, ponle un color de fondo de la cuadrícula y agrupa la colección por colores. La foto original se puede recuperar siempre."),
               ("Nombre e historial", "Cada muñeco tiene su nombre, sus rasgos y un historial con los nombres anteriores, para cuando cambia de nombre en una nueva historia."),
               ("¿Quién es?", "Haz una foto a un muñeco y NickClick te muestra los más parecidos de tu colección. El reconocimiento se hace dentro del iPhone, sin conexión.")],
        steps=[("Crea una colección", "Para llevarla en serio o solo para tener tus muñecos ordenados. Ponle nombre e imagen y elige si es libre, para ir añadiendo lo que tengas, o con lista, si es una serie cerrada (por ejemplo, 12 figuras)."),
               ("Añade tus muñecos", "Pulsa «+», haz una foto o elígela de la galería, escribe su nombre y, si quieres, sus rasgos (pelo, ropa, accesorios)."),
               ("Quita el fondo", "En la ficha, pulsa «Quitar el fondo» y elige un color en la cuadrícula. «Recuperar el fondo» devuelve la foto original."),
               ("Apunta los que te faltan", "En las colecciones con lista, «Me faltan» guarda a mano los que aún no tienes y la barra muestra el progreso. Al conseguir uno, «¡La tengo!» lo pasa a tu colección con su nombre."),
               ("Marca tus favoritos", "Toca la estrella en la ficha o al editar para marcar un favorito, y fíltralos después con el botón de filtro."),
               ("Busca, filtra y reconoce", "Usa el buscador, el botón de filtro (orden, favoritos, color y familia) o la pestaña «¿Quién es?» para identificar un muñeco con una foto."),
               ("En iPhone y iPad", "Con la misma cuenta de iCloud, tus colecciones aparecen en todos tus dispositivos. Desde el menú puedes añadir más usuarios; cada uno tiene sus propias colecciones.")],
        privacy="Las colecciones, fotos y nombres se guardan en tu dispositivo y se sincronizan con tu iCloud privado entre iPhone y iPad. NickClick no tiene cuentas, anuncios ni analíticas, y el recorte del fondo y el reconocimiento por foto se hacen dentro del dispositivo.",
        hub="Colecciones de muñecos con foto y nombre. Se sincronizan con el iCloud privado del usuario y el reconocimiento por foto se hace en el dispositivo.",
    ),
    dict(
        slug="disfrazados", name="Disfrazados", accent="#E0559F",
        badge="Juego de adivinar para toda la familia", kicker="Juego de deducción",
        tagline="¿Quién se ha llevado la tarta?",
        desc="Un juego de deducción para niños desde 6 años y para toda la familia: alguien se ha llevado la tarta de la fiesta y hay que descubrir qué invitado disfrazado ha sido, a base de preguntas de sí o no.",
        points=["Invitados distintos en cada partida, con preguntas que se hacen tocando dibujos.", "Contra Mask, en duelo, en el Reto del día o en los modos «Te toca responder» y «¡Que se escapa!».", "Diseño propio para iPhone, iPad y Apple TV."],
        meta="Disfrazados es un juego de deducción para iPhone, iPad y Apple TV: descubre qué invitado disfrazado se ha llevado la tarta haciendo preguntas de sí o no.",
        lead="Alguien se ha llevado la tarta de la fiesta. Pregunta, descarta y pilla al culpable antes que nadie.",
        screen=("¿Quién ha sido?", "16 invitados · Turno de Luna", [
            ("Pregunta", "¿Lleva corona?", "Se pregunta tocando un dibujo, sin necesidad de leer."),
            ("Respuesta", "¡SÍ! Se descartan 6 invitados", "Las cartas que no encajan se tachan solas."),
            ("VIP", "Brunix era en realidad… Conde Pirulí", "40 invitados VIP disfrazados por coleccionar.")]),
        head=("Deducción de verdad, a medida de los peques.", "Disfrazados toma la idea clásica de adivinar con preguntas y la convierte en una fiesta distinta cada vez: invitados generados al momento, sorpresas que cambian el tablero y un rival, Mask, con un nivel de dificultad bajo control."),
        feats=[("Cada partida es nueva", "Los invitados se crean en cada partida combinando colores, cuerpos, ojos, cuernos, sombreros y objetos, con los rasgos bien repartidos para que todas las preguntas cuenten."),
               ("Mask, un rival a tu nivel", "En Fácil, Normal o Experto, Mask juega a un ritmo fijo y sin trampas de azar, para que un niño pueda ganarle y un adulto tenga un reto de verdad."),
               ("Modos para toda la familia", "Duelo pasando el dispositivo, modo clásico eligiendo tu disfrazado, «Te toca responder», «¡Que se escapa!» y un Reto del día con un solo intento.")],
        privacy="Disfrazados guarda todo solo en el dispositivo: nombres de los detectives, ajustes, álbum de culpables, invitados VIP y resultados del Reto del día. No tiene cuentas, anuncios, compras ni analíticas, no necesita internet y no pide ningún permiso.",
        hub="Juego de deducción para toda la familia. Todo se guarda solo en el dispositivo, sin cuentas, anuncios, compras ni conexión a internet.",
    ),
    dict(
        slug="carta-alta", name="Carta Alta", accent="#1E8A63",
        badge="Duelo de cartas para dos", kicker="Juego de cartas",
        tagline="El duelo de cartas más rápido",
        desc="Un duelo de cartas para dos en un solo móvil: cada uno destapa su carta y gana la más alta. Con cartas de poder, barajas ilustradas y barajas hechas con tus propias fotos.",
        points=["Pantalla dividida: un jugador a cada lado de la mesa.", "Contra otra persona o contra la máquina en Fácil, Medio o Experto.", "Barajas con tus fotos, recortadas y sin fondo, sin salir del móvil."],
        meta="Carta Alta es un duelo de cartas para dos en iPhone: destapa tu carta, usa tus cartas de poder y gana la ronda. Con barajas ilustradas y barajas con tus fotos.",
        lead="Una partida rápida para esperar una cola, una sobremesa o un viaje. Destapa, sorprende con un poder y llévate la ronda.",
        screen=("Ronda 6 de 10", "Gito 07 · 05 Rival", [
            ("Destapa", "Un 12 contra un 11", "El primero en destapar gana céntimos de iniciativa."),
            ("Poder", "¡Robo!", "Pierdes por poco y te quedas la ronda."),
            ("Baraja", "La familia", "Las figuras son vuestras fotos, sin fondo.")]),
        head=("La carta más alta, con giros.", "Carta Alta convierte el juego más sencillo en un duelo con decisiones: cuándo destapar, qué poderes llevar y cuándo usarlos."),
        feats=[("Cartas de poder", "Robo, Giro, Escudo, Doble o nada y más. Cada jugador monta su mazo de poder con los que ha conseguido en la tienda y elige el momento de usarlos."),
               ("Justo y con ritmo", "Reparto equilibrado, con las mismas cartas para los dos en distinto orden, y una máquina que juega con las mismas reglas, sin mirar sus cartas."),
               ("Barajas a tu gusto", "Cuatro temáticas ilustradas, dorsos coleccionables, tapetes distintos en cada partida y barajas con fotos de tu familia como figuras.")],
        privacy="Carta Alta guarda en el dispositivo los perfiles de juego, los puntos, los poderes y las barajas con fotos. Las fotos se eligen una a una, se recortan y se les quita el fondo dentro del iPhone, y nunca salen de él. Sin cuentas, anuncios, compras ni conexión.",
        hub="Duelo de cartas para dos. Perfiles, puntos y barajas con fotos se guardan solo en el dispositivo; las fotos se procesan dentro del iPhone y no se envían a ningún sitio.",
    ),
]

# ---------------------------------------------------------------- prensa
# Apps con kit de prensa (el orden de PRESS es el de la página /press/).
# Para nominar otra app: añade su entrada aquí y deja sus imágenes en
#   assets/press/<slug>/capturas/   capturas reales (PNG/JPG), en orden por nombre: 01-..., 02-...
#   assets/press/<slug>/imagenes/   imágenes promocionales y mockups exclusivos de prensa
#   assets/press/<slug>/app-store/  los mockups publicados en la App Store
# En capturas/ y app-store/, el prefijo 1-iphone-... / 2-ipad-... agrupa por dispositivo.
# Si la app ya está publicada, pon su enlace en appstore=...
# El script genera las miniaturas, los iconos y el ZIP del kit.

PRESS = {
    "familybank": dict(
        facts=[("Desarrollador", "Jorge Sanz Borrell · GitoCorp Studios"),
               ("Plataformas", "iPhone y iPad"),
               ("Disponibilidad", "Próximamente en la App Store"),
               ("Lanzamiento", "Otoño de 2026"),
               ("Idioma", "Español"),
               ("Moneda", "El gito (GTO), ficticia y sin relación con ninguna moneda real"),
               ("Acceso", "Iniciar sesión con Apple; tarjeta NFC, Face ID o Touch ID")],
        short="FamilyBank es el banco de la familia con dinero ficticio: una tarjeta para cada miembro, paga, ahorro, huchas y un programa de puntos con premios, para que los niños aprendan a gestionar su dinero.",
        long=["FamilyBank reproduce la experiencia de una app bancaria de verdad, pero con dinero ficticio y bajo el control de los adultos de la casa. La moneda de la app es el gito (GTO), ficticia y sin relación con ninguna moneda real. Cada miembro tiene su tarjeta virtual con su saldo en gitos y sus puntos, y los niños entran acercando su tarjeta NFC al iPhone o con Face ID o Touch ID.",
              "Los adultos que dirigen el banco ingresan la paga, dan puntos explicando el motivo y ven todos los movimientos. Los niños retiran, transfieren a sus hermanos y ahorran: en un fondo de ahorro que no se puede tocar o en huchas para retos concretos, cada una con su icono y su color.",
              "Cada familia crea su propio catálogo de premios, desde canjes inmediatos hasta metas a las que aporta toda la casa. Los avisos llegan al momento a los móviles de la familia, y los datos de cada familia se guardan en un espacio propio y separado. Sin dinero real y sin datos bancarios."],
        short_en="FamilyBank is a family bank with pretend money: a card for every family member, allowance, savings, piggy banks and a points programme with rewards, so children learn to manage their money.",
        long_en=["FamilyBank recreates the feel of a real banking app, but with pretend money and with the parents in charge. The app's currency is the gito (GTO), a pretend currency unrelated to any real one. Every member has a virtual card showing their balance in gitos and their points, and children sign in by tapping their NFC card on the iPhone or with Face ID or Touch ID.",
                 "The adults who run the bank pay the allowance, award points with a reason and see every transaction. Children withdraw, transfer to their siblings and save: in a savings fund they cannot touch, or in piggy banks for specific goals, each with its own icon and colour.",
                 "Each family builds its own rewards catalogue, from instant treats to bigger goals the whole household contributes to. Notifications reach the family's phones instantly, and each family's data lives in its own separate space. No real money and no bank details."],
        highlights=[("Una tarjeta para cada miembro", "Saldo y puntos de un vistazo, con acceso por tarjeta NFC, Face ID o Touch ID y una tarjeta que cada uno puede personalizar."),
                    ("Los adultos al mando", "Roles de director y cliente: los directores ingresan la paga, dan puntos y ven todos los movimientos para trasladarlos al mundo real."),
                    ("Ahorrar tiene premio", "Fondo de ahorro intocable, huchas para retos y un programa de puntos con premios flash y acumulativos creados por cada familia.")],
    ),
    "noche-de-juegos": dict(
        appstore="https://apps.apple.com/es/app/noche-de-juegos/id6771836805",
        facts=[("Desarrollador", "Jorge Sanz Borrell · GitoCorp Studios"),
               ("Plataformas", "iPhone y iPad"),
               ("Disponibilidad", "App Store"),
               ("Idioma", "Español"),
               ("Datos", "En el dispositivo y en el iCloud de la familia")],
        short="Noche de Juegos es la app para familias y grupos que juegan a juegos de mesa: organiza la ludoteca, registra cada partida y ayuda a decidir qué sacar a la mesa.",
        long=["Noche de Juegos convierte una colección de juegos de mesa en algo vivo. Cada juego tiene su ficha, cada partida queda registrada con quién ganó y los retos animan a sacar de la estantería juegos que llevaban tiempo sin jugarse.",
              "Ludo, el asistente de la app, propone qué jugar según cuántos sois, el tiempo que tenéis, el historial de partidas y los retos activos. Funciona dentro del propio iPhone, sin depender de servidores externos.",
              "La ludoteca se comparte con la familia mediante iCloud, y la información pública de cada juego puede completarse desde BoardGameGeek. Perfiles, rankings y planificación de sesiones completan una app pensada para jugar más y elegir mejor."],
        short_en="Noche de Juegos (Game Night) is an app for families and groups who love board games: it organises the collection, logs every play and helps decide what to bring to the table.",
        long_en=["Noche de Juegos brings a board game collection to life. Every game has its own page, every play is logged along with the winner, and challenges encourage the family to bring games back off the shelf.",
                 "Ludo, the app's assistant, suggests what to play based on the number of players, the time available, play history and active challenges. It runs entirely on the iPhone, with no external servers.",
                 "The collection is shared with the family through iCloud, and public game information can be filled in from BoardGameGeek. Player profiles, rankings and session planning round out an app designed to help people play more and choose better."],
        highlights=[("Ludoteca organizada", "Toda la colección con su ficha, añadida a mano o completada con la información pública de BoardGameGeek."),
                    ("Partidas, retos y rankings", "Cada partida queda registrada, y los retos y la planificación de sesiones dan continuidad a las noches de juego."),
                    ("Ludo, el asistente", "Recomienda qué jugar según la mesa, el tiempo y el historial, sin salir del iPhone.")],
    ),
}

STUDIO_LOGO = "assets/press/gitocorp/gitocorp-studios-simbolo.png"
IMG_EXT = {".png", ".jpg", ".jpeg"}

try:
    from PIL import Image
except ImportError:  # sin Pillow se usan los originales como miniatura
    Image = None

NUMBERS = {1: "Una", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco", 6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez", 11: "Once", 12: "Doce"}
N = len(APPS)
E = html.escape


def t(s, **kw):
    """Texto de interfaz en el idioma actual (la clave es el texto en español)."""
    if LANG == "en":
        s = UI_EN.get(s, s)
    return s.format(**kw) if kw else s


def A(app, key):
    """Campo de una app en el idioma actual; si falta en inglés, cae al español."""
    if LANG == "en":
        return APPS_EN.get(app["slug"], {}).get(key, app.get(key))
    return app.get(key)


# ---------------------------------------------------------------- piezas


def icon(app, root, size=256):
    return f"{root}assets/icons/{app['slug']}-{size}.png"


def pre():
    """Prefijo de carpeta del idioma actual ('' en español, 'en/' en inglés)."""
    return "en/" if LANG == "en" else ""


def has_policy_en(slug):
    return (ROOT / "content" / "privacy" / "en" / f"{slug}.html").exists()


def policy_href(app, root):
    """Enlace a la política en el idioma actual; en inglés, si aún no hay texto inglés, a la española."""
    if LANG == "en" and has_policy_en(app["slug"]):
        return f"{root}{pre()}privacy/{app['slug']}.html", True
    return f"{root}privacy/{app['slug']}.html", LANG == "es"


def lang_switch(root, path):
    """Enlace al mismo contenido en el otro idioma (path es la ruta sin prefijo de idioma)."""
    if LANG == "es":
        return (f'<a class="nav__lang" href="{root}en/{path}" hreflang="en" lang="en" '
                f'aria-label="{E(UI_EN["Switch to English"])}" title="English">EN</a>')
    return (f'<a class="nav__lang" href="{root}{path}" hreflang="es" lang="es" '
            f'aria-label="{E(UI_EN["Cambiar a español"])}" title="Español">ES</a>')


def has_en(path):
    """¿Existe la versión inglesa de esta ruta (sin prefijo de idioma)?"""
    m = re.fullmatch(r"privacy/([\w-]+)\.html", path)
    return has_policy_en(m.group(1)) if m else True


def head(root, title, desc, accent=None, path=None):
    style = f' style="--accent:{accent}"' if accent else ""
    seo = ""
    if path is not None:
        seo = f'  <link rel="canonical" href="{BASE_URL}{pre()}{path}">\n'
        if has_en(path):
            seo += (f'  <link rel="alternate" hreflang="es" href="{BASE_URL}{path}">\n'
                    f'  <link rel="alternate" hreflang="en" href="{BASE_URL}en/{path}">\n'
                    f'  <link rel="alternate" hreflang="x-default" href="{BASE_URL}{path}">\n')
    return f"""<!doctype html>
<html lang="{LANG}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{E(title)}</title>
  <meta name="description" content="{E(desc)}">
{seo}  <meta name="color-scheme" content="light dark">
  <meta name="theme-color" content="#eef1f5" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0a0e18" media="(prefers-color-scheme: dark)">
  <link rel="icon" href="{root}favicon.ico" sizes="48x48">
  <link rel="icon" href="{root}assets/brand/favicon-48.png" type="image/png" sizes="48x48">
  <link rel="icon" href="{root}assets/brand/favicon-96.png" type="image/png" sizes="96x96">
  <link rel="icon" href="{root}assets/brand/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="{root}assets/brand/favicon-192.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">
  <link rel="stylesheet" href="{root}assets/styles.css">
  <script src="{root}assets/site.js" defer></script>
</head>
<body{style}>
<a class="skip" href="#main">{t("Saltar al contenido")}</a>
"""


def topbar(root, current, path=""):
    lr = root + pre()

    def a(label, href, key):
        cur = ' aria-current="page"' if current == key else ""
        cls = ' class="nav__opt"' if key in ("apps", "studio", "press") else ""
        return f'<a href="{href}"{cur}{cls}>{label}</a>'
    return f"""<header class="topbar">
  <div class="wrap topbar__in">
    <a class="brand" href="{lr or './'}" aria-label="{t("GitoCorp Studios, inicio")}"><img src="{root}assets/brand/mark-96.png" alt="" width="36" height="36"><span>GitoCorp<span class="brand__sub"> Studios</span></span></a>
    <nav class="nav" aria-label="{t("Navegación principal")}">
      {a(t('Apps'), lr + '#apps', 'apps')}
      {a(t('Estudio'), lr + '#studio', 'studio')}
      {a(t('Privacidad'), lr + 'privacy/', 'privacy')}
      {a(t('Prensa'), lr + 'press/', 'press')}
      <a href="mailto:{EMAIL}">{t('Contacto')}</a>
      {lang_switch(root, path)}
    </nav>
  </div>
</header>
<main id="main">
"""


def footer(root):
    lr = root + pre()
    links = "\n".join(f'        <a href="{lr}apps/{a["slug"]}/">{E(a["name"])}</a>' for a in APPS)
    return f"""</main>
<footer class="foot">
  <div class="wrap foot__in">
    <div class="foot__brand">
      <a class="brand" href="{lr or './'}"><img src="{root}assets/brand/mark-96.png" alt="" width="36" height="36"><span>GitoCorp<span class="brand__sub"> Studios</span></span></a>
      <p>{t("Apps iPhone independientes: juegos, herramientas y experiencias digitales.")}</p>
      <p class="foot__legal">{t("Desarrollador: Jorge Sanz Borrell.<br>Marca pública: GitoCorp Studios.")}</p>
    </div>
    <div class="foot__links">
      <div>
{links}
      </div>
      <div>
        <a href="{lr}privacy/">{t("Privacidad")}</a>
        <a href="{lr}press/">{t("Prensa")}</a>
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
    lr = root + pre()
    pol_href, pol_native = policy_href(app, root)
    pol_label = t("Privacidad") if pol_native else t("Política (ES)")
    if mode == "apps":
        text = f'<p>{E(A(app, "desc"))}</p>\n        <ul class="points">' + "".join(f"<li>{E(p)}</li>" for p in A(app, "points")) + "</ul>"
        main_href, main_label = f'{lr}apps/{slug}/', t("Ver app")
        sec_href, sec_label = pol_href, pol_label
    else:
        text = f'<p>{E(A(app, "hub"))}</p>'
        main_href, main_label = pol_href, t("Ver política") if pol_native else t("Política (ES)")
        sec_href, sec_label = f'{lr}apps/{slug}/', t("Ver app")
    return f"""    <article class="app-row" style="--accent:{app['accent']}">
      <div class="app-row__id">
        <img class="app-row__icon" src="{icon(app, root)}" alt="{t("Icono de ")}{E(app['name'])}" width="88" height="88" loading="lazy">
        <div>
          <p class="kicker">{E(A(app, 'kicker'))}</p>
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
    root = "../" if LANG == "en" else ""
    lr = root + pre()
    tiles = []
    for i, a in enumerate(APPS):
        tiles.append(
            f'      <a class="tile" href="{lr}apps/{a["slug"]}/" style="--i:{i}" data-accent="{a["accent"]}" '
            f'data-name="{E(a["name"])}" data-tagline="{E(A(a, "tagline"))}">'
            f'<img src="{icon(a, root)}" alt="{E(a["name"])}" width="256" height="256"></a>')
    rows = "".join(app_row(a, root, "apps") for a in APPS)
    studio_items = [
        (t("Diseñadas para iPhone"), t("Interfaces directas, legibles y pensadas para usarse cómodamente desde el primer momento.")),
        (t("Privacidad sin rodeos"), t("Cada app tiene su política, su contacto y una explicación clara de lo que necesita para funcionar.")),
        (t("Identidad propia"), t("Cada app tiene su carácter, su color y su ritmo, pero todas comparten una misma mirada de estudio.")),
    ]
    items = "".join(f'<div class="studio__item"><h3>{E(a)}</h3><p>{E(p)}</p></div>' for a, p in studio_items)
    caption = (f"{NUMBERS[N]} apps independientes. Elige una para ver su ficha." if LANG == "es"
               else t("{n} apps independientes. Elige una para ver su ficha.", n=N))
    out = head(root, t("GitoCorp Studios · Donde una idea se convierte en una app"),
               t("GitoCorp Studios: estudio independiente de apps iPhone para juegos, herramientas y experiencias digitales útiles, entretenidas y con identidad propia."), path="")
    out += topbar(root, "", "")
    out += f"""  <section class="hero" data-hero>
    <div class="hero__glow" aria-hidden="true"></div>
    <div class="wrap hero__grid">
      <div class="hero__copy">
        <h1 class="display">{t("Donde una idea se convierte en una app.")}</h1>
        <p class="lead">{t("En GitoCorp Studios convertimos ideas reales en apps iPhone independientes: herramientas útiles, juegos sociales y experiencias digitales con diseño cuidado y personalidad propia.")}</p>
        <div class="actions">
          <a class="btn btn--solid" href="#apps">{t("Ver las apps")}</a>
          <a class="btn" href="{lr}privacy/">{t("Privacidad")}</a>
        </div>
      </div>
      <div class="wallwrap">
        <div class="wall" data-wall>
{chr(10).join(tiles)}
        </div>
        <p class="caption" aria-live="polite" data-caption data-default="{caption}">{caption}</p>
      </div>
    </div>
  </section>

  <section id="apps" class="block">
    <div class="wrap">
      <div class="sechead">
        <h2 class="h2">{t("Apps útiles, entretenidas y con identidad propia.")}</h2>
        <p class="sub">{t("Entretenimiento, organización, planificación y pequeñas herramientas pensadas para resolver momentos concretos con una experiencia clara.")}</p>
      </div>
      <div class="apps">
{rows}    <article class="app-row app-row--soon">
      <div class="app-row__id">
        <div class="ghost" aria-hidden="true">+</div>
        <div>
          <p class="kicker">{t("Próximamente")}</p>
          <h3 class="app-row__name">{t("Más ideas en camino")}</h3>
        </div>
      </div>
      <div class="app-row__text">
        <p>{t("GitoCorp Studios seguirá sumando apps independientes: herramientas útiles, juegos sociales y nuevas experiencias narrativas como <strong>Expedientes</strong>, siempre con la misma idea de fondo: convertir necesidades reales en aplicaciones cuidadas.")}</p>
      </div>
    </article>
      </div>
    </div>
  </section>

  <section id="studio" class="wrap">
    <div class="studio">
      <h2 class="h2">{t("Ideas reales, experiencias cuidadas.")}</h2>
      <p class="studio__lead">{t("El punto de partida siempre es una necesidad concreta: jugar mejor, organizar algo, simplificar una tarea o dar forma a una idea que merece convertirse en app.")}</p>
      <div class="studio__items">{items}</div>
    </div>
  </section>

  <section class="block">
    <div class="wrap duo">
      <div>
        <h2 class="h3x">{t("Información clara y accesible.")}</h2>
        <p class="sub">{t("Cada aplicación cuenta con su propia política de privacidad y una página de referencia para soporte, contacto y consulta pública.")}</p>
        <p><a class="btn btn--solid" href="{lr}privacy/">{t("Ver privacidad")}</a></p>
      </div>
      <div>
        <h2 class="h3x">{t("Contacto directo.")}</h2>
        <p class="sub">{t("Para soporte, sugerencias o consultas relacionadas con las apps, escribe al correo oficial de GitoCorp Studios.")}</p>
        <p><a class="bigmail" href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </div>
  </section>
"""
    out += footer(root)
    return out


def phone(app, root):
    title, sub, rows = A(app, "screen")
    r = "".join(f'<div class="srow"><small>{E(l)}</small><b>{E(x)}</b><span>{E(s)}</span></div>' for l, x, s in rows)
    return f"""<div class="phone" role="img" aria-label="{t("Ilustración de la pantalla de ")}{E(app['name'])}">
        <div class="screen">
          <div class="screen__head"><img src="{icon(app, root)}" alt="" width="44" height="44"><div><b>{E(title)}</b><span>{E(sub)}</span></div></div>
          {r}
        </div>
      </div>"""


def steps_html(app):
    """Guía rápida opcional (clave 'steps' en APPS)."""
    steps = A(app, "steps")
    if not steps:
        return ""
    items = "".join(f'<div class="feat"><h3>{i}. {E(x)}</h3><p>{E(p)}</p></div>' for i, (x, p) in enumerate(steps, 1))
    return f"""  <section class="block" id="como-empezar">
    <div class="wrap">
      <div class="sechead">
        <h2 class="h2">{t("Cómo empezar")}</h2>
        <p class="sub">{E(A(app, "steps_sub")) if app.get("steps_sub") else t("Una guía rápida de {name}. El mismo tutorial aparece en la app la primera vez y desde el menú «Cómo funciona».", name=E(app['name']))}</p>
      </div>
      <div class="feats">{items}</div>
    </div>
  </section>

"""


def page_app(app):
    root = "../../" + ("../" if LANG == "en" else "")
    lr = root + pre()
    slug = app["slug"]
    pol_href, pol_native = policy_href(app, root)
    others = "".join(
        f'<a class="other" href="{lr}apps/{o["slug"]}/"><img src="{icon(o, root)}" alt="" width="84" height="84" loading="lazy"><span>{E(o["name"])}</span></a>'
        for o in APPS if o["slug"] != slug)
    feats = "".join(f'<div class="feat"><h3>{E(x)}</h3><p>{E(p)}</p></div>' for x, p in A(app, "feats"))
    h0, h1 = A(app, "head")
    out = head(root, f"{app['name']} · GitoCorp Studios", A(app, "meta"), app["accent"], path=f"apps/{slug}/")
    out += topbar(root, "apps", f"apps/{slug}/")
    out += f"""  <section class="ahero">
    <div class="wrap ahero__grid">
      <div>
        <a class="crumb" href="{lr}#apps">{t("Todas las apps")}</a>
        <div class="ahero__id">
          <img src="{icon(app, root)}" alt="{t("Icono de ")}{E(app['name'])}" width="96" height="96">
          <p class="kicker">{E(A(app, 'badge'))}</p>
        </div>
        <h1 class="display display--app">{E(app['name'])}</h1>
        <p class="lead">{E(A(app, 'lead'))}</p>
        <div class="actions">
          <a class="btn btn--solid" href="{pol_href}">{t("Política de privacidad") if pol_native else t("Política de privacidad") + " (ES)"}</a>
          {f'<a class="btn" href="{lr}press/{slug}/">{t("Kit de prensa")}</a>' if slug in PRESS else f'<a class="btn" href="mailto:{EMAIL}">{t("Contactar")}</a>'}
        </div>
      </div>
      {phone(app, root)}
    </div>
  </section>

  <section class="block">
    <div class="wrap">
      <div class="sechead">
        <h2 class="h2">{E(h0)}</h2>
        <p class="sub">{E(h1)}</p>
      </div>
      <div class="feats">{feats}</div>
    </div>
  </section>

{steps_html(app)}  <section class="wrap">
    <div class="note">
      <div>
        <h2 class="h3x">{t("Privacidad de {name}", name=E(app['name']))}</h2>
        <p class="sub">{E(A(app, 'privacy'))}</p>
      </div>
      <a class="btn btn--solid" href="{pol_href}">{t("Leer la política") if pol_native else t("Leer la política (ES)")}</a>
    </div>
  </section>

  <section class="block">
    <div class="wrap">
      <h2 class="h3x">{t("Más apps de GitoCorp")}</h2>
      <div class="others">{others}</div>
    </div>
  </section>
"""
    out += footer(root)
    return out


def page_privacy(app):
    root = "../" + ("../" if LANG == "en" else "")
    lr = root + pre()
    folder = ROOT / "content" / "privacy" / ("en" if LANG == "en" else "")
    frag = (folder / f"{app['slug']}.html").read_text()
    m = re.match(r"<!--lead:(.*?)-->\n", frag, re.S)
    lead, legal = m.group(1), frag[m.end():]
    name = E(app['name'])
    out = head(root, t("Política de privacidad de {name} · GitoCorp Studios", name=app['name']),
               t("Política de privacidad de {name}, una app de GitoCorp Studios.", name=app['name']), app["accent"],
               path=f"privacy/{app['slug']}.html")
    out += topbar(root, "privacy", f"privacy/{app['slug']}.html" if (LANG == "en" or has_policy_en(app["slug"])) else "privacy/")
    out += f"""  <section class="phero">
    <div class="wrap">
      <a class="crumb" href="{lr}privacy/">{t("Todas las políticas")}</a>
      <div class="phero__id">
        <img src="{icon(app, root)}" alt="{t("Icono de ")}{name}" width="72" height="72">
        <p class="kicker">{t("Política de privacidad de {name}", name=name)}</p>
      </div>
      <h1 class="display display--legal">{t("Privacidad de {name}.", name=name)}</h1>
      <p class="lead">{lead}</p>
    </div>
  </section>
  <section class="block block--tight">
    <div class="wrap">
      <div class="legal">
{legal}
        <p><a class="link" href="{lr}apps/{app['slug']}/">{t("Volver a la ficha de {name}", name=name)}</a></p>
      </div>
    </div>
  </section>
"""
    out += footer(root)
    return out


def page_privacy_hub():
    root = "../" + ("../" if LANG == "en" else "")
    rows = "".join(app_row(a, root, "privacy") for a in APPS)
    out = head(root, t("Privacidad · GitoCorp Studios"), t("Privacidad y soporte de las apps de GitoCorp Studios."), path="privacy/")
    out += topbar(root, "privacy", "privacy/")
    out += f"""  <section class="phero">
    <div class="wrap">
      <h1 class="display display--legal">{t("Privacidad y soporte.")}</h1>
      <p class="lead">{t("Cada app tiene su propia política para consultar qué información necesita, cómo funciona y cómo contactar con soporte.")}</p>
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



# ---------------------------------------------------------------- prensa: ficheros


def human_size(n):
    return (f"{n / 1_048_576:.1f} MB" if LANG == "en" else f"{n / 1_048_576:.1f} MB".replace(".", ",")) if n >= 1_048_576 else f"{max(1, round(n / 1024))} KB"


def media(slug, folder):
    """Imágenes de assets/press/<slug>/<folder>/, con su miniatura web y dimensiones."""
    src_dir = ROOT / "assets" / "press" / slug / folder
    if not src_dir.is_dir():
        return []
    out = []
    for f in sorted(src_dir.iterdir()):
        if f.suffix.lower() not in IMG_EXT:
            continue
        rel = f.relative_to(ROOT).as_posix()
        item = dict(path=rel, thumb=rel, name=f.name, size=f.stat().st_size, w=0, h=0)
        if Image:
            with Image.open(f) as im:
                item["w"], item["h"] = im.size
                thumb = ROOT / "assets" / "press" / slug / "_web" / folder / (f.stem + ".jpg")
                if not thumb.exists() or thumb.stat().st_mtime < f.stat().st_mtime:
                    thumb.parent.mkdir(parents=True, exist_ok=True)
                    t = im.convert("RGBA")
                    t.thumbnail((1400, 1400) if folder == "imagenes" else (720, 720 * 3))
                    bg = Image.new("RGB", t.size, (255, 255, 255))
                    bg.paste(t, mask=t.split()[3])
                    bg.save(thumb, "JPEG", quality=82, optimize=True, progressive=True)
                item["thumb"] = thumb.relative_to(ROOT).as_posix()
        out.append(item)
    return out


def press_files():
    """Iconos y logotipo derivados (solo se generan si faltan)."""
    if not Image:
        return
    logo = ROOT / STUDIO_LOGO
    if not logo.exists():
        logo.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(ROOT / "assets/brand/gito-mark.png") as im:
            im = im.convert("RGBA")
            side = max(im.size)
            sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
            sq.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
            sq.resize((1024, 1024), Image.LANCZOS).save(logo, optimize=True)
    for slug in PRESS:
        d = ROOT / "assets" / "press" / slug
        d.mkdir(parents=True, exist_ok=True)
        with Image.open(ROOT / f"assets/icons/{slug}.png") as im:
            for px in (1024, 512):
                f = d / f"icono-{slug}-{px}.png"
                if not f.exists():
                    im.convert("RGBA").resize((px, px), Image.LANCZOS).save(f, optimize=True)


def press_text(app, p):
    lines = [f"{app['name']} · Kit de prensa", "GitoCorp Studios · https://gitocorp.com/", ""]
    lines += [f"{k}: {v}" for k, v in p["facts"]]
    lines += ["", "DESCRIPCIÓN CORTA", p["short"], "", "DESCRIPCIÓN", *sum(([x, ""] for x in p["long"]), [])]
    lines += ["LO MÁS DESTACADO", *[f"- {t}. {d}" for t, d in p["highlights"]], ""]
    lines += ["SHORT DESCRIPTION (ENGLISH)", p["short_en"], "", "DESCRIPTION (ENGLISH)", *sum(([x, ""] for x in p["long_en"]), [])]
    if p.get("appstore"):
        lines += [f"App Store: {p['appstore']}"]
    lines += [f"Web: https://gitocorp.com/apps/{app['slug']}/", f"Privacidad: https://gitocorp.com/privacy/{app['slug']}.html",
              f"Contacto de prensa: {EMAIL}", "",
              "Puedes usar este material para hablar de la app. Por favor, no modifiques el icono ni el logotipo."]
    return "\n".join(lines) + "\n"


def press_zip(app, p):
    """ZIP del kit, con fecha fija para que no cambie si no cambia el contenido."""
    import zipfile
    slug = app["slug"]
    zpath = ROOT / "assets" / "press" / slug / f"{slug}-kit-de-prensa.zip"
    entries = [(f"{slug}-kit-de-prensa/LEEME-{slug}.txt", press_text(app, p).encode())]
    for px in (1024, 512):
        f = ROOT / "assets" / "press" / slug / f"icono-{slug}-{px}.png"
        if f.exists():
            entries.append((f"{slug}-kit-de-prensa/icono/{f.name}", f.read_bytes()))
    for folder in ("capturas", "app-store", "imagenes"):
        for m in media(slug, folder):
            entries.append((f"{slug}-kit-de-prensa/{folder}/{m['name']}", (ROOT / m["path"]).read_bytes()))
    logo = ROOT / STUDIO_LOGO
    if logo.exists():
        entries.append((f"{slug}-kit-de-prensa/gitocorp-studios/{logo.name}", logo.read_bytes()))
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in entries:
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
    print("escrito", zpath.relative_to(ROOT))
    return zpath


# ---------------------------------------------------------------- prensa: páginas


def dl_card(href, thumb, title, meta, kind="icon"):
    return (f'<a class="dl dl--{kind}" href="{href}" download>'
            f'<span class="dl__img"><img src="{thumb}" alt="" loading="lazy"></span>'
            f'<span class="dl__txt"><b>{E(title)}</b><small>{E(meta)}</small></span></a>')


def gallery(app, root, folder, title, sub):
    items = media(app["slug"], folder)
    if not items:
        return ""
    kind = "promo" if folder == "imagenes" else "shot"

    def card(m):
        dims = f' width="{m["w"]}" height="{m["h"]}"' if m["w"] else ""
        meta = m["name"].rsplit(".", 1)[1].upper() + (f' · {m["w"]} × {m["h"]}' if m["w"] else "") + f' · {human_size(m["size"])}'
        alt = m["name"].rsplit(".", 1)[0].split("-", 1)[-1].replace("-", " ")
        return (f'<a class="media media--{kind}" href="{root}{m["path"]}" download>'
                f'<img src="{root}{m["thumb"]}" alt="{E(app["name"])}: {E(alt)}" loading="lazy"{dims}><small>{meta}</small></a>')

    groups = {}
    for m in items:
        key = "iPhone" if "iphone" in m["name"] else "iPad" if "ipad" in m["name"] else ""
        groups.setdefault(key, []).append(m)
    body = ""
    for key, ms in groups.items():
        head_ = f'<h3 class="gallery__dev">{key}</h3>' if key and len(groups) > 1 else ""
        body += f'{head_}<div class="gallery gallery--{kind}{" gallery--pad" if key == "iPad" else ""}">{"".join(card(m) for m in ms)}</div>'
    return f"""  <section class="block block--tight">
    <div class="wrap">
      <div class="sechead">
        <h2 class="h2">{title}</h2>
        <p class="sub">{sub}</p>
      </div>
      {body}
    </div>
  </section>

"""


def copy_block(id_, title, paras):
    body = "".join(f"<p>{E(x)}</p>" for x in paras)
    return (f'<div class="copy"><div class="copy__head"><h3>{E(title)}</h3>'
            f'<button class="copybtn" type="button" data-copy="#{id_}" data-done="{t("Copiado")}">{t("Copiar")}</button></div>'
            f'<div class="copy__body" id="{id_}">{body}</div></div>')


def pr(slug, key):
    """Dato de prensa en el idioma actual (hechos y destacados; las descripciones usan short/long y short_en/long_en)."""
    if LANG == "en":
        return PRESS_EN.get(slug, {}).get(key, PRESS[slug][key])
    return PRESS[slug][key]


def page_press(app, p, zpath):
    root = "../../" + ("../" if LANG == "en" else "")
    lr = root + pre()
    slug = app["slug"]
    en = LANG == "en"
    short, long_ = (p["short_en"], p["long_en"]) if en else (p["short"], p["long"])
    short2, long2 = (p["short"], p["long"]) if en else (p["short_en"], p["long_en"])
    facts = "".join(f"<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>" for k, v in pr(slug, "facts"))
    feats = "".join(f'<div class="feat"><h3>{E(x)}</h3><p>{E(d)}</p></div>' for x, d in pr(slug, "highlights"))
    icon_alt = t("Icono de ") + app["name"]
    transparent = t("PNG · 1024 × 1024 · fondo transparente")
    icons = "".join([
        dl_card(f"{root}assets/press/{slug}/icono-{slug}-1024.png", f"{root}{icon(app, root='')}", icon_alt, "PNG · 1024 × 1024"),
        dl_card(f"{root}assets/press/{slug}/icono-{slug}-512.png", f"{root}{icon(app, root='')}", icon_alt, "PNG · 512 × 512"),
        dl_card(f"{root}{STUDIO_LOGO}", f"{root}{STUDIO_LOGO}", t("Símbolo de GitoCorp Studios"), transparent, "logo"),
    ])
    out = head(root, f"{app['name']} · {t('Kit de prensa')} · GitoCorp Studios",
               t("Kit de prensa de {name}: textos, ficha técnica, iconos, capturas e imágenes para descargar.", name=app['name']), app["accent"],
               path=f"press/{slug}/")
    out += topbar(root, "press", f"press/{slug}/")
    store = (f'<a class="btn" href="{p["appstore"]}">{t("Ver en la App Store")}</a>' if p.get("appstore")
             else f'<a class="btn" href="{lr}apps/{slug}/">{t("Ficha de la app")}</a>')
    sizes = human_size(zpath.stat().st_size)
    out += f"""  <section class="ahero">
    <div class="wrap ahero__grid">
      <div>
        <a class="crumb" href="{lr}press/">{t("Prensa")}</a>
        <div class="ahero__id">
          <img src="{icon(app, root)}" alt="{E(icon_alt)}" width="96" height="96">
          <p class="kicker">{t("Kit de prensa")}</p>
        </div>
        <h1 class="display display--app">{E(app['name'])}</h1>
        <p class="lead">{E(short)}</p>
        <div class="actions">
          <a class="btn btn--solid" href="{root}assets/press/{slug}/{zpath.name}" download>{t("Descargar el kit · ZIP, {size}", size=sizes)}</a>
          {store}
        </div>
      </div>
      <dl class="facts">{facts}</dl>
    </div>
  </section>

  <section class="block">
    <div class="wrap">
      <div class="sechead">
        <h2 class="h2">{t("Textos listos para usar.")}</h2>
        <p class="sub">{t("Descripción corta y larga, en español y en inglés. También van en el fichero de texto del ZIP.")}</p>
      </div>
      <div class="copies">
        {copy_block(f"{slug}-" + ("short" if en else "corta"), t("Descripción corta"), [short])}
        {copy_block(f"{slug}-" + ("long" if en else "larga"), t("Descripción"), long_)}
      </div>
      <details class="lang">
        <summary>{"En español" if en else "In English"}</summary>
        <div class="copies">
          {copy_block(f"{slug}-" + ("corta" if en else "short"), "Descripción corta" if en else "Short description", [short2])}
          {copy_block(f"{slug}-" + ("larga" if en else "long"), "Descripción" if en else "Description", long2)}
        </div>
      </details>
    </div>
  </section>

  <section class="block block--tight">
    <div class="wrap">
      <h2 class="h3x">{t("Lo más destacado")}</h2>
      <div class="feats feats--press">{feats}</div>
    </div>
  </section>

{gallery(app, root, "imagenes", t("Imágenes de prensa."), t("Composiciones para artículos y redes, hechas con capturas reales. Pulsa una para descargarla a tamaño completo."))}{gallery(app, root, "capturas", t("Capturas."), t("Capturas reales de la app, sin retocar, a resolución nativa del iPhone 17 Pro Max y del iPad Pro de 13 pulgadas."))}{gallery(app, root, "app-store", t("En la App Store."), t("Las imágenes que acompañan a la app en su página de la App Store."))}  <section class="block block--tight">
    <div class="wrap">
      <div class="sechead">
        <h2 class="h2">{t("Icono y logotipo.")}</h2>
        <p class="sub">{t("Úsalos tal cual: sin recortar, deformar ni cambiar sus colores.")}</p>
      </div>
      <div class="dls">{icons}</div>
    </div>
  </section>

  <section class="wrap">
    <div class="note">
      <div>
        <h2 class="h3x">{t("Contacto de prensa")}</h2>
        <p class="sub">{t("Para entrevistas, más material o cualquier consulta sobre {name}, escribe a GitoCorp Studios.", name=E(app['name']))}</p>
      </div>
      <a class="btn btn--solid" href="mailto:{EMAIL}?subject={E(app['name'])}%20%C2%B7%20{"Press" if en else "Prensa"}">{EMAIL}</a>
    </div>
  </section>
"""
    out += footer(root)
    return out


def page_press_hub(zips):
    root = "../" + ("../" if LANG == "en" else "")
    lr = root + pre()
    en = LANG == "en"
    rows = []
    for slug, p in PRESS.items():
        a = next(x for x in APPS if x["slug"] == slug)
        rows.append(f"""    <article class="app-row" style="--accent:{a['accent']}">
      <div class="app-row__id">
        <img class="app-row__icon" src="{icon(a, root)}" alt="{t("Icono de ")}{E(a['name'])}" width="88" height="88" loading="lazy">
        <div>
          <p class="kicker">{E(A(a, 'kicker'))}</p>
          <h3 class="app-row__name"><a href="{lr}press/{slug}/">{E(a['name'])}</a></h3>
        </div>
      </div>
      <div class="app-row__text">
        <p>{E(p['short_en'] if en else p['short'])}</p>
      </div>
      <div class="app-row__links">
        <a class="btn btn--solid" href="{lr}press/{slug}/">{t("Kit de prensa")}</a>
        <a class="btn" href="{root}assets/press/{slug}/{zips[slug].name}" download>ZIP</a>
      </div>
    </article>
""")
    out = head(root, t("Prensa · GitoCorp Studios"),
               t("Kits de prensa de las apps de GitoCorp Studios: textos, ficha técnica, iconos, capturas e imágenes para descargar."), path="press/")
    out += topbar(root, "press", "press/")
    out += f"""  <section class="phero">
    <div class="wrap">
      <h1 class="display display--legal">{t("Prensa.")}</h1>
      <p class="lead">{t("Textos, iconos, capturas e imágenes de las apps de GitoCorp Studios, listos para descargar. Para medios, editores y cualquiera que quiera hablar de ellas.")}</p>
    </div>
  </section>
  <section class="block block--tight">
    <div class="wrap">
      <div class="apps">
{"".join(rows)}      </div>
    </div>
  </section>

  <section class="block block--tight">
    <div class="wrap duo">
      <div>
        <h2 class="h3x">GitoCorp Studios.</h2>
        <p class="sub">{t("Estudio independiente de apps para iPhone y iPad de Jorge Sanz Borrell: herramientas útiles, juegos sociales y experiencias digitales con diseño cuidado y personalidad propia.")}</p>
        <div class="dls dls--one">{dl_card(f"{root}{STUDIO_LOGO}", f"{root}{STUDIO_LOGO}", t("Símbolo de GitoCorp Studios"), t("PNG · 1024 × 1024 · fondo transparente"), "logo")}</div>
      </div>
      <div>
        <h2 class="h3x">{t("Contacto de prensa.")}</h2>
        <p class="sub">{t("Entrevistas, material adicional o cualquier consulta.")}</p>
        <p><a class="bigmail" href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
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


def build_lang(lang):
    """Landing, fichas, hub de privacidad y políticas en un idioma ('' = español, 'en/' = inglés)."""
    global LANG
    LANG = lang
    base = pre()
    write(f"{base}index.html", page_index())
    write(f"{base}privacy/index.html", page_privacy_hub())
    for a in APPS:
        write(f"{base}apps/{a['slug']}/index.html", page_app(a))
        if lang == "es" or has_policy_en(a["slug"]):
            write(f"{base}privacy/{a['slug']}.html", page_privacy(a))


def build_press(lang, zips):
    global LANG
    LANG = lang
    base = pre()
    for slug, p in PRESS.items():
        app = next(x for x in APPS if x["slug"] == slug)
        write(f"{base}press/{slug}/index.html", page_press(app, p, zips[slug]))
    write(f"{base}press/index.html", page_press_hub(zips))


def build_seo():
    """sitemap.xml (con alternativas de idioma) y robots.txt."""
    paths = ["", "privacy/", "press/"]
    paths += [f"apps/{a['slug']}/" for a in APPS]
    paths += [f"privacy/{a['slug']}.html" for a in APPS]
    paths += [f"press/{slug}/" for slug in PRESS]
    urls = []
    for pth in paths:
        alts = (f'    <xhtml:link rel="alternate" hreflang="es" href="{BASE_URL}{pth}"/>\n'
                f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE_URL}en/{pth}"/>\n'
                f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}{pth}"/>\n') if has_en(pth) else ""
        urls.append(f"  <url>\n    <loc>{BASE_URL}{pth}</loc>\n{alts}  </url>")
        if has_en(pth):
            urls.append(f"  <url>\n    <loc>{BASE_URL}en/{pth}</loc>\n{alts}  </url>")
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    write("sitemap.xml", sitemap)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}sitemap.xml\n")


def main():
    build_lang("es")
    build_lang("en")
    press_files()
    zips = {}
    for slug, p in PRESS.items():
        app = next(x for x in APPS if x["slug"] == slug)
        zips[slug] = press_zip(app, p)
    build_press("es", zips)
    build_press("en", zips)
    build_seo()


if __name__ == "__main__":
    main()

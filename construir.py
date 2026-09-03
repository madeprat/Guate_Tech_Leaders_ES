#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el sitio de Guatemala Tech Leaders España."""
import os, shutil, math

BASE = "https://madeprat.github.io/Guate_Tech_Leaders_ES/"
OUT = "/home/claude/build2"

# ---------------------------------------------------------------- marca
def marca_svg(cls="mark"):
    size, r_ring, r_dot, r_table, n = 40, 14.2, 2.55, 7.4, 12
    c = size / 2
    p = [f'<circle cx="{c}" cy="{c}" r="{r_table}" fill="none" stroke="currentColor" stroke-width="1.15" opacity=".42"/>']
    for i in range(n):
        a = -math.pi / 2 + i * 2 * math.pi / n
        p.append(f'<circle cx="{c + r_ring * math.cos(a):.2f}" cy="{c + r_ring * math.sin(a):.2f}" r="{r_dot}" fill="currentColor"/>')
    return f'<svg class="{cls}" viewBox="0 0 {size} {size}" aria-hidden="true" focusable="false">' + "".join(p) + "</svg>"

MARK = marca_svg()

NAV = [("la-iniciativa.html", "La iniciativa"), ("posicion.html", "El vacío"), ("la-mesa.html", "La mesa"), ("instituciones.html", "Instituciones")]

def cabecera(actual):
    enlaces = "".join(
        f'<a href="./{h}"{" aria-current=\"page\"" if h == actual else ""}>{t}</a>' for h, t in NAV
    )
    cta = ' aria-current="page"' if actual == "participar.html" else ""
    return f"""<header class="cab">
  <div class="wrap cab-int">
    <a class="marca" href="./index.html" aria-label="Guatemala Tech Leaders España — inicio">
      {MARK}
      <span class="marca-txt">
        <b>Guatemala Tech Leaders España</b>
        <span>Liderazgo tecnológico guatemalteco en España</span>
      </span>
    </a>
    <button class="hamb" aria-expanded="false" aria-controls="menu">Menú</button>
    <nav id="menu" aria-label="Navegación principal">{enlaces}<a class="n-cta" href="./participar.html"{cta}>Participar</a></nav>
  </div>
</header>"""

PIE = f"""<footer class="pie-sitio">
  <div class="wrap">
    <div class="pie-rej">
      <div>
        <a class="marca pie-marca" href="./index.html">
          {MARK}
          <span class="marca-txt"><b>Guatemala Tech Leaders España</b><span>Liderazgo tecnológico guatemalteco en España</span></span>
        </a>
        <p>Iniciativa profesional independiente. Origen guatemalteco, carrera construida en España, conocimiento compartido aquí.</p>
      </div>
      <div>
        <h4>La iniciativa</h4>
        <ul>
          <li><a href="./la-iniciativa.html">Qué es y quién la impulsa</a></li>
          <li><a href="./posicion.html">El vacío en el mapa</a></li>
          <li><a href="./la-mesa.html">La primera mesa</a></li>
          <li><a href="./instituciones.html">Instituciones y empresas</a></li>
          <li><a href="./participar.html">Participar</a></li>
        </ul>
      </div>
      <div>
        <h4>Contacto</h4>
        <ul>
          <li><a href="#" data-mail="Guatemala Tech Leaders España"><span data-mail-texto>Correo</span></a></li>
          <li><a href="#" data-linkedin target="_blank" rel="noopener">LinkedIn de la impulsora</a></li>
          <li><a href="./legal.html">Aviso legal y privacidad</a></li>
        </ul>
      </div>
    </div>
    <div class="pie-fin">
      <span>Iniciativa profesional independiente, no vinculada oficialmente a ninguna administración española ni guatemalteca.</span>
      <span>2026</span>
    </div>
  </div>
</footer>"""


def pagina(archivo, titulo, desc, og_titulo, og_desc, cuerpo, noindex=False, precarga=True):
    canonical = BASE + ("" if archivo == "index.html" else archivo)
    fuentes = """<link rel="preload" as="font" type="font/woff2" href="./assets/fonts/newsreader-var.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="./assets/fonts/librefranklin-var.woff2" crossorigin>""" if precarga else ""
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ""
    html = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{'website' if archivo == 'index.html' else 'article'}">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Guatemala Tech Leaders España">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{og_titulo}">
<meta property="og:description" content="{og_desc}">
<meta property="og:image" content="{BASE}assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Guatemala Tech Leaders España — iniciativa profesional independiente.">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="./assets/img/icon-32.png" sizes="32x32">
<link rel="icon" href="./assets/img/mark.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="./assets/img/icon-180.png">
{fuentes}
<link rel="stylesheet" href="./assets/style.css">
</head>
<body>
<a class="skip" href="#principal">Ir al contenido</a>
{cabecera(archivo)}
<main id="principal">
{cuerpo}
</main>
{PIE}
<script src="./assets/site.js"></script>
</body>
</html>
"""
    with open(os.path.join(OUT, archivo), "w", encoding="utf-8") as f:
        f.write(html)


# ================================================================ CUERPOS

FICHA_INST = """<aside class="ficha-inst">
  <h2>Ficha de la iniciativa</h2>
  <dl>
    <dt>Naturaleza</dt><dd>Iniciativa profesional independiente, sin ánimo de lucro y sin forma jurídica en esta etapa.</dd>
    <dt>Ámbito</dt><dd>Profesionales de origen guatemalteco que ejercen en el sector tecnológico en España.</dd>
    <dt>Etapa actual</dt><dd>Identificación de perfiles y constitución de la primera mesa. Madrid, cuarto trimestre de 2026.</dd>
    <dt>Documento público</dt><dd>Posición sobre el vacío en la cartografía de la diáspora profesional guatemalteca en España (2026).</dd>
    <dt>Impulsada por</dt><dd>Madelaine Castro, Secretaria General de itSMF España.</dd>
    <dt>Financiación</dt><dd>Ninguna. Sin cuotas, sin patrocinio y sin coste para quien participa.</dd>
  </dl>
</aside>"""

CARTA = """<section class="banda-hueso sec" id="carta">
  <div class="wrap">
    <div class="linea-jade"></div>
    <h2 style="max-width:24ch">Carta de la impulsora</h2>
    <div class="carta">
      <div class="carta-txt">
        <p class="entrada">Nací en Guatemala y llevo más de veinte años construyendo mi carrera en tecnología en España. En estos años he coincidido en comités, congresos y consejos con gente que dirige equipos, funda empresas, investiga o invierte, y de vez en cuando he descubierto, casi por casualidad, que alguien de esa sala también nació allí.</p>
        <p>Luego cada uno vuelve a lo suyo y no volvemos a hablar. Esa es toda la razón de ser de esta iniciativa: no hay que demostrar que existimos, hay que encontrarnos. Y no lo arregla una asociación, ni un directorio, ni un grupo de WhatsApp. Lo arregla sentarse en la misma habitación una tarde y escucharse.</p>
        <p>Quiero decir una cosa que no siempre se dice en voz alta. Yo no leo las noticias de Guatemala. No sé bien qué está pasando allí. Me preocupa Ceuta, me preocupan los incendios, me preocupan las riadas, sufro el calor de julio y me preocupa lo que cuesta vivir aquí. Mi vida está en España desde hace más de veinte años y mi trabajo también. Sé que hay mucha gente en mi misma situación, y que por eso no aparecemos en ningún estudio sobre transferencia de conocimiento hacia Guatemala. No estamos ahí porque no es lo nuestro. Lo nuestro pasa aquí.</p>
        <p>Por eso empiezo por lo más pequeño que se me ocurre, una mesa de diez o doce personas, en lugar de por unos estatutos y una junta directiva. Si de esa tarde sale algo que merezca continuidad, lo construiremos entre quienes estemos. Si no sale, habremos conocido a diez personas que no conocíamos.</p>
        <p>Si estás leyendo esto, es probable que alguien haya pensado en ti. Escríbeme y hablamos.</p>
        <div class="firma">
          <img src="./assets/img/madelaine.jpg" alt="Retrato de Madelaine Castro.">
          <div><b>Madelaine Castro</b><span>Impulsora de la iniciativa. Valencia, 2026.</span></div>
        </div>
      </div>
      <div class="carta-lado">
        <p class="voz">«Nuestro origen nos une. Nuestra aportación sucede aquí.»</p>
        <p class="pie" style="margin-top:20px">Principio fundacional de Guatemala Tech Leaders España.</p>
        <p style="margin-top:24px"><a class="enlace" href="./la-iniciativa.html#impulsora">Quién impulsa la iniciativa</a></p>
      </div>
    </div>
  </div>
</section>"""

TEMAS_CORTOS = """<div class="temas">
  <article class="tema">
    <div><h3>Nuestros hijos frente a la inteligencia artificial</h3>
    <p>Privacidad, aprendizaje, dependencia y criterio. Qué deberían saber las familias y qué papel les toca a colegios y empresas.</p></div>
    <span class="et">IA y educación</span>
  </article>
  <article class="tema">
    <div><h3>Nos están estafando por WhatsApp</h3>
    <p>Cómo ha cambiado el fraude de verdad en los últimos tres años, y qué necesita entender cualquier ciudadano que no trabaje en esto.</p></div>
    <span class="et">Ciberseguridad</span>
  </article>
  <article class="tema">
    <div><h3>¿Quién responde cuando decide un algoritmo?</h3>
    <p>Qué pasa con la responsabilidad cuando se reparte entre tecnología, negocio, proveedor y dirección, y al final no la asume nadie.</p></div>
    <span class="et">Gobierno y riesgo</span>
  </article>
</div>"""

AMBITO = """<ul class="ambito">
  <li>Inteligencia artificial</li><li>Ciberseguridad</li><li>Software y producto</li>
  <li>Datos</li><li>Cloud e infraestructura</li><li>Fintech</li>
  <li>Investigación</li><li>Inversión</li><li>Gobierno tecnológico</li>
</ul>"""

# ---------------------------------------------------------------- índice
INDEX = f"""
<section class="wrap port">
  <div class="port-rej">
    <div>
      <p class="rotulo">Iniciativa profesional independiente · Constitución de la primera mesa, 2026</p>
      <h1>El liderazgo tecnológico guatemalteco en España existe. Todavía no se conoce entre sí.</h1>
      <p class="entrada">Guatemala Tech Leaders España reúne a profesionales de origen guatemalteco que dirigen, fundan, investigan o invierten en tecnología en España, con dos objetivos: conectarlos entre sí y poner ese conocimiento al servicio de los desafíos tecnológicos de la sociedad española.</p>
      <div class="acciones">
        <a class="btn btn-p" href="./la-iniciativa.html">Conocer la iniciativa</a>
        <a class="btn btn-s" href="./participar.html">Quiero participar</a>
      </div>
      <div class="datos">
        <span>Madrid, cuarto trimestre de 2026</span>
        <span>Entre 10 y 12 personas</span>
        <span>Sin coste y sin cuotas</span>
      </div>
    </div>
    {FICHA_INST}
  </div>
</section>

<section class="banda-jade sec">
  <div class="wrap">
    <div class="linea-jade"></div>
    <h2 style="max-width:24ch">Existe un mapa. Nosotros no estamos en él.</h2>
    <p class="entrada medida" style="color:var(--cielo-clr);margin-top:22px">En julio de 2026 se publicó la primera caracterización de la diáspora científica y profesional guatemalteca en España. Es un trabajo necesario y bien hecho. Y deja fuera, por diseño, a un segmento entero.</p>
    <div class="tres" style="margin-top:48px">
      <div><h3>Un segmento sin cartografiar</h3><p>La base de ese estudio se construyó difundiendo una convocatoria por canales académicos y digitales. Eso localiza investigadores. De los 51 encuestados, siete de cada diez tenían menos de cuarenta años y más de la mitad seguía estudiando. Quien dirige una función en una empresa española, funda compañías o gestiona un fondo no aparece en Google Scholar.</p></div>
      <div><h3>Una dirección distinta</h3><p>Aquel estudio define la diáspora, entre otros criterios, por mantener vínculos de transferencia de conocimiento con Guatemala. Esta iniciativa se define por lo contrario: profesionales cuya vida y cuya aportación suceden en España. No es el mismo grupo ni persigue el mismo objetivo.</p></div>
      <div><h3>Una red que nadie construye</h3><p>La debilidad de las redes profesionales estructuradas es uno de los cinco obstáculos que ese mismo estudio identifica. Para la capa académica existen RedCTi y un proyecto europeo en marcha. Para la capa directiva e industrial no existe nada.</p></div>
    </div>
    <p class="entrada medida" style="color:var(--cielo-clr);margin-top:50px">Esta iniciativa no compite con ese trabajo ni lo duplica: se ocupa de la parte del mapa que aquella metodología no podía alcanzar.</p>
    <p style="margin-top:26px"><a class="btn btn-clr" href="./posicion.html">Leer el documento de posición</a></p>
  </div>
</section>

<section class="wrap sec-cp">
  <div class="doc">
    <div>
      <div class="linea-jade"></div>
      <h2 style="max-width:20ch">Lo que nos preocupa pasa aquí.</h2>
      <p class="entrada medida" style="margin-top:24px">Esto no es una red de retorno, ni una asociación de nostalgia, ni un canal de cooperación. Las personas a las que se dirige llevan quince, veinte o veinticinco años en España. Sus hijos son de aquí, sus equipos son de aquí y sus preocupaciones son las de cualquiera que viva en este país: Ceuta, los incendios, las riadas, el calor de julio, lo que cuesta llegar a fin de mes.</p>
      <p class="medida">El origen guatemalteco es el vínculo que permite que este grupo se reconozca. No es el asunto del que va a hablar.</p>
    </div>
    <div class="margen">
      <p class="voz">«Nuestro origen nos une. Nuestra aportación sucede aquí.»</p>
      <p class="pie" style="margin-top:18px">Principio fundacional.</p>
    </div>
  </div>
</section>

<section class="wrap sec">
  <div class="doc">
    <div>
      <div class="linea-jade"></div>
      <h2>A quién reúne.</h2>
      <p class="entrada medida" style="margin-top:24px">La pertenencia se basa en la trayectoria, el liderazgo o el reconocimiento profesional, no en el orden de llegada ni en una inscripción abierta. Estos son los cuatro criterios de la primera etapa.</p>
      <ul class="criterios">
        <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 10.5l4 4 8-9"/></svg>
        <div><b>Ejercicio profesional actual en España.</b><span>No basta con haber estudiado o trabajado aquí en el pasado.</span></div></li>
        <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 10.5l4 4 8-9"/></svg>
        <div><b>Origen guatemalteco, por nacimiento o por familia.</b><span>No se exige nacionalidad vigente ni vínculo profesional actual con el país.</span></div></li>
        <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 10.5l4 4 8-9"/></svg>
        <div><b>Responsabilidad directiva o reconocimiento técnico.</b><span>Dirección de un equipo, una función, una empresa, un producto, una línea de investigación o una cartera de inversión; o autoridad reconocida en un campo.</span></div></li>
        <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 10.5l4 4 8-9"/></svg>
        <div><b>Disposición a aportar, no a vender.</b><span>Los encuentros no son un espacio comercial y no incluyen presentaciones de empresa.</span></div></li>
      </ul>
      {AMBITO}
    </div>
    <div class="margen">
      <div class="bloque">
        <h3>¿Conoces a alguien que encaje?</h3>
        <p class="menor">Buena parte de este talento no aparece buscando en internet. Aparece porque alguien de dentro dice a quién falta.</p>
        <p style="margin-top:16px"><a class="enlace" href="./participar.html#proponer">Proponer a una persona</a></p>
      </div>
    </div>
  </div>
</section>

<section class="banda-cielo sec">
  <div class="wrap doc">
    <div>
      <div class="linea-jade"></div>
      <h2>La primera mesa.</h2>
      <p class="entrada medida" style="margin-top:24px">Antes de construir una estructura, la iniciativa quiere comprobar que la conversación merece la pena. Por eso empieza por un solo encuentro, pequeño y privado, y todo lo demás se decidirá entre quienes participen.</p>
      <div class="cifras">
        <div><strong>10&nbsp;–&nbsp;12</strong><span>personas alrededor de una mesa</span></div>
        <div><strong>90 min</strong><span>de conversación y después, informal</span></div>
        <div><strong>Madrid</strong><span>cuarto trimestre de 2026</span></div>
        <div><strong>Sin coste</strong><span>ni cuota ni permanencia</span></div>
      </div>
      <p style="margin-top:34px" class="medida">Sin ponencias, sin moderación con reloj y sin público. Nadie presenta nada y nadie representa a nadie.</p>
      <p><a class="enlace" href="./la-mesa.html">El formato completo y a qué compromete</a></p>
    </div>
    <div class="margen">
      <p class="voz">«¿Qué está cambiando la tecnología en la vida cotidiana que nosotros vemos desde dentro y la gente todavía no?»</p>
      <p class="pie" style="margin-top:18px">Pregunta de apertura de la primera mesa.</p>
    </div>
  </div>
</section>

{CARTA}

<section class="wrap sec">
  <div class="linea-jade"></div>
  <h2 style="max-width:22ch">De lo que se va a hablar.</h2>
  <p class="entrada medida" style="margin-top:22px">No tecnología para tecnólogos. Asuntos que ya están afectando a la gente y que este grupo entiende antes que casi nadie.</p>
  {TEMAS_CORTOS}
  <p style="margin-top:32px"><a class="enlace" href="./la-mesa.html#temas">Ver los cinco temas de trabajo</a></p>
</section>

<section class="banda-hueso sec">
  <div class="wrap doc">
    <div>
      <div class="linea-jade"></div>
      <h2>Preguntas frecuentes.</h2>
      <div class="preg" style="margin-top:30px">
        <details><summary>¿Hay que tener relación profesional con Guatemala?</summary><div class="resp"><p>No. El vínculo es de origen. Lo que interesa es la trayectoria profesional actual en España. Si además hay colaboración con el país, bienvenida, pero no es un requisito ni el objetivo de la iniciativa.</p></div></details>
        <details><summary>¿Esto lo organiza la Embajada de Guatemala?</summary><div class="resp"><p>No. Es una iniciativa profesional independiente, impulsada a título personal por Madelaine Castro. La iniciativa está en contacto con instituciones guatemaltecas y españolas y agradecería su acompañamiento, pero no depende de ninguna ni representa oficialmente a Guatemala.</p></div></details>
        <details><summary>¿Cuánto cuesta y a qué compromete?</summary><div class="resp"><p>No cuesta nada y no hay cuota, ni ahora ni como condición para participar. El compromiso es una conversación previa y una tarde. Si de ahí sale algo que merezca continuidad, lo decidirán quienes participen, y quien no quiera seguir no sigue.</p></div></details>
        <details><summary>¿Se va a publicar mi nombre?</summary><div class="resp"><p>Solo con autorización previa y por escrito. Participar en una conversación no convierte a nadie en imagen pública de la iniciativa. Se puede asistir, escuchar y no aparecer en ningún sitio.</p></div></details>
        <details><summary>¿Qué se obtiene participando?</summary><div class="resp"><p>En esta primera etapa, con honestidad: no se promete negocio. Lo que hay es una sala con diez o doce profesionales de nivel equivalente que comparten algo que casi nunca puede compartirse en el trabajo, y una conversación que hoy no existe en ningún otro sitio.</p></div></details>
        <details><summary>¿Y si encajo pero no puedo asistir a esa fecha?</summary><div class="resp"><p>Conviene escribir igualmente. La iniciativa no busca llenar una fecha, busca dar con las personas adecuadas. Habrá más encuentros.</p></div></details>
        <details><summary>¿Hay que haber nacido en Guatemala?</summary><div class="resp"><p>Nacimiento o familia, ambas cosas valen. Si el vínculo con el país viene de padres o abuelos y la persona se reconoce en esto, su sitio está igual de asegurado.</p></div></details>
        <details><summary>¿Esto no lo hace ya la red de diáspora científica guatemalteca?</summary><div class="resp"><p>No, y conviene explicarlo bien porque ese trabajo existe, es serio y merece respeto. RedCTi y el proyecto de vinculación de la diáspora científica y profesional impulsado por SENACYT trabajan para conectar a profesionales guatemaltecos en el exterior con Guatemala, y el estudio publicado en 2026 sobre la diáspora en España es la primera caracterización que se ha hecho.</p><p>Esta iniciativa se ocupa de otra cosa. Reúne a profesionales cuya trayectoria y cuya aportación suceden en España, sin exigir vínculo con Guatemala, y se dirige a la capa directiva e industrial, que es justamente la que aquella metodología no podía localizar. Son dos objetivos distintos y compatibles.</p></div></details>
        <details><summary>¿Y si mi vínculo con Guatemala es muy débil?</summary><div class="resp"><p>No es un problema, es el punto de partida. Muchas de las personas a las que se dirige esta iniciativa llevan décadas aquí, no siguen la actualidad guatemalteca y no tienen ninguna colaboración con el país. Eso no las excluye. Precisamente por eso no figuran en ningún mapa existente.</p></div></details>
        <details><summary>¿Va a convertirse en una asociación?</summary><div class="resp"><p>Puede que sí y puede que no, y esa decisión no está tomada. Lo que no va a pasar es que nadie se encuentre dentro de una asociación con junta directiva y cuota anual sin haberlo votado.</p></div></details>
      </div>
    </div>
    <div class="margen">
      <div class="bloque">
        <h3>Compartir la iniciativa</h3>
        <p class="menor">La forma más eficaz de que llegue a quien tiene que llegar es que alguien se la reenvíe diciendo por qué ha pensado en esa persona.</p>
        <div class="compartir">
          <button data-compartir="nativo">Compartir</button>
          <button data-compartir="linkedin">LinkedIn</button>
          <button data-compartir="whatsapp">WhatsApp</button>
          <button data-compartir="copiar">Copiar texto</button>
        </div>
        <p class="aviso" role="status"></p>
      </div>
    </div>
  </div>
</section>

<section class="banda-tinta sec">
  <div class="wrap dos">
    <div>
      <div class="linea-jade"></div>
      <h2>No hay que afiliarse a nada. Solo hay que conocerse.</h2>
      <p style="color:#c3d2d1;margin-top:22px;max-width:48ch">El primer paso es escribir cuatro líneas. Responde directamente Madelaine Castro y lo siguiente es una conversación de veinte minutos, no un proceso de admisión.</p>
    </div>
    <div style="padding-top:14px">
      <div class="acciones pila">
        <a class="btn btn-clr" href="./participar.html#hablemos">Quiero participar</a>
        <a class="btn btn-fant" href="./participar.html#proponer">Proponer a otra persona</a>
        <a class="btn btn-fant" href="./instituciones.html">Soy una institución o una empresa</a>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- la iniciativa
INICIATIVA = f"""
<section class="wrap sec-ap">
  <div class="doc">
    <div>
      <p class="rotulo">La iniciativa</p>
      <h1 style="max-width:19ch">Una comunidad profesional que todavía no se ha reunido nunca.</h1>
      <p class="entrada medida" style="margin-top:26px">En España hay profesionales de origen guatemalteco dirigiendo áreas de tecnología en empresas nacionales y multinacionales, doctorándose e investigando en universidades españolas, fundando compañías, gestionando fondos de inversión y enseñando. No es una comunidad por descubrir: es una comunidad que no se conoce entre sí.</p>
      <p class="entrada medida">Guatemala Tech Leaders España existe para cambiar eso, y para que ese conocimiento colectivo sirva a la sociedad en la que este grupo desarrolla su trabajo.</p>
    </div>
    <div class="margen">{FICHA_INST}</div>
  </div>
</section>

<section class="banda-jade sec">
  <div class="wrap">
    <div class="linea-jade"></div>
    <h2 style="max-width:20ch">Principios.</h2>
    <p class="entrada medida" style="color:var(--cielo-clr);margin-top:22px">Cinco compromisos que definen la iniciativa desde el primer día y que cualquiera puede exigirle.</p>
    <ol class="principios">
      <li><b>Nuestro origen nos une, nuestra aportación sucede aquí.</b><span>No es una red de retorno ni una asociación basada en la nostalgia. El objetivo es contribuir a la sociedad española, que es donde este grupo vive y trabaja.</span></li>
      <li><b>Independencia.</b><span>Sin dependencia de administraciones, partidos, empresas ni patrocinadores. Sin agenda política guatemalteca ni española.</span></li>
      <li><b>Sin coste y sin cuotas.</b><span>Participar no cuesta dinero, ni ahora ni como condición futura. Nadie compra un asiento.</span></li>
      <li><b>Discreción por defecto.</b><span>Las conversaciones son privadas. Ningún nombre, foto o afiliación se publica sin autorización previa y por escrito de la persona.</span></li>
      <li><b>Utilidad antes que estructura.</b><span>Primero se comprueba que la conversación aporta algo. Solo si aporta, y solo si quienes participan lo deciden, se construirá una estructura.</span></li>
    </ol>
  </div>
</section>

<section class="wrap sec">
  <div class="linea-jade"></div>
  <h2 style="max-width:22ch">Qué es y qué no es.</h2>
  <div class="dos" style="margin-top:44px">
    <div>
      <h3 style="margin-bottom:16px">Es</h3>
      <ul class="lista-si">
        <li>Una iniciativa profesional independiente en fase de constitución.</li>
        <li>Un grupo reducido y seleccionado por trayectoria.</li>
        <li>Un espacio de conversación privada entre pares.</li>
        <li>Un punto de partida para producir cosas útiles fuera de la sala: charlas, documentos y colaboraciones.</li>
      </ul>
    </div>
    <div>
      <h3 style="margin-bottom:16px">No es</h3>
      <ul class="lista-no">
        <li>Una asociación constituida, con junta directiva o cuota.</li>
        <li>Un registro abierto ni una red de contactos comerciales.</li>
        <li>Una organización de diáspora, de cooperación o de retorno.</li>
        <li>Una entidad con representación oficial de Guatemala ni vinculada a ninguna administración.</li>
      </ul>
    </div>
  </div>
</section>

<section class="banda-hueso sec">
  <div class="wrap doc">
    <div>
      <div class="linea-jade"></div>
      <h2>Estado de la iniciativa.</h2>
      <p class="entrada medida" style="margin-top:24px">Registro público de lo hecho hasta la fecha. Ninguna etapa compromete a la siguiente.</p>
      <ol class="registro">
        <li><span class="reg-fecha">Julio de 2026</span><div><b>Se publica la primera caracterización de la diáspora científica y profesional guatemalteca en España.</b><span>Su lectura confirma la hipótesis que da origen a esta iniciativa: la capa directiva e industrial no está representada, y no por descuido, sino por el método de localización empleado.</span></div></li>
        <li><span class="reg-fecha">Agosto de 2026</span><div><b>Análisis del estudio y definición del ámbito.</b><span>Se fijan los cuatro criterios de pertenencia, los nueve campos del perímetro tecnológico y los cinco principios de la iniciativa.</span></div></li>
        <li><span class="reg-fecha">Septiembre de 2026</span><div><b>Publicación del documento de posición y de la infraestructura digital.</b><span>Desarrollada íntegramente por la impulsora, sin coste y sin proveedores.</span></div></li>
        <li><span class="reg-fecha">En curso</span><div><b>Identificación y contacto de perfiles, uno a uno.</b><span>Localización a través de fuentes públicas y, sobre todo, de recomendación personal, que es la vía que funciona en este segmento.</span></div></li>
        <li><span class="reg-fecha">Cuarto trimestre de 2026</span><div><b>Primera mesa en Madrid.</b><span>Entre diez y doce personas. A partir de ahí, quienes participen deciden si hay continuidad, en qué forma y con qué compromiso.</span></div></li>
      </ol>
    </div>
    <div class="margen">
      <div class="bloque">
        <h3>Cómo se decide quién participa</h3>
        <p class="menor">La selección la realiza hoy la impulsora, con los cuatro criterios publicados y buscando variedad de sectores, de trayectorias y de puntos de vista. A partir de la primera mesa, ese criterio pasa a decidirse de forma colegiada.</p>
      </div>
    </div>
  </div>
</section>

<section class="banda-tinta sec" id="impulsora">
  <div class="wrap">
    <div class="linea-jade"></div>
    <h2 style="max-width:22ch">Quién impulsa la iniciativa.</h2>
    <div class="impulsora">
      <div class="impulsora-foto"><img src="./assets/img/madelaine.jpg" width="760" height="950" alt="Retrato de Madelaine Castro."></div>
      <div>
        <h3 style="color:var(--papel);font-size:27px">Madelaine Castro</h3>
        <p style="color:var(--cielo);margin:6px 0 20px;font-size:15px">Secretaria General de itSMF España. Calidad, continuidad y gobierno de la tecnología en S2 Grupo.</p>
        <p style="color:#c3d2d1;max-width:54ch">Nacida en Guatemala y residente en España, donde ha desarrollado más de veinte años de carrera en tecnología. Dirige la calidad, la continuidad y el gobierno tecnológico en S2 Grupo, compañía española de ciberseguridad, con responsabilidad funcional sobre cinco marcos de certificación. Es Secretaria General de itSMF España, la asociación profesional de gestión de servicios de tecnologías de la información.</p>
        <p style="color:#c3d2d1;max-width:54ch">Impulsa esta iniciativa a título personal y con su nombre delante, precisamente para que cualquiera pueda comprobar quién la propone antes de decidir si merece su tiempo.</p>
        <div class="acciones" style="margin-top:24px">
          <a class="btn btn-clr" href="#" data-mail="Guatemala Tech Leaders España">Escribir a Madelaine</a>
          <a class="btn btn-fant" href="#" data-linkedin target="_blank" rel="noopener">Ver su perfil en LinkedIn</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="wrap sec-cp">
  <div class="dos">
    <div>
      <div class="linea-jade"></div>
      <h2 style="font-size:clamp(26px,3vw,36px)">El siguiente paso.</h2>
      <p class="medida" style="margin-top:20px">Si encajas en los criterios, o si conoces a alguien que encaje, el primer movimiento es siempre el mismo: una conversación de veinte minutos.</p>
    </div>
    <div style="padding-top:14px">
      <div class="acciones pila">
        <a class="btn btn-p" href="./participar.html#hablemos">Quiero participar</a>
        <a class="btn btn-s" href="./la-mesa.html">Ver el formato de la mesa</a>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- la mesa
MESA = f"""
<section class="wrap sec-ap">
  <div class="doc">
    <div>
      <p class="rotulo">La primera mesa</p>
      <h1 style="max-width:18ch">Antes de construir nada, una conversación que merezca continuar.</h1>
      <p class="entrada medida" style="margin-top:26px">La iniciativa podría haber empezado por unos estatutos, una junta y una web con la palabra «asociación». Es el orden equivocado. Primero hay que comprobar si, sentados en la misma habitación, este grupo tiene algo que decirse. Si lo tiene, la estructura se decide después y entre todos. Si no lo tiene, nadie habrá firmado nada.</p>
    </div>
    <div class="margen">
      <div class="bloque">
        <h3>Lo esencial</h3>
        <p class="menor" style="margin-top:10px">Entre 10 y 12 personas.<br>Noventa minutos de conversación y después un rato informal.<br>Madrid, cuarto trimestre de 2026.<br>Sin coste, sin cuota y sin compromiso de continuidad.</p>
        <p style="margin-top:16px"><a class="enlace" href="./participar.html#hablemos">Quiero participar</a></p>
      </div>
    </div>
  </div>
</section>

<section class="banda-jade sec">
  <div class="wrap doc">
    <div>
      <div class="linea-jade"></div>
      <h2>Pequeña, privada y presencial.</h2>
      <p class="entrada medida" style="color:var(--cielo-clr);margin-top:24px">Pequeña porque en una sala de cincuenta personas nadie dice nada verdadero. Privada porque el valor está en poder hablar de lo que no se cuenta en un congreso. Presencial porque después de seis años de reuniones por videollamada, esto solo funciona en el mismo sitio.</p>
      <p class="medida" style="color:var(--cielo-clr)">No hay moderación con reloj, ni turno de palabra, ni presentaciones. Se abre con una pregunta y a partir de ahí es una conversación entre profesionales.</p>
    </div>
    <div class="margen"><p class="voz" style="color:var(--cielo)">«Interesa mucho más lo que no cabe en una diapositiva.»</p></div>
  </div>
</section>

<section class="wrap sec">
  <div class="linea-jade"></div>
  <h2 style="max-width:22ch">Quién se sienta.</h2>
  <div class="tres" style="margin-top:44px">
    <div><h3>Quien dirige</h3><p>Directivas y directivos, responsables de tecnología, de seguridad, de datos o de producto, y quien tiene a su cargo una función completa dentro de una organización grande.</p></div>
    <div><h3>Quien construye o financia</h3><p>Fundadoras y fundadores, profesionales que han creado y vendido empresas, y quienes invierten en tecnología desde un fondo o a título propio.</p></div>
    <div><h3>Quien investiga o enseña</h3><p>Doctoras y doctores, personal investigador consolidado, profesorado universitario y especialistas técnicos reconocidos en su campo.</p></div>
  </div>
  <p class="entrada medida" style="margin-top:44px">Mezclar estos tres mundos es parte del experimento. En España rara vez se sientan juntos, y cuando lo hacen es en un panel con público. Aquí no hay público.</p>
</section>

<section class="banda-cielo sec" id="temas">
  <div class="wrap">
    <div class="linea-jade"></div>
    <h2 style="max-width:24ch">Cinco temas de trabajo.</h2>
    <p class="entrada medida" style="margin-top:22px">Son la propuesta de partida, no un programa cerrado. Si la mesa quiere trabajar otra cosa, trabajará otra cosa.</p>
    <div class="temas">
      <article class="tema"><div><h3>Nuestros hijos frente a la inteligencia artificial</h3><p>Privacidad, aprendizaje, fraude, dependencia y criterio. Qué necesitan saber las familias, y qué papel les corresponde a colegios, empresas y administraciones.</p></div><span class="et">IA y educación</span></article>
      <article class="tema"><div><h3>Nos están estafando por WhatsApp</h3><p>Cómo ha cambiado el fraude en los últimos tres años, qué está viendo desde dentro quien trabaja en seguridad, y qué debería saber cualquiera que tenga un móvil.</p></div><span class="et">Ciberseguridad</span></article>
      <article class="tema"><div><h3>¿Puede una empresa obligar a usar inteligencia artificial?</h3><p>Productividad, responsabilidad, privacidad y límites organizativos de una adopción que va mucho más rápido que las reglas.</p></div><span class="et">IA y trabajo</span></article>
      <article class="tema"><div><h3>¿Quién responde cuando decide un algoritmo?</h3><p>Qué ocurre con la responsabilidad cuando se automatizan decisiones y queda repartida entre tecnología, negocio, proveedor y dirección, de forma que al final no la asume nadie.</p></div><span class="et">Gobierno y riesgo</span></article>
      <article class="tema"><div><h3>Qué empleos va a cambiar de verdad la IA y cuáles no</h3><p>Separar el titular de la transformación real, desde la experiencia de quienes ya la están implantando dentro de organizaciones y ven qué funciona y qué no.</p></div><span class="et">Talento y empresa</span></article>
    </div>
  </div>
</section>

<section class="wrap sec">
  <div class="doc">
    <div>
      <div class="linea-jade"></div>
      <h2>Y después de esa tarde, ¿qué?</h2>
      <p class="entrada medida" style="margin-top:24px">Lo decide la mesa. Estos son los tres escenarios posibles, en orden de probabilidad.</p>
      <ol class="pasos">
        <li><div><b>Que no haya continuidad.</b><span>Es un resultado legítimo. Se habrán conocido diez personas que no se conocían y cada una sigue con su trabajo.</span></div></li>
        <li><div><b>Que haya más encuentros.</b><span>Otra mesa, en otra ciudad, con otras personas o con las mismas. Sin estructura, sin cuota y sin papeles.</span></div></li>
        <li><div><b>Que salga algo que merezca hacerse público.</b><span>Una charla abierta, un documento breve, una guía para familias o una colaboración con una universidad, un colegio, una empresa o una administración. Solo si es útil de verdad.</span></div></li>
      </ol>
      <p class="medida" style="margin-top:32px">Lo que no va a ocurrir es que nadie se encuentre, sin haberlo decidido, dentro de una asociación con junta directiva, cuota anual y logotipo. Si algún día existe algo así, se habrá votado.</p>
    </div>
    <div class="margen">
      <div class="bloque">
        <h3>El compromiso exacto</h3>
        <p class="menor" style="margin-top:10px">Manifestar interés compromete a una sola cosa: una conversación de veinte minutos. Ni afiliación, ni pago, ni presencia pública, ni obligación de asistir si finalmente no encaja.</p>
        <p style="margin-top:18px"><a class="btn btn-p" href="./participar.html#hablemos" style="width:100%">Escribir</a></p>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- instituciones
INSTITUCIONES = f"""
<section class="wrap sec-ap">
  <div class="doc">
    <div>
      <p class="rotulo">Instituciones, universidades y empresas</p>
      <h1 style="max-width:18ch">Hay una generación guatemalteca dirigiendo tecnología en España. Casi nadie lo ha contado.</h1>
      <p class="entrada medida" style="margin-top:26px">Cuando se habla de la comunidad guatemalteca en Europa se habla, casi siempre, de cooperación, de cultura o de trámites. Se habla muy poco de que hay guatemaltecas y guatemaltecos dirigiendo áreas de tecnología en empresas españolas, doctorándose en universidades de aquí, fundando compañías y gestionando fondos de inversión.</p>
      <p class="entrada medida">Esa historia no se ha contado nunca, porque las personas que la protagonizan no se conocen entre sí. Guatemala Tech Leaders España está constituyendo una primera mesa de diez o doce para empezar a cambiarlo.</p>
    </div>
    <div class="margen">{FICHA_INST}</div>
  </div>
</section>

<section class="banda-jade sec">
  <div class="wrap doc">
    <div>
      <div class="linea-jade"></div>
      <h2>Lo que la iniciativa no pide.</h2>
      <p class="entrada medida" style="color:var(--cielo-clr);margin-top:24px">Conviene empezar por aquí, porque es lo que más facilita la conversación. Esta iniciativa no necesita presupuesto y no compromete a nadie.</p>
      <ul class="criterios criterios-no" style="margin-top:26px">
        <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 5l10 10M15 5L5 15"/></svg>
        <div><b>No solicita financiación.</b><span>Ni ahora ni como condición futura. La primera mesa no tiene coste y lo poco que requiera lo asume la impulsora.</span></div></li>
        <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 5l10 10M15 5L5 15"/></svg>
        <div><b>No solicita respaldo oficial ni aval de personas.</b><span>Ninguna institución tiene que validar a los participantes ni responder de lo que digan.</span></div></li>
        <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 5l10 10M15 5L5 15"/></svg>
        <div><b>No tiene agenda política.</b><span>No se debate política guatemalteca ni española, y la iniciativa no representa oficialmente a Guatemala.</span></div></li>
        <li><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 5l10 10M15 5L5 15"/></svg>
        <div><b>No plantea transferencia de conocimiento a Guatemala.</b><span>La aportación de estas personas sucede en España. Si con el tiempo alguien quiere hacer algo para el país, será decisión suya.</span></div></li>
      </ul>
    </div>
    <div class="margen"><p class="voz" style="color:var(--cielo)">«Es una iniciativa independiente, pero no quiere estar sola.»</p></div>
  </div>
</section>

<section class="banda-cielo sec">
  <div class="wrap doc">
    <div>
      <div class="linea-jade"></div>
      <h2>Un diagnóstico ya publicado.</h2>
      <p class="entrada medida" style="margin-top:24px">En julio de 2026, la revista <em>Frontiers in Research Metrics and Analytics</em> publicó la primera caracterización de la diáspora científica y profesional guatemalteca en España, dentro de un proyecto liderado por SENACYT con apoyo de la Unión Europea y de la AECID.</p>
      <p class="medida">Dos de sus hallazgos son directamente pertinentes para cualquier institución guatemalteca en España. El primero: las personas participantes describieron su relación con la misión diplomática como mínima, inexistente o limitada a trámites administrativos. El segundo: el 89&nbsp;% considera que no existe ningún registro sistemático de esta población, y señalan al MINEX, SENACYT, SEGEPLAN y el INE como responsables de construirlo.</p>
      <p class="medida">Esta iniciativa no resuelve ese problema, que es de política pública. Pero atiende un segmento concreto que aquel estudio, por su método, no podía alcanzar, y lo hace sin coste público y sin comprometer a ninguna institución.</p>
      <p style="margin-top:26px"><a class="enlace" href="./posicion.html">Leer el documento de posición completo</a></p>
    </div>
    <div class="margen">
      <div class="bloque">
        <h3>Referencia</h3>
        <p class="pie" style="margin-top:10px">Bonilla, K., Romero-Oliva, C. S., Arrechea, S., Castillo-Zamora, J. M. y Destarac, M. A. (2026). Frontiers in Research Metrics and Analytics, 11:1860284. Acceso abierto.</p>
        <p style="margin-top:12px"><a class="enlace" href="https://doi.org/10.3389/frma.2026.1860284" target="_blank" rel="noopener" style="font-size:14px">Consultar el estudio</a></p>
      </div>
    </div>
  </div>
</section>

<section class="wrap sec">
  <div class="linea-jade"></div>
  <h2 style="max-width:22ch">Tres formas de acompañarla.</h2>
  <p class="entrada medida" style="margin-top:22px">De menor a mayor implicación. Cualquiera de las tres es suficiente, y la primera no tiene coste alguno.</p>
  <div class="tres" style="margin-top:46px">
    <div><h3>Verlo de cerca</h3><p>Asistir a la primera mesa como observadora u observador, sin intervenir ni presidir. Conocer en una sola tarde a diez o doce profesionales guatemaltecos de alto nivel en España que, en muchos casos, no figuran en ningún registro ni en ninguna lista.</p></div>
    <div><h3>Prestar la sala</h3><p>Ceder un espacio para una tarde: una sala de reuniones, un aula, un salón de actos. Es hoy la aportación más útil que puede hacerse a la iniciativa y no compromete a nada más.</p></div>
    <div><h3>Dar visibilidad</h3><p>Compartir esta página con quien pueda encajar. Buena parte del talento que se busca no aparece en un buscador: aparece porque alguien dice «yo conozco a esta persona».</p></div>
  </div>
</section>

<section class="banda-hueso sec">
  <div class="wrap doc">
    <div>
      <div class="linea-jade"></div>
      <h2>Para empresas, universidades y centros educativos.</h2>
      <p class="entrada medida" style="margin-top:24px">La mesa no es un fin en sí misma. Si de las conversaciones sale conocimiento que sirva a alguien, el compromiso es sacarlo de la sala.</p>
      <p class="medida">Puede tomar la forma de una charla abierta sobre menores e inteligencia artificial para una comunidad educativa, una sesión sobre fraude digital para plantillas o para familias, una mesa redonda universitaria, o un documento breve y sin jerga sobre alguno de los temas de trabajo. Sin coste y sin contrapartida comercial: la razón de ser de la iniciativa es aportar algo aquí.</p>
      <p style="margin-top:26px"><a class="enlace" href="./la-mesa.html#temas">Ver los temas de trabajo</a></p>
    </div>
    <div class="margen">
      <div class="bloque">
        <h3>Contacto institucional</h3>
        <p class="menor" style="margin-top:10px">Responde directamente Madelaine Castro. Si prefiere una llamada de veinte minutos antes de nada, basta con indicarlo en el mensaje.</p>
        <p style="margin-top:18px"><a class="btn btn-p" style="width:100%" href="#" data-mail="Instituciones · Guatemala Tech Leaders España">Escribir</a></p>
        <p class="pie" style="margin-top:14px"><span data-mail-texto></span></p>
      </div>
    </div>
  </div>
</section>

<section class="banda-tinta sec-cp">
  <div class="wrap dos">
    <div>
      <div class="linea-jade"></div>
      <h2 style="font-size:clamp(26px,3vw,36px)">Quién responde de la iniciativa.</h2>
      <p style="color:#c3d2d1;margin-top:20px;max-width:46ch">Guatemala Tech Leaders España la impulsa a título personal Madelaine Castro, nacida en Guatemala y con más de veinte años de carrera en tecnología en España. Dirige la calidad, la continuidad y el gobierno tecnológico en S2 Grupo, compañía española de ciberseguridad, y es Secretaria General de itSMF España.</p>
      <div class="firma">
        <img src="./assets/img/madelaine.jpg" alt="" aria-hidden="true">
        <div><b>Madelaine Castro</b><span>Impulsora de la iniciativa</span></div>
      </div>
    </div>
    <div style="padding-top:14px">
      <div class="acciones pila">
        <a class="btn btn-clr" href="#" data-mail="Instituciones · Guatemala Tech Leaders España">Escribir a Madelaine</a>
        <a class="btn btn-fant" href="./la-iniciativa.html">Conocer la iniciativa</a>
        <button class="btn btn-fant" data-compartir="nativo">Compartir esta página</button>
      </div>
      <p class="aviso" role="status" style="color:var(--cielo)"></p>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- documento de posición
POSICION = """
<section class="wrap sec-ap documento">
  <p class="rotulo">Documento de posición · Septiembre de 2026</p>
  <h1 style="max-width:19ch">El vacío en el mapa de la diáspora profesional guatemalteca en España.</h1>
  <div class="doc" style="margin-top:34px">
    <div>
      <div class="resumen">
        <h2>En resumen</h2>
        <p>En julio de 2026 se publicó la primera caracterización académica de la diáspora científica y profesional guatemalteca en España. Su método de localización, apoyado en canales académicos, produce un retrato del carril investigador y becario. La capa directiva e industrial &mdash;profesionales con quince o veinticinco años de trayectoria en empresas españolas, personas fundadoras e inversoras&mdash; queda fuera de forma estructural, no accidental.</p>
        <p>A ese segmento se suma una diferencia de fondo: aquel estudio define la pertenencia a la diáspora, entre otros criterios, por mantener vínculos de transferencia de conocimiento con Guatemala. Una parte importante de estos profesionales no los tiene, porque su vida y su aportación suceden íntegramente en España.</p>
        <p>Guatemala Tech Leaders España nace para ocupar ese espacio, sin duplicar ni competir con el trabajo existente.</p>
      </div>

      <h2>1. El estudio</h2>
      <p>El 16 de julio de 2026, la revista <em>Frontiers in Research Metrics and Analytics</em> publicó <em>Guatemala scientific and professional diaspora in Spain: an initial characterization</em>, firmado por Kleinsy Bonilla, Claudia S. Romero-Oliva, Susana Arrechea, Juan Manuel Castillo-Zamora y Marie André Destarac. Forma parte del proyecto de vinculación de la diáspora científica y profesional guatemalteca liderado por SENACYT y la Academia de Ciencias Médicas, Físicas y Naturales de Guatemala, con apoyo del Global Diaspora Facility de la Unión Europea y de la AECID.</p>
      <p>Es el primer trabajo que caracteriza a esta población en España y merece ser reconocido como tal. Construyó una base de 111 personas, obtuvo 51 cuestionarios completos y reunió un grupo focal de 25. Sus autoras y autores declaran expresamente que se trata de una muestra no probabilística y autoseleccionada, y que sobrerrepresenta a las personas más conectadas institucionalmente y más visibles digitalmente.</p>
      <p>Este documento parte de esa limitación, declarada por el propio estudio, y sostiene que describe un segmento concreto y localizable de la población que queda al otro lado.</p>

      <h2>2. Lo que el método puede ver y lo que no</h2>
      <p>La convocatoria del estudio se difundió a través de redes personales del equipo investigador, correo electrónico, LinkedIn, Google Scholar, ResearchGate y las cuentas de SENACYT y RedCTi. Es un procedimiento razonable y estándar. También determina qué tipo de persona puede aparecer.</p>
      <p>Google Scholar y ResearchGate indexan producción científica. Una directora de continuidad de negocio en una empresa española de ciberseguridad no tiene producción científica indexada. Un gestor de un fondo de capital riesgo tampoco. Un fundador que ha construido y vendido dos compañías, tampoco. No son perfiles poco visibles: son perfiles visibles en otro sitio.</p>
      <p>Los resultados lo reflejan. Entre las 51 personas encuestadas, el 26&nbsp;% tenía entre 20 y 30 años y el 45&nbsp;% entre 31 y 40. Más de la mitad seguía estudiando y aproximadamente un tercio trabajaba. En el ámbito de negocio se registraron seis personas, todas hombres y todas con financiación propia.</p>
      <p>Ese es el retrato de una población en formación o en consolidación temprana, llegada mayoritariamente por vía de beca. Es un retrato válido y útil. Simplemente no es el de quien lleva veinticinco años dirigiendo en España.</p>

      <h2>3. La cuestión del cuarto criterio</h2>
      <p>El estudio considera miembro de la diáspora a quien cumple cuatro condiciones: ser nacional guatemalteco, haber residido más de un año en España, ejercer actividades profesionales o altamente cualificadas y mantener vínculos de transferencia de conocimiento con Guatemala.</p>
      <p>Los tres primeros criterios describen una situación. El cuarto describe una orientación, y es el que marca la frontera. Todo el marco institucional de diáspora, en Guatemala y en la literatura internacional sobre el asunto, está construido para que el conocimiento de quienes se fueron revierta en el país de origen. Es un objetivo legítimo y valioso.</p>
      <p>Pero hay un grupo numeroso de profesionales guatemaltecos en España que no cumple ese cuarto criterio y no va a cumplirlo. No siguen la actualidad guatemalteca, no colaboran con instituciones del país y no tienen intención de volver. Llevan aquí quince, veinte o veinticinco años. Sus hijos son españoles. Sus equipos son españoles. Lo que les preocupa es lo que le preocupa a cualquiera que viva en este país.</p>
      <p>Bajo la definición vigente, esas personas no son diáspora científica y profesional guatemalteca. Y probablemente sea correcto que no lo sean. El problema es que tampoco son ninguna otra cosa: no existe ninguna categoría, ningún registro y ninguna red que las contemple.</p>

      <h2>4. Un segmento que se define por España</h2>
      <p>La propuesta de este documento es sencilla: ese grupo debe definirse por su aportación en España, no por su vínculo con Guatemala.</p>
      <p>El origen guatemalteco compartido no es el asunto sobre el que hay que trabajar. Es únicamente el mecanismo que permite que estas personas se reconozcan entre sí, y no es poca cosa: en un país donde el colectivo guatemalteco es reducido, ese vínculo es lo único que hace que una directiva de una multinacional y un inversor de fintech se sienten a la misma mesa sin que medie una transacción.</p>
      <p>Lo que ocurre después de sentarse pertenece a España. Qué está cambiando la tecnología en la vida cotidiana de este país, qué necesitan saber las familias sobre la inteligencia artificial y sus hijos, cómo ha cambiado el fraude digital, quién responde cuando decide un algoritmo. Ese es el trabajo.</p>

      <h2>5. Qué propone esta iniciativa</h2>
      <p>Guatemala Tech Leaders España se constituye para reunir a ese segmento, con cuatro criterios propios: ejercicio profesional actual en España, origen guatemalteco por nacimiento o por familia, responsabilidad directiva o reconocimiento técnico, y disposición a aportar sin ánimo comercial. No se exige vínculo con Guatemala ni nacionalidad vigente.</p>
      <p>El método es deliberadamente pequeño. Una primera mesa de diez o doce personas, noventa minutos, en Madrid, sin coste, sin cuota y sin compromiso de continuidad. Primero se comprueba que la conversación aporta algo; solo después, y solo si quienes participan lo deciden, se construye una estructura.</p>
      <p>Es pertinente señalar que la debilidad de las redes profesionales estructuradas figura entre los cinco obstáculos que el propio estudio de 2026 identifica, y que su apartado de discusión reclama expresamente redes profesionales transnacionales y mecanismos de vinculación. Esta iniciativa es una respuesta parcial a esa recomendación, en el segmento al que aquel trabajo no podía llegar.</p>

      <h2>6. Relación con el trabajo existente</h2>
      <p>Esta iniciativa no compite con RedCTi, ni con el proyecto de vinculación de la diáspora científica y profesional impulsado por SENACYT, ni con el equipo que firma el estudio de 2026. No busca sustituirlos, no reclama su ámbito y no pretende hablar en su nombre.</p>
      <p>Ocupa un espacio contiguo y vacío, y aspira a que las dos cosas se conozcan. Quien encaje en ambas descripciones no tiene que elegir.</p>
      <p>También conviene registrar una observación que el estudio hace sobre sí mismo y que esta iniciativa hereda agravada: el 95&nbsp;% de sus participantes se identificó como mestizo o ladino y la población indígena está prácticamente ausente, en un contexto de movilidad internacional que sus autoras describen como marcadamente elitista y excluyente. Una mesa seleccionada por responsabilidad directiva reproducirá ese sesgo con más intensidad todavía. No es un problema que esta iniciativa pueda resolver por sí sola ni convocando a personas que no existen, pero sí debe nombrarlo y no presentar su composición como un retrato de nada.</p>

      <h2>Referencia</h2>
      <p class="menor">Bonilla, K., Romero-Oliva, C. S., Arrechea, S., Castillo-Zamora, J. M. y Destarac, M. A. (2026). <em>Guatemala scientific and professional diaspora in Spain: an initial characterization</em>. Frontiers in Research Metrics and Analytics, 11:1860284. Acceso abierto.<br>
      <a class="enlace" href="https://doi.org/10.3389/frma.2026.1860284" target="_blank" rel="noopener">doi.org/10.3389/frma.2026.1860284</a></p>
      <p class="menor" style="margin-top:18px">Este documento cita ese estudio como fuente. No implica respaldo, revisión ni vinculación alguna por parte de sus autores, de SENACYT ni de ninguna de las instituciones mencionadas.</p>

      <div class="firma" style="margin-top:40px">
        <img src="./assets/img/madelaine.jpg" alt="Retrato de Madelaine Castro.">
        <div><b>Madelaine Castro</b><span>Impulsora de la iniciativa. Valencia, septiembre de 2026.</span></div>
      </div>
    </div>

    <div class="margen">
      <div class="bloque">
        <h3>Si estás leyendo esto porque conoces el estudio</h3>
        <p class="menor">Y crees que este documento se equivoca en algo, o que hay una forma mejor de plantearlo, escríbeme. Prefiero corregirlo ahora que defenderlo después.</p>
        <p style="margin-top:16px"><a class="enlace" href="#" data-mail="Sobre el documento de posición">Escribirme</a></p>
      </div>
      <div class="bloque" style="margin-top:22px">
        <h3>Compartir</h3>
        <div class="compartir">
          <button data-compartir="nativo">Compartir</button>
          <button data-compartir="linkedin">LinkedIn</button>
          <button data-compartir="copiar">Copiar</button>
        </div>
        <p class="aviso" role="status"></p>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- participar
PARTICIPAR = """
<section class="wrap sec-ap" id="hablemos">
  <div class="doc">
    <div>
      <p class="rotulo">Participar</p>
      <h1 style="max-width:16ch">No es una candidatura. Es una conversación.</h1>
      <p class="entrada medida" style="margin-top:26px">La vía más rápida y la preferida: escribir cuatro líneas contando quién eres, a qué te dedicas y por qué te ha llamado la atención la iniciativa. Responde directamente Madelaine Castro, normalmente en un par de días.</p>
      <div class="acciones" style="margin-top:30px">
        <a class="btn btn-p" href="#" data-mail="Participar en Guatemala Tech Leaders España">Escribir un correo</a>
        <a class="btn btn-s" href="#" data-linkedin target="_blank" rel="noopener">Mensaje por LinkedIn</a>
      </div>
      <p class="pie" style="margin-top:14px">Correo de contacto: <span data-mail-texto></span></p>
      <ol class="pasos" style="margin-top:44px">
        <li><div><b>Escribes.</b><span>Con lo mínimo: nombre, a qué te dedicas y qué te ha hecho parar en esta página.</span></div></li>
        <li><div><b>Conversación de veinte minutos.</b><span>Por teléfono o videollamada, para conoceros y para que valores tú también si te encaja. Funciona en las dos direcciones.</span></div></li>
        <li><div><b>Cierre de la mesa.</b><span>Se busca variedad de sectores, de trayectorias y de puntos de vista, no orden de llegada. Si no entras en la primera, se te dice con la misma claridad y se cuenta contigo para la siguiente.</span></div></li>
      </ol>
    </div>
    <div class="margen">
      <aside class="tarjeta-form">
        <h3 style="margin-bottom:6px">Formulario de contacto</h3>
        <p class="pie" style="margin-bottom:20px">Lo mismo, pero ordenado. No es una solicitud de admisión.</p>
        <form class="form" data-tipo="participar" data-asunto="Participar en Guatemala Tech Leaders España">
          <div class="campo"><label for="p1">Nombre</label><input id="p1" name="nombre" required autocomplete="name"></div>
          <div class="campo"><label for="p2">Cargo o función</label><input id="p2" name="cargo" required></div>
          <div class="campo"><label for="p3">Empresa o institución</label><input id="p3" name="organizacion"></div>
          <div class="campo"><label for="p4">Ciudad</label><input id="p4" name="ciudad" required></div>
          <div class="campo"><label for="p5">Área tecnológica</label><input id="p5" name="area" required></div>
          <div class="campo"><label for="p6">LinkedIn o web profesional</label><input id="p6" name="perfil" inputmode="url"></div>
          <div class="campo"><label for="p7">¿Por qué te interesa o qué crees que puedes aportar?</label><textarea id="p7" name="mensaje" required></textarea></div>
          <div class="consent"><input type="checkbox" id="p8" name="consent" required>
          <label for="p8">He leído el <a class="enlace" href="./legal.html#privacidad" style="font-size:14px">aviso de privacidad</a> y acepto que se usen estos datos únicamente para ponerse en contacto conmigo.</label></div>
          <button class="btn btn-p" type="submit">Enviar</button>
        </form>
        <p class="aviso" role="status"></p>
      </aside>
    </div>
  </div>
</section>

<section class="banda-jade sec" id="proponer">
  <div class="wrap doc">
    <div>
      <div class="linea-jade"></div>
      <h2>¿Conoces a alguien que debería estar en esa mesa?</h2>
      <p class="entrada medida" style="color:var(--cielo-clr);margin-top:24px">Es probablemente la ayuda más valiosa que puede prestarse a la iniciativa. Buscando por cuenta propia se llega hasta donde llega un buscador. A las personas que de verdad importan se llega porque alguien dice «yo conozco a esta persona».</p>
      <p class="medida" style="color:var(--cielo-clr)">No hace falta una ficha completa: un nombre, un enlace público y el motivo por el que has pensado en ella es suficiente para empezar. Y si lo prefieres, no la propongas: reenvíale esta página directamente. Muchas veces funciona mejor.</p>
      <div class="compartir" style="margin-top:28px">
        <button class="btn btn-clr" data-compartir="nativo">Reenviar la iniciativa</button>
        <button class="btn btn-fant" data-compartir="linkedin">LinkedIn</button>
        <button class="btn btn-fant" data-compartir="whatsapp">WhatsApp</button>
        <button class="btn btn-fant" data-compartir="copiar">Copiar texto y enlace</button>
      </div>
      <p class="aviso" role="status" style="color:var(--cielo)"></p>
    </div>
    <div class="margen">
      <aside class="tarjeta-form">
        <h3 style="margin-bottom:6px">Proponer a una persona</h3>
        <p class="pie" style="margin-bottom:20px">Solo información profesional que ya sea pública, por favor.</p>
        <form class="form" data-tipo="proponer" data-asunto="Propuesta de persona para la primera mesa">
          <div class="campo"><label for="q1">Nombre de la persona</label><input id="q1" name="nombre" required></div>
          <div class="campo"><label for="q2">Cargo o función</label><input id="q2" name="cargo"></div>
          <div class="campo"><label for="q3">Empresa o institución</label><input id="q3" name="organizacion"></div>
          <div class="campo"><label for="q4">LinkedIn o web pública</label><input id="q4" name="perfil" inputmode="url"></div>
          <div class="campo"><label for="q5">¿Por qué has pensado en ella?</label><textarea id="q5" name="mensaje" required></textarea></div>
          <div class="campo"><label for="q6">Tu nombre</label><input id="q6" name="persona" required></div>
          <div class="consent"><input type="checkbox" id="q7" name="consent" required>
          <label for="q7">Entiendo que solo debo enviar información profesional pública y que se contactará a esa persona informándola de quién la ha propuesto.</label></div>
          <button class="btn btn-p" type="submit">Enviar la propuesta</button>
        </form>
        <p class="aviso" role="status"></p>
      </aside>
    </div>
  </div>
</section>

<section class="wrap sec-cp">
  <div class="doc">
    <div>
      <div class="linea-jade"></div>
      <h2 style="font-size:clamp(26px,3vw,36px)">Qué se hace con la información que envías.</h2>
      <p class="medida" style="margin-top:20px">Se usa para contactar contigo y para nada más. No hay lista de correo, no se comparten datos con otros participantes sin autorización, no se publica ningún nombre sin permiso escrito y puedes pedir que se borre todo en cualquier momento escribiendo a la misma dirección.</p>
      <p class="medida">Si propones a otra persona, cuando se la contacte se le indicará quién habló de ella, salvo que pidas lo contrario. Es la única forma decente de hacerlo.</p>
      <p style="margin-top:22px"><a class="enlace" href="./legal.html#privacidad">Leer el aviso de privacidad completo</a></p>
    </div>
    <div class="margen">
      <div class="firma">
        <img src="./assets/img/madelaine.jpg" alt="Retrato de Madelaine Castro.">
        <div><b>Madelaine Castro</b><span>Responde ella, no un buzón.</span></div>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- legal
LEGAL = """
<section class="wrap sec-ap legal">
  <p class="rotulo">Información legal</p>
  <h1 style="font-size:clamp(32px,4vw,46px)">Aviso legal y privacidad</h1>
  <p class="entrada" style="margin-top:20px;max-width:60ch">Escrito para que se entienda. Si algo no queda claro, basta con escribir y se explica.</p>

  <h2 id="aviso">Responsable de este sitio</h2>
  <p><strong>Guatemala Tech Leaders España</strong> es una iniciativa profesional independiente impulsada a título personal por <strong>Madelaine Castro</strong>, de origen guatemalteco y residente en España. No es una asociación constituida, no es una empresa y no tiene actividad económica: no se vende nada, no se cobra nada y no hay publicidad.</p>
  <p>No está vinculada oficialmente a la Embajada de Guatemala en España, a ninguna administración española o guatemalteca, ni a la empresa en la que trabaja la impulsora. Las opiniones expresadas aquí son personales.</p>
  <p>Contacto: <a class="enlace" href="#" data-mail="Consulta legal o de privacidad"><span data-mail-texto></span></a></p>

  <h2>Contenido y propiedad</h2>
  <p>Los textos, la identidad visual y las imágenes de este sitio son de elaboración propia. Puede citarse, enlazarse y reenviarse libremente: es exactamente lo que se espera. Solo se pide que no se reproduzca alterando su sentido ni se presente como una iniciativa oficial de ninguna institución.</p>

  <h2 id="privacidad">Qué datos se recogen y para qué</h2>

  <h3>Si escribes o rellenas un formulario</h3>
  <p>Se recogen los datos que decidas facilitar: nombre, cargo, organización, ciudad, área profesional, perfil público y el contenido del mensaje.</p>
  <ul>
    <li><strong>Finalidad:</strong> únicamente ponerse en contacto contigo, valorar conjuntamente si encaja tu participación y organizar los encuentros.</li>
    <li><strong>Base legal:</strong> tu consentimiento, que otorgas al marcar la casilla o al escribir directamente.</li>
    <li><strong>Quién accede:</strong> solo Madelaine Castro. No hay equipo, ni proveedor de marketing, ni lista de distribución.</li>
    <li><strong>Conservación:</strong> mientras la iniciativa siga activa o hasta que solicites su supresión. Si finalmente no hay mesa, se eliminan.</li>
    <li><strong>Cesiones:</strong> ninguna. No se comparten tus datos con otros participantes salvo autorización expresa, ni con instituciones, ni con terceros.</li>
    <li><strong>Publicación:</strong> no se publica tu nombre, tu fotografía ni tu empresa sin autorización previa y por escrito. Participar en una conversación no convierte a nadie en imagen pública de la iniciativa.</li>
  </ul>

  <h3>Si propones a otra persona</h3>
  <p>Esto merece un apartado propio porque afecta a alguien que no está leyendo esto.</p>
  <ul>
    <li>Se pide enviar <strong>solo información profesional que ya sea pública</strong>: nombre, cargo y perfil público.</li>
    <li>Al contactar con esa persona se le indicará desde el primer mensaje quién la propuso, qué información se tiene y de dónde procede, conforme al artículo 14 del Reglamento General de Protección de Datos.</li>
    <li>Si esa persona no desea que se conserve nada, se elimina en el momento y no se le vuelve a escribir.</li>
    <li>No se construyen listas ni bases de datos de personas que no hayan manifestado interés.</li>
  </ul>

  <h3>Tus derechos</h3>
  <p>Puedes solicitar en cualquier momento acceso a tus datos, su rectificación, su supresión, la limitación de su tratamiento o su portabilidad. Basta con escribir a la dirección de contacto. Si consideras que no se ha atendido correctamente, puedes reclamar ante la Agencia Española de Protección de Datos (<a class="enlace" href="https://www.aepd.es" target="_blank" rel="noopener">aepd.es</a>).</p>

  <h2>Cookies, analítica y servicios externos</h2>
  <p>Este sitio <strong>no usa cookies</strong>, no tiene analítica, no incorpora píxeles de seguimiento y no incrusta contenido de terceros. Las tipografías están alojadas en el propio servidor, de modo que tampoco se envía tu dirección IP a Google ni a ningún otro proveedor de fuentes. Por eso no verás banner de cookies: no hay nada que consentir.</p>
  <p>Los únicos elementos externos son los botones de compartir, y solo actúan si los pulsas: en ese momento se abre WhatsApp o LinkedIn en una pestaña nueva y se aplican las condiciones de esos servicios.</p>
  <p>El sitio está alojado en GitHub Pages, que como cualquier servidor registra las peticiones que recibe.</p>

  <h2>Actualizaciones</h2>
  <p>Cualquier cambio relevante de este aviso se publicará aquí. Última revisión: 2026.</p>

  <p style="margin-top:44px"><a class="enlace" href="./index.html">Volver al inicio</a></p>
</section>
"""

# ================================================================ salida
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    if os.path.exists("/home/claude/assets_src"):
        shutil.rmtree(os.path.join(OUT, "assets"), ignore_errors=True)
        shutil.copytree("/home/claude/assets_src", os.path.join(OUT, "assets"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: " + BASE + "sitemap.xml\n")
    paginas_map = ["", "la-iniciativa.html", "posicion.html", "la-mesa.html", "instituciones.html", "participar.html"]
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for i, u in enumerate(paginas_map):
            f.write(f"  <url><loc>{BASE}{u}</loc><priority>{'1.0' if i == 0 else '0.8'}</priority></url>\n")
        f.write("</urlset>\n")

    pagina("index.html",
           "Guatemala Tech Leaders España — Liderazgo tecnológico guatemalteco en España",
           "Iniciativa profesional independiente que reúne a profesionales de origen guatemalteco que dirigen, fundan, investigan o invierten en tecnología en España. Constitución de la primera mesa, 2026.",
           "Guatemala Tech Leaders España",
           "El liderazgo tecnológico guatemalteco en España existe. Todavía no se conoce entre sí. Constitución de la primera mesa, Madrid 2026.",
           INDEX)

    pagina("la-iniciativa.html",
           "La iniciativa — Guatemala Tech Leaders España",
           "Qué es Guatemala Tech Leaders España, sus cinco principios, su ámbito, sus etapas y quién la impulsa.",
           "Una comunidad profesional que todavía no se ha reunido nunca",
           "Principios, ámbito, etapas y gobierno de Guatemala Tech Leaders España.",
           INICIATIVA)

    pagina("la-mesa.html",
           "La primera mesa — Guatemala Tech Leaders España",
           "Formato de la primera mesa: diez o doce personas, noventa minutos, Madrid, sin coste y sin compromiso de continuidad. Y los cinco temas de trabajo.",
           "Una tarde, noventa minutos y ninguna ponencia",
           "Diez o doce profesionales de origen guatemalteco que dirigen, fundan, investigan o invierten en tecnología en España.",
           MESA)

    pagina("instituciones.html",
           "Instituciones y empresas — Guatemala Tech Leaders España",
           "Para embajadas, universidades, centros educativos y empresas: qué es la iniciativa, qué no pide y de qué tres formas concretas puede acompañarse.",
           "Hay una generación guatemalteca dirigiendo tecnología en España",
           "Qué es la iniciativa, qué no pide y de qué tres formas concretas puede acompañarse.",
           INSTITUCIONES)

    pagina("posicion.html",
           "El vacío en el mapa — Guatemala Tech Leaders España",
           "Documento de posición: por qué la capa directiva e industrial de los profesionales guatemaltecos en España queda fuera de la cartografía existente de la diáspora, y qué propone esta iniciativa.",
           "El vacío en el mapa de la diáspora profesional guatemalteca en España",
           "Por qué la capa directiva e industrial queda fuera de la cartografía existente, y qué propone esta iniciativa.",
           POSICION)

    pagina("participar.html",
           "Participar — Guatemala Tech Leaders España",
           "Manifiesta tu interés en la primera mesa o propón a alguien que creas que debería estar. No es una candidatura, es una conversación.",
           "No es una candidatura. Es una conversación.",
           "Manifiesta tu interés en la primera mesa o propón a alguien que creas que debería estar.",
           PARTICIPAR)

    pagina("legal.html",
           "Aviso legal y privacidad — Guatemala Tech Leaders España",
           "Aviso legal y política de privacidad de Guatemala Tech Leaders España.",
           "Aviso legal y privacidad",
           "Aviso legal y política de privacidad de Guatemala Tech Leaders España.",
           LEGAL, noindex=True, precarga=False)

    with open(os.path.join(OUT, "assets/img/mark.svg"), "w") as f:
        f.write(marca_svg(cls="").replace('class="" ', "").replace("currentColor", "#2c5d57"))

    print("páginas generadas:", sorted(x for x in os.listdir(OUT) if x.endswith(".html")))

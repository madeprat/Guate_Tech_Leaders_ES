# Guatemala Tech Leaders España

Sitio institucional de la iniciativa. Estático, sin dependencias, sin build, sin cookies y sin peticiones a servidores externos.

---

## ⚠️ ANTES DE SUBIRLO: dos líneas que tienes que cambiar

Abre `assets/site.js`. Lo primero del archivo son las únicas dos líneas que hay que tocar:

```js
email:    "hola@ejemplo.com",                        ← el correo de contacto
linkedin: "https://www.linkedin.com/in/TU-PERFIL",   ← la URL de tu LinkedIn
```

Con eso quedan funcionando todos los botones de contacto del sitio.

---

## Publicación en GitHub Pages

1. Sube **todo el contenido de este ZIP** a la raíz del repositorio `Guate_Tech_Leaders_ES`.
   En la raíz deben quedar los siete `.html`, la carpeta `assets` y `.nojekyll`.
2. Settings → Pages → Build and deployment → **Deploy from a branch**.
3. Rama **main**, carpeta **/ (root)**. Save.
4. En dos minutos estará en `https://madeprat.github.io/Guate_Tech_Leaders_ES/`.

Si más adelante usas dominio propio, hay que cambiar esa URL en la constante `SITIO` de `assets/site.js` y en las etiquetas `og:url` y `canonical` de cada página (o regenerarlas cambiando `BASE` en `construir.py`).

---

## Estructura

| Archivo | Para quién |
|---|---|
| `index.html` | Portada institucional. Incluye la carta de la impulsora. |
| `la-iniciativa.html` | Principios, ámbito, estado de la iniciativa y quién la impulsa. |
| `posicion.html` | Documento de posición sobre el vacío en el mapa. Cita el estudio de 2026. Es la pieza para lectores académicos e institucionales. |
| `la-mesa.html` | Formato de la primera mesa y los cinco temas de trabajo. |
| `instituciones.html` | Embajada, universidades, centros educativos y empresas. |
| `participar.html` | Contacto, formulario y proponer a otra persona. |
| `legal.html` | Aviso legal y privacidad. |

`construir.py` (fuera del ZIP) genera las seis páginas desde una plantilla común, para que la cabecera, el pie y la ficha institucional no se desincronicen nunca.

---

## Qué revisar antes de publicar

- **El cargo de Madelaine.** Aparece en la ficha de la iniciativa (todas las páginas), en `la-iniciativa.html` y en `instituciones.html`. Debe coincidir exactamente con el perfil de LinkedIn.
- **Ciudad y fecha de la primera mesa.** Ahora dice «Madrid, primer trimestre de 2026». Está en la ficha institucional y en `index.html`, `la-mesa.html` e `instituciones.html`.
- **Los cinco temas de trabajo.** En `la-mesa.html`, sección `#temas`.

## Formularios

Por defecto abren el gestor de correo con todos los campos ya escritos. Funciona en cualquier sitio, pero se pierde a quien use webmail corporativo.

Cuando puedas, crea un formulario gratuito en [formspree.io](https://formspree.io) y pega su endpoint en la tercera línea de `assets/site.js`. A partir de ahí los envíos llegan al correo sin que el visitante haga nada más.

## Identidad

- **Marca:** una mesa redonda de doce puestos. `assets/img/mark.svg`, y en línea dentro de cada página para que herede el color.
- **Color:** jade `#2c5d57`, tinta `#1b2a2e`, azul claro `#bfd4dd`, papel `#fbfaf7`.
- **Tipografías:** Newsreader (titulares y voz) y Libre Franklin (texto y estructura), autoalojadas en `assets/fonts` con subconjunto latino, 160 KB en total. Ninguna llamada a Google Fonts.
- **Documento de posición:** `posicion.html` cita el estudio de Bonilla et al. (2026), doi 10.3389/frma.2026.1860284, en acceso abierto. Se cita como fuente, nunca como respaldo.
- **Tarjeta social:** `assets/img/og.jpg`, 1200×630, declarada en las seis páginas. Si la cambias, refresca la caché con el [Post Inspector de LinkedIn](https://www.linkedin.com/post-inspector/).

## Técnico

- Sin cookies, sin analítica, sin scripts de terceros.
- Open Graph, título, descripción, imagen y URL canónica en todas las páginas.
- Navegación por teclado con foco visible, salto al contenido y `prefers-reduced-motion` respetado.

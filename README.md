# Guatemala Tech Leaders España

Web de la iniciativa, publicada con GitHub Pages en https://502tech34.prat-cas.com/

Sitio estático: HTML, CSS y JavaScript sin dependencias, sin cookies y sin analítica. Se edita directamente en los archivos `.html`.

## Configuración

Las primeras líneas de `assets/site.js` contienen el correo de contacto, el LinkedIn y el endpoint opcional de [Formspree](https://formspree.io) para los formularios. Si el endpoint está vacío, los formularios abren el gestor de correo de quien los envía con los datos ya escritos.

## Estructura

- `*.html`: páginas del sitio. `participar.html`, `prerreserva.html` y `la-mesa.html` solo redirigen a las páginas actuales.
- `assets/cal/`: archivos de calendario (.ics) de cada encuentro. Las fechas también están en `index.html`, `apuntate.html` y `assets/eventos.js`.
- `assets/`: estilos, script, tipografía e imágenes.
- `CNAME`: dominio propio.

/* ============================================================
   ⬇⬇⬇  LO ÚNICO QUE TIENES QUE EDITAR ESTÁ AQUÍ DEBAJO  ⬇⬇⬇
   ============================================================ */

const CONFIG = {
  // 1. Tu correo de contacto para la iniciativa.
  email: "hola@ejemplo.com",

  // 2. La URL completa de tu perfil de LinkedIn.
  linkedin: "https://www.linkedin.com/in/TU-PERFIL",

  // 3. (Opcional) Si creas un formulario en https://formspree.io,
  //    pega aquí su endpoint y los formularios enviarán sin abrir el correo.
  //    Si lo dejas vacío, el formulario abrirá el gestor de correo con todo relleno.
  formspree: ""
};

/* ============================================================
   ⬆⬆⬆  A PARTIR DE AQUÍ NO HACE FALTA TOCAR NADA  ⬆⬆⬆
   ============================================================ */

const SITIO = "https://madeprat.github.io/Guate_Tech_Leaders_ES/";

/* --- Contacto: rellena todos los enlaces marcados --- */
document.querySelectorAll('[data-mail]').forEach(el => {
  const asunto = el.dataset.mail || "Sobre la primera mesa";
  el.href = `mailto:${CONFIG.email}?subject=${encodeURIComponent(asunto)}`;
});
document.querySelectorAll('[data-linkedin]').forEach(el => { el.href = CONFIG.linkedin; });
document.querySelectorAll('[data-mail-texto]').forEach(el => { el.textContent = CONFIG.email; });

/* --- Menú en pantallas pequeñas --- */
const hamb = document.querySelector('.hamb');
const menu = document.querySelector('.cab nav');
if (hamb && menu) {
  hamb.addEventListener('click', () => {
    const abierto = menu.classList.toggle('abierta');
    hamb.setAttribute('aria-expanded', abierto ? 'true' : 'false');
  });
}

/* --- Compartir --- */
const TEXTO_COMPARTIR =
  "Madelaine Castro está reuniendo una primera mesa de profesionales de origen guatemalteco que dirigen, fundan, investigan o invierten en tecnología en España. He pensado que te interesaría.";

function avisar(msg) {
  document.querySelectorAll('.aviso').forEach(el => {
    el.textContent = msg;
    clearTimeout(el._t);
    el._t = setTimeout(() => { el.textContent = ''; }, 4000);
  });
}

async function copiar() {
  const txt = `${TEXTO_COMPARTIR}\n${SITIO}`;
  try {
    await navigator.clipboard.writeText(txt);
    avisar('Texto y enlace copiados. Ya puedes pegarlos donde quieras.');
  } catch (e) {
    window.prompt('Copia este texto:', txt);
  }
}

document.querySelectorAll('[data-compartir]').forEach(btn => {
  btn.addEventListener('click', async () => {
    const tipo = btn.dataset.compartir;
    if (tipo === 'nativo') {
      if (navigator.share) {
        try {
          await navigator.share({ title: 'Liderazgo tecnológico guatemalteco en España', text: TEXTO_COMPARTIR, url: SITIO });
          return;
        } catch (e) { if (e && e.name === 'AbortError') return; }
      }
      return copiar();
    }
    if (tipo === 'copiar') return copiar();
    if (tipo === 'whatsapp') {
      window.open('https://wa.me/?text=' + encodeURIComponent(TEXTO_COMPARTIR + ' ' + SITIO), '_blank', 'noopener');
    }
    if (tipo === 'linkedin') {
      window.open('https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(SITIO), '_blank', 'noopener');
    }
  });
});

/* --- Formularios --- */
const ETIQUETAS = {
  nombre: 'Nombre', cargo: 'Cargo o función', organizacion: 'Empresa o institución',
  ciudad: 'Ciudad', area: 'Área tecnológica', perfil: 'LinkedIn o web',
  entidad: 'Entidad', persona: 'Persona de contacto', mensaje: 'Mensaje'
};

document.querySelectorAll('form[data-tipo]').forEach(form => {
  form.addEventListener('submit', async e => {
    e.preventDefault();
    const datos = Object.fromEntries(new FormData(form).entries());
    delete datos.consent;
    const asunto = form.dataset.asunto || 'Contacto';

    if (CONFIG.formspree) {
      const btn = form.querySelector('button[type=submit]');
      const original = btn.textContent;
      btn.textContent = 'Enviando…';
      btn.disabled = true;
      try {
        const r = await fetch(CONFIG.formspree, {
          method: 'POST',
          headers: { 'Accept': 'application/json' },
          body: new FormData(form)
        });
        if (!r.ok) throw new Error('fallo');
        form.innerHTML = '<p class="voz" style="max-width:34ch">Recibido. Te escribo en los próximos días.</p>';
        return;
      } catch (err) {
        btn.textContent = original;
        btn.disabled = false;
        avisar('El envío no ha funcionado. Escríbeme directamente a ' + CONFIG.email + '.');
        return;
      }
    }

    const cuerpo = Object.entries(datos)
      .map(([k, v]) => `${ETIQUETAS[k] || k}: ${v}`)
      .join('\n');
    window.location.href = `mailto:${CONFIG.email}?subject=${encodeURIComponent(asunto)}&body=${encodeURIComponent(cuerpo)}`;
    avisar('Se abrirá tu gestor de correo con el mensaje preparado. Si no se abre, escríbeme a ' + CONFIG.email + '.');
  });
});

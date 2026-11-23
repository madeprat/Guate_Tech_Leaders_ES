/* ============================================================
   CONFIGURACIÓN — lo único que puede hacer falta tocar
   ============================================================ */
const CONFIG = {
  email: "madelainedepratdesaba@gmail.com",
  linkedin: "https://www.linkedin.com/in/madelaine-r-c-55906387/",
  // Endpoint de https://formspree.io (p. ej. "https://formspree.io/f/abcdwxyz").
  // Vacío: los formularios abren el gestor de correo con los datos ya escritos.
  formspree: ""
};
const SITIO = "https://502tech34.prat-cas.com/";
/* ============================================================ */

/* --- Contacto --- */
document.querySelectorAll('[data-mail]').forEach(el => {
  const asunto = el.dataset.mail || "Guatemala Tech Leaders España";
  el.href = `mailto:${CONFIG.email}?subject=${encodeURIComponent(asunto)}`;
});
document.querySelectorAll('[data-linkedin]').forEach(el => { el.href = CONFIG.linkedin; });
document.querySelectorAll('[data-mail-texto]').forEach(el => { el.textContent = CONFIG.email; });

/* --- Menú móvil --- */
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
  "Talento TI made in Guatemala en España. Encuentros abiertos en 2027 (18 de marzo, 17 de junio y 16 de diciembre), en Madrid y online. Me he acordado de ti:";

function avisar(msg, ambito) {
  (ambito ? ambito.querySelectorAll('.aviso') : document.querySelectorAll('.aviso')).forEach(el => {
    el.textContent = msg;
    clearTimeout(el._t);
    el._t = setTimeout(() => { el.textContent = ''; }, 6000);
  });
}

async function copiar(btn) {
  const txt = `${TEXTO_COMPARTIR}\n${SITIO}`;
  const ambito = btn ? btn.closest('section') : null;
  try {
    await navigator.clipboard.writeText(txt);
    avisar('Texto y enlace copiados.', ambito);
  } catch (e) {
    window.prompt('Copia este texto:', txt);
  }
}

document.querySelectorAll('[data-compartir]').forEach(btn => {
  btn.addEventListener('click', async () => {
    const tipo = btn.dataset.compartir;
    if (tipo === 'copiar') return copiar(btn);
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
  nombre: 'Nombre y apellidos', email: 'Correo electrónico', telefono: 'Teléfono',
  cargo: 'Cargo o función', organizacion: 'Empresa o institución', ciudad: 'Ciudad',
  area: 'Área tecnológica', perfil: 'LinkedIn o web', modalidad: 'Modalidad preferida',
  origen: 'Origen guatemalteco', aporte: 'Qué le gustaría aportar o llevarse',
  conocido: 'Cómo ha conocido la iniciativa', referencia: 'Referencia', encuentros: 'Encuentros',
  persona: 'Persona propuesta', proponente: 'Propuesta por', motivo: 'Motivo', mensaje: 'Mensaje'
};

function referencia() {
  const abc = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let r = '';
  const v = new Uint32Array(4);
  (window.crypto || window.msCrypto).getRandomValues(v);
  v.forEach(n => { r += abc[n % abc.length]; });
  return 'GTL-27-' + r;
}

function escapar(t) {
  return String(t).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function confirmar(form, datos, porCorreo) {
  const tipo = form.dataset.tipo;
  const caja = form.closest('.form-caja') || form;
  let html;
  if (tipo === 'inscripcion') {
    const nombre = (datos.nombre || '').split(' ')[0];
    const evs = [...form.querySelectorAll('input[name=encuentros]:checked')].map(i => i.dataset.ev);
    const cal = (typeof EVENTOS !== 'undefined') ? evs.map(id => EVENTOS[id]).filter(Boolean).map(ev =>
      `<a class="btn btn-s" href="${ev.g}" target="_blank" rel="noopener">${ev.t} · Google</a><a class="btn btn-s" href="${ev.i}" download>${ev.t} · Outlook/Apple</a>`).join('') : '';
    html = `<div class="recibido" role="status" tabindex="-1">
      <p class="antetitulo">${porCorreo ? 'Casi listo' : 'Estás dentro'}</p>
      <h3>${nombre ? '¡Gracias, ' + escapar(nombre) + '!' : '¡Gracias!'}</h3>
      <p>${porCorreo
        ? 'Se ha abierto tu correo con la inscripción escrita: envíalo para completarla. Si no se ha abierto, escribe a <a href="mailto:' + CONFIG.email + '">' + CONFIG.email + '</a>.'
        : 'Te enviaremos la sede o el enlace antes de cada encuentro.'}</p>
      ${cal ? '<p style="margin:18px 0 0;font-weight:650;color:var(--tinta)">Guárdalo en tu calendario</p><div class="cal-links">' + cal + '</div>' : ''}
      <p style="margin:0;font-size:14px;color:var(--suave)">Tu código: <b>${escapar(datos.referencia)}</b></p>
    </div>`;
  } else if (tipo === 'prerreserva') {
    const nombre = (datos.nombre || '').split(' ')[0];
    html = `<div class="recibido" role="status" tabindex="-1">
      <p class="antetitulo">${porCorreo ? 'Prerreserva preparada' : 'Prerreserva recibida'}</p>
      <h3>${nombre ? 'Gracias, ' + escapar(nombre) + '.' : 'Gracias.'}</h3>
      <p>Tu referencia</p>
      <span class="ref">${escapar(datos.referencia)}</span>
      <p>${porCorreo
        ? 'Se ha abierto tu gestor de correo con la prerreserva escrita. Envía ese mensaje para completarla. Si no se ha abierto, escribe a <a href="mailto:' + CONFIG.email + '">' + CONFIG.email + '</a> indicando tu referencia.'
        : 'Te escribiré personalmente en los próximos días para confirmar tu plaza y la modalidad. La fecha exacta la conocerás antes de que se publique.'}</p>
      <p style="margin:0;font-size:14.5px;color:var(--suave)">Guarda la referencia: la usaremos en todas las comunicaciones de la primera mesa.</p>
    </div>`;
  } else {
    html = `<div class="recibido" role="status" tabindex="-1">
      <h3>${porCorreo ? 'Mensaje preparado' : 'Recibido. Gracias.'}</h3>
      <p style="margin:0">${porCorreo
        ? 'Se ha abierto tu gestor de correo con el mensaje escrito. Envíalo para completarlo. Si no se ha abierto, escribe a <a href="mailto:' + CONFIG.email + '">' + CONFIG.email + '</a>.'
        : 'Lo leo personalmente y te respondo en los próximos días.'}</p>
    </div>`;
  }
  caja.innerHTML = html;
  const r = caja.querySelector('.recibido');
  if (r) r.focus();
}

document.querySelectorAll('form[data-tipo]').forEach(form => {
  form.addEventListener('submit', async e => {
    e.preventDefault();
    if (form.dataset.tipo === 'prerreserva' || form.dataset.tipo === 'inscripcion') {
      const marcados = form.querySelectorAll('input[name=encuentros]');
      if (marcados.length && !form.querySelector('input[name=encuentros]:checked')) {
        avisar('Elige al menos un encuentro.', form.parentElement);
        marcados[0].focus();
        return;
      }
      let campo = form.querySelector('input[name=referencia]');
      if (!campo) {
        campo = document.createElement('input');
        campo.type = 'hidden'; campo.name = 'referencia';
        form.appendChild(campo);
      }
      if (!campo.value) campo.value = referencia();
    }
    const fd = new FormData(form);
    const datos = Object.fromEntries(fd.entries());
    if (fd.getAll('encuentros').length) datos.encuentros = fd.getAll('encuentros').join(', ');
    delete datos.consent;
    const asunto = (form.dataset.asunto || 'Contacto') + (datos.referencia ? ' · ' + datos.referencia : '');

    if (CONFIG.formspree) {
      const btn = form.querySelector('button[type=submit]');
      const original = btn.textContent;
      btn.textContent = 'Enviando…';
      btn.disabled = true;
      fd.append('_subject', asunto);
      try {
        const r = await fetch(CONFIG.formspree, { method: 'POST', headers: { 'Accept': 'application/json' }, body: fd });
        if (!r.ok) throw new Error('fallo');
        confirmar(form, datos, false);
        return;
      } catch (err) {
        btn.textContent = original;
        btn.disabled = false;
        avisar('No se ha podido enviar. Escribe directamente a ' + CONFIG.email + '.', form.parentElement);
        return;
      }
    }

    const cuerpo = Object.entries(datos)
      .filter(([, v]) => String(v).trim() !== '')
      .map(([k, v]) => `${ETIQUETAS[k] || k}: ${v}`)
      .join('\n');
    window.location.href = `mailto:${CONFIG.email}?subject=${encodeURIComponent(asunto)}&body=${encodeURIComponent(cuerpo)}`;
    confirmar(form, datos, true);
  });
});

/* --- Preseleccionar encuentro desde ?e= --- */
const pe = new URLSearchParams(location.search).get('e');
if (pe) document.querySelectorAll(`input[name=encuentros][data-ev="${CSS.escape(pe)}"]`).forEach(i => { i.checked = true; });

/* --- Menú de calendario: cerrar al pulsar fuera --- */
document.addEventListener('click', e => {
  document.querySelectorAll('details.cal[open]').forEach(d => { if (!d.contains(e.target)) d.removeAttribute('open'); });
});

/* --- Aparición suave al hacer scroll --- */
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(es => es.forEach(en => {
    if (en.isIntersecting) { en.target.classList.add('visto'); io.unobserve(en.target); }
  }), { threshold: .12 });
  document.querySelectorAll('.aparece').forEach(el => io.observe(el));
} else {
  document.querySelectorAll('.aparece').forEach(el => el.classList.add('visto'));
}

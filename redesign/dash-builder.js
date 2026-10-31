// Dash Builder: pick a car and see every gauge system that fits it, in real photos of each
// lighting theme. Fitment comes from garage.js; products, prices and photos from
// dash-builder-data.json (written by tools/build_pages.py from the product pages).
(() => {
  const root = document.getElementById('main');
  const G = window.DDGarage;
  if (!root || !G) return;
  const $ = (k) => root.querySelector(`[data-db="${k}"]`);
  const ORDER = ['R', 'H', 'V', 'G', 'D'];
  const money = (n) => n.toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: n % 1 ? 2 : 0 });
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  // Analytics is wired up later. Calls mark the moments worth measuring.
  const track = (eventName, data) => {};

  const carSel = $('car');
  const yearSel = $('years');
  const view = $('view');
  const stage = $('stage');
  const THREE_BASE = new URL(`${document.currentScript.dataset.three}/`, document.baseURI).href;
  let data = null;
  const state = { pid: '', ri: -1, s: '', theme: '', console: false, version: 0 };

  // ---- Picker ----
  carSel.insertAdjacentHTML('beforeend', G.PLATFORMS.map((p) => `<option value="${p.id}">${esc(p.label)}</option>`).join(''));
  const platform = () => G.PLATFORMS.find((p) => p.id === state.pid);
  const range = () => (platform() && state.ri >= 0 ? platform().r[state.ri] : null);
  const fillYears = () => {
    const p = platform();
    yearSel.innerHTML = '<option value="">Choose years</option>' + (p ? p.r.map((r, i) => `<option value="${i}">${r[0]}</option>`).join('') : '');
    yearSel.disabled = !p;
    yearSel.value = state.ri >= 0 ? String(state.ri) : '';
  };

  // Pre-fill: URL first, then the saved garage car, then nothing.
  const params = new URLSearchParams(location.search);
  const fromUrl = G.PLATFORMS.find((p) => p.id === params.get('car'));
  if (fromUrl) {
    state.pid = fromUrl.id;
    state.ri = fromUrl.r.findIndex((r) => r[0] === params.get('years'));
    const code = ORDER.find((k) => G.SERIES[k].name === (params.get('system') || '').toUpperCase());
    if (code) state.s = code;
    state.theme = params.get('theme') || '';
    state.console = params.get('console') === '1';
  } else {
    const saved = G.get();
    if (saved) { state.pid = saved.pid; state.ri = saved.ri; }
  }
  carSel.value = state.pid;
  fillYears();

  // ---- Products that fit ----
  const productsFor = (code) => {
    const p = platform();
    const years = G.yearsOf(range()[0]);
    const line = data.products.filter((x) => x.s === G.SERIES[code].name && x.c.includes(p.cat));
    const dated = line.filter((x) => x.y.some((y) => years.includes(y)));
    return dated.length ? dated : line.filter((x) => !x.y.length);
  };
  // Series that fit this car (garage.js) and have a product page to send the visitor to.
  const systems = () => {
    const codes = range()[1];
    return ORDER.filter((k) => codes.includes(k))
      .map((k) => ({ code: k, all: productsFor(k) }))
      .filter((x) => x.all.length)
      .map((x) => {
        const consoleOnes = x.all.filter((p) => p.x);
        const plain = x.all.filter((p) => !p.x);
        return { ...x, consoleOnes, plain };
      });
  };
  const choices = (sys) => (state.console ? sys.consoleOnes : (sys.plain.length ? sys.plain : sys.all));
  const pickTheme = (prod) => {
    if (!prod.th.length) return null;
    return prod.th.find((t) => t[0].toLowerCase() === state.theme.toLowerCase()) || prod.th[0];
  };

  // ---- URL ----
  const syncUrl = (prod, theme) => {
    const url = new URL(location.href);
    url.search = '';
    if (state.pid) url.searchParams.set('car', state.pid);
    if (range()) url.searchParams.set('years', range()[0]);
    if (prod) url.searchParams.set('system', G.SERIES[state.s].name);
    if (theme) url.searchParams.set('theme', theme[0]);
    if (state.console) url.searchParams.set('console', '1');
    history.replaceState(null, '', url);
  };

  const preloaded = new Set();
  const preload = (prod) => {
    prod.th.forEach(([, src]) => {
      if (preloaded.has(src)) return;
      preloaded.add(src);
      new Image().src = src;
    });
  };

  // ---- Dash view ----
  function render() {
    // Lay out for the car right away (no shift when the data arrives), fill in once it has.
    const has = Boolean(range());
    $('empty').hidden = has;
    view.hidden = !has;
    view.classList.toggle('is-loading', has && !data);
    if (!has) syncUrl(null, null);
    if (!has || !data) { updateStage(); return; }

    const p = platform();
    const carName = `${range()[0]} ${p.label}`;
    const anyConsole = systems().some((x) => x.consoleOnes.length);
    if (!anyConsole) state.console = false;
    let list = systems();
    if (state.console) list = list.filter((x) => x.consoleOnes.length);
    const cur = list.find((x) => x.code === state.s) || list[0];
    if (!cur) return;
    if (cur.code !== state.s) { state.s = cur.code; state.version = 0; }

    const opts = choices(cur);
    if (!opts[state.version]) state.version = 0;
    const prod = opts[state.version];
    const theme = pickTheme(prod);

    const n = list.length;
    $('count').textContent = `${n} ${n === 1 ? 'system fits' : 'systems fit'} your ${carName}${state.console ? ' with console gauges' : ''}`;
    $('systems').innerHTML = list.map((x) => {
      const s = G.SERIES[x.code];
      const low = Math.min(...choices(x).map((q) => q.p));
      return `<button type="button" class="db-sys" data-code="${x.code}" aria-pressed="${x === cur}"><strong>${s.name}</strong><span>${s.tag}</span><span class="db-sys-price">From ${money(low)}</span></button>`;
    }).join('');

    $('console-wrap').hidden = !anyConsole;
    $('console').checked = state.console;
    $('version-wrap').hidden = opts.length < 2;
    $('version').innerHTML = opts.map((q, i) => `<option value="${i}">${esc(q.t)}</option>`).join('');
    $('version').value = String(state.version);

    $('name').textContent = prod.t;
    $('sku').textContent = prod.k;
    $('price').textContent = money(prod.p);
    $('themes').innerHTML = prod.th.map(([name, src]) =>
      `<button type="button" class="db-theme" data-theme="${esc(name)}" aria-pressed="${theme && name === theme[0]}"><img src="${src}" alt="" width="72" height="40" loading="lazy" decoding="async"><span>${esc(name)}</span></button>`).join('');
    $('themes').hidden = !theme;
    $('no-themes').hidden = Boolean(theme);

    const photo = $('photo');
    const src = theme ? theme[1] : prod.img;
    if (photo.getAttribute('src') !== src) { photo.src = src; $('fade-img').src = src; }
    photo.alt = theme ? `${prod.t}, lit up in the ${theme[0]} theme` : prod.t;
    $('photo-cap').textContent = `Real photo of the ${prod.k}${theme ? ` in the ${theme[0]} theme` : ''}.`;
    const dashKey = `${p.id}-${range()[0]}`;
    const bg = $('bg');
    bg.hidden = !data.dash.includes(dashKey);
    if (!bg.hidden) bg.src = `img/dash/${dashKey}.webp`;
    $('frame').classList.toggle('has-bg', !bg.hidden);

    const see = $('see');
    see.href = prod.u + (theme ? `?theme=${encodeURIComponent(theme[0])}` : '');
    preload(prod);
    syncUrl(prod, theme);
    updateStage();
  }

  // ---- 3D pilot stage (1969 Camaro only) ----
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
  let webgl = null;
  const hasWebGL = () => {
    if (webgl === null) {
      try {
        const c = document.createElement('canvas');
        webgl = Boolean(c.getContext('webgl2') || c.getContext('webgl'));
      } catch { webgl = false; }
    }
    return webgl;
  };
  let loading = null;
  let scene = null;
  let failed = false;
  let reached = false;
  let caption = '';
  const isPilot = () => state.pid === 'camaro' && range() && range()[0] === '1969';

  const reach = () => {
    view.inert = false;
    if (reached) return;
    reached = true;
    track('reached_dash', { car: state.pid, years: range()[0], view: stage.hidden ? 'photo' : '3d' });
  };

  const onScroll = () => {
    if (stage.hidden) return;
    const total = stage.offsetHeight - window.innerHeight;
    const p = total > 0 ? Math.min(1, Math.max(0, -stage.getBoundingClientRect().top / total)) : 1;
    if (scene) scene.setProgress(p);
    const theme = $('themes').querySelector('[aria-pressed="true"]');
    const text = p < 0.42 ? 'Your 1969 Camaro. Scroll to walk around.'
      : p < 0.46 ? 'Around back.'
        : p < 0.82 ? 'Now climb in through the back glass.'
          : `Your dash${state.s ? `, with ${G.SERIES[state.s].name}` : ''}${theme ? ` in ${theme.dataset.theme}` : ''}.`;
    if (text !== caption) { caption = text; $('caption').textContent = text; }
    const step = p < 0.46 ? 0 : p < 0.82 ? 1 : 2;
    $('rail').querySelectorAll('li').forEach((li, i) => (i === step ? li.setAttribute('aria-current', 'step') : li.removeAttribute('aria-current')));
    $('fade').style.opacity = String(Math.min(1, Math.max(0, (p - 0.82) / 0.1)));
    if (p >= 0.82) reach();
  };

  // 3D only for the pilot car, with WebGL and motion allowed. Everyone else gets the dash view at once.
  // The 3D code loads on the visitor's first scroll, tap or key press, so the picker and photos
  // paint first and phones don't parse three.js for a visit that never scrolls.
  let wanted = false;
  const load3d = () => {
    if (loading || !wanted || !data || stage.hidden) return;
    loading = import('./dash-builder-3d.js')
      .then((m) => m.mount({ canvas: $('canvas'), stage, base: THREE_BASE, model: data.models.includes('camaro-69') ? 'models/camaro-69.glb' : null }))
      .then((api) => { scene = api; onScroll(); })
      .catch(() => { failed = true; updateStage(); });
  };
  const intent = () => {
    wanted = true;
    load3d();
    ['scroll', 'pointerdown', 'keydown'].forEach((t) => window.removeEventListener(t, intent));
  };
  ['scroll', 'pointerdown', 'keydown'].forEach((t) => window.addEventListener(t, intent, { passive: true }));

  function updateStage() {
    const has = Boolean(range());
    const on = has && isPilot() && !failed && !reduceMotion.matches && hasWebGL();
    stage.hidden = !on;
    $('note').hidden = !has || on;
    if (!on) { view.inert = false; return; }
    if (!reached) view.inert = true;
    load3d();
    onScroll();
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  reduceMotion.addEventListener('change', updateStage);

  // Keep keyboard focus on the button that was pressed after a re-render.
  const refocus = (group, attr, value) => {
    const again = $(group).querySelector(`[${attr}="${CSS.escape(value)}"]`);
    if (again) again.focus();
  };

  // ---- Events ----
  const carChanged = () => {
    if (range()) {
      G.set({ pid: state.pid, ri: state.ri });
      track('car_selected', { car: state.pid, years: range()[0] });
    }
    render();
  };
  carSel.addEventListener('change', () => {
    state.pid = carSel.value;
    state.ri = -1;
    fillYears();
    carChanged();
  });
  yearSel.addEventListener('change', () => {
    state.ri = yearSel.value === '' ? -1 : Number(yearSel.value);
    carChanged();
  });
  $('systems').addEventListener('click', (e) => {
    const btn = e.target.closest('.db-sys');
    if (!btn) return;
    state.s = btn.dataset.code;
    state.version = 0;
    render();
    track('system_selected', { system: G.SERIES[state.s].name });
    refocus('systems', 'data-code', state.s);
  });
  $('themes').addEventListener('click', (e) => {
    const btn = e.target.closest('.db-theme');
    if (!btn) return;
    state.theme = btn.dataset.theme;
    render();
    track('theme_selected', { theme: state.theme });
    refocus('themes', 'data-theme', state.theme);
  });
  $('console').addEventListener('change', () => { state.console = $('console').checked; state.version = 0; render(); });
  $('version').addEventListener('change', () => { state.version = Number($('version').value); render(); });
  $('skip').addEventListener('click', () => {
    reach();
    view.scrollIntoView({ behavior: 'instant', block: 'start' });
    $('count').focus({ preventScroll: true });
  });
  $('see').addEventListener('click', () => track('click_see_system', { sku: $('sku').textContent }));

  track('builder_open', { car: state.pid, years: range() ? range()[0] : '' });
  render();
  fetch('dash-builder-data.json')
    .then((r) => r.json())
    .then((d) => {
      data = d;
      if (range()) track('car_selected', { car: state.pid, years: range()[0] });
      render();
    });
})();

// Dash Finder: pick a car, its years and a look; preview the gauge with the key on.
// Fitment data comes from the Dash Finder design (verify against the catalog before launch).
(() => {
  const root = document.getElementById('finder');
  if (!root) return;

  // Each range: [years, series codes that fit]. cat = store category id.
  const PLATFORMS = [
    { id: 'camaro', label: 'Camaro', cat: 422, r: [['1967-68', 'GRHVD'], ['1969', 'GRHVD'], ['1970-81', 'RHVD'], ['1982-89', 'RVD'], ['1990-92', 'RV'], ['1997-02', 'R']] },
    { id: 'chevelle', label: 'Chevelle / El Camino', cat: 424, r: [['1964-65', 'RHVD'], ['1966-67', 'GRHVD'], ['1968', 'RHVD'], ['1969', 'RHVD'], ['1970-72', 'RHVD'], ['1973-77', 'V'], ['1978-88', 'RHVD']] },
    { id: 'nova', label: 'Nova', cat: 426, r: [['1963-65', 'RHVD'], ['1966-67', 'RHVD']] },
    { id: 'corvette', label: 'Corvette', cat: 427, r: [['1953-57', 'RH'], ['1958-62', 'RHVD'], ['1963-67', 'RHVD'], ['1968-77', 'RHVD'], ['1978-82', 'RHVD'], ['1984-89', 'D']] },
    { id: 'gmtruck', label: 'Chevy / GMC truck', cat: 421, r: [['1940-46', 'VD'], ['1947-53', 'GRHVD'], ['1954', 'RHVD'], ['1955-59', 'GRHVD'], ['1960-63', 'GRHVD'], ['1964-66', 'GRHVD'], ['1967-72', 'GRHVD']] },
    { id: 'squarebody', label: 'Square body truck', cat: 784, r: [['1973-87', 'GRHVD'], ['1988-94', 'RHVD'], ['1995-98', 'RHV']] },
    { id: 'mustang', label: 'Mustang / Falcon', cat: 434, r: [['1960-63', 'V'], ['1964-65', 'RHV'], ['1965-66', 'RHVD'], ['1967-68', 'RHVD'], ['1969-70', 'RHVD'], ['1971-73', 'VD'], ['1979-86', 'RV'], ['1987-93', 'RHV'], ['1994-04', 'RV']] },
    { id: 'fordtruck', label: 'Ford truck / Bronco', cat: 830, r: [['1967-72', 'RHVD'], ['1973-79', 'RD'], ['1980-86', 'RV'], ['1987-91', 'RV'], ['1992-96', 'R'], ['1997-04', 'R']] }
  ];
  const SERIES = {
    G: { name: 'GRFX', tag: 'Full screen', body: 'One color screen fills the whole cluster. Pick it if you want the dash to look as new as the drivetrain.' },
    R: { name: 'RTX', tag: 'Factory look', body: 'Looks like the original cluster until you turn the key. Behind the stock style you get a color message center, lighting you can change and setup from your phone.' },
    H: { name: 'HDX', tag: 'Custom modern', body: 'Custom faces, sweeping needles and full color message centers. Change the lighting and settings from your phone.' },
    V: { name: 'VHX', tag: 'Classic analog', body: 'Real needles with a simple digital readout in the center. A clean upgrade that costs less than RTX or HDX.' },
    D: { name: 'VFD3', tag: 'All digital', body: 'Bright digital numbers and no needles. The look Dakota Digital started with.' }
  };
  // Redesigned product pages, keyed by platform|years|series. Everything else goes to the category page.
  const PRODUCT_PAGES = { 'camaro|1969|R': 'camaro-1969-rtx.html' };
  const ORDER = ['R', 'H', 'V', 'G', 'D'];
  const LIGHTS = [['Ice blue', '#3A9BFF'], ['Red', '#FF4B3E'], ['Amber', '#FFB020'], ['White', '#F2F2EE'], ['Green', '#3DDC84']];

  const state = { pid: 'camaro', ri: 0, s: 'R', light: '#3A9BFF', speed: 65 };

  const $ = (sel) => root.querySelector(sel);
  const list = (name) => $(`[data-list="${name}"]`);
  const out = (name) => $(`[data-out="${name}"]`);
  const speedInput = document.getElementById('spd');

  const platform = () => PLATFORMS.find((p) => p.id === state.pid) || PLATFORMS[0];
  const codes = () => platform().r[state.ri][1];
  const firstFit = (c) => ORDER.find((k) => c.includes(k));
  const keepSeries = (c) => { if (!c.includes(state.s)) state.s = firstFit(c); };

  // ---- Gauge drawing ----
  const CX = 160, CY = 160;
  const rad = (v) => (150 + (v / 120) * 240) * Math.PI / 180;
  const needleDeg = (v) => (150 + (v / 120) * 240).toFixed(1);
  const arcVal = (v) => ((v / 120) * 460.8).toFixed(1);
  const TICKS = (() => {
    let d = '';
    for (let v = 0; v <= 120; v += 5) {
      const a = rad(v), r1 = v % 20 === 0 ? 108 : 118, r2 = 130;
      d += `M${(CX + Math.cos(a) * r1).toFixed(1)} ${(CY + Math.sin(a) * r1).toFixed(1)}L${(CX + Math.cos(a) * r2).toFixed(1)} ${(CY + Math.sin(a) * r2).toFixed(1)}`;
    }
    return d;
  })();
  const NUMS = [0, 20, 40, 60, 80, 100, 120].map((v) =>
    `<text x="${(CX + Math.cos(rad(v)) * 86).toFixed(1)}" y="${(CY + Math.sin(rad(v)) * 86).toFixed(1)}" class="g-num">${v}</text>`).join('');

  function gaugeSvg() {
    const s = state.s, L = state.light, v = state.speed;
    const label = `${SERIES[s].name} speedometer preview showing ${v} miles per hour`;
    if (s === 'G') {
      return `<svg viewBox="0 0 320 320" role="img" aria-label="${label}">
        <rect x="4" y="4" width="312" height="312" rx="20" fill="#05070A" stroke="#3A3E45" stroke-width="4"/>
        <circle cx="160" cy="160" r="110" fill="none" stroke="#1F2329" stroke-width="16" stroke-dasharray="460.8 691.2" transform="rotate(150 160 160)"/>
        <circle data-g="arc" cx="160" cy="160" r="110" fill="none" stroke="${L}" stroke-width="16" stroke-dasharray="${arcVal(v)} 691.2" transform="rotate(150 160 160)"/>
        <text data-g="speed" x="160" y="160" fill="#F2F2EE" class="g-big" font-size="88">${v}</text>
        <text x="160" y="214" fill="#9EA3AA" class="g-unit" font-size="20" letter-spacing="3">MPH</text>
      </svg>`;
    }
    if (s === 'D') {
      return `<svg viewBox="0 0 320 320" role="img" aria-label="${label}">
        <rect x="4" y="60" width="312" height="200" rx="10" fill="#C9CCD1"/>
        <rect x="16" y="72" width="288" height="176" rx="6" fill="#030505"/>
        <text data-g="speed" x="160" y="164" fill="#3DF5D1" class="g-big" font-weight="600" font-size="116">${v}</text>
        <text x="270" y="228" fill="#3DF5D1" class="g-unit" font-size="18" letter-spacing="2" text-anchor="end">MPH</text>
      </svg>`;
    }
    const g = {
      R: { ring: '#C9CCD1', face: '#14161A', ticks: '#F2F2EE', needle: L, screen: L, screenText: '#F2F2EE' },
      H: { ring: L, face: '#0B0C0E', ticks: L, needle: L, screen: L, screenText: '#F2F2EE' },
      V: { ring: '#3A3E45', face: '#0B0C0E', ticks: '#F2F2EE', needle: '#FF4B3E', screen: '#3A3E45', screenText: '#B9BCC2' }
    }[s];
    return `<svg viewBox="0 0 320 320" role="img" aria-label="${label}">
      <circle cx="160" cy="160" r="152" fill="${g.ring}"/>
      <circle cx="160" cy="160" r="143" fill="${g.face}"/>
      <path d="${TICKS}" stroke="${g.ticks}" stroke-width="3" stroke-linecap="round" fill="none"/>
      <g fill="#F2F2EE">${NUMS}</g>
      <rect x="112" y="204" width="96" height="44" rx="4" fill="#05070A" stroke="${g.screen}" stroke-width="2"/>
      <text data-g="speed" x="160" y="227" fill="${g.screenText}" class="g-unit" font-size="24">${v} MPH</text>
      <g data-g="needle" class="needle" style="transform: rotate(${needleDeg(v)}deg)">
        <path d="M148 156 L272 160 L148 164 Z" fill="${g.needle}"/>
      </g>
      <circle cx="160" cy="160" r="13" fill="#2A2D33" stroke="${g.ticks}" stroke-width="2"/>
    </svg>`;
  }

  // Speed changes only move the existing needle so the transition can animate.
  function updateSpeed() {
    const v = state.speed, gauge = out('gauge');
    const svg = gauge.querySelector('svg');
    const speed = gauge.querySelector('[data-g="speed"]');
    const needle = gauge.querySelector('[data-g="needle"]');
    const arc = gauge.querySelector('[data-g="arc"]');
    if (speed) speed.textContent = /[RHV]/.test(state.s) ? `${v} MPH` : v;
    if (needle) needle.style.transform = `rotate(${needleDeg(v)}deg)`;
    if (arc) arc.setAttribute('stroke-dasharray', `${arcVal(v)} 691.2`);
    svg.setAttribute('aria-label', `${SERIES[state.s].name} speedometer preview showing ${v} miles per hour`);
  }

  // ---- Chips ----
  function chips(el, items, cls) {
    el.innerHTML = items.map((it) =>
      `<button type="button" class="${cls}" data-key="${it.key}" aria-pressed="${it.on}"${it.aria ? ` aria-label="${it.aria}"` : ''}${it.style ? ` style="${it.style}"` : ''}>${it.html}</button>`).join('');
  }

  function render() {
    // Remember focus so keyboard users stay on the chip they pressed.
    const active = document.activeElement;
    const focusKey = root.contains(active) && active.dataset.key ? [active.closest('[data-list]').dataset.list, active.dataset.key] : null;

    const p = platform();
    const c = codes();
    const avail = ORDER.filter((k) => c.includes(k));
    const cur = SERIES[state.s];
    const years = p.r[state.ri][0];

    chips(list('car'), PLATFORMS.map((x) => ({ key: x.id, on: x.id === p.id, html: x.label })), 'chip');
    chips(list('years'), p.r.map((x, i) => ({ key: i, on: i === state.ri, html: x[0] })), 'chip chip-year');
    chips(list('looks'), avail.map((k) => ({ key: k, on: k === state.s, html: `<strong>${SERIES[k].name}</strong><span>${SERIES[k].tag}</span>` })), 'look');
    chips(list('lights'), LIGHTS.map(([name, hex]) => ({ key: hex, on: hex === state.light, aria: `${name} lighting`, html: '', style: `background:${hex}` })), 'swatch');

    out('fit').textContent = `(${avail.length === 1 ? '1 system' : avail.length + ' systems'} fit your ${years} ${p.label})`;
    out('title').textContent = `${years} ${p.label} · ${cur.name}`;
    out('gauge').innerHTML = gaugeSvg();
    out('lights').hidden = !/[RH]/.test(state.s);
    out('name').textContent = cur.name;
    out('tag').textContent = cur.tag;
    out('body').textContent = cur.body;
    const shop = out('shop');
    shop.textContent = `See ${cur.name} for your ${p.label}`;
    shop.href = PRODUCT_PAGES[`${p.id}|${years}|${state.s}`] ||
      `https://www.dakotadigital.com/index.cfm/page/ptype=results/category_id=${p.cat}/mode=cat/cat${p.cat}.htm`;
    speedInput.style.accentColor = state.light;

    if (focusKey) {
      const again = list(focusKey[0]).querySelector(`[data-key="${CSS.escape(focusKey[1])}"]`);
      if (again) again.focus();
    }
  }

  root.addEventListener('click', (e) => {
    const btn = e.target.closest('button[data-key]');
    if (!btn) return;
    const which = btn.closest('[data-list]').dataset.list;
    const key = btn.dataset.key;
    if (which === 'car') { state.pid = key; state.ri = 0; keepSeries(codes()); }
    if (which === 'years') { state.ri = Number(key); keepSeries(codes()); }
    if (which === 'looks') state.s = key;
    if (which === 'lights') state.light = key;
    render();
  });

  speedInput.addEventListener('input', () => { state.speed = Number(speedInput.value); updateSpeed(); });

  speedInput.value = state.speed;
  render();
})();

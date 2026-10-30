// Instant search: type-ahead results under the header search box, grouped by what
// people are looking for. Uses search-index.json (built by tools/build_pages.py) plus
// the Dash Finder's cars from garage.js. Enter with nothing picked searches the full catalog.
(() => {
  const form = document.querySelector('.header-row .search');
  if (!form) return;
  const input = form.querySelector('input[type="search"]');
  const MAX = { car: 3, product: 4, help: 3, build: 2 };
  const GROUPS = [['car', 'Gauges for your car'], ['product', 'Products and parts'], ['help', 'Help and pages'], ['build', 'Feature builds']];
  const KIND_GROUP = { Vehicle: 'product', Part: 'product', Motorcycle: 'product', Universal: 'product', Accessory: 'product', Help: 'help', Page: 'help', Build: 'build' };
  const SERIES_ORDER = 'RHVGD';

  // ---- Markup: combobox + popup listbox ----
  input.setAttribute('role', 'combobox');
  input.setAttribute('aria-autocomplete', 'list');
  input.setAttribute('aria-expanded', 'false');
  input.setAttribute('aria-controls', 'search-list');
  input.setAttribute('autocomplete', 'off');
  input.placeholder = 'Search car, part # or question';
  const pop = document.createElement('div');
  pop.className = 'search-pop';
  pop.hidden = true;
  pop.innerHTML = '<ul role="listbox" id="search-list" aria-label="Search suggestions"></ul>' +
    '<p class="search-keys" aria-hidden="true"><kbd>↑</kbd><kbd>↓</kbd> to move · <kbd>Enter</kbd> to open · <kbd>Esc</kbd> to close</p>';
  const list = pop.querySelector('ul');
  const status = document.createElement('p');
  status.className = 'sr-only';
  status.setAttribute('aria-live', 'polite');
  form.append(pop, status);

  // ---- Index ----
  let index = null;
  const norm = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const compact = (s) => s.toLowerCase().replace(/[^a-z0-9]/g, '');
  const prep = (e) => {
    const text = norm(`${e.t} ${e.s || ''} ${e.x || ''} ${(e.years || []).join(' ')}`);
    return { ...e, words: text.split(' '), titleWords: norm(`${e.t} ${(e.years || []).join(' ')}`).split(' '), flat: compact(`${e.t} ${e.s || ''}`) };
  };
  const yearsOf = (range) => {
    const [a, b] = range.split('-');
    const start = Number(a);
    const end = b ? Number(a.slice(0, 4 - b.length) + b) : start;
    const out = [];
    for (let y = start; y <= end && out.length < 40; y++) out.push(String(y), String(y).slice(2));
    return out;
  };
  const vehicles = () => (window.DDGarage ? window.DDGarage.PLATFORMS : []).flatMap((p) =>
    p.r.map(([years, codes], ri) => prep({
      k: 'Car', g: 'car', t: `${years} ${p.label}`, s: 'See every system that fits, with a live preview',
      x: 'chevy chevrolet ford gm', years: yearsOf(years), pid: p.id, ri, codes
    })));
  const load = () => {
    if (index) return Promise.resolve(index);
    return fetch('search-index.json')
      .then((r) => r.json())
      .then((data) => (index = vehicles().concat(data.map((e) => prep({ ...e, g: KIND_GROUP[e.k] || 'help' })))))
      .catch(() => (index = vehicles()));
  };

  // ---- Matching ----
  const lev1 = (a, b) => { // true when edit distance <= 1
    if (Math.abs(a.length - b.length) > 1) return false;
    let i = 0, j = 0, edits = 0;
    while (i < a.length && j < b.length) {
      if (a[i] === b[j]) { i++; j++; continue; }
      if (++edits > 1) return false;
      if (a.length > b.length) i++; else if (b.length > a.length) j++; else { i++; j++; }
    }
    return edits + (a.length - i) + (b.length - j) <= 1;
  };
  const scoreToken = (tok, e) => {
    let best = 0;
    for (const w of e.words) {
      if (w === tok) return 3;
      if (w.startsWith(tok)) best = Math.max(best, 2);
      else if (tok.length >= 4 && lev1(tok, w.slice(0, tok.length + 1)) && lev1(tok, w)) best = Math.max(best, 1);
    }
    if (!best && tok.length >= 3 && e.flat.includes(tok)) best = 1;
    return best;
  };
  const KIND_BONUS = { Car: 3, Part: 2, Page: 2, Vehicle: 1, Help: 1 };
  const search = (q) => {
    const toks = norm(q).split(' ').filter(Boolean);
    const qflat = compact(q);
    const hits = [];
    for (const e of index) {
      let score = 0, ok = true;
      for (const t of toks) {
        const s = scoreToken(t, e);
        if (!s) { ok = false; break; }
        score += s;
        if (e.titleWords.some((w) => w.startsWith(t))) score += 3; // title beats background keywords
      }
      if (!ok && qflat.length >= 4 && e.flat.includes(qflat)) { ok = true; score = 4; } // part numbers typed without dashes
      if (!ok) continue;
      if (norm(e.t).startsWith(norm(q))) score += 3;
      score += KIND_BONUS[e.k] || 0;
      hits.push({ e, score });
    }
    hits.sort((a, b) => b.score - a.score || a.e.t.length - b.e.t.length);
    const groups = {};
    for (const { e } of hits) {
      (groups[e.g] ||= []);
      if (groups[e.g].length < MAX[e.g]) groups[e.g].push(e);
    }
    return groups;
  };

  // ---- Rendering ----
  const escapeHTML = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const mark = (text, q) => {
    const toks = norm(q).split(' ').filter((t) => t.length > 1).sort((a, b) => b.length - a.length);
    let html = escapeHTML(text);
    if (!toks.length) return html;
    const re = new RegExp(`\\b(${toks.map((t) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|')})`, 'gi');
    return html.replace(re, '<mark>$1</mark>');
  };
  let options = [];
  let active = -1;
  const ICONS = {
    car: '<path d="M5 17h14M3 13l2-6a2 2 0 0 1 1.9-1.4h10.2A2 2 0 0 1 19 7l2 6v4H3z"/>',
    product: '<circle cx="12" cy="12" r="8"/><path d="m12 12 4-3"/>',
    help: '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3 2.4c-.6.2-1 .7-1 1.3v.8M12 17v.5"/>',
    build: '<path d="M4 18h16M6 18V9l6-4 6 4v9"/>',
    go: '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
    link: '<path d="M7 17 17 7M9 7h8v8"/>'
  };
  const icon = (k) => `<svg viewBox="0 0 24 24" aria-hidden="true">${ICONS[k]}</svg>`;

  const option = (o, i, q) => {
    const external = o.u && /^https?:/.test(o.u);
    return `<li role="option" id="sr-${i}" class="sr-opt" aria-selected="false" data-i="${i}">
      ${icon(o.icon || o.g)}
      <span class="sr-text"><span class="sr-title">${mark(o.t, q)}</span>${o.s ? `<span class="sr-sub">${mark(o.s, q)}</span>` : ''}</span>
      ${external ? `<span class="sr-ext" aria-hidden="true">${icon('link')}</span><span class="sr-only">(opens dakotadigital.com)</span>` : ''}
    </li>`;
  };

  const render = () => {
    const q = input.value.trim();
    options = [];
    let html = '';
    const add = (label, items) => {
      if (!items.length) return;
      const gid = `sg-${label.replace(/\W/g, '')}`;
      html += `<li role="presentation" class="sr-group" id="${gid}">${label}</li>`;
      for (const it of items) { html += option(it, options.length, q); options.push(it); }
    };

    if (!q) {
      const car = window.DDGarage && window.DDGarage.get();
      const quick = [];
      if (car) quick.push({ ...index.find((e) => e.pid === car.pid && e.ri === car.ri), t: `Gauges for your ${car.label}`, s: 'Open the Dash Finder on your car' });
      else quick.push({ t: 'Find gauges for your car', s: 'Pick your car and years in the Dash Finder', u: 'index.html#finder', g: 'car' });
      quick.push({ t: '1969 Camaro RTX Instruments', s: 'RTX-69C-CAM-X · $1,765', u: 'camaro-1969-rtx.html', g: 'product' });
      quick.push({ t: 'Install manuals and tech support', s: 'Manuals, videos and warranty', u: 'support.html', g: 'help' });
      quick.push({ t: 'How long will my order take?', s: 'Build times and shipping', u: 'shipping.html', g: 'help' });
      quick.push({ t: 'Find an installer near you', s: 'Get an install quote', u: 'dealers.html', g: 'help' });
      add('Popular', quick);
      status.textContent = '';
    } else {
      const groups = search(q);
      let count = 0;
      for (const [g, label] of GROUPS) { add(label, groups[g] || []); count += (groups[g] || []).length; }
      if (!count) {
        html += `<li role="presentation" class="sr-empty">No quick matches for “${escapeHTML(q)}”. Try a car like <b>Chevelle</b>, a part # like <b>RTX</b>, or a question like <b>warranty</b>.</li>`;
      }
      add('', [{ t: `Search the full catalog for “${q}”`, s: 'Every product on dakotadigital.com', submit: true, icon: 'go' }]);
      status.textContent = count ? `${count} suggestions. Use the up and down arrows to review.` : 'No quick matches.';
    }
    list.innerHTML = html;
    setActive(-1);
  };

  const setActive = (i) => {
    active = i;
    list.querySelectorAll('.sr-opt').forEach((el) => el.setAttribute('aria-selected', String(Number(el.dataset.i) === i)));
    const el = i >= 0 && list.querySelector(`#sr-${i}`);
    if (el) { input.setAttribute('aria-activedescendant', el.id); el.scrollIntoView({ block: 'nearest' }); }
    else input.removeAttribute('aria-activedescendant');
  };

  const place = () => {
    const r = form.getBoundingClientRect();
    pop.style.setProperty('--pop-top', `${Math.round(r.bottom + 6)}px`);
  };
  const open = () => { place(); pop.hidden = false; input.setAttribute('aria-expanded', 'true'); };
  const close = () => { pop.hidden = true; input.setAttribute('aria-expanded', 'false'); setActive(-1); };

  const choose = (o) => {
    if (!o) return;
    if (o.submit) { close(); form.submit(); return; }
    if (o.pid) {
      const s = [...SERIES_ORDER].find((k) => o.codes.includes(k));
      close();
      input.value = '';
      if (window.DDFinder) { window.DDFinder.show(o.pid, o.ri, s); return; }
      window.DDGarage.set({ pid: o.pid, ri: o.ri });
      location.href = 'index.html#finder';
      return;
    }
    close();
    const here = location.pathname.split('/').pop() || 'index.html';
    const [path, hash] = o.u.split('#');
    location.href = o.u;
    if (path === here && hash) location.hash = hash; // same page: still jump
  };

  // ---- Events ----
  input.addEventListener('focus', () => load().then(() => { render(); open(); }));
  input.addEventListener('input', () => load().then(() => { render(); open(); }));
  input.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      if (pop.hidden) { load().then(() => { render(); open(); }); return; }
      const n = options.length;
      if (!n) return;
      setActive(e.key === 'ArrowDown' ? (active + 1) % n : (active <= 0 ? n - 1 : active - 1));
    } else if (e.key === 'Enter') {
      if (!pop.hidden && active >= 0) { e.preventDefault(); choose(options[active]); }
    } else if (e.key === 'Escape') {
      if (!pop.hidden) { e.preventDefault(); close(); } else if (input.value) { input.value = ''; }
    } else if (e.key === 'Tab') {
      close();
    }
  });
  list.addEventListener('mousedown', (e) => e.preventDefault()); // keep focus in the input
  list.addEventListener('click', (e) => {
    const el = e.target.closest('.sr-opt');
    if (el) choose(options[Number(el.dataset.i)]);
  });
  list.addEventListener('mousemove', (e) => {
    const el = e.target.closest('.sr-opt');
    if (el && Number(el.dataset.i) !== active) setActive(Number(el.dataset.i));
  });
  document.addEventListener('pointerdown', (e) => { if (!form.contains(e.target)) close(); });
  addEventListener('resize', () => { if (!pop.hidden) place(); });
  addEventListener('scroll', () => { if (!pop.hidden) place(); }, { passive: true });

  // "/" jumps to search from anywhere that isn't a text field
  document.addEventListener('keydown', (e) => {
    if (e.key !== '/' || e.metaKey || e.ctrlKey || e.altKey) return;
    const t = e.target;
    if (t.closest && t.closest('input, textarea, select, [contenteditable="true"]')) return;
    e.preventDefault();
    input.focus();
  });
})();

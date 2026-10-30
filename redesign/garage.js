// My Garage: remember the visitor's car across pages, show it in the header,
// and let pages check fitment against it. Stored per browser in localStorage.
(() => {
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
  const KEY = 'dd-garage';
  const listeners = [];

  const read = () => {
    try {
      const v = JSON.parse(localStorage.getItem(KEY));
      const p = v && PLATFORMS.find((x) => x.id === v.pid);
      return p && p.r[v.ri] ? { pid: p.id, ri: v.ri } : null;
    } catch (e) { return null; }
  };
  let car = read();

  const describe = (c) => {
    if (!c) return null;
    const p = PLATFORMS.find((x) => x.id === c.pid);
    return { ...c, platform: p, years: p.r[c.ri][0], label: `${p.r[c.ri][0]} ${p.label}`, codes: p.r[c.ri][1] };
  };

  const set = (c) => {
    car = c;
    try { c ? localStorage.setItem(KEY, JSON.stringify(c)) : localStorage.removeItem(KEY); } catch (e) { /* storage blocked: keep for this page only */ }
    listeners.forEach((fn) => fn(describe(car)));
  };

  window.DDGarage = {
    PLATFORMS,
    get: () => describe(car),
    set,
    onChange: (fn) => { listeners.push(fn); fn(describe(car)); }
  };

  // ---- Header button + dialog ----
  const actions = document.querySelector('.header-actions');
  if (!actions) return;

  const ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 17h14M5 17v2M19 17v2M3 13l2-6a2 2 0 0 1 1.9-1.4h10.2A2 2 0 0 1 19 7l2 6v4H3z"/><circle cx="7.5" cy="13.5" r="1"/><circle cx="16.5" cy="13.5" r="1"/></svg>';
  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'garage-btn';
  btn.setAttribute('aria-haspopup', 'dialog');
  const search = document.querySelector('.header-row .search');
  search ? search.after(btn) : actions.prepend(btn);

  const dlg = document.createElement('dialog');
  dlg.className = 'garage-dialog';
  dlg.setAttribute('aria-labelledby', 'garage-title');
  dlg.innerHTML = `
    <form method="dialog" class="garage-form">
      <div class="garage-head">
        <h2 id="garage-title">My garage</h2>
        <button type="button" class="garage-close" aria-label="Close">×</button>
      </div>
      <p class="garage-lede">Save your car and every page will tell you what fits it.</p>
      <div class="qfield">
        <label for="g-car">Car</label>
        <select id="g-car"><option value="">Choose your car</option>${PLATFORMS.map((p) => `<option value="${p.id}">${p.label}</option>`).join('')}</select>
      </div>
      <div class="qfield">
        <label for="g-years">Years</label>
        <select id="g-years" disabled><option value="">Choose years</option></select>
      </div>
      <button type="submit" class="btn btn-primary btn-block" id="g-save" disabled>Save my car</button>
      <div class="garage-foot">
        <a href="index.html#finder" id="g-shop">See gauges that fit</a>
        <button type="button" class="garage-remove" id="g-remove">Remove car</button>
      </div>
    </form>`;
  document.body.append(dlg);

  const gCar = dlg.querySelector('#g-car');
  const gYears = dlg.querySelector('#g-years');
  const gSave = dlg.querySelector('#g-save');

  const fillYears = (pid, ri) => {
    const p = PLATFORMS.find((x) => x.id === pid);
    gYears.innerHTML = '<option value="">Choose years</option>' + (p ? p.r.map((r, i) => `<option value="${i}">${r[0]}</option>`).join('') : '');
    gYears.disabled = !p;
    if (ri != null) gYears.value = String(ri);
    gSave.disabled = gYears.value === '';
  };
  gCar.addEventListener('change', () => fillYears(gCar.value));
  gYears.addEventListener('change', () => { gSave.disabled = gYears.value === ''; });

  btn.addEventListener('click', () => {
    const c = describe(car);
    gCar.value = c ? c.pid : '';
    fillYears(gCar.value, c ? c.ri : null);
    dlg.querySelector('.garage-foot').hidden = !c;
    dlg.showModal();
  });
  dlg.querySelector('.garage-close').addEventListener('click', () => dlg.close());
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });
  dlg.querySelector('form').addEventListener('submit', () => {
    if (gCar.value && gYears.value !== '') set({ pid: gCar.value, ri: Number(gYears.value) });
  });
  dlg.querySelector('#g-remove').addEventListener('click', () => { set(null); dlg.close(); });

  let first = true;
  window.DDGarage.onChange((c) => {
    if (!first && c) { btn.classList.remove('pulse'); void btn.offsetWidth; btn.classList.add('pulse'); }
    first = false;
    btn.innerHTML = `${ICON}<span class="garage-label">${c ? c.label : 'Add your car'}</span>`;
    btn.classList.toggle('has-car', !!c);
    btn.setAttribute('aria-label', c ? `My garage: ${c.label}. Change car` : 'My garage: add your car');
  });
})();

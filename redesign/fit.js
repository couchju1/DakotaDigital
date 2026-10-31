// My Garage everywhere: "Fits your car" badges on product cards, a fit strip on product pages,
// and a filter on category pages. Fit data comes from data-cats (store categories for the car
// lines a product belongs to) and data-years (years in its title), written by build_catalog.py.
(() => {
  if (!window.DDGarage) return;
  const BASE = new URL('.', document.currentScript.src).href;
  const yearsOf = window.DDGarage.yearsOf;
  const read = (el) => ({
    cats: (el.dataset.cats || '').split(',').filter(Boolean).map(Number),
    years: (el.dataset.years || '').split(',').filter(Boolean).map(Number),
    not: (el.dataset.not || '').split(',').filter(Boolean).map(Number)
  });
  // 'yes' | 'maybe' (right car, no years to check) | 'no' | '' (not car-specific)
  const verdict = (data, car) => {
    // Listed under a truck it doesn't fit, or made only for a car the finder doesn't list (S-10s).
    if (car && (data.not.includes(car.platform.cat) || (data.not.length && !data.cats.length))) return 'no';
    if (!data.cats.length || !car) return '';
    if (!data.cats.includes(car.platform.cat)) return 'no';
    if (!data.years.length) return 'maybe';
    const mine = yearsOf(car.years);
    return data.years.some((y) => mine.includes(y)) ? 'yes' : 'no';
  };
  const ICON = {
    yes: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>',
    no: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 2 20h20zM12 10v4M12 17v.5"/></svg>',
    car: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 17h14M3 13l2-6a2 2 0 0 1 1.9-1.4h10.2A2 2 0 0 1 19 7l2 6v4H3z"/></svg>'
  };

  // ---- Product page strip ----
  const strip = document.getElementById('fit');
  const renderStrip = (car) => {
    if (!strip || !strip.dataset.cats) return;
    const v = verdict(read(strip), car);
    if (!car) {
      strip.className = 'fit fit-unknown';
      strip.innerHTML = `${ICON.car}<p><strong>Will it fit?</strong> <button type="button" class="fit-add">Add your car</button> and we'll check every product for you.</p>`;
      strip.querySelector('.fit-add').addEventListener('click', () => document.querySelector('.garage-btn').click());
    } else if (v === 'yes') {
      strip.className = 'fit fit-yes';
      strip.innerHTML = `${ICON.yes}<p><strong>Fits your ${car.label}.</strong></p>`;
    } else if (v === 'maybe') {
      strip.className = 'fit fit-unknown';
      strip.innerHTML = `${ICON.car}<p><strong>Made for the ${car.platform.label}.</strong> Check the years and notes below, or <a href="tel:+18008523228">call us</a> to confirm.</p>`;
    } else {
      strip.className = 'fit fit-no';
      strip.innerHTML = `${ICON.no}<p><strong>Doesn't fit your ${car.label}.</strong> <a href="${BASE}index.html#finder">See what fits your car</a></p>`;
    }
  };

  // ---- Product cards + category filter ----
  const cards = [...document.querySelectorAll('.shop-card[data-cats], .shop-card[data-not]')];
  const allCards = [...document.querySelectorAll('.shop-card')];
  const bar = document.querySelector('.fit-filter');
  // The "31 products" heading above the grid: keep its number in step with what is shown.
  const countHead = document.getElementById('prods');
  const setCount = (n) => { if (countHead) countHead.textContent = `${n} ${n === 1 ? 'product' : 'products'}`; };
  let showAll = false;
  const badge = (card, v, car) => {
    let el = card.querySelector('.card-fit');
    if (v === 'yes' || v === 'maybe') {
      if (!el) {
        el = document.createElement('span');
        el.className = 'card-fit';
        card.querySelector('a').prepend(el);
      }
      el.textContent = v === 'yes' ? 'Fits your car' : `For your ${car.platform.label}`;
    } else if (el) el.remove();
  };
  // ?line=RTX (from the Dash Finder) narrows the list to one gauge line, matched on the card's SKU.
  const LINES = ['GRFX', 'RTX', 'HDX', 'VHX', 'VFD3'];
  const lineOf = (card) => ((card.querySelector('.card-sku') || {}).textContent || '').trim().toUpperCase();
  let line = (new URLSearchParams(location.search).get('line') || '').toUpperCase();
  if (!LINES.includes(line) || !allCards.some((c) => lineOf(c).startsWith(line))) line = '';
  const clearLine = () => {
    line = '';
    const url = new URL(location.href);
    url.searchParams.delete('line');
    history.replaceState(null, '', url);
    renderCards(window.DDGarage.get());
  };
  // Years for a card: data-years, or the years in its name when the card has no fit data.
  const cardYears = (card) => {
    const data = read(card);
    if (data.years.length) return data.years;
    const name = (card.querySelector('.card-name') || {}).textContent || '';
    const m = name.match(/\b((?:19|20)\d\d)(?:\s*-\s*(\d{2,4}))?/);
    return m ? yearsOf(m[2] ? `${m[1]}-${m[2]}` : m[1]) : [];
  };
  const fitsLine = (card, car) => {
    if (!lineOf(card).startsWith(line)) return false;
    if (!car) return true;
    const data = read(card);
    if (data.not.includes(car.platform.cat) || (data.not.length && !data.cats.length)) return false;
    if (data.cats.length && !data.cats.includes(car.platform.cat)) return false;
    const ys = cardYears(card);
    const mine = yearsOf(car.years);
    return !ys.length || ys.some((y) => mine.includes(y));
  };
  const renderCards = (car) => {
    if (line) return renderLine(car);
    let fits = 0, relevant = 0;
    cards.forEach((card) => {
      const v = verdict(read(card), car);
      badge(card, v, car);
      if (v === 'yes' || v === 'maybe') fits += 1;
      if (v) relevant += 1;
      card.hidden = !showAll && car && v === 'no';
    });
    // Untagged cards: a kit for a model year belongs to some other car, so it can't fit this one;
    // anything without years (universal panels, clocks) stays.
    const untagged = allCards.filter((c) => !c.dataset.cats && !c.dataset.not);
    untagged.forEach((c) => { c.hidden = Boolean(!showAll && car && cardYears(c).length); });
    if (!bar) return;
    if (!car || !relevant || !fits) { bar.hidden = true; allCards.forEach((c) => { c.hidden = false; }); setCount(allCards.length); return; }
    bar.hidden = false;
    setCount(allCards.filter((c) => !c.hidden).length);
    // Products with no fit data (universal panels, clocks) stay in the list; say so, so the count adds up.
    const general = untagged.filter((c) => !cardYears(c).length).length;
    const plus = general ? `, plus ${general} universal ${general === 1 ? 'product' : 'products'}` : '';
    bar.innerHTML = `<p>${showAll ? `Showing all ${allCards.length}. <strong>${fits}</strong> fit your ${car.label}.` : `Showing <strong>${fits}</strong> that fit your ${car.label}${plus}.`}</p>
      <button type="button" class="btn btn-ghost fit-toggle" aria-pressed="${!showAll}">${showAll ? 'Show only my car' : 'Show all products'}</button>`;
    bar.querySelector('.fit-toggle').addEventListener('click', () => { showAll = !showAll; renderCards(window.DDGarage.get()); });
  };
  const renderLine = (car) => {
    let shown = 0;
    allCards.forEach((card) => {
      badge(card, verdict(read(card), car), car);
      card.hidden = !fitsLine(card, car);
      if (!card.hidden) shown += 1;
    });
    // Nothing in this line for the saved car: show the whole line rather than an empty page.
    const fitsCar = Boolean(car && shown);
    if (!shown) allCards.forEach((card) => { card.hidden = !lineOf(card).startsWith(line); if (!card.hidden) shown += 1; });
    setCount(shown);
    if (!bar) return;
    bar.hidden = false;
    bar.innerHTML = `<p>Showing <strong>${shown} ${line}</strong> ${shown === 1 ? 'system' : 'systems'}${fitsCar ? ` that fit your ${car.label}` : ''}.</p>
      <button type="button" class="btn btn-ghost fit-toggle">Show all lines</button>`;
    bar.querySelector('.fit-toggle').addEventListener('click', clearLine);
  };

  window.DDGarage.onChange((car) => { renderStrip(car); renderCards(car); });
})();

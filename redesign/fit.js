// My Garage everywhere: "Fits your car" badges on product cards, a fit strip on product pages,
// and a filter on category pages. Fit data comes from data-cats (store categories for the car
// lines a product belongs to) and data-years (years in its title), written by build_catalog.py.
(() => {
  if (!window.DDGarage) return;
  const BASE = new URL('.', document.currentScript.src).href;
  const yearsOf = (range) => {
    const [a, b] = range.split('-');
    const start = Number(a);
    const end = b ? Number(a.slice(0, 4 - b.length) + b) : start;
    const out = [];
    for (let y = start; y <= end; y++) out.push(y);
    return out;
  };
  const read = (el) => ({
    cats: (el.dataset.cats || '').split(',').filter(Boolean).map(Number),
    years: (el.dataset.years || '').split(',').filter(Boolean).map(Number)
  });
  // 'yes' | 'maybe' (right car, no years to check) | 'no' | '' (not car-specific)
  const verdict = (data, car) => {
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
  const cards = [...document.querySelectorAll('.shop-card[data-cats]')];
  const bar = document.querySelector('.fit-filter');
  let showAll = false;
  const renderCards = (car) => {
    let fits = 0, relevant = 0;
    cards.forEach((card) => {
      const v = verdict(read(card), car);
      let badge = card.querySelector('.card-fit');
      if (v === 'yes' || v === 'maybe') {
        if (!badge) {
          badge = document.createElement('span');
          badge.className = 'card-fit';
          card.querySelector('a').prepend(badge);
        }
        badge.textContent = v === 'yes' ? 'Fits your car' : `For your ${car.platform.label}`;
        fits += 1;
      } else if (badge) badge.remove();
      if (v) relevant += 1;
      card.hidden = !showAll && car && v === 'no';
    });
    if (!bar) return;
    if (!car || !relevant || !fits) { bar.hidden = true; cards.forEach((c) => { c.hidden = false; }); return; }
    bar.hidden = false;
    bar.innerHTML = `<p>${showAll ? `Showing all ${cards.length}. <strong>${fits}</strong> fit your ${car.label}.` : `Showing <strong>${fits}</strong> that fit your ${car.label}.`}</p>
      <button type="button" class="btn btn-ghost fit-toggle" aria-pressed="${!showAll}">${showAll ? 'Show only my car' : 'Show all products'}</button>`;
    bar.querySelector('.fit-toggle').addEventListener('click', () => { showAll = !showAll; renderCards(window.DDGarage.get()); });
  };

  window.DDGarage.onChange((car) => { renderStrip(car); renderCards(car); });
})();

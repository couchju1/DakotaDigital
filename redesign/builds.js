// Builds gallery: "Put this dash in my car" loads the build's car and look into the
// Dash Finder, and builds that match the saved car move to the front.
(() => {
  const rail = document.getElementById('build-rail');
  if (!rail) return;
  const cards = [...rail.children];

  rail.addEventListener('click', (e) => {
    const btn = e.target.closest('.build-try');
    if (!btn) return;
    const { pid, ri, s } = btn.closest('.build').dataset;
    window.DDFinder.show(pid, Number(ri), s);
  });

  window.DDGarage.onChange((car) => {
    const matches = (el) => car && el.dataset.pid === car.pid && Number(el.dataset.ri) === car.ri;
    const sameModel = (el) => car && el.dataset.pid === car.pid;
    const rank = (el) => (matches(el) ? 0 : sameModel(el) ? 1 : 2);
    cards
      .map((el, i) => ({ el, i }))
      .sort((a, b) => rank(a.el) - rank(b.el) || a.i - b.i)
      .forEach(({ el }) => rail.append(el));
    cards.forEach((el) => {
      const badge = el.querySelector('.build-match');
      badge.hidden = !sameModel(el);
      badge.textContent = matches(el) ? 'Your car' : `Your ${car ? car.platform.label : ''}`;
    });
    rail.scrollLeft = 0;
  });
})();

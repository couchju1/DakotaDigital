// Buy dock: when the buy box scrolls out of view, a compact bar keeps the live total,
// fit status and Add to cart in reach. Bottom of the screen on phones, under the header
// on desktop. It mirrors the buy box rather than duplicating its logic.
// Works on the hand-built product page (#buy-form) and every catalog page (.shop-buy).
(() => {
  const BASE = new URL('.', document.currentScript.src).href;
  const form = document.getElementById('buy-form') || document.querySelector('.shop-buy');
  const addBtn = document.getElementById('add-btn');
  if (!form || !addBtn) return;
  const total = document.getElementById('total') || form.querySelector('[data-b="total"]');
  const title = document.getElementById('buy-title');
  const fit = document.getElementById('fit');
  const note = document.getElementById('buy-note') || form.querySelector('[data-b="note"]');

  const dock = document.createElement('aside');
  dock.className = 'buy-dock';
  dock.setAttribute('aria-label', 'Quick buy');
  dock.hidden = true;
  dock.innerHTML = `
    <div class="wrap dock-row">
      <img class="dock-thumb" alt="" width="240" height="163">
      <div class="dock-info">
        <p class="dock-title"></p>
        <p class="dock-meta"><span class="dock-total"></span><span class="dock-fit"></span><span class="dock-ship"></span></p>
        <p class="dock-note" role="status"></p>
      </div>
      <div class="dock-actions">
        <a class="btn btn-ghost dock-call" href="tel:+18008523228" aria-label="Call (800) 852-3228"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg><span>Call</span></a>
        <a class="btn btn-ghost dock-options" href="#buy-title">Options</a>
        <button type="button" class="btn btn-primary dock-add"></button>
      </div>
    </div>`;
  document.body.append(dock);
  const $ = (s) => dock.querySelector(s);

  // Mirror the buy box: title, total, item count, backlight photo, fit status.
  const sync = () => {
    $('.dock-title').textContent = title.textContent;
    $('.dock-total').textContent = total.textContent;
    $('.dock-add').textContent = addBtn.textContent;
    const ship = document.querySelector('[data-ship="range"]');
    $('.dock-ship').textContent = ship ? `Ships ${ship.textContent.replace(/^Est\. /, 'est. ')}` : '';
    const color = document.querySelector('.backlight .swatch[aria-pressed="true"]');
    const pic = document.querySelector('[data-theme-img]') || document.querySelector('.shop-main img');
    if (color) $('.dock-thumb').src = `${BASE}img/rtx69/${color.dataset.color}-thumb.webp`;
    else if (pic) $('.dock-thumb').src = pic.src;
    else $('.dock-thumb').hidden = true;
    const f = $('.dock-fit');
    if (fit && fit.classList.contains('fit-yes')) { f.textContent = 'Fits your car'; f.className = 'dock-fit is-yes'; }
    else if (fit && fit.classList.contains('fit-no')) { f.textContent = "Doesn't fit your car"; f.className = 'dock-fit is-no'; }
    else { f.textContent = ''; f.className = 'dock-fit'; }
  };
  const watch = (el, opts) => el && new MutationObserver(sync).observe(el, opts);
  watch(total, { childList: true, characterData: true, subtree: true });
  watch(addBtn, { childList: true, characterData: true, subtree: true });
  watch(fit, { attributes: true, attributeFilter: ['class'] });
  watch(document.querySelector('.backlight'), { attributes: true, subtree: true, attributeFilter: ['aria-pressed'] });
  watch(document.querySelector('[data-theme-img]'), { attributes: true, attributeFilter: ['src'] });
  sync();

  // Add to cart from the dock submits the real form and echoes its confirmation here.
  $('.dock-add').addEventListener('click', () => {
    form.requestSubmit();
    $('.dock-note').textContent = note && !note.hidden ? note.textContent : '';
  });
  form.addEventListener('change', () => { $('.dock-note').textContent = ''; });

  // Show the dock only while the buy box's own button is off screen and we've scrolled past the top.
  let buyVisible = true;
  const top = document.querySelector('.product-grid') || document.querySelector('.shop-product');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let shown = false;
  const setShown = (show) => {
    if (show === shown) return;
    shown = show;
    if (show) {
      dock.hidden = false;
      requestAnimationFrame(() => dock.classList.add('is-in'));
      document.body.classList.add('has-dock');
    } else {
      dock.classList.remove('is-in');
      document.body.classList.remove('has-dock');
      if (reduce.matches) dock.hidden = true;
      else setTimeout(() => { if (!shown) dock.hidden = true; }, 200);
    }
  };
  const decide = () => {
    const pastTop = top ? top.getBoundingClientRect().top < 0 : scrollY > 400;
    setShown(!buyVisible && pastTop);
  };
  new IntersectionObserver(([e]) => { buyVisible = e.isIntersecting; decide(); }, { rootMargin: '-80px 0px 0px 0px' }).observe(addBtn);
  addEventListener('scroll', decide, { passive: true });

  // On desktop the dock tucks under the sticky header.
  const header = document.querySelector('.site-header');
  const place = () => dock.style.setProperty('--dock-top', `${header ? Math.round(header.getBoundingClientRect().height) : 0}px`);
  place();
  addEventListener('resize', place);

  // "Options" scrolls back to the buy box and puts focus on its first choice.
  $('.dock-options').addEventListener('click', (e) => {
    e.preventDefault();
    title.scrollIntoView({ behavior: reduce.matches ? 'auto' : 'smooth', block: 'start' });
    const first = form.querySelector('input:checked') || form.querySelector('input');
    if (first) first.focus({ preventScroll: true });
  });
})();

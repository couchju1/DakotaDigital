// Generic buy box for catalog product pages: version picker, option steps, add-ons and
// running total, from the item data embedded in the page.
(() => {
  const form = document.querySelector('.shop-buy');
  if (!form) return;
  const items = JSON.parse(form.querySelector('[data-b="items"]').textContent);
  const $ = (k) => form.querySelector(`[data-b="${k}"]`);
  const money = (n) => n.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  let cur = 0;

  const renderSteps = () => {
    const it = items[cur];
    $('steps').innerHTML = it.steps.map((s, si) => {
      if (s.type === 'select') {
        return `<div class="qfield"><label for="st-${si}">${esc(s.title.replace(/^please select\s*/i, '') || 'Option')}</label>
          <select id="st-${si}" data-step="${si}">${s.options.map((o, oi) => `<option value="${oi}">${esc(o.t)}</option>`).join('')}</select></div>`;
      }
      return `<fieldset class="opt-group"><legend>${esc(s.title)}</legend>${s.options.map((o, oi) =>
        `<label class="opt"><input type="checkbox" data-step="${si}" value="${oi}"><span class="opt-text">${esc(o.t)}</span>${o.d ? `<span class="opt-price">+${money(o.d)}</span>` : ''}</label>`).join('')}</fieldset>`;
    }).join('');
  };

  const update = () => {
    const it = items[cur];
    let total = it.price;
    let count = 1;
    form.querySelectorAll('[data-step]').forEach((el) => {
      const step = it.steps[el.dataset.step];
      if (el.tagName === 'SELECT') total += step.options[el.value].d || 0;
      else if (el.checked) { total += step.options[el.value].d || 0; count += 1; }
    });
    $('sku').textContent = it.sku;
    $('price').textContent = money(it.price);
    $('total').textContent = money(total);
    document.getElementById('add-btn').textContent = `Add ${count} item${count > 1 ? 's' : ''} to cart`;
    $('note').hidden = true;
  };

  form.addEventListener('change', (e) => {
    if (e.target.name === 'item') { cur = Number(e.target.value); renderSteps(); }
    update();
  });
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const it = items[cur];
    const picks = [...form.querySelectorAll('[data-step]')].filter((el) => el.tagName === 'SELECT' || el.checked)
      .map((el) => it.steps[el.dataset.step].options[el.value].t);
    const note = $('note');
    note.innerHTML = `Prototype: this would add ${esc(it.sku)}${picks.length ? ` (${esc(picks.join(', '))})` : ''} to the cart. <a href="${form.dataset.live}">Buy on dakotadigital.com</a>`;
    note.hidden = false;
  });
  renderSteps();
  update();
})();

// Lighting theme switcher: real "Theme:" photos from the product gallery
(() => {
  const box = document.querySelector('.themes');
  if (!box) return;
  const img = box.querySelector('[data-theme-img]');
  const chips = [...box.querySelectorAll('.theme-chip')];
  chips.forEach((c) => { const pre = new Image(); pre.src = c.dataset.src; });
  box.addEventListener('click', (e) => {
    const chip = e.target.closest('.theme-chip');
    if (!chip) return;
    img.src = chip.dataset.src;
    img.alt = `Lit up in the ${chip.textContent} theme`;
    chips.forEach((c) => c.setAttribute('aria-pressed', String(c === chip)));
  });
})();

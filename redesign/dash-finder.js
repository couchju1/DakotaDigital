// Dash Finder: pick a car, its years and a look; preview the gauge with the key on.
// Fitment data comes from the Dash Finder design (verify against the catalog before launch).
(() => {
  const root = document.getElementById('finder');
  if (!root) return;

  // Fitment data lives in garage.js so every page shares it.
  const PLATFORMS = window.DDGarage.PLATFORMS;
  const SERIES = window.DDGarage.SERIES;
  // Redesigned product pages, keyed by platform|years|series. Everything else goes to the category page.
  const PRODUCT_PAGES = { 'camaro|1969|R': 'camaro-1969-rtx.html' };
  // Local catalog page for each store category (filled in by tools/build_pages.py)
  const CAT_PATHS = {/*CAT_PATHS*/59:"shop/automotive-c59.html",60:"shop/motorcycle-c60.html",69:"shop/universal-instrument-systems-c69.html",70:"shop/individual-instruments-c70.html",71:"shop/air-ride-monitoring-c71.html",77:"shop/mounts-cups-senders-c77.html",113:"shop/senders-speed-adaptors-c113.html",115:"shop/speedometer-calibration-devices-c115.html",230:"shop/universal-street-rod-panels-c230.html",231:"shop/retrotech-c231.html",232:"shop/designer-series-c232.html",233:"shop/oval-designer-series-c233.html",234:"shop/round-designer-series-c234.html",236:"shop/individual-instruments-gauges-c236.html",239:"shop/antennas-c239.html",240:"shop/speedometers-tachometers-c240.html",241:"shop/oil-pressure-oil-temp-c241.html",243:"shop/voltage-amperage-c243.html",244:"shop/fuel-level-fuel-and-nitrous-pressure-c244.html",245:"shop/water-temp-transmission-temp-c245.html",247:"shop/boost-vacuum-c247.html",248:"shop/egt-pyrometer-cylinder-head-temp-c248.html",249:"shop/ambient-air-amp-temp-c249.html",250:"shop/clocks-c250.html",252:"shop/multi-function-gauges-c252.html",253:"shop/complete-gauge-sets-c253.html",255:"shop/technical-support-manuals-c255.html",260:"shop/ion-series-c260.html",261:"shop/odyssey-series-i-c261.html",262:"shop/odyssey-series-ii-and-solarix-series-c262.html",287:"shop/speedometer-calibration-and-interfaces-c287.html",291:"shop/climate-control-c291.html",297:"shop/elliptical-designer-series-c297.html",298:"shop/programable-gear-indicators-c298.html",311:"shop/sending-units-c311.html",328:"shop/led-replacement-tail-lights-c328.html",329:"shop/chevrolet-c329.html",330:"shop/1955-59-full-size-car-tail-lights-c330.html",331:"shop/1958-90-impala-caprice-bel-air-biscayne-tail-lights-c331.html",332:"shop/1964-72-chevelle-malibu-cars-tail-lights-c332.html",333:"shop/1962-74-nova-tail-lights-c333.html",334:"shop/1967-77-camaro-tail-lights-c334.html",335:"shop/1940-91-full-size-truck-tail-lights-c335.html",337:"shop/digital-climate-control-c337.html",339:"shop/pontiac-c339.html",341:"shop/1961-67-corvette-tail-lights-c341.html",342:"shop/ford-c342.html",343:"shop/1964-73-mustang-tail-lights-c343.html",344:"shop/1966-77-bronco-tail-lights-c344.html",345:"shop/64-72-pickup-c345.html",346:"shop/1965-74-econoline-van-tail-lights-c346.html",350:"shop/gift-certificate-c350.html",351:"shop/replacement-parts-c351.html",357:"shop/replacement-parts-c357.html",358:"shop/sending-units-c358.html",371:"shop/american-ironhorse-models-c371.html",373:"shop/careers-c373.html",374:"shop/no-load-flasher-c374.html",375:"shop/victory-models-c375.html",381:"shop/big-dog-models-c381.html",399:"shop/cruise-control-c399.html",400:"shop/remote-controls-and-accessories-c400.html",401:"shop/gear-position-indicators-auto-trans-c401.html",402:"shop/linear-actuators-and-controllers-c402.html",403:"shop/accessory-electronics-controllers-c403.html",406:"shop/automotive-accessories-c406.html",408:"shop/chevy-gm-c408.html",409:"shop/ford-c409.html",410:"shop/jeep-c410.html",411:"shop/buick-c411.html",412:"shop/oldsmobile-c412.html",413:"shop/pontiac-c413.html",414:"shop/volkswagen-c414.html",415:"shop/mercury-c415.html",417:"shop/custom-instruments-c417.html",420:"shop/1932-57-chevy-full-size-car-c420.html",421:"shop/1940-72-chevy-and-gmc-pickup-suburban-c421.html",422:"shop/camaro-c422.html",423:"shop/caprice-impala-c423.html",424:"shop/chevelle-malibu-c424.html",425:"shop/el-camino-c425.html",426:"shop/nova-c426.html",427:"shop/corvette-c427.html",428:"shop/monte-carlo-c428.html",429:"shop/led-tail-lights-gm-c429.html",433:"shop/1932-57-ford-and-mercury-cars-c433.html",434:"shop/falcon-and-mustangs-c434.html",435:"shop/mercury-c435.html",437:"shop/1935-66-ford-pickup-and-bronco-c437.html",438:"shop/broncos-c438.html",439:"shop/led-tail-lights-c439.html",473:"shop/universal-mounts-c473.html",476:"shop/cruise-control-accessories-c476.html",477:"shop/cruise-control-kits-c477.html",478:"shop/replacement-parts-for-cruise-controls-c478.html",479:"shop/remote-systems-c479.html",480:"shop/remote-control-accessories-c480.html",481:"shop/replacement-parts-for-remote-control-systems-c481.html",497:"shop/64-73-mustang-c497.html",498:"shop/64-77-pickup-c498.html",499:"shop/65-74-econoline-van-c499.html",500:"shop/66-77-bronco-c500.html",504:"shop/55-59-full-size-car-c504.html",505:"shop/61-67-corvette-c505.html",506:"shop/58-90-impala-caprice-bel-air-biscayne-c506.html",507:"shop/62-74-nova-c507.html",508:"shop/64-72-chevelle-malibu-cars-c508.html",509:"shop/67-77-camaro-c509.html",510:"shop/40-91-full-size-truck-c510.html",516:"shop/universal-gauges-for-custom-or-standard-and-metric-bikes-c516.html",517:"shop/hidden-antenna-c517.html",518:"shop/mcl-5000-series-c518.html",519:"shop/speedometer-interface-c519.html",529:"shop/speedometer-with-indicators-c529.html",531:"shop/individual-instruments-gauges-c531.html",534:"shop/speedometer-c534.html",537:"shop/individual-instruments-gauges-c537.html",538:"shop/programmable-gear-indicators-c538.html",540:"shop/direct-fit-big-dog-speedometer-c540.html",541:"shop/individual-instruments-gauges-c541.html",542:"shop/programmable-gear-indicators-c542.html",543:"shop/round-gauges-c543.html",544:"shop/mcl-5000-series-c544.html",545:"shop/replacement-parts-c545.html",546:"shop/mounts-cups-senders-c546.html",549:"shop/temperature-gauges-c549.html",550:"shop/speedometers-tachometers-c550.html",551:"shop/oil-air-pressure-gauges-c551.html",557:"shop/mounts-cups-senders-c557.html",558:"shop/mcl-5000-series-c558.html",560:"shop/speedometers-tachometers-c560.html",561:"shop/temperature-gauges-c561.html",562:"shop/oil-air-pressure-gauges-c562.html",563:"shop/fuel-level-volt-gauges-c563.html",564:"shop/fuel-level-volt-gauges-c564.html",567:"shop/gauge-cups-and-mounting-brackets-c567.html",568:"shop/sending-units-c568.html",569:"shop/gauge-cups-and-mounting-bracket-c569.html",570:"shop/sending-units-c570.html",571:"shop/mcl-5000-series-c571.html",572:"shop/round-gauges-c572.html",579:"shop/speedometers-tachometers-c579.html",580:"shop/temperature-gauges-c580.html",581:"shop/oil-air-pressure-gauges-c581.html",582:"shop/fuel-level-volt-gauges-c582.html",583:"shop/clock-c583.html",584:"shop/mounts-cups-senders-c584.html",586:"shop/mcv-7000-and-mcl-5000-series-c586.html",587:"shop/round-gauges-c587.html",589:"shop/speedometers-tachometers-c589.html",590:"shop/temperature-gauges-c590.html",591:"shop/oil-air-pressure-gauges-c591.html",592:"shop/fuel-level-volt-gauges-c592.html",593:"shop/clock-c593.html",594:"shop/mounts-cups-senders-c594.html",596:"shop/mcv-7000-and-mcl-5000-series-c596.html",597:"shop/round-gauges-c597.html",598:"shop/replacement-parts-mc-c598.html",600:"shop/speedometers-tachometers-c600.html",601:"shop/temperature-gauges-c601.html",602:"shop/oil-air-pressure-gauges-c602.html",603:"shop/fuel-level-volt-gauges-c603.html",604:"shop/clock-c604.html",605:"shop/mounts-cups-senders-c605.html",616:"shop/gauge-cups-and-mounting-brackets-c616.html",617:"shop/sending-units-c617.html",618:"shop/gauge-cups-and-mounting-brackets-c618.html",619:"shop/sending-units-c619.html",620:"shop/gauge-cups-and-mounting-brackets-c620.html",621:"shop/sending-units-c621.html",622:"shop/gauge-cups-and-mounting-brackets-c622.html",643:"shop/motor-market-six-degrees-c643.html",646:"shop/expansion-modules-c646.html",649:"shop/expansion-modules-c649.html",679:"shop/mopar-c679.html",682:"shop/toyota-c682.html",687:"shop/lincoln-c687.html",688:"shop/fairlane-galaxie-and-torino-c688.html",689:"shop/hdx-series-c689.html",694:"shop/tachometer-calibration-and-interfaces-c694.html",695:"shop/air-ride-monitoring-c695.html",697:"shop/rtx-hdx-vhx-or-vfd-c697.html",705:"shop/cadillac-c705.html",706:"shop/rtx-series-c706.html",707:"shop/harley-davidson-dressers-and-baggers-c707.html",708:"shop/harley-davidson-road-king-softail-deuce-dyna-c708.html",709:"shop/harley-davidson-sportster-dyna-rocker-softail-c709.html",711:"shop/new-motorcycle-products-c711.html",712:"shop/new-automotive-products-c712.html",714:"shop/automotive-app-privacy-policy-c714.html",716:"shop/motorcycle-app-privacy-policy-c716.html",784:"shop/1973-98-gm-trucks-c784.html",787:"shop/accessories-app-privacy-policy-c787.html",804:"shop/media-coverage-c804.html",805:"shop/technical-support-frequently-asked-questions-c805.html",806:"shop/technical-support-frequently-asked-questions-powersports-c806.html",808:"shop/automotive-instrument-system-videos-c808.html",809:"shop/cruise-control-videos-c809.html",810:"shop/automotive-instrument-add-on-videos-c810.html",811:"shop/automotive-accessory-controller-videos-c811.html",812:"shop/motorcycle-videos-c812.html",814:"shop/mlx-9000-series-c814.html",815:"shop/mlx-9000-series-c815.html",816:"shop/mlx-9000-series-c816.html",817:"shop/speed-tach-with-indicators-mlx-9000-series-for-american-iron-c817.html",818:"shop/speed-tach-with-indicators-c818.html",825:"shop/dakota-digital-app-privacy-policy-c825.html",826:"shop/mlx-5000-series-c826.html",830:"shop/1967-04-ford-pickup-e-van-and-bronco-c830.html",836:"shop/international-c836.html",840:"shop/dakota-digital-software-downloads-c840.html",842:"shop/land-rover-c842.html"};
  const ORDER = ['R', 'H', 'V', 'G', 'D'];
  const LIGHTS = [['Ice blue', '#3A9BFF'], ['Red', '#FF4B3E'], ['Amber', '#FFB020'], ['White', '#F2F2EE'], ['Green', '#3DDC84']];

  const state = { pid: 'camaro', ri: 0, s: 'R', light: '#3A9BFF', speed: 65 };
  // Start from the visitor's saved car, if any.
  const saved = window.DDGarage.get();
  if (saved) { state.pid = saved.pid; state.ri = saved.ri; }

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
      (CAT_PATHS[p.cat] ? `${CAT_PATHS[p.cat]}?line=${cur.name}` : '') ||
      `https://www.dakotadigital.com/index.cfm/page/ptype=results/category_id=${p.cat}/mode=cat/cat${p.cat}.htm`;
    // Once a car is picked (and saved), offer the Dash Builder for it.
    const dash = out('dash');
    dash.hidden = !window.DDGarage.get();
    dash.href = `dash-builder.html?car=${p.id}&years=${encodeURIComponent(years)}&system=${cur.name}`;
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
    // Picking a car or years saves it to the garage; render() runs from the garage listener.
    if (which === 'car' || which === 'years') { window.DDGarage.set({ pid: state.pid, ri: state.ri }); return; }
    if (which === 'looks') state.s = key;
    if (which === 'lights') state.light = key;
    render();
  });

  speedInput.addEventListener('input', () => { state.speed = Number(speedInput.value); updateSpeed(); });

  speedInput.value = state.speed;
  keepSeries(codes());
  // Let other sections (the builds gallery) load a car + look into the finder.
  window.DDFinder = {
    show(pid, ri, s) {
      state.s = s;
      if (state.pid === pid && state.ri === ri) render();
      window.DDGarage.set({ pid, ri });
      root.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
      const picked = list('looks').querySelector('[aria-pressed="true"]');
      if (picked) picked.focus({ preventScroll: true });
    }
  };

  // Follow garage changes made from the header dialog too.
  window.DDGarage.onChange((c) => {
    if (c && (c.pid !== state.pid || c.ri !== state.ri)) { state.pid = c.pid; state.ri = c.ri; keepSeries(codes()); }
    render();
  });
})();

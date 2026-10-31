"""Generate the content pages of the redesign and keep the header/footer of every page in sync.

Run from the repo root:  python tools/build_pages.py
Content lives in tools/content/*.json (media, builds, FAQ, legal text) and in this file.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'redesign'
CONTENT = ROOT / 'tools' / 'content'
LIVE = 'https://www.dakotadigital.com/'
# Where this redesign is published (used for absolute URLs in structured data). Change at launch.
SITE_URL = 'https://dakotadigital-ten.vercel.app/'
# Launch switch (site.config.json): while false, every page says noindex and robots.txt blocks crawlers.
INDEXABLE = json.loads((ROOT / 'site.config.json').read_text(encoding='utf-8')).get('indexable', False)
ROBOTS_META = '' if INDEXABLE else '  <meta name="robots" content="noindex, nofollow">\n'


def load(name):
    return json.loads((CONTENT / f'{name}.json').read_text(encoding='utf-8'))


def esc(s):
    return html.escape(s, quote=True)


# Catalog pages built by tools/build_catalog.py (shop/...). Links go there when a page exists.
_CATALOG_PATH = CONTENT / 'catalog.json'
CATALOG = json.loads(_CATALOG_PATH.read_text(encoding='utf-8')) if _CATALOG_PATH.exists() else {'cats': {}, 'products': {}}


def cat(cid):
    c = CATALOG['cats'].get(str(cid))
    return c['path'] if c else f'{LIVE}index.cfm/page/ptype=results/category_id={cid}/mode=cat/cat{cid}.htm'


def prd(pid, cid):
    p = CATALOG['products'].get(str(pid))
    return p['path'] if p else f'{LIVE}index.cfm/page/ptype=product/product_id={pid}/category_id={cid}/mode=prod/prd{pid}.htm'


def localize_links(s):
    """Point live category/product URLs in hand-built pages at our catalog pages."""
    def repl(m):
        url = m.group(1)
        pm = re.search(r'ptype=product/product_id=(\d+)', url)
        if pm and CATALOG['products'].get(pm.group(1)):
            return f'href="{CATALOG["products"][pm.group(1)]["path"]}"'
        cm = re.search(r'ptype=results/category_id=(\d+)', url)
        if cm and CATALOG['cats'].get(cm.group(1)):
            return f'href="{CATALOG["cats"][cm.group(1)]["path"]}"'
        return m.group(0)
    return re.sub(r'href="(https://www\.dakotadigital\.com/index\.cfm/page/[^"]+)"', repl, s)


PHONE = '(800) 852-3228'

# Search index entries collected while pages are built: kind, title, sub, url, extra keywords.
SEARCH = []


def index(kind, title, url, sub='', keys=''):
    SEARCH.append({'k': kind, 't': html.unescape(title), 'u': html.unescape(url), 's': sub, 'x': keys})
TEL = 'tel:+18008523228'

# ---------- Shared chrome ----------

NAV = [
    ('index.html#finder', 'Shop by vehicle', 'finder'),
    ('automotive.html', 'Automotive', 'automotive'),
    ('motorcycle.html', 'Motorcycle', 'motorcycle'),
    ('universal.html', 'Universal gauges', 'universal'),
    ('efi.html', 'EFI and add-ons', 'efi'),
    ('support.html', 'Manuals and support', 'support'),
    ('dealers.html', 'Find a dealer', 'dealers'),
    ('careers.html', 'Careers', 'careers'),
]

FOOTER = [
    ('Shop', [('dash-builder.html', 'Dash Builder'), ('automotive.html', 'Automotive'), ('motorcycle.html', 'Motorcycle'), ('universal.html', 'Universal gauges'),
              ('efi.html', 'EFI and add-ons'), ('clearance.html', 'Clearance'), ('sitemap.html', 'Site map')]),
    ('Company', [('about.html', 'About and shop tour'), ('builds.html', 'Feature builds'), ('builds-40.html', '40 builds for 40 years'), ('media.html', 'Media coverage'),
                 ('careers.html', 'Careers'), ('contact.html', 'Contact us')]),
    ('Help', [('support.html', 'Manuals and support'), ('faq.html', 'FAQ'), ('shipping.html', 'Shipping and returns'),
              ('dealers.html', 'Find a dealer'), ('privacy.html', 'Privacy and Prop 65'), ('terms.html', 'Terms and copyright')]),
]


def header(active=''):
    items = '\n'.join(
        f'        <li><a href="{href}"{" aria-current=\"page\"" if key == active else ""}>{label}</a></li>'
        for href, label, key in NAV)
    return f'''  <header class="site-header">
    <div class="wrap header-row">
      <a class="logo" href="index.html" aria-label="Dakota Digital home">
        <img src="img/logo.png" alt="Dakota Digital" width="382" height="85">
      </a>

      <form class="search" role="search" method="post" action="{LIVE}index.cfm">
        <input type="hidden" name="ptype" value="results_w">
        <input type="hidden" name="mode" value="search">
        <label class="sr-only" for="q">Search products</label>
        <input id="q" name="keywords" type="search" placeholder="Search part # or vehicle">
        <button type="submit" aria-label="Search">
          <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>
        </button>
      </form>

      <div class="header-actions">
        <a href="{LIVE}index.cfm?ptype=account&amp;mode=user" class="icon-link" aria-label="Account">
          <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>
          <span>Account</span>
        </a>
        <a href="{LIVE}index.cfm?ptype=results_w&amp;mode=cart_list" class="icon-link" aria-label="Cart, 0 items">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 4h2l2.4 11h10.8L21 7H6.2"/><circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/></svg>
          <span>Cart</span>
          <span class="badge" aria-label="0 items">0</span>
        </a>
        <button class="menu-btn" aria-expanded="false" aria-controls="nav">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
          <span class="sr-only">Menu</span>
        </button>
      </div>
    </div>

    <nav id="nav" class="main-nav" aria-label="Main">
      <ul class="wrap">
{items}
        <li class="nav-more"><a href="contact.html"{" aria-current=\"page\"" if active == 'contact' else ""}>Contact</a></li>
      </ul>
    </nav>
  </header>'''


def footer():
    cols = '\n'.join(f'''      <nav aria-label="{title}">
        <h2>{title}</h2>
        <ul>
{chr(10).join(f'          <li><a href="{h}">{l}</a></li>' for h, l in links)}
        </ul>
      </nav>''' for title, links in FOOTER)
    return f'''  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <img src="img/logo.png" alt="Dakota Digital" width="191" height="42" loading="lazy">
        <address>
          Dakota Digital, Inc.<br>
          4510 W. 61st St. N.<br>
          Sioux Falls, SD 57107<br>
          <a href="tel:+16053326513">(605) 332-6513</a> · <a href="{TEL}">{PHONE}</a>
        </address>
      </div>
{cols}
    </div>
    <div class="wrap footer-bottom">
      <p>© Dakota Digital, Inc.</p>
      <ul class="social" aria-label="Social media">
        <li><a href="https://www.facebook.com/DakotaDigitalGauges/">Facebook</a></li>
        <li><a href="https://instagram.com/dakota_digital">Instagram</a></li>
        <li><a href="https://www.youtube.com/user/DakotaDigitalTV">YouTube</a></li>
        <li><a href="https://x.com/dakotadigital">X</a></li>
      </ul>
    </div>
  </footer>'''


MENU_JS = '''  <script src="garage.js"></script>
  <script src="search.js"></script>
  <script>
    // Mobile menu
    const menuBtn = document.querySelector('.menu-btn');
    const nav = document.getElementById('nav');
    menuBtn.addEventListener('click', () => {
      const open = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('open', !open);
    });
  </script>'''


def page(slug, title, desc, active, body, canonical, script=''):
    out = f'''<!doctype html>
<!-- Redesign prototype for experimentation. Generated by tools/build_pages.py: edit there, not here. -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
{ROBOTS_META}  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="canonical" href="{esc(canonical)}">
  <meta name="theme-color" content="#0E0F11">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

{header(active)}

  <main id="main">
{body}
  </main>

{footer()}

{MENU_JS}
{script}</body>
</html>
'''
    (SITE / f'{slug}.html').write_text(out, encoding='utf-8')
    return slug


def hero(eyebrow, h1, lede, actions='', crumbs=None):
    crumb = ''
    if crumbs:
        crumb = '      <nav class="crumbs" aria-label="Breadcrumb"><ol>' + ''.join(
            f'<li><a href="{h}">{l}</a></li>' for h, l in crumbs) + f'<li aria-current="page">{h1 if len(h1) < 40 else eyebrow}</li></ol></nav>\n'
    act = f'\n      <div class="cta-row">{actions}</div>' if actions else ''
    return f'''    <div class="wrap page-hero">
{crumb}      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>{act}
    </div>'''


def tiles(items, cls='tiles'):
    """items: (href, title, sub, external)"""
    lis = []
    for href, title, sub, *rest in items:
        lis.append(f'''        <li><a class="tile" href="{href}"><strong>{title}</strong>{f"<span>{sub}</span>" if sub else ""}<span class="tile-go" aria-hidden="true">→</span></a></li>''')
    return f'      <ul class="{cls}">\n' + '\n'.join(lis) + '\n      </ul>'


def section(title, inner, sid='', intro=''):
    hid = sid or re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    i = f'\n      <p class="section-intro">{intro}</p>' if intro else ''
    return f'''    <section class="wrap page-section" aria-labelledby="{hid}">
      <h2 id="{hid}">{title}</h2>{i}
{inner}
    </section>'''


def help_band():
    return f'''    <section class="wrap help-band" aria-label="Get help">
      <div>
        <h2>Not sure what fits?</h2>
        <p>Talk to a tech in Sioux Falls, Monday to Friday, 8am to 5pm Central.</p>
      </div>
      <div class="cta-row">
        <a class="btn btn-primary" href="{TEL}">Call {PHONE}</a>
        <a class="btn btn-ghost" href="contact.html">Send a message</a>
      </div>
    </section>'''


# ---------- Pages ----------

def automotive():
    gm = [(408, 'All Chevy and GM'), (420, '1932-57 Chevy full-size car'), (421, '1940-72 Chevy and GMC pickup / Suburban'),
          (784, '1973-98 GM trucks'), (422, 'Camaro'), (423, 'Caprice / Impala'), (424, 'Chevelle / Malibu'),
          (427, 'Corvette'), (425, 'El Camino'), (426, 'Nova'), (428, 'Monte Carlo'), (411, 'Buick'), (705, 'Cadillac'),
          (412, 'Oldsmobile'), (413, 'Pontiac'), (429, 'GM LED tail lights')]
    ford = [(409, 'All Ford'), (433, '1932-57 Ford and Mercury cars'), (434, 'Falcon and Mustang'),
            (437, '1935-66 Ford pickup and Bronco'), (830, '1967-04 Ford pickup, E-Van and Bronco'),
            (688, 'Fairlane, Galaxie and Torino'), (687, 'Lincoln'), (415, 'Mercury'), (439, 'Ford LED tail lights')]
    other = [(679, 'Mopar'), (410, 'Jeep'), (682, 'Toyota'), (842, 'Land Rover'), (414, 'Volkswagen'), (836, 'International')]
    acc = [(646, 'Expansion modules', 'efi.html'), (71, 'Air ride monitoring', ''), (337, 'Digital climate control', ''),
           (399, 'Cruise control', ''), (287, 'Speedometer calibration and interfaces', ''),
           (694, 'Tachometer calibration and interfaces', ''), (401, 'Gear position indicators', ''),
           (400, 'Remote controls and accessories', ''), (402, 'Linear actuators and controllers', ''),
           (403, 'Accessory electronics controllers', ''), (311, 'Sending units', ''), (406, 'Automotive accessories', ''),
           (351, 'Replacement parts', ''), (350, 'Gift certificate', '')]
    for c, l in gm:
        index('Vehicle', l, cat(c), 'Chevy / GM', 'chevrolet chevy gm')
    for c, l in ford:
        index('Vehicle', l, cat(c), 'Ford', 'ford')
    for c, l in other:
        index('Vehicle', l, cat(c), 'Automotive')
    for c, l, href in acc:
        index('Accessory', l, href or cat(c), 'Automotive accessories')
    t = lambda xs: tiles([(cat(c), l, '') for c, l in xs], 'tiles tiles-compact')
    body = '\n'.join([
        hero('Automotive', 'Gauges for cars and trucks',
             'Direct-fit gauge systems for classic Chevy, Ford, Mopar and more, plus universal panels for custom dashes. '
             'Start with your car, or browse by make below.',
             '<a class="btn btn-primary" href="index.html#finder">Find gauges for my car</a>'
             f'<a class="btn btn-ghost" href="{cat(712)}">New automotive products</a>'),
        section('Chevrolet and GM', t(gm)),
        section('Ford, Lincoln and Mercury', t(ford)),
        section('Mopar, Jeep and more', t(other)),
        section('No kit for your car?', tiles([
            ('universal.html', 'Universal gauges', 'Round, oval, elliptical and street rod panels for custom dashes'),
            (cat(70), 'Individual instruments', 'Single gauges to add or replace one reading'),
            (prd(214, 417), 'Custom shop', 'Send your bezel and we build gauges into it'),
        ])),
        section('Add-ons and accessories', tiles([(href or cat(c), l, '') for c, l, href in acc], 'tiles tiles-compact')),
        help_band(),
    ])
    return page('automotive', 'Automotive Gauges for Classic Cars and Trucks | Dakota Digital',
                'Direct-fit digital and analog gauge systems for Chevy, Ford, Mopar, Jeep and more, plus universal gauges and accessories.',
                'automotive', body, cat(59))


def motorcycle():
    cats = [(707, 'Harley-Davidson dressers and baggers', 'Direct plug-in MLX instruments'),
            (708, 'Harley-Davidson Road King, Softail, Deuce and Dyna', ''),
            (709, 'Harley-Davidson Sportster, Dyna, Rocker and Softail', ''),
            (516, 'Universal gauges for custom and metric bikes', ''),
            (814, 'MLX-9000 series', ''), (826, 'MLX-5000 series', ''), (518, 'MCL-5000 series', ''),
            (236, 'Individual instruments and gauges', ''), (298, 'Programmable gear indicators', ''),
            (77, 'Mounts, cups and senders', ''), (519, 'Speedometer interface', ''), (517, 'Hidden antenna', ''),
            (371, 'American Ironhorse models', ''), (381, 'Big Dog models', ''), (375, 'Victory models', ''),
            (357, 'Replacement parts', ''), (711, 'New motorcycle products', '')]
    for c, l, sub in cats:
        index('Motorcycle', l, cat(c), sub or 'Motorcycle', 'motorcycle bike harley')
    dealers = [('https://www.dragspecialties.com', 'Drag Specialties'), ('https://www.mid-usa.com/', 'Mid-USA'),
               ('http://www.rollies.com.au/', 'Rollies'), ('http://www.zodiac.nl/en/locator/index.html', 'Zodiac'),
               ('http://mcas.com.au/pw/', 'Motorcycle Accessories Supermarket')]
    body = '\n'.join([
        f'''    <div class="wrap page-hero page-hero-media">
      <div>
        <p class="eyebrow">Motorcycle</p>
        <h1>Gauges built for bikes</h1>
        <p class="lede">Plug-in MLX instruments for Harley-Davidson, plus speedos and gauge systems for custom and metric bikes.</p>
        <div class="cta-row"><a class="btn btn-primary" href="{cat(707)}">Shop Harley dressers and baggers</a><a class="btn btn-ghost" href="#dealers">Find a motorcycle dealer</a></div>
      </div>
      <img src="img/mlx.webp" alt="MLX motorcycle gauges showing speed, RPM, oil and voltage" width="730" height="183">
    </div>''',
        section('Shop by bike and series', tiles([(cat(c), l, s) for c, l, s in cats], 'tiles tiles-compact')),
        section('Built for the ride', '''      <div class="facts-grid">
        <div><h3>Weatherproof</h3><p>All Dakota Digital motorcycle gauges are designed to survive in the weather. The circuit boards are internally coated, so even if water gets into the housing they will not be damaged.</p></div>
        <div><h3>Made for vibration</h3><p>Machined aluminum housings with the circuit board mounts built into the machine work, designed with big stroker motors in mind.</p></div>
        <div><h3>Readable in the sun</h3><p>MLX instruments use high-visibility TFT displays with a high-contrast sunlight mode. Most universal gauges use teal displays with non-glare lenses.</p></div>
      </div>'''),
        section('Motorcycle dealers', f'''      <p class="section-intro">Our motorcycle products are sold through these distributors. Each has a dealer locator on its own site. Dakota Digital doesn't maintain their dealer information.</p>
      <ul class="tiles tiles-compact">
{chr(10).join(f'        <li><a class="tile" href="{h}" target="_blank" rel="noopener"><strong>{l}</strong><span class="tile-go" aria-hidden="true">↗</span></a></li>' for h, l in dealers)}
      </ul>''', sid='dealers'),
        help_band(),
    ])
    return page('motorcycle', 'Motorcycle Gauges for Harley-Davidson and Custom Bikes | Dakota Digital',
                'MLX plug-in instruments for Harley-Davidson, universal gauges for custom and metric bikes, and where to buy them.',
                'motorcycle', body, cat(60))


def universal():
    series = [(297, 'Elliptical Designer Series'), (232, 'Designer Series'), (233, 'Oval Designer Series'),
              (234, 'Round Designer Series'), (231, 'RetroTech'), (230, 'Universal street rod panels'),
              (649, 'Expansion modules')]
    items = [(1404, 'Universal rectangle, digital GRFX', 'GRFX-3200'), (1076, 'Dual 5.4" round, analog HDX', 'HDX-2014'),
             (1201, '6 gauge round, analog HDX', 'HDX-2024'), (1088, '6 gauge round, analog HDX', 'HDX-2060'),
             (1176, '7 gauge round, analog HDX', 'HDX-2070'), (845, 'Single 7" round, analog VHX', 'VHX-1019'),
             (726, 'Dual 5.4" round, analog VHX', 'VHX-1014'), (725, 'Triple round, analog VHX', 'VHX-1013'),
             (851, '5.4" round trio, analog VHX', 'VHX-1020'), (790, 'Five gauge round, analog VHX', 'VHX-1015'),
             (937, 'Five gauge round, analog VHX', 'VHX-1022'), (973, 'Six gauge round, analog VHX', 'VHX-1024'),
             (919, '5 and 6 gauge round, analog VHX', 'VHX-1050, VHX-1060'), (225, 'Single 6.75" round, digital', 'VFD3-1005'),
             (224, 'Dual 4.5" round, digital', 'VFD3-1004'), (1202, '2-1/16" round HDX clock', 'HLC-2162'),
             (1227, '2-1/16" round VHX clock', 'VLC-16-2'), (1013, '3" round VHX clock', 'VLC-16-1')]
    for c, l in series:
        index('Universal', l, cat(c), 'Universal gauges', 'universal custom')
    for p, n, sku in items:
        index('Part', n, prd(p, 69), sku, 'universal')
    rows = '\n'.join(f'          <tr><td><a href="{prd(p, 69)}">{esc(n)}</a></td><td>{s}</td></tr>' for p, n, s in items)
    body = '\n'.join([
        f'''    <div class="wrap page-hero page-hero-media">
      <div>
        <p class="eyebrow">Universal gauges</p>
        <h1>For dashes we don't make a kit for</h1>
        <p class="lede">Round, oval, elliptical and rectangle panels for custom builds, street rods and swaps, in the same GRFX, HDX, VHX and VFD3 looks as our direct-fit systems.</p>
        <div class="cta-row"><a class="btn btn-primary" href="#all">See universal systems</a><a class="btn btn-ghost" href="{prd(214, 417)}">Ask about a custom build</a></div>
      </div>
      <img src="img/camera-dash.webp" alt="Universal elliptical display with oil and water gauges around a backup camera view" width="1000" height="533">
    </div>''',
        section('Shop by shape', tiles([(cat(c), l, '') for c, l in series], 'tiles tiles-compact')),
        section('Universal systems', f'''      <div class="table-wrap">
        <table class="spec-table">
          <thead><tr><th scope="col">System</th><th scope="col">Part number</th></tr></thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>
      <p class="fine">More shapes and individual gauges on <a href="{cat(69)}">the full universal catalog</a>.</p>''', sid='all'),
        help_band(),
    ])
    return page('universal', 'Universal Gauges for Custom Dashes and Street Rods | Dakota Digital',
                'Universal round, oval, elliptical and rectangle gauge panels in GRFX, HDX, VHX and VFD3 styles for custom dashes.',
                'universal', body, cat(69))


def efi():
    mods = [(1425, 'Bridge module for EFI systems', 'BIM-EFI-1'), (752, 'OBD-II / CAN interface', 'BIM-01-2'),
            (1104, 'FAST XFI interface', 'BIM-01-2-FAST'), (1106, 'MSD Atomic EFI TBI interface', 'BIM-01-2-MSD'),
            (1328, 'J-1939 CAN interface', 'BIM-01-2-J1939'), (837, 'GPS speed and compass sender', 'GPS-50-2'),
            (1368, 'RGB lighting control', 'BIM-RGB'), (753, 'Pressure module', 'BIM-03-2'), (755, 'Temperature module', 'BIM-04-2'),
            (756, 'Voltage and current module', 'BIM-05-1'), (758, 'EGT and head temperature module', 'BIM-12-2'),
            (785, 'Wideband air/fuel module', 'BIM-13-2'), (759, 'Clock module', 'BIM-16-1'),
            (760, 'Compass with outside temperature', 'BIM-17-2'), (761, 'Quad air pressure module', 'BIM-19-2'),
            (1108, 'Tire pressure monitoring (TPMS)', 'BIM-22-3')]
    for p, n, sku in mods:
        index('Part', n, prd(p, 646), sku, 'efi bim module expansion add-on')
    body = '\n'.join([
        f'''    <div class="wrap page-hero page-hero-media">
      <div>
        <p class="eyebrow">EFI and add-ons</p>
        <h1>Up to 16 more gauges, no new holes</h1>
        <p class="lede">BIM expansion modules plug into RTX, HDX, VHX and VFD3 systems to add specialty readings, or read straight from your engine computer, without cutting the dash or hanging pods.</p>
        <div class="cta-row"><a class="btn btn-primary" href="#modules">See all modules</a><a class="btn btn-ghost" href="https://www.youtube.com/watch?v=7qyeM7vuJpE">Watch the BIM video</a></div>
      </div>
      <img src="img/efi-module.webp" alt="Dakota Digital GRAFIX interface module with OBD-II connector" width="232" height="179" class="hero-product">
    </div>''',
        '''    <div class="wrap">
      <p class="notice"><strong>Check your control box.</strong> BIM modules work with current RTX, HDX, VHX, VFD3 and RET control boxes that have a black plastic housing. Older metal-housing control boxes aren't compatible.</p>
    </div>''',
        section('Expansion modules', tiles([(prd(p, 646), n, s) for p, n, s in mods], 'tiles tiles-compact'), sid='modules'),
        help_band(),
    ])
    return page('efi', 'EFI Interfaces and BIM Expansion Modules | Dakota Digital',
                'Add up to 16 gauges or read from your EFI system with BIM modules for RTX, HDX, VHX and VFD3 instrument systems.',
                'efi', body, cat(646))


def clearance():
    body = '\n'.join([
        hero('Clearance', 'Clearance', 'Limited stock at reduced prices. Items change often, so check the live list before you decide.',
             f'<a class="btn btn-primary" href="{LIVE}index.cfm/page/ptype=results_w/mode=clearance/clearance.htm">See today\'s clearance items</a>'),
        section('On clearance now', tiles([(prd(772, -1), 'MCL Series: à la carte and accessory digital dresser gauges',
                                            'Single replacement gauges for 1996 and newer Dressers')])),
    ])
    return page('clearance', 'Clearance | Dakota Digital', 'Discontinued and limited-stock Dakota Digital gauges at reduced prices.',
                'clearance', body, f'{LIVE}index.cfm/page/ptype=results_w/mode=clearance/clearance.htm')


def support():
    sup = lambda q: f'{LIVE}index.cfm?ptype=results&amp;category_id={q}&amp;mode=cat'
    auto = [(sup(805), 'Knowledge base', 'Diagrams and how-tos'), (prd(393, 255), 'Product manuals', 'Install and setup PDFs'),
            (sup(840), 'Downloads', 'Software and files'), (sup(808).replace('?ptype=results&amp;', '?ptype=results&amp;'), 'Instrument system videos', ''),
            (sup(810), 'Instrument add-on videos', ''), (sup(809), 'Cruise control videos', ''), (sup(811), 'Vehicle accessory videos', '')]
    moto = [(sup(806), 'Knowledge base', 'Diagrams and how-tos'), (prd(392, 255), 'Product manuals', 'Install and setup PDFs'),
            (sup(812), 'Motorcycle videos', '')]
    body = '\n'.join([
        hero('Manuals and support', 'Install help from the people who build them',
             'Manuals, wiring diagrams and videos for every system. Stuck? Our tech support team is here Monday to Friday, 8am to 5pm Central.',
             f'<a class="btn btn-primary" href="{TEL}">Call tech support</a>'
             f'<a class="btn btn-ghost" href="{LIVE}index.cfm?ptype=input_form&amp;data_header_id=6">Email tech support</a>'),
        section('Automotive', tiles(auto)),
        section('Motorcycle', tiles(moto)),
        section('Repairs and warranty', f'''      <div class="facts-grid">
        <div><h3>Warranty</h3><p>Full gauge systems (part numbers starting STR, VFD, RET, VHX, HDX, RTX and GRFX) are typically covered by a lifetime warranty, for the life of the vehicle, against manufacturer's defects. Individual automotive gauges and all motorcycle products are typically covered for 24 months from purchase.</p></div>
        <div><h3>Sending a unit in</h3><p>Contact us for an RMA number first. Then send the complete unit with your name, address, phone number and a description of the problem to: Dakota Digital Inc., Attn: Repair Dept., 4510 W. 61st St North, Sioux Falls SD 57107.</p></div>
        <div><h3>Repair cost</h3><p>Warranty repairs are free. Typical non-warranty repairs start at $65, depending on the product and the problem.</p></div>
      </div>
      <p class="fine">More answers in the <a href="faq.html">FAQ</a>.</p>'''),
    ])
    return page('support', 'Manuals, Install Help and Tech Support | Dakota Digital',
                'Product manuals, knowledge base, install videos, warranty and repair info, and tech support hours for Dakota Digital gauges.',
                'support', body, cat(255))


def faq():
    faqs = load('faq')
    groups = []
    n = 0
    for g in faqs:
        for i in g['items']:
            n += 1
            i['id'] = f'q{n}'
            index('Help', i['q'], f'faq.html#{i["id"]}', g['cat'], ' '.join(i['a'])[:200])
        items = '\n'.join(f'''        <details id="{i['id']}">
          <summary>{esc(i['q'])}</summary>
{chr(10).join(f'          <p>{esc(p)}</p>' for p in i['a'])}
        </details>''' for i in g['items'])
        groups.append(section(g['cat'], f'      <div class="faq">\n{items}\n      </div>'))
    ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': i['q'], 'acceptedAnswer': {'@type': 'Answer', 'text': ' '.join(i['a'])}}
        for g in faqs for i in g['items']]}
    body = '\n'.join([hero('Help', 'Frequently asked questions',
                           'Ordering, warranty, repairs, installation and how the gauges read. Still stuck? Call us.',
                           f'<a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a>')] + groups + [help_band()])
    script = f'  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n' + '''  <script>
    // Open the question a search result or link points at
    const openHash = () => { const d = location.hash && document.querySelector(location.hash); if (d && d.tagName === 'DETAILS') d.open = true; };
    addEventListener('hashchange', openHash); openHash();
  </script>
'''
    return page('faq', 'Frequently Asked Questions | Dakota Digital',
                'Answers about ordering, warranty, repairs, installation and gauge displays for Dakota Digital instruments.',
                '', body, f'{LIVE}index.cfm?ptype=article&article_id=6', script)


def contact():
    depts = ['Sales Department', 'New Dealer Accounts', 'Custom Shop', 'Careers', 'Office / Accounting', "I'm not sure"]
    opts = '\n'.join(f'              <option>{esc(d)}</option>' for d in depts)
    body = '\n'.join([
        hero('Contact', 'Talk to the people who build them', 'Call, write or stop by. We\'re in Sioux Falls, South Dakota.'),
        f'''    <div class="wrap contact-grid">
      <div class="contact-cards">
        <a class="help-card" href="{TEL}"><h3>{PHONE}</h3><p>Toll free. Local: (605) 332-6513</p></a>
        <div class="help-card"><h3>Hours</h3><p>Monday to Friday, 8:00am to 5:00pm Central</p></div>
        <a class="help-card" href="https://maps.google.com/?q=4510+W+61st+St+N,+Sioux+Falls,+SD+57107" target="_blank" rel="noopener"><h3>Visit</h3><p>4510 W. 61st St. N.<br>Sioux Falls, SD 57107</p></a>
        <a class="help-card" href="support.html"><h3>Tech support</h3><p>Install help, manuals and repairs</p></a>
        <div class="help-card"><h3>Custom shop</h3><p>No kit for your car? Call <a href="tel:+18005934160">(800) 593-4160</a> and ask for the custom shop.</p></div>
      </div>
      <form class="quote-card" id="contact-form" novalidate>
        <div class="hp" aria-hidden="true"><label for="c-website">Website</label><input id="c-website" name="website" type="text" tabindex="-1" autocomplete="off"></div>
        <h2>Send a message</h2>
        <div class="qfield"><label for="c-dept">Send to</label><select id="c-dept">
{opts}
            </select></div>
        <div class="qfield"><label for="c-name">Your name</label><input id="c-name" autocomplete="name" required></div>
        <div class="qfield"><label for="c-email">Your email</label><input id="c-email" type="email" autocomplete="email" required></div>
        <div class="qfield"><label for="c-phone">Phone <span class="opt-label">(optional)</span></label><input id="c-phone" type="tel" autocomplete="tel"></div>
        <div class="qfield"><label for="c-msg">Message</label><textarea id="c-msg" rows="5" required></textarea></div>
        <p class="form-error" id="c-error" role="alert" hidden></p>
        <button class="btn btn-primary btn-block" type="submit">Send message</button>
        <p class="buy-note" id="c-sent" role="status" hidden></p>
      </form>
    </div>''',
    ])
    script = '''  <script>
    document.getElementById('contact-form').addEventListener('submit', async (e) => {
      e.preventDefault();
      const f = e.target, err = document.getElementById('c-error');
      if (f.querySelector('[name="website"]').value) return; // honeypot: bots fill the hidden field
      const missing = ['c-name', 'c-email', 'c-msg'].filter((id) => !f.querySelector('#' + id).value.trim());
      if (missing.length) { err.textContent = 'Please fill in your name, email and message.'; err.hidden = false; return; }
      err.hidden = true;
      const sent = document.getElementById('c-sent');
      const btn = f.querySelector('button[type="submit"]');
      const val = (id) => f.querySelector('#' + id).value;
      btn.disabled = true;
      try {
        const r = await fetch('/api/submit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ kind: 'contact', department: val('c-dept'), name: val('c-name'), email: val('c-email'), phone: val('c-phone'), message: val('c-msg') }),
        });
        const j = await r.json();
        if (!j.ok) throw new Error(j.error);
        sent.textContent = `Thanks. We got your message for ${val('c-dept')}.`;
        sent.hidden = false;
        f.querySelector('#c-msg').value = '';
      } catch (ex) {
        err.textContent = ex.message && !/fetch|JSON/i.test(ex.message) ? ex.message : 'That did not go through. Please try again or call (800) 852-3228.';
        err.hidden = false;
      }
      btn.disabled = false;
    });
  </script>
'''
    return page('contact', 'Contact Dakota Digital | Sioux Falls, SD',
                'Call (800) 852-3228, send a message, or visit Dakota Digital in Sioux Falls, South Dakota. Monday to Friday, 8am to 5pm Central.',
                'contact', body, f'{LIVE}index.cfm/page/ptype=page/page_cd=contact/contact.htm', script)


def about():
    tour = [('art_3', 'Aerial view of the Dakota Digital headquarters in Sioux Falls', 'Dual 40,000 square foot facilities in Sioux Falls.'),
            ('art_4', 'Ross Ortman in his office', 'Ross Ortman, president and founder, oversees every part of the business.'),
            ('art_9', 'Wide view of the production floor', 'Our production crew assembles and tests every product.'),
            ('fac_12383', 'Surface-mount electronics assembly line', 'Electronics are designed and built in-house.'),
            ('fac_12385', 'Circuit board under an inspection magnifier', 'Boards are inspected before they go into a gauge.'),
            ('fac_12386', 'Hands assembling small electronic parts', 'Most of manufacturing is handled in-house for tight quality control.'),
            ('art_12', 'CNC machining center', 'CNC milling centers and lathes turn out bezels and housings.'),
            ('art_63', 'Aluminum chips piled in a machining center', 'Much of the aluminum ends up on the cutting room floor.'),
            ('art_61', 'Large CNC router cutting plastic', 'A 4 by 8 foot CNC router cuts HDPE and polycarbonate.'),
            ('art_62', 'UV printer printing gauge faces', 'UV printers make high-resolution prints with specialty inks.'),
            ('art_13', 'Laser engraver for lenses', 'Lenses are engraved and cut with precision lasers.'),
            ('art_15', 'Research and development lab with vehicles', 'The R&D lab has a four-post lift, in-ground dyno and climate chamber.')]
    figs = '\n'.join(f'''        <figure><img src="img/tour/{f}.webp" alt="{esc(a)}" loading="lazy"><figcaption>{esc(c)}</figcaption></figure>''' for f, a, c in tour)
    body = '\n'.join([
        f'''    <div class="wrap page-hero page-hero-media">
      <div>
        <p class="eyebrow">About and shop tour</p>
        <h1>Built in Sioux Falls since 1986</h1>
        <p class="lede">Dakota Digital designs and builds aftermarket instrumentation for cars, trucks and motorcycles. Designing and manufacturing innovative products is our passion.</p>
        <div class="cta-row"><a class="btn btn-primary" href="#tour">Take the tour</a><a class="btn btn-ghost" href="careers.html">Work with us</a></div>
      </div>
      <img src="img/factory.webp" alt="Dakota Digital production floor from above" width="1000" height="667">
    </div>''',
        '''    <div class="wrap">
      <ul class="stats stats-wide">
        <li><strong>1986</strong><span>in business since</span></li>
        <li><strong>80,000</strong><span>square feet of electronics manufacturing</span></li>
        <li><strong>10,000s</strong><span>of units on the road</span></li>
        <li><strong>Lifetime</strong><span>warranty on full gauge systems</span></li>
      </ul>
    </div>''',
        section('A look inside', f'''      <p class="section-intro">The most important part of our business isn't pictured: our customers. Stop and see us if you're ever in the neighborhood, or visit our booth at an event.</p>
      <div class="photo-grid">
{figs}
      </div>''', sid='tour'),
        section('Keep exploring', tiles([('builds.html', 'Feature builds', 'Cars running our gauges'),
                                         ('media.html', 'Media coverage', 'What the magazines say'),
                                         ('careers.html', 'Careers', 'Join the team')])),
    ])
    return page('about', 'About Dakota Digital and Shop Tour | Sioux Falls, SD',
                'Dakota Digital has designed and built aftermarket instrumentation in Sioux Falls, South Dakota since 1986. Take a photo tour of the shop.',
                '', body, f'{LIVE}index.cfm?ptype=article&article_id=7')


def careers():
    body = '\n'.join([
        f'''    <div class="wrap page-hero page-hero-media">
      <div>
        <p class="eyebrow">Careers</p>
        <h1>Build the dash at the next car show</h1>
        <p class="lede">Join a hands-on, innovative team building high quality digital instrumentation for custom vehicles and motorcycles, in a steady, friendly, collaborative shop.</p>
        <div class="cta-row"><a class="btn btn-primary" href="https://dakotadigital.hireclick.com/jobboard/jobboard.aspx">See open positions</a><a class="btn btn-ghost" href="about.html#tour">Tour the shop</a></div>
      </div>
      <img src="img/tour/fac_12385.webp" alt="Circuit board under an inspection magnifier" width="1000" height="667">
    </div>''',
        section('Why work here', '''      <div class="facts-grid">
        <div><h3>Craftsmanship you can see</h3><p>If you take pride in craftsmanship, you'll see your work turn into striking dash clusters at car shows.</p></div>
        <div><h3>Products people love</h3><p>Lifetime warranties, good looks and real install support keep customers impressed.</p></div>
        <div><h3>Solid benefits</h3><p>Health coverage, vision, dental, PTO and 401k.</p></div>
      </div>'''),
        section('Inside the facility', '''      <div class="photo-grid photo-grid-3">
        <figure><img src="img/factory.webp" alt="Production floor from above" loading="lazy"></figure>
        <figure><img src="img/tour/fac_12383.webp" alt="Surface-mount electronics assembly line" loading="lazy"></figure>
        <figure><img src="img/tour/fac_12386.webp" alt="Hands assembling small electronic parts" loading="lazy"></figure>
      </div>'''),
        '''    <section class="wrap help-band" aria-label="Apply">
      <div><h2>Ready to apply?</h2><p>View and apply for every open position online.</p></div>
      <div class="cta-row"><a class="btn btn-primary" href="https://dakotadigital.hireclick.com/jobboard/jobboard.aspx">Apply at HireClick</a></div>
    </section>''',
    ])
    return page('careers', 'Careers at Dakota Digital | Sioux Falls, SD',
                'Work on a hands-on team building digital instrumentation for custom cars and motorcycles. Health, vision, dental, PTO and 401k.',
                'careers', body, cat(373))


def media():
    items = load('media')
    cards = '\n'.join(f'''        <li class="press">
          <img src="{m['img']}" alt="" loading="lazy">
          <div class="press-body">
            <p class="press-outlet">{esc(m['outlet'])}</p>
            <h3><a href="{esc(m['url'])}" target="_blank" rel="noopener">{esc(m['title'])}</a></h3>
            <blockquote>“{esc(m['quote'])}”</blockquote>
            {f'<p class="press-part">Part # {esc(m["part"])}</p>' if m['part'] else ''}
          </div>
        </li>''' for m in items)
    body = '\n'.join([
        hero('Media coverage', 'What the magazines say',
             f'{len(items)} installs, reviews and features from Hot Rod, Hemmings, Chevy Hardcore, Street Trucks, Super Chevy and more.'),
        f'''    <section class="wrap page-section" aria-label="Articles">
      <ul class="press-grid">
{cards}
      </ul>
    </section>''',
    ])
    return page('media', 'Media Coverage and Reviews | Dakota Digital',
                'Magazine installs, reviews and features of Dakota Digital gauges from Hot Rod, Hemmings, Chevy Hardcore, Street Trucks and more.',
                '', body, cat(804))


def fix_typos(t):
    return t.replace('Sqaurebody', 'Squarebody')


def builds():
    items = load('builds')
    for b in items:
        b['name'] = fix_typos(b['name'])
    for b in items:
        index('Build', b['name'], prd(b['id'], 643), 'Feature build')
    cards = '\n'.join(f'''        <li class="build build-sm">
          {f'<img src="{b["img"]}" alt="" loading="lazy">' if b['img'] else '<div class="build-noimg" aria-hidden="true"></div>'}
          <div class="build-body">
            <h3><a href="{prd(b['id'], 643)}">{esc(b['name'])}</a></h3>
          </div>
        </li>''' for b in items)
    body = '\n'.join([
        hero('Feature builds', 'Cars and bikes running our gauges',
             f'{len(items)} builds from shops like Ring Brothers, Kindig-It, ICON and Revology. Tap any build for the full story.',
             '<a class="btn btn-primary" href="index.html#finder">Find gauges for my car</a>'),
        f'''    <section class="wrap page-section" aria-label="All builds">
      <ul class="build-grid">
{cards}
      </ul>
    </section>''',
    ])
    return page('builds', 'Feature Builds Running Dakota Digital Gauges',
                'Custom cars, trucks and bikes from Ring Brothers, Kindig-It, ICON, Revology and more, all running Dakota Digital instruments.',
                '', body, cat(643))


def builds40():
    """40th anniversary: 40 feature builds, newest first."""
    items = [dict(b, name=fix_typos(b['name'])) for b in load('builds') if b['img']][:40]
    cards = '\n'.join(f'''        <li class="build build-sm build-num">
          <img src="{b["img"]}" alt="" loading="lazy">
          <span class="build-n" aria-hidden="true">{i:02d}</span>
          <div class="build-body">
            <h3><a href="{prd(b['id'], 643)}"><span class="sr-only">Build {i}: </span>{esc(b['name'])}</a></h3>
          </div>
        </li>''' for i, b in enumerate(items, 1))
    body = '\n'.join([
        hero('1986 to 2026', '40 builds for 40 years',
             'Dakota Digital has built gauges in Sioux Falls since 1986. To mark 40 years, here are 40 of our favorite feature builds from the shops and owners who run our instruments.',
             '<a class="btn btn-primary" href="index.html#finder">Find gauges for my car</a><a class="btn btn-ghost" href="about.html">Our story</a>'),
        f'''    <section class="wrap page-section" aria-label="The 40 builds">
      <ol class="build-grid build-forty">
{cards}
      </ol>
    </section>''',
        help_band(),
    ])
    index('Page', '40 builds for 40 years', 'builds-40.html', '40th anniversary', 'anniversary 40 years 1986 builds')
    return page('builds-40', '40 Builds for 40 Years | Dakota Digital 40th Anniversary',
                'Dakota Digital turns 40: 40 feature builds from the shops and owners who run our gauges, from 1986 to 2026.',
                '', body, f'{LIVE}index.cfm/page/ptype=results/category_id=643/mode=cat/cat643.htm')


def shipping():
    body = '\n'.join([
        hero('Help', 'Shipping and returns', 'How long it takes, how it ships, and how returns work.'),
        '''    <div class="wrap">
      <ul class="stats stats-wide">
        <li><strong>1-2 days</strong><span>in-stock items usually ship</span></li>
        <li><strong>2-3 weeks</strong><span>build time for VFD systems and individual digital gauges</span></li>
        <li><strong>8-10 weeks</strong><span>build time for many VHX, HDX, RTX and GRFX systems</span></li>
        <li><strong>30 days</strong><span>to return, with a 15% restocking fee</span></li>
      </ul>
      <p class="fine">Build times are estimates, not guarantees. If a backorder or delay comes up, we'll email you an estimated completion date.</p>
    </div>''',
        section('Shipping', '''      <div class="prose">
        <p>Orders normally ship by UPS, FedEx or, when necessary, USPS. Other carriers can be used with your own shipping account: contact us for details.</p>
        <p>Flat fee shipping is available on all web orders shipped within the continental United States (not Hawaii or Alaska). Basic shipping is UPS or FedEx Ground, at Dakota Digital's discretion.</p>
        <p>Orders may be shipped signature required, so you'll need to be available to sign at delivery. Orders ship to the credit card's billing address. For a different shipping address, call 1-800-593-4160 to order by money order, cashier's check or wire transfer. Dakota Digital may ask for a Credit Card Authorization Form before an order ships, and reserves the right to refuse shipment to an address other than the billing address.</p>
        <p>Your card may be charged the day you place the order.</p>
        <p>Address corrections after shipment cost $21 per correction. Returned, refused or undeliverable packages incur the actual shipping fees, which aren't refundable, including orders sent with special or free shipping. Reshipping costs the reshipping fee.</p>
        <p>We ship to foreign countries by UPS or FedEx. Customs and import fees are assessed by your local authorities. If they go unpaid, Dakota Digital will bill your payment method for related charges later. We can't change the invoice total or mark a shipment as a gift.</p>
        <p>Dakota Digital may change this shipping policy without notice.</p>
      </div>'''),
        section('Returns', '''      <div class="prose">
        <p>Dakota Digital offers a 30 day return policy from the purchase date. All returns are subject to a 15% restocking fee, and refunds are less the original shipping cost.</p>
        <p>We can't accept returns of custom built, damaged or special order items.</p>
      </div>'''),
        help_band(),
    ])
    return page('shipping', 'Shipping and Returns | Dakota Digital',
                'Ship times, build times for VFD, VHX, HDX, RTX and GRFX systems, shipping methods, and the 30 day return policy.',
                '', body, f'{LIVE}index.cfm/page/ptype=page/page_cd=shipping/shipping.htm')


def legal_prose(paras, headings):
    out = []
    for p in paras:
        if p in ('HERE', '.', 'HERE.'):
            continue
        if p in headings:
            out.append(f'        <h2>{esc(p.rstrip(":"))}</h2>')
        else:
            out.append(f'        <p>{esc(p)}</p>')
    return '\n'.join(out)


def privacy():
    lg = load('legal')['legal']
    heads = {'California Proposition 65', 'Liability', 'Security & Privacy:', 'Online Privacy Statement', 'App Privacy Policy:',
             'Outside Product Ideas', 'Asking for your information', 'Personal Information Privacy',
             'Order Information Privacy and Credit Card Security', 'Cookies', 'Contact Us', 'WARNING:'}
    # App privacy links lose their targets in text form; render that block by hand.
    a, b = lg.index('App Privacy Policy:'), lg.index('Outside Product Ideas')
    apps = f'''        <h2>App privacy policies</h2>
        <ul>
          <li><a href="{LIVE}index.cfm?ptype=results&amp;category_id=825&amp;mode=cat">Dakota Digital app</a></li>
          <li><a href="{LIVE}index.cfm?ptype=results&amp;category_id=714&amp;mode=cat">Automotive app</a></li>
          <li><a href="{LIVE}index.cfm?ptype=results&amp;category_id=716&amp;mode=cat">Motorcycle app</a></li>
          <li><a href="{LIVE}index.cfm?ptype=results&amp;category_id=787&amp;mode=cat">Accessories app</a></li>
        </ul>'''
    text = legal_prose(lg[:a], heads) + '\n' + apps + '\n' + legal_prose(lg[b:], heads)
    text = text.replace('<h2>WARNING</h2>\n        <p>', '<p class="notice"><strong>WARNING:</strong> ', 1)
    body = '\n'.join([
        hero('Legal', 'Privacy, Prop 65 and liability', 'How we handle your information, the California Proposition 65 warning, and product liability.'),
        f'''    <div class="wrap page-section">
      <div class="prose">
{text}
      </div>
    </div>''',
    ])
    return page('privacy', 'Privacy, Proposition 65 and Liability | Dakota Digital',
                'Dakota Digital privacy statement, California Proposition 65 warning, product liability and app privacy policies.',
                '', body, f'{LIVE}index.cfm/page/ptype=page/page_cd=legal/legal.htm')


def terms():
    t = load('legal')['terms']
    t = t[:t.index('Click Here')]
    body = '\n'.join([
        hero('Legal', 'Terms and copyright', 'The terms for using this site, and who owns its content.'),
        f'''    <div class="wrap page-section">
      <div class="prose">
        <h2>Copyright</h2>
        <p>The entire contents of this website, including words, drawings, photos and logos are property of Dakota Digital, Inc and may not be copied without written permission of Dakota Digital, Inc.</p>
{legal_prose(t, {'Terms and Conditions:'})}
      </div>
    </div>''',
    ])
    return page('terms', 'Terms and Copyright | Dakota Digital', 'Terms and conditions for using the Dakota Digital website, and copyright notice.',
                '', body, f'{LIVE}index.cfm/page/ptype=page/page_cd=copyright/copyright.htm')


def sitemap(pages):
    groups = [
        ('Shop', [('index.html', 'Home and Dash Finder'), ('dash-builder.html', 'Dash Builder'), ('automotive.html', 'Automotive'), ('motorcycle.html', 'Motorcycle'),
                  ('universal.html', 'Universal gauges'), ('efi.html', 'EFI and add-ons'), ('clearance.html', 'Clearance'),
                  ('camaro-1969-rtx.html', '1969 Camaro RTX instruments')]),
        ('Gauge series', [('shop/grfx-series.html', 'GRFX'), ('shop/rtx-series-c706.html', 'RTX'), ('shop/hdx-series-c689.html', 'HDX'),
                          ('shop/vhx-series.html', 'VHX'), ('shop/vfd3-series.html', 'VFD3')]),
        ('Help', [('support.html', 'Manuals and support'), ('faq.html', 'FAQ'), ('dealers.html', 'Find a dealer'),
                  ('shipping.html', 'Shipping and returns'), ('contact.html', 'Contact us')]),
        ('Company', [('about.html', 'About and shop tour'), ('builds.html', 'Feature builds'), ('builds-40.html', '40 builds for 40 years'), ('media.html', 'Media coverage'),
                     ('careers.html', 'Careers'), ('privacy.html', 'Privacy and Prop 65'), ('terms.html', 'Terms and copyright')]),
    ]
    cols = '\n'.join(f'''        <div>
          <h2>{t}</h2>
          <ul>{''.join(f'<li><a href="{h}">{l}</a></li>' for h, l in links)}</ul>
        </div>''' for t, links in groups)
    body = '\n'.join([
        hero('Site map', 'Site map', 'Every page on the site.'),
        f'''    <div class="wrap page-section">
      <div class="sitemap">
{cols}
      </div>
    </div>''',
    ])
    return page('sitemap', 'Site Map | Dakota Digital', 'Every page on the Dakota Digital site.', '', body,
                f'{LIVE}index.cfm/page/ptype=results_w/mode=cat_directory/home.htm')


# ---------- Dash Builder ----------

BUILDER_SERIES = ('GRFX', 'RTX', 'HDX', 'VHX', 'VFD3')


def builder_data():
    """Gauge systems for the Dash Builder, read from the built product pages (shop/*.html).

    Which series fit which car and years stays in garage.js; this only says which product page
    sells each series for a car line, with its price and real photos. Products without car fit
    data (data-cats) are left out, since the builder can't place them on a car.
    """
    prods = []
    for f in sorted((SITE / 'shop').glob('*-p*.html')):
        s = f.read_text(encoding='utf-8')
        items = re.search(r'<script type="application/json" data-b="items">(.*?)</script>', s, re.S)
        fit = re.search(r'<div class="fit" id="fit"([^>]*)>', s)
        if not items or not fit:
            continue
        main = json.loads(items.group(1))[0]
        series = next((x for x in BUILDER_SERIES if main['sku'].upper().startswith(x)), None)
        attrs = dict(re.findall(r'data-(\w+)="([^"]*)"', fit.group(1)))
        if not series or not attrs.get('cats'):
            continue
        pid = int(re.search(r'-p(\d+)\.html$', f.name).group(1))
        title = html.unescape(re.search(r'<h1>(.*?)</h1>', s).group(1))
        title = re.sub(r'^[A-Z0-9-]+:\s*', '', title)  # "GRFX-69C-CAM: 1969 Camaro GRFX Instruments"
        main_img = re.search(rf'<img src="\.\./(img/shop/prd-{pid}-[^"]+)"', s) or re.search(r'<img src="\.\./(img/shop/[^"]+)"', s)
        themes = [[html.unescape(name), src] for src, name in
                  re.findall(r'class="theme-chip" data-src="\.\./([^"]+)"[^>]*>([^<]*)<', s)]
        prods.append({
            'id': pid, 't': title, 'u': f'shop/{f.name}', 's': series, 'k': main['sku'], 'p': main['price'],
            'img': main_img.group(1) if main_img else '',
            'c': [int(x) for x in attrs['cats'].split(',')],
            'y': [int(x) for x in attrs.get('years', '').split(',') if x],
            'x': 'console' in title.lower(),
            'th': themes,
        })
    # Optional files the page uses only when they exist, so it never requests a missing one.
    dash = sorted(f.stem for f in (SITE / 'img' / 'dash').glob('*.webp'))
    models = sorted(f.stem for f in (SITE / 'models').glob('*.glb'))
    data = {'products': prods, 'dash': dash, 'models': models}
    (SITE / 'dash-builder-data.json').write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    return len(prods)


THREE_VERSION = json.loads((ROOT / 'package.json').read_text(encoding='utf-8'))['devDependencies']['three']


def dash_builder():
    three = f'js/vendor/three/{THREE_VERSION}'
    body = '''    <div class="wrap page-hero db-hero">
      <p class="eyebrow">Dash Builder</p>
      <h1>See the gauges in your car</h1>
      <p class="lede">Pick your car to see every system that fits it, in real photos of the gauges lit up.</p>
      <form class="db-picker" data-db="picker" aria-label="Your car">
        <div class="qfield">
          <label for="db-car">Car</label>
          <select id="db-car" data-db="car"><option value="">Choose your car</option></select>
        </div>
        <div class="qfield">
          <label for="db-years">Years</label>
          <select id="db-years" data-db="years" disabled><option value="">Choose years</option></select>
        </div>
      </form>
      <p class="db-note" data-db="note" hidden>3D view is coming for more cars.</p>
    </div>

    <section class="db-stage" data-db="stage" aria-label="Climb into a 1969 Camaro" hidden>
      <div class="db-sticky">
        <button type="button" class="btn btn-ghost db-skip" data-db="skip">Skip to the dash</button>
        <canvas class="db-canvas" data-db="canvas" role="img" aria-label="A red 1969 Camaro. Scroll to turn it around and climb into the driver's seat."></canvas>
        <ol class="db-rail" data-db="rail" aria-label="Steps">
          <li data-step="0">Walk around</li>
          <li data-step="1">Climb in</li>
          <li data-step="2">Your dash</li>
        </ol>
        <p class="db-caption" data-db="caption" aria-live="polite"></p>
        <div class="db-fade" data-db="fade" aria-hidden="true"><div class="db-frame"><img alt="" data-db="fade-img"></div></div>
      </div>
    </section>

    <section id="dash" class="wrap db-view" data-db="view" aria-labelledby="db-count" hidden>
      <div class="db-dash">
        <div class="db-frame" data-db="frame">
          <img class="db-bg" alt="" data-db="bg" hidden>
          <img class="db-cluster" alt="" data-db="photo">
        </div>
        <p class="db-photo-cap" data-db="photo-cap"></p>
      </div>
      <div class="db-panel">
        <h2 id="db-count" class="db-count" data-db="count" tabindex="-1"></h2>
        <div class="db-systems" role="group" aria-label="Gauge system" data-db="systems"></div>
        <label class="db-check" data-db="console-wrap" hidden><input type="checkbox" data-db="console"> My car has console gauges</label>
        <div class="qfield" data-db="version-wrap" hidden>
          <label for="db-version">Version</label>
          <select id="db-version" data-db="version"></select>
        </div>
        <h3 class="db-name" data-db="name"></h3>
        <p class="db-sku">SKU <span data-db="sku"></span></p>
        <div class="db-themes" role="group" aria-label="Lighting theme" data-db="themes"></div>
        <p class="db-no-themes" data-db="no-themes" hidden>Lighting color for this system is chosen when you order.</p>
        <p class="price" data-db="price"></p>
        <ul class="buy-proof"><li><strong>Lifetime warranty</strong> on full gauge systems. <a href="faq.html#q4">Details</a></li><li><strong>Built in Sioux Falls</strong>, South Dakota, since 1986</li></ul>
        <div class="db-actions">
          <a class="btn btn-primary" data-db="see" href="#">See this system</a>
          <a class="btn btn-ghost" href="contact.html">Ask us what fits</a>
        </div>
      </div>
    </section>

    <div class="wrap db-empty" data-db="empty">
      <p>Pick your car and years above to see every gauge system that fits it.</p>
    </div>'''
    # The import map lets the 3D module and the vendored loaders import 'three'. Nothing loads until the module asks.
    script = f'''  <script type="importmap">{{"imports":{{"three":"./{three}/three.module.min.js"}}}}</script>
  <script src="dash-builder.js" data-three="{three}"></script>
'''
    return page('dash-builder', 'Dash Builder: See the Gauges in Your Car | Dakota Digital',
                'Pick your car and years to see every Dakota Digital gauge system that fits it, in real photos of each lighting theme.',
                '', body, f'{SITE_URL}dash-builder.html', script)


# ---------- Hand-built pages: keep their header/footer in sync ----------

HAND_BUILT = {'index.html': '', 'camaro-1969-rtx.html': '', 'dealers.html': 'dealers'}


def write_robots():
    """robots.txt and the X-Robots-Tag header on Vercel follow the indexable switch."""
    if INDEXABLE:
        txt = 'User-agent: *\nAllow: /\n\nSitemap: https://www.dakotadigital.com/sitemap.xml\n'
    else:
        txt = 'User-agent: *\nDisallow: /\n'
    (SITE / 'robots.txt').write_text(txt, encoding='utf-8')
    vj = ROOT / 'vercel.json'
    conf = json.loads(vj.read_text(encoding='utf-8'))
    headers = [h for h in conf.get('headers', []) if not any(x['key'] == 'X-Robots-Tag' for x in h.get('headers', []))]
    if not INDEXABLE:
        headers.insert(0, {'source': '/(.*)', 'headers': [{'key': 'X-Robots-Tag', 'value': 'noindex, nofollow'}]})
    conf.pop('headers', None)
    if headers:  # keep headers ahead of the redirects, where they've always been
        conf = {**{k: v for k, v in conf.items() if k != 'redirects'}, 'headers': headers, **({'redirects': conf['redirects']} if 'redirects' in conf else {})}
    vj.write_text(json.dumps(conf, indent=2) + '\n', encoding='utf-8')


def sync_chrome():
    for name, active in HAND_BUILT.items():
        p = SITE / name
        s = p.read_text(encoding='utf-8')
        s = re.sub(r'  <header class="site-header">.*?</header>', lambda m: header(active), s, count=1, flags=re.S)
        s = re.sub(r'  <footer class="site-footer">.*?</footer>', lambda m: footer(), s, count=1, flags=re.S)
        s = re.sub(r'  <meta name="robots"[^>]*>\n', '', s)
        viewport = '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        s = s.replace(viewport, viewport + ROBOTS_META, 1)
        p.write_text(localize_links(s), encoding='utf-8')
    # Catalog pages share the footer. Their bodies need the crawl cache (build_catalog.py), the footer doesn't.
    shop_footer = re.sub(r'\b(href|src)="(?!https?:|#|tel:|mailto:|data:|/)([^"]*)"', lambda m: f'{m.group(1)}="../{m.group(2)}"', footer())
    for f in sorted((SITE / 'shop').glob('*.html')):
        s = f.read_text(encoding='utf-8')
        new = re.sub(r'  <footer class="site-footer">.*?</footer>', lambda m: shop_footer, s, count=1, flags=re.S)
        if new != s:
            f.write_text(new, encoding='utf-8')
    # Dash Finder: car category -> local catalog page
    df = SITE / 'dash-finder.js'
    paths = {int(k): v['path'] for k, v in CATALOG['cats'].items()}
    js = re.sub(r'const CAT_PATHS = \{.*?\};', 'const CAT_PATHS = {/*CAT_PATHS*/' + ','.join(f'{k}:{json.dumps(v)}' for k, v in sorted(paths.items())) + '};', df.read_text(encoding='utf-8'), count=1)
    df.write_text(js, encoding='utf-8')


if __name__ == '__main__':
    built = [automotive(), motorcycle(), universal(), efi(), clearance(), support(), faq(), contact(), about(),
             careers(), media(), builds(), builds40(), shipping(), privacy(), terms(), dash_builder()]
    print(f'Dash Builder: {builder_data()} products')
    built.append(sitemap(built))
    sync_chrome()
    write_robots()
    pages = [('index.html#finder', 'Find gauges for your car', 'Dash Finder', 'shop by vehicle fitment fit'),
             ('dash-builder.html', 'See the gauges in your car', 'Dash Builder', 'dash builder preview lighting theme 3d'),
             ('automotive.html', 'Automotive', 'All makes', 'car truck'), ('motorcycle.html', 'Motorcycle', 'Harley and custom bikes', 'bike'),
             ('universal.html', 'Universal gauges', 'Custom dashes', 'custom street rod'), ('efi.html', 'EFI and add-ons', 'BIM expansion modules', 'efi obd'),
             ('support.html', 'Manuals and support', 'Install help', 'manual install wiring video tech support help warranty repair'),
             ('faq.html', 'FAQ', 'Common questions', 'questions help'), ('dealers.html', 'Find a dealer', 'Installers near you', 'installer install shop dealer quote'),
             ('contact.html', 'Contact us', '(800) 852-3228', 'phone call email hours address'), ('shipping.html', 'Shipping and returns', 'Build times, returns', 'shipping return refund lead time order'),
             ('about.html', 'About and shop tour', 'Since 1986', 'company factory history'), ('careers.html', 'Careers', 'Jobs', 'job hiring work'),
             ('media.html', 'Media coverage', 'Magazine reviews', 'review press article magazine'), ('builds.html', 'Feature builds', '48 builds', 'gallery cars'),
             ('clearance.html', 'Clearance', 'Sale', 'sale discount'), ('privacy.html', 'Privacy and Prop 65', 'Legal', 'privacy legal warranty liability'),
             ('terms.html', 'Terms and copyright', 'Legal', 'terms legal'), ('sitemap.html', 'Site map', 'All pages', '')]
    for u, t, sub, k in pages:
        index('Page', t, u, sub, k)
    for sku, name, url in [('RTX-69C-CAM-X', '1969 Camaro RTX Instruments', 'camaro-1969-rtx.html'),
                           ('HDX-69C-CAM', '1969 Camaro HDX Instruments', prd(1042, 422)), ('VHX-69C-CAM', '1969 Camaro VHX Instruments', prd(722, 422)),
                           ('GRFX-69C-CAM', '1969 Camaro GRFX Instruments', prd(1397, 422)), ('VFD3-69C-CAM', '1969 Camaro VFD3 Instruments', prd(166, 422)),
                           ('ICM-69C-CAM', '1969 Camaro instrument carrier', 'camaro-1969-rtx.html'),
                           ('GSS-3000', 'Gear position sensor', 'camaro-1969-rtx.html'), ('DIM-1', 'Dimmer knob', 'camaro-1969-rtx.html')]:
        index('Part', name, url, sku, 'camaro 69')
    cat_index = CONTENT / 'catalog_index.json'
    if cat_index.exists():
        seen = {e['u'] for e in SEARCH}
        SEARCH.extend(e for e in json.loads(cat_index.read_text(encoding='utf-8')) if e['u'] not in seen)
    (SITE / 'search-index.json').write_text(json.dumps(SEARCH, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print(f'Search index: {len(SEARCH)} entries')
    print(f'Built {len(built)} pages:', ', '.join(built))

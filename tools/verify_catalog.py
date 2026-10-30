"""Compare every generated catalog page with the live page it reproduces.

Usage (repo root):  python tools/verify_catalog.py <cache_dir> [--refetch N]
--refetch N re-downloads N random live pages first and checks the cache is still current.
Writes tools/content/verify_report.json and prints a summary; exit code 1 if anything fails.
"""
import html
import json
import random
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'redesign'
cache = Path(sys.argv[1])
RAW = cache / 'raw'
catalog = json.loads((ROOT / 'tools' / 'content' / 'catalog.json').read_text(encoding='utf-8'))
images = json.loads((ROOT / 'tools' / 'content' / 'catalog_images.json').read_text(encoding='utf-8'))
LIVE = 'https://www.dakotadigital.com/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'

fails = []


def fail(kind, ident, msg):
    fails.append({'kind': kind, 'id': ident, 'msg': msg})


def content(page):
    a = page.find('class="innercontent"')
    if a < 0:
        return ''
    ends = [i for i in (page.find('<div id="bot"', a), page.find('class="footerlinkbox"', a)) if i > 0]
    b = min(ends) if ends else len(page)
    a = page.find('>', a) + 1
    return re.sub(r'<!--.*?-->', ' ', page[a:b], flags=re.S)


def text_of(s):
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)
    s = re.sub(r'<(script|style|noscript|select|button|textarea)[^>]*>.*?</\1>', ' ', s, flags=re.S | re.I)
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', s)).split())


def norm(t):
    return re.sub(r'[^a-z0-9]+', ' ', t.lower()).strip()


def words(t):
    return {w for w in norm(t).split() if len(w) > 3 and not w.isdigit()}


def local(path):
    p = SITE / path
    return p.read_text(encoding='utf-8') if p.exists() else ''


# ---- Optional freshness check against the live site ----
if '--refetch' in sys.argv:
    n = int(sys.argv[sys.argv.index('--refetch') + 1])
    sample = random.sample(sorted(RAW.glob('*.html')), min(n, len(list(RAW.glob('*.html')))))
    changed = 0
    for f in sample:
        kind, ident = f.stem[:3], f.stem[3:]
        url = (f'{LIVE}index.cfm/page/ptype=results/category_id={ident}/mode=cat/cat{ident}.htm' if kind == 'cat'
               else f'{LIVE}index.cfm/page/ptype=product/product_id={ident}/mode=prod/prd{ident}.htm')
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=30) as r:
                fresh = r.read().decode('utf-8', errors='replace')
        except Exception as e:  # noqa: BLE001
            fail('refetch', f.stem, f'could not fetch: {e}')
            continue
        time.sleep(0.4)
        # The live breadcrumb depends on which category URL a product is opened through, so leave it out.
        crumb = r'<div align="left" class="smallbody">.*?</div>'
        now = words(text_of(re.sub(crumb, '', content(fresh), count=1, flags=re.S)))
        then = words(text_of(re.sub(crumb, '', content(f.read_text(encoding='utf-8', errors='replace')), count=1, flags=re.S)))
        if now != then:
            changed += 1
            fail('refetch', f.stem, 'live page changed since crawl')
    print(f'Freshness: {len(sample) - changed}/{len(sample)} sampled live pages unchanged since the crawl')

# ---- Categories ----
for cid, c in catalog['cats'].items():
    page = local(c['path'])
    if not page:
        fail('category', cid, 'page missing')
        continue
    live = (RAW / f'cat{cid}.html').read_text(encoding='utf-8', errors='replace')
    frag = content(live)
    for m in re.finditer(r'<div class="thm(prd|subcat)float">.*?href="([^"]+)"', frag, re.S):
        kind, url = m.group(1), m.group(2)
        ident = re.search(r'(?:product|category)_id[=/](\d+)', url)
        if not ident:
            continue
        ident = ident.group(1)
        target = (catalog['products'] if kind == 'prd' else catalog['cats']).get(ident)
        href = target['path'].split('/', 1)[1] if target else None
        if not href or f'href="{href}"' not in page and f'href="../{target["path"]}"' not in page:
            fail('category', cid, f'missing link to {kind} {ident}')
    t = re.search(r'<title>(.*?)</title>', live, re.S)
    if t and norm(text_of(t.group(1))) not in norm(text_of(page)):
        fail('category', cid, f'title "{text_of(t.group(1))}" not on page')
    lw = words(text_of(re.sub(r'<div id="thm(?:prd|subcat)parent".*', '', frag, flags=re.S)))
    lw -= {'click', 'image', 'text', 'view', 'details'}  # the old "Click image or text to view details" hint, dropped on purpose
    pw = words(text_of(page))
    if lw and len(lw & pw) / len(lw) < 0.9:
        fail('category', cid, f'only {len(lw & pw)}/{len(lw)} intro words carried over: missing {sorted(lw - pw)[:8]}')

# ---- Products ----
for pid, p in catalog['products'].items():
    page = local(p['path'])
    if not page:
        fail('product', pid, 'page missing')
        continue
    raw_file = RAW / f'prd{pid}.html'
    if not raw_file.exists():
        fail('product', pid, 'live page not crawled')
        continue
    live = raw_file.read_text(encoding='utf-8', errors='replace')
    frag = content(live)
    text = text_of(page)
    h1 = re.search(r'<h1[^>]*black_headline[^>]*>(.*?)</h1>', live, re.S)
    if h1 and norm(text_of(h1.group(1))) not in norm(text):
        fail('product', pid, f'title "{text_of(h1.group(1))}" not on page')
    for sku in p['skus']:
        if sku and sku not in page:
            fail('product', pid, f'SKU {sku} not on page')
    for price in p['prices']:
        if price and f'{price:,.2f}' not in page and str(price) not in page:
            fail('product', pid, f'price {price} not on page')
    for title, opts in p['steps']:
        for o in opts:
            if html.escape(o, quote=False) not in page and o not in page and json.dumps(o)[1:-1] not in page:
                fail('product', pid, f'option "{o}" ({title}) not on page')
    live_tabs = re.findall(r'<li[^>]*rel="view\d+"[^>]*>(.*?)</li>', frag)
    if len(live_tabs) != len(p['tabs']):
        empty = len(live_tabs) - len(p['tabs'])
        fail('product', pid, f'{len(live_tabs)} tabs live, {len(p["tabs"])} here ({empty} empty or missing)')
    for pdf in set(re.findall(r'href="([^"]+\.pdf)"', frag, re.I)):
        name = pdf.rsplit('/', 1)[-1]
        if name not in page:
            fail('product', pid, f'manual {name} not linked')
    for rel in re.findall(r'<div class="thmprdfloat">.*?product_id[=/](\d+)', frag, re.S):
        tgt = catalog['products'].get(rel)
        if tgt and tgt['path'].split('/', 1)[1] not in page:
            fail('product', pid, f'related product {rel} not linked')
    # The old inline buy form and its "notify me" pop-up are replaced by our buy box (checked above).
    # Breadcrumbs are compared separately below (a product listed in several categories may show a different one).
    frag_text = re.sub(r'<form action="p_sql_cart\.cfm".*?</form>|<div id="myModal\d+" class="modal">.*?</form>|<div align="left" class="smallbody">.*?</div>', '', frag, count=0, flags=re.S)
    home = catalog['cats'].get(str(p['cat']))
    listed_anywhere = any(int(pid) in c['products'] for c in catalog['cats'].values())
    if home and listed_anywhere and int(pid) not in home['products']:
        fail('product', pid, f'breadcrumb category {p["cat"]} does not list this product')
    lw = words(text_of(re.sub(r'<div id="thmprdparent".*|<section class="product_divider">.*?</section>', '', frag_text, flags=re.S)))
    lw -= {'your', 'browser', 'must', 'support', 'iframes', 'purchase', 'this', 'product', 'click', 'image', 'text', 'view', 'details'}
    pw = words(text)
    if lw and len(lw & pw) / len(lw) < 0.9:
        fail('product', pid, f'only {len(lw & pw)}/{len(lw)} words carried over: missing {sorted(lw - pw)[:8]}')

# ---- Images ----
missing_imgs = [u for u, path in images.items() if not (SITE / path).exists()]
for u in missing_imgs:
    fail('image', u, 'not downloaded')

report = {'categories': len(catalog['cats']), 'products': len(catalog['products']), 'images': len(images), 'failures': fails}
(ROOT / 'tools' / 'content' / 'verify_report.json').write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding='utf-8')
by = {}
for f in fails:
    key = f['kind'] + ': ' + re.sub(r'\d[\d,.]*|"[^"]*"|\{[^}]*\}|\[[^\]]*\]', '#', f['msg'])
    by[key] = by.get(key, 0) + 1
print(f'Checked {len(catalog["cats"])} categories, {len(catalog["products"])} products, {len(images)} images: {len(fails)} problems')
for k, v in sorted(by.items(), key=lambda x: -x[1])[:15]:
    print(f'  {v:5}  {k}')
sys.exit(1 if fails else 0)

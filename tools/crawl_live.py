"""Polite crawl of dakotadigital.com categories and products for the redesign.

Usage:  python tools/crawl_live.py <cache_dir>
Fetches category and product pages one at a time with a delay, honors robots.txt
(never fetches /p_item.cfm, /p_product.cfm or /addresses.cfm), caches raw HTML in
<cache_dir>/raw, and writes <cache_dir>/graph.json with the category tree and product ids.
"""
import json
import re
import sys
import time
import urllib.request
import urllib.robotparser
from pathlib import Path

LIVE = 'https://www.dakotadigital.com/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
DELAY = 0.35
SEEDS = [59, 60, 69, 70, 646, 643, 804, 255, 373, 712, 711, 805, 806, 808, 809, 810, 811, 812, 840, 825, 714, 716, 787]

cache = Path(sys.argv[1])
raw = cache / 'raw'
raw.mkdir(parents=True, exist_ok=True)
rp = urllib.robotparser.RobotFileParser(LIVE + 'robots.txt')
rp.read()


def cat_url(c):
    return f'{LIVE}index.cfm/page/ptype=results/category_id={c}/mode=cat/cat{c}.htm'


def prd_url(p, c):
    return f'{LIVE}index.cfm/page/ptype=product/product_id={p}/category_id={c}/mode=prod/prd{p}.htm'


def fetch(url, path):
    if path.exists() and path.stat().st_size > 2000:
        return path.read_text(encoding='utf-8', errors='replace')
    if not rp.can_fetch('*', url):
        return ''
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                html = r.read().decode('utf-8', errors='replace')
            path.write_text(html, encoding='utf-8')
            time.sleep(DELAY)
            return html
        except Exception as e:  # noqa: BLE001
            time.sleep(2 + attempt * 3)
            err = e
    print('FAILED', url, err, flush=True)
    return ''


def content(html):
    a = html.find('class="innercontent"')
    b = html.find('class="footerlinkbox"', a)
    return html[a:b] if a >= 0 else html


cats, products, edges = {}, {}, {}
queue = list(SEEDS)
seen = set(queue)
while queue:
    c = queue.pop(0)
    html = fetch(cat_url(c), raw / f'cat{c}.html')
    if not html:
        continue
    body = content(html)
    t = re.search(r'<title>(.*?)</title>', html, re.S)
    subs = []
    for m in re.finditer(r'category_id[=/](\d+)', body):
        s = int(m.group(1))
        if s not in subs and s != c:
            subs.append(s)
    prods = []
    for m in re.finditer(r'product_id[=/](\d+)', body):
        p = int(m.group(1))
        if p not in prods:
            prods.append(p)
            products.setdefault(p, c)
    cats[c] = {'title': ' '.join(t.group(1).split()) if t else '', 'subs': subs, 'products': prods}
    for s in subs:
        if s not in seen:
            seen.add(s)
            queue.append(s)
    print(f'cat {c}: {len(subs)} subs, {len(prods)} products | queue {len(queue)} | cats {len(cats)} | products {len(products)}', flush=True)

(cache / 'graph.json').write_text(json.dumps({'cats': cats, 'products': products}), encoding='utf-8')
print('CATEGORIES DONE', len(cats), 'categories', len(products), 'products', flush=True)

done = 0
for p, c in products.items():
    fetch(prd_url(p, c), raw / f'prd{p}.html')
    done += 1
    if done % 25 == 0:
        print(f'products {done}/{len(products)}', flush=True)
print('ALL DONE', flush=True)

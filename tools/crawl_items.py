"""Fetch price/SKU/option steps for every product item (authorized by the site owner).

Usage:  python tools/crawl_items.py <cache_dir>
Reads cached product pages from <cache_dir>/raw, finds each item's p_item.cfm frame and
fetches option steps (proc_row=1, 2, ...) until a step has no more choices. One request at
a time with a delay; cached in <cache_dir>/items.
"""
import re
import sys
import time
import urllib.request
from pathlib import Path

LIVE = 'https://www.dakotadigital.com/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
DELAY = 0.4
MAX_ROWS = 8

cache = Path(sys.argv[1])
raw, out = cache / 'raw', cache / 'items'
out.mkdir(parents=True, exist_ok=True)


def get(url):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                html = r.read().decode('utf-8', errors='replace')
            time.sleep(DELAY)
            return html
        except Exception as e:  # noqa: BLE001
            time.sleep(2 + attempt * 3)
            err = e
    print('FAILED', url, err, flush=True)
    return ''


files = sorted(raw.glob('prd*.html'))
total = 0
for n, f in enumerate(files, 1):
    pid = f.stem[3:]
    html = f.read_text(encoding='utf-8', errors='replace')
    for item in dict.fromkeys(re.findall(r'p_item\.cfm\?product_id=\d+&(?:amp;)?ptype=product&(?:amp;)?item_id=(\d+)', html)):
        for row in range(1, MAX_ROWS + 1):
            path = out / f'{pid}_{item}_{row}.html'
            if path.exists() and path.stat().st_size > 500:
                page = path.read_text(encoding='utf-8', errors='replace')
            else:
                page = get(f'{LIVE}p_item.cfm?product_id={pid}&ptype=product&item_id={item}&proc_row={row}&vBuy_yn=N&bg=FFFFFF')
                if not page:
                    break
                path.write_text(page, encoding='utf-8')
                total += 1
            # A step with no choices (just quantity) is the last one.
            if not re.search(r'<select|type="checkbox"|type="radio"', page, re.I):
                break
    if n % 25 == 0:
        print(f'products {n}/{len(files)} | requests {total}', flush=True)
print('ITEMS DONE', total, flush=True)

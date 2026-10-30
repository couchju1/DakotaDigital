"""Download and convert every catalog image listed in tools/content/catalog_images.json.

Usage (repo root):  python tools/fetch_images.py <cache_dir>
Originals are cached in <cache_dir>/img; WebP copies (max 1000px wide) go to redesign/<local path>.
One request at a time with a short delay; existing files are skipped.
"""
import hashlib
import io
import json
import sys
import time
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
cache = Path(sys.argv[1]) / 'img'
cache.mkdir(parents=True, exist_ok=True)
images = json.loads((ROOT / 'tools' / 'content' / 'catalog_images.json').read_text(encoding='utf-8'))

done = failed = skipped = 0
missing = []
for n, (url, local) in enumerate(images.items(), 1):
    out = ROOT / 'redesign' / local
    if out.exists():
        skipped += 1
        continue
    orig = cache / hashlib.md5(url.encode()).hexdigest()
    try:
        if not orig.exists():
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                orig.write_bytes(r.read())
            time.sleep(0.2)
        im = Image.open(io.BytesIO(orig.read_bytes()))
        im = im.convert('RGBA') if im.mode in ('P', 'LA', 'RGBA') else im.convert('RGB')
        if im.mode == 'RGBA':  # flatten transparency onto white so product shots look right
            bg = Image.new('RGB', im.size, 'white')
            bg.paste(im, mask=im.split()[3])
            im = bg
        im.thumbnail((1000, 1000))
        out.parent.mkdir(parents=True, exist_ok=True)
        im.save(out, 'WEBP', quality=72, method=5)
        done += 1
    except Exception as e:  # noqa: BLE001
        failed += 1
        missing.append([url, str(e)[:80]])
    if n % 100 == 0:
        print(f'{n}/{len(images)} | new {done} | skipped {skipped} | failed {failed}', flush=True)

(ROOT / 'tools' / 'content' / 'catalog_images_missing.json').write_text(json.dumps(missing, indent=0), encoding='utf-8')
print(f'IMAGES DONE new {done} skipped {skipped} failed {failed}', flush=True)

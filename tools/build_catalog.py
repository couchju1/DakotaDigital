"""Build every category and product page of the live catalog into redesign/shop/.

Usage (repo root):  python tools/build_catalog.py <cache_dir>
<cache_dir> is what tools/crawl_live.py and tools/crawl_items.py filled: raw/*.html, items/*.html,
graph.json. Images listed in tools/content/catalog_images.json (written here) are downloaded and
converted by tools/fetch_images.py into redesign/img/shop/.

Outputs:
  redesign/shop/<slug>-c<id>.html   one per category
  redesign/shop/<slug>-p<id>.html   one per product
  tools/content/catalog.json        parsed catalog (titles, SKUs, prices, options) used by the
                                    search index, build_pages.py links and verify_catalog.py
"""
import hashlib
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_pages as bp  # noqa: E402  (shared header, footer, page shell)

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'redesign'
SHOP = SITE / 'shop'
CONTENT = ROOT / 'tools' / 'content'
LIVE = 'https://www.dakotadigital.com/'

cache = Path(sys.argv[1])
RAW, ITEMS = cache / 'raw', cache / 'items'
graph = json.loads((cache / 'graph.json').read_text(encoding='utf-8'))
CATS = {int(k): v for k, v in graph['cats'].items()}
PRODS = {int(k): int(v) for k, v in graph['products'].items()}

# Images: remote URL -> local path (filled while building, saved for fetch_images.py)
img_map_path = CONTENT / 'catalog_images.json'
IMAGES = json.loads(img_map_path.read_text(encoding='utf-8')) if img_map_path.exists() else {}
_missing = CONTENT / 'catalog_images_missing.json'
BROKEN = {u for u, _ in json.loads(_missing.read_text(encoding='utf-8'))} if _missing.exists() else set()
for u in BROKEN:
    IMAGES.pop(u, None)


def slugify(s):
    s = html.unescape(s).lower().replace('&', ' and ')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:60] or 'item'


def raw(name):
    p = RAW / f'{name}.html'
    return p.read_text(encoding='utf-8', errors='replace') if p.exists() else ''


def main_content(page):
    a = page.find('class="innercontent"')
    if a < 0:
        return ''
    ends = [i for i in (page.find('<div id="bot"', a), page.find('class="footerlinkbox"', a)) if i > 0]
    b = min(ends) if ends else len(page)
    a = page.find('>', a) + 1
    return page[a:b]


# Spelling mistakes in the live data, fixed in titles and URLs (old URLs get a redirect).
TYPOS = {'Sqaurebody': 'Squarebody'}


def clean_title(t):
    t = ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', t)).split()).replace('- ', '-').replace(' /', '/')
    for bad, good in TYPOS.items():
        t = t.replace(bad, good)
    return t


SITE_URL = bp.SITE_URL
REWRITES = {k: v for k, v in json.loads((CONTENT / 'rewrites.json').read_text(encoding='utf-8')).items() if not k.startswith('_')}
_norm = lambda t: ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', t)).split())


def modernize(s):
    """Swap the old site's repeated copy for the rewrites and drop its navigation instructions."""
    def para(m):
        new = REWRITES.get(_norm(m.group(1)))
        return f'<p>{html.escape(new, quote=False)}</p>' if new else m.group(0)
    s = re.sub(r'<p>(.*?)</p>', para, s, flags=re.S)
    s = re.sub(r'\s*Click the tabs below[^.!<]*[.!]', '', s, flags=re.I)
    s = re.sub(r'\s*Click Here to See More\.?', '', s, flags=re.I)

    def link_text(m):
        href, attrs, text = m.group(1), m.group(2), _norm(m.group(3))
        if re.fullmatch(r'(click here( for more information)?|more info(rmation)?|click here to see more)[.!]?', text, re.I):
            target = TITLE_BY_PATH.get(href)
            label = f'More about the {target}' if target else 'Learn more'
            return f'<a href="{href}"{attrs}>{html.escape(label)}</a>'
        return m.group(0)
    return re.sub(r'<a href="([^"]+)"([^>]*)>(.*?)</a>', link_text, s, flags=re.S)


# ---------- First pass: names and paths for every page ----------

CAT_INFO, PRD_INFO, REDIRECTS = {}, {}, {}
for c, info in CATS.items():
    page = raw(f'cat{c}')
    t = re.search(r'<title>(.*?)</title>', page, re.S)
    title = clean_title(t.group(1)) if t else info.get('title') or f'Category {c}'
    CAT_INFO[c] = {'title': title, 'path': f'shop/{slugify(title)}-c{c}.html'}
for p, c in PRODS.items():
    page = raw(f'prd{p}')
    h = re.search(r'<h1[^>]*class="black_headline"[^>]*>(.*?)</h1>', page, re.S)
    title = clean_title(h.group(1)) if h else ''
    if not title:  # discontinued: the live page is empty
        title = f'Product {p} (no longer listed)'
    PRD_INFO[p] = {'title': title, 'cat': c, 'path': f'shop/{slugify(title)}-p{p}.html'}
    raw_title = clean_title(h.group(1)) if h else ''
    for bad, good in TYPOS.items():  # remember the old, misspelled URL so it can redirect
        if good in raw_title and h and bad in ' '.join(html.unescape(h.group(1)).split()):
            REDIRECTS[f'/shop/{slugify(raw_title.replace(good, bad))}-p{p}.html'] = '/' + PRD_INFO[p]['path']
TITLE_BY_PATH = {i['path']: i['title'] for i in PRD_INFO.values()}


# Parent of each category, read from its own breadcrumb (the last link is the parent).
PARENT = {}
for c in CATS:
    m = re.search(r'<div align="left" class="smallbody">(.*?)</div>', main_content(raw(f'cat{c}')), re.S)
    ids = [int(x) for x in re.findall(r'category_id[=/](\d+)', m.group(1))] if m else []
    if ids and ids[-1] != c:
        PARENT[c] = ids[-1]


def chain(c):
    out, seen = [], set()
    while c in PARENT and c not in seen:
        seen.add(c)
        c = PARENT[c]
        out.insert(0, c)
    return out


# Showcase categories link to products but aren't where a product "lives".
SHOWCASE = {804, 643, 712, 711, 255, 697}
LISTED_IN = {}
for c, info in CATS.items():
    for p in info['products']:
        LISTED_IN.setdefault(p, []).append(c)


def home_cat(p):
    grid = [c for c in GRID_LISTED.get(p, []) if c not in SHOWCASE]
    cands = grid or [c for c in LISTED_IN.get(p, []) if c not in SHOWCASE] or GRID_LISTED.get(p) or LISTED_IN.get(p, []) or [PRODS[p]]
    return max(cands, key=lambda c: (len(chain(c)), -cands.index(c)))




def local_link(url):
    """Map a live-site URL to our page, or return an absolute live URL."""
    u = html.unescape(url).strip()
    if u.startswith(('mailto:', 'tel:', '#', 'javascript:')):
        return u if not u.startswith('javascript:') else ''
    m = re.search(r'ptype[=/]product[&/](?:amp;)?product_id[=/](\d+)', u) or re.search(r'product_id[=/](\d+)', u)
    if m and 'p_item' not in u and int(m.group(1)) in PRD_INFO:
        return PRD_INFO[int(m.group(1))]['path']
    m = re.search(r'category_id[=/](\d+)', u)
    if m and 'ptype=product' not in u and int(m.group(1)) in CAT_INFO:
        return CAT_INFO[int(m.group(1))]['path']
    if re.search(r'page_cd[=/]contact', u):
        return 'contact.html'
    if re.search(r'page_cd[=/]shipping', u):
        return 'shipping.html'
    if re.search(r'article_id[=/]12\b', u):
        return 'dealers.html'
    if re.search(r'article_id[=/]6\b', u):
        return 'faq.html'
    if re.search(r'article_id[=/]7\b', u):
        return 'about.html'
    if u.startswith('http://www.dakotadigital.com'):
        u = 'https://' + u[7:]
    if u.startswith('//'):
        return 'https:' + u
    if not re.match(r'https?:', u):
        return LIVE + u.lstrip('/')
    return u


def local_img(src):
    """Register a remote image for download and return its local path."""
    u = html.unescape(src).strip()
    if not u or 'spacer.gif' in u or u.startswith('data:'):
        return ''
    if not re.match(r'https?:', u):
        u = LIVE + u.lstrip('/')
    u = re.sub(r'^http://', 'https://', u).split('?')[0]
    if 'etechglobal.com' in u and 'v12_images' in u:
        return ''
    if u in BROKEN:  # 404 on the live site too
        return ''
    if u not in IMAGES:
        stem = re.sub(r'[^a-z0-9]+', '-', u.rsplit('/', 1)[-1].rsplit('.', 1)[0].lower())[:40]
        IMAGES[u] = f'img/shop/{stem}-{hashlib.md5(u.encode()).hexdigest()[:6]}.webp'
    return IMAGES[u]


# ---------- Sanitizer: live content HTML -> clean, styled-by-us HTML ----------

KEEP = {'p', 'br', 'h2', 'h3', 'h4', 'strong', 'b', 'em', 'i', 'u', 'ul', 'ol', 'li', 'table', 'thead', 'tbody',
        'tr', 'td', 'th', 'a', 'img', 'sup', 'sub', 'hr', 'blockquote', 'figure', 'figcaption', 'iframe'}
RENAME = {'h1': 'h3', 'h5': 'h4', 'h6': 'h4', 'b': 'strong', 'i': 'em'}
VOID = {'br', 'img', 'hr'}
DROP_WITH_CONTENT = {'script', 'style', 'noscript', 'select', 'button', 'textarea', 'object', 'svg'}
DROP_VOID = {'input', 'embed', 'source', 'link', 'meta', 'area', 'col', 'param', 'wbr'}


class Sanitizer(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.stack, self.skip = [], [], 0

    def handle_starttag(self, tag, attrs):
        if self.skip:
            if tag in DROP_WITH_CONTENT:
                self.skip += 1
            return
        if tag in DROP_WITH_CONTENT:
            self.skip = 1
            return
        if tag in DROP_VOID:
            return
        tag = RENAME.get(tag, tag)
        a = dict(attrs)
        if tag not in KEEP:
            if tag in ('div', 'section', 'center') and tag not in VOID:
                self.stack.append(('div-break', tag))
                self.out.append('\n')
            else:
                self.stack.append(('unwrap', tag))
            return
        attr = ''
        if tag == 'a':
            orig = a.get('href') or ''
            # Full-size photo links open our local copy instead of the old site
            href = local_img(orig) if re.search(r'\.(jpe?g|png|gif|webp)$', orig.split('?')[0], re.I) else local_link(orig)
            if not href:
                self.stack.append(('unwrap', tag))
                return
            ext = href.startswith('http')
            attr = f' href="{html.escape(href)}"' + (' target="_blank" rel="noopener"' if ext and 'dakotadigital.com' not in href else '')
        elif tag == 'img':
            src = local_img(a.get('src') or a.get('data-src') or '')
            if not src:
                return
            alt = a.get('alt') or a.get('title') or ''
            attr = f' src="{src}" alt="{html.escape(alt)}" loading="lazy"'
        elif tag == 'iframe':
            src = a.get('src') or ''
            if 'youtube' not in src and 'vimeo' not in src:
                return  # drop non-video embeds (widgets, price frames); their text is fallback only
            src = 'https:' + src if src.startswith('//') else src
            attr = f' src="{html.escape(src)}" title="Video" loading="lazy" allowfullscreen'
        elif tag in ('td', 'th'):
            for k in ('colspan', 'rowspan'):
                if a.get(k):
                    attr += f' {k}="{html.escape(a[k])}"'
        self.out.append(f'<{tag}{attr}>')
        if tag not in VOID:
            self.stack.append(('keep', tag))

    def handle_endtag(self, tag):
        if self.skip:
            if tag in DROP_WITH_CONTENT:
                self.skip -= 1
            return
        tag = RENAME.get(tag, tag)
        for i in range(len(self.stack) - 1, -1, -1):
            kind, t = self.stack[i]
            if t == tag:
                for kind2, t2 in reversed(self.stack[i:]):
                    if kind2 == 'keep':
                        self.out.append(f'</{t2}>')
                    elif kind2 == 'div-break':
                        self.out.append('\n')
                del self.stack[i:]
                return

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and RENAME.get(tag, tag) in KEEP and tag != 'img':
            self.handle_endtag(tag)

    def handle_data(self, data):
        if not self.skip:
            self.out.append(html.escape(data, quote=False))

    def result(self):
        for kind, t in reversed(self.stack):
            if kind == 'keep':
                self.out.append(f'</{t}>')
        s = ''.join(self.out)
        s = re.sub(r'(<br>\s*){3,}', '<br><br>', s)
        s = re.sub(r'<(p|li|td|strong|em|u|h[234]|span)>\s*(&nbsp;|\xa0|\s)*</\1>', '', s)
        s = re.sub(r'<p>\s*(<br>\s*)+', '<p>', s)
        s = re.sub(r'\n\s*\n+', '\n', s)
        return s.strip()


def sanitize(fragment):
    # Remove scripts, styles and form controls as matched pairs first; an unclosed one in the
    # live markup would otherwise make the parser skip everything after it.
    fragment = re.sub(r'<(script|style|noscript|select|button|textarea|object|svg)\b[^>]*>.*?</\1\s*>', '', fragment, flags=re.S | re.I)
    fragment = re.sub(r'</?(script|style|noscript|select|button|textarea|object|svg)\b[^>]*>', '', fragment, flags=re.I)
    p = Sanitizer()
    p.feed(fragment)
    p.close()
    return p.result()


def galleries(fragment):
    """Replace jssor sliders with a simple gallery of their images."""
    def repl(m):
        block = m.group(0)
        imgs = re.findall(r'<img[^>]*data-u="image"[^>]*>', block) or re.findall(r'<img[^>]*>', block)
        out = []
        for tag in imgs:
            src = re.search(r'src="([^"]+)"', tag)
            alt = re.search(r'(?:title|alt)="([^"]*)"', tag)
            if src:
                out.append(f'<img src="{src.group(1)}" alt="{alt.group(1) if alt else ""}">')
        return '<figure class="gallery">' + ''.join(out) + '</figure>'
    # The slider markup ends with its bullet/arrow navigator; cut through the closing script.
    return re.sub(r'<div[^>]*id="jssor_\d+".*?(?=<script|<div class="pagecontent|<h3 class="[^"]*tab_drawer_heading|$)', repl, fragment, flags=re.S)


def cut_block(fragment, start_pat):
    """Remove a balanced <div ...> block that starts at start_pat; return (fragment, block)."""
    m = re.search(start_pat, fragment)
    if not m:
        return fragment, ''
    i, depth = m.start(), 0
    for t in re.finditer(r'<(/?)div\b[^>]*>', fragment[i:]):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            j = i + t.end()
            return fragment[:i] + fragment[j:], fragment[i:j]
    return fragment[:i], fragment[i:]


def grid_items(block):
    """Thumbnail grid (products or subcategories) -> list of (id, kind, name, thumb, skus)."""
    items = []
    for cell in re.findall(r'<div class="thm(?:prd|subcat)float">(.*?)</table>\s*</div>', block, re.S):
        link = re.search(r'href="([^"]+)"', cell)
        name = re.search(r'class="Category_Nav"[^>]*>(.*?)</a>', cell, re.S)
        thumb = re.search(r"background:url\(([^)]+)\)", cell)
        sku = re.search(r'font-style:italic;">(.*?)</span>', cell, re.S)
        if not link:
            continue
        u = link.group(1)
        m = re.search(r'product_id[=/](\d+)', u)
        kind, iid = ('p', int(m.group(1))) if m else ('c', int(re.search(r'category_id[=/](\d+)', u).group(1)) if re.search(r'category_id[=/](\d+)', u) else -1)
        items.append({'id': iid, 'kind': kind, 'name': clean_title(name.group(1)) if name else '',
                      'thumb': thumb.group(1).strip('\'"') if thumb else '', 'skus': clean_title(sku.group(1)) if sku else ''})
    return items


def breadcrumb(fragment):
    m = re.search(r'<div align="left" class="smallbody">(.*?)</div>', fragment, re.S)
    crumbs = []
    if m:
        for a in re.finditer(r'<a href="([^"]+)"[^>]*>(.*?)</a>', m.group(1), re.S):
            crumbs.append((local_link(a.group(1)), clean_title(a.group(2))))
    return crumbs


# ---------- Items: price, SKU and option steps ----------

def parse_steps(page):
    """Option select lists inside one buy form or price frame."""
    steps = []
    for sel in re.finditer(r'<div[^>]*class="itemoptiontitle[^"]*"[^>]*>(.*?)</div>\s*<select[^>]*>(.*?)</select>', page, re.S):
        opts = []
        for o in re.finditer(r'<option[^>]*value="([^"]*)"[^>]*>(.*?)</option>', sel.group(2), re.S):
            text = clean_title(o.group(2))
            if not text or text.lower().startswith(('please select', 'select')):
                continue
            delta = re.search(r'([+-])\s*\$\s*([\d,]+(?:\.\d\d)?)', text)
            d = (1 if delta.group(1) == '+' else -1) * float(delta.group(2).replace(',', '')) if delta else 0
            opts.append({'v': o.group(1), 't': text, 'd': d})
        if opts:
            steps.append({'type': 'select', 'title': clean_title(sel.group(1)), 'options': opts})
    return steps


def inline_items(page):
    """Simple products put their buy form right in the page instead of a price frame."""
    items = []
    for form in re.findall(r'<form action="p_sql_cart\.cfm"[^>]*>(.*?)</form>', page, re.S):
        g = lambda n: (re.search(rf'name="{n}" value="([^"]*)"', form) or [None, ''])[1]
        if not g('item_id'):
            continue
        items.append({'id': g('item_id'), 'sku': html.unescape(g('item_cd')), 'name': clean_title(g('short_desc')),
                      'price': float(g('base_price') or 0), 'label': g('price_label') or 'Price', 'steps': parse_steps(form)})
    return items


def strip_inline_buy(frag):
    """Remove inline buy forms and their 'notify me' pop-ups from page content."""
    frag = re.sub(r'<form action="p_sql_cart\.cfm".*?</form>', '', frag, flags=re.S)
    frag = re.sub(r'<div id="myModal\d+" class="modal">.*?</form>', '', frag, flags=re.S)
    return frag


def parse_items(pid):
    inline = inline_items(raw(f'prd{pid}'))
    items = {}
    for f in sorted(ITEMS.glob(f'{pid}_*_*.html'), key=lambda f: (int(f.stem.split('_')[1]), int(f.stem.split('_')[2]))):
        _, item, row = f.stem.split('_')
        page = f.read_text(encoding='utf-8', errors='replace')
        g = lambda n: (re.search(rf'name="{n}" value="([^"]*)"', page) or [None, ''])[1]
        it = items.setdefault(item, {'id': item, 'sku': html.unescape(g('item_cd')), 'name': clean_title(g('short_desc')),
                                     'price': float(g('base_price') or 0), 'label': g('price_label') or 'Price', 'steps': []})
        reg = re.search(r'class="ckregprice">\s*&nbsp;\$([\d,]+\.\d\d)', page)
        if reg and not it['price']:
            it['price'] = float(reg.group(1).replace(',', ''))
        stock = re.search(r'(out of stock|special order|backorder[^<]*)', page, re.I)
        if stock:
            it['note'] = clean_title(stock.group(1))
        # Select lists
        for sel in re.finditer(r'<div[^>]*class="itemoptiontitle[^"]*"[^>]*>(.*?)</div>\s*<select[^>]*>(.*?)</select>', page, re.S):
            opts = []
            for o in re.finditer(r'<option[^>]*value="([^"]*)"[^>]*>(.*?)</option>', sel.group(2), re.S):
                text = clean_title(o.group(2))
                if not text or text.lower().startswith(('please select', 'select')):
                    continue
                delta = re.search(r'([+-])\s*\$\s*([\d,]+(?:\.\d\d)?)', text)
                d = (1 if not delta or delta.group(1) == '+' else -1) * float(delta.group(2).replace(',', '')) if delta else 0
                opts.append({'v': o.group(1), 't': text, 'd': d})
            if opts:
                it['steps'].append({'type': 'select', 'title': clean_title(sel.group(1)), 'options': opts})
        # Add-on checkboxes
        adds = []
        for m in re.finditer(r'<input[^>]*type="checkbox"[^>]*>(.*?)(?=<input[^>]*type="checkbox"|</table>|</form>|<span class="ckbodyboldred")', page, re.S | re.I):
            text = clean_title(m.group(1))
            price = re.search(r'\$\s*([\d,]+\.\d\d)', text)
            name = re.sub(r'\$\s*[\d,]+\.\d\d', '', text).strip(' -')
            if name:
                adds.append({'t': name, 'd': float(price.group(1).replace(',', '')) if price else 0})
        if adds:
            it['steps'].append({'type': 'addons', 'title': 'Popular add-on accessories', 'options': adds})
    # The price frame holds the product itself; inline forms on the same page are companion
    # items (carrier, bezel). List the product first, then the companions.
    framed = list(items.values())
    # Inline items are companions (carrier, bezel) when the page also has its own priced versions.
    companions = [dict(it, companion=bool(framed)) for it in inline if it['id'] not in items]
    return framed + companions


def money(n):
    return f'${n:,.2f}'


# ---------- Page bodies ----------

def thumb_card(it):
    if it['kind'] == 'p':
        info = PRD_INFO.get(it['id'])
        href = info['path'] if info else local_link(f"{LIVE}index.cfm/page/ptype=product/product_id={it['id']}/mode=prod/prd{it['id']}.htm")
        price = PRICES.get(it['id'])
        meta = f'<span class="card-sku">{html.escape(it["skus"])}</span>' if it['skus'] else ''
        meta += f'<span class="card-price">{"From " if price and price[1] else ""}{money(price[0])}</span>' if price else ''
    else:
        info = CAT_INFO.get(it['id'])
        href = info['path'] if info else local_link(f"{LIVE}index.cfm/page/ptype=results/category_id={it['id']}/mode=cat/cat{it['id']}.htm")
        meta = ''
    img = local_img(it['thumb'])
    pic = f'<img src="{img}" alt="" loading="lazy">' if img else '<span class="card-noimg" aria-hidden="true"></span>'
    fit = fit_attrs(it['id']) if it['kind'] == 'p' and it['id'] in PRD_INFO else ''
    return f'''        <li class="shop-card"{fit}><a href="{href}">{pic}<span class="card-body"><span class="card-name">{html.escape(TYPO_FIX(it["name"]))}</span>{meta}</span></a></li>'''


def TYPO_FIX(t):
    for bad, good in TYPOS.items():
        t = t.replace(bad, good)
    return t


def tree_crumbs(c, include_self):
    ids = chain(c) + ([c] if include_self else [])
    return [(CAT_INFO[i]['path'], CAT_INFO[i]['title']) for i in ids if i in CAT_INFO]


def crumbs_html(crumbs, current):
    parts = [f'<li><a href="{h}">{html.escape(t)}</a></li>' for h, t in crumbs if h]
    return f'      <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li>{"".join(parts)}<li aria-current="page">{html.escape(current)}</li></ol></nav>'


def build_category(c):
    page = raw(f'cat{c}')
    frag = main_content(page)
    info = CAT_INFO[c]
    crumbs = tree_crumbs(c, False)
    frag = re.sub(r'<div align="left" class="smallbody">.*?</div>', '', frag, count=1, flags=re.S)
    frag, subs_block = cut_block(frag, r'<div id="thmsubcatparent"')
    frag, prds_block = cut_block(frag, r'<div id="thmprdparent"')
    subs, prds = grid_items(subs_block), grid_items(prds_block)
    frag = re.sub(r'<section class="product_divider">.*?</section>', '', frag, flags=re.S)
    intro = modernize(sanitize(galleries(frag)))
    intro = re.sub(r'Click image or text to view details', '', intro)
    INDEX.append({'k': 'Category', 't': info['title'], 'u': info['path'], 's': f'{len(prds)} products' if prds else 'Category', 'x': ''})
    parts = [f'''    <div class="wrap page-hero shop-hero">
{crumbs_html(crumbs, info["title"])}
      <h1>{html.escape(info["title"])}</h1>
    </div>''']
    if intro.strip():
        parts.append(f'    <div class="wrap shop-intro rich">\n{intro}\n    </div>')
    if subs:
        parts.append('    <section class="wrap page-section" aria-labelledby="subs">\n      <h2 id="subs">Shop by category</h2>\n      <ul class="shop-grid">\n'
                     + '\n'.join(thumb_card(s) for s in subs) + '\n      </ul>\n    </section>')
    if prds:
        parts.append(f'    <section class="wrap page-section" aria-labelledby="prods">\n      <h2 id="prods">{len(prds)} product{"s" if len(prds) != 1 else ""}</h2>\n'
                     '      <div class="fit-filter" hidden></div>\n      <ul class="shop-grid">\n'
                     + '\n'.join(thumb_card(p) for p in prds) + '\n      </ul>\n    </section>')
    parts.append(bp.help_band())
    CATALOG['cats'][c] = {'title': info['title'], 'path': info['path'], 'subs': [s['id'] for s in subs], 'products': [p['id'] for p in prds]}
    write(info['path'], f'{info["title"]} | Dakota Digital', f'Shop {info["title"]} from Dakota Digital: gauges, instruments and accessories.',
          '\n'.join(parts), f'{LIVE}index.cfm/page/ptype=results/category_id={c}/mode=cat/cat{c}.htm', script='  <script src="fit.js"></script>\n')


ACRONYMS = {'hdx', 'vhx', 'rtx', 'grfx', 'vfd', 'vfd3', 'mlx', 'mcl', 'bim', 'faq', 'pdf', 'led', 'obd', 'gps', 'efi', 'tpms', 'ls', 'gm', 'usb', 'app', 'diy'}


def tab_label(t):
    """ORDERING -> Ordering, HDX DETAILS -> HDX details (only rewrites all-caps labels)."""
    if t != t.upper():
        return t
    words = t.lower().split()
    words = [w.upper() if w in ACRONYMS and w != 'app' else w for w in words]
    return (words[0][:1].upper() + words[0][1:] + (' ' + ' '.join(words[1:]) if len(words) > 1 else '')) if words else t


def build_tabs(frag):
    """Turn the live page's tabs into open/close sections."""
    m = re.search(r'<div class="tab_container">', frag)
    if not m:
        return frag, '', 0
    frag = re.sub(r'<ul class="tabs">.*?</ul>', '', frag, flags=re.S)
    # The live markup has unbalanced divs inside tabs, so take everything from the container on
    # (it is the last block once related products are cut out).
    i = re.search(r'<div class="tab_container">', frag).start()
    frag, block = frag[:i], frag[i:]
    heads = list(re.finditer(r'<h3 class="[^"]*tab_drawer_heading[^"]*"[^>]*>(.*?)</h3>', block, re.S))
    sections, empty = [], 0
    for i, h in enumerate(heads):
        body = block[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(block)]
        label = tab_label(clean_title(h.group(1)))
        content = modernize(sanitize(galleries(body)))
        if not _norm(content) and not re.search(r'<(img|iframe)\b', content):
            empty += 1  # empty on the live site too; leave it out
            continue
        sid = 'sec-' + slugify(label)
        sections.append((sid, label, content))
    if not sections:
        return frag, '', empty
    nav = ''.join(f'<li><a href="#{sid}">{html.escape(label)}</a></li>' for sid, label, _ in sections)
    out = [f'      <nav class="psec-nav" aria-label="On this page"><ul>{nav}</ul></nav>']
    for sid, label, content in sections:
        out.append(f'      <section class="psec" id="{sid}" aria-labelledby="{sid}-h">\n        <h2 id="{sid}-h">{html.escape(label)}</h2>\n        <div class="rich">\n{content}\n        </div>\n      </section>')
    return frag, '\n'.join(out), empty


# ---------- My Garage fit data ----------

PLATFORM_CATS = {int(c) for c in re.findall(r'cat: (\d+)', (SITE / 'garage.js').read_text(encoding='utf-8'))}


def product_platforms(p):
    cats = set(GRID_LISTED.get(p, [])) | set(LISTED_IN.get(p, []))
    cats -= SHOWCASE
    full = set()
    for c in cats:
        full |= {c, *chain(c)}
    return sorted(full & PLATFORM_CATS)


def title_years(t):
    years = set()
    for m in re.finditer(r'\b((?:19|20)\d\d)\s*-\s*((?:19|20)?\d\d)\b|\b((?:19|20)\d\d)\b', t):
        if m.group(1):
            a, b = int(m.group(1)), m.group(2)
            b = int(b) if len(b) == 4 else int(str(a)[:2] + b)
            if a <= b <= a + 60:
                years.update(range(a, b + 1))
        else:
            years.add(int(m.group(3)))
    return sorted(years)


def fit_attrs(p):
    cats = product_platforms(p)
    if not cats:
        return ''
    ys = title_years(PRD_INFO[p]['title'])
    return f' data-cats="{",".join(map(str, cats))}" data-years="{",".join(map(str, ys))}"'


# ---------- Proof, themes ----------

LIFETIME = ('STR', 'VFD', 'RET', 'VHX', 'HDX', 'RTX', 'GRFX')  # full systems, per the FAQ
SEMA_URL = 'https://www.sema.org/news-media/press-release/sema-announces-new-product-award-winners-5'


def proof_html(items):
    main = items[0]['sku'].upper() if items else ''
    lines = []
    if main.startswith(LIFETIME):
        lines.append('<li><strong>Lifetime warranty</strong> on full gauge systems. <a href="faq.html#q4">Details</a></li>')
    lines.append('<li><strong>Built in Sioux Falls</strong>, South Dakota, since 1986</li>')
    lines.append(f'<li><strong>2 SEMA Show awards in 2024</strong>: Best Engineered Product (Velocity Commander cruise control) and Best New Powersports Product (MLX-5000). <a href="{SEMA_URL}" target="_blank" rel="noopener">Source</a></li>')
    return '<ul class="buy-proof">' + ''.join(lines) + '</ul>'


# ---------- Descriptions (meta + Product schema) ----------

# One line per series, using facts from the product copy and FAQ.
SERIES_LINES = [
    ('GRFX', 'A full-color screen with selectable graphic themes, GPS speed calibration and Bluetooth app setup.'),
    ('RTX', 'The factory look with the key off; LED bar gauges, color message centers and lighting you choose with it on.'),
    ('HDX', 'Real needles on black or silver alloy faces, with color message centers and Bluetooth app setup.'),
    ('VHX', 'Lit needles, backlit faces and LCD message centers, with a limited lifetime warranty.'),
    ('MLX', 'Plug-in motorcycle instruments with bright TFT displays and a high-contrast sunlight mode.'),
    ('VFD', 'Bright vacuum fluorescent digital displays that are easy to read and built to last.'),
]
SERIES_RE = 'VHX|RTX|HDX|GRFX|VFD3?|MLX|Retrotech|Odyssey|Solarix|Ion'


# Product types by part-number prefix. Gauge systems (and their metric "M" twins) are the kit
# versions; companions are sold alongside a kit but aren't a version of it.
SYSTEM_PREFIXES = {'VFD3', 'MFD3', 'VFD', 'MFD', 'RTX', 'MTX', 'HDX', 'MDX', 'VHX', 'MHX', 'GRFX', 'MGRFX', 'STR', 'RET', 'MRT'}
COMPANION_PREFIXES = {
    'ICM',                                    # instrument carriers
    'BZL', 'SPKR', 'LNS',                     # bezels, speaker bezels, lenses
    'RLC', 'HLC', 'VLC', 'CLK', 'VL',          # matching clocks
    'SEN', 'BKT',                             # senders, brackets
    'ALC', 'ALH', 'ALG', 'ALR', 'CALG',       # dash panels, handles, glove box and radio covers
}
OFFER_REPORT = {'unclassified': []}


def sku_type(sku):
    p = sku.split('-')[0].strip().upper()
    if p in SYSTEM_PREFIXES:
        return 'system'
    if p in COMPANION_PREFIXES or re.fullmatch(r'61\d{4}', p):  # 61xxxx: carrier and bezel part numbers
        return 'companion'
    return 'unknown'


def is_version(it, main, pid=None):
    """True when an item is a version of the product itself, decided by product type."""
    if it is main:
        return True
    if it.get('companion'):
        return False
    if sku_type(main['sku']) == 'system':
        kind = sku_type(it['sku'])
        if kind == 'unknown' and pid is not None:
            OFFER_REPORT['unclassified'].append({'product': pid, 'sku': it['sku'], 'name': it['name']})
        return kind == 'system'
    # Accessories and parts: versions share the main item's part-number family (or its metric twin)
    a, b = it['sku'].split('-')[0].upper(), main['sku'].split('-')[0].upper()
    return a == b or (a[:1] == 'M' and a[1:] == b[1:]) or (b[:1] == 'M' and b[1:] == a[1:])


def series_line(title, skus):
    # Only full gauge systems get the series summary (not clocks, single gauges or accessories).
    if not re.search(r'instrument|cluster|gauge system', title, re.I) or re.search(r'clock|single|individual', title, re.I):
        return ''
    hay = (title + ' ' + ' '.join(skus)).upper()
    for key, line in SERIES_LINES:
        if re.search(rf'\b{key}', hay) or (key == 'VFD' and 'DIGITAL INSTRUMENT' in hay):
            return line
    return ''


def describe(title, body_html, skus):
    """Short meta description (~155 chars) and a fuller Product schema description, from clean copy."""
    # Paragraph text only: headings would run into the first sentence.
    text = ' '.join(_norm(p) for p in re.findall(r'<p>(.*?)</p>', re.sub(r'<(figure|table)\b.*?</\1>', ' ', body_html, flags=re.S), re.S))
    text = re.sub(r'^From Dakota Digital(?: (?:' + SERIES_RE + r'))?\b\s*', '', text)
    sentences = []
    for s in re.split(r'(?<=[.!?])\s+', text):
        # Don't break after abbreviations like "Sr." or "St."
        if sentences and re.search(r'\b(Sr|Jr|Mr|Mrs|Dr|St|No|vs|Inc|Co|approx)\.$', sentences[-1]):
            sentences[-1] += ' ' + s.strip()
        else:
            sentences.append(s.strip())
    sentences = [s for s in sentences if len(s) >= 25 and not s.startswith(('*', 'Click')) and s.endswith(('.', '!', '?'))]
    head = title.rstrip('.') + '.'
    line = series_line(title, skus)

    def build(limit, parts):
        out = head
        for s in parts:
            if len(out) + 1 + len(s) > limit:
                break
            out += ' ' + s
        return out
    short = build(160, ([line] if line else []) + sentences)
    if short == head:  # nothing fit: trim the first sentence on a word boundary
        first = (line or (sentences[0] if sentences else '')).rstrip('.')
        short = (head + ' ' + first[:155 - len(head)].rsplit(' ', 1)[0] + '…') if first else f'{head} From Dakota Digital in Sioux Falls, South Dakota.'
    long = build(600, ([line] if line else []) + sentences[:4])
    return short, long


def theme_switcher(html_text):
    """Real 'Theme:' photos from the gallery -> a lighting theme switcher."""
    seen, themes = set(), []
    for src, alt in re.findall(r'<img src="([^"]+)" alt="(Theme\s*:[^"]*)"', html_text):
        name = re.sub(r'^Theme\s*:\s*', '', html.unescape(alt)).strip()
        if name and name.lower() not in seen:
            seen.add(name.lower())
            themes.append((src, name))
    if len(themes) < 2:
        return ''
    chips = ''.join(f'<button type="button" class="theme-chip" data-src="{src}" aria-pressed="{"true" if i == 0 else "false"}">{html.escape(name)}</button>'
                    for i, (src, name) in enumerate(themes))
    first_src, first_name = themes[0]
    return f'''<section class="themes" aria-labelledby="themes-h">
  <h2 id="themes-h" class="themes-title">Lighting themes</h2>
  <div class="theme-stage"><img src="{first_src}" alt="Lit up in the {html.escape(first_name)} theme" data-theme-img></div>
  <div class="theme-chips" role="group" aria-label="Pick a lighting theme">{chips}</div>
  <p class="fine">Real photos of this system in each factory color theme. Most systems also let you set your own colors.</p>
</section>
'''


def buy_box(pid, items, live_url):
    if not items:
        return ''
    data = json.dumps(items, separators=(',', ':')).replace('</', '<\\/')
    first = items[0]
    choose = ''
    if len(items) > 1:
        choose = '<fieldset class="opt-group"><legend>Version</legend>' + ''.join(
            f'<label class="opt"><input type="radio" name="item" value="{i}"{" checked" if i == 0 else ""}><span class="opt-text">{html.escape(it["name"] or it["sku"])} <small>({html.escape(it["sku"])})</small></span><span class="opt-price">{money(it["price"])}</span></label>'
            for i, it in enumerate(items)) + '</fieldset>'
    return f'''      <aside class="buy" aria-labelledby="buy-title">
        <form class="buy-card shop-buy" data-live="{html.escape(live_url)}">
          <h2 id="buy-title">{html.escape(PRD_INFO[pid]["title"])}</h2>
          <p class="sku">SKU <span data-b="sku">{html.escape(first["sku"])}</span></p>
          <p class="price" data-b="price">{money(first["price"])}</p>
          {choose}
          <div data-b="steps"></div>
          <div class="total"><span>Your total</span><strong data-b="total" aria-live="polite">{money(first["price"])}</strong></div>
          <button type="submit" class="btn btn-primary btn-block" id="add-btn">Add to cart</button>
          <p class="buy-note" data-b="note" role="status" hidden></p>
          {proof_html(items)}
          <p class="buy-help">Questions? <a href="tel:+18008523228">Call (800) 852-3228</a> or <a href="contact.html">send a message</a>.</p>
          <script type="application/json" data-b="items">{data}</script>
        </form>
      </aside>'''


def build_product(p):
    page = raw(f'prd{p}')
    frag = main_content(page)
    info = PRD_INFO[p]
    live_url = f'{LIVE}index.cfm/page/ptype=product/product_id={p}/mode=prod/prd{p}.htm'
    crumbs = tree_crumbs(info['cat'], True)
    frag = re.sub(r'<div align="left" class="smallbody">.*?</div>', '', frag, count=1, flags=re.S)
    frag = re.sub(r'<h1[^>]*class="black_headline"[^>]*>.*?</h1>', '', frag, count=1, flags=re.S)
    frag, related_block = cut_block(frag, r'<div id="thmprdparent"')
    related = grid_items(related_block)
    frag = re.sub(r'<section class="product_divider">.*?</section>', '', frag, flags=re.S)
    # Price frames: drop the tags one by one (a greedy match would swallow the tabs between them)
    frag = re.sub(r'<iframe[^>]*p_item\.cfm[^>]*>(\s*Your browser must support iframes to purchase this product\s*)?(</iframe>)?', '', frag, flags=re.I)
    frag = strip_inline_buy(frag)
    frag, tabs, empty_tabs = build_tabs(frag)
    body = modernize(sanitize(galleries(frag)))
    # The old site's brand field ("From Dakota Digital RTX") ran into the first sentence; drop it.
    if 'From Dakota Digital' in body[:1500]:
        body = re.sub(r'From Dakota Digital(?: (?:' + SERIES_RE + r'))?\b\s*(?=<|[A-Z]|$)', '', body, count=1)
    body = re.sub(r'Your browser must support iframes to purchase this product', '', body)
    items = parse_items(p)
    if not body.strip() and not tabs and not items:
        body = ('<p>This product is no longer listed on dakotadigital.com. It may have been discontinued or replaced.</p>'
                '<p>Search above for a current part, or <a href="contact.html">ask the people who build these</a> what replaced it.</p>')
    skus = [it['sku'] for it in items if it['sku']]
    themes = theme_switcher(body + tabs)
    fit = fit_attrs(p)
    CATALOG['products'][p] = {'title': info['title'], 'path': info['path'], 'cat': info['cat'], 'skus': skus,
                              'prices': [it['price'] for it in items],
                              'steps': [[s['title'], [o['t'] for o in s['options']]] for it in items for s in it['steps']],
                              'tabs': re.findall(r'<h2 id="sec-[^"]+-h">(.*?)</h2>', tabs), 'empty_tabs': empty_tabs,
                              'related': [r['id'] for r in related], 'themes': len(re.findall('theme-chip', themes)),
                              'fit': fit.strip()}
    INDEX.append({'k': 'Part', 't': info['title'], 'u': info['path'], 's': ', '.join(skus[:2]) or 'Product', 'x': ' '.join(skus)})
    buy = buy_box(p, items, live_url)
    fit_strip = f'      <div class="fit" id="fit"{fit} aria-live="polite"></div>\n' if fit else ''
    parts = [f'''    <div class="wrap page-hero shop-hero">
{crumbs_html(crumbs, info["title"])}
      <h1>{html.escape(info["title"])}</h1>
{fit_strip}    </div>''',
             f'''    <div class="wrap shop-product{" has-buy" if buy else ""}">
      <div class="shop-main rich">
{themes}{body}
      </div>
{buy}
    </div>''']
    if tabs:
        parts.append(f'    <div class="wrap page-section psecs">\n{tabs}\n    </div>')
    if related:
        parts.append('    <section class="wrap page-section" aria-labelledby="rel">\n      <h2 id="rel">Related products</h2>\n      <ul class="shop-grid">\n'
                     + '\n'.join(thumb_card(r) for r in related) + '\n      </ul>\n    </section>')
    parts.append(f'''    <div class="wrap"><p class="fine">Also on <a href="{live_url}">dakotadigital.com</a>.</p></div>''')
    desc, long_desc = describe(info['title'], body, skus)
    # Product structured data so search results can show price
    imgs = re.findall(r'<img src="([^"]+)"', themes + body + tabs)
    ld = {'@context': 'https://schema.org', '@type': 'Product', 'name': info['title'], 'description': long_desc,
          'brand': {'@type': 'Brand', 'name': 'Dakota Digital'}, 'url': SITE_URL + info['path']}
    if imgs:
        ld['image'] = [SITE_URL + i for i in dict.fromkeys(imgs)][:5]
    if skus:
        ld['sku'] = skus[0]
    if items:
        offers = [{'@type': 'Offer', 'sku': it['sku'], 'name': it['name'] or info['title'], 'price': f'{it["price"]:.2f}',
                   'priceCurrency': 'USD', 'url': SITE_URL + info['path']}
                  for it in items if it['price'] and is_version(it, items[0], p)]  # gauge versions only, by product type
        if offers:
            ld['offers'] = offers if len(offers) > 1 else offers[0]
    script = f'  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n  <script src="shop.js"></script>\n  <script src="fit.js"></script>\n'
    if buy:
        script += '  <script src="buy-dock.js" defer></script>\n'
    write(info['path'], f'{info["title"]} | Dakota Digital', desc, '\n'.join(parts), live_url, script=script)


def write(path, title, desc, body, canonical, script=''):
    """Write a page into shop/: build it root-relative, then point relative links up one level."""
    tmp_slug = '__tmp__'
    bp.page(tmp_slug, title, desc, '', body, canonical, script)
    tmp = SITE / f'{tmp_slug}.html'
    s = tmp.read_text(encoding='utf-8')
    tmp.unlink()
    s = re.sub(r'\b(href|src)="(?!https?:|#|tel:|mailto:|data:|/)([^"]*)"', lambda m: f'{m.group(1)}="../{m.group(2)}"', s)
    (SITE / path).write_text(s, encoding='utf-8')


# ---------- Run ----------

SHOP.mkdir(exist_ok=True)
for old in SHOP.glob('*.html'):
    old.unlink()
CATALOG = {'cats': {}, 'products': {}}
INDEX = []
# Where each product lives: categories that show it in their product grid
GRID_LISTED = {}
for c in CATS:
    _, block = cut_block(main_content(raw(f'cat{c}')), r'<div id="thmprdparent"')
    for it in grid_items(block):
        if it['kind'] == 'p':
            GRID_LISTED.setdefault(it['id'], []).append(c)
for p in PRD_INFO:
    PRD_INFO[p]['cat'] = home_cat(p)
# Prices first, so category cards can show them
PRICES = {}
for p in PRODS:
    its = parse_items(p)
    if its:
        ps = [it['price'] for it in its if it['price']]
        if ps:
            # Card price: the product's own (first) item. "From" only when its options change the price.
            main = its[0]
            PRICES[p] = (main['price'], any(o['d'] for s in main['steps'] if s['type'] == 'select' for o in s['options']))
for p in PRODS:
    build_product(p)
for c in CATS:
    build_category(c)
(CONTENT / 'catalog.json').write_text(json.dumps(CATALOG, ensure_ascii=False, indent=0), encoding='utf-8')
(CONTENT / 'catalog_index.json').write_text(json.dumps(INDEX, ensure_ascii=False), encoding='utf-8')
img_map_path.write_text(json.dumps(IMAGES, indent=0), encoding='utf-8')
# Old (misspelled) URLs -> new ones, as permanent redirects on Vercel
vj = ROOT / 'vercel.json'
conf = json.loads(vj.read_text(encoding='utf-8'))
conf['redirects'] = [{'source': s, 'destination': d, 'permanent': True} for s, d in sorted(REDIRECTS.items())]
vj.write_text(json.dumps(conf, indent=2) + '\n', encoding='utf-8')
(CONTENT / 'offer_report.json').write_text(json.dumps(OFFER_REPORT, indent=1, ensure_ascii=False), encoding='utf-8')
print(f'Offers: {len(OFFER_REPORT["unclassified"])} kit items left out because their type is unclassified (see tools/content/offer_report.json)')
print(f'Built {len(CATALOG["cats"])} category pages and {len(CATALOG["products"])} product pages; {len(IMAGES)} images referenced; '
      f'{len(PRICES)} products priced')

#!/usr/bin/env python3
"""Build a review-board artifact page from a review.json description.

    python3 build.py path/to/review.json OUT_DIR [--embed] [--max-width 760]

Writes OUT_DIR/index.html, OUT_DIR/img/* (unless --embed) and OUT_DIR/files-map.json
(the map to pass as `files` to the Artifact tool, with `root: OUT_DIR`).
See the design-critic method (§6) and templates/decision-board.review.json for the data model.
"""
import argparse, base64, hashlib, html, io, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, '..', 'assets', 'template.html')
DEFAULT_VERDICTS = [
    {"v": "ok", "label": "Ok", "tone": "ok"},
    {"v": "fix", "label": "Fix", "tone": "fix"},
    {"v": "skip", "label": "Skip", "tone": "skip"},
]

try:
    from PIL import Image
except ImportError:  # images are copied as-is and `frame` becomes mandatory for pins
    Image = None

esc = lambda s: html.escape(str(s or ''), quote=True)


def safe_id(s):
    s = re.sub(r'[^A-Za-z0-9_\-.~:@+]', '-', str(s)).strip('-')
    if not s or s in ('.', '..'):
        s = 'x' + hashlib.md5(str(s).encode()).hexdigest()[:8]
    return s[:120]


def norm(s):
    return re.sub(r'\s+', ' ', str(s or '').replace('’', "'").replace('‘', "'")).strip().lower()


def load_texts(screen, base):
    """texts = [[text, style, x, y, w, h], ...] inline, or a path to a JSON / JSON-lines file."""
    t = screen.get('texts')
    if isinstance(t, list):
        return t
    if isinstance(t, str):
        path = os.path.join(base, t)
        raw = open(path, encoding='utf-8').read().strip()
        if raw.startswith('['):
            return json.loads(raw)
        rows = [json.loads(l) for l in raw.splitlines() if l.strip()]
        want = screen.get('textsRoot')
        for r in rows:
            if want is None or r.get('afterId') == want or r.get('root') == want:
                return r.get('texts', [])
    return []


def resolve_boxes(item, texts, skip_styles):
    if item.get('boxes'):
        return [list(b)[:4] for b in item['boxes']]
    hits = []
    for pat in item.get('match', []):
        style = None
        if '@@' in pat:
            pat, style = pat.split('@@', 1)
        for row in texts:
            txt, st = row[0], row[1]
            if style is None and any(st.startswith(s) for s in skip_styles):
                continue
            if style is not None and st != style:
                continue
            if norm(txt).startswith(norm(pat)):
                b = list(row[2:6])
                if b not in hits:
                    hits.append(b)
    return hits


def process_image(src, base, out_dir, name, embed, max_w):
    path = os.path.join(base, src)
    if not os.path.exists(path):
        sys.exit(f'image not found: {path}')
    size = None
    if Image is None:
        ext = os.path.splitext(path)[1].lower()
        data = open(path, 'rb').read()
        if embed:
            mime = 'image/png' if ext == '.png' else 'image/jpeg'
            return f'data:{mime};base64,' + base64.b64encode(data).decode(), None, None
        rel = f'img/{name}{ext}'
        shutil.copy(path, os.path.join(out_dir, rel))
        return rel, None, rel
    im = Image.open(path).convert('RGB')
    size = im.size
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)))
    buf = io.BytesIO()
    im.save(buf, 'JPEG', quality=80, optimize=True)
    if embed:
        return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode(), size, None
    rel = f'img/{name}.jpg'
    open(os.path.join(out_dir, rel), 'wb').write(buf.getvalue())
    return rel, size, rel


def verdict_buttons(verdicts):
    return ''.join(f'<button class="rb-v" type="button" data-v="{esc(v["v"])}" data-tone="{esc(v.get("tone", v["v"]))}">{esc(v["label"])}</button>' for v in verdicts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('review')
    ap.add_argument('out')
    ap.add_argument('--embed', action='store_true', help='inline images as data URIs (no files map)')
    ap.add_argument('--max-width', type=int, default=760)
    a = ap.parse_args()

    base = os.path.dirname(os.path.abspath(a.review))
    R = json.load(open(a.review, encoding='utf-8'))
    os.makedirs(os.path.join(a.out, 'img'), exist_ok=True)
    verdicts = R.get('verdicts') or DEFAULT_VERDICTS
    skip_styles = R.get('skipStyles', ['UI/Button'])
    files = {}
    stats = {'screens': 0, 'items': 0, 'pinned': 0, 'unpinned': []}

    header = f'''<header class="rb-hero">
  {f'<span class="rb-eyebrow">{esc(R["eyebrow"])}</span>' if R.get('eyebrow') else ''}
  <h1>{esc(R["title"])}</h1>
  {f'<p class="rb-lead">{R["lead"]}</p>' if R.get('lead') else ''}
  <div class="rb-help">{R.get('help') or 'Each screen has a number, each item has a number like «3.2». On the image, items are marked with the same tags: clicking a tag jumps to the item, clicking the item number jumps to the tag. Set a verdict and leave a comment for each item — everything saves immediately. The JSON button at the top shows all verdicts and downloads them as a file.'}</div>
</header>'''

    nav = []
    dec_html = ''
    if R.get('decisions'):
        nav.append('<a href="#rb-decisions">Decisions</a>')
        cards = []
        for d in R['decisions']:
            key = safe_id(d['key'])
            opts = ''.join(f'<button class="rb-opt{" rec" if o == d.get("recommended") else ""}" type="button" data-value="{esc(o)}">{esc(o)}</button>' for o in d.get('options', []))
            cards.append(f'''<div class="rb-dec" data-key="{key}" data-q="{esc(d["question"])[:200]}">
  <div class="q">{esc(d["question"])}</div>
  <div class="rb-opts">{opts}</div>
  {f'<div class="rb-why">{d["why"]}</div>' if d.get('why') else ''}
  <textarea placeholder="Comment on the decision" aria-label="Comment on the decision {esc(d["question"])}"></textarea>
  <div class="rb-st"></div>
</div>''')
        dec_html = f'<h2 id="rb-decisions">{esc(R.get("decisionsTitle", "Decisions"))}</h2>\n<div class="rb-decs">' + '\n'.join(cards) + '</div>'

    sections_html = []
    no = 0
    for si, sec in enumerate(R.get('sections', []), 1):
        sid = safe_id(sec.get('id') or f's{si}')
        nav.append(f'<a href="#sec-{sid}">{esc(sec.get("nav") or sec["title"])}</a>')
        blocks = [f'<h2 id="sec-{sid}">{esc(sec["title"])}</h2>']
        if sec.get('intro'):
            blocks.append(f'<p class="rb-cap">{sec["intro"]}</p>')
        for scr in sec.get('screens', []):
            no += 1
            stats['screens'] += 1
            scid = safe_id(scr['id'])
            texts = load_texts(scr, base)
            imgs = scr.get('images', [])
            pin_idx = next((i for i, im in enumerate(imgs) if im.get('pins')), len(imgs) - 1)
            items = scr.get('items', [])
            item_boxes = [resolve_boxes(it, texts, skip_styles) for it in items]
            shots = []
            wide = False
            for ii, im in enumerate(imgs):
                src, size, rel = process_image(im['src'], base, a.out, f'{scid}-{ii + 1}', a.embed, a.max_width)
                if rel:
                    files[rel] = rel
                fw, fh = (im.get('frame') or size or (None, None))
                wide = wide or (fw and fw > 500)
                overlay = ''
                if ii == pin_idx and fw and fh:
                    parts = []
                    for k, boxes in enumerate(item_boxes, 1):
                        tag = f'{no}-{k}'
                        if not boxes:
                            continue
                        for (x, y, w, h) in boxes:
                            parts.append(f'<span class="rb-box" data-it="{tag}" style="left:{x / fw * 100:.2f}%;top:{y / fh * 100:.2f}%;width:{w / fw * 100:.2f}%;height:{h / fh * 100:.2f}%"></span>')
                        fx, fy, _, fhh = min(boxes, key=lambda b: (b[1], b[0]))
                        parts.append(f'<a class="rb-pin" id="pin-{tag}" href="#it-{tag}" data-it="{tag}" style="left:{max(fx, 14) / fw * 100:.2f}%;top:{(fy + fhh / 2) / fh * 100:.2f}%" title="{no}.{k}">{no}.{k}</a>')
                    overlay = ''.join(parts)
                label = f'<div class="t"><span>{esc(im.get("label", ""))}</span>{("<span class=rb-meta>" + esc(im["note"]) + "</span>") if im.get("note") else ""}</div>' if (im.get('label') or im.get('note')) else ''
                maxw = f'max-width:{min(fw, 420)}px' if fw and fw <= 500 else ''
                shots.append(f'<div class="rb-shot">{label}<div class="rb-pinwrap" style="{maxw}"><img src="{src}" alt="{esc(scr["title"])} {esc(im.get("label", ""))}" loading="lazy">{overlay}</div></div>')

            lis = []
            for k, it in enumerate(items, 1):
                tag = f'{no}-{k}'
                key = f'i-{scid}-{k}'
                has_pin = bool(item_boxes[k - 1])
                stats['items'] += 1
                if has_pin:
                    stats['pinned'] += 1
                else:
                    stats['unpinned'].append(f'{no}.{k}')
                num = f'<a class="rb-num" href="#pin-{tag}" data-it="{tag}" title="Show on the image">{no}.{k}</a>' if has_pin else f'<span class="rb-num">{no}.{k}</span>'
                plain = re.sub(r'<[^>]+>', '', it['text'])[:160]
                lis.append(f'''<li class="rb-item" id="it-{tag}" data-it="{tag}" data-key="{key}" data-screen="{scid}" data-no="{no}.{k}" data-t="{esc(plain)}">
  {num}<span>{it["text"]}</span><span class="rb-vs">{verdict_buttons(verdicts)}</span>
  <span class="rb-cmt"><input type="text" placeholder="Comment on item {no}.{k}" aria-label="Comment on item {no}.{k}"><span class="rb-st"></span></span>
</li>''')
            items_html = f'<ul class="rb-items">{"".join(lis)}</ul>' if lis else ''
            foot = f'<div class="rb-foot">{scr["footnote"]}</div>' if scr.get('footnote') else ''
            all_btn = f'<button class="rb-btn" type="button" data-all="{esc(verdicts[0]["v"])}">All items: {esc(verdicts[0]["label"])}</button>' if items else ''
            sbar = f'<div class="rb-sbar"><span class="rb-cap">Screen {no} as a whole:</span>{verdict_buttons(verdicts)}{all_btn}<input type="text" placeholder="Comment on screen {no}" aria-label="Comment on screen {no}"><span class="rb-st"></span></div>'
            single = len(imgs) == 1
            body = (f'<div class="rb-body single{" wide" if wide else ""}">{"".join(shots)}<div>{items_html}{foot}</div></div>' if single
                    else f'<div class="rb-body"><div class="rb-imgs">{"".join(shots)}</div>{items_html}{foot}</div>')
            meta = f'<span class="rb-meta">{esc(scr["meta"])}</span>' if scr.get('meta') else ''
            lead = f'<div class="rb-lead-s">{scr["lead"]}</div>' if scr.get('lead') else ''
            blocks.append(f'''<section class="rb-screen" id="scr-{scid}" data-key="s-{scid}" data-id="{scid}" data-no="{no}" data-t="{esc(scr["title"])[:120]}">
  <h3><span class="rb-no">{no}</span>{esc(scr["title"])}{meta}</h3>{lead}
  {body}
  {sbar}
</section>''')
        sections_html.append('\n'.join(blocks))

    cfg = {
        'title': R['title'],
        'collection': safe_id(R.get('collection', 'verdicts')),
        'storageKey': safe_id(R.get('storageKey') or R['title']),
        'exportFilename': R.get('exportFilename', 'review-verdicts.json'),
        'verdicts': verdicts,
        'focusCommentOn': R.get('focusCommentOn', 'fix'),
        'appliedLabel': R.get('appliedLabel', 'review passed'),
    }
    page = open(TEMPLATE, encoding='utf-8').read()
    page = (page.replace('{{TITLE}}', esc(R['title']))
                .replace('{{HEADER}}', header)
                .replace('{{NAV}}', '\n  '.join(nav))
                .replace('{{DECISIONS}}', dec_html)
                .replace('{{SECTIONS}}', '\n'.join(sections_html))
                .replace('{{CONFIG}}', json.dumps(cfg, ensure_ascii=False).replace('</', '<\\/')))
    open(os.path.join(a.out, 'index.html'), 'w', encoding='utf-8').write(page)
    json.dump(files, open(os.path.join(a.out, 'files-map.json'), 'w'), indent=1)
    size = os.path.getsize(os.path.join(a.out, 'index.html'))
    print(json.dumps({'index': os.path.join(a.out, 'index.html'), 'bytes': size, 'files': len(files),
                      'screens': stats['screens'], 'items': stats['items'], 'pinned': stats['pinned'],
                      'unpinned': stats['unpinned'][:40]}, ensure_ascii=False))
    if len(files) > 250:
        print('WARNING: more than 250 files — the Artifact tool accepts at most 255 per publish; use --embed or split.', file=sys.stderr)
    if size > 15_000_000:
        print('WARNING: page is over 15 MB — do not use --embed for this many images.', file=sys.stderr)


if __name__ == '__main__':
    main()

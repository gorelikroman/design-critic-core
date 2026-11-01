// ---------------------------------------------------------------------------
// Live layout checks: a read-only inspector for a rendered page. Inject this
// whole file into the page (a test runner's execute, a browser extension's
// content script, or the DevTools console), then call
//
//   window.designCriticChecks({ root, touch, axeResults })
//
// root        element to inspect (default: document.body)
// touch       true on a touch viewport: adds the 44 px recommendation
// reflow      false to skip the sideways-scroll check (a component shown in a
//             fixed-width frame, where the frame and not the component sets
//             the width); default true
// axeResults  optional result of axe.run() on the same root; its violations
//             are mapped to catalog IDs (contrast, names, labels, alt, size)
// apca        false to skip the perceptual contrast pass (default true): every
//             text pair gets its APCA lightness contrast (Lc) next to the WCAG 2
//             ratio; a pair that passes the ratio but falls below its APCA level
//             is a warning, one that fails the ratio but meets APCA is a note.
//             The WCAG 2 ratio stays the floor (its failures come from axe).
//
// Returns { url, viewport, findings[] }. Each finding carries the catalog ID,
// the lens entry and the severity of the rule it applies, a CSS path to the
// element and a measured detail. Geometry is measured, not judged: a finding
// is evidence for review, and the severity is the rule's, not a verdict on
// the screen. Nothing on the page is changed.
// ---------------------------------------------------------------------------
(function () {
  const RULES = {
    overlap:   { id: 'A-06', lens: 'lens 10 · Hit areas never overlap and decorative layers never eat clicks', severity: 'blocking' },
    target24:  { id: 'A-03', lens: 'lens 10 · Target size', severity: 'blocking' },
    target44:  { id: 'A-03', lens: 'lens 10 · Target size', severity: 'warning' },
    target32:  { id: 'A-03', lens: 'lens 10 · Target size', severity: 'warning' },
    clipped:   { id: 'I-06', lens: 'lens 02 · Wrap deliberately; truncate without losing content', severity: 'blocking' },
    ellipsis:  { id: 'I-06', lens: 'lens 02 · Wrap deliberately; truncate without losing content', severity: 'warning' },
    spill:     { id: 'M-09', lens: 'lens 02 · Wrap deliberately; truncate without losing content', severity: 'warning' },
    reflow:    { id: 'L-04', lens: 'lens 10 · Structure is navigation; zoom and reflow', severity: 'blocking' },
    textHit:   { id: '—',    lens: 'lens 05 · Look once, report what visibly broke, name the owning discipline', severity: 'note' },
    apca:      { id: 'L-01', lens: 'lens 03 · Contrast floors, measured on the rendered pair', severity: 'warning' },
    apcaOnly:  { id: 'L-01', lens: 'lens 03 · Contrast floors, measured on the rendered pair', severity: 'note' },
    contrast:  { id: 'L-01', lens: 'lens 03 · Contrast floors, measured on the rendered pair', severity: 'blocking' },
    name:      { id: 'K-07', lens: 'lens 10 · Every control exposes name, role and state', severity: 'blocking' },
    label:     { id: 'D-02', lens: 'lens 10 · Every field has a programmatic label', severity: 'blocking' },
    alt:       { id: 'K-08', lens: 'lens 10 · Images and icons: alt by purpose', severity: 'blocking' },
  };
  const AXE = {
    'color-contrast': 'contrast', 'button-name': 'name', 'link-name': 'name', 'aria-command-name': 'name',
    'aria-toggle-field-name': 'name', 'input-button-name': 'name', 'label': 'label', 'select-name': 'label',
    'image-alt': 'alt', 'role-img-alt': 'alt', 'svg-img-alt': 'alt', 'target-size': 'target24',
  };
  const INTERACTIVE = 'a[href],button,input:not([type=hidden]),select,textarea,summary,' +
    '[role=button],[role=link],[role=checkbox],[role=radio],[role=switch],[role=tab],[role=menuitem],' +
    '[role=option],[role=slider],[tabindex]:not([tabindex="-1"])';

  const px = n => Math.round(n * 10) / 10;

  function cssPath(el) {
    const parts = [];
    for (let e = el; e && e.nodeType === 1 && parts.length < 5; e = e.parentElement) {
      if (e.id) { parts.unshift('#' + CSS.escape(e.id)); break; }
      let p = e.localName;
      const cls = [...e.classList].filter(c => !/^(css|sc|jsx|_)[-_a-z0-9]{3,}$/i.test(c)).slice(0, 2);
      if (cls.length) p += '.' + cls.map(c => CSS.escape(c)).join('.');
      const sib = e.parentElement ? [...e.parentElement.children].filter(c => c.localName === e.localName) : [];
      if (sib.length > 1) p += `:nth-of-type(${sib.indexOf(e) + 1})`;
      parts.unshift(p);
    }
    return parts.join(' > ');
  }
  const label = el => (el.getAttribute('aria-label') || el.innerText || el.value || el.getAttribute('title') || '')
    .replace(/\s+/g, ' ').trim().slice(0, 60);

  function visible(el) {
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return false;
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      const s = getComputedStyle(e);
      if (s.display === 'none' || s.visibility === 'hidden' || parseFloat(s.opacity) === 0) return false;
      if (s.clip === 'rect(0px, 0px, 0px, 0px)' || s.clipPath === 'inset(50%)') return false;
    }
    return true;
  }
  // A sticky or fixed layer covers content only at some scroll positions.
  function pinned(el) {
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      if (/fixed|sticky/.test(getComputedStyle(e).position)) return e;
    }
    return null;
  }
  const inside = (inner, outer) => inner.left >= outer.left - 1 && inner.right <= outer.right + 1 &&
    inner.top >= outer.top - 1 && inner.bottom <= outer.bottom + 1;
  const field = el => ['INPUT', 'TEXTAREA', 'SELECT'].includes(el.tagName);
  const intersect = (a, b) => ({ w: Math.min(a.right, b.right) - Math.max(a.left, b.left), h: Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) });

  // Inline text links inside a sentence are exempt from the size floor (WCAG 2.5.8).
  function inlineLink(el) {
    if (el.localName !== 'a' || getComputedStyle(el).display !== 'inline') return false;
    const p = el.parentElement;
    return !!p && (p.innerText || '').trim().length > (el.innerText || '').trim().length + 10;
  }

  // ---- Contrast: WCAG 2 ratio and APCA lightness contrast --------------------
  // APCA-W3 0.0.98G-4g constants (Andrew Somers, W3 licence: web content only).
  const parseColor = s => {
    const m = /rgba?\(([^)]+)\)/.exec(s || '');
    if (!m) return null;
    const p = m[1].split(/[\s,/]+/).filter(Boolean).map(Number);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const over = (top, under) => ({ r: top.r * top.a + under.r * (1 - top.a), g: top.g * top.a + under.g * (1 - top.a),
    b: top.b * top.a + under.b * (1 - top.a), a: 1 });
  const apcaY = c => 0.2126729 * Math.pow(c.r / 255, 2.4) + 0.7151522 * Math.pow(c.g / 255, 2.4) + 0.0721750 * Math.pow(c.b / 255, 2.4);
  function apcaLc(text, bg) {
    let t = apcaY(text), b = apcaY(bg);
    if (t <= 0.022) t += Math.pow(0.022 - t, 1.414);
    if (b <= 0.022) b += Math.pow(0.022 - b, 1.414);
    if (Math.abs(b - t) < 0.0005) return 0;
    if (b > t) { const s = (Math.pow(b, 0.56) - Math.pow(t, 0.57)) * 1.14; return s < 0.1 ? 0 : (s - 0.027) * 100; }
    const s = (Math.pow(b, 0.65) - Math.pow(t, 0.62)) * 1.14; return s > -0.1 ? 0 : (s + 0.027) * 100;
  }
  const lin = v => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  const relL = c => 0.2126 * lin(c.r) + 0.7152 * lin(c.g) + 0.0722 * lin(c.b);
  function wcagRatio(a, b) { const x = relL(a), y = relL(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
  // The solid colour a text box renders on; null where an image or gradient is under it.
  function backdrop(el) {
    const layers = [];
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      const s = getComputedStyle(e);
      if (s.backgroundImage && s.backgroundImage !== 'none') return null;
      const c = parseColor(s.backgroundColor);
      if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; }
    }
    let base = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = layers.length - 1; i >= 0; i--) base = over(layers[i], base);
    return base;
  }
  const hex = c => '#' + [c.r, c.g, c.b].map(v => Math.round(v).toString(16).padStart(2, '0')).join('').toUpperCase();

  window.designCriticChecks = function (opts = {}) {
    const root = opts.root || document.body;
    const findings = [];
    const add = (key, el, detail, extra) => findings.push(Object.assign({ check: key }, RULES[key], {
      selector: el ? cssPath(el) : null, text: el ? label(el) : '', detail }, extra || {}));

    // Interactive targets: size and overlap.
    const targets = [...root.querySelectorAll(INTERACTIVE)].filter(visible).filter(el => !el.disabled);
    const rects = targets.map(el => el.getBoundingClientRect());
    targets.forEach((el, i) => {
      const r = rects[i];
      if (inlineLink(el)) return;
      // The 24 px floor and its spacing exception come from axe (target-size);
      // these are the lens's recommendations above the floor.
      if (opts.touch && (r.width < 44 || r.height < 44)) {
        add('target44', el, `${px(r.width)} × ${px(r.height)} px; touch recommendation is 44 × 44`);
      } else if (!opts.touch && (r.width < 32 || r.height < 32)) {
        add('target32', el, `${px(r.width)} × ${px(r.height)} px; desktop recommendation is 40 × 40, 32 × 32 for a mouse-only control`);
      }
    });
    for (let i = 0; i < targets.length; i++) {
      for (let j = i + 1; j < targets.length; j++) {
        const a = targets[i], b = targets[j];
        if (a.contains(b) || b.contains(a)) continue;
        if (a.closest('label') && a.closest('label') === b.closest('label')) continue;
        // An adornment (clear, reveal, calendar) drawn inside a field is one control, not two.
        if ((field(a) && inside(rects[j], rects[i])) || (field(b) && inside(rects[i], rects[j]))) continue;
        if (pinned(a) !== pinned(b)) continue;
        const o = intersect(rects[i], rects[j]);
        if (o.w > 1 && o.h > 1) add('overlap', a, `overlaps ${cssPath(b)} by ${px(o.w)} × ${px(o.h)} px`, { other: cssPath(b) });
      }
    }

    // Text that is cut off or spills out of its box.
    const texty = [...root.querySelectorAll('*')].filter(el =>
      [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()) && visible(el));
    for (const el of texty) {
      const s = getComputedStyle(el);
      const overX = el.scrollWidth - el.clientWidth, overY = el.scrollHeight - el.clientHeight;
      if (el.clientWidth === 0 || ['INPUT', 'TEXTAREA', 'SELECT'].includes(el.tagName)) continue;
      const hiddenX = /hidden|clip/.test(s.overflowX), hiddenY = /hidden|clip/.test(s.overflowY);
      const clamped = s.webkitLineClamp && s.webkitLineClamp !== 'none';
      const reachable = el.hasAttribute('title') || el.hasAttribute('aria-label');
      if ((hiddenX && overX > 1) || (hiddenY && overY > 1 && !clamped)) {
        if (s.textOverflow === 'ellipsis' || clamped) {
          if (!reachable) add('ellipsis', el, `truncated with ${clamped ? 'a line clamp' : 'an ellipsis'}; full text has no title or reveal`);
        } else {
          add('clipped', el, `text cut off: content ${overX > 1 ? px(el.scrollWidth) + ' px wide in ' + px(el.clientWidth) : px(el.scrollHeight) + ' px tall in ' + px(el.clientHeight)} px, overflow ${hiddenX ? s.overflowX : s.overflowY}, no ellipsis`);
        }
      } else if (!hiddenX && overX > 2 && s.whiteSpace !== 'normal' && !/auto|scroll/.test(s.overflowX)) {
        add('spill', el, `text runs ${px(overX)} px past its box (white-space: ${s.whiteSpace})`);
      }
    }

    // Perceptual contrast: APCA next to the WCAG 2 ratio, for each text pair.
    if (opts.apca !== false) {
      const seen = new Set();
      for (const el of texty.slice(0, 800)) {
        if (el.closest('[disabled],[aria-disabled="true"]')) continue;
        const s = getComputedStyle(el), fg = parseColor(s.color), bg = backdrop(el);
        if (!fg || !bg) continue;
        const text = over(fg, bg), size = parseFloat(s.fontSize), weight = parseInt(s.fontWeight, 10) || 400;
        const words = (el.innerText || '').trim();
        const body = /^(P|LI|DD|BLOCKQUOTE|TD)$/.test(el.tagName) || words.length >= 80;
        const level = size > 36 ? 45 : body ? 75 : 60;
        const kind = size > 36 ? 'text above 36 px' : body ? 'body text' : 'other content text';
        const large = size >= 24 || (size >= 18.66 && weight >= 700);
        const floor = large ? 3 : 4.5;
        const ratio = Math.floor(wcagRatio(text, bg) * 100) / 100, lc = Math.abs(apcaLc(text, bg));  // truncated, as axe reports
        const key = `${hex(text)}|${hex(bg)}|${level}`;
        if (seen.has(key)) continue;
        const pair = `${hex(text)} on ${hex(bg)}, ${px(size)} px / ${weight}`;
        if (ratio >= floor && lc < level) {
          seen.add(key);
          add('apca', el, `${pair}: passes WCAG 2 (${ratio.toFixed(2)} : 1) but APCA Lc ${lc.toFixed(1)} is below Lc ${level} for ${kind} — reads weaker than the ratio says`, { ratio: +ratio.toFixed(2), lc: +lc.toFixed(1) });
        } else if (ratio < floor && lc >= level) {
          seen.add(key);
          add('apcaOnly', el, `${pair}: fails WCAG 2 (${ratio.toFixed(2)} : 1, the floor stays blocking) but APCA rates Lc ${lc.toFixed(1)}, above Lc ${level} for ${kind}`, { ratio: +ratio.toFixed(2), lc: +lc.toFixed(1) });
        }
      }
    }

    // Text boxes painted on top of each other.
    const lines = texty.filter(el => !el.querySelector('*') || el.children.length === 0).slice(0, 400)
      .map(el => ({ el, r: el.getBoundingClientRect() }));
    for (let i = 0; i < lines.length; i++) {
      for (let j = i + 1; j < lines.length; j++) {
        const a = lines[i], b = lines[j];
        if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
        if (pinned(a.el) !== pinned(b.el)) continue;
        const o = intersect(a.r, b.r);
        if (o.w > 4 && o.h > 4) add('textHit', a.el, `text box overlaps ${cssPath(b.el)} by ${px(o.w)} × ${px(o.h)} px`, { other: cssPath(b.el) });
      }
    }

    // Horizontal overflow of the page itself (reflow).
    const doc = document.documentElement, vw = doc.clientWidth;
    if (opts.reflow !== false && doc.scrollWidth > vw + 1) {
      const wide = [...root.querySelectorAll('*')].filter(el => {
        const r = el.getBoundingClientRect();
        return r.right > vw + 1 && r.width > 0 && visible(el) && !(el.parentElement && el.parentElement.getBoundingClientRect().right > vw + 1);
      }).slice(0, 5);
      if (!wide.length) add('reflow', null, `page scrolls sideways: ${doc.scrollWidth} px of content in a ${vw} px viewport`);
      wide.forEach(el => add('reflow', el, `ends at ${px(el.getBoundingClientRect().right)} px in a ${vw} px viewport; the page scrolls sideways`));
    }

    // axe-core results, mapped to the catalog.
    for (const v of (opts.axeResults && opts.axeResults.violations) || []) {
      const key = AXE[v.id];
      if (!key) continue;
      for (const node of v.nodes.slice(0, 10)) {
        const el = document.querySelector(node.target[0]);
        findings.push(Object.assign({ check: key }, RULES[key], {
          selector: el ? cssPath(el) : node.target.join(' '), text: el ? label(el) : '',
          detail: `axe ${v.id}: ${(node.failureSummary || v.help).replace(/\s+/g, ' ').replace(/^Fix any of the following: /, '').slice(0, 200)}`,
        }));
      }
    }

    return { url: location.href, viewport: { width: innerWidth, height: innerHeight }, findings };
  };
  window.designCriticChecks.apcaLc = (text, bg) => apcaLc(parseColor(text), parseColor(bg));
  window.designCriticChecks.wcagRatio = (a, b) => wcagRatio(parseColor(a), parseColor(b));
})();

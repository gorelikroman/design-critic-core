// ---------------------------------------------------------------------------
// Structural fingerprint: a read-only inspector for a handful of nodes in a
// design file. Paste this whole file into the code parameter of the script
// runtime that exposes the design tool's node API (the one that supports
// top-level `await` and a final `return`); fill in IDS first. It walks each
// root down to a depth cap and returns one `{ id, name, lines }` record per
// root, where `lines` is a text tree: one line per layer (type, name, id,
// size, style/binding info), followed by a per-root summary block (style
// coverage, variable-binding coverage, font/style variety, max depth).
// Output is capped at roughly 20 KB per root, with a truncation marker if a
// tree is large — keep IDS to 2–4 nodes per call. Read the returned lines to
// find layers, values and locations to reference in a review; the script
// never creates, moves, renames, or restyles anything.
// ---------------------------------------------------------------------------

// Fill with the node ids to fingerprint, 2–4 per call.
const IDS = [];

const MAX_DEPTH = 4;    // how many levels deep to walk under each root
const BYTE_CAP = 20000; // approx output size cap per root, in characters

const clean = s => String(s || '').replace(/[\u0000-\u001f"\\]/g, ' ').replace(/\s+/g, ' ').trim();

// Local variables are the fast path. Ids not found locally (typically
// library/remote variables) fall back to an async lookup, cached on first use.
const localVars = await figma.variables.getLocalVariablesAsync();
const vn = Object.fromEntries(localVars.map(v => [v.id, v.name]));
const varName = async id => {
  if (!id) return '?';
  if (vn[id]) return vn[id];
  try {
    const v = await figma.variables.getVariableByIdAsync(id);
    if (v) { vn[id] = v.name; return v.name; }
  } catch (e) {}
  return '?';
};

const styleName = async id => {
  if (!id || typeof id !== 'string') return id ? 'mixed' : '';
  try { const s = await figma.getStyleByIdAsync(id); return s ? s.name : '?'; }
  catch (e) { return '?'; }
};

const hex = c => '#' + [c.r, c.g, c.b].map(x => Math.round(x * 255).toString(16).padStart(2, '0')).join('');

// fill/stroke: "var:<name>" = bound to a variable (local or library), "#hex" = raw value (debt).
const fillDesc = async n => {
  try {
    if (!('fills' in n) || !Array.isArray(n.fills) || !n.fills.length) return '';
    const f = n.fills[0];
    if (f.type !== 'SOLID') return f.type;
    const bv = f.boundVariables && f.boundVariables.color;
    if (bv) return 'var:' + (await varName(bv.id));
    return hex(f.color) + (f.opacity < 1 ? '@' + f.opacity.toFixed(2) : '');
  } catch (e) { return '?'; }
};

const strokeDesc = async n => {
  try {
    if (!('strokes' in n) || !Array.isArray(n.strokes) || !n.strokes.length) return '';
    const s0 = n.strokes[0];
    const sb = s0.boundVariables && s0.boundVariables.color;
    if (sb) return 'var:' + (await varName(sb.id));
    return s0.color ? hex(s0.color) : s0.type;
  } catch (e) { return '?'; }
};

// layout: direction letter, gap (bound var name or raw number), padding (bound or raw "T/R/B/L").
const layoutDesc = async n => {
  if (!('layoutMode' in n) || n.layoutMode === 'NONE') return { text: '', gapBound: null, padBound: null };
  const bv = n.boundVariables || {};
  const gapBound = !!bv.itemSpacing;
  const g = gapBound ? 'g=' + (await varName(bv.itemSpacing.id)) : 'g=' + n.itemSpacing;
  const p = [n.paddingTop, n.paddingRight, n.paddingBottom, n.paddingLeft].join('/');
  const padBound = !!(bv.paddingTop || bv.paddingRight || bv.paddingBottom || bv.paddingLeft);
  const pb = bv.paddingTop ? 'P=' + (await varName(bv.paddingTop.id)) : 'p=' + p;
  const sb = n.primaryAxisAlignItems === 'SPACE_BETWEEN' ? ' SB' : '';
  return { text: n.layoutMode[0] + ' ' + g + ' ' + pb + sb, gapBound, padBound };
};

const fontDesc = n => {
  const f = n.fontName;
  if (!f || typeof f !== 'object' || !f.family) return { text: 'mixed', size: null };
  const size = typeof n.fontSize === 'number' ? Math.round(n.fontSize) : null;
  const weight = typeof n.fontWeight === 'number' ? ' w' + n.fontWeight : '';
  return { text: f.family.split(' ')[0] + ' ' + f.style + weight + ' ' + (size === null ? 'mixed' : size), size };
};

const sizingDesc = n => {
  const parts = [];
  if ('layoutSizingHorizontal' in n && n.layoutSizingHorizontal) parts.push('sizeH=' + String(n.layoutSizingHorizontal).toLowerCase());
  if ('layoutSizingVertical' in n && n.layoutSizingVertical) parts.push('sizeV=' + String(n.layoutSizingVertical).toLowerCase());
  return parts.join(' ');
};

async function fp(root) {
  const summary = {
    textNoStyle: 0, textStyled: 0,
    fillBound: 0, fillRaw: 0,
    strokeBound: 0, strokeRaw: 0,
    gapBound: 0, gapRaw: 0,
    padBound: 0, padRaw: 0,
    fontSizes: new Set(), textStyles: new Set(),
    maxDepth: 0,
  };
  if (!root) return { rows: ['(not found)'], summary };

  const rows = [];
  let bytes = 0;
  let truncated = false;
  const emit = line => {
    if (truncated) return;
    const next = bytes + line.length + 1;
    if (next > BYTE_CAP) { rows.push('... (truncated at ~20KB cap)'); truncated = true; return; }
    bytes = next;
    rows.push(line);
  };

  const walk = async (n, depth) => {
    if (truncated || depth > MAX_DEPTH) return;
    summary.maxDepth = Math.max(summary.maxDepth, depth);

    const head = '  '.repeat(depth) + n.type[0] + ' "' + clean(n.name) + '" #' + n.id + ' ' + Math.round(n.width) + 'x' + Math.round(n.height);
    const extra = [];

    if (n.type === 'INSTANCE') {
      try {
        const mc = await n.getMainComponentAsync();
        extra.push('component="' + clean(mc ? (mc.parent && mc.parent.type === 'COMPONENT_SET' ? mc.parent.name : mc.name) : '?') + '"');
      } catch (e) {}
    }

    if ('opacity' in n && typeof n.opacity === 'number' && n.opacity < 1) extra.push('opacity=' + n.opacity.toFixed(2));
    if ('strokeWeight' in n && typeof n.strokeWeight === 'number' && Array.isArray(n.strokes) && n.strokes.length) {
      extra.push('strokeWeight=' + n.strokeWeight);
    }
    const sizing = sizingDesc(n);
    if (sizing) extra.push(sizing);

    if (n.type === 'TEXT') {
      const sName = await styleName(n.textStyleId);
      if (!sName) summary.textNoStyle++;
      else { summary.textStyled++; if (sName !== 'mixed' && sName !== '?') summary.textStyles.add(sName); }

      const fd = fontDesc(n);
      if (fd.size !== null) summary.fontSizes.add(fd.size);

      const fill = await fillDesc(n);
      if (fill.startsWith('var:')) summary.fillBound++; else if (fill.startsWith('#')) summary.fillRaw++;

      extra.push('style="' + (sName || '-') + '"', 'text="' + clean(n.characters).slice(0, 45) + '"', 'font="' + fd.text + '"');
      if (fill) extra.push('fill=' + fill);
    } else {
      const ld = await layoutDesc(n);
      if (ld.text) {
        extra.push('layout="' + ld.text + '"');
        if (ld.gapBound !== null) { if (ld.gapBound) summary.gapBound++; else summary.gapRaw++; }
        if (ld.padBound !== null) { if (ld.padBound) summary.padBound++; else summary.padRaw++; }
      }
      const fill = await fillDesc(n);
      if (fill) {
        extra.push('fill=' + fill);
        if (fill.startsWith('var:')) summary.fillBound++; else if (fill.startsWith('#')) summary.fillRaw++;
      }
      if ('cornerRadius' in n && typeof n.cornerRadius === 'number' && n.cornerRadius) extra.push('r=' + n.cornerRadius);
      const stroke = await strokeDesc(n);
      if (stroke) {
        extra.push('stroke=' + stroke);
        if (stroke.startsWith('var:')) summary.strokeBound++; else summary.strokeRaw++;
      }
    }

    emit(head + (extra.length ? ' ' + extra.join(' ') : ''));
    if (truncated) return;
    if ('children' in n) for (const c of n.children) { if (c.visible === false) continue; await walk(c, depth + 1); }
  };

  await walk(root, 0);

  const note = truncated ? ' (partial — based on nodes visited before the cap)' : '';
  rows.push('-- summary' + note + ' --');
  rows.push('text: ' + summary.textStyled + ' styled, ' + summary.textNoStyle + ' no-style');
  rows.push('fill: ' + summary.fillBound + ' bound, ' + summary.fillRaw + ' raw');
  rows.push('stroke: ' + summary.strokeBound + ' bound, ' + summary.strokeRaw + ' raw');
  rows.push('auto-layout gap: ' + summary.gapBound + ' bound, ' + summary.gapRaw + ' raw');
  rows.push('auto-layout padding: ' + summary.padBound + ' bound, ' + summary.padRaw + ' raw');
  rows.push('font sizes used: ' + summary.fontSizes.size + ' (' + [...summary.fontSizes].sort((a, b) => a - b).join(', ') + ')');
  rows.push('text styles used: ' + summary.textStyles.size);
  rows.push('max depth reached: ' + summary.maxDepth);

  return { rows, summary };
}

const out = [];
for (const id of IDS) {
  const n = await figma.getNodeByIdAsync(id);
  const { rows } = await fp(n);
  out.push({ id, name: n ? clean(n.name) : 'missing', lines: rows });
}
return out;

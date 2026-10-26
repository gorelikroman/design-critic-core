// Collect position and style of every visible text on one or more Figma frames.
// Paste into use_figma (load /figma-use first). Replace PAGE_ID and ROOT_IDS.
// Read-only. Keep 2–4 roots per call: use_figma output is cut at ~20 KB.
// Returns [{root, name, w, h, texts: [[text, style, x, y, w, h], ...]}]
// with x/y relative to the root frame — the same units as its screenshot at 1x.
const PAGE_ID = '__PAGE__';
const ROOT_IDS = ['__ROOT__'];

const page = await figma.getNodeByIdAsync(PAGE_ID);
await figma.setCurrentPageAsync(page); // without this the first read can silently return 0 texts

const styleNames = {};
async function styleName(id) {
  if (id === figma.mixed) return 'MIXED';
  if (!id) return '';
  if (!(id in styleNames)) { const s = await figma.getStyleByIdAsync(id); styleNames[id] = s ? s.name : '?'; }
  return styleNames[id];
}
// U+2028 and friends break the MCP transport — strip them.
function clean(s) {
  let out = '';
  for (const ch of String(s)) {
    const c = ch.codePointAt(0);
    if (c === 0x2028 || c === 0x2029 || c === 0x85 || c === 0x0B || c === 0x0C) { out += ' '; continue; }
    if (c >= 0xD800 && c <= 0xDFFF) continue;
    out += ch;
  }
  return out.replace(/\s+/g, ' ').trim().slice(0, 40);
}
function hidden(n) { let p = n; while (p && p.type !== 'PAGE') { if (p.visible === false) return true; p = p.parent; } return false; }

const result = [];
for (const id of ROOT_IDS) {
  const root = await figma.getNodeByIdAsync(id);
  if (!root) { result.push({root: id, error: 'not found'}); continue; }
  const rb = root.absoluteBoundingBox;
  const texts = [];
  for (const t of root.findAllWithCriteria({types: ['TEXT']})) {
    if (hidden(t) || !t.absoluteBoundingBox) continue;
    const b = t.absoluteBoundingBox;
    texts.push([clean(t.characters), await styleName(t.textStyleId), Math.round(b.x - rb.x), Math.round(b.y - rb.y), Math.round(b.width), Math.round(b.height)]);
  }
  // Cloned instances sometimes expose inner texts only on a later call: if a root returns
  // suspiciously few texts, call it again in a separate use_figma and keep the larger result.
  result.push({root: id, name: root.name, w: Math.round(root.width), h: Math.round(root.height), texts});
}
return result;

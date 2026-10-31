// Copy lint for product description rewrites (data/descriptions/*.md).
// Checks every rewrite against the style rules and against the product's original description
// (tools/content/originals.json, written by tools/build_catalog.py). Exits 1 on any failure.
//
// Usage: npm run lint:copy        (add --json for machine-readable output)
import { readFileSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const DIR = join(ROOT, 'data', 'descriptions');
const ORIGINALS = JSON.parse(readFileSync(join(ROOT, 'tools', 'content', 'originals.json'), 'utf8'));

const MIN_WORDS = 90;
const MAX_WORDS = 150;
const CARRYOVER_RUN = 12;
const SCHEMA_LIMIT = 300;
const BANNED = ['delve', 'elevate', 'empower', 'seamless', 'unlock', 'robust', 'leverage', 'streamline', 'comprehensive',
  'cutting-edge', 'top-notch', 'raise the bar', 'game changer', 'next level', 'look no further', "whether you're",
  'state-of-the-art', 'allows you to'];
const PUNCTUATION = [['—', 'em dash'], ['–', 'en dash'], [';', 'semicolon'], ['!', 'exclamation point']];

// Quoted text (brand slogans like "The Ultimate Wagon") is exempt from the word and carryover checks.
const unquote = (s) => s.replace(/"[^"\n]*"|“[^”\n]*”/g, ' ');
const words = (s) => s.toLowerCase().replace(/[’]/g, "'").match(/[a-z0-9]+(?:'[a-z]+)?/g) || [];
const escapeRe = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const bannedRe = BANNED.map((w) => [w, new RegExp(`(?<![\\w-])${escapeRe(w).replace(/ /g, '\\s+')}(?![\\w-])`, 'i')]);
// A sentence ends at . or ? followed by a space or the end, so decimals like 0.1 don't split it.
const firstSentences = (text, n) => (text.match(/\S.*?[.?](?=\s|$)/g) || [text]).slice(0, n).map((s) => s.trim()).join(' ');

function parse(file) {
  const raw = readFileSync(join(DIR, file), 'utf8').replace(/\r\n/g, '\n');
  const fm = raw.match(/^---\n([\s\S]*?)\n---\n?/);
  const meta = {};
  if (fm) for (const line of fm[1].split('\n')) { const m = line.match(/^(\w+):\s*(.*)$/); if (m) meta[m[1]] = m[2].trim(); }
  const body = (fm ? raw.slice(fm[0].length) : raw).trim();
  const paras = body.split(/\n\s*\n/).map((p) => p.split(/\s+/).join(' ')).filter(Boolean);
  return { file, meta, product: meta.product, paras, text: paras.join(' ') };
}

function ngrams(list, n) {
  const out = new Set();
  for (let i = 0; i + n <= list.length; i++) out.add(list.slice(i, i + n).join(' '));
  return out;
}

const failures = {
  missing: [], empty: [], words: [], punctuation: [], banned: [], carryover: [], duplicateOpening: [], schema: [], unknownProduct: []
};
const notes = [];
const rewrites = readdirSync(DIR).filter((f) => f.endsWith('.md') && !/^REVIEW/i.test(f)).map(parse);
const covered = new Set();

for (const r of rewrites) {
  const orig = ORIGINALS[r.product];
  if (!orig) { failures.unknownProduct.push({ file: r.file, detail: `product ${r.product ?? '(none)'} is not in the catalog` }); continue; }
  if (orig.build) continue;
  covered.add(r.product);
  const tag = { file: r.file, product: r.product, sku: orig.skus[0] || '', title: orig.title };
  if (!r.text) { failures.empty.push(tag); continue; }

  const count = r.text.split(/\s+/).length;
  if (r.meta.short && count < MIN_WORDS) notes.push({ ...tag, detail: `${count} words, marked short: ${r.meta.short}` });
  else if (count < MIN_WORDS || count > MAX_WORDS) failures.words.push({ ...tag, detail: `${count} words` });

  const marks = PUNCTUATION.filter(([ch]) => r.text.includes(ch)).map(([, name]) => name);
  if (marks.length) failures.punctuation.push({ ...tag, detail: marks.join(', ') });

  const plain = unquote(r.text);
  const hits = bannedRe.filter(([, re]) => re.test(plain)).map(([w]) => w);
  if (hits.length) failures.banned.push({ ...tag, detail: hits.join(', ') });

  const origRuns = ngrams(words(unquote(orig.original.join(' '))), CARRYOVER_RUN);
  const mine = words(plain);
  for (let i = 0; i + CARRYOVER_RUN <= mine.length; i++) {
    const run = mine.slice(i, i + CARRYOVER_RUN).join(' ');
    if (origRuns.has(run)) { failures.carryover.push({ ...tag, detail: `"${run}"` }); break; }
  }

  const schema = firstSentences(r.text, 2);
  if (schema.length >= SCHEMA_LIMIT) failures.schema.push({ ...tag, detail: `${schema.length} characters` });
}

const openings = new Map();
for (const r of rewrites) {
  if (!r.text || ORIGINALS[r.product]?.build) continue;
  const first = firstSentences(r.text, 1).toLowerCase();
  if (!openings.has(first)) openings.set(first, []);
  openings.get(first).push(r.file);
}
for (const [first, files] of openings) if (files.length > 1) failures.duplicateOpening.push({ file: files.join(', '), detail: `"${first}"` });

for (const [pid, o] of Object.entries(ORIGINALS)) {
  if (!o.build && !covered.has(pid)) failures.missing.push({ product: pid, sku: o.skus[0] || '', title: o.title });
}

const total = Object.values(failures).reduce((n, list) => n + list.length, 0);
const out = process.stdout;
if (process.argv.includes('--json')) {
  out.write(JSON.stringify({ total, failures, notes }, null, 1) + '\n');
} else {
  out.write(`Checked ${rewrites.length} rewrite files against ${Object.keys(ORIGINALS).length} products.\n\n`);
  for (const [check, list] of Object.entries(failures)) {
    out.write(`${list.length ? 'FAIL' : 'ok  '}  ${check}: ${list.length}\n`);
    for (const f of list.slice(0, 40)) out.write(`        ${f.file || `p${f.product}`}${f.sku ? ` (${f.sku})` : ''}${f.detail ? `: ${f.detail}` : ` ${f.title}`}\n`);
    if (list.length > 40) out.write(`        ... and ${list.length - 40} more\n`);
  }
  if (notes.length) {
    out.write(`\nAllowed short (front matter "short:"): ${notes.length}\n`);
    for (const n of notes) out.write(`        ${n.file}: ${n.detail}\n`);
  }
  out.write(`\n${total ? `${total} failures` : 'No failures'}\n`);
}
process.exitCode = total ? 1 : 0;

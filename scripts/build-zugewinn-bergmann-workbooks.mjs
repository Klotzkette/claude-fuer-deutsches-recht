#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';

// Usage: bundled-node scripts/build-zugewinn-bergmann-workbooks.mjs [repoRoot] [qaTmp]
const [repoArg, qaArg] = process.argv.slice(2);
const repo = path.resolve(repoArg || path.join(path.dirname(fileURLToPath(import.meta.url)), '..'));
const akte = path.join(repo, 'testakten/zugewinnausgleich-familie-bergmann-potsdam');
const sourceDir = path.join(akte, 'zahlenwerk');
const outputDir = path.join(akte, 'xlsx');
const qa = path.resolve(qaArg || await fs.mkdtemp(path.join(os.tmpdir(), 'bergmann-xlsx-')));
assert(qa !== repo && !qa.startsWith(`${repo}${path.sep}`), 'QA directory must be outside the repository');
const dependencies = path.resolve(path.dirname(process.execPath), '../..');
const soffice = path.join(dependencies, 'bin/override/soffice');
const python = path.join(dependencies, 'python/bin/python3');
const pdftoppm = path.join(dependencies, 'bin/override/pdftoppm');
await fs.access(soffice);
await fs.access(python);
await fs.access(pdftoppm);
await fs.mkdir(qa, { recursive: true });
const moduleLink = path.join(qa, 'node_modules');
try { await fs.lstat(moduleLink); }
catch { await fs.symlink(path.join(dependencies, 'node/node_modules'), moduleLink, 'dir'); }
const requireRuntime = createRequire(path.join(qa, 'runtime.cjs'));
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(requireRuntime.resolve('@oai/artifact-tool')).href);
const JSZip = requireRuntime('jszip');
const xml = requireRuntime('xml-js');

const C = { ink: '#27332F', green: '#375B4C', pale: '#EFF4F0', line: '#B8C9BE', gray: '#64706A', white: '#FFFFFF' };
const EUR = '[$-407]#,##0.00"  ";[$-407]-#,##0.00"  ";[$-407]0.00"  "';
const DATE = 'dd"."mm"."yyyy';
const FIRST = 10;
const HEADER = FIRST - 1;
const ACCOUNT_FIELDS = ['Buchungstag', 'Valuta', 'Referenz', 'Auftraggeber_Empfänger', 'Buchungstext', 'Betrag_EUR', 'Saldo_EUR', 'Belegdatei'];
const schemas = [
  { name: 'Mara', file: 'Konto_Mara_2025_2026.csv', fields: ACCOUNT_FIELDS, dates: [0, 1], numbers: [5, 6], account: true, owner: 'Kontoinhaberin: Mara Bergmann' },
  { name: 'Jonas', file: 'Konto_Jonas_2025_2026.csv', fields: ACCOUNT_FIELDS, dates: [0, 1], numbers: [5, 6], account: true, owner: 'Kontoinhaber: Jonas Bergmann' },
  { name: 'Haushalt', file: 'Konto_Haushalt_2025_2026.csv', fields: ACCOUNT_FIELDS, dates: [0, 1], numbers: [5, 6], account: true, owner: 'Kontoinhaber: Mara und Jonas Bergmann' },
  { name: 'Jahreszahlen', file: 'Euer_Jonas_2023_2025.csv', fields: ['Position', '2023_EUR', '2024_EUR', '2025_EUR', 'Belegdatei'], dates: [], numbers: [1, 2, 3] },
  { name: 'OffenePosten', file: 'Offene_Posten_2026-07-08.csv', fields: ['Rechnungsnummer', 'Rechnungsdatum', 'Fälligkeit', 'Auftraggeber', 'Brutto_EUR', 'Bezahlt_EUR', 'Rest_EUR', 'Bemerkung', 'Belegdatei'], dates: [1, 2], numbers: [4, 5, 6] },
  { name: 'Inventar', file: 'Inventar_Jonas_2026-07-08.csv', fields: ['Inventarnummer', 'Gegenstand', 'Anschaffung', 'Anschaffungskosten_EUR', 'Buchwert_EUR', 'Angebot_Haendler_EUR', 'Bemerkung', 'Belegdatei'], dates: [2], numbers: [3, 4, 5], nullableNumbers: [5] },
];
const col = n => String.fromCharCode(65 + n);
const sum = xs => xs.reduce((a, b) => a + b, 0);
const set = (s, address, v) => { s.getRange(address).values = [[v]]; };
const get = (s, address) => s.getRange(address).values[0][0];
const hash = text => createHash('sha256').update(text).digest('hex');
const near = (actual, expected, label) => assert(typeof actual === 'number' && Math.abs(actual - expected) < 0.000001, `${label}: ${actual} != ${expected}`);

function serial(text, label) {
  assert(/^\d{4}-\d{2}-\d{2}$/.test(text), `${label}: expected ISO date, got ${text}`);
  const date = new Date(`${text}T00:00:00Z`);
  assert(Number.isFinite(date.valueOf()) && date.toISOString().slice(0, 10) === text, `${label}: invalid date`);
  return (date.valueOf() - Date.UTC(1899, 11, 30)) / 86400000;
}

function amount(text, label, nullable = false) {
  if (text === '' && nullable) return null;
  // Accept ungrouped decimal points and German decimal commas, never infer a missing value.
  assert(/^[+-]?\d+(?:\.\d{1,2})?$/.test(text) || /^[+-]?(?:\d+|\d{1,3}(?:\.\d{3})+),\d{1,2}$/.test(text), `${label}: invalid amount ${JSON.stringify(text)}`);
  const result = Number(text.includes(',') ? text.replaceAll('.', '').replace(',', '.') : text);
  assert(Number.isFinite(result), `${label}: not finite`);
  return result;
}

async function loadSources() {
  const missing = [];
  for (const s of schemas) {
    try { await fs.access(path.join(sourceDir, s.file)); }
    catch { missing.push(s.file); }
  }
  assert.equal(missing.length, 0, `CSV sources not ready: ${missing.join(', ')}`);
  const sources = [];
  for (const schema of schemas) {
    const file = path.join(sourceDir, schema.file);
    const text = await fs.readFile(file, 'utf8');
    const parsed = JSON.parse(execFileSync(python, ['-c',
      'import csv,json,sys\nwith open(sys.argv[1],encoding="utf-8-sig",newline="") as f:\n print(json.dumps(list(csv.reader(f,delimiter=";",strict=True)),ensure_ascii=False))', file], { encoding: 'utf8' }));
    assert.deepEqual(parsed.shift(), schema.fields, `${schema.file}: schema mismatch`);
    assert(parsed.length > 0, `${schema.file}: empty source`);
    const rows = parsed.map((row, r) => {
      assert.equal(row.length, schema.fields.length, `${schema.file}:${r + 2}: field count`);
      assert(row.every(v => !v.includes(String.fromCharCode(167))), `${schema.file}:${r + 2}: unexpected section symbol`);
      return row.map((v, c) => schema.dates.includes(c) ? serial(v, `${schema.file}:${r + 2}:${col(c)}`)
        : schema.numbers.includes(c) ? amount(v, `${schema.file}:${r + 2}:${col(c)}`, schema.nullableNumbers?.includes(c)) : v);
    });
    if (schema.account) {
      assert(rows.length > 1, `${schema.file}: no transactions after opening record`);
      assert.equal(rows[0][2], 'VORTRAG', `${schema.file}: opening record`);
      assert.equal(rows[0][0], serial('2025-03-31', 'opening date'));
      assert.equal(rows[0][5], 0);
      for (let i = 1; i < rows.length; i++) {
        assert(rows[i][0] >= serial('2025-04-01', 'start') && rows[i][0] <= serial('2026-07-08', 'end'), `${schema.file}: booking outside period`);
        assert(rows[i][0] >= rows[i - 1][0], `${schema.file}: source order not chronological`);
        near(rows[i][6], rows[i - 1][6] + rows[i][5], `${schema.file}:${i + 2}: running balance`);
      }
    }
    if (schema.name === 'OffenePosten') rows.forEach((r, i) => near(r[6], r[4] - r[5], `${schema.file}:${i + 2}: balance`));
    if (['OffenePosten', 'Inventar'].includes(schema.name)) assert.equal(new Set(rows.map(r => r[0])).size, rows.length, `${schema.file}: duplicate identifier`);
    sources.push({ ...schema, text, rows, sha256: hash(text) });
  }
  return sources;
}

function base(book, source, widths, title, owner, period) {
  const sheet = book.wb.worksheets.getItem(source.name);
  const last = FIRST + source.rows.length - 1;
  const endCol = col(widths.length - 1);
  sheet.showGridLines = false;
  sheet.tabColor = C.green;
  sheet.getRange(`A1:${endCol}${last}`).format = {
    font: { name: 'Arial', size: 11, color: C.ink }, verticalAlignment: 'center', rowHeight: 24,
  };
  widths.forEach((w, i) => { sheet.getRange(`${col(i)}1:${col(i)}${last}`).format.columnWidthPx = w; });
  sheet.getRange(`A1:${endCol}1`).format.rowHeight = 9;
  sheet.getRange(`A2:${endCol}2`).format.rowHeight = 30;
  set(sheet, 'A2', title);
  sheet.getRange('A2').format.font = { name: 'Arial', size: 16, bold: true, color: C.green };
  set(sheet, 'A3', owner);
  set(sheet, 'A4', period);
  sheet.getRange(`A4:${endCol}4`).format.borders = { bottom: { style: 'thin', color: C.line } };
  set(sheet, 'A7', `Quelle: zahlenwerk/${source.file}`);
  sheet.getRange('A7').format.font = { name: 'Arial', size: 11, italic: true, color: C.gray };
  sheet.getRange(`A8:${endCol}8`).format.rowHeight = 8;
  sheet.getRange(`A${FIRST}:${endCol}${last}`).values = source.rows.map(row => row.map(v => typeof v === 'string' && v.startsWith('=') ? `'${v}` : v));
  const meta = { source, sheet, last, endCol, widths, formulas: {}, expected: {}, paperSize: source.name === 'Jahreszahlen' ? '9' : '8' };
  book.sheets.push(meta);
  return meta;
}

function table(meta, headers) {
  const { sheet, source, last, endCol, widths } = meta;
  sheet.getRange(`A${HEADER}:${endCol}${HEADER}`).values = [headers];
  const name = `Bergmann_${source.name}`;
  sheet.tables.add(`A${HEADER}:${endCol}${last}`, true, name).showFilterButton = true;
  sheet.getRange(`A${HEADER}:${endCol}${HEADER}`).format = {
    fill: C.green, font: { name: 'Arial', size: 11, bold: true, color: C.white },
    horizontalAlignment: 'center', verticalAlignment: 'center', wrapText: true, rowHeight: 38,
    borders: { insideVertical: { style: 'thin', color: C.white } },
  };
  sheet.getRange(`A${FIRST}:${endCol}${last}`).format.wrapText = true;
  for (let r = FIRST; r <= last; r++) {
    if ((r - FIRST) % 2 === 0) sheet.getRange(`A${r}:${endCol}${r}`).format.fill = C.pale;
    const row = source.rows[r - FIRST];
    const lines = Math.max(...row.map((v, c) => {
      if (typeof v !== 'string') return 1;
      const capacity = Math.max(8, Math.floor((widths[c] - 16) / 7.2));
      return v.split('\n').reduce((n, line) => n + Math.max(1, Math.ceil(line.length / capacity)), 0);
    }));
    sheet.getRange(`A${r}:${endCol}${r}`).format.rowHeight = Math.max(28, lines * 15 + 8);
  }
  for (const c of source.numbers) {
    sheet.getRange(`${col(c)}${FIRST}:${col(c)}${last}`).setNumberFormat(EUR);
    sheet.getRange(`${col(c)}${FIRST}:${col(c)}${last}`).format.horizontalAlignment = 'right';
    sheet.getRange(`${col(c)}${FIRST}:${col(c)}${last}`).format.wrapText = false;
  }
  for (const c of source.dates) {
    sheet.getRange(`${col(c)}${FIRST}:${col(c)}${last}`).setNumberFormat(DATE);
    sheet.getRange(`${col(c)}${FIRST}:${col(c)}${last}`).format.horizontalAlignment = 'center';
    sheet.getRange(`${col(c)}${FIRST}:${col(c)}${last}`).format.wrapText = false;
  }
  sheet.freezePanes.freezeRows(HEADER);
  sheet.freezePanes.freezeColumns(1);
}

function formula(meta, address, expression, expected) {
  meta.sheet.getRange(address).formulas = [[expression]];
  meta.sheet.getRange(address).setNumberFormat(EUR);
  meta.sheet.getRange(address).format = { horizontalAlignment: 'right', font: { name: 'Arial', size: 11, bold: true, color: C.ink } };
  meta.formulas[address] = expression.slice(1);
  meta.expected[address] = expected;
}

function buildAccounts(sources) {
  const book = { wb: Workbook.create(), file: 'Kontoumsaetze_2025_2026.xlsx', sheets: [] };
  sources.forEach(s => book.wb.worksheets.add(s.name));
  for (const source of sources) {
    const m = base(book, source, [126, 126, 204, 232, 310, 132, 132, 330], 'Kontoumsätze 2025/2026', `Konto ${source.name}. ${source.owner}`, 'Familie Bergmann, Potsdam. Buchungen 01.04.2025 bis 08.07.2026 mit Vortrag zum 31.03.2025.');
    table(m, ['Buchungstag', 'Valuta', 'Referenz', 'Auftraggeber / Empfänger', 'Buchungstext', 'Betrag EUR', 'Saldo EUR', 'Belegdatei']);
    set(m.sheet, 'A6', 'Eingänge EUR');
    set(m.sheet, 'D6', 'Ausgänge EUR');
    set(m.sheet, 'G6', 'Endsaldo EUR');
    formula(m, 'B6', `=SUMIFS(F${FIRST}:F${m.last},F${FIRST}:F${m.last},">0")`, sum(source.rows.map(r => Math.max(0, r[5]))));
    formula(m, 'E6', `=SUMIFS(F${FIRST}:F${m.last},F${FIRST}:F${m.last},"<0")`, sum(source.rows.map(r => Math.min(0, r[5]))));
    set(m.sheet, 'H6', source.rows.at(-1)[6]);
    m.sheet.getRange('H6').setNumberFormat(EUR);
    m.sheet.getRange('H6').format.horizontalAlignment = 'right';
    m.sheet.getRange(`A${FIRST}:H${FIRST}`).format.font = { name: 'Arial', size: 11, italic: true, color: C.gray };
  }
  return book;
}

function buildBusiness(sources) {
  const book = { wb: Workbook.create(), file: 'Betriebsunterlagen_2023_2026.xlsx', sheets: [] };
  sources.forEach(s => book.wb.worksheets.add(s.name));
  const e = base(book, sources[0], [340, 146, 146, 146, 350], 'Betriebszahlen 2023 bis 2025', 'Jonas Bergmann, Potsdam', 'Betriebswirtschaftliche Mehrjahresübersicht. Nettoangaben in EUR, ohne Umsatzsteuerbewegungen.');
  table(e, ['Position', '2023 EUR', '2024 EUR', '2025 EUR', 'Belegdatei']);
  set(e.sheet, 'A6', 'Ergebnis EUR');
  for (const [i, year] of [[1, 2023], [2, 2024], [3, 2025]]) {
    set(e.sheet, `${col(i)}5`, year);
    e.sheet.getRange(`${col(i)}5`).format.horizontalAlignment = 'right';
    formula(e, `${col(i)}6`, `=SUM(${col(i)}${FIRST}:${col(i)}${e.last})`, sum(e.source.rows.map(r => r[i])));
  }
  const o = base(book, sources[1], [160, 130, 130, 215, 133, 133, 133, 265, 330], 'Offene Posten', 'Jonas Bergmann, Potsdam', 'Stand 08.07.2026. Rechnungsbeträge und Zahlungen in EUR.');
  table(o, ['Rechnungs-\nnummer', 'Rechnungs-\ndatum', 'Fälligkeit', 'Auftraggeber', 'Brutto EUR', 'Bezahlt EUR', 'Rest EUR', 'Bemerkung', 'Belegdatei']);
  set(o.sheet, 'A6', 'Summen EUR');
  for (const [i, label] of [[4, 'Brutto'], [5, 'Bezahlt'], [6, 'Rest']]) {
    set(o.sheet, `${col(i)}5`, label);
    o.sheet.getRange(`${col(i)}5`).format.horizontalAlignment = 'right';
    formula(o, `${col(i)}6`, `=SUM(${col(i)}${FIRST}:${col(i)}${o.last})`, sum(o.source.rows.map(r => r[i])));
  }
  const inv = base(book, sources[2], [154, 264, 132, 150, 144, 152, 280, 330], 'Inventarverzeichnis', 'Jonas Bergmann, Potsdam', 'Stand 08.07.2026. Anschaffungskosten, Buchwerte und Händlerangebote in EUR.');
  table(inv, ['Inventarnummer', 'Gegenstand', 'Anschaffung', 'Anschaffungs-\nkosten EUR', 'Buchwert EUR', 'Händlerangebot\nEUR', 'Bemerkung', 'Belegdatei']);
  return book;
}

function expectedValues(book) {
  return Object.fromEntries(book.sheets.flatMap(m => Object.entries(m.expected).map(([a, n]) => [`${m.source.name}!${a}`, n])));
}
function checkArtifact(book) {
  for (const m of book.sheets) for (const [a, n] of Object.entries(m.expected)) near(get(m.sheet, a), n, `${m.source.name}!${a}`);
}

const el = (name, attributes = {}, elements = []) => ({ type: 'element', name, attributes, elements });
const txt = text => ({ type: 'text', text: String(text) });
const children = (root, name) => (root?.elements || []).filter(e => e.type === 'element' && e.name === name);
const child = (root, name) => children(root, name)[0];
const rootOf = doc => doc.elements.find(e => e.type === 'element');
const content = node => (node?.elements || []).map(e => e.type === 'text' ? e.text : content(e)).join('');
async function readXml(zip, name) {
  const doc = xml.xml2js(await zip.file(name).async('string'));
  const root = rootOf(doc);
  const prefix = root.name.includes(':') ? root.name.split(':')[0] : null;
  if (prefix && root.attributes?.[`xmlns:${prefix}`] === 'http://schemas.openxmlformats.org/spreadsheetml/2006/main') {
    const strip = node => { if (node.name?.startsWith(`${prefix}:`)) node.name = node.name.slice(prefix.length + 1); for (const e of node.elements || []) strip(e); };
    strip(root);
    root.attributes.xmlns = root.attributes[`xmlns:${prefix}`];
    delete root.attributes[`xmlns:${prefix}`];
  }
  return doc;
}
const writeXml = (zip, name, doc) => zip.file(name, xml.js2xml(doc, { compact: false }));
function replace(root, name, node, order) {
  root.elements = (root.elements || []).filter(e => e.name !== name);
  const i = root.elements.findIndex(e => order.indexOf(e.name) > order.indexOf(name));
  root.elements.splice(i < 0 ? root.elements.length : i, 0, node);
}

// Only print settings and native freeze-pane coordinates lack a sufficient public authoring API.
async function packagePrint(file, book) {
  const zip = await JSZip.loadAsync(await fs.readFile(file));
  const doc = await readXml(zip, 'xl/workbook.xml');
  const root = rootOf(doc);
  const defs = child(root, 'definedNames') || el('definedNames');
  defs.elements = (defs.elements || []).filter(e => !['_xlnm.Print_Area', '_xlnm.Print_Titles'].includes(e.attributes?.name));
  book.sheets.forEach((m, i) => {
    defs.elements.push(el('definedName', { name: '_xlnm.Print_Area', localSheetId: String(i) }, [txt(`'${m.source.name}'!$A$1:$${m.endCol}$${m.last}`)]));
    defs.elements.push(el('definedName', { name: '_xlnm.Print_Titles', localSheetId: String(i) }, [txt(`'${m.source.name}'!$1:$${HEADER}`)]));
  });
  replace(root, 'definedNames', defs, ['fileVersion', 'fileSharing', 'workbookPr', 'workbookProtection', 'bookViews', 'sheets', 'functionGroups', 'externalReferences', 'definedNames', 'calcPr', 'extLst']);
  writeXml(zip, 'xl/workbook.xml', doc);
  const order = ['sheetPr', 'dimension', 'sheetViews', 'sheetFormatPr', 'cols', 'sheetData', 'sheetCalcPr', 'sheetProtection', 'protectedRanges', 'scenarios', 'autoFilter', 'sortState', 'dataConsolidate', 'customSheetViews', 'mergeCells', 'phoneticPr', 'conditionalFormatting', 'dataValidations', 'hyperlinks', 'printOptions', 'pageMargins', 'pageSetup', 'headerFooter', 'rowBreaks', 'colBreaks', 'customProperties', 'cellWatches', 'ignoredErrors', 'smartTags', 'drawing', 'legacyDrawing', 'legacyDrawingHF', 'picture', 'oleObjects', 'controls', 'webPublishItems', 'tableParts', 'extLst'];
  for (const [i, m] of book.sheets.entries()) {
    const name = `xl/worksheets/sheet${i + 1}.xml`;
    const d = await readXml(zip, name);
    const r = rootOf(d);
    const pr = child(r, 'sheetPr') || el('sheetPr');
    replace(pr, 'pageSetUpPr', el('pageSetUpPr', { fitToPage: '1' }), ['tabColor', 'outlinePr', 'pageSetUpPr']);
    replace(r, 'sheetPr', pr, order);
    replace(r, 'printOptions', el('printOptions', { gridLines: '0', headings: '0' }), order);
    replace(r, 'pageMargins', el('pageMargins', { left: '0.3', right: '0.3', top: '0.35', bottom: '0.4', header: '0.15', footer: '0.18' }), order);
    replace(r, 'pageSetup', el('pageSetup', { paperSize: m.paperSize, orientation: 'landscape', fitToWidth: '1', fitToHeight: '0' }), order);
    replace(r, 'headerFooter', el('headerFooter', {}, [el('oddFooter', {}, [txt(`&LFamilie Bergmann, Potsdam&C${m.source.name}&RSeite &P von &N`)])]), order);
    const view = child(child(r, 'sheetViews'), 'sheetView');
    if (view) {
      view.attributes.showGridLines = '0';
      const pane = child(view, 'pane');
      if (pane) Object.assign(pane.attributes, { ySplit: String(HEADER), xSplit: '1', topLeftCell: `B${FIRST}`, state: 'frozen', activePane: 'bottomRight' });
    }
    writeXml(zip, name, d);
  }
  await fs.writeFile(file, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
}

async function verifySaved(file, book, expected, original = true) {
  const zip = await JSZip.loadAsync(await fs.readFile(file));
  const strings = zip.file('xl/sharedStrings.xml') ? children(rootOf(await readXml(zip, 'xl/sharedStrings.xml')), 'si').map(content) : [];
  const cells = {}, formulas = {};
  const names = children(child(rootOf(await readXml(zip, 'xl/workbook.xml')), 'sheets'), 'sheet').map(e => e.attributes.name);
  assert.deepEqual(names, book.sheets.map(m => m.source.name));
  for (const [i, m] of book.sheets.entries()) {
    const root = rootOf(await readXml(zip, `xl/worksheets/sheet${i + 1}.xml`));
    for (const row of children(child(root, 'sheetData'), 'row')) for (const c of children(row, 'c')) {
      const key = `${m.source.name}!${c.attributes.r}`;
      const raw = content(child(c, 'v'));
      const t = c.attributes.t;
      cells[key] = t === 's' ? strings[Number(raw)] : t === 'inlineStr' ? content(child(c, 'is')) : t === 'str' || t === 'e' ? raw : raw === '' ? null : Number(raw);
      assert.notEqual(t, 'e', `${key}: ${raw}`);
      if (child(c, 'f')) {
        formulas[key] = content(child(c, 'f'));
        assert(raw !== '' && Number.isFinite(Number(raw)), `${key}: empty/non-numeric formula cache`);
      }
    }
    assert.equal(child(root, 'pageSetup')?.attributes.orientation, 'landscape');
    const pane = child(child(child(root, 'sheetViews'), 'sheetView'), 'pane');
    assert.equal(Number(pane?.attributes.ySplit), HEADER);
    assert.equal(Number(pane?.attributes.xSplit), 1);
    for (const [a, f] of Object.entries(m.formulas)) assert.equal(formulas[`${m.source.name}!${a}`], f);
    if (original) for (const [r, row] of m.source.rows.entries()) for (const [c, v] of row.entries()) {
      const actual = cells[`${m.source.name}!${col(c)}${FIRST + r}`];
      const label = `${m.source.name}!${col(c)}${FIRST + r}: source mismatch`;
      if (v === '' || v === null) assert(actual === '' || actual === null || actual === undefined, label);
      else assert.equal(actual, v, label);
    }
  }
  assert.deepEqual(Object.keys(formulas).sort(), Object.keys(expected).sort(), 'Unexpected or missing formula cells');
  for (const [key, n] of Object.entries(expected)) near(cells[key], n, `Saved ${key}`);
  const tables = Object.keys(zip.files).filter(n => /^xl\/tables\/table\d+\.xml$/.test(n));
  if (original) {
    assert.equal(tables.length, 3);
    for (const f of tables) assert((await zip.file(f).async('string')).includes('autoFilter'), `Missing table filters: ${f}`);
  }
  return { checkedSourceRows: original ? sum(book.sheets.map(m => m.source.rows.length)) : 0, formulaCells: formulas, expected };
}

function convert(input, dir, format, profile) {
  return execFileSync(soffice, [`-env:UserInstallation=${pathToFileURL(profile).href}`, '--headless', '--convert-to', format, '--outdir', dir, input], { encoding: 'utf8', timeout: 120000 });
}

async function nativeMutation(book, dir) {
  const expected = expectedValues(book);
  const restore = [];
  const mutations = [];
  function change(m, address, value, totals) {
    restore.push([m.sheet, address, get(m.sheet, address)]);
    set(m.sheet, address, value);
    for (const [a, delta] of Object.entries(totals)) expected[`${m.source.name}!${a}`] += delta;
    mutations.push({ sheet: m.source.name, address, value });
  }
  if (book.sheets[0].source.account) {
    for (const m of book.sheets) {
      const row = m.source.rows[1];
      const replacement = row[5] >= 0 ? -37.25 : 37.25;
      change(m, `F${FIRST + 1}`, replacement, { B6: Math.max(0, replacement) - Math.max(0, row[5]), E6: Math.min(0, replacement) - Math.min(0, row[5]) });
    }
  } else {
    const [e, o] = book.sheets;
    change(e, `B${FIRST}`, e.source.rows[0][1] + 17.35, { B6: 17.35 });
    change(e, `C${FIRST}`, 0, { C6: -e.source.rows[0][2] });
    change(e, `D${e.last}`, e.source.rows.at(-1)[3] - 19.25, { D6: -19.25 });
    change(o, `F${FIRST}`, o.source.rows[0][5] + 25, { F6: 25 });
  }
  try {
    for (const [key, n] of Object.entries(expected)) {
      const [s, a] = key.split('!');
      near(get(book.wb.worksheets.getItem(s), a), n, `Changed ${key}`);
    }
    const file = path.join(dir, 'mutation.xlsx');
    await (await SpreadsheetFile.exportXlsx(book.wb)).save(file);
    await packagePrint(file, book);
    const native = path.join(dir, 'native-mutation');
    await fs.mkdir(native, { recursive: true });
    convert(file, native, 'xlsx:Calc MS Excel 2007 XML', path.join(dir, 'lo-profile'));
    await verifySaved(path.join(native, 'mutation.xlsx'), book, expected, false);
  } finally { for (const [s, a, v] of restore) set(s, a, v); }
  return mutations;
}

async function finalBook(book) {
  const dir = path.join(qa, path.basename(book.file, '.xlsx'));
  await fs.mkdir(dir, { recursive: true });
  const mutations = await nativeMutation(book, dir);
  book.wb.recalculate();
  checkArtifact(book);
  const errors = (await book.wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!', options: { useRegex: true, maxResults: 100 }, maxChars: 6000 })).ndjson;
  const inspections = [];
  for (const m of book.sheets) {
    inspections.push((await book.wb.inspect({ kind: 'table', range: `'${m.source.name}'!A5:${m.endCol}${Math.min(m.last, 13)}`, include: 'values,formulas', tableMaxRows: 12, tableMaxCols: 9, maxChars: 4500 })).ndjson);
    for (const [tag, range] of [['top', `A1:${m.endCol}${Math.min(m.last, FIRST + 4)}`], ['tail', `A${Math.max(FIRST, m.last - 5)}:${m.endCol}${m.last}`]]) {
      const image = await book.wb.render({ sheetName: m.source.name, range, scale: 1.5, format: 'png' });
      await fs.writeFile(path.join(dir, `${m.source.name}-${tag}.png`), new Uint8Array(await image.arrayBuffer()));
    }
  }
  await fs.writeFile(path.join(dir, 'artifact-inspect.ndjson'), [...inspections, errors].join('\n'));
  const staged = path.join(dir, book.file);
  await (await SpreadsheetFile.exportXlsx(book.wb)).save(staged);
  await packagePrint(staged, book);
  const expected = expectedValues(book);
  const exported = await verifySaved(staged, book, expected);
  const nativeDir = path.join(dir, 'native');
  await fs.mkdir(nativeDir, { recursive: true });
  const log = [convert(staged, nativeDir, 'xlsx:Calc MS Excel 2007 XML', path.join(dir, 'lo-profile'))];
  const nativeFile = path.join(nativeDir, book.file);
  await verifySaved(nativeFile, book, expected, false);
  log.push(convert(staged, dir, 'pdf:calc_pdf_Export', path.join(dir, 'lo-profile')));
  const pdf = path.join(dir, book.file.replace(/\.xlsx$/, '.pdf'));
  const pages = JSON.parse(execFileSync(python, ['-c',
    'from pypdf import PdfReader\nimport json,sys\nr=PdfReader(sys.argv[1])\nprint(json.dumps([{"page":i+1,"width":float(p.mediabox.width),"height":float(p.mediabox.height),"text":p.extract_text()} for i,p in enumerate(r.pages)],ensure_ascii=False))', pdf], { encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 }));
  assert(pages.length >= 3, 'Missing native PDF sheet pages');
  assert(pages.every(p => p.width > p.height && p.text.trim() && !p.text.includes('####')), 'Invalid native PDF page');
  for (const m of book.sheets) {
    const needles = [m.source.rows[0][m.source.account ? 2 : 0], m.source.rows.at(-1)[m.source.account ? 2 : 0]];
    for (const needle of needles) assert(pages.some(p => p.text.replace(/\s/g, '').includes(String(needle).replace(/\s/g, ''))), `Native PDF missing first/last record: ${needle}`);
  }
  execFileSync(pdftoppm, ['-r', '90', '-png', pdf, path.join(dir, 'native-page')], { timeout: 120000, maxBuffer: 4 * 1024 * 1024 });
  await fs.writeFile(path.join(dir, 'native-conversion.log'), log.join('\n'));
  await fs.writeFile(path.join(dir, 'native-pages.json'), JSON.stringify(pages, null, 2));
  // Keep native Excel tables and styles from Artifact Tool; both native passes above independently verified the caches.
  return { book, staged, report: { file: path.join(outputDir, book.file), sheets: book.sheets.map(m => ({ name: m.source.name, rows: m.source.rows.length, dataRange: `A${FIRST}:${m.endCol}${m.last}` })), ...exported, mutations, nativePdfPages: pages.length, qa: dir } };
}

const sources = await loadSources();
const books = [buildAccounts(sources.slice(0, 3)), buildBusiness(sources.slice(3))];
const ready = [];
for (const book of books) ready.push(await finalBook(book));
for (const s of sources) assert.equal(await fs.readFile(path.join(sourceDir, s.file), 'utf8'), s.text, `Source changed during build: ${s.file}`);
await fs.mkdir(outputDir, { recursive: true });
for (const result of ready) {
  await fs.copyFile(result.staged, result.report.file);
  await verifySaved(result.report.file, result.book, expectedValues(result.book));
}
const report = { sources: sources.map(s => ({ file: s.file, sha256: s.sha256, rows: s.rows.length })), engine: 'Bundled LibreOffice', results: ready.map(r => r.report) };
await fs.writeFile(path.join(qa, 'qa-report.json'), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));

#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';

// Usage: bundled-node scripts/build-lindenhof-betriebsaufzeichnungen.mjs [repoRoot] [qaTmp]
const [repoArg, qaArg] = process.argv.slice(2);
const repo = path.resolve(repoArg || path.join(path.dirname(fileURLToPath(import.meta.url)), '..'));
const akte = path.join(repo, 'testakten/strassennutzung-poller-lieferzufahrt-lindenhof-muenster');
const filename = '30_betriebsaufzeichnungen_lindenhof.xlsx';
const qa = path.resolve(qaArg || await fs.mkdtemp(path.join(os.tmpdir(), 'lindenhof-xlsx-')));
assert(qa !== repo && !qa.startsWith(`${repo}${path.sep}`), 'QA directory must be outside the repository');
const dependencies = path.resolve(path.dirname(process.execPath), '../..');
const python = path.join(dependencies, 'python/bin/python3');
const soffice = path.join(dependencies, 'bin/override/soffice');
const pdftoppm = path.join(dependencies, 'bin/override/pdftoppm');
for (const file of [python, soffice, pdftoppm]) await fs.access(file);
await fs.mkdir(qa, { recursive: true });
const moduleLink = path.join(qa, 'node_modules');
try { await fs.lstat(moduleLink); }
catch { await fs.symlink(path.join(dependencies, 'node/node_modules'), moduleLink, 'dir'); }
const runtime = createRequire(path.join(qa, 'runtime.cjs'));
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(runtime.resolve('@oai/artifact-tool')).href);
const JSZip = runtime('jszip');
const xml = runtime('xml-js');

const FIRST = 8;
const HEADER = FIRST - 1;
const FONT = 'Arial';
const SIZE = 11;
const DATE = 'dd"."mm"."yyyy';
const TIME = 'hh:mm';
const STAMP = `${DATE} hh:mm`;
const C = { ink: '#25312E', green: '#35574B', pale: '#F1F5F2', line: '#CBD5CE', muted: '#56645D', white: '#FFFFFF' };
const col = index => String.fromCharCode(65 + index);
const sum = values => values.reduce((a, b) => a + b, 0);
const hash = text => createHash('sha256').update(text).digest('hex');
const put = (sheet, address, value) => { sheet.getRange(address).values = [[value]]; };
const get = (sheet, address) => sheet.getRange(address).values[0][0];
const near = (actual, expected, label) => assert(typeof actual === 'number' && Math.abs(actual - expected) < 1e-7, `${label}: ${actual} != ${expected}`);
const schemas = [
  {
    name: 'Lieferfahrten', table: 'Lindenhof_Lieferfahrten', file: '23_fahrtenbuch_2026-08-24_bis_09-08.csv',
    fields: ['Fahrt_ID', 'Datum', 'Ankunft', 'Betrieb', 'Fahrer', 'Fahrzeug', 'Zugang', 'Wartezeit_min', 'Zusatzentgelt_netto_EUR', 'Beleg', 'Notiz'],
    headers: ['Fahrt-ID', 'Datum', 'Ankunft', 'Betrieb', 'Fahrer', 'Fahrzeug', 'Zugang', 'Wartezeit\n(min)', 'Zusatz-\nentgelt\nnetto (EUR)', 'Beleg', 'Notiz'],
    types: ['text', 'date', 'time', 'text', 'text', 'text', 'text', 'integer', 'decimal', 'text', 'text'],
    widths: [57, 89, 62, 116, 94, 107, 99, 70, 97, 105, 192],
  },
  {
    name: 'Schlüsselvorgänge', table: 'Lindenhof_Schluesselvorgaenge', file: '24_schluesseljournal_2026-08-21_bis_09-22.csv',
    fields: ['Vorgang_ID', 'Datum', 'Uhrzeit', 'Schlüssel', 'Von', 'An', 'Vorgang', 'Rückgabe_bis', 'Notiz'],
    headers: ['Vorgang-ID', 'Datum', 'Uhrzeit', 'Schlüssel', 'Von', 'An', 'Vorgang', 'Rückgabe bis', 'Notiz'],
    types: ['text', 'date', 'time', 'text', 'text', 'text', 'text', 'datetime', 'text'],
    widths: [78, 89, 64, 77, 108, 116, 149, 161, 226],
  },
  {
    name: 'Beobachtungen', table: 'Lindenhof_Beobachtungen', file: '25_beobachtungen_lindenbogen_2026-08-24_bis_09-18.csv',
    fields: ['Beobachtung_ID', 'Datum', 'Von', 'Bis', 'Ort', 'Erfasser', 'Fahrzeuge_Anzahl', 'Restbreite_m', 'Beobachtung'],
    headers: ['Beobachtung-ID', 'Datum', 'Von', 'Bis', 'Ort', 'Erfasser', 'Fahrzeuge\n(Anzahl)', 'Restbreite\n(m)', 'Beobachtung', 'Dauer\n(min)'],
    types: ['text', 'date', 'time', 'time', 'text', 'text', 'integer', 'decimal', 'text'],
    widths: [98, 89, 62, 62, 143, 109, 78, 82, 246, 71],
  },
];

function dateSerial(value, label) {
  assert(/^\d{4}-\d{2}-\d{2}$/.test(value), `${label}: invalid date ${value}`);
  const date = new Date(`${value}T00:00:00Z`);
  assert(Number.isFinite(date.valueOf()) && date.toISOString().slice(0, 10) === value, `${label}: invalid date`);
  return (date.valueOf() - Date.UTC(1899, 11, 30)) / 86400000;
}
function timeSerial(value, label) {
  assert(/^(?:[01]\d|2[0-3]):[0-5]\d$/.test(value), `${label}: unsupported time ${value}`);
  const [h, m] = value.split(':').map(Number);
  return (60 * h + m) / 1440;
}
function typed(value, type, label) {
  if (value === '') return null;
  if (type === 'date') return dateSerial(value, label);
  if (type === 'time') return timeSerial(value, label);
  if (type === 'datetime') {
    assert(/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$/.test(value), `${label}: invalid datetime`);
    return dateSerial(value.slice(0, 10), label) + timeSerial(value.slice(11), label);
  }
  if (type === 'integer' || type === 'decimal') {
    assert((type === 'integer' ? /^\d+$/ : /^\d+,\d{2}$/).test(value), `${label}: invalid numeric value ${value}`);
    return Number(value.replace(',', '.'));
  }
  return value;
}
function restored(value, type, source) {
  if (value === null || value === undefined || value === '') return '';
  if (type === 'date') return new Date(Date.UTC(1899, 11, 30) + Math.round(value) * 86400000).toISOString().slice(0, 10);
  if (type === 'time') {
    const minutes = Math.round(value * 1440);
    return `${String(Math.floor(minutes / 60)).padStart(2, '0')}:${String(minutes % 60).padStart(2, '0')}`;
  }
  if (type === 'datetime') return `${restored(Math.floor(value), 'date')} ${restored(value - Math.floor(value), 'time')}`;
  if (type === 'decimal') return Number(value).toFixed(source.split(',')[1].length).replace('.', ',');
  return String(value);
}
async function loadSources() {
  const result = [];
  for (const schema of schemas) {
    const file = path.join(akte, schema.file);
    const text = await fs.readFile(file, 'utf8');
    // Python's strict CSV parser preserves quoted semicolons and blank fields.
    const parsed = JSON.parse(execFileSync(python, ['-c', 'import csv,json,sys\nwith open(sys.argv[1],encoding="utf-8-sig",newline="") as f:\n print(json.dumps(list(csv.reader(f,delimiter=";",strict=True)),ensure_ascii=False))', file], { encoding: 'utf8' }));
    assert.deepEqual(parsed.shift(), schema.fields, `${schema.file}: changed schema`);
    assert(parsed.length, `${schema.file}: no records`);
    assert.equal(new Set(parsed.map(row => row[0])).size, parsed.length, `${schema.file}: duplicate record ID`);
    const rows = parsed.map((row, r) => {
      assert.equal(row.length, schema.fields.length, `${schema.file}:${r + 2}: field count`);
      return row.map((value, c) => typed(value, schema.types[c], `${schema.file}:${r + 2}:${schema.fields[c]}`));
    });
    result.push({ ...schema, text, raw: parsed, rows, sha256: hash(text) });
  }
  return result;
}

function setFormula(meta, address, formula, expected, format = '0') {
  meta.sheet.getRange(address).formulas = [[formula]];
  meta.sheet.getRange(address).setNumberFormat(format);
  meta.formulas[address] = formula.slice(1);
  meta.expected[address] = expected;
}
function buildSheet(wb, source) {
  const sheet = wb.worksheets.add(source.name);
  const last = FIRST + source.rows.length - 1;
  const endCol = col(source.headers.length - 1);
  const meta = { sheet, source, last, endCol, formulas: {}, expected: {} };
  sheet.showGridLines = false;
  sheet.getRange(`A1:${endCol}${last}`).format = {
    font: { name: FONT, size: SIZE, color: C.ink }, rowHeight: 20,
    verticalAlignment: 'center', horizontalAlignment: 'left',
  };
  source.widths.forEach((width, c) => { sheet.getRange(`${col(c)}1:${col(c)}${last}`).format.columnWidthPx = width * 1.25; });
  sheet.getRange(`A1:${endCol}1`).format.rowHeight = 8;
  sheet.getRange(`A2:${endCol}2`).format.rowHeight = 25;
  put(sheet, 'A2', source.name);
  sheet.getRange('A2').format.font = { name: FONT, size: 15, bold: true, color: C.green };
  put(sheet, 'A3', 'Lindenhof Vorrat, Münster');
  put(sheet, 'A4', `Quelle: ${source.file}`);
  sheet.getRange('A4').format.font = { name: FONT, size: SIZE, italic: true, color: C.muted };
  sheet.getRange(`A5:${endCol}5`).format = { rowHeight: 6, borders: { bottom: { style: 'thin', color: C.line } } };
  sheet.getRange(`A6:${endCol}6`).format.rowHeight = 8;
  sheet.getRange(`A${HEADER}:${endCol}${HEADER}`).values = [source.headers];
  sheet.getRange(`A${FIRST}:${col(source.fields.length - 1)}${last}`).values = source.rows.map(row => row.map(value => typeof value === 'string' && value.startsWith('=') ? `'${value}` : value));
  const table = sheet.tables.add(`A${HEADER}:${endCol}${last}`, true, source.table);
  table.showFilterButton = true;
  sheet.getRange(`A${HEADER}:${endCol}${HEADER}`).format = {
    fill: C.green, font: { name: FONT, size: SIZE, bold: true, color: C.white },
    horizontalAlignment: 'center', verticalAlignment: 'center', wrapText: true, rowHeight: 52,
    borders: { insideVertical: { style: 'thin', color: C.white } },
  };
  sheet.getRange(`A${FIRST}:${endCol}${last}`).format.wrapText = true;
  for (const [i, row] of source.rows.entries()) {
    const r = FIRST + i;
    const lines = Math.max(...row.map((value, c) => {
      if (source.types[c] !== 'text' || typeof value !== 'string') return 1;
      const capacity = Math.max(5, Math.floor((source.widths[c] - 13) / 7.2));
      return value.split('\n').reduce((n, line) => n + Math.max(1, Math.ceil(line.length / capacity)), 0);
    }));
    sheet.getRange(`A${r}:${endCol}${r}`).format.rowHeight = Math.max(34, 15 * lines + 10);
    if (i % 2 === 0) sheet.getRange(`A${r}:${endCol}${r}`).format.fill = C.pale;
  }
  for (const [c, type] of source.types.entries()) {
    const range = sheet.getRange(`${col(c)}${FIRST}:${col(c)}${last}`);
    if (type === 'text') {
      range.setNumberFormat('" "@');
      continue;
    }
    range.format.wrapText = false;
    range.format.horizontalAlignment = 'right';
    range.setNumberFormat(`${{ date: DATE, time: TIME, datetime: STAMP, integer: '0', decimal: '0.00' }[type]}"  "`);
  }
  if (source.name === 'Lieferfahrten') {
    put(sheet, 'G3', 'Summen');
    put(sheet, 'H3', 'Minuten');
    put(sheet, 'I3', 'Netto EUR');
    setFormula(meta, 'H4', `=SUM(H${FIRST}:H${last})`, sum(source.rows.map(row => row[7])));
    setFormula(meta, 'I4', `=SUM(I${FIRST}:I${last})`, sum(source.rows.map(row => row[8])), '0.00');
    sheet.getRange('H3:I4').format.horizontalAlignment = 'right';
    sheet.getRange('H4:I4').format.font = { name: FONT, size: SIZE, bold: true, color: C.ink };
  }
  if (source.name === 'Beobachtungen') {
    for (const [i, row] of source.rows.entries()) {
      assert(row[2] !== null && row[3] !== null && row[3] >= row[2], `${source.file}:${i + 2}: duration requires same-day start and end`);
      const r = FIRST + i;
      setFormula(meta, `J${r}`, `=IF(AND(ISNUMBER(C${r}),ISNUMBER(D${r}),D${r}>=C${r}),ROUND((D${r}-C${r})*1440,0),"")`, Math.round((row[3] - row[2]) * 1440));
    }
    sheet.getRange(`J${FIRST}:J${last}`).format.horizontalAlignment = 'right';
  }
  sheet.freezePanes.freezeRows(HEADER);
  sheet.freezePanes.freezeColumns(2);
  return meta;
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

// Match the reference builder: package-only print settings, no cell authoring in XML.
async function packagePrint(file, sheets) {
  const zip = await JSZip.loadAsync(await fs.readFile(file));
  const doc = await readXml(zip, 'xl/workbook.xml');
  const root = rootOf(doc);
  const defs = child(root, 'definedNames') || el('definedNames');
  defs.elements = (defs.elements || []).filter(e => !['_xlnm.Print_Area', '_xlnm.Print_Titles'].includes(e.attributes?.name));
  for (const [i, m] of sheets.entries()) {
    defs.elements.push(el('definedName', { name: '_xlnm.Print_Area', localSheetId: String(i) }, [txt(`'${m.source.name}'!$A$1:$${m.endCol}$${m.last}`)]));
    defs.elements.push(el('definedName', { name: '_xlnm.Print_Titles', localSheetId: String(i) }, [txt(`'${m.source.name}'!$1:$${HEADER}`)]));
  }
  replace(root, 'definedNames', defs, ['fileVersion', 'fileSharing', 'workbookPr', 'workbookProtection', 'bookViews', 'sheets', 'functionGroups', 'externalReferences', 'definedNames', 'calcPr', 'extLst']);
  writeXml(zip, 'xl/workbook.xml', doc);
  const order = ['sheetPr', 'dimension', 'sheetViews', 'sheetFormatPr', 'cols', 'sheetData', 'sheetCalcPr', 'sheetProtection', 'protectedRanges', 'scenarios', 'autoFilter', 'sortState', 'dataConsolidate', 'customSheetViews', 'mergeCells', 'phoneticPr', 'conditionalFormatting', 'dataValidations', 'hyperlinks', 'printOptions', 'pageMargins', 'pageSetup', 'headerFooter', 'rowBreaks', 'colBreaks', 'customProperties', 'cellWatches', 'ignoredErrors', 'smartTags', 'drawing', 'legacyDrawing', 'legacyDrawingHF', 'picture', 'oleObjects', 'controls', 'webPublishItems', 'tableParts', 'extLst'];
  for (const [i, m] of sheets.entries()) {
    const name = `xl/worksheets/sheet${i + 1}.xml`;
    const d = await readXml(zip, name);
    const r = rootOf(d);
    const pr = child(r, 'sheetPr') || el('sheetPr');
    replace(pr, 'pageSetUpPr', el('pageSetUpPr', { fitToPage: '1' }), ['tabColor', 'outlinePr', 'pageSetUpPr']);
    replace(r, 'sheetPr', pr, order);
    replace(r, 'printOptions', el('printOptions', { gridLines: '0', headings: '0' }), order);
    replace(r, 'pageMargins', el('pageMargins', { left: '0.25', right: '0.25', top: '0.3', bottom: '0.4', header: '0.12', footer: '0.18' }), order);
    replace(r, 'pageSetup', el('pageSetup', { paperSize: '9', orientation: 'landscape', fitToWidth: '1', fitToHeight: '0' }), order);
    replace(r, 'headerFooter', el('headerFooter', {}, [el('oddFooter', {}, [txt(`&LLindenhof Vorrat, Münster&C${m.source.name}&RSeite &P von &N`)])]), order);
    const view = child(child(r, 'sheetViews'), 'sheetView');
    assert(view, `${m.source.name}: missing sheet view`);
    view.attributes.showGridLines = '0';
    const pane = child(view, 'pane');
    assert(pane, `${m.source.name}: missing freeze panes`);
    Object.assign(pane.attributes, { ySplit: String(HEADER), xSplit: '2', topLeftCell: `C${FIRST}`, state: 'frozen', activePane: 'bottomRight' });
    writeXml(zip, name, d);
  }
  await fs.writeFile(file, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
}

async function verifySaved(file, sheets, native = false) {
  const zip = await JSZip.loadAsync(await fs.readFile(file));
  const strings = zip.file('xl/sharedStrings.xml') ? children(rootOf(await readXml(zip, 'xl/sharedStrings.xml')), 'si').map(content) : [];
  const book = rootOf(await readXml(zip, 'xl/workbook.xml'));
  assert.deepEqual(children(child(book, 'sheets'), 'sheet').map(e => e.attributes.name), sheets.map(m => m.source.name));
  let sourceCells = 0;
  const caches = {};
  for (const [i, m] of sheets.entries()) {
    const root = rootOf(await readXml(zip, `xl/worksheets/sheet${i + 1}.xml`));
    const cells = {}, formulas = {};
    for (const row of children(child(root, 'sheetData'), 'row')) for (const c of children(row, 'c')) {
      const a = c.attributes.r;
      const raw = content(child(c, 'v'));
      const t = c.attributes.t;
      cells[a] = t === 's' ? strings[Number(raw)] : t === 'inlineStr' ? content(child(c, 'is')) : t === 'str' || t === 'e' ? raw : raw === '' ? null : Number(raw);
      assert.notEqual(t, 'e', `${m.source.name}!${a}: ${raw}`);
      if (child(c, 'f')) {
        formulas[a] = content(child(c, 'f'));
        assert(raw !== '' && Number.isFinite(Number(raw)), `${m.source.name}!${a}: missing numeric formula cache`);
        caches[`${m.source.name}!${a}`] = Number(raw);
      }
    }
    assert.deepEqual(formulas, m.formulas, `${m.source.name}: changed formula text`);
    for (const [a, expected] of Object.entries(m.expected)) near(cells[a], expected, `${m.source.name}!${a}`);
    for (const [r, row] of m.source.raw.entries()) for (const [c, value] of row.entries()) {
      const a = `${col(c)}${FIRST + r}`;
      const type = m.source.types[c];
      if (value && type !== 'text') assert.equal(typeof cells[a], 'number', `${m.source.name}!${a}: not numeric`);
      assert.equal(restored(cells[a], type, value), value, `${m.source.name}!${a}: CSV source field differs`);
      sourceCells++;
    }
    for (const [c, header] of m.source.headers.entries()) assert.equal(cells[`${col(c)}${HEADER}`], header, `${m.source.name}: header ${c}`);
    const setup = child(root, 'pageSetup')?.attributes;
    assert.equal(setup?.paperSize, '9', `${m.source.name}: not A4`);
    assert.equal(setup.orientation, 'landscape');
    const pane = child(child(child(root, 'sheetViews'), 'sheetView'), 'pane')?.attributes;
    assert.equal(Number(pane?.xSplit), 2);
    assert.equal(Number(pane?.ySplit), HEADER);
  }
  if (!native) {
    const tables = Object.keys(zip.files).filter(n => /^xl\/tables\/table\d+\.xml$/.test(n));
    assert.equal(tables.length, sheets.length);
    for (const [i, table] of tables.sort().entries()) {
      const t = rootOf(await readXml(zip, table));
      assert.equal(t.attributes.ref, `A${HEADER}:${sheets[i].endCol}${sheets[i].last}`);
      assert(child(t, 'autoFilter'), `${table}: no native filter`);
    }
    const defs = children(child(book, 'definedNames'), 'definedName');
    for (const i of sheets.keys()) for (const name of ['_xlnm.Print_Titles', '_xlnm.Print_Area']) assert(defs.some(d => d.attributes.name === name && Number(d.attributes.localSheetId) === i), `${name}: sheet ${i}`);
  }
  return { sourceRows: sum(sheets.map(m => m.source.rows.length)), sourceCells, formulaCache: caches };
}

function mutationTests(wb, sheets) {
  const cases = [];
  const [rides, , observations] = sheets;
  function change(meta, address, value, checks) {
    const original = get(meta.sheet, address);
    try {
      put(meta.sheet, address, value);
      wb.recalculate();
      for (const [cell, expected] of Object.entries(checks)) {
        const actual = get(meta.sheet, cell);
        if (typeof expected === 'number') near(actual, expected, `${meta.source.name}!${cell}: mutation`);
        else assert.equal(actual, expected, `${meta.source.name}!${cell}: mutation`);
      }
      cases.push({ sheet: meta.source.name, address, value, checked: checks });
    } finally { put(meta.sheet, address, original); }
  }
  change(rides, 'H8', 0, { H4: rides.expected.H4 - rides.source.rows[0][7] });
  change(rides, 'I31', 12, { I4: rides.expected.I4 + 12 });
  change(observations, 'D8', observations.source.rows[0][3] + 5 / 1440, { J8: observations.expected.J8 + 5 });
  change(observations, 'D8', observations.source.rows[0][2], { J8: 0 });
  change(observations, 'C8', null, { J8: '' });
  change(observations, 'D8', observations.source.rows[0][2] - 1 / 1440, { J8: '' });
  change(observations, `D${observations.last}`, observations.source.rows.at(-1)[3] + 3 / 1440, { [`J${observations.last}`]: observations.expected[`J${observations.last}`] + 3 });
  return cases;
}
function convert(file, directory, format) {
  return execFileSync(soffice, [`-env:UserInstallation=${pathToFileURL(path.join(qa, 'lo-profile')).href}`, '--headless', '--convert-to', format, '--outdir', directory, file], { encoding: 'utf8', timeout: 120000 });
}

const sources = await loadSources();
const wb = Workbook.create();
const sheets = sources.map(source => buildSheet(wb, source));
const mutations = mutationTests(wb, sheets);
wb.recalculate();
for (const m of sheets) for (const [a, expected] of Object.entries(m.expected)) near(get(m.sheet, a), expected, `${m.source.name}!${a}`);
const inspections = [];
for (const m of sheets) {
  inspections.push((await wb.inspect({ kind: 'table', range: `'${m.source.name}'!A3:${m.endCol}${FIRST + 2}`, include: 'values,formulas', tableMaxRows: 10, tableMaxCols: 11, maxChars: 5000 })).ndjson);
  for (const [tag, range] of [['top', `A1:${m.endCol}${FIRST + 3}`], ['tail', `A${Math.max(FIRST, m.last - 3)}:${m.endCol}${m.last}`]]) {
    const preview = await wb.render({ sheetName: m.source.name, range, scale: 1.5, format: 'png' });
    await fs.writeFile(path.join(qa, `${m.source.table}-${tag}.png`), new Uint8Array(await preview.arrayBuffer()));
  }
}
inspections.push((await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!', options: { useRegex: true, maxResults: 100 }, maxChars: 5000 })).ndjson);
await fs.writeFile(path.join(qa, 'artifact-inspect.ndjson'), inspections.join('\n'));
const staged = path.join(qa, filename);
await (await SpreadsheetFile.exportXlsx(wb)).save(staged);
await packagePrint(staged, sheets);
const exported = await verifySaved(staged, sheets);
const nativeDir = path.join(qa, 'native');
await fs.mkdir(nativeDir, { recursive: true });
const nativeLog = [convert(staged, nativeDir, 'xlsx:Calc MS Excel 2007 XML')];
const nativeVerified = await verifySaved(path.join(nativeDir, filename), sheets, true);
nativeLog.push(convert(staged, qa, 'pdf:calc_pdf_Export'));
await fs.writeFile(path.join(qa, 'native-conversion.log'), nativeLog.join('\n'));
const pdf = path.join(qa, filename.replace(/\.xlsx$/, '.pdf'));
const pages = JSON.parse(execFileSync(python, ['-c', 'import json,sys,pdfplumber\nwith pdfplumber.open(sys.argv[1]) as d:\n print(json.dumps([{"page":i+1,"width":p.width,"height":p.height,"text":p.extract_text(),"min_font_size":min((c["size"] for c in p.chars),default=0)} for i,p in enumerate(d.pages)],ensure_ascii=False))', pdf], { encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 }));
assert(pages.length >= sheets.length, 'Missing native PDF sheets');
for (const p of pages) {
  assert(Math.abs(p.width - 841.89) < 2 && Math.abs(p.height - 595.28) < 2, `PDF page ${p.page}: not A4 landscape`);
  assert(p.text && !/#{2,}/.test(p.text), `PDF page ${p.page}: missing or truncated text`);
  assert(p.min_font_size >= 9, `PDF page ${p.page}: font too small (${p.min_font_size})`);
}
const pdfText = pages.map(p => p.text.replace(/\s/g, '')).join('\n');
for (const source of sources) for (const row of source.raw) {
  assert(pdfText.includes(row[0]), `PDF missing record ${row[0]}`);
}
execFileSync(pdftoppm, ['-r', '100', '-png', pdf, path.join(qa, 'native-page')], { timeout: 120000, maxBuffer: 4 * 1024 * 1024 });
await fs.writeFile(path.join(qa, 'native-pages.json'), JSON.stringify(pages, null, 2));
for (const source of sources) assert.equal(await fs.readFile(path.join(akte, source.file), 'utf8'), source.text, `CSV changed during build: ${source.file}`);
const output = path.join(akte, filename);
await fs.copyFile(staged, output);
await verifySaved(output, sheets);
const report = {
  file: output, engine: 'Bundled Artifact Tool; native LibreOffice recalculation and PDF', qa,
  sources: sources.map(source => ({ file: source.file, sha256: source.sha256, rows: source.rows.length,
    sheet: source.name, range: `A${FIRST}:${col(source.fields.length - 1)}${FIRST + source.rows.length - 1}`,
    fieldMapping: source.fields.map((field, i) => ({ field, column: col(i), header: source.headers[i].replaceAll('\n', ' '), type: source.types[i] })),
  })),
  totals: { rides: sources[0].rows.length, waitingMinutes: sum(sources[0].rows.map(r => r[7])), surchargeNetEUR: sum(sources[0].rows.map(r => r[8])),
    surchargesByOperator: Object.fromEntries([...new Set(sources[0].rows.map(r => r[3]))].map(operator => [operator, sum(sources[0].rows.filter(r => r[3] === operator).map(r => r[8]))])),
    keyEvents: sources[1].rows.length, observations: sources[2].rows.length, emptyReturnDates: sources[1].rows.filter(r => r[7] === null).length,
    emptyWidths: sources[2].rows.filter(r => r[7] === null).length, observationDurationsMinutes: sources[2].rows.map(r => Math.round((r[3] - r[2]) * 1440)),
  }, ...exported, nativeVerified, mutations, nativePdfPages: pages.length,
};
await fs.writeFile(path.join(qa, 'qa-report.json'), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));

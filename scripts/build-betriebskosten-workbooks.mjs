#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';

// Usage: node build-betriebskosten-workbooks.mjs dataset.json [repoRoot] [previewTmp]
const [datasetArg, repoArg, previewArg] = process.argv.slice(2);
if (!datasetArg) throw new Error('Usage: dataset.json [repoRoot] [previewTmp]');
const datasetPath = path.resolve(datasetArg);
const repo = path.resolve(repoArg || path.join(path.dirname(fileURLToPath(import.meta.url)), '..'));
const preview = path.resolve(previewArg || await fs.mkdtemp(path.join(os.tmpdir(), 'betriebskosten-xlsx-')));
assert(preview !== repo && !preview.startsWith(`${repo}${path.sep}`), 'Preview directory must be outside the repository');
await fs.mkdir(preview, { recursive: true });
const moduleLink = path.join(preview, 'node_modules');
try {
  await fs.lstat(moduleLink);
} catch {
  await fs.symlink(path.resolve(path.dirname(process.execPath), '../node_modules'), moduleLink, 'dir');
}
const requireRuntime = createRequire(path.join(preview, 'runtime.cjs'));
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(requireRuntime.resolve('@oai/artifact-tool')).href);
const JSZip = requireRuntime('jszip');
const xml = requireRuntime('xml-js');
const soffice = path.resolve(path.dirname(process.execPath), '../../bin/override/soffice');
await fs.access(soffice);

const C = { blue: '#1F4E78', pale: '#EAF3F8', line: '#B5CBD9', ink: '#202B33', gray: '#59666F' };
const EUR = '#,##0.00 "EUR ";-#,##0.00 "EUR ";0.00 "EUR "';
const DATE = 'dd"."mm"."yyyy';
const round = n => Math.round((n + Number.EPSILON) * 100) / 100;
const sum = xs => xs.reduce((a, b) => a + b, 0);
const serial = iso => (Date.parse(`${iso}T00:00:00Z`) - Date.UTC(1899, 11, 30)) / 86400000;
const set = (s, a, v) => { s.getRange(a).values = [[v]]; };
const formula = (s, a, f) => { s.getRange(a).formulas = [[f]]; };
const value = (s, a) => s.getRange(a).values[0][0];
const near = (actual, expected, name) => assert(Math.abs(actual - expected) < 0.000001, `${name}: ${actual} != ${expected}`);
const col = n => String.fromCharCode(65 + n);
const sheetNames = ['Belegeingang', 'Mietkonto2025', 'Abrechnung_Stand'];
const categoryLabel = category => ({ Heizoel: 'Heiz\u00f6l', Strassenreinigung: 'Stra\u00dfenreinigung' })[category] || category;

function base(wb, name, widths, lastRow, title, c) {
  const s = wb.worksheets.getItem(name);
  const last = col(widths.length - 1);
  s.showGridLines = false;
  s.tabColor = C.blue;
  s.getRange(`A1:${last}${lastRow}`).format = {
    font: { name: 'Arial', size: 10, color: C.ink },
    verticalAlignment: 'center', rowHeight: 22,
  };
  widths.forEach((w, i) => { s.getRange(`${col(i)}1:${col(i)}${lastRow}`).format.columnWidthPx = w; });
  s.getRange(`A1:${last}1`).format.rowHeight = 9;
  s.getRange(`A2:${last}2`).format.rowHeight = 26;
  set(s, 'A2', title);
  s.getRange('A2').format.font = { name: 'Arial', size: 15, bold: true, color: C.blue };
  set(s, 'A3', `${c.address} | 01.01.2025 bis 31.12.2025`.replace(' | ', ' / '));
  set(s, 'A4', c.manager);
  s.getRange(`A3:${last}4`).format.rowHeight = 18;
  s.getRange(`A4:${last}4`).format.borders = { bottom: { style: 'thin', color: C.blue } };
  s.getRange(`A6:${last}6`).format.rowHeight = 8;
  return s;
}

function header(s, range) {
  s.getRange(range).format = {
    fill: C.blue, font: { name: 'Arial', size: 10, color: '#FFFFFF', bold: true },
    horizontalAlignment: 'center', verticalAlignment: 'center', wrapText: true,
    borders: { insideVertical: { style: 'thin', color: '#FFFFFF' } }, rowHeight: 30,
  };
}

function body(s, first, last, endCol) {
  s.getRange(`A${first}:${endCol}${last}`).format.wrapText = true;
  for (let r = first; r <= last; r++) {
    if ((r - first) % 2 === 0) s.getRange(`A${r}:${endCol}${r}`).format.fill = C.pale;
  }
}

function total(s, row, endCol, strong = false) {
  s.getRange(`A${row}:${endCol}${row}`).format = {
    fill: strong ? C.blue : '#DFEAF1',
    font: { name: 'Arial', size: 10, bold: true, color: strong ? '#FFFFFF' : C.ink },
    borders: { top: { style: 'thin', color: C.blue } }, rowHeight: 27,
  };
}

function makeBook(c) {
  assert(['betriebskosten-2025-weg-schoeneberg', 'betriebskosten-2025-mietshaus-schoeneberg'].includes(c.slug));
  assert(c.belege.length === (c.slug.includes('-weg-') ? 42 : 41));
  assert.equal(new Set(c.belege.map(b => b.number)).size, c.belege.length);
  assert.equal(sum(c.areas), c.area);
  assert.equal(c.areas[Number(c.unit) - 1], 108);
  assert.equal(c.cold + c.heat, 300);
  for (const b of c.belege) {
    assert(Number.isFinite(b.amount) && Number.isFinite(b.vat));
    assert(Number.isInteger(serial(b.date)) && Number.isInteger(serial(b.paid)));
  }
  const wb = Workbook.create();
  sheetNames.forEach(n => wb.worksheets.add(n));
  const end = 7 + c.belege.length;
  const b = base(wb, sheetNames[0], [150, 190, 300, 140, 300, 132, 112, 115, 132, 315], end, 'Belegeingang 2025', c);
  set(b, 'A4', `${c.manager} / Objektkonto ${c.code} / Sachbearbeitung: ${c.clerk}`);
  set(b, 'F2', 'Belegdetails 2025');
  b.getRange('F2').format.font = { name: 'Arial', size: 15, bold: true, color: C.blue };
  set(b, 'F3', `${c.address} / 01.01.2025 bis 31.12.2025`);
  set(b, 'F4', c.manager);
  b.getRange('A7:J7').values = [[
    'Kostenart', 'Belegsteller', 'Beleg / Zeitraum', 'Betrag', 'Rechnungsempf\u00e4nger',
    'Belegnummer', 'Belegdatum', 'Enthaltene USt.', 'Zahlungsdatum', 'Belegdatei',
  ]];
  b.getRange(`A8:J${end}`).values = c.belege.map(x => [
    categoryLabel(x.category), x.issuer, `${x.number} / ${x.label}`, x.amount, c.recipient, x.number, serial(x.date), x.vat, serial(x.paid), x.file,
  ]);
  const bt = b.tables.add(`A7:J${end}`, true, `Belege_${c.code}`);
  bt.showFilterButton = true;
  header(b, 'A7:J7');
  body(b, 8, end, 'J');
  b.getRange(`A8:J${end}`).format.rowHeight = 28;
  for (const cc of ['D', 'H']) {
    b.getRange(`${cc}8:${cc}${end}`).setNumberFormat(EUR);
    b.getRange(`${cc}8:${cc}${end}`).format.horizontalAlignment = 'right';
  }
  for (const cc of ['G', 'I']) {
    b.getRange(`${cc}8:${cc}${end}`).setNumberFormat(DATE);
    b.getRange(`${cc}8:${cc}${end}`).format.horizontalAlignment = 'center';
  }
  set(b, 'A5', 'Belegsumme'); set(b, 'F5', 'USt.-Summe');
  formula(b, 'D5', `=SUM(D8:D${end})`);
  formula(b, 'H5', `=SUM(H8:H${end})`);
  b.getRange('D5').setNumberFormat(EUR); b.getRange('H5').setNumberFormat(EUR);
  b.getRange('A5:J5').format.font = { name: 'Arial', size: 10, bold: true, color: C.blue };
  b.freezePanes.freezeRows(7);
  b.freezePanes.freezeColumns(1);

  const m = base(wb, sheetNames[1], [118, 105, 136, 145, 133, 136, 145, 255], 21, 'Mietkonto 2025', c);
  set(m, 'A5', `WE${c.unit} / ${c.tenant}`);
  m.getRange('A7:H7').values = [[
    'Buchungstag', 'Monat', 'Kaltmiete', 'VZ Betriebskosten', 'VZ Heizung', 'VZ gesamt', 'Zahlung gesamt', 'Buchungstext',
  ]];
  m.getRange('A8:H19').values = Array.from({ length: 12 }, (_, i) => [
    serial(`2025-${String(i + 1).padStart(2, '0')}-03`),
    serial(`2025-${String(i + 1).padStart(2, '0')}-01`),
    c.rent, c.cold, c.heat, null, null, `Dauerauftrag ${c.tenant}`,
  ]);
  m.getRange('F8').formulas = [['=SUM(D8:E8)']];
  m.getRange('F8:F19').fillDown();
  m.getRange('G8').formulas = [['=SUM(C8:E8)']];
  m.getRange('G8:G19').fillDown();
  m.tables.add('A7:H19', true, `Mietkonto_${c.code}`).showFilterButton = true;
  header(m, 'A7:H7');
  body(m, 8, 19, 'H');
  m.getRange('A8:H19').format.rowHeight = 28;
  m.getRange('A8:A19').setNumberFormat(DATE);
  m.getRange('B8:B19').setNumberFormat('mm/yyyy');
  m.getRange('C8:G21').setNumberFormat(EUR);
  m.getRange('C8:G21').format.horizontalAlignment = 'right';
  set(m, 'A21', 'Jahressumme');
  for (const cc of ['C', 'D', 'E', 'F', 'G']) formula(m, `${cc}21`, `=SUM(${cc}8:${cc}19)`);
  total(m, 21, 'H', true);
  m.freezePanes.freezeRows(7);

  const areaFirst = 35;
  const areaLast = areaFirst + c.areas.length - 1;
  const areaTotal = areaLast + 2;
  const a = base(wb, sheetNames[2], [265, 131, 99, 99, 140], areaTotal, 'Betriebskostenabrechnung 2025', c);
  set(a, 'A5', `WE${c.unit} / ${c.tenant}`);
  set(a, 'A7', 'Abrechnungsdatum'); set(a, 'B7', serial(c.tenant_date));
  set(a, 'A8', 'Verwaltungsstand'); set(a, 'B8', serial(c.draft_date));
  a.getRange('B7:B8').setNumberFormat(DATE);
  set(a, 'A9', 'Wohnfl\u00e4che Wohnung / m\u00b2');
  formula(a, 'B9', `=B${areaFirst + Number(c.unit) - 1}`);
  set(a, 'A10', 'Wohnfl\u00e4che Objekt / m\u00b2');
  formula(a, 'B10', `=B${areaTotal}`);
  set(a, 'A11', 'Angerechnete Vorauszahlungen'); set(a, 'B11', c.draft_credited);
  a.getRange('B11').setNumberFormat(EUR);
  a.getRange('A12:E13').format.rowHeight = 8;
  a.getRange('A14:E14').values = [['Kostenart', 'Kostenbetrag EUR', 'Gesamt m\u00b2', 'Wohnung m\u00b2', 'Ihr Anteil EUR']];
  const start = 15;
  assert.equal(c.draft_costs.length, 10);
  a.getRange('A15:B24').values = c.draft_costs;
  a.getRange('C15').formulas = [['=$B$10']]; a.getRange('C15:C24').fillDown();
  a.getRange('D15').formulas = [['=$B$9']]; a.getRange('D15:D24').fillDown();
  a.getRange('E15').formulas = [['=ROUND(B15*D15/C15,2)']]; a.getRange('E15:E24').fillDown();
  const directTax = c.slug.includes('-weg-');
  set(a, 'A25', directTax ? `Grundsteuer WE${c.unit}` : 'Grundsteuer');
  set(a, 'B25', directTax ? c.draft_ground : c.tax);
  if (directTax) formula(a, 'E25', '=B25');
  else {
    formula(a, 'C25', '=$B$10'); formula(a, 'D25', '=$B$9');
    formula(a, 'E25', '=ROUND(B25*D25/C25,2)');
  }
  set(a, 'A26', 'Heizung / Warmwasser\nlaut Rechenbogen');
  set(a, 'B26', c.draft_heating); formula(a, 'E26', '=B26');
  header(a, 'A14:E14'); body(a, 15, 26, 'E');
  a.getRange('A15:E26').format.rowHeight = 25;
  a.getRange('A26:E26').format.rowHeight = 33;
  a.getRange('B15:B26').setNumberFormat(EUR);
  a.getRange('E15:E30').setNumberFormat(EUR);
  a.getRange('C15:D25').setNumberFormat('#,##0.00');
  set(a, 'A28', 'Kostenanteile gesamt'); formula(a, 'E28', '=SUM(E15:E26)');
  set(a, 'A29', 'Angerechnete Vorauszahlungen'); formula(a, 'E29', '=B11');
  set(a, 'A30', 'Nachzahlung'); formula(a, 'E30', '=ROUND(E28-E29,2)');
  total(a, 28, 'E'); total(a, 30, 'E', true);
  a.getRange('A31:E32').format.rowHeight = 10;
  set(a, 'A33', 'Wohnfl\u00e4chenverzeichnis');
  a.getRange('A33').format.font = { name: 'Arial', size: 12, bold: true, color: C.blue };
  a.getRange('A34:B34').values = [['Einheit', 'Wohnfl\u00e4che m\u00b2']];
  a.getRange(`A35:B${areaLast}`).values = c.areas.map((area, i) => [`WE${String(i + 1).padStart(2, '0')}`, area]);
  a.tables.add(`A34:B${areaLast}`, true, `Flaechen_${c.code}`).showFilterButton = true;
  header(a, 'A34:B34'); body(a, areaFirst, areaLast, 'B');
  set(a, `A${areaTotal}`, 'Gesamtwohnfl\u00e4che');
  formula(a, `B${areaTotal}`, `=SUM(B${areaFirst}:B${areaLast})`);
  a.getRange(`B35:B${areaTotal}`).setNumberFormat('#,##0.00');
  total(a, areaTotal, 'B');
  a.freezePanes.freezeRows(14);
  wb.recalculate();
  return { wb, b, m, a, c, end, areaTotal, areaFirst, areaLast, start };
}

function expectations(book) {
  const { c, end, areaTotal } = book;
  const x = {};
  const add = (s, addr, n) => { x[`${s}!${addr}`] = n; };
  add(sheetNames[0], 'D5', sum(c.belege.map(b => b.amount)));
  add(sheetNames[0], 'H5', sum(c.belege.map(b => b.vat)));
  for (let row = 8; row <= 19; row++) {
    add(sheetNames[1], `F${row}`, 300);
    add(sheetNames[1], `G${row}`, c.rent + 300);
  }
  for (const [cc, n] of Object.entries({ C: c.rent, D: c.cold, E: c.heat, F: 300, G: c.rent + 300 })) add(sheetNames[1], `${cc}21`, n * 12);
  c.draft_costs.forEach((r, i) => add(sheetNames[2], `E${15 + i}`, round(r[1] * 108 / c.area)));
  for (const [addr, n] of Object.entries({ B9: 108, B10: c.area, B11: c.draft_credited, E25: c.draft_ground, E26: c.draft_heating, E28: c.draft_total, E29: c.draft_credited, E30: c.draft_balance, [`B${areaTotal}`]: c.area })) add(sheetNames[2], addr, n);
  return x;
}

function assertValues(book, expected) {
  for (const [key, n] of Object.entries(expected)) {
    const [name, cell] = key.split('!');
    near(value(book.wb.worksheets.getItem(name), cell), n, key);
  }
}

async function artifactTests(book, dir) {
  const { wb, a, b, m, c, end, areaFirst } = book;
  const expected = expectations(book);
  assertValues(book, expected);
  const tests = [];
  function test(sheet, cell, input, check, label) {
    const old = value(sheet, cell);
    try { set(sheet, cell, input); wb.recalculate(); check(); tests.push(label); }
    finally { set(sheet, cell, old); wb.recalculate(); }
    assertValues(book, expected);
  }
  test(b, 'D8', c.belege[0].amount + 100, () => {
    near(value(b, 'D5'), expected['Belegeingang!D5'] + 100, 'Belegsumme');
    near(value(a, 'E30'), c.draft_balance, 'Abrechnungsstand bleibt separat');
  }, 'Belegbetrag +100, Belegsumme reagiert, Abrechnungsstand unveraendert');
  test(m, 'D19', c.cold + 17, () => {
    near(value(m, 'F19'), 317, 'Dezember VZ'); near(value(m, 'F21'), 3617, 'Jahres-VZ');
    near(value(m, 'G21'), (c.rent + 300) * 12 + 17, 'Jahreszahlung');
    near(value(a, 'B11'), c.draft_credited, 'Angerechnete VZ');
  }, 'Dezember-VZ +17, Monats- und Jahressummen reagieren, Anrechnung unveraendert');
  test(a, 'B15', 0, () => near(value(a, 'E15'), 0, 'Nullkosten'), 'Kostenansatz null');
  test(a, 'B15', 100.05, () => near(value(a, 'E15'), round(100.05 * 108 / c.area), 'Centrundung'), 'Centrundung');
  test(a, `B${areaFirst}`, c.areas[0] + 12, () => {
    near(value(a, 'B10'), c.area + 12, 'Flaechensumme');
    near(value(a, 'E15'), round(c.draft_costs[0][1] * 108 / (c.area + 12)), 'Flaechenanteil');
    near(value(a, 'E25'), c.slug.includes('-weg-') ? c.draft_ground : round(c.tax * 108 / (c.area + 12)), 'Grundsteueranteil');
  }, 'Flaeche +12 und direkte/proportionale Grundsteuer');
  test(a, 'B26', c.draft_heating + 10, () => near(value(a, 'E30'), c.draft_balance + 10, 'Heizbetrag'), 'Heizbetrag +10');
  test(a, 'B11', c.draft_credited + 100, () => near(value(a, 'E30'), c.draft_balance - 100, 'Anrechnung'), 'Anrechnung +100');
  wb.recalculate();
  const inspections = [];
  for (const [name, range] of [[sheetNames[0], `A5:J${end}`], [sheetNames[1], 'A7:H21'], [sheetNames[2], 'A7:E30']]) {
    inspections.push((await wb.inspect({ kind: 'table', range: `${name}!${range}`, include: 'values,formulas', tableMaxRows: 50, tableMaxCols: 10, maxChars: 28000 })).ndjson);
  }
  const errorScan = (await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!', options: { useRegex: true, maxResults: 100 }, maxChars: 4000 })).ndjson;
  await fs.writeFile(path.join(dir, 'artifact-inspect.ndjson'), `${inspections.join('\n')}\n${errorScan}\n`);
  await fs.writeFile(path.join(dir, 'artifact-tests.json'), JSON.stringify({ tests, expected, errorScan }, null, 2));
  return expected;
}

const el = (name, attributes = {}, elements = []) => ({ type: 'element', name, attributes, elements });
const txt = text => ({ type: 'text', text: String(text) });
const children = (root, name) => (root.elements || []).filter(e => e.type === 'element' && e.name === name);
const child = (root, name) => children(root, name)[0];
function replace(root, name, node, order) {
  root.elements ||= [];
  root.elements = root.elements.filter(e => e.name !== name);
  const rank = order.indexOf(name);
  const i = root.elements.findIndex(e => order.indexOf(e.name) > rank);
  root.elements.splice(i < 0 ? root.elements.length : i, 0, node);
}
async function readXml(zip, name) {
  const doc = xml.xml2js(await zip.file(name).async('string'));
  const root = doc.elements.find(e => e.type === 'element');
  const prefix = root.name.includes(':') ? root.name.split(':')[0] : null;
  if (prefix && root.attributes?.[`xmlns:${prefix}`] === 'http://schemas.openxmlformats.org/spreadsheetml/2006/main') {
    const strip = node => {
      if (node.name?.startsWith(`${prefix}:`)) node.name = node.name.slice(prefix.length + 1);
      for (const e of node.elements || []) strip(e);
    };
    strip(root);
    root.attributes.xmlns = root.attributes[`xmlns:${prefix}`];
    delete root.attributes[`xmlns:${prefix}`];
  }
  return doc;
}
function writeXml(zip, name, obj) { zip.file(name, xml.js2xml(obj, { compact: false })); }

// The documented authoring API does not expose print setup or core properties.
// Keep this OOXML pass restricted to these native packaging features.
async function packagePrint(file, book) {
  const { c, end, areaTotal } = book;
  const zip = await JSZip.loadAsync(await fs.readFile(file));
  const core = zip.file('docProps/core.xml') ? await readXml(zip, 'docProps/core.xml') : {
    elements: [el('cp:coreProperties', {
      'xmlns:cp': 'http://schemas.openxmlformats.org/package/2006/metadata/core-properties',
      'xmlns:dc': 'http://purl.org/dc/elements/1.1/',
      'xmlns:dcterms': 'http://purl.org/dc/terms/',
      'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    })],
  };
  const cr = core.elements.find(e => e.type === 'element');
  for (const [name, content, attr] of [
    ['dc:creator', 'Klotzkette', {}], ['cp:lastModifiedBy', 'Klotzkette', {}],
    ['dc:title', `Verwaltungsbuchhaltung 2025 - ${c.address}`, {}],
    ['dcterms:created', `${c.draft_date}T00:00:00Z`, { 'xsi:type': 'dcterms:W3CDTF' }],
    ['dcterms:modified', `${c.tenant_date}T00:00:00Z`, { 'xsi:type': 'dcterms:W3CDTF' }],
  ]) {
    cr.elements = (cr.elements || []).filter(e => e.name !== name);
    cr.elements.push(el(name, attr, [txt(content)]));
  }
  writeXml(zip, 'docProps/core.xml', core);
  const rels = await readXml(zip, '_rels/.rels');
  const relRoot = rels.elements.find(e => e.type === 'element');
  if (!children(relRoot, 'Relationship').some(e => e.attributes.Type.endsWith('/metadata/core-properties'))) {
    relRoot.elements.push(el('Relationship', { Id: 'rCoreProperties', Type: 'http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties', Target: 'docProps/core.xml' }));
  }
  writeXml(zip, '_rels/.rels', rels);
  const types = await readXml(zip, '[Content_Types].xml');
  const typeRoot = types.elements.find(e => e.type === 'element');
  if (!children(typeRoot, 'Override').some(e => e.attributes.PartName === '/docProps/core.xml')) {
    typeRoot.elements.push(el('Override', { PartName: '/docProps/core.xml', ContentType: 'application/vnd.openxmlformats-package.core-properties+xml' }));
  }
  writeXml(zip, '[Content_Types].xml', types);
  const wbxml = await readXml(zip, 'xl/workbook.xml');
  const wr = wbxml.elements.find(e => e.type === 'element');
  const defs = child(wr, 'definedNames') || el('definedNames');
  defs.elements = (defs.elements || []).filter(e => !['_xlnm.Print_Area', '_xlnm.Print_Titles'].includes(e.attributes?.name));
  const regions = [[`A1:E${end}`, `F1:J${end}`], ['A1:H21'], [`A1:E${areaTotal}`]];
  for (let i = 0; i < 3; i++) {
    defs.elements.push(el('definedName', { name: '_xlnm.Print_Area', localSheetId: String(i) }, [txt(regions[i].map(r => `'${sheetNames[i]}'!${r.replace(/([A-Z]+)(\d+)/g, '$$$1$$$2')}`).join(','))]));
    defs.elements.push(el('definedName', { name: '_xlnm.Print_Titles', localSheetId: String(i) }, [txt(`'${sheetNames[i]}'!$1:$${i === 2 ? 8 : 7}`)]));
  }
  replace(wr, 'definedNames', defs, ['fileVersion', 'fileSharing', 'workbookPr', 'workbookProtection', 'bookViews', 'sheets', 'functionGroups', 'externalReferences', 'definedNames', 'calcPr', 'oleSize', 'customWorkbookViews', 'pivotCaches', 'smartTagPr', 'smartTagTypes', 'webPublishing', 'fileRecoveryPr', 'webPublishObjects', 'extLst']);
  replace(wr, 'calcPr', el('calcPr', { calcId: '191029', fullCalcOnLoad: '1', forceFullCalc: '1', calcMode: 'auto' }), ['fileVersion', 'workbookPr', 'bookViews', 'sheets', 'definedNames', 'calcPr', 'extLst']);
  writeXml(zip, 'xl/workbook.xml', wbxml);
  const order = ['sheetPr', 'dimension', 'sheetViews', 'sheetFormatPr', 'cols', 'sheetData', 'sheetCalcPr', 'sheetProtection', 'protectedRanges', 'scenarios', 'autoFilter', 'sortState', 'dataConsolidate', 'customSheetViews', 'mergeCells', 'phoneticPr', 'conditionalFormatting', 'dataValidations', 'hyperlinks', 'printOptions', 'pageMargins', 'pageSetup', 'headerFooter', 'rowBreaks', 'colBreaks', 'customProperties', 'cellWatches', 'ignoredErrors', 'smartTags', 'drawing', 'legacyDrawing', 'legacyDrawingHF', 'picture', 'oleObjects', 'controls', 'webPublishItems', 'tableParts', 'extLst'];
  for (let i = 0; i < 3; i++) {
    const name = `xl/worksheets/sheet${i + 1}.xml`;
    const doc = await readXml(zip, name);
    const root = doc.elements.find(e => e.type === 'element');
    const pr = child(root, 'sheetPr') || el('sheetPr');
    replace(pr, 'pageSetUpPr', el('pageSetUpPr', { fitToPage: '1' }), ['tabColor', 'outlinePr', 'pageSetUpPr']);
    replace(root, 'sheetPr', pr, order);
    replace(root, 'printOptions', el('printOptions', { gridLines: '0', headings: '0', horizontalCentered: '1' }), order);
    replace(root, 'pageMargins', el('pageMargins', { left: '0.28', right: '0.28', top: '0.35', bottom: '0.4', header: '0.15', footer: '0.18' }), order);
    replace(root, 'pageSetup', el('pageSetup', { paperSize: '9', orientation: i === 2 ? 'portrait' : 'landscape', fitToWidth: '1', fitToHeight: '0' }), order);
    replace(root, 'headerFooter', el('headerFooter', {}, [el('oddFooter', {}, [txt(`&L${c.code} / 2025&C${sheetNames[i]}&RSeite &P von &N`)])]), order);
    if (i !== 1) {
      const breaks = i === 0 ? ['21', '35'] : ['32'];
      replace(root, 'rowBreaks', el('rowBreaks', { count: String(breaks.length), manualBreakCount: String(breaks.length) }, breaks.map(id => el('brk', { id, max: '16383', man: '1' }))), order);
    }
    const views = child(root, 'sheetViews');
    const view = child(views, 'sheetView');
    if (view) {
      view.attributes.showGridLines = '0';
      const pane = child(view, 'pane');
      const frozenRows = i === 2 ? 14 : 7;
      if (pane) Object.assign(pane.attributes, { ySplit: String(frozenRows), xSplit: i === 0 ? '1' : '0', topLeftCell: `${i === 0 ? 'B' : 'A'}${frozenRows + 1}`, state: 'frozen', activePane: i === 0 ? 'bottomRight' : 'bottomLeft' });
    }
    writeXml(zip, name, doc);
  }
  await fs.writeFile(file, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
}

async function savedCells(file) {
  const zip = await JSZip.loadAsync(await fs.readFile(file));
  let shared = [];
  const stringText = node => (node.elements || []).map(e => e.type === 'text' ? e.text : stringText(e)).join('');
  if (zip.file('xl/sharedStrings.xml')) {
    const d = await readXml(zip, 'xl/sharedStrings.xml');
    shared = children(d.elements.find(e => e.type === 'element'), 'si').map(stringText);
  }
  const cells = {}, formulas = {};
  for (let i = 0; i < 3; i++) {
    const d = await readXml(zip, `xl/worksheets/sheet${i + 1}.xml`);
    const root = d.elements.find(e => e.type === 'element');
    for (const row of children(child(root, 'sheetData'), 'row')) for (const cell of children(row, 'c')) {
      const key = `${sheetNames[i]}!${cell.attributes.r}`;
      const raw = stringText(child(cell, 'v') || {});
      const t = cell.attributes.t;
      cells[key] = t === 's' ? shared[Number(raw)] : t === 'inlineStr' ? stringText(child(cell, 'is')) : t === 'e' || t === 'str' ? raw : raw === '' ? null : Number(raw);
      if (child(cell, 'f')) formulas[key] = stringText(child(cell, 'f'));
      assert(t !== 'e', `${file}: ${key}: ${raw}`);
    }
    assert(child(root, 'pageSetup'), `Missing page setup ${i}`);
    assert(child(child(root, 'sheetViews'), 'sheetView') && child(child(child(root, 'sheetViews'), 'sheetView'), 'pane'), `Missing freeze ${i}`);
  }
  return { zip, cells, formulas };
}

async function verifySaved(file, book, expected, baseline = true) {
  const { cells, formulas, zip } = await savedCells(file);
  for (const [key, n] of Object.entries(expected)) near(cells[key], n, `Saved ${key}`);
  if (baseline) {
    const c = book.c;
    c.belege.forEach((r, i) => {
      const row = i + 8;
      const fields = { A: categoryLabel(r.category), B: r.issuer, C: `${r.number} / ${r.label}`, D: r.amount, E: c.recipient, F: r.number, G: serial(r.date), H: r.vat, I: serial(r.paid), J: r.file };
      for (const [cc, v] of Object.entries(fields)) assert.equal(cells[`Belegeingang!${cc}${row}`], v);
    });
    for (let row = 8; row <= 19; row++) {
      assert.equal(cells[`Mietkonto2025!A${row}`], serial(`2025-${String(row - 7).padStart(2, '0')}-03`));
      assert.equal(formulas[`Mietkonto2025!F${row}`], `SUM(D${row}:E${row})`);
      assert.equal(formulas[`Mietkonto2025!G${row}`], `SUM(C${row}:E${row})`);
    }
    assert.equal(cells['Abrechnung_Stand!B7'], serial(c.tenant_date));
    assert.equal(cells['Abrechnung_Stand!B8'], serial(c.draft_date));
    assert.equal(cells['Abrechnung_Stand!B26'], c.draft_heating);
    const core = await zip.file('docProps/core.xml').async('string');
    assert(core.includes('Klotzkette') && core.includes(`${c.draft_date}T00:00:00Z`) && core.includes(`${c.tenant_date}T00:00:00Z`));
    const tableFiles = Object.keys(zip.files).filter(n => /^xl\/tables\/table\d+\.xml$/.test(n));
    assert.equal(tableFiles.length, 3);
    for (const f of tableFiles) assert((await zip.file(f).async('string')).includes('autoFilter'));
  }
  return { checkedValues: Object.keys(expected).length, formulas: Object.keys(formulas).length };
}

function convert(input, outdir, format, profile) {
  return execFileSync(soffice, [`-env:UserInstallation=${pathToFileURL(profile).href}`, '--headless', '--convert-to', format, '--outdir', outdir, input], { encoding: 'utf8', timeout: 120000 });
}

async function buildCase(c, datasetText) {
  const dir = path.join(preview, c.code);
  await fs.mkdir(dir, { recursive: true });
  const book = makeBook(c);
  const expected = await artifactTests(book, dir);
  const { wb, a, m } = book;
  for (const [name, range] of [[sheetNames[0], `A1:J${book.end}`], [sheetNames[1], 'A1:H21'], [sheetNames[2], `A1:E${book.areaTotal}`]]) {
    const img = await wb.render({ sheetName: name, range, scale: 1.5, format: 'png' });
    await fs.writeFile(path.join(dir, `${name}.png`), new Uint8Array(await img.arrayBuffer()));
  }
  // The native-engine perturbation is a disposable export, never a deliverable.
  set(a, 'B15', c.draft_costs[0][1] + 100);
  set(a, 'B11', c.draft_credited + 100);
  set(a, 'B26', c.draft_heating + 10);
  set(m, 'D19', c.cold + 17);
  wb.recalculate();
  const perturbed = { ...expected };
  for (const key of ['Abrechnung_Stand!B11', 'Abrechnung_Stand!E29']) perturbed[key] += 100;
  const delta = round((c.draft_costs[0][1] + 100) * 108 / c.area) - expected['Abrechnung_Stand!E15'];
  perturbed['Abrechnung_Stand!E15'] += delta;
  perturbed['Abrechnung_Stand!E26'] += 10;
  perturbed['Abrechnung_Stand!E28'] += delta + 10;
  perturbed['Abrechnung_Stand!E30'] += delta - 90;
  for (const key of ['Mietkonto2025!F19', 'Mietkonto2025!G19', 'Mietkonto2025!D21', 'Mietkonto2025!F21', 'Mietkonto2025!G21']) perturbed[key] += 17;
  const perturbFile = path.join(dir, 'perturbation.xlsx');
  await (await SpreadsheetFile.exportXlsx(wb)).save(perturbFile);
  await packagePrint(perturbFile, book);
  set(a, 'B15', c.draft_costs[0][1]); set(a, 'B11', c.draft_credited); set(a, 'B26', c.draft_heating); set(m, 'D19', c.cold);
  wb.recalculate();
  assertValues(book, expected);
  assert.equal(await fs.readFile(datasetPath, 'utf8'), datasetText, 'Dataset changed; rerun against latest source');
  const output = path.join(repo, 'testakten', c.slug, 'zahlenwerk', 'Verwaltungsbuchhaltung_2025.xlsx');
  const staged = path.join(dir, path.basename(output));
  await (await SpreadsheetFile.exportXlsx(wb)).save(staged);
  await packagePrint(staged, book);
  const exported = await verifySaved(staged, book, expected);
  const nativeDir = path.join(dir, 'native-recalculated');
  await fs.mkdir(nativeDir, { recursive: true });
  const log = [];
  log.push(convert(perturbFile, nativeDir, 'xlsx:Calc MS Excel 2007 XML', path.join(dir, 'lo-profile')));
  const nativePerturb = await verifySaved(path.join(nativeDir, 'perturbation.xlsx'), book, perturbed, false);
  log.push(convert(staged, nativeDir, 'xlsx:Calc MS Excel 2007 XML', path.join(dir, 'lo-profile')));
  const recalculated = path.join(nativeDir, path.basename(output));
  await packagePrint(recalculated, book);
  const nativeBaseline = await verifySaved(recalculated, book, expected);
  // Retain Artifact Tool's native table/style export; LibreOffice is the independent engine check.
  log.push(convert(staged, dir, 'pdf:calc_pdf_Export', path.join(dir, 'lo-profile')));
  await fs.writeFile(path.join(dir, 'native-conversion.log'), log.join('\n'));
  assert.equal(await fs.readFile(datasetPath, 'utf8'), datasetText, 'Dataset changed before final save');
  await fs.mkdir(path.dirname(output), { recursive: true });
  await fs.copyFile(staged, output);
  const final = await verifySaved(output, book, expected);
  return { code: c.code, file: output, sourceBelege: c.belege.length, exported, nativeBaseline, nativePerturb, final, previewDirectory: dir, draftHeating: c.draft_heating, total: c.draft_total, credited: c.draft_credited, balance: c.draft_balance };
}

const datasetText = await fs.readFile(datasetPath, 'utf8');
const data = JSON.parse(datasetText);
assert.equal(data.length, 2);
const results = [];
for (const c of data) results.push(await buildCase(c, datasetText));
assert.equal(await fs.readFile(datasetPath, 'utf8'), datasetText, 'Dataset changed before completion; rebuild both workbooks');
const report = { sourceSha256: createHash('sha256').update(datasetText).digest('hex'), author: 'Klotzkette', engine: 'Bundled LibreOffice', results };
await fs.writeFile(path.join(preview, 'qa-report.json'), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));

#!/usr/bin/env node
// Die Inhaltsdaten kommen aus dem fallbezogenen Python-Builder; Authoring ausschließlich hier.
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import assert from 'node:assert/strict';
import { loadWorkbookRuntime } from './akten-workbook-runtime.mjs';

const { Workbook, SpreadsheetFile, requireRuntime } = await loadWorkbookRuntime(['jszip', 'xml-js']);
const JSZip = requireRuntime('jszip');
const xml = requireRuntime('xml-js');
const [payload, destination, changesJson = '{}'] = process.argv.slice(2);
if (!payload || !destination) throw new Error('Aufruf über build-vertragserstellung-kassel-akte.py');
const data = JSON.parse(await fs.readFile(payload, 'utf8'));
const changes = JSON.parse(changesJson);
const qa = await fs.mkdtemp(path.join(os.tmpdir(), 'kassel-workbook-qa-'));
const wb = Workbook.create();
const ws = wb.worksheets.add('Vergleich');
const inputs = wb.worksheets.add('Ansätze');
const money = '#,##0.00;[Red](#,##0.00);"-"';

for (const s of [ws, inputs]) {
  const last = s.name === 'Vergleich' ? 'D' : 'F';
  s.showGridLines = false;
  s.getRange(`A1:${last}26`).format = {
    font: { name: 'Arial', size: 10, color: '#20252B' }, rowHeight: s === ws ? 17.5 : 21,
    verticalAlignment: 'center', horizontalAlignment: 'left',
  };
  const widths = s === ws ? [330, 170, 170, 170] : [200, 108, 114, 114, 310, 115];
  widths.forEach((width, i) => { s.getRangeByIndexes(0, i, 26, 1).format.columnWidthPx = width; });
  const sourceRows = data[s.name];
  const matrix = sourceRows.map(row => Array.from({ length: widths.length }, (_, i) => {
    const value = row[i] ?? null;
    return typeof value === 'string' && value.startsWith('=') ? null : value;
  }));
  s.getRange(`A1:${last}26`).values = matrix;
  sourceRows.forEach((row, ri) => row.forEach((value, ci) => {
    const target = s.getRangeByIndexes(ri, ci, 1, 1);
    if (typeof value === 'string' && value.startsWith('=')) {
      target.formulas = [[value]];
      target.setNumberFormat(money);
      target.format.horizontalAlignment = 'right';
    } else if (typeof value === 'number') {
      target.setNumberFormat(money);
      target.format.font.color = '#205898';
      target.format.horizontalAlignment = 'right';
    }
  }));
  s.getRange('A1').format.font = { name: 'Arial', size: 13, bold: true };
  s.getRange(`A1:${last}1`).format.rowHeight = 23;
}
ws.getRange('A2').format.font = { name: 'Arial', size: 13, bold: true };
ws.getRange('A2:D2').format.rowHeight = 23;
for (const row of [3, 22, 23, 24, 25, 26]) {
  ws.getRange(`A${row}`).format.font = { name: 'Arial', size: 9, color: '#505050' };
}
for (const [s, rows, last] of [[ws, [5], 'D'], [inputs, [4, 9, 22], 'F']]) {
  for (const r of rows) {
    s.getRange(`A${r}:${last}${r}`).format = {
      fill: '#394754', font: { name: 'Arial', size: 10, bold: true, color: '#FFFFFF' },
      horizontalAlignment: 'center', verticalAlignment: 'center', wrapText: true, rowHeight: 32,
    };
  }
}
for (const row of [9, 11, 19]) {
  ws.getRange(`A${row}:D${row}`).format = {
    fill: '#E9EEE9', font: { name: 'Arial', size: 10, bold: true },
    borders: { top: { style: 'thin', color: '#B3BDB6' } }, rowHeight: row === 19 ? 31 : 22,
  };
  ws.getRange(`A${row}`).format.wrapText = true;
}
for (const row of [5, 6, 7, 8, 14, 15, 16, 17, 18, 19, 20, 23, 24]) {
  inputs.getRange(`E${row}`).format = { wrapText: true, font: { name: 'Arial', size: 9, color: '#505050' } };
  inputs.getRange(`A${row}:F${row}`).format.rowHeight = 31;
}
inputs.getRange('A4:A24').format.wrapText = true;
inputs.getRange('A21:F21').format.rowHeight = 31;
for (const coord of ['B5', 'B6', 'B18', 'B19', 'B20', 'D10', 'D11', 'D12']) inputs.getRange(coord).setNumberFormat('#,##0');
inputs.getRange('B8').setNumberFormat('0%');
inputs.getRange('F10:F12').setNumberFormat('0%');
ws.getRange('B15:D17').setNumberFormat('#,##0');
ws.getRange('A22:D26').format.rowHeight = 16;
inputs.freezePanes.freezeRows(4);
for (const range of ['B5:B7', 'B10:F12', 'B14:B15', 'B18:B20']) {
  inputs.getRange(range).dataValidation = { rule: { type: 'decimal', operator: 'greaterThanOrEqual', formula1: 0 } };
}
for (const [address, value] of Object.entries(changes)) inputs.getRange(address).values = [[value]];
wb.recalculate();
if (!Object.keys(changes).length) {
  for (const [address, expected] of Object.entries({ B9: 37840, C9: 40720, D9: 33600, C12: 7120 })) {
    assert(Math.abs(ws.getRange(address).values[0][0] - expected) < .005, address);
  }
}
const errors = await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!', options: { useRegex: true, maxResults: 20 }, maxChars: 2000 });
assert(!/"(?:value|text)":"#/.test(errors.ndjson), errors.ndjson);
if (!Object.keys(changes).length) {
  for (const [s, range] of [[ws, 'A1:D26'], [inputs, 'A1:F26']]) {
    const preview = await wb.render({ sheetName: s.name, range, scale: 1.5, format: 'png' });
    await fs.writeFile(path.join(qa, `${s.name}.png`), new Uint8Array(await preview.arrayBuffer()));
    const inspected = await wb.inspect({ kind: 'table', range: `${s.name}!${range}`, include: 'values,formulas', tableMaxRows: 26, tableMaxCols: 6, maxChars: 12000 });
    await fs.writeFile(path.join(qa, `${s.name}.ndjson`), inspected.ndjson);
  }
}
const staged = path.join(qa, 'staged.xlsx');
await (await SpreadsheetFile.exportXlsx(wb)).save(staged);

// Druckeinstellungen per strukturiertem OOXML ergänzen; alle Zellinhalte bleiben artifact-tool-Ausgaben.
const zip = await JSZip.loadAsync(await fs.readFile(staged));
const local = e => e.name?.split(':').at(-1);
const el = (name, attributes, elements = []) => ({ type: 'element', name, attributes, elements });
const doc = xml.xml2js(await zip.file('xl/workbook.xml').async('string'), { compact: false });
const book = doc.elements.find(e => local(e) === 'workbook');
const prefix = book.name.includes(':') ? book.name.split(':')[0] + ':' : '';
let names = book.elements.find(e => local(e) === 'definedNames');
if (!names) {
  names = el(prefix + 'definedNames', {}, []);
  const calc = book.elements.findIndex(e => local(e) === 'calcPr');
  book.elements.splice(calc < 0 ? book.elements.length : calc, 0, names);
}
for (const [index, sheet, area] of [[0, 'Vergleich', '$A$1:$D$26'], [1, 'Ansätze', '$A$1:$F$26']]) {
  names.elements.push(el(prefix + 'definedName', { name: '_xlnm.Print_Area', localSheetId: String(index) }, [{ type: 'text', text: `'${sheet}'!${area}` }]));
}
names.elements.push(el(prefix + 'definedName', { name: '_xlnm.Print_Titles', localSheetId: '1' }, [{ type: 'text', text: "'Ansätze'!$1:$2" }]));
zip.file('xl/workbook.xml', xml.js2xml(doc, { compact: false }));
for (let index = 1; index <= 2; index++) {
  const filename = `xl/worksheets/sheet${index}.xml`;
  const model = xml.xml2js(await zip.file(filename).async('string'), { compact: false });
  const sheet = model.elements.find(e => local(e) === 'worksheet');
  const p = sheet.name.includes(':') ? sheet.name.split(':')[0] + ':' : '';
  sheet.elements = sheet.elements.filter(e => !['pageMargins', 'pageSetup', 'headerFooter', 'rowBreaks'].includes(local(e)));
  const later = new Set(['colBreaks', 'customProperties', 'cellWatches', 'ignoredErrors', 'smartTags', 'drawing', 'legacyDrawing', 'legacyDrawingHF', 'picture', 'oleObjects', 'controls', 'webPublishItems', 'tableParts', 'extLst']);
  const before = sheet.elements.findIndex(e => later.has(local(e)));
  const additions = [
    el(p + 'pageMargins', { left: '.3', right: '.3', top: '.4', bottom: '.4', header: '.15', footer: '.15' }),
    el(p + 'pageSetup', { paperSize: '9', orientation: 'landscape', fitToWidth: '1', fitToHeight: '0' }),
    el(p + 'headerFooter', {}, [el(p + 'oddFooter', {}, [{ type: 'text', text: '&CFuldabogen · Leonie Hartung · 22.09.2026 · Seite &P' }])]),
  ];
  if (index === 2) additions.push(el(p + 'rowBreaks', { count: '1', manualBreakCount: '1' }, [el(p + 'brk', { id: '13', max: '16383', man: '1' })]));
  sheet.elements.splice(before < 0 ? sheet.elements.length : before, 0, ...additions);
  zip.file(filename, xml.js2xml(model, { compact: false }));
}
await fs.writeFile(destination, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
console.log(`artifact-tool: zwei Blätter erstellt und geprüft; QA außerhalb der Akte: ${qa}`);

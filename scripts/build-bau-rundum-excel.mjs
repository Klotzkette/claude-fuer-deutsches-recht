import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {Workbook, SpreadsheetFile} from '@oai/artifact-tool';

const [root, output, qa, only] = process.argv.slice(2);
if (!root || !output || !qa) throw Error('Aufruf: build-bau-rundum-excel.mjs REPO AUSGABE PRUEFORDNER [FALL]');
const specs = [];
for (const part of ['basis', 'vertiefung']) {
  specs.push(...JSON.parse(await fs.readFile(path.join(root, `scripts/bau_rundum_excel_${part}.json`), 'utf8')));
}
const column = i => String.fromCharCode(65 + i);
const dateValue = value => (Date.parse(`${value}T00:00:00Z`) - Date.UTC(1899, 11, 30)) / 86400000;
const timeValue = value => {const [h, m] = value.split(':').map(Number); return (h * 60 + m) / 1440;};
const formats = {text: '" "@', number: '[$-407]#,##0.00" ";[$-407](#,##0.00)" ";"– "', money: '[$-407]#,##0.00" ";[$-407](#,##0.00)" ";"– "', percent: '[$-407]0.0%" "', date: 'dd.mm.yyyy" "', time: 'hh:mm" "'};
const colors = ['#244C43', '#385A78', '#70475D', '#4B5572', '#5A6041'];
const errorPattern = /#REF!|#DIV\/0!|#VALUE!|#NAME\?|#N\/A|#NUM!|#NULL!|#SPILL!|#CALC!/;
function equal(actual, expected, label) {
  if (typeof expected === 'number') assert.ok(typeof actual === 'number' && Math.abs(actual - expected) < 0.00001, `${label}: ${actual} != ${expected}`);
  else assert.equal(actual, expected, label);
}
function checkedValue(wb, control) {
  const value = wb.worksheets.getItem(control.sheet).getRange(control.cell).values[0][0];
  equal(value, control.value, `${control.sheet}!${control.cell}`);
}

for (const [index, spec] of specs.entries()) {
  if (only && spec.slug !== only) continue;
  const wb = Workbook.create();
  const dir = path.join(output, spec.slug);
  const review = path.join(qa, spec.slug);
  await fs.mkdir(dir, {recursive: true});
  await fs.mkdir(review, {recursive: true});
  const accent = colors[index % colors.length];
  for (const s of spec.sheets) wb.worksheets.add(s.name);
  for (const [sheetIndex, s] of spec.sheets.entries()) {
    const sh = wb.worksheets.getItem(s.name);
    const end = 8 + s.rows.length, last = column(s.columns.length - 1);
    assert.ok(s.columns.length <= 9 && s.rows.length > 0);
    assert.ok(s.rows.every(row => row.length === s.columns.length), `${spec.slug}/${s.name}: Spaltenzahl`);
    sh.showGridLines = false;
    sh.tabColor = sheetIndex === 0 ? accent : '#B8C4C2';
    const area = sh.getRange(`A1:${last}${end}`);
    area.format.font = {name: 'Arial', size: 10, color: '#202D32'};
    area.format.rowHeight = 29;
    area.format.verticalAlignment = 'center';
    sh.getRange('A1').values = [[s.title]];
    sh.getRange(`A1:${last}1`).format.font = {name: 'Arial', size: 15, bold: true, color: accent};
    sh.getRange(`A1:${last}1`).format.rowHeight = 34;
    sh.getRange('A2').values = [[s.subtitle]];
    sh.getRange(`A2:${last}2`).format.font = {name: 'Arial', size: 10, color: '#536269'};
    sh.getRange('A3').values = [[`${spec.author}, Stand ${spec.date.split('-').reverse().join('.')}`]];
    sh.getRange(`A3:${last}3`).format.borders = {bottom: {style: 'thin', color: accent}};
    sh.getRange('A4').values = [['Positionen']];
    sh.getRange('A5').values = [[s.rows.length]];
    sh.getRange(`A5:${last}5`).format.font = {name: 'Arial', size: 13, bold: true, color: accent};
    sh.getRange(`A6:${last}7`).format.rowHeight = 12;
    sh.getRange(`A8:${last}8`).values = [s.columns.map(c => c.label)];
    const values = s.rows.map(row => row.map((v, j) => {
      if (typeof v === 'string' && v.startsWith('=')) return null;
      if (s.columns[j].type === 'date' && typeof v === 'string') return dateValue(v);
      if (s.columns[j].type === 'time' && typeof v === 'string') return timeValue(v);
      return v;
    }));
    // Text identifiers must retain leading zeroes and dotted position numbers.
    for (const [j, c] of s.columns.entries()) {
      sh.getRange(`${column(j)}9:${column(j)}${end}`).setNumberFormat(c.type === 'text' ? '@' : formats[c.type]);
      sh.getRange(`${column(j)}1:${column(j)}${end}`).format.columnWidth = c.width;
      sh.getRange(`${column(j)}9:${column(j)}${end}`).format.horizontalAlignment = c.type === 'text' ? 'left' : 'right';
    }
    sh.getRange(`A9:${last}${end}`).values = values;
    for (const [i, row] of s.rows.entries()) {
      for (const [j, v] of row.entries()) {
        const cell = sh.getRange(`${column(j)}${i + 9}`);
        if (typeof v === 'string' && v.startsWith('=')) {
          cell.formulas = [[v]];
          if (s.columns.some(c => c.type === 'money')) cell.format.font.color = v.includes('!') ? '#23704B' : '#202D32';
        } else if (typeof v === 'number' && s.columns.some(c => c.type === 'money')) cell.format.font.color = '#245E9A';
      }
      sh.getRange(`A${i + 9}:${last}${i + 9}`).format.fill = i % 2 ? '#F0F4F3' : '#FFFFFF';
    }
    const table = sh.tables.add(`A8:${last}${end}`, true, `Register${index + 1}_${sheetIndex + 1}`);
    table.style = 'TableStyleMedium2';
    table.showFilterButton = true;
    for (const [j, c] of s.columns.entries()) sh.getRange(`${column(j)}9:${column(j)}${end}`).setNumberFormat(c.format ?? formats[c.type]);
    const header = sh.getRange(`A8:${last}8`);
    header.format = {fill: accent, font: {name: 'Arial', size: 10, bold: true, color: '#FFFFFF'}, wrapText: true, horizontalAlignment: 'center', verticalAlignment: 'center', rowHeight: 42};
    sh.getRange(`A9:${last}${end}`).format.wrapText = true;
    for (const [i, row] of s.rows.entries()) {
      const lines = Math.max(1, ...row.map((v, j) => s.columns[j].type === 'text' && typeof v === 'string' && !v.startsWith('=') ? Math.ceil(v.length / (s.columns[j].width * 0.9)) : 1));
      sh.getRange(`A${i + 9}:${last}${i + 9}`).format.rowHeight = Math.max(22, lines * 14 + 6);
    }
    for (const j of s.totals ?? []) {
      assert.ok(j > 0 && j < s.columns.length);
      const c = column(j);
      sh.getRange(`${c}4`).values = [[s.columns[j].label]];
      sh.getRange(`${c}4`).format.wrapText = true;
      sh.getRange(`${c}4`).format.font.size = 9;
      sh.getRange(`${c}5`).formulas = [[`=SUM(${c}9:${c}${end})`]];
      sh.getRange(`${c}5`).setNumberFormat(s.columns[j].format ?? formats[s.columns[j].type]);
    }
    sh.getRange(`A4:${last}4`).format.rowHeight = 34;
    sh.freezePanes.freezeRows(8);
  }
  wb.recalculate();
  for (const s of spec.sheets) {
    const sh = wb.worksheets.getItem(s.name);
    for (let i = 0; i < s.rows.length; i++) for (let j = 0; j < s.columns.length; j++) {
      if (s.columns[j].type !== 'number') continue;
      const cell = sh.getRange(`${column(j)}${i + 9}`), v = cell.values[0][0];
      if (typeof v === 'number' && v !== 0 && Math.abs(v) < 0.005) cell.setNumberFormat('[$-407]0.00E+00" "');
    }
  }
  for (const c of spec.controls) checkedValue(wb, c);
  for (const s of spec.sheets) {
    const sh = wb.worksheets.getItem(s.name);
    for (const row of sh.getUsedRange().values) {
      for (const v of row) assert.ok(!errorPattern.test(String(v)), `${spec.slug}/${s.name}: ${v}`);
    }
  }
  const m = spec.mutation;
  const input = wb.worksheets.getItem(m.sheet).getRange(m.cell);
  const originalValue = input.values[0][0], originalFormula = input.formulas?.[0]?.[0];
  const before = wb.worksheets.getItem(m.outputSheet).getRange(m.outputCell).values[0][0];
  input.values = [[typeof m.value === 'string' && /^\d{2}:\d{2}$/.test(m.value) ? timeValue(m.value) : m.value]];
  wb.recalculate();
  checkedValue(wb, {sheet: m.outputSheet, cell: m.outputCell, value: m.expected});
  assert.notEqual(before, m.expected, 'Die Mutation muss ein Ergebnis verändern.');
  await (await SpreadsheetFile.exportXlsx(wb)).save(path.join(review, 'mutation.xlsx'));
  if (originalFormula) input.formulas = [[originalFormula]];
  else input.values = [[originalValue]];
  wb.recalculate();
  for (const c of spec.controls) checkedValue(wb, c);
  for (const [i, s] of spec.sheets.entries()) {
    const image = await wb.render({sheetName: s.name, range: `A1:${column(s.columns.length - 1)}${Math.min(19, s.rows.length + 8)}`, scale: 1.5});
    await fs.writeFile(path.join(review, `blatt-${i + 1}.png`), new Uint8Array(await image.arrayBuffer()));
  }
  const inspection = await wb.inspect({kind: 'table', range: `${spec.sheets[0].name}!A4:I12`, include: 'values,formulas', tableMaxRows: 9, tableMaxCols: 9, maxChars: 4500});
  await fs.writeFile(path.join(review, 'inspection.ndjson'), inspection.ndjson);
  await (await SpreadsheetFile.exportXlsx(wb)).save(path.join(dir, spec.filename));
  console.log(JSON.stringify({case: spec.slug, sheets: spec.sheets.length, rows: spec.sheets.reduce((n, s) => n + s.rows.length, 0), controls: spec.controls.length, mutation: true}));
}

import { copyFile, readFile, writeFile, mkdir } from 'node:fs/promises';
import { basename, dirname, join } from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const [input, previewDirectory] = process.argv.slice(2);
const workbooks = JSON.parse(await readFile(input, 'utf8'));
if (previewDirectory) await mkdir(previewDirectory, { recursive: true });

const ink = '#173D42';
const muted = '#4A6468';
const stripe = '#EEF4F3';

function columnName(index) {
  let name = '';
  for (let n = index + 1; n > 0; n = Math.floor((n - 1) / 26)) {
    name = String.fromCharCode(65 + (n - 1) % 26) + name;
  }
  return name;
}

function buildSheet(sheet, spec) {
  const last = columnName(spec.headers.length - 1);
  const rowCount = spec.rows.length + 3;
  const widths = spec.headers.map((label, index) => {
    const widest = Math.max(label.length, ...spec.rows.map((row) => String(row[index] ?? '').length));
    return Math.min(31, Math.max(13, widest * 0.8 + 2));
  });
  const range = sheet.getRange(`A1:${last}${rowCount}`);
  range.format.font.name = 'Arial';
  range.format.font.size = 10;
  range.format.verticalAlignment = 'center';
  sheet.showGridLines = false;
  sheet.getRange(`A1:${last}1`).merge();
  sheet.getRange('A1').values = [[spec.title || spec.name]];
  sheet.getRange(`A1:${last}1`).format = {
    fill: ink, font: { name: 'Arial', color: '#FFFFFF', bold: true, size: 13 }, rowHeight: 26,
  };
  sheet.getRange(`A2:${last}2`).merge();
  sheet.getRange('A2').values = [[spec.note || 'Bildungscampus Leineaue · Einkauf']];
  sheet.getRange(`A2:${last}2`).format = {
    fill: stripe, font: { color: muted, italic: true, size: 9 }, rowHeight: 28, wrapText: true,
  };
  sheet.getRange(`A3:${last}3`).values = [spec.headers];
  sheet.getRange(`A3:${last}3`).format = {
    fill: ink, font: { color: '#FFFFFF', bold: true }, rowHeight: 29, wrapText: true,
  };
  if (spec.rows.length) {
    sheet.getRange(`A4:${last}${rowCount}`).values = spec.rows;
    sheet.getRange(`A4:${last}${rowCount}`).format.wrapText = true;
    spec.rows.forEach((row, index) => {
      const maxChars = Math.max(...row.map((cell) => String(cell ?? '').length));
      const line = sheet.getRange(`A${index + 4}:${last}${index + 4}`);
      line.format.rowHeight = maxChars > 110 ? 56 : maxChars > 45 ? 38 : 25;
      if (index % 2 === 0) line.format.fill = stripe;
    });
  }
  spec.headers.forEach((label, index) => {
    const column = columnName(index);
    sheet.getRange(`${column}:${column}`).format.columnWidth = widths[index];
    if (/EUR|Euro|netto/i.test(label) && spec.rows.some((row) => typeof row[index] === 'number')) {
      sheet.getRange(`${column}4:${column}${rowCount}`).setNumberFormat('#,##0.00');
    }
  });
  for (const column of spec.textColumns || []) {
    sheet.getRange(`${column}4:${column}${rowCount}`).setNumberFormat('@');
  }
  for (const [address, formula] of Object.entries(spec.formulas || {})) {
    sheet.getRange(address).formulas = [[formula]];
    sheet.getRange(address).setNumberFormat(spec.formulaFormat || '#,##0.00');
    sheet.getRange(address).format.fill = '#DCEAE8';
  }
  sheet.freezePanes.freezeRows(3);
  return { sheetName: spec.name, range: `A1:${last}${rowCount}`, scale: 1.4 };
}

for (const spec of workbooks) {
  const workbook = Workbook.create();
  const sheets = spec.sheets.map((sheet) => workbook.worksheets.add(sheet.name));
  const views = spec.sheets.map((sheet, index) => buildSheet(sheets[index], sheet));
  workbook.recalculate();
  if (previewDirectory) {
    for (const [index, view] of views.entries()) {
      const blob = await workbook.render(view);
      await writeFile(join(previewDirectory, `${spec.caseId}-${basename(spec.path, '.xlsx')}-${index + 1}.png`),
        new Uint8Array(await blob.arrayBuffer()));
    }
  }
  await mkdir(dirname(spec.path), { recursive: true });
  const file = await SpreadsheetFile.exportXlsx(workbook);
  const staged = join(dirname(input), `${spec.caseId}-${basename(spec.path)}`);
  await file.save(staged);
  await copyFile(staged, spec.path);
}

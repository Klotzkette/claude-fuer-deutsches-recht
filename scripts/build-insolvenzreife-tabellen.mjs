import { readFile, mkdir, writeFile, unlink } from 'node:fs/promises';
import { join } from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const [fixture, root, previewDir] = process.argv.slice(2);
if (!previewDir) throw new Error('Aufruf: fixture.json Zielrepository Vorschauverzeichnis');
const { cases } = JSON.parse(await readFile(fixture, 'utf8'));
const moneyFormat = '#,##0.00;[Red]-#,##0.00';
const amount = cents => cents == null ? null : cents / 100;
const column = number => String.fromCharCode(65 + number);

function sheet(book, name, company, headers, rows, widths, moneyColumns = []) {
  const tab = book.worksheets.add(name);
  tab.showGridLines = false;
  const last = column(headers.length - 1);
  tab.mergeCells(`A1:${last}1`);
  tab.getRange('A1').values = [[name]];
  tab.getRange(`A1:${last}1`).format = {
    rowHeight: 27, fill: '#183039', font: { name: 'Arial', size: 16, bold: true, color: '#FFFFFF' },
  };
  tab.mergeCells(`A2:${last}2`);
  tab.getRange('A2').values = [[company]];
  tab.getRange(`A2:${last}2`).format = { rowHeight: 20, font: { name: 'Arial', size: 10, color: '#006663' } };
  tab.getRange(`A4:${last}4`).values = [headers];
  tab.getRange(`A4:${last}4`).format = {
    rowHeight: 29, wrapText: true, verticalAlignment: 'center', fill: '#006663',
    font: { name: 'Arial', size: 10, color: '#FFFFFF', bold: true },
  };
  if (rows.length) {
    tab.getRange(`A5:${last}${4 + rows.length}`).values = rows;
    tab.getRange(`A5:${last}${4 + rows.length}`).format = {
      rowHeight: 19, font: { name: 'Arial', size: 10, color: '#183039' },
    };
    for (let i = 0; i < rows.length; i += 2) tab.getRange(`A${i + 5}:${last}${i + 5}`).format.fill = '#EAF2F1';
    for (const col of moneyColumns) tab.getRange(`${col}5:${col}${4 + rows.length}`).setNumberFormat(moneyFormat);
  }
  for (const [index, width] of widths.entries()) {
    const col = column(index);
    tab.getRange(`${col}:${col}`).format.columnWidth = width;
  }
  tab.freezePanes.freezeRows(4);
  return tab;
}

await mkdir(previewDir, { recursive: true });
for (const entry of cases) {
  const book = Workbook.create();
  const liabilities = [];
  const assets = [];
  const forecasts = [];
  const assumptions = [];
  for (const snapshot of entry.valuations) {
    for (const row of snapshot.assets) assets.push([
      snapshot.date, row.item, amount(row.book_cents), amount(row.liquidation_cents), row.source,
    ]);
    for (const row of snapshot.liabilities) liabilities.push([
      snapshot.date, row.item, amount(row.amount_cents), row.source,
    ]);
    const forecast = snapshot.forecast;
    for (const row of forecast.months) forecasts.push([
      snapshot.date, row.from_date, row.through_date, amount(row.opening_cents), amount(row.operating_in_cents),
      amount(row.operating_out_cents), amount(row.financing_in_cents), amount(row.financing_out_cents),
      amount(row.closing_cents), row.source || forecast.source, null,
    ]);
    for (const note of [...forecast.assumptions, forecast.notes].filter(Boolean)) assumptions.push([
      snapshot.date, String(note), forecast.source,
    ]);
  }
  const checkpoints = entry.status_dates.map(value => [value]);
  const t = sheet(book, 'Stichtage', entry.company, ['Stichtag'], checkpoints, [22]);
  t.getRange('C4').values = [['Beträge in EUR. Bankjournal und OP-Listen liegen als getrennte Exporte vor.']];
  t.getRange('C:C').format.columnWidth = 95;
  sheet(book, 'Vermögenswerte', entry.company, ['Stichtag', 'Position', 'Buchwert EUR', 'Verwertungswert EUR', 'Herkunft'],
    assets, [16, 47, 19, 23, 56], ['C', 'D']);
  sheet(book, 'Verbindlichkeiten', entry.company, ['Stichtag', 'Position', 'Nennbetrag EUR', 'Herkunft'],
    liabilities, [16, 51, 21, 64], ['C']);
  const projection = sheet(book, 'Finanzplanung', entry.company, ['Planstand', 'Von', 'Bis', 'Anfang EUR', 'Betrieb ein EUR',
    'Betrieb aus EUR', 'Finanzierung ein EUR', 'Finanzierung aus EUR', 'Plan Ende EUR', 'Herkunft', 'Rechenabgleich EUR'],
    forecasts, [14, 14, 14, 15, 16, 16, 19, 19, 16, 30, 18], ['D', 'E', 'F', 'G', 'H', 'I', 'K']);
  const inputEnd = 4 + forecasts.length;
  projection.getRange(`K5:K${inputEnd}`).formulas = forecasts.map((_, i) => {
    const row = i + 5;
    return [`=ROUND(D${row}+E${row}-F${row}+G${row}-H${row}-I${row},2)`];
  });
  const notes = sheet(book, 'Planannahmen', entry.company, ['Planstand', 'Annahme laut Akte', 'Herkunft'],
    assumptions, [16, 100, 47]);
  if (assumptions.length) {
    notes.getRange(`B5:C${4 + assumptions.length}`).format.wrapText = true;
    notes.getRange(`A5:C${4 + assumptions.length}`).format.rowHeight = 49;
  }
  book.recalculate();
  const differences = projection.getRange(`K5:K${inputEnd}`).values.flat();
  if (differences.some(value => value !== 0)) throw new Error(`Planabweichung ${entry.slug}: ${differences}`);
  for (const [sheetName, range] of [['Vermögenswerte', 'A1:E13'], ['Finanzplanung', 'A1:K13'], ['Planannahmen', 'A1:C9']]) {
    const preview = await book.render({ sheetName, range, scale: 1, format: 'png' });
    await writeFile(join(previewDir, `${entry.slug}-${sheetName}.png`), new Uint8Array(await preview.arrayBuffer()));
  }
  const directory = join(root, 'testakten', entry.slug, '02_Buchhaltung');
  await mkdir(directory, { recursive: true });
  const target = join(directory, '05_Stichtagsunterlagen.xlsx');
  const file = await SpreadsheetFile.exportXlsx(book);
  await file.save(target);
  try { await unlink(target + '.inspect.ndjson'); } catch (error) { if (error.code !== 'ENOENT') throw error; }
  console.log(`${entry.slug}: ${assets.length} Werte, ${liabilities.length} Verbindlichkeiten und ${forecasts.length} Planmonate geprüft`);
}

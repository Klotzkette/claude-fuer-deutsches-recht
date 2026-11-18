#!/usr/bin/env node
/** Creates the empty Wolkenwerft worksheet with the bundled Artifact Tool. */
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const option = (name) => {
  const index = args.indexOf(name);
  return index >= 0 ? args[index + 1] : undefined;
};
const output = option('--output');
if (!output || output.startsWith('--')) {
  throw new Error('Usage: node scripts/build-jugendmedien-vorlage.mjs --output <xlsx-path> [--preview <png-path>]');
}

const runtimeModules = process.env.CODEX_RUNTIME_NODE_MODULES || path.join(
  os.homedir(), '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules',
);
await fs.access(runtimeModules);
const workspace = await fs.mkdtemp(path.join(os.tmpdir(), 'jugendmedien-xlsx-'));
await fs.symlink(runtimeModules, path.join(workspace, 'node_modules'), 'dir');
const runtimeRequire = createRequire(path.join(workspace, 'runtime.cjs'));
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(runtimeRequire.resolve('@oai/artifact-tool')).href);

const workbook = Workbook.create();
const sheet = workbook.worksheets.add('Sachverhalt');
sheet.showGridLines = false;
sheet.tabColor = '#273C59';
const headers = ['ID', 'Funktion', 'Zeitstand', 'Tatsachenbeleg', 'Offene Frage', 'Quelle', 'Ergebnis', 'Maßnahme', 'Zuständig', 'Frist', 'Nachweis', 'Wiedervorlage'];
const widths = [9, 24, 18, 34, 34, 30, 32, 30, 22, 18, 30, 20];
sheet.getRange('A1:L17').format.font = { name: 'Times New Roman', size: 11, color: '#243144' };
sheet.getRange('A1:L17').format.verticalAlignment = 'center';
sheet.getRange('A2').values = [['Inselatlas: Sachverhalt und Bearbeitung']];
sheet.getRange('A2').format.font = { name: 'Times New Roman', size: 15, bold: true, color: '#273C59' };
sheet.getRange('A2:L2').format.rowHeight = 25;
sheet.getRange('A3').values = [['Fiktive Schulungsakte. Leere Arbeitsvorlage zum eigenen Befüllen; keine Musterlösung.']];
sheet.getRange('A3:L3').format.rowHeight = 20;
sheet.getRange('A3:L3').format.font = { name: 'Times New Roman', size: 11, italic: true, color: '#53647B' };
sheet.getRange('A4:L4').format.rowHeight = 9;
sheet.getRange('A5:L5').values = [headers];
sheet.getRange('A5:L5').format = {
  fill: '#273C59',
  font: { name: 'Times New Roman', size: 11, bold: true, color: '#FFFFFF' },
  rowHeight: 30,
  horizontalAlignment: 'center',
  verticalAlignment: 'center',
  wrapText: false,
  borders: { insideVertical: { style: 'thin', color: '#FFFFFF' } },
};
sheet.getRange('A6:L17').values = Array.from({ length: 12 }, () => Array(12).fill(null));
sheet.getRange('A6:L17').format.rowHeight = 31;
sheet.getRange('A6:L17').format.wrapText = true;
sheet.getRange('A6:L17').format.verticalAlignment = 'top';
for (let row = 6; row <= 17; row++) {
  sheet.getRange(`A${row}:L${row}`).format.fill = row % 2 === 0 ? '#FFF9ED' : '#FFFFFF';
  sheet.getRange(`A${row}:L${row}`).format.borders = { bottom: { style: 'thin', color: '#E3E8EF' } };
}
for (let col = 0; col < 12; col++) {
  sheet.getRangeByIndexes(0, col, 17, 1).format.columnWidth = widths[col];
}
sheet.getRange('J6:J17').setNumberFormat('dd.mm.yyyy');
sheet.getRange('L6:L17').setNumberFormat('dd.mm.yyyy');
sheet.freezePanes.freezeRows(5);
sheet.freezePanes.freezeColumns(2);

workbook.recalculate();
const blanks = sheet.getRange('A6:L17').values;
if (blanks.some(row => row.some(value => value !== null && value !== ''))) {
  throw new Error('The template must not contain completed answers.');
}
const review = await workbook.inspect({ kind: 'table', range: 'Sachverhalt!A5:L7', include: 'values,formulas', tableMaxRows: 3, tableMaxCols: 12, maxChars: 1800 });
console.log(review.ndjson);
const errors = await workbook.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!', options: { useRegex: true, maxResults: 20 }, summary: 'Template formula-error scan', maxChars: 1000 });
console.log(errors.ndjson);
const previewPath = path.resolve(option('--preview') || path.join(workspace, 'vorlage.png'));
await fs.mkdir(path.dirname(previewPath), { recursive: true });
const preview = await workbook.render({ sheetName: 'Sachverhalt', range: 'A1:L17', scale: 1, format: 'png' });
await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));
await fs.mkdir(path.dirname(path.resolve(output)), { recursive: true });
const file = await SpreadsheetFile.exportXlsx(workbook);
await file.save(path.resolve(output));
// Artifact Tool may emit its own diagnostic sidecar; it is not an exercise file.
await fs.rm(`${path.resolve(output)}.inspect.ndjson`, { force: true });
console.log(JSON.stringify({ output: path.resolve(output), preview: previewPath, sheet: 'Sachverhalt', blankRows: 12, columns: 12 }));

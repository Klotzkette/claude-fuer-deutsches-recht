#!/usr/bin/env node
// Creates only the new workbook. Previews and native recalculation stay in a temporary directory.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import { constants } from 'node:fs';
import { execFile } from 'node:child_process';
import { createRequire } from 'node:module';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { promisify } from 'node:util';

const run = promisify(execFile);
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const runtime = path.join(process.env.HOME, '.cache/codex-runtimes/codex-primary-runtime/dependencies');
const python = path.join(runtime, 'python/bin/python3');
const office = path.join(runtime, 'native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/MacOS/soffice');
const caseDir = path.join(root, 'testakten/inkasso-zahlungsklage-modefuchs');
const filename = '31_Forderungskonto_Arbeitsstand_20250705.xlsx';
const target = path.join(caseDir, filename);
const qaOnly = process.argv.includes('--qa-only');
assert(process.argv.slice(2).every(arg => arg === '--qa-only'), 'Only --qa-only is supported.');
if (!qaOnly) {
  await assert.rejects(fs.access(target), { code: 'ENOENT' }, 'Existing workbooks are never overwritten.');
}
const qaDir = await fs.mkdtemp(path.join(tmpdir(), 'modefuchs-forderungskonto-'));
await fs.symlink(path.join(runtime, 'node/node_modules'), path.join(qaDir, 'node_modules'), 'dir');
const require = createRequire(path.join(qaDir, 'runtime.cjs'));
const { SpreadsheetFile, Workbook } = await import(pathToFileURL(require.resolve('@oai/artifact-tool')).href);

const pdfNames = [
  '01_Bestellbestaetigung_03-04-2025.pdf', '04_Rechnung_R-20250406-3098.pdf',
  '06_Zweite_Mahnung_E-Mail_04-05-2025.pdf', '09_Abtretungserklaerung_08-06-2025.pdf',
  '12_Gebuehrenrechnung_Inkasso_10-06-2025.pdf', '13_Interner_Eingangsvermerk_Inkasso_08-06-2025.pdf',
  '15_Zahlungsnotiz_Inkasso_01-07-2025.pdf', '19_Kontoauszug_Altenhausen_26-06-2025.pdf',
  '27_Zahlungsbestaetigung_ModeFuchs_30-06-2025.pdf',
  '21_Mahnbescheid_Antrag_InkassoZentrale_05-07-2025.pdf',
];
const { stdout: pdfJson } = await run(python, ['-B', '-c',
  'import json,sys; from pypdf import PdfReader; print(json.dumps(["\\n".join(p.extract_text() or "" for p in PdfReader(f).pages) for f in sys.argv[1:]]))',
  ...pdfNames.map(name => path.join(caseDir, 'originale', name)),
]);
const pdfTexts = JSON.parse(pdfJson);
for (const [index, marker] of [[0, 'MF-20250403-1749'], [1, '698,00'], [2, '5,50'], [3, '714,30'],
  [4, '83,54'], [5, 'IZ-MF-2025-1749'], [6, '01.07.2025'], [7, '26.06.2025'], [8, '28.06.2025'], [9, '797,84']]) {
  assert(pdfTexts[index].includes(marker), `${pdfNames[index]}: missing ${marker}`);
}
const facts = {
  invoice: { number: pdfTexts[1].match(/R-\d{8}-\d{4}/)[0] },
  original_creditor: { name: pdfTexts[0].split('\n')[0].trim() },
  debtor: { name: 'Gottlieb von Altenhausen' },
};
assert.equal(facts.invoice.number, 'R-20250406-3098');
assert.equal(facts.original_creditor.name, 'ModeFuchs GmbH');
assert(pdfTexts[1].includes(facts.debtor.name));
assert(pdfTexts[4].startsWith('InkassoZentrale GmbH'));
const labels = ['Hauptforderung', 'Mahngebühren', 'Verzugszinsen', 'Inkassokosten'];
const charges = labels.map(label => {
  const match = pdfTexts[9].match(new RegExp(`${label}[^€\\n]*€\\s*([\\d.,]+)`));
  assert(match, `Missing source amount: ${label}`);
  return Number(match[1].replaceAll('.', '').replace(',', '.'));
});
assert.deepEqual(charges, [698, 5.5, 10.8, 83.54]);
assert.equal(charges.reduce((sum, value) => sum + Math.round(value * 100), 0), 79784);
const principal = charges[0];
const mail = await fs.readFile(path.join(caseDir, '10_email_zahlungseingang_modefuchs_inkasso.eml'), 'utf8');
assert(mail.includes('Denise Radtke') && mail.includes('Sabine Wienecke'));
const correspondence = JSON.parse(await fs.readFile(path.join(root, 'scripts/fixtures/modefuchs/korrespondenz.json'), 'utf8'));
assert(JSON.stringify(correspondence).includes('am 30.06. ungekürzt an die InkassoZentrale weitergeleitet'));

const workbook = Workbook.create();
const ledger = workbook.worksheets.add('Forderungskonto');
const notes = workbook.worksheets.add('Zahlungsbelege');
const colors = { ink: '#252B29', muted: '#58605D', header: '#40544B', line: '#CFD6D2', total: '#E8EEEA', input: '#24548A' };
const currency = '#,##0.00;(#,##0.00);0.00';
const date = value => new Date(`${value}T00:00:00.000Z`);
function cell(sheet, address, value) { sheet.getRange(address).values = [[value]]; }
function base(sheet, range, widths) {
  sheet.showGridLines = false;
  sheet.getRange(range).format.font = { name: 'Arial', size: 11, color: colors.ink };
  sheet.getRange(range).format.rowHeight = 23;
  sheet.getRange(range).format.verticalAlignment = 'center';
  for (const [column, width] of Object.entries(widths)) sheet.getRange(`${column}1:${column}28`).format.columnWidthPx = width;
  sheet.getRange('A1:G1').format.rowHeight = 12;
}
function header(sheet, range) {
  sheet.getRange(range).format = {
    fill: colors.header, font: { name: 'Arial', size: 11, bold: true, color: '#FFFFFF' },
    horizontalAlignment: 'center', verticalAlignment: 'center', wrapText: true,
    borders: { insideVertical: { style: 'thin', color: '#FFFFFF' } },
  };
}
base(ledger, 'A1:H27', { A: 135, B: 220, C: 174, D: 132, E: 132, F: 120, G: 18, H: 265 });
// Keep the ledger total with its column headings in the native print layout.
ledger.getRange('A4:H4').format.rowHeight = 8;
ledger.getRange('A9:H9').format.rowHeight = 8;
ledger.tabColor = colors.header;
cell(ledger, 'A2', 'InkassoZentrale GmbH');
cell(ledger, 'A3', 'Forderungskonto');
ledger.getRange('A2').format.font = { size: 16, bold: true };
ledger.getRange('A3').format.font = { size: 14, bold: true };
ledger.getRange('A3:H3').format.borders = { bottom: { style: 'thin', color: colors.line } };
for (const [address, value] of Object.entries({
  A5: 'Stand', B5: date('2025-07-05'), C5: 'Vorgang', D5: 'IZ-MF-2025-1749',
  A6: 'Kundenkonto', B6: 'KD-0047-ALT', C6: 'Schuldner', D6: facts.debtor.name,
  A7: 'Rechnung', B7: facts.invoice.number, C7: 'Bestellung', D7: 'MF-20250403-1749',
  A8: 'Auftraggeberin', B8: facts.original_creditor.name, C8: 'Bearbeitung', D8: 'Denise Radtke',
  A10: 'Übernommene Belastungen und eingegangene Gutschriften. Zahlung unaufgeteilt gebucht.',
})) cell(ledger, address, value);
ledger.getRange('B5').setNumberFormat('yyyy-mm-dd');
ledger.getRange('B5').format.horizontalAlignment = 'left';
ledger.getRange('A5:A8').format.font.color = colors.muted;
ledger.getRange('C5:C8').format.font.color = colors.muted;
ledger.getRange('A10').format.font = { italic: true, color: colors.muted };
ledger.getRange('A11:F16').values = [
  ['Belegdatum', 'Buchungstext', 'Beleg', 'Angeforderte\nBelastungen (EUR)', 'Eingegangene\nGutschriften (EUR)', 'Buchsaldo (EUR)'],
  [date('2025-06-08'), 'Übernahme Hauptforderung', facts.invoice.number, charges[0], 0, null],
  [date('2025-06-08'), 'Mahngebühren, Vorbestand', 'Mahnung 04.05.2025', charges[1], 0, null],
  [date('2025-06-08'), 'Zinsen, Vorbestand', 'Abtretung 08.06.2025', charges[2], 0, null],
  [date('2025-06-10'), 'Inkassokosten', 'IZ-R-20250610-88291', charges[3], 0, null],
  [date('2025-07-01'), 'Zahlungseingang aus Weiterleitung ModeFuchs GmbH', 'Zahlungsnotiz 01.07.2025', 0, principal, null],
];
header(ledger, 'A11:F11');
cell(ledger, 'H11', 'Belegquelle');
ledger.getRange('H11').format.font.bold = true;
ledger.getRange('H12:H16').values = [
  ['04 Rechnung; 13 Eingangsvermerk (je S. 1)'],
  ['06 Mahnung; 13 Eingangsvermerk (je S. 1)'],
  ['09 Abtretung; 13 Eingangsvermerk (je S. 1)'],
  ['12 Gebührenrechnung, S. 1'],
  ['15 Zahlungsnotiz, S. 1'],
];
ledger.getRange('A12:A16').setNumberFormat('yyyy-mm-dd');
ledger.getRange('A12:A16').format.horizontalAlignment = 'left';
ledger.getRange('D12:F17').setNumberFormat(currency);
ledger.getRange('D12:E16').format.font.color = colors.input;
ledger.getRange('D12:F17').format.horizontalAlignment = 'right';
ledger.getRange('F12').formulas = [['=ROUND(D12-E12,2)']];
ledger.getRange('F13').formulas = [['=ROUND(SUM(F12,D13)-E13,2)']];
ledger.getRange('F13:F16').fillDown();
ledger.getRange('A11:H11').format.rowHeight = 48;
ledger.getRange('A12:H16').format.rowHeight = 42;
ledger.getRange('B12:C16').format.wrapText = true;
ledger.getRange('H12:H16').format.wrapText = true;
ledger.getRange('H12:H16').format.font = { size: 10, color: colors.muted };
cell(ledger, 'B17', 'Summen und Buchsaldo');
ledger.getRange('D17:F17').formulas = [['=ROUND(SUM(D12:D16),2)', '=ROUND(SUM(E12:E16),2)', '=F16']];
ledger.getRange('A17:F17').format.fill = colors.total;
ledger.getRange('A17:F17').format.font.bold = true;
ledger.getRange('A17:F17').format.borders = { top: { style: 'thin', color: colors.header } };
for (const [address, value] of Object.entries({
  A19: 'Zinsen als Vorbestand übernommen. Keine Fortschreibung nach Tagen oder Zinssätzen.',
  A20: 'Übergabe-Nebenforderungen 16,30 EUR: Mahngebühren 5,50 EUR und Zinsen 10,80 EUR (Abtretung, S. 1).',
  A21: 'Gutschrift vom 01.07.2025 ohne Aufteilung auf Hauptforderung, Gebühren und Zinsen erfasst.',
  A23: 'Verfahrensnotiz vom 05.07.2025',
  A24: 'Mahnbescheidsantrag: 797,84 EUR laut Antragsbeleg. Keine zusätzliche Belastungsbuchung.',
  A25: 'Belegquelle: 21 Mahnbescheid-Antrag InkassoZentrale, 05.07.2025, S. 1.',
})) cell(ledger, address, value);
ledger.getRange('A19:A21').format.font = { size: 10, color: colors.muted };
ledger.getRange('A23').format.font.bold = true;
ledger.getRange('A25').format.font = { size: 10, color: colors.muted };

base(notes, 'A1:F23', { A: 105, B: 190, C: 133, D: 370, E: 18, F: 260, G: 18 });
cell(notes, 'A2', 'Zahlungsbelege');
notes.getRange('A2').format.font = { size: 16, bold: true };
cell(notes, 'A3', 'InkassoZentrale GmbH');
notes.getRange('A3:F3').format.borders = { bottom: { style: 'thin', color: colors.line } };
cell(notes, 'A5', 'Vorgang');
cell(notes, 'B5', 'IZ-MF-2025-1749');
cell(notes, 'D5', 'Rechnung R-20250406-3098');
cell(notes, 'A6', 'Arbeitsstand');
cell(notes, 'B6', date('2025-07-05'));
notes.getRange('B6').setNumberFormat('yyyy-mm-dd');
notes.getRange('B6').format.horizontalAlignment = 'left';
notes.getRange('A8:D12').values = [
  ['Belegdatum', 'Beleg', 'Betrag (EUR)', 'Vermerk'],
  [date('2025-06-26'), 'Kontoauszug 2025/12', principal,
    'Überweisung von Gottlieb von Altenhausen am 26.06.2025 an ModeFuchs GmbH. Verwendungszweck R-20250406-3098.'],
  [date('2025-06-30'), 'Zahlungsbestätigung ModeFuchs GmbH', principal,
    'Eingang bei ModeFuchs GmbH am 28.06.2025 bestätigt. Der Betrag wurde der Rechnung zugeordnet.'],
  [date('2025-06-30'), 'Weiterleitung ModeFuchs GmbH', principal,
    'ModeFuchs GmbH hat den Betrag am 30.06.2025 an InkassoZentrale GmbH weitergeleitet.'],
  [date('2025-07-01'), 'Interne Zahlungsnotiz InkassoZentrale GmbH', principal,
    'Eingang und Verbuchung auf dem Inkassokonto am 01.07.2025. Als eine Gutschrift im Forderungskonto erfasst.'],
];
header(notes, 'A8:D8');
cell(notes, 'F8', 'Belegquelle');
notes.getRange('F8').format.font.bold = true;
notes.getRange('F9:F12').values = [
  ['19 Kontoauszug Altenhausen, S. 1'], ['27 Zahlungsbestätigung 30.06.2025, S. 1'],
  ['Weiterleitung_Direktzahlung_1749.eml, 01.07.2025'], ['15 Zahlungsnotiz 01.07.2025, S. 1'],
];
notes.getRange('A9:A12').setNumberFormat('yyyy-mm-dd');
notes.getRange('A9:A12').format.horizontalAlignment = 'left';
// Literal display padding separates the amount from the adjacent note without changing its value.
notes.getRange('C9:C12').setNumberFormat('#,##0.00"   ";(#,##0.00)"   ";0.00"   "');
notes.getRange('C9:C12').format.horizontalAlignment = 'right';
notes.getRange('A8:F8').format.rowHeight = 32;
notes.getRange('A9:F12').format.rowHeight = 72;
notes.getRange('B9:B12').format.wrapText = true;
notes.getRange('D9:D12').format.wrapText = true;
notes.getRange('F9:F12').format.wrapText = true;
notes.getRange('F9:F12').format.font = { size: 10, color: colors.muted };
cell(notes, 'A14', 'Alle Vermerke betreffen dieselbe Zahlung über 698,00 EUR. Die Beträge sind nicht zu addieren.');
notes.getRange('A14').format.font = { size: 10, italic: true, color: colors.muted };
cell(notes, 'A16', 'Buchungszuordnung');
notes.getRange('A16').format.font.bold = true;
cell(notes, 'A17', 'Der Eingang bei ModeFuchs am 28.06.2025 ist von der Überweisung des Schuldners am 26.06.2025 zu trennen.');
cell(notes, 'A18', 'Für das Inkassokonto ist der bestätigte Eingang am 01.07.2025 als Gutschrift übernommen.');
cell(notes, 'A20', 'Kontakt ModeFuchs GmbH: Sabine Wienecke, Buchhaltung.');
cell(notes, 'A21', 'Bearbeitung InkassoZentrale GmbH: Denise Radtke, Forderungsmanagement.');

workbook.recalculate();
const expected = [698, 703.5, 714.3, 797.84, 99.84];
for (let index = 0; index < expected.length; index++) {
  assert(Math.abs(ledger.getRange(`F${12 + index}`).values[0][0] - expected[index]) < 1e-8);
}
assert(Math.abs(ledger.getRange('D17').values[0][0] - 797.84) < 1e-8);
assert.equal(ledger.getRange('E17').values[0][0], 698);
const inspection = await workbook.inspect({ kind: 'table', range: 'Forderungskonto!A11:F17', include: 'values,formulas', tableMaxRows: 8, tableMaxCols: 6 });
const errors = await workbook.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!', options: { useRegex: true, maxResults: 50 }, summary: 'formula error scan' });
console.log(inspection.ndjson);
console.log(errors.ndjson);
for (const [sheetName, range, png] of [['Forderungskonto', 'A1:H27', 'forderungskonto.png'], ['Zahlungsbelege', 'A1:F23', 'zahlungsbelege.png']]) {
  const preview = await workbook.render({ sheetName, range, scale: 1.5, format: 'png' });
  await fs.writeFile(path.join(qaDir, png), new Uint8Array(await preview.arrayBuffer()));
}
const exported = path.join(qaDir, filename);
await (await SpreadsheetFile.exportXlsx(workbook)).save(exported);

// Change a disposable OOXML input and remove formula caches so native calculation is mandatory.
const inputDir = path.join(qaDir, 'recalc-input');
const outputDir = path.join(qaDir, 'recalc-output');
await fs.mkdir(inputDir);
await fs.mkdir(outputDir);
const variant = path.join(inputDir, 'input-change.xlsx');
await run(python, ['-B', '-c', `
import sys,zipfile,xml.etree.ElementTree as E
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(sys.argv[1]) as src, zipfile.ZipFile(sys.argv[2], 'w', zipfile.ZIP_DEFLATED) as out:
    for item in src.infolist():
        data=src.read(item.filename)
        if item.filename=='xl/worksheets/sheet1.xml':
            root=E.fromstring(data)
            root.find('.//s:c[@r="D12"]/s:v',ns).text='699'
            for cell in root.findall('.//s:c',ns):
                if cell.find('s:f',ns) is not None:
                    value=cell.find('s:v',ns)
                    if value is not None:
                        cell.remove(value)
            data=E.tostring(root,encoding='utf-8',xml_declaration=True)
        out.writestr(item,data)
`, exported, variant]);
const native = await run(office, [
  `-env:UserInstallation=${pathToFileURL(path.join(qaDir, 'office-profile')).href}`,
  '--headless', '--convert-to', 'xlsx', '--outdir', outputDir, variant,
], { timeout: 120000, maxBuffer: 1024 * 1024 });
const { stdout: validation } = await run(python, ['-B', '-c', `
import sys,json,zipfile,xml.etree.ElementTree as E
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
results=[]
for filename,increment in [(sys.argv[1],0),(sys.argv[2],1)]:
    with zipfile.ZipFile(filename) as z:
        for name in z.namelist():
            if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
                r=E.fromstring(z.read(name))
                assert not r.findall('.//s:c[@t="e"]',ns),name
        root=E.fromstring(z.read('xl/worksheets/sheet1.xml'))
        values={}
        for cell,value in {'F12':698,'F13':703.50,'F14':714.30,'F15':797.84,'F16':99.84,'D17':797.84,'E17':698,'F17':99.84}.items():
            c=root.find('.//s:c[@r="'+cell+'"]',ns)
            assert c.find('s:f',ns) is not None,cell
            got=float(c.find('s:v',ns).text)
            delta=0 if cell=='E17' else increment
            assert abs(got-value-delta)<1e-7,(cell,got,value+delta)
            values[cell]=got
        assert root.find('.//s:c[@r="A12"]/s:v',ns).text
        results.append({'file':filename,'cached_values':values})
print(json.dumps(results,ensure_ascii=False))
`, exported, path.join(outputDir, 'input-change.xlsx')]);
await fs.writeFile(path.join(qaDir, 'verification.json'), JSON.stringify({
  sourcePdfs: pdfNames, nativeCommand: office,
  nativeOutput: native.stdout.trim(), recalculation: JSON.parse(validation),
}, null, 2));
if (!qaOnly) await fs.copyFile(exported, target, constants.COPYFILE_EXCL);
console.log(JSON.stringify({ mode: qaOnly ? 'qa-only' : 'created', workbook: qaOnly ? exported : target, qaDir, nativeRecalculation: 'passed' }));

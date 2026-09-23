#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { loadWorkbookRuntime } from './akten-workbook-runtime.mjs';

const { Workbook, SpreadsheetFile, requireRuntime } = await loadWorkbookRuntime(['jszip', 'xml-js']);
const JSZip = requireRuntime('jszip');
const xml = requireRuntime('xml-js');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out = path.join(root, 'testakten/wirtschaftsanwalt-gesellschafterkonflikt-handwerk-hannover');
const qa = process.env.HANNOVER_AKTEN_QA || await fs.mkdtemp(path.join(os.tmpdir(), 'wirtschaftsanwalt-hannover-qa-'));
await fs.mkdir(qa, { recursive: true });
const wb = Workbook.create();
const currency = '#,##0.00;(#,##0.00);"-"';
const day = s => (Date.parse(s + 'T00:00:00Z') - Date.UTC(1899, 11, 30)) / 86400000;
const cell = (s, address, value) => { s.getRange(address).values = [[value]]; };
const near = (got, want) => assert(Math.abs(got - want) < .00001, `${got} != ${want}`);
const formula = (s, address, value) => {
  s.getRange(address).formulas = [[value]];
  s.getRange(address).format.font.color = value.includes('!') ? '#276647' : '#16191c';
};

function sheet(name, widths, last, title, subtitle) {
  const s = wb.worksheets.add(name);
  s.showGridLines = false;
  s.getRange(`A1:F${last}`).format = { font: { name: 'Times New Roman', size: 11, color: '#202427' }, rowHeight: 16, verticalAlignment: 'center' };
  s.getRange('A1:F1').format.rowHeight = 8;
  widths.forEach((width, index) => { s.getRangeByIndexes(0, index, last, 1).format.columnWidthPx = width; });
  cell(s, 'A2', title);
  s.getRange('A2').format.font = { name: 'Times New Roman', size: 16, bold: true };
  s.getRange('A2:F2').format.rowHeight = 30;
  cell(s, 'A3', subtitle);
  s.getRange('A3:F3').format.borders = { bottom: { style: 'thin', color: '#80918c' } };
  return s;
}

function header(s, row, labels) {
  s.getRange(`A${row}:F${row}`).values = [labels];
  s.getRange(`A${row}:F${row}`).format = { fill: '#354e48', font: { name: 'Times New Roman', size: 11, color: '#ffffff', bold: true }, wrapText: true, rowHeight: 32, horizontalAlignment: 'center' };
}

const status = sheet('Zahlungsstand', [160, 140, 140, 140, 145, 180], 33,
  'NB Gebäudetechnik Zahlungsstand', 'Bettina Kruse · 23.09.2026, 13:00 Uhr · Beträge EUR · Planung bis 02.10.2026');
const inflow = sheet('Eingänge', [150, 205, 130, 115, 115, 260], 24,
  'Offene Kundenposten', 'Stand 23.09.2026 · offene Bruttobeträge · Zahlungstermine nur soweit eingetragen');
const outflow = sheet('Ausgänge', [150, 205, 130, 115, 115, 260], 24,
  'Offene Zahlungen', 'Stand 23.09.2026 · Kreditoren und Lohnkreis getrennt · Beträge EUR');

header(inflow, 5, ['Beleg', 'Kunde', 'Offen EUR', 'Fälligkeit', 'Eingang geplant', 'Quelle / Terminstand']);
inflow.getRange('A6:F10').values = [
  ['NB-260902', 'Hofgarten Gewerbehöfe', 20000, day('2026-09-16'), null, '19 CSV, Zeile 2; 24 EML: kein Zahlungstag'],
  ['NB-260910', 'Hartung Hausverwaltung', 8450, day('2026-09-24'), day('2026-09-25'), '19 CSV, Zeile 3; 23 Notiz: mündlich angekündigt'],
  ['NB-260914', 'Praxis Riedgarten', 9790, day('2026-09-28'), day('2026-09-29'), '19 CSV, Zeile 4; 23 Notiz: eigene Erwartung'],
  ['NB-260916', 'WEG Lenzstraße 14', 3570, day('2026-09-30'), null, '19 CSV, Zeile 5; Zahlungslauf offen'],
  ['NB-260921', 'Borkel Metallbau', 6545, day('2026-10-05'), null, '19 CSV, Zeile 6; Termin nicht erfragt'],
];
inflow.getRange('A6:F10').format.rowHeight = 38;
inflow.getRange('B6:B10').format.wrapText = true;
inflow.getRange('F6:F10').format.wrapText = true;
cell(inflow, 'A11', 'Offene Posten gesamt');
formula(inflow, 'C11', '=SUM(C6:C10)');
cell(inflow, 'A13', 'Terminierte Eingänge im Planzeitraum');
formula(inflow, 'C14', '=SUMIFS(C6:C10,E6:E10,">="&\'Zahlungsstand\'!$B$8,E6:E10,"<="&\'Zahlungsstand\'!$D$8)');
cell(inflow, 'A16', 'Ohne Eingang im Planzeitraum');
formula(inflow, 'C16', '=C11-C14');
cell(inflow, 'A18', 'Kein gebuchter Erlass oder Abschlag auf den Forderungswert.');
cell(inflow, 'A19', 'Der Einbehalt bleibt vollständig offen; ein Eingangstag ist nicht zugesagt.');
cell(inflow, 'A21', 'Die Schlussrate Hofgarten von 42.840,00 EUR ist noch nicht fakturiert.');
cell(inflow, 'A22', 'Sie ist weder in der OP-Summe noch als Eingang im Plan enthalten (09 Vertrag, 23 Notiz).');
inflow.getRange('C6:C16').setNumberFormat(currency);
inflow.getRange('D6:E10').setNumberFormat('yyyy-mm-dd');
inflow.getRange('C6:E10').format.font.color = '#2054a0';
inflow.getRange('E6:E10').format.fill = '#fff4d4';

header(outflow, 5, ['Beleg', 'Zahlung an / Art', 'Betrag EUR', 'Fälligkeit', 'Ausgang geplant', 'Quelle / Stand']);
outflow.getRange('A6:F16').values = [
  ['RH-268417', 'Rößler Haustechnik', 29274, day('2026-09-07'), day('2026-09-23'), '20 CSV, Z. 2; 23 Notiz: überfällig, noch unbezahlt'],
  ['EW-260909', 'Elektro Wende', 4879, day('2026-09-25'), day('2026-09-25'), '20 CSV, Z. 3; Werkstatt, nicht Hofgarten'],
  ['LF-09-884', 'Leine Fahrzeugleasing', 2153.9, day('2026-09-28'), day('2026-09-28'), '20 CSV, Z. 4; Lastschrift'],
  ['EN-260930', 'Energieversorgung Südstadt', 1128.4, day('2026-09-30'), day('2026-09-30'), '20 CSV, Z. 5; Lastschrift'],
  ['MI-2026-10', 'Hägenhof Gewerbemiete', 3450, day('2026-10-01'), day('2026-10-01'), '20 CSV, Z. 6; Dauerauftrag'],
  ['SK-26218', 'Küster und Lohse', 892.5, day('2026-10-02'), day('2026-10-02'), '20 CSV, Z. 7; Finanzbuchhaltung'],
  ['SV-2026-09', 'Sozialversicherung', 16950, day('2026-09-28'), day('2026-09-28'), '21 EML; vorläufig, Nachmeldung offen'],
  ['NET-2026-09', '15 Beschäftigte netto', 31800, day('2026-09-30'), day('2026-09-30'), '21 EML; Bankdatei bis 29.09., 14 Uhr'],
  ['GF-2026-09', '2 Geschäftsführer netto', 7400, day('2026-09-30'), day('2026-09-30'), '21 EML; keine Gehaltsänderung gebucht'],
  ['LG-Q3-2026', 'Bankzinsen und Gebühren', 480, day('2026-09-30'), day('2026-09-30'), '22 Anrufnotiz; mündliche Schätzung'],
  ['LST-2026-09', 'Lohnsteuer September', 8260, day('2026-10-12'), day('2026-10-12'), '21 EML; außerhalb des Planzeitraums'],
];
outflow.getRange('A6:F16').format.rowHeight = 27;
outflow.getRange('B6:B16').format.wrapText = true;
outflow.getRange('F6:F16').format.wrapText = true;
cell(outflow, 'A18', 'Kreditoren laut CSV'); formula(outflow, 'C18', '=SUM(C6:C11)');
cell(outflow, 'A19', 'Ausgänge bis 02.10.');
formula(outflow, 'C19', '=SUMIFS(C6:C16,E6:E16,">="&\'Zahlungsstand\'!$B$8,E6:E16,"<="&\'Zahlungsstand\'!$D$8)');
cell(outflow, 'A21', 'Ratenanfrage vom 23.09., 12:15 Uhr (26 EML) noch nicht angenommen.');
cell(outflow, 'A22', '350 EUR Aufstockungsgebühr nur bei Kreditabschluss; derzeit nicht eingeplant.');
cell(outflow, 'A23', 'USt-Zahlbetrag Oktober und Zusatzarbeiten Hofgarten noch unbekannt (21 EML / 23 Notiz).');
outflow.getRange('C6:C19').setNumberFormat(currency);
outflow.getRange('D6:E16').setNumberFormat('yyyy-mm-dd');
outflow.getRange('C6:E16').format.font.color = '#2054a0';
outflow.getRange('E6:E16').format.fill = '#fff4d4';

status.getRange('A5:B7').values = [['Bank gebucht', -14250.6], ['Kreditlinie gültig', 40000], ['Vormerkungen', 0]];
cell(status, 'C5', '18 Bankansicht vom 23.09., 08:10 Uhr');
cell(status, 'C6', '17 Bankbrief / 22 Anrufnotiz, bislang unverändert');
cell(status, 'C7', '18 Bankansicht; keine weiteren Konten laut 22 Anrufnotiz');
cell(status, 'A8', 'Stichtag'); cell(status, 'B8', day('2026-09-23'));
cell(status, 'C8', 'Planende'); cell(status, 'D8', day('2026-10-02'));
status.getRange('B8').setNumberFormat('yyyy-mm-dd'); status.getRange('D8').setNumberFormat('yyyy-mm-dd');
cell(status, 'A9', 'Verfügbar'); formula(status, 'B9', '=B5+B6-B7');
status.getRange('B5:B7').format.font.color = '#2054a0';
status.getRange('B5:B7').setNumberFormat(currency); status.getRange('B9').setNumberFormat(currency);
header(status, 11, ['Tag', 'Anfang Bank', 'Eingänge', 'Ausgänge', 'Bank rechnerisch', 'Mit gültiger Linie']);
const dates = ['2026-09-23','2026-09-24','2026-09-25','2026-09-26','2026-09-27','2026-09-28','2026-09-29','2026-09-30','2026-10-01','2026-10-02'];
dates.forEach((date, index) => {
  const r = 12 + index;
  cell(status, `A${r}`, day(date));
  formula(status, `B${r}`, r === 12 ? '=$B$5' : `=E${r-1}`);
  formula(status, `C${r}`, `=SUMIFS('Eingänge'!$C$6:$C$10,'Eingänge'!$E$6:$E$10,A${r})`);
  formula(status, `D${r}`, `=SUMIFS('Ausgänge'!$C$6:$C$16,'Ausgänge'!$E$6:$E$16,A${r})`);
  formula(status, `E${r}`, `=B${r}+C${r}-D${r}`);
  formula(status, `F${r}`, `=E${r}+$B$6-$B$7`);
});
status.getRange('A12:A21').setNumberFormat('yyyy-mm-dd');
status.getRange('B12:F24').setNumberFormat(currency);
status.getRange('C12:D21').setNumberFormat('#,##0.00;(#,##0.00);0.00');
cell(status, 'A23', 'Summe im Zeitraum'); formula(status, 'C23', '=SUM(C12:C21)'); formula(status, 'D23', '=SUM(D12:D21)');
cell(status, 'A24', 'Stand am Planende'); formula(status, 'E24', '=E21'); formula(status, 'F24', '=F21');
status.getRange('F12:F21').conditionalFormats.add('cellIs', { operator: 'lessThan', formula: 0, format: { fill: '#f9e6e4', font: { color: '#9d342c' } } });
cell(status, 'A26', 'Zusatzlinie 30.000 EUR: noch nicht freigeschaltet, ohne Ansatz (17 Bankbrief / 22 Anruf).');
cell(status, 'A27', 'Neue Bürgschaften und August-BWA fehlen; kein bestätigter Bereitstellungstag.');
cell(status, 'A29', 'Eingänge: 8.450 EUR mündlich angekündigt, 9.790 EUR eigene Erwartung; keine Gutschriften.');
cell(status, 'A30', 'Negative Werte zeigen den rechnerischen Stand bei den eingetragenen Zahlungstagen.');
cell(status, 'A31', 'Sie sind keine ausgeführten Überweisungen. Nicht terminierte Einnahmen bleiben daneben offen.');
cell(status, 'A32', 'Stand und Termine stammen aus den bezeichneten Belegen; offene Oktoberbeträge fehlen noch.');
for (const [s, ranges] of [[status, ['A9:B9','A23:F24']], [inflow,['A11:F11','A16:F16']], [outflow,['A18:F19']]]) {
  for (const range of ranges) {
    s.getRange(range).format.fill = '#e6eeeb';
    s.getRange(range).format.font.bold = true;
    s.getRange(range).format.borders = { top: { style: 'thin', color: '#869790' } };
  }
}

wb.recalculate();
near(inflow.getRange('C11').values[0][0], 48355);
near(outflow.getRange('C18').values[0][0], 41777.8);
near(status.getRange('B9').values[0][0], 25749.4);
near(status.getRange('C23').values[0][0], 18240);
near(status.getRange('D23').values[0][0], 98407.8);
near(status.getRange('E21').values[0][0], -94418.4);
near(status.getRange('F21').values[0][0], -54418.4);
for (const row of [15, 16]) {
  near(status.getRange(`C${row}`).values[0][0], 0);
  near(status.getRange(`D${row}`).values[0][0], 0);
  near(status.getRange(`E${row}`).values[0][0], status.getRange(`B${row}`).values[0][0]);
}

// Prüfe Terminverschiebung, leeren Termin und echte Null ohne die Quellen zu ändern.
const checks = [];
for (const [date, row] of [['2026-09-26', 15], ['2026-09-27', 16]]) {
  cell(inflow, 'E7', day(date)); wb.recalculate();
  near(status.getRange(`C${row}`).values[0][0], 8450);
  near(status.getRange('C14').values[0][0], 0);
  near(status.getRange('C23').values[0][0], inflow.getRange('C14').values[0][0]);
  near(status.getRange('F21').values[0][0], -54418.4);
  checks.push(`Hartung am ${date}: Tag und Eingangssumme stimmen überein`);
}
cell(inflow, 'E7', day('2026-10-05')); wb.recalculate();
near(status.getRange('F21').values[0][0], -62868.4); checks.push('Hartung nach Planende: -62868,40');
cell(inflow, 'E7', null); wb.recalculate();
near(status.getRange('F21').values[0][0], -62868.4); checks.push('Leerer Eingangstermin bleibt außerhalb der Rechnung');
cell(inflow, 'E7', day('2026-09-25')); cell(inflow, 'C7', 0); wb.recalculate();
near(status.getRange('F21').values[0][0], -62868.4); checks.push('Nullbetrag bleibt Null');
cell(inflow, 'C7', 8450); cell(outflow, 'C15', 500); wb.recalculate();
near(status.getRange('F21').values[0][0], -54438.4); checks.push('Spätere Bankkosten wirken auf den Endstand');
cell(outflow, 'C15', 480); wb.recalculate();
near(status.getRange('F21').values[0][0], -54418.4);

const ranges = [['Zahlungsstand','A1:F33'],['Eingänge','A1:F24'],['Ausgänge','A1:F24']];
const errors = await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!', options: { useRegex: true, maxResults: 50 }, maxChars: 2000 });
assert(!/"(?:value|text)":"#/.test(errors.ndjson), errors.ndjson);
const inspections = [];
for (const [name, range] of ranges) {
  inspections.push((await wb.inspect({ kind: 'table', range: `${name}!${range}`, include: 'values,formulas', tableMaxRows: 33, tableMaxCols: 6, maxChars: 15000 })).ndjson);
  const preview = await wb.render({ sheetName: name, range, scale: 1.5, format: 'png' });
  await fs.writeFile(path.join(qa, `xlsx-${name}.png`), new Uint8Array(await preview.arrayBuffer()));
}
await fs.writeFile(path.join(qa, 'workbook-inspect.ndjson'), inspections.join('\n'));
await fs.writeFile(path.join(qa, 'workbook-checks.json'), JSON.stringify({ inputChecks: checks, restoredEnd: status.getRange('F21').values[0][0], formulaErrors: errors.ndjson }, null, 2));

const exported = await SpreadsheetFile.exportXlsx(wb);
const staged = path.join(qa, 'workbook-export.xlsx');
await exported.save(staged);
// Druckbereiche ergänzen wie in den vorhandenen Akten-Buildern; Rechenwerte bleiben erhalten.
const zip = await JSZip.loadAsync(await fs.readFile(staged));
const local = e => e.name?.split(':').at(-1);
const element = (name, attributes, elements = []) => ({ type: 'element', name, attributes, elements });
const bookXml = xml.xml2js(await zip.file('xl/workbook.xml').async('string'), { compact: false });
const book = bookXml.elements.find(e => local(e) === 'workbook');
const prefix = book.name.includes(':') ? book.name.split(':')[0] + ':' : '';
book.elements = book.elements.filter(e => local(e) !== 'definedNames');
const names = element(prefix + 'definedNames', {}, ranges.map(([name, range], index) =>
  element(prefix + 'definedName', { name: '_xlnm.Print_Area', localSheetId: String(index) }, [{ type: 'text', text: `'${name}'!${range.replace(/([A-Z]+)([0-9]+)/g, '$$$1$$$2')}` }])));
const calcIndex = book.elements.findIndex(e => local(e) === 'calcPr');
book.elements.splice(calcIndex < 0 ? book.elements.length : calcIndex, 0, names);
const calculation = book.elements.find(e => local(e) === 'calcPr');
const calculationAttributes = { calcMode: 'auto', fullCalcOnLoad: '1', forceFullCalc: '1' };
if (calculation) Object.assign(calculation.attributes, calculationAttributes);
else book.elements.push(element(prefix + 'calcPr', calculationAttributes));
zip.file('xl/workbook.xml', xml.js2xml(bookXml, { compact: false }));
for (let index = 1; index <= ranges.length; index++) {
  const filename = `xl/worksheets/sheet${index}.xml`;
  const model = xml.xml2js(await zip.file(filename).async('string'), { compact: false });
  const worksheet = model.elements.find(e => local(e) === 'worksheet');
  const p = worksheet.name.includes(':') ? worksheet.name.split(':')[0] + ':' : '';
  worksheet.elements = worksheet.elements.filter(e => !['pageMargins','pageSetup'].includes(local(e)));
  worksheet.elements.push(element(p + 'pageMargins', { left: '.25', right: '.25', top: '.35', bottom: '.35', header: '.15', footer: '.15' }));
  worksheet.elements.push(element(p + 'pageSetup', { paperSize: '9', orientation: 'landscape', fitToWidth: '1', fitToHeight: '1' }));
  zip.file(filename, xml.js2xml(model, { compact: false }));
}
const output = path.join(out, '25_Liquiditaetsstatus_2026-09-23.xlsx');
await fs.writeFile(output, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
await fs.rm(output + '.inspect.ndjson', { force: true });
console.log('Arbeitsmappe: drei Blätter, Formeln geprüft, Termintests bestanden, Rechenstand wiederhergestellt.');

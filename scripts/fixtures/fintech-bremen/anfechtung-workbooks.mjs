import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const data = JSON.parse(await fs.readFile(process.argv[2], 'utf8'));
const out = process.argv[3];
const qa = process.argv[4];
await fs.mkdir(out, { recursive: true });
await fs.mkdir(qa, { recursive: true });
// Native numeric Excel date values avoid string dates in the renderer/export.
const date = s => (Date.parse(`${s}T00:00:00Z`) - Date.UTC(1899, 11, 30)) / 86400000;
const cell = (s, a, v) => { s.getRange(a).values = [[v]]; };
const formula = (s, a, v) => { s.getRange(a).formulas = [[v]]; };
const euro = '[$-407]#,##0.00_);[Red](#,##0.00);0.00_)';
const letter = n => String.fromCharCode(65 + n);
const lastColumns = new Map();
function setup(s, title, widths, end) {
  s.showGridLines = false;
  lastColumns.set(s.name, letter(widths.length - 1));
  s.getRange(`A1:${letter(widths.length - 1)}${end}`).format.font = { name: 'Times New Roman', size: 11, color: '#202020' };
  s.getRange(`A1:${letter(widths.length - 1)}${end}`).format.rowHeight = 17;
  s.getRange(`A1:${letter(widths.length - 1)}${end}`).format.verticalAlignment = 'center';
  widths.forEach((w, i) => { s.getRange(`${letter(i)}1:${letter(i)}${end}`).format.columnWidthPx = w; });
  cell(s, 'A2', title);
  s.getRange('A2').format.font = { name: 'Times New Roman', size: 15, bold: true };
  s.getRange('A2').format.rowHeight = 30;
}
function header(s, row, labels) {
  const r = s.getRange(`A${row}:${letter(labels.length - 1)}${row}`);
  r.values = [labels];
  r.format = { fill: '#293A4A', font: { name: 'Times New Roman', size: 11, color: '#FFFFFF', bold: true }, wrapText: true, rowHeight: 28 };
}
function note(s, row, text) {
  const range = s.getRange(`A${row}:${lastColumns.get(s.name)}${row}`);
  range.merge();
  range.format.wrapText = true;
  cell(s, `A${row}`, text);
  s.getRange(`A${row}`).format.font.italic = true;
}
function assertValue(s, a, n) {
  const v = s.getRange(a).values[0][0];
  if (v !== n) throw new Error(`${s.name}!${a}: ${JSON.stringify(v)} != ${JSON.stringify(n)}`);
}
async function save(wb, filename, ranges) {
  wb.recalculate();
  const errors = await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!', options: { useRegex: true, maxResults: 20 }, maxChars: 2000 });
  await fs.writeFile(path.join(qa, `${filename}.checks.txt`), errors.ndjson);
  for (const [sheetName, range] of ranges) {
    const inspection = await wb.inspect({ kind: 'table', range: `${sheetName}!${range}`, include: 'values,formulas', tableMaxRows: 45, tableMaxCols: 8, maxChars: 24000 });
    await fs.writeFile(path.join(qa, `${filename}-${sheetName}.txt`), inspection.ndjson);
    const blob = await wb.render({ sheetName, range, scale: 1.5, format: 'png' });
    await fs.writeFile(path.join(qa, `${filename}-${sheetName}.png`), new Uint8Array(await blob.arrayBuffer()));
  }
  await (await SpreadsheetFile.exportXlsx(wb)).save(path.join(out, filename));
  try { await fs.rename(path.join(out, `${filename}.inspect.ndjson`), path.join(qa, `${filename}.inspect.ndjson`)); }
  catch (error) { if (error.code !== 'ENOENT') throw error; }
}

const wb = Workbook.create();
const st = wb.worksheets.add('Stichtage');
const be = wb.worksheets.add('Belege');
setup(st, 'Stichtage und fehlende Verpflichtungen', [395, 160, 160, 310], 25);
note(st, 3, 'Jutta Kröger | Zusammenstellung 24.09.2026 | EUR | Ausgewählte Belege, kein vollständiger Liquiditätsstatus');
header(st, 5, ['Position', '15.04.2024', '02.05.2024', 'Bedeutung']);
const rows = [
 ['Bankguthaben', null, null, 'April nach Schlusszahlung'],
 ['Zwölf Lieferantenrechnungen', null, null, 'Auswahl laut K7; unverändert offen'],
 ['Neue Erstattung N42', null, null, 'Erst am 2. Mai vereinbart'],
 ['Erfasste Verpflichtungen', null, null, 'Summe der beiden vorigen Zeilen'],
 ['Differenz aus ausgewählten Belegen', null, null, 'Keine abschließende Zahlungsfähigkeitsprüfung'],
 ['Zusätzliche fällige Verpflichtungen', null, null, 'Eingabe offen; nicht durch null ersetzen'],
 ['Stand nach zusätzlicher Eingabe', null, null, 'Berechnung erst nach belegter Ergänzung'],
 ['Vollständigkeit der Eingaben', null, null, 'Lohn-, Steuer- und Vertragslisten fehlen']
];
st.getRange('A6:D13').values = rows;
st.getRange('A6:D13').format.wrapText = true;
st.getRange('A6:D13').format.rowHeight = 24;
formula(st, 'B6', '=Belege!B22'); formula(st, 'C6', '=Belege!B23');
for (const c of ['B','C']) formula(st, `${c}7`, '=SUM(Belege!D6:D17)');
formula(st, 'B8', '=Belege!B24'); formula(st, 'C8', '=Belege!B25');
for (const c of ['B','C']) {
 formula(st, `${c}9`, `=SUM(${c}7:${c}8)`);
 formula(st, `${c}10`, `=${c}6-${c}9`);
 formula(st, `${c}12`, `=IF(ISNUMBER(${c}11),${c}10-${c}11,"offen")`);
 formula(st, `${c}13`, `=IF(ISNUMBER(${c}11),"Eingabe ergänzt; Belegumfang prüfen","Belege fehlen")`);
}
st.getRange('B6:C12').setNumberFormat(euro);
st.getRange('B11:C11').format.fill = '#FFF2CC';
st.getRange('B11:C11').format.font.color = '#174A9B';
st.getRange('B10:C10').conditionalFormats.add('cellIs', { operator: 'lessThan', formula: 0, format: { fill: '#FCE8E6', font: { color: '#9B2424' } } });
note(st, 16, 'Gelb: ergänzbare Eingabe. Erst eintragen, wenn Betrag und Stichtag belegt sind. Null ist eine Aussage.');
note(st, 18, 'Die April-Differenz betrifft nur die ausgewählten zwölf Rechnungen. Guthaben ist kein Vollständigkeitsnachweis.');
note(st, 20, 'Die Erstattung von 598.600 EUR entstand am 02.05.2024. Nicht in frühere Stichtage zurückrechnen.');
note(st, 22, 'Die April-Schlusszahlung ist bereits im Bankguthaben enthalten. Sie wird hier nicht nochmals abgezogen.');
note(st, 24, 'Quellen und Originalbeträge stehen im Blatt Belege. Frühere Excel-Dateien bleiben unverändert erhalten.');

setup(be, 'Belege für die Stichtagsgegenüberstellung', [235, 280, 120, 140, 245], 28);
note(be, 3, 'Quelle: K7 Blätter 2 und 3; K4 Blatt 18; K7 Blatt 6; Ergänzungen 51, 54 und 55.');
header(be, 5, ['Gläubiger', 'Rechnung', 'Fälligkeit', 'Offen EUR', 'Quelle']);
be.getRange('A6:E17').values = data.creditors.map(r => [r.name, r.invoice, date(r.due), r.amount, r.source]);
be.getRange('C6:C17').setNumberFormat('dd.mm.yyyy');
be.getRange('D6:D17').setNumberFormat(euro);
be.getRange('A6:E17').format.wrapText = true;
be.getRange('A6:E17').format.rowHeight = 17;
be.getRange('D6:D17').format.font.color = '#17613C';
header(be, 20, ['Weitere Ausgangsdaten', 'EUR', 'Stichtag', 'Beleg', 'Einordnung']);
be.getRange('A22:E25').values = [
 ['Bank nach Schlusszahlung', 520900, date('2024-04-15'), 'K4 Blatt 18 / 51', 'Tatsächlicher Saldo'],
 ['Bank vor neuer Erstattung', 383000, date('2024-05-02'), 'K7 Blatt 6', 'Kein neuer Eingang mitgeteilt'],
 ['Erstattung am Aprilstichtag', 0, date('2024-04-15'), 'K7 Blatt 6 / 54', 'Noch nicht vereinbart'],
 ['Erstattung am Maistichtag', 598600, date('2024-05-02'), 'K7 Blatt 6 / 54', 'Neue Forderung; noch unbezahlt']
];
be.getRange('A22:E25').format.wrapText = true;
be.getRange('A22:E25').format.rowHeight = 20;
be.getRange('B22:B25').setNumberFormat(euro); be.getRange('C22:C25').setNumberFormat('dd.mm.yyyy');
note(be, 27, 'Fortbestand der zwölf ausgewählten Posten am 02.05.: Erinnerung mit Kontenabgleich Kröger, Dokument 55.');
be.getRange('C6:C25').format.horizontalAlignment = 'center';
be.freezePanes.freezeRows(5);
wb.recalculate();
assertValue(st, 'B7', 478380); assertValue(st, 'B10', 42520); assertValue(st, 'C10', -693980);
assertValue(st, 'B12', 'offen');
cell(st, 'B11', 10000); wb.recalculate(); assertValue(st, 'B12', 32520);
cell(st, 'B11', 0); wb.recalculate(); assertValue(st, 'B12', 42520);
st.getRange('B11').clear({ applyTo: 'contents' }); wb.recalculate(); assertValue(st, 'B12', 'offen');
await save(wb, '59_Stichtage_und_Belegluecken_20260924.xlsx', [['Stichtage','A1:D25'],['Belege','A1:E28']]);

const pw = Workbook.create();
const ab = pw.worksheets.add('Abgleich');
const bv = pw.worksheets.add('Bewegungen');
setup(ab, 'Ausführungen und bloße Vorschläge', [440,170,420], 24);
note(ab, 3, 'Zusammenstellung 24.09.2026 | Beträge in EUR | Kein Urteil über die Rückgewährpflicht');
header(ab, 5, ['Vorgang', 'Betrag EUR', 'Abgrenzung']);
ab.getRange('A6:C12').values = [
 ['Schuldnerzahlungen an Vellio',null,'18 Zinsraten und Endtilgung'],
 ['Davon Zahlungen ab 02.02.2024',null,'Teilbetrag der Zeile darüber'],
 ['Davon Schlusszahlungen 15.04.2024',null,'5.000 Zins und 500.000 Kapital'],
 ['Erwerbspreis Vellio an Nexora',null,'Eigener Vorgang am 14.10.2022'],
 ['Angefragte Direktzahlung an Nordkai',null,'Nicht ausgeführt; kein Zahlungseingang'],
 ['Bankauszahlung an Weserfunken',null,'Zufluss; keine Rückzahlung'],
 ['Ausgeführte Schuldnerzahlungen gezählt',null,'19 Einzelaufträge']
];
formula(ab,'B6','=SUMIFS(Bewegungen!$E$6:$E$27,Bewegungen!$D$6:$D$27,"Schuldnerzahlung",Bewegungen!$F$6:$F$27,"ausgeführt")');
formula(ab,'B7','=SUMIFS(Bewegungen!$E$6:$E$27,Bewegungen!$D$6:$D$27,"Schuldnerzahlung",Bewegungen!$F$6:$F$27,"ausgeführt",Bewegungen!$B$6:$B$27,">="&DATE(2024,2,2))');
formula(ab,'B8','=SUMIFS(Bewegungen!$E$6:$E$27,Bewegungen!$D$6:$D$27,"Schuldnerzahlung",Bewegungen!$B$6:$B$27,DATE(2024,4,15))');
formula(ab,'B9','=SUMIFS(Bewegungen!$E$6:$E$27,Bewegungen!$D$6:$D$27,"Erwerbspreis")');
formula(ab,'B10','=SUMIFS(Bewegungen!$E$6:$E$27,Bewegungen!$D$6:$D$27,"Vorschlag")');
formula(ab,'B11','=SUMIFS(Bewegungen!$E$6:$E$27,Bewegungen!$D$6:$D$27,"Auszahlung")');
formula(ab,'B12','=COUNTIFS(Bewegungen!$D$6:$D$27,"Schuldnerzahlung",Bewegungen!$F$6:$F$27,"ausgeführt")');
ab.getRange('A6:C12').format.wrapText = true; ab.getRange('A6:C12').format.rowHeight = 24;
ab.getRange('B6:B11').setNumberFormat(euro);
ab.getRange('B12').setNumberFormat('0"  "');
note(ab,15,'Keine Addition der Teilsummen. Erwerbspreis, Auszahlung und Vorschlag sind keine Schuldnerzahlungen.');
note(ab,17,'Die rechtliche Zeitraumberechnung ist gesondert zu prüfen. 02.02.2024 dient hier nur dem Belegabgleich.');
note(ab,19,'Der Vertragswechsel um 12:30 Uhr ist eine Vereinbarung, keine zusätzliche Geldbewegung.');
note(ab,21,'Ein wahrer Empfängername beweist noch nicht die rechtliche Anspruchsgegnerstellung.');
note(ab,23,'Erinnerungen und Kenntnisstände: Dokumente 55 bis 57. Diese Mappe trifft keine Beweiswürdigung.');
setup(bv,'Zahlungsdaten mit Beleg und Status',[78,115,260,150,130,140,230],28);
note(bv,3,'Quellen: K3, K4, B3, B4; Vorschlag in 62 und Absage in 63. Beträge sind positiv dargestellt.');
header(bv,5,['ID','Datum','Sender an Empfänger','Art','Betrag EUR','Status','Beleg']);
bv.getRange('A6:G27').values = data.movements.map(r => [r.id,date(r.date),r.parties,r.type,r.amount,r.status,r.source]);
bv.getRange('B6:B27').setNumberFormat('dd.mm.yyyy'); bv.getRange('E6:E27').setNumberFormat(euro);
bv.getRange('A6:G27').format.wrapText = true; bv.getRange('A6:G27').format.rowHeight = 17;
bv.getRange('E6:E27').format.font.color = '#17613C';
bv.getRange('B6:B27').format.horizontalAlignment = 'center';
bv.freezePanes.freezeRows(5);
pw.recalculate();
assertValue(ab,'B6',590000); assertValue(ab,'B7',515000); assertValue(ab,'B8',505000); assertValue(ab,'B9',500000); assertValue(ab,'B10',42840); assertValue(ab,'B12',19);
const original = bv.getRange('E6').values[0][0];
cell(bv,'E6',original+100); pw.recalculate(); assertValue(ab,'B6',590100);
cell(bv,'E6',original); pw.recalculate(); assertValue(ab,'B6',590000);
await save(pw,'60_Zahlungswege_und_Vorschlaege_20260924.xlsx',[['Abgleich','A1:C24'],['Bewegungen','A1:G28']]);
console.log('Zwei Arbeitsmappen erstellt; Betragssummen, Änderung, Rücksetzung und Leerwert gegenüber Null geprüft.');

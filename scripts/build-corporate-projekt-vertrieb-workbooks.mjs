#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import assert from 'node:assert/strict';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import { execFileSync } from 'node:child_process';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const p = path.join(root, 'testakten/corporate-contract-law-projektvertrag-automation-augsburg');
const v = path.join(root, 'testakten/corporate-contract-law-vertrieb-messtechnik-bremen');
const qa = process.env.CORPORATE_AKTEN_QA || await fs.mkdtemp(path.join(os.tmpdir(), 'corporate-projekt-vertrieb-'));
await fs.mkdir(qa, { recursive: true });
const deps = path.resolve(path.dirname(process.execPath), '../..');
const moduleLink = path.join(qa, 'node_modules');
try { await fs.lstat(moduleLink); } catch { await fs.symlink(path.join(deps, 'node/node_modules'), moduleLink, 'dir'); }
const requireRuntime = createRequire(path.join(qa, 'runtime.cjs'));
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(requireRuntime.resolve('@oai/artifact-tool')).href);
const JSZip = requireRuntime('jszip');
const xmlParser = requireRuntime('xml-js');
const money = '#,##0.00;(#,##0.00);"-"';
const dateFormat = 'yyyy-mm-dd';
const col = n => String.fromCharCode(65 + n);
const serial = s => (Date.parse(`${s}T00:00:00Z`) - Date.UTC(1899, 11, 30)) / 86400000;
const val = (s, address, value) => { s.getRange(address).values = [[value]]; };
const formula = (s, address, value) => { s.getRange(address).formulas = [[value]]; s.getRange(address).format.font.color = value.includes('!') ? '#286047' : '#000000'; };
const near = (a, b) => assert(Math.abs(a-b) < 1e-7, `${a} != ${b}`);

function sheet(wb, name, widths, last, title, meta) {
  const s = wb.worksheets.add(name);
  s.showGridLines = false;
  const end = col(widths.length-1);
  s.getRange(`A1:${end}${last}`).format = { font: { name: 'Times New Roman', size: 11, color: '#16191c' }, rowHeight: 24, verticalAlignment: 'center' };
  widths.forEach((w, i) => { s.getRange(`${col(i)}1:${col(i)}${last}`).format.columnWidthPx = w; });
  s.getRange(`A1:${end}1`).format.rowHeight = 8;
  val(s, 'A2', title);
  s.getRange('A2').format.font = { name: 'Times New Roman', size: 16, bold: true };
  s.getRange(`A2:${end}2`).format.rowHeight = 31;
  val(s, 'A3', meta);
  s.getRange(`A3:${end}3`).format.borders = { bottom: { style: 'thin', color: '#9ea7aa' } };
  return s;
}

function header(s, row, labels) {
  const range = s.getRange(`A${row}:${col(labels.length-1)}${row}`);
  range.values = [labels];
  range.format = { fill: '#384b50', font: { name: 'Times New Roman', size: 11, color: '#ffffff', bold: true }, rowHeight: 34, wrapText: true, horizontalAlignment: 'center' };
}

function total(s, range) {
  s.getRange(range).format.fill = '#e6eeeb';
  s.getRange(range).format.font.bold = true;
  s.getRange(range).format.borders = { top: { style: 'thin', color: '#748781' } };
}

function input(s, range, format) {
  s.getRange(range).format.font.color = '#164ea2';
  if (format) s.getRange(range).setNumberFormat(format);
}

async function exportBook(wb, out, ranges, expected) {
  wb.recalculate();
  for (const [sn, address, amount] of expected) near(wb.worksheets.getItem(sn).getRange(address).values[0][0], amount);
  const errorScan = await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!', options: { useRegex: true, maxResults: 100 }, maxChars: 2000 });
  assert(!/"(?:value|text)":"#/.test(errorScan.ndjson), errorScan.ndjson);
  console.log(errorScan.ndjson);
  for (const [name, range] of ranges) {
    const report = await wb.inspect({ kind: 'table', range: `${name}!${range}`, include: 'values,formulas', tableMaxRows: 6, tableMaxCols: 8, maxChars: 2000 });
    console.log(report.ndjson);
    const png = await wb.render({ sheetName: name, range, scale: 1.5, format: 'png' });
    await fs.writeFile(path.join(qa, `${path.basename(out, '.xlsx')}-${name}.png`), new Uint8Array(await png.arrayBuffer()));
  }
  const exported = await SpreadsheetFile.exportXlsx(wb);
  const staged = path.join(qa, path.basename(out));
  await exported.save(staged);
  // Bounded print areas keep the independent office renderer on each populated sheet.
  const zip = await JSZip.loadAsync(await fs.readFile(staged));
  const model = xmlParser.xml2js(await zip.file('xl/workbook.xml').async('string'), { compact: false });
  const local = e => e.name?.split(':').at(-1);
  const root = model.elements.find(e => local(e) === 'workbook');
  const prefix = root.name.includes(':') ? root.name.split(':')[0] + ':' : '';
  root.elements = root.elements.filter(e => local(e) !== 'definedNames');
  const names = { type:'element', name:prefix+'definedNames', elements: ranges.map(([name, range], i) => ({ type:'element', name:prefix+'definedName', attributes:{ name:'_xlnm.Print_Area', localSheetId:String(i) }, elements:[{ type:'text', text:`'${name}'!${range.replace(/([A-Z]+)([0-9]+)/g, '$$$1$$$2')}` }] })) };
  const calcIndex = root.elements.findIndex(e => local(e) === 'calcPr');
  root.elements.splice(calcIndex < 0 ? root.elements.length : calcIndex, 0, names);
  zip.file('xl/workbook.xml', xmlParser.js2xml(model, { compact: false }));
  for (let i = 1; i <= ranges.length; i++) {
    const name = `xl/worksheets/sheet${i}.xml`;
    const model = xmlParser.xml2js(await zip.file(name).async('string'), { compact:false });
    const worksheet = model.elements.find(e => local(e) === 'worksheet');
    const prefix = worksheet.name.includes(':') ? worksheet.name.split(':')[0] + ':' : '';
    const sheetData = worksheet.elements.find(e => local(e) === 'sheetData');
    for (const row of sheetData.elements ?? []) {
      for (const cell of row.elements ?? []) {
        if (local(cell) !== 'c' || cell.attributes?.t !== 'str') continue;
        const formulaIndex = cell.elements?.findIndex(e => local(e) === 'f') ?? -1;
        if (formulaIndex < 0 || cell.elements.some(e => local(e) === 'v')) continue;
        const cached = wb.worksheets.getItem(ranges[i-1][0]).getRange(cell.attributes.r).values[0][0];
        assert.equal(cached, '', `Missing nonempty string cache: ${ranges[i-1][0]}!${cell.attributes.r}`);
        // The exporter omits the value element for calculated empty strings.
        cell.elements.splice(formulaIndex + 1, 0, { type:'element', name:prefix+'v' });
      }
    }
    worksheet.elements = worksheet.elements.filter(e => !['pageMargins','pageSetup'].includes(local(e)));
    worksheet.elements.push({ type:'element', name:prefix+'pageMargins', attributes:{ left:'0.25', right:'0.25', top:'0.35', bottom:'0.35', header:'0.15', footer:'0.15' } });
    worksheet.elements.push({ type:'element', name:prefix+'pageSetup', attributes:{ paperSize:'8', orientation:'landscape', fitToWidth:'1', fitToHeight:'1' } });
    zip.file(name, xmlParser.js2xml(model, { compact:false }));
  }
  await fs.writeFile(out, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
  await fs.rm(`${out}.inspect.ndjson`, { force: true });
  console.log(`Gespeichert: ${out}`);
}

async function projectBook() {
  const wb = Workbook.create();
  const s = sheet(wb, 'Zahlungen', [235, 105, 140, 140, 140, 135, 360], 35, 'Linie 3 Meilensteinzahlungen', 'Miriam Seidel, Wertau | Stand 22.09.2026 | Hauptauftrag und Zahlungsfolge noch nicht vereinbart');
  const t = sheet(wb, 'Zeitplan', [240, 140, 140, 120, 190, 490], 18, 'Linie 3 Zeitplan', 'Paula König / Timo Brandt | Planungsstand 22.09.2026 | Ausführung 2027');
  s.getRange('A5:B9').values = [['Hauptpreis netto EUR', 675000], ['Umsatzsteuer', .19], ['Vorplanung bezahlt netto EUR', 9500], ['Vorplanung Steuer EUR', null], ['Vorplanung bezahlt brutto EUR', null]];
  input(s, 'B5', money); input(s, 'B6', '0%'); input(s, 'B7', money);
  formula(s, 'B8', '=ROUND(B7*B6,2)'); formula(s, 'B9', '=B7+B8');
  s.getRange('B8:B9').setNumberFormat(money);
  val(s, 'D5', 'Quellen: HP-2618 Rev. 2 und LOI WA-26-08.');
  val(s, 'D7', 'Vorplanung überwiesen am 12.08.2026.');
  val(s, 'D9', 'Keine Rechnung und keine Zahlung zum Hauptauftrag.');
  header(s, 12, ['Stufe nach Helix-Entwurf', 'Anteil', 'Netto EUR', 'Steuer EUR', 'Brutto EUR', 'Plantermin', 'Auslöser im Entwurf']);
  const rows = [
    ['1 Vertrag', .2, null, null, null, serial('2026-09-30'), 'Unterzeichnung, noch ausstehend'],
    ['2 Versandbereitschaft', .4, null, null, null, serial('2027-06-14'), 'Meldung nach Werkprüfung'],
    ['3 Montage', .3, null, null, null, serial('2027-07-28'), 'Mechanisch und elektrisch fertig'],
    ['4 Abnahme', .1, null, null, null, serial('2027-07-30'), 'Abnahme; Verfahren noch offen'],
  ];
  s.getRange('A13:G16').values = rows;
  for (let r=13; r<=16; r++) {
    formula(s, `C${r}`, `=ROUND($B$5*B${r},2)`);
    formula(s, `D${r}`, `=ROUND(C${r}*$B$6,2)`);
    formula(s, `E${r}`, `=C${r}+D${r}`);
  }
  input(s, 'B13:B16', '0%'); input(s, 'F13:F16', dateFormat);
  s.getRange('C13:E17').setNumberFormat(money);
  val(s, 'A17', 'Summe Hauptpreis');
  for (const c of ['B','C','D','E']) formula(s, `${c}17`, `=SUM(${c}13:${c}16)`);
  s.getRange('B17').setNumberFormat('0%'); total(s, 'A17:G17');
  val(s, 'A20', 'Unterschiedliche Behandlung der Vorplanung, keine Verrechnung freigegeben');
  header(s, 22, ['Berechnungsstand', 'Bezug', 'Netto EUR', 'Steuer EUR', 'Brutto EUR', 'Stand', 'Position der Beteiligten']);
  s.getRange('A23:B26').values = [['Wertau: erste Rate', 'mit Abzug'], ['Wertau: Gesamtaufwand', 'inkl. LOI'], ['Helix: erste Rate', 'ohne Abzug'], ['Helix: Gesamtaufwand', 'inkl. LOI']];
  formula(s, 'C23', '=C13-$B$7'); formula(s, 'C24', '=$B$5'); formula(s, 'C25', '=C13'); formula(s, 'C26', '=$B$5+$B$7');
  for (let r=23; r<=26; r++) { formula(s, `D${r}`, `=ROUND(C${r}*$B$6,2)`); formula(s, `E${r}`, `=C${r}+D${r}`); val(s, `F${r}`, 'nicht vereinbart'); }
  s.getRange('G23:G26').values = [['E-Mail Seidel 18.09.2026'], ['Budget einschließlich Vorplanung'], ['E-Mail Rehm 18.09.2026'], ['Vorplanung zusätzlich zum Hauptpreis']];
  s.getRange('C23:E26').setNumberFormat(money);
  val(s, 'A29', 'Option N01 netto EUR'); val(s, 'C29', 24000); input(s, 'C29', money);
  formula(s, 'D29', '=ROUND(C29*$B$6,2)'); formula(s, 'E29', '=C29+D29');
  s.getRange('D29:E29').setNumberFormat(money); val(s, 'G29', 'Nicht bestellt; außerhalb der Zahlungsstufen');
  val(s, 'A32', 'Wertau schlägt die 30-Prozent-Stufe erst nach erfolgreichem Leistungslauf vor.');
  val(s, 'A33', 'Die Plantermine begründen keine Fälligkeit. Helix schlägt 14 Kalendertage ab Rechnung vor.');
  val(s, 'A34', 'Der Nachtrag N01 wird nicht in Hauptpreis oder bereits bezahlte Vorplanung eingerechnet.');

  header(t, 5, ['Vorgang', 'Bisher geplant', 'Neu besprochen', 'Delta Tage', 'Verantwortlich', 'Voraussetzung oder Stand']);
  t.getRange('A6:F13').values = [
    ['Anschlussdaten', serial('2026-09-18'), null, null, 'Wertau', 'Nicht abschließend bestätigt'],
    ['Vertrag', serial('2026-09-30'), serial('2026-09-30'), null, 'Beide Parteien', 'Planannahme, noch keine Unterzeichnung'],
    ['E1 energisiert', serial('2027-06-11'), serial('2027-07-09'), null, 'Wertau', 'Frühester Termin, Prüfprotokoll fehlt'],
    ['Werkprüfung', serial('2027-06-14'), serial('2027-06-14'), null, 'Helix', 'Mit Simulator, nicht mit Bestandslinie'],
    ['Anlieferung', serial('2027-07-12'), serial('2027-07-12'), null, 'Helix / Wertau', 'Nordfläche erst ab 19.07. zugesagt'],
    ['Montagebeginn', serial('2027-07-19'), serial('2027-07-19'), null, 'Helix', 'Strom und Baufreiheit erforderlich'],
    ['Leistungslauf / Reserve', serial('2027-07-29'), serial('2027-07-30'), null, 'Beide Parteien', 'Zwei Läufe von Wertau verlangt; nicht terminiert'],
    ['Produktionsstart', serial('2027-08-02'), serial('2027-08-02'), null, 'Wertau', 'Gewünschter Start; keine Terminbestätigung'],
  ];
  for(let r=6; r<=13; r++) formula(t, `D${r}`, `=IF(C${r}="","",C${r}-B${r})`);
  input(t, 'B6:C13', dateFormat);
  t.getRange('A6:F13').format.rowHeight = 39;
  t.getRange('F6:F13').format.wrapText = true;
  t.getRange('D6:D13').setNumberFormat('0');
  val(t, 'A16', 'Quelle: TP-2618 Rev. 1, E-Mails 10.09. und 14.09., Chat vom 16.09.2026.');
  val(t, 'A17', 'Optivis: 26. bis 28.07. reserviert; nächster genannter Termin ab 16.08.2027.');
  s.freezePanes.freezeRows(12);
  t.freezePanes.freezeRows(5);
  const before = s.getRange('E17').values[0][0];
  val(s, 'B5', 700000); wb.recalculate(); near(s.getRange('E17').values[0][0], 833000);
  val(s, 'B5', 675000); wb.recalculate(); near(s.getRange('E17').values[0][0], before);
  await exportBook(wb, path.join(p, '17_Meilensteinzahlungen_und_Termine.xlsx'), [['Zahlungen','A1:G35'], ['Zeitplan','A1:F18']], [['Zahlungen','C17',675000],['Zahlungen','E17',803250],['Zahlungen','E23',149345],['Zahlungen','E26',814555],['Zeitplan','D8',28]]);
}

async function distributionBook() {
  const wb = Workbook.create();
  const s = sheet(wb, 'Kalkulation', [255, 95, 145, 145, 150, 155, 150, 135], 35, 'Luminara Händlerkalkulation 2027', 'Marco Rinaldi | 07.09.2026 | Eigene Verkaufspreise; noch kein Vertriebsvertrag');
  const f = sheet(wb, 'Monatsforecast', [145, 120, 120, 155, 155, 165, 370], 24, 'Geplanter Bezug 2027', 'Luminara | Planung vom 07.09.2026 | Erstbevorratung bereits im Januar enthalten');
  s.getRange('A5:D6').values = [['Produkt', 'Bezug EUR', 'Verkauf EUR', 'Betriebliche Herkunft'], ['M24', 420, 585, 'WM-IT-260714 / Marco']];
  s.getRange('A7:D7').values = [['M48', 690, 950, 'WM-IT-260714 / Marco']];
  input(s, 'B6:C7', money);
  val(s, 'F5', 'Lokale Handlingkosten EUR / Stück'); val(s, 'F6', 8); input(s, 'F6', money);
  val(s, 'F8', 'Messe / Werbung / Schulung EUR'); val(s, 'F9', 9000); input(s, 'F9', money);
  header(s, 12, ['Erstbevorratung', 'Stück', 'Einkauf / Stk.', 'Verkauf / Stk.', 'Einkauf gesamt', 'Verkauf gesamt', 'Handelsspanne', 'Spanne in %']);
  s.getRange('A13:B14').values = [['M24', 60], ['M48', 15]];
  for (let r=13; r<=14; r++) {
    const source = r-7;
    formula(s, `C${r}`, `=B${source}`); formula(s, `D${r}`, `=C${source}`);
    formula(s, `E${r}`, `=B${r}*C${r}`); formula(s, `F${r}`, `=B${r}*D${r}`);
    formula(s, `G${r}`, `=F${r}-E${r}`); formula(s, `H${r}`, `=IF(F${r}=0,0,G${r}/F${r})`);
  }
  val(s, 'A15', 'Summe');
  for(const c of ['B','E','F','G']) formula(s, `${c}15`, `=SUM(${c}13:${c}14)`);
  formula(s, 'H15', '=IF(F15=0,0,G15/F15)');
  s.getRange('C13:G15').setNumberFormat(money); s.getRange('H13:H15').setNumberFormat('0.0%'); total(s, 'A15:H15');
  val(s, 'A18', 'Jahresplanung netto EUR');
  formula(s, 'E18', "='Monatsforecast'!F18");
  val(s, 'A19', 'Geplanter eigener Verkauf');
  formula(s, 'F19', "='Monatsforecast'!B18*C6+'Monatsforecast'!C18*C7");
  val(s, 'A20', 'Handling und Markteinführung');
  formula(s, 'F20', "=('Monatsforecast'!B18+'Monatsforecast'!C18)*F6+F9");
  val(s, 'A21', 'Beitrag vor weiteren Kosten');
  formula(s, 'G21', '=F19-E18-F20');
  s.getRange('E18:G21').setNumberFormat(money);
  val(s, 'A23', 'Mindestbezug Weserblick EUR'); val(s, 'E23', 180000); input(s, 'E23', money);
  val(s, 'A24', 'Mindestbezug Luminara EUR'); val(s, 'E24', 150000); input(s, 'E24', money);
  val(s, 'A25', 'Plan minus Weserblick'); formula(s, 'G25', '=E18-E23');
  val(s, 'A26', 'Plan minus Luminara'); formula(s, 'G26', '=E18-E24'); s.getRange('G25:G26').setNumberFormat(money);
  val(s, 'A28', 'Lieferdatum geplant'); val(s, 'C28', serial('2027-01-11')); input(s, 'C28', dateFormat);
  val(s, 'D28', 'Ziel Tage, verlangt'); val(s, 'F28', 45); input(s, 'F28', '0');
  val(s, 'G28', 'Zieldatum'); formula(s, 'H28', '=C28+F28'); s.getRange('H28').setNumberFormat(dateFormat);
  val(s, 'A30', 'Herstellerangebot Anzahlung'); formula(s, 'E30', '=E15*30%');
  val(s, 'A31', 'Herstellerangebot vor Versand'); formula(s, 'E31', '=E15*40%');
  val(s, 'A32', 'Herstellerangebot Rest'); formula(s, 'E32', '=E15*30%'); s.getRange('E30:E32').setNumberFormat(money);
  val(s, 'A34', 'Alle Beträge netto. Eigenhandel, keine Provision. Steueransatz der Proforma unter Nachweisvorbehalt.');
  val(s, 'A35', 'Nicht enthalten: laufende Personalkosten, Finanzierung, weitere Serviceeinsätze und Steuern.');
  const csv = path.join(v, '14_Monthly_forecast_2027.csv');
  const python = path.join(deps, 'python/bin/python3');
  const source = JSON.parse(execFileSync(python, ['-c', 'import csv,json,sys\nwith open(sys.argv[1],encoding="utf-8-sig",newline="") as f: print(json.dumps(list(csv.DictReader(f,delimiter=";")),ensure_ascii=False))', csv], { encoding:'utf8' }));
  assert.equal(source.length, 12);
  header(f, 5, ['Monat', 'M24 Stück', 'M48 Stück', 'M24 Einkauf EUR', 'M48 Einkauf EUR', 'Bezug gesamt EUR', 'Planungsstatus']);
  f.getRange('A6:G17').values = source.map(row => [serial(`${row.Monat}-01`), Number(row['M24_Stück']), Number(row['M48_Stück']), null, null, null, row.Planstatus]);
  for(let r=6; r<=17; r++) {
    formula(f, `D${r}`, `=B${r}*'Kalkulation'!$B$6`);
    formula(f, `E${r}`, `=C${r}*'Kalkulation'!$B$7`);
    formula(f, `F${r}`, `=D${r}+E${r}`);
  }
  val(f, 'A18', 'Jahr 2027');
  for(const c of ['B','C','D','E','F']) formula(f, `${c}18`, `=SUM(${c}6:${c}17)`);
  input(f, 'A6:A17', 'yyyy-mm'); input(f, 'B6:C17', '0');
  f.getRange('D6:F18').setNumberFormat(money); total(f, 'A18:G18');
  val(f, 'A21', 'Quelle: 14_Monthly_forecast_2027.csv. Keine bestätigten Bestellungen.');
  val(f, 'A22', 'Direktkundengeschäfte und sechs Leihgeräte sind nicht in diesen Mengen enthalten.');
  val(f, 'A23', 'Die Januarzeile enthält 60 M24 und 15 M48 im Wert von 35.550 EUR.');
  s.freezePanes.freezeRows(12);
  f.freezePanes.freezeRows(5);
  wb.recalculate();
  val(f, 'B17', 31); wb.recalculate(); near(s.getRange('E18').values[0][0], 203250);
  val(f, 'B17', 30); val(s, 'F28', 0); wb.recalculate(); near(s.getRange('H28').values[0][0], serial('2027-01-11'));
  val(s, 'F28', 45); wb.recalculate();
  await exportBook(wb, path.join(v, '13_Haendlerkalkulation_2027.xlsx'), [['Kalkulation','A1:H35'], ['Monatsforecast','A1:G24']], [['Kalkulation','E15',35550],['Kalkulation','F15',49350],['Kalkulation','G15',13800],['Kalkulation','E18',202830],['Kalkulation','G21',66304],['Kalkulation','H28',serial('2027-02-25')],['Monatsforecast','B18',340],['Monatsforecast','C18',87],['Monatsforecast','F18',202830]]);
}

await projectBook();
await distributionBook();
console.log(`Visuelle Tabellenprüfung: ${qa}`);

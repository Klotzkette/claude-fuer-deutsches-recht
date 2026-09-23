#!/usr/bin/env node
// Baut ausschließlich die vier Excel-Quellen und ihre lokalen Sichtprüfungen.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadWorkbookRuntime } from './akten-workbook-runtime.mjs';

const { Workbook, SpreadsheetFile } = await loadWorkbookRuntime();
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const leipzig = path.join(root, 'testakten/anwaltschaft-lieferstreit-kaffeeroesterei-leipzig');
const mainz = path.join(root, 'testakten/anwaltschaft-arbeitsrecht-vertrieb-mainz');
const qaRoot = process.env.AKTEN_QA_DIR || '/tmp/anwaltschaft-leipzig-mainz-445-1-0';
const qaFor = dir => path.join(qaRoot, path.basename(dir));
const ld = JSON.parse(await fs.readFile(path.join(qaFor(leipzig), 'tabellendaten.json'), 'utf8'));
const md = JSON.parse(await fs.readFile(path.join(qaFor(mainz), 'tabellendaten.json'), 'utf8'));
const euro = '#,##0.00" EUR"';
const date = s => new Date(`${s}T00:00:00Z`);
const letter = index => String.fromCharCode(65 + index);

function base(name, title, source, headers, widths, count) {
  const wb = Workbook.create();
  const sheet = wb.worksheets.add(name);
  const last = letter(headers.length - 1);
  sheet.showGridLines = false;
  sheet.getRange(`A1:${last}${count + 15}`).format.font = { name: 'Times New Roman', size: 11, color: '#111111' };
  sheet.getRange('A2').values = [[title]];
  sheet.getRange('A2').format.font = { name: 'Times New Roman', size: 14, bold: true };
  sheet.getRange('A3').values = [[source]];
  sheet.getRange(`A5:${last}5`).values = [headers];
  sheet.getRange(`A5:${last}5`).format = { fill: '#334d47', font: { name: 'Times New Roman', size: 11, bold: true, color: '#ffffff' }, rowHeight: 34, wrapText: true, verticalAlignment: 'center' };
  sheet.getRange(`A6:${last}${count + 5}`).format.rowHeight = 25;
  sheet.getRange(`A6:${last}${count + 5}`).format.verticalAlignment = 'center';
  widths.forEach((width, i) => { sheet.getRange(`${letter(i)}1:${letter(i)}${count + 15}`).format.columnWidth = width; });
  sheet.freezePanes.freezeRows(5);
  return { wb, sheet, last };
}

function assertClose(actual, expected, label) {
  if (Math.abs(Number(actual) - expected) > 0.001) throw new Error(`${label}: ${actual} statt ${expected}`);
}

async function finish(wb, sheet, dir, filename, range, checks) {
  sheet.getRange(range).format.font.name = 'Times New Roman';
  wb.recalculate();
  checks();
  const errors = await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:20},maxChars:2000});
  await fs.writeFile(path.join(qaFor(dir), `${filename}.formelpruefung.txt`), errors.ndjson);
  const preview = await wb.render({sheetName:sheet.name,range,scale:1.5,format:'png'});
  await fs.writeFile(path.join(qaFor(dir), `${filename}.png`), new Uint8Array(await preview.arrayBuffer()));
  const xlsx = await SpreadsheetFile.exportXlsx(wb);
  await xlsx.save(path.join(qaFor(dir), filename));
  await fs.copyFile(path.join(qaFor(dir), filename), path.join(dir, filename));
  console.log(`${filename}: berechnet und gerendert`);
}

{
  const rows = ld['08_produktionsbuch_px12.csv'].slice(1);
  const {wb,sheet:s} = base('Produktion', 'PX12 Produktion 18. bis 20. August 2026', 'Maja Brandt, 21.09.2026. Übertragung aus Produktionsbuch P01 bis P18.', ['Messung','Datum','Minuten','Beutel 450 g','Naht offen','Naht geschlossen','Beutel je Minute'], [13,16,12,16,14,18,19],18);
  s.getRange('A6:G23').values = rows.map(r=>[r[0],date(r[1]),Number(r[3]),Number(r[4]),Number(r[5]),null,null]);
  s.getRange('A6:G23').format.rowHeight = 16;
  s.getRange('B6:B23').setNumberFormat('yyyy-mm-dd');
  s.getRange('C6:F25').setNumberFormat('0');
  s.getRange('F6:F23').formulas = rows.map((r,i)=>[`=D${i+6}-E${i+6}`]);
  s.getRange('G6:G23').formulas = rows.map((r,i)=>[`=D${i+6}/C${i+6}`]);
  s.getRange('G6:G25').setNumberFormat('0.0');
  s.getRange('A25').values = [['Summe']];
  s.getRange('C25:G25').formulas = [['=SUM(C6:C23)','=SUM(D6:D23)','=SUM(E6:E23)','=SUM(F6:F23)','=D25/C25']];
  s.getRange('A25:G25').format.font.bold = true;
  s.getRange('A27').values = [['Service vom 26.08.2026 separat: 60 Beutel in 10 Minuten, drei Nähte offen.']];
  s.getRange('A28').values = [['Nicht in obiger Summe enthalten. Quelle: SV-260826-114.']];
  const leaks = rows.reduce((sum,r)=>sum+Number(r[5]),0);
  await finish(wb,s,leipzig,'24_produktion_uebertragung.xlsx','A1:G29',()=>{
    assertClose(s.getRange('D25').values[0][0],990,'Beutel');
    assertClose(s.getRange('E25').values[0][0],leaks,'Naht offen');
    assertClose(s.getRange('G25').values[0][0],5.5,'Durchsatz');
    s.getRange('D6').values = [[60]];
    assertClose(s.getRange('G6').values[0][0],6,'Geänderter Zähler');
    s.getRange('D6').values = [[55]];
    wb.recalculate();
  });
}

{
  const {wb,sheet:s} = base('Zahlungen','PX12 Rechnungen und Zahlung','Leonie Pohl, 21.09.2026. Auftrag NW-260312-47; Beträge in EUR.', ['Vorgang','Netto','USt-Satz','Umsatzsteuer','Brutto'],[39,19,14,20,20],4);
  s.getRange('A6:E8').values = [['Auftrag / NW-261184',36000,.19,null,null],['Anzahlung / NW-260341',12000,.19,null,null],['Rest laut NW-261184',null,.19,null,null]];
  s.getRange('B8').formulas = [['=B6-B7']];
  s.getRange('D6:E8').formulas = [6,7,8].map(r=>[`=ROUND(B${r}*C${r},2)`,`=B${r}+D${r}`]);
  s.getRange('B6:B8').setNumberFormat(euro);
  s.getRange('C6:C8').setNumberFormat('0%');
  s.getRange('D6:E8').setNumberFormat(euro);
  s.getRange('A11:C11').values = [['Zahlung am','Betrag brutto','Beleg']];
  s.getRange('A12:C12').values = [[date('2026-03-20'),14280,'Kontoauszug Umsatz 184']];
  s.getRange('A12').setNumberFormat('yyyy-mm-dd');
  s.getRange('B12').setNumberFormat(euro);
  s.getRange('C12:E12').merge();
  s.getRange('A15').values = [['Gesamtrechnung abzüglich Bankzahlung']];
  s.getRange('E15').formulas = [['=E6-B12']];
  s.getRange('E15').setNumberFormat(euro);
  s.getRange('A17').values = [['Zahlungsdatei: 28.560 EUR vorgemerkt, nicht freigegeben. Kein weiterer Abgang.']];
  s.getRange('A18').values = [['Belege: NW-261184 vom 19.08., Kontoauszug, E-Mail vom 09.09.2026.']];
  s.getRange('A19').values = [['Angekündigter Einzug: 25.09.2026; Mandatskopie und Gläubigerkennung fehlen.']];
  s.getRange('A20').values = [['Quelle für Einzug: Schreiben Nordwerk vom 08.09.2026; kein gebuchter Umsatz.']];
  await finish(wb,s,leipzig,'25_zahlungen_px12.xlsx','A1:E21',()=>{
    assertClose(s.getRange('E6').values[0][0],42840,'Bruttoauftrag');
    assertClose(s.getRange('E8').values[0][0],28560,'Rest Rechnung');
    assertClose(s.getRange('E15').values[0][0],28560,'Offener Betrag');
    s.getRange('B12').values = [[15000]];
    assertClose(s.getRange('E15').values[0][0],27840,'Weitere Zahlung');
    s.getRange('B12').values = [[14280]];
    wb.recalculate();
  });
}

{
  const rows = md['14_crm_bonus_2025_rohdaten.csv'].slice(1);
  const {wb,sheet:s} = base('Bonus 2025','Torben Hesse Bonus 2025','Derya Engel, 21.09.2026. CRM-Auszug V25-101 bis V25-120, Änderung 21.04.2026.', ['Auftrag','Hesse Umsatz EUR','Personal Umsatz EUR','Abweichung EUR','Bonus Hesse EUR','Bonus Personal EUR'],[16,22,23,22,23,23],20);
  s.getRange('A6:F25').values = rows.map(r=>[r[0],Number(r[5]),Number(r[6]),null,null,null]);
  s.getRange('A29:B29').values = [['Bonussatz',.02]];
  s.getRange('B29').setNumberFormat('0%');
  s.getRange('D6:F25').formulas = rows.map((r,i)=>[`=B${i+6}-C${i+6}`,`=ROUND(B${i+6}*$B$29,2)`,`=ROUND(C${i+6}*$B$29,2)`]);
  s.getRange('A27').values = [['Summe']];
  s.getRange('B27:F27').formulas = [['=SUM(B6:B25)','=SUM(C6:C25)','=SUM(D6:D25)','=SUM(E6:E25)','=SUM(F6:F25)']];
  s.getRange('B6:F27').setNumberFormat('#,##0.00');
  s.getRange('A27:F27').format.font.bold = true;
  s.getRange('A31').values = [['Von Geschäftsführung genannte Verrechnung']];
  s.getRange('F31').values = [[1800]];
  s.getRange('A32').values = [['Rechenstand Personal nach dieser Verrechnung']];
  s.getRange('F32').formulas = [['=F27-F31']];
  s.getRange('F31:F32').setNumberFormat(euro);
  s.getRange('A34').values = [['Verrechnung aus E-Mail Engel vom 28.04.2026; GS26-0410 betrifft Umsatz 2026.']];
  s.getRange('A35').values = [['Bisher ausgezahlt: 0,00 EUR. Keine Freigabe der Geschäftsführung.']];
  s.getRange('A36').values = [['Die drei geänderten Zuordnungen stehen im CRM-Auszug, Spalten Änderung und Vermerk.']];
  await finish(wb,s,mainz,'15_bonusabgleich_2025.xlsx','A1:F37',()=>{
    assertClose(s.getRange('E27').values[0][0],14200,'Bonus Hesse');
    assertClose(s.getRange('F27').values[0][0],13000,'Bonus Personal');
    assertClose(s.getRange('F32').values[0][0],11200,'Rechenstand Verrechnung');
    s.getRange('B29').values = [[.03]];
    assertClose(s.getRange('E27').values[0][0],21300,'Geänderter Bonussatz');
    s.getRange('B29').values = [[.02]];
    wb.recalculate();
  });
}

{
  const days = ['2026-01-02','2026-01-05','2026-05-04','2026-05-05','2026-05-06','2026-05-07','2026-05-08','2026-07-20','2026-07-21','2026-07-22','2026-07-23','2026-07-24','2026-09-07','2026-09-08','2026-09-09','2026-09-10','2026-09-11'];
  const {wb,sheet:s} = base('Kalender','Torben Hesse Urlaubskalender 2026','Derya Engel, Stand 21.09.2026. Urlaubskarte und E-Mail Hesse vom 16.09.2026.', ['Datum','Teamkalender','Tage Personal','Tage Hesse','Termin / Rückmeldung'],[17,21,18,17,50],17);
  s.getRange('A6:E22').values = days.map((d,i)=>[date(d),'Urlaub genehmigt',1,i<12?1:0,i<12?'Genommen; kein Änderungsantrag':[
    'Altenhof: Besprechung 09:00 bis 10:00',
    'Berghaus: Telefontermin 10:30 bis 11:30',
    'Nora: Hesse nennt Übergabegespräch',
    'CRM-Auswertung, Chat vom 10.09.',
    'Budgettabelle, Teamablage 09:17 Uhr'][i-12]]);
  s.getRange('A6:A22').setNumberFormat('yyyy-mm-dd');
  s.getRange('C6:D22').setNumberFormat('0');
  s.getRange('A24:D28').values = [['Jahresurlaub',null,30,30],['Übertrag 2025',null,4,4],['Abgebucht',null,null,null],['Rest Personal',null,null,null],['Rest laut Hesse',null,null,null]];
  s.getRange('C26:D26').formulas = [['=SUM(C6:C22)','=SUM(D6:D22)']];
  s.getRange('C27').formulas = [['=C24+C25-C26']];
  s.getRange('D28').formulas = [['=D24+D25-D26']];
  s.getRange('A30').values = [['07. bis 11.09.: Hesse verlangt Rückbuchung von fünf Tagen; Berg hat nicht gegengezeichnet.']];
  s.getRange('A31').values = [['Terminquellen: Teamkalender, E-Mail Berg 07.09., Gespräch Seifert 18.09. und Bürochat.']];
  s.getRange('A32').values = [['Für die Septemberwoche fehlen vollständige Tagesaufzeichnungen.']];
  s.getRange('A33').values = [['Übertrag: Genehmigungen Berg vom 12.12.2025 und 20.03.2026 auf der Urlaubskarte.']];
  await finish(wb,s,mainz,'18_urlaubskalender_2026.xlsx','A1:E34',()=>{
    assertClose(s.getRange('C27').values[0][0],17,'Rest Personal');
    assertClose(s.getRange('D28').values[0][0],22,'Rest Hesse');
    s.getRange('D18').values = [[1]];
    assertClose(s.getRange('D28').values[0][0],21,'Änderung Septembertag');
    s.getRange('D18').values = [[0]];
    wb.recalculate();
  });
}

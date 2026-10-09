import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';

// Der Paketpfad wird vom aufrufenden Arbeitsplatz bereitgestellt.
const require = createRequire(path.join(process.env.ARTIFACT_NODE_MODULES, '..', 'package.json'));
const { Workbook, SpreadsheetFile } = require('@oai/artifact-tool');
const root = path.resolve(process.argv[2] || '.');
const out = path.join(root, 'testakten/gesellschaftervereinbarung-drohnenfriseur-berlin');
const previewDir = process.argv[3];
const wb = Workbook.create();
const cap = wb.worksheets.add('Kapital');
const cash = wb.worksheets.add('Tranchen');
const budget = wb.worksheets.add('Budget');
const sheets = [cap, cash, budget];
for (const sheet of sheets) {
  sheet.showGridLines = false;
  sheet.getRange('A1:J24').format.font = { name: 'Arial', size: 10, color: '#202020' };
  sheet.getRange('A1:J24').format.rowHeight = 22;
  sheet.getRange('A1:J24').format.verticalAlignment = 'center';
  sheet.getRange('A1:A24').format.columnWidth = 3;
  sheet.getRange('B1:B24').format.columnWidth = 29;
  sheet.getRange('C1:J24').format.columnWidth = 17;
  sheet.getRange('B2').format.font = { name: 'Arial', size: 15, bold: true };
}
function header(sheet, range) {
  sheet.getRange(range).format = { fill: '#394955', font: { name: 'Arial', color: '#FFFFFF', bold: true }, wrapText: true, rowHeight: 38, horizontalAlignment: 'center' };
}
function total(sheet, range) {
  sheet.getRange(range).format = { fill: '#E7EDF0', font: { name: 'Arial', bold: true }, borders: { top: { style: 'thin', color: '#394955' } } };
}
cap.getRange('B2').values = [['SkyFade Robotics Kapitalübersicht']];
cap.getRange('B3').values = [['9. Oktober 2026 · Bestand und geplante Kapitalzustände · EUR Nennbetrag']];
cap.getRange('B5:I5').values = [['Gesellschafter','Bestand','Neu Tranche 1','Nach Tranche 1','Neu Tranche 2','Nach Tranche 2','Quote Bestand','Quote final']];
header(cap,'B5:I5');
const parties = ['Kunigunde Wolkenberger','Kilian Funkenschlag','Ottilie Trutz','ABC Ventures GmbH','DEF Partners GmbH','GHI Capital GmbH','JKL Fonds GmbH'];
cap.getRange('B6:D12').values = parties.map((name,i)=>[name,[12500,12500,5000,11000,9000,0,0][i],0]);
cap.getRange('D11:D12').formulas = [["='Tranchen'!F7"],["='Tranchen'!F8"]];
cap.getRange('F6:F12').values = [[0],[0],[0],[0],[0],[0],[0]];
cap.getRange('F11:F12').formulas = [["='Tranchen'!F9"],["='Tranchen'!F10"]];
for (let r=6;r<=12;r++) {
  cap.getRange(`E${r}`).formulas = [[`=SUM(C${r}:D${r})`]];
  cap.getRange(`G${r}`).formulas = [[`=SUM(E${r}:F${r})`]];
  cap.getRange(`H${r}:I${r}`).formulas = [[`=C${r}/$C$13`,`=G${r}/$G$13`]];
}
cap.getRange('B13').values=[['Gesamt']];
cap.getRange('C13:I13').formulas=[['=SUM(C6:C12)','=SUM(D6:D12)','=SUM(E6:E12)','=SUM(F6:F12)','=SUM(G6:G12)','=SUM(H6:H12)','=SUM(I6:I12)']];
cap.getRange('C6:G13').setNumberFormat('#,##0');
cap.getRange('C6:I13').format.horizontalAlignment='right';
cap.getRange('H6:I13').setNumberFormat('0.0000%');
cap.getRange('C6:C12').format.font.color='#0000FF';
cap.getRange('D11:D12').format.font.color='#008000';
cap.getRange('F11:F12').format.font.color='#008000';
total(cap,'B13:I13');
cap.getRange('B16').values=[['Bestand: Beteiligungsübersicht vom 30. September 2026.']];
cap.getRange('B17').values=[['Neue Anteile sind geplant. Entstehung jeweils erst nach dem erforderlichen Registervollzug.']];
cap.getRange('B18').values=[['Kein neuer Mitarbeiterpool eingerechnet. Keine Erlösverteilung aus diesen Quoten ableiten.']];
cash.getRange('B2').values=[['SkyFade Robotics Finanzierungsplan']];
cash.getRange('B3').values=[['Vorschlag vom 9. Oktober 2026 · noch keine Zahlung der neuen Investoren']];
cash.getRange('B5:C5').values=[['Ausgabebetrag je Anteil EUR',500]];
cash.getRange('C5').format.font.color='#0000FF';
cash.getRange('B6:H6').values=[['Investor','Tranche','Ausgabebetrag EUR','Nennwert je Anteil','Neue Anteile','Nennbetrag EUR','Agio EUR']];
header(cash,'B6:H6');
cash.getRange('B7:E10').values=[['GHI Capital GmbH',1,4500000,1],['JKL Fonds GmbH',1,1500000,1],['GHI Capital GmbH',2,3000000,1],['JKL Fonds GmbH',2,1000000,1]];
cash.getRange('C7:E10').format.font.color='#0000FF';
for(let r=7;r<=10;r++) cash.getRange(`F${r}:H${r}`).formulas=[[`=D${r}/$C$5`,`=F${r}*E${r}`,`=D${r}-G${r}`]];
cash.getRange('B12').values=[['Tranche 1 gesamt']];
cash.getRange('D12:H12').formulas=[['=SUM(D7:D8)','', '=SUM(F7:F8)','=SUM(G7:G8)','=SUM(H7:H8)']];
cash.getRange('B13').values=[['Tranche 2 gesamt']];
cash.getRange('D13:H13').formulas=[['=SUM(D9:D10)','', '=SUM(F9:F10)','=SUM(G9:G10)','=SUM(H9:H10)']];
cash.getRange('B14').values=[['Beide Tranchen']];
cash.getRange('D14:H14').formulas=[['=SUM(D12:D13)','', '=SUM(F12:F13)','=SUM(G12:G13)','=SUM(H12:H13)']];
cash.getRange('D7:H14').setNumberFormat('#,##0');
cash.getRange('C7:H14').format.horizontalAlignment='right';
cash.getRange('D7:H14').format.columnWidth=20;
total(cash,'B14:H14');
cash.getRange('B17').values=[['Quelle: Term Sheet Nummer 3. Die zweite Tranche hängt von noch zu vereinbarenden Nachweisen ab.']];
cash.getRange('B18').values=[['Blaue Zahlen: Eingaben. Schwarze Zahlen: Formeln. Grüne Zahlen: Verknüpfungen zu anderen Blättern.']];
budget.getRange('B2').values=[['SkyFade Robotics Mittelverwendung']];
budget.getRange('B3').values=[['Budgetvorschlag bei vollständiger Finanzierung · keine bereits gebuchten Ausgaben']];
budget.getRange('B5').values=[['Gesamtrahmen EUR']];
budget.getRange('C5').formulas=[["='Tranchen'!D14"]];
budget.getRange('C5').format.font.color='#008000';
budget.getRange('C5').setNumberFormat('#,##0');
budget.getRange('B7:D7').values=[['Verwendungsbereich','Anteil','Budget EUR']];
header(budget,'B7:D7');
budget.getRange('B8:C12').values=[['Robotik und Sicherheit',0.35],['Zulassung und Versicherung',0.2],['Software und Daten',0.2],['Personal und Pilotstandorte',0.15],['Betriebskapital',0.1]];
for(let r=8;r<=12;r++) budget.getRange(`D${r}`).formulas=[[`=C${r}*$C$5`]];
budget.getRange('B13').values=[['Gesamt']];
budget.getRange('C13:D13').formulas=[['=SUM(C8:C12)','=SUM(D8:D12)']];
budget.getRange('C8:C13').setNumberFormat('0%');
budget.getRange('D8:D13').setNumberFormat('#,##0');
budget.getRange('C8:D13').format.horizontalAlignment='right';
budget.getRange('C8:C12').format.font.color='#0000FF';
total(budget,'B13:D13');
budget.getRange('B16').values=[['Quelle: Term Sheet Nummer 5. Ein Zeitplan bis zur zweiten Tranche wird noch abgestimmt.']];
wb.recalculate();
const totals = cap.getRange('C13:I13').values[0];
if(totals[0]!==50000 || totals[2]!==62000 || totals[4]!==70000 || Math.abs(totals[5]-1)>1e-10 || Math.abs(totals[6]-1)>1e-10) throw new Error('Kapitalabgleich fehlgeschlagen');
if(cash.getRange('D14').values[0][0]!==10000000 || cash.getRange('H14').values[0][0]!==9980000 || budget.getRange('D13').values[0][0]!==10000000) throw new Error('Finanzierungsabgleich fehlgeschlagen');
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!',options:{useRegex:true,maxResults:20}})).ndjson);
if(previewDir) {
  await fs.mkdir(previewDir,{recursive:true});
  for(const sheet of sheets) {
    const png=await wb.render({sheetName:sheet.name,range:sheet.name==='Budget'?'B2:H17':'B2:I19',scale:1.3,format:'png'});
    await fs.writeFile(path.join(previewDir,`${sheet.name}.png`),new Uint8Array(await png.arrayBuffer()));
  }
}
await fs.mkdir(out,{recursive:true});
await (await SpreadsheetFile.exportXlsx(wb)).save(path.join(out,'22_Kapital_und_Finanzierungsplan.xlsx'));
console.log(JSON.stringify({capital:totals,financing:cash.getRange('D14:H14').values[0]}));

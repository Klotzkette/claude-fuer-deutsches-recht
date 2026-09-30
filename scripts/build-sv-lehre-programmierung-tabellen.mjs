import fs from 'node:fs/promises';
import path from 'node:path';
import {Workbook, SpreadsheetFile} from '@oai/artifact-tool';

// Run with bundled Node and the bundled public artifact-tool package available.
const root=process.argv[2];
if(!root) throw new Error('Repository root argument required');
const qa=process.env.SV_AKTEN_QA_DIR||'/tmp/sozialversicherungspflicht-20260930/akten-qa';
await fs.mkdir(qa,{recursive:true});
const reports=[];
const money='#,##0.00 "€";[Red](#,##0.00) "€";"–"';

function style(s,last,title,subtitle,widths){
  s.showGridLines=false;
  s.getRange(`A1:${last}23`).format.font={name:'Calibri',size:11,color:'#222222'};
  s.getRange(`A1:${last}23`).format.rowHeight=24;
  s.getRange(`A1:${last}1`).merge();s.getRange('A1').values=[[title]];
  s.getRange(`A1:${last}1`).format={fill:'#ECECEC',font:{name:'Calibri',size:16,bold:true,color:'#222222'},rowHeight:32};
  s.getRange(`A2:${last}2`).merge();s.getRange('A2').values=[[subtitle]];
  s.getRange(`A2:${last}2`).format.font={name:'Calibri',size:10,color:'#555555'};
  s.getRange(`A4:${last}4`).format={fill:'#DAE5EB',font:{name:'Calibri',size:11,bold:true},rowHeight:36,wrapText:true};
  widths.forEach((w,i)=>s.getRange(`${String.fromCharCode(65+i)}:${String.fromCharCode(65+i)}`).format.columnWidth=w);
  s.freezePanes.freezeRows(4);
}
function note(s,row,last,text){s.getRange(`A${row}:${last}${row}`).merge();s.getRange(`A${row}`).values=[[text]];s.getRange(`A${row}:${last}${row}`).format={wrapText:true,rowHeight:34,font:{name:'Calibri',size:10,color:'#555555'}};}
function total(s,row,last){s.getRange(`A${row}:${last}${row}`).format={fill:'#E8E8E8',font:{name:'Calibri',size:11,bold:true},rowHeight:28};}
function assertNear(actual,expected,label){if(Math.abs(Number(actual)-expected)>0.00001||!Number.isFinite(Number(actual)))throw new Error(`${label}: ${actual} != ${expected}`);}
async function finish(wb,slug,filename,checks){
  wb.recalculate();
  const inspection=await wb.inspect({kind:'workbook,sheet,table',maxChars:4000,tableMaxRows:4,tableMaxCols:5});
  const sheets=[];
  for(let i=0;i<2;i++){
    const s=wb.worksheets.getItemAt(i);const vals=s.getRange('A1:J24').values;
    for(const row of vals)for(const v of row)if(typeof v==='string'&&/^#(?:REF!|DIV\/0!|VALUE!|N\/A|NAME\?|NUM!|SPILL!|CALC!)/.test(v))throw new Error(`Formula error ${v}`);
    const png=await wb.render({sheetName:s.name,range:'A1:'+ (i===0?(slug.includes('musik')?'I':'H'):'F')+'23',scale:1.6,format:'png'});
    const image=path.join(qa,`${slug}__${i+1}.png`);await fs.writeFile(image,new Uint8Array(await png.arrayBuffer()));
    sheets.push({name:s.name,image,values:vals,formulas:s.getRange('A1:J24').formulas});
  }
  const output=path.join(root,'testakten',slug,filename);
  await(await SpreadsheetFile.exportXlsx(wb)).save(output);
  try{await fs.rename(output+'.inspect.ndjson',path.join(qa,slug+'.inspect.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
  reports.push({slug,output,checks,sheets,inspection});
}

if(!process.argv.includes('--programming-only')){
const wb=Workbook.create();const s=wb.worksheets.add('Akademie 2025');const own=wb.worksheets.add('Weitere Einnahmen');
style(s,'I','Honorarübersicht 2025 – Mara Noémi Zwirn','Büroabgleich vom 23.09.2026 · Beträge laut korrigierten Monatsrechnungen',[13,12,12,12,13,17,17,16,34]);
s.getRange('A4:I4').values=[['Monat','Unterricht / 45 Min.','Bezahlte Ausfälle','Auftritt / 45 Min.','Satz','Honorar','Zahlungen','Differenz','Bemerkung']];
const data=[[64,4,0,'Januar: Korrektur statt Erstfassung'],[60,3,2,'72 € Probespiel separat überwiesen'],[72,4,0,''],[48,2,0,'Osterferien'],[68,4,0,''],[56,2,2,'Konzertreise; Nachholstunden'],[36,1,0,'Sommerferien'],[0,0,0,'Keine Rechnung'],[76,3,0,''],[64,2,0,'Herbstferien'],[72,2,0,'Eigene Ausfälle ohne Honorar'],[48,3,2,'Schülerkonzert']];
s.getRange('A5:I16').values=data.map(([u,a,v,n],i)=>[`2025-${String(i+1).padStart(2,'0')}`,u,a,v,36,null,(u+a+v)*36,null,n]);
s.getRange('F5:F16').formulas=data.map((_,i)=>[`=SUM(B${i+5}:D${i+5})*E${i+5}`]);
s.getRange('H5:H16').formulas=data.map((_,i)=>[`=G${i+5}-F${i+5}`]);
s.getRange('A17').values=[['Jahr 2025']];s.getRange('B17:D17').formulas=[['=SUM(B5:B16)','=SUM(C5:C16)','=SUM(D5:D16)']];s.getRange('F17:H17').formulas=[['=SUM(F5:F16)','=SUM(G5:G16)','=SUM(H5:H16)']];total(s,17,'I');
s.getRange('E5:H17').setNumberFormat(money);s.getRange('B5:E16').format.font.color='#174F82';s.getRange('G5:G16').format.font.color='#174F82';s.getRange('I5:I16').format={wrapText:true,rowHeight:34};
note(s,19,'I','Januar: 72 zunächst berechnete Einheiten wurden um 4 Einheiten gekürzt. Korrigierte Rechnung: 68 × 36 € = 2.448 €.');
note(s,20,'I','Notenerstattung 27,80 € vom 18.02.2025 ist kein Honorar und bleibt in dieser Übersicht unberücksichtigt.');
note(s,21,'I','Zahlungen sind den Leistungsmonaten zugeordnet, nicht nach Bankmonat sortiert. Grundlage: Honorarkonto und Rechnungskopien.');
style(own,'F','Eigene Unterrichts- und Auftrittseinnahmen','Aufstellung Mara vom 24.09.2026 · Einnahmen, keine Gewinnermittlung',[29,18,18,21,26,42]);
own.getRange('A4:F4').values=[['Auftrag / Person','Einheiten 2025','Honorar je Einheit','Jahreseinnahmen','Abrechnung','Anmerkung']];
own.getRange('A5:F8').values=[['Paul Werner',40,48,null,'Eigene Rechnung','60 Minuten; Unterricht zu Hause'],['Greta Lind',30,48,null,'Eigene Rechnung','60 Minuten; Unterricht zu Hause'],['Louis Schapp',25,48,null,'Eigene Rechnung','60 Minuten; Unterricht zu Hause'],['Musikraum Pankow',65,60,null,'Monatsrechnung','Workshops / Auftritte; noch aufzuteilen']];
own.getRange('D5:D8').formulas=[['=B5*C5'],['=B6*C6'],['=B7*C7'],['=B8*C8']];own.getRange('A10').values=[['Weitere Einnahmen']];own.getRange('D10').formulas=[['=SUM(D5:D8)']];total(own,10,'F');
own.getRange('A12').values=[['Akademiehonorar']];own.getRange('D12').formulas=[["='Akademie 2025'!F17"]];own.getRange('A13').values=[['Honorare zusammen']];own.getRange('D13').formulas=[['=D10+D12']];total(own,13,'F');own.getRange('C5:D13').setNumberFormat(money);own.getRange('B5:C8').format.font.color='#174F82';own.getRange('E5:F8').format={wrapText:true,rowHeight:38};
note(own,16,'F','Keine Betriebsausgaben abgezogen. Private Altersvorsorge, Krankenversicherung und Fahrtkosten sind hier nicht erfasst.');
note(own,17,'F','Die drei Privatpersonen hatten schon vor Beginn des Akademievertrags Unterricht bei Mara. Belege im privaten Rechnungsordner.');
note(own,18,'F','Pankow: Rechnungspositionen sind bisher nur nach Honorarstunden addiert. Trennung von Workshops und Auftritten für die KSK noch offen.');
wb.recalculate();const expected=data.reduce((sum,[u,a,v])=>sum+(u+a+v)*36,0);assertNear(s.getRange('F17').values[0][0],expected,'music total');assertNear(own.getRange('D10').values[0][0],8460,'own total');assertNear(own.getRange('D13').values[0][0],expected+8460,'cross sheet');
const original=s.getRange('B5').values[0][0];s.getRange('B5').values=[[original+1]];wb.recalculate();assertNear(s.getRange('F17').values[0][0],expected+36,'input delta');assertNear(own.getRange('D13').values[0][0],expected+8460+36,'cross sheet input delta');assertNear(s.getRange('H5').values[0][0],-36,'reconciliation delta');s.getRange('B5').values=[[original]];wb.recalculate();assertNear(s.getRange('H17').values[0][0],0,'restored reconciliation');
await finish(wb,'sozialversicherung-musikakademie-prenzlauer-berg','27_Honorarabgleich_2025.xlsx',{independentAnnual:expected,otherIncome:8460,inputChange:'B5 +1 => honorar +36, discrepancy -36, cross-sheet +36; restored',restoredTotal:s.getRange('F17').values[0][0]});
}

{
const wb=Workbook.create();const s=wb.worksheets.add('Nordlicht 2025');const other=wb.worksheets.add('Linde und Gesamt');
style(s,'H','Kern Software – Rechnungsabgleich 2025','Jonas Kern-Knörz · Stand 22.09.2026 · Nettowerte, Umsatzsteuer und Zahlung getrennt',[14,14,15,19,19,19,19,34]);
s.getRange('A4:H4').values=[['Monat','Stunden','Satz netto','Nettohonorar','USt 19 %','Bruttobetrag','Zahlungseingang','Bemerkung']];
s.getRange('A4:H17').format.verticalAlignment='center';
s.getRange('B4:G4').format.horizontalAlignment='center';
const hrs=[128,136,144,120,136,128,96,112,144,152,128,88];
const paydates=['2025-02-26','2025-03-26','2025-04-25','2025-05-26','2025-06-26','2025-07-25','2025-08-26','2025-09-26','2025-10-27','2025-11-26','2025-12-23','2026-01-26'];
s.getRange('A5:H16').values=hrs.map((h,i)=>[`2025-${String(i+1).padStart(2,'0')}`,h,105,null,null,null,paydates[i],i===3?'3 Stunden nach Rücksprache abgezogen':i===6?'Zwei Wochen ohne Leistungsstunden':i===11?'Zahlung erst im Folgejahr':'']);
s.getRange('D5:F16').formulas=hrs.map((_,i)=>{const r=i+5;return [`=B${r}*C${r}`,`=ROUND(D${r}*19%,2)`,`=D${r}+E${r}`]});
s.getRange('A17').values=[['Summe']];s.getRange('B17').formulas=[['=SUM(B5:B16)']];s.getRange('D17:F17').formulas=[['=SUM(D5:D16)','=SUM(E5:E16)','=SUM(F5:F16)']];total(s,17,'H');s.getRange('C5:F17').setNumberFormat(money);s.getRange('B5:C16').format.font.color='#174F82';s.getRange('H5:H16').format={wrapText:true,rowHeight:34};
s.getRange('B5:F17').format.horizontalAlignment='right';
s.getRange('A5:H16').format.rowHeight=24;
s.getRange('B5:B17').setNumberFormat('0"  "');
s.getRange('C5:F17').setNumberFormat('#,##0.00 "€  ";[Red](#,##0.00) "€  ";"–  "');
s.getRange('G5:G16').format.horizontalAlignment='center';
note(s,19,'H','Nur Nordlicht-Rechnungen für Leistungen 2025. Die ursprüngliche Migration wurde 2024 mit 95 € pro Stunde abgerechnet.');
note(s,20,'H','Zahlungsdaten stammen aus den Kontozuordnungen. Die Dezemberleistung wurde erst am 26.01.2026 bezahlt.');
note(s,21,'H','Rechnung KS-2025-002: Januar 128 Stunden × 105 € = 13.440 € netto; 15.993,60 € brutto.');
s.getRange('A19:H21').format.rowHeight=24;
style(other,'F','Linde Analytik und Jahresüberblick','Ausgangsrechnungen nach Leistungszuordnung · Zusammenstellung für den Beratungstermin',[20,20,20,21,22,39]);
other.getRange('A4:F4').values=[['Rechnung / Monat','Netto','USt 19 %','Brutto','Zahlung','Leistung']];
other.getRange('A4:F13').format.verticalAlignment='center';
other.getRange('B4:E4').format.horizontalAlignment='center';
other.getRange('A5:F8').values=[['März 2025',4000,null,null,'2025-04-09','Messdatenformat A'],['Juni 2025',4800,null,null,'2025-07-08','Bericht und Prüflauf'],['September 2025',5200,null,null,'2025-10-10','Erweiterung Serienimport'],['November 2025',4400,null,null,'2025-12-09','Zusätzliche Spalten / KS-2025-024']];
other.getRange('C5:D8').formulas=[5,6,7,8].map(r=>[`=ROUND(B${r}*19%,2)`,`=B${r}+C${r}`]);other.getRange('A10').values=[['Linde 2025']];other.getRange('B10:D10').formulas=[['=SUM(B5:B8)','=SUM(C5:C8)','=SUM(D5:D8)']];total(other,10,'F');
other.getRange('A12').values=[['Nordlicht 2025']];other.getRange('B12:D12').formulas=[["='Nordlicht 2025'!D17","='Nordlicht 2025'!E17","='Nordlicht 2025'!F17"]];other.getRange('A13').values=[['Zusammen']];other.getRange('B13:D13').formulas=[['=B10+B12','=C10+C12','=D10+D12']];total(other,13,'F');other.getRange('B5:D13').setNumberFormat(money);other.getRange('B5:B8').format.font.color='#174F82';other.getRange('F5:F8').format={wrapText:true,rowHeight:38};
other.getRange('B5:D13').format.horizontalAlignment='right';
other.getRange('B5:D13').setNumberFormat('#,##0.00 "€  ";[Red](#,##0.00) "€  ";"–  "');
other.getRange('E5:E8').format.horizontalAlignment='center';
note(other,16,'F','Die Aufstellung enthält Umsätze vor Ausgaben. Software, Haftpflicht, Reisen und eigene Vorsorge sind nicht abgezogen.');
note(other,17,'F','Die Linde-Pakete wurden zum Festpreis angeboten. Stunden für diese Arbeiten werden in der Nordlicht-Liste nicht erfasst.');
wb.recalculate();const net=hrs.reduce((a,b)=>a+b,0)*105;assertNear(s.getRange('D17').values[0][0],net,'programmer net');assertNear(other.getRange('B10').values[0][0],18400,'linde net');assertNear(other.getRange('B13').values[0][0],net+18400,'all net');
s.getRange('B5').values=[[129]];wb.recalculate();assertNear(s.getRange('D17').values[0][0],net+105,'hour delta');assertNear(s.getRange('E5').values[0][0],2573.55,'VAT delta');assertNear(other.getRange('B13').values[0][0],net+18400+105,'cross sheet delta');s.getRange('B5').values=[[128]];wb.recalculate();assertNear(s.getRange('F5').values[0][0],15993.6,'restored invoice');
await finish(wb,'sozialversicherung-programmierer-leipzig','27_Rechnungsabgleich_2025.xlsx',{independentNet:net,lindeNet:18400,inputChange:'B5 128→129: net +105, VAT +19.95, cross-sheet +105; restored',restoredInvoice:s.getRange('F5').values[0][0]});
}
await fs.writeFile(path.join(qa,'tabellen-pruefung.json'),JSON.stringify(reports,null,2));
console.log(JSON.stringify(reports.map(({slug,checks})=>({slug,checks})),null,2));

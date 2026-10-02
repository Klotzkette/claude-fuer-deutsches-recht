/** Zwei Arbeitsmappen der Berliner und Münchner Vorführakten, ohne Lösungsbewertung. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook, SpreadsheetFile, requireRuntime} = await loadWorkbookRuntime(['jszip']);
const JSZip = requireRuntime('jszip');
const [root, qa] = process.argv.slice(2);
if (!root || !qa) throw new Error('Aufruf: <Testakten-Verzeichnis> <QA-Verzeichnis>');
await fs.mkdir(qa, {recursive:true});
const euro = '#,##0.00;(#,##0.00);0.00';
function sheet(wb, name, title, widths, rows) {
  const s = wb.worksheets.add(name);
  s.showGridLines = false;
  s.getRangeByIndexes(0,0,rows,widths.length).format = {font:{name:'Arial',size:10,color:'#222222'},rowHeight:20,verticalAlignment:'center'};
  widths.forEach((w,i) => {s.getRangeByIndexes(0,i,rows,1).format.columnWidth = w;});
  s.getRange('A2').values = [[title]];
  s.getRange('A2').format.font = {name:'Arial',size:14,bold:true};
  s.getRangeByIndexes(1,0,1,widths.length).format.rowHeight=28;
  for(const row of [1,4])s.getRangeByIndexes(row-1,0,1,widths.length).format.rowHeight=8;
  return s;
}
function header(s,row,labels) {
  const r=s.getRangeByIndexes(row-1,0,1,labels.length);
  r.values=[labels]; r.format={fill:'#E5E8ED',font:{bold:true},wrapText:true,rowHeight:34,horizontalAlignment:'center'};
}
function f(s,cell,text) {s.getRange(cell).formulas=[[text]];}
function assertCell(s,cell,expected) {
  const actual=s.getRange(cell).values[0][0];
  if(typeof actual!=='number'||Math.abs(actual-expected)>1e-8) throw new Error(`${s.name}!${cell}: ${actual}, erwartet ${expected}`);
}
const bank=Workbook.create();
const b=sheet(bank,'Projektkonto','Spreebogen Lichtwerk GmbH – Projektkonto August 2026',[15,16,33,18,18,18],21);
b.getRange('A3').values=[['Ottilie Heller, 31.08.2026. Beträge in EUR. Quelle: Bankexport B-0818 bis B-0831.']];
header(b,5,['Buchungstag','Beleg','Zweck','Eingang EUR','Ausgang EUR','Saldo EUR']);
b.getRange('A6:F6').values=[[new Date('2026-08-17T00:00:00Z'),'Übertrag','Bestand vor Buchungen',null,null,32000]];
const records=[['2026-08-18','B-0818','Lindenhof Abschlag',25000,0],['2026-08-19','B-0819','Werkstattmiete',0,2400],['2026-08-21','B-0821','SBS-2026-084',0,18400],['2026-08-24','B-0824','Kabelkontor',0,1250],['2026-08-28','B-0828','Lindenhof Restzahlung',12000,0],['2026-08-31','B-0831','Löhne Sammelauftrag',0,18750]];
b.getRange('A7:E12').values=records.map(([d,...r])=>[new Date(d+'T00:00:00Z'),...r]);
for(let row=7;row<=12;row++) f(b,`F${row}`,`=F${row-1}+D${row}-E${row}`);
b.getRange('C14').values=[['Summe / Schlussbestand']];
f(b,'D14','=SUM(D7:D12)'); f(b,'E14','=SUM(E7:E12)'); f(b,'F14','=F12');
b.getRange('C14:F14').format={fill:'#F1F2F4',font:{bold:true},rowHeight:29};
b.getRange('D6:F14').setNumberFormat(euro); b.getRange('A6:A12').setNumberFormat('yyyy-mm-dd');
b.getRange('D6:F14').format.horizontalAlignment='right';
b.getRange('A17').values=[['Erfassung: Projektkonto, nicht sämtliche Konten der Gesellschaft.']];
b.getRange('A18').values=[['Das Geschäftsführerentgelt September läuft über das Lohnkonto und steht hier nicht.']];
b.getRange('A19').values=[['Ausführungszeit B-0821: 21.08.2026, 07:43 Uhr, Nutzerkennung GS.']];
b.getRange('A20').values=[['Die Liste dokumentiert Zahlungen, keine Bestell- oder Gesellschafterfreigaben.']];
bank.recalculate(); assertCell(b,'D14',37000); assertCell(b,'E14',40800); assertCell(b,'F14',28200);
b.getRange('E9').values=[[19400]];bank.recalculate();assertCell(b,'F14',27200);b.getRange('E9').values=[[18400]];bank.recalculate();
const cap=Workbook.create();
const c=sheet(cap,'Kapitalaufnahme','Isarwinkel Gerätebau GmbH – Beteiligungsvorschlag',[30,19,19,19,19,19],23);
c.getRange('A3').values=[['Ottmar Fürst, 30.09.2026. Vorschlag aus Vogls Eckpunkten, noch nicht vollzogen.']];
header(c,5,['Beteiligter','Bisher EUR','Bisher Anteil','Neue Einlage EUR','Danach EUR','Danach Anteil']);
c.getRange('A6:F8').values=[['Hildegard Steinlechner',15000,null,0,null,null],['Quirin Rottmayer',10000,null,0,null,null],['Albrecht Vogl',0,null,6250,null,null]];
c.getRange('A9').values=[['Summe']];
for(const col of ['B','D','E'])f(c,`${col}9`,`=SUM(${col}6:${col}8)`);
for(let row=6;row<=8;row++){f(c,`C${row}`,`=B${row}/$B$9`);f(c,`E${row}`,`=B${row}+D${row}`);f(c,`F${row}`,`=E${row}/$E$9`);}
f(c,'C9','=SUM(C6:C8)');f(c,'F9','=SUM(F6:F8)');
c.getRange('A9:F9').format={fill:'#F1F2F4',font:{bold:true},rowHeight:29};
c.getRange('A12:B15').values=[['Vogl, Zahlung insgesamt',200000],['Davon neue Stammeinlage',null],['Davon Aufgeld',null],['Zahlung an Altgesellschafter',0]];
f(c,'B13','=D8');f(c,'B14','=B12-B13');
for(const range of ['B6:B9','D6:E9','B12:B15'])c.getRange(range).setNumberFormat(euro);
for(const range of ['C6:C9','F6:F9'])c.getRange(range).setNumberFormat('0.0%');
c.getRange('B6:F15').format.horizontalAlignment='right';
c.getRange('A18').values=[['Quelle Stammkapital: Gesellschafterliste vom 15.07.2021.']];
c.getRange('A19').values=[['Quelle neue Mittel: Eckpunkte Albrecht Vogl vom 25.09.2026.']];
c.getRange('A20').values=[['Alle 200000 EUR sind für die Gesellschaft vorgesehen. Keine Zahlung ist eingegangen.']];
c.getRange('A21').values=[['Einzahlung, Beschlüsse und Registervollzug sind noch abzustimmen.']];
c.getRange('A22').values=[['Diese Rechnung legt keine Zustimmungs- oder Verkaufsrechte fest.']];
cap.recalculate();assertCell(c,'E9',31250);assertCell(c,'F6',0.48);assertCell(c,'F7',0.32);assertCell(c,'F8',0.2);assertCell(c,'B14',193750);
c.getRange('D8').values=[[12500]];cap.recalculate();assertCell(c,'E9',37500);assertCell(c,'F8',1/3);assertCell(c,'B14',187500);c.getRange('D8').values=[[6250]];cap.recalculate();
const outputs=[[bank,b,'gesellschafterstreit-klageerwiderung-berlin','19_Projektkonto.xlsx','A1:F21'],[cap,c,'gesellschafterstreit-shareholder-agreement-muenchen','18_Beteiligungsrechnung.xlsx','A1:F23']];
for(const [wb,s,slug,file,range] of outputs){
  const check=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!',options:{useRegex:true,maxResults:20}});
  await fs.writeFile(path.join(qa,file+'.errors.ndjson'),check.ndjson);
  for(const row of s.getRange(range).values)for(const v of row)if(typeof v==='string'&&/^#(REF!|DIV\/0!|VALUE!|NAME\?|NUM!)/.test(v))throw new Error(v);
  const preview=await wb.render({sheetName:s.name,range,scale:1.4,format:'png'});
  await fs.writeFile(path.join(qa,file+'.png'),new Uint8Array(await preview.arrayBuffer()));
  const out=path.join(root,slug,file);await fs.mkdir(path.dirname(out),{recursive:true});
  await(await SpreadsheetFile.exportXlsx(wb)).save(out);
  // Excel und der zentrale PDF-Builder sollen dasselbe Querformat verwenden.
  const z=await JSZip.loadAsync(await fs.readFile(out));
  for(const name of Object.keys(z.files).filter(n=>/^xl\/worksheets\/sheet\d+\.xml$/.test(n))){
    let xml=await z.file(name).async('string');const p=xml.match(/<(\w+:)?worksheet\b/)[1]??'';
    xml=xml.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'');
    xml=xml.replace(new RegExp(`</${p}worksheet>`),`<${p}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="1"/></${p}worksheet>`);z.file(name,xml);
  }
  await fs.writeFile(out,await z.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
  try{await fs.rename(out+'.inspect.ndjson',path.join(qa,file+'.inspect.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
  console.log(out);
}

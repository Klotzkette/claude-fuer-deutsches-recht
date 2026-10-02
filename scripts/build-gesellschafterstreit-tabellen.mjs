/** Zwei native Arbeitsmappen der Akte Zink & Zunder.
 * Aufruf: node scripts/build-gesellschafterstreit-tabellen.mjs <Originalordner> <QA-Ordner>
 * AKTEN_NODE_MODULES kann ein vorhandenes node_modules-Verzeichnis angeben.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import { loadWorkbookRuntime } from './akten-workbook-runtime.mjs';
const { Workbook, SpreadsheetFile, requireRuntime } = await loadWorkbookRuntime(['jszip']);
const JSZip = requireRuntime('jszip');
const [outputDir, qaDir] = process.argv.slice(2);
if (!outputDir || !qaDir) throw new Error('Original- und QA-Ordner angeben.');
await fs.mkdir(outputDir,{recursive:true}); await fs.mkdir(qaDir,{recursive:true});
const euro='#,##0.00" ";(#,##0.00)" ";"– "';
const pct='0.0%" ";(0.0%)" ";"– "';
const date=s=>new Date(s+'T00:00:00Z');
const cell=(s,r,c,v)=>s.getCell(r-1,c-1).values=[[v]];
const formula=(s,r,c,v)=>{s.getCell(r-1,c-1).formulas=[[v]];s.getCell(r-1,c-1).format.font.color=v.includes("'!")?'#166534':'#172630';};
const info=[];
function prepare(wb,name,title,subtitle,widths,rows){
 const s=wb.worksheets.add(name);s.showGridLines=false;s.tabColor='#305865';
 const full=s.getRangeByIndexes(0,0,rows,widths.length);
 full.format={font:{name:'Arial',size:10,color:'#172630'},wrapText:true,verticalAlignment:'center',rowHeight:25};
 widths.forEach((w,c)=>s.getRangeByIndexes(0,c,rows,1).format.columnWidth=w);
 const last=String.fromCharCode(64+widths.length);
 s.mergeCells(`A1:${last}1`);cell(s,1,1,title);s.getRange(`A1:${last}1`).format={fill:'#263E49',font:{name:'Arial',size:15,bold:true,color:'#FFFFFF'},rowHeight:35};
 s.mergeCells(`A2:${last}2`);cell(s,2,1,subtitle);s.getRange(`A2:${last}2`).format={rowHeight:36,font:{name:'Arial',size:10,color:'#52636D'}};
 s.freezePanes.freezeRows(4);
 info.push({workbook:wb,sheet:s,name,rows,cols:widths.length});return s;
}
function head(s,row,values){s.getRangeByIndexes(row-1,0,1,values.length).values=[values];s.getRangeByIndexes(row-1,0,1,values.length).format={fill:'#E6EDF0',font:{name:'Arial',size:10,bold:true},rowHeight:32};}
function note(s,row,text,last='F',height=38){s.mergeCells(`A${row}:${last}${row}`);cell(s,row,1,text);s.getRange(`A${row}:${last}${row}`).format={font:{name:'Arial',size:10,color:'#52636D'},rowHeight:height};}
function inputs(s,range,fmt){s.getRange(range).format.font.color='#1D4ED8';if(fmt)s.getRange(range).setNumberFormat(fmt);}
function total(s,row,last='F'){s.getRange(`A${row}:${last}${row}`).format={fill:'#EEF4F1',font:{name:'Arial',size:10,bold:true},borders:{top:{style:'thin',color:'#8A9B9D'}}};}
const finance=Workbook.create();
const bank=prepare(finance,'Bank September','Zink & Zunder | Bankbewegungen','Auszug der Buchhaltung, 30.09.2026 · Konto Werkstatt · Beträge in EUR',[14,18,41,18,18,18],21);
head(bank,4,['Buchung','Beleg','Verwendungszweck','Eingang EUR','Ausgang EUR','Saldo EUR']);
bank.getRange('A5:F5').values=[[date('2026-09-01'),'EB-09','Übertrag aus August',null,null,42000]];
const movements=[['2026-09-02','B-0902','Septembermiete',0,3200],['2026-09-04','B-0904','Altbogen – Teilzahlung',28000,0],['2026-09-07','B-0907','Stahl – Sammelzahlung',0,18500],['2026-09-10','B-0910','Augustlöhne, Sammelauftrag',0,24000],['2026-09-12','B-0912','Treppenhof – Abschlag',19000,0],['2026-09-15','B-0915','Teilrückzahlung Darlehen Knopf',0,30000],['2026-09-18','B-0918','Werkstattreparatur',0,4200],['2026-09-22','B-0922','Hoflicht – Schlusszahlung',27000,0],['2026-09-24','B-0924','Umsatzsteuer',0,7800],['2026-09-25','B-0925','Werkzeugrechnung',0,1300],['2026-09-30','B-0930','Energieabschlag',0,2000]];
bank.getRange('A6:E16').values=movements.map(([d,...r])=>[date(d),...r]);
for(let r=6;r<=16;r++)formula(bank,r,6,`=F${r-1}+D${r}-E${r}`);
cell(bank,18,3,'September gesamt / Schlussbestand');formula(bank,18,4,'=SUM(D6:D16)');formula(bank,18,5,'=SUM(E6:E16)');formula(bank,18,6,'=F16');total(bank,18);
bank.getRange('A5:A16').setNumberFormat('yyyy-mm-dd');bank.getRange('D5:F18').setNumberFormat(euro);inputs(bank,'D6:E16');inputs(bank,'F5');
note(bank,20,'Quelle: Buchungsexport von Gundula Pfennig. Zahlungseingänge sind keine Umsatzaufstellung. Darlehensrückzahlung ist kein Aufwand.');
note(bank,21,'Diese Liste enthält nur die genannten Bankbewegungen. Andere Konten, Kreditlinien, Stundungen und die Fälligkeit einzelner Ansprüche sind nicht bestätigt.');
const op=prepare(finance,'Offene Posten','Zink & Zunder | Noch zu bezahlen','Interne Liste von Gundula Pfennig · Stand 30.09.2026 · kein geprüfter Abschluss',[17,34,19,19,20,18],18);
head(op,4,['Beleg','Gläubiger / Anlass','Fälligkeit','Betrag EUR','Bis Stichtag EUR','Später EUR']);
const debts=[['STA-0821','Stahlkontor Nord','2026-09-20',12000],['MI-08','Augustmiete – Rest','2026-08-05',3200],['STB-0920','Steuerbüro – Honorar','2026-09-27',2800],['EN-0722','Energie – Nachzahlung','2026-09-15',1600],['LO-09','Septemberlöhne – offener Teil','2026-09-30',12000],['BE-0820','Beschläge Sammelrechnung','2026-09-28',18400],['MA-0915','Maschinenlieferung','2026-10-15',25000]];
op.getRange('A5:D11').values=debts.map(([a,b,d,n])=>[a,b,date(d),n]);
cell(op,15,3,'Stichtag');cell(op,15,4,date('2026-09-30'));op.getRange('D15').setNumberFormat('yyyy-mm-dd');inputs(op,'D15');
for(let r=5;r<=11;r++){formula(op,r,5,`=IF(C${r}<=$D$15,D${r},0)`);formula(op,r,6,`=D${r}-E${r}`);}
cell(op,13,2,'Offene Beträge');for(const c of [4,5,6])formula(op,13,c,`=SUM(${String.fromCharCode(64+c)}5:${String.fromCharCode(64+c)}11)`);total(op,13);
op.getRange('C5:C11').setNumberFormat('yyyy-mm-dd');op.getRange('D5:F13').setNumberFormat(euro);inputs(op,'D5:D11');
note(op,17,'Quelle: OP-Liste 30.09.2026. Der Oktober-Maschinenposten wird gesondert gezeigt. Die Bankliste enthält bereits bezahlte Vorgänge.');
note(op,18,'Buchhaltungsvermerk: Über strittige Rechnungen, weitere Mittel oder wirksame Zahlungsaufschübe liegen mir noch keine vollständigen Unterlagen vor.');
const bal=prepare(finance,'Bilanz und Darlehen','Zink & Zunder | Bilanznotiz und Darlehen','Bilanzwerte 31.08.2026, Darlehensbewegungen bis 30.09.2026 · EUR · intern und ungeprüft',[32,19,26,20,19,18],30);
head(bal,4,['Aktiva 31.08.','EUR','Passiva 31.08.','EUR','Quelle','Stand']);
bal.getRange('A5:F12').values=[['Anlagevermögen',90000,'Stammkapital',50000,'BWA/Bilanznotiz','31.08.2026'],['Vorräte',48000,'Verlustvortrag',-18000,'intern','31.08.2026'],['Forderungen',77000,'Laufender Verlust',-25000,'intern','31.08.2026'],['Bank',42000,'Gesellschafterdarlehen',100000,'intern','31.08.2026'],[null,null,'Bankverbindlichkeiten',50000,'intern','31.08.2026'],[null,null,'Lieferanten',70000,'intern','31.08.2026'],[null,null,'Sonstige Verbindlichkeiten',30000,'intern','31.08.2026'],['Summe Aktiva',null,'Summe Passiva',null,null,null]];
formula(bal,12,2,'=SUM(B5:B8)');formula(bal,12,4,'=SUM(D5:D11)');total(bal,12);cell(bal,14,3,'Eigenkapital laut Notiz');formula(bal,14,4,'=SUM(D5:D7)');
head(bal,17,['Darlehensgeber','Zugang EUR','Auszahlung an GmbH','Rückzahlung EUR','Restkapital EUR','Zinssatz p.a.']);
bal.getRange('A18:F19').values=[['Romy Yilmaz',60000,date('2025-01-10'),0,null,0.03],['Kunibert Knopf',40000,date('2026-06-01'),null,null,0.04]];
formula(bal,19,4,"='Bank September'!E11");for(let r=18;r<=19;r++)formula(bal,r,5,`=B${r}-D${r}`);cell(bal,20,1,'Restkapital gesamt');formula(bal,20,5,'=SUM(E18:E19)');total(bal,20);
bal.getRange('B5:B12').setNumberFormat(euro);bal.getRange('D5:D14').setNumberFormat(euro);bal.getRange('B18:B19').setNumberFormat(euro);bal.getRange('D18:E20').setNumberFormat(euro);bal.getRange('C18:C19').setNumberFormat('yyyy-mm-dd');bal.getRange('F18:F19').setNumberFormat(pct);
inputs(bal,'B5:B8');inputs(bal,'D5:D11');inputs(bal,'B18:B19');inputs(bal,'D18');inputs(bal,'F18:F19');
note(bal,22,'Zinsbeleg 30.12.2025: Zahlung an Romy Yilmaz 1.800 EUR. Für 2026 ist keine Zinszahlung erfasst. Abgrenzung und Abrechnung laut Steuerbüro noch zu klären.');
note(bal,24,'30.000 EUR an Kunibert Knopf am 15.09.2026: aus Bank September übernommen. Es handelt sich laut Buchungstext um Kapitalrückzahlung, nicht um Zins oder laufenden Aufwand.');
note(bal,26,'Die August-Bilanznotiz wird nicht auf September fortgeschrieben. Beiratsfreigaben und Unterschriftsunterlagen liegen nur teilweise vor.');
note(bal,28,'Erstellt von Gundula Pfennig, 30.09.2026. Grundlage: internes Hauptbuch und Zahlungsbelege. Keine Aussage zur Berechtigung einzelner Ansprüche.');
const votes=Workbook.create();
const capital=prepare(votes,'Kapitalvorschlag','Zink & Zunder | Kapitalvorschlag','Arbeitsrechnung Kunibert Knopf, 08.09.2026 · Bezugsrecht nur für Knopf beantragt · noch nicht vollzogen',[28,18,18,21,20,20],19);
head(capital,4,['Gesellschafter','Bisher EUR','Bisher %','Neue Einlage EUR','Danach EUR','Danach %']);
capital.getRange('A5:F7').values=[['Kunibert Knopf',20000,null,50000,null,null],['Romy Yilmaz',17500,null,0,null,null],['Thekla Spätzle',12500,null,0,null,null]];
for(let r=5;r<=7;r++){formula(capital,r,3,`=B${r}/$B$8`);formula(capital,r,5,`=B${r}+D${r}`);formula(capital,r,6,`=E${r}/$E$8`);}
cell(capital,8,1,'Summe');for(const c of [2,3,4,5,6])formula(capital,8,c,`=SUM(${String.fromCharCode(64+c)}5:${String.fromCharCode(64+c)}7)`);total(capital,8);
cell(capital,11,1,'Zusätzliches Aufgeld EUR');cell(capital,11,2,30000);cell(capital,12,1,'Geplanter Mittelzufluss EUR');formula(capital,12,2,'=D8+B11');
capital.getRange('B5:B12').setNumberFormat(euro);capital.getRange('D5:E8').setNumberFormat(euro);capital.getRange('C5:C8').setNumberFormat(pct);capital.getRange('F5:F8').setNumberFormat(pct);inputs(capital,'B5:B7');inputs(capital,'D5:D7');inputs(capital,'B11');
note(capital,15,'Knopfs Vorschlag: 50.000 EUR neues Stammkapital und 30.000 EUR Aufgeld. Yilmaz erklärt, dass sie derzeit kein frisches Geld aufbringen könne.');
note(capital,17,'Für alle Abstimmungszettel vom 25.09.2026 werden die bisherigen Anteile verwendet. Die wechselseitigen Einziehungsbeschlüsse sind bestritten.');
note(capital,19,'Notartermin zur Kapitalmaßnahme ist für 09.10.2026 geplant. Bisher keine notarielle Urkunde und keine Registereintragung zu dieser Kapitalerhöhung.');
const raw=prepare(votes,'Stimmzettel','Zink & Zunder | Abstimmungsnotizen','Übertragung der Wortmeldungen durch Thekla Spätzle, 25.09.2026 · Spalte E gibt nur ihre Zählentscheidung wieder',[9,27,18,15,18,42],26);
head(raw,4,['TOP','Abstimmende Person','Nominal EUR','Votum','Gezählt: 1 / 0','Notiz der Leitung']);
const names=['Kunibert Knopf','Romy Yilmaz','Thekla Spätzle'];
const decisions=[['Z1',['Ja','Nein','Ja'],[1,0,1],'Romy wegen fehlender Finanzierung nicht gezählt'],['Z2',['Nein','Ja','Enthaltung'],[1,1,1],'Kunibert trotz Widerspruch von Romy mitgezählt'],['Z3',['Nein','Ja','Ja'],[0,1,1],'Kunibert nicht gezählt; er widerspricht'],['Z4',['Ja','Nein','Nein'],[1,0,1],'Romy nicht gezählt; sie widerspricht'],['Z5',['Ja','Nein','Ja'],[1,0,1],'Romy nicht gezählt; sie widerspricht'],['Z6',['Ja','Nein','Ja'],[1,1,1],'Alle Stimmen gezählt']];
for(let t=0;t<decisions.length;t++){const[top,v,c,n]=decisions[t];for(let j=0;j<3;j++){const r=5+t*3+j;raw.getRange(`A${r}:F${r}`).values=[[top,names[j],null,v[j],c[j],j===0?n:'']];formula(raw,r,3,`='Kapitalvorschlag'!B${5+j}`);raw.getRange(`A${r}:F${r}`).format.rowHeight=22;}}
raw.getRange('C5:C22').setNumberFormat(euro);inputs(raw,'E5:E22');raw.dataValidations.add({range:'E5:E22',rule:{type:'whole',operator:'between',formula1:0,formula2:1}});
note(raw,24,'1 = von der Leiterin gezählt, 0 = von ihr nicht gezählt. Diese Erfassung entscheidet nicht, ob ein Stimmverbot tatsächlich bestand.','F',38);
note(raw,26,'Z7: Nur Auskunftsauftrag zum Darlehensvorgang und Beirat, keine Genehmigung oder Entlastung. Dazu keine Stimmzählung in dieser Datei.','F',38);
const record=prepare(votes,'Protokollrechnung','Zink & Zunder | Rechnung zur Niederschrift','Rechenblatt zur Niederschrift vom 25.09.2026 · die Feststellungen sind streitig',[8,33,15,15,13,24,28],15);
head(record,4,['TOP','Antrag','Ja gezählt EUR','Nein gezählt EUR','Ja / Ja+Nein','Feststellung Thekla','Widerspruch / Vermerk']);
const matters=[['Kapitalerhöhung / Bezugsrechtsausschluss','angenommen','Romy: Stimmrecht und Finanzierung'],['Kunibert als Geschäftsführer abberufen','abgelehnt','Romy: Kunibert sei ausgeschlossen'],['Kuniberts Anteile einziehen','vorläufig angenommen','Kunibert widerspricht'],['Romy als Geschäftsführerin abberufen','vorläufig angenommen','Romy widerspricht'],['Romys Anteile einziehen','vorläufig angenommen','Romy widerspricht'],['Gesamten Anteilsverkauf an Hanna Blech billigen','abgelehnt','75 % laut Satzung verlangt']];
for(let i=0;i<6;i++){const r=5+i;record.getRange(`A${r}:G${r}`).values=[['Z'+(i+1),matters[i][0],null,null,null,matters[i][1],matters[i][2]]];for(const [c,v]of [[3,'Ja'],[4,'Nein']])formula(record,r,c,`=SUMIFS('Stimmzettel'!$C$5:$C$22,'Stimmzettel'!$A$5:$A$22,A${r},'Stimmzettel'!$D$5:$D$22,"${v}",'Stimmzettel'!$E$5:$E$22,1)`);formula(record,r,5,`=IF(C${r}+D${r}=0,0,C${r}/(C${r}+D${r}))`);record.getRange(`A${r}:G${r}`).format.rowHeight=44;}
record.getRange('C5:D10').setNumberFormat(euro);record.getRange('E5:E10').setNumberFormat(pct);
note(record,12,'Die Quote folgt nur der Auswahl in „Stimmzettel“. Enthaltungen sind in dieser Rechenquote nicht enthalten. Beschlussmehrheit und Wirksamkeit sind damit nicht geprüft.','G');
note(record,14,'Z3 bis Z5 wurden nicht vollzogen. Keine neue Gesellschafterliste eingereicht. Kein Ergebnis wird hier automatisch als wirksam oder unwirksam bezeichnet.','G');
// Explizite Ausrichtung und kurze Leerzeilen halten Ausdrucke zusammen.
for (const entry of info) {
 const grid=entry.sheet.getRangeByIndexes(0,0,entry.rows,entry.cols).values;
 for (let r=2;r<grid.length;r++) {
  if(grid[r].every(v=>v===null||v===undefined||v==='')) entry.sheet.getRangeByIndexes(r,0,1,entry.cols).format.rowHeight=8;
  for(let c=0;c<grid[r].length;c++){
   const value=grid[r][c], target=entry.sheet.getCell(r,c);
   if(typeof value==='number') target.format.horizontalAlignment='right';
   else if(typeof value==='string') target.format.horizontalAlignment='left';
  }
 }
}
bal.getRange('A5:F14').format.rowHeight=17;
bal.getRange('A18:F20').format.rowHeight=18;
for(const r of [22,24,26,28]) bal.getRange(`A${r}:F${r}`).format.rowHeight=26;
raw.getRange('A5:F22').format.rowHeight=18;
for(const r of [24,26]) raw.getRange(`A${r}:F${r}`).format.rowHeight=26;
raw.getRange('D5:E22').format.horizontalAlignment='center';
capital.getRange('C5:C8').format.horizontalAlignment='right';
bank.getRange('A5:A16').format.horizontalAlignment='center';
bal.getRange('C18:C19').format.horizontalAlignment='center';
const checks=[];
function check(wb,s,a,expected){const actual=wb.worksheets.getItem(s).getRange(a).values[0][0];if(typeof actual!=='number'||Math.abs(actual-expected)>1e-8)throw new Error(`${s}!${a}: ${actual}, erwartet ${expected}`);checks.push({sheet:s,cell:a,expected,actual});}
for(const w of [finance,votes])w.recalculate();
check(finance,'Bank September','F18',25000);check(finance,'Offene Posten','E13',50000);check(finance,'Offene Posten','F13',25000);check(finance,'Bilanz und Darlehen','E20',70000);check(finance,'Bilanz und Darlehen','D14',7000);check(finance,'Bilanz und Darlehen','B12',257000);check(finance,'Bilanz und Darlehen','D12',257000);
check(votes,'Kapitalvorschlag','F5',0.7);check(votes,'Kapitalvorschlag','F6',0.175);check(votes,'Kapitalvorschlag','B12',80000);check(votes,'Protokollrechnung','E5',1);check(votes,'Protokollrechnung','E6',17500/37500);check(votes,'Protokollrechnung','E8',20000/32500);check(votes,'Protokollrechnung','E10',0.65);
// Eingabeproben einschließlich vollständiger Tilgung und leerer Zählbasis.
bank.getRange('E11').values=[[40000]];finance.recalculate();check(finance,'Bilanz und Darlehen','E19',0);check(finance,'Bank September','F18',15000);bank.getRange('E11').values=[[30000]];
capital.getRange('D5').values=[[0]];votes.recalculate();check(votes,'Kapitalvorschlag','F5',0.4);capital.getRange('D5').values=[[50000]];
raw.getRange('E5:E7').values=[[0]];votes.recalculate();check(votes,'Protokollrechnung','E5',0);raw.getRange('E5:E7').values=[[1],[0],[1]];
for(const wb of [finance,votes])wb.recalculate();
async function printSetup(file){
 const zip=await JSZip.loadAsync(await fs.readFile(file));
 for(const n of Object.keys(zip.files).filter(n=>/^xl\/worksheets\/sheet\d+\.xml$/.test(n))){let xml=await zip.file(n).async('string');const p=xml.match(/<(\w+:)?worksheet\b/)[1]??'';xml=xml.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'').replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,`<${p}pageMargins left="0.3" right="0.3" top="0.35" bottom="0.35" header="0.15" footer="0.15"/>`);xml=xml.replace(new RegExp(`</${p}worksheet>`),`<${p}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="1"/></${p}worksheet>`);zip.file(n,xml);}
 await fs.writeFile(file,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
}
for(const [wb,file]of [[finance,'37_Finanzuebersicht.xlsx'],[votes,'38_Stimmen_und_Kapital.xlsx']]){
 for(const s of info.filter(x=>x.workbook===wb)){
  for(const row of s.sheet.getRangeByIndexes(0,0,s.rows,s.cols).values)for(const v of row)if(typeof v==='string'&&/^#(?:REF!|DIV\/0!|VALUE!|NAME\?|N\/A|NUM!|NULL!|SPILL!|CALC!)/.test(v))throw new Error(`${s.name}: ${v}`);
  const img=await wb.render({sheetName:s.name,range:`A1:${String.fromCharCode(64+s.cols)}${s.rows}`,scale:1.4,format:'png'});await fs.writeFile(path.join(qaDir,s.name.replaceAll(' ','_')+'.png'),new Uint8Array(await img.arrayBuffer()));
 }
 const out=path.join(outputDir,file);await(await SpreadsheetFile.exportXlsx(wb)).save(out);await printSetup(out);
 try{await fs.rename(out+'.inspect.ndjson',path.join(qaDir,file+'.export-inspect.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 const inspected=await wb.inspect({kind:'sheet',include:'id,name',maxChars:3000});await fs.writeFile(path.join(qaDir,file+'.inspect.ndjson'),inspected.ndjson);
 console.log(out);
}
await fs.writeFile(path.join(qaDir,'tabellen-pruefung.json'),JSON.stringify({checks,workbooks:2,worksheets:6,zero_denominator:'0 displayed; no legal conclusion'},null,2)+'\n');

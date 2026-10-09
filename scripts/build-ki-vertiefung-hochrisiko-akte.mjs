/** Erstellt die nachvollziehbare Arbeitsmappe zur Mainblick-Bewerbungsakte. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook,SpreadsheetFile,requireRuntime}=await loadWorkbookRuntime(['jszip']);
const JSZip=requireRuntime('jszip');
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const data=JSON.parse(await fs.readFile(path.join(root,'scripts/data/ki-vertiefung-hochrisiko-akte.json'),'utf8'));
const output=path.join(root,'testakten',data.slug,data.workbook);
const qa=process.argv[2]??'/tmp/mainblick-native-qa';
const report=path.join(root,'quality/ki-verordnung-2026-10-09-vertiefung/hochrisiko-akte-formelpruefung.json');
await fs.mkdir(qa,{recursive:true});
const wb=Workbook.create();
const summary=wb.worksheets.add('Auswertung'),raw=wb.worksheets.add('Export'),control=wb.worksheets.add('Kontrollen');
const checks=[];
function setup(s,cols,last,widths,title){
 s.showGridLines=false;s.freezePanes.freezeRows(5);
 s.getRange(`A1:${cols}${last}`).format={font:{name:'Times New Roman',size:11,color:'#172331'},verticalAlignment:'center',rowHeight:22};
 widths.forEach((w,i)=>s.getRangeByIndexes(0,i,last,1).format.columnWidth=w);
 s.getRange(`A1:${cols}1`).merge();s.getRange('A1').values=[[title]];s.getRange('A1').format={font:{size:16,bold:true},rowHeight:35};
}
function note(s,row,last,text,height=34){s.getRange(`A${row}:${last}${row}`).merge();s.getRange(`A${row}`).values=[[text]];s.getRange(`A${row}`).format={wrapText:true,rowHeight:height,font:{size:10,color:'#425466'}};}
function header(s,row,labels){s.getRangeByIndexes(row-1,0,1,labels.length).values=[labels];s.getRangeByIndexes(row-1,0,1,labels.length).format={fill:'#254F6B',font:{color:'#FFFFFF',bold:true},wrapText:true,rowHeight:34};}
function val(s,cell,v){s.getRange(cell).values=[[v]];}
function formula(s,cell,v){s.getRange(cell).formulas=[[v]];}
function expected(s,cell,want,scenario){wb.recalculate();const got=s.getRange(cell).values[0][0];if(typeof want==='number'?typeof got!=='number'||Math.abs(got-want)>1e-8:got!==want)throw Error(`${scenario}: ${s.name}!${cell}: ${JSON.stringify(got)} != ${JSON.stringify(want)}`);checks.push({sheet:s.name,cell,scenario,expected:want,actual:got});}
setup(raw,'I',35,[12,9,11,15,12,15,14,12,12],'1 Export: Bewerberpool Auftragsbearbeitung Herbst');
note(raw,2,'I','Stand 09.10.2026, 07:15 Uhr. Rang, Punkte und Auswahl beziehen sich auf die Bestätigung am 29.09.2026.');
note(raw,3,'I','Blau: übernommene Eingabewerte. Schwarz: Kontrollformeln. Änderungen sind Arbeitsvarianten; gesicherte Ursprungsdaten bleiben unverändert.');
header(raw,5,['Kennung','Rang','Punkte 0–100','Abschlussort','Shortlist 1/0','Original geöffnet 1/0','Zusatzbefund 1/0','ID-Anzahl','Fehlerfelder']);
raw.getRange('A6:G29').values=data.rows;raw.getRange('A6:G29').format.font.color='#1D4ED8';raw.getRange('A6:I29').format.rowHeight=23;
raw.getRange('B6:C29').setNumberFormat('0');raw.getRange('E6:I29').setNumberFormat('0');
const idFormulas=[],badFormulas=[];
for(let r=6;r<=29;r++){
 idFormulas.push([`=COUNTIF($A$6:$A$29,A${r})`]);
 badFormulas.push([`=IF(AND(ISNUMBER(B${r}),B${r}>=1,B${r}<=24,ISNUMBER(C${r}),C${r}>=0,C${r}<=100,OR(D${r}="DE",D${r}="Ausland"),ISNUMBER(E${r}),OR(E${r}=0,E${r}=1),ISNUMBER(F${r}),OR(F${r}=0,F${r}=1),ISNUMBER(G${r}),OR(G${r}=0,G${r}=1)),0,1)`]);
}
raw.getRange('H6:H29').formulas=idFormulas;raw.getRange('I6:I29').formulas=badFormulas;
raw.getRange('D6:D29').dataValidation={rule:{type:'list',values:['DE','Ausland']}};
for(const c of ['E','F','G'])raw.getRange(`${c}6:${c}29`).dataValidation={rule:{type:'list',values:['0','1']}};
note(raw,31,'I','„Ausland“ bezeichnet nur den Ort des beruflichen Abschlusses; keine Aussage über Staatsangehörigkeit, Herkunft oder Sprache.');
note(raw,32,'I','„Original geöffnet“: mindestens ein Ereignis in MainSort vor Bestätigung. Keine Messung der Lesetiefe; externe Öffnungen fehlen.');
note(raw,33,'I','B07: Zusatzzeugnis im Original vorhanden, nicht in strukturierten Feldern. Punkte sind unberichtigte Anbieterwerte, keine Eigenberechnung.');
note(raw,34,'I','Quelle: Export 0910-0745 und Kontrollnotiz vom 09.10.2026. ID-Anzahl muss 1 sein; Fehlerfelder zählt ungültige Zeilen.');
setup(summary,'E',30,[36,17,17,18,35],'1 Auswertung: Zählwerte und Aussagegrenzen');
note(summary,2,'E','Mainblick Präzisionstechnik GmbH · Alma Heim / Noah Schell · Stand 09.10.2026.');
note(summary,3,'E','Diese Mappe berechnet Zählwerte aus „Export“. Sie berechnet weder Bewerbereignung noch eine rechtliche Einstufung.');
header(summary,5,['Kennzahl / Gruppe','Alle Fälle','Ausgewählt','Anteil Auswahl','Aussage']);
val(summary,'A6','Gesamter aktueller Pool');formula(summary,'B6',"=COUNTA('Export'!A6:A29)");formula(summary,'C6',"=SUM('Export'!E6:E29)");formula(summary,'D6','=IF(B6=0,"n.a.",C6/B6)');val(summary,'E6','Erste Gesprächsrunde');
val(summary,'A7','Abschluss in Deutschland');formula(summary,'B7',"=COUNTIF('Export'!D6:D29,\"DE\")");formula(summary,'C7',"=COUNTIFS('Export'!D6:D29,\"DE\",'Export'!E6:E29,1)");formula(summary,'D7','=IF(B7=0,"n.a.",C7/B7)');val(summary,'E7','Gruppenbezeichnung: DE');
val(summary,'A8','Abschluss außerhalb Deutschlands');formula(summary,'B8',"=COUNTIF('Export'!D6:D29,\"Ausland\")");formula(summary,'C8',"=COUNTIFS('Export'!D6:D29,\"Ausland\",'Export'!E6:E29,1)");formula(summary,'D8','=IF(B8=0,"n.a.",C8/B8)');val(summary,'E8','Keine Herkunftskategorie');
summary.getRange('A6:E8').format={wrapText:true,rowHeight:37};summary.getRange('D6:D8').setNumberFormat('0.0%');
header(summary,10,['Dokumentierte Sichtung','Fälle','Bezugszahl','Anteil','Aussage']);
val(summary,'A11','Original in MainSort geöffnet');formula(summary,'B11',"=SUM('Export'!F6:F29)");formula(summary,'C11','=B6');formula(summary,'D11','=IF(C11=0,"n.a.",B11/C11)');val(summary,'E11','Vor Auswahlbestätigung');
val(summary,'A12','Ohne Öffnungsereignis in MainSort');formula(summary,'B12','=B6-B11');formula(summary,'C12','=B6');formula(summary,'D12','=IF(C12=0,"n.a.",B12/C12)');val(summary,'E12','Keine Aussage über externe Sichtung');summary.getRange('D11:D12').setNumberFormat('0.0%');summary.getRange('A11:E12').format={rowHeight:35,wrapText:true};
header(summary,14,['Abschluss außerhalb Deutschlands','Fälle','Gesamt','Gruppenanteil','Datenstand / Quelle']);
val(summary,'A15','Aktueller Bewerberpool');formula(summary,'B15','=B8');formula(summary,'C15','=B6');formula(summary,'D15','=IF(C15=0,"n.a.",B15/C15)');val(summary,'E15','Export vom 09.10.2026');
val(summary,'A16','Kalibrierungsstichprobe Anbieter');val(summary,'B16',data.controls.calibration_abroad);val(summary,'C16',data.controls.calibration_total);formula(summary,'D16','=IF(C16=0,"n.a.",B16/C16)');val(summary,'E16','Anbieterbrief vom 07.10.2026');summary.getRange('B16:C16').format.font.color='#1D4ED8';summary.getRange('D15:D16').setNumberFormat('0.0%');summary.getRange('A15:E16').format={rowHeight:35,wrapText:true};
val(summary,'A18','Differenz Gruppenanteile in %-Punkten');formula(summary,'D18','=IF(OR(C15=0,C16=0),"n.a.",(D15-D16)*100)');summary.getRange('D18').setNumberFormat('0.0');summary.getRange('A18:C18').merge();summary.getRange('A18:E18').format={fill:'#EAF0F4',font:{bold:true},rowHeight:30};
note(summary,20,'E','1.1 Lesart: 1 bedeutet ein dokumentiertes Ereignis, 0 dessen Fehlen. Null im Zähler ist ein Wert; null im Nenner ergibt „n.a.“.');
note(summary,21,'E','Der aktuelle Gruppenanteil und der Kalibrierungsanteil beschreiben unterschiedliche Fallbestände. Die Kalibrierung ist nicht das gesamte Modelltraining.',38);
note(summary,22,'E','Die Zahlen erklären keinen individuellen Rang. Sie belegen für sich keine Benachteiligung wegen eines bestimmten Merkmals.');
note(summary,23,'E','Eine Öffnung belegt keine unabhängige inhaltliche Prüfung. Fehlende Öffnungsereignisse schließen eine externe Sichtung nicht aus.');
note(summary,24,'E','1.2 Bedienung: Eingaben in „Export“ oder B16:C16 ändern sich durch manuelle Bearbeitung. Die Formeln aktualisieren Summen und Quoten.');
note(summary,25,'E','Das Blatt „Kontrollen“ vergleicht den Arbeitsstand mit dokumentierten Zahlen. Ein abweichender Kontrollwert zeigt eine Änderung oder Lücke.');
note(summary,26,'E','Quellen: Export 0910-0745; Auswahlprotokoll vom 29.09. mit Ergänzung 08.10.; Anbieterbrief 07.10.; Kontrollnotiz 09.10.2026.');
setup(control,'E',23,[39,15,15,15,37],'1 Kontrollen: Vollständigkeit und Arbeitsstand');
note(control,2,'E','Kontrollzahlen stammen aus Exportdialog und Kontrollnotiz. Abweichungen sind zu klären; „OK“ bestätigt nur diese Rechenkontrolle.');
note(control,3,'E','Blau: vorliegende Kontrollzahlen. Schwarz: Formeln. Bei Arbeitsvarianten bleiben die Kontrollzahlen zum Vergleich bestehen.');
header(control,5,['Kontrollgegenstand','Ist','Soll','Differenz','Status']);
const cs=[
 ['Datensätze',"=COUNTA('Export'!A6:A29)",24],
 ['Ausgewählte Personen',"=SUM('Export'!E6:E29)",6],
 ['Originale vor Bestätigung geöffnet',"=SUM('Export'!F6:F29)",8],
 ['Dokumentierte Zusatzbefunde',"=SUM('Export'!G6:G29)",1],
 ['Leere Pflichtfelder im Export',"=COUNTBLANK('Export'!A6:G29)",0],
 ['Kennungen mit mehrfacher Vergabe',"=COUNTIF('Export'!H6:H29,\">1\")",0],
 ['Zeilen mit unzulässigen Werten',"=SUM('Export'!I6:I29)",0],
 ['Summe der beiden Abschlussgruppen',"='Auswertung'!B7+'Auswertung'!B8",24]
];
cs.forEach((x,i)=>{let r=i+6;val(control,`A${r}`,x[0]);formula(control,`B${r}`,x[1]);val(control,`C${r}`,x[2]);formula(control,`D${r}`,`=B${r}-C${r}`);formula(control,`E${r}`,`=IF(D${r}=0,"OK","Prüfen")`);});
control.getRange('C6:C13').format.font.color='#1D4ED8';control.getRange('A6:E13').format={wrapText:true,rowHeight:32};
val(control,'A15','Kalibrierungsangaben plausibel');formula(control,'E15',"=IF(AND(ISNUMBER('Auswertung'!B16),ISNUMBER('Auswertung'!C16),'Auswertung'!C16>0,'Auswertung'!B16>=0,'Auswertung'!B16<='Auswertung'!C16),\"OK\",\"Prüfen\")");control.getRange('A15:D15').merge();
note(control,17,'E','1.1 Grenzen: Die Pflichtfeldkontrolle erkennt Leerzellen. Werteprüfung erfasst Rang 1–24, Punkte 0–100, die zwei Gruppen und binäre Statusfelder.');
note(control,18,'E','Die ID-Kontrolle zählt betroffene Zeilen bei mehrfachen Kennungen. Sie ersetzt keinen Abgleich mit Originalunterlagen.');
note(control,19,'E','1.2 Änderungen: Der Export ist eine Arbeitskopie. Veränderte Kennungen, Statuswerte oder Fallzahlen können eine Differenz erzeugen.');
note(control,20,'E','Die Kalibrierungskontrolle verlangt eine positive Gesamtzahl und einen Gruppenwert zwischen null und der Gesamtzahl.');
note(control,21,'E','Ein rechnerisch konsistenter Export belegt weder die Richtigkeit der Punktwerte noch eine wirksame menschliche Prüfung.');
// Kompakte Zeilen halten die Druckfassung jedes Blatts zusammen.
for(const r of [4,9,13,17,19])summary.getRange(`A${r}:E${r}`).format.rowHeight=8;
for(const r of [2,3])summary.getRange(`A${r}:E${r}`).format.rowHeight=24;
for(const r of [5,10,14])summary.getRange(`A${r}:E${r}`).format.rowHeight=24;
for(const r of [6,7,8,11,12,15,16])summary.getRange(`A${r}:E${r}`).format.rowHeight=24;
summary.getRange('A20:E26').format.rowHeight=20;
for(const r of [2,3])raw.getRange(`A${r}:I${r}`).format.rowHeight=24;
for(const r of [4,30])raw.getRange(`A${r}:I${r}`).format.rowHeight=8;
raw.getRange('A6:I29').format.rowHeight=16;raw.getRange('A31:I34').format.rowHeight=22;
for(const r of [2,3])control.getRange(`A${r}:E${r}`).format.rowHeight=24;
for(const r of [4,14,16])control.getRange(`A${r}:E${r}`).format.rowHeight=8;
control.getRange('A5:E13').format.rowHeight=24;control.getRange('A17:E21').format.rowHeight=22;
expected(summary,'B6',24,'Ausgang: Datensätze');expected(summary,'C6',6,'Ausgang: Shortlist');expected(summary,'D6',.25,'Ausgang: Auswahlanteil');expected(summary,'B8',6,'Ausgang: Ausland');expected(summary,'C8',0,'Ausgang: Ausland ausgewählt');expected(summary,'D7',1/3,'Ausgang: DE-Auswahlanteil');expected(summary,'B11',8,'Ausgang: Öffnungen');expected(summary,'D15',.25,'Ausgang: aktueller Gruppenanteil');expected(summary,'D16',.05,'Ausgang: Kalibrierungsanteil');expected(summary,'D18',20,'Ausgang: Differenz Prozentpunkte');
for(let r=6;r<=13;r++)expected(control,`E${r}`,'OK','Ausgang: Kontrollstatus');expected(control,'E15','OK','Ausgang: Kalibrierung');
// Reale Änderungen der Eingabefelder mit Wiederherstellung vor Export.
val(raw,'E12',1);expected(summary,'C8',1,'Änderung B07 in Shortlist');expected(summary,'C6',7,'Änderung B07 Gesamt');expected(summary,'D8',1/6,'Änderung B07 Gruppenquote');expected(control,'E7','Prüfen','Änderung Auswahlkontrolle');val(raw,'E12',0);
val(summary,'C16',0);expected(summary,'D16','n.a.','Null: Kalibrierungsnenner');expected(summary,'D18','n.a.','Null: Differenz ohne Nenner');expected(control,'E15','Prüfen','Null: Kalibrierungskontrolle');val(summary,'C16',120);
val(summary,'B16',0);expected(summary,'D16',0,'Null: Kalibrierungszähler');expected(summary,'D18',25,'Null: Differenz bei Nullzähler');val(summary,'B16',6);
val(raw,'D12',null);expected(control,'B10',1,'Leerwert: Gruppenfeld');expected(control,'E10','Prüfen','Leerwert: Pflichtfeldkontrolle');expected(control,'E13','Prüfen','Leerwert: Gruppenabgleich');val(raw,'D12','Ausland');
val(raw,'A12','B06');expected(control,'B11',2,'Änderung: doppelte Kennung');val(raw,'A12','B07');
val(raw,'F6',2);expected(control,'B12',1,'Änderung: unzulässiger Status');val(raw,'F6',1);
const originals=raw.getRange('D6:D29').values;raw.getRange('D6:D29').values=Array.from({length:24},()=>['DE']);expected(summary,'D8','n.a.','Null: leere Abschlussgruppe');raw.getRange('D6:D29').values=originals;
expected(summary,'D18',20,'Wiederhergestellt: Differenz');expected(summary,'C6',6,'Wiederhergestellt: Shortlist');expected(control,'B10',0,'Wiederhergestellt: vollständig');for(let r=6;r<=13;r++)expected(control,`E${r}`,'OK','Wiederhergestellt: Kontrollstatus');
wb.recalculate();
const ranges=[[summary,'A1:E26'],[raw,'A1:I34'],[control,'A1:E21']];
for(const [s,range] of ranges){
 for(const row of s.getRange(range).values)for(const v of row)if(typeof v==='string'&&/^#(?:REF!|VALUE!|DIV\/0!|NAME\?|NUM!|N\/A|SPILL!)/.test(v))throw Error(`Formelfehler ${s.name}: ${v}`);
 const result=await wb.inspect({kind:'table',range:`'${s.name}'!${range}`,include:'values,formulas',tableMaxRows:40,tableMaxCols:9,maxChars:28000});await fs.writeFile(path.join(qa,s.name+'.ndjson'),result.ndjson);
 const rendered=await wb.render({sheetName:s.name,range,scale:1.2,format:'png'});await fs.writeFile(path.join(qa,s.name+'.png'),new Uint8Array(await rendered.arrayBuffer()));
}
await(await SpreadsheetFile.exportXlsx(wb)).save(output);
// Nur Druckmetadaten ergänzen; Zellinhalt, Formeln und Formatierung stammen aus artifact-tool.
const zip=await JSZip.loadAsync(await fs.readFile(output));
for(const name of Object.keys(zip.files).filter(n=>/^xl\/worksheets\/sheet\d+\.xml$/.test(n))){let xml=await zip.file(name).async('string');const p=xml.match(/<(\w+:)?worksheet\b/)[1]??'';xml=xml.replace(new RegExp(`(<${p}worksheet[^>]*>)`),`$1<${p}sheetPr><${p}pageSetUpPr fitToPage="1"/></${p}sheetPr>`);xml=xml.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'').replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,'');xml=xml.replace(`</${p}worksheet>`,`<${p}pageMargins left="0.3" right="0.3" top="0.35" bottom="0.35" header="0.15" footer="0.15"/><${p}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="1"/></${p}worksheet>`);zip.file(name,xml);}
let wx=await zip.file('xl/workbook.xml').async('string');const p=wx.match(/<(\w+:)?workbook\b/)[1]??'';const defs=ranges.map(([s,r],i)=>`<${p}definedName name="_xlnm.Print_Area" localSheetId="${i}">'${s.name}'!${r.replace(/([A-Z]+)(\d+)/g,'$$$1$$$2')}</${p}definedName>`).join('');
if(wx.includes(`</${p}definedNames>`))wx=wx.replace(`</${p}definedNames>`,defs+`</${p}definedNames>`);else wx=wx.replace(`</${p}workbook>`,`<${p}definedNames>${defs}</${p}definedNames></${p}workbook>`);zip.file('xl/workbook.xml',wx);await fs.writeFile(output,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
try{await fs.rename(output+'.inspect.ndjson',path.join(qa,'export.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
await fs.writeFile(report,JSON.stringify({workbook:`testakten/${data.slug}/${data.workbook}`,checks,formulaErrors:0,restored:true},null,2)+'\n');console.log(JSON.stringify({output,checks:checks.length}));

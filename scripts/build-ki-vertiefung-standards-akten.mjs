/** Zwei native Tabellen; Eingaben und berechnete Beobachtungswerte. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook,SpreadsheetFile,requireRuntime}=await loadWorkbookRuntime(['jszip']);
const JSZip=requireRuntime('jszip');
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const cases=JSON.parse(await fs.readFile(path.join(root,'scripts/data/ki-vertiefung-standards-akten.json'),'utf8'));
const qa=process.env.STANDARDS_AKTEN_QA??'/tmp/ki-standards-akten-qa';await fs.mkdir(qa,{recursive:true});
const results=[];
function setup(wb,name,title){
 const s=wb.worksheets.add(name);s.showGridLines=false;
 s.getRange('A1:F24').format={font:{name:'Arial',size:11,color:'#172331'},verticalAlignment:'center',rowHeight:23};
 [39,19,19,22,21,24].forEach((w,i)=>s.getRangeByIndexes(0,i,24,1).format.columnWidth=w);
 s.getRange('A2').values=[[title]];s.getRange('A2').format={font:{size:15,bold:true},rowHeight:31};
 note(s,3,'Aktenstand 09.10.2026. Blaue Werte sind Eingaben; schwarze Werte sind Formeln.');
 return s;
}
function note(s,row,value){s.getRange(`A${row}:F${row}`).merge();s.getRange(`A${row}`).values=[[value]];s.getRange(`A${row}`).format={font:{size:10,color:'#465460'},wrapText:true,rowHeight:29};}
function header(s,row,labels){s.getRangeByIndexes(row-1,0,1,6).values=[labels];s.getRangeByIndexes(row-1,0,1,6).format={fill:'#274C68',font:{color:'#FFFFFF',bold:true},wrapText:true,rowHeight:36,horizontalAlignment:'center'};}
function section(s,row,text){s.getRange(`A${row}:F${row}`).merge();s.getRange(`A${row}`).values=[[text]];s.getRange(`A${row}:F${row}`).format={fill:'#E9EEF2',font:{bold:true},rowHeight:27};}
function record(s,range,values){s.getRange(range).values=values;s.getRange(range).format={rowHeight:36,wrapText:true};}
function input(s,range){s.getRange(range).format.font.color='#1D4ED8';}
function test(wb,s,cell,expected,label){wb.recalculate();const got=s.getRange(cell).values[0][0];if(typeof expected==='number'?(typeof got!=='number'||Math.abs(got-expected)>1e-8):got!==expected)throw new Error(`${label} ${s.name}!${cell}: ${got} != ${expected}`);results.push({label,sheet:s.name,cell,expected,actual:got});}
for(const c of cases){
 const havel=c.slug.includes('havelgrund'),wb=Workbook.create();
 const t=setup(wb,'Testwerte',havel?'Fallspur Testzählungen':'Eichengrund Testumfang');
 const b=setup(wb,'Aufwand',havel?'Fallspur Angebotsrechnung':'Eichengrund Angebotsrechnung');
 const n=setup(wb,havel?'Planspiel':'Nachweise',havel?'Zukünftiges Bereitschaftsplanspiel':'Dokumente und offene Nachweise');
 if(havel){
  header(t,5,['Testgruppe','Fälle','Abweichungen','Original geöffnet','Abweichungsanteil','Sichtungsanteil']);
  record(t,'A6:D8',c.rows);input(t,'B6:D8');
  t.getRange('E6:E8').formulas=c.rows.map((_,i)=>[`=IF(COUNT(B${i+6})=0,"offen",IF(B${i+6}=0,"nicht geprüft",C${i+6}/B${i+6}))`]);
  t.getRange('F6:F8').formulas=c.rows.map((_,i)=>[`=IF(COUNT(B${i+6})=0,"offen",IF(B${i+6}=0,"nicht geprüft",D${i+6}/B${i+6}))`]);
  section(t,10,'Zählwerte des tatsächlich vorliegenden Testsatzes');
  t.getRange('A11:D11').values=[['Summe Fälle',null,'Summe Abweichungen',null]];
  t.getRange('B11').formulas=[['=SUM(B6:B8)']];t.getRange('D11').formulas=[['=SUM(C6:C8)']];
  t.getRange('A12').values=[['Originalfenster insgesamt']];t.getRange('B12').formulas=[['=SUM(D6:D8)']];
  t.getRange('C12').values=[['Nur Kurzansicht']];t.getRange('D12').formulas=[['=B11-B12']];
  t.getRange('A13').values=[['Kontrolle Sichtung höchstens Fälle']];t.getRange('D13').formulas=[['=IF(B12<=B11,"plausibel","Zählung prüfen")']];
  test(wb,t,'E6',5/12,c.slug+' Basisquote');test(wb,t,'B11',80,c.slug+' Fallzahl');test(wb,t,'D12',23,c.slug+' Kurzansichten');
  t.getRange('B6').values=[[0]];test(wb,t,'E6','nicht geprüft',c.slug+' Nullgruppe');
  t.getRange('B6').values=[[null]];test(wb,t,'E6','offen',c.slug+' fehlende Fallzahl');t.getRange('B6').values=[[12]];
  t.getRange('C6').values=[[6]];test(wb,t,'E6',0.5,c.slug+' geänderter Befund');test(wb,t,'D11',10,c.slug+' Gesamtsumme reagiert');t.getRange('C6').values=[[5]];
 }else{
  header(t,5,['Testgruppe','Planfälle','Ausgeführt','Abweichungen','Planabdeckung','Abweichungsanteil']);
  record(t,'A6:D10',c.rows);input(t,'B6:D10');
  t.getRange('E6:E10').formulas=c.rows.map((_,i)=>[`=IF(COUNT(B${i+6})=0,"offen",IF(B${i+6}=0,"kein Plan",C${i+6}/B${i+6}))`]);
  t.getRange('F6:F10').formulas=c.rows.map((_,i)=>[`=IF(COUNT(C${i+6})=0,"offen",IF(C${i+6}=0,"nicht geprüft",D${i+6}/C${i+6}))`]);
  section(t,12,'Umfangskontrolle ohne rechtliche Gesamtbewertung');
  t.getRange('A13').values=[['Planfälle insgesamt']];t.getRange('B13').formulas=[['=SUM(B6:B10)']];
  t.getRange('C13').values=[['Ausgeführt insgesamt']];t.getRange('D13').formulas=[['=SUM(C6:C10)']];
  t.getRange('A14').values=[['Noch nicht ausgeführt']];t.getRange('B14').formulas=[['=B13-D13']];
  t.getRange('C14').values=[['Kontrolle Umfang']];t.getRange('D14').formulas=[['=IF(D13<=B13,"plausibel","Plan prüfen")']];
  test(wb,t,'F6',8/120,c.slug+' Dispositionsquote');test(wb,t,'F9',3/75,c.slug+' S1 Quote');test(wb,t,'B14',85,c.slug+' Fehlende Testfälle');
  test(wb,t,'F7','nicht geprüft',c.slug+' Ungeprüfte Nachtgruppe');
  t.getRange('C6').values=[[null]];test(wb,t,'F6','offen',c.slug+' fehlende Testzahl');t.getRange('C6').values=[[120]];
  t.getRange('D9').values=[[6]];test(wb,t,'F9',0.08,c.slug+' geänderter S1 Befund');t.getRange('D9').values=[[3]];
 }
 t.getRange('E6:F10').setNumberFormat('0.0%');
 c.notes.forEach((v,i)=>note(t,17+i,v));note(t,20,'Prüfwerte kontrollieren Zählung und Umfang. Sie bescheinigen keine rechtliche oder technische Freigabe.');
 header(b,5,['Position','Anzahl','Preis netto EUR','Perioden','Summe netto EUR','Art']);
 record(b,'A6:F8',c.budget.map((r,i)=>[...r,null,i===0?'monatlich':'einmalig']));input(b,'B6:D8');
 b.getRange('E6:E8').formulas=c.budget.map((_,i)=>[`=ROUND(B${i+6}*C${i+6}*D${i+6},2)`]);
 b.getRange('A10').values=[['Netto gesamt']];b.getRange('E10').formulas=[['=SUM(E6:E8)']];
 b.getRange('A11').values=[['Umsatzsteuer']];b.getRange('C11').values=[[0.19]];input(b,'C11');b.getRange('C11').setNumberFormat('0%');b.getRange('E11').formulas=[['=ROUND(E10*C11,2)']];
 b.getRange('A12').values=[['Brutto gesamt']];b.getRange('E12').formulas=[['=E10+E11']];
 b.getRange('A14').values=[['Prüfwert Netto laut Mail']];b.getRange('C14').values=[[havel?6160:8460]];input(b,'C14');b.getRange('E14').formulas=[['=E10-C14']];b.getRange('F14').values=[['Differenz EUR']];
 b.getRange('C6:C8').setNumberFormat('#,##0.00');b.getRange('C14').setNumberFormat('#,##0.00');b.getRange('E6:E14').setNumberFormat('#,##0.00');
 note(b,17,havel?'Quelle: E-Mail 11 vom 08.10.2026. Planangebot, keine Bestellung und keine fällige Rechnung.':'Quelle: E-Mail 09 vom 06.10.2026. Planangebot, keine Bestellung und keine fällige Rechnung.');
 note(b,18,'Monatliche Positionen: Anzahl mal Monatspreis mal Monate. Einmalige Positionen haben eine Periode.');
 note(b,19,'Der unveränderte Prüfwert ist die Angebotssumme aus der Quelle; eine Eingabeänderung zeigt eine Abweichung.');
 note(b,20,'Die Rechnung setzt keine gesetzlichen Fristen und entscheidet nicht über den Einsatz einer Anwendung.');
 test(wb,b,'E10',havel?6160:8460,c.slug+' Nettosumme');test(wb,b,'E12',havel?7330.4:10067.4,c.slug+' Bruttosumme');test(wb,b,'E14',0,c.slug+' Quellenabgleich');
 b.getRange('B6').values=[[0]];test(wb,b,'E10',havel?3100:6300,c.slug+' Null monatliche Menge');b.getRange('B6').values=[[c.budget[0][1]]];
 b.getRange('D6').values=[[4]];test(wb,b,'E14',havel?1020:720,c.slug+' Periodenaenderung');b.getRange('D6').values=[[3]];
 if(havel){
  note(n,4,'Ausschließlich angenommene Ereignisse vom 21. und 22.02.2028; am Aktenstand nicht geschehen.');
  header(n,6,['Szenarioereignis','Rohstunden ab Tag 1','Zeitbasis laut Entwurf','Abstand zum Vorwert h','Kenntnisinhalt','Belegstatus']);
  record(n,'A7:F10',c.scenario.map((r,i)=>[r[0],r[1],r[2],null,['Verzögerung berichtet','Prioritätswert erwähnt','Zusammenhang wahrscheinlich','Ticket vollständig'][i],'Szenarioannahme']));input(n,'B7:C10');
  n.getRange('D8:D10').formulas=[['=B8-B7'],['=B9-B8'],['=B10-B9']];n.getRange('B7:B10').setNumberFormat('0.000');n.getRange('D8:D10').setNumberFormat('0.000');
  test(wb,n,'D10',18+25/60,c.slug+' Rohzeitdifferenz');n.getRange('B10').values=[[33.75]];test(wb,n,'D10',19+25/60,c.slug+' geaenderter Szenariozeitpunkt');n.getRange('B10').values=[[32.75]];
  note(n,13,'Rohzeiten sind noch nicht auf eine gemeinsame Zeitzone gebracht. Die Differenz ist kein Fristbeginn.');
  note(n,14,'09:10, 10:35 und 14:20 stehen im Ortszeitentwurf; 08:45 am Folgetag im Journal ist als UTC bezeichnet.');
  note(n,16,'Quelle: Dokument 05, ausdrücklich zukünftige Bereitschaftsvariante. Kenntnisumfang und Folgen bleiben offen.');
  note(n,17,'Das Blatt berechnet keine gesetzlichen Höchstfristen, meldet keinen Vorfall und behauptet keinen Eingang.');
 }else{
  header(n,5,['Dokument','Organisation','Systembezug','Vorhanden 1 oder 0','Offene Angabe','Quelle']);
  record(n,'A6:F10',[
   ['AIMS-Abschrift','Holding Services GmbH','Beratung im Konzern',1,'Original und Anlagen','Dokument 05 Abschnitt 1'],
   ['Normenfolie S1','Eichenrobotik','Wächterkern S1',1,'Ausgabe und Anwendung','Dokument 05 Abschnitt 2'],
   ['Nachtbericht Disposition','Taktweg Systeme','Disposition 2.4',0,'Testdaten fehlen','Dokument 02 Abschnitt 1'],
   ['Nachtbericht S1','Eichenrobotik','S1 mit neuem Sensor',0,'Läufe fehlen','Dokument 02 Abschnitt 3'],
   ['Ursachenbericht S1','Eichenrobotik','Drei Freigaben',0,'Ursachenklärung','Dokument 05 Abschnitt 3']
  ]);input(n,'D6:D10');
  n.getRange('A12').values=[['Vorhandene Dokumente']];n.getRange('D12').formulas=[['=SUM(D6:D10)']];
  n.getRange('A13').values=[['Noch offene Dokumente']];n.getRange('D13').formulas=[['=ROWS(D6:D10)-SUM(D6:D10)']];
  test(wb,n,'D13',3,c.slug+' Fehlende Dokumente');n.getRange('D8').values=[[1]];test(wb,n,'D13',2,c.slug+' nachgereichter Bericht');n.getRange('D8').values=[[0]];
  note(n,16,'Vorhanden bedeutet nur in der Mappe erfasst. Es bedeutet weder geprüft noch geeignet oder gesetzlich erforderlich.');
  note(n,17,'Zählwerte entscheiden weder Rollen noch Konformitätsverfahren. Angaben zum Inhalt bleiben einzeln zu prüfen.');
  note(n,18,'Quelle: Kontrollblatt vom 08.10.2026. Ausgaben und Amtsblattbelege sind ausdrücklich noch offen.');
 }
 // Zentrierte Zahlen halten Abstand zu den folgenden Beschreibungsspalten.
 t.getRange('B6:F14').format.horizontalAlignment='center';
 b.getRange('B6:E14').format.horizontalAlignment='center';
 n.getRange(havel?'B7:D10':'D6:D13').format.horizontalAlignment='center';
 wb.recalculate();
 for(const s of [t,b,n]){
  for(const row of s.getRange('A1:F20').values)for(const v of row)if(typeof v==='string'&&/^#(?:REF!|DIV\/0!|VALUE!|NAME\?|NUM!|N\/A)/.test(v))throw new Error(s.name+': '+v);
  const check=await wb.inspect({kind:'table',range:`'${s.name}'!A1:F20`,include:'values,formulas',tableMaxRows:24,tableMaxCols:6,maxChars:15000});await fs.writeFile(path.join(qa,c.slug+'-'+s.name+'.ndjson'),check.ndjson);
  const image=await wb.render({sheetName:s.name,range:'A1:F20',scale:1.2,format:'png'});await fs.writeFile(path.join(qa,c.slug+'-'+s.name+'.png'),new Uint8Array(await image.arrayBuffer()));
 }
 const out=path.join(root,'testakten',c.slug,c.xlsx);await(await SpreadsheetFile.exportXlsx(wb)).save(out);
 // Ergänzt ausschließlich Druckmetadaten, für die die dokumentierte API kein Verfahren anbietet.
 const z=await JSZip.loadAsync(await fs.readFile(out));
 for(const name of Object.keys(z.files).filter(v=>/^xl\/worksheets\/sheet\d+\.xml$/.test(v))){
  let xml=await z.file(name).async('string');const prefix=xml.match(/<(\w+:)?worksheet\b/)[1]??'';
  xml=xml.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'').replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,'');
  xml=xml.replace(`</${prefix}worksheet>`,`<${prefix}pageMargins left="0.3" right="0.3" top="0.35" bottom="0.35" header="0.15" footer="0.15"/><${prefix}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="1"/></${prefix}worksheet>`);z.file(name,xml);
 }
 let xml=await z.file('xl/workbook.xml').async('string');const prefix=xml.match(/<(\w+:)?workbook\b/)[1]??'';
 const defs=[t,b,n].map((s,i)=>`<${prefix}definedName name="_xlnm.Print_Area" localSheetId="${i}">'${s.name}'!$A$1:$F$20</${prefix}definedName>`).join('');
 if(xml.includes(`</${prefix}definedNames>`))xml=xml.replace(`</${prefix}definedNames>`,defs+`</${prefix}definedNames>`);else xml=xml.replace(`</${prefix}workbook>`,`<${prefix}definedNames>${defs}</${prefix}definedNames></${prefix}workbook>`);
 z.file('xl/workbook.xml',xml);await fs.writeFile(out,await z.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
 try{await fs.rename(out+'.inspect.ndjson',path.join(qa,c.slug+'-export.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 console.log(out);
}
await fs.mkdir(path.join(root,'quality/ki-verordnung-2026-10-09-vertiefung'),{recursive:true});
await fs.writeFile(path.join(root,'quality/ki-verordnung-2026-10-09-vertiefung/standards-akten-formeln.json'),JSON.stringify(results,null,2)+'\n');

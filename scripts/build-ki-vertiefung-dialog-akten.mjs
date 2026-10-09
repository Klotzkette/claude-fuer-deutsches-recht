/** Zwei native Arbeitsmappen zu Aktenständen vom 9. Oktober 2026. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook,SpreadsheetFile,requireRuntime}=await loadWorkbookRuntime(['jszip']);
const JSZip=requireRuntime('jszip');
const root=path.resolve(process.argv[2]??'.');
const qa=path.resolve(process.argv[3]??'/tmp/ki-dialog-akten-qa/sheets');
await fs.mkdir(qa,{recursive:true});
const cases=JSON.parse(await fs.readFile(path.join(root,'scripts/data/ki-vertiefung-dialog-akten.json'),'utf8'));
const checks=[];
function val(s,a,v){s.getRange(a).values=[[v]];}
function formula(s,a,f){s.getRange(a).formulas=[[f]];s.getRange(a).format.font.color='#111111';}
function base(wb,name,title,widths,rows=29){
 const s=wb.worksheets.add(name);s.showGridLines=false;
 const end=String.fromCharCode(64+widths.length);
 s.getRange(`A1:${end}${rows}`).format={font:{name:'Arial',size:10,color:'#222222'},rowHeight:22,verticalAlignment:'center'};
 widths.forEach((w,i)=>s.getRangeByIndexes(0,i,rows,1).format.columnWidth=w);
 val(s,'A2',title);s.getRange('A2').format={font:{size:14,bold:true},rowHeight:30};
 val(s,'A3','Stand 09.10.2026. Blaue Werte sind Eingaben; schwarze Werte werden berechnet.');
 s.getRange('A3').format.font.color='#555555';
 return s;
}
function header(s,row,labels){const end=String.fromCharCode(64+labels.length);s.getRange(`A${row}:${end}${row}`).values=[labels];s.getRange(`A${row}:${end}${row}`).format={fill:'#274760',font:{color:'#FFFFFF',bold:true},rowHeight:30,wrapText:true,horizontalAlignment:'center'};}
function note(s,row,text){val(s,`A${row}`,text);s.getRange(`A${row}`).format.font.color='#555555';}
function expect(wb,s,cell,want,label){wb.recalculate();const got=s.getRange(cell).values[0][0];if(typeof want==='number'?typeof got!=='number'||Math.abs(got-want)>1e-8:got!==want)throw Error(`${label}: ${cell}: ${got} != ${want}`);checks.push({label,sheet:s.name,cell,expected:want,actual:got});}
const eur='#,##0.00;(#,##0.00);"-"';
for(const c of cases){
 const wb=Workbook.create();let ranges;
 if(c.workbook.kind==='abo'){
  const out=base(wb,'Kosten','SorglosPlus Kosten und belegte Zahlungen',[45,21,21,29]);
  const inp=base(wb,'Eingaben','Tarifangaben und offene Zusatzoption',[37,19,18,41]);
  const bank=base(wb,'Buchungen','Bankumsätze und unabhängiger Summenabgleich',[22,23,23,42]);
  header(inp,5,['Angabe','Wert','Einheit','Quelle oder Einschränkung']);
  inp.getRange('A6:D13').values=[['Grundrate',39,'EUR / Monat','01_Pruefauftrag Abschnitt 2'],['Grundlaufzeit',18,'Monate','01_Pruefauftrag Abschnitt 2'],['Einrichtung',89,'EUR einmalig','01_Pruefauftrag Abschnitt 2'],['Zusatzrate',7,'EUR / Monat','01_Pruefauftrag Abschnitt 2'],['Zusatzmonate',null,'Monate','Bestellnachweis fehlt'],['Journalgutschrift',39,'EUR','10_Gutschrift_Buchhaltung.eml'],['Rente laut Kundin',1118,'EUR / Monat','03_Gespraechsprotokoll'],['Warmmiete laut Kundin',642,'EUR / Monat','03_Gespraechsprotokoll']];
  inp.getRange('B6:B13').format.font.color='#1D4ED8';inp.getRange('B10').format.fill='#FFF0C2';inp.getRange('D6:D13').format.wrapText=true;inp.getRange('A6:D13').format.rowHeight=36;
  inp.getRange('B6:B13').setNumberFormat(eur);inp.getRange('B7').setNumberFormat('0');inp.getRange('B10').setNumberFormat('0');
  inp.getRange('B10').dataValidation={rule:{type:'whole',operator:'between',formula1:0,formula2:18}};
  note(inp,16,'Zusatzmonate bleiben leer, solange der tatsächliche Bestellumfang ungeklärt ist.');
  note(inp,17,'Eine Eingabe 0 wäre eine Rechenannahme; sie ist derzeit nicht als Tatsache belegt.');
  note(inp,19,'Rente und Miete sind Angaben der Kundin. Andere notwendige Ausgaben fehlen.');
  note(inp,20,'Die Journalgutschrift ist weder Bankeingang noch belegte Änderung des Gesamtpreises.');
  header(bank,5,['Buchungsmonat','Belastung EUR','Erstattung EUR','Quelle']);
  bank.getRange('A6:D7').values=[['September 2026',128,0,'Umsatzzeile September'],['Oktober 2026',46,0,'Umsatzzeile Oktober']];
  bank.getRange('B6:C7').setNumberFormat(eur);bank.getRange('B6:C7').format.font.color='#1D4ED8';
  val(bank,'A10','Banknetto');formula(bank,'D10','=IF(COUNT(B6:C7)=4,SUM(B6:B7)-SUM(C6:C7),"offen")');
  val(bank,'A13','Kontrollsumme Kundin');val(bank,'D13',174);bank.getRange('D13').format.font.color='#1D4ED8';
  val(bank,'A14','Abweichung zum Netto');formula(bank,'D14','=IF(COUNT(D10,D13)=2,D10-D13,"offen")');bank.getRange('D10:D14').setNumberFormat(eur);
  note(bank,17,'Quelle der Beträge und Kontrollsumme: 05_Kontrollnotiz_Betrieb, Abschnitt 3.');
  note(bank,18,'Null Erstattung bedeutet: In den zwei vorliegenden Umsatzzeilen ist keine enthalten.');
  note(bank,19,'Weitere Kontoumsätze sind nicht Teil dieses Auszugs; keine vollständige Kontoabstimmung.');
  note(bank,21,'Der Kontrollbereich beobachtet die Zahlen. Keine andere Berechnung hängt davon ab.');
  header(out,5,['Rechnung','Tarif oder Annahme','Einheit','Ergebnis']);
  const labels={6:'Grundentgelt nach Eingaben',7:'Belegte Bankbelastung netto',8:'Grundentgelt abzüglich Banknetto',10:'Zusatzentgelt bei eingegebenen Monaten',11:'Entgelt einschließlich Zusatzannahme',13:'Gutschrift im Journal',15:'Rente abzüglich Warmmiete',16:'Grundrate / Betrag aus Zeile 15'};
  for(const [r,l] of Object.entries(labels))val(out,`A${r}`,l);
  for(const [r,t] of Object.entries({6:'Laufzeit und Einrichtung',7:'2 Umsatzzeilen',8:'ohne Zusatzannahme',10:'Monate laut Eingaben',11:'nach Eingabe der Monate',13:'Auszahlung offen',15:'Angaben der Kundin',16:'Grundrate aus Eingaben'})){val(out,`B${r}`,t);val(out,`C${r}`,r==='16'?'Anteil':'EUR');}
  formula(out,'D6','=IF(COUNT(Eingaben!B6:B8)=3,Eingaben!B6*Eingaben!B7+Eingaben!B8,"offen")');
  formula(out,'D7',"='Buchungen'!D10");formula(out,'D8','=IF(COUNT(D6:D7)=2,D6-D7,"offen")');
  formula(out,'D10','=IF(COUNT(Eingaben!B9:B10)=2,Eingaben!B9*Eingaben!B10,"offen")');
  formula(out,'D11','=IF(COUNT(D6,D10)=2,D6+D10,"offen")');formula(out,'D13','=IF(ISNUMBER(Eingaben!B11),Eingaben!B11,"offen")');
  formula(out,'D15','=IF(COUNT(Eingaben!B12:B13)=2,Eingaben!B12-Eingaben!B13,"offen")');
  formula(out,'D16','=IF(COUNT(D15,Eingaben!B6)=2,IF(D15=0,"n.a.",Eingaben!B6/D15),"offen")');
  out.getRange('D6:D15').setNumberFormat(eur);out.getRange('D16').setNumberFormat('0.0%');out.getRange('A6:B16').format.wrapText=true;out.getRange('A6:D16').format.rowHeight=36;
  note(out,19,'Zeile 8 ist eine Rechengröße, keine Feststellung einer wirksamen Restforderung.');
  note(out,20,'Die Journalgutschrift wird nicht zusätzlich von Banknetto oder Grundentgelt abgezogen.');
  note(out,22,'Zeile 15 ist kein frei verfügbares Einkommen. Weitere Lebenshaltungskosten fehlen.');
  note(out,23,'Ein Kostenanteil allein belegt weder Ursache noch Erheblichkeit eines Schadens.');
  expect(wb,out,'D6',791,c.slug+' Grundentgelt');expect(wb,out,'D7',174,c.slug+' Bank');expect(wb,out,'D8',617,c.slug+' Differenz');expect(wb,out,'D10','offen',c.slug+' fehlende Monate');expect(wb,bank,'D14',0,c.slug+' Kontrollsumme');
  val(inp,'B10',0);expect(wb,out,'D11',791,c.slug+' Null Zusatz');val(inp,'B10',18);expect(wb,out,'D11',917,c.slug+' 18 Zusatzmonate');val(inp,'B10',null);
  val(inp,'B13',1118);expect(wb,out,'D16','n.a.',c.slug+' Null Rest');val(inp,'B13',642);
  val(inp,'B12',null);expect(wb,out,'D15','offen',c.slug+' fehlende Rente');val(inp,'B12',1118);
  val(bank,'B7',0);expect(wb,out,'D7',128,c.slug+' Null Oktober');expect(wb,bank,'D14',-46,c.slug+' Kontrolle reagiert');val(bank,'B7',46);
  val(inp,'B6',null);expect(wb,out,'D6','offen',c.slug+' Grundrate fehlt');expect(wb,out,'D8','offen',c.slug+' Differenz bei fehlender Grundrate');expect(wb,out,'D16','offen',c.slug+' Kostenanteil bei fehlender Grundrate');val(inp,'B6',39);
  val(inp,'B10',18);val(inp,'B9',null);expect(wb,out,'D10','offen',c.slug+' Zusatzrate fehlt');expect(wb,out,'D11','offen',c.slug+' Gesamtsumme bei fehlender Zusatzrate');val(inp,'B9',7);val(inp,'B10',null);
  val(inp,'B11',null);expect(wb,out,'D13','offen',c.slug+' Journalwert fehlt');val(inp,'B11',39);
  val(bank,'C7',null);expect(wb,out,'D7','offen',c.slug+' Erstattungsfeld fehlt');expect(wb,bank,'D14','offen',c.slug+' Kontrollabgleich bei Datenluecke');val(bank,'C7',0);
  val(inp,'B7',12);expect(wb,out,'D6',557,c.slug+' geaenderte Laufzeit');val(inp,'B7',18);
  inp.getRange('B6:B13').format.horizontalAlignment='center';bank.getRange('B6:C7').format.horizontalAlignment='center';
  ranges=[['Kosten','A1:D24'],['Eingaben','A1:D22'],['Buchungen','A1:D23']];
 }else{
  const out=base(wb,'Ausspielung','Pegnesus Fassungen und vorhandene Belege',[22,21,22,24,22,27],29);
  const cut=base(wb,'Schnittplan','Audioclip und erhaltener Vorspann',[42,19,22,37],27);
  header(out,5,['Kanal','Sollfassung','Belegte Prüffassung','Versionsabgleich','Medienprobe belegt','Zuständig']);
  out.getRange('A6:F11').values=[['Webseite','Text v3','Text v2',null,0,'Ottmar Dörfler'],['Newsletter','Text v3 kurz','Text v2',null,0,'Jule Sommer'],['Satireseite','SAT-51','Beschreibung',null,0,'Frida Karg'],['Vorschaukarte','SAT-51','ROOM-14 alt',null,0,'Ben Riegel'],['Langer Ton','AU-62','AU-62',null,0,'Jule Sommer'],['Kurzclip','AU-62-C','Schnittplan',null,0,'Ben Riegel']];
  for(let r=6;r<=11;r++)formula(out,`D${r}`,`=IF(AND(B${r}<>"",C${r}<>"",B${r}=C${r}),"gleich","abweichend/offen")`);
  out.getRange('A6:F11').format={wrapText:true,rowHeight:38};out.getRange('B6:C11').format.font.color='#1D4ED8';out.getRange('E6:E11').format.font.color='#1D4ED8';out.getRange('E6:E11').dataValidation={rule:{type:'list',values:['0','1']}};
  val(out,'A14','Geplante Ausspielungen');formula(out,'D14','=COUNTA(A6:A11)');
  val(out,'A15','Abweichend oder offen');formula(out,'D15','=COUNTIF(D6:D11,"abweichend/offen")');
  val(out,'A16','Belegte Medienproben');formula(out,'D16','=IF(COUNT(E6:E11)=6,SUM(E6:E11),"offen")');
  note(out,19,'Quelle: 03_Redaktionsprotokoll und 05_Kontrollblatt_Ausspielung. Keine Veröffentlichung erfolgt.');
  note(out,20,'0 = keine Medienprobe belegt; 1 = zugeordnete Probe dokumentiert. Keine rechtliche Freigabe.');
  note(out,21,'AU-62 ist durch das Produktionsprotokoll bezeichnet. Eine Hörprobe ist auch dort nicht belegt.');
  note(out,23,'Der Versionsabgleich vergleicht Kennungen. Gleiche Kennungen belegen keine inhaltliche Prüfung.');
  note(out,24,'Neue Ergebnisse mit Fassung und Prüfperson nachtragen; keine rückwirkende Freigabe eintragen.');
  header(cut,5,['Angabe','Sekunden','Art','Quelle oder Bedeutung']);
  cut.getRange('A6:D10').values=[['Lange Fassung insgesamt',96,'Eingabe','AU-62 Produktionsplan'],['Vorspann beginnt',0,'Eingabe','Lange Fassung'],['Vorspann endet',6,'Eingabe','Lange Fassung'],['Clip beginnt',12,'Eingabe','AU-62-C Schnittplanung'],['Clip endet',42,'Eingabe','AU-62-C Schnittplanung']];
  cut.getRange('B6:B10').format.font.color='#1D4ED8';
  val(cut,'A12','Clipdauer');formula(cut,'B12','=IF(COUNT(B9:B10)=2,B10-B9,"offen")');
  val(cut,'A13','Vorspann im Clip');formula(cut,'B13','=IF(COUNT(B7:B10)=4,MAX(0,MIN(B8,B10)-MAX(B7,B9)),"offen")');
  val(cut,'A14','Anteil Vorspann an Clip');formula(cut,'B14','=IF(COUNT(B12:B13)=2,IF(B12=0,"n.a.",B13/B12),"offen")');cut.getRange('B14').setNumberFormat('0.0%');
  val(cut,'A16','Schnitt innerhalb Langfassung');formula(cut,'D16','=IF(COUNT(B6,B9:B10)=3,IF(AND(B9>=0,B10>=B9,B10<=B6),"ja","prüfen"),"offen")');
  note(cut,19,'Quelle: 02_Produktionsbeschreibung und 05_Kontrollblatt, Abschnitt 3.');
  note(cut,20,'Rechnung aus dem Schnittplan. Die tatsächlich exportierte Tondatei ist noch nicht geprüft.');
  note(cut,22,'Der fehlende Originalvorspann sagt nichts über einen zusätzlichen Plattformhinweis.');
  note(cut,23,'Auch einen ergänzten Hinweis muss das Publikum bei der konkreten Ausspielung wahrnehmen.');
  expect(wb,out,'D14',6,c.slug+' Anzahl');expect(wb,out,'D15',5,c.slug+' Versionen');expect(wb,out,'D16',0,c.slug+' Medienproben');expect(wb,cut,'B12',30,c.slug+' Dauer');expect(wb,cut,'B13',0,c.slug+' Vorspann entfernt');
  val(cut,'B9',0);expect(wb,cut,'B13',6,c.slug+' Vorspann erhalten');val(cut,'B9',12);
  val(cut,'B10',12);expect(wb,cut,'B14','n.a.',c.slug+' Nullclip');val(cut,'B10',42);
  val(cut,'B9',null);expect(wb,cut,'B12','offen',c.slug+' Anfang fehlt');val(cut,'B9',12);
  val(out,'C6','Text v3');expect(wb,out,'D15',4,c.slug+' Textbeleg nachgereicht');val(out,'C6','Text v2');
  val(out,'E11',1);expect(wb,out,'D16',1,c.slug+' Medienprobe nachgereicht');val(out,'E11',0);
  val(cut,'B7',null);expect(wb,cut,'B13','offen',c.slug+' Vorspannanfang fehlt');expect(wb,cut,'B14','offen',c.slug+' Anteil bei fehlendem Vorspannanfang');val(cut,'B7',0);
  val(cut,'B8',null);expect(wb,cut,'B14','offen',c.slug+' Anteil bei fehlendem Vorspannende');val(cut,'B8',6);
  val(out,'B10',null);val(out,'C10',null);expect(wb,out,'D10','abweichend/offen',c.slug+' zwei leere Versionskennungen');expect(wb,out,'D15',6,c.slug+' Versionsluecke wird gezaehlt');val(out,'B10','AU-62');val(out,'C10','AU-62');
  val(out,'E11',null);expect(wb,out,'D16','offen',c.slug+' Medienprobenstatus fehlt');val(out,'E11',0);
  cut.getRange('B6:B14').format.horizontalAlignment='center';out.getRange('E6:E11').format.horizontalAlignment='center';
  ranges=[['Ausspielung','A1:F25'],['Schnittplan','A1:D24']];
 }
 wb.recalculate();
 for(const [name,range] of ranges){
  const s=wb.worksheets.getItem(name);
  for(const row of s.getRange(range).values)for(const x of row)if(typeof x==='string'&&/^#(REF!|DIV\/0!|VALUE!|NAME\?|N\/A|NUM!|NULL!|SPILL!|CALC!)/.test(x))throw Error(`${c.slug} ${name}: ${x}`);
  const inspect=await wb.inspect({kind:'table',range:`${name}!${range}`,include:'values,formulas',tableMaxRows:29,tableMaxCols:6,maxChars:22000});
  await fs.writeFile(path.join(qa,`${c.slug}-${name}.ndjson`),inspect.ndjson);
  const preview=await wb.render({sheetName:name,range,scale:1.4,format:'png'});
  await fs.writeFile(path.join(qa,`${c.slug}-${name}.png`),new Uint8Array(await preview.arrayBuffer()));
 }
 const dir=path.join(root,'testakten',c.slug);await fs.mkdir(dir,{recursive:true});
 const target=path.join(dir,c.workbook.file);await(await SpreadsheetFile.exportXlsx(wb)).save(target);
 // Print areas and page setup only; all data and formulas remain artifact-tool authored.
 const zip=await JSZip.loadAsync(await fs.readFile(target));
 for(let i=0;i<ranges.length;i++){
  const file=`xl/worksheets/sheet${i+1}.xml`;let xml=await zip.file(file).async('string');const pre=xml.match(/<(\w+:)?worksheet\b/)[1]??'';
  xml=xml.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'').replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,'');
  xml=xml.replace(`</${pre}worksheet>`,`<${pre}pageMargins left="0.3" right="0.3" top="0.4" bottom="0.4" header="0.15" footer="0.15"/><${pre}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="1"/></${pre}worksheet>`);zip.file(file,xml);
 }
 let xml=await zip.file('xl/workbook.xml').async('string');const pre=xml.match(/<(\w+:)?workbook\b/)[1]??'';
 const defs=ranges.map(([name,range],i)=>`<${pre}definedName name="_xlnm.Print_Area" localSheetId="${i}">'${name}'!${range.replace(/([A-Z]+)(\d+)/g,'$$$1$$$2')}</${pre}definedName>`).join('');
 xml=xml.includes(`</${pre}definedNames>`)?xml.replace(`</${pre}definedNames>`,defs+`</${pre}definedNames>`):xml.replace(`</${pre}workbook>`,`<${pre}definedNames>${defs}</${pre}definedNames></${pre}workbook>`);
 zip.file('xl/workbook.xml',xml);await fs.writeFile(target,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
 try{await fs.rename(target+'.inspect.ndjson',path.join(qa,c.slug+'-export.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 console.log(c.slug+' XLSX erstellt und Eingabeproben bestanden');
}
await fs.writeFile(path.join(qa,'checks.json'),JSON.stringify(checks,null,2)+'\n');

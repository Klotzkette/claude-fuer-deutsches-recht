// WH26: drei additive Fortführungen. Artefakterstellung mit artifact-tool.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook,SpreadsheetFile}=await loadWorkbookRuntime();
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const out=path.join(root,'testakten/bauwirtschaft-baumanagement-werkhalle-warendorf');
const qa='/tmp/bauwirtschaft-vertiefung-20261006/warendorf';
await fs.mkdir(qa,{recursive:true});
const serial=s=>(Date.parse(s+'T00:00:00Z')-Date.UTC(1899,11,30))/86400000;
const money='#,##0.00_);(#,##0.00);"-"_)';
const col=i=>String.fromCharCode(65+i);
const gapSheets=new Set();
function sheet(wb,name,title,headers,widths,end=30){
  const s=wb.worksheets.add(name);s.showGridLines=false;
  if(widths.length===3){widths=[widths[0],widths[1],3,widths[2]];headers=[headers[0],headers[1],'',headers[2]];gapSheets.add(s);}
  s.getRange(`A1:${col(widths.length-1)}${end}`).format={font:{name:'Arial',size:11},verticalAlignment:'center',rowHeight:26};
  s.getRange('A2').values=[[title]];s.getRange('A2').format.font={name:'Arial',size:15,bold:true};
  s.getRange('A3').values=[['Stand 25.09.2026 16:00 Uhr']];s.getRange('A3').format.font.italic=true;
  s.getRange(`A5:${col(headers.length-1)}5`).values=[headers];
  s.getRange(`A5:${col(headers.length-1)}5`).format={fill:'#30485C',font:{name:'Arial',size:11,color:'#FFFFFF',bold:true},wrapText:true,rowHeight:34,horizontalAlignment:'center'};
  widths.forEach((width,i)=>s.getRange(`${col(i)}1:${col(i)}${end}`).format.columnWidth=width);
  if(gapSheets.has(s))s.getRange(`C5:C${end}`).format.fill='#FFFFFF';
  return s;
}
function write(s,range,values){if(gapSheets.has(s)&&range.includes(':C')){range=range.replace(':C',':D');values=values.map(([a,b,c])=>[a,b,null,c]);}s.getRange(range).values=values;s.getRange(range).format.wrapText=true;}
function formula(s,cell,f){s.getRange(cell).formulas=[[f]];s.getRange(cell).format.font.color=f.includes('!')?'#216E39':'#000000';}
function inputs(s,range){s.getRange(range).format.fill='#FFF2CC';s.getRange(range).format.font.color='#2457A7';}
function bit(s,range){inputs(s,range);s.getRange(range).dataValidation={rule:{type:'whole',operator:'between',formula1:0,formula2:1}};}
function notes(s,row,entries){for(const [i,e] of entries.entries()){const end=gapSheets.has(s)?'D':'C';s.getRange(`A${row+i}:${end}${row+i}`).merge();s.getRange(`A${row+i}`).values=[[e]];s.getRange(`A${row+i}:${end}${row+i}`).format={wrapText:true,rowHeight:28,font:{name:'Arial',size:10}};}}
async function save(wb,name,ranges){
 wb.recalculate();
 const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:60},maxChars:5000});
 await fs.writeFile(path.join(qa,name+'.errors.ndjson'),errors.ndjson);
 for(const [sheetName,range] of ranges){
   const img=await wb.render({sheetName,range,scale:1.35,format:'png'});
   await fs.writeFile(path.join(qa,name+'-'+sheetName+'.png'),new Uint8Array(await img.arrayBuffer()));
   const values=await wb.inspect({kind:'table',range:`'${sheetName}'!${range}`,include:'values,formulas',tableMaxRows:45,tableMaxCols:10,maxChars:24000});
   await fs.writeFile(path.join(qa,name+'-'+sheetName+'.ndjson'),values.ndjson);
 }
 await(await SpreadsheetFile.exportXlsx(wb)).save(path.join(out,name));
 try{await fs.rename(path.join(out,name+'.inspect.ndjson'),path.join(qa,name+'.export.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 console.log(name);
}

async function energie(){
 const w=Workbook.create();
 const t=sheet(w,'Termine','Energie und Produktionsanlauf',['Ansatz oder Ergebnis','Wert','Bedeutung und Quelle'],[45,24,66],32);
 const v=sheet(w,'Voraussetzungen','Freigaben der mobilen Versorgung',['Voraussetzung','Bestätigt 0 oder 1','Nachweis und offene Angabe'],[45,24,66],24);
 write(t,'A6:C21',[
 ['Dauerhafte Energie',serial('2026-11-16'),'07 Lieferfortschreibung; Netztermin ist bedingt.'],
 ['Mobile Energie',serial('2026-10-12'),'18 Angebot; noch keine Anschlussfreigabe.'],
 ['Versuche regulär in Kalendertagen',15,'27 Baufolge und 40 Maschinenbauer.'],
 ['Einweisung in Kalendertagen',6,'27 Baufolge und 40 Maschinenbauer.'],
 ['Versuche mit Abendfenstern',12,'40 Maschinenbauer; Teamzusage fehlt.'],
 ['Variante 0 1 oder 2',1,'0 dauerhaft / 1 mobil tags / 2 mobil abends.'],
 ['Energie für Linie 1',null,'Die gewählte Variante bestimmt das Energiedatum.'],
 ['Versuchsdauer Linie 1',null,'Die Abendvariante verwendet ausschließlich den Ansatz zwölf Tage.'],
 ['Anlauf Linie 1 als Terminannahme',null,'Energiedatum plus Versuchsdauer plus Einweisung.'],
 ['Anlauf Linie 2 als Terminannahme',null,'Dauerhafte Energie plus reguläre Versuche plus Einweisung.'],
 ['Vollbetrieb als Terminannahme',null,'Der spätere Anlauf beider Linien bestimmt diesen Termin.'],
 ['Mobilmiete endet laut Angebot',serial('2026-11-22'),'18 MB 0925; Umschaltung und Rückbau noch abstimmen.'],
 ['Vorgesehene Anschlusslast in kVA',240,'28 Anschlusswerte und 33 Vorprüfung: 220 plus 20.'],
 ['Angebotene Leistung in kVA',250,'18 Angebot; Anlaufkurve steht noch aus.'],
 ['Rechnerische Differenz in kVA',null,'Kein technischer Nachweis der Eignung für Anlaufströme.'],
 ['Stand der Ausführungsfreigabe',null,'Eine berechnete Terminannahme ist keine Freigabe.']]);
 inputs(t,'B6:B11');inputs(t,'B17:B19');
 t.getRange('B11').dataValidation={rule:{type:'whole',operator:'between',formula1:0,formula2:2}};
 t.getRange('B6:B7').setNumberFormat('yyyy-mm-dd');t.getRange('B12').setNumberFormat('yyyy-mm-dd');t.getRange('B14:B17').setNumberFormat('yyyy-mm-dd');
 const variantGuard=f=>`=IF(NOT(ISNUMBER(B11)),"Variante prüfen",IF(OR(B11<0,B11>2,B11<>INT(B11)),"Variante prüfen",${f}))`;
 formula(t,'B12',variantGuard('IF(B11=0,IF(ISNUMBER(B6),B6,"Datum fehlt"),IF(ISNUMBER(B7),B7,"Datum fehlt"))'));
 formula(t,'B13',variantGuard('IF(B11=2,IF(AND(ISNUMBER(B10),B10>=0),B10,"Dauer fehlt"),IF(AND(ISNUMBER(B8),B8>=0),B8,"Dauer fehlt"))'));
 formula(t,'B14','=IF(AND(ISNUMBER(B12),ISNUMBER(B13),ISNUMBER(B9),B9>=0),SUM(B12:B13)+B9,"Eingabe offen")');
 formula(t,'B15','=IF(AND(ISNUMBER(B6),ISNUMBER(B8),ISNUMBER(B9),B8>=0,B9>=0),B6+B8+B9,"Eingabe offen")');
 formula(t,'B16','=IF(COUNT(B14:B15)=2,MAX(B14:B15),"Eingabe offen")');
 formula(t,'B20','=IF(COUNT(B18:B19)=2,B19-B18,"Leistung fehlt")');
 formula(t,'B21',variantGuard('IF(B11=0,"Dauerhaften Anschluss bestätigen",IF(AND(\'Voraussetzungen\'!B6=1,\'Voraussetzungen\'!B7=1,\'Voraussetzungen\'!B8=1,\'Voraussetzungen\'!B9=1,OR(B11=1,AND(\'Voraussetzungen\'!B10=1,\'Voraussetzungen\'!B11=1))),"Freigaben dokumentiert","Freigaben offen"))'));
 t.getRange('A6:D21').format.rowHeight=28;t.getRange('B21').format.wrapText=true;
 notes(t,24,[
 'Gelb = bearbeitbare Eingabe. Grün = Formel mit Bezug auf ein anderes Blatt. Schwarz = berechnetes Ergebnis.',
 'Zuerst die Variante in B11 wählen. Nur belegte neue Termine und Dauern eintragen. Die Quelldateien 07, 18, 27 und 40 bleiben unverändert.',
 'Kalendertage werden addiert; Wochenenden und Feiertage werden nicht ausgeschlossen. B14 bis B16 zeigen Planannahmen, keine Terminzusagen.',
 'Für eine Fortschreibung neue Bestätigungen im Blatt Voraussetzungen mit Beleg und Datum ergänzen. Danach 0 erst bei belegter Bestätigung auf 1 setzen.',
 'Die Vorgängermappe 09 bleibt der Planstand 25.09.2026 ohne Provisorium. Diese Datei vertieft deren Terminansätze; sie importiert keine verdeckten externen Werte.'
 ]);
 write(v,'A6:C11',[
 ['Kaufmännischer Auftrag',0,'36 Freigabevermerk: Angebote nicht angenommen.'],
 ['Netzanschluss freigegeben',0,'19 Netzanschluss und 33 Vorprüfung: Unterlagen ausstehend.'],
 ['Schutzprüfung und Startversuch',0,'33 Vorprüfung: am Aufstelltag zu dokumentieren.'],
 ['Maschinenbereich und Team bestätigt',0,'40 Maschinenbauer: Team und Maschinenaufstellung offen.'],
 ['Abendzeiten geklärt',0,'35 Anfrage: bis 25.09. 15:45 Uhr keine Antwort.'],
 ['Zusätzlicher Service beauftragt',0,'40 Maschinenbauer: Preis und Teamzusage fehlen.']]);
 bit(v,'B6:B11');v.getRange('A6:D11').format.rowHeight=34;
 notes(v,14,[
 '0 bedeutet nicht belegt oder noch offen; 1 bedeutet durch einen bezeichneten Nachweis bestätigt. Die Quellenzelle muss bei einer Änderung den neuen Beleg nennen.',
 'Die ersten vier Voraussetzungen betreffen die mobile Tagesvariante. Für die Abendvariante werden zusätzlich die letzten beiden Bestätigungen benötigt.',
 'Eine einzelne Bestätigung genügt nicht. Auch bei kaufmännischem Auftrag bleiben fehlende Anschlussprüfung oder Teamzusage sichtbar.',
 'Die Stromwerte sind Nennwerte aus Unterlagen. Eine positive rechnerische Differenz ersetzt die fehlende Anlaufkurve nicht.'
 ]);
 await save(w,'41_Energie_und_Freigaben.xlsx',[['Termine','A1:D28'],['Voraussetzungen','A1:D17']]);
}

async function kosten(){
 const w=Workbook.create();
 const k=sheet(w,'Kalkulation','Mobile Versorgung mit Zusatzfenstern',['Kosten oder Entscheidung','Wert','Funktion und Verwendung'],[43,25,70],31);
 const a=sheet(w,'Ansätze','Angebotswerte und veränderbare Mengen',['Eingabe','Wert','Quelle und Einheit'],[43,25,70],29);
 write(a,'A6:C19',[
 ['Grundpreis netto',36000,'18 MB 0925: sechs Wochen einschließlich Einschichtbetriebsstoff.'],
 ['Vorauszahlung auf Grundpreis',0.3,'18 Angebot und 34 Ergänzung: keine Vorauszahlung auf Zusatzstunden.'],
 ['Umsatzsteuersatz',0.19,'18 und 34 Angebote; Belege weisen 19 Prozent aus.'],
 ['Zusätzliche Abendfenster',10,'34 Ergänzungsangebot: Anzahl der vorgesehenen Fenster.'],
 ['Stunden je Abendfenster',3,'34 Ergänzungsangebot: 20:00 bis 23:00 Uhr.'],
 ['Elektrofachkräfte je Fenster',2,'34 Ergänzungsangebot: Anzahl Personen.'],
 ['Preis je Fachkraftstunde',78,'34 Ergänzungsangebot: EUR netto einschließlich kalkulierter Zuschläge.'],
 ['Sicherungswache je Stunde',42,'34 Ergänzungsangebot: EUR netto.'],
 ['Zusätzlicher Betriebsstoff je Stunde',18,'34 Ergänzungsangebot: EUR netto nur für Abendfenster.'],
 ['Einmaliger Schallschutz',1250,'34 Ergänzungsangebot: EUR netto nach Ausführung.'],
 ['Zusätzliche angefangene Mietwochen',0,'34 Ergänzungsangebot: 0 bis 2 Wochen nach 22.11.; noch nicht bestellt.'],
 ['Miete je zusätzlicher Woche',4000,'34 Ergänzungsangebot: EUR netto.'],
 ['Betriebsstoff je zusätzlicher Woche',500,'34 Ergänzungsangebot: EUR netto nur Einschichtbetrieb.'],
 ['Zusatzservice Maschinenbauer netto',null,'40 Maschinenbauer: Preis fehlt. Bei Variante 2 ist er erforderlich.']]);
 inputs(a,'B6:B19');a.getRange('B7:B8').setNumberFormat('0.0%');a.getRange('B6').setNumberFormat(money);a.getRange('B12:B15').setNumberFormat(money);a.getRange('B17:B19').setNumberFormat(money);
 a.getRange('B16').dataValidation={rule:{type:'whole',operator:'between',formula1:0,formula2:2}};a.getRange('A6:D19').format.rowHeight=28;
 notes(a,22,[
 'Gelbe Zellen sind Eingaben. Der leere Servicepreis bedeutet unbekannt, nicht null. Ein bestätigter kostenfreier Service kann mit 0 und Beleg erfasst werden.',
 'Fenster, Stunden und Personalzahl treiben die Zusatzkosten. Die angebotenen Personensätze enthalten Zuschläge; diese werden nicht nochmals aufgeschlagen.',
 'Die Verlängerung gilt nur für Einschichtbetrieb. Weitere Abendstunden in der Verlängerung müssen gesondert angeboten und hier neu abgegrenzt werden.',
 'Zur Fortschreibung Mengen und Preise nur mit neuer Quelle ändern. Das Blatt Kalkulation berechnet netto, Umsatzsteuer, Vorauszahlung und Rest automatisch.'
 ]);
 write(k,'A6:C20',[
 ['Variante 1 oder 2',1,'1 mobil tags / 2 mobil mit Abendfenstern.'],
 ['Elektro Personenstunden',null,'Fenster mal Stunden mal Zahl der Fachkräfte.'],
 ['Grundangebot netto',null,'Der Grundpreis bleibt einmal enthalten.'],
 ['Abendleistungen Breden netto',null,'Fachkräfte, Sicherungswache, Mehrbetriebsstoff und einmaliger Schallschutz.'],
 ['Maschinenservice zusätzlich netto',null,'Bei Abendbetrieb derzeit preislich offen.'],
 ['Mietverlängerung netto',null,'Angefangene Wochen mal Miete und Einschichtbetriebsstoff.'],
 ['Gesamter Ansatz netto',null,'Nur vollständig bekannte aktive Ansätze werden summiert.'],
 ['Umsatzsteuer',null,'Steuersatz aus den Angebotsbelegen.'],
 ['Gesamter Ansatz brutto',null,'Nettoansatz plus Umsatzsteuer.'],
 ['Angebotsbetrag ohne Maschinenservice',null,'Bekannte Beträge; bei Variante 2 kein vollständiger Gesamtpreis.'],
 ['Vorauszahlung brutto bei Annahme',null,'30 Prozent nur vom Grundangebot, zuzüglich Umsatzsteuer.'],
 ['Restbetrag brutto nach Rückbau',null,'Gesamtbetrag minus Vorauszahlung. Keine bereits ausgeführte Zahlung.'],
 ['Bestellung erteilt 0 oder 1',0,'36 Freigabevermerk: bislang keine Bestellung.'],
 ['Kaufmännischer Stand',null,'Auch ein vollständiger Preis ersetzt keine Beauftragung.'],
 ['Verlängerung maximal zwei Wochen',null,'Ein darüber hinausgehender Ansatz benötigt ein neues Angebot.']]);
 inputs(k,'B6');bit(k,'B18');k.getRange('B6').dataValidation={rule:{type:'whole',operator:'between',formula1:1,formula2:2}};
 formula(k,'B7','=IF(B6=1,0,IF(AND(B6=2,COUNT(\'Ansätze\'!B9:B11)=3,MIN(\'Ansätze\'!B9:B11)>=0),\'Ansätze\'!B9*\'Ansätze\'!B10*\'Ansätze\'!B11,"Menge fehlt"))');
 formula(k,'B8','=IF(AND(ISNUMBER(\'Ansätze\'!B6),\'Ansätze\'!B6>=0),\'Ansätze\'!B6,"Preis fehlt")');
 formula(k,'B9','=IF(B6=1,0,IF(AND(B6=2,ISNUMBER(B7),COUNT(\'Ansätze\'!B12:B15)=4,MIN(\'Ansätze\'!B12:B15)>=0),B7*\'Ansätze\'!B12+\'Ansätze\'!B9*\'Ansätze\'!B10*SUM(\'Ansätze\'!B13:B14)+\'Ansätze\'!B15,"Preis fehlt"))');
 formula(k,'B10','=IF(B6=1,0,IF(AND(B6=2,ISNUMBER(\'Ansätze\'!B19),\'Ansätze\'!B19>=0),\'Ansätze\'!B19,"Servicepreis fehlt"))');
 formula(k,'B11','=IF(AND(COUNT(\'Ansätze\'!B16:B18)=3,\'Ansätze\'!B16>=0,\'Ansätze\'!B16<=2,\'Ansätze\'!B16=INT(\'Ansätze\'!B16),MIN(\'Ansätze\'!B17:B18)>=0),\'Ansätze\'!B16*SUM(\'Ansätze\'!B17:B18),"Verlängerung prüfen")');
 formula(k,'B12','=IF(COUNT(B8:B11)=4,SUM(B8:B11),"Preis offen")');
 formula(k,'B13','=IF(AND(ISNUMBER(B12),ISNUMBER(\'Ansätze\'!B8),\'Ansätze\'!B8>=0),ROUND(B12*\'Ansätze\'!B8,2),"Preis offen")');
 formula(k,'B14','=IF(COUNT(B12:B13)=2,SUM(B12:B13),"Preis offen")');
 formula(k,'B15','=IF(COUNT(B8:B9)=2,IF(ISNUMBER(B11),SUM(B8:B9,B11),"Preis offen"),"Preis offen")');
 formula(k,'B16','=IF(AND(ISNUMBER(B8),COUNT(\'Ansätze\'!B7:B8)=2,MIN(\'Ansätze\'!B7:B8)>=0,\'Ansätze\'!B7<=1),ROUND(B8*\'Ansätze\'!B7*(1+\'Ansätze\'!B8),2),"Satz fehlt")');
 formula(k,'B17','=IF(AND(ISNUMBER(B14),ISNUMBER(B16)),B14-B16,"Preis offen")');
 formula(k,'B19','=IF(B18=0,"Nicht bestellt",IF(B18=1,IF(ISNUMBER(B12),"Bestellung erfassen","Preis weiterhin offen"),"Eingabe prüfen"))');
 formula(k,'B20','=IF(AND(ISNUMBER(\'Ansätze\'!B16),\'Ansätze\'!B16>=0,\'Ansätze\'!B16<=2),"Im Angebotsrahmen","Neues Angebot erforderlich")');
 k.getRange('B8:B17').setNumberFormat(money);k.getRange('A6:D20').format.rowHeight=28;k.getRange('B6:B20').format.wrapText=true;
 k.getRange('B12:B14').conditionalFormats.add('containsText',{text:'offen',format:{fill:'#FCE4D6',font:{color:'#9C0006',bold:true}}});
 notes(k,23,[
 'Diese Rechnung erweitert die Angebotsprüfung zu Datei 18. Sie ist weder Kostenbuchung noch Zahlungsfreigabe. Die alten Istwerte in Datei 10 bleiben erhalten.',
 'Variante 1 lässt den noch unbekannten Servicepreis unberücksichtigt. Variante 2 zeigt einen offenen Gesamtpreis, bis dieser Preis belegt eingetragen ist.',
 'Vorauszahlung und Rest sind Zahlungsanlässe bei Beauftragung. Die Staffelung ist von den tatsächlichen Zahlungsdaten in Datei 43 zu unterscheiden.',
 'Weitere Kosten wie die Kranforderung und die alte Produktionsmiete gehören nicht zu diesem Angebot. Die technisch nutzbaren Termine stehen in Datei 41.'
 ]);
 await save(w,'42_Mobilversorgung_Kosten.xlsx',[['Kalkulation','A1:D26'],['Ansätze','A1:D25']]);
}

async function zahlungen(){
 const w=Workbook.create();
 const p=sheet(w,'Monatsplan','Zahlungsfortführung nach Datum',['Monat oder Ansatz','Anfang brutto','Zufluss brutto','Abfluss brutto','Ende brutto'],[25,22,22,22,22],29);
 const z=sheet(w,'Zahlungsregister','Zahlungsansätze mit Einzelentscheidung',['ID','Netto EUR','Datum geplant','Einplanen 0/1','Freigabe 0/1','Bezahlt brutto','Rest brutto','Bearbeitung'],[20,17,18,14,14,18,18,31],33);
 write(z,'A6:H17',[
 ['WH 260924',160000,serial('2026-10-08'),1,0,0,null,null],
 ['Plan Oktober',260000,serial('2026-10-30'),1,0,0,null,null],
 ['Plan November',430000,serial('2026-11-30'),1,0,0,null,null],
 ['Plan Dezember',316000,serial('2026-12-31'),1,0,0,null,null],
 ['MB Voraus',10800,serial('2026-09-28'),0,0,0,null,null],
 ['MB Rest',25200,serial('2026-11-30'),0,0,0,null,null],
 ['KM N03',9600,null,0,0,0,null,null],
 ['Abend Breden',7730,serial('2026-11-30'),0,0,0,null,null],
 ['DR Mehransatz',1750,serial('2026-11-30'),0,0,0,null,null],
 ['Service Abend',null,null,0,0,0,null,null],
 [null,null,null,null,null,null,null,null],
 [null,null,null,null,null,null,null,null]
 ]);
 inputs(z,'A6:F17');bit(z,'D6:E17');z.getRange('B6:B17').setNumberFormat(money);z.getRange('C6:C17').setNumberFormat('yyyy-mm-dd');z.getRange('F6:G17').setNumberFormat(money);z.freezePanes.freezeRows(5);
 for(let r=6;r<=17;r++){
  formula(z,`G${r}`,`=IF(A${r}="","",IF(AND(ISNUMBER(B${r}),B${r}>=0,ISNUMBER(F${r}),F${r}>=0,ISNUMBER('Monatsplan'!B13),'Monatsplan'!B13>=0,'Monatsplan'!B13<=1,F${r}<=ROUND(B${r}*(1+'Monatsplan'!B13),2)),ROUND(B${r}*(1+'Monatsplan'!B13),2)-F${r},"Betrag fehlt"))`);
  formula(z,`H${r}`,`=IF(A${r}="","",IF(COUNTIFS($A$6:$A$17,A${r})>1,"ID doppelt",IF(AND(D${r}<>0,D${r}<>1),"Planwahl prüfen",IF(AND(E${r}<>0,E${r}<>1),"Freigabe prüfen",IF(D${r}=0,"Nicht eingeplant",IF(NOT(ISNUMBER(C${r})),"Datum fehlt",IF(OR(C${r}<'Monatsplan'!B14,C${r}>='Monatsplan'!B15),"Außerhalb Zeitraum",IF(NOT(ISNUMBER(G${r})),"Betrag fehlt",IF(E${r}=1,"Freigegeben","Freigabe offen")))))))))`);
 }
 formula(z,'B14',`=IF(AND(COUNT('Monatsplan'!B20:B21)=2,MIN('Monatsplan'!B20:B21)>=0),'Monatsplan'!B20-'Monatsplan'!B21,"Angebot fehlt")`);
 z.getRange('A6:H17').format.rowHeight=30;
 z.getRange('H6:H17').conditionalFormats.add('containsText',{text:'fehlt',format:{fill:'#FCE4D6',font:{color:'#9C0006',bold:true}}});
 z.getRange('H6:H17').conditionalFormats.add('containsText',{text:'doppelt',format:{fill:'#FCE4D6',font:{color:'#9C0006',bold:true}}});
 for(const [row,text] of [
 [20,'Zeilen 6 bis 9: 21 Zahlungsplan und 37 Rechnungseingang. Der offene Septemberabschlag ist genau einmal am 08.10. eingeplant.'],
 [21,'Zeilen 10 und 11: 18 MB 0925. 10.800 EUR Vorauszahlung und 25.200 EUR Rest bleiben ohne Auftrag außerhalb des aktiven Plans.'],
 [22,'Zeilen 12 und 13: 15 Kranangebot und 34 Ergänzungsangebot. Krantermin fehlt; Abendpreis umfasst keinen Maschinenservice.'],
 [23,'Zeilen 14 und 15: 38 und 39 Druckluft (31.750 minus 30.000 EUR) sowie 40 Maschinenbauer (Preis fehlt).'],
 [24,'Gelb = Eingabe. Einplanen ist eine Prognoseentscheidung. Freigabe ist eine separate Entscheidung und löst keine Bankzahlung aus.'],
 [25,'Leere Zeilen 16 und 17 sind für weitere Vorgänge vorbereitet. ID, Betrag, Datum, 0/1-Werte und bezahlt = 0 eingeben. Formeln bleiben stehen.'],
 [26,'Bei weiteren Zeilen nach 17 müssen Formeln und die begrenzten Auswertungsbereiche 6 bis 17 erweitert werden. IDs dürfen nicht doppelt vergeben sein.'],
 [27,'Bei Fortschreibung des Kontostichtags Anfangssaldo und bisher bezahlte Anteile zusammen aktualisieren. Frühere Ausgaben nicht nochmals vom neuen Saldo abziehen.'],
 [28,'Die Druckluftdifferenz verändert bei Einplanung den alten Restansatz. Die gesamten 31.750 EUR dürfen nicht zusätzlich zum unveränderten Grundplan angesetzt werden.']
 ]){z.getRange(`A${row}:H${row}`).merge();z.getRange(`A${row}`).values=[[text]];z.getRange(`A${row}:H${row}`).format={wrapText:true,rowHeight:31,font:{name:'Arial',size:10}};}
 write(p,'A6:E9',[[serial('2026-09-01'),null,0,null,null],[serial('2026-10-01'),null,400000,null,null],[serial('2026-11-01'),null,600000,null,null],[serial('2026-12-01'),null,0,null,null]]);
 p.getRange('A6:A9').setNumberFormat('yyyy-mm');p.getRange('B6:E9').setNumberFormat(money);inputs(p,'C6:C9');
 write(p,'A12:C19',[
 ['Bankbestand zum Stichtag',512400,'30 Finanzierung und 24 Bankansicht.'],
 ['Steuersatz',0.19,'19 Prozent laut Angebots- und Rechnungsbelegen.'],
 ['Plan beginnt am',serial('2026-09-25'),'Inklusive dieses Tages; offene Zahlungen.'],
 ['Plan endet vor',serial('2027-01-01'),'Exklusive dieses Tages.'],
 ['Unvollständige aktive Zeilen',null,'Bei Fehlern bleibt der Monatsabfluss offen.'],
 ['Freigegebener Rest im Zeitraum',null,'Nur aktive Zeilen mit gesonderter Freigabe.'],
 ['Basisendbestand nach altem Plan',124860,'09 Ablauf und 30 Finanzierung; Stand 25.09.'],
 ['Änderung gegenüber Basis',null,'Zeitverschiebung allein verändert den Endbestand nicht.']]);
 write(p,'A20:C21',[['Druckluftangebot netto',31750,'38 Angebot DR 260925.'],['Bisheriger Druckluftansatz netto',30000,'13 Restkostenerhebung; im Grundplan enthalten.']]);
 inputs(p,'B20:B21');p.getRange('B20:B21').setNumberFormat(money);p.getRange('C20:E21').merge(true);p.getRange('A20:E21').format.wrapText=true;p.getRange('A20:E21').format.rowHeight=40;
 inputs(p,'B12:B15');p.getRange('B12').setNumberFormat(money);p.getRange('B13').setNumberFormat('0.0%');p.getRange('B14:B15').setNumberFormat('yyyy-mm-dd');p.getRange('B17:B19').setNumberFormat(money);p.getRange('C12:E19').merge(true);p.getRange('A12:E19').format.wrapText=true;p.getRange('A12:E19').format.rowHeight=42;
 p.getRange('B14:B15').format.horizontalAlignment='center';
 formula(p,'B16',`=COUNTIFS('Zahlungsregister'!$D$6:$D$17,1,'Zahlungsregister'!$H$6:$H$17,"<>Freigegeben",'Zahlungsregister'!$H$6:$H$17,"<>Freigabe offen")+COUNTIFS('Zahlungsregister'!$H$6:$H$17,"Planwahl prüfen")+IF(AND('Zahlungsregister'!D13=1,'Zahlungsregister'!D15<>1),1,0)`);
 formula(p,'B17',`=IF(B16=0,SUMIFS('Zahlungsregister'!$G$6:$G$17,'Zahlungsregister'!$D$6:$D$17,1,'Zahlungsregister'!$E$6:$E$17,1,'Zahlungsregister'!$C$6:$C$17,">="&B14,'Zahlungsregister'!$C$6:$C$17,"<"&B15),"Eingabe offen")`);
 for(let r=6;r<=9;r++){
   formula(p,`B${r}`,r===6?'=B12':`=E${r-1}`);
   formula(p,`D${r}`,`=IF($B$16=0,SUMIFS('Zahlungsregister'!$G$6:$G$17,'Zahlungsregister'!$D$6:$D$17,1,'Zahlungsregister'!$C$6:$C$17,">="&MAX(A${r},$B$14),'Zahlungsregister'!$C$6:$C$17,"<"&MIN(EDATE(A${r},1),$B$15)),"Eingabe offen")`);
   formula(p,`E${r}`,`=IF(COUNT(B${r}:D${r})=3,B${r}+C${r}-D${r},"Eingabe offen")`);
 }
 formula(p,'B19','=IF(ISNUMBER(E9),E9-B18,"Eingabe offen")');
 for(const [row,text] of [
 [22,'Der aktive Plan verwendet Zahlungsdaten und Bruttobeträge. Die alte Septemberreserve wird nicht zusätzlich abgezogen.'],
 [23,'Planbeträge sind keine Rechnungen. Das Register nennt für jede Position Einplanung und Freigabe getrennt.'],
 [24,'Abendleistungen in Zeile 13 erfordern auch Service in Zeile 15. Ohne Einplanung und Preis des Services bleibt der Gesamtplan offen.'],
 [25,'Weitere Kreditabrufe sind geplant. Vorsteuererstattungen sowie Miete der alten Produktion werden hier nicht als Baukontozufluss oder Bauinvestition erfasst.'],
 [26,'Die Mappe ergänzt Datei 09. Datei 10 bleibt die separate Sicht auf Nettoinvestition und Obligo. Ein positiver Bankbestand ist kein freies Kostenbudget.']
 ]){p.getRange(`A${row}:E${row}`).merge();p.getRange(`A${row}`).values=[[text]];p.getRange(`A${row}:E${row}`).format={wrapText:true,rowHeight:34,font:{name:'Arial',size:10}};}
 await save(w,'43_Zahlungen_und_Entscheidungen.xlsx',[['Monatsplan','A1:E26'],['Zahlungsregister','A1:H28']]);
}
await energie();await kosten();await zahlungen();

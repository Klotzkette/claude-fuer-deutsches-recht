// Drei native Ergänzungsmappen. Artefaktautorenschaft ausschließlich Artifact Tool.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {pathToFileURL,fileURLToPath} from 'node:url';
const modules=process.env.AKTEN_NODE_MODULES;
if(!modules)throw Error('AKTEN_NODE_MODULES auf die gebündelten Abhängigkeiten setzen.');
const req=createRequire(path.join(modules,'.einbeck-loader.cjs'));
const {Workbook,SpreadsheetFile}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const dir=path.join(root,'testakten/bauwirtschaft-hoai-buergerhaus-einbeck');
const qa=process.env.EINBECK_VERTIEFUNG_QA||'/tmp/bauwirtschaft-vertiefung-20261006/einbeck';
await fs.mkdir(qa,{recursive:true});
const files=JSON.parse(await fs.readFile(path.join(qa,'neue-dateien.json')));
const reports=[];
const dates=d=>Math.round((Date.parse(d+'T00:00:00Z')-Date.parse('1899-12-30T00:00:00Z'))/86400000);
const c=(s,a,v)=>s.getRange(a).values=[[v]];
const f=(s,a,v)=>s.getRange(a).formulas=[[v]];
function input(s,a,v){c(s,a,v);s.getRange(a).format.fill='#fff2cc';s.getRange(a).format.font.color='#174b99';}
function base(w,name,title,sub,headers,widths,endrow=35){
 const s=w.worksheets.add(name),end=String.fromCharCode(64+headers.length);
 s.showGridLines=false;s.getRange(`A1:${end}${endrow}`).format={font:{name:'Times New Roman',size:11,color:'#111111'},verticalAlignment:'center',rowHeight:20};
 c(s,'A2',title);s.getRange('A2').format.font={name:'Times New Roman',size:15,bold:true};
 c(s,'A3',sub);s.getRange('A3').format.font.italic=true;
 s.getRange(`A7:${end}7`).values=[headers];s.getRange(`A7:${end}7`).format={fill:'#344956',font:{name:'Times New Roman',bold:true,size:11,color:'#ffffff'},rowHeight:38,wrapText:true,horizontalAlignment:'center'};
 widths.forEach((v,i)=>s.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}${endrow}`).format.columnWidth=v);
 s.getRange(`A1:${end}1`).format.rowHeight=8;s.getRange(`A4:${end}6`).format.rowHeight=12;s.getRange(`A8:${end}${endrow}`).format.wrapText=true;s.freezePanes.freezeRows(7);return s;
}
function note(s,row,text){c(s,'A'+row,text);s.getRange('A'+row).format.wrapText=false;}
function summary(s,row,label,col,formula){c(s,'A'+row,label);f(s,col+row,formula);s.getRange(`A${row}:${col}${row}`).format.fill='#e8edf0';s.getRange(`A${row}:${col}${row}`).format.font.bold=true;}
async function finish(w,n,ranges,probes){
 w.recalculate();const checks=[];
 for(const [name,range]of ranges){
  const inspection=await w.inspect({kind:'table',range:`'${name}'!${range}`,include:'values,formulas',tableMaxRows:45,tableMaxCols:9,maxChars:25000});checks.push(inspection.ndjson);
  const blob=await w.render({sheetName:name,range,scale:1.5,format:'png'});await fs.writeFile(path.join(qa,`${n}-${name}.png`),new Uint8Array(await blob.arrayBuffer()));
 }
 const errors=await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},maxChars:4000});
 const output=await SpreadsheetFile.exportXlsx(w);await output.save(path.join(dir,files[n]));
 try{await fs.rename(path.join(dir,files[n]+'.inspect.ndjson'),path.join(qa,files[n]+'.inspect.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 reports.push({n,file:files[n],ranges,probes,checks,errors:errors.ndjson});
 await fs.writeFile(path.join(qa,'tabellen-pruefung.json'),JSON.stringify(reports,null,2));
}

{
 const w=Workbook.create();
 const s=base(w,'Abgleich','Aufmaß und Schlussrechnung Los 1','Hartwig Architektur · 25.09.2026 · Fortführung zu 35, 36 und 37',
 ['Position','Menge laut Rechnung','AM 07 Menge','EP netto EUR','Verlangt EUR','Prüfansatz EUR','Differenz EUR','Beleg'],[25,12,12,14,16,16,14,24],44);
 const m=base(w,'Mengen','Mengenherleitung aus AM 07','Übertragung vom 23.09.2026 (46). Keine neue Vermessung verdeckter Bauteile.',
 ['Position','Basis','Faktor','Zusatz','AM 07 Menge','Einheit','Quelle und Grenze'],[25,12,12,12,15,10,48],36);
 const k=base(w,'Prüfannahmen','Prüfanteil und Zahlungsbelege','Eingaben gelb. Die ursprüngliche Prüfung 37 und die Rechnung 36 bleiben unverändert.',
 ['Eingabe oder Beleg','Wert','Einheit','Erläuterung'],[37,19,15,65],30);
 input(k,'B8',0);c(k,'A8','Prüfanteil N01.5');c(k,'C8','Anteil');c(k,'D8','0 % = bisher keine Freigabe. 50 % wäre ein unverbindliches Rechenszenario.');k.getRange('B8').setNumberFormat('0%');
 input(k,'B9',.19);c(k,'A9','Umsatzsteuersatz');c(k,'C9','Anteil');c(k,'D9','36, Schlussrechnung: 19 Prozent.');k.getRange('B9').setNumberFormat('0%');
 input(k,'B10',35700);c(k,'A10','Abschlag 12.10.2023');c(k,'C10','EUR brutto');c(k,'D10','36, Abschnitt 2: vereinnahmt zu LB-231002.');
 input(k,'B11',47600);c(k,'A11','Abschlag 18.12.2023');c(k,'C11','EUR brutto');c(k,'D11','36, Abschnitt 2: vereinnahmt zu LB-231201.');
 c(k,'A12','Spätere Zahlung nachgewiesen');input(k,'B12','Offen');c(k,'D12','Offen lässt den heutigen Restbetrag unbestimmt. Null ist erst bei bestätigtem Zahlungsverlauf zulässig.');
 c(k,'A13','Späterer Zahlbetrag');input(k,'B13',null);c(k,'C13','EUR brutto');c(k,'D13','Nur belegte Zahlungen nach den beiden Abschlägen erfassen. Keine Summe aus dem Prüfungsvorschlag übertragen.');
 c(k,'A14','Beleg der späteren Zahlung');input(k,'B14',null);c(k,'D14','Kontoauszug oder Bestätigung mit Datum und Rechnungsbezug eintragen.');
 f(k,'B16','=IF(OR(B12<>"Belegt",NOT(ISNUMBER(B13)),B14=""),"Zahlungsbeleg fehlt","Beleg eingetragen")');c(k,'A16','Aktueller Belegstatus');
 k.getRange('B8').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:1}};
 k.getRange('B12').dataValidation={rule:{type:'list',values:['Offen','Belegt']}};
 k.getRange('A8:D14').format.rowHeight=50;k.getRange('B10:B13').setNumberFormat('#,##0.00');k.getRange('B12').setNumberFormat('@');
 note(k,19,'1 Bedienung');note(k,20,'Nur gelbe Felder ändern. Formeln stehen in schwarzen Zellen. Beleg und Zahlung gemeinsam erfassen.');
 note(k,22,'2 Rechenweg');note(k,23,'Mengen × Vertragspreis ergeben den Grundauftrag. N01.5 wird mit dem eingegebenen Anteil bewertet.');
 note(k,25,'3 Grenzen');note(k,26,'Kein Zahlungsauftrag, Anerkenntnis oder Mängelabzug. Keine automatische Festlegung von Fälligkeit.');
 note(k,27,'Prüfanteile zwischen 0 und 100 Prozent sind Recheneingaben und ersetzen keine Einigung.');
 const rows=[['2.1 Einrichtung',1,1,0,'psch','35, AM-07; eine Pauschale.'],['2.2 Rückbau',18,12,0,'m²','35, AM-07: 18,00 × 12,00 m.'],['2.3 Aushub',60,1,6,'m³','35 und 46: ohne 4 m³ N01.2. Geometrisches Einzelblatt fehlt.'],['2.4 Fundamente',24,1,1.2,'m³','35 und 46: verdeckte Verbreiterung übernommen.'],['2.5 Bodenplatte',10,8,0,'m²','35: Anbau 10,00 × 8,00 m.'],['2.6 Mauerwerk',95,1,3,'m²','35: Grund- und Zusatzfläche; Öffnungen gemäß LV abgezogen.'],['2.7 Sockel',36,1,6,'m²','35: Feststellung vor Verfüllung am 03.10.2023.'],['2.8 Innenputz',144,1,6,'m²','35: Zusatzfläche ohne neue Schadenszuordnung.'],['2.9 Dach',10,8,0,'m²','35: Anbau 10,00 × 8,00 m.'],['2.10 Türen',3,1,0,'St','35: drei Außentüren.'],['2.11 Rampe',12,1.5,null,'m²','35 und 46: Läufe, Zwischenpodest und Anschlussstreifen.'],['2.12 Rinne',9,1,.4,'m','35: Endstück 0,40 m; keine Gefällemessung.']];
 const qty=[1,216,66,25.2,80,98,42,150,80,3,21.45,9.4],ep=[9000,41,92,330,152,135,205,52,268,2590,260,172];
 rows.forEach((r,i)=>{const a=i+8;c(m,'A'+a,r[0]);input(m,'B'+a,r[1]);input(m,'C'+a,r[2]);if(i===10)f(m,'D'+a,'=IF(COUNT(E23:E24)<>2,"Eingabe fehlt",SUM(E23:E24))');else input(m,'D'+a,r[3]);f(m,'E'+a,`=IF(OR(NOT(ISNUMBER(B${a})),NOT(ISNUMBER(C${a})),NOT(ISNUMBER(D${a}))),"Eingabe fehlt",ROUND(B${a}*C${a}+D${a},2))`);c(m,'F'+a,r[4]);c(m,'G'+a,r[5]);
 c(s,'A'+a,r[0]);input(s,'B'+a,qty[i]);f(s,'C'+a,`='Mengen'!E${a}`);input(s,'D'+a,ep[i]);f(s,'E'+a,`=IF(OR(NOT(ISNUMBER(B${a})),NOT(ISNUMBER(D${a}))),"Eingabe fehlt",ROUND(B${a}*D${a},2))`);f(s,'F'+a,`=IF(OR(NOT(ISNUMBER(C${a})),NOT(ISNUMBER(D${a}))),"Eingabe fehlt",ROUND(C${a}*D${a},2))`);f(s,'G'+a,`=IF(OR(NOT(ISNUMBER(E${a})),NOT(ISNUMBER(F${a}))),"Offen",E${a}-F${a})`);c(s,'H'+a,'25 / Preis; 35 / Menge; 36 / Rechnung');});
 c(m,'A23','Zwischenpodest');input(m,'B23',1.5);input(m,'C23',1.5);f(m,'E23','=IF(AND(ISNUMBER(B23),ISNUMBER(C23)),B23*C23,"Eingabe fehlt")');c(m,'F23','m²');c(m,'G23','35: 1,50 × 1,50 m.');
 c(m,'A24','Anschlussstreifen');input(m,'E24',1.2);c(m,'F24','m²');c(m,'G24','35: Flächenwert ohne getrennte Kantenlängen.');
 note(m,27,'Gelb = übertragene Eingabe, Schwarz = Rechnung. Basis × Faktor + Zusatz ergibt die Menge.');
 note(m,29,'Einheiten sind positionsbezogen. Bei einfachen Mengenüberträgen ist der Faktor 1 dimensionslos.');
 note(m,31,'Fehlende Eingaben werden angezeigt. Eine echte Null bleibt eine Null und ist keine fehlende Angabe.');
 note(m,33,'Die ursprünglichen AM-07 Werte bleiben in Rechnung 36 und Datei 35 unverändert dokumentiert.');
 const nt=[['N01.1 Leitung',14,145],['N01.2 Graben',4,92],['N01.3 Abtransport',1,380],['N01.4 Anschluss',16,58],['N01.5 Bereitschaft',2,620]];
 nt.forEach((r,i)=>{const a=i+20;c(s,'A'+a,r[0]);input(s,'B'+a,r[1]);input(s,'D'+a,r[2]);if(i<4)input(s,'C'+a,r[1]);else c(s,'C'+a,'nicht bestätigt');
 f(s,'E'+a,`=IF(AND(ISNUMBER(B${a}),ISNUMBER(D${a})),ROUND(B${a}*D${a},2),"Eingabe fehlt")`);
 f(s,'F'+a,i<4?`=IF(AND(ISNUMBER(C${a}),ISNUMBER(D${a})),ROUND(C${a}*D${a},2),"Eingabe fehlt")`:`=IF(NOT(ISNUMBER(E24)),"Eingabe fehlt",IF(OR(NOT(ISNUMBER('Prüfannahmen'!B8)),'Prüfannahmen'!B8<0,'Prüfannahmen'!B8>1),"Anteil prüfen",ROUND(E24*'Prüfannahmen'!B8,2)))`);
 f(s,'G'+a,`=IF(AND(ISNUMBER(E${a}),ISNUMBER(F${a})),E${a}-F${a},"Offen")`);c(s,'H'+a,i<4?'33, 34 und 35':'33 und 47; 34 ohne Freigabe');});
 for(const col of ['E','F'])f(s,col+'26',`=IF(COUNT(${col}8:${col}24)<>17,"Eingabe fehlt",SUM(${col}8:${col}24))`);
 c(s,'A26','Gesamt netto');c(s,'A27','Umsatzsteuer');c(s,'A28','Gesamt brutto');c(s,'A30','Nach bekannten Abschlägen');
 for(const col of ['E','F']){f(s,col+'27',`=IF(AND(ISNUMBER(${col}26),ISNUMBER('Prüfannahmen'!B9)),ROUND(${col}26*'Prüfannahmen'!B9,2),"Offen")`);f(s,col+'28',`=IF(ISNUMBER(${col}27),${col}26+${col}27,"Offen")`);f(s,col+'30',`=IF(AND(ISNUMBER(${col}28),COUNT('Prüfannahmen'!B10:B11)=2),${col}28-SUM('Prüfannahmen'!B10:B11),"Offen")`);}
 f(s,'G30','=IF(AND(ISNUMBER(E30),ISNUMBER(F30)),E30-F30,"Offen")');
 c(s,'A32','Rest nach späterer Zahlung');f(s,'F32','=IF(OR(\'Prüfannahmen\'!B12<>"Belegt",NOT(ISNUMBER(\'Prüfannahmen\'!B13)),\'Prüfannahmen\'!B14="",NOT(ISNUMBER(F30))),"Zahlungsbeleg fehlt",F30-\'Prüfannahmen\'!B13)');
 note(s,33,'1 Lesen: Verlangt folgt Rechnung 36. Prüfansatz folgt AM-07 und dem Anteil auf Prüfannahmen.');
 note(s,34,'2 Ausgangsstand: 114.153,80 EUR netto geprüft; N01.5 mit 1.240,00 EUR netto weiter streitig.');
 note(s,35,'3 F30 ist ein historischer Prüfungsvorschlag. F32 bleibt bis zum späteren Zahlungsnachweis offen.');
 note(s,36,'Änderungen in Mengen oder Prüfannahmen wirken auf die Berechnung, nicht auf die alten Originale.');
 m.getRange('A8:G19').format.rowHeight=44;s.getRange('A8:H24').format.rowHeight=36;
 m.getRange('B8:E24').setNumberFormat('#,##0.00');s.getRange('B8:G32').setNumberFormat('#,##0.00');
 s.getRange('F32:H32').format.rowHeight=42;s.getRange('F32').format.columnWidth=20;
 for(const a of ['A26:H28','A30:H30'])s.getRange(a).format.fill='#e8edf0';
 s.getRange('G8:G30').conditionalFormats.add('cellIs',{operator:'greaterThan',formula:0,format:{fill:'#fff2cc'}});
 await finish(w,48,[['Abgleich','A1:H36'],['Mengen','A1:G34'],['Prüfannahmen','A1:D28']],
 [{sheet:'Prüfannahmen',cell:'B8',value:.5,outSheet:'Abgleich',outCell:'F30',expected:53280.82},{sheet:'Mengen',cell:'B8',value:2,outSheet:'Abgleich',outCell:'F26',expected:123153.8},{sheet:'Mengen',cell:'B8',value:null,outSheet:'Abgleich',outCell:'F26',expected:'Eingabe fehlt'},
 ...['C20','C21','C22','C23','D21','B24'].map(cell=>({sheet:'Abgleich',cell,value:null,outSheet:'Abgleich',outCell:'F26',expected:'Eingabe fehlt'})),
 {sheet:'Abgleich',cell:'C21',value:'offen',outSheet:'Abgleich',outCell:'F26',expected:'Eingabe fehlt'},
 {sheet:'Abgleich',cell:'C21',value:0,outSheet:'Abgleich',outCell:'F26',expected:113785.8},
 {sheet:'Abgleich',cell:'B20',value:null,outSheet:'Abgleich',outCell:'E26',expected:'Eingabe fehlt'},
 ...['B23','E24'].map(cell=>({sheet:'Mengen',cell,value:null,outSheet:'Abgleich',outCell:'F26',expected:'Eingabe fehlt'})),
 ...['B9','B10'].map(cell=>({sheet:'Prüfannahmen',cell,value:null,outSheet:'Abgleich',outCell:'F30',expected:'Offen'}))]);
}

{
 const w=Workbook.create();
 const s=base(w,'Vorgänge','Mängel und Befundverfolgung','Hartwig Architektur · Stand 02.10.2026 · Bestand, neue Befunde und Nachweise getrennt',
 ['Kennung und Vorgang','Prüfung erfolgt','Nachweis eingetragen','Erledigung bestätigt','Nächster Schritt','Beleg'],[30,14,27,17,33,35],31);
 const b=base(w,'Beobachtungen','Messungen und Betriebsbeobachtungen','Keine Ursachenautomatik. Werte verschiedener Methoden sind nicht als Messreihe vergleichbar.',
 ['ID und Datum','Ort oder Methode','Wert von','Wert bis','Einheit','Beleg und Aussagegrenze'],[26,29,12,12,13,48],29);
 c(s,'A5','Offene Vorgänge');f(s,'B5','=COUNTIFS(E8:E12,"<>Abgeschlossen")');
 const rows=[['M-01 Rinnenrost','Ja','39, Nachkontrolle 28.03.2024','Ja','38/39: damaliges Klappern beseitigt.'],['M-02 Türschließer','Ja','39, Nachkontrolle 28.03.2024','Ja','38/39: damalige Einstellung bestätigt.'],['B-01 Saalnordwand','Nein','','Nein','41–44/50: Ursache weiterhin offen.'],['B-02 Rinnenanschluss','Nein','','Nein','43/50/51: Ablauf und Höhen prüfen.'],['D-01 Architekturabnahme','Nein','','Nein','39/40/45: gesonderte Erklärung fehlt.']];
 rows.forEach((r,i)=>{const a=i+8;c(s,'A'+a,r[0]);input(s,'B'+a,r[1]);input(s,'C'+a,r[2]);input(s,'D'+a,r[3]);f(s,'E'+a,`=IF(B${a}<>"Ja","Prüfung offen",IF(C${a}="","Nachweis fehlt",IF(D${a}<>"Ja","Bestätigung offen","Abgeschlossen")))`);c(s,'F'+a,r[4]);});
 s.getRange('B8:B12').dataValidation={rule:{type:'list',values:['Ja','Nein']}};s.getRange('D8:D12').dataValidation={rule:{type:'list',values:['Ja','Nein']}};
 s.getRange('E8:E12').conditionalFormats.add('notContainsText',{text:'Abgeschlossen',format:{fill:'#fff2cc'}});
 s.getRange('A8:F12').format.rowHeight=64;
 note(s,15,'1 Bedienung');note(s,16,'Die gelben Spalten B bis D halten Bearbeitung und Nachweis fest. Die Kennung bleibt beim Vorgang.');
 note(s,18,'2 Statusregel');note(s,19,'Ein Vorgang endet erst mit Prüfung, bezeichnetem Nachweis und bestätigter Erledigung.');
 note(s,21,'3 Inhaltliche Grenzen');note(s,22,'M-01 aus 2024 und B-02 aus 2026 sind getrennt. Ein fester Rost bestätigt keinen freien Ablauf.');
 note(s,24,'Die Termine aus 44 bleiben dort geführt. Diese Mappe berechnet keine Verjährung oder Haftungsquote.');
 note(s,26,'Kein Auftrag zur Öffnung liegt vor. Angebot 51 ist ein Vorschlag, keine bereits ausgeführte Untersuchung.');
 const obs=[['O-01 · 17.09.2026','Sockel, kapazitive Anzeige',86,92,'Geräteeinheit','43, Abschnitt 1. Keine Masseprozente.'],['O-02 · 17.09.2026','Vergleich bei 1,20 m Höhe',34,39,'Geräteeinheit','43, Abschnitt 1. Dasselbe Gerät, keine Materialprobe.'],['O-03 · 17.09.2026','Rost zum angrenzenden Belag',6,6,'mm','43, Abschnitt 2. Ungefähre Höhendifferenz.'],['O-04 · 17.09.2026','Wasserversuch',10,10,'Liter','43: langsamer Ablauf; Dauer nicht gemessen.'],['O-05 · 24.09.2026','Pfützentiefe, Zollstock',4,4,'mm','50: punktuell abgelesen, kein Nivellement.'],['O-06 · 24.09.2026','Abstand zweier Rundgänge',35,35,'Minuten','50: 17:35 bis 18:10 Uhr. Kein Beweis der gesamten Ablaufdauer.']];
 obs.forEach((r,i)=>{const a=i+8;b.getRange(`A${a}:F${a}`).values=[r];});b.getRange('A8:F13').format.rowHeight=54;
 c(b,'A16','Abstand Anzeigeintervalle');f(b,'C16','=C8-D9');f(b,'D16','=D8-C9');c(b,'E16','Geräteeinheit');c(b,'F16','Untere/obere Differenz der Intervalle, keine Schadens- oder Feuchtequote.');b.getRange('A16:F16').format.rowHeight=50;
 note(b,19,'1 Quellenzeilen');note(b,20,'43 ist die gemeinsame Begehung. 50 ist die spätere Erklärung des Hauswarts, ohne neue Materialprüfung.');
 note(b,22,'2 Auswertung');note(b,23,'Die Intervallabstände sind ein Rechenvergleich. Sie erlauben keine Umrechnung in Masseprozent.');
 note(b,25,'3 Weitere Angaben');note(b,26,'Zu Pfützentiefe und Rinnenversatz fehlen gemeinsamer Bezugspunkt und identische Messmethode.');
 await finish(w,53,[['Vorgänge','A1:F27'],['Beobachtungen','A1:F27']],
 [{sheet:'Vorgänge',cell:'B10',value:'Ja',outSheet:'Vorgänge',outCell:'E10',expected:'Nachweis fehlt'},{sheet:'Vorgänge',cell:'D8',value:'Nein',outSheet:'Vorgänge',outCell:'B5',expected:4}]);
}

{
 const w=Workbook.create();
 const s=base(w,'Honorar','Honorarzuordnung und Leistungsanteile','Hartwig Architektur · 05.10.2026 · Vertragspauschale, keine neue Honorarschlussrechnung',
 ['Leistungsphase','Vertragsanteil','Pauschale EUR','Rechenanteil','Ansatz EUR','Rest EUR','Belegstatus'],[29,14,17,14,17,17,32],34);
 const b=base(w,'Leistungsbelege','Leistungsbelege und offene Fragen','Grundlage: Vertrag 02, Erläuterung 52 und vorhandene Projektunterlagen.',
 ['Phase','Beleg und konkretes Ergebnis','Offene Frage','Status'],[14,60,46,18],30);
 input(s,'C5',48000);c(s,'A5','Pauschale Grundleistungen');c(s,'G5','02, Abschnitt 2');
 const names=['Grundlagen','Vorplanung','Entwurf','Genehmigung','Ausführung','LV und Mengen','Vergabe','Überwachung','Betreuung'];const shares=[.02,.07,.15,.03,.25,.10,.04,.32,.02];
 const evidence=[['03/04: Untersuchungsbedarf und Bestandsaufnahme.','Zusatzleistung Bestand separat vergütet.','Belegt'],['05/06: Variantenvergleich und Nordanbauentscheidung.','Keine weitere Umnutzungsvariante beauftragt.','Belegt'],['07–10: Entwurf, Kosten und Fachplanerabstimmung.','Gebührenansatz in 09 ist frühe Steuerpauschale.','Belegt'],['11–17: Antrag, Ergänzung und Bescheid.','Späterer Gymnastikwunsch ist nicht mit umfasst.','Belegt'],['18–22: Abruf, AP-01, D-12 und Portalstände.','Auflösung abweichender Höheninformation prüfen.','Rückfrage'],['23/24: zwölf LV-Positionen mit Mengen und Preisen.','Kein Nachweis der tatsächlichen Ausführung allein durch LV.','Belegt'],['25–28: Angebote, Preisspiegel und Zuschlag.','Nachtrag N01 wurde nur teilweise beauftragt.','Belegt'],['30/35–40: Bauablauf, Aufmaß, Prüfung und Übergabe.','Einzelblatt Nachkontrolle und Architekturabnahme fehlen.','Rückfrage'],['41–44/50/51: Begehung, Bewertung und Untersuchungsvorschlag.','Ursache offen; weitere Betreuung und Kontrollbegehung stehen aus.','Laufend']];
 names.forEach((name,i)=>{const a=i+8;c(s,'A'+a,`${i+1} ${name}`);input(s,'B'+a,shares[i]);f(s,'C'+a,`=IF(AND(ISNUMBER($C$5),ISNUMBER(B${a}),B${a}>=0,B${a}<=1),ROUND($C$5*B${a},2),"Eingabe fehlt")`);input(s,'D'+a,i===8?0:1);f(s,'E'+a,`=IF(OR(NOT(ISNUMBER(C${a})),NOT(ISNUMBER(D${a})),D${a}<0,D${a}>1),"Anteil prüfen",ROUND(C${a}*D${a},2))`);f(s,'F'+a,`=IF(AND(ISNUMBER(C${a}),ISNUMBER(E${a})),C${a}-E${a},"Offen")`);f(s,'G'+a,`='Leistungsbelege'!D${a}`);
 c(b,'A'+a,i+1);c(b,'B'+a,evidence[i][0]);c(b,'C'+a,evidence[i][1]);input(b,'D'+a,evidence[i][2]);});
 s.getRange('B8:B18').setNumberFormat('0%');s.getRange('C5:C22').setNumberFormat('#,##0.00');s.getRange('D8:D16').setNumberFormat('0%');s.getRange('C8:C16').setNumberFormat('#,##0.00');s.getRange('E8:F23').setNumberFormat('#,##0.00');
 s.getRange('D8:D16').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:1}};
 b.getRange('D8:D16').dataValidation={rule:{type:'list',values:['Belegt','Rückfrage','Laufend']}};
 c(s,'A18','Grundleistungen');f(s,'B18','=IF(COUNT(B8:B16)=9,SUM(B8:B16),"Anteil prüfen")');f(s,'C18','=IF(AND(COUNT(C8:C16)=9,ABS(SUM(B8:B16)-1)<0.000001),SUM(C8:C16),"Vertrag prüfen")');f(s,'E18','=IF(OR(COUNT(E8:E16)<>9,NOT(ISNUMBER(C18))),"Anteil prüfen",SUM(E8:E16))');f(s,'F18','=IF(AND(ISNUMBER(C18),ISNUMBER(E18)),C18-E18,"Offen")');
 c(s,'A19','Bestandsarbeiten');input(s,'C19',3000);f(s,'E19','=IF(ISNUMBER(C19),C19,"Eingabe fehlt")');c(s,'G19','02 und 04, gesonderte Pauschale');
 c(s,'A20','Nebenkosten');input(s,'C20',3000);f(s,'E20','=IF(ISNUMBER(C20),C20,"Eingabe fehlt")');c(s,'G20','02, pauschal vereinbart');
 c(s,'A22','Gesamt netto');f(s,'C22','=IF(COUNT(C18:C20)=3,SUM(C18:C20),"Eingabe fehlt")');f(s,'E22','=IF(NOT(ISNUMBER(E18)),"Anteil prüfen",IF(COUNT(E18:E20)=3,SUM(E18:E20),"Eingabe fehlt"))');f(s,'F22','=IF(AND(ISNUMBER(C22),ISNUMBER(E22)),C22-E22,"Offen")');
 c(s,'A23','Umsatzsteuer');input(s,'B23',.19);s.getRange('B23').setNumberFormat('0%');f(s,'E23','=IF(AND(ISNUMBER(E22),ISNUMBER(B23)),ROUND(E22*B23,2),"Offen")');
 c(s,'A24','Ansatz brutto');f(s,'E24','=IF(ISNUMBER(E23),E22+E23,"Offen")');s.getRange('E24').setNumberFormat('#,##0.00');
 c(s,'A26','Offene Belegfragen');f(s,'G26','=COUNTIFS(\'Leistungsbelege\'!D8:D16,"<>Belegt")');
 note(s,28,'Gelbe Rechenanteile sind Annahmen zur Pauschalzuordnung, keine Abnahme oder Fälligkeitsentscheidung.');
 note(s,30,'100 Prozent in Phase 8 schließt die offenen Belegfragen nicht. Rückfragen stehen unabhängig im rechten Blatt.');
 note(s,32,'Ausgangsstand wie 37/40: 53.040,00 EUR netto zugeordnet; 960,00 EUR für laufende Betreuung verbleiben.');
 s.getRange('A8:G16').format.rowHeight=39;s.getRange('A19:G20').format.rowHeight=42;s.getRange('A18:G18').format.fill='#e8edf0';s.getRange('A22:G24').format.fill='#e8edf0';
 b.getRange('A8:D16').format.rowHeight=61;
 note(b,19,'1 Bedienung');note(b,20,'Status nur nach Belegabgleich ändern. Eine hohe Prozentzahl im Honorarblatt schließt keine Belegfrage.');
 note(b,22,'2 Vertragsgrundlage');note(b,23,'02 vereinbart 48.000 EUR für Grundleistungen sowie jeweils 3.000 EUR für Bestand und Nebenkosten.');
 note(b,25,'3 Grenzen');note(b,26,'Kein Saldo aus Rechnungen und Zahlungen. Keine automatische Honoraranpassung anhand der Baukosten.');
 note(b,28,'Die Unterlage 52 erläutert die einzelnen Ergebnisse. Die Zuordnung behauptet keine lückenlose Überwachung.');
 await finish(w,54,[['Honorar','A1:G33'],['Leistungsbelege','A1:D29']],
 [{sheet:'Honorar',cell:'D16',value:.5,outSheet:'Honorar',outCell:'E22',expected:53520},{sheet:'Honorar',cell:'D15',value:null,outSheet:'Honorar',outCell:'E22',expected:'Anteil prüfen'},{sheet:'Honorar',cell:'D15',value:0,outSheet:'Honorar',outCell:'E22',expected:37680},
 ...['C5','B8'].map(cell=>({sheet:'Honorar',cell,value:null,outSheet:'Honorar',outCell:'E22',expected:'Anteil prüfen'})),
 ...['C19','C20'].map(cell=>({sheet:'Honorar',cell,value:null,outSheet:'Honorar',outCell:'E22',expected:'Eingabe fehlt'})),
 {sheet:'Honorar',cell:'B8',value:.03,outSheet:'Honorar',outCell:'E22',expected:'Anteil prüfen'},
 {sheet:'Honorar',cell:'B23',value:null,outSheet:'Honorar',outCell:'E24',expected:'Offen'},
 {sheet:'Honorar',cell:'C19',value:0,outSheet:'Honorar',outCell:'E22',expected:50040}]);
}
console.log(JSON.stringify({created:reports.map(r=>r.file),report:path.join(qa,'tabellen-pruefung.json')}));

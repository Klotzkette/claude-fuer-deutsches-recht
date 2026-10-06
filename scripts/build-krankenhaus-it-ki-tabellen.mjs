// Vier native Arbeitsmappen der fiktiven Klinikakte; Autorenschaft: Artifact Tool.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {pathToFileURL,fileURLToPath} from 'node:url';
const req=createRequire(path.join(process.env.AKTEN_NODE_MODULES,'.klinik-loader.cjs'));
const {Workbook,SpreadsheetFile}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const dir=path.join(root,'testakten/krankenhaus-it-ki-auenhoehe-thueringen');
const qa=process.env.KLINIK_QA||'/tmp/krankenhaus-it-ki-20261006/tabellen';
await fs.mkdir(dir,{recursive:true});await fs.mkdir(qa,{recursive:true});
const reports=[];
const c=(s,a,v)=>s.getRange(a).values=[[v]],f=(s,a,v)=>s.getRange(a).formulas=[[v]];
const date=d=>(Date.parse(d+'T00:00:00Z')-Date.parse('1899-12-30T00:00:00Z'))/86400000;
function input(s,a,v){c(s,a,v);s.getRange(a).format.fill='#fff2cc';s.getRange(a).format.font.color='#174b99';}
function note(s,r,t){c(s,'A'+r,t);s.getRange('A'+r).format.wrapText=false;}
function base(w,name,title,headers,widths,rows=34){
 const s=w.worksheets.add(name),end=String.fromCharCode(64+headers.length);
 s.showGridLines=false;s.getRange(`A1:${end}${rows}`).format={font:{name:'Times New Roman',size:11,color:'#111111'},rowHeight:22,verticalAlignment:'center',wrapText:true};
 const widthScale=Math.min(1,152/widths.reduce((a,b)=>a+b,0));
 widths=widths.map(v=>v*widthScale);
 widths.forEach((v,i)=>s.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}${rows}`).format.columnWidth=v);
 c(s,'A2',title);s.getRange('A2').format={font:{name:'Times New Roman',size:15,bold:true},wrapText:false,rowHeight:28};
 note(s,3,'Klinikverbund Auenhöhe GmbH · Nora Bergmann · Arbeitsstand 06.10.2026');
 s.getRange(`A7:${end}7`).values=[headers];s.getRange(`A7:${end}7`).format={fill:'#344956',font:{name:'Times New Roman',size:11,bold:true,color:'#ffffff'},rowHeight:42,wrapText:true};s.freezePanes.freezeRows(7);return s;
}
async function finish(w,n,name,ranges,probes=[]){
 for(const [name,range]of ranges){const s=w.worksheets.getItem(name);const end=range.match(/:([A-Z]+)([0-9]+)/);let last=7;for(let r=8;r<=Number(end[2]);r++){const val=s.getRange('A'+r).values[0][0];if(val===null||val==='')break;last=r;}s.getRange(`A7:${end[1]}${last}`).format.borders={preset:'all',style:'thin',color:'#d2d9df'};}
 w.recalculate();const checks=[];
 for(const [sheet,range]of ranges){checks.push((await w.inspect({kind:'table',range:`'${sheet}'!${range}`,include:'values,formulas',tableMaxRows:45,tableMaxCols:8,maxChars:28000})).ndjson);const b=await w.render({sheetName:sheet,range,scale:1.2,format:'png'});await fs.writeFile(path.join(qa,`${n}-${sheet}.png`),new Uint8Array(await b.arrayBuffer()));}
 const file=`${n}_${name}.xlsx`;await (await SpreadsheetFile.exportXlsx(w)).save(path.join(dir,file));
 const errors=(await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:100},maxChars:2000})).ndjson;
 reports.push({file,ranges,probes,checks,errors});await fs.writeFile(path.join(qa,'tabellen-pruefung.json'),JSON.stringify(reports,null,2));
 try{await fs.rename(path.join(dir,file+'.inspect.ndjson'),path.join(qa,file+'.inspect.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
}

{
 const w=Workbook.create();
 const s=base(w,'Vorhaben','Drei Vorhaben und ihre nächste Entscheidung',['Vorhaben und Version','Verantwortliche','Ziel und vorgesehener Nutzerkreis','Nächste Entscheidung','Stand'],[29,23,41,41,22],26);
 const rows=[['P01 Sprechfeder Clinical 2.4','Nora Bergmann / Dr. Amira Feld','Diktat und Entlassbrief; ärztlich prüfen, keine autonome Therapie.','Cloudvertrag, Datenflüsse und klinischen Pilotumfang abstimmen.','Nicht freigegeben'],['P02 Radialert Triage 5.1','Dr. Amira Feld / Karim Seidel','Radiologische Priorisierung; lokale Verarbeitung, Fernwartung vorgesehen.','Zweckbestimmung und Nachweise müssen die Version 5.1 abdecken.','Nicht freigegeben'],['P03 SEPSIS-LR','Dr. Oskar Wenck / Benedikt Fink','Retrospektive Versorgungsforschung 2022–2025; Hochschulpartner.','Eigene Forschung, Übermittlung, MVZ-Daten und Training trennen.','Nicht freigegeben']];
 s.getRange('A8:E10').values=rows;s.getRange('A8:E10').format.rowHeight=88;c(s,'A5','Vorhaben ohne Betriebsfreigabe');f(s,'E5','=COUNTIF(E8:E10,"Nicht freigegeben")');
 note(s,13,'1 Verwendung');note(s,14,'Das Blatt Datenflüsse hält jeden Verarbeitungsschritt getrennt fest. Gleiche Konzernmarke bedeutet');note(s,15,'keine gemeinsame verantwortliche Stelle. Das MVZ ist eine eigene juristische Person.');
 note(s,17,'2 Stand der Entscheidung');note(s,18,'Die gewünschte Pilotplanung ersetzt keine Freigabe. Technische Tests ohne Patientendaten separat planen.');
 note(s,20,'3 Quellen');note(s,21,'01 Projektauftrag, 09 Datenfluss, 17 Zweckbestimmung, 24 Forschungsprotokoll und 25 Datenkatalog.');
 const d=base(w,'Datenflüsse','Verarbeitungsschritte, Empfänger und offene Angaben',['ID / Vorhaben','Daten und Zweck','Von / an','Ort und Zugriff','Offene Angabe','Belegstatus'],[20,38,36,31,37,20],30);
 const flows=[['D01 / P01','Audio zur ärztlichen Dokumentation','Klinik → Sprechfeder Health Europe','Cloud Frankfurt','Audiospeicherung, Löschlauf, Zugriffsschutz','Lieferantenangabe'],['D02 / P01','Entlassbriefentwurf zurück ins KIS','Sprechfeder → behandelnde Ärztin','Klinik und Cloud','Wer prüft und dokumentiert die Freigabe?','Geplant'],['D03 / P01','Support mit möglichen Inhaltsdaten','Sprechfeder Support Inc.','USA, optionaler Remotezugriff','Unternehmen, Aktivierung, Umfang, Transferweg','Nachweis offen'],['D04 / P01','Produktverbesserung / Modelltraining','Lieferant oder dessen Partner','Nicht abschließend bezeichnet','Trainingsklausel und tatsächlichen Datenfluss klären','Streitig'],['D05 / P02','Bilddaten, Befundpriorisierung','PACS → Radialert 5.1','Lokaler Klinikserver','Version und abgedeckte Zweckbestimmung','Nachweis offen'],['D06 / P02','Wartungsdaten, möglicher Bildzugriff','Radiaviso Medical','Remotezugriff, Zielsystem offen','Personen, Ort, Rechte, Protokollierung','Nachweis offen'],['D07 / P03','Behandlungsdaten 2022–2025','Klinik → internes Forschungsteam','Kliniknetz','Forschungsgrundlage, Minimierung, Verknüpfung','Geplant'],['D08 / P03','Pseudonymisierter Analysedatensatz','Klinik → Hochschule Saalebogen','Hochschulumgebung noch zu prüfen','Übermittlungsgrundlage, Verträge, Reidentifikation','Nachweis offen'],['D09 / P03','Ambulante Behandlungsdaten','MVZ → Forschungsprojekt','Noch nicht bestimmt','Eigene Verantwortlichkeit und eigene Grundlage','Nicht beschlossen']];
 d.getRange('A8:F16').values=flows;d.getRange('A8:F16').format.rowHeight=65;c(d,'A5','Datenflüsse insgesamt');f(d,'F5','=COUNTA(A8:A16)');
 note(d,19,'1 Fortschreibung');note(d,20,'Pro Empfänger und Zweck eine eigene Zeile. Nachweis offen ist keine bestätigte Übermittlung.');
 note(d,22,'2 Zuordnung');note(d,23,'Lieferantenangaben aus der Akte sind noch keine verifizierten Garantien; Vertrag und Technik abgleichen.');
 note(d,25,'3 Reichweite');note(d,26,'Die Liste dokumentiert den geplanten Stand. Keine Patientennamen oder medizinischen Einzelwerte eintragen.');
 await finish(w,37,'Vorhaben_Datenfluesse',[['Vorhaben','A1:E23'],['Datenflüsse','A1:F27']],[{sheet:'Vorhaben',cell:'E8',value:'Freigabe dokumentiert',outSheet:'Vorhaben',outCell:'E5',expected:2}]);
}
{
 const w=Workbook.create();const s=base(w,'Maßnahmen','Maßnahmen und belegte Erledigung',['Kennung / Gegenstand','Zuständig','Interner Zieltermin','Prüfung erfolgt','Nachweis / Fundstelle','Erledigung bestätigt','Bearbeitungsstand'],[29,24,16,15,32,18,26],31);
 const rows=[['M01 / Cloudvertrag und Training','Benedikt Fink','2026-10-09'],['M02 / C5-Systemumfang und Kontrollen','Karim Seidel','2026-10-12'],['M03 / US-Support und Transferweg','Benedikt Fink','2026-10-12'],['M04 / DSFA und Schutzmaßnahmen','Nora Bergmann','2026-10-14'],['M05 / Patient:inneninformation','Dr. Amira Feld','2026-10-14'],['M06 / Anzeige ThürKHG 27b','Geschäftsführung','2026-10-13'],['M07 / Radialert 5.1 Zweck / Nachweise','Dr. Amira Feld','2026-10-15'],['M08 / SEPSIS-LR / Hochschule / MVZ','Dr. Oskar Wenck','2026-10-16'],['M09 / Beteiligung Betriebsrat','Paul Lindner','2026-10-14'],['M10 / Rückfallbetrieb und Schulung','Nora Bergmann','2026-10-16']];
 rows.forEach((r,i)=>{const a=8+i;c(s,'A'+a,r[0]);c(s,'B'+a,r[1]);input(s,'C'+a,date(r[2]));input(s,'D'+a,'Nein');input(s,'E'+a,null);input(s,'F'+a,'Nein');f(s,'G'+a,`=IF(D${a}<>"Ja","Prüfung offen",IF(E${a}="","Nachweis fehlt",IF(F${a}<>"Ja","Bestätigung offen","Erledigung dokumentiert")))`);});
 s.getRange('C8:C17').setNumberFormat('dd.mm.yyyy');s.getRange('C8:D17').format.horizontalAlignment='center';s.getRange('A8:G17').format.rowHeight=51;for(const a of ['D8:D17','F8:F17'])s.getRange(a).dataValidation={rule:{type:'list',values:['Ja','Nein']}};
 c(s,'A5','Noch nicht dokumentiert erledigt');f(s,'G5','=COUNTIF(G8:G17,"<>Erledigung dokumentiert")');
 note(s,20,'1 Bedienung');note(s,21,'Gelbe Felder fortschreiben. Eine Ja-Angabe ohne Fundstelle beendet die Aufgabe nicht.');
 note(s,23,'2 Termine');note(s,24,'Die Termine sind interne Planung von Nora Bergmann am 06.10.2026, keine gesetzlichen Fristen.');
 note(s,26,'3 Entscheidung');note(s,27,'Die Zeilensumme zählt Aufgaben. Auch null offene Aufgaben erzeugen keine rechtliche Betriebsfreigabe.');
 note(s,29,'Eine Freigabe benötigt eine eigene datierte Entscheidung mit Umfang, Voraussetzungen und Unterschrift.');
 await finish(w,38,'Massnahmen_Freigaben',[['Maßnahmen','A1:G30']],[{sheet:'Maßnahmen',cell:'D8',value:'Ja',outSheet:'Maßnahmen',outCell:'G8',expected:'Nachweis fehlt'},{sheet:'Maßnahmen',cell:'E8',value:'Datei 11, Ziffer 3',outSheet:'Maßnahmen',outCell:'G8',expected:'Prüfung offen'}]);
}
{
 const w=Workbook.create();const s=base(w,'Nachweise','Lieferantenangaben und angeforderte Nachweise',['Vorhaben / Gegenstand','Angabe des Lieferanten','Vorliegender Stand','Nächste konkrete Rückfrage','Antwort erhalten'],[27,39,41,47,14],31);
 const rows=[['P01 / C5','Typ 1 vom 15.04.2026','Erstes Marktangebot soll 04.11.2025 sein.','Markteintritt, Systemumfang und Kundenkontrollen belegen.','Nein'],['P01 / Cloudort','Frankfurt','EU-Speicherung behauptet; US-Support optional.','Alle Speicher-, Wartungs- und Zugriffsländer benennen.','Nein'],['P01 / DPF','Registrierungsbeleg folgt','Kein überprüfbarer Zertifizierungsnachweis vorgelegt.','Genaue US-Rechtsperson, Eintrag, Status und Datenumfang.','Nein'],['P01 / Training','Produktverbesserung vorgesehen','Trainingsklausel streitig.','Datennutzung, Rechtsrolle und verbindlichen Ausschluss klären.','Nein'],['P02 / Medizinprodukt','Zweckbestimmung Version 5.0','Pilot soll Version 5.1 verwenden.','Passende Zweckbestimmung, Konformität und Änderungen belegen.','Nein'],['P02 / Wartung','Herstellerzugang vorgesehen','Ort, Zugriff und Protokolle noch nicht vollständig.','Personenrechte und zeitlich begrenzte Freischaltung darlegen.','Nein'],['P03 / Hochschule','Pseudonymisierter Export gewünscht','Empfängerumgebung und Vereinbarung offen.','Reidentifizierungswissen, Zwecke und Übermittlungsgrundlage klären.','Nein']];
 s.getRange('A8:E14').values=rows;s.getRange('A8:E14').format.rowHeight=76;s.getRange('E8:E14').format.fill='#fff2cc';s.getRange('E8:E14').dataValidation={rule:{type:'list',values:['Ja','Nein']}};
 c(s,'A5','Noch unbeantwortete Rückfragen');f(s,'E5','=COUNTIF(E8:E14,"<>Ja")');
 note(s,17,'1 Quellenstatus');note(s,18,'06 TOM/C5, 07 Unteraufträge, 17 Zweckbestimmung und 20 Technikabgleich. Ja zählt nur eine Antwort.');
 note(s,20,'2 C5');note(s,21,'Typ 1 nicht pauschal ablehnen: Paragraf 393 Absatz 4 SGB V enthält eine eng begrenzte 18-Monatsregel.');
 note(s,23,'Der konkrete Zeitraum und die übrigen gesetzlichen Voraussetzungen bleiben gesondert zu prüfen.');
 note(s,25,'3 Transfer');note(s,26,'EU-Speicherung beantwortet nicht die Frage nach Drittlandzugriffen. Ein TIA ist kein Ersatz für');note(s,27,'fehlende Zulässigkeit nach Paragraf 393 SGB V, Geheimnisschutz, DSGVO oder Krankenhausrecht.');
 const t=base(w,'Transferinventar','Zugriffswege und konkrete Transferfragen',['Weg','Exporteur / Empfänger','Datenzugriff','Nachweis / Mechanismus','Zusatzmaßnahmen','Stand'],[22,33,32,35,35,18],27);
 t.getRange('A8:F10').values=[['T01 P01 Support','Klinik / Sprechfeder Support Inc.','Möglicher Inhaltszugriff USA','DPF-Nachweis fehlt; Alternative nicht vereinbart','Kein pauschaler Dauerzugang; Freischaltung, Rollen, Logs','Offen'],['T02 P02 Wartung','Klinik / Radiaviso Medical GmbH','Zugriffsländer ungeklärt','Kein Drittlandweg allein aus Firmenname ableiten','Zeitfenster, Begleitung, Datenminimierung','Aufklärung'],['T03 P03 Hochschule','Klinik / Hochschule Saalebogen','Export pseudonymisierter Daten','Verantwortlichkeit und Weitergaben ungeklärt','Getrennter Schlüssel, Empfängeranalyse, Rückgaberegel','Aufklärung']];
 t.getRange('A8:F10').format.rowHeight=90;
 note(t,13,'1 Bearbeitung');note(t,14,'Jeden tatsächlichen Zugriff erfassen, auch Fernwartung und weitere Unterauftragnehmer.');
 note(t,16,'2 TIA');note(t,17,'Bei SCC: Rechtslage und Praxis, Datenzugriff, technische Zusatzmaßnahmen und Restbewertung dokumentieren.');
 note(t,19,'3 Status');note(t,20,'Ein behaupteter DPF-Eintrag ist noch kein geprüfter Angemessenheitsweg. Die konkrete Person prüfen.');
 note(t,22,'4 Abgrenzung');note(t,23,'Die Hochschulübermittlung kann schon im Inland unzulässig sein; Kapitel V löst diese Vorfrage nicht.');
 await finish(w,39,'Lieferanten_Transfernachweise',[['Nachweise','A1:E28'],['Transferinventar','A1:F24']],[{sheet:'Nachweise',cell:'E8',value:'Ja',outSheet:'Nachweise',outCell:'E5',expected:6}]);
}

{
 const w=Workbook.create();const b=base(w,'Pilotkosten','P01 Pilotbudget und interne Kapazität',['Position','Menge','Einheit','Satz EUR netto','Betrag EUR netto','Quelle / Rechenannahme'],[32,14,18,20,23,53],34);
 const rows=[['Lizenzen, zwei Monate',30,'Nutzer',89,'04 Angebot / 36 Planung: 89 EUR je Nutzer und Monat'],['Einrichtung',1,'Pauschale',4800,'04 Angebot / 36 Planung vom 06.10.2026'],['Interne Projektarbeit',48,'Stunden',65,'36 Lenkungsrunde: interner Satz, kein Lieferantenentgelt']];
 c(b,'A5','Anzahl Lizenzmonate');input(b,'B5',2);
 rows.forEach((r,i)=>{const a=8+i;c(b,'A'+a,r[0]);input(b,'B'+a,r[1]);c(b,'C'+a,r[2]);input(b,'D'+a,r[3]);c(b,'F'+a,r[4]);f(b,'E'+a,i===0?`=IF(COUNT(B8,D8,$B$5)<>3,"Eingabe fehlt",IF(OR(B8<0,B8<>INT(B8),D8<0,$B$5<=0,$B$5<>INT($B$5)),"Werte prüfen",ROUND(B8*D8*$B$5,2)))`:`=IF(COUNT(B${a},D${a})<>2,"Eingabe fehlt",IF(OR(B${a}<0,D${a}<0),"Werte prüfen",ROUND(B${a}*D${a},2)))`);});
 c(b,'A12','Externe Kosten netto');f(b,'E12','=IF(COUNT(E8:E9)<>2,"Eingabe fehlt",SUM(E8:E9))');
 c(b,'A13','Umsatzsteuersatz extern');input(b,'D13',.19);b.getRange('D13').setNumberFormat('0%');f(b,'E13','=IF(AND(ISNUMBER(E12),ISNUMBER(D13)),IF(OR(D13<0,D13>1),"Werte prüfen",ROUND(E12*D13,2)),"Eingabe fehlt")');
 c(b,'A14','Extern brutto / Zahlungsbudget');f(b,'E14','=IF(COUNT(E12:E13)<>2,"Eingabe fehlt",SUM(E12:E13))');
 c(b,'A16','Gesamter Ressourcenbedarf');f(b,'E16','=IF(COUNT(E10,E14)<>2,"Eingabe fehlt",E10+E14)');c(b,'F16','Externe Bruttokosten plus interne Vollkosten; kein Rechnungsbetrag.');
 b.getRange('D8:E16').setNumberFormat('[$-407]#,##0.00');b.getRange('D13').setNumberFormat('0%');b.getRange('A8:F10').format.rowHeight=50;b.getRange('A12:F16').format.rowHeight=34;b.getRange('A16:F16').format.fill='#e8edf0';
 note(b,19,'1 Ausgangsstand');note(b,20,'Diese Rechnung ist Noras vorläufige Planung, kein angenommenes Angebot und keine Bestellung.');
 note(b,22,'2 Eingaben');note(b,23,'Gelbe Felder ändern. Fehlende Werte lassen den betroffenen Betrag offen; eine echte Null bleibt null.');
 note(b,25,'3 Kostenumfang');note(b,26,'Nur P01. Radiologie, Forschung und Folgebetrieb sind nicht enthalten. Vorsteuerabzug wird nicht unterstellt.');
 note(b,28,'4 Zeitraum');note(b,29,'Zwei Abrechnungsmonate sind eine Budgetannahme für acht Pilotwochen, keine zugesagte Vertragslaufzeit.');
 const s=base(w,'Messplan','Acht Wochen P01: geplante Beobachtung',['Pilotwoche','Ziel Briefe','Geprüfte Briefe','Korrekturbedarf','Prüfzeit Minuten','Anteil korrigiert','Minuten je Brief'],[24,18,20,22,23,25,26],31);
 for(let i=0;i<8;i++){const a=i+8;c(s,'A'+a,`Woche ${i+1} nach Freigabe`);input(s,'B'+a,20);for(const col of ['C','D','E'])input(s,col+a,null);f(s,'F'+a,`=IF(COUNT(C${a}:D${a})<>2,"Noch keine Messung",IF(OR(C${a}<=0,C${a}<>INT(C${a}),D${a}<0,D${a}<>INT(D${a}),D${a}>C${a}),"Werte prüfen",D${a}/C${a}))`);f(s,'G'+a,`=IF(COUNT(C${a},E${a})<>2,"Noch keine Messung",IF(OR(C${a}<=0,C${a}<>INT(C${a}),E${a}<0),"Werte prüfen",E${a}/C${a}))`);}
 c(s,'A17','Geplante Briefe');f(s,'B17','=IF(COUNT(B8:B15)<>8,"Ziel fehlt",IF(OR(MIN(B8:B15)<0,B8<>INT(B8),B9<>INT(B9),B10<>INT(B10),B11<>INT(B11),B12<>INT(B12),B13<>INT(B13),B14<>INT(B14),B15<>INT(B15)),"Werte prüfen",SUM(B8:B15)))');
 c(s,'A18','Erfasste Wochen');f(s,'C18','=COUNT(C8:C15)');
 s.getRange('F8:F15').setNumberFormat('[$-407]0.0%');s.getRange('G8:G15').setNumberFormat('[$-407]0.0');s.getRange('A8:G15').format.rowHeight=42;
 note(s,21,'1 Messung beginnt nach Freigabe');note(s,22,'Am 06.10.2026 liegen keine Pilotmessungen vor. Leere Felder sind unbekannt, nicht null Fehler.');
 note(s,24,'2 Erfassung');note(s,25,'Gezählt werden geprüfte Entwürfe und davon Entwürfe mit Korrekturbedarf, nicht einzelne Fehler.');
 note(s,27,'3 Interpretation');note(s,28,'Prüfzeit umfasst ärztliche Kontrolle. Diese Kennzahlen belegen allein keine Sicherheit oder Zulässigkeit.');
 await finish(w,40,'Pilotmessung_Kosten',[['Pilotkosten','A1:F30'],['Messplan','A1:G29']],[{sheet:'Pilotkosten',cell:'B8',value:-1,outSheet:'Pilotkosten',outCell:'E8',expected:'Werte prüfen'},{sheet:'Pilotkosten',cell:'D13',value:1.2,outSheet:'Pilotkosten',outCell:'E13',expected:'Werte prüfen'},{sheet:'Messplan',cell:'B8',value:0.5,outSheet:'Messplan',outCell:'B17',expected:'Werte prüfen'},{sheet:'Pilotkosten',cell:'B8',value:31,outSheet:'Pilotkosten',outCell:'E14',expected:12278.42},{sheet:'Pilotkosten',cell:'B8',value:null,outSheet:'Pilotkosten',outCell:'E14',expected:'Eingabe fehlt'},{sheet:'Pilotkosten',cell:'B8',value:0,outSheet:'Pilotkosten',outCell:'E14',expected:5712},{sheet:'Messplan',cell:'C8',value:20,outSheet:'Messplan',outCell:'F8',expected:'Noch keine Messung'}]);
}
console.log(JSON.stringify({created:reports.map(r=>r.file),report:path.join(qa,'tabellen-pruefung.json')}));

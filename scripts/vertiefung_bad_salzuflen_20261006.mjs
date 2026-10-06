// Autor: Klotzkette. Neue Arbeitsmappen mit artifact-tool; Altdateien unverändert.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook, SpreadsheetFile}=await loadWorkbookRuntime();
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const dir=path.join(root,'testakten/bauwirtschaft-buchhaltung-bauunternehmen-bad-salzuflen');
const qa='/tmp/bauwirtschaft-vertiefung-20261006/bad';
await fs.mkdir(qa,{recursive:true});
const money='#,##0.00;(#,##0.00);"0.00"';
const col=i=>String.fromCharCode(65+i);
function sheet(w,name,title,headers,widths,note){
 const s=w.worksheets.add(name), end=col(headers.length-1);
 s.showGridLines=false;
 s.getRange('A1:'+end+'70').format={font:{name:'Arial',size:11},rowHeight:18,verticalAlignment:'center',wrapText:true};
 widths.forEach((v,i)=>s.getRange(col(i)+'1:'+col(i)+'70').format.columnWidth=v);
 s.getRange('A1:'+end+'2').merge(); s.getRange('A1').values=[[title]];
 s.getRange('A1').format.font={name:'Arial',size:16,bold:true,color:'#213E50'};
 s.getRange('A3:'+end+'3').merge();s.getRange('A3').values=[['Mertens GmbH | Nora Brinkmann | Stand 25.09.2026, 16:00 Uhr']];
 s.getRange('A4:'+end+'5').merge();s.getRange('A4').values=[[note]];
 s.getRange('A4').format.fill='#EDF3F5';
 s.getRange('A7:'+end+'7').values=[headers];s.getRange('A7:'+end+'7').format={fill:'#213E50',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:38,wrapText:true};
 s.freezePanes.freezeRows(7);return s;
}
function values(s,start,data){
 let r=start;
 for(const row of data){s.getRange('A'+r+':'+col(row.length-1)+r).values=[row];s.getRange('A'+r+':'+col(row.length-1)+r).format.rowHeight=26;
 row.forEach((v,i)=>{if(typeof v==='number')s.getRange(col(i)+r).format.font.color='#2457A7';});r++;}
}
function formula(s,c,f){s.getRange(c).formulas=[[f]];s.getRange(c).format.font.color=f.includes('!')?'#25704B':'#000000';}
function note(s,r,end,text){s.getRange('A'+r+':'+end+(r+1)).merge();s.getRange('A'+r).values=[[text]];s.getRange('A'+r).format.fill='#F0F3F4';}
function total(s,r,last,start=2){s.getRange('A'+r).values=[['Summe']];for(let i=start;i<=last;i++)formula(s,col(i)+r,'=SUM('+col(i)+'8:'+col(i)+(r-1)+')');s.getRange('A'+r+':'+col(last)+r).format.fill='#DCE9E9';s.getRange('A'+r+':'+col(last)+r).format.font.bold=true;}
async function save(w,name,ranges,checks){
 w.recalculate();
 const inspect=await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:50},maxChars:5000});
 await fs.writeFile(path.join(qa,name+'.errors.txt'),inspect.ndjson);
 for(const [sn,r]of ranges){
 const image=await w.render({sheetName:sn,range:r,scale:1.4,format:'png'});
 await fs.writeFile(path.join(qa,name+'-'+sn+'.png'),new Uint8Array(await image.arrayBuffer()));
 const evidence=await w.inspect({kind:'table',range:"'"+sn+"'!"+r,include:'values,formulas',tableMaxRows:65,tableMaxCols:10,maxChars:40000});
 await fs.writeFile(path.join(qa,name+'-'+sn+'.jsonl'),evidence.ndjson);
 }
 for(const [sn,c,v]of checks){
 const actual=w.worksheets.getItem(sn).getRange(c).values[0][0];
 if(typeof v==='number'?Math.abs(actual-v)>0.005:actual!==v)throw Error(name+' '+sn+'!'+c+': '+actual+' != '+v);
 }
 await(await SpreadsheetFile.exportXlsx(w)).save(path.join(dir,name));
 try{await fs.rename(path.join(dir,name+'.inspect.ndjson'),path.join(qa,name+'.export.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 console.log(name+': '+checks.length+' Ergebnisprüfungen bestanden');
}

const invoices=[
['RB-260901','Röding',24000,0,22800,'05 Rechnung; 03 Vertrag; 19/28 Betriebskonto','1.200 EUR Sicherheit bleiben offen; keine zusätzliche Kostenminderung.'],
['LB-260908','Lippe Baustoff',14280,1451.8,12828.2,'08 Rechnung; 11 Korrektur; 19/28 Betriebskonto','1.190 EUR Korrektur + 261,80 EUR Bruttoskonto. Kopie 09/12 nicht erneut buchen.'],
['WM-260915','Weser Miettechnik',2975,0,2975,'13 Rechnung; 14 Mietnachweis; 19/28 Konto','1.785 EUR weiterer Bankabgang unzugeordnet, siehe 29; nicht zusätzlich absetzen.'],
['ST-260922','Seidel Planung',2142,0,0,'15 Rechnung; 16 Rückfrage; 23 OPOS','Inhaltliche Freigabe ausstehend; kein Beleg für eine Zahlung.'],
['ST-260902','Steinwerk',2142,0,2142,'31 Rechnung; 57 Zuordnung; 68 Bestätigung','Teilbetrag aus Sammelzahlung EB-0916A.'],
['HB-260903','Holzhandel Bega',2856,238,2618,'32 Rechnung; 45 Korrektur; 67 Rücklieferbeleg','Korrektur HB-G260916 nur einmal ansetzen.'],
['EL-260904','Elektrohandel',892.5,0,892.5,'33 Rechnung; 48/49 Konto; 57 Zuordnung','Ausgeführte Zahlung vollständig zugeordnet.'],
['TB-260905','Trockenbau Vogt',4800,0,0,'34 Rechnung; 63 Aufmaß; 65 Rückfrage','Leistungsnachweis vorhanden; Bescheinigung/Jahresumfang zum Bauabzug offen.'],
['SA-260906','Sanitär Ahle',3200,0,0,'35 Rechnung; 64 Stunden; 66 Rückfrage','Kein Skonto oder Sicherheit vereinbart; steuerliche Unterlagen offen.'],
['MR-260907','Mietpark Rethmar',1071,0,500,'36 Rechnung; 59 Antwort; 60 Mietkarte','Teilzahlung 500 EUR; eigener Lieferant, keine Verrechnung mit Weser.'],
['GE-260908','Gerüst Exter',1309,0,1309,'37 Rechnung; 47 Leistungsregister; 57 Zuordnung','Vermietung ohne Aufbau; Rechnung ausgeglichen.'],
['EN-260909','Entsorgung',571.2,0,571.2,'38 Rechnung; 47 Leistungsregister; 57 Zuordnung','Entsorgung; keine zusätzliche Abbruchleistung angesetzt.'],
['TP-260910','Retzer Planung',1428,0,0,'39 Rechnung; 61 Prüfung; 62 Erklärung','15 Stunden; sachliche Freigabe noch ausstehend.'],
['ST-260911','Steinwerk',714,0,714,'40 Rechnung; 57 Zuordnung; 68 Bestätigung','Zweiter Teilbetrag der Sammelzahlung; Bankabgang nur einmal zählen.'],
['TR-260912','Transport Lemgo',499.8,0,499.8,'41 Rechnung; 48/49 Konto; 57 Zuordnung','Beleg und Zahlung zugeordnet.'],
['VW-260913','Vermessung',1130.5,59.5,1071,'42 Rechnung; 46 Korrektur; 57 Zuordnung','Korrektur VW-G260919 zu dieser Rechnung.'],
['MT-260914','Miettechnik Ravensberg',285.6,0,285.6,'43 Rechnung; 47 Leistungsregister; 57 Zuordnung','Trocknermiete Lage; eigener Lieferant.'],
['DZ-260915','Dachbaustoffe',1178.1,0,1178.1,'44 Rechnung; 48/49 Konto; 57 Zuordnung','Beleg und Zahlung zugeordnet.']
];
{
 const w=Workbook.create();
 const o=sheet(w,'Offene Posten','Rechnungen mit nachvollziehbarem Saldo',['Rechnung','Lieferant','Beleg EUR','Absetzung EUR','Zahlung EUR','Offen EUR'],[19,24,16,17,17,17],'Belegbetrag minus Rechnungskorrektur/Skonto minus zugeordnete Zahlung. Ein offener Betrag ist noch keine Zahlungsfreigabe.');
 values(o,8,invoices.map(i=>[...i.slice(0,5),null]));
 invoices.forEach((i,n)=>{const r=n+8;formula(o,'F'+r,'=IF(COUNT(C'+r+':E'+r+')=3,ROUND(C'+r+'-D'+r+'-E'+r+',2),"Angabe fehlt")');});
 total(o,26,5);for(const c of ['C','D','E','F'])formula(o,c+'26','=IF(COUNT('+c+'8:'+c+'25)=18,SUM('+c+'8:'+c+'25),"Angabe fehlt")');o.getRange('C8:F26').setNumberFormat(money);
 note(o,28,'F','Blau = belegte Eingabewerte; Schwarz = Rechnung. Absetzungen sind hier positive Abzugsbeträge. Der Belegweg erklärt jeden Ansatz.');
 note(o,31,'F','Röding: 1.200 EUR Sicherheit bleiben eine Verbindlichkeit. Weser: die ungeklärten 1.785 EUR sind kein Abzug in dieser Rechnungsliste.');
 note(o,34,'F','Diese Mappe ersetzt weder ein Hauptbuch noch die Zahlungsfreigabe. Ursprüngliche Arbeitsstände: 24, 25 und 55. Quellenangaben im zweiten Blatt.');
 const q=sheet(w,'Belegweg','Quellen und Bearbeitungsstand',['Rechnung','Belegnummern in der Akte','Verwendung im Saldo'],[21,43,46],'Alle Beträge in EUR. 18 verschiedene Rechnungen; drei Korrekturen. Mehrfach übermittelte Rechnungskopien bilden keinen neuen Vorgang.');
 values(q,8,invoices.map(i=>[i[0],i[5],i[6]]));q.getRange('A8:C25').format.rowHeight=44;
 note(q,26,'C','Belegnummer = Dateinamen-Präfix. Konto 471108: 19/28. Konto 471109: 48/49. Keine Umbuchung belegt.');
 await save(w,'72_Offene_Posten_mit_Belegweg.xlsx',[['Offene Posten','A1:F35'],['Belegweg','A1:C28']],[['Offene Posten','F26',13341],['Offene Posten','F17',571]]);
}
{
 const w=Workbook.create();
 const s=sheet(w,'Stunden','Auguststunden und Arbeitgeberkosten',['Personal','Projekt','Stunden','EUR / Std.','AG EUR','Brutto EUR','Kosten EUR'],[15,18,13,15,15,17,18],'Quelle 18: 70 Stunden je Person zu 30 EUR. Quelle 17/71: 440 EUR Arbeitgeberbelastung je Person. Keine individuelle Abgabenberechnung.');
 values(s,8,Array.from({length:10},(_,i)=>['P'+String(i+1).padStart(3,'0'),i<6?'BS26-01':'BS26-02',70,30,440,null,null]));
 for(let r=8;r<=17;r++){formula(s,'F'+r,'=IF(COUNT(C'+r+':D'+r+')=2,ROUND(C'+r+'*D'+r+',2),"Angabe fehlt")');formula(s,'G'+r,'=IF(COUNT(E'+r+':F'+r+')=2,SUM(E'+r+':F'+r+'),"Angabe fehlt")');}
 total(s,18,6);for(const c of ['C','E','F','G'])formula(s,c+'18','=IF(COUNT('+c+'8:'+c+'17)=10,SUM('+c+'8:'+c+'17),"Angabe fehlt")');s.getRange('D18').values=[[null]];s.getRange('C8:C18').setNumberFormat('0.00');s.getRange('D8:G18').setNumberFormat(money);
 note(s,20,'G','Kosten = Bruttolohn + Arbeitgeberbelastung. Stunden gehören in August 2026; Bankzahlungen erfolgten im September. Ein Zahlungsdatum erzeugt keinen zweiten Aufwand.');
 const a=sheet(w,'Abstimmung','Projektkosten und Geldabfluss',['Position','Stunden','Kosten / Betrag EUR','Quelle / Bedeutung'],[25,15,24,47],'Grün = Übernahme aus Blatt Stunden. Die nachfolgenden Bankbeträge stammen aus 19/28; Änderungen der Stunden ändern nicht automatisch den Kontoauszug.');
 values(a,8,[['BS26-01',null,null,'Sechs Personen; Werkstattanbau Fricke'],['BS26-02',null,null,'Vier Personen; Ladenfläche Lage'],['Kosten gesamt',null,null,'Verteilte Bruttolöhne und Arbeitgeberanteile'],['Nettolohn',null,15700,'23.09.2026 | Betriebskonto'],['Sozialversicherung',null,7700,'24.09.2026 | enthält 3.300 AN + 4.400 AG'],['Lohnsteuer',null,2000,'24.09.2026 | Betriebskonto'],['Bank gesamt',null,null,'Summe der drei ausgeführten Zahlungen'],['Differenz',null,null,'Kosten minus Bank; Abweichungen aufklären']]);
 for(let r=8;r<=9;r++){formula(a,'B'+r,'=IF(COUNT(Stunden!$C$8:$C$17)=10,SUMIF(Stunden!$B$8:$B$17,A'+r+',Stunden!$C$8:$C$17),"Angabe fehlt")');formula(a,'C'+r,'=IF(AND(COUNT(Stunden!$G$8:$G$17)=10,COUNTIF(Stunden!$B$8:$B$17,"BS26-01")+COUNTIF(Stunden!$B$8:$B$17,"BS26-02")=10),SUMIF(Stunden!$B$8:$B$17,A'+r+',Stunden!$G$8:$G$17),"Angabe fehlt")');}
 formula(a,'B10','=IF(COUNT(B8:B9)=2,SUM(B8:B9),"Angabe fehlt")');formula(a,'C10','=IF(COUNT(C8:C9)=2,SUM(C8:C9),"Angabe fehlt")');formula(a,'C14','=IF(COUNT(C11:C13)=3,SUM(C11:C13),"Angabe fehlt")');formula(a,'C15','=IF(AND(ISNUMBER(C10),ISNUMBER(C14)),C10-C14,"Angabe fehlt")');
 a.getRange('C8:C15').setNumberFormat(money);a.getRange('A8:D15').format.rowHeight=35;
 note(a,17,'D','Der Arbeitgeberanteil steckt bereits in der Sozialversicherungszahlung. Ihn zur Banksumme nochmals zu addieren würde denselben Abfluss doppelt zählen.');
 note(a,20,'D','Änderungshinweis: Neue Stunden oder Korrekturen nur mit Nachweis übernehmen. Eine Differenz beweist noch keinen Fehler der Lohnabrechnung. Rückfrage an Sabine Krüger (Beleg 71).');
 await save(w,'73_Projektstunden_mit_Kostenbruecke.xlsx',[['Stunden','A1:G21'],['Abstimmung','A1:D21']],[['Stunden','G18',25400],['Abstimmung','C8',15240],['Abstimmung','C9',10160],['Abstimmung','C15',0]]);
}
{
 const w=Workbook.create();
 const s=sheet(w,'Mietansatz','Miete nach Leistung und Lieferant',['Beleg / Gerät','Projekt','Tage','EUR / Tag','Netto EUR','USt EUR','Brutto EUR'],[25,15,11,15,16,15,17],'Die Tagespreise stammen aus den Rechnungen und Mietnachweisen. Geräte wurden ohne Bediener, das Gerüst ohne Aufbau überlassen. Quellen im zweiten Blatt.');
 values(s,8,[['WM Rüttelplatte','BS26-01',10,150,null,null,null],['WM Verdichter','BS26-02',10,100,null,null,null],['MR Minibagger','BS26-01',6,150,null,null,null],['GE Gerüst','BS26-01',20,55,null,null,null],['MT Trockner','BS26-02',4,60,null,null,null]]);
 for(let r=8;r<=12;r++){formula(s,'E'+r,'=IF(COUNT(C'+r+':D'+r+')=2,ROUND(C'+r+'*D'+r+',2),"Angabe fehlt")');formula(s,'F'+r,'=IF(ISNUMBER(E'+r+'),ROUND(E'+r+'*0.19,2),"Angabe fehlt")');formula(s,'G'+r,'=IF(COUNT(E'+r+':F'+r+')=2,SUM(E'+r+':F'+r+'),"Angabe fehlt")');}
 total(s,13,6,4);for(const c of ['E','F','G'])formula(s,c+'13','=IF(COUNT('+c+'8:'+c+'12)=5,SUM('+c+'8:'+c+'12),"Angabe fehlt")');s.getRange('D8:G13').setNumberFormat(money);
 note(s,15,'G','Bei Weser sind zehn berechnete Tage je Gerät innerhalb des Mietzeitraums 01.–14.09. angesetzt. Die 14 Kalendertage werden nicht als neue Rechnungsmenge verwendet.');
 note(s,18,'G','Die Netto-Tagesmiete des Gerüsts wird aus 1.100 EUR / 20 Tagen hergeleitet. Mengenänderungen wirken nur auf die Rechnungssimulation, nicht auf historische Bankwerte.');
 const z=sheet(w,'Zahlungsweg','Zuordnung der Mietzahlungen',['Rechnung','Konto','Beleg EUR','Zahlung EUR','Offen EUR','Quelle / Status'],[19,14,16,16,16,34],'Rechnungen und Zahlungen getrennt prüfen. Blau sind die ausgeführten Zahlungen aus den Kontoauszügen; Grün übernimmt die Mietberechnung.');
 values(z,8,[['WM-260915','471108',null,2975,null,'13/14; Zahlung 19/28'],['MR-260907','471109',null,500,null,'36; Nachweise 59/60'],['GE-260908','471109',null,1309,null,'37; Register 47; 57'],['MT-260914','471109',null,285.6,null,'43; Register 47; 57']]);
 formula(z,'C8','=IF(COUNT(Mietansatz!G8:G9)=2,SUM(Mietansatz!G8:G9),"Angabe fehlt")');formula(z,'C9','=Mietansatz!G10');formula(z,'C10','=Mietansatz!G11');formula(z,'C11','=Mietansatz!G12');
 for(let r=8;r<=11;r++)formula(z,'E'+r,'=IF(COUNT(C'+r+':D'+r+')=2,C'+r+'-D'+r+',"Angabe fehlt")');total(z,12,4);for(const c of ['C','D','E'])formula(z,c+'12','=IF(COUNT('+c+'8:'+c+'11)=4,SUM('+c+'8:'+c+'11),"Angabe fehlt")');z.getRange('C8:E12').setNumberFormat(money);
 note(z,14,'F','Zusätzlicher Abgang: 24.09., Konto 471108, 1.785 EUR an Weser. Kein bestätigter Rechnungsbezug. Beleg 29 hält die Rückfrage offen; nicht mit Rethmar verrechnen.');
 note(z,17,'F','59/60 bestätigt 571 EUR Restforderung Rethmar. Ein gleichlautendes Wort im Banktext ist kein Kreditorenabgleich. Die neue Mietkarte ist keine zweite Rechnung.');
 await save(w,'74_Mietbelege_und_Zahlungszuordnung.xlsx',[['Mietansatz','A1:G19'],['Zahlungsweg','A1:F18']],[['Zahlungsweg','E9',571],['Zahlungsweg','E12',571],['Mietansatz','G13',5640.6]]);
}
{
 const w=Workbook.create();
 const s=sheet(w,'Zahlvorschlag','Nächster Zahlungslauf zur Bearbeitung',['Rechnung','Konto','Freigabe','Lieferant EUR','Steuer EUR','Abfluss EUR'],[20,15,23,18,18,19],'Keine Freigabe erteilt (Beleg 70). D/E erst nach Prüfung ausfüllen. 0 bedeutet ausdrücklich kein Abfluss; leer bedeutet unbekannt. F wird erst bei vollständiger Freigabe berechnet.');
 values(s,8,[['ST-260922','471108','offen',null,null,null],['TB-260905','471109','offen',null,null,null],['SA-260906','471109','offen',null,null,null],['MR-260907','471109','offen',null,null,null],['TP-260910','471109','offen',null,null,null]]);
 for(let r=8;r<=12;r++){formula(s,'F'+r,'=IF(AND(C'+r+'="freigegeben",ISNUMBER(D'+r+'),ISNUMBER(E'+r+'),D'+r+'>=0,E'+r+'>=0),SUM(D'+r+':E'+r+'),"offen")');}
 s.getRange('C8:C12').dataValidation={rule:{type:'list',values:['offen','freigegeben','zurückgestellt']}};
 s.getRange('B8:B12').dataValidation={rule:{type:'list',values:['471108','471109']}};
 s.getRange('D8:F12').setNumberFormat(money);
 note(s,14,'F','Zurückgestellt bleibt offen für die Gesamtplanung. Für einen ausdrücklich ohne Zahlung geprüften Vorgang beide Beträge mit 0 und den Freigabenachweis dokumentieren.');
 note(s,17,'F','Eine gesonderte Steuerzahlung ist ein tatsächlicher weiterer Geldabfluss, kein zweiter Rechnungsbetrag. Bauabzug und Umsatzsteuerbehandlung getrennt prüfen; keine automatische Steuerberechnung.');
 note(s,20,'F','Freigabenachweis mit Name, Datum und Quelle im Blatt Belegweg ergänzen. Die Arbeitsmappe führt keine Überweisung aus. Historische Sicherheiten sind hier nicht als fällige Zahlung vorgeschlagen.');
 const k=sheet(w,'Konten','Kontengetrennte Liquiditätsvorschau',['Konto','Bestand EUR','Geplanter Abfluss EUR','Restbestand EUR'],[22,26,31,32],'Bestände laut 28/49; kein Live-Bankabruf. Solange eine Zeile dieses Kontos offen ist, bleiben Abfluss und Vorschau offen. Keine stillschweigende Nullannahme.');
 values(k,8,[['471108',79211.8,null,null],['471109',38218.8,null,null]]);
 for(let r=8;r<=9;r++){
 formula(k,'C'+r,'=IF(COUNTIF(Zahlvorschlag!$B$8:$B$12,"471108")+COUNTIF(Zahlvorschlag!$B$8:$B$12,"471109")<>5,"Kontozuordnung offen",IF(COUNTIFS(Zahlvorschlag!$B$8:$B$12,A'+r+',Zahlvorschlag!$F$8:$F$12,"offen")>0,"offen",SUMIF(Zahlvorschlag!$B$8:$B$12,A'+r+',Zahlvorschlag!$F$8:$F$12)))');
 formula(k,'D'+r,'=IF(ISNUMBER(C'+r+'),B'+r+'-C'+r+',"offen")');}
 k.getRange('B8:D9').setNumberFormat(money);
 note(k,11,'D','Bestände wurden am 25.09.2026 um 16:00 Uhr festgehalten. Ein späterer Umsatz, eine Rückzahlung oder Umbuchung benötigt einen neuen Bankbeleg.');
 note(k,14,'D','Beispiel zum Bearbeiten einer Kopie: Rethmar nach Freigabe mit 571 EUR und 0 EUR gesonderter Steuerzahlung eintragen. Die anderen ungeklärten Zeilen bleiben sichtbar offen.');
 const q=sheet(w,'Belegweg','Freigaben und noch fehlende Unterlagen',['Rechnung','Offen EUR','Anforderung / Nachweis','Freigabevermerk'],[20,17,48,28],'Quelle 70: kein ausgeführter Auftrag. Die offene Verbindlichkeit dient nur dem Abgleich; sie wird nicht automatisch in den Zahlungsbetrag kopiert.');
 values(q,8,[['ST-260922',2142,'15/16: sachliche Freigabe Jan Hellwig fehlt.',null],['TB-260905',4800,'34/63/65: Bescheinigung und Jahresumfang zum Bauabzug offen.',null],['SA-260906',3200,'35/64/66: Bescheinigung und Jahresumfang zum Bauabzug offen.',null],['MR-260907',571,'36/59/60: Rest bestätigt; Geschäftsführung entscheidet über Lauf.',null],['TP-260910',1428,'39/61/62: Maßbezug und Türdarstellung noch zu klären.',null]]);
 q.getRange('A8:D12').format.rowHeight=67;q.getRange('B8:B12').setNumberFormat(money);
 note(q,14,'D','Nachweis bitte vollständig: freigebende Person, Zeitpunkt, Umfang und Quelldokument. Die Statusauswahl allein belegt keine erteilte Vollmacht oder Bankfreigabe.');
 await save(w,'75_Zahlungsplanung_mit_Freigaben.xlsx',[['Zahlvorschlag','A1:F21'],['Konten','A1:D15'],['Belegweg','A1:D15']],[['Zahlvorschlag','F8','offen'],['Konten','D8','offen'],['Konten','D9','offen']]);
}

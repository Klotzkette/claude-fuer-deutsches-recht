/** Formelbasierte Rechenbelege zu drei fiktiven Akten. Keine Rechtsfolgenbewertung. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook,SpreadsheetFile,requireRuntime}=await loadWorkbookRuntime(['jszip']);
const JSZip=requireRuntime('jszip');
const root=process.argv[2]??path.resolve('testakten');
const qa=process.argv[3]??'/tmp/gs-nachtrag-qa/sheets';
await fs.mkdir(qa,{recursive:true});
const euro='#,##0.00;(#,##0.00);"-"';
const all=[];const checks=[];
const excelDate=s=>Date.parse(s+'T00:00:00Z')/86400000+25569;
function sheet(wb,name,title,widths,rows){
 const s=wb.worksheets.add(name);s.showGridLines=false;
 s.getRangeByIndexes(0,0,rows,widths.length).format={font:{name:'Arial',size:10,color:'#222222'},verticalAlignment:'center',rowHeight:18};
 widths.forEach((v,i)=>s.getRangeByIndexes(0,i,rows,1).format.columnWidth=v);
 s.getRange('A2').values=[[title]];s.getRange('A2').format={font:{name:'Arial',size:14,bold:true},rowHeight:30};
 s.getRange('A3').values=[['Stand 08.10.2026. Blaue Zahlen: Eingaben. Schwarze Zahlen: Formeln. Belegpfade relativ zum Ordner.']];
 s.getRange('A3').format={font:{name:'Arial',size:10,color:'#5A5A5A'},rowHeight:21};
 all.push({wb,s,rows,range:`A1:${String.fromCharCode(64+widths.length)}${rows}`});return s;
}
function header(s,r,labels){s.getRangeByIndexes(r-1,0,1,labels.length).values=[labels];s.getRangeByIndexes(r-1,0,1,labels.length).format={fill:'#E4E8ED',font:{name:'Arial',size:10,bold:true},wrapText:true,horizontalAlignment:'center',rowHeight:26};}
function val(s,a,v){s.getRange(a).values=[[v]];if(typeof v==='number')s.getRange(a).format.font.color='#1D4ED8';}
function formula(s,a,v){s.getRange(a).formulas=[[v]];s.getRange(a).format.font.color=v.includes('!')?'#166534':'#111111';}
function note(s,r,v){val(s,`A${r}`,v);s.getRange(`A${r}`).format={font:{name:'Arial',size:10,color:'#4B5563'},wrapText:false,rowHeight:18};}
function total(s,r){s.getRange(`A${r}:E${r}`).format={fill:'#F1F3F5',font:{bold:true},rowHeight:24,borders:{top:{style:'thin',color:'#929AA5'}}};}
function control(wb,s,a,expected,label){const actual=s.getRange(a).values[0][0];if(typeof actual!=='number'||Math.abs(actual-expected)>0.00001)throw new Error(`${s.name}!${a}=${actual}; erwartet ${expected}`);checks.push({case:label,sheet:s.name,cell:a,actual,expected});}
function numeric(s,range){s.getRange(range).setNumberFormat(euro);s.getRange(range).format.horizontalAlignment='right';}

const berlin=Workbook.create();
const br=sheet(berlin,'Rechnung','Lindenhof Rechnung und rechnerische Varianten',[35,17,17,17,46],30);
header(br,5,['Position','Netto EUR','USt Satz','Rechnerisch brutto EUR','Beleg']);
br.getRange('A6:E9').values=[['Sechs Geräte',11700,0.19,null,'../10_Rechnung_SBS_K6.pdf'],['Kabel und Stecker',1900,0.19,null,'../10_Rechnung_SBS_K6.pdf'],['Transport und Einbauhilfe',1000,0.19,null,'../10_Rechnung_SBS_K6.pdf'],['Express und Zusatzarbeit',862.18,0.19,null,'../10_Rechnung_SBS_K6.pdf']];
for(let r=6;r<=9;r++)formula(br,`D${r}`,`=ROUND(B${r}*(1+C${r}),2)`);
val(br,'A10','Rechnung laut Beleg');formula(br,'B10','=SUM(B6:B9)');formula(br,'D10','=B10+B11');total(br,10);
val(br,'A11','Umsatzsteuer laut Beleg');val(br,'B11',2937.82);val(br,'E11','../10_Rechnung_SBS_K6.pdf');
val(br,'A12','USt rechnerisch / Differenz');formula(br,'B12','=ROUND(B10*C6,2)');formula(br,'D12','=B11-B12');
val(br,'A13','Erste Preisangabe brutto EUR');val(br,'B13',14900);val(br,'E13','../11_Nachrichten_K7.txt');
val(br,'A14','Differenz zur Endrechnung');formula(br,'D14','=D10-B13');
header(br,17,['Rechenannahme','Eingabe','Einheit','Ergebnis EUR','Quelle und Bedeutung']);
br.getRange('A18:E20').values=[['Zu untersuchende Stückzahl',1,'Stück',null,'Annahme für Preisrechnung; kein Befund'],['Rechnungspreis je Gerät',1950,'EUR netto',null,'../10_Rechnung_SBS_K6.pdf'],['Umsatzsteuersatz',0.19,'Satz',null,'../10_Rechnung_SBS_K6.pdf']];
val(br,'A21','Rechenbetrag netto');formula(br,'D21','=B18*B19');
val(br,'A22','Rechenbetrag brutto');formula(br,'D22','=ROUND(D21*(1+B20),2)');
note(br,24,'Die Variante ist keine Gutschrift und kein festgestellter Zahlungsanspruch. Eingabe B18 ist frei änderbar.');
note(br,25,'Bankzahlung: 18.400 EUR am 21.08.2026, 07:43 Uhr; Quelle ../17_Bankprotokoll.csv, B-0821.');
note(br,26,'Eine Lieferung, interne Freigabe oder Genehmigung ergibt sich nicht allein aus der Bankzahlung.');
note(br,27,'N03_Seidel_Kalkulationsnachtrag.docx: 360 EUR Stunden und 502,18 EUR Rest sind Teile der Expressposition.');
note(br,28,'Die alte Preisangabe war brutto; sie wird nur mit der Brutto-Endrechnung verglichen.');
note(br,29,'D12: 0,01 EUR Abweichung zwischen USt laut Rechnung und 19-Prozent-Rechnung. Der Altbeleg bleibt unverändert.');
numeric(br,'B6:B14');numeric(br,'B19');numeric(br,'D6:D22');br.getRange('C6:C9').setNumberFormat('0.0%');br.getRange('B20').setNumberFormat('0.0%');br.getRange('B18').setNumberFormat('0');
br.getRange('B6:C9').format.font.color='#1D4ED8';br.getRange('B18:B20').format.font.color='#1D4ED8';
br.getRange('E5:E22').format.wrapText=true;br.getRange('A18:E20').format.rowHeight=30;
const bg=sheet(berlin,'Geräte','Lindenhof Gerätezuordnung nach späteren Aussagen',[10,17,26,39,40],17);
header(bg,5,['Pos.','Seriennummer','Zeitnaher Beleg','Spätere Beobachtung','Quelle']);
bg.getRange('A6:E11').values=[
 [1,'L-402','Wareneingang 24.08.','Am 06.10. eingebaut gesehen','../14_Wareneingang_Lindenhof.docx; N01_Ergaenzung_Brandt.docx'],
 [2,'L-407','Wareneingang 24.08.','Am 06.10. eingebaut gesehen','../14_Wareneingang_Lindenhof.docx; N01_Ergaenzung_Brandt.docx'],
 [3,'L-411','Wareneingang 24.08.','Am 06.10. eingebaut gesehen','../14_Wareneingang_Lindenhof.docx; N01_Ergaenzung_Brandt.docx'],
 [4,'L-419','Wareneingang 24.08.','Am 06.10. eingebaut gesehen','../14_Wareneingang_Lindenhof.docx; N01_Ergaenzung_Brandt.docx'],
 [5,'L-433','Notiz am 25.08. zum 22.08.','Riedel nennt ein gesehenes Gerät','N02_Betriebsbuch_Riedel.docx'],
 [6,'Zuordnung offen','Rechnung nennt sechs Geräte','L-427 war 2025 vorhanden; Platinenarbeit laut Seidel möglich','N02_Betriebsbuch_Riedel.docx; N03_Seidel_Kalkulationsnachtrag.docx']];
bg.getRange('A6:E11').format={wrapText:true,rowHeight:42};
note(bg,13,'Zahlungseingänge des Kunden über 37.000 EUR belegen den Gesamtauftrag, nicht sechs neu gelieferte Geräte.');
note(bg,14,'Kontrollorte: Werkstatt am 24. August; Technikraum am 6. Oktober. Die Zeitpunkte sind nicht austauschbar.');
note(bg,15,'Quellenpfade gelten relativ zu diesem Nachtragsordner. Die Erstbelege liegen eine Ebene darüber.');
berlin.recalculate();control(berlin,br,'D10',18400,'Berlin');control(berlin,br,'B10',15462.18,'Berlin');control(berlin,br,'B11',2937.82,'Berlin');control(berlin,br,'B12',2937.81,'Berlin rechnerische USt');control(berlin,br,'D12',0.01,'Berlin Altbeleg Rundungsabweichung');control(berlin,br,'D14',3500,'Berlin');control(berlin,br,'D22',2320.5,'Berlin');
val(br,'B18',0);berlin.recalculate();control(berlin,br,'D22',0,'Berlin Null Stück');val(br,'B18',2);berlin.recalculate();control(berlin,br,'D22',4641,'Berlin Zwei Stück');val(br,'B18',1);

const munich=Workbook.create();
const mk=sheet(munich,'Kapital','Isarwinkel Kapital und Verhandlungsmehrheiten',[35,21,23,20,33],32);
header(mk,5,['Beteiligter','Bisher EUR','Neu EUR','Danach EUR','Danach Anteil']);
mk.getRange('A6:E8').values=[['Hildegard Steinlechner',15000,0,null,null],['Quirin Rottmayer',10000,0,null,null],['Albrecht Vogl',0,6250,null,null]];
for(let r=6;r<=8;r++){formula(mk,`D${r}`,`=B${r}+C${r}`);formula(mk,`E${r}`,`=D${r}/$D$9`);}
val(mk,'A9','Summe');for(const c of ['B','C','D','E'])formula(mk,`${c}9`,`=SUM(${c}6:${c}8)`);total(mk,9);
val(mk,'A12','Vogl Zahlungsvorschlag EUR');val(mk,'B12',200000);
val(mk,'A13','Davon neues Stammkapital');formula(mk,'B13','=C8');
val(mk,'A14','Davon Aufgeld');formula(mk,'B14','=B12-B13');
val(mk,'A15','Zahlung an Altgesellschafter');val(mk,'B15',0);
val(mk,'A18','Vogls Schwelle am 08.10.');val(mk,'B18',0.85);val(mk,'C18','Gesamtes Stammkapital');
header(mk,20,['Kombination','Anteil zusammen','Abstand zu Schwelle','Bedeutung','Quelle']);
mk.getRange('A21:E23').values=[['Hildegard und Quirin',null,null,'Nur Rechenvergleich','N09_Vogl_Position.eml'],['Hildegard und Vogl',null,null,'Keine Abstimmung','N06_Vogl_Anmerkungen.docx'],['Quirin und Vogl',null,null,'Kein Vertragsschluss','N01_Gespraech_05_Oktober.docx']];
formula(mk,'B21','=E6+E7');formula(mk,'B22','=E6+E8');formula(mk,'B23','=E7+E8');
for(let r=21;r<=23;r++)formula(mk,`C${r}`,`=B${r}-$B$18`);
note(mk,26,'Stammkapitalquelle: ../03_Gesellschafterliste.docx. Neue Einlage: N01_Gespraech_05_Oktober.docx.');
note(mk,27,'Die Zahlung von 200.000 EUR ist vorgeschlagen und noch nicht erfolgt; kein Anteilskauf von den Gründern.');
note(mk,28,'85 Prozent sind Vogls Verhandlungswunsch vom 8. Oktober, bezogen auf das gesamte Stammkapital.');
note(mk,29,'Kein Satzungsbeschluss, kein Vollzug und keine rechtliche Prüfung von Zustimmung oder Stimmverbot.');
numeric(mk,'B6:D15');mk.getRange('E6:E9').setNumberFormat('0.0%');mk.getRange('B18').setNumberFormat('0.0%');mk.getRange('B21:C23').setNumberFormat('0.0%');mk.getRange('B6:C8').format.font.color='#1D4ED8';
mk.getRange('C18:E23').format.wrapText=true;mk.getRange('A21:E23').format.rowHeight=30;
const mz=sheet(munich,'Zahlungen','Isarwinkel Zahlungen und offene Bestellung',[30,20,21,21,40],31);
header(mz,5,['Datum oder Position','Eingang EUR','Ausgang EUR','Saldo EUR','Beleg']);
mz.getRange('A6:E10').values=[['30.09.2026 Anfang',null,null,86200,'../17_Budgetnotiz_Ottmar.docx'],[excelDate('2026-10-02'),0,6400,null,'N03_Ottmar_Zahlungsstand.docx'],[excelDate('2026-10-05'),0,1900,null,'N03_Ottmar_Zahlungsstand.docx'],[excelDate('2026-10-06'),0,9800,null,'N03_Ottmar_Zahlungsstand.docx'],[excelDate('2026-10-07'),5474,0,null,'N03_Ottmar_Zahlungsstand.docx']];
for(let r=7;r<=10;r++)formula(mz,`D${r}`,`=D${r-1}+B${r}-C${r}`);
val(mz,'A11','Stand 07.10.2026');formula(mz,'D11','=D10');total(mz,11);
header(mz,14,['Position','Gesamt EUR','Bezahlt EUR','Rest EUR','Quelle oder Stand']);
mz.getRange('A15:E17').values=[['Material aus September',21800,9800,null,'N03_Ottmar_Zahlungsstand.docx'],['Prüfstand brutto',142800,35700,null,'../12_Pruefstand_Bestellung.pdf'],['Neue Investorenzahlung',200000,0,null,'Vorschlag, kein fälliger Debitor']];
formula(mz,'C15','=C9');
for(let r=15;r<=17;r++)formula(mz,`D${r}`,`=B${r}-C${r}`);
header(mz,20,['Noch nicht beauftragt','Netto EUR','USt Satz','Brutto EUR','Beleg und Bedingung']);
mz.getRange('A21:E22').values=[['Ersatzteillager',28000,0.19,null,'N03_Ottmar_Zahlungsstand.docx'],['Horns Zusatzrechte',2400,0.19,null,'N04_Horn_Zusatzangebot.docx']];
for(let r=21;r<=22;r++)formula(mz,`D${r}`,`=ROUND(B${r}*(1+C${r}),2)`);
note(mz,25,'Anzahlung Prüfstand am 18.09. bereits im Anfangsbestand enthalten; nicht erneut vom Bankstand abgezogen.');
note(mz,26,'Prüfstandrest nach Lieferung, Inbetriebnahme und Rechnung; Plantermin 16.11.2026, keine neue Fälligkeit.');
note(mz,27,'Die Linie von 80.000 EUR ist ungezogen und kein Bankguthaben. Quelle: N11_Bank_Stand.eml.');
note(mz,28,'Die Tabelle ist ein Belegabgleich; Oktoberlöhne, Steuern und weitere Zahlungen bilden keine Vollplanung.');
note(mz,29,'Materialrest und Vorschläge werden nicht zu einer scheinbar vollständigen Liquiditätslücke addiert.');
mz.getRange('A7:A10').setNumberFormat('dd.mm.yyyy');numeric(mz,'B6:D17');numeric(mz,'B21:B22');numeric(mz,'D21:D22');mz.getRange('C21:C22').setNumberFormat('0.0%');
mz.getRange('E5:E22').format.wrapText=true;mz.getRange('A6:E10').format.rowHeight=24;mz.getRange('A15:E17').format.rowHeight=30;
munich.recalculate();control(munich,mk,'D9',31250,'München');control(munich,mk,'E6',0.48,'München');control(munich,mk,'E7',0.32,'München');control(munich,mk,'E8',0.2,'München');control(munich,mk,'B14',193750,'München');control(munich,mk,'B21',0.8,'München');control(munich,mz,'D11',73574,'München');control(munich,mz,'D15',12000,'München');control(munich,mz,'D16',107100,'München');
val(mk,'C8',12500);munich.recalculate();control(munich,mk,'D9',37500,'München alternative Einlage');control(munich,mk,'B14',187500,'München alternatives Aufgeld');val(mk,'C8',6250);
val(mz,'C9',0);munich.recalculate();control(munich,mz,'D11',83374,'München ohne Materialzahlung');control(munich,mz,'D15',21800,'München Materialrest ohne Zahlung');val(mz,'C9',9800);

const zink=Workbook.create();
const zb=sheet(zink,'Bank und OP','Zink und Zunder Fortschreibung der Belege',[34,19,19,19,41],31);
header(zb,5,['Datum oder Position','Eingang EUR','Ausgang EUR','Saldo EUR','Beleg']);
zb.getRange('A6:E10').values=[['30.09.2026 Anfang',null,null,25000,'../37_Finanzuebersicht.xlsx'],[excelDate('2026-10-01'),0,3200,null,'N01_Gundula_Bank_und_OP.docx'],[excelDate('2026-10-02'),0,12000,null,'N01_Gundula_Bank_und_OP.docx'],[excelDate('2026-10-05'),18000,0,null,'N01_Gundula_Bank_und_OP.docx'],[excelDate('2026-10-06'),0,8000,null,'N01_Gundula_Bank_und_OP.docx']];
for(let r=7;r<=10;r++)formula(zb,`D${r}`,`=D${r-1}+B${r}-C${r}`);
val(zb,'A11','Stand 07.10.2026');formula(zb,'D11','=D10');total(zb,11);
header(zb,14,['OP aus Septemberliste','Ursprung EUR','Gezahlt EUR','Rest EUR','Quelle / Fälligkeit']);
zb.getRange('A15:E21').values=[['Stahlkontor STA-0821',12000,null,null,'N01; ursprünglich 20.09.'],['Augustmiete Rest',3200,null,null,'N01; ursprünglich 05.08.'],['Steuerbüro STB-0920',2800,0,null,'../37_Finanzuebersicht.xlsx'],['Energie EN-0722',1600,0,null,'../37_Finanzuebersicht.xlsx'],['Septemberlöhne Rest',12000,null,null,'N01; ursprünglich 30.09.'],['Beschläge BE-0820',18400,0,null,'../37_Finanzuebersicht.xlsx'],['Maschinen MA-0915',25000,0,null,'../37_Finanzuebersicht.xlsx; 15.10.']];
formula(zb,'C15','=C10');formula(zb,'C16','=C7');formula(zb,'C19','=C8');
for(let r=15;r<=21;r++)formula(zb,`D${r}`,`=B${r}-C${r}`);
val(zb,'A23','Davon alte fällige Posten');formula(zb,'D23','=SUM(D15:D20)');
val(zb,'A24','Mit Maschinenrechnung');formula(zb,'D24','=SUM(D15:D21)');total(zb,24);
note(zb,27,'N01 bezeichnet N01_Gundula_Bank_und_OP.docx. Oktoberbelege sind noch nicht vollständig ergänzt.');
note(zb,28,'Bezahlte Teilbeträge sind mit den Bankzeilen verknüpft; Septembertilgung von 30.000 EUR ist im Anfang enthalten.');
note(zb,29,'Weder Stundungen noch zusätzliche Mittel sind bestätigt. Diese Tabelle ist keine vollständige Finanzplanung.');
zb.getRange('A7:A10').setNumberFormat('dd.mm.yyyy');numeric(zb,'B6:D24');zb.getRange('E5:E21').format.wrapText=true;zb.getRange('A6:E10').format.rowHeight=21;zb.getRange('A15:E21').format.rowHeight=24;
const zd=sheet(zink,'Darlehen und Wünsche','Zink und Zunder Darlehen und Preiswünsche',[34,20,21,20,37],28);
header(zd,5,['Darlehensgeber','Ausgezahlt EUR','Tilgung EUR','Rest EUR','Beleg']);
zd.getRange('A6:E7').values=[['Romy Yilmaz',60000,0,null,'../06_Darlehen_Romy_60000.docx'],['Kunibert Knopf',40000,30000,null,'../07_Darlehen_Kunibert_40000.docx']];
for(let r=6;r<=7;r++)formula(zd,`D${r}`,`=B${r}-C${r}`);
val(zd,'A8','Hauptforderung rechnerisch');formula(zd,'D8','=SUM(D6:D7)');total(zd,8);
note(zd,10,'Tilgung Knopf: ../10_Zahlungsnachweis_15_September.docx. Keine weitere Tilgung bis 07.10. gebucht.');
note(zd,11,'Zinsen sind nicht in den Hauptforderungen enthalten. Zinszahlung 2025 an Romy: 1.800 EUR, keine Tilgung.');
header(zd,14,['Gesprächsposition','Eingabe EUR','Einheit','Rechenwert EUR','Urheber und Beleg']);
zd.getRange('A15:E17').values=[['Hannas erster Gesamtpreis',150000,'alle Anteile',null,'N05_Hanna_Gespraech_06_Oktober.docx'],['Romys Wunsch Anteilspreis',60000,'nur ihr Anteil',null,'N05_Hanna_Gespraech_06_Oktober.docx'],['Romys Darlehenshauptbetrag',null,'getrennte Position',null,'Dar­lehen oben, keine Preisannahme']];
formula(zd,'B17','=D6');
val(zd,'A19','Romys zwei Positionen addiert');formula(zd,'D19','=SUM(B16:B17)');
val(zd,'A20','Romys bisherige Anteilquote');val(zd,'B20',0.35);
val(zd,'A21','Quote mal Hannas Gesprächszahl');formula(zd,'D21','=B15*B20');
note(zd,24,'Quote mal Gesprächszahl ergibt weder einen Verkehrswert noch eine Abfindung. Keine Einigung über einen Wert.');
note(zd,25,'N05: Hanna sagt weder Darlehensübernahme noch Abfindungsfinanzierung zu. Forderungen und Wünsche sind getrennt.');
note(zd,26,'Bisherige Quote: ../02_Gesellschaft_und_Personen.docx. Die streitigen Einziehungen sind hier nicht umgesetzt.');
numeric(zd,'B6:D8');numeric(zd,'B15:B19');numeric(zd,'D15:D21');zd.getRange('B20').setNumberFormat('0.0%');zd.getRange('E5:E17').format.wrapText=true;zd.getRange('A15:E17').format.rowHeight=30;
zink.recalculate();control(zink,zb,'D11',19800,'Zink');control(zink,zb,'D23',26800,'Zink');control(zink,zb,'D24',51800,'Zink');control(zink,zd,'D8',70000,'Zink');control(zink,zd,'D19',120000,'Zink');control(zink,zd,'D21',52500,'Zink');
val(zb,'C10',12000);zink.recalculate();control(zink,zb,'D11',15800,'Zink volle Stahlzahlung');control(zink,zb,'D15',0,'Zink Stahlrest');control(zink,zb,'D23',22800,'Zink OP nach Zahlung');val(zb,'C10',8000);
val(zd,'B15',0);zink.recalculate();control(zink,zd,'D21',0,'Zink Preisannahme Null');control(zink,zd,'D8',70000,'Zink Darlehen unverändert');val(zd,'B15',150000);

const outputs=[[berlin,'gesellschafterstreit-klageerwiderung-berlin','N13_Belegabgleich_Lindenhof.xlsx'],[munich,'gesellschafterstreit-shareholder-agreement-muenchen','N13_Kapital_und_Freigaben.xlsx'],[zink,'gesellschafterstreit-zink-und-zunder','N13_Zahlungen_und_Abfindungsannahmen.xlsx']];
for(const [wb,slug,file] of outputs){
 for(const item of all.filter(x=>x.wb===wb)){
  const vs=item.s.getRange(item.range).values,fs=item.s.getRange(item.range).formulas;
  for(let r=0;r<vs.length;r++)if(vs[r].every(v=>v===null||v===undefined||v===''))item.s.getRangeByIndexes(r,0,1,5).format.rowHeight=6;
  item.printRows=vs.reduce((last,row,index)=>row.some(v=>v!==null&&v!==undefined&&v!=='')?index+1:last,1);
  for(let r=0;r<vs.length;r++)for(let c=0;c<vs[r].length;c++)if(typeof vs[r][c]==='number'&&!fs[r]?.[c])item.s.getCell(r,c).format.font.color='#1D4ED8';
 }
 wb.recalculate();
 const error=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100}});
 await fs.writeFile(path.join(qa,file+'.errors.ndjson'),error.ndjson);
 for(const item of all.filter(x=>x.wb===wb)){
  for(const row of item.s.getRange(item.range).values)for(const v of row)if(typeof v==='string'&&/^#(?:REF!|DIV\/0!|VALUE!|NAME\?|N\/A|NUM!|NULL!|SPILL!|CALC!)/.test(v))throw new Error(v);
  const inspected=await wb.inspect({kind:'table',range:`'${item.s.name}'!${item.range}`,include:'values,formulas',tableMaxRows:40,tableMaxCols:5,maxChars:30000});
  await fs.writeFile(path.join(qa,file+'.'+item.s.name+'.ndjson'),inspected.ndjson);
  const img=await wb.render({sheetName:item.s.name,range:item.range,scale:1.3,format:'png'});
  await fs.writeFile(path.join(qa,file+'.'+item.s.name+'.png'),new Uint8Array(await img.arrayBuffer()));
 }
 const out=path.join(root,slug,'Nachtrag_2026-10-08',file);
 await(await SpreadsheetFile.exportXlsx(wb)).save(out);
 // Druckbereiche bleiben auf fünf Spalten begrenzt. Pro Blatt A4 quer, beliebig viele Seiten hoch.
 const z=await JSZip.loadAsync(await fs.readFile(out));
 const sheets=Object.keys(z.files).filter(n=>/^xl\/worksheets\/sheet\d+\.xml$/.test(n)).sort();
 for(const name of sheets){let xml=await z.file(name).async('string');const p=xml.match(/<(\w+:)?worksheet\b/)[1]??'';
  xml=xml.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'').replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,'');
  xml=xml.replace(new RegExp(`</${p}worksheet>`),`<${p}pageMargins left="0.28" right="0.28" top="0.35" bottom="0.35" header="0.15" footer="0.15"/><${p}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="0"/></${p}worksheet>`);z.file(name,xml);
 }
 let wx=await z.file('xl/workbook.xml').async('string');const wp=wx.match(/<(\w+:)?workbook\b/)[1]??'';
 const defs=all.filter(x=>x.wb===wb).map((x,i)=>`<${wp}definedName name="_xlnm.Print_Area" localSheetId="${i}">'${x.s.name}'!$A$1:$E$${x.printRows}</${wp}definedName>`).join('');
 if(wx.includes(`</${wp}definedNames>`))wx=wx.replace(`</${wp}definedNames>`,defs+`</${wp}definedNames>`);
 else wx=wx.replace(new RegExp(`<${wp}calcPr\\b`),`<${wp}definedNames>${defs}</${wp}definedNames><${wp}calcPr`);
 if(!wx.includes('_xlnm.Print_Area'))wx=wx.replace(`</${wp}workbook>`,`<${wp}definedNames>${defs}</${wp}definedNames></${wp}workbook>`);
 z.file('xl/workbook.xml',wx);await fs.writeFile(out,await z.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
 try{await fs.rename(out+'.inspect.ndjson',path.join(qa,file+'.export.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 console.log(out);
}
await fs.writeFile(path.join(qa,'checks.json'),JSON.stringify(checks,null,2)+'\n');

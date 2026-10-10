#!/usr/bin/env node
// Ausführen mit dem von Codex bereitgestellten @oai/artifact-tool.
import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const root = process.argv[2] || process.cwd();
const qa = process.argv[3] || '/tmp/dd-bankakte-qa';
const data = JSON.parse(await fs.readFile(path.join(root, 'scripts/data/dd-bankakte.json'),'utf8'));
const output = path.join(root,'testakten',data.case_slug,'11_Portfolio_und_Kaufpreis.xlsx');
await fs.mkdir(qa,{recursive:true});
const wb = Workbook.create();
const names = ['Ueberblick','Portfolio','Buchungen','Stichprobe','Anleitung'];
const tabs = Object.fromEntries(names.map(name=>[name,wb.worksheets.add(name)]));
const EUR = '#,##0.00;[Red](#,##0.00);0.00';
const blue = '#193D54', pale = '#EAF1F5', ink = '#172B38', input = '#215EAB';

function title(s,text,last='F') {
  s.showGridLines=false;
  s.getRange(`A1:${last}2`).merge();s.getRange('A1').values=[[text]];
  s.getRange(`A1:${last}2`).format={fill:blue,font:{name:'Aptos',size:17,bold:true,color:'#FFFFFF'},verticalAlignment:'center',rowHeight:24};
}
function header(s,row,values) {
  s.getRangeByIndexes(row-1,0,1,values.length).values=[values];
  s.getRangeByIndexes(row-1,0,1,values.length).format={fill:blue,font:{name:'Aptos',size:11,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:36,verticalAlignment:'center'};
}
function base(s,range) {
  s.getRange(range).format={font:{name:'Aptos',size:11,color:ink},rowHeight:22,verticalAlignment:'center'};
}

// Eingänge liegen unverändert im Portfolio und in den Buchungen. Die Übersicht
// liest das berechnete Portfolio, niemals einen Prüfstatus als Eingang.
const p=tabs.Portfolio;
base(p,'A1:K1006');title(p,'Forderungsbestand zum 30.09.2026','K');
p.getRange('A3:K3').merge();p.getRange('A3').values=[['Verkäuferexport 12.00 Uhr | Geldbeträge in EUR | Faktor und Status sind unbestätigte Verkäuferangaben']];
header(p,5,['Darlehen','Name im Export','Belegumfang','Kapital EUR','Zinsen EUR','Kosten EUR','Saldo EUR','Verkäuferfaktor','Preis EUR','Verkäuferstatus','Beleg / Herkunft']);
const pdata=data.portfolio.map(r=>[r.id,r.name,r.scope,r.principal/100,r.interest/100,r.costs/100,null,r.seller_price_ratio,null,r.status,r.source]);
p.getRange('A6:K1005').values=pdata;
p.getRange('G6:G1005').formulas=data.portfolio.map((_,i)=>[`=SUM(D${i+6}:F${i+6})`]);
p.getRange('I6:I1005').formulas=data.portfolio.map((_,i)=>[`=ROUND(D${i+6}*H${i+6},2)`]);
p.getRange('D6:F1005').setNumberFormat(EUR);p.getRange('G6:G1005').setNumberFormat(EUR);p.getRange('I6:I1005').setNumberFormat(EUR);p.getRange('H6:H1005').setNumberFormat('0.0%');
p.getRange('D6:F1005').format.font.color=input;p.getRange('H6:H1005').format.font.color=input;
p.getRange('G6:G1005').format.fill=pale;p.getRange('I6:I1005').format.fill=pale;
for (const [col,width] of Object.entries({A:17,B:27,C:25,D:19,E:17,F:17,G:19,H:19,I:20,J:40,K:69}))p.getRange(`${col}1:${col}1005`).format.columnWidth=width;
p.tables.add('A5:K1005',true,'PortfolioDarlehen');p.freezePanes.freezeRows(5);p.freezePanes.freezeColumns(1);
p.getRange('A6:K25').format.rowHeight=29;

const b=tabs.Buchungen;
base(b,'A1:N246');title(b,'Monatsbuchungen der 20 Detailfälle','N');
b.getRange('A3:N3').merge();b.getRange('A3').values=[['01.10.2025 bis 30.09.2026 | zwölf Buchungen je Detailfall | Anfangssalden aus Vorjahresexport | EUR']];
header(b,5,['Darlehen','Buchungsdatum','Kapital Anfang','Zins gebucht','Kosten gebucht','Zahlung Kapital','Zahlung Zins','Zahlung Kosten','Geldeingang','Kapital Ende','Zins Ende','Kosten Ende','Saldo Ende','Buchungstext']);
const bdata=[];
for(const c of data.cases)for(const j of c.journal)bdata.push([c.id,j.date,j.principal_start/100,j.interest_charge/100,j.costs_charge/100,j.paid_principal/100,j.paid_interest/100,j.paid_costs/100,null,null,j.interest_end/100,j.costs_end/100,null,j.note]);
b.getRange('A6:N245').values=bdata;
b.getRange('I6:I245').formulas=bdata.map((_,i)=>[`=SUM(F${i+6}:H${i+6})`]);
b.getRange('J6:J245').formulas=bdata.map((_,i)=>[`=C${i+6}-F${i+6}`]);
b.getRange('M6:M245').formulas=bdata.map((_,i)=>[`=SUM(J${i+6}:L${i+6})`]);
b.getRange('C6:M245').setNumberFormat(EUR);b.getRange('C6:H245').format.font.color=input;b.getRange('K6:L245').format.font.color=input;
b.getRange('I6:J245').format.fill=pale;b.getRange('M6:M245').format.fill=pale;
b.getRange('A1:A245').format.columnWidth=17;b.getRange('B1:B245').format.columnWidth=18;b.getRange('C1:M245').format.columnWidth=20;b.getRange('N1:N245').format.columnWidth=69;
b.tables.add('A5:N245',true,'Buchungsjournal');b.freezePanes.freezeRows(5);b.freezePanes.freezeColumns(2);

const st=tabs.Stichprobe;
base(st,'A1:F27');title(st,'Auswahl und Umfang der Detailakten');
st.getRange('A3:F3').merge();st.getRange('A3').values=[['20 gezielt ausgewählte Fälle; keine Zufallsstichprobe und keine Hochrechnung auf die übrigen 980 Forderungen.']];
header(st,5,['Darlehen','Name','Auswahlthema','Vertrag und Belege','Prüfung durch Erwerber','Zusätzliche Nachforderung']);
st.getRange('A6:F25').values=data.cases.map(c=>[c.id,c.name,c.topic,`${c.id}_01 bis _04`,'Offen','']);
st.getRange('E6:E25').dataValidation={rule:{type:'list',values:['Offen','In Bearbeitung','Rückfrage','Dokumentiert']}};
st.getRange('E6:F25').format.fill='#FFF5D9';st.getRange('A6:F25').format.wrapText=true;st.getRange('A6:F25').format.rowHeight=51;
for(const [col,width]of Object.entries({A:17,B:28,C:43,D:29,E:26,F:44}))st.getRange(`${col}1:${col}25`).format.columnWidth=width;
st.tables.add('A5:F25',true,'Detailauswahl');st.freezePanes.freezeRows(5);

const u=tabs.Ueberblick;
base(u,'A1:F39');title(u,'Projekt Lindenbogen  |  Kaufpreis und Bestand');
u.getRange('A3:F3').merge();u.getRange('A3').values=[['Arbeitsstand 10.10.2026 | wirtschaftlicher Stichtag 30.09.2026, 24.00 Uhr | EUR']];
u.getRange('A4:F4').merge();u.getRange('A4').values=[['Verkäuferwerte. Keine Bewertung durch den Erwerber und keine Feststellung der Einziehbarkeit.']];
header(u,6,['Bestandsübersicht','Wert','','Preisgrundlage','Wert','']);
u.getRange('A7:A13').values=[['Darlehensnummern'],['Detailakten'],['Nur knapper Export'],['Kapital'],['Gebuchte Zinsen'],['Gebuchte Kosten'],['Nebenbuchsaldo']];
u.getRange('B7:B13').formulas=[['=COUNTA(Portfolio!A6:A1005)'],['=COUNTIFS(Portfolio!C6:C1005,"Detailakte")'],['=COUNTIFS(Portfolio!C6:C1005,"Nur Verkäuferexport")'],['=SUM(Portfolio!D6:D1005)'],['=SUM(Portfolio!E6:E1005)'],['=SUM(Portfolio!F6:F1005)'],['=SUM(Portfolio!G6:G1005)']];
u.getRange('D7:D10').values=[['Indikativer Verkäuferpreis'],['Preis nur auf Kapital'],['Anteil Preis / Kapital'],['Weiterer Erwerberabschlag']];
u.getRange('E7').formulas=[['=SUM(Portfolio!I6:I1005)']];u.getRange('E8').values=[['Zinsen / Kosten ohne Preis']];u.getRange('E9').formulas=[['=E7/B10']];u.getRange('E9').setNumberFormat('0.0%');u.getRange('E10').values=[['Noch nicht vereinbart']];
header(u,16,['Stichtagsüberleitung','EUR','','Grundlage','','']);
u.getRange('A17:A20').values=[['Nebenbuch um 12.00 Uhr'],['Zahlung auf Sammelkonto'],['Technische Nettoposition'],['Hauptbuch laut Verkäufer']];
u.getRange('B17').formulas=[['=B13']];u.getRange('B18').values=[[-720]];u.getRange('B19').formulas=[['=SUM(B17:B18)']];u.getRange('B20').values=[[data.general_ledger_net/100]];
u.getRange('D17:F17').merge();u.getRange('D17').values=[['Unveränderter Mittagsauszug']];
u.getRange('D18:F18').merge();u.getRange('D18').values=[['APB-0017, Eingang 30.09.2026 um 16.42 Uhr']];
u.getRange('D19:F19').merge();u.getRange('D19').values=[['Zuordnung zu Zins / Kapital vor Endpreis klären']];
u.getRange('D20:F20').merge();u.getRange('D20').values=[['03_Hauptbuch_und_Stichtagsbruecke.pdf']];
header(u,23,['Kontrollen','Ergebnis','','Bedeutung','','']);
u.getRange('A24:A26').values=[['Differenz Hauptbuch'],['Bestandsanzahl minus 1000'],['Prüfung Detailfälle offen']];
u.getRange('B24:B26').formulas=[['=B19-B20'],['=B7-1000'],['=COUNTIFS(Stichprobe!E6:E25,"<>Dokumentiert")']];
u.getRange('D24:F24').merge();u.getRange('D24').values=[['Null belegt nur die technische Abstimmung.']];
u.getRange('D25:F25').merge();u.getRange('D25').values=[['Keine Aussage über Vollständigkeit der Belege.']];
u.getRange('D26:F26').merge();u.getRange('D26').values=[['Dokumentiert ersetzt keine fachliche Freigabe.']];
u.getRange('A29:F30').merge();u.getRange('A29').values=[['Die 20 Detailfälle sind bewusst problemorientiert ausgewählt. Für 980 weitere Darlehen fehlen Einzelakten. Ein fehlender Risikovermerk im Verkäuferexport ist kein negatives Prüfungsergebnis.']];
u.getRange('A32:F33').merge();u.getRange('A32').values=[['Die Preisfaktoren können in Portfolio geändert werden. Ein Faktor von null bedeutet Preis null; ein fehlender Faktor ist keine zulässige Nullannahme. Leere Faktoren müssen vor Verwendung der Endliste geklärt werden.']];
u.getRange('A35:F37').merge();u.getRange('A35').values=[['Vollzug noch offen: tatsächlicher Erlaubnisstatus, Übertragbarkeit, Servicevereinbarung, Datenzugriff und Kundenmitteilungen sind nicht durch diese Arbeitsmappe freigegeben. Die Buchung von Zinsen oder Kosten bestätigt keinen entsprechenden Anspruch.']];
u.getRange('A29:F37').format.wrapText=true;u.getRange('A29:F37').format.rowHeight=24;
u.getRange('A1:A39').format.columnWidth=34;u.getRange('B1:B39').format.columnWidth=22;u.getRange('C1:C39').format.columnWidth=4;u.getRange('D1:D39').format.columnWidth=34;u.getRange('E1:E39').format.columnWidth=25;u.getRange('F1:F39').format.columnWidth=17;
u.getRange('B10:B20').setNumberFormat(EUR);u.getRange('B24').setNumberFormat(EUR);u.getRange('E7').setNumberFormat(EUR);
u.getRange('B18').format.font.color=input;u.getRange('B20').format.font.color=input;
u.getRange('B24:B25').conditionalFormats.add('cellIs',{operator:'notEqual',formula:0,format:{fill:'#FBE6E5',font:{color:'#A12929'}}});
u.getRange('B26').conditionalFormats.add('cellIs',{operator:'greaterThan',formula:0,format:{fill:'#FFF0C2'}});
u.freezePanes.freezeRows(6);

const a=tabs.Anleitung;
base(a,'A1:D29');title(a,'Arbeitsweise und Quellen der Verkäuferdatei','D');
header(a,5,['Thema','Erläuterung','Quelle','Verwendung']);
const explanation=[
['Stichtag','Verkäuferexport vom 30.09.2026, 12.00 Uhr. Wirtschaftlicher Stichtag 24.00 Uhr.','03_Hauptbuch_und_Stichtagsbruecke.pdf','Die Nachmittagszahlung getrennt überleiten.'],
['Grundgesamtheit','1.000 eindeutige Darlehensnummern APB-0001 bis APB-1000.','Verkäuferexport KREDIT-ERF-20260930','Die Nummern ersetzen keine Einzelakten.'],
['Detailauswahl','20 Fälle bewusst nach Bearbeitungsverlauf ausgewählt. Keine Zufallsauswahl.','04_Datenraum_und_Urkundeninventar.pdf','Keine Fehlerquote für 1.000 Fälle hochrechnen.'],
['Kapital','Offene Hauptforderung laut Verkäufer, ohne Zinsen und Kosten.','APB-0001 bis APB-0020, jeweiliges Kontojournal','Bestand und Durchsetzbarkeit getrennt prüfen.'],
['Zinsen','Unbezahlte Buchungszinsen; Altsystem bucht teilweise trotz Statusänderung weiter.','Kontojournal und Buchungen','Keine automatische Einziehbarkeit unterstellen.'],
['Kosten','Verkäuferbuchung einschließlich streitiger Pauschalen.','Schriftwechsel der Detailfälle','Anspruch und Nachweis gesondert prüfen.'],
['Saldo','Formel: Kapital plus Zinsen plus Kosten.','Portfolio Spalten D bis G','Kein zusätzlicher Preisbestandteil.'],
['Kaufpreis','Formel: Kapital mal Verkäuferfaktor, auf Cent gerundet.','Portfolio Spalten D, H und I','Faktor ist eine verhandelbare Verkäuferannahme.'],
['Buchungen','Zwölf Monatszeilen je Detailfall, Oktober 2025 bis September 2026.','Jeweiliges Kontojournal; Anfangssalden Verkäuferexport','Eingang und Zuordnung nicht doppelt zählen.'],
['Anfangssalden','Kapital und Zinsstand vor Oktober 2025 sind übernommene Werte.','Vorjahresexport, Einzelbelege nachzufordern','Keine Vollprüfung historischer Zahlungen behaupten.'],
['Stichtagsbrücke','720 Euro gingen nach 12 Uhr auf dem Sammelkonto ein.','APB-0017_03_Schreiben.pdf','Einmal abziehen; Kapital-/Zinsaufteilung noch klären.'],
['Preisänderungen','Faktor in H ändern; Preis und Übersicht rechnen neu.','Verkäuferangebot','Eine Änderung ist keine rechtliche Freigabe.'],
['Stichprobenarbeit','Erwerberstatus und Nachforderungen neben stabiler Vertragsnummer pflegen.','Eigene Bearbeitung','Nach Sortierung bleiben Notizen in derselben Zeile.'],
['Erweiterung','Weitere Akten und Datensätze nur nach Abgleich übernehmen; Tabellen und Summenbereiche gemeinsam erweitern.','Neue Verkäuferlieferung','Die vorliegende Mappe bildet genau 1.000 Nummern ab.'],
['Fehlende Werte','Leere Preisfaktoren ergeben einen sichtbaren Fehler; sie bedeuten nicht null.','Originaldaten und offene Nachfrage','Null nur als ausdrücklich gesetzten Preis verwenden.'],
['Abgrenzung','Kein Erwerb von Einlagen, Mietvertrag, Personal oder ganzen Kundenverträgen freigegeben.','00_Auftrag_Due_Diligence.docx','Jeden zusätzlichen Gegenstand getrennt entscheiden.'],
['Bilanzgrenze','Keine vollständige Bankbilanz und keine bestätigte Bewertung der Forderungen.','03_Hauptbuch_und_Stichtagsbruecke.pdf','Wertberichtigungen und Abschluss separat anfordern.'],
['Kontrollen','Null Differenz zeigt nur rechnerische Übereinstimmung der hier vorhandenen Werte.','Ueberblick Zeilen 23 bis 26','Kontrollfelder sind kein fachlicher Abschluss.']];
a.getRange(`A6:D${explanation.length+5}`).values=explanation;a.getRange(`A6:D${explanation.length+5}`).format.wrapText=true;a.getRange(`A6:D${explanation.length+5}`).format.rowHeight=68;
for(const [col,width]of Object.entries({A:22,B:59,C:47,D:51}))a.getRange(`${col}1:${col}29`).format.columnWidth=width;
a.freezePanes.freezeRows(5);

// Leere Preisannahmen dürfen nicht als scheinbar gesunder Nullpreis verschwinden.
p.getRange('I6:I1005').formulas=data.portfolio.map((_,i)=>[`=IF(ISNUMBER(H${i+6}),ROUND(D${i+6}*H${i+6},2),NA())`]);
p.getRange('H6:H1005').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:1}};

wb.recalculate();
const proof={expected:data.totals,checks:[]};
function assertClose(actual,expected,label){if(Math.abs(actual-expected)>.005)throw new Error(`${label}: ${actual} != ${expected}`);proof.checks.push(label);}
assertClose(u.getRange('B7').values[0][0],1000,'1000 Darlehen');
assertClose(u.getRange('B8').values[0][0],20,'20 Detailakten');
assertClose(u.getRange('B13').values[0][0],data.totals.balance/100,'Saldoüberleitung');
assertClose(u.getRange('E7').values[0][0],data.totals.price/100,'Kaufpreis');
assertClose(u.getRange('B24').values[0][0],0,'Hauptbuchdifferenz');
const old=p.getRange('H6').values[0][0], baseprice=u.getRange('E7').values[0][0];
p.getRange('H6').values=[[0]];wb.recalculate();assertClose(p.getRange('I6').values[0][0],0,'Nullfaktor wird Nullpreis');
assertClose(u.getRange('E7').values[0][0],baseprice-data.portfolio[0].price/100,'Preisänderung erreicht Übersicht');
p.getRange('H6').clear({applyTo:'contents'});wb.recalculate();
const missing=await wb.inspect({kind:'region',sheetId:'Portfolio',range:'H6:I6',maxChars:1500});
if(p.getRange('I6').values[0][0]!=='#N/A')throw new Error('Fehlender Faktor muss sichtbar fehlschlagen');proof.checks.push('Fehlender Faktor bleibt sichtbar');
p.getRange('H6').values=[[old]];st.getRange('E6').values=[['Dokumentiert']];wb.recalculate();assertClose(u.getRange('B26').values[0][0],19,'Weitere Prüfungen bleiben offen');
st.getRange('E6').values=[['Offen']];wb.recalculate();
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:20},maxChars:2000});
const foundErrors=[];
for(const name of names)for(const row of tabs[name].getUsedRange().values)for(const value of row)if(typeof value==='string' && /^#(REF!|DIV\/0!|VALUE!|NAME\?|N\/A|NUM!|NULL!)/.test(value))foundErrors.push({name,value});
if(foundErrors.length)throw new Error('Formelfehler: '+JSON.stringify(foundErrors));
proof.error_scan=foundErrors;
await fs.writeFile(path.join(qa,'excel-pruefung.json'),JSON.stringify(proof,null,2));
for(const [name,range]of [['Ueberblick','A1:F37'],['Portfolio','A1:K15'],['Buchungen','A1:N15'],['Stichprobe','A1:F12'],['Anleitung','A1:D12']]){
  const preview=await wb.render({sheetName:name,range,scale:1,format:'png'});
  await fs.writeFile(path.join(qa,name+'.png'),new Uint8Array(await preview.arrayBuffer()));
}
const xlsx=await SpreadsheetFile.exportXlsx(wb);await xlsx.save(output);
await fs.rm(output+'.inspect.ndjson',{force:true});
console.log(JSON.stringify({output,sheets:names,checks:proof.checks,errors:proof.error_scan}));

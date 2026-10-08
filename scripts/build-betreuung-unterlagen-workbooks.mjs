#!/usr/bin/env node
/** Reproduzierbare Excel-Originale und fallneutrale Abrechnungsvorlage. */
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const CASE = path.join(ROOT, 'testakten/betreuung-adelheid-pfister-dreijahresabrechnung');
const PREVIEW = process.env.BETREUUNG_EXCEL_PREVIEW || '/tmp/betreuung-pfister-excel';
const CAPACITY = 1500;
const LAST = CAPACITY + 6;
const MONEY = '#,##0.00;[Red](#,##0.00);0.00';
const C = { ink:'#20272E', navy:'#263C4A', pale:'#EAF0F3', blue:'#174DAD', green:'#247044', amber:'#FFF0C7', red:'#9B2020', lightred:'#FCE5E2' };
const reports = [];
// Native Excel dates at midnight. Numeric serials avoid the renderer's ISO-Date spill.
const date = s => Math.round((Date.parse(`${s}T00:00:00Z`)-Date.UTC(1899,11,30))/86400000);
const col = n => { let s=''; for (;n;n=Math.floor((n-1)/26)) s=String.fromCharCode(65+(n-1)%26)+s; return s; };

function sheet(wb, name, lastCol, rows=30) {
  const s=wb.worksheets.add(name);
  s.showGridLines=false;
  s.getRange(`A1:${lastCol}${rows}`).format = {font:{name:'Times New Roman',size:11,color:C.ink},rowHeight:22,verticalAlignment:'center'};
  s.getRange(`A1:${lastCol}${rows}`).format.columnWidth=18;
  return s;
}
function title(s, text, note, lastCol) {
  s.getRange('A2').values=[[text]];
  s.getRange('A2').format.font={name:'Times New Roman',size:15,bold:true,color:C.navy};
  s.getRange(`A3:${lastCol}3`).format.borders={bottom:{style:'thin',color:'#8D9FA8'}};
  if(note) {s.getRange('A4').values=[[note]];s.getRange('A4').format.font={italic:true,color:'#59656D'};}
}
function table(s, range, name, headers) {
  const start=Number(range.match(/\d+/)[0]);
  s.getRange(`A${start}:${col(headers.length)}${start}`).values=[headers];
  const t=s.tables.add(range,true,name);
  t.style='TableStyleMedium2';
  s.getRange(`A${start}:${col(headers.length)}${start}`).format={fill:C.navy,font:{name:'Times New Roman',size:11,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:38,horizontalAlignment:'center'};
  s.freezePanes.freezeRows(start);
  s.freezePanes.freezeColumns(1);
  return t;
}
function widths(s, values) {values.forEach((v,i)=>s.getRange(`${col(i+1)}:${col(i+1)}`).format.columnWidth=v);}
function money(s, range) {s.getRange(range).setNumberFormat(MONEY);s.getRange(range).format.horizontalAlignment='right';}
function input(s, range) {s.getRange(range).format.fill=C.amber;s.getRange(range).format.font.color=C.blue;}
function warn(s,range) {s.getRange(range).conditionalFormats.add('cellIs',{operator:'notEqual',formula:0,format:{fill:C.lightred,font:{color:C.red,bold:true}}});}
async function save(wb, outfile, previews, label) {
  wb.recalculate();
  const scan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:40},maxChars:4000,summary:label});
  assert(!/#REF!|#DIV\/0!|#VALUE!|#NAME\?|#N\/A|#NUM!|#NULL!|#SPILL!|#CALC!/.test(scan.ndjson.replace(/"searchTerm"[^\n]*/g,'')), `Formelfehler ${label}: ${scan.ndjson}`);
  await fs.mkdir(path.dirname(outfile),{recursive:true});
  await fs.mkdir(PREVIEW,{recursive:true});
  for(const [name,range] of previews) {
    const blob=await wb.render({sheetName:name,range,scale:1.5,format:'png'});
    await fs.writeFile(path.join(PREVIEW,`${label}-${name}.png`),new Uint8Array(await blob.arrayBuffer()));
  }
  await (await SpreadsheetFile.exportXlsx(wb)).save(outfile);
  await fs.rm(`${outfile}.inspect.ndjson`,{force:true});
  reports.push({label,path:path.relative(ROOT,outfile),sheets:previews.map(x=>x[0]),formula_errors:scan.ndjson});
  console.log(JSON.stringify({saved:path.relative(ROOT,outfile),sheets:previews.length}));
}

function makeTemplate() {
  const wb=Workbook.create();
  const out=sheet(wb,'Abrechnung','H',42);
  const acc=sheet(wb,'Konten','K',30);
  const tx=sheet(wb,'Buchungen','O',LAST);
  const receipts=sheet(wb,'Belege','H',306);
  const questions=sheet(wb,'Rückfragen','L',106);
  const how=sheet(wb,'Anleitung','D',30);
  out.tabColor=C.navy;acc.tabColor='#708894';tx.tabColor='#D8CDBB';
  title(out,'Einnahmen, Ausgaben und offene Zuordnungen','Fallneutrale Arbeitsvorlage. Angaben erst nach Belegsichtung übernehmen.','H');
  widths(out,[40,21,20,19,20,22,22,25]);
  out.getRange('A6:B9').values=[['Betreute Person',null],['Zeitraum von',null],['Zeitraum bis',null],['Bearbeitet von / Stand',null]];
  input(out,'B6:B9');out.getRange('B7:B8').setNumberFormat('yyyy-mm-dd');
  out.getRange('A12:C12').values=[['1. Zahlungsströme','Betrag EUR','Buchungen']];
  out.getRange('A12:C12').format={fill:C.navy,font:{bold:true,color:'#FFFFFF'}};
  const types=[['Bestätigte Einnahmen','Einnahme',1],['Bestätigte Ausgaben','Ausgabe',-1],['Erstattungen, gesondert','Erstattung',1],['Umbuchungen, netto','Umbuchung',1],['Bargeldbewegungen, netto','Bargeld',1],['Ungeklärt, netto','Ungeklärt',1]];
  const amount=`'Buchungen'!$F$7:$F$${LAST}`, days=`'Buchungen'!$B$7:$B$${LAST}`, kind=`'Buchungen'!$H$7:$H$${LAST}`, confirm=`'Buchungen'!$J$7:$J$${LAST}`, ids=`'Buchungen'!$A$7:$A$${LAST}`;
  const scope=`${days},">="&$B$7,${days},"<"&$B$8+1`;
  const period=`OR($B$7="",$B$8="",$B$8<$B$7)`;
  types.forEach(([label,type,sign],i)=>{
    const r=13+i;out.getRange(`A${r}`).values=[[label]];
    const confirmation=i<3?`,${confirm},"Ja"`:'';
    out.getRange(`B${r}`).formulas=[[`=IF(${period},"Zeitraum fehlt",${sign===-1?'0-':''}SUMIFS(${amount},${kind},"${type}",${scope}${confirmation}))`]];
    out.getRange(`C${r}`).formulas=[[`=IF(${period},"",COUNTIFS(${ids},"<>",${kind},"${type}",${scope}${confirmation}))`]];
  });
  out.getRange('A20').values=[['Saldo Einnahmen minus Ausgaben']];
  out.getRange('B20').formulas=[['=IF(AND(ISNUMBER(B13),ISNUMBER(B14)),B13-B14,"Zeitraum fehlt")']];
  out.getRange('A21').values=[['Mit gesonderten Erstattungen']];
  out.getRange('B21').formulas=[['=IF(AND(ISNUMBER(B20),ISNUMBER(B15)),SUM(B20,B15),"Zeitraum fehlt")']];
  out.getRange('A20:C21').format.font.bold=true;
  out.getRange('A24:C24').values=[['2. Noch zu bearbeiten','Anzahl','']];
  out.getRange('A24:C24').format={fill:C.navy,font:{bold:true,color:'#FFFFFF'}};
  out.getRange('A25:A28').values=[['Buchungen mit Prüfbedarf'],['Angelegte Rückfragen'],['Rückfragen ohne Erledigungsnachweis'],['Buchungen außerhalb des Zeitraums']];
  out.getRange('B25').formulas=[[`=COUNTIFS(${ids},"<>",'Buchungen'!$O$7:$O$${LAST},"<>vollständig erfasst")`]];
  out.getRange('B26').formulas=[['=COUNTIFS(\'Rückfragen\'!$A$7:$A$106,"<>")']];
  out.getRange('B27').formulas=[['=COUNTIFS(\'Rückfragen\'!$A$7:$A$106,"<>")-COUNTIFS(\'Rückfragen\'!$A$7:$A$106,"<>",\'Rückfragen\'!$I$7:$I$106,"erledigt",\'Rückfragen\'!$L$7:$L$106,"<>")']];
  out.getRange('B28').formulas=[[`=IF(${period},"Zeitraum fehlt",COUNTIFS(${ids},"<>",${days},"<"&$B$7)+COUNTIFS(${ids},"<>",${days},">="&$B$8+1))`]];
  out.getRange('A31').values=[['Bargeldabhebung belegt den Kontenabfluss, nicht die spätere Verwendung.']];
  out.getRange('A33').values=[['Umbuchungen verbinden eigene Konten und werden nicht als Einnahme oder Ausgabe gezählt.']];
  out.getRange('A35').values=[['Eine vollständige Erfassung bestätigt weder einen Anspruch noch einen Verdacht.']];
  money(out,'B13:B21');out.getRange('C13:C18').setNumberFormat('0');
  out.getRange('B25:B28').conditionalFormats.add('cellIs',{operator:'greaterThan',formula:0,format:{fill:C.amber}});

  title(acc,'Konten und Saldierung','Je Konto eine Zeile. Anfang und Ende müssen zum gewählten Zeitraum gehören.','K');
  widths(acc,[17,26,20,20,21,21,19,29,29,27,28]);
  table(acc,'A6:K26','Kontensaldierung',['Konto-ID','Bezeichnung','Anfang EUR','Ende laut Beleg EUR','Bewegungen EUR','Ende gerechnet EUR','Differenz EUR','Quelle Anfang','Quelle Ende','Prüfvermerk','Kontrollnotiz']);
  input(acc,'A7:D26');input(acc,'H7:I26');input(acc,'K7:K26');
  for(let r=7;r<=26;r++){
    acc.getRange(`E${r}:G${r}`).formulas=[[
      `=IF(A${r}="","",IF(OR('Abrechnung'!$B$7="",'Abrechnung'!$B$8=""),"Zeitraum fehlt",SUMIFS('Buchungen'!$F$7:$F$${LAST},'Buchungen'!$C$7:$C$${LAST},A${r},'Buchungen'!$B$7:$B$${LAST},">="&'Abrechnung'!$B$7,'Buchungen'!$B$7:$B$${LAST},"<"&'Abrechnung'!$B$8+1)))`,
      `=IF(A${r}="","",IF(NOT(ISNUMBER(C${r})),"Anfang fehlt",IF(ISNUMBER(E${r}),SUM(C${r},E${r}),"Zeitraum fehlt")))`,
      `=IF(A${r}="","",IF(NOT(ISNUMBER(D${r})),"Ende fehlt",IF(ISNUMBER(F${r}),ROUND(F${r}-D${r},2),"nicht berechnet")))`
    ]];
    acc.getRange(`J${r}`).formulas=[[`=IF(A${r}="","",IF(COUNTIFS($A$7:$A$26,A${r})>1,"Konto-ID doppelt",IF(OR(H${r}="",I${r}=""),"Saldoquellen fehlen",IF(ISNUMBER(G${r}),IF(G${r}=0,"rechnerisch ausgeglichen","Differenz klären"),"Saldoangaben fehlen"))))`]];
  }
  money(acc,'C7:G26');warn(acc,'G7:G26');

  title(tx,'Buchungen mit Belegzuordnung',`${CAPACITY} Zeilen vorbereitet. Jede Kontobewegung einmal erfassen; Originaltext erhalten.`,'O');
  widths(tx,[19,16,16,29,48,18,25,19,24,20,22,43,20,42,29]);
  table(tx,`A6:O${LAST}`,'Buchungsregister',['Buchung-ID','Datum','Konto-ID','Gegenpartei','Original-Buchungstext','Betrag EUR','Beleg-ID(s)','Art','Kategorie','Zuordnung bestätigt','Gegenbuchung-ID','Quelle / Seite','Belegstand','Sachverhaltsnotiz','Prüfstatus']);
  input(tx,`A7:N${LAST}`);
  tx.getRange(`B7:B${LAST}`).setNumberFormat('yyyy-mm-dd');money(tx,`F7:F${LAST}`);
  tx.getRange(`H7:H${LAST}`).dataValidation={rule:{type:'list',values:['Einnahme','Ausgabe','Erstattung','Umbuchung','Bargeld','Ungeklärt']}};
  tx.getRange(`J7:J${LAST}`).dataValidation={rule:{type:'list',values:['Ja','Nein']}};
  tx.getRange(`M7:M${LAST}`).dataValidation={rule:{type:'list',values:['belegt','teilbelegt','offen']}};
  const checks=[];
  for(let r=7;r<=LAST;r++) {
    const checksForRow=[
      [`A${r}=""`, ''],
      [`COUNTIFS($A$7:$A$${LAST},A${r})>1`, 'Buchung-ID doppelt'],
      [`OR(NOT(ISNUMBER(B${r})),C${r}="",NOT(ISNUMBER(F${r})),H${r}="",L${r}="")`, 'Pflichtangaben fehlen'],
      [`COUNTIFS('Konten'!$A$7:$A$26,C${r})<>1`, 'Konto nicht eindeutig'],
      [`J${r}<>"Ja"`, 'Zuordnung bestätigen'],
      [`OR(AND(H${r}="Einnahme",F${r}<0),AND(H${r}="Ausgabe",F${r}>0))`, 'Vorzeichen prüfen'],
      [`AND(H${r}="Umbuchung",OR(K${r}="",COUNTIFS($A$7:$A$${LAST},K${r})<>1))`, 'Gegenbuchung fehlt'],
      [`AND(H${r}="Umbuchung",ROUND(SUMIFS($F$7:$F$${LAST},$A$7:$A$${LAST},K${r})+F${r},2)<>0)`, 'Umbuchung abweichend'],
      [`OR(G${r}="",M${r}="",M${r}="offen",M${r}="teilbelegt",H${r}="Ungeklärt",H${r}="Bargeld")`, 'Beleg / Verwendung klären']
    ];
    checks.push(['='+checksForRow.reduceRight((tail,[condition,text])=>`IF(${condition},"${text}",${tail})`,'"vollständig erfasst"')]);
  }
  tx.getRange(`O7:O${LAST}`).formulas=checks;
  tx.getRange(`O7:O${LAST}`).conditionalFormats.add('containsText',{text:'fehlt',format:{fill:C.lightred,font:{color:C.red}}});
  tx.getRange(`O7:O${LAST}`).conditionalFormats.add('containsText',{text:'klären',format:{fill:C.amber}});

  title(receipts,'Belegregister','Ein Beleg kann mehreren Buchungen zugeordnet sein; Betrag nicht erneut als Zahlung buchen.','H');
  widths(receipts,[19,17,29,22,45,34,23,50]);
  table(receipts,'A6:H306','Belegregister',['Beleg-ID','Belegdatum','Aussteller','Belegbetrag EUR','Datei / Seite','Buchung-ID(s)','Nachweisumfang','Fehlende Angaben']);
  input(receipts,'A7:H306');receipts.getRange('B7:B306').setNumberFormat('yyyy-mm-dd');money(receipts,'D7:D306');
  receipts.getRange('G7:G306').dataValidation={rule:{type:'list',values:['Zahlung','Vertrag','Rechnung','Verwendungsbeleg','Korrespondenz','sonstiger Nachweis']}};

  title(questions,'Rückfragen und Anschreiben','Adressquelle und Zuständigkeit belegen. Entwurf und tatsächlicher Versand bleiben getrennt.','L');
  widths(questions,[17,25,36,33,39,38,40,18,23,29,25,42]);
  table(questions,'A6:L106','Rueckfragenregister',['Vorgang-ID','Buchung / Beleg','Empfänger','Anschrift / E-Mail','Adressquelle','Zu klärender Sachverhalt','Schreiben / Prüfauftrag','Frist','Bearbeitungsstand','Entwurfspfad','Freigabe durch / am','Versandbeleg / Antwort']);
  input(questions,'A7:L106');questions.getRange('H7:H106').setNumberFormat('yyyy-mm-dd');
  questions.getRange('I7:I106').dataValidation={rule:{type:'list',values:['offen','Entwurf','freigegeben','versandt','Antwort prüfen','erledigt']}};
  questions.getRange('K7:K106').conditionalFormats.addCustom('AND($I7="versandt",$K7="")',{fill:C.lightred,font:{color:C.red}});
  questions.getRange('L7:L106').conditionalFormats.addCustom('AND($I7="erledigt",$L7="")',{fill:C.lightred,font:{color:C.red}});

  title(how,'Die Abrechnung führen','Gelbe Felder sind Eingaben. Formeln und Rohquellen nicht mit Bewertungen überschreiben.','D');
  widths(how,[35,110,20,18]);
  const instructions=[
    ['1. Zeitraum','Tragen Sie Person, Berichtszeitraum und Bearbeiter in der Abrechnung ein. Die Vorlage ist leer und enthält keine Falldaten.'],
    ['2. Konten','Erfassen Sie jedes eigene Konto mit einer eindeutigen Konto-ID. Übernehmen Sie Anfangs- und Endsaldo aus passenden Bankbelegen. Ein echter Nullsaldo wird als Zahl 0 erfasst.'],
    ['3. Rohdaten','Übernehmen Sie jede Buchung genau einmal in Buchungen. Negative Beträge sind Abflüsse, positive Beträge Zuflüsse. Datum, Originaltext und Quellenstelle bleiben erhalten.'],
    ['4. Belege','Erfassen Sie Rechnungen und andere Nachweise im Belegregister. Trennen Sie Rechnungsbetrag, tatsächliche Zahlung und behaupteten Anspruch. Verknüpfen Sie über stabile IDs.'],
    ['5. Zuordnung','Bestätigen Sie die Art erst nach Prüfung. Einnahmen, Ausgaben und Erstattungen werden erst bei Ja ausgewertet. Bargeld, Umbuchungen und ungeklärte Positionen bleiben gesondert sichtbar.'],
    ['6. Umbuchungen','Geben Sie bei beiden Buchungen die jeweilige Gegenbuchung-ID an. Gleicher Betrag mit umgekehrtem Vorzeichen ist eine rechnerische Hilfe, ersetzt aber keinen Nachweis gleicher Kontoinhaberschaft.'],
    ['7. Bargeld','Eine Abhebung ist zunächst eine Bargeldbewegung. Ohne Kassen- oder Einkaufsbeleg keine automatische Verbrauchsausgabe oder Veruntreuung annehmen.'],
    ['8. Kontenabgleich','Die Kontenrechnung enthält alle Bewegungen des Zeitraums, auch ungeklärte. Einnahmen minus Ausgaben können deshalb vom Kontenbestand abweichen. Erklären Sie Differenzen; setzen Sie keine Ausgleichsbuchung ohne Beleg.'],
    ['9. Anschreiben','Erfassen Sie pro Empfänger eine konkrete Frage, Adressquelle und den Entwurfspfad. Kündigung, Widerruf, Anfechtung, Rücktritt und Rückforderung erfordern jeweils eigene Voraussetzungen. Die Tabelle trifft keine Rechtsentscheidung.'],
    ['10. Rückfragen','Ein offener Punkt ist erst erledigt, wenn Antwort oder andere Erledigung mit Quelle dokumentiert ist. Eine Freigabe ist ein namentlicher menschlicher Entscheid; Versandbelege gesondert sichern.'],
    ['11. Kapazität','Vorbereitet sind 1.500 Buchungen, 20 Konten, 300 Belege und 100 Rückfragen. Bei Erweiterung Tabellen UND begrenzte Formelbezüge verlängern, Endzeile prüfen und Salden neu abstimmen.'],
    ['12. Sortieren','Sortieren oder filtern Sie stets die vollständige Tabelle. IDs verbinden Buchungen und Belege unabhängig von ihrer Zeilenposition. Keine einzelnen Spalten isoliert sortieren.'],
    ['13. Ausgabe','Prüfen Sie Zeitraum, Vorzeichen, Belegstand und offene Fragen vor jeder Weitergabe. Zahlen aus dieser Arbeitsmappe sind keine automatische gerichtliche Rechnungslegung.'],
    ['14. Vertraulichkeit','Geben Sie reale personenbezogene Finanzdaten nur im freigegebenen Arbeitsbereich weiter. Die Vorlage versendet keine Nachricht und baut keine Bankverbindung auf.']
  ];
  how.getRange(`A6:B${5+instructions.length}`).values=instructions;
  how.getRange(`A6:B${5+instructions.length}`).format.wrapText=true;how.getRange(`A6:B${5+instructions.length}`).format.rowHeight=56;
  return {wb,out,acc,tx,questions};
}

async function testTemplate(t) {
  const {wb,out,acc,tx,questions}=t;
  out.getRange('B7:B8').values=[[date('2026-01-01')],[date('2026-12-31')]];
  acc.getRange('A7:D7').values=[['K-1','Prüfkonto',100,80]];acc.getRange('H7:I7').values=[['Startbeleg','Endbeleg']];
  tx.getRange('A7:N7').values=[['P-1',date('2026-01-02'),'K-1','Prüfempfänger','Prüfausgabe',-20,'B-1','Ausgabe','Haushalt','Ja',null,'Prüfbeleg Seite 1','belegt',null]];
  wb.recalculate();assert.equal(acc.getRange('G7').values[0][0],0);assert.equal(out.getRange('B14').values[0][0],20);assert.equal(tx.getRange('O7').values[0][0],'vollständig erfasst');
  tx.getRange('F7').values=[[-21.37]];wb.recalculate();assert.equal(out.getRange('B14').values[0][0],21.37);assert.equal(acc.getRange('G7').values[0][0],-1.37);
  await (await SpreadsheetFile.exportXlsx(wb)).save(path.join(PREVIEW,'eingabeaenderung-pruefkopie.xlsx'));
  acc.getRange('C7').values=[[null]];wb.recalculate();assert.equal(acc.getRange('F7').values[0][0],'Anfang fehlt');
  acc.getRange('C7').values=[[0]];wb.recalculate();assert.equal(acc.getRange('F7').values[0][0],-21.37);
  tx.getRange('J7').values=[['Nein']];wb.recalculate();assert.equal(out.getRange('B14').values[0][0],0);assert.equal(tx.getRange('O7').values[0][0],'Zuordnung bestätigen');
  questions.getRange('A7:I7').values=[['R-1','P-1','Empfänger','Anschrift','Quelle','Frage','Auskunft',null,'Entwurf']];
  wb.recalculate();assert.equal(out.getRange('B27').values[0][0],1);
  questions.getRange('K7').values=[['Max Muster / 01.02.2026']];wb.recalculate();assert.equal(out.getRange('B27').values[0][0],1);
  questions.getRange('I7').values=[['erledigt']];wb.recalculate();assert.equal(out.getRange('B27').values[0][0],1);
  questions.getRange('L7').values=[['Antwort vom 05.02.2026 geprüft, Quelle A-2']];wb.recalculate();assert.equal(out.getRange('B27').values[0][0],0);
  tx.getRange('J7').values=[['Ja']];tx.getRange('H7').values=[['Bargeld']];wb.recalculate();assert.equal(out.getRange('B14').values[0][0],0);assert.equal(out.getRange('B17').values[0][0],-21.37);assert.equal(tx.getRange('O7').values[0][0],'Beleg / Verwendung klären');
  tx.getRange('H7').values=[['Umbuchung']];wb.recalculate();assert.equal(tx.getRange('O7').values[0][0],'Gegenbuchung fehlt');
  tx.getRange('K7').values=[['P-2']];tx.getRange('A8:N8').values=[['P-2',date('2026-01-02'),'K-1','Prüfempfänger','Gegenbuchung',21.37,'B-2','Umbuchung','Umbuchung','Ja','P-1','Prüfbeleg Seite 2','belegt',null]];wb.recalculate();assert.equal(out.getRange('B16').values[0][0],0);assert.equal(tx.getRange('O7').values[0][0],'vollständig erfasst');
  tx.getRange('A8').values=[['P-1']];wb.recalculate();assert.equal(tx.getRange('O7').values[0][0],'Buchung-ID doppelt');
  // Restore every temporary value. Only formulas remain in the delivered template.
  out.getRange('B6:B9').clear({applyTo:'contents'});acc.getRange('A7:D7').clear({applyTo:'contents'});acc.getRange('H7:I7').clear({applyTo:'contents'});tx.getRange('A7:N8').clear({applyTo:'contents'});questions.getRange('A7:L7').clear({applyTo:'contents'});
  wb.recalculate();assert.equal(out.getRange('B14').values[0][0],'Zeitraum fehlt');assert.equal(out.getRange('B25').values[0][0],0);
  reports.push({template_tests:['Ausgabe und Kontensaldo','Centänderung','fehlender Anfangssaldo versus Null','unbestätigte Zuordnung','offene Frage trotz Freigabe','Bargeld nicht Verbrauchsausgabe','Umbuchungspaar und Gegenbuchung','doppelte Buchungs-ID','vollständig geleerte Testeingaben']});
}

async function bankBook(data) {
  const wb=Workbook.create(), sum=sheet(wb,'Kontensalden','I',84), tx=sheet(wb,'Bankbuchungen','J',data.transactions.length+6), how=sheet(wb,'Lesehinweise','B',26);
  sum.tabColor=C.navy;tx.tabColor='#D8CDBB';
  title(sum,'Kontenübersicht Adelheid Pfister','01.10.2023 bis 30.09.2026. Beträge in EUR. Monatswerte umfassen sämtliche Bankbewegungen.','I');
  widths(sum,[18,18,21,21,21,22,24,22,46]);
  table(sum,'A6:I78','Monatssalden',['Monat','Konto-ID','Anfang EUR','Gutschriften EUR','Belastungen EUR','Ende gerechnet EUR','Ende laut Auszug EUR','Differenz EUR','Kontoauszug']);
  const rows=[], formule=[], rowsTx=data.transactions;
  let r=7;
  for(const account of data.accounts) {
    let balance=account.opening_balance_cents??account.opening_cents;
    for(let m=0;m<36;m++,r++){
      const month=new Date(Date.UTC(2023,9+m,1,12)),next=new Date(Date.UTC(2023,10+m,1,12)),key=month.toISOString().slice(0,7);
      const ts=rowsTx.filter(t=>(t.account_id??t.account)===account.id&&t.date.startsWith(key));
      const plus=ts.filter(t=>t.amount_cents>0).reduce((s,t)=>s+t.amount_cents,0),minus=ts.filter(t=>t.amount_cents<0).reduce((s,t)=>s-t.amount_cents,0);
      const end=balance+plus-minus;
      rows.push([month,account.id,m===0?balance/100:null,null,null,null,end/100,null,ts[0]?.source_file??`02_Konten/${account.id}_${key}.pdf`]);
      formule.push([r,m===0?null:`=G${r-1}`,`=SUMIFS('Bankbuchungen'!$F$7:$F$${rowsTx.length+6},'Bankbuchungen'!$B$7:$B$${rowsTx.length+6},B${r},'Bankbuchungen'!$C$7:$C$${rowsTx.length+6},">="&A${r},'Bankbuchungen'!$C$7:$C$${rowsTx.length+6},"<"&EDATE(A${r},1),'Bankbuchungen'!$F$7:$F$${rowsTx.length+6},">0")`,`=-SUMIFS('Bankbuchungen'!$F$7:$F$${rowsTx.length+6},'Bankbuchungen'!$B$7:$B$${rowsTx.length+6},B${r},'Bankbuchungen'!$C$7:$C$${rowsTx.length+6},">="&A${r},'Bankbuchungen'!$C$7:$C$${rowsTx.length+6},"<"&EDATE(A${r},1),'Bankbuchungen'!$F$7:$F$${rowsTx.length+6},"<0")`,`=C${r}+D${r}-E${r}`,`=ROUND(F${r}-G${r},2)`]);
      balance=end;
    }
  }
  sum.getRange(`A7:I${6+rows.length}`).values=rows;
  for(const [rr,opening,p,m,e,d] of formule){if(opening)sum.getRange(`C${rr}`).formulas=[[opening]];sum.getRange(`D${rr}:F${rr}`).formulas=[[p,m,e]];sum.getRange(`H${rr}`).formulas=[[d]];}
  sum.getRange(`A7:A${6+rows.length}`).setNumberFormat('mm/yyyy');money(sum,`C7:H${6+rows.length}`);warn(sum,`H7:H${6+rows.length}`);
  title(tx,'Bankbuchungen','Original-Buchungstexte, ohne Einordnung als Verbrauch, Schenkung oder Rückforderung.','J');
  widths(tx,[19,16,16,32,65,19,20,49,25,22]);
  table(tx,`A6:J${rowsTx.length+6}`,'Bankexport',['Buchung-ID','Konto-ID','Buchungstag','Gegenpartei','Verwendungszweck','Betrag EUR','Wertstellung','Kontoauszug','Beleg-ID(s)','Bankreferenz']);
  tx.getRange(`A7:J${rowsTx.length+6}`).values=rowsTx.map(t=>[t.id,t.account_id??t.account,date(t.date),t.party??t.counterparty,t.purpose,t.amount_cents/100,date(t.value_date??t.date),t.source_file,(t.receipt_ids??[]).join(', '),t.bank_reference??t.id]);
  tx.getRange(`C7:C${rowsTx.length+6}`).setNumberFormat('yyyy-mm-dd');tx.getRange(`G7:G${rowsTx.length+6}`).setNumberFormat('yyyy-mm-dd');money(tx,`F7:F${rowsTx.length+6}`);
  tx.getRange(`D7:E${rowsTx.length+6}`).format.wrapText=true;tx.getRange(`A7:J${rowsTx.length+6}`).format.rowHeight=35;
  title(how,'Lesehinweise zum Kontenexport','Auszug aus den vorgelegten Kontenunterlagen.','B');widths(how,[34,120]);
  how.getRange('A6:B13').values=[['1. Inhaberin','Adelheid Pfister'],['2. Zeitraum','Die Datei umfasst Buchungstage vom 01.10.2023 bis einschließlich 30.09.2026.'],['3. Konten',data.accounts.map(a=>`${a.id}: ${a.name}`).join('; ')],['4. Vorzeichen','Positive Beträge sind Bankgutschriften, negative Beträge Bankbelastungen.'],['5. Monatsrechnung','Anfang plus Gutschriften minus Belastungen ergibt den rechnerischen Endsaldo. Die Differenz vergleicht ihn mit dem ausgewiesenen Monatsende.'],['6. Aussagegrenze','Eine Bankbelastung zeigt den Geldabfluss. Ihr Verwendungszweck beweist nicht ohne Weiteres die tatsächliche Gegenleistung.'],['7. Eigene Konten','Überträge zwischen eigenen Konten erscheinen auf beiden Konten. Die Summe der Gutschriften ist deshalb keine bereinigte Einnahmensumme.'],['8. Quellen','Die Kontoauszugs-Spalte benennt die zugehörige Unterlage. Beleg-IDs sind Verknüpfungshinweise, keine rechtliche Bewertung.']];
  how.getRange('A6:B13').format.wrapText=true;how.getRange('A6:B13').format.rowHeight=50;
  wb.recalculate();
  for(let rr=7;rr<=6+rows.length;rr++)assert.equal(sum.getRange(`H${rr}`).values[0][0],0,`Saldozeile ${rr}`);
  const original=tx.getRange('F7').values[0][0];tx.getRange('F7').values=[[original+0.01]];wb.recalculate();assert.equal(sum.getRange('H7').values[0][0],0.01);tx.getRange('F7').values=[[original]];wb.recalculate();
  reports.push({bank_tests:{transactions:rowsTx.length,monthly_accounts:rows.length,all_differences_zero:true,one_cent_perturbation:true}});
  await save(wb,path.join(CASE,'06_Tabellen/Bankexport_2023-10_bis_2026-09.xlsx'),[['Kontensalden','A1:I20'],['Bankbuchungen','A1:J17'],['Lesehinweise','A1:B14']],'bankexport');
}

async function householdBook(data) {
  const wb=Workbook.create(), s=sheet(wb,'Haushaltsnotizen','G',32);
  const notes=data.household_sheet_rows??data.household_notes;
  if(!Array.isArray(notes)||notes.length===0) throw new Error('household_notes fehlen im canonical JSON; keine unabhängigen Falldaten erfinden.');
  title(s,'Haushaltsnotizen nach dem Erstgespräch','Adelheid Pfister. Zusammenstellung von Dr. Maja Winterfeld, Stand 08.10.2026.','G');widths(s,[28,24,20,19,48,36,32]);
  table(s,`A6:G${6+notes.length}`,'Haushaltsnotizen',['Position','Anbieter / Empfänger','Betrag EUR','Rhythmus','Notiz aus Gespräch / Sichtung','Unterlage / Rückfrage','Notiert von']);
  const rows=notes.map(n=>[n.item??n.position,n.party??n.provider,n.amount_cents==null?null:n.amount_cents/100,n.frequency??n.rhythm,n.note??n.memory,n.source??n.question,n.author??'Adelheid Pfister']);
  s.getRange(`A7:G${6+rows.length}`).values=rows;s.getRange(`A7:G${6+rows.length}`).format.wrapText=true;s.getRange(`A7:G${6+rows.length}`).format.rowHeight=69;money(s,`C7:C${6+rows.length}`);
  s.getRange(`A${9+rows.length}`).values=[['Leere Beträge sind noch ungeklärt. Bitte nicht als 0 EUR lesen.']];
  await save(wb,path.join(CASE,'06_Tabellen/Haushaltsnotizen_Adelheid_2026-10-02.xlsx'),[['Haushaltsnotizen',`A1:G${10+rows.length}`]],'haushalt');
}

await fs.mkdir(PREVIEW,{recursive:true});
const template=makeTemplate();
await testTemplate(template);
await save(template.wb,path.join(ROOT,'betreuungsrecht/templates/unterlagen-abrechnung.xlsx'),[['Abrechnung','A1:H36'],['Konten','A1:K13'],['Buchungen','A1:O12'],['Belege','A1:H13'],['Rückfragen','A1:L12'],['Anleitung','A1:B20']],'vorlage');
if(!process.argv.includes('--template-only')){
  const data=JSON.parse(await fs.readFile(path.join(ROOT,'scripts/data/betreuung-pfister.json'),'utf8'));
  await bankBook(data);await householdBook(data);
}
await fs.writeFile(path.join(PREVIEW,'pruefung.json'),JSON.stringify(reports,null,2)+'\n');

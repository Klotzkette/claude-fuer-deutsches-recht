#!/usr/bin/env node
/** Fallregister aus den kanonischen Aktenangaben; keine rechtliche Musterlösung. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
import {Workbook, SpreadsheetFile} from '@oai/artifact-tool';

const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const data=JSON.parse(await fs.readFile(path.join(ROOT,'scripts/data/geldwaeschebeauftragter-akten.json'),'utf8'));
const preview=process.env.AML_PREVIEW||'/tmp/aml-tabellen';
await fs.mkdir(preview,{recursive:true});
const date=s=>Math.round((Date.parse(s+'T00:00:00Z')-Date.UTC(1899,11,30))/86400000);
const col=n=>String.fromCharCode(64+n);
const categories=['Vertragssoll','Kassenbeleg','Bankabgang','Planwert','Behauptung'];
function category(t){
 if(/Gesamtpreis|Kaufpreis/.test(t.status))return 'Vertragssoll';
 if(t.status.startsWith('belegt durch Kassenbeleg'))return 'Kassenbeleg';
 if(t.status.startsWith('Bankabgang'))return 'Bankabgang';
 if(t.status.includes('behauptet'))return 'Behauptung';
 return 'Planwert';
}
function sheet(wb,name,title,widths,rows=35){
 const s=wb.worksheets.add(name);s.showGridLines=false;
 s.getRange(`A1:${col(widths.length)}${rows}`).format={font:{name:'Times New Roman',size:11,color:'#242A30'},rowHeight:24,verticalAlignment:'center'};
 widths.forEach((w,i)=>s.getRange(`${col(i+1)}:${col(i+1)}`).format.columnWidth=w);
 s.getRange('A2').values=[[title]];s.getRange('A2').format.font={name:'Times New Roman',size:15,bold:true,color:'#253A48'};
 s.getRange(`A3:${col(widths.length)}3`).format.borders={bottom:{style:'thin',color:'#A7B3BB'}};
 return s;
}
function table(s,start,headers,rows,name){
 s.getRange(`A${start}:${col(headers.length)}${start}`).values=[headers];
 if(rows.length)s.getRange(`A${start+1}:${col(headers.length)}${start+rows.length}`).values=rows;
 const range=`A${start}:${col(headers.length)}${start+rows.length}`;
 const t=s.tables.add(range,true,name);t.style='TableStyleMedium2';
 s.getRange(`A${start}:${col(headers.length)}${start}`).format={fill:'#253A48',font:{name:'Times New Roman',size:11,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:34,horizontalAlignment:'center'};
 s.getRange(`A${start+1}:${col(headers.length)}${start+rows.length}`).format.wrapText=true;
 s.freezePanes.freezeRows(start);
}

const reports=[];
const selected = process.argv[2];
const cases = selected ? data.cases.filter(c=>c.slug===selected) : data.cases;
assert(cases.length, 'Unbekannte Fallkennung');
for(const c of cases){
 const wb=Workbook.create();
 const sum=sheet(wb,'Übersicht','Beträge nach Nachweisstand',[27,21,18,66],38);sum.tabColor='#253A48';
 const tx=sheet(wb,'Zahlungen','Zahlungsangaben und Belege',[15,16,20,24,45,42,42,18,65],22);
 const people=sheet(wb,'Beteiligte','Ansprechpartner und Beteiligungen',[30,43,43,48],40);
 const log=sheet(wb,'Verlauf','Chronologie und offene Fragen',[17,84,20,42],35);
 sum.getRange('A4:D5').values=[['Fall',c.slug,null,null],['Bearbeitungsstand',date(c.reference_date),null,null]];sum.getRange('B5').setNumberFormat('yyyy-mm-dd');
 const rows=c.transactions.map(t=>[t.id,date(t.date),t.amount_eur,category(t),t.status,t.payer,t.payee,t.evidence_id,t.allocation]);
 table(tx,6,['Vorgang-ID','Datum','Betrag EUR','Betragsart','Nachweisstand laut Unterlage','Zahler / Leistender','Empfänger','Beleg-ID','Zuordnung'],rows,'Zahlungsangaben');
 tx.getRange(`B7:B${6+rows.length}`).setNumberFormat('yyyy-mm-dd');tx.getRange(`C7:C${6+rows.length}`).setNumberFormat('#,##0.00');
 tx.getRange(`A7:I${6+rows.length}`).format.rowHeight=80;
 table(sum,7,['Betragsart','Betrag EUR','Positionen','Aussagegrenze'],categories.map(cat=>[cat,null,null,{
  Vertragssoll:'Verpflichtung aus Vertrag oder Entwurf. Keine zusätzliche Zahlung.',
  Kassenbeleg:'Belegt ist die im Kassenbeleg beschriebene Annahme. Herkunft und Befugnis bleiben gesonderte Fragen.',
  Bankabgang:'Belegt ist der Abgang laut Unterlage. Der Eingang beim Empfänger ist damit noch nicht bestätigt.',
  Planwert:'Angekündigt oder bedingt. Zum Bearbeitungsstand nicht als erfolgte Zahlung gezählt.',
  Behauptung:'Widersprüchliche oder noch unbestätigte Angabe. Keine bestätigte Kaufpreisleistung.'
 }[cat]]),'Betragsarten');
 for(let i=0;i<categories.length;i++){
  const r=8+i;
  sum.getRange(`C${r}`).formulas=[[`=COUNTIFS('Zahlungen'!$D$7:$D$${6+rows.length},A${r})`]];
  sum.getRange(`B${r}`).formulas=[[`=IF(C${r}=0,"keine Angabe",SUMIFS('Zahlungen'!$C$7:$C$${6+rows.length},'Zahlungen'!$D$7:$D$${6+rows.length},A${r}))`]];
 }
  sum.getRange('B8:B12').setNumberFormat('#,##0.00');sum.getRange('A8:D12').format.rowHeight=63;
  sum.getRange('C8:C12').format.horizontalAlignment='center';
  tx.getRange(`D7:D${6+rows.length}`).format.horizontalAlignment='center';
 sum.getRange('A15').values=[['Bearbeitungsfragen']];sum.getRange('A15').format.font.bold=true;
 c.questions.forEach((q,i)=>{sum.getRange(`A${17+i*3}`).values=[[`${i+1}. ${q}`]];sum.getRange(`A${17+i*3}:D${18+i*3}`).format.rowHeight=23;});
 sum.getRange('A34').values=[['Betragsarten nicht addieren. Vertragssoll und Teilbeträge überschneiden sich.']];
 sum.getRange('A35').values=[['Beleg-IDs verweisen auf die Originaldateien. Keine rechtliche Bewertung in dieser Übersicht.']];
 table(people,6,['Person','Rolle','Organisation / Kontakt','Anschrift'],c.contacts.map(p=>[p.name,p.role,p.organisation+'\n'+p.email,p.address]),'Kontakte');
 people.getRange(`A7:D${6+c.contacts.length}`).format.rowHeight=68;
 const start=10+c.contacts.length;
  table(people,start,['Anteilseigner / Kontrollperson','Gesellschaft','Anteil','Quelle und Aussage der Unterlage'],c.ownership.map(p=>[p.owner,p.company,p.percent==null?null:p.percent/100,p.evidence_id+'\n'+p.qualification]),'Beteiligungsangaben');
  people.getRange(`C${start+1}:C${start+c.ownership.length}`).setNumberFormat('0.0%');
 people.getRange(`A${start+1}:D${start+c.ownership.length}`).format.rowHeight=78;
 table(log,6,['Datum','Ereignis','Beleg-ID','Ergänzung nach Sichtung'],c.chronology.map(p=>[date(p.date),p.event,p.evidence_id,null]),'Chronologie');
  log.getRange(`A7:A${6+c.chronology.length}`).setNumberFormat('yyyy-mm-dd');log.getRange(`A7:D${6+c.chronology.length}`).format.rowHeight=63;
  log.getRange(`A7:A${6+c.chronology.length}`).format.horizontalAlignment='center';
 log.getRange(`D7:D${6+c.chronology.length}`).format.fill='#FFF0CA';
 log.getRange(`A${9+c.chronology.length}`).values=[['Gelbe Felder sind für eigene Ergänzungen bestimmt. Quellenangaben bleiben erhalten.']];
 wb.recalculate();
 for(let i=0;i<categories.length;i++){
  const matching=c.transactions.filter(t=>category(t)===categories[i]);
  assert.equal(sum.getRange(`B${8+i}`).values[0][0],matching.length?matching.reduce((a,b)=>a+b.amount_eur,0):'keine Angabe');
 }
 // Rechenwirkung beobachten und vor Auslieferung wiederherstellen.
 const original=tx.getRange('C7').values[0][0], cat=category(c.transactions[0]);
 tx.getRange('C7').values=[[original+1]];wb.recalculate();
 assert.equal(sum.getRange(`B${8+categories.indexOf(cat)}`).values[0][0],original+1);
 tx.getRange('C7').values=[[original]];wb.recalculate();
 const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:2000,summary:'Formelprüfung'});
 assert(!/#REF!|#DIV\/0!|#VALUE!|#NAME\?|#N\/A|#NUM!|#NULL!|#SPILL!|#CALC!/.test(errors.ndjson.replace(/"searchTerm"[^\n]*/g,'')));
 const views=[['Übersicht','A1:D35'],['Zahlungen',`A1:I${rows.length+7}`],['Beteiligte',`A1:D${start+c.ownership.length+1}`],['Verlauf',`A1:D${10+c.chronology.length}`]];
 for(const [name,range] of views){const img=await wb.render({sheetName:name,range,scale:1.3,format:'png'});await fs.writeFile(path.join(preview,c.slug+'-'+name+'.png'),new Uint8Array(await img.arrayBuffer()));}
 const dest=path.join(ROOT,'testakten',c.slug,'04_Tabellen/Fallregister.xlsx');await fs.mkdir(path.dirname(dest),{recursive:true});
 await (await SpreadsheetFile.exportXlsx(wb)).save(dest);await fs.rm(dest+'.inspect.ndjson',{force:true});
 reports.push({case:c.slug,records:rows.length,formula_change_test:true,views:views.length});console.log(c.slug+' gespeichert');
}
await fs.writeFile(path.join(preview,'pruefung.json'),JSON.stringify(reports,null,2)+'\n');

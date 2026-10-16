#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const cases=JSON.parse(await fs.readFile(path.join(root,'scripts/data/strafvollzug-jva-akten.json'),'utf8'));
const qa='/tmp/jva-akten-qa';await fs.mkdir(qa,{recursive:true});
const files={antrag:'02_Antrag_an_die_JVA.docx',bescheid:'03_Bescheid.pdf',bekanntgabe:'04_Bekanntgabevermerk.pdf',hausordnung:'05_Hausordnung_Auszug.pdf',beleg1:'06_Sachbeleg.pdf',beleg2:'07_Ergaenzende_Auskunft.pdf',gespraech:'08_Gespraechsvermerk.docx',plan:'16_Vollzugsplan_Auszug.pdf',mail5:'15_Nachricht_zum_Sachstand.eml'};
const reports=[];
const serialDate=s=>Date.parse(s+'T00:00:00Z')/86400000+25569;
for(const c of cases){
 const wb=Workbook.create();
 const chrono=wb.worksheets.add('Chronologie'),belege=wb.worksheets.add('Belege'),termine=wb.worksheets.add('Termine');
 const sheets=[chrono,belege,termine];
 for(const ws of sheets){
  ws.showGridLines=false;ws.getRange('A1:D30').format.font={name:'Aptos',size:11,color:'#172B3A'};
  ws.getRange('A1:D1').merge();ws.getRange('A1').values=[[c.person+' '+ws.name]];
  ws.getRange('A1:D1').format.font={name:'Aptos',size:17,bold:true,color:'#172B3A'};ws.getRange('A1:D1').format.rowHeight=30;
  ws.getRange('A2:D3').merge();ws.getRange('A2:D3').format.wrapText=true;ws.getRange('A2:D3').format.rowHeight=23;
  ws.getRange('A4').values=[['Bearbeitungsstand']];ws.getRange('B4').values=[[serialDate('2026-10-16')]];ws.getRange('B4').setNumberFormat('yyyy-mm-dd');
  ws.getRange('A6:D6').format.fill='#244B5D';ws.getRange('A6:D6').format.font={name:'Aptos',size:11,bold:true,color:'#FFFFFF'};ws.getRange('A6:D6').format.rowHeight=29;
  ws.getRange('A7:D30').format.wrapText=true;ws.getRange('A7:D30').format.verticalAlignment='top';ws.getRange('A7:D30').format.rowHeight=55;
  ws.freezePanes.freezeRows(6);
 }
 chrono.getRange('A2').values=[['Daten werden aus den bezeichneten Aktenstücken übernommen. Zugang, Entscheidung und spätere Ergänzung sind getrennte Ereignisse. Diese Liste berechnet keine gesetzliche Frist.']];
 chrono.getRange('A6:D6').values=[['Datum','Ereignis','Belegdatei','Einordnung laut Unterlage']];
 chrono.getRange(`A7:D${6+c.dates.length}`).values=c.dates.map(r=>[serialDate(r[0]),r[1],files[r[2]],r[3]]);
 chrono.getRange(`A7:A${6+c.dates.length}`).setNumberFormat('yyyy-mm-dd');
 chrono.getRange('A:A').format.columnWidth=19;chrono.getRange('B:B').format.columnWidth=45;chrono.getRange('C:C').format.columnWidth=41;chrono.getRange('D:D').format.columnWidth=38;
 belege.getRange('A2').values=[['Die Anlagenkennungen entsprechen dem gerichtlichen Parteientwurf. Die Zuordnung belegt keine Richtigkeit sämtlicher Aussagen eines Dokuments. Originaltexte und spätere Ergänzungen gemeinsam lesen.']];
 const rows=[['A1',files.antrag,'Antrag und beantragte Alternativen','Wortlaut des Begehrens'],['A2',files.bescheid,'Entscheidung und Gründe der JVA','Behördliche Position'],['A3',files.bekanntgabe,'Persönliche Bekanntgabe am 05.10.2026','Kein Nachweis eines Gerichtseingangs'],['A4',files.hausordnung,'Interner Organisationsablauf','Keine amtliche Rechtsquelle'],['A5',files.beleg1,c.proof1title,'Zeitpunkt und Verfasser beachten'],['A6',files.beleg2,c.proof2title,'Reichweite der Aussage prüfen'],['A7',files.gespraech,'Anwaltliches Gespräch vom 12.10.2026','Teilweise Angaben aus Erinnerung'],['A8',files.plan,'Vollzugsplanung und nächste Schritte','Keine vorweggenommene Genehmigung']];
 belege.getRange('A6:D6').values=[['Anlage','Originaldatei','Gegenstand','Beweisgrenze']];belege.getRange('A7:D14').values=rows;
 belege.getRange('A:A').format.columnWidth=19;belege.getRange('B:B').format.columnWidth=43;belege.getRange('C:C').format.columnWidth=44;belege.getRange('D:D').format.columnWidth=37;
 termine.getRange('A2').values=[['Aufgeführt sind nur zukünftige Organisations- und Wunschter mine aus den Unterlagen. Die letzte Spalte zählt Kalendertage ab dem Bearbeitungsstand. Sie ist keine Berechnung von Rechtsbehelfsfristen.'.replace('Wunschter mine','Wunschtermine')]];
 termine.getRange('A6:D6').values=[['Datum','Anlass und Quelle','Status laut Unterlage','Kalendertage ab Stand']];
 const future=c.dates.filter(r=>r[0]>='2026-10-16');
 termine.getRange(`A7:C${6+future.length}`).values=future.map(r=>[serialDate(r[0]),r[1]+'; '+files[r[2]],r[3]]);
 termine.getRange(`A7:A${6+future.length}`).setNumberFormat('yyyy-mm-dd');
 for(let i=0;i<future.length;i++)termine.getRange(`D${7+i}`).formulas=[[`=A${7+i}-$B$4`]];
 termine.getRange(`D7:D${6+future.length}`).setNumberFormat('0');termine.getRange('A:A').format.columnWidth=19;termine.getRange('B:B').format.columnWidth=54;termine.getRange('C:C').format.columnWidth=43;termine.getRange('D:D').format.columnWidth=27;
 for(const ws of sheets){ws.getRange('A4:D4').format.fill='#E7EFF2';}
 wb.recalculate();
 const calc=termine.getRange(`D7:D${6+future.length}`).values.map(r=>r[0]);
 const expected=future.map(r=>Math.round((new Date(r[0]+'T12:00:00Z')-new Date('2026-10-16T12:00:00Z'))/86400000));
 if(JSON.stringify(calc)!==JSON.stringify(expected))throw new Error(c.slug+' Tagesdifferenzen '+JSON.stringify(calc)+' '+JSON.stringify(expected));
 const inspection=await wb.inspect({kind:'table',range:`Termine!A6:D${6+future.length}`,include:'values,formulas',tableMaxRows:15,tableMaxCols:4,maxChars:3500});
 const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:1000});
 const outdir=path.join(root,'testakten',c.slug);await fs.mkdir(outdir,{recursive:true});const output=await SpreadsheetFile.exportXlsx(wb);await output.save(path.join(outdir,'14_Chronologie_Belege_Termine.xlsx'));await fs.rm(path.join(outdir,'14_Chronologie_Belege_Termine.xlsx.inspect.ndjson'),{force:true});
 const renders=path.join(qa,c.slug);await fs.mkdir(renders,{recursive:true});
 for(const ws of sheets){const n=ws.name==='Chronologie'?c.dates.length:ws.name==='Belege'?rows.length:future.length;const blob=await wb.render({sheetName:ws.name,range:`A1:D${6+n}`,scale:1,format:'png'});await fs.writeFile(path.join(renders,ws.name+'.png'),new Uint8Array(await blob.arrayBuffer()));}
 reports.push({slug:c.slug,date_differences:calc,expected,inspection:inspection.ndjson,errors:errors.ndjson,sheets:3});
}
await fs.writeFile(path.join(qa,'xlsx-pruefung.json'),JSON.stringify(reports,null,2)+'\n');console.log('4 Exceldateien erstellt und zwölf Blätter gerendert.');

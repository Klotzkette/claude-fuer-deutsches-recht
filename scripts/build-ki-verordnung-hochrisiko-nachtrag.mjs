/** Native Arbeitsmappen: tatsächliche Testzählwerte und Angebotsrechnung. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook,SpreadsheetFile,requireRuntime}=await loadWorkbookRuntime(['jszip']);
const JSZip=requireRuntime('jszip');
const root=process.argv[2]??path.resolve('testakten');
const qa=process.argv[3]??'/tmp/hochrisiko-nachtrag-qa';
const cases=JSON.parse(await fs.readFile(path.join(qa,'cases.json'),'utf8'));
const checks=[];
function setup(wb,name,title){
 const s=wb.worksheets.add(name);s.showGridLines=false;s.freezePanes.freezeRows(5);
 s.getRange('A1:E21').format={font:{name:'Arial',size:11,color:'#172331'},verticalAlignment:'center',rowHeight:21};
 [40,19,20,20,22].forEach((w,i)=>s.getRangeByIndexes(0,i,21,1).format.columnWidth=w);
 s.getRange('A1:E1').merge();s.getRange('A1').values=[[title]];s.getRange('A1').format={font:{name:'Arial',size:15,bold:true},rowHeight:34};
 s.getRange('A2:E2').merge();s.getRange('A2').values=[['Stand 09.10.2026. Blau: veränderbare Eingaben. Schwarz: Formeln.']];s.getRange('A2').format={font:{size:10,color:'#506174'},rowHeight:25};
 return s;
}
function header(s,row,labels){s.getRangeByIndexes(row-1,0,1,5).values=[labels];s.getRangeByIndexes(row-1,0,1,5).format={fill:'#254F6B',font:{color:'#FFFFFF',bold:true},wrapText:true,rowHeight:32};}
function note(s,row,text){s.getRange(`A${row}:E${row}`).merge();s.getRange(`A${row}`).values=[[text]];s.getRange(`A${row}`).format={font:{size:10,color:'#44515C'},wrapText:true,rowHeight:31};}
function check(wb,s,cell,expected,scenario){wb.recalculate();const actual=s.getRange(cell).values[0][0];if(typeof actual!=='number'||Math.abs(actual-expected)>0.000001)throw new Error(`${scenario} ${cell}: ${actual} != ${expected}`);checks.push({case:wb.caseName,sheet:s.name,cell,expected,actual,scenario});}
for(const c of cases){
 const wb=Workbook.create();const jena=c.slug.includes('jena');
 const t=setup(wb,'Testdaten',jena?'Aktenklar Testzählwerte':'Bildspur synthetischer Labortest');
 header(t,5,jena?['Teiltest','Akten','Fehlerbefunde','Vollständig geöffnet','Fehleranteil']:['Referenzgruppe','Serien','Marker gesetzt','Ohne Marker','Markeranteil']);
 t.getRange('A6:D7').values=c.rows;t.getRange('B6:D7').format.font.color='#1D4ED8';
 t.getRange('E6:E7').formulas=[['=IF(B6=0,0,C6/B6)'],['=IF(B7=0,0,C7/B7)']];t.getRange('E6:E7').setNumberFormat('0.0%');
 t.getRange('A6:E7').format={wrapText:true,rowHeight:38,borders:{preset:'all',style:'thin',color:'#D9D9D9'}};
 note(t,9,jena?'Die Teiltests betreffen dieselben 30 Akten; ihre Fallzahlen werden nicht als Personen addiert.':'Die Quotienten sind Testzählwerte. Sie belegen keine klinische Eignung für den Patienteneinsatz.');
 c.notes.slice(0,4).forEach((text,i)=>note(t,11+i,text));
 note(t,16,'Ein Wert von 0 bei leerer Testgruppe ist eine Rechenkonvention; die Gruppe ist dann nicht geprüft.');
 note(t,17,'Die Tabelle entscheidet weder Hochrisikoeinstufung noch Ausnahme oder Produktfreigabe.');
 const k=setup(wb,'Angebot',jena?'Aktenklar Angebot für drei Monate':'Bildspur Angebot für vier Monate');
 header(k,5,['Position','Anzahl','Einzelpreis netto EUR','Perioden','Gesamt netto EUR']);
 k.getRange('A6:D8').values=c.costs;k.getRange('B6:D8').format.font.color='#1D4ED8';
 k.getRange('E6:E8').formulas=[['=ROUND(B6*C6*D6,2)'],['=ROUND(B7*C7*D7,2)'],['=ROUND(B8*C8*D8,2)']];
 k.getRange('A6:E8').format={wrapText:true,rowHeight:37,borders:{preset:'all',style:'thin',color:'#D9D9D9'}};
 k.getRange('A10').values=[['Netto gesamt']];k.getRange('E10').formulas=[['=SUM(E6:E8)']];
 k.getRange('A11').values=[['Umsatzsteuer']];k.getRange('C11').values=[[0.19]];k.getRange('C11').setNumberFormat('0%');k.getRange('C11').format.font.color='#1D4ED8';k.getRange('E11').formulas=[['=ROUND(E10*C11,2)']];
 k.getRange('A12').values=[['Brutto gesamt']];k.getRange('E12').formulas=[['=E10+E11']];k.getRange('A12:E12').format={fill:'#EAF0F4',font:{bold:true},rowHeight:28};
 k.getRange('C6:C8').setNumberFormat('#,##0.00');k.getRange('E6:E12').setNumberFormat('#,##0.00');
 note(k,14,c.notes[4]);note(k,15,'Monatliche Position: Anzahl mal Monatspreis mal Monate. Einmalige Positionen haben eine Periode.');
 note(k,16,'Die Preise sind Angebotsdaten; eine Änderung der Eingaben ist nur eine eigene Rechenvariante.');
 note(k,17,'Gesetzliche Anwendungsfristen, medizinische Validierung und Konformitätsbewertung werden nicht berechnet.');
 const net=jena?9030:9660, gross=jena?10745.7:11495.4;
 check(wb,t,'E6',jena?4/30:3/4,c.slug+' Quote1');check(wb,t,'E7',jena?7/30:3/36,c.slug+' Quote2');check(wb,k,'E10',net,c.slug+' Netto');check(wb,k,'E12',gross,c.slug+' Brutto');
 k.getRange('B6').values=[[0]];check(wb,k,'E12',jena?3034.5:4641,c.slug+' Null Zugänge');k.getRange('B6').values=[[c.costs[0][1]]];
 k.getRange('C11').values=[[0]];check(wb,k,'E12',net,c.slug+' Null Steuer');k.getRange('C11').values=[[0.19]];
 const b=t.getRange('B6').values[0][0];t.getRange('B6').values=[[0]];check(wb,t,'E6',0,c.slug+' Leere Testgruppe');t.getRange('B6').values=[[b]];wb.recalculate();
 for(const s of [t,k]){
  const values=s.getRange('A1:E17').values;for(const row of values)for(const v of row)if(typeof v==='string'&&/^#(?:REF!|VALUE!|DIV\/0!|NAME\?|NUM!|N\/A)/.test(v))throw new Error(v);
  const inspected=await wb.inspect({kind:'table',range:`'${s.name}'!A1:E17`,include:'values,formulas',tableMaxRows:20,tableMaxCols:5,maxChars:20000});await fs.writeFile(path.join(qa,c.slug+'-'+s.name+'.ndjson'),inspected.ndjson);
  const img=await wb.render({sheetName:s.name,range:'A1:E17',scale:1.2,format:'png'});await fs.writeFile(path.join(qa,c.slug+'-'+s.name+'.png'),new Uint8Array(await img.arrayBuffer()));
 }
 const out=path.join(root,c.slug,c.xlsx);await(await SpreadsheetFile.exportXlsx(wb)).save(out);
 // Print setup not exposed by the documented authoring API: preserve authored cells and set only OOXML page metadata.
 const z=await JSZip.loadAsync(await fs.readFile(out));
 for(const n of Object.keys(z.files).filter(n=>/^xl\/worksheets\/sheet\d+\.xml$/.test(n))){let xml=await z.file(n).async('string');const p=xml.match(/<(\w+:)?worksheet\b/)[1]??'';xml=xml.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'').replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,'');xml=xml.replace(`</${p}worksheet>`,`<${p}pageMargins left="0.3" right="0.3" top="0.35" bottom="0.35" header="0.15" footer="0.15"/><${p}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="0"/></${p}worksheet>`);z.file(n,xml);}
 let wx=await z.file('xl/workbook.xml').async('string');const p=wx.match(/<(\w+:)?workbook\b/)[1]??'';const defs=[t,k].map((s,i)=>`<${p}definedName name="_xlnm.Print_Area" localSheetId="${i}">'${s.name}'!$A$1:$E$17</${p}definedName>`).join('');
 if(wx.includes(`</${p}definedNames>`))wx=wx.replace(`</${p}definedNames>`,defs+`</${p}definedNames>`);else wx=wx.replace(new RegExp(`<${p}calcPr\\b`),`<${p}definedNames>${defs}</${p}definedNames><${p}calcPr`);
 if(!wx.includes('_xlnm.Print_Area'))wx=wx.replace(`</${p}workbook>`,`<${p}definedNames>${defs}</${p}definedNames></${p}workbook>`);
 z.file('xl/workbook.xml',wx);await fs.writeFile(out,await z.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
 try{await fs.rename(out+'.inspect.ndjson',path.join(qa,c.slug+'-export.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 console.log(out);
}
await fs.writeFile(path.join(qa,'formelpruefung.json'),JSON.stringify(checks,null,2)+'\n');

#!/usr/bin/env node
// Prüft die unveränderten Exporte des ausgelieferten VVT-Helfers mit Artifact Tool.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {FileBlob, SpreadsheetFile} from '@oai/artifact-tool';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const data=JSON.parse(await fs.readFile(path.join(root,'scripts/data/vvt-testakten.json'),'utf8'));
const qa='/tmp/vvt-akten-qa';await fs.mkdir(qa,{recursive:true});
const inputs=data.map(c=>({name:c.slug,file:path.join(root,'testakten',c.slug,'04_Verzeichnis.xlsx'),expected:c.after.activities.length}));
inputs.push({name:'startregister',file:path.join(root,'verarbeitungsverzeichnis/templates/startregister/verarbeitungsverzeichnis.xlsx'),expected:0});
const reports=[];
for(const input of inputs){
  const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(input.file));
  const names=['Uebersicht','Taetigkeiten','Art30','Screening','Organisation','Entscheidungen','_meta'];
  const rows=wb.worksheets.getItem('Taetigkeiten').getUsedRange().values;
  const actual=rows.slice(2).filter(r=>r[0]).length;
  if(actual!==input.expected)throw new Error(`${input.name}: ${actual} statt ${input.expected} Tätigkeiten`);
  wb.recalculate();
  const inspected=await wb.inspect({kind:'table',range:'Taetigkeiten!A1:F5',include:'values,formulas',tableMaxRows:5,tableMaxCols:6,maxChars:2000});
  const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:1500});
  const filedir=path.join(qa,input.name);await fs.mkdir(filedir,{recursive:true});
  for(const name of names){
    // Alle Spalten werden gerendert; lange Tabellen erscheinen breit, ohne Kürzung.
    const blob=await wb.render({sheetName:name,autoCrop:'all',scale:1,format:'png'});
    await fs.writeFile(path.join(filedir,name+'.png'),new Uint8Array(await blob.arrayBuffer()));
  }
  reports.push({name:input.name,expected_activities:input.expected,actual_activities:actual,sheets:names,inspection:inspected.ndjson,error_scan:errors.ndjson});
}
await fs.writeFile(path.join(qa,'artifact-inspection.json'),JSON.stringify(reports,null,2)+'\n');
console.log(JSON.stringify(reports.map(r=>({name:r.name,activities:r.actual_activities,sheets:r.sheets.length})),null,2));

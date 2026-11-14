#!/usr/bin/env node
// Native Rohdatentabellen; keine nachträgliche Musterabrechnung.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath,pathToFileURL} from 'node:url';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const qa=path.resolve(process.argv[2]);
const runtime=path.join(process.env.HOME,'.cache/codex-runtimes/codex-primary-runtime/dependencies');
await fs.mkdir(qa,{recursive:true});
try { await fs.symlink(path.join(runtime,'node/node_modules'),path.join(qa,'node_modules'),'dir'); } catch(e) {if(e.code!=='EEXIST')throw e;}
const require=createRequire(path.join(qa,'runtime.cjs'));
const {Workbook,SpreadsheetFile}=await import(pathToFileURL(require.resolve('@oai/artifact-tool')).href);
const source=JSON.parse(await fs.readFile(path.join(qa,'source.json'),'utf8'));
const caseDir=path.join(root,'testakten',source.slug);
for (const data of source.workbooks) {
  const workbook=Workbook.create();
  const sheet=workbook.worksheets.add(data.sheet);
  const lastCol=String.fromCharCode(64+data.headers.length),lastRow=6+data.rows.length;
  sheet.showGridLines=false;
  sheet.getRange(`A1:${lastCol}${lastRow}`).format={font:{name:'Arial',size:11,color:'#233540'},rowHeight:26,verticalAlignment:'center'};
  const widths=data.sheet==='Betriebszahlen'?[120,160,140,155,155,240]:[200,130,90,190,130,150,135,115];
  widths.forEach((width,i)=>sheet.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}${lastRow}`).format.columnWidthPx=width);
  sheet.getRange(`A2:${lastCol}2`).merge();sheet.getRange('A2').values=[[data.title]];
  sheet.getRange('A2').format.font={name:'Arial',size:16,bold:true,color:'#1F4355'};
  sheet.getRange('A2').format.rowHeight=34;
  sheet.getRange(`A3:${lastCol}4`).merge();sheet.getRange('A3').values=[[data.note]];sheet.getRange('A3').format.wrapText=true;sheet.getRange('A3').format.font.size=10;
  sheet.getRange(`A6:${lastCol}6`).values=[data.headers];
  sheet.getRange(`A6:${lastCol}6`).format={fill:'#234F65',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:45,wrapText:true,verticalAlignment:'center'};
  const rows=data.rows.map(row=>row.map((value,i)=>i===1&&data.sheet==='Ereignisse'?new Date(value+'T00:00:00Z'):value));
  sheet.getRange(`A7:${lastCol}${lastRow}`).values=rows;
  for(let row=7;row<=lastRow;row++)if(row%2)sheet.getRange(`A${row}:${lastCol}${row}`).format.fill='#EFF4F6';
  if(data.sheet==='Ereignisse') {
    sheet.getRange(`B7:B${lastRow}`).setNumberFormat('yyyy-mm-dd');
    sheet.getRange(`H7:H${lastRow}`).setNumberFormat('#,##0');
  } else sheet.getRange(`B7:E${lastRow}`).setNumberFormat('#,##0');
  sheet.freezePanes.freezeRows(6);
  sheet.tables.add(`A6:${lastCol}${lastRow}`,true, data.sheet==='Ereignisse'?'Fahrzeugereignisse':'Betriebszahlen');
  workbook.recalculate();
  const inspection=await workbook.inspect({kind:'table',range:`${data.sheet}!A6:${lastCol}${Math.min(lastRow,12)}`,include:'values,formulas',tableMaxRows:7,tableMaxCols:8});
  await fs.writeFile(path.join(qa,`${data.sheet}-inspection.ndjson`),inspection.ndjson);
  const errors=await workbook.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!',options:{useRegex:true,maxResults:20}});
  await fs.writeFile(path.join(qa,`${data.sheet}-errors.ndjson`),errors.ndjson);
  assert.equal(sheet.getRange(`A${lastRow}`).values[0][0],data.rows.at(-1)[0]);
  const preview=await workbook.render({sheetName:data.sheet,range:`A1:${lastCol}${Math.min(lastRow,17)}`,scale:1.2,format:'png'});
  await fs.writeFile(path.join(qa,`${data.sheet}.png`),new Uint8Array(await preview.arrayBuffer()));
  const temporary=path.join(qa,path.basename(data.path));
  await (await SpreadsheetFile.exportXlsx(workbook)).save(temporary);
  await fs.copyFile(temporary,path.join(caseDir,data.path));
  await fs.rm(path.join(caseDir,data.path)+'.inspect.ndjson',{force:true});
  console.log(`${data.path}: ${data.rows.length} Datensätze`);
}

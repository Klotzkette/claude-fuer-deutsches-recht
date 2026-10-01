/** Native Excel-Belege der Berliner Bildungsakten.
 * AKTEN_NODE_MODULES wählt das gebündelte node_modules-Verzeichnis.
 * node build-berlin-bildungsakten-tabellen.mjs <spec.json> <qa-directory>
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import { loadWorkbookRuntime } from './akten-workbook-runtime.mjs';
const { Workbook, SpreadsheetFile, requireRuntime } = await loadWorkbookRuntime(['jszip']);
const JSZip = requireRuntime('jszip');

const [specPath, qaDirectory] = process.argv.slice(2);
if (!specPath || !qaDirectory) throw new Error('Spezifikation und QA-Verzeichnis erforderlich.');
await fs.mkdir(qaDirectory, {recursive: true});
const specifications = JSON.parse(await fs.readFile(specPath, 'utf8'));
const results = [];
function col(n) { let out=''; for (n++; n>0; n=Math.floor((n-1)/26)) out=String.fromCharCode(65+(n-1)%26)+out; return out; }
function printWidths(sheet) {
  const widths=sheet.headers.map((_,c)=>sheet.widths?.[c]??25);
  // 126 Zeichenbreiten passen bei 10 pt auf A4 quer. Lange Belegtexte
  // werden in höhere Zeilen umgebrochen, niemals auf Kleinschrift skaliert.
  const sum=widths.reduce((a,b)=>a+b,0);
  if(sum<=126)return widths;
  const base=13,remaining=126-base*widths.length;
  const variable=widths.reduce((a,b)=>a+Math.max(0,b-base),0);
  return widths.map(w=>Math.round((base+Math.max(0,w-base)*remaining/variable)*100)/100);
}
async function addPrintSettings(file) {
  const zip=await JSZip.loadAsync(await fs.readFile(file));
  for(const name of Object.keys(zip.files).filter(n=>/^xl\/worksheets\/sheet\d+\.xml$/.test(n))) {
    let xml=await zip.file(name).async('string');
    const prefix=xml.match(/<(\w+:)?worksheet\b/)[1]??'';
    const setup=`<${prefix}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="0" />`;
    xml=xml.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'');
    xml=xml.replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,`<${prefix}pageMargins left="0.4" right="0.4" top="0.4" bottom="0.4" header="0.15" footer="0.15" />`);
    xml=xml.replace(new RegExp(`</${prefix}worksheet>`),setup+`</${prefix}worksheet>`);
    zip.file(name,xml);
  }
  await fs.writeFile(file,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
}
function wrappedLines(value, width) {
  if(value===null||value===undefined)return 1;
  const text=value instanceof Date?'2026-10-01':String(value).startsWith('=')?'000000.00':String(value);
  const capacity=Math.max(5,Math.floor(width*0.78));
  return text.split('\n').reduce((sum,line)=>{let lines=1,used=0;for(const word of line.split(/\s+/)){const length=word.length;if(used&&used+1+length>capacity){lines++;used=0;}if(length>capacity){lines+=Math.floor(length/capacity);used=length%capacity;}else used+=length+(used?1:0);}return sum+lines;},0);
}
function typed(value) {
  if (typeof value==='string' && /^\d{2}\.\d{2}\.\d{4}$/.test(value)) {
    const [d,m,y]=value.split('.').map(Number); return new Date(Date.UTC(y,m-1,d));
  }
  return value ?? null;
}
for (const spec of specifications) {
  const workbook = Workbook.create();
  for (const sheet of spec.sheets) workbook.worksheets.add(sheet.name);
  for (const sheet of spec.sheets) {
    const ws=workbook.worksheets.getItem(sheet.name); ws.showGridLines=false;
    const widths=printWidths(sheet);
    const width=sheet.headers.length; const matrix=[sheet.headers,...sheet.rows].map(r=>Array.from({length:width},(_,i)=>typed(r[i])));
    const range=ws.getRangeByIndexes(0,0,matrix.length,width);
    range.values=matrix.map(r=>r.map(v=>typeof v==='string'&&v.startsWith('=')?null:v));
    for (let r=1;r<matrix.length;r++) for (let c=0;c<width;c++) {
      const v=matrix[r][c];
      if (typeof v==='string'&&v.startsWith('=')) ws.getCell(r,c).formulas=[[v]];

    }
    range.format.font={name:'Arial',size:10,color:'#172630'};
    range.format.verticalAlignment='center';range.format.wrapText=true;
    ws.getRangeByIndexes(0,0,1,width).format={fill:'#263641',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},rowHeight:34,wrapText:true,horizontalAlignment:'center'};
    for(let c=0;c<width;c++) ws.getRange(`${col(c)}1:${col(c)}${matrix.length}`).format.columnWidth=widths[c];
    for (const [column,format] of Object.entries(sheet.formats??{})) ws.getRange(`${column}2:${column}${matrix.length}`).setNumberFormat(format);
    for(let r=0;r<matrix.length;r++){
      const lines=Math.max(...matrix[r].map((v,c)=>wrappedLines(v,widths[c])));
      ws.getRangeByIndexes(r,0,1,width).format.rowHeight=Math.max(r===0?36:24,lines*15+8);
    }
    for(const column of Object.keys(sheet.formats??{}))ws.getRange(`${column}2:${column}${matrix.length}`).format.horizontalAlignment='center';
    for (let r=1;r<matrix.length;r++) for (let c=0;c<width;c++) if(matrix[r][c] instanceof Date) {
      ws.getCell(r,c).setNumberFormat('yyyy-mm-dd');
      ws.getCell(r,c).format.horizontalAlignment='center';
    }
    if(matrix.length>10) ws.freezePanes.freezeRows(1);
  }
  workbook.recalculate();
  const checks=[];
  for (const sheet of spec.sheets) for (const check of sheet.perturbations??[]) {
    const ws=workbook.worksheets.getItem(sheet.name);const input=ws.getRange(check.input);const saved=input.values;input.values=[[check.value]];workbook.recalculate();
    const actual=ws.getRange(check.output).values[0][0];if(typeof actual!=='number'||Math.abs(actual-check.expected)>1e-8) throw new Error(`Rechenprobe ${spec.file}: ${actual} statt ${check.expected}`);
    checks.push({type:'input_change',sheet:sheet.name,...check,actual});input.values=saved;workbook.recalculate();
  }
  for (const sheet of spec.sheets) {
    const ws=workbook.worksheets.getItem(sheet.name);const range=ws.getRangeByIndexes(0,0,sheet.rows.length+1,sheet.headers.length);
    for(const row of range.values) for(const value of row) if(typeof value==='string'&&/^#(?:REF!|DIV\/0!|VALUE!|NAME\?|N\/A|NUM!|NULL!|SPILL!|CALC!)/.test(value)) throw new Error(`${spec.file}/${sheet.name}: ${value}`);
    for(const [cell,expected] of Object.entries(sheet.expected??{})) {
      const actual=ws.getRange(cell).values[0][0];
      if(typeof expected==='number' ? Math.abs(actual-expected)>1e-8 : actual!==expected) throw new Error(`${spec.file}/${sheet.name}!${cell}: ${actual} statt ${expected}`);
      checks.push({sheet:sheet.name,cell,expected,actual});
    }
    const image=await workbook.render({sheetName:sheet.name,range:`A1:${col(sheet.headers.length-1)}${sheet.rows.length+1}`,scale:1.5,format:'png'});
    const preview=path.join(qaDirectory,`${spec.case}__${path.basename(spec.file,'.xlsx')}__${sheet.name.replace(/[^\p{L}\p{N}-]/gu,'_')}.png`);
    await fs.writeFile(preview,new Uint8Array(await image.arrayBuffer()));
  }
  const output=await SpreadsheetFile.exportXlsx(workbook);await output.save(spec.output);
  await addPrintSettings(spec.output);
  const inspected=await workbook.inspect({kind:'table',range:spec.sheets[0].name+'!A1:'+col(spec.sheets[0].headers.length-1)+(spec.sheets[0].rows.length+1),include:'values,formulas',tableMaxRows:20,tableMaxCols:10});
  await fs.writeFile(path.join(qaDirectory,spec.case+'__inspect.ndjson'),inspected.ndjson);
  const inspect=spec.output+'.inspect.ndjson';try {await fs.rename(inspect,path.join(qaDirectory,spec.case+'__'+path.basename(inspect)));} catch(e) {if(e.code!=='ENOENT')throw e;}
  results.push({file:spec.output,sheets:spec.sheets.length,checks});
  console.log(JSON.stringify({file:spec.file,sheets:spec.sheets.length,checks:checks.length}));
}
await fs.writeFile(path.join(qaDirectory,'tabellen-pruefung.json'),JSON.stringify(results,null,2)+'\n');

// Native Excel-/PowerPoint-Aktenstücke; Ausführung nur im gebündelten Runtime.
import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {Workbook, SpreadsheetFile, Presentation, PresentationFile} from '@oai/artifact-tool';

const [fixture, outputRoot, qaRoot] = process.argv.slice(2);
if (!qaRoot) throw new Error('fixture.json output-root qa-root fehlen');
const cases = JSON.parse(await fs.readFile(fixture, 'utf8'));
const runtime = path.join(process.env.HOME, '.cache/codex-runtimes/codex-primary-runtime/dependencies');
const presentationSkill = path.join(process.env.HOME, '.codex/plugins/cache/openai-primary-runtime/presentations/26.1111.10934/skills/presentations');
const money = '#,##0.00;(#,##0.00);"-"';
const col = n => {let x='';for(n++;n;n=Math.floor((n-1)/26))x=String.fromCharCode(65+(n-1)%26)+x;return x;};
const report=[];

for (const c of cases) {
 const qa=path.join(qaRoot,c.slug);await fs.mkdir(qa,{recursive:true});
 for(const item of c.workbooks??[]){
  const wb=Workbook.create();
  const all=item.sheets.map(s=>({spec:s,sh:wb.worksheets.add(s.name)}));
  const formulaRecords=[];
  for(const {spec:s,sh} of all){
   sh.showGridLines=false;
   const last=col(s.columns.length-1), end=s.rows.length+5;
   sh.getRange(`A1:${last}${end+3}`).format={font:{name:'Arial',size:11},verticalAlignment:'center',rowHeight:23};
   sh.getRange('A2').values=[[s.title??item.title]];
   sh.getRange('A2').format.font={name:'Arial',size:15,bold:true,color:'#203B50'};
   sh.getRange('A3').values=[[s.source??item.source??`${c.client} · ${item.date??'30.09.2026'}`]];
   sh.getRange('A3').format.font={name:'Arial',size:10,italic:true,color:'#586571'};
   sh.getRange(`A5:${last}5`).values=[s.columns];
   sh.getRange(`A5:${last}5`).format={fill:'#203B50',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:44,wrapText:true,horizontalAlignment:'center'};
   const values=s.rows.map(row=>row.map((v,j)=>typeof v==='string'&&v.startsWith('=')?null:typeof v==='string'&&(/^\d{4}-\d{2}-\d{2}$/.test(v)||s.formats?.[s.columns[j]]==='date')?new Date(v):v));
   if(values.length)sh.getRange(`A6:${last}${end}`).values=values;
   s.rows.forEach((row,i)=>row.forEach((v,j)=>{
    if(typeof v==='string'&&v.startsWith('=')){
     const a=`${col(j)}${i+6}`;sh.getRange(a).formulas=[[v]];formulaRecords.push([s.name,a,v]);
     sh.getRange(a).format.font.color=v.includes('!')?'#008000':'#000000';
    }else if(typeof v==='number')sh.getRange(`${col(j)}${i+6}`).format.font.color='#0000FF';
    else if(typeof v==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(v))sh.getRange(`${col(j)}${i+6}`).setNumberFormat('dd.mm.yyyy');
   }));
   for(const [a,f]of Object.entries(s.formulas??{})){sh.getRange(a).formulas=[[f]];formulaRecords.push([s.name,a,f]);}
   for(let j=0;j<s.columns.length;j++){
    const letter=col(j),fmt=s.formats?.[s.columns[j]], width=s.widths?.[j]??(fmt?19:j===0?28:31);
    sh.getRange(`${letter}1:${letter}${end+3}`).format.columnWidth=width;
    if(fmt)sh.getRange(`${letter}6:${letter}${end}`).setNumberFormat({currency:money,integer:'#,##0',date:'dd.mm.yyyy',percent:'0.0%'}[fmt]??fmt);
   }
   sh.freezePanes.freezeRows(5);
   if(s.rows.length>10)sh.freezePanes.freezeColumns(1);
   for(let row=6;row<=end;row++)if(row%2===0)sh.getRange(`A${row}:${last}${row}`).format.fill='#F1F5F7';
   sh.getRange(`A6:${last}${end}`).format.wrapText=true;
   sh.getRange(`A6:${last}${end}`).format.autofitRows();
  }
  wb.recalculate();
  const mutationChecks=[];
  for(const [sheet,address,formula] of formulaRecords){
   // Direkte Zweizellenrechnungen sind nachvollziehbare unabhängige Tests.
   const match=formula.match(/^=([A-Z]+[0-9]+)([-+*])([A-Z]+[0-9]+)$/);
   if(!match)continue;
   const sh=wb.worksheets.getItem(sheet),a=sh.getRange(match[1]),b=sh.getRange(match[3]);
   const av=a.values[0][0],bv=b.values[0][0];
   if(typeof av!=='number'||typeof bv!=='number'||a.formulas[0]?.[0])continue;
   const original=sh.getRange(address).values[0][0];
   a.values=[[av+7]];wb.recalculate();
   const changed=sh.getRange(address).values[0][0];
   const expected=match[2]==='+'?av+7+bv:match[2]==='-'?av+7-bv:(av+7)*bv;
   if(Math.abs(changed-expected)>.0001)throw new Error(`Eingabemutation ${sheet}!${address} ergibt ${changed}, erwartet ${expected}`);
   a.values=[[av]];wb.recalculate();
   if(Math.abs(sh.getRange(address).values[0][0]-original)>.0001)throw new Error('Rücksetzen fehlgeschlagen');
   mutationChecks.push({sheet,input:match[1],result:address,original,changed,expected});
   break;
  }
  if(formulaRecords.length&&!mutationChecks.length){
   for(const [sheet,address,formula] of formulaRecords){
    const sum=formula.match(/^=SUM\(([A-Z]+)([0-9]+):\1([0-9]+)\)$/);
    if(!sum)continue;
    const sh=wb.worksheets.getItem(sheet);
    for(let row=Number(sum[2]);row<=Number(sum[3]);row++){
     const input=`${sum[1]}${row}`,cell=sh.getRange(input),old=cell.values[0][0];
     if(typeof old!=='number'||cell.formulas[0]?.[0])continue;
     const original=sh.getRange(address).values[0][0];cell.values=[[old+7]];wb.recalculate();
     const changed=sh.getRange(address).values[0][0];
     if(Math.abs(changed-original-7)>.0001)throw new Error(`SUM-Eingabemutation fehlgeschlagen: ${item.path}`);
     cell.values=[[old]];wb.recalculate();
     if(Math.abs(sh.getRange(address).values[0][0]-original)>.0001)throw new Error('SUM-Rücksetzen fehlgeschlagen');
     mutationChecks.push({sheet,input,result:address,original,changed,expected:original+7});break;
    }
    if(mutationChecks.length)break;
   }
  }
  if(formulaRecords.length&&!mutationChecks.length)throw new Error(`Kein unabhängiger Eingabemutationstest für Formeln: ${item.path}`);
  const controls=[];
  for(const control of item.controls??[]){
   const actual=all.find(a=>a.spec.name===control.sheet).sh.getRange(control.cell).values[0][0];
   if(typeof actual==='number'&&typeof control.expected==='number'?Math.abs(actual-control.expected)>.005:actual!==control.expected)throw new Error(`${item.path} ${control.sheet}!${control.cell}: ${actual} != ${control.expected}`);
   controls.push({...control,actual});
  }
  const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:2500});
  const errValues=new Set(['#REF!','#DIV/0!','#VALUE!','#NAME?','#N/A','#NUM!','#NULL!','#SPILL!','#CALC!']);
  for(const {spec:s,sh} of all)for(const row of sh.getRange(`A1:${col(s.columns.length-1)}${s.rows.length+8}`).values)for(const val of row)if(errValues.has(val))throw new Error(`${item.path}: ${val}`);
  const inspections=[];
  for(const {spec:s,sh}of all){
   const last=col(s.columns.length-1),end=s.rows.length+5;
   const inspect=await wb.inspect({kind:'table',range:`'${s.name}'!A5:${last}${Math.min(end,14)}`,include:'values,formulas',tableMaxRows:10,tableMaxCols:s.columns.length,maxChars:5000});
   inspections.push({sheet:s.name,inspect:inspect.ndjson});
   const preview=await wb.render({sheetName:s.name,range:`A1:${last}${Math.min(end+1,23)}`,scale:1.3,format:'png'});
   await fs.writeFile(path.join(qa,`${path.basename(item.path)}-${s.name}.png`),new Uint8Array(await preview.arrayBuffer()));
  }
  const out=path.join(outputRoot,c.slug,item.path);await fs.mkdir(path.dirname(out),{recursive:true});
  const file=await SpreadsheetFile.exportXlsx(wb);await file.save(out);
  try{await fs.rename(out+'.inspect.ndjson',path.join(qa,path.basename(out)+'.export-inspect.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
  const result={file:item.path,controls,mutationChecks,formulaRecords:formulaRecords.map(([s,a,f])=>[s,a,f,wb.worksheets.getItem(s).getRange(a).values[0][0]]),inspections,errors:errors.ndjson};
  await fs.writeFile(path.join(qa,path.basename(out)+'.verification.json'),JSON.stringify(result,null,2));report.push({case:c.slug,...result});
 }
 for(const item of c.slides??[]){
  const p=Presentation.create({slideSize:{width:1280,height:720}});
  function text(slide,value,x,y,w,h,size,bold=false,color='#203B50'){
   const sh=slide.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
   sh.text=value;sh.text.style={fontFamily:'Arial',fontSize:size,bold,color};return sh;
  }
  for(let i=0;i<item.slides.length;i++){
   const s=item.slides[i], slide=p.slides.add();slide.background.fill='#F8F9FA';
   if((s.bullets??[]).length>3)throw new Error(`Maximal drei lesbare Absätze pro Folie: ${item.path} ${i+1}`);
   text(slide,c.client,65,35,1150,38,19,true,'#647580');
   text(slide,s.title,65,110,1150,112,40,true);
   let y=255;
   for(const b of s.bullets??[]){text(slide,b,65,y,1120,100,25,false,'#243F50');y+=112;}
   text(slide,`${item.date??'30.09.2026'}   ${i+1} / ${item.slides.length}`,65,655,1150,30,16,false,'#647580');
   const png=await p.export({slide,format:'png',scale:1});
   await fs.writeFile(path.join(qa,`${path.basename(item.path)}-${i+1}.png`),new Uint8Array(await png.arrayBuffer()));
  }
  const staging=await fs.mkdtemp(path.join(qa,path.basename(item.path)+'.staging-'));
  const candidate=path.join(staging,'candidate.pptx'),final=path.join(staging,'output','final.pptx');
  await fs.mkdir(path.dirname(final),{recursive:true});
  await(await PresentationFile.exportPptx(p)).save(candidate);
  await fs.rm(final,{force:true});
  const {finalizePresentation}=await import(pathToFileURL(path.join(presentationSkill,'container_tools/artifact_tool_utils.mjs')).href);
  await finalizePresentation({workspaceDir:qa,candidatePath:candidate,finalPath:final,pythonExecutable:path.join(runtime,'python/bin/python3'),integrityValidatorPath:path.join(presentationSkill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(presentationSkill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],fontPolicy:{basis:'design',families:['Arial']},explicitTotalSlideCount:item.slides.length,verifyArtifactToolImport:true,receiptPath:path.join(staging,'validation.json')});
  const out=path.join(outputRoot,c.slug,item.path);await fs.mkdir(path.dirname(out),{recursive:true});await fs.copyFile(final,out);
 }
}
await fs.writeFile(path.join(qaRoot,'office-checks.json'),JSON.stringify(report,null,2));
console.log(`Office-Aktenstücke für ${cases.length} Mandate erstellt`);

import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';
const [fixture, root, qa] = process.argv.slice(2);
if (!qa) throw new Error('Arguments: fixture.json repository-root qa-directory');
const cases = JSON.parse(await fs.readFile(fixture, 'utf8'));
const reports=[];
const money='[$-407]#,##0.00"  "';
for (const c of cases) for (const item of c.files.filter(i=>i.name.endsWith('.xlsx'))) {
 const wb=Workbook.create(); const sh=wb.worksheets.add('Arbeitsstand');
 sh.showGridLines=false;
 sh.getRange('A1:F28').format={font:{name:'Times New Roman',size:11},rowHeight:15,verticalAlignment:'center'};
 sh.getRange('A2').values=[[item.title]];
 sh.getRange('A2').format.font={name:'Times New Roman',size:15,bold:true};
 sh.getRange('A2:F2').format.rowHeight=25;sh.getRange('A3:F3').format.rowHeight=18;
 sh.getRange('A3').values=[[`${item.author} | Stand ${item.date}`]];
 sh.getRange('A3').format.font={name:'Times New Roman',size:11,italic:true,color:'#555555'};
 let headers, end, noteRow, total, driver, delta, last;
 const formulas=[];
 function f(a,v){sh.getRange(a).formulas=[[v]];formulas.push(a);}
 if(item.kind==='claims'){
  headers=['Eingang','Gläubiger','Basis EUR','Abzug EUR','Zinsen EUR','Rechenstand EUR'];
  const data=item.rows.map(r=>[r[0],r[1],r[2],r[3],r[4],null]);
  sh.getRange('A6:F10').values=data;
  for(let i=0;i<data.length;i++)f(`F${i+6}`,`=C${i+6}-D${i+6}+E${i+6}`);
  sh.getRange('A12').values=[['Summe Eingänge']];
  for(const col of ['C','D','E','F'])f(`${col}12`,`=SUM(${col}6:${col}10)`);
  sh.getRange('C6:E10').format.font.color='#0000FF';sh.getRange('C6:F12').setNumberFormat(money);
  sh.getRange('A:A').format.columnWidth=20;sh.getRange('B:B').format.columnWidth=20;sh.getRange('C:E').format.columnWidth=17;sh.getRange('F:F').format.columnWidth=22;
  const notes=item.rows.map(r=>`${r[0]}: ${r[5]}.`).join(' ');
  sh.mergeCells('A14:F15');sh.getRange('A14').values=[[notes]];sh.getRange('A14:F15').format.wrapText=true;
  end=12;noteRow=17;total='F12';driver='D7';delta=-100;
 }else if(item.kind==='inventory'){
  headers=['Artikel','Stück','Brutto je Stück EUR','Wert EUR','Beleg'];
  sh.getRange('A6:E8').values=item.rows.map(r=>[r[0],r[1],r[2],null,r[3]]);
  for(let i=0;i<item.rows.length;i++)f(`D${i+6}`,`=B${i+6}*C${i+6}`);
  sh.getRange('A10').values=[['Gesamt']];f('D10','=SUM(D6:D8)');
  sh.getRange('B6:C8').format.font.color='#0000FF';sh.getRange('C6:D10').setNumberFormat(money);
  sh.getRange('A:A').format.columnWidth=27;sh.getRange('B:B').format.columnWidth=12;sh.getRange('C:D').format.columnWidth=22;sh.getRange('E:E').format.columnWidth=34;
  end=10;noteRow=13;total='D10';driver='B6';delta=6000;
 }else if(item.kind==='ledger'){
  headers=['Vorgang','Betrag EUR','Gutschrift EUR','Rest EUR','Beleg'];
  sh.getRange('A6:E8').values=item.rows.map(r=>[r[0],r[1],r[2],null,r[3]]);
  for(let i=0;i<item.rows.length;i++)f(`D${i+6}`,`=B${i+6}-C${i+6}`);
  sh.getRange('A10').values=[['Summe dieser Belege']];f('D10','=SUM(D6:D8)');
  sh.getRange('B6:C8').format.font.color='#0000FF';sh.getRange('B6:D10').setNumberFormat(money);
  sh.getRange('A:A').format.columnWidth=26;sh.getRange('B:D').format.columnWidth=19;sh.getRange('E:E').format.columnWidth=43;
  end=10;noteRow=13;total='D10';driver='C8';delta=-100;
 }else if(item.kind==='cafe'){
  headers=['Gutscheine','Stück','Nennwert EUR','Gesamt EUR','Beleg'];
  sh.getRange('A6:E8').values=item.rows.map(r=>[r[0],r[1],r[2],null,r[3]]);
  for(let i=0;i<item.rows.length;i++)f(`D${i+6}`,`=B${i+6}*C${i+6}`);
  sh.getRange('A10').values=[['Verkauft und noch offen']];f('B10','=B6-B7');f('D10','=D6-D7');
  sh.getRange('A12:C14').values=[['Standort','Betrag EUR','Beleg'],['Backsteg',1640,'09 Bestandsaufnahme'],['Mühlenbogen',860,'08–10 Korrektur']];
  sh.getRange('A15').values=[['Standorte gesamt']];f('B15','=SUM(B13:B14)');
  sh.getRange('B6:C8').format.font.color='#0000FF';sh.getRange('B13:B14').format.font.color='#0000FF';sh.getRange('C6:D10').setNumberFormat(money);sh.getRange('B13:B15').setNumberFormat(money);
  sh.getRange('A:A').format.columnWidth=32;sh.getRange('B:B').format.columnWidth=18;sh.getRange('C:C').format.columnWidth=25;sh.getRange('D:D').format.columnWidth=20;sh.getRange('E:E').format.columnWidth=30;
  end=15;noteRow=18;total='D10';driver='B7';delta=-2500;
 }else throw new Error(item.kind);
 last=String.fromCharCode(64+headers.length);
 sh.getRange(`A5:${last}5`).values=[headers];
 sh.getRange(`A5:${last}5`).format={fill:'#33465B',font:{name:'Times New Roman',size:11,bold:true,color:'#FFFFFF'},rowHeight:32,wrapText:true,horizontalAlignment:'center'};
 sh.getRange(`A6:${last}${end}`).format.rowHeight=22;
 sh.getRange(`A${end}:${last}${end}`).format.font.bold=true;
 sh.getRange(`A${end}:${last}${end}`).format.borders={top:{style:'thin',color:'#8899AA'}};
 const notes=[item.note,'Blaue Zahlen sind Eingaben aus den genannten Aktenstücken. Schwarze Ergebnisse sind Formeln. Die Belegangaben beziehen sich auf die Dateinummern derselben Akte.'];
 for(let i=0;i<notes.length;i++){
  const r=noteRow+i*3;sh.mergeCells(`A${r}:${last}${r+1}`);sh.getRange(`A${r}`).values=[[notes[i]]];sh.getRange(`A${r}:${last}${r+1}`).format={wrapText:true,verticalAlignment:'top',rowHeight:22,font:{name:'Times New Roman',size:11,color:'#444444'}};
 }
 if(item.kind!=='claims')sh.getRange('E6:E8').setNumberFormat('  @');
 if(item.kind==='cafe')sh.getRange('C13:C14').setNumberFormat('  @');
 wb.recalculate();
 const before=Number(sh.getRange(total).values[0][0]);const old=Number(sh.getRange(driver).values[0][0]);
 sh.getRange(driver).values=[[old+100]];wb.recalculate();const changed=Number(sh.getRange(total).values[0][0]);
 if(Math.abs(changed-before-delta)>0.001)throw new Error(`Recalculation failed ${item.name}: ${before}/${changed}`);
 sh.getRange(driver).values=[[old]];wb.recalculate();
 const inspect=await wb.inspect({kind:'table',range:`Arbeitsstand!A5:${last}${end}`,include:'values,formulas',tableMaxRows:20,tableMaxCols:6,maxChars:5000});
 const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:2500});
 const qaDir=path.join(qa,c.slug);await fs.mkdir(qaDir,{recursive:true});
 await fs.writeFile(path.join(qaDir,item.name+'.inspection.json'),JSON.stringify({before,changed,input_change_test:true,formulas:formulas.map(a=>[a,sh.getRange(a).formulas[0][0],sh.getRange(a).values[0][0]]),inspect:inspect.ndjson,errors:errors.ndjson},null,2));
 const preview=await wb.render({sheetName:'Arbeitsstand',range:`A1:${last}${noteRow+4}`,scale:1.5,format:'png'});
 await fs.writeFile(path.join(qaDir,item.name+'.png'),new Uint8Array(await preview.arrayBuffer()));
 const out=path.join(root,'testakten',c.slug,item.name);await fs.mkdir(path.dirname(out),{recursive:true});
 const file=await SpreadsheetFile.exportXlsx(wb);await file.save(out);
 try{await fs.rename(out+'.inspect.ndjson',path.join(qaDir,item.name+'.export-inspect.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 reports.push({file:out,total:before,input_change_test:true,formulas:formulas.length});
}
await fs.mkdir(qa,{recursive:true});await fs.writeFile(path.join(qa,'xlsx-checks.json'),JSON.stringify(reports,null,2));console.log(JSON.stringify(reports));

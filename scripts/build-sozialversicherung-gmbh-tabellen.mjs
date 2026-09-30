// Native XLSX originals and disposable calculation checks via the public Artifact Tool API.
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const qa=process.env.SV_AKTEN_QA_DIR||path.join(os.tmpdir(),'sozialversicherungspflicht-20260930','gmbh-qa');
// Prefer a caller-selected runtime; otherwise normal Node package resolution,
// including NODE_PATH, applies. No desktop-specific runtime path is assumed.
const runtimeRoot=process.env.CODEX_RUNTIME_DEPENDENCIES_ROOT;
const require=createRequire(runtimeRoot?path.join(runtimeRoot,'node','package.json'):import.meta.url);
const {Workbook,SpreadsheetFile}=await import(require.resolve('@oai/artifact-tool'));
const cases=JSON.parse(await fs.readFile(path.join(qa,'cases.json'),'utf8'));
await fs.mkdir(path.join(qa,'mutations'),{recursive:true});
const results=[];
function base(wb,name,c,last){
  const s=wb.worksheets.add(name);s.showGridLines=false;
  s.getRange(`A1:E${last}`).format.font={name:'Arial',size:11,color:'#222222'};
  s.getRange(`A1:E${last}`).format.rowHeight=23;
  s.getRange(`A1:E${last}`).format.verticalAlignment='center';
  s.getRange('A:A').format.columnWidth=26;
  s.getRange('B:D').format.columnWidth=19;
  s.getRange('E:E').format.columnWidth=45;
  s.getRange('A1:E1').merge();s.getRange('A1').values=[[c.company]];
  s.getRange('A1:E1').format.fill='#243C50';s.getRange('A1:E1').format.font={color:'#FFFFFF',bold:true,size:15};
  s.getRange('A1:E1').format.rowHeight=34;
  s.getRange('A2:E2').merge();s.getRange('A2').values=[['Interne Buchhaltung | Stand 30.09.2026 | Beträge in EUR']];
  s.getRange('A2:E2').format.font={color:'#56616B',size:10};
  s.freezePanes.freezeRows(4);return s;
}
function band(s,r){s.getRange(r).format.fill='#E5EBEF';s.getRange(r).format.font={bold:true};}
function header(s,row){
  s.getRange(`A${row}:E${row}`).format.wrapText=true;
  s.getRange(`A${row}:E${row}`).format.rowHeight=36;
  s.getRange(`B${row}:D${row}`).format.horizontalAlignment='center';
}
async function save(wb,s,c,name,range,mutation){
  wb.recalculate();
  const inspection=await wb.inspect({kind:'region',sheetId:s.name,range,maxChars:18000,tableMaxRows:40,tableMaxCols:5});
  await fs.writeFile(path.join(qa,c.short+'-'+name+'.inspect.ndjson'),inspection.ndjson);
  const preview=await wb.render({sheetName:s.name,range,scale:1,format:'png'});
  await fs.writeFile(path.join(qa,c.short+'-'+name+'.png'),new Uint8Array(await preview.arrayBuffer()));
  const out=path.join(root,'testakten',c.slug,name+'.xlsx');
  await (await SpreadsheetFile.exportXlsx(wb)).save(out);
  try { await fs.rename(out+'.inspect.ndjson',path.join(qa,c.short+'-'+name+'.export-inspect.ndjson')); } catch(e) { if(e.code!=='ENOENT')throw e; }
  const before=s.getRange(mutation.output).values;
  s.getRange(mutation.input).values=[[mutation.value]];wb.recalculate();
  const after=s.getRange(mutation.output).values;
  const mutated=path.join(qa,'mutations',c.short+'-'+name+'.xlsx');
  await (await SpreadsheetFile.exportXlsx(wb)).save(mutated);
  results.push({case:c.short,file:out,sheet:s.name,mutation:{...mutation,before,after,file:mutated}});
}
for(const c of cases){
  const wb=Workbook.create(),s=base(wb,'Anteile',c,20),n=c.shares.length,end=4+n,total=end+1;
  s.getRange('A4:E4').values=[['Gesellschafter','Nennbetrag','Anteil aktuell','Anteil-Nr.','Quelle / Stand']];band(s,'A4:E4');
  header(s,4);
  s.getRange(`A5:B${end}`).values=c.shares;
  s.getRange(`C5:C${end}`).formulas=c.shares.map((_,i)=>[`=B${5+i}/SUM($B$5:$B$${end})`]);
  s.getRange(`D5:E${end}`).values=c.shares.map((_,i)=>[i+1,'Gesellschafterliste, Datei 04']);
  s.getRange(`A${total}`).values=[['Summe']];s.getRange(`B${total}`).formulas=[[`=SUM(B5:B${end})`]];s.getRange(`C${total}`).formulas=[[`=SUM(C5:C${end})`]];band(s,`A${total}:E${total}`);
  s.getRange(`B5:B${total}`).setNumberFormat('#,##0.00"  "');s.getRange(`C5:C${total}`).setNumberFormat('0.00%"  "');
  s.getRange(`B5:C${total}`).format.horizontalAlignment='right';
  s.getRange(`D5:D${end}`).format.horizontalAlignment='center';
  s.getRange(`B5:B${end}`).format.font={color:'#1F5B9E'};
  s.getRange('A11:E11').merge();s.getRange('A11').values=[['Besprechungsstand – mögliche spätere Veränderung']];band(s,'A11:E11');
  if(c.short==='Berlin'){
    s.getRange('A12:E12').values=[['Gesellschafter','Bisher','Geplante Übertragung','Danach geplant','Verhandlungsstand']];band(s,'A12:E12');header(s,12);
    s.getRange('A13:A15').values=c.shares.map(x=>[x[0]]);
    s.getRange('B13:B15').formulas=[['=B5'],['=B6'],['=B7']];s.getRange('C13:C15').values=[[6000],[0],[-6000]];
    s.getRange('D13:D15').formulas=[['=B13+C13'],['=B14+C14'],['=B15+C15']];
    s.getRange('E13:E15').values=[['Finanzierung noch offen'],['Keine Übertragung geplant'],['Kein notarielles Angebot']];
    s.getRange('B13:D15').setNumberFormat('#,##0.00"  "');s.getRange('B13:D15').format.horizontalAlignment='right';
  }else{
    s.getRange('A12:E13').merge();s.getRange('A12').values=[['Keine Anteilsübertragung vereinbart. Beide Beteiligungen betragen weiterhin jeweils 25.000 EUR. Der Satzungsentwurf vom 31.07.2026 betrifft die Beschlussfassung.']];s.getRange('A12:E13').format.wrapText=true;
  }
  s.getRange('A17:E18').merge();s.getRange('A17').values=[['Quelle: Dateien 02 und 04. Die Planung ist kein aktueller Registerstand. Gesellschaftsvertrag und Nebenvereinbarungen stehen separat in der Vertragsablage.']];s.getRange('A17:E18').format.wrapText=true;s.getRange('A17:E18').format.font={color:'#56616B',size:10};
  await save(wb,s,c,'14_Anteilsuebersicht','A1:E18',{input:'B5',value:c.shares[0][1]+100,output:`B${total}:C${total}`,expectedSum:c.capital+100});
  const w=Workbook.create(),v=base(w,'Vergütung',c,34);
  v.getRange('A3:E3').merge();v.getRange('A3').values=[[c.person+' | Monatswerte aus der Vertragsablage']];
  v.getRange('A4:E4').values=[['Monat','Festvergütung','Sondervergütung','Brutto gesamt','Vertragsgrundlage']];band(v,'A4:E4');
  header(v,4);
  const monthly=[];for(let y=2025;y<=2026;y++)for(let m=1;m<=(y===2025?12:9);m++)monthly.push([new Date(Date.UTC(y,m-1,1)),y===2025?c.oldsalary:c.salary,0,null,y===2025?'Anstellungsvertrag, Datei 06':'Nachtrag 12.12.2025, Datei 11']);
  v.getRange('A5:E25').values=monthly;v.getRange('A5:A25').setNumberFormat('mmm yyyy');
  v.getRange('D5:D25').formulas=monthly.map((_,i)=>[`=B${5+i}+C${5+i}`]);
  v.getRange('B5:C25').format.font={color:'#1F5B9E'};v.getRange('B5:D29').setNumberFormat('#,##0.00"  "');
  v.getRange('B5:D29').format.horizontalAlignment='right';
  v.getRange('A27:C27').merge();v.getRange('A27').values=[['Jahr 2025']];v.getRange('D27').formulas=[['=SUM(D5:D16)']];band(v,'A27:E27');
  v.getRange('A28:C28').merge();v.getRange('A28').values=[['Januar bis September 2026']];v.getRange('D28').formulas=[['=SUM(D17:D25)']];band(v,'A28:E28');
  v.getRange('A29:C29').merge();v.getRange('A29').values=[['Gesamter dokumentierter Zeitraum']];v.getRange('D29').formulas=[['=SUM(D27:D28)']];band(v,'A29:E29');
  v.getRange('A31:E32').merge();v.getRange('A31').values=[['Auslagen und Gesellschafterdarlehen sind hier nicht als Vergütung erfasst. Zahlungsübersicht: Datei 25; Einzelabrechnung und Bankbuchung August: Dateien 12 und 13.']];v.getRange('A31:E32').format.wrapText=true;v.getRange('A31:E32').format.font={color:'#56616B',size:10};
  await save(w,v,c,'15_Verguetungen_2025_2026','A1:E32',{input:'B5',value:c.oldsalary+100,output:'D27:D29',expected2025:c.oldsalary*12+100});
}
await fs.writeFile(path.join(qa,'workbook-checks.json'),JSON.stringify(results,null,2));
console.log(JSON.stringify({workbooks:results.length,previewSheets:results.length,mutationFiles:results.length}));

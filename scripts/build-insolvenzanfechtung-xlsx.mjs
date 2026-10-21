import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

// Run with the bundled Node runtime and a task-local node_modules symlink.
const [fixture, root, qa] = process.argv.slice(2);
if (!qa) throw new Error('Arguments: fixture.json repository-root qa-directory');
const cases = JSON.parse(await fs.readFile(fixture, 'utf8'));
await fs.mkdir(qa, { recursive: true });
const money = '[$-407]#,##0.00_);[Red](#,##0.00);"-"_)';
const reports = [];
const date = value => (Date.parse(`${value}T00:00:00Z`) - Date.UTC(1899, 11, 30)) / 86400000;

for (const c of cases) for (const item of c.files.filter(x => x.name.endsWith('.xlsx'))) {
  const wb = Workbook.create();
  const sh = wb.worksheets.add('Abgleich');
  sh.showGridLines = false;
  sh.getRange('A1:F28').format.font = { name: 'Times New Roman', size: 11 };
  sh.getRange('A1:F28').format.verticalAlignment = 'center';
  sh.getRange('A1:F28').format.rowHeight = 20;
  sh.getRange('A2').values = [[item.title]];
  sh.getRange('A2').format.font = { name: 'Times New Roman', size: 15, bold: true };
  sh.getRange('A3').values = [[`${item.author} | Stand ${item.date} | EUR`]];
  sh.getRange('A3').format.font = { italic: true, color: '#555555' };
  let headers, data, formulaCells = [], end, noteRow;
  if (item.kind === 'opos') {
    headers = ['Rechnung', 'Fällig am', 'Brutto EUR', 'Gebucht EUR', 'Beleg', 'Offen EUR'];
    data = item.rows.map(r => [r[0], date(r[1]), r[2], r[3], r[4], null]);
    sh.getRange('A6:F9').values = data;
    for (let i = 0; i < data.length; i++) { const row = i + 6; sh.getRange(`F${row}`).formulas = [[`=C${row}-D${row}`]]; formulaCells.push(`F${row}`); }
    sh.getRange('B6:B9').setNumberFormat('dd.mm.yyyy');
    sh.getRange('C6:D9').format.font.color = '#0000FF';
    sh.getRange('E6:E9').setNumberFormat('  @');
    sh.getRange('C6:D11').setNumberFormat(money); sh.getRange('F6:F11').setNumberFormat(money);
    sh.getRange('A11').values = [['Gesamt']];
    for (const col of ['C','D','F']) sh.getRange(`${col}11`).formulas = [[`=SUM(${col}6:${col}9)`]];
    formulaCells.push('C11','D11','F11'); end = 11; noteRow = 14;
    sh.getRange('A:A').format.columnWidth = 16; sh.getRange('B:B').format.columnWidth = 16;
    sh.getRange('C:D').format.columnWidth = 18; sh.getRange('E:E').format.columnWidth = 40; sh.getRange('F:F').format.columnWidth = 18;
  } else if (item.kind === 'payments') {
    headers = ['Wertstellung', 'Betrag EUR', 'Zuordnung', 'Beleg', 'Laufend EUR'];
    data = item.rows.map(r => [date(r[0]), r[1], r[2], r[3], null]);
    sh.getRange('A6:E10').values = data;
    sh.getRange('A6:A10').setNumberFormat('dd.mm.yyyy'); sh.getRange('B6:B10').format.font.color = '#0000FF';
    sh.getRange('C6:D10').setNumberFormat('  @');
    for (let i=0;i<data.length;i++) {const r=i+6;sh.getRange(`E${r}`).formulas=[[`=SUM($B$6:B${r})`]];formulaCells.push(`E${r}`);}
    sh.getRange('A12:A14').values = [['Altbestand'],['Neulieferung'],['Gesamteingang']];
    sh.getRange('B12').formulas = [['=SUMIF(C6:C10,A12,B6:B10)']];
    sh.getRange('B13').formulas = [['=SUMIF(C6:C10,A13,B6:B10)']];
    sh.getRange('B14').formulas = [['=SUM(B6:B10)']]; formulaCells.push('B12','B13','B14');
    sh.getRange('B6:B14').setNumberFormat(money);sh.getRange('E6:E10').setNumberFormat(money);
    sh.getRange('A:A').format.columnWidth=20;sh.getRange('B:B').format.columnWidth=18;
    sh.getRange('C:C').format.columnWidth=20;sh.getRange('D:D').format.columnWidth=43;sh.getRange('E:E').format.columnWidth=18;
    end=14;noteRow=17;
  } else if(item.kind==='loans') {
    headers=['Konto','Auszahlung EUR','Rückzahlung EUR','Beleg','Rest EUR'];
    data=item.rows.map(r=>[r[0],r[1],r[2],r[3],null]);
    sh.getRange('A6:E8').values=data;
    sh.getRange('D6:D8').setNumberFormat('  @');
    for(let i=0;i<data.length;i++){const r=i+6;sh.getRange(`E${r}`).formulas=[[`=B${r}-C${r}`]];formulaCells.push(`E${r}`);}
    sh.getRange('A10').values=[['Gesamt']];
    for(const col of ['B','C','E']){sh.getRange(`${col}10`).formulas=[[`=SUM(${col}6:${col}8)`]];formulaCells.push(`${col}10`);}
    sh.getRange('B6:C8').format.font.color='#0000FF';sh.getRange('B6:C10').setNumberFormat(money);sh.getRange('E6:E10').setNumberFormat(money);
    sh.getRange('A:A').format.columnWidth=25;sh.getRange('B:C').format.columnWidth=21;sh.getRange('D:D').format.columnWidth=43;sh.getRange('E:E').format.columnWidth=18;
    end=10;noteRow=13;
  } else if(item.kind==='bank') {
    headers=['Position','Betrag EUR','Erläuterung'];
    data=item.rows.map((r,i)=>[r[0],r[1],['12_Bank_Bestaetigung.pdf','16_Kontoauszug_Auswahl.pdf','10_Bank_Buergschaft.pdf'][i]]);
    sh.getRange('A6:C8').values=data;sh.getRange('B6:B8').format.font.color='#0000FF';
    sh.getRange('C6:C10').setNumberFormat('  @');
    sh.getRange('A10').values=[['Restkapital nach Zahlung']];sh.getRange('B10').formulas=[['=B6-B7']];formulaCells.push('B10');
    sh.getRange('C10').values=[['Nur Kapital; Zinsen und Kosten nicht enthalten']];
    sh.getRange('B6:B10').setNumberFormat(money);
    sh.getRange('A:A').format.columnWidth=38;sh.getRange('B:B').format.columnWidth=21;sh.getRange('C:C').format.columnWidth=54;
    end=10;noteRow=13;
  } else throw new Error(item.kind);
  const last=String.fromCharCode(64+headers.length);
  sh.getRange(`A5:${last}5`).values=[headers];
  sh.getRange(`A5:${last}5`).format={fill:'#293C50',font:{name:'Times New Roman',size:11,color:'#FFFFFF',bold:true},rowHeight:32,wrapText:true,horizontalAlignment:'center'};
  sh.getRange(`A${end}:${last}${end}`).format.font.bold=true;
  sh.getRange(`A${end}:${last}${end}`).format.borders={top:{style:'thin',color:'#8192A0'}};
  for(const addr of formulaCells) sh.getRange(addr).format.font.color='#111111';
  const notes=[item.note,'Blaue Beträge sind Eingaben aus den bezeichneten Belegen. Schwarze Beträge sind Formeln. Änderungen an Eingaben aktualisieren den Abgleich.', 'Weitere Vorgänge unterhalb der Einzelzeilen ergänzen und Summenbereiche entsprechend erweitern. Die Tabelle betrifft nur die hier bezeichneten Vorgänge.'];
  for(let i=0;i<notes.length;i++){
    const row=noteRow+i*3;sh.mergeCells(`A${row}:${last}${row+1}`);sh.getRange(`A${row}`).values=[[notes[i]]];sh.getRange(`A${row}:${last}${row+1}`).format={wrapText:true,font:{name:'Times New Roman',size:11,color:'#555555'},verticalAlignment:'top'};
  }
  const before = sh.getRange(item.kind==='bank'?'B10':item.kind==='opos'?'F11':item.kind==='payments'?'B14':'E10').values[0][0];
  const driver = item.kind==='opos'?'D6':item.kind==='payments'?'B6':item.kind==='loans'?'C6':'B7';
  const previous=sh.getRange(driver).values[0][0];sh.getRange(driver).values=[[previous+100]];wb.recalculate();
  const after=sh.getRange(item.kind==='bank'?'B10':item.kind==='opos'?'F11':item.kind==='payments'?'B14':'E10').values[0][0];
  if(Number(after)!==Number(before)+(item.kind==='payments'?100:-100))throw new Error(`Input change failed: ${item.name}: ${before}/${after}`);
  sh.getRange(driver).values=[[previous]];wb.recalculate();
  const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:3000});
  await fs.writeFile(path.join(qa,item.name+'.inspection.json'),JSON.stringify({name:item.name,before,changed:after,errors:errors.ndjson,formulas:formulaCells.map(a=>[a,sh.getRange(a).formulas[0][0],sh.getRange(a).values[0][0]])},null,2));
  const preview=await wb.render({sheetName:'Abgleich',range:`A1:${last}${noteRow+7}`,scale:1.5,format:'png'});
  await fs.writeFile(path.join(qa,item.name+'.png'),new Uint8Array(await preview.arrayBuffer()));
  const output=path.join(root,'testakten',c.slug,item.name);await fs.mkdir(path.dirname(output),{recursive:true});
  const file=await SpreadsheetFile.exportXlsx(wb);await file.save(output);
  try { await fs.rename(output+'.inspect.ndjson', path.join(qa,item.name+'.export-inspect.ndjson')); } catch (e) { if(e.code!=='ENOENT') throw e; }
  reports.push({file:output,total:before,formulas:formulaCells.length,input_change_test:true});
}
await fs.writeFile(path.join(qa,'xlsx-checks.json'),JSON.stringify(reports,null,2));
console.log(JSON.stringify(reports));

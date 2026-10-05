/** Kleine Rechenlisten der kommunalen Haftpflichtakten, keine Deckungsmodelle. */
import fs from 'node:fs/promises';
import path from 'node:path';
import { loadWorkbookRuntime } from './akten-workbook-runtime.mjs';
const { Workbook, SpreadsheetFile, requireRuntime } = await loadWorkbookRuntime(['jszip']);
const JSZip=requireRuntime('jszip');
const [outputDir,qaDir]=process.argv.slice(2);
if(!outputDir||!qaDir)throw new Error('Ausgabe- und QA-Ordner angeben.');
await fs.mkdir(outputDir,{recursive:true});await fs.mkdir(qaDir,{recursive:true});
const money='#,##0.00;(#,##0.00);"–"';
const checks=[];const cases=[];
function create(slug,file,name,title,context,rows){
 const wb=Workbook.create(),s=wb.worksheets.add(name);
 s.showGridLines=false;s.tabColor='#535353';
 s.getRange(`A1:F${rows}`).format={font:{name:'Arial',size:10,color:'#242424'},verticalAlignment:'center',rowHeight:25};
 [38,17,18,20,4,60].forEach((w,i)=>s.getRangeByIndexes(0,i,rows,1).format.columnWidth=w);
 s.getRange('A1:F1').format.rowHeight=8;
 s.getRange('A2').values=[[title]];s.getRange('A2').format.font={name:'Arial',size:15,bold:true};
 s.getRange('A3:F3').format.borders.bottom={style:'thin',color:'#AAAAAA'};
 s.getRange('A4').values=[[context]];s.getRange('A4').format.font={name:'Arial',size:10,italic:true,color:'#555555'};
 const item={slug,file,name,wb,s,rows};cases.push(item);return item;
}
function head(s,row,values){s.getRange(`A${row}:D${row}`).values=[values];s.getRange(`A${row}:D${row}`).format={fill:'#E7E7E7',font:{name:'Arial',size:10,bold:true},wrapText:true,rowHeight:36,horizontalAlignment:'center'};s.getRange(`F${row}`).values=[['Beleg und Stand']];s.getRange(`F${row}`).format.font.bold=true;}
function total(s,row,label,formula){s.getRange(`A${row}`).values=[[label]];s.getRange(`D${row}`).formulas=[[formula]];s.getRange(`A${row}:D${row}`).format={borders:{top:{style:'thin',color:'#888888'}},font:{name:'Arial',size:10,bold:true},rowHeight:30};}
const pipe=create('akha-wuerzburg-rohrbruch','12_Kostenliste.xlsx','Kostenliste','Zimt & Zange: angemeldete Kosten','Gundula Pfennig, Kommunalversorgung Mainbogen GmbH, Stand 05.10.2026',18);
head(pipe.s,6,['Position','Menge','Ansatz EUR','Angemeldet EUR']);
pipe.s.getRange('A7:D10').values=[['Trocknung',1,2400,null],['Elektroarbeiten',1,1800,null],['Vorführmühlen, Neupreis',3,2500,null],['Schließtage, Nettoumsatz',4,850,null]];
pipe.s.getRange('F7:F10').values=[['04: Rechnung bezahlt; netto 2.400, brutto 2.856 EUR'],['06: Angebot, noch nicht beauftragt; netto'],['05: drei gebrauchte Mühlen; Neupreis telefonisch'],['10: Umsatz, ersparte Kosten und Nachholungen offen']];
for(let r=7;r<=10;r++)pipe.s.getRange(`D${r}`).formulas=[[`=B${r}*C${r}`]];
total(pipe.s,12,'Angemeldete Summe','=SUM(D7:D10)');
pipe.s.getRange('F12').values=[['Summe der Anmeldung, keine geprüfte Ersatzleistung.']];
pipe.s.getRange('A14').values=[['Beträge ohne Umsatzsteuer gemäß E-Mail 07. Kein zusätzlicher Umsatzsteueransatz.']];
pipe.s.getRange('A16').values=[['Reparaturfähigkeit, Zeitwerte und mögliche Restwerte der Mühlen sind noch ungeklärt.']];
pipe.s.getRange('A18').values=[['Deckung und Rückdeckung sind in dieser Liste nicht berechnet. Vertragsunterlagen fehlen.']];
const car=create('akha-wuerzburg-betriebsfahrzeug','12_Forderungsuebersicht.xlsx','Forderungen','Fahrzeug 7: drei Anmeldungen','Gundula Pfennig, Frankenbogen Kommunalversicherung VVaG, Stand 05.10.2026',22);
head(car.s,6,['Anspruchstellerin','Anzahl','Ansatz EUR','Angemeldet EUR']);
car.s.getRange('A7:D9').values=[['Hofbogen Immobilien GmbH',1,145000,null],['Prisma Bühnenbildtechnik GmbH',1,1650000,null],['Nuri Nudelwerk GmbH',1,45000,null]];
car.s.getRange('F7:F9').values=[['07/04: Gebäudeangebot, noch nicht beauftragt; netto'],['08/05: gebrauchte Geräte, Neupreisansätze; netto'],['09: Nettoumsatz, keine eigene Sachbeschädigung gemeldet']];
for(let r=7;r<=9;r++)car.s.getRange(`D${r}`).formulas=[[`=B${r}*C${r}`]];
total(car.s,11,'Angemeldete Summe','=SUM(D7:D9)');
car.s.getRange('F11').values=[['Keine Addition anerkannter oder gedeckter Ansprüche.']];
car.s.getRange('A14').values=[['Prisma: ungeprüfte Spanne laut technischer Leitung (nur Geräte)']];
car.s.getRange('A16:D16').values=[['Unterer Schätzansatz',null,1200000,null]];
car.s.getRange('A17:D17').values=[['Oberer Schätzansatz',null,2100000,null]];
car.s.getRange('F16:F17').values=[['05: Reparaturumfang und Ersatzbeschaffung offen'],['05: weder Gutachten noch Deckungsgrenze']];
car.s.getRange('A19').values=[['Die Spanne wird nicht zur Anmeldung addiert. Gebäude und Nachbarumsatz sind nicht enthalten.']];
car.s.getRange('A21').values=[['Bewertung, Umsatzabgrenzung und Anspruchsgrundlagen sind getrennt zu prüfen.']];
car.s.getRange('A22').values=[['Deckungs- und Rückdeckungsbeträge bleiben ohne vollständige Verträge offen.']];
function check(item,address,expected){const actual=item.s.getRange(address).values[0][0];if(typeof actual!=='number'||Math.abs(actual-expected)>1e-6)throw Error(`${item.name}!${address}: ${actual} != ${expected}`);checks.push({case:item.slug,sheet:item.name,cell:address,actual,expected});}
for(const item of cases){
 const{s,wb,rows}=item;
 s.getRange(`B7:D${rows}`).format.horizontalAlignment='right';s.getRange(`C7:D${rows}`).setNumberFormat(money);
 s.getRange(`B7:C${item===pipe?10:9}`).format.fill='#FFF4D0';
 s.getRange(`F7:F${rows}`).format.font.color='#565656';
 for(let r=5;r<=rows;r++){const values=s.getRange(`A${r}:F${r}`).values[0];if(values.every(x=>x===null||x===''))s.getRange(`A${r}:F${r}`).format.rowHeight=9;}
 wb.recalculate();
}
check(pipe,'D12',15100);check(pipe,'D9',7500);check(pipe,'D10',3400);check(car,'D11',1840000);
pipe.s.getRange('B10').values=[[0]];pipe.wb.recalculate();check(pipe,'D12',11700);pipe.s.getRange('B10').values=[[4]];
car.s.getRange('C8').values=[[1200000]];car.wb.recalculate();check(car,'D11',1390000);car.s.getRange('C8').values=[[1650000]];
async function printSetup(file){
 const z=await JSZip.loadAsync(await fs.readFile(file));
 for(const n of Object.keys(z.files).filter(n=>/^xl\/worksheets\/sheet\d+\.xml$/.test(n))){let xml=await z.file(n).async('string');const p=xml.match(/<(\w+:)?worksheet\b/)[1]??'';xml=xml.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'').replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,`<${p}pageMargins left="0.3" right="0.3" top="0.35" bottom="0.35" header="0.15" footer="0.15"/>`);xml=xml.replace(new RegExp(`</${p}worksheet>`),`<${p}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="1"/></${p}worksheet>`);z.file(n,xml);}
 await fs.writeFile(file,await z.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
}
for(const item of cases){
 const {wb,s,slug,file,name,rows}=item;wb.recalculate();check(item,item===pipe?'D12':'D11',item===pipe?15100:1840000);
 const inspected=await wb.inspect({kind:'table',range:`'${name}'!A1:F${rows}`,include:'values,formulas',tableMaxRows:rows,tableMaxCols:6});await fs.writeFile(path.join(qaDir,slug+'-inspect.ndjson'),inspected.ndjson);
 const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},summary:'final formula error scan'});await fs.writeFile(path.join(qaDir,slug+'-errors.ndjson'),errors.ndjson);
 for(const row of s.getRange(`A1:F${rows}`).values)for(const v of row)if(typeof v==='string'&&/^#(?:REF!|DIV\/0!|VALUE!|NAME\?|N\/A|NUM!|NULL!|SPILL!|CALC!)/.test(v))throw Error(v);
 const img=await wb.render({sheetName:name,range:`A1:F${rows}`,scale:1.4,format:'png'});await fs.writeFile(path.join(qaDir,slug+'.png'),new Uint8Array(await img.arrayBuffer()));
 const dir=path.join(outputDir,slug);await fs.mkdir(dir,{recursive:true});const out=path.join(dir,file);await(await SpreadsheetFile.exportXlsx(wb)).save(out);await printSetup(out);
 try{await fs.rename(out+'.inspect.ndjson',path.join(qaDir,slug+'-export.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 console.log(out);
}
await fs.writeFile(path.join(qaDir,'tabellen-pruefung.json'),JSON.stringify({status:'pass',workbooks:2,worksheets:2,checks},null,2)+'\n');

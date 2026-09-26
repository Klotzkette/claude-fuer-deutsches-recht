#!/usr/bin/env node
// Autor: Klotzkette. Individuelle Rechenwerke, gemeinsame Formatierungsfunktionen.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';

const {Workbook, SpreadsheetFile} = await loadWorkbookRuntime();
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const option=(name)=>{const i=process.argv.indexOf(name);if(i<0||!process.argv[i+1])throw new Error(`${name} fehlt`);return process.argv[i+1];};
const data=JSON.parse(await fs.readFile(option('--data'),'utf8'));
const qa=path.resolve(option('--qa'));await fs.mkdir(qa,{recursive:true});
const money='[$-407]#,##0.00';
const put=(s,a,v)=>{s.getRange(a).values=[[v]];};
const formula=(s,a,v)=>{s.getRange(a).formulas=[[v]];};
const val=(s,a)=>s.getRange(a).values[0][0];
function sheet(w,name,title,sub,widths,end){
  const s=w.worksheets.add(name);s.showGridLines=false;
  const last=String.fromCharCode(64+widths.length);
  s.getRange(`A1:${last}${end}`).format={font:{name:'Arial',size:11,color:'#202629'},rowHeight:18,verticalAlignment:'center'};
  widths.forEach((width,i)=>{s.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}${end}`).format.columnWidthPx=width;});
  put(s,'A2',title);s.getRange('A2').format.font={name:'Arial',size:15,bold:true};put(s,'A3',sub);
  return s;
}
function header(s,range,row){s.getRange(range).values=[row];s.getRange(range).format={fill:'#354c58',font:{name:'Arial',size:11,color:'#ffffff',bold:true},rowHeight:29,wrapText:true,horizontalAlignment:'center'};}
async function finish(w,phase,num,ranges,checks){
  w.recalculate();
  for(const [s,a,expected] of checks)assert(Math.abs(val(w.worksheets.getItem(s),a)-expected)<.0001,`${s}!${a}`);
  const inspect=await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:30},maxChars:2000});
  assert(!/"value"\s*:\s*"#/.test(inspect.ndjson),inspect.ndjson);
  const name=data.files[phase][num].filename;
  await fs.writeFile(path.join(qa,name+'.inspect.ndjson'),inspect.ndjson);
  for(const [sheetName,range] of ranges){
    const preview=await w.render({sheetName,range,scale:1.3,format:'png'});
    await fs.writeFile(path.join(qa,`phase-${phase}-${sheetName}.png`),new Uint8Array(await preview.arrayBuffer()));
  }
  const out=await SpreadsheetFile.exportXlsx(w);const dest=path.join(root,'testakten',data.cases[phase].slug,name);await out.save(dest);
  try{await fs.rename(dest+'.inspect.ndjson',path.join(qa,name+'.export.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
  console.log(dest);
}

if(data.cases['7']){
  const w=Workbook.create();const s=sheet(w,'Planer-LV','Bibliothek Hasebogen, Planerpreise','Ole Venn | 24.08.2026 | HM-26-F01',[75,310,90,80,125,135],27);
  put(s,'A5','Nettosumme EUR');formula(s,'F5','=IF(COUNT(F10:F17)=8,SUM(F10:F17),"")');
  put(s,'A6','Umsatzsteuer');put(s,'E6',.19);formula(s,'F6','=IF(COUNT(F5)=1,ROUND(F5*E6,2),"")');s.getRange('E6').setNumberFormat('0%');
  put(s,'A7','Gesamt brutto EUR');formula(s,'F7','=IF(COUNT(F5:F6)=2,SUM(F5:F6),"")');s.getRange('F5:F7').setNumberFormat(money);
  header(s,'A9:F9',['Pos.','Leistung','Menge','Einheit','EP netto EUR','GP netto EUR']);
  data.lv7.forEach((p,i)=>{const r=i+10;s.getRange(`A${r}:E${r}`).values=[[p[0],p[1],data.q7[i],p[2],data.ep7[i]]];formula(s,`F${r}`,`=IF(COUNT(C${r},E${r})=2,ROUND(C${r}*E${r},2),"")`);});
  s.getRange('C10:C17').setNumberFormat('[$-407]0.00');s.getRange('E10:F17').setNumberFormat(money);s.getRange('C10:E17').format.font.color='#245f83';
  put(s,'A20','Mengen und Leistungsumfang: Langtext-LV vom 24.08.2026 und F-04 B.');
  put(s,'A21','Preise: Kostenansatz Konturhaus vom 24.08.2026, keine Unternehmerpreise.');
  put(s,'A23','Budget Fensterlos netto EUR');put(s,'F23',45000);s.getRange('F23').setNumberFormat(money);
  put(s,'A25','Aufgestellt: Ole Venn. Die Steuerzeile folgt der Projektkalkulation mit 19 Prozent.');
  w.recalculate();assert.equal(val(s,'F5'),39736);
  const old=val(s,'E10');put(s,'E10',old+100);w.recalculate();assert.equal(val(s,'F5'),39836);put(s,'E10',old);
  put(s,'E10',null);w.recalculate();assert.equal(val(s,'F5'),'');put(s,'E10',0);w.recalculate();assert.equal(val(s,'F5'),37936);put(s,'E10',old);
  await finish(w,7,6,[['Planer-LV','A1:F26']],[['Planer-LV','F5',39736],['Planer-LV','F7',47285.84]]);
}

if(data.cases['8']){
  const w=Workbook.create();const s=sheet(w,'Kostenjournal','Kita Mühlenwiese, Kostenjournal','Fenja Rost | 17.08.2026 | Vertrags- und Rechnungseingangsstand',[235,130,125,130,130,85,145],28);
  put(s,'A5','Verträge mit Änderungen netto EUR');formula(s,'D5','=SUM(D11:D16)');
  put(s,'A6','Rechnungseingang netto EUR');formula(s,'E6','=SUM(E11:E16)');
  put(s,'A7','Rechnungseingang brutto EUR');formula(s,'G7','=SUM(G11:G16)');
  header(s,'A10:G10',['Gewerk / Bezug','Vertrag netto','Änderung netto','Summe netto','Rechnung netto','Steuer','Rechnung brutto']);
  const rows=[['Rohbau, SR-H2607',168000,0,168000,.19],['Dach, AD-26081',36986,900,39640,.19],['Fenster/Türen, LK-2608',44000,1200,45200,.19],['Elektro, EW-2608',62000,0,61500,.19],['Planung, RA-2606',78000,0,60000,.19],['Gebühren, G-26-041',3500,0,3500,0]];
  rows.forEach((row,i)=>{const r=i+11;s.getRange(`A${r}:C${r}`).values=[[row[0],row[1],row[2]]];formula(s,`D${r}`,`=SUM(B${r}:C${r})`);put(s,`E${r}`,row[3]);put(s,`F${r}`,row[4]);formula(s,`G${r}`,`=ROUND(E${r}*(1+F${r}),2)`);});
  s.getRange('B11:E16').setNumberFormat(money);s.getRange('G11:G16').setNumberFormat(money);s.getRange('F11:F16').setNumberFormat('0%');
  for(const a of ['D5','E6','G7'])s.getRange(a).setNumberFormat(money);
  put(s,'A19','Quelle: Kassenordner VM-26, Rechnungseingänge bis 17.08.2026.');
  put(s,'A20','Eingangsrechnungen sind erfasst, nicht durch diese Tabelle technisch geprüft.');
  put(s,'A21','Dach: Vertrag 10.04. und N1 11.07.; Rechnung AD-26081. N2 steht nur in der Rechnung.');
  put(s,'A22','Andere Schlussbelege verwahrt die Kasse; in dieser Dachakte nicht als Original enthalten.');
  put(s,'A24','Gebühren ohne Umsatzsteuer. Zahlungen stehen im gesonderten Journal, nicht in Spalte E.');
  put(s,'A26','Erfasst: Fenja Rost. Planung: Abschlagsstand, noch keine Schlussrechnung.');
  w.recalculate();assert.equal(val(s,'D5'),394586);assert.equal(val(s,'E6'),377840);
  const old=val(s,'E12');put(s,'E12',old+100);w.recalculate();assert(Math.abs(val(s,'G7')-449083.6)<.0001);put(s,'E12',old);
  await finish(w,8,12,[['Kostenjournal','A1:G27']],[['Kostenjournal','D5',394586],['Kostenjournal','E6',377840],['Kostenjournal','G7',448964.6]]);
}

if(data.cases['9']){
  const w=Workbook.create();const s=sheet(w,'Sicherungen','Rathaus Westflügel, Sicherungseinbehalte','Kasse | 24.09.2026 | Konto 8842, keine Bankverbindung',[225,145,95,145,140,145],25);
  put(s,'A5','Bestand Einbehalte EUR');formula(s,'F5','=SUM(F10:F11)');s.getRange('F5').setNumberFormat(money);
  header(s,'A9:F9',['Vertrag / Kreditor','Abrechnung brutto','Satz','Einbehalt EUR','Freigaben EUR','Bestand EUR']);
  s.getRange('A10:C11').values=[['UR-21-D / Ilmenaudach',92820,.05],['UR-21-M / Heideprofil',56882,.05]];
  for(const r of [10,11]){formula(s,`D${r}`,`=ROUND(B${r}*C${r},2)`);put(s,`E${r}`,0);formula(s,`F${r}`,`=D${r}-E${r}`);}
  s.getRange('B10:B11').setNumberFormat(money);s.getRange('C10:C11').setNumberFormat('0%');s.getRange('D10:F11').setNumberFormat(money);
  put(s,'A14','Quelle: Sicherungskonto 8842, Buchungen 18.11. und 16.12.2021.');
  put(s,'A15','Beide Beträge sind Bareinbehalte aus Schlusszahlungen; keine Bürgschaft abgelöst.');
  put(s,'A17','Dach: Abnahme 15.10.2021. Metallbau: Abnahme 12.11.2021.');
  put(s,'A18','Jeweilige Vertragsvereinbarung: fünf Jahre ab Abnahme; Rückgabe nach Sicherungsabrede.');
  put(s,'A20','Es liegt am 24.09.2026 keine Auszahlungsanordnung vor.');
  put(s,'A21','Der Kassenbestand trifft keine Aussage zur Freigabefähigkeit oder Anspruchshöhe.');
  put(s,'A23','Erfasst: Rike Born, Stadtkasse. Originalbelege im Vertragsordner UR-21.');
  w.recalculate();assert.equal(val(s,'F5'),7485.1);put(s,'E10',1000);w.recalculate();assert.equal(val(s,'F5'),6485.1);put(s,'E10',0);
  await finish(w,9,12,[['Sicherungen','A1:F24']],[['Sicherungen','D10',4641],['Sicherungen','D11',2844.1],['Sicherungen','F5',7485.1]]);
}

#!/usr/bin/env node
// Autor: Klotzkette. Tabellen werden ausschließlich mit artifact_tool erstellt.
import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook, SpreadsheetFile} = await loadWorkbookRuntime();
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const dir = path.join(root,'testakten/bauwirtschaft-vergabeverfahren-feuerwehrhaus-northeim');
const qa = '/tmp/bauwirtschaft-assets/.northeim-qa';
await fs.mkdir(qa,{recursive:true});
const data = JSON.parse(await fs.readFile(path.join(qa,'build-data.json'),'utf8'));
const money = '[$-407]#,##0.00';
const put = (s,a,v) => {s.getRange(a).values=[[v]];};
const f = (s,a,v) => {s.getRange(a).formulas=[[v]];};
const get = (s,a) => s.getRange(a).values[0][0];
const near = (a,b) => assert(Math.abs(a-b)<0.00001,`${a} != ${b}`);
function sheet(wb,name,widths,rows) {
  const s=wb.worksheets.add(name);s.showGridLines=false;
  s.getRange(`A1:${String.fromCharCode(64+widths.length)}${rows}`).format={font:{name:'Arial',size:11,color:'#20292d'},rowHeight:25,verticalAlignment:'center'};
  widths.forEach((w,i)=>s.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}${rows}`).format.columnWidthPx=w);
  s.getRange('A2').format.font={name:'Arial',size:15,bold:true};
  return s;
}
function header(s,r,values) {
  s.getRange(r).values=[values];
  s.getRange(r).format={fill:'#34474c',font:{name:'Arial',size:11,bold:true,color:'#ffffff'},rowHeight:36,wrapText:true,horizontalAlignment:'center'};
}
async function finish(wb,name,ranges) {
  wb.recalculate();
  const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:50},maxChars:3000});
  assert(!/"value"\s*:\s*"#/.test(errors.ndjson),errors.ndjson);
  await fs.writeFile(path.join(qa,name+'.inspect.ndjson'),errors.ndjson);
  for(const [sheetName,range] of ranges) {
    const preview=await wb.render({sheetName,range,scale:1.2,format:'png'});
    await fs.writeFile(path.join(qa,`${name}-${sheetName}.png`),new Uint8Array(await preview.arrayBuffer()));
  }
  const out=await SpreadsheetFile.exportXlsx(wb);await out.save(path.join(dir,name));
  await fs.rename(path.join(dir,name+'.inspect.ndjson'),path.join(qa,name+'.export.ndjson'));
  console.log(name);
}
async function offer(bidder=null) {
  const wb=Workbook.create();
  const s=sheet(wb,bidder?'Angebot':'Preisblatt',[325,155,140,145,150],31);
  const lv=sheet(wb,'LV',[90,510,70,80,130,140],31);
  put(s,'A2',bidder?'Angebot Los 430 Lüftung':'Preisblatt Los 430 Lüftung');
  put(s,'A3','NO-FH26-L430 · Feuerwehrhaus Northeim');
  put(s,'A5',bidder?.name || 'Stadt Northeim · Ausgabe 29.07.2026');
  put(s,'A6',bidder?.address || 'Angebotsfrist 31.08.2026 um 10:00 Uhr MESZ');
  put(s,'A7',bidder?`Erklärt durch ${bidder.person}, Geschäftsführung, ${bidder.date}`:'Mengen und Texte gemäß Vergabeunterlagen vom 29.07.2026');
  put(s,'A9','Summe der Positionen netto EUR');f(s,'B9',"=IF(COUNT(LV!E6:E25)=20,SUM(LV!F6:F25),\"\")");
  put(s,'A10','Unbedingter Nachlass');put(s,'B10',0);s.getRange('B10').setNumberFormat('0.00%');
  put(s,'A11','Angebotssumme netto EUR');f(s,'B11','=IF(B9="","",ROUND(B9*(1-B10),2))');
  put(s,'A12','Umsatzsteuer');put(s,'B12',0.19);s.getRange('B12').setNumberFormat('0%');
  put(s,'A13','Umsatzsteuerbetrag EUR');f(s,'B13','=IF(B11="","",ROUND(B11*B12,2))');
  put(s,'A14','Angebotssumme brutto EUR');f(s,'B14','=IF(B11="","",SUM(B11,B13))');
  for(const addr of ['B9','B11','B13','B14'])s.getRange(addr).setNumberFormat(money);
  s.getRange('A14:B14').format.fill='#e6ecec';s.getRange('A14:B14').format.font.bold=true;
  put(s,'A16','Hersteller und Typ Position 01.020');put(s,'B16',bidder?.device || '');
  put(s,'A18',bidder?'Wir bieten alle 20 Positionen ohne Vorbehalt an. Es gelten die Vergabeunterlagen':'Einheitspreise sind im Blatt LV einzutragen; leere Preise ergeben keine Angebotssumme.');
  put(s,'A19',bidder?'vom 29.07.2026 und die Antwort vom 14.08.2026. Eigene AGB gelten nicht.':'Auch ein Einheitspreis von 0,00 EUR ist eine eigenständige Preisangabe.');
  put(s,'A20',bidder?'Bindung bis 30.10.2026, 24:00 Uhr. Ausführung 02.11.2026 bis 30.04.2027.':'Quelle der Mengen und Leistungsmerkmale: 03_vergabeunterlagen.docx, Abschnitte 2 bis 4.');
  put(s,'A21',bidder?'Sämtliche Arbeiten erfolgen in Eigenleistung. Es gibt keine Eignungsleihe.':'Die Spalten Menge und Einheit sind unverändert zu übernehmen.');
  put(s,'A22',bidder?'Die Eigenerklärung ist Bestandteil dieses Angebots. Es werden keine Nebenangebote abgegeben.':'Quelle des Umsatzsteuersatzes: Vorgabe der Vergabestelle, Angebotsformular Abschnitt 3.');
  put(s,'A24',bidder?`Quelle der Einheitspreise: eigene Kalkulation ${bidder.name}, ${bidder.date}.`:'Die erste Wartung gehört zum zu wertenden Gesamtumfang.');
  if(bidder) {
    put(s,'A25','Mengen und Texte: unverändert aus 04_lv_lueftung.xlsx, Stand 29.07.2026.');
    put(s,'A26','Die ausgeschriebenen technischen Mindestwerte werden zugesagt.');
    if(bidder.short==='weserklima') {
      put(s,'A27','FW 6200: SFP 1,74 kW/(m³/s), Wärmerückgewinnung 81 %, BACnet/IP.');
      put(s,'A28','Gehäuse 3.100 x 1.550 x 1.750 mm; segmentierte Einbringung, Wartungsgang 0,90 m.');
    } else if(bidder.short==='harzraum') {
      put(s,'A27','NV 6000: SFP 1,71 kW/(m³/s), Wärmerückgewinnung 83 %, BACnet/IP.');
      put(s,'A28','Gehäuse 3.180 x 1.590 x 1.780 mm; segmentierte Einbringung, Wartungsgang 0,90 m.');
    } else {
      put(s,'A27','AL 6000 K: Nachweis der projektspezifischen Werte auf Anforderung.');
      put(s,'A28','Der angebotene Preis umfasst die vollständige Leistung am ausgeschriebenen Betriebspunkt.');
    }
    put(s,'A30',`Erklärende Person: ${bidder.person}. Elektronische Abgabe in Textform.`);
  }
  s.getRange('B16:E16').format.font.color='#1d4f70';
  s.getRange('B10').format.font.color='#1d4f70';
  put(lv,'A2','Leistungsverzeichnis Los 430');put(lv,'A3','NO-FH26-L430 · Mengenstand 29.07.2026 · Preise in EUR netto');
  header(lv,'A5:F5',['Position','Leistung einschließlich Liefer- und Montageumfang','Menge','Einheit','EP EUR','GP EUR']);
  lv.getRange('A6:A25').setNumberFormat('@');
  for(let i=0;i<data.positions.length;i++) {
    const p=data.positions[i], r=i+6;
    lv.getRange(`A${r}:F${r}`).values=[[p[0],p[1]+'. '+p[4],p[2],p[3],bidder?p[bidder.price_col]:null,null]];
    f(lv,`F${r}`,`=IF(E${r}="","",ROUND(C${r}*E${r},2))`);
  }
  lv.getRange('A6:F25').format.rowHeight=60;
  lv.getRange('B6:B25').format.wrapText=true;
  lv.getRange('B7').format.rowHeight=80;
  lv.getRange('E6:F28').setNumberFormat(money);
  lv.getRange('E6:E25').format.font.color='#1d4f70';
  lv.getRange('E6:E25').dataValidation={rule:{type:'decimal',operator:'greaterThanOrEqual',formula1:0}};
  put(lv,'B27','Summe netto vor Nachlass');f(lv,'F27','=IF(COUNT(E6:E25)=20,SUM(F6:F25),"")');
  put(lv,'B29','Mengen/Leistung: Unterlagen vom 29.07.2026.');
  put(lv,'B30',bidder?`Preise: ${bidder.short}, ${bidder.date}.`:'Preise: vom Bieter einzutragen.');
  lv.freezePanes.freezeRows(5);
  wb.recalculate();
  if(bidder) {
    const expected=data.totals[data.bidders.indexOf(bidder)];near(get(s,'B11'),expected);
    near(get(s,'B14'),Math.round(expected*1.19*100)/100);
    const old=get(lv,'E7');put(lv,'E7',old+100);wb.recalculate();near(get(s,'B11'),expected+100);
    put(lv,'E7',null);wb.recalculate();assert.equal(get(s,'B11'),'');
    put(lv,'E7',0);wb.recalculate();near(get(s,'B11'),expected-old);
    put(lv,'E7',old);put(s,'B10',0.02);wb.recalculate();near(get(s,'B11'),Math.round(expected*0.98*100)/100);
    put(s,'B10',0);wb.recalculate();near(get(s,'B11'),expected);
  } else assert.equal(get(s,'B11'),'');
  const name=bidder?`${bidder.id}_angebot_${bidder.short}.xlsx`:'04_lv_lueftung.xlsx';
  await fs.writeFile(path.join(qa,name+'.values.ndjson'),(await wb.inspect({kind:'table',range:`${s.name}!A9:B14`,include:'values,formulas',tableMaxRows:6,tableMaxCols:2,maxChars:4000})).ndjson);
  await finish(wb,name,[[s.name,'A1:E31'],['LV','A1:F31']]);
}
await offer();
for(const b of data.bidders)await offer(b);
const wb=Workbook.create();
const s=sheet(wb,'Preisspiegel',[250,165,165,165,170],31);
put(s,'A2','Preisspiegel Los 430');put(s,'A3','Nora Brandt · 11.09.2026 · sämtliche Werte netto EUR');
header(s,'A5:D5',['Position / Menge','Leinetal','Weserklima','Harzraum']);
data.positions.forEach((p,i)=>{
  const r=i+6;put(s,`A${r}`,`${p[0]} · ${p[2]} ${p[3]}`);
  ['B','C','D'].forEach((col,j)=>put(s,`${col}${r}`,p[j+5]*p[2]));
});
put(s,'A27','Nettosumme');['B','C','D'].forEach(col=>f(s,`${col}27`,`=SUM(${col}6:${col}25)`));
put(s,'A28','Mehrpreis zu Leinetal');['B','C','D'].forEach(col=>f(s,`${col}28`,`=${col}27-$B$27`));
put(s,'A29','Rechnerischer Preisrang');['B','C','D'].forEach(col=>f(s,`${col}29`,`=RANK(${col}27,$B$27:$D$27,1)`));
s.getRange('B6:D28').setNumberFormat(money);
put(s,'A31','Quelle: Angebote 08, 10 und 12, Blatt LV; keine Aussage zur Berücksichtigungsfähigkeit.');
wb.recalculate();data.totals.forEach((t,i)=>near(get(s,`${['B','C','D'][i]}27`),t));
put(s,'B7',178000);wb.recalculate();near(get(s,'B29'),3);put(s,'B7',78000);wb.recalculate();near(get(s,'B29'),1);
await finish(wb,'23_preisspiegel.xlsx',[['Preisspiegel','A1:E31']]);

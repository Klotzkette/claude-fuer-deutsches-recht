#!/usr/bin/env node
// Individuelle Rechenunterlagen, Autor: Klotzkette. Autorenschaft mit Artifact Tool.
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import assert from 'node:assert/strict';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook, SpreadsheetFile} = await loadWorkbookRuntime();
const option = process.argv.indexOf('--qa-dir');
const qa = option >= 0 ? path.resolve(process.argv[option+1]) : path.join(os.tmpdir(),'hoai-4-6-qa');
const data = JSON.parse(await fs.readFile(path.join(qa,'build-data.json'),'utf8'));
const put=(s,a,v)=>{s.getRange(a).values=[[v]];};
const formula=(s,a,v)=>{s.getRange(a).formulas=[[v]];};
const value=(s,a)=>s.getRange(a).values[0][0];
const near=(a,b)=>assert(Math.abs(a-b)<0.000001,`${a} != ${b}`);
function sheet(wb,name,widths,rows) {
  const s=wb.worksheets.add(name);s.showGridLines=false;
  s.getRange(`A1:${String.fromCharCode(64+widths.length)}${rows}`).format={font:{name:'Arial',size:11,color:'#202529'},rowHeight:18,verticalAlignment:'center'};
  widths.forEach((width,i)=>s.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}${rows}`).format.columnWidthPx=width);
  s.getRange('A2').format.font={name:'Arial',size:15,bold:true};s.getRange('A2').format.rowHeight=24;
  return s;
}
function header(s,range,labels) {
  s.getRange(range).values=[labels];
  s.getRange(range).format={fill:'#3d4a52',font:{name:'Arial',size:11,bold:true,color:'#ffffff'},wrapText:true,rowHeight:36,horizontalAlignment:'center'};
}
function input(s,range,format='[$-407]0.00') {
  s.getRange(range).setNumberFormat(format);s.getRange(range).format.font.color='#215774';
  s.getRange(range).format.fill='#f6edcf';
}
async function finish(wb,phase,name,views) {
  for(const [sheetName,range] of views) {
    const s=wb.worksheets.getItem(sheetName);const rows=s.getRange(range).values;
    rows.forEach((values,i)=>{if(values.every(v=>v===null || v===''))s.getRange(`A${i+1}`).format.rowHeight=8;});
  }
  wb.recalculate();
  const result=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:3000});
  assert(!/"value"\s*:\s*"#/.test(result.ndjson),result.ndjson);
  const dir=path.join(qa,`phase-${phase}`,'workbooks');await fs.mkdir(dir,{recursive:true});
  await fs.writeFile(path.join(dir,name+'.errors.ndjson'),result.ndjson);
  for(const [sheetName,range] of views) {
    const inspection=await wb.inspect({kind:'table',range:`${sheetName}!${range}`,include:'values,formulas',tableMaxRows:35,tableMaxCols:8,maxChars:18000});
    await fs.writeFile(path.join(dir,`${name}-${sheetName}.ndjson`),inspection.ndjson);
    const image=await wb.render({sheetName,range,scale:1.3,format:'png'});
    await fs.writeFile(path.join(dir,`${name}-${sheetName}.png`),new Uint8Array(await image.arrayBuffer()));
  }
  const output=path.join(data[phase].directory,name);
  await (await SpreadsheetFile.exportXlsx(wb)).save(output);
  try {await fs.rename(output+'.inspect.ndjson',path.join(dir,name+'.export.ndjson'));} catch(error) {if(error.code!=='ENOENT')throw error;}
  console.log(`LPH ${phase}: ${name}`);
}

if(data['4']) {
  const wb=Workbook.create();const s=sheet(wb,'Flaechen',[225,80,100,100,135,315],29);
  put(s,'A2','Werkhof Uhlenried Flächen');put(s,'A3','FL-01 · Rieke Cordes · 27.08.2026 / Variante ergänzt 18.09.2026');
  header(s,'A5:F5',['Bauteil / Fläche','Anzahl','Länge m','Breite m','Fläche m²','Plan- und Quellenbezug']);
  s.getRange('A6:F10').values=[['Halle beantragt',1,24,15,null,'G-02/B Außenkontur'],['Sozialtrakt',1,12,8,null,'G-02/B Außenkontur'],['Hof und Zufahrt',1,48,18,null,'G-01/B, ohne Pkw und Fahrräder'],['Pkw-Stellplätze',8,5,2.5,null,'G-01/B, acht Stellplätze'],['Fahrradfläche',1,6,3,null,'G-01/B, wasserdurchlässig']];
  for(let r=6;r<=10;r++)formula(s,`E${r}`,`=IF(COUNT(B${r}:D${r})=3,B${r}*C${r}*D${r},"")`);
  input(s,'B6:D10');s.getRange('E6:E24').setNumberFormat('[$-407]#,##0.00');s.getRange('F6:F10').format.wrapText=true;s.getRange('A6:F10').format.rowHeight=30;
  put(s,'A12','Grundstück m²');put(s,'E12',2880);put(s,'F12','V-26-118, 60,00 x 48,00 m');input(s,'E12');
  put(s,'A13','Belegte Flächen m²');formula(s,'E13','=IF(COUNT(E6:E10)=5,SUM(E6:E10),"")');
  put(s,'A14','Restfläche m²');formula(s,'E14','=IF(E13="","",E12-E13)');
  header(s,'A17:F17',['Variante G-03','Anzahl','Länge m','Tiefe m','Fläche m²','Bezug']);
  s.getRange('A18:F18').values=[['Halle verkürzt',1,24,14.7,null,'G-03, nur zur Entscheidung']];input(s,'B18:D18');
  formula(s,'E18','=IF(COUNT(B18:D18)=3,B18*C18*D18,"")');
  put(s,'A19','Differenz Hallenfläche');formula(s,'E19','=IF(OR(E18="",E6=""),"",E18-E6)');
  put(s,'A20','Dachfläche Variante');formula(s,'E20','=IF(OR(E18="",E7=""),"",E18+E7)');
  put(s,'A21','Dachfläche Antrag');formula(s,'E21','=IF(COUNT(E6:E7)=2,SUM(E6:E7),"")');
  put(s,'A24','Nordabstand Antrag m');put(s,'E24',2.7);put(s,'F24','Vermessung, keine Zulässigkeitsprüfung');
  put(s,'A26','Eingaben blau auf hellem Feld. Rechenwerte sind geometrische Flächen, keine Genehmigungsbescheinigung.');
  put(s,'A27','Hof, Pkw-Stellplätze und Fahrradfläche sind getrennte Ansätze. Entwässerung verwendet eigene Anschlussflächen.');
  put(s,'A28','gez. Rieke Cordes · Cordes Bauatelier · CE-WU26');
  wb.recalculate();near(value(s,'E13'),1438);near(value(s,'E14'),1442);near(value(s,'E20'),448.8);
  put(s,'D18',14.6);wb.recalculate();near(value(s,'E20'),446.4);put(s,'D18',null);wb.recalculate();assert.equal(value(s,'E20'),'');put(s,'D18',14.7);
  await finish(wb,4,'06_Flaechen.xlsx',[['Flaechen','A1:F29']]);
}

if(data['5']) {
  const wb=Workbook.create();const s=sheet(wb,'Hoehen',[205,105,105,105,105,115,110,105],25);
  put(s,'A2','Schule Brückenanger Höhenketten');put(s,'A3','HM-BA26 · Lea Wernicke · 15.09.2026 · alle Höhen und Dicken in m');
  header(s,'A5:H5',['Route / Stand','UK Tragwerk','Montage oben','Kanal frei','Dämmung je Seite','Decke unten','Lichte Höhe','Differenz Ziel']);
  s.getRange('A6:H8').values=[['Direkt L-301/D',3.15,.05,.28,.04,.06,null,null],['Seitlich, Studie',3.6,.05,.28,.04,.06,null,null],['Altstand L-301/B',3.15,.05,.20,.04,.06,null,null]];
  input(s,'B6:F8','[$-407]0.000');s.getRange('G6:H8').setNumberFormat('[$-407]0.000');s.getRange('A6:H8').format.rowHeight=30;
  put(s,'A13','Projektziel lichte Höhe');put(s,'B13',2.75);input(s,'B13','[$-407]0.00');put(s,'A14','Entwurfsdecke UK');put(s,'B14',2.8);
  for(let r=6;r<=8;r++) {formula(s,`G${r}`,`=IF(COUNT(B${r}:F${r})=5,B${r}-C${r}-D${r}-2*E${r}-F${r},"")`);formula(s,`H${r}`,`=IF(OR(G${r}="",B13=""),"",G${r}-$B$13)`);}
  s.getRange('H6:H8').conditionalFormats.add('cellIs',{operator:'lessThan',formula:0,format:{fill:'#f4d7d7',font:{color:'#8c2222'}}});
  put(s,'A17','Quellen: T-201/B UK Unterzug 3,15 m, UK Decke 3,60 m; L-301/D Kanal 600 x 280 mm frei.');
  put(s,'A18','Dämmung 40 mm je Seite; Montageabstand 50 mm; Deckenunterkonstruktion 60 mm, Koordination 15.09.2026.');
  put(s,'A19','Seitliche Route ist eine geometrische Studie. Befestigung, Wartung und Abschottung sind nicht bestätigt.');
  put(s,'A20','Altstand zeigt die frühere Kanalhöhe von 200 mm frei; er ist keine bestätigte Alternative zum Fachstand D.');
  put(s,'A22','Blaue Zahlen auf hellem Feld sind Eingaben. Positive Resthöhe ist keine technische Freigabe.');
  put(s,'A24','gez. Lea Wernicke · Nordfeld Architektur');
  wb.recalculate();near(value(s,'G6'),2.68);near(value(s,'G7'),3.13);near(value(s,'H6'),-.07);
  put(s,'B6',3.25);wb.recalculate();near(value(s,'G6'),2.78);put(s,'D6',null);wb.recalculate();assert.equal(value(s,'G6'),'');put(s,'B6',3.15);put(s,'D6',.28);
  await finish(wb,5,'08_Hoehenketten.xlsx',[['Hoehen','A1:H25']]);
}

if(data['6']) {
  {
    const wb=Workbook.create();const s=sheet(wb,'Kosten',[310,170,385],23);
    put(s,'A2','Sporthalle Okerbogen Kostenberechnung');put(s,'A3','KB-03 · Mira Falkenhain · 15.07.2026 · EUR netto');
    header(s,'A5:C5',['Projektseitige Kostengruppe','Betrag EUR','Inhalt / Grundlage']);
    s.getRange('A6:C11').values=[['200 Vorbereitende Maßnahmen',45000,'Freimachung und Anschlussarbeiten'],['300 Baukonstruktion',630000,'Enthält Ausbauanteil 94.000 EUR'],['400 Technische Anlagen',195000,'Fachbeitrag Harms, Stand 10.07.2026'],['500 Außenanlagen',48000,'Zugänge und Entwässerungsanschlüsse'],['600 Ausstattung',17000,'Mobile Sport- und Lagereinrichtung'],['700 Baunebenkosten',130000,'Planung, Fachnachweise und Gebührenansätze']];
    input(s,'B6:B11','[$-407]#,##0.00');s.getRange('A6:C11').format.rowHeight=30;
    put(s,'A13','Kostenberechnung netto');formula(s,'B13','=SUM(B6:B11)');
    put(s,'A14','Gesonderte Reserve');put(s,'B14',65000);input(s,'B14','[$-407]#,##0.00');
    put(s,'A15','Finanzierungsrahmen netto');formula(s,'B15','=B13+B14');
    put(s,'A16','Umsatzsteuer Planannahme');put(s,'B16',.19);s.getRange('B16').setNumberFormat('0%');
    put(s,'A17','Finanzierungsrahmen brutto');formula(s,'B17','=ROUND(B15*(1+B16),2)');s.getRange('B13:B15').setNumberFormat('[$-407]#,##0.00');s.getRange('B17').setNumberFormat('[$-407]#,##0.00');
    put(s,'A20','Ausbauanteil: Boden 30.400, Wände/Oberflächen 38.200, Decken 19.000, Türen 6.400 EUR netto.');
    put(s,'A21','Summe Ausbau 94.000 EUR ist Teil der Kostengruppe 300, nicht zusätzlich zur Kostenberechnung.');
    put(s,'A22','gez. Mira Falkenhain · PE-OB26 · Reserve nicht in Einheitspreisen enthalten');
    wb.recalculate();near(value(s,'B13'),1065000);near(value(s,'B17'),1344700);
    await finish(wb,6,'03_Kostenberechnung.xlsx',[['Kosten','A1:C23']]);
  }
  {
    const wb=Workbook.create();const s=sheet(wb,'Mengen',[240,65,95,95,115,115,120,245],27);
    put(s,'A2','Sporthalle Okerbogen Mengen');put(s,'A3','ML-01 · Mira Falkenhain · 04.09.2026 · geometrischer Abzug aller bezeichneten Öffnungen');
    header(s,'A5:H5',['Ansatz','Anzahl','Maß 1 m','Maß 2 m','Brutto','Abzug','Ergebnis','Quelle / Einheit']);
    s.getRange('A6:H19').values=[
      ['Hallenboden',1,24,12,null,0,null,'A-601/B / m²'],['Hallenwände gesamt',1,72,4.8,null,null,null,'A-602/B / m²'],['Prallwandband',1,72,2,null,null,null,'A-602/B / m²'],['Hallendecke netto',1,24,12,null,null,null,'A-603/B / m²'],['Trennwände Ansicht',1,34,3.2,null,null,null,'A-601/B / m²'],['Oberflächen beidseitig',2,null,1,null,0,null,'zweifache Wandansicht / m²'],['Sozialtrakt Boden',1,18,6,null,0,null,'A-601/B lichte Rechenfläche / m²'],['Reinigung gesamt',1,null,1,null,0,null,'Halle und Trakt / m²'],['Sockel Halle',1,72,1,null,null,null,'Umfang abzüglich Türen / m'],['Sockel Sozialtrakt',1,98,1,null,0,null,'raumweise Längenaufnahme / m'],['Deckenöffnungen',4,.6,.6,null,0,null,'A-603/B R-01 bis R-04 / m²'],['Fensteröffnungen',6,1.5,1.2,null,0,null,'A-602/B / m²'],['Hallentüröffnungen',2,1.26,2.26,null,0,null,'T-05 und T-06 / m²'],['Innentüröffnungen',4,1.01,2.135,null,0,null,'T-01 bis T-04 / m²']];
    for(let r=6;r<=19;r++) {formula(s,`E${r}`,`=IF(COUNT(B${r}:D${r})=3,B${r}*C${r}*D${r},"")`);formula(s,`G${r}`,`=IF(COUNT(E${r}:F${r})=2,E${r}-F${r},"")`);}
    formula(s,'F7','=IF(COUNT(G17:G18)=2,SUM(G17:G18),"")');formula(s,'F8','=IF(COUNT(B18:C18)=2,B18*C18*D8,"")');formula(s,'F9','=G16');formula(s,'F10','=G19');formula(s,'C11','=G10');formula(s,'C13','=IF(COUNT(G6,G12)=2,G6+G12,"")');formula(s,'F14','=B18*C18');
    input(s,'B6:D19','[$-407]0.0000');s.getRange('E6:G19').setNumberFormat('[$-407]0.0000');s.getRange('H6:H19').format.wrapText=true;s.getRange('A6:H19').format.rowHeight=30;
    put(s,'A22','Quelle: A-601/B, A-602/B, A-603/B und Türliste TL-02/B, jeweils 04.09.2026.');
    put(s,'A23','Maße sind lichte projektseitige Rechenmaße. Keine pauschale Übernahme einer DIN-/ATV-Abzugsregel.');
    put(s,'A24','Neue Fachbeiträge nach dem 04.09.2026 sind in dieser Mengenfassung noch nicht eingearbeitet.');
    put(s,'A26','gez. Mira Falkenhain · PE-OB26');
    wb.recalculate();near(value(s,'G8'),138.96);near(value(s,'G9'),286.56);near(value(s,'G10'),100.1746);near(value(s,'G11'),200.3492);
    put(s,'B16',6);wb.recalculate();near(value(s,'G9'),285.84);put(s,'B16',4);
    await finish(wb,6,'06_Mengenermittlung.xlsx',[['Mengen','A1:H27']]);
  }
  {
    const wb=Workbook.create();const s=sheet(wb,'LV',[80,530,100,70,110,125],27);const k=sheet(wb,'Kosten',[375,170,400],25);
    put(s,'A2','Planer-Bepreisung Ausbau LV-AU 02');put(s,'A3','Mira Falkenhain · 14.09.2026 · PE-OB26 · interne Arbeitsannahmen, EUR netto');
    header(s,'A5:F5',['Position','Leistungsbeschreibung','Menge','Einheit','EP EUR','GP EUR']);
    data['6'].positions.forEach((p,i)=>{const r=i+6;s.getRange(`A${r}:F${r}`).values=[[p[0],p[1]+'. '+p[6],p[2],p[3],p[4],null]];formula(s,`F${r}`,`=IF(COUNT(C${r},E${r})=2,ROUND(C${r}*E${r},2),"")`);});
    s.getRange('A6:A21').setNumberFormat('@');s.getRange('B6:B21').format.wrapText=true;s.getRange('A6:F21').format.rowHeight=138;
    input(s,'C6:C21','[$-407]0.0000');input(s,'E6:E21','[$-407]#,##0.00');s.getRange('F6:F24').setNumberFormat('[$-407]#,##0.00');
    put(s,'B23','Summe netto');formula(s,'F23','=IF(COUNT(F6:F21)=16,SUM(F6:F21),"")');
    put(s,'B25','Mengen: ML-01, 04.09.2026. Preise: interne Preisannahmen, 14.09.2026.');s.getRange('B25').format.wrapText=true;s.getRange('A25:F25').format.rowHeight=30;
    s.freezePanes.freezeRows(5);
    put(k,'A2','Ausbau Kostenüberleitung');put(k,'A3','Stand LV-AU/02, 14.09.2026. Spätere Fachbeiträge noch nicht eingerechnet.');
    header(k,'A5:C5',['Vergleichsgröße','EUR netto','Bezug']);
    k.getRange('A6:C6').values=[['Ausbau in Kostenberechnung',94000,'KB-03: gleicher betrachteter Ausbauumfang']];input(k,'B6','[$-407]#,##0.00');
    put(k,'A7','Planer-LV Ausbau');formula(k,'B7','=LV!F23');put(k,'C7','Nur die 16 Positionen dieser Fassung');
    put(k,'A8','Differenz LV zu Kostenberechnung');formula(k,'B8','=IF(B7="","",B7-B6)');
    put(k,'A10','Kostenberechnung Gesamtprojekt');put(k,'B10',1065000);input(k,'B10','[$-407]#,##0.00');
    put(k,'A11','Übriger Umfang aus Kostenberechnung');formula(k,'B11','=B10-B6');
    put(k,'A12','Gesamt mit diesem Planer-LV');formula(k,'B12','=IF(B7="","",B11+B7)');
    put(k,'A14','Reserve gesondert');put(k,'B14',65000);input(k,'B14','[$-407]#,##0.00');
    put(k,'A15','Gesamt einschließlich Reserve');formula(k,'B15','=IF(B12="","",B12+B14)');
    k.getRange('B6:B15').setNumberFormat('[$-407]#,##0.00');k.getRange('A6:C15').format.rowHeight=35;
    put(k,'A19','Restleistungen sind mit KB-03 fortgeführt, nicht bereits durch eigene LV bepreist.');
    put(k,'A20','Der Vergleich ist keine Bestätigung des gesamten Budgets und keine Vergabefreigabe.');
    put(k,'A21','Tür T-04 und zusätzliche Wartungsstellen stammen aus späterer Korrespondenz.');
    put(k,'A23','gez. Mira Falkenhain · Falkenhain Architektur');
    wb.recalculate();const expected=data['6'].positions.reduce((a,p)=>a+Math.round(p[2]*p[4]*100)/100,0);near(value(s,'F23'),expected);
    const old=value(s,'E6');put(s,'E6',old+1);wb.recalculate();near(value(k,'B7'),expected+288);put(s,'E6',null);wb.recalculate();assert.equal(value(s,'F23'),'');put(s,'E6',old);
    await finish(wb,6,'08_Planer_LV.xlsx',[['LV','A1:F27'],['Kosten','A1:C25']]);
  }
  {
    const wb=Workbook.create();const s=sheet(wb,'Termine',[310,150,150,150,320],24);
    put(s,'A2','Sporthalle Okerbogen Vergabetermine');put(s,'A3','Torben Riekert / Mira Falkenhain · 22.09.2026 · Kalendertage');
    put(s,'A5','Geplanter Ausbaubeginn');put(s,'C5',new Date('2027-01-11T00:00:00Z'));s.getRange('C5').setNumberFormat('dd.mm.yyyy');
    header(s,'A7:E7',['Rückwärts gerechneter Vorgang','Dauer Tage','Spätester Beginn','Spätestes Ende','Quelle / Voraussetzung']);
    s.getRange('A8:E11').values=[['Fertigung und Lieferung',35,null,null,'Unverbindliche Annahme, Bestellung nötig'],['Prüfung und Entscheidung',14,null,null,'Interne Vereinsannahme'],['Angebotszeit',21,null,null,'Interne Vereinsannahme, kein Gesetzesminimum'],['Vorstandsprüfung / Versand',7,null,null,'Interner Ablauf, keine Versandfreigabe']];
    formula(s,'D8','=C5');formula(s,'C8','=D8-B8');
    for(let r=9;r<=11;r++){formula(s,`D${r}`,`=C${r-1}`);formula(s,`C${r}`,`=D${r}-B${r}`);}
    input(s,'B8:B11','0');s.getRange('C8:D16').setNumberFormat('dd.mm.yyyy');s.getRange('E8:E11').format.wrapText=true;s.getRange('A8:E11').format.rowHeight=38;
    put(s,'A14','Interner Paketabschluss');put(s,'C14',new Date('2026-10-16T00:00:00Z'));s.getRange('C14').setNumberFormat('dd.mm.yyyy');
    put(s,'A15','Rechnerischer Abstand Tage');formula(s,'C15','=C11-C14');s.getRange('C15').setNumberFormat('0');
    put(s,'A18','Betriebspause 24.12.2026 bis 03.01.2027 ist noch nicht in den 35 Tagen verbindlich geklärt.');
    put(s,'A19','Keine Feiertags-/Arbeitstagsrechnung. Technische Planfreigaben und Beauftragung sind Voraussetzungen.');
    put(s,'A20','Der rechnerische Abstand ist kein gesicherter Puffer, solange Vorläufe und Betriebspause offen sind.');
    put(s,'A22','Quelle: Projektkalender 22.09.2026 und Koordinationsprotokoll desselben Tages.');
    put(s,'A23','gez. Mira Falkenhain · PE-OB26');
    wb.recalculate();near(value(s,'C15'),10);put(s,'B8',42);wb.recalculate();near(value(s,'C15'),3);put(s,'B8',35);
    await finish(wb,6,'13_Vergabetermine.xlsx',[['Termine','A1:E24']]);
  }
}

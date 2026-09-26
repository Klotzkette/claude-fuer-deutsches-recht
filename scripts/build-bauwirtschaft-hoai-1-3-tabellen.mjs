// Individuelle rechnende Originale mit Artifact Tool. Autor: Klotzkette.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath, pathToFileURL} from 'node:url';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const modules=process.env.AKTEN_NODE_MODULES;
if(!modules) throw new Error('AKTEN_NODE_MODULES auf gebündelte Laufzeit setzen.');
const require=createRequire(path.join(modules,'.hoai-1-3-loader.cjs'));
const {Workbook,SpreadsheetFile}=await import(pathToFileURL(require.resolve('@oai/artifact-tool')).href);
const assets=process.env.HOAI_1_3_ASSETS || '/tmp/bauwirtschaft-hoai-1-3-assets';
const qa=path.join(assets,'qa-hoai-1-3'); await fs.mkdir(qa,{recursive:true});
const requested=process.argv.includes('--phase') ? Number(process.argv[process.argv.indexOf('--phase')+1]) : null;
const slugs={1:'bauwirtschaft-hoai-1-grundlagen-kulturhof-detmold',2:'bauwirtschaft-hoai-2-vorplanung-kita-bad-pyrmont',3:'bauwirtschaft-hoai-3-entwurf-aerztehaus-stadthagen'};
const MONEY='[$-407]#,##0.00"  "';
function val(s,cell,value){s.getRange(cell).values=[[value]];}
function input(s,cell,value){val(s,cell,value);s.getRange(cell).format.font.color='#195ba0';}
function formula(s,cell,value){s.getRange(cell).formulas=[[value]];}
function setup(wb,name,title,subtitle,headers,widths){
  const s=wb.worksheets.add(name); const last=String.fromCharCode(64+headers.length);
  s.showGridLines=false;s.getRange(`A1:${last}36`).format.font={name:'Arial',size:11,color:'#111111'};
  s.getRange(`A1:${last}1`).merge();s.getRange(`A2:${last}2`).merge();s.getRange(`A3:${last}3`).merge();
  val(s,'A1',title);s.getRange('A1').format.font={name:'Arial',size:15,bold:true};s.getRange('A1').format.rowHeight=24;
  val(s,'A2',subtitle);s.getRange('A2').format.rowHeight=20;
  s.getRange(`A3:${last}4`).format.rowHeight=12;
  s.getRange(`A5:${last}5`).values=[headers];s.getRange(`A5:${last}5`).format={fill:'#354d45',font:{name:'Arial',size:11,bold:true,color:'#ffffff'},wrapText:true,rowHeight:28,horizontalAlignment:'center',verticalAlignment:'center'};
  s.getRange(`A6:${last}36`).format.rowHeight=14;s.getRange(`A6:${last}36`).format.verticalAlignment='center';
  s.getRange(`A6:${last}36`).format.wrapText=true;
  widths.forEach((w,i)=>s.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}36`).format.columnWidth=w);
  s.freezePanes.freezeRows(5);return s;
}
function note(s,row,text,last='G'){s.getRange(`A${row}:${last}${row}`).merge();val(s,`A${row}`,text);s.getRange(`A${row}:${last}${row}`).format.rowHeight=18;}
function band(s,row,last='G'){s.getRange(`A${row}:${last}${row}`).format.fill='#e8eeeb';s.getRange(`A${row}:${last}${row}`).format.font.bold=true;}
async function finish(wb,phase,name,ranges,probe){
  wb.recalculate();const checks=[];
  for(const [sheetName,range] of ranges){
    const table=await wb.inspect({kind:'table',range:`'${sheetName}'!${range}`,include:'values,formulas',tableMaxRows:36,tableMaxCols:8,maxChars:18000});checks.push(table.ndjson);
    const image=await wb.render({sheetName,range,scale:1.5,format:'png'});
    await fs.writeFile(path.join(qa,`${phase}-${name.slice(0,2)}-${sheetName}.png`),new Uint8Array(await image.arrayBuffer()));
  }
  const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:50},maxChars:2500});
  const out=path.join(root,'testakten',slugs[phase],name);await fs.mkdir(path.dirname(out),{recursive:true});
  await (await SpreadsheetFile.exportXlsx(wb)).save(out);
  try{await fs.rename(out+'.inspect.ndjson',path.join(qa,`${phase}-${name}.inspect.ndjson`));}catch(e){if(e.code!=='ENOENT')throw e;}
  await fs.writeFile(path.join(qa,`${phase}-${name}.artifact.json`),JSON.stringify({phase,name,checks,errors:errors.ndjson,probe},null,2));
  console.log(`Phase ${phase}: ${name}`);
}

if(!requested||requested===1){
  const wb=Workbook.create();const s=setup(wb,'Budget','Kulturhof Untersuchungsbudget','Stiftung Buchenrain Kultur · Hanna Wendt · 17.02.2026 · KD-26-01',
    ['Leistung','Menge','Einheit','Ansatz netto EUR','Netto EUR','Quelle','Stand'],[33,10,10,17,18,23,27]);
  const rows=[
    ['Tragwerkssichtung',1,'psch',1850,'F 26 041','Angebot; kein Auftrag'],
    ['Anfahrt Tragwerk',1,'psch',120,'F 26 041','Angebot; kein Auftrag'],
    ['Materialbegehung',1,'psch',1250,'L 26 118','Angebot; kein Auftrag'],
    ['Einzelproben mit Labor',6,'St',145,'L 26 118','Nur Erdgeschoss'],
    ['Materialbericht',1,'psch',420,'L 26 118','Angebot; kein Auftrag'],
    ['Kleine Öffnungsarbeiten',8,'h',65,'Ansatz Wendt','Noch ohne Angebot'],
    ['Wiederherstellung',1,'psch',150,'Ansatz Wendt','Noch ohne Angebot'],
    ['Bestandsaufmaß',1,'psch',1600,'Ansatz Wendt','Noch ohne Angebot'],
  ];
  rows.forEach((r,i)=>{const k=i+6;s.getRange(`A${k}:D${k}`).values=[r.slice(0,4)];formula(s,`E${k}`,`=IF(OR(B${k}="",D${k}=""),NA(),ROUND(B${k}*D${k},2))`);val(s,`F${k}`,r[4]);val(s,`G${k}`,r[5]);});
  s.getRange('B6:D13').format.font.color='#195ba0';val(s,'A15','Gesamt netto');formula(s,'E15','=SUM(E6:E13)');band(s,15);
  val(s,'A16','Umsatzsteuer');input(s,'B16',.19);s.getRange('B16').setNumberFormat('0%');formula(s,'E16','=ROUND(E15*B16,2)');
  val(s,'A17','Gesamt brutto');formula(s,'E17','=E15+E16');band(s,17);
  val(s,'A19','Untersuchungsrahmen brutto');input(s,'E19',12000);val(s,'F19','Beschluss 02.02.2026');
  val(s,'A20','Rechnerisch nicht belegt');formula(s,'E20','=E19-E17');
  note(s,22,'Enthalten: Angebote und interne Ansätze. Keine Bestellung, keine Statik und keine Baukostenschätzung.');
  note(s,23,'Dachboden nicht enthalten. Zugang, Öffnungen und Probenahme bedürfen gesonderter Abstimmung.');
  note(s,25,'gez. Hanna Wendt · an Marlene Voss · Quellen: Angebote 16.02.2026 und Vorstandsbeschluss.');
  s.getRange('D6:E20').setNumberFormat(MONEY);s.getRange('C6:C13').format.horizontalAlignment='center';s.getRange('B6:B13').setNumberFormat('0"  "');s.getRange('A6:G13').format.rowHeight=20;
  await finish(wb,1,'12_2026-02-17_Untersuchungsbudget.xlsx',[['Budget','A1:G25']],{sheet:'Budget',input:'B9',output:'E17',baseline:8068.2,changedInput:7,expected:8240.75});
}

if(!requested||requested===2){
  const wb=Workbook.create();const s=setup(wb,'Kosten','Kita Wiesenbogen Kostenschätzung','Büro Sander · an Wiesenbogen Bildung · 19.03.2026 · KP-26-02',
    ['Projektbestandteil','Menge','Einheit','V1 Ansatz EUR','V1 netto EUR','V2 Ansatz EUR','V2 netto EUR'],[34,10,10,18,20,18,20]);
  const rows=[['Baukonstruktion',864,'m² BGF',1650,1580],['Technik ohne Küche',864,'m² BGF',480,520],['Aufzug',1,'psch',0,45000],['Ausgabeküche',1,'psch',48000,0],['Außenanlagen',1500,'m²',95,95],['Lose Ausstattung',1,'psch',78000,78000],['Planung und Nebenkosten',1,'psch',320000,320000],['Herrichten und Anschlüsse',1,'psch',65000,65000]];
  rows.forEach((r,i)=>{const k=i+6;s.getRange(`A${k}:D${k}`).values=[r.slice(0,4)];input(s,`F${k}`,r[4]);formula(s,`E${k}`,`=IF(OR(B${k}="",D${k}=""),NA(),ROUND(B${k}*D${k},2))`);formula(s,`G${k}`,`=IF(OR(B${k}="",F${k}=""),NA(),ROUND(B${k}*F${k},2))`);});
  val(s,'A15','Summe netto');formula(s,'E15','=SUM(E6:E13)');formula(s,'G15','=SUM(G6:G13)');band(s,15);
  val(s,'A16','Umsatzsteuer');input(s,'B16',.19);s.getRange('B16').setNumberFormat('0%');formula(s,'E16','=ROUND(E15*$B$16,2)');formula(s,'G16','=ROUND(G15*$B$16,2)');
  val(s,'A17','Kosten brutto');formula(s,'E17','=E15+E16');formula(s,'G17','=G15+G16');
  val(s,'A18','Reserve brutto');input(s,'E18',200000);input(s,'G18',200000);
  val(s,'A19','Mit Reserve brutto');formula(s,'E19','=E17+E18');formula(s,'G19','=G17+G18');band(s,19);
  val(s,'A21','Finanzrahmen brutto');input(s,'E21',3200000);formula(s,'G21','=E21');
  val(s,'A22','Abstand zum Rahmen');formula(s,'E22','=E21-E19');formula(s,'G22','=G21-G19');
  note(s,24,'V1 eingeschossig, V2 zweigeschossig. Je 864 m² BGF, 75 Plätze. Grundstück vorhanden, nicht enthalten.');
  note(s,25,'Preisstand März 2026. Bau- und Technikansätze: Sander / Oertel 16.03.; keine Unternehmerpreise.');
  note(s,26,'V2 Küche: Ansatz 0 nach Telefonnotiz 18.03., Betreiberbestand angenommen. Schriftliche Antwort fehlt.');
  note(s,27,'Nebenkosten sind ein Planungsansatz einschließlich Honoraren und steuerpflichtiger Untersuchungen.');
  note(s,28,'Gebühren: außerhalb dieser Summe noch ohne Ansatz. Reserve nicht als erteilter Auftrag zu verstehen.');
  note(s,30,'gez. Levin Sander · Planbezug V1-01 / V2-01 vom 12.03.2026 · interne Kostengliederung.');
  for(const row of [14,20,23,29])s.getRange(`A${row}:G${row}`).format.rowHeight=7;
  s.getRange('D6:G22').setNumberFormat(MONEY);s.getRange('C6:C13').format.horizontalAlignment='center';s.getRange('B6:B13').setNumberFormat('0"  "');s.getRange('A6:G13').format.rowHeight=20;
  await finish(wb,2,'10_2026-03-19_Kostenschaetzung.xlsx',[['Kosten','A1:G30']],{sheet:'Kosten',input:'F9',output:'G19',baseline:3133231,changedInput:48000,expected:3190351});
}

if(!requested||requested===3){
  const wb=Workbook.create();const s=setup(wb,'Berechnung','Ärztehaus Kostenberechnung','Heller und Seifert · an Mühlenanger Immobilien · 08.06.2026 · AS-26-03',
    ['Projektbestandteil','Menge','Einheit','Ansatz netto EUR','Netto EUR','Quelle','Stand'],[34,11,11,18,20,22,29]);
  const rows=[['Erdarbeiten',540,'m²',95,'E-03 / Grundfläche','Ansatz Juni'],['Gründung und Bodenplatte',540,'m²',260,'E-03 / T-02','Ohne Bodenverbesserung'],['Tragwerk und Decken',1080,'m² BGF',290,'T-02 / 03.06.','Schachtänderung offen'],['Fassade geschlossen',720,'m²',310,'E-03 / Ansicht','Fenster separat'],['Dachaufbau',540,'m²',210,'E-03 / Schnitt','Flachdach'],['Fenster und Außentüren',180,'m²',590,'E-03 / Ansicht','Planeransatz'],['Innenausbau',1080,'m² BGF',420,'E-03 / Raumstand','Allgemeine Praxisnutzung'],['Technische Anlagen',1,'psch',690000,'TGA 04.06.','Ohne Aufzug'],['Aufzug',1,'St',48000,'TGA 04.06.','Zwei Haltestellen'],['Außenanlagen',1250,'m²',110,'Vorplanung 01.04.','Unverändert'],['Lose Ausstattung',1,'psch',150000,'Betreiber 10.04.','Keine OP-Ausstattung'],['Planung und Nebenkosten',1,'psch',380000,'Abruf / Ansatz','Steuerpflichtige Ansätze']];
  rows.forEach((r,i)=>{const k=i+6;s.getRange(`A${k}:D${k}`).values=[r.slice(0,4)];formula(s,`E${k}`,`=IF(OR(B${k}="",D${k}=""),NA(),ROUND(B${k}*D${k},2))`);val(s,`F${k}`,r[4]);val(s,`G${k}`,r[5]);});
  val(s,'A19','Gesamt netto');formula(s,'E19','=SUM(E6:E17)');band(s,19);
  val(s,'A20','Umsatzsteuer');input(s,'B20',.19);s.getRange('B20').setNumberFormat('0%');formula(s,'E20','=ROUND(E19*B20,2)');
  val(s,'A21','Kosten brutto');formula(s,'E21','=E19+E20');
  val(s,'A22','Reserve brutto');input(s,'E22',200000);val(s,'A23','Mit Reserve brutto');formula(s,'E23','=E21+E22');band(s,23);
  val(s,'A25','Kostenschätzung netto');input(s,'E25',2780000);val(s,'F25','01.04.2026');
  val(s,'A26','Veränderung netto');formula(s,'E26','=E19-E25');
  val(s,'A27','Finanzrahmen brutto');input(s,'E27',3800000);val(s,'A28','Abstand mit Reserve');formula(s,'E28','=E27-E23');
  note(s,30,'Planbezug E-03. Schachtgeometrie K-07 ungeklärt; TGA-Ansatz ohne Änderung am Tragwerk.');
  note(s,31,'Grundstück und öffentlich-rechtliche Gebühren außerhalb dieser Berechnung; Gebühren noch offen.');
  note(s,32,'Interne Projektkostengliederung. Keine Kostenerfassung für später vorgeschlagene OP-Nutzung.');
  note(s,34,'gez. Janne Heller · Mengen aus Zeichnungen 03 bis 05 und Raumliste 10; Fachansätze 08 und 09.');
  s.getRange('D6:E28').setNumberFormat(MONEY);s.getRange('C6:C17').format.horizontalAlignment='center';s.getRange('B6:B17').setNumberFormat('0"  "');s.getRange('A6:G17').format.rowHeight=20;
  for(const row of [18,24,29,33])s.getRange(`A${row}:G${row}`).format.rowHeight=7;
  await finish(wb,3,'11_2026-06-08_Kostenberechnung.xlsx',[['Berechnung','A1:G34']],{sheet:'Berechnung',input:'D13',output:'E19',baseline:2806800,changedInput:710000,expected:2826800});
  const wt=Workbook.create();const t=setup(wt,'Termine','Ärztehaus Terminfortschreibung','Heller und Seifert · 10.06.2026 · Kalenderdauer, Ende exklusiv · AS-26-03',
    ['Vorgang','Beginn','Kalendertage','Ende','Vorgänger','Verantwortung','Grundlage'],[33,16,15,16,17,24,30]);
  const serial=(date)=>Math.round((Date.parse(date)-Date.UTC(1899,11,30))/86400000);
  const steps=[['Fachkoordination K-07',7,'Start','Planung / Fachbüros','Antworten ab 15.06. erwartet'],['Bauherrenentscheidung',3,'Fachkoordination','Mühlenanger KG','Sitzungsfenster vorbehaltlich'],['Genehmigungsunterlagen',28,'Entwurfsentscheidung','Objekt- und Fachplanung','Folgeabruf erforderlich'],['Behördenverfahren',70,'Einreichung','Annahme Büro','Keine zugesicherte Dauer'],['Weitere Planung',42,'Behördenstand','Objekt- und Fachplanung','Vereinfachte Abfolge'],['Vergabe',35,'Weitere Planung','Bauherr / Planung','Kein Vergabetermin zugesagt'],['Bauausführung',280,'Vergabe','Noch nicht beauftragt','Rahmenannahme'],['Inbetriebnahme',14,'Bauausführung','Bauherr / Betreiber','Mit Nachweisen und Übergabe']];
  steps.forEach((r,i)=>{const k=i+6;val(t,`A${k}`,r[0]);if(i===0)input(t,`B${k}`,serial('2026-06-15'));else formula(t,`B${k}`,`=D${k-1}`);input(t,`C${k}`,r[1]);formula(t,`D${k}`,`=IF(C${k}="",NA(),B${k}+C${k})`);val(t,`E${k}`,r[2]);val(t,`F${k}`,r[3]);val(t,`G${k}`,r[4]);});
  val(t,'A16','Ziel Betriebsbeginn');input(t,'D16',serial('2027-10-01'));
  val(t,'A17','Tage nach Zieltermin');formula(t,'D17','=D13-D16');
  note(t,19,'Stand 01.04.: Entscheidung 12.06. vorgesehen. Neuer Beginn der offenen Fachkoordination 15.06.');
  note(t,20,'Keine Fristzusage der Behörde; kein Abruf späterer Phasen und keine Beauftragung der Ausführung.');
  note(t,22,'gez. Janne Heller · an Theda Mertin · Grundlage: Koordinationsprotokoll 09.06.2026.');
  t.getRange('B6:B13').setNumberFormat('dd.mm.yyyy"  "');t.getRange('D6:D16').setNumberFormat('dd.mm.yyyy"  "');t.getRange('D17').setNumberFormat('0"  "');t.getRange('A6:G13').format.rowHeight=32;
  val(t,'E8','Entscheidung');
  await finish(wt,3,'14_2026-06-10_Terminfortschreibung.xlsx',[['Termine','A1:G22']],{sheet:'Termine',input:'C6',output:'D17',baseline:6,changedInput:14,expected:13});
}

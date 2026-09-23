#!/usr/bin/env node
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const qa = await fs.mkdtemp(path.join(os.tmpdir(), 'dortmund-sensorik-xlsx-'));
const dependencies = path.resolve(path.dirname(process.execPath), '../..');
await fs.symlink(path.join(dependencies, 'node/node_modules'), path.join(qa, 'node_modules'), 'dir');
const runtime = createRequire(path.join(qa, 'runtime.cjs'));
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(runtime.resolve('@oai/artifact-tool')).href);
const JSZip = runtime('jszip');
const xml = runtime('xml-js');
const money = '#,##0.00"  "';
const put = (s, a, v) => { s.getRange(a).values = [[v]]; };
const formula = (s, a, v) => { s.getRange(a).formulas = [[v]]; };
const val = (s, a) => s.getRange(a).values[0][0];
const near = (actual, expected) => assert(Math.abs(actual - expected) < 0.000001, `${actual} != ${expected}`);

function sheet(wb, name, widths, rows = 26) {
  const s = wb.worksheets.add(name);
  s.showGridLines = false;
  const end = String.fromCharCode(64 + widths.length);
  s.getRange(`A1:${end}${rows}`).format = {
    font: { name: 'Arial', size: 11, color: '#202c32' },
    rowHeight: 26, verticalAlignment: 'center',
  };
  widths.forEach((width, i) => {
    s.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}${rows}`).format.columnWidthPx = width;
  });
  s.getRange('A2').format.font = { name: 'Arial', size: 15, bold: true, color: '#263e46' };
  return s;
}

function header(s, range, values) {
  s.getRange(range).values = [values];
  s.getRange(range).format = {
    fill: '#354e58', font: { name: 'Arial', size: 11, bold: true, color: '#ffffff' },
    wrapText: true, rowHeight: 43, horizontalAlignment: 'center',
  };
}

function total(s, range) {
  s.getRange(range).format.fill = '#e9eff0';
  s.getRange(range).format.font.bold = true;
  s.getRange(range).format.borders = { top: { style: 'thin', color: '#9aabaf' } };
}

// Druckbereiche und Papierformat werden nach dem Tabellenexport ergänzt.
async function printSettings(file, ranges) {
  const zip = await JSZip.loadAsync(await fs.readFile(file));
  const el = (name, attributes = {}, elements = []) => ({type:'element',name,attributes,elements});
  const child = (node,name) => (node.elements || []).find(x=>x.name===name);
  async function read(name) {
    const doc=xml.xml2js(await zip.file(name).async('string'));
    const root=doc.elements.find(x=>x.type==='element');
    const prefix=root.name.includes(':') ? root.name.split(':')[0] : null;
    if(prefix) {
      const strip=n=>{if(n.name?.startsWith(prefix+':'))n.name=n.name.slice(prefix.length+1);for(const c of n.elements || [])strip(c);};
      strip(root);root.attributes.xmlns=root.attributes['xmlns:'+prefix];delete root.attributes['xmlns:'+prefix];
    }
    return [doc,root];
  }
  function replace(root,name,node,order) {
    root.elements=(root.elements || []).filter(x=>x.name!==name);
    const i=root.elements.findIndex(x=>order.indexOf(x.name)>order.indexOf(name));
    root.elements.splice(i<0?root.elements.length:i,0,node);
  }
  const [doc,root]=await read('xl/workbook.xml');
  const defs=child(root,'definedNames') || el('definedNames');
  defs.elements=(defs.elements || []).filter(x=>x.attributes?.name!=='_xlnm.Print_Area');
  ranges.forEach(([name,range],i)=>defs.elements.push(el('definedName',{name:'_xlnm.Print_Area',localSheetId:String(i)},[{type:'text',text:`'${name}'!${range.replace(/([A-Z]+)(\d+)/g,'$$$1$$$2')}`}])));
  replace(root,'definedNames',defs,['fileVersion','fileSharing','workbookPr','workbookProtection','bookViews','sheets','functionGroups','externalReferences','definedNames','calcPr','extLst']);
  zip.file('xl/workbook.xml',xml.js2xml(doc));
  const order=['sheetPr','dimension','sheetViews','sheetFormatPr','cols','sheetData','sheetCalcPr','sheetProtection','protectedRanges','scenarios','autoFilter','sortState','dataConsolidate','customSheetViews','mergeCells','phoneticPr','conditionalFormatting','dataValidations','hyperlinks','printOptions','pageMargins','pageSetup','headerFooter','rowBreaks','colBreaks','customProperties','cellWatches','ignoredErrors','smartTags','drawing','legacyDrawing','legacyDrawingHF','picture','oleObjects','controls','webPublishItems','tableParts','extLst'];
  for(let i=0;i<ranges.length;i++) {
    const name=`xl/worksheets/sheet${i+1}.xml`;
    const [doc,root]=await read(name);
    const pr=child(root,'sheetPr') || el('sheetPr');
    replace(pr,'pageSetUpPr',el('pageSetUpPr',{fitToPage:'1'}),['tabColor','outlinePr','pageSetUpPr']);
    replace(root,'sheetPr',pr,order);
    replace(root,'printOptions',el('printOptions',{gridLines:'0',headings:'0'}),order);
    replace(root,'pageMargins',el('pageMargins',{left:'0.3',right:'0.3',top:'0.35',bottom:'0.35',header:'0.15',footer:'0.15'}),order);
    replace(root,'pageSetup',el('pageSetup',{paperSize:'9',orientation:'landscape',fitToWidth:'1',fitToHeight:'1'}),order);
    zip.file(name,xml.js2xml(doc));
  }
  await fs.writeFile(file,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
}

async function finish(wb, filename, ranges) {
  wb.recalculate();
  const errors = await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!', options: { useRegex: true, maxResults: 30 }, maxChars: 2000 });
  assert(!/"value"\s*:\s*"#/.test(errors.ndjson), errors.ndjson);
  console.log(errors.ndjson);
  for (const [name, range] of ranges) {
    const preview = await wb.render({ sheetName: name, range, scale: 1.5, format: 'png' });
    const target = path.join(qa, `${path.basename(filename, '.xlsx')}-${name}.png`);
    await fs.writeFile(target, new Uint8Array(await preview.arrayBuffer()));
    console.log(`Vorschau: ${target}`);
  }
  const file = await SpreadsheetFile.exportXlsx(wb);
  const staging = path.join(qa, path.basename(filename));
  await file.save(staging);
  await printSettings(staging, ranges);
  await fs.copyFile(staging, filename);
  try { await fs.rename(filename + '.inspect.ndjson', path.join(qa, path.basename(filename) + '.inspect.previous.ndjson')); }
  catch (error) { if (error.code !== 'ENOENT') throw error; }
  console.log(`Arbeitsmappe: ${filename}`);
}

async function dortmund() {
  const wb = Workbook.create();
  const s = sheet(wb, 'Rechnungsabgleich', [350,90,125,125,115,125,125,125], 27);
  const h = sheet(wb, 'Stunden', [140,135,115,110,130,115,280], 22);
  s.freezePanes.freezeRows(6);
  h.freezePanes.freezeRows(6);
  put(s,'A2','Kettenlicht / Rechnungs- und Leistungsabgleich');
  put(s,'A3','Maren Fink, 23.09.2026 · EUR · Erfasste Rechnungen und gebuchte Zahlungen');
  put(s,'A5','Offen laut erfassten Rechnungen, brutto');
  formula(s,'H5','=H13');
  s.getRange('H5').setNumberFormat(money);
  header(s,'A6:H6',['Rechnung und Leistung','Menge','Satz netto EUR','Netto EUR','USt EUR','Brutto EUR','Bezahlt EUR','Rest EUR']);
  s.getRange('A7:C11').values = [
    ['ND-2024-021 / Einrichtung Rate 1',1,4500],
    ['ND-2024-119 / Einrichtung Rate 2',1,4500],
    ['ND-2026-388 / Betrieb September',1,450],
    ['ND-2026-388 / Zweiter Testmandant',1,800],
    ['ND-2026-388 / Importbereinigung',null,125],
  ];
  formula(s,'B11',"='Stunden'!D10");
  put(s,'A16','Umsatzsteuersatz'); put(s,'B16',0.19); s.getRange('B16').setNumberFormat('0%');
  s.getRange('G7:G11').values = [[5355],[5355],[0],[0],[0]];
  for(let r=7;r<=11;r++) {
    s.getRange(`D${r}:F${r}`).formulas = [[`=ROUND(B${r}*C${r},2)`,`=ROUND(D${r}*$B$16,2)`,`=SUM(D${r}:E${r})`]];
    formula(s,`H${r}`,`=F${r}-G${r}`);
  }
  put(s,'A13','Gesamt');
  for(const c of ['D','E','F','G','H']) formula(s,`${c}13`,`=SUM(${c}7:${c}11)`);
  s.getRange('C7:H13').setNumberFormat(money);
  s.getRange('B7:C11').format.font.color = '#23557c';
  s.getRange('G7:G11').format.font.color = '#23557c';
  total(s,'A13:H13');
  put(s,'A18','ND-2026-388 netto'); formula(s,'D18','=SUM(D9:D11)'); s.getRange('D18').setNumberFormat(money);
  put(s,'A20','Belege: Rechnungen ND-2024-021, ND-2024-119 und ND-2026-388.');
  put(s,'A21','Zahlungen: Umsatzanzeige vom 21.09.2026, Referenzen RB240125-1862 und RB240410-0941.');
  put(s,'A22','Septemberrechnung: Bis 23.09.2026 keine Zahlung in der Buchhaltung erfasst.');
  put(s,'A23','Die laufenden Monatsrechnungen bis August sind in dieser Auswahl nicht enthalten.');
  put(s,'A24','Zum Betrieb am 09. bis 12.09.2026: Ticket ND-6721. Keine Gutschrift eingegangen.');
  put(s,'A25','Zur Importarbeit: zunächst vier Stunden per E-Mail vom 25.08. freigegeben; zwölf Stunden berechnet.');
  put(h,'A2','Importbereinigung / Zeitbuchungen Netzraum');
  put(h,'A3','Abschrift der Zeitangaben aus ND-2026-388 durch Maren Fink, 23.09.2026');
  put(h,'A4','Angebot vom 24.08.2026: zwölf Stunden geschätzt, 125 EUR netto je Stunde.');
  header(h,'A6:G6',['Datum','Von','Bis','Stunden','Satz netto EUR','Betrag EUR','Bearbeitung']);
  const dates = ['2026-09-02','2026-09-03','2026-09-04'];
  const starts = [9,10,9], ends = [13,15,12];
  for(let i=0;i<3;i++) {
    const r=i+7;
    h.getRange(`A${r}:G${r}`).values = [[new Date(`${dates[i]}T00:00:00Z`),starts[i]/24,ends[i]/24,null,125,null,'Nils Böttcher']];
    formula(h,`D${r}`,`=ROUND((C${r}-B${r})*24,2)`);
    formula(h,`F${r}`,`=ROUND(D${r}*E${r},2)`);
  }
  h.getRange('A7:A9').setNumberFormat('dd"."mm"."yyyy');
  h.getRange('B7:C9').setNumberFormat('hh:mm');
  h.getRange('D7:D10').setNumberFormat('0.00'); h.getRange('E7:F10').setNumberFormat(money);
  put(h,'A10','Summe'); formula(h,'D10','=SUM(D7:D9)'); formula(h,'F10','=SUM(F7:F9)'); total(h,'A10:G10');
  put(h,'A13','E-Mail-Freigabe 25.08.'); put(h,'D13',4); put(h,'E13',125); formula(h,'F13','=D13*E13');
  put(h,'A14','Mehrstunden zur E-Mail'); formula(h,'D14','=D10-D13'); formula(h,'F14','=F10-F13');
  h.getRange('E13:F14').setNumberFormat(money);
  put(h,'A17','02.09.: erste Zuordnungsliste erstellt. 03.09.: weitere Zuordnungen telefonisch mit Tom besprochen.');
  put(h,'A18','04.09.: restliche Importzeilen bearbeitet. Quelle für die Stunden: Rechnung vom 07.09.');
  put(h,'A19','Jana Römer bat am 25.08. vor weiteren Stunden um eine Rückmeldung.');
  put(h,'A20','Zum Telefonat am 03.09.: Darstellungen in E-Mail vom 16.09. und Chat vom 22.09.');
  wb.recalculate();
  near(val(s,'D18'),2750); near(val(s,'H13'),3272.5); near(val(s,'G13'),10710); near(val(h,'F14'),1000);
  put(h,'C9',13/24); wb.recalculate(); near(val(s,'D18'),2875);
  put(h,'C9',12/24); wb.recalculate(); near(val(s,'H13'),3272.5);
  console.log((await wb.inspect({kind:'table',range:'Rechnungsabgleich!D7:H13',include:'values,formulas',tableMaxRows:8,tableMaxCols:5,maxChars:2500})).ndjson);
  await finish(wb,path.join(root,'testakten/anwaltschaft-dienstleister-datenzugang-dortmund/23_rechnungs_leistungsabgleich.xlsx'),[['Rechnungsabgleich','A1:H26'],['Stunden','A1:G21']]);
}

async function aachen() {
  const wb=Workbook.create();
  const s=sheet(wb,'Preisstaffeln',[240,160,145,150,170,180,190],28);
  const a=sheet(wb,'Anlauf',[260,125,175,170,180,175,180],28);
  s.freezePanes.freezeRows(8);
  a.freezePanes.freezeRows(8);
  put(s,'A2','Rheinkern / D400 Preisstaffeln');
  put(s,'A3','Eva Schulte, 22.09.2026 · Angebot TS-260902 bei fest zugesagter Jahresmenge');
  put(s,'A4','Ausgangspreis EUR');put(s,'B4',186); put(s,'C4','USt');put(s,'D4',0.19);
  put(s,'A5','Staffel 1 ab Stück');put(s,'B5',1200);put(s,'C5','Nachlass');put(s,'D5',0.03);
  put(s,'A6','Staffel 2 ab Stück');put(s,'B6',1800);put(s,'C6','Nachlass');put(s,'D6',0.05);
  s.getRange('D4:D6').setNumberFormat('0%');s.getRange('B4').setNumberFormat(money);
  s.getRange('B5:B6').setNumberFormat('0"  "');
  header(s,'A8:G8',['Jahresmenge Stück','Basis EUR/Stück','Nachlass','Netto EUR/Stück','Jahr netto EUR','Jahr brutto EUR','Nachlassbetrag EUR']);
  [600,1000,1200,1500,1800,2400].forEach((qty,i)=>{
    const r=i+9;put(s,`A${r}`,qty);
    s.getRange(`B${r}:G${r}`).formulas=[[
      '=$B$4',`=IF(A${r}>=$B$6,$D$6,IF(A${r}>=$B$5,$D$5,0))`,
      `=ROUND(B${r}*(1-C${r}),2)`,`=ROUND(A${r}*D${r},2)`,`=ROUND(E${r}*(1+$D$4),2)`,`=ROUND(A${r}*B${r}-E${r},2)`,
    ]];
  });
  s.getRange('B9:G14').setNumberFormat(money);s.getRange('C9:C14').setNumberFormat('0%');
  s.getRange('A9:A14').format.font.color='#23557c';
  put(s,'A17','Planung Stück/Jahr');put(s,'B17',1200);put(s,'C17','Jahre');put(s,'D17',3);
  put(s,'A18','Planung gesamt Stück');formula(s,'B18','=B17*D17');
  s.getRange('B17:B18').setNumberFormat('0"  "');
  put(s,'A20','Quelle: Angebot TS-260902 vom 02.09.2026, Abschnitt 1.');
  put(s,'A21','Die sechs Zeilen sind Preisvergleiche, keine Bestellungen. Rüstzuschläge sind nicht enthalten.');
  put(s,'A22','Lieferant: Staffel nur bei fester Jahreszusage. Einkauf: Jahresplanung weiterhin unverbindlich.');
  put(s,'A23','Gegenvorschlag 0.8: nachträgliche Gutschrift nach tatsächlicher Jahresabnahme; noch nicht bestätigt.');
  put(s,'A24','Planung über drei Jahre: 01.10.2026 bis 30.09.2029. Keine Zusammenrechnung mit Abrufen 2026.');
  put(a,'A2','D400 / Anlaufmengen und Werkzeug');
  put(a,'A3','Terminabfrage vom 21.09.2026 · Ohne feste Jahreszusage und ohne Staffelabschlag');
  put(a,'A5','Rüstzuschlag EUR/Stück');put(a,'B5',8);put(a,'C5','Losgrenze Stück');put(a,'D5',100);
  a.getRange('B5').setNumberFormat(money);
  header(a,'A8:G8',['Wunschtermin','Stück','Netto EUR/Stück','Zuschlag/Stück EUR','Los netto EUR','USt EUR','Los brutto EUR']);
  ['2026-10-19','2026-11-16','2026-12-14'].forEach((date,i)=>{
    const r=i+9;put(a,`A${r}`,new Date(`${date}T00:00:00Z`));put(a,`B${r}`,[60,80,100][i]);
    a.getRange(`C${r}:G${r}`).formulas=[[
      "='Preisstaffeln'!$B$4",`=IF(B${r}<$D$5,$B$5,0)`,`=ROUND(B${r}*(C${r}+D${r}),2)`,`=ROUND(E${r}*'Preisstaffeln'!$D$4,2)`,`=SUM(E${r}:F${r})`,
    ]];
  });
  a.getRange('A9:A11').setNumberFormat('dd"."mm"."yyyy'); a.getRange('C9:G19').setNumberFormat(money);
  put(a,'A13','Serienanlauf');formula(a,'B13','=SUM(B9:B11)');
  for(const c of ['E','F','G'])formula(a,`${c}13`,`=SUM(${c}9:${c}11)`);
  total(a,'A13:G13');
  put(a,'A15','Werkzeug und 12 Muster');put(a,'E15',12400);formula(a,'F15',"=ROUND(E15*'Preisstaffeln'!$D$4,2)");formula(a,'G15','=SUM(E15:F15)');
  put(a,'A17','Anlauf plus Werkzeug');for(const c of ['E','F','G'])formula(a,`${c}17`,`=${c}13+${c}15`);total(a,'A17:G17');
  put(a,'A18','Werkzeug bezahlt brutto');put(a,'G18',14756);
  put(a,'A19','Rechenrest brutto');formula(a,'G19','=G17-G18');
  put(a,'A21','Mengen und Termine: 11_erp_abrufe_20260921.csv, drei Terminabfragen 2026.');
  put(a,'A22','Stückpreis und Zuschlag: Angebot TS-260902. Kein Preisnachlass für ungebundene Planmengen.');
  put(a,'A23','Werkzeug: TS-2026-491. Zahlung 04.09.2026, Bankbeleg AGB-260904-7319.');
  put(a,'A24','Zwölf Muster sind im Werkzeugpreis enthalten; sie erhöhen die Serienmenge nicht.');
  put(a,'A25','Der Rechenrest ist ein Planbetrag. Serienrechnungen und bestätigte Serientermine liegen nicht vor.');
  wb.recalculate();
  near(val(s,'D11'),180.42);near(val(s,'D13'),176.7);near(val(a,'E13'),45760);near(val(a,'G15'),14756);near(val(a,'G17'),69210.4);
  put(a,'B9',100);wb.recalculate();near(val(a,'D9'),0);near(val(a,'E9'),18600);
  put(a,'B9',99);wb.recalculate();near(val(a,'D9'),8);near(val(a,'E9'),19206);
  put(a,'B9',60);wb.recalculate();near(val(a,'G19'),54454.4);
  console.log((await wb.inspect({kind:'table',range:'Preisstaffeln!A9:G14',include:'values,formulas',tableMaxRows:6,tableMaxCols:7,maxChars:2500})).ndjson);
  await finish(wb,path.join(root,'testakten/corporate-contract-law-rahmenlieferung-sensorik-aachen/12_preisstaffeln_d400.xlsx'),[['Preisstaffeln','A1:G25'],['Anlauf','A1:G26']]);
}

await dortmund();
await aachen();
console.log(`Prüfverzeichnis: ${qa}`);

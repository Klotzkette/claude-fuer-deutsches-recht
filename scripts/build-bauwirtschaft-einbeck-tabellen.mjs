// Native Tabellenautorenschaft mit Artifact Tool. Autor: Klotzkette.
import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const modules = process.env.AKTEN_NODE_MODULES;
const require = modules ? createRequire(path.join(modules, '.einbeck-loader.cjs')) : createRequire(import.meta.url);
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(require.resolve('@oai/artifact-tool')).href);
const assets=process.env.EINBECK_ASSETS || '/tmp/bauwirtschaft-assets';
const model=JSON.parse(await fs.readFile(path.join(assets,'einbeck-model.json'),'utf8'));
const output=model.case;
const results=[];

function setup(wb,name,title,sub,headers,widths){
  const s=wb.worksheets.add(name);
  const end=String.fromCharCode(64+headers.length);
  s.showGridLines=false;
  s.getRange(`A1:${end}45`).format.font={name:'Arial',size:11,color:'#111111'};
  s.getRange('A2').values=[[title]];s.getRange('A2').format.font={name:'Arial',size:15,bold:true};
  s.getRange('A3').values=[[sub]];
  s.getRange(`A5:${end}5`).values=[headers];
  s.getRange(`A5:${end}5`).format={fill:'#354a55',font:{name:'Arial',size:11,bold:true,color:'#ffffff'},wrapText:true,rowHeight:36};
  s.getRange(`A6:${end}40`).format.rowHeight=34;
  s.getRange(`A6:${end}40`).format.verticalAlignment='center';
  widths.forEach((w,i)=>s.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}45`).format.columnWidth=w);
  s.freezePanes.freezeRows(5);
  return s;
}
function cell(s,a,v){s.getRange(a).values=[[v]];}
function formula(s,a,v){s.getRange(a).formulas=[[v]];s.getRange(a).format.font.color='#111111';}
function input(s,a,v){cell(s,a,v);s.getRange(a).format.font.color='#174b99';}
function total(s,row,label,expr,col='E',end='G'){
  cell(s,`A${row}`,label);formula(s,`${col}${row}`,expr);
  s.getRange(`A${row}:${end}${row}`).format.fill='#e5ebee';
  s.getRange(`A${row}:${end}${row}`).format.font.bold=true;
}
async function finish(wb,n,ranges,probe){
  wb.recalculate();
  const inspection=[];
  for (const [name,range] of ranges){
    const r=await wb.inspect({kind:'table',range:`'${name}'!${range}`,include:'values,formulas',tableMaxRows:35,tableMaxCols:8,maxChars:18000});
    inspection.push(r.ndjson);
    const blob=await wb.render({sheetName:name,range,scale:1.5,format:'png'});
    await fs.writeFile(path.join(assets,`xlsx-einbeck-${n}-${name}.png`),new Uint8Array(await blob.arrayBuffer()));
  }
  const errs=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},maxChars:5000});
  const exported=await SpreadsheetFile.exportXlsx(wb);await exported.save(path.join(output,model.files[n]));
  const sidecar=path.join(output,model.files[n]+'.inspect.ndjson');
  try { await fs.rename(sidecar,path.join(assets,'einbeck-'+model.files[n]+'.inspect.ndjson')); } catch(e) { if(e.code!=='ENOENT')throw e; }
  results.push({number:n,inspection,errors:errs.ndjson,probe});
}

{
  const wb=Workbook.create();const s=setup(wb,'Kosten','Kostenberechnung Gebäude und Projekt','Hartwig Architektur · an den Vorstand · 14.06.2021 · BH-21-04',
    ['Leistungsbereich','Menge','Einheit','Ansatz netto EUR','Netto EUR','Brutto EUR','Beleg / Herleitung'],[34,11,10,18,19,19,42]);
  const rows=[['Bestandumbau',216,'m²',340,'04 / Bestandsfläche × Ansatz Juni 2021'],['Anbau',80,'m²',1150,'07 / Anbaugrundfläche × Ansatz Juni 2021'],
    ['Rampe mit Podest',1,'psch',4500,'07 / örtlicher Ansatz für Gesamtanlage'],['Technische Anlagen',296,'m²',250,'10 / Abstimmung Mertens'],
    ['Außenanlagen',300,'m²',70,'01 / Bedarf und 10 / Abstimmung'],['Bewegliche Ausstattung',1,'psch',12000,'01 / Raumprogramm'],
    ['Architektur und Nebenkosten',1,'psch',54000,'02 / individuell vereinbartes Honorar'],['Untersuchung und Vermessung',1,'psch',4500,'03 / Untersuchungsbedarf'],
    ['Gebührenansatz',1,'psch',1800,'10 / Planungsansatz, ohne Umsatzsteuer']];
  // Der historische Kostenstand enthält auch auf Gebühren einen pauschalen Steueransatz.
  // Dies wird sichtbar abgegrenzt, nicht nachträglich als reale Steuer ausgegeben.
  rows.forEach((r,i)=>{const k=i+6;s.getRange(`A${k}:D${k}`).values=[r.slice(0,4)];cell(s,`G${k}`,r[4]);formula(s,`E${k}`,`=IF(OR(B${k}="",D${k}=""),NA(),ROUND(B${k}*D${k},2))`);formula(s,`F${k}`,`=ROUND(E${k}*(1+$B$18),2)`);});
  s.getRange('B6:D14').format.font.color='#174b99';
  total(s,16,'Kostenstand netto','=SUM(E6:E14)');formula(s,'F16','=SUM(F6:F14)');
  cell(s,'A18','Steuerpauschale Kostenplanung');input(s,'B18',.19);s.getRange('B18').setNumberFormat('0.0%');
  cell(s,'A19','Finanzrahmen brutto');input(s,'F19',430000);
  cell(s,'A20','Abstand zum Finanzrahmen');formula(s,'F20','=F19-F16');
  cell(s,'A22','Vergleich Schätzung 18.03.2021');input(s,'E22',322000);formula(s,'F22','=ROUND(E22*(1+$B$18),2)');cell(s,'G22','05 / Variante 1');
  cell(s,'A23','Mehrkosten seit Vorplanung');formula(s,'E23','=E16-E22');formula(s,'F23','=F16-F22');
  cell(s,'A25','Stand: frühe Kostenplanung, keine Rechnungssteuer.');
  cell(s,'A26','Auf Gebühren ist hier vorsorglich die Steuerpauschale enthalten.');
  cell(s,'A27','Die spätere Kostenfeststellung behandelt Gebühren ohne Umsatzsteuer.');
  cell(s,'A29','gez. Lena Hartwig · Bezug: Entwurf E-01 · Anlagen: keine');
  s.getRange('D6:F23').setNumberFormat('#,##0.00');s.getRange('G6:G22').format.wrapText=true;
  s.getRange('D6:F23').format.horizontalAlignment='right';
  s.getRange('C6:C14').format.horizontalAlignment='center';
  await finish(wb,9,[['Kosten','A1:G29']],{input:'Kosten!B6',output:'Kosten!E16',baseline:337240,changedInput:217,expected:337580});
}
{
  const wb=Workbook.create();const s=setup(wb,'Termine','Rahmenterminplan Bürgerhaus','Hartwig Architektur · an Vorstand und Fachplaner · 25.04.2022 · BH-21-04',
    ['Vorgang','Start','Dauer Tage','Ende','Abstand Tage','Zuständig','Grundlage'],[37,16,12,16,14,25,35]);
  const serial=(date)=>Math.round((new Date(date+'T00:00:00Z')-new Date('1899-12-30T00:00:00Z'))/86400000);
  const rows=[['Ausführungsplanung','2022-05-02',36,0,'Hartwig','18 / Abruf, Ziel 06.06.2022'],['Vereinsveranstaltungen','2022-06-07',242,0,'Vorstand','01 / Nutzung bis Winter 2022'],
    ['Vergabeunterlagen','2023-02-06',31,0,'Hartwig','18 / Abruf'],['Angebotsfrist','2023-03-09',27,0,'Vorstand','Vergabeplanung, 04.04.2023'],
    ['Prüfung und Zuschlag','2023-04-05',14,0,'Hartwig / Vorstand','Vorgesehener Zuschlag 18.04.2023'],['Bauvorbereitung','2023-04-19',124,0,'Vorstand / Firmen','Räumung bis 20.08.2023'],
    ['Rückbau und Gründung','2023-08-21',40,0,'Los 1','Vertragstermin noch anzubieten'],['Hülle und Dach','2023-09-30',61,0,'Los 1','Anschluss nach Gründung'],
    ['Technik und Innenausbau','2023-11-30',91,0,'Fachfirmen','Abstimmung mit Gebäudeplanung'],['Restarbeiten Los 1','2024-02-29',16,0,'Los 1','Ziel Fertigstellung 15.03.2024'],
    ['Abnahmen und Einweisung','2024-03-16',20,0,'Vorstand / Firmen','Gewerke einzeln abnehmen'],['Übergabe','2024-04-05',1,0,'Vorstand / Hauswart','Nutzungsbeginn nach Freigaben'],
    ['Objektbetreuung Begehung','2026-09-01',30,0,'Hartwig','02 / Vertrag; Termin noch abzustimmen']];
  rows.forEach((r,i)=>{const k=i+6;cell(s,`A${k}`,r[0]);input(s,`B${k}`,serial(r[1]));input(s,`C${k}`,r[2]);formula(s,`D${k}`,`=IF(OR(B${k}="",C${k}="",C${k}<1),NA(),B${k}+C${k}-1)`);if(i)formula(s,`E${k}`,`=B${k}-D${k-1}-1`);cell(s,`F${k}`,r[4]);cell(s,`G${k}`,r[5]);});
  s.getRange('B6:B18').setNumberFormat('yyyy-mm-dd');s.getRange('D6:D18').setNumberFormat('yyyy-mm-dd');
  s.getRange('B5:E18').format.horizontalAlignment='center';
  s.getRange('A6:A18').format.wrapText=true;s.getRange('F6:G18').format.wrapText=true;s.getRange('A6:G18').format.rowHeight=43;
  cell(s,'A20','Kalendertage einschließlich Beginn und Ende; keine Werktagsannahme.');
  cell(s,'A21','Starts sind abgestimmte Meilensteine; Verschiebungen nicht automatisch freigegeben.');
  cell(s,'A22','Abstand negativ: Überschneidung. Abstand positiv: geplanter Zwischenraum.');
  cell(s,'A24','gez. Lena Hartwig · Anlagen: keine · Stand ohne spätere Ist-Daten');
  await finish(wb,19,[['Termine','A1:G24']],{input:'Termine!C6',output:'Termine!D6',baseline:serial('2022-06-06'),changedInput:37,expected:serial('2022-06-07')});
}
{
  const wb=Workbook.create();const s=setup(wb,'LV','Bepreistes Leistungsverzeichnis Los 1','Hartwig Architektur · interne Kostenkontrolle an den Vorstand · 08.03.2023',
    ['Position und Leistung','Menge','Einheit','EP netto EUR','Gesamt netto EUR','Quelle','Mengenbasis'],[36,12,11,19,21,18,32]);
  model.items.forEach((it,i)=>{const r=i+6;cell(s,`A${r}`,`2.${i+1} ${it[0]}`);input(s,`B${r}`,model.qty[i]);cell(s,`C${r}`,model.units[i]);input(s,`D${r}`,model.plan_ep[i]);formula(s,`E${r}`,`=ROUND(B${r}*D${r},2)`);cell(s,`F${r}`,'23 / Position '+(i+1));cell(s,`G${r}`,i===10?'12 × 1,5 + 1,5 × 1,5':'AP-01 / örtlicher Ansatz');});
  total(s,19,'Los 1 netto','=SUM(E6:E17)');cell(s,'A20','Umsatzsteuer');input(s,'B20',.19);s.getRange('B20').setNumberFormat('0.0%');formula(s,'E20','=ROUND(E19*B20,2)');total(s,21,'Los 1 brutto','=E19+E20');
  cell(s,'A23','Baukonstruktion Kostenberechnung');input(s,'E23',169940);cell(s,'G23','09 / Bestand, Anbau und Rampe');
  cell(s,'A24','Für übrige Baukonstruktion verfügbar');formula(s,'E24','=E23-E19');
  cell(s,'A26','Rest betrifft Fenster und weitere Ausbauleistungen, nicht eine Baureserve.');
  cell(s,'A27','Einheitspreise sind Planeransätze März 2023, keine Unternehmerangebote.');
  cell(s,'A29','gez. Lena Hartwig · Bezug BH-21-04 · Anlagen: LV 08.03.2023');
  s.getRange('A6:A17').format.wrapText=true;s.getRange('G6:G24').format.wrapText=true;s.getRange('D6:E24').setNumberFormat('#,##0.00');s.getRange('B6:B17').setNumberFormat('0.00');
  await finish(wb,24,[['LV','A1:G29']],{input:'LV!B6',output:'LV!E19',baseline:99785,changedInput:2,expected:108285});
}
{
  const wb=Workbook.create();const s=setup(wb,'Rechnung','Prüfung Schlussrechnung Los 1','Kostenabschluss 08.04.2024 · Prüfung 11.03.2024 · LB-240301, Zugang 04.03.2024',
    ['Position','Menge','EP netto EUR','Verlangt EUR','Geprüft EUR','Differenz EUR','Beleg / Befund'],[36,12,18,20,20,18,36]);
  model.items.forEach((it,i)=>{const r=i+6;cell(s,`A${r}`,`2.${i+1} ${it[0]}`);input(s,`B${r}`,model.final_qty[i]);input(s,`C${r}`,model.leine_ep[i]);formula(s,`D${r}`,`=ROUND(B${r}*C${r},2)`);formula(s,`E${r}`,`=D${r}`);formula(s,`F${r}`,`=D${r}-E${r}`);cell(s,`G${r}`,'35 / AM-07; 25 / Angebot');});
  const nt=[['N01.1 Rohrleitung',14,145],['N01.2 Zusatzgraben',4,92],['N01.3 Abtransport',1,380],['N01.4 Anschlussstunden',16,58],['N01.5 Gerätebereitschaft',2,620]];
  nt.forEach((it,i)=>{const r=i+18;cell(s,`A${r}`,it[0]);input(s,`B${r}`,it[1]);input(s,`C${r}`,it[2]);formula(s,`D${r}`,`=ROUND(B${r}*C${r},2)`);if(i<4)formula(s,`E${r}`,`=D${r}`);else input(s,`E${r}`,0);formula(s,`F${r}`,`=D${r}-E${r}`);cell(s,`G${r}`,i<4?'33 / Angebot; 34 / Auftrag':'34 / nicht bestätigt; Nachweise offen');});
  for(const col of ['D','E','F'])formula(s,`${col}24`,`=SUM(${col}6:${col}22)`);cell(s,'A24','Gesamt netto');
  cell(s,'A25','Umsatzsteuer');input(s,'B25',.19);s.getRange('B25').setNumberFormat('0.0%');
  for(const col of ['D','E','F'])formula(s,`${col}25`,`=ROUND(${col}24*$B$25,2)`);
  cell(s,'A26','Gesamt brutto');for(const col of ['D','E','F'])formula(s,`${col}26`,`=${col}24+${col}25`);
  cell(s,'A28','Gezahlt 12.10.2023 brutto');input(s,'D28',35700);cell(s,'G28','36 / vereinnahmter Abschlag');
  cell(s,'A29','Gezahlt 18.12.2023 brutto');input(s,'D29',47600);cell(s,'G29','36 / vereinnahmter Abschlag');
  cell(s,'A30','Offener Rechnungsbetrag');formula(s,'D30','=D26-SUM(D28:D29)');formula(s,'E30','=E26-SUM(D28:D29)');formula(s,'F30','=D30-E30');
  cell(s,'A32','N01.5 nicht freigegeben. Kein abschließender Anspruchsausschluss.');
  cell(s,'A33','Zahlungsvorschlag ohne Mängelrechte oder Abnahme vorwegzunehmen.');
  cell(s,'A34','gez. Lena Hartwig · Anlagen: Schlussrechnung und Aufmaß');
  s.getRange('A6:A22').format.wrapText=true;s.getRange('G6:G29').format.wrapText=true;s.getRange('C6:F30').setNumberFormat('#,##0.00');
  s.getRange('A24:G26').format.fill='#e5ebee';s.getRange('A30:G30').format.fill='#e5ebee';
  const k=setup(wb,'Kostenstand','Kostenfeststellung zum 08.04.2024','Hartwig Architektur · an Vorstand · Objektbetreuung und Streitbetrag getrennt ausgewiesen.',
    ['Leistung','Netto EUR','Steuersatz','Brutto EUR','Status','Quelle'],[38,22,15,23,32,36]);
  const others=[['Los 1 schlussgeprüft',null,.19,'Schlussrechnung geprüft','Rechnung!E24'],['Heizung und Sanitär',54200,.19,'Schlussrechnung MI-240322','40 / Abrechnungsregister'],
    ['Elektro',27400,.19,'Schlussrechnung LP-240325','40 / Abrechnungsregister'],['Fenster und Ausbau',61800,.19,'Schlussrechnung WW-240327','40 / Abrechnungsregister'],
    ['Außenanlagen',23600,.19,'Schlussrechnung HR-240402','40 / Abrechnungsregister'],['Bewegliche Ausstattung',12900,.19,'Rechnung RG-240402','40 / Abrechnungsregister'],
    ['Architektur erbrachter Anteil',53040,.19,'Ohne offene Objektbetreuung','02 und 40 / 54.000 abzüglich 960'],['Untersuchung und Vermessung',4650,.19,'Abgerechneter Stand','40 / VM-210210 und VM-230817'],['Gebühren',1780,0,'Ohne Umsatzsteuer','40 / Gebührenregister']];
  others.forEach((r,i)=>{const row=i+6;cell(k,`A${row}`,r[0]);if(i===0)formula(k,`B${row}`,'=Rechnung!E24');else input(k,`B${row}`,r[1]);input(k,`C${row}`,r[2]);formula(k,`D${row}`,`=ROUND(B${row}*(1+C${row}),2)`);cell(k,`E${row}`,r[3]);cell(k,`F${row}`,r[4]);});
  total(k,16,'Festgestellter Kostenstand','=SUM(B6:B14)','B','F');formula(k,'D16','=SUM(D6:D14)');
  cell(k,'A17','Offene Objektbetreuung');input(k,'B17',960);input(k,'C17',.19);formula(k,'D17','=ROUND(B17*(1+C17),2)');
  cell(k,'A18','Finanzrahmen brutto');input(k,'D18',430000);cell(k,'A19','Abstand einschließlich Betreuung');formula(k,'D19','=D18-D16-D17');
  cell(k,'A21','Streitbetrag zusätzlich brutto');formula(k,'D21','=Rechnung!F26');
  cell(k,'A22','Kosten mit Betreuung und Streit');formula(k,'D22','=D16+D17+D21');
  cell(k,'A24','Stand nach Bauausführung; strittige Vergütung nicht als anerkannt behandelt.');
  cell(k,'A25','Andere Gewerke nach Register R-01, Einzelbelege beim Verein.');
  cell(k,'A26','Eine Zahlung oder Abnahme wird durch diesen Stand nicht bestätigt.');
  cell(k,'A28','gez. Lena Hartwig · Bezug BH-21-04 · Anlagen: keine');
  k.getRange('B6:B16').setNumberFormat('#,##0.00');k.getRange('D6:D22').setNumberFormat('#,##0.00');k.getRange('C6:C14').setNumberFormat('0%');k.getRange('E6:F14').format.wrapText=true;
  k.getRange('A6:F14').format.rowHeight=48;
  s.getRange('A6:G34').format.rowHeight=28;
  await finish(wb,37,[['Rechnung','A1:G34'],['Kostenstand','A1:F28']],{input:'Rechnung!B6',output:'Rechnung!E24',baseline:114153.8,changedInput:2,expected:123153.8});
}
await fs.writeFile(path.join(assets,'einbeck-artifact-pruefung.json'),JSON.stringify(results,null,2));
console.log(JSON.stringify({workbooks:results.map(r=>model.files[r.number]),checks:path.join(assets,'einbeck-artifact-pruefung.json')}));

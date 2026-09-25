// Autor: Klotzkette. Arbeitsmappen ausschließlich mit artifact_tool erstellt.
import fs from 'node:fs/promises';
import path from 'node:path';
import { loadWorkbookRuntime } from './akten-workbook-runtime.mjs';
const { Workbook, SpreadsheetFile, requireRuntime } = await loadWorkbookRuntime(['playwright']);
const { chromium } = requireRuntime('playwright');

if(process.argv[2]==='--verify-imports') {
  for(const file of process.argv.slice(3)) {
    const wb=await SpreadsheetFile.importXlsx(await fs.readFile(file));
    const result=await wb.inspect({kind:'sheet',include:'name',maxChars:1200});
    console.log(path.basename(file)+': '+result.ndjson);
  }
  process.exit(0);
}

const m = JSON.parse(await fs.readFile(process.argv[2], 'utf8'));
const qa = m.qa;
const outputs = [];
const date = s => Math.round((Date.parse(s+'T00:00:00Z') - Date.UTC(1899,11,30))/86400000);
const money = '#,##0.00;(#,##0.00);"-"';
const col = i => String.fromCharCode(65+i);

function sheet(wb, name, title, headers, widths) {
  const s = wb.worksheets.add(name);
  s.showGridLines = false;
  s.getRange('A2').values = [[title]];
  s.getRange('A2').format.font = { name:'Arial', size:14, bold:true };
  s.getRange('A3').values = [['Stand 25.09.2026 | EUR netto, soweit nicht anders bezeichnet']];
  s.getRange('A3').format.font = { name:'Arial', size:10, italic:true };
  s.getRange(`A5:${col(headers.length-1)}5`).values = [headers];
  s.getRange(`A5:${col(headers.length-1)}5`).format = {fill:'#344A47',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:34,horizontalAlignment:'center',verticalAlignment:'center'};
  widths.forEach((v,i)=>s.getRange(`${col(i)}1:${col(i)}60`).format.columnWidth=v);
  s.freezePanes.freezeRows(5);
  return s;
}
function rows(s, data) {
  const last = 5+data.length, end=col(data[0].length-1);
  s.getRange(`A6:${end}${last}`).values=data;
  s.getRange(`A6:${end}${last}`).format = {font:{name:'Arial',size:10},rowHeight:29,verticalAlignment:'center',wrapText:true};
  for(let i=0;i<data.length;i++) for(let j=0;j<data[i].length;j++) if(typeof data[i][j]==='number') s.getRange(`${col(j)}${i+6}`).format.font.color='#2457A7';
}
function formula(s, cell, value) {
  s.getRange(cell).formulas=[[value]];
  s.getRange(cell).format.font = {name:'Arial',size:10,color:value.includes('!')?'#25704B':'#000000'};
}
function totals(s, r, start, end, first=6) {
  s.getRange(`A${r}`).values=[['Summe']];
  for(let c=start;c<=end;c++) formula(s,`${col(c)}${r}`,`=SUM(${col(c)}${first}:${col(c)}${r-1})`);
  s.getRange(`A${r}:${col(end)}${r}`).format={fill:'#E8EBED',font:{name:'Arial',size:10,bold:true},rowHeight:29};
  s.getRange(`${col(start)}${r}:${col(end)}${r}`).setNumberFormat(money);
}
async function save(wb, caseName, filename, ranges) {
  wb.recalculate();
  const checked = await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:50},maxChars:3000});
  await fs.writeFile(path.join(qa,filename+'.inspect.txt'), checked.ndjson);
  for(const [name,range] of ranges) {
    const img=await wb.render({sheetName:name,range,scale:1.5,format:'png'});
    await fs.writeFile(path.join(qa,filename+'-'+name+'.png'),new Uint8Array(await img.arrayBuffer()));
    const data = await wb.inspect({kind:'table',range:`'${name}'!${range}`,include:'values,formulas',tableMaxRows:40,tableMaxCols:12,maxChars:20000});
    await fs.writeFile(path.join(qa,filename+'-'+name+'.jsonl'),data.ndjson);
  }
  const file=path.join(m.root,'testakten',caseName,filename);
  await (await SpreadsheetFile.exportXlsx(wb)).save(file);
  try {await fs.rename(file+'.inspect.ndjson',path.join(qa,filename+'.export-inspect.ndjson'));}
  catch(e) {if(e.code!=='ENOENT') throw e;}
  outputs.push(file);
  console.log('Arbeitsmappe erzeugt: '+filename);
}

async function badExtra() {
  const w=Workbook.create(), e=m.extra;
  const o=sheet(w,'Offene Posten','Ergänzungsstapel Lieferanten',['Rechnung','Kreditor','Rechnung EUR','Korrektur EUR','Zahlung EUR','Offen EUR','Bearbeitung'],[20,13,17,17,17,17,29]);
  const b=sheet(w,'Belege','Ergänzungsstapel Rechnungseingang',['Beleg','Projekt','Netto EUR','Schlüssel','USt im Beleg','Belegbetrag','Bezug'],[21,16,18,12,18,18,22]);
  const z=sheet(w,'Zuordnung','Projektkonto Zahlungszuordnung',['Bankreferenz','Valuta','Rechnung','Zugeordnet EUR'],[24,18,23,23]);
  const bank=sheet(w,'Bank','Projektkonto 471109',['Referenz','Valuta','Soll EUR','Zugeordnet EUR','Differenz EUR','Saldo EUR'],[24,18,20,22,20,22]);
  for(const s of [o,b,z,bank])s.getRange('A3').values=[['Stand 25.09.2026 | Ergänzungsstapel | Beträge in EUR']];
  const all=[...e.invoices,...e.credits];
  rows(b,all.map(i=>[i.id,i.project,i.net,i.rc?'RC19':'V19',null,null,i.invoice||i.id]));
  all.forEach((i,n)=>{const r=n+6;formula(b,`E${r}`,`=IF(D${r}="V19",ROUND(C${r}*0.19,2),0)`);formula(b,`F${r}`,`=SUM(C${r},E${r})`);});
  b.getRange('C6:C21').setNumberFormat(money);b.getRange('E6:F21').setNumberFormat(money);
  b.getRange('D6:D21').dataValidation={rule:{type:'list',values:['V19','RC19']}};
  b.tables.add('A5:G21',true,'Ergaenzungsbelege').style='TableStyleLight1';
  totals(b,22,4,5);formula(b,'C22','=SUM(C6:C21)');b.getRange('C22').setNumberFormat(money);
  b.getRange('A25').values=[['Quelle: 50 Ergänzungsjournal. RC19 enthält keine an den Lieferanten gezahlte Steuer.']];
  rows(z,e.allocations.map(r=>[r[0],date(r[1]),r[2],r[3]]));
  z.getRange('B6:B16').setNumberFormat('yyyy-mm-dd');z.getRange('D6:D17').setNumberFormat(money);
  z.tables.add('A5:D16',true,'Zahlungszuordnungen').style='TableStyleLight1';totals(z,17,3,3);
  z.getRange('A20').values=[['Quelle: 57 Zahlungszuordnung. EB-0916A verteilt sich auf zwei Rechnungen.']];
  rows(o,e.invoices.map(i=>[i.id,i.creditor,i.gross,null,null,null,i.status]));
  e.invoices.forEach((i,n)=>{const r=n+6;
    formula(o,`D${r}`,`=-SUMIFS('Belege'!$F$20:$F$21,'Belege'!$G$20:$G$21,A${r})`);
    formula(o,`E${r}`,`=SUMIFS('Zuordnung'!$D$6:$D$16,'Zuordnung'!$C$6:$C$16,A${r})`);
    formula(o,`F${r}`,`=C${r}-SUM(D${r}:E${r})`);
    formula(o,`C${r}`,`=SUMIFS('Belege'!$F$6:$F$21,'Belege'!$A$6:$A$21,A${r})`);
  });
  o.getRange('C6:F20').setNumberFormat(money);totals(o,20,2,5);
  o.tables.add('A5:G19',true,'ErgaenzungsOPOS').style='TableStyleLight1';
  o.getRange('G6:G19').dataValidation={rule:{type:'list',values:['ausgeglichen','Restzahlung offen','Bauabzug prüfen','Leistungsfreigabe fehlt','zur Prüfung']}};
  o.getRange('F6:F19').conditionalFormats.add('cellIs',{operator:'greaterThan',formula:0,format:{fill:'#FFF2CC'}});
  o.getRange('A22:C22').values=[['Nettokosten EUR','RC-Steuer EUR','RC-Vorsteuer EUR']];
  o.getRange('A22:C22').format={font:{name:'Arial',size:10,bold:true},wrapText:true,rowHeight:28};
  formula(o,'A23',"='Belege'!C22");
  formula(o,'B23',"=SUMIFS('Belege'!$C$6:$C$21,'Belege'!$D$6:$D$21,\"RC19\")*0.19");
  formula(o,'C23','=B23');o.getRange('A23:C23').setNumberFormat(money);
  o.getRange('A25').values=[['Fachliche Freigabe bleibt erforderlich. Steueransätze unter den Verwendungsannahmen in Datei 56.']];
  rows(bank,e.bank.map(r=>[r.reference,date(r.date),r.amount,null,null,null]));
  bank.getRange('B6:B15').setNumberFormat('yyyy-mm-dd');bank.getRange('C6:F15').setNumberFormat(money);
  bank.getRange('A18:B20').values=[['Anfangssaldo',e.opening],['Schluss laut Auszug',e.opening-e.bank.reduce((a,r)=>a+r.amount,0)],['Abweichung zum Auszug',null]];
  e.bank.forEach((i,n)=>{const r=n+6;formula(bank,`D${r}`,`=SUMIFS('Zuordnung'!$D$6:$D$16,'Zuordnung'!$A$6:$A$16,A${r})`);formula(bank,`E${r}`,`=C${r}-D${r}`);formula(bank,`F${r}`,r===6?'=$B$18-C6':`=F${r-1}-C${r}`);});
  formula(bank,'B20','=F15-B19');bank.getRange('B18:B20').setNumberFormat(money);
  bank.getRange('A23').values=[['Quelle: 48 Projektkonto Bank und 49 Kontoauszug. Keine Umsätze des Betriebskontos 471108.']];
  bank.tables.add('A5:F15',true,'ProjektkontoUmsaetze').style='TableStyleLight1';
  o.getRange('A6:G20').format.rowHeight=23;
  b.getRange('A6:G22').format.rowHeight=23;
  z.getRange('A6:D17').format.rowHeight=23;
  bank.getRange('A6:F15').format.rowHeight=23;
  await save(w,m.bad,'55_Ergaenzungsabgleich.xlsx',[['Offene Posten','A1:G25'],['Belege','A1:G25'],['Zuordnung','A1:D20'],['Bank','A1:F23']]);
}

async function warCost() {
  const w=Workbook.create();
  const k=sheet(w,'Kostenstand','WH26 Kostenfortschreibung',['Gewerk','Budget','Ist','Obligo','Unbestellt','Forecast','Abweichung'],[28,17,17,17,17,17,17]);
  const o=sheet(w,'Bestellungen','WH26 verbindliche Vergaben',['Gewerk','Leistung','Bestellt','Bestandsdatum'],[15,34,19,20]);
  const b=sheet(w,'Belege','WH26 gebuchte Kostenbelege',['Beleg','Gewerk','Buchung','Netto','Umsatzsteuer','Brutto'],[19,14,18,18,18,18]);
  const r=sheet(w,'Restleistungen','WH26 unbestellte Restleistungen',['Gewerk','Leistung','Nettoansatz'],[15,42,20]);
  rows(o,m.trades.map(t=>[t[0],t[1],t[3],date('2026-08-31')]));
  o.getRange('C6:C13').setNumberFormat(money); o.getRange('D6:D13').setNumberFormat('yyyy-mm-dd'); totals(o,14,2,2);
  rows(b,m.journal.map(t=>[t[0],t[1],date(t[2]),t[3],t[4],null]));
  b.getRange('C6:C19').setNumberFormat('yyyy-mm-dd');
  m.journal.forEach((t,i)=>formula(b,`F${i+6}`,`=SUM(D${i+6}:E${i+6})`));
  b.getRange('D6:F19').setNumberFormat(money); totals(b,20,3,5);
  rows(r,m.trades.map(t=>[t[0],t[1],t[5]]));r.getRange('C6:C13').setNumberFormat(money);totals(r,14,2,2);
  rows(k,m.trades.map(t=>[t[0]+' '+t[1],t[2],null,null,null,null,null]));
  m.trades.forEach((t,i)=>{
    const n=i+6;
    formula(k,`C${n}`,`=SUMIFS('Belege'!$D$6:$D$19,'Belege'!$B$6:$B$19,"${t[0]}")`);
    formula(k,`D${n}`,`='Bestellungen'!C${n}-C${n}`);
    formula(k,`E${n}`,`=IF(ISBLANK('Restleistungen'!C${n}),"offen",'Restleistungen'!C${n})`);
    formula(k,`F${n}`,`=IF(COUNT(C${n}:E${n})=3,SUM(C${n}:E${n}),"offen")`);
    formula(k,`G${n}`,`=IF(ISNUMBER(F${n}),F${n}-B${n},"offen")`);
  });
  k.getRange('B6:G13').setNumberFormat(money); totals(k,14,1,6);
  k.getRange('A6:G14').format.rowHeight=24;
  for(const column of ['E','F','G']) formula(k,column+'14',`=IF(COUNT(${column}6:${column}13)=8,SUM(${column}6:${column}13),"offen")`);
  k.getRange('A17:B20').values=[['Unvergebene Reserve',100000],['Gesamtbudget',null],['Abstand zum Budget',null],['Belegkontrolle',null]];
  formula(k,'B18','=SUM(B14,B17)'); formula(k,'B19','=IF(ISNUMBER(F14),B18-F14,"offen")'); formula(k,'B20',"=C14-'Belege'!D20");
  k.getRange('B17:B20').setNumberFormat(money);
  k.getRange('B20').setNumberFormat('#,##0.00');
  k.getRange('A23').values=[['Ohne KM N03 und MB 0925. Siehe Restkostenerhebung vom 25.09.2026.']];
  k.getRange('A24').values=[['Ist ist Leistungsaufwand, kein Zahlungsstand. Obligo ist bestellt abzüglich Ist.']];
  k.getRange('A25').values=[['Quellen: 04 Kostenrahmen, 11 Belegjournal, 12 Bestellbuch, 13 Restkostenerhebung.']];
  await save(w,m.war,'10_Kostenfortschreibung.xlsx',[['Kostenstand','A1:G25'],['Bestellungen','A1:D14'],['Belege','A1:F20'],['Restleistungen','A1:C14']]);
}

async function warSchedule() {
  const w=Workbook.create();
  const t=sheet(w,'Termine','WH26 Ablauf ohne mobiles Provisorium',['Vorgang','Planbeginn','Planende','Dauer Tage','Beginn aktuell','Ende aktuell','Tage später'],[33,17,17,16,18,18,17]);
  const z=sheet(w,'Zahlungen','WH26 Projektkonto und Zahlungsvorschau',['Monat','Anfang brutto','Zufluss brutto','Istrest netto','Neuleistung netto','Abfluss brutto','Ende brutto'],[16,18,18,18,20,18,18]);
  const a=sheet(w,'Ansätze','WH26 Termin und Zahlungsansätze',['Ansatz','Wert','Einheit','Bezug'],[37,22,17,54]);
  rows(a,[['Dauerhafte Energie',date('2026-11-16'),'Datum','07 Lieferfortschreibung'],['Maschinenversuche',15,'Kalendertage','27 Logistik Baufolge'],['Einweisung und Freigabe',6,'Kalendertage','27 Logistik Baufolge'],['Konto am 25.09.',512400,'EUR brutto','24 Bankansicht / 30 Finanzierung'],['Umsatzsteuersatz',.19,'Anteil','Bestellungen'],['Kranangebot',9600,'EUR netto','15 KM N03, nicht bestellt'],['Mobiles Angebot',36000,'EUR netto','18 MB 0925, nicht bestellt']]);
  a.getRange('B6').setNumberFormat('yyyy-mm-dd'); a.getRange('B9').setNumberFormat(money);a.getRange('B10').setNumberFormat('0.0%');a.getRange('B11:B12').setNumberFormat(money);
  rows(t,[['Fundamente',date('2026-04-01'),date('2026-05-08'),37,date('2026-04-01'),null,null],['Stahlmontage',date('2026-05-11'),date('2026-09-18'),130,date('2026-05-11'),null,null],['Gebäudehülle',date('2026-07-01'),date('2026-10-16'),107,date('2026-07-01'),null,null],['Sozialräume',date('2026-10-12'),date('2026-10-30'),18,date('2026-10-12'),null,null],['Außenentwässerung',date('2026-10-12'),date('2026-11-02'),21,date('2026-10-12'),null,null],['Dauerhafte Energie',date('2026-10-12'),date('2026-10-12'),0,null,null,null],['Maschinenversuche',date('2026-10-12'),date('2026-10-27'),null,null,null,null],['Einweisung und Freigabe',date('2026-10-27'),date('2026-11-02'),null,null,null,null]]);
  for(let n=6;n<=13;n++){formula(t,`F${n}`,`=E${n}+D${n}`);formula(t,`G${n}`,`=F${n}-C${n}`);}
  formula(t,'E11',"='Ansätze'!B6");formula(t,'E12','=E11');formula(t,'D12',"='Ansätze'!B7");formula(t,'E13','=F12');formula(t,'D13',"='Ansätze'!B8");
  t.getRange('B6:C13').setNumberFormat('yyyy-mm-dd');t.getRange('E6:F13').setNumberFormat('yyyy-mm-dd');
  t.getRange('A16').values=[['Maschinenversuche: Energie vorausgesetzt. Teilbetrieb mit mobiler Anlage nicht freigegeben.']];
  t.getRange('A17').values=[['Quellen: 07 Lieferfortschreibung, 08 Baubesprechung, 27 Baufolge. Tage sind Kalendertage.']];
  rows(z,[[date('2026-09-01'),null,0,160000,0,null,null],[date('2026-10-01'),null,400000,0,260000,null,null],[date('2026-11-01'),null,600000,0,430000,null,null],[date('2026-12-01'),null,0,0,316000,null,null]]);
  formula(z,'B6',"='Ansätze'!B9");
  for(let n=6;n<=9;n++) { if(n>6)formula(z,`B${n}`,`=G${n-1}`);formula(z,`F${n}`,`=ROUND(SUM(D${n}:E${n})*(1+'Ansätze'!$B$10),2)`);formula(z,`G${n}`,`=SUM(B${n}:C${n})-F${n}`); }
  z.getRange('A6:A9').setNumberFormat('yyyy-mm');z.getRange('B6:G9').setNumberFormat(money);
  totals(z,10,2,5);z.getRange('A10').values=[['Flüsse gesamt']];
  z.getRange('A13:B16').values=[['Restzahlung netto',null],['Restzahlung brutto',null],['Quelle brutto',1387540],['Kontrollsumme',null]];
  formula(z,'B13','=SUM(D10:E10)');formula(z,'B14','=F10');formula(z,'B16','=B14-B15');z.getRange('B13:B16').setNumberFormat(money);
  z.getRange('B16').setNumberFormat('#,##0.00');
  z.getRange('A19').values=[['September beginnt am Kontostand 25.09.; der offene Abschlag wird vorsorglich vor Fälligkeit geplant.']];
  z.getRange('A20').values=[['Ohne unbestellte Zusatzangebote, Zinsen und Vorsteuererstattungen. Quelle: 21 Zahlungsplan, 30 Finanzierung.']];
  await save(w,m.war,'09_Ablauf_und_Zahlungen.xlsx',[['Termine','A1:G17'],['Zahlungen','A1:G20'],['Ansätze','A1:D12']]);
}

async function badCredit() {
  const w=Workbook.create();
  const k=sheet(w,'Kreditoren','Mertens Lieferantenstand',['Kreditor','Belege brutto','Zahlung','Skonto brutto','Offen','Sicherheit','Freie OP'],[23,20,19,20,18,18,18]);
  const b=sheet(w,'Belege','Mertens Rechnungseingang',['Buchung','Kreditor','Netto','Steuerausweis %','USt im Beleg','Belegbetrag','Freigabe'],[21,14,18,15,18,20,22]);
  const p=sheet(w,'Ausgleich','Mertens Zahlungen und Abzüge',['Kreditor','Bankreferenz','Zahlung','Skonto brutto','Sicherheit','Bezugsbeleg'],[16,20,19,20,18,22]);
  rows(b,m.invoices.map(r=>[r[0],r[2],r[4],r[5],null,null,r[9]]));
  b.getRange('G6:G10').format.horizontalAlignment='center';
  for(let n=6;n<=10;n++){formula(b,`E${n}`,`=ROUND(C${n}*D${n},2)`);formula(b,`F${n}`,`=SUM(C${n},E${n})`);}
  b.getRange('C6:C10').setNumberFormat(money);b.getRange('D6:D10').setNumberFormat('0.0%');b.getRange('E6:F10').setNumberFormat(money);totals(b,11,4,5);
  b.getRange('A14').values=[['K100: Steuerschuldnerschaft des Leistungsempfängers, kein steuerfreier Umsatz.']];
  b.getRange('A15').values=[['Quellen: 22 Eingangsjournal sowie 05, 08, 11, 13 und 15 Rechnungsbelege.']];
  rows(p,[['K100','BK-0914',22800,0,1200,'RB-260901'],['K200','BK-0918',12828.2,261.8,0,'LB-260908'],['K300','BK-0922',2975,0,0,'WM-260915'],['K400','',0,0,0,'ST-260922']]);
  p.getRange('F6:F9').format.horizontalAlignment='center';
  p.getRange('C6:E9').setNumberFormat(money);totals(p,10,2,4);
  p.getRange('A13').values=[['Quelle: 19 Bankumsatz, 26 Freigabe. Die Zahlung BK-0924C ist noch nicht zugeordnet.']];
  rows(k,[['K100 Röding',null,null,null,null,null,null],['K200 Lippe',null,null,null,null,null,null],['K300 Weser',null,null,null,null,null,null],['K400 Seidel',null,null,null,null,null,null]]);
  for(let n=6;n<=9;n++) {
    const id='K'+((n-5)*100);
    formula(k,`B${n}`,`=SUMIFS('Belege'!$F$6:$F$10,'Belege'!$B$6:$B$10,"${id}")`);
    formula(k,`C${n}`,`='Ausgleich'!C${n}`); formula(k,`D${n}`,`='Ausgleich'!D${n}`);
    formula(k,`E${n}`,`=B${n}-SUM(C${n}:D${n})`);formula(k,`F${n}`,`='Ausgleich'!E${n}`);formula(k,`G${n}`,`=E${n}-F${n}`);
  }
  k.getRange('B6:G9').setNumberFormat(money);totals(k,10,1,6);
  k.getRange('A13:B15').values=[['OPOS laut Export',3342],['Differenz zum OPOS',null],['Belegsumme Kontrolle',null]];
  formula(k,'B14','=E10-B13');formula(k,'B15',"=B10-'Belege'!F11");k.getRange('B13:B15').setNumberFormat(money);
  k.getRange('B14:B15').setNumberFormat('#,##0.00');
  k.getRange('A18').values=[['Freie OP bezeichnet den Betrag ohne vertragliche Sicherheit, nicht eine Zahlungsfreigabe.']];
  k.getRange('A19').values=[['Quelle: 23 OPOS. ST-260922 ist gebucht; die Leistungsfreigabe steht aus.']];
  await save(w,m.bad,'24_Kreditorenabgleich.xlsx',[['Kreditoren','A1:G19'],['Belege','A1:G15'],['Ausgleich','A1:F13']]);
}

async function badProjects() {
  const w=Workbook.create();
  const s=sheet(w,'Projektkosten','Mertens ausgewählter Kostenstand',['Projekt','Fremdleistung netto','Lohnkosten','Gesamt netto','Budget netto','Budgetrest'],[23,27,20,21,22,21]);
  const f=sheet(w,'Fremdleistungen','Mertens Projektzuordnung',['Beleg','Projekt','Netto','Minderung netto','Projektkosten'],[24,22,20,22,22]);
  const l=sheet(w,'Lohn August','Mertens gewerbliche Projektstunden',['Personalnr','Projekt','Stunden','Lohn je Stunde','Bruttolohn','AG Belastung','Projektkosten'],[20,22,17,20,21,21,21]);
  const b=sheet(w,'Bank','Mertens Betriebskonto September',['Referenz','Valuta','Gegenpartei','Haben','Soll','Saldo'],[21,18,31,20,20,21]);
  rows(f,[['RB-260901','BS26-01',24000,0,null],['LB-260908','BS26-01',12000,220,null],['LB-G260912','BS26-01',-1000,0,null],['WM-260915/1','BS26-01',1500,0,null],['WM-260915/2','BS26-02',1000,0,null],['ST-260922','BS26-02',1800,0,null]]);
  for(let n=6;n<=11;n++) formula(f,`E${n}`,`=C${n}-D${n}`);
  f.getRange('C6:E11').setNumberFormat(money);totals(f,12,2,4);
  f.getRange('A15').values=[['Quelle: Rechnungen, 14 Mietnachweis, 12 Skontobestätigung. Seidel bleibt trotz offener Freigabe im Kostenstand.']];
  rows(l,Array.from({length:10},(_,i)=>['P'+String(i+1).padStart(3,'0'),i<6?'BS26-01':'BS26-02',70,30,null,440,null]));
  for(let n=6;n<=15;n++){formula(l,`E${n}`,`=ROUND(C${n}*D${n},2)`);formula(l,`G${n}`,`=SUM(E${n}:F${n})`);}
  l.getRange('D6:G15').setNumberFormat(money);totals(l,16,4,6);
  l.getRange('A19:B20').values=[['Lohnquelle Kosten',25400],['Kontrollsumme',null]];formula(l,'B20','=G16-B19');l.getRange('B19:B20').setNumberFormat(money);
  l.getRange('B20').setNumberFormat('#,##0.00');
  l.getRange('A23').values=[['Quelle: 17 Lohnzusammenfassung, 18 Projektstunden. Leistungsmonat August; Zahlung im September.']];
  rows(s,[['BS26-01',null,null,null,180000,null],['BS26-02',null,null,null,95000,null]]);
  for(let n=6;n<=7;n++) {formula(s,`B${n}`,`=SUMIFS('Fremdleistungen'!$E$6:$E$11,'Fremdleistungen'!$B$6:$B$11,A${n})`);formula(s,`C${n}`,`=SUMIFS('Lohn August'!$G$6:$G$15,'Lohn August'!$B$6:$B$15,A${n})`);formula(s,`D${n}`,`=SUM(B${n}:C${n})`);formula(s,`F${n}`,`=E${n}-D${n}`);}
  s.getRange('B6:F7').setNumberFormat(money);totals(s,8,1,5);
  s.getRange('A11').values=[['Ausgewählter Belegstapel und Auguststunden. Budgetrest ist keine Restkostenprognose.']];
  s.getRange('A12').values=[['Keine Vollständigkeitsaussage zum Gesamtprojekt. Konto 1590 ist noch ohne Projektzuordnung.']];
  s.getRange('A13').values=[['Quelle Budget: 02 Projektstamm. Fremdleistungen enthalten noch nicht bezahlte Rechnungen.']];
  rows(b,m.bank.map(r=>[r[0],date(r[1]),r[2],r[4],r[5],null]));
  b.getRange('B6:B13').setNumberFormat('yyyy-mm-dd');
  b.getRange('B6:B13').format.horizontalAlignment='center';
  b.getRange('A16:B19').values=[['Anfangssaldo',85000],['Schluss laut Auszug',79211.8],['Kontrollsumme',null],['Konto 1590',1785]];
  formula(b,'F6','=SUM($B$16,D6)-E6');for(let n=7;n<=13;n++)formula(b,`F${n}`,`=SUM(F${n-1},D${n})-E${n}`);
  formula(b,'B18','=F13-B17');b.getRange('D6:F13').setNumberFormat(money);b.getRange('B16:B19').setNumberFormat(money);
  b.getRange('B18').setNumberFormat('#,##0.00');
  b.getRange('A22').values=[['Quelle: 19 Bankumsatz und 28 Kontoauszug. BK-0924C auf Konto 1590 ohne Belegzuordnung.']];
  await save(w,m.bad,'25_Projektkosten_und_Bank.xlsx',[['Projektkosten','A1:F13'],['Fremdleistungen','A1:E15'],['Lohn August','A1:G23'],['Bank','A1:F22']]);
}

function html(title, subtitle, headers, data, summary, gantt=false) {
  const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;');
  return `<!doctype html><html lang="de"><meta charset="utf-8"><style>*{box-sizing:border-box}body{margin:0;background:#f0f2f3;color:#202829;font:18px Arial}header{height:68px;background:#314947;color:white;padding:22px 34px}nav{padding:20px 34px;border-bottom:1px solid #ccd3d3;background:white;color:#48605e}main{padding:30px 34px}h1{font-size:29px;margin:0 0 12px}p{margin:0 0 24px;color:#556563}.summary{display:flex;gap:60px;background:white;padding:23px;margin-bottom:26px;border-left:5px solid #698e80}.summary b{display:block;font-size:28px;margin-top:8px;color:#182b28}table{border-collapse:collapse;width:100%;background:white;table-layout:fixed}th{text-align:left;background:#dce4e1;padding:17px 14px;font-size:17px}td{padding:19px 14px;border-bottom:1px solid #e3e7e6;overflow-wrap:anywhere}td:last-child{text-align:right}footer{padding:18px 34px;font-size:15px;color:#596a67}.bar{height:15px;background:#82a69a;margin-top:6px}</style><header>${esc(title)}</header><nav>Übersicht &nbsp; / &nbsp; Vorgänge &nbsp; / &nbsp; Auswertung</nav><main><h1>${esc(subtitle)}</h1><p>25.09.2026 · 16:00 Uhr · gespeicherte Ansicht</p><div class="summary">${summary.map(([a,b])=>`<div>${esc(a)}<b>${esc(b)}</b></div>`).join('')}</div><table><thead><tr>${headers.map(s=>`<th>${esc(s)}</th>`).join('')}</tr></thead><tbody>${data.map((r,i)=>`<tr>${r.map((s,j)=>`<td>${esc(s)}${gantt&&j===1?`<div class="bar" style="width:${35+i*8}%"></div>`:''}</td>`).join('')}</tr>`).join('')}</tbody></table></main><footer>Geschäftsansicht · Zugriff Buchhaltung und Projektleitung</footer></html>`;
}
async function screenshots() {
  let browser;
  browser=await chromium.launch({headless:true,...(process.env.AKTEN_CHROMIUM ? {executablePath:process.env.AKTEN_CHROMIUM} : {})});
  const page=await browser.newPage({viewport:{width:1400,height:1000},deviceScaleFactor:1});
  const specs=[
    [m.war,'24_Bankansicht.png',html('Emsland Firmenbank · Hagedorn Präzisionsteile GmbH','Projektkonto WH26',['Buchungsgruppe','Zeitraum','Haben EUR','Soll EUR'],[['Eigenmittel und Kredit','bis 25.09.2026','1.750.000,00','0,00'],['Ausgeführte Zahlungen','bis 25.09.2026','0,00','1.237.600,00'],['Vorgemerkte Umsätze','25.09.2026','0,00','0,00']],[['Buchsaldo','512.400,00 EUR'],['Verfügbar','512.400,00 EUR'],['Offener Abschlag','190.400,00 EUR']])],
    [m.war,'25_Bauterminansicht.png',html('Westkamp Bauablauf · WH26','Terminfortschreibung',['Vorgang','Zeitraum aktuell','Bisheriges Ende','Aktuelles Ende'],[['Gebäudehülle','01.07. bis 16.10.','16.10.2026','16.10.2026'],['Sozialräume','12.10. bis 30.10.','30.10.2026','30.10.2026'],['Trafo Inbetriebnahme','16.11.','12.10.2026','16.11.2026'],['Maschinenversuche','16.11. bis 01.12.','27.10.2026','01.12.2026'],['Einweisung und Freigabe','01.12. bis 07.12.','02.11.2026','07.12.2026']],[['Planstand','25.09.2026'],['Baufolge','ohne Provisorium'],['Teilbetrieb','nicht freigegeben']],true)],
    [m.bad,'20_Bankansicht.png',html('Lippische Gewerbebank · Bauunternehmen Mertens GmbH','Geschäftskonto 471108',['Referenz','Empfänger','Verwendungszweck','Soll EUR'],[['BK-0922','Weser Miettechnik','WM-260915','2.975,00'],['BK-0923','Lohn August','SAM-0826','15.700,00'],['BK-0924A','Sozialkassen','SV-0826','7.700,00'],['BK-0924B','Finanzamt','LSt-0826','2.000,00'],['BK-0924C','Weser Miettechnik','Mietpark 09','1.785,00']],[['Buchsaldo','79.211,80 EUR'],['Vorgemerkt','0,00 EUR'],['Umsätze September','8']])],
    [m.bad,'21_ERP_Belegansicht.png',html('Mertens Büro · Rechnungseingang','Gebuchte Lieferantenbelege',['Buchung','Lieferantenbeleg','Freigabe','Belegbetrag EUR'],[['ER-260901','RB-260901','freigegeben','24.000,00'],['ER-260908','LB-260908','freigegeben','14.280,00'],['GS-260912','LB-G260912','verrechnet','-1.190,00'],['ER-260915','WM-260915','freigegeben','2.975,00'],['ER-260922','ST-260922','ausstehend','2.142,00']],[['Belege','5'],['Offene Posten','3.342,00 EUR'],['Konto 1590','1.785,00 EUR']])]
  ];
  for(const [caseName,name,content] of specs){await page.setContent(content);await page.screenshot({path:path.join(m.root,'testakten',caseName,name),fullPage:true});}
  await browser.close();
}

if(!m.extra_only) {
  await warCost();
  await warSchedule();
  await badCredit();
  await badProjects();
  await screenshots();
}
await badExtra();
await fs.writeFile(path.join(qa,'workbooks.json'),JSON.stringify(outputs,null,2));

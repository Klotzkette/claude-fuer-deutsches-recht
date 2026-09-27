// Drei native Projektarbeitsmappen; ausschließlich Artifact Tool. Autor: Klotzkette.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import { loadWorkbookRuntime } from './akten-workbook-runtime.mjs';
const {Workbook, SpreadsheetFile} = await loadWorkbookRuntime();
const m=JSON.parse(await fs.readFile(process.argv[2],'utf8'));
m.root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
m.case=path.resolve(m.root,m.case);
await fs.mkdir(m.qa,{recursive:true});
const money='#,##0.00_);(#,##0.00);"-"_);@';
const number='#,##0.00;(#,##0.00);"-"';
const serial=s=>Math.round((Date.parse(s+'T00:00:00Z')-Date.UTC(1899,11,30))/86400000);
const letter=n=>String.fromCharCode(65+n);
const reports=[];

function sheet(w,name,title,headers,widths,subtitle='SW-HI-26-08 · Beträge in EUR') {
  const s=w.worksheets.add(name);s.showGridLines=false;
  const last=letter(headers.length-1);
  s.getRange(`A1:${last}90`).format.font={name:'Arial',size:10,color:'#222222'};
  s.getRange('A2').values=[[title]];s.getRange('A2').format.font={name:'Arial',size:14,bold:true};
  s.getRange('A3').values=[[subtitle]];s.getRange('A3').format.font={name:'Arial',size:10,italic:true};
  s.getRange(`A5:${last}5`).values=[headers];
  s.getRange(`A5:${last}5`).format={fill:'#324B62',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:35,horizontalAlignment:'center',verticalAlignment:'center'};
  widths.forEach((v,i)=>s.getRange(`${letter(i)}1:${letter(i)}90`).format.columnWidth=v);
  s.freezePanes.freezeRows(5);return s;
}
function put(s,data) {
  const last=data.length+5,end=letter(data[0].length-1);
  s.getRange(`A6:${end}${last}`).values=data;
  s.getRange(`A6:${end}${last}`).format={font:{name:'Arial',size:10},rowHeight:31,wrapText:true,verticalAlignment:'center'};
  data.forEach((r,i)=>r.forEach((v,j)=>{if(typeof v==='number')s.getRange(`${letter(j)}${i+6}`).format.font.color='#2457A7';}));
}
function formula(s,cell,f) {s.getRange(cell).formulas=[[f]];s.getRange(cell).format.font.color=f.includes('!')?'#246946':'#222222';}
function total(s,row,start,end,first=6) {
  s.getRange(`A${row}`).values=[['Summe']];
  for(let c=start;c<=end;c++)formula(s,`${letter(c)}${row}`,`=SUM(${letter(c)}${first}:${letter(c)}${row-1})`);
  s.getRange(`A${row}:${letter(end)}${row}`).format={fill:'#E8EDF1',font:{name:'Arial',size:10,bold:true},rowHeight:29};
}
async function save(w,filename,ranges,mutations=[]) {
  w.recalculate();
  const report={file:filename,sheets:[],mutations:[]};
  const errors=await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:200},maxChars:10000});
  await fs.writeFile(path.join(m.qa,filename+'.errors.jsonl'),errors.ndjson);
  for(const [name,range] of ranges) {
    const inspect=await w.inspect({kind:'table',range:`'${name}'!${range}`,include:'values,formulas',tableMaxRows:90,tableMaxCols:12,maxChars:50000});
    await fs.writeFile(path.join(m.qa,filename+'-'+name+'.jsonl'),inspect.ndjson);
    const png=await w.render({sheetName:name,range,scale:1.5,format:'png'});
    await fs.writeFile(path.join(m.qa,filename+'-'+name+'.png'),new Uint8Array(await png.arrayBuffer()));
    report.sheets.push({name,range});
  }
  await (await SpreadsheetFile.exportXlsx(w)).save(path.join(m.case,filename));
  const baseline=[];
  for(let i=0;i<mutations.length;i++) {
    const spec=mutations[i],s=w.worksheets.getItem(spec.sheet);
    const original=s.getRange(spec.cell).values;
    s.getRange(spec.cell).values=[[spec.value]];w.recalculate();
    const out=w.worksheets.getItem(spec.outputSheet).getRange(spec.outputCell).values[0][0];
    if(typeof spec.expected==='number' ? Math.abs(out-spec.expected)>.005 : out!==spec.expected)throw new Error(JSON.stringify({mutation:spec,actual:out}));
    const p=path.join(m.qa,'mutation-input',`${i+1}_${filename}`);await fs.mkdir(path.dirname(p),{recursive:true});
    await (await SpreadsheetFile.exportXlsx(w)).save(p);
    report.mutations.push({...spec,result:out,path:p});
    s.getRange(spec.cell).values=original;w.recalculate();
  }
  // The delivered file is the restored baseline; mutations remain only in QA.
  await (await SpreadsheetFile.exportXlsx(w)).save(path.join(m.case,filename));
  try {await fs.rename(path.join(m.case,filename+'.inspect.ndjson'),path.join(m.qa,filename+'.export-inspect.ndjson'));}
  catch(e) {if(e.code!=='ENOENT')throw e;}
  reports.push(report);console.log(filename+' geschrieben und gerechnet');
}

function belegSheet(w, name='Belege') {
  const s=sheet(w,name,'Projektbelege',['Beleg','KG','Datum','Leistung','Netto EUR','USt EUR','Brutto EUR'],[21,8,15,43,19,17,19]);
  put(s,m.invoices.map(x=>[x.id,x.kg,serial(x.date),x.label,x.net,x.vat,null]));
  m.invoices.forEach((x,i)=>formula(s,`G${i+6}`,`=SUM(E${i+6}:F${i+6})`));
  const end=m.invoices.length+5;
  s.getRange(`C6:C${end}`).setNumberFormat('yyyy-mm-dd');s.getRange(`E6:G${end+1}`).setNumberFormat(money);
  s.getRange(`C6:C${end}`).format.horizontalAlignment='center';
  s.tables.add(`A5:G${end}`,true,'Projektbelege'+name.replace(/[^A-Za-z]/g,'')).style='TableStyleLight1';
  total(s,end+1,4,6);
  s.getRange(`A${end+3}`).values=[['Quelle: Einzelbelege 70–106 und 119; Rechnungskorrekturen sind negativ.']];
  return s;
}

async function kosten() {
  const w=Workbook.create();
  const s=sheet(w,'Kostenstand','Wohnhof Am Steinbogen 18 · Kostenentwicklung',['KG','Kostenbereich','Ausgang EUR','Abgerechnet EUR','Änderung EUR'],[8,44,23,23,22]);
  const b=belegSheet(w);
  const end=m.invoices.length+5;
  put(s,m.groups.map(x=>[x[0],x[1],x[2],null,null]));
  for(let r=6;r<=12;r++) {formula(s,`D${r}`,`=SUMIF('Belege'!$B$6:$B$${end},A${r},'Belege'!$G$6:$G$${end})`);formula(s,`E${r}`,`=D${r}-C${r}`);}
  total(s,13,2,4);s.getRange('C6:E13').setNumberFormat(money);
  s.getRange('B16:C19').values=[['Freigegebener Kostenrahmen',m.budget],['Noch verfügbar bis Kostenrahmen',null],['Eigenkapital und Darlehen',m.equity+m.loan],['Projektmittel nach Belegbeträgen',null]];
  formula(s,'C17','=C16-D13');formula(s,'C19','=C18-D13');s.getRange('C16:C19').setNumberFormat(money);
  s.getRange('B22').values=[['Stand 05.10.2033. Kostenfortschreibung einschließlich LPH 9.']];
  s.getRange('B23').values=[['Projektkosten und Zahlungen sind getrennt; keine AfA- oder Bilanzberechnung.']];
  s.getRange('B24').values=[['Umsatzsteuerbeträge werden für die Wohnvermietung nicht als Vorsteuer abgezogen.']];
  s.getRange('C16:C19').format.rowHeight=27;
  s.getRange('A6:E12').format.rowHeight=27;
  s.getRange('A21:E25').format.rowHeight=17;
  const mutrow=m.invoices.findIndex(x=>x.id==='SH-28-021')+6;
  await save(w,'120_Kostenentwicklung.xlsx',[['Kostenstand','A1:E25'],['Belege',`A1:G${end+3}`]],[{sheet:'Belege',cell:`E${mutrow}`,value:201000,outputSheet:'Kostenstand',outputCell:'D13',expected:m.total+1000}]);
}

async function payments() {
  const w=Workbook.create();
  const o=sheet(w,'Offene Posten','Rechnungen und Zahlungen',['Beleg','Rechnungsdatum','Beleg bis Stichtag','Zahlung bis Stichtag','Saldo EUR'],[23,18,25,26,22], 'SW-HI-26-08 · Eingangsbelege und tatsächliche Kontoumsätze');
  const b=belegSheet(w);
  const z=sheet(w,'Bank','Projektkonto 882608',['Valuta','Bankreferenz','Beleg / Herkunft','Zahlung EUR','Zufluss Mittel','Kontosaldo EUR'],[16,27,25,22,22,23]);
  o.getRange('A3').values=[['Stichtag']];o.getRange('B3').values=[[serial('2028-09-30')]];o.getRange('B3').setNumberFormat('yyyy-mm-dd');o.getRange('B3').format={fill:'#FFF2CC',font:{name:'Arial',size:11,color:'#2457A7'}};
  const end=m.invoices.length+5,bend=m.transactions.length+5;
  put(z,m.transactions.map(t=>[serial(t.date),t.reference,t.invoice,t.direction==='Abfluss'?t.amount:t.direction==='Erstattung'?-t.amount:0,t.direction==='Zufluss'?t.amount:0,null]));
  m.transactions.forEach((t,i)=>formula(z,`F${i+6}`,i===0?'=E6-D6':`=F${i+5}+E${i+6}-D${i+6}`));
  z.getRange(`A6:A${bend}`).setNumberFormat('yyyy-mm-dd');z.getRange(`D6:F${bend}`).setNumberFormat(money);
  z.getRange(`A6:A${bend}`).format.horizontalAlignment='center';
  z.tables.add(`A5:F${bend}`,true,'Projektkontoumsaetze').style='TableStyleLight1';
  z.getRange(`A${bend+2}`).values=[['Quelle: vollständige Projektkontoauszüge 109–112; Erstattungen als negative Zahlungen.']];
  put(o,m.invoices.map(i=>[i.id,serial(i.date),null,null,null]));o.getRange(`B6:B${end}`).setNumberFormat('yyyy-mm-dd');o.getRange(`C6:E${end+1}`).setNumberFormat(money);
  for(let r=6;r<=end;r++) {
    formula(o,`C${r}`,`=SUMIFS('Belege'!$G$6:$G$${end},'Belege'!$A$6:$A$${end},A${r},'Belege'!$C$6:$C$${end},"<="&$B$3)`);
    formula(o,`D${r}`,`=SUMIFS('Bank'!$D$6:$D$${bend},'Bank'!$C$6:$C$${bend},A${r},'Bank'!$A$6:$A$${bend},"<="&$B$3)`);
    formula(o,`E${r}`,`=C${r}-D${r}`);
  }
  total(o,end+1,2,4);
  o.getRange(`A${end+3}`).values=[['Positiver Saldo: noch nicht gezahlt; negativer Saldo: Zahlbetrag über Belegbetrag.']];
  o.getRange(`A${end+4}`).values=[['Die Liste ersetzt keine fachliche Rechnungsfreigabe. Spätere Belege werden durch den Stichtag ausgeschlossen.']];
  o.tables.add(`A5:E${end}`,true,'RechnungenStichtag').style='TableStyleLight1';
  const r=m.invoices.findIndex(x=>x.id==='LE-28-061')+6;
  await save(w,'121_Rechnungen_und_Zahlungen.xlsx',[['Offene Posten',`A1:E${end+4}`],['Belege',`A1:G${end+3}`],['Bank',`A1:F${bend+2}`]],
    [{sheet:'Offene Posten',cell:'B3',value:serial('2028-06-17'),outputSheet:'Offene Posten',outputCell:`E${r}`,expected:0},
     {sheet:'Offene Posten',cell:'B3',value:serial('2028-06-20'),outputSheet:'Offene Posten',outputCell:`E${r}`,expected:-89250},
     {sheet:'Offene Posten',cell:'B3',value:serial('2033-10-05'),outputSheet:'Offene Posten',outputCell:`E${end+1}`,expected:0}]);
}

async function financing() {
  const w=Workbook.create();
  const f=sheet(w,'Finanzierung','Projektfinanzierung und Vermietungsannahmen',['Ansatz / Ergebnis','Wert','Grundlage'],[47,24,61]);
  const r=sheet(w,'Vermietung','Vermietung · volles Planjahr',['Wohnung','Wohnfläche m²','EUR je m²','Wohnung mtl.','Stellplatz mtl.','Jahresmiete'],[16,21,19,23,24,24]);
  const d=sheet(w,'Tilgung','Darlehensplan 2029 bis 2033',['Monat','Anfangsschuld','Annuität','Zinsen','Tilgung','Restschuld'],[18,24,22,22,22,24]);
  put(f,[['Projektkosten Ausgang',m.base,'Kostenansätze aus Einzelbelegen; ohne Nachtrag/Korrektur'],['Nachtrag und Entgeltminderung',m.total-m.base,'105 Rohbau / 106 Innenausbau'],['Projektkosten fortgeschrieben',null,'Summe aus den beiden vorstehenden Ansätzen'],['Eigenkapital',m.equity,'108 Gesellschafterbeschluss'],['Darlehen',m.loan,'107 Darlehensvereinbarung'],['Finanzierungsmittel',null,'Eigenkapital und Darlehen'],['Mittel nach Projektkosten',null,'Finanzierungsmittel abzüglich Projektkosten'],['Sollzins p. a.',m.interest,'107 Darlehensvereinbarung ab 2029'],['Anfängliche Tilgung p. a.',m.repayment,'107 Darlehensvereinbarung ab 2029'],['Annuität volles Jahr',null,'Anfängliche Zinsen plus anfängliche Tilgung'],['Leerstand / Mietausfall',0,'Annahme; Anteil der möglichen Jahreskaltmiete'],['Nicht umlagefähige Kosten p. a.',m.operating_cost,'108 Planannahme; keine bereits angefallenen Kosten'],['Miete volles Jahr vor Ausfall',null,'Vermietung: Wohnungs- und Stellplatzkaltmieten'],['Miete nach Ausfall',null,'Mögliche Miete mal vermieteter Anteil'],['Ergebnis vor Finanzierung',null,'Miete nach Ausfall abzüglich laufender Kosten'],['Jährlicher Schuldendienst',null,'Annuität ab Januar 2029'],['Liquidität vor Ertragsteuern',null,'Laufendes Ergebnis abzüglich Schuldendienst'],['Schuldendienstdeckung',null,'Ergebnis vor Finanzierung / Schuldendienst']]);
  formula(f,'B8','=SUM(B6:B7)');formula(f,'B11','=SUM(B9:B10)');formula(f,'B12','=B11-B8');
  formula(f,'B15','=B10*SUM(B13:B14)');formula(f,'B18',"='Vermietung'!F14");
  formula(f,'B19','=IF(AND(ISNUMBER(B18),ISNUMBER(B16)),B18*(1-B16),"offen")');
  formula(f,'B20','=IF(AND(ISNUMBER(B19),ISNUMBER(B17)),B19-B17,"offen")');formula(f,'B21','=B15');
  formula(f,'B22','=IF(ISNUMBER(B20),B20-B21,"offen")');formula(f,'B23','=IF(AND(ISNUMBER(B20),B21>0),B20/B21,"offen")');
  f.getRange('B6:B22').setNumberFormat(money);f.getRange('B13:B14').setNumberFormat('0.0%');f.getRange('B16').setNumberFormat('0.0%');f.getRange('B23').setNumberFormat('0.00" x"');
  f.getRange('B13:B14').format.horizontalAlignment='center';f.getRange('B16').format.horizontalAlignment='center';
  f.getRange('A25').values=[['Planjahr 2029 bei ganzjähriger Vermietung. Keine Aussage zur zulässigen Miethöhe.']];
  f.getRange('A26').values=[['Keine Betriebs-/Heizkostenvorauszahlungen und keine Kautionen als Ertrag gerechnet.']];
  f.getRange('A27').values=[['AfA, Ertragsteuern und spätere Anschlussfinanzierung sind hier nicht modelliert.']];
  f.getRange('B16').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:1}};
  put(r,m.areas.map((a,i)=>[`WE ${String(i+1).padStart(2,'0')}`,a,m.rent_sqm,null,m.parking_rent,null]));
  for(let n=6;n<=13;n++){formula(r,`D${n}`,`=IF(COUNT(B${n}:C${n})=2,B${n}*C${n},"offen")`);formula(r,`F${n}`,`=IF(COUNT(D${n}:E${n})=2,SUM(D${n}:E${n})*12,"offen")`);}
  total(r,14,1,5);r.getRange('C14').clear({applyTo:'contents'});formula(r,'D14','=IF(COUNT(D6:D13)=8,SUM(D6:D13),"offen")');formula(r,'F14','=IF(COUNT(F6:F13)=8,SUM(F6:F13),"offen")');
  r.getRange('B6:B14').setNumberFormat('#,##0.00');r.getRange('C6:F14').setNumberFormat(money);
  r.getRange('A17').values=[['Quelle: 108 Gesellschafterbeschluss und Vermietungsannahmen.']];
  r.getRange('A18').values=[['Die acht Stellplätze sind den acht Wohnungen zugeordnet.']];
  const monthly=Array.from({length:60},(_,i)=>[serial(`${2029+Math.floor(i/12)}-${String(i%12+1).padStart(2,'0')}-01`),null,null,null,null,null]);
  put(d,monthly);
  for(let n=6;n<=65;n++) {
    formula(d,`B${n}`,n===6?"='Finanzierung'!B10":`=F${n-1}`);
    formula(d,`C${n}`,`=MIN(B${n}+D${n},'Finanzierung'!$B$15/12)`);
    formula(d,`D${n}`,`=ROUND(B${n}*'Finanzierung'!$B$13/12,2)`);
    formula(d,`E${n}`,`=C${n}-D${n}`);formula(d,`F${n}`,`=B${n}-E${n}`);
  }
  d.getRange('A6:A65').setNumberFormat('mmm-yyyy');d.getRange('B6:F66').setNumberFormat(money);total(d,66,2,4);d.getRange('A66').values=[['Summe 60 Monate']];formula(d,'F66','=F65');
  d.getRange('A68').values=[['Quelle: 107 Darlehensvereinbarung; gleichbleibende Monatsrate bei sinkender Restschuld.']];
  const rentWithoutFirst=102000-m.areas[0]*m.rent_sqm*12;
  await save(w,'122_Finanzierung_und_Vermietung.xlsx',[['Finanzierung','A1:C28'],['Vermietung','A1:F19'],['Tilgung','A1:F68']],
    [{sheet:'Vermietung',cell:'C6',value:0,outputSheet:'Finanzierung',outputCell:'B18',expected:rentWithoutFirst},
     {sheet:'Vermietung',cell:'C6',value:null,outputSheet:'Finanzierung',outputCell:'B22',expected:'offen'},
     {sheet:'Finanzierung',cell:'B16',value:.05,outputSheet:'Finanzierung',outputCell:'B22',expected:-2700},
     {sheet:'Finanzierung',cell:'B13',value:.04,outputSheet:'Tilgung',outputCell:'D6',expected:5333.33}]);
}
await kosten();await payments();await financing();
await fs.writeFile(path.join(m.qa,'workbook-qa.json'),JSON.stringify(reports,null,2)+'\n');

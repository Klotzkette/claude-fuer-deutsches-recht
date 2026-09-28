#!/usr/bin/env node
// Reproduzierbare Finanzunterlagen der Schnittflug-Akte. Benötigt den gebündelten Codex-Node.
// Aufruf: node scripts/build-startup-gruender-finanz.mjs [QA-Verzeichnis außerhalb des Repos]
import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createHash } from 'node:crypto';

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const qa = path.resolve(process.argv[2] || '/tmp/startup-gruender-finanz-qa');
assert(!qa.startsWith(repo + path.sep));
await fs.mkdir(qa, { recursive: true });
try { await fs.lstat(path.join(qa, 'node_modules')); } catch {
  await fs.symlink(path.resolve(path.dirname(process.execPath), '../node_modules'), path.join(qa, 'node_modules'), 'dir');
}
const runtime = createRequire(path.join(qa, 'runtime.cjs'));
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(runtime.resolve('@oai/artifact-tool')).href);
const JSZip = runtime('jszip');
const data = JSON.parse(await fs.readFile(path.join(repo, 'scripts/data/startup-gruender/finanz.json'), 'utf8'));
const fall = JSON.parse(await fs.readFile(path.join(repo, 'scripts/data/startup-gruender/fallstamm.json'), 'utf8'));
const dest = path.join(repo, 'testakten', fall.case_slug);
await fs.mkdir(dest, { recursive: true });
const C = { ink:'#1D2833', blue:'#234769', input:'#174FC0', linked:'#176539', pale:'#EEF3F8', amber:'#FFF3C4', red:'#9C2634', line:'#B9C9D7' };
const EUR = '#,##0.00;(#,##0.00);"–"';
const NOM = '#,##0;(#,##0);"–"';
const PCT = '0.00%;(0.00%);"–"';
const col = n => String.fromCharCode(65+n);
const sum = xs => xs.reduce((a,b)=>a+b,0);
const near = (a,b,label) => assert(Math.abs(a-b)<0.0000001, `${label}: ${a} != ${b}`);
const put=(s,cell,v)=>{s.getRange(cell).values=[[v]];};
const fx=(s,cell,v)=>{s.getRange(cell).formulas=[[v]];s.getRange(cell).format.font.color=v.includes('!')?C.linked:'#000000';};
const val=(s,cell)=>s.getRange(cell).values[0][0];
const input=(s,range,fmt)=>{s.getRange(range).format.font.color=C.input;s.getRange(range).format.fill=C.amber;if(fmt)s.getRange(range).setNumberFormat(fmt);};
function book(names){const w=Workbook.create();for(const n of names)w.worksheets.add(n);return w;}
function base(w,name,widths,rows,title,subtitle='Stand 28.09.2026. Ottilie Kühnle. Nicht vollzogene Planung.'){
 const s=w.worksheets.getItem(name),last=col(widths.length-1);s.showGridLines=false;
 s.getRange(`A1:${last}${rows}`).format={font:{name:'Arial',size:11,color:C.ink},verticalAlignment:'center',rowHeight:25};
 widths.forEach((v,i)=>{s.getRange(`${col(i)}1:${col(i)}${rows}`).format.columnWidthPx=v;});
 s.getRange(`A1:${last}1`).format.rowHeight=10;
 put(s,'B2',title);s.getRange('B2').format.font={name:'Arial',size:16,bold:true,color:C.blue};
 put(s,'B3',subtitle);s.getRange(`B3:${last}3`).format.rowHeight=24;
 s.getRange(`B4:${last}4`).format.borders={bottom:{style:'thin',color:C.blue}};
 s.tabColor=C.blue;return s;
}
function header(s,range){s.getRange(range).format={fill:C.blue,font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},horizontalAlignment:'center',verticalAlignment:'center',wrapText:true,rowHeight:40,borders:{insideVertical:{style:'thin',color:'#FFFFFF'}}};}
function total(s,range){s.getRange(range).format={fill:C.pale,font:{name:'Arial',size:11,bold:true,color:C.ink},borders:{top:{style:'thin',color:C.blue}},rowHeight:28};}
function note(s,row,text,end='H',height=34){put(s,`B${row}`,text);s.mergeCells(`B${row}:${end}${row}`);s.getRange(`B${row}:${end}${row}`).format={wrapText:true,rowHeight:height,font:{name:'Arial',size:11,color:C.ink}};}
function numeric(s,range,fmt=EUR){s.getRange(range).setNumberFormat(fmt);s.getRange(range).format.horizontalAlignment='right';}
const reports=[];
// Drucktitel und Abschnittsumbrüche halten Fortsetzungen ohne Inhaltsänderung lesbar.
const printLayout={
 '50_CapTable_Gruendung_und_Finanzierungsoptionen.xlsx':[
  {titles:'$6:$6'},{titles:'$6:$6'},{titles:'$6:$6'},{titles:'$18:$18',breaks:[17]}],
 '51_Auslagen_und_Liquiditaetsplanung.xlsx':[
  {titles:'$6:$6'},{titles:'$6:$6'},{titles:'$6:$6'}],
 '52_Mehrheiten_und_Bezugsrechte.xlsx':[
  {titles:'$2:$5',breaks:[22]},{titles:'$13:$13'},{titles:'$21:$21',breaks:[20]}]
};

function capTable(){
 const w=book(['Cap Table','Runden','Virtueller Pool','Eingaben']);
 const inp=base(w,'Eingaben',[18,300,145,150,170,190,190,100],40,'Schnittflug: Eingaben zur Beteiligung');
 inp.getRange('B6:D6').values=[['Gründerin oder Gründer','Nominal geplant (EUR)','Person-ID']];header(inp,'B6:D6');
 fall.founders.forEach((f,i)=>{const r=i+7;put(inp,`B${r}`,f.name);put(inp,`C${r}`,f.nominal_eur);put(inp,`D${r}`,f.id);});input(inp,'C7:C13',NOM);
 put(inp,'B15','Summe Gründung');fx(inp,'C15','=SUM(C7:C13)');total(inp,'B15:D15');numeric(inp,'C15',NOM);
 inp.getRange('B18:F18').values=[['Planungsrunde','Neue Nominale (EUR)','Zufluss (EUR)','Pre-Money laut Gespräch','Post-Money laut Gespräch']];header(inp,'B18:F18');
 fall.funding_scenarios.slice(1).forEach((f,i)=>{const r=19+i;put(inp,`B${r}`,['Seed','Serie A','Serie B'][i]);put(inp,`C${r}`,f.nominal_new_eur);put(inp,`D${r}`,f.investment_cash_eur);put(inp,`E${r}`,f.pre_money_eur);put(inp,`F${r}`,f.post_money_eur);});input(inp,'C19:F21',NOM);
 inp.dataValidations.add({range:'C7:C13',rule:{type:'whole',operator:'between',formula1:1,formula2:1000000}});
 inp.dataValidations.add({range:'C19:C21',rule:{type:'whole',operator:'between',formula1:1,formula2:1000000}});
 put(inp,'B24','Virtueller Anteil nach Pool');put(inp,'C24',fall.option_pool.post_pool_fd_percent/100);input(inp,'C24',PCT);
 note(inp,27,'Quelle: Gründerabstimmung und Investorengespräche, Stand 28.09.2026. Sämtliche Zahlen sind unbeschlossene Verhandlungsstände.','G',38);
 note(inp,29,'Blaue Werte auf gelbem Grund sind Eingaben. Echte Geschäftsanteile werden nur in vollen EUR geplant. Virtuelle Einheiten sind keine Geschäftsanteile.','G',42);
 note(inp,31,'Der Nominalwert ist vom wirtschaftlichen Preis zu trennen. Ein späterer Bezugsrechtsausgleich, Anti-Dilution oder Optionsausübung ist hier nicht eingerechnet.','G',42);

 const c=base(w,'Cap Table',[18,390,135,135,135,135,125,125,125,125],34,'Schnittflug: Cap Table vor Beurkundung');
 c.getRange('B6:J6').values=[['Beteiligte','Gründung EUR','Nach Seed EUR','Nach A EUR','Nach B EUR','Gründung %','Nach Seed %','Nach A %','Nach B %']];header(c,'B6:J6');
 const names=[...fall.founders.map(f=>f.name),...fall.funding_scenarios.slice(1).map(f=>f.investor)];
 names.forEach((n,i)=>{const r=i+7;put(c,`B${r}`,n);if(i<7)fx(c,`C${r}`,`='Eingaben'!C${r}`);else put(c,`C${r}`,0);
  fx(c,`D${r}`,i===7?`=C${r}+'Eingaben'!C19`:`=C${r}`);fx(c,`E${r}`,i===8?`=D${r}+'Eingaben'!C20`:`=D${r}`);fx(c,`F${r}`,i===9?`=E${r}+'Eingaben'!C21`:`=E${r}`);
  ['C','D','E','F'].forEach((sc,j)=>fx(c,`${col(6+j)}${r}`,`=${sc}${r}/${sc}$18`));
 });
 put(c,'B18','Gesamt');for(const cc of ['C','D','E','F','G','H','I','J'])fx(c,`${cc}18`,`=SUM(${cc}7:${cc}16)`);total(c,'B18:J18');numeric(c,'C7:F18',NOM);numeric(c,'G7:J18',PCT);
 c.getRange('B7:B16').format.wrapText=true;c.getRange('B7:J16').format.rowHeight=40;
 note(c,21,'Die Spalten sind eine aufeinander aufbauende Planungsfolge. Kein Registerstand, keine Einzahlung und keine Kapitalerhöhung sind damit nachgewiesen.','J',36);
 note(c,23,'Alle neuen Nominalbeträge gehen hier an den jeweiligen Investor. Bezugsrechte der Altgesellschafter und etwaige Kompensation bleiben im Verhandlungsmodell gesondert.','J',36);
 note(c,25,'Virtuelle Vergütung wird ausschließlich im Blatt „Virtueller Pool“ dargestellt. Sie verändert in diesem Modell weder Stammkapital noch Stimmrechte.','J',36);
 note(c,27,'Die frühe Notiz „21 % bleiben 21 %“ ist in dieser Fassung nicht als Zusage berücksichtigt. Dafür wäre eine gesonderte, finanzierbare Vereinbarung erforderlich.','J',36);
 c.freezePanes.freezeRows(6);c.freezePanes.freezeColumns(2);

 const r=base(w,'Runden',[18,390,175,175,175,150,150,100],33,'Schnittflug: Preis und Kapitalaufbringung');
 r.getRange('B6:E6').values=[['Kennzahl','Seed','Serie A','Serie B']];header(r,'B6:E6');
 const labels={7:'Bisheriges Stammkapital (EUR)',8:'Neue Nominale (EUR)',9:'Stammkapital nach Runde (EUR)',11:'Geplanter Zufluss (EUR)',12:'Preis je 1 EUR Nominal (EUR)',13:'Nominalteil (EUR)',14:'Agio gesamt (EUR)',16:'Pre-Money berechnet (EUR)',17:'Post-Money berechnet (EUR)',19:'Neuer Investor: nominaler Anteil',20:'Neuer Investor: Zufluss / Post-Money',22:'Pre-Money laut Gespräch (EUR)',23:'Post-Money laut Gespräch (EUR)',25:'Differenz Pre-Money (EUR)',26:'Differenz Post-Money (EUR)',27:'Differenz Investoranteil'};
 Object.entries(labels).forEach(([rr,t])=>put(r,`B${rr}`,t));
 ['C','D','E'].forEach((cc,i)=>{const ir=19+i;fx(r,`${cc}7`,i===0?"='Eingaben'!C15":`=${col(1+i)}9`);fx(r,`${cc}8`,`='Eingaben'!C${ir}`);fx(r,`${cc}9`,`=SUM(${cc}7:${cc}8)`);fx(r,`${cc}11`,`='Eingaben'!D${ir}`);fx(r,`${cc}12`,`=${cc}11/${cc}8`);fx(r,`${cc}13`,`=${cc}8`);fx(r,`${cc}14`,`=${cc}11-${cc}13`);fx(r,`${cc}16`,`=${cc}7*${cc}12`);fx(r,`${cc}17`,`=SUM(${cc}16,${cc}11)`);fx(r,`${cc}19`,`=${cc}8/${cc}9`);fx(r,`${cc}20`,`=${cc}11/${cc}17`);fx(r,`${cc}22`,`='Eingaben'!E${ir}`);fx(r,`${cc}23`,`='Eingaben'!F${ir}`);fx(r,`${cc}25`,`=${cc}16-${cc}22`);fx(r,`${cc}26`,`=${cc}17-${cc}23`);fx(r,`${cc}27`,`=${cc}19-${cc}20`);});numeric(r,'C7:E26');numeric(r,'C19:E20',PCT);numeric(r,'C27:E27','0.000000%');
 for(const row of [9,14,17])total(r,`B${row}:E${row}`);
 r.getRange('C25:E26').setNumberFormat('0.00');r.getRange('C25:E27').conditionalFormats.add('cellIs',{operator:'notEqual',formula:0,format:{fill:'#FBE3E3',font:{color:C.red,bold:true}}});
 note(r,30,'Serie B setzt 90 EUR je 1 EUR Nominal an, gegenüber 240 EUR in Serie A. Liquidationspräferenzen und wirtschaftlicher Verwässerungsschutz sind nicht modelliert.','G',38);

 const v=base(w,'Virtueller Pool',[18,330,185,185,185,185,90],29,'Schnittflug: virtueller Pool');
 v.getRange('B6:F6').values=[['Rechengröße','Gründung','Nach Seed','Nach Serie A','Nach Serie B']];header(v,'B6:F6');
 const vl={7:'Echte Nominale (EUR)',8:'Poolziel nach virtueller Erweiterung',10:'Virtuelle Recheneinheiten, ungerundet',11:'Recheneinheiten gesamt, ungerundet',12:'Poolquote rechnerisch',14:'Gründerteam vor virtuellem Pool',15:'Gründerteam wirtschaftlich nach Pool',17:'Ottilie vor virtuellem Pool',18:'Ottilie wirtschaftlich nach Pool',20:'Zusätzliche Stimmrechte durch VSOP'};
 Object.entries(vl).forEach(([rr,t])=>put(v,`B${rr}`,t));
 ['C','D','E','F'].forEach((cc,i)=>{fx(v,`${cc}7`,`='Cap Table'!${cc}18`);fx(v,`${cc}8`,"='Eingaben'!C24");fx(v,`${cc}10`,`=${cc}7*${cc}8/(1-${cc}8)`);fx(v,`${cc}11`,`=SUM(${cc}7,${cc}10)`);fx(v,`${cc}12`,`=${cc}10/${cc}11`);fx(v,`${cc}14`,`=SUM('Cap Table'!${cc}7:${cc}13)/${cc}7`);fx(v,`${cc}15`,`=SUM('Cap Table'!${cc}7:${cc}13)/${cc}11`);fx(v,`${cc}17`,`='Cap Table'!${cc}7/${cc}7`);fx(v,`${cc}18`,`='Cap Table'!${cc}7/${cc}11`);put(v,`${cc}20`,0);});numeric(v,'C7:F20',NOM);for(const rr of [8,12,14,15,17,18])numeric(v,`C${rr}:F${rr}`,PCT);numeric(v,'C10:F11','#,##0.0000');
 note(v,23,'10 % „fully diluted“ bedeutet hier: zehn Prozent an der virtuellen Gesamtrechengröße nach Einrichtung des Pools. Die dafür nötigen Einheiten werden nicht auf echte Geschäftsanteile gerundet.','F',46);
 note(v,25,'Reine wirtschaftliche Modellrechnung. Es gibt bisher keine VSOP-Zusage, keine Zuteilung, keinen Ausübungsfall und keine zusätzlichen Stimmen. Auszahlungsbedingungen bleiben offen.','F',46);
 return {w,filename:'50_CapTable_Gruendung_und_Finanzierungsoptionen.xlsx',views:[['Cap Table','B2:J27'],['Runden','B2:G30'],['Virtueller Pool','B2:F25'],['Eingaben','B2:G31']],checks(){near(val(c,'C18'),25000,'Gründung');near(val(c,'F18'),60000,'Nach B');near(val(c,'G7'),.21,'Ottilie21');near(val(c,'J7'),.0875,'OttilieB');near(val(r,'E12'),90,'BPreis');near(val(v,'F12'),.1,'PoolFD');const old=val(inp,'C19');put(inp,'C19',6000);w.recalculate();near(val(c,'D18'),31000,'Seedänderung');near(val(r,'C16'),2500000,'Neuberechneter PreMoney');put(inp,'C19',old);put(inp,'C24',0);w.recalculate();near(val(v,'C10'),0,'PoolNull');put(inp,'C24',.1);w.recalculate();}};
}

function liquidity(){
 const w=book(['Liquidität','Auslagen','Annahmen']);
 const a=base(w,'Auslagen',[18,115,105,240,180,125,125,125,155,130,145,290],43,'Schnittflug: private Auslagen', 'Stand 28.09.2026. Privatbelege vor Beurkundung. Keine Gesellschaftszahlungen.');
 a.getRange('B6:L6').values=[['Beleg-ID','Datum','Lieferant','Empfänger / Person','Netto EUR','USt. EUR','Brutto EUR','Privatfluss EUR','Bezahlt am','Status','Datei']];header(a,'B6:L6');
 data.receipts.forEach((x,i)=>{const r=i+7;put(a,`B${r}`,x.id);put(a,`C${r}`,new Date(`${x.date}T00:00:00Z`));put(a,`D${r}`,x.supplier);put(a,`E${r}`,x.recipient);put(a,`F${r}`,x.net_cents/100);put(a,`G${r}`,x.vat_cents/100);fx(a,`H${r}`,`=SUM(F${r}:G${r})`);fx(a,`I${r}`,x.paid_date?`=H${r}`:'=0');put(a,`J${r}`,x.paid_date?new Date(`${x.paid_date}T00:00:00Z`):null);put(a,`K${r}`,x.status);put(a,`L${r}`,x.filename);});input(a,'F7:G19',EUR);numeric(a,'H7:I19');a.getRange('C7:C19').setNumberFormat('dd"."mm"."yyyy');a.getRange('J7:J19').setNumberFormat('dd"."mm"."yyyy');a.getRange('B7:L19').format.wrapText=true;a.getRange('B7:L19').format.rowHeight=48;
 put(a,'B21','Gesamt');['F','G','H','I'].forEach(cc=>fx(a,`${cc}21`,`=SUM(${cc}7:${cc}19)`));total(a,'B21:L21');numeric(a,'F21:I21');
 put(a,'B24','Noch unbezahlt (EUR)');fx(a,'F24','=H21-I21');put(a,'B25','Erstattungen durch Gesellschaft (EUR)');put(a,'F25',0);input(a,'F25',EUR);put(a,'B26','Privat finanziert, noch nicht erstattet (EUR)');fx(a,'F26','=I21-F25');numeric(a,'F24:F26');
 note(a,29,'Alle zwölf Rechnungen nennen natürliche Personen. Die Gutschrift SF-A011 mindert Alois’ Auslage. Eine Kostenübernahme durch die künftige Gesellschaft ist noch nicht beschlossen.','L',36);
 note(a,31,'Der Steuerbetrag ist der auf dem jeweiligen Beleg ausgewiesene Betrag. Dieser Plan trifft keine Aussage über einen Vorsteuerabzug der späteren Gesellschaft.','L',36);
 note(a,33,'SF-A007 und SF-A010 sind zum Stichtag unbezahlt. Die Auslagen dürfen nicht zugleich als private Forderung und als bereits vom Gesellschaftskonto gezahlter Aufwand erfasst werden.','L',36);
 a.freezePanes.freezeRows(6);a.freezePanes.freezeColumns(2);

 const ass=base(w,'Annahmen',[18,390,145,145,145,145,145,145],46,'Schnittflug: sechs Monate Finanzbedarf');
 ass.getRange('B6:H6').values=[['Auszahlung oder Finanzierung',...data.cash_plan.months.map(x=>new Date(`${x}T00:00:00Z`))]];header(ass,'B6:H6');ass.getRange('C6:H6').setNumberFormat('mmm-yy');
 const rows=[['planned_capital_cents','Stammeinlagen geplant',7],['other_financing_cents','Weitere Finanzierung geplant',8],['premises_cents','Werkraum und Betrieb',10],['prototype_cents','Prüfstand und Bauteile',11],['external_services_cents','Externe Leistungen',12],['software_cents','Software und Rechenzeit',13],['founder_pay_cents','Geschäftsführervergütungen brutto',14],['founder_pay_reserve_cents','Reserve Vergütungsnebenkosten',15],['other_costs_cents','Sonstige Auszahlungen',16],['security_deposit_cents','Kaution Raum, geplant',17]];
 for(const [key,label,row]of rows){put(ass,`B${row}`,label);ass.getRange(`C${row}:H${row}`).values=[data.cash_plan[key].map(x=>x/100)];input(ass,`C${row}:H${row}`,EUR);}
 put(ass,'B18','Private Auslagen: Erstattung je Monat');ass.getRange('C18:H18').values=[data.cash_plan.reimburse_private_percent];input(ass,'C18:H18',PCT);
 put(ass,'B20','Unbezahlte Altbelege im Oktober');fx(ass,'C20',"='Auslagen'!F24");for(const cc of ['D','E','F','G','H'])put(ass,`${cc}20`,0);numeric(ass,'C20:H20');
 put(ass,'B22','Datum der Annahmen');put(ass,'C22',new Date('2026-09-28T00:00:00Z'));ass.getRange('C22').setNumberFormat('dd"."mm"."yyyy');
 data.cash_plan.notes.forEach((text,i)=>note(ass,25+i*3,text,'H',i===6?70:46));

 const l=base(w,'Liquidität',[18,390,145,145,145,145,145,145],38,'Schnittflug: Liquiditätsplan bis März 2027');
 l.getRange('B6:H6').values=[['Geplanter Geldfluss in EUR',...data.cash_plan.months.map(x=>new Date(`${x}T00:00:00Z`))]];header(l,'B6:H6');l.getRange('C6:H6').setNumberFormat('mmm-yy');
 const labs={7:'Anfangsbestand',9:'Stammeinlagen, geplant',10:'Weitere Finanzierung, geplant',11:'Finanzierung gesamt',13:'Werkraum und Betrieb',14:'Prüfstand und Bauteile',15:'Externe Leistungen',16:'Software und Rechenzeit',17:'Geschäftsführervergütungen brutto',18:'Reserve Vergütungsnebenkosten',19:'Sonstige Auszahlungen',20:'Erstattung privater Auslagen, angenommen',21:'Übernahme unbezahlter Altbelege, angenommen',22:'Kaution Raum, geplant',23:'Auszahlungen gesamt',25:'Monatlicher Überschuss / Fehlbetrag',27:'Rechnerischer Endbestand',29:'Nicht gedeckter Finanzbedarf'};
 Object.entries(labs).forEach(([rr,text])=>put(l,`B${rr}`,text));
 ['C','D','E','F','G','H'].forEach((cc,i)=>{if(i===0)put(l,`${cc}7`,0);else fx(l,`${cc}7`,`=${col(1+i)}27`);fx(l,`${cc}9`,`='Annahmen'!${cc}7`);fx(l,`${cc}10`,`='Annahmen'!${cc}8`);fx(l,`${cc}11`,`=SUM(${cc}9:${cc}10)`);for(let rr=13;rr<=19;rr++)fx(l,`${cc}${rr}`,`='Annahmen'!${cc}${rr-3}`);fx(l,`${cc}20`,`='Auslagen'!F26*'Annahmen'!${cc}18`);fx(l,`${cc}21`,`='Annahmen'!${cc}20`);fx(l,`${cc}22`,`='Annahmen'!${cc}17`);fx(l,`${cc}23`,`=SUM(${cc}13:${cc}22)`);fx(l,`${cc}25`,`=${cc}11-${cc}23`);fx(l,`${cc}27`,`=SUM(${cc}7,${cc}25)`);fx(l,`${cc}29`,`=MAX(0,-${cc}27)`);});numeric(l,'C7:H29');[11,23,27,29].forEach(rr=>total(l,`B${rr}:H${rr}`));l.getRange('C27:H27').conditionalFormats.add('cellIs',{operator:'lessThan',formula:0,format:{fill:'#FBE3E3',font:{color:C.red,bold:true}}});
 note(l,32,'Negative Endbestände zeigen ungedeckten Bedarf, keinen bewilligten Kontokorrentkredit. Vor Auslösung weiterer Bestellungen ist die Finanzierung zu klären.','H',36);
 note(l,34,'Gründung und Finanzierung sind geplant. Zum 28.09.2026 existiert kein eröffnetes Gesellschaftskonto und keine eingezahlte Stammeinlage.','H',36);
 note(l,36,'Die Reserve zu Geschäftsführerbezügen ist nur ein Budgetposten. Ottilies sozialversicherungsrechtlicher Status und die Vergütungsverträge bleiben gesondert zu klären.','H',36);
 return{w,filename:'51_Auslagen_und_Liquiditaetsplanung.xlsx',views:[['Liquidität','B2:H36'],['Auslagen','B2:L33'],['Annahmen','B2:H43']],checks(){near(val(a,'H21'),sum(data.receipts.map(x=>x.gross_cents))/100,'Belegsumme');near(val(a,'I21'),sum(data.receipts.filter(x=>x.paid_date).map(x=>x.gross_cents))/100,'Privatsumme');const previous=val(l,'H27');put(ass,'H8',100000);w.recalculate();near(val(l,'H27'),previous+100000,'FinanzierungMärz');put(ass,'H8',0);put(ass,'C18',1);w.recalculate();near(val(l,'C20'),val(a,'F26'),'Auslagenerstattung');put(ass,'C18',0);w.recalculate();}};
}

function votes(){
 const w=book(['Abstimmung','Bezugsrechte','Eingaben']);
 const e=base(w,'Eingaben',[18,320,135,240,240,250,240,180],40,'Schnittflug: Rechenannahmen für Beschlüsse');
 e.getRange('B6:C6').values=[['Person','Nominal bei Gründung EUR']];header(e,'B6:C6');fall.founders.forEach((f,i)=>{put(e,`B${i+7}`,f.name);put(e,`C${i+7}`,f.nominal_eur);});input(e,'C7:C13',NOM);put(e,'B15','Summe Stammkapital');fx(e,'C15','=SUM(C7:C13)');numeric(e,'C15',NOM);total(e,'B15:C15');
 put(e,'B18','Qualifizierte Quote');put(e,'C18',.75);input(e,'C18',PCT);
 e.getRange('B21:G21').values=[['Person','Fall 1','Fall 2','Fall 3','Fall 4','Fall 5']];header(e,'B21:G21');fall.founders.forEach((f,i)=>{put(e,`B${i+22}`,f.name);for(let j=0;j<5;j++)put(e,`${col(j+2)}${i+22}`,data.voting_cases[j].votes[i]);});e.getRange('C22:G28').dataValidation={rule:{type:'list',values:['Ja','Nein','Enthaltung','Abwesend']}};input(e,'C22:G28');
 note(e,31,'1: Alle stimmen, Ottilie dagegen. 2: Eberhard abwesend. 3: Eberhard enthält sich. 4: Alois abwesend, Ottilie dagegen. 5: Keine gültige Stimme.','G',44);
 note(e,34,'Der Gründerkreis hat sich noch nicht auf die Beschlussordnung geeinigt. Stimmverbote, Vollmachten und Beschlussfähigkeit sind nicht in Zahlen übersetzt.','G',44);
 note(e,37,'Stand: Ottilies Liste vom 28.09.2026. Das Budgetveto über 50.000 EUR steht bisher nur im Entwurf der Gesellschaftervereinbarung.','G',36);

 const a=base(w,'Abstimmung',[18,330,150,170,160,160,150,160],39,'Schnittflug: 75 % und die Bezugsgröße');
 put(a,'B5','Abstimmungsfall (1 bis 5)');put(a,'C5',1);input(a,'C5',NOM);a.dataValidations.add({range:'C5',rule:{type:'whole',operator:'between',formula1:1,formula2:5}});
 a.getRange('B7:E7').values=[['Person','Nominal EUR','Stimme','Ja-Nominal EUR']];header(a,'B7:E7');
 fall.founders.forEach((f,i)=>{const rr=i+8;fx(a,`B${rr}`,`='Eingaben'!B${i+7}`);fx(a,`C${rr}`,`='Eingaben'!C${i+7}`);fx(a,`D${rr}`,`=INDEX('Eingaben'!$C$22:$G$28,${i+1},$C$5)`);fx(a,`E${rr}`,`=IF(D${rr}="Ja",C${rr},0)`);});numeric(a,'C8:C14',NOM);numeric(a,'E8:E14',NOM);a.getRange('D8:D14').format.horizontalAlignment='center';
 put(a,'B17','Ja-Stimmen (Nominal EUR)');fx(a,'C17','=SUM(E8:E14)');put(a,'B18','Nein-Stimmen (Nominal EUR)');fx(a,'C18','=SUMIFS(C8:C14,D8:D14,"Nein")');put(a,'B19','Gültig abgegebene Stimmen (EUR)');fx(a,'C19','=SUM(C17:C18)');put(a,'B20','Stimmberechtigtes Kapital (EUR)');fx(a,'C20',"='Eingaben'!C15");numeric(a,'C17:C20',NOM);total(a,'B19:E19');
 a.getRange('B23:D23').values=[['Rechenregel','Abgegebene Stimmen','Gesamtes Kapital']];header(a,'B23:D23');
 put(a,'B24','Ja-Anteil am jeweiligen Nenner');fx(a,'C24','=IF(C19=0,"n.a.",C17/C19)');fx(a,'D24','=C17/C20');numeric(a,'C24:D24',PCT);
 put(a,'B25','Erforderliche Quote');fx(a,'C25',"='Eingaben'!C18");fx(a,'D25','=C25');numeric(a,'C25:D25',PCT);
 put(a,'B26','Quote rechnerisch erreicht?');fx(a,'C26','=IF(C19=0,"Keine gültige Stimme",IF(C24>=C25,"Ja","Nein"))');fx(a,'D26','=IF(D24>=D25,"Ja","Nein")');a.getRange('C26:D26').format.wrapText=true;a.getRange('B26:E26').format.rowHeight=43;
 put(a,'B29','Ottilies Kapitalanteil bei Gründung');fx(a,'C29',"='Eingaben'!C7/'Eingaben'!C15");numeric(a,'C29',PCT);
 note(a,32,'Die zwei Spalten bilden konkurrierende Entwurfsfassungen ab. Ein rechnerisches „Ja“ ist keine Aussage zur Wirksamkeit eines Beschlusses.','G',40);
 note(a,34,'Das Vertragsveto zu Budgetfragen ist hier nicht als allgemeine Sperrminorität eingerechnet. Die Matrix trifft keine Entscheidung über Ottilies Sozialversicherungspflicht.','G',42);
 note(a,36,'Bei Enthaltung oder Abwesenheit werden keine gültigen Ja- oder Nein-Stimmen abgegeben. Stimmverbote und sonstige Sonderlagen sind vor Anwendung gesondert einzutragen.','G',42);

 const b=base(w,'Bezugsrechte',[18,390,145,185,145,145,155,155,155],39,'Schnittflug: Serie B und Bezugsrechte');
 put(b,'B5','Variante (1 bis 3)');put(b,'C5',2);input(b,'C5',NOM);b.dataValidations.add({range:'C5',rule:{type:'whole',operator:'between',formula1:1,formula2:3}});
 put(b,'B7','Kapital vor Serie B (EUR)');fx(b,'C7',"=SUM('Eingaben'!C7:C13)+C9+C10");put(b,'D7','Neu nominal EUR');put(b,'E7',20000);input(b,'E7',NOM);
 put(b,'B8','Zufluss Serie B (EUR)');put(b,'C8',1800000);input(b,'C8',EUR);put(b,'D8','Preis / EUR nominal');fx(b,'E8','=C8/E7');numeric(b,'E8',EUR);b.getRange('D7:D8').format.horizontalAlignment='center';
 put(b,'B9','Seed-Nominale (EUR)');put(b,'C9',5000);input(b,'C9',NOM);put(b,'B10','Serie-A-Nominale (EUR)');put(b,'C10',10000);input(b,'C10',NOM);numeric(b,'C7',NOM);
 b.getRange('B13:I13').values=[['Person / Investor','Vor B EUR','Rechnerisch pro rata EUR','Gewählte Zeichnung EUR','Rundungsrest EUR','Kapital nach B EUR','Anteil nach B','Zahlung bei Zeichnung EUR']];header(b,'B13:I13');b.getRange('B13:I13').format.rowHeight=55;
 const names=[...fall.founders.map(f=>f.name),fall.funding_scenarios[1].investor,fall.funding_scenarios[2].investor,fall.funding_scenarios[3].investor];
 names.forEach((n,i)=>{const rr=14+i;put(b,`B${rr}`,n);if(i<7)fx(b,`C${rr}`,`='Eingaben'!C${7+i}`);else if(i<9)fx(b,`C${rr}`,`=$C$${i+2}`);else put(b,`C${rr}`,0);
  if(i<9){fx(b,`D${rr}`,`=C${rr}/$C$7*$E$7`);fx(b,`E${rr}`,`=IF($C$5=1,ROUNDDOWN(D${rr},0),IF(AND($C$5=3,${i+1}=1),ROUNDDOWN(D${rr},0),0))`);fx(b,`F${rr}`,`=IF($C$5=1,D${rr}-E${rr},IF(AND($C$5=3,${i+1}=1),D${rr}-E${rr},0))`);}else{put(b,`D${rr}`,0);fx(b,`E${rr}`,'=$E$7-SUM(E14:E22)');put(b,`F${rr}`,0);}
  fx(b,`G${rr}`,`=SUM(C${rr},E${rr})`);fx(b,`H${rr}`,`=G${rr}/($C$7+$E$7)`);fx(b,`I${rr}`,`=E${rr}*$E$8`);
 });
 put(b,'B25','Gesamt');for(const cc of ['C','D','E','F','G','H','I'])fx(b,`${cc}25`,`=SUM(${cc}14:${cc}23)`);total(b,'B25:I25');numeric(b,'C14:G25',NOM);numeric(b,'D14:D25','#,##0.0000');numeric(b,'F14:F25','#,##0.0000');numeric(b,'H14:H25',PCT);numeric(b,'I14:I25',EUR);b.getRange('B14:B23').format.wrapText=true;b.getRange('B14:I23').format.rowHeight=42;
 note(b,28,'1: Alle Altgesellschafter zeichnen pro rata. 2: Nur neuer Investor zeichnet. 3: Nur Ottilie zeichnet pro rata, Investor übernimmt den Rest. Keine der Varianten ist beschlossen.','I',36);
 note(b,30,'Nur ganze EUR werden als Zeichnung angesetzt. Rechnerische Bruchteile sind in Spalte F offen ausgewiesen; der Investor übernimmt im Modell sämtliche nicht gezeichneten EUR.','I',36);
 note(b,32,'Diese Zuteilung ist eine Finanzierungsannahme. Sie ersetzt keine Einigung über Bezugsrechte, Bezugsrechtsausschluss, Bewertung, Fristen oder Rundungszuteilung.','I',36);
 note(b,34,'Der Anteilserhalt erfordert in Variante 1 zusätzliches Geld der Altgesellschafter. Ein gleichbleibender Prozentwert entsteht nicht durch eine bloße Bestandsschutzzusage.','I',36);
 return{w,filename:'52_Mehrheiten_und_Bezugsrechte.xlsx',views:[['Abstimmung','B2:G36'],['Bezugsrechte','B2:I34'],['Eingaben','B2:G37']],checks(){near(val(a,'C24'),.79,'AlleohneOttilie');put(a,'C5',2);w.recalculate();near(val(a,'C24'),57/78,'Abwesenheit');assert.equal(val(a,'C26'),'Nein');put(a,'C5',5);w.recalculate();assert.equal(val(a,'C24'),'n.a.');put(a,'C5',1);near(val(b,'H14'),.0875,'BInvestoronly');put(b,'C5',1);w.recalculate();near(val(b,'E14'),2625,'OttilieproRata');near(val(b,'E23'),0,'KeinInvestorrest');near(val(b,'I25'),1800000,'Zahlungssumme');put(b,'C5',3);w.recalculate();near(val(b,'E23'),17375,'Teilzeichnungsrest');put(b,'E7',20001);w.recalculate();near(val(b,'G25'),60001,'Ganzzahligetest');assert(Number.isInteger(val(b,'E14')));assert(val(b,'F14')>0);put(b,'E7',20000);put(b,'C5',2);w.recalculate();}};
}

assert.equal(sum(fall.founders.map(x=>x.nominal_eur)),25000);
assert(data.receipts.every(x=>Number.isInteger(x.net_cents)&&Number.isInteger(x.vat_cents)&&Number.isInteger(x.gross_cents)));
for(const build of [capTable,liquidity,votes]){
 const pack=build();pack.w.recalculate();pack.checks();pack.w.recalculate();
 const err=await pack.w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},summary:'Formelfehler'});
 await fs.writeFile(path.join(qa,pack.filename+'.errors.ndjson'),err.ndjson);
 const inspections=[];
 for(const [name,range]of pack.views){
  const check=await pack.w.inspect({kind:'table',range:`'${name}'!${range}`,include:'values,formulas',tableMaxRows:50,tableMaxCols:15,maxChars:50000});inspections.push(check.ndjson);
  const preview=await pack.w.render({sheetName:name,range,scale:1.4,format:'png'});
  await fs.writeFile(path.join(qa,`${pack.filename}-${name.replaceAll(' ','_')}.png`),new Uint8Array(await preview.arrayBuffer()));
 }
 await fs.writeFile(path.join(qa,pack.filename+'.inspection.ndjson'),inspections.join('\n'));
 const output=await SpreadsheetFile.exportXlsx(pack.w);await output.save(path.join(qa,pack.filename));
 // Druckeinstellungen sind in dieser Runtime nicht Teil der öffentlichen API.
 // Nur standardisierte OOXML-Druckmetadaten ergänzen, keine Zellen oder Formeln ändern.
 const zip=await JSZip.loadAsync(await fs.readFile(path.join(qa,pack.filename)));
 for(const name of Object.keys(zip.files).filter(x=>/^xl\/worksheets\/sheet\d+\.xml$/.test(x))){
  const sheetIndex=Number(name.match(/sheet(\d+)\.xml$/)[1])-1;
  const layout=printLayout[pack.filename][sheetIndex];
  let text=await zip.file(name).async('string');
  const prefix=text.match(/<((?:\w+:)?)worksheet\b/)[1];
  text=text.replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,'').replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'');
  text=text.replace(`</${prefix}worksheet>`,`<${prefix}pageMargins left="0.25" right="0.25" top="0.35" bottom="0.35" header="0.15" footer="0.15"/><${prefix}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="0"/></${prefix}worksheet>`);
  text=text.replace(/<(?:\w+:)?pageSetUpPr\b[^>]*\/>/g,'');
  if(text.includes(`</${prefix}sheetPr>`)) text=text.replace(`</${prefix}sheetPr>`,`<${prefix}pageSetUpPr fitToPage="1"/></${prefix}sheetPr>`);
  else text=text.replace(new RegExp(`<${prefix}sheetPr\\s*/>`),`<${prefix}sheetPr><${prefix}pageSetUpPr fitToPage="1"/></${prefix}sheetPr>`);
  if(layout.breaks?.length){
   const br=layout.breaks.map(id=>`<${prefix}brk id="${id}" min="0" max="16383" man="1"/>`).join('');
   text=text.replace(`</${prefix}worksheet>`,`<${prefix}rowBreaks count="${layout.breaks.length}" manualBreakCount="${layout.breaks.length}">${br}</${prefix}rowBreaks></${prefix}worksheet>`);
  }
  zip.file(name,text);
 }
 let bookXml=await zip.file('xl/workbook.xml').async('string');
 const prefix=bookXml.match(/<((?:\w+:)?)workbook\b/)[1];
 const printNames=pack.views.map(([name,range],i)=>`<${prefix}definedName name="_xlnm.Print_Area" localSheetId="${i}">'${name}'!${range.replace(/([A-Z]+)(\d+)/g,'$$$1$$$2')}</${prefix}definedName><${prefix}definedName name="_xlnm.Print_Titles" localSheetId="${i}">'${name}'!${printLayout[pack.filename][i].titles}</${prefix}definedName>`).join('');
 bookXml=bookXml.replace(`</${prefix}workbook>`,`<${prefix}definedNames>${printNames}</${prefix}definedNames></${prefix}workbook>`);
 zip.file('xl/workbook.xml',bookXml);
 const final=await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'});await fs.writeFile(path.join(dest,pack.filename),final);
 reports.push({filename:pack.filename,bytes:final.length,sha256:createHash('sha256').update(final).digest('hex'),sheets:pack.views.map(x=>x[0]),formula_error_scan:err.ndjson});
 console.log(`${pack.filename}: erstellt, Eingabenänderungen und Formeln geprüft, ${pack.views.length} Blätter gerendert`);
}
await fs.writeFile(path.join(qa,'manifest.json'),JSON.stringify({created:new Date().toISOString(),source_revision:data.revision,workbooks:reports},null,2)+'\n');

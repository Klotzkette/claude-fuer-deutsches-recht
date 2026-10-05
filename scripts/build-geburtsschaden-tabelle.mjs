/** Reproduzierbare Vergleichs-, Zahlungs- und Modellrechnung des fiktiven Geburtsschadens. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook,SpreadsheetFile,requireRuntime}=await loadWorkbookRuntime(['jszip']);
const JSZip=requireRuntime('jszip');
const [outDir,qaDir]=process.argv.slice(2);if(!outDir||!qaDir)throw Error('Ausgabe und QA angeben');
await fs.mkdir(outDir,{recursive:true});await fs.mkdir(qaDir,{recursive:true});
const wb=Workbook.create(), sheets={};const money='#,##0.00;(#,##0.00);"–"';const checks=[];
for(const name of ['Vergleich','Zahlungen','Ausgleichsmodell','Bedarfsansatz']){
 const s=wb.worksheets.add(name);sheets[name]=s;s.showGridLines=false;
 s.getRange('A1:E30').format={font:{name:'Arial',size:10,color:'#222222'},verticalAlignment:'center',rowHeight:22};
 [38,19,19,3,48].forEach((v,i)=>s.getRangeByIndexes(0,i,30,1).format.columnWidth=v);
 s.getRange('B1:C30').setNumberFormat(money);s.getRange('B1:C30').format.horizontalAlignment='right';
 s.getRange('A1:E1').format.rowHeight=8;s.getRange('A2').format.font={name:'Arial',size:14,bold:true};
 s.getRange('A3:E3').format.borders.bottom={style:'thin',color:'#BBBBBB'};
 s.getRange('A4').values=[['Nora Winter · FK-2016-0214 · Stand 05.10.2026 · EUR']];
 s.getRange('E6:E30').format.font.color='#555555';
}
function set(s,c,v){s.getRange(c).values=[[v]];}
function formula(s,c,v){s.getRange(c).formulas=[[v]];s.getRange(c).format.font.color=v.includes('!')?'#008000':'#222222';}
function head(s,r,a){s.getRange(`A${r}:C${r}`).values=[a];s.getRange(`A${r}:C${r}`).format={fill:'#E7E7E7',font:{name:'Arial',size:10,bold:true},rowHeight:30,wrapText:true,horizontalAlignment:'center'};}
function total(s,r){s.getRange(`A${r}:C${r}`).format={font:{name:'Arial',size:10,bold:true},borders:{top:{style:'thin',color:'#888888'}},rowHeight:28};}
function input(s,c,v){set(s,c,v);s.getRange(c).format={fill:'#FFF4D0',font:{name:'Arial',size:10,color:'#0000FF'}};}
const v=sheets.Vergleich;set(v,'A2','Vergleich und Anrechnung');head(v,6,['Position','Vereinbart','Vorschüsse']);
v.getRange('A7:C11').values=[['Schmerzensgeld',900000,300000],['Vergangener Mehrbedarf',800000,800000],['Künftige Pflege und Assistenz',8500000,0],['Wohn- und Hilfsmittelmehrbedarf',750000,100000],['Künftiger Erwerbsschaden',2250000,0]];
v.getRange('B7:C11').format.font.color='#0000FF';
v.getRange('E7:E11').values=[['11 Teilvergleich, Nummer 1 und 3'],['Bis 30.09.2026; Nummer 1 und 3'],['Ab 01.10.2026; Kapitalbetrag'],['180.000 EUR Umbau darin enthalten'],['Vergleichswert; kein sicherer Berufsweg']];
set(v,'A13','Vereinbart / angerechnet');formula(v,'B13','=SUM(B7:B11)');formula(v,'C13','=SUM(C7:C11)');total(v,13);
set(v,'A15','Verbleibende Schlusszahlung');formula(v,'B15','=B13-C13');set(v,'E15','11 Teilvergleich, Nummer 3');total(v,15);
set(v,'A17','Tatsächlich ausgezahlt');formula(v,'B17',"='Zahlungen'!C13");
set(v,'A18','Differenz zum Vergleich');formula(v,'B18','=B13-B17');v.getRange('B18').setNumberFormat('#,##0.00;(#,##0.00);0.00');
set(v,'A21','Schäden aus dem Vorbehalt sind nicht in diesen Beträgen enthalten.');
set(v,'A23','Die Zuordnung der Vorschüsse folgt dem unterschriebenen Teilvergleich.');
const z=sheets.Zahlungen;set(z,'A2','Ausgeführte Zahlungen');head(z,6,['Valuta','Referenz','Betrag']);
const dates=['2018-06-29','2020-07-31','2022-07-29','2024-07-31','2026-09-29'];
const refs=['Z-180629-41','Z-200731-18','Z-220729-08','Z-240731-22','Z-260929-06'];
const amounts=[300000,250000,350000,300000,12000000];
for(let i=0;i<5;i++){z.getRange(`A${7+i}:C${7+i}`).values=[[new Date(dates[i]+'T00:00:00Z'),refs[i],amounts[i]]];set(z,`E${7+i}`,'18 Kassenabgleich; Empfängerin Nora');}
z.getRange('A7:A11').setNumberFormat('dd.mm.yyyy');z.getRange('C7:C11').format.font.color='#0000FF';
set(z,'A13','Familie insgesamt');formula(z,'C13','=SUM(C7:C11)');total(z,13);
head(z,16,['Valuta','Referenz','Erstattung']);z.getRange('A17:C17').values=[[new Date('2026-10-02T00:00:00Z'),'MOD-261002-WI',8500000]];z.getRange('A17').setNumberFormat('dd.mm.yyyy');set(z,'E17','15 und 18: Eingang bei Frankenbogen');
set(z,'A19','Bisheriger Nettoabfluss');formula(z,'C19','=C13-C17');total(z,19);set(z,'E19','Liquidität; keine endgültige Risikotragung');
set(z,'A22','Keine Zahlung von Ausgleich oder Rückversicherung an die Familie.');
set(z,'A24','Vorschüsse sind in 13,20 Mio. EUR enthalten; Reserve ist keine Zahlung.');
const a=sheets.Ausgleichsmodell;set(a,'A2','Interne Schichtenrechnung');set(a,'A4','Nur Modellannahmen aus 14 · keine tatsächlichen AKHA-Bedingungen');
head(a,6,['Parameter / Rechnung','Betrag','Status']);
input(a,'B7',1500000);set(a,'A7','Mitgliedsselbstbehalt');set(a,'E7','14 Nummer 2; trägt Frankenbogen');
input(a,'B8',10000000);set(a,'A8','Rückversicherungspriorität');set(a,'E8','Bezugsgröße: ursprünglicher Gesamtschaden');
input(a,'B9',10000000);set(a,'A9','Rückversicherungslimit');set(a,'E9','Weitere Schicht oberhalb der Priorität');
set(a,'A11','Anrechenbarer Gesamtschaden');formula(a,'B11',"='Vergleich'!B13");
set(a,'A12','Frankenbogen trägt endgültig');formula(a,'B12','=MIN(B11,B7)');
set(a,'A13','Bruttoforderung an Ausgleich');formula(a,'B13','=MAX(0,B11-B12)');set(a,'C13','angemeldet');
set(a,'A14','Davon obere Rückdeckung');formula(a,'B14','=MIN(MAX(0,B11-B8),B9)');set(a,'C14','ungeprüft');
set(a,'A15','Gegenseitiger Ausgleich netto');formula(a,'B15','=B13-B14');total(a,15);
set(a,'A17','Ausgleich bereits erhalten');formula(a,'B17',"='Zahlungen'!C17");set(a,'C17','eingegangen');
set(a,'A18','Ausgleich noch offen');formula(a,'B18','=B13-B17');set(a,'C18','Forderung');
set(a,'A20','Rückdeckung dort eingegangen');input(a,'B20',0);set(a,'C20','kein Eingang');set(a,'E20','15: bei der Ausgleichsebene');
set(a,'A21','Rückdeckung dort offen');formula(a,'B21','=B14-B20');set(a,'C21','angemeldet');
set(a,'A23','Reserve für offene Drittregresse');input(a,'B23',650000);set(a,'E23','16; außerhalb aktueller Abrechnung');
set(a,'A25','Abgleich Schichten / Zahlung');formula(a,'B25','=B12+B14+B15-B11');a.getRange('B25').setNumberFormat('#,##0.00;(#,##0.00);0.00');
set(a,'A27','Offene 3,20 Mio. EUR bestehen auf zwei verschiedenen Abrechnungsebenen.');
set(a,'A28','Die Beträge dürfen weder addiert noch als neue Familienforderung behandelt werden.');
const b=sheets.Bedarfsansatz;set(b,'A2','Grundlagen der Vergleichsbewertung');set(b,'A4','Ausgehandelte Kapitalbeträge · keine individuelle Barwertprognose');head(b,6,['Pflegeansatz jährlich','Eingabe','Berechnung']);
set(b,'A7','Assistenzstunden je Tag');input(b,'B7',10);b.getRange('B7').setNumberFormat('0');
set(b,'A8','Endpreis je Stunde');input(b,'B8',69);set(b,'E8','08 Assistenzangebot');
set(b,'A9','Tage je Jahr');input(b,'B9',365);b.getRange('B9').setNumberFormat('0');
set(b,'A10','Assistenz pro Jahr');formula(b,'C10','=B7*B8*B9');
set(b,'A11','Therapie und Fahrten');input(b,'B11',18000);set(b,'E11','11 Vergleich; elterliche Angaben');
set(b,'A12','Hilfsmittel und Wartung');input(b,'B12',10150);set(b,'E12','Wiederkehrend; kein Umbau doppelt');
set(b,'A13','Bedarf vor Drittleistungen');formula(b,'C13','=C10+B11+B12');
set(b,'A14','Leistungen anderer Träger');input(b,'B14',50000);set(b,'E14','Vereinbarter Ansatz, keine Kassenzusage');
set(b,'A15','Ungedeckter Jahresansatz');formula(b,'C15','=C13-B14');total(b,15);
set(b,'A16','Vereinbartes Pflegekapital');input(b,'B16',8500000);set(b,'E16','11 Vergleich, Nummer 1');
set(b,'A17','Kapital / Jahresansatz');formula(b,'C17','=B16/C15');b.getRange('C17').setNumberFormat('0.00');set(b,'E17','Kontrollquotient; kein Barwertfaktor');
head(b,20,['Erwerbsbewertung','Eingabe','Kapital']);set(b,'A21','Jährlicher Nettoausfall');input(b,'B21',55000);set(b,'E21','09: Annahme, Erwerb von 21 bis 67');
set(b,'A22','Vereinbartes Erwerbskapital');input(b,'B22',2250000);
set(b,'A23','Kapital / Jahresansatz');formula(b,'C23','=B22/B21');b.getRange('C23').setNumberFormat('0.00');set(b,'E23','Kontrollquotient; kein Barwertfaktor');
set(b,'A26','Kapitalbeträge sind frei verhandelt; Quotienten dienen nur der Orientierung.');
set(b,'A27','Keine Sterbetafel und keine gesicherte Prognose zu Lebensdauer oder Beruf.');
for(const [s,c] of [[v,'B18'],[a,'B25']])s.getRange(c).conditionalFormats.add('cellIs',{operator:'notEqual',formula:0,format:{fill:'#FCE4D6',font:{color:'#9C0006',bold:true}}});
for(const s of Object.values(sheets))for(let r=1;r<=30;r++)if(s.getRange(`A${r}:E${r}`).values[0].every(v=>v===null||v===''))s.getRange(`A${r}:E${r}`).format.rowHeight=8;
function check(name,c,want){const got=sheets[name].getRange(c).values[0][0];if(typeof got!=='number'||Math.abs(got-want)>0.001)throw Error(`${name}!${c}: ${got} != ${want}`);checks.push({sheet:name,cell:c,expected:want,actual:got});}
wb.recalculate();check('Vergleich','B13',13200000);check('Vergleich','C13',1200000);check('Vergleich','B15',12000000);check('Vergleich','B18',0);check('Ausgleichsmodell','B13',11700000);check('Ausgleichsmodell','B14',3200000);check('Ausgleichsmodell','B15',8500000);check('Ausgleichsmodell','B18',3200000);check('Bedarfsansatz','C17',8500000/230000);check('Bedarfsansatz','C23',2250000/55000);
// Änderungen prüfen dieselben Formeln, danach ursprüngliche Eingaben wiederherstellen.
input(a,'B8',15000000);wb.recalculate();check('Ausgleichsmodell','B14',0);check('Ausgleichsmodell','B15',11700000);input(a,'B8',10000000);
input(a,'B9',2000000);wb.recalculate();check('Ausgleichsmodell','B14',2000000);check('Ausgleichsmodell','B15',9700000);input(a,'B9',10000000);
input(b,'B7',0);wb.recalculate();check('Bedarfsansatz','C10',0);input(b,'B7',10);b.getRange('B7').setNumberFormat('0');
wb.recalculate();check('Ausgleichsmodell','B14',3200000);check('Bedarfsansatz','C17',8500000/230000);
for(const [name,s] of Object.entries(sheets)){
 for(const row of s.getRange('A1:E30').values)for(const val of row)if(typeof val==='string'&&/^#(?:REF!|DIV\/0!|VALUE!|NAME\?|N\/A|NUM!|NULL!|SPILL!|CALC!)/.test(val))throw Error(val);
 const inspected=await wb.inspect({kind:'table',range:`'${name}'!A1:E30`,include:'values,formulas',tableMaxRows:30,tableMaxCols:5});await fs.writeFile(path.join(qaDir,`${name}-inspect.ndjson`),inspected.ndjson);
 const pic=await wb.render({sheetName:name,range:'A1:E29',scale:1.3,format:'png'});await fs.writeFile(path.join(qaDir,`${name}.png`),new Uint8Array(await pic.arrayBuffer()));
}
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},summary:'final formula error scan'});await fs.writeFile(path.join(qaDir,'errors.ndjson'),errors.ndjson);
const out=path.join(outDir,'12_Zahlung_und_Schichten.xlsx');await(await SpreadsheetFile.exportXlsx(wb)).save(out);
const zip=await JSZip.loadAsync(await fs.readFile(out));for(const n of Object.keys(zip.files).filter(n=>/^xl\/worksheets\/sheet\d+\.xml$/.test(n))){let xml=await zip.file(n).async('string');const p=xml.match(/<(\w+:)?worksheet\b/)[1]??'';if(!/<(?:\w+:)?sheetPr\b/.test(xml))xml=xml.replace(/(<(?:\w+:)?worksheet\b[^>]*>)/,`$1<${p}sheetPr><${p}pageSetUpPr fitToPage="1"/></${p}sheetPr>`);else xml=xml.replace(new RegExp(`</${p}sheetPr>`),`<${p}pageSetUpPr fitToPage="1"/></${p}sheetPr>`);xml=xml.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'').replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,`<${p}pageMargins left="0.25" right="0.25" top="0.3" bottom="0.3" header="0.1" footer="0.1"/>`);xml=xml.replace(new RegExp(`</${p}worksheet>`),`<${p}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="1"/></${p}worksheet>`);zip.file(n,xml);}await fs.writeFile(out,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
await fs.writeFile(path.join(qaDir,'tabellen-pruefung.json'),JSON.stringify({status:'pass',workbooks:1,sheets:4,checks},null,2)+'\n');console.log(out);

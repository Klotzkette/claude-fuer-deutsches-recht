/** Bearbeitbare Rechenbelege zu den KI-Verordnungsfällen, keine automatische Rechtsbewertung. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {loadWorkbookRuntime} from './akten-workbook-runtime.mjs';
const {Workbook,SpreadsheetFile,requireRuntime}=await loadWorkbookRuntime(['jszip']);
const JSZip=requireRuntime('jszip');
const root=path.resolve(process.argv[2]??'.');const qa=process.argv[3]??'/tmp/art5-qa/sheets';await fs.mkdir(qa,{recursive:true});
const cases=JSON.parse(await fs.readFile(path.join(root,'scripts/data/ki-verordnung-artikel5-testakten.json'),'utf8'));
const checks=[];const eur='#,##0.00;(#,##0.00);"-"';
function v(s,a,value){s.getRange(a).values=[[value]];if(typeof value==='number')s.getRange(a).format.font.color='#1D4ED8';}
function f(s,a,formula){s.getRange(a).formulas=[[formula]];s.getRange(a).format.font.color='#111111';}
function h(s,row,labels){s.getRange(`A${row}:D${row}`).values=[labels];s.getRange(`A${row}:D${row}`).format={fill:'#DFE5ED',font:{bold:true},wrapText:true,rowHeight:26,horizontalAlignment:'center'};}
function note(s,row,t){v(s,`A${row}`,t);s.getRange(`A${row}`).format.font.color='#555555';}
function check(wb,s,a,expected,label){wb.recalculate();let actual=s.getRange(a).values[0][0];if(typeof actual==='number'&&typeof expected==='number'?Math.abs(actual-expected)>1e-7:actual!==expected)throw Error(`${label}: ${actual} != ${expected}`);checks.push({case:label,cell:a,actual,expected});}
for(const c of cases){
 const wb=Workbook.create();const s=wb.worksheets.add('Arbeitsstand');s.showGridLines=false;
 s.getRange('A1:D29').format={font:{name:'Arial',size:10,color:'#222222'},verticalAlignment:'center',rowHeight:18};
 [37,23,23,30].forEach((w,i)=>s.getRangeByIndexes(0,i,29,1).format.columnWidth=w);
 s.getRange('A2').format={font:{size:14,bold:true},rowHeight:28};v(s,'A2',c.title);
 note(s,3,'Stand 09.10.2026. Blaue Zahlen sind Eingaben, schwarze Zahlen werden berechnet.');
 if(c.workbook.kind==='kosten'){
  h(s,5,['Position','Betrag EUR','Anzahl','Gesamt EUR']);
  s.getRange('A6:D8').values=[['Einrichtung brutto',149,1,null],['Monatsrate brutto',79,12,null],['Bereits bezahlt',228,1,null]];
  for(let r=6;r<=8;r++)f(s,`D${r}`,`=B${r}*C${r}`);
  v(s,'A10','Vertragssumme brutto');f(s,'D10','=SUM(D6:D7)');
  v(s,'A11','Nach Zahlung rechnerisch offen');f(s,'D11','=D10-D8');
  h(s,14,['Angaben der Kundin','Betrag EUR','Monate','Rechenwert EUR']);
  s.getRange('A15:D17').values=[['Monatliche Rente',1140,1,null],['Monatliche Wohnkosten',680,1,null],['Verbleibend vor anderen Kosten',null,null,null]];
  f(s,'D15','=B15*C15');f(s,'D16','=B16*C16');f(s,'D17','=D15-D16');
  v(s,'A19','Monatsrate / Betrag aus D17');f(s,'D19','=IF(D17=0,"n.a.",B7/D17)');s.getRange('D19').setNumberFormat('0.0%');
  note(s,22,'Quelle Kosten und Zahlung: 01_Pruefauftrag.docx, Abschnitt 2.');
  note(s,23,'Quelle Rente und Wohnen: 03_Gespraech_Riemenschneider.docx; Angaben unbestätigt.');
  note(s,24,'D11 ist eine Rechengröße, keine Feststellung einer durchsetzbaren Forderung.');
  note(s,25,'Andere Lebenshaltungskosten fehlen. D17 ist kein frei verfügbares Einkommen.');
  s.getRange('B6:B17').setNumberFormat(eur);s.getRange('D6:D17').setNumberFormat(eur);
  check(wb,s,'D10',1097,c.slug);check(wb,s,'D11',869,c.slug);check(wb,s,'D17',460,c.slug);
  v(s,'B8',0);check(wb,s,'D11',1097,c.slug+' Nullzahlung');v(s,'B8',228);
  v(s,'B16',1140);check(wb,s,'D19','n.a.',c.slug+' Nullrest');v(s,'B16',680);
 }else if(c.workbook.kind==='schichten'){
  h(s,5,['Beschäftigte Person','Gewünscht','Zugeteilt','Differenz']);
  s.getRange('A6:D9').values=[['Leopold Hummel',8,3,null],['Zora Scheuerlein',8,4,null],['Mika Wipfler',6,6,null],['Brunhilde Krügel',6,5,null]];
  for(let r=6;r<=9;r++)f(s,`D${r}`,`=B${r}-C${r}`);
  v(s,'A11','Summe vier Datensätze');for(const x of ['B','C','D'])f(s,`${x}11`,`=SUM(${x}6:${x}9)`);
  h(s,14,['Person','Engagementanzeige','Zeitraum','Angabe laut Personal']);
  s.getRange('A15:D18').values=[['Leopold Hummel',0.31,'KW 40 und 41','Privattermin in Woche 40'],['Zora Scheuerlein',0.43,'KW 40 und 41','Widerspruch zum Label'],['Mika Wipfler',0.88,'KW 40 und 41','Keine Beschwerde bekannt'],['Brunhilde Krügel',0.79,'KW 40 und 41','Urlaubsgrenze beachtet']];
  s.getRange('B15:B18').setNumberFormat('0%');s.getRange('D15:D18').format={wrapText:true,rowHeight:26};
  note(s,21,'Quelle: 03_Personalnotiz.docx und Datensatzübertragung der Personalleitung.');
  note(s,22,'Die Prozentwerte sind ungeprüfte Systemanzeigen, keine objektiven Emotionen.');
  note(s,23,'Eine Mengendifferenz belegt nicht allein die Ursache einer Schichtentscheidung.');
  note(s,24,'Nur vier Datensätze; keine vollständige Auswertung der Belegschaft.');
  check(wb,s,'D11',10,c.slug);v(s,'C6',8);check(wb,s,'D6',0,c.slug+' volle Zuteilung');check(wb,s,'D11',5,c.slug+' Summe verändert');v(s,'C6',3);
 }else if(c.workbook.kind==='index'){
  h(s,5,['Person','Verspätete Rückgaben','Tonabzug','Index']);
  s.getRange('A6:D9').values=[['Roswitha Scheuerlein',2,25,null],['Berthold Riemenschneider',0,0,null],['Mina Trautwein',1,10,null],['Ottmar Wipfler',0,5,null]];
  v(s,'A12','Startpunkte');v(s,'B12',100);v(s,'A13','Abzug je Rückgabe');v(s,'B13',5);
  for(let r=6;r<=9;r++)f(s,`D${r}`,`=$B$12-B${r}*$B$13-C${r}`);
  v(s,'A16','Scheuerlein ohne Fremddaten');f(s,'D16','=B12');
  v(s,'A17','Rechnerischer Unterschied');f(s,'D17','=D16-D6');
  note(s,20,'Quelle: 02_Datenweg.docx und 06_Auszug.eml; Ausschnitt des Piloten.');
  note(s,21,'Bei diesen vier Personen keine offenen Mieten im Export; andere Fälle fehlen.');
  note(s,22,'Tonabzüge stammen aus ungeprüften Modellklassen, nicht aus Tatsachenfeststellung.');
  note(s,23,'D16 ist eine Vergleichsrechnung, keine empfohlene Vergaberegel.');
  note(s,24,'Ein Index beweist weder Kontextzusammenhang noch tatsächliche Benachteiligung.');
  check(wb,s,'D6',65,c.slug);check(wb,s,'D17',35,c.slug);v(s,'C6',0);check(wb,s,'D6',90,c.slug+' ohne Tonabzug');v(s,'C6',25);
 }else if(c.workbook.kind==='generic'){
  h(s,5,c.workbook.headers);s.getRange('A6:D9').values=c.workbook.rows;
  for(let r=6;r<=9;r++)if(c.workbook.formula)f(s,`D${r}`,c.workbook.formula.replaceAll('{r}',r));
  if((c.workbook.controls??[]).length)h(s,12,['Arbeitsfrage','Eingabe','Einheit','Ergebnis']);
  for(let i=0;i<(c.workbook.controls??[]).length;i++){const z=c.workbook.controls[i];v(s,`A${13+i}`,z[0]);v(s,`B${13+i}`,z[1]);v(s,`C${13+i}`,z[2]);if(z[3])f(s,`D${13+i}`,z[3]);}
  for(let i=0;i<c.workbook.notes.length;i++)note(s,20+i,c.workbook.notes[i]);
  for(const fmt of c.workbook.formats??[])s.getRange(fmt[0]).setNumberFormat(fmt[1]);
  for(const ck of c.workbook.checks??[])check(wb,s,ck[0],ck[1],c.slug);
  for(const z of c.workbook.probes??[]){const old=s.getRange(z[0]).values[0][0];v(s,z[0],z[1]);check(wb,s,z[2],z[3],c.slug+' Probe');v(s,z[0],old);}
 }
 s.getRange('A5:D29').format.wrapText=false;
 const vals=s.getRange('A1:D29').values,forms=s.getRange('A1:D29').formulas;
 for(let r=0;r<vals.length;r++){if(vals[r].every(x=>x===null||x===undefined||x===''))s.getRangeByIndexes(r,0,1,4).format.rowHeight=8;for(let col=0;col<4;col++)if(typeof vals[r][col]==='number'&&!forms[r]?.[col])s.getCell(r,col).format.font.color='#1D4ED8';}
 s.getRange('A5:D5').format.wrapText=true;s.getRange('A5:D5').format.rowHeight=30;
 wb.recalculate();
 const inspect=await wb.inspect({kind:'table',range:'Arbeitsstand!A1:D29',include:'values,formulas',tableMaxRows:30,tableMaxCols:4,maxChars:18000});await fs.writeFile(path.join(qa,c.slug+'.ndjson'),inspect.ndjson);
 const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:50}});await fs.writeFile(path.join(qa,c.slug+'.errors.ndjson'),errors.ndjson);
 for(const row of s.getRange('A1:D29').values)for(const x of row)if(typeof x==='string'&&/^#(REF!|DIV\/0!|VALUE!|NAME\?|N\/A|NUM!|NULL!|SPILL!|CALC!)/.test(x))throw Error(x);
 const preview=await wb.render({sheetName:'Arbeitsstand',range:'A1:D26',scale:1.4,format:'png'});await fs.writeFile(path.join(qa,c.slug+'.png'),new Uint8Array(await preview.arrayBuffer()));
 const dir=path.join(root,'testakten',c.slug);await fs.mkdir(dir,{recursive:true});const out=path.join(dir,c.workbook.file);await(await SpreadsheetFile.exportXlsx(wb)).save(out);
 const zip=await JSZip.loadAsync(await fs.readFile(out));let sx=await zip.file('xl/worksheets/sheet1.xml').async('string');const p=sx.match(/<(\w+:)?worksheet\b/)[1]??'';
 sx=sx.replace(/<(?:\w+:)?pageSetup\b[^>]*\/>/g,'').replace(/<(?:\w+:)?pageMargins\b[^>]*\/>/g,'');sx=sx.replace(`</${p}worksheet>`,`<${p}pageMargins left="0.3" right="0.3" top="0.35" bottom="0.35" header="0.15" footer="0.15"/><${p}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="0"/></${p}worksheet>`);zip.file('xl/worksheets/sheet1.xml',sx);
 let wx=await zip.file('xl/workbook.xml').async('string');const wp=wx.match(/<(\w+:)?workbook\b/)[1]??'';const def=`<${wp}definedName name="_xlnm.Print_Area" localSheetId="0">'Arbeitsstand'!$A$1:$D$26</${wp}definedName>`;if(wx.includes(`</${wp}definedNames>`))wx=wx.replace(`</${wp}definedNames>`,def+`</${wp}definedNames>`);else wx=wx.replace(`</${wp}workbook>`,`<${wp}definedNames>${def}</${wp}definedNames></${wp}workbook>`);zip.file('xl/workbook.xml',wx);await fs.writeFile(out,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
 try{await fs.rename(out+'.inspect.ndjson',path.join(qa,c.slug+'.export.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
 console.log(c.slug);
}
await fs.writeFile(path.join(qa,'checks.json'),JSON.stringify(checks,null,2)+'\n');

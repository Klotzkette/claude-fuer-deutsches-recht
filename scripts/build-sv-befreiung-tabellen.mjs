import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook, SpreadsheetFile} from '@oai/artifact-tool';
import JSZip from 'jszip';
const root=process.argv[2] || path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const out='/tmp/sozialversicherungspflicht-20260930/befreiung-akten/tabellen';
await fs.mkdir(out,{recursive:true});
const proofs=[];
function layout(s,title,last='G20') {
  s.showGridLines=false;
  s.getRange(`A1:${last}`).format.font={name:'Arial',size:11};
  s.getRange(`A1:${last}`).format.rowHeight=25;
  s.getRange(`A1:${last}`).format.verticalAlignment='center';
  s.getRange(`A1:${last}`).format.columnWidth=18;
  s.getRange('A2').values=[[title]];
  s.getRange('A2').format.font={name:'Arial',size:15,bold:true};
  s.getRange('A2:G2').format.rowHeight=29;
}
function header(s,range){s.getRange(range).format={fill:'#31485B',font:{name:'Arial',size:11,color:'#FFFFFF',bold:true},wrapText:true,rowHeight:42,horizontalAlignment:'center'};}
async function printLayout(dest,ranges){
  // Artifact Tool creates the workbook. Only OOXML print settings are added here.
  const zip=await JSZip.loadAsync(await fs.readFile(dest));
  for(let i=0;i<ranges.length;i++){
    const key=`xl/worksheets/sheet${i+1}.xml`;let xml=await zip.file(key).async('string');
    const p=xml.match(/<(\w+:)?worksheet\b/)[1]||'';
    xml=xml.replace(/(<(?:\w+:)?worksheet\b[^>]*>)/,`$1<${p}sheetPr><${p}pageSetUpPr fitToPage="1"/></${p}sheetPr>`);
    xml=xml.replace(`</${p}worksheet>`,`<${p}pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="1"/></${p}worksheet>`);
    zip.file(key,xml);
  }
  let book=await zip.file('xl/workbook.xml').async('string');const p=book.match(/<(\w+:)?workbook\b/)[1]||'';
  const names=ranges.map(([name,range],i)=>`<${p}definedName name="_xlnm.Print_Area" localSheetId="${i}">'${name}'!${range.replace(/([A-Z]+)(\d+)/g,'$$$1$$$2')}</${p}definedName>`).join('');
  book=book.replace(`</${p}workbook>`,`<${p}definedNames>${names}</${p}definedNames><${p}calcPr calcMode="auto" fullCalcOnLoad="1" forceFullCalc="1"/></${p}workbook>`);zip.file('xl/workbook.xml',book);
  await fs.writeFile(dest,await zip.generateAsync({type:'nodebuffer',compression:'DEFLATE'}));
}
async function verifyExport(wb,caseName,filename,ranges,mutations) {
  wb.recalculate();
  const tests=[];
  for(const m of mutations){
    const s=wb.worksheets.getItem(m.sheet);const cell=s.getRange(m.input);const old=cell.values;
    const before=s.getRange(m.output).values[0][0];cell.values=[[m.value]];wb.recalculate();
    const after=s.getRange(m.output).values[0][0];
    if(Math.abs(after-m.expected)>0.001)throw Error(JSON.stringify({m,before,after}));
    cell.values=old;wb.recalculate();const restored=s.getRange(m.output).values[0][0];
    if(restored!==before)throw Error('Wiederherstellung fehlgeschlagen');
    tests.push({...m,before,after,restored});
  }
  wb.recalculate();
  const inspect=[];
  for(const [name,range] of ranges){
    inspect.push((await wb.inspect({kind:'table',range:`'${name}'!${range}`,include:'values,formulas',tableMaxRows:30,tableMaxCols:9})).ndjson);
    const img=await wb.render({sheetName:name,range,scale:1.5,format:'png'});
    await fs.writeFile(path.join(out,`${caseName}-${name}.png`),new Uint8Array(await img.arrayBuffer()));
  }
  const errors=(await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},summary:'Formelfehler'})).ndjson;
  const dest=path.join(root,'testakten',caseName,filename);await(await SpreadsheetFile.exportXlsx(wb)).save(dest);
  await printLayout(dest,ranges);
  await fs.rename(dest+'.inspect.ndjson',path.join(out,caseName+'-'+filename+'.inspect.ndjson')).catch(e=>{if(e.code!=='ENOENT')throw e;});
  proofs.push({file:dest,authoring:'@oai/artifact-tool',mutations:tests,errors,inspect});
}
{
const wb=Workbook.create();const v=wb.worksheets.add('Versorgung');const k=wb.worksheets.add('Kanzlei');
layout(v,'Zahlungsliste Versorgung 2026');v.getRange('A4').values=[['Entgeltstelle Fleetbogen, Stand 25. September 2026']];
v.getRange('A6:G6').values=[['Monat','Brutto EUR','Einbehalt EUR','Zuschuss EUR','Gezahlt EUR','Soll EUR','Differenz EUR']];header(v,'A6:G6');
const months=['Januar','Februar','März','April','Mai','Juni','Juli','August','September'];
v.getRange('A7:E15').values=months.map((m,i)=>[m,i<6?6500:8000,i<6?604.5:744,i<6?604.5:744,i===6?1209:i===7?1767:i<6?1209:1488]);
v.getRange('F7').formulas=[['=SUM(C7:D7)']];v.getRange('F7:F15').fillDown();v.getRange('G7').formulas=[['=E7-F7']];v.getRange('G7:G15').fillDown();
v.getRange('A17').values=[['Summe']];v.getRange('B17:G17').formulas=[['=SUM(B7:B15)','=SUM(C7:C15)','=SUM(D7:D15)','=SUM(E7:E15)','=SUM(F7:F15)','=SUM(G7:G15)']];
v.getRange('B7:G17').setNumberFormat('#,##0.00');v.getRange('B7:E15').format.font.color='#21569B';v.getRange('A19').values=[['Juli: Bankdatei mit altem Betrag. Nachzahlung 279 EUR am 20. August.']];v.getRange('A20').values=[['Grundlage: Entgeltabrechnungen und Beitragskonto; keine rechtliche Neubewertung.']];
layout(k,'Kanzleieinnahmen 2026','F16');k.getRange('A4').values=[['Mila Ahrens, Zahlungseingänge bis 25. September 2026']];
k.getRange('A6:F6').values=[['Zahlungstag','Rechnung','Netto EUR','USt Satz','Brutto EUR','Mandat']];header(k,'A6:F6');k.getRange('F1:F16').format.columnWidth=26;
k.getRange('A7:F10').values=[[new Date('2026-02-11T00:00:00Z'),'MA-26-01',450,.19,null,'Nachbarschaft 01'],[new Date('2026-04-17T00:00:00Z'),'MA-26-03',680,.19,null,'Mietvertrag 02'],[new Date('2026-06-22T00:00:00Z'),'MA-26-04',920,.19,null,'Kaufvertrag 03'],[new Date('2026-09-03T00:00:00Z'),'MA-26-05',1200,.19,null,'Nachbarschaft 04']];
k.getRange('A7:A10').format.horizontalAlignment='left';k.getRange('F7:F10').format.horizontalAlignment='center';
k.getRange('E7').formulas=[['=ROUND(C7*(1+D7),2)']];k.getRange('E7:E10').fillDown();k.getRange('A7:A10').setNumberFormat('yyyy-mm-dd');k.getRange('C7:C12').setNumberFormat('#,##0.00');k.getRange('E7:E12').setNumberFormat('#,##0.00');k.getRange('D7:D10').setNumberFormat('0%');k.getRange('A12').values=[['Summe']];k.getRange('C12').formulas=[['=SUM(C7:C10)']];k.getRange('E12').formulas=[['=SUM(E7:E10)']];k.getRange('A14').values=[['Rechnung MA-26-05 stammt aus Juli; Zahlung ging am 3. September ein.']];k.getRange('A15').values=[['Grundlage: eigener Kanzleikontoauszug; Kosten und weitere Einnahmen fehlen hier.']];
await verifyExport(wb,'sozialversicherung-syndikus-versorgungswerk-hamburg','19_Zahlungen_und_Kanzlei.xlsx',[['Versorgung','A1:G20'],['Kanzlei','A1:F16']],[{sheet:'Versorgung',input:'C13',value:745,output:'G13',expected:-280},{sheet:'Kanzlei',input:'C7',value:500,output:'E7',expected:595}]);
}
{
const wb=Workbook.create();const v=wb.worksheets.add('Verguetungen');const b=wb.worksheets.add('Beratung');
layout(v,'Vergütungsübersicht April bis September','F23');v.getRange('A4').values=[['Elfriede Holle, berichtigte Zusammenstellung vom 24. September 2026']];
v.getRange('A6:F6').values=[['Zeitraum','Gesellschaft','Art','Betrag EUR','Stand','Beleg']];header(v,'A6:F6');v.getRange('B1:C23').format.columnWidth=23;v.getRange('F1:F23').format.columnWidth=27;
v.getRange('A7:F15').values=[['April','Leinefaden','Festvergütung',6200,'bezahlt','Dienstvertrag 20.03.'],['Mai','Leinefaden','Festvergütung',6200,'bezahlt','Entgeltliste'],['Juni','Leinefaden','Festvergütung',6200,'bezahlt','Entgeltliste'],['Juli','Leinefaden','Festvergütung',6200,'bezahlt','Entgeltliste'],['August','Leinefaden','Festvergütung',6200,'bezahlt','Entgeltliste'],['September','Leinefaden','Festvergütung',6200,'bezahlt','Entgeltliste'],['2026','Leinefaden','Bonusreserve',24000,'Budget','Keine Zielvereinbarung'],['April bis Dezember','Havelstrom','Aufsichtsrat',9000,'vorgemerkt','Mitteilung 25.09.'],['Juni','Havelstrom','Reisekosten',68.4,'bezahlt','Erstattung 24.06.']];v.getRange('A7:A15').format.wrapText=true;v.getRange('E7:E15').format.horizontalAlignment='center';v.getRange('A7:F15').format.rowHeight=32;v.getRange('D7:D20').setNumberFormat('#,##0.00');
v.getRange('A18').values=[['Gezahlte Beträge EUR']];v.getRange('D18').formulas=[['=SUMIFS(D7:D15,E7:E15,"bezahlt")']];v.getRange('A19').values=[['Vorgemerkt EUR']];v.getRange('D19').formulas=[['=SUMIFS(D7:D15,E7:E15,"vorgemerkt")']];v.getRange('A20').values=[['Budgetreserve EUR']];v.getRange('D20').formulas=[['=SUMIFS(D7:D15,E7:E15,"Budget")']];v.getRange('A22').values=[['Mohnwinkel wird in der gesonderten Beratungsliste geführt.']];v.getRange('A23').values=[['Beträge sind Vergütungsdaten, keine Feststellung beitragspflichtiger Einnahmen.']];
layout(b,'Beratungstage Mohnwinkel','F21');b.getRange('A4').values=[['Dr. Elif Brandt, Tagesliste mit Septemberstand 29. September 2026']];b.getRange('A6:F6').values=[['Monat','Tage','Tagessatz EUR','Netto EUR','USt EUR','Brutto EUR']];header(b,'A6:F6');
b.getRange('A7:C12').values=[['April',3,900],['Mai',4,900],['Juni',3.5,900],['Juli',0,900],['August',4,900],['September',1.5,900]];
b.getRange('D7').formulas=[['=ROUND(B7*C7,2)']];b.getRange('D7:D12').fillDown();b.getRange('E7').formulas=[['=ROUND(D7*$B$17,2)']];b.getRange('E7:E12').fillDown();b.getRange('F7').formulas=[['=SUM(D7:E7)']];b.getRange('F7:F12').fillDown();b.getRange('A14').values=[['Summe']];b.getRange('B14').formulas=[['=SUM(B7:B12)']];b.getRange('D14:F14').formulas=[['=SUM(D7:D12)','=SUM(E7:E12)','=SUM(F7:F12)']];
b.getRange('A16:B18').values=[['Vereinbarte Tage',16],['Umsatzsteuersatz',.19],['Restliche Tage',null]];b.getRange('B18').formulas=[['=B16-B14']];b.getRange('B7:B14').setNumberFormat('0.0');b.getRange('B17').setNumberFormat('0%');b.getRange('C7:F14').setNumberFormat('#,##0.00');b.getRange('A20').values=[['September ist zur Rechnungsstellung vorbereitet, noch nicht bezahlt.']];b.getRange('A21').values=[['Havelstroms Sitzung vom 15. Juni wurde vor Rechnungsversand entfernt.']];
await verifyExport(wb,'sozialversicherung-ag-organe-hannover','08_Verguetungen_und_Beratung.xlsx',[['Verguetungen','A1:F23'],['Beratung','A1:F21']],[{sheet:'Verguetungen',input:'D7',value:6300,output:'D18',expected:37368.4},{sheet:'Beratung',input:'B11',value:5,output:'B18',expected:-1}]);
}
await fs.writeFile(path.join(out,'artifact-proof.json'),JSON.stringify(proofs,null,2));
console.log(JSON.stringify({workbooks:proofs.length,mutations:proofs.reduce((n,p)=>n+p.mutations.length,0)}));

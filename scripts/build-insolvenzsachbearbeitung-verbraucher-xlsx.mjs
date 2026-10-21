import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const [fixture, root, qa] = process.argv.slice(2);
const [c] = JSON.parse(await fs.readFile(fixture, 'utf8'));
await fs.mkdir(qa, { recursive: true });
const money = '#,##0.00;[Red](#,##0.00);"-"';
const reports = [];
function sheet(wb, name, title, widths, lastRow) {
  const s = wb.worksheets.add(name); s.showGridLines = false;
  const last = String.fromCharCode(64 + widths.length);
  s.getRange(`A1:${last}${lastRow}`).format = { font: { name: 'Times New Roman', size: 11 }, rowHeight: 16, verticalAlignment: 'center' };
  widths.forEach((n, i) => { const a = String.fromCharCode(65 + i); s.getRange(`${a}:${a}`).format.columnWidth = n; });
  s.getRange('A2').format.rowHeight=24;
  s.getRange('A2').values = [[title]]; s.getRange('A2').format.font = { name: 'Times New Roman', size: 15, bold: true };
  return s;
}
function header(s, row, values) {
  const last=String.fromCharCode(64+values.length); s.getRange(`A${row}:${last}${row}`).values=[values];
  s.getRange(`A${row}:${last}${row}`).format={fill:'#293C50',font:{name:'Times New Roman',size:11,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:30,horizontalAlignment:'center'};
}
function input(s,r){s.getRange(r).format.font.color='#0000FF';s.getRange(r).setNumberFormat(money);}
function note(s,r,text){s.getRange(`A${r}`).values=[[text]];s.getRange(`A${r}`).format.font={name:'Times New Roman',size:11,color:'#555555'};}
for (const item of c.files.filter(x=>x.name.endsWith('.xlsx'))) {
  const wb=Workbook.create();let views,driver,target,expected,changed;
  if(item.kind==='household') {
    const s=sheet(wb,'Haushalt','Haushalt Haberlein', [37,20,20,43],38);
    note(s,3,'September 2026. Kontobewegungen und Monatsbedarf getrennt prüfen. EUR.');
    header(s,5,['Position','Einnahmen','Ausgaben','Beleg / Abgrenzung']);
    s.getRange('A6:D8').values=[['Entgelt Fridolin',3120,null,'10_Entgelt_Fridolin.pdf'],['Entgelt Lale',1380,null,'11_Entgelt_Lale.pdf'],['Kindergeld',518,null,'15_Konto_Lale.pdf']];
    s.getRange('A10:D17').values=[['Hausrate',null,1440,'33_Haushaltskonto.pdf'],['Lebensmittel',null,760,'33_Haushaltskonto.pdf'],['Energie und Wasser',null,420,'33_Haushaltskonto.pdf'],['Schule und Verein',null,140,'33_Haushaltskonto.pdf'],['Mobilität Haushaltskonto',null,80,'33_Haushaltskonto.pdf'],['Telefon und Internet',null,79,'33_Haushaltskonto.pdf'],['Hausrat / Haftpflicht',null,95,'14_Konto_Fridolin.pdf'],['Supermarkt / Apotheke Fridolin',null,83.4,'14_Konto_Fridolin.pdf']];
    s.getRange('A20').values=[['Erfasste Beträge']];s.getRange('B20').formulas=[['=SUM(B6:B8)']];s.getRange('C20').formulas=[['=SUM(C10:C17)']];
    s.getRange('A22').values=[['Eingänge abzüglich Abflüsse']];s.getRange('B22').formulas=[['=B20-C20']];
    s.getRange('D22').values=[['Keine freie Rate und kein pfändbarer Betrag']];
    s.getRange('D6:D22').setNumberFormat('  @');input(s,'B6:B8');input(s,'C10:C17');s.getRange('B20:C22').setNumberFormat(money);
    s.getRange('A20:D20').format.borders={top:{style:'thin',color:'#8192A0'}};
    s.getRange('A20:D22').format.font.bold=true;
    const notes=[
      'Blau: veränderbare Belegwerte. Schwarz: berechnete Summen.',
      'Überträge auf das Haushaltskonto sind keine zusätzlichen Einnahmen.',
      'Der Übertrag von 120 EUR gehört zu den internen Kontobewegungen.',
      'September enthält keine Zahlung auf den Kredit K7742 oder E24188.',
      'Gebäudeversicherung, Kleidung, Gesundheit und weitere Kosten sind offen.',
      'Der rechnerische Rest darf deshalb nicht als verfügbare Planrate gelten.',
      'Hausrückstände 4.320 EUR sind keine zweite monatliche Hausrate.',
      'Kaution 2.700 EUR wäre erst bei Anmietung fällig. Noch kein Vertrag.',
      'Die angekündigte Hilfe des Bruders ist entfallen und kein Einkommen.',
      'Lohnpfändung, Kontopfändung und Haushaltsbedarf getrennt berechnen.',
      'Stand der Zusammenstellung: 14.10.2026, Ottilie Gündling.'
    ];notes.forEach((t,i)=>note(s,25+i,t));
    const k=sheet(wb,'Konten','Kontenabgleich September 2026',[32,20,20,20,20],23);
    note(k,3,'Kontrollrechnung aus den drei Auszügen. Interne Überträge nicht konsolidiert.');
    header(k,5,['Konto','Anfang','Eingänge','Abgänge','Ende']);
    k.getRange('A6:D8').values=[['Fridolin 1812',184.3,3120,2798.4],['Lale 7044',-2200,1898,1818],['Gemeinsam 3388',72,4438,2919]];
    for(let r=6;r<=8;r++)k.getRange(`E${r}`).formulas=[[`=B${r}+C${r}-D${r}`]];
    input(k,'B6:D8');k.getRange('E6:E8').setNumberFormat(money);
    note(k,11,'Quellen: 14_Konto_Fridolin.pdf, 15_Konto_Lale.pdf, 33_Haushaltskonto.pdf.');
    note(k,13,'Keine Summierung aller Eingänge: 4.438 EUR sind interne Überträge.');
    note(k,15,'Der negative Endsaldo Lales ist ein Kreditstand, keine Haushaltsausgabe.');
    note(k,17,'Zinsen des dritten Quartals sind am 30.09. noch nicht gebucht.');
    note(k,19,'Guthaben allein belegt weder Verfügungsbefugnis noch Pfändungsschutz.');
    for(const r of [1,4,9,19,21,23,24])s.getRange(`A${r}:D${r}`).format.rowHeight=6;
    views=[['Haushalt','D',36],['Konten','E',20]];driver=[s,'B6'];target=[s,'B22'];expected=1920.6;changed=2020.6;
  } else {
    const s=sheet(wb,'Abgleich','Kreditkonten und persönliche Haftung',[25,18,18,18,18,18],34);
    note(s,3,'Je Kredit-ID einmal erfasst. Beträge aus unterschiedlich alten Belegen. EUR.');
    header(s,5,['Kredit-ID','Kapital','Bekannte Kosten','Erfasst','Fridolin','Lale']);
    s.getRange('A6:C9').values=[['H8831 Haus',258000,0],['K7742 Ratenkredit',11800,0],['E24188 Elektronik',5400,160],['Dispo Lale',2120,0]];
    for(let r=6;r<=9;r++)s.getRange(`D${r}`).formulas=[[`=B${r}+C${r}`]];
    s.getRange('E6:F9').formulas=[['=D6','=D6'],['=D7','=D7'],['=D8','=0'],['=0','=D9']];
    s.getRange('A11').values=[['Summe je Auswertung']];for(const col of ['B','C','D','E','F'])s.getRange(`${col}11`).formulas=[[`=SUM(${col}6:${col}9)`]];
    input(s,'B6:C9');s.getRange('D6:F11').setNumberFormat(money);s.getRange('B11:C11').setNumberFormat(money);
    s.getRange('A11:F11').format.font.bold=true;s.getRange('A11:F11').format.borders={top:{style:'thin',color:'#8192A0'}};
    const notes=[
      'D: wirtschaftliche Konten einmal. E/F: persönliche Haftung je Verfahren.',
      'E und F nicht zur wirtschaftlichen Gesamtbelastung addieren.',
      'Gemeinsame Haftung wird nicht allein wegen der Ehe halbiert.',
      'H8831: Kapitalstand 30.06.2026, Aktualisierung und Ablösesaldo fehlen.',
      'K7742: 19_Gemeinsamer_Kredit.pdf. Zinsen und Kosten nachfordern.',
      'E24188: 18_Elektronik_Finanzierung.pdf und Titel in 13_Pfaendungsbeschluss.pdf.',
      'Die Entwicklung von Kaufpreis 5.000 zu Kapital 5.400 EUR bleibt ungeklärt.',
      'Dispo: 15_Konto_Lale.pdf, Stand 30.09.2026. Q3-Zinsen noch offen.',
      'Null in Kosten bedeutet hier: noch keine gesonderte Kostenposition erfasst.',
      'Null in E/F bedeutet: nach dem vorhandenen Vertrag kein Mitschuldner.',
      'Grundschuld nominal 310.000 EUR nicht zusätzlich als Kredit addieren.',
      'Hausrückstände 4.320 EUR können Kapitalanteile enthalten. Kein Doppelansatz.',
      'Besicherung und Ausfallforderung sind noch nicht abschließend geprüft.',
      'Dies ist keine geprüfte Insolvenztabelle. Eröffnungsstände nachfordern.',
      'Blau: Belegwerte. Schwarz: Formeln. Stand 14.10.2026, Ottilie Gündling.'
    ];notes.forEach((t,i)=>note(s,14+i,t));
    views=[['Abgleich','F',30]];driver=[s,'B8'];target=[s,'D11'];expected=277480;changed=277580;
  }
  wb.recalculate();const before=target[0].getRange(target[1]).values[0][0];
  if(Math.abs(before-expected)>0.001)throw new Error(`Kontrollsumme ${item.name}: ${before} != ${expected}`);
  const old=driver[0].getRange(driver[1]).values[0][0];driver[0].getRange(driver[1]).values=[[old+100]];wb.recalculate();
  const after=target[0].getRange(target[1]).values[0][0];if(Math.abs(after-changed)>0.001)throw new Error('Eingabeänderung ohne richtige Folgewirkung');
  driver[0].getRange(driver[1]).values=[[old]];wb.recalculate();
  const scan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:3000});
  for(const [name,last,row] of views){const image=await wb.render({sheetName:name,range:`A1:${last}${row}`,scale:1.5,format:'png'});await fs.writeFile(path.join(qa,`${item.name}-${name}.png`),new Uint8Array(await image.arrayBuffer()));}
  const out=path.join(root,'testakten',c.slug,item.name);await fs.mkdir(path.dirname(out),{recursive:true});await(await SpreadsheetFile.exportXlsx(wb)).save(out);
  try{await fs.rename(out+'.inspect.ndjson',path.join(qa,item.name+'.inspect.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
  reports.push({file:item.name,before,changed:after,restored:target[0].getRange(target[1]).values[0][0],input_change_test:true,error_scan:scan.ndjson,views});
}
await fs.writeFile(path.join(qa,'xlsx-checks.json'),JSON.stringify(reports,null,2));console.log(JSON.stringify(reports));

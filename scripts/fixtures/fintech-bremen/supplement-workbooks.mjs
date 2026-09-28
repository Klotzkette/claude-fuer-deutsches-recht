import fs from "node:fs/promises";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const input = JSON.parse(await fs.readFile(process.argv[2], "utf8"));
const output = process.argv[3];
const preview = process.argv[4];
const euros = '[$-407]#,##0.00_);[Red](#,##0.00);"-"_)';
const col = (index) => String.fromCharCode(65 + index);
const dt = (value) => new Date(`${value}T00:00:00Z`);
const f = (sheet, cell, formula) => { sheet.getRange(cell).formulas = [[formula]]; };
const v = (sheet, cell, value) => { sheet.getRange(cell).values = [[value]]; };

function setup(sheet, title, subtitle, widths, endRow) {
  sheet.showGridLines = false;
  const last = col(widths.length - 1);
  const range = sheet.getRange(`A1:${last}${endRow}`);
  range.format.font = { name: "Times New Roman", size: 11, color: "#171717" };
  range.format.rowHeight = 19;
  range.format.verticalAlignment = "center";
  widths.forEach((width, i) => {
    sheet.getRange(`${col(i)}1:${col(i)}${endRow}`).format.columnWidthPx = width;
  });
  v(sheet, "A1", title);
  sheet.getRange(`A1:${last}1`).format.rowHeight = 27;
  sheet.getRange("A1").format.font = { name: "Times New Roman", size: 15, bold: true };
  note(sheet, 2, last, subtitle, 26);
  sheet.freezePanes.freezeRows(4);
}

function note(sheet, row, last, text, height = 34) {
  const range = sheet.getRange(`A${row}:${last}${row}`);
  range.merge();
  v(sheet, `A${row}`, text);
  range.format.wrapText = true;
  range.format.rowHeight = height;
  range.format.verticalAlignment = "center";
}

function header(sheet, names, row = 4) {
  const range = sheet.getRange(`A${row}:${col(names.length - 1)}${row}`);
  range.values = [names];
  range.format.fill = "#303937";
  range.format.font = { name: "Times New Roman", size: 11, color: "#FFFFFF", bold: true };
  range.format.wrapText = true;
  range.format.rowHeight = 28;
}

function grid(sheet, range) {
  sheet.getRange(range).format.borders = { insideHorizontal: {style: "thin", color: "#DDDDDD"} };
  sheet.getRange(range).format.wrapText = true;
}

function total(sheet, range) {
  sheet.getRange(range).format.fill = "#E9EFEB";
  sheet.getRange(range).format.font.bold = true;
  sheet.getRange(range).format.rowHeight = 24;
}

function check(sheet, address, expected) {
  const actual = sheet.getRange(address).values[0][0];
  if (actual !== expected) throw new Error(`${sheet.name}!${address}: ${actual} != ${expected}`);
}

async function save(workbook, filename, ranges) {
  workbook.recalculate();
  const errors = await workbook.inspect({kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#N/A", options: {useRegex: true, maxResults: 20}, maxChars: 1500});
  console.log(filename, errors.ndjson);
  const xlsx = await SpreadsheetFile.exportXlsx(workbook);
  await xlsx.save(path.join(output, filename));
  const inspection = path.join(output, filename + ".inspect.ndjson");
  try {
    await fs.rename(inspection, path.join(preview, filename + ".inspect.ndjson"));
  } catch (error) {
    if (error.code !== "ENOENT") throw error;
  }
  for (const [sheetName, range] of ranges) {
    const png = await workbook.render({sheetName, range, scale: 1.4, format: "png"});
    await fs.writeFile(path.join(preview, `${filename}-${sheetName}.png`), new Uint8Array(await png.arrayBuffer()));
  }
}

await fs.mkdir(output, {recursive: true});
await fs.mkdir(preview, {recursive: true});

const service = Workbook.create();
const payments = service.worksheets.add("Zahlungen");
const closing = service.worksheets.add("Abschluss");
const labels = service.worksheets.add("Zuordnung");
setup(payments, "1. Zahlungseingänge Vellio", "Nora Wendt | 13.07.2026 | NF-WP-221014-01 | Datenstand: Abschluss 16.04.2024", [115,126,92,113,124,126,186], 28);
header(payments, ["Buchung", "Referenz B3", "Art", "Zinsen EUR", "Valuta EUR", "Gesamt EUR", "Empfänger"]);
input.payments.forEach((row, i) => {
  const r = i + 5;
  payments.getRange(`A${r}:G${r}`).values = [[dt(row.date), row.ref, row.kind, row.interest, row.principal, null, "Vellio Finance GmbH"]];
  f(payments, `F${r}`, `=D${r}+E${r}`);
});
payments.getRange("A5:A23").setNumberFormat('dd.mm.yyyy"  "');
payments.getRange("A5:G23").format.rowHeight = 16;
payments.getRange("D5:F25").setNumberFormat(euros);
payments.getRange("D5:E23").format.font.color = "#245C3F";
grid(payments, "A5:G23");
v(payments, "A25", "Summe");
for (const c of ["D", "E", "F"]) f(payments, `${c}25`, `=SUM(${c}5:${c}23)`);
total(payments, "A25:G25");
note(payments, 27, "G", "Grundlage: Zahlungsjournal B3 und Zahlungsbelege K4. Positive Beträge sind Eingänge bei Vellio; im Geschäftskonto der Darlehensnehmerin stehen dieselben Zahlungen mit negativem Vorzeichen.");
note(payments, 28, "G", "Die April-Zinsrate und die Endtilgung sind zwei Aufträge am selben Tag. Keine zusätzliche neunzehnte Zinsrate; der Erwerbspreis vom 14.10.2022 gehört nicht in diese Summe.");

setup(closing, "2. Abschluss und Teilbeträge", "Vellio Finance GmbH | Nora Wendt | Zusammenstellung 13.07.2026 | EUR", [450,155,260], 24);
header(closing, ["Position", "Betrag EUR", "Beleg / Zuordnung"]);
const summary = [
  ["18 Zinsraten", null, "Zahlungen, Spalte D"],
  ["Endtilgung 15.04.2024", null, "Zahlungen, Spalte E"],
  ["Gesamte Schuldnerzahlungen", null, "Enthält die unten genannten Teilbeträge"],
  ["Letzte drei Zinsraten", null, "15.02., 15.03. und 15.04.2024"],
  ["Letzte drei Zinsraten zuzüglich Valuta", null, "Teilbetrag, nicht zusätzliche Zahlung"],
  ["Zahlungen am 15.04.2024", null, "Zinsrate und Endtilgung"],
  ["Übernommene Darlehensvaluta 14.10.2022", 500000, "B1 / B3, Eröffnung VF-WP-01"],
  ["Offene Valuta nach Endtilgung", null, "Keine laufenden Zinsen auf Restvaluta"],
  ["Erwerbspreis Vellio an Nexora 14.10.2022", 500000, "B4; 12:31 Uhr; außerhalb Journal"],
];
closing.getRange("A5:C13").values = summary;
for (const [r, formula] of [[5,"=Zahlungen!D25"],[6,"=Zahlungen!E25"],[7,"=SUM(B5:B6)"],[8,"=SUM(Zahlungen!D20:D22)"],[9,"=B8+B6"],[10,"=SUM(Zahlungen!F22:F23)"],[12,"=B11-B6"]]) f(closing, `B${r}`, formula);
closing.getRange("B5:B13").setNumberFormat(euros);
grid(closing, "A5:C13");
closing.getRange("A5:C13").format.rowHeight = 27;
total(closing, "A7:C7");
total(closing, "A9:C9");
note(closing, 15, "C", "14.10.2022, 10:11 Uhr: Auszahlung Nexora an Weserfunken. 12:30 Uhr: Vollzug der Vertragsübernahme. 12:31 Uhr: gesonderter Kaufpreisausgleich Vellio an Nexora.");
note(closing, 17, "C", "Der Erwerbspreis ist eine eigene Zahlung von Vellio und mindert die Schuldner-Valuta nicht. Die Kaufpreisposition ist keine zweite Darlehensauszahlung und kein Teil der 590.000,00 EUR.");
note(closing, 19, "C", "Der Abschlussabgleich enthält keine Feststellung über sämtliche konzerninternen Vergütungen. Die fehlende gesonderte Schuldnergebühr beantwortet diese andere Frage nicht.");
note(closing, 21, "C", "Bearbeitung: Nora Wendt, Vellio Finance GmbH. Zugrunde gelegt wurden B2 bis B4 und die einzelnen Zahlungsdaten. Diese Arbeitsmappe ersetzt weder Kontoauszüge noch den Übernahmevertrag.");

setup(labels, "3. Bezeichnung und Zahlungsrolle", "Vellio Finance GmbH | Abstimmung zum Einzelkredit NF-WP-221014-01 | 13.07.2026", [202,305,358], 22);
header(labels, ["Feld / Vorgang", "Erfasste Angabe", "Abgleich / Herkunft"]);
const mapping = [
  ["Ursprüngliche Kreditgeberin", "Nexora Frontbank AG", "Angebot und Auszahlung, 11. bis 14.10.2022"],
  ["Übernommene Vertragsposition", "Vellio Finance GmbH", "Vollzug 14.10.2022, 12:30 Uhr; B1 / K8"],
  ["Historische Bezeichnung", "Nexora in älteren Buchhaltungsübersichten", "Kröger 12.03.2024; Wendt 14.03.2024"],
  ["Empfänger der Folgeraten", "Vellio Finance GmbH", "Zahlungsstamm bestätigt am 14.10.2022; B2"],
  ["Empfängerkonto", "AT61 1904 3002 3457 3201", "Keine Umstellung auf ein Nexora-Konto"],
  ["Unverändertes Kennzeichen", "NF-WP-221014-01", "Kennzeichen bezeichnet den Kredit, nicht den Kontoinhaber"],
  ["Erwerbspreisempfängerin", "Nexora Frontbank AG", "Einmaliger Kaufpreis; kein Schuldner-Zahlungsauftrag"],
  ["Änderungsanfragen", "An Vellio zu richten", "Anfrage ersetzt keine vereinbarte Stundung oder Verlängerung"],
];
labels.getRange("A5:C12").values = mapping;
grid(labels, "A5:C12");
labels.getRange("A5:C12").format.rowHeight = 30;
note(labels, 14, "C", "In den Zahlungsfeldern ist Vellio als Empfängerin erfasst. Eine zusätzliche Gläubigerrolle von Nexora lässt sich nicht allein aus einer unveränderten Altbezeichnung ablesen. Dies ist die Buchungszuordnung von Vellio, keine Entscheidung über streitige Ansprüche.", 43);
note(labels, 16, "C", "Die behauptete Inkassofunktion wird von den Beteiligten unterschiedlich bewertet. Historische Textfelder bleiben unverändert; eine spätere Erläuterung wird daneben abgelegt und nicht als ursprünglicher Buchungsinhalt ausgegeben.", 40);
note(labels, 18, "C", "Reichweite: dieser Kredit und die bezeichneten Belege. Die Tabelle weist keine vollständigen fremden Konten, keine allgemeine Konzernprüfung und keinen Verzicht auf eigenständige Ansprüche aus früherem Verhalten aus.", 40);
for (const row of [13,15,17]) labels.getRange(`A${row}:C${row}`).format.rowHeight = 8;
service.recalculate();
check(payments, "F25", 590000); check(closing, "B9", 515000); check(closing, "B12", 0);
v(payments, "D5", 5001); service.recalculate(); check(payments, "F25", 590001); check(closing, "B7", 590001);
v(payments, "D5", 5000); service.recalculate(); check(payments, "F25", 590000);
await save(service, "42_Zahlungszuordnung_20260713.xlsx", [["Zahlungen","A1:G28"],["Abschluss","A1:C21"],["Zuordnung","A1:C18"]]);

const bank = Workbook.create();
const march = bank.worksheets.add("Maerz");
const april = bank.worksheets.add("April");
const op = bank.worksheets.add("OffenePosten");
const balances = bank.worksheets.add("Stichtage");
const may = bank.worksheets.add("MaiAbgrenzung");
for (const [sheet, month, opening] of [[march,"2024-03",421800],[april,"2024-04",431000]]) {
  const rows = input.bank.filter(row => row.date.startsWith(month));
  setup(sheet, `1.${month === "2024-03" ? "1" : "2"}. Kontobuchungen ${month === "2024-03" ? "März" : "April"} 2024`, "Weserfunken Präzisionsbau GmbH | Jutta Kröger | Abgleich 11.06.2026 | Konto 01728400", [115,215,280,125,135,135,100], 23);
  v(sheet, "A3", "Vortrag EUR"); v(sheet, "E3", opening); sheet.getRange("E3").setNumberFormat(euros);
  header(sheet, ["Datum", "Gegenkonto / Empfänger", "Verwendungszweck", "Betrag EUR", "Berechnet EUR", "K4-Saldo EUR", "Differenz EUR"]);
  rows.forEach((row, i) => {
    const r = i + 5;
    sheet.getRange(`A${r}:G${r}`).values = [[dt(row.date),row.recipient,row.purpose,row.amount,null,row.balance,null]];
    f(sheet, `E${r}`, `=E${r === 5 ? 3 : r-1}+D${r}`);
    f(sheet, `G${r}`, `=E${r}-F${r}`);
  });
  const last = 4 + rows.length;
  sheet.getRange(`A5:A${last}`).setNumberFormat('dd.mm.yyyy"  "');
  sheet.getRange(`D5:G${last}`).setNumberFormat(euros);
  sheet.getRange(`A5:G${last}`).format.rowHeight = 27;
  sheet.getRange(`D5:D${last}`).format.font.color = "#245C3F";
  sheet.getRange(`F5:F${last}`).format.font.color = "#245C3F";
  grid(sheet, `A5:G${last}`);
  total(sheet, `A${last}:G${last}`);
  note(sheet, last+2, "G", `Quelle: K4 Blatt ${month === "2024-03" ? "17" : "18"}; 30_Buchungsdaten_Geschaeftskonto.csv. Empfänger, Zwecke und Beträge entsprechen dem Export. Die Differenz vergleicht die Fortschreibung mit jeder einzelnen Auszugsbuchung.`, 32);
  note(sheet, last+3, "G", "Keine zusätzlichen Konten oder Kreditlinien erfasst. Der ausgewiesene Saldo ist ein Kontoguthaben, kein vollständiger Status aller fälligen Verpflichtungen. Bearbeitungsvermerk vom 11.06.2026.", 30);
}

setup(op, "2. Ausgewählte offene Lieferantenposten", "Weserfunken Präzisionsbau GmbH | K7, Blätter 2 und 3 | Stand 15.04.2024, 16:30 Uhr", [220,183,123,124,145,220], 23);
header(op, ["Konto / Gläubiger", "Rechnung", "Belegdatum", "Fällig", "Offen brutto EUR", "Beleg"]);
input.op.forEach((row, i) => {
  op.getRange(`A${i+5}:F${i+5}`).values = [[row.creditor,row.invoice,dt(row.date),dt(row.due),row.amount,row.source]];
});
op.getRange("C5:D16").setNumberFormat("dd.mm.yyyy");
op.getRange("E5:E18").setNumberFormat(euros);
op.getRange("A5:F16").format.rowHeight = 24;
grid(op,"A5:F16");
v(op,"A18","Summe der 12 Posten"); f(op,"E18","=SUM(E5:E16)"); total(op,"A18:F18");
note(op,20,"F","Auswahl für die Zahlungsbesprechung, kein vollständiges Kreditorenverzeichnis. Ausstehende Löhne, Steuern und weitere Verpflichtungen sind hier nicht vollständig zusammengestellt. Mahnungen werden nicht als neue Forderungen hinzugezählt.",40);
note(op,22,"F","Alle zwölf Rechnungen sind bis einschließlich 15.04.2024 fällig. Der Auszug enthält keine Ausgleichsbuchung auf diese Posten; die Darlehenszahlung ist separat auf dem Finanzierungskonto erfasst. Zusammengestellt am 11.06.2026 durch Jutta Kröger.",40);

setup(balances,"3. Stichtagsabgleich", "Jutta Kröger | 11.06.2026 | Beträge aus K4 und der ausgewählten Kreditorenliste",[470,170,330],22);
header(balances,["Zeitpunkt / Rechenschritt","Betrag EUR","Verknüpfung"]);
const checkpoints = [
 ["März: Eröffnung", "=Maerz!E3", "K4 Blatt 16 / Vortrag Blatt 17"],
 ["März: vor Zinszahlung", "=Maerz!E8", "Nach Buchung vom 08.03.2024"],
 ["März: nach Zinszahlung", "=Maerz!E9", "Nach Buchung vom 15.03.2024"],
 ["März: Monatsende", "=Maerz!E16", "Letzte Buchung im März"],
 ["April: vor beiden Darlehenszahlungen", "=April!E8", "Nach Buchung vom 08.04.2024"],
 ["April: nach Zins und Endtilgung", "=April!E10", "Nach beiden Aufträgen vom 15.04.2024"],
 ["April: Monatsende", "=April!E17", "Letzte Buchung im April"],
 ["Auswahl der bis 15.04. fälligen Kreditoren", "=OffenePosten!E18", "Zwölf Rechnungen; kein Gesamtstatus"],
 ["Restbetrag nach Abzug nur dieser Auswahl", "=B10-B12", "Kontostand nach Darlehen minus Auswahl"],
];
checkpoints.forEach(([label,formula,source], i)=>{const r=i+5;balances.getRange(`A${r}:C${r}`).values=[[label,null,source]]; f(balances,`B${r}`,formula);});
balances.getRange("B5:B13").setNumberFormat(euros);
balances.getRange("A5:C13").format.rowHeight=28; grid(balances,"A5:C13"); total(balances,"A13:C13");
note(balances,15,"C","Der Restbetrag ist positiv. Die vorgelegte Auswahl belegt daher für sich keinen Fehlbetrag nach den Zahlungen am 15. April. Sie erlaubt umgekehrt keine Bestätigung, dass sämtliche fälligen Verpflichtungen erfüllt werden konnten.",40);
note(balances,17,"C","Für einen vollständigen Abgleich wären weitere damals fällige Verpflichtungen, ihre Belege und verfügbare Mittel gesondert aufzunehmen. Hier werden keine unbelegten Zusatzverbindlichkeiten oder freien Kreditlinien angesetzt.",40);
note(balances,19,"C","Die Rückforderung Nordhafen vom 02.05.2024 gehört nicht in die April-Auswahl. Der nachfolgende Mai-Vermerk stellt nur den späteren, separat dokumentierten Vorgang dar; eine frühere Fälligkeit wird daraus nicht abgeleitet.",40);

setup(may,"4. Gesonderter Vorgang vom 2. Mai 2024", "Jutta Kröger | Abgrenzung zum April-Abgleich | Quelle: K7 Blatt 6 | Zusammenstellung 11.06.2026",[430,165,375],23);
header(may,["Position","Betrag EUR","Beleg / zeitliche Einordnung"]);
may.getRange("A5:C7").values = [
 ["Rückforderung Nordhafen, N42-R240502",598600,"02.05.2024, 09:20 Uhr; Grothe 10:05 Uhr"],
 ["April-Schlusssaldo als Ausgangsbetrag",null,"K4 Blatt 18; kein neuer Mai-Kontoauszug"],
 ["Rückforderung abzüglich Ausgangsbetrag",null,"Nur dieser spätere Vergleich"]
];
f(may,"B6","=April!E17"); f(may,"B7","=B5-B6"); may.getRange("B5:B7").setNumberFormat(euros);
may.getRange("A5:C7").format.rowHeight=30; grid(may,"A5:C7"); total(may,"A7:C7");
note(may,9,"C","09:20 Uhr: Nordhafen beanstandet Risse bei Temperaturwechselprüfungen an den Losen N42-2402 und N42-2403 und verlangt die Rücknahme der April-Lieferung sowie Rückzahlung von 598.600,00 EUR am selben Tag.",40);
note(may,11,"C","10:05 Uhr: Grothe bestätigt Rücknahme und Rückzahlung ohne Aufrechnung. Damit ist noch keine tatsächliche Zahlung gebucht. Der Betrag entspricht dem im April eingegangenen Kundenbetrag, nicht einer weiteren April-Auszahlung.",40);
note(may,13,"C","11:10 Uhr: Kröger führt den Vorgang gesondert und berichtet, dass heute kein weiterer Eingang vorhanden ist. Ihre Nachricht knüpft an den April-Endbestand an. Sie ersetzt keinen Kontoauszug mit sämtlichen Mai-Bewegungen.",40);
note(may,15,"C","15:40 Uhr: Grothe teilt mit, dass der Insolvenzantrag heute gestellt wurde und keine neue Finanzierung vorliegt. Diese Information ist zeitlich vom März- und April-Zahlungsstand zu trennen.",36);
note(may,17,"C","Die rechnerischen 215.600,00 EUR betreffen ausschließlich den Vergleich der neuen Rückforderung mit dem genannten Ausgangsbetrag. Sie sind weder ein April-Fehlbetrag noch eine vollständige Summe aller am 2. Mai offenen Verpflichtungen.",40);
note(may,19,"C","Bearbeitung: Jutta Kröger. Der Arbeitsmappe sind keine neuen Bankbuchungen nach dem 30.04.2024 zugrunde gelegt. Die zugrunde liegende Korrespondenz bleibt als gesonderter Beleg erhalten.",36);
bank.recalculate();
for (const [r,value] of [[5,421800],[6,573900],[7,568900],[8,431000],[9,1025900],[10,520900],[11,383000],[12,478380],[13,42520]]) check(balances,`B${r}`,value);
check(may,"B7",215600);
v(april,"D5",598601); bank.recalculate(); check(balances,"B13",42521); check(may,"B7",215599);
v(april,"D5",598600); bank.recalculate(); check(balances,"B13",42520); check(may,"B7",215600);
await save(bank,"43_Kontoabgleich_20260611.xlsx",[["Maerz","A1:G19"],["April","A1:G20"],["OffenePosten","A1:F22"],["Stichtage","A1:C19"],["MaiAbgrenzung","A1:C19"]]);
console.log("Verified: 590000 / 515000 / 478380 / 42520 / 215600; both perturbation checks passed.");

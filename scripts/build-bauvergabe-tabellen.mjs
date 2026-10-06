// Author with the bundled @oai/artifact-tool runtime; no repository dependencies.
// Reproducible example from the repository root. Resolve CODEX_PYTHON, CODEX_NODE
// and CODEX_NODE_MODULES through load_workspace_dependencies; use the bundled paths.
//   work_dir="$(mktemp -d)"
//   "$CODEX_PYTHON" scripts/bauvergabe-tabellen-spec.py \
//     --output "$work_dir/tabellen-spec.json" --qa-dir "$work_dir/qa"
//   ln -s "$CODEX_NODE_MODULES" "$work_dir/node_modules"
//   cp scripts/build-bauvergabe-tabellen.mjs "$work_dir/"
//   "$CODEX_NODE" "$work_dir/build-bauvergabe-tabellen.mjs" "$work_dir/tabellen-spec.json"
// The JSON generator writes no workbooks; the final command replaces the four case XLSX files.
import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const spec = JSON.parse(await fs.readFile(process.argv[2], 'utf8'));
await fs.mkdir(spec.qaDir, { recursive: true });
const numberFormat = '#,##0.00;[Red](#,##0.00);0.00';
const theme = { ink: '#192D3E', input: '#FFF4D6', blue: '#0000FF', rule: '#BDCBD5' };
const manifest = [];

function value(sh, cell, v) { sh.getRange(cell).values = [[v]]; }
function formula(sh, cell, f) { sh.getRange(cell).formulas = [[f]]; }
function line(sh, row, text) { value(sh, `A${row}`, text); }
function totalStyle(sh, row) {
  sh.getRange(`B${row}:F${row}`).format.font.bold = true;
  sh.getRange(`B${row}:F${row}`).format.borders = { top: { style: 'thin', color: theme.rule } };
}
function guardedProduct(a, b) { return `=IF(COUNT(${a},${b})=2,ROUND(${a}*${b},2),"n.a.")`; }
function guardedSum(start, end, count) { return `=IF(COUNT(F${start}:F${end})=${count},SUM(F${start}:F${end}),"n.a.")`; }

for (const c of spec.cases) {
  for (const kind of ['angebot', 'nachtrag']) {
    const offer = kind === 'angebot';
    const wb = Workbook.create();
    const sh = wb.worksheets.add(offer ? 'Angebot' : 'Nachtrag N01');
    sh.showGridLines = false;
    sh.tabColor = theme.ink;
    const lastRow = offer ? 39 : 36;
    sh.getRange(`A1:F${lastRow}`).format = {
      font: { name: 'Times New Roman', size: 11, color: '#000000' },
      verticalAlignment: 'center', rowHeight: 16,
    };
    for (const [col, width] of Object.entries({ A: 56, B: 300, C: 46, D: 105, E: 106, F: 124 })) {
      sh.getRange(`${col}1:${col}${lastRow}`).format.columnWidthPx = width;
    }
    sh.getRange(`D1:F${lastRow}`).setNumberFormat(numberFormat);
    sh.getRange(`A1:A${lastRow}`).setNumberFormat('@');
    sh.getRange(`D1:F${lastRow}`).format.horizontalAlignment = 'right';
    line(sh, 2, offer ? '1. Angebotskalkulation' : '1. Nachtragskosten N01');
    sh.getRange('A2:F2').format.font = { name: 'Times New Roman', size: 11, bold: true, color: theme.ink };
    sh.getRange('A2:F2').format.borders = { bottom: { style: 'thin', color: theme.rule } };
    line(sh, 3, `${c.shortTitle} · ${c.reference}`);
    line(sh, 4, c.winner);
    line(sh, 5, offer ? `Angebotsstand ${c.offerDate} · ${c.lot}` : 'Kalkulationsstand 10.03.2027 · Anordnung 05.03.2027 · Plan P07');
    line(sh, 6, 'Beträge in EUR · Berechnungsgrundlagen siehe Quellen');
    line(sh, 7, 'Gelb / blaue Schrift: Eingaben. Schwarz: Formeln. Leer ist „n.a.“, null ist 0,00.');
    if (offer) {
      value(sh, 'B9', 'Angebot netto'); formula(sh, 'F9', '=F32');
      value(sh, 'B10', 'Angebot brutto'); formula(sh, 'F10', '=F34');
      sh.getRange('B9:F10').format.font.bold = true;
      line(sh, 12, '1.1 Preisblatt U04 mit Berichtigung 01');
      sh.getRange('A13:F13').values = [['OZ', 'Leistung', 'Einh.', 'Menge', 'EP netto', 'Betrag netto']];
      sh.getRange('A14:E29').values = c.offerRows.map(r => [r.oz, r.description, r.unit, r.quantity, r.rate]);
      formula(sh, 'F14', guardedProduct('D14', 'E14'));
      sh.getRange('F14:F29').fillDown();
      sh.getRange('B14:B29').format.wrapText = true;
      sh.getRange('A14:F29').format.rowHeight = 29;
      sh.getRange('A15:F15').format.rowHeight = 42;
      sh.getRange('A29:F29').format.rowHeight = 42;
      sh.getRange('D14:E29').format.fill = theme.input;
      sh.getRange('D14:E29').format.font.color = theme.blue;
      value(sh, 'B31', 'Umsatzsteuersatz'); value(sh, 'E31', 0.19);
      value(sh, 'B32', 'Summe netto'); formula(sh, 'F32', guardedSum(14, 29, 16));
      value(sh, 'B33', 'Umsatzsteuer'); formula(sh, 'F33', guardedProduct('F32', 'E31'));
      value(sh, 'B34', 'Summe brutto'); formula(sh, 'F34', guardedSum(32, 33, 2));
      sh.getRange('E31').format.fill = theme.input;
      sh.getRange('E31').format.font.color = theme.blue;
      sh.getRange('E31').setNumberFormat('0.0%');
      totalStyle(sh, 32); totalStyle(sh, 34);
      line(sh, 36, '1.2 Quellen');
      line(sh, 37, 'OZ / Mengen: 01-vergabeunterlagen/07_Mengen_Preisblatt.csv.');
      line(sh, 38, 'Einheitspreise: eigene Kalkulation; gelb markierte Eingaben.');
      line(sh, 39, 'Transportansatz: 02-vergabeverfahren/03_Berichtigung_01.docx.');
    } else {
      value(sh, 'B9', 'Beansprucht netto'); formula(sh, 'F9', '=F25');
      value(sh, 'B10', 'Beansprucht brutto'); formula(sh, 'F10', '=F28');
      sh.getRange('B9:F10').format.font.bold = true;
      line(sh, 11, 'Angebotsforderung, nicht anerkannt. Zuschläge sind nicht vereinbart.');
      sh.getRange('A11:F11').format.font.color = '#9C3E16';
      line(sh, 13, '1.1 Ausschließlich zusätzliche Mengen nach P07');
      sh.getRange('A14:F14').values = [['OZ', 'Mehrleistung', 'Einh.', 'Menge', 'Kostensatz', 'Direkte Kosten']];
      sh.getRange('A15:E17').values = c.changeRows.map(r => [r.oz, r.description, r.unit, r.quantity, r.rate]);
      formula(sh, 'F15', guardedProduct('D15', 'E15')); sh.getRange('F15:F17').fillDown();
      sh.getRange('B15:B17').format.wrapText = true;
      sh.getRange('A15:F17').format.rowHeight = 30;
      sh.getRange('D15:E17').format.fill = theme.input;
      sh.getRange('D15:E17').format.font.color = theme.blue;
      value(sh, 'B19', 'Direkte Kosten'); formula(sh, 'F19', guardedSum(15, 17, 3)); totalStyle(sh, 19);
      line(sh, 21, '1.2 Zuschläge jeweils auf direkte Kosten');
      value(sh, 'B22', 'Allgemeine Geschäftskosten'); value(sh, 'E22', 0.08); formula(sh, 'F22', guardedProduct('F19', 'E22'));
      value(sh, 'B23', 'Wagnis und Gewinn'); value(sh, 'E23', 0.05); formula(sh, 'F23', guardedProduct('F19', 'E23'));
      sh.getRange('E22:E23').setNumberFormat('0.0%');
      sh.getRange('E22:E23').format.fill = theme.input;
      sh.getRange('E22:E23').format.font.color = theme.blue;
      value(sh, 'B25', 'Beanspruchter Nachtrag netto');
      formula(sh, 'F25', '=IF(COUNT(F19,F22,F23)=3,SUM(F19,F22,F23),"n.a.")');
      totalStyle(sh, 25);
      value(sh, 'B26', 'Umsatzsteuersatz'); value(sh, 'E26', 0.19);
      sh.getRange('E26').format.fill = theme.input; sh.getRange('E26').format.font.color = theme.blue;
      sh.getRange('E26').setNumberFormat('0.0%');
      value(sh, 'B27', 'Umsatzsteuer'); formula(sh, 'F27', guardedProduct('F25', 'E26'));
      value(sh, 'B28', 'Beanspruchter Nachtrag brutto'); formula(sh, 'F28', '=IF(COUNT(F25,F27)=2,SUM(F25,F27),"n.a.")'); totalStyle(sh, 28);
      line(sh, 30, '1.3 Abgrenzung und Quelle');
      line(sh, 31, 'Kein pauschaler BGK-Zuschlag; konkret enthaltene BGK nicht doppelt fordern.');
      line(sh, 32, 'Bauzeit: 12 Kalendertage behauptet; Preisfolge streitig und hier nicht bewertet.');
      line(sh, 33, 'Mengen- und Preisfreigabe getrennt prüfen; keine Anerkennung durch Aufmaß.');
      line(sh, 34, 'Quelle: 05-nachtragsmanagement/03_Nachtragsangebot.docx, Abschnitt 2.');
      line(sh, 35, 'Mengen: 05-nachtragsmanagement/04_Aufmass_N01.csv; OZ wie Vertrags-LV.');
      line(sh, 36, 'N01 enthält ausschließlich die drei dargestellten Mehrleistungen.');
    }
    const header = offer ? 13 : 14;
    sh.getRange(`A${header}:F${header}`).format = {
      fill: theme.ink, font: { name: 'Times New Roman', size: 11, bold: true, color: '#FFFFFF' },
      horizontalAlignment: 'center', rowHeight: 26,
      borders: { insideVertical: { style: 'thin', color: '#FFFFFF' } },
    };
    sh.getRange(`F9:F${lastRow}`).conditionalFormats.add('containsText', { text: 'n.a.', format: { fill: '#FEE2E2', font: { color: '#9C0006' } } });
    wb.recalculate();
    const filename = offer ? '03-bieterarbeit/02_Angebotskalkulation.xlsx' : '05-nachtragsmanagement/06_Nachtragskosten.xlsx';
    const target = path.join(spec.repo, 'testakten', c.slug, filename);
    await fs.mkdir(path.dirname(target), { recursive: true });
    const tag = `${c.short}-${kind}`;
    const preview = await wb.render({ sheetName: sh.name, range: `A1:F${lastRow}`, scale: 1.5, format: 'png' });
    await fs.writeFile(path.join(spec.qaDir, `${tag}.png`), new Uint8Array(await preview.arrayBuffer()));
    await (await SpreadsheetFile.exportXlsx(wb)).save(target);
    // The runtime adds an inspection sidecar; keep QA files out of the case delivery.
    await fs.rm(`${target}.inspect.ndjson`, { force: true });
    const inputCell = offer ? 'D14' : 'D15';
    const baseQty = offer ? c.offerRows[0].quantity : c.changeRows[0].quantity;
    const rate = offer ? c.offerRows[0].rate : c.changeRows[0].rate;
    const record = { tag, target, sheet: sh.name, inputCell, rate, baseQty,
      baseNet: offer ? c.expectedOfferNet : c.expectedChangeDirect * 1.13,
      netCell: offer ? 'F32' : 'F25', grossCell: offer ? 'F34' : 'F28', directCell: offer ? null : 'F19',
      mutationFiles: {}, inputStyle: 'yellow fill / blue font', lastRow };
    const audit = await wb.inspect({ kind: 'region', sheetId: sh.name, range: offer ? 'E31:F34' : 'E19:F28', maxChars: 5000, tableMaxRows: 12, tableMaxCols: 2 });
    await fs.writeFile(path.join(spec.qaDir, `${tag}-inspection.json`), JSON.stringify(audit, null, 2));
    for (const [scenario, qty] of Object.entries({ normal: baseQty + 1, blank: null, zero: 0 })) {
      value(sh, inputCell, qty); wb.recalculate();
      const copy = path.join(spec.qaDir, 'mutations', `${tag}-${scenario}.xlsx`);
      await fs.mkdir(path.dirname(copy), { recursive: true });
      await (await SpreadsheetFile.exportXlsx(wb)).save(copy);
      record.mutationFiles[scenario] = copy;
    }
    manifest.push(record);
    console.log(`Created ${tag}`);
  }
}
await fs.writeFile(path.join(spec.qaDir, 'manifest.json'), JSON.stringify(manifest, null, 2));

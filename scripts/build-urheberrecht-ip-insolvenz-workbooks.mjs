#!/usr/bin/env node
/** Baut die Arbeitsmappen der drei IP-Insolvenzakten aus JSON-Spezifikationen. */

import fs from "node:fs/promises";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const specPath = process.argv[2];
const previewDir = process.argv[3];
if (!specPath || !previewDir) {
  throw new Error("Aufruf: build.mjs <workbooks.json> <preview-dir>");
}

const data = JSON.parse(await fs.readFile(specPath, "utf8"));
await fs.mkdir(previewDir, { recursive: true });

const BLUE = "#173A54";
const PALE = "#E7EFF4";
const INK = "#172B38";
const MUTED = "#64717B";

function excelColumn(index) {
  let value = index + 1;
  let label = "";
  while (value) {
    const digit = (value - 1) % 26;
    label = String.fromCharCode(65 + digit) + label;
    value = Math.floor((value - 1) / 26);
  }
  return label;
}

function cleanName(value, fallback) {
  const cleaned = String(value || fallback)
    .replace(/[\\/:*?\[\]]/g, "_")
    .slice(0, 31)
    .trim();
  return cleaned || fallback;
}

function previewName(workbookPath, sheetName) {
  const parts = path.normalize(workbookPath).split(path.sep);
  const testaktenIndex = parts.lastIndexOf("testakten");
  const slug = testaktenIndex >= 0 && parts[testaktenIndex + 1]
    ? parts[testaktenIndex + 1]
    : path.basename(path.dirname(workbookPath));
  const stem = path.basename(workbookPath, path.extname(workbookPath));
  return `${slug}__${stem}__${sheetName}`.replace(/[^A-Za-z0-9._-]+/g, "_") + ".png";
}

const report = [];
const previewPaths = new Set();
for (const workbookSpec of data.workbooks || []) {
  const workbook = Workbook.create();
  const sheetNames = [];

  for (const [sheetIndex, rawSheet] of (workbookSpec.sheets || []).entries()) {
    const sheetName = cleanName(rawSheet.name, `Tabelle_${sheetIndex + 1}`);
    const sheet = workbook.worksheets.add(sheetName);
    sheetNames.push(sheetName);
    sheet.showGridLines = false;

    const headers = (rawSheet.headers || []).map((value) => String(value ?? ""));
    const rows = rawSheet.rows || [];
    const columnCount = Math.max(1, headers.length, ...rows.map((row) => row.length));
    const lastColumn = excelColumn(columnCount - 1);
    const title = String(rawSheet.title || workbookSpec.title || sheetName);

    sheet.getRange(`A1:${lastColumn}2`).merge();
    sheet.getRange("A1").values = [[title]];
    sheet.getRange(`A1:${lastColumn}2`).format = {
      fill: BLUE,
      font: { name: "Times New Roman", size: 16, bold: true, color: "#FFFFFF" },
      verticalAlignment: "center",
      rowHeight: 24,
      wrapText: true,
    };

    const sheetNotes = (rawSheet.notes || []).map((value) => String(value).trim()).filter(Boolean);
    const noteText = [
      "Arbeitsstand aus den beigefügten Aktenstücken; offene Angaben bleiben offen und sind nicht als Nullwert zu behandeln.",
      ...sheetNotes,
    ].join(" ");
    sheet.getRange(`A3:${lastColumn}3`).merge();
    sheet.getRange("A3").values = [[noteText]];
    sheet.getRange(`A3:${lastColumn}3`).format = {
      fill: PALE,
      font: { name: "Times New Roman", size: 11, italic: true, color: MUTED },
      verticalAlignment: "center",
      wrapText: true,
      rowHeight: 28,
    };

    if (headers.length) {
      sheet.getRangeByIndexes(4, 0, 1, columnCount).values = [
        Array.from({ length: columnCount }, (_, index) => headers[index] || `Spalte ${index + 1}`),
      ];
      sheet.getRangeByIndexes(4, 0, 1, columnCount).format = {
        fill: BLUE,
        font: { name: "Times New Roman", size: 11, bold: true, color: "#FFFFFF" },
        verticalAlignment: "center",
        wrapText: true,
        rowHeight: 36,
      };
    }

    if (rows.length) {
      const normalized = rows.map((row) =>
        Array.from({ length: columnCount }, (_, index) => row[index] ?? "")
      );
      sheet.getRangeByIndexes(5, 0, normalized.length, columnCount).values = normalized;
      sheet.getRangeByIndexes(5, 0, normalized.length, columnCount).format = {
        font: { name: "Times New Roman", size: 11, color: INK },
        verticalAlignment: "top",
        wrapText: true,
        rowHeight: 34,
      };
      for (let index = 1; index < normalized.length; index += 2) {
        sheet.getRangeByIndexes(5 + index, 0, 1, columnCount).format.fill = "#F5F8FA";
      }
    }

    const widths = rawSheet.widths || [];
    for (let column = 0; column < columnCount; column += 1) {
      const configured = Number(widths[column]);
      const sample = [headers[column] || "", ...rows.slice(0, 60).map((row) => String(row[column] ?? ""))];
      const longest = Math.max(8, ...sample.map((value) => value.length));
      const width = Number.isFinite(configured) && configured > 0
        ? configured
        : Math.min(48, Math.max(13, Math.ceil(longest * 0.88)));
      sheet.getRange(`${excelColumn(column)}1:${excelColumn(column)}${Math.max(6, rows.length + 5)}`).format.columnWidth = width;
    }
    sheet.freezePanes.freezeRows(5);
    if (columnCount > 4) sheet.freezePanes.freezeColumns(1);

    const previewRows = Math.min(Math.max(8, rows.length + 5), 22);
    const preview = await workbook.render({
      sheetName,
      range: `A1:${lastColumn}${previewRows}`,
      scale: 1,
      format: "png",
    });
    const previewFilename = previewName(workbookSpec.path, sheetName);
    if (previewPaths.has(previewFilename)) {
      throw new Error(`Doppelter Vorschaupfad: ${previewFilename}`);
    }
    previewPaths.add(previewFilename);
    await fs.writeFile(
      path.join(previewDir, previewFilename),
      new Uint8Array(await preview.arrayBuffer()),
    );
  }

  const errorScan = await workbook.inspect({
    kind: "match",
    searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!",
    options: { useRegex: true, maxResults: 50 },
    maxChars: 4000,
  });
  const scanText = JSON.stringify(errorScan);
  if (/\"text\"\s*:\s*\"#(?:REF!|DIV\/0!|VALUE!|NAME\?|N\/A|NUM!|NULL!)/.test(scanText)) {
    throw new Error(`Formelfehler in ${workbookSpec.path}: ${scanText}`);
  }

  await fs.mkdir(path.dirname(workbookSpec.path), { recursive: true });
  const exported = await SpreadsheetFile.exportXlsx(workbook);
  await exported.save(workbookSpec.path);
  await fs.rm(`${workbookSpec.path}.inspect.ndjson`, { force: true });
  report.push({ path: workbookSpec.path, sheets: sheetNames });
}

await fs.writeFile(
  path.join(previewDir, "workbook-build-report.json"),
  JSON.stringify({ workbooks: report }, null, 2),
);
console.log(JSON.stringify({ workbooks: report.length, report }, null, 2));

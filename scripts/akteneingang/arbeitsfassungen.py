"""Führt vorhandene Arbeitsunterlagen in ihrer eigenen Word- oder Tabellenform fort."""

from __future__ import annotations

import csv
import io
from pathlib import Path

from docx import Document
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from pypdf import PdfReader, PdfWriter

from .dokumente import office_bytes, read_pdf, table_rows


def arbeitskopie(item, original):
    name = Path(item["quelle"])
    if name.suffix == ".docx":
        doc = Document(io.BytesIO(original))
        doc.add_page_break()
        doc.add_heading(item["titel"], level=1)
        doc.add_paragraph(item["von"] + " · " + item["an"])
        for text in item["text"]:
            doc.add_paragraph(text)
        return name.name, office_bytes(doc)
    if name.suffix == ".csv":
        raw = original.decode("utf-8-sig")
        sep = csv.Sniffer().sniff(raw[:4096], delimiters=",;\t").delimiter
        wb = Workbook()
        ws = wb.active
        ws.title = "Originalexport"
        for row in csv.reader(io.StringIO(raw), delimiter=sep):
            ws.append(row)
            for cell in ws[ws.max_row]:
                if cell.data_type == "f":
                    cell.data_type = "s"
    elif name.suffix == ".xlsx":
        wb = load_workbook(io.BytesIO(original))
    else:
        raise ValueError("Ungeeignete Arbeitsunterlage: " + str(name))
    if "Rueckfragen" in wb.sheetnames:
        raise ValueError("Blattname bereits belegt")
    ws = wb.create_sheet("Rueckfragen")
    ws.append([item["titel"]])
    ws.append([item["von"], item["an"]])
    ws.append([])
    rows = table_rows(item)
    for row in rows:
        ws.append(row)
    for cell in ws[4]:
        cell.fill = PatternFill("solid", fgColor="235657")
        cell.font = Font(bold=True, color="FFFFFF")
    for i in range(len(rows[0])):
        ws.column_dimensions[get_column_letter(i + 1)].width = max(
            22, min(65, max(len(r[i]) for r in rows) + 1)
        )
    for row in ws.iter_rows(min_row=4):
        for c in row:
            c.alignment = Alignment(vertical="top", wrap_text=True)
    ws.freeze_panes = "A5"
    return name.with_suffix(".xlsx").name, office_bytes(wb)


def ergaenze(akten, lesestuecke, records):
    for item in records:
        original = item["quelle"]
        if not original.startswith("Grundakte/") or original not in akten:
            raise ValueError("Quelle der Arbeitsfassung fehlt: " + original)
        name, data = arbeitskopie(item, akten[original])
        new = "Grundakte/Arbeitsfassungen/" + name
        if new in akten:
            raise ValueError("Kollision Arbeitsfassung: " + new)
        akten[new] = data
        src = Path(original).with_suffix(".pdf")
        # Gedruckte Bestandsstücke können den Verzeichnispfad flach oder separat tragen.
        candidates = [
            n
            for n in lesestuecke
            if n == src.name or n.replace("__", "/").endswith("/" + src.name)
        ]
        if len(candidates) != 1:
            raise ValueError(
                "Lesefassung nicht eindeutig: " + str(src) + " " + str(candidates)
            )
        merged = PdfWriter()
        for b in (lesestuecke[candidates[0]], read_pdf({**item, "_fachfassung": True})):
            merged.append(PdfReader(io.BytesIO(b)), import_outline=False)
        buffer = io.BytesIO()
        merged.write(buffer)
        merged.close()
        lesestuecke[new.replace("/", "__").rsplit(".", 1)[0] + ".pdf"] = (
            buffer.getvalue()
        )

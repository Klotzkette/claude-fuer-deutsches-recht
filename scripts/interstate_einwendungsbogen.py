"""Leere Arbeitsmappe für die Prüfung der Eingangspost einer Vergabeakte."""
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.properties import PageSetupProperties

from akteneingang.dokumente import office_bytes


def pruefbogen():
    book = Workbook()
    book.properties.title = "Deutsche Interstate AG · Prüfbogen für Einwendungen"
    book.properties.creator = "Deutsche Interstate AG · Niederlassung West (fiktiv)"
    sheets = (
        ("Eingang", "Jedes Schreiben erhält eine eigene Kennung. Für mehrere Beanstandungen im selben Schreiben können Sie Unterpunkte bilden.",
         (("Kennung", 12), ("Fall / Los / Verfahrensstand", 28), ("Absender / Empfänger", 28),
          ("Eingang (Ortszeit)", 22), ("Übermittlungsweg / Aktenstück / Belegstelle", 47))),
        ("Prüfung", "Übernehmen Sie die Kennung. Halten Sie zu jeder Tatsachenbehauptung auch den Gegenbeleg oder die offene Beweisfrage fest.",
         (("Kennung", 12), ("Beanstandung / konkretes Begehren", 31), ("Bezeichnung im Schreiben / eigene rechtliche Einordnung", 33),
          ("Beleg und Gegenbeleg (jeweils mit Fundstelle)", 35), ("Maßstab / vorläufige Würdigung", 30))),
        ("Entscheidung", "Halten Sie fest, welches Ereignis welche Frist oder Sperre auslösen könnte. Dokumentieren Sie auch einen noch fehlenden Nachweis.",
         (("Kennung", 12), ("Fristgrundlage / Auslöser / Beleg", 36), ("Fristende / Wirkung auf Verfahren oder Vertrag", 32),
          ("Entscheidungsvorschlag / Antwort an", 35), ("Zuständig / Wiedervorlage / Freigabe", 27))),
    )
    for index, (name, hint, columns) in enumerate(sheets):
        sheet = book.active if index == 0 else book.create_sheet()
        sheet.title = name
        sheet.sheet_view.showGridLines = False
        for row, value in ((1, "Einwendungen prüfen · " + name), (2, hint)):
            sheet.merge_cells(start_row=row, start_column=1, end_row=row, end_column=len(columns))
            cell = sheet.cell(row, 1, value)
            cell.font = Font(name="Calibri", size=16 if row == 1 else 11, bold=row == 1, color="234C5A")
            cell.alignment = Alignment(vertical="center", wrap_text=True)
        sheet.row_dimensions[1].height = 32
        sheet.row_dimensions[2].height = 38
        sheet.row_dimensions[3].height = 36
        for col, (label, width) in enumerate(columns, 1):
            sheet.column_dimensions[get_column_letter(col)].width = width
            header = sheet.cell(3, col, label)
            header.font = Font(name="Calibri", bold=True, color="FFFFFF")
            header.fill = PatternFill("solid", fgColor="234C5A")
            header.alignment = Alignment(vertical="center", wrap_text=True)
            for row in range(4, 12):
                cell = sheet.cell(row, col)
                cell.alignment = Alignment(vertical="top", wrap_text=True)
                cell.border = Border(bottom=Side(style="thin", color="9CAFB4"))
                cell.fill = PatternFill("solid", fgColor="F1F6F6" if row % 2 == 0 else "FFFFFF")
                if name == "Eingang" and col == 4:
                    cell.number_format = "dd.mm.yyyy hh:mm"
                sheet.row_dimensions[row].height = 38
        sheet.freeze_panes = "B4"
        sheet.print_options.horizontalCentered = True
        sheet.page_setup.orientation = "landscape"
        sheet.page_setup.paperSize = sheet.PAPERSIZE_A4
        sheet.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
        sheet.page_setup.fitToWidth = 1
        sheet.page_setup.fitToHeight = 0
        sheet.print_title_rows = "1:3"
        sheet.oddFooter.left.text = "Deutsche Interstate AG · Arbeitsvorlage"
        sheet.oddFooter.right.text = "Seite &P"
    return office_bytes(book)

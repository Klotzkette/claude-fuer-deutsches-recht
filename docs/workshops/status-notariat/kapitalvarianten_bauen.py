"""G10, interne Arbeitsmappe vom 17. April 2026. Ausführen mit Python und XlsxWriter."""
from datetime import datetime
from pathlib import Path

import xlsxwriter


CASE = Path(__file__).resolve().parents[3] / "testakten/neuralis-medtech-erlangen-gestaltungsakte"
TARGET = CASE / "02_Gestaltungsvorschlaege/G10_Kapitalvarianten_zur_Finanzierungsrunde.xlsx"


def build(target):
    with xlsxwriter.Workbook(target) as book:
        book.set_properties({"title": "Kapitalvarianten zur Finanzierungsrunde", "author": "Caroline Benkert",
                             "company": "Neuralis MedTech GmbH", "created": datetime(2026, 4, 17, 9, 30)})

        def style(**options):
            return book.add_format({"font_name": "Calibri", "font_size": 11, "valign": "vcenter",
                                    "font_color": "#213943", **options})

        label = style()
        header = style(bold=True, text_wrap=True, bg_color="#DBEBEA")
        title = style(bold=True, font_size=20, font_color="#FFFFFF", bg_color="#145C5D")
        meta = style(bold=True, font_size=10, font_color="#145C5D")
        notes = style(text_wrap=True)
        integer = style(num_format='#,##0')
        percent = style(num_format='0.0%')
        input_value = style(num_format='#,##0', bg_color="#FFF1D8", font_color="#674816")
        sum_value = style(num_format='#,##0', bold=True, top=1)
        sum_label = style(bold=True, top=1)
        sum_percent = style(num_format='0.0%', bold=True, top=1)

        def setup(name, headline, widths):
            sheet = book.add_worksheet(name)
            for col, width in enumerate(widths):
                sheet.set_column(col, col, width)
            sheet.set_landscape()
            sheet.set_paper(9)
            sheet.fit_to_pages(1, 1)
            sheet.set_margins(.42, .42, .5, .5)
            sheet.hide_gridlines(2)
            sheet.set_footer('&LNeuralis MedTech GmbH  ·  Finanzen&R17.04.2026   |   Blatt &P')
            sheet.merge_range('A1:G1', 'FINANZEN  /  CAROLINE BENKERT                                      ERLANGEN  ·  17. APRIL 2026', meta)
            sheet.merge_range('A2:G2', headline, title)
            sheet.set_row(1, 42)
            sheet.set_tab_color('#145C5D')
            return sheet

        cap = setup('Kapital', 'Beteiligungen für die Finanzierungsrunde', [32, 14, 13, 15, 13, 16, 14])
        cap.merge_range('A4:G4', 'Arbeitsstand für die Besprechung. Bestand laut Liste A04. Zwei getrennte Rechenaufträge; eine Zeichnung oder Abtretung ist im Ordner nicht hinterlegt.', notes)
        cap.set_row(3, 32)
        cap.write_row('A6', ['Gesellschafter', 'Bestand EUR', 'Quote', 'Nach Kauf EUR', 'Quote', 'Nach Ausgabe EUR', 'Quote'], header)
        cap.set_row(5, 32)
        for r, name, base, after_sale, after_issue in [
                (7, 'FrankenHealth Ventures GmbH', 51000, 33000, 51000),
                (8, 'Dr. Henrik Vogt', 32000, 50000, 68000),
                (9, 'Dr. Miriam Seidl', 17000, 17000, 17000)]:
            cap.write(f'A{r}', name, label)
            cap.write_number(f'B{r}', base, input_value)
            sale = {7: '-$B$13', 8: '+$B$13', 9: ''}[r]
            cap.write_formula(f'D{r}', f'=B{r}{sale}', integer, after_sale)
            cap.write_formula(f'F{r}', f'=B{r}' + ('+$B$14' if r == 8 else ''), integer, after_issue)
            for col, amt, numerator, denominator in [('C', 'B', base, 100000), ('E', 'D', after_sale, 100000),
                                                    ('G', 'F', after_issue, 136000)]:
                cap.write_formula(f'{col}{r}', f'={amt}{r}/{amt}$10', percent, numerator / denominator)
            cap.set_row(r-1, 26)
        cap.write('A10', 'Stammkapital gesamt', sum_label)
        for col, value in zip('BCDEFG', [100000, 1, 100000, 1, 136000, 1]):
            cap.write_formula(f'{col}10', f'=SUM({col}7:{col}9)', sum_percent if col in 'CEG' else sum_value, value)
        cap.set_row(9, 25)
        cap.merge_range('A12:G12', 'Rechenannahmen für das Gespräch   ·   gelbe Felder sind Eingaben', header)
        cap.set_row(11, 24)
        assumptions = [
            ('Teilnennbetrag aus Fondsanteil', 18000, 'G08: Verkauf an Vogt aus dem Bestand des Fonds.'),
            ('Neueinlage zum Nennbetrag', 36000, 'Separate Idee aus Finanzen: Nur Vogt zeichnet den neuen Anteil.'),
            ('Eigenkapitalwert laut G08', 2000000, 'Rechenwert der Fondsseite; über die Bewertung ist weiter zu verhandeln.'),
            ('Eigenmittel Vogt für Kauf', 120000, 'Für den Anteilskauf laut G08 vorgesehener privater Mitteleinsatz.')]
        for r, (caption, val, comment) in enumerate(assumptions, 13):
            cap.write(f'A{r}', caption, label)
            cap.write_number(f'B{r}', val, input_value)
            cap.merge_range(f'C{r}:G{r}', comment, notes)
            cap.set_row(r-1, 24)
        for r, caption, formula, value, detail in [
                (18, 'Kaufpreisannahme', '=B15*B13/B10', 360000, 'Empfänger wäre der Fonds. Zufluss bei Neuralis aus dem Kauf: 0 EUR.'),
                (19, 'Privater Kreditbedarf', '=B18-B16', 240000, 'Finanzierungsbedarf vor Nebenkosten. Eine Zusage liegt Finanzen nicht vor.'),
                (20, 'Neueinlage bei Neuralis', '=B14', 36000, 'Nominalbetrag bei voller Einzahlung. Bewertung, Agio und Zeichnungsbedingungen sind offen.')]:
            cap.write(f'A{r}', caption, label)
            cap.write_formula(f'B{r}', formula, integer, value)
            cap.merge_range(f'C{r}:G{r}', detail, notes)
            cap.set_row(r-1, 27)
        cap.print_area('A1:G20')

        votes = setup('Zählprobe', 'Zählprobe für die nächste Einladung', [27, 16, 15, 15, 15, 15, 16])
        votes.merge_range('A4:G4', 'Bitte dieselbe Einkaufsweisung wie am 19. März unter geänderter Teilnahme durchrechnen. Für die Terminplanung sind Anwesenheit und abgegebene Stimmen getrennt zu zählen.', notes)
        votes.set_row(3, 35)
        votes.write_row('A6', ['Rechenfall', 'Stammkapital', 'Vertreten', 'Ja', 'Nein', 'Enthaltung', 'Ja / abgegeben'], header)
        votes.set_row(5, 30)
        cases = [
            ('19.03. laut B11', 'B10', '=B7', '=Kapital!B7+Kapital!B9', '=Kapital!B8', '=0', [100000,100000,68000,32000,0]),
            ('Kauf, alle stimmen', 'D10', '=B8', '=Kapital!D7+Kapital!D9', '=Kapital!D8', '=0', [100000,100000,50000,50000,0]),
            ('Kauf, Vogt enthält sich', 'D10', '=B9', '=Kapital!D7+Kapital!D9', '=0', '=Kapital!D8', [100000,100000,50000,0,50000]),
            ('Kauf, Vogt fehlt', 'D10', '=Kapital!D7+Kapital!D9', '=C10', '=0', '=0', [100000,50000,50000,0,0]),
            ('Ausgabe, alle stimmen', 'F10', '=B11', '=Kapital!F7+Kapital!F9', '=Kapital!F8', '=0', [136000,136000,68000,68000,0])]
        for r, (caption, total, present, yes, no, abstain, vals) in enumerate(cases, 7):
            votes.write(f'A{r}', caption, label)
            for col, formula, val in zip('BCDEF', ['=Kapital!'+total, present, yes, no, abstain], vals):
                votes.write_formula(f'{col}{r}', formula, integer, val)
            votes.write_formula(f'G{r}', f'=IF(D{r}+E{r}=0,0,D{r}/(D{r}+E{r}))', percent, vals[2]/(vals[2]+vals[3]))
            votes.set_row(r-1, 29)
        votes.merge_range('A13:G13', 'Rückfragen an die Geschäftsleitung', header)
        votes.set_row(12, 24)
        for r, paragraph in [
            (14, 'Für die Einladung: Gilt für den vorgesehenen Beschluss die einfache Mehrheit? Welches Kapital muss beim ersten Termin vertreten sein, und wer übernimmt bei einer zweiten Einladung die Fristenkontrolle?'),
            (15, 'Für das Protokoll: In der Mappe bedeutet „abgegeben“ die Summe aus Ja und Nein. Bitte Enthaltungen und abwesende Anteile getrennt ins Präsenzblatt übernehmen.'),
            (16, 'Für die Runde mit dem Fonds: Beim Kauf fließt der Preis an den Verkäufer. Bei der Ausgabe eines neuen Anteils braucht die Gesellschaft eine eigene Finanzierungs- und Bewertungsabrede. Bitte die beiden Varianten getrennt zur Beratung anmelden.')]:
            votes.merge_range(f'A{r}:G{r}', paragraph, notes)
            votes.set_row(r-1, 42)
        votes.print_area('A1:G16')


if __name__ == '__main__':
    build(TARGET)

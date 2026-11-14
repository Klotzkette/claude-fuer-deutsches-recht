#!/usr/bin/env python3
"""Prüft native Belege, Zeitstände und Rechnungs-/Ereignisabgleich in Hamburg."""
from pathlib import Path
import csv
from decimal import Decimal, ROUND_HALF_UP
from email import policy
from email.parser import BytesParser
import re
import unittest
import zipfile

from openpyxl import load_workbook
from pypdf import PdfReader
from testakte_file_filter import include_in_working_dump

ROOT=Path(__file__).resolve().parents[1]
CASE=ROOT/'testakten/forderungsmanagement-baeckerei-behaeltertausch-hamburg'
G=CASE/'Grundakte'
N=CASE/'02_Nachlieferung_2026-11-12_und_13'
P=CASE/'01_Gerichtseingang_2026-11-06'


def text(path):return ' '.join(' '.join(p.extract_text() or '' for p in PdfReader(path).pages).split())
def euro(value):return f'{value:,.2f}'.replace(',','~').replace('.',',').replace('~','.')


class HamburgAkte(unittest.TestCase):
    def test_native_documents_and_phase_separation(self):
        originals=[p for p in CASE.rglob('*') if include_in_working_dump(p,CASE) and 'gesamt-pdf' not in p.parts]
        self.assertEqual(len(originals),55)
        self.assertEqual({p.suffix for p in originals},{'.pdf','.eml','.docx','.xlsx','.csv','.png'})
        self.assertFalse(list(CASE.rglob('*.inspect.ndjson')))
        self.assertFalse(any(re.search('klage|gericht|verfuegung|systemticket|zuordnungshistorie',p.name,re.I) for p in G.rglob('*')))
        self.assertFalse(any('Nachlieferung' in p for p in [x.name for x in G.iterdir()]))
        self.assertTrue((P/'01_Klage_2026-10-30.pdf').is_file())
        self.assertIn('QR-71B0',text(G/'03_Behaelteruebergabe_2025-12-29.pdf'))
        self.assertIn('QR-71A9',text(G/'Rechnungen/EW-26-01-1047.pdf'))
        self.assertIn('Kundenwerte vertauscht',text(N/'03_Systemticket_2026-11-12.pdf'))

    def test_events_and_invoice_amounts(self):
        with (N/'07_Fahrzeugereignisse_2026-01_bis_09.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f,delimiter=';'))
        self.assertEqual(len(rows),274);self.assertEqual(len({r['event_id'] for r in rows}),274)
        self.assertEqual(sum(r['standortcode']=='KA-LH' for r in rows),196)
        self.assertEqual(sum(r['standortcode']=='BB-HOF' for r in rows),78)
        total=Decimal(0);paid=Decimal(0)
        for month in range(1,10):
            events=[r for r in rows if int(r['datum'][5:7])==month and r['abrechnung_kunde']=='B1047']
            net=Decimal(120)+48*len(events)+Decimal(sum(int(r['netto_kg']) for r in events))*Decimal('.215')
            vat=(net*Decimal('.19')).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
            gross=net+vat;payment=gross if month<3 else Decimal(800)
            invoice=text(G/f'Rechnungen/EW-26-{month:02}-1047.pdf')
            for value in (net,vat,gross):self.assertIn(euro(value),invoice)
            self.assertTrue(all(r['event_id'] in invoice for r in events))
            bank=text(G/f'Bank/Kontoauszug_2026-{month+1:02}.pdf')
            self.assertIn(euro(payment),bank);self.assertIn(f'EW-26-{month:02}-1047',bank)
            total+=gross;paid+=payment
        self.assertEqual(total,Decimal('34545.22'));self.assertEqual(paid,Decimal('13012.75'))
        claim=' '.join(text(P/'01_Klage_2026-10-30.pdf').split())
        self.assertIn(euro(total-paid),claim)
        self.assertIn('21.532,47',text(P/'05_K13_Kontoaufstellung.pdf'))

    def test_actual_pleading_form(self):
        claim=' '.join(text(P/'01_Klage_2026-10-30.pdf').split())
        for marker in ['VOSSEN & KLINK','Landgericht Hamburg','Sievekingplatz 1','20355 Hamburg','1.1 Zahlung','1.2 Kosten','3.3 Einzelne Forderungen','neun Prozentpunkten','27. Oktober 2026','Dr. Arvid Klink','K1 bis K3']:
            self.assertIn(marker,claim)
        self.assertGreaterEqual(len(PdfReader(P/'01_Klage_2026-10-30.pdf').pages),4)
        self.assertIn('nicht zurückgenommen',BytesParser(policy=policy.default).parsebytes((N/'13_Klaegerkollege_2026-11-13.eml').read_bytes()).get_body().get_content())
        court=text(P/'02_Verfuegung_2026-11-02.pdf')
        for marker in ['Notfrist','zwei Wochen','zwei weiterer Wochen','§ 91 ZPO','§ 708 Nr. 2 ZPO','Anwaltszwang']:
            self.assertIn(marker,court)

    def test_mail_attachments_are_exact_and_not_from_future(self):
        files={p.name:p for p in CASE.rglob('*') if p.is_file()}
        attached=0
        for path in CASE.rglob('*.eml'):
            msg=BytesParser(policy=policy.default).parsebytes(path.read_bytes())
            self.assertTrue(msg['From'] and msg['To'] and msg['Date'] and msg['Message-ID'])
            self.assertTrue(msg.get_body(preferencelist=('plain',)).get_content().strip())
            for part in msg.iter_attachments():
                attached+=1;name=part.get_filename();self.assertIn(name,files)
                self.assertEqual(part.get_payload(decode=True),files[name].read_bytes())
                if G in path.parents:self.assertIn(G,files[name].parents)
        self.assertGreaterEqual(attached,15)

    def test_native_table_roundtrip(self):
        first=load_workbook(G/'16_Produktion_und_Ruecklaeufe.xlsx',data_only=True)
        self.assertEqual(first.sheetnames,['Betriebszahlen']);self.assertEqual(first.active['B7'].value,48120)
        wb=load_workbook(N/'15_Ereignisexport_Disposition.xlsx',data_only=True)
        self.assertEqual(wb.sheetnames,['Ereignisse']);ws=wb.active
        self.assertEqual(ws.max_row,280);self.assertEqual(ws['A7'].value,'EW-01-KA-LH-01')
        self.assertEqual(sum(ws.cell(r,8).value for r in range(7,281)),96380)
        self.assertTrue(ws['B7'].is_date)

    def test_finished_files_have_no_draft_placeholders_or_warning(self):
        forbidden=['Lorem ipsum','[Datum','Musterlösung','Diese Testakte wurde mit KI generiert','\u25a0']
        for path in CASE.rglob('*.pdf'):
            if 'gesamt-pdf' in path.parts:continue
            reader=PdfReader(path);self.assertTrue(reader.pages)
            for page in reader.pages:
                content=page.extract_text() or '';self.assertGreater(len(content.strip()),70)
                for marker in forbidden:self.assertNotIn(marker,content,path)
        for path in CASE.rglob('*.docx'):
            with zipfile.ZipFile(path) as z:
                xml=z.read('word/document.xml').decode()
                self.assertNotIn('Lorem ipsum',xml)
                self.assertIn('Times New Roman',z.read('word/styles.xml').decode())


if __name__=='__main__':unittest.main()

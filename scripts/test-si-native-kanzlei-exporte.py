#!/usr/bin/env python3
"""Begrenzte Exporttests: beA-Kopien und XRechnung-Standardfall.

Keine Versandhandlung. Kein Ersatz für KoSIT-Schematron oder visuelle Prüfung.
--visual-fixture PATH erzeugt drei gezielte PDF-Quellen und die Versandkopien
für eine anschließende visuelle Prüfung; vorhandenes Verzeichnis wird abgewiesen.
"""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile
from xml.sax.saxutils import escape

from pypdf import PdfReader
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT/'ki-native-kanzlei/scripts'
sys.path.insert(0, str(SCRIPTS))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    instance = importlib.util.module_from_spec(spec)
    sys.modules[name] = instance
    spec.loader.exec_module(instance)
    return instance


B = module('si_bea_export', SCRIPTS/'build_anlagenkonvolut.py')
X = module('si_xrechnung_export', SCRIPTS/'xrechnung.py')
F = module('si_testakte_filter', ROOT/'scripts/testakte_file_filter.py')
EXAMPLE = ROOT/'ki-native-kanzlei/assets/xrechnung-beispiel.json'


def make_pdf(path, title, pages=2, wide=False):
    size = landscape(A4) if wide else A4
    c = canvas.Canvas(str(path), pagesize=size, invariant=1)
    c.setAuthor('Klotzkette')
    c.setTitle(title)
    for index in range(pages):
        c.setFont('Times-Roman', 11)
        c.drawString(56, size[1]-80, title)
        c.drawString(56, size[1]-105, f'Seite {index+1} von {pages}. Ausschliesslich fiktive Testunterlagen.')
        c.drawString(56, size[1]-135, 'Der obere Seitenrand bleibt fuer die Anlagenkennzeichnung frei.')
        c.drawString(56, size[1]-165, 'Beleginhalt, Betragsangaben und Seitenfolge muessen unveraendert bleiben.')
        c.drawString(56, 50, f'Pruefwert 208,00 EUR netto; Dokumentseite {index+1}.')
        c.showPage()
    c.save()


def setup_sources(folder):
    incoming = folder/'Quellen'; incoming.mkdir()
    main = folder/'Schriftsatz.pdf'
    make_pdf(main, 'Schriftsatzentwurf - Test', pages=1)
    make_pdf(incoming/'Anlage_K1_Pachtvertrag.pdf', 'Pachtvertrag - K1', pages=2)
    make_pdf(incoming/'Anlage_K2_Abrechnung.pdf', 'Abrechnung - K2', pages=2, wide=True)
    return incoming, main


def run_bea(incoming, main, output, *extra):
    args = ['--eingang', str(incoming), '--ausgang', str(output),
            '--hauptdokument', str(main), '--praefix', 'K', '--datum', '20261007',
            '--gericht', 'Amtsgericht Teststadt', '--aktenzeichen', 'Neueingang', '--strict', *extra]
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        return B.main(args)


def manifest(output):
    return json.loads((output/'intern/Versandmanifest.json').read_text())


class BeaTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)
        self.incoming, self.main = setup_sources(self.folder)

    def test_real_default_export_preserves_originals_pages_and_only_first_stamp(self):
        originals = {p: B.sha256(p) for p in [self.main, *self.incoming.glob('*.pdf')]}
        output = self.folder/'Ausgabe'
        self.assertEqual(run_bea(self.incoming, self.main, output), 0)
        info = manifest(output)
        self.assertFalse(info['metadaten']['stempel_alle_seiten'])
        self.assertEqual(info['metadaten']['dateien'], 3)
        copied_main = output/'versandfertig'/info['metadaten']['hauptdokument']
        self.assertEqual(B.sha256(copied_main), originals[self.main])
        for row in info['anlagen']:
            source = self.incoming/row['quelle']
            result = output/'versandfertig'/row['versanddatei']
            old, new = PdfReader(source), PdfReader(result)
            self.assertEqual(len(old.pages), len(new.pages))
            self.assertEqual(len(new.pages), row['seiten'])
            self.assertIn(row['anlage'], new.pages[0].extract_text())
            self.assertNotIn(row['anlage'], new.pages[1].extract_text())
            for a, b in zip(old.pages, new.pages):
                self.assertIn(a.extract_text().strip(), b.extract_text())
                self.assertEqual(tuple(a.mediabox), tuple(b.mediabox))
        self.assertEqual(originals, {p: B.sha256(p) for p in originals})
        self.assertNotIn('Berliner Gerichtshinweis', (output/'intern/Preflight-Bericht.md').read_text())

    def test_filename_profiles_are_bounded_and_sanitized(self):
        record = B.Anlage(self.main, self.main, 'K', 1, '', 'Ärger / Sonderzeichen: '+('Lange Bezeichnung '*20))
        for profile, limit in [('bund', 84), ('gericht-sicher', 60), ('berlin', 60), ('nrw', 60)]:
            with self.subTest(profile=profile):
                name = B.ausgabe_name_anlage(record, 1, 2, profile, '20261007')
                self.assertLessEqual(len(name), limit)
                self.assertRegex(name, r'^[A-Za-z0-9_-]+\.pdf$')
                self.assertLessEqual(len(B.ausgabe_name_hauptdokument(profile, '20261007', 'K', 'Titel '*40)), limit)
        self.assertEqual(B.MAX_DATEIEN_PRO_NACHRICHT, 1000)
        self.assertEqual(B.MAX_BYTES_PRO_NACHRICHT, 200_000_000)

    def test_input_output_overlap_and_overwrite_are_rejected_before_changes(self):
        digest = B.sha256(self.incoming/'Anlage_K1_Pachtvertrag.pdf')
        for target in [self.incoming, self.incoming/'Unterordner', self.folder]:
            with self.subTest(target=target):
                self.assertEqual(run_bea(self.incoming, self.main, target, '--ueberschreiben'), 2)
        output = self.folder/'Ausgabe'
        self.assertEqual(run_bea(self.incoming, self.main, output), 0)
        before = B.sha256(output/'intern/Versandmanifest.json')
        self.assertEqual(run_bea(self.incoming, self.main, output), 2)
        self.assertEqual(B.sha256(output/'intern/Versandmanifest.json'), before)
        self.assertEqual(B.sha256(self.incoming/'Anlage_K1_Pachtvertrag.pdf'), digest)

    def test_extra_files_count_at_1000_and_stop_at_1001(self):
        extras = self.folder/'Zusatz'; extras.mkdir()
        paths = []
        for index in range(998):
            path = extras/f'Signatur_{index:04d}.p7s'; path.write_bytes(b'TEST')
            paths.append(path)
        args = [item for p in paths[:997] for item in ['--zusatzdatei', str(p)]]
        good = self.folder/'Genau1000'
        self.assertEqual(run_bea(self.incoming, self.main, good, *args), 0)
        self.assertEqual(manifest(good)['metadaten']['dateien'], 1000)
        bad = self.folder/'ZuViele'
        self.assertEqual(run_bea(self.incoming, self.main, bad, *args, '--zusatzdatei', str(paths[-1])), 3)
        self.assertEqual(manifest(bad)['metadaten']['dateien'], 1001)
        self.assertIn('mehr als 1000', (bad/'intern/Preflight-Bericht.md').read_text())
        self.assertTrue(all(p.read_bytes() == b'TEST' for p in paths))

    def test_extra_file_size_included_and_decimal_limit_enforced(self):
        baseline = self.folder/'Basis'; self.assertEqual(run_bea(self.incoming, self.main, baseline), 0)
        base_size = manifest(baseline)['metadaten']['bytes_gesamt']
        extra = self.folder/'Nachrichtentext.pdf'
        # Sparse file: only size is relevant to this boundary test; never parsed as a PDF.
        with extra.open('wb') as stream:
            stream.truncate(200_000_000-base_size)
        exact = self.folder/'Genau200MB'
        self.assertEqual(run_bea(self.incoming, self.main, exact, '--zusatzdatei', str(extra)), 0)
        self.assertEqual(manifest(exact)['metadaten']['bytes_gesamt'], 200_000_000)
        with extra.open('r+b') as stream:
            stream.truncate(extra.stat().st_size+1)
        too_big = self.folder/'ZuGross'
        self.assertEqual(run_bea(self.incoming, self.main, too_big, '--zusatzdatei', str(extra)), 3)
        self.assertEqual(manifest(too_big)['metadaten']['bytes_gesamt'], 200_000_001)
        self.assertIn('überschreitet 200 MB', (too_big/'intern/Preflight-Bericht.md').read_text())

    def test_missing_or_oversized_extra_filename_rejected(self):
        self.assertEqual(run_bea(self.incoming, self.main, self.folder/'Missing', '--zusatzdatei', str(self.folder/'fehlt.xml')), 2)
        for suffix, limit in [('.xml', 84), ('.p7s', 90)]:
            with self.subTest(suffix=suffix):
                extra = self.folder/(('x'*(limit-len(suffix)+1))+suffix); extra.write_bytes(b'TEST')
                output = self.folder/('Lang'+suffix.replace('.', '_'))
                self.assertEqual(run_bea(self.incoming, self.main, output, '--zusatzdatei', str(extra)), 3)
                self.assertIn(f'Grenze von {limit}', (output/'intern/Preflight-Bericht.md').read_text())


class XRechnungTests(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads(EXAMPLE.read_text())

    def rejected(self, data):
        with self.assertRaises((ValueError, ArithmeticError, KeyError)):
            X.build(data)

    def test_real_example_xml_totals_and_draft_state(self):
        root = ET.fromstring(X.build(self.payload))
        self.assertEqual(root.find('cbc:ID', X.NS).text, self.payload['invoice_number'])
        self.assertIn('ENTWURF', root.find('cbc:Note', X.NS).text)
        self.assertEqual(root.find('cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount', X.NS).text, '208.00')
        self.assertEqual(root.find('cac:TaxTotal/cbc:TaxAmount', X.NS).text, '39.52')
        self.assertEqual(root.find('cac:LegalMonetaryTotal/cbc:PayableAmount', X.NS).text, '247.52')
        self.assertIn('xrechnung_3.0', root.find('cbc:CustomizationID', X.NS).text)

    def test_approved_state_needs_actual_review_flag(self):
        self.payload['document_state'] = 'approved'
        self.rejected(self.payload)
        self.payload['legal_reviewed'] = True
        root = ET.fromstring(X.build(self.payload))
        self.assertIsNone(root.find('cbc:Note', X.NS))

    def test_nonstandard_currency_tax_country_and_adjustments_rejected(self):
        for field, value in [('currency','USD'), ('vat_rate',7), ('vat_rate',0), ('schema_version',2), ('document_state','sent')]:
            with self.subTest(field=field, value=value):
                data = copy.deepcopy(self.payload); data[field] = value; self.rejected(data)
        for party in ['supplier','customer']:
            data = copy.deepcopy(self.payload); data[party]['country'] = 'AT'; self.rejected(data)
        for field in ['allowances','prepaid_amount','credit_note','reverse_charge']:
            data = copy.deepcopy(self.payload); data[field] = 0; self.rejected(data)

    def test_dates_and_missing_fields_rejected(self):
        for field, value in [('issue_date','2026-02-30'), ('due_date','2026-10-01'), ('period_end','2026-10-01'), ('period_start','07.10.2026')]:
            with self.subTest(field=field):
                data = copy.deepcopy(self.payload); data[field] = value; self.rejected(data)
        for field in ['invoice_number','buyer_reference','issue_date']:
            data = copy.deepcopy(self.payload); data.pop(field); self.rejected(data)
        self.payload['supplier']['vat_id'] = 'DE000'; self.rejected(self.payload)

    def test_invalid_quantities_prices_duplicates_and_empty_lines_rejected(self):
        for field, values in [('quantity',[-1,0,True,'NaN','Infinity','0.0000001']), ('unit_price_net',[-1,True,'NaN','Infinity','0.0000001']), ('unit_code',['UNKNOWN'])]:
            for value in values:
                with self.subTest(field=field,value=value):
                    data = copy.deepcopy(self.payload); data['lines'][0][field] = value; self.rejected(data)
        data = copy.deepcopy(self.payload); data['lines'].append(copy.deepcopy(data['lines'][0])); self.rejected(data)
        data = copy.deepcopy(self.payload); data['lines'] = []; self.rejected(data)

    def test_bad_iban_and_email_rejected(self):
        self.payload['supplier']['iban'] = 'DE00000000001234567890'; self.rejected(self.payload)
        self.payload = json.loads(EXAMPLE.read_text()); self.payload['customer']['email'] = 'invalid'; self.rejected(self.payload)

    def test_cli_preserves_existing_output_and_does_not_claim_validation(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)/'rechnung.xml'
            args = [sys.executable, str(SCRIPTS/'xrechnung.py'), '--input', str(EXAMPLE), '--output', str(output)]
            first = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertFalse(json.loads(first.stdout)['kosit_validated'])
            digest = B.sha256(output)
            repeat = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(repeat.returncode, 2)
            self.assertEqual(B.sha256(output), digest)


class TestaktenFilterTests(unittest.TestCase):
    @staticmethod
    def document(path, content):
        path.parent.mkdir(parents=True, exist_ok=True)
        # Minimal OOXML content fixture for the export filter, not a delivery DOCX.
        with zipfile.ZipFile(path, 'w') as archive:
            archive.writestr('word/document.xml',
                '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                '<w:body><w:p><w:r><w:t>'+escape(content)+'</w:t></w:r></w:p></w:body></w:document>')

    def test_requested_fields_only_allowed_for_exact_root_document(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)/'si-kanzlei-filterfall'
            authorized = root/'09_Fachlicher_Dokumententwurf.docx'
            self.document(authorized, 'Der Antrag wird am [Datum einsetzen] gestellt. Platzhalter bleiben zur Ergänzung.')
            self.assertTrue(F.include_in_working_dump(authorized, root))
            other = root/'10_Anderer_Entwurf.docx'
            self.document(other, 'Der Antrag wird am [Datum einsetzen] gestellt.')
            self.assertFalse(F.include_in_working_dump(other, root))
            nested = root/'Unterordner'/'09_Fachlicher_Dokumententwurf.docx'
            self.document(nested, 'Der Antrag wird am [Datum einsetzen] gestellt.')
            self.assertFalse(F.include_in_working_dump(nested, root))
            unrelated = Path(temporary)/'anderer-fall'/'09_Fachlicher_Dokumententwurf.docx'
            self.document(unrelated, 'Der Antrag wird am [Datum einsetzen] gestellt.')
            self.assertFalse(F.include_in_working_dump(unrelated, unrelated.parent))
            text_file = root/'09_Fachlicher_Dokumententwurf.txt'
            text_file.write_text('Der Antrag wird am [Datum einsetzen] gestellt.')
            self.assertFalse(F.include_in_working_dump(text_file, root))

    def test_requested_template_does_not_allow_solution_or_meta_content(self):
        with tempfile.TemporaryDirectory() as temporary:
            for index, marker in enumerate(['Musterlösung', 'Erwartungshorizont', 'Prüferhinweis',
                                             'fiktive Testakte', 'Testakte zum Plugin', 'Inhalt folgt']):
                with self.subTest(marker=marker):
                    root = Path(temporary)/f'si-kanzlei-filter-{index}'
                    path = root/'09_Fachlicher_Dokumententwurf.docx'
                    self.document(path, f'[Datum einsetzen]. {marker}: nicht für das Arbeitspaket.')
                    self.assertFalse(F.include_in_working_dump(path, root))

    def test_all_24_real_root_drafts_are_exported(self):
        files = sorted((ROOT/'testakten').glob('si-kanzlei-*/09_Fachlicher_Dokumententwurf.docx'))
        self.assertEqual(len(files), 24)
        for path in files:
            with self.subTest(case=path.parent.name):
                self.assertTrue(F.include_in_working_dump(path, path.parent))


def visual_fixture(folder):
    folder.mkdir(parents=True, exist_ok=False)
    incoming, main = setup_sources(folder)
    output = folder/'Ausgabe'
    result = run_bea(incoming, main, output)
    if result:
        raise RuntimeError(f'Fixture: beA return code {result}')
    info = manifest(output)
    evidence = {'source_hashes': {str(p.relative_to(folder)): B.sha256(p) for p in [main, *incoming.glob('*.pdf')]},
                'output_hashes': {str(p.relative_to(folder)): B.sha256(p) for p in (output/'versandfertig').glob('*.pdf')},
                'generated_pages': sum(len(PdfReader(p).pages) for p in (output/'versandfertig').glob('*.pdf')),
                'visual_review': 'pending', 'manifest': info}
    (folder/'evidence.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'folder':str(folder),'pages':evidence['generated_pages']}, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--visual-fixture':
        visual_fixture(Path(sys.argv[2]))
    else:
        unittest.main()

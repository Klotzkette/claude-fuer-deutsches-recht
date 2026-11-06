#!/usr/bin/env python3
"""Fachliche Exportgrenzen und echte externe Validierung der E-Rechnungen.

Für den zusätzlichen Integrationstest die drei Variablen E_RECHNUNG_MUSTANG_JAR,
E_RECHNUNG_KOSIT_HOME und E_RECHNUNG_JAVA auf eingerichtete lokale Werkzeuge setzen.
Ohne diese Werkzeuge wird die Integration ausdrücklich übersprungen.
"""
from copy import deepcopy
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'e-rechnung-werkstatt'
SCRIPT = PLUGIN / 'werkzeuge/erechnung.py'
spec = importlib.util.spec_from_file_location('erechnung', SCRIPT)
engine = importlib.util.module_from_spec(spec); spec.loader.exec_module(engine)
EXAMPLE = PLUGIN / 'beispiele/rechnungsdaten.json'


class RechnungTests(unittest.TestCase):
    def setUp(self): self.data = json.loads(EXAMPLE.read_text())

    def test_two_rates_and_independent_totals_in_both_syntaxes(self):
        groups, totals = engine.validate(self.data, EXAMPLE.parent)
        self.assertEqual({str(k): str(v) for k, v in groups.items()}, {'19': '850.00', '7': '58.00'})
        self.assertEqual(str(totals['gross']), '1073.56')
        ubl = ET.fromstring(engine.ubl(self.data)); cii = ET.fromstring(engine.cii(self.data))
        self.assertEqual(ubl.findtext('cbc:CustomizationID', namespaces=engine.NS), engine.XR_ID)
        self.assertEqual(ubl.findtext('cac:LegalMonetaryTotal/cbc:PayableAmount', namespaces=engine.NS), '1073.56')
        taxes = ubl.findall('cac:TaxTotal/cac:TaxSubtotal', engine.NS)
        self.assertEqual({x.findtext('cbc:TaxAmount', namespaces=engine.NS) for x in taxes}, {'4.06', '161.50'})
        self.assertEqual(cii.findtext('.//ram:DuePayableAmount', namespaces=engine.NS), '1073.56')
        self.assertEqual(len(cii.findall('.//ram:IncludedSupplyChainTradeLineItem', engine.NS)), 2)

    def test_wrong_totals_and_unsupported_cases_are_not_silently_converted(self):
        mutations = [lambda d: d['totals'].update(payable='0.01'),
                     lambda d: d.update(prepaid_amount='10.00'),
                     lambda d: d.update(invoice_type='381'),
                     lambda d: d.update(currency='USD'),
                     lambda d: d['lines'][0].update(vat_rate='0'),
                     lambda d: d['lines'][0].update(tax_category='AE'),
                     lambda d: d['lines'][0].update(quantity='-1'),
                     lambda d: d['lines'][0].update(quantity='NaN'),
                     lambda d: d['lines'][0].update(unit_price_net=85.0),
                     lambda d: d.update(schema_version=True),
                     lambda d: d.update(reviewed=False),
                     lambda d: d['supplier'].update(iban='DE79000000001234567891')]
        for change in mutations:
            data = deepcopy(self.data); change(data)
            with self.subTest(data=data), self.assertRaises(ValueError): engine.validate(data)

    def test_sources_and_field_mapping_are_required_and_hash_checked(self):
        engine.validate(self.data, EXAMPLE.parent)
        for mode in ('hash', 'escape', 'missing_evidence', 'unknown_source', 'unknown_field'):
            data = deepcopy(self.data)
            if mode == 'hash': data['sources'][0]['sha256'] = '0' * 64
            if mode == 'escape': data['sources'][0]['file'] = '../../README.md'
            if mode == 'missing_evidence': data['evidence'].pop()
            if mode == 'unknown_source': data['evidence'][0]['source_id'] = 'UNBEKANNT'
            if mode == 'unknown_field': data['evidence'][0]['field'] = 'zusatzfeld'
            with self.subTest(mode=mode), self.assertRaises(ValueError): engine.validate(data, EXAMPLE.parent)

    def test_duplicate_json_keys_and_nonfinite_constants_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'input.json'
            for raw in ('{"invoice_number":"A","invoice_number":"B"}', '{"value":NaN}', '{"value":Infinity}'):
                path.write_text(raw)
                with self.subTest(raw=raw), self.assertRaises(ValueError): engine.json_read(path)

    def test_pdf_guard_rejects_previous_false_green_behavior(self):
        positive = '''<?xml version="1.0"?><validation><pdf>ValidationResult [flavour=3u, totalAssertions=25838, assertions=[], isCompliant=true]<summary status="valid"/></pdf><xml><messages/><summary status="valid"/></xml><messages/><summary status="valid"/></validation>'''
        engine.mustang_report(positive, require_pdf=True)
        negatives = [positive.replace('isCompliant=true', 'isCompliant=false'),
                     positive.replace('assertions=[]', 'assertions=[failed]'),
                     positive.replace('totalAssertions=25838', 'totalAssertions=0'),
                     positive.replace('flavour=3u', 'flavour=2b'),
                     positive.replace('<messages/>', '<messages><warning>PDF/A failed</warning></messages>', 1),
                     positive.replace('<pdf>', '<pdf><warning>PDF/A failed</warning>', 1),
                     positive.replace('ValidationResult [flavour=3u, totalAssertions=25838, assertions=[], isCompliant=true]', ''),
                     positive.replace('<xml><messages/>', '<xml><messages><error>BR-CO-16</error></messages>')]
        for raw in negatives:
            with self.subTest(raw=raw), self.assertRaises(ValueError): engine.mustang_report(raw, require_pdf=True)

    def test_existing_destination_and_wrong_runtime_are_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp); out = folder / 'existing'; out.mkdir()
            keep = out / 'keep.txt'; keep.write_text('UNVERÄNDERT')
            jar = folder / 'fake.jar'; jar.write_bytes(b'not Mustang')
            with self.assertRaisesRegex(ValueError, 'Ausgabeverzeichnis'):
                engine.create(EXAMPLE, out, 'zugferd', jar, 'java')
            self.assertEqual(keep.read_text(), 'UNVERÄNDERT')
            new = folder / 'new'
            with self.assertRaisesRegex(ValueError, 'SHA-256'):
                engine.create(EXAMPLE, new, 'zugferd', jar, 'java')
            self.assertFalse(new.exists())

    def test_input_changed_during_backend_run_is_not_certified(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp); source = folder / 'rechnungsdaten.json'
            source.write_bytes(EXAMPLE.read_bytes())
            (folder / 'rechnungsquelle.txt').write_bytes((EXAMPLE.parent / 'rechnungsquelle.txt').read_bytes())
            jar = folder / 'fake.jar'; jar.write_bytes(b'mocked backend only')
            def changed(*unused):
                source.write_bytes(source.read_bytes() + b'\n')
            with patch.object(engine, 'MUSTANG_SHA256', sha256(jar.read_bytes()).hexdigest()), \
                    patch.object(engine, 'kosit_validate', side_effect=changed):
                with self.assertRaisesRegex(ValueError, 'während der Erstellung geändert'):
                    engine.create(source, folder / 'output', 'xrechnung', jar, 'java', folder)
            self.assertFalse((folder / 'output').exists())
            diagnostics = list(folder.glob('.output-*/FEHLGESCHLAGEN.txt'))
            self.assertEqual(len(diagnostics), 1)
            self.assertIn('NICHT FREIGEGEBEN', diagnostics[0].read_text())

    def test_layout_preserves_price_precision_and_groups_rates_numerically(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            self.data['lines'][0].update(quantity='2', unit_price_net='29.123456')
            self.data['totals'].update(net='116.25', tax='15.13', gross='131.38', payable='131.38')
            engine.validate(self.data)
            fo, config = engine.write_layout(self.data, folder / 'fake.jar', folder)
            visible = ' '.join(ET.parse(fo).getroot().itertext())
            self.assertIn('29,123456', visible)
            self.assertIn('58,25', visible)
            self.assertNotIn('Leitweg-ID', visible)
            self.assertIn('Kundenreferenz: BEST-2026-1042', visible)
            self.data['lines'][0].update(quantity='1', unit_price_net='0.05', vat_rate='7')
            self.data['lines'][1].update(quantity='1', unit_price_net='0.05', vat_rate='07')
            self.data['totals'].update(net='0.10', tax='0.01', gross='0.11', payable='0.11')
            engine.validate(self.data)
            fo, unused = engine.write_layout(self.data, folder / 'fake.jar', folder)
            visible = ' '.join(ET.parse(fo).getroot().itertext())
            self.assertEqual(visible.count('Umsatzsteuer 7 %'), 1)
            self.assertIn('0,01', visible)

    def test_renderer_warnings_block_release(self):
        with tempfile.TemporaryDirectory() as temp:
            log = Path(temp) / 'render.log'
            log.write_text('[main] INFO Rendered page #1')
            engine.layout_log_check(log)
            for message in ('WARN Content overflows the viewport', 'Glyph test not available in font',
                            'Font SourceSansPro substituted with Helvetica', 'ERROR invalid FO'):
                log.write_text(message)
                with self.subTest(message=message), self.assertRaises(ValueError): engine.layout_log_check(log)

    @unittest.skipUnless(all(os.environ.get(k) for k in ('E_RECHNUNG_MUSTANG_JAR', 'E_RECHNUNG_KOSIT_HOME', 'E_RECHNUNG_JAVA')),
                         'Echte lokale Java-/Mustang-/KoSIT-Umgebung nicht konfiguriert')
    def test_real_schema_schematron_and_pdfa_with_corrupted_counterexamples(self):
        jar = Path(os.environ['E_RECHNUNG_MUSTANG_JAR']).resolve()
        home = Path(os.environ['E_RECHNUNG_KOSIT_HOME']).resolve()
        java = os.environ['E_RECHNUNG_JAVA']
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp); out = folder / 'output'
            result = engine.create(EXAMPLE, out, 'both', jar, java, home)
            self.assertEqual(result['state'], 'generated_and_validated_not_sent')
            self.assertTrue(result['results']['ZUGFeRD.pdf']['pdfa_valid'])
            self.assertEqual(result['generator_sha256'], sha256(SCRIPT.read_bytes()).hexdigest())
            self.assertEqual(result['input_sha256'], sha256(EXAMPLE.read_bytes()).hexdigest())
            self.assertEqual(result['runtime_lock_sha256'], sha256(SCRIPT.with_name('runtime-lock.json').read_bytes()).hexdigest())
            self.assertEqual(result['layout_sha256'], sha256(SCRIPT.with_name('rechnung_layout.py').read_bytes()).hexdigest())
            # A syntactically correct XML with wrong actual payable must be rejected by KoSIT.
            broken = ET.parse(out / 'XRechnung.xml')
            broken.find('cac:LegalMonetaryTotal/cbc:PayableAmount', engine.NS).text = '0.01'
            bad = folder / 'wrong-payable.xml'; broken.write(bad, encoding='utf-8', xml_declaration=True)
            rejected = folder / 'negative-xml'; rejected.mkdir()
            with self.assertRaises(ValueError): engine.kosit_validate(bad, home, java, rejected)
            report = (rejected / 'kosit/wrong-payable-report.xml').read_text()
            self.assertIn('BR-CO-16', report)
            self.assertEqual(ET.fromstring(report).get('valid'), 'false')
            # PDF/A remains mandatory even if the embedded invoice XML is valid.
            from pypdf import PdfReader, PdfWriter
            writer = PdfWriter(); writer.clone_document_from_reader(PdfReader(out / 'ZUGFeRD.pdf'))
            metadata = writer.xmp_metadata; metadata.pdfaid_part = '2'; writer.xmp_metadata = metadata
            corrupt = folder / 'wrong-pdfa.pdf'
            with corrupt.open('wb') as stream: writer.write(stream)
            command = [java, '-jar', str(jar), '--disable-file-logging', '--action', 'validate', '--source', str(corrupt)]
            process = subprocess.run(command, capture_output=True, text=True, timeout=180, cwd=folder)
            with self.assertRaises(ValueError): engine.mustang_report(process.stdout, require_pdf=True)


if __name__ == '__main__': unittest.main(verbosity=2)

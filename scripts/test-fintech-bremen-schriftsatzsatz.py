#!/usr/bin/env python3
"""Form, echter PDF-Empfängerbereich und Bestandsschutz der Weserfunken-Schriftsätze."""
import argparse
import hashlib
import json
import re
import tempfile
import unittest
from pathlib import Path
from docx import Document
from pypdf import PdfReader
from fintech_schriftsatz_satz import approved_original_hashes, pdf

ROOT=Path(__file__).resolve().parents[1]
FIX=ROOT/'scripts/fixtures/fintech-bremen'
CASE=ROOT/'testakten/fintech-darlehen-vertragsuebernahme-bremen'
MIGRATION=json.loads((FIX/'satz-migration-2026-11.json').read_text())
FACTS=json.loads((FIX/'case.json').read_text())

def norm(text):return ' '.join(text.split())
def form_errors(text,headings):
    errors=[]
    for value in ['Landgericht Bremen','Domsheide 16','28195 Bremen','Klägerin','Beklagte']:
        if value not in text:errors.append('Formangabe fehlt: '+value)
    if not any(re.match(r'^\d+\.\d+ ',h) for h in headings):errors.append('Mehrstufige Dezimalgliederung fehlt')
    if not any(h=='1 Anträge' for h in headings):errors.append('Vorangestellter Antragsabschnitt fehlt')
    return errors

class Schriftsatzsatz(unittest.TestCase):
    def test_actual_old_pdf_and_flat_headings_are_rejected(self):
        old=json.loads((FIX/'satz-regression-before.json').read_text())
        self.assertEqual(old['sha256'],MIGRATION['files']['01_eingang/01_Klage_20260908.pdf']['before_sha256'])
        errors=form_errors(old['first_page_text'],old['headings'])
        self.assertIn('Formangabe fehlt: Domsheide 16',errors)
        self.assertIn('Mehrstufige Dezimalgliederung fehlt',errors)
        self.assertIn('Vorangestellter Antragsabschnitt fehlt',errors)

    def test_generated_claim_recipient_area_and_requests(self):
        source=json.loads((FIX/'claim.json').read_text())['documents'][0]
        reader=PdfReader(CASE/'01_eingang/01_Klage_20260908.pdf')
        text='\n'.join(p.extract_text() for p in reader.pages)
        self.assertEqual(form_errors(text,[s['heading'] for s in source['pages']]),[])
        recipient=[]
        def visit(value,cm,tm,font,size):
            if 55<=tm[4]+cm[4]<=540 and 530<=tm[5]+cm[5]<=716:
                recipient.append(value)
        reader.pages[0].extract_text(visitor_text=visit)
        recipient=norm(' '.join(recipient))
        for line in ['Landgericht Bremen','4. Zivilkammer','Domsheide 16','28195 Bremen']:
            self.assertIn(line,recipient)
        first=reader.pages[0].extract_text()
        self.assertIn('TETTENBORN',first)
        self.assertIn('Contrescarpe 82',first)
        self.assertIn('kanzlei@tettenborn.example',first)
        self.assertNotIn('per beA',text)
        self.assertLess(text.index('1.1.1 Die Beklagte'),text.index('2 Parteien und Zulässigkeit'))
        for number in ['1.3.1','1.3.2','1.3.3','1.3.4','1.3.5','1.4.1','1.4.2']:
            self.assertIn(number+' ',text)
        self.assertIn('590.000,00 EUR',text);self.assertIn('515.000,00 EUR',text);self.assertIn('68.000,00 EUR',text)
        for n,page in enumerate(reader.pages,1):
            self.assertIn(f'Seite {n} von 18',page.extract_text())
            self.assertGreater(len(page.extract_text()),500)
        self.assertEqual(len(reader.pages),18)

    def test_sachvortrag_is_not_shortened_or_silently_corrected(self):
        for name,minimum in [('claim',95),('defence',80)]:
            d=json.loads((FIX/(name+'.json')).read_text())['documents'][0]
            corpus=MIGRATION['substantive_text_preservation'][name]
            actual={hashlib.sha256(norm(p).encode()).hexdigest() for s in d['pages'] for p in s['paragraphs']}
            self.assertGreaterEqual(len(corpus['paragraphs']),minimum)
            self.assertTrue({p['after_sha256'] for p in corpus['paragraphs']}<=actual)
            headings=[s['heading'].split(' ',1)[0] for s in d['pages']]
            self.assertEqual(len(headings),len(set(headings)))
            for h in headings:
                self.assertRegex(h,r'^\d+(?:\.\d+)*$')
                if '.' in h:self.assertIn(h.rsplit('.',1)[0],headings)
        claim=json.loads((FIX/'claim.json').read_text())['documents'][0]
        self.assertIn('Einziehung und wirtschaftliche Zuordnung zur Beklagten',json.dumps(claim,ensure_ascii=False))
        defence=json.loads((FIX/'defence.json').read_text())['documents'][0]
        text=json.dumps(defence,ensure_ascii=False)
        self.assertNotRegex(text,r'Antr(?:ag|äge) 22\.|Hilfsanträge 23\.')
        self.assertIn('Antrag 1.3.3',text)
        self.assertIn('Ziffer 3.4 der Klage',text)

    def test_word_is_native_with_real_heading_styles_and_page_fields(self):
        doc=Document(CASE/'02_klageerwiderung/00_Klageerwiderung_20260928.docx')
        text='\n'.join(p.text for p in doc.paragraphs)
        for line in ['RADEMACHER WESTHOFF','Am Wall 146','Domsheide 16','28195 Bremen','westhoff@rw-kanzlei.example']:
            self.assertIn(line,text)
        self.assertTrue(any(p.style.name=='Heading 2' and p.text.startswith('4.6 ') for p in doc.paragraphs))
        self.assertEqual(doc.styles['Normal'].font.name,'Times New Roman')
        self.assertEqual(doc.styles['Normal'].font.size.pt,11)
        self.assertIn('NUMPAGES',doc.sections[0].footer._element.xml)
        self.assertIn('PAGE',doc.sections[0].first_page_footer._element.xml)

    def test_only_five_originals_have_documented_migration(self):
        self.assertEqual(len(MIGRATION['files']),5)
        expected=approved_original_hashes(FIX/'anfechtung-original42-sha256.json')
        baseline=json.loads((FIX/'anfechtung-original42-sha256.json').read_text())
        self.assertEqual(len(expected),42)
        self.assertEqual(sum(expected[p]==baseline[p] for p in baseline),37)
        for name,digest in expected.items():self.assertEqual(hashlib.sha256((CASE/name).read_bytes()).hexdigest(),digest,name)
        for name,values in MIGRATION['files'].items():
            self.assertNotEqual(values['before_sha256'],values['after_sha256'])
            self.assertTrue(values['reason'])

    def test_stored_pdfs_embed_true_times_new_roman_for_all_visible_text(self):
        for name in ['01_eingang/01_Klage_20260908.pdf', '03_korrespondenz/00_Verteidigungsanzeige_20260922.pdf']:
            used=set()
            for page in PdfReader(CASE/name).pages:
                def visit(text,cm,tm,font,size):
                    if text.strip():
                        self.assertIsNotNone(font)
                        self.assertIn('TimesNewRoman',str(font['/BaseFont']))
                        used.add(str(font['/BaseFont']))
                        descriptor=font['/FontDescriptor'].get_object()
                        self.assertGreater(len(descriptor['/FontFile2'].get_object().get_data()),1000)
                page.extract_text(visitor_text=visit)
            self.assertGreaterEqual(len(used),2)

    def test_renderer_reproduces_claim_without_hidden_font_substitution(self):
        source=json.loads((FIX/'claim.json').read_text())['documents'][0]
        with tempfile.TemporaryDirectory() as work:
            path=Path(work)/'claim.pdf';pdf(source,FACTS,path)
            self.assertEqual(path.read_bytes(),(CASE/'01_eingang/01_Klage_20260908.pdf').read_bytes())
            for page in PdfReader(path).pages:
                for ref in page['/Resources']['/Font'].values():
                    font=ref.get_object()
                    if '/FontDescriptor' in font:
                        self.assertIn('TimesNewRoman',str(font['/BaseFont']))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--read-only', action='store_true', help='Sechs Bestandsprüfungen ohne Renderer; benötigt keine lokal installierten Schriftdateien.')
    args=parser.parse_args()
    loader=unittest.TestLoader()
    names=loader.getTestCaseNames(Schriftsatzsatz)
    if args.read_only:
        names.remove('test_renderer_reproduces_claim_without_hidden_font_substitution')
    suite=unittest.TestSuite(Schriftsatzsatz(name) for name in names)
    unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() or __import__('sys').exit(1)

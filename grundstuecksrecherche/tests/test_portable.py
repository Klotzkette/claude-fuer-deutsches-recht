from io import BytesIO
import json
from pathlib import Path
import re
import sys
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'app'))
from portable import build_website, json_script


def case_data():
    return {'case_id': 'VERTRAULICH-4711', 'sender_organisation': 'VERTRAULICH-Absender',
            'purpose': 'VERTRAULICH-Zweck', 'recipients': {'kataster': 'VERTRAULICH-Empfänger'},
            'profile': {'profile_id': 'intern', 'name': 'Münster', 'state': 'Nordrhein-Westfalen',
                        'municipality_code': '05515000', 'center': [51.9607, 7.6261],
                        'bounds': [7.45, 51.8, 7.85, 52.1], 'warnings': ['VERTRAULICH-Notiz']},
            'selected_parcels': [{'numerator': '71', 'municipality': 'Münster',
                                  'identification_status': 'manuell_ergaenzt'}]}


class PortableWebsiteTests(unittest.TestCase):
    def contents(self, case=None, include_case=False):
        with zipfile.ZipFile(BytesIO(build_website(case, include_case=include_case))) as archive:
            self.assertEqual(archive.testzip(), None)
            self.assertEqual(len(archive.namelist()), len(set(archive.namelist())))
            return {name: archive.read(name) for name in archive.namelist()}

    def test_root_index_and_all_local_dependencies(self):
        files = self.contents()
        html = files['index.html'].decode()
        refs = re.findall(r'(?:src|href)="\./([^"]+)"', html)
        self.assertGreaterEqual(len(refs), 9)
        for name in refs:
            self.assertIn(name, files)
        self.assertIn('README.txt', files)
        self.assertIn('Content-Security-Policy', html)
        self.assertNotIn('src="/', html)
        self.assertNotIn('href="/', html)
        self.assertNotIn("script-src 'unsafe-inline'", html)
        self.assertFalse(any(name.startswith('/') or '..' in name.split('/') for name in files))

    def test_no_private_case_fields_without_opt_in(self):
        files = self.contents(case_data())
        bundle = files['portable-bundle.js'].decode()
        self.assertNotIn('VERTRAULICH', bundle)
        parsed = json.loads(bundle.removeprefix('window.PORTABLE_BUNDLE=').strip().removesuffix(';'))
        self.assertIsNone(parsed['case'])
        self.assertEqual(parsed['profile']['name'], 'Münster')
        self.assertNotIn('warnings', parsed['profile'])
        self.assertNotIn('profile_id', parsed['profile'])
        self.assertNotIn('authority_profiles', parsed['catalogs'])
        self.assertIn(b'No case data', files['README.txt'])

    def test_explicit_case_inclusion_and_source_unchanged(self):
        case = case_data()
        before = json.dumps(case, ensure_ascii=False)
        files = self.contents(case, True)
        self.assertIn('VERTRAULICH-Absender', files['portable-bundle.js'].decode())
        self.assertIn(b'Includes case data', files['README.txt'])
        self.assertEqual(before, json.dumps(case, ensure_ascii=False))

    def test_empty_start_and_determinism(self):
        self.assertEqual(build_website(), build_website())
        self.assertIn(b'"profile":null,"case":null', self.contents()['portable-bundle.js'])

    def test_explicit_boolean_and_schema_required(self):
        for invalid in ('false', 1, None, []):
            with self.assertRaises(ValueError):
                build_website(case_data(), include_case=invalid)
        with self.assertRaises(ValueError):
            build_website({}, include_case=True)
        with self.assertRaises(ValueError):
            build_website([])
        with self.assertRaises(ValueError):
            build_website({'unexpected': 'value'})

    def test_json_string_cannot_inject_script(self):
        value = {'text': '</script><script>alert(1)</script>\u2028&'}
        escaped = json_script(value)
        self.assertNotIn('<', escaped)
        self.assertNotIn('&', escaped)
        self.assertEqual(json.loads(escaped), value)


if __name__ == '__main__':
    unittest.main()

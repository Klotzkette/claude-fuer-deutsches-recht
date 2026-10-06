import hashlib
import json
from pathlib import Path
import unittest


class ReferenceTests(unittest.TestCase):
    def test_supplied_reference_is_unchanged(self):
        root = Path(__file__).resolve().parents[1] / 'examples/nrw-muenster'
        manifest = json.loads((root / 'reference-integrity.json').read_text())
        files = {str(p.relative_to(root / 'reference')): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in (root / 'reference').rglob('*') if p.is_file()}
        self.assertEqual(files, manifest['files'])


if __name__ == '__main__':
    unittest.main()

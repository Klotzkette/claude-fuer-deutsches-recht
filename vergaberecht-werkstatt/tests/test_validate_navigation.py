from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
SCRIPT = ROOT / "scripts" / "validate-navigation.py"
SPEC = importlib.util.spec_from_file_location("validate_navigation", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
navigation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(navigation)


class NavigationParserTests(unittest.TestCase):
    def test_only_navigable_markdown_links_are_returned(self) -> None:
        text = """
[Direkt](./01_akte.md "Aktenstück")
[Fragment](02_akte.md#fundstelle)
[Kodiert](<03%5Fakte.md>)
![Bild](04_akte.md)
<!-- [Kommentar](05_akte.md) -->

```markdown
[Codebeispiel](06_akte.md)
```
"""

        self.assertEqual(
            navigation.markdown_link_targets(text),
            {"./01_akte.md", "02_akte.md", "03_akte.md"},
        )

    def test_numbered_case_docs_accepts_more_than_two_digits(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            for name in ("01_start.md", "99_fortsetzung.md", "100_anlage.md", "README.md"):
                (directory / name).touch()

            self.assertEqual(
                [path.name for path in navigation.numbered_case_docs(directory)],
                ["01_start.md", "99_fortsetzung.md", "100_anlage.md"],
            )


if __name__ == "__main__":
    unittest.main()

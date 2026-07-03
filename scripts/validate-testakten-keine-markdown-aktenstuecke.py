#!/usr/bin/env python3
"""Validator: Aktenstuecke in Testakten duerfen nicht als Markdown vorliegen.

Grundregel aus testakten/QUALITAETSSTANDARD.md: Der Akten-ZIP-Export soll ein
lebensechter Formatemix sein (DOCX, PDF, XLSX, EML, JPG, TXT, CSV). Markdown
ist nur fuer README, rubric und Meta-/Loesungsdateien erlaubt, die der
testakte_file_filter ohnehin vom Export ausschliesst.
Exit 0 = sauber; Exit 1 = Verstoesse (werden gelistet).
"""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from testakte_file_filter import is_export_meta_file

ROOT = Path(__file__).resolve().parent.parent / "testakten"
SKIP = {"megaprompts", "formatvorlagen-paradebeispiele"}

def main() -> int:
    bad: list[str] = []
    for d in sorted(ROOT.iterdir()):
        if not d.is_dir() or d.name in SKIP:
            continue
        for p in d.rglob("*.md"):
            if "gesamt-pdf" in p.parts:
                continue
            if is_export_meta_file(p, d):
                continue
            bad.append(str(p.relative_to(ROOT.parent)))
    if bad:
        print(f"FEHLER: {len(bad)} Markdown-Aktenstueck(e) gefunden (Grundregel: native Formate):")
        for b in bad[:40]:
            print("  -", b)
        return 1
    print("validate-testakten-keine-markdown-aktenstuecke OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

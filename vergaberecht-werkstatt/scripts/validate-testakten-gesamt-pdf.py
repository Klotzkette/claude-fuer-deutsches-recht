#!/usr/bin/env python3
"""Validiert die Gesamt-PDF-Regel fuer Testakten.

Jede testakten/<slug>/ Akte muss genau das Standard-Gesamt-PDF
gesamt-pdf/<slug>_gesamt.pdf enthalten. Das PDF muss groesser als 1 KB sein,
mit %PDF beginnen, ein EOF-Marker haben und im README verlinkt sein.

Der Check nutzt nur die Python-Standardbibliothek, damit er in GitHub Actions
ohne zusaetzliche PDF-Abhaengigkeiten laeuft.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = ROOT / "testakten"

# Hilfsmaterial-Ordner unterhalb testakten/ ohne Akten-Struktur.
# Diese enthalten Formatvorlagen / Megaprompt-Material, keine Mandatsakten,
# und sind daher von der Gesamt-PDF-Pflicht ausgenommen.
SKIP_DIRS = {
    "formatvorlagen-paradebeispiele",
    "megaprompts",
}


def fs_path(path: Path) -> Path:
    """Return a Windows long-path-safe Path without changing display paths."""
    if sys.platform != "win32":
        return path
    resolved = str(path.resolve())
    if resolved.startswith("\\\\?\\"):
        return Path(resolved)
    if resolved.startswith("\\\\"):
        return Path("\\\\?\\UNC\\" + resolved[2:])
    return Path("\\\\?\\" + resolved)


def path_exists(path: Path) -> bool:
    return fs_path(path).exists()


def read_bytes(path: Path) -> bytes:
    return fs_path(path).read_bytes()


def read_text(path: Path) -> str:
    return fs_path(path).read_text(encoding="utf-8", errors="replace")


def is_probable_pdf(path: Path) -> str | None:
    data = read_bytes(path)
    if len(data) < 1024:
        return "PDF ist kleiner als 1 KB"
    if not data.startswith(b"%PDF"):
        return "PDF beginnt nicht mit %PDF"
    if b"%%EOF" not in data[-4096:]:
        return "PDF hat keinen EOF-Marker im Dateiende"
    if b"/Type /Page" not in data:
        return "PDF enthaelt keine Page-Marker"
    return None


def main() -> int:
    errors: list[str] = []
    dirs = sorted(d for d in TESTAKTEN.iterdir() if d.is_dir() and d.name not in SKIP_DIRS)
    for d in dirs:
        slug = d.name
        pdf = d / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        gesamt_dir = d / "gesamt-pdf"
        if not path_exists(pdf):
            errors.append(f"{slug}: fehlt {pdf.relative_to(ROOT)}")
            continue
        extra_pdfs = []
        if path_exists(gesamt_dir):
            extra_pdfs = sorted(p for p in gesamt_dir.glob("*.pdf") if p != pdf)
        if extra_pdfs:
            listed = ", ".join(str(p.relative_to(ROOT)) for p in extra_pdfs)
            errors.append(f"{slug}: zusaetzliche Gesamt-PDFs gefunden: {listed}")
        problem = is_probable_pdf(pdf)
        if problem:
            errors.append(f"{slug}: {problem}: {pdf.relative_to(ROOT)}")
        readme_candidates = [d / "README.md"] + sorted(d.glob("00_*.md")) + sorted(d.glob("aktenuebersicht*.md"))
        readme = next((p for p in readme_candidates if path_exists(p)), None)
        if readme:
            text = read_text(readme)
            rel = f"gesamt-pdf/{slug}_gesamt.pdf"
            if rel not in text:
                errors.append(f"{slug}: {readme.name} verlinkt {rel} nicht")
        else:
            errors.append(f"{slug}: README.md / 00_*.md / aktenuebersicht*.md fehlt")

    if errors:
        print("validate-testakten-gesamt-pdf: FEHLER", file=sys.stderr)
        for err in errors:
            print(f" - {err}", file=sys.stderr)
        return 1

    print(f"validate-testakten-gesamt-pdf OK ({len(dirs)} Testakten)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

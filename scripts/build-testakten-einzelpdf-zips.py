#!/usr/bin/env python3
"""Baut pro Testakte ein ZIP, das jede Unterlage als eigene PDF enthaelt.

Anders als das Gesamt-PDF (alles in einem Dokument) liefert dieses ZIP jede
Akte-Unterlage als separate, sauber gerenderte PDF-Datei. Original-PDFs werden
unveraendert uebernommen, alle anderen Dokumente (MD/TXT/EML/CSV/XLSX/DOCX/ODT
und Bilder) in jeweils eine eigene PDF gerendert. Die Ordnerstruktur der Akte
bleibt erhalten.

Aufruf:
  python3 scripts/build-testakten-einzelpdf-zips.py [dist]            # alle Testakten
  python3 scripts/build-testakten-einzelpdf-zips.py [dist] <name> ... # gezielt

Erzeugt:
  <dist>/testakte-<name>-einzelpdfs.zip   (pro Testakte)
  <dist>/alle-testakten-einzelpdfs.zip    (Sammel-ZIP)
"""

from __future__ import annotations

import importlib.util
import io
import sys
import zipfile
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from testakte_einzelpdf_common import (
    COPY_EXTS,
    IMAGE_EXTS,
    document_arcname_pairs,
    ext_of,
)

SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parent
TESTAKTEN = REPO_ROOT / "testakten"


def _load_gesamt_module():
    """Laedt das Gesamt-PDF-Skript (Dateiname mit Bindestrichen) als Modul,
    um dessen erprobte Konverter wiederzuverwenden."""
    path = SCRIPTS / "build-testakte-gesamt-pdf.py"
    spec = importlib.util.spec_from_file_location("build_testakte_gesamt_pdf", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


G = _load_gesamt_module()


def odt_to_flowables(path: Path) -> list:
    """Rendert ODT-Text in Flowables. Nutzt odfpy, faellt sonst auf Hinweis."""
    out: list = []
    try:
        from odf.opendocument import load as odf_load
        from odf.element import Element
    except ImportError:
        out.append(Paragraph("<i>odfpy nicht installiert, ODT-Inhalt uebersprungen.</i>", G.s_meta))
        return out
    try:
        doc = odf_load(str(path))
    except Exception as e:  # pragma: no cover - defekte Datei
        out.append(Paragraph(f"<i>ODT konnte nicht gelesen werden: {G.escape(str(e))}</i>", G.s_meta))
        return out

    def text_of(node) -> str:
        parts: list[str] = []
        for child in node.childNodes:
            if child.nodeType == child.TEXT_NODE:
                parts.append(child.data)
            elif isinstance(child, Element):
                parts.append(text_of(child))
        return "".join(parts)

    def walk(node) -> None:
        """Durchlaeuft den Baum in Dokumentreihenfolge und gibt Absaetze/
        Ueberschriften aus, sobald sie auftreten (erhaelt die Reihenfolge)."""
        for child in node.childNodes:
            if not isinstance(child, Element):
                continue
            local = child.qname[1]
            if local in ("p", "h"):
                txt = text_of(child).strip()
                if txt:
                    out.append(Paragraph(G.escape(txt), G.s_h3 if local == "h" else G.s_body))
            else:
                walk(child)

    walk(doc.text)
    if not out:
        out.append(Paragraph("<i>ODT enthielt keinen lesbaren Text.</i>", G.s_meta))
    return out


def render_document_pdf(path: Path, testakte_dir: Path) -> bytes | None:
    """Rendert eine Einzeldatei in eine PDF und liefert die Bytes.

    Original-PDFs werden unveraendert zurueckgegeben.
    """
    ext = ext_of(path)
    if ext in COPY_EXTS:
        return path.read_bytes()

    rel = path.relative_to(testakte_dir)
    flow: list = [Paragraph(f"<b>Datei:</b> {G.escape(str(rel))}", G.s_meta), Spacer(1, 6)]
    try:
        if ext == "md":
            flow.extend(G.md_to_flowables(path.read_text(encoding="utf-8", errors="replace")))
        elif ext == "txt":
            flow.extend(G.txt_to_flowables(path.read_text(encoding="utf-8", errors="replace")))
        elif ext == "eml":
            flow.extend(G.eml_to_flowables(path))
        elif ext == "csv":
            flow.extend(G.csv_to_flowables(path))
        elif ext == "xlsx":
            flow.extend(G.xlsx_to_flowables(path))
        elif ext == "docx":
            flow.extend(G.docx_to_flowables(path))
        elif ext == "odt":
            flow.extend(odt_to_flowables(path))
        elif ext in IMAGE_EXTS:
            flow.extend(G.image_to_flowables(path))
        else:  # pragma: no cover - durch is_einzelpdf_document ausgeschlossen
            return None
    except Exception as e:
        flow.append(Paragraph(f"<i>Inhalt konnte nicht gerendert werden: {G.escape(str(e))}</i>", G.s_meta))

    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
        title=f"{testakte_dir.name} — {rel}", author="Kanzleiakte",
    )
    hf = G.header_footer_factory(testakte_dir.name)
    try:
        doc.build(flow, onFirstPage=hf, onLaterPages=hf)
    except Exception as e:
        print(f"    FEHLER beim Rendern von {rel}: {e}")
        return None
    return buf.getvalue()


def add_testakte(zipf: zipfile.ZipFile, testakte_dir: Path) -> int:
    count = 0
    for path, arcname in document_arcname_pairs(testakte_dir):
        data = render_document_pdf(path, testakte_dir)
        if data is None:
            continue
        zipf.writestr(arcname, data)
        count += 1
    return count


def build_single(testakte_dir: Path, dist: Path) -> tuple[Path, int]:
    out = dist / f"testakte-{testakte_dir.name}-einzelpdfs.zip"
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        count = add_testakte(zipf, testakte_dir)
    if count == 0:
        out.unlink(missing_ok=True)
    return out, count


def _is_testakte_name(arg: str) -> bool:
    return "/" not in arg and "\\" not in arg and (TESTAKTEN / arg).is_dir()


def main() -> None:
    argv = sys.argv[1:]
    # Erstes Argument, das KEIN Testakten-Name ist, gilt als Ziel-Verzeichnis.
    dist = REPO_ROOT / "dist"
    targets: list[str] = []
    for arg in argv:
        if _is_testakte_name(arg):
            targets.append(arg)
        elif dist == REPO_ROOT / "dist":
            dist = Path(arg)
        else:
            targets.append(arg)
    dist.mkdir(parents=True, exist_ok=True)

    dirs = sorted(d for d in TESTAKTEN.iterdir() if d.is_dir())
    if targets:
        dirs = [d for d in dirs if d.name in targets]
    if not dirs:
        print("Keine Testakten gefunden.")
        return

    built: list[Path] = []
    total_pdfs = 0
    skipped: list[str] = []
    for d in dirs:
        out, count = build_single(d, dist)
        if count == 0:
            skipped.append(d.name)
            continue
        built.append(d)
        total_pdfs += count
        print(f"Baue {out.name}: {count} PDFs")

    if skipped:
        print(f"Hinweis: {len(skipped)} Ordner ohne renderbare Unterlagen uebersprungen: {skipped[:10]}")

    all_out = dist / "alle-testakten-einzelpdfs.zip"
    with zipfile.ZipFile(all_out, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        all_count = 0
        for d in built:
            all_count += add_testakte(zipf, d)
    print(f"Baue {all_out.name}: {all_count} PDFs aus {len(built)} Testakten")
    print(f"Fertig: {len(built)} Einzel-PDF-ZIPs, {total_pdfs} PDFs")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Baut pro Testakte ein ZIP, das jede Unterlage als eigene PDF enthaelt.

Anders als das Gesamt-PDF (alles in einem Dokument) liefert dieses ZIP jede
Akte-Unterlage als separate, sauber gerenderte PDF-Datei. Original-PDFs und
Office-Ausgaben werden bei Bedarf proportional auf A4 normalisiert; alle
anderen Dokumente (TXT/EML/CSV/XLSX/DOCX/ODT und Bilder) werden in jeweils eine
eigene PDF gerendert. Alle PDFs liegen unmittelbar auf der ZIP-Wurzelebene;
ehemalige Pfadbestandteile stehen lesbar im Dateinamen.

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
import shutil
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
from testakte_office_pdf import OFFICE_EXTS, OfficeRenderError, render_office, render_office_batch
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, without_notice_pages

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
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
SKIP_DIRS = {"megaprompts"}


def write_pdf(zipf: zipfile.ZipFile, arcname: str, data: bytes) -> None:
    """Schreibt ein PDF mit stabilen Metadaten fuer reproduzierbare Archive."""
    info = zipfile.ZipInfo(arcname, ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    zipf.writestr(info, data)


def write_archive(zipf: zipfile.ZipFile, path: Path) -> None:
    """Schreibt ein Einzel-ZIP streamend mit reproduzierbaren Metadaten."""
    info = zipfile.ZipInfo(path.name, ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    with path.open("rb") as source, zipf.open(info, "w") as target:
        shutil.copyfileobj(source, target, length=1024 * 1024)


def odt_to_flowables(path: Path) -> list:
    """Kompatibilitätswrapper für den gemeinsamen strengen ODT-Fallback."""
    return G.odt_to_flowables(path)


def normalize_pdf_to_a4(data: bytes, label: str) -> bytes:
    """Normalisiert nicht-A4-Seiten, ohne passende Originale neu zu schreiben."""
    try:
        reader = G.PdfReader(io.BytesIO(data))
        pages = list(reader.pages)
    except Exception as exc:
        raise G.DocumentRenderError(f"{label}: PDF konnte nicht gelesen werden: {exc}") from exc
    if not pages:
        raise G.DocumentRenderError(f"{label}: PDF enthält keine Seite")

    a4_width, a4_height = map(float, A4)

    def is_a4(page) -> bool:
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        return (
            abs(width - a4_width) < 1 and abs(height - a4_height) < 1
        ) or (
            abs(width - a4_height) < 1 and abs(height - a4_width) < 1
        )

    if all(is_a4(page) for page in pages):
        return data

    writer = G.PdfWriter()
    for page in pages:
        writer.add_page(G.a4_normalized_page(page))
    out = io.BytesIO()
    writer.write(out)
    normalized = out.getvalue()
    if not normalized.startswith(b"%PDF-"):
        raise G.DocumentRenderError(f"{label}: A4-Normalisierung lieferte kein PDF")
    return normalized


def render_document_pdf(
    path: Path,
    testakte_dir: Path,
    office_cache: dict[Path, bytes] | None = None,
) -> bytes | None:
    """Rendert eine Einzeldatei in eine PDF und liefert die Bytes.

    Bereits passende A4-PDFs werden unveraendert zurueckgegeben.
    """
    ext = ext_of(path)
    if ext in COPY_EXTS:
        data = without_notice_pages(path.read_bytes())
        return normalize_pdf_to_a4(data, path.name)

    if ext in OFFICE_EXTS:
        try:
            native = office_cache.get(path) if office_cache is not None else render_office(path)
        except OfficeRenderError as exc:
            raise G.DocumentRenderError(f"{path.name}: {exc}") from exc
        if native is not None:
            data = normalize_pdf_to_a4(native, path.name)
            return without_notice_pages(data)

    rel = path.relative_to(testakte_dir)
    flow: list = [Paragraph(f"<b>Datei:</b> {G.escape(str(rel))}", G.s_meta), Spacer(1, 6)]
    try:
        if ext == "md":
            rendered = G.md_to_flowables(path.read_text(encoding="utf-8", errors="strict"))
        elif ext == "txt":
            rendered = G.txt_to_flowables(path.read_text(encoding="utf-8", errors="strict"))
        elif ext == "eml":
            rendered = G.eml_to_flowables(path)
        elif ext == "csv":
            rendered = G.csv_to_flowables(path)
        elif ext == "xlsx":
            rendered = G.xlsx_to_flowables(path)
        elif ext == "docx":
            rendered = G.docx_to_flowables(path)
        elif ext == "odt":
            rendered = odt_to_flowables(path)
        elif ext in G.STRUCTURED_EXTS:
            rendered = G.structured_text_to_flowables(path)
        elif ext in IMAGE_EXTS:
            rendered = G.image_to_flowables(path)
        else:  # pragma: no cover - durch is_einzelpdf_document ausgeschlossen
            raise G.DocumentRenderError(f"nicht unterstützter Dokumenttyp: {ext}")
    except Exception as exc:
        if isinstance(exc, G.DocumentRenderError):
            raise G.DocumentRenderError(f"{rel}: {exc}") from exc
        raise G.DocumentRenderError(f"{rel}: {type(exc).__name__}: {exc}") from exc
    if not rendered:
        raise G.DocumentRenderError(f"{rel}: Konverter lieferte keine PDF-Inhalte")
    flow.extend(rendered)

    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
        title=f"{testakte_dir.name} — {rel}", author="Kanzleiakte",
    )
    hf = G.header_footer_factory(testakte_dir.name)
    try:
        doc.build(flow, onFirstPage=hf, onLaterPages=hf, canvasmaker=G.invariant_canvas)
        data = buf.getvalue()
        if not list(G.PdfReader(io.BytesIO(data)).pages):
            raise G.DocumentRenderError("erzeugtes PDF enthält keine Seite")
        data = normalize_pdf_to_a4(data, str(rel))
        return without_notice_pages(data)
    except Exception as exc:
        if isinstance(exc, G.DocumentRenderError):
            raise
        raise G.DocumentRenderError(f"{rel}: Einzel-PDF konnte nicht gebaut werden: {exc}") from exc


def add_testakte(zipf: zipfile.ZipFile, testakte_dir: Path) -> int:
    return add_testakte_many([zipf], testakte_dir)


def add_testakte_many(zipfiles: list[zipfile.ZipFile], testakte_dir: Path) -> int:
    """Rendert jede Quelle einmal und schreibt sie in mehrere Zielarchive."""
    count = 0
    pairs = document_arcname_pairs(testakte_dir)
    if pairs:
        for zipf in zipfiles:
            write_pdf(zipf, NOTICE_FILENAME, NOTICE_BYTES)
    try:
        office_cache = render_office_batch([path for path, _ in pairs])
    except OfficeRenderError as exc:
        raise G.DocumentRenderError(f"{testakte_dir.name}: {exc}") from exc
    for path, arcname in pairs:
        data = render_document_pdf(path, testakte_dir, office_cache)
        if data is None:
            continue
        for zipf in zipfiles:
            write_pdf(zipf, arcname, data)
        count += 1
    return count


def build_single(testakte_dir: Path, dist: Path) -> tuple[Path, int]:
    out = dist / f"testakte-{testakte_dir.name}-einzelpdfs.zip"
    tmp = out.with_name(f".{out.name}.tmp")
    with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1) as zipf:
        count = add_testakte(zipf, testakte_dir)
    if count == 0:
        tmp.unlink(missing_ok=True)
        out.unlink(missing_ok=True)
    else:
        tmp.replace(out)
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

    all_dirs = sorted(d for d in TESTAKTEN.iterdir() if d.is_dir() and d.name not in SKIP_DIRS)
    dirs = all_dirs
    if targets:
        unknown = sorted(set(targets) - {d.name for d in all_dirs})
        if unknown:
            raise SystemExit(f"Unbekannte Testakten: {unknown}")
        dirs = [d for d in dirs if d.name in targets]
    if not dirs:
        print("Keine Testakten gefunden.")
        return

    built: list[Path] = []
    pending: list[tuple[Path, Path]] = []
    total_pdfs = 0
    skipped: list[str] = []
    all_out = dist / "alle-testakten-einzelpdfs.zip"
    all_tmp = all_out.with_name(f".{all_out.name}.tmp")
    try:
        for d in dirs:
            out = dist / f"testakte-{d.name}-einzelpdfs.zip"
            tmp = out.with_name(f".{out.name}.tmp")
            try:
                with zipfile.ZipFile(
                    tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1
                ) as individual:
                    count = add_testakte(individual, d)
                if count == 0:
                    tmp.unlink(missing_ok=True)
                    out.unlink(missing_ok=True)
                    skipped.append(d.name)
                    continue
                pending.append((tmp, out))
            except Exception:
                tmp.unlink(missing_ok=True)
                raise
            built.append(d)
            total_pdfs += count
            print(f"Baue {out.name}: {count} PDFs")
        for tmp, out in pending:
            tmp.replace(out)
        bundle_archives = [dist / f"testakte-{d.name}-einzelpdfs.zip" for d in all_dirs]
        missing_archives = [path.name for path in bundle_archives if not path.is_file()]
        if missing_archives:
            raise G.DocumentRenderError(
                "Zentralarchiv unvollständig; zuerst fehlende Einzelarchive bauen: "
                + ", ".join(missing_archives[:10])
            )
        combined_pdfs = 0
        with zipfile.ZipFile(
            all_tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1
        ) as combined:
            write_pdf(combined, NOTICE_FILENAME, NOTICE_BYTES)
            for archive in bundle_archives:
                with zipfile.ZipFile(archive) as individual:
                    combined_pdfs += sum(name.lower().endswith(".pdf") for name in individual.namelist())
                write_archive(combined, archive)
        all_tmp.replace(all_out)
    except Exception:
        all_tmp.unlink(missing_ok=True)
        for tmp, _ in pending:
            tmp.unlink(missing_ok=True)
        raise

    if skipped:
        print(f"Hinweis: {len(skipped)} Ordner ohne renderbare Unterlagen uebersprungen: {skipped[:10]}")

    print(
        f"Baue {all_out.name}: {len(bundle_archives)} flache Einzel-ZIPs "
        f"mit {combined_pdfs} PDFs"
    )
    print(f"Fertig: {len(built)} Einzel-PDF-ZIPs, {total_pdfs} PDFs")


if __name__ == "__main__":
    main()

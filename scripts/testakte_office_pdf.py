#!/usr/bin/env python3
"""Rendert Office-Aktenstücke layoutgetreu und reproduzierbar als PDF.

Die bisherige reine Textextraktion bleibt in den aufrufenden Buildern als
Fallback erhalten. Ist LibreOffice verfügbar, bleiben dagegen Briefköpfe,
Kopf- und Fußzeilen, Tabellengeometrie und Seitenumbrüche erhalten.
"""

from __future__ import annotations

import hashlib
import io
import os
import shutil
import subprocess
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

from pypdf import PdfReader, PdfWriter


OFFICE_EXTS = {"docx", "odt", "xlsx"}
FIXED_DATE = "D:20000101000000Z"
SHEET_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"


class OfficeRenderError(RuntimeError):
    """Eine native Office-Konvertierung ist fehlgeschlagen."""


def valid_office_container(path: Path) -> bool:
    """Verhindert, dass Office beliebigen Text mit falscher Endung rendert."""
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
    except (OSError, zipfile.BadZipFile):
        return False
    ext = path.suffix.lower()
    if ext == ".docx":
        return "[Content_Types].xml" in names and "word/document.xml" in names
    if ext == ".odt":
        return "mimetype" in names and "content.xml" in names
    if ext == ".xlsx":
        return "[Content_Types].xml" in names and "xl/workbook.xml" in names
    return False


def prepare_source(source: Path, target: Path) -> None:
    """Passt nur die Druckkopie an; Originaldaten und Formeln bleiben erhalten."""
    if source.suffix.lower() != ".xlsx":
        shutil.copyfile(source, target)
        return
    ns = f"{{{SHEET_NS}}}"
    with zipfile.ZipFile(source) as original, zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as staged:
        for info in original.infolist():
            data = original.read(info)
            if info.filename.startswith("xl/worksheets/") and info.filename.endswith(".xml"):
                sheet = ET.fromstring(data)
                properties = sheet.find(f"{ns}sheetPr")
                if properties is None:
                    properties = ET.Element(f"{ns}sheetPr")
                    sheet.insert(0, properties)
                setup_properties = properties.find(f"{ns}pageSetUpPr")
                if setup_properties is None:
                    setup_properties = ET.SubElement(properties, f"{ns}pageSetUpPr")
                setup_properties.set("fitToPage", "1")
                setup = sheet.find(f"{ns}pageSetup")
                if setup is None:
                    setup = ET.Element(f"{ns}pageSetup")
                    later = {"headerFooter", "rowBreaks", "colBreaks", "customProperties", "cellWatches", "ignoredErrors", "smartTags", "drawing", "legacyDrawing", "legacyDrawingHF", "picture", "oleObjects", "controls", "webPublishItems", "tableParts", "extLst"}
                    position = next((i for i, child in enumerate(sheet) if child.tag.rsplit("}", 1)[-1] in later), len(sheet))
                    sheet.insert(position, setup)
                setup.attrib.pop("scale", None)
                setup.set("paperSize", "9")
                setup.set("fitToWidth", "1")
                setup.set("fitToHeight", "0")
                if "orientation" not in setup.attrib:
                    widest = max((len(row) for row in sheet.findall(f"{ns}sheetData/{ns}row")), default=0)
                    setup.set("orientation", "landscape" if widest > 6 else "portrait")
                data = ET.tostring(sheet, encoding="utf-8", xml_declaration=True)
            elif info.filename == "xl/workbook.xml":
                workbook = ET.fromstring(data)
                calculation = workbook.find(f"{ns}calcPr")
                if calculation is None:
                    calculation = ET.SubElement(workbook, f"{ns}calcPr")
                calculation.set("calcMode", "auto")
                calculation.set("fullCalcOnLoad", "1")
                calculation.set("forceFullCalc", "1")
                data = ET.tostring(workbook, encoding="utf-8", xml_declaration=True)
            staged.writestr(info, data)


def uncached_formula_cells(path: Path) -> list[str]:
    """Verhindert stille Leerwerte im PDF-Fallback ohne Rechenprogramm."""
    ns = f"{{{SHEET_NS}}}"
    missing = []
    with zipfile.ZipFile(path) as archive:
        for name in archive.namelist():
            if not name.startswith("xl/worksheets/") or not name.endswith(".xml"):
                continue
            sheet = ET.fromstring(archive.read(name))
            for cell in sheet.iter(f"{ns}c"):
                value = cell.find(f"{ns}v")
                if cell.find(f"{ns}f") is not None and (value is None or (value.text is None and cell.get("t") != "str")):
                    missing.append(f"{name}:{cell.get('r', '?')}")
    return missing


def office_binary() -> str | None:
    configured = os.environ.get("SOFFICE", "").strip()
    if configured:
        return configured
    return shutil.which("soffice") or shutil.which("libreoffice")


def normalize_pdf(data: bytes, title: str) -> bytes:
    """Entfernt variable Office-Metadaten und erzeugt stabile PDF-Bytes."""
    try:
        pages = list(PdfReader(io.BytesIO(data)).pages)
    except Exception as exc:
        raise OfficeRenderError(f"Office-Ausgabe ist kein lesbares PDF: {exc}") from exc
    if not pages:
        raise OfficeRenderError("Office-Ausgabe enthält keine Seite")

    writer = PdfWriter()
    for page in pages:
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": title,
            "/Author": "Kanzleiakte",
            "/CreationDate": FIXED_DATE,
            "/ModDate": FIXED_DATE,
        }
    )
    out = io.BytesIO()
    writer.write(out)
    return out.getvalue()


def render_office_batch(paths: list[Path]) -> dict[Path, bytes]:
    """Konvertiert mehrere Office-Dateien in einem isolierten Office-Lauf.

    Ein leerer Rückgabewert bedeutet, dass LibreOffice nicht installiert ist.
    Fehlende Ausgaben einzelner defekter Dateien bleiben ebenfalls aus der
    Abbildung heraus; der aufrufende Builder verwendet dann seinen strengen
    Parser-Fallback und meldet einen nachvollziehbaren Dokumentfehler.
    """
    candidates = [
        p
        for p in paths
        if p.suffix.lower().lstrip(".") in OFFICE_EXTS and valid_office_container(p)
    ]
    if not candidates:
        return {}
    binary = office_binary()
    if not binary:
        return {}

    with tempfile.TemporaryDirectory(prefix="testakte-office-") as tmp:
        root = Path(tmp)
        source_dir = root / "source"
        output_dir = root / "pdf"
        profile_dir = root / "profile"
        home_dir = root / "home"
        for directory in (source_dir, output_dir, profile_dir, home_dir):
            directory.mkdir()

        staged: dict[Path, Path] = {}
        for index, source in enumerate(candidates):
            digest = hashlib.sha256(str(source.resolve()).encode("utf-8")).hexdigest()[:10]
            target = source_dir / f"{index:04d}-{digest}{source.suffix.lower()}"
            prepare_source(source, target)
            staged[source] = target

        command = [
            binary,
            f"-env:UserInstallation={profile_dir.resolve().as_uri()}",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(output_dir),
            *[str(path) for path in staged.values()],
        ]
        env = os.environ.copy()
        env["HOME"] = str(home_dir)
        timeout = max(90, min(900, 20 + len(staged) * 15))
        try:
            completed = subprocess.run(
                command,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            raise OfficeRenderError(
                f"LibreOffice-Konvertierung nach {timeout} Sekunden abgebrochen"
            ) from exc

        rendered: dict[Path, bytes] = {}
        for source, stage in staged.items():
            pdf = output_dir / f"{stage.stem}.pdf"
            if not pdf.is_file() or pdf.stat().st_size == 0:
                continue
            rendered[source] = normalize_pdf(pdf.read_bytes(), source.name)

        if completed.returncode != 0 and not rendered:
            stderr = completed.stderr.decode("utf-8", errors="replace").strip()
            raise OfficeRenderError(
                f"LibreOffice-Konvertierung fehlgeschlagen: {stderr[:500]}"
            )
        return rendered


def render_office(path: Path) -> bytes | None:
    """Konvertiert eine Office-Datei; ohne Office-Programm wird None geliefert."""
    return render_office_batch([path]).get(path)

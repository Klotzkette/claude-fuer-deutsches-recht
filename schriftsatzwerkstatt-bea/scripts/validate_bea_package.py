#!/usr/bin/env python3
"""Validiert einen fertigen beA-Ausgabeordner ohne Dateien zu verändern."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
import os
import re
import shutil
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stderr
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Callable


MAX_NAME_LENGTH = 80
MAX_SIGNATURE_NAME_LENGTH = 90
MAX_FILES = 1_000
MAX_BYTES = 200_000_000
WARN_FILES = 900
WARN_BYTES = 180_000_000
MAX_MANIFEST_BYTES = 2_000_000
SCAN_CHUNK_BYTES = 1024 * 1024
MAX_PDF_WORKERS = 4

EXPECTED_COLUMNS = (
    "Reihenfolge",
    "Rolle",
    "Anlage",
    "Quelldatei",
    "Zieldatei",
    "Seiten",
    "Bytes",
    "SHA256",
    "OCR",
    "Kennzeichnung",
    "Datenschutz",
    "Status",
)
SIGNATURE_COLUMNS = (
    "Signaturdatei",
    "Zieldokument",
    "Zieldokument_SHA256",
    "Bytes",
    "SHA256",
    "Format",
    "Signaturniveau",
    "Prüfstatus",
    "Unterzeichner",
    "Prüfprotokoll",
)
NAME_RE = re.compile(r"^(\d{2,4})_([A-Za-z0-9]+(?:[_-][A-Za-z0-9]+)*)\.pdf$")
MAIN_NAME_RE = re.compile(r"^\d{2,4}_[KB]_[A-Za-z0-9]+(?:[_-][A-Za-z0-9]+)*\.pdf$")
SIGNATURE_NAME_RE = re.compile(
    r"^[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*\.(?:p7|p7s|p7m|pkcs7)$"
)
ATTACHMENT_LABEL_RE = re.compile(r"^([KB]) ([1-9]\d*)$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
WINDOWS_DRIVE_RE = re.compile(r"^[A-Za-z]:")
CSV_FORMULA_PREFIXES = ("=", "+", "-", "@")
ALLOWED_OCR = {"vorhanden", "nicht nötig", "nicht noetig"}
ALLOWED_PRIVACY = {"geprüft", "geprueft"}
ALLOWED_MAIN_MARKING = {"nicht anwendbar"}
ALLOWED_ATTACHMENT_MARKING = {
    "geprüft",
    "geprueft",
    "deckblatt",
    "signiertes original",
}
ALLOWED_SIGNATURE_STATUS = {"grün", "gruen", "erfolgreich"}
SIGNATURE_SUFFIXES = {".p7", ".p7s", ".p7m", ".pkcs7"}
PROTOCOL_SUFFIXES = {".pdf", ".txt", ".html", ".xml"}
ACTIVE_PDF_PATTERNS = (
    ("Verschlüsselung oder Passwortschutz", re.compile(rb"/Encrypt\b")),
    ("JavaScript", re.compile(rb"/JavaScript\b|/JS(?:\s|\(|<|\d+\s+\d+\s+R)")),
    ("eingebettete Dateien", re.compile(rb"/EmbeddedFiles?\b")),
    ("Dateianhang-Annotation", re.compile(rb"/FileAttachment\b")),
    ("Startaktion", re.compile(rb"/Launch\b")),
    ("aktive Formularaktion", re.compile(rb"/(?:SubmitForm|ImportData)\b")),
    ("dynamisches XFA-Formular", re.compile(rb"/XFA\b")),
    ("PDF-Portfolio", re.compile(rb"/Collection\b")),
    ("Rich-Media-Inhalt", re.compile(rb"/RichMedia\b")),
    ("3D-Inhalt", re.compile(rb"/3D\b")),
    ("Audio-/Videoinhalt", re.compile(rb"/(?:Sound|Movie)\b")),
)


@dataclass(frozen=True)
class PdfInspection:
    pages: int | None
    size: int
    sha256: str
    errors: tuple[str, ...]


def sha256(path: Path) -> str:
    """Berechnet einen Hash blockweise; für externe Aufrufer beibehalten."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(SCAN_CHUNK_BYTES), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect_pdf(path: Path) -> PdfInspection:
    """Hasht, scannt und parst eine PDF mit begrenztem Speicherbedarf."""
    errors: list[str] = []
    digest = hashlib.sha256()
    first_bytes = b""
    tail = b""
    findings: set[str] = set()

    try:
        before = path.stat()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(SCAN_CHUNK_BYTES), b""):
                if not first_bytes:
                    first_bytes = chunk[:8]
                digest.update(chunk)
                window = tail + chunk
                for finding, pattern in ACTIVE_PDF_PATTERNS:
                    if finding not in findings and pattern.search(window):
                        findings.add(finding)
                tail = window[-4096:]
        after = path.stat()
    except OSError as exc:
        return PdfInspection(None, 0, "", (f"{path.name}: Datei nicht lesbar: {exc}",))

    if before.st_size != after.st_size or before.st_mtime_ns != after.st_mtime_ns:
        errors.append(f"{path.name}: Datei wurde während der Prüfung verändert")
    if not first_bytes.startswith(b"%PDF-"):
        errors.append(f"{path.name}: kein echter PDF-Header")
        return PdfInspection(None, after.st_size, digest.hexdigest(), tuple(errors))
    if b"%%EOF" not in tail:
        errors.append(f"{path.name}: PDF-Endemarkierung fehlt")
    for finding in sorted(findings):
        errors.append(f"{path.name}: PDF enthält {finding}")

    try:
        from pypdf import PdfReader
    except ImportError:
        errors.append(
            f"{path.name}: pypdf fehlt; vollständige PDF-Strukturprüfung ist nicht möglich"
        )
        return PdfInspection(None, after.st_size, digest.hexdigest(), tuple(errors))

    pages: int | None = None
    try:
        reader = PdfReader(path)
        if reader.is_encrypted:
            errors.append(f"{path.name}: PDF ist verschlüsselt")
        else:
            pages = len(reader.pages)
            if pages < 1:
                errors.append(f"{path.name}: PDF enthält keine Seite")
            for page_number, page in enumerate(reader.pages, start=1):
                for box_name, box in (
                    ("MediaBox", page.mediabox),
                    ("CropBox", page.cropbox),
                ):
                    width = abs(float(box.right) - float(box.left))
                    height = abs(float(box.top) - float(box.bottom))
                    if not all(
                        math.isfinite(value) and value > 0 for value in (width, height)
                    ):
                        errors.append(
                            f"{path.name}: Seite {page_number} hat keine gültige {box_name}"
                        )
                try:
                    rotation = int(page.get("/Rotate", 0))
                except (TypeError, ValueError):
                    errors.append(
                        f"{path.name}: Seite {page_number} hat eine ungültige Drehung"
                    )
                else:
                    if rotation % 90:
                        errors.append(
                            f"{path.name}: Seite {page_number} ist nicht rechtwinklig gedreht"
                        )
            parsed = path.stat()
            if (
                parsed.st_size != after.st_size
                or parsed.st_mtime_ns != after.st_mtime_ns
            ):
                errors.append(
                    f"{path.name}: Datei wurde während der Strukturprüfung verändert"
                )
    except Exception as exc:  # noqa: BLE001 - Defekt soll als Befund ausgegeben werden.
        errors.append(f"{path.name}: PDF kann nicht vollständig gelesen werden: {exc}")
        pages = None
    return PdfInspection(pages, after.st_size, digest.hexdigest(), tuple(errors))


def inspect_pdfs(paths: list[Path]) -> dict[str, PdfInspection]:
    """Prüft größere Pakete parallel, behält aber eine deterministische Ausgabe."""
    if len(paths) < 4:
        inspections = [inspect_pdf(path) for path in paths]
    else:
        workers = min(MAX_PDF_WORKERS, len(paths), os.cpu_count() or 1)
        with ThreadPoolExecutor(max_workers=workers) as executor:
            inspections = list(executor.map(inspect_pdf, paths))
    if len(inspections) != len(paths):
        raise RuntimeError("PDF-Prüfung lieferte nicht für jede Datei ein Ergebnis")
    return dict(zip((path.name for path in paths), inspections))


def locate_dirs(path: Path) -> tuple[Path, Path]:
    path = path.expanduser().absolute()
    if path.name == "upload":
        return path, path.parent / "intern"
    return path / "upload", path / "intern"


def read_manifest(
    path: Path,
) -> tuple[list[dict[str | None, str | list[str]]], list[str]]:
    if path.is_symlink():
        return [], [f"Manifest darf kein Symlink sein: {path}"]
    if not path.is_file():
        return [], [f"Manifest fehlt: {path}"]
    if path.stat().st_size > MAX_MANIFEST_BYTES:
        return [], [
            f"Manifest überschreitet die interne Obergrenze {MAX_MANIFEST_BYTES} Bytes: {path}"
        ]
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            actual = tuple(reader.fieldnames or ())
            if actual != EXPECTED_COLUMNS:
                return [], [
                    "Manifestkopf ist nicht exakt: "
                    f"erwartet={list(EXPECTED_COLUMNS)}, vorhanden={list(actual)}"
                ]
            return list(reader), []
    except (OSError, UnicodeError, csv.Error) as exc:
        return [], [f"Manifest kann nicht sicher gelesen werden: {exc}"]


def read_signature_manifest(
    path: Path,
) -> tuple[list[dict[str | None, str | list[str]]], list[str]]:
    if path.is_symlink():
        return [], [f"Signaturmanifest darf kein Symlink sein: {path}"]
    if not path.is_file():
        return [], [f"Signaturmanifest fehlt: {path}"]
    if path.stat().st_size > MAX_MANIFEST_BYTES:
        return [], [
            "Signaturmanifest überschreitet die interne Obergrenze "
            f"{MAX_MANIFEST_BYTES} Bytes: {path}"
        ]
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            actual = tuple(reader.fieldnames or ())
            if actual != SIGNATURE_COLUMNS:
                return [], [
                    "Signaturmanifestkopf ist nicht exakt: "
                    f"erwartet={list(SIGNATURE_COLUMNS)}, vorhanden={list(actual)}"
                ]
            return list(reader), []
    except (OSError, UnicodeError, csv.Error) as exc:
        return [], [f"Signaturmanifest kann nicht sicher gelesen werden: {exc}"]


def filename_errors(name: str, total_files: int) -> list[str]:
    errors: list[str] = []
    if len(name) > MAX_NAME_LENGTH:
        errors.append(f"{name}: {len(name)} Zeichen überschreiten {MAX_NAME_LENGTH}")
    try:
        name.encode("ascii")
    except UnicodeEncodeError:
        errors.append(f"{name}: Dateiname ist nicht ASCII")
    match = NAME_RE.fullmatch(name)
    if match is None:
        errors.append(
            f"{name}: Name muss Reihenfolge, getrennte ASCII-Wörter und .pdf enthalten"
        )
        return errors
    if int(match.group(1)) < 1:
        errors.append(f"{name}: Reihenfolge muss mit 1 beginnen")
    width = max(2, len(str(total_files)))
    if len(match.group(1)) != width:
        errors.append(
            f"{name}: Reihenfolge muss für {total_files} Dateien {width}-stellig sein"
        )
    return errors


def signature_filename_errors(name: str) -> list[str]:
    errors: list[str] = []
    if len(name) > MAX_SIGNATURE_NAME_LENGTH:
        errors.append(
            f"{name}: {len(name)} Zeichen überschreiten {MAX_SIGNATURE_NAME_LENGTH} für Signaturdateien"
        )
    try:
        name.encode("ascii")
    except UnicodeEncodeError:
        errors.append(f"{name}: Signaturdateiname ist nicht ASCII")
    if SIGNATURE_NAME_RE.fullmatch(name) is None:
        errors.append(
            f"{name}: Signaturdatei braucht einen sicheren ASCII-Namen und .p7, .p7s, .p7m oder .pkcs7"
        )
    return errors


def safe_relative_source(value: str) -> bool:
    if not value or "\x00" in value or "\\" in value or "//" in value:
        return False
    if value.startswith("/") or WINDOWS_DRIVE_RE.match(value):
        return False
    raw_parts = value.split("/")
    if raw_parts[0] == ".":
        raw_parts = raw_parts[1:]
    parts = PurePosixPath(value).parts
    return bool(parts) and all(part not in {"", ".", ".."} for part in raw_parts)


def has_formula_prefix(value: str) -> bool:
    candidate = value.lstrip()
    return value.startswith(("\t", "\r")) or candidate.startswith(CSV_FORMULA_PREFIXES)


def normalized(value: str) -> str:
    return value.strip().casefold()


def has_control_character(value: str) -> bool:
    return any(ord(character) < 32 or ord(character) == 127 for character in value)


def parse_positive_int(
    value: str,
    field: str,
    row_number: int,
    errors: list[str],
    *,
    record_label: str = "Manifestzeile",
) -> int | None:
    if not value.isdecimal() or int(value) < 1:
        errors.append(
            f"{record_label} {row_number}: {field} muss eine positive Ganzzahl sein"
        )
        return None
    return int(value)


def validate_signatures(
    signatures: list[Path],
    pdfs: list[Path],
    inspections: dict[str, PdfInspection],
    internal: Path,
) -> list[str]:
    errors: list[str] = []
    manifest_path = internal / "signaturmanifest.csv"
    if not signatures:
        if manifest_path.exists() or manifest_path.is_symlink():
            errors.append(
                "Signaturmanifest ist vorhanden, aber im Upload liegt keine separate Signaturdatei"
            )
        return errors

    rows, manifest_errors = read_signature_manifest(manifest_path)
    errors.extend(manifest_errors)
    if manifest_errors:
        return errors
    if len(rows) != len(signatures):
        errors.append(
            f"Signaturmanifest enthält {len(rows)} Zeilen, Upload aber {len(signatures)} Signaturdateien"
        )

    pdf_by_name = {path.name: path for path in pdfs}
    signature_by_name = {path.name: path for path in signatures}
    manifest_names: set[str] = set()
    signature_hashes: dict[str, list[str]] = {}

    for index, row in enumerate(rows, start=1):
        row_number = index + 1
        if None in row:
            errors.append(
                f"Signaturmanifestzeile {row_number}: zusätzliche CSV-Werte ohne Spaltenkopf"
            )
        clean: dict[str, str] = {}
        for field in SIGNATURE_COLUMNS:
            raw = row.get(field, "")
            value = raw if isinstance(raw, str) else ""
            if has_control_character(value):
                errors.append(
                    f"Signaturmanifestzeile {row_number}: {field} enthält Steuerzeichen"
                )
            if value != value.strip():
                errors.append(
                    f"Signaturmanifestzeile {row_number}: {field} hat Rand-Leerzeichen"
                )
            value = value.strip()
            clean[field] = value
            if has_formula_prefix(value):
                errors.append(
                    f"Signaturmanifestzeile {row_number}: {field} beginnt wie eine Tabellenformel"
                )
            if not value:
                errors.append(f"Signaturmanifestzeile {row_number}: {field} fehlt")

        signature_name = clean["Signaturdatei"]
        if signature_name:
            if (
                "/" in signature_name
                or "\\" in signature_name
                or Path(signature_name).name != signature_name
            ):
                errors.append(
                    f"Signaturmanifestzeile {row_number}: Signaturdatei darf keinen Pfad enthalten"
                )
            if signature_name in manifest_names:
                errors.append(
                    f"Signaturmanifest: Signaturdatei doppelt: {signature_name}"
                )
            manifest_names.add(signature_name)

        target_name = clean["Zieldokument"]
        if target_name and (
            "/" in target_name
            or "\\" in target_name
            or Path(target_name).name != target_name
        ):
            errors.append(
                f"Signaturmanifestzeile {row_number}: Zieldokument darf keinen Pfad enthalten"
            )
        target = pdf_by_name.get(target_name)
        if target is None and target_name:
            errors.append(
                f"Signaturmanifestzeile {row_number}: Zieldokument fehlt im Upload: {target_name}"
            )
        target_hash = clean["Zieldokument_SHA256"]
        if not SHA256_RE.fullmatch(target_hash):
            errors.append(
                f"Signaturmanifestzeile {row_number}: Zieldokument_SHA256 muss aus 64 kleinen Hexzeichen bestehen"
            )
        elif target is not None and target_hash != inspections[target.name].sha256:
            errors.append(
                f"Signaturmanifestzeile {row_number}: Zielhash passt nicht zur finalen PDF {target.name}"
            )

        signature = signature_by_name.get(signature_name)
        if signature is None and signature_name:
            errors.append(
                f"Signaturmanifestzeile {row_number}: Signaturdatei fehlt im Upload: {signature_name}"
            )
        bytes_value = parse_positive_int(
            clean["Bytes"],
            "Bytes",
            row_number,
            errors,
            record_label="Signaturmanifestzeile",
        )
        signature_hash = clean["SHA256"]
        if not SHA256_RE.fullmatch(signature_hash):
            errors.append(
                f"Signaturmanifestzeile {row_number}: SHA256 muss aus 64 kleinen Hexzeichen bestehen"
            )
        if signature is not None:
            actual_size = signature.stat().st_size
            actual_hash = sha256(signature)
            if bytes_value is not None and bytes_value != actual_size:
                errors.append(
                    f"{signature.name}: Bytes im Signaturmanifest stimmen nicht"
                )
            if signature_hash and signature_hash != actual_hash:
                errors.append(
                    f"{signature.name}: SHA256 im Signaturmanifest stimmt nicht"
                )
            signature_hashes.setdefault(actual_hash, []).append(signature.name)

        if normalized(clean["Format"]) != "cades":
            errors.append(f"Signaturmanifestzeile {row_number}: Format muss CAdES sein")
        if normalized(clean["Signaturniveau"]) != "qes":
            errors.append(
                f"Signaturmanifestzeile {row_number}: Signaturniveau muss qeS sein"
            )
        if normalized(clean["Prüfstatus"]) not in ALLOWED_SIGNATURE_STATUS:
            errors.append(
                f"Signaturmanifestzeile {row_number}: qeS-Prüfstatus muss grün sein"
            )

        protocol_name = clean["Prüfprotokoll"]
        if protocol_name and (
            "/" in protocol_name
            or "\\" in protocol_name
            or Path(protocol_name).name != protocol_name
            or Path(protocol_name).suffix.lower() not in PROTOCOL_SUFFIXES
        ):
            errors.append(
                f"Signaturmanifestzeile {row_number}: Prüfprotokoll braucht einen Dateinamen mit PDF, TXT, HTML oder XML im internen Ordner"
            )
        elif protocol_name:
            protocol = internal / protocol_name
            if protocol.is_symlink() or not protocol.is_file():
                errors.append(
                    f"Signaturmanifestzeile {row_number}: Prüfprotokoll fehlt oder ist kein reguläres internes Dokument: {protocol_name}"
                )
            elif protocol.stat().st_size < 1:
                errors.append(
                    f"Signaturmanifestzeile {row_number}: Prüfprotokoll ist leer: {protocol_name}"
                )

    actual_names = set(signature_by_name)
    if actual_names != manifest_names:
        errors.append(
            "Signaturmanifest und Upload unterscheiden sich: "
            f"fehlend={sorted(actual_names - manifest_names)}, "
            f"zusätzlich={sorted(manifest_names - actual_names)}"
        )
    for names in signature_hashes.values():
        if len(names) > 1:
            errors.append(
                f"Inhaltsgleiche Signaturdateien sind nicht eindeutig: {', '.join(names)}"
            )
    return errors


def validate(package: Path) -> tuple[list[str], list[str]]:
    upload, internal = locate_dirs(package)
    errors: list[str] = []
    warnings: list[str] = []
    if upload.is_symlink():
        return [f"Upload-Ordner darf kein Symlink sein: {upload}"], warnings
    if not upload.is_dir():
        return [f"Upload-Ordner fehlt: {upload}"], warnings
    if internal.is_symlink():
        return [f"Interner Paketordner darf kein Symlink sein: {internal}"], warnings

    entries: list[Path] = []
    try:
        for entry in upload.iterdir():
            entries.append(entry)
            if len(entries) > MAX_FILES:
                errors.append(
                    f"Upload-Ordner enthält mehr als {MAX_FILES} Einträge; "
                    "Prüfung zum Schutz vor übergroßen Verzeichnissen beendet"
                )
                return errors, warnings
    except OSError as exc:
        return [f"Upload-Ordner kann nicht sicher gelesen werden: {exc}"], warnings
    entries.sort(key=lambda item: item.name.casefold())
    regular_files: list[Path] = []
    for entry in entries:
        if entry.is_symlink():
            errors.append(f"{entry.name}: Symlink im Upload-Ordner ist unzulässig")
        elif entry.is_dir():
            errors.append(f"{entry.name}: Unterordner im Upload-Ordner ist unzulässig")
        elif not entry.is_file():
            errors.append(
                f"{entry.name}: nur reguläre Dateien sind im Upload-Ordner zulässig"
            )
        else:
            regular_files.append(entry)
            if entry.suffix != ".pdf" and entry.suffix not in SIGNATURE_SUFFIXES:
                errors.append(
                    f"{entry.name}: Upload-Ordner erlaubt nur PDF und zugeordnete CAdES-Signaturdateien"
                )

    pdfs = [entry for entry in regular_files if entry.suffix == ".pdf"]
    signatures = [
        entry for entry in regular_files if entry.suffix in SIGNATURE_SUFFIXES
    ]
    if not pdfs:
        errors.append("Upload-Ordner enthält keine PDF-Datei")
        return errors, warnings
    if len(regular_files) > MAX_FILES:
        errors.append(
            f"{len(regular_files)} Dateien überschreiten die Obergrenze {MAX_FILES}"
        )
    elif len(regular_files) > WARN_FILES:
        warnings.append(f"Warnschwelle: {len(regular_files)} Dateien")

    total_bytes = sum(path.stat().st_size for path in regular_files)
    if total_bytes > MAX_BYTES:
        errors.append(f"{total_bytes} Bytes überschreiten die Obergrenze {MAX_BYTES}")
    elif total_bytes > WARN_BYTES:
        warnings.append(f"Warnschwelle: {total_bytes} Bytes Gesamtgröße")

    folded_names: dict[str, str] = {}
    sequence_by_path: dict[Path, int] = {}
    for entry in regular_files:
        if entry.suffix == ".pdf":
            errors.extend(filename_errors(entry.name, len(pdfs)))
        elif entry.suffix in SIGNATURE_SUFFIXES:
            errors.extend(signature_filename_errors(entry.name))
        folded = entry.name.casefold()
        if folded in folded_names:
            errors.append(
                f"{entry.name}: kollidiert ohne Beachtung der Großschreibung mit {folded_names[folded]}"
            )
        folded_names[folded] = entry.name
        if entry.suffix == ".pdf":
            match = NAME_RE.fullmatch(entry.name)
            if match is not None:
                sequence_by_path[entry] = int(match.group(1))

    sequence = sorted(sequence_by_path.values())
    expected_sequence = list(range(1, len(pdfs) + 1))
    if sequence != expected_sequence:
        errors.append(
            f"Dateireihenfolge ist nicht lückenlos 1 bis {len(pdfs)}: {sequence}"
        )
    ordered_pdfs = sorted(
        pdfs,
        key=lambda path: (
            sequence_by_path.get(path, MAX_FILES + 1),
            path.name.casefold(),
        ),
    )

    inspections = inspect_pdfs(ordered_pdfs)
    for pdf in ordered_pdfs:
        errors.extend(inspections[pdf.name].errors)
    errors.extend(validate_signatures(signatures, pdfs, inspections, internal))

    duplicate_hashes: dict[str, list[str]] = {}
    for pdf in ordered_pdfs:
        digest = inspections[pdf.name].sha256
        if digest:
            duplicate_hashes.setdefault(digest, []).append(pdf.name)
    for names in duplicate_hashes.values():
        if len(names) > 1:
            warnings.append(f"Inhaltsgleiche Upload-Dateien prüfen: {', '.join(names)}")

    rows, manifest_errors = read_manifest(internal / "versandmanifest.csv")
    errors.extend(manifest_errors)
    if manifest_errors:
        return errors, warnings
    if not rows:
        errors.append("Manifest enthält keine Dateizeile")
        return errors, warnings
    if len(rows) != len(pdfs):
        errors.append(
            f"Manifest enthält {len(rows)} Zeilen, Upload aber {len(pdfs)} PDF-Dateien"
        )

    by_name: dict[str, dict[str | None, str | list[str]]] = {}
    folded_manifest_names: dict[str, str] = {}
    attachment_labels: set[str] = set()
    width = max(2, len(str(len(pdfs))))
    for index, row in enumerate(rows, start=1):
        row_number = index + 1
        if None in row:
            errors.append(
                f"Manifestzeile {row_number}: zusätzliche CSV-Werte ohne Spaltenkopf"
            )
        clean: dict[str, str] = {}
        for field in EXPECTED_COLUMNS:
            raw = row.get(field, "")
            value = raw if isinstance(raw, str) else ""
            if has_control_character(value):
                errors.append(
                    f"Manifestzeile {row_number}: {field} enthält Steuerzeichen"
                )
            if value != value.strip():
                errors.append(
                    f"Manifestzeile {row_number}: {field} hat Rand-Leerzeichen"
                )
            value = value.strip()
            clean[field] = value
            if has_formula_prefix(value):
                errors.append(
                    f"Manifestzeile {row_number}: {field} beginnt wie eine Tabellenformel"
                )

        for field in EXPECTED_COLUMNS:
            if field != "Anlage" and not clean[field]:
                errors.append(f"Manifestzeile {row_number}: {field} fehlt")

        expected_order = f"{index:0{width}d}"
        if clean["Reihenfolge"] != expected_order:
            errors.append(
                f"Manifestzeile {row_number}: Reihenfolge muss exakt {expected_order} sein"
            )
        if not safe_relative_source(clean["Quelldatei"]):
            errors.append(
                f"Manifestzeile {row_number}: Quelldatei muss ein sicherer relativer Pfad sein"
            )

        name = clean["Zieldatei"]
        if name:
            if "/" in name or "\\" in name or Path(name).name != name:
                errors.append(
                    f"Manifestzeile {row_number}: Zieldatei darf keinen Pfad enthalten"
                )
            if name in by_name:
                errors.append(f"Manifest: Zieldatei doppelt: {name}")
            folded = name.casefold()
            if (
                folded in folded_manifest_names
                and folded_manifest_names[folded] != name
            ):
                errors.append(
                    f"Manifest: Zieldateien kollidieren ohne Beachtung der Großschreibung: "
                    f"{folded_manifest_names[folded]} und {name}"
                )
            by_name[name] = row
            folded_manifest_names[folded] = name

        if index == 1:
            if clean["Rolle"] != "Hauptschriftsatz":
                errors.append(
                    f"Manifestzeile {row_number}: Datei 01 muss Hauptschriftsatz sein"
                )
            if clean["Anlage"]:
                errors.append(
                    f"Manifestzeile {row_number}: Hauptschriftsatz darf keine Anlage sein"
                )
            if name and MAIN_NAME_RE.fullmatch(name) is None:
                errors.append(
                    f"Manifestzeile {row_number}: Hauptschriftsatzname muss nach Präfix K oder B enthalten"
                )
            if normalized(clean["Kennzeichnung"]) not in ALLOWED_MAIN_MARKING:
                errors.append(
                    f"Manifestzeile {row_number}: Hauptschriftsatz braucht Kennzeichnung nicht anwendbar"
                )
        else:
            if clean["Rolle"] != "Anlage":
                errors.append(
                    f"Manifestzeile {row_number}: Dateien nach 01 müssen Anlagen sein"
                )
            label_match = ATTACHMENT_LABEL_RE.fullmatch(clean["Anlage"])
            if label_match is None:
                errors.append(
                    f"Manifestzeile {row_number}: Anlage muss dem Muster K 1 oder B 1 folgen"
                )
            else:
                label = clean["Anlage"]
                if label in attachment_labels:
                    errors.append(
                        f"Manifestzeile {row_number}: Anlagenbezeichnung doppelt: {label}"
                    )
                attachment_labels.add(label)
                compact = f"{label_match.group(1)}{int(label_match.group(2)):02d}"
                if name and f"_Anlage_{compact}_" not in name:
                    errors.append(
                        f"Manifestzeile {row_number}: Anlage {label} passt nicht zum Zieldateinamen"
                    )
            if normalized(clean["Kennzeichnung"]) not in ALLOWED_ATTACHMENT_MARKING:
                errors.append(
                    f"Manifestzeile {row_number}: Anlagenkennzeichnung ist nicht freigabefähig"
                )

        pages = parse_positive_int(clean["Seiten"], "Seiten", row_number, errors)
        bytes_value = parse_positive_int(clean["Bytes"], "Bytes", row_number, errors)
        if not SHA256_RE.fullmatch(clean["SHA256"]):
            errors.append(
                f"Manifestzeile {row_number}: SHA256 muss aus 64 kleinen Hexzeichen bestehen"
            )
        if normalized(clean["OCR"]) not in ALLOWED_OCR:
            errors.append(
                f"Manifestzeile {row_number}: OCR-Status ist nicht freigabefähig"
            )
        if normalized(clean["Datenschutz"]) not in ALLOWED_PRIVACY:
            errors.append(
                f"Manifestzeile {row_number}: Datenschutzstatus ist nicht geprüft"
            )
        if normalized(clean["Status"]) != "bereit":
            errors.append(f"Manifestzeile {row_number}: Status ist nicht bereit")

        if index <= len(ordered_pdfs):
            pdf = ordered_pdfs[index - 1]
            inspection = inspections[pdf.name]
            if name != pdf.name:
                errors.append(
                    f"Manifestzeile {row_number}: erwartet {pdf.name}, vorhanden {name or '[leer]'}"
                )
            if bytes_value is not None and bytes_value != inspection.size:
                errors.append(f"{pdf.name}: Bytes im Manifest stimmen nicht")
            if clean["SHA256"] and clean["SHA256"] != inspection.sha256:
                errors.append(f"{pdf.name}: SHA256 im Manifest stimmt nicht")
            if (
                pages is not None
                and inspection.pages is not None
                and pages != inspection.pages
            ):
                errors.append(f"{pdf.name}: Seitenzahl im Manifest stimmt nicht")

    actual_names = {path.name for path in pdfs}
    manifest_names = set(by_name)
    if actual_names != manifest_names:
        errors.append(
            "Manifest und Upload unterscheiden sich: "
            f"fehlend={sorted(actual_names - manifest_names)}, "
            f"zusätzlich={sorted(manifest_names - actual_names)}"
        )

    main_rows = sum(
        1
        for row in rows
        if isinstance(row.get("Rolle"), str)
        and row["Rolle"].strip() == "Hauptschriftsatz"
    )
    if main_rows != 1:
        errors.append(
            f"Manifest muss genau einen Hauptschriftsatz enthalten, gefunden {main_rows}"
        )
    return errors, warnings


def write_test_pdf(path: Path, *, width: int = 595) -> None:
    from pypdf import PdfWriter

    writer = PdfWriter()
    writer.add_blank_page(width=width, height=842)
    with path.open("wb") as handle:
        writer.write(handle)


def test_rows(root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    specs = (
        ("01_K_Schriftsatz_Test.pdf", "Hauptschriftsatz", "", "nicht anwendbar"),
        ("02_Anlage_K01_Test.pdf", "Anlage", "K 1", "geprüft"),
    )
    for order, (name, role, attachment, marking) in enumerate(specs, start=1):
        pdf = root / "upload" / name
        inspection = inspect_pdf(pdf)
        rows.append(
            {
                "Reihenfolge": f"{order:02d}",
                "Rolle": role,
                "Anlage": attachment,
                "Quelldatei": f"quelle/{name.removesuffix('.pdf')}.docx",
                "Zieldatei": name,
                "Seiten": str(inspection.pages or ""),
                "Bytes": str(inspection.size),
                "SHA256": inspection.sha256,
                "OCR": "nicht nötig",
                "Kennzeichnung": marking,
                "Datenschutz": "geprüft",
                "Status": "bereit",
            }
        )
    return rows


def write_manifest(
    root: Path,
    rows: list[dict[str, str]],
    fieldnames: tuple[str, ...] = EXPECTED_COLUMNS,
) -> None:
    path = root / "intern" / "versandmanifest.csv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_signature_manifest(root: Path, rows: list[dict[str, str]]) -> None:
    path = root / "intern" / "signaturmanifest.csv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=SIGNATURE_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def add_test_signature(
    root: Path,
    *,
    extension: str = ".p7s",
    signature_name: str | None = None,
    target_name: str = "01_K_Schriftsatz_Test.pdf",
    payload: bytes = b"0\x03test-cades-signature",
) -> dict[str, str]:
    target = root / "upload" / target_name
    name = signature_name or f"{target_name}{extension}"
    signature = root / "upload" / name
    signature.write_bytes(payload)
    signature_count = sum(
        1 for path in (root / "upload").iterdir() if path.suffix in SIGNATURE_SUFFIXES
    )
    protocol_name = f"signaturpruefprotokoll_{signature_count:02d}.txt"
    (root / "intern" / protocol_name).write_text(
        "qeS-Prüfung erfolgreich; Testprotokoll ohne Echtheitswirkung.\n",
        encoding="utf-8",
    )
    return {
        "Signaturdatei": name,
        "Zieldokument": target_name,
        "Zieldokument_SHA256": sha256(target),
        "Bytes": str(signature.stat().st_size),
        "SHA256": sha256(signature),
        "Format": "CAdES",
        "Signaturniveau": "qeS",
        "Prüfstatus": "grün",
        "Unterzeichner": "Rechtsanwältin Test",
        "Prüfprotokoll": protocol_name,
    }


def build_test_package(root: Path) -> None:
    upload = root / "upload"
    internal = root / "intern"
    upload.mkdir(parents=True)
    internal.mkdir()
    write_test_pdf(upload / "01_K_Schriftsatz_Test.pdf")
    write_test_pdf(upload / "02_Anlage_K01_Test.pdf", width=596)
    write_manifest(root, test_rows(root))


def build_signed_test_package(
    root: Path,
    *,
    extension: str = ".p7s",
    signature_name: str | None = None,
) -> None:
    build_test_package(root)
    row = add_test_signature(root, extension=extension, signature_name=signature_name)
    write_signature_manifest(root, [row])


def mutate_row(root: Path, index: int, field: str, value: str) -> None:
    rows = test_rows(root)
    rows[index][field] = value
    write_manifest(root, rows)


def mutate_signature_row(root: Path, field: str, value: str) -> None:
    row = add_test_signature(root)
    row[field] = value
    write_signature_manifest(root, [row])


def append_test_bytes(root: Path, name: str, payload: bytes) -> None:
    with (root / "upload" / name).open("ab") as handle:
        handle.write(payload)


def replace_test_bytes(root: Path, name: str, payload: bytes) -> None:
    (root / "upload" / name).write_bytes(payload)


def append_manifest_value(root: Path) -> None:
    path = root / "intern" / "versandmanifest.csv"
    lines = path.read_text(encoding="utf-8").splitlines()
    lines[1] += ",unerwartet"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def duplicate_manifest_header(root: Path) -> None:
    write_manifest(root, test_rows(root), (*EXPECTED_COLUMNS, "Status"))


def make_upload_symlink(root: Path) -> None:
    source = root / "upload" / "02_Anlage_K01_Test.pdf"
    (root / "upload" / "03_Anlage_K02_Link.pdf").symlink_to(source.name)


def make_manifest_symlink(root: Path) -> None:
    manifest = root / "intern" / "versandmanifest.csv"
    backup = root / "intern" / "versandmanifest-original.csv"
    manifest.rename(backup)
    manifest.symlink_to(backup.name)


def make_internal_symlink(root: Path) -> None:
    internal = root / "intern"
    backup = root / "intern-real"
    internal.rename(backup)
    internal.symlink_to(backup.name)


def make_oversized_manifest(root: Path) -> None:
    path = root / "intern" / "versandmanifest.csv"
    path.write_bytes(b"X" * (MAX_MANIFEST_BYTES + 1))


def make_entry_overflow(root: Path) -> None:
    upload = root / "upload"
    for index in range(MAX_FILES - 1):
        (upload / f"extra-{index:04d}.tmp").touch()


def remove_pdf_eof(root: Path) -> None:
    path = root / "upload" / "01_K_Schriftsatz_Test.pdf"
    data = path.read_bytes()
    marker = data.rfind(b"%%EOF")
    path.write_bytes(data[:marker] if marker >= 0 else data)


def make_zero_width_pdf(root: Path) -> None:
    write_test_pdf(root / "upload" / "01_K_Schriftsatz_Test.pdf", width=0)


def make_empty_pdf(root: Path) -> None:
    from pypdf import PdfWriter

    path = root / "upload" / "01_K_Schriftsatz_Test.pdf"
    writer = PdfWriter()
    with path.open("wb") as handle:
        writer.write(handle)


def make_signature_without_manifest(root: Path) -> None:
    (root / "upload" / "01_K_Schriftsatz_Test.pdf.p7s").write_bytes(
        b"0\x03test-cades-signature"
    )


def make_signature_without_artifact(root: Path) -> None:
    row = add_test_signature(root)
    (root / "upload" / row["Signaturdatei"]).unlink()
    write_signature_manifest(root, [row])


def make_signature_without_protocol(root: Path) -> None:
    row = add_test_signature(root)
    (root / "intern" / row["Prüfprotokoll"]).unlink()
    write_signature_manifest(root, [row])


def make_duplicate_signature_content(root: Path) -> None:
    first = add_test_signature(root)
    second = add_test_signature(
        root,
        signature_name="externe_zweitsignatur.p7s",
        payload=b"0\x03test-cades-signature",
    )
    write_signature_manifest(root, [first, second])


def validate_quietly_for_selftest(package: Path) -> tuple[list[str], list[str]]:
    with redirect_stderr(io.StringIO()):
        return validate(package)


def selftest() -> int:
    try:
        import pypdf  # noqa: F401
    except ImportError:
        print("Selbsttest benötigt pypdf", file=sys.stderr)
        return 1

    started = time.perf_counter()
    checked = 0
    valid_names = ("01_K_Test.pdf", "02_Anlage_K01_Test.pdf")
    for name in valid_names:
        if filename_errors(name, 2):
            print(f"Selbsttest verwirft gültigen Dateinamen: {name}", file=sys.stderr)
            return 1
        checked += 1

    forbidden_ascii = [
        chr(code)
        for code in (
            *range(33, 48),
            *range(58, 65),
            *range(91, 95),
            96,
            *range(123, 127),
        )
        if chr(code) not in {"-"}
    ]
    invalid_names = [f"01_K_Test{char}X.pdf" for char in forbidden_ascii]
    invalid_names.extend(f"01_K_Test{chr(code)}.pdf" for code in range(0x00C0, 0x0120))
    invalid_names.extend(
        [
            "",
            "01.pdf",
            "1_K_Test.pdf",
            "001_K_Test.pdf",
            "01__K_Test.pdf",
            "01_K__Test.pdf",
            "01_K_Test_.pdf",
            "01_K_Test-.pdf",
            "01_-K_Test.pdf",
            "01_K Test.pdf",
            "01_K.Test.pdf",
            "01_K_Test.PDF",
            "01_K_Test.pdf.exe",
            "01/K_Test.pdf",
            "01\\K_Test.pdf",
            "00_K_Test.pdf",
            f"01_{'A' * 76}.pdf",
        ]
    )
    for name in invalid_names:
        if not filename_errors(name, 2):
            print(
                f"Selbsttest übersieht ungültigen Dateinamen: {name!r}", file=sys.stderr
            )
            return 1
        checked += 1

    Mutation = tuple[str, Callable[[Path], None], str]
    mutations: list[Mutation] = [
        ("leeres Manifest", lambda root: write_manifest(root, []), "keine Dateizeile"),
        (
            "falsche Kopfzeile",
            lambda root: write_manifest(root, test_rows(root), EXPECTED_COLUMNS[:-1]),
            "Manifestkopf ist nicht exakt",
        ),
        (
            "absolute Quelle",
            lambda root: mutate_row(root, 0, "Quelldatei", "/tmp/Schriftsatz.docx"),
            "sicherer relativer Pfad",
        ),
        (
            "Windows-Quelle",
            lambda root: mutate_row(root, 0, "Quelldatei", "C:/tmp/Schriftsatz.docx"),
            "sicherer relativer Pfad",
        ),
        (
            "Pfadaufstieg",
            lambda root: mutate_row(root, 0, "Quelldatei", "../Schriftsatz.docx"),
            "sicherer relativer Pfad",
        ),
        (
            "Pfadpunkt innen",
            lambda root: mutate_row(root, 0, "Quelldatei", "quelle/./Schriftsatz.docx"),
            "sicherer relativer Pfad",
        ),
        (
            "Rückwärtsschrägstrich",
            lambda root: mutate_row(root, 0, "Quelldatei", "quelle\\Schriftsatz.docx"),
            "sicherer relativer Pfad",
        ),
        (
            "Tabellenformel",
            lambda root: mutate_row(root, 0, "Quelldatei", "=HYPERLINK('x')"),
            "Tabellenformel",
        ),
        (
            "falscher Status",
            lambda root: mutate_row(root, 0, "Status", "gelb"),
            "Status ist nicht bereit",
        ),
        (
            "OCR fehlgeschlagen",
            lambda root: mutate_row(root, 1, "OCR", "fehlgeschlagen"),
            "OCR-Status ist nicht freigabefähig",
        ),
        (
            "Datenschutz offen",
            lambda root: mutate_row(root, 1, "Datenschutz", "Stopp"),
            "Datenschutzstatus ist nicht geprüft",
        ),
        (
            "Hashformat",
            lambda root: mutate_row(root, 0, "SHA256", "ABC"),
            "64 kleinen Hexzeichen",
        ),
        (
            "falsche Bytes",
            lambda root: mutate_row(root, 0, "Bytes", "1"),
            "Bytes im Manifest stimmen nicht",
        ),
        (
            "falsche Seiten",
            lambda root: mutate_row(root, 0, "Seiten", "2"),
            "Seitenzahl im Manifest stimmt nicht",
        ),
        (
            "negative Seiten",
            lambda root: mutate_row(root, 0, "Seiten", "-1"),
            "positive Ganzzahl",
        ),
        (
            "Anlage ohne Label",
            lambda root: mutate_row(root, 1, "Anlage", ""),
            "Muster K 1 oder B 1",
        ),
        (
            "Anlagenkonflikt",
            lambda root: mutate_row(root, 1, "Anlage", "B 3"),
            "passt nicht zum Zieldateinamen",
        ),
        (
            "Hauptrolle falsch",
            lambda root: mutate_row(root, 0, "Rolle", "Anlage"),
            "Datei 01 muss Hauptschriftsatz sein",
        ),
        (
            "Anlagenrolle falsch",
            lambda root: mutate_row(root, 1, "Rolle", "Hauptschriftsatz"),
            "Dateien nach 01 müssen Anlagen sein",
        ),
        (
            "Manifestreihenfolge",
            lambda root: mutate_row(root, 1, "Reihenfolge", "03"),
            "Reihenfolge muss exakt 02 sein",
        ),
        (
            "Zielpfad",
            lambda root: mutate_row(
                root, 0, "Zieldatei", "upload/01_K_Schriftsatz_Test.pdf"
            ),
            "darf keinen Pfad enthalten",
        ),
        (
            "Rand-Leerzeichen",
            lambda root: mutate_row(root, 0, "Rolle", " Hauptschriftsatz"),
            "Rand-Leerzeichen",
        ),
        (
            "CSV-Steuerzeichen",
            lambda root: mutate_row(root, 0, "Rolle", "Haupt\x01schriftsatz"),
            "enthält Steuerzeichen",
        ),
        (
            "zusätzlicher CSV-Wert",
            append_manifest_value,
            "zusätzliche CSV-Werte",
        ),
        (
            "doppelter CSV-Kopf",
            duplicate_manifest_header,
            "Manifestkopf ist nicht exakt",
        ),
        (
            "Manifest-Symlink",
            make_manifest_symlink,
            "Manifest darf kein Symlink sein",
        ),
        (
            "interner Symlink",
            make_internal_symlink,
            "Interner Paketordner darf kein Symlink sein",
        ),
        (
            "übergroßes Manifest",
            make_oversized_manifest,
            "überschreitet die interne Obergrenze",
        ),
        (
            "übergroßer Upload-Ordner",
            make_entry_overflow,
            "mehr als 1000 Einträge",
        ),
        (
            "Nicht-PDF",
            lambda root: (root / "upload" / "hinweis.txt").write_text("x"),
            "erlaubt nur PDF und zugeordnete CAdES-Signaturdateien",
        ),
        (
            "Signatur ohne Manifest",
            make_signature_without_manifest,
            "Signaturmanifest fehlt",
        ),
        (
            "unbekanntes Signaturformat",
            lambda root: (root / "upload" / "Signatur.sig").write_bytes(b"x"),
            "erlaubt nur PDF und zugeordnete CAdES-Signaturdateien",
        ),
        (
            "Signaturdateiname nicht ASCII",
            lambda root: (
                (root / "upload" / "Signatur_Ü.p7s").write_bytes(b"x"),
                write_signature_manifest(root, []),
            ),
            "Signaturdateiname ist nicht ASCII",
        ),
        (
            "Signatur ohne Artefakt",
            make_signature_without_artifact,
            "Signaturmanifest ist vorhanden, aber im Upload liegt keine separate Signaturdatei",
        ),
        (
            "Signatur ohne Ziel-PDF",
            lambda root: mutate_signature_row(
                root, "Zieldokument", "99_K_Unbekannt.pdf"
            ),
            "Zieldokument fehlt im Upload",
        ),
        (
            "falscher Zielhash",
            lambda root: mutate_signature_row(root, "Zieldokument_SHA256", "0" * 64),
            "Zielhash passt nicht",
        ),
        (
            "falscher Signaturhash",
            lambda root: mutate_signature_row(root, "SHA256", "0" * 64),
            "SHA256 im Signaturmanifest stimmt nicht",
        ),
        (
            "falsche Signaturbytes",
            lambda root: mutate_signature_row(root, "Bytes", "1"),
            "Bytes im Signaturmanifest stimmen nicht",
        ),
        (
            "falsches Signaturformat",
            lambda root: mutate_signature_row(root, "Format", "PAdES"),
            "Format muss CAdES sein",
        ),
        (
            "keine qeS",
            lambda root: mutate_signature_row(root, "Signaturniveau", "feS"),
            "Signaturniveau muss qeS sein",
        ),
        (
            "Signaturprüfung nicht grün",
            lambda root: mutate_signature_row(root, "Prüfstatus", "gelb"),
            "qeS-Prüfstatus muss grün sein",
        ),
        (
            "Signatur ohne Prüfprotokoll",
            make_signature_without_protocol,
            "Prüfprotokoll fehlt",
        ),
        (
            "identische Signaturartefakte",
            make_duplicate_signature_content,
            "Inhaltsgleiche Signaturdateien sind nicht eindeutig",
        ),
        (
            "Unterordner",
            lambda root: (root / "upload" / "intern").mkdir(),
            "Unterordner im Upload-Ordner",
        ),
        ("Upload-Symlink", make_upload_symlink, "Symlink im Upload-Ordner"),
        (
            "aktiver Inhalt",
            lambda root: append_test_bytes(
                root, "01_K_Schriftsatz_Test.pdf", b"\n/Launch\n"
            ),
            "Startaktion",
        ),
        (
            "eingebettete Datei",
            lambda root: append_test_bytes(
                root, "01_K_Schriftsatz_Test.pdf", b"\n/EmbeddedFile\n"
            ),
            "eingebettete Dateien",
        ),
        (
            "JavaScript",
            lambda root: append_test_bytes(
                root, "01_K_Schriftsatz_Test.pdf", b"\n/JavaScript\n"
            ),
            "JavaScript",
        ),
        (
            "XFA-Formular",
            lambda root: append_test_bytes(
                root, "01_K_Schriftsatz_Test.pdf", b"\n/XFA\n"
            ),
            "dynamisches XFA-Formular",
        ),
        ("fehlendes PDF-Ende", remove_pdf_eof, "PDF-Endemarkierung fehlt"),
        ("leere PDF", make_empty_pdf, "PDF enthält keine Seite"),
        ("ungültige Seitengröße", make_zero_width_pdf, "keine gültige MediaBox"),
        (
            "falscher PDF-Header",
            lambda root: replace_test_bytes(
                root, "01_K_Schriftsatz_Test.pdf", b"kein PDF"
            ),
            "kein echter PDF-Header",
        ),
        (
            "falsche Sequenz",
            lambda root: (root / "upload" / "02_Anlage_K01_Test.pdf").rename(
                root / "upload" / "03_Anlage_K01_Test.pdf"
            ),
            "nicht lückenlos",
        ),
        (
            "fehlendes Manifest",
            lambda root: (root / "intern" / "versandmanifest.csv").unlink(),
            "Manifest fehlt",
        ),
    ]

    with tempfile.TemporaryDirectory(prefix="bea-package-selftest-") as temp:
        base = Path(temp)
        valid = base / "valid"
        build_test_package(valid)
        errors, warnings = validate_quietly_for_selftest(valid)
        if errors or warnings:
            print(
                f"Selbsttest-Basispaket fehlerhaft: {errors} {warnings}",
                file=sys.stderr,
            )
            return 1
        checked += 1

        for extension in sorted(SIGNATURE_SUFFIXES):
            signed = base / f"valid-signature-{extension.removeprefix('.')}"
            build_signed_test_package(signed, extension=extension)
            errors, warnings = validate_quietly_for_selftest(signed)
            if errors or warnings:
                print(
                    f"Selbsttest verwirft gültiges CAdES-Artefakt {extension}: "
                    f"{errors} {warnings}",
                    file=sys.stderr,
                )
                return 1
            checked += 1
            shutil.rmtree(signed)

        for case_number, (label, mutate, expected) in enumerate(mutations, start=1):
            root = base / f"case-{case_number:02d}"
            build_test_package(root)
            mutate(root)
            errors, _ = validate_quietly_for_selftest(root)
            if not any(expected in error for error in errors):
                print(
                    f"Selbsttest übersieht {label}: erwartet {expected!r}, erhalten {errors}",
                    file=sys.stderr,
                )
                return 1
            checked += 1
            shutil.rmtree(root)

    elapsed = time.perf_counter() - started
    print(f"validate_bea_package Selbsttest OK: {checked} Prüffälle in {elapsed:.2f}s")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prüft ein _bea_ausgabe-Paket schreibgeschützt gegen den Werkstattstandard."
    )
    parser.add_argument("package", nargs="?", type=Path)
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    if args.package is None:
        parser.error("package oder --selftest erforderlich")
    errors, warnings = validate(args.package)
    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"FEHLER: {error}", file=sys.stderr)
        print(f"validate_bea_package: {len(errors)} Fehler", file=sys.stderr)
        return 1
    print("validate_bea_package OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

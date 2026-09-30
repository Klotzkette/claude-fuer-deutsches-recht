#!/usr/bin/env python3
"""Validate a court-facing beA package, its manifest and bound approval."""

from __future__ import annotations

import argparse
import hashlib
import html
import io
import json
import os
import re
import stat
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from bea_common import (
    APPROVAL_CONFIRMATIONS,
    APPROVAL_SCHEMA_VERSION,
    ContractError,
    MANIFEST_SCHEMA_VERSION,
    MAX_EXHIBIT_NUMBER,
    MAX_PDF_BYTES,
    REPORT_SCHEMA_VERSION,
    digest_json,
    exhibit_filename,
    hash_stable,
    load_json,
    main_filename,
    normalized_token,
    package_fingerprint,
    read_stable,
    validate_approval,
    validate_manifest,
    validate_order,
    validate_pdf_dimensions,
    validate_pdf_page_count,
)

try:
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import ArrayObject, DictionaryObject, IndirectObject
except ImportError:  # The raw-byte safety profile remains usable without optional PDF packages.
    PdfReader = PdfWriter = None
    ArrayObject = DictionaryObject = IndirectObject = ()  # type: ignore[assignment]


MAX_FILES = 1000
MAX_BYTES = 200 * 1024 * 1024
SOFT_BYTES = 190 * 1024 * 1024
MAX_NAME_LENGTH = 90
SOFT_NAME_LENGTH = 80
MAX_CLOCK_SKEW = timedelta(minutes=5)
ASCII_PDF_NAME = re.compile(r"^[A-Za-z0-9_-]+\.pdf$")
SHORT_CODE = re.compile(r"^[A-Za-z]{1,6}$")
NAME_BODY = r"[A-Za-z0-9](?:[A-Za-z0-9_-]*[A-Za-z0-9])?"
EXHIBIT_NAME = re.compile(
    rf"^(?P<order>\d{{2,3}})_Anlage_(?P<prefix>[A-Z]{{1,6}})"
    rf"(?P<number>[1-9][0-9]{{0,5}})_"
    rf"(?P<description>{NAME_BODY})\.pdf$"
)
PDF_VERSION = re.compile(rb"^%PDF-(?:1\.[0-7]|2\.0)(?:\r?\n|\r)")
PDF_FORBIDDEN = {
    "Verschlüsselung": re.compile(rb"/Encrypt\b"),
    "JavaScript-/Script-Hinweis": re.compile(rb"/(?:JavaScript|JS)\b"),
    "eingebettete Datei oder Objekt": re.compile(rb"/(?:EmbeddedFile|Filespec)\b"),
    "ausführbare Launch-Aktion": re.compile(rb"/Launch\b"),
    "aktive Formularaktion": re.compile(rb"/(?:SubmitForm|ImportData)\b"),
    "aktive Multimedia-/3D-Komponente": re.compile(rb"/(?:RichMedia|Movie|Sound|3D)\b"),
}
DEEP_FORBIDDEN_KEYS = {
    "/Encrypt": "Verschlüsselung",
    "/JavaScript": "JavaScript-/Script-Hinweis",
    "/JS": "JavaScript-/Script-Hinweis",
    "/EmbeddedFile": "eingebettete Datei oder Objekt",
    "/Filespec": "eingebettete Datei oder Objekt",
    "/Launch": "ausführbare Launch-Aktion",
    "/SubmitForm": "aktive Formularaktion",
    "/ImportData": "aktive Formularaktion",
    "/RichMedia": "aktive Multimedia-/3D-Komponente",
    "/Movie": "aktive Multimedia-/3D-Komponente",
    "/Sound": "aktive Multimedia-/3D-Komponente",
    "/3D": "aktive Multimedia-/3D-Komponente",
}


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Prüft beA-Versanddateien gegen Paketmanifest und hashgebundene anwaltliche Freigabe."
        )
    )
    parser.add_argument("package", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--role", default="K", help="Rollenpräfix des Hauptdokuments, z. B. K oder B")
    parser.add_argument("--anlagen-prefix", default="K", help="Anlagenpräfix, z. B. K oder B")
    parser.add_argument(
        "--start",
        type=parse_exhibit_start,
        default=1,
        help="Erste Anlagenzahl im Paket (1 bis 999999)",
    )
    parser.add_argument("--expected-az", help="Aktenzeichen, das im Hauptdateinamen erwartet wird")
    parser.add_argument("--manifest", type=Path, help="Paketmanifest; Standard: kontrolle/paket-manifest.json")
    parser.add_argument("--approval", type=Path, help="Freigabe; Standard: kontrolle/freigabe.json")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--report", type=Path, help="Prüfbericht zusätzlich als JSON schreiben")
    parser.add_argument("--selftest", action="store_true")
    return parser


def parse_exhibit_start(value: str) -> int:
    if re.fullmatch(r"[1-9][0-9]{0,5}", value) is None:
        raise argparse.ArgumentTypeError(
            f"--start muss eine kanonische ASCII-Ganzzahl zwischen 1 und {MAX_EXHIBIT_NUMBER} sein"
        )
    return int(value)


def _resolve_send_dir(package: Path) -> Path:
    package = package.expanduser().absolute()
    candidate = package / "versand"
    return candidate if candidate.is_dir() else package


def _resolve_control_file(package: Path, explicit: Path | None, name: str) -> Path:
    if explicit is not None:
        return explicit.expanduser().absolute()
    root = package.expanduser().absolute()
    if root.name == "versand":
        root = root.parent
    return root / "kontrolle" / name


def inspect_pdf(name: str, content: bytes) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if PDF_VERSION.search(content) is None:
        errors.append(f"{name}: ungültiger oder nicht unterstützter PDF-Dateikopf")
        return errors, warnings
    if b"%%EOF" not in content[-2048:]:
        errors.append(f"{name}: PDF-Endemarkierung fehlt oder liegt nicht am Dateiende")
    for label, pattern in PDF_FORBIDDEN.items():
        if pattern.search(content):
            errors.append(f"{name}: {label}")
    if re.search(rb"/OpenAction\b", content):
        warnings.append(f"{name}: OpenAction manuell auf Unbedenklichkeit prüfen")
    if re.search(rb"/AA\b", content):
        warnings.append(f"{name}: zusätzliche Seiten-/Feldaktion manuell prüfen")
    if re.search(rb"/ByteRange\b", content):
        warnings.append(f"{name}: Signaturhinweis; Integrität und Signaturstatus manuell prüfen")
    if len(content) < 100:
        warnings.append(f"{name}: ungewöhnlich kleine PDF-Datei")
    return errors, warnings


def _deep_object_keys(value: Any, found: set[str], seen: set[tuple[int, int]], budget: list[int]) -> None:
    if budget[0] <= 0:
        raise ValueError("PDF-Objektprüfung überschreitet Sicherheitsbudget")
    budget[0] -= 1
    if PdfReader is None:
        return
    if isinstance(value, IndirectObject):
        marker = (value.idnum, value.generation)
        if marker in seen:
            return
        seen.add(marker)
        _deep_object_keys(value.get_object(), found, seen, budget)
        return
    if isinstance(value, DictionaryObject):
        for key, child in value.items():
            key_text = str(key)
            if key_text in DEEP_FORBIDDEN_KEYS:
                found.add(DEEP_FORBIDDEN_KEYS[key_text])
            _deep_object_keys(child, found, seen, budget)
        return
    if isinstance(value, ArrayObject):
        for child in value:
            _deep_object_keys(child, found, seen, budget)


def inspect_pdf_deep(
    name: str,
    content: bytes,
    expected_label: str | None,
    require_extractable_label: bool,
) -> tuple[list[str], list[str], str, int | None]:
    if PdfReader is None:
        return [], [], "rohtext", None
    errors: list[str] = []
    warnings: list[str] = []
    try:
        reader = PdfReader(io.BytesIO(content), strict=True)
        if reader.is_encrypted:
            errors.append(f"{name}: PDF ist verschlüsselt")
            return errors, warnings, "pypdf", None
        page_count = len(reader.pages)
        try:
            validate_pdf_page_count(page_count, f"{name}.Seitenzahl")
        except ContractError as exc:
            errors.append(str(exc))
        else:
            for index, page in enumerate(reader.pages, start=1):
                try:
                    validate_pdf_dimensions(
                        page.mediabox.width,
                        page.mediabox.height,
                        f"{name}.Seite[{index}].MediaBox",
                    )
                    validate_pdf_dimensions(
                        page.cropbox.width,
                        page.cropbox.height,
                        f"{name}.Seite[{index}].CropBox",
                    )
                except ContractError as exc:
                    errors.append(str(exc))
                    break
        found: set[str] = set()
        _deep_object_keys(reader.trailer, found, set(), [100_000])
        for label in sorted(found):
            errors.append(f"{name}: {label} in der PDF-Objektstruktur")
        if require_extractable_label and expected_label:
            first_text = reader.pages[0].extract_text() or "" if reader.pages else ""
            if expected_label not in first_text:
                errors.append(f"{name}: erwarteter sichtbarer Textstempel {expected_label!r} nicht extrahierbar")
    except Exception as exc:
        errors.append(f"{name}: PDF-Tiefenprüfung fehlgeschlagen: {exc}")
        page_count = None
    return errors, warnings, "pypdf", page_count


def normalized_code(value: str, label: str, errors: list[str]) -> str:
    cleaned = value.strip().upper()
    if SHORT_CODE.fullmatch(cleaned) is None:
        errors.append(f"{label} muss aus 1 bis 6 ASCII-Buchstaben bestehen")
        return "INVALID"
    return cleaned


def markdown_text(value: object) -> str:
    text = str(value).replace("\r", " ").replace("\n", " ")
    text = html.escape(" ".join(text.split()), quote=False)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("`", "&#96;")


def write_report(path: Path, rendered: str, send_dir: Path) -> None:
    requested = path.expanduser().absolute()
    if requested.is_symlink():
        raise ValueError("Prüfbericht darf kein symbolischer Link sein")
    target = requested.resolve(strict=False)
    resolved_send = send_dir.resolve(strict=True)
    if target == resolved_send or resolved_send in target.parents:
        raise ValueError("Prüfbericht darf nicht im Versandverzeichnis liegen")
    if target.exists():
        if not target.is_file():
            raise ValueError("Prüfbericht-Ziel ist keine reguläre Datei")
        try:
            previous = load_json(target)
        except ContractError as exc:
            raise ValueError("Vorhandenes Ziel ist kein früherer beA-Prüfbericht") from exc
        if previous.get("schema_version") != REPORT_SCHEMA_VERSION or "status" not in previous:
            raise ValueError("Vorhandenes Ziel ist kein früherer beA-Prüfbericht")
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, raw_temp = tempfile.mkstemp(prefix=f".{target.name}.", suffix=".tmp", dir=target.parent)
    temporary = Path(raw_temp)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(rendered)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)


def _validate_order_manifest(
    order: dict[str, Any],
    manifest: dict[str, Any],
    errors: list[str],
) -> None:
    order_hash = digest_json(order)
    if manifest["order_sha256"] != order_hash:
        errors.append("Paketauftrag: normalisierter Auftrag und Manifest-Hash weichen ab")
    if manifest["matter"] != order["matter"]:
        errors.append("Paketauftrag: Vorgangsmetadaten weichen vom Paketmanifest ab")
    if manifest["main_document"]["input_sha256"] != order["main_document"]["approved_sha256"]:
        errors.append("Paketauftrag: freigegebener Hauptdokument-Hash weicht vom Manifest ab")
    if manifest["main_document"]["source_name"] != Path(order["main_document"]["source"]).name:
        errors.append("Paketauftrag: Hauptdokument-Quellname weicht vom Manifest ab")
    expected_main_name = main_filename(order["matter"])
    if manifest["main_document"]["versand_name"] != expected_main_name:
        errors.append("Paketauftrag: Hauptdokument-Dateiname weicht vom Auftrag ab")
    if len(order["exhibits"]) != len(manifest["exhibits"]):
        errors.append("Paketauftrag: Anlagenzahl weicht vom Manifest ab")
        return
    for index, (ordered, produced) in enumerate(zip(order["exhibits"], manifest["exhibits"]), start=1):
        for source_key, manifest_key in (
            ("number", "number"),
            ("title", "title"),
            ("document_date", "document_date"),
            ("reference", "reference"),
            ("stamp_mode", "stamp_mode"),
            ("expected_sha256", "input_sha256"),
        ):
            if ordered[source_key] != produced[manifest_key]:
                errors.append(
                    f"Paketauftrag: Anlage {index} Feld {source_key} weicht vom Manifest ab"
                )
        if Path(ordered["source"]).name != produced["source_name"]:
            errors.append(f"Paketauftrag: Anlage {index} Quellname weicht vom Manifest ab")
        expected_name = exhibit_filename(
            index,
            len(order["exhibits"]),
            ordered,
            order["matter"]["exhibit_prefix"],
        )
        if produced["versand_name"] != expected_name:
            errors.append(f"Paketauftrag: Anlage {index} Versanddateiname weicht vom Auftrag ab")


def _validate_original_trace(
    package_root: Path,
    send_dir: Path,
    manifest: dict[str, Any],
    errors: list[str],
) -> None:
    original_dir = package_root / "original"
    if not original_dir.is_dir() or original_dir.is_symlink():
        errors.append(f"Originalspur fehlt oder ist unsicher: {original_dir}")
        return
    expected = {
        manifest["main_document"]["original_name"]: (
            manifest["main_document"]["input_sha256"],
            manifest["main_document"]["versand_name"],
        )
    }
    for exhibit in manifest["exhibits"]:
        expected[exhibit["original_name"]] = (
            exhibit["input_sha256"],
            exhibit["versand_name"],
        )
    actual: dict[str, Path] = {}
    identities: dict[tuple[int, int], str] = {}
    try:
        entries = sorted(original_dir.iterdir(), key=lambda item: item.name)
    except OSError as exc:
        errors.append(f"Originalspur kann nicht gelesen werden: {exc}")
        return
    for path in entries:
        try:
            status = path.lstat()
            mode = status.st_mode
        except OSError as exc:
            errors.append(f"Originalspur {path.name}: Dateistatus nicht lesbar: {exc}")
            continue
        if stat.S_ISLNK(mode) or not stat.S_ISREG(mode):
            errors.append(f"Originalspur {path.name}: nur reguläre Dateien, keine Links/Ordner zulässig")
            continue
        identity = (status.st_dev, status.st_ino)
        if identity in identities:
            errors.append(
                f"Originalspur {path.name}: Hardlink-Dublette zu {identities[identity]} ist unzulässig"
            )
        else:
            identities[identity] = path.name
        actual[path.name] = path
    missing = sorted(set(expected) - set(actual))
    unexpected = sorted(set(actual) - set(expected))
    if missing:
        errors.append(f"Originalspur: Dateien fehlen: {', '.join(missing)}")
    if unexpected:
        errors.append(f"Originalspur: unerwartete Dateien: {', '.join(unexpected)}")
    for name in sorted(set(expected) & set(actual)):
        expected_hash, send_name = expected[name]
        try:
            _, digest = hash_stable(actual[name], max_bytes=MAX_PDF_BYTES)
        except (OSError, ContractError) as exc:
            errors.append(f"Originalspur {name}: stabile Prüfung fehlgeschlagen: {exc}")
            continue
        if digest != expected_hash:
            errors.append(f"Originalspur {name}: Hash weicht vom Paketmanifest ab")
        send_path = send_dir / send_name
        try:
            if send_path.exists() and actual[name].samefile(send_path):
                errors.append(f"Originalspur {name}: Original und Versanddatei sind derselbe Hardlink")
        except OSError as exc:
            errors.append(f"Originalspur {name}: Hardlink-Prüfung fehlgeschlagen: {exc}")


def _validate_manifest_relations(
    manifest: dict[str, Any],
    files_payload: list[dict[str, Any]],
    role: str,
    exhibit_prefix: str,
    start: int,
    expected_docket: str | None,
    page_counts: dict[str, int],
    errors: list[str],
) -> None:
    matter = manifest["matter"]
    if matter["role"] != role:
        errors.append(f"Paketmanifest: Rolle {matter['role']} statt {role}")
    if matter["exhibit_prefix"] != exhibit_prefix:
        errors.append(f"Paketmanifest: Anlagenpräfix {matter['exhibit_prefix']} statt {exhibit_prefix}")
    if matter["first_exhibit_number"] != start:
        errors.append(f"Paketmanifest: erste Anlagenzahl {matter['first_exhibit_number']} statt {start}")
    if expected_docket:
        expected_token = normalized_token(expected_docket)
        actual_token = normalized_token(matter["docket"] or "Neueingang")
        if not expected_token or expected_token.casefold() != actual_token.casefold():
            errors.append(f"Paketmanifest: erwartetes Aktenzeichen passt nicht: {expected_docket}")

    expected_files: dict[str, dict[str, Any]] = {}
    for item in manifest["files"]:
        expected_files[item["name"]] = item
    actual_files = {item["name"]: item for item in files_payload}
    missing = sorted(set(expected_files) - set(actual_files))
    unexpected = sorted(set(actual_files) - set(expected_files))
    if missing:
        errors.append(f"Paketmanifest: Versanddateien fehlen: {', '.join(missing)}")
    if unexpected:
        errors.append(f"Paketmanifest: nicht freigegebene Versanddateien vorhanden: {', '.join(unexpected)}")
    for name in sorted(set(expected_files) & set(actual_files)):
        expected = expected_files[name]
        actual = actual_files[name]
        for key in ("kind", "bytes", "sha256"):
            if expected[key] != actual[key]:
                errors.append(f"Paketmanifest: {name} {key} weicht ab")

    main = manifest["main_document"]
    if main["versand_name"] not in expected_files:
        errors.append("Paketmanifest: Hauptdokument fehlt in files")
    elif expected_files[main["versand_name"]]["kind"] != "hauptdokument":
        errors.append("Paketmanifest: Hauptdokument hat falsche Art")
    if main["input_sha256"] != main["versand_sha256"]:
        errors.append("Paketmanifest: Hauptdokument wurde gegenüber der freigegebenen Endfassung verändert")

    expected_orders = list(range(1, len(manifest["exhibits"]) + 1))
    actual_orders = [item["order"] for item in manifest["exhibits"]]
    if actual_orders != expected_orders:
        errors.append(f"Paketmanifest: Anlagenreihenfolge nicht lückenlos: {actual_orders}")
    expected_numbers = list(range(start, start + len(manifest["exhibits"])))
    actual_numbers = [item["number"] for item in manifest["exhibits"]]
    if actual_numbers != expected_numbers:
        errors.append(f"Paketmanifest: Anlagennummern nicht lückenlos ab {start}: {actual_numbers}")
    for item in manifest["exhibits"]:
        expected_label = f"Anlage {exhibit_prefix}{item['number']}"
        if item["label"] != expected_label:
            errors.append(f"Paketmanifest: Label {item['label']} statt {expected_label}")
        file_item = expected_files.get(item["versand_name"])
        if file_item is None:
            errors.append(f"Paketmanifest: Anlage fehlt in files: {item['versand_name']}")
        elif file_item["kind"] != "anlage" or file_item["label"] != item["label"]:
            errors.append(f"Paketmanifest: Anlagenzuordnung widersprüchlich: {item['versand_name']}")
        if file_item and (
            file_item["sha256"] != item["versand_sha256"] or file_item["bytes"] != item["bytes"]
        ):
            errors.append(f"Paketmanifest: Hash/Größe der Anlage widersprüchlich: {item['versand_name']}")
        actual_pages = page_counts.get(item["versand_name"])
        if actual_pages is not None and actual_pages != item["output_pages"]:
            errors.append(
                f"Paketmanifest: Seitenzahl der Anlage {item['versand_name']} "
                f"ist {actual_pages} statt {item['output_pages']}"
            )

    calculated_fingerprint = package_fingerprint(manifest)
    if calculated_fingerprint != manifest["package_fingerprint"]:
        errors.append("Paketmanifest: package_fingerprint ist ungültig")


def validate_package(
    package: Path,
    role: str,
    exhibit_prefix: str,
    start: int,
    expected_docket: str | None,
    manifest_path: Path | None = None,
    approval_path: Path | None = None,
) -> dict[str, Any]:
    requested_package = package.expanduser().absolute()
    send_dir = _resolve_send_dir(package)
    package_root = send_dir.parent if send_dir.name == "versand" else requested_package
    errors: list[str] = []
    warnings: list[str] = []
    files_payload: list[dict[str, Any]] = []
    page_counts: dict[str, int] = {}
    inspection_level = "pypdf+rohtext" if PdfReader is not None else "rohtext"
    approval: dict[str, Any] = {
        "provided": False,
        "valid": False,
        "approved_by": None,
        "approved_at": None,
        "package_fingerprint": None,
    }
    manifest: dict[str, Any] | None = None
    order: dict[str, Any] | None = None
    manifest_location = _resolve_control_file(requested_package, manifest_path, "paket-manifest.json")
    order_location = _resolve_control_file(
        requested_package, None, "paketauftrag-normalisiert.json"
    )
    approval_location = _resolve_control_file(requested_package, approval_path, "freigabe.json")

    if PdfReader is None:
        warnings.append(
            "pypdf fehlt; ohne PDF-Objekt- und Stempeltiefenprüfung ist keine Versandfreigabe möglich"
        )

    if requested_package.is_symlink():
        errors.append(f"Paketpfad darf kein symbolischer Link sein: {requested_package}")
    if not send_dir.is_dir():
        errors.append(f"Versandverzeichnis fehlt: {send_dir}")
    elif send_dir.is_symlink():
        errors.append(f"Versandverzeichnis darf kein symbolischer Link sein: {send_dir}")

    role = normalized_code(role, "Rolle", errors)
    exhibit_prefix = normalized_code(exhibit_prefix, "Anlagenpräfix", errors)
    if (
        not isinstance(start, int)
        or isinstance(start, bool)
        or not 1 <= start <= MAX_EXHIBIT_NUMBER
    ):
        errors.append(
            f"Erste Anlagenzahl muss eine ganze Zahl zwischen 1 und {MAX_EXHIBIT_NUMBER} sein"
        )
        start = 1

    if manifest_location.is_file() and not manifest_location.is_symlink():
        try:
            manifest = validate_manifest(load_json(manifest_location))
            manifest_time = datetime.fromisoformat(manifest["created_at"].replace("Z", "+00:00"))
            if manifest_time.astimezone(timezone.utc) > datetime.now(timezone.utc) + MAX_CLOCK_SKEW:
                raise ContractError("Paketmanifest.created_at liegt unplausibel in der Zukunft")
        except ContractError as exc:
            errors.append(f"Paketmanifest ungültig: {exc}")
            manifest = None
    else:
        errors.append(f"Paketmanifest fehlt oder ist unsicher: {manifest_location}")
    if order_location.is_file() and not order_location.is_symlink():
        try:
            order = validate_order(load_json(order_location))
        except ContractError as exc:
            errors.append(f"Paketauftrag ungültig: {exc}")
    else:
        errors.append(f"Normalisierter Paketauftrag fehlt oder ist unsicher: {order_location}")
    if order is not None and manifest is not None:
        try:
            _validate_order_manifest(order, manifest, errors)
        except (KeyError, TypeError, ContractError) as exc:
            errors.append(f"Paketauftrag-/Manifest-Beziehung ungültig: {exc}")

    regular_files: list[Path] = []
    regular_identities: dict[tuple[int, int], str] = {}
    if send_dir.is_dir() and not send_dir.is_symlink():
        try:
            entries = sorted(send_dir.iterdir(), key=lambda path: path.name)
        except OSError as exc:
            errors.append(f"Versandverzeichnis kann nicht gelesen werden: {exc}")
            entries = []
        for path in entries:
            try:
                status = path.lstat()
                mode = status.st_mode
            except OSError as exc:
                errors.append(f"{path.name}: Dateistatus nicht lesbar: {exc}")
                continue
            if stat.S_ISLNK(mode):
                errors.append(f"{path.name}: symbolische Links sind im Versandverzeichnis verboten")
            elif stat.S_ISDIR(mode):
                errors.append(f"{path.name}: Versandverzeichnis muss flach sein; Unterordner sind verboten")
            elif not stat.S_ISREG(mode):
                errors.append(f"{path.name}: nur reguläre Dateien sind zulässig")
            else:
                identity = (status.st_dev, status.st_ino)
                if identity in regular_identities:
                    errors.append(
                        f"{path.name}: Hardlink-Dublette zu {regular_identities[identity]} ist unzulässig"
                    )
                else:
                    regular_identities[identity] = path.name
                regular_files.append(path)

    casefold_names: dict[str, str] = {}
    for path in regular_files:
        key = path.name.casefold()
        previous = casefold_names.get(key)
        if previous is not None and previous != path.name:
            errors.append(f"Portable Dateinamenskollision: {previous} / {path.name}")
        else:
            casefold_names[key] = path.name

    pdfs = [path for path in regular_files if path.suffix.casefold() == ".pdf"]
    non_pdfs = [path.name for path in regular_files if path.suffix.casefold() != ".pdf"]
    if non_pdfs:
        errors.append(f"Nicht-PDF-Dateien im Versandverzeichnis: {', '.join(non_pdfs)}")
    if not pdfs:
        errors.append("Keine PDF-Dateien im Versandverzeichnis")
    if len(regular_files) > MAX_FILES:
        errors.append(f"Dateizahl {len(regular_files)} überschreitet ERVB-Grenze {MAX_FILES}")

    main_pattern = re.compile(rf"^00_{re.escape(role)}_{NAME_BODY}\.pdf$")
    main_files = [path for path in pdfs if main_pattern.fullmatch(path.name)]
    if len(main_files) != 1:
        errors.append(
            f"Genau ein Hauptdokument nach Muster 00_{role}_Beschreibung.pdf erwartet; gefunden: {len(main_files)}"
        )
    if expected_docket and len(main_files) == 1:
        docket = normalized_token(expected_docket)
        if not docket:
            errors.append("Erwartetes Aktenzeichen enthält keine verwendbaren Zeichen")
        elif f"_{docket.casefold()}_" not in f"_{main_files[0].stem.casefold()}_":
            errors.append(f"Hauptdateiname enthält das erwartete Aktenzeichen nicht: {docket}")

    exhibits: list[tuple[int, str, int, Path]] = []
    for path in pdfs:
        name = path.name
        if len(name) > MAX_NAME_LENGTH:
            errors.append(f"{name}: {len(name)} Zeichen überschreiten die ERVB-Grenze {MAX_NAME_LENGTH}")
        elif len(name) > SOFT_NAME_LENGTH:
            warnings.append(f"{name}: {len(name)} Zeichen überschreiten den Hauszielwert {SOFT_NAME_LENGTH}")
        if not ASCII_PDF_NAME.fullmatch(name):
            errors.append(f"{name}: verletzt den ASCII-/Unterstrich-Hausstandard")
        match = EXHIBIT_NAME.fullmatch(name)
        if match:
            prefix = match.group("prefix")
            if prefix != exhibit_prefix:
                errors.append(f"{name}: Anlagenpräfix {prefix} statt {exhibit_prefix}")
            exhibits.append(
                (
                    int(match.group("order")),
                    match.group("order"),
                    int(match.group("number")),
                    path,
                )
            )
        elif path not in main_files:
            errors.append(
                f"{name}: weder Hauptdokument noch Anlage nach Muster 01_Anlage_{exhibit_prefix}{start}_Beschreibung.pdf"
            )
        files_payload.append(
            {
                "name": name,
                "bytes": path.lstat().st_size,
                "sha256": None,
                "kind": "hauptdokument" if path in main_files else "anlage",
            }
        )

    for path in regular_files:
        if path not in pdfs:
            files_payload.append(
                {"name": path.name, "bytes": path.lstat().st_size, "sha256": None, "kind": "sonstige"}
            )

    exhibits.sort(key=lambda item: item[0])
    orders = [item[0] for item in exhibits]
    order_tokens = [item[1] for item in exhibits]
    numbers = [item[2] for item in exhibits]
    if orders and orders != list(range(1, len(orders) + 1)):
        errors.append(f"Dateireihenfolge nicht lückenlos ab 01: {orders}")
    if order_tokens:
        width = max(2, len(str(len(order_tokens))))
        expected_tokens = [f"{index:0{width}d}" for index in range(1, len(order_tokens) + 1)]
        if order_tokens != expected_tokens:
            errors.append(
                f"Sortiernummern müssen einheitlich {width}-stellig sein: {order_tokens}"
            )
    if numbers and numbers != list(range(start, start + len(numbers))):
        errors.append(f"Anlagennummern nicht lückenlos ab {start}: {numbers}")
    if len(numbers) != len(set(numbers)):
        errors.append("Doppelte Anlagennummer")

    total_bytes = sum(item["bytes"] for item in files_payload)
    manifest_exhibits = {
        item["versand_name"]: item for item in manifest.get("exhibits", [])
    } if manifest else {}
    if total_bytes <= MAX_BYTES:
        payload_by_name = {item["name"]: item for item in files_payload}
        for path in regular_files:
            try:
                content, digest = read_stable(path, max_bytes=MAX_PDF_BYTES)
            except (OSError, ContractError) as exc:
                errors.append(f"{path.name}: stabile Dateiprüfung fehlgeschlagen: {exc}")
                continue
            payload_by_name[path.name]["sha256"] = digest
            payload_by_name[path.name]["bytes"] = len(content)
            if path.suffix.casefold() == ".pdf":
                pdf_errors, pdf_warnings = inspect_pdf(path.name, content)
                errors.extend(pdf_errors)
                warnings.extend(pdf_warnings)
                exhibit = manifest_exhibits.get(path.name)
                expected_label = exhibit["label"] if exhibit else None
                require_label = bool(exhibit and exhibit["stamp_mode"] != "already_stamped")
                deep_errors, deep_warnings, _, page_count = inspect_pdf_deep(
                    path.name, content, expected_label, require_label
                )
                errors.extend(deep_errors)
                warnings.extend(deep_warnings)
                if page_count is not None:
                    page_counts[path.name] = page_count

    total_bytes = sum(item["bytes"] for item in files_payload)
    if total_bytes > MAX_BYTES:
        errors.append(f"Gesamtgröße {total_bytes} Bytes überschreitet 200-MB-Grenze")
    elif total_bytes > SOFT_BYTES:
        warnings.append("Gesamtgröße überschreitet 190 MB; Übertragungsreserve prüfen")

    if manifest is not None:
        try:
            _validate_manifest_relations(
                manifest,
                files_payload,
                role,
                exhibit_prefix,
                start,
                expected_docket,
                page_counts,
                errors,
            )
        except (KeyError, TypeError, ContractError) as exc:
            errors.append(f"Paketmanifest-Beziehungen ungültig: {exc}")
        try:
            _validate_original_trace(package_root, send_dir, manifest, errors)
        except (KeyError, TypeError, ContractError) as exc:
            errors.append(f"Originalspur-/Manifest-Beziehung ungültig: {exc}")

    if approval_location.exists() or approval_location.is_symlink():
        approval["provided"] = True
        if approval_location.is_symlink() or not approval_location.is_file():
            errors.append(f"Freigabe ist kein sicherer regulärer JSON-Vertrag: {approval_location}")
        elif manifest is None:
            errors.append("Freigabe kann ohne gültiges Paketmanifest nicht geprüft werden")
        else:
            try:
                approval = validate_approval(load_json(approval_location), manifest["package_fingerprint"])
                if manifest["matter"]["signature_route"] == "noch_festzulegen":
                    raise ContractError("Signatur-/Versandweg ist noch nicht festgelegt")
                manifest_time = datetime.fromisoformat(manifest["created_at"].replace("Z", "+00:00"))
                approval_time = datetime.fromisoformat(approval["approved_at"].replace("Z", "+00:00"))
                if approval_time < manifest_time:
                    raise ContractError("Freigabezeitpunkt liegt vor der Paketproduktion")
                if approval_time.astimezone(timezone.utc) > datetime.now(timezone.utc) + MAX_CLOCK_SKEW:
                    raise ContractError("Freigabezeitpunkt liegt unplausibel in der Zukunft")
            except ContractError as exc:
                errors.append(f"Freigabe ungültig: {exc}")
                approval["valid"] = False

    technical_status = "BESTANDEN" if not errors and not warnings else "NICHT_BESTANDEN"
    if errors or warnings:
        status = "NICHT_VERSANDFERTIG"
    elif approval["valid"]:
        status = "VERSANDFERTIG"
    else:
        status = "FREIGABE_AUSSTEHEND"

    manual_checks = [
        "Im beA richtigen Empfänger, Nachrichtart und Aktenzeichen/Neueingang prüfen.",
        "Freigegebene Dateiliste und Signaturstatus unmittelbar vor dem Versand erneut abgleichen.",
        "Nach Versand automatisierte gerichtliche Eingangsbestätigung mit sämtlichen Dateinamen sichern.",
    ]
    return {
        "schema_version": REPORT_SCHEMA_VERSION,
        "package": str(send_dir),
        "status": status,
        "technical_status": technical_status,
        "inspection_level": inspection_level,
        "manifest": {
            "path": str(manifest_location),
            "valid": manifest is not None
            and order is not None
            and not any(
                item.startswith(("Paketmanifest", "Paketauftrag", "Normalisierter Paketauftrag"))
                for item in errors
            ),
            "package_fingerprint": manifest.get("package_fingerprint") if manifest else None,
            "order_path": str(order_location),
            "order_sha256": manifest.get("order_sha256") if manifest else None,
        },
        "approval": approval,
        "profile": {
            "role": role,
            "anlagen_prefix": exhibit_prefix,
            "start": start,
            "expected_az": expected_docket,
            "filename_policy": "ASCII, Unterstrich/Minus, Ziel <=80, absolut <=90 Zeichen",
        },
        "totals": {"files": len(files_payload), "bytes": total_bytes},
        "files": files_payload,
        "errors": errors,
        "warnings": warnings,
        "manual_checks": manual_checks,
    }


def format_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# beA-Paketprüfung: {report['status']}",
        "",
        f"- Versandverzeichnis: `{markdown_text(report['package'])}`",
        f"- Technik: `{report['technical_status']}` ({report['inspection_level']})",
        f"- Dateien: {report['totals']['files']}",
        f"- Gesamtgröße: {report['totals']['bytes']} Bytes",
        f"- Paket-Fingerprint: `{report['manifest']['package_fingerprint']}`",
        f"- Anwaltliche Freigabe: `{'GÜLTIG' if report['approval']['valid'] else 'AUSSTEHEND/UNGÜLTIG'}`",
        "",
    ]
    if report["errors"]:
        lines.append("## Fehler")
        lines.extend(f"- {markdown_text(item)}" for item in report["errors"])
        lines.append("")
    if report["warnings"]:
        lines.append("## Warnungen")
        lines.extend(f"- {markdown_text(item)}" for item in report["warnings"])
        lines.append("")
    lines.append("## Dateien")
    lines.append("")
    lines.append("| Datei | Art | Bytes | SHA-256 |")
    lines.append("| --- | --- | ---: | --- |")
    for item in report["files"]:
        lines.append(
            f"| `{markdown_text(item['name'])}` | {markdown_text(item['kind'])} | "
            f"{item['bytes']} | `{item['sha256']}` |"
        )
    lines.extend(["", "## Verbleibende beA-Handkontrollen"])
    lines.extend(f"- [ ] {markdown_text(item)}" for item in report["manual_checks"])
    return "\n".join(lines)


def _minimal_pdf() -> bytes:
    if PdfWriter is not None:
        writer = PdfWriter()
        writer.add_blank_page(width=595, height=842)
        stream = io.BytesIO()
        writer.write(stream)
        return stream.getvalue()
    return (
        b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
        b"2 0 obj<</Type/Pages/Count 0/Kids[]>>endobj\n"
        b"trailer<</Root 1 0 R>>\n%%EOF\n"
    )


def _write_selftest_contract(
    root: Path,
    send: Path,
    *,
    approved: bool = True,
    role: str = "K",
    prefix: str = "K",
    start: int = 12,
    docket: str = "16 O 123/24",
    document_type: str = "Replik",
) -> tuple[Path, Path]:
    control = root / "kontrolle"
    control.mkdir(exist_ok=True)
    original = root / "original"
    original.mkdir(exist_ok=True)
    main_candidates = sorted(send.glob(f"00_{role}_*.pdf"))
    if len(main_candidates) != 1:
        raise AssertionError("Selbsttestvertrag benötigt genau ein Hauptdokument")
    main = main_candidates[0]
    exhibit_paths = sorted(path for path in send.glob("*_Anlage_*.pdf") if path.is_file())
    main_hash = hashlib.sha256(main.read_bytes()).hexdigest()
    (original / "00_Hauptdokument_Original.pdf").write_bytes(main.read_bytes())
    files = [
        {
            "name": main.name,
            "kind": "hauptdokument",
            "label": None,
            "bytes": main.stat().st_size,
            "sha256": main_hash,
        }
    ]
    exhibits = []
    for index, path in enumerate(exhibit_paths, start=1):
        match = EXHIBIT_NAME.fullmatch(path.name)
        if match is None:
            continue
        number = int(match.group("number"))
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        label = f"Anlage {prefix}{number}"
        original_name = f"{index:02d}_Anlage_{prefix}{number}_Original.pdf"
        (original / original_name).write_bytes(path.read_bytes())
        files.append(
            {"name": path.name, "kind": "anlage", "label": label, "bytes": path.stat().st_size, "sha256": digest}
        )
        exhibits.append(
            {
                "order": index,
                "number": number,
                "label": label,
                "title": "Kaufvertrag" if index == 1 else "KBA Rueckruf",
                "document_date": None,
                "reference": f"Schriftsatz Rn. {index}",
                "source_name": path.name,
                "original_name": original_name,
                "versand_name": path.name,
                "input_sha256": digest,
                "versand_sha256": digest,
                "bytes": path.stat().st_size,
                "input_pages": 1,
                "output_pages": 1,
                "stamp_mode": "already_stamped",
                "visual_qa_required": True,
            }
        )
    matter = {
        "court": "Landgericht Stuttgart",
        "docket": docket,
        "new_filing": False,
        "role": role,
        "document_type": document_type,
        "document_date": "2026-07-10",
        "deadline": "2026-07-15",
        "responsible_person": "Rechtsanwältin Test",
        "signature_route": "einfach_signiert_persoenliches_beA",
        "exhibit_prefix": prefix,
        "first_exhibit_number": start,
    }
    order = {
        "schema_version": "1.0.0",
        "matter": matter,
        "main_document": {"source": main.name, "approved_sha256": main_hash},
        "exhibits": [
            {
                "number": item["number"],
                "source": item["source_name"],
                "expected_sha256": item["input_sha256"],
                "title": item["title"],
                "document_date": item["document_date"],
                "reference": item["reference"],
                "stamp_mode": item["stamp_mode"],
            }
            for item in exhibits
        ],
    }
    order = validate_order(order)
    (control / "paketauftrag-normalisiert.json").write_text(
        json.dumps(order, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    manifest = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "created_at": "2026-07-14T12:00:00+02:00",
        "order_sha256": digest_json(order),
        "matter": matter,
        "main_document": {
            "source_name": main.name,
            "original_name": "00_Hauptdokument_Original.pdf",
            "versand_name": main.name,
            "input_sha256": main_hash,
            "versand_sha256": main_hash,
            "bytes": main.stat().st_size,
        },
        "exhibits": exhibits,
        "files": files,
        "package_fingerprint": "0" * 64,
    }
    manifest["package_fingerprint"] = package_fingerprint(manifest)
    manifest_path = control / "paket-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    approval_path = control / "freigabe.json"
    if approved:
        approval = {
            "schema_version": APPROVAL_SCHEMA_VERSION,
            "package_fingerprint": manifest["package_fingerprint"],
            "approved_by": "Rechtsanwältin Test",
            "approved_at": "2026-07-14T12:30:00+02:00",
            "confirmations": {key: True for key in APPROVAL_CONFIRMATIONS},
        }
        approval_path.write_text(json.dumps(approval, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest_path, approval_path


def selftest() -> None:
    with tempfile.TemporaryDirectory(prefix="bea-paket-test-") as raw:
        root = Path(raw)
        send = root / "versand"
        send.mkdir()
        (send / "00_K_2026-07-10_Replik_16_O_123_24.pdf").write_bytes(_minimal_pdf())
        (send / "01_Anlage_K12_Kaufvertrag.pdf").write_bytes(_minimal_pdf())
        (send / "02_Anlage_K13_KBA_Rueckruf.pdf").write_bytes(_minimal_pdf())
        _, approval_path = _write_selftest_contract(root, send, start=12)
        valid = validate_package(root, "K", "K", 12, "16 O 123/24")
        expected_valid = "VERSANDFERTIG" if PdfReader is not None else "NICHT_VERSANDFERTIG"
        assert valid["status"] == expected_valid, valid
        if PdfReader is None:
            assert any("pypdf fehlt" in item for item in valid["warnings"])
        approval_path.unlink()
        pending = validate_package(root, "K", "K", 12, "16 O 123/24")
        expected_pending = "FREIGABE_AUSSTEHEND" if PdfReader is not None else "NICHT_VERSANDFERTIG"
        assert pending["status"] == expected_pending, pending
        _write_selftest_contract(root, send, start=12)
        (send / "03 Anlage K14 falsch.pdf").write_bytes(_minimal_pdf())
        invalid = validate_package(root, "K", "K", 12, "16 O 123/24")
        assert invalid["status"] == "NICHT_VERSANDFERTIG"
        assert invalid["errors"]
        (send / "03 Anlage K14 falsch.pdf").unlink()
        approval = load_json(root / "kontrolle" / "freigabe.json")
        approval["package_fingerprint"] = "f" * 64
        (root / "kontrolle" / "freigabe.json").write_text(
            json.dumps(approval, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        invalid_approval = validate_package(root, "K", "K", 12, "16 O 123/24")
        assert invalid_approval["status"] == "NICHT_VERSANDFERTIG"
        assert any("Freigabe ungültig" in item for item in invalid_approval["errors"])
    print("bea-paket-pruefer selftest OK (Manifest, Hashbindung, Freigabegate)")


def main() -> int:
    parser = make_parser()
    args = parser.parse_args()
    if args.selftest:
        selftest()
        return 0
    report = validate_package(
        args.package,
        args.role,
        args.anlagen_prefix,
        args.start,
        args.expected_az,
        args.manifest,
        args.approval,
    )
    rendered_json = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        try:
            write_report(args.report, rendered_json, Path(report["package"]))
        except (OSError, ValueError) as exc:
            print(f"FEHLER: Prüfbericht konnte nicht sicher geschrieben werden: {exc}", file=sys.stderr)
            return 1
    if args.format == "json":
        print(rendered_json, end="")
    else:
        print(format_markdown(report))
    if report["status"] == "VERSANDFERTIG":
        return 0
    if report["status"] == "FREIGABE_AUSSTEHEND":
        return 2
    return 1


if __name__ == "__main__":
    sys.exit(main())

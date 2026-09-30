#!/usr/bin/env python3
"""Shared contracts for deterministic beA package production and validation."""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import stat
import unicodedata
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable


ORDER_SCHEMA_VERSION = "1.0.0"
MANIFEST_SCHEMA_VERSION = "1.1.0"
APPROVAL_SCHEMA_VERSION = "1.0.0"
REPORT_SCHEMA_VERSION = "2.0.0"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_PDF_BYTES = 200 * 1024 * 1024
MAX_PDF_PAGES = 5_000
MAX_PDF_DIMENSION_POINTS = 14_400.0
MAX_EXHIBIT_NUMBER = 999_999
HASH_RE = re.compile(r"^[a-f0-9]{64}$")
CODE_RE = re.compile(r"^[A-Za-z]{1,6}$")
EXHIBIT_LABEL_RE = re.compile(r"^Anlage [A-Z]{1,6}[1-9][0-9]{0,5}$")
CONTROL_RE = re.compile(r"[\x00-\x1f\x7f]")
ISO_DATETIME_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|[+-]\d{2}:\d{2})$"
)
SIGNATURE_ROUTES = {
    "qeS",
    "einfach_signiert_persoenliches_beA",
    "noch_festzulegen",
}
STAMP_MODES = {"first", "all", "cover", "already_stamped"}
STAMP_RENDER_MODES = {"first", "all", "cover"}
APPROVAL_CONFIRMATIONS = (
    "hauptdokument_ist_freigegebene_endfassung",
    "rubrum_antraege_tatsachen_recht_geprueft",
    "anlagenbezugnahmen_vollstaendig_und_eindeutig",
    "stempel_dateinamen_verzeichnis_deckungsgleich",
    "pdfs_visuell_auf_vollstaendigkeit_lesbarkeit_geprueft",
    "frist_empfaenger_aktenzeichen_signaturweg_geprueft",
)


class ContractError(ValueError):
    """Raised when a beA input or approval contract is invalid."""


def _reject_constant(value: str) -> None:
    raise ContractError(f"nicht endliche JSON-Zahl ist unzulässig: {value}")


def _object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ContractError(f"doppelter JSON-Schlüssel: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, Any]:
    requested = path.expanduser().absolute()
    try:
        content, _ = read_stable(requested, max_bytes=MAX_JSON_BYTES)
        raw = content.decode("utf-8")
        value = json.loads(
            raw,
            object_pairs_hook=_object_pairs,
            parse_constant=_reject_constant,
        )
    except ContractError:
        raise
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        raise ContractError(f"JSON-Vertrag kann nicht gelesen werden ({requested}): {exc}") from exc
    if not isinstance(value, dict):
        raise ContractError(f"JSON-Vertrag muss ein Objekt sein: {requested}")
    return value


def canonical_json(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def digest_json(value: object) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def ensure_exact_keys(value: dict[str, Any], expected: Iterable[str], location: str) -> None:
    expected_set = set(expected)
    actual = set(value)
    missing = sorted(expected_set - actual)
    unknown = sorted(actual - expected_set)
    problems: list[str] = []
    if missing:
        problems.append(f"fehlt: {', '.join(missing)}")
    if unknown:
        problems.append(f"unbekannt: {', '.join(unknown)}")
    if problems:
        raise ContractError(f"{location}: {'; '.join(problems)}")


def ensure_text(value: Any, location: str, *, max_length: int = 240) -> str:
    if not isinstance(value, str):
        raise ContractError(f"{location}: Text erwartet")
    cleaned = value.strip()
    if not cleaned:
        raise ContractError(f"{location}: leerer Text ist unzulässig")
    if cleaned != value:
        raise ContractError(f"{location}: führende oder nachgestellte Leerzeichen sind unzulässig")
    if len(cleaned) > max_length:
        raise ContractError(f"{location}: mehr als {max_length} Zeichen")
    if CONTROL_RE.search(cleaned) or any(
        unicodedata.category(character).startswith("C")
        or unicodedata.category(character) in {"Zl", "Zp"}
        for character in cleaned
    ):
        raise ContractError(f"{location}: Steuer-/Formatzeichen sind unzulässig")
    return cleaned


def ensure_nullable_text(value: Any, location: str, *, max_length: int = 240) -> str | None:
    if value is None:
        return None
    return ensure_text(value, location, max_length=max_length)


def ensure_hash(value: Any, location: str) -> str:
    if not isinstance(value, str) or HASH_RE.fullmatch(value) is None:
        raise ContractError(f"{location}: SHA-256 in 64 Kleinbuchstaben-Hexzeichen erwartet")
    return value


def ensure_code(value: Any, location: str) -> str:
    text = ensure_text(value, location, max_length=6).upper()
    if CODE_RE.fullmatch(text) is None:
        raise ContractError(f"{location}: 1 bis 6 ASCII-Buchstaben erwartet")
    return text


def ensure_iso_date(value: Any, location: str, *, nullable: bool = False) -> str | None:
    if value is None and nullable:
        return None
    text = ensure_text(value, location, max_length=10)
    try:
        parsed = date.fromisoformat(text)
    except ValueError as exc:
        raise ContractError(f"{location}: echtes ISO-Datum YYYY-MM-DD erwartet") from exc
    if parsed.isoformat() != text:
        raise ContractError(f"{location}: kanonisches ISO-Datum YYYY-MM-DD erwartet")
    return text


def ensure_iso_datetime(value: Any, location: str) -> str:
    text = ensure_text(value, location, max_length=40)
    if ISO_DATETIME_RE.fullmatch(text) is None:
        raise ContractError(f"{location}: ISO-Zeitpunkt YYYY-MM-DDTHH:MM:SS mit Zeitzone erwartet")
    candidate = text[:-1] + "+00:00" if text.endswith("Z") else text
    try:
        parsed = datetime.fromisoformat(candidate)
    except ValueError as exc:
        raise ContractError(f"{location}: ISO-Zeitpunkt mit Zeitzone erwartet") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ContractError(f"{location}: Zeitzone fehlt")
    return text


def ensure_int(
    value: Any,
    location: str,
    *,
    minimum: int = 0,
    maximum: int | None = None,
) -> int:
    invalid = (
        not isinstance(value, int)
        or isinstance(value, bool)
        or value < minimum
        or (maximum is not None and value > maximum)
    )
    if invalid:
        if maximum is None:
            expected = f"ab {minimum}"
        else:
            expected = f"zwischen {minimum} und {maximum}"
        raise ContractError(f"{location}: ganze Zahl {expected} erwartet")
    return value


def ensure_bool(value: Any, location: str) -> bool:
    if not isinstance(value, bool):
        raise ContractError(f"{location}: boolescher Wert erwartet")
    return value


def normalized_token(value: str) -> str:
    value = value.replace("Ä", "Ae").replace("Ö", "Oe").replace("Ü", "Ue")
    value = value.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(character for character in value if not unicodedata.combining(character))
    value = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return re.sub(r"_+", "_", value)


def _filename_token(value: str, location: str) -> str:
    token = normalized_token(value)
    if not token:
        raise ContractError(f"{location}: ergibt keinen verwendbaren ASCII-Dateinamen")
    return token


def main_filename(matter: dict[str, Any]) -> str:
    docket = "Neueingang" if matter["new_filing"] else _filename_token(matter["docket"], "matter.docket")
    document_type = _filename_token(matter["document_type"], "matter.document_type")
    name = f"00_{matter['role']}_{matter['document_date']}_{document_type}_{docket}.pdf"
    validate_output_name(name, "Hauptdokument")
    return name


def exhibit_filename(order_index: int, total: int, exhibit: dict[str, Any], prefix: str) -> str:
    width = max(2, len(str(max(total, 1))))
    order = f"{order_index:0{width}d}"
    title = _filename_token(exhibit["title"], f"exhibits[{order_index - 1}].title")
    suffix = f"_{exhibit['document_date']}" if exhibit["document_date"] else ""
    name = f"{order}_Anlage_{prefix}{exhibit['number']}_{title}{suffix}.pdf"
    validate_output_name(name, f"Anlage {prefix}{exhibit['number']}")
    return name


def validate_output_name(name: str, location: str) -> None:
    if re.fullmatch(r"[A-Za-z0-9_-]+\.pdf", name) is None:
        raise ContractError(f"{location}: unsicherer PDF-Dateiname: {name}")
    if len(name) > 90:
        raise ContractError(f"{location}: Dateiname überschreitet 90 Zeichen: {name}")
    if len(name) > 80:
        raise ContractError(f"{location}: Dateiname überschreitet den Hauszielwert 80 Zeichen: {name}")


def validate_order(value: dict[str, Any]) -> dict[str, Any]:
    ensure_exact_keys(value, ("schema_version", "matter", "main_document", "exhibits"), "Paketauftrag")
    if value["schema_version"] != ORDER_SCHEMA_VERSION:
        raise ContractError(f"Paketauftrag.schema_version: {ORDER_SCHEMA_VERSION} erwartet")

    matter_raw = value["matter"]
    if not isinstance(matter_raw, dict):
        raise ContractError("matter: Objekt erwartet")
    matter_keys = (
        "court",
        "docket",
        "new_filing",
        "role",
        "document_type",
        "document_date",
        "deadline",
        "responsible_person",
        "signature_route",
        "exhibit_prefix",
        "first_exhibit_number",
    )
    ensure_exact_keys(matter_raw, matter_keys, "matter")
    matter = {
        "court": ensure_text(matter_raw["court"], "matter.court", max_length=160),
        "docket": ensure_nullable_text(matter_raw["docket"], "matter.docket", max_length=80),
        "new_filing": ensure_bool(matter_raw["new_filing"], "matter.new_filing"),
        "role": ensure_code(matter_raw["role"], "matter.role"),
        "document_type": ensure_text(matter_raw["document_type"], "matter.document_type", max_length=48),
        "document_date": ensure_iso_date(matter_raw["document_date"], "matter.document_date"),
        "deadline": ensure_iso_date(matter_raw["deadline"], "matter.deadline", nullable=True),
        "responsible_person": ensure_text(
            matter_raw["responsible_person"], "matter.responsible_person", max_length=160
        ),
        "signature_route": ensure_text(matter_raw["signature_route"], "matter.signature_route", max_length=48),
        "exhibit_prefix": ensure_code(matter_raw["exhibit_prefix"], "matter.exhibit_prefix"),
        "first_exhibit_number": ensure_int(
            matter_raw["first_exhibit_number"],
            "matter.first_exhibit_number",
            minimum=1,
            maximum=MAX_EXHIBIT_NUMBER,
        ),
    }
    if matter["signature_route"] not in SIGNATURE_ROUTES:
        raise ContractError(
            "matter.signature_route: qeS, einfach_signiert_persoenliches_beA oder noch_festzulegen erwartet"
        )
    if matter["new_filing"] and matter["docket"] is not None:
        raise ContractError("matter: bei Neueingang muss docket null sein")
    if not matter["new_filing"] and matter["docket"] is None:
        raise ContractError("matter: bei bestehendem Verfahren ist docket erforderlich")

    main_raw = value["main_document"]
    if not isinstance(main_raw, dict):
        raise ContractError("main_document: Objekt erwartet")
    ensure_exact_keys(main_raw, ("source", "approved_sha256"), "main_document")
    main = {
        "source": ensure_text(main_raw["source"], "main_document.source", max_length=1024),
        "approved_sha256": ensure_hash(main_raw["approved_sha256"], "main_document.approved_sha256"),
    }

    exhibits_raw = value["exhibits"]
    if not isinstance(exhibits_raw, list):
        raise ContractError("exhibits: Array erwartet")
    if len(exhibits_raw) > 999:
        raise ContractError("exhibits: höchstens 999 Anlagen pro Paketauftrag")
    exhibits: list[dict[str, Any]] = []
    exhibit_keys = (
        "number",
        "source",
        "expected_sha256",
        "title",
        "document_date",
        "reference",
        "stamp_mode",
    )
    for index, item in enumerate(exhibits_raw):
        location = f"exhibits[{index}]"
        if not isinstance(item, dict):
            raise ContractError(f"{location}: Objekt erwartet")
        ensure_exact_keys(item, exhibit_keys, location)
        stamp_mode = ensure_text(item["stamp_mode"], f"{location}.stamp_mode", max_length=24)
        if stamp_mode not in STAMP_MODES:
            raise ContractError(f"{location}.stamp_mode: {', '.join(sorted(STAMP_MODES))} erwartet")
        exhibits.append(
            {
                "number": ensure_int(
                    item["number"],
                    f"{location}.number",
                    minimum=1,
                    maximum=MAX_EXHIBIT_NUMBER,
                ),
                "source": ensure_text(item["source"], f"{location}.source", max_length=1024),
                "expected_sha256": ensure_hash(item["expected_sha256"], f"{location}.expected_sha256"),
                "title": ensure_text(item["title"], f"{location}.title", max_length=100),
                "document_date": ensure_iso_date(
                    item["document_date"], f"{location}.document_date", nullable=True
                ),
                "reference": ensure_text(item["reference"], f"{location}.reference", max_length=240),
                "stamp_mode": stamp_mode,
            }
        )
    expected_numbers = list(
        range(matter["first_exhibit_number"], matter["first_exhibit_number"] + len(exhibits))
    )
    actual_numbers = [item["number"] for item in exhibits]
    if actual_numbers != expected_numbers:
        raise ContractError(
            f"exhibits.number: lückenlose Folge ab {matter['first_exhibit_number']} erwartet; erhalten {actual_numbers}"
        )
    source_values = [main["source"], *(item["source"] for item in exhibits)]
    if len(source_values) != len(set(source_values)):
        raise ContractError("Paketauftrag: dieselbe Quellpfadangabe darf nur einmal vorkommen")

    normalized = {
        "schema_version": ORDER_SCHEMA_VERSION,
        "matter": matter,
        "main_document": main,
        "exhibits": exhibits,
    }
    main_filename(matter)
    for index, exhibit in enumerate(exhibits, start=1):
        exhibit_filename(index, len(exhibits), exhibit, matter["exhibit_prefix"])
    return normalized


def validate_manifest(value: dict[str, Any]) -> dict[str, Any]:
    keys = (
        "schema_version",
        "created_at",
        "order_sha256",
        "matter",
        "main_document",
        "exhibits",
        "files",
        "package_fingerprint",
    )
    ensure_exact_keys(value, keys, "Paketmanifest")
    if value["schema_version"] != MANIFEST_SCHEMA_VERSION:
        raise ContractError(f"Paketmanifest.schema_version: {MANIFEST_SCHEMA_VERSION} erwartet")
    ensure_iso_datetime(value["created_at"], "Paketmanifest.created_at")
    ensure_hash(value["order_sha256"], "Paketmanifest.order_sha256")
    ensure_hash(value["package_fingerprint"], "Paketmanifest.package_fingerprint")
    matter = value["matter"]
    if not isinstance(matter, dict):
        raise ContractError("Paketmanifest.matter: Objekt erwartet")
    matter_keys = (
        "court",
        "docket",
        "new_filing",
        "role",
        "document_type",
        "document_date",
        "deadline",
        "responsible_person",
        "signature_route",
        "exhibit_prefix",
        "first_exhibit_number",
    )
    ensure_exact_keys(matter, matter_keys, "Paketmanifest.matter")
    ensure_text(matter["court"], "Paketmanifest.matter.court", max_length=160)
    ensure_nullable_text(matter["docket"], "Paketmanifest.matter.docket", max_length=80)
    ensure_bool(matter["new_filing"], "Paketmanifest.matter.new_filing")
    if ensure_code(matter["role"], "Paketmanifest.matter.role") != matter["role"]:
        raise ContractError("Paketmanifest.matter.role: kanonische Großschreibung erwartet")
    ensure_text(matter["document_type"], "Paketmanifest.matter.document_type", max_length=48)
    ensure_iso_date(matter["document_date"], "Paketmanifest.matter.document_date")
    ensure_iso_date(matter["deadline"], "Paketmanifest.matter.deadline", nullable=True)
    ensure_text(matter["responsible_person"], "Paketmanifest.matter.responsible_person", max_length=160)
    signature_route = ensure_text(
        matter["signature_route"], "Paketmanifest.matter.signature_route", max_length=48
    )
    if signature_route not in SIGNATURE_ROUTES:
        raise ContractError("Paketmanifest.matter.signature_route: unerwarteter Wert")
    if (
        ensure_code(matter["exhibit_prefix"], "Paketmanifest.matter.exhibit_prefix")
        != matter["exhibit_prefix"]
    ):
        raise ContractError("Paketmanifest.matter.exhibit_prefix: kanonische Großschreibung erwartet")
    ensure_int(
        matter["first_exhibit_number"],
        "Paketmanifest.matter.first_exhibit_number",
        minimum=1,
        maximum=MAX_EXHIBIT_NUMBER,
    )
    if matter["new_filing"] != (matter["docket"] is None):
        raise ContractError("Paketmanifest.matter: docket/Neueingang widersprüchlich")

    main = value["main_document"]
    if not isinstance(main, dict):
        raise ContractError("Paketmanifest.main_document: Objekt erwartet")
    main_keys = (
        "source_name",
        "original_name",
        "versand_name",
        "input_sha256",
        "versand_sha256",
        "bytes",
    )
    ensure_exact_keys(main, main_keys, "Paketmanifest.main_document")
    for key in ("source_name", "original_name", "versand_name"):
        ensure_text(main[key], f"Paketmanifest.main_document.{key}", max_length=255)
    if Path(main["source_name"]).name != main["source_name"] or any(
        separator in main["source_name"] for separator in ("/", "\\")
    ):
        raise ContractError("Paketmanifest.main_document.source_name: reiner Basisname erwartet")
    if main["original_name"] != "00_Hauptdokument_Original.pdf":
        raise ContractError("Paketmanifest.main_document.original_name: kanonischer Originalname erwartet")
    expected_main_name = main_filename(matter)
    if main["versand_name"] != expected_main_name:
        raise ContractError("Paketmanifest.main_document.versand_name: weicht von den Vorgangsdaten ab")
    ensure_hash(main["input_sha256"], "Paketmanifest.main_document.input_sha256")
    ensure_hash(main["versand_sha256"], "Paketmanifest.main_document.versand_sha256")
    if main["input_sha256"] != main["versand_sha256"]:
        raise ContractError("Paketmanifest.main_document: freigegebene Endfassung wurde verändert")
    ensure_int(main["bytes"], "Paketmanifest.main_document.bytes", minimum=1)

    exhibits = value["exhibits"]
    files = value["files"]
    if not isinstance(exhibits, list) or not isinstance(files, list):
        raise ContractError("Paketmanifest.exhibits/files: Arrays erwartet")
    if len(exhibits) > 999:
        raise ContractError("Paketmanifest.exhibits: höchstens 999 Anlagen")
    if not 1 <= len(files) <= 1000:
        raise ContractError("Paketmanifest.files: 1 bis 1000 Versanddateien erwartet")
    exhibit_keys = (
        "order",
        "number",
        "label",
        "title",
        "document_date",
        "reference",
        "source_name",
        "original_name",
        "versand_name",
        "input_sha256",
        "versand_sha256",
        "bytes",
        "input_pages",
        "output_pages",
        "stamp_mode",
        "visual_qa_required",
    )
    for index, exhibit in enumerate(exhibits):
        location = f"Paketmanifest.exhibits[{index}]"
        if not isinstance(exhibit, dict):
            raise ContractError(f"{location}: Objekt erwartet")
        ensure_exact_keys(exhibit, exhibit_keys, location)
        ensure_int(exhibit["order"], f"{location}.order", minimum=1)
        ensure_int(
            exhibit["number"],
            f"{location}.number",
            minimum=1,
            maximum=MAX_EXHIBIT_NUMBER,
        )
        ensure_text(exhibit["label"], f"{location}.label", max_length=32)
        ensure_text(exhibit["title"], f"{location}.title", max_length=100)
        ensure_iso_date(exhibit["document_date"], f"{location}.document_date", nullable=True)
        ensure_text(exhibit["reference"], f"{location}.reference", max_length=240)
        for key in ("source_name", "original_name", "versand_name"):
            ensure_text(exhibit[key], f"{location}.{key}", max_length=255)
        if Path(exhibit["source_name"]).name != exhibit["source_name"] or any(
            separator in exhibit["source_name"] for separator in ("/", "\\")
        ):
            raise ContractError(f"{location}.source_name: reiner Basisname erwartet")
        ensure_hash(exhibit["input_sha256"], f"{location}.input_sha256")
        ensure_hash(exhibit["versand_sha256"], f"{location}.versand_sha256")
        ensure_int(exhibit["bytes"], f"{location}.bytes", minimum=1)
        ensure_int(exhibit["input_pages"], f"{location}.input_pages", minimum=1)
        ensure_int(exhibit["output_pages"], f"{location}.output_pages", minimum=1)
        stamp_mode = ensure_text(exhibit["stamp_mode"], f"{location}.stamp_mode", max_length=24)
        if stamp_mode not in STAMP_MODES:
            raise ContractError(f"{location}.stamp_mode: unerwarteter Wert")
        if ensure_bool(exhibit["visual_qa_required"], f"{location}.visual_qa_required") is not True:
            raise ContractError(f"{location}.visual_qa_required: true erwartet")
        expected_output_pages = exhibit["input_pages"] + (
            1 if exhibit["stamp_mode"] == "cover" else 0
        )
        if exhibit["output_pages"] != expected_output_pages:
            raise ContractError(
                f"{location}.output_pages: für {exhibit['stamp_mode']} "
                f"werden {expected_output_pages} Seiten erwartet"
            )
        if exhibit["stamp_mode"] == "already_stamped" and (
            exhibit["input_sha256"] != exhibit["versand_sha256"]
        ):
            raise ContractError(f"{location}: already_stamped darf den Dateiinhalt nicht verändern")

    expected_orders = list(range(1, len(exhibits) + 1))
    actual_orders = [item["order"] for item in exhibits]
    if actual_orders != expected_orders:
        raise ContractError(f"Paketmanifest.exhibits.order: lückenlose Folge erwartet; erhalten {actual_orders}")
    expected_numbers = list(
        range(matter["first_exhibit_number"], matter["first_exhibit_number"] + len(exhibits))
    )
    actual_numbers = [item["number"] for item in exhibits]
    if actual_numbers != expected_numbers:
        raise ContractError(
            f"Paketmanifest.exhibits.number: lückenlose Folge ab {matter['first_exhibit_number']} erwartet"
        )
    width = max(2, len(str(max(len(exhibits), 1))))
    for index, exhibit in enumerate(exhibits, start=1):
        location = f"Paketmanifest.exhibits[{index - 1}]"
        expected_label = f"Anlage {matter['exhibit_prefix']}{exhibit['number']}"
        if exhibit["label"] != expected_label:
            raise ContractError(f"{location}.label: {expected_label!r} erwartet")
        expected_original = (
            f"{index:0{width}d}_Anlage_{matter['exhibit_prefix']}{exhibit['number']}_Original.pdf"
        )
        if exhibit["original_name"] != expected_original:
            raise ContractError(f"{location}.original_name: kanonischer Originalname erwartet")
        expected_send = exhibit_filename(index, len(exhibits), exhibit, matter["exhibit_prefix"])
        if exhibit["versand_name"] != expected_send:
            raise ContractError(f"{location}.versand_name: weicht von den Anlagendaten ab")

    file_keys = ("name", "kind", "label", "bytes", "sha256")
    names: list[str] = []
    for index, item in enumerate(files):
        location = f"Paketmanifest.files[{index}]"
        if not isinstance(item, dict):
            raise ContractError(f"{location}: Objekt erwartet")
        ensure_exact_keys(item, file_keys, location)
        name = ensure_text(item["name"], f"{location}.name", max_length=90)
        validate_output_name(name, location)
        kind = ensure_text(item["kind"], f"{location}.kind", max_length=16)
        if kind not in {"hauptdokument", "anlage"}:
            raise ContractError(f"{location}.kind: unerwarteter Wert")
        ensure_nullable_text(item["label"], f"{location}.label", max_length=32)
        ensure_int(item["bytes"], f"{location}.bytes", minimum=1)
        ensure_hash(item["sha256"], f"{location}.sha256")
        names.append(name)
    if len(names) != len(set(names)) or len(names) != len({name.casefold() for name in names}):
        raise ContractError("Paketmanifest.files: doppelte oder portable kollidierende Dateinamen")
    expected_file_names = [main["versand_name"], *(item["versand_name"] for item in exhibits)]
    if names != expected_file_names:
        raise ContractError("Paketmanifest.files: Reihenfolge/Dateiliste weicht von Hauptdokument und Anlagen ab")
    expected_file_payloads = [
        {
            "name": main["versand_name"],
            "kind": "hauptdokument",
            "label": None,
            "bytes": main["bytes"],
            "sha256": main["versand_sha256"],
        },
        *(
            {
                "name": exhibit["versand_name"],
                "kind": "anlage",
                "label": exhibit["label"],
                "bytes": exhibit["bytes"],
                "sha256": exhibit["versand_sha256"],
            }
            for exhibit in exhibits
        ),
    ]
    if files != expected_file_payloads:
        raise ContractError("Paketmanifest.files: Inhalt widerspricht Hauptdokument oder Anlagen")
    return value


def fingerprint_payload(manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": manifest["schema_version"],
        "created_at": manifest["created_at"],
        "order_sha256": manifest["order_sha256"],
        "matter": manifest["matter"],
        "main_document": manifest["main_document"],
        "exhibits": manifest["exhibits"],
        "files": manifest["files"],
    }


def package_fingerprint(manifest: dict[str, Any]) -> str:
    return digest_json(fingerprint_payload(manifest))


def validate_approval(value: dict[str, Any], expected_fingerprint: str) -> dict[str, Any]:
    ensure_exact_keys(
        value,
        ("schema_version", "package_fingerprint", "approved_by", "approved_at", "confirmations"),
        "Freigabe",
    )
    if value["schema_version"] != APPROVAL_SCHEMA_VERSION:
        raise ContractError(f"Freigabe.schema_version: {APPROVAL_SCHEMA_VERSION} erwartet")
    fingerprint = ensure_hash(value["package_fingerprint"], "Freigabe.package_fingerprint")
    if fingerprint != expected_fingerprint:
        raise ContractError("Freigabe.package_fingerprint passt nicht zum aktuellen Versandpaket")
    approved_by = ensure_text(value["approved_by"], "Freigabe.approved_by", max_length=160)
    approved_at = ensure_iso_datetime(value["approved_at"], "Freigabe.approved_at")
    confirmations = value["confirmations"]
    if not isinstance(confirmations, dict):
        raise ContractError("Freigabe.confirmations: Objekt erwartet")
    ensure_exact_keys(confirmations, APPROVAL_CONFIRMATIONS, "Freigabe.confirmations")
    for key in APPROVAL_CONFIRMATIONS:
        if confirmations[key] is not True:
            raise ContractError(f"Freigabe.confirmations.{key}: ausdrückliche Bestätigung true erforderlich")
    return {
        "provided": True,
        "valid": True,
        "approved_by": approved_by,
        "approved_at": approved_at,
        "package_fingerprint": fingerprint,
    }


def _read_stable(
    path: Path,
    *,
    max_bytes: int | None,
    retain_content: bool,
) -> tuple[bytes, int, str]:
    requested = path.expanduser().absolute()
    if max_bytes is not None and (not isinstance(max_bytes, int) or max_bytes < 1):
        raise ContractError("max_bytes muss eine positive Ganzzahl sein")
    if requested.is_symlink():
        raise ContractError("symbolische Links sind als Quelldatei unzulässig")
    before = requested.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise ContractError("ist keine reguläre Datei")
    if max_bytes is not None and before.st_size > max_bytes:
        raise ContractError(f"überschreitet die Größengrenze {max_bytes} Bytes")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(requested, flags)
    try:
        opened = os.fstat(descriptor)
        if (opened.st_dev, opened.st_ino) != (before.st_dev, before.st_ino):
            raise ContractError("wurde vor dem Lesen ausgetauscht")
        chunks: list[bytes] = []
        digest = hashlib.sha256()
        size = 0
        with os.fdopen(descriptor, "rb", closefd=False) as handle:
            while True:
                read_size = 1024 * 1024
                if max_bytes is not None:
                    read_size = min(read_size, max_bytes + 1 - size)
                chunk = handle.read(read_size)
                if not chunk:
                    break
                if retain_content:
                    chunks.append(chunk)
                digest.update(chunk)
                size += len(chunk)
                if max_bytes is not None and size > max_bytes:
                    raise ContractError(f"überschreitet die Größengrenze {max_bytes} Bytes")
        after = requested.lstat()
        opened_after = os.fstat(descriptor)
        identity_before = (
            before.st_dev,
            before.st_ino,
            before.st_size,
            before.st_mtime_ns,
            before.st_ctime_ns,
        )
        identity_opened = (
            opened.st_dev,
            opened.st_ino,
            opened.st_size,
            opened.st_mtime_ns,
            opened.st_ctime_ns,
        )
        identity_opened_after = (
            opened_after.st_dev,
            opened_after.st_ino,
            opened_after.st_size,
            opened_after.st_mtime_ns,
            opened_after.st_ctime_ns,
        )
        identity_after = (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mtime_ns,
            after.st_ctime_ns,
        )
        if (
            identity_before != identity_opened
            or identity_opened != identity_opened_after
            or identity_before != identity_after
            or opened_after.st_size != size
        ):
            raise ContractError("wurde während des Lesens verändert")
        return (b"".join(chunks) if retain_content else b""), size, digest.hexdigest()
    finally:
        os.close(descriptor)


def read_stable(path: Path, *, max_bytes: int | None = None) -> tuple[bytes, str]:
    content, _, digest = _read_stable(path, max_bytes=max_bytes, retain_content=True)
    return content, digest


def hash_stable(path: Path, *, max_bytes: int | None = None) -> tuple[int, str]:
    _, size, digest = _read_stable(path, max_bytes=max_bytes, retain_content=False)
    return size, digest


def finite_number(value: Any, location: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ContractError(f"{location}: endliche Zahl erwartet")
    try:
        normalized = float(value)
    except (OverflowError, TypeError, ValueError) as exc:
        raise ContractError(f"{location}: endliche Zahl erwartet") from exc
    if not math.isfinite(normalized):
        raise ContractError(f"{location}: endliche Zahl erwartet")
    return normalized


def ensure_exhibit_label(value: Any, location: str = "label") -> str:
    text = ensure_text(value, location, max_length=19)
    if EXHIBIT_LABEL_RE.fullmatch(text) is None:
        raise ContractError(
            f"{location}: 'Anlage ', 1 bis 6 ASCII-Großbuchstaben und Nummer 1 bis 999999 erwartet"
        )
    return text


def validate_stamp_parameters(
    label: Any,
    pages_mode: Any,
    font_size: Any,
    margin: Any,
) -> tuple[str, str, float, float]:
    normalized_label = ensure_exhibit_label(label)
    normalized_mode = ensure_text(pages_mode, "pages_mode", max_length=8)
    if normalized_mode not in STAMP_RENDER_MODES:
        raise ContractError("pages_mode: first, all oder cover erwartet")
    normalized_font_size = finite_number(font_size, "font_size")
    if not 6.0 <= normalized_font_size <= 24.0:
        raise ContractError("font_size: Zahl zwischen 6 und 24 erwartet")
    normalized_margin = finite_number(margin, "margin")
    if not 8.0 <= normalized_margin <= 100.0:
        raise ContractError("margin: Zahl zwischen 8 und 100 erwartet")
    return normalized_label, normalized_mode, normalized_font_size, normalized_margin


def validate_pdf_page_count(value: Any, location: str = "PDF-Seitenzahl") -> int:
    count = ensure_int(value, location, minimum=1)
    if count > MAX_PDF_PAGES:
        raise ContractError(f"{location}: höchstens {MAX_PDF_PAGES} Seiten zulässig")
    return count


def validate_pdf_dimensions(
    width: Any,
    height: Any,
    location: str = "PDF-Seite",
) -> tuple[float, float]:
    normalized_width = finite_number(width, f"{location}.Breite")
    normalized_height = finite_number(height, f"{location}.Höhe")
    if normalized_width <= 0 or normalized_height <= 0:
        raise ContractError(f"{location}: positive Abmessungen erwartet")
    if (
        normalized_width > MAX_PDF_DIMENSION_POINTS
        or normalized_height > MAX_PDF_DIMENSION_POINTS
    ):
        raise ContractError(
            f"{location}: Abmessungen dürfen {MAX_PDF_DIMENSION_POINTS:g} Punkte nicht überschreiten"
        )
    return normalized_width, normalized_height

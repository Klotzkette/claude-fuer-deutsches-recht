#!/usr/bin/env python3
"""Inventarize a Diesel case folder safely and create a deterministic start card."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import threading
import unicodedata
import zipfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any


SCHEMA_VERSION = "1.0.0"
TOOL_VERSION = "1.2.0"
QUICKSTART_REQUEST = (
    "Neuer Diesel-Fall. Starte den Profi-Schnelllauf. Prüfe alle beigefügten Unterlagen, "
    "beginne mit Sicherheitsstopps und Fristen, stelle höchstens drei nur wirklich "
    "blockierende Fragen und liefere dann Fallkarte, Beleglücken sowie genau einen nächsten Schritt."
)
DEFAULT_MAX_FILES = 10_000
DEFAULT_MAX_FILE_BYTES = 200 * 1024 * 1024
DEFAULT_MAX_TOTAL_BYTES = 20 * 1024 * 1024 * 1024
MAX_CONFIG_FILE_BYTES = 1024 * 1024 * 1024
MAX_CONFIG_TOTAL_BYTES = 1024 * 1024 * 1024 * 1024
CAPTURE_LIMIT = 32 * 1024 * 1024
HEAD_LIMIT = 1024 * 1024
MAX_ZIP_MEMBERS = 10_000
MAX_ZIP_MEMBER_BYTES = 200 * 1024 * 1024
MAX_ZIP_TOTAL_BYTES = 1024 * 1024 * 1024
MAX_ZIP_PATH_BYTES = 1024
MAX_ZIP_COMPONENT_BYTES = 255
MAX_MANIFEST_PATH_CHARS = 4096
MAX_PDF_PAGES = 5_000
MAX_PDF_PROBE_MEMORY_BYTES = 512 * 1024 * 1024
PDF_PROBE_TIMEOUT_SECONDS = 8
MAX_MARKDOWN_ROWS = 80
CONTROL_RE = re.compile(r"[\x00-\x1f\x7f]")
PDF_PROBE_SEMAPHORE = threading.BoundedSemaphore(2)


class IntakeError(ValueError):
    """Raised for an invalid or unsafe invocation."""


class FileChangedError(IntakeError):
    """Raised when a file changes during the bounded read."""


class FileTooLargeError(IntakeError):
    """Raised before an oversized file is read."""


@dataclass(frozen=True)
class Candidate:
    path: Path
    relative: str
    kind: str
    size: int | None
    identity: tuple[int, int, int, int, int] | None


@dataclass(frozen=True)
class Fingerprint:
    size: int
    sha256: str
    head: bytes
    captured: bytes | None


CATEGORY_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("kauf_erwerb", ("kaufvertrag", "kauf_vertrag", "fahrzeugkauf", "bestellung", "kaufrechnung", "rechnung_auto", "rechnung_fahrzeug")),
    ("fahrzeugpapiere", ("fahrzeugschein", "fahrzeugbrief", "zulassung", "zlb", "coc", "uebereinstimmung", "typenschild", "fin_", "vin_")),
    ("kba_rueckruf", ("kba", "rueckruf", "rueckrufcode", "feldmassnahme", "servicemassnahme", "aktion_23", "aktion_45")),
    ("update_werkstatt", ("software_update", "update", "werkstatt", "service", "reparatur", "inspektion", "massnahme_bestaetigung")),
    ("finanzierung_leasing", ("finanzierung", "darlehen", "kredit", "leasing", "bankvertrag", "schlussrate")),
    ("zahlung", ("kontoauszug", "ueberweisung", "zahlung", "quittung", "abbuchung", "zahlungsbeleg")),
    ("gericht_schriftsatz", ("klage", "klageerwiderung", "replik", "schriftsatz", "urteil", "beschluss", "gericht", "ladung", "verfuegung", "aktenzeichen")),
    ("gutachten_messung", ("gutachten", "messung", "messbericht", "pruefbericht", "obd", "emission", "sachverstaendig")),
    ("vollmacht_mandat", ("vollmacht", "mandat", "prozessvollmacht", "abtretung")),
    ("korrespondenz", ("email", "e_mail", "mail", "korrespondenz", "anschreiben", "mahnung", "antwortschreiben")),
)

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".heic", ".webp"}
TEXT_EXTENSIONS = {".txt", ".md", ".csv", ".tsv", ".xml", ".html", ".htm", ".eml", ".svg", ".rtf", ".yaml", ".yml", ".toml", ".ini", ".log"}
OOXML_EXTENSIONS = {".docx", ".xlsx", ".pptx", ".docm", ".xlsm", ".pptm"}
MACRO_EXTENSIONS = {".docm", ".xlsm", ".pptm"}
LEGACY_OFFICE_EXTENSIONS = {".doc", ".xls", ".ppt"}
EXECUTABLE_EXTENSIONS = {".app", ".bat", ".cmd", ".com", ".dll", ".exe", ".jar", ".js", ".msi", ".ps1", ".py", ".scr", ".sh", ".vbs"}
SHORTCUT_EXTENSIONS = {".desktop", ".lnk", ".url", ".webloc"}
ACTIVE_TEXT_EXTENSIONS = {".html", ".htm", ".svg", ".rtf"}
EXECUTABLE_TYPES = {"windows_executable", "elf_executable", "mach_o_executable", "script"}
WINDOWS_RESERVED_NAMES = {
    "con", "prn", "aux", "nul",
    *(f"com{index}" for index in range(1, 10)),
    *(f"lpt{index}" for index in range(1, 10)),
}


def _unsafe_character(character: str) -> bool:
    category = unicodedata.category(character)
    return category.startswith("C") or category in {"Zl", "Zp"}


def normalized_token(value: str) -> str:
    value = value.replace("Ä", "Ae").replace("Ö", "Oe").replace("Ü", "Ue")
    value = value.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(character for character in value if not unicodedata.combining(character))
    value = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    return re.sub(r"_+", "_", value)


def portable_filename_key(name: str) -> str:
    path = Path(name)
    stem = normalized_token(path.stem) or "datei"
    extension = normalized_token(path.suffix.lstrip("."))
    return f"{stem}.{extension}" if extension else stem


def _binary_text_payload(payload: bytes) -> bool:
    if b"\x00" in payload:
        return True
    controls = sum(byte < 32 and byte not in {9, 10, 12, 13} for byte in payload)
    return bool(payload) and controls / len(payload) > 0.01


def markdown_cell(value: Any) -> str:
    text = str(value if value is not None else "-")
    text = "".join(" " if _unsafe_character(character) else character for character in text)
    text = CONTROL_RE.sub(" ", text).replace("\t", " ").replace("\r", " ").replace("\n", " ")
    text = " ".join(text.split())
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("`", "&#96;")


def classify_name(name: str, extension: str) -> str:
    token = normalized_token(name)
    for category, needles in CATEGORY_RULES:
        if any(needle in token for needle in needles):
            return category
    if extension in IMAGE_EXTENSIONS:
        return "foto"
    return "sonstiges"


def evidence_role(category: str) -> str:
    return {
        "kauf_erwerb": "kerndokument",
        "fahrzeugpapiere": "kerndokument",
        "kba_rueckruf": "betroffenheitshinweis",
        "update_werkstatt": "betroffenheitshinweis",
        "finanzierung_leasing": "vertragsbeleg",
        "zahlung": "zahlungsbeleg",
        "gericht_schriftsatz": "verfahrensdokument",
        "gutachten_messung": "sachbeleg",
        "vollmacht_mandat": "vertretungsbeleg",
        "korrespondenz": "kommunikationsbeleg",
        "foto": "bildbeleg",
    }.get(category, "ungeklaert")


def _identity(value: os.stat_result) -> tuple[int, int, int, int, int]:
    return (value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns, value.st_ctime_ns)


def read_stable(path: Path, maximum: int, expected_identity: tuple[int, int, int, int, int] | None = None) -> Fingerprint:
    requested = path.absolute()
    before = requested.lstat()
    if stat.S_ISLNK(before.st_mode) or not stat.S_ISREG(before.st_mode):
        raise IntakeError("keine reguläre Datei oder symbolischer Link")
    if expected_identity is not None and _identity(before) != expected_identity:
        raise FileChangedError("Datei wurde seit der Inventarisierung verändert")
    if before.st_size > maximum:
        raise FileTooLargeError(f"Datei überschreitet {maximum} Bytes")
    descriptor = os.open(requested, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        opened = os.fstat(descriptor)
        if _identity(before) != _identity(opened):
            raise FileChangedError("Datei wurde vor dem Lesen ausgetauscht")
        digest = hashlib.sha256()
        head = bytearray()
        captured = bytearray() if opened.st_size <= CAPTURE_LIMIT else None
        size = 0
        with os.fdopen(descriptor, "rb", closefd=False) as handle:
            while True:
                chunk = handle.read(1024 * 1024)
                if not chunk:
                    break
                size += len(chunk)
                if size > maximum:
                    raise FileTooLargeError(f"Datei überschreitet {maximum} Bytes")
                digest.update(chunk)
                if len(head) < HEAD_LIMIT:
                    head.extend(chunk[: HEAD_LIMIT - len(head)])
                if captured is not None:
                    captured.extend(chunk)
        opened_after = os.fstat(descriptor)
        after = requested.lstat()
        if (
            _identity(before) != _identity(opened_after)
            or _identity(before) != _identity(after)
            or size != opened.st_size
        ):
            raise FileChangedError("Datei wurde während des Lesens verändert")
        return Fingerprint(size, digest.hexdigest(), bytes(head), bytes(captured) if captured is not None else None)
    finally:
        os.close(descriptor)


def detect_type(head: bytes, captured: bytes | None, extension: str) -> str:
    if head.startswith(b"%PDF-"):
        return "pdf"
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if head.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    if head.startswith((b"II*\x00", b"MM\x00*")):
        return "tiff"
    if head.startswith((b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08")):
        if captured is not None:
            try:
                with zipfile.ZipFile(io.BytesIO(captured)) as archive:
                    members = archive.infolist()
                    if len(members) > MAX_ZIP_MEMBERS:
                        return "zip_container"
                    names = {member.filename for member in members}
                if "[Content_Types].xml" in names:
                    if "word/document.xml" in names:
                        return "docx_container"
                    if "xl/workbook.xml" in names:
                        return "xlsx_container"
                    if "ppt/presentation.xml" in names:
                        return "pptx_container"
                if "mimetype" in names and extension in {".odt", ".ods", ".odp"}:
                    return "opendocument_container"
            except (OSError, ValueError, zipfile.BadZipFile, RuntimeError):
                return "broken_zip"
        return "zip_container"
    if head.startswith(b"MZ"):
        return "windows_executable"
    if head.startswith(b"\x7fELF"):
        return "elf_executable"
    if head.startswith((b"\xfe\xed\xfa\xce", b"\xfe\xed\xfa\xcf", b"\xcf\xfa\xed\xfe", b"\xce\xfa\xed\xfe", b"\xca\xfe\xba\xbe", b"\xbe\xba\xfe\xca", b"\xca\xfe\xba\xbf")):
        return "mach_o_executable"
    if head.startswith((b"#!", b"\xef\xbb\xbf#!")):
        return "script"
    if head.startswith(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"):
        return "ole_container"
    if head.startswith(b"{\\rtf"):
        return "rtf"
    if extension == ".json" and captured is not None:
        try:
            def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
                result: dict[str, Any] = {}
                for key, value in pairs:
                    if key in result:
                        raise ValueError(f"doppelter JSON-Schlüssel: {key}")
                    result[key] = value
                return result

            def reject_constant(value: str) -> None:
                raise ValueError(f"nichtstandardkonstante: {value}")

            def finite_float(value: str) -> float:
                parsed = float(value)
                if not math.isfinite(parsed):
                    raise ValueError("nicht endliche Zahl")
                return parsed

            json.loads(
                captured.decode("utf-8"),
                object_pairs_hook=unique_object,
                parse_constant=reject_constant,
                parse_float=finite_float,
            )
            return "json"
        except (UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
            return "invalid_json"
    if extension in TEXT_EXTENSIONS or extension == ".json":
        try:
            payload = captured if captured is not None else head
            payload.decode("utf-8")
            if _binary_text_payload(payload):
                return "binary_unknown"
            if extension == ".rtf" and head.startswith(b"{\\rtf"):
                return "rtf"
            return "text"
        except UnicodeError:
            return "binary_unknown"
    return "binary_unknown"


def signature_issues(extension: str, detected: str) -> list[tuple[str, str, str]]:
    issues: list[tuple[str, str, str]] = []
    expected: set[str] | None = None
    if extension == ".pdf":
        expected = {"pdf"}
    elif extension in {".jpg", ".jpeg"}:
        expected = {"jpeg"}
    elif extension == ".png":
        expected = {"png"}
    elif extension in {".tif", ".tiff"}:
        expected = {"tiff"}
    elif extension in OOXML_EXTENSIONS:
        family = {".docx": "docx_container", ".docm": "docx_container", ".xlsx": "xlsx_container", ".xlsm": "xlsx_container", ".pptx": "pptx_container", ".pptm": "pptx_container"}[extension]
        expected = {family}
    elif extension == ".zip":
        expected = {"zip_container", "docx_container", "xlsx_container", "pptx_container", "opendocument_container"}
    elif extension == ".json":
        expected = {"json"}
    elif extension in LEGACY_OFFICE_EXTENSIONS:
        expected = {"ole_container"}
    elif extension == ".rtf":
        expected = {"rtf"}
    elif extension in TEXT_EXTENSIONS:
        expected = {"text"}
    if detected in EXECUTABLE_TYPES:
        issues.append(("blocker", "ausfuehrbarer_inhalt", "Ausführbarer Inhalt gehört nicht ungeprüft in die Fallakte."))
    if expected is not None and detected not in expected:
        issues.append(("blocker", "endung_signatur_widerspruch", "Dateiendung und erkannter Dateikopf widersprechen sich."))
    elif expected is None and detected in {"pdf", "png", "jpeg", "tiff"}:
        issues.append(("warning", "endung_unpassend", "Erkannter Dateityp und Dateiendung sollten vor Weitergabe abgeglichen werden."))
    if detected in {"broken_zip", "invalid_json"}:
        issues.append(("blocker", "container_unlesbar", "Der deklarierte Container ist strukturell nicht lesbar."))
    if extension in MACRO_EXTENSIONS:
        issues.append(("blocker", "makroformat", "Makrofähiges Office-Format muss vor Verarbeitung isoliert und geprüft werden."))
    if extension in LEGACY_OFFICE_EXTENSIONS:
        issues.append(("blocker", "legacy_office_format", "Altes Office-Binärformat kann aktive Inhalte tragen und muss isoliert konvertiert werden."))
    if extension in EXECUTABLE_EXTENSIONS:
        issues.append(("blocker", "ausfuehrbare_dateiendung", "Ausführbare oder skriptfähige Dateiendung ist im Akteneingang gesperrt."))
    if extension in SHORTCUT_EXTENSIONS:
        issues.append(("blocker", "verknuepfungsdatei", "Verknüpfungsdateien werden nicht als Akteninhalt geöffnet."))
    if extension in ACTIVE_TEXT_EXTENSIONS and detected in {"text", "rtf"}:
        issues.append(("warning", "aktiver_textcontainer", "Aktiver Textcontainer nur als Quelltext lesen und niemals ausführen oder rendern."))
    if extension in {".eml", ".msg"}:
        issues.append(("warning", "nachrichtencontainer_pruefen", "Nachrichtencontainer und eingebettete Anhänge gesondert inventarisieren."))
    return issues


def inspect_zip(content: bytes) -> list[tuple[str, str, str]]:
    issues: list[tuple[str, str, str]] = []
    issue_codes: set[str] = set()

    def flag(code: str, message: str) -> None:
        if code not in issue_codes:
            issue_codes.add(code)
            issues.append(("blocker", code, message))

    try:
        with zipfile.ZipFile(io.BytesIO(content)) as archive:
            all_members = archive.infolist()
            if len(all_members) > MAX_ZIP_MEMBERS:
                flag("zip_zu_viele_eintraege", "ZIP-Container überschreitet die sichere Eintragsgrenze.")
            members = all_members[:MAX_ZIP_MEMBERS]
            total = 0
            names: dict[str, str] = {}
            files: set[str] = set()
            required_directories: set[str] = set()
            allowed_compression = {
                zipfile.ZIP_STORED,
                zipfile.ZIP_DEFLATED,
                zipfile.ZIP_BZIP2,
                zipfile.ZIP_LZMA,
            }
            if hasattr(zipfile, "ZIP_ZSTANDARD"):
                allowed_compression.add(zipfile.ZIP_ZSTANDARD)
            for member in members:
                total += member.file_size
                normalized_name = member.filename.replace("\\", "/")
                is_directory = member.is_dir()
                raw_components = normalized_name.split("/")
                if is_directory and raw_components[-1:] == [""]:
                    raw_components = raw_components[:-1]
                pure = PurePosixPath(normalized_name)
                if (
                    not normalized_name
                    or "\\" in member.filename
                    or normalized_name.startswith("/")
                    or re.match(r"^[A-Za-z]:", normalized_name)
                    or ".." in pure.parts
                    or not raw_components
                    or any(component in {"", ".", ".."} for component in raw_components)
                    or any(_unsafe_character(character) for character in normalized_name)
                ):
                    flag("zip_pfadtraversal", "ZIP-Container enthält einen unsicheren Mitgliedspfad.")
                if (
                    len(normalized_name.encode("utf-8", errors="surrogatepass")) > MAX_ZIP_PATH_BYTES
                    or any(len(component.encode("utf-8", errors="surrogatepass")) > MAX_ZIP_COMPONENT_BYTES for component in raw_components)
                ):
                    flag("zip_pfad_zu_lang", "ZIP-Container enthält einen portabel überlangen Mitgliedspfad.")
                portable_components: list[str] = []
                for component in raw_components:
                    portable_component = unicodedata.normalize("NFKC", component).casefold().rstrip(" .")
                    portable_components.append(portable_component)
                    basename = portable_component.split(".", 1)[0]
                    if (
                        portable_component != unicodedata.normalize("NFKC", component).casefold()
                        or basename in WINDOWS_RESERVED_NAMES
                        or any(character in '<>:"|?*' for character in component)
                    ):
                        flag("zip_nicht_portabel", "ZIP-Container enthält einen unter Windows oder im DMS nicht portablen Mitgliedsnamen.")
                portable_name = "/".join(portable_components)
                if portable_name in names:
                    flag("zip_namenskollision", "ZIP-Container enthält doppelte oder portabel kollidierende Mitgliedspfade.")
                else:
                    names[portable_name] = normalized_name
                canonical_path = portable_name.rstrip("/")
                for index in range(1, len(portable_components)):
                    required_directories.add("/".join(portable_components[:index]))
                if not is_directory:
                    files.add(canonical_path)
                if member.flag_bits & 0x1:
                    flag("zip_verschluesselt", "Verschlüsselter ZIP-Inhalt kann nicht verlässlich inventarisiert werden.")
                if member.compress_type not in allowed_compression:
                    flag("zip_kompression_unbekannt", "ZIP-Container verwendet ein nicht freigegebenes Kompressionsverfahren.")
                if member.file_size > MAX_ZIP_MEMBER_BYTES:
                    flag("zip_mitglied_zu_gross", "ZIP-Container enthält ein übergroßes Mitglied.")
                if member.file_size and (member.compress_size == 0 or member.file_size / member.compress_size > 1000):
                    flag("zip_extreme_kompression", "ZIP-Container weist eine extreme oder widersprüchliche Kompressionsrate auf.")
                mode = (member.external_attr >> 16) & 0xFFFF
                file_type = stat.S_IFMT(mode)
                if file_type not in {0, stat.S_IFREG, stat.S_IFDIR}:
                    flag("zip_spezialdatei", "ZIP-Container enthält einen symbolischen Link oder eine Spezialdatei.")
                if (is_directory and file_type == stat.S_IFREG) or (not is_directory and file_type == stat.S_IFDIR):
                    flag("zip_typ_widerspruch", "ZIP-Mitglied widerspricht sich bei Pfadform und Dateityp.")
                if is_directory and member.file_size:
                    flag("zip_verzeichnis_mit_daten", "ZIP-Verzeichniseintrag enthält unerwartete Nutzdaten.")
                lower_name = normalized_name.casefold()
                if lower_name.endswith("vbaproject.bin") or "/activex/" in f"/{lower_name}":
                    flag("container_aktiver_inhalt", "Office-Container enthält Makro- oder ActiveX-Inhalt.")
                if Path(lower_name).suffix in EXECUTABLE_EXTENSIONS | SHORTCUT_EXTENSIONS:
                    flag("zip_ausfuehrbarer_inhalt", "ZIP-Container enthält eine ausführbare, skriptfähige oder verweisende Datei.")
            if files & required_directories:
                flag("zip_datei_verzeichnis_schatten", "ZIP-Container verwendet denselben Pfad als Datei und als Verzeichniswurzel.")
            if total > MAX_ZIP_TOTAL_BYTES:
                flag("zip_entpackt_zu_gross", "ZIP-Container würde die sichere Entpackgrenze überschreiten.")
    except (OSError, ValueError, zipfile.BadZipFile, RuntimeError, OverflowError):
        flag("zip_unlesbar", "ZIP-Container ist nicht zuverlässig lesbar.")
    return issues


def _pdf_probe_worker() -> int:
    try:
        import resource
    except ImportError:
        resource = None
    if resource is not None:
        resource_limits = (
            ("RLIMIT_CPU", max(1, PDF_PROBE_TIMEOUT_SECONDS - 2)),
            ("RLIMIT_AS", MAX_PDF_PROBE_MEMORY_BYTES),
            ("RLIMIT_FSIZE", 1024 * 1024),
            ("RLIMIT_NOFILE", 64),
            ("RLIMIT_CORE", 0),
        )
        for limit_name, desired in resource_limits:
            if not hasattr(resource, limit_name):
                continue
            limit = getattr(resource, limit_name)
            try:
                _, hard = resource.getrlimit(limit)
                bounded = desired if hard == resource.RLIM_INFINITY else min(desired, hard)
                resource.setrlimit(limit, (bounded, bounded))
            except (OSError, ValueError):
                pass
    content = sys.stdin.buffer.read(CAPTURE_LIMIT + 1)
    if len(content) > CAPTURE_LIMIT:
        result = {"status": "payload_too_large"}
    else:
        try:
            from pypdf import PdfReader
        except ImportError:
            result = {"status": "parser_missing"}
        else:
            try:
                reader = PdfReader(io.BytesIO(content), strict=True)
                if reader.is_encrypted:
                    result = {"status": "encrypted"}
                else:
                    pages = len(reader.pages)
                    if pages > MAX_PDF_PAGES:
                        result = {"status": "page_limit", "pages": pages}
                    else:
                        catalog = reader.trailer.get("/Root")
                        if hasattr(catalog, "get_object"):
                            catalog = catalog.get_object()
                        active = isinstance(catalog, dict) and any(key in catalog for key in ("/OpenAction", "/AA"))
                        if isinstance(catalog, dict):
                            names = catalog.get("/Names")
                            if hasattr(names, "get_object"):
                                names = names.get_object()
                            active = active or (
                                isinstance(names, dict)
                                and any(key in names for key in ("/JavaScript", "/EmbeddedFiles"))
                            )
                        if not active:
                            active = any("/AA" in reader.pages[index] for index in range(pages))
                        if active:
                            result = {"status": "active", "pages": pages}
                        else:
                            sample = " ".join((reader.pages[index].extract_text() or "") for index in range(min(3, pages)))
                            result = {
                                "status": "ok",
                                "pages": pages,
                                "text": len(" ".join(sample.split())) >= 40,
                            }
            except Exception as exc:  # pypdf exposes parser-specific exception classes.
                result = {"status": "parser_error", "error": type(exc).__name__}
    print(json.dumps(result, allow_nan=False, sort_keys=True))
    return 0


def inspect_pdf(content: bytes | None, head: bytes) -> tuple[str, int | None, list[tuple[str, str, str]]]:
    issues: list[tuple[str, str, str]] = []
    probe = content if content is not None else head
    if any(marker in probe for marker in (b"/JavaScript", b"/JS ", b"/OpenAction", b"/Launch", b"/EmbeddedFile")):
        issues.append(("blocker", "pdf_aktiver_inhalt", "PDF enthält Hinweise auf aktive oder eingebettete Inhalte."))
    if b"/Encrypt" in probe:
        issues.append(("blocker", "pdf_verschluesselt", "PDF enthält einen Verschlüsselungshinweis und kann nicht vollständig geprüft werden."))
    if content is None:
        return "ocr_pruefen", None, issues
    if issues:
        encrypted = any(code == "pdf_verschluesselt" for _, code, _ in issues)
        return "nicht_lesbar" if encrypted else "ocr_pruefen", None, issues
    try:
        with PDF_PROBE_SEMAPHORE:
            process = subprocess.run(
                [sys.executable, "-I", str(Path(__file__).resolve()), "--_pdf-probe"],
                input=content,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=PDF_PROBE_TIMEOUT_SECONDS,
                check=False,
            )
    except subprocess.TimeoutExpired:
        issues.append(("blocker", "pdf_pruefung_timeout", "PDF-Strukturprüfung hat das feste Zeitlimit überschritten."))
        return "nicht_lesbar", None, issues
    except OSError:
        issues.append(("warning", "pdf_pruefung_nicht_gestartet", "Isolierte PDF-Strukturprüfung konnte nicht gestartet werden."))
        return "ocr_pruefen", None, issues
    if process.returncode != 0 or len(process.stdout) > 4096:
        issues.append(("blocker", "pdf_pruefung_prozessfehler", "Isolierte PDF-Strukturprüfung endete nicht vertragsgemäß."))
        return "nicht_lesbar", None, issues
    try:
        result = json.loads(process.stdout.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError):
        issues.append(("blocker", "pdf_pruefung_antwortfehler", "Isolierte PDF-Strukturprüfung lieferte keine gültige Antwort."))
        return "nicht_lesbar", None, issues
    if not isinstance(result, dict) or not isinstance(result.get("status"), str):
        issues.append(("blocker", "pdf_pruefung_antwortfehler", "Isolierte PDF-Strukturprüfung lieferte keine gültige Antwort."))
        return "nicht_lesbar", None, issues
    if result["status"] == "ok" and isinstance(result.get("pages"), int) and not isinstance(result.get("pages"), bool):
        return "textschicht_erkannt" if result.get("text") is True else "ocr_pruefen", result["pages"], issues
    if result["status"] == "encrypted":
        issues.append(("blocker", "pdf_verschluesselt", "Verschlüsseltes PDF kann nicht vollständig geprüft werden."))
    elif result["status"] == "active":
        issues.append(("blocker", "pdf_aktiver_inhalt", "PDF-Objektstruktur enthält aktive oder eingebettete Inhalte."))
    elif result["status"] == "parser_missing":
        issues.append(("warning", "pdf_parser_fehlt", "pypdf fehlt; Seiten, Verschlüsselung und Textschicht konnten nicht vollständig geprüft werden."))
        return "ocr_pruefen", None, issues
    elif result["status"] == "page_limit":
        issues.append(("blocker", "pdf_seitenlimit", f"PDF überschreitet die sichere Grenze von {MAX_PDF_PAGES} Seiten."))
    elif result["status"] == "payload_too_large":
        issues.append(("blocker", "pdf_pruefung_zu_gross", "PDF überschreitet die interne Tiefenprüfgrenze."))
    else:
        error_name = result.get("error") if isinstance(result.get("error"), str) else "ParserError"
        issues.append(("blocker", "pdf_struktur_unlesbar", f"PDF-Strukturprüfung fehlgeschlagen ({error_name})."))
    return "nicht_lesbar", None, issues


def _candidate_issue(relative: str, severity: str, code: str, message: str) -> dict[str, Any]:
    return {"severity": severity, "code": code, "paths": [relative], "message": message}


def scan_candidates(root: Path, excluded: Path | None, max_files: int) -> tuple[list[Candidate], list[dict[str, Any]]]:
    candidates: list[Candidate] = []
    issues: list[dict[str, Any]] = []
    stack = [root]
    stopped = False
    seen_entries = 0
    while stack and not stopped:
        directory = stack.pop()
        try:
            directory_info = directory.lstat()
            if stat.S_ISLNK(directory_info.st_mode) or not stat.S_ISDIR(directory_info.st_mode):
                raise IntakeError("Verzeichnispfad wurde ausgetauscht oder ist ein symbolischer Link")
            remaining = max_files - seen_entries
            with os.scandir(directory) as iterator:
                entries = []
                for item in iterator:
                    item_path = Path(item.path).absolute()
                    if excluded is not None and item_path == excluded:
                        continue
                    entries.append(item)
                    if len(entries) > remaining:
                        break
        except (OSError, IntakeError) as exc:
            relative = directory.relative_to(root).as_posix() or "."
            issues.append(_candidate_issue(relative, "blocker", "verzeichnis_unlesbar", f"Verzeichnis kann nicht gelesen werden ({type(exc).__name__})."))
            continue
        if len(entries) > remaining:
            issues.append(_candidate_issue(".", "blocker", "dateilimit", f"Inventar wurde nach {max_files} Dateisystemeinträgen gestoppt."))
            stopped = True
            break
        entries.sort(key=lambda item: (unicodedata.normalize("NFC", item.name), item.name))
        seen_entries += len(entries)
        child_directories: list[Path] = []
        for entry in entries:
            path = Path(entry.path).absolute()
            relative = path.relative_to(root).as_posix()
            try:
                info = entry.stat(follow_symlinks=False)
            except OSError as exc:
                candidates.append(Candidate(path, relative, "unreadable", None, None))
                issues.append(_candidate_issue(relative, "blocker", "datei_unlesbar", f"Dateimetadaten können nicht gelesen werden ({type(exc).__name__})."))
            else:
                identity = _identity(info)
                if stat.S_ISLNK(info.st_mode):
                    candidates.append(Candidate(path, relative, "symlink", info.st_size, identity))
                    issues.append(_candidate_issue(relative, "blocker", "symbolischer_link", "Symbolische Links werden nicht verfolgt."))
                elif stat.S_ISDIR(info.st_mode):
                    if any(_unsafe_character(character) for character in relative):
                        issues.append(_candidate_issue(relative, "blocker", "unsicheres_verzeichniszeichen", "Verzeichnispfad enthält ein Steuer- oder Formatzeichen."))
                    if len(relative) > MAX_MANIFEST_PATH_CHARS:
                        issues.append(_candidate_issue(relative, "blocker", "verzeichnispfad_zu_lang", "Relativer Verzeichnispfad überschreitet die Manifestgrenze."))
                    child_directories.append(path)
                elif stat.S_ISREG(info.st_mode):
                    candidates.append(Candidate(path, relative, "regular", info.st_size, identity))
                else:
                    candidates.append(Candidate(path, relative, "special", info.st_size, identity))
                    issues.append(_candidate_issue(relative, "blocker", "spezialdatei", "Nur reguläre Dateien dürfen inventarisiert werden."))
        stack.extend(reversed(child_directories))
    return sorted(candidates, key=lambda item: (unicodedata.normalize("NFC", item.relative), item.relative)), issues


def process_candidate(candidate: Candidate, max_file_bytes: int, within_total_budget: bool = True) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    extension = candidate.path.suffix.lower()
    category = classify_name(candidate.path.name, extension)
    document: dict[str, Any] = {
        "id": "",
        "path": candidate.relative,
        "name": candidate.path.name,
        "extension": extension,
        "kind": candidate.kind,
        "bytes": candidate.size,
        "sha256": None,
        "detected_type": "not_read",
        "category": category,
        "classification_basis": "dateiname_heuristik" if category != "foto" else "endung_und_dateiname_heuristik",
        "evidence_role": evidence_role(category),
        "text_status": "nicht_geprueft",
        "pages": None,
        "duplicate_group": None,
        "filename_collision_group": None,
        "issues": [],
    }
    issues: list[dict[str, Any]] = []
    if any(_unsafe_character(character) for character in candidate.relative):
        issues.append(_candidate_issue(candidate.relative, "blocker", "unsicheres_dateizeichen", "Dateipfad enthält Steuer- oder Formatzeichen."))
    if len(candidate.relative) > MAX_MANIFEST_PATH_CHARS:
        issues.append(_candidate_issue(candidate.relative, "blocker", "dateipfad_manifestgrenze", "Relativer Dateipfad überschreitet die Manifestgrenze."))
    if len(candidate.relative) > 500:
        issues.append(_candidate_issue(candidate.relative, "warning", "dateipfad_zu_lang", "Relativer Dateipfad überschreitet 500 Zeichen."))
    if candidate.path.name != candidate.path.name.strip() or candidate.path.name.startswith("."):
        issues.append(_candidate_issue(candidate.relative, "warning", "problematischer_dateiname", "Versteckter oder außen mit Leerzeichen versehener Dateiname."))
    if candidate.kind != "regular":
        document["issues"] = sorted({item["code"] for item in issues})
        return document, issues
    if not within_total_budget:
        issues.append(_candidate_issue(candidate.relative, "blocker", "gesamtbudget_datei_uebersprungen", "Datei wurde wegen Überschreitung des Gesamtgrößenlimits nicht gelesen."))
        document["issues"] = sorted({item["code"] for item in issues})
        return document, issues
    try:
        fingerprint = read_stable(candidate.path, max_file_bytes, candidate.identity)
    except FileTooLargeError:
        issues.append(_candidate_issue(candidate.relative, "blocker", "datei_zu_gross", f"Datei überschreitet {max_file_bytes} Bytes und wurde nicht gelesen."))
    except (OSError, IntakeError) as exc:
        issues.append(_candidate_issue(candidate.relative, "blocker", "stabiler_lesefehler", f"Datei konnte nicht stabil gelesen werden ({type(exc).__name__})."))
    else:
        detected = detect_type(fingerprint.head, fingerprint.captured, extension)
        document.update({"bytes": fingerprint.size, "sha256": fingerprint.sha256, "detected_type": detected})
        for severity, code, message in signature_issues(extension, detected):
            issues.append(_candidate_issue(candidate.relative, severity, code, message))
        if detected in {"zip_container", "docx_container", "xlsx_container", "pptx_container", "opendocument_container"} and fingerprint.captured is not None:
            for severity, code, message in inspect_zip(fingerprint.captured):
                issues.append(_candidate_issue(candidate.relative, severity, code, message))
        elif detected in {"zip_container", "docx_container", "xlsx_container", "pptx_container", "opendocument_container"}:
            issues.append(_candidate_issue(candidate.relative, "warning", "container_tiefenpruefung_ausstehend", "Großer Container wurde gehasht, aber nicht strukturell tiefengeprüft."))
        if detected == "pdf":
            if fingerprint.captured is None:
                issues.append(_candidate_issue(candidate.relative, "warning", "pdf_tiefenpruefung_ausstehend", "Großes PDF wurde gehasht; Verschlüsselung, aktive Inhalte, Seiten und Textschicht sind nur teilweise geprüft."))
            text_status, pages, pdf_issues = inspect_pdf(fingerprint.captured, fingerprint.head)
            document["text_status"] = text_status
            document["pages"] = pages
            for severity, code, message in pdf_issues:
                issues.append(_candidate_issue(candidate.relative, severity, code, message))
        elif detected in {"png", "jpeg", "tiff"}:
            document["text_status"] = "ocr_pruefen"
        elif detected in {"text", "json"} and fingerprint.captured is None:
            document["text_status"] = "nicht_geprueft"
            issues.append(_candidate_issue(candidate.relative, "warning", "text_tiefenpruefung_ausstehend", "Große Textdatei wurde gehasht; UTF-8- und Binärprüfung decken nur den Dateikopf ab."))
        elif detected in {"text", "json", "docx_container"}:
            document["text_status"] = "digitaltext"
        elif detected in {"xlsx_container", "pptx_container", "opendocument_container", "rtf"}:
            document["text_status"] = "strukturierter_container"
        else:
            document["text_status"] = "nicht_anwendbar"
    document["issues"] = sorted({item["code"] for item in issues})
    return document, issues


def _group_duplicates(documents: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_hash: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for document in documents:
        if isinstance(document["bytes"], int) and document["sha256"]:
            by_hash[(document["bytes"], document["sha256"])].append(document)
    groups: list[dict[str, Any]] = []
    duplicates = [items for items in by_hash.values() if len(items) > 1]
    duplicates.sort(key=lambda items: [item["path"] for item in items])
    for index, items in enumerate(duplicates, 1):
        group_id = f"DUP-{index:03d}"
        for item in items:
            item["duplicate_group"] = group_id
        groups.append({"id": group_id, "sha256": items[0]["sha256"], "bytes": items[0]["bytes"], "paths": [item["path"] for item in items]})
    return groups


def _group_filename_collisions(documents: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_name: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for document in documents:
        token = portable_filename_key(document["name"])
        by_name[token].append(document)
    groups: list[dict[str, Any]] = []
    collisions = [items for items in by_name.values() if len(items) > 1 and len({item["path"] for item in items}) > 1]
    collisions.sort(key=lambda items: [item["path"] for item in items])
    for index, items in enumerate(collisions, 1):
        group_id = f"NAME-{index:03d}"
        for item in items:
            item["filename_collision_group"] = group_id
        groups.append({"id": group_id, "portable_name": portable_filename_key(items[0]["name"]), "paths": [item["path"] for item in items]})
    return groups


def build_manifest(root: Path, *, excluded: Path | None = None, jobs: int = 4, max_files: int = DEFAULT_MAX_FILES, max_file_bytes: int = DEFAULT_MAX_FILE_BYTES, max_total_bytes: int = DEFAULT_MAX_TOTAL_BYTES) -> dict[str, Any]:
    for label, value in (("jobs", jobs), ("max_files", max_files), ("max_file_bytes", max_file_bytes), ("max_total_bytes", max_total_bytes)):
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise IntakeError(f"{label} muss eine positive Ganzzahl sein")
    if jobs > 16:
        raise IntakeError("jobs darf höchstens 16 sein")
    if max_files > DEFAULT_MAX_FILES:
        raise IntakeError(f"max_files darf höchstens {DEFAULT_MAX_FILES} sein")
    if max_file_bytes > MAX_CONFIG_FILE_BYTES:
        raise IntakeError(f"max_file_bytes darf höchstens {MAX_CONFIG_FILE_BYTES} sein")
    if max_total_bytes > MAX_CONFIG_TOTAL_BYTES:
        raise IntakeError(f"max_total_bytes darf höchstens {MAX_CONFIG_TOTAL_BYTES} sein")
    requested = root.expanduser().absolute()
    try:
        root_info = requested.lstat()
    except OSError as exc:
        raise IntakeError(f"Aktenordner kann nicht gelesen werden: {exc}") from exc
    if stat.S_ISLNK(root_info.st_mode) or not stat.S_ISDIR(root_info.st_mode):
        raise IntakeError("Aktenwurzel muss ein echtes Verzeichnis ohne symbolischen Link sein")
    if not requested.name or any(_unsafe_character(character) for character in requested.name):
        raise IntakeError("Name der Aktenwurzel enthält ein unsicheres Steuer- oder Formatzeichen")
    excluded_abs = excluded.expanduser().absolute() if excluded is not None else None
    candidates, issues = scan_candidates(requested, excluded_abs, max_files)
    try:
        root_after_scan = requested.lstat()
    except OSError as exc:
        raise IntakeError("Aktenwurzel wurde während der Inventarisierung entfernt") from exc
    if _identity(root_info) != _identity(root_after_scan):
        raise IntakeError("Aktenwurzel wurde während der Inventarisierung verändert")
    total_bytes = sum(candidate.size or 0 for candidate in candidates if candidate.kind == "regular")
    if total_bytes > max_total_bytes:
        issues.append(_candidate_issue(".", "blocker", "gesamtgroesse", f"Reguläre Dateien überschreiten zusammen {max_total_bytes} Bytes."))
    running_bytes = 0
    within_budget: list[bool] = []
    for candidate in candidates:
        allowed = True
        if candidate.kind == "regular":
            running_bytes += candidate.size or 0
            allowed = running_bytes <= max_total_bytes
        within_budget.append(allowed)
    with ThreadPoolExecutor(max_workers=jobs) as executor:
        processed = list(executor.map(lambda pair: process_candidate(pair[0], max_file_bytes, pair[1]), zip(candidates, within_budget)))
    documents = [item[0] for item in processed]
    for index, document in enumerate(documents, 1):
        document["id"] = f"D-{index:05d}"
    for _, document_issues in processed:
        issues.extend(document_issues)
    duplicate_groups = _group_duplicates(documents)
    filename_collision_groups = _group_filename_collisions(documents)
    for group in duplicate_groups:
        issues.append({"severity": "warning", "code": "exakte_dubletten", "paths": group["paths"], "message": "Inhaltsgleiche Dateien wurden mehrfach gefunden; jüngste oder beweisstärkste Fassung fachlich bestimmen."})
    for group in filename_collision_groups:
        if len({next(item["sha256"] for item in documents if item["path"] == path) for path in group["paths"]}) > 1:
            issues.append({"severity": "warning", "code": "portable_namenskollision", "paths": group["paths"], "message": "Verschiedene Inhalte würden bei portabler Dateinamennormalisierung kollidieren."})
    unique_issues: dict[tuple[str, str, tuple[str, ...], str], dict[str, Any]] = {}
    for issue in issues:
        key = (issue["severity"], issue["code"], tuple(issue["paths"]), issue["message"])
        unique_issues[key] = issue
    issues = list(unique_issues.values())
    for document in documents:
        inherited = {item["code"] for item in issues if document["path"] in item["paths"]}
        document["issues"] = sorted(set(document["issues"]) | inherited)
    category_counts = Counter(document["category"] for document in documents if document["kind"] == "regular")
    missing_core: list[str] = []
    if category_counts["kauf_erwerb"] == 0:
        missing_core.append("Kaufvertrag oder Erwerbsrechnung ist anhand der Dateinamen nicht erkennbar.")
    if category_counts["fahrzeugpapiere"] == 0:
        missing_core.append("Fahrzeugpapier oder FIN-Nachweis ist anhand der Dateinamen nicht erkennbar.")
    if not documents:
        missing_core.append("Der Aktenordner enthält keine inventarisierbaren Einträge.")
    blockers = sum(item["severity"] == "blocker" for item in issues)
    warnings = sum(item["severity"] == "warning" for item in issues)
    ocr_review = sum(document["text_status"] == "ocr_pruefen" for document in documents)
    if blockers:
        status = "BLOCKIERT"
    elif warnings or ocr_review or missing_core:
        status = "PRUEFUNG_NOETIG"
    else:
        status = "STARTBEREIT"
    focus: list[str] = []
    if blockers:
        focus.append("Unsichere oder nicht stabil lesbare Dateien vor jeder Inhaltsanalyse isolieren.")
    if duplicate_groups:
        focus.append("Dubletten und Fassungsstand fachlich auflösen; Hashgleichheit sagt nichts über Beweisrang oder Aktualität.")
    if ocr_review:
        focus.append("OCR-Bedarf und Seitenvollständigkeit visuell prüfen.")
    focus.extend(missing_core)
    if not focus:
        focus.append("Maschineninventar in Skill 01 übernehmen und Stammdaten mit Fundstelle und Sicherheit extrahieren.")
    severity_order = {"blocker": 0, "warning": 1, "info": 2}
    issues.sort(key=lambda item: (severity_order[item["severity"]], item["code"], item["paths"]))
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": {"name": "diesel-aktenstart", "version": TOOL_VERSION},
        "root": {"name": requested.name},
        "limits": {"max_files": max_files, "max_file_bytes": max_file_bytes, "max_total_bytes": max_total_bytes},
        "summary": {
            "status": status,
            "entries_total": len(documents),
            "regular_files": sum(document["kind"] == "regular" for document in documents),
            "bytes_total": total_bytes,
            "hashed_files": sum(document["sha256"] is not None for document in documents),
            "categories": dict(sorted(category_counts.items())),
            "duplicate_groups": len(duplicate_groups),
            "filename_collision_groups": len(filename_collision_groups),
            "ocr_review_files": ocr_review,
            "blockers": blockers,
            "warnings": warnings,
        },
        "routing": {"next_skill": "01-kaltstart-aktenaufnahme", "focus": focus, "missing_core": missing_core},
        "documents": documents,
        "duplicate_groups": duplicate_groups,
        "filename_collision_groups": filename_collision_groups,
        "issues": issues,
        "notices": [
            "Kategorie und Beweisrolle sind vorsichtige Dateinamenheuristiken, keine Inhalts- oder Rechtsfeststellungen.",
            "Hash, Größe, Dateikopf und Pfad sind Maschinenbefunde; Lesbarkeit, Vollständigkeit, Echtheit und Beweiswert bleiben fachlich zu prüfen.",
            "Das Manifest enthält bewusst keinen absoluten Quellpfad und keinen Laufzeitstempel.",
        ],
    }


def format_bytes(value: int) -> str:
    units = ("B", "KiB", "MiB", "GiB", "TiB")
    number = float(value)
    for unit in units:
        if number < 1024 or unit == units[-1]:
            return f"{number:.0f} {unit}" if unit == "B" else f"{number:.1f} {unit}"
        number /= 1024
    return f"{value} B"


def render_markdown(manifest: dict[str, Any]) -> str:
    summary = manifest["summary"]
    traffic_light = {
        "BLOCKIERT": "rot - Mindestens ein Sicherheitsstopp verhindert die automatische Inhaltsanalyse der betroffenen Datei.",
        "PRUEFUNG_NOETIG": "gelb - Das Inventar ist erstellt; ausdrücklich benannte Lücken oder Kontrollen bleiben offen.",
        "STARTBEREIT": "grün - Das Maschineninventar enthält keinen Stopp; die fachliche Inhaltsprüfung steht noch aus.",
    }[summary["status"]]
    lines = [
        "# Dieselgate-Aktenstart",
        "",
        "## Kanzlei-Arbeitskopf",
        "",
        "| Feld | Stand |",
        "|---|---|",
        f"| Status | `{summary['status']}` |",
        f"| Ampel | {traffic_light} |",
        "| Frist | Nicht maschinell geprüft; Dokumentfristen in Skill 01 feststellen. |",
        "| Quellenstand | Nur Maschinenbefunde; Inhalts- und Rechtsquellenprüfung offen. |",
        "| Arbeitsprodukt | Aktenstart-Manifest und kompakte Startkarte. |",
        "| Nächster Schritt | Nächster Skill: `01-kaltstart-aktenaufnahme`. |",
        "",
        "## Kennzahlen",
        "",
        f"- **Bestand:** {summary['regular_files']} reguläre Dateien, {format_bytes(summary['bytes_total'])}, {summary['hashed_files']} stabil gehasht.",
        f"- **Kontrolle:** {summary['blockers']} Stopps, {summary['warnings']} Warnungen, {summary['ocr_review_files']} OCR-Prüfungen.",
        "",
        "## Jetzt bearbeiten",
        "",
    ]
    lines.extend(f"- {markdown_cell(item)}" for item in manifest["routing"]["focus"])
    lines.extend(
        [
            "",
            "## Übergabe in den Arbeitschat",
            "",
            "Die unveränderten Originaldateien zusammen mit `aktenstart-manifest.json` und dieser Startkarte bereitstellen. Dann senden:",
            "",
            f"> {QUICKSTART_REQUEST}",
        ]
    )
    if manifest["issues"]:
        lines.extend(["", "## Stopps und Warnungen", ""])
        for issue in manifest["issues"][:40]:
            paths = ", ".join(f"`{markdown_cell(path)}`" for path in issue["paths"][:5])
            suffix = " …" if len(issue["paths"]) > 5 else ""
            lines.append(f"- **{issue['severity'].upper()} · `{issue['code']}`:** {markdown_cell(issue['message'])} ({paths}{suffix})")
        if len(manifest["issues"]) > 40:
            lines.append(f"- Weitere {len(manifest['issues']) - 40} Befunde stehen vollständig im JSON-Manifest.")
    lines.extend(["", "## Inventar", "", "| ID | Datei | Kategorie | Typ | Text/OCR | Größe | SHA-256 |", "|---|---|---|---|---|---:|---|"])
    for document in manifest["documents"][:MAX_MARKDOWN_ROWS]:
        digest = document["sha256"][:12] if document["sha256"] else "-"
        lines.append(
            "| {id} | `{path}` | {category} | {kind} / {detected} | {text} | {size} | `{digest}` |".format(
                id=markdown_cell(document["id"]),
                path=markdown_cell(document["path"]),
                category=markdown_cell(document["category"]),
                kind=markdown_cell(document["kind"]),
                detected=markdown_cell(document["detected_type"]),
                text=markdown_cell(document["text_status"]),
                size=markdown_cell(format_bytes(document["bytes"] or 0)),
                digest=digest,
            )
        )
    if len(manifest["documents"]) > MAX_MARKDOWN_ROWS:
        lines.extend(["", f"Das kompakte Blatt zeigt {MAX_MARKDOWN_ROWS} von {len(manifest['documents'])} Einträgen; das JSON-Manifest enthält alle."])
    lines.extend(["", "> Kategorien und Beweisrollen sind Dateinamenheuristiken. Inhalt, Echtheit, Vollständigkeit, Fahrzeugbezug und Rechtsfolge sind in Skill 01 beziehungsweise den Fachskills zu prüfen.", ""])
    return "\n".join(lines)


def _atomic_write(path: Path, content: bytes, force: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() or path.is_symlink():
        if path.is_symlink():
            raise IntakeError(f"Ausgabedatei ist ein symbolischer Link: {path}")
        if not force:
            raise IntakeError(f"Ausgabedatei existiert bereits; --force erforderlich: {path}")
        if not path.is_file():
            raise IntakeError(f"Ausgabeziel ist keine reguläre Datei: {path}")
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        if path.exists() and not force:
            raise IntakeError(f"Ausgabedatei wurde während des Laufs angelegt: {path}")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _validate_bundle_entries(target: Path, expected_names: set[str]) -> None:
    unexpected: list[str] = []
    unsafe: list[str] = []
    for path in target.iterdir():
        if path.name not in expected_names:
            unexpected.append(path.name)
            continue
        info = path.lstat()
        if stat.S_ISLNK(info.st_mode) or not stat.S_ISREG(info.st_mode):
            unsafe.append(path.name)
    if unexpected:
        raise IntakeError(f"Ausgabeverzeichnis enthält fremde Dateien: {', '.join(sorted(unexpected))}")
    if unsafe:
        raise IntakeError(f"Erwarteter Bundle-Name ist keine reguläre Datei: {', '.join(sorted(unsafe))}")


def _remove_bundle_backup(backup: Path, expected_names: set[str]) -> None:
    _validate_bundle_entries(backup, expected_names)
    for name in sorted(expected_names):
        path = backup / name
        if not path.exists() and not path.is_symlink():
            continue
        info = path.lstat()
        if stat.S_ISLNK(info.st_mode) or not stat.S_ISREG(info.st_mode):
            raise IntakeError(f"Altes Bundle-Ziel wurde vor der Bereinigung ausgetauscht: {name}")
        path.unlink()
    backup.rmdir()


def write_bundle(output_dir: Path, manifest: dict[str, Any], force: bool) -> tuple[Path, Path]:
    target = output_dir.expanduser().absolute()
    if target.is_symlink():
        raise IntakeError("Ausgabeverzeichnis darf kein symbolischer Link sein")
    expected_names = {"aktenstart-manifest.json", "aktenstart-startkarte.md"}
    target_identity: tuple[int, int, int, int, int] | None = None
    if target.exists():
        if not target.is_dir():
            raise IntakeError("Ausgabeziel muss ein Verzeichnis sein")
        _validate_bundle_entries(target, expected_names)
        if not force:
            raise IntakeError(f"Ausgabeverzeichnis existiert bereits; --force erforderlich: {target}")
        target_identity = _identity(target.lstat())
    target.parent.mkdir(parents=True, exist_ok=True)
    json_bytes = (json.dumps(manifest, ensure_ascii=False, allow_nan=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    markdown_bytes = render_markdown(manifest).encode("utf-8")
    stage = Path(tempfile.mkdtemp(prefix=f".{target.name}-stage-", dir=target.parent))
    backup: Path | None = None
    try:
        _atomic_write(stage / "aktenstart-manifest.json", json_bytes, False)
        _atomic_write(stage / "aktenstart-startkarte.md", markdown_bytes, False)
        if target.exists():
            if target_identity != _identity(target.lstat()):
                raise IntakeError("Ausgabeverzeichnis wurde während des Laufs verändert")
            _validate_bundle_entries(target, expected_names)
            backup = Path(tempfile.mkdtemp(prefix=f".{target.name}-backup-", dir=target.parent))
            backup.rmdir()
            target.rename(backup)
            if target_identity[:2] != _identity(backup.lstat())[:2]:
                backup.rename(target)
                raise IntakeError("Ausgabeverzeichnis wurde unmittelbar vor Veröffentlichung ausgetauscht")
            try:
                _validate_bundle_entries(backup, expected_names)
            except (OSError, IntakeError):
                backup.rename(target)
                raise
        try:
            stage.rename(target)
        except OSError:
            if backup is not None and backup.exists() and not target.exists():
                backup.rename(target)
            raise
        if backup is not None:
            _remove_bundle_backup(backup, expected_names)
        return target / "aktenstart-manifest.json", target / "aktenstart-startkarte.md"
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def _canonical_ascii_integer(value: str) -> int:
    if re.fullmatch(r"[1-9][0-9]*", value) is None:
        raise argparse.ArgumentTypeError("kanonische positive ASCII-Ganzzahl erwartet")
    parsed = int(value)
    return parsed


def positive_int(value: str) -> int:
    parsed = _canonical_ascii_integer(value)
    if not 1 <= parsed <= 16:
        raise argparse.ArgumentTypeError("Wert muss zwischen 1 und 16 liegen")
    return parsed


def max_mib(value: str) -> int:
    parsed = _canonical_ascii_integer(value)
    if not 1 <= parsed <= 1024:
        raise argparse.ArgumentTypeError("Wert muss zwischen 1 und 1024 MiB liegen")
    return parsed * 1024 * 1024


def max_gib(value: str) -> int:
    parsed = _canonical_ascii_integer(value)
    if not 1 <= parsed <= 1024:
        raise argparse.ArgumentTypeError("Wert muss zwischen 1 und 1024 GiB liegen")
    return parsed * 1024 * 1024 * 1024


def selftest() -> None:
    assert normalized_token("Käufer-Vertrag.pdf") == "kaeufer_vertrag_pdf"
    assert classify_name("01_Kaufvertrag.pdf", ".pdf") == "kauf_erwerb"
    assert classify_name("Zulassungsbescheinigung_Teil_I.pdf", ".pdf") == "fahrzeugpapiere"
    assert detect_type(b"%PDF-1.7\n", None, ".pdf") == "pdf"
    assert detect_type(b"MZ" + b"\0" * 20, None, ".pdf") == "windows_executable"
    assert "\\|" in markdown_cell("a|b") and "&#96;" in markdown_cell("`x`")
    with tempfile.TemporaryDirectory() as raw:
        root = Path(raw) / "akte"
        root.mkdir()
        (root / "Kaufvertrag.txt").write_text("Kaufpreis 20.000 EUR", encoding="utf-8")
        (root / "Fahrzeugschein.txt").write_text("FIN anonymisiert", encoding="utf-8")
        first = build_manifest(root, jobs=1)
        second = build_manifest(root, jobs=2)
        assert first == second
        assert first["summary"]["status"] == "STARTBEREIT"
        assert first["routing"]["next_skill"] == "01-kaltstart-aktenaufnahme"
        assert str(root) not in json.dumps(first, ensure_ascii=False)
        rendered = render_markdown(first)
        assert "## Übergabe in den Arbeitschat" in rendered
        assert QUICKSTART_REQUEST in rendered
        (root / "Kaufvertrag_Kopie.txt").write_text("Kaufpreis 20.000 EUR", encoding="utf-8")
        duplicate = build_manifest(root, jobs=2)
        assert duplicate["summary"]["duplicate_groups"] == 1
        (root / "falsch.pdf").write_text("kein pdf", encoding="utf-8")
        blocked = build_manifest(root, jobs=1)
        assert blocked["summary"]["status"] == "BLOCKIERT"
        assert any(issue["code"] == "endung_signatur_widerspruch" for issue in blocked["issues"])
    print("diesel-aktenstart selftest OK (deterministisch, pfadsparsam, signatur-, dubletten- und übergabefest)")


def main() -> int:
    raw_arguments = sys.argv[1:]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, help="Aktenordner")
    parser.add_argument("--output-dir", type=Path, help="schreibt JSON-Manifest und kompakte Startkarte")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="stdout-Format ohne --output-dir")
    parser.add_argument("--jobs", type=positive_int, default=min(8, max(2, os.cpu_count() or 2)))
    parser.add_argument("--max-file-mib", type=max_mib, default=DEFAULT_MAX_FILE_BYTES, metavar="MIB")
    parser.add_argument("--max-total-gib", type=max_gib, default=DEFAULT_MAX_TOTAL_BYTES, metavar="GIB")
    parser.add_argument("--force", action="store_true", help="vorhandene reguläre Bundle-Dateien atomar ersetzen")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--_pdf-probe", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args._pdf_probe:
        if raw_arguments != ["--_pdf-probe"]:
            parser.error("interner PDF-Prüfmodus akzeptiert keine weiteren Argumente")
        return _pdf_probe_worker()
    if args.selftest:
        if raw_arguments != ["--selftest"]:
            parser.error("--selftest akzeptiert keine weiteren Argumente")
        selftest()
        return 0
    if args.root is None:
        parser.error("Aktenordner fehlt")
    if args.force and args.output_dir is None:
        parser.error("--force erfordert --output-dir")
    format_supplied = any(argument == "--format" or argument.startswith("--format=") for argument in raw_arguments)
    if args.output_dir is not None and format_supplied:
        parser.error("--format gilt nur für stdout ohne --output-dir")
    try:
        root = args.root.expanduser().absolute()
        excluded = None
        if args.output_dir is not None:
            excluded = args.output_dir.expanduser().absolute()
            if excluded == root:
                raise IntakeError("Ausgabeverzeichnis darf nicht die Aktenwurzel selbst sein")
            if excluded.is_symlink():
                raise IntakeError("Ausgabeverzeichnis darf kein symbolischer Link sein")
        manifest = build_manifest(root, excluded=excluded, jobs=args.jobs, max_file_bytes=args.max_file_mib, max_total_bytes=args.max_total_gib)
        if args.output_dir is not None:
            json_path, markdown_path = write_bundle(args.output_dir, manifest, args.force)
            print(f"{manifest['summary']['status']}: {manifest['summary']['regular_files']} Dateien; Bundle {json_path.name} + {markdown_path.name}")
        elif args.format == "json":
            print(json.dumps(manifest, ensure_ascii=False, allow_nan=False, sort_keys=True, indent=2))
        else:
            print(render_markdown(manifest), end="")
    except (OSError, IntakeError, ValueError) as exc:
        print(f"diesel-aktenstart: {exc}", file=sys.stderr)
        return 1
    return 0 if manifest["summary"]["status"] == "STARTBEREIT" else 2


if __name__ == "__main__":
    raise SystemExit(main())

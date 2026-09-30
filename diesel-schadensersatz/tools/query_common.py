#!/usr/bin/env python3
"""Shared defensive helpers for the standalone corpus query tools."""

from __future__ import annotations

import argparse
import html
import ipaddress
import json
import math
import os
import re
import stat
import sys
import unicodedata
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from bgh_sources import is_canonical_bgh_pdf_url


MAX_CORPUS_BYTES = 64 * 1024 * 1024
MAX_QUERY_CHARS = 240
MAX_QUERY_TERMS = 16
_FORMULA_PREFIXES = ("=", "+", "-", "@")
_FORMULA_IGNORABLE = "\ufeff\u200b\u200c\u200d\u2060"
_UMLAUTS = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue"})
_UNSAFE_URL_RE = re.compile(r'[\x00-\x20\x7f<>\\{}^`|\"]')
_UNSAFE_DECODED_URL_RE = re.compile(r'[\x00-\x1f\x7f<>\\{}^`|\"]')
_CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_BAD_PERCENT_RE = re.compile(r"%(?![0-9A-Fa-f]{2})")
_MAX_URL_CHARS = 4096
_MAX_URL_DECODE_PASSES = 16
_CANONICAL_UNSIGNED_INT_RE = re.compile(r"(?:0|[1-9][0-9]*)")


def _unsafe_unicode_character(character: str) -> bool:
    category = unicodedata.category(character)
    return category.startswith("C") or category in {"Zl", "Zp"}


def _read_bounded_regular_file(path: Path, maximum: int) -> bytes:
    requested = path.expanduser().absolute()
    before = requested.lstat()
    if stat.S_ISLNK(before.st_mode) or not stat.S_ISREG(before.st_mode):
        raise ValueError("Korpus muss eine reguläre Datei ohne symbolischen Link sein")
    if before.st_size > maximum:
        raise ValueError(f"Korpus überschreitet {maximum} Bytes")
    descriptor = os.open(requested, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        opened = os.fstat(descriptor)
        if (opened.st_dev, opened.st_ino) != (before.st_dev, before.st_ino):
            raise ValueError("Korpus wurde vor dem Lesen ausgetauscht")
        chunks: list[bytes] = []
        size = 0
        with os.fdopen(descriptor, "rb", closefd=False) as handle:
            while True:
                chunk = handle.read(min(1024 * 1024, maximum + 1 - size))
                if not chunk:
                    break
                chunks.append(chunk)
                size += len(chunk)
                if size > maximum:
                    raise ValueError(f"Korpus überschreitet {maximum} Bytes")
        after = requested.lstat()
        opened_after = os.fstat(descriptor)
        before_identity = (
            before.st_dev,
            before.st_ino,
            before.st_size,
            before.st_mtime_ns,
            before.st_ctime_ns,
        )
        opened_identity = (
            opened.st_dev,
            opened.st_ino,
            opened.st_size,
            opened.st_mtime_ns,
            opened.st_ctime_ns,
        )
        opened_after_identity = (
            opened_after.st_dev,
            opened_after.st_ino,
            opened_after.st_size,
            opened_after.st_mtime_ns,
            opened_after.st_ctime_ns,
        )
        after_identity = (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mtime_ns,
            after.st_ctime_ns,
        )
        if (
            before_identity != opened_identity
            or opened_identity != opened_after_identity
            or before_identity != after_identity
            or opened_after.st_size != size
        ):
            raise ValueError("Korpus wurde während des Lesens verändert")
        return b"".join(chunks)
    finally:
        os.close(descriptor)


def _reject_constant(value: str) -> None:
    raise ValueError(f"nicht endliche JSON-Zahl: {value}")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"doppelter JSON-Schlüssel: {key}")
        result[key] = value
    return result


def load_json_object(path: Path) -> dict[str, Any]:
    try:
        raw = _read_bounded_regular_file(path, MAX_CORPUS_BYTES)
        text = raw.decode("utf-8")
        data = json.loads(
            text,
            parse_constant=_reject_constant,
            object_pairs_hook=_unique_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError) as exc:
        raise ValueError(f"Korpus konnte nicht geladen werden: {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"Korpuswurzel muss ein Objekt sein: {path}")
    return data


def normalize_search(value: Any) -> str:
    if isinstance(value, dict):
        value = " ".join(f"{key} {normalize_search(item)}" for key, item in value.items())
    elif isinstance(value, set):
        value = " ".join(normalize_search(item) for item in sorted(value, key=str))
    elif isinstance(value, (list, tuple)):
        value = " ".join(normalize_search(item) for item in value)
    elif value is None:
        value = ""
    text = unicodedata.normalize("NFKC", str(value)).casefold().translate(_UMLAUTS)
    return " ".join(text.split())


def contains_terms(value: Any, query: str | None) -> bool:
    if query is None:
        return True
    terms = normalize_search(query).split()
    if not terms:
        return True
    haystack = normalize_search(value)
    return all(term in haystack for term in terms)


def parse_canonical_int(
    value: str,
    *,
    label: str,
    minimum: int,
    maximum: int,
) -> int:
    """Parse one bounded, canonical ASCII integer for command-line use."""
    if not isinstance(value, str) or _CANONICAL_UNSIGNED_INT_RE.fullmatch(value) is None:
        raise argparse.ArgumentTypeError(
            f"{label} muss eine kanonische ASCII-Ganzzahl ohne Vorzeichen oder führende Null sein"
        )
    parsed = int(value)
    if not minimum <= parsed <= maximum:
        raise argparse.ArgumentTypeError(
            f"{label} muss zwischen {minimum} und {maximum} liegen"
        )
    return parsed


def parse_year(value: str) -> int:
    return parse_canonical_int(
        value,
        label="Jahr",
        minimum=1900,
        maximum=2100,
    )


def parse_result_limit(value: str) -> int:
    return parse_canonical_int(
        value,
        label="Limit",
        minimum=0,
        maximum=1000,
    )


def parse_query_text(value: str) -> str:
    """Reject oversized, invisible or needlessly broad CLI search values."""
    if not isinstance(value, str) or not value:
        raise argparse.ArgumentTypeError("Suchfilter darf nicht leer sein")
    if value != value.strip():
        raise argparse.ArgumentTypeError(
            "Suchfilter darf keine führenden oder nachgestellten Leerzeichen enthalten"
        )
    if len(value) > MAX_QUERY_CHARS:
        raise argparse.ArgumentTypeError(
            f"Suchfilter darf höchstens {MAX_QUERY_CHARS} Zeichen enthalten"
        )
    if _CONTROL_RE.search(value) or any(_unsafe_unicode_character(char) for char in value):
        raise argparse.ArgumentTypeError("Suchfilter enthält ein unsicheres Steuer-/Formatzeichen")
    terms = normalize_search(value).split()
    if not terms:
        raise argparse.ArgumentTypeError("Suchfilter enthält keinen auswertbaren Begriff")
    if len(terms) > MAX_QUERY_TERMS:
        raise argparse.ArgumentTypeError(
            f"Suchfilter darf höchstens {MAX_QUERY_TERMS} Begriffe enthalten"
        )
    return value


def write_stdout(value: str) -> None:
    """Write one normalized trailing newline and exit quietly on a closed pipe."""
    rendered = value.rstrip("\n") + "\n"
    try:
        sys.stdout.write(rendered)
        sys.stdout.flush()
    except BrokenPipeError as exc:
        try:
            null_fd = os.open(os.devnull, os.O_WRONLY)
            try:
                os.dup2(null_fd, sys.stdout.fileno())
            finally:
                os.close(null_fd)
        except (AttributeError, OSError, ValueError):
            pass
        raise SystemExit(0) from exc


def iso_year(value: Any) -> int:
    return parse_iso_date(value).year


def parse_iso_date(value: Any) -> date:
    if not isinstance(value, str):
        raise ValueError(f"ungültiges ISO-Datum: {value!r}")
    text = value
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text) is None:
        raise ValueError(f"ungültiges ISO-Datum: {value!r}")
    try:
        parsed = date.fromisoformat(text)
    except ValueError:
        raise ValueError(f"ungültiges ISO-Datum: {value!r}")
    return parsed


def validate_collection_date(value: Any, *, label: str = "stand") -> date:
    parsed = parse_iso_date(value)
    if parsed > date.today():
        raise ValueError(f"{label} liegt in der Zukunft: {value!r}")
    return parsed


def require_exact_fields(record: dict[str, Any], expected: set[str], label: str) -> None:
    actual = set(record)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ValueError(f"{label}: Feldabweichung fehlt={missing}, extra={extra}")


def require_text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} muss nichtleeren Text enthalten")
    if value != value.strip():
        raise ValueError(f"{label} darf keine äußeren Leerzeichen enthalten")
    if _CONTROL_RE.search(value) or any(_unsafe_unicode_character(char) for char in value):
        raise ValueError(f"{label} enthält ein unsicheres Steuer-/Formatzeichen")
    return value


def require_optional_text(value: Any, label: str) -> None:
    if value is not None:
        require_text(value, label)


def require_unique_text_list(value: Any, label: str, *, allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list) or (not allow_empty and not value):
        raise ValueError(f"{label} muss eine nichtleere Textliste sein")
    for index, item in enumerate(value):
        require_text(item, f"{label}[{index}]")
    normalized = [normalize_search(item) for item in value]
    if len(normalized) != len(set(normalized)):
        raise ValueError(f"{label} enthält normalisierte Dubletten")
    return value


def require_nonnegative_number(value: Any, label: str, *, optional: bool = True) -> None:
    if value is None and optional:
        return
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} muss eine nichtnegative Zahl sein")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"{label} muss endlich sein")
    if value < 0:
        raise ValueError(f"{label} darf nicht negativ sein")


def require_canonical_bgh_source(level: Any, docket: Any, url: Any, label: str) -> None:
    if level == "BGH" and not is_canonical_bgh_pdf_url(docket, url):
        raise ValueError(f"{label}: BGH-Quelle passt nicht kanonisch zum Aktenzeichen")


def validate_year_range(year_from: int | None, year_to: int | None) -> None:
    for label, value in (("--jahr-von", year_from), ("--jahr-bis", year_to)):
        if value is not None and not 1900 <= value <= 2100:
            raise ValueError(f"{label} muss zwischen 1900 und 2100 liegen")
    if year_from is not None and year_to is not None and year_from > year_to:
        raise ValueError("--jahr-von darf nicht nach --jahr-bis liegen")


def safe_tsv_cell(value: Any) -> str:
    raw = str(value if value is not None else "")
    text = "".join(" " if _unsafe_unicode_character(char) else char for char in raw)
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    text = " ".join(text.split())
    probe = unicodedata.normalize("NFKC", text)
    previous = None
    while probe != previous:
        previous = probe
        probe = probe.lstrip().lstrip(_FORMULA_IGNORABLE)
    if probe.startswith(_FORMULA_PREFIXES):
        text = "'" + text
    return text


def markdown_cell(value: Any) -> str:
    text = str(value if value is not None else "-")
    text = "".join(" " if _unsafe_unicode_character(char) else char for char in text)
    text = _CONTROL_RE.sub(" ", text).replace("\t", " ").replace("\r", " ").replace("\n", " ")
    text = html.escape(" ".join(text.split()), quote=False)
    return text.replace("\\", "\\\\").replace("|", "\\|")


def markdown_code(value: Any) -> str:
    return markdown_cell(value).replace("`", "&#96;")


def markdown_url(value: Any) -> str | None:
    if not is_https_url(value):
        return None
    from urllib.parse import quote

    return quote(str(value), safe="%/:?&=#+,;@!$*-._~")


def is_https_url(value: Any) -> bool:
    if (
        not isinstance(value, str)
        or not value
        or len(value) > _MAX_URL_CHARS
        or value != value.strip()
        or _UNSAFE_URL_RE.search(value)
        or _BAD_PERCENT_RE.search(value)
        or any(_unsafe_unicode_character(char) for char in value)
    ):
        return False
    decoded = value
    for _ in range(_MAX_URL_DECODE_PASSES):
        try:
            candidate = unquote(decoded, errors="strict")
        except UnicodeError:
            return False
        if candidate == decoded:
            break
        decoded = candidate
    else:
        return False
    if _UNSAFE_DECODED_URL_RE.search(decoded) or any(
        _unsafe_unicode_character(char) for char in decoded
    ):
        return False
    try:
        parsed = urlparse(value)
        hostname = parsed.hostname
        port = parsed.port
    except ValueError:
        return False
    if (
        parsed.scheme != "https"
        or not hostname
        or not hostname.isascii()
        or hostname.startswith(".")
        or hostname.endswith(".")
        or parsed.username is not None
        or parsed.password is not None
        or "%" in hostname
        or port == 0
    ):
        return False
    try:
        ipaddress.ip_address(hostname)
    except ValueError:
        try:
            ascii_hostname = hostname.encode("idna").decode("ascii")
        except UnicodeError:
            return False
        labels = ascii_hostname.split(".")
        if any(
            not label
            or len(label) > 63
            or re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?", label) is None
            for label in labels
        ):
            return False
    except UnicodeError:
        return False
    return True

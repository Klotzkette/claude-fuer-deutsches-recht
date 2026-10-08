#!/usr/bin/env python3
"""Prueft Nummerierung, Verlinkung und zentrale Falllogik der Testakten."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = REPO_ROOT / "testakten"
SKIP_DIRS = {"formatvorlagen-paradebeispiele", "megaprompts"}
SOURCE_RE = re.compile(r"^(?P<number>\d{2})_.+\.md$")
META_RE = re.compile(r"<!--\s*aktenmeta(?P<body>.*?)-->", re.S)
META_LINE_RE = re.compile(r"^(?P<key>[^:\n]+):\s*(?P<value>.+?)\s*$", re.M)
DATE_RE = re.compile(r"\b(\d{2}\.\d{2}\.\d{4})\b")
EARLIEST_AWARD_RE = re.compile(
    r"(?:nicht\s+vor(?:\s+dem)?|fruehestens\s+am)\s+(\d{2}\.\d{2}\.\d{4})",
    re.I,
)
GAEB_POSITION_RE = re.compile(r"\b\d{2}\.\d{2}\.\d{3}\b")
SYNTHETIC_TITLE_RE = re.compile(r"^#\s+(?:aktenstueck\s+)?\d{2}(?:\s*[-:])?\s+", re.I)
META_MARKERS = (
    "fuer uebungszwecke",
    "testakte",
    "lernziel",
    "arbeitsauftrag",
    "beschwerdeskizze",
    "diese mitteilung ersetzt keine rechtsberatung",
)
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[(?:hier\s+)?(?:eintragen|erg[aä]nzen)\]", re.I)


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(REPO_ROOT)}: {message}")


def parse_date(value: str, path: Path, errors: list[str]) -> datetime | None:
    try:
        return datetime.strptime(value, "%d.%m.%Y")
    except ValueError:
        fail(errors, path, f"ungueltiges Datum {value!r}")
        return None


def metadata(text: str) -> dict[str, str]:
    match = META_RE.search(text)
    if not match:
        return {}
    return {
        item.group("key").strip(): item.group("value").strip()
        for item in META_LINE_RE.finditer(match.group("body"))
    }


def validate_numbering_and_readme(
    case_dir: Path,
    sources: list[Path],
    errors: list[str],
) -> None:
    numbers = [int(SOURCE_RE.fullmatch(path.name).group("number")) for path in sources]  # type: ignore[union-attr]
    expected = list(range(1, max(numbers) + 1))
    if numbers != expected:
        fail(errors, case_dir, f"Aktenstuecke nicht lueckenlos nummeriert: {numbers}; erwartet {expected}")

    readme = case_dir / "README.md"
    if not readme.is_file():
        fail(errors, case_dir, "README.md fehlt")
        return
    readme_text = readme.read_text(encoding="utf-8")
    for source in sources:
        if source.name not in readme_text:
            fail(errors, readme, f"{source.name} ist nicht verlinkt")


def validate_document_shape(path: Path, text: str, errors: list[str]) -> None:
    headings = [line for line in text.splitlines() if line.startswith("# ")]
    if len(headings) != 1:
        fail(errors, path, f"genau eine H1-Ueberschrift erwartet, gefunden: {len(headings)}")
    else:
        heading_folded = (
            headings[0].casefold().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
        )
        if SYNTHETIC_TITLE_RE.match(heading_folded):
            fail(errors, path, "synthetische Nummerierung in der Dokumentueberschrift")

    folded = (
        text.casefold()
        .replace("ä", "ae")
        .replace("ö", "oe")
        .replace("ü", "ue")
        .replace("ß", "ss")
    )
    for marker in META_MARKERS:
        if marker in folded:
            fail(errors, path, f"didaktischer oder interner Marker {marker!r} im Aktenstueck")
    placeholder = PLACEHOLDER_RE.search(text)
    if placeholder:
        fail(errors, path, f"offener Platzhalter {placeholder.group(0)!r}")


def validate_section_134(
    path: Path,
    text: str,
    meta: dict[str, str],
    errors: list[str],
) -> tuple[datetime, datetime] | None:
    if meta.get("Dokumenttyp") != "Informationsschreiben nach \u00a7 134 GWB":
        return None
    if not re.search(r"Zuschlag.{0,120}auf\s+das\s+Angebot\s+der", text, re.I | re.S):
        fail(errors, path, "\u00a7-134-Pflichtinhalt fehlt: erfolgreiche Bieterin")
    if "gr\u00fcnde" not in text.casefold():
        fail(errors, path, "\u00a7-134-Pflichtinhalt fehlt: Gruende")

    sent_value = meta.get("Datum")
    if not sent_value:
        fail(errors, path, "Versanddatum im Aktenmetablock fehlt")
        return None
    sent = parse_date(sent_value, path, errors)
    award_match = EARLIEST_AWARD_RE.search(
        text.replace("\u00fc", "ue").replace("\u00fch", "ueh")
    )
    if not award_match:
        fail(errors, path, "ausdrueckliches fruehestes Zuschlagsdatum fehlt")
        return None
    award = parse_date(award_match.group(1), path, errors)
    if sent is None or award is None:
        return None
    if (award.date() - sent.date()).days < 11:
        fail(errors, path, "elektronische Wartefrist unterschreitet zehn volle Kalendertage")
    return sent, award


def validate_review_timing(
    case_dir: Path,
    dated_sources: list[tuple[Path, datetime, str]],
    notices: list[tuple[Path, datetime, datetime]],
    errors: list[str],
) -> None:
    applications = [
        (path, date)
        for path, date, document_type in dated_sources
        if document_type == "Nachpr\u00fcfungsantrag"
    ]
    for application_path, application_date in applications:
        prior = [notice for notice in notices if notice[1] <= application_date]
        if not prior:
            continue
        notice_path, _, earliest_award = max(prior, key=lambda notice: notice[1])
        if application_date >= earliest_award:
            fail(
                errors,
                application_path,
                f"Antrag liegt nicht vor dem in {notice_path.name} genannten fruehesten Zuschlag",
            )

    if any("sofortige_beschwerde" in path.name for path, _, _ in dated_sources):
        if not any("beschluss_vk" in path.name for path, _, _ in dated_sources):
            fail(errors, case_dir, "sofortige Beschwerde ohne vorgelagerten VK-Beschluss")


def validate_gaeb_positions(case_dir: Path, sources: list[Path], errors: list[str]) -> None:
    gaeb_file = case_dir / "gaeb" / "lv_stadthalle_x83.xml"
    if not gaeb_file.is_file():
        return
    try:
        root = ET.parse(gaeb_file).getroot()
    except ET.ParseError as exc:
        fail(errors, gaeb_file, f"ungueltiges XML: {exc}")
        return

    gaeb_positions = {
        value
        for element in root.iter()
        if element.tag.rsplit("}", 1)[-1] == "Item"
        for value in [element.attrib.get("no")]
        if value
    }
    referenced = {
        match.group(0)
        for source in sources
        for match in GAEB_POSITION_RE.finditer(source.read_text(encoding="utf-8"))
    }
    unknown = sorted(referenced - gaeb_positions)
    if unknown:
        fail(errors, gaeb_file, f"Markdown verweist auf unbekannte GAEB-Positionen: {unknown}")


def validate_review_jurisdiction(case_dir: Path, sources: list[Path], errors: list[str]) -> None:
    combined = "\n".join(source.read_text(encoding="utf-8") for source in sources)
    if "Oberlandesgericht Westfalen" in combined:
        fail(errors, case_dir, "nicht existentes Beschwerdegericht Oberlandesgericht Westfalen")
    if (
        "Vergabekammer Westfalen" in combined
        and any("sofortige_beschwerde" in source.name for source in sources)
        and "Oberlandesgericht Düsseldorf" not in combined
    ):
        fail(
            errors,
            case_dir,
            "Beschwerde gegen die Vergabekammer Westfalen nicht dem OLG Düsseldorf zugeordnet",
        )


def validate_case(case_dir: Path, errors: list[str]) -> int:
    sources = sorted(
        (
            path
            for path in case_dir.iterdir()
            if path.is_file() and SOURCE_RE.fullmatch(path.name)
        ),
        key=lambda path: int(path.name[:2]),
    )
    if not sources:
        fail(errors, case_dir, "keine nummerierten Aktenstuecke gefunden")
        return 0

    validate_numbering_and_readme(case_dir, sources, errors)
    notices: list[tuple[Path, datetime, datetime]] = []
    dated_sources: list[tuple[Path, datetime, str]] = []
    for source in sources:
        text = source.read_text(encoding="utf-8")
        validate_document_shape(source, text, errors)
        meta = metadata(text)
        date_value = meta.get("Datum")
        if date_value:
            date = parse_date(date_value, source, errors)
            if date:
                dated_sources.append((source, date, meta.get("Dokumenttyp", "")))
        notice = validate_section_134(source, text, meta, errors)
        if notice:
            notices.append((source, notice[0], notice[1]))

    validate_review_timing(case_dir, dated_sources, notices, errors)
    validate_gaeb_positions(case_dir, sources, errors)
    validate_review_jurisdiction(case_dir, sources, errors)
    return len(sources)


def main() -> int:
    errors: list[str] = []
    case_dirs = sorted(
        path for path in TESTAKTEN.iterdir() if path.is_dir() and path.name not in SKIP_DIRS
    )
    document_count = sum(validate_case(case_dir, errors) for case_dir in case_dirs)
    if errors:
        print(f"validate-testakten-falllogik failed ({len(errors)} Fehler):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"validate-testakten-falllogik OK "
        f"({len(case_dirs)} Testakten, {document_count} Aktenstuecke)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

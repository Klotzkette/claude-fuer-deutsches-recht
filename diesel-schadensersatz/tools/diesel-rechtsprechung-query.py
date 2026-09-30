#!/usr/bin/env python3
"""Filter the curated EuGH/BGH/OLG/KG diesel case-law matrix."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from query_common import (
    contains_terms,
    is_https_url,
    iso_year,
    load_json_object,
    markdown_cell,
    markdown_code,
    markdown_url,
    normalize_search,
    parse_iso_date,
    parse_query_text,
    parse_result_limit,
    parse_year,
    require_canonical_bgh_source,
    require_exact_fields,
    require_nonnegative_number,
    require_optional_text,
    require_text,
    require_unique_text_list,
    safe_tsv_cell,
    validate_collection_date,
    validate_year_range,
    write_stdout,
)


TOOL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = TOOL_ROOT / "references" / "diesel-rechtsprechung-obergerichte.json"
LEVELS = ("EuGH", "GA", "BGH", "OLG/KG")
EXPECTED_ROOT_FIELDS = {
    "schema",
    "stand",
    "titel",
    "hinweis",
    "umfang",
    "quellenregeln",
    "olg_kg_abdeckung",
    "entscheidungen",
}
EXPECTED_FIELDS = {
    "id",
    "datum",
    "ebene",
    "gericht",
    "entscheidungsart",
    "az",
    "themen",
    "fallgruppen",
    "status",
    "richtung",
    "quelle_art",
    "quelle_url",
    "kernaussage",
    "arbeitsregel",
    "betrag_eur",
    "ecli",
    "folgestatus",
    "geprueft_am",
}
ALLOWED_DIRECTIONS = {"verbraucherfreundlich", "herstellerfreundlich", "gemischt", "neutral_prozessual"}
ALLOWED_STATUS = {
    "aufgegeben",
    "gegenstandslos",
    "gestrichen",
    "historisch",
    "hoechstrichterlich",
    "instanzrechtsprechung",
    "nicht_bindend",
    "qualifizierungsbeduerftig",
    "teilweise_ueberholt",
}
ALLOWED_SOURCE_TYPES = {
    "amtlich_bgh",
    "amtlich_eu",
    "freie_fundstellenvernetzung",
    "freie_volltextkopie",
    "kanzlei_nutzermaterial",
    "landesrecht",
}
ALLOWED_DECISION_TYPES = {
    "Beschluss",
    "Erledigungsbeschluss",
    "Schlussanträge",
    "Streichungsbeschluss",
    "Urteil",
}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Durchsucht die kuratierte Diesel-Rechtsprechungsmatrix."
    )
    result.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    result.add_argument("--query", type=parse_query_text, help="Volltextsuche über alle Felder")
    result.add_argument("--ebene", choices=LEVELS)
    result.add_argument("--gericht", type=parse_query_text, help="Teilstring des Gerichtsnamens")
    result.add_argument("--az", type=parse_query_text, help="Teilstring des Aktenzeichens")
    result.add_argument("--thema", type=parse_query_text, help="Teilstring in Themen oder Fallgruppen")
    result.add_argument(
        "--status",
        choices=tuple(sorted(ALLOWED_STATUS | {"bindend"})),
        help="Exakter Status, z. B. hoechstrichterlich oder gestrichen; bindend bleibt Alias",
    )
    result.add_argument(
        "--richtung",
        choices=(
            "verbraucherfreundlich",
            "herstellerfreundlich",
            "gemischt",
            "neutral_prozessual",
        ),
    )
    result.add_argument("--quelle", choices=tuple(sorted(ALLOWED_SOURCE_TYPES)), help="Exakte Quellenart")
    result.add_argument("--jahr-von", type=parse_year)
    result.add_argument("--jahr-bis", type=parse_year)
    result.add_argument("--limit", type=parse_result_limit, default=25, help="0 = alle Treffer")
    result.add_argument("--format", choices=("markdown", "json", "tsv"), default="markdown")
    result.add_argument("--stats", action="store_true", help="Nur Verteilungsstatistik ausgeben")
    result.add_argument("--selftest", action="store_true")
    return result


def load_corpus(path: Path) -> dict[str, Any]:
    try:
        data = load_json_object(path)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if data.get("schema") != "dieselgate.obergerichte.v1":
        raise SystemExit(f"Unerwartetes Schema in {path}: {data.get('schema')!r}")
    try:
        require_exact_fields(data, EXPECTED_ROOT_FIELDS, "Korpuswurzel")
        stand = validate_collection_date(data.get("stand"))
    except ValueError as exc:
        raise SystemExit(f"Ungültiger Korpus in {path}: {exc}") from exc
    rows = data.get("entscheidungen")
    if not isinstance(rows, list):
        raise SystemExit(f"Ungültiger Korpus in {path}: entscheidungen fehlt")
    ids: set[str] = set()
    identities: set[tuple[str, str, str, str]] = set()
    for index, item in enumerate(rows, start=1):
        label = f"Datensatz {index}"
        if not isinstance(item, dict):
            raise SystemExit(f"Ungültiger Korpus in {path}: {label} ist kein Objekt")
        try:
            require_exact_fields(item, EXPECTED_FIELDS, label)
            decision_date = parse_iso_date(item["datum"])
            if decision_date > stand:
                raise ValueError(f"{label}.datum liegt nach dem Korpusstand")
            checked_date = parse_iso_date(item["geprueft_am"])
            if checked_date < decision_date or checked_date > stand:
                raise ValueError(f"{label}.geprueft_am liegt außerhalb Entscheidung/Korpusstand")
            for field in (
                "id",
                "ebene",
                "gericht",
                "entscheidungsart",
                "az",
                "status",
                "richtung",
                "quelle_art",
                "kernaussage",
                "arbeitsregel",
                "quelle_url",
            ):
                require_text(item[field], f"{label}.{field}")
            require_optional_text(item["ecli"], f"{label}.ecli")
            require_optional_text(item["folgestatus"], f"{label}.folgestatus")
            require_unique_text_list(item["themen"], f"{label}.themen")
            require_unique_text_list(item["fallgruppen"], f"{label}.fallgruppen")
            require_nonnegative_number(item["betrag_eur"], f"{label}.betrag_eur")
            require_canonical_bgh_source(item["ebene"], item["az"], item["quelle_url"], label)
        except ValueError as exc:
            raise SystemExit(f"Ungültiger Korpus in {path}: {exc}") from exc
        if item["ebene"] not in LEVELS:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label} hat unbekannte Ebene")
        if item["id"] in ids:
            raise SystemExit(f"Ungültiger Korpus in {path}: doppelte ID {item['id']!r}")
        ids.add(item["id"])
        identity = (item["ebene"], item["gericht"], item["datum"], item["az"])
        if identity in identities:
            raise SystemExit(f"Ungültiger Korpus in {path}: doppelte Entscheidungsidentität {identity!r}")
        identities.add(identity)
        if item["richtung"] not in ALLOWED_DIRECTIONS:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: unbekannte Richtung")
        if item["status"] not in ALLOWED_STATUS:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: unbekannter Status")
        if item["quelle_art"] not in ALLOWED_SOURCE_TYPES:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: unbekannte Quellenart")
        if item["entscheidungsart"] not in ALLOWED_DECISION_TYPES:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: unbekannte Entscheidungsart")
        if not is_https_url(item["quelle_url"]):
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: Quelle ist keine HTTPS-URL")
    return data


def normalized(value: Any) -> str:
    return normalize_search(value)


def contains(value: Any, needle: str | None) -> bool:
    return contains_terms(value, needle)


def searchable_text(item: dict[str, Any]) -> str:
    return normalized([value for value in item.values() if value is not None])


def select(rows: Iterable[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    requested_status = "hoechstrichterlich" if args.status == "bindend" else args.status
    for item in rows:
        year = iso_year(item["datum"])
        if args.ebene and item["ebene"] != args.ebene:
            continue
        if not contains(item["gericht"], args.gericht):
            continue
        if not contains(item["az"], args.az):
            continue
        if args.thema and not contains(item["themen"] + item["fallgruppen"], args.thema):
            continue
        if requested_status and item["status"] != requested_status:
            continue
        if args.richtung and item["richtung"] != args.richtung:
            continue
        if args.quelle and item["quelle_art"] != args.quelle:
            continue
        if args.jahr_von is not None and year < args.jahr_von:
            continue
        if args.jahr_bis is not None and year > args.jahr_bis:
            continue
        if not contains_terms(searchable_text(item), args.query):
            continue
        selected.append(item)
    selected.sort(key=lambda item: (item["datum"], item["ebene"], item["gericht"], item["az"]), reverse=True)
    return selected


def format_markdown(
    rows: list[dict[str, Any]],
    stand: str,
    *,
    total: int | None = None,
) -> str:
    match_count = len(rows) if total is None else total
    truncated = len(rows) < match_count
    lines = [
        "# Diesel-Rechtsprechungsabfrage",
        "",
        f"Treffer: **{match_count}** | Ausgegeben: **{len(rows)}** | Korpusstand: **{stand}**",
        "",
        "> Status, Quellenart und Folgestatus sind Teil des Treffers. Kanzleiquellen und freie Vernetzungen vor Schriftsatzverwendung am Volltext verifizieren.",
        "",
    ]
    if truncated:
        lines.extend(
            [
                "> Ausgabe gekürzt. Mit `--limit 0` alle Treffer ausgeben.",
                "",
            ]
        )
    if not rows:
        lines.append("Keine Treffer. Filter eingrenzen oder Schreibweise prüfen.")
        return "\n".join(lines)
    lines.extend(
        [
            "| Datum | Ebene/Gericht | Az. | Status | Kernaussage | Quelle |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in rows:
        court = f"{markdown_cell(item['ebene'])} / {markdown_cell(item['gericht'])}"
        holding = markdown_cell(item["kernaussage"])
        follow = item.get("folgestatus")
        status = markdown_cell(item["status"] if not follow else f"{item['status']}; {follow}")
        source = f"[{markdown_cell(item['quelle_art'])}]({markdown_url(item['quelle_url'])})"
        lines.append(
            f"| {markdown_cell(item['datum'])} | {court} | `{markdown_code(item['az'])}` | {status} | {holding} | {source} |"
        )
    return "\n".join(lines)


def format_tsv(rows: list[dict[str, Any]]) -> str:
    fields = (
        "datum",
        "ebene",
        "gericht",
        "entscheidungsart",
        "az",
        "status",
        "richtung",
        "kernaussage",
        "arbeitsregel",
        "folgestatus",
        "quelle_art",
        "quelle_url",
    )
    lines = ["\t".join(fields)]
    for item in rows:
        lines.append("\t".join(safe_tsv_cell(item.get(field)) for field in fields))
    return "\n".join(lines)


def stats(rows: list[dict[str, Any]], stand: str) -> str:
    payload = {
        "stand": stand,
        "treffer": len(rows),
        "ebenen": dict(sorted(Counter(item["ebene"] for item in rows).items())),
        "status": dict(sorted(Counter(item["status"] for item in rows).items())),
        "richtungen": dict(sorted(Counter(item["richtung"] for item in rows).items())),
        "quellenarten": dict(sorted(Counter(item["quelle_art"] for item in rows).items())),
        "olg_kg_gerichte": len({item["gericht"] for item in rows if item["ebene"] == "OLG/KG"}),
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def selftest(data: dict[str, Any]) -> None:
    rows = data["entscheidungen"]
    assert len(rows) == 73
    assert Counter(item["ebene"] for item in rows) == Counter(
        {"EuGH": 11, "GA": 2, "BGH": 33, "OLG/KG": 27}
    )
    assert len({item["gericht"] for item in rows if item["ebene"] == "OLG/KG"}) == 24
    by_id = {item["id"]: item for item in rows}
    assert by_id["eugh-c667-c668-status"]["status"] == "gestrichen"
    assert by_id["eugh-c751-24-status"]["status"] == "gegenstandslos"
    assert by_id["bgh-via-zr87-24"]["entscheidungsart"] == "Beschluss"
    assert by_id["bgh-via-zr87-24"]["status"] == "hoechstrichterlich"
    assert "vollständig aufzehren" in by_id["bgh-via-zr87-24"]["kernaussage"]
    assert by_id["olg-naumburg-8u68-20"]["status"] == "aufgegeben"
    transliterated_args = parser().parse_args(["--query", "Zustaendigkeit"])
    assert select(rows, transliterated_args)
    legacy_status_args = parser().parse_args(["--status", "bindend"])
    assert select(rows, legacy_status_args)
    assert by_id["bgh-via-zr17-23"]["status"] == "hoechstrichterlich"
    assert by_id["bgh-via-zr1157-23"]["status"] == "hoechstrichterlich"
    print("diesel-rechtsprechung-query selftest OK (73 Datensätze, 24 OLG/KG-Gerichte)")


def main() -> int:
    argument_parser = parser()
    args = argument_parser.parse_args()
    try:
        validate_year_range(args.jahr_von, args.jahr_bis)
    except ValueError as exc:
        argument_parser.error(str(exc))
    data = load_corpus(args.corpus)
    if args.selftest:
        selftest(data)
        return 0
    rows = select(data["entscheidungen"], args)
    if args.stats:
        write_stdout(stats(rows, data["stand"]))
    else:
        shown = rows if args.limit == 0 else rows[: args.limit]
        if args.format == "json":
            write_stdout(json.dumps(shown, ensure_ascii=False, indent=2))
        elif args.format == "tsv":
            write_stdout(format_tsv(shown))
        else:
            write_stdout(format_markdown(shown, data["stand"], total=len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

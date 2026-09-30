#!/usr/bin/env python3
"""Filter the bundled EA288 case-law corpus without third-party packages."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.parse import urlparse

from query_common import (
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
    validate_collection_date,
    validate_year_range,
    write_stdout,
)


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
CORPUS_PATH = PLUGIN_ROOT / "references" / "ea288-rechtsprechung-instanzen.json"
SEARCH_FIELDS = (
    "typ",
    "spruchkoerper",
    "gericht",
    "az",
    "alias_az",
    "parteien",
    "vorlegendes_gericht",
    "modell",
    "motor",
    "norm",
    "abschalteinrichtung",
    "kernaussage",
)
LIVE_CHECK_NOTICE = (
    "Nutzermaterial: Gericht, Datum, Aktenzeichen, Tenor und tragende Passage vor "
    "Schriftsatzverwendung am Volltext oder in einer amtlichen Quelle live prüfen."
)
EXPECTED_ROOT_FIELDS = {"titel", "stand", "hinweis", "anzahl", "entscheidungen"}
EXPECTED_FIELDS = {
    "abschalteinrichtung",
    "alias_az",
    "az",
    "datum",
    "differenzschaden_eur",
    "ez",
    "gericht",
    "kernaussage",
    "modell",
    "motor",
    "norm",
    "parteien",
    "podcast_url",
    "quelle",
    "spruchkoerper",
    "typ",
    "volltext_url",
    "vorlegendes_gericht",
}
ALLOWED_TYPES = {"instanzentscheidung", "leitentscheidung", "schlussantrag_generalanwalt"}
COUNT_FIELDS = {
    "gesamt",
    "leitentscheidungen_eugh",
    "leitentscheidungen_bgh",
    "schlussantraege",
    "instanzentscheidungen",
}


def normalize(value: object) -> str:
    return normalize_search(value)


def parse_decimal(value: str) -> Decimal:
    normalized = value.strip().replace(" ", "").replace("\u00a0", "")
    german = re.fullmatch(r"([+-]?)(\d{1,3}(?:\.\d{3})+|\d+)(?:,(\d+))?", normalized)
    english = re.fullmatch(r"([+-]?)(\d{1,3}(?:,\d{3})+|\d+)(?:\.(\d+))?", normalized)
    plain = re.fullmatch(r"[+-]?\d+(?:[.,]\d+)?", normalized)
    if german and "." in normalized:
        sign, integer, fraction = german.groups()
        normalized = sign + integer.replace(".", "") + (f".{fraction}" if fraction else "")
    elif english and "," in normalized and (normalized.count(",") > 1 or "." in normalized):
        sign, integer, fraction = english.groups()
        normalized = sign + integer.replace(",", "") + (f".{fraction}" if fraction else "")
    elif plain:
        normalized = normalized.replace(",", ".")
    else:
        raise argparse.ArgumentTypeError(f"ungültiger Betrag: {value!r}")
    try:
        result = Decimal(normalized)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError(f"ungültiger Betrag: {value!r}") from exc
    if not result.is_finite():
        raise argparse.ArgumentTypeError(f"Betrag muss endlich sein: {value!r}")
    if result < 0:
        raise argparse.ArgumentTypeError(f"Betrag darf nicht negativ sein: {value!r}")
    return result


@dataclass
class Filters:
    queries: list[str] = field(default_factory=list)
    typ: str | None = None
    gericht: str | None = None
    az: str | None = None
    modell: str | None = None
    einrichtung: str | None = None
    norm: str | None = None
    jahr_von: int | None = None
    jahr_bis: int | None = None
    betrag_min: Decimal | None = None
    betrag_max: Decimal | None = None
    mit_volltext: bool = False


def load_corpus(path: Path = CORPUS_PATH) -> dict:
    try:
        corpus = load_json_object(path)
    except ValueError as exc:
        raise ValueError(f"Korpus nicht lesbar: {exc}") from exc
    require_exact_fields(corpus, EXPECTED_ROOT_FIELDS, "Korpuswurzel")
    stand = validate_collection_date(corpus.get("stand"))
    require_text(corpus.get("titel"), "titel")
    require_text(corpus.get("hinweis"), "hinweis")
    counts = corpus.get("anzahl")
    if not isinstance(counts, dict) or set(counts) != COUNT_FIELDS or not all(
        isinstance(value, int) and not isinstance(value, bool) and value >= 0
        for value in counts.values()
    ):
        raise ValueError("anzahl hat nicht die erwartete Zählstruktur")
    if not isinstance(corpus.get("entscheidungen"), list):
        raise ValueError("entscheidungen muss eine Liste sein")
    identities: set[tuple[str, str, str, str]] = set()
    actual_counts = {
        "gesamt": len(corpus["entscheidungen"]),
        "leitentscheidungen_eugh": 0,
        "leitentscheidungen_bgh": 0,
        "schlussantraege": 0,
        "instanzentscheidungen": 0,
    }
    for index, record in enumerate(corpus["entscheidungen"], start=1):
        label = f"Datensatz {index}"
        if not isinstance(record, dict):
            raise ValueError(f"{label} ist kein Objekt")
        require_exact_fields(record, EXPECTED_FIELDS, label)
        kind = require_text(record.get("typ"), f"{label}.typ")
        if kind not in ALLOWED_TYPES:
            raise ValueError(f"{label}: unbekannter Typ {kind!r}")
        for field in ("spruchkoerper", "gericht", "az", "quelle"):
            require_text(record.get(field), f"{label}.{field}")
        for field in (
            "parteien",
            "vorlegendes_gericht",
            "kernaussage",
            "modell",
            "motor",
            "ez",
            "norm",
            "abschalteinrichtung",
        ):
            require_optional_text(record.get(field), f"{label}.{field}")
        decision_date = parse_iso_date(record.get("datum"))
        if decision_date > stand:
            raise ValueError(f"{label}.datum liegt nach dem Korpusstand")
        aliases = record.get("alias_az")
        if aliases is not None:
            aliases = require_unique_text_list(aliases, f"{label}.alias_az")
            if record["az"] in aliases:
                raise ValueError(f"{label}.alias_az enthält das kanonische Aktenzeichen")
        identity = (kind, record["gericht"], record["datum"], record["az"])
        if identity in identities:
            raise ValueError(f"{label}: doppelte Entscheidungsidentität {identity!r}")
        identities.add(identity)
        for field in ("volltext_url", "podcast_url"):
            url = record.get(field)
            if url is not None and not is_https_url(url):
                raise ValueError(f"{label}.{field} ist keine sichere HTTPS-URL")

        if kind == "instanzentscheidung":
            actual_counts["instanzentscheidungen"] += 1
            if record["spruchkoerper"] not in {"AG", "LG", "OLG/KG"}:
                raise ValueError(f"{label}.spruchkoerper ist für eine Instanzentscheidung unzulässig")
            for field in ("parteien", "vorlegendes_gericht", "alias_az", "kernaussage"):
                if record[field] is not None:
                    raise ValueError(f"{label}.{field} muss bei anonymisierten Instanzdaten null sein")
            if record["motor"] != "EA288":
                raise ValueError(f"{label}.motor muss EA288 sein")
            for field in ("volltext_url", "podcast_url"):
                if not is_https_url(record[field]):
                    raise ValueError(f"{label}.{field} ist für Instanzdaten erforderlich")
            require_nonnegative_number(
                record["differenzschaden_eur"],
                f"{label}.differenzschaden_eur",
                optional=False,
            )
        else:
            require_text(record.get("kernaussage"), f"{label}.kernaussage")
            if not is_https_url(record.get("volltext_url")):
                raise ValueError(f"{label}.volltext_url ist für Leit- und Schlussentscheidungen erforderlich")
            if record["differenzschaden_eur"] is not None:
                raise ValueError(f"{label}.differenzschaden_eur muss null sein")
            for field in ("modell", "motor", "ez", "norm", "abschalteinrichtung"):
                if record[field] is not None:
                    raise ValueError(f"{label}.{field} muss bei Leitmaterial null sein")
            if kind == "schlussantrag_generalanwalt":
                actual_counts["schlussantraege"] += 1
                if not str(record["spruchkoerper"]).startswith("EuGH-Generalanwalt"):
                    raise ValueError(f"{label}.spruchkoerper passt nicht zum Schlussantrag")
                if record["gericht"] != "Gerichtshof der Europäischen Union":
                    raise ValueError(f"{label}.gericht passt nicht zum Schlussantrag")
            elif record["spruchkoerper"] == "EuGH":
                actual_counts["leitentscheidungen_eugh"] += 1
                if record["gericht"] != "Gerichtshof der Europäischen Union":
                    raise ValueError(f"{label}.gericht passt nicht zum EuGH")
            elif record["spruchkoerper"] == "BGH":
                actual_counts["leitentscheidungen_bgh"] += 1
                if record["gericht"] != "Bundesgerichtshof":
                    raise ValueError(f"{label}.gericht passt nicht zum BGH")
                require_canonical_bgh_source("BGH", record["az"], record["volltext_url"], label)
            else:
                raise ValueError(f"{label}.spruchkoerper passt nicht zur Leitentscheidung")
            if record["spruchkoerper"] != "BGH":
                host = (urlparse(record["volltext_url"]).hostname or "").lower()
                if not (host == "eur-lex.europa.eu" or host.endswith(".curia.europa.eu")):
                    raise ValueError(f"{label}.volltext_url ist keine amtliche EuGH-Quelle")
    if counts != actual_counts:
        raise ValueError(f"anzahl widerspricht den Datensätzen: erwartet {actual_counts}, gefunden {counts}")
    return corpus


def _contains(record: dict, field_name: str, needle: str | None) -> bool:
    return needle is None or normalize(needle) in normalize(record.get(field_name))


def matches(record: dict, filters: Filters) -> bool:
    if filters.typ and record.get("typ") != filters.typ:
        return False
    if not _contains(record, "gericht", filters.gericht):
        return False
    if filters.az:
        docket_haystack = normalize([record.get("az"), *(record.get("alias_az") or [])])
        if normalize(filters.az) not in docket_haystack:
            return False
    if not _contains(record, "modell", filters.modell):
        return False
    if not _contains(record, "abschalteinrichtung", filters.einrichtung):
        return False
    if not _contains(record, "norm", filters.norm):
        return False
    try:
        year = iso_year(record.get("datum"))
    except ValueError:
        return False
    if filters.jahr_von is not None and year < filters.jahr_von:
        return False
    if filters.jahr_bis is not None and year > filters.jahr_bis:
        return False
    amount_value = record.get("differenzschaden_eur")
    amount = None
    if not isinstance(amount_value, bool) and isinstance(amount_value, (int, float)):
        if isinstance(amount_value, float) and not math.isfinite(amount_value):
            return False
        amount = Decimal(str(amount_value))
    if filters.betrag_min is not None and (amount is None or amount < filters.betrag_min):
        return False
    if filters.betrag_max is not None and (amount is None or amount > filters.betrag_max):
        return False
    if filters.mit_volltext and not is_https_url(record.get("volltext_url")):
        return False
    haystack = normalize([record.get(field_name) for field_name in SEARCH_FIELDS])
    return all(normalize(query) in haystack for query in filters.queries)


def filter_records(records: list[dict], filters: Filters, sort_mode: str) -> list[dict]:
    selected = [record for record in records if matches(record, filters)]
    if sort_mode == "datum-desc":
        selected.sort(key=lambda record: (record.get("datum") or "", record.get("az") or ""), reverse=True)
    elif sort_mode == "betrag-desc":
        def amount_key(record: dict) -> tuple[bool, Decimal, str]:
            value = record.get("differenzschaden_eur")
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                return False, Decimal(0), str(record.get("datum") or "")
            if isinstance(value, float) and not math.isfinite(value):
                return False, Decimal(0), str(record.get("datum") or "")
            return True, Decimal(str(value)), str(record.get("datum") or "")

        selected.sort(
            key=amount_key,
            reverse=True,
        )
    return selected


def _escape_markdown(value: object) -> str:
    return markdown_cell(value)


def _format_amount(value: object) -> str:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return "-"
    if isinstance(value, float) and not math.isfinite(value):
        return "-"
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def render_markdown(
    records: list[dict],
    total: int,
    truncated: bool,
    stand: str | None = None,
) -> str:
    result_line = f"Treffer: **{total}** | Ausgegeben: **{len(records)}**"
    if stand:
        result_line += f" | Korpusstand: **{stand}**"
    lines = [
        "# EA288-Korpusabfrage",
        "",
        f"> {LIVE_CHECK_NOTICE}",
        "",
        result_line,
        "",
    ]
    if truncated:
        lines.extend(["> Ausgabe gekürzt. Mit `--limit 0` alle Treffer ausgeben.", ""])
    if not records:
        lines.append("Keine Treffer. Filter eingrenzen oder Schreibweise prüfen.")
        return "\n".join(lines) + "\n"
    lines.extend(
        [
            "| Typ | Gericht | Datum | Az. | Modell | Einrichtung | Betrag EUR | Volltext |",
            "| --- | --- | --- | --- | --- | --- | ---: | --- |",
        ]
    )
    for record in records:
        url = record.get("volltext_url")
        safe_url = markdown_url(url)
        full_text = f"[Volltext]({safe_url})" if safe_url else "-"
        lines.append(
            "| "
            + " | ".join(
                (
                    _escape_markdown(record.get("typ")),
                    _escape_markdown(record.get("gericht")),
                    _escape_markdown(record.get("datum")),
                    f"`{markdown_code(record.get('az'))}`",
                    _escape_markdown(record.get("modell")),
                    _escape_markdown(record.get("abschalteinrichtung")),
                    _format_amount(record.get("differenzschaden_eur")),
                    full_text,
                )
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def _filters_from_args(args: argparse.Namespace) -> Filters:
    return Filters(
        queries=args.query,
        typ=args.typ,
        gericht=args.gericht,
        az=args.az,
        modell=args.modell,
        einrichtung=args.einrichtung,
        norm=args.norm,
        jahr_von=args.jahr_von,
        jahr_bis=args.jahr_bis,
        betrag_min=args.betrag_min,
        betrag_max=args.betrag_max,
        mit_volltext=args.mit_volltext,
    )


def _filter_metadata(filters: Filters, sort_mode: str, limit: int) -> dict:
    return {
        "query": filters.queries,
        "typ": filters.typ,
        "gericht": filters.gericht,
        "az": filters.az,
        "modell": filters.modell,
        "einrichtung": filters.einrichtung,
        "norm": filters.norm,
        "jahr_von": filters.jahr_von,
        "jahr_bis": filters.jahr_bis,
        "betrag_min": str(filters.betrag_min) if filters.betrag_min is not None else None,
        "betrag_max": str(filters.betrag_max) if filters.betrag_max is not None else None,
        "mit_volltext": filters.mit_volltext,
        "sort": sort_mode,
        "limit": limit,
    }


def selftest(records: list[dict]) -> None:
    tests = (
        (Filters(queries=["C-100/21"], typ="leitentscheidung"), 1),
        (Filters(gericht="Stuttgart", einrichtung="umgebungsdruck", typ="instanzentscheidung"), 1),
        (Filters(betrag_min=Decimal("12000"), typ="instanzentscheidung"), 1),
        (Filters(queries=["sicher-kein-treffer-288"]), 0),
    )
    for filters, minimum in tests:
        found = filter_records(records, filters, "datum-desc")
        if (minimum == 0 and found) or (minimum > 0 and len(found) < minimum):
            raise AssertionError(f"Filter-Selbsttest fehlgeschlagen: {filters} -> {len(found)}")
    print(f"ea288-corpus-query selftest OK ({len(tests)} Filterfälle, {len(records)} Datensätze)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--query",
        action="append",
        default=[],
        type=parse_query_text,
        help="Volltext-Teilbegriff; mehrfach = UND, höchstens achtmal",
    )
    parser.add_argument(
        "--typ",
        choices=("instanzentscheidung", "leitentscheidung", "schlussantrag_generalanwalt"),
    )
    parser.add_argument("--gericht", type=parse_query_text)
    parser.add_argument("--az", type=parse_query_text)
    parser.add_argument("--modell", type=parse_query_text)
    parser.add_argument("--einrichtung", type=parse_query_text)
    parser.add_argument("--norm", type=parse_query_text)
    parser.add_argument("--jahr-von", type=parse_year)
    parser.add_argument("--jahr-bis", type=parse_year)
    parser.add_argument("--betrag-min", type=parse_decimal)
    parser.add_argument("--betrag-max", type=parse_decimal)
    parser.add_argument("--mit-volltext", action="store_true")
    parser.add_argument("--sort", choices=("datum-desc", "betrag-desc", "korpus"), default="datum-desc")
    parser.add_argument("--limit", type=parse_result_limit, default=25, help="0 = alle Treffer")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if len(args.query) > 8:
        parser.error("--query darf höchstens achtmal angegeben werden")
    try:
        corpus = load_corpus()
        records = corpus["entscheidungen"]
        if args.selftest:
            selftest(records)
            return
        validate_year_range(args.jahr_von, args.jahr_bis)
        if args.betrag_min is not None and args.betrag_max is not None and args.betrag_min > args.betrag_max:
            raise ValueError("--betrag-min darf nicht über --betrag-max liegen")
        filters = _filters_from_args(args)
        selected = filter_records(records, filters, args.sort)
    except (AssertionError, ValueError) as exc:
        print(f"ea288-corpus-query failed: {exc}", file=sys.stderr)
        raise SystemExit(1)

    total = len(selected)
    shown = selected if args.limit == 0 else selected[: args.limit]
    truncated = len(shown) < total
    if args.format == "json":
        output = {
            "schema": "dieselgate.ea288-query-result.v1",
            "source_status": LIVE_CHECK_NOTICE,
            "collection_date": corpus.get("stand"),
            "filters": _filter_metadata(filters, args.sort, args.limit),
            "matches": total,
            "returned": len(shown),
            "truncated": truncated,
            "results": shown,
        }
        write_stdout(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        write_stdout(render_markdown(shown, total, truncated, corpus.get("stand")))


if __name__ == "__main__":
    main()

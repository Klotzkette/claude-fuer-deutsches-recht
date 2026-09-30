#!/usr/bin/env python3
"""Filter the curated 2021-2026 diesel case-law corpus."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse

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
DEFAULT_CORPUS = TOOL_ROOT / "references" / "diesel-rechtsprechung-2021-2026.json"
LEVELS = ("EuGH", "GA", "BGH", "OLG/KG", "LG", "VG/OVG/BVerwG")
EXPECTED_ROOT_FIELDS = {
    "schema",
    "stand",
    "zeitraum",
    "titel",
    "hinweis",
    "umfang",
    "quellenregeln",
    "praxisquellen",
    "entscheidungen",
}
EXPECTED_FIELDS = {
    "id",
    "datum",
    "ebene",
    "gericht",
    "az",
    "themen",
    "fallgruppen",
    "status",
    "richtung",
    "quellenrang",
    "verifikationsstatus",
    "zitierrolle",
    "kernaussage",
    "arbeitsregel",
    "verwendungsgrenze",
    "quelle_url",
    "quelle_art",
    "entscheidungsart",
    "betrag_eur",
    "ecli",
    "folgestatus",
    "geprueft_am",
    "herkunft",
}
ALLOWED_DIRECTIONS = {"verbraucherfreundlich", "herstellerfreundlich", "gemischt", "neutral_prozessual"}
ALLOWED_STATUS = {
    "amtliche_kontextentscheidung",
    "anhaengig",
    "geschlossen",
    "gegenstandslos",
    "gestrichen",
    "historisch",
    "hoechstrichterlich",
    "instanzrechtsprechung",
    "nicht_bindend",
    "offensichtlich_unzulaessig",
    "qualifizierungsbeduerftig",
    "teilweise_ueberholt",
}
ALLOWED_DECISION_TYPES = {
    "Beschluss",
    "Erledigungsbeschluss",
    "Schlussanträge",
    "Streichungsbeschluss",
    "Statusakt",
    "Urteil",
    "Vorabentscheidungsersuchen",
}
ALLOWED_ORIGINS = {"obergerichtsmatrix", "fuenfjahre_ergaenzung"}
LIVE_STATUS_DATE = "2026-09-30"
PENDING_EU_DOCKETS = {
    "C-95/26",
    "C-152/26",
    "C-162/26",
    "C-173/26",
    "C-189/26",
    "C-232/26",
    "C-270/26",
    "C-293/26",
    "C-443/26",
}
CLOSED_EU_CONTRACTS = {
    "C-408/25": "2026-07-21",
}
NEW_STRUCK_EU_CONTRACTS = {
    "C-8/26": ("2026-04-24", "ECLI:EU:C:2026:394"),
    "C-9/26": ("2026-08-04", "ECLI:EU:C:2026:638"),
    "C-43/26": ("2026-08-05", "ECLI:EU:C:2026:647"),
    "C-113/26": ("2026-08-05", "ECLI:EU:C:2026:639"),
    "C-114/26": ("2026-08-12", "ECLI:EU:C:2026:651"),
    "C-228/26": ("2026-08-05", "ECLI:EU:C:2026:641"),
    "C-440/26": ("2026-08-12", "ECLI:EU:C:2026:644"),
    "C-554/25": ("2026-08-06", "ECLI:EU:C:2026:636"),
}
RANK_CONTRACTS = {
    "A": {
        "verification": {"amtliche_pressemitteilung", "primaerquelle_volltext"},
        "roles": {"instanz_oder_kontextanker", "status_oder_rechercheanker", "tragender_anker"},
        "sources": {"amtlich_bgh", "amtlich_bverwg", "amtlich_eu", "amtliche_pressemitteilung", "landesrecht"},
    },
    "B": {
        "verification": {"freie_volltextkopie"},
        "roles": {"instanzanker_nach_volltextpruefung"},
        "sources": {"freie_volltextkopie"},
    },
    "C": {
        "verification": {"metadaten_suchanker"},
        "roles": {"suchanker_volltext_nachziehen"},
        "sources": {"freie_fundstellenvernetzung"},
    },
    "D": {
        "verification": {"parteiquelle_suchanker"},
        "roles": {"parteiquelle_nur_recherche"},
        "sources": {"kanzlei_nutzermaterial"},
    },
}
OFFICIAL_HOST_SUFFIXES = (
    "bundesgerichtshof.de",
    "bverwg.de",
    "curia.europa.eu",
    "eur-lex.europa.eu",
    "justiz.nrw.de",
    "gesetze-bayern.de",
    "schleswig-holstein.de",
    "landesrecht-bw.de",
    "voris.wolterskluwer-online.de",
    "gesetze.berlin.de",
)


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Durchsucht den verifizierten Diesel-Fünfjahreskorpus."
    )
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--query", type=parse_query_text, help="Volltextsuche über alle Felder")
    parser.add_argument("--ebene", choices=LEVELS)
    parser.add_argument("--gericht", type=parse_query_text, help="Teilstring des Gerichtsnamens")
    parser.add_argument("--az", type=parse_query_text, help="Teilstring des Aktenzeichens")
    parser.add_argument("--thema", type=parse_query_text, help="Teilstring in Themen oder Fallgruppen")
    parser.add_argument(
        "--status",
        choices=tuple(sorted(ALLOWED_STATUS | {"bindend"})),
        help="Exakter Verfahrensstatus, z. B. hoechstrichterlich; bindend bleibt Alias",
    )
    parser.add_argument(
        "--richtung",
        choices=(
            "verbraucherfreundlich",
            "herstellerfreundlich",
            "gemischt",
            "neutral_prozessual",
        ),
    )
    parser.add_argument("--quelle-rang", choices=("A", "B", "C", "D"))
    parser.add_argument(
        "--verifikation",
        choices=tuple(
            sorted(
                {
                    value
                    for contract in RANK_CONTRACTS.values()
                    for value in contract["verification"]
                }
            )
        ),
        help="Exakter Verifikationsstatus",
    )
    parser.add_argument("--jahr-von", type=parse_year)
    parser.add_argument("--jahr-bis", type=parse_year)
    parser.add_argument("--limit", type=parse_result_limit, default=25, help="0 = alle Treffer")
    parser.add_argument(
        "--arbeitsset",
        action="store_true",
        help="Höchstens sechs ausgewogene Anker für kleine Modellkontexte",
    )
    parser.add_argument("--format", choices=("markdown", "json", "tsv"), default="markdown")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    return parser


def load_corpus(path: Path) -> dict[str, Any]:
    try:
        data = load_json_object(path)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if data.get("schema") != "dieselgate.fuenfjahre.v1":
        raise SystemExit(f"Unerwartetes Schema in {path}: {data.get('schema')!r}")
    try:
        require_exact_fields(data, EXPECTED_ROOT_FIELDS, "Korpuswurzel")
        stand = validate_collection_date(data.get("stand"))
        period = data.get("zeitraum")
        if not isinstance(period, dict) or set(period) != {"von", "bis"}:
            raise ValueError("zeitraum muss genau von und bis enthalten")
        period_from = parse_iso_date(period["von"])
        period_to = parse_iso_date(period["bis"])
        if period_from > period_to or period_to > stand:
            raise ValueError("zeitraum ist chronologisch ungültig")
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
            if not period_from <= decision_date <= period_to:
                raise ValueError(f"{label}.datum liegt außerhalb des Fünfjahresfensters")
            checked_date = validate_collection_date(
                item["geprueft_am"], label=f"{label}.geprueft_am"
            )
            if checked_date < decision_date:
                raise ValueError(f"{label}.geprueft_am liegt vor dem Entscheidungsdatum")
            for field in (
                "id",
                "ebene",
                "gericht",
                "entscheidungsart",
                "az",
                "status",
                "richtung",
                "verifikationsstatus",
                "zitierrolle",
                "kernaussage",
                "arbeitsregel",
                "verwendungsgrenze",
                "herkunft",
                "quelle_art",
                "quelle_url",
                "quellenrang",
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
        if item["ebene"] not in LEVELS or item["quellenrang"] not in RANK_CONTRACTS:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label} hat unbekannte Klassifikation")
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
        if item["entscheidungsart"] not in ALLOWED_DECISION_TYPES:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: unbekannte Entscheidungsart")
        if item["az"] in PENDING_EU_DOCKETS and (
            item["status"] != "anhaengig"
            or item["entscheidungsart"] != "Vorabentscheidungsersuchen"
            or item["ecli"] is not None
            or item["geprueft_am"] < LIVE_STATUS_DATE
        ):
            raise SystemExit(
                f"Ungültiger Korpus in {path}: {label}: {item['az']} verletzt den "
                f"amtlichen Pending-Statusvertrag vom {LIVE_STATUS_DATE}"
            )
        struck_contract = NEW_STRUCK_EU_CONTRACTS.get(item["az"])
        if struck_contract is not None:
            decision_date, ecli = struck_contract
            source = urlparse(item["quelle_url"])
            if (
                item["status"] != "gestrichen"
                or item["entscheidungsart"] != "Streichungsbeschluss"
                or item["datum"] != decision_date
                or item["ecli"] != ecli
                or item["geprueft_am"] < LIVE_STATUS_DATE
                or source.hostname != "juris.curia.europa.eu"
                or source.path != "/juris/document/document.jsf"
            ):
                raise SystemExit(
                    f"Ungültiger Korpus in {path}: {label}: {item['az']} verletzt den "
                    f"amtlichen Streichungsstatusvertrag vom {LIVE_STATUS_DATE}"
                )
        closed_date = CLOSED_EU_CONTRACTS.get(item["az"])
        if closed_date is not None:
            source = urlparse(item["quelle_url"])
            if (
                item["status"] != "geschlossen"
                or item["entscheidungsart"] != "Statusakt"
                or item["datum"] != closed_date
                or item["ecli"] is not None
                or item["geprueft_am"] < LIVE_STATUS_DATE
                or source.hostname not in {"infocuria.curia.europa.eu", "juris.curia.europa.eu"}
            ):
                raise SystemExit(
                    f"Ungültiger Korpus in {path}: {label}: {item['az']} verletzt den "
                    f"amtlichen Schließungsstatusvertrag vom {LIVE_STATUS_DATE}"
                )
        if item["herkunft"] not in ALLOWED_ORIGINS:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: unbekannte Herkunft")
        if not is_https_url(item["quelle_url"]):
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: Quelle ist keine HTTPS-URL")
        contract = RANK_CONTRACTS[item["quellenrang"]]
        if item["verifikationsstatus"] not in contract["verification"]:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: Quellenrang/Verifikation widersprüchlich")
        if item["zitierrolle"] not in contract["roles"]:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: Quellenrang/Zitierrolle widersprüchlich")
        if item["quelle_art"] not in contract["sources"]:
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: Quellenrang/Quellenart widersprüchlich")
        if item["quellenrang"] == "A":
            host = (urlparse(item["quelle_url"]).hostname or "").lower()
            if not any(host == suffix or host.endswith("." + suffix) for suffix in OFFICIAL_HOST_SUFFIXES):
                raise SystemExit(f"Ungültiger Korpus in {path}: {label}: Rang A ohne amtlichen Host")
        if item["status"] in {"anhaengig", "geschlossen", "gestrichen", "gegenstandslos", "offensichtlich_unzulaessig"} and item["zitierrolle"] == "tragender_anker":
            raise SystemExit(f"Ungültiger Korpus in {path}: {label}: Statusakte darf kein tragender Anker sein")
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
        if args.quelle_rang and item["quellenrang"] != args.quelle_rang:
            continue
        if args.verifikation and item["verifikationsstatus"] != args.verifikation:
            continue
        if args.jahr_von is not None and year < args.jahr_von:
            continue
        if args.jahr_bis is not None and year > args.jahr_bis:
            continue
        if not contains_terms(searchable_text(item), args.query):
            continue
        selected.append(item)
    rank_order = {"A": 0, "B": 1, "C": 2, "D": 3}
    selected.sort(key=lambda item: (item["datum"], item["ebene"], item["az"]), reverse=True)
    selected.sort(key=lambda item: rank_order.get(item["quellenrang"], 99))
    return selected


def balanced_workset(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    used: set[str] = set()

    def take(predicate: Any, amount: int) -> None:
        for item in rows:
            if len([entry for entry in result if predicate(entry)]) >= amount:
                break
            if item["id"] not in used and predicate(item):
                result.append(item)
                used.add(item["id"])

    take(
        lambda item: item["ebene"] in {"EuGH", "BGH"}
        and item["status"] == "hoechstrichterlich"
        and item["quellenrang"] == "A",
        2,
    )
    take(
        lambda item: item["ebene"] in {"OLG/KG", "LG"}
        and item["quellenrang"] in {"A", "B"},
        2,
    )
    take(lambda item: item["ebene"] in {"OLG/KG", "LG"}, 2)
    take(
        lambda item: item["richtung"] == "herstellerfreundlich"
        and item["quellenrang"] in {"A", "B"},
        1,
    )
    take(lambda item: item["richtung"] == "herstellerfreundlich", 1)
    take(
        lambda item: item["quellenrang"] == "A"
        and (
            item["ebene"] == "VG/OVG/BVerwG"
            or item["status"] in {"anhaengig", "geschlossen", "gestrichen", "gegenstandslos", "offensichtlich_unzulaessig"}
        ),
        1,
    )
    if not result and rows:
        result.append(rows[0])
    return result


def format_markdown(
    rows: list[dict[str, Any]],
    stand: str,
    *,
    total: int | None = None,
    workset: bool = False,
) -> str:
    match_count = len(rows) if total is None else total
    truncated = len(rows) < match_count
    result_line = (
        f"Filtertreffer: **{match_count}** | Arbeitsset: **{len(rows)}** | Korpusstand: **{stand}**"
        if workset
        else f"Treffer: **{match_count}** | Ausgegeben: **{len(rows)}** | Korpusstand: **{stand}**"
    )
    lines = [
        "# Diesel-Fünfjahresabfrage",
        "",
        result_line,
        "",
        "> Status, Quellenrang und Verwendungsgrenze sind Bestandteil jedes Treffers. Rang C/D nie unmittelbar als Rechtsprechungsbeleg verwenden.",
        "",
    ]
    if truncated:
        hint = (
            "> Das ausgewogene Arbeitsset ist bewusst auf höchstens sechs Anker begrenzt. "
            "Ohne `--arbeitsset` gilt das normale Ausgabelimit."
            if workset
            else "> Ausgabe gekürzt. Mit `--limit 0` alle Treffer ausgeben; "
            "für kleine Kontexte `--arbeitsset` verwenden."
        )
        lines.extend(
            [
                hint,
                "",
            ]
        )
    if not rows:
        lines.append("Keine Treffer. Filter eingrenzen oder Schreibweise prüfen.")
        return "\n".join(lines)
    for index, item in enumerate(rows, start=1):
        source = markdown_url(item["quelle_url"])
        lines.extend(
            [
                f"### {index}. {markdown_cell(item['gericht'])}, `{markdown_code(item['az'])}`, {markdown_cell(item['datum'])}",
                f"- **Status:** {markdown_cell(item['status'])} | **Rang:** {markdown_cell(item['quellenrang'])} | **Verifikation:** {markdown_cell(item['verifikationsstatus'])}",
                f"- **Rolle:** {markdown_cell(item['zitierrolle'])} | **Richtung:** {markdown_cell(item['richtung'])}",
                f"- **Kernaussage:** {markdown_cell(item['kernaussage'])}",
                f"- **Arbeitsregel:** {markdown_cell(item['arbeitsregel'])}",
                f"- **Grenze:** {markdown_cell(item['verwendungsgrenze'])}",
                f"- **Quelle:** {source}",
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def format_tsv(rows: list[dict[str, Any]]) -> str:
    fields = (
        "datum",
        "ebene",
        "gericht",
        "az",
        "status",
        "richtung",
        "quellenrang",
        "verifikationsstatus",
        "zitierrolle",
        "kernaussage",
        "arbeitsregel",
        "verwendungsgrenze",
        "quelle_url",
    )
    lines = ["\t".join(fields)]
    for item in rows:
        lines.append("\t".join(safe_tsv_cell(item[field]) for field in fields))
    return "\n".join(lines)


def format_stats(rows: list[dict[str, Any]], stand: str) -> str:
    payload = {
        "stand": stand,
        "treffer": len(rows),
        "ebenen": dict(sorted(Counter(item["ebene"] for item in rows).items())),
        "status": dict(sorted(Counter(item["status"] for item in rows).items())),
        "richtungen": dict(sorted(Counter(item["richtung"] for item in rows).items())),
        "quellenraenge": dict(sorted(Counter(item["quellenrang"] for item in rows).items())),
        "verifikationsstatus": dict(
            sorted(Counter(item["verifikationsstatus"] for item in rows).items())
        ),
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def selftest(data: dict[str, Any]) -> None:
    rows = data["entscheidungen"]
    assert len(rows) == 135
    assert Counter(item["ebene"] for item in rows) == Counter(
        {"EuGH": 33, "GA": 2, "BGH": 53, "OLG/KG": 35, "LG": 8, "VG/OVG/BVerwG": 4}
    )
    assert Counter(item["quellenrang"] for item in rows) == Counter(
        {"A": 112, "B": 4, "C": 3, "D": 16}
    )
    sample_args = make_parser().parse_args(["--thema", "EA288", "--arbeitsset"])
    sample = balanced_workset(select(rows, sample_args))
    assert 1 <= len(sample) <= 6
    assert sum(item["ebene"] in {"OLG/KG", "LG"} for item in sample) <= 2
    assert sum(
        item["ebene"] == "VG/OVG/BVerwG"
        or item["status"] in {"anhaengig", "geschlossen", "gestrichen", "gegenstandslos", "offensichtlich_unzulaessig"}
        for item in sample
    ) <= 1
    assert all(item["status"] != "anhaengig" or "keine" in item["verwendungsgrenze"].casefold() for item in sample)
    transliterated_args = make_parser().parse_args(["--query", "Rueckruf"])
    assert select(rows, transliterated_args)
    assert next(item for item in rows if item["az"] == "C-175/25")["status"] == "gestrichen"
    assert next(item for item in rows if item["az"] == "C-732/25")["status"] == "gestrichen"
    assert next(item for item in rows if item["az"] == "XI ZR 162/21")["status"] == "hoechstrichterlich"
    assert next(item for item in rows if item["az"] == "XI ZR 258/22")["status"] == "hoechstrichterlich"
    assert {"VIa ZR 545/23", "VIa ZR 151/23", "VIa ZR 46/24", "VIa ZB 3/24"} <= {
        item["az"] for item in rows if item["status"] == "hoechstrichterlich"
    }
    assert PENDING_EU_DOCKETS == {
        item["az"] for item in rows if item["status"] == "anhaengig"
    }
    for docket, (decision_date, ecli) in NEW_STRUCK_EU_CONTRACTS.items():
        item = next(item for item in rows if item["az"] == docket)
        assert item["status"] == "gestrichen"
        assert item["entscheidungsart"] == "Streichungsbeschluss"
        assert item["datum"] == decision_date
        assert item["ecli"] == ecli
        assert item["geprueft_am"] >= LIVE_STATUS_DATE
    for docket, closed_date in CLOSED_EU_CONTRACTS.items():
        item = next(item for item in rows if item["az"] == docket)
        assert item["status"] == "geschlossen"
        assert item["entscheidungsart"] == "Statusakt"
        assert item["datum"] == closed_date
        assert item["ecli"] is None
        assert item["geprueft_am"] >= LIVE_STATUS_DATE
    print("diesel-fuenfjahre-query selftest OK (135 Datensätze, Arbeitsset maximal 6)")


def main() -> int:
    parser = make_parser()
    args = parser.parse_args()
    try:
        validate_year_range(args.jahr_von, args.jahr_bis)
    except ValueError as exc:
        parser.error(str(exc))
    data = load_corpus(args.corpus)
    if args.selftest:
        selftest(data)
        return 0
    selected = select(data["entscheidungen"], args)
    if args.stats:
        write_stdout(format_stats(selected, data["stand"]))
        return 0
    if args.arbeitsset:
        rows = balanced_workset(selected)
        if args.limit != 0:
            rows = rows[: min(args.limit, 6)]
    else:
        rows = selected if args.limit == 0 else selected[: args.limit]
    if args.format == "json":
        write_stdout(json.dumps(rows, ensure_ascii=False, indent=2))
    elif args.format == "tsv":
        write_stdout(format_tsv(rows))
    else:
        write_stdout(
            format_markdown(
                rows,
                data["stand"],
                total=len(selected),
                workset=args.arbeitsset,
            )
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())

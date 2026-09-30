#!/usr/bin/env python3
"""Report corpus freshness and pending-status risks without network access."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

from query_common import load_json_object


TOOL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = TOOL_ROOT / "references" / "diesel-rechtsprechung-2021-2026.json"
NON_MERITS = {
    "anhaengig",
    "gegenstandslos",
    "gestrichen",
    "nicht_bindend",
    "offensichtlich_unzulaessig",
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_iso_date(value: object, label: str) -> date:
    if not isinstance(value, str) or DATE_RE.fullmatch(value) is None:
        raise ValueError(f"{label} muss YYYY-MM-DD sein")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{label} ist kein gültiges Kalenderdatum") from exc


def parse_age_limit(raw: str) -> int:
    if re.fullmatch(r"(?:[1-9]|[1-9]\d{1,2}|1000)", raw) is None:
        raise argparse.ArgumentTypeError("--max-age-days muss eine Ganzzahl von 1 bis 1000 sein")
    return int(raw)


def load_corpus(path: Path) -> dict[str, Any]:
    try:
        payload = load_json_object(path)
    except ValueError as exc:
        raise ValueError(f"Korpus nicht lesbar: {exc}") from exc
    if payload.get("schema") != "dieselgate.fuenfjahre.v1":
        raise ValueError("unerwartetes Korpusschema")
    rows = payload.get("entscheidungen")
    if not isinstance(rows, list) or not rows or not all(isinstance(row, dict) for row in rows):
        raise ValueError("entscheidungen muss eine nichtleere Objektliste sein")
    return payload


def build_report(payload: dict[str, Any], *, as_of: date, max_age_days: int) -> dict[str, Any]:
    stand = parse_iso_date(payload.get("stand"), "stand")
    rows = payload["entscheidungen"]
    errors: list[str] = []
    stand_age = (as_of - stand).days
    if stand_age < 0:
        errors.append(f"Korpusstand {stand.isoformat()} liegt nach dem Prüftag")

    levels: Counter[str] = Counter()
    ranks: Counter[str] = Counter()
    pending: list[dict[str, Any]] = []
    merits: list[tuple[date, dict[str, Any]]] = []
    for index, row in enumerate(rows, start=1):
        label = f"Datensatz {index}"
        decision_date = parse_iso_date(row.get("datum"), f"{label}.datum")
        checked = parse_iso_date(row.get("geprueft_am"), f"{label}.geprueft_am")
        if decision_date > as_of:
            errors.append(f"{row.get('az', label)}: Entscheidungsdatum liegt nach dem Prüftag")
        if checked > as_of:
            errors.append(f"{row.get('az', label)}: Prüfdatum liegt nach dem Prüftag")
        level = row.get("ebene")
        rank = row.get("quellenrang")
        status = row.get("status")
        if not isinstance(level, str) or not isinstance(rank, str) or not isinstance(status, str):
            raise ValueError(f"{label}: Ebene, Quellenrang und Status müssen Text sein")
        levels[level] += 1
        ranks[rank] += 1
        if status == "anhaengig":
            pending.append(
                {
                    "az": str(row.get("az", "")),
                    "gericht": str(row.get("gericht", "")),
                    "geprueft_am": checked.isoformat(),
                    "alter_tage": (as_of - checked).days,
                }
            )
        elif status not in NON_MERITS and level != "GA":
            merits.append((decision_date, row))

    stale_pending = sorted(
        (item for item in pending if item["alter_tage"] > max_age_days),
        key=lambda item: (-item["alter_tage"], item["az"]),
    )
    stale_reasons: list[str] = []
    if stand_age > max_age_days:
        stale_reasons.append(
            f"Korpusstand ist {stand_age} Tage alt; Grenze {max_age_days} Tage"
        )
    if stale_pending:
        stale_reasons.append(
            f"{len(stale_pending)} anhängige Verfahren haben ein älteres Einzelprüfdatum"
        )

    if not merits:
        raise ValueError("Korpus enthält keine materielle Entscheidung")
    newest_date, newest_row = max(merits, key=lambda item: (item[0], str(item[1].get("az", ""))))
    freigabe = "ROT" if errors else "GELB" if stale_reasons else "GRUEN"
    return {
        "schema": "dieselgate.rechtsstand-monitor.v1",
        "prueftag": as_of.isoformat(),
        "korpusstand": stand.isoformat(),
        "alter_tage": stand_age,
        "max_age_days": max_age_days,
        "freigabe": freigabe,
        "datensaetze": len(rows),
        "ebenen": dict(sorted(levels.items())),
        "quellenraenge": dict(sorted(ranks.items())),
        "amtliche_datensaetze": ranks.get("A", 0),
        "anhaengige_verfahren": len(pending),
        "aeltestes_anhaengig_pruefdatum": min(
            (item["geprueft_am"] for item in pending), default=None
        ),
        "neueste_sachentscheidung": {
            "datum": newest_date.isoformat(),
            "gericht": newest_row.get("gericht"),
            "az": newest_row.get("az"),
        },
        "veraltete_anhaengige_verfahren": stale_pending,
        "hinweise": stale_reasons,
        "fehler": errors,
        "verwendungsgrenze": (
            "Lokaler Aktualitätscheck ohne Netzabruf. Vor produktiver Zitierung Volltext, "
            "Randnummer, Verfahrensstatus und Folgeentwicklung live prüfen."
        ),
    }


def markdown_report(report: dict[str, Any]) -> str:
    newest = report["neueste_sachentscheidung"]
    lines = [
        "# Rechtsstand-Cockpit",
        "",
        f"- Freigabe: **{report['freigabe']}**",
        f"- Prüftag / Korpusstand: `{report['prueftag']}` / `{report['korpusstand']}` ({report['alter_tage']} Tage)",
        f"- Umfang: {report['datensaetze']} Akten, davon {report['amtliche_datensaetze']} mit Quellenrang A",
        f"- Anhängige Verfahren: {report['anhaengige_verfahren']}",
        f"- Neueste Sachentscheidung: {newest['gericht']}, `{newest['az']}`, {newest['datum']}",
        "",
    ]
    for heading, key in (("Stopps", "fehler"), ("Aktualisierung nötig", "hinweise")):
        values = report[key]
        if values:
            lines.extend((f"## {heading}", ""))
            lines.extend(f"- {value}" for value in values)
            lines.append("")
    stale = report["veraltete_anhaengige_verfahren"]
    if stale:
        lines.extend(("## Veraltete Statusprüfungen", ""))
        lines.extend(
            f"- `{item['az']}`: {item['geprueft_am']} ({item['alter_tage']} Tage)"
            for item in stale
        )
        lines.append("")
    lines.extend(("## Verwendungsgrenze", "", report["verwendungsgrenze"], ""))
    return "\n".join(lines)


def run_selftest() -> None:
    fixture = {
        "schema": "dieselgate.fuenfjahre.v1",
        "stand": "2026-08-01",
        "entscheidungen": [
            {
                "datum": "2026-07-28",
                "geprueft_am": "2026-08-01",
                "ebene": "BGH",
                "gericht": "Bundesgerichtshof",
                "az": "VIa ZR 1/26",
                "status": "hoechstrichterlich",
                "quellenrang": "A",
            },
            {
                "datum": "2026-03-19",
                "geprueft_am": "2026-07-15",
                "ebene": "EuGH",
                "gericht": "Gerichtshof der Europäischen Union",
                "az": "C-1/26",
                "status": "anhaengig",
                "quellenrang": "A",
            },
        ],
    }
    fresh = build_report(fixture, as_of=date(2026, 8, 9), max_age_days=45)
    stale = build_report(fixture, as_of=date(2026, 9, 15), max_age_days=45)
    future_fixture = dict(fixture, stand="2026-08-10")
    future = build_report(future_fixture, as_of=date(2026, 8, 9), max_age_days=45)
    checks = (
        (fresh["freigabe"] == "GRUEN", "frischer Korpus nicht grün"),
        (stale["freigabe"] == "GELB", "veralteter Status nicht gelb"),
        (future["freigabe"] == "ROT", "zukünftiger Korpusstand nicht rot"),
        ("Rechtsstand-Cockpit" in markdown_report(fresh), "Markdown-Ausgabe unvollständig"),
    )
    failures = [message for passed, message in checks if not passed]
    if failures:
        raise ValueError("; ".join(failures))
    print("rechtsstand-monitor selftest OK (4 Fälle)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--as-of", help="Prüftag YYYY-MM-DD; Standard ist heute")
    parser.add_argument("--max-age-days", type=parse_age_limit, default=45)
    parser.add_argument("--strict", action="store_true", help="bei GELB oder ROT mit Exitcode 1 stoppen")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    try:
        if args.selftest:
            run_selftest()
            return 0
        as_of = parse_iso_date(args.as_of, "--as-of") if args.as_of else date.today()
        report = build_report(load_corpus(args.input), as_of=as_of, max_age_days=args.max_age_days)
    except ValueError as exc:
        print(f"rechtsstand-monitor failed: {exc}", file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(markdown_report(report), end="")
    return 1 if args.strict and report["freigabe"] != "GRUEN" else 0


if __name__ == "__main__":
    raise SystemExit(main())

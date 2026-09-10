#!/usr/bin/env python3
"""Vergleicht Grundsteuerwerte dezimal, ohne Rechtswahl oder Rundungsannahme."""

import argparse
from decimal import Decimal, localcontext
import json
from pathlib import Path
import re
import sys


FIELDS = {
    "grundsteuerwert_eur", "messzahl_promille", "messbetrag_bescheid_eur",
    "messbetrag_jahresbescheid_eur", "hebesatz_prozent", "jahressteuer_bescheid_eur",
    "gemeiner_wert_eur",
}


def number(value, field):
    if not isinstance(value, str) or not re.fullmatch(r"(?:0|[1-9][0-9]{0,14})(?:\.[0-9]{1,8})?", value):
        raise ValueError(f"{field}: Dezimaltext ohne Tausenderzeichen erwartet, z. B. 114.05")
    result = Decimal(value)
    if field == "gemeiner_wert_eur" and result == 0:
        raise ValueError("gemeiner_wert_eur: Für den Schwellenvergleich muss der Wert positiv sein")
    return result


def compare(data):
    if not isinstance(data, dict) or not data or set(data) - FIELDS:
        raise ValueError("Ein nicht leeres Objekt mit den dokumentierten Feldern ist erforderlich")
    values = {key: number(value, key) for key, value in data.items()}
    output = {
        "eingaben": data,
        "rohwerte": {},
        "fehlende_eingaben": {},
        "hinweis": "Keine Rundungsregel, Rechtswahl, Fristberechnung oder Zahlungsfreigabe. Fehlende Werte werden nicht als null behandelt.",
    }
    calculations = (
        ("messbetrag_rechnerisch_eur", ("grundsteuerwert_eur", "messzahl_promille"), lambda a, b: a * b / 1000),
        ("steuer_aus_messbescheid_eur", ("messbetrag_bescheid_eur", "hebesatz_prozent"), lambda a, b: a * b / 100),
        ("steuer_aus_jahresbescheid_eur", ("messbetrag_jahresbescheid_eur", "hebesatz_prozent"), lambda a, b: a * b / 100),
        ("messbetrag_uebernahmedifferenz_eur", ("messbetrag_jahresbescheid_eur", "messbetrag_bescheid_eur"), lambda a, b: a - b),
    )
    with localcontext() as context:
        context.prec = 64
        for name, inputs, operation in calculations:
            missing = [key for key in inputs if key not in values]
            if missing:
                output["fehlende_eingaben"][name] = missing
            else:
                output["rohwerte"][name] = format(operation(*(values[key] for key in inputs)), "f")
        if {"jahressteuer_bescheid_eur", "messbetrag_jahresbescheid_eur", "hebesatz_prozent"} <= values.keys():
            raw = values["messbetrag_jahresbescheid_eur"] * values["hebesatz_prozent"] / 100
            output["rohwerte"]["jahressteuer_differenz_zum_rohprodukt_eur"] = format(values["jahressteuer_bescheid_eur"] - raw, "f")
        if {"grundsteuerwert_eur", "gemeiner_wert_eur"} <= values.keys():
            threshold = values["gemeiner_wert_eur"] * Decimal("1.40")
            output["bundesmodell_schwelle"] = {
                "vergleichswert_eur": format(threshold, "f"),
                "rechnerisch_erreicht": values["grundsteuerwert_eur"] >= threshold,
                "hinweis": "Nur Rechenvergleich für Paragraf 220 Absatz 2 BewG; Nachweisqualität, Stichtag und Änderbarkeit sind nicht geprüft. Nicht auf Landesmodelle übertragen.",
            }
    return output


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Doppeltes Feld: {key}")
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("datei", help="JSON-Datei; '-' liest von der Standardeingabe")
    args = parser.parse_args()
    try:
        if args.datei == "-":
            source = sys.stdin.read(65537)
        else:
            with Path(args.datei).open(encoding="utf-8") as handle:
                source = handle.read(65537)
        if len(source) > 65536:
            raise ValueError("Eingabe überschreitet 65536 Zeichen")
        data = json.loads(source, object_pairs_hook=unique_object)
        print(json.dumps(compare(data), ensure_ascii=False, indent=2))
    except (OSError, UnicodeError, ValueError, RecursionError) as error:
        print(f"Rechenabgleich abgebrochen: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Inventar der lesbaren Werkstatttexte mit Fundstellen für die redaktionelle Prüfung."""

import argparse
import json
import re
import runpy
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Auch nach der Zusammenführung öffentlich lesbare Fachwerkstätten ohne eigenen
# Marketplace-Eintrag. Vertriebs- und Reihenstände in quality sind keine Prompts.
EIGENSTAENDIGE_QUELLEN = (
    "arbeitszeugnis-analyse",
    "bautraegervertragspruefer",
    "insolvenzforderungsanmeldungspruefung",
    "insolvenzrecht",
    "projekteinkauf-baubranche",
    "sozialversicherungsstatus-pruefer",
)


def weitere_werkstaetten():
    vorgaenger = [ROOT / slug / f"{slug}-werkstatt.md" for slug in EIGENSTAENDIGE_QUELLEN]
    rollenprompts = sorted((ROOT / "vergaberecht-werkstatt").glob("vergaberecht-arbeitsprompt-*.md"))
    return [*vorgaenger, ROOT / "patentrecht/references/patentanmelder-anspruchswerkstatt.md", *rollenprompts]


def erster_absatz(text):
    """Kommentar und Überschrift überspringen, eine führende Tabelle sichtbar lassen."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return next((p.strip() for p in re.split(r"\n\s*\n", text)
                 if p.strip() and not p.strip().startswith("#")), "")


def fundstellen(text):
    # Der identische Bedien- und Visualisierungsteil würde im Fachtext fehlende
    # Schritte überdecken. Fundstellen dienen der Durchsicht, nicht der Benotung.
    fachtext = text.split("<!-- BEGIN werkstatt-visualisierung -->", 1)[0]
    muster = {
        "eingang": r"Unterlag|Akten?|Datei|Quellen?|Belege?|Nachweis|Vertrag|Urkund|Bescheid",
        "variante": r"\b(?:wenn|falls|sobald|je nach|liegt|fehlt|bei)\b",
        "fortsetzung": r"nach(?:ge)?reich|kommt[^.\n]{0,110}hinzu|später|fortschreib|ergänz|aktualisier|fortführ|weiterarbeit|fortsetz|nachtrag|geänder|berichtig",
        "arbeitsergebnis": r"erstell|ausformulier|schreib|liefere?|formuliere?|entwerf|Entwurf|berechn|Bericht|überarbeit",
    }
    zeilen = fachtext.splitlines()
    return {name: next((i for i, zeile in enumerate(zeilen, 1)
                        if re.search(regex, zeile, re.I)), None) for name, regex in muster.items()}


def rows():
    inventory = runpy.run_path(str(ROOT / "scripts/audit-rechtsprechungs-metadaten.py"))
    _, registriert = inventory["workshop_inventory"]()
    katalog = {ROOT / entry["path"]: "Marketplace" for entry in registriert}
    for path in weitere_werkstaetten():
        katalog.setdefault(path, "Weitere Fachwerkstatt")
    for path, gruppe in sorted(katalog.items()):
        text = path.read_text(encoding="utf-8")
        yield {
            "pfad": path.relative_to(ROOT).as_posix(),
            "gruppe": gruppe,
            "woerter": len(text.split()),
            "einstieg_zeichen": len(erster_absatz(text)),
            "abschnitte": len(re.findall(r"^## ", text, re.M)),
            "fundstellen_zeilen": fundstellen(text),
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--details", action="store_true", help="Einzelbefunde mit Zeilennummern als JSON")
    args = parser.parse_args()
    daten = list(rows())
    if args.details:
        print(json.dumps(daten, ensure_ascii=False, indent=2))
        return
    for gruppe in sorted({item["gruppe"] for item in daten}):
        teil = [r for r in daten if r["gruppe"] == gruppe]
        print(f"{gruppe}: {len(teil)} Quellen")
        for label in ("woerter", "einstieg_zeichen", "abschnitte"):
            zahlen = [r[label] for r in teil]
            print(f"  {label}: {min(zahlen)} bis {max(zahlen)}, Median {statistics.median(zahlen):g}")
        for k in teil[0]["fundstellen_zeilen"]:
            count = sum(bool(r["fundstellen_zeilen"][k]) for r in teil)
            print(f"  Fundstelle {k}: {count}/{len(teil)}")


if __name__ == "__main__":
    main()

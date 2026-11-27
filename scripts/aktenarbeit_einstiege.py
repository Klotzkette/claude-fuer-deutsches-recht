"""Verlinkt die fachnahen Aktenseiten mit den Schriftstücken des jeweiligen Falls."""

import argparse
from collections import defaultdict
import json
import os
from pathlib import Path
import re

from aktenarbeit_katalog import VERZEICHNIS, kapitel
from aktenbestand import ROOT, fallquellen

BEGIN = "<!-- BEGIN Aktenarbeit -->"
END = "<!-- END Aktenarbeit -->"


def ohne_verweise(inhalt):
    if BEGIN not in inhalt and END not in inhalt:
        return inhalt
    if inhalt.count(BEGIN) != 1 or inhalt.count(END) != 1:
        raise ValueError("Mehrdeutiger Block mit Aktenverweisen")
    start = inhalt.index(BEGIN)
    ende = inhalt.index(END, start) + len(END)
    if not inhalt[ende:].startswith("\n\n"):
        raise ValueError("Beschädigter Abschluss des Aktenverweises")
    return inhalt[:start] + inhalt[ende + 2:]


def bezeichnung(kennung, original):
    if kennung.startswith("personalakte-"):
        nummer = kennung.split("-")[1]
        person = re.search(rf"^- ({nummer} .+)$", original, re.M)
        if person:
            return person.group(1)
    if kennung.startswith("immobilien-"):
        slug = kennung.removeprefix("immobilien-")
        for row in original.splitlines():
            if row.startswith("|") and f"testakte-{slug}.zip" in row:
                return row.split("|")[1].strip()
    return kennung


def mit_verweisen(inhalt, seite, kennungen):
    """Ergänzt einen reproduzierbaren Block und lässt die Originalbytes rekonstruierbar."""
    original = ohne_verweise(inhalt)
    position = original.index("\n\n") + 2
    ursprung = original[position:]
    # Den eigentlichen Aktenauftrag und vorhandene kurze Navigation zuerst lesen.
    for absatz in ursprung.split("\n\n"):
        if absatz.startswith(("#", "<!--", "|", ">")) or not absatz:
            break
        position += len(absatz) + 2
        if not absatz.startswith(("[", "**")):
            break
    position = min(position, len(original))
    pfad = Path(seite)
    ziel = Path(os.path.relpath(VERZEICHNIS, pfad.parent)).as_posix()
    links = []
    for kennung in kennungen:
        if len(kennungen) == 1:
            name = "Arbeitsvermerk und Korrespondenz zu diesem Fall"
        else:
            name = bezeichnung(kennung, original)
        links.append(f"[{name}]({ziel}/{kapitel(kennung)}#fall-{kennung})")
    if len(links) == 1:
        block = links[0]
    else:
        block = "Arbeitsvermerke und Korrespondenz zu den einzelnen Fällen\n\n" + "\n".join(f"- {link}" for link in links)
    return original[:position] + BEGIN + "\n" + block + "\n" + END + "\n\n" + original[position:]


def einstiege(check=False):
    katalog = json.loads((ROOT / "scripts/data/grundakten-lebenswelt/basis-zentral.json").read_text())
    gruppen = defaultdict(list)
    for key, fall in fallquellen().items():
        if key.startswith("testakten/") and key.removeprefix("testakten/") in katalog:
            continue
        gruppen[fall["seite"]].append(fall["id"])
    for seite, kennungen in gruppen.items():
        datei = ROOT / seite
        inhalt = datei.read_text(encoding="utf-8")
        neu = mit_verweisen(inhalt, seite, kennungen)
        if inhalt != neu:
            if check:
                raise ValueError(f"Verweis auf die Aktenarbeit fehlt oder ist veraltet: {seite}")
            datei.write_text(neu, encoding="utf-8")
    print(f"{sum(map(len, gruppen.values()))} Fallverweise auf {len(gruppen)} Einstiegsseiten.")


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--check", action="store_true")
    einstiege(cli.parse_args().check)

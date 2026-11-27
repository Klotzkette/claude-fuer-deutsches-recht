#!/usr/bin/env python3
"""Verlinkt die konkreten Word- und PDF-Fassungen mit ihren Fallakten."""

import argparse
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
import re
from urllib.parse import quote

from aktenbestand import fallquellen, pruefe_fundstellen
from testakte_disclaimer import NOTICE_MARKDOWN

ROOT = Path(__file__).resolve().parents[1]
VERZEICHNIS = Path("docs/downloads/aktenarbeit")
GRUPPEN = ("A–B", "C–F", "G–K", "L–P", "Q–S", "T–Z")
GITHUB = "https://github.com/Klotzkette/claude-fuer-deutsches-recht"
RAW = "https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main"


def gruppe(kennung):
    buchstabe = kennung[0].upper()
    for teil in GRUPPEN:
        if buchstabe <= teil[-1]:
            return teil
    raise ValueError(f"Unbekannter Anfangsbuchstabe: {kennung}")


def kapitel(kennung):
    return "faelle-" + gruppe(kennung).lower().replace("–", "-") + ".md"


def text(wert):
    return " ".join(wert.split()).replace("|", "&#124;").replace("[", "&#91;").replace("]", "&#93;")


def laden():
    return json.loads((ROOT / VERZEICHNIS / "bestand.json").read_text(encoding="utf-8"))["faelle"]


@lru_cache(maxsize=1)
def verweise():
    return {fall["fallpfad"]: f"{kapitel(fall['id'])}#fall-{fall['id']}" for fall in laden()}


def seiten(faelle):
    titel = "# Schriftstücke zu den Testakten"
    einleitung = (
        "Öffne das Kapitel mit dem Anfangsbuchstaben der Fallkennung. Über den Aktennamen gelangst du zu den "
        "Ausgangsunterlagen. Das erste Schriftstück zeigt, wie der Fall ins Rollen kommt. Im Arbeitsvermerk kannst du "
        "Belege abgleichen, offene Fragen festhalten und eine Antwort vorbereiten. Word eignet sich zum Bearbeiten, PDF zum Lesen und Drucken."
    )
    index = [titel, "", einleitung, "", "| Fallkennung | Akten |", "| --- | ---: |"]
    daten = {}
    for teil in GRUPPEN:
        auswahl = sorted((f for f in faelle if gruppe(f["id"]) == teil), key=lambda f: f["id"])
        if not auswahl:
            continue
        name = kapitel(auswahl[0]["id"])
        index.append(f"| [Fallkennungen {teil}]({name}) | {len(auswahl)} |")
        zeilen = [f"# Schriftstücke zu den Testakten {teil}", "",
                  "[Alle Fallkennungen](README.md) · [Testakten nach Thema](../../../testakten/README.md)", "",
                  "Öffne den Aktennamen für die Ausgangsunterlagen oder lade ein einzelnes Schriftstück herunter.",
                  "", NOTICE_MARKDOWN, "", "| Fall und Aktenunterlagen | Schriftstück | Word | PDF |",
                  "| --- | --- | --- | --- |"]
        for fall in auswahl:
            kennung = fall["id"]
            if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", kennung):
                raise ValueError(f"Ungültige Aktenkennung: {kennung}")
            quelle = Path(fall["quelle"])
            if quelle.is_absolute() or not (ROOT / quelle).resolve().is_relative_to(ROOT) or not (ROOT / quelle).exists():
                raise ValueError(f"Aktenquelle fehlt: {quelle}")
            art = "tree" if (ROOT / quelle).is_dir() else "blob"
            falllink = f'{GITHUB}/{art}/main/{quote(quelle.as_posix())}'
            einstieg = f'<a id="fall-{kennung}"></a>[{text(fall["titel"])}]({falllink})<br><sub>{kennung}</sub>'
            paare = {}
            for datei in fall["dateien"]:
                pfad = Path(datei["pfad"])
                if not (ROOT / pfad).resolve().is_relative_to(ROOT / VERZEICHNIS) or not (ROOT / pfad).is_file():
                    raise ValueError(f"Schriftstück fehlt: {pfad}")
                endung = pfad.suffix.lower()
                paar = paare.setdefault(datei["typ"], {})
                if endung not in {".docx", ".pdf"} or endung in paar:
                    raise ValueError(f"Unerwartete Fassung: {pfad}")
                label = "Word" if endung == ".docx" else "PDF"
                paar[endung] = f"[{label}]({RAW}/{quote(pfad.as_posix())})"
            for typ, links in paare.items():
                dokument = {"korrespondenz": fall["familie"], "arbeitsvermerk": "Arbeitsvermerk"}.get(typ, typ)
                zeilen.append(f"| {einstieg} | {text(dokument)} | {links.get('.docx', '–')} | {links.get('.pdf', '–')} |")
                einstieg = ""
            if not paare:
                raise ValueError(f"Akte ohne Schriftstück: {kennung}")
        daten[name] = "\n".join(zeilen) + "\n"
    index.extend([
        "", "## Mit den Schriftstücken arbeiten", "",
        "1. Lies zuerst die E-Mail, den Brief, die Notiz, das Gesprächsprotokoll oder die Arbeitsliste des Falls. "
        "Absender, Anlass und offene Frage ergeben sich aus dem Aktenstück.",
        "2. Öffne die Grundakte über den Aktennamen. Suche die im Arbeitsvermerk genannten Belege und prüfe die zitierten Passagen im Zusammenhang.",
        "3. Trage deinen Befund und die noch fehlende Auskunft im Arbeitsvermerk ein. Der jeweilige Werkstattprompt hilft dir beim Entwurf des beauftragten Schreibens.",
        "", "Bei Uferwerk führt der Aktenname zur Berufungsakte in PDF, bei Tomasius zur Steuerakte im Originalformat. Die zusätzlichen Schriftstücke hier kannst du jeweils als Word und PDF öffnen.",
        "", "[Testakten nach Thema](../../../testakten/README.md) · [Grundakten mit Eingangspost](../../grundakten-lebenswelt/README.md)", ""])
    daten["README.md"] = "\n".join(index)
    return daten


def bestand_pruefen(faelle):
    quellen = fallquellen(ROOT)
    pruefe_fundstellen(ROOT, faelle, quellen)
    if {fall["fallpfad"] for fall in faelle} != set(quellen):
        raise ValueError("Bearbeitete Akten und Fallquellen stimmen nicht überein")
    erfasst = set()
    for fall in faelle:
        quelle = quellen[fall["fallpfad"]]
        kennung = fall["id"]
        if kennung != quelle["id"] or fall["quelle"] != quelle["seite"]:
            raise ValueError(f"Falsche Zuordnung zur Akte {kennung}")
        erwartet = {
            (typ, fmt) for typ in ("arbeitsvermerk", "korrespondenz")
            for fmt in ("docx", "pdf")
        }
        gefunden = set()
        for datei in fall["dateien"]:
            typ, fmt = datei["typ"], datei["format"]
            pfad = Path(datei["pfad"])
            if pfad != VERZEICHNIS / kennung / f"{typ}.{fmt}" or pfad in erfasst:
                raise ValueError(f"Uneindeutige Fassung: {pfad}")
            if sha256((ROOT / pfad).read_bytes()).hexdigest() != datei["sha256"]:
                raise ValueError(f"Prüfsumme stimmt nicht: {pfad}")
            gefunden.add((typ, fmt))
            erfasst.add(pfad)
        if gefunden != erwartet:
            raise ValueError(f"Abweichende Dokumente für {kennung}: {gefunden ^ erwartet}")
    dateien = {p.relative_to(ROOT) for p in (ROOT / VERZEICHNIS).rglob("*")
               if p.is_file() and p.suffix.lower() in {".docx", ".pdf"}}
    if dateien != erfasst:
        raise ValueError(f"Fassungen ohne Zuordnung: {dateien ^ erfasst}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    faelle = laden()
    if not faelle or len({fall["id"] for fall in faelle}) != len(faelle):
        raise SystemExit("Leeres Verzeichnis oder doppelte Aktenkennung")
    if args.check:
        bestand_pruefen(faelle)
    for name, inhalt in seiten(faelle).items():
        ziel = ROOT / VERZEICHNIS / name
        if args.check:
            if not ziel.is_file() or ziel.read_text(encoding="utf-8") != inhalt:
                raise SystemExit(f"Abweichende Katalogseite: {ziel}")
        else:
            ziel.write_text(inhalt, encoding="utf-8")
    print(f"Schriftstücke für {len(faelle)} Fallakten verlinkt.")


if __name__ == "__main__":
    main()

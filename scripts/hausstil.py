#!/usr/bin/env python3
"""Hausstil: eine Quelle fuer Schrift und Groesse der Arbeitsprodukte.

Der neutrale Standard steht allein in hausstil.json. Texte im Repository nennen
eine Schrift nur in der kanonischen Phrase
    "Hausschrift laut Kanzleiprofil, ohne Profil <Schrift> <Groesse>"
oder an einer in hausstil.json eingetragenen Ausnahme. Dieses Modul liefert die
Phrase, ersetzt freie Schriftangaben durch die Phrase und findet Verstoesse.
Die Kommandozeilen stehen in apply-hausstil.py und audit-hausstil.py.
"""
from __future__ import annotations

import fnmatch
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HAUSSTIL_DATEI = REPO / "hausstil.json"
PHRASE_ANFANG = "Hausschrift laut Kanzleiprofil, ohne Profil "
ENDUNGEN_ANWENDEN = (".md", ".txt", ".json")
# HTML und CSS sind Web-Oberflaechen, keine Enddokumente; sie bleiben ungeprueft.
ENDUNGEN_PRUEFEN = (".md", ".txt", ".json", ".py", ".mjs", ".js", ".yaml", ".yml", ".sh")
MASKE = "\x00FREMDVORGABE{index}\x00"
QUELLDATEI = "hausstil.json"
# Schnellstart- und Hauptproblem-Prompts haben eine Bytegrenze von 7500 Bytes (scripts/prompt-limits.json,
# scripts/test-schwerpunkt-coverage.py) und tragen deshalb statt der langen Phrase diese Kurzform ohne
# Schriftnamen; die lange Form steht in Werkstatt-Prompts, Skills und References.
KURZPHRASE = "Kanzleihausschrift"
# Die TXT-Kopie eines Prompts muss byteidentisch zur Markdown-Fassung bleiben.
KURZFORM_ENDUNGEN = ("-schnellstart.md", "-schnellstart.txt", "-hauptproblem.md", "-hauptproblem.txt")
# Wortanfang: kein Wortzeichen davor, oder ein JSON-Zeilenumbruch. In JSON-Dateien steht ein
# Zeilenumbruch als die zwei Zeichen Backslash und n; das n davor ist ein Wortzeichen, deshalb
# wuerde \b dort keinen Wortanfang sehen und "\nArial" bliebe unerkannt.
WORTANFANG = r"(?:(?<!\w)|(?<=\\[nt]))"


@dataclass(frozen=True)
class Hausstil:
    schrift: str
    groesse: str
    gliederung: str
    bekannte_schriftnamen: tuple[str, ...]
    fremdvorgaben: tuple[str, ...]
    ausnahmepfade: tuple[str, ...]


def lade_hausstil(datei: Path = HAUSSTIL_DATEI) -> Hausstil:
    daten = json.loads(datei.read_text(encoding="utf-8"))
    standard = daten["standard"]
    fremdvorgaben = tuple(eintrag["text"] for eintrag in daten["fremdvorgaben"])
    ausnahmepfade = []
    for ausnahme in daten["ausnahmen"]:
        ausnahmepfade.extend(ausnahme["pfade"])
    return Hausstil(
        schrift=standard["schrift"],
        groesse=standard["groesse"],
        gliederung=standard["gliederung"],
        bekannte_schriftnamen=tuple(daten["bekannte_schriftnamen"]),
        fremdvorgaben=fremdvorgaben,
        ausnahmepfade=tuple(ausnahmepfade),
    )


def kanonische_phrase(hausstil: Hausstil) -> str:
    return f"{PHRASE_ANFANG}{hausstil.schrift} {hausstil.groesse}"


def groesse_in_punkt(hausstil: Hausstil) -> float:
    """Liefert die Grundgroesse als Zahl, z. B. "11 pt" -> 11.0; Builder setzen damit Pt(...)."""
    zahl, einheit = hausstil.groesse.split()
    if einheit != "pt":
        raise ValueError(f"Schriftgroesse in hausstil.json muss in pt stehen, nicht in {einheit!r}")
    return float(zahl)


def kurzform(text: str, hausstil: Hausstil) -> str:
    """Ersetzt die lange Phrase durch die Kurzform; fuer Prompts mit Bytegrenze."""
    return text.replace(kanonische_phrase(hausstil), KURZPHRASE)


def formatsatz(hausstil: Hausstil) -> str:
    return f"{kanonische_phrase(hausstil)}, ausschließlich {hausstil.gliederung}e Gliederung"


def ist_ausgenommen(pfad: str, hausstil: Hausstil) -> bool:
    for ausnahme in hausstil.ausnahmepfade:
        ist_muster = "*" in ausnahme
        ist_verzeichnis = ausnahme.endswith("/")
        if ist_muster and fnmatch.fnmatchcase(pfad, ausnahme):
            return True
        if ist_verzeichnis and pfad.startswith(ausnahme):
            return True
        if not ist_muster and not ist_verzeichnis and pfad == ausnahme:
            return True
    return False


def repo_textdateien(repo: Path, endungen: tuple[str, ...]) -> list[str]:
    """Alle versionierten und nicht ignorierten Dateien mit passender Endung, relativ zum Repo."""
    befehl = ["git", "-C", str(repo), "ls-files", "--cached", "--others", "--exclude-standard", "-z"]
    ausgabe = subprocess.run(befehl, capture_output=True, check=True).stdout.decode("utf-8")
    dateien = []
    for pfad in ausgabe.split("\0"):
        if not pfad or not pfad.endswith(endungen):
            continue
        if (repo / pfad).is_file():
            dateien.append(pfad)
    return sorted(set(dateien))


def _schriftnamen_alternation(hausstil: Hausstil) -> str:
    """Die Reihenfolge der Namen ist gleichgueltig: passt ein kuerzerer Name nicht, weil danach
    keine Groesse folgt, probiert die Regex den naechsten Namen (z. B. "Noto Sans" vor "Noto Sans Mono")."""
    return "|".join(re.escape(name) for name in hausstil.bekannte_schriftnamen)


def _maskiere_fremdvorgaben(text: str, hausstil: Hausstil) -> str:
    for index, vorgabe in enumerate(hausstil.fremdvorgaben):
        text = text.replace(vorgabe, MASKE.format(index=index))
    return text


def _demaskiere_fremdvorgaben(text: str, hausstil: Hausstil) -> str:
    for index, vorgabe in enumerate(hausstil.fremdvorgaben):
        text = text.replace(MASKE.format(index=index), vorgabe)
    return text


def ersetze_schriftangaben(text: str, hausstil: Hausstil) -> str:
    """Bringt jede Schriftangabe mit Groesse auf die kanonische Phrase.

    Erfasst werden: eine schon vorhandene kanonische Phrase mit beliebiger
    Schrift (damit ein geaenderter Standard durchschlaegt) sowie freie Angaben
    wie "Times New Roman 11 pt", "Times New Roman, Schriftgroesse 11 pt",
    "Times New Roman mit 11 Punkt". Steht davor "in ", wird "in der " daraus.
    Angaben ohne Groesse bleiben stehen; sie meldet der Validator.
    """
    phrase = kanonische_phrase(hausstil)
    namen = _schriftnamen_alternation(hausstil)
    text = _maskiere_fremdvorgaben(text, hausstil)

    alte_phrase = re.compile(re.escape(PHRASE_ANFANG) + r"(?:" + namen + r") \d{1,2} ?(?:pt|Punkt)\b")
    text = alte_phrase.sub(phrase, text)

    freie_angabe = re.compile(
        r"(?<!ohne Profil )(?P<in>" + WORTANFANG + r"in )?" + WORTANFANG
        + r"(?:" + namen + r"),?\s+(?:in |mit )?(?:Schriftgröße )?\d{1,2} ?(?:pt|Punkt)\b"
    )

    def ersatz(treffer: re.Match) -> str:
        if treffer.group("in"):
            return "in der " + phrase
        return phrase

    text = freie_angabe.sub(ersatz, text)
    return _demaskiere_fremdvorgaben(text, hausstil)


def _schriftname_flexibel(name: str) -> str:
    """Schriftname mit beliebigen Trennern zwischen den Woertern; die Wortgrenzen setzt der Aufrufer."""
    woerter = [re.escape(wort) for wort in name.split()]
    return r"[\s\-_]*".join(woerter)


def finde_verstoesse(text: str, hausstil: Hausstil) -> list[tuple[int, str]]:
    """Zeilennummer und Zeile jeder Schriftnennung ausserhalb der kanonischen Phrase und der Fremdvorgaben."""
    phrase = kanonische_phrase(hausstil)
    bereinigt = text.replace(phrase, " " * len(phrase))
    for vorgabe in hausstil.fremdvorgaben:
        bereinigt = bereinigt.replace(vorgabe, " " * len(vorgabe))
    namen = "|".join(_schriftname_flexibel(name) for name in hausstil.bekannte_schriftnamen)
    # Ganze Woerter, sonst traefe "Lato" in "regulatorisch". Der Wortanfang steht einmal vor der
    # Alternation, nicht in jedem Zweig; das haelt die Suche ueber das ganze Repository schnell.
    muster = re.compile(WORTANFANG + "(?:" + namen + r")\b", re.IGNORECASE)
    originalzeilen = text.split("\n")
    verstoesse = []
    for nummer, zeile in enumerate(bereinigt.split("\n"), start=1):
        if muster.search(zeile):
            verstoesse.append((nummer, originalzeilen[nummer - 1].strip()))
    return verstoesse


def claude_md_nennt_phrase(claude_md_text: str, hausstil: Hausstil) -> bool:
    return kanonische_phrase(hausstil) in claude_md_text

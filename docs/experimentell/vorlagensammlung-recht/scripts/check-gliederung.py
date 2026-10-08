#!/usr/bin/env python3
"""Prüft die verbindliche Gliederungsregel aus references/gliederung.md:

- Keine römische Ziffer als Gliederungsnummer (I., II., III., …, X.).
- Kein Großbuchstaben-Punkt (A., B., …) als eigenständige Gliederungsmarke.
- Keine Buchstaben-Zahlen-Mischform wie A.1, B.2 oder II.1.
- Keine Kleinbuchstaben-Gliederung wie a), b), c).
- Kein verschachtelter Verlagsstil wie aa), bb), cc).
- Keine Paragrafen-Klauselüberschriften wie § 1 als Gliederungsersatz.
- Nach Gliederungsüberschriften muss eine Leerzeile stehen.
- Keine unnummerierte 'Präambel'-Überschrift (CLAUDE.md §2: eine Präambel
  steht niemals unnummeriert vor dem Vertragstext, sondern als Abschnitt
  '1. Präambel / Gegenstand').
- Keine freistehende Gegenstandszeile vor dem ersten Regelungsabschnitt.
  Der Gegenstand steht im Rubrum nur knapp als Kopfangabe oder materiell in
  Abschnitt 1, nicht als fett gesetzter Zwischenkopf.
- Keine Bulletpoint- oder nummerierte Parteienliste im Rubrum,
  Vertragseingang oder notariellen Urkundseingang.

Der Check ist eng gefasst: nur eindeutige Verstoßmuster.
"""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def git_ls_files(pattern: str) -> list[Path]:
    result = subprocess.run(
        [
            "git",
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "--",
            pattern,
        ],
        cwd=REPO, capture_output=True, text=True, check=True,
    )
    return [REPO / line for line in result.stdout.splitlines()]


# Verbotene Gliederungsmuster — am Zeilenanfang (mit Markdown-Überschriften
# erlaubt: '## 1.', '### 1.1', niemals '## I.' oder '## A.')
VERBOTENE_GLIEDERUNG = [
    # Markdown-Überschrift mit römischer Ziffer und Unterzahl, z. B. II.1
    (
        re.compile(r"^#+\s+([IVXLCDM]+(?:\.\d+)+)(?:\s|$)", re.MULTILINE),
        "Markdown-Überschrift mit römisch-dezimaler Mischgliederung",
    ),
    # Paragrafen-Klauselüberschrift als Gliederungsersatz, z. B. § 1 Vertrag.
    (
        re.compile(r"^#+\s+§\s+\d+[a-z]?(?:\s|$)", re.MULTILINE),
        "Paragrafen-Klauselüberschrift statt dezimaler Gliederung",
    ),
    # Markdown-Überschrift mit Großbuchstabe und Unterzahl, z. B. A.1
    (
        re.compile(r"^#+\s+([A-Z](?:\.\d+)+)(?:\s|$)", re.MULTILINE),
        "Markdown-Überschrift mit Buchstaben-Zahlen-Mischgliederung",
    ),
    # Markdown-Überschrift mit römischer Ziffer
    (
        re.compile(r"^#+\s+([IVX]+)\.(?:\s|$)", re.MULTILINE),
        "Markdown-Überschrift mit römischer Gliederungsziffer",
    ),
    # Markdown-Überschrift mit Großbuchstabe + Punkt
    (
        re.compile(r"^#+\s+([A-Z])\.(?:\s|$)", re.MULTILINE),
        "Markdown-Überschrift mit Großbuchstaben-Gliederung",
    ),
    # Fett gesetzte Gliederungszeilen, etwa **A. Sachverhalt** oder **II. Antrag**
    (
        re.compile(r"^\*\*([IVXLCDM]+|[A-Z])\.(?:\d+(?:\.\d+)*)?\s", re.MULTILINE),
        "fett gesetzte römische oder Buchstaben-Gliederung",
    ),
    # Einfache Kleinbuchstaben-Gliederung am Zeilenanfang
    (
        re.compile(r"^\s*([a-z])\)\s", re.MULTILINE),
        "Kleinbuchstaben-Gliederung (a), b), …)",
    ),
    # Listenebene mit 'aa)', 'bb)', etc. (verschachtelter Verlagsstil)
    (
        re.compile(r"^\s*([a-z]{2})\)\s", re.MULTILINE),
        "verschachtelte Verlagsstil-Gliederung (aa), bb), …)",
    ),
    # Klammerbuchstaben am Zeilenanfang — (A), (B), (C) als Präambel-
    # oder Erwägungsgrund-Marker, häufig in englischsprachigen Mustern.
    (
        re.compile(r"^\s*\(([A-Z])\)\s", re.MULTILINE),
        "Klammer-Großbuchstabe als Gliederungsmarke ((A), (B), …)",
    ),
]


def pruefe_leerzeile_nach_h2_h3(text: str) -> list[tuple[int, str]]:
    """Findet H2/H3-Überschriften, denen direkt eine Nicht-Leer-Zeile folgt."""
    fehler = []
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if re.match(r"^#{2,4}\s+\S", line):
            # nächste Zeile prüfen
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                # Ausnahmen: Blockzitat oder direkt eine Aufzählung, das ist
                # legitim — nur eindeutig fehlende Leerzeile vor Fließtext melden
                next_line = lines[i + 1]
                # OK: leere Zeile, --- (HR), >, -/*/+/Ziffer für Liste, |, ```
                # Fail: alles andere, z. B. unmittelbarer Fließtext
                if not re.match(r"^(?:---|\s*[->*+|`]|\s*\d+\.)", next_line):
                    fehler.append((i + 1, line))
    return fehler


def pruefe_unnummerierte_praeambel(text: str) -> list[tuple[int, str]]:
    """Findet unnummerierte 'Präambel'- oder 'Vorbemerkung'-Überschriften.

    CLAUDE.md §2: Eine Präambel steht niemals unnummeriert vor dem
    Vertragstext. Trägt sie inhaltlich, ist sie als erster materieller
    Abschnitt '1. Präambel / Gegenstand' zu nummerieren; sonst als
    einleitendes Rezital ohne eigene Überschrift in Abschnitt 1 zu führen.
    """
    fehler = []
    for i, line in enumerate(text.split("\n")):
        if re.match(r"^#+\s*(?:Präambel|Vorbemerkung)(?:\b.*)?\s*$", line):
            fehler.append((i + 1, line))
    return fehler


def pruefe_freistehenden_gegenstand(text: str) -> list[tuple[int, str]]:
    """Findet Gegenstandszeilen außerhalb der Abschnittslogik."""
    fehler = []
    for i, line in enumerate(text.split("\n")):
        if re.match(r"^(?:\*\*Gegenstand:\*\*|Gegenstand:)\s+", line):
            fehler.append((i + 1, line))
    return fehler


def pruefe_rubrum_ohne_parteienliste(text: str) -> list[tuple[int, str]]:
    """Findet listenartige Rubra und Vertragseingänge.

    CLAUDE.md §2: Rubrum, Beteiligtenkopf, Vertragseingang und notarieller
    Urkundseingang stehen als normaler Eingangstext. Gerade dort sind
    Bulletpoints und nummerierte Parteienschablonen unzulässig.
    """
    fehler = []
    heading = re.compile(
        r"^###\s+(?:Rubrum|Vertragseingang|Notarieller Urkundseingang)[^\n]*\n",
        re.MULTILINE,
    )
    for m in heading.finditer(text):
        start = m.end()
        next_heading = re.search(r"^(?:##\s+|###\s+)", text[start:], re.MULTILINE)
        end = start + next_heading.start() if next_heading else len(text)
        section = text[start:end]
        separator = re.search(r"^---\s*$", section, re.MULTILINE)
        if separator:
            section = section[: separator.start()]
        # Der formale Kopf steht am Anfang des Abschnitts. Ohne Trennlinie
        # begrenzen wir die Prüfung bewusst auf den nahen Kopfbereich, damit
        # spätere Antrags-, Begründungs- oder Anlagenlisten nicht als Rubrum
        # fehlklassifiziert werden.
        lines = section.splitlines()[:35]
        base_line = text[:start].count("\n") + 1
        for offset, line in enumerate(lines, start=0):
            stripped = line.strip()
            if re.match(r"^[-*+]\s+", stripped):
                fehler.append((base_line + offset, line))
            if re.match(
                r"^(?:Erste|Zweite|Dritte|Vierte)\s+Vertragspartei:\s+",
                stripped,
            ):
                fehler.append((base_line + offset, line))
            if re.match(r"^\*\*Parteien(?:\s*/\s*Parties)?\*\*\s*$", stripped):
                fehler.append((base_line + offset, line))
            if re.match(
                r"^\d+\.\s+\*\*(?:[^*]*(?:Partei|Beteiligte|Bauträger|Erwerber|"
                r"Veräußerer|Käufer|Verkäufer)[^*]*)\*\*",
                stripped,
            ):
                fehler.append((base_line + offset, line))
    return fehler


def main() -> int:
    fehler: list[str] = []
    for pfad in git_ls_files("*.md"):
        rel = pfad.relative_to(REPO)
        # Referenzdatei, CHANGELOG, README beachten andere Regeln
        if rel.name in ("gliederung.md", "CHANGELOG.md", "leitentscheidungen-anker.md"):
            continue
        if rel.parts[0] in ("scripts", "templates"):
            continue
        text = pfad.read_text(encoding="utf-8")
        for muster, hinweis in VERBOTENE_GLIEDERUNG:
            for m in muster.finditer(text):
                zn = text[: m.start()].count("\n") + 1
                fehler.append(f"{rel}:{zn}: {hinweis}: {m.group(0).strip()!r}")
        # Leerzeile nach H2/H3 prüfen — nur in Vorlagendateien (nicht im README)
        if rel.name != "README.md":
            for zn, ueberschrift in pruefe_leerzeile_nach_h2_h3(text):
                fehler.append(f"{rel}:{zn}: keine Leerzeile nach Überschrift: {ueberschrift.strip()!r}")
            for zn, ueberschrift in pruefe_unnummerierte_praeambel(text):
                fehler.append(
                    f"{rel}:{zn}: unnummerierte Präambel-Überschrift "
                    f"(CLAUDE.md §2: als '1. Präambel / Gegenstand' nummerieren): "
                    f"{ueberschrift.strip()!r}"
                )
            for zn, eintrag in pruefe_freistehenden_gegenstand(text):
                fehler.append(
                    f"{rel}:{zn}: freistehende Gegenstandszeile "
                    f"(CLAUDE.md §2: Gegenstand in Abschnitt 1 oder nur als "
                    f"Kopfangabe im Rubrum führen): {eintrag.strip()!r}"
                )
            for zn, eintrag in pruefe_rubrum_ohne_parteienliste(text):
                fehler.append(
                    f"{rel}:{zn}: listenartiges Rubrum oder listenartiger "
                    f"Vertragseingang (CLAUDE.md §2: als normalen Eingangstext "
                    f"setzen): {eintrag.strip()!r}"
                )

    if fehler:
        print("check-gliederung: FEHLER")
        for eintrag in fehler[:200]:
            print(" -", eintrag)
        if len(fehler) > 200:
            print(f" ... ({len(fehler) - 200} weitere)")
        return 1
    print("check-gliederung OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

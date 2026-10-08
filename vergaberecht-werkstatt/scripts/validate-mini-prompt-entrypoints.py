#!/usr/bin/env python3
"""Prueft die rechtsprechungsfesten Einstiegskerne der Unified Mini Prompts."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MINI_DIR = ROOT / "unified-mini-prompts"
MAX_CHARS = 7500
MIN_CHARS = 6200


COMMON_REQUIRED = [
    "## Claude-Skill-Modus",
    "## Start",
    "## Fallkarte",
    "## Sofortworkflow",
    "## Output-Weiche",
    "## Rechtsprechungs- und Normkern",
    "## Arbeitsregeln",
    "## Arbeitsmodule",
    "## Ausgabeformat",
    "autark",
    "ohne generische Fülltexte",
    "ohne Skillwahl",
    "Höchstens drei echte Blockerfragen",
    "höchstens drei Fachskills",
    "Prioritätsdateien",
    "Tatbestand",
    "Quellenstatus",
    "Rechtsfolge",
    "EU-Eigenvergabe",
    "Selbstkontrolle",
]

DISALLOWED = [
    "## Rechtsprechungscheck",
    "Schmuckzitat",
    "allgemein schreiben",
]

ROLE_REQUIRED = {
    "vergabestelle-behoerden": [
        "Neuer Vergabestellenfall.",
        "Lage | Rot | Akte | Rechtsweiche | Jetzt",
        "Bestangebot",
        "§ 127 GWB",
        "§ 58 VgV",
        "Mara C-769/23 schafft kein Nur-Preis-Verbot",
        "AESTE C-210/24",
        "C-692/23",
        "C-313/24",
        "C-856/24, ECLI:EU:C:2026:569",
        "C-820/24 Strominator",
        "C-888/24 Adão da Fonseca",
        "EuGH 16.04.2026 C-568/24 Sof Medica, ECLI:EU:C:2026:305",
        "C-424/23 DYKA Plastics",
        "C-534/23 P/C-539/23 P Instituto Cervantes",
        "C-590/24, ECLI:EU:C:2026:41",
        "C-810/24 Urban Vision, ECLI:EU:C:2026:69",
        "C-186/25, ECLI:EU:C:2026:567",
        "§§ 1 bis 19 BwBBG",
        "EuGH 09.01.2025 C-578/23, ECLI:EU:C:2025:4",
        "BGH 31.01.2017 X ZB 10/16",
        "Bundestariftreue",
        "Bundes-Bau/Dienstleistung/Konzession ab 50.000 Euro, nicht reine Lieferung",
        "§-5-Status, §-13-Feststellung und ArbGG-Vorentscheidung prüfen",
        "§ 160 Abs. 2 Satz 2 GWB",
        "VO (EU) 2026/718",
        "Windrotorblätter 70 Prozent",
        "Art.-29-Feststellung",
        "Antea/Varec",
        "Advania/pressetext",
        "Bestwertungsmatrix",
        "Typ, LV, System, Format",
        "Feldautorität",
        "Entscheidungsbrücke",
        "Fristenampel, Schwärzungsmatrix, Laufzeit-/Änderungs-/Insolvenzvermerk",
        "BVerfG 1 BvR 1160/03",
    ],
    "bieter-unternehmen": [
        "Neue Bewerbung.",
        "Lage | Rot | Angebot | Rechtsweiche | Jetzt",
        "Teurer, aber besser",
        "§ 127 GWB",
        "§ 58 VgV",
        "C-769/23 Mara",
        "schafft keine zusätzlichen Kriterien",
        "C-210/24 AESTE",
        "C-313/24",
        "C-820/24",
        "C-856/24",
        "C-888/24 Adão da Fonseca",
        "EuGH 16.04.2026 C-568/24 Sof Medica",
        "C-424/23 DYKA Plastics",
        "C-534/23 P/C-539/23 P Instituto Cervantes",
        "C-590/24",
        "C-810/24 Urban Vision, ECLI:EU:C:2026:69",
        "§§ 1 bis 19 BwBBG",
        "§ 15 Abs. 2",
        "BGH 31.01.2017 X ZB 10/16",
        "§§ 13 bis 16 BTTG",
        "§ 160 Abs. 2 Satz 2 GWB",
        "§-5-Status, §-13-Feststellung, ArbGG-Vorentscheidung",
        "VO (EU) 2026/718",
        "Windquote",
        "Art.-29-Feststellung",
        "C-268/25 nur Schlussanträge",
        "Punktebrücke",
        "Qualitätsvorsprung",
        "Zuschlagschance",
        "Anschluss-/Migrationsalternative, Bieterfrage oder Rüge",
        "Angebotsfreeze",
        "Quittungsabgleich",
        "BVerfG 1 BvR 1160/03",
    ],
    "konkurrenten-rechtsschutz": [
        "Neuer Konkurrentenfall.",
        "Lage | Rot | Angriff | Rechtsweiche | Jetzt",
        "Billigzuschlag/Preis-only",
        "§§ 127, 160 GWB",
        "§ 60 VgV",
        "C-769/23 Mara",
        "nur bei konkreter Sonderregel",
        "C-313/24",
        "C-820/24",
        "C-856/24",
        "C-888/24 Adão da Fonseca",
        "EuGH 16.04.2026 C-568/24 Sof Medica",
        "C-424/23 DYKA Plastics",
        "C-534/23 P/C-539/23 P Instituto Cervantes",
        "C-578/23",
        "C-590/24",
        "C-810/24",
        "§§ 1 bis 19 BwBBG",
        "§ 15 Abs. 2",
        "§§ 13 bis 16 BTTG",
        "§ 160 Abs. 2 Satz 2 GWB",
        "§-13-Feststellung, ArbGG-Vorentscheidung",
        "VO (EU) 2026/718",
        "Art.-29-Feststellung",
        "C-268/25 nur Schlussanträge",
        "Antea, Klaipedos, Varec",
        "Preisformeltest",
        "Niedrigpreisaufklärung",
        "Kausalität",
        "Herkunftszone",
        "Tatsachenkern",
        "Gegenhypothese",
        "BVerfG 1 BvR 1160/03",
    ],
}


def fail(errors: list[str]) -> int:
    print("validate-mini-prompt-entrypoints: FEHLER", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return 1


def main() -> int:
    errors: list[str] = []

    for role, required in ROLE_REQUIRED.items():
        path = MINI_DIR / f"{role}.md"
        if not path.is_file():
            errors.append(f"{path}: Datei fehlt")
            continue
        text = path.read_text(encoding="utf-8")
        length = len(text)
        byte_length = len(text.encode("utf-8"))
        if byte_length > MAX_CHARS:
            errors.append(f"{path}: {byte_length} UTF-8-Bytes, Limit {MAX_CHARS}")
        if length < MIN_CHARS:
            errors.append(f"{path}: nur {length} Zeichen, Einstiegskern wirkt zu duenn")
        for needle in COMMON_REQUIRED:
            if needle not in text:
                errors.append(f"{path}: Pflichtbaustein fehlt: {needle}")
        for needle in required:
            if needle not in text:
                errors.append(f"{path}: Rollenanker fehlt: {needle}")
        for needle in DISALLOWED:
            if needle in text:
                errors.append(f"{path}: generischer Altbaustein noch vorhanden: {needle}")
        if text.count("|") < 35:
            errors.append(f"{path}: Tabellenstruktur zu schwach fuer Schnellstart und Normkern")
        if text.count("ECLI:EU:C:") < 2:
            errors.append(f"{path}: zu wenige ECLI-Anker im Mini-Prompt")

    if errors:
        return fail(errors)
    print("validate-mini-prompt-entrypoints OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

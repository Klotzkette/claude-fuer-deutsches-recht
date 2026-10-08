#!/usr/bin/env python3
"""Prüft die rollenspezifischen System-, Datenherkunfts- und Beweispfade."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ROLE_CHECKS = {
    "Vergabestelle": {
        "files": (
            "vergabestelle-behoerden/skills/legacy-systeme-integration/SKILL.md",
            "vergabestelle-behoerden/skills/wirklichkeitsdaten-beschaffung-steuern/SKILL.md",
            "vergabestelle-behoerden/skills/18-wertungsvermerk-erstellen/SKILL.md",
            "vergabestelle-behoerden/skills/23-stellungnahme-vergabekammer/SKILL.md",
            "vergabestelle-behoerden/references/LEGACY-SYSTEME-INTEGRATION.md",
            "vergabestelle-behoerden/references/FORMATE-UND-SCHNITTSTELLEN.md",
            "vergabestelle-behoerden/assets/templates/systemuebergabe-entscheidungsdaten.md",
        ),
        "terms": (
            ("Feldautorität",),
            ("Entscheidungsbrücke",),
            ("Rückkanal",),
            ("Sof Medica", "C-568/24"),
            ("Verg 2/24",),
            ("Verg 34/20",),
            ("Instituto Cervantes", "C-534/23"),
            ("SIB-Bauwerke",),
            ("BIM/IFC",),
            ("Eingangsbestätigung", "Eingangsabgleich"),
        ),
    },
    "Bieter": {
        "files": (
            "bieter-unternehmen/skills/legacy-systeme-integration/SKILL.md",
            "bieter-unternehmen/skills/angebot-in-vorgegebenem-format-erstellen/SKILL.md",
            "bieter-unternehmen/skills/nachpruefungsantrag-vk/SKILL.md",
            "bieter-unternehmen/references/LEGACY-SYSTEME-INTEGRATION.md",
            "bieter-unternehmen/references/FORMATE-UND-SCHNITTSTELLEN.md",
            "bieter-unternehmen/assets/templates/angebotsfreeze-systemuebergabe.md",
        ),
        "terms": (
            ("Angebotsfreeze", "Freeze-Manifest"),
            ("Nachweis",),
            ("Portalquittung", "Quittungsabgleich"),
            ("veränderbare",),
            ("Sof Medica", "C-568/24"),
            ("Verg 2/24",),
            ("Instituto Cervantes", "C-534/23"),
            ("Source-to-Offer",),
            ("HR-System",),
            ("Eingangsbestätigung", "Eingangsabgleich"),
        ),
    },
    "Konkurrent": {
        "files": (
            "konkurrenten-rechtsschutz/skills/legacy-systeme-integration/SKILL.md",
            "konkurrenten-rechtsschutz/skills/beweisstrategie-und-portalnachweise/SKILL.md",
            "konkurrenten-rechtsschutz/skills/wertungsangriff-und-dokumentationsluecken/SKILL.md",
            "konkurrenten-rechtsschutz/skills/nachpruefungsantrag-konkurrent-vk/SKILL.md",
            "konkurrenten-rechtsschutz/references/LEGACY-SYSTEME-INTEGRATION.md",
            "konkurrenten-rechtsschutz/references/FORMATE-BELEG-UND-UPLOAD.md",
            "konkurrenten-rechtsschutz/assets/templates/beweiskette-systemexport.md",
        ),
        "terms": (
            ("Herkunftszone",),
            ("Tatsachenkern",),
            ("Gegenhypothese",),
            ("unzulässig", "ungeklärt"),
            ("Sof Medica", "C-568/24"),
            ("Verg 2/24",),
            ("Verg 36/23",),
            ("Instituto Cervantes", "C-534/23"),
            ("Akteneinsichtsziel",),
            ("Eingangsbestätigung", "Eingangsabgleich"),
        ),
    },
}

PROMPT_CHECKS = {
    "Vergabestelle": (
        "vergaberecht-arbeitsprompt-vergabestelle.md",
        "vergaberecht-kurzprompt-vergabestelle.md",
        "unified-mini-prompts/vergabestelle-behoerden.md",
        "testakten/megaprompts/vergabestelle-behoerden.md",
    ),
    "Bieter": (
        "vergaberecht-arbeitsprompt-bieter.md",
        "vergaberecht-kurzprompt-bieter.md",
        "unified-mini-prompts/bieter-unternehmen.md",
        "testakten/megaprompts/bieter-unternehmen.md",
    ),
    "Konkurrent": (
        "vergaberecht-arbeitsprompt-konkurrenten.md",
        "vergaberecht-kurzprompt-konkurrenten.md",
        "unified-mini-prompts/konkurrenten-rechtsschutz.md",
        "testakten/megaprompts/konkurrenten-rechtsschutz.md",
    ),
}

PROMPT_ROLE_TERMS = {
    "Vergabestelle": ("Feldautorität", "Entscheidungsbrücke"),
    "Bieter": ("Angebotsfreeze", "Quittungsabgleich"),
    "Konkurrent": ("Herkunftszone", "Tatsachenkern"),
}


def missing_group(text: str, group: tuple[str, ...]) -> bool:
    lowered = text.casefold()
    return not any(term.casefold() in lowered for term in group)


def main() -> int:
    errors: list[str] = []
    checked: set[Path] = set()

    for role, config in ROLE_CHECKS.items():
        combined: list[str] = []
        for relative in config["files"]:
            path = ROOT / relative
            if not path.is_file():
                errors.append(f"{role}: Pflichtdatei fehlt: {relative}")
                continue
            text = path.read_text(encoding="utf-8")
            checked.add(path)
            combined.append(text)
        corpus = "\n".join(combined)
        for group in config["terms"]:
            if missing_group(corpus, group):
                errors.append(f"{role}: Pflichtanker fehlt: {' oder '.join(group)}")

    for role, files in PROMPT_CHECKS.items():
        role_terms = PROMPT_ROLE_TERMS[role]
        for relative in files:
            path = ROOT / relative
            if not path.is_file():
                errors.append(f"{role}: Prompt fehlt: {relative}")
                continue
            text = path.read_text(encoding="utf-8")
            checked.add(path)
            for term in ("C-568/24", "C-534/23", "EU-Eigenvergabe", *role_terms):
                if term.casefold() not in text.casefold():
                    errors.append(f"{relative}: System-/Rechtsprechungsanker fehlt: {term}")

    if errors:
        for error in errors:
            print(f"FEHLER: {error}", file=sys.stderr)
        print(f"validate-system-integration: {len(errors)} Fehler", file=sys.stderr)
        return 1

    print(
        "validate-system-integration OK "
        f"({len(ROLE_CHECKS)} Rollen, {len(checked)} Dateien)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

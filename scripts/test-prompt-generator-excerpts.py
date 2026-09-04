#!/usr/bin/env python3
"""Regressionstest für vollständige Sätze in gekürzten Prompt-Auszügen."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from themen_profile import PROFILE_BY_KEY


SCRIPT = Path(__file__).resolve().parent / "generate-werkstatt-und-schnellstart-prompts.py"
SPEC = importlib.util.spec_from_file_location("generate_prompts", SCRIPT)
assert SPEC and SPEC.loader
G = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G
SPEC.loader.exec_module(G)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    source = (
        "Ein Insolvenzplan darf nur Gegenstände regeln, die nach Paragraf 217 InsO "
        "und den besonderen Planvorschriften disponibel sind. Nicht disponible "
        "Regelungen sind gesondert zu prüfen."
    )
    shortened = G.clean(source, 145)
    require(
        shortened.endswith("disponibel sind."),
        f"vollständiger Satz wurde verstümmelt: {shortened!r}",
    )

    fragment = G.clean("Frist und Form prüfen und anschließend mit den", 42)
    require(not fragment.endswith(" den."), f"echtes Hängewort blieb stehen: {fragment!r}")

    rental = G.quick_grip(PROFILE_BY_KEY["miet"], "Kündigung wegen Zahlungsverzugs", "")
    require("Dreiwochenfrist" not in rental, "Mietkündigung wurde arbeitsrechtlich geroutet")
    require("Schonfrist" in rental, "Mietkündigung verlor die mietrechtliche Prüfroute")
    appointment = G.quick_grip(PROFILE_BY_KEY["verwaltung"], "Konkurrentenschutz", "")
    require("Entgeltpunkte" not in appointment, "Konkurrentenschutz wurde zur Rentenberechnung")
    housing = G.quick_grip(PROFILE_BY_KEY["verwaltung"], "Wohnung und Kündigung einer Genehmigung", "")
    require("Verwaltungsakt" in housing and "Räumungsrisiko" not in housing, "Fachprofil wurde durch ein Einzelwort verdrängt")
    family = G.quick_grip(PROFILE_BY_KEY["famil"], "Unterhalt und Rente", "")
    require("Selbstbehalt" in family and "SGB VI" not in family, "Familienrechtliche Renteneinkünfte wurden ins Rentenverfahren verschoben")

    material = [{"slug": "mietmangel", "heading": "Mietmangel", "desc": "Mietmangel und Mietminderung anhand Vertrag, Anzeige und Belegen prüfen.", "body": ""}]
    require(len(G.profile_fields(PROFILE_BY_KEY["miet"], material, 1)) == 1, "Feldbudget von einem Eintrag überschritten")
    require(G.profile_fields(PROFILE_BY_KEY["miet"], material, 0) == [], "Leeres Feldbudget wurde nicht beachtet")

    with TemporaryDirectory() as folder:
        plugin = Path(folder)
        for number in range(85):
            skill = plugin / "skills" / f"fachthema-{number:03}"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                f'---\nname: fachthema-{number:03}\ndescription: "Eigenständiges Fachthema Nummer {number:03} mit Tatbestand und Rechtsfolge."\n---\n\n# Fachthema {number:03}\n\nKonkretes Material.\n',
                encoding="utf-8",
            )
        collected = G.collect_skill_material(plugin)
        require(len(collected) == 85, "Fachthemen hinter dem achtzigsten Skill fehlen")
        late = next(item for item in collected if item["slug"] == "fachthema-084")
        require(late["heading"] == "Fachthema 084", "Titel eines späteren Skills fehlt")
        require("Nummer 084" in late["desc"], "Beschreibung eines späteren Skills fehlt")
        require(sum(bool(item["raw"]) for item in collected) == 80, "Volltextbudget der Materialauswahl überschritten")

    print("test-prompt-generator-excerpts OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

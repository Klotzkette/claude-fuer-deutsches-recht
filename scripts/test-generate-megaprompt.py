#!/usr/bin/env python3
"""Regressionstest für Links aus Skills in erzeugten Vollprüfungen."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from skill_sources import fachinhalt_path
from tempfile import TemporaryDirectory
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parent / "generate-megaprompt.py"
SPEC = importlib.util.spec_from_file_location("generate_megaprompt", SCRIPT)
assert SPEC and SPEC.loader
G = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G
SPEC.loader.exec_module(G)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    with TemporaryDirectory() as temporary:
        plugin = Path(temporary)
        originals = []
        for slug in ("beweislast", "verjaehrung"):
            source = plugin / "skills" / slug / "FACHINHALT.md"
            source.parent.mkdir(parents=True)
            source.write_text(f'---\nname: {slug}\ndescription: Fachliche Prüfung {slug}.\n---\n\n# {slug}\n\nErhaltene Fachregel {slug}.\n', encoding="utf-8")
            originals.append(source)
        router = plugin / "skills" / "anspruch-pruefen" / "SKILL.md"
        router.parent.mkdir(parents=True)
        router.write_text('---\nname: anspruch-pruefen\ndescription: Fachmodul auswählen.\n---\n\nAuswahlmenü.\n', encoding="utf-8")
        with patch.object(G, "original_skill_sources", return_value=originals):
            subjects = G.collect_skills(plugin)
        require({item[0] for item in subjects} == {"beweislast", "verjaehrung"},
                "Vollprüfung hat Originalfachmodule durch Sammelrouter ersetzt")
        require(all("Erhaltene Fachregel" in item[3] for item in subjects),
                "Vollprüfung hat erhaltenen Fachtext verloren")

    skill_path = fachinhalt_path(
        G.REPO
        / "fachanwalt-insolvenz-sanierungsrecht"
        / "skills"
        / "inso-normenbibliothek"
        / "SKILL.md"
    )
    reference = skill_path.parent / "references" / "index.md"
    require(skill_path.is_file() and reference.is_file(), "Prüfreferenz fehlt")

    body = (
        "[Index](references/index.md)\n"
        "[Abschnitt](references/index.md#suchweg)\n"
        "[Extern](https://example.org/fundstelle)\n"
        "[Fehlt](references/fehlt.md)\n"
    )
    rewritten = G.rewrite_relative_links(body, skill_path)
    expected = (
        f"{G.GITHUB_BLOB}/fachanwalt-insolvenz-sanierungsrecht/skills/"
        "inso-normenbibliothek/references/index.md"
    )

    require(f"[Index]({expected})" in rewritten, "lokaler Link wurde nicht aufgelöst")
    require(
        f"[Abschnitt]({expected}#suchweg)" in rewritten,
        "Anker eines lokalen Links ging verloren",
    )
    require(
        "[Extern](https://example.org/fundstelle)" in rewritten,
        "externer Link darf nicht verändert werden",
    )
    require(
        "[Fehlt](references/fehlt.md)" in rewritten,
        "nicht vorhandener Pfad muss für die Strukturprüfung sichtbar bleiben",
    )

    print("test-generate-megaprompt OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

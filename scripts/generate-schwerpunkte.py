#!/usr/bin/env python3
"""Verzeichnet vorhandene individuelle Schwerpunkt-Prompts; erzeugt keine Fachinhalte."""

import html
import re
from pathlib import Path
from urllib.parse import quote

from quality_lab import ROOT, bounded_bytes, load, marketplace


def main():
    lines = ["# 1. Fachliche Schwerpunktaufträge", "",
             "Je Fachanwalts-Plugin sowie für Steuer- und Insolvenzrecht ein abgegrenzter, arbeitsintensiver Mandatsauftrag. Die Auswahl ist fachlich begründet, keine statistische Rangliste der häufigsten Mandate.", "",
             "Der Skill gehört zum Plugin. Der eigenständige Hauptproblem-Prompt ist ein separater Markdown-Download mit höchstens 7500 Zeichen und Bytes; nicht gemeinsam mit allen anderen Prompts in denselben Auftrag laden.", "",
             "[Alle Plugins](README.md#was-ist-drin) · [Alle Skills](SKILLS.md) · [Werkstatt und Mini](docs/werkstatt-und-schnellstart-coverage.md) · [Qualitätslabor](QUALITY.md)", "",
             "## 1.1. Alphabetische Übersicht", "",
             "| Plugin | Konkreter Schwerpunkt | Skill | Eigenständiger Prompt |", "| --- | --- | --- | --- |"]
    for name, directory in sorted(marketplace().items()):
        if not (name.startswith("fachanwalt-") or name in {"insolvenzrecht", "steuerrecht-anwalt-und-berater"}):
            continue
        path = directory / f"{name}-hauptproblem.md"
        data = bounded_bytes(path)
        if len(data) > 7500 or not data.strip():
            raise ValueError(f"Ungültiger Schwerpunkt-Prompt: {name}")
        text = data.decode("utf-8")
        heading = re.search(r"^#\s+(.+)$", text, re.M)
        if not heading:
            raise ValueError(f"Überschrift fehlt: {name}")
        title = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", heading[1]).replace("|", " / ")
        profile = load(ROOT / "quality/evals" / f"{name}.json")
        skill = profile["cases"][0]["target_skill"]
        skill_path = directory / "skills" / skill / "SKILL.md"
        if not skill_path.is_file():
            raise ValueError(f"Schwerpunkt-Skill fehlt: {name}/{skill}")
        relative = directory.relative_to(ROOT).as_posix()
        url = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=" + quote(path.relative_to(ROOT).as_posix(), safe="/")
        skill_url = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=" + quote(skill_path.relative_to(ROOT).as_posix(), safe="/")
        lines.append(f'| [{name}]({relative}/README.md) | {html.escape(title)} | [{skill}]({skill_url}) | <a href="{url}" download>MD herunterladen</a> |')
    (ROOT / "SCHWERPUNKTE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Schwerpunkt-Verzeichnis aktualisiert; Fachinhalte unverändert.")


if __name__ == "__main__":
    main()

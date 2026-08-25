#!/usr/bin/env python3
"""Prüft Laufzeitbudgets installierbarer Plugins.

Skill-Beschreibungen stehen bereits bei der Auswahl eines Workflows zur Verfügung.
Zu viele Einzelskills oder überlange Einstiegsskills vergrößern deshalb den
Startkontext und verschlechtern Auswahlgeschwindigkeit sowie Treffergenauigkeit.
Vertiefungen gehören in lokale Referenzdateien und werden erst bei Bedarf gelesen.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"

MAX_SKILLS_PER_PLUGIN = 500
MAX_DESCRIPTION_CHARS_PER_PLUGIN = 120_000
MAX_SKILL_LINES = 500
MAX_REFERENCE_BYTES = 96 * 1024
MAX_PLUGIN_FILES = 5_000
MAX_PLUGIN_BYTES = 200 * 1024 * 1024

FRONTMATTER_RE = re.compile(r"\A---\n(?P<frontmatter>.*?)\n---(?:\n|\Z)", re.DOTALL)
DESCRIPTION_RE = re.compile(r"^description:\s*(?P<value>.+?)\s*$", re.MULTILINE)
EMBEDDED_CATALOG_HEADING = "### 5. Fachmodule in diesem Plugin"


def description_length(path: Path, text: str) -> int:
    frontmatter = FRONTMATTER_RE.match(text)
    if not frontmatter:
        raise ValueError(f"{path.relative_to(REPO)}: Frontmatter fehlt")
    match = DESCRIPTION_RE.search(frontmatter.group("frontmatter"))
    if not match:
        raise ValueError(f"{path.relative_to(REPO)}: description fehlt")
    value = match.group("value").strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return len(value)


def plugin_metrics(plugin: dict[str, object]) -> dict[str, object]:
    name = str(plugin["name"])
    source = str(plugin.get("source") or f"./{name}")
    plugin_dir = (REPO / source).resolve()
    try:
        plugin_dir.relative_to(REPO)
    except ValueError as exc:
        raise ValueError(f"{name}: Quelle liegt außerhalb des Repositories") from exc
    if not plugin_dir.is_dir():
        raise ValueError(f"{name}: Plugin-Quelle fehlt: {source}")

    skill_files = sorted((plugin_dir / "skills").glob("*/SKILL.md"))
    description_chars = 0
    longest_skill = 0
    embedded_catalogs: list[str] = []
    long_skills: list[tuple[str, int]] = []
    large_references: list[tuple[str, int]] = []

    for skill_path in skill_files:
        text = skill_path.read_text(encoding="utf-8")
        description_chars += description_length(skill_path, text)
        lines = len(text.splitlines())
        longest_skill = max(longest_skill, lines)
        if lines > MAX_SKILL_LINES:
            long_skills.append((str(skill_path.relative_to(REPO)), lines))
        if EMBEDDED_CATALOG_HEADING in text:
            embedded_catalogs.append(str(skill_path.relative_to(REPO)))

    for reference_path in sorted((plugin_dir / "skills").glob("*/references/*.md")):
        size = reference_path.stat().st_size
        if size > MAX_REFERENCE_BYTES:
            large_references.append((str(reference_path.relative_to(REPO)), size))

    files = [path for path in plugin_dir.rglob("*") if path.is_file()]
    return {
        "name": name,
        "skills": len(skill_files),
        "description_chars": description_chars,
        "longest_skill": longest_skill,
        "files": len(files),
        "bytes": sum(path.stat().st_size for path in files),
        "long_skills": long_skills,
        "large_references": large_references,
        "embedded_catalogs": embedded_catalogs,
    }


def main() -> int:
    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    errors: list[str] = []
    metrics: list[dict[str, object]] = []

    for plugin in marketplace.get("plugins", []):
        try:
            item = plugin_metrics(plugin)
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(str(exc))
            continue
        metrics.append(item)

        name = str(item["name"])
        if item["skills"] > MAX_SKILLS_PER_PLUGIN:
            errors.append(
                f"{name}: {item['skills']} Skills überschreiten das Budget von "
                f"{MAX_SKILLS_PER_PLUGIN}; Normserien als Referenzbibliothek ablegen"
            )
        if item["description_chars"] > MAX_DESCRIPTION_CHARS_PER_PLUGIN:
            errors.append(
                f"{name}: {item['description_chars']} Zeichen Skill-Beschreibungen "
                f"überschreiten das Budget von {MAX_DESCRIPTION_CHARS_PER_PLUGIN}"
            )
        if item["files"] > MAX_PLUGIN_FILES:
            errors.append(
                f"{name}: {item['files']} Dateien überschreiten das Paketlimit von "
                f"{MAX_PLUGIN_FILES}"
            )
        if item["bytes"] > MAX_PLUGIN_BYTES:
            errors.append(
                f"{name}: {item['bytes']} Bytes überschreiten das Paketlimit von "
                f"{MAX_PLUGIN_BYTES}"
            )
        for path, lines in item["long_skills"]:
            errors.append(f"{path}: {lines} Zeilen überschreiten das Budget von {MAX_SKILL_LINES}")
        for path, size in item["large_references"]:
            errors.append(
                f"{path}: {size} Bytes überschreiten das Referenzbudget von "
                f"{MAX_REFERENCE_BYTES}; an Abschnittsgrenzen teilen"
            )
        for path in item["embedded_catalogs"]:
            errors.append(
                f"{path}: vollständige Fachmodulkarte im Einstiegsskill; "
                "nach references/fachmodule.md auslagern"
            )

    print("Größte Plugin-Routingbudgets:")
    for item in sorted(metrics, key=lambda value: int(value["description_chars"]), reverse=True)[:10]:
        print(
            f"  {item['name']}: {item['skills']} Skills, "
            f"{item['description_chars']} Beschreibungszeichen, "
            f"längster Skill {item['longest_skill']} Zeilen"
        )
    print(
        f"Gesamt: {sum(int(item['skills']) for item in metrics)} Skills, "
        f"{sum(int(item['description_chars']) for item in metrics)} Beschreibungszeichen"
    )

    if errors:
        print(f"validate-runtime-performance: {len(errors)} Fehler", file=sys.stderr)
        for error in errors:
            print(f"  FEHLER: {error}", file=sys.stderr)
        return 1
    print("validate-runtime-performance: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

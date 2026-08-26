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

MAX_SKILLS_PER_PLUGIN = 320
MAX_DESCRIPTION_CHARS_PER_PLUGIN = 55_000
MAX_SKILL_LINES = 500
MAX_REFERENCE_BYTES = 96 * 1024
MAX_PLUGIN_FILES = 5_000
MAX_PLUGIN_BYTES = 200 * 1024 * 1024
MAX_TOTAL_SKILLS = 23_000
MAX_TOTAL_DESCRIPTION_CHARS = 3_600_000
MAX_ROUTER_REFERENCE_BYTES = 40 * 1024

RUNTIME_ROUTERS = {
    "hoai-leistungsphasen-praxis": {f"lph-{phase:02d}-arbeitsrouter" for phase in range(1, 10)},
    "kartellrecht-marktabgrenzung-pruefung": {"internationale-kartellrechts-jurisdiktionen"},
    "datenschutzrecht": {"meldung-deutsche-aufsichtsbehoerde"},
    "steuerrecht-anwalt-und-berater": {
        "dba-alle-abkommen-laendermatrix-2026",
        "lohnabrechnung-und-arbeitgeberpflichten",
        "bwa-analyse-und-mandantenbericht",
        "sanierungsgewinn-steuerpruefung",
    },
    "grosskanzlei-corporate-ma": {"beirat-gestaltung-und-governance"},
    "haushaltsrecht-bho-bund-laender": {"bho-normen-und-titelpruefung"},
}

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
    large_router_references: list[tuple[str, int]] = []
    old_selector_phrases: list[str] = []

    for skill_path in skill_files:
        text = skill_path.read_text(encoding="utf-8")
        description_chars += description_length(skill_path, text)
        frontmatter = FRONTMATTER_RE.match(text)
        if frontmatter and "Wenn es um " in frontmatter.group("frontmatter"):
            old_selector_phrases.append(str(skill_path.relative_to(REPO)))
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
        if (
            reference_path.parent.parent.name in RUNTIME_ROUTERS.get(name, set())
            and size > MAX_ROUTER_REFERENCE_BYTES
        ):
            large_router_references.append((str(reference_path.relative_to(REPO)), size))

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
        "large_router_references": large_router_references,
        "embedded_catalogs": embedded_catalogs,
        "old_selector_phrases": old_selector_phrases,
    }


def runtime_route_errors(plugin_dir: Path, name: str) -> list[str]:
    errors: list[str] = []
    skills_dir = plugin_dir / "skills"
    slugs = {path.parent.name for path in skills_dir.glob("*/SKILL.md")}
    for router in RUNTIME_ROUTERS.get(name, set()):
        if router not in slugs:
            errors.append(f"{name}: Laufzeitrouter fehlt: {router}")

    forbidden: set[str] = set()
    if name == "hoai-leistungsphasen-praxis":
        forbidden.update(slug for slug in slugs if re.fullmatch(r"lph-\d{2}-.+", slug) and not slug.endswith("-arbeitsrouter"))
    elif name == "kartellrecht-marktabgrenzung-pruefung":
        forbidden.update(slug for slug in slugs if slug.startswith("jurisdiktion-"))
    elif name == "steuerrecht-anwalt-und-berater":
        forbidden.update(slug for slug in slugs if slug.startswith("lohn-"))
        forbidden.update(slug for slug in slugs if slug.startswith("bwa-") and slug != "bwa-analyse-und-mandantenbericht")
        forbidden.update(slug for slug in slugs if slug.startswith("sanierungsgewinn-") and slug != "sanierungsgewinn-steuerpruefung")
    elif name == "grosskanzlei-corporate-ma":
        forbidden.update(slug for slug in slugs if slug.startswith("beirat-") and slug != "beirat-gestaltung-und-governance")
    elif name == "haushaltsrecht-bho-bund-laender":
        forbidden.update(slug for slug in slugs if slug.startswith("bho-") and slug != "bho-normen-und-titelpruefung")
    if forbidden:
        errors.append(f"{name}: wieder eingeführte Serienrouten: {', '.join(sorted(forbidden)[:8])}")

    alias_prefixes = ("spezial-", "dsv-", "gk-", "anw-", "rom-neu-")
    duplicate_aliases = []
    for slug in slugs:
        for prefix in alias_prefixes:
            if slug.startswith(prefix) and slug[len(prefix) :] in slugs:
                duplicate_aliases.append(slug)
                break
    if duplicate_aliases:
        errors.append(
            f"{name}: doppelte Kern-/Spezialrouten: {', '.join(sorted(duplicate_aliases)[:8])}"
        )
    return errors


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
        for path, size in item["large_router_references"]:
            errors.append(
                f"{path}: {size} Bytes überschreiten das Abrufbudget von "
                f"{MAX_ROUTER_REFERENCE_BYTES} für Laufzeitrouter"
            )
        for path in item["embedded_catalogs"]:
            errors.append(
                f"{path}: vollständige Fachmodulkarte im Einstiegsskill; "
                "nach references/fachmodule.md auslagern"
            )
        for path in item["old_selector_phrases"]:
            errors.append(f"{path}: alte ausufernde Wenn-es-um-Auswahlfloskel")
        source = str(plugin.get("source") or f"./{name}")
        errors.extend(runtime_route_errors((REPO / source).resolve(), name))

    print("Größte Plugin-Routingbudgets:")
    for item in sorted(metrics, key=lambda value: int(value["description_chars"]), reverse=True)[:10]:
        print(
            f"  {item['name']}: {item['skills']} Skills, "
            f"{item['description_chars']} Beschreibungszeichen, "
            f"längster Skill {item['longest_skill']} Zeilen"
        )
    total_skills = sum(int(item["skills"]) for item in metrics)
    total_descriptions = sum(int(item["description_chars"]) for item in metrics)
    print(f"Gesamt: {total_skills} Skills, {total_descriptions} Beschreibungszeichen")
    if total_skills > MAX_TOTAL_SKILLS:
        errors.append(f"Gesamt: {total_skills} Skills überschreiten das Budget von {MAX_TOTAL_SKILLS}")
    if total_descriptions > MAX_TOTAL_DESCRIPTION_CHARS:
        errors.append(
            f"Gesamt: {total_descriptions} Beschreibungszeichen überschreiten das Budget von "
            f"{MAX_TOTAL_DESCRIPTION_CHARS}"
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

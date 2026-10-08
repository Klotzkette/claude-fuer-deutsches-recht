#!/usr/bin/env python3
"""Prüft Dual-Mode-Prompts: Skill-Routing sichtbar, autark nutzbar."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from skill_routing_priorities import (
    MINI_SKILL_SUMMARIES,
    PLUGIN_PRIORITY_SKILLS,
    PLUGIN_TRIGGER_ROUTES,
)


ROOT = Path(__file__).resolve().parents[1]

ROLE_FILES = {
    "vergabestelle-behoerden": [
        ROOT / "vergaberecht-arbeitsprompt-vergabestelle.md",
        ROOT / "vergaberecht-kurzprompt-vergabestelle.md",
        ROOT / "unified-mini-prompts" / "vergabestelle-behoerden.md",
        ROOT / "testakten" / "megaprompts" / "vergabestelle-behoerden.md",
    ],
    "bieter-unternehmen": [
        ROOT / "vergaberecht-arbeitsprompt-bieter.md",
        ROOT / "vergaberecht-kurzprompt-bieter.md",
        ROOT / "unified-mini-prompts" / "bieter-unternehmen.md",
        ROOT / "testakten" / "megaprompts" / "bieter-unternehmen.md",
    ],
    "konkurrenten-rechtsschutz": [
        ROOT / "vergaberecht-arbeitsprompt-konkurrenten.md",
        ROOT / "vergaberecht-kurzprompt-konkurrenten.md",
        ROOT / "unified-mini-prompts" / "konkurrenten-rechtsschutz.md",
        ROOT / "testakten" / "megaprompts" / "konkurrenten-rechtsschutz.md",
    ],
}

DISALLOWED_REQUIRED_CONTEXT = [
    r"Nutze diesen Skill",
    r"## Skill:",
    r"Skills des Plugins",
    r"des Plugins `",
    r"Plugin-Kontext",
    r"vollständige Plugin",
    r"SKILL\.md",
    r"\.claude-plugin",
    r"(?:^|[\s`])references/",
]


def skill_names(plugin: str) -> set[str]:
    skills_dir = ROOT / plugin / "skills"
    return {
        path.parent.name
        for path in skills_dir.glob("*/SKILL.md")
        if path.is_file()
    }


def prompt_kind(path: Path) -> str:
    if path.parent.name == "unified-mini-prompts":
        return "unified"
    if path.parent.name == "megaprompts":
        return "mega"
    return "root"


def extract_skill_slugs(text: str, known_skills: set[str] | None = None) -> list[str]:
    slugs = []
    for token in re.findall(r"`([a-z0-9][a-z0-9-]{2,80})`", text):
        if "-" in token or (known_skills and token in known_skills):
            slugs.append(token)
    return slugs


def validate_prompt(path: Path, plugin: str, skills: set[str]) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"{path}: Datei fehlt"]

    text = path.read_text(encoding="utf-8")
    kind = prompt_kind(path)

    if kind == "unified":
        if "## Claude-Skill-Modus" not in text:
            errors.append(f"{path}: Claude-Skill-Modus fehlt")
    else:
        if "## Claude-Skill-Routing" not in text:
            errors.append(f"{path}: Claude-Skill-Routing fehlt")

    if "autark" not in text.lower():
        errors.append(f"{path}: autarker Fallback fehlt")

    if kind == "mega" and "## Sichtbare Skill-Slugs" not in text:
        errors.append(f"{path}: Sichtbare Skill-Slugs fehlen")
    if kind == "mega":
        h1_count = len(re.findall(r"^#\s+\S", text, flags=re.MULTILINE))
        if h1_count != 1:
            errors.append(f"{path}: genau eine Hauptüberschrift erwartet, gefunden: {h1_count}")
        longest_line = max((len(line) for line in text.splitlines()), default=0)
        if longest_line > 1000:
            errors.append(f"{path}: überlange Einzelzeile mit {longest_line} Zeichen")

    for pattern in DISALLOWED_REQUIRED_CONTEXT:
        if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            errors.append(f"{path}: verbotener notwendiger Kontext: {pattern}")

    prompt_slugs = extract_skill_slugs(text, skills)
    missing = sorted({slug for slug in prompt_slugs if slug not in skills})
    if missing:
        errors.append(f"{path}: unbekannte Skill-Slugs: {', '.join(missing[:20])}")

    if len(set(prompt_slugs)) < 5:
        errors.append(f"{path}: zu wenige Skill-Slugs im Routing sichtbar")

    return errors


def validate_router_tables(
    plugin: str,
    skills: set[str],
    prompt_slugs: dict[Path, set[str]],
) -> list[str]:
    errors: list[str] = []

    priority = PLUGIN_PRIORITY_SKILLS.get(plugin, [])
    unknown_priority = sorted({slug for slug in priority if slug not in skills})
    if unknown_priority:
        errors.append(f"{plugin}: unbekannte Prioritaets-Skills: {', '.join(unknown_priority[:20])}")

    routes = PLUGIN_TRIGGER_ROUTES.get(plugin, [])
    route_targets = [slug for _, slug in routes]
    unknown_routes = sorted({slug for slug in route_targets if slug not in skills})
    if unknown_routes:
        errors.append(f"{plugin}: unbekannte Routing-Skills: {', '.join(unknown_routes[:20])}")

    route_not_prioritized = sorted({slug for slug in route_targets if slug not in priority})
    if route_not_prioritized:
        errors.append(f"{plugin}: Routing-Skills fehlen in Prioritaetsliste: {', '.join(route_not_prioritized[:20])}")

    expected_visible = set(route_targets)
    for path, slugs in prompt_slugs.items():
        missing_visible = sorted(expected_visible - slugs)
        if missing_visible:
            errors.append(f"{path}: Routing-Skills nicht sichtbar: {', '.join(missing_visible[:20])}")

    return errors


def validate_summary_slugs(all_skills: set[str]) -> list[str]:
    missing = sorted({slug for slug in MINI_SKILL_SUMMARIES if slug not in all_skills})
    if missing:
        return [f"skill_routing_priorities.py: Summary-Slugs ohne Skill: {', '.join(missing[:20])}"]
    return []


def main() -> int:
    errors: list[str] = []
    all_skills: set[str] = set()
    for plugin, files in ROLE_FILES.items():
        skills = skill_names(plugin)
        all_skills.update(skills)
        if not skills:
            errors.append(f"{plugin}: keine Skills gefunden")
            continue
        slugs_by_prompt: dict[Path, set[str]] = {}
        for path in files:
            prompt_errors = validate_prompt(path, plugin, skills)
            errors.extend(prompt_errors)
            if path.is_file():
                slugs_by_prompt[path] = set(extract_skill_slugs(path.read_text(encoding="utf-8"), skills))
        errors.extend(validate_router_tables(plugin, skills, slugs_by_prompt))
    errors.extend(validate_summary_slugs(all_skills))

    if errors:
        print("validate-prompt-routing-autarky: FEHLER", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("validate-prompt-routing-autarky OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

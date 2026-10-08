#!/usr/bin/env python3
"""Prueft, ob Skills eindeutig auffindbar und in den Uebersichten sichtbar sind."""

from __future__ import annotations

import json
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
SIMILARITY_LIMIT = 0.80
MIN_SHARED_TOKENS = 8

FORBIDDEN_BOILERPLATE = (
    "anwaltlicher vertiefungs-skill mit normenanker",
    "anwaltlicher vertiefungsskill mit normenanker",
    "von der ersten aktenordnung bis zur belastbaren empfehlung",
    "dieser skill ist ein konkreter fachbaustein",
    "statt austauschbarer standardpruefung",
    "statt austauschbarer standardprüfung",
    "welches verhandlungsziel hat der mandant?",
    "mindestabfindung / freistellung / zeugnisformulierung",
    "erbrechtliche abfindung",
    "bevor das template eins-zu-eins gefüllt wird",
    "vorab: der untenstehende workflow ist die typische standardlinie",
    "vorab: der untenstehende ist die typische standardlinie",
    "rolle klären: auftraggeber, bieter, beigeladener",
    "fallbild bilden: sachverhalt, rollen, zeitachse",
    "normen-/quellenanker: gwb, vgv, uvgo",
    "tragende normen verifizieren: die für rolle und verfahrensstand",
    "lehrgang 120 stunden + drei klausuren",
    "40 fälle in den letzten drei jahren",
    "behängender vorwurf",
    "anstehende auftraggeberentscheidung und spätesten freigabezeitpunkt bestimmen",
    "angebots-, rüge-, stillhalte- oder gerichtsfrist mit zugangsbeleg sichern",
)

ENTRYPOINT_DESCRIPTION_MARKERS = {
    ("vergabestelle-behoerden", "vergabe-os-master-orchestrator"): (
        "ordner",
        "zip",
        "ohne skillwahl",
    ),
    ("vergabestelle-behoerden", "workflow-kaltstart-und-routing"): (
        "einzelnes dokument",
        "konkrete frage",
        "kein vollständiger ordnerfall",
    ),
    ("vergabestelle-behoerden", "einstieg-routing"): (
        "ohne unterlagen",
        "regime",
        "nächsten output",
    ),
    ("bieter-unternehmen", "vergabe-os-master-orchestrator"): (
        "ordner",
        "zip",
        "ohne skillwahl",
    ),
    ("bieter-unternehmen", "workflow-kaltstart-und-routing"): (
        "einzelnes dokument",
        "konkrete frage",
        "kein vollständiger ordnerfall",
    ),
    ("bieter-unternehmen", "einstieg-routing"): (
        "ohne unterlagen",
        "regime",
        "nächsten output",
    ),
    ("konkurrenten-rechtsschutz", "konkurrenzrechtsschutz-orchestrator"): (
        "ordner",
        "zip",
        "ohne skillwahl",
    ),
    ("konkurrenten-rechtsschutz", "startbildschirm-konkurrentenangriff"): (
        "nach der triage",
        "dashboard",
        "kein eigenständiger kaltstart",
    ),
}

ROLE_FORBIDDEN = {
    "vergabestelle-behoerden": (
        "auftraggeber oder bieter?",
        "auftraggeber- oder bieter-mandat?",
        "konzessionsgeber oder bieter",
        "bieter will sektvo-konformes",
        "prüfraster für bieter und vergabekammer",
        "rügeschriftsatz-modul losverzicht (bieter)",
        "prüfvermerk wertungsrüge (bieter)",
        "output je nach rolle",
        "kein ersatz für eine vollständige mandantenberatung",
        "keine festlegung des mandanten",
    ),
    "bieter-unternehmen": (
        "prüfraster für bieter und vergabestelle",
        "auftraggeber oder bieter?",
    ),
}

BODY_SPELLED_PARAGRAPH_RE = re.compile(
    r"\b(?:Paragraf(?:en)?|Paragraph(?:en)?)(?:\s+|-)\d",
    re.IGNORECASE,
)
ROUTING_COLUMN_MARKERS = ("skill", "modul", "routing", "arbeitsweg", "fachpfad")
BACKTICK_SLUG_RE = re.compile(r"`([a-z0-9][a-z0-9-]{2,80})`")
MAX_SKILL_LINES = 500

COMMON_TOKENS = {
    "aber",
    "alle",
    "auch",
    "aus",
    "bei",
    "belastbar",
    "belastbarem",
    "belastbaren",
    "belege",
    "belegen",
    "beweislast",
    "das",
    "dem",
    "den",
    "der",
    "des",
    "die",
    "durch",
    "ein",
    "eine",
    "einem",
    "einen",
    "einer",
    "eines",
    "erstellt",
    "erstellen",
    "fall",
    "fristen",
    "fuer",
    "für",
    "gegen",
    "gegenargumente",
    "gwb",
    "im",
    "in",
    "inklusive",
    "mit",
    "nach",
    "normenanker",
    "oder",
    "paragraf",
    "pruefen",
    "prüfen",
    "rechtsprechung",
    "sowie",
    "und",
    "von",
    "wenn",
    "werden",
    "wird",
    "zur",
    "zum",
}


@dataclass(frozen=True)
class Skill:
    plugin: str
    slug: str
    description: str
    path: Path


def skill_body(path: Path) -> str:
    """Liefert den Skilltext ohne Frontmatter fuer Rollen-Duplikatchecks."""
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    return parts[2].strip() if len(parts) == 3 else text.strip()


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("Frontmatter fehlt")
    try:
        raw = text.split("---", 2)[1]
    except IndexError as exc:
        raise ValueError("Frontmatter ist nicht abgeschlossen") from exc
    parsed = yaml.safe_load(raw)
    if not isinstance(parsed, dict):
        raise ValueError("Frontmatter ist kein Objekt")
    return parsed


def description_tokens(description: str) -> set[str]:
    normalized = description.lower().replace("ß", "ss")
    return {
        token
        for token in re.findall(r"[a-z0-9äöü-]{4,}", normalized)
        if token not in COMMON_TOKENS
    }


def routing_targets(body: str) -> list[tuple[str, int]]:
    """Liest Skill-Slugs nur aus ausdrücklich bezeichneten Routing-Spalten."""
    lines = body.splitlines()
    targets: list[tuple[str, int]] = []
    for index in range(len(lines) - 1):
        header = lines[index]
        separator = lines[index + 1]
        if "|" not in header or not re.fullmatch(r"\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*", separator):
            continue
        headers = [cell.strip().casefold() for cell in header.strip().strip("|").split("|")]
        route_columns = {
            position
            for position, cell in enumerate(headers)
            if any(marker in cell for marker in ROUTING_COLUMN_MARKERS)
        }
        if not route_columns:
            continue
        row_index = index + 2
        while row_index < len(lines) and "|" in lines[row_index]:
            cells = [cell.strip() for cell in lines[row_index].strip().strip("|").split("|")]
            for position in route_columns:
                if position >= len(cells):
                    continue
                targets.extend(
                    (slug, row_index + 1)
                    for slug in BACKTICK_SLUG_RE.findall(cells[position])
                )
            row_index += 1
    return targets


def load_plugins() -> list[tuple[str, Path]]:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    plugins: list[tuple[str, Path]] = []
    for entry in data.get("plugins", []):
        name = entry.get("name")
        source = entry.get("source")
        if not isinstance(name, str) or not isinstance(source, str):
            raise ValueError("Marketplace-Eintrag ohne name oder source")
        plugins.append((name, (ROOT / source).resolve()))
    return plugins


def main() -> int:
    errors: list[str] = []
    skills: list[Skill] = []

    try:
        plugins = load_plugins()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FEHLER: Marketplace kann nicht gelesen werden: {exc}", file=sys.stderr)
        return 1

    for plugin, plugin_path in plugins:
        readme = plugin_path / "README.md"
        index = ROOT / "skills-index" / f"{plugin}.md"
        readme_text = readme.read_text(encoding="utf-8") if readme.exists() else ""
        index_text = index.read_text(encoding="utf-8") if index.exists() else ""

        if not readme_text:
            errors.append(f"{plugin}: Plugin-README fehlt")
        if not index_text:
            errors.append(f"{plugin}: Skill-Index fehlt")

        for path in sorted((plugin_path / "skills").glob("*/SKILL.md")):
            try:
                frontmatter = parse_frontmatter(path)
            except (OSError, ValueError, yaml.YAMLError) as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")
                continue
            slug = frontmatter.get("name")
            description = frontmatter.get("description")
            if not isinstance(slug, str) or not isinstance(description, str):
                errors.append(f"{path.relative_to(ROOT)}: name/description ungueltig")
                continue
            skill = Skill(plugin, slug, description, path)
            skills.append(skill)

            lowered = description.lower()
            for marker in ENTRYPOINT_DESCRIPTION_MARKERS.get((plugin, slug), ()):
                if marker not in lowered:
                    errors.append(
                        f"{path.relative_to(ROOT)}: Einstiegsskill grenzt sich nicht ab; Marker fehlt: '{marker}'"
                    )
            for phrase in FORBIDDEN_BOILERPLATE:
                if phrase in lowered:
                    errors.append(
                        f"{path.relative_to(ROOT)}: generische Description-Phrase '{phrase}'"
                    )
            full_text = path.read_text(encoding="utf-8")
            body = skill_body(path)
            body_lowered = body.lower()
            for phrase in FORBIDDEN_BOILERPLATE:
                if phrase in body_lowered and phrase not in lowered:
                    errors.append(
                        f"{path.relative_to(ROOT)}: generische Body-Phrase '{phrase}'"
                    )
            combined_lowered = f"{lowered}\n{body_lowered}"
            for phrase in ROLE_FORBIDDEN.get(plugin, ()):
                if phrase in combined_lowered:
                    errors.append(
                        f"{path.relative_to(ROOT)}: rollensachfremde Phrase '{phrase}'"
                    )

            body_without_inline_code = re.sub(r"`[^`\n]+`", "", body)
            if BODY_SPELLED_PARAGRAPH_RE.search(body_without_inline_code):
                errors.append(
                    f"{path.relative_to(ROOT)}: Normzitat im Body ausschreiben; dort § oder §§ verwenden"
                )
            line_count = len(full_text.splitlines())
            if line_count > MAX_SKILL_LINES:
                errors.append(
                    f"{path.relative_to(ROOT)}: {line_count} Zeilen; Skill auf höchstens {MAX_SKILL_LINES} Zeilen straffen"
                )
            if full_text.count("<!-- BEGIN output-format-block (autogen) -->") != 1:
                errors.append(f"{path.relative_to(ROOT)}: verwalteter Outputblock fehlt oder ist doppelt")
            headings = re.findall(r"^(#{1,6})\s+(.+?)\s*$", body, flags=re.MULTILINE)
            seen_headings: set[tuple[str, str]] = set()
            for level, title in headings:
                key = (level, title.casefold())
                if key in seen_headings:
                    errors.append(
                        f"{path.relative_to(ROOT)}: doppelte Überschrift '{title}' auf Ebene {len(level)}"
                    )
                seen_headings.add(key)

            if f"`{slug}`" not in readme_text:
                errors.append(f"{plugin}: Skill {slug} fehlt im Plugin-README")
            if f"`{slug}`" not in index_text:
                errors.append(f"{plugin}: Skill {slug} fehlt im Skill-Index")

    by_plugin: dict[str, list[Skill]] = {}
    for skill in skills:
        by_plugin.setdefault(skill.plugin, []).append(skill)

    for plugin, plugin_skills in by_plugin.items():
        known_slugs = {skill.slug for skill in plugin_skills}
        for skill in plugin_skills:
            for target, line_no in routing_targets(skill_body(skill.path)):
                if target not in known_slugs:
                    errors.append(
                        f"{skill.path.relative_to(ROOT)}:{line_no}: Routing verweist auf "
                        f"nicht vorhandenen Skill '{target}'"
                    )

        seen: dict[str, str] = {}
        for skill in plugin_skills:
            if skill.description in seen:
                errors.append(
                    f"{plugin}: identische Descriptions bei {seen[skill.description]} und {skill.slug}"
                )
            seen[skill.description] = skill.slug

        token_sets = {skill.slug: description_tokens(skill.description) for skill in plugin_skills}
        for index, left in enumerate(plugin_skills):
            for right in plugin_skills[index + 1 :]:
                left_tokens = token_sets[left.slug]
                right_tokens = token_sets[right.slug]
                shared = left_tokens & right_tokens
                union = left_tokens | right_tokens
                similarity = len(shared) / len(union) if union else 1.0
                if len(shared) >= MIN_SHARED_TOKENS and similarity >= SIMILARITY_LIMIT:
                    errors.append(
                        f"{plugin}: Descriptions von {left.slug} und {right.slug} "
                        f"sind zu aehnlich ({similarity:.2f}; gemeinsam: {', '.join(sorted(shared))})"
                    )

    descriptions: dict[str, list[Skill]] = {}
    bodies: dict[str, list[Skill]] = {}
    for skill in skills:
        descriptions.setdefault(skill.description.strip(), []).append(skill)
        digest = hashlib.sha256(skill_body(skill.path).encode("utf-8")).hexdigest()
        bodies.setdefault(digest, []).append(skill)

    for duplicate_group in descriptions.values():
        if len(duplicate_group) > 1:
            locations = ", ".join(
                f"{skill.plugin}/{skill.slug}" for skill in duplicate_group
            )
            errors.append(f"pluginuebergreifend identische Description: {locations}")

    for duplicate_group in bodies.values():
        if len(duplicate_group) > 1:
            locations = ", ".join(
                f"{skill.plugin}/{skill.slug}" for skill in duplicate_group
            )
            errors.append(
                "pluginuebergreifend identischer Skill-Body ohne Rollenprofil: "
                f"{locations}"
            )

    if errors:
        for error in errors:
            print(f"FEHLER: {error}", file=sys.stderr)
        print(f"validate-skill-discovery: {len(errors)} Fehler", file=sys.stderr)
        return 1

    print(f"validate-skill-discovery OK ({len(skills)} Skills, {len(plugins)} Plugins)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

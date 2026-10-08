#!/usr/bin/env python3
"""Consolidate oversized plugin skill sets into larger kompendium skills.

This is intentionally mechanical and conservative:
- keep essential entry/workflow skills and any skill directory that has extra files;
- keep Steuerrecht DBA skills as individual skills;
- merge the remaining SKILL.md bodies into longer kompendium skills;
- delete only source skill directories whose full markdown body was embedded.
"""

from __future__ import annotations

import argparse
import math
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Skill:
    plugin: str
    slug: str
    path: Path
    name: str
    description: str
    body: str
    has_extra_files: bool


PREFERRED_EXACT = {
    "allgemein": 0,
    "workflow-kaltstart-und-routing": 1,
    "workflow-dokumentenintake": 2,
    "workflow-unterlagen-lueckenliste": 3,
    "workflow-rechtsquellen-livecheck": 4,
    "workflow-output-waehlen": 5,
    "workflow-anschluss-skills-router": 6,
    "workflow-redteam-qualitygate": 7,
}

PREFERRED_PATTERNS = [
    (re.compile(r"(^|-)kaltstart($|-)"), 1),
    (re.compile(r"(^|-)dokumentenintake($|-)"), 2),
    (re.compile(r"(^|-)unterlagen($|-)"), 3),
    (re.compile(r"(^|-)rechtsquellen($|-)"), 4),
    (re.compile(r"(^|-)livequellen($|-)"), 4),
    (re.compile(r"(^|-)output($|-)"), 5),
    (re.compile(r"red-?team|qualitygate"), 7),
]


def parse_frontmatter(text: str) -> tuple[str, str, str]:
    if not text.startswith("---\n"):
        return "", "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", "", text
    raw = text[4:end]
    body = text[end + 5 :]
    name = ""
    description = ""
    for line in raw.splitlines():
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("description:"):
            description = line.split(":", 1)[1].strip().strip('"').strip("'")
    return name, description, body.lstrip("\n")


def yaml_string(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{value}"'


def natural_key(text: str) -> list[object]:
    parts: list[object] = []
    for part in re.split(r"(\d+)", text):
        if part.isdigit():
            parts.append(int(part))
        else:
            parts.append(part)
    return parts


def thematic_key(skill: Skill) -> tuple[str, list[object]]:
    s = skill.slug
    d = skill.description.lower()
    if "kaltstart" in s or s == "allgemein":
        bucket = "00-workflow"
    elif s.startswith("workflow-") or "workflow" in s:
        bucket = "01-workflow"
    elif "livequellen" in s or "rechtsquellen" in s or "rechtsprechung" in s:
        bucket = "02-quellen"
    elif s.startswith("staat-"):
        bucket = "03-staaten"
    elif s.startswith("jurisdiktion-"):
        bucket = "04-jurisdiktionen"
    elif "dba" in s:
        bucket = "05-dba"
    elif re.search(r"(^|-)lph\d+", s):
        bucket = "06-hoai-lph"
    elif "frist" in s or "zustaendigkeit" in s or "verfahren" in s:
        bucket = "07-verfahren"
    elif "vertrag" in s or "klausel" in s or "entwurf" in s:
        bucket = "08-vertrag"
    elif "haftung" in s or "schaden" in s or "bussgeld" in s or "sanktion" in s:
        bucket = "09-haftung"
    elif "steuer" in d or "abgabe" in d:
        bucket = "10-steuer"
    else:
        bucket = "99-fachkern"
    return bucket, natural_key(s)


def preferred_priority(skill: Skill) -> int | None:
    if skill.slug in PREFERRED_EXACT:
        return PREFERRED_EXACT[skill.slug]
    for pattern, score in PREFERRED_PATTERNS:
        if pattern.search(skill.slug):
            return score
    return None


def should_always_keep(skill: Skill) -> bool:
    if skill.has_extra_files:
        return True
    if skill.plugin == "steuerrecht-anwalt-und-berater" and "dba" in skill.slug.lower():
        return True
    return False


def load_skills(plugin_dir: Path) -> list[Skill]:
    skills_dir = plugin_dir / "skills"
    result: list[Skill] = []
    for skill_md in sorted(skills_dir.glob("*/SKILL.md"), key=lambda p: natural_key(p.parent.name)):
        text = skill_md.read_text(encoding="utf-8")
        name, description, body = parse_frontmatter(text)
        extra_files = [p for p in skill_md.parent.rglob("*") if p.is_file() and p.name != "SKILL.md"]
        result.append(
            Skill(
                plugin=plugin_dir.name,
                slug=skill_md.parent.name,
                path=skill_md,
                name=name or skill_md.parent.name,
                description=description or "(keine Beschreibung)",
                body=body,
                has_extra_files=bool(extra_files),
            )
        )
    return result


def chunked(skills: list[Skill], slots: int) -> list[list[Skill]]:
    if not skills:
        return []
    slots = max(1, slots)
    chunk_size = max(2, math.ceil(len(skills) / slots))
    return [skills[i : i + chunk_size] for i in range(0, len(skills), chunk_size)]


def aggregate_slug(index: int, group: list[Skill], existing: set[str]) -> str:
    first = re.sub(r"[^a-z0-9]+", "-", group[0].slug.lower()).strip("-")[:20]
    last = re.sub(r"[^a-z0-9]+", "-", group[-1].slug.lower()).strip("-")[:20]
    base = f"kompendium-{index:02d}-{first}-bis-{last}"
    base = re.sub(r"-+", "-", base).strip("-")
    slug = base[:90]
    n = 2
    while slug in existing:
        suffix = f"-{n}"
        slug = (base[: 90 - len(suffix)] + suffix).strip("-")
        n += 1
    existing.add(slug)
    return slug


def aggregate_text(plugin: str, index: int, slug: str, group: list[Skill]) -> str:
    title = f"Kompendium {index:02d} - {plugin}"
    examples = ", ".join(s.slug for s in group[:5])
    if len(group) > 5:
        examples += f" und {len(group) - 5} weitere"
    description = (
        f"{plugin}: Freistehendes verdichtetes Prüfprogramm {index:02d} für {len(group)} "
        f"zusammengehörige Fachfragen ({examples}); führt Workflows, Normanker, Prüfprogramme und Ausgabemuster ohne Entstehungsgeschichte zusammen."
    )
    lines: list[str] = [
        "---",
        f"name: {slug}",
        f"description: {yaml_string(description)}",
        "---",
        "",
        f"# {title}",
        "",
        "## Zweck",
        "",
        "Dieser Skill liefert ein freistehendes, vollständig ausformuliertes Prüf-, Workflow- und Ausgabeprogramm. Wähle den passenden Abschnitt nach Sachthema, Frist, Zuständigkeit, Beweisfrage oder gewünschtem Arbeitsprodukt und arbeite ihn in ganzen Sätzen ab.",
        "",
        "## Prüffelder und Arbeitsmodule",
        "",
        "| Prüffeld | Arbeitsauftrag |",
        "| --- | --- |",
    ]
    for skill in group:
        desc = skill.description.replace("|", "/").replace("\n", " ")
        lines.append(f"| `{skill.slug}` | {desc} |")
    lines.extend(
        [
            "",
            "## Arbeitsregel",
            "",
            "1. Zuerst den passenden Unterabschnitt anhand des Sachthemas, der Frist, der Zuständigkeit, der Beweisfrage oder des gewünschten Outputs auswählen.",
            "2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.",
            "3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.",
            "4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.",
            "",
            "## Konsolidierte Inhalte",
            "",
        ]
    )
    for idx, skill in enumerate(group, start=1):
        body = skill.body.strip()
        lines.extend(
            [
                f"## {idx}. `{skill.slug}`",
                "",
                f"Frühere Beschreibung: {skill.description}",
                "",
                body if body else "_Kein weiterer Body vorhanden._",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def consolidate_plugin(plugin_dir: Path, default_target: int, dry_run: bool) -> tuple[int, int, int]:
    skills = load_skills(plugin_dir)
    if len(skills) <= default_target:
        return len(skills), len(skills), 0

    target = 90 if plugin_dir.name == "steuerrecht-anwalt-und-berater" else default_target

    always = [s for s in skills if should_always_keep(s)]
    always_slugs = {s.slug for s in always}
    preferred_candidates = [s for s in skills if s.slug not in always_slugs and preferred_priority(s) is not None]
    preferred_candidates.sort(key=lambda s: (preferred_priority(s) or 99, natural_key(s.slug)))
    max_preferred = max(0, min(8, target - 1 - len(always)))
    keep = always + preferred_candidates[:max_preferred]
    keep_slugs = {s.slug for s in keep}

    remaining = [s for s in skills if s.slug not in keep_slugs]
    effective_target = max(target, len(keep) + 1)
    slots = max(1, effective_target - len(keep))
    remaining.sort(key=thematic_key)
    groups = chunked(remaining, slots)

    existing = {s.slug for s in keep}
    aggregate_items: list[tuple[str, str, list[Skill]]] = []
    for idx, group in enumerate(groups, start=1):
        slug = aggregate_slug(idx, group, existing)
        aggregate_items.append((slug, aggregate_text(plugin_dir.name, idx, slug, group), group))

    new_count = len(keep) + len(aggregate_items)
    if dry_run:
        return len(skills), new_count, len(remaining)

    for slug, text, _group in aggregate_items:
        target_dir = plugin_dir / "skills" / slug
        target_dir.mkdir(parents=True, exist_ok=False)
        (target_dir / "SKILL.md").write_text(text, encoding="utf-8")

    for skill in remaining:
        shutil.rmtree(skill.path.parent)

    return len(skills), new_count, len(remaining)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=int, default=30)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    plugin_dirs = []
    for skills_dir in ROOT.glob("*/skills"):
        plugin_dir = skills_dir.parent
        if (plugin_dir / ".claude-plugin" / "plugin.json").exists() or (
            plugin_dir / ".codex-plugin" / "plugin.json"
        ).exists():
            plugin_dirs.append(plugin_dir)

    total_before = total_after = total_merged = 0
    changed = 0
    for plugin_dir in sorted(plugin_dirs, key=lambda p: p.name):
        before, after, merged = consolidate_plugin(plugin_dir, args.target, args.dry_run)
        total_before += before
        total_after += after
        total_merged += merged
        if before != after:
            changed += 1
            print(f"{plugin_dir.name}: {before} -> {after} (merged {merged})")
    print(f"plugins_changed={changed}")
    print(f"skills_before={total_before}")
    print(f"skills_after={total_after}")
    print(f"skills_merged_into_kompendien={total_merged}")


if __name__ == "__main__":
    main()

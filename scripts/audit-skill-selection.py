#!/usr/bin/env python3
"""Prüft Auswahlkonflikte und die Ziele dokumentierter Skill-Umstellungen."""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import unicodedata

import yaml


REPO = Path(__file__).resolve().parents[1]
MIGRATIONS = REPO / "scripts" / "skill-selection-migrations.json"
SLUG = re.compile(r"[a-z0-9-]{1,64}\Z")
INVOCATION = re.compile(r"/([a-z0-9-]+):([a-z0-9-]+)")


def invocation_corrections(text: str, available: dict[str, set[str]]) -> dict[str, str]:
    corrections = {}
    for match in INVOCATION.finditer(text):
        plugin, name = match.groups()
        names = available.get(plugin, set())
        prefix = plugin + "-"
        if name not in names and name.startswith(prefix) and name[len(prefix):] in names:
            corrections[match[0]] = f"/{plugin}:{name[len(prefix):]}"
    return corrections


def heading_key(title: str) -> str:
    title = unicodedata.normalize("NFKC", title).casefold()
    title = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", title)
    return " ".join(re.findall(r"\w+", title))


def skill_metadata(path: Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("Frontmatter fehlt")
    data = yaml.safe_load(match[1])
    if not isinstance(data, dict):
        raise ValueError("Frontmatter ist keine Zuordnung")
    title = re.search(r"^#\s+(.+)$", text[match.end():], re.M)
    if not title:
        raise ValueError("Hauptüberschrift fehlt")
    return str(data.get("name", "")), str(data.get("description", "")), title[1].strip()


def inspect_plugin(directory: Path) -> dict:
    titles: dict[str, list[str]] = defaultdict(list)
    names: dict[str, list[str]] = defaultdict(list)
    errors = []
    metadata_chars = 0
    files = sorted((directory / "skills").glob("*/SKILL.md"))
    for path in files:
        try:
            name, description, title = skill_metadata(path)
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"{path.parent.name}: {exc}")
            continue
        if not SLUG.fullmatch(name) or name != path.parent.name:
            errors.append(f"{path.parent.name}: ungültiger oder abweichender Name {name!r}")
        names[name].append(path.parent.name)
        titles[heading_key(title)].append(name)
        metadata_chars += len(name) + len(description)
    for name, paths in names.items():
        if len(paths) > 1:
            errors.append(f"{name}: mehrfacher Aufrufname")
    return {
        "plugin": directory.name,
        "skills": len(files),
        "metadata_chars": metadata_chars,
        # Eine gemeinsame Überschrift ist ein Prüfanlass, kein Löschbeweis.
        "same_title_groups": [group for group in titles.values() if len(group) > 1],
        "errors": errors,
    }


def validate_migrations(repo: Path, migrations: list[dict]) -> list[str]:
    errors = []
    seen = set()
    for migration in migrations:
        plugin = migration.get("plugin", "")
        old = migration.get("old", "")
        new = migration.get("new", "")
        if not all(isinstance(value, str) and SLUG.fullmatch(value) for value in (plugin, old, new)):
            errors.append(f"Ungültige Umstellung: {migration!r}")
            continue
        key = (plugin, old)
        if key in seen:
            errors.append(f"{plugin}/{old}: mehrfaches Umstellungsziel")
        seen.add(key)
        root = repo / plugin / "skills"
        if old == new:
            errors.append(f"{plugin}/{old}: Umstellung zeigt auf sich selbst")
        elif (root / old / "SKILL.md").exists():
            errors.append(f"{plugin}/{old}: alter Auswahlpunkt wurde wieder eingeführt")
        target = root / new / "SKILL.md"
        if not target.is_file():
            errors.append(f"{plugin}/{old}: Ziel {new} fehlt")
        reference = migration.get("reference")
        if reference:
            base = (root / new).resolve()
            resolved = (base / reference).resolve()
            if not resolved.is_relative_to(base) or not resolved.is_file():
                errors.append(f"{plugin}/{old}: Vertiefung fehlt oder liegt außerhalb des Zielskills")
            elif not reference_reachable(target, resolved):
                errors.append(f"{plugin}/{old}: Vertiefung ist vom Zielskill nicht verlinkt")
    return errors


def reference_reachable(start: Path, target: Path) -> bool:
    root = start.parent.resolve()
    pending = [start.resolve()]
    seen = set()
    while pending:
        path = pending.pop()
        if path == target:
            return True
        if path in seen or not path.is_file():
            continue
        seen.add(path)
        for raw in re.findall(r"\]\(([^)\s]+)\)", path.read_text(encoding="utf-8")):
            if "://" in raw:
                continue
            linked = (path.parent / raw.partition("#")[0]).resolve()
            if linked.is_relative_to(root) and linked.suffix == ".md":
                pending.append(linked)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Ausführlicher Befund zur individuellen Prüfung")
    args = parser.parse_args()
    marketplace = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text())
    reports = [inspect_plugin(REPO / entry["source"]) for entry in marketplace["plugins"]]
    migrations = json.loads(MIGRATIONS.read_text(encoding="utf-8"))
    errors = [f"{report['plugin']}: {error}" for report in reports for error in report["errors"]]
    errors += validate_migrations(REPO, migrations)
    available = {}
    for entry in marketplace["plugins"]:
        directory = REPO / entry["source"]
        available[entry["name"]] = {p.parent.name for p in (directory / "skills").glob("*/SKILL.md")}
        available[entry["name"]].update(p.stem for p in (directory / "commands").glob("*.md"))
    for entry in marketplace["plugins"]:
        directory = REPO / entry["source"]
        for path in directory.rglob("*.md"):
            if any(part in {"testakte", "testakten"} for part in path.relative_to(directory).parts):
                continue
            corrections = invocation_corrections(path.read_text(encoding="utf-8"), available)
            for old, new in corrections.items():
                errors.append(f"{path.relative_to(REPO)}: nicht vorhandener Aufruf {old}; Ziel {new}")
    duplicate_count = sum(len(group) - 1 for report in reports for group in report["same_title_groups"])
    if args.json:
        print(json.dumps({"plugins": reports, "migration_errors": errors}, ensure_ascii=False, indent=2))
    else:
        print(f"Auswahlprüfung: {len(reports)} Plugins, {sum(r['skills'] for r in reports)} Skills")
        print(f"{len(migrations)} Umstellungen geprüft; {duplicate_count} weitere gleichnamige Titel zur fachlichen Prüfung")
        for report in sorted(reports, key=lambda r: (-len(r["same_title_groups"]), r["plugin"]))[:10]:
            print(f"- {report['plugin']}: {report['skills']} Skills, {len(report['same_title_groups'])} Titelgruppen")
        for error in errors:
            print(f"FEHLER: {error}")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())

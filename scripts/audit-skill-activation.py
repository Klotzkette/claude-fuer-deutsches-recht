#!/usr/bin/env python3
"""Prüft, ob Skill-Beschreibungen als Auswahlsignale taugen."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DUPLICATE_TITLE_RE = re.compile(r"^([^:]{3,90}):\s*\1:", re.IGNORECASE)
COMMA_NUMBER_RE = re.compile(r"\d\s*,\s*\d")
XML_TAG_RE = re.compile(r"<[a-zA-Z]")
MIN_DESCRIPTION_CHARS = 80
MAX_DESCRIPTION_CHARS = 360


def skill_files(repo: Path | None = None) -> list[Path]:
    """Prüft aktive Auswahl; nur ausdrücklich erklärte Quellarchive ausnehmen."""
    repo = (repo or REPO).resolve()
    marketplace = json.loads((repo / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    active = {}
    for row in marketplace["plugins"]:
        name, source = row["name"], row["source"]
        if not isinstance(source, str) or not source.startswith("./"):
            raise ValueError(f"{name}: ungültige Marketplace-Quelle")
        directory = (repo / source).resolve()
        if not directory.is_relative_to(repo) or directory == repo or not directory.is_dir():
            raise ValueError(f"{name}: Marketplace-Quelle fehlt oder verlässt Repository")
        if name in active or directory in active.values():
            raise ValueError(f"{name}: doppelte Marketplace-Zuordnung")
        active[name] = directory
    archives = set()
    registry = repo / "scripts/plugin-consolidations.json"
    if registry.is_file():
        data = json.loads(registry.read_text(encoding="utf-8"))
        if (not isinstance(data, dict) or data.get("schema_version") != 1
                or not isinstance(data.get("consolidations"), list)):
            raise ValueError("Ungültiges Plugin-Zusammenführungsregister")
        for row in data["consolidations"]:
            if not isinstance(row, dict):
                raise ValueError("Ungültige Quellarchiv-Zuordnung")
            old, new = row.get("legacy"), row.get("canonical")
            if (not isinstance(old, str) or not re.fullmatch(r"[a-z0-9-]+", old)
                    or row.get("legacy_status") != "retained_source_archive"
                    or old in active or new not in active or old == new):
                raise ValueError(f"Ungültiges Quellarchiv: {old!r}")
            directory = repo / old
            if (directory.is_symlink() or not directory.is_dir() or directory in archives
                    or directory in active.values()):
                raise ValueError(f"Fehlendes, doppeltes oder verlinktes Quellarchiv: {old}")
            manifest = directory / ".claude-plugin/plugin.json"
            if (manifest.parent.is_symlink() or manifest.is_symlink()
                    or json.loads(manifest.read_text(encoding="utf-8")).get("name") != old):
                raise ValueError(f"Quellarchiv-Manifest passt nicht zu {old}")
            archives.add(directory)
    files = []
    for file in sorted(repo.rglob("SKILL.md")):
        if ".git" in file.parts or "node_modules" in file.parts:
            continue
        if any(file.is_relative_to(directory) for directory in archives):
            continue
        if not any(file.is_relative_to(directory / "skills") for directory in active.values()):
            raise ValueError(f"Skill ohne aktives Plugin oder deklariertes Quellarchiv: {file.relative_to(repo)}")
        files.append(file)
    return files


def description(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return ""
    frontmatter = text.split("---", 2)[1]
    for line in frontmatter.splitlines():
        if line.startswith("description:"):
            value = line.split(":", 1)[1].strip()
            if len(value) >= 2 and value[0] in {"'", '"'} and value[-1] == value[0]:
                value = value[1:-1]
            return value
    return ""


def owner(path: Path) -> str:
    parts = path.relative_to(REPO).parts
    if "skills" not in parts:
        return path.parent.parent.as_posix()
    return Path(*parts[: parts.index("skills")]).as_posix()


def main() -> int:
    try:
        descriptions: list[tuple[Path, str]] = [(p, description(p)) for p in skill_files()]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FEHLER: {exc}")
        return 1
    by_description: dict[str, list[Path]] = defaultdict(list)
    for path, desc in descriptions:
        if desc:
            by_description[desc].append(path)

    counters = Counter()
    examples: dict[str, list[tuple[Path, str]]] = defaultdict(list)
    for path, desc in descriptions:
        checks = {
            "leer": not desc,
            "unter_80": len(desc) < MIN_DESCRIPTION_CHARS,
            "ueber_360": len(desc) > MAX_DESCRIPTION_CHARS,
            "doppelte_beschreibung": len(by_description.get(desc, [])) > 1,
            "doppelter_titel": bool(DUPLICATE_TITLE_RE.search(desc)),
            "baustein_fachlich_vertieft": "fachlich vertieftes Modul" in desc,
            "plugin_floksel": "im Plugin" in desc or "-Plugin" in desc,
            "paragrafzeichen": chr(167) in desc,
            "xml_tag": bool(XML_TAG_RE.search(desc)),
            "zahl_komma_zahl": bool(COMMA_NUMBER_RE.search(desc)),
        }
        for key, hit in checks.items():
            if hit:
                counters[key] += 1
                if len(examples[key]) < 8:
                    examples[key].append((path.relative_to(REPO), desc[:220]))

    print(f"Skill-Dateien: {len(descriptions)}")
    for key in sorted(counters):
        print(f"{key}: {counters[key]}")

    owner_hits = Counter()
    for desc, paths in by_description.items():
        if desc and len(paths) > 1:
            for path in paths:
                owner_hits[owner(path)] += 1
    if owner_hits:
        print("\nPlugins mit vielen gleichen Beschreibungen:")
        for plugin, count in owner_hits.most_common(20):
            print(f"- {plugin}: {count}")

    print("\nBeispiele:")
    for key in sorted(examples):
        print(f"\n## {key}")
        for path, desc in examples[key]:
            print(f"- {path}: {desc}")
    if counters:
        return 1
    print("\nOK: Skill-Beschreibungen haben ausreichende Auswahlsignale.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

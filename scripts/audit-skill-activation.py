#!/usr/bin/env python3
"""Prüft, ob Skill-Beschreibungen als Auswahlsignale taugen."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DUPLICATE_TITLE_RE = re.compile(r"^([^:]{3,90}):\s*\1:", re.IGNORECASE)
COMMA_NUMBER_RE = re.compile(r"\d\s*,\s*\d")
XML_TAG_RE = re.compile(r"<[a-zA-Z]")
MIN_DESCRIPTION_CHARS = 80
MAX_DESCRIPTION_CHARS = 360


def skill_files() -> list[Path]:
    return sorted(
        p
        for p in REPO.rglob("SKILL.md")
        if ".git" not in p.parts and "node_modules" not in p.parts
    )


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
    descriptions: list[tuple[Path, str]] = [(p, description(p)) for p in skill_files()]
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

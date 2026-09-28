"""Gemeinsame Publikationsprofile für Begleitprompts, nicht für Skills.

Ohne explizites Profil bleibt die bisherige Veröffentlichung unverändert:
Werkstatt und Schnellstart als Markdown, Schwerpunkt optional, Megaprompt.
MD bleibt die redaktionelle Quelle; TXT ist eine unveränderte UTF-8-Kopie.
"""

from __future__ import annotations

import json
from pathlib import Path

CONFIG = Path(__file__).with_name("prompt-profiles.json")
KINDS = ("werkstatt", "schnellstart", "hauptproblem")
FORMATS = ("md", "txt", "docx", "pdf")
PROMPT_SUFFIXES = tuple(f"-{kind}.{ext}" for kind in KINDS for ext in FORMATS)


def load_profiles(path: Path = CONFIG) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not isinstance(data.get("plugins"), dict):
        raise ValueError("Ungültige Promptprofil-Konfiguration")
    for slug, profile in data["plugins"].items():
        if not isinstance(profile, dict) or set(profile) != {"standalone", "formats", "megaprompt", "hand_curated"}:
            raise ValueError(f"{slug}: unvollständiges Promptprofil")
        for key, allowed in (("standalone", KINDS), ("formats", ("md", "txt"))):
            values = profile[key]
            if not isinstance(values, list) or not values or len(values) != len(set(values)) or not set(values) <= set(allowed):
                raise ValueError(f"{slug}: ungültiges Feld {key}")
        if "md" not in profile["formats"] or any(type(profile[key]) is not bool for key in ("megaprompt", "hand_curated")):
            raise ValueError(f"{slug}: Markdown-Quelle oder boolescher Schalter fehlt")
    return data["plugins"]


PROFILES = load_profiles()


def enabled(slug: str, kind: str) -> bool:
    profile = PROFILES.get(slug)
    if kind == "megaprompt":
        return profile is None or profile["megaprompt"]
    return kind in (profile["standalone"] if profile else KINDS)


def standalone_kinds(slug: str) -> tuple[str, ...]:
    """Pflichtdateien; bestehende Schwerpunktdateien bleiben optional."""
    return tuple(PROFILES[slug]["standalone"]) if slug in PROFILES else KINDS[:2]


def formats(slug: str) -> tuple[str, ...]:
    return tuple(PROFILES[slug]["formats"]) if slug in PROFILES else ("md",)


def hand_curated(slug: str) -> bool:
    return bool(PROFILES.get(slug, {}).get("hand_curated"))


def sync_text_copies(directory: Path, slug: str) -> None:
    if "txt" in formats(slug):
        for kind in standalone_kinds(slug):
            source = directory / f"{slug}-{kind}.md"
            (directory / f"{slug}-{kind}.txt").write_bytes(source.read_bytes())


def validate_files(directory: Path, slug: str, root: Path) -> list[str]:
    """Prüft explizite Profile einschließlich unerwünschter Derivate."""
    if slug not in PROFILES:
        return []
    errors = []
    expected = {f"{slug}-{kind}.{ext}" for kind in standalone_kinds(slug) for ext in formats(slug)}
    for name in sorted(expected):
        path = directory / name
        if not path.is_file() or not path.stat().st_size:
            errors.append(f"{slug}: Prompt fehlt oder ist leer: {name}")
    for path in directory.iterdir():
        if path.is_file() and path.name.endswith(PROMPT_SUFFIXES) and path.name not in expected:
            errors.append(f"{slug}: Prompt laut Profil nicht vorgesehen: {path.name}")
    for kind in standalone_kinds(slug):
        md, txt = (directory / f"{slug}-{kind}.{ext}" for ext in ("md", "txt"))
        if "txt" in formats(slug) and md.is_file() and txt.is_file() and md.read_bytes() != txt.read_bytes():
            errors.append(f"{slug}: TXT und Markdown sind nicht byteidentisch: {kind}")
    if not enabled(slug, "megaprompt") and (root / "testakten/megaprompts" / f"{slug}.md").exists():
        errors.append(f"{slug}: Megaprompt laut Profil nicht vorgesehen")
    return errors

"""Quellpfade erhaltener Fachmodule nach der expliziten Skill-Konsolidierung.

Aktive Skills werden weiterhin ausschließlich über skills/*/SKILL.md ermittelt.
Dieser Resolver ist für fachliche Inhaltsprüfungen und Dokumentationsbuilder,
die einen bestimmten bisherigen Fachtext lesen müssen. Er erzeugt keine
Skill-Aliase und akzeptiert kein beliebiges FACHINHALT.md als Ersatz.
"""
from __future__ import annotations
from functools import lru_cache
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'scripts/data/skill-cap-registry.json'

def replacements():
    """Ausdrücklich redaktionell ersetzte Bestände; kein stiller Alias auf Altrecht."""
    path = ROOT / 'scripts/data/skill-source-replacements.json'
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('schema_version') != 1:
        raise ValueError('Unbekannte Fassung des Fachquellen-Ersatzregisters')
    return data['plugins']

@lru_cache(maxsize=1)
def registry():
    return json.loads(REGISTRY.read_text(encoding='utf-8'))['plugins']

@lru_cache(maxsize=1)
def moved_sources():
    return {
        (ROOT / plugin['source'] / 'skills' / member / 'SKILL.md').resolve():
        (ROOT / plugin['source'] / 'skills' / member / 'FACHINHALT.md').resolve()
        for plugin in registry() for route in plugin['routes'] for member in route['members']
    }

def fachinhalt_path(path: Path) -> Path:
    """Liefert nur einen vorhandenen oder explizit zugeordneten Fachquellpfad."""
    path=Path(path)
    if path.is_file():
        return path
    target=moved_sources().get(path.resolve())
    if target is None or not target.is_file():
        raise FileNotFoundError(f'Fachquelle fehlt oder ist nicht zugeordnet: {path}')
    return target

def original_skill_sources(directory: Path) -> list[Path]:
    """Alle ursprünglichen Fachtexte, keine zusätzlich erzeugten Sammelrouter."""
    directory=Path(directory).resolve()
    replacement = replacements().get(directory.name)
    if replacement is not None and directory == (ROOT / replacement['source']).resolve():
        active = sorted((directory/'skills').glob('*/SKILL.md'))
        if {path.parent.name for path in active} != set(replacement['active_skills']):
            raise ValueError(f'Aktiver Fachbestand weicht vom geprüften Ersatzregister ab: {directory.name}')
        return active
    plugin=next((p for p in registry() if (ROOT / p['source']).resolve()==directory),None)
    if plugin is None:
        return sorted((directory/'skills').glob('*/SKILL.md'))
    names=plugin['keep']+[member for route in plugin['routes'] for member in route['members']]
    return [fachinhalt_path(directory/'skills'/slug/'SKILL.md') for slug in sorted(names)]

def active_owner(directory: Path, original_slug: str) -> str:
    directory=Path(directory).resolve()
    plugin=next((p for p in registry() if (ROOT / p['source']).resolve()==directory),None)
    if plugin:
        for route in plugin['routes']:
            if original_slug in route['members']:
                if not (directory/'skills'/route['slug']/'SKILL.md').is_file():
                    raise FileNotFoundError(f"Zugeordneter aktiver Skill fehlt: {directory.name}/{route['slug']}")
                return route['slug']
    if not (directory/'skills'/original_slug/'SKILL.md').is_file():
        raise FileNotFoundError(f'Aktiver Skill fehlt: {directory.name}/{original_slug}')
    return original_slug

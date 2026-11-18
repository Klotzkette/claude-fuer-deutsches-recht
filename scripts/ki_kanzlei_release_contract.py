"""Aktive Arbeitswege und vollständig erhaltene Fachmodule getrennt prüfen."""
from pathlib import Path
from skill_sources import registry, original_skill_sources
from skill_limits import MAX_ACTIVE_SKILLS_PER_PLUGIN

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "ki-native-kanzlei"
_SPEC = next(p for p in registry() if p["name"] == "ki-native-kanzlei")
ACTIVE_SKILL_SLUGS = frozenset(_SPEC["keep"] + [r["slug"] for r in _SPEC["routes"]])
ACTIVE_SKILL_COUNT = len(ACTIVE_SKILL_SLUGS)
MODULE_COUNT = 30
MODULE_SLUGS = frozenset(_SPEC["keep"] + [m for r in _SPEC["routes"] for m in r["members"]])
assert len(MODULE_SLUGS) == MODULE_COUNT
assert ACTIVE_SKILL_COUNT <= MAX_ACTIVE_SKILLS_PER_PLUGIN

def module_sources():
    paths = original_skill_sources(PLUGIN)
    assert {p.parent.name for p in paths} == MODULE_SLUGS
    return paths

VERSION = '445.36.0'
PRODUCT_SKILLS = {
    'akte-chronologie-beweismittel', 'anspruch-berechnen-beziffern',
    'dokumente-erstellen-formatieren', 'anlagen-ordnen-abgleichen',
    'schriftsatz-ueberarbeiten-erwidern', 'gerichtstermin-vorbereiten-nachbereiten',
    'vergleich-verhandeln-formulieren', 'gerichtskosten-kostenerstattung',
    'titel-pruefen-vollstreckung-planen', 'mandatswissen-vorlagen-pflegen',
}


def minimum_pages(skill):
    if skill in PRODUCT_SKILLS:
        return 2
    if skill in {'kanzlei-gruenden-einrichten', 'posteingang-mandate-zuordnen'}:
        return 3
    return 10


def validate_module_report(report):
    """Ein kurzer Router ersetzt weder einen Fachtext noch dessen PDF-Mindestumfang."""
    assert report['schema_version'] == 2, 'Lesefassungen nach der Skill-Neuordnung neu erzeugen'
    assert report['version'] == VERSION, 'Lesefassung gehört nicht zur Komponentenfassung'
    assert report['module_count'] == MODULE_COUNT
    assert report['active_skill_count'] == ACTIVE_SKILL_COUNT
    assert set(report['active_skills']) == ACTIVE_SKILL_SLUGS
    rows = report['modules']
    assert len(rows) == MODULE_COUNT
    assert {r['skill'] for r in rows} == MODULE_SLUGS
    assert all(r['pages'] >= minimum_pages(r['skill']) for r in rows)
    assert report['total_module_pages'] == sum(r['pages'] for r in rows)
    if 'handbook_pages' in report:
        assert report['navigation_pages'] >= 1
        assert report['handbook_pages'] == report['total_module_pages'] + report['navigation_pages']
    return rows

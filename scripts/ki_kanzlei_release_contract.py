"""Gemeinsamer Umfangsvertrag; bestehende Mindestumfänge bleiben unverändert."""
VERSION = '445.35.0'
SKILL_COUNT = 30
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

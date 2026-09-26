"""Gemeinsame Zuordnung der neun eigenständigen Gebäude-Phasenpakete."""

PHASEN = (
    (1, "Grundlagenermittlung", "hoai-1-grundlagen-und-planungsauftrag-klaeren",
     "bauwirtschaft-hoai-1-grundlagen-kulturhof-detmold",
     "Aufgabenklärung, Ortsbesichtigung und Untersuchungsbedarf für einen Kulturhof."),
    (2, "Vorplanung", "hoai-2-vorplanung-und-varianten-entwickeln",
     "bauwirtschaft-hoai-2-vorplanung-kita-bad-pyrmont",
     "Vergleichbare Kita-Varianten, Kostenschätzung und Entscheidung des Bauherrn."),
    (3, "Entwurfsplanung", "hoai-3-entwurf-und-kostenberechnung-abstimmen",
     "bauwirtschaft-hoai-3-entwurf-aerztehaus-stadthagen",
     "Abgestimmter Entwurf, Fachplanerbeiträge und Kostenberechnung für ein Ärztehaus."),
    (4, "Genehmigungsplanung", "hoai-4-genehmigungsplanung-und-nachforderungen-bearbeiten",
     "bauwirtschaft-hoai-4-genehmigung-werkhof-celle",
     "Bauantragsunterlagen, Nachforderungen und Einreichungsstand eines Werkhofs."),
    (5, "Ausführungsplanung", "hoai-5-ausfuehrungsplanung-und-details-koordinieren",
     "bauwirtschaft-hoai-5-ausfuehrung-schule-hameln",
     "Ausführungsreife Details, Planrevisionen und Schnittstellen beim Schulumbau."),
    (6, "Vorbereitung der Vergabe", "hoai-6-leistungsverzeichnis-und-vergabeunterlagen-erstellen",
     "bauwirtschaft-hoai-6-lv-sporthalle-peine",
     "Mengen, Leistungsbeschreibungen und Ausschreibungsunterlagen einer Sporthalle."),
    (7, "Mitwirkung bei der Vergabe", "hoai-7-angebote-werten-und-vergabe-vorbereiten",
     "bauwirtschaft-hoai-7-vergabe-bibliothek-melle",
     "Angebotsprüfung, Preisspiegel und begründeter Vergabevorschlag für eine Bibliothek."),
    (8, "Objektüberwachung und Dokumentation", "hoai-8-bauueberwachung-und-dokumentation-fuehren",
     "bauwirtschaft-hoai-8-bauueberwachung-kita-verden",
     "Baustellenstand, Aufmaß, Rechnungen und Abnahmeunterlagen beim Kita-Neubau."),
    (9, "Objektbetreuung", "hoai-9-objektbetreuung-und-maengelverfolgung-organisieren",
     "bauwirtschaft-hoai-9-objektbetreuung-rathaus-uelzen",
     "Spätere Mängel, Begehung vor Fristablauf und Sicherheiten am Rathaus."),
)


def werkstatt_path(phase: int) -> str:
    return f"bauwirtschaft/bauwirtschaft-hoai-{phase}-werkstatt.md"

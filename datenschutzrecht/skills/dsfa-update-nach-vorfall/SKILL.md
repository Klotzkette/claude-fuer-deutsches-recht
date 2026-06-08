---
name: dsfa-update-nach-vorfall
description: "Aktualisiert die Datenschutz-Folgenabschätzung nach Art. 35 DSGVO im Nachgang eines Datenschutzvorfalls. Behandelt: Erforderlichkeit der DSFA bei voraussichtlich hohem Risiko; Anpassung der Risikoanalyse; Abhilfemaßnahmen; Konsultation der Aufsichtsbehörde nach Art. 36 DSGVO bei verbleibendem hohem Risiko; Verknüpfung mit VVT und Vorfallregister. Output: DSFA-Update-Vorlage mit Pflichtfeldern. Abgrenzung: keine neue DSFA; kein Verfahrensverzeichnis."
---

# Datenschutz-Folgenabschätzung nach Datenschutzvorfall aktualisieren

## Triage — kläre vor der Bearbeitung

1. Gab es bisher eine DSFA für die betroffene Verarbeitung?
2. Welche Risiken haben sich realisiert oder offenbart?
3. Welche Abhilfemaßnahmen sind nachhaltig wirksam?
4. Bleibt nach Maßnahmen ein hohes Risiko bestehen?
5. Ist Konsultation Art. 36 DSGVO erforderlich?
- Was will der Mandant wirklich erreichen? (rechtskonforme Fortführung der Verarbeitung; Behördenkonsens)

## Rechtsgrundlagen

- **Art. 35 DSGVO** DSFA.
- **Art. 36 DSGVO** vorherige Konsultation.
- **Art. 32 DSGVO** TOM.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **BfDI- und LDA-DSFA-Listen** (Black- und Whitelist).

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Anforderungen an die DSFA-Aktualisierung nach Vorfall vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 32; Art. 35; Art. 36 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — DSFA-Update-Felder

1. Beschreibung der Verarbeitung mit Bezug auf VVT.
2. Bewertung der Notwendigkeit und Verhältnismäßigkeit.
3. Bewertung der Risiken — vorher und nachher.
4. Geplante Maßnahmen — vor und nach Vorfall.
5. Konsultation der Aufsichtsbehörde nach Art. 36 DSGVO erforderlich ja/nein mit Begründung.
6. Stellungnahme des Datenschutzbeauftragten.
7. Versionsstand mit Datum und Bearbeiter.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-vvt-update-nach-vorfall` deckt das VVT ab.

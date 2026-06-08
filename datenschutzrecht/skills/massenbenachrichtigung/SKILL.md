---
name: massenbenachrichtigung
description: "Steuert die Massenbenachrichtigung tausender oder Millionen Betroffener nach Art. 34 DSGVO. Behandelt: Versandlogistik E-Mail-Welle; Brief-Welle; Push und SMS; Adressqualität; Bounces; Sprachvarianten; Hotline-Dimensionierung; Pressewelle; Hilfsdienste wie Schufa-Auskunft. Output: Versandplan, Skalierungsraster, Q&A-Matrix. Abgrenzung: keine individuelle Benachrichtigung; keine Behördenmeldung."
---

# Massenbenachrichtigung bei großem Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Adressdaten liegen in welcher Qualität vor?
2. Welche Sprachen müssen abgedeckt werden?
3. Welche Hotline-Kapazität ist erforderlich?
4. Welche Versanddienstleister sind vertraglich gebunden?
5. Welche regulatorischen Anforderungen an Massenversand bestehen (E-Privacy)?
- Was will der Mandant wirklich erreichen? (zuverlässige Erreichung der Betroffenen; saubere Logistik)

## Rechtsgrundlagen

- **Art. 34 Abs. 1 DSGVO** Benachrichtigung.
- **Art. 34 Abs. 2 DSGVO** Pflichtinhalte.
- **Art. 12 Abs. 1 DSGVO** klare einfache Sprache.
- **§ 7 UWG** Werbung im Geschäftsverkehr (nicht anwendbar auf Pflichtinformation).
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Sammelklagen nach Massendatenpannen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 12 Abs. 1; Art. 34 Abs. 1; Art. 34 Abs. 2; Art. 5 Abs. 2 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Versandplan

Welle 1: E-Mail an alle Adressaten mit valider E-Mail-Adresse — Versand über DSGVO-konformen Dienstleister; Bounce-Handling automatisiert.

Welle 2: Brief an alle Adressaten ohne E-Mail oder mit Bounce — innerhalb von sieben Tagen.

Welle 3: öffentliche Bekanntmachung über Webseite und Pressemeldung — als Auffangnetz.

Hotline: 24/7 in der ersten Woche; 8-20 Uhr ab Woche zwei; mehrsprachig.

Q&A-Matrix: 20-30 Fragen mit abgestimmten Antworten.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-pressemitteilung-krisenkommunikation` deckt Pressekommunikation ab.

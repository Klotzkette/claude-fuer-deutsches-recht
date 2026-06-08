---
name: risikobewertung-schwellen-art-33-34
description: "Strukturiert die Schwellenwertentscheidung nach Art. 33 und Art. 34 DSGVO als anwaltlichen Entscheidungsbaum. Behandelt: voraussichtlich-kein-Risiko-Schwelle Art. 33 Abs. 1; Meldeschwelle; voraussichtlich-hohes-Risiko Art. 34 Abs. 1; Ausnahmen Art. 34 Abs. 3 (technische Schutzmaßnahmen, nachträgliche Risikominderung, unverhältnismäßiger Aufwand); EDSA-Auslegung; deutsche Praxis. Output: Entscheidungsbaum mit Begründungstexten für jede Verzweigung. Abgrenzung: keine konkrete Meldung; keine ENISA-Quantifizierung."
---

# Schwellenwerte Art. 33 und Art. 34 DSGVO — Entscheidungsbaum

## Triage — kläre vor der Bearbeitung

1. Liegt überhaupt eine Verletzung des Schutzes personenbezogener Daten nach Art. 4 Nr. 12 DSGVO vor?
2. Welche Wahrscheinlichkeit eines Risikos für Rechte und Freiheiten besteht?
3. Welche Schwere des Risikos ist plausibel?
4. Greift eine Ausnahme nach Art. 34 Abs. 3 DSGVO?
5. Welche Begründung trägt die Behörde wahrscheinlich mit?
- Was will der Mandant wirklich erreichen? (sichere Entscheidung; nachprüfbare Begründung)

## Rechtsgrundlagen

- **Art. 4 Nr. 12 DSGVO** Definition Verletzung.
- **Art. 33 Abs. 1 DSGVO** Meldeschwelle.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigungsschwelle.
- **Art. 34 Abs. 3 DSGVO** Ausnahmen.
- **Erwägungsgrund 75; 76; 85; 86 DSGVO**.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Auslegung Art. 34 Abs. 3 lit. a DSGVO (Verschlüsselung) und lit. c (unverhältnismäßiger Aufwand) vor Ausgabe verifizieren.

## Zentrale Normen

Art. 4 Nr. 12; Art. 33 Abs. 1; Art. 34 Abs. 1; Art. 34 Abs. 3 DSGVO; Erwägungsgrund 75; 76; 85; 86.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Entscheidungsbaum

Frage 1: Verletzung im Sinne Art. 4 Nr. 12? Nein → Dokumentation reicht. Ja → Frage 2.

Frage 2: Voraussichtlich kein Risiko? Ja → keine Meldung; Dokumentation Art. 33 Abs. 5. Nein → Meldung Art. 33.

Frage 3: Voraussichtlich hohes Risiko? Nein → keine Benachrichtigung. Ja → Frage 4.

Frage 4: Art. 34 Abs. 3 DSGVO Ausnahme? Ja → öffentliche Bekanntmachung statt individueller Benachrichtigung. Nein → individuelle Benachrichtigung.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-risikobewertung-edsa-leitlinie` und `dsv-risikobewertung-enisa-schweregrad` liefern die methodische Tiefe.

---
name: dsv-vvt-update-nach-vorfall
description: "Steuert die Aktualisierung des Verzeichnisses von Verarbeitungstätigkeiten nach Art. 30 DSGVO im Nachgang eines Datenschutzvorfalls. Behandelt: Identifikation der betroffenen Verarbeitungen; Anpassung der technischen und organisatorischen Maßnahmen; neue Risikoeinschätzung; Auftragsverarbeiter-Update; Aufbewahrungsfristen; Verknüpfung mit Vorfallregister Art. 33 Abs. 5. Output: Update-Checkliste mit Pflichtfeldern. Abgrenzung: kein neues VVT; keine DSFA."
---

# Aktualisierung des Verfahrensverzeichnisses nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche VVT-Einträge sind durch den Vorfall berührt?
2. Welche TOM müssen aktualisiert werden?
3. Sind neue Auftragsverarbeiter hinzugekommen (Forensiker, Hotline)?
4. Welche Aufbewahrungsfristen ändern sich (Logs, Vorfallakten)?
5. Wer pflegt das VVT und genehmigt die Änderung?
- Was will der Mandant wirklich erreichen? (Rechenschaftspflicht erfüllen; Bußgeldverteidigung; saubere Audit-Spur)

## Rechtsgrundlagen

- **Art. 30 DSGVO** VVT.
- **Art. 32 DSGVO** TOM.
- **Art. 33 Abs. 5 DSGVO** Vorfallregister.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 24 DSGVO** Verantwortung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Vorlagepflicht des VVT auf Behördenanforderung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 24; Art. 30; Art. 32; Art. 33 Abs. 5 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Update-Checkliste

Schritt 1: Vorfall einer Verarbeitung VVT-ID zuordnen.

Schritt 2: TOM-Liste aktualisieren — was war wirksam, was nicht, was wurde nachgerüstet.

Schritt 3: Risikobewertung in VVT überarbeiten.

Schritt 4: Auftragsverarbeiter-Eintrag pflegen — neue Subunternehmer dokumentieren.

Schritt 5: Aufbewahrungsfristen anpassen; Vorfallakte mit Aufbewahrungsende eintragen.

Schritt 6: Versionsstand mit Datum und Bearbeiter speichern; alte Version revisionssicher archivieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-dsfa-update-nach-vorfall` deckt die Datenschutz-Folgenabschätzung ab.
- `dsv-interne-dokumentation-art-33-abs-5` deckt das Vorfallregister ab.

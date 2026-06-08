---
name: erstgespraech-vorfallmeldung
description: "Führt das anwaltliche oder DSB-Erstgespräch nach einem gemeldeten Datenschutzvorfall mit Geschäftsleitung oder Fachabteilung. Behandelt: Zeitstrahl der Kenntnisnahme; betroffene Systeme und Verarbeitungen; Datenkategorien und Schutzbedarfsklassen; geschätzte Anzahl betroffener Personen; Auftragsverarbeiter-Konstellation; Konzernbezug Art. 56 DSGVO; bereits eingeleitete Sofortmaßnahmen; Beweissicherung; Pressekontakte; aufsichtsbehördliche Vorkontakte. Output: strukturiertes Gesprächsprotokoll mit Lücken-Liste. Abgrenzung: keine eigene Risikobewertung; keine Behördenmeldung."
---

# Erstgespräch nach gemeldetem Datenschutzvorfall — Fragenkatalog

## Triage — kläre vor der Bearbeitung

1. Wer nimmt am Erstgespräch teil — Geschäftsleitung, DSB, IT-Leitung, externer Forensiker, Versicherer?
2. Liegt eine schriftliche Vorfallmeldung vor oder erfolgt sie mündlich?
3. Ist der Vorfall bereits öffentlich oder droht öffentliche Wahrnehmung?
4. Ist eine Cyberversicherung im Spiel und welche Meldepflichten bestehen dort?
5. Gibt es einen Auftragsverarbeitervertrag oder eine gemeinsame Verantwortlichkeit?
- Was will der Mandant wirklich erreichen? (Lagebild, Meldepflichtprüfung, Bußgeldverteidigung, Haftungsminimierung)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldepflicht binnen 72 Stunden.
- **Art. 33 Abs. 2 DSGVO** Meldepflicht des Auftragsverarbeiters an den Verantwortlichen.
- **Art. 28 Abs. 3 lit. f DSGVO** Unterstützungspflicht des Auftragsverarbeiters.
- **Art. 56 DSGVO** Federführende Aufsichtsbehörde bei grenzüberschreitender Verarbeitung.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Kenntnisbegriff Art. 33 Abs. 1 DSGVO und Reichweite der Meldepflicht des Auftragsverarbeiters vor Ausgabe verifizieren.

## Zentrale Normen

Art. 4 Nr. 12; Art. 28; Art. 33; Art. 34; Art. 56 DSGVO; § 42 BDSG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Fragenblöcke

Zeitstrahl: Wann wurde was durch wen wahrgenommen — minutengenau wenn möglich.

Betroffene Verarbeitungen: Welche Verarbeitungstätigkeiten nach VVT sind tangiert?

Datenkategorien: Art. 9 DSGVO, Art. 10 DSGVO, Sozialdaten, Berufsgeheimnis § 203 StGB, Kinderdaten?

Personenkreis: Mitarbeiter, Kunden, Patienten, Mandanten, Schüler — geschätzte Anzahl.

Auftragsverarbeiter: Liegt AV-Vertrag vor; wer hat zuerst Kenntnis erlangt?

Konzernbezug: Hauptniederlassung in welchem EU-Mitgliedstaat?

Sofortmaßnahmen: Welche technischen und organisatorischen Schritte sind bereits erfolgt?

Beweissicherung: Logs, Images, Zeugen, Chain of Custody.

Externe Kommunikation: Presse, Kunden, Aufsichtsbehörde bereits angesprochen?

Versicherung: Cyberpolice; Meldepflicht-Trigger?

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

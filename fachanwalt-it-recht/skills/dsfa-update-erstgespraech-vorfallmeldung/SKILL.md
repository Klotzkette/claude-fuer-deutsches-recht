---
name: dsfa-update-erstgespraech-vorfallmeldung
description: "DSV Dsfa Update Erstgespraech Vorfallmeldung im Plugin Fachanwalt It Recht: prüft konkret Aktualisiert die Datenschutz-Folgenabschätzung nach Art, Führt das anwaltliche oder DSB-Erstgespräch nach einem, Definiert eine Eskalationsmatrix vom Erstmelder über, Pflegt das interne Vorfallregister nach Art."
---

# DSV Dsfa Update Erstgespraech Vorfallmeldung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `dsv-dsfa-update-nach-vorfall`

**Fokus:** Aktualisiert die Datenschutz-Folgenabschätzung nach Art. 35 DSGVO im Nachgang eines Datenschutzvorfalls. Behandelt: Erforderlichkeit der DSFA bei voraussichtlich hohem Risiko; Anpassung der Risikoanalyse; Abhilfemaßnahmen; Konsultation der Aufsichtsbehörde nach Art. 36 DSGVO bei verbleibendem hohem Risiko; Verknüpfung mit VVT und Vorfallregister. Output: DSFA-Update-Vorlage mit Pflichtfeldern. Abgrenzung: keine neue DSFA; kein Verfahrensverzeichnis.

### Datenschutz-Folgenabschätzung nach Datenschutzvorfall aktualisieren

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

## 2. `dsv-erstgespraech-vorfallmeldung`

**Fokus:** Führt das anwaltliche oder DSB-Erstgespräch nach einem gemeldeten Datenschutzvorfall mit Geschäftsleitung oder Fachabteilung. Behandelt: Zeitstrahl der Kenntnisnahme; betroffene Systeme und Verarbeitungen; Datenkategorien und Schutzbedarfsklassen; geschätzte Anzahl betroffener Personen; Auftragsverarbeiter-Konstellation; Konzernbezug Art. 56 DSGVO; bereits eingeleitete Sofortmaßnahmen; Beweissicherung; Pressekontakte; aufsichtsbehördliche Vorkontakte. Output: strukturiertes Gesprächsprotokoll mit Lücken-Liste. Abgrenzung: keine eigene Risikobewertung; keine Behördenmeldung.

### Erstgespräch nach gemeldetem Datenschutzvorfall — Fragenkatalog

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

## 3. `dsv-eskalationsmatrix`

**Fokus:** Definiert eine Eskalationsmatrix vom Erstmelder über Service-Desk und Datenschutzbeauftragten bis zur Geschäftsleitung und externen Beratern. Behandelt: Schwellenwerte für Eskalation; Erreichbarkeit außerhalb der Bürozeiten; Stellvertreter; Wochenend- und Feiertagsregelung; Eskalationsprotokoll; Ausweichkommunikation bei IT-Ausfall. Output: Matrix mit Stufen und Verantwortlichen plus Erreichbarkeitsplan. Abgrenzung: keine konkrete Stakeholder-Information.

### Eskalationsmatrix Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Schwellenwerte rechtfertigen welche Eskalationsstufe?
2. Welche Erreichbarkeit ist außerhalb der Bürozeiten gewährleistet?
3. Wer entscheidet über externe Eskalation (Anwalt, Versicherung, Behörde)?
4. Welche Ausweichkommunikation gilt bei IT-Ausfall (Mobilfunk, persönlich, Pager)?
5. Wer dokumentiert die Eskalationsentscheidung?
- Was will der Mandant wirklich erreichen? (klare Entscheidungswege; keine Eskalation läuft ins Leere)

## Rechtsgrundlagen

- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 24 DSGVO** Verantwortung des Verantwortlichen.
- **Art. 32 DSGVO** technische und organisatorische Maßnahmen.
- **Art. 33 Abs. 1 DSGVO** Meldepflicht binnen 72 Stunden.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Bußgeldfälle wegen verspäteter Meldung infolge Eskalationsversagen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 24; Art. 32; Art. 33 Abs. 1 DSGVO.

## Praxisformulierung — Eskalationsstufen

Stufe 1: Erstmelder → Service-Desk (innerhalb 30 Minuten).
Stufe 2: Service-Desk → DSB / IT-Sicherheit (innerhalb 1 Stunde).
Stufe 3: DSB → Geschäftsleitung und Anwalt (innerhalb 4 Stunden).
Stufe 4: Geschäftsleitung → Cyberversicherung und Aufsichtsbehörde (innerhalb 24 Stunden ab Kenntnisnahme).
Stufe 5: Pressemitteilung und Mitarbeiter-Information (nach Lagebeurteilung).

Erreichbarkeit: Hauptkontakt + zwei Stellvertreter je Stufe; 24/7-Rufbereitschaft definieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 4. `dsv-interne-dokumentation-art-33-abs-5`

**Fokus:** Pflegt das interne Vorfallregister nach Art. 33 Abs. 5 DSGVO als Beweisinstrument der Rechenschaftspflicht. Behandelt: Pflichtinhalte Sachverhalt, Auswirkungen, Abhilfemaßnahmen, Bewertung; Verknüpfung mit VVT; Aufbewahrungsfristen; Schnittstelle zu Risikomanagement; Vorlage auf Anforderung der Aufsichtsbehörde; Versionierung. Output: Vorlage Vorfallregister mit Pflichtfeldern. Abgrenzung: kein Verfahrensverzeichnis Art. 30.

### Interne Dokumentation Art. 33 Abs. 5 DSGVO — Vorfallregister

## Triage — kläre vor der Bearbeitung

1. Wer pflegt das Register — DSB, IT-Sicherheit, Compliance?
2. Welches System (Excel, GRC-Tool, DMS)?
3. Welche Aufbewahrungsfrist gilt im Unternehmen?
4. Welche Schnittstellen zu VVT, DSFA, ISMS bestehen?
5. Wer hat Zugriff?
- Was will der Mandant wirklich erreichen? (Rechenschaftspflicht erfüllen; Bußgeldverteidigung)

## Rechtsgrundlagen

- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 30 DSGVO** VVT.
- **Art. 24 DSGVO** Verantwortung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Aufbewahrungsdauer und Vorlagepflicht vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 24; Art. 30; Art. 33 Abs. 5 DSGVO.

## Praxisformulierung — Pflichtfelder Vorfallregister

Vorfall-ID; Datum Kenntnisnahme; Datum Eintritt; Kategorie (V/I/V); Sachverhalt; betroffene Verarbeitung VVT-ID; Datenarten; Anzahl Betroffener; Folgen; ergriffene Maßnahmen; Bewertung Art. 33; Bewertung Art. 34; Meldedatum; Aktenzeichen Aufsichtsbehörde; verantwortlicher Bearbeiter; Status; Aufbewahrung bis.

Versionierung: jede Änderung mit Datum und Bearbeiter; alte Versionen revisionssicher.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-vvt-update-nach-vorfall` deckt die Aktualisierung des VVT ab.

## 5. `dsv-kein-risiko-dokumentation`

**Fokus:** Erstellt die interne Dokumentation eines Datenschutzvorfalls, der nicht an die Aufsichtsbehörde gemeldet wird, weil voraussichtlich kein Risiko für die Rechte und Freiheiten besteht. Behandelt: Pflichtangaben nach Art. 33 Abs. 5 DSGVO; Sachverhalt; Auswirkungen; Abhilfemaßnahmen; Begründung der Nichtmeldung; Risikoabwägung mit Faktoren; Aufbewahrungsfristen; Vorlage für Aufsichtsbehörde auf Anforderung. Output: vollständige Dokumentationsvorlage. Abgrenzung: keine Behördenmeldung; keine Benachrichtigung.

### Kein-Risiko-Dokumentation nach Art. 33 Abs. 5 DSGVO

## Triage — kläre vor der Bearbeitung

1. Auf welchen Tatsachen beruht die Einschätzung kein Risiko?
2. Welche Risikoabmilderung war vor dem Vorfall wirksam (Verschlüsselung, Pseudonymisierung)?
3. Welche Anzahl Betroffener und welche Datenkategorien?
4. Welche Aufbewahrungsfrist gilt für die Dokumentation?
5. Wer prüft die Dokumentation mit (DSB, Anwalt)?
- Was will der Mandant wirklich erreichen? (Beweislast bei Nichtmeldung erfüllen; Bußgeldverteidigung)

## Rechtsgrundlagen

- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht für jeden Vorfall.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Erwägungsgrund 85 DSGVO** Voraussichtlich-kein-Risiko-Ausnahme.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Beweislastverteilung bei Nichtmeldung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 5; Art. 5 Abs. 2 DSGVO; Erwägungsgrund 85.

## Praxisformulierung — Inhaltsraster

1. Sachverhalt: was ist passiert; wann; in welchem System.
2. Auswirkungen: welche Datenkategorien; welche Betroffenenanzahl; welche Identifizierbarkeit.
3. Risikoabwägung: Faktoren mit Reasoning vor Conclusion; warum voraussichtlich kein Risiko.
4. Abhilfemaßnahmen: was wurde getan; was wird getan; bis wann.
5. Verzicht auf Meldung: begründete Conclusion mit Bezug auf Risikobewertung.
6. Verzicht auf Benachrichtigung: begründete Conclusion zu Art. 34 DSGVO.
7. Aufbewahrung: drei Jahre Mindestempfehlung; im Verfahrensverzeichnis verlinken.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-interne-dokumentation-art-33-abs-5` deckt die Dokumentation auch für gemeldete Faelle ab.


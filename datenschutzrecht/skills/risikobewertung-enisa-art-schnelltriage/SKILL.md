---
name: risikobewertung-enisa-art-schnelltriage
description: "DSV Risikobewertung Enisa ART Schnelltriage im Datenschutzrecht: prüft konkret Wendet die ENISA-Methodik Recommendations for a methodology, Strukturiert die Schwellenwertentscheidung nach Art, Liefert in 15-30 Minuten eine Schnelltriage zum Risiko, Generiert eine priorisierte Sofortmaßnahmen-Checkliste. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# DSV Risikobewertung Enisa ART Schnelltriage

## Arbeitsbereich

**DSV Risikobewertung Enisa ART Schnelltriage** ordnet den Fall über die tragenden Prüfungslinien: Wendet die ENISA-Methodik Recommendations for a methodology, Strukturiert die Schwellenwertentscheidung nach Art, Liefert in 15-30 Minuten eine Schnelltriage zum Risiko. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `dsv-risikobewertung-enisa-schweregrad` | Wendet die ENISA-Methodik Recommendations for a methodology of the assessment of severity of personal data breaches auf einen konkreten Vorfall an. Behandelt: Data Processing Context DPC; Ease of Identification EI; Circumstances of Breach CB; Schweregradformel SE = DPC × EI + CB; vier Stufen Low Medium High Very High; Übersetzung in Meldepflicht Art. 33 und Benachrichtigung Art. 34 DSGVO. Output: quantitative ENISA-Bewertung mit Faktoren und Schwellenwerten. Abgrenzung: keine EDSA-Beispielmethodik; keine Behördenmeldung. |
| `dsv-risikobewertung-schwellen-art-33-34` | Strukturiert die Schwellenwertentscheidung nach Art. 33 und Art. 34 DSGVO als anwaltlichen Entscheidungsbaum. Behandelt: voraussichtlich-kein-Risiko-Schwelle Art. 33 Abs. 1; Meldeschwelle; voraussichtlich-hohes-Risiko Art. 34 Abs. 1; Ausnahmen Art. 34 Abs. 3 (technische Schutzmaßnahmen, nachträgliche Risikominderung, unverhältnismäßiger Aufwand); EDSA-Auslegung; deutsche Praxis. Output: Entscheidungsbaum mit Begründungstexten für jede Verzweigung. Abgrenzung: keine konkrete Meldung; keine ENISA-Quantifizierung. |
| `dsv-schnelltriage-risiko` | Liefert in 15-30 Minuten eine Schnelltriage zum Risiko eines gemeldeten Datenschutzvorfalls als Entscheidungsgrundlage für die 72-Stunden-Meldung. Behandelt: Vertraulichkeits-, Integritäts- und Verfügbarkeitsverletzung; Datenkategorien; Identifizierbarkeit; Anzahl betroffener Personen; Reversibilität; besondere Schutzbedürftigkeit Kinder Patienten Mitarbeiter; Eintrittswahrscheinlichkeit und Schwere; vorläufige Ampel grün gelb rot schwarz. Output: Triage-Memo mit Begründung und Empfehlung Meldung Ja/Nein/Vorsorglich. Abgrenzung: ersetzt nicht die vertiefte Bewertung nach EDSA-Leitlinien und ENISA. |
| `dsv-sofortmassnahmen-checkliste` | Generiert eine priorisierte Sofortmaßnahmen-Checkliste innerhalb der ersten Stunden nach Bekanntwerden eines Datenschutzvorfalls. Behandelt: Eindämmung; Beweissicherung; Zugriffsbeschränkung; Passwort-Reset; Account-Sperrung; Netzwerksegmentierung; forensische Erstsicherung; Benachrichtigung interner Stakeholder; Versicherungsmeldung; Logging-Sicherung; Backups schützen; Pressepolitik; rechtliche Sofortmaßnahmen bei Insider-Tätern oder Strafanzeige. Output: priorisierte Maßnahmenliste mit Verantwortlichen und Zeitvorgaben. Abgrenzung: keine Behördenmeldung; keine vertiefte Forensik. |
| `dsv-sozialdaten-sgb` | Bewertet einen Datenschutzvorfall bei Sozialleistungsträgern, Sozialversicherungen und sozialen Diensten nach den Sondervorschriften der Sozialgesetzbücher. Behandelt: Sozialdatenbegriff § 67 SGB X; Sozialgeheimnis § 35 SGB I; Verhältnis zur DSGVO; Meldepflicht nach § 83a SGB X; besondere Bußgeldvorschriften; Aufsichtsstruktur Bund/Länder. Output: Memo zur Meldepflicht-Doppelspur und Empfehlung. Abgrenzung: keine konkrete Behördenmeldung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `dsv-risikobewertung-enisa-schweregrad`

**Fokus:** Wendet die ENISA-Methodik Recommendations for a methodology of the assessment of severity of personal data breaches auf einen konkreten Vorfall an. Behandelt: Data Processing Context DPC; Ease of Identification EI; Circumstances of Breach CB; Schweregradformel SE = DPC × EI + CB; vier Stufen Low Medium High Very High; Übersetzung in Meldepflicht Art. 33 und Benachrichtigung Art. 34 DSGVO. Output: quantitative ENISA-Bewertung mit Faktoren und Schwellenwerten. Abgrenzung: keine EDSA-Beispielmethodik; keine Behördenmeldung.

### ENISA-Methodik zur Schweregradbewertung von Datenschutzverletzungen

## Triage — kläre vor der Bearbeitung

1. Welche Verarbeitungskontextstufe (DPC) liegt vor — einfach, behavior, sensitive, oder highly sensitive?
2. Wie leicht sind Betroffene identifizierbar (EI von 0,25 bis 1)?
3. Welche Umstände erhöhen oder mindern das Risiko (CB-Faktoren)?
4. Welche Daten sind besonders schutzbedürftig?
5. Wie ist die quantitative Bewertung zu kommunizieren?
- Was will der Mandant wirklich erreichen? (objektivierte Bewertung; Verteidigung gegen Behörde)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldepflicht.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigung.
- **Erwägungsgrund 75; 76 DSGVO**.
- **ENISA Recommendations for a methodology of the assessment of severity of personal data breaches** (2013, weiterhin in Praxis verwendet).
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Akzeptanz der ENISA-Methodik durch deutsche Aufsichtsbehörden vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 1; Art. 34 Abs. 1; Art. 5 Abs. 2 DSGVO; ENISA-Methodik 2013.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — ENISA-Berechnung

DPC: simple data 1; behavioural data 2; sensitive data 3; highly sensitive data 4.

EI: negligible 0,25; limited 0,5; significant 0,75; maximum 1.

CB: -2 bis +0,5 je nach Umständen (Loss of confidentiality, integrity, availability; malicious intent; etc.).

SE = DPC × EI + CB.

Stufen: SE < 2 Low; 2-3 Medium; 3-4 High; > 4 Very High.

Conclusion: Meldung Art. 33 ab Medium; Benachrichtigung Art. 34 ab High.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-risikobewertung-edsa-leitlinie` ergaenzt um qualitative Beispielfallgruppen.

## 2. `dsv-risikobewertung-schwellen-art-33-34`

**Fokus:** Strukturiert die Schwellenwertentscheidung nach Art. 33 und Art. 34 DSGVO als anwaltlichen Entscheidungsbaum. Behandelt: voraussichtlich-kein-Risiko-Schwelle Art. 33 Abs. 1; Meldeschwelle; voraussichtlich-hohes-Risiko Art. 34 Abs. 1; Ausnahmen Art. 34 Abs. 3 (technische Schutzmaßnahmen, nachträgliche Risikominderung, unverhältnismäßiger Aufwand); EDSA-Auslegung; deutsche Praxis. Output: Entscheidungsbaum mit Begründungstexten für jede Verzweigung. Abgrenzung: keine konkrete Meldung; keine ENISA-Quantifizierung.

### Schwellenwerte Art. 33 und Art. 34 DSGVO — Entscheidungsbaum

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

## 3. `dsv-schnelltriage-risiko`

**Fokus:** Liefert in 15-30 Minuten eine Schnelltriage zum Risiko eines gemeldeten Datenschutzvorfalls als Entscheidungsgrundlage für die 72-Stunden-Meldung. Behandelt: Vertraulichkeits-, Integritäts- und Verfügbarkeitsverletzung; Datenkategorien; Identifizierbarkeit; Anzahl betroffener Personen; Reversibilität; besondere Schutzbedürftigkeit Kinder Patienten Mitarbeiter; Eintrittswahrscheinlichkeit und Schwere; vorläufige Ampel grün gelb rot schwarz. Output: Triage-Memo mit Begründung und Empfehlung Meldung Ja/Nein/Vorsorglich. Abgrenzung: ersetzt nicht die vertiefte Bewertung nach EDSA-Leitlinien und ENISA.

### Schnelltriage Risikoeinschätzung nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Schutzziele sind verletzt — Vertraulichkeit, Integrität, Verfügbarkeit?
2. Welche Datenkategorien und welcher Personenkreis sind betroffen?
3. Sind besondere Kategorien nach Art. 9 DSGVO oder strafrechtsrelevante Daten nach Art. 10 DSGVO beteiligt?
4. Ist die Verletzung eingrenzbar oder breitet sie sich aus?
5. Wie viel Zeit bleibt bis zum Ende der 72-Stunden-Frist?
- Was will der Mandant wirklich erreichen? (schnelle Entscheidung; rechtssichere Begründung der Nichtmeldung)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 Satz 1 DSGVO** Meldepflicht außer wenn voraussichtlich kein Risiko.
- **Art. 33 Abs. 5 DSGVO** Dokumentation auch bei Nichtmeldung.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigung bei voraussichtlich hohem Risiko.
- **Erwägungsgrund 75 DSGVO** Risikofaktoren.
- **Erwägungsgrund 76 DSGVO** Wahrscheinlichkeit und Schwere des Risikos.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Schwelle voraussichtlich kein Risiko und zur Beweislast bei Nichtmeldung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 4 Nr. 12; Art. 33 Abs. 1; Art. 33 Abs. 5; Art. 34 Abs. 1 DSGVO; Erwägungsgrund 75; Erwägungsgrund 76.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Schnelltriage-Raster

Schutzzielverletzung: V/I/V mit kurzer Begründung.

Datenkategorien: normale / besondere Art. 9 / strafrechtsrelevant Art. 10 / Berufsgeheimnis § 203 StGB.

Personenkreis und Anzahl: geschätzter Bereich; Identifizierbarkeit ja/nein.

Reversibilität: vollständig wiederherstellbar / teilweise / irreversibel.

Schwere: gering / mittel / hoch / sehr hoch — mit Reasoning.

Wahrscheinlichkeit: gering / mittel / hoch.

Ampelvorschlag: 🟢 keine Meldung / 🟡 Vorsorglich melden / 🔴 melden / ⚫ zusätzlich Art. 34.

Begründung: drei bis fünf Sätze für die Akte.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 4. `dsv-sofortmassnahmen-checkliste`

**Fokus:** Generiert eine priorisierte Sofortmaßnahmen-Checkliste innerhalb der ersten Stunden nach Bekanntwerden eines Datenschutzvorfalls. Behandelt: Eindämmung; Beweissicherung; Zugriffsbeschränkung; Passwort-Reset; Account-Sperrung; Netzwerksegmentierung; forensische Erstsicherung; Benachrichtigung interner Stakeholder; Versicherungsmeldung; Logging-Sicherung; Backups schützen; Pressepolitik; rechtliche Sofortmaßnahmen bei Insider-Tätern oder Strafanzeige. Output: priorisierte Maßnahmenliste mit Verantwortlichen und Zeitvorgaben. Abgrenzung: keine Behördenmeldung; keine vertiefte Forensik.

### Sofortmaßnahmen-Checkliste nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Ist der Angriff oder das Leck noch aktiv oder bereits gestoppt?
2. Sind Backups intakt und vom kompromittierten System getrennt?
3. Gibt es Hinweise auf einen Innentäter — dann besondere Vorsicht bei Account-Sperrungen wegen Beweismittelvernichtung?
4. Greift eine Strafanzeigepflicht oder ein Strafanzeigeinteresse?
5. Welche Verträge mit Auftragsverarbeitern oder Cyberversicherern verlangen Sofortmeldungen?
- Was will der Mandant wirklich erreichen? (Schadensbegrenzung; Beweissicherung; Compliance-Dokumentation)

## Rechtsgrundlagen

- **Art. 32 DSGVO** Pflicht zu angemessenen technischen und organisatorischen Maßnahmen einschließlich Wiederherstellungsfähigkeit.
- **Art. 33 Abs. 3 lit. c DSGVO** Angabe der ergriffenen oder vorgeschlagenen Maßnahmen in der Meldung.
- **Art. 5 Abs. 1 lit. f DSGVO** Integrität und Vertraulichkeit.
- **§ 42 BDSG** Strafvorschriften.
- **§ 274 StGB** Urkundenunterdrückung; **§ 303a StGB** Datenveränderung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Entscheidungen zu Beweisverwertungsverboten bei eilig getroffenen Maßnahmen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 1 lit. f; Art. 32; Art. 33 Abs. 3 lit. c DSGVO; § 42 BDSG; §§ 274; 303a StGB.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Sofortmaßnahmen Priorität 1 bis 4

Priorität 1 (sofort, 0-1 h):
- Eindämmung — System isolieren oder Account sperren ohne Beweisvernichtung.
- Beweissicherung — Logs einfrieren; Speicherabbild ziehen lassen.
- Interner Alarm — DSB, Geschäftsleitung, IT-Sicherheit.
- Versicherer kontaktieren falls Cyberpolice vorhanden.

Priorität 2 (1-6 h):
- Forensiker beauftragen.
- Passwort- und Token-Reset für betroffene Konten.
- Backups vom Netz trennen.
- Kommunikationssperre bis zur Lagebeurteilung.

Priorität 3 (6-24 h):
- Detaillierte Bestandsaufnahme der betroffenen Verarbeitungen.
- Auftragsverarbeiter informieren.
- Risikoabwägung Art. 33 / Art. 34 DSGVO einleiten.

Priorität 4 (24-72 h):
- Meldung an Aufsichtsbehörde vorbereiten und absenden.
- Strafanzeige bei Insider-Verdacht prüfen.
- Pressemitteilung und Kundenkommunikation vorbereiten.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 5. `dsv-sozialdaten-sgb`

**Fokus:** Bewertet einen Datenschutzvorfall bei Sozialleistungsträgern, Sozialversicherungen und sozialen Diensten nach den Sondervorschriften der Sozialgesetzbücher. Behandelt: Sozialdatenbegriff § 67 SGB X; Sozialgeheimnis § 35 SGB I; Verhältnis zur DSGVO; Meldepflicht nach § 83a SGB X; besondere Bußgeldvorschriften; Aufsichtsstruktur Bund/Länder. Output: Memo zur Meldepflicht-Doppelspur und Empfehlung. Abgrenzung: keine konkrete Behördenmeldung.

### Sozialdaten im Datenschutzvorfall — SGB I und SGB X

## Triage — kläre vor der Bearbeitung

1. Liegen Sozialdaten im Sinne § 67 SGB X vor?
2. Welche Stelle ist Verantwortlicher — Sozialleistungsträger, Krankenkasse, Berufsgenossenschaft?
3. Welche Aufsicht ist zuständig (Bundesbeauftragte oder Landesbeauftragte)?
4. Welche Meldewege überschneiden sich (DSGVO und SGB)?
5. Welche besonderen Strafvorschriften greifen (§ 85 SGB X)?
- Was will der Mandant wirklich erreichen? (Doppelmeldung sauber abwickeln; berufs- und beamtenrechtliche Folgen vermeiden)

## Rechtsgrundlagen

- **§ 35 SGB I** Sozialgeheimnis.
- **§ 67 SGB X** Definitionen.
- **§ 83a SGB X** Meldung Datenschutzverletzungen.
- **§ 85 SGB X** Bußgeldvorschriften.
- **Art. 33 DSGVO** allgemeine Meldepflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zum Verhältnis § 83a SGB X zu Art. 33 DSGVO vor Ausgabe verifizieren.

## Zentrale Normen

§ 35; § 67; § 83a; § 85 SGB X; § 35 SGB I; Art. 33 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Doppelspur Meldung

DSGVO-Spur: Meldung an Aufsichtsbehörde (BfDI bei Bundesbehörde oder zuständige Landesbehörde).

SGB-Spur: zusätzliche Pflichten nach § 83a SGB X; ggf. Aufsicht durch Sozialministerium.

Berichtsformate parallel halten; Konsistenz beachten.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-art-9-besondere-kategorien` deckt Gesundheitsdaten ab.
- `dsv-paragraf-203-stgb-berufsgeheimnis` deckt aerztliches Geheimnis ab.

---
name: risikobewertung-art-schnelltriage-risiko
description: "DSV Risikobewertung ART Schnelltriage Risiko im Plugin Fachanwalt It Recht: prüft konkret Strukturiert die Schwellenwertentscheidung nach Art, Liefert in 15-30 Minuten eine Schnelltriage zum Risiko, Generiert eine priorisierte Sofortmaßnahmen-Checkliste, Bewertet einen Datenschutzvorfall bei Sozialleistungsträgern."
---

# DSV Risikobewertung ART Schnelltriage Risiko

## Aktenstart statt Formularstart

Wenn zu **Risikobewertung Art Schnelltriage Risiko** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt It Recht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `dsv-risikobewertung-schwellen-art-33-34`

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

## 2. `dsv-schnelltriage-risiko`

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

## 3. `dsv-sofortmassnahmen-checkliste`

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

## 4. `dsv-sozialdaten-sgb`

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

## 5. `dsv-spezialfaelle-uebersicht`

**Fokus:** Liefert eine schnelle Übersicht über häufige Spezialfälle eines Datenschutzvorfalls und verweist auf vertiefte Skills. Behandelt: Ransomware; Insider-Threat; Fehlversand E-Mail/Brief; Endgeräteverlust; verlorener Datenträger; Cloud-Fehlkonfiguration; offene S3-Buckets; kompromittiertes E-Mail-Konto; Phishing-Erfolg; Schatten-IT; kompromittierter Dienstleister; Web-Defacement; Datenleck durch Whistleblower. Output: Übersichts-Matrix mit Erstbewertung und Verweisen auf vertiefte Skills. Abgrenzung: ersetzt nicht die Einzelbewertung.

### Spezialfälle Datenschutzvorfall — Übersicht für die Triage

## Triage — kläre vor der Bearbeitung

1. Welcher Spezialfall liegt vor und welche Sofortmaßnahmen prägt das?
2. Liegt ein typischer Mehrfach-Trigger vor (Ransomware = V+I+V)?
3. Welche besondere Sektoraufsicht ist betroffen (KRITIS, Finanzen, Gesundheit)?
4. Welche typischen Bußgeldhebel sind aus der Praxis bekannt?
5. Welche typischen Beweisprobleme prägen den Fall?
- Was will der Mandant wirklich erreichen? (schneller Überblick; passende vertiefte Skills wählen)

## Rechtsgrundlagen

- **Art. 32 DSGVO** Sicherheit der Verarbeitung.
- **Art. 33 DSGVO** Meldepflicht.
- **Art. 34 DSGVO** Benachrichtigung.
- **§ 8b BSIG** Meldepflicht KRITIS.
- **NIS-2-UmsuCG** (sofern in Kraft) zusätzliche Meldepflichten.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Ransomware-Bußgeldbescheide und Sammelklagen wegen Datenleck vor Ausgabe verifizieren.

## Zentrale Normen

Art. 32; Art. 33; Art. 34 DSGVO; § 8b BSIG.

## Praxisformulierung — Spezialfall-Matrix

Ransomware → V+I+V; Lösegeldverbot prüfen; KRITIS-Meldung.
Insider-Threat → Beweissicherung diskret; Strafanzeige prüfen; Mitbestimmung beachten.
Fehlversand → Empfänger kontaktieren; Vernichtungsbestätigung einholen.
Endgeräteverlust → Verschlüsselungsnachweis; Remote-Wipe protokollieren.
Cloud-Fehlkonfiguration → Konfigurationsänderung; Logs; CSP-AV-Pflichten.
Kompromittiertes E-Mail-Konto → Tokens widerrufen; Mailregeln prüfen; Phishing-Welle erwarten.
Dienstleisterleck → AV-Vertrag prüfen; Meldekette Art. 33 Abs. 2 DSGVO.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.


---
name: it-recht-massenbenachrichtigung-meldekette-auftragsverarbeiter
description: "Massenbenachrichtigung Meldekette Auftragsverarbeiter im Plugin Fachanwalt It Recht: prüft konkret Steuert die Massenbenachrichtigung tausender oder Millionen, Steuert die Meldekette in einer, Steuert die Meldung eines Datenschutzvorfalls mit Bezug zu, Steuert die parallele Meldung an Sektoraufsichten neben der."
---

# Massenbenachrichtigung Meldekette Auftragsverarbeiter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `dsv-massenbenachrichtigung`

**Fokus:** Steuert die Massenbenachrichtigung tausender oder Millionen Betroffener nach Art. 34 DSGVO. Behandelt: Versandlogistik E-Mail-Welle; Brief-Welle; Push und SMS; Adressqualität; Bounces; Sprachvarianten; Hotline-Dimensionierung; Pressewelle; Hilfsdienste wie Schufa-Auskunft. Output: Versandplan, Skalierungsraster, Q&A-Matrix. Abgrenzung: keine individuelle Benachrichtigung; keine Behördenmeldung.

### Massenbenachrichtigung bei großem Datenschutzvorfall

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

## 2. `dsv-meldekette-auftragsverarbeiter`

**Fokus:** Steuert die Meldekette in einer Auftragsverarbeiter-Konstellation nach Art. 33 Abs. 2 DSGVO. Behandelt: Meldung des Auftragsverarbeiters an den Verantwortlichen; Form, Frist, Inhalt; Eskalation bei Schweigen oder Verzögerung; AV-Vertragsklauseln nach Art. 28 Abs. 3 lit. f und h DSGVO; Unterauftragsverarbeiter; Vertragsstrafen; Beweissicherungspflichten beim Auftragsverarbeiter. Output: Mustermeldung Auftragsverarbeiter an Verantwortlichen plus Eskalationsschreiben. Abgrenzung: keine Behördenmeldung durch den Auftragsverarbeiter.

### Meldekette Auftragsverarbeiter — Art. 33 Abs. 2 DSGVO

## Triage — kläre vor der Bearbeitung

1. Wer ist Verantwortlicher und wer Auftragsverarbeiter (klare Abgrenzung)?
2. Liegt ein AV-Vertrag nach Art. 28 Abs. 3 DSGVO vor?
3. Welche Meldefristen sind dort vereinbart (oft kürzer als 72 Stunden)?
4. Sind Unterauftragsverarbeiter beteiligt?
5. Welche Vertragsstrafen oder Schadensersatzklauseln greifen?
- Was will der Mandant wirklich erreichen? (klare Verantwortungsabgrenzung; Schadensersatzansprüche sichern)

## Rechtsgrundlagen

- **Art. 28 Abs. 3 lit. f; h DSGVO** AV-Pflichten.
- **Art. 33 Abs. 2 DSGVO** Meldepflicht des Auftragsverarbeiters.
- **Art. 82 DSGVO** Schadensersatz.
- **§ 280 BGB** Pflichtverletzung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Fristberechnung Art. 33 Abs. 1 DSGVO bei Kenntnis nur des Auftragsverarbeiters vor Ausgabe verifizieren.

## Zentrale Normen

Art. 28 Abs. 3; Art. 33 Abs. 2; Art. 82 DSGVO; § 280 BGB.

## Praxisformulierung — Muster Meldung Auftragsverarbeiter

Betreff: Meldung einer Verletzung des Schutzes personenbezogener Daten nach Art. 33 Abs. 2 DSGVO.

Sehr geehrte Damen und Herren, gemäß Art. 33 Abs. 2 DSGVO und unserem AV-Vertrag vom [Datum] melden wir Ihnen folgenden Vorfall:

- Datum und Uhrzeit der Kenntnisnahme: [...]
- Beschreibung der Verletzung: [...]
- Betroffene Verarbeitung: [...]
- Geschätzte Anzahl betroffener Datensätze: [...]
- Bereits eingeleitete Sofortmaßnahmen: [...]
- Vorgeschlagene weitere Maßnahmen: [...]
- Ansprechpartner: [...]

Eine Nachmeldung mit weiteren Details folgt unverzüglich nach Abschluss der forensischen Analyse.

Eskalationsschreiben bei Schweigen: Fristsetzung 24 h; danach Vertragsstrafe und Kündigungsandrohung.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung des Verantwortlichen ab.

## 3. `dsv-meldung-grenzueberschreitend`

**Fokus:** Steuert die Meldung eines Datenschutzvorfalls mit Bezug zu mehreren Mitgliedstaaten oder Drittstaaten. Behandelt: Lead-Authority-Verfahren Art. 56 DSGVO; parallele Meldung an betroffene Behörden; Sprache der Meldung; Drittstaaten-Aufsichten und ihre Meldepflichten (z.B. UK ICO, Schweiz EDÖB); Schnittstelle zu Art. 49 DSGVO-Übermittlungen; Hinweispflichten an US-Aufsichten bei BIPA, CCPA, GLBA. Output: Memo zur Meldelandkarte. Abgrenzung: keine vertiefte US-Beratung.

### Meldung grenzüberschreitender Datenschutzvorfälle — EU und Drittstaaten

## Triage — kläre vor der Bearbeitung

1. In welchen EU-Staaten sind Betroffene?
2. Welche Drittstaaten sind tangiert?
3. Welche Lead Authority ist nach Art. 56 DSGVO zuständig?
4. Welche Drittstaatsaufsichten erfordern parallele Meldung?
5. Welche Sprache verlangt jede Behörde?
- Was will der Mandant wirklich erreichen? (rechtssichere Meldelandkarte; keine vergessene Behörde)

## Rechtsgrundlagen

- **Art. 56 DSGVO** Lead Authority.
- **Art. 60 DSGVO** Kooperation.
- **Art. 33 DSGVO** Meldepflicht.
- **Art. 49 DSGVO** Übermittlungen.
- **UK GDPR; Swiss DSG; CCPA; BIPA** je nach Drittstaatsbezug.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu One-Stop-Shop-Streitigkeiten und Drittstaaten-Anerkennung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33; Art. 49; Art. 56; Art. 60 DSGVO; UK GDPR; Swiss DSG.

## Praxisformulierung — Meldelandkarte

Spalte 1: Land; Spalte 2: Behörde; Spalte 3: Pflicht oder freiwillig; Spalte 4: Frist; Spalte 5: Sprache; Spalte 6: Verantwortlicher intern; Spalte 7: Status.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-lead-authority-konzern` deckt die Bestimmung der federfuehrenden Behörde ab.

## 4. `dsv-meldung-kritis-sektoraufsicht`

**Fokus:** Steuert die parallele Meldung an Sektoraufsichten neben der Datenschutzaufsicht. Behandelt: § 8b BSIG für KRITIS; NIS-2-Umsetzung mit erweiterten Meldepflichten; BaFin BAIT/MaRisk für Finanzinstitute; BNetzA für TK- und Postdienste; Meldungen nach § 168 TKG; Konsistenz der Meldetexte; Datenschutzschnittstelle. Output: Memo zur Mehrfachmeldelandschaft. Abgrenzung: keine vertiefte BaFin-Beratung.

### Parallele Meldung KRITIS und Sektoraufsicht — BSIG, BaFin, BNetzA, NIS-2

## Triage — kläre vor der Bearbeitung

1. Ist der Mandant KRITIS-Betreiber, NIS-2-pflichtige Einrichtung oder reguliertes Institut?
2. Welche Sektoraufsicht ist zusätzlich zur Datenschutzbehörde zu informieren?
3. Welche Fristen gelten (BSIG, NIS-2, TKG)?
4. Welcher Texte muss konsistent gehalten werden?
5. Welche Aufsicht hat informellen Vorrang?
- Was will der Mandant wirklich erreichen? (rechtssichere Parallel-Meldung; konsistente Aussagen)

## Rechtsgrundlagen

- **§ 8b BSIG** KRITIS-Meldepflicht.
- **NIS-2-Richtlinie** und deutsches Umsetzungsgesetz (Stand prüfen).
- **§ 168 TKG** Sicherheitsvorfälle TK.
- **BaFin BAIT/MaRisk** für Finanzinstitute.
- **Art. 33 DSGVO** Datenschutzmeldung.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Stände zur NIS-2-Umsetzung in Deutschland vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 DSGVO; § 8b BSIG; § 168 TKG; NIS-2-Richtlinie; BAIT.

## Praxisformulierung — Mehrfach-Meldelandschaft

Datenschutz-Spur: zuständige Datenschutzbehörde (Lead-Authority + Land).

BSIG/NIS-2-Spur: BSI Meldestelle.

TK-Spur: BNetzA.

Finanzaufsicht: BaFin.

Texte synchronisiert; Aktenzeichen wechselseitig zitieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-meldung-art-33-pflichtangaben` deckt die Datenschutz-Meldung ab.

## 5. `dsv-paragraf-203-stgb-berufsgeheimnis`

**Fokus:** Bewertet einen Datenschutzvorfall bei Berufsgeheimnisträgern nach § 203 StGB. Behandelt: Ärzte; Rechtsanwälte; Steuerberater; Wirtschaftsprüfer; Psychotherapeuten; Sozialarbeiter; berufsmäßige Gehilfen; mitwirkende Personen nach § 203 Abs. 3 StGB; Reichweite der Schweigepflicht; Verhältnis zur DSGVO; Anzeige- und Benachrichtigungspflichten; Risiken bei Cloud-Auslagerung; berufsrechtliche Folgen. Output: Memo zu Strafbarkeitsrisiko und Pflichten. Abgrenzung: keine berufsrechtliche Verteidigung; keine Strafanzeige.

### § 203 StGB Berufsgeheimnis im Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welcher Berufsgeheimnisträger ist betroffen?
2. Wurde das Geheimnis offenbart oder unbefugt zugänglich gemacht?
3. Lag Vorsatz oder Fahrlässigkeit vor?
4. Sind mitwirkende Personen nach § 203 Abs. 3 StGB beteiligt — Cloud-Anbieter, Praxisverwaltungssystem?
5. Welche Schweigepflichtsentbindung der Betroffenen liegt vor?
- Was will der Mandant wirklich erreichen? (Strafbarkeitsrisiko vermeiden; Berufszulassung sichern)

## Rechtsgrundlagen

- **§ 203 Abs. 1 StGB** Verletzung von Privatgeheimnissen.
- **§ 203 Abs. 3 Satz 2 StGB** mitwirkende Personen.
- **§ 203 Abs. 4 StGB** Offenbarungstatbestände.
- **Art. 33 DSGVO** Meldepflicht (zusätzlich zur strafrechtlichen Bewertung).
- **§ 43a Abs. 2 BRAO** anwaltliche Verschwiegenheit.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Reichweite des § 203 Abs. 3 Satz 2 StGB bei IT-Dienstleistern vor Ausgabe verifizieren.

## Zentrale Normen

§ 203 Abs. 1; § 203 Abs. 3; § 203 Abs. 4 StGB; Art. 33 DSGVO; § 43a Abs. 2 BRAO.

## Praxisformulierung — Strafbarkeitsraster

Tathandlung: Offenbaren / unbefugt Zugänglichmachen.

Täterkreis: § 203 Abs. 1 StGB Katalog; § 203 Abs. 3 mitwirkende Personen.

Schuld: Vorsatz / Fahrlässigkeit (§ 203 Abs. 1 setzt Vorsatz voraus; fahrlässige Offenbarung nicht strafbar, aber berufsrechtlich relevant).

Berufsrecht: zusätzliche Meldung an Kammer; Disziplinarverfahren möglich.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-art-9-besondere-kategorien` deckt sensible Daten ab.
- `dsv-sozialdaten-sgb` deckt Sozialdaten ab.


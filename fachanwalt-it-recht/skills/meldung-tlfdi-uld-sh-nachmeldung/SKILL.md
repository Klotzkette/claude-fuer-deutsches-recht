---
name: meldung-tlfdi-uld-sh-nachmeldung
description: "DSV Meldung Tlfdi ULD SH Nachmeldung im Plugin Fachanwalt It Recht: prüft konkret Reicht eine Meldung nach Art, Erstellt die Nachmeldung zu einer vorläufigen Erstmeldung, Führt die Risikobewertung eines Datenschutzvorfalls anhand. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# DSV Meldung Tlfdi ULD SH Nachmeldung

## Arbeitsbereich

**DSV Meldung Tlfdi ULD SH Nachmeldung** ordnet den Fall über die tragenden Prüfungslinien: Reicht eine Meldung nach Art, Erstellt die Nachmeldung zu einer vorläufigen Erstmeldung. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `dsv-meldung-tlfdi` | Reicht eine Meldung nach Art. 33 DSGVO bei der Thüringer Landesbeauftragter für den Datenschutz und die Informationsfreiheit (TLfDI) ein. Behandelt: Zuständigkeit für Verantwortliche mit Hauptniederlassung in Thüringen und für nicht-öffentliche Stellen; Online-Formular und Postweg; Pflichtangaben in der Reihenfolge der Berliner Goldstandard-Struktur I bis VI; Sonderregelungen aus ThürDSG Thüringer Datenschutzgesetz; Eingangsbestätigung; Aktenzeichen; Nachmeldung. Output: einreichungsfertige Meldung als Fließtext mit Erläuterung der Eingabewege. Abgrenzung: keine Risikobewertung; keine Benachrichtigung Art. 34 DSGVO. |
| `dsv-meldung-uld-sh` | Reicht eine Meldung nach Art. 33 DSGVO bei der Unabhängiges Landeszentrum für Datenschutz Schleswig-Holstein (ULD) ein. Behandelt: Zuständigkeit für Verantwortliche mit Hauptniederlassung in Schleswig-Holstein und für nicht-öffentliche Stellen; Online-Formular und Postweg; Pflichtangaben in der Reihenfolge der Berliner Goldstandard-Struktur I bis VI; Sonderregelungen aus LDSG Schleswig-Holstein; Eingangsbestätigung; Aktenzeichen; Nachmeldung. Output: einreichungsfertige Meldung als Fließtext mit Erläuterung der Eingabewege. Abgrenzung: keine Risikobewertung; keine Benachrichtigung Art. 34 DSGVO. |
| `dsv-nachmeldung-aktualisierung-art-33-abs-4` | Erstellt die Nachmeldung zu einer vorläufigen Erstmeldung nach Art. 33 Abs. 4 DSGVO. Behandelt: 14-Tage-Frist der Berliner Praxis; Ergänzung der Datenarten; Korrektur der Anzahl Betroffener; Update der Gegenmaßnahmen; Information zur Pressemitteilung; Verweis auf Forensikbericht; Mitteilung zur Strafanzeige; Schluss der Meldung. Output: Nachmeldungs-Schreiben mit Bezug auf Aktenzeichen der Erstmeldung. Abgrenzung: keine neue Erstmeldung. |
| `dsv-risikobewertung-edsa-leitlinie` | Führt die Risikobewertung eines Datenschutzvorfalls anhand der EDSA-Leitlinie 9/2022 zu Beispielen für die Meldung von Datenschutzverletzungen durch. Behandelt: Beispielfallgruppen Ransomware; Datenexfiltration; Insider; Verlust; Fehlversand; soziale Ingenieurkunst; jeweils mit Schwere-Schwellen für Meldepflicht Art. 33 DSGVO und Benachrichtigungspflicht Art. 34 DSGVO. Output: strukturierte Bewertung mit Bezug auf konkrete Beispielfallgruppe und begründeter Empfehlung Meldung Ja/Nein und Benachrichtigung Ja/Nein. Abgrenzung: keine Behördenmeldung; keine ENISA-Methodik. |
| `dsv-risikobewertung-enisa-schweregrad` | Wendet die ENISA-Methodik Recommendations for a methodology of the assessment of severity of personal data breaches auf einen konkreten Vorfall an. Behandelt: Data Processing Context DPC; Ease of Identification EI; Circumstances of Breach CB; Schweregradformel SE = DPC × EI + CB; vier Stufen Low Medium High Very High; Übersetzung in Meldepflicht Art. 33 und Benachrichtigung Art. 34 DSGVO. Output: quantitative ENISA-Bewertung mit Faktoren und Schwellenwerten. Abgrenzung: keine EDSA-Beispielmethodik; keine Behördenmeldung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `dsv-meldung-tlfdi`

**Fokus:** Reicht eine Meldung nach Art. 33 DSGVO bei der Thüringer Landesbeauftragter für den Datenschutz und die Informationsfreiheit (TLfDI) ein. Behandelt: Zuständigkeit für Verantwortliche mit Hauptniederlassung in Thüringen und für nicht-öffentliche Stellen; Online-Formular und Postweg; Pflichtangaben in der Reihenfolge der Berliner Goldstandard-Struktur I bis VI; Sonderregelungen aus ThürDSG Thüringer Datenschutzgesetz; Eingangsbestätigung; Aktenzeichen; Nachmeldung. Output: einreichungsfertige Meldung als Fließtext mit Erläuterung der Eingabewege. Abgrenzung: keine Risikobewertung; keine Benachrichtigung Art. 34 DSGVO.

### Meldung Art. 33 DSGVO an die TLfDI

## Triage — kläre vor der Bearbeitung

1. Ist die TLfDI tatsächlich zuständig (Sitzland, Lead Authority Art. 56 DSGVO)?
2. Liegt ein nicht-öffentlicher oder öffentlicher Verantwortlicher vor?
3. Welcher Eingabeweg ist vorgegeben (Online-Formular versus Post versus E-Mail)?
4. Welche Sonderregelung aus ThürDSG Thüringer Datenschutzgesetz ist zu beachten?
5. Ist eine vorläufige Meldung sinnvoll und wann erfolgt die Nachmeldung?
- Was will der Mandant wirklich erreichen? (akzeptierte Erstmeldung in 72 h; keine Rückfragen)

## Rechtsgrundlagen

- **Art. 33 DSGVO** Meldepflicht.
- **Art. 55 DSGVO** Zuständigkeit der Aufsichtsbehörde.
- **ThürDSG Thüringer Datenschutzgesetz** landesrechtliche Sondervorschriften für öffentliche Stellen.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Bußgeldpraxis der TLfDI vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33; Art. 55; Art. 5 Abs. 2 DSGVO; ThürDSG Thüringer Datenschutzgesetz.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Behördenstammdaten TLfDI

- Name: Thüringer Landesbeauftragter für den Datenschutz und die Informationsfreiheit
- Anschrift: Häßlerstraße 8; 99096 Erfurt
- Kontakt: poststelle@datenschutz.thueringen.de; Telefon 0361 57311-2900
- Online-Meldeformular: tlfdi.de — Online-Meldeformular Datenpanne
- Sondernorm: ThürDSG Thüringer Datenschutzgesetz
- Bundesland: Thüringen

Hinweis: Adressen und URLs werden vor Versendung über die offizielle Behördenseite verifiziert; sie können sich ändern.

## Berliner Struktur als Goldstandard

Die Meldeformular-Vorlage der Berliner Beauftragten für Datenschutz und Informationsfreiheit deckt strukturell alle Pflichtangaben nach Art. 33 Abs. 3 DSGVO ab und wird als inhaltliche Pruefliste verwendet. Die Meldung gliedert sich in sechs Bloecke:

**I. Wo ist die Datenpanne passiert?**
- Verantwortliche Stelle (Unternehmen, Verein, Praxis, Behörde) — Name, Anschrift, Webseite, Branche.
- Angaben zur meldenden Person — Name, Funktion, dienstliche E-Mail, Telefon.

**II. Was ist passiert?**
- Art der Datenpanne (Vertraulichkeit, Integritaet, Verfuegbarkeit; konkrete Kategorie).
- Beschreibung — was ist passiert; welche Fehler oder Sicherheitsluecken; welche technischen Systeme und Dienste.
- Auftragsverarbeiter beteiligt — falls ja Name und Anschrift.
- Beginn und Dauer der Datenpanne; ggf. fruehestmoeglichen Zeitpunkt.
- Datum der Kenntnisnahme (loest 72-Stunden-Frist aus).
- Betroffene Datenarten — Namen; Adressen; E-Mail-Adressen; Standort; Geburtsdatum; Passwoerter; Personalausweisnummer; Pass; Steuernummer; Bankdaten; wirtschaftliche Verhaeltnisse; Straftaten; politische Meinungen; religioese Ueberzeugungen; Gewerkschaftszugehoerigkeit; Gesundheit; Sexualitaet; ethnische Herkunft; Biometrie; Identifikationsnummern; Fotos/Videos; unbekannt.
- Art. 9 DSGVO-Daten ja/nein/nicht bekannt.
- Kategorien betroffener Personen — Mitarbeitende; Nutzer; Kunden; Patienten; Politiker; Kinder/Minderjaehrige; Personen öffentlichen Lebens; andere.
- Anzahl betroffener Personen (Obergrenze).
- Anzahl betroffener Datensaetze.
- Wahrscheinliche Folgen für Betroffene — Geheimnisoffenbarung; wirtschaftliche Nachteile; finanzieller Schaden; Bloss­stellung; Rufschaedigung; Verlust des Arbeitsplatzes; Existenzgefaehrdung; Lebensgefaehrdung; Diskriminierung; gesellschaftliche Nachteile; Identitaetsdiebstahl; Aufhebung Pseudonymisierung; andere.

**III. Welche Gegenmassnahmen wurden ergriffen oder werden vorgeschlagen?**
- Bereits eingeleitete und geplante Gegenmassnahmen zur Schadensminderung und zur kuenftigen Verhinderung.
- Vorbestehende technische und organisatorische Massnahmen sowie Begruendung, weswegen sie nicht ausgereicht haben.
- Information der Betroffenen ja/nein; wie und wann; welche Empfehlungen; bei nein Begruendung zu Art. 34 DSGVO.

**IV. Sonstige Mitteilungen an die Aufsichtsbehoerde**
- Andere Behörden eingeschaltet (mit Aktenzeichen).
- Strafanzeige (Dienststelle, Aktenzeichen).
- Sonstige Hinweise.

**V. Dokumente**
- Forensischer Untersuchungsbericht.
- Auflistung der technischen und organisatorischen Massnahmen.
- Muster Benachrichtigungsschreiben Art. 34 DSGVO.
- Schluesselmaterial (PGP).

**VI. Abschluss**
- Vorlaeufige Meldung ja/nein; bei vorläufiger Meldung Ergaenzung binnen 14 Tagen.

Diese sechs Bloecke werden in jeder Behörden-spezifischen Meldung adressiert; die Reihenfolge kann je nach Formular variieren.

## Praxisformulierung — Einreichungsablauf

1. Erstmeldung über das Online-Formular oder per E-Mail an die unten genannte Adresse.
2. Pflichtangaben in der Reihenfolge der Berliner Goldstandard-Struktur (Block I bis VI).
3. Anlagen als PDF (forensischer Bericht; TOM-Liste; Muster Benachrichtigung).
4. Bei Bedarf vorläufige Meldung mit Hinweis auf Nachreichung binnen 14 Tagen.
5. Eingangsbestätigung archivieren; Aktenzeichen in das interne Vorfallregister übernehmen.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-meldung-art-33-pflichtangaben` liefert die generische Pflichtinhalte-Vorlage.
- `dsv-nachmeldung-aktualisierung-art-33-abs-4` deckt die Nachmeldung ab.

## 2. `dsv-meldung-uld-sh`

**Fokus:** Reicht eine Meldung nach Art. 33 DSGVO bei der Unabhängiges Landeszentrum für Datenschutz Schleswig-Holstein (ULD) ein. Behandelt: Zuständigkeit für Verantwortliche mit Hauptniederlassung in Schleswig-Holstein und für nicht-öffentliche Stellen; Online-Formular und Postweg; Pflichtangaben in der Reihenfolge der Berliner Goldstandard-Struktur I bis VI; Sonderregelungen aus LDSG Schleswig-Holstein; Eingangsbestätigung; Aktenzeichen; Nachmeldung. Output: einreichungsfertige Meldung als Fließtext mit Erläuterung der Eingabewege. Abgrenzung: keine Risikobewertung; keine Benachrichtigung Art. 34 DSGVO.

### Meldung Art. 33 DSGVO an die ULD

## Triage — kläre vor der Bearbeitung

1. Ist die ULD tatsächlich zuständig (Sitzland, Lead Authority Art. 56 DSGVO)?
2. Liegt ein nicht-öffentlicher oder öffentlicher Verantwortlicher vor?
3. Welcher Eingabeweg ist vorgegeben (Online-Formular versus Post versus E-Mail)?
4. Welche Sonderregelung aus LDSG Schleswig-Holstein ist zu beachten?
5. Ist eine vorläufige Meldung sinnvoll und wann erfolgt die Nachmeldung?
- Was will der Mandant wirklich erreichen? (akzeptierte Erstmeldung in 72 h; keine Rückfragen)

## Rechtsgrundlagen

- **Art. 33 DSGVO** Meldepflicht.
- **Art. 55 DSGVO** Zuständigkeit der Aufsichtsbehörde.
- **LDSG Schleswig-Holstein** landesrechtliche Sondervorschriften für öffentliche Stellen.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Bußgeldpraxis der ULD vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33; Art. 55; Art. 5 Abs. 2 DSGVO; LDSG Schleswig-Holstein.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Behördenstammdaten ULD

- Name: Unabhängiges Landeszentrum für Datenschutz Schleswig-Holstein
- Anschrift: Holstenstraße 98; 24103 Kiel
- Kontakt: mail@datenschutzzentrum.de; Telefon 0431 988-1200
- Online-Meldeformular: datenschutzzentrum.de — Online-Meldeformular Datenpanne
- Sondernorm: LDSG Schleswig-Holstein
- Bundesland: Schleswig-Holstein

Hinweis: Adressen und URLs werden vor Versendung über die offizielle Behördenseite verifiziert; sie können sich ändern.

## Berliner Struktur als Goldstandard

Die Meldeformular-Vorlage der Berliner Beauftragten für Datenschutz und Informationsfreiheit deckt strukturell alle Pflichtangaben nach Art. 33 Abs. 3 DSGVO ab und wird als inhaltliche Pruefliste verwendet. Die Meldung gliedert sich in sechs Bloecke:

**I. Wo ist die Datenpanne passiert?**
- Verantwortliche Stelle (Unternehmen, Verein, Praxis, Behörde) — Name, Anschrift, Webseite, Branche.
- Angaben zur meldenden Person — Name, Funktion, dienstliche E-Mail, Telefon.

**II. Was ist passiert?**
- Art der Datenpanne (Vertraulichkeit, Integritaet, Verfuegbarkeit; konkrete Kategorie).
- Beschreibung — was ist passiert; welche Fehler oder Sicherheitsluecken; welche technischen Systeme und Dienste.
- Auftragsverarbeiter beteiligt — falls ja Name und Anschrift.
- Beginn und Dauer der Datenpanne; ggf. fruehestmoeglichen Zeitpunkt.
- Datum der Kenntnisnahme (loest 72-Stunden-Frist aus).
- Betroffene Datenarten — Namen; Adressen; E-Mail-Adressen; Standort; Geburtsdatum; Passwoerter; Personalausweisnummer; Pass; Steuernummer; Bankdaten; wirtschaftliche Verhaeltnisse; Straftaten; politische Meinungen; religioese Ueberzeugungen; Gewerkschaftszugehoerigkeit; Gesundheit; Sexualitaet; ethnische Herkunft; Biometrie; Identifikationsnummern; Fotos/Videos; unbekannt.
- Art. 9 DSGVO-Daten ja/nein/nicht bekannt.
- Kategorien betroffener Personen — Mitarbeitende; Nutzer; Kunden; Patienten; Politiker; Kinder/Minderjaehrige; Personen öffentlichen Lebens; andere.
- Anzahl betroffener Personen (Obergrenze).
- Anzahl betroffener Datensaetze.
- Wahrscheinliche Folgen für Betroffene — Geheimnisoffenbarung; wirtschaftliche Nachteile; finanzieller Schaden; Bloss­stellung; Rufschaedigung; Verlust des Arbeitsplatzes; Existenzgefaehrdung; Lebensgefaehrdung; Diskriminierung; gesellschaftliche Nachteile; Identitaetsdiebstahl; Aufhebung Pseudonymisierung; andere.

**III. Welche Gegenmassnahmen wurden ergriffen oder werden vorgeschlagen?**
- Bereits eingeleitete und geplante Gegenmassnahmen zur Schadensminderung und zur kuenftigen Verhinderung.
- Vorbestehende technische und organisatorische Massnahmen sowie Begruendung, weswegen sie nicht ausgereicht haben.
- Information der Betroffenen ja/nein; wie und wann; welche Empfehlungen; bei nein Begruendung zu Art. 34 DSGVO.

**IV. Sonstige Mitteilungen an die Aufsichtsbehoerde**
- Andere Behörden eingeschaltet (mit Aktenzeichen).
- Strafanzeige (Dienststelle, Aktenzeichen).
- Sonstige Hinweise.

**V. Dokumente**
- Forensischer Untersuchungsbericht.
- Auflistung der technischen und organisatorischen Massnahmen.
- Muster Benachrichtigungsschreiben Art. 34 DSGVO.
- Schluesselmaterial (PGP).

**VI. Abschluss**
- Vorlaeufige Meldung ja/nein; bei vorläufiger Meldung Ergaenzung binnen 14 Tagen.

Diese sechs Bloecke werden in jeder Behörden-spezifischen Meldung adressiert; die Reihenfolge kann je nach Formular variieren.

## Praxisformulierung — Einreichungsablauf

1. Erstmeldung über das Online-Formular oder per E-Mail an die unten genannte Adresse.
2. Pflichtangaben in der Reihenfolge der Berliner Goldstandard-Struktur (Block I bis VI).
3. Anlagen als PDF (forensischer Bericht; TOM-Liste; Muster Benachrichtigung).
4. Bei Bedarf vorläufige Meldung mit Hinweis auf Nachreichung binnen 14 Tagen.
5. Eingangsbestätigung archivieren; Aktenzeichen in das interne Vorfallregister übernehmen.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-meldung-art-33-pflichtangaben` liefert die generische Pflichtinhalte-Vorlage.
- `dsv-nachmeldung-aktualisierung-art-33-abs-4` deckt die Nachmeldung ab.

## 3. `dsv-nachmeldung-aktualisierung-art-33-abs-4`

**Fokus:** Erstellt die Nachmeldung zu einer vorläufigen Erstmeldung nach Art. 33 Abs. 4 DSGVO. Behandelt: 14-Tage-Frist der Berliner Praxis; Ergänzung der Datenarten; Korrektur der Anzahl Betroffener; Update der Gegenmaßnahmen; Information zur Pressemitteilung; Verweis auf Forensikbericht; Mitteilung zur Strafanzeige; Schluss der Meldung. Output: Nachmeldungs-Schreiben mit Bezug auf Aktenzeichen der Erstmeldung. Abgrenzung: keine neue Erstmeldung.

### Nachmeldung und Aktualisierung nach Art. 33 Abs. 4 DSGVO

## Triage — kläre vor der Bearbeitung

1. Liegt das Aktenzeichen der Erstmeldung vor?
2. Welche Felder waren in der Erstmeldung noch offen oder vorläufig?
3. Liegt zwischenzeitlich ein Forensikbericht vor?
4. Hat sich die Risikoeinschätzung verändert?
5. Wurde Art. 34 DSGVO zwischenzeitlich ausgelöst?
- Was will der Mandant wirklich erreichen? (saubere Akte; Behörde schließt Vorgang)

## Rechtsgrundlagen

- **Art. 33 Abs. 4 DSGVO** schrittweise Übermittlung.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht.
- **§ 51 BlnDSG** und vergleichbare Landesnormen.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Frage, ob neue Erkenntnisse den 72-Stunden-Lauf neu auslösen können, vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 4; Art. 33 Abs. 5; Art. 5 Abs. 2 DSGVO; § 51 BlnDSG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Nachmeldungstext

Betreff: Nachmeldung zur Datenpannenmeldung [Aktenzeichen] vom [Datum].

Sehr geehrte Damen und Herren, im Anschluss an die vorläufige Meldung vom [Datum] übermittle ich für die [Verantwortliche Stelle] folgende Ergänzungen:

1. Aktualisierte Sachverhaltsdarstellung [...].
2. Endgültige Anzahl betroffener Personen [...] und Datensätze [...].
3. Forensik-Ergebnisse [...]; der Bericht ist als Anlage beigefügt.
4. Umgesetzte und geplante Gegenmaßnahmen [...].
5. Bewertung der Benachrichtigungspflicht Art. 34 DSGVO [...].
6. Status anderer Behörden und Strafanzeige [...].

Mit dieser Nachmeldung gilt die Meldung als endgültig.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-meldung-art-33-pflichtangaben` deckt die Erstmeldung ab.

## 4. `dsv-risikobewertung-edsa-leitlinie`

**Fokus:** Führt die Risikobewertung eines Datenschutzvorfalls anhand der EDSA-Leitlinie 9/2022 zu Beispielen für die Meldung von Datenschutzverletzungen durch. Behandelt: Beispielfallgruppen Ransomware; Datenexfiltration; Insider; Verlust; Fehlversand; soziale Ingenieurkunst; jeweils mit Schwere-Schwellen für Meldepflicht Art. 33 DSGVO und Benachrichtigungspflicht Art. 34 DSGVO. Output: strukturierte Bewertung mit Bezug auf konkrete Beispielfallgruppe und begründeter Empfehlung Meldung Ja/Nein und Benachrichtigung Ja/Nein. Abgrenzung: keine Behördenmeldung; keine ENISA-Methodik.

### Risikobewertung nach EDSA-Leitlinie 9/2022

## Triage — kläre vor der Bearbeitung

1. Welcher EDSA-Beispielfallgruppe ist der Vorfall am nächsten?
2. Welche Schutzziele sind verletzt — Vertraulichkeit, Integrität, Verfügbarkeit?
3. Wie hoch ist die Anzahl Betroffener und welche Datenkategorien sind involviert?
4. Welche technischen und organisatorischen Maßnahmen waren wirksam?
5. Welche Risikoabmilderung wurde bereits umgesetzt?
- Was will der Mandant wirklich erreichen? (begründete Risikoeinschätzung; Behörden-feste Argumentation)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldepflicht außer kein Risiko.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigung bei hohem Risiko.
- **Erwägungsgrund 75; 76 DSGVO** Risikofaktoren.
- **EDSA-Leitlinien 9/2022** Beispiele für die Meldung von Datenschutzverletzungen (englisch: Examples regarding Personal Data Breach Notification).
- **EDSA-Leitlinien 4/2022** Berechnung von Geldbußen.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Anwendungspraxis der Aufsichtsbehörden zu EDSA-Beispielen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 1; Art. 34 Abs. 1 DSGVO; Erwägungsgrund 75; 76; EDSA-Leitlinien 9/2022.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Anwendung EDSA-Beispiele

Fallgruppe identifizieren: Ransomware mit/ohne Exfiltration; Datenexfiltration Hashes Passwörter; Insider absichtlich/unabsichtlich; Verlust verschlüsselt/unverschlüsselt; Fehlversand mit Empfängerrückläufer; soziale Ingenieurkunst.

Schwellenwerte EDSA: Meldung an Aufsichtsbehörde regelmäßig bei Ransomware mit unverschlüsselten Daten oder Exfiltration; Benachrichtigung Betroffene bei Klartext-Passwörtern, Finanzdaten, Gesundheitsdaten.

Risikomatrix: Eintrittswahrscheinlichkeit × Schwere; Begründung mit EDSA-Referenz und Begründung aus dem konkreten Fall.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-risikobewertung-enisa-schweregrad` ergaenzt um quantitative ENISA-Methodik.

## 5. `dsv-risikobewertung-enisa-schweregrad`

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

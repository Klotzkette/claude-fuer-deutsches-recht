---
name: it-recht-aufnahme-statusinformation-benachrichtigung-art
description: "Aufnahme Statusinformation Benachrichtigung ART im Plugin Fachanwalt It Recht: prüft konkret Erstellt nach einem gemeldeten Datenschutzvorfall eine, Prüft die Ausnahmen von der Benachrichtigungspflicht nach, Erstellt das Benachrichtigungsschreiben an die von einer, Bewertet. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Aufnahme Statusinformation Benachrichtigung ART

## Arbeitsbereich

**Aufnahme Statusinformation Benachrichtigung ART** ordnet den Fall über die tragenden Prüfungslinien: Erstellt nach einem gemeldeten Datenschutzvorfall eine, Prüft die Ausnahmen von der Benachrichtigungspflicht nach, Erstellt das Benachrichtigungsschreiben an die von einer. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `dsv-aufnahme-statusinformation` | Erstellt nach einem gemeldeten Datenschutzvorfall eine knappe Statusinformation an Mandant und Datenschutzbeauftragten in Fließtextform. Behandelt: Vorgangsbezeichnung; Zeitpunkt der Kenntnisnahme; Eingang Service-Desk und Datenschutzpostfach; Sachverhaltskurzfassung; 72-Stunden-Endpunkt als Datum und Uhrzeit; Ampelstatus grün gelb rot schwarz mit Begründung; aktuelle Einschätzung; Bewertung Meldepflicht nach Art. 33 DSGVO; Bewertung Informationspflicht nach Art. 34 DSGVO; nächster Schritt mit Verantwortlichem. Output: Fließtext-Memo 100-300 Wörter; matter-of-factly; Reasoning vor Conclusion in jedem Feld. Abgrenzung: keine Behördenmeldung; keine Risikobewertung im engeren Sinne. |
| `dsv-benachrichtigung-art-34-ausnahmen` | Prüft die Ausnahmen von der Benachrichtigungspflicht nach Art. 34 Abs. 3 DSGVO. Behandelt: lit. a technische und organisatorische Maßnahmen (insb. Verschlüsselung) die Daten unverständlich machen; lit. b nachträgliche Maßnahmen die hohes Risiko nicht mehr eintreten lassen; lit. c unverhältnismäßiger Aufwand mit öffentlicher Bekanntmachung als Ersatz; Darlegungs- und Beweislast; Behördenakzeptanz. Output: Ausnahmenprüfungs-Memo mit Begründung. Abgrenzung: keine Schwellenwertentscheidung. |
| `dsv-benachrichtigung-art-34-betroffene` | Erstellt das Benachrichtigungsschreiben an die von einer Datenschutzverletzung betroffenen Personen nach Art. 34 DSGVO. Behandelt: Pflichtinhalte nach Art. 34 Abs. 2 DSGVO; klare und einfache Sprache; Beschreibung der Art der Verletzung; Kontaktdaten des Datenschutzbeauftragten; wahrscheinliche Folgen; ergriffene und vorgeschlagene Abhilfemaßnahmen; konkrete Empfehlungen für Betroffene; Hotline; Versandweg E-Mail oder Brief. Output: Anschreiben mit Q&A. Abgrenzung: keine öffentliche Bekanntmachung; keine Behördenmeldung. |
| `dsv-benachrichtigung-art-34-schwelle-hohes-risiko` | Bewertet, ob die Schwelle voraussichtlich hohes Risiko nach Art. 34 Abs. 1 DSGVO erreicht ist. Behandelt: Abgrenzung zur Meldeschwelle Art. 33 Abs. 1 DSGVO; EDSA-Beispielfallgruppen; Faktoren Schwere und Wahrscheinlichkeit; Sondergruppen Art. 9 DSGVO und Minderjährige; Klartext-Passwörter; Finanzdaten; Gesundheitsdaten; Bewertungsmemo für die Akte. Output: Schwellenentscheidung mit Begründung und Bezug auf EDSA. Abgrenzung: keine konkrete Benachrichtigung; keine Ausnahmenprüfung. |
| `dsv-beweissicherung` | Strukturiert die Beweissicherung nach einem Datenschutzvorfall so, dass die Beweismittel in einem späteren Bußgeldverfahren, Strafverfahren oder Zivilprozess verwertbar bleiben. Behandelt: Chain of Custody; Logging-Sicherung; Speicherabbilder; Hashes; Zeugenidentifikation; Dokumentation der Wahrnehmungen; Aufbewahrungsfristen; Datenschutzbeschränkungen bei Mitarbeiterüberwachung; Telekommunikationsgeheimnis. Output: Beweissicherungs-Protokoll mit Checkliste und Übergabeformular. Abgrenzung: keine eigene Forensik; keine Strafanzeige. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `dsv-aufnahme-statusinformation`

**Fokus:** Erstellt nach einem gemeldeten Datenschutzvorfall eine knappe Statusinformation an Mandant und Datenschutzbeauftragten in Fließtextform. Behandelt: Vorgangsbezeichnung; Zeitpunkt der Kenntnisnahme; Eingang Service-Desk und Datenschutzpostfach; Sachverhaltskurzfassung; 72-Stunden-Endpunkt als Datum und Uhrzeit; Ampelstatus grün gelb rot schwarz mit Begründung; aktuelle Einschätzung; Bewertung Meldepflicht nach Art. 33 DSGVO; Bewertung Informationspflicht nach Art. 34 DSGVO; nächster Schritt mit Verantwortlichem. Output: Fließtext-Memo 100-300 Wörter; matter-of-factly; Reasoning vor Conclusion in jedem Feld. Abgrenzung: keine Behördenmeldung; keine Risikobewertung im engeren Sinne.

# Datenschutzvorfall — Erstaufnahme als Statusinformation

## Triage — kläre vor der Bearbeitung

1. Wann genau wurde der Vorfall durch wen bemerkt und an welche interne Stelle gemeldet?
2. Welche Datenkategorien und welcher Personenkreis sind potenziell betroffen?
3. Ist der 72-Stunden-Lauf nach Art. 33 Abs. 1 DSGVO bereits angestoßen oder läuft er noch?
4. Welche Sofortmaßnahmen wurden bereits getroffen und welche stehen aus?
5. Wer ist Empfänger der Statusinformation — Geschäftsleitung, Datenschutzbeauftragter, Vorstand, externer Berater?
- Was will der Mandant wirklich erreichen? (Lagebild, Entscheidungsgrundlage Meldung, Eskalation, Dokumentation)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldepflicht binnen 72 Stunden ab Kenntniserlangung an die zuständige Aufsichtsbehörde.
- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht jedes Vorfalls unabhängig von der Meldepflicht.
- **Art. 34 DSGVO** Benachrichtigung der betroffenen Personen bei voraussichtlich hohem Risiko.
- **§ 42 BDSG** Strafvorschriften bei vorsätzlicher unbefugter Offenlegung.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht des Verantwortlichen.

## Aktuelle Rechtsprechung

Rechtsprechung wird nicht aus Modellwissen zitiert; aktuelle Entscheidungen des EuGH und BGH zur Auslegung der 72-Stunden-Frist und zum Kenntnisbegriff sind vor Ausgabe über die unten genannten Quellen zu verifizieren.

## Zentrale Normen

Art. 4 Nr. 12; Art. 33 Abs. 1; Art. 33 Abs. 3; Art. 33 Abs. 5; Art. 34 Abs. 1 DSGVO; § 42 BDSG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Statusinformation (Stilreferenz Fließtext)

Vorgang: kurze sprechende Bezeichnung des Vorfalls.

Kenntnisnahme: Wer hat wann was durch welche Wahrnehmung erkannt — Reasoning vor Conclusion.

Eingang Service-Desk: Zeitpunkt und Ticketnummer mit kurzer Begründung der Zuordnung.

Eingang Datenschutzpostfach: Zeitpunkt der formalen Weiterleitung an die Datenschutzorganisation.

Sachverhalt: drei bis fünf Sätze; was ist passiert; welche Systeme; welche Datenkategorien; welcher Personenkreis.

72-Stunden-Endpunkt: konkretes Datum und Uhrzeit mit Bezug auf den Kenntnisnahmezeitpunkt.

Ampelstatus: 🟢 unkritisch / 🟡 beobachtet / 🔴 meldepflichtig / ⚫ benachrichtigungspflichtig — mit kurzer Erläuterung.

Aktuelle Einschätzung: technische und organisatorische Lage; eingrenzbar oder nicht.

Bewertung: Wahrscheinlichkeit eines Risikos für die Rechte und Freiheiten; Reasoning vor Conclusion.

Meldepflicht Art. 33: ja / nein / noch offen mit Begründung.

Informationspflicht Art. 34: ja / nein / noch offen mit Begründung.

Nächster Schritt: konkret, mit Verantwortlichem und Zeitpunkt.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 2. `dsv-benachrichtigung-art-34-ausnahmen`

**Fokus:** Prüft die Ausnahmen von der Benachrichtigungspflicht nach Art. 34 Abs. 3 DSGVO. Behandelt: lit. a technische und organisatorische Maßnahmen (insb. Verschlüsselung) die Daten unverständlich machen; lit. b nachträgliche Maßnahmen die hohes Risiko nicht mehr eintreten lassen; lit. c unverhältnismäßiger Aufwand mit öffentlicher Bekanntmachung als Ersatz; Darlegungs- und Beweislast; Behördenakzeptanz. Output: Ausnahmenprüfungs-Memo mit Begründung. Abgrenzung: keine Schwellenwertentscheidung.

# Ausnahmen von der Benachrichtigungspflicht nach Art. 34 Abs. 3 DSGVO

## Triage — kläre vor der Bearbeitung

1. Welche Verschlüsselung war wirksam und entspricht dem Stand der Technik?
2. Welche nachträglichen Maßnahmen reduzieren das Risiko nachweisbar?
3. Welcher Aufwand wäre für die individuelle Benachrichtigung tatsächlich angefallen?
4. Welche öffentliche Bekanntmachung kommt als Ersatz in Betracht?
5. Welche Beweise dokumentieren die Ausnahme?
- Was will der Mandant wirklich erreichen? (rechtssichere Nichtbenachrichtigung; saubere Akte)

## Rechtsgrundlagen

- **Art. 34 Abs. 3 lit. a DSGVO** technische Schutzmaßnahmen.
- **Art. 34 Abs. 3 lit. b DSGVO** nachträgliche Maßnahmen.
- **Art. 34 Abs. 3 lit. c DSGVO** unverhältnismäßiger Aufwand und öffentliche Bekanntmachung.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Erwägungsgrund 86 DSGVO**.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu lit. a Verschlüsselungsstandards und lit. c unverhältnismäßiger Aufwand vor Ausgabe verifizieren.

## Zentrale Normen

Art. 34 Abs. 3 lit. a-c; Art. 5 Abs. 2 DSGVO; Erwägungsgrund 86.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Ausnahmenprüfung

lit. a: Verschlüsselung nachweisen — Algorithmus, Schlüsselverwaltung, Stand der Technik (BSI-Empfehlungen). Reasoning vor Conclusion.

lit. b: Nachträgliche Maßnahmen mit Wirksamkeitsnachweis dokumentieren.

lit. c: Aufwandsabschätzung mit Vergleich zum Risiko; öffentliche Bekanntmachung Format und Reichweite.

Beweislast: liegt beim Verantwortlichen — schriftlich dokumentieren mit Datum und Verantwortlichem.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-pressemitteilung-krisenkommunikation` deckt die öffentliche Bekanntmachung ab.

## 3. `dsv-benachrichtigung-art-34-betroffene`

**Fokus:** Erstellt das Benachrichtigungsschreiben an die von einer Datenschutzverletzung betroffenen Personen nach Art. 34 DSGVO. Behandelt: Pflichtinhalte nach Art. 34 Abs. 2 DSGVO; klare und einfache Sprache; Beschreibung der Art der Verletzung; Kontaktdaten des Datenschutzbeauftragten; wahrscheinliche Folgen; ergriffene und vorgeschlagene Abhilfemaßnahmen; konkrete Empfehlungen für Betroffene; Hotline; Versandweg E-Mail oder Brief. Output: Anschreiben mit Q&A. Abgrenzung: keine öffentliche Bekanntmachung; keine Behördenmeldung.

# Benachrichtigung der Betroffenen nach Art. 34 DSGVO

## Triage — kläre vor der Bearbeitung

1. Liegt die Schwelle voraussichtlich hohes Risiko nach Art. 34 Abs. 1 DSGVO vor?
2. Welche Adressdaten der Betroffenen sind vorhanden?
3. Welcher Versandweg ist sachgerecht (E-Mail, Brief, Push-Nachricht)?
4. Welche konkreten Schutzempfehlungen können gegeben werden?
5. Welche Hotline oder E-Mail-Adresse steht zur Verfügung?
- Was will der Mandant wirklich erreichen? (rechtskonforme Benachrichtigung; Vertrauenserhalt; Sammelklagen-Schutz)

## Rechtsgrundlagen

- **Art. 34 Abs. 1 DSGVO** Benachrichtigung bei voraussichtlich hohem Risiko.
- **Art. 34 Abs. 2 DSGVO** Pflichtinhalte und klare einfache Sprache.
- **Art. 34 Abs. 3 DSGVO** Ausnahmen.
- **Art. 12 DSGVO** Transparenz.
- **§ 29 BDSG** Beschränkungen.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Form der Benachrichtigung und zu Sammelklagen wegen unvollständiger Benachrichtigung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 12; Art. 34 Abs. 1; Art. 34 Abs. 2; Art. 34 Abs. 3 DSGVO; § 29 BDSG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Benachrichtigungsschreiben

Betreff: Wichtige Information zu einem Datenschutzvorfall.

Sehr geehrte/r [Name],

wir möchten Sie darüber informieren, dass es am [Datum] in unserem Unternehmen zu einer Verletzung des Schutzes personenbezogener Daten gekommen ist, von der auch Ihre Daten betroffen sind.

Was ist passiert: [klare einfache Beschreibung in zwei bis drei Sätzen].

Welche Ihrer Daten sind betroffen: [konkrete Aufzählung].

Welche Folgen sind möglich: [realistische Einschätzung ohne Verharmlosung und ohne Panikmache].

Was wir bereits unternommen haben: [Sofortmaßnahmen].

Was wir Ihnen empfehlen: [konkrete Schritte — Passwort ändern, Konten beobachten, Schufa-Auskunft einholen, je nach Fall].

Kontakt: Datenschutzbeauftragter [Name, E-Mail, Telefon]; Hotline [Nummer]; FAQ [URL].

Wir entschuldigen uns für die entstandene Unannehmlichkeit und stehen Ihnen für Rückfragen zur Verfügung.

Mit freundlichen Grüßen, [Geschäftsleitung]

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-benachrichtigung-art-34-schwelle-hohes-risiko` deckt die Schwellenwertentscheidung ab.
- `dsv-benachrichtigung-art-34-ausnahmen` deckt die Ausnahmen ab.

## 4. `dsv-benachrichtigung-art-34-schwelle-hohes-risiko`

**Fokus:** Bewertet, ob die Schwelle voraussichtlich hohes Risiko nach Art. 34 Abs. 1 DSGVO erreicht ist. Behandelt: Abgrenzung zur Meldeschwelle Art. 33 Abs. 1 DSGVO; EDSA-Beispielfallgruppen; Faktoren Schwere und Wahrscheinlichkeit; Sondergruppen Art. 9 DSGVO und Minderjährige; Klartext-Passwörter; Finanzdaten; Gesundheitsdaten; Bewertungsmemo für die Akte. Output: Schwellenentscheidung mit Begründung und Bezug auf EDSA. Abgrenzung: keine konkrete Benachrichtigung; keine Ausnahmenprüfung.

# Schwelle hohes Risiko nach Art. 34 Abs. 1 DSGVO

## Triage — kläre vor der Bearbeitung

1. Welche Schwere der Folgen ist plausibel und welche Wahrscheinlichkeit?
2. Welche EDSA-Beispielfallgruppe passt (Klartext-Passwort-Leak; Gesundheitsdaten-Leak; Finanzdaten-Leak)?
3. Sind besondere Schutzbedürftige betroffen (Kinder, Patienten)?
4. Welche Beweislast trifft den Verantwortlichen?
5. Welche Folgewirkung hat die Entscheidung auf Pressekommunikation und Bußgeldverfahren?
- Was will der Mandant wirklich erreichen? (begründete Entscheidung; Verteidigungsfähigkeit)

## Rechtsgrundlagen

- **Art. 34 Abs. 1 DSGVO** Schwellenwert.
- **Erwägungsgrund 75; 76; 86 DSGVO**.
- **EDSA-Leitlinien 9/2022** Beispiele.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Entscheidungen zur Schwellenwertentscheidung Art. 34 DSGVO vor Ausgabe verifizieren.

## Zentrale Normen

Art. 34 Abs. 1; Art. 5 Abs. 2 DSGVO; Erwägungsgrund 75; 76; 86; EDSA-Leitlinien 9/2022.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Bewertungsraster

Faktor 1 Schwere: gering / mittel / hoch / sehr hoch.

Faktor 2 Wahrscheinlichkeit: gering / mittel / hoch.

Faktor 3 Datenkategorie: normale Daten / Art. 9 / Finanzdaten / Identitätsdaten.

Faktor 4 Personengruppe: Erwachsene / Minderjährige / Patienten / besonders Schutzbedürftige.

Conclusion: hohes Risiko ab Schwere hoch + Wahrscheinlichkeit mittel; bei Art. 9 + Kinder regelmäßig zu bejahen.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-risikobewertung-edsa-leitlinie` und `dsv-risikobewertung-enisa-schweregrad` liefern methodische Tiefe.

## 5. `dsv-beweissicherung`

**Fokus:** Strukturiert die Beweissicherung nach einem Datenschutzvorfall so, dass die Beweismittel in einem späteren Bußgeldverfahren, Strafverfahren oder Zivilprozess verwertbar bleiben. Behandelt: Chain of Custody; Logging-Sicherung; Speicherabbilder; Hashes; Zeugenidentifikation; Dokumentation der Wahrnehmungen; Aufbewahrungsfristen; Datenschutzbeschränkungen bei Mitarbeiterüberwachung; Telekommunikationsgeheimnis. Output: Beweissicherungs-Protokoll mit Checkliste und Übergabeformular. Abgrenzung: keine eigene Forensik; keine Strafanzeige.

# Beweissicherung nach Datenschutzvorfall — Chain of Custody

## Triage — kläre vor der Bearbeitung

1. Welche Systeme und Speichermedien sind potenziell Beweismittel?
2. Gibt es Hinweise auf einen Innentäter und damit besondere Anforderungen an die Vertraulichkeit?
3. Liegt Telekommunikationsgeheimnis nach § 3 TTDSG vor?
4. Welche Aufbewahrungsfristen gelten für die Logs?
5. Wer übernimmt die forensische Sicherung — interne IT oder externer Forensiker?
- Was will der Mandant wirklich erreichen? (gerichtsverwertbare Beweise; saubere Akte; spätere Verteidigung)

## Rechtsgrundlagen

- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 32 DSGVO** angemessene Sicherheitsmaßnahmen.
- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht.
- **§ 26 BDSG** Mitarbeiterdatenverarbeitung.
- **§ 3 TTDSG** Fernmeldegeheimnis.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Beweisverwertungsverboten bei verdeckter Mitarbeiterkontrolle vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 32; Art. 33 Abs. 5 DSGVO; § 26 BDSG; § 3 TTDSG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Chain-of-Custody-Protokoll

Asset-ID; Beschreibung; Sicherungszeitpunkt; sichernde Person; Übergabezeitpunkt; übernehmende Person; Hashwert vor/nach Sicherung; Aufbewahrungsort; Zugriffsberechtigte; Zweck der Sicherung; Rechtsgrundlage der Verarbeitung der gesicherten Daten.

Logging: Welche Log-Quellen wurden eingefroren? Welche Retention war eingestellt? Welche Lücken gibt es?

Zeugen: Wer hat wann was wahrgenommen — in eigenen Worten und mit Zeitstempel protokollieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

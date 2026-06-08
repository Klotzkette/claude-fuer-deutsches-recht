---
name: spezialfaelle-uebersicht-stakeholder
description: "DSV Spezialfaelle Uebersicht Stakeholder im Datenschutzrecht: prüft konkret Liefert eine schnelle Übersicht über häufige Spezialfälle, Kartiert alle internen und externen Stakeholder eines, Bestimmt den richtigen Tonfall und die Sprachregelung in, Bewertet. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# DSV Spezialfaelle Uebersicht Stakeholder

## Arbeitsbereich

**DSV Spezialfaelle Uebersicht Stakeholder** ordnet den Fall über die tragenden Prüfungslinien: Liefert eine schnelle Übersicht über häufige Spezialfälle, Kartiert alle internen und externen Stakeholder eines, Bestimmt den richtigen Tonfall und die Sprachregelung in. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `dsv-spezialfaelle-uebersicht` | Liefert eine schnelle Übersicht über häufige Spezialfälle eines Datenschutzvorfalls und verweist auf vertiefte Skills. Behandelt: Ransomware; Insider-Threat; Fehlversand E-Mail/Brief; Endgeräteverlust; verlorener Datenträger; Cloud-Fehlkonfiguration; offene S3-Buckets; kompromittiertes E-Mail-Konto; Phishing-Erfolg; Schatten-IT; kompromittierter Dienstleister; Web-Defacement; Datenleck durch Whistleblower. Output: Übersichts-Matrix mit Erstbewertung und Verweisen auf vertiefte Skills. Abgrenzung: ersetzt nicht die Einzelbewertung. |
| `dsv-stakeholder-mapping` | Kartiert alle internen und externen Stakeholder eines Datenschutzvorfalls inklusive Informationsbedarf, Zeitpunkt und Verantwortlicher. Behandelt: Geschäftsleitung; Datenschutzbeauftragter; IT-Sicherheit; Betriebsrat; Auftragsverarbeiter; gemeinsam Verantwortliche; Cyberversicherung; Aufsichtsbehörde; Strafverfolgungsbehörden; Betroffene; Großkunden mit Vertragsklauseln; Presse; Sozialmedien. Output: Stakeholder-Matrix mit Eskalations- und Informationsplan. Abgrenzung: keine konkreten Schreiben. |
| `dsv-tonfall-krisenkommunikation` | Bestimmt den richtigen Tonfall und die Sprachregelung in der Krisenkommunikation nach einem Datenschutzvorfall. Behandelt: Vermeidung von Verharmlosung; Vermeidung von Panikmache; matter-of-factly; Reasoning vor Conclusion; Vermeidung selbstbelastender Aussagen; keine voreiligen Schuldzuweisungen; Empathie ohne Anerkenntnis; rechtliche Grenzen (§ 824 BGB; § 4 UWG; Art. 5 Abs. 1 lit. a DSGVO). Output: Sprachregel-Leitfaden mit Beispielsätzen Do/Don't. Abgrenzung: keine Pressemitteilung; keine individuelle Benachrichtigung. |
| `dsv-verdacht-vs-festgestellt` | Bewertet, ob der Mandant bereits Kenntnis von einer Verletzung im Sinne Art. 33 Abs. 1 DSGVO hat oder ob noch bloßer Verdacht vorliegt. Behandelt: Abgrenzung Verdacht und Kenntnis; angemessene Sicherheit der Feststellung; Pflicht zur unverzüglichen Aufklärung; Erwägungsgrund 87; Dokumentationspflichten in der Verdachtsphase; Risiko einer verspäteten Meldung. Output: Memo zur Einordnung und Begründung des Fristbeginns. Abgrenzung: keine eigene Meldung; keine Risikobewertung. |
| `dsv-zeitleiste` | Erstellt eine minutiös rekonstruierte Zeitleiste vom Eintritt der Verletzung bis zur Meldung und Benachrichtigung. Behandelt: Eintritt; Erstwahrnehmung; Meldung an Service-Desk; Eingang Datenschutzpostfach; Kenntnisbegriff Art. 33 DSGVO; 72-Stunden-Lauf; Sofortmaßnahmen; Forensik-Beauftragung; Meldung an Aufsichtsbehörde; Benachrichtigung Betroffene; Pressemitteilung; Nachmeldung. Output: tabellarische Zeitleiste mit Quellen und Rechtsfolgen. Abgrenzung: keine Risikobewertung; keine Behördenmeldung im engeren Sinne. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `dsv-spezialfaelle-uebersicht`

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

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

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

## 2. `dsv-stakeholder-mapping`

**Fokus:** Kartiert alle internen und externen Stakeholder eines Datenschutzvorfalls inklusive Informationsbedarf, Zeitpunkt und Verantwortlicher. Behandelt: Geschäftsleitung; Datenschutzbeauftragter; IT-Sicherheit; Betriebsrat; Auftragsverarbeiter; gemeinsam Verantwortliche; Cyberversicherung; Aufsichtsbehörde; Strafverfolgungsbehörden; Betroffene; Großkunden mit Vertragsklauseln; Presse; Sozialmedien. Output: Stakeholder-Matrix mit Eskalations- und Informationsplan. Abgrenzung: keine konkreten Schreiben.

### Stakeholder-Mapping nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Vertragsbeziehungen verlangen frühzeitige Information (Banken, Großkunden, Auftragsverarbeiter)?
2. Welche Aufsichtsbehörde ist primär, welche zusätzlich (Sektoraufsicht BaFin, BSI § 8b BSIG)?
3. Ist der Konzern grenzüberschreitend tätig — Lead-Authority nach Art. 56 DSGVO?
4. Gibt es Betriebsrat und welche Beteiligungsrechte?
5. Welche Sozialmedien-Kanäle hat der Mandant?
- Was will der Mandant wirklich erreichen? (kein Stakeholder vergessen; keine Doppelkommunikation)

## Rechtsgrundlagen

- **Art. 26 DSGVO** gemeinsam Verantwortliche.
- **Art. 28 DSGVO** Auftragsverarbeiter.
- **Art. 33 DSGVO** Meldepflicht.
- **Art. 56 DSGVO** federführende Aufsichtsbehörde.
- **§ 8b BSIG** Meldepflicht bei kritischen Infrastrukturen.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Abgrenzung gemeinsam Verantwortlicher und reiner Auftragsverarbeitung vor Ausgabe verifizieren.

## Zentrale Normen

Art. 26; Art. 28; Art. 33; Art. 56 DSGVO; § 8b BSIG; § 109 TKG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Stakeholder-Matrix-Spalten

Stakeholder; Rolle; Pflicht oder freiwillig; Zeitpunkt; Verantwortlicher intern; Format der Information; abgestimmte Kernbotschaft; Eskalationsstufe.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 3. `dsv-tonfall-krisenkommunikation`

**Fokus:** Bestimmt den richtigen Tonfall und die Sprachregelung in der Krisenkommunikation nach einem Datenschutzvorfall. Behandelt: Vermeidung von Verharmlosung; Vermeidung von Panikmache; matter-of-factly; Reasoning vor Conclusion; Vermeidung selbstbelastender Aussagen; keine voreiligen Schuldzuweisungen; Empathie ohne Anerkenntnis; rechtliche Grenzen (§ 824 BGB; § 4 UWG; Art. 5 Abs. 1 lit. a DSGVO). Output: Sprachregel-Leitfaden mit Beispielsätzen Do/Don't. Abgrenzung: keine Pressemitteilung; keine individuelle Benachrichtigung.

### Tonfall und Sprache in der Krisenkommunikation nach Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Zielgruppe wird angesprochen (Betroffene, Presse, Mitarbeiter, Großkunden)?
2. Welcher Markenton ist beim Mandanten etabliert?
3. Welche Aussagen sind faktenfest belegbar?
4. Welche Aussagen wären selbstbelastend im Bußgeldverfahren?
5. Welche Aussagen wären zivilrechtlich riskant?
- Was will der Mandant wirklich erreichen? (Vertrauenserhalt; keine Selbstbelastung; keine Sammelklagen-Munition)

## Rechtsgrundlagen

- **Art. 12 Abs. 1 DSGVO** klare einfache Sprache.
- **Art. 34 Abs. 2 DSGVO** Inhalt der Benachrichtigung.
- **Art. 5 Abs. 1 lit. a DSGVO** Transparenz.
- **§ 824 BGB** Kreditgefährdung.
- **§ 4 UWG** Mitbewerberschutz.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Wortlaut-Streitigkeiten in Massendatenpannen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 1 lit. a; Art. 12 Abs. 1; Art. 34 Abs. 2 DSGVO; § 824 BGB; § 4 UWG.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Do/Don't

Do: konkrete Beschreibung des Vorfalls; konkrete Folgen; konkrete Empfehlungen; respektvolle Anrede; Hotline.

Don't: Pauschalentschuldigungen ohne Bezug; Schuldzuweisungen an Dritte ohne Beleg; Versprechungen Es-kann-nicht-mehr-passieren; juristische Wertungen wie kein-Risiko ohne Beleg.

Empathie ohne Anerkenntnis: Wir bedauern den Vorfall; wir verstehen Ihre Sorge; wir prüfen alle erforderlichen Schritte.

Reasoning vor Conclusion: erst Beschreibung der Lage; dann Bewertung; dann Empfehlung.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-pressemitteilung-krisenkommunikation` deckt die Pressemitteilung ab.
- `dsv-benachrichtigung-art-34-betroffene` deckt das Anschreiben ab.

## 4. `dsv-verdacht-vs-festgestellt`

**Fokus:** Bewertet, ob der Mandant bereits Kenntnis von einer Verletzung im Sinne Art. 33 Abs. 1 DSGVO hat oder ob noch bloßer Verdacht vorliegt. Behandelt: Abgrenzung Verdacht und Kenntnis; angemessene Sicherheit der Feststellung; Pflicht zur unverzüglichen Aufklärung; Erwägungsgrund 87; Dokumentationspflichten in der Verdachtsphase; Risiko einer verspäteten Meldung. Output: Memo zur Einordnung und Begründung des Fristbeginns. Abgrenzung: keine eigene Meldung; keine Risikobewertung.

### Verdacht versus festgestellte Verletzung — Kenntnisbegriff Art. 33 DSGVO

## Triage — kläre vor der Bearbeitung

1. Worauf basiert der Verdacht — Logeintrag, Anruf, Drittmeldung, Pressebericht?
2. Welche internen Prüfungen wurden bereits durchgeführt?
3. Liegen objektive Anhaltspunkte für eine Verletzung vor oder reine Spekulation?
4. Wie lange dauert die Aufklärung voraussichtlich?
5. Welche Sofortmaßnahmen sind während der Aufklärung sinnvoll?
- Was will der Mandant wirklich erreichen? (Rechtssicherheit beim Fristbeginn; keine voreilige Falschmeldung)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldung ab Kenntniserlangung.
- **Erwägungsgrund 87 DSGVO** unverzügliche Feststellung mit angemessener Sicherheit.
- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht auch in der Verdachtsphase.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Maßstäben angemessener Sicherheit der Feststellung und Reichweite der Aufklärungspflicht vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 1; Art. 33 Abs. 5; Art. 5 Abs. 2 DSGVO; Erwägungsgrund 87.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Einordnungsraster

Phase Verdacht: kein Fristbeginn; Dokumentation der eingeleiteten Aufklärungsschritte.

Phase qualifizierte Kenntnis: Fristbeginn 72 Stunden; Festlegung des Zeitpunkts.

Maßstab: ein verständiger Verantwortlicher würde von einer Verletzung ausgehen — Reasoning zuerst dann Conclusion.

Dokumentationsbausteine: was wurde wann wahrgenommen; welche Prüfungen wurden eingeleitet; welche Ergebnisse haben den Verdacht zur Kenntnis verdichtet.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## 5. `dsv-zeitleiste`

**Fokus:** Erstellt eine minutiös rekonstruierte Zeitleiste vom Eintritt der Verletzung bis zur Meldung und Benachrichtigung. Behandelt: Eintritt; Erstwahrnehmung; Meldung an Service-Desk; Eingang Datenschutzpostfach; Kenntnisbegriff Art. 33 DSGVO; 72-Stunden-Lauf; Sofortmaßnahmen; Forensik-Beauftragung; Meldung an Aufsichtsbehörde; Benachrichtigung Betroffene; Pressemitteilung; Nachmeldung. Output: tabellarische Zeitleiste mit Quellen und Rechtsfolgen. Abgrenzung: keine Risikobewertung; keine Behördenmeldung im engeren Sinne.

### Zeitleiste des Datenschutzvorfalls — minutiöse Rekonstruktion

## Triage — kläre vor der Bearbeitung

1. Aus welchen Quellen lässt sich der Zeitstrahl rekonstruieren — Logs, E-Mails, Tickets, Aussagen?
2. Welche Zeitstempel sind in welcher Zeitzone protokolliert?
3. Wann genau hat der Verantwortliche im Sinne Art. 33 DSGVO Kenntnis erlangt?
4. Wann beginnt der 72-Stunden-Lauf — Erstwahrnehmung oder qualifizierte Kenntnis?
5. Gibt es Lücken, die durch Zeugenaussagen geschlossen werden müssen?
- Was will der Mandant wirklich erreichen? (verteidigungsfähige Zeitachse; Begründung Fristbeginn)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Kenntnisbegriff und 72-Stunden-Frist.
- **Erwägungsgrund 87 DSGVO** unverzügliche Feststellung.
- **Art. 33 Abs. 4 DSGVO** schrittweise Übermittlung.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Auslegung Kenntnisbegriff und zum Beginn der 72-Stunden-Frist vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 1; Art. 33 Abs. 4; Art. 5 Abs. 2 DSGVO; Erwägungsgrund 87.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Zeitleisten-Spalten

Datum/Uhrzeit (Zeitzone); Ereignis; Quelle; Akteur; Rechtsfolge; Anmerkungen; Beweismittel.

Wichtig: Kenntnisbegriff sauber dokumentieren — ein bloßer Verdacht oder Hinweis löst noch nicht den Fristlauf aus; maßgeblich ist die qualifizierte Kenntnis im Sinne Erwägungsgrund 87.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

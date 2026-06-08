---
name: trade-conflict
description: "Untersucht Geheimnisverrat und Trade-Secret-Leaks – GeschGehG, § 17 UWG a.F., Täteridentifizierung, einstweilige Verfügung, Strafanzeige im Internal Investigations Praxis."
---

# Trade-Secret-Leak und Geheimnisverrat

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Der Schutz von Geschäftsgeheimnissen richtet sich nach dem GeschGehG (Gesetz zum Schutz von Geschäftsgeheimnissen, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/)), das die EU-Richtlinie 2016/943 ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943)) umsetzt. Strafrechtlich ist § 23 GeschGehG (Strafbarkeit Geheimnisverrat) und § 17 UWG a. F. (heute weitgehend durch GeschGehG ersetzt) relevant. Täter können Mitarbeiter, ehemalige Mitarbeiter, Wettbewerber oder staatliche Akteure (Industriespionage) sein. Sofortmaßnahmen und einstweilige Verfügungen sind zeitkritisch.

## Ziel dieses Skills

Dieser Skill identifiziert den Täter, sichert Beweise und leitet zivil- und strafrechtliche Maßnahmen sowie einstweiligen Rechtsschutz ein.

## Arbeitsprogramm

### 1. Schadensfeststellung und Scope-Analyse
- Was wurde abgeflossen? Welche Geschäftsgeheimnisse (Definition § 2 Nr. 1 GeschGehG)?
- Wie wurde es abgeflossen? E-Mail-Versand, USB, Cloud-Upload, mündliche Weitergabe?
- An wen wurde es weitergegeben? Wettbewerber, ausländische Regierung, Presse?
- Welche wirtschaftlichen Schäden sind entstanden oder drohen?

### 2. Täteridentifizierung – Digitale Forensik
- **Access Logs**: Wer hat auf die betreffenden Dateien/Systeme zugegriffen (wann, wie oft)?
- **DLP-Systeme**: Data Loss Prevention – Alerts auf ungewöhnliche Downloads oder E-Mail-Ausgang?
- **USB-Protokolle**: Wurden USB-Sticks an Unternehmensgeräten verwendet?
- **Cloud-Upload-Logs**: Uploads zu Dropbox, Google Drive, persönlichen Konten?
- **E-Mail-Header**: externe Weitergabe via privater E-Mail-Adressen?
- **Printing-Logs**: ungewöhnliche Druckaufträge vor dem Ausscheiden?

### 3. Datenschutzrechtliche Grenzen der Tätersuche
- § 26 BDSG: Forensik zur Aufdeckung einer Straftat (§ 23 GeschGehG) zulässig bei konkreten Verdachtsmomenten.
- Verhältnismäßigkeit: gezielte Suche, keine Massenüberwachung.
- Betriebsrat: Mitbestimmung bei Einrichtung von DLP-Systemen (§ 87 Abs. 1 Nr. 6 BetrVG); ad-hoc-Forensik im Verdachtsfall regelmäßig ohne Mitbestimmung.
- § 202a StGB: kein unberechtigter Zugriff auf Systeme, auch nicht zur Tätersuche.

### 4. Einstweilige Verfügung
- § 935 ZPO: einstweilige Verfügung gegen Täter und Empfänger zur Unterlassung weiterer Nutzung des Geheimnisses.
- §§ 6, 7 GeschGehG: Ansprüche auf Unterlassung, Beseitigung, Schadensersatz, Herausgabe.
- Dringlichkeit: einstweilige Verfügung muss unverzüglich beantragt werden; Kammergericht Berlin akzeptiert oft 4-6 Wochen als Frist.
- Ex-parte-Verfügung (ohne Anhörung des Antragsgegners): bei Gefahr der Vernichtung von Beweisen möglich.

### 5. Strafanzeige
- § 23 GeschGehG: Strafbarkeit des Täters; Freiheitsstrafe bis zu 3 Jahren.
- Strafantrag erforderlich (§ 23 Abs. 4 GeschGehG); Frist 3 Monate ab Kenntnis.
- § 17 UWG a. F. noch relevant für Altfälle (vor GeschGehG 2019).
- ZAC (Zentrale Ansprechstelle Cybercrime): bei IT-gestütztem Geheimnisverrat.
- Wirtschaftsspionage durch ausländische Staatsstellen: Kontakt mit Verfassungsschutz.

### 6. Arbeitsrechtliche Maßnahmen
- Außerordentliche Kündigung des Täters (§ 626 BGB): schwerwiegende Verletzung der Verschwiegenheitspflicht.
- Schadensersatzklage: § 10 GeschGehG (Schadensersatz inkl. Lizenzanalogie).
- Unterlassungserklärung durch den (ehemaligen) Mitarbeiter verlangen.
- Nachvertragliche Wettbewerbsverbote (§§ 74 ff. HGB): durchsetzen oder auf Karenzzahlung verzichten.

### 7. Präventive Maßnahmen
- GeschGehG-Anforderungen (§ 2 Nr. 1): aktive Geheimhaltungsmaßnahmen sind Schutzvoraussetzung.
- NDA für alle Mitarbeiter und Auftragnehmer mit Zugang zu Geheimnissen.
- Need-to-know-Prinzip bei Datenzugriff.
- DLP-Systeme und USB-Beschränkungen einrichten (mit Betriebsratseinbindung).
- Regelmäßige Überprüfung der Zugriffsberechtigungen.

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| GeschGehG §§ 2, 6, 7, 10 | Schutz, Ansprüche | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/) |
| § 23 GeschGehG | Strafbarkeit Geheimnisverrat | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/__23.html) |
| § 935 ZPO | Einstweilige Verfügung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/__935.html) |
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| EU-RL 2016/943 | Geheimnisschutzrichtlinie | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943) |

## Ausgabeformate

- **Digitale-Forensik-Checkliste** für Trade-Secret-Leak
- **Einstweilige-Verfügungs-Antrag** (Musterstruktur)
- **Strafanzeige** nach § 23 GeschGehG
- **Kündigung und Unterlassungserklärung** für Täter
- **GeschGehG-Schutzmaßnahmen-Audit**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.


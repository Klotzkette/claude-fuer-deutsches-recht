---
name: inv-betriebsrat-datenschutz
description: "Inv 006 Betriebsrat, Inv 007 Datenschutz: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 006 Betriebsrat, Inv 007 Datenschutz

## Arbeitsbereich

Dieser Skill bündelt **Inv 006 Betriebsrat, Inv 007 Datenschutz** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-006-betriebsrat` | Klärt Mitbestimmungsrechte des Betriebsrats bei Internal Investigations – Überwachung, Interviews, Datenzugriffe, Sanktionen. |
| `inv-007-datenschutz` | Prüft DSGVO/BDSG bei E-Mail-Auswertung, Chatlogs, Forensik, Zugriffen, Drittstaatentransfer und Betroffenenrechten in Internal Investigations. |

## Arbeitsweg

Für **Inv 006 Betriebsrat, Inv 007 Datenschutz** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-006-betriebsrat`

**Fokus:** Klärt Mitbestimmungsrechte des Betriebsrats bei Internal Investigations – Überwachung, Interviews, Datenzugriffe, Sanktionen.

# Betriebsrat und Mitbestimmung in Internal Investigations

## Rechtlicher Rahmen

Der Betriebsrat ist in Internal Investigations ein zentraler Akteur, dessen Rechte zwingend zu beachten sind. Missachtung von Mitbestimmungsrechten führt zur Unverwertbarkeit von Beweismitteln in Arbeitsgerichtsverfahren und kann das gesamte Untersuchungsergebnis delegitimieren. Die einschlägigen Normen sind §§ 80, 87, 99, 102 BetrVG ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/)). Gleichzeitig hat der Betriebsrat eine Verschwiegenheitspflicht nach § 79 BetrVG, die in Untersuchungen relevant ist, wenn er sensible Informationen über Betroffene erhält.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass der Betriebsrat rechtzeitig, vollständig und in rechtlich gebotener Form einbezogen wird, ohne dass die Untersuchung durch überschießende Mitbestimmungsrechte faktisch blockiert wird.

## Arbeitsprogramm

### 1. Allgemeines Überwachungsrecht (§ 80 BetrVG)
- § 80 Abs. 1 BetrVG: Der Betriebsrat hat das Recht, darüber zu wachen, dass zugunsten der Arbeitnehmer geltende Gesetze, Tarifverträge und Betriebsvereinbarungen durchgeführt werden ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__80.html)).
- Folge: Betriebsrat hat ein allgemeines Auskunftsrecht über laufende Untersuchungen, nicht aber ein Einsichtsrecht in privilegierte Anwaltsdokumente.
- Grenze: § 80 Abs. 2 BetrVG erfordert ausreichende Unterrichtung, aber keine Offenlegung von Berufsgeheimnissen oder personenbezogenen Daten unbeteiligter Dritter.

### 2. Mitbestimmung bei technischer Überwachung (§ 87 Abs. 1 Nr. 6 BetrVG)
- Technische Einrichtungen, die das Verhalten oder die Leistung von Arbeitnehmern überwachen, bedürfen der Zustimmung des Betriebsrats ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html)).
- Anwendungsfälle: E-Mail-Auswertung, Keylogger, GPS-Tracking, Videoüberwachung, Chat-Monitoring.
- Keine Mitbestimmung bei anlassbezogener forensischer Auswertung bereits existierender Daten, wenn kein fortlaufendes Überwachungssystem eingerichtet wird (BAG, Beschl. v. 26.8.2008 – 1 ABR 16/07).
- Betriebsvereinbarung als Erlaubnisgrundlage und Schranke (§ 26 Abs. 1 S. 2 BDSG, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)).

### 3. Mitbestimmung bei Ordnungsmaßnahmen (§ 87 Abs. 1 Nr. 1 BetrVG)
- Verhaltensregeln, die Ordnung oder Verhalten im Betrieb betreffen, unterliegen der Mitbestimmung.
- Interviewobliegenheiten (z. B. Pflicht zur Teilnahme an Befragungen) können als Ordnungsmaßnahme qualifizieren.
- Mitbestimmungspflicht gilt nicht für Maßnahmen des konkreten Einzelfalls bei konkretem Verdacht.

### 4. Anhörung vor Kündigung (§ 102 BetrVG)
- Jede ordentliche und außerordentliche Kündigung ist vorher dem Betriebsrat mitzuteilen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__102.html)).
- Kündigung ohne ordnungsgemäße Anhörung ist unwirksam (§ 102 Abs. 1 S. 3 BetrVG).
- Inhalt der Mitteilung: alle für die Kündigungsentscheidung maßgeblichen Umstände – nicht mehr, nicht weniger.
- Problematik: Kann der Betriebsrat aus der Anhörungsmitteilung Rückschlüsse auf noch laufende Untersuchungsmaßnahmen ziehen?

### 5. Zustimmung bei Versetzung und Eingruppierung (§§ 99, 100 BetrVG)
- Versetzung eines verdächtigen Mitarbeiters zur Beweissicherung: § 99 BetrVG-Zustimmung erforderlich ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__99.html)).
- Vorläufige Maßnahmen nach § 100 BetrVG möglich, wenn dringende betriebliche Erfordernisse vorliegen.

### 6. Verschwiegenheitspflicht des Betriebsrats (§ 79 BetrVG)
- Betriebsratsmitglieder sind zur Verschwiegenheit über Betriebs- und Geschäftsgeheimnisse verpflichtet ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__79.html)).
- Personenbezogene Daten von Betroffenen: Betriebsrat darf diese nicht an Dritte weitergeben.
- Verletzung kann zur Amtsenthebung und Strafbarkeit nach § 203 StGB führen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__203.html)).

### 7. Betriebsrat als Konfliktpartei
- Was tun, wenn der Betriebsrat selbst in den Untersuchungsgegenstand involviert ist (z. B. Betriebsratsmitglied als Beschuldigter)?
- Sonderregelung § 103 BetrVG: Außerordentliche Kündigung von Betriebsratsmitglied bedarf Zustimmung des Betriebsrats oder Ersetzung durch Arbeitsgericht ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__103.html)).
- Befangenheit des Betriebsrats bei Interessenkollision: Mitglied muss sich für betreffende Beschlüsse enthalten.

## Red-Team-Fragen

- Wurde der Betriebsrat über die Untersuchung informiert, bevor technische Überwachungsmaßnahmen ergriffen wurden?
- Liegt für alle eingesetzten Überwachungstools eine Betriebsvereinbarung oder eine ad-hoc-Zustimmung des Betriebsrats vor?
- Wurde die Betriebsratsanhörung nach § 102 BetrVG korrekt durchgeführt, bevor Kündigungen ausgesprochen wurden?
- Hat der Betriebsrat Zugang zu vertraulichen Ermittlungsdokumenten erhalten, der über sein § 80-Recht hinausgeht?
- Ist ein Betriebsratsmitglied selbst Beschuldigter, und wurde das Verfahren nach § 103 BetrVG eingeleitet?
- Wurde die Verschwiegenheitspflicht des Betriebsrats in die Informationsweitergabe eingepreist?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 80 BetrVG | Überwachungsrecht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__80.html) |
| § 87 BetrVG | Mitbestimmung Ordnung / Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |
| § 99 BetrVG | Mitbestimmung Versetzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__99.html) |
| § 102 BetrVG | Anhörung vor Kündigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__102.html) |
| § 103 BetrVG | Kündigung Betriebsratsmitglied | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__103.html) |
| § 79 BetrVG | Schweigepflicht Betriebsrat | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__79.html) |

## Ausgabeformate

- **Mitbestimmungsmatrix**: Maßnahme × BetrVG-Norm × Zustimmungserfordernis
- **Informationsschreiben** an Betriebsrat (§ 80 BetrVG)
- **Betriebsratsanhörung** nach § 102 BetrVG (Kündigungsfall)
- **Checkliste** Betriebsratsbeteiligung für jede Untersuchungsphase

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-007-datenschutz`

**Fokus:** Prüft DSGVO/BDSG bei E-Mail-Auswertung, Chatlogs, Forensik, Zugriffen, Drittstaatentransfer und Betroffenenrechten in Internal Investigations.

# Datenschutz in Internal Investigations

## Rechtlicher Rahmen

Internal Investigations sind datenschutzrechtlich hochriskant. Jede Verarbeitung personenbezogener Daten von Mitarbeitern, Verdächtigen oder Zeugen bedarf einer Rechtsgrundlage nach der DSGVO ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679)) und dem BDSG ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/)). Die Kernorm für Beschäftigtendaten ist § 26 BDSG, der für die Verarbeitung zur Aufdeckung von Straftaten spezifische Voraussetzungen aufstellt ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)). Verstöße gegen die DSGVO können zu Bußgeldern bis 20 Mio. EUR oder 4 % des weltweiten Jahresumsatzes führen (Art. 83 DSGVO) und Beweisverwertungsverbote auslösen.

## Ziel dieses Skills

Dieser Skill stellt für jede Untersuchungsmaßnahme eine DSGVO-konforme Rechtsgrundlage sicher, dokumentiert die Interessenabwägung und verhindert, dass Datenschutzverstöße das Ermittlungsergebnis oder den Bericht kompromittieren.

## Arbeitsprogramm

### 1. Rechtsgrundlagen im Überblick
- **§ 26 Abs. 1 S. 2 BDSG**: Verarbeitung zur Aufdeckung von Straftaten – tatsächliche Anhaltspunkte erforderlich, Verhältnismäßigkeit wahren ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)).
- **Art. 6 Abs. 1 lit. f DSGVO**: Berechtigtes Interesse des Unternehmens – Dreistufentest (Interesse, Notwendigkeit, Abwägung mit Betroffeneninteressen).
- **Art. 6 Abs. 1 lit. c DSGVO**: Rechtliche Verpflichtung (z. B. BaFin-Anforderungen, HinSchG-Pflichten).
- **Betriebsvereinbarung** als Erlaubnisgrundlage nach § 26 Abs. 4 BDSG.

### 2. E-Mail-Auswertung
- Zulässigkeit: § 26 BDSG bei konkretem Straftatverdacht; reine Verhaltensüberwachung ohne Verdacht regelmäßig unzulässig.
- Technische Anforderung: Suche über Schlüsselwörter (keyword search) ist weniger eingriffsintensiv als vollständiges Lesen aller E-Mails.
- Private Nutzung: Erlaubnis privater E-Mail-Nutzung schafft erhöhten Schutzanspruch (BAG-Rechtsprechung; vgl. § 88 TKG a. F. / § 3 TTDSG).
- Betriebsrat: Mitbestimmung nach § 87 Abs. 1 Nr. 6 BetrVG bei systematischer Überwachung.

### 3. Chat-Logs und Collaboration-Tools
- Teams, Slack, WhatsApp: grundsätzlich wie E-Mail zu behandeln.
- Besonderheit: Ende-zu-Ende-Verschlüsselung (WhatsApp Business) kann Auswertung erschweren oder unmöglich machen.
- Retention-Policies der Plattformen beachten (z. B. 30-Tage-Löschung in Teams standardmäßig).
- Legal Hold muss vor Löschfrist aktiviert werden.

### 4. Forensik-Maßnahmen
- Vollständige Image-Erstellung von Laptops, Servern: eingriffsintensivste Maßnahme.
- Verhältnismäßigkeit: Ist ein vollständiges Image erforderlich, oder reicht eine gezielte Datensicherung?
- Datenminimierung (Art. 5 Abs. 1 lit. c DSGVO): Scope auf relevante Zeiträume, Ordner und Personen eingrenzen.
- Drittstaatentransfer: Forensik-Dienstleister mit US-Rechtsträger → DSGVO-Kapitel V, Standardvertragsklauseln (SCC) nach Schrems II (EuGH C-311/18, [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=228677&doclang=DE)).

### 5. Betroffenenrechte und Ausnahmen
- **Auskunftsrecht (Art. 15 DSGVO)**: Betroffener kann Auskunft über alle über ihn gespeicherten Daten verlangen – auch Interviewprotokolle.
- **Ausnahme**: Art. 23 DSGVO i. V. m. § 29 BDSG erlaubt Einschränkung der Betroffenenrechte, wenn Auskunft Untersuchung gefährden oder Rechte anderer verletzen würde.
- **Löschungsrecht (Art. 17 DSGVO)**: Entfällt während laufender Untersuchung (Art. 17 Abs. 3 lit. e DSGVO), ist aber nach Abschluss zu beachten.
- Löschkonzept für Untersuchungsdaten nach Abschluss erstellen.

### 6. Drittstaatentransfer
- US-Cloud-Dienste (AWS, Azure, M365): DSGVO-Kapitel V prüfen; EU-US-Data-Privacy-Framework 2023 aktuell anwendbar, aber Schrems-III-Risiko im Blick behalten.
- Forensik-Dienstleister mit US-Mutterfirma: DPA (Data Processing Agreement) und SCC abschließen.
- US-DOJ oder SEC-Anfrage: Herausgabe personenbezogener Daten in die USA bedarf DSGVO-Rechtsgrundlage (Art. 49 Abs. 1 lit. e DSGVO bei Strafverfolgung möglich, aber eng).

### 7. Datenpannen und Meldepflicht
- Datenpanne während Untersuchung (z. B. Leak des Berichts): Art. 33 DSGVO – Meldung an Aufsichtsbehörde binnen 72 Stunden.
- Art. 34 DSGVO: Information der Betroffenen bei hohem Risiko.
- Dokumentationspflicht (Art. 33 Abs. 5 DSGVO) auch ohne Meldepflicht.

### 8. Dokumentation
- Verzeichnis der Verarbeitungstätigkeiten (Art. 30 DSGVO) für die Untersuchung.
- Datenschutz-Folgenabschätzung (Art. 35 DSGVO) bei Hochrisikomaßnahmen (vollständige Forensik, Massenauswertung).
- DSB einbinden (Art. 38 DSGVO).

## Red-Team-Fragen

- Ist für jede Datenverarbeitungsmaßnahme eine Rechtsgrundlage dokumentiert – nicht nur behauptet?
- Wurde die Verhältnismäßigkeit (Datenminimierung, Scope) aktiv geprüft und schriftlich festgehalten?
- Gibt es Drittstaatentransfers, für die keine wirksame DSGVO-Grundlage vorliegt?
- Kann ein Betroffener per Art. 15-Anfrage Einsicht in Interviewprotokolle erzwingen – und was würde er dann sehen?
- Wurde der DSB rechtzeitig eingebunden?
- Liegt eine Datenpanne vor, die Meldepflichten nach Art. 33/34 DSGVO ausgelöst hat?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| Art. 6 DSGVO | Rechtsgrundlagen | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 17 DSGVO | Löschungsrecht | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 33 DSGVO | Meldepflicht Datenpannen | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 35 DSGVO | Datenschutz-Folgenabschätzung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| EuGH C-311/18 | Schrems II | [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=228677&doclang=DE) |

## Ausgabeformate

- **DSGVO-Rechtsgrundlagen-Matrix**: Maßnahme × Rechtsgrundlage × Risikostufe
- **Interessenabwägung** (Art. 6 Abs. 1 lit. f DSGVO) als Memo
- **Datenschutz-Folgenabschätzung** (DSFA) für Forensik-Maßnahmen
- **Drittstaatentransfer-Analyse**
- **Löschkonzept** nach Abschluss der Untersuchung

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

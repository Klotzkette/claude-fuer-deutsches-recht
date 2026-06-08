---
name: datenschutz
description: "Prüft DSGVO/BDSG bei E-Mail-Auswertung, Chatlogs, Forensik, Zugriffen, Drittstaatentransfer und Betroffenenrechten in Internal Investigations im Internal Investigations Praxis."
---

# Datenschutz in Internal Investigations

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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


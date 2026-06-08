# Offene Punkte und Lückenliste — NIS2-Cybersicherheit Lahnwerke

## Status

Stand: 02.06.2026. Mandant: Lahnwerke GmbH (Industrieprodukte, Konzerntochter Stahlring AG). Beratung: Dr. Henning Brettschneider (IT-/Cybersecurityrecht), Senior Associate L. Wenstedt.

## Offene Punkte

### 1. Rechtsquellen-Live-Check

- **BSIG** in der Fassung des NIS2-Umsetzungsgesetzes 2024/2025; insbesondere die §§ 28-37 BSIG (Risikomanagement, Meldepflicht, Geschäftsleitungspflichten). Live gegen `gesetze-im-internet.de` verifizieren.
- **NIS2-Richtlinie 2022/2555**: aktueller Stand der nationalen Umsetzung in den Mitgliedstaaten relevant, weil Lahnwerke auch in Österreich, Polen, Tschechien aktiv ist.
- **DSGVO Art. 32-34**: technische und organisatorische Maßnahmen, Meldepflichten, Benachrichtigung Betroffener.
- **Cyber Resilience Act (EU 2024/2847)**: relevant für die Frage, ob Lahnwerke-Produkte unter die Vorgaben fallen — Übergangsfrist beachten.
- **DigitalEU-VO 2018/1807**: freier Datenverkehr nicht-personenbezogener Daten — relevant für Cloud-Setup-Frage.

### 2. Fehlende technische und kaufmännische Nachweise

- **Vollständiges Asset-Inventar**: Aktuelles Asset-Inventar liegt mit Stand 03/2025 vor. Müsste auf den Stand 06/2026 aktualisiert werden — insbesondere zu OT-Komponenten (Sensorik, Steuerungen).
- **Lieferketten-Inventar**: Welche Drittanbieter haben Zugriff auf Lahnwerke-Systeme? Vollständige Liste der SaaS-Anbieter (Slack, M365, Teams-Telefonie, Salesforce, AzureDevOps), Cloud-Provider, externe Wartungsfirmen.
- **Patch-Management-Berichte** der letzten 12 Monate.
- **Notfallübungs-Protokolle** der letzten 24 Monate (existieren in welchem Umfang?).
- **Schulungsnachweise** für Beschäftigte zu Phishing und Cybersecurity.
- **AVV-Verträge mit Drittanbietern**: vollständig? Aktualität?
- **Verträge mit dem externen Forensiker** (Bittner+Renz, NorthSec): SLA, Bereitschaftsstufen, Tagessätze.

### 3. Widersprüche und Inkonsistenzen

- **Slack-Nutzung vs. interne Richtlinie**: Lahnwerke-IT-Richtlinie 2024 verbietet die Nutzung externer Messenger für vertrauliche Kommunikation. Tatsächlich nutzen Engineering und Vertrieb Slack intensiv. Diskrepanz zwischen Richtlinie und Praxis dokumentieren.
- **AirTag-Verwendung an Werkstücken**: Aktenstück 14 dokumentiert, dass Lahnwerke AirTags zur Verfolgung von Werkstücken (Lieferung an Kunden) verwendet. Datenschutzrechtliche Bewertung (Datenfluss an Apple, personenbeziehbarer Standort) ist nicht dokumentiert.
- **MFA-Coverage**: Behauptung im internen Report 04/2026: "MFA bei 95 % aller Accounts aktiv". Tatsächlich: nur 70 %, weil mehrere Service-Accounts und Wartungs-Accounts ausgenommen. Lücke schließen.

### 4. Beweisfundstellen für harte Aussagen

- Behauptung "Lahnwerke ist NIS2-pflichtig": derzeit nur Vermutung über Größenklassifizierung. Bessere Belege: Jahresabschluss Beschäftigtenzahl, Konzernzuordnung, Sektorzuordnung nach Anhang I/II der Richtlinie.
- Behauptung "kein wesentlicher Vorfall seit 2023": derzeit auf interne Vorfalls-Logs gestützt; vollständige Aufstellung mit Klassifikation nach NIS2-Wesentlichkeitskriterien anfertigen.
- Behauptung "Geschäftsleitung ist über Cybersecurity-Lage informiert": derzeit nur indirekt aus Aufsichtsratsprotokollen. Bessere Belege: konkrete Sitzungsprotokolle Geschäftsleitung mit ausdrücklicher Cybersecurity-Berichterstattung.

## Lückenliste (Dokumente)

| Lücke | Beweisthema | Beschaffungsweg | Frist | Verantwortlich | Status |
| --- | --- | --- | --- | --- | --- |
| Aktualisiertes Asset-Inventar | NIS2 § 30 BSIG | intern IT | 4 Wochen | CISO | offen |
| Lieferketten-Inventar | NIS2 § 30 BSIG | intern Einkauf + IT | 3 Wochen | Einkauf | offen |
| Patch-Management-Berichte 06/2025-06/2026 | Sorgfalt | intern IT | 1 Woche | IT-Operations | beauftragt |
| Notfallübungs-Protokolle | NIS2 Risikomanagement | intern CISO | 2 Wochen | CISO | offen |
| Schulungsnachweise Cybersecurity | NIS2 Schulungspflicht | HR | 1 Woche | HR | beauftragt |
| AVV-Verträge alle SaaS-Anbieter | DSGVO Art. 28 | Justiziariat | 2 Wochen | Justiziariat | initialisiert |
| Forensiker-SLA | Bereitschaft Vorfall | Justiziariat | 1 Woche | Justiziariat | gemacht |
| Cloud-HSM-Beschaffung Code-Signing | siehe Aktenstück 18 | IT-Operations | 5 Werktage | CISO | beauftragt |
| Datenschutzbewertung AirTag-Nutzung | DSGVO + § 4f BDSG | DSB | 2 Wochen | DSB | initialisiert |
| Slack-Nutzungsbewertung | Geschäftsgeheimnisse + DSGVO | DSB + Justiziariat | 2 Wochen | DSB | initialisiert |
| Notfalltelefonliste offline | siehe Aktenstück 16 | Sekretariat | 5 Werktage | Sekretariat | beauftragt |
| MFA-Coverage 100 % | Sorgfalt § 30 BSIG | IT-Operations | 3 Wochen | IT-Operations | offen |

## Grundregeln für die Aktenbearbeitung

- Originalquellen und aktuelle Gesetzesfassungen live prüfen — nicht aus älteren Schriftsätzen übernehmen.
- Fehlende technische oder kaufmännische Nachweise nicht durch Vermutungen ersetzen — als Lücke führen, gezielt schließen.
- Widersprüche zwischen Richtlinie, Tatsache und Vertrag explizit benennen — Risiko der unredlichen Compliance-Behauptung.
- Für jede harte Aussage Aktenfundstelle nennen — andernfalls "noch zu belegen" markieren.
- Geschäftsleitungs-Information dokumentieren, damit § 30 BSIG / Art. 20 NIS2-Pflichten nachweisbar sind.

## Nächste Aktualisierung

Donnerstag, 04.06.2026, 14:00 Uhr — vor der Geschäftsleitungssitzung.

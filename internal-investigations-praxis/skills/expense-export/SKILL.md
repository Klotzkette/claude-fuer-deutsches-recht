---
name: expense-export
description: "Untersucht Spesenabrechungs- und Reisekostenbetrug – forensische Buchprüfung, Beweissicherung, arbeitsrechtliche und strafrechtliche Konsequenzen im Internal Investigations Praxis."
---

# Spesenbetrug und Reisekostenmissbrauch

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Spesenabrechungsbetrug ist eine der häufigsten Formen des Mitarbeiterbetrugs und erfüllt regelmäßig den Tatbestand des § 263 StGB (Betrug, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__263.html)) oder § 266 StGB (Untreue, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__266.html)), wenn der Täter besondere Vertrauensstellung hat. Hinzu kommt § 370 AO (Steuerhinterziehung), wenn Falschabrechnungen steuerlich geltend gemacht werden. Für Unternehmen begründet § 130 OWiG eine Haftung, wenn fehlende Kontrollmechanismen den Missbrauch ermöglicht haben.

## Ziel dieses Skills

Dieser Skill strukturiert die forensische Untersuchung von Spesenbetrug: von der Datenbankanalyse über Dokumentenprüfung bis zu den arbeitsrechtlichen und strafrechtlichen Maßnahmen.

## Arbeitsprogramm

### 1. Datenanalyse – Erste Auffälligkeiten
- **Statistische Ausreißer**: Mitarbeiter mit überdurchschnittlich hohen Spesenabrechnungen im Vergleich zu Peers.
- **Timing-Analyse**: Abrechnungen direkt nach Jahresendabrechnung oder kurz vor Ausscheiden.
- **Doppelabrechnung**: dieselbe Leistung zweimal abgerechnet (z. B. Taxi und Mietwagen für dieselbe Strecke).
- **Phantomrechnungen**: Lieferanten, die nicht existieren oder keine Leistung erbracht haben.
- **Round-Numbers-Test**: Rechnungen in runden Beträgen (z. B. genau 999 EUR kurz unter Genehmigungsgrenze).
- **Benford's Law**: führende Ziffern der Abrechnungsbeträge auf Manipulation prüfen.

### 2. Dokumentenprüfung
- Originalbelege verlangen: Kreditkartenabrechnung, Quittung, Hotelbuchungsbestätigung.
- Abgleich mit externen Quellen: Flugbuchungen, Hotelraten, Taxiquittungen.
- Modifizierte Belege (PDF-Manipulation): Metadaten, Schriftarten, Formatierungsfehler prüfen.
- Lieferantenregister: Existenz und Aktivität der in Rechnungen genannten Unternehmen prüfen (Handelsregister).

### 3. Digitale Forensik
- E-Mails: Kommunikation mit Lieferanten; Selbstbuchungen; Genehmigungsanfragen.
- Systeme: ERP-Buchungen (SAP, Oracle), Kreditkartensystemdaten, Reisebuchungstools.
- Zugriffsrechte: Hatte der Täter Zugriff auf Genehmigungsprozesse, die er manipulieren konnte?
- Temporäre Dateien: gelöschte Dokumente, Entwürfe (in forensischen Images oder Backup).

### 4. Interviews
- Täter-Interview: erst nach vollständiger Dokumenten- und Datenanalyse; Konfrontation mit konkreten Belegen.
- Zeugen: Kollegen, Vorgesetzte, Genehmiger; haben sie Auffälligkeiten wahrgenommen?
- Kontrollperson: Wer hat die Abrechnungen genehmigt? Mitverantwortung?
- Belehrung: wenn strafrechtliche Relevanz, nemo tenetur.

### 5. Schadensberechnung
- Vollständige Berechnung des Schadens: zu Unrecht erstattete Beträge + steuerliche Nachteile des Unternehmens.
- Gegenrechnung: Steuererstattungen, die auf betrügerischen Abrechnungen basieren → auch Schadensposition.
- Zeitraum: Wie lange dauerte der Betrug? Verjährung (§ 78 StGB, § 195 BGB)?

### 6. Arbeitsrechtliche und strafrechtliche Konsequenzen
- Außerordentliche Kündigung: Betrug am Arbeitgeber ist regelmäßig ein wichtiger Grund (§ 626 BGB); kein Abmahnungserfordernis bei erheblichem Betrug.
- Strafanzeige: § 263 oder § 266 StGB; Ermessen des Unternehmens; Interessenabwägung (Öffentlichkeit vs. Reputationsschaden).
- Schadensersatz: § 249 BGB; Einbehalt des letzten Gehalts auf Basis einer Aufrechnung (Aufrechnung nach § 387 BGB mit zu Unrecht erstatteten Beträgen).

### 7. Systemic Findings
- Wie war der Betrug möglich? Fehlende Vier-Augen-Prinzipien, fehlende Belegnachweise, überhöhte Genehmigungsgrenzen.
- Remediation: Kontrollen verschärfen, Spending-Limits anpassen, Prüfung externer Lieferanten automatisieren.
- § 130 OWiG: Fehlende Kontrollen können selbst bußgeldbewehrt sein.

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 263 StGB | Betrug | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__263.html) |
| § 266 StGB | Untreue | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__266.html) |
| § 370 AO | Steuerhinterziehung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/__370.html) |
| § 626 BGB | Außerordentliche Kündigung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__626.html) |
| § 130 OWiG | Aufsichtspflichtverletzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html) |

## Ausgabeformate

- **Spesenbetrugs-Analyse-Template** (Statistische Ausreißer, Doppelbuchungen, Phantomrechnungen)
- **Dokumenten-Prüfmatrix** (Beleg × Originalcheck × Ergebnis)
- **Schadensberechnungs-Tabelle**
- **Kündigungsschreiben** bei Spesenbetrug
- **Remediation-Maßnahmenplan** (Kontrolllücken schließen)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.


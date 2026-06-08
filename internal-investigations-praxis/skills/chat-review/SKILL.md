---
name: chat-review
description: "Sichert und wertet Chat-Kommunikation (Teams, Slack, WhatsApp, Signal) in Internal Investigations aus – Retention, Forensik, DSGVO im Internal Investigations Praxis."
---

# Chat-Review in Internal Investigations

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Chat-Kommunikation über Microsoft Teams, Slack, WhatsApp Business oder Signal ist in Internal Investigations ein wachsend wichtiger Beweismittelpool. Sie unterliegt denselben datenschutzrechtlichen Anforderungen wie E-Mails (§ 26 BDSG, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html); Art. 6 DSGVO) und der Betriebsratsmitbestimmung (§ 87 Abs. 1 Nr. 6 BetrVG). Besondere technische Herausforderungen bestehen bei Ende-zu-Ende-verschlüsselten Diensten (Signal, WhatsApp) und bei kurzen Retention-Perioden (Teams standardmäßig 30 Tage). Regulatorische Anforderungen an Finanzinstitute (z. B. BaFin-Rundschreiben, MiFID II Record-Keeping) verlangen spezifische Archivierungslösungen.

## Ziel dieses Skills

Dieser Skill sichert alle relevanten Chat-Kommunikationen rechtssicher, wertet sie effizient aus und beachtet die datenschutz- und mitbestimmungsrechtlichen Grenzen.

## Arbeitsprogramm

### 1. Plattform-spezifische Sicherung
- **Microsoft Teams**: Compliance-Center (Purview) nutzen; eDiscovery-Hold setzen; Chat-History-Export möglich (Admin-Rechte erforderlich).
- **Slack**: eDiscovery-Export über Slack Enterprise Grid; kostenlose Pläne haben begrenzte History.
- **WhatsApp Business**: kein zentrales Archiv; Sicherung über Gerätespeicherung oder Cloud-Backup (iCloud, Google Drive).
- **Signal**: Ende-zu-Ende-verschlüsselt; kein serverseitiger Zugriff; nur Gerätezugriff über forensische Tools.
- **Jira/Confluence**: projektbezogene Kommunikation; Sicherung über Admin-Export.

### 2. Retention-Policies und Legal Hold
- Teams: 30-Tage-Standard-Retention deaktivieren → Compliance-Hold setzen.
- Slack: Free Plan behält nur 90 Tage; Enterprise nötig für unbegrenzte History.
- WhatsApp/Signal: keine zentrale Hold-Möglichkeit; Gerät sofort sichern.
- Legal-Hold-Notice an alle Custodians mit explizitem Hinweis auf Chat-Dienste.
- Automatische Löschroutinen deaktivieren (MDM-Profil für Unternehmensgeräte).

### 3. Forensische Sicherung
- Unternehmensgeräte: Backup-Extraktion aus MDM (Mobile Device Management) möglich.
- Private Geräte (BYOD): nur mit Einwilligung des Mitarbeiters oder nach gesonderter Rechtsgrundlage (§ 26 BDSG; verhältnismäßig?).
- Cellebrite, Oxygen Forensics: extrahieren Chat-Daten aus Mobilgeräten einschließlich gelöschter Nachrichten (wenn nicht dauerhaft gelöscht).
- Ende-zu-Ende-Verschlüsselung: Entschlüsselung nur auf Gerät möglich; Cloud-Backup ist häufig nicht E2E-verschlüsselt.

### 4. Auswertung und Kontextualisierung
- Chats ohne Kontext sind gefährlich: Emojis, Abkürzungen, GIFs können mehrdeutig sein.
- Threading: Konversationen im Zusammenhang lesen; einzelne Nachrichten herausreißen kann Sinn verzerren.
- Zeitzonenprobleme: Zeitstempel in UTC normalisieren.
- Mehrsprachige Chats: Übersetzung durch zertifizierten Übersetzer, keine automatische Maschinenübersetzung für Beweisstücke.

### 5. DSGVO und Betriebsrat
- § 26 BDSG: Verarbeitung zur Aufdeckung von Straftaten; proportionale Scope-Einschränkung.
- Betriebsrat: § 87 Abs. 1 Nr. 6 BetrVG bei systematischer Überwachung; Ad-hoc-Forensik nach konkretem Verdacht regelmäßig nicht mitbestimmungspflichtig.
- Private Chats (wenn auch auf Dienstgeräten): höherer Schutz; Filter einsetzen.
- Gruppen-Chats mit Nichtmitarbeitern: personenbezogene Daten Dritter schützen.

### 6. Regulatorische Besonderheiten (Finanzbranche)
- MiFID II Art. 16 Abs. 7: Aufzeichnungspflicht für Kommunikation im Zusammenhang mit Wertpapierdienstleistungen ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014L0065)).
- BaFin: Kommunikation über private Messaging-Dienste (WhatsApp) für regulierte Tätigkeiten grundsätzlich unzulässig; eigenständiger Compliance-Verstoß.
- Archivierungspflichten: Banken müssen Kommunikation 7 Jahre aufbewahren (§ 257 HGB).

### 7. Verwertbarkeit
- Metadaten (Zeitstempel, Geräte-ID, IP) für Integritätsnachweis sichern.
- Hash-Werte des extrahierten Datensatzes.
- Kein Selektionsbias: alle relevanten Nachrichten sichern, nicht nur belastende.

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |
| MiFID II Art. 16 | Aufzeichnungspflicht Kommunikation | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014L0065) |
| Art. 5 DSGVO | Datenminimierung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |

## Ausgabeformate

- **Plattform-Matrix** (Teams/Slack/WhatsApp × Sicherungsmethode × Retention)
- **Legal-Hold-Notice** mit Chat-spezifischen Anweisungen
- **Forensik-Protokoll** für Mobile Chat-Extraktion
- **Verwertbarkeitsanalyse** für Chat-Beweise
- **Regulatorische Archivierungsliste** (MiFID II, BaFin)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.


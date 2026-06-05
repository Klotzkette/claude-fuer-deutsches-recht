---
name: inv-e-chat
description: "Inv 016 E Mail Review, Inv 017 Chat Review: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 016 E Mail Review, Inv 017 Chat Review

## Arbeitsbereich

Dieser Skill bündelt **Inv 016 E Mail Review, Inv 017 Chat Review** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-016-e-mail-review` | Strukturiert den E-Mail-Review in Internal Investigations – Keyword-Suche, TAR, Privilege-Log, DSGVO und Verwertbarkeit. |
| `inv-017-chat-review` | Sichert und wertet Chat-Kommunikation (Teams, Slack, WhatsApp, Signal) in Internal Investigations aus – Retention, Forensik, DSGVO. |

## Arbeitsweg

Für **Inv 016 E Mail Review, Inv 017 Chat Review** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-016-e-mail-review`

**Fokus:** Strukturiert den E-Mail-Review in Internal Investigations – Keyword-Suche, TAR, Privilege-Log, DSGVO und Verwertbarkeit.

# E-Mail-Review in Internal Investigations

## Rechtlicher Rahmen

Die Auswertung von Geschäfts-E-Mails im Rahmen einer Internal Investigation ist zulässig, wenn eine Rechtsgrundlage nach § 26 BDSG oder Art. 6 Abs. 1 lit. f DSGVO vorliegt, Verhältnismäßigkeit gewahrt wird und die Betriebsratsmitbestimmung nach § 87 Abs. 1 Nr. 6 BetrVG beachtet wurde ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html)). Bei erlaubter privater E-Mail-Nutzung ist die Rechtslage komplizierter – das BAG hat wiederholt betont, dass der Schutz der privaten Kommunikation auch am Arbeitsplatz gilt. Die fehlerhafte Auswertung führt zu Beweisverwertungsverboten.

## Ziel dieses Skills

Dieser Skill steuert den E-Mail-Review von der Planung bis zur Produktion: Keyword-Entwicklung, Technology-Assisted Review (TAR), Privilege-Screening, DSGVO-Compliance und Verwertbarkeitsanalyse.

## Arbeitsprogramm

### 1. Rechtsgrundlage und Scope
- § 26 BDSG: Verarbeitung zur Aufdeckung von Straftaten – konkrete Verdachtsmomente erforderlich.
- Verhältnismäßigkeit: Zeitraum, Custodians, Postfächer eingrenzen.
- Private E-Mails: Filter einsetzen, wenn private Nutzung erlaubt; keine Auswertung ohne separate Rechtsgrundlage.
- Betriebsrat informieren (§ 80 BetrVG) und ggf. Zustimmung nach § 87 Abs. 1 Nr. 6 BetrVG einholen.

### 2. Keyword-Entwicklung
- Keyword-Liste mit Rechtsanwalt und Sachverständigen entwickeln; dokumentieren, warum jedes Keyword gewählt wurde.
- Iterativer Prozess: Ergebnisse der ersten Runde informieren verfeinerte Keywords.
- Custodian-spezifische Keywords (Spitznamen, interne Codes, Projektnamen).
- Negativliste: Keywords, die ausgeschlossen werden, und Begründung.
- Hit-Rate-Bericht: Anzahl der Treffer pro Keyword → Plausibilitätsprüfung.

### 3. Technology-Assisted Review (TAR)
- TAR/Predictive Coding: Machine-Learning-Klassifizierung von relevanten vs. nicht-relevanten Dokumenten.
- Seed-Set-Qualität: manuell überprüfte Beispieldokumente für das Training des Modells.
- Validation: Statistische Prüfung der Recall- und Precision-Werte (95 % Konfidenzintervall standard).
- Transparenz: TAR-für US-Discovery dokumentierbar; Gegenseite kann Methodik anfechten.

### 4. Privilege-Screening
- Alle Dokumente mit Anwaltskommunikation (To/From Anwalt, „privileged", „attorney-client") separat sichern.
- Privilege-Log erstellen (FRCP Rule 26(b)(5) Standard): Dokument, Datum, Autor, Empfänger, Basis des Privilege.
- Claw-Back-Vereinbarung (FRCP Rule 502(d)): Schutz vor unfreiwilligem Privilege-Waiver bei versehentlicher Produktion.
- Inadvertent Disclosure: sofortiger Claw-Back bei versehentlicher Herausgabe privilegierter Dokumente.

### 5. DSGVO-Konformität bei der Auswertung
- Reviewer dürfen nur Dokumente sehen, für die eine Rechtsgrundlage besteht.
- Drittbetroffene (Kunden, Lieferanten): personenbezogene Daten minimieren, bevor Reviewer Zugriff erhält.
- Drittstaatentransfer bei US-Review-Dienstleister: SCC, Art. 46 DSGVO.
- Review-Plattform: DSGVO-konformer Anbieter oder eigene Infrastructure.

### 6. Verwertbarkeit im Arbeits- und Strafverfahren
- E-Mail aus rechtswidrigem Zugriff (Passwortknacken, Admin-Backdoor ohne Erlaubnis): Beweisverwertungsverbot.
- Ordnungsgemäß aus Unternehmens-Server gesicherte E-Mail: grundsätzlich verwertbar, wenn DSGVO und BetrVG beachtet.
- Metadaten (Zeitstempel, IP-Adresse, E-Mail-Header): wichtige Korroboration; manipulierbar – immer prüfen.
- Hash-Wert der Original-E-Mail für Integritätsnachweis.

### 7. Dokumentation und Reporting
- Review-Log: welcher Reviewer hat wann welche Dokumente gesehen?
- Tag-Set: welche Tags wurden vergeben (relevant, privileged, hot doc, not relevant)?
- Hot-Documents-Liste: bedeutsame Dokumente mit Kurzzusammenfassung für den Anwalt.
- Produktions-Log: welche Dokumente wurden wem wann übergeben?

## Red-Team-Fragen

- Ist die Keyword-Liste dokumentiert und begründet – sodass sie vor Gericht verteidigt werden kann?
- Wurden private E-Mails gefiltert, wenn die Nutzung erlaubt war?
- Ist das Privilege-Log vollständig und im FRCP-konformen Format?
- Haben Reviewer aus Drittstaaten (US) Zugriff auf DSGVO-geschützte Daten gehabt, ohne dass eine DSGVO-Grundlage vorlag?
- Wurden E-Mail-Metadaten auf Manipulationen überprüft?
- Hat der Betriebsrat die Auswertung gebilligt, oder droht ein Beweisverwertungsverbot?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |
| Art. 5 DSGVO | Datenminimierung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 46 DSGVO | Drittstaatentransfer SCC | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |

## Ausgabeformate

- **Keyword-Liste-Vorlage** mit Hit-Rate-Spalte
- **TAR-Workflow-Dokumentation**
- **Privilege-Log-Vorlage** (FRCP Rule 26(b)(5))
- **DSGVO-Konformitätsprüfung** für E-Mail-Review
- **Hot-Documents-Zusammenfassung**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-017-chat-review`

**Fokus:** Sichert und wertet Chat-Kommunikation (Teams, Slack, WhatsApp, Signal) in Internal Investigations aus – Retention, Forensik, DSGVO.

# Chat-Review in Internal Investigations

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

## Red-Team-Fragen

- Wurden alle Chat-Plattformen identifiziert, auch die, die das Unternehmen nicht offiziell unterstützt (Shadow IT)?
- Wurden Retention-Policies rechtzeitig deaktiviert, bevor relevante Chats automatisch gelöscht wurden?
- Sind Ende-zu-Ende-verschlüsselte Dienste (Signal, WhatsApp) zugänglich, und wenn nein, welche Beweislücke entsteht?
- Wurden BYOD-Geräte rechtskonform einbezogen?
- Haben Regulatoren (BaFin) eigene Anforderungen an die Sicherung von Kommunikation, die separat zu erfüllen sind?
- Wurden Chat-Nachrichten stets im Kontext des gesamten Gesprächsverlaufs bewertet?

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

---
name: cyber-incident
description: "Reagiert auf Cyber-Incidents (Ransomware, Datenleck, APT) – DSGVO-Meldepflichten, forensische Sicherung, Behördenstrategie, Strafverfolgung im Internal Investigations Praxis."
---

# Cyber-Incident-Response und forensische Untersuchung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Cyber-Incidents lösen eine Vielzahl von Rechtspflichten aus: DSGVO Art. 33 (Meldung binnen 72 Stunden bei Datenpanne, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679)), NIS2-Richtlinie (Meldepflicht für kritische Infrastrukturen und wichtige Einrichtungen, RL (EU) 2022/2555), BSI-Gesetz (§§ 8a, 8b BSIG) und ggf. sektorspezifische Pflichten (§ 25a KWG für Banken, [bafin.de](https://www.bafin.de/)). Strafbarkeit der Täter nach §§ 202a ff. StGB; Ansprüche des Unternehmens aus §§ 823, 826 BGB.

## Ziel dieses Skills

Dieser Skill strukturiert die unmittelbare Incident-Response, die forensische Beweissicherung und alle Meldepflichten bei einem Cyber-Incident.

## Arbeitsprogramm

### 1. Incident-Klassifizierung
- **Ransomware**: Verschlüsselung von Systemen; Erpressung; oft mit Datenexfiltration kombiniert.
- **APT (Advanced Persistent Threat)**: staatlich gesponserter Angreifer; langfristiger Zugriff auf Systeme.
- **Insider-Threat**: Mitarbeiter oder ehem. Mitarbeiter mit Zugriff auf Systeme.
- **Phishing/BEC**: Business E-Mail Compromise; Überweisungsbetrug.
- **Data Leak**: unbeabsichtigte oder vorsätzliche Offenlegung personenbezogener Daten.

### 2. Sofortmaßnahmen (Incident-Response)
- Netzwerktrennung kompromittierter Systeme (Containment); keine vollständige Abschaltung, wenn forensische Spuren auf flüchtigen Daten (RAM) verloren gehen würden.
- Incident-Response-Team aktivieren (IT-Security, CISO, Anwalt, Kommunikation, Management).
- BSI informieren (§ 8b Abs. 4 BSIG) bei kritischer Infrastruktur oder erheblichem Incident.
- Logs sichern: alle relevanten Event-Logs, Netzwerk-Logs, Firewall-Logs mit Hash-Wert sichern.
- Kein Löschen von Systemen vor forensischer Sicherung.

### 3. Forensische Untersuchung
- Memory-Forensik: RAM-Dump vor Systemabschaltung; flüchtige Daten gehen bei Ausschalten verloren.
- Disk-Forensik: Forensic Imaging aller betroffenen Systeme (vgl. inv-015-forensic-imaging).
- Netzwerkanalyse: Firewall-Logs, DNS-Logs, Proxy-Logs; welche IPs kommuniziert, welche Daten exfiltriert?
- Malware-Analyse: Reverse Engineering der Schadsoftware; Command-and-Control-Server identifizieren.
- Timeline-Rekonstruktion: wann hat der Angreifer erstmals Zugriff erlangt?

### 4. DSGVO-Meldepflichten (Art. 33/34)
- 72-Stunden-Frist: Meldung bei der Aufsichtsbehörde, auch wenn noch nicht alle Fakten bekannt sind; Updates möglich.
- Inhalt der Meldung: Art der Verletzung, Kategorien und Anzahl betroffener Personen, Folgen, Maßnahmen.
- Art. 34: Information der Betroffenen, wenn hohes Risiko für Rechte und Freiheiten.
- DSB einbinden (Art. 37–39 DSGVO).

### 5. Sektorspezifische Meldepflichten
- **Banken/Finanzdienstleister**: § 25a KWG, BaFin-Rundschreiben IT-Sicherheit, EZB-Meldung bei signifikanten IT-Vorfällen.
- **Kritische Infrastruktur**: NIS2-Richtlinie (RL (EU) 2022/2555, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022L2555)); Meldung innerhalb von 24 Stunden (Early Warning).
- **Energiesektor, Gesundheitssektor**: eigene Meldepflichten nach Sektorrecht.

### 6. Strafverfolgung und behördliche Zusammenarbeit
- Strafanzeige: §§ 202a, 202c, 303a, 303b StGB; ZAC (Zentrale Ansprechstelle Cybercrime der LKAs).
- BKA: bei erheblichen Angriffen auf kritische Infrastruktur.
- Europol/FBI: bei transnationalen Angreifern.
- Beweise sichern für Strafverfolgung: Chain of Custody, Hash-Werte.
- Lösegeld zahlen? Rechtliche Risiken: Sanktionsrisiko (OFAC), Geldwäscherisiko; keine Garantie der Entschlüsselung.

### 7. Remediation und Kommunikation
- Systeme bereinigen und neu aufbauen (clean-room recovery).
- Schwachstellen schließen, die den Incident ermöglicht haben.
- Mitarbeiterkommunikation: was ist passiert, was tut das Unternehmen?
- Kundenkommunikation: falls Kundendaten betroffen.
- Pressekommunikation (vgl. inv-051-press-strategy): kontrollierte Information, keine Spekulation.

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| Art. 33 DSGVO | Datenpannen-Meldung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| §§ 8a, 8b BSIG | BSI-Meldepflichten | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bsig_2009/) |
| §§ 202a ff. StGB | Computerstrafrecht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__202a.html) |
| RL (EU) 2022/2555 | NIS2-Richtlinie | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022L2555) |
| § 25a KWG | IT-Sicherheit Banken | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/__25a.html) |

## Ausgabeformate

- **Incident-Response-Checkliste** (Containment, Forensik, Meldung)
- **DSGVO-Meldungsvorlage** Art. 33 (72-Stunden)
- **Forensik-Beauftragungstemplate** für Cyber-IR
- **Behördenmeldungs-Matrix** (BSI, BaFin, LKA, DSGVO-Behörde)
- **Kommunikationsplan** (intern, Kunden, Presse)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.


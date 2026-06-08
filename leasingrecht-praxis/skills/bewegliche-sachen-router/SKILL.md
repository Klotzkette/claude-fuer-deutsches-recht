---
name: bewegliche-sachen-router
description: "Leasing von Netzwerkequipment (Router, Switches, Access Points): Abnahme, Konfiguration, Datenlöschung, Eigentumsfragen und Rückgabe im Leasingrecht."
---

# Leasing von Netzwerkequipment: Router, Switches, Access Points

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtliche Einordnung

### Leasingobjekt: Bewegliche Sache
- Router/Switches: Bewegliche körperliche Sache (§ 90 BGB)
- Keine wesentlichen Bestandteile (§ 94 BGB): Einbau in Serverrack ist kein dauerhafter Einbau
- § 95 BGB nicht relevant: Netzwerkequipment ist ohnehin beweglich

### Software auf Hardware
- Embedded Software: Mit Hardware verkauft und lizenziert
- Firmware-Updates: Pflicht des Herstellers, Pflicht des LN zur Installation?
- Lizenz: Läuft Firmware-Lizenz mit Hardware-Leasing; endet mit Rückgabe

## Abnahme und Konfiguration

### Übergabe
- Factory Default: Hardware wird unkonfiguriert geliefert
- Konfiguration: Vom LN oder Dienstleister; Konfigurationsdaten = LN-Eigentum
- Dokumentation: Konfigurationsplan, IP-Adressen, VLAN-Konfiguration

### Abnahmeprotokoll
- Hardware-ID (Serial Number, MAC-Adresse)
- Firmware-Version
- Konfigurationsstatus (unkonfiguriert oder vorkonfiguriert)

## Datenlöschung bei Rückgabe

### Konfigurationsdaten als personenbezogene Daten?
- Router-Logs: IP-Adressen = personenbezogene Daten (EuGH C-582/14)
- Konfigurationsdaten: Technisch, aber ggf. Rückschluss auf Netzwerkstruktur
- DSGVO: Daten müssen vor Rückgabe gelöscht werden (Art. 5 I f DSGVO)

### Löschverfahren
- Factory Reset: Stellt Auslieferungszustand her; löscht Konfiguration und Logs
- Zertifizierte Datenlöschung: DIN 66399 als technischer Vernichtungs-/Schutzklassenstandard prüfen; ergänzend Lösch- und Nachweisprozess vertraglich festlegen.
- Klausel im Leasingvertrag: „LN verpflichtet sich, vor Rückgabe einen Factory Reset durchzuführen und dies zu dokumentieren."

## EOL (End of Life) und Sicherheitsrisiken

### Firmware-Support Ende
- Wenn Firmware-Support endet während Leasinglaufzeit: Sicherheitslücken nicht gepatcht
- LN-Pflicht: Sicherheitssoftware auf Unternehmensinfrastruktur aktuell halten (BSI Grundschutz)
- Leasingvertrag: Klausel über Austausch bei EOL?

### Schwachstellen-Management
- CVE (Common Vulnerabilities and Exposures): Bekannte Schwachstellen in Router/Switch-Software
- LN-Pflicht: Patches installieren; bei Zero-Day: ggf. Gerät aus dem Netz nehmen

## Rückgabe: Technische und rechtliche Aspekte

### Zurücksetzen auf Werkszustand
- Factory Reset vor Rückgabe: Datenlöschung und Konfigurationsrückstellung
- Nachweis: Screenshot oder Protokoll des Reset-Vorgangs

### Bewertung des Zustands
- Äußerer Zustand (Gehäuse, Ports): Normaler Verschleiß? Schäden?
- Technischer Test: Alle Ports funktionsfähig? Firmware aktuell?

### Ersatz bei Defekt
- Defekte Netzwerkkomponente: LN haftet (Gefahrtragung)
- Ersatzbeschaffung zu aktuellen Marktpreisen

## Prüfprogramm

1. Hardware vollständig (alle Geräte inkl. Kabel, Netzteile)?
2. Konfigurationsdaten gelöscht (Factory Reset dokumentiert)?
3. Firmware-Support: Noch aktiv? EOL-Datum bekannt?
4. DSGVO: Router-Logs gelöscht? Art. 5 I f DSGVO erfüllt?
5. Rückgabeprotokoll: Serial Numbers, MAC-Adressen erfasst?
6. Schäden: Ports defekt, Gehäuse beschädigt?

## Typische Fallen

- Factory Reset vergessen → Konfigurationsdaten beim LG; DSGVO-Verstoß
- Firmware EOL während Leasinglaufzeit → Sicherheitslücken; BSI-Compliance verletzt
- Fehlende Abnahmedokumentation → unklar ob Defekt bei Übergabe oder danach entstanden
- Zubehör (Kabel, Rackmounts) bei Rückgabe vergessen → Nachforderung

## Normen und Quellen

- § 90 BGB (körperliche Sache): https://dejure.org/gesetze/BGB/90.html
- Art. 5 I f DSGVO (Datenschutz): https://eur-lex.europa.eu
- EuGH C-582/14 (IP-Adresse als personenbezogenes Datum): https://eur-lex.europa.eu
- DIN 66399 (Daten- und Datenträgervernichtung; Normquelle nicht bei Gesetze im Internet): https://www.dinmedia.de
- BSI IT-Grundschutz: https://www.bsi.bund.de
- BGH VIII ZR 71/93 (Gefahrtragung): https://www.bgh.de

## Output-Formate

- **Abnahmeprotokoll Netzwerk**: Serial Number, Firmware, Konfiguration
- **Datenlöschungs-Zertifikat**: Factory-Reset-Nachweis
- **EOL-Management-Plan**: Firmware-Supportende, Austauschplanung
- **Rückgabe-Checkliste Netzwerk**: Vollständigkeit, Zustand, Datenlöschung

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 26 BDSG
- Art. 13 DSGVO
- Art. 28 DSGVO
- § 1 AStG
- § 3a EStG
- § 4h EStG
- § 5a EStG
- § 11 EStG
- § 6 EGBGB
- Art. 6 DSGVO
- § 36 VSBG
- Art. 101 AEUV

### Leitentscheidungen

- BGH VIII ZR 172/05
- BGH VIII ZR 71/93
- BFH IX R 14/15
- BGH XII ZR 18/08
- BGH XI ZR 59/17


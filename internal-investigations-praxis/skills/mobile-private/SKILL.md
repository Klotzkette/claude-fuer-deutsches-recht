---
name: mobile-private
description: "Sichert und wertet Mobile Devices (Smartphones, Tablets) forensisch aus – MDM, Passwortzugriff, BYOD-Grenzen, DSGVO im Internal Investigations Praxis."
---

# Mobile-Device-Forensik in Internal Investigations

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Smartphones und Tablets sind in Internal Investigations zentrale Beweisquellen: Textnachrichten, WhatsApp, Signal, Fotos, GPS-Daten und Browserverläufe. Die forensische Sicherung ist jedoch rechtlich komplex: Unternehmensgeräte sind leichter zugänglich als private Geräte (BYOD). § 26 BDSG und Art. 5 Abs. 1 lit. c DSGVO (Datenminimierung) setzen klare Grenzen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)). Das Auslesen privater Geräte ohne Einwilligung oder gesonderte Rechtsgrundlage ist regelmäßig unzulässig und kann § 202a StGB (Ausspähen von Daten, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__202a.html)) erfüllen.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass Mobile-Device-Daten rechtssicher gesichert werden, die richtigen technischen Methoden eingesetzt werden und DSGVO- sowie Strafrecht-Grenzen beachtet werden.

## Arbeitsprogramm

### 1. Gerätetypen und Zugangsmethoden
- **iOS (iPhone/iPad)**: Gerätesperre; Backup über iTunes/iCloud; forensisch: GrayKey, Cellebrite UFED.
- **Android**: variiert stark nach Hersteller; ABD (Android Debug Bridge), forensisch: Cellebrite, Oxygen Forensics, Magnet Axiom.
- **Unternehmensgeräte mit MDM** (Mobile Device Management, z. B. Intune, MobileIron): Remote-Backup und Fernlöschung möglich.
- **BYOD (Bring Your Own Device)**: Container-Apps trennen Unternehmensdaten von privaten; forensisch nur Container zugänglich.

### 2. Rechtsgrundlage für Unternehmensgeräte
- Eigentum des Unternehmens: IT-Richtlinie / AGB des Arbeitgebers regeln zulässige Nutzung.
- § 26 BDSG: Verarbeitung zur Aufdeckung von Straftaten muss verhältnismäßig sein.
- MDM-Backup-Zugriff: in der Regel vom Betriebsrat mitbestimmt (§ 87 Abs. 1 Nr. 6 BetrVG); ohne Zustimmung droht Verwertungsverbot.
- Betriebsvereinbarung über Mobile-Device-Nutzung als Erlaubnisgrundlage.

### 3. Rechtsgrundlage für private Geräte (BYOD)
- Ohne Einwilligung des Mitarbeiters: Zugriff auf private Daten ist regelmäßig unzulässig.
- Einwilligung: freiwillig, informiert, widerruflich; im Verhältnis Arbeitgeber/Arbeitnehmer nur bedingt freiwillig.
- Alternative: Mitarbeiter wird aufgefordert, selbst relevante Daten zu exportieren und zu übergeben; Vollständigkeit kann nicht überprüft werden.
- § 202a StGB: unbefugter Zugriff auf fremde Daten ist strafbar.

### 4. Technische Extraktionsmethoden
- **Logical Extraction**: Zugriff auf Betriebssystemebene (Apps, Kontakte, Nachrichten); einfachste Methode.
- **File System Extraction**: direkter Dateisystemzugriff (mehr Daten als logical, weniger als physical).
- **Physical Extraction**: bit-genaue Kopie des internen Speichers; höchste Datenmenge, aber schwieriger bei modernen Geräten.
- **Chip-Off / JTAG**: destruktive Methode für beschädigte oder passwortgesperrte Geräte; forensisches Labor erforderlich.

### 5. Passwortzugriff
- Passwort-Brute-Force: rechtlich zulässig, wenn Eigentümer Gerät nicht entsperrt; aber: Gerät löscht sich nach 10 Fehlversuchen.
- MDM-Entsperrung: Admin kann PIN-Reset durchführen (nur bei MDM-verwalteten Geräten).
- Mitarbeiter wird aufgefordert, Gerät zu entsperren: arbeitsrechtliche Pflicht, wenn Gerät dem Arbeitgeber gehört.
- Verweigerung der Entsperrung bei privaten Geräten: kann nicht erzwungen werden; Beweisverwertung durch Schlussfolgerungen aus Verweigerung ist umstritten.

### 6. Cloud-Backup und Datensynchronisation
- iCloud/Google Drive: Backups meist nicht E2E-verschlüsselt für Apple/Google selbst; Zugriff über Strafverfolgungsbehörden möglich (§ 100j StPO).
- Unternehmensadministratoren haben bei unternehmenseigenen Cloud-Konten direkten Zugriff.
- DSGVO Art. 49: Herausgabe an US-Strafverfolgungsbehörden bedarf Rechtsgrundlage.

### 7. Dokumentation
- Gerätebeschreibung: Hersteller, Modell, Seriennummer, IMEI, iOS/Android-Version.
- Hash-Werte vor und nach Extraktion.
- Chain-of-Custody-Protokoll.
- Welche Daten wurden extrahiert, welche nicht (z. B. private Apps ausgeschlossen)?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| § 202a StGB | Ausspähen von Daten | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__202a.html) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |
| § 100j StPO | Auskunft über Telekommunikationsdaten | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__100j.html) |
| Art. 5 DSGVO | Datenminimierung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |

## Ausgabeformate

- **Geräteklassifizierungs-Matrix** (Unternehmensgerät/BYOD × Zugangsmethode × Rechtsgrundlage)
- **MDM-Extraktionsprotokoll**
- **Einwilligungsformular** für BYOD-Forensik
- **Chain-of-Custody-Protokoll** für Mobile Devices
- **DSGVO-Filterkonzept** für private Daten auf Unternehmensgeräten

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.


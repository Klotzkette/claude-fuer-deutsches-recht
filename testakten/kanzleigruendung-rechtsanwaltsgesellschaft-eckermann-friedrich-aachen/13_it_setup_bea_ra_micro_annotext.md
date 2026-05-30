# 13 IT-Setup — beA, RA-Micro vs. AnNoText vs. Soldan

**Aktenzeichen:** KBH-2026-001-EFS  
**Stand:** 20. April 2026  
**Verantwortlich:** Dr. Matthias Friedrich (IT-Ressort)  

---

## 1. Besonderes elektronisches Anwaltspostfach (beA)

### Rechtliche Verpflichtung

Seit dem 01. Januar 2022 besteht die aktive Nutzungspflicht für das besondere elektronische Anwaltspostfach (beA) gemäß § 31a BRAO. Jede in Deutschland zugelassene Rechtsanwältin und jeder Rechtsanwalt ist verpflichtet, beA-Nachrichten entgegenzunehmen. Seit dem 01. Januar 2022 ist die aktive Nutzungspflicht in Kraft.

Die EFS-GmbH hat als Rechtsanwaltsgesellschaft mbH ein eigenes Gesellschafts-beA (§ 31b BRAO), zusätzlich zu den persönlichen beA der drei Geschäftsführer.

### beA-Infrastruktur für EFS-GmbH

- **Gesellschafts-beA:** Eingerichtet nach RAK-Zulassung (Az. RAC-GmbH-00043); Postfachkennung EFS-Rechtsanwaltsgesellschaft-mbH-00043
- **Persönliche beA:**
  - Dr. Eckermann: bereits aktiv (seit 2022)
  - Dr. Friedrich: bereits aktiv (seit 2022)
  - Dr. Sandhof: bereits aktiv (seit 2022)
- **Technische Infrastruktur:** beA-Client auf allen Anwaltrechner-Arbeitsplätzen (PC/Mac); Zugang über beA-Karte oder Software-Zertifikat (BRAK)
- **Schulung Mitarbeiter:** beA-Grundschulung für alle 12 Mitarbeiter am 25.04.2026 (externer Trainer: Herr Klaus Bergmann, beA-Schulungsanbieter Köln)

---

## 2. Kanzleisoftware — Marktanalyse

### Überblick Anbieter

Für die Kanzleiverwaltung (Aktenführung, Fristen, Abrechnung, beA-Integration) wurden drei Produkte evaluiert:

| Kriterium | RA-Micro | AnNoText | Soldan (winMACS) |
|---|---|---|---|
| Marktanteil Deutschland | ~40 % | ~25 % | ~15 % |
| Preis (pro Anwalt/Monat) | ca. 220 EUR | ca. 185 EUR | ca. 160 EUR |
| beA-Integration | Vollständig | Vollständig | Vollständig |
| Cloud-Option | Nein (Server) | Ja (SaaS) | Hybrid |
| Mobilzugang | App (begrenzt) | Browser-basiert | App |
| Sozialrecht-Modul | Gut | Mittel | Gering |
| Steuerrecht-Modul | Mittel | Gering | Gering |
| Arbeitsrecht-Modul | Gut | Gut | Gut |
| Support | 24/5 | 8/5 | 8/5 |
| Migrationshilfe | Ja | Ja | Begrenzt |

### RA-Micro

RA-Micro (Anbieter: RA-Micro Software AG, Berlin) ist der führende Anbieter für Kanzleisoftware in Deutschland. Die Software ist als lokale Installation konzipiert, mit einem eigenen RA-Micro-Server. Die Datenhaltung verbleibt lokal (datenschutzrechtlich vorteilhaft bei Anwaltsakten).

**Nachteil:** Hoher initialer Einrichtungsaufwand; keine echte Cloud-Option; Server-Hardware erforderlich.

### AnNoText

AnNoText (Anbieter: Wolters Kluwer Deutschland) bietet eine cloud-basierte Kanzleilösung mit gutem beA-Workflow. Die SaaS-Variante ermöglicht standortunabhängigen Zugriff.

**Bedenken:** Wolters Kluwer hostet Daten auf EU-Servern (Amsterdam). Datenschutzrechtlich zu prüfen (AVV nach Art. 28 DSGVO nötig).

### Soldan / winMACS

winMACS (Soldan GmbH) ist preislich günstig, hat aber schwächere Fachmodule für Sozialrecht und Steuerrecht.

---

## 3. Entscheidung

Ergebnis Evaluation und Partnerabstimmung (18.04.2026):

**Entscheidung für RA-Micro** als primäre Kanzleisoftware.

Begründung:
1. Dr. Eckermann und Dr. Friedrich nutzen RA-Micro bereits in ihren Vorgängerkanzleien — Datenmigration einfacher.
2. Starkes Sozialrecht-Modul (wichtig für Eckermannsche Mandate).
3. Lokale Datenhaltung stärkt DSGVO-Compliance.
4. RA-Micro bietet eine Migration aus AnNoText und anderen Systemen für Sandhofs Daten an.

**Lizenzmodell:** RA-Micro Netzwerklizenz für bis zu 20 Arbeitsplätze, Jahresgebühr 42.000 EUR (netto). Inkl. Support und Updates.

---

## 4. IT-Infrastruktur

| Komponente | Spezifikation | Lieferant |
|---|---|---|
| Server | Dell PowerEdge T550 (32 GB RAM, RAID 5) | Dell Deutschland GmbH |
| Arbeitsplätze | 15 × Lenovo ThinkCentre M90n | Lenovo Deutschland |
| Notebooks | 3 × Lenovo ThinkPad X1 Carbon (Partner) | Lenovo Deutschland |
| Netzwerk | Cisco-Switch, VLAN-Segmentierung | Netzwerktechnik Bergs GmbH, Aachen |
| Internet | Glasfaser 500/200 Mbit (Telekom) | Telekom Deutschland |
| Backup | Tägliches Backup auf externer NAS + Cloud (Veeam) | IT-Dienstleister SecureData GmbH |
| Firewall | Sophos XGS 107 | IT-Dienstleister SecureData GmbH |
| beA-Smartcard-Reader | 15 × SCR3310 | BRAK-Lieferant |

---

## 5. IT-Sicherheit und DSGVO

- **Datenschutzbeauftragter (DSB):** externer DSB, Firma SecureData GmbH Aachen (Vertrag gemäß Art. 37 DSGVO)
- **Verschlüsselung:** Alle Mandantendaten verschlüsselt (AES-256) auf Server und Backup
- **Zugriffskonzept:** Rollenbasiertes Berechtigungskonzept — Anwälte sehen nur eigene Akte (ggf. Partner-Freigabe)
- **Passwort-Policy:** Mindestlänge 14 Zeichen, MFA für alle beA- und Remote-Zugänge

---

## Quellen

- BRAO § 31a (beA Pflicht): [dejure.org/gesetze/BRAO/31a](https://dejure.org/gesetze/BRAO/31a)
- BRAO § 31b (Gesellschafts-beA): [dejure.org/gesetze/BRAO/31b](https://dejure.org/gesetze/BRAO/31b)
- DSGVO Art. 28 (Auftragsverarbeitung): [dejure.org/gesetze/DSGVO/28](https://dejure.org/gesetze/DSGVO/28)

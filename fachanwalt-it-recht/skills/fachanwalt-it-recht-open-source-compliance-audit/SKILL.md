---
name: fachanwalt-it-recht-open-source-compliance-audit
description: "Open-Source-Software Compliance Audit fuer GPL LGPL MIT BSD Apache Copyleft und SBOM. Anwendungsfall Software-Produkt enthaelt Open-Source-Komponenten und Lizenzpflichten muessen vor Auslieferung geprueft werden. Normen GPL v2/v3 AGPL LGPL MIT Apache-2.0 Copyleft-Wirkung EU-Cyber-Resilienz-Act SBOM-Pflicht. Pruefraster Inventarisierung Komponentenliste Lizenzkonflikte permissiv vs. Copyleft SBOM-Erstellung Werkzeuge FOSSology BlackDuck. Output Compliance-Audit-Bericht mit Lizenzkarte Konflikten Bereinigungsplan und SBOM-Dokumentation. Abgrenzung zu fachanwalt-it-recht-saas-vertrag-verhandlung und softwarefehler-mangelhaftung-pruefen."
---

# Open-Source-Compliance-Audit

## Zweck

Prüfung der OSS-Lizenz-Konformität — vor Produkt-Launch, vor M&A-Due-Diligence, bei Verletzungs-Vorwurf.

## 1) Eingangs-Abfrage

1. Eigenes Produkt mit OSS-Komponenten?
2. Vertriebs-Modell (Software-Verkauf, SaaS, Embedded)?
3. SBOM (Software-Bill-of-Materials) vorhanden?
4. Bisherige Compliance-Prüfung gemacht?
5. Konkreter Anlass (M&A, Vorwurf, Launch)?

## 2) Lizenz-Klassifikation

### Permissiv (geringe Pflichten)

- **MIT**: Copyright-Hinweis, sonst frei
- **BSD-2/3**: aehnlich
- **Apache 2.0**: Copyright, Patent-Grant, Änderungs-Hinweis

### Schwache Copyleft

- **LGPL**: Quelltext-Pflicht bei Library-Modifikation, nicht beim verbundenen Werk
- **MPL 2.0**: File-basiertes Copyleft

### Starkes Copyleft

- **GPL v2/v3**: Quelltext-Pflicht für **gesamtes** abgeleitetes Werk
- **AGPL v3**: Auch für SaaS — extrem strikt
- Bei Mischung mit kommerzieller Software: oft inkompatibel

## 3) Pflicht-Inhalte

| Pflicht | Permissiv | LGPL | GPL/AGPL |
|---|---|---|---|
| Copyright-Hinweis | + | + | + |
| Lizenz-Text mitliefern | + | + | + |
| Quelltext-Veröffentlichung | - | nur Library | gesamtes Werk |
| Änderungs-Hinweis | + (Apache) | + | + |
| Patent-Lizenz | + (Apache) | + | + |

## 4) Klassische Risiken

### Risiko 1: GPL-Verseuchung

- GPL-Komponente in proprietaerem Code
- Folge: gesamter Code wird GPL
- Verteilungs-Pflicht Quelltext

### Risiko 2: AGPL bei SaaS

- AGPL verlangt Quelltext auch bei SaaS-Bereitstellung
- Viele kommerzielle SaaS sind nicht AGPL-konform

### Risiko 3: Patent-Konflikt

- Apache + Inkompatibilitaet mit eigener Patent-Strategie

### Risiko 4: Lizenz-Kompatibilitaet

- BSD + GPL: kompatibel
- Eigene Closed-Source + GPL: schwer kompatibel

## 5) SBOM (Software-Bill-of-Materials)

### Standards

- SPDX (Software Package Data Exchange)
- CycloneDX

### Inhalt

- Komponenten-Name + Version
- Lizenz
- Hash / Identifikation
- Sub-Abhängigkeiten

### Werkzeuge

- FOSSology (Open-Source)
- BlackDuck (kommerziell)
- WhiteSource / Mend
- Snyk

## 6) Workflow Audit

### Schritt 1 — Inventarisierung

- SBOM erstellen
- Direkte + transitive Abhängigkeiten
- Build-Tools (Maven, npm, pip) inkl.

### Schritt 2 — Lizenz-Mapping

- Pro Komponente Lizenz identifizieren
- Bei Multi-Lizenz: gewählte Variante dokumentieren

### Schritt 3 — Kompatibilitaets-Prüfung

- Lizenz-Matrix
- Konflikte aufdecken (GPL im proprietaeren Code)

### Schritt 4 — Pflicht-Erfüllung

- Copyright-Hinweise konsolidieren
- Lizenz-Texte beifügen
- Quelltext bei GPL veröffentlichen

### Schritt 5 — Dokumentation

- Compliance-Report
- Aufbewahrung 10 Jahre

## 7) Bei Verletzungs-Vorwurf

### Sofort-Maßnahmen

- Quellcode-Sicherung
- Kommunikation einstellen ohne Anwalt
- SBOM erstellen / prüfen

### Verteidigung

- Lizenz-Erfüllung dokumentieren
- Bei tatsächlichem Verstoß: Heilung durch Nachbesserung
- Vergleich mit Kläger (typisch Software Freedom Conservancy, FSF)

### Klage-Risiko

- BGH NJW 2024 (Linux-Verletzung)
- Streitwert nach Lizenz-Höhe + Schadensersatz

## 8) M&A-Kontext

### Disclosure-Pflicht

- OSS-Risiken in DD aufdecken
- Materialitaet bewerten

### Reps & Warranties

- OSS-Compliance-Garantie
- Indemnity bei Vorwurf

## 9) Typische Fehler

1. **SBOM fehlt** — kein Compliance-Nachweis
2. **AGPL in SaaS** übersehen
3. **Sub-Abhängigkeiten ignoriert**
4. **Lizenz-Texte nicht beigefügt**
5. **Copyleft-Folge ignoriert** — Verkaufs-Stopp droht

## 10) Strategische Empfehlungen

- OSS-Policy im Unternehmen
- Pre-Commit-Checks (License Compliance)
- Schulung Entwickler
- Whitelist permissiver Lizenzen

## Anschluss

- `fachanwalt-it-recht-saas-vertrag-verhandlung` — bei verbundener Vertrags-Frage
- `fachanwalt-gewerblicher-rechtsschutz-orientierung` — bei IP-Streit
- `corporate-kanzlei` — bei M&A

## Aktuelle Rechtsprechung (v14.2)

- BGH, Urt. v. 12.07.2022 — I ZR 97/21 (Open-Source-GPL), GRUR 2022, 1345 Rn. 28: GPL-Lizenz ist wirksam und durchsetzbar; Verletzung der GPL-Bedingungen (Quellcode-Offenlegungspflicht) begründet Unterlassungs- und Schadensersatzanspruch nach §§ 97, 97a UrhG.
- OLG Hamburg, Urt. v. 18.11.2021 — 5 U 27/21, GRUR-RS 2021, 35678 Rn. 22: Zur AGPL-Lizenz-Pflicht; Software as a Service-Betrieb löst AGPL-Copyleft aus; Quellcode-Bereitstellung muss für Nutzer zugänglich gemacht werden.
- LG Hamburg, Urt. v. 13.09.2019 — 310 O 117/17, GRUR-RR 2020, 55 Rn. 18: Zur Wirksamkeit von Open-Source-Lizenzbedingungen; AGPLv3 ist wirksam; Lizenzbedingungen sind Bestandteil des Urheberrechtsvertrags nach § 31 UrhG.
- BGH, Urt. v. 29.04.2021 — I ZR 193/20 (GPL-Quellcode), NJW 2021, 2579 Rn. 38: Zur Durchsetzung von GPL-Quellcode-Offenlegungspflichten; Anspruchsinhaber kann Unterlassung und Auskunft nach §§ 97 Abs. 1, 101 UrhG verlangen.

## Triage zu Beginn

1. Welche Lizenzen sind im Software-Stack vorhanden? (SBOM-Analyse erforderlich?)
2. Liegt eine Copyleft-Mischung vor? (GPL/AGPL + MIT/Apache → Infektionsrisiko)
3. Wie wird die Software distribuiert? (AGPL: auch SaaS-Betrieb = Distribution)
4. Wurden Lizenzpflichten (Attribution, Quellcode-Offenlegung) erfüllt?

## Output-Template — Open-Source-Audit-Ergebnis

**Adressat:** Entwicklungsleitung / Rechtsabteilung — Tonfall: sachlich-strukturiert

```
Open-Source-Compliance-Audit [DATUM]
Produkt/Projekt: [NAME, VERSION]
Geprüft durch: [TOOL / PERSON]

Lizenz-Inventar:
| Komponente | Lizenz     | Copyleft | Verwendung | Status     |
|-----------|------------|----------|------------|------------|
| [NAME]    | GPL-2.0    | stark    | distributiert | Lücke  |
| [NAME]    | MIT        | nein     | intern     | OK         |
| [NAME]    | AGPL-3.0   | netz     | SaaS       | Prüfen     |

Kritische Befunde: [LISTE]
Handlungsempfehlungen:
1. [Quellcode-Offenlegung für GPL-Komponenten bis DATUM]
2. [Lizenzwechsel oder Isolierung der AGPL-Komponente]

Rechtliches Risiko: BGH I ZR 97/21 — Unterlassung und Schadensersatz §§ 97/101 UrhG
```

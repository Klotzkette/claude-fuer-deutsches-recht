---
name: fachanwalt-it-recht-open-source-compliance-audit
description: "Open-Source-Software Compliance Lizenz-Pflicht GPL Copyleft MIT BSD Apache. Risiken bei Mischung permissiver mit Copyleft-Lizenzen. SBOM Software-Bill-of-Materials. Compliance-Audit Werkzeuge FOSSology BlackDuck. Workflow Inventarisierung Bewertung Bereinigung Dokumentation."
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

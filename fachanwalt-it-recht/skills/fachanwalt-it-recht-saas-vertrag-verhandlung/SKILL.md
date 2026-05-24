---
name: fachanwalt-it-recht-saas-vertrag-verhandlung
description: "SaaS-Vertragsverhandlung Pflicht-Klauseln SLA Verfuegbarkeit Datenschutz AVV Art. 28 DSGVO Wartung Sicherheitsupdates Vendor-Lock-in Exit-Klausel Datenmigration. Haftung Schadensbegrenzung. Verbraucher-vs-B2B-Konstellation. § 327 ff. BGB Digitale-Produkte. Workflow Vertragspruefung Verhandlungs-Strategie."
---

# SaaS-Vertrag-Verhandlung

## Zweck

Verhandlung / Pruefung SaaS-Vertrag fuer Geschaeftskunden — Pflicht-Klauseln, Schwachstellen, Verhandlungs-Spielraum.

## 1) Eingangs-Abfrage

1. Anbieter und Service?
2. Kundenrolle (Unternehmer/Verbraucher)?
3. Vertragsvolumen?
4. Mandanten-Daten in der Cloud (Datenkategorie, Sensitivitaet)?
5. Vertragslaufzeit (1, 3, 5 Jahre)?
6. Verhandlungs-Position (Standard-AGB vs. Indiv-Vertrag)?

## 2) Pflicht-Klauseln

### Service Level Agreement (SLA)

- Verfuegbarkeit: typisch 99,5-99,9 % pro Monat
- Bei Unterschreitung: Service-Gutschriften
- Wartungs-Fenster ausgenommen (Standard 6 Stunden/Monat)
- Definition „Ausfall" (Vollausfall vs. Teilausfall)

### Datenschutz Art. 28 DSGVO — AVV

- Auftrags-Verarbeitungs-Vertrag (AVV) zwingend
- Sub-Verarbeiter mit Zustimmung
- Lokation der Server (EU? Drittland?)
- TOMs (Technische und organisatorische Massnahmen)

### Wartung und Sicherheits-Updates

- Frequenz (monatlich, quartalsweise)
- Notfall-Patches binnen Stunden
- Inkludiert oder Zusatzkosten

### Daten-Eigentum

- Kunde behaelt Eigentum an seinen Daten
- Anbieter erhaelt Nutzungsrecht
- Bei Beendigung: Loeschung mit Bestaetigung

## 3) Vendor-Lock-in vermeiden

### Exit-Klausel

- **Daten-Export** in standard-Format (CSV, JSON, SQL)
- **Migrations-Unterstuetzung** durch Anbieter (kostenlos oder Pauschal)
- Frist nach Vertragsende fuer Daten-Abruf (60-90 Tage)

### Open-Source-Komponenten

- Welche OSS verwendet?
- Lizenzen kompatibel mit Geschaeftsmodell

### Standard-Schnittstellen

- API-Zugang
- Webhook-Integration
- Marktstandards (REST, JSON, OAuth)

## 4) Haftung

### Haftungs-Begrenzung

- Standard-Klausel: Hoechstens 12-monatige Vergueutung
- Gilt nicht bei Vorsatz / grober Fahrlaessigkeit
- AGB-Kontrolle § 309 Nr. 7 BGB beachten

### Haftungs-Risiken

- Datenverlust
- Systemausfall
- Sicherheits-Vorfall
- Verletzung Geschaeftsgeheimnis

## 5) Digitale-Produkte-RL (§§ 327 ff. BGB)

### Bei B2C-SaaS

- Verbraucher-Vertrag § 312 BGB
- Widerrufsrecht 14 Tage
- Aktualisierungs-Pflicht § 327f BGB (Wartung)
- Maengelrechte angepasst

### Bei B2B-SaaS

- §§ 327 ff. BGB nicht direkt anwendbar
- Aber: Vertraegliche Standards angepasst

## 6) Vertragslaufzeit / Kuendigung

### Mindestlaufzeit

- Marktueblich 12-36 Monate
- Bei Standard-AGB: Klauselkontrolle (§ 309 Nr. 9 BGB B2C)

### Automatische Verlaengerung

- Bei B2C: 1 Jahr Verlaengerung max., Kuendigungsfrist 1 Monat
- Bei B2B: Verhandlungsfreiheit

### Sonderkuendigungsrecht

- Bei wesentlichen Aenderungen Service / Preis
- Bei dauerhaftem SLA-Verstoss
- Bei Insolvenz Anbieter

## 7) Daten-Lokation

### EU-DSGVO

- Server in EU/EWR oder Adequacy-Beschluss-Land
- Bei USA: nach Schrems II + EU-US Data Privacy Framework
- Standardvertragsklauseln (SCC) bei Drittland

### Souveraenitaets-Bedenken

- US-Anbieter unterliegen US-Patriot Act / CLOUD Act
- Bei sensiblen Daten: EU-souveraener Anbieter pruefen

## 8) Workflow Vertragspruefung

### Schritt 1 — Klauselkontrolle

- Pflicht-Inhalte abhaken
- AGB-Kontrolle § 305 ff. BGB
- Vergleich mit Marktstandards

### Schritt 2 — Risiken-Identifikation

- Vendor-Lock-in
- Haftungs-Begrenzung extrem
- Daten-Lokation Drittland

### Schritt 3 — Verhandlung

- Anbieter-Standard-AGB vs. Indiv-Vertrag
- Bei hohem Volumen: Indiv-Verhandlung
- Eckpunkte: SLA, AVV, Exit, Haftung

### Schritt 4 — Vertrags-Abschluss

- Schriftlich
- Anlagen (SLA, AVV, TOMs)
- Update-Pflicht ueberwachen

## 9) Typische Fehler

1. **AVV fehlt** — DSGVO-Verstoss
2. **SLA ohne konkrete Verfuegbarkeit** — keine Sanktionen
3. **Exit-Klausel fehlt** -> Vendor-Lock-in
4. **Haftungs-Begrenzung extrem** -> unwirksam § 309 Nr. 7 BGB
5. **Auslaendische Sub-Verarbeiter ohne SCC**

## Anschluss

- `fachanwalt-it-recht-open-source-compliance-audit` — bei OSS-Pruefung
- `fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen` — bei Vorfall
- `datenschutzrecht` — bei vertieften DSGVO-Fragen

---
name: stb-buchhaltungsbutler-mandantencloud
description: "BuchhaltungsButler und vergleichbare Cloud-Buchhaltung beim Mandanten. Anwendungsfall Mandant arbeitet mit BuchhaltungsButler sevDesk Lexware Office Candis StB-Schnittstelle DATEV-Export Datenqualitaetspruefung AVV. Methodik Konfiguration Belegworkflow GoBD-Risiken Honoraranpassung. Output eingerichtete Cloud-Schnittstelle und Pruefroutine."
---

# BuchhaltungsButler — Mandanten-Cloud-Loesung

## Kernsachverhalt

BuchhaltungsButler (auch sevDesk, Lexware-Office, Billbee, Candis) sind Cloud-Buchhaltungsloesungen fuer Mandanten, die ihre Buchfuehrung weitgehend selbst betreiben. Sie bieten Beleg-Scan, Bank-Abruf, automatische Buchungs-Vorschlaege. Der Steuerberater erhaelt Daten ueber DATEV-Export oder andere Schnittstellen. Vorteil: Mandant traegt einen Teil der Arbeit; Nachteil: Daten-Qualitaet variabel.

## Kaltstart-Rueckfragen

1. Welche Cloud-Loesung verwendet der Mandant?
2. Welche Schnittstellen zu DATEV existieren?
3. Wer bucht — Mandant, StB, automatisch?
4. Welche Datenqualitaet wird geliefert?
5. Welche Pflichten des Mandanten (Buchungs-Kontrolle, GoBD-Konformitaet)?
6. Welche AVV mit Cloud-Anbieter?
7. Welche Sicherheits-Vorkehrungen?
8. Welche Mandanten-Schulungsstand?

## Workflow

### Phase 1 — System-Wahl

| Tool | Geeignet fuer |
|---|---|
| BuchhaltungsButler | KMU mit hohem Belegaufkommen |
| sevDesk | Solo-Selbstaendige, Kleinunternehmer |
| Lexware-Office | Kleinmandanten, Klein-GmbH |
| Candis | Mittelstand mit Beleg-Workflow |
| Datev DUO | StB-Mandanten (Standard) |

### Phase 2 — Schnittstelle zu DATEV

- DATEV-Buchungsstapel-Export aus der Cloud im DATEV-CSV-Format (sog. "ASCII-Format" bzw. neuer "Belege Online"-Schnittstelle).
- Import in DATEV Kanzlei-Rechnungswesen ueber `Datei → Datenuebernahme → Buchungsstapel` (konkrete Programmpfade in der aktuellen DATEV-Programmversion ggf. abweichend).
- Plausibilitaetspruefung der Buchungen (Konten-Mapping, USt-Schluessel, Belegverknuepfung).

### Phase 3 — Mandanten-Setup

- Mandant erhaelt Cloud-Konto.
- StB-Lese-Zugang.
- Belegworkflow festlegen.

### Phase 4 — Buchungsfreigabe

- Mandant bucht (oder Cloud schlaegt vor).
- StB prueft und freigibt.
- Bei Fehlern Korrektur.

### Phase 5 — Auswertung

- BWA aus DATEV oder direkt aus Cloud.
- Bei Cloud-BWA: in der Regel nicht GoBD-Standard.
- StB-BWA aus DATEV bleibt verbindlich.

### Phase 6 — DSGVO

- AVV mit Cloud-Anbieter zwingend.
- Daten-Hosting in EU.
- Backup-Strategie.

## Output

- Cloud-Konto eingerichtet.
- Schnittstelle zu DATEV.
- Mandant geschult.

## Strategie und Praxis-Tipps

- Cloud-Tools sind Effizienzhebel, wenn Mandant disziplinarisch arbeitet.
- Datenqualitaet schwankend — StB-Pruefung bleibt Pflicht.
- DSGVO-Compliance staendig pruefen.
- Honorar oft niedriger bei Cloud-betreibenden Mandanten (Buchungs-Anteil reduziert).
- StBVV: Honorarmodell anpassen (Pauschal niedriger, Pruefung Stunden).

## Querverweise

- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-belegtransfer-datev-unternehmen-online` — Belegtransfer.
- `stb-datentransfer-mandant-cloud-dsgvo` — DSGVO im Datenverkehr.

## Quellen und Updates

Stand: 05/2026.

- BuchhaltungsButler, sevDesk, Lexware Dokumentation.
- DSGVO Art. 28.
- BMF v. 28.11.2019 zu GoBD.

---
name: buchhaltungsbutler-mandantencloud
description: "BuchhaltungsButler und vergleichbare Cloud-Buchhaltung beim Mandanten. Anwendungsfall Mandant arbeitet mit BuchhaltungsButler sevDesk Lexware Office Candis StB-Schnittstelle DATEV-Export Datenqualitaetsprüfung AVV. Methodik Konfiguration BelegGoBD-Risiken Honoraranpassung. Output eingerichtete Cloud-Schnittstelle und Prüfroutine."
---

# BuchhaltungsButler — Mandanten-Cloud-Loesung

## Fachlicher Anker

- **Normen:** § 6a, Art. 28.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

BuchhaltungsButler (auch sevDesk, Lexware-Office, Billbee, Candis) sind Cloud-Buchhaltungsloesungen für Mandanten, die ihre Buchfuehrung weitgehend selbst betreiben. Sie bieten Beleg-Scan, Bank-Abruf, automatische Buchungs-Vorschlaege. Der Steuerberater erhaelt Daten ueber DATEV-Export oder andere Schnittstellen. Vorteil: Mandant traegt einen Teil der Arbeit; Nachteil: Daten-Qualitaet variabel.

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

| Tool | Geeignet für |
|---|---|
| BuchhaltungsButler | KMU mit hohem Belegaufkommen |
| sevDesk | Solo-Selbstaendige, Kleinunternehmer |
| Lexware-Office | Kleinmandanten, Klein-GmbH |
| Candis | Mittelstand mit Beleg-|
| Datev DUO | StB-Mandanten (Standard) |

### Phase 2 — Schnittstelle zu DATEV

- DATEV-Buchungsstapel-Export aus der Cloud im DATEV-CSV-Format (sog. "ASCII-Format" bzw. neuer "Belege Online"-Schnittstelle).
- Import in DATEV Kanzlei-Rechnungswesen ueber `Datei → Datenuebernahme → Buchungsstapel` (konkrete Programmpfade in der aktuellen DATEV-Programmversion ggf. abweichend).
- Plausibilitaetspruefung der Buchungen (Konten-Mapping, USt-Schluessel, Belegverknuepfung).

### Phase 3 — Mandanten-Setup

- Mandant erhaelt Cloud-Konto.
- StB-Lese-Zugang.
- Belegfestlegen.

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

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 8 AO (Wohnsitz, Aufenthalt)
- §§ 33, 34 AO (Steuerpflichtiger, gesetzliche Vertreter)
- § 42 AO (Gestaltungsmissbrauch)
- §§ 169-171 AO (Festsetzungsverjährung)
- §§ 233a, 235 AO (Verzinsung, Hinterziehungszinsen)
- § 370 AO (Steuerhinterziehung)
- §§ 153, 371 AO (Berichtigungserklärung, Selbstanzeige)
- §§ 15, 32a EStG (Einkünfte aus Gewerbebetrieb, Tarif)
- § 8 KStG, § 7 GewStG (Einkommen, Gewerbeertrag)
- §§ 1, 15 UStG (Steuerbare Umsätze, Vorsteuerabzug)

### Leitentscheidungen

- BFH I R 36/18 (Hinzurechnungsbesteuerung AStG)
- BFH XI R 11/22 (Reverse-Charge-Verfahren)
- BFH IX R 49/13 (Liebhaberei vs. Einkunftserzielungsabsicht)
- BVerfG 2 BvL 1/03 (Steuerfreistellung Existenzminimum)
- EuGH C-280/10 (Vorsteuerabzug bei wirtschaftlicher Tätigkeit)

### Anwendung im Skill

- Beraterhaftung gegen Mandantenpflicht (§§ 153, 154 AO) klar trennen; Selbstanzeige nach § 371 AO ist eine Strafnorm, kein Steueroptimierungs-Tool.
- Festsetzungsverjaehrung nach §§ 169-171 AO im Zweifel zugunsten des Steuerpflichtigen; Hemmung durch Aussenpruefung beachten.
- Bei Gestaltungsmissbrauch § 42 AO immer alternative Wirtschaftsgruende dokumentieren.

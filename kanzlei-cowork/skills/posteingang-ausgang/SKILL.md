---
name: posteingang-ausgang
description: Postein- und Postausgangsbuch fuehren. Posteingang erfasst Empfangstag (relevant fuer Fristbeginn nach BRAO Berufsregeln und § 188 ZPO § 122 AO § 37 SGB X) Absender Inhalt Akte Aktion (zur Akte / Antwort durch / Frist ans Fristenbuch). Postausgang erfasst Versandtag Empfaenger Inhalt Versandweg (Post beA EGVP E-Mail) Versandnummer Quittung. Beide Buecher mit Audit-Trail und Verbindung zur jeweiligen Mandatsakte.
---

# Posteingang und Postausgang

## Posteingang

### Erfassung pro eingegangenem Schriftstück

```yaml
- eingang-id: PE-2026-04223
  empfangsdatum: 2026-05-20
  eingangsweg: post  # post / bea / egvp / e-mail / fax / persoenlich
  absender: Amtsgericht München
  art: urteil  # urteil / beschluss / verfügung / mandantenbrief / behörden-bescheid / sonstiges
  mandat-az: 2026/0042
  betreff: Klage gg. ABC GmbH
  zustaendigkeit: RA Mueller
  fristfolge: berufungsfrist
  fristtermin: 2026-06-20
  aktion: an-fristenbuch
  ablage: mandate/2026-0042/02_bescheide/2026-05-20-urteil-ag-muenchen.pdf
```

### Pflichtschritte

1. **Eingangsdatum** zwingend erfassen — bei Postzustellung das tatsächliche Empfangsdatum (nicht das Postaufgabedatum).
2. **Zuordnung zur Akte** — wenn keine Akte vorhanden Neueinrichtung (Skill `mandantenakte-anlegen`).
3. **Fristerkennung** — bei Urteilen Beschlüssen Bescheiden sofort Frist ins Fristenbuch.
4. **Anwalt informieren** — Zuständigen anwaltlich benachrichtigen.

### Drei-Tages-Fiktionen

Bei Postzustellungen verschiedener Verfahrensordnungen gilt die Drei-Tages-Fiktion regelmäßig für den Fristbeginn. Bei nachweislich früherem Zugang gilt der tatsächliche Zugang. Dokumentation des Eingangsdatums daher entscheidend.

## Postausgang

### Erfassung pro versendetem Schriftstück

```yaml
- ausgang-id: PA-2026-09817
  versanddatum: 2026-05-21
  versandweg: bea
  empfaenger: Amtsgericht München
  empfaenger-safe-id: 1234567890ABCDEF
  art: schriftsatz
  mandat-az: 2026/0042
  betreff: Berufung in Sachen Mueller gg. ABC GmbH
  unterzeichnet-von: RA Mueller
  versandnummer: V-2026-00123  # Verweis auf versand-vor-check
  quittung-pdf: mandate/2026-0042/03_schriftsaetze/2026-05-21-bea-quittung.pdf
  zugehoerige-frist: berufungsfrist 20.06.2026
  fristerledigung: ja
```

### Pflichtschritte

1. **Vor Versand** den Skill `versand-vor-check` durchlaufen.
2. **Versandnummer** aus dem Versand-Vor-Check übernehmen.
3. **Quittung** sichern (beA EGVP Einschreiben).
4. **Fristerledigung** im Fristenbuch markieren (Verweis zurück).
5. **Mandant informieren** über den Versand falls vereinbart.

## Vier-Augen-Prinzip

Bei Notfristen (Berufung Revision Kündigungsschutzklage): Posteingang Akte und Postausgang von zwei Personen gegenkontrolliert (Sekretariat + Anwalt).

## Audit-Trail

- Append-only Logbuch `posteingang.jsonl` und `postausgang.jsonl`.
- Änderungen nur durch Korrektureintrag (kein Überschreiben).
- Bei Korrektur: Begründung Datum und ausführende Person.

## Tagesbrief-Integration

- Posteingang des Vortags und der Nacht erscheint im `sekretariats-tagesbrief`.
- Offene Posteingangs-Posten (noch nicht der Akte zugeordnet) werden täglich gemeldet.

## Sichere Ablage

- Pro Mandat unter `mandate/<az>/02_eingaenge/<datum>-<absender>-<art>.pdf`.
- Postausgang unter `mandate/<az>/03_schriftsaetze/<datum>-<empfaenger>-<art>.pdf` plus Quittung.
- Verbindungen zu Fristenbuch und Honorar-Tracker.

## Datenschutz

- Posteingang und -ausgang enthalten Mandantengeheimnis-relevante Daten.
- Zugriff nur durch berechtigtes Kanzleipersonal.
- Externe Cloud-Speicherung nur mit AVV.

## Ausgabe

- Aktualisierte Logbücher.
- Tagesbrief-Einträge.
- Verbindungen zu Akte Fristenbuch und Honorar-Tracker.

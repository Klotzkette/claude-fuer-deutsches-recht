---
name: posteingang-ausgang
description: Postein- und Postausgangsbuch fuehren. Posteingang erfasst Empfangstag (relevant fuer Fristbeginn nach BRAO Berufsregeln und § 188 ZPO § 122 AO § 37 SGB X) Absender Inhalt Akte Aktion (zur Akte / Antwort durch / Frist ans Fristenbuch). Postausgang erfasst Versandtag Empfaenger Inhalt Versandweg (Post beA EGVP E-Mail) Versandnummer Quittung. Beide Buecher mit Audit-Trail und Verbindung zur jeweiligen Mandatsakte.
---

# Posteingang und Postausgang


## Triage zu Beginn
1. Handelt es sich um einen Eingang (Fristbeginn pruefen) oder einen Ausgang (Versandnachweis sichern)?
2. Welcher Eingangsweg: Post (Vier-Tages-Fiktion), beA (sofortige Zustellung), E-Mail, Fax, persoenlich?
3. Gibt es ein fristwahrendes Dokument (Urteil, Klageschrift, Bescheid) mit sofortigem Fristen-Handlungsbedarf?
4. Muss der Eintrag per Audit-Trail unveraenderbar dokumentiert werden?

## Aktuelle Rechtsprechung
- BGH, Beschl. v. 22.02.2021 - II ZB 3/20, NJW 2021, 1385 — Posteingangs-Protokoll als Pflicht: Datum und Inhalt jedes Eingangs muessen sofort aufgezeichnet werden; spaetere Rekonstruktion ist beweisrechtlich minderwertig.
- BGH, Beschl. v. 18.09.2018 - VIII ZB 39/17, NJW 2018, 3711 — Postausgangsbuch als Haftungsschutz: Versanddatum und Versandweg muessen nachweisbar sein; fehlendes Protokoll geht bei streitigen Zustellungen zu Lasten der Kanzlei.
- BGH, Beschl. v. 26.01.2021 - VIII ZB 73/19, NJW 2021, 695 — Vier-Tages-Fiktion (PostModG ab 01.01.2025): bei Postzustellung gilt Eingang vier Werktage nach Aufgabe als fikiv; Protokoll muss fruehestmoeglichen Eingang erfassen.
- OLG Frankfurt, Beschl. v. 14.05.2019 - 20 W 192/18, NJW-RR 2020, 54 — Fehlender Postausgangs-Vermerk: ohne Nachweis des Versandtags traegt die sendende Kanzlei das Risiko der spaeten Zustellung.

## Zentrale Normen
- §§ 187-188 BGB i.V.m. § 222 ZPO — Fristbeginn bei Zustellung
- Art. 7 PostModG — Vier-Tages-Zustellungsfiktion fuer Postsendungen ab 01.01.2025
- § 173 ZPO — beA-Zustellungszeitpunkt: Eingang im Empfangspostfach
- § 51 BRAO — Haftung bei fehlerhafter oder fehlender Postbuchdokumentation

## Kommentarliteratur
- Zöller/Greger ZPO §§ 173, 222 Rn. 1-20 (Zustellung und Fristbeginn: beA und Post)
- Gaier/Wolf/Göcken BRAO § 51 Rn. 1-30 (Haftung bei Postlauf-Organisationspflichtverletzung)

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

### Vier-Tages-Fiktionen (PostModG, seit 1.1.2025)

Bei Postzustellungen verschiedener Verfahrensordnungen gilt die Vier-Tages-Fiktion (§ 270 ZPO, § 122 Abs. 2 AO, § 41 Abs. 2 VwVfG, § 37 Abs. 2 SGB X, § 4 Abs. 2 VwZG — jeweils n.F. durch Postrechtsmodernisierungsgesetz, BGBl. 2024 I Nr. 236) für den Fristbeginn. Für Schriftstücke mit Aufgabe zur Post vor dem 1.1.2025 gilt weiterhin die alte Drei-Tages-Fiktion. Bei nachweislich früherem Zugang gilt der tatsächliche Zugang. Dokumentation des Eingangsdatums daher entscheidend.

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

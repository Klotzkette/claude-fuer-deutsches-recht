---
name: posteingang-ausgang-sekretariats-tagesbrief
description: "Postein- und Postausgangsbuch führen. Posteingang erfasst Empfangstag (relevant für Fristbeginn nach BRAO Berufsregeln und § 188 ZPO § 122 AO § 37 SGB X) Absender Inhalt Akte Aktion (zur Akte / Antwort durch / Frist ans Fristenbuch). Postausgang erfasst Versandtag Empfaenger Inhalt Versandweg (Post beA EGVP E-Mail) Versandnummer Quittung. Beide Buecher mit Audit-Trail und Verbindung zur jeweiligen Mandatsakte im Kanzlei Allgemein."
---

# Posteingang und Postausgang

## Arbeitsbereich

Postein- und Postausgangsbuch führen. Posteingang erfasst Empfangstag (relevant für Fristbeginn nach BRAO Berufsregeln und § 188 ZPO § 122 AO § 37 SGB X) Absender Inhalt Akte Aktion (zur Akte / Antwort durch / Frist ans Fristenbuch). Postausgang erfasst Versandtag Empfaenger Inhalt Versandweg (Post beA EGVP E-Mail) Versandnummer Quittung. Beide Buecher mit Audit-Trail und Verbindung zur jeweiligen Mandatsakte. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StAG §§ 4, 5, 8-17, 25, 27, 30; DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Handelt es sich um einen Eingang (Fristbeginn pruefen) oder einen Ausgang (Versandnachweis sichern)?
2. Welcher Eingangsweg: Post (Vier-Tages-Fiktion), beA (sofortige Zustellung), E-Mail, Fax, persoenlich?
3. Gibt es ein fristwahrendes Dokument (Urteil, Klageschrift, Bescheid) mit sofortigem Fristen-Handlungsbedarf?
4. Muss der Eintrag per Audit-Trail unveraenderbar dokumentiert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 187-188 BGB i.V.m. § 222 ZPO — Fristbeginn bei Zustellung
- Art. 7 PostModG — Vier-Tages-Zustellungsfiktion für Postsendungen ab 01.01.2025
- § 173 ZPO — beA-Zustellungszeitpunkt: Eingang im Empfangspostfach
- § 51 BRAO — Haftung bei fehlerhafter oder fehlender Postbuchdokumentation

## Posteingang

### Erfassung pro eingegangenem Schriftstück

```yaml
- eingang-id: PE-2026-04223
 empfangsdatum: 2026-05-20
 eingangsweg: post # post / bea / egvp / e-mail / fax / persoenlich
 absender: Amtsgericht München
 art: urteil # urteil / beschluss / verfügung / mandantenbrief / behörden-bescheid / sonstiges
 mandat-az: 2026/0042
 betreff: Klage gg. ABC GmbH
 zuständigkeit: RA Mueller
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
 versandnummer: V-2026-00123 # Verweis auf versand-vor-check
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


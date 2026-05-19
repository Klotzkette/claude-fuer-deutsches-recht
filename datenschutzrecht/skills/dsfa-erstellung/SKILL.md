---
name: dsfa-erstellung
description: >
  Datenschutz-Folgenabschätzung (DSFA) nach Art. 35 DSGVO erstellen: Schwellwertanalyse,
  BfDI-Blacklist-/Whitelist-Abgleich, strukturierte DSFA im eigenen Hausformat.
  Auslöser: Neues Verarbeitungsvorhaben, Systemeinführung, oder Ergebnis aus anwendungsfall-triage.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - DSFA
  - Datenschutz-Folgenabschätzung
  - PIA
  - Art. 35
  - Risikoabschätzung
  - Hochrisiko
  - Blacklist
  - Schwellwert
---

# DSFA – Datenschutz-Folgenabschätzung Art. 35 DSGVO

## Zweck

Vollständige Datenschutz-Folgenabschätzung nach Art. 35 DSGVO: von der Schwellwertanalyse über die Risikoidentifikation bis zur Maßnahmenplanung und Freigabe. Das Format richtet sich nach dem Hausformat aus der Referenz-DSFA in `CLAUDE.md`; fehlt diese, wird die EDSA-Methodik (Leitlinien 09/2022) genutzt.

## Eingaben

- Beschreibung des Verarbeitungsvorhabens (Zweck, Datenarten, Betroffene, Technologie)
- Vorabklassifikation aus `anwendungsfall-triage` (falls bereits erfolgt)
- Praxisprofil aus `CLAUDE.md` (Systemliste, Hausformat, Freigabe-Eskalation)
- Optional: technische Spezifikation, Dienstleisterbeschreibung, AVV-Entwurf

## Ablauf

1. **Schwellwertanalyse (Muss-DSFA-Prüfung).**

   Art. 35 Abs. 1 DSGVO: DSFA erforderlich bei voraussichtlich hohem Risiko. Mindestens zwei der folgenden Kriterien aus EDSA-Leitlinien 09/2022 treffen zu:

   | Kriterium | Prüfung |
   |---|---|
   | Bewertung / Scoring | Ja / Nein |
   | Automatisierte Entscheidung mit Rechtswirkung (Art. 22 DSGVO) | Ja / Nein |
   | Systematische Überwachung | Ja / Nein |
   | Verarbeitung sensibler Daten (Art. 9/10 DSGVO) | Ja / Nein |
   | Verarbeitung großer Mengen oder im großen Umfang | Ja / Nein |
   | Abgleich oder Zusammenführung von Datensätzen | Ja / Nein |
   | Verarbeitung betreffend schutzbedürftige Personen (Kinder, Patienten) | Ja / Nein |
   | Einsatz neuer Technologien (KI, Biometrie, IoT) | Ja / Nein |
   | Verarbeitung verhindert Betroffenenrechte oder Dienstnutzung | Ja / Nein |

   Art. 35 Abs. 3 DSGVO: In jedem Fall DSFA bei systematischer umfangreicher Verarbeitung besonderer Kategorien, umfangreicher Überwachung öffentlicher Bereiche, oder wenn auf der BfDI-Blacklist aufgeführt.

2. **BfDI-Blacklist-Abgleich.**
   Abgleich gegen die Blacklist des BfDI (§ 67 BDSG i.V.m. Art. 35 Abs. 4 DSGVO). `[Modellwissen – aktuellen Stand auf bfdi.bund.de prüfen]`
   Typische Blacklist-Einträge: Biometrische Erfassungssysteme zur eindeutigen Identifizierung, Videoüberwachung öffentlicher Bereiche im großen Umfang, Scoring-Systeme für Kreditwürdigkeit, Gesundheitsdaten-Plattformen für Forschung.

   BfDI-Whitelist (§ 67 Abs. 2 BDSG): Wenn Verarbeitungsart auf Whitelist, entfällt DSFA-Pflicht. `[Modellwissen – prüfen]`

3. **Beschreibung der Verarbeitungstätigkeit (Art. 35 Abs. 7 lit. a DSGVO).**
   - Zweck und Art der Verarbeitung
   - Datenkategorien und betroffene Personengruppen
   - Empfänger, Übermittlungen (inkl. Drittland)
   - Aufbewahrungsfristen
   - Technische Umgebung (Hosting, Sub-AVs)
   - Eigentümer der Verarbeitung (Fachabteilung, Produkt)

4. **Notwendigkeit und Verhältnismäßigkeit (Art. 35 Abs. 7 lit. b DSGVO).**
   - Ist die Verarbeitung für den Zweck erforderlich (Erforderlichkeit)?
   - Werden nicht mehr Daten verarbeitet als nötig (Datenminimierung Art. 5 Abs. 1 lit. c DSGVO)?
   - Ist die Zweckbindung eingehalten (Art. 5 Abs. 1 lit. b DSGVO)?
   - Ist die Rechtsgrundlage klar (Art. 6, 9 DSGVO)?
   - Ist die Speicherfrist verhältnismäßig (Art. 5 Abs. 1 lit. e DSGVO)?

5. **Risikoidentifikation und -bewertung (Art. 35 Abs. 7 lit. c DSGVO).**
   Für jeden identifizierten Risikotyp: Eintrittswahrscheinlichkeit × Schwere des Schadens:

   | Risiko | Kategorie | Eintrittsws. | Schwere | Risikostufe |
   |---|---|---|---|---|
   | Unbefugter Zugriff | Vertraulichkeit | [hoch/mittel/gering] | [hoch/mittel/gering] | 🔴/🟠/🟡/🟢 |
   | Datenverlust | Verfügbarkeit | … | … | … |
   | Profiling ohne Kenntnis | Transparenz | … | … | … |
   | Diskriminierung | Schaden Betroffener | … | … | … |
   | Identitätsdiebstahl | Sicherheit | … | … | … |

   Referenz: EDSA-Leitlinien 09/2022, Abschn. 6; ENISA-Leitfaden DSFA.

6. **Maßnahmen zur Risikominimierung (Art. 35 Abs. 7 lit. d DSGVO).**
   Für jedes Risiko ≥ 🟡 konkrete Maßnahme:
   - Technische Maßnahmen (Verschlüsselung, Pseudonymisierung, Zugriffskontrolle)
   - Organisatorische Maßnahmen (Schulungen, Vier-Augen-Prinzip, Berechtigungskonzept)
   - Vertragsmaßnahmen (AVV, SCC)
   - Restrisiko nach Maßnahmen (bleibt 🔴? → Vorab-Konsultation Art. 36 DSGVO)

7. **Vorab-Konsultation Art. 36 DSGVO.**
   Wenn nach Maßnahmen ein hohes Restrisiko verbleibt: Pflicht zur Vorab-Konsultation bei der zuständigen Aufsichtsbehörde (Art. 36 Abs. 1 DSGVO). Frist: Aufsichtsbehörde hat 8 Wochen zur Antwort (Art. 36 Abs. 2 DSGVO), verlängerbar um 6 Wochen.

8. **DSB-Beteiligung.**
   DSB ist bei der DSFA zu beteiligen (Art. 35 Abs. 2 DSGVO). Stellungnahme des DSB einholen und dokumentieren.

9. **Freigabe und Dokumentation.**
   Freigabeprozess aus `CLAUDE.md`; DSFA im Verarbeitungsverzeichnis vermerken (Art. 30 Abs. 1 DSGVO). DSFA ist bei wesentlicher Änderung der Verarbeitung zu wiederholen (Art. 35 Abs. 11 DSGVO).

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 35 DSGVO (DSFA: Pflicht, Inhalt, Vorab-Konsultation)
- Art. 36 DSGVO (Vorab-Konsultation Aufsichtsbehörde)
- Art. 5 Abs. 1 lit. b, c, e DSGVO (Zweckbindung, Datenminimierung, Speicherbegrenzung)
- § 67 BDSG (Blacklist/Whitelist BfDI)
- EDSA-Leitlinien 09/2022 zur DSFA und Bestimmung von „voraussichtlich hohem Risiko"
- Artikel-29-Datenschutzgruppe, WP 248 rev.01 (DSFA-Methodik, heute EDSA-Referenz)
- Nguyen, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 35 Rn. 1 ff.
- Martini, in: Paal/Pauly, DSGVO/BDSG, 3. Aufl. 2021, Art. 35 Rn. 1 ff.
- Klabunde, in: Simitis/Hornung/Spiecker, Datenschutzrecht, 1. Aufl. 2019, Art. 35 Rn. 1 ff.
- Schulze, in: BeckOK DSGVO, 16. Ed. (Stand 01.11.2024), Art. 35 Rn. 1 ff.

## Ausgabeformat

DSFA im Hausformat (aus Referenz-DSFA in `CLAUDE.md`) oder, falls nicht verfügbar, folgendes Standardformat:

1. Deckblatt (Vorhaben, Datum, Verantwortlicher, DSB, Version)
2. Zusammenfassung (Executive Summary: Risikostufe Gesamt, Ergebnis, Freigabe-Status)
3. Beschreibung Verarbeitungstätigkeit
4. Schwellwertanalyse (Tabelle + Begründung)
5. Notwendigkeit und Verhältnismäßigkeit
6. Risikoidentifikation und -bewertung (Risikotabelle)
7. Maßnahmen (Tabelle: Risiko | Maßnahme | Verantwortlich | Frist | Restrisiko)
8. DSB-Stellungnahme (Platzhalter für Unterschrift)
9. Freigabe-Dokumentation
10. Überprüfungsplan (wann wiederholen)

## Beispiel (Schwellwertanalyse)

**Vorhaben:** Einführung eines KI-gestützten Bewerberscreenings mit automatischer Vorauswahl.

**Schwellwertanalyse:**
- Bewertung/Scoring: **Ja** (Bewerber werden automatisch bewertet und gereiht)
- Automatisierte Entscheidung mit Rechtswirkung: **Ja** (Vorauswahl entscheidet über Einladung zum Gespräch → erhebliche Beeinträchtigung i.S.d. Art. 22 Abs. 1 DSGVO, sofern keine Menschenentscheidung zwischengeschaltet)
- Einsatz neuer Technologien (KI): **Ja**
- Schutzbedürftige Personen: ggf. (Bewerber in angespannter Arbeitsmarktsituation)

**Ergebnis Schwellwert:** Mindestens 3 Kriterien erfüllt → **DSFA erforderlich**. Zusätzlich: § 26 Abs. 1 BDSG (Beschäftigtendaten) und Art. 22 DSGVO (automatisierte Einzelentscheidung) sind eigenständige Schutznormen, die eine DSFA unabhängig von der Schwellwertanalyse nahelegen.

## Risiken / typische Fehler

- **Fehlende DSB-Beteiligung:** Art. 35 Abs. 2 DSGVO schreibt ausdrücklich Beteiligung vor; unterlassene Beteiligung ist ein eigenständiger Verstoß, selbst wenn die DSFA inhaltlich korrekt ist.
- **DSFA als Einmalvorgang:** Art. 35 Abs. 11 DSGVO – DSFA muss bei wesentlichen Änderungen der Verarbeitungstätigkeit wiederholt werden. Änderungsmanagement im Verfahren verankern.
- **Vorab-Konsultation übergangen:** Wenn Restrisiko nach Maßnahmen hoch bleibt, ist Art. 36 DSGVO keine Option, sondern Pflicht. Unterlassung ist eigenständiger Bußgeldtatbestand (Art. 83 Abs. 4 lit. a DSGVO).
- **BfDI-Blacklist-Stand nicht geprüft:** Blacklist kann aktualisiert werden. Immer aktuelle Fassung auf bfdi.bund.de prüfen.
- **KI-VO-Überschneidung (ab 2026):** Für KI-Systeme mit hohem Risiko nach VO (EU) 2024/1689 (KI-VO) ist eine Konformitätsprüfung nach KI-VO und eine DSFA nach Art. 35 DSGVO durchzuführen. Beide Instrumente ergänzen sich; die KI-VO-Konformitätsbewertung ersetzt die DSFA nicht. `[Modellwissen – Zeitplan KI-VO prüfen]`

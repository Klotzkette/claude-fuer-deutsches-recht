---
name: regulierungs-luecken-analyse
description: >
  Datenschutz-Gap-Analyse: Abgleich der aktuellen Datenschutzpraxis gegen neue oder
  geänderte Anforderungen aus EDSA-Leitlinien, DSK-Beschlüssen, Gesetzesänderungen oder
  Behördenentscheidungen. Ergebnis: priorisierte Maßnahmenliste mit Handlungsfristen.
language: de
triggers:
  - "Gap-Analyse"
  - "Lückenanalyse"
  - "EDSA-Leitlinie"
  - "DSK-Beschluss"
  - "neue Anforderung"
  - "Umsetzungspflicht"
  - "reg-gap"
  - "Compliance-Check"
---

# DS-Gap-Analyse – Datenschutzrecht

## Zweck

Systematische Lückenanalyse zwischen dem aktuellen Datenschutz-Status der Organisation und neuen oder geänderten Anforderungen aus: EDSA-Leitlinien, DSK-Orientierungshilfen, Gesetzesnovellen (BDSG, TTDSG, sektorspezifisches Recht), Aufsichtsbeschlüssen oder EuGH-Entscheidungen. Ergebnis ist ein priorisierter Umsetzungsplan – kein pauschales Compliance-Dashboard.

## Eingaben

- Neue Anforderung (Leitlinie, Beschluss, Urteil, Gesetz) – als Dokument, URL oder Beschreibung
- Praxisprofil aus `CLAUDE.md` (Verarbeitungsstruktur, aktuelle Maßnahmen, Systemliste)
- Optional: bestehende Datenschutz-Richtlinien, TOMs-Dokumentation, Verarbeitungsverzeichnis

## Ablauf

1. **Anforderungsanalyse.**
   - Dokument oder URL lesen: Was sind die normativen Kernaussagen?
   - Handelt es sich um verbindliche Anforderungen (VO, Beschluss Art. 65 DSGVO) oder Leitlinien mit Empfehlungscharakter (die dennoch Behördenpraxis widerspiegeln)?
   - Sachlicher Anwendungsbereich: Gilt die Anforderung für diese Organisation? (Branche, Verarbeitungsart, Größe, Drittlandbezug)
   - Zeitlicher Geltungsbeginn und ggf. Übergangsfristen?

2. **Anforderungs-Inventur.**
   Aus dem Dokument alle konkreten Anforderungen extrahieren und strukturieren:

   | Nr. | Anforderung | Norm / Quelle | Verbindlich? | Frist |
   |---|---|---|---|---|
   | 1 | [Konkrete Pflicht] | [Art. X DSGVO / EDSA-Leitlinie Y] | Ja/Empfehlung | [Datum] |
   | … | … | … | … | … |

3. **Ist-Zustand-Abgleich.**
   Für jede Anforderung: Erfüllt die aktuelle Praxis die Anforderung?
   - Vollständig erfüllt ✅
   - Teilweise erfüllt ⚠️ (Lücke beschreiben)
   - Nicht erfüllt 🔴 (Lücke beschreiben)
   - Nicht anwendbar auf diese Organisation ⬜

4. **Gap-Bewertung.**
   Für jede Lücke (⚠️ oder 🔴):
   - Rechtliches Risiko (Bußgeld Art. 83 DSGVO, Unterlassung, Schadensersatz Art. 82 DSGVO)
   - Reputationsrisiko
   - Umsetzungsaufwand (hoch / mittel / gering)
   - Priorität (kombiniert aus Risiko und Aufwand)

5. **Maßnahmenplan.**
   Priorisierte Liste konkreter Umsetzungsschritte:

   | Priorität | Lücke | Maßnahme | Verantwortlich | Frist | Status |
   |---|---|---|---|---|---|
   | 🔴 Kritisch | [Beschreibung] | [Konkrete Maßnahme] | [Abteilung] | [Datum] | Offen |
   | 🟠 Hoch | … | … | … | … | … |
   | 🟡 Mittel | … | … | … | … | … |

6. **EDSA-/DSK-Positionierung.**
   Bei widersprüchlichen Leitlinien zwischen EDSA und DSK (z.B. Cookie-Einwilligung): DSK-Position für Deutschland maßgeblich; EDSA-Position als EU-weiter Standard vermerken; Abweichungen kennzeichnen.

7. **Muster-Dokumente oder Klauseln.**
   Für häufig nachgefragte Anpassungen: Textbausteine oder Klauselentwürfe anbieten (AVV-Anlagen, DSFA-Trigger-Kriterien, Datenschutzerklärungsabschnitte).

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 5 DSGVO (Grundsätze)
- Art. 24, 25, 32 DSGVO (Verantwortlichkeit, Privacy by Design, Sicherheit)
- Art. 35 DSGVO (DSFA)
- Art. 44–49 DSGVO (Drittlandtransfer)
- Art. 65 DSGVO (verbindliche EDSA-Beschlüsse)
- Art. 83, 84 DSGVO (Bußgelder)
- §§ 19–26 TTDSG (Cookie-Einwilligung, Endgerätezugriff)
- EDSA-Leitlinien 01/2022 zu Datenübermittlungen
- EDSA-Leitlinien 05/2020 zu Einwilligung
- EDSA-Empfehlungen 01/2020 (TIA)
- DSK-Orientierungshilfe zu Telemedien (aktuell Stand) `[Modellwissen – aktuellen Stand auf dskonferenz.de prüfen]`
- EuGH, Urt. v. 16.07.2020 – C-311/18 (Schrems II), NJW 2020, 2945 (Drittlandtransfer)
- EuGH, Urt. v. 04.07.2023 – C-252/21 (Meta Platforms), NJW 2023, 2997 (berechtigtes Interesse)
- Holznagel/Hartmann, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 83 Rn. 1 ff.
- Nguyen, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 44 Rn. 1 ff.
- Schulze, in: BeckOK DSGVO, 16. Ed. (Stand 01.11.2024), Art. 83 Rn. 1 ff.

## Ausgabeformat

1. **Kopfzeile:** Analysierte Anforderung, Datum, Anwendungsbereich (ja/nein/teilweise)
2. **Anforderungs-Inventur** (Tabelle)
3. **Ist-Zustand-Abgleich** (Gap-Tabelle: Anforderung | Status | Lückenbeschreibung)
4. **Gap-Bewertung** (mit Risikobeschreibung)
5. **Maßnahmenplan** (Prioritäts-Tabelle mit Fristen)
6. **Entscheidungsoptionen**

## Beispiel (EDSA-Leitlinie zu Drittlandtransfers)

**Anforderung:** EDSA-Empfehlungen 01/2020 zur Transferfolgenabschätzung (TIA) – Schritt-6-Methodik nach Schrems II.

**Ist-Zustand (Beispiel):**
Organisation nutzt AWS US-East als Backup-System. AVV enthält EU-SCC Modul 2. Keine TIA dokumentiert.

**Gap:**
- EDSA-Empfehlungen 01/2020, Schritt 3: Rechtslage im Empfängerland bewerten.
- EDSA-Empfehlungen 01/2020, Schritt 4: Auf Lücken in Schutzäquivalenz prüfen.
- EDSA-Empfehlungen 01/2020, Schritte 5–6: Ergänzende Maßnahmen / Zurückhalten der Übermittlung.
- **Gap:** TIA fehlt vollständig. SCC ohne TIA schützt zwar formal, aber EuGH, Urt. v. 16.07.2020 – C-311/18, NJW 2020, 2945 Rn. 134: „Die Übermittlung auf der Grundlage von Standarddatenschutzklauseln ist nur dann zulässig, wenn der Schutz des angemessenen Schutzniveaus durch die Klauseln plus ergänzende Maßnahmen im Empfängerland gewährleistet ist."

**Maßnahme (Priorität 🟠):**
1. TIA für AWS US-East nach EDSA-Empfehlungen 01/2020 erstellen (2 Wochen, DSB + IT-Sicherheit).
2. Ergebnis in AVV-Anlage dokumentieren.
3. Falls TIA kein angemessenes Schutzniveau ergibt: AWS EU-Hosting als Alternative prüfen oder Backup-Strategie anpassen.

## Risiken / typische Fehler

- **Leitlinie mit VO verwechseln:** EDSA-Leitlinien sind keine verbindlichen Rechtsnormen, spiegeln aber die Behördenpraxis wider. Sie werden von Aufsichtsbehörden bei Prüfungen angewandt; Abweichungen sind begründungspflichtig.
- **Zeitliche Geltung nicht geprüft:** Neue Leitlinien gelten nicht rückwirkend; ältere Verträge müssen ggf. angepasst werden. Übergangsfristen aus der Leitlinie herausarbeiten.
- **Nur horizontale Analyse:** Gap-Analyse sollte nicht nur die neue Anforderung, sondern auch prüfen, ob andere bekannte Anforderungen bereits durch die gefundenen Maßnahmen mitadressiert werden (Synergien).
- **Maßnahmenplan ohne Verantwortliche:** Maßnahmen ohne Zuordnung versanden. Jede Maßnahme braucht eine Person und ein Datum.
- **Bußgeld-Kalkulation:** Art. 83 Abs. 4 DSGVO (bis 10 Mio. EUR / 2 % des weltweiten Jahresumsatzes) und Art. 83 Abs. 5 DSGVO (bis 20 Mio. EUR / 4 %) sind Deckel, keine Automatismen. Deutsche Aufsichtsbehörden orientieren sich am DSK-Konzept zur Bußgeldbemessung. `[Modellwissen – aktuellen Beschluss prüfen]`

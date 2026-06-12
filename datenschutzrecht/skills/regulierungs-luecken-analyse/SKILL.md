---
name: regulierungs-luecken-analyse
description: "Regulatorische Luecken im Datenschutzrecht identifizieren und Handlungsoptionen aufzeigen. Art. 5 6 24 DSGVO BDSG. Prüfraster: Bestandsaufnahme bestehender Maßnahmen Soll-Ist-Abgleich Lueckenbewertung Prioritaeten. Output: Lueckenanalyse Maßnahmenkatalog Prioritaetenliste. Abgrenzung: nicht für..."
---

# DS-Gap-Analyse – Datenschutzrecht

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
- §§ 19–26 TDDDG (Cookie-Einwilligung, Endgerätezugriff)
- EDSA-Leitlinien 01/2022 zu Datenübermittlungen
- EDSA-Leitlinien 05/2020 zu Einwilligung
- EDSA-Empfehlungen 01/2020 (TIA)
- DSK-Orientierungshilfe zu Telemedien (aktuell Stand) `[Modellwissen – aktuellen Stand auf dskonferenz.de prüfen]`
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beispiel (EDSA-Leitlinie zu Drittlandtransfers)

**Anforderung:** EDSA-Empfehlungen 01/2020 zur Transferfolgenabschätzung (TIA) – Schritt-6-Methodik nach Schrems II.

**Ist-Zustand (Beispiel):**
Organisation nutzt AWS US-East als Backup-System. AVV enthält EU-SCC Modul 2. Keine TIA dokumentiert.

**Gap:**
- EDSA-Empfehlungen 01/2020, Schritt 3: Rechtslage im Empfängerland bewerten.
- EDSA-Empfehlungen 01/2020, Schritt 4: Auf Lücken in Schutzäquivalenz prüfen.
- EDSA-Empfehlungen 01/2020, Schritte 5–6: Ergänzende Maßnahmen / Zurückhalten der Übermittlung.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

## Quellen / Updates

Stand: 05/2026. Lückenliste laufend aktualisieren bei neuen EDSA-Leitlinien (edpb.europa.eu), DSK-Beschlüssen (dskonferenz.de) und EuGH-Vorabentscheidungen zu DSGVO-Grundbegriffen.

**Querverweise:**
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Gap-Analyse bei neuen Angemessenheitsbeschlüssen oder SCC-Änderungen
- `datenschutzrecht/skills/richtlinien-monitor/SKILL.md` — Interner Praxis-Drift nach regulatorischer Änderung
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — DSFA-Pflicht bei neuen regulatorischen Anforderungen

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Welcher Anlass? (Neues Gesetz/EDSA-Leitlinie, Audit-Befund, Behördenentscheidung, Regelmäßige Überprüfung)
2. Welcher Scope? (gesamtes Unternehmen / bestimmte Verarbeitungstätigkeiten / bestimmte Systeme)
3. Wie sind die Ergebnisse zu priorisieren? (Bußgeldrisiko / Reputationsrisiko / Betroffenenrisiko)
4. Wer ist verantwortlich für die Umsetzung der Maßnahmen?

## Output-Template — Gap-Analyse-Ergebnis

**Adressat:** DSB / Management / Rechtsabteilung — Tonfall: sachlich-strukturiert

```
Regulierungs-Lücken-Analyse [DATUM]
Organisation: [NAME]
Scope: [BESCHREIBUNG]
Anlass: [NEUES GESETZ / AUDIT / REGELMAESSIG]

Gap-Tabelle:
| Nr. | Anforderung (Norm) | Ist-Stand | Luecke | Prioritaet | Frist |
|-----|----------------------|------------------|-------------------|------------|-------|
| 1 | Art. 30 DSGVO VVT | unvollstaendig | 3 Eintraege fehlen| HOCH | [DATUM]|
| 2 | § 25 TDDDG Cookie | nicht konform | kein TCF-Consent | HOCH | [DATUM]|
| 3 | Art. 37 DSGVO DSB | kein DSB bestellt| Bestellungspflicht| MITTEL | [DATUM]|

Zusammenfassung:
Kritische Lücken (ROT): [X]
Mittlere Lücken (GELB): [X]
Geringe Lücken (GRUEN): [X]

Empfehlung: Maßnahmenplan bis [DATUM]
```

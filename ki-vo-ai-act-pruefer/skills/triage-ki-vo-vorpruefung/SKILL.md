---
name: triage-ki-vo-vorpruefung
description: "Nutzer kommt mit unklarer KI-VO-Frage oder moeglicherweise betroffener Software und fragt: Wie starte ich die KI-VO-Pruefung? Eingangs-Triage-Skill. Pruefraster: Erfassung ob eigene Softwareentwicklung fremder Dienst Produktintegration oder Beratungsanfrage. Eingangsfragen zu Systemart Branche Einsatzgebiet Rolle des Anfragenden. Output: Weiterleitung zum naechsten passenden Skill entscheidungsbaum-ki-vo-gesamt-workflow oder risikoklassen-uebersicht-und-triage. Warnt vor typischen Fehlzuordnungen. Abgrenzung zu liegt-ki-system-vor-art-3-nr-1 (Vollpruefung KI-System-Definition)."
---

# Triage: KI-VO-Vorprüfung — Was prüft der Nutzer?

## Zweck

Dieser Skill ist der Einstiegspunkt in den vollständigen Prüfungsworkflow der Verordnung (EU) 2024/1689 (KI-VO). Bevor Risikoklassen, Pflichten oder Verbote geprüft werden können, muss das System verstehen, welchen Sachverhalt der Nutzer einbringt und welche Rolle er in Bezug auf das fragliche System einnimmt.

## Eingangsfragen

Das System stellt folgende Fragen der Reihe nach:

**Frage 1 — Art des Gegenstands**

Was wird geprüft?
- (A) Ich habe selbst eine Software oder ein System entwickelt oder lasse es entwickeln.
- (B) Ich nutze einen fremden KI-Dienst (Cloud-Dienst, Drittanbieter-Produkt, API) in meinem Betrieb.
- (C) Ich integriere ein KI-System oder KI-Komponente in ein eigenes Produkt.
- (D) Ich berate Mandanten zu einem KI-System oder einer KI-VO-Fragestellung.
- (E) Ich weiß noch nicht genau — bitte führe mich.

**Frage 2 — Beschreibung des Systems**

Bitte beschreiben Sie in Stichpunkten:
- Was tut das System? (Beispiele: Bilderkennung, Textgenerierung, Scoring, Empfehlung, Entscheidungsunterstützung)
- In welchem Bereich wird es eingesetzt? (Beispiele: Personalwesen, Medizin, Kredit, Strafverfolgung, Bildung, allgemeine Nutzung)
- Wer sind die betroffenen Personen? (Beispiele: Bewerber, Patienten, Kreditnehmer, Bürger)

**Frage 3 — Standort und Markt**

- Wo soll das System eingesetzt werden? (EU / außerhalb EU / unklar)
- Werden Ausgaben des Systems in der EU verwendet, auch wenn das System außerhalb betrieben wird?

## Plausibilitätsprüfung

Das System prüft auf Basis der Eingaben:
- Handelt es sich möglicherweise gar nicht um ein KI-System im Sinne von Art. 3 Nr. 1 KI-VO? → Weiterleitung zu `liegt-ki-system-vor-art-3-nr-1`
- Liegt ein offensichtlicher Ausschluss nach Art. 2 Abs. 3 bis 12 vor (Militär, rein persönliche Nutzung)? → Weiterleitung zu `sachlicher-ausschluss-art-2-abs-3-bis-12`
- Verwechselt der Nutzer die KI-VO mit einem anderen Rechtsgebiet (DSGVO, Produkthaftung)? → Weiterleitung zu `falsche-wiese-warnung-ki-vo`

## Routing-Logik

| Antwort | Nächster Skill |
|---|---|
| Variante A oder C | `liegt-ki-system-vor-art-3-nr-1` → `rolle-anbieter-pruefen-art-3-nr-3` |
| Variante B | `liegt-ki-system-vor-art-3-nr-1` → `rolle-betreiber-pruefen-art-3-nr-4` |
| Variante D | `mandatsabbruch-empfehlung-komplexe-faelle` (Hinweis auf Grenzen des Mechanik-Workflows) |
| Variante E | Rückfragen zu Beschreibung, dann Routing nach Sachverhalt |

## Wichtige Einschränkungen

- Das System akzeptiert keine fiktiven Testdaten oder Mustersachverhalte.
- Unvollständige Sachverhalte führen zu unvollständigen Ergebnissen — das System weist ausdrücklich darauf hin.
- Dieser Workflow ist ein mechanisches Prüfinstrument, kein juristisches Gutachten.

## Warnblock

**Achtung — Keine Rechtsberatung:**
Dieser Skill erfasst nur, was der Nutzer mitteilt. Er kann nicht prüfen, ob die Sachverhaltsdarstellung vollständig oder korrekt ist. Alle Ergebnisse stehen unter dem Vorbehalt der vom Nutzer behaupteten Tatsachen.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- EuGH, Urt. v. 07.12.2023 — C-634/21 (SCHUFA-Score), NJW 2024, 248 Rn. 49: KI-Scoring-System als automatisierte Einzelentscheidung nach Art. 22 DSGVO — Masstab fuer Hochrisiko-Klassifikation und Betreiberpflichten nach KI-VO.
- EuGH, Urt. v. 04.10.2024 — C-203/22 (Dun & Bradstreet), NJW 2025, 56 Rn. 38: Betreiber muss Entscheidungslogik offenlegen — Art. 13 KI-VO Transparenzpflicht und Art. 26 Abs. 6 Korrekturrecht.
- BGH, Urt. v. 19.06.2018 — VI ZR 184/17, NJW 2018, 2877 Rn. 15: Organisationspflichten bei technischen Systemen — massgeblich fuer KI-VO Betreiberpflichten und interne Governance.
- EuGH, Urt. v. 16.07.2020 — C-311/18 (Schrems II), NJW 2020, 2557 Rn. 87: Drittlandtransfer bei KI-APIs erfordert Schutzgarantien; Art. 28 DSGVO AVV in KI-Lieferkette.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Kommentarliteratur
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 2 Rn. 1: Anwendungsbereich und Pflichten.
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10: Wechselwirkung KI-VO und DSGVO.

## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — TRIAGE KI VO VORPRUEFUNG
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 2 Rn. 1]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

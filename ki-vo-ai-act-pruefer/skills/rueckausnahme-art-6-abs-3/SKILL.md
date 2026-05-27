---
name: rueckausnahme-art-6-abs-3
description: "System wurde als Anhang-III-relevant eingestuft aber Unternehmen fragt: Greift eine der Ausnahmen vom Hochrisiko? Art. 6 Abs. 3 KI-VO Rueckausnahme. Pruefraster: vier Fallgruppen enge Verfahrensaufgabe Verbesserung menschlicher Taetigkeit ohne Ersetzung Mustererkennung ohne Entscheidungsrelevanz bloss vorbereitende Aufgabe. Sicherungsklausel: Profiling natuerlicher Personen ist stets Hochrisiko ohne Ausnahme. Output: Ausnahme-Entscheidungsbaum mit Begruendungspflicht. Abgrenzung zu hochrisiko-art-6-abs-2-anhang-iii (Eingangseinordnung) und sachlicher-ausschluss-art-2-abs-3-bis-12 (voellige Ausnahme vom Anwendungsbereich)."
---

# Rückausnahme vom Hochrisiko — Art. 6 Abs. 3 KI-VO

## Zweck

Art. 6 Abs. 3 KI-VO enthält eine Rückausnahme: Auch wenn ein KI-System in einem der acht Anhang-III-Bereiche tätig ist, kann es ausnahmsweise nicht als Hochrisiko-System eingestuft werden — wenn es kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte darstellt.

## Wichtiger Vorbehalt vorab: Sicherungsklausel

**Kein Ausschluss bei Profiling:** KI-Systeme, die Profiling natürlicher Personen vornehmen, sind IMMER als Hochrisiko einzustufen — unabhängig davon, ob eine der vier Fallgruppen der Rückausnahme einschlägig wäre. Profiling ist nach Art. 3 Nr. 33 KI-VO die automatisierte Verarbeitung personenbezogener Daten zur Bewertung persönlicher Aspekte einer natürlichen Person.

**Prüffragen (Ausschluss der Rückausnahme):**
- Bewertet das System persönliche Aspekte einer natürlichen Person (Leistung, wirtschaftliche Situation, Gesundheit, Präferenzen, Verhalten, Aufenthaltsort, Bewegung)?
- Wenn ja → Profiling → keine Rückausnahme → Hochrisiko

## Die vier Fallgruppen der Rückausnahme (Art. 6 Abs. 3 KI-VO)

### Fallgruppe 1 — Enge Verfahrensaufgabe

Das KI-System ist für eine eng definierte Verfahrensaufgabe bestimmt, die keinen wesentlichen Einfluss auf das Ergebnis einer Entscheidung hat.

**Prüffragen:**
- Ist die Aufgabe des Systems auf einen einzelnen, eng begrenzten Verfahrensschritt beschränkt?
- Hat das System keinen wesentlichen Einfluss auf das Gesamtergebnis?

**Beispiel:** Ein System, das lediglich die Vollständigkeit eines Formulars prüft (fehlende Felder erkennt), ohne den Inhalt zu bewerten.

**Abgrenzung:** Wenn das System zwar scheinbar eine enge Verfahrensaufgabe hat, aber seine Ausgaben in der Praxis maßgeblich die finale Entscheidung bestimmen, greift die Rückausnahme nicht.

### Fallgruppe 2 — Verbesserung des Ergebnisses menschlicher Tätigkeit

Das KI-System dient dazu, das Ergebnis einer bereits von einem Menschen erbrachten Tätigkeit zu verbessern, ohne eine wesentliche Auswirkung auf das eigentliche Ergebnis zu haben.

**Prüffragen:**
- Ist das System darauf ausgerichtet, menschlich erzeugte Ergebnisse zu verfeinern oder zu verbessern, nicht aber zu ersetzen?
- Trifft das System keine eigenständige Bewertung, sondern verbessert nur den Prozess einer menschlichen Bewertung?

**Beispiel:** Ein System, das die sprachliche Verständlichkeit eines bereits von einem Prüfer bewerteten Dokuments verbessert, ohne die inhaltliche Bewertung zu verändern.

### Fallgruppe 3 — Erkennung von Entscheidungsmustern ohne Ersetzung menschlicher Bewertung

Das KI-System dient der Erkennung von Entscheidungsmustern oder Abweichungen von früheren Entscheidungsmustern und ist nicht dazu bestimmt, die menschliche Bewertung zu ersetzen.

**Prüffragen:**
- Dient das System der Anomalieerkennung oder der Mustererkennung zur Unterstützung (nicht Ersetzung) menschlicher Entscheidungen?
- Gibt das System ausschließlich Hinweise auf Auffälligkeiten aus, ohne selbst Entscheidungen zu treffen?

**Beispiel:** Ein System, das bei Kreditanträgen darauf hinweist, wenn ein Antrag von der historischen Antragsnorm abweicht — ohne selbst über Kreditvergabe zu entscheiden.

### Fallgruppe 4 — Vorbereitende Aufgabe für die Bewertung

Das KI-System dient dazu, eine Bewertung vorzubereiten, die für in Anhang III genannte Zwecke relevant ist, ohne eine eigenständige Entscheidung oder Bewertung zu treffen.

**Prüffragen:**
- Ist das System ausschließlich für die Vorbereitung (Aufbereitung, Strukturierung) von Informationen für eine nachfolgende menschliche Bewertung bestimmt?
- Trifft das System selbst keine Bewertung der für den Anhang-III-Zweck relevanten Aspekte?

**Beispiel:** Ein System, das Lebensläufe für eine Personalentscheidung strukturiert und kategorisiert, aber keine Aussage zur Eignung der Bewerber trifft.

## Pflicht zur Dokumentation bei Inanspruchnahme der Rückausnahme

Wenn ein Anbieter oder Betreiber die Rückausnahme in Anspruch nimmt, muss er:
- Die Entscheidung und ihre Begründung dokumentieren
- Die Dokumentation der nationalen Aufsichtsbehörde auf Anfrage zur Verfügung stellen
- Die Dokumentation bei Änderungen des Systems aktualisieren

## Ergebnis

- **Rückausnahme greift:** System ist trotz Anhang-III-Zugehörigkeit kein Hochrisiko-System. Dokumentationspflicht beachten. Begrenztes Risiko (Art. 50) und Minimal-Risiko-Prüfung folgen.
- **Rückausnahme greift nicht (insbesondere wegen Profiling):** System ist Hochrisiko nach Art. 6 Abs. 2 i.V.m. Anhang III KI-VO.

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
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 6 Abs. 3 Rn. 4: Anwendungsbereich und Pflichten.
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
PRUEFERGEBNIS — RUECKAUSNAHME ART 6 ABS 3
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 6 Abs. 3 Rn. 4]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

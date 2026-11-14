---
name: ampelsystem-tabellenausgabe
description: "Für Ampelsystem-Tabellenausgabe: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Ampelsystem-Tabellenausgabe

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Element | Ampel-Zuordnung |
|---|---|
| Note 1-Formel vorhanden | Grün |
| Note 2-Formel vorhanden | Grün |
| Note 3-Formel vorhanden | Orange |
| Note 4-Formel vorhanden | Rot |
| Note 5-Formel vorhanden | Rot |
| Gemischter Satz (grün + orange) | Orange gesamt |
| Gemischter Satz (grün + rot) | Rot gesamt |
| Fehlende Pflichtaussage | Rot |

## Beispiele

**Beispiel 1 – Ausgabe für Note-1-Zeugnis:**

| Satz | Ampel | Bewertung | Notentendenz | Begründung |
|---|---|---|---|---|
| "stets zur vollsten Zufriedenheit" | Grün | Note 1 | Stabil | Vollständige Maximalformel |
| "stets einwandfrei" (Verhalten) | Grün | Note 1 | Stabil | Maximale Verhaltensformel |
| Vollständige Schlussformel | Grün | Note 1-2 | Stabil | Alle drei Elemente vorhanden |

**Beispiel 2 – Ausgabe für gemischtes Zeugnis:**

| Satz | Ampel | Bewertung | Notentendenz | Begründung |
|---|---|---|---|---|
| "zur vollen Zufriedenheit" | Orange | Note 3 | Abschwächend | Fehlendes "stets" |
| "bemüht" (Leistungsaussage) | Rot | Note 4 | Abwärts | Rotes Signal durch "bemüht" |
| Schlussformel ohne Bedauern | Orange | Note 3 | Abschwächend | Fehlendes Bedauern |

**Beispiel 3 – Gesamtzusammenfassung:** Grüne Sätze: 4 / Orange Sätze: 2 / Rote Sätze: 1 → Gewichtete Gesamtnote: Note 2 bis 3. Empfehlung: Nachverhandlung des roten Satzes und eines orangen Satzes sinnvoll.

## Rechtliche Einordnung und Normen

- **Paragraf 109 GewO** — Anspruch auf qualifiziertes Zeugnis; Wohlwollensgebot und Wahrheitspflicht
- **Paragraf 109 Abs. 2 GewO** — Zeugnis muss klar und verständlich formuliert sein; Codierungen, die Fortkommen erschweren, verstoßen gegen Wohlwollensgebot

## Triage — vor der Tabellenausgabe klären

1. Welche Analyse-Skills wurden bereits ausgeführt? (Leistungsbeurteilung, Verhaltensbeurteilung, Schlussformel)
2. Liegt ein vollständiges Zeugnisdokument vor oder nur Auszüge?
3. Ist das Ziel: Mandantenbericht, Klageantrag-Vorbereitung oder interne Einschätzung?


## Ampel-Symbol-Disziplin

**Die Ampel wird grafisch gesetzt, nicht als Farbwort geschrieben.** In jeder Ausgabe gilt:

- 🔴 = Rot (Note 4-6, Negativcode, dringender Berichtigungspunkt)
- 🟠 = Orange (Note 3, Abschwaechung, Verhandlungspunkt) - bei Darstellungsproblemen: 🟡
- 🟢 = Gruen (Note 1-2, unbedenklich)

Regeln:

1. In Matrizen, Tabellen und Fliesstext immer das **farbige Ampelsymbol** setzen ("🔴"), nicht "Rot". Die Farbwoerter in internen Katalogtabellen sind Kodierung - in der Nutzerausgabe erscheinen Symbole.
2. In reiner ASCII-Umgebung ersatzweise `[ROT]`, `[ORANGE]`, `[GRUEN]` in Grossbuchstaben.
3. Im **Hauptbefund** zusaetzlich eine Ampel-Bilanz-Zeile ausgeben: `Ampel-Bilanz: 🔴 4 · 🟠 3 · 🟢 5`.
4. Mischbefunde als Doppelsymbol: 🟢🟠.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.

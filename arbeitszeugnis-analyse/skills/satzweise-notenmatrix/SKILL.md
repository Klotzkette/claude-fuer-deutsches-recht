---
name: satzweise-notenmatrix
description: "Bewertet jeden notenrelevanten Satz eines Arbeitszeugnisses mit Schulnote 1 bis 5. Anwendungsfall notenrelevante Saetze wurden identifiziert und sollen systematisch bewertet werden. Normen § 109 GewO Bewertungsmassstab BAG-Linie zur Zeugnissprache. Prüfraster Satzkurzform Themenbereich Note Steigerungsadverb-Befund Begründung. Output Geschlossene Notenmatrix als Grundlage für Bereichs-Drift-Detektor und Gesamtnoten-Aggregation. Abgrenzung zu notenrelevante-saetze-identifizieren (Vorstufe) und gesamtnoten-aggregation (Folgestufe)."
---

# Satzweise Notenmatrix

Die Ampelfarbe allein reicht nicht, um ein Zeugnis sauber zu bewerten. Wer Drift erkennen, Schwerpunkte verschieben oder gezielt nachverhandeln will, braucht die Note jedes einzelnen notenrelevanten Satzes. Dieser Skill liefert genau das: eine vollständige Tabelle mit Satz, Themenbereich und Note von eins bis fünf.

Die Notenzuweisung folgt keinem starren Automaten, sondern einer sprachlichen Plausibilitätsprüfung. Note 1 erfordert regelmäßig ein Steigerungsadverb ("stets", "jederzeit", "äußerst", "vollkommen", "in höchstem Maße") in Kombination mit einem Superlativ oder einer Maximalformel. Note 2 hat das Adverb, aber keinen Superlativ, oder den Superlativ ohne durchgehende Zeitkomponente. Note 3 enthält die Grundaussage ohne Steigerungsadverb und ohne Superlativ. Note 4 nutzt Einschränkungen ("im Wesentlichen", "weitgehend", "im Großen und Ganzen") oder das Codewort "bemüht". Note 5 fehlt die positive Aussage ganz oder enthält Distanzformeln, die im konkreten Kontext abwertend wirken.

Die Themenbereich-Zuordnung folgt acht Kategorien: Fachkenntnisse, Lernbereitschaft, strategisches Denken, Arbeitsweise, Engagement, Innovation, Arbeitsergebnis und Sozialverhalten. Sätze, die mehreren Bereichen zugeordnet werden können, erhalten Mehrfachzuordnung. Die Matrix ist die direkte Eingangsbasis fuer den Bereichs-Drift-Detektor: ohne saubere Einzelnoten kein Drift-Befund.

Besondere Aufmerksamkeit gilt zwei Mustern: erstens dem fehlenden Steigerungsadverb bei sonst guter Formulierung, zweitens dem positiv klingenden Verb ohne Qualifikator ("zeigte", "fand", "war in der Lage"). Diese Konstruktionen sind häufig mittelwertig, aber nicht automatisch schlecht. Entscheidend bleiben Position, Branche, Aufgabenprofil und Gesamtzusammenhang.

## Geheimcode-Regeln

| Sprachmuster | Note |
|---|---|
| Steigerungsadverb plus Superlativ ("stets äußerst", "jederzeit hervorragend") | Note 1 |
| Superlativ ohne Adverb oder Adverb ohne Superlativ | Note 2 |
| Grundaussage ohne Adverb, ohne Superlativ ("gute Ideen", "hohe Lernbereitschaft") | Note 3 |
| Einschränkung ("im Wesentlichen", "weitgehend") oder Codewort "bemüht" | Note 4 |
| "angemessen", "korrekt" im Leistungsteil, fehlende positive Aussage | Note 5 |
| "zeigte", "fand", "war in der Lage zu" ohne Steigerung | Note 3 |
| "verfügt über" ohne Steigerung | Note 3 |
| "verfügt über äußerst profundes" plus Maximalbereich | Note 1 |

## Beispiele

**Beispiel 1 – Note 1:** "verfuegt auch in Randbereichen seines vielfaeltigen Aufgabenbereiches ueber aeusserst profundes Fachwissen" → Steigerungsadverb "aeusserst", Maximalbereichsangabe "auch in Randbereichen", Superlativ "profundes". Themenbereich Fachkenntnisse.

**Beispiel 2 – Note 3:** "nahm in eigener Initiative regelmaessig erfolgreich an internen und externen Weiterbildungsseminaren teil" → kein Steigerungsadverb, kein Superlativ ("regelmaessig" ist Haeufigkeit, kein Steigerer). Themenbereich Lernbereitschaft.

**Beispiel 3 – Note 1:** "Alle Aufgaben fuehrte er jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig und planvoll durchdacht aus" → drei Steigerer ("jederzeit", "vollkommen", "aeusserst"). Themenbereich Arbeitsweise.

**Beispiel 4 – Note 3:** "war Neuem gegenueber aufgeschlossen, fand gute neue Ideen und innovative Ansaetze" → "gute" statt "hervorragende", kein Steigerungsadverb, Verb "fand" statt "entwickelte". Themenbereich Innovation.

**Beispiel 5 – Note 1:** "Arbeitsergebnisse lagen stets sehr weit ueber unseren Anforderungen" → Steigerer "stets sehr weit", expliziter Vergleich "ueber unseren Anforderungen". Themenbereich Arbeitsergebnis.

**Beispiel 6 – Note 3:** "war ein geschaetzter Ansprechpartner, sein persoenliches Verhalten war einwandfrei" → "geschaetzt" ohne Steigerung, "einwandfrei" ohne "stets". Themenbereich Sozialverhalten.

**Beispiel 7 – Note 4:** "war stets bemueht" → Codewort, unabhaengig vom restlichen Satz. Themenbereich je nach Kontext.

## Ausgabeformat

Tabelle mit den Spalten: laufende Nummer, Satzkurzform (gekuerzt auf maximal achtzig Zeichen), Themenbereich, Note, erkannte Steigerungsadverbien, erkannte Superlative, Begruendung in einem Satz. Anschliessend eine Bereichsuebersicht mit Anzahl Saetze und Notenmittel je Themenbereich. Diese Matrix dient als Eingangsbasis fuer den Bereichs-Drift-Detektor und die Gesamtnoten-Aggregation.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

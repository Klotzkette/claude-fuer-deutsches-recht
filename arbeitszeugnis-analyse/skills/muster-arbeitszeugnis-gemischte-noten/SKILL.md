---
name: muster-arbeitszeugnis-gemischte-noten
description: "Anonymisiertes Schulungszeugnis mit Schaufenster-Pattern für Training und Demonstration. Anwendungsfall Rechtsanwalt oder Mitarbeiter will Zeugnisanalyse-Skills an einem Musterfall trainieren. Zeigt klassisches Drift-Muster einzelne Saetze Note eins benachbarte Saetze Note drei gleicher Themenbereich. Output vollständige Satz-für-Satz-Notenmatrix mit Bereichs-Drift-Analyse als kommentiertes Lernbeispiel. Abgrenzung zu muster-arbeitszeugnis-mit-roten-flaggen und muster-arbeitszeugnis-note-1."
---

# Muster-Arbeitszeugnis mit gemischten Noten (Schulungsmaterial)

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Satz im Muster | Themenbereich | Note | Befund |
|---|---|---|---|
| "verfuegt auch in Randbereichen über aeusserst profundes Fachwissen" | Fachkenntnisse | 1 | Steigerer plus Maximalbereich |
| "nahm regelmaessig erfolgreich an Weiterbildungsseminaren teil" | Lernbereitschaft | 3 | Kein Steigerungsadverb |
| "ausgeprägt strategisches Denkvermoegen, stets in kuerzester Zeit optimale Loesungen" | Strategisches Denken | 1 | "stets" plus Superlativ |
| "zeigte sich bei neuen Aufgabenbereichen flexibel und aufgeschlossen" | Flexibilitaet | 3 | "zeigte" ohne Steigerung |
| "besonders hohe Arbeitsmoral, stets aeusserst motiviert, beharrlich zu verfolgen" | Engagement | 1 | Drei Steigerer |
| "zeigte eine hohe Lernbereitschaft" | Lernbereitschaft | 3 | "hohe" ohne Adverb |
| "jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig, planvoll durchdacht" | Arbeitsweise | 1 | Drei Steigerer |
| "fand gute neue Ideen und innovative Ansaetze" | Innovation | 3 | "gute" statt "hervorragende" |
| "Arbeitsergebnisse lagen stets sehr weit über unseren Anforderungen" | Arbeitsergebnis | 1 | Maximalvergleich |
| "war in der Lage, Konflikte erfolgreich zu bewaeltigen" | Sozialverhalten | 3 | "war in der Lage" |
| "vollsten Zufriedenheit erfuellt und teilweise sogar uebertroffen" | Gesamtbeurteilung | 1 | Maximalformel |
| "geschaetzter Ansprechpartner, persönliches Verhalten war einwandfrei" | Sozialverhalten | 3 | "einwandfrei" ohne "stets" |
| "stets ausgezeichnete Mitarbeit" plus volles Bedauern und voller Dank | Schlussformel | 1 | Vollstaendig auf Spitze |

## Beispiele

### Vollstaendiges Muster-Schulungszeugnis

---

**Beispiel GmbH, Beispielstrasse 5, 20000 Beispielstadt**

**Arbeitszeugnis**

Herr Albert Beispiel, geboren am neunten Juni neunzehnhundertsiebzig, war vom ersten Januar zweitausendelf bis zum dreissigsten September zweitausenddreizehn als Baumeister im Bereich Geschäftsleitung unseres Unternehmens tätig.

Herr Beispiel verfuegt auch in Randbereichen seines vielfaeltigen Aufgabenbereiches über aeusserst profundes Fachwissen.

Herr Beispiel nahm in eigener Initiative regelmaessig erfolgreich an internen und externen Weiterbildungsseminaren teil.

Hervorzuheben ist sein ausgeprägt strategisches Denkvermoegen, das es ihm ermoeglichte, auch bei neuen geschäftlichen Entwicklungen stets in kuerzester Zeit optimale Loesungen zu entwickeln.

Er zeigte sich auch bei der Bewaeltigung neuer Aufgabenbereiche flexibel und aufgeschlossen.

Herr Beispiel verfuegt über eine besonders hohe Arbeitsmoral und war stets aeusserst motiviert, die gesetzten Ziele beharrlich zu verfolgen.

Herr Beispiel zeigte eine hohe Lernbereitschaft.

Alle Aufgaben fuehrte er jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig und planvoll durchdacht aus. Er agierte immer ruhig, ueberlegt und zielorientiert und in hoechstem Masse praezise.

Herr Beispiel war Neuem gegenueber aufgeschlossen, fand gute neue Ideen und innovative Ansaetze.

Die von Herrn Beispiel entwickelten Arbeitsergebnisse lagen stets sehr weit über unseren Anforderungen.

Herr Beispiel war in der Lage, Konflikte erfolgreich zu bewaeltigen. Durch sein konstruktives Verhalten und ueberlegtes Handeln konnte er so ein gutes Arbeitsklima in seinem Team schaffen.

Herr Beispiel hat die an ihn gestellten sehr hohen Erwartungen zu unserer vollsten Zufriedenheit erfuellt und teilweise sogar uebertroffen.

Wegen seines freundlichen und hilfsbereiten Auftretens war Herr Beispiel ein geschaetzter Ansprechpartner. Sein persönliches Verhalten gegenueber Vorgesetzten, Mitarbeitern und Externen war einwandfrei.

Das Arbeitsverhaeltnis endet aus betriebsbedingten Gruenden zum dreissigsten September zweitausenddreizehn. Wir bedanken uns für seine stets ausgezeichnete Mitarbeit in unserem Unternehmen. Sein Ausscheiden bedauern wir sehr und wuenschen ihm für seine Zukunft beruflich und privat weiterhin viel Erfolg und alles Gute.

---

### Bereichs-Drift-Analyse

| Themenbereich | Hoechste Note | Niedrigste Note | Drift | Ampel |
|---|---|---|---|---|
| Fachkenntnisse | 1 | 1 | keine | Grün |
| Lernbereitschaft | 1 (indirekt aus Engagement) | 3 | zwei Stufen | Rot |
| Strategisches Denken | 1 | 1 | keine | Grün |
| Flexibilitaet | 3 | 3 | keine | Orange |
| Engagement | 1 | 1 | keine | Grün |
| Arbeitsweise | 1 | 1 | keine | Grün |
| Innovation | 3 | 3 | keine | Orange |
| Arbeitsergebnis | 1 | 1 | keine | Grün |
| Sozialverhalten | 3 | 3 | keine | Orange |
| Gesamtbeurteilung und Schlussformel | 1 | 1 | keine | Grün |

### Gesamtnoten-Aggregation

Gewichteter Wert vor Drift-Penalty: Note 1 bis 2. Drift-Penalty Lernbereitschaft (zwei Stufen, weicher Bereich): minus eine halbe Stufe. Konstante Note 3 in Innovation und Sozialverhalten (heikle weiche Bereiche): minus eine halbe Stufe. Gesamtnote nach Aggregation: Note 2 bis Note 3.

### Empfehlung

Spitzensaetze sind authentisch (Fachkenntnisse, Arbeitsweise, Arbeitsergebnis, Engagement). Drift bei Lernbereitschaft, konstant niedrige Note bei Innovation und Sozialverhalten. Nachverhandelbar: Saetze zu Lernbereitschaft, Innovation und Sozialverhalten. Beweislast nach BAG: Gesamtnote schlechter als befriedigend muesste der Arbeitgeber beweisen, Gesamtnote besser als befriedigend muss der Arbeitnehmer beweisen — bei diesem Zeugnis ist die Drei in den weichen Bereichen aus den Formulierungen selbst herauslesbar.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


# Arbeitszeugnis-Analyse (Ampelsystem)

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Analyse deutscher Arbeitszeugnisse nach Ampelsystem. Prüft Geheimcodes, Schaufenster-Drift, negative Codeworte, Steigerungsadverbien, Satznoten und Gesamtnotenspanne. Führt vom Erstgespräch über Mandantenbericht und Aufforderungsschreiben bis zur Klagestrategie.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/arbeitszeugnis-analyse.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnis-analyse.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnis-analyse.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnis-analyse/arbeitszeugnis-analyse-werkstatt.md" download><code>arbeitszeugnis-analyse-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnis-analyse/arbeitszeugnis-analyse-schnellstart.md" download><code>arbeitszeugnis-analyse-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Arbeitszeugnis-Analyse — aus dem blühenden Leben](../testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md) | [Gesamt-PDF](../testakten/arbeitszeugnis-analyse-bluehendes-leben/gesamt-pdf/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf) | [`testakte-arbeitszeugnis-analyse-bluehendes-leben.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitszeugnis-analyse-bluehendes-leben.zip) | [`testakte-arbeitszeugnis-analyse-bluehendes-leben-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitszeugnis-analyse-bluehendes-leben-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein deutsches Arbeitszeugnis nach dem Ampelsystem decodieren, die versteckte Gesamtnote bestimmen und entscheiden, ob sich ein Berichtigungsverlangen oder eine Zeugnisklage lohnt.

Dieses Plugin analysiert deutsche Arbeitszeugnisse nach dem Ampelsystem (Rot/Orange/Grün). Es decodiert den Geheimcode der deutschen Zeugnissprache, identifiziert notenrelevante Sätze und klassifiziert sie mit vollständiger Interpretation der versteckten Bewertung.

Das Plugin richtet sich an Arbeitnehmer, die ihr eigenes Zeugnis verstehen oder verbessern wollen, an Rechtsanwälte, die Zeugnisstreitigkeiten begleiten, und an Personalverantwortliche, die Zeugnisse professionell ausstellen oder prüfen möchten.

**Hinweis:** Im Repository liegt ergänzend die Testakte `testakten/arbeitszeugnis-analyse-bluehendes-leben/` mit zehn realistisch ausgearbeiteten Zeugnisfällen. Jede Ausgabe ist ein Analyse-Entwurf zur eigenverantwortlichen Prüfung — kein Ersatz für anwaltliche Beratung im Einzelfall.

## Ampelsystem

Das Ampelsystem klassifiziert jeden notenrelevanten Satz in drei Kategorien:

| Ampel | Bedeutung | Notentendenz |
|---|---|---|
| **Grün** | Starke positive Formulierung, entspricht dem Geheimcode für Note 1 oder Note 2 | Note 1-2 |
| **Orange** | Schwache positive Formulierung, Note 3, oft durch fehlende Steigerungsadverbien oder Einschränkungen | Note 3 |
| **Rot** | Kodierte Negativaussage, entspricht Note 4 oder Note 5, oft scheinbar positiv formuliert | Note 4-5 |

Rote Signale entstehen durch: das Wort "bemüht", Einschränkungen wie "im Wesentlichen", fehlende positionsnahe Erwartungsbausteine wie Integritäts- oder Führungsverhalten, falsche Reihenfolge bei Personengruppen in der Verhaltensbeurteilung oder eine auffällig kühle Schlussformel. Bei der Schlussformel ist strikt zu trennen: starke Signalwirkung im Bewerbungsverkehr, aber kein automatischer einklagbarer Anspruch auf Dank, Bedauern und Wünsche.

## Enthaltene Skills

Die wichtigsten Skills sind alphabetisch geordnet; die vollständige automatisch generierte Liste steht weiter unten:

| Skill | Funktion |
|---|---|
| `/arbeitszeugnis-analyse:ampelsystem-tabellenausgabe` | Standardisiertes Ausgabeformat mit Ampeltabelle (Satz / Ampel / Bewertung / Note / Begründung) |
| `/arbeitszeugnis-analyse:aufforderungsschreiben-arbeitgeber` | Außergerichtliches Berichtigungsverlangen an den Arbeitgeber mit Wortlaut alt/neu pro Streitstelle |
| `/arbeitszeugnis-analyse:azubi-zeugnis-analyse` | Ausbildungszeugnisse nach BBiG: Lernfortschritt, Berufsschule, Praxis, Verhalten |
| `/arbeitszeugnis-analyse:bereichs-drift-detektor` | Erkennt das Schaufenster-Pattern: Spitzensatz und Durchschnittssatz im selben Themenbereich |
| `/arbeitszeugnis-analyse:branchen-spezifische-formulierungen` | Branchenspezifika für Vertrieb, Recht, IT, Pflege und weitere Bereiche |
| `/arbeitszeugnis-analyse:erstgespraech-und-mandatsannahme` | Mandatsannahme mit Dank für das Zeugnis, Anforderung der noch fehlenden Unterlagen, Erstgespräch-Leitfaden |
| `/arbeitszeugnis-analyse:geheimcode-katalog` | Zentraler Referenzkatalog aller Standardformulierungen mit Ampelzuordnung |
| `/arbeitszeugnis-analyse:gesamtnoten-aggregation` | Aggregation der Einzelbewertungen zur gewichteten Gesamtnote |
| `/arbeitszeugnis-analyse:gruen-flaggen-katalog` | Katalog aller grünen Signale: Superlative, vollständige Formeln, Note 1-2 |
| `/arbeitszeugnis-analyse:klage-strategie-zeugnisberichtigung` | Vom Befund zur Klage: Berichtigungsverlangen, Klageantrag, Beweislast, Streitwert |
| `/arbeitszeugnis-analyse:leitende-positionen-zeugnisse` | Führungskräfte-Zeugnisse: Mitarbeiterführung, Strategie, Loyalität |
| `/arbeitszeugnis-analyse:leistungsbeurteilung-analyse` | Arbeitsqualität, Arbeitsbereitschaft, Belastbarkeit, Eigeninitiative |
| `/arbeitszeugnis-analyse:mandantenbericht-zeugnisanalyse` | Ergebnisbericht an den Arbeitnehmer mit Gesamtnote, kritischen Stellen, drei Handlungsoptionen, klarer Empfehlung |
| `/arbeitszeugnis-analyse:muster-arbeitszeugnis-gemischte-noten` | Schulungsmuster mit Schaufenster-Pattern: 1er- und 3er-Sätze gemischt, vollständige Drift-Analyse |
| `/arbeitszeugnis-analyse:muster-arbeitszeugnis-mit-roten-flaggen` | Schulungsbeispiel mit gemischten Bewertungen und vollständiger Analyse |
| `/arbeitszeugnis-analyse:muster-arbeitszeugnis-note-1` | Vollständiges Musterzeugnis Note 1 — alle Bausteine grün |
| `/arbeitszeugnis-analyse:negationen-und-auslassungen-erkennen` | Fehlende Pflichtaussagen als versteckte Negativsignale erkennen |
| `/arbeitszeugnis-analyse:negative-codeworte-katalog` | Erweiterter Katalog negativer Codeworte: Alkohol, Krankheit, Diebstahl, Konflikte, Loyalität |
| `/arbeitszeugnis-analyse:notenrelevante-saetze-identifizieren` | Trennung notenrelevanter Sätze von neutralen Aufgabenbeschreibungen |
| `/arbeitszeugnis-analyse:orange-flaggen-katalog` | Schwache positive Formulierungen, Note 3, fehlende Steigerungen |
| `/arbeitszeugnis-analyse:rechtliche-bewertung-bag-rechtsprechung` | Paragraf 109 GewO, BAG-Rechtsprechung, Beweislast, Zeugnisklage |
| `/arbeitszeugnis-analyse:rote-flaggen-katalog` | Klassische Warnsignale: "bemüht", "im Großen und Ganzen", Note 4-5 |
| `/arbeitszeugnis-analyse:satzweise-notenmatrix` | Satz-für-Satz-Notenzuweisung von eins bis fünf mit Themenbereich — Datenbasis für Drift |
| `/arbeitszeugnis-analyse:schlussformel-bewertung` | Bedauern, Dank, Zukunftswünsche — Signalwirkung, Ton und rechtliche Durchsetzbarkeit getrennt |
| `/arbeitszeugnis-analyse:steigerungsadverbien-katalog` | Vollständige Referenzliste der Steigerer mit Notenwirkung — echte, scheinbare und negative Adverbien |
| `/arbeitszeugnis-analyse:verbesserungsvorschlaege-formulieren` | Konkrete Textvorschläge zur Aufwertung von roten und orangen Formulierungen |
| `/arbeitszeugnis-analyse:verhaltensbeurteilung-analyse` | Verhalten zu Vorgesetzten, Kollegen, Kunden; Reihenfolge und Euphemismen |
| `/arbeitszeugnis-analyse:widerspruechliche-bewertungen` | Widersprüche zwischen Leistungs-, Verhaltensteil und Schlussformel |
| `/arbeitszeugnis-analyse:zeugnis-problem-sortieren` | Neuer Einstieg für unsortierte Fragen: Was ist eigentlich das Problem am Zeugnis? |
| `/arbeitszeugnis-analyse:zeugnisart-erkennung` | Qualifiziertes/einfaches Zeugnis, Zwischen-/Endzeugnis, Ausbildungszeugnis |
| `/arbeitszeugnis-analyse:zeugnis-ueberblick-extraktion` | Kopfdaten: Arbeitgeber, Arbeitnehmer, Zeitraum, Position, Unterschrift |
| `/arbeitszeugnis-analyse:zufriedenheitsformel-decodierung` | Fünfstufige Zufriedenheitsformel von Note 1 bis Note 5 |

## Verwendung

Laden Sie das zu analysierende Arbeitszeugnis hoch oder fügen Sie es als Text ein. Starten Sie dann mit dem gewünschten Skill:

```
/arbeitszeugnis-analyse:notenrelevante-saetze-identifizieren

Bitte analysiere das folgende Arbeitszeugnis und identifiziere alle notenrelevanten Sätze mit Ampelzuordnung:

[Zeugnis hier einfügen]
```

Für den vollständigen Mandatsablauf empfiehlt sich die Reihenfolge:
1. `erstgespraech-und-mandatsannahme` — Eingangsbestätigung, Unterlagenanforderung, Erstgespräch
2. `zeugnis-ueberblick-extraktion` — Kopfdaten prüfen
3. `zeugnisart-erkennung` — Zeugnistyp bestimmen
4. `notenrelevante-saetze-identifizieren` — Sätze kategorisieren
5. `steigerungsadverbien-katalog` — Adverbien tabellieren und Notenwirkung bestimmen
6. `satzweise-notenmatrix` — Note eins bis fünf pro Satz mit Themenzuordnung
7. `zufriedenheitsformel-decodierung` — Kernformel decodieren
8. `leistungsbeurteilung-analyse` + `verhaltensbeurteilung-analyse` — Detailanalyse
9. `schlussformel-bewertung` — Schlussformel als Signal und als Rechtsproblem getrennt bewerten
10. `negationen-und-auslassungen-erkennen` — Auslassungen prüfen
11. `negative-codeworte-katalog` — Geheimcodes für Alkohol, Krankheit, Diebstahl, Konflikte, Loyalität prüfen
12. `bereichs-drift-detektor` — Schaufenster-Pattern prüfen
13. `widerspruechliche-bewertungen` — Block-Widersprüche prüfen
14. `ampelsystem-tabellenausgabe` — Gesamttabelle
15. `gesamtnoten-aggregation` — Gesamtnote berechnen, inkl. Drift-Penalty
16. `verbesserungsvorschlaege-formulieren` — Aufwertungs-Rewrites pro Satz
17. `rechtliche-bewertung-bag-rechtsprechung` — rechtliche Einordnung der Befunde
18. `mandantenbericht-zeugnisanalyse` — Ergebnisbericht an den Mandanten mit drei Handlungsoptionen
19. `aufforderungsschreiben-arbeitgeber` — außergerichtliches Berichtigungsverlangen
20. `klage-strategie-zeugnisberichtigung` — bei fruchtlosem Fristablauf zur Klage

## Rechtsgrundlagen

- **Paragraf 109 GewO** — Zeugnisanspruch: Anspruch auf einfaches oder qualifiziertes Zeugnis, Wahrheitspflicht, Wohlwollensgebot
- **Paragraf 16 BBiG** — Zeugnisanspruch für Auszubildende

Kein Ersatz für anwaltliche Beratung. Für die gerichtliche Geltendmachung eines Zeugnisberichtigungsanspruchs ist die Beauftragung eines Rechtsanwalts empfohlen.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`erstgespraech-und-mandatsannahme`](skills/erstgespraech-und-mandatsannahme/SKILL.md), [`erstpruefung-rollenklaerung-mandatsziel`](skills/erstpruefung-rollenklaerung-mandatsziel/SKILL.md), [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste`](skills/arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste/SKILL.md), [`arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk`](skills/arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk/SKILL.md), [`arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen`](skills/arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen/SKILL.md), [`chronologie-und-belegmatrix`](skills/chronologie-und-belegmatrix/SKILL.md), [`drift-quellenkarte`](skills/drift-quellenkarte/SKILL.md), [`satzweise-notenmatrix`](skills/satzweise-notenmatrix/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`arbeitszeugnis-orange-risikoampel-gegenargumente`](skills/arbeitszeugnis-orange-risikoampel-gegenargumente/SKILL.md), [`arbeitszeugnis-zeugnisanalyse-wortlaut-codes`](skills/arbeitszeugnis-zeugnisanalyse-wortlaut-codes/SKILL.md), [`azubi-zeugnis-analyse`](skills/azubi-zeugnis-analyse/SKILL.md), [`fristen-und-risikoampel`](skills/fristen-und-risikoampel/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`leistungsbeurteilung-analyse`](skills/leistungsbeurteilung-analyse/SKILL.md), [`mandantenbericht-zeugnisanalyse`](skills/mandantenbericht-zeugnisanalyse/SKILL.md), [`rechtliche-bewertung-bag-rechtsprechung`](skills/rechtliche-bewertung-bag-rechtsprechung/SKILL.md), [`schlussformel-bewertung`](skills/schlussformel-bewertung/SKILL.md), [`verhaltensbeurteilung-analyse`](skills/verhaltensbeurteilung-analyse/SKILL.md), [`widerspruechliche-bewertungen`](skills/widerspruechliche-bewertungen/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation`](skills/arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation/SKILL.md), [`klage-strategie-zeugnisberichtigung`](skills/klage-strategie-zeugnisberichtigung/SKILL.md), [`steigerungsadverbien-katalog`](skills/steigerungsadverbien-katalog/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine`](skills/arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine/SKILL.md), [`arbeitszeugnis-gruen-behoerden-gerichts-registerweg`](skills/arbeitszeugnis-gruen-behoerden-gerichts-registerweg/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`aufforderungsschreiben-arbeitgeber`](skills/aufforderungsschreiben-arbeitgeber/SKILL.md), [`output-waehlen`](skills/output-waehlen/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`ampelsystem-tabellenausgabe`](skills/ampelsystem-tabellenausgabe/SKILL.md), [`arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung`](skills/arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung/SKILL.md), [`bereichs-drift-detektor`](skills/bereichs-drift-detektor/SKILL.md), [`branchen-spezifische-formulierungen`](skills/branchen-spezifische-formulierungen/SKILL.md), [`geheimcode-katalog`](skills/geheimcode-katalog/SKILL.md), [`gesamtnoten-aggregation`](skills/gesamtnoten-aggregation/SKILL.md), [`gruen-flaggen-katalog`](skills/gruen-flaggen-katalog/SKILL.md), [`leitende-positionen-zeugnisse`](skills/leitende-positionen-zeugnisse/SKILL.md), [`muster-arbeitszeugnis-gemischte-noten`](skills/muster-arbeitszeugnis-gemischte-noten/SKILL.md), [`muster-arbeitszeugnis-mit-roten-flaggen`](skills/muster-arbeitszeugnis-mit-roten-flaggen/SKILL.md), [`muster-arbeitszeugnis-note-1`](skills/muster-arbeitszeugnis-note-1/SKILL.md), [`negationen-und-auslassungen-erkennen`](skills/negationen-und-auslassungen-erkennen/SKILL.md), [`negative-codeworte-katalog`](skills/negative-codeworte-katalog/SKILL.md), [`notenrelevante-saetze-identifizieren`](skills/notenrelevante-saetze-identifizieren/SKILL.md), [`orange-flaggen-katalog`](skills/orange-flaggen-katalog/SKILL.md), [`rote-flaggen-katalog`](skills/rote-flaggen-katalog/SKILL.md), [`verbesserungsvorschlaege-formulieren`](skills/verbesserungsvorschlaege-formulieren/SKILL.md), [`zeugnis-problem-sortieren`](skills/zeugnis-problem-sortieren/SKILL.md), ... plus 3 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 51 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`ampelsystem-tabellenausgabe`](skills/ampelsystem-tabellenausgabe/SKILL.md) | Wenn es um Ampelsystem-Tabellenausgabe in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste`](skills/arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste/SKILL.md) | Wenn es um Ampelsystem: Dokumentenmatrix, Lückenliste und Nachforderung in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk`](skills/arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk/SKILL.md) | Wenn es um Codeworte: Compliance-Dokumentation und Aktenvermerk in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen`](skills/arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen/SKILL.md) | Wenn es um Deutscher: Tatbestandsmerkmale, Beweisfragen und Beleglage in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine`](skills/arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine/SKILL.md) | Wenn es um Geheimcodes: Schriftsatz-, Brief- und Memo-Bausteine in Arbeitszeugnis-Analyse geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitszeugnis-gruen-behoerden-gerichts-registerweg`](skills/arbeitszeugnis-gruen-behoerden-gerichts-registerweg/SKILL.md) | Wenn es um Gruen: Behörden-, Gerichts- oder Registerweg in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung`](skills/arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung/SKILL.md) | Wenn es um Negative: Zahlen, Schwellenwerte und Berechnung in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitszeugnis-orange-risikoampel-gegenargumente`](skills/arbeitszeugnis-orange-risikoampel-gegenargumente/SKILL.md) | Wenn es um Orange: Risikoampel, Gegenargumente und Verteidigungslinien in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation`](skills/arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation/SKILL.md) | Wenn es um Schaufenster: Verhandlung, Vergleich und Eskalation in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitszeugnis-zeugnisanalyse-wortlaut-codes`](skills/arbeitszeugnis-zeugnisanalyse-wortlaut-codes/SKILL.md) | Wenn es um Arbeitszeugnisse: Fristen, Form, Zuständigkeit und Rechtsweg in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`aufforderungsschreiben-arbeitgeber`](skills/aufforderungsschreiben-arbeitgeber/SKILL.md) | Wenn es um Aufforderungsschreiben an den Arbeitgeber in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`azubi-zeugnis-analyse`](skills/azubi-zeugnis-analyse/SKILL.md) | Wenn es um Ausbildungszeugnis-Analyse (Azubi-Zeugnis) in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bereichs-drift-detektor`](skills/bereichs-drift-detektor/SKILL.md) | Wenn es um Bereichs-Drift-Detektor (Schaufenster-Pattern) in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Na... |
| [`branchen-spezifische-formulierungen`](skills/branchen-spezifische-formulierungen/SKILL.md) | Wenn es um Branchenspezifische Formulierungen in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`chronologie-und-belegmatrix`](skills/chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix Arbeitszeugnis in Arbeitszeugnis-Analyse geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`drift-quellenkarte`](skills/drift-quellenkarte/SKILL.md) | Wenn es um Drift Quellenkarte in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`erstgespraech-und-mandatsannahme`](skills/erstgespraech-und-mandatsannahme/SKILL.md) | Wenn es um Erstgespräch und Mandatsannahme im Zeugnisrecht in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`erstpruefung-rollenklaerung-mandatsziel`](skills/erstpruefung-rollenklaerung-mandatsziel/SKILL.md) | Wenn es um Analyse: Erstprüfung, Rollenklärung und Mandatsziel in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fristen-und-risikoampel`](skills/fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel Arbeitszeugnis in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`geheimcode-katalog`](skills/geheimcode-katalog/SKILL.md) | Wenn es um Geheimcode-Katalog der Zeugnissprache in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gesamtnoten-aggregation`](skills/gesamtnoten-aggregation/SKILL.md) | Wenn es um Gesamtnoten-Aggregation in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gruen-flaggen-katalog`](skills/gruen-flaggen-katalog/SKILL.md) | Wenn es um Grünen-Flaggen-Katalog in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Arbeitszeugnis Analyse ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md) | Wenn es um Kaltstart Triage in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`klage-strategie-zeugnisberichtigung`](skills/klage-strategie-zeugnisberichtigung/SKILL.md) | Wenn es um Klagestrategie Zeugnisberichtigung in Arbeitszeugnis-Analyse geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`leistungsbeurteilung-analyse`](skills/leistungsbeurteilung-analyse/SKILL.md) | Wenn es um Leistungsbeurteilung-Analyse in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`leitende-positionen-zeugnisse`](skills/leitende-positionen-zeugnisse/SKILL.md) | Wenn es um Arbeitszeugnisse für leitende Positionen in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mandantenbericht-zeugnisanalyse`](skills/mandantenbericht-zeugnisanalyse/SKILL.md) | Wenn es um Mandantenbericht zur Zeugnisanalyse in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`muster-arbeitszeugnis-gemischte-noten`](skills/muster-arbeitszeugnis-gemischte-noten/SKILL.md) | Wenn es um Muster-Arbeitszeugnis mit gemischten Noten (Schulungsmaterial) in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`muster-arbeitszeugnis-mit-roten-flaggen`](skills/muster-arbeitszeugnis-mit-roten-flaggen/SKILL.md) | Wenn es um Muster-Arbeitszeugnis mit roten Flaggen (Schulungsmaterial) in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`muster-arbeitszeugnis-note-1`](skills/muster-arbeitszeugnis-note-1/SKILL.md) | Wenn es um Muster-Arbeitszeugnis Note 1 (Referenzdokument) in Arbeitszeugnis-Analyse geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`negationen-und-auslassungen-erkennen`](skills/negationen-und-auslassungen-erkennen/SKILL.md) | Wenn es um Negationen und Auslassungen erkennen in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`negative-codeworte-katalog`](skills/negative-codeworte-katalog/SKILL.md) | Wenn es um Negative Codeworte und ihre kodierte Bedeutung in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`notenrelevante-saetze-identifizieren`](skills/notenrelevante-saetze-identifizieren/SKILL.md) | Wenn es um Notenrelevante Sätze identifizieren in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`orange-flaggen-katalog`](skills/orange-flaggen-katalog/SKILL.md) | Wenn es um Orange-Flaggen-Katalog in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Arbeitszeugnis-Analyse geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`rechtliche-bewertung-bag-rechtsprechung`](skills/rechtliche-bewertung-bag-rechtsprechung/SKILL.md) | Wenn es um Rechtliche Bewertung und BAG-Rechtsprechung zum Arbeitszeugnis in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`rote-flaggen-katalog`](skills/rote-flaggen-katalog/SKILL.md) | Wenn es um Rote-Flaggen-Katalog in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`satzweise-notenmatrix`](skills/satzweise-notenmatrix/SKILL.md) | Wenn es um Satzweise Notenmatrix in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schlussformel-bewertung`](skills/schlussformel-bewertung/SKILL.md) | Wenn es um Schlussformel Bewertung in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`steigerungsadverbien-katalog`](skills/steigerungsadverbien-katalog/SKILL.md) | Wenn es um Steigerungsadverbien-Katalog in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verbesserungsvorschlaege-formulieren`](skills/verbesserungsvorschlaege-formulieren/SKILL.md) | Wenn es um Verbesserungsvorschläge formulieren in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verhaltensbeurteilung-analyse`](skills/verhaltensbeurteilung-analyse/SKILL.md) | Wenn es um Verhaltensbeurteilung-Analyse in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`widerspruechliche-bewertungen`](skills/widerspruechliche-bewertungen/SKILL.md) | Wenn es um Widersprüchliche Bewertungen erkennen und kommentieren in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits... |
| [`zeugnis-problem-sortieren`](skills/zeugnis-problem-sortieren/SKILL.md) | Wenn es um Zeugnisproblem Sortieren in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`zeugnis-ueberblick-extraktion`](skills/zeugnis-ueberblick-extraktion/SKILL.md) | Wenn es um Zeugnis-Überblick und Kopfdaten-Extraktion in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`zeugnisart-erkennung`](skills/zeugnisart-erkennung/SKILL.md) | Wenn es um Zeugnisart-Erkennung in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`zufriedenheitsformel-decodierung`](skills/zufriedenheitsformel-decodierung/SKILL.md) | Wenn es um Zufriedenheitsformel-Decodierung in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.

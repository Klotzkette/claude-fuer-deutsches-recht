# Arbeitszeugnis-Analyse (Ampelsystem)


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`arbeitszeugnis-analyse`) | [`arbeitszeugnis-analyse.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnis-analyse.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Arbeitszeugnis-Analyse — aus dem blühenden Leben** (`arbeitszeugnis-analyse-bluehendes-leben`) | [Gesamt-PDF lesen](../testakten/arbeitszeugnis-analyse-bluehendes-leben/gesamt-pdf/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf) | [`testakte-arbeitszeugnis-analyse-bluehendes-leben.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitszeugnis-analyse-bluehendes-leben.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Analyse deutscher Arbeitszeugnisse nach Ampelsystem. Prüft Geheimcodes, Schaufenster-Drift, negative Codeworte, Steigerungsadverbien, Satznoten und Gesamtnotenspanne. Führt vom Erstgespräch über Mandantenbericht und Aufforderungsschreiben bis zur Klagestrategie.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnis-analyse.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnis-analyse.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnis-analyse/arbeitszeugnis-analyse-werkstatt.md" download><code>arbeitszeugnis-analyse-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnis-analyse/arbeitszeugnis-analyse-schnellstart.md" download><code>arbeitszeugnis-analyse-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Arbeitszeugnis-Analyse — aus dem blühenden Leben: [Gesamt-PDF](../testakten/arbeitszeugnis-analyse-bluehendes-leben/gesamt-pdf/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf), [`testakte-arbeitszeugnis-analyse-bluehendes-leben.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitszeugnis-analyse-bluehendes-leben.zip), [`testakte-arbeitszeugnis-analyse-bluehendes-leben-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitszeugnis-analyse-bluehendes-leben-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Kein Ersatz für anwaltliche Beratung. Für die gerichtliche Geltendmachung eines Zeugnisberichtigungsanspruchs ist die Beauftragung eines Rechtsanwalts empfohlen.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `dokumente-intake`, `einstieg-routing`, `erstgespraech-und-mandatsannahme`, `erstpruefung-rollenklaerung-mandatsziel`, `kaltstart-triage` |
| 2. Unterlagen, Sachverhalt und Quellen | `arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste`, `arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk`, `arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen`, `chronologie-und-belegmatrix`, `drift-quellenkarte`, `satzweise-notenmatrix`, `unterlagen-luecken` |
| 3. Prüfung, Anspruch und Subsumtion | `arbeitszeugnis-orange-risikoampel-gegenargumente`, `arbeitszeugnis-zeugnisanalyse-wortlaut-codes`, `azubi-zeugnis-analyse`, `fristen-und-risikoampel`, `leistungsbeurteilung-analyse`, `mandantenbericht-zeugnisanalyse`, `rechtliche-bewertung-bag-rechtsprechung`, `schlussformel-bewertung`, `verhaltensbeurteilung-analyse`, `widerspruechliche-bewertungen` |
| 4. Gestaltung, Strategie und Verhandlung | `arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation`, `klage-strategie-zeugnisberichtigung` |
| 5. Verfahren, Behörde und Gericht | `arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine`, `arbeitszeugnis-gruen-behoerden-gerichts-registerweg` |
| 6. Ergebnis, Schreiben und Kommunikation | `aufforderungsschreiben-arbeitgeber`, `output-waehlen` |
| 8. Spezialmodule und Schnittstellen | `ampelsystem-tabellenausgabe`, `arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung`, `bereichs-drift-detektor`, `branchen-spezifische-formulierungen`, `geheimcode-katalog`, `gesamtnoten-aggregation`, `gruen-flaggen-katalog`, `leitende-positionen-zeugnisse`, `muster-arbeitszeugnis-gemischte-noten`, `muster-arbeitszeugnis-mit-roten-flaggen`, `muster-arbeitszeugnis-note-1`, `negationen-und-auslassungen-erkennen`, `negative-codeworte-katalog`, `notenrelevante-saetze-identifizieren`, `orange-flaggen-katalog`, `rote-flaggen-katalog`, `steigerungsadverbien-katalog`, `verbesserungsvorschlaege-formulieren`, ... plus 4 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ampelsystem-tabellenausgabe` | Wenn es um Ampelsystem-Tabellenausgabe in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste` | Wenn es um Ampelsystem: Dokumentenmatrix, Lückenliste und Nachforderung in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk` | Wenn es um Codeworte: Compliance-Dokumentation und Aktenvermerk in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen` | Wenn es um Deutscher: Tatbestandsmerkmale, Beweisfragen und Beleglage in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine` | Wenn es um Geheimcodes: Schriftsatz-, Brief- und Memo-Bausteine in Arbeitszeugnis-Analyse geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitszeugnis-gruen-behoerden-gerichts-registerweg` | Wenn es um Gruen: Behörden-, Gerichts- oder Registerweg in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung` | Wenn es um Negative: Zahlen, Schwellenwerte und Berechnung in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitszeugnis-orange-risikoampel-gegenargumente` | Wenn es um Orange: Risikoampel, Gegenargumente und Verteidigungslinien in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation` | Wenn es um Schaufenster: Verhandlung, Vergleich und Eskalation in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitszeugnis-zeugnisanalyse-wortlaut-codes` | Wenn es um Arbeitszeugnisse: Fristen, Form, Zuständigkeit und Rechtsweg in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aufforderungsschreiben-arbeitgeber` | Wenn es um Aufforderungsschreiben an den Arbeitgeber in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `azubi-zeugnis-analyse` | Wenn es um Ausbildungszeugnis-Analyse (Azubi-Zeugnis) in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bereichs-drift-detektor` | Wenn es um Bereichs-Drift-Detektor (Schaufenster-Pattern) in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Na... |
| `branchen-spezifische-formulierungen` | Wenn es um Branchenspezifische Formulierungen in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix Arbeitszeugnis in Arbeitszeugnis-Analyse geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `dokumente-intake` | Wenn es um Dokumentenintake in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `drift-quellenkarte` | Wenn es um Drift Quellenkarte in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `einstieg-routing` | Wenn es um Einstieg und Routing in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erstgespraech-und-mandatsannahme` | Wenn es um Erstgespräch und Mandatsannahme im Zeugnisrecht in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erstpruefung-rollenklaerung-mandatsziel` | Wenn es um Analyse: Erstprüfung, Rollenklärung und Mandatsziel in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel Arbeitszeugnis in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `geheimcode-katalog` | Wenn es um Geheimcode-Katalog der Zeugnissprache in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gesamtnoten-aggregation` | Wenn es um Gesamtnoten-Aggregation in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gruen-flaggen-katalog` | Wenn es um Grünen-Flaggen-Katalog in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-triage` | Wenn es um Kaltstart Triage in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `klage-strategie-zeugnisberichtigung` | Wenn es um Klagestrategie Zeugnisberichtigung in Arbeitszeugnis-Analyse geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `leistungsbeurteilung-analyse` | Wenn es um Leistungsbeurteilung-Analyse in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `leitende-positionen-zeugnisse` | Wenn es um Arbeitszeugnisse für leitende Positionen in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mandantenbericht-zeugnisanalyse` | Wenn es um Mandantenbericht zur Zeugnisanalyse in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `muster-arbeitszeugnis-gemischte-noten` | Wenn es um Muster-Arbeitszeugnis mit gemischten Noten (Schulungsmaterial) in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `muster-arbeitszeugnis-mit-roten-flaggen` | Wenn es um Muster-Arbeitszeugnis mit roten Flaggen (Schulungsmaterial) in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `muster-arbeitszeugnis-note-1` | Wenn es um Muster-Arbeitszeugnis Note 1 (Referenzdokument) in Arbeitszeugnis-Analyse geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `negationen-und-auslassungen-erkennen` | Wenn es um Negationen und Auslassungen erkennen in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `negative-codeworte-katalog` | Wenn es um Negative Codeworte und ihre kodierte Bedeutung in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `notenrelevante-saetze-identifizieren` | Wenn es um Notenrelevante Sätze identifizieren in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `orange-flaggen-katalog` | Wenn es um Orange-Flaggen-Katalog in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `output-waehlen` | Wenn es um Output wählen in Arbeitszeugnis-Analyse geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rechtliche-bewertung-bag-rechtsprechung` | Wenn es um Rechtliche Bewertung und BAG-Rechtsprechung zum Arbeitszeugnis in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rote-flaggen-katalog` | Wenn es um Rote-Flaggen-Katalog in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `satzweise-notenmatrix` | Wenn es um Satzweise Notenmatrix in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schlussformel-bewertung` | Wenn es um Schlussformel Bewertung in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `steigerungsadverbien-katalog` | Wenn es um Steigerungsadverbien-Katalog in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verbesserungsvorschlaege-formulieren` | Wenn es um Verbesserungsvorschläge formulieren in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verhaltensbeurteilung-analyse` | Wenn es um Verhaltensbeurteilung-Analyse in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `widerspruechliche-bewertungen` | Wenn es um Widersprüchliche Bewertungen erkennen und kommentieren in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits... |
| `zeugnis-problem-sortieren` | Wenn es um Zeugnisproblem Sortieren in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `zeugnis-ueberblick-extraktion` | Wenn es um Zeugnis-Überblick und Kopfdaten-Extraktion in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zeugnisart-erkennung` | Wenn es um Zeugnisart-Erkennung in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zufriedenheitsformel-decodierung` | Wenn es um Zufriedenheitsformel-Decodierung in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

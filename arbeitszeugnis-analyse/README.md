# Arbeitszeugnis-Analyse (Ampelsystem)

Dieses Plugin analysiert deutsche Arbeitszeugnisse nach dem Ampelsystem (Rot/Orange/Grün). Es decodiert den Geheimcode der deutschen Zeugnissprache, identifiziert notenrelevante Sätze und klassifiziert sie mit vollständiger Interpretation der versteckten Bewertung.

Das Plugin richtet sich an Arbeitnehmer, die ihr eigenes Zeugnis verstehen oder verbessern wollen, an Rechtsanwälte, die Zeugnisstreitigkeiten begleiten, und an Personalverantwortliche, die Zeugnisse professionell ausstellen oder prüfen möchten.

**Hinweis:** Im Repository liegt ergänzend die Testakte `testakten/arbeitszeugnis-analyse-bluehendes-leben/` mit zehn realistisch ausgearbeiteten Zeugnisfällen. Jede Ausgabe ist ein Analyse-Entwurf zur eigenverantwortlichen Prüfung — kein Ersatz für anwaltliche Beratung im Einzelfall.


## ⬇️ Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **arbeitszeugnis analyse bluehendes leben** | [testakte-arbeitszeugnis-analyse-bluehendes-leben.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitszeugnis-analyse-bluehendes-leben.zip) |

Im ZIP sind die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
|---|---|
| Arbeitszeugnis-Analyse (`arbeitszeugnis-analyse`, dieses Plugin) | [arbeitszeugnis-analyse.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnis-analyse.zip) |

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Alle 32 Skills sind sofort verfügbar.

## Ampelsystem

Das Ampelsystem klassifiziert jeden notenrelevanten Satz in drei Kategorien:

| Ampel | Bedeutung | Notentendenz |
|---|---|---|
| **Grün** | Starke positive Formulierung, entspricht dem Geheimcode für Note 1 oder Note 2 | Note 1-2 |
| **Orange** | Schwache positive Formulierung, Note 3, oft durch fehlende Steigerungsadverbien oder Einschränkungen | Note 3 |
| **Rot** | Kodierte Negativaussage, entspricht Note 4 oder Note 5, oft scheinbar positiv formuliert | Note 4-5 |

Rote Signale entstehen durch: das Wort "bemüht", Einschränkungen wie "im Wesentlichen", fehlende positionsnahe Erwartungsbausteine wie Integritäts- oder Führungsverhalten, falsche Reihenfolge bei Personengruppen in der Verhaltensbeurteilung oder eine auffällig kühle Schlussformel. Bei der Schlussformel ist strikt zu trennen: starke Signalwirkung im Bewerbungsverkehr, aber kein automatischer einklagbarer Anspruch auf Dank, Bedauern und Wünsche.

## Enthaltene Skills

Die 32 Skills sind alphabetisch geordnet:

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
| `/arbeitszeugnis-analyse:rechtliche-bewertung-bag-rechtsprechung` | § 109 GewO, BAG-Rechtsprechung, Beweislast, Zeugnisklage |
| `/arbeitszeugnis-analyse:rote-flaggen-katalog` | Klassische Warnsignale: "bemüht", "im Großen und Ganzen", Note 4-5 |
| `/arbeitszeugnis-analyse:satzweise-notenmatrix` | Satz-für-Satz-Notenzuweisung von eins bis fünf mit Themenbereich — Datenbasis für Drift |
| `/arbeitszeugnis-analyse:schlussformel-bewertung` | Bedauern, Dank, Zukunftswünsche — Signalwirkung, Ton und rechtliche Durchsetzbarkeit getrennt |
| `/arbeitszeugnis-analyse:steigerungsadverbien-katalog` | Vollständige Referenzliste der Steigerer mit Notenwirkung — echte, scheinbare und negative Adverbien |
| `/arbeitszeugnis-analyse:verbesserungsvorschlaege-formulieren` | Konkrete Textvorschläge zur Aufwertung von roten und orangen Formulierungen |
| `/arbeitszeugnis-analyse:verhaltensbeurteilung-analyse` | Verhalten zu Vorgesetzten, Kollegen, Kunden; Reihenfolge und Euphemismen |
| `/arbeitszeugnis-analyse:widerspruechliche-bewertungen` | Widersprüche zwischen Leistungs-, Verhaltensteil und Schlussformel |
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

- **§ 109 GewO** — Zeugnisanspruch: Anspruch auf einfaches oder qualifiziertes Zeugnis, Wahrheitspflicht, Wohlwollensgebot
- **§ 16 BBiG** — Zeugnisanspruch für Auszubildende
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Kein Ersatz für anwaltliche Beratung. Für die gerichtliche Geltendmachung eines Zeugnisberichtigungsanspruchs ist die Beauftragung eines Rechtsanwalts empfohlen.

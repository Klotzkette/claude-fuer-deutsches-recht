# Arbeitszeugnis-Analyse (Ampelsystem)

Dieses Plugin analysiert deutsche Arbeitszeugnisse nach dem Ampelsystem (Rot/Orange/Grün). Es decodiert den Geheimcode der deutschen Zeugnissprache, identifiziert notenrelevante Sätze und klassifiziert sie mit vollständiger Interpretation der versteckten Bewertung.

Das Plugin richtet sich an Arbeitnehmer, die ihr eigenes Zeugnis verstehen oder verbessern wollen, an Rechtsanwälte, die Zeugnisstreitigkeiten begleiten, und an Personalverantwortliche, die Zeugnisse professionell ausstellen oder prüfen möchten.

**Hinweis:** Im Repository liegt ergänzend die Testakte `testakten/arbeitszeugnis-analyse-bluehendes-leben/` mit zehn realistisch ausgearbeiteten Zeugnisfällen. Jede Ausgabe ist ein Analyse-Entwurf zur eigenverantwortlichen Prüfung — kein Ersatz für anwaltliche Beratung im Einzelfall.

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Arbeitszeugnis-Analyse — aus dem blühenden Leben** ([`testakten/arbeitszeugnis-analyse-bluehendes-leben/`](../testakten/arbeitszeugnis-analyse-bluehendes-leben/)).

Direkt-Download als ZIP: [testakte-arbeitszeugnis-analyse-bluehendes-leben.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitszeugnis-analyse-bluehendes-leben.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

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

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 32 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Steuerung für das Arbeitszeugnis-Analyse-Plugin. Erkennt Zeugnisart, Ziel, Fristen, Rollen und Streitniveau, schlägt passende Spezial-Skills aus diesem Plugin vor und führt vom ersten Upload bis zu Ma... |
| `ampelsystem-tabellenausgabe` | Erstellt die standardisierte Ampel-Ausgabetabelle für analysierte Arbeitszeugnisse. Anwendungsfall Zeugnisanalyse ist abgeschlossen und Ergebnis soll in einheitlicher Tabelle mit Satz Ampel Bewertung Notentendenz und Begründung dargestel... |
| `aufforderungsschreiben-arbeitgeber` | Außergerichtliches Berichtigungsverlangen an den Arbeitgeber. Aufbau mit Mandatsanzeige, konkreter Beanstandung pro Streitstelle (Wortlaut alt, Wortlaut neu, Begründung mit BAG-Rechtsprechung und Geheimcode-Hinweis), Fristsetzung, Klagea... |
| `azubi-zeugnis-analyse` | Analyse von Ausbildungszeugnissen nach § 16 BBiG bei Zeugnisstreit oder Berichtigungsverlangen. Anwendungsfall Auszubildender hat Ausbildungszeugnis erhalten das er für schlecht haelt. Normen § 16 BBiG Zeugnispflicht § 109 GewO analog. P... |
| `bereichs-drift-detektor` | Erkennt das Schaufenster-Pattern in Arbeitszeugnissen: einzelne Spitzensaetze suggerieren Note eins, waehrend benachbarte Saetze zum selben Themenbereich nur Note drei tragen. Tracked Drift pro Themenbereich (Fachkenntnisse, Arbeitsweise... |
| `branchen-spezifische-formulierungen` | Decodiert branchenspezifische Formulierungen im Arbeitszeugnis zur praezisen Noteneinordnung. Anwendungsfall Zeugnis enthaelt Formulierungen die nur im Kontext einer bestimmten Branche verstaendlich sind. Branchen Vertrieb (Umsatz Zieler... |
| `erstgespraech-und-mandatsannahme` | Mandatsannahme im Zeugnisrecht mit Erstgespraech Unterlagenerfassung und Fristen-Erstprognose. Anwendungsfall Arbeitnehmer erhaelt Zeugnis das er für mangelhaft haelt und sucht anwaltliche Hilfe. Normen § 109 GewO Anspruch auf qualifizie... |
| `geheimcode-katalog` | Zentraler Referenzkatalog aller Standardformulierungen im deutschen Arbeitszeugnis mit Ampelzuordnung. Anwendungsfall Anwalt oder Arbeitnehmer will eine Zeugnisformulierung einordnen und weiss nicht ob sie positiv neutral oder negativ ko... |
| `gesamtnoten-aggregation` | Aggregiert Einzelbewertungen aus Leistungs- Verhaltens- und Schlussformel-Analyse zur Gesamtnote. Anwendungsfall alle Einzelsaetze sind analysiert und eine gewichtete Gesamtnote soll bestimmt werden. Normen § 109 GewO Gesamteindruck BAG-... |
| `gruen-flaggen-katalog` | Katalog starker positiver Formulierungen im Arbeitszeugnis, die auf Note 1 oder Note 2 hindeuten. Umfasst Superlative, vollständige Zufriedenheitsformeln und alle grünen Ampelsignale mit Notentendenz und Begründung. |
| `klage-strategie-zeugnisberichtigung` | Strategie und Antragsformulierungen für die Zeugnisberichtigungsklage vor dem Arbeitsgericht. Anwendungsfall außergerichtliches Berichtigungsverlangen ist gescheitert und Klage soll eingereicht werden. Normen § 109 GewO Berichtigungsansp... |
| `leistungsbeurteilung-analyse` | Analysiert Sätze zur Arbeitsqualität, Arbeitsbereitschaft, Arbeitsweise, Arbeitstempo und Belastbarkeit im Arbeitszeugnis. Decodiert Formulierungen wie 'stets sorgfältig', 'bemüht' oder 'im Wesentlichen' und ordnet sie dem Ampelsystem zu. |
| `leitende-positionen-zeugnisse` | Analyse von Arbeitszeugnissen für Führungskräfte und leitende Angestellte. Besondere Formulierungen zu Mitarbeiterführung, Personalentwicklung, strategischer Verantwortung und Repräsentation. Fehlende Führungsbausteine als Ampelsignale. |
| `mandantenbericht-zeugnisanalyse` | Schriftlicher Ergebnisbericht an den Arbeitnehmer nach abgeschlossener Ampelanalyse. Strukturierter Aufbau in Gesamtnote, Befund pro Themenbereich, kritische Geheimcodes und Drift-Stellen, rechtliche Einordnung, Erfolgsaussichten, drei H... |
| `muster-arbeitszeugnis-gemischte-noten` | Anonymisiertes Schulungszeugnis mit Schaufenster-Pattern für Training und Demonstration. Anwendungsfall Rechtsanwalt oder Mitarbeiter will Zeugnisanalyse-Skills an einem Musterfall trainieren. Zeigt klassisches Drift-Muster einzelne Saet... |
| `muster-arbeitszeugnis-mit-roten-flaggen` | Anonymisiertes Beispielzeugnis mit roten orangen und gruenen Bewertungen als Schulungsmaterial. Anwendungsfall Training für Zeugnissprache und Geheimcode-Erkennung. Enthalt gemischte Ampelsignale mit vollständiger Analysetabelle. Output... |
| `muster-arbeitszeugnis-note-1` | Vollständiges Musterarbeitszeugnis Note 1 als Referenzdokument für Vergleich und Berichtigung. Anwendungsfall Anwalt oder Mandant will wissen wie ein optimales Zeugnis aussieht. Alle Kernbausteine in grüner Formulierung: Kopfdaten, Aufga... |
| `negationen-und-auslassungen-erkennen` | Erkennt fehlende Pflichtaussagen im Arbeitszeugnis: Was nicht gesagt wird, ist oft entscheidend. Prüft Checkliste auf fehlende Loyalität, Ehrlichkeit, Pünktlichkeit und andere Standardaussagen und bewertet Auslassungen nach Ampelsystem. |
| `negative-codeworte-katalog` | Erweiterter Katalog negativer Codeworte und ihrer kodierten Bedeutung. Erfasst die thematischen Cluster Alkohol und Suchtmittel, Krankheitshaeufung, Konflikte, Diebstahl und Vertrauensbruch, mangelnde Loyalitaet, schwierige Persoenlichke... |
| `notenrelevante-saetze-identifizieren` | Identifiziert notenrelevante Saetze im Arbeitszeugnis und trennt sie von neutralen Aufgabenbeschreibungen. Anwendungsfall Zeugnis liegt vor und muss für Ampelanalyse vorbereitet werden. Normen § 109 GewO Inhalte eines qualifizierten Zeug... |
| `orange-flaggen-katalog` | Katalog schwacher positiver Formulierungen im Arbeitszeugnis, die auf Note 3 hindeuten. Umfasst alle Orange-Signale: fehlende Steigerungsadverbien, eingeschränkte Lobesformeln und strukturelle Abschwächungen mit Notentendenz Note 3. |
| `rechtliche-bewertung-bag-rechtsprechung` | Rechtliche Einordnung von Zeugnisansprüchen nach § 109 GewO und BAG-Rechtsprechung für die anwaltliche Praxis. Anwendungsfall Anwalt benoetigt Beweislastverteilung und Rechtsgrundlagen für Zeugnisstreit oder Klagebegründung. Normen § 109... |
| `rote-flaggen-katalog` | Katalog klassischer roter Warnsignale im deutschen Arbeitszeugnis: Formulierungen, die trotz positiv klingendem Wortlaut eine schlechte Beurteilung kodieren. Umfasst alle Note-4- und Note-5-Signale mit Erklärung und Alternativformulierun... |
| `satzweise-notenmatrix` | Bewertet jeden notenrelevanten Satz eines Arbeitszeugnisses mit Schulnote 1 bis 5. Anwendungsfall notenrelevante Saetze wurden identifiziert und sollen systematisch bewertet werden. Normen § 109 GewO Bewertungsmassstab BAG-Linie zur Zeug... |
| `schlussformel-bewertung` | Workflow-Skill zu schlussformel bewertung. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `steigerungsadverbien-katalog` | Vollständige Referenzliste aller Steigerungsadverbien der Zeugnissprache mit Notenwert. Ein Adverb fehlt, eine Note faellt. Trennt echte Steigerer (stets, jederzeit, vollkommen, hoechst) von scheinbaren Steigerern (regelmäßig, ueberwiege... |
| `verbesserungsvorschlaege-formulieren` | Formuliert konkrete Verbesserungsvorschläge für orange und rote Zeugnissätze. Zeigt, wie aus einer Note-4-Formulierung eine Note-2-Formulierung wird — mit Gegenüberstellung Original/Vorschlag und Begründung der sprachlichen Änderung. |
| `verhaltensbeurteilung-analyse` | Analysiert Verhaltensbeurteilungen im Arbeitszeugnis: Verhalten zu Vorgesetzten, Kollegen und Kunden. Decodiert die Reihenfolge der Genannten, Qualifikationswörter und die Bedeutung von Auslassungen als versteckte Signale. |
| `widerspruechliche-bewertungen` | Erkennt und kommentiert Widersprüche im Arbeitszeugnis: wenn Leistungsteil grün, aber Schlussformel rot ist, oder wenn Einzelsätze sich inhaltlich ausschließen. Erklärt die Signalwirkung von Widersprüchen auf potenzielle neue Arbeitgeber. |
| `zeugnis-ueberblick-extraktion` | Extrahiert Kopfdaten aus deutschen Arbeitszeugnissen für Mandatsanlage und Analysestart. Anwendungsfall Zeugnis wurde hochgeladen und Basisdaten sollen für Akte und Analyse erfasst werden. Normen § 109 GewO Pflichtinhalt § 16 BBiG Ausbil... |
| `zeugnisart-erkennung` | Unterscheidet qualifiziertes Endzeugnis einfaches Zeugnis Zwischenzeugnis und Ausbildungszeugnis am Beginn jeder Analyse. Anwendungsfall Zeugnis liegt vor und muss bevor Analyse startet der richtigen Zeugnisart zugeordnet werden. Normen... |
| `zufriedenheitsformel-decodierung` | Decodiert die fünfstufige Zufriedenheitsformel deutscher Arbeitszeugnisse: von Note 1 bis Note 5. Tabellarische Ampelzuordnung aller Standardformulierungen mit Erklärung der sprachlichen Feinheiten und ihrer rechtlichen Bedeutung. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

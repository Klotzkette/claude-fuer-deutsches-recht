# Arbeitszeugnis-Analyse (Ampelsystem)

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`arbeitszeugnis-analyse`) | [`arbeitszeugnis-analyse.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnis-analyse.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Arbeitszeugnis-Analyse — aus dem blühenden Leben** (`arbeitszeugnis-analyse-bluehendes-leben`) | [Gesamt-PDF lesen](../testakten/arbeitszeugnis-analyse-bluehendes-leben/gesamt-pdf/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf) | [`testakte-arbeitszeugnis-analyse-bluehendes-leben.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitszeugnis-analyse-bluehendes-leben.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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
| `/arbeitszeugnis-analyse:rechtliche-bewertung-bag-rechtsprechung` | § 109 GewO, BAG-Rechtsprechung, Beweislast, Zeugnisklage |
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

- **§ 109 GewO** — Zeugnisanspruch: Anspruch auf einfaches oder qualifiziertes Zeugnis, Wahrheitspflicht, Wohlwollensgebot
- **§ 16 BBiG** — Zeugnisanspruch für Auszubildende
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Kein Ersatz für anwaltliche Beratung. Für die gerichtliche Geltendmachung eines Zeugnisberichtigungsanspruchs ist die Beauftragung eines Rechtsanwalts empfohlen.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ampelsystem-tabellenausgabe` | Erstellt die standardisierte Ampel-Ausgabetabelle für analysierte Arbeitszeugnisse. Anwendungsfall Zeugnisanalyse ist abgeschlossen und Ergebnis soll in einheitlicher Tabelle mit Satz Ampel Bewertung Notentendenz und Begründung dargestel... |
| `arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste` | Ampelsystem: Dokumentenmatrix, Lückenliste und Nachforderung im Arbeitszeugnisrecht: fachlich vertiefter Fachmodul mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk` | Codeworte: Compliance-Dokumentation und Aktenvermerk im Arbeitszeugnisrecht: fachlich vertiefter Fachmodul mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nu... |
| `arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen` | Deutscher: Tatbestandsmerkmale, Beweisfragen und Beleglage im Arbeitszeugnisrecht: fachlich vertiefter Fachmodul mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und dir... |
| `arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine` | Geheimcodes: Schriftsatz-, Brief- und Memo-Bausteine im Arbeitszeugnisrecht: fachlich vertiefter Fachmodul mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nu... |
| `arbeitszeugnis-gruen-behoerden-gerichts-registerweg` | Gruen: Behörden-, Gerichts- oder Registerweg im Arbeitszeugnisrecht: fachlich vertiefter Fachmodul mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem... |
| `arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung` | Negative: Zahlen, Schwellenwerte und Berechnung im Arbeitszeugnisrecht: fachlich vertiefter Fachmodul mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbar... |
| `arbeitszeugnis-orange-risikoampel-gegenargumente` | Orange: Risikoampel, Gegenargumente und Verteidigungslinien im Arbeitszeugnisrecht: fachlich vertiefter Fachmodul mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und di... |
| `arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation` | Schaufenster: Verhandlung, Vergleich und Eskalation im Arbeitszeugnisrecht: fachlich vertiefter Fachmodul mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nut... |
| `arbeitszeugnis-zeugnisanalyse-wortlaut-codes` | Arbeitszeugnisse: Fristen, Form, Zuständigkeit und Rechtsweg im Arbeitszeugnisrecht: fachlich vertiefter Fachmodul mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `aufforderungsschreiben-arbeitgeber` | Außergerichtliches Berichtigungsverlangen an den Arbeitgeber. Aufbau mit Mandatsanzeige, konkreter Beanstandung pro Streitstelle (Wortlaut alt, Wortlaut neu, Begründung mit BAG-Rechtsprechung und Geheimcode-Hinweis), Fristsetzung, Klagea... |
| `azubi-zeugnis-analyse` | Analyse von Ausbildungszeugnissen nach § 16 BBiG bei Zeugnisstreit oder Berichtigungsverlangen. Anwendungsfall Auszubildender hat Ausbildungszeugnis erhalten das er für schlecht haelt. Normen § 16 BBiG Zeugnispflicht § 109 GewO analog. P... |
| `bereichs-drift-detektor` | Erkennt das Schaufenster-Pattern in Arbeitszeugnissen: einzelne Spitzensaetze suggerieren Note eins, waehrend benachbarte Saetze zum selben Themenbereich nur Note drei tragen. Tracked Drift pro Themenbereich (Fachkenntnisse, Arbeitsweise... |
| `branchen-spezifische-formulierungen` | Decodiert branchenspezifische Formulierungen im Arbeitszeugnis zur praezisen Noteneinordnung. Anwendungsfall Zeugnis enthaelt Formulierungen die nur im Kontext einer bestimmten Branche verstaendlich sind. Branchen Vertrieb (Umsatz Zieler... |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin Arbeitszeugnis Analyse im Arbeitszeugnis-Analyse. |
| `dokumente-intake` | Dokumentenintake für Arbeitszeugnis-Analyse: sortiert Erstes Zeugnis, Berichtigungszeugnis, Zwischenzeugnis, prüft Datum, Absender, Frist und Beweiswert (Leistungsbeurteilungen, E-Mail-Verkehr HR); markiert Lücken; berücksichtigt Mandats... |
| `drift-quellenkarte` | Drift Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `einstieg-routing` | Einstieg, Triage und Routing für Arbeitszeugnis-Analyse: ordnet Rolle (Mandant/Arbeitnehmer, Arbeitgeber/HR, Vorgesetzte), markiert Frist (BAG 5.7.2018 – 9 AZR 244/17 Anspruch entstehung), wählt Norm (§ 109 GewO Wohlwollensgrundsatz, § 1... |
| `erstgespraech-und-mandatsannahme` | Mandatsannahme im Zeugnisrecht mit Erstgespraech Unterlagenerfassung und Fristen-Erstprognose. Anwendungsfall Arbeitnehmer erhaelt Zeugnis das er für mangelhaft haelt und sucht anwaltliche Hilfe. Normen § 109 GewO Anspruch auf qualifizie... |
| `erstpruefung-rollenklaerung-mandatsziel` | Analyse: Erstprüfung, Rollenklärung und Mandatsziel im Arbeitszeugnisrecht: fachlich vertiefter Fachmodul mit Normenradar (GewO/BGB/AGG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nut... |
| `fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin Arbeitszeugnis Analyse im Arbeitszeugnis-Analyse. |
| `geheimcode-katalog` | Zentraler Referenzkatalog aller Standardformulierungen im deutschen Arbeitszeugnis mit Ampelzuordnung. Anwendungsfall Anwalt oder Arbeitnehmer will eine Zeugnisformulierung einordnen und weiss nicht ob sie positiv neutral oder negativ ko... |
| `gesamtnoten-aggregation` | Aggregiert Einzelbewertungen aus Leistungs- Verhaltens- und Schlussformel-Analyse zur Gesamtnote. Anwendungsfall alle Einzelsaetze sind analysiert und eine gewichtete Gesamtnote soll bestimmt werden. Normen § 109 GewO Gesamteindruck BAG-... |
| `gruen-flaggen-katalog` | Katalog starker positiver Formulierungen im Arbeitszeugnis, die auf Note 1 oder Note 2 hindeuten. Umfasst Superlative, vollständige Zufriedenheitsformeln und alle grünen Ampelsignale mit Notentendenz und Begründung. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Workflow-Steuerung für das Arbeitszeugnis-Analyse-Plugin. Erkennt Zeugnisart, Ziel, Fristen, Rollen und Streitniveau, schlägt passende Fachmodule aus diesem Plugin vor und führt vom ersten Upload bis zu Mandan... |
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
| `output-waehlen` | Output-Wahl für Arbeitszeugnis-Analyse: stimmt Adressat (Mandant/Arbeitnehmer, Arbeitgeber/HR, Vorgesetzte), Frist (BAG 5.7.2018 – 9 AZR 244/17 Anspruch entstehung) und Form auf den Zweck ab — typische Outputs: Notenmatrix, Geheimcode-Be... |
| `rechtliche-bewertung-bag-rechtsprechung` | Rechtliche Einordnung von Zeugnisansprüchen nach § 109 GewO und BAG-Rechtsprechung für die anwaltliche Praxis. Anwendungsfall Anwalt benoetigt Beweislastverteilung und Rechtsgrundlagen für Zeugnisstreit oder Klagebegründung. Normen § 109... |
| `rote-flaggen-katalog` | Katalog klassischer roter Warnsignale im deutschen Arbeitszeugnis: Formulierungen, die trotz positiv klingendem Wortlaut eine schlechte Beurteilung kodieren. Umfasst alle Note-4- und Note-5-Signale mit Erklärung und Alternativformulierun... |
| `satzweise-notenmatrix` | Bewertet jeden notenrelevanten Satz eines Arbeitszeugnisses mit Schulnote 1 bis 5. Anwendungsfall notenrelevante Saetze wurden identifiziert und sollen systematisch bewertet werden. Normen § 109 GewO Bewertungsmassstab BAG-Linie zur Zeug... |
| `schlussformel-bewertung` | Prüfungslinie für schlussformel bewertung im Arbeitszeugnis-Analyse. |
| `steigerungsadverbien-katalog` | Vollständige Referenzliste aller Steigerungsadverbien der Zeugnissprache mit Notenwert. Ein Adverb fehlt, eine Note faellt. Trennt echte Steigerer (stets, jederzeit, vollkommen, hoechst) von scheinbaren Steigerern (regelmäßig, ueberwiege... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Arbeitszeugnis-Analyse: trennt fehlende Tatsachen von fehlenden Belegen (Erstes Zeugnis, Berichtigungszeugnis, Zwischenzeugnis), nennt pro Lücke Beweisthema, Beschaffungsweg (Arbeitsgericht), Frist und E... |
| `verbesserungsvorschlaege-formulieren` | Formuliert konkrete Verbesserungsvorschläge für orange und rote Zeugnissätze. Zeigt, wie aus einer Note-4-Formulierung eine Note-2-Formulierung wird — mit Gegenüberstellung Original/Vorschlag und Begründung der sprachlichen Änderung. |
| `verhaltensbeurteilung-analyse` | Analysiert Verhaltensbeurteilungen im Arbeitszeugnis: Verhalten zu Vorgesetzten, Kollegen und Kunden. Decodiert die Reihenfolge der Genannten, Qualifikationswörter und die Bedeutung von Auslassungen als versteckte Signale. |
| `widerspruechliche-bewertungen` | Erkennt und kommentiert Widersprüche im Arbeitszeugnis: wenn Leistungsteil grün, aber Schlussformel rot ist, oder wenn Einzelsätze sich inhaltlich ausschließen. Erklärt die Signalwirkung von Widersprüchen auf potenzielle neue Arbeitgeber. |
| `zeugnis-problem-sortieren` | Allgemeiner Startskill für Arbeitszeugnisse, wenn der Nutzer nur ein komisches Gefuehl, ein PDF, einen Screenshot oder eine unsortierte Frage hat. Klaert Problem, Zeugnisart, Ziel, Frist, Kontext, Belege und naechsten Arbeitsweg. |
| `zeugnis-ueberblick-extraktion` | Extrahiert Kopfdaten aus deutschen Arbeitszeugnissen für Mandatsanlage und Analysestart. Anwendungsfall Zeugnis wurde hochgeladen und Basisdaten sollen für Akte und Analyse erfasst werden. Normen § 109 GewO Pflichtinhalt § 16 BBiG Ausbil... |
| `zeugnisart-erkennung` | Unterscheidet qualifiziertes Endzeugnis einfaches Zeugnis Zwischenzeugnis und Ausbildungszeugnis am Beginn jeder Analyse. Anwendungsfall Zeugnis liegt vor und muss bevor Analyse startet der richtigen Zeugnisart zugeordnet werden. Normen... |
| `zufriedenheitsformel-decodierung` | Decodiert die fünfstufige Zufriedenheitsformel deutscher Arbeitszeugnisse: von Note 1 bis Note 5. Tabellarische Ampelzuordnung aller Standardformulierungen mit Erklärung der sprachlichen Feinheiten und ihrer rechtlichen Bedeutung. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

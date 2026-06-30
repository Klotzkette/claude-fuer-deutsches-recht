# Arbeitszeugnisgenerator

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Erstellt deutsche Arbeitszeugnisse Schritt für Schritt: Rolle, Stammdaten, Tätigkeiten, Leistungs- und Verhaltensbewertung, Notenwahl per Ampelsystem, Schlussformeln. Wahlweise vorgegebene Note oder geführte Einschätzung. Mehrere Harnesses: qualifiziert, einfach, Ausbildung.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnisgenerator.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnisgenerator/arbeitszeugnisgenerator-werkstatt.md" download><code>arbeitszeugnisgenerator-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnisgenerator/arbeitszeugnisgenerator-schnellstart.md" download><code>arbeitszeugnisgenerator-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`arbeitszeugnisgenerator-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator-testakte.zip), [`arbeitszeugnisgenerator-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein deutsches Arbeitszeugnis Schritt für Schritt erstellen — rechtssicher, mit korrekter Zeugnissprache, in der gewünschten Notenstufe.

## Wenn du das brauchst

- **Personalabteilung** muss für einen ausscheidenden Mitarbeiter ein qualifiziertes Arbeitszeugnis erstellen und braucht passende Formeln zur Wunschnote.
- **Geschäftsführer einer kleinen Firma** schreibt zum ersten Mal ein Arbeitszeugnis und will nicht versehentlich Geheimcodes einbauen, die die Note kippen.
- **Arbeitnehmer** möchte einen sauberen Vorschlag für das Wunschzeugnis erstellen und der HR-Abteilung vorlegen.
- **Auszubildender oder Ausbilder** braucht ein Ausbildungszeugnis nach Paragraf 16 BBiG.

## Was du am Ende in der Hand hast

Ein vollständiges Arbeitszeugnis im richtigen Format — qualifiziertes Zeugnis, einfaches Zeugnis, Zwischenzeugnis oder Ausbildungszeugnis — mit Kopfdaten, Tätigkeitsbeschreibung, Leistungs- und Verhaltensbewertung in der Wunschnote, Schlussformel und Beendigungsgrund. Auf Wunsch mit Begründung pro Satz, welche Notenwirkung er entfaltet.

## Der Weg dorthin

Rolle und Anliegen klären → Zeugnisart und Harness wählen → Stammdaten erfassen → Tätigkeiten erheben → Notenwahl (vorgeben oder durch Fragen ermitteln lassen) → satzweise Generierung mit Ampel-Vorschau → Schlussformel und Beendigungsgrund → Revision und Feinschliff.

## Workflows

Drei Modi zur Wahl:

- **Direkt-Modus**: Du gibst die Wunschnote pro Bewertungsfeld vor (Leistung, Verhalten, Führung). Der Generator setzt die passenden Formeln.
- **Geführter Modus**: Der Generator stellt gezielte Fragen zu Leistung, Engagement, Verhalten — und schlägt am Ende eine Note vor ("das klingt nach Note 2 bis 3, soll ich so schreiben?"). Du bestätigst oder korrigierst.
- **Hybrid-Modus**: Du gibst die Gesamtnote vor, der Generator fragt nur noch die offenen Details ab (typische Tätigkeiten, besondere Projekte, Beendigungsgrund).

## Was dich aufhält

- **Wohlwollensgrundsatz versus Wahrheitspflicht**: Beides muss eingehalten werden, kein Schönschreiben um den Preis der Wahrheit.
- **Geheimcodes**: Versehentlich eingebaute Negativcodes ("bemüht sich", "im Großen und Ganzen", "lernte schnell kennen und schätzen") kippen die Note. Der Generator vermeidet sie aktiv.
- **Zeugnisklarheit (objektiver Empfängerhorizont, BAG 9 AZR 352.04)**: Keine doppelten Böden, keine widersprüchlichen Aussagen.
- **Äußere Form**: Briefkopf, Datum, Unterschrift, kein Knick, keine Streichungen.
- **Schlussformel-Wirkung**: Schlussformeln wirken oft stärker als die Bewertungssätze. Eine schwache Schlussformel zieht die Gesamtnote.

## Rechtlicher Anker

- Paragraf 109 GewO (Zeugnisanspruch)
- Paragraf 16 BBiG (Ausbildungszeugnis)
- Paragrafen 241 Absatz 2, 280 Absatz 1 BGB (Nebenpflicht und Schadensersatz)
- BAG-Leitentscheidungen zu Notenstufen, Beweislast, Schlussformel und Zeugnisklarheit (im Werkstatt-Prompt ausführlich)

## KI-Verordnung: mögliche Einstufung als Hochrisiko-KI

Wird dieses Plugin im Personalwesen produktiv eingesetzt, kann es ein Hochrisiko-KI-System nach Artikel 6 Absatz 2 in Verbindung mit Anhang III Nummer 4 Buchstabe b der Verordnung (EU) 2024/1689 (KI-Verordnung) sein. Anhang III Nummer 4 Buchstabe b erfasst KI-Systeme, die bestimmungsgemäß für Entscheidungen über die Bedingungen von Arbeitsverhältnissen, für die Bewertung der Arbeitsleistung und des Arbeitsverhaltens oder für vergleichbare Personalentscheidungen verwendet werden. Ein automatisiert erstelltes Arbeitszeugnis betrifft genau diese Bewertungs- und Bedingungsdimension. Anhang III Nummer 4 Buchstabe a erfasst dagegen die Personalauswahl und Bewerbungsphase und greift hier in der Regel nicht.

Folgen einer Einstufung als Hochrisiko-KI können sein: Pflicht zu menschlicher Aufsicht, Dokumentations- und Transparenzpflichten, Risikomanagement, Information der Beschäftigten beziehungsweise des Betriebsrats und gegebenenfalls eine Grundrechte-Folgenabschätzung. Die genaue Reichweite hängt vom Einsatzkontext, von der Rolle als Anbieter oder Betreiber und vom Geltungsbeginn nach Artikel 113 KI-VO ab. Diese Hinweise sind keine Rechtsberatung; im Zweifel ist eine arbeitsrechtliche und KI-rechtliche Bewertung im Einzelfall geboten.

## Hinweise

Generischer Entwurfsstand, alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer prüft den generierten Text auf Plausibilität und Eignung im konkreten Einzelfall. Keine Rechtsberatung. Keine Garantie für Vollständigkeit oder Aktualität der Rechtsprechung. Bei streitigen Fällen Fachanwalt für Arbeitsrecht hinzuziehen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 40 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `auslassungen-vermeiden` | Schweigen als Negativcode im Zeugnis erkennen und vermeiden. Fehlende Pflichtaussagen für eine Position sind eigenständige Berichtigungspunkte. Enthält eine vollständige Tabelle der positionsabhängigen Pflichtaussagen und erklärt, was da... |
| `bag-leitentscheidungen-beweislast` | Die BAG-Leitentscheidungen zur Beweislast im Zeugnisstreit. BAG 9 AZR 12.03 und BAG 9 AZR 584.13 als Kernnormen. Note 3 ist Ausgangspunkt: besser als Note 3 = Beweislast Arbeitnehmer; schlechter als Note 3 = Beweislast Arbeitgeber. Branc... |
| `bag-leitentscheidungen-notenstufen` | Die BAG-Leitentscheidungen zur Notenstufenmatrix im Arbeitszeugnis. Kernentscheidung: BAG, Urteil v. 15.11.2011 – 9 AZR 386.10 (Formulierungsspielraum, Grenzen Zeugniswahrheit/Klarheit). BAG, Urteil v. 14.10.2003 – 9 AZR 12.03 (Note 3 al... |
| `beendigungsgrund-formulieren` | Formulierungskatalog für den Beendigungssatz im Zeugnis. Der Beendigungsgrund (Eigenkündigung, Arbeitgeberkündigung, Aufhebungsvertrag, Befristungsende, betriebsbedingte Kündigung) beeinflusst die Schlussformel und den Gesamteindruck. En... |
| `belastbarkeit-formeln` | Formulierungskatalog für Belastbarkeitsaussagen im Zeugnis. Belastbarkeit ist bei stressrelevanten Positionen eine Pflichtaussage — fehlt sie, wird Belastbarkeitsdefizit impliziert. Enthält Formeln für alle Noten sowie Hinweise auf Formu... |
| `besondere-leistungen-projekte` | Formulierungsregeln für die Darstellung besonderer Leistungen, herausragender Projekte, Auszeichnungen und messbarer Erfolge im Zeugnis. Besondere Leistungen verstärken die Hauptformel und sind das stärkste Positivsignal. Sie müssen wahr... |
| `compliance-integritaet-formeln` | Formulierungskatalog für Aussagen zu Compliance, Integrität, Vertrauenswürdigkeit und Loyalität. Bei Kassenpositionen, Finanzverantwortung und Führungsrollen sind Integritätsaussagen Pflicht — fehlen sie, entsteht ein Vertrauensproblem-S... |
| `drift-und-schaufenster-vermeiden` | Erklärt das Schaufenster-Drift-Problem: Ein langer, positiver Aufgabenkatalog oder einzelne Spitzensätze stehen neben einer schwachen Gesamtnote oder einzelnen abgewerteten Bereichen. Der Generator muss Konsistenz sicherstellen. Enthält... |
| `einfuehrung-mandantenanliegen` | Klärt zu Beginn jeder Generator-Sitzung, wer das Zeugnis benötigt und aus welchem Anlass. Unterscheidet Arbeitgeber-/HR-Seite (Zeugnis ausstellen) von Arbeitnehmer-Seite (Zeugnis erhalten wollen oder prüfen lassen). Legt die Perspektive... |
| `engagement-motivation-formeln` | Formulierungskatalog für Engagement- und Motivationsaussagen im Zeugnis. Enthält Formeln für alle Noten, Abgrenzung zwischen echter Motivation und Mitläufertum-Signalen sowie eine Liste von Formulierungen, die ungewollt Passivität oder O... |
| `frequenzadverbien-katalog` | Katalog der Frequenzadverbien der deutschen Zeugnissprache mit ihrer Notenwirkung. Frequenzadverbien (oft, meist, häufig, gelegentlich, bisweilen) drücken Häufigkeit aus, keine Qualität — sie sind keine echten Steigerer. Wer 'oft' statt... |
| `fuehrungskraft-bewertung` | Formulierungskatalog für den Führungsabschnitt in Zeugnissen von Personen mit Leitungsfunktion. Führungszeugnisse haben fünf zusätzliche Pflichtbausteine. Das Fehlen des Führungsabschnitts ist ein eigenständiger Berichtigungspunkt. Enthä... |
| `geheimcodes-vermeiden` | Vollständiger Katalog der Negativcodes der deutschen Zeugnissprache, die der Generator unter keinen Umständen produzieren darf. Unterteilt nach Themen: Suchtmittel-Lesarten, Krankheit/Fehlzeiten, Vertrauensbruch, Konflikte, Loyalität, Be... |
| `kopfdaten-und-aussere-form` | Prüfraster und Generierregeln für Briefkopf, Datum, Unterschrift und äußere Form des Arbeitszeugnisses. Fehlerhafte Formalia sind eigenständige Berichtigungspunkte. Enthält die Anforderungen aus BAG (9 AZR 893/98) zur Unterschrift, das F... |
| `langzeit-arbeitsverhaeltnis` | Besonderheiten bei Zeugnissen nach langer Beschäftigungsdauer (zehn Jahre und mehr). Langjährige Beschäftigung erfordert besondere Gewichtung von Loyalität, Unternehmensentwicklung, Kompetenzentwicklung und Bindungsformel. Eine kurze, ka... |
| `mehrere-positionen-im-zeugnis` | Regeln für Zeugnisse, in denen die Person mehrere Positionen innehatte: Beförderungen, Versetzungen, Positionswechsel. Jede Position wird mit Zeitraum und Aufgaben genannt. Die Leistungsnote bezieht sich auf die gesamte Beschäftigungszei... |
| `note-1-formeln-leistung` | Vollständiger Formulierungskatalog für Leistungsaussagen der Note 1 (sehr gut). Enthält Hauptformel, Verstärker-Adverbien, Einzelsatz-Varianten für Fachkenntnisse, Arbeitsweise, Ergebnisse, Engagement und Belastbarkeit. Alle Formeln sind... |
| `note-2-formeln-leistung` | Vollständiger Formulierungskatalog für Leistungsaussagen der Note 2 (gut). Enthält Hauptformel, Standardsteigerer, Einzelsatz-Varianten für alle Bewertungsachsen. Note 2 setzt 'stets' vor 'volle Zufriedenheit' voraus — fehlt das Adverb,... |
| `note-3-formeln-leistung` | Vollständiger Formulierungskatalog für Leistungsaussagen der Note 3 (befriedigend). Hauptformel 'zur vollen Zufriedenheit' ohne 'stets'. Note 3 ist nach BAG (9 AZR 12/03) der gesetzliche Ausgangspunkt der Bewertungsskala. Wer besser als... |
| `note-4-formeln-leistung` | Formulierungskatalog für Leistungsaussagen der Note 4 (ausreichend). Hauptformel 'zur Zufriedenheit' ohne Steigerer. Note 4 ist rechtlich riskant: der Arbeitgeber trägt die Darlegungs- und Beweislast. Generator weist zwingend auf dieses... |
| `note-5-formeln-leistung` | Formulierungskatalog für Leistungsaussagen der Note 5 (mangelhaft). Hauptformel 'im Großen und Ganzen zur Zufriedenheit'. Note 5 ist die schärfste reguläre Bewertung in der deutschen Zeugnissprache und nur bei schwerwiegenden, nachgewies... |
| `notenwahl-modus` | Steuert, auf welchem Weg die Leistungsnote bestimmt wird: direkte Vorgabe durch den Nutzer oder interaktive Ermittlung über gezielte Fragen zu Leistung und Verhalten. Im Vorgabe-Modus übernimmt der Generator die Note und wählt passende F... |
| `rechtlicher-anker-109-gewo` | Vollständiger Rechtsanker für den Arbeitszeugnis-Generator: Paragraf 109 GewO, Paragraf 16 BBiG, Paragraf 241 Abs. 2 BGB, Paragraf 280 Abs. 1 BGB und zuständiges Gericht. Beschreibt die Rechtslage zur elektronischen Form seit dem Vierten... |
| `revision-und-aenderungswuensche` | Workflow für Änderungswünsche nach dem ersten Zeugnisgenerierlauf. Der Nutzer möchte einzelne Sätze ändern, eine Note anpassen oder Abschnitte ergänzen. Enthält Regeln für konsistente Nachbearbeitung: Notenanpassung zieht Formulierungsan... |
| `rollen-und-harness-wahl` | Bestimmt nach der Rollenklärung, welches der vier Zeugnis-Harnesses aktiviert wird: qualifiziertes Zeugnis, einfaches Zeugnis, Zwischenzeugnis oder Ausbildungszeugnis nach Paragraf 16 BBiG. Jedes Harness hat einen eigenen Pflichtaufbau,... |
| `schlussformel-baukasten` | Vollständiger Baukasten für Schlussformeln im Arbeitszeugnis mit allen fünf Bausteinen: Bedauern, Dank, beruflicher Wunsch, persönlicher Wunsch, Erfolgswunsch. Jeder Baustein trägt zur Signalwirkung bei. Kein gesetzlicher Anspruch auf ei... |
| `schlussformel-notenwirkung` | Ordnet jede Schlussformel-Variante der entsprechenden Notenwirkung im Bewerbungsverkehr zu. Die Schlussformel hat keine eigenständige Klagbarkeit, aber eine klare Signalwirkung. Tabelle mit allen relevanten Kombination von Bausteinen und... |
| `stammdaten-erhebung` | Erhebt alle Pflichtdaten für den Zeugniskopf: vollständiger Name, Geburtsdatum, Eintrittsdatum, Austrittsdatum, exakte Positionsbezeichnung mit Hierarchiestufe, Abteilung und Unternehmen. Fehlende Daten werden als gekennzeichnete Platzha... |
| `steigerungsadverbien-katalog` | Vollständiger Katalog aller Steigerungsadverbien der deutschen Zeugnissprache mit ihrer exakten Notenwirkung. Unterteilt in Maximalsteigerer (Note 1), Standardsteigerer (Note 1 bis 2), Scheinsteigerer (Note 3) und Abschwächer (Note 3 bis... |
| `taetigkeitsbeschreibung-erheben` | Erhebt strukturiert, was die Person konkret getan hat: Kernaufgaben, Verantwortungsbereiche, Projekte, Führungsumfang, Budget- und Ergebnisverantwortung. Unterscheidet zwischen Pflichtaussagen (positionsabhängig) und optionalen Hervorheb... |
| `teamarbeit-formeln` | Formulierungskatalog für Teamarbeits- und Kollegialitätsaussagen im Zeugnis. Enthält Formeln für alle Noten sowie eine Liste riskanter Formulierungen, die ungewollt Konfliktsignale oder Alkohol-/Geselligkeitslesarten erzeugen. Die Teamau... |
| `teilzeit-elternzeit-darstellung` | Regeln für die Darstellung von Teilzeitarbeit und Elternzeit im Zeugnis. Teilzeitarbeit darf nicht negativ erwähnt werden. Elternzeit ist anzugeben, wenn sie einen wesentlichen Teil der Beschäftigungszeit ausmacht. Enthält korrekte Formu... |
| `verhalten-vorgesetzte-kollegen-kunden` | Formulierungskatalog für den Verhaltensabschnitt im qualifizierten Zeugnis. Die Reihenfolge Vorgesetzte vor Kollegen vor Kunden ist Pflicht — eine falsche Reihenfolge ist ein eigenständiger Berichtigungspunkt. Enthält Formeln für alle No... |
| `wohlwollensgrundsatz-und-wahrheit` | Erklärt das Spannungsverhältnis zwischen Zeugniswahrheit und verständigem Wohlwollen als zentrale Generierungsprinzipien. Das Zeugnis muss wahr sein und darf gleichzeitig wohlwollend formuliert sein — beides ist Pflicht. Zeugniswahrheit... |
| `zeugnisart-ausbildungszeugnis-16-bbig` | Aufbau und Pflichtinhalt des Ausbildungszeugnisses nach Paragraf 16 BBiG. Unterscheidet einfaches und qualifiziertes Ausbildungszeugnis (auf Verlangen). Enthält Formulierungskatalog für Lernfortschritt, Berufsschulleistungen und Verhalte... |
| `zeugnisart-einfach` | Aufbau und Pflichtinhalt des einfachen Arbeitszeugnisses nach Paragraf 109 Abs. 1 S. 1 und 2 GewO. Enthält nur Art und Dauer der Tätigkeit, keine Leistungs- oder Verhaltensaussage. Wann ist das einfache Zeugnis angemessen und wann hat de... |
| `zeugnisart-praktikum` | Aufbau und Besonderheiten des Praktikumszeugnisses. Kein gesetzlicher Anspruch auf Leistungs-/Verhaltensaussage nach Paragraf 109 GewO bei Praktikantenverhältnissen — analoge Anwendung ist jedoch üblich. Enthält vollständiges Musterzeugn... |
| `zeugnisart-qualifiziert` | Vollständiger Aufbau des qualifizierten Arbeitszeugnisses nach Paragraf 109 Abs. 1 S. 3 GewO. Beschreibt alle Pflichtabschnitte in der richtigen Reihenfolge, Formvorschriften, Fließtextpflicht und Unterschriftserfordernisse. Das qualifiz... |
| `zeugnisart-zwischenzeugnis` | Aufbau und Besonderheiten des Zwischenzeugnisses bei laufendem Arbeitsverhältnis. Präsens statt Vergangenheit, kein Beendigungssatz, kein Abschlussdatum. Das Zwischenzeugnis ist an dasselbe Qualitätsniveau wie das qualifizierte Endzeugni... |
| `zeugnisklarheit-objektiver-empfaengerhorizont` | Das Gebot der Zeugnisklarheit aus Paragraf 109 Abs. 2 GewO und der BAG-Rechtsprechung (9 AZR 352/04; 9 AZR 386/10). Maßgeblich ist der objektive Empfängerhorizont. Formulierungen müssen das ausdrücken, was ihr Wortlaut besagt — nicht meh... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Arbeitszeugnis Analyse-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Arbeitszeugnis-Analyse (Ampelsystem) — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Arbeitszeugnis Analyse**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Analyse deutscher Arbeitszeugnisse nach Ampelsystem (Rot/Orange/Gruen). Geheimcodes, Schaufenster-Drift, negative Codeworte, Steigerungsadverbien. Satzweise Notenmatrix, gewichtete Gesamtnote. Vollständiger Mandatsablauf: Erstgespraech, Mandantenbericht, Aufforderungsschreiben, Klagestrategie.

### 0. Stummer Upload — Dokument ohne Begleittext

Wenn der Nutzer **nur ein Dokument hochlaedt und keinen weiteren Text schreibt** (kein Auftrag, keine Frage, keine Rolle), startet dieser Skill von selbst und wartet **nicht** auf einen Prompt. Verhalte dich dann wie der diensthabende Fachanwalt am Empfang, der eine zugestellte Akte sieht und sofort sinnvoll handelt.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Dokument-Klassifikation** in einem Satz: Welche Aktenart liegt vor? (Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz der Gegenseite, Akten-Konvolut, Tabelle, Foto/Screenshot, Anhoerungsbogen, Mahnbescheid, Rechnung, AU-Bescheinigung, KBA-Auszug, Registerauszug, ...). Wenn das Dokument einen klaren Briefkopf oder Tenor hat, das woertlich nennen.
2. **Norm- und Themenzuordnung** in ein bis drei Stichworten: Welches Rechtsgebiet, welche Norm, welcher Lebenssachverhalt? (z. B. "Gebuehrenbescheid BVG — § 23 MobG BE — Umsetzung aus Bushaltestelle".)
3. **Fristen-Triage zuerst:** Pruefe sichtbare Fristen (Widerspruchsfrist, Klagefrist, Berufungsfrist, Anhoerungsfrist, Rechtsbehelfsbelehrung). Wenn eine Frist erkennbar laeuft, das **als erstes** ausgeben — vor allem anderen.
4. **Beteiligten-Notiz:** Wer ist Absender, wer ist Adressat, gibt es Aktenzeichen, Behoerde, Gericht, Gegenseite?
5. **Routing in den passenden Spezial-Skill** dieses Plugins: Nenne **genau einen** Skill als primaeren Bearbeitungs-Skill und bis zu zwei weitere als Alternativen. Wenn der primaere Skill eindeutig ist, **arbeite sofort mit diesem Skill weiter** (nicht erst nachfragen). Wenn er nicht eindeutig ist, frage **eine einzige** gezielte Klaerungsfrage — nicht die volle Intake-Liste aus Abschnitt 1.
6. **Wenn die Klassifikation scheitert** (Dokument unleserlich, nicht zuordenbar, fremdes Rechtsgebiet): genau das sagen, eine konkrete Rueckfrage stellen ("Worum geht es?" reicht **nicht** — besser: "Ist das ein Bescheid der Behoerde X gegen Sie persoenlich oder gegen Ihren Mandanten Y?").

**Was du bei stummem Upload nicht machst:**

- Keine generische Inhaltszusammenfassung des Dokuments ("Sie haben ein PDF mit drei Seiten hochgeladen ...").
- Keine vollstaendige Intake-Abfrage aus Abschnitt 1 (Rolle, Ziel, Format ...). Diese Fragen kommen nur, wenn das Routing nicht eindeutig ist.
- Kein Warten auf einen Prompt. Der Upload **ist** der Prompt.

**Antwortformat bei stummem Upload:**

**Erkannt:** [Aktenart in einem Satz, mit Aktenzeichen/Absender wenn sichtbar]
**Rechtsgebiet:** [Norm/Thema in 1–3 Stichworten]
**Fristen-Hinweis:** [konkrete Frist mit Datum, oder "keine Frist erkennbar"]
**Primaerer Skill:** `skill-name` — [warum]
**Alternativen:** `...`, `...`
**Naechster Schritt:** [entweder direkter Arbeitsschritt ODER **eine** gezielte Rueckfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `ampelsystem-tabellenausgabe` | Erstellt die standardisierte Ampel-Ausgabetabelle für analysierte Arbeitszeugnisse. Anwendungsfall Zeugnisanalyse ist abgeschlossen und Ergebnis soll in einheitlicher Tabelle mit Satz Ampel Bewertung Notentendenz und… |
| `aufforderungsschreiben-arbeitgeber` | Außergerichtliches Berichtigungsverlangen an den Arbeitgeber. Aufbau mit Mandatsanzeige, konkreter Beanstandung pro Streitstelle (Wortlaut alt, Wortlaut neu, Begründung mit BAG-Rechtsprechung und Geheimcode-Hinweis),… |
| `azubi-zeugnis-analyse` | Analyse von Ausbildungszeugnissen nach § 16 BBiG bei Zeugnisstreit oder Berichtigungsverlangen. Anwendungsfall Auszubildender hat Ausbildungszeugnis erhalten das er für schlecht haelt. Normen § 16 BBiG Zeugnispflicht §… |
| `bereichs-drift-detektor` | Erkennt das Schaufenster-Pattern in Arbeitszeugnissen: einzelne Spitzensaetze suggerieren Note eins, waehrend benachbarte Saetze zum selben Themenbereich nur Note drei tragen. Tracked Drift pro Themenbereich… |
| `branchen-spezifische-formulierungen` | Decodiert branchenspezifische Formulierungen im Arbeitszeugnis zur praezisen Noteneinordnung. Anwendungsfall Zeugnis enthaelt Formulierungen die nur im Kontext einer bestimmten Branche verstaendlich sind. Branchen… |
| `erstgespraech-und-mandatsannahme` | Mandatsannahme im Zeugnisrecht mit Erstgespraech Unterlagenerfassung und Fristen-Erstprognose. Anwendungsfall Arbeitnehmer erhaelt Zeugnis das er für mangelhaft haelt und sucht anwaltliche Hilfe. Normen § 109 GewO… |
| `geheimcode-katalog` | Zentraler Referenzkatalog aller Standardformulierungen im deutschen Arbeitszeugnis mit Ampelzuordnung. Anwendungsfall Anwalt oder Arbeitnehmer will eine Zeugnisformulierung einordnen und weiss nicht ob sie positiv… |
| `gesamtnoten-aggregation` | Aggregiert Einzelbewertungen aus Leistungs- Verhaltens- und Schlussformel-Analyse zur Gesamtnote. Anwendungsfall alle Einzelsaetze sind analysiert und eine gewichtete Gesamtnote soll bestimmt werden. Normen § 109 GewO… |
| `gruen-flaggen-katalog` | Katalog starker positiver Formulierungen im Arbeitszeugnis, die auf Note 1 oder Note 2 hindeuten. Umfasst Superlative, vollständige Zufriedenheitsformeln und alle grünen Ampelsignale mit Notentendenz und Begründung. |
| `klage-strategie-zeugnisberichtigung` | Strategie und Antragsformulierungen für die Zeugnisberichtigungsklage vor dem Arbeitsgericht. Anwendungsfall außergerichtliches Berichtigungsverlangen ist gescheitert und Klage soll eingereicht werden. Normen § 109… |
| `leistungsbeurteilung-analyse` | Analysiert Sätze zur Arbeitsqualität, Arbeitsbereitschaft, Arbeitsweise, Arbeitstempo und Belastbarkeit im Arbeitszeugnis. Decodiert Formulierungen wie 'stets sorgfältig', 'bemüht' oder 'im Wesentlichen' und ordnet sie… |
| `leitende-positionen-zeugnisse` | Analyse von Arbeitszeugnissen für Führungskräfte und leitende Angestellte. Besondere Formulierungen zu Mitarbeiterführung, Personalentwicklung, strategischer Verantwortung und Repräsentation. Fehlende Führungsbausteine… |
| `mandantenbericht-zeugnisanalyse` | Schriftlicher Ergebnisbericht an den Arbeitnehmer nach abgeschlossener Ampelanalyse. Strukturierter Aufbau in Gesamtnote, Befund pro Themenbereich, kritische Geheimcodes und Drift-Stellen, rechtliche Einordnung,… |
| `muster-arbeitszeugnis-gemischte-noten` | Anonymisiertes Schulungszeugnis mit Schaufenster-Pattern für Training und Demonstration. Anwendungsfall Rechtsanwalt oder Mitarbeiter will Zeugnisanalyse-Skills an einem Musterfall trainieren. Zeigt klassisches… |
| `muster-arbeitszeugnis-mit-roten-flaggen` | Anonymisiertes Beispielzeugnis mit roten orangen und gruenen Bewertungen als Schulungsmaterial. Anwendungsfall Training für Zeugnissprache und Geheimcode-Erkennung. Enthalt gemischte Ampelsignale mit vollständiger… |
| `muster-arbeitszeugnis-note-1` | Vollständiges Musterarbeitszeugnis Note 1 als Referenzdokument für Vergleich und Berichtigung. Anwendungsfall Anwalt oder Mandant will wissen wie ein optimales Zeugnis aussieht. Alle Bausteine in gruener Formulierung… |
| `negationen-und-auslassungen-erkennen` | Erkennt fehlende Pflichtaussagen im Arbeitszeugnis: Was nicht gesagt wird, ist oft entscheidend. Prüft Checkliste auf fehlende Loyalität, Ehrlichkeit, Pünktlichkeit und andere Standardaussagen und bewertet Auslassungen… |
| `negative-codeworte-katalog` | Erweiterter Katalog negativer Codeworte und ihrer kodierten Bedeutung. Erfasst die thematischen Cluster Alkohol und Suchtmittel, Krankheitshaeufung, Konflikte, Diebstahl und Vertrauensbruch, mangelnde Loyalitaet,… |
| `notenrelevante-saetze-identifizieren` | Identifiziert notenrelevante Saetze im Arbeitszeugnis und trennt sie von neutralen Aufgabenbeschreibungen. Anwendungsfall Zeugnis liegt vor und muss für Ampelanalyse vorbereitet werden. Normen § 109 GewO Inhalte eines… |
| `orange-flaggen-katalog` | Katalog schwacher positiver Formulierungen im Arbeitszeugnis, die auf Note 3 hindeuten. Umfasst alle Orange-Signale: fehlende Steigerungsadverbien, eingeschränkte Lobesformeln und strukturelle Abschwächungen mit… |
| `rechtliche-bewertung-bag-rechtsprechung` | Rechtliche Einordnung von Zeugnisansprüchen nach § 109 GewO und BAG-Rechtsprechung für die anwaltliche Praxis. Anwendungsfall Anwalt benoetigt Beweislastverteilung und Rechtsgrundlagen für Zeugnisstreit oder… |
| `rote-flaggen-katalog` | Katalog klassischer roter Warnsignale im deutschen Arbeitszeugnis: Formulierungen, die trotz positiv klingendem Wortlaut eine schlechte Beurteilung kodieren. Umfasst alle Note-4- und Note-5-Signale mit Erklärung und… |
| `satzweise-notenmatrix` | Bewertet jeden notenrelevanten Satz eines Arbeitszeugnisses mit Schulnote 1 bis 5. Anwendungsfall notenrelevante Saetze wurden identifiziert und sollen systematisch bewertet werden. Normen § 109 GewO Bewertungsmassstab… |
| `schlussformel-bewertung` | Bewertet die Schlussformel eines Arbeitszeugnisses nach Vollständigkeit der drei Elemente: Bedauern über das Ausscheiden, Dank für geleistete Arbeit und Zukunftswünsche. Fehlende Elemente senken die Gesamtnote messbar. |
| `steigerungsadverbien-katalog` | Vollständige Referenzliste aller Steigerungsadverbien der Zeugnissprache mit Notenwert. Ein Adverb fehlt, eine Note faellt. Trennt echte Steigerer (stets, jederzeit, vollkommen, hoechst) von scheinbaren Steigerern… |
| `verbesserungsvorschlaege-formulieren` | Formuliert konkrete Verbesserungsvorschläge für orange und rote Zeugnissätze. Zeigt, wie aus einer Note-4-Formulierung eine Note-2-Formulierung wird — mit Gegenüberstellung Original/Vorschlag und Begründung der… |
| `verhaltensbeurteilung-analyse` | Analysiert Verhaltensbeurteilungen im Arbeitszeugnis: Verhalten zu Vorgesetzten, Kollegen und Kunden. Decodiert die Reihenfolge der Genannten, Qualifikationswörter und die Bedeutung von Auslassungen als versteckte… |
| `widerspruechliche-bewertungen` | Erkennt und kommentiert Widersprüche im Arbeitszeugnis: wenn Leistungsteil grün, aber Schlussformel rot ist, oder wenn Einzelsätze sich inhaltlich ausschließen. Erklärt die Signalwirkung von Widersprüchen auf… |
| `zeugnis-ueberblick-extraktion` | Extrahiert Kopfdaten aus deutschen Arbeitszeugnissen für Mandatsanlage und Analysestart. Anwendungsfall Zeugnis wurde hochgeladen und Basisdaten sollen für Akte und Analyse erfasst werden. Normen § 109 GewO… |
| `zeugnisart-erkennung` | Unterscheidet qualifiziertes Endzeugnis einfaches Zeugnis Zwischenzeugnis und Ausbildungszeugnis am Beginn jeder Analyse. Anwendungsfall Zeugnis liegt vor und muss bevor Analyse startet der richtigen Zeugnisart… |
| `zufriedenheitsformel-decodierung` | Decodiert die fünfstufige Zufriedenheitsformel deutscher Arbeitszeugnisse: von Note 1 bis Note 5. Tabellarische Ampelzuordnung aller Standardformulierungen mit Erklärung der sprachlichen Feinheiten und ihrer… |

## Worum geht es?

Das Ampelsystem fuer die Zeugnisanalyse decodiert die verdeckte Notenskalierung in deutschen Arbeitszeugnissen: Formulierungen werden Ampelfarben zugeordnet (gruen = Note eins bis zwei, orange = Note drei, rot = Note vier bis fuenf). Das Plugin deckt den gesamten Mandatsablauf ab: vom Erstgespraech ueber die satzweise Notenmatrix und Gesamtnotenberechnung bis hin zum Mandantenbericht, dem aussergerichtlichen Aufforderungsschreiben und der Klagestrategie vor dem Arbeitsgericht.

Zielgruppe sind Arbeitsrechts-Anwaelte und deren Sekretariate. Das Plugin ist auf die BAG-Rechtsprechung zum Zeugnisrecht abgestimmt.

## Wann brauchen Sie diese Skill?

- Ein Arbeitnehmer hat ein Zeugnis erhalten, das er fuer inhaltlich oder sprachlich ungenuegend haelt, und sucht anwaltliche Einschaetzung.
- Ein Auszubildender will sein Ausbildungszeugnis nach § 16 BBiG anfechten.
- Ein Mandat im Kuendigungsschutz beinhaltet auch einen Zeugnisanspruch (§ 109 GewO), der in einem Vergleich geregelt werden soll.
- Eine Fuerungskraft erhaelt ein Zeugnis ohne Fuehrungs-Bausteine und fragt, ob das ein Negativsignal ist.
- Die Kanzlei benoetigt ein Schulungsmaterial fuer die Zeugnisanalyse (Musterzeugnisse).

## Fachbegriffe (kurz erklaert)

- **Geheimcode** — Formulierung, die trotz positiv klingendem Wortlaut eine schlechte Bewertung kodiert (z.B. "Er hat sich bemuht" = mangelhaft).
- **Steigerungsadverb** — Adverb, das die Staerke eines Lobs quantifiziert; Fehlen eines Steigerungsadverbs senkt die Note um eine Stufe.
- **Schaufenster-Drift** — einzelne Spitzensaetze (Note eins) in einem Themenbereich, der sonst nur Note drei traegt; systematisch irreführend.
- **Schlussformel** — dreisteiliges Pflichtelement: Bedauern, Dank und Zukunftswuensche; jedes fehlende Element senkt die Gesamtnote.
- **Wohlwollenspflicht** — Pflicht des Arbeitgebers, ein der Wahrheit entsprechendes, aber wohlwollendes Zeugnis auszustellen (§ 109 GewO).
- **Berichtigungsklage** — Klage auf Neufassung des Zeugnisses; Streitwert ein bis drei Bruttomonatsentgelte; Zustaendigkeit: Arbeitsgericht.

## Rechtsgrundlagen

- § 109 GewO — Anspruch auf qualifiziertes Zeugnis
- § 16 BBiG — Anspruch auf Ausbildungszeugnis
- § 241 Abs. 2 BGB — Wohlwollenspflicht (Nebenpflicht aus Arbeitsvertrag)
- § 195 BGB — Verjaehrung drei Jahre
- § 611a BGB — Arbeitsvertrag

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Arbeitnehmer oder Auszubildender? Endzeugniss, Zwischenzeugnis oder Ausbildungszeugnis?
2. Phase des Mandats bestimmen: Erstanalyse, aussergerichtliche Aufforderung, Klage oder Vergleichsformulierung?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen pruefen: Verjaehrung des Berichtigungsanspruchs nach § 195 BGB; Verjaehrung beginnt mit Zeugniserhalt (§ 199 BGB).
5. Anschluss-Skill bestimmen: Nach Notenmatrix Gesamtnotenberechnung, dann Mandantenbericht, dann Aufforderungsschreiben.

## Skill-Tour (was gibt es hier?)

- `erstgespraech-und-mandatsannahme` — Mandatsannahme mit Unterlagenerfassung, Erstprognose und Fristen-Uebersicht.
- `zeugnisart-erkennung` — Unterscheidung qualifiziertes Endzeugnis, einfaches Zeugnis, Zwischenzeugnis und Ausbildungszeugnis.
- `zeugnis-ueberblick-extraktion` — Kopfdaten aus dem Zeugnis extrahieren: Arbeitgeber, Arbeitnehmer, Zeitraum, Position.
- `notenrelevante-saetze-identifizieren` — Notenrelevante Saetze von neutralen Aufgabenbeschreibungen trennen.
- `satzweise-notenmatrix` — Jeden notenrelevanten Satz mit Schulnote bewerten: Pruefraster Themenbereich, Note, Begruendung.
- `bereichs-drift-detektor` — Schaufenster-Pattern erkennen: Note-eins-Saetze neben Note-drei-Saetzen im gleichen Themenbereich.
- `gesamtnoten-aggregation` — Gewichtete Gesamtnote aus Leistungsteil, Verhaltensteil und Schlussformel aggregieren.
- `ampelsystem-tabellenausgabe` — Standardisierte Ampel-Ausgabetabelle fuer den Mandantenbericht erstellen.
- `geheimcode-katalog` — Zentraler Referenzkatalog aller Standardformulierungen mit Ampelzuordnung.
- `rote-flaggen-katalog` — Katalog Note-vier- und Note-fuenf-Signale mit Erlaeuterungen.
- `orange-flaggen-katalog` — Katalog Note-drei-Signale: fehlende Steigerungsadverbien und eingeschraenkte Lobesformeln.
- `gruen-flaggen-katalog` — Katalog Note-eins- und Note-zwei-Signale: Superlative und vollstaendige Zufriedenheitsformeln.
- `negative-codeworte-katalog` — Erweiterte Katalog kodierter Negativformulierungen (Sucht, Konflikte, Diebstahl, Loyalitaet).
- `steigerungsadverbien-katalog` — Vollstaendige Referenzliste aller Steigerungsadverbien mit Notenwert und Abgrenzung zu Scheinsteigern.
- `zufriedenheitsformel-decodierung` — Fuenfstufige Zufriedenheitsformel decodieren: von "vollste Zufriedenheit" bis "Zufriedenheit".
- `leistungsbeurteilung-analyse` — Saetze zu Arbeitsqualitaet, Arbeitsbereitschaft und Belastbarkeit decodieren.
- `verhaltensbeurteilung-analyse` — Verhaltensbeurteilungen decodieren: Reihenfolge der Genannten, Auslassungen, Qualifikationswoerter.
- `schlussformel-bewertung` — Vollstaendigkeit der drei Schlussformel-Elemente pruefen und Notenauswirkung bestimmen.
- `negationen-und-auslassungen-erkennen` — Fehlende Pflichtaussagen im Zeugnis identifizieren und als Negativsignal bewerten.
- `widerspruechliche-bewertungen` — Widersprueche zwischen Leistungsteil und Schlussformel erkennen und deren Signalwirkung erklaeren.
- `branchen-spezifische-formulierungen` — Branchenspezifische Formulierungen in Vertrieb, IT, Recht, Pflege und anderen Bereichen einordnen.
- `leitende-positionen-zeugnisse` — Zeugnisse fuer Fuehrungskraefte analysieren: fehlende Fuehrungs-Bausteine als Ampelsignal.
- `azubi-zeugnis-analyse` — Ausbildungszeugnisse nach § 16 BBiG analysieren: Lernfortschritt, Berufsschulleistungen, Verhalten.
- `verbesserungsvorschlaege-formulieren` — Konkrete Alternativformulierungen fuer orange und rote Saetze vorschlagen.
- `rechtliche-bewertung-bag-rechtsprechung` — Beweislastverteilung und Rechtsgrundlagen nach § 109 GewO und BAG-Linie fuer Klagebegruendung.
- `mandantenbericht-zeugnisanalyse` — Strukturierter Ergebnisbericht an den Mandanten mit Handlungsoptionen und Empfehlung.
- `aufforderungsschreiben-arbeitgeber` — Aussergerichtliches Berichtigungsverlangen mit BAG-Rechtsprechungs-Pinpoints und Fristsetzung.
- `klage-strategie-zeugnisberichtigung` — Klageschrift-Baustein fuer Zeugnisberichtigungsklage vor dem Arbeitsgericht.
- `muster-arbeitszeugnis-note-1` — Vollstaendiges Musterarbeitszeugnis Note eins als Referenzdokument.
- `muster-arbeitszeugnis-mit-roten-flaggen` — Anonymisiertes Beispielzeugnis mit roten und orangen Bewertungen als Schulungsmaterial.
- `muster-arbeitszeugnis-gemischte-noten` — Schulungszeugnis mit Schaufenster-Pattern und Drift-Analyse als Lernbeispiel.

## Worauf besonders achten

- **Steigerungsadverb-Pruefung**: Ein fehlendes "stets" oder "jederzeit" senkt die Note des gesamten Satzes; auch Frequenzadverbien wie "regelmaessig" oder "gelegentlich" bedeuten Note drei oder schlechter.
- **Schaufenster-Pattern fruehzeitig erkennen**: Einzelne Spitzensaetze koennen den Gesamteindruck bewusst positiver erscheinen lassen; der Bereichs-Drift-Detektor muss jeden Themenbereich separat auswerten.
- **Schlussformel ist Pflichtelement**: Ein fehlendes Bedauern senkt die Gesamtnote messbar; Arbeitgeber koennen nicht auf Schlussformel-Bestandteile verzichten, ohne Notenfolgen zu akzeptieren.
- **Beweislast beim Zeugnisstreit**: Arbeitnehmer muss darlegen, dass seine Leistung besser war als das Zeugnis suggeriert; Arbeitgeber hat dann die schlechtere Note zu substantiieren.
- **Verjaehrung beachten**: Der Berichtigungsanspruch verjaehrt in drei Jahren nach § 195 BGB; bei laengerer Untaetigkeit des Mandanten Fristen rechnen.

## Typische Fehler

- Zeugnisart nicht bestimmt: Eine Zwischenzeugnisanalyse unterscheidet sich vom Endzeugniss; Massstabe sind nicht identisch.
- Notenmatrix ohne Bereichs-Drift erstellt: Die Gesamtnote kann positiver erscheinen, als die satzweise Analyse vermuten laesst; Drift-Pruefung ist Pflicht.
- Verbesserungsvorschlaege zu allgemein formuliert: Das Gericht verurteilt nicht zu einer bestimmten Formulierung, wenn der Antrag zu weit oder zu unkonkret ist; praezise Antragsformulierung ist entscheidend.
- Keine Beweislastanalyse vor dem Aufforderungsschreiben: Wenn die Ausgangsbewertung nicht substantiiert werden kann, ist die Aussicht auf eine Klage gering.
- Schlussformel als optional behandelt: Fehlende Zukunftswuensche sind ein messbares Note-Drei-Signal; Mandanten muessen das verstehen.

## Querverweise

- `arbeitsrecht` — Wenn der Zeugnisanspruch im Rahmen einer Kuendigungsschutzklage oder eines Aufhebungsvertrags geregelt wird.
- `prozessrecht` — Fuer prozessuale Fragen zur Klageschrift, Beweislast und Vollstreckung von Zeugnisurteilen.

## Quellen und Aktualitaet

- Stand: 05/2026
- § 109 GewO in geltender Fassung
- § 16 BBiG in geltender Fassung
- BAG-Rechtsprechung zum Zeugnisrecht (aktuelle Fassung)

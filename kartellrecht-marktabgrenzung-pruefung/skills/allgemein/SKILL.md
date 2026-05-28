---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Kartellrecht Marktabgrenzung Pruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Kartellrecht-Marktabgrenzungs-Pruefer — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Kartellrecht Marktabgrenzung Pruefung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Kritische kartellrechtliche Prüfinstanz für vorgelegte Marktabgrenzungen nach Paragraf 18 GWB und Art 101 und 102 AEUV. SSNIP-Test Nachfrage- und Angebotsumstellung räumlicher Markt Evidenzbasierung Konsistenzcheck EuGH-Leitentscheidungen Red Flags alternative Marktdefinitionen Marktbeherrschung.

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
| `alternative-marktdefinition-eng` | Mandant will eine engere Marktabgrenzung argumentieren um niedrigere Marktanteile oder fehlende Marktbeherrschung zu zeigen. Generiert engere alternative Marktdefinition mit juristischer und oekonomischer Begründung.… |
| `alternative-marktdefinition-weit` | Mandant will eine weitere Marktabgrenzung argumentieren um niedrigere Marktanteile zu zeigen oder Behoerden-Markt anzugreifen. Generiert weitere alternative Marktdefinition mit juristischer und oekonomischer… |
| `auswirkungen-marktanteile-marktbeherrschung` | Wie aendert sich der Marktanteil des Mandanten je nachdem wie eng oder weit der Markt abgegrenzt wird. Quantifiziert Auswirkungen alternativer Marktabgrenzungen auf Marktanteile und Marktbeherrschungsvermutungen.… |
| `cluster-und-systemmaerkte` | Behoerde oder Gegenseite argumentiert mit Cluster-Markt oder Aftermarkt-Doktrin oder Mandant will dies nutzen. Prüft Cluster-Maerkte Buendelung nicht-substitutiver Produkte und Systemmaerkte Primaermarkt plus… |
| `dma-und-gatekeeper-markt` | Digital Markets Act (VO 2022/1925): Gatekeeper-Designierung Kernplattformdienste quantitative und qualitative Schwellenwerte. Auswirkungen der DMA-Designierung auf die Marktdefinition in kartellrechtlichen Verfahren.… |
| `elastizitaeten-diversion-ratios` | Oekonomischer Gutachter oder Mandant legt Elastizitaetsdaten oder Diversion-Ratio-Analyse vor und Belastbarkeit ist zu prüfen. Prüft Eigenpreis-Elastizitaet Kreuzpreis-Elastizitaet und Diversion Ratios als Instrumente… |
| `eu-bekanntmachung-marktdefinition-2024` | Skill zur neuen EU-Kommissions-Bekanntmachung zur Marktdefinition (Februar 2024) und ihrer praktischen Anwendung. Vergleich zur Bekanntmachung von 1997. Neue Elemente: digitale Maerkte Innovationswettbewerb… |
| `eugh-rechtsprechung-leitentscheidungen` | Einschlägige EuGH/EuG/BGH/BKartA-Leitentscheidungen zur Marktdefinition mit Pinpoint-Zitaten: Continental Can Rs 6/72 United Brands Rs 27/76 Hoffmann-La Roche Rs 85/76 Michelin I Rs 322/81 Tetra Pak II T-83/91… |
| `evidenz-qualitaet-bewertung` | Bewertet die Qualitaet und Belastbarkeit der vorgelegten Belege für eine Marktabgrenzung: interne Unternehmensdokumente Kundenverhaltensdaten Marktdaten Elastizitaeten Diversion Ratios Branchenberichte. Erkennt… |
| `fusionskontrolle-modus` | Prüft Marktabgrenzung im Kontext der EU-Fusionskontrolle (FKVO 139/2004): Phase I und Phase II SIEC-Test (Significant Impediment to Effective Competition) horizontale und nicht-horizontale Fusionen Effizienzeinrede und… |
| `gesamtbewertung-tragfaehigkeit` | Gesamturteil zur Tragfähigkeit einer Marktabgrenzung: hoch mittel oder gering. Fasst zentrale Schwachstellen in 3 bis 5 scharfen Punkten zusammen. Bewertet Angreifbarkeit vor Gericht oder Behoerde und empfiehlt… |
| `innovations-und-technologiemaerkte` | Marktabgrenzung in dynamischen Technologiemaerkten wo kuenftige Innovation den Wettbewerb praegt oder Patent-Pools streitig sind. Prüft Innovationsmaerkte technologische Substitution Standard-Essential-Patents… |
| `kartellverbot-modus` | Prüft Marktabgrenzung im Kontext des Kartellverbots (Art 101 AEUV und Paragraf 1 GWB): Wettbewerbsbeschraenkung bezweckt oder bewirkt Single-Brand vs Inter-Brand Wettbewerb Spuerbarkeit nach Bagatellbekanntmachung und… |
| `konsistenzpruefung-marktdefinition` | Prüft die interne Widerspruchsfreiheit einer Marktabgrenzung: Übereinstimmung von Sachmarkt und räumlichem Markt tatsaechlichem Marktverhalten Behoerdenpraxis und oekonomischen Grundprinzipien. Erkennt Zirkelschluesse… |
| `marktabgrenzung-kontextanalyse` | Verfahren beginnt und Verfahrensart und Parteistellung muessen bestimmt werden bevor die Marktabgrenzung-Analyse starten kann. Identifiziert Verfahrensart Fusionskontrolle Kartellverbot Missbrauchsverfahren und… |
| `mehrseitige-maerkte-plattformen` | Sonderprobleme der Marktdefinition für mehrseitige Plattformen: zweiseitige Marktdefinition indirekte Netzwerkeffekte getrennte vs. integrierte Marktbetrachtung. Einschluss von App-Store App-Markt Werbe- und… |
| `missbrauchsverbot-modus` | Unternehmen in marktbeherrschender Stellung soll auf Missbrauch geprüft werden oder Wettbewerber klagt auf Missbrauch. Prüft Marktabgrenzung und Missbrauchstatbestaende Art. 102 AEUV § 19 GWB. Prüfraster… |
| `paragraf-18-gwb-pruefung` | Prüft Marktbeherrschung nach Paragraf 18 GWB: Einzelmarktbeherrschung Abs 1 Marktanteils-Schwellen Abs 4 (40 Prozent) gemeinsame Marktbeherrschung Abs 5 und 6 intermediaere Plattformen Abs 3a sowie relative Marktmacht… |
| `potenzieller-wettbewerb-marktzutritt` | Behoerde oder Gegenseite argumentiert fehlende Markteintrittsbarrieren um Marktbeherrschung zu verneinen. Analysiert Markteintrittsschranken und Wahrscheinlichkeit potenziellen Wettbewerbs im Zeitrahmen 2 bis 3 Jahre.… |
| `produktmarkt-angebotsumstellung` | Prüft angebotsseitige Substitution (Supply-Side Substitution): Kann ein anderer Anbieter kurzfristig und ohne erhebliche Kosten auf den relevanten Markt wechseln? Bewertet Umstellungskosten regulatorische Anforderungen… |
| `produktmarkt-nachfragesubstitution` | Kernschritt jeder Marktabgrenzung: sachlicher Markt aus Nachfragersicht bestimmen. Prüft funktionale Austauschbarkeit Preisreagibilitaet qualitative Unterschiede Verwendungszweck Bedarfsdeckungsaequivalenz. Normen § 18… |
| `raeumlicher-markt-abgrenzung` | Prüft den räumlich relevanten Markt: national europaeisch global. Analysiert Preisstrukturen Transportkosten regulatorische Unterschiede Homogenitaetsannahmen Handelsstroeme und Arbitragemoeaeglichkeiten. Bewertet ob… |
| `red-flags-checkliste` | Strukturierte Checkliste problematischer Muster in Marktabgrenzungen: ergebnisgetriebene Argumentation Zirkelschluesse fehlende oekonomische Fundierung selektive Datenwahl kuenstliche Marktverengung oder -erweiterung… |
| `ssnip-test-anwendung` | Sachlichen Markt mit dem SSNIP-Test abgrenzen ob ein hypothetischer Monopolist profitabel Preise um 5 bis 10 Prozent erhoehen koennte. Wendet Small but Significant Non-transitory Increase in Price… |

## Worum geht es?

Dieses Plugin ist die kritische Pruefinstanz fuer vorgelegte Marktabgrenzungen in kartellrechtlichen Verfahren. Es prueft Marktabgrenzungen nach § 18 GWB sowie Art. 101 und 102 AEUV — unabhaengig davon, ob es sich um Fusionskontrollverfahren, Missbrauchsverfahren oder Kartellverbotsverfahren handelt.

Das Plugin orientiert sich an der EU-Bekanntmachung zur Marktdefinition von Februar 2024 (ABl. 2024/C 1645), an der Rechtsprechung des EuGH und EuG sowie an der Praxis des BKartA. Es identifiziert systematisch methodische Schwachstellen, selektive Datenwahl, Zirkelschluesse und alternative Marktdefinitionen, die prozessual oder behoerdlich angreifbar sind.

## Wann brauchen Sie diese Skill?

- Sie pruefen eine von der Gegenseite oder einer Behoerde vorgelegte Marktabgrenzung auf Angreifbarkeit.
- Sie erstellen eine eigene Marktabgrenzungsargumentation fuer ein Fusionskontroll-, Missbrauchs- oder Kartellverfahren.
- Sie begleiten ein BKartA- oder Kommissionsverfahren und muessen den Verfahrenskontext und die Parteistellung klaeren.
- Sie pruefen, ob eine DMA-Gatekeeper-Designation kartellrechtlich relevante Marktdefinitionen verschiebt.
- Sie wollen die Qualitaet und Belastbarkeit oekonomischer Gutachten zu Elastizitaeten oder Diversion Ratios beurteilen.

## Fachbegriffe (kurz erklaert)

- **SSNIP-Test** — Hypothetischer-Monopolisten-Test (Small but Significant Non-transitory Increase in Price): Klaert, welche Produkte und Regionen so nah substituierbar sind, dass ein Monopolist keinen profitablen Preisaufschlag von 5 bis 10 Prozent erzielen koennte.
- **Nachfragesubstitution** — Kernschritt der Marktabgrenzung: Welche Produkte wechseln Nachfrager bei einem kleinen Preisanstieg? Bestimmt den sachlichen Markt.
- **Angebotsumstellung** — Supply-Side-Substitution: Koennen andere Anbieter kurzfristig und ohne erhebliche Kosten auf den relevanten Markt wechseln?
- **Marktbeherrschung** — Erheblicher Wettbewerbsdruck fehlt; Vermutung bei 40-Prozent-Einzelmarktanteil nach § 18 Abs. 4 GWB.
- **Cellophane-Fallacy** — Methodischer Fehler beim SSNIP-Test: Pruefung von der bereits ueberhoeahten Marktmacht-Position aus fuehrt zu kuenstlich weitem Markt.
- **Inkongruente Deckung** — Begriff aus dem Anfechtungsrecht; hier nicht relevant.
- **Diversion Ratio** — Oekonomisches Mass fuer den Anteil der Nachfrage, der bei einem Preisanstieg zu einem bestimmten Wettbewerber abwandert; hohe Ratio spricht fuer engen Markt.
- **Gatekeeper** — Designierter Plattformbetreiber nach DMA; Designation beeinflusst kartellrechtliche Marktdefinition in parallelen Verfahren.

## Rechtsgrundlagen

- § 18 GWB — Marktbeherrschung, Marktanteils-Vermutungen, Plattformen.
- § 19 GWB — Missbrauch marktbeherrschender Stellung.
- § 20 GWB — Relative Marktmacht.
- § 35 GWB und FKVO 139/2004 — Fusionskontrolle und SIEC-Test.
- Art. 101 AEUV — Kartellverbot.
- Art. 102 AEUV — Missbrauchsverbot.
- EU-Bekanntmachung zur Marktdefinition 2024 (ABl. 2024/C 1645) — Methodischer Rahmen.
- DMA (VO 2022/1925) Art. 2 und 3 — Kernplattformdienste und Gatekeeper-Designation.

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Verfahrenskontext und Parteistellung klaeren: Skill `marktabgrenzung-kontextanalyse`.
2. Verfahrensmodus auswaehlen: `fusionskontrolle-modus`, `missbrauchsverbot-modus` oder `kartellverbot-modus`.
3. Sachlichen Markt pruefen: `produktmarkt-nachfragesubstitution` und `produktmarkt-angebotsumstellung`.
4. Raeumlichen Markt pruefen: `raeumlicher-markt-abgrenzung`.
5. Marktanteile und Beherrschung bewerten: `auswirkungen-marktanteile-marktbeherrschung` und `paragraf-18-gwb-pruefung`.
6. Gesamturteil und Angreifbarkeit: `gesamtbewertung-tragfaehigkeit`.

## Skill-Tour (was gibt es hier?)

**Einstieg und Kontext**

- `marktabgrenzung-kontextanalyse` — Verfahrensart und Zielrichtung bestimmen, Routing-Empfehlung.
- `fusionskontrolle-modus` — SIEC-Test, Phase I und II, horizontale und nicht-horizontale Fusionen.
- `missbrauchsverbot-modus` — Marktabgrenzung im Kontext von Art. 102 AEUV und § 19 GWB.
- `kartellverbot-modus` — Marktabgrenzung im Kontext von Art. 101 AEUV und § 1 GWB.

**Sachlicher Markt**

- `produktmarkt-nachfragesubstitution` — Sachlicher Markt aus Nachfragersicht; Kernschritt jeder Marktabgrenzung.
- `produktmarkt-angebotsumstellung` — Angebotsseitige Substitution; kurzfristiger Marktzutritt anderer Anbieter.
- `ssnip-test-anwendung` — SSNIP-Test (Hypothetischer-Monopolisten-Test) anwenden.
- `elastizitaeten-diversion-ratios` — Belastbarkeit oekonomischer Elastizitaetsdaten und Diversion-Ratio-Analysen pruefen.

**Raeumlicher Markt**

- `raeumlicher-markt-abgrenzung` — Raeumlich relevanter Markt: national, europaeisch oder global.

**Spezialmaerkte**

- `cluster-und-systemmaerkte` — Cluster-Maerkte und Aftermarket-Doktrin (Pelikan-Doktrin, Kyocera-Doktrin).
- `mehrseitige-maerkte-plattformen` — Zweiseitige Marktdefinition, indirekte Netzwerkeffekte, Plattform-Spezifika.
- `innovations-und-technologiemaerkte` — Innovationsmaerkte, SEPs, FuE-Maerkte in dynamischen Technologiesektoren.
- `dma-und-gatekeeper-markt` — DMA-Gatekeeper-Designation und Auswirkungen auf Marktdefinition.

**Marktanteile und Beherrschung**

- `paragraf-18-gwb-pruefung` — Marktbeherrschung nach § 18 GWB: Einzelbeherrschung, Schwellen, gemeinsame Beherrschung.
- `auswirkungen-marktanteile-marktbeherrschung` — Sensitivitaetsanalyse Marktanteil je Marktabgrenzungs-Szenario.
- `potenzieller-wettbewerb-marktzutritt` — Markteintrittsbarrieren und potenzieller Wettbewerb im Zeitrahmen zwei bis drei Jahre.

**Alternative Marktdefinitionen**

- `alternative-marktdefinition-eng` — Engere Marktdefinition argumentieren fuer niedrigere Marktanteile.
- `alternative-marktdefinition-weit` — Weitere Marktdefinition argumentieren gegen Beherrschungsvermutung.

**Evidenz und Qualitaet**

- `evidenz-qualitaet-bewertung` — Qualitaet und Belastbarkeit der Belege fuer eine Marktabgrenzung beurteilen.
- `eu-bekanntmachung-marktdefinition-2024` — Neue EU-Bekanntmachung Februar 2024 und Vergleich zur Bekanntmachung von 1997.
- `eugh-rechtsprechung-leitentscheidungen` — EuGH/EuG/BGH/BKartA-Leitentscheidungen zur Marktdefinition.

**Konsistenz und Gesamturteil**

- `konsistenzpruefung-marktdefinition` — Interne Widerspruchsfreiheit einer Marktabgrenzung pruefen.
- `red-flags-checkliste` — Problematische Muster in Marktabgrenzungen: ergebnisgetriebene Argumentation, Zirkelschluesse.
- `gesamtbewertung-tragfaehigkeit` — Gesamturteil zur Tragfaehigkeit; Angreifbarkeit und Prozesstaktik.

## Worauf besonders achten

- **Verfahrenskontext bestimmt Marktdefinition** — Die Richtung der Marktabgrenzungsargumentation haengt davon ab, ob Mandant Klaeger, Beklagter oder Zusammenschlusspartei ist; `marktabgrenzung-kontextanalyse` immer zuerst.
- **Cellophane-Fallacy** — Beim SSNIP-Test immer pruefen, ob Ausgangspreis bereits Marktmacht-Preis ist; Fehler fuehrt zu kuenstlich weitem Markt.
- **EU-Bekanntmachung 2024** — Seit Februar 2024 gelten neue Methodik-Standards fuer digitale Maerkte und Innovationswettbewerb; aeltere Marktabgrenzungen koennen veraltet sein.
- **DMA-Designation nicht gleichsetzen** — Eine DMA-Gatekeeper-Designation ist kein kartellrechtlicher Marktbeherrschungs-Befund; die Rechtsfragen sind trennbar.
- **Potenzielle Anbieter nicht uebergewichten** — Markteintrittsbarrieren muessen realistisch im Zeitfenster zwei bis drei Jahre bewertet werden; bloss theoretische Marktzutrittsmoeoglichkeit genuegt nicht.

## Typische Fehler

- Nachfragesubstitution und Angebotsumstellung werden verwechselt oder zusammengeworfen.
- SSNIP-Test wird ohne Cellophane-Fallacy-Pruefung auf einem bereits durch Marktmacht verzerrten Preisniveau angewendet.
- Leitentscheidungen werden ohne Pinpoint-Zitat zitiert und koennen prozessual nicht verwertet werden.
- Alternative Marktdefinitionen werden nicht erwaehnt, obwohl sie die Anteilsschwellen verschieben wuerden.
- Raeumlicher und sachlicher Markt werden nicht aufeinander abgestimmt (Konsistenzbruch).

## Querverweise

- `europarecht-kompass` — Fuer allgemeine EU-Rechtsfragen, Vorlagenverfahren und EU-Verfahrensrecht.
- `dsa-dma-digitalregulierung` — Fuer DMA-Gatekeeper-Pflichten und DSA-Fragen parallel zum Kartellrecht.
- `insolvenzplan-starug-planwerkstatt` — Bei Restrukturierungen mit kartellrechtlich relevantem Marktaustritt.

## Quellen und Aktualitaet

- Stand: 05/2026
- GWB §§ 18 ff. in der geltenden Fassung
- Art. 101 und 102 AEUV
- EU-Bekanntmachung zur Marktdefinition 2024 (ABl. 2024/C 1645)
- FKVO 139/2004 in der geltenden Fassung

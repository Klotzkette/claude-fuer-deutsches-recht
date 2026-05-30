# Kartellrecht — Marktabgrenzungsprüfung

Hochspezialisierte kartellrechtliche Prüfinstanz für vorgelegte Marktabgrenzungen — ob vom eigenen Team, der gegnerischen Partei oder einer Wettbewerbsbehörde. Schwerpunkte: § 18 GWB, Art. 101 und Art. 102 AEUV, EU-Bekanntmachung zur Marktdefinition 2024 (ABl. 2024/C 1645), SSNIP-Test, Nachfrage- und Angebotssubstitution, Evidenzbasierung, EuGH-Leitentscheidungen, Red Flags und alternative Marktdefinitionen.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Kartellrecht Marktabgrenzungsprüfung (`kartellrecht-marktabgrenzung-pruefung`, dieses Plugin) | [kartellrecht-marktabgrenzung-pruefung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kartellrecht-marktabgrenzung-pruefung.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Zweck

Dieses Prüfwerkzeug analysiert Marktabgrenzungen auf juristischer, ökonomischer und methodischer Ebene. Es unterstützt bei:

- **Fusionskontrolle:** FKVO-Verfahren Phase I/II, BKartA-Verfahren, SIEC-Test.
- **Missbrauchsverfahren:** Art. 102 AEUV / §§ 19–20 GWB; Marktbeherrschungsnachweis.
- **Kartellverbot:** Art. 101 AEUV / § 1 GWB; Spürbarkeit, Bagatell-Ausnahme.
- **Behördliche Stellungnahmen:** Stellungnahmen in BKartA- und Kommissionsverfahren.
- **Parteigutachten:** Kritische Würdigung gegnerischer Marktdefinitionen.

## Enthaltene Skills (25)

| Skill | Zweck |
| --- | --- |
| `marktabgrenzung-kontextanalyse` | Verfahrensart und Zielrichtung der Marktabgrenzung identifizieren, ergebnisgetriebene Argumentation erkennen |
| `produktmarkt-nachfragesubstitution` | Nachfragerseitige Austauschbarkeit prüfen — Funktionalität Preis Qualität Kundensegmente |
| `ssnip-test-anwendung` | SSNIP-Test vollständig durchführen — hypothetischer Monopolist kritischer Verlust Cellophane Fallacy |
| `produktmarkt-angebotsumstellung` | Supply-Side Substitution prüfen — Kurzfristigkeit Umstellungskosten regulatorische Hürden |
| `potenzieller-wettbewerb-marktzutritt` | Markteintrittsschranken und TLS-Analyse für potenziellen Wettbewerb |
| `mehrseitige-maerkte-plattformen` | Plattformmärkte und zweiseitige Märkte — Netzwerkeffekte getrennte vs. integrierte Marktdefinition |
| `cluster-und-systemmaerkte` | Clustermärkte und Aftermärkte — Pelikan-Doktrin Lock-in Primär- vs. Sekundärmarkt |
| `innovations-und-technologiemaerkte` | Innovationsmärkte FuE-Wettbewerb SEPs Patent-Pools dynamische Märkte |
| `raeumlicher-markt-abgrenzung` | Räumliche Marktdefinition — Preisstrukturen Handelsstöme Homogenität regulatorische Grenzen |
| `evidenz-qualitaet-bewertung` | Evidenz-Hierarchie — interne Dokumente Kundenverhalten Marktdaten Selektivitätsrisiko |
| `elastizitaeten-diversion-ratios` | Kreuzpreiselastizität und Diversion Ratio — ökonometrische Methodik Endogenität Robustheit |
| `konsistenzpruefung-marktdefinition` | Interne Widerspruchsfreiheit — Zirkelschluss-Check Konsistenz mit Behördenpraxis |
| `eugh-rechtsprechung-leitentscheidungen` | EuGH/EuG/BGH/BKartA-Leitentscheidungen mit Pinpoint-Zitaten |
| `paragraf-18-gwb-pruefung` | § 18 GWB Marktbeherrschung — Vermutungsregeln Abs 4 gemeinsame Beherrschung Plattformen Abs 3a |
| `fusionskontrolle-modus` | FKVO-Modus — Phase I/II SIEC-Test HHI Effizienzeinrede |
| `kartellverbot-modus` | Art 101 AEUV/§ 1 GWB — Spürbarkeit Bagatell Single-Brand GVOs |
| `missbrauchsverbot-modus` | Art 102 AEUV/§§ 19–20 GWB — Kampfpreise Margin Squeeze Refusal to Deal Self-Preferencing |
| `red-flags-checkliste` | Priorisierte Mängelliste — kritische erhebliche und mittlere Schwachstellen |
| `alternative-marktdefinition-eng` | Engere alternative Marktdefinition mit juristischer und ökonomischer Begründung |
| `alternative-marktdefinition-weit` | Weitere alternative Marktdefinition mit juristischer und ökonomischer Begründung |
| `auswirkungen-marktanteile-marktbeherrschung` | Marktanteil-Matrix bei alternativen Abgrenzungen — HHI Schaltereffekte rechtliche Konsequenzen |
| `gesamtbewertung-tragfaehigkeit` | Gesamturteil Tragfähigkeit hoch/mittel/gering — 3 bis 5 scharfe Schwachstellen prozesstaktische Empfehlung |
| `eu-bekanntmachung-marktdefinition-2024` | Neue EU-Bekanntmachung Februar 2024 — Inhalt Anwendung Vergleich zu 1997 |
| `dma-und-gatekeeper-markt` | Digital Markets Act 2022/1925 — Gatekeeper-Designierung Kernplattformdienste Auswirkung auf Kartellrecht |

## Referenzen

| Datei | Inhalt |
| --- | --- |
| `references/methodik-marktdefinition.md` | Umfassende Darstellung der Marktdefinitions-Methodik (SSNIP, Elastizitäten, Supply-Side, räumlicher Markt, Evidenz) |
| `references/eugh-leitentscheidungen.md` | Chronologische Entscheidungssammlung EuGH/EuG/BGH/BKartA mit Kernsätzen zur Marktdefinition |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Alle Aussagen beruhen auf der im Plugin hinterlegten Rechtsprechung und genannter Bekanntmachungsliteratur. Das Prüfwerkzeug ersetzt keine eigene anwaltliche Prüfung im Einzelfall. Kartellrechtliche Marktdefinitionen sind immer fallebhängig und können von der Behördenpraxis abweichen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 25 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Kartellrecht Marktabgrenzung Pruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen... |
| `alternative-marktdefinition-eng` | Mandant will eine engere Marktabgrenzung argumentieren um niedrigere Marktanteile oder fehlende Marktbeherrschung zu zeigen. Generiert engere alternative Marktdefinition mit juristischer und oekonomischer Begründung. Normen § 18 GWB Art.... |
| `alternative-marktdefinition-weit` | Mandant will eine weitere Marktabgrenzung argumentieren um niedrigere Marktanteile zu zeigen oder Behoerden-Markt anzugreifen. Generiert weitere alternative Marktdefinition mit juristischer und oekonomischer Begründung. Normen § 18 GWB A... |
| `auswirkungen-marktanteile-marktbeherrschung` | Wie aendert sich der Marktanteil des Mandanten je nachdem wie eng oder weit der Markt abgegrenzt wird. Quantifiziert Auswirkungen alternativer Marktabgrenzungen auf Marktanteile und Marktbeherrschungsvermutungen. Normen § 18 Abs. 4 GWB 4... |
| `cluster-und-systemmaerkte` | Behoerde oder Gegenseite argumentiert mit Cluster-Markt oder Aftermarkt-Doktrin oder Mandant will dies nutzen. Prüft Cluster-Maerkte Buendelung nicht-substitutiver Produkte und Systemmaerkte Primaermarkt plus Aftermarkt. Normen Art. 102... |
| `dma-und-gatekeeper-markt` | Digital Markets Act (VO 2022/1925): Gatekeeper-Designierung Kernplattformdienste quantitative und qualitative Schwellenwerte. Auswirkungen der DMA-Designierung auf die Marktdefinition in kartellrechtlichen Verfahren. Verhältnis DMA zu Ar... |
| `elastizitaeten-diversion-ratios` | Oekonomischer Gutachter oder Mandant legt Elastizitaetsdaten oder Diversion-Ratio-Analyse vor und Belastbarkeit ist zu prüfen. Prüft Eigenpreis-Elastizitaet Kreuzpreis-Elastizitaet und Diversion Ratios als Instrumente quantitativer Markt... |
| `eu-bekanntmachung-marktdefinition-2024` | Skill zur neuen EU-Kommissions-Bekanntmachung zur Marktdefinition (Februar 2024) und ihrer praktischen Anwendung. Vergleich zur Bekanntmachung von 1997. Neue Elemente: digitale Maerkte Innovationswettbewerb Datenmaerkte beidseitiger SSNI... |
| `eugh-rechtsprechung-leitentscheidungen` | Workflow-Skill zu eugh rechtsprechung leitentscheidungen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `evidenz-qualitaet-bewertung` | Bewertet die Qualitaet und Belastbarkeit der vorgelegten Belege für eine Marktabgrenzung: interne Unternehmensdokumente Kundenverhaltensdaten Marktdaten Elastizitaeten Diversion Ratios Branchenberichte. Erkennt selektive Datenwahl method... |
| `fusionskontrolle-modus` | Prüft Marktabgrenzung im Kontext der EU-Fusionskontrolle (FKVO 139/2004): Phase I und Phase II SIEC-Test (Significant Impediment to Effective Competition) horizontale und nicht-horizontale Fusionen Effizienzeinrede und Koordinierungseffe... |
| `gesamtbewertung-tragfaehigkeit` | Gesamturteil zur Tragfähigkeit einer Marktabgrenzung: hoch mittel oder gering. Fasst zentrale Schwachstellen in 3 bis 5 scharfen Punkten zusammen. Bewertet Angreifbarkeit vor Gericht oder Behoerde und empfiehlt prozesstaktische Konsequen... |
| `innovations-und-technologiemaerkte` | Marktabgrenzung in dynamischen Technologiemaerkten wo kuenftige Innovation den Wettbewerb praegt oder Patent-Pools streitig sind. Prüft Innovationsmaerkte technologische Substitution Standard-Essential-Patents FuE-Maerkte. Normen Art. 10... |
| `kartellverbot-modus` | Workflow-Skill zu kartellverbot modus. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `konsistenzpruefung-marktdefinition` | Prüft die interne Widerspruchsfreiheit einer Marktabgrenzung: Übereinstimmung von Sachmarkt und räumlichem Markt tatsaechlichem Marktverhalten Behoerdenpraxis und oekonomischen Grundprinzipien. Erkennt Zirkelschluesse und inkonsistente A... |
| `marktabgrenzung-kontextanalyse` | Verfahren beginnt und Verfahrensart und Parteistellung muessen bestimmt werden bevor die Marktabgrenzung-Analyse starten kann. Identifiziert Verfahrensart Fusionskontrolle Kartellverbot Missbrauchsverfahren und Zielrichtung der Marktabgr... |
| `mehrseitige-maerkte-plattformen` | Workflow-Skill zu mehrseitige maerkte plattformen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `missbrauchsverbot-modus` | Unternehmen in marktbeherrschender Stellung soll auf Missbrauch geprüft werden oder Wettbewerber klagt auf Missbrauch. Prüft Marktabgrenzung und Missbrauchstatbestaende Art. 102 AEUV § 19 GWB. Prüfraster Behinderungsmissbrauch (Kampfprei... |
| `paragraf-18-gwb-pruefung` | Prüft Marktbeherrschung nach Paragraf 18 GWB: Einzelmarktbeherrschung Abs 1 Marktanteils-Schwellen Abs 4 (40 Prozent) gemeinsame Marktbeherrschung Abs 5 und 6 intermediaere Plattformen Abs 3a sowie relative Marktmacht nach Paragraf 20 GW... |
| `potenzieller-wettbewerb-marktzutritt` | Behoerde oder Gegenseite argumentiert fehlende Markteintrittsbarrieren um Marktbeherrschung zu verneinen. Analysiert Markteintrittsschranken und Wahrscheinlichkeit potenziellen Wettbewerbs im Zeitrahmen 2 bis 3 Jahre. Normen Art. 102 AEU... |
| `produktmarkt-angebotsumstellung` | Prüft angebotsseitige Substitution (Supply-Side Substitution): Kann ein anderer Anbieter kurzfristig und ohne erhebliche Kosten auf den relevanten Markt wechseln? Bewertet Umstellungskosten regulatorische Anforderungen Zertifizierungen u... |
| `produktmarkt-nachfragesubstitution` | Kernschritt jeder Marktabgrenzung: sachlicher Markt aus Nachfragersicht bestimmen. Prüft funktionale Austauschbarkeit Preisreagibilitaet qualitative Unterschiede Verwendungszweck Bedarfsdeckungsaequivalenz. Normen § 18 GWB Art. 102 AEUV... |
| `raeumlicher-markt-abgrenzung` | Prüft den räumlich relevanten Markt: national europaeisch global. Analysiert Preisstrukturen Transportkosten regulatorische Unterschiede Homogenitaetsannahmen Handelsstroeme und Arbitragemoeaeglichkeiten. Bewertet ob nationale Marktdefin... |
| `red-flags-checkliste` | Strukturierte Checkliste problematischer Muster in Marktabgrenzungen: ergebnisgetriebene Argumentation Zirkelschluesse fehlende oekonomische Fundierung selektive Datenwahl kuenstliche Marktverengung oder -erweiterung und Präzedenzfall-Mi... |
| `ssnip-test-anwendung` | Sachlichen Markt mit dem SSNIP-Test abgrenzen ob ein hypothetischer Monopolist profitabel Preise um 5 bis 10 Prozent erhoehen koennte. Wendet Small but Significant Non-transitory Increase in Price Hypothetischer-Monopolisten-Test an. Nor... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

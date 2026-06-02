# Kartellrecht — Marktabgrenzungsprüfung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kartellrecht-marktabgrenzung-pruefung`) | [`kartellrecht-marktabgrenzung-pruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kartellrecht-marktabgrenzung-pruefung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Zusammenschlusskontrolle GBW / Tannenheim — Bahnbetonschwellen, Bußgeld, ECN+** (`kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen`) | [Gesamt-PDF lesen](../testakten/kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen/gesamt-pdf/kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen_gesamt.pdf) | [`testakte-kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kartell-zusammenschlusskontrolle-bahnbetonschwellen-grosskopf-westfalen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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

Automatisch generierte Komplett-Liste aller 126 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `1-gwb-kartellverbot-nationale-pruefung` | § 1 GWB Kartellverbot nationale Prüfung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720... |
| `19-gwb-behinderungs-ausbeutungsmissbrauch` | § 19 GWB Behinderungs Ausbeutungsmissbrauch: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022... |
| `19a-gwb-ueberragende-marktuebergreifende-bedeutung` | § 19a GWB überragende marktübergreifende Bedeutung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-G... |
| `20-gwb-relative-marktmacht` | § 20 GWB relative Marktmacht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizonta... |
| `alleinvertrieb-kundengruppen-gebietsschutz` | Alleinvertrieb Kundengruppen Gebietsschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Kartellrecht Marktabgrenzung Pruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen... |
| `alternative-marktdefinition-eng` | Mandant will eine engere Marktabgrenzung argumentieren um niedrigere Marktanteile oder fehlende Marktbeherrschung zu zeigen. Generiert engere alternative Marktdefinition mit juristischer und oekonomischer Begründung. Normen § 18 GWB Art.... |
| `alternative-marktdefinition-weit` | Mandant will eine weitere Marktabgrenzung argumentieren um niedrigere Marktanteile zu zeigen oder Behoerden-Markt anzugreifen. Generiert weitere alternative Marktdefinition mit juristischer und oekonomischer Begründung. Normen § 18 GWB A... |
| `anmeldepflicht-joint-venture` | Anmeldepflicht Joint Venture: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizonta... |
| `arbeitsmarkt-no-poach-wage-fixing` | Arbeitsmarkt No-Poach Wage-Fixing: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Hori... |
| `art-101-aeuv-kooperationspruefung-einstieg` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Art 101 AEUV Kooperationsprüfung Einstieg. |
| `art-101-aeuv-tatbestand-vereinbarung-beschluss-abgestimmte-verha` | Art 101 AEUV Tatbestand Vereinbarung Beschluss abgestimmte Verhaltensweise: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff.,... |
| `art-102-aeuv-marktbeherrschung-missbrauch` | Art 102 AEUV Marktbeherrschung Missbrauch: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/7... |
| `art-102-aeuv-missbrauchspruefung-einstieg` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Art 102 AEUV Missbrauchsprüfung Einstieg. |
| `auswirkungen-marktanteile-marktbeherrschung` | Wie aendert sich der Marktanteil des Mandanten je nachdem wie eng oder weit der Markt abgegrenzt wird. Quantifiziert Auswirkungen alternativer Marktabgrenzungen auf Marktanteile und Marktbeherrschungsvermutungen. Normen § 18 Abs. 4 GWB 4... |
| `bietergemeinschaft-vergabekartellrecht` | Bietergemeinschaft Vergabekartellrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720,... |
| `bussgeldbemessung-unternehmen-verband` | Bußgeldbemessung Unternehmen Verband: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, H... |
| `cluster-und-systemmaerkte` | Behoerde oder Gegenseite argumentiert mit Cluster-Markt oder Aftermarkt-Doktrin oder Mandant will dies nutzen. Prüft Cluster-Maerkte Buendelung nicht-substitutiver Produkte und Systemmaerkte Primaermarkt plus Aftermarkt. Normen Art. 102... |
| `compliance-programm-kartellrecht-mittelstand` | Compliance-Programm Kartellrecht Mittelstand: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 202... |
| `compliance-schulung-kartellrisiken` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Compliance-Schulung Kartellrisiken. |
| `datenzugang-und-interoperabilitaet` | Datenzugang und Interoperabilität: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Hori... |
| `dawn-raid-kartellbehoerde-sofortplan` | Dawn Raid Kartellbehörde Sofortplan: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Ho... |
| `de-minimis-inlandsauswirkung-fusionskontrolle` | De-minimis Inlandsauswirkung Fusionskontrolle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 20... |
| `disclosure-33g-gwb-akteneinsicht` | Disclosure § 33g GWB Akteneinsicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Hor... |
| `dma-schnittstelle-kartellrecht` | DMA Schnittstelle Kartellrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizon... |
| `dma-und-gatekeeper-markt` | Digital Markets Act (VO 2022/1925): Gatekeeper-Designierung Kernplattformdienste quantitative und qualitative Schwellenwerte. Auswirkungen der DMA-Designierung auf die Marktdefinition in kartellrechtlichen Verfahren. Verhältnis DMA zu Ar... |
| `einkaufskooperation-nachfragemacht` | Einkaufskooperation Nachfragemacht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Hor... |
| `einstweiliger-rechtsschutz-kartellrecht` | Einstweiliger Rechtsschutz Kartellrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720... |
| `elastizitaeten-diversion-ratios` | Oekonomischer Gutachter oder Mandant legt Elastizitaetsdaten oder Diversion-Ratio-Analyse vor und Belastbarkeit ist zu prüfen. Prüft Eigenpreis-Elastizitaet Kreuzpreis-Elastizitaet und Diversion Ratios als Instrumente quantitativer Markt... |
| `energiekartellrecht-netz-und-vertrieb` | Energiekartellrecht Netz und Vertrieb: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720,... |
| `eu-bekanntmachung-marktdefinition-2024` | Skill zur neuen EU-Kommissions-Bekanntmachung zur Marktdefinition (Februar 2024) und ihrer praktischen Anwendung. Vergleich zur Bekanntmachung von 1997. Neue Elemente: digitale Maerkte Innovationswettbewerb Datenmaerkte beidseitiger SSNI... |
| `eu-fusionskontrolle-fkvo-zustaendigkeit` | EU-Fusionskontrolle FKVO Zuständigkeit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720,... |
| `eugh-rechtsprechung-leitentscheidungen` | Workflow-Skill zu eugh rechtsprechung leitentscheidungen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `evidenz-qualitaet-bewertung` | Bewertet die Qualitaet und Belastbarkeit der vorgelegten Belege für eine Marktabgrenzung: interne Unternehmensdokumente Kundenverhaltensdaten Marktdaten Elastizitaeten Diversion Ratios Branchenberichte. Erkennt selektive Datenwahl method... |
| `exklusivitaetsrabatte-treuerabatte` | Exklusivitätsrabatte Treuerabatte: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Hori... |
| `follow-on-klage-bindungswirkung` | Follow-on Klage Bindungswirkung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizo... |
| `franchise-vertrag-kartellrecht` | Franchise-Vertrag Kartellrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizon... |
| `freistellung-art-101-abs-3-aeuv-effizienz-verbraucheranteil` | Freistellung Art 101 Abs 3 AEUV Effizienz Verbraucheranteil: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, V... |
| `fusionskontrolle-anmeldung-routing` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Fusionskontrolle Anmeldung Routing. |
| `fusionskontrolle-gwb-umsatzschwellen` | Fusionskontrolle GWB Umsatzschwellen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, H... |
| `fusionskontrolle-modus` | Prüft Marktabgrenzung im Kontext der EU-Fusionskontrolle (FKVO 139/2004): Phase I und Phase II SIEC-Test (Significant Impediment to Effective Competition) horizontale und nicht-horizontale Fusionen Effizienzeinrede und Koordinierungseffe... |
| `geoblocking-und-kartellrecht-schnittstelle` | Geoblocking und Kartellrecht Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/... |
| `gesamtbewertung-tragfaehigkeit` | Gesamturteil zur Tragfähigkeit einer Marktabgrenzung: hoch mittel oder gering. Fasst zentrale Schwachstellen in 3 bis 5 scharfen Punkten zusammen. Bewertet Angreifbarkeit vor Gericht oder Behoerde und empfiehlt prozesstaktische Konsequen... |
| `geschaeftsleiterhaftung-kartellverstoss` | Geschäftsleiterhaftung Kartellverstoß: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720,... |
| `handelsvertreterprivileg-echtes-unechtes-agenturmodell` | Handelsvertreterprivileg echtes unechtes Agenturmodell: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertik... |
| `healthcare-kartellrecht-kooperation-kliniken` | Healthcare Kartellrecht Kooperation Kliniken: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 202... |
| `horizontal-gvo-forschung-und-entwicklung` | Horizontal-GVO Forschung und Entwicklung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/72... |
| `horizontal-gvo-spezialisierung` | Horizontal-GVO Spezialisierung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizon... |
| `hub-and-spoke-kartell` | Hub-and-Spoke Kartell: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-GVO,... |
| `informationsaustausch-wettbewerber` | Informationsaustausch Wettbewerber: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Hor... |
| `innovations-und-technologiemaerkte` | Marktabgrenzung in dynamischen Technologiemaerkten wo kuenftige Innovation den Wettbewerb praegt oder Patent-Pools streitig sind. Prüft Innovationsmaerkte technologische Substitution Standard-Essential-Patents FuE-Maerkte. Normen Art. 10... |
| `kart-innovationswettbewerb-spezial` | Spezialfall Innovationswettbewerb und Killer Acquisitions: Pipeline-Produkte, Innovation Theory of Harm. Pruefraster fuer Fusionskontrollanmeldung. |
| `kart-marktanteilsanalyse-leitfaden` | Leitfaden Marktanteilsanalyse: Umsatz- und Mengenmarktanteile, HHI, Marktstrukturmerkmale. Pruefraster fuer Fusionskontrollmeldung. |
| `kart-marktdefinition-bauleiter` | Bauleiter Marktdefinition: sachlich, raeumlich, zeitlich. SSNIP-Test, Hypothetischer Monopolist, Mehrproduktmaerkte. Pruefraster fuer typische Branchen. |
| `kart-zweiseitige-plattformen-spezial` | Spezialfall zweiseitige Plattformen / Mehrseitige Maerkte: Netzwerkeffekte, Tipping, DMA-Gatekeeper. Pruefraster fuer Digitalplattformen. |
| `kartellrecht-kaltstart-mandat-neu` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Kartellrecht Kaltstart Mandat neu. |
| `kartellrechtliche-vertragsklausel-redline` | Kartellrechtliche Vertragsklausel-Redline: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/7... |
| `kartellschadensersatz-33a-gwb` | Kartellschadensersatz § 33a GWB: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizo... |
| `kartellverbot-modus` | Workflow-Skill zu kartellverbot modus. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `ki-preisgestaltung-kartellrecht` | KI Preisgestaltung Kartellrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizo... |
| `konsistenzpruefung-marktdefinition` | Prüft die interne Widerspruchsfreiheit einer Marktabgrenzung: Übereinstimmung von Sachmarkt und räumlichem Markt tatsaechlichem Marktverhalten Behoerdenpraxis und oekonomischen Grundprinzipien. Erkennt Zirkelschluesse und inkonsistente A... |
| `kronzeugenprogramm-bonusregelung` | Kronzeugenprogramm Bonusregelung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horiz... |
| `landwirtschaftliche-erzeugerkooperation` | Landwirtschaftliche Erzeugerkooperation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720... |
| `margin-squeeze-telekom-energie-plattform` | Margin Squeeze Telekom Energie Plattform: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/72... |
| `marktabgrenzung-kontextanalyse` | Verfahren beginnt und Verfahrensart und Parteistellung muessen bestimmt werden bevor die Marktabgrenzung-Analyse starten kann. Identifiziert Verfahrensart Fusionskontrolle Kartellverbot Missbrauchsverfahren und Zielrichtung der Marktabgr... |
| `mehrseitige-maerkte-plattformen` | Workflow-Skill zu mehrseitige maerkte plattformen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `ministererlaubnis-42-gwb` | Ministererlaubnis § 42 GWB: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-... |
| `missbrauchsverbot-modus` | Unternehmen in marktbeherrschender Stellung soll auf Missbrauch geprüft werden oder Wettbewerber klagt auf Missbrauch. Prüft Marktabgrenzung und Missbrauchstatbestaende Art. 102 AEUV § 19 GWB. Prüfraster Behinderungsmissbrauch (Kampfprei... |
| `nachhaltigkeitskooperation-wettbewerbsrecht` | Nachhaltigkeitskooperation Wettbewerbsrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022... |
| `nicht-horizontale-fusion-vertikal-konglomerat` | Nicht-horizontale Fusion vertikal konglomerat: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 20... |
| `paragraf-18-gwb-pruefung` | Prüft Marktbeherrschung nach Paragraf 18 GWB: Einzelmarktbeherrschung Abs 1 Marktanteils-Schwellen Abs 4 (40 Prozent) gemeinsame Marktbeherrschung Abs 5 und 6 intermediaere Plattformen Abs 3a sowie relative Marktmacht nach Paragraf 20 GW... |
| `passing-on-einwand-schadensweitergabe` | Passing-on Einwand Schadensweitergabe: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720,... |
| `potenzieller-wettbewerb-marktzutritt` | Behoerde oder Gegenseite argumentiert fehlende Markteintrittsbarrieren um Marktbeherrschung zu verneinen. Analysiert Markteintrittsschranken und Wahrscheinlichkeit potenziellen Wettbewerbs im Zeitrahmen 2 bis 3 Jahre. Normen Art. 102 AEU... |
| `predatory-pricing-kampfpreise` | Predatory Pricing Kampfpreise: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizont... |
| `preisalgorithmen-kollusives-risiko` | Preisalgorithmen kollusives Risiko: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Hor... |
| `preisbindung-der-zweiten-hand-rpm` | Preisbindung der zweiten Hand RPM: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Hori... |
| `presseverlage-plattformen-leistungsschutz-schnittstelle` | Presseverlage Plattformen Leistungsschutz Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Verti... |
| `private-enforcement-schadensersatz-intake` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Private Enforcement Schadensersatz Intake. |
| `produktmarkt-angebotsumstellung` | Prüft angebotsseitige Substitution (Supply-Side Substitution): Kann ein anderer Anbieter kurzfristig und ohne erhebliche Kosten auf den relevanten Markt wechseln? Bewertet Umstellungskosten regulatorische Anforderungen Zertifizierungen u... |
| `produktmarkt-nachfragesubstitution` | Kernschritt jeder Marktabgrenzung: sachlicher Markt aus Nachfragersicht bestimmen. Prüft funktionale Austauschbarkeit Preisreagibilitaet qualitative Unterschiede Verwendungszweck Bedarfsdeckungsaequivalenz. Normen § 18 GWB Art. 102 AEUV... |
| `raeumlicher-markt-abgrenzung` | Prüft den räumlich relevanten Markt: national europaeisch global. Analysiert Preisstrukturen Transportkosten regulatorische Unterschiede Homogenitaetsannahmen Handelsstroeme und Arbitragemoeaeglichkeiten. Bewertet ob nationale Marktdefin... |
| `red-flags-checkliste` | Strukturierte Checkliste problematischer Muster in Marktabgrenzungen: ergebnisgetriebene Argumentation Zirkelschluesse fehlende oekonomische Fundierung selektive Datenwahl kuenstliche Marktverengung oder -erweiterung und Präzedenzfall-Mi... |
| `refusal-to-supply-essential-facilities` | Refusal to Supply Essential Facilities: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720,... |
| `remedies-zusagen-veraeusserung-zugang` | Remedies Zusagen Veräußerung Zugang: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Ho... |
| `sammelklagen-abtretungsmodelle-kartellschaden` | Sammelklagen Abtretungsmodelle Kartellschaden: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 20... |
| `schiedsverfahren-kartellrecht-einwand-nichtigkeit` | Schiedsverfahren Kartellrecht Einwand Nichtigkeit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GV... |
| `selektivvertrieb-luxus-internetplattform` | Selektivvertrieb Luxus Internetplattform: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/72... |
| `self-preferencing-plattformen` | Self-Preferencing Plattformen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizont... |
| `sep-frand-kartellrecht` | SEP FRAND Kartellrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-GVO,... |
| `siec-test-horizontale-fusion` | SIEC-Test horizontale Fusion: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizonta... |
| `spezial-aeuv-behoerden-gericht-und-registerweg` | Aeuv: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-angebotsumstellung-zahlen-schwellen-und-berechnung` | Angebotsumstellung: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-evidenz-internationaler-bezug-und-schnittstellen` | Evidenz: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-flags-red-team-und-qualitaetskontrolle` | Flags: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kartellrechtliche-tatbestand-beweis-und-belege` | Kartellrechtliche: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-konsistenz-formular-portal-und-einreichung` | Konsistenz: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kritische-erstpruefung-und-mandatsziel` | Kritische: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-markt-mehrparteien-konflikt-und-interessen` | Markt: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-marktabgrenzungen-dokumentenmatrix-und-lueckenliste` | Marktabgrenzungen: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-marktbeherrschung-mandantenentscheidung` | Marktbeherrschung: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-nachfrage-livequellen-und-rechtsprechungscheck` | Nachfrage: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-paragraf-risikoampel-und-gegenargumente` | Paragraf: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pruefinstanz-fristen-form-und-zustaendigkeit` | Pruefinstanz: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-raeumlicher-compliance-dokumentation-und-akte` | Raeumlicher: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsprechung-beweislast-und-darlegungslast` | Rechtsprechung: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ssnip-schriftsatz-brief-und-memo-bausteine` | Ssnip: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-test-verhandlung-vergleich-und-eskalation` | Test: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `sportkartellrecht-verbandsregeln` | Sportkartellrecht Verbandsregeln: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horiz... |
| `spuerbarkeit-und-zwischenstaatlichkeit` | Spürbarkeit und Zwischenstaatlichkeit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720,... |
| `ssnip-test-anwendung` | Sachlichen Markt mit dem SSNIP-Test abgrenzen ob ein hypothetischer Monopolist profitabel Preise um 5 bis 10 Prozent erhoehen koennte. Wendet Small but Significant Non-transitory Increase in Price Hypothetischer-Monopolisten-Test an. Nor... |
| `transaktionswertschwelle-35-abs-1a-gwb` | Transaktionswertschwelle § 35 Abs 1a GWB: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/72... |
| `verbandsarbeit-informationsaustausch-grenzen` | Verbandsarbeit Informationsaustausch Grenzen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 202... |
| `vergleichsvereinbarung-patent-settlement-pay-for-delay` | Vergleichsvereinbarung Patent Settlement Pay-for-delay: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertik... |
| `verjaehrung-kartellschaden-33h-gwb` | Verjährung Kartellschaden § 33h GWB: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Ho... |
| `vertikal-gvo-2022-720-vertriebsvertraege` | Vertikal-GVO 2022/720 Vertriebsverträge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720... |
| `vertikale-leitlinien-eu-selektiver-vertrieb-plattformverbote` | Vertikale Leitlinien EU selektiver Vertrieb Plattformverbote: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO,... |
| `verweisung-art-4-9-22-fkvo` | Verweisung Art 4 9 22 FKVO: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-... |
| `vollzugsverbot-gun-jumping` | Vollzugsverbot Gun Jumping: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin kartellrecht-marktabgrenzung-pruefung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin kartellrecht-marktabgrenzung-pruefung: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin kartellrecht-marktabgrenzung-pruefung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin kartellrecht-marktabgrenzung-pruefung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin kartellrecht-marktabgrenzung-pruefung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin kartellrecht-marktabgrenzung-pruefung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin kartellrecht-marktabgrenzung-pruefung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin kartellrecht-marktabgrenzung-pruefung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

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

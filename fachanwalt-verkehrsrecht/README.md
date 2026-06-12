# Fachanwalt Verkehrsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`fachanwalt-verkehrsrecht.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/fachanwalt-verkehrsrecht.md) (57 KB)
- Im Repo: [`testakten/megaprompts/fachanwalt-verkehrsrecht.md`](../testakten/megaprompts/fachanwalt-verkehrsrecht.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

### Formatvorlagen (Markdown + ODT)

Sofort verwendbare Vorlagen (Times Roman 11pt, A4, mit Disclaimer und Feldern in [Klammern]). Markdown zum Lesen / Anpassen, ODT zum Bearbeiten in LibreOffice/Word.

| Vorlage | Markdown | ODT |
| --- | --- | --- |
| Einspruch Bussgeldbescheid Paragraf 67 Owig | [`.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-verkehrsrecht/einspruch-bussgeldbescheid-paragraf-67-owig.md) | [`.odt`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-verkehrsrecht/einspruch-bussgeldbescheid-paragraf-67-owig.odt) |

*Experimentelle KI-Vorlagen — keine Haftung. Vor Verwendung im Mandat anwaltlich prüfen und an konkreten Fall anpassen.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-verkehrsrecht`) | [`fachanwalt-verkehrsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-verkehrsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **StVO-Akte Schulstraße/Lieferzone** (`strassenverkehrsrecht-stvo-schulstrasse-lieferzone`) | [Gesamt-PDF lesen](../testakten/strassenverkehrsrecht-stvo-schulstrasse-lieferzone/gesamt-pdf/strassenverkehrsrecht-stvo-schulstrasse-lieferzone_gesamt.pdf) | [`testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip) |
| **Verkehrsunfall Tannenbruck — A45 Quotenstreit, OWi, Fahrerlaubnis-Entzug, MPU** (`verkehrsunfall-quotenstreit-tannenbruck-a45`) | [Gesamt-PDF lesen](../testakten/verkehrsunfall-quotenstreit-tannenbruck-a45/gesamt-pdf/verkehrsunfall-quotenstreit-tannenbruck-a45_gesamt.pdf) | [`testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

## Anwalts-Dashboard für den Schnelleinstieg

Der Skill `einstieg-routing` ist das Anwalts-Dashboard zu diesem Plugin:
Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch,
Zustaendigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs,
Norm-Radar, Leitentscheidungs-Anker und genau eine Rueckfrage - bei
klarer Faktenlage sofort zum Spezial-Skill. Der Anwalt bleibt im Driver Seat.

Konvention: [`references/anwalts-dashboard-konvention.md`](../references/anwalts-dashboard-konvention.md)
| Quellen-Anker: [`references/leitentscheidungen-anker.md`](../references/leitentscheidungen-anker.md)
| Quellenhygiene: [`references/quellenhygiene.md`](../references/quellenhygiene.md).


Plugin Fachanwalt für Verkehrsrecht. Orientierung StVG StVO PflVG VVG-Bezüge. Verkehrsunfall Personenschaden Sachschaden Bußgeld Fahrerlaubnis OWi-Verfahren Verkehrsstrafrecht (§§ 315c 316 StGB). Schnittstellen zu Versicherungs- und Strafrecht.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-verkehrsrecht-orientierung` | Orientierung im Verkehrsrecht — FAO Voraussetzungen Normen typische Mandate Fristen Quellenprüfung. Verkehrsunfall mit Personen- und Sachschaden Schadensregulierung Versicherung Haftpflicht Kasko Bußgeld Fahrerlau… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 64 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `315c-internationaler-bezug-und-schnittstellen` | 315C: Internationaler Bezug und Schnittstellen: 315C: Internationaler Bezug und Schnittstellen. |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Verkehrsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 67 OWiG Einspruch 2 Wochen, Bußgeldbescheid, Polizeiprotokoll, Anhörungsbogen), dokumentiert Router-Entscheidung mit Begründung. |
| `autonom-abschlussprodukt-und-uebergabe` | Autonom: Abschlussprodukt und Übergabe: Autonom: Abschlussprodukt und Übergabe. |
| `bezuege-behoerden-gericht-und-registerweg` | Bezuege: Behörden-, Gerichts- oder Registerweg: Bezuege: Behörden-, Gerichts- oder Registerweg. |
| `blitzer-messung-paragraf-3-stvo` | Blitzer Messung § 3 StVO: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `bussgeld-einspruch-pruefen` | Bussgeld Einspruch Prüfen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Bussgeld Einspruch Prüfen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprec... |
| `bussgeld-zahlen-schwellen-und-berechnung` | Bussgeld: Zahlen, Schwellenwerte und Berechnung: Bussgeld: Zahlen, Schwellenwerte und Berechnung. |
| `bussgeldbescheid-pruefen` | Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist: OWiG §§ 65 ff. StVG § 26 Abs. 3 Verjährung. Prüfraster: Form- und Verfahrensfehler Verj... |
| `dieselskandal-paragraf-826-bgb` | Dieselskandal § 826 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Verkehrsrecht: sortiert Bußgeldbescheid, Polizeiprotokoll, Anhörungsbogen, prüft Datum, Absender, Frist und Beweiswert (Messprotokoll, Eichschein); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `einstieg-in-den-skill-verbund-verkehrsrecht` | Einstieg in den Skill-Verbund Verkehrsrecht: Orientierung im Verkehrsrecht FAO Voraussetzungen §§ 14g bis 14i FAO Verkehrsrecht. Typische Mandate Verkehrsunfall Schadensregulierung OWi-Bußgeld Fahrerlaubnis MPU V... |
| `einstieg-routing` | Anwalts-Dashboard Fachanwalt Verkehrsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt... |
| `einstieg-schnelltriage-fallrouting` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Verkehrsrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus die... |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen:... |
| `erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel. |
| `fahrerlaubnis-compliance-dokumentation-und-akte` | Fahrerlaubnis: Compliance-Dokumentation und Aktenvermerk: Fahrerlaubnis: Compliance-Dokumentation und Aktenvermerk. |
| `fahrerlaubnis-entzug` | Mandant hat Führerschein entzogen bekommen oder befürchtet Entziehung und fragt nach Möglichkeiten: § 69 StGB strafgerichtlich § 3 StVG verwaltungsrechtlich.... |
| `fahrerlaubnis-entzug-paragraf-3-stvg` | Fahrerlaubnis Entzug § 3 StVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `haftpflicht-paragraf-115-vvg` | Haftpflicht § 115 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `kanzlei-mandantenkommunikation-entscheidungsvorlage` | Kanzlei: Mandantenkommunikation und Entscheidungsvorlage: Kanzlei: Mandantenkommunikation und Entscheidungsvorlage. |
| `kaskoversicherung-paragraf-81-vvg-bgh-iv-zr-25-21` | Kaskoversicherung Paragraf 81 Vvg BGH Iv Zr 25 21: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `kfz-handel-paragraf-434-bgb` | kfz Handel § 434 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `mandat-triage-verkehrsrecht` | Neues Verkehrsrechtsmandat kommt rein und Anwalt muss Sachgebiet klären und Fristen prüfen: Eingangs-Triage Verkehrsrecht. Prüfraster: Verfahrensart (Zivilrecht Sc... |
| `mpu-vorbereitung` | Mandant muss MPU ablegen und fragt wie er sich vorbereiten soll: MPU Medizinisch-Psychologische Untersuchung Fahrerlaubnisrecht. Prüfraster: Anlass Alkohol Drogen Punkte Aggression zugelassene... |
| `output-waehlen` | Output-Wahl für Fachanwalt Verkehrsrecht: stimmt Adressat (Betroffener/Geschädigter, Behörde, Versicherer), Frist (§ 67 OWiG Einspruch 2 Wochen) und Form auf den Zweck ab — typische Outputs: Einspruch OWi, Strafbefehlseinspruch, MPU-Bera... |
| `personen-verhandlung-vergleich-und-eskalation` | Personen: Verhandlung, Vergleich und Eskalation: Personen: Verhandlung, Vergleich und Eskalation. |
| `personenschaden-paragraf-249-bgb` | Personenschaden § 249 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `pflvg-risikoampel-und-gegenargumente` | Pflvg: Risikoampel, Gegenargumente und Verteidigungslinien: Pflvg: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `punkte-fahrerlaubnis-paragraf-4-stvg-bverwg-3-c-25-19` | Punkte Fahrerlaubnis Paragraf 4 Stvg BVerwG 3 C 25 19: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Verkehrsrecht: prüft Normen (StGB §§ 142/315c, 316, StVG, StVO) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt AG (Bußgeld + Straf) und Quellenhygiene nach references/quellenhygi... |
| `quoten-sonderfall-edge-case` | Quoten: Sonderfall und Edge-Case-Prüfung: Quoten: Sonderfall und Edge-Case-Prüfung. |
| `regulierungsanforderung` | Mandant hat Verkehrsunfall und fordert Schadensersatz vom Haftpflichtversicherer des Unfallverursachers: § 115 VVG Direktanspruch §§ 7 17 StVG § 823 BGB... |
| `sachschaden-quellenkarte` | Sachschaden Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `schmerzensgeld-paragraf-253-bgb` | Schmerzensgeld § 253 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `schnittstelle-fehlerkatalog` | Schnittstelle Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Klage Verkehrsunfall, Einspruch OWi-Bußgeldbescheid, Klage KFZ-Versicherung: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau: Substantiiert... |
| `stgb-formular-portal-und-einreichung` | Stgb: Formular, Portal und Einreichungslogik: Stgb: Formular, Portal und Einreichungslogik. |
| `stvg-fristen-form-und-zustaendigkeit` | Stvg: Fristen, Form, Zuständigkeit und Rechtsweg: Stvg: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `stvo-dokumentenmatrix-und-lueckenliste` | Stvo: Dokumentenmatrix, Lückenliste und Nachforderung: Stvo: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `tempo-messung-beweis` | Mandant bestreitet korrekte Geschwindigkeitsmessung in Bußgeldbescheid: Tempo-Messung Beweisanfechtung OWiG. Prüfraster: Standardmessgeräte PoliScan Speed Es 3.0 LeivTec XV-3 Multanova... |
| `unfall-haftungsquote-berechnen` | Mandant hatte Verkehrsunfall und fragt: Wer haftet wie viel und welche Schadensposten können geltend gemacht werden? §§ 7 17 18 StVG iVm § 254 BGB Haftungsquote: Mandant hatte Verkehrsunfall und fragt: Wer haftet wie viel und welche Sch... |
| `unfallregulierung-beweislast-und-darlegungslast` | Unfallregulierung: Beweislast, Darlegungslast und Substantiierung: Unfallregulierung: Beweislast, Darlegungslast und Substantiierung. |
| `unfallregulierung-quoten` | Mandant hat Unfall mit Mitverschulden und fragt welche Schadensposten zu welcher Quote durchsetzbar sind: § 254 BGB Mitverschulden Quoten-Modelle. Prüf... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Verkehrsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Bußgeldbescheid, Polizeiprotokoll, Anhörungsbogen), nennt pro Lücke Beweisthema, Beschaffungsweg (AG (Bußgeld + Straf)), Frist u... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht): ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich): Ver... |
| `verk-fahrerlaubnisrecht-leitfaden` | Leitfaden Fahrerlaubnisrecht: Entziehung, MPU, Sperrfrist, vorzeitige Wiedererteilung: Prüfraster FeV-Begutachtung und Klage gegen Fahrerlaubnisbehoerde. |
| `verk-fahrtenbuch-anordnung-spezial` | Spezialfall Fahrtenbuchanordnung § 31a StVZO: Voraussetzungen, Ermessen, Mitwirkung, Verhältnismäßigkeit: Prüfraster für Widerspruch und Klage. |
| `verk-trunkenheit-drogenfahrt-spezial` | Spezialfall Trunkenheits- und Drogenfahrt: § 24a StVG OWi, § 316 StGB, relative und absolute Fahruntuechtigkeit, BAK-Werte, Cannabis-Grenzwert Reform 2024: Spezialfall Trunkenheits- und Drogenfahrt: § 24a StVG OWi, § 316 StGB, relative u... |
| `verk-unfallregulierung-workflow` | Unfallregulierung: Anspruchsgrundlagen § 7 StVG / § 18 StVG / § 823 BGB / § 115 VVG, Quote, Schadenspositionen Wiederbeschaffungswert, Wertminderung, Nutzungsausfall: Unfallregulierung: Anspruchsgrundlagen § 7 StVG / § 18 StVG / § 823 BG... |
| `verkehr-autonom-1d-stvg` | Unfall mit autonomem Fahrzeug oder Frage zur Haftung bei automatisiertem Fahren: § 1d StVG autonomes Fahren Level 4. Prüfraster: Haftungsverteilung Halter § 7 StVG Fahrer § 18... |
| `verkehr-fristennotiz-und-naechster-schritt` | Verkehr: Fristennotiz und nächster Schritt: Verkehr: Fristennotiz und nächster Schritt. |
| `verkehrsrecht-tatbestand-beweis-und-belege` | Verkehrsrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage: Verkehrsrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `verkehrsstrafrecht-mehrparteien-konflikt-und-interessen` | Verkehrsstrafrecht: Mehrparteienkonflikt und Interessenmatrix: Verkehrsstrafrecht: Mehrparteienkonflikt und Interessenmatrix. |
| `verkehrsunfall-paragraf-7-stvg` | Verkehrsunfall § 7 StVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `verkehrsunfall-schriftsatz-brief-und-memo-bausteine` | Verkehrsunfall: Schriftsatz-, Brief- und Memo-Bausteine: Verkehrsunfall: Schriftsatz-, Brief- und Memo-Bausteine. |
| `versicherer-quotenverhandlung-vergleich` | Versicherer hat Regulierung angeboten und Anwalt verhandelt Quotenerhöhung oder Vergleich: Versicherer-Verhandlung Unfallregulierung. Prüfraster: Mitverschuldensquote... |
| `vkr-blitzer-messverfahren-spezial` | Spezialfall Blitzer- und Messverfahren: standardisiertes Messverfahren, Rohmessdaten-Recht des Verteidigers (BVerfG 2 BvR 1167/20), Verwertbarkeit, Beweisantrag Sachverstaendigengutachten: Spezialfall Blitzer- und Messverfahren: standard... |
| `vkr-bussgeldverfahren-grundzuege` | Bussgeldverfahren Grundzuege: Anhörungsbogen, Einspruch innerhalb 2 Wochen, Hauptverhandlung Amtsgericht, Rechtsbeschwerde OLG nach §§ 79 ff: Bussgeldverfahren Grundzuege: Anhörungsbogen, Einspruch innerhalb 2 Wochen, Hauptverhandlung Am... |
| `vkr-einfuehrung-rechtsfelder` | Verkehrsrecht einfuehrend: Verkehrsstrafrecht (Trunkenheit § 316 StGB, Gefaehrdung § 315c StGB, Unfallflucht § 142 StGB), OWi (Bussgeldverfahren), Haftpflicht, Kasko, Fuehrerscheinrecht, FeV, MPU: Verkehrsrecht einfuehrend: Verkehrsstraf... |
| `vkr-totalschaden-fiktiv-spezial` | Spezialfall fiktive Abrechnung beim Totalschaden: Wiederbeschaffungswert minus Restwert, 130-Prozent-Grenze BGH, Verweisung auf guenstigere Reparaturen (BGH-Verweisrechtsprechung): Spezialfall fiktive Abrechnung beim Totalschaden: Wieder... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

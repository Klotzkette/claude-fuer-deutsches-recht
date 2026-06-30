# Fachanwalt Verkehrsrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Plugin Fachanwalt für Verkehrsrecht. StVG StVO PflVG VVG-Bezüge. Verkehrsunfall Personen- und Sachschaden Bußgeld Fahrerlaubnis Verkehrsstrafrecht (§§ 315c 316 StGB). Schnittstelle Plugin kanzlei-allgemein.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`fachanwalt-verkehrsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-verkehrsrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fachanwalt-verkehrsrecht/fachanwalt-verkehrsrecht-werkstatt.md" download><code>fachanwalt-verkehrsrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fachanwalt-verkehrsrecht/fachanwalt-verkehrsrecht-schnellstart.md" download><code>fachanwalt-verkehrsrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | StVO-Akte Schulstraße/Lieferzone: [Gesamt-PDF](../testakten/strassenverkehrsrecht-stvo-schulstrasse-lieferzone/gesamt-pdf/strassenverkehrsrecht-stvo-schulstrasse-lieferzone_gesamt.pdf), [`testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip), [`testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone-einzelpdfs.zip); Verkehrsunfall Tannenbruck — A45 Quotenstreit, OWi, Fahrerlaubnis-Entzug, MPU: [Gesamt-PDF](../testakten/verkehrsunfall-quotenstreit-tannenbruck-a45/gesamt-pdf/verkehrsunfall-quotenstreit-tannenbruck-a45_gesamt.pdf), [`testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip), [`testakte-verkehrsunfall-quotenstreit-tannenbruck-a45-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsunfall-quotenstreit-tannenbruck-a45-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
## Anwalts-Dashboard für den Schnelleinstieg

Der Skill `einstieg-routing` ist das Anwalts-Dashboard zu diesem Plugin:
Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch,
Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs,
Norm-Radar, Leitentscheidungs-Anker und genau eine Rueckfrage - bei
klarer Faktenlage sofort zum Spezial-Skill. Der Anwalt bleibt im Driver Seat.

Konvention: [`Install from .zip`](../references/anwalts-dashboard-konvention.md)
| Quellen-Anker: [`references/leitentscheidungen-anker.md`](../references/leitentscheidungen-anker.md)
| Quellenhygiene: [`references/quellenhygiene.md`](../references/quellenhygiene.md).


Plugin Fachanwalt für Verkehrsrecht. Orientierung StVG StVO PflVG VVG-Bezüge. Verkehrsunfall Personenschaden Sachschaden Bußgeld Fahrerlaubnis OWi-Verfahren Verkehrsstrafrecht (§§ 315c 316 StGB). Schnittstellen zu Versicherungs- und Strafrecht.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-verkehrsrecht-orientierung` | Orientierung im Verkehrsrecht — FAO Voraussetzungen Normen typische Mandate Fristen Quellenprüfung. Verkehrsunfall mit Personen- und Sachschaden Schadensregulierung Versicherung Haftpflicht Kasko Bußgeld Fahrerlau… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 77 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `315c-internationaler-bezug-und-schnittstellen` | 315C: Internationaler Bezug und Schnittstellen: 315C: Internationaler Bezug und Schnittstellen. |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Verkehrsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 67 OWiG Einspruch 2 Wochen, Bußgeldbescheid, Polizeiprotokoll, Anhörungsbogen), dokumentiert Router-Entscheidung mit Begründung. |
| `autonom-abschlussprodukt-und-uebergabe` | Autonom: Abschlussprodukt und Übergabe: Autonom: Abschlussprodukt und Übergabe. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `bezuege-behoerden-gericht-und-registerweg` | Bezuege: Behörden-, Gerichts- oder Registerweg: Bezuege: Behörden-, Gerichts- oder Registerweg. |
| `blitzer-messung-paragraf-3-stvo` | Blitzer Messung § 3 StVO: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `bussgeld-einspruch-pruefen` | Bussgeld Einspruch Prüfen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Bussgeld Einspruch Prüfen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechu... |
| `bussgeld-zahlen-schwellen-und-berechnung` | Bussgeld: Zahlen, Schwellenwerte und Berechnung: Bussgeld: Zahlen, Schwellenwerte und Berechnung. |
| `bussgeldbescheid-pruefen` | Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist: OWiG §§ 65 ff. StVG § 26 Abs. 3 Verjährung. Prüfraster: Form- und Verfahrensfehler Verj... |
| `dieselskandal-paragraf-826-bgb` | Dieselskandal § 826 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Verkehrsrecht: sortiert Bußgeldbescheid, Polizeiprotokoll, Anhörungsbogen, prüft Datum, Absender, Frist und Beweiswert (Messprotokoll, Eichschein); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `einstieg-in-den-skill-verbund-verkehrsrecht` | Einstieg in den Skill-Verbund Verkehrsrecht: Orientierung im Verkehrsrecht FAO Voraussetzungen §§ 14g bis 14i FAO Verkehrsrecht. Typische Mandate Verkehrsunfall Schadensregulierung OWi-Bußgeld Fahrerlaubnis MPU V... |
| `einstieg-routing` | Anwalts-Dashboard Fachanwalt Verkehrsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt... |
| `einstieg-schnelltriage-fallrouting` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Verkehrsrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus die... |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen:... |
| `erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel. |
| `fachanwalt-verkehr-autonom-1d-stvg` | Unfall mit autonomem Fahrzeug oder Frage zur Haftung bei automatisiertem Fahren. § 1d StVG autonomes Fahren Level 4. Prüfraster: Haftungsverteilung Halter § 7 StVG Fahrer § 18 StVG Hersteller § 1 ProdHaftG Datensaetze Black-Box § 1g StVG... |
| `fachanwalt-verkehrsrecht-bussgeldbescheid-pruefen` | Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist. OWiG §§ 65 ff. StVG § 26 Abs. 3 Verjährung. Prüfraster: Form- und Verfahrensfehler Verjährung 3 Monate ab Tat unterbrochen § 33 OWiG Messverfahren stand... |
| `fachanwalt-verkehrsrecht-fahrerlaubnis-entzug` | Mandant hat Führerschein entzogen bekommen oder befuerchtet Entziehung und fragt nach Möglichkeiten. § 69 StGB strafgerichtlich § 3 StVG verwaltungsrechtlich. Prüfraster: Sperrfrist § 69a StGB vorlaeufige Entziehung § 111a StPO Wiederert... |
| `fachanwalt-verkehrsrecht-mpu-vorbereitung` | Mandant muss MPU ablegen und fragt wie er sich vorbereiten soll. MPU Medizinisch-Psychologische Untersuchung Fahrerlaubnisrecht. Prüfraster: Anlass Alkohol Drogen Punkte Aggression zugelassene Begutachtungsstellen § 66 FeV Vorbereitungsk... |
| `fachanwalt-verkehrsrecht-orientierung` | Einstieg in den Skill-Verbund Verkehrsrecht. Orientierung im Verkehrsrecht FAO Voraussetzungen §§ 14g bis 14i FAO Verkehrsrecht. Typische Mandate Verkehrsunfall Schadensregulierung OWi-Bußgeld Fahrerlaubnis MPU Verkehrsstrafrecht §§ 315c... |
| `fachanwalt-verkehrsrecht-regulierungsanforderung` | Mandant hat Verkehrsunfall und fordert Schadensersatz vom Haftpflichtversicherer des Unfallverursachers. § 115 VVG Direktanspruch §§ 7 17 StVG § 823 BGB. Prüfraster: Direktanspruch Reparatur vs. fiktive Abrechnung Wiederbeschaffungswert... |
| `fachanwalt-verkehrsrecht-tempo-messung-beweis` | Mandant bestreitet korrekte Geschwindigkeitsmessung in Bußgeldbescheid. Tempo-Messung Beweisanfechtung OWiG. Prüfraster: Standardmessgeräte PoliScan Speed Es 3.0 LeivTec XV-3 Multanova PTB-Zulassung Eichschein Messdokumentation Messverfa... |
| `fachanwalt-verkehrsrecht-unfallregulierung-quoten` | Mandant hat Unfall mit Mitverschulden und fragt welche Schadensposten zu welcher Quote durchsetzbar sind. § 254 BGB Mitverschulden Quoten-Modelle. Prüfraster: Schadenstabellen Reparatur Mietwagen Wertminderung Nutzungsausfall Schmerzensg... |
| `fachanwalt-verkehrsrecht-versicherer-quotenverhandlung-vergleich` | Versicherer hat Regulierung angeboten und Anwalt verhandelt Quotenerhöhung oder Vergleich. Versicherer-Verhandlung Unfallregulierung. Prüfraster: Mitverschuldensquote § 254 BGB vorgerichtliche Korrespondenz Schmerzensgeld-Tabellen gerich... |
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
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Verkehrsrecht: prüft Normen (StGB §§ 142/315c und 316, StVG, StVO) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt AG (Bußgeld + Straf) und Quellenhygiene nach references/quellenh... |
| `quoten-sonderfall-edge-case` | Quoten: Sonderfall und Edge-Case-Prüfung: Quoten: Sonderfall und Edge-Case-Prüfung. |
| `regulierungsanforderung` | Mandant hat Verkehrsunfall und fordert Schadensersatz vom Haftpflichtversicherer des Unfallverursachers: § 115 VVG Direktanspruch §§ 7 17 StVG § 823 BGB... |
| `sachschaden-quellenkarte` | Sachschaden Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `schmerzensgeld-paragraf-253-bgb` | Schmerzensgeld § 253 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `schnittstelle-fehlerkatalog` | Schnittstelle Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Klage Verkehrsunfall, Einspruch OWi-Bußgeldbescheid, Klage KFZ-Versicherung: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau: Substantiiert... |
| `spezial-sachschaden-livequellen-und-rechtsprechungscheck` | Sachschaden: Livequellen- und Rechtsprechungscheck. |
| `spezial-schnittstelle-red-team-und-qualitaetskontrolle` | Schnittstelle: Red-Team und Qualitätskontrolle. |
| `stgb-formular-portal-und-einreichung` | Stgb: Formular, Portal und Einreichungslogik: Stgb: Formular, Portal und Einreichungslogik. |
| `stvg-fristen-form-und-zustaendigkeit` | Stvg: Fristen, Form, Zuständigkeit und Rechtsweg: Stvg: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `stvo-dokumentenmatrix-und-lueckenliste` | Stvo: Dokumentenmatrix, Lückenliste und Nachforderung: Stvo: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `tempo-messung-beweis` | Mandant bestreitet korrekte Geschwindigkeitsmessung in Bußgeldbescheid: Tempo-Messung Beweisanfechtung OWiG. Prüfraster: Standardmessgeräte PoliScan Speed Es 3.0 LeivTec XV-3 Multanova... |
| `unfall-haftungsquote-berechnen` | Mandant hatte Verkehrsunfall und fragt: Wer haftet wie viel und welche Schadensposten koennen geltend gemacht werden? §§ 7 17 18 StVG iVm § 254 BGB Haftungsquote: Mandant hatte Verkehrsunfall und fragt: Wer haftet wie viel und welche Sch... |
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
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

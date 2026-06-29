# Umweltrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes Umweltrecht-Plugin für BImSchG, TEHG, Abfall, Wasser, Boden, Naturschutz, UIG, Verfahren, Bußgeld, Umwelt-Due-Diligence, Klimaklagen UmwRG, Lieferkettensorgfalt LkSG/CSDDD und ESG-Greenwashing/CSRD.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`umweltrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/umweltrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/umweltrecht-werkstatt.md" download><code>umweltrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/umweltrecht-schnellstart.md" download><code>umweltrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-batteriespeicher-brandenburg-berlin-resilienz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) (Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin); [`testakte-kernfusion-transrapid-starnberger-see.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kernfusion-transrapid-starnberger-see.zip) (Projekt Isarlicht — Kernfusion und Transrapid am Starnberger See); [`testakte-umweltrecht-industrieanlage-genehmigung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-umweltrecht-industrieanlage-genehmigung.zip) (Akte Umweltrecht: Industrieanlage — Genehmigung, Emissionshandel, Altlast und Transaktion); [`testakte-umweltschutzverband-windpark-moorbach-umwrg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-umweltschutzverband-windpark-moorbach-umwrg.zip) (Umweltverbandsakte Moorbach) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Vollständiger Umweltrechts-Assistent für Anlagenbetreiber, Verbände, Investoren, Kommunen und öffentliche Hand: Emissionshandel, Immissionsschutz, Abfall, Wasser, Boden, Naturschutz, Umweltinformation, Verfahren, Sanktionen und Transaktionen.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn ein Anschluss an Register, Behördenportale, E-Mail, beA, Datenraum, Bank, GIS, Tabellen oder Kanzleisoftware fehlt, arbeitet es mit manuellen Uploads oder mit einem gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Eine neue Sache mit `umweltrecht-kommandocenter` starten.
3. Mandant, Ziel, Frist, Dokumente und gewünschtes Ergebnis nennen.
4. Bei fehlenden Systemanschlüssen `Simulation` sagen; das Plugin erzeugt dann realistische Testdaten und erklärt, welche echte Schnittstelle später ersetzt werden müsste.
5. Am Ende immer das Qualitätstor ausgeben lassen: offene Annahmen, Fristen, Rechenprüfung, Anlagen, Zuständigkeiten und nächste Schritte.

## Enthaltene Skills

- `umweltrecht-kommandocenter` - Umweltrecht-Kommandocenter
- `umweltrecht-emissionshandel-tehg` - Emissionshandel und TEHG
- `umweltrecht-immissionsschutz-bimschg` - Immissionsschutz und BImSchG
- `umweltrecht-stoerfall-anlagen` - Störfall, Anlagenbetrieb und Betreiberpflichten
- `umweltrecht-abfall-circular-economy` - Abfallrecht und Circular Economy
- `umweltrecht-wasser-bodenschutz` - Wasser- und Bodenschutzrecht
- `umweltrecht-naturschutz-artenschutz` - Naturschutz und Artenschutz
- `umweltrecht-umweltinformation-uig-ifg` - Umweltinformation nach UIG und IFG
- `umweltrecht-verfahren` - Umweltrechtliche Verwaltungs- und Gerichtsverfahren
- `umweltrecht-bussgeld-sanktionen` - Bußgeld, Sanktionen und Anhörung
- `umweltrecht-transaktionen-dd` - Umweltrechtliche Transaktions-Due-Diligence
- `umweltrecht-compliance-schulung` - Compliance, Beauftragte und Schulung
- `klimaklagen-verbandsklage-umwrg` - Klimaklagen, Verbandsklage UmwRG, EGMR Klima-Seniorinnen
- `lksg-csddd-lieferkettensorgfalt` - Lieferkettensorgfalt LkSG und CSDDD-Richtlinie (EU) 2024/1760
- `esg-greenwashing-csrd` - ESG-Greenwashing, CSRD-Umsetzung, ESRS, UWG-Werbung

## Vorlagen

- `assets/templates/umwelt-mandatskarte.md` - Umweltrecht-Mandatskarte
- `assets/templates/tehg-zuteilung-check.md` - TEHG-Zuteilungs- und Sanktionscheck
- `assets/templates/bimschg-genehmigungsfahrplan.md` - BImSchG-Genehmigungsfahrplan
- `assets/templates/stoerfall-anlagenmatrix.md` - Störfall- und Anlagenpflichtenmatrix
- `assets/templates/abfall-circular-matrix.md` - Abfall- und Circular-Economy-Matrix
- `assets/templates/wasser-boden-pruefplan.md` - Wasser- und Boden-Prüfplan
- `assets/templates/naturschutz-artenschutz-check.md` - Naturschutz- und Artenschutzcheck
- `assets/templates/uig-ifg-verfahren.md` - UIG/IFG-Verfahrenskarte
- `assets/templates/umweltverfahren-fristen.md` - Umwelt-Verfahrens- und Fristenplan
- `assets/templates/bussgeld-verteidigungsplan.md` - Bußgeld-Verteidigungsplan Umwelt
- `assets/templates/umwelt-dd-grid.md` - Umwelt-DD-Grid
- `assets/templates/schulung-beauftragte-plan.md` - Schulungs- und Beauftragtenplan

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen; unsichere Normen und Rechtsprechung werden als Prüfbedarf markiert.
- Zahlen, Fristen, Schwellenwerte und Zuständigkeiten werden sichtbar hergeleitet oder als Annahme gekennzeichnet.
- Ausgabe immer so, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 58 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abfall-anlagen-bimschg` | Abfall: Dokumentenmatrix, Lückenliste und Nachforderung im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `abfall-circular-economy` | Unternehmen oder Anlagenbetreiber hat Abfall-Frage: Abfalleigenschaft Entsorgungspflichten Nebenprodukt-Einstufung Ende der Abfalleigenschaft. Normen KrWG §§ 3 4 5 7 14 17 EU-Abfallrahmenrichtlinie 2008/98/EG LAGA. Prüfraster Abfalleigen... |
| `anlagen-abschlussprodukt-und-uebergabe` | Anlagen: Abschlussprodukt und Übergabe im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `anschluss-routing` | Anschluss-Routing für Umweltrecht: wählt den nächsten Spezial-Skill nach Engpass (Klagefrist UVPG, UVP-Bericht, Genehmigungsbescheid, Stellungnahmen Umweltverbände), dokumentiert Router-Entscheidung mit Begründung. |
| `bimschg-tatbestand-beweis-und-belege` | Bimschg: Tatbestandsmerkmale, Beweisfragen und Beleglage im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `boden-csddd-csrd-sonderfall` | Boden: Behörden-, Gerichts- oder Registerweg im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `bussgeld-emissionshandel-tehg-uwr` | Unternehmen erhaelt Anhörung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWiG §§ 55 67 68 BImSchG §§ 62 64 KrWG §§ 69 70 WHG § 103 BNatSchG §§ 69 71a Bußgeld bis 100000 EUR. Prüfraster Tatbesta... |
| `bussgeld-quellenkarte` | Bussgeld Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `compliance-schulung` | Anlagenbetreiber muss Umwelt-Compliance-Schulungen und Jahresaudit-Plaene erstellen für Immissionsschutzbeauftragte Abfallverantwortliche. Normen BImSchG §§ 53-58 KrWG §§ 59 60 WHG §§ 64 65. Prüfraster Schulungspflichten Dokumentationspf... |
| `csddd-mandantenkommunikation-entscheidungsvorlage` | Csddd: Mandantenkommunikation und Entscheidungsvorlage im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `csrd-sonderfall-und-edge-case` | Csrd: Sonderfall und Edge-Case-Prüfung im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `diligence-greenwashing-beweislast-klimaklagen` | Diligence: Compliance-Dokumentation und Aktenvermerk im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `dokumente-intake` | Dokumentenintake für Umweltrecht: sortiert UVP-Bericht, Genehmigungsbescheid, Stellungnahmen Umweltverbände, prüft Datum, Absender, Frist und Beweiswert (Immissionsmessungen, Bodengutachten); markiert Lücken; berücksichtigt Mandatsgeheim... |
| `einstieg-routing` | Einstieg, Triage und Routing für Umweltrecht: ordnet Rolle (Vorhabenträger, Behörde, Umweltverband), markiert Frist (Klagefrist UVPG), wählt Norm (BImSchG, BNatSchG, WHG, BBodSchG, UVPG) und Zuständigkeit (Umweltbehörden Länder), leitet... |
| `emissionshandel-tehg` | Anlagenbetreiber begutachtet Zuteilungsantrag Monitoring Abgabepflicht oder wehrt DEHSt-Sanktion ab. TEHG §§ 4 5 7 8 9 26 ZuV 2020 BEHG. Abgabe bis 30. April Sanktion 100 EUR je fehlende Tonne CO2. Prüfraster Zuteilungs-Berechnung Monito... |
| `esg-greenwashing-klimaklagen-verbandsklage` | Esg Greenwashing Csrd: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Umweltrecht. |
| `greenwashing-beweislast-und-darlegungslast` | Greenwashing: Beweislast, Darlegungslast und Substantiierung im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `immissionsschutz-bimschg` | Anlagenbetreiber oder Nachbar: BImSchG-Genehmigung beantragen anfechten oder Nachbar-Drittschutz geltend machen. BImSchG §§ 4 6 10 16 17 4. BImSchV UVPG. Normen BImSchG § 5 Abs. 1 Nr. 1 Drittschutz Rücksichtnahmegebot. Prüfraster Genehmi... |
| `klimaklagen-mehrparteien-konflikt-und-interessen` | Klimaklagen: Mehrparteienkonflikt und Interessenmatrix im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `klimaklagen-verbandsklage-umwrg` | Klimaklagen Verbandsklage Umwrg: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Umweltrecht. |
| `kommandocenter` | Umweltmandat-Einstieg: Intake Anlagenkarte Behördenkarte Fristen Risiken naechstes Arbeitsprodukt. Routing zu BImSchG KrWG WHG BBodSchG TEHG BNatSchG-Skills. Normen je nach Routing. Prüfraster Mandanten-Typ-Identifikation Sachgebiets-Rou... |
| `lieferkettensorgfalt-lksg-red-naturschutz` | Lieferkettensorgfalt: Formular, Portal und Einreichungslogik im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `lksg-csddd-lieferkettensorgfalt` | Unternehmen ab 1000 Mitarbeitern muss Lieferketten-Sorgfaltspflichten nach LkSG und kuenftig CSDDD erfuellen. LkSG seit 1.1.2023 CSDDD Richtlinie 2024/1760 Phasing ab 2027. Normen LkSG §§ 3 4 8 11 24 CSDDD Art. 1 ff. Prüfraster Anwendung... |
| `lksg-red-team-und-qualitaetskontrolle` | Lksg: Red-Team und Qualitätskontrolle im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `mandantenkommunikation-redteam-qualitygate-stoerfall` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Umweltrecht. |
| `naturschutz-artenschutz` | Unternehmen plant Bauvorhaben mit naturschutzrechtlichem Eingriff oder Artenschutz-Konflikt. FFH-Vertraeglichkeit Artenschutz §§ 44 45 BNatSchG Kompensationspflichten. Normen BNatSchG §§ 13-19 34-36 44-45 FFH-RL 92/43/EWG Vogelschutz-RL.... |
| `naturschutz-schriftsatz-brief-und-memo-bausteine` | Naturschutz: Schriftsatz-, Brief- und Memo-Bausteine im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `output-waehlen` | Output-Wahl für Umweltrecht: stimmt Adressat (Vorhabenträger, Behörde, Umweltverband), Frist (Klagefrist UVPG) und Form auf den Zweck ab — typische Outputs: UVP-Bericht, Verbandsklage, Genehmigungsantrag. |
| `quellen-livecheck` | Quellen-Live-Check für Umweltrecht: prüft Normen (BImSchG, BNatSchG, WHG, BBodSchG, UVPG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Umweltbehörden Länder und Quellenhygiene nach references/quellenhygiene.md. |
| `spezial-bussgeld-livequellen-und-rechtsprechungscheck` | Bussgeld: Livequellen- und Rechtsprechungscheck. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Umweltrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Up... |
| `stoerfall-anlagen-transaktionen-dd` | Anlagenbetreiber prüft Stoerfallrelevanz betreibt Seveso-III-Anlage oder will DEHSt-Anordnung abwehren. Normen BImSchG 12. BImSchV Stoerfallverordnung Seveso-III-RL. Prüfraster Stoerfallrelevanz-Prüfung Sicherheitsbericht Betreiberpflich... |
| `stoerfall-fristennotiz-und-naechster-schritt` | Stoerfall: Fristennotiz und nächster Schritt im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `tehg-verfahren-umweltrecht` | Tehg: Fristen, Form, Zuständigkeit und Rechtsweg im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `transaktionen-dd` | M&A-Transaktion und Anwalt prüft Umwelt-DD-Risiken im Datenraum: Genehmigungen Altlasten Emissionen Abfall Wasser Naturschutz. Normen BImSchG KrWG WHG BBodSchG TEHG Umwelthaftungsrecht. Prüfraster Red-Flags Closing-Conditions Capex-Risik... |
| `umwelt-umweltrecht-umwrg` | Umwelt: Zahlen, Schwellenwerte und Berechnung im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `umweltinformation-uig-ifg` | Buerger Verband oder Unternehmen stellt UIG/IFG-Antrag auf Umweltinformation oder wehrt Ablehnung ab. Normen UIG §§ 3 4 8 9 10 IFG §§ 1 3 5 6 9 Auskunftsfrist 1 Monat. Prüfraster Antragsrecht Ausnahmen Geheimnisschutz Drittbeteiligung Wi... |
| `umweltrecht-bussgeld-sanktionen` | Unternehmen erhaelt Anhoerung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWiG §§ 55 67 68 BImSchG §§ 62 64 KrWG §§ 69 70 WHG § 103 BNatSchG §§ 69 71a Bußgeld bis 100000 EUR. Prüfraster Tatbest... |
| `umweltrecht-erstpruefung-und-mandatsziel` | Umweltrecht: Erstprüfung, Rollenklärung und Mandatsziel im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `umwrg-internationaler-bezug-und-schnittstellen` | Umwrg: Internationaler Bezug und Schnittstellen im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Umweltrecht: trennt fehlende Tatsachen von fehlenden Belegen (UVP-Bericht, Genehmigungsbescheid, Stellungnahmen Umweltverbände), nennt pro Lücke Beweisthema, Beschaffungsweg (Umweltbehörden Länder), Fris... |
| `uwr-altlasten-pruefung-spezial` | Spezialfall Altlastenpruefung: BBodSchG, Sanierungs- und Untersuchungsanordnung, Sicherungsverantwortlicher, Zustandsstoerer, Verhaltensstoerer, Eigentuemer-Haftung. Prüfraster und Mustertexte für Bescheid-Anfechtung im Umweltrecht. |
| `uwr-bimschg-genehmigung-bauleiter` | Bauleiter BImSchG-Genehmigung: Verfahrensarten foermlich und vereinfacht, öffentliche Auslegung, Nebenbestimmungen. Prüfraster für Antragsteller und Einwender im Umweltrecht. |
| `uwr-bundesnaturschutzgesetz-eingriff-co2` | Spezialfall Eingriff in Natur und Landschaft §§ 14 ff. BNatSchG: Vermeidung, Minimierung, Ausgleich und Ersatz, Eingriff Prüfraster. Anwendung in Bauleitplanung im Umweltrecht. |
| `uwr-co2-emissionshandel-spezial` | Spezialfall CO2-Emissionshandel TEHG / EU-ETS und Reform ETS 2: Zuteilung, Auktion, freie Zuteilung, CBAM Schnittstelle. Prüfraster für Anlagenbetreiber im Umweltrecht. |
| `uwr-einfuehrung-rechtsquellen` | Umweltrecht einfuehrend: BImSchG, BNatSchG, WHG, KrWG, BBodSchG, USchadG, EU-IED, REACH. Pro Norm Anwendungsbereich, Aufsicht, typische Mandantenfragen. Entscheidungstabelle. |
| `uwr-emissionshandel-ets-spezial` | Spezialfall EU-Emissionshandel ETS: Anwendungsbereich, Zuteilung kostenloser Zertifikate, Berichts- und Abgabepflicht, CBAM seit 2026 für Importe. Prüfraster für Industriebetriebe und Sanktionen bei Verstoss im Umweltrecht. |
| `uwr-immissionsschutz-praxis` | Immissionsschutzrecht Praxis: § 4 BImSchG genehmigungsbeduerftige Anlagen, 4. BImSchV, Genehmigungsverfahren, Anhörung, Einwendungen, sofortige Vollziehbarkeit. Prüfraster für Anlagenbetreiber und Anwohner im Umweltrecht. |
| `uwr-wasserrechtliche-erlaubnis-leitfaden` | Leitfaden wasserrechtliche Erlaubnis WHG: Bewirtschaftungsermessen, Benutzung, Stand der Technik: Prüfraster für Industrieanlagen und kommunale Vorhaben. |
| `verfahren` | Umweltrechtssache geht in Verwaltungsgericht: Ausgangsverfahren Anhörung Widerspruch Eil- und Klageverfahren. Normen VwGO §§ 42 43 47 80 80a 80b 113 123 VwVfG §§ 28 39 UmwRG §§ 1 2 4. Prüfraster Klagebefugnis Praeklusion Eilantrag-Ground... |
| `verfahren-verhandlung-vergleich-und-eskalation` | Verfahren: Verhandlung, Vergleich und Eskalation im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `wasser-abfall-circular-umweltrecht-schulung` | Wasser: Risikoampel, Gegenargumente und Verteidigungslinien im Umweltrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `wasser-bodenschutz-uwr-altlasten-bimschg` | Unternehmen beantragt WHG-Erlaubnis oder hat Altlastenverantwortung oder Bodenverunreinigung. Normen WHG §§ 8 9 10 12 57 BBodSchG §§ 4 9 10 12 24 BodSchV. Prüfraster Erlaubnis-Voraussetzungen Altlasten-Haftungskette Sanierungsverantwortl... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Umweltrecht. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Umweltrecht. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Umweltrecht. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

# VerkehrsOWi-Verteidiger

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verkehrsowi-verteidiger`) | [`verkehrsowi-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehrsowi-verteidiger.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Norderhof-Tannenmoor — Abstandsverstoß Section Control BAB 7 Bispingen, Bußgeld und Fahrverbot** (`verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof`) | [Gesamt-PDF lesen](../testakten/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof/gesamt-pdf/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof_gesamt.pdf) | [`testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof.zip) |
| **VerkehrsOWi – Qualifizierter Rotlichtverstoß, Tempoüberschreitung und Fahrverbot** (`verkehrsowi-rotlicht-tempo`) | [Gesamt-PDF lesen](../testakten/verkehrsowi-rotlicht-tempo/gesamt-pdf/verkehrsowi-rotlicht-tempo_gesamt.pdf) | [`testakte-verkehrsowi-rotlicht-tempo.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-rotlicht-tempo.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein freistehender Verteidigungsassistent für Verkehrsordnungswidrigkeiten: vom Anhörungsbogen über Einspruch, Akteneinsicht, Messakte und Punkte bis zur Amtsgerichtsverhandlung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn Register, Kanzleisoftware, beA, E-Mail, Datenraum oder Aktenexport fehlen, arbeitet es mit manuellen Uploads oder mit einem klar gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `verkehrsowi-kommandocenter` starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nicht raten lassen, sondern mit der passenden Vorlage nachfordern oder Simulation ausdrücklich aktivieren.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `verkehrsowi-kommandocenter` - VerkehrsOWi-Kommandocenter
- `verkehrsowi-aktenanlage` - Aktenanlage und Dokumentenregister
- `verkehrsowi-anhoerung-bussgeldbescheid` - Anhörung und Bußgeldbescheid prüfen
- `verkehrsowi-fristen-einspruch` - Fristen und Einspruch
- `verkehrsowi-verjaehrung-zustellung` - Verjährung und Zustellung
- `verkehrsowi-akteneinsicht-messakte` - Akteneinsicht und Messakte
- `verkehrsowi-messverfahren-geschwindigkeit` - Geschwindigkeitsmessung
- `verkehrsowi-rotlicht-abstand-handy` - Rotlicht, Abstand und Handy
- `verkehrsowi-alkohol-drogen-24a` - Alkohol und Drogen nach § 24a StVG
- `verkehrsowi-fahreridentifizierung` - Fahreridentifizierung
- `verkehrsowi-punkte-fahrverbot-flensburg` - Punkte, Fahrverbot und Flensburg
- `verkehrsowi-haertefall-fahrverbot` - Härtefall beim Fahrverbot
- `verkehrsowi-beweisverwertung-standardisiert` - Beweisverwertung und Standardisierung
- `verkehrsowi-zeugen-polizei-strategie` - Zeugen- und Polizeibefragung
- `verkehrsowi-hauptverhandlung-amtsgericht` - Hauptverhandlung vor dem Amtsgericht
- `verkehrsowi-rechtsbeschwerde` - Rechtsbeschwerde
- `verkehrsowi-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `verkehrsowi-mandantenkommunikation` - Mandantenkommunikation
- `verkehrsowi-simulation-training` - Simulation und Training
- `verkehrsowi-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/verkehrsowi-mandatskarte.md` - VerkehrsOWi-Mandatskarte
- `assets/templates/frist-und-verjaehrung.md` - Fristen- und Verjährungsblatt
- `assets/templates/anhoerungsbogen-check.md` - Anhörungsbogen-Check
- `assets/templates/bussgeldbescheid-pruefung.md` - Bußgeldbescheid-Prüfung
- `assets/templates/einspruch-owig-67.md` - Einspruch nach § 67 OWiG
- `assets/templates/akteneinsicht-messakte.md` - Akteneinsicht und Messakte
- `assets/templates/messverfahren-checkliste.md` - Messverfahren-Checkliste
- `assets/templates/fahreridentifizierung.md` - Fahreridentifizierung
- `assets/templates/punkte-fahrverbot-matrix.md` - Punkte- und Fahrverbotsmatrix
- `assets/templates/haertefall-fahrverbot.md` - Härtefallpaket Fahrverbot
- `assets/templates/zeugen-polizei-fragenkatalog.md` - Zeugen- und Polizeifragen
- `assets/templates/hauptverhandlung-amtsgericht.md` - Hauptverhandlung Amtsgericht
- `assets/templates/rechtsbeschwerde-check.md` - Rechtsbeschwerde-Check
- `assets/templates/rechtsprechungsrecherche.md` - Rechtsprechungsrecherche
- `assets/templates/mandantenanschreiben.md` - Mandantenanschreiben
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

## Arbeitsakte

Zum Arbeiten liegt die Akte unter `testakten/verkehrsowi-rotlicht-tempo`. Sie wird im Release als `testakte-verkehrsowi-rotlicht-tempo.zip` bereitgestellt und ist kein Bestandteil des Plugin-ZIPs.

## Download

- Plugin-ZIP: [verkehrsowi-verteidiger.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehrsowi-verteidiger.zip)
- Akte: [testakte-verkehrsowi-rotlicht-tempo.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-rotlicht-tempo.zip)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Verkehrsowi Verteidiger-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeits... |
| `spezial-abstand-livequellen-und-rechtsprechungscheck` | Abstand: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-akteneinsicht-internationaler-bezug-und-schnittstellen` | Akteneinsicht: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-alkohol-compliance-dokumentation-und-akte` | Alkohol: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-amtsgericht-mandantenkommunikation-entscheidungsvorlage` | Amtsgericht: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-anhoerung-fristen-form-und-zustaendigkeit` | Anhoerung: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bussgeldbescheid-tatbestand-beweis-und-belege` | Bussgeldbescheid: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-drogen-mehrparteien-konflikt-und-interessen` | Drogen: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-einspruch-dokumentenmatrix-und-lueckenliste` | Einspruch: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fahrverbot-behoerden-gericht-und-registerweg` | Fahrverbot: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-geschwindigkeit-verhandlung-vergleich-und-eskalation` | Geschwindigkeit: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-handy-zahlen-schwellen-und-berechnung` | Handy: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-hauptverhandlung-sonderfall-und-edge-case` | Hauptverhandlung: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-messakte-formular-portal-und-einreichung` | Messakte: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-messung-fahrverbot-punkte` | Messung, Punkte, Fahrverbot und Verteidigungsziel im Verkehrs-OWi: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-punkte-risikoampel-und-gegenargumente` | Punkte: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rotlicht-schriftsatz-brief-und-memo-bausteine` | Rotlicht: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verkehrsowi-erstpruefung-und-mandatsziel` | Verkehrsowi: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verteidiger-beweislast-und-darlegungslast` | Verteidiger: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zeugenstrategie-red-team-und-qualitaetskontrolle` | Zeugenstrategie: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `verkehrsowi-aktenanlage` | Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster: Bußgeldbescheid, Me... |
| `verkehrsowi-akteneinsicht-messakte` | Workflow-Skill zu verkehrsowi akteneinsicht messakte. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `verkehrsowi-alkohol-drogen-24a` | Alkohol- und Drogen-OWi verteidigen: Mandant hat Bußgeldbescheid wegen 0.5-Promille oder Drogennachweis erhalten. Normen: § 24a Abs. 1 StVG (0.5-Promille-Grenze), § 24a Abs. 2 StVG (Wirkstoffnachweis THC/Kokain/Amphetamin), § 81a StPO (B... |
| `verkehrsowi-anhoerung-bussgeldbescheid` | Anhoerung vor Bußgeldbescheid und Reaktion auf Bußgeldbescheid: Mandant hat Anhoerungsbogen oder Bußgeldbescheid erhalten. Normen: § 55 OWiG (Anhoerung, Schweigerecht), § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch 2-Wo... |
| `verkehrsowi-beweisverwertung-standardisiert` | Workflow-Skill zu verkehrsowi beweisverwertung standardisiert. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `verkehrsowi-fahreridentifizierung` | Fahreridentifizierung im OWi-Verfahren angreifen oder verteidigen: Mandant bestreitet Fahrereigenschaft oder will Fahrer nicht nennen. Normen: § 31a StVG (Halter-Auskunftspflicht und Fahrtenbuchauflage), § 55 OWiG (Aussageverweigerungsre... |
| `verkehrsowi-fristen-einspruch` | Einspruchsfrist im OWi-Verfahren berechnen und wahren: Drohende Rechtsbestandskraft des Bußgeldbescheids. Normen: § 67 OWiG (Einspruch 2 Wochen ab Zustellung), §§ 33 OWiG, 177-182 ZPO (Zustellungsfiktion), § 52 OWiG (Wiedereinsetzung), §... |
| `verkehrsowi-haertefall-fahrverbot` | Haertefall-Argumentation gegen Fahrverbot nach § 25 StVG: Mandant ist beruflich auf Führerschein angewiesen. Normen: § 25 StVG (Fahrverbot), § 25 Abs. 2a StVG (Wirkungszeitpunkt verschiebbar), § 17 Abs. 3 OWiG (Geldbusse erhoehen als Alt... |
| `verkehrsowi-hauptverhandlung-amtsgericht` | Hauptverhandlung in OWi-Sache am Amtsgericht vorbereiten und führen: Termin nach Einspruch gegen Bußgeldbescheid. Normen: § 71 OWiG (HV nach StPO), § 77 OWiG (Beweisanträge), § 55 OWiG (Schweigerecht), § 17 OWiG (Strafmass). Prüfraster:... |
| `verkehrsowi-kommandocenter` | Zentrales Steuerungsmodul VerkehrsOWi-Verteidiger: Mandant stellt OWi-Mandat vor und benoetigt schnelle Orientierung. Normen: §§ 24 StVG, 67 OWiG, 25 StVG, 4 StVG (FAER). Prüfraster: Ampel-Schnelldiagnose (Tatvorwurf, Frist, Fahrverbot-R... |
| `verkehrsowi-mandantenkommunikation` | Mandantenkommunikation im OWi-Mandat: Mandant versteht Verfahren nicht und benoetigt verstaendliche Erklärung. Normen: BRAO § 43a (Beratungspflicht), § 67 OWiG, § 25 StVG. Prüfraster: Erstgespraeche-Leitfaden, Anhoerungsbogen-Empfehlung,... |
| `verkehrsowi-messverfahren-geschwindigkeit` | Workflow-Skill zu verkehrsowi messverfahren geschwindigkeit. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `verkehrsowi-punkte-fahrverbot-flensburg` | Punkte im Fahreignungsregister (FAER) Flensburg und Fahrverbot § 25 StVG: Mandant hat Punktewarnung erhalten oder Führerscheinentzug droht. Normen: § 4 StVG (Punktesystem: Warnung 4 Pkt, Verwarnung 6 Pkt, Entzug 8 Pkt), § 65 StVG (Tilgun... |
| `verkehrsowi-quality-gate` | Quality-Gate-Checkliste OWi-Mandat: Vor Einspruch, nach Akteneingang und vor HV prüft Kanzlei Vollständigkeit. Normen: § 67 OWiG (Einspruch), § 77 OWiG (HV-Beweisanträge), BVerfG Rohmessdaten. Prüfraster: Messakte vollständig, Rohmessdat... |
| `verkehrsowi-rechtsbeschwerde` | Rechtsbeschwerde im OWi-Verfahren nach § 79 OWiG einlegen: AG hat OWi-Urteil gesprochen und Mandant will Rechtsbeschwerde. Normen: § 79 OWiG (Zulassigkeit: Geldbusse über 250 EUR oder Fahrverbot), § 80 OWiG (Zulassungsbeschwerde), § 344... |
| `verkehrsowi-rechtsprechungsrecherche` | Rechtsprechungsrecherche für OWi-Verkehrsmandate: Anwalt sucht OLG-Entscheidungen zu Messverfahren, Rohmessdaten und Fahrverbot. Normen: §§ 24 StVG, 25 StVG, 4 StVG; OWiG §§ 67 und 79 und 80. Prüfraster: OLG-Datenbanken (amtliche oder fr... |
| `verkehrsowi-rotlicht-abstand-handy` | Rotlicht-OWi, Abstand-OWi und Handy-OWi verteidigen: Mandant hat Bußgeldbescheid wegen Rotlicht, zu geringem Abstand oder Handynutzung erhalten. Normen: § 37 StVO (Rotlicht: einfach vs. qualifiziert 1 Sekunde), § 4 StVO (Abstand-Berechnu... |
| `verkehrsowi-simulation-training` | Simulationstraining für OWi-Mandate. Uebungsszenarien Messverfahren Rotlicht Handy Alkohol Fahreridentifizierung. Rollenspiel Mandantengespraeche Hauptverhandlung. Fallvarianten mit Erwartungshorizont. Training ohne echte Mandatsdaten. |
| `verkehrsowi-verjaehrung-zustellung` | Verfolgungsverjährung im OWi-Verfahren prüfen: Anwalt will Verjährungseinwand erheben. Normen: § 26 StVG i.V.m. § 31 OWiG (Verjährungsfrist 3 Monate nach Tatende), § 33 OWiG (Unterbrechungshandlungen), absolute Verjährung 6 Monate. Prüfr... |
| `verkehrsowi-zeugen-polizei-strategie` | Zeugen-Strategie gegenüber Polizeibeamten im OWi-Verfahren: Polizeibeamter als einziger Zeuge in der HV. Normen: § 240 StPO i.V.m. § 71 OWiG (Fragerecht), §§ 373 ff. StPO (Zeugenvernehmung). Prüfraster: Aussage-Konstanz (Protokoll vs. HV... |
| `vowi-akteneinsicht-rohmessdaten-leitfaden` | Leitfaden Akteneinsicht und Rohmessdaten in OWi-Verfahren: BVerfG- und OLG-Rechtsprechung, Sachverstaendigengutachten, standardisiertes Messverfahren. Pruefraster fuer Verteidiger. |
| `vowi-bussgeldbescheid-pruefung-bauleiter` | Bauleiter Pruefung Bussgeldbescheid OWiG: Tatvorwurf, Beweismittel, Hoehe, Rechtsfolgen Punkte und Fahrverbot. Pruefraster fuer Verteidiger im Erstgespraech. |
| `vowi-handyverstoss-spezial` | Spezialfall Handy- und Geraeteverstoss § 23 Abs. 1a StVO: erfasste Geraete, Halten, Nutzen, Abgrenzung Sprachsteuerung. Pruefraster fuer Verteidiger. |
| `vowi-tempomessverfahren-fehlerquellen-spezial` | Spezialfall Tempomessverfahren und Fehlerquellen: Poliscan, ES 3.0, ES 8.0, Riegl, Eichschein, Verkehrsfehlergrenzen. Pruefraster fuer Verteidiger und Sachverstaendiger. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin verkehrsowi-verteidiger: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin verkehrsowi-verteidiger: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin verkehrsowi-verteidiger: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin verkehrsowi-verteidiger: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin verkehrsowi-verteidiger: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin verkehrsowi-verteidiger: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin verkehrsowi-verteidiger: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin verkehrsowi-verteidiger: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin verkehrsowi-verteidiger: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin verkehrsowi-verteidiger: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

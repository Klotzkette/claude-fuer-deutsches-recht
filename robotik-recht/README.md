# robotik-recht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`robotik-recht`) | [`robotik-recht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/robotik-recht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7** (`robotikrecht-roboterflotte-vellbruck-muenchen`) | [Gesamt-PDF lesen](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

> Großes Robotik-Rechtsplugin für Deutschland und EU. Es führt von der ersten Produktbeschreibung über Rollenklärung, Maschinenverordnung, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Data Act, Marktüberwachung, Rückruf, Verträge und Streitfall bis zur verwertbaren anwaltlichen Ausgabe.

## Wofür dieses Plugin gedacht ist

Robotikrecht ist keine einzelne Norm. Ein physischer Roboter verbindet Maschine, Software, KI, Sensorik, Cloud, Daten, Arbeitsschutz, Produkthaftung und Vertrag. Dieses Plugin soll genau diesen Knoten lösen: schnell genug für den Kaltstart, tief genug für Produktfreigabe, Behördenkontakt und Haftungsstreit.

Typische Fälle:

- kollaborierende Roboter in Produktion und Lager,
- mobile AMR-/AGV-Flotten in Logistik und Krankenhaus,
- Service-, Pflege-, Haushalts- und Sozialroboter,
- Medizin-, Reha- und OP-Robotik,
- Roboter mit Kamera, Mikrofon, Lidar, Biometrie, Telemetrie oder Cloudsteuerung,
- Robot-as-a-Service, Wartung, Updates, Lieferkette und Rückruf,
- Unfall, Beinaheunfall, Cybervorfall, Datenschutzbeschwerde oder Marktüberwachung.

## Arbeitsstil

Der Einstiegsskill `allgemein` fragt nicht abstrakt nach allem, sondern baut sofort eine Arbeitskarte:

1. Rolle und Produkt.
2. Zweckbestimmung und tatsächliche Nutzung.
3. physisches Sicherheitsrisiko.
4. KI- und Softwarefunktion.
5. Daten- und Cyberlage.
6. Fristen, Behörden, Unfall oder Rückruf.
7. Zieloutput.

Danach werden die passenden Spezialskills vorgeschlagen. Das Plugin ist bewusst erweiternd: Es hilft Ingenieurinnen, Inhouse-Teams und Anwältinnen, die richtige Tiefe zu finden, ohne sie in ein starres Formular zu sperren.

## Quellenhygiene

- Normen werden aus amtlichen oder frei zugänglichen Quellen geprüft: EUR-Lex, Gesetze im Internet, Recht.Bund, BAuA, EU-Kommission und Gerichtsseiten.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine BeckRS-/juris-/Kommentar-Blindzitate.
- Technische Normen und harmonisierte Standards werden nicht geraten; Fundstelle, Fassung und Anwendbarkeit live prüfen.

## Kernmodule

- **Einstieg und Workflow:** Kaltstart, Rollenmatrix, Dokumentenintake, Rechtsregime-Matrix, Fristen, Outputwahl, Red-Team.
- **Produktsicherheit:** Maschinenverordnung, MaschinenDG, ProdSG/GPSR, CE, technische Dokumentation, Anleitung, Normen, Marktüberwachung.
- **KI-VO:** Art. 3, Art. 5, Art. 6, Anhang III, Sicherheitskomponenten, Provider-/Deployerpflichten, Human Oversight, Logging, Robustheit.
- **Produkthaftung:** ProdHaftG, neue EU-Produkthaftungsrichtlinie, Fehlerbegriff, Beweislast, Updates, digitale Dienste, Betreiber-Mitverschulden.
- **Datenschutz und Cyber:** Sensorik, DSFA, Beschäftigte, Biometrie, Data Act, CRA, SBOM, Schwachstellenmeldungen, NIS2-Schnittstellen.
- **Sektoren:** Industrie, Logistik, Pflege, Medizin, Haushalt, Kinder, Agrar, Bau, Sicherheit, öffentlicher Raum, Drohnen und Dual-Use.
- **Vertrag und Streit:** RaaS, Wartung, SLA, Lieferkette, Indemnity, Versicherung, Sachverständige, Besichtigung, Rückruf, Vergleich.

## Demonstrationsakte

Die Akte `robotikrecht-roboterflotte-vellbruck-muenchen` zeigt eine verdichtete Robotiklage: Vellbruck Robotics GmbH bringt eine Cobot-/AMR-Flotte, einen Pflegepiloten und eine Cloudsteuerung in den Markt. Es gibt Unfall, Softwareupdate, Marktüberwachung, Datenschutzbeschwerde, Cyber-Schwachstelle, MDR-Nähe, Betreiberfehler, Lieferantenstreit und Versicherungsdruck. Die Akte ist als unordentlicher Datenraum angelegt und hat zusätzlich ein Gesamt-PDF.

## Pflichtdisclaimer für externe Outputs

Jede externe Ausgabe soll knapp klarstellen: KI-gestützte Vorprüfung; keine amtliche Konformitätsbewertung; technische und regulatorische Bewertung hängen von vollständigen Unterlagen, aktuellem Normenstand und Live-Quellenprüfung ab.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 143 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `accuracy-robustness-cybersecurity-ai` | Prüft Genauigkeit, Robustheit und Cybersicherheit von KI-Funktionen im Roboter mit realistischen Einsatzgrenzen. |
| `agile-entwicklung-und-compliance-gates` | Entwirft Compliance-Gates für agile Robotikentwicklung: Definition of Done, Release-Board, Sicherheitsfreigabe und Rechtsfreigabe. |
| `allgemein` | Robotik-Recht-Kompass für Deutschland und EU: Einstieg, Rollenklärung, Produktklassifizierung, Maschinenverordnung, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Marktüberwachung und passende Spezialskills. |
| `anwaltliche-quellenhygiene-robotik` | Sichert Quellenhygiene: keine Paywall-Blindzitate, keine erfundenen Rechtsprechungsfundstellen, Normen live prüfen, Aktenzeichen nur verifiziert. |
| `arbeitsschutz-betrsichv-robotik` | Prüft Arbeitsschutz und Betriebssicherheit bei Robotern im Betrieb: Gefährdungsbeurteilung, Unterweisung, Prüfungen, Betriebsanweisung. |
| `autonome-lieferroboter-oeffentlicher-raum` | Prüft autonome Lieferroboter im öffentlichen Raum: Verkehrsrecht, Sondernutzung, Haftung, Datenschutz und kommunale Genehmigungen. |
| `barrierefreiheit-und-inklusion-robotik` | Prüft Barrierefreiheit, Inklusion und diskriminierungsarme Bedienung bei Robotikprodukten und Nutzerinterfaces. |
| `batterie-ladeinfrastruktur-und-brandschutz` | Prüft Batterie, Ladeinfrastruktur, Brandschutz, Transport, Lagerung, Rückruf und Versicherungsfragen bei mobilen Robotern. |
| `bau-und-inspektionsroboter` | Prüft Bau-, Inspektions- und Wartungsroboter: Baustelle, Arbeitsschutz, Drittschäden, Betreiberorganisation und Beweissicherung. |
| `beschaeftigtendatenschutz-cobot` | Prüft Beschäftigtendatenschutz bei Cobots: Leistungsdaten, Standort, Video, Betriebsrat, Zweckbindung und Löschfristen. |
| `betreiber-mitverschulden-und-fehlbedienung` | Prüft Betreiber-Mitverschulden: missachtete Anleitung, fehlende Wartung, Umgehung von Schutzfunktionen, Schulungslücken und Logspuren. |
| `betriebsanleitung-sprache-und-warnhinweise` | Prüft Betriebsanleitung, Sicherheitsinformationen, digitale Anleitung, Sprache, Restgefahren und Verständlichkeit für Zielgruppen. |
| `beweislast-und-offenlegung-produkthaftung` | Prüft Beweislast, Indizien, Offenlegung technischer Unterlagen, Kausalität und Schwierigkeiten komplexer Robotiksysteme. |
| `biometrie-emotion-und-personenerkennung` | Prüft Biometrie, Emotionserkennung, Personenerkennung, Beschäftigtenkontext und Transparenzpflichten bei Robotern. |
| `ce-zeichen-fehlgebrauch-und-abmahnung` | Prüft CE-Kennzeichnung, irreführende Werbung, fehlende Unterlagen, Wettbewerbsrecht und Abmahnrisiken. |
| `chirurgie-und-op-robotik` | Prüft OP- und Chirurgierobotik: MDR-Klasse, klinische Bewertung, Vigilanz, Betreiber, Aufklärung, Wartung und Behandlungsfehlernähe. |
| `cra-produkt-mit-digitalen-elementen` | Prüft Cyber Resilience Act für Roboter, Steuerungssoftware, Apps, Cloud-Komponenten und Updatekanäle. |
| `data-act-roboterdaten` | Prüft Data-Act-Fragen bei vernetzten Robotern: Nutzerdatenzugang, B2B-Datenbereitstellung, Geschäftsgeheimnisse und Cloudwechsel. |
| `datenminimierung-edge-cloud` | Prüft lokale Verarbeitung, Edge/Cloud-Aufteilung, Telemetrie, Anonymisierung, Zugriffskontrolle und Retention. |
| `datensatzqualitaet-und-bias-hri` | Prüft Datenqualität und Bias bei Robotern, die Menschen erkennen, unterstützen, bewerten oder priorisieren. |
| `datenschutz-kameras-und-sensorik` | Prüft Kameras, Lidar, Mikrofone, Tiefensensoren und Umgebungsdaten von Robotern nach DSGVO und BDSG. |
| `datenverlust-und-digitaler-schaden` | Bewertet Schäden durch Datenverlust, Fehlsteuerung, Produktionsstillstand, Privacy-Schäden und reine Vermögensschäden. |
| `deliktische-haftung-paragraph-823-bgb` | Prüft deliktische Haftung nach § 823 BGB bei Robotik: Verkehrssicherung, Organisationsverschulden, Schutzgesetze, Beweis und Verschulden. |
| `digitaler-zwilling-und-simulation` | Prüft digitalen Zwilling, Simulation, Validierung, virtuelle Inbetriebnahme und Beweiswert für Konformität und Haftung. |
| `dronen-und-robotik-schnittstelle` | Prüft Drohnen als Robotik-Schnittstelle: EU-UAS-Regeln, Kamera, autonome Funktionen, Haftung und Einsatzplanung. |
| `dsfa-fuer-robotik` | Erstellt Datenschutz-Folgenabschätzung für Roboter mit Sensorik, Telemetrie, KI-Auswertung oder vulnerablen Nutzergruppen. |
| `dual-use-und-militaerische-robotik` | Prüft Dual-Use, Exportkontrolle und militärische Robotik-Schnittstellen, ohne zivile Produktpflichten zu übersehen. |
| `eu-de-umsetzung-und-rechtsstand-livecheck` | Prüft aktuellen Rechtsstand, Übergangsrecht, nationale Durchführungsgesetze, delegierte Rechtsakte und Leitlinien vor jeder Ausgabe. |
| `eu-konformitaetserklaerung-und-einbauerklaerung` | Erstellt und prüft EU-Konformitätserklärung, Einbauerklärung, Sprachfassung, Unterzeichner und technische Bezüge. |
| `foss-und-open-source-komponenten` | Prüft FOSS in Robotik: kommerzielle Bereitstellung, Hochrisiko-KI-Ausnahmen, SBOM, Lizenzen, Security und Haftungsallokation. |
| `foundation-model-und-gpai-im-roboter` | Prüft GPAI-/Foundation-Model-Komponenten im Roboter: Anbieterrolle, Integrationspflichten, Zweckbestimmung, Logging und Instructions. |
| `funkanlagen-und-konnektivitaet` | Prüft Funkmodule, WLAN, 5G, Bluetooth, RED, EMV, Cybersecurity und Betriebsumgebung. |
| `geschaeftsgeheimnisse-und-logdaten` | Prüft Schutz von Geschäftsgeheimnissen in Logs, Diagnosedaten, Trainingsdaten, Quellcode, Sachverständigenverfahren und Behördenkontakten. |
| `grundrechte-und-psychische-belastung` | Prüft grundrechtliche und soziale Risiken: Nähe, Druck, Überwachung, Pflegeabhängigkeit, Kinder, Arbeitsplatz und Würde. |
| `haftung-arzt-klinik-hersteller` | Ordnet Haftung zwischen Arzt, Klinik, Betreiber, Hersteller, Wartung und Softwareanbieter bei Medizinrobotik. |
| `harmonisierte-normen-iso-ts-15066` | Plant Normenrecherche zu industrieller Robotik, kollaborierenden Robotern, Sicherheitsfunktionen und Stand der Technik. |
| `human-oversight-in-physischer-robotik` | Prüft menschliche Aufsicht bei physischer Robotik: Not-Halt, Override, Monitoring, Kompetenz, Eskalation und Verantwortlichkeit. |
| `importeur-haendler-fulfilment-robotik` | Prüft Importeur-, Händler- und Fulfilment-Pflichten bei Robotern aus Drittstaaten und Plattformvertrieb. |
| `ki-training-mit-roboterdaten` | Prüft Training und Nachtraining mit Roboterlogs, Video, Telemetrie, synthetischen Daten und Drittanbieterdaten. |
| `ki-vo-anhang-iii-robotik-usecases` | Prüft Anhang-III-Fälle bei Robotik: Beschäftigung, Bildung, Gesundheit/Versorgung, öffentliche Leistungen, Grenzkontrolle, Strafverfolgung und Justiznähe. |
| `ki-vo-artikel-3-ki-system-robotik` | Prüft, ob die Software im Roboter ein KI-System nach Art. 3 KI-VO ist, inklusive Autonomie, Inferenz, Output und Zweck. |
| `ki-vo-artikel-6-hochrisiko-robotik` | Prüft Hochrisiko-KI nach Art. 6 KI-VO bei Sicherheitskomponente, Produktregime oder Anhang-III-Einsatz. |
| `ki-vo-deployer-pflichten-robotik` | Prüft Betreiber-/Deployerpflichten: Nutzung nach Anleitung, Aufsicht, Eingabedaten, Monitoring, Grundrechtefolgen und Logaufbewahrung. |
| `ki-vo-provider-qms-und-risk-management` | Prüft Anbieterpflichten für Hochrisiko-KI: QMS, Risikomanagement, Daten, Dokumentation, Logging, Transparenz und Human Oversight. |
| `ki-vo-verbotene-praktiken-robotik` | Prüft Manipulation, Vulnerabilität, Social Scoring, biometrische Kategorisierung und Emotionserkennung im Robotikkontext. |
| `klinische-bewertung-robotik` | Prüft klinische Bewertung und Zweckbestimmung bei medizinischer Robotik mit KI-Funktion. |
| `kollaborierende-roboter-cobot-safety` | Prüft Cobots: Kraft-/Leistungsbegrenzung, Sicherheitsabstände, Schutzräume, Betriebsarten, Validierung und Arbeitsplatzintegration. |
| `kommunal-und-behoerdenrobotik` | Prüft Robotik in Verwaltung, ÖPNV, Polizei-/Ordnungsnähe und öffentlichen Einrichtungen mit Grundrechts- und Vergabeblick. |
| `konformitaetsbescheinigung-robotik-ki` | Erstellt interne Konformitätsbescheinigung für Robotik mit KI: Scope, Regime, Nachweise, Lücken, Restrisiko, Freigabe. |
| `konformitaetsbewertung-modulwahl` | Wählt Konformitätsbewertungsverfahren, interne Fertigungskontrolle, Baumusterprüfung oder Qualitätssicherung mit benannter Stelle. |
| `lager-und-intralogistikflotte` | Prüft Roboterflotten in Lager und Intralogistik: Flottensteuerung, Zonen, Mitarbeiterschutz, Telemetrie, Wartung und Incident Logs. |
| `landwirtschaftsroboter-und-autonome-feldtechnik` | Prüft Agrarroboter: Maschinenrecht, autonome Fahrt, Umweltrisiken, Pflanzenschutz, Daten, Betreiberpflichten und Versicherung. |
| `lieferantenqualifizierung-sensor-cloud` | Prüft Lieferantenqualifizierung für Sensoren, Aktoren, Batterien, Cloud, KI-Modell, FOSS und Wartung. |
| `lieferantenregress-und-indemnity` | Baut Regress- und Freistellungskette gegen Zulieferer, Softwareanbieter, Sensorhersteller, Cloudprovider und Integratoren. |
| `logging-und-traceability-robotik` | Prüft Logging, Traceability, Audit Trail und forensische Nutzbarkeit bei Unfall, Datenschutzvorfall und Produkthaftung. |
| `marktueberwachung-unterlagenvorlage` | Bereitet Unterlagenvorlage und Argumentation gegenüber Marktüberwachung vor: technische Dokumentation, Risikobewertung, Normen, Maßnahmen. |
| `maschine-oder-unvollstaendige-maschine` | Klassifiziert Roboter als Maschine, unvollständige Maschine, Sicherheitsbauteil, austauschbare Ausrüstung oder Softwarekomponente. |
| `maschinenverordnung-annex-iii-hochrisiko` | Prüft, ob Robotik unter besondere Maschinenkategorien und strengere Konformitätsbewertung fällt. |
| `medizinprodukt-software-ki-roboter` | Prüft Zusammenspiel von MDR, KI-VO und Software als Bestandteil medizinischer Robotik. |
| `mitbestimmung-betriebsrat-robotik` | Prüft Betriebsratsrechte bei Robotik, Leistungs-/Verhaltenskontrolle, Arbeitsabläufen, Schulung und Gesundheitsschutz. |
| `mobile-roboter-amr-agv` | Prüft AMR/AGV in Logistik und Produktion: Navigation, Karten, Flottenmanagement, Kollisionsschutz, Not-Halt und Verkehrswege. |
| `nis2-betreiber-kritische-sektoren` | Prüft NIS2-Schnittstellen, wenn Roboter in kritischen Sektoren, Gesundheit, Logistik, Energie oder öffentlicher Verwaltung eingesetzt werden. |
| `patientenaufklaerung-robotik` | Prüft Patientenaufklärung bei robotergestützter Behandlung: Behandlungsalternative, Risiken, menschliche Kontrolle und Dokumentation. |
| `pflege-und-assistenzroboter` | Prüft Pflege- und Assistenzrobotik in Heim, Klinik und Haushalt: Würde, Aufsicht, Einwilligung, Haftung, MDR-Nähe und Datenschutz. |
| `pilotbetrieb-und-beta-robotik` | Prüft Pilot-/Beta-Betrieb mit Kunden: Haftung, Datenschutz, Kennzeichnung, Verantwortung, Abbruchkriterien und Lessons Learned. |
| `prodhaftg-und-neue-pld-vergleich` | Vergleicht deutsches ProdHaftG mit neuer EU-Produkthaftungsrichtlinie: Software, digitale Dienste, Offenlegung, Beweislast und Übergang. |
| `produktakte-gap-analyse` | Führt Gap-Analyse der Produktakte durch: fehlende Nachweise, falsche Annahmen, ungeklärte Rollen, nicht belegte Standards. |
| `produktbeobachtung-und-field-data` | Prüft Produktbeobachtungspflicht und Auswertung von Felddaten ohne Datenschutz- und Geschäftsgeheimnisfehler. |
| `produktfehler-verbrauchererwartung-robotik` | Prüft Produktfehler bei Robotern: berechtigte Sicherheitserwartung, Lernfähigkeit, Updates, Warnungen, Autonomie und Einsatzumgebung. |
| `produktsicherheit-vs-betriebssicherheit` | Trennt Inverkehrbringen/Produktsicherheit von Betrieb/Arbeitsschutz und verhindert falsche Verantwortungszuordnung. |
| `produktsicherheitsrechtliche-werbung` | Prüft Marketingaussagen zu Autonomie, Sicherheit, KI, Zertifizierung, CE, MDR und Normenkonformität. |
| `qualitaetsmanagement-robotikhersteller` | Prüft QM-System eines Robotikherstellers: Design Control, CAPA, Change Control, Lieferantensteuerung und Post-Market-Daten. |
| `quasihersteller-private-label-robotik` | Prüft Private-Label-, Rebranding- und Quasihersteller-Konstellationen bei Robotern und KI-Komponenten. |
| `rehabilitations-und-exoskelett-robotik` | Prüft Reha-Roboter und Exoskelette: Medizinprodukt, Arbeitsschutz, Körpernähe, Training, Fehlbedienung und Kostenträger-Schnittstelle. |
| `remote-update-und-secure-channel` | Prüft Remote-Update-Kanäle, Signaturen, Rollback, Fail-safe, Änderungsdokumentation und Verantwortung nach Update. |
| `risikobeurteilung-en-iso-12100` | Prüft Risikobeurteilung nach Stand der Technik: Grenzen, Gefährdungen, Risikominderung, Validierung und Restgefahren. |
| `robot-as-a-service-vertrag` | Entwirft und prüft Robot-as-a-Service-Verträge: Leistungsbeschreibung, SLA, Updates, Daten, Haftung, Wartung, Exit und Versicherung. |
| `rollen-hersteller-anbieter-integrator` | Prüft Hersteller-, Anbieter- und Integratorrollen bei Robotern mit Hardware, Software, KI-Modell und eigenem Markenauftritt. |
| `rueckrufpflicht-und-safety-gate` | Prüft Rückruf, Warnung, Korrekturmaßnahme, Safety-Gate-Meldung, Kundenkommunikation und Behördenunterrichtung. |
| `safety-gate-und-oeffentliche-warnung` | Prüft Folgen von Safety-Gate-Warnung, öffentlicher Produktwarnung, Reputationsrisiko und Korrekturkommunikation. |
| `sbom-und-cyber-dokumentation` | Prüft SBOM, Dependency-Management, CVE-Tracking, Sicherheitsanforderungen und Nachweise für Robotiksoftware. |
| `schadensberechnung-produktionsausfall` | Prüft Schaden bei Produktionsausfall, Körperverletzung, Sachschaden, Datenverlust, Rückrufkosten und Regress. |
| `serviceroboter-haushalt-gpsr` | Prüft Service- und Haushaltsroboter: Verbraucherprodukt, GPSR, Instruktionen, Updatepflicht, Sicherheitswarnung und Rückruf. |
| `sicherheits-und-ueberwachungsroboter` | Prüft Sicherheitsroboter, Wachroboter und Zugangskontrolle: Hausrecht, Datenschutz, Biometrie, Einsatzgrenzen und Beweisverwertung. |
| `sicherheitskomponente-mit-ki` | Prüft KI als Sicherheitskomponente einer Maschine: Schutzfunktion, Konformitätsbewertung, Hochrisiko-KI und technische Dokumentation. |
| `smart-factory-und-industrie-4-0` | Prüft Smart Factory: vernetzte Maschinen, Roboterzellen, Datenräume, Security, Produktionsstillstand und Haftungsketten. |
| `softwareupdate-als-produktbezogener-dienst` | Prüft Update, Cloud-Funktion, Kartenmaterial, KI-Modell und andere digitale Dienste als Sicherheits- und Haftungsfaktor. |
| `sozialer-humanoider-roboter` | Prüft soziale/humanoide Roboter: Vertrauen, Anthropomorphisierung, Manipulation, Kinder, Pflege, Transparenz und Datenschutz. |
| `spielzeug-und-kinderroboter` | Prüft Kinder-, Lern- und Spielzeugroboter: Spielzeugrecht, GPSR, Datenschutz Minderjähriger, KI-Transparenz und Verbraucherschutz. |
| `strom-emv-und-niederspannung` | Prüft elektrische Sicherheit, EMV, Niederspannung, Ladegeräte und Schnittstelle zur Maschinenverordnung. |
| `systemintegrator-als-hersteller` | Bewertet, wann ein Systemintegrator durch Zusammenbau, Marke, Umbau oder Konfiguration zum verantwortlichen Hersteller wird. |
| `technische-besichtigung-und-geheimnisschutz` | Plant gerichtliche oder außergerichtliche Besichtigung eines Roboters mit Geheimnisschutz, Sachverständigem und Testprotokoll. |
| `testdaten-und-validierung-vor-marktstart` | Prüft Testdaten, Validierungsplan, Feldtest, Pilotkunden, Beta-Betrieb und regulatorische Grenzen vor Marktstart. |
| `transparenz-und-nutzerinformation` | Prüft Informationspflichten, Piktogramme, Bedienoberfläche, Datenschutzhinweise und KI-Transparenz für Mensch-Roboter-Interaktion. |
| `unfallanalyse-chain-of-custody` | Sichert Beweise nach Robotikunfall: Gerät, Logexport, Video, Firmware, Konfiguration, Zeugen, Wartung und Chain of Custody. |
| `vergaberecht-robotik-beschaffung` | Prüft Vergabeunterlagen für Robotik: funktionale Anforderungen, Sicherheit, Daten, Barrierefreiheit, Wartung, Referenzen und Zuschlagskriterien. |
| `vergleich-und-sanierung-nach-incident` | Entwirft Vergleichs- und Sanierungsstrategie nach Vorfall: Patch, Austausch, Entschädigung, NDA, Behördenkommunikation und Lessons Learned. |
| `vernunftigerweise-vorhersehbarer-gebrauch` | Prüft vorhersehbaren Gebrauch, Fehlgebrauch und Grenzen von Warnhinweisen bei Robotern im Betrieb und beim Verbraucher. |
| `versicherungsdeckung-robotik` | Prüft Produkthaftpflicht, Betriebshaftpflicht, Cyber, Rückrufkosten, D&O und Maschinenbruchversicherung für Robotikrisiken. |
| `vigilanz-medizinrobotik` | Prüft Vigilanz und Post-Market Surveillance für Medizinrobotik nach MDR und nationalem Medizinprodukterecht. |
| `vulnerability-disclosure-und-reporting` | Prüft Schwachstellenmanagement, Coordinated Vulnerability Disclosure, Meldepflichten, Patch-Triage und Kundeninformation. |
| `wartungs-und-servicevertrag-robotik` | Prüft Wartungs-, Kalibrierungs- und Serviceverträge: Reaktionszeiten, Ersatzteile, Remote-Zugriff, Logdaten, Haftungsgrenzen und Dokumentation. |
| `wesentliche-veraenderung-digital` | Prüft wesentliche physische oder digitale Veränderung durch Umbau, Retrofit, Update, Fine-Tuning oder neue Sensorik. |
| `workflow-abschlussqualitaet-und-redteam` | Red-Team-Check für jedes Ergebnis: Normenstand, Quellen, fehlende Tatsachen, Gegenargumente, technische Annahmen, Datenschutz und Haftungsfolgen. |
| `workflow-anschluss-skills-router` | Schlägt nach jeder Robotikprüfung passende Anschlussplugins vor: KI-VO, Datenschutz, IT-Recht, Arbeitsrecht, Medizinrecht, Produkthaftung, Vertragsrecht und Prozess. |
| `workflow-arbeitswelt-cobot-check` | Prüft Cobots im Betrieb: Arbeitsschutz, Beschäftigtendaten, Mitbestimmung, Qualifikation, Mensch-Roboter-Interaktion, Unfälle und Produktverantwortung. |
| `workflow-beschaffung-oeffentlich-privat` | Unterstützt Beschaffung von Robotik durch Unternehmen oder öffentliche Hand: Lastenheft, Vergabe, Compliance-Kriterien, Abnahme, Gewährleistung und Exit. |
| `workflow-betreiberpflichten-und-training` | Prüft Betreiberpflichten: Arbeitsschutz, BetrSichV-Schnittstelle, Einweisung, Wartung, Betriebsanweisung, Nutzerlogs und Verantwortlichkeiten vor Ort. |
| `workflow-beweismatrix-und-logauswertung` | Baut Beweismatrix aus Telemetrie, Event Logs, Wartungsprotokollen, Video, Sensorik, Tickets, E-Mails und Versionsständen. |
| `workflow-board-und-c-level-briefing` | Übersetzt komplexes Robotikrecht in entscheidungsfähige Vorstands-/C-Level-Vorlagen mit Risiko, Optionen, Zeitplan und Budget. |
| `workflow-ce-akte-und-technische-dokumentation` | Erstellt eine CE-/Konformitätsakte mit technischer Dokumentation, EU-Konformitätserklärung, Einbauerklärung, Anleitung, Prüfprotokollen und offenen Nachweisen. |
| `workflow-datenschutz-cyber-intake` | Startet Datenschutz- und Cyberprüfung: Kameras, Mikrofone, Telemetrie, biometrische Daten, Beschäftigte, Patienten, DSFA, TOMs und CRA-Schnittstelle. |
| `workflow-dokumentenintake-datenraum` | Liest Robotik-Datenräume mit Anleitungen, CE-Unterlagen, Risikobeurteilung, Logs, Verträgen, Incident Reports und ordnet die nächsten Prüfschritte. |
| `workflow-first-year-associate-robotik` | Führt junge Anwältinnen und Anwälte durch den ersten Robotikfall: Aktenaufnahme, Normenlandkarte, Rückfragen, Quellencheck, Memo und Red-Team. |
| `workflow-fristen-und-uebergangsrecht` | Erstellt Fristenplan für Maschinenverordnung, MaschinenDG, CRA, KI-VO, Produkthaftungsrichtlinie, Meldungen, Rückruf und Prozessfristen. |
| `workflow-gutachten-memo-output` | Wählt den passenden Output: Kurzvermerk, Vorstandsvorlage, Gutachten, Behördenantwort, Rückrufplan, Vertragsredline, Klageskizze oder Counsel-Briefing. |
| `workflow-haftungsampel` | Erstellt Haftungsampel für Hersteller, Integrator, Betreiber, Händler, Wartung, KI-Anbieter, Versicherer und Geschädigte. |
| `workflow-human-robot-interaction-redteam` | Prüft besondere Mensch-Roboter-Interaktion: Nähe, Vertrauen, Manipulation, psychische Belastung, vulnerable Nutzer und klare Grenzen. |
| `workflow-ingenieur-rueckfragenliste` | Erzeugt präzise Rückfragen an Technik, QM, Datenschutz, IT-Security, Vertrieb und Service, damit das Recht nicht im Nebel prüft. |
| `workflow-internationaler-export` | Routet Robotikexport: EU-Markt, Drittstaat, Dual-Use, Sanktionen, Produktsicherheit, lokale Zulassung, Incoterms und Vertrag. |
| `workflow-kaltstart-und-routing` | Kaltstart für jedes Robotikmandat: sortiert Produkt, Rolle, Ziel, Frist, Risiko, Rechtsregime und schlägt sofort die passenden Skills im Robotik-Recht-Plugin vor. |
| `workflow-ki-vo-integrationscheck` | Prüft integrierte KI-Systeme, Sicherheitskomponenten, Anhang III, Hochrisiko-Nähe, Anbieter-/Betreiberpflichten und Zweckänderungen. |
| `workflow-laienmodus-robotikrecht` | Erklärt Robotik-Recht in verständlicher Sprache für Gründer, Ingenieurinnen, Betreiber, Versicherer und Behörden, ohne juristische Genauigkeit zu verlieren. |
| `workflow-litigation-vorbereitung` | Bereitet Robotikstreit vor: Anspruchsgrundlagen, Beweislast, Sachverständige, Besichtigung, Geheimnisschutz, Produktakte und Vergleichsoptionen. |
| `workflow-marktueberwachung-dialog` | Bereitet Antworten an Marktüberwachung, BAuA-/Landesbehörden, Safety-Gate-Meldungen, Unterlagenvorlage, Korrekturmaßnahmen und Rückrufkommunikation vor. |
| `workflow-mdr-und-gesundheitsrobotik` | Routet Gesundheits-, Pflege-, Reha- und OP-Robotik nach MDR, MPDG, Datenschutz, Haftung und klinischen/produktbezogenen Nachweisen. |
| `workflow-normen-und-standardrecherche` | Plant Recherche nach harmonisierten Normen, ISO/IEC-Standards, C-Normen, Stand der Technik und behördlichen Leitlinien ohne Normenblindflug. |
| `workflow-open-source-und-sbom` | Sammelt FOSS, SBOM, Lizenzen, Security Advisories, Maintainer-Risiken und regulatorische Verantwortungsfragen. |
| `workflow-post-market-monitoring` | Baut Post-Market-Monitoring für Robotik: Reklamationen, Vorfälle, Patches, Trends, Rückrufschwellen und Management-Review. |
| `workflow-presse-und-krisenkommunikation` | Bereitet Kommunikation nach Unfall, Rückruf oder Datenschutzvorfall vor: sachlich, rechtlich vorsichtig, kundenverständlich und belegbar. |
| `workflow-privacy-by-design-sprint` | Führt Produktteam durch Privacy-by-Design für Roboter: Sensorik, lokale Verarbeitung, Datenminimierung, Rollen, Transparenz und Löschkonzept. |
| `workflow-produkt-und-rollenprofil` | Erstellt ein Produkt- und Rollenprofil: Hersteller, Anbieter, Importeur, Händler, Betreiber, Integrator, KI-Anbieter, Wartungsdienstleister und Nutzer. |
| `workflow-rechtsregime-matrix` | Baut eine Regime-Matrix aus Maschinenverordnung, KI-VO, ProdSG/GPSR, ProdHaftG/PLD, MDR, DSGVO, CRA, Data Act, NIS2 und Vertrag. |
| `workflow-risikoklassifizierung-schnelltest` | Führt durch Risikoklassen: Maschine, Sicherheitsbauteil, Hochrisiko-KI, Medizinprodukt, Verbraucherprodukt, kritische Infrastruktur, Beschäftigtendaten. |
| `workflow-rueckruf-und-field-action` | Plant freiwillige oder behördliche Korrekturmaßnahme: Risiko, Reichweite, Kundenliste, Software-Patch, Austausch, Stilllegung und Nachweisführung. |
| `workflow-sachverstaendigenbriefing` | Briefing für technische Sachverständige: Prüfgegenstand, Hypothesen, Logdaten, Testaufbau, Reproduzierbarkeit und Grenzen der rechtlichen Bewertung. |
| `workflow-security-by-design-sprint` | Führt Produktteam durch Security-by-Design: Bedrohungsmodell, Updatekanal, SBOM, Schwachstellenprozess, Logging und Notfallplan. |
| `workflow-unfall-incident-response` | Leitet nach Unfall, Beinaheunfall, Datenpanne oder Cybervorfall: Sicherung, Meldungen, Beweise, Kommunikation, Rückruf, Betreiber- und Herstellerfragen. |
| `workflow-update-und-change-control` | Prüft Softwareupdates, KI-Modellwechsel, Fine-Tuning, Parametrisierung und wesentliche Veränderung mit Dokumentationsspur. |
| `workflow-versicherungs-und-regressakte` | Ordnet Versicherung, Produkthaftpflicht, Cyberversicherung, D&O, Regress gegen Lieferanten und Schadensdokumentation. |
| `workflow-vertrags-und-lieferkettenintake` | Erfasst Lieferkette, RaaS-Vertrag, Wartung, Softwarelizenz, Cloud, Datenrechte, FOSS, Indemnity, Versicherung und Regressfenster. |
| `workflow-zweckbestimmung-und-usecase` | Kläre Zweckbestimmung, vernünftigerweise vorhersehbaren Gebrauch, Fehlanwendung, Hochrisiko-Nähe und spätere Zweckänderung. |
| `zweckbestimmung-enge-nutzungsbedingungen` | Bewertet enge Zweckbestimmungen, Nutzungsbedingungen, vorhersehbare Fehlanwendung und regulatorische Verlagerung auf Betreiber. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

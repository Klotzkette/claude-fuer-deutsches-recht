# Energierecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`energierecht`) | [`energierecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/energierecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin** (`batteriespeicher-brandenburg-berlin-resilienz`) | [Gesamt-PDF lesen](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [`testakte-batteriespeicher-brandenburg-berlin-resilienz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) |
| **Akte Energierecht: Stadtwerke Klotzkette AG – Quartier Hafenbogen** (`energierecht-stadtwerke-quartier`) | [Gesamt-PDF lesen](../testakten/energierecht-stadtwerke-quartier/gesamt-pdf/energierecht-stadtwerke-quartier_gesamt.pdf) | [`testakte-energierecht-stadtwerke-quartier.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-energierecht-stadtwerke-quartier.zip) |
| **Projekt Isarlicht — Kernfusion und Transrapid am Starnberger See** (`kernfusion-transrapid-starnberger-see`) | [Gesamt-PDF lesen](../testakten/kernfusion-transrapid-starnberger-see/gesamt-pdf/kernfusion-transrapid-starnberger-see_gesamt.pdf) | [`testakte-kernfusion-transrapid-starnberger-see.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kernfusion-transrapid-starnberger-see.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akten demonstrieren dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin** (`batteriespeicher-brandenburg-berlin-resilienz`) | [Gesamt-PDF lesen](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) |
| **Akte Energierecht: Stadtwerke Klotzkette AG – Quartier Hafenbogen** (`energierecht-stadtwerke-quartier`) | [Gesamt-PDF lesen](../testakten/energierecht-stadtwerke-quartier/gesamt-pdf/energierecht-stadtwerke-quartier_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-energierecht-stadtwerke-quartier.zip) |
| **Projekt Isarlicht — Kernfusion und Transrapid am Starnberger See** (`kernfusion-transrapid-starnberger-see`) | [Gesamt-PDF lesen](../testakten/kernfusion-transrapid-starnberger-see/gesamt-pdf/kernfusion-transrapid-starnberger-see_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kernfusion-transrapid-starnberger-see.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->
Vollständiger Energierechts-Assistent für Stadtwerke, Energieversorger, Wärmewirtschaft, energieintensive Unternehmen, Immobilienwirtschaft, Infrastrukturbetreiber, Contracting, Wasserstoff, E-Mobility, Transaktionen und Projektfinanzierung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn ein Anschluss an Register, Behördenportale, E-Mail, beA, Datenraum, Bank, GIS, Tabellen oder Kanzleisoftware fehlt, arbeitet es mit manuellen Uploads oder mit einem gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Eine neue Sache mit `energierecht-kommandocenter` starten.
3. Mandant, Ziel, Frist, Dokumente und gewünschtes Ergebnis nennen.
4. Bei fehlenden Systemanschlüssen `Simulation` sagen; das Plugin erzeugt dann realistische Testdaten und erklärt, welche echte Schnittstelle später ersetzt werden müsste.
5. Am Ende immer das Qualitätstor ausgeben lassen: offene Annahmen, Fristen, Rechenprüfung, Anlagen, Zuständigkeiten und nächste Schritte.

## Enthaltene Skills

- `energierecht-kommandocenter` - Energierecht-Kommandocenter
- `energierecht-infrastrukturprojekte` - Energieinfrastrukturprojekte
- `energierecht-netz-speicher-zugang` - Netz-, Speicher- und Anschlussregulierung
- `energierecht-energievertraege` - Energieverträge
- `energierecht-vertrieb-marktrollen` - Energievertrieb und Marktrollen
- `energierecht-industriekunden` - Industriekunden und Kostenoptimierung
- `energierecht-eeg-kwkg-erzeugung` - EEG, KWKG und Erzeugung
- `energierecht-waerme-quartier` - Wärme, Quartier und Fernwärme
- `energierecht-emobility-wasserstoff` - E-Mobility, Wasserstoff und Power-to-Gas
- `energierecht-wettbewerb` - Energie und Wettbewerb
- `energierecht-verfahren` - Verwaltungs- und Gerichtsverfahren Energie
- `energierecht-transaktionen-dd` - Energierechtliche Transaktions-Due-Diligence
- `energierecht-projektfinanzierung` - Erneuerbare-Energien-Projektfinanzierung

## Vorlagen

- `assets/templates/energie-mandatskarte.md` - Energierecht-Mandatskarte
- `assets/templates/energie-projektphasenplan.md` - Projektphasenplan Energieinfrastruktur
- `assets/templates/netzanschluss-zugangsmatrix.md` - Netzanschluss- und Zugangsmatrix
- `assets/templates/energieliefervertrag-check.md` - Energieliefervertrag-Check
- `assets/templates/waerme-quartier-playbook.md` - Wärme- und Quartiers-Playbook
- `assets/templates/industrie-umlagen-check.md` - Industrie-Umlagen- und Entlastungscheck
- `assets/templates/eeg-kwkg-foerdermatrix.md` - EEG/KWKG-Fördermatrix
- `assets/templates/vertrieb-marktrollen-map.md` - Vertrieb- und Marktrollenkarte
- `assets/templates/transaktions-dd-energielaw.md` - Energierechtliche DD-Matrix
- `assets/templates/verwaltungsverfahren-energie.md` - Energie-Verfahrensplan
- `assets/templates/wasserstoff-ptg-check.md` - Wasserstoff- und Power-to-Gas-Check
- `assets/templates/energie-wettbewerb-uwg-kartell.md` - Energie-Wettbewerbscheck

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen; unsichere Normen und Rechtsprechung werden als Prüfbedarf markiert.
- Zahlen, Fristen, Schwellenwerte und Zuständigkeiten werden sichtbar hergeleitet oder als Annahme gekennzeichnet.
- Ausgabe immer so, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

## Download

- Plugin-ZIP: [energierecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/energierecht.zip)
- Akte: [testakte-energierecht-stadtwerke-quartier.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-energierecht-stadtwerke-quartier.zip)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 92 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Energierecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei D... |
| `energierecht-eeg-kwkg-erzeugung` | EEG- und KWKG-Verguetungen für Stromerzeugungsanlagen prüfen: Einspeiseverguetung, Marktpraemie, KWK-Zuschlag. Normen: §§ 19 ff. EEG, §§ 6 ff. KWKG. Prüfraster: Anlagenanschluss, Verguetungsmodalitaeten, Direktvermarktung, Ausschreibungs... |
| `energierecht-emobility-wasserstoff` | Rechtliche Rahmenbedingungen für Elektromobilitaet und gruenen Wasserstoff prüfen: Ladepunkte, H2-Einspeisung. Normen: § 14a EnWG, EEG, GEG, EU-Verordnung Alternative Kraftstoffe. Prüfraster: Netzintegration, Foerderrecht, Liefervertrag,... |
| `energierecht-energievertraege` | Energieliefervertraege prüfen und entwerfen: Strom- und Gasliefervertraege mit Industrie- und Privatkunden. Normen: §§ 41 ff. EnWG, StromGVV, GasGVV. Prüfraster: Preisanpassungsklauseln, Laufzeiten, Sonderkündigungsrecht, Lieferbedingung... |
| `energierecht-industriekunden` | Sonderregelungen für Industriekunden im Energierecht: Netzentgeltbefreiungen, Direktleitungen, Eigenerzeugung. Normen: § 19 StromNEV, §§ 17 ff. EnWG, EEG. Prüfraster: atypische Netznutzung, Eigenversorgungsprivileg, Konzerneigenversorgun... |
| `energierecht-infrastrukturprojekte` | Energieinfrastrukturprojekte rechtlich begleiten: Leitungsgenehmigungen, Planfeststellung, Enteignung. Normen: §§ 43 ff. EnWG, NABEG, BImSchG, BauGB. Prüfraster: Genehmigungsverfahren, Einwendungen, Planfeststellungsbeschluss, Enteignung... |
| `energierecht-kommandocenter` | Navigationszentrum für alle Energierecht-Skills: Weiterleitung je Rechtsthema und Anfrageart. Normen: EnWG, EEG, KWKG, GEG. Prüfraster: Themenfeld Erzeugung/Netz/Vertrieb, Kundentyp, einschlaegige Norm. Output: Skillauswahl-Empfehlung En... |
| `energierecht-netz-speicher-zugang` | Netzanschluss und Netzzugang für Erzeugungsanlagen und Speicher prüfen. Normen: §§ 17 ff. 20 ff. EnWG, NAV. Prüfraster: Netzanschlussrecht, Anschlussbegehren, Kapazitaetsprüfung, Diskriminierungsfreiheit. Output: Netzanschluss-Rechtsguta... |
| `energierecht-projektfinanzierung` | Projektfinanzierung für Energieanlagen strukturieren: Darlehen, Sicherheiten, Ratinganforderungen. Normen: EnWG, EEG, KWKG, BGB. Prüfraster: Finanzierungsstruktur, Sicherheitenpakete, Cashflow-Analyse, Foerderdarlehen. Output: Projektfin... |
| `energierecht-transaktionen-dd` | Due Diligence bei Energierecht-Transaktionen: Kauf von Windparks, Solarprojekten, Netzen. Normen: §§ 453 ff. BGB, EnWG, EEG, KWKG. Prüfraster: Genehmigungs-Status, Netzvertrag, EEG-Verguetungsrecht, Umweltrisiken. Output: Due-Diligence-B... |
| `energierecht-verfahren` | Regulierungsverfahren und Gerichtsverfahren im Energierecht durchführen: BNetzA-Verfahren, Kartellamt. Normen: §§ 75 ff. EnWG, GWB, VwGO. Prüfraster: Verfahrenstyp, Beschwerde, Klage, Fristenmanagement. Output: Verfahrensstrategie Energi... |
| `energierecht-vertrieb-marktrollen` | Energievertrieb und Marktrollen im liberalisierten Energiemarkt: Lieferant, Netzbetreiber, Bilanzkreis. Normen: §§ 4 ff. EnWG, MaBiS-Prozesse. Prüfraster: Marktrollen, Bilanzkreisvertrag, Lieferantenwechsel. Output: Marktrollenanalyse un... |
| `energierecht-waerme-quartier` | Waermenetze und Quartiersversorgung rechtlich strukturieren: Fernwaerme, GEG-Erfuellung, lokale Waermewende. Normen: AVBFernwaermeV, GEG, EnWG, EEG. Prüfraster: Konzessionspflicht, Preisanpassungsklauseln, GEG-Anforderungen. Output: Waer... |
| `energierecht-wettbewerb` | Wettbewerbs- und Kartellrecht im Energiesektor prüfen: Marktmacht, Diskriminierung, Missbrauch. Normen: §§ 18 ff. GWB, Art. 101 102 AEUV, EnWG. Prüfraster: Marktabgrenzung, Marktmacht, Diskriminierungsverbot, Entflechtung. Output: Kartel... |
| `er-bess-abfall-recycling-rueckbau` | Prüft Rückbaupflichten, Batterieentsorgung, Recycling, Herstellerpflichten und Grundstücksrückgabe. |
| `er-bess-abstandsflaechen-und-layout` | Prüft Containerabstände, Transformatoren, Umrichter, Zaun, Leitungen, Feuerwehrbewegungsflächen und Nachbarpositionen. |
| `er-bess-baurecht-brandenburg` | Prüft Zulässigkeit im Außenbereich, Bebauungsplan, Sondergebiet Energie, Privilegierung, Erschließung und Nachbarrechte. |
| `er-bess-behoerdenstrategie` | Plant Vorgespräche mit Gemeinde, Bauaufsicht, Immissionsschutz, Feuerwehr, Netzbetreiber, Polizei und Datenschutzaufsicht. |
| `er-bess-bimschg-und-4-bimschv` | Prüft, ob Batteriespeicher immissionsschutzrechtlich genehmigungsbedürftig ist oder Nebenanlagen/Generatoren den Weg ändern. |
| `er-bess-brandschutz-lithium-ionen` | Prüft Brandabschnitte, Abstände, Löschwasserkonzept, Thermal Runaway, Zufahrt, Evakuierung und Einsatzplan. |
| `er-bess-co-location-pv-wind` | Prüft Batteriespeicher neben Erneuerbaren: gemeinsame Messeinrichtung, Förderlogik, Netzanschluss, Direktleitung und Curtailment. |
| `er-bess-datenschutz-video-leitwarte` | Prüft Videoüberwachung, Zutrittslogs, Fernwartung, Auftragsverarbeitung und Drittlandzugriffe. |
| `er-bess-dieselgenerator-notstrom` | Prüft, ob Dieselgeneratoren als Nebenanlage genehmigungspflichtig, emissionsrelevant oder sicherheitskritisch sind. |
| `er-bess-epc-o-and-m-vertraege` | Prüft Bau-/Liefervertrag, O&M, Garantien, Degradation, Availability, LDs, Ersatzteile und Cyberpflichten. |
| `er-bess-fca-agnes-bnetza` | Prüft Netzanschlussdokumente nach BNetzA/Festlegungslogik und markiert, was im konkreten Vertrag fehlt. |
| `er-bess-finanzierung-bankability` | Prüft Projektfinanzierung, Sicherheiten, Erlösmodell, Netzanschlussrisiko, Bau-/Betriebsrisiko und Insurance DD. |
| `er-bess-kaltstart-projektaufnahme` | Batteriespeicherprojekt aufnehmen: Projektgröße, Standort, Netzebene, Betreiberrolle, Fristen, Unterlagen und Zieloutput. |
| `er-bess-kapazitaetsmarkt-grundlast` | Ordnet Aussagen zu Grundlast, gesicherter Leistung, Kapazitätsmarkt, Gaskraftwerken und Speicherfunktion rechtlich ein. |
| `er-bess-kritis-nis2-cyber` | Prüft, ob Speicher, Leitwarte, Netzanschluss oder Betreiber kritische Anlage/IT-Sicherheitsfall sind. |
| `er-bess-marktrollen-bilanzkreis` | Prüft Betreiber, Lieferant, Direktvermarkter, Bilanzkreis, Redispatch, Fahrplan, MaStR und Datenpflichten. |
| `er-bess-naturschutz-artenschutz` | Prüft Eingriffsregelung, Artenschutz, Ausgleich, Landschaftsbild, Ackerflächen und FFH/Vogelschutz. |
| `er-bess-netzanschluss-hoehe-spannung` | Prüft Netzanschlussbegehren, Anschlusszusage, Netzverträglichkeitsprüfung, Kostentragung und Zeitplan. |
| `er-bess-netzentgelte-und-abgaben` | Prüft Strombezug, Einspeicherung, Ausspeicherung, Netzentgelte, Umlagen, Messung und Entlastungen. |
| `er-bess-output-board-paper` | Erstellt Entscheidungsvorlage für Vorstand/Geschäftsführung/Aufsichtsrat zu Investition, Risiko, Genehmigung und Finanzierung. |
| `er-bess-physische-sicherheit-terror` | Prüft Zaun, Zutritt, Drohnen, Video, Wachschutz, Polizei/Feuerwehr, Geheimschutz und Betreiberpflichten. |
| `er-bess-power-quality-emv` | Prüft Oberschwingungen, Spannungshaltung, Umrichter, elektromagnetische Verträglichkeit und Nachbar-/Netzbetreiberforderungen. |
| `er-bess-ppa-und-merchant-risk` | Prüft Erlösverträge für Speicher: Tolling, Capacity, Arbitrage, Regelenergie, Floor/Cap und Verfügbarkeitsgarantien. |
| `er-bess-produktsicherheit-haftung` | Prüft Batteriecontainer, BMS, Wechselrichter, CE, Herstellerdokumentation, Rückruf und Betreiberhaftung. |
| `er-bess-projektakte-qualitygate` | Prüft die gesamte Speicherakte auf Lücken, Widersprüche, fehlende Quellen, falsche Rollen und unrealistische Annahmen. |
| `er-bess-rechtsmittel-und-nachbarabwehr` | Prüft Widerspruch/Klage, Nachbarrechte, Sofortvollzug, Baustopp, Umweltverbandsklage und Verteidigung. |
| `er-bess-regelenergie-systemdienstleistung` | Prüft Präqualifikation, Vermarktung, Verfügbarkeit, Messdaten, Sanktionen und Aggregator-Struktur. |
| `er-bess-vergabe-kommunale-stadtwerke` | Prüft, ob Stadtwerk, Kommune oder öffentlich beherrschte Gesellschaft Vergaberecht und Beihilfe beachten muss. |
| `er-bess-versicherung-und-schadenfall` | Prüft Property, BI, Cyber, Haftpflicht, Umwelt, Bauleistung, Garantien und Claims-Prozess. |
| `er-bess-wasser-awsv-und-boden` | Prüft Kühlmittel, Transformatorenöl, Löschwasser, Bodenversiegelung, Havariebecken und Grundwasserschutz. |
| `er-einfuehrung-system` | Energierecht einfuehrend: Saeulen Strom, Gas, Waerme. Erzeugung, Netz, Vertrieb, Speicher. Kernnormen EnWG, EEG, KWKG, GEG, EnEfG, StromNZV, GasNZV, KraftNAV. Akteure BNetzA, Landesregulierer, Uebertragungsnetzbetreiber, Verteilnetzbetre... |
| `er-fusion-bauleitplanung-starnberger-see` | Prüft Raumordnung, Bauleitplanung, Landschaftsschutz, Wasserrecht, Seenschutz und Nachbarrechte. |
| `er-fusion-buergerbeteiligung-und-politik` | Plant Beteiligung, Umweltinformationen, Presse, Einwendungen, Bürgerentscheid-Schnittstellen und Konfliktmanagement. |
| `er-fusion-foerderung-beihilfe` | Prüft staatliche Förderung, EU-Beihilfe, IP-Rechte, Kooperation mit Forschungseinrichtungen und Exportkontrolle. |
| `er-fusion-kaltstart-regulierungsweg` | Ordnet Fusionsreaktor-Projekt zwischen Atomrecht, Strahlenschutz, Baurecht, Immissionsschutz und Forschungsförderung. |
| `er-fusion-netzanschluss-und-systemnutzen` | Prüft Netzanschluss, gesicherte Leistung, PPA, Marktrolle, Wasserstoff-/Wärme-Kopplung und Systemintegration. |
| `er-fusion-sicherheitsnachweis` | Prüft Sicherheitskonzept, Störfallszenarien, Notfallplanung, Sachverständige, Feuerwehr und Katastrophenschutz. |
| `er-fusion-strahlenschutz-neutronen` | Prüft Strahlenschutzfragen, Aktivierung von Materialien, Überwachung, Dosismanagement und Entsorgung. |
| `er-fusion-transrapid-anbindung` | Prüft Planungsrecht, Infrastrukturzulassung, Grundstücke, Sicherheit, Betreiberrollen und Schnittstellen zum Energieprojekt. |
| `er-h2-electrolyseur-foerderung` | Spezialfall Wasserstoff-Elektrolyseur: Foerderwege (Wasserstoffstrategie Bund, EU-Wasserstoffbank, IPCEI), Strompreisbedingungen Industrieprivileg, Anschluss Netz, Sicherheitsabstaende BImSchG, Hochdruck-Pipeline-Genehmigung. Pruefraster... |
| `er-netzanschluss-praesumtion-spezial` | Spezialfall Netzanschluss-Verweigerung trotz EEG-Vorrang: Pflicht zur Optimierung und Verstaerkung § 12 EEG, wirtschaftliche Zumutbarkeit, einstweilige Verfuegung gegen Netzbetreiber. Schriftsatzbausteine und Rechtsprechung BGH und Clear... |
| `er-netzentgelte-rechtsfragen` | Netzentgelte aktuell: § 19 Abs. 2 StromNEV individuelle Netzentgelte, BNetzA-Festlegung StromNEV 2027 ff., Stationaere Speicher, Industriestromentgelt. Praxis: Antragsverfahren, Anwendungsfaelle Energieintensive, Klagewege gegen BNetzA-F... |
| `er-redispatch-3-0-spezial` | Spezialfall Redispatch 3.0: Einbeziehung Anlagen kleiner 100 kW, Marktrolle EIV, Datenaustauschformate, Entschaedigung, Bilanzierungsverantwortung. Pruefraster fuer Anlagenbetreiber und Aggregator. Schnittstelle Marktstammdatenregister. |
| `er-stakeholder-mapping-energie` | Stakeholder-Mapping fuer Energieprojekte: Vorhabentraeger, Netzbetreiber, BNetzA, Landesregulierer, Kommune, Naturschutz, Anwohnerinitiativen, Foerdergeber. Pro Stakeholder Interesse, Hebel, Risiko. Mustertabelle fuer Projektsteuerung. |
| `er-typ-anfrage-mandanten-routing` | Anfrage-Routing im Energierecht: 5 typische Mandantenanfragen (Anschluss, Vertrag, Foerderung, Verfahren, Streit) und ihre Sub-Skills im Plugin. Entscheidungsbaum, der zur richtigen Detail-Skill leitet. |
| `ladeinfrastruktur-spezial-vertragskette` | Spezialfall Ladeinfrastruktur: Vertragskette Standortgeber, CPO, eMSP, Roaming-Hub. Rechte aus AFIR (Alternative Fuels Infrastructure Regulation), Anforderungen an Bezahlsysteme, Preis-Transparenz, ad-hoc-Laden. Mustertexte und typische... |
| `ppa-cppa-vertragsspezialitaeten` | PPA und Corporate PPA Vertragsspezialitaeten: Pay as produced / baseload / sleeved, Marktwertanpassung, Negativpreis-Klausel, Curtailment, Bilanzkreis, Herkunftsnachweise. Risikoverteilung Stromabnehmer und Erzeuger. Mustertexte fuer 10-... |
| `spezial-anfrage-mehrparteien-konflikt-und-interessen` | Anfrage: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-einfuehrung-mandantenkommunikation-entscheidungsvorlage` | Einfuehrung: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-energieprojekt-intake-und-regulierungsweiche` | Energieprojekt-Intake mit Regulierungs-, Netz- und Förderweiche: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-energierecht-erstpruefung-und-mandatsziel` | Energierecht: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-industrie-schriftsatz-brief-und-memo-bausteine` | Industrie: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kwkg-verhandlung-vergleich-und-eskalation` | Kwkg: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-livecheck-fristennotiz-und-naechster-schritt` | Livecheck: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-netzanschluss-formular-portal-und-einreichung` | Netzanschluss: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-netze-risikoampel-und-gegenargumente` | Netze: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-praesumtion-red-team-und-qualitaetskontrolle` | Praesumtion: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-projektfinanzierung-compliance-dokumentation-und-akte` | Projektfinanzierung: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsquellen-sonderfall-und-edge-case` | Rechtsquellen: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-routing-internationaler-bezug-und-schnittstellen` | Routing: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-stadtwerke-tatbestand-beweis-und-belege` | Stadtwerke: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-system-beweislast-und-darlegungslast` | System: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-transaktionen-zahlen-schwellen-und-berechnung` | Transaktionen: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verfahren-livequellen-und-rechtsprechungscheck` | Verfahren: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-versorger-fristen-form-und-zustaendigkeit` | Versorger: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vertrieb-behoerden-gericht-und-registerweg` | Vertrieb: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-waerme-dokumentenmatrix-und-lueckenliste` | Waerme: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `strompreisbremse-und-extras` | Strompreisbremse, Energiepreisbremsengesetze (StromPBG, EWPBG) historisch und Folgen: Abschoepfung, Soforthilfe, Beihilferecht. Aktuelle Lage 2025/2026 nach Auslaufen, offene Glaubensfragen Wirtschaftsministerien, Bundesverfassungsgerich... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin energierecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin energierecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin energierecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin energierecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin energierecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin energierecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin energierecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin energierecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin energierecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin energierecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

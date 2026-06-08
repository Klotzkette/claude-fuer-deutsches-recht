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

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 92 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anfrage-mehrparteien-konflikt-und-interessen` | Anfrage: Mehrparteienkonflikt und Interessenmatrix; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen Tatbe... |
| `anschluss` | Einstieg, Schnelltriage und Fallrouting im Energierecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-U... |
| `bess-abfall-recycling-rueckbau` | Prüft Rückbaupflichten, Batterieentsorgung, Recycling, Herstellerpflichten und Grundstücksrückgabe im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit... |
| `bess-abstandsflaechen-baurecht-brandenburg` | Prüft Containerabstände, Transformatoren, Umrichter, Zaun, Leitungen, Feuerwehrbewegungsflächen und Nachbarpositionen im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prior... |
| `bess-baurecht-brandenburg` | Prüft Zulässigkeit im Außenbereich, Bebauungsplan, Sondergebiet Energie, Privilegierung, Erschließung und Nachbarrechte im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert pri... |
| `bess-behoerdenstrategie` | Plant Vorgespräche mit Gemeinde, Bauaufsicht, Immissionsschutz, Feuerwehr, Netzbetreiber, Polizei und Datenschutzaufsicht im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert p... |
| `bess-bimschg-und-4-bimschv` | Prüft, ob Batteriespeicher immissionsschutzrechtlich genehmigungsbedürftig ist oder Nebenanlagen/Generatoren den Weg ändern im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `bess-brandschutz-co-location-datenschutz` | Prüft Brandabschnitte, Abstände, Löschwasserkonzept, Thermal Runaway, Zufahrt, Evakuierung und Einsatzplan im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Ou... |
| `bess-co-location-pv-wind` | Prüft Batteriespeicher neben Erneuerbaren: gemeinsame Messeinrichtung, Förderlogik, Netzanschluss, Direktleitung und Curtailment im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Li... |
| `bess-datenschutz-video-leitwarte` | Prüft Videoüberwachung, Zutrittslogs, Fernwartung, Auftragsverarbeitung und Drittlandzugriffe im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm... |
| `bess-dieselgenerator-notstrom` | Prüft, ob Dieselgeneratoren als Nebenanlage genehmigungspflichtig, emissionsrelevant oder sicherheitskritisch sind im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisi... |
| `bess-epc-fca-agnes-finanzierung` | Prüft Bau-/Liefervertrag, O&M, Garantien, Degradation, Availability, LDs, Ersatzteile und Cyberpflichten im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Outp... |
| `bess-fca-agnes-bnetza` | Prüft Netzanschlussdokumente nach BNetzA/Festlegungslogik und markiert, was im konkreten Vertrag fehlt im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `bess-finanzierung-bankability` | Prüft Projektfinanzierung, Sicherheiten, Erlösmodell, Netzanschlussrisiko, Bau-/Betriebsrisiko und Insurance DD im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisiert... |
| `bess-kaltstart-projektaufnahme` | Batteriespeicherprojekt aufnehmen: Projektgröße, Standort, Netzebene, Betreiberrolle, Fristen, Unterlagen und Zieloutput. |
| `bess-kapazitaetsmarkt-grundlast` | Ordnet Aussagen zu Grundlast, gesicherter Leistung, Kapazitätsmarkt, Gaskraftwerken und Speicherfunktion rechtlich ein im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prio... |
| `bess-kritis-marktrollen-bilanzkreis` | Prüft, ob Speicher, Leitwarte, Netzanschluss oder Betreiber kritische Anlage/IT-Sicherheitsfall sind im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output m... |
| `bess-marktrollen-bilanzkreis` | Prüft Betreiber, Lieferant, Direktvermarkter, Bilanzkreis, Redispatch, Fahrplan, MaStR und Datenpflichten im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Out... |
| `bess-naturschutz-artenschutz` | Prüft Eingriffsregelung, Artenschutz, Ausgleich, Landschaftsbild, Ackerflächen und FFH/Vogelschutz im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit... |
| `bess-netzanschluss-hoehe-spannung` | Prüft Netzanschlussbegehren, Anschlusszusage, Netzverträglichkeitsprüfung, Kostentragung und Zeitplan im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `bess-netzentgelte-board-physische` | Prüft Strombezug, Einspeicherung, Ausspeicherung, Netzentgelte, Umlagen, Messung und Entlastungen im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit... |
| `bess-output-board-paper` | Erstellt Entscheidungsvorlage für Vorstand/Geschäftsführung/Aufsichtsrat zu Investition, Risiko, Genehmigung und Finanzierung im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefe... |
| `bess-physische-sicherheit-terror` | Prüft Zaun, Zutritt, Drohnen, Video, Wachschutz, Polizei/Feuerwehr, Geheimschutz und Betreiberpflichten im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Outpu... |
| `bess-power-quality-emv` | Prüft Oberschwingungen, Spannungshaltung, Umrichter, elektromagnetische Verträglichkeit und Nachbar-/Netzbetreiberforderungen im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefe... |
| `bess-ppa-projektakte-rechtsmittel` | Prüft Erlösverträge für Speicher: Tolling, Capacity, Arbitrage, Regelenergie, Floor/Cap und Verfügbarkeitsgarantien im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prioris... |
| `bess-produktsicherheit-haftung-versicherung-schadenfall` | Prüft Batteriecontainer, BMS, Wechselrichter, CE, Herstellerdokumentation, Rückruf und Betreiberhaftung im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Outpu... |
| `bess-projektakte-qualitygate` | Prüft die gesamte Speicherakte auf Lücken, Widersprüche, fehlende Quellen, falsche Rollen und unrealistische Annahmen im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prior... |
| `bess-rechtsmittel-und-nachbarabwehr` | Prüft Widerspruch/Klage, Nachbarrechte, Sofortvollzug, Baustopp, Umweltverbandsklage und Verteidigung im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `bess-regelenergie-systemdienstleistung` | Prüft Präqualifikation, Vermarktung, Verfügbarkeit, Messdaten, Sanktionen und Aggregator-Struktur im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit... |
| `bess-versicherung-und-schadenfall` | Prüft Property, BI, Cyber, Haftpflicht, Umwelt, Bauleistung, Garantien und Claims-Prozess im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pin... |
| `bess-wasser-awsv-und-boden` | Prüft Kühlmittel, Transformatorenöl, Löschwasser, Bodenversiegelung, Havariebecken und Grundwasserschutz im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Outp... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `eeg-kwkg-erzeugung` | EEG- und KWKG-Verguetungen für Stromerzeugungsanlagen prüfen: Einspeiseverguetung, Marktpraemie, KWK-Zuschlag. Normen: §§ 19 ff. EEG, §§ 6 ff. KWKG. Prüfraster: Anlagenanschluss, Verguetungsmodalitaeten, Direktvermarktung, Ausschreibungs... |
| `einfuehrung-energieprojekt-intake` | Einfuehrung: Mandantenkommunikation und Entscheidungsvorlage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschläg... |
| `einfuehrung-system` | Energierecht einfuehrend: Saeulen Strom, Gas, Waerme. Erzeugung, Netz, Vertrieb, Speicher. Kernnormen EnWG, EEG, KWKG, GEG, EnEfG, StromNZV, GasNZV, KraftNAV. Akteure BNetzA, Landesregulierer, Uebertragungsnetzbetreiber, Verteilnetzbetre... |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `emobility-wasserstoff` | Rechtliche Rahmenbedingungen für Elektromobilitaet und gruenen Wasserstoff prüfen: Ladepunkte, H2-Einspeisung. Normen: § 14a EnWG, EEG, GEG, EU-Verordnung Alternative Kraftstoffe. Prüfraster: Netzintegration, Foerderrecht, Liefervertrag,... |
| `energieprojekt-intake-und-regulierungsweiche` | Energieprojekt-Intake mit Regulierungs-, Netz- und Förderweiche: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Energierecht: prüft konkret die einschlägigen Tatbestan... |
| `energierecht-erstpruefung-und-mandatsziel` | Energierecht: Erstprüfung, Rollenklärung und Mandatsziel; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen... |
| `energievertraege` | Energieliefervertraege prüfen und entwerfen: Strom- und Gasliefervertraege mit Industrie- und Privatkunden. Normen: §§ 41 ff. EnWG, StromGVV, GasGVV. Prüfraster: Preisanpassungsklauseln, Laufzeiten, Sonderkündigungsrecht, Lieferbedingung... |
| `fusion-bauleitplanung-starnberger-see` | Prüft Raumordnung, Bauleitplanung, Landschaftsschutz, Wasserrecht, Seenschutz und Nachbarrechte im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit No... |
| `fusion-buergerbeteiligung-foerderung` | Plant Beteiligung, Umweltinformationen, Presse, Einwendungen, Bürgerentscheid-Schnittstellen und Konfliktmanagement im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prioris... |
| `fusion-foerderung-beihilfe` | Prüft staatliche Förderung, EU-Beihilfe, IP-Rechte, Kooperation mit Forschungseinrichtungen und Exportkontrolle im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisiert... |
| `fusion-kaltstart-regulierungsweg` | Ordnet Fusionsreaktor-Projekt zwischen Atomrecht, Strahlenschutz, Baurecht, Immissionsschutz und Forschungsförderung. |
| `fusion-netzanschluss-und-systemnutzen` | Prüft Netzanschluss, gesicherte Leistung, PPA, Marktrolle, Wasserstoff-/Wärme-Kopplung und Systemintegration im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten... |
| `fusion-sicherheitsnachweis` | Prüft Sicherheitskonzept, Störfallszenarien, Notfallplanung, Sachverständige, Feuerwehr und Katastrophenschutz im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierte... |
| `fusion-strahlenschutz-neutronen-transrapid-anbindung-h2` | Prüft Strahlenschutzfragen, Aktivierung von Materialien, Überwachung, Dosismanagement und Entsorgung im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output m... |
| `fusion-transrapid-anbindung` | Prüft Planungsrecht, Infrastrukturzulassung, Grundstücke, Sicherheit, Betreiberrollen und Schnittstellen zum Energieprojekt im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `h2-electrolyseur-foerderung` | Spezialfall Wasserstoff-Elektrolyseur: Foerderwege (Wasserstoffstrategie Bund, EU-Wasserstoffbank, IPCEI), Strompreisbedingungen Industrieprivileg, Anschluss Netz, Sicherheitsabstaende BImSchG, Hochdruck-Pipeline-Genehmigung. Pruefraster... |
| `industrie-schriftsatz-brief-und-memo-bausteine` | Industrie: Schriftsatz-, Brief- und Memo-Bausteine; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen Tatbe... |
| `industriekunden` | Sonderregelungen für Industriekunden im Energierecht: Netzentgeltbefreiungen, Direktleitungen, Eigenerzeugung. Normen: § 19 StromNEV, §§ 17 ff. EnWG, EEG. Prüfraster: atypische Netznutzung, Eigenversorgungsprivileg, Konzerneigenversorgun... |
| `infrastrukturprojekte` | Energieinfrastrukturprojekte rechtlich begleiten: Leitungsgenehmigungen, Planfeststellung, Enteignung. Normen: §§ 43 ff. EnWG, NABEG, BImSchG, BauGB. Prüfraster: Genehmigungsverfahren, Einwendungen, Planfeststellungsbeschluss, Enteignung... |
| `kommunale-stadtwerke-vergabe-und-beihilfe` | Prüft, ob Stadtwerk, Kommune oder öffentlich beherrschte Gesellschaft Vergaberecht und Beihilfe beachten muss im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten... |
| `kwkg-netzanschluss-netze-praesumtion-red-team-korrektur` | Kwkg: Verhandlung, Vergleich und Eskalation; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen Tatbestandsm... |
| `ladeinfrastruktur-spezial-vertragskette` | Spezialfall Ladeinfrastruktur: Vertragskette Standortgeber, CPO, eMSP, Roaming-Hub. Rechte aus AFIR (Alternative Fuels Infrastructure Regulation), Anforderungen an Bezahlsysteme, Preis-Transparenz, ad-hoc-Laden. Mustertexte und typische... |
| `livecheck-fristennotiz-versorger` | Livecheck: Fristennotiz und nächster Schritt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen Tatbestands... |
| `mandantenkommunikation-output-waehlen-redteam` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lie... |
| `netz-speicher` | Navigationszentrum für alle Energierecht-Skills: Weiterleitung je Rechtsthema und Anfrageart. Normen: EnWG, EEG, KWKG, GEG. Prüfraster: Themenfeld Erzeugung/Netz/Vertrieb, Kundentyp, einschlaegige Norm. Output: Skillauswahl-Empfehlung En... |
| `netz-speicher-zugang` | Netzanschluss und Netzzugang für Erzeugungsanlagen und Speicher prüfen. Normen: §§ 17 ff. 20 ff. EnWG, NAV. Prüfraster: Netzanschlussrecht, Anschlussbegehren, Kapazitaetsprüfung, Diskriminierungsfreiheit. Output: Netzanschluss-Rechtsguta... |
| `netzanschluss-formular-portal-und-einreichung` | Netzanschluss: Formular, Portal und Einreichungslogik; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen Ta... |
| `netzanschluss-praesumtion-spezial` | Spezialfall Netzanschluss-Verweigerung trotz EEG-Vorrang: Pflicht zur Optimierung und Verstaerkung § 12 EEG, wirtschaftliche Zumutbarkeit, einstweilige Verfuegung gegen Netzbetreiber. Schriftsatzbausteine und Rechtsprechung BGH und Clear... |
| `netze-risikoampel-und-gegenargumente` | Netze: Risikoampel, Gegenargumente und Verteidigungslinien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägig... |
| `netzentgelte-rechtsfragen-redispatch-spezial-typ-anfrage` | Netzentgelte aktuell: § 19 Abs. 2 StromNEV individuelle Netzentgelte, BNetzA-Festlegung StromNEV 2027 ff., Stationaere Speicher, Industriestromentgelt. Praxis: Antragsverfahren, Anwendungsfaelle Energieintensive, Klagewege gegen BNetzA-F... |
| `ppa-cppa-vertragsspezialitaeten` | PPA und Corporate PPA Vertragsspezialitaeten: Pay as produced / baseload / sleeved, Marktwertanpassung, Negativpreis-Klausel, Curtailment, Bilanzkreis, Herkunftsnachweise. Risikoverteilung Stromabnehmer und Erzeuger. Mustertexte für 10-J... |
| `praesumtion-red-team-und-qualitaetskontrolle` | Praesumtion: Red-Team und Qualitätskontrolle; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen Tatbestands... |
| `projektfinanzierung` | Projektfinanzierung für Energieanlagen strukturieren: Darlehen, Sicherheiten, Ratinganforderungen. Normen: EnWG, EEG, KWKG, BGB. Prüfraster: Finanzierungsstruktur, Sicherheitenpakete, Cashflow-Analyse, Foerderdarlehen. Output: Projektfin... |
| `projektfinanzierung-stadtwerke-system` | Projektfinanzierung: Compliance-Dokumentation und Aktenvermerk; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschl... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rechtsquellen-sonderfall-edge-case` | Rechtsquellen: Quellenprüfung; Sonderfall und Edge-Case-Prüfung: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `redispatch-3-0-spezial` | Spezialfall Redispatch 3.0: Einbeziehung Anlagen kleiner 100 kW, Marktrolle EIV, Datenaustauschformate, Entschaedigung, Bilanzierungsverantwortung. Pruefraster für Anlagenbetreiber und Aggregator. Schnittstelle Marktstammdatenregister im... |
| `routing-internationaler-bezug-und-schnittstellen` | Routing: Internationaler Bezug und Schnittstellen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen Tatbes... |
| `stadtwerke-tatbestand-beweis-und-belege` | Stadtwerke: Tatbestandsmerkmale, Beweisfragen und Beleglage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägi... |
| `stakeholder-mapping-energie` | Stakeholder-Mapping für Energieprojekte: Vorhabentraeger, Netzbetreiber, BNetzA, Landesregulierer, Kommune, Naturschutz, Anwohnerinitiativen, Foerdergeber. Pro Stakeholder Interesse, Hebel, Risiko. Mustertabelle für Projektsteuerung im E... |
| `strompreisbremse-und-extras` | Strompreisbremse, Energiepreisbremsengesetze (StromPBG, EWPBG) historisch und Folgen: Abschoepfung, Soforthilfe, Beihilferecht. Aktuelle Lage 2025/2026 nach Auslaufen, offene Glaubensfragen Wirtschaftsministerien, Bundesverfassungsgerich... |
| `system-beweislast-und-darlegungslast` | System: Beweislast, Darlegungslast und Substantiierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen T... |
| `transaktionen-dd` | Due Diligence bei Energierecht-Transaktionen: Kauf von Windparks, Solarprojekten, Netzen. Normen: §§ 453 ff. BGB, EnWG, EEG, KWKG. Prüfraster: Genehmigungs-Status, Netzvertrag, EEG-Verguetungsrecht, Umweltrisiken. Output: Due-Diligence-B... |
| `transaktionen-vertrieb-waerme` | Transaktionen: Zahlen, Schwellenwerte und Berechnung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen Tat... |
| `typ-anfrage-mandanten-routing` | Anfrage-Routing im Energierecht: 5 typische Mandantenanfragen (Anschluss, Vertrag, Förderung, Verfahren, Streit) und ihre Sub-Skills im Plugin. Entscheidungsbaum, der zur richtigen Detail-Skill leitet im Energierecht: prüft konkret die e... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verfahren` | Regulierungsverfahren und Gerichtsverfahren im Energierecht durchführen: BNetzA-Verfahren, Kartellamt. Normen: §§ 75 ff. EnWG, GWB, VwGO. Prüfraster: Verfahrenstyp, Beschwerde, Klage, Fristenmanagement. Output: Verfahrensstrategie Energi... |
| `verfahren-quellenkarte` | Verfahren Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `versorger-fristen-form-und-zustaendigkeit` | Versorger: Fristen, Form, Zuständigkeit und Rechtsweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen Ta... |
| `vertrieb-behoerden-gericht-und-registerweg` | Vertrieb: Behörden-, Gerichts- oder Registerweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen Tatbesta... |
| `vertrieb-marktrollen-waerme` | Energievertrieb und Marktrollen im liberalisierten Energiemarkt: Lieferant, Netzbetreiber, Bilanzkreis. Normen: §§ 4 ff. EnWG, MaBiS-Prozesse. Prüfraster: Marktrollen, Bilanzkreisvertrag, Lieferantenwechsel. Output: Marktrollenanalyse un... |
| `waerme-dokumentenmatrix-und-lueckenliste` | Waerme: Dokumentenmatrix, Lückenliste und Nachforderung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Energierecht: prüft konkret die einschlägigen... |
| `waerme-quartier` | Waermenetze und Quartiersversorgung rechtlich strukturieren: Fernwaerme, GEG-Erfuellung, lokale Waermewende. Normen: AVBFernwaermeV, GEG, EnWG, EEG. Prüfraster: Konzessionspflicht, Preisanpassungsklauseln, GEG-Anforderungen. Output: Waer... |
| `wettbewerb` | Wettbewerbs- und Kartellrecht im Energiesektor prüfen: Marktmacht, Diskriminierung, Missbrauch. Normen: §§ 18 ff. GWB, Art. 101 102 AEUV, EnWG. Prüfraster: Marktabgrenzung, Marktmacht, Diskriminierungsverbot, Entflechtung. Output: Kartel... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Ou... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert pri... |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prior... |
| `workflow-output-waehlen` | Output wählen: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefe... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Energierecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priori... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

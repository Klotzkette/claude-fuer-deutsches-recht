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

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `einfuehrung-energieprojekt-intake` | Einfuehrung Mandantenkommunikation Entscheidungsvorlage, Energieprojekt Intake Und Regulierungsweiche, Energierecht Erstpruefung Und Mandatsziel, Industrie Schriftsatz Brief Und Memo Bausteine: wählt den konkreten Prüfpfad, trennt Frist,... |
| `energie-bess-produktsicherheit-haftung-versicherung-schadenfall` | Bess Produktsicherheit Haftung / Bess Versicherung Schadenfall / Stakeholder Mapping Energie / Energierecht Eeg Kwkg Erzeugung: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten b... |
| `energie-bess-vergabe-kommunale-wasser-awsv-einfuehrung-system` | Bess Vergabe Kommunale Stadtwerke / Bess Wasser Awsv Boden / Einfuehrung System / Fusion Bauleitplanung Starnberger See: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastba... |
| `energie-fusion-strahlenschutz-neutronen-transrapid-anbindung-h2` | Fusion Strahlenschutz Neutronen / Fusion Transrapid Anbindung / H2 Electrolyseur Foerderung / Netzanschluss Praesumtion Spezial: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten... |
| `energie-mandantenkommunikation-output-waehlen-redteam` | Mandantenkommunikation, Output Waehlen, Redteam Qualitygate, Energierecht Verfahren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `energie-netzentgelte-rechtsfragen-redispatch-spezial-typ-anfrage` | Netzentgelte Rechtsfragen / Redispatch Spezial / Typ Anfrage Mandanten Routing / Spezial Anfrage Mehrparteien Konflikt Interessen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächste... |
| `energierecht-anschluss` | Allgemein, Anschluss Skills Router, Chronologie Und Belegmatrix, Fristen Und Risikoampel: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `energierecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `energierecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `energierecht-emobility-wasserstoff` | Energierecht Emobility Wasserstoff, Energierecht Energievertraege, Energierecht Industriekunden, Energierecht Infrastrukturprojekte: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nä... |
| `energierecht-netz-speicher` | Energierecht Kommandocenter, Energierecht Netz Speicher Zugang, Energierecht Projektfinanzierung, Energierecht Transaktionen Dd: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächst... |
| `energierecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `energierecht-rechtsquellen-sonderfall-edge-case` | Rechtsquellen: Quellenprüfung; Sonderfall und Edge-Case-Prüfung: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `energierecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `energierecht-vertrieb-marktrollen-waerme` | Energierecht Vertrieb Marktrollen, Energierecht Waerme Quartier, Energierecht Wettbewerb, Er Bess Abfall Recycling Rueckbau: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten b... |
| `er-bess-abstandsflaechen-baurecht-brandenburg` | Er Bess Abstandsflaechen Und Layout, Er Bess Baurecht Brandenburg, Er Bess Behoerdenstrategie, Er Bess Bimschg Und 4 Bimschv: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten... |
| `er-bess-brandschutz-co-location-datenschutz` | Er Bess Brandschutz Lithium Ionen, Er Bess Co Location Pv Wind, Er Bess Datenschutz Video Leitwarte, Er Bess Dieselgenerator Notstrom: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den... |
| `er-bess-epc-fca-agnes-finanzierung` | Er Bess Epc O And M Vertraege, Er Bess Fca Agnes Bnetza, Er Bess Finanzierung Bankability, Er Bess Kapazitaetsmarkt Grundlast: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten... |
| `er-bess-kaltstart-projektaufnahme` | Batteriespeicherprojekt aufnehmen: Projektgröße, Standort, Netzebene, Betreiberrolle, Fristen, Unterlagen und Zieloutput. |
| `er-bess-kritis-marktrollen-bilanzkreis` | Er Bess Kritis Nis2 Cyber, Er Bess Marktrollen Bilanzkreis, Er Bess Naturschutz Artenschutz, Er Bess Netzanschluss Hoehe Spannung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den näch... |
| `er-bess-netzentgelte-board-physische` | Er Bess Netzentgelte Und Abgaben, Er Bess Output Board Paper, Er Bess Physische Sicherheit Terror, Er Bess Power Quality Emv: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten... |
| `er-bess-ppa-projektakte-rechtsmittel` | Er Bess Ppa Und Merchant Risk, Er Bess Projektakte Qualitygate, Er Bess Rechtsmittel Und Nachbarabwehr, Er Bess Regelenergie Systemdienstleistung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und... |
| `er-fusion-buergerbeteiligung-foerderung` | Er Fusion Buergerbeteiligung Und Politik, Er Fusion Foerderung Beihilfe, Er Fusion Netzanschluss Und Systemnutzen, Er Fusion Sicherheitsnachweis: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und l... |
| `er-fusion-kaltstart-regulierungsweg` | Ordnet Fusionsreaktor-Projekt zwischen Atomrecht, Strahlenschutz, Baurecht, Immissionsschutz und Forschungsförderung. |
| `kwkg-netzanschluss-netze-praesumtion-red` | Kwkg Verhandlung Vergleich Und Eskalation, Netzanschluss Formular Portal Und Einreichung, Netze Risikoampel Und Gegenargumente, Praesumtion Red Team Und Qualitaetskontrolle: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Bele... |
| `livecheck-fristennotiz-versorger` | Livecheck Fristennotiz Und Naechster Schritt, Versorger Fristen Form Und Zustaendigkeit, Ladeinfrastruktur Vertragskette, Ppa Cppa Vertragsspezialitaeten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundl... |
| `projektfinanzierung-stadtwerke-system` | Projektfinanzierung Compliance Dokumentation Und Akte, Routing Internationaler Bezug Und Schnittstellen, Stadtwerke Tatbestand Beweis Und Belege, System Beweislast Und Darlegungslast: wählt den konkreten Prüfpfad, trennt Frist, Zuständig... |
| `transaktionen-vertrieb-waerme` | Transaktionen Zahlen Schwellen Und Berechnung, Vertrieb Behörden Gericht Und Registerweg, Waerme Dokumentenmatrix Und Lueckenliste, Strompreisbremse Und Extras: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechts... |
| `verfahren-quellenkarte` | Verfahren Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

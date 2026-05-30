# Strafbefehl-Verteidiger


<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **LUMEN Studios GmbH — Insolvenz- und Wirtschaftsstrafverfahren** (`lumen-studios-insolvenz-strafverfahren`) | [Gesamt-PDF lesen](../testakten/lumen-studios-insolvenz-strafverfahren/gesamt-pdf/lumen-studios-insolvenz-strafverfahren_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Ein freistehender Strafbefehls-Assistent für Kanzleien: vom Fristnotruf über Akteneinsicht und Einspruch bis zur beschränkten Rechtsfolgenstrategie oder Hauptverhandlung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn Register, Kanzleisoftware, beA, E-Mail, Datenraum oder Aktenexport fehlen, arbeitet es mit manuellen Uploads oder mit einem klar gekennzeichneten Simulationsmodus.

### Arbeitsakte (separat)

Separate Arbeitsakte — **kein Teil des Plugins**, eigener Download:

| Akte | Direkt-Download |
| --- | --- |
| **LUMEN Studios (Insolvenz + Wirtschaftsstrafverfahren)** | [testakte-lumen-studios-insolvenz-strafverfahren.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Strafbefehl – Ladendiebstahl und Fahrerflucht** ([`testakten/strafbefehl-ladendiebstahl-fahrerflucht/`](../testakten/strafbefehl-ladendiebstahl-fahrerflucht/)).

Direkt-Download als ZIP: [testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `strafbefehl-kommandocenter` starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nicht raten lassen, sondern mit der passenden Vorlage nachfordern oder Simulation ausdrücklich aktivieren.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `strafbefehl-kommandocenter` - Strafbefehl-Kommandocenter
- `strafbefehl-aktenanlage` - Aktenanlage Strafbefehl
- `strafbefehl-fristen-einspruch` - Frist und Einspruch nach § 410 StPO
- `strafbefehl-akteneinsicht-147` - Akteneinsicht
- `strafbefehl-zulaessigkeit-407` - Zulässigkeit des Strafbefehls
- `strafbefehl-inhalt-409-pruefung` - Inhaltsprüfung nach § 409 StPO
- `strafbefehl-einspruch-beschraenkung` - Einspruch beschränken oder nicht
- `strafbefehl-wiedereinsetzung` - Wiedereinsetzung
- `strafbefehl-pflichtverteidiger` - Pflichtverteidigung
- `strafbefehl-tagessaetze-geldstrafe` - Tagessätze und Geldstrafe
- `strafbefehl-nebenfolgen-fahrerlaubnis` - Nebenfolgen
- `strafbefehl-beweis-und-einlassung` - Beweis und Einlassung
- `strafbefehl-zeugen-befragungsstrategie` - Zeugenbefragung
- `strafbefehl-hauptverhandlung-vorbereitung` - Hauptverhandlung vorbereiten
- `strafbefehl-abwesenheit-vertretung` - Abwesenheit und Vertretung
- `strafbefehl-einstellung-153-153a-170` - Einstellung und Verständigung
- `strafbefehl-deal-verstaendigung` - Gesprächsstrategie mit Gericht und Staatsanwaltschaft
- `strafbefehl-rechtsmittel-nach-urteil` - Rechtsmittel nach Urteil
- `strafbefehl-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `strafbefehl-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/strafbefehl-mandatskarte.md` - Strafbefehl-Mandatskarte
- `assets/templates/frist-einspruch-410.md` - Frist und Einspruch nach § 410 StPO
- `assets/templates/akteneinsicht-147.md` - Akteneinsicht nach § 147 StPO
- `assets/templates/strafbefehl-inhaltspruefung.md` - Inhaltsprüfung Strafbefehl
- `assets/templates/einspruch-unbeschraenkt.md` - Unbeschränkter Einspruch
- `assets/templates/einspruch-beschraenkt.md` - Beschränkter Einspruch
- `assets/templates/wiedereinsetzung.md` - Wiedereinsetzung
- `assets/templates/pflichtverteidiger-check.md` - Pflichtverteidiger-Check
- `assets/templates/tagessaetze.md` - Tagessatzprüfung
- `assets/templates/einlassungsstrategie.md` - Einlassungsstrategie
- `assets/templates/zeugen-fragenkatalog.md` - Zeugenfragen
- `assets/templates/hauptverhandlung-plan.md` - Hauptverhandlung
- `assets/templates/einstellung-153-153a.md` - Einstellung nach §§ 153, 153a StPO
- `assets/templates/nebenfolgen-fahrerlaubnis.md` - Nebenfolgen
- `assets/templates/rechtsmittel-nach-urteil.md` - Rechtsmittel nach Urteil
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

## Arbeitsakte

Zum Arbeiten liegt die Akte unter `testakten/strafbefehl-ladendiebstahl-fahrerflucht`. Sie wird im Release als `testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip` bereitgestellt und ist kein Bestandteil des Plugin-ZIPs.

## Download

- Plugin-ZIP: [strafbefehl-verteidiger.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafbefehl-verteidiger.zip)
- Akte: [testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 21 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Strafbefehl Verteidiger-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeits... |
| `strafbefehl-abwesenheit-vertretung` | Mandant kann oder will zur Hauptverhandlung nach Strafbefehl-Einspruch nicht erscheinen und Verteidiger soll ihn vertreten. Prüfraster Entbindung von Erscheinungspflicht § 411 Abs. 2 StPO Voraussetzungen und Antrag. Verwerfung des Einspr... |
| `strafbefehl-aktenanlage` | Neues Strafbefehl-Mandat anlegen und Mandatsakte strukturieren damit Fristen und Beweismittel sicher verwaltet werden. Prüfraster Aktenstruktur Vollmacht Fristenkalender Beweismittelverzeichnis. Normen § 410 StPO Einspruchsfrist § 147 St... |
| `strafbefehl-akteneinsicht-147` | Akteneinsicht im Strafbefehlsverfahren nach § 147 StPO. Antrag bei Staatsanwaltschaft oder Amtsgericht. Versagungsgründe § 147 Abs. 2 StPO. Akte im Strafbefehlsverfahren: Ermittlungsakte Messakte Bußgeldheft. Beschwerderecht § 147 Abs. 5... |
| `strafbefehl-beweis-und-einlassung` | Beweisprüfung und Einlassungsstrategie im Strafbefehlsverfahren. Schweigen nach § 136 StPO darf nicht nachteilig gewertet werden (BGH st. Rspr.). Gestaendnis vs. Bestreiten Strategie. Beweisanträge § 244 StPO. Einlassung schriftlich oder... |
| `strafbefehl-deal-verstaendigung` | Verständigung nach § 257c StPO im Strafbefehlsverfahren. Voraussetzungen Inhalt Bindungswirkung Belehrung nach § 257c Abs. 4 und 5 StPO. Grenzen: kein Freispruch kein Schuldspruchverzicht. Abgrenzung informelle Absprache. Ablaufprotokoll... |
| `strafbefehl-einspruch-beschraenkung` | Beschraenkter Einspruch nach § 410 Abs. 2 StPO auf Rechtsfolgen. Schuldspruch wird rechtskraeftig. Taktisches Kalkuel. Geldstrafe Tagessatz Fahrverbot Einziehung angreifbar. Vollstreckungsverzug § 456a StPO. Abgrenzung unbeschraenkter Ei... |
| `strafbefehl-einstellung-153-153a-170` | Einstellung im Strafbefehlsverfahren: § 153 StPO (Geringfuegigkeit ohne Auflage) § 153a StPO (mit Auflage) § 170 Abs. 2 StPO (Einstellung mangels hinreichenden Tatverdachts). Opportunitaetsprinzip. Zustimmungserfordernisse. BZR-Eintrag b... |
| `strafbefehl-fristen-einspruch` | Sichert die Einspruchsfrist nach § 410 StPO (2 Wochen ab Zustellung) und erstellt Einspruchsentwuerfe. Berechnung Zustellungsfiktion § 418 ZPO i.V.m. § 37 StPO. Unbeschraenkter oder beschraenkter Einspruch § 410 Abs. 2 StPO. Wiedereinset... |
| `strafbefehl-hauptverhandlung-vorbereitung` | Hauptverhandlung nach § 411 StPO bei Einspruch. Termin Vorbereitungspflichten. Beweisanträge § 244 StPO. Einlassung oder Schweigen. Strafzumessung § 46 StGB. Befangenheitsantrag § 24 StPO. Entbindung von Erscheinungspflicht § 411 Abs. 2... |
| `strafbefehl-inhalt-409-pruefung` | Prüft Strafbefehl auf Pflichtinhalt nach § 409 StPO (7 Mindestangaben) und identifiziert Nichtigkeitsgründe. Tatbeschreibung Bestimmtheitsgrundsatz Art. 103 Abs. 2 GG. Fehlerhafte Rechtsfolgen Geldstrafe Tagessatz Fahrverbot. Strafbefehl... |
| `strafbefehl-kommandocenter` | Einstieg in das Strafbefehl-Mandat — Ampel-Schnelldiagnose zeigt kritische Fristen und offene Handlungsfelder auf einen Blick. Zentrales Steuerungsmodul routet auf Subskills: Frist § 410 StPO Akteneinsicht § 147 StPO Inhaltsprüfung § 409... |
| `strafbefehl-nebenfolgen-fahrerlaubnis` | Fahrerlaubnisentzug § 69 StGB und Fahrverbot § 44 StGB im Strafbefehl. Regelentziehung § 69 Abs. 2 StGB bei §§ 315c 316 142 StGB. Sperrfrist § 69a StGB. Vorzeitige Aufhebung § 69a Abs. 7 StGB. Abgrenzung § 25 StVG (OWi-Fahrverbot). MPU-A... |
| `strafbefehl-pflichtverteidiger` | Pflichtverteidigerbestellung im Strafbefehlsverfahren nach § 140 StPO. Notwendige Verteidigung. Antrag auf Beiordnung § 141 StPO. Bestellung durch Gericht. Auswechslung des Pflichtverteidigers § 143a StPO. Gebühren Nr. 4100 ff. VV-RVG. |
| `strafbefehl-quality-gate` | Vor dem Einspruch-Versand vor der Hauptverhandlung oder nach dem Urteil eine Abschlussprüfung durchführen. Prüfraster Fristen Vollmacht Zulässigkeit Einlassung Beweisanträge Strafzumessung Protokoll. Normen § 410 StPO Einspruchsfrist § 4... |
| `strafbefehl-rechtsmittel-nach-urteil` | Rechtsmittel nach Urteil in der Hauptverhandlung nach Strafbefehl-Einspruch. Berufung § 312 StPO (Frist 1 Woche schriftlich). Revision § 333 StPO (Frist 1 Woche Rechtsfehler). Revisionsbegründung § 345 StPO 1 Monat. Absolute Revisionsgrü... |
| `strafbefehl-rechtsprechungsrecherche` | Rechtsprechung zum Strafbefehlsverfahren recherchieren für Schriftsaetze oder Argumentation in der Hauptverhandlung. Prüfraster BGH OLG-Rspr zu §§ 407-412 StPO Einspruch Wiedereinsetzung Strafzumessung. Normen §§ 407 408 410 412 StPO. Wo... |
| `strafbefehl-tagessaetze-geldstrafe` | Berechnung Tagessaetze und Geldstrafe nach §§ 40 41 StGB. Tagessatzanzahl nach Schuld. Tagessatzhoehe nach Nettoeinkommen Dreissigstel. Mindest-Tagessatz 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB. Einkommensnachweise. Ratenza... |
| `strafbefehl-wiedereinsetzung` | Wiedereinsetzung in den vorigen Stand nach § 44 StPO bei versaeumter Einspruchsfrist. Voraussetzungen: kein Verschulden. Antragsfrist 1 Woche. Glaubhaftmachung § 45 StPO. Zustellungsfiktion entgegnen. Eidesstattliche Versicherung. Wieder... |
| `strafbefehl-zeugen-befragungsstrategie` | Hauptverhandlung nach Strafbefehl-Einspruch — Zeugen erschuettern oder Entlastungszeugen foerdern. Prüfraster Glaubwürdigkeitsanalyse Aussage-Konstanz Vorhalt fruehere Aussage Fragerecht § 240 StPO. Normen § 68 StPO Zeugenpflichten § 52... |
| `strafbefehl-zulaessigkeit-407` | Zulässigkeit des Strafbefehls nach § 407 StPO. Nur Vergehen. Sanktionskatalog § 407 Abs. 2 StPO. Sachliche Zuständigkeit Amtsgericht. Keine U-Haft. Keine Beweisprobleme die Hauptverhandlung erfordern. Ablehnung durch Richter § 408 Abs. 3... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

# Mietrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`mietrecht`) | [`mietrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mietrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Mietstreit Tannenkamp / Strassburger Immobilien GmbH — Altbau Leipzig-Plagwitz, Modernisierung und Mietminderung** (`mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp`) | [Gesamt-PDF lesen](../testakten/mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp/gesamt-pdf/mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp_gesamt.pdf) | [`testakte-mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Mietrecht für Mieter und Vermieter sowie Wohnungseigentumsrecht mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitätsstädte. Workflows für Datenerhebung, Mieterhöhungs-Widerspruch, Mietsenkungsverlangen, Nebenkostenprüfung, Mieteranfragen, Kündigung, Kaution, WEG-Beschlussklage und Klageentwurf Amtsgericht.

## Rechtsstand und Quellen-Gate

Für aktuelle Mietrechts- und WEG-Fragen zuerst `/mietrecht:rechtsstand-mai-2026-faktenbank` laden. Der Skill enthält geprüfte freie Anker zu Mietpreisbremse, Modernisierung, Steckersolargeräten, virtueller Eigentümerversammlung, Verwalterabberufung, WEG-baulichen Veränderungen und Störerhaftung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatzzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier Quelle; Mietspiegel nur aus amtlicher kommunaler Quelle oder der mitgelieferten Mietspiegel-Referenz.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Mietrecht (`mietrecht`, dieses Plugin) | [mietrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mietrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Triage und Workflow-Routing im Plugin. Fragt Rolle (Vermieter/Mieter/WEG/Verwalter), Ziel, Fristen, Unterlagen und Risiken ab und schlägt passende Spezial-Skills vor. Bei stummem Upload reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, schlägt den passenden Spezial-Skill vor oder stellt genau eine gezielte Rückfrage. |
| `eigenbedarfskuendigung-erstellen` | Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehörige Haushaltsangehörige) konkrete Begründ… |
| `klageentwurf-amtsgericht` | Beide Rollen — entwirf eine Klageschrift zum Amtsgericht in einer Mietsache. Sachliche Zuständigkeit für Wohnraummietsachen nach § 23 Nr. 2a GVG ohne Rücksicht auf den Streitwert; bei Geschäftsraummiete allgemeine… |
| `lage-und-ausstattung-erheben` | Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnfläche Bad Küche Heizung Wohnungsausstattung Gebäudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als… |
| `mahnung-zahlungsverzug-mieter` | Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot frist… |
| `mandat-triage-mietrecht` | Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klärt Mandantenrolle (Vermieter/Mieter/WEG-Eigentümer/Verwalter), Gegenstand (Wohnraum/Gewerbe/WEG) und Sachgebiet (Kündigung, Mieterhöhung, Mietminderung, Modernisierung, Nebenkosten, Mietkaution, Eigenbedarf, Räumung, WEG-Beschluss, WEG-Hausgeld). Fristen-Sofort-Check (§ 573c BGB, § 721 ZPO, § 45 WEG, § 558b BGB). Eskalations-Pfad bei laufenden Fristen. |
| `mieteranfragen-beantworten` | Vermieter- und Hausverwaltungssicht — beantworte Mieteranfragen sachlich und ehrlich. Deckt typische Themen ab (Mietminderung Mangelanzeige Modernisierungsankündigung Schönheitsreparaturen Hausordnung Kaution Eigenb… |
| `mieterhoehung-pruefen-widersprechen` | Mietersicht — prüfe ein Mieterhöhungsverlangen nach ortsüblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begründung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. P… |
| `mieterhoehungsverlangen-erstellen` | Vermietersicht — verfasse ein Mieterhöhungsverlangen auf ortsübliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemäßer Begründung (Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen).… |
| `mietkaution-rueckforderung` | Mietersicht — Workflow zur Rückforderung der Mietkaution nach Beendigung des Mietverhältnisses. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Prüfung mit Gericht, Datum und Aktenzeichen. |
| `mietsenkungsverlangen` | Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Verstoß gegen die Mietpreisbremse (§§ 556d ff. BGB) gegen § 5 WiStG (Mietpreisüberhöhung) und gegen § 291 StGB (Wucher). Erzeugt ein… |
| `mietspiegel-quellen` | Verweist auf die mitgelieferte Referenz references/mietspiegel-quellen.md mit ausschließlich amtlichen Mietspiegel-Quellen (Bundesländer Top-Städte Universitätsstädte). Nutze diese Referenz immer wenn die ortsüb… |
| `nebenkostenabrechnung-erstellen` | Vermieter- und Hausverwaltungssicht — Workflow für rechtssichere Betriebskostenabrechnungen nach § 556 BGB und BetrKV. Deckt Abrechnungszeitraum Zugangsfrist (zwölf Monate) Umlagefähigkeit Verteilerschlüssel Heizk… |
| `nebenkostenabrechnung-pruefen` | Mietersicht — prüfe eine Betriebskostenabrechnung auf Form (§ 556 Abs. 3 BGB) Frist (Zugang innerhalb von zwölf Monaten nach Abrechnungszeitraum) Umlagefähigkeit nach BetrKV Verteilerschlüssel rechnerische Richtig… |
| `rechtsstand-mai-2026-faktenbank` | Quellen-Gate: Mietpreisbremse, Modernisierung, Steckersolargeräte, virtuelle Eigentümerversammlung, Verwalterabberufung, WEG-bauliche Veränderung und freie BGH-/Normquellen |
| `weg-beschluss-anfechten` | WEG-Sicht — Prüfraster für die Beschlussanfechtung in der Wohnungseigentümergemeinschaft nach §§ 44 ff. WEG (Reform 2020). Beschluss-, Anfechtungs-, Nichtigkeits- und Feststellungsklage. Prüft formelle Mängel (Ladung, Tagesordnung, Beschlussfähigkeit, Mehrheit, Stimmrechtsausschluss) und materielle Mängel (ordnungsmäßige Verwaltung, Treu und Glauben). Klagefrist ein Monat ab Beschluss (§ 45 WEG). |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Mietrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Doku... |
| `eigenbedarfskuendigung-erstellen` | Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehoerige Haushaltsangehoerige) konkrete Begründung im Kündigungsschrei... |
| `klageentwurf-amtsgericht` | Beide Rollen — entwirf eine Klageschrift zum Amtsgericht in einer Mietsache. Sachliche Zuständigkeit für Wohnraummietsachen nach § 23 Nr. 2a GVG ohne Rücksicht auf den Streitwert; bei Geschäftsraummiete allgemeine AG-Grenze nach § 23 Nr.... |
| `lage-und-ausstattung-erheben` | Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnflaeche Bad Kueche Heizung Wohnungsausstattung Gebaeudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als Sondermerkmale bewer... |
| `mahnung-zahlungsverzug-mieter` | Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot fristlose Kündigung nach § 5... |
| `mandat-triage-mietrecht` | Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klaert Mandantenrolle (Vermieter Mieter WEG-Eigentuemer Verwalter) Gegenstandsart (Wohnraum Gewerbe WEG) Sachgebiet (Kündigung Mieterhoehung Mietminderung Modernisierung Nebenkos... |
| `miet-gewerbemiete-vertragsklauseln-spezial` | Spezialfall Gewerbemiete: Wertsicherungsklauseln, Konkurrenzschutz, Schriftform § 550 BGB, Doppelschriftformklausel. Pruefraster fuer Vermieter und Mieter. |
| `miet-kuendigungsschutz-checkliste` | Checkliste Kuendigungsschutz Wohnraum §§ 573 ff. BGB: Eigenbedarf, Vertragsverletzung, Zahlungsverzug, Sozialklausel § 574 BGB. Pruefraster fuer Mieter und Vermieter. |
| `miet-mietminderung-mangel-spezial` | Spezialfall Mietminderung bei Mangel § 536 BGB: Erheblichkeit, Mangelanzeige, Hoehe der Minderung, Beweislast. Pruefraster fuer Mietminderungsbescheid und Klage. |
| `miet-mietvertrag-bauleiter` | Bauleiter Wohnraum-Mietvertrag: Schoenheitsreparaturen, Kaution, Kuendigung, Mieterhoehung, Untervermietung. Pruefraster fuer Vermieter und Mieter. |
| `mieteranfragen-beantworten` | Vermieter- und Hausverwaltungssicht — beantworte Mieteranfragen sachlich und ehrlich. Deckt typische Themen ab (Mietminderung Mangelanzeige Modernisierungsankündigung Schoenheitsreparaturen Hausordnung Kaution Eigenbedarfskündigung Beleg... |
| `mieterhoehung-pruefen-widersprechen` | Mietersicht — prüfe ein Mieterhoehungsverlangen nach ortsueblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begründung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. Prüfroutine deckt Textf... |
| `mieterhoehungsverlangen-erstellen` | Vermietersicht — verfasse ein Mieterhoehungsverlangen auf ortsuebliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemäßer Begründung (Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen). Prüfroutine deckt Textf... |
| `mietkaution-rueckforderung` | Workflow-Skill zu mietkaution rueckforderung. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `mietsenkungsverlangen` | Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Verstoss gegen die Mietpreisbremse (§§ 556d ff. BGB) gegen § 5 WiStG (Mietpreisueberhoehung) und gegen § 291 StGB (Wucher). Erzeugt eine qualifizierte Ruege... |
| `mietspiegel-quellen` | Operationalisiert die Prüfung der ortsueblichen Vergleichsmiete und der Mietpreisbremse anhand der mitgelieferten Referenz references/mietspiegel-quellen.md. Nutze diesen Skill, wenn für eine konkrete Adresse die ortsuebliche Vergleichsm... |
| `mr-betriebskostenabrechnung-fehler-spezial` | Spezialfall fehlerhafte Betriebskostenabrechnung: formell und materiell pruefen, Belegrecht § 259 BGB, Einsichtnahme, Saumnis 12-Monatsfrist § 556 Abs. 3 BGB. Klage des Mieters auf Rueckzahlung. Pruefraster und Mustertexte. |
| `mr-einfuehrung-vertragstypen` | Mietrecht einfuehrend: Wohnraum-, Gewerberaum-, Pacht-, Unter-, Index- und Staffelmiete. Schutzvorschriften pro Typ, Kuendigungsregime, typische Klauselrisiken. Entscheidungstabelle. |
| `mr-kuendigungsschutz-praxis` | Wohnraum-Kuendigungsschutz Praxis: ordentliche Kuendigung § 573 BGB nur bei berechtigtem Interesse, Eigenbedarf § 573 Abs. 2 Nr. 2 BGB, Kuendigung bei Pflichtverletzung, Zahlungsverzug. Sozialklausel § 574 BGB. Pruefraster. |
| `mr-modernisierung-und-rolling-rent-spezial` | Spezialfall Modernisierungs-Umlage in der laufenden Mieterhoehung: Verhaeltnis § 559 BGB zur ortsueblichen Vergleichsmiete § 558 BGB, Kappungsgrenze, Haerteeinwand. Aktuelle Rechtsprechung BGH. Pruefraster. |
| `nebenkostenabrechnung-erstellen` | Vermieter- und Hausverwaltungssicht — Workflow für rechtssichere Betriebskostenabrechnungen nach § 556 BGB und BetrKV. Deckt Abrechnungszeitraum Zugangsfrist (zwoelf Monate) Umlagefähigkeit Verteilerschluessel HeizkostenV Vorauszahlungen... |
| `nebenkostenabrechnung-pruefen` | Mietersicht — prüfe eine Betriebskostenabrechnung auf Form (§ 556 Abs. 3 BGB) Frist (Zugang innerhalb von zwoelf Monaten nach Abrechnungszeitraum) Umlagefähigkeit nach BetrKV Verteilerschluessel rechnerische Richtigkeit Belegrecht (§ 259... |
| `rechtsstand-mai-2026-faktenbank` | Faktenbank und Quellen-Gate für aktuelle mietrechtliche und WEG-rechtliche Aussagen mit Stand 29.05.2026. Nutze diesen Skill vor Ausgaben zu Mietpreisbremse, Mieterhöhung, Betriebskosten, Kündigung, Kaution, Steckersolargeräten, virtuell... |
| `spezial-amtlichen-risikoampel-und-gegenargumente` | Amtlichen: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-amtsgericht-sonderfall-und-edge-case` | Amtsgericht: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ausschliesslich-dokumentenmatrix-und-lueckenliste` | Ausschliesslich: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bundesland-verhandlung-vergleich-und-eskalation` | Bundesland: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-datenerhebung-zahlen-schwellen-und-berechnung` | Datenerhebung: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-erstellung-red-team-und-qualitaetskontrolle` | Erstellung: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-grossstadt-mietspiegel-und-kappung` | Großstadt-Mietspiegel, Kappungsgrenze und Vergleichsmiete: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-klageentwurf-beweislast-und-darlegungslast` | Klageentwurf: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mieter-tatbestand-beweis-und-belege` | Mieter: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mieteranfragen-mandantenentscheidung` | Mieteranfragen: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mieterhoehungs-compliance-dokumentation-und-akte` | Mieterhoehungs: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mietrecht-erstpruefung-und-mandatsziel` | Mietrecht: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mietsenkungsverlangen-international-schnittstellen` | Mietsenkungsverlangen: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mietspiegel-behoerden-gericht-und-registerweg` | Mietspiegel: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-nebenkostenpruefung-formular-portal-und-einreichung` | Nebenkostenpruefung: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-prozessstrategie-mieterhoehung` | Prozessstrategie bei Mieterhöhung, Belegen und Sachverständigenrisiko: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-quellen-schriftsatz-brief-und-memo-bausteine` | Quellen: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-universitaetsstaedte-livequellen-check` | Universitaetsstaedte: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vermieter-fristen-form-und-zustaendigkeit` | Vermieter: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-widerspruch-mehrparteien-konflikt-und-interessen` | Widerspruch: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `weg-beschluss-anfechten` | Prüfraster für die Beschlussanfechtung in der Wohnungseigentuemergemeinschaft nach §§ 44 ff. WEG-Reform 2020. Beschlussklage Anfechtungsklage Nichtigkeitsklage Feststellungsklage. Prüfung formelle Maengel (Ladung Tagesordnung Beschlussfä... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin mietrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin mietrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin mietrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin mietrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin mietrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin mietrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin mietrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin mietrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin mietrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin mietrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

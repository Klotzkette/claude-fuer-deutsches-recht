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
| `mietpreisueberhoehung-wistrg-1954-mietwucher` | Dreistufige Prüfung überhöhter Wohnraummiete: Mietpreisbremse, § 5 WiStrG 1954 als Ordnungswidrigkeit und § 291 StGB als Straftat; mit Mietspiegel-, Beweis-, Rückforderungs- und Behördenpfad. |
| `mietsenkungsverlangen` | Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Mietpreisbremse (§§ 556d ff. BGB), § 5 WiStrG 1954 (Mietpreisüberhöhung) und § 291 StGB (Mietwucher). Erzeugt ein… |
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

Automatisch generierte Komplett-Liste aller 56 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtlichen-amtsgericht-sonderfall` | Amtlichen: Risikoampel, Gegenargumente und Verteidigungslinien im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und dir... |
| `amtsgericht-sonderfall-und-edge-case` | Amtsgericht: Sonderfall und Edge-Case-Prüfung im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arb... |
| `anschluss-routing` | Anschluss-Routing für Mietrecht (Wohnraum/Gewerbe): wählt den nächsten Spezial-Skill nach Engpass (§ 573c BGB Kündigung 3 Mon., Mietvertrag, Nebenkostenabrechnung, Mängelanzeige), dokumentiert Router-Entscheidung mit Begründung. |
| `ausschliesslich-dokumentenmatrix-und-lueckenliste` | Ausschliesslich: Dokumentenmatrix, Lückenliste und Nachforderung im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `betriebskostenabrechnung-belege-und-formelpruefer` | Prüft und erstellt Betriebskostenabrechnungen mit BGH-Linie zu formeller Ordnungsgemäßheit, Belegeinsicht, Umlageschlüsseln, Vorwegabzug, HeizkostenV und Einwendungsfristen im Mietrecht. |
| `bundesland-datenerhebung-grossstadt` | Bundesland: Verhandlung, Vergleich und Eskalation im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem... |
| `datenerhebung-zahlen-schwellen-und-berechnung` | Datenerhebung: Zahlen, Schwellenwerte und Berechnung im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzba... |
| `dokumente-intake` | Dokumentenintake für Mietrecht (Wohnraum/Gewerbe): sortiert Mietvertrag, Nebenkostenabrechnung, Mängelanzeige, prüft Datum, Absender, Frist und Beweiswert (Mängelfotos, Mietspiegel); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a... |
| `eigenbedarfskuendigung-erstellen` | Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehoerige Haushaltsangehoerige) konkrete Begründung im Kündigungsschrei... |
| `einstieg-routing` | Einstieg, Triage und Routing für Mietrecht (Wohnraum/Gewerbe): ordnet Rolle (Mieter, Vermieter, Hausverwaltung), markiert Frist (§ 573c BGB Kündigung 3 Mon.), wählt Norm (BGB §§ 535/536/543/558/573 ff., WEG, BetrKV) und Zuständigkeit (Am... |
| `erstellung-fehlerkatalog` | Erstellung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `grossstadt-mietspiegel-und-kappung` | Großstadt-Mietspiegel, Kappungsgrenze und Vergleichsmiete: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Mietrecht. |
| `klageentwurf-amtsgericht-miet-gewerbemiete` | Beide Rollen — entwirf eine Klageschrift zum Amtsgericht in einer Mietsache. Sachliche Zuständigkeit für Wohnraummietsachen nach § 23 Nr. 2a GVG ohne Rücksicht auf den Streitwert; bei Geschäftsraummiete allgemeine AG-Grenze nach § 23 Nr.... |
| `klageentwurf-beweislast-und-darlegungslast` | Klageentwurf: Beweislast, Darlegungslast und Substantiierung im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direk... |
| `lage-ausstattung-mahnung-zahlungsverzug` | Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnflaeche Bad Kueche Heizung Wohnungsausstattung Gebaeudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als Sondermerkmale bewer... |
| `mahnung-zahlungsverzug-mieter` | Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot fristlose Kündigung nach § 5... |
| `mandantenkommunikation-redteam-qualitygate-vermieter` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Mietrecht. |
| `mandat-triage-mietrecht` | Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klaert Mandantenrolle (Vermieter Mieter WEG-Eigentuemer Verwalter) Gegenstandsart (Wohnraum Gewerbe WEG) Sachgebiet (Kündigung Mieterhoehung Mietminderung Modernisierung Nebenkos... |
| `miet-gewerbemiete-vertragsklauseln-spezial` | Spezialfall Gewerbemiete: Wertsicherungsklauseln, Konkurrenzschutz, Schriftform § 550 BGB, Doppelschriftformklausel. Pruefraster für Vermieter und Mieter im Mietrecht. |
| `miet-kuendigungsschutz-mietminderung` | Checkliste Kuendigungsschutz Wohnraum §§ 573 ff. BGB: Eigenbedarf, Vertragsverletzung, Zahlungsverzug, Sozialklausel § 574 BGB. Pruefraster für Mieter und Vermieter im Mietrecht. |
| `miet-mietminderung-mangel-spezial` | Spezialfall Mietminderung bei Mangel § 536 BGB: Erheblichkeit, Mangelanzeige, Hoehe der Minderung, Beweislast. Pruefraster für Mietminderungsbescheid und Klage im Mietrecht. |
| `miet-mietvertrag-bauleiter` | Bauleiter Wohnraum-Mietvertrag: Schoenheitsreparaturen, Kaution, Kuendigung, Mieterhoehung, Untervermietung. Pruefraster für Vermieter und Mieter im Mietrecht. |
| `mieter-mieteranfragen-mandantenentscheidung` | Mieter: Tatbestandsmerkmale, Beweisfragen und Beleglage im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nut... |
| `mieteranfragen-beantworten` | Vermieter- und Hausverwaltungssicht — beantworte Mieteranfragen sachlich und ehrlich. Deckt typische Themen ab (Mietminderung Mangelanzeige Modernisierungsankündigung Schoenheitsreparaturen Hausordnung Kaution Eigenbedarfskündigung Beleg... |
| `mieteranfragen-mandantenentscheidung` | Mieteranfragen: Mandantenkommunikation und Entscheidungsvorlage im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und di... |
| `mieterhoehung-widersprechen` | Mietersicht — prüfe ein Mieterhoehungsverlangen nach ortsueblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begründung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. Prüfroutine deckt Textf... |
| `mieterhoehungs-compliance-dokumentation-und-akte` | Mieterhoehungs: Compliance-Dokumentation und Aktenvermerk im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt n... |
| `mieterhoehungsverlangen-erstellen` | Vermietersicht — verfasse ein Mieterhoehungsverlangen auf ortsuebliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemäßer Begründung (Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen). Prüfroutine deckt Textf... |
| `mietkaution-rueckforderung` | Mietkaution Rueckforderung: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Mietrecht. |
| `mietpreisueberhoehung-wistrg` | Prueft ueberhoehte Wohnraummiete dreistufig: Mietpreisbremse §§ 556d ff. BGB, Mietpreisueberhoehung § 5 WiStrG 1954 als Ordnungswidrigkeit und Mietwucher § 291 StGB als Straftat; mit Mietspiegel-, Beweis-, Rueckforderungs- und Behördenpf... |
| `mietsenkungsverlangen` | Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Verstoß gegen die Mietpreisbremse (§§ 556d ff. BGB), § 5 WiStrG 1954 (Mietpreisüberhöhung als Ordnungswidrigkeit) und § 291 StGB (Mietwucher als Straftat).... |
| `mietsenkungsverlangen-international` | Mietrecht: Erstprüfung, Rollenklärung und Mandatsziel im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzb... |
| `mietsenkungsverlangen-international-schnittstellen` | Mietsenkungsverlangen: Internationaler Bezug und Schnittstellen im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und di... |
| `mietspiegel-behoerden-gericht-und-registerweg` | Mietspiegel: Behörden-, Gerichts- oder Registerweg im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbare... |
| `mietspiegel-quellen` | Operationalisiert die Prüfung der ortsueblichen Vergleichsmiete und der Mietpreisbremse anhand der mitgelieferten Referenz references/mietspiegel-quellen.md. Anwendungsfall: für eine konkrete Adresse die ortsuebliche Vergleichsmiete, die... |
| `mr-betriebskostenabrechnung-mr` | Fehlerhafte Betriebskostenabrechnung als Streitfall: formelle Mindestangaben, materielle Umlagefähigkeit, Belegeinsicht nach § 259 BGB, Zahlungsbelege, 12-Monats-Fristen nach § 556 Abs. 3 BGB, Zurückbehaltung, Rückzahlungsklage und Muste... |
| `mr-einfuehrung-klageentwurf-beweislast` | Mietrecht einfuehrend: Wohnraum-, Gewerberaum-, Pacht-, Unter-, Index- und Staffelmiete. Schutzvorschriften pro Typ, Kuendigungsregime, typische Klauselrisiken. Entscheidungstabelle im Mietrecht. |
| `mr-kuendigungsschutz-praxis` | Wohnraum-Kuendigungsschutz Praxis: ordentliche Kuendigung § 573 BGB nur bei berechtigtem Interesse, Eigenbedarf § 573 Abs. 2 Nr. 2 BGB, Kuendigung bei Pflichtverletzung, Zahlungsverzug. Sozialklausel § 574 BGB. Pruefraster im Mietrecht. |
| `mr-modernisierung-und-rolling-rent-spezial` | Spezialfall Modernisierungs-Umlage in der laufenden Mieterhoehung: Verhaeltnis § 559 BGB zur ortsueblichen Vergleichsmiete § 558 BGB, Kappungsgrenze, Haerteeinwand. Aktuelle Rechtsprechung BGH. Pruefraster im Mietrecht. |
| `nebenkostenabrechnung-erstellen-faktenbank` | Betriebskostenabrechnung erstellen aus Vermieter- und Hausverwaltungssicht: Umlagevereinbarung, BetrKV-Kostenarten, HeizkostenV, CO2KostAufG, Abrechnungsfrist, Vorauszahlungen, Belegpaket, Zugangsnachweis und Versand-Qualitygate im Mietr... |
| `nebenkostenabrechnung-pruefen` | Betriebskostenabrechnung prüfen aus Mietersicht: formelle Mindestangaben, Frist, Umlagefähigkeit, Belegeinsicht, Zahlungsbelege, HeizkostenV, CO2KostAufG, Rechenkontrolle, Einwendungen und temporäres Zurückbehaltungsrecht im Mietrecht. |
| `nebenkostenpruefung-prozessstrategie` | Nebenkostenprüfung als Einreichungs- und Verfahrensworkflow: Belegeinsicht verlangen, Einwendungen fristwahrend formulieren, Rückzahlungsanspruch beziffern, Mahnung/Mahnverfahren/Klage behandeln und Unterlagen für Amtsgericht oder Mieter... |
| `output-waehlen` | Output-Wahl für Mietrecht (Wohnraum/Gewerbe): stimmt Adressat (Mieter, Vermieter, Hausverwaltung), Frist (§ 573c BGB Kündigung 3 Mon.) und Form auf den Zweck ab — typische Outputs: Kündigungsschreiben, Mietminderungserklärung, Klage AG. |
| `prozessstrategie-mieterhoehung` | Prozessstrategie bei Mieterhöhung, Belegen und Sachverständigenrisiko: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Mietrecht. |
| `quellen-livecheck` | Quellen-Live-Check für Mietrecht (Wohnraum/Gewerbe): prüft Normen (BGB §§ 535/536/543/558/573 ff., WEG, BetrKV) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Amtsgericht Belegenheit und Quellenhygiene nach refer... |
| `quellen-schriftsatz-brief-und-memo-bausteine` | Quellen: Schriftsatz-, Brief- und Memo-Bausteine im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem... |
| `rechtsstand-mai-2026-faktenbank` | Faktenbank und Quellen-Gate für aktuelle mietrechtliche und WEG-rechtliche Aussagen mit Stand 29.05.2026. Dieses Fachmodul dient als Quellen-Gate vor Ausgaben zu Mietpreisbremse, Mieterhöhung, Betriebskosten, Kündigung, Kaution, Steckers... |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Mietrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Uplo... |
| `universitaetsstaedte-quellenkarte-check` | Universitaetsstaedte Quellenkarte Check: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Mietrecht (Wohnraum/Gewerbe): trennt fehlende Tatsachen von fehlenden Belegen (Mietvertrag, Nebenkostenabrechnung, Mängelanzeige), nennt pro Lücke Beweisthema, Beschaffungsweg (Amtsgericht Belegenheit),... |
| `vermieter-fristen-form-und-zustaendigkeit` | Vermieter: Fristen, Form, Zuständigkeit und Rechtsweg im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzb... |
| `weg-beschluss-anfechten` | Prüfraster für die Beschlussanfechtung in der Wohnungseigentuemergemeinschaft nach §§ 44 ff. WEG-Reform 2020. Beschlussklage Anfechtungsklage Nichtigkeitsklage Feststellungsklage. Prüfung formelle Maengel (Ladung Tagesordnung Beschlussfä... |
| `widerspruch-interessen` | Widerspruch: Mehrparteienkonflikt und Interessenmatrix im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutz... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Mietrecht. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Mietrecht. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Mietrecht. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

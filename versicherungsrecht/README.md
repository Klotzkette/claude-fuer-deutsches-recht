# Versicherungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`versicherungsrecht`) | [`versicherungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versicherungsrecht.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Brandstiftung Lagerhalle Magdeburg-Rothensee** (`strafrecht-brandstiftung-lagerhalle-magdeburg`) | [Gesamt-PDF lesen](../testakten/strafrecht-brandstiftung-lagerhalle-magdeburg/gesamt-pdf/strafrecht-brandstiftung-lagerhalle-magdeburg_gesamt.pdf) | [`testakte-strafrecht-brandstiftung-lagerhalle-magdeburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-brandstiftung-lagerhalle-magdeburg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Großes Versicherungsrecht-Plugin für VVG, VAG, europäische Versicherungsaufsicht, Lebensversicherung, BU, PKV, Rechtsschutz, Kreditversicherung, D&O, Cyber, Sach- und Haftpflichtdeckung.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`versicherungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versicherungsrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/versicherungsrecht/versicherungsrecht-werkstatt.md" download><code>versicherungsrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/versicherungsrecht/versicherungsrecht-schnellstart.md" download><code>versicherungsrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Deckungsanspruch prüfen und gegen die Ablehnung des Versicherers durchsetzen.
Großes, praxisnahes Versicherungsrecht-Plugin für Deckung, Ablehnung, Vertragsgestaltung, Aufsicht und Prozess. Es ist bewusst nicht nur ein Fachanwalts-Lernplugin, sondern ein Arbeitswerkzeug für Kanzlei, Rechtsabteilung, Versicherungsnehmer, Vermittler und Versicherer.

## Was dieses Plugin gut kann

- Deckungsablehnungen und Leistungsprüfung nach VVG zerlegen.
- Lebensversicherung, BU, PKV, Unfall, Rechtsschutz, Kreditversicherung, D&O, Cyber und Sachversicherung mit eigenen Spezial-Skills prüfen.
- BaFin, Ombudsmann, Klage und Vergleich taktisch voneinander trennen.
- Europäische Aufsicht, IDD, Solvency II, DORA und grenzüberschreitenden Vertrieb einordnen.

## Startlogik

Beginne mit dem allgemeinen Skill. Er fragt Rolle, Ziel, Fristen, Unterlagen, Eskalationsniveau und gewünschten Output ab. Danach schlägt er nur die Spezial-Skills vor, die zum Fall passen.

## Quellenhygiene

Normtexte werden aus amtlichen Quellen geprüft. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle verwendet. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `vers-dokumentenintake-police-avb-nachtraege`, `vers-kaltstart-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `bu-abstrakte-konkrete-verweisung`, `bu-berufsbild-bu-nachpruefung-datenschutz`, `datenschutz-schweigepflicht-gesundheitsdaten`, `idd-vertrieb-beratung-dokumentation`, `versicherungsmakler-haftung-deckungsluecke` |
| 3. Prüfung, Anspruch und Subsumtion | `bu-nachpruefung-anerkenntnis-leistungseinstellung`, `d-o-claims-made-innenhaftung-43-gmbhg`, `direktanspruch-pflichtversicherung-eiopa`, `kreditversicherung-obliegenheiten-limit-pruefung`, `lebensversicherung-ueberschussbeteiligung-bewertungsreserven` |
| 4. Gestaltung, Strategie und Verhandlung | `dora-cyber-abfindung-entschaedigungsquittung`, `rechtsschutz-vorvertraglichkeit-schadenereignis`, `vergleich-abfindung-entschaedigungsquittung` |
| 5. Verfahren, Behörde und Gericht | `rechtsabteilung-rechtsschutzversicherung-im-massenverfahren`, `sachverstaendigenverfahren-versicherung`, `vers-fristen-verjaehrung-klagefrist-fallkalender` |
| 8. Spezialmodule und Schnittstellen | `betriebshaftpflicht-versicherungsfall-serienschaden`, `betriebsunterbrechung-sachschaden-trigger`, `cyberversicherung-ransomware-d-o`, `deckungsprozess-vvg-rechtsabteilung`, `eiopa-grenzueberschreitender-vertrieb`, `elementarschaden-starkregen-ueberschwemmung`, `gewerbe-betriebsschliessung-infektionsschutz`, `hausrat-einbruchdiebstahl-idd-vertrieb`, `internationales-versicherungsprogramm-master-local-policy`, `kfz-haftpflicht-kasko-grobe-krankentagegeld`, `kfz-kasko-grobe-fahrlaessigkeit-entwendung`, `krankentagegeld-berufsunfaehigkeit-abgrenzung`, `kreditausfallversicherung-warenkredit`, `lebensversicherung-bezugsrecht-widerruf-aenderung`, `lebensversicherung-rueckkaufswert`, `nachhaltigkeit-taxonomie-sfdr-versicherungsprodukt`, `pkv-kostenerstattung-private`, `private-krankenversicherung-beitragsanpassung-treuhaender`, ... plus 28 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 64 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `betriebshaftpflicht-versicherungsfall-serienschaden` | Wenn es um Betriebshaftpflicht: Versicherungsfall und Serienschaden in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risik... |
| `betriebsunterbrechung-sachschaden-trigger` | Wenn es um Betriebsunterbrechung: Sachschaden-Trigger in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächste... |
| `bu-abstrakte-konkrete-verweisung` | Wenn es um BU: abstrakte und konkrete Verweisung in Versicherungsrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `bu-berufsbild-bu-nachpruefung-datenschutz` | Wenn es um BU: Berufsbild und 50-Prozent-Prüfung in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `bu-nachpruefung-anerkenntnis-leistungseinstellung` | Wenn es um BU: Anerkenntnis, Nachprüfung, Leistungseinstellung in Versicherungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `cyberversicherung-ransomware-d-o` | Wenn es um Cyberversicherung: Ransomware, DORA, Sanktionen in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nä... |
| `d-o-claims-made-innenhaftung-43-gmbhg` | Wenn es um D&O: Claims-made, Innenhaftung und Organstreit in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näc... |
| `datenschutz-schweigepflicht-gesundheitsdaten` | Wenn es um Gesundheitsdaten, Schweigepflicht und Versicherer in Versicherungsrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `deckungsprozess-vvg-rechtsabteilung` | Wenn es um Deckungsprozess und Gerichtsstand Paragraf 215 VVG in Versicherungsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `direktanspruch-pflichtversicherung-eiopa` | Wenn es um Direktanspruch in Pflichtversicherung Paragraf 115 VVG in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `dora-cyber-abfindung-entschaedigungsquittung` | Wenn es um DORA für Versicherer und Vermittler in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `eiopa-grenzueberschreitender-vertrieb` | Wenn es um EIOPA und grenzüberschreitender Versicherungsvertrieb in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken... |
| `elementarschaden-starkregen-ueberschwemmung` | Wenn es um Elementarschaden: Starkregen und Überschwemmung in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nä... |
| `gewerbe-betriebsschliessung-infektionsschutz` | Wenn es um Betriebsschließungsversicherung und Infektionsschutz in Versicherungsrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `hausrat-einbruchdiebstahl-idd-vertrieb` | Wenn es um Hausrat: Einbruchdiebstahl und Entschädigungsgrenzen in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken u... |
| `idd-vertrieb-beratung-dokumentation` | Wenn es um IDD/VVG-Vertrieb: Beratung und Dokumentation in Versicherungsrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `internationales-versicherungsprogramm-master-local-policy` | Wenn es um Internationale Versicherungsprogramme: Master und Local Policy in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigk... |
| `kfz-haftpflicht-kasko-grobe-krankentagegeld` | Wenn es um Kfz-Haftpflicht: Regress bei Alkohol, Flucht, Obliegenheit in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Ris... |
| `kfz-kasko-grobe-fahrlaessigkeit-entwendung` | Wenn es um Kfz-Kasko: Entwendung, Unfall, grobe Fahrlässigkeit in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| `krankentagegeld-berufsunfaehigkeit-abgrenzung` | Wenn es um Krankentagegeld vs. Berufsunfähigkeit in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sch... |
| `kreditausfallversicherung-warenkredit` | Wenn es um Kreditausfallversicherung und Warenkreditversicherung in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `kreditversicherung-obliegenheiten-limit-pruefung` | Wenn es um Kreditversicherung: Limitprüfung und Obliegenheiten in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `lebensversicherung-bezugsrecht-widerruf-aenderung` | Wenn es um Lebensversicherung: Bezugsrecht, Widerruf, Änderung in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| `lebensversicherung-rueckkaufswert` | Wenn es um Lebensversicherung: Rückkaufswert, Abschlusskosten, Widerspruch in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten... |
| `lebensversicherung-ueberschussbeteiligung-bewertungsreserven` | Wenn es um Überschussbeteiligung und Bewertungsreserven in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| `nachhaltigkeit-taxonomie-sfdr-versicherungsprodukt` | Wenn es um Nachhaltigkeit bei Versicherungsprodukten in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| `pkv-kostenerstattung-private` | Wenn es um PKV: Kostenerstattung und medizinische Notwendigkeit in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken u... |
| `private-krankenversicherung-beitragsanpassung-treuhaender` | Wenn es um PKV: Beitragsanpassung und Treuhänder in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `produkthaftpflicht-rueckrufkosten` | Wenn es um Produkthaftpflicht und Rückrufkosten in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `rechtsabteilung-betriebsunterbrechung` | Wenn es um Rechtsabteilung: Betriebsunterbrechung und Lieferkettenausfall in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `rechtsabteilung-cyberversicherung-nach-ransomware` | Wenn es um Rechtsabteilung: Cyberversicherung nach Ransomware in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und... |
| `rechtsabteilung-d-umwelthaftpflicht` | Wenn es um Rechtsabteilung: D&O-Deckung bei Organhaftung in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| `rechtsabteilung-idd-vertrieb-und-provisionskonflikt` | Wenn es um Rechtsabteilung: IDD-Vertrieb und Provisionskonflikt in Versicherungsrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `rechtsabteilung-rechtsschutzversicherung-im-massenverfahren` | Wenn es um Rechtsabteilung: Rechtsschutzversicherung im Massenverfahren in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| `rechtsschutz-deckungszusage-erfolgsaussicht` | Wenn es um Rechtsschutz: Deckungszusage und Stichentscheid in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nä... |
| `rechtsschutz-erfolgsaussicht-mutwilligkeit` | Wenn es um Rechtsschutz: Erfolgsaussicht und Mutwilligkeit in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nä... |
| `rechtsschutz-vorvertraglichkeit-schadenereignis` | Wenn es um Rechtsschutz: Vorvertraglichkeit und Schadenereignis in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken u... |
| `reiseversicherung-ruecktritt-abbruch-krankheit` | Wenn es um Reiseversicherung: Rücktritt, Abbruch, Krankheit in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und n... |
| `restschuldversicherung-widerruf` | Wenn es um Restschuldversicherung und Verbraucherdarlehen in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näc... |
| `rueckversicherung-cut-through-und-fronting` | Wenn es um Rückversicherung, Cut-through und Fronting in Versicherungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sachverstaendigenverfahren-versicherung` | Wenn es um Sachverständigenverfahren in der Versicherung in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `solvency-ii-scr-orsa-aufsichtsrecht` | Wenn es um Solvency II, SCR und ORSA für Versicherer in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| `subrogation-regress-transportversicherung` | Wenn es um Regress und Legalzession Paragraf 86 VVG in Versicherungsrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| `transportversicherung-ware-lagerung` | Wenn es um Transportversicherung: Ware, Lagerung, Lieferkette in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und... |
| `umwelthaftpflicht-umweltschadenversicherung` | Wenn es um Umwelthaftpflicht und Umweltschadenversicherung in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `unfallversicherung-invaliditaet-vers` | Wenn es um Private Unfallversicherung: Invalidität, Fristen, Gliedertaxe in Versicherungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vag-bafin-aufsicht-beschwerde-missstand` | Wenn es um VAG/BaFin-Aufsicht: Beschwerde und Missstand in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| `vergleich-abfindung-entschaedigungsquittung` | Wenn es um Vergleich, Abfindung und Entschädigungsquittung in Versicherungsrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `vers-deckungsablehnung-redteam` | Wenn es um Deckungsablehnung Red-Team in Versicherungsrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| `vers-dokumentenintake-police-avb-nachtraege` | Wenn es um Police, AVB, Nachträge und Maklerakte lesbar machen in Versicherungsrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `vers-fristen-verjaehrung-klagefrist-fallkalender` | Wenn es um Fristenkalender für Versicherungsfälle in Versicherungsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vers-kaltstart-routing` | Wenn es um Versicherungsrecht: Kaltstart, Rollenklärung und Triage in Versicherungsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vers-ombudsmann-versicherungsbetrug` | Wenn es um Ombudsmann, BaFin-Beschwerde oder Klage? in Versicherungsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `versicherungsbetrug-verdachtsfall-kooperation-strafrecht` | Wenn es um Verdacht Versicherungsbetrug und Kooperation mit Strafrecht in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Ri... |
| `versicherungsmakler-haftung-deckungsluecke` | Wenn es um Versicherungsmaklerhaftung bei Deckungslücken in Versicherungsrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `versicherungsprodukt-agb-betriebshaftpflicht` | Wenn es um Versicherungsbedingungen als AGB prüfen in Versicherungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `versicherungssumme-unterversicherung-taxwert` | Wenn es um Versicherungssumme, Unterversicherung und Taxwert in Versicherungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vvg-anzeigepflicht-ruecktritt-arglist` | Wenn es um Vorvertragliche Anzeigepflicht Paragraf 19 VVG in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näc... |
| `vvg-arglist-taeuschung-anfechtung` | Wenn es um Arglistanfechtung des Versicherers in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `vvg-falligkeit-14-abschlagszahlung` | Wenn es um Fälligkeit und Abschlagszahlung Paragraf 14 VVG in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachw... |
| `vvg-gefahrerhoehung-mehrfachversicherung` | Wenn es um Gefahrerhöhung Paragrafen 23–27 VVG in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `vvg-obliegenheit-28-quotelung-kausalitaet` | Wenn es um Obliegenheitsverletzung Paragraf 28 VVG und Quotierung in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `vvg-versicherung-wohngebaeude-leitungswasser` | Wenn es um Versicherung für fremde Rechnung Paragrafen 43–48 VVG in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und... |
| `wohngebaeude-leitungswasser-sturm-hagel-brand` | Wenn es um Wohngebäudeversicherung: Leitungswasser, Sturm, Brand in Versicherungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

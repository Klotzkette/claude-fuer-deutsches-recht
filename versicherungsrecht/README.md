# Versicherungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`versicherungsrecht`) | [`versicherungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versicherungsrecht.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

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

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `bu-berufsbild-bu-nachpruefung-datenschutz` | Bu Berufsbild 50 Prozent Substantiierung, Bu Nachpruefung Anerkenntnis Leistungseinstellung, Datenschutz Schweigepflicht Gesundheitsdaten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `cyberversicherung-ransomware-d-o` | Cyberversicherung Ransomware Sanktionsrecht, D O Claims Made Innenhaftung 43 Gmbhg, Elementarschaden Starkregen Ueberschwemmung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächst... |
| `deckungsprozess-vvg-rechtsabteilung` | Deckungsprozess Zustaendigkeit 215 Vvg, Rechtsabteilung Rechtsschutzversicherung Im Massenverfahren, Sachverstaendigenverfahren Versicherung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefe... |
| `direktanspruch-pflichtversicherung-eiopa` | Direktanspruch Pflichtversicherung 115 Vvg, Eiopa Grenzueberschreitender Vertrieb, Gewerbe Betriebsschliessung Infektionsschutz: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächst... |
| `dora-cyber-abfindung-entschaedigungsquittung` | Dora Cyber Ikt Versicherer, Vergleich Abfindung Entschaedigungsquittung, Bu Abstrakte Konkrete Verweisung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `hausrat-einbruchdiebstahl-idd-vertrieb` | Hausrat Einbruchdiebstahl Entschaedigungsgrenze, Idd Vertrieb Beratung Dokumentation, Internationales Versicherungsprogramm Master Local Policy: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und li... |
| `kfz-haftpflicht-kasko-grobe-krankentagegeld` | Kfz Haftpflicht Regress Alkohol Flucht, Kfz Kasko Grobe Fahrlaessigkeit Entwendung, Krankentagegeld Berufsunfaehigkeit Abgrenzung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den näch... |
| `kreditausfallversicherung-warenkredit` | Kreditausfallversicherung Warenkredit Forderungsausfall, Kreditversicherung Obliegenheiten Limit Prüfung, Lebensversicherung Bezugsrecht Widerruf Aenderung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrun... |
| `lebensversicherung-rueckkaufswert` | Lebensversicherung Rueckkaufswert Abschlusskosten Widerspruch, Lebensversicherung Ueberschussbeteiligung Bewertungsreserven, Nachhaltigkeit Taxonomie Sfdr Versicherungsprodukt: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, B... |
| `pkv-kostenerstattung-private` | Pkv Kostenerstattung Medizinische Notwendigkeit, Private Krankenversicherung Beitragsanpassung Treuhaender, Produkthaftpflicht Rueckrufkosten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lief... |
| `rechtsabteilung-betriebsunterbrechung` | Rechtsabteilung Betriebsunterbrechung Und Lieferkettenausfall, Rechtsabteilung Cyberversicherung Nach Ransomware, Rechtsabteilung Idd Vertrieb Und Provisionskonflikt: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `rechtsabteilung-d-umwelthaftpflicht` | Rechtsabteilung D O Deckung Bei Organhaftung, Umwelthaftpflicht Umweltschadenversicherung, Versicherungsmakler Haftung Deckungsluecke: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den... |
| `rechtsschutz-deckungszusage-erfolgsaussicht` | Rechtsschutz Deckungszusage Stichentscheid, Rechtsschutz Erfolgsaussicht Mutwilligkeit, Reiseversicherung Rücktritt Abbruch Krankheit: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den... |
| `restschuldversicherung-widerruf` | Restschuldversicherung Widerruf Kopplung Verbraucherdarlehen, Rueckversicherung Cut Through Und Fronting, Solvency Ii Scr Orsa Aufsichtsrecht: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lief... |
| `subrogation-regress-transportversicherung` | Subrogation Regress 86 Vvg, Transportversicherung Ware Lagerung, Vag Bafin Aufsicht Beschwerde Missstand: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `unfallversicherung-invaliditaet-vers` | Unfallversicherung Invaliditaet Fristen Gliedertaxe, Vers Fristen Verjaehrung Klagefrist Fallkalender, Rechtsschutz Vorvertraglichkeit Schadenereignis: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `vers-deckungsablehnung-redteam` | Deckungsablehnung des Versicherers zerlegen: Risikoausschluss, Obliegenheit, Kausalität, grobe Fahrlässigkeit, Arglist, Beweislast und Vergleichsfenster systematisch prüfen. |
| `vers-dokumentenintake-police-avb-nachtraege` | Dokumentenintake für Versicherungsakten: Versicherungsschein, AVB, Nachträge, Beratungsdokumentation, Schadenanzeige, Gutachten, Korrespondenz und Ablehnung in eine Aktenmatrix überführen. |
| `vers-kaltstart-routing` | Allgemeiner Einstieg ins Versicherungsrecht: Police, Bedingungen, Schadenereignis, Ablehnung, Fristen, Aufsicht, Ombudsmann und Klageweg strukturiert erfassen und passende Fachmodule vorschlagen. |
| `vers-ombudsmann-versicherungsbetrug` | Vers Ombudsmann Bafin Beschwerde Klageweg, Versicherungsbetrug Verdachtsfall Kooperation Strafrecht, Versicherungssumme Unterversicherung Taxwert: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und... |
| `versicherungsprodukt-agb-betriebshaftpflicht` | Versicherungsprodukt Agb Klauselkontrolle, Betriebshaftpflicht Versicherungsfall Serienschaden, Betriebsunterbrechung Sachschaden Trigger: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `versicherungsrecht-vvg-anzeigepflicht-ruecktritt-arglist` | Vvg Anzeigepflicht Ruecktritt Kuendigung Anpassung / Vvg Arglist Taeuschung Anfechtung / Vvg Falligkeit Abschlagszahlung: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastb... |
| `vvg-gefahrerhoehung-mehrfachversicherung` | Vvg Gefahrerhoehung 23 27, Vvg Mehrfachversicherung 78, Vvg Obliegenheit 28 Quotelung Kausalitaet: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `vvg-versicherung-wohngebaeude-leitungswasser` | Vvg Versicherung Für Fremde 43 48, Wohngebaeude Leitungswasser Sturm Hagel Brand: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

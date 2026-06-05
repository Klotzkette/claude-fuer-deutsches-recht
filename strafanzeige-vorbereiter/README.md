# Strafanzeige-Vorbereiter

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strafanzeige-vorbereiter`) | [`strafanzeige-vorbereiter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafanzeige-vorbereiter.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist ausdrücklich keine Strafanzeigenkanone. Es soll Gerichte und Staatsanwaltschaften nicht mit wütenden, unbelegten Anzeigen fluten und niemanden durch haltlose Vorwürfe unter Druck setzen. Wenn eine Strafanzeige aber nötig ist, führt es zu einem sauberen, nüchternen, beweisnahen Entwurf.

## Leitplanke

Wehe, es werden Dinge behauptet, die nicht stimmen. Das Plugin zwingt zur Trennung von eigener Wahrnehmung, Dokument, Zeuge, Vermutung und rechtlicher Bewertung. Bei eigener Beteiligung, Unternehmensfällen, schweren Gewalt-/Sexualdelikten, Wirtschaftsstrafsachen oder Berufsgeheimnissen: anwaltliche Hilfe einschalten.

## Was dieses Plugin gut kann

- Trennt Strafanzeige, Strafantrag, zivilrechtliche Alternativen und bloße Beschwerde.
- Prüft vorab § 164 StGB, §§ 186/187 StGB, § 824 BGB und Druckmittelrisiken.
- Baut Sachverhalt, Beweismatrix, Anlagenverzeichnis und Strafantragsfristen auf.
- Erzeugt erst am Ende einen Anzeigeentwurf, wenn die Tatsachenbasis trägt.

## Startlogik

Beginne mit dem allgemeinen Kaltstart-Skill. Er fragt Rolle, Ziel, Frist, Unterlagen, Risiken und gewünschten Output ab. Danach werden nur passende Spezial-Skills vorgeschlagen.

## Quellenhygiene

Normtexte werden aus amtlichen Quellen geprüft. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle verwendet. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anzeige-anfangsverdacht-anlagenverzeichnis` | Anzeige Anfangsverdacht 152 160 Stpo, Anzeige Anlagenverzeichnis Hashlog: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-antragsdelikte-anzeige-strafantrag` | Anzeige Antragsdelikte 77b Frist, Anzeige Strafantrag Form Frist: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-anwalt-anzeige-arbeitsplatz` | Anzeige Anwalt Einschalten Schwelle, Anzeige Arbeitsplatz Sexuelle Belaestigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-bankrott-anzeige-bedrohung` | Anzeige Bankrott 283, Anzeige Bedrohung 241: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-beleidigung-anzeige-betrug` | Anzeige Beleidigung 185 194, Anzeige Betrug 263: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-beweismatrix-anzeige-chatverlaeufe` | Anzeige Beweismatrix Tatsachen Meinungen, Anzeige Chatverlaeufe Emails Header: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-datenstraftaten-anzeige-diebstahl` | Anzeige Datenstraftaten 202a 303a, Anzeige Diebstahl Unterschlagung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-druckmittel-anzeige-falsche` | Anzeige Druckmittel Verbot Noetigung, Anzeige Falsche Verdaechtigung 164: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-gegenanzeige-anzeige-geldwaesche` | Anzeige Gegenanzeige Risiko, Anzeige Geldwaesche 261: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-geschgehg-anzeige-haeusliche` | Anzeige Geschgehg 23 Geheimnisverrat, Anzeige Haeusliche Gewalt Gewschg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-hausfriedensbruch` | Anzeige Hausfriedensbruch 123, Anzeige Insolvenzverschleppung 15a: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-international-anzeige-klageerzwingung` | Anzeige International Eu 158 3, Anzeige Klageerzwingung 172 Stpo: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-kaltstart-routing` | Geführter Einstieg für Strafanzeigen: Sachverhalt, Beweise, Straftatverdacht, Strafantrag, Risiken falscher Verdächtigung, Alternativen und anwaltliche Eskalationsschwelle. |
| `anzeige-koerperverletzung-anzeige-korruption` | Anzeige Koerperverletzung 223 230, Anzeige Korruption 299 331ff: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-kreditgefaehrdung-minderjaehrige` | Anzeige Kreditgefaehrdung 824 Bgb, Anzeige Minderjaehrige Schule: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-muster-anzeige-noetigung` | Anzeige Muster Strafanzeige Generator, Anzeige Noetigung 240: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-nicht-anzeigen-redteam` | Red-Team prüft, ob eine Strafanzeige unnötig, riskant, zivilrechtlich kontraproduktiv oder straf-/haftungsrechtlich gefährlich wäre. |
| `anzeige-notruf-anzeige-online` | Anzeige Notruf Akut Gefahr, Anzeige Online Plattform Screenshots: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-onlinewache-anzeige-opferschutz` | Anzeige Onlinewache Vs Staatsanwaltschaft, Anzeige Opferschutz Nebenklage: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-rechtsfolgen-anzeige-ruecknahme` | Anzeige Rechtsfolgen Und Zivilstrategie, Anzeige Ruecknahme Einstellung 170 153: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-sachbeschaedigung-anzeige-sachverhalt` | Anzeige Sachbeschaedigung 303, Anzeige Sachverhalt Ohne Adjektive: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-stalking-anzeige-vs` | Anzeige Stalking 238, Anzeige Strafanzeige Vs Strafantrag 158: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-steuerhinterziehung-akteneinsicht` | Anzeige Steuerhinterziehung 370 Ao, Anzeige Akteneinsicht Verletzter 406e: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-tierschutz-anzeige-ueblerede` | Anzeige Tierschutz 17, Anzeige Ueblerede Verleumdung 186 187: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-umweltstraftaten-anzeige-unternehmen` | Anzeige Umweltstraftaten 324ff, Anzeige Unternehmen Internal Investigation: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-untreue-anzeige-urheberrecht` | Anzeige Untreue 266, Anzeige Urheberrecht Markenrecht: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-verkehrsunfall-anzeige-video` | Anzeige Verkehrsunfall Flucht 142, Anzeige Video Audio Kug 201: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-wer-anzeige-zeugenliste` | Anzeige Wer Was Wann Wo Wie, Anzeige Zeugenliste Kontakt: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anzeige-whistleblower-anzeige-computerbetrug` | Anzeige Compliance Whistleblower Hinschg, Anzeige Computerbetrug Phishing: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

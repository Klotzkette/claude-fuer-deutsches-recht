# Fluggastrechte

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fluggastrechte`) | [`fluggastrechte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fluggastrechte.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Fluggastrechte – Familie Bräutigam-Zaytuna** (`fluggastrechte-familie-braeutigam`) | [Gesamt-PDF lesen](../testakten/fluggastrechte-familie-braeutigam/gesamt-pdf/fluggastrechte-familie-braeutigam_gesamt.pdf) | [`testakte-fluggastrechte-familie-braeutigam.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fluggastrechte-familie-braeutigam.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Fluggastrechte selber geltend machen — VO (EG) Nr. 261/2004 plus EuGH-Rspr. Tickets erfassen Annullierung vs Verspätung prüfen außergewöhnliche Umstände Distanz und Ausgleich Forderungsschreiben Mahnung Klage Amtsgericht. Vollmacht Familie. Katalog Airline-Standardausreden.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Fluggastrechte (`fluggastrechte`, dieses Plugin) | [fluggastrechte.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fluggastrechte.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Fluggastrechte – Familie Bräutigam-Zaytuna** ([`testakten/fluggastrechte-familie-braeutigam/`](../testakten/fluggastrechte-familie-braeutigam/)).

Direkt-Download als ZIP: [testakte-fluggastrechte-familie-braeutigam.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fluggastrechte-familie-braeutigam.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Zum Ausprobieren: Beispielakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

[testakte-fluggastrechte-familie-braeutigam.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fluggastrechte-familie-braeutigam.zip)

Fiktive Mandatsakte einer fünfköpfigen Familie mit Verspätung von 10 Stunden auf der Strecke Frankfurt → Sydney via Singapur (Pacific Sky Airways, fiktiv) — enthält Mandantenanfrage, Tickets, Bestätigungs-Mails, Bordkarten, Hotelrechnung.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `airline-standardausreden-pruefen` | Katalog typischer Standardausreden der Fluggesellschaften mit Gegenargumenten und Pinpoint auf EuGH-Rechtsprechung. Behandelt technischer Defekt wilder Streik Streik der Gewerkschaft Crew-Engpass verdeckter Konstrukti… |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `ausnahmen-aussergewoehnliche-umstaende-pruefen` | Prüft die Einrede außergewöhnliche Umstände nach Art. 5 Abs. 3 VO 261/2004. Differenziert zwischen Wetter Vulkanasche Vogelschlag Streik Flugsicherung Streik der eigenen Mitarbeiter wilder Streik technischem Defek… |
| `distanz-und-ausgleich-berechnen` | Berechnet die Ausgleichszahlung nach Art. 7 VO 261/2004. Distanzbestimmung nach Großkreisrechnung zwischen Abflug- und Zielflughafen. Drei Stufen 250 EUR bis 1500 km / 400 EUR mehr als 1500 km innergemeinschaftlich o… |
| `forderungsschreiben-erste-stufe` | Erstes Forderungsschreiben an die Airline. Erfasst Anspruchsteller (alle Passagiere mit Vollmachten) Anspruchsgrundlage Art. 7 VO 261/2004 konkrete Berechnung Frist zur Zahlung (typisch zwei Wochen) Bankverbindung. In… |
| `forderungsschreiben-mahnung` | Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und dr… |
| `fluggastrechte-kaltstart-interview` | Kaltstart-Interview für das Fluggastrechte-Plugin. Klärt Anwendungsrolle (eigener Fluggastrechte-Anspruch / Vertretung Familie / Mitreisende). Erfasst Buchungsstammdaten Vertragspartner (Airline IATA-Code) und Reise… |
| `klage-amtsgericht-fluggast` | Klageentwurf zum Amtsgericht in Fluggastrechtsangelegenheiten. Sachliche Zuständigkeit § 23 Nr. 1 GVG bei Streitwert bis zehntausend Euro (i. d. F. seit 01.01.2026). Örtlich wahlweise Abflughafen oder Zielflughafen … |
| `ticket-und-fluginformationen-erfassen` | Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestätigungen Boardingpässe PDF-Scans Foto-Belegen. Extrahiert Buchungscode (PNR) Flugnummer Datum Abflughafen Zielflughafen geplante Abflugzeit geplante Ankun… |
| `vollmacht-familienmitglieder` | Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde) damit der Hauptansprechpartner deren Fluggastrechtsanspruch im Schriftverkehr und im gerichtlichen Verfahren mitvertreten kann. Pro Person eigene Vollm… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abtretung-an-fluggastportal-spezial` | Abtretung an Fluggastrechte-Portale (Flightright, EUclaim, AirHelp): Wirksamkeit nach RDG seit 2021, Provisionen, Vertragsklauseln gegenueber Mandanten. Eigene Vertretung gegen Portale, Vor- und Nachteile der Direktklage gegenueber Porta... |
| `airline-bonitaet-und-vollstreckung` | Airline-Bonitaetspruefung und Vollstreckung: Risikoliste bekannter Insolvenzen, Hinterlegung in dotierten Reisesicherungsfonds, EU-Garantien, Pruefraster bevor Klage erhoben wird. Vollstreckung im Ausland (Bruessel-I-VO, EuVTVO). Pruefli... |
| `airline-standardausreden-pruefen` | Katalog typischer Standardausreden der Fluggesellschaften mit Gegenargumenten und Pinpoint auf EuGH-Rechtsprechung. Behandelt technischer Defekt wilder Streik Streik der Gewerkschaft Crew-Engpass verdeckter Konstruktionsfehler vorheriger... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Fluggastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei... |
| `annullierung-oder-verspaetung-einordnen` | Workflow-Skill zu annullierung oder verspaetung einordnen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `anschlussflug-und-reiseplan` | Workflow-Skill zu anschlussflug und reiseplan. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `ausnahmen-aussergewoehnliche-umstaende-pruefen` | Workflow-Skill zu ausnahmen aussergewoehnliche umstaende pruefen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `aussergewoehnliche-umstaende-strikt` | Streng auszulegende aussergewoehnliche Umstaende Art. 5 Abs. 3 VO 261: Wetter, Streik nicht eigener Mitarbeiter, gerichtlich verfuegte Flugverbote, Wildschlag in Triebwerk. Keine aussergewoehnlichen Umstaende: technische Defekte (EuGH Wa... |
| `distanz-und-ausgleich-berechnen` | Berechnet die Ausgleichszahlung nach Art. 7 VO 261/2004. Distanzbestimmung nach Grosskreisrechnung zwischen Abflug- und Zielflughafen. Drei Stufen 250 EUR bis 1500 km / 400 EUR mehr als 1500 km innergemeinschaftlich oder 1500 bis 3500 km... |
| `flug-anschlussflug-codeshare-spezial` | Spezialfall Anschlussflug und Codeshare: einheitliche Buchung, ausfuehrendes Luftfahrtunternehmen, Drittland-Strecken nach EuGH wegfin. Pruefraster fuer Klagezustaendigkeit. |
| `flug-anspruch-uebersicht` | Uebersicht Fluggastrechte VO 261 / 2004: Annullierung, grosse Verspaetung ab drei Stunden, Nichtbefoerderung, Pauschalentschaedigung 250 Euro / 400 Euro / 600 Euro je nach Distanz. Pruefraster Anspruchsgrundlage. |
| `flug-ausserordentlicher-umstand-leitfaden` | Leitfaden ausserordentlicher Umstand: EuGH-Kasuistik Streik / Wetter / technischer Defekt, Beweislast Airline, zumutbare Massnahmen. Pruefraster fuer Klaegeranwalt. |
| `flug-massenklage-prozessfinanzierung-spezial` | Spezialfall Massenklage und Prozessfinanzierung in Fluggastrechten: Abtretung, Inkasso-Modelle, RDG-Grenzen, Anti-Claim-Klausel. Pruefraster fuer Verbraucher und Legal-Tech. |
| `fluggastrechte-anlagen-bauen` | Baut aus den Belegen eines Fluggastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsatz (Forderungsschreiben Mahnung Klage) die Belege Buchungsbestätigung Boardingpass Annullierungsbestätigung E-Mail-Ve... |
| `fluggastrechte-einfuehrung-vo-261` | Einfuehrung VO (EG) 261/2004: Anwendungsbereich (Abflug aus EU, Ankunft in EU mit EU-Carrier), Annullierung, Verspaetung ab 3 Stunden (EuGH-Sturgeon), Nichtbefoerderung. Ausgleichsstufen 250 Euro / 400 Euro / 600 Euro. Betreuungsleistung... |
| `fluggastrechte-kaltstart-interview` | Kaltstart-Interview für das Fluggastrechte-Plugin. Klaert Anwendungsrolle (eigener Fluggastrechte-Anspruch / Vertretung Familie / Mitreisende). Erfasst Buchungsstammdaten Vertragspartner (Airline IATA-Code) und Reiseplan-Konvention. Schr... |
| `forderungsschreiben-erste-stufe` | Workflow-Skill zu forderungsschreiben erste stufe. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `forderungsschreiben-mahnung` | Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und droht konkret SOEP-Sch... |
| `klage-amtsgericht-fluggast` | Workflow-Skill zu klage amtsgericht fluggast. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `pauschalreise-statt-flug-pruefen` | Pauschalreise gegen Flug-Einzelbuchung: Reiseveranstalterhaftung nach §§ 651a ff. BGB, Pauschalreise-RL EU 2015 2302. Minderung, Schadensersatz, Ruecktritt. Verhaeltnis zur VO 261 (kumulativ moeglich, Anrechnung nach BGH). Pruefraster ob... |
| `rechtsweg-und-gerichtsstand-fluggast` | Rechtsweg und Gerichtsstand bei Flugverspaetung und Annullierung: Wohnsitz oder Flughafen Klaegerwahl nach EuGH Rehder. Amtsgericht bei bis 5000 Euro Streitwert. Zustaendige Schlichtungsstellen soep. Internationale Fragen Montrealer Uebe... |
| `spezial-annullierung-schriftsatz-brief-und-memo-bausteine` | Annullierung: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ausgleich-internationaler-bezug-und-schnittstellen` | Ausgleich: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-aussergewoehnliche-zahlen-schwellen-und-berechnung` | Aussergewoehnliche: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-distanz-mehrparteien-konflikt-und-interessen` | Distanz: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-erfassen-behoerden-gericht-und-registerweg` | Erfassen: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fluggastrechte-erstpruefung-und-mandatsziel` | Fluggastrechte: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-forderungsschreiben-formular-portal-und-einreichung` | Forderungsschreiben: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-geltend-fristen-form-und-zustaendigkeit` | Geltend: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kaltstart-abschlussprodukt-und-uebergabe` | Kaltstart: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-klage-mandantenkommunikation-entscheidungsvorlage` | Klage: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-live-sonderfall-und-edge-case` | Live: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-machen-dokumentenmatrix-und-lueckenliste` | Machen: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mahnung-red-team-und-qualitaetskontrolle` | Mahnung: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pruefen-livequellen-und-rechtsprechungscheck` | Pruefen: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsprechung-beweislast-und-darlegungslast` | Rechtsprechung: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-selber-tatbestand-beweis-und-belege` | Selber: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-tickets-risikoampel-und-gegenargumente` | Tickets: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-umstaende-compliance-dokumentation-und-akte` | Umstaende: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verifikation-fristennotiz-und-naechster-schritt` | Verifikation: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verspaetung-verhandlung-vergleich-und-eskalation` | Verspaetung: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `ticket-und-fluginformationen-erfassen` | Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestätigungen Boardingpaesse PDF-Scans Foto-Belegen. Extrahiert Buchungscode (PNR) Flugnummer Datum Abflughafen Zielflughafen geplante Abflugzeit geplante Ankunftszeit Tarifklasse P... |
| `vollmacht-familienmitglieder` | Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde) damit der Hauptansprechpartner deren Fluggastrechtsanspruch im Schriftverkehr und im gerichtlichen Verfahren mitvertreten kann. Pro Person eigene Vollmacht mit Inhalt Bezug... |
| `vorverlegung-flug-rechtsprechung` | Vorverlegung des Fluges um mehr als 1 Stunde gilt als Annullierung nach EuGH C-188/20 Azurair. Pruefraster und Berechnungsbeispiel, wann Ausgleichsanspruch entsteht. Abgrenzung zur Umbuchung ohne Ausgleichsanspruch. Schriftsatzbausteine. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin fluggastrechte: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin fluggastrechte: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin fluggastrechte: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fluggastrechte: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin fluggastrechte: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fluggastrechte: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin fluggastrechte: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin fluggastrechte: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fluggastrechte: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin fluggastrechte: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

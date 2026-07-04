# Fluggastrechte


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fluggastrechte`) | [`fluggastrechte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fluggastrechte.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Fluggastrechte – Familie Bräutigam-Zaytuna** (`fluggastrechte-familie-braeutigam`) | [Gesamt-PDF lesen](../testakten/fluggastrechte-familie-braeutigam/gesamt-pdf/fluggastrechte-familie-braeutigam_gesamt.pdf) | [`testakte-fluggastrechte-familie-braeutigam.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fluggastrechte-familie-braeutigam.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Fluggastrechte selber geltend machen nach VO (EG) Nr. 261/2004. Tickets erfassen, Annullierung oder Verspätung prüfen, außergewöhnliche Umstände, Distanz, Ausgleich, Forderungsschreiben, Mahnung und Klage. Rechtsprechung nur nach Live-Verifikation.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`fluggastrechte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fluggastrechte.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fluggastrechte/fluggastrechte-werkstatt.md" download><code>fluggastrechte-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fluggastrechte/fluggastrechte-schnellstart.md" download><code>fluggastrechte-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Fluggastrechte – Familie Bräutigam-Zaytuna: [Gesamt-PDF](../testakten/fluggastrechte-familie-braeutigam/gesamt-pdf/fluggastrechte-familie-braeutigam_gesamt.pdf), [`testakte-fluggastrechte-familie-braeutigam.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fluggastrechte-familie-braeutigam.zip), [`testakte-fluggastrechte-familie-braeutigam-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fluggastrechte-familie-braeutigam-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Fluggastrechte selber geltend machen — VO (EG) Nr. 261/2004 plus EuGH-Rspr. Tickets erfassen Annullierung vs Verspätung prüfen außergewöhnliche Umstände Distanz und Ausgleich Forderungsschreiben Mahnung Klage Amtsgericht. Vollmacht Familie. Katalog Airline-Standardausreden.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

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

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anschluss-router`, `anschluss-routing`, `dokumente-intake`, `einstieg-routing`, `erstpruefung-rollenklaerung-mandatsziel`, `kaltstart-abschlussprodukt-und-uebergabe`, `kaltstart-interview`, `kaltstart-triage`, `workflow-anschluss-skills-router`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `chronologie-und-belegmatrix`, `forderungsschreiben-formular-portal-und-einreichung`, `machen-dokumentenmatrix-lueckenliste`, `machen-dokumentenmatrix-und-lueckenliste`, `pruefen-quellenkarte`, `quellen-livecheck`, `rechtsprechung-beweislast-darlegungslast`, `rechtsprechung-beweislast-vorverlegung-flug`, `selber-tatbestandsmerkmale-beweisfragen-beleglage`, `spezial-pruefen-livequellen-und-rechtsprechungscheck`, `umstaende-compliance-dokumentation-aktenvermerk`, `umstaende-compliance-dokumentation-und-akte`, `unterlagen-luecken`, `workflow-chronologie-und-belegmatrix`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `flug-anschlussflug-codeshare-anspruch`, `flug-anspruch-uebersicht`, `fristen-und-risikoampel`, `tickets-risikoampel-gegenargumente`, `tickets-risikoampel-und-gegenargumente` |
| 4. Gestaltung, Strategie und Verhandlung | `anschlussflug-und-reiseplan`, `ausgleich-internationaler-bezug-schnittstellen`, `ausgleich-internationaler-bezug-und-schnittstellen`, `distanz-und-ausgleich-berechnen`, `verspaetung-verhandlung-vergleich-eskalation` |
| 5. Verfahren, Behörde und Gericht | `airline-bonitaet-und-vollstreckung`, `annullierung-schriftsatz-brief-memo-bausteine`, `annullierung-schriftsatz-brief-und-memo-bausteine`, `erfassen-behoerden-gericht-und-registerweg`, `erfassen-behoerden-gerichts-registerweg`, `flug-massenklage-einfuehrung-vo`, `flug-massenklage-prozessfinanzierung-spezial`, `forderungsschreiben-klage`, `forderungsschreiben-mahnung-klage-amtsgericht`, `geltend-fristen-form-und-zustaendigkeit`, `geltend-fristen-form-zustaendigkeit-rechtsweg`, `klage`, `klage-amtsgericht-fluggast`, `klage-mandantenkommunikation-entscheidungsvorlage`, `rechtsweg-gerichtsstand-annullierung`, `rechtsweg-und-gerichtsstand-fluggast`, `verifikation-fristennotiz-abtretung-an`, `verifikation-fristennotiz-naechster-schritt` |
| 6. Ergebnis, Schreiben und Kommunikation | `forderungsschreiben-airline`, `forderungsschreiben-erste-stufe`, `forderungsschreiben-mahnung`, `mandantenkommunikation`, `output-waehlen`, `workflow-mandantenkommunikation` |
| 7. Kontrolle, Qualität und Gegenprüfung | `live-sonderfall-machen-mahnung-red-team-korrektur`, `mahnung-fehlerkatalog`, `mahnung-red-team-und-qualitaetskontrolle`, `redteam-qualitygate`, `workflow-redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `abtretung-an-fluggastportal-spezial`, `airline-standardausreden-annullierung`, `airline-standardausreden-pruefen`, `anlagen-bauen`, `annullierung-oder-verspaetung-einordnen`, `ausnahmen-aussergewoehnliche-umstaende`, `ausnahmen-aussergewoehnliche-umstaende-02`, `aussergewoehnliche-distanz-interessen`, `aussergewoehnliche-umstaende`, `aussergewoehnliche-umstaende-strikt`, `distanz-interessen`, `distanz-mehrparteien-konflikt-und-interessen`, `einfuehrung-vo-261`, `flug-anschlussflug-codeshare-spezial`, `flug-ausserordentlicher-umstand-leitfaden`, `fluggastrechte-anlagen-bauen`, `live-sonderfall-edge-case`, `pauschalreise-statt-flug-pruefen`, ... plus 5 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 87 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abtretung-an-fluggastportal-spezial` | Wenn es um Abtretung an Fluggastportale in Fluggastrechte geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `airline-bonitaet-und-vollstreckung` | Wenn es um Airline-Bonitaet und Vollstreckung in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `airline-standardausreden-annullierung` | Wenn es um Airline-Standardausreden — Katalog und Gegenargumente in Fluggastrechte geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: A... |
| `airline-standardausreden-pruefen` | Wenn es um Airline-Standardausreden — Katalog und Gegenargumente in Fluggastrechte geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: A... |
| `anlagen-bauen` | Wenn es um Fluggastrechte — Anlagen bauen in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `annullierung-oder-verspaetung-einordnen` | Wenn es um Annullierung Verspätung oder Nichtbeförderung einordnen in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `annullierung-schriftsatz-brief-memo-bausteine` | Wenn es um Annullierung: Schriftsatz-, Brief- und Memo-Bausteine in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `annullierung-schriftsatz-brief-und-memo-bausteine` | Wenn es um Annullierung: Schriftsatz-, Brief- und Memo-Bausteine in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anschluss-router` | Wenn es um Fluggastrechte — Allgemein in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anschluss-routing` | Wenn es um Anschluss-Routing in Fluggastrechte geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `anschlussflug-und-reiseplan` | Wenn es um Anschlussflug und Reiseplan in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausgleich-internationaler-bezug-schnittstellen` | Wenn es um Ausgleich: Internationaler Bezug und Schnittstellen in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ausgleic... |
| `ausgleich-internationaler-bezug-und-schnittstellen` | Wenn es um Ausgleich: Internationaler Bezug und Schnittstellen in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ausgleic... |
| `ausnahmen-aussergewoehnliche-umstaende` | Wenn es um Außergewöhnliche Umstände prüfen (Art. 5 Abs. 3 VO 261/2004) in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `ausnahmen-aussergewoehnliche-umstaende-02` | Wenn es um Außergewöhnliche Umstände prüfen (Art. 5 Abs. 3 VO 261/2004) in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `aussergewoehnliche-distanz-interessen` | Wenn es um Aussergewoehnliche: Zahlen, Schwellenwerte und Berechnung in Fluggastrechte geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `aussergewoehnliche-umstaende` | Wenn es um Aussergewoehnliche: Zahlen, Schwellenwerte und Berechnung in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aussergewoehnliche-umstaende-strikt` | Wenn es um Aussergewoehnliche Umstaende in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `distanz-interessen` | Wenn es um Distanz: Mehrparteienkonflikt und Interessenmatrix in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Distanz I... |
| `distanz-mehrparteien-konflikt-und-interessen` | Wenn es um Distanz: Mehrparteienkonflikt und Interessenmatrix in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Distanz M... |
| `distanz-und-ausgleich-berechnen` | Wenn es um Distanz und Ausgleichszahlung berechnen in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `dokumente-intake` | Wenn es um Dokumentenintake in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einfuehrung-vo-261` | Wenn es um Fluggastrechte VO 261: Einfuehrung in Fluggastrechte geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `einstieg-routing` | Wenn es um Einstieg und Routing in Fluggastrechte geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erfassen-behoerden-gericht-und-registerweg` | Wenn es um Erfassen: Behörden-, Gerichts- oder Registerweg in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Erfassen Beh... |
| `erfassen-behoerden-gerichts-registerweg` | Wenn es um Erfassen: Behörden-, Gerichts- oder Registerweg in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Erfassen Beh... |
| `erstpruefung-rollenklaerung-mandatsziel` | Wenn es um Fluggastrechte: Erstprüfung, Rollenklärung und Mandatsziel in Fluggastrechte geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `flug-anschlussflug-codeshare-anspruch` | Wenn es um Flug: Anschlussflug Codeshare in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Flug Anschlussflug Codeshare A... |
| `flug-anschlussflug-codeshare-spezial` | Wenn es um Flug: Anschlussflug Codeshare in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Flug Anschlussflug Codeshare S... |
| `flug-anspruch-uebersicht` | Wenn es um Flug: Anspruch-Übersicht in Fluggastrechte geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `flug-ausserordentlicher-umstand-leitfaden` | Wenn es um Flug: ausserordentlicher Umstand in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `flug-massenklage-einfuehrung-vo` | Wenn es um Flug: Massenklage RDG in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort: Flug Massen... |
| `flug-massenklage-prozessfinanzierung-spezial` | Wenn es um Flug: Massenklage RDG in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort: Flug Massen... |
| `fluggastrechte-anlagen-bauen` | Wenn es um Fluggastrechte-Anlagen bauen in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `forderungsschreiben-airline` | Wenn es um Forderungsschreiben: Formular, Portal und Einreichungslogik in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `forderungsschreiben-erste-stufe` | Wenn es um Forderungsschreiben Erste Stufe in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `forderungsschreiben-formular-portal-und-einreichung` | Wenn es um Forderungsschreiben: Formular, Portal und Einreichungslogik in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `forderungsschreiben-klage` | Wenn es um Fluggastrechte: Erstprüfung, Rollenklärung und Mandatsziel in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlage... |
| `forderungsschreiben-mahnung` | Wenn es um Forderungsschreiben — Mahnung (zweite Stufe) in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Forderu... |
| `forderungsschreiben-mahnung-klage-amtsgericht` | Wenn es um Forderungsschreiben — Mahnung (zweite Stufe) in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Forderu... |
| `fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `geltend-fristen-form-und-zustaendigkeit` | Wenn es um Geltend: Fristen, Form, Zuständigkeit und Rechtsweg in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Geltend... |
| `geltend-fristen-form-zustaendigkeit-rechtsweg` | Wenn es um Geltend: Fristen, Form, Zuständigkeit und Rechtsweg in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Geltend... |
| `kaltstart-abschlussprodukt-und-uebergabe` | Wenn es um Kaltstart: Abschlussprodukt und Übergabe in Fluggastrechte geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-interview` | Wenn es um /fluggastrechte:fluggastrechte-kaltstart-interview in Fluggastrechte geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-triage` | Wenn es um Kaltstart Triage in Fluggastrechte geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `klage` | Wenn es um Klage: Mandantenkommunikation und Entscheidungsvorlage in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `klage-amtsgericht-fluggast` | Wenn es um Klage Amtsgericht Fluggast in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `klage-mandantenkommunikation-entscheidungsvorlage` | Wenn es um Klage: Mandantenkommunikation und Entscheidungsvorlage in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `live-sonderfall-edge-case` | Wenn es um Live: Sonderfall und Edge-Case-Prüfung in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `live-sonderfall-machen-mahnung-red-team-korrektur` | Wenn es um Live: Sonderfall und Edge-Case-Prüfung in Fluggastrechte geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `machen-dokumentenmatrix-lueckenliste` | Wenn es um Machen: Dokumentenmatrix, Lückenliste und Nachforderung in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `machen-dokumentenmatrix-und-lueckenliste` | Wenn es um Machen: Dokumentenmatrix, Lückenliste und Nachforderung in Fluggastrechte geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `mahnung-fehlerkatalog` | Wenn es um Mahnung Fehlerkatalog in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mahnung-red-team-und-qualitaetskontrolle` | Wenn es um Mahnung: Red-Team und Qualitätskontrolle in Fluggastrechte geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mandantenkommunikation` | Wenn es um Mandantenkommunikation in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `output-waehlen` | Wenn es um Output wählen in Fluggastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pauschalreise-statt-flug-pruefen` | Wenn es um Pauschalreise gegen Einzelflug in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pruefen-quellenkarte` | Wenn es um Prüfen Quellenkarte in Fluggastrechte geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in Fluggastrechte geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `rechtsprechung-beweislast-darlegungslast` | Wenn es um Rechtsprechung: Beweislast, Darlegungslast und Substantiierung in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwor... |
| `rechtsprechung-beweislast-vorverlegung-flug` | Wenn es um Rechtsprechung: Beweislast, Darlegungslast und Substantiierung in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwor... |
| `rechtsweg-gerichtsstand-annullierung` | Wenn es um Rechtsweg und Gerichtsstand in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Rechtsweg Gerichtsstand Annullie... |
| `rechtsweg-und-gerichtsstand-fluggast` | Wenn es um Rechtsweg und Gerichtsstand in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Rechtsweg Und Gerichtsstand Flug... |
| `redteam-qualitygate` | Wenn es um Red-Team Qualitygate in Fluggastrechte geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Redteam Qualitygate; Arbeitsfeld:... |
| `selber-tatbestandsmerkmale-beweisfragen-beleglage` | Wenn es um Selber: Tatbestandsmerkmale, Beweisfragen und Beleglage in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `selber-tickets-umstaende` | Wenn es um Selber: Tatbestandsmerkmale, Beweisfragen und Beleglage in Fluggastrechte geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `spezial-pruefen-livequellen-und-rechtsprechungscheck` | Wenn es um Pruefen: Livequellen- und Rechtsprechungscheck in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ticket-und-fluginformationen-erfassen` | Wenn es um Ticket- und Fluginformationen erfassen in Fluggastrechte geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `tickets-risikoampel-gegenargumente` | Wenn es um Tickets: Risikoampel, Gegenargumente und Verteidigungslinien in Fluggastrechte geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstich... |
| `tickets-risikoampel-und-gegenargumente` | Wenn es um Tickets: Risikoampel, Gegenargumente und Verteidigungslinien in Fluggastrechte geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstich... |
| `umstaende-compliance-dokumentation-aktenvermerk` | Wenn es um Umstaende: Compliance-Dokumentation und Aktenvermerk in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umstaende-compliance-dokumentation-und-akte` | Wenn es um Umstaende: Compliance-Dokumentation und Aktenvermerk in Fluggastrechte geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verifikation-fristennotiz-abtretung-an` | Wenn es um Verifikation: Fristennotiz und nächster Schritt in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Verifikation... |
| `verifikation-fristennotiz-naechster-schritt` | Wenn es um Verifikation: Fristennotiz und nächster Schritt in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Verifikation... |
| `verspaetung-ticket-fluginformationen` | Wenn es um Verspaetung: Verhandlung, Vergleich und Eskalation in Fluggastrechte geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `verspaetung-verhandlung-vergleich-eskalation` | Wenn es um Verspaetung: Verhandlung, Vergleich und Eskalation in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vollmacht-familienmitglieder` | Wenn es um Vollmacht für Familienmitglieder und Mitreisende in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vorverlegung-flug-rechtsprechung` | Wenn es um Vorverlegung als Annullierung in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-anschluss-skills-router` | Wenn es um Anschluss-Skills Router in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Fluggastrechte geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in Fluggastrechte geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-mandantenkommunikation` | Wenn es um Mandantenkommunikation in Fluggastrechte geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `workflow-redteam-qualitygate` | Wenn es um Red-Team Qualitygate in Fluggastrechte geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Workflow Redteam Qualitygate; Arbe... |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in Fluggastrechte geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

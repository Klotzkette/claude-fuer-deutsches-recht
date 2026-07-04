# Handelsregister Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`handelsregister-praxis`) | [`handelsregister-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsregister-praxis.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Rabenhof Sensorik GmbH - Registergericht Charlottenburg, HRB 246810 B** (`handelsregister-registergericht-rabenhof-gmbh-2026`) | [Gesamt-PDF lesen](../testakten/handelsregister-registergericht-rabenhof-gmbh-2026/gesamt-pdf/handelsregister-registergericht-rabenhof-gmbh-2026_gesamt.pdf) | [`testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Praxisplugin für den Umgang mit dem Handelsregister: Anmeldung, Registergericht, Rechtspfleger, Registerrichter, Beanstandung, Zwischenverfügung, Beschwerde, Gesellschafterliste, Kapitalmaßnahmen, Firma, Vertretung, Prokura, Löschung, Insolvenzvermerk und registerfeste Nachweise.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`handelsregister-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsregister-praxis.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/handelsregister-praxis/handelsregister-praxis-werkstatt.md" download><code>handelsregister-praxis-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/handelsregister-praxis/handelsregister-praxis-schnellstart.md" download><code>handelsregister-praxis-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Rabenhof Sensorik GmbH - Registergericht Charlottenburg, HRB 246810 B: [Gesamt-PDF](../testakten/handelsregister-registergericht-rabenhof-gmbh-2026/gesamt-pdf/handelsregister-registergericht-rabenhof-gmbh-2026_gesamt.pdf), [`testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip), [`testakte-handelsregister-registergericht-rabenhof-gmbh-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsregister-registergericht-rabenhof-gmbh-2026-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine Handelsregistersache praktisch vorbereiten: Anmeldung, Vertretungsnachweis, Gesellschafterliste, Eintragungshindernis, Zwischenverfügung, Registerbeschwerde oder Vollzug.
Ein Registergerichts-Cockpit für Gesellschaftsrechtler, Notariate, Kanzleien und Rechtsabteilungen. Es ordnet, was eingetragen werden soll, welche Urkunden nötig sind, wer beim Registergericht entscheidet, wie man Beanstandungen beantwortet und wann Beschwerde oder Eilrechtsschutz Sinn ergeben.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `handelsregister-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- HGB §§ 8 ff., § 15
- FamFG Registersachen und Beschwerde
- GmbHG Anmeldung, Gesellschafterliste, Kapitalmaßnahmen
- [Registerportal der Länder](https://www.handelsregister.de)
- [Unternehmensregister](https://www.unternehmensregister.de)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `kaltstart-routing`, `registerrecht-mandatsannahme-notarferne` |
| 2. Unterlagen, Sachverhalt und Quellen | `chronologischer-registerauszug`, `ki-registerakte-nachlass`, `registerakte-schnellscan-registerauszug-lesen`, `registerauszug-lesen`, `registerbeweis-im-prozess`, `registergericht-rollen-datenschutz`, `registergericht-und-datenschutz`, `registerrecht-registerzeichen-und-aktenzeichen` |
| 3. Prüfung, Anspruch und Subsumtion | `firma-firmenbildung-formwechsel-registercheck`, `formwechsel-registercheck`, `verschmelzung-gmbh-registercheck` |
| 4. Gestaltung, Strategie und Verhandlung | `eintragung-prozessvergleich-registerfolge`, `gesellschafterlistenstreit-eilstrategie-gmbh`, `internationaler-registervergleich` |
| 5. Verfahren, Behörde und Gericht | `amtsloeschung-familienloeschung-registerblatt`, `beanstandung-zwischenverfuegung`, `closing-handelregister-einstweiliger`, `einstweiliger-rechtsschutz-registerstreit`, `famfg-beschwerde-registersache`, `frist-und-vollzugslog-register`, `genossenschaft-registerschnittstelle`, `gmbh-co-kg-registerdoppelvollzug`, `insolvenzvermerk-registereintrag`, `nachlass-und-testamentsvollstrecker-register`, `notar-registergericht-kommunikation`, `online-abruf-registerportal-unternehmensregister`, `partg-partgmbb-register`, `rechtsabteilung-kapitalerhoehung-und-zwischenverfuegung`, `rechtsabteilung-mopeg-gesellschaftsregister-und-ohg-sprung`, `rechtsprechung-register-frist-vollzugslog`, `rechtsschein-innenstreit-register`, `register-mandantenbrief`, ... plus 18 weitere |
| 6. Ergebnis, Schreiben und Kommunikation | `fehlerhafte-eintragung-berichtigung`, `rechtsabteilung-insolvenzvermerk` |
| 7. Kontrolle, Qualität und Gegenprüfung | `register-qualitaetsgate-vor-einreichung`, `unternehmensgegenstand-beanstandung` |
| 8. Spezialmodule und Schnittstellen | `auslandsurkunden-apostille-legalisation-uebersetzung`, `bekanntmachungen-monitoring`, `erlaubnispflichtige-taetigkeit-famfg`, `gmbh-geschaeftsfuehrerbestellung-abberufung`, `gmbh-gesellschafterliste-paragraph-gruendung`, `gmbh-gruendung-erstanmeldung`, `gmbh-kapitalerhoehung-bareinlage`, `gmbh-kapitalerhoehung-sacheinlage`, `gmbh-kapitalherabsetzung-und-schutzjahr`, `gmbh-liquidation-und-loeschung`, `gmbh-satzungsaenderung-handelsvollmacht-nicht`, `handelsvollmacht-nicht-eintragungsfaehig`, `hgb-publizitaet-paragraph-15`, `kg-kommanditist-eintritt-austritt-haftsumme`, `ohg-kg-online-abruf-partg-partgmbb`, `prokura-eintragung-rechtsabteilung`, `rechtsabteilung-geschaeftsfuehrerbestellung-mit-auslandsbezug`, `rechtsabteilung-gesellschafterliste-nach-streit-und-ev`, ... plus 3 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 77 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtsloeschung-familienloeschung-registerblatt` | Wenn es um Amtslöschung und Registerbereinigung in Handelsregister Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `auslandsurkunden-apostille-legalisation-uebersetzung` | Wenn es um Auslandsurkunden registerfest machen in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beanstandung-zwischenverfuegung` | Wenn es um Beanstandung und Zwischenverfügung beantworten in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bekanntmachungen-monitoring` | Wenn es um Registerbekanntmachungen überwachen in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `chronologischer-registerauszug` | Wenn es um Chronologischen Auszug auswerten in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `closing-handelregister-einstweiliger` | Wenn es um Registervollzug im Closing in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einstweiliger-rechtsschutz-registerstreit` | Wenn es um Eilrechtsschutz bei Registerstillstand in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `eintragung-prozessvergleich-registerfolge` | Wenn es um Prozessvergleich mit Registerfolge in Handelsregister Praxis geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `erlaubnispflichtige-taetigkeit-famfg` | Wenn es um Erlaubnispflichten und Register in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `famfg-beschwerde-registersache` | Wenn es um Beschwerde in Registersachen in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fehlerhafte-eintragung-berichtigung` | Wenn es um Fehlerhafte Eintragung korrigieren in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `firma-firmenbildung-formwechsel-registercheck` | Wenn es um Firma und Firmenbeanstandung in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `formwechsel-registercheck` | Wenn es um Formwechsel Registercheck in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `frist-und-vollzugslog-register` | Wenn es um Fristen- und Vollzugslog in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `genossenschaft-registerschnittstelle` | Wenn es um Genossenschaftsregister-Schnittstelle in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gesellschafterlistenstreit-eilstrategie-gmbh` | Wenn es um Gesellschafterlistenstreit strategisch führen in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `gmbh-co-kg-registerdoppelvollzug` | Wenn es um GmbH & Co. KG Doppelvollzug in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gmbh-geschaeftsfuehrerbestellung-abberufung` | Wenn es um Geschäftsführerwechsel in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gmbh-gesellschafterliste-paragraph-gruendung` | Wenn es um Gesellschafterliste und Widerspruch in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `gmbh-gruendung-erstanmeldung` | Wenn es um GmbH/UG-Erstanmeldung in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `gmbh-kapitalerhoehung-bareinlage` | Wenn es um Barkapitalerhöhung in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gmbh-kapitalerhoehung-sacheinlage` | Wenn es um Sachkapitalerhöhung in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gmbh-kapitalherabsetzung-und-schutzjahr` | Wenn es um Kapitalherabsetzung in Handelsregister Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `gmbh-liquidation-und-loeschung` | Wenn es um Liquidation und Löschung in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `gmbh-satzungsaenderung-handelsvollmacht-nicht` | Wenn es um Satzungsänderung in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `handelsvollmacht-nicht-eintragungsfaehig` | Wenn es um Handlungsvollmacht richtig abgrenzen in Handelsregister Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `hgb-publizitaet-paragraph-15` | Wenn es um Publizität und Vertrauen auf das Register in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `insolvenzvermerk-registereintrag` | Wenn es um Insolvenzvermerk im Register in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `internationaler-registervergleich` | Wenn es um Ausländische Register verstehen in Handelsregister Praxis geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `kaltstart-routing` | Wenn es um Kaltstart-Interview und Registerfahrplan in Handelsregister Praxis geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kg-kommanditist-eintritt-austritt-haftsumme` | Wenn es um Kommanditist und Haftsumme in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ki-registerakte-nachlass` | Wenn es um digitale Werkzeuge-Halluzinationsschutz in Registerakten in Handelsregister Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `nachlass-und-testamentsvollstrecker-register` | Wenn es um Nachlassvertretung im Register in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `notar-registergericht-kommunikation` | Wenn es um Notar und Registergericht steuern in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `ohg-kg-online-abruf-partg-partgmbb` | Wenn es um GbR/eGbR zu OHG/KG in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `online-abruf-registerportal-unternehmensregister` | Wenn es um Registerabruf richtig dokumentieren in Handelsregister Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `partg-partgmbb-register` | Wenn es um PartG/PartG mbB in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `prokura-eintragung-rechtsabteilung` | Wenn es um Prokura anmelden und löschen in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rechtsabteilung-geschaeftsfuehrerbestellung-mit-auslandsbezug` | Wenn es um Rechtsabteilung: Geschäftsführerbestellung mit Auslandsbezug in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständi... |
| `rechtsabteilung-gesellschafterliste-nach-streit-und-ev` | Wenn es um Rechtsabteilung: Gesellschafterliste nach Streit und EV in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweisc... |
| `rechtsabteilung-insolvenzvermerk` | Wenn es um Rechtsabteilung: Insolvenzvermerk und ausländischer Trustee in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachw... |
| `rechtsabteilung-kapitalerhoehung-und-zwischenverfuegung` | Wenn es um Rechtsabteilung: Kapitalerhöhung und Zwischenverfügung in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Ris... |
| `rechtsabteilung-mopeg-gesellschaftsregister-und-ohg-sprung` | Wenn es um Rechtsabteilung: MoPeG-Gesellschaftsregister und OHG-Sprung in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachw... |
| `rechtsprechung-register-frist-vollzugslog` | Wenn es um Rechtsprechung nur verifiziert nutzen in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rechtsschein-innenstreit-register` | Wenn es um Innenstreit trotz Registerschein in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `register-mandantenbrief` | Wenn es um Mandantenbrief Registerstand in Handelsregister Praxis geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `register-qualitaetsgate-vor-einreichung` | Wenn es um Quality Gate vor Einreichung in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerakte-schnellscan-registerauszug-lesen` | Wenn es um Registerakte in 10 Minuten sortieren in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerauszug-lesen` | Wenn es um Handelsregisterauszug lesen in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerbeweis-im-prozess` | Wenn es um Registerbeweis im Zivilprozess in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registergericht-rollen-datenschutz` | Wenn es um Rechtspfleger, Registerrichter, Geschäftsstelle in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `registergericht-und-datenschutz` | Wenn es um Datenschutz im Registerverfahren in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerkosten-und-notarkosten` | Wenn es um Kosten und Gebühren antizipieren in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerrecht-aktiengesellschaft-vorstand` | Wenn es um AG: Vorstand/Aufsichtsrat anmelden in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerrecht-beschlussmaengel-und-registervollzug` | Wenn es um Beschlussmängel im Registervollzug in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `registerrecht-digitalgruendung` | Wenn es um Online-Gründung und DiRUG in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerrecht-fehlende-einzahlung-fehlerhafte` | Wenn es um Einzahlungsrisiko Stammkapital in Handelsregister Praxis geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `registerrecht-fehlerhafte-geschaeftsfuehreradresse` | Wenn es um Private Daten im Register in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerrecht-kapitalgesellschaft-co-kg-komplementaerwechsel` | Wenn es um Komplementärwechsel in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerrecht-mandatsannahme-notarferne` | Wenn es um Kanzlei ohne Notarvollzug in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerrecht-niederlassung-registergericht` | Wenn es um Niederlassung und Filiale in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerrecht-registergericht-telefonat-protokoll` | Wenn es um Registertelefonat protokollieren in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerrecht-registerzeichen-und-aktenzeichen` | Wenn es um Registerzeichen verstehen in Handelsregister Praxis geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `registerrecht-scheinloeschung` | Wenn es um Nachtragsliquidation in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerrecht-se-und-europaeische-gesellschaft` | Wenn es um SE Registervollzug in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registerrecht-umbenennung-rebranding` | Wenn es um Rebranding im Register in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `registersperre-closing-sitz-inlandsanschrift` | Wenn es um Registersperre als Deal-Risiko in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sitz-inlandsanschrift-und-geschaeftsanschrift` | Wenn es um Sitz, Geschäftsanschrift, Zustellung in Handelsregister Praxis geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `todesfall-gesellschafter-register` | Wenn es um Todesfall eines Gesellschafters in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `transparenzregister-schnittstelle-umwandlung` | Wenn es um Transparenzregister-Schnittstelle in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umwandlung-registervollzug` | Wenn es um Umwandlung im Register in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umzug-registerbezirk-amtsloeschung` | Wenn es um Sitzverlegung und Registerbezirk in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unternehmensgegenstand-beanstandung` | Wenn es um Unternehmensgegenstand entwerfen in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verein-registerschnittstelle-verschmelzung` | Wenn es um Vereinsregister-Schnittstelle in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `verschmelzung-gmbh-registercheck` | Wenn es um Verschmelzung GmbH Registercheck in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `vollmacht-und-anmeldung-oeffentliche-beglaubigung` | Wenn es um Anmeldung und Vollmacht formfest machen in Handelsregister Praxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zweigniederlassung-auslaendische-gesellschaft` | Wenn es um Zweigniederlassung Auslaendische Gesellschaft in Handelsregister Praxis geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

# Grundbuchamt Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`grundbuchamt-praxis`) | [`grundbuchamt-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grundbuchamt-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Haus Altenau - verlorener Grundschuldbrief, Wegerecht und Kaufpreisfälligkeit** (`grundbuchamt-briefgrundschuld-wegerecht-altenau-2026`) | [Gesamt-PDF lesen](../testakten/grundbuchamt-briefgrundschuld-wegerecht-altenau-2026/gesamt-pdf/grundbuchamt-briefgrundschuld-wegerecht-altenau-2026_gesamt.pdf) | [`testakte-grundbuchamt-briefgrundschuld-wegerecht-altenau-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grundbuchamt-briefgrundschuld-wegerecht-altenau-2026.zip) |
| **Akte Wusterhagen: Mühlenstau, Chaussee und Aufopferung** (`preussisches-landrecht-wusterhagen-muehlenstau-aufopferung`) | [Gesamt-PDF lesen](../testakten/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung/gesamt-pdf/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung_gesamt.pdf) | [`testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Grundbuch-Cockpit für alle, die Auszüge lesen, Urkunden grundbuchtauglich nachweisen, Zwischenverfügungen verstehen und Grundbuchvollzug sauber betreiben müssen. Schwerpunkt ist die praktische Leseführung durch Abteilung I, II und III, damit keine Dienstbarkeit, Vormerkung, Rangstelle oder Briefgrundschuld übersehen wird.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `grundbuchamt-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- [GBO](https://www.gesetze-im-internet.de/gbo/)
- [GBV](https://www.gesetze-im-internet.de/gbvfg/)
- [FamFG Aufgebotsverfahren](https://www.gesetze-im-internet.de/famfg/)
- [BGB Grundstücksrechte](https://www.gesetze-im-internet.de/bgb/)
- [Justizportal des Bundes und der Länder](https://justiz.de/)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 23 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abteilung-ii-iii-grundschuld-auflassung` | Abteilung Ii Dienstbarkeit Vormerkung Beschraenkung, Abteilung Iii Grundschuld Hypothek Rang, Auflassung Und Eigentumsumschreibung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den näc... |
| `auslandsurkunden-apostille-baulast-ist` | Auslandsurkunden Apostille Grundbuch, Baulast Ist Nicht Grundbuch, Beschwerde Grundbuchsache: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `bestandsverzeichnis-flurstueck-briefrecht` | Bestandsverzeichnis Flurstueck Und Zuschreibung, Briefrecht Abtretung Und Löschung, Dienstbarkeit Wegerecht Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbare... |
| `elektronischer-rechtsverkehr` | Elektronischer Rechtsverkehr Grundbuch, Familiengerichtliche Genehmigung Grundbuch, Finanzierung Und Rangstelle: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren O... |
| `gbo-antrag-gbr-egbr-genehmigungen` | Gbo Antrag Bewilligung Eintragung, Gbr Egbr Grundbuch, Genehmigungen Landwirtschaft Verkehrswert: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `grundbuch-grunderwerbsteuer-unbedenklichkeit` | Grunderwerbsteuer Unbedenklichkeitsbescheinigung, Grundschuld Bestellung Buchgrundschuld, Grundschuldbrief Verlust Aufgebot: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten b... |
| `grundbuch-qualitygate-vor-vollzug` | Prüft Antrag, Bewilligung, Rang, Nachweise, Anlagen, Genehmigungen, Urkundenform und Zahlungslogik. |
| `grundbuch-vollzugslog-amtswiderspruch` | Grundbuch Vollzugslog, Grundbuchamt Amtswiderspruch Und Richtigstellung, Grundbuchamt Brief Vs Buchrecht Erklaerung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbar... |
| `grundbuchamt-eilfall-rangverlust-erbbaurecht` | Grundbuchamt Eilfall Rangverlust, Grundbuchamt Erbbaurecht Schnittstelle, Grundbuchamt Flurbereinigung Und Umlegung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbar... |
| `grundbuchamt-gesamtgrundschuld-mithaft` | Grundbuchamt Gesamtgrundschuld Und Mithaft, Grundbuchamt Gesellschaftsrechtliche Vertretung, Grundbuchamt Insolvenz Auslaendischer Trustee: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `grundbuchamt-kaltstart-routing` | Führt durch Eigentum, Belastungen, Vollzugsziel, Grundbuchbezirk, Urkundentyp, Nachweise, Rang, Fristdruck und Kommunikationsweg mit dem Grundbuchamt. |
| `grundbuchamt-kommunikation-konkurrierende` | Grundbuchamt Kommunikation, Grundbuchamt Konkurrierende Antraege Rangkonflikt, Grundbuchamt Teilloesung Rangfreigabe: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastba... |
| `grundbuchamt-maengelmatrix-notariat` | Grundbuchamt Maengelmatrix, Notariat Vollzugsauftrag Grundbuch, Abteilung I Eigentum Und Erwerbsgrund: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `grundbuchamt-nichtigkeitsrisiko-kaufvertrags` | Grundbuchamt Nichtigkeitsrisiko Kaufvertrag, Kaufvertrags Check Grundbuch, Amtshaftung Und Vollzugsfehler: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `grundbuchauszug-due-lesen-abteilung` | Grundbuchauszug Für Due Diligence, Grundbuchauszug Lesen Abteilung I Ii Iii, Grundbuchberichtigung Erbfall: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `insolvenzvermerk-zwangsversteigerung-kataster` | Insolvenzvermerk Zwangsversteigerung, Kataster Liegenschaftskarte Abgleich, Leitungsrecht Und Energieanlagen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `loeschungsbewilligung-bank-nacherbenvermerk` | Loeschungsbewilligung Bank, Nacherbenvermerk Und Verfuegungsbeschraenkung, Niessbrauch Wohnungsrecht: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `paragraph-gbo-prioritaetsmitteilung` | Paragraph 29 Gbo Formnachweis, Prioritaetsmitteilung Und Rangbescheinigung, Rangprinzip Und Rangvorbehalt: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `reallast-erbbauzins-sanierungsvermerk` | Reallast Und Erbbauzins, Sanierungsvermerk Und Vorkaufsrechte Kommune, Teilflaechenkauf Und Vermessung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `rechtsprechung-grundbuch-aufgebotsverfahren` | Rechtsprechung Grundbuch Live Verifizieren, Aufgebotsverfahren Famfg, Auflassungsvormerkung Kaufvertrag: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `testamentsvollstrecker-grundbuch-vollmacht` | Testamentsvollstrecker Grundbuch, Vollmacht Vorsorgevollmacht Grundbuch, Vorkaufsrecht Wiederkaufsrecht: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `verlorene-genehmigung-verwalterzustimmung-weg` | Grundbuchamt Verlorene Genehmigung Und Ersatznachweis, Grundbuchamt Verwalterzustimmung Weg, Grundbuchamt Vollstreckungsunterwerfung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den n... |
| `weg-teilungsgrundbuch-zwischenverfuegung` | Weg Teilungsgrundbuch, Zwischenverfuegung Paragraph 18 Gbo: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

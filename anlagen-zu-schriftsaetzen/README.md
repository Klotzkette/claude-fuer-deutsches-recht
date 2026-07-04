# Anlagen zu Schriftsätzen


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`anlagen-zu-schriftsaetzen`) | [`anlagen-zu-schriftsaetzen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/anlagen-zu-schriftsaetzen.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Werkmann ./. K+B — Werklohnklage Lackieranlage Eschweiler — Anlagenkonvolut-Verfahren** (`anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler`) | [Gesamt-PDF lesen](../testakten/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler/gesamt-pdf/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler_gesamt.pdf) | [`testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Anlagenmanagement für gerichtliche Schriftsätze: sortiert chaotische Mandantenordner, E-Mails, Scans, Tabellen und Vorversionen zu beA-tauglichen K/B/AST/AG-Anlagen mit Verzeichnis, Konvolutdeckblaettern, Stempel-/Dateinamenregeln, Hashlog, Lückenliste und Qualitygate.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`anlagen-zu-schriftsaetzen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/anlagen-zu-schriftsaetzen.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/anlagen-zu-schriftsaetzen/anlagen-zu-schriftsaetzen-werkstatt.md" download><code>anlagen-zu-schriftsaetzen-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/anlagen-zu-schriftsaetzen/anlagen-zu-schriftsaetzen-schnellstart.md" download><code>anlagen-zu-schriftsaetzen-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Werkmann ./. K+B — Werklohnklage Lackieranlage Eschweiler — Anlagenkonvolut-Verfahren: [Gesamt-PDF](../testakten/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler/gesamt-pdf/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler_gesamt.pdf), [`testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip), [`testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin ist die Anlagenkanzlei im Kleinen: Es nimmt einen Schriftsatz, einen chaotischen Mandantenordner oder ein schon halb nummeriertes Anlagenpaket und macht daraus eine nachvollziehbare, gerichtstaugliche Anlagenstruktur.

Es hilft besonders dann, wenn nicht einfach „Anlage K1 bis K12“ vorliegt, sondern wenn eine echte Akte lebt: E-Mails mit Anhängen, Scans ohne OCR, Excel-Tabellen, Fotos, Chat-Screenshots, mehrere Vertragsfassungen, fremdsprachige Unterlagen, doppelte Dateien, geschwärzte Drittunterlagen, beA-Grenzen, Verfahrenswechsel und Richterhinweise. Das Plugin führt dann nicht nur eine Nummerierung aus, sondern baut eine Arbeitslogik: Welche Tatsache soll durch welche Anlage belegt werden? Welche Datei gehört wirklich zu K1? Welche Unterlagen sind nur Konvolutbestandteil? Welche Anlage ist zu groß, unleserlich, falsch benannt, doppelt oder im Schriftsatz nicht eingeführt?

## Wofür es gedacht ist

| Situation | Was das Plugin macht | Ergebnis |
| --- | --- | --- |
| Klage/Replik liegt vor, Anlagen sind noch ungeordnet | Schriftsatz lesen, Beweisanker erkennen, K-Nummern vorschlagen, Dateien zuordnen | K1/K2/K3-Reihenfolge, Anlagenverzeichnis, Lückenliste |
| Anlagen sind schon nummeriert, aber niemand traut dem Paket | Prüfmodus: Nummern, Zitate, Dateien, Stempel, Namen, Lesbarkeit und beA-Fähigkeit prüfen | Fehlerprotokoll mit Korrekturplan |
| Mandant liefert Datenraum/ZIP/USB-Stick | Duplikate, Fassungen, Hashes, Dateitypen, Zeitfolge und Relevanz sortieren | Belegmatrix und Nachforderungsliste |
| Eine Anlage ist ein Konvolut | Deckblatt, Untergliederung, interne Seiten-/Dokumentlogik, kurze Erläuterung für Gericht | `Anlage K1` mit `K1.1`, `K1.2`, `K1.3` |
| Elektronische Einreichung steht bevor | Dateinamen, PDF/OCR, Paketgrößen, Anlagenverzeichnis, Prüfvermerk | beA-/ERV-taugliches Versandpaket |

## Der K1-Gedanke

Die erste Anlage ist fast nie nur eine Datei. In großen Verfahren ist `K1` häufig der Orientierungspunkt für das Gericht: Vertrag, Auftrag, Rahmenvereinbarung, Nachtrag, Bestätigungsmail, Protokoll oder Dokumentenfamilie. Das Plugin behandelt `K1` deshalb als Sortierproblem:

1. **Was soll K1 beweisen?** Nicht „alles zum Vertrag“, sondern eine konkrete Tatsache.
2. **Ist K1 Einzelanlage oder Konvolut?** Bei Konvolut: Deckblatt, Reihenfolge, interne Kurzbezeichnungen.
3. **Welche Fassungen gibt es?** Entwurf, unterschriebene Fassung, Scan, OCR-PDF, E-Mail-Anhang, spätere Ergänzung.
4. **Welche Datei ist die gerichtliche Fassung?** Die anderen Fassungen wandern in den internen Hash-/Versionenlog.
5. **Wie wird K1 im Schriftsatz eingeführt?** Der Schriftsatz muss den Tatsachenkern selbst tragen; die Anlage belegt ihn nur.

## Drei Arbeitsmodi

**Auto-Benennung:** Der Schriftsatz enthält noch keine Nummern. Das Plugin liest die Beweisstellen und schlägt die Reihenfolge vor.

**Schriftsatz folgt:** Der Schriftsatz enthält bereits `Anlage K...`-Verweise. Das Plugin sucht die passenden Dateien, erkennt Lücken und meldet Überschüsse.

**Prüfmodus:** Ein fertiges Anlagenpaket wird gegengeprüft: `K7` fehlt, `K12` ist doppelt, `K18` wird im Schriftsatz nie erwähnt, `K23` hat keinen OCR-Text, `K31` enthält ungeschwärzte Drittinformationen.

## Typische Outputs

- Anlagenverzeichnis für Gericht und Kanzleiakte.
- K/B/AST/AG-Nummerierung mit eindeutiger Dateinamenkonvention.
- Konvolutdeckblätter für Sammelanlagen.
- Belegmatrix: Tatsachenbehauptung ↔ Schriftsatzstelle ↔ Anlage ↔ Datei ↔ Status.
- Hash-/Duplikat-/Fassungslog für interne Kontrolle.
- beA-Versandliste mit Paketgrößen, Dateinamen und letzten Prüfpunkten.
- Nachforderungsliste an Mandant oder Sachbearbeitung.
- Berichtigungs- oder Nachreichungsplan nach gerichtlichem Hinweis.

## Wichtig

Anlagen ersetzen keinen Tatsachenvortrag. Wenn eine Behauptung entscheidungserheblich ist, muss sie im Schriftsatz stehen. Die Anlage belegt, erläutert oder vertieft; sie darf nicht der Ort sein, an dem der eigentliche Vortrag versteckt wird.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Besonders wichtige Skills

| Skill | Zweck |
| --- | --- |
| `anlagen-zu-schriftsaetzen-allgemein` | Kaltstart, Triage, Nummernkreis, Ziel-Schriftsatz, K1-Frage und Routing in die passenden Spezial-Skills. |
| `anlagen-zu-schriftsaetzen` | Hauptworkflow für Auto-Benennung, Schriftsatz-folgt-Modus, Prüfmodus und Reparatur nach Hinweis. |
| `k1-sortierwerkstatt` | Baut aus Vertrag, Nachtrag, Mail, Scan und OCR-Fassung eine klare Leit-Anlage `K1` oder ein K1-Konvolut. |
| `schriftsatz-anlagen-mapping` | Verknüpft Tatsachenvortrag, Schriftsatzstelle, Beweisangebot, Anlage und Datei in einer Belegmatrix. |
| `anlagen-duplikate-versionen-hashlog` | Erkennt Dubletten, Versionen, OCR-Kopien und die maßgebliche gerichtliche Fassung. |
| `bea-paketierung-groessen-und-versandplan` | Plant Dateinamen, Paketgrößen, Teilpakete, Begleitvermerk und Eingangskontrolle. |
| `anlagen-qualitygate-finalcheck` | Letzter strenger Check vor Versand: Nummern, Zitate, Dateien, OCR, Schwärzung, Stempel, Paket. |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anlagen-schriftsaetze-start-belegmatrix-fristen`, `anschluss-routing`, `dokumente-intake`, `einstieg-routing`, `kaltstart-triage`, `workflow-kaltstart-und-routing`, `zuordnung-erstpruefung-rollenklaerung-mandatsziel` |
| 2. Unterlagen, Sachverhalt und Quellen | `anlagen-aus-datenraum-und-sharepoint`, `anlagen-elektronische-dokumente-format`, `anlagen-elektronische-dokumente-spezial`, `anlagen-tatbestand-beweis-und-belege`, `anlagenmatrix-csv-xlsx-aufbau`, `baut-beweislast-benennt-bereits-excel`, `baut-beweislast-darlegungslast`, `benennt-compliance-dokumentation-aktenvermerk`, `benennt-compliance-dokumentation-und-akte`, `beweisangebot-anlage-emails-chats-excel`, `beweisangebot-anlage-zeugen`, `chronologie-und-belegmatrix`, `excel-tabellen-und-zahlenbeweis`, `logik-quellenkarte`, `oben-formular-portal-und-einreichung`, `ocr-scan-lesbarkeit-und-beweiswert`, `pruefmodus-fristennotiz-datenraum-sharepoint`, `quellen-livecheck`, ... plus 8 weitere |
| 3. Prüfung, Anspruch und Subsumtion | `anlagen-check-zustellung-redaktion-dsgvo`, `anlagen-prozessual-pruefung-spezial`, `anlagen-quality-check-vor-zustellung`, `fristen-und-risikoampel`, `sortiert-risikoampel-gegenargumente`, `sortiert-risikoampel-und-gegenargumente` |
| 4. Gestaltung, Strategie und Verhandlung | `anlagenband-strukturieren`, `anlagenband-strukturieren-anlagenbezug`, `bea-paketierung-groessen-und-versandplan`, `schriftsatz-verhandlung-vergleich` |
| 5. Verfahren, Behörde und Gericht | `anlagen-bei-eilantrag-eu-arrest`, `anlagen-berufung-revision-eilantrag-eu-bilder`, `anlagenbezug-im-schriftsatz`, `anlagenverzeichnis-gericht-kanzlei-und-intern`, `excel-schriftsatz-brief-und-memo-bausteine`, `frist-eilversand-schiedsverfahren-anlagenband`, `frist-und-eilversand-anlagenpaket`, `gerichtlichen-fristen-form-und-zustaendigkeit`, `gerichtlichen-fristen-form-zustaendigkeit-rechtsweg`, `nachreichung-berichtigung-und-gerichtshinweis`, `pruefmodus-fristennotiz-naechster-schritt`, `schriftsatz-anlagen-mapping`, `word-behoerden-gericht-und-registerweg` |
| 6. Ergebnis, Schreiben und Kommunikation | `anlagen-redaktion-dsgvo-geschgehg`, `arial-mandantenkommunikation-entscheidungsvorlage`, `mandantenkommunikation`, `nachreichung-berichtigung-ocr-scan-original`, `output-waehlen` |
| 7. Kontrolle, Qualität und Gegenprüfung | `anlage-fehlerkatalog`, `anlagen-qualitygate-finalcheck`, `redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `anlage-red-anlagen-anlagenkonvolut-sonderfall`, `anlagen-an-assistenz-uebersetzungspflicht`, `anlagen-aus-edv-systemen`, `anlagen-aus-mandantenmaterial`, `anlagen-bei-berufung-revision`, `anlagen-bilder-screenshots`, `anlagen-duplikate-versionen-hashlog`, `anlagen-format-und-dateinamen`, `anlagen-fuer-bea-versand`, `anlagen-fuer-glaubhaftmachung`, `anlagen-haftpflicht-versicherer`, `anlagen-konvention-k-b-erlaeutert`, `anlagen-konvention-mandantenfreundlich`, `anlagen-konvertierung-zahlen-technische-schwellen`, `anlagen-portal-bea-einreichungslogik`, `anlagen-schriftsaetze-k1-sortierung`, `anlagen-schwaerzen-anonymisieren`, `anlagen-stempel-und-deckblattlogik`, ... plus 34 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 116 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anlage-fehlerkatalog` | Wenn es um Anlage Fehlerkatalog in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlage-red-anlagen-anlagenkonvolut-sonderfall` | Wenn es um Anlage: Red-Team und Qualitätskontrolle in Anlagen zu Schriftsätzen geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-an-assistenz-uebersetzungspflicht` | Wenn es um Übergabe an Assistenz und Legal Tech in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfr... |
| `anlagen-aus-datenraum-und-sharepoint` | Wenn es um Datenraum und SharePoint als Anlagenquelle in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und n... |
| `anlagen-aus-edv-systemen` | Wenn es um Anlagen aus IT-Systemen in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `anlagen-aus-mandantenmaterial` | Wenn es um Anlagen aus Mandantenmaterial in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-bei-berufung-revision` | Wenn es um Anlagen in Berufung/Revision in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-bei-eilantrag-eu-arrest` | Wenn es um Anlagen bei Eilantrag und Arrest in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anlagen-berufung-revision-eilantrag-eu-bilder` | Wenn es um Anlagen in Berufung/Revision in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anlagen-bilder-screenshots` | Wenn es um Bilder/Screenshots als Anlagen in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-check-zustellung-redaktion-dsgvo` | Wenn es um Anlagen: Quality-Check vor Zustellung in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Aus... |
| `anlagen-duplikate-versionen-hashlog` | Wenn es um Duplikate, Fassungen und Hashlog in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `anlagen-elektronische-dokumente-format` | Wenn es um Anlagen: elektronische Dokumente in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. Auswahlstich... |
| `anlagen-elektronische-dokumente-spezial` | Wenn es um Anlagen: elektronische Dokumente in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. Auswahlstich... |
| `anlagen-format-und-dateinamen` | Wenn es um Anlagen: Format und Dateinamen in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-fuer-bea-versand` | Wenn es um Anlagen für beA-Versand in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-fuer-glaubhaftmachung` | Wenn es um Anlagen für Glaubhaftmachung in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `anlagen-haftpflicht-versicherer` | Wenn es um Anlagen für Haftpflichtversicherer in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Anlagen Haftpfl... |
| `anlagen-konvention-k-b-erlaeutert` | Wenn es um K/B-Konvention erläutert in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `anlagen-konvention-mandantenfreundlich` | Wenn es um Anlagen: Konvention mandantenfreundlich in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-konvertierung-zahlen-technische-schwellen` | Wenn es um Konvertierung, Zahlen und technische Schwellen in Anlagen zu Schriftsätzen geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. Aus... |
| `anlagen-portal-bea-einreichungslogik` | Wenn es um Portal, beA und Einreichungslogik in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-prozessual-pruefung-spezial` | Wenn es um Anlagen: Substantiierung BGH in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anlagen-quality-check-vor-zustellung` | Wenn es um Anlagen: Quality-Check vor Zustellung in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Aus... |
| `anlagen-qualitygate-finalcheck` | Wenn es um Anlagen-Qualitygate vor Versand in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `anlagen-redaktion-dsgvo-geschgehg` | Wenn es um Redaktion, DSGVO und Geschäftsgeheimnisse in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-schriftsaetze-k1-sortierung` | Wenn es um Dokumentenmatrix und Lückenliste in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahls... |
| `anlagen-schriftsaetze-start-belegmatrix-fristen` | Wenn es um Anlagen zu Schriftsätzen — Allgemein in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `anlagen-schwaerzen-anonymisieren` | Wenn es um Anlagen schwaerzen/anonymisieren in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sc... |
| `anlagen-stempel-und-deckblattlogik` | Wenn es um Stempel- und Deckblattlogik in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `anlagen-stempelbild-entscheidungsvorlage` | Wenn es um Stempelbild und Entscheidungsvorlage in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-tatbestand-beweis-und-belege` | Wenn es um Anlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `anlagen-uebergabe-an-assistenz-und-legal-tech` | Wenn es um Übergabe an Assistenz und Legal Tech in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfr... |
| `anlagen-uebersetzungspflicht` | Wenn es um Fremdsprachige Anlagen in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anlagen-vorlagepflicht-141-zpo` | Wenn es um Urkundenvorlage Paragrafen 142. 421 ZPO in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `anlagen-zu-schriftsaetzen` | Wenn es um Anlagen zu Schriftsaetzen bauen in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anlagen-zur-substantiierung-pflicht` | Wenn es um Anlagen vs. Substantiierungspflicht in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `anlagenband-strukturieren` | Wenn es um Anlagenband strukturieren in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwor... |
| `anlagenband-strukturieren-anlagenbezug` | Wenn es um Anlagenband strukturieren in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwor... |
| `anlagenbezug-im-schriftsatz` | Wenn es um Anlagenbezug im Schriftsatz in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anlagenkonvolut-konsolidieren` | Wenn es um Anlagenkonvolut konsolidieren in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anlagenkonvolut-sonderfall-edge-case` | Wenn es um Anlagenkonvolut: Sonderfall und Edge-Case-Prüfung in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `anlagenkonvolut-sonderfall-und-edge-case` | Wenn es um Anlagenkonvolut: Sonderfall und Edge-Case-Prüfung in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `anlagenmatrix-csv-xlsx-aufbau` | Wenn es um Anlagenmatrix CSV/XLSX Aufbau in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anlagenverzeichnis-gericht-kanzlei-und-intern` | Wenn es um Anlagenverzeichnis für Gericht, Kanzlei und intern in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risik... |
| `anlagenverzeichnis-grundaufbau` | Wenn es um Anlagenverzeichnis-Grundaufbau in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anlagenverzeichnis-kanzlei-grundaufbau-bea` | Wenn es um Anlagenverzeichnis für Gericht, Kanzlei und intern in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risik... |
| `anschluss-routing` | Wenn es um Anschluss-Routing in Anlagen zu Schriftsätzen geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arial-mandantenkommunikation-entscheidungsvorlage` | Wenn es um Stempelbild und Entscheidungsvorlage in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `baut-beweislast-benennt-bereits-excel` | Wenn es um Beweislast, Darlegungslast und Anlagen in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. Auswahlstichwort: Baut Beweislast Benennt Be... |
| `baut-beweislast-darlegungslast` | Wenn es um Beweislast, Darlegungslast und Anlagen in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. Auswahlstichwort: Baut Beweislast Darlegungs... |
| `bea-paketierung-groessen-und-versandplan` | Wenn es um beA-Paketierung und Versandplan in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sch... |
| `benennt-compliance-dokumentation-aktenvermerk` | Wenn es um Benennt: Compliance-Dokumentation und Aktenvermerk in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `benennt-compliance-dokumentation-und-akte` | Wenn es um Benennt: Compliance-Dokumentation und Aktenvermerk in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sch... |
| `bereits-abschlussprodukt-uebergabe` | Wenn es um Bereits: Abschlussprodukt und Übergabe in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Bereits Abs... |
| `bereits-abschlussprodukt-und-uebergabe` | Wenn es um Bereits: Abschlussprodukt und Übergabe in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Bereits Abs... |
| `berufung-beschwerde-und-neue-anlagen` | Wenn es um Berufung, Beschwerde und neue Anlagen in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisf... |
| `beweisangebot-anlage-emails-chats-excel` | Wenn es um Beweisangebot über Anlagen (Zeugen) in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beweisangebot-anlage-zeugen` | Wenn es um Beweisangebot über Anlagen (Zeugen) in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `dokumente-intake` | Wenn es um Dokumentenintake in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einstieg-routing` | Wenn es um Einstieg und Routing in Anlagen zu Schriftsätzen geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `emails-chats-screenshots-als-anlagen` | Wenn es um E-Mails, Chats und Screenshots als Anlagen in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `excel` | Wenn es um Excel-Anlagen und Zahlenbausteine in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahl... |
| `excel-schriftsatz-brief-und-memo-bausteine` | Wenn es um Excel-Anlagen und Zahlenbausteine in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahl... |
| `excel-tabellen-und-zahlenbeweis` | Wenn es um Excel-Tabellen und Zahlenbeweis in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `fremdsprachige-anlagen-uebersetzung` | Wenn es um Fremdsprachige Anlagen und Übersetzung in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `frist-eilversand-schiedsverfahren-anlagenband` | Wenn es um Frist, Eilversand und Anlagenband im Schiedsverfahren in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `frist-und-eilversand-anlagenpaket` | Wenn es um Frist und Eilversand Anlagenpaket in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `gerichtlichen-fristen-form-und-zustaendigkeit` | Wenn es um Gerichtlichen: Fristen, Form, Zuständigkeit und Rechtsweg in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlsti... |
| `gerichtlichen-fristen-form-zustaendigkeit-rechtsweg` | Wenn es um Gerichtlichen: Fristen, Form, Zuständigkeit und Rechtsweg in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlsti... |
| `haftpflicht-versicherer-konvention-k` | Wenn es um Anlagen für Haftpflichtversicherer in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Haftpflicht Ver... |
| `k1-anlagenpaket-aus-chaosordner` | Wenn es um K1 aus Chaosordner bauen in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. A... |
| `k1-anlagenpaket-k1-sortierwerkstatt` | Wenn es um K1 aus Chaosordner bauen in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. A... |
| `k1-sortierwerkstatt` | Wenn es um K1-Sortierwerkstatt in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `kaltstart-triage` | Wenn es um Kaltstart Triage in Anlagen zu Schriftsätzen geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `konform-interessen` | Wenn es um Konform: Mehrparteienkonflikt und Interessenmatrix in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `konform-interessen-konvertiert-oben` | Wenn es um Konform: Mehrparteienkonflikt und Interessenmatrix in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `konvertiert-zahlen-schwellen-und-berechnung` | Wenn es um Konvertierung, Zahlen und technische Schwellen in Anlagen zu Schriftsätzen geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. Aus... |
| `logik-quellenkarte` | Wenn es um Logik Quellenkarte in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `mandantenkommunikation` | Wenn es um Mandantenkommunikation in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `massenanlagen-sampling-repraesentativitaet` | Wenn es um Massenanlagen, Sampling und Repräsentativität in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. Auswahlstichwort: Massenanlagen Sampl... |
| `massenanlagen-sampling-und-repraesentativitaet` | Wenn es um Massenanlagen, Sampling und Repräsentativität in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. Auswahlstichwort: Massenanlagen Sampl... |
| `mehrparteien-rollen-und-praefixe` | Wenn es um Mehrparteien, Rollen und Präfixe in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `nachreichung-berichtigung-ocr-scan-original` | Wenn es um Nachreichung, Berichtigung und gerichtlicher Hinweis in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweisch... |
| `nachreichung-berichtigung-und-gerichtshinweis` | Wenn es um Nachreichung, Berichtigung und gerichtlicher Hinweis in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweisch... |
| `oben-formular-portal-und-einreichung` | Wenn es um Portal, beA und Einreichungslogik in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `ocr-scan-lesbarkeit-und-beweiswert` | Wenn es um OCR, Scanqualität und Lesbarkeit in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `original-abschrift-kopie-elektronische` | Wenn es um Original, Abschrift, Kopie und elektronische Fassung in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem S... |
| `original-abschrift-kopie-und-elektronische-fassung` | Wenn es um Original, Abschrift, Kopie und elektronische Fassung in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem S... |
| `output-waehlen` | Wenn es um Output wählen in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pruefmodus-fristennotiz-datenraum-sharepoint` | Wenn es um Prüfmodus, Fristennotiz und nächster Schritt in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Pruef... |
| `pruefmodus-fristennotiz-naechster-schritt` | Wenn es um Prüfmodus, Fristennotiz und nächster Schritt in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Pruef... |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `redteam-qualitygate` | Wenn es um Red-Team Qualitygate in Anlagen zu Schriftsätzen geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schiedsverfahren-anlagenband-und-datentraeger` | Wenn es um Schiedsverfahren: Anlagenband und Datenträger in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| `schriftsaetzen` | Wenn es um Zuordnung von Anlagen zu gerichtlichen Schriftsätzen in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und An... |
| `schriftsaetzen-dokumentenmatrix-und-lueckenliste` | Wenn es um Dokumentenmatrix und Lückenliste in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahls... |
| `schriftsatz-anlagen-mapping` | Wenn es um Schriftsatz-Anlagen-Mapping in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schriftsatz-verhandlung-vergleich` | Wenn es um Schriftsatz: Verhandlung, Vergleich und Eskalation in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sortiert-risikoampel-gegenargumente` | Wenn es um Sortiert: Risikoampel, Gegenargumente und Verteidigungslinien in Anlagen zu Schriftsätzen geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. A... |
| `sortiert-risikoampel-und-gegenargumente` | Wenn es um Sortiert: Risikoampel, Gegenargumente und Verteidigungslinien in Anlagen zu Schriftsätzen geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. A... |
| `sortiert-stempelt-word` | Wenn es um Schriftsatz: Verhandlung, Vergleich und Eskalation in Anlagen zu Schriftsätzen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anla... |
| `spezial-logik-livequellen-und-rechtsprechungscheck` | Wenn es um Logik: Livequellen- und Rechtsprechungscheck in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stempelt-internationaler-bezug-schnittstellen` | Wenn es um Stempelt: Internationaler Bezug und Schnittstellen in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `stempelt-internationaler-bezug-und-schnittstellen` | Wenn es um Stempelt: Internationaler Bezug und Schnittstellen in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort:... |
| `tatbestandsmerkmale-beweisfragen-beleglage` | Wenn es um Anlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `word` | Wenn es um Word/PDF-Umwandlung für Gericht und Behörden in Anlagen zu Schriftsätzen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `word-behoerden-gericht-und-registerweg` | Wenn es um Word/PDF-Umwandlung für Gericht und Behörden in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in Anlagen zu Schriftsätzen geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `zeitleiste-und-belegkette` | Wenn es um Zeitleiste und Belegkette in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `zuordnung-erstpruefung-rollenklaerung-mandatsziel` | Wenn es um Zuordnung: Erstprüfung, Rollenklärung und Mandatsziel in Anlagen zu Schriftsätzen geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zuordnung-zeitleiste-belegkette` | Wenn es um Zuordnung: Erstprüfung, Rollenklärung und Mandatsziel in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

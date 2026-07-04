# Vertragsausfüller

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`vertragsausfueller`) | [`vertragsausfueller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsausfueller.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Vertragsausfueller - BSAG Kiosk Huckelriede** (`vertragsausfueller-bsag-kiosk-huckelriede`) | [Gesamt-PDF lesen](../testakten/vertragsausfueller-bsag-kiosk-huckelriede/gesamt-pdf/vertragsausfueller-bsag-kiosk-huckelriede_gesamt.pdf) | [`testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`vertragsausfueller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsausfueller.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vertragsausfueller/vertragsausfueller-werkstatt.md" download><code>vertragsausfueller-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vertragsausfueller/vertragsausfueller-schnellstart.md" download><code>vertragsausfueller-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Akte Vertragsausfueller - BSAG Kiosk Huckelriede: [Gesamt-PDF](../testakten/vertragsausfueller-bsag-kiosk-huckelriede/gesamt-pdf/vertragsausfueller-bsag-kiosk-huckelriede_gesamt.pdf), [`testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip), [`testakte-vertragsausfueller-bsag-kiosk-huckelriede-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vertragsausfueller-bsag-kiosk-huckelriede-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Freistehendes Cowork-Plugin für workflowgestütztes Ausfüllen von Vertragsvorlagen und Altverträgen. Ein Nutzer lädt eine Word-Vorlage, einen alten Vertrag, ein Term Sheet oder Freitextdaten hoch. Das Plugin strippt das Dokument, erkennt Felder und Klauseln, fragt fehlende Daten ab, mappt Term-Sheet-Daten auf Vertragsfelder und erstellt daraus einen neuen Vertragsentwurf.

Der BSAG-Mietvertrag und das Term Sheet Kiosk Huckelriede sind als Beispielakte eingebunden.

## Installation

1. Plugin-Umgebung öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `vertragsausfueller.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Fülle diesen Mietvertrag mit den Daten aus dem Term Sheet aus.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install vertragsausfueller@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/` und `assets/` enthalten.

## Workflow

1. Vorlage oder alten Vertrag hochladen.
2. Dokument strippen: Absätze, Tabellen, Platzhalter, Klauseln, Anlagen und Signaturen erkennen.
3. Term Sheet, E-Mail oder Freitextdaten danebenlegen.
4. Feldinventar und Mapping erzeugen.
5. Fehlende Daten freundlich abfragen oder als offene Platzhalter markieren.
6. Clean-Vertrag erstellen.
7. Nur auf ausdrückliche Nachfrage zusätzlich Track Changes oder Redline vorbereiten.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| vaf-kommandocenter | steuert den gesamten Workflow von Upload bis neuem Vertragsentwurf. |
| vaf-docx-stripper | macht aus Word-Dokumenten ein bearbeitbares Vertragsmodell. |
| vaf-template-erkennung | klassifiziert den Vertrag und trennt Fixtext von Variablen. |
| vaf-feldinventar | baut die zentrale Datenmatrix für den Vertrag. |
| vaf-termsheet-mapping | überführt wirtschaftliche Eckdaten in Vertragsklauseln. |
| vaf-rueckfrageninterview | füllt Datenlücken ohne den Nutzer zu überfordern. |
| vaf-bsag-mietvertrag | setzt den Huckelriede-Term-Sheet-Fall in die BSAG-Vorlage um. |
| vaf-klauselentscheidung | verhindert stilles Auswählen riskanter Optionen. |
| vaf-plausibilitaetscheck | härtet den Entwurf vor Versand oder Verhandlung. |
| vaf-clean-output | liefert den ersten belastbaren Vertragsentwurf. |
| vaf-track-changes-nur-nach-frage | setzt die ausdrückliche Nachfragepflicht durch. |
| vaf-redline-qa | kontrolliert Änderungsfassungen vor Herausgabe. |
| vaf-altvertrag-nachziehen | macht aus alten Verträgen neue Entwürfe. |
| vaf-quality-gate | ist die letzte Schleuse vor Vertragserzeugung. |

## BSAG-Beispiel

Die Beispielakte enthält die Word-Vorlage `BSAG-Mietvertrag-Vorlage.docx` und das Term Sheet `BSAG-TermSheet-Kiosk-Huckelriede - Kopie.docx`. Der Spezialskill `vaf-bsag-mietvertrag` mappt daraus insbesondere Mieter, Mietobjekt, Nutzung, Fläche, Miete, Nebenkosten, Kaution, Mietbeginn, Laufzeit, Optionen, Indexierung, Umsatzsteuer, Öffnungszeiten, Konkurrenzschutz, Sortiment, Fettabscheider, Werbung und Versicherung.

## Track-Changes-Regel

Das Plugin erzeugt keine Track-Changes- oder Redline-Fassung stillschweigend. Es fragt immer ausdrücklich: Soll zusätzlich eine Track-Changes- oder Redline-Fassung erstellt werden? Ohne Bestätigung bleibt es bei Clean-Entwurf, Änderungslog und Ausfüllprotokoll.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anschluss-routing`, `dokumente-intake`, `einstieg-routing`, `start-chronologie-fristen`, `vertragsausfueller-erstpruefung-und-mandatsziel`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `altvertraege-dokumentenmatrix-und-lueckenliste`, `changes-beweislast-docx-erkennen`, `docx-tatbestand-beweis-und-belege`, `quellen-livecheck`, `rueckfragen-compliance-dokumentation-und-akte`, `sheets-quellenkarte`, `spezial-sheets-livequellen-und-rechtsprechungscheck`, `spezial-vertraege-formular-portal-und-einreichung`, `unterlagen-luecken`, `vertraege-formular-portal-und-einreichung`, `workflow-chronologie-und-belegmatrix`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `plausibilitaetscheck-termsheet`, `strippen-risikoampel-und-gegenargumente`, `workflow-fristen-und-risikoampel` |
| 4. Gestaltung, Strategie und Verhandlung | `altvertrag-nachziehen`, `bsag-mietvertrag-klauselentscheidung`, `klauselentscheidung`, `konzern-rahmenvertrag-anpassen`, `vorlagen-vertragsausfueller-vaf-altvertrag` |
| 5. Verfahren, Behörde und Gericht | `ausdruecklicher-fristennotiz-und-naechster-schritt`, `erkennen-schriftsatz-brief-und-memo-bausteine`, `felder-behoerden-gericht-und-registerweg` |
| 6. Ergebnis, Schreiben und Kommunikation | `clean-output`, `output-waehlen`, `track-mandantenkommunikation-entscheidungsvorlage` |
| 7. Kontrolle, Qualität und Gegenprüfung | `mandantenkommunikation-redteam-qualitygate`, `workflow-redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `batch-modus-docx-stripper-einfuehrung`, `docx-stripper`, `einfuehrung-prozess`, `erzeugen-red-fassungen-sonderfall-felder`, `fassungen-sonderfall-und-edge-case`, `feldinventar-fragebogen-input`, `fragebogen-input-leitfaden`, `fremdsprachige-vertraege-bilingual`, `fuehren-interessen-mappen-nachfrage`, `kommandocenter-mehrsprachige-vertraege`, `mappen-zahlen-schwellen-und-berechnung`, `mehrsprachige-vertraege-spezial`, `nachfrage-abschlussprodukt-und-uebergabe`, `neue-rueckfragen-strippen`, `platzhalterlogik-bauleiter`, `quality-gate-redline-qa`, `redline-qa`, `rueckfrageninterview`, ... plus 8 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `altvertraege-dokumentenmatrix-und-lueckenliste` | Wenn es um Altvertraege: Dokumentenmatrix, Lückenliste und Nachforderung in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `altvertrag-nachziehen` | Wenn es um Altvertrag nachziehen in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anschluss-routing` | Wenn es um Anschluss-Routing in Vertragsausfüller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausdruecklicher-fristennotiz-und-naechster-schritt` | Wenn es um Ausdruecklicher: Fristennotiz und nächster Schritt in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `batch-modus-docx-stripper-einfuehrung` | Wenn es um VAF: Batch-Modus Konzern in Vertragsausfüller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `bsag-mietvertrag-klauselentscheidung` | Wenn es um BSAG-Mietvertrag in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `changes-beweislast-docx-erkennen` | Wenn es um Changes: Beweislast, Darlegungslast und Substantiierung in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `clean-output` | Wenn es um Clean-Output in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `docx-stripper` | Wenn es um DOCX-Stripper in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `docx-tatbestand-beweis-und-belege` | Wenn es um Docx: Tatbestandsmerkmale, Beweisfragen und Beleglage in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `dokumente-intake` | Wenn es um Dokumentenintake in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einfuehrung-prozess` | Wenn es um VAF: Prozess einfuehrend in Vertragsausfüller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `einstieg-routing` | Wenn es um Einstieg und Routing in Vertragsausfüller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erkennen-schriftsatz-brief-und-memo-bausteine` | Wenn es um Erkennen: Schriftsatz-, Brief- und Memo-Bausteine in Vertragsausfüller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `erzeugen-red-fassungen-sonderfall-felder` | Wenn es um Erzeugen: Red-Team und Qualitätskontrolle in Vertragsausfüller geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fassungen-sonderfall-und-edge-case` | Wenn es um Fassungen: Sonderfall und Edge-Case-Prüfung in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `felder-behoerden-gericht-und-registerweg` | Wenn es um Felder: Behörden-, Gerichts- oder Registerweg in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `feldinventar-fragebogen-input` | Wenn es um Feldinventar in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fragebogen-input-leitfaden` | Wenn es um VAF: Fragebogen-Input in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fremdsprachige-vertraege-bilingual` | Wenn es um Bilinguale Verträge in Vertragsausfüller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `fuehren-interessen-mappen-nachfrage` | Wenn es um Fuehren: Mehrparteienkonflikt und Interessenmatrix in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `klauselentscheidung` | Wenn es um Klauselentscheidungen in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kommandocenter-mehrsprachige-vertraege` | Wenn es um Kommandocenter in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `konzern-rahmenvertrag-anpassen` | Wenn es um Rahmenvertrag-Anpassung in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mandantenkommunikation-redteam-qualitygate` | Wenn es um Mandantenkommunikation in Vertragsausfüller geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `mappen-zahlen-schwellen-und-berechnung` | Wenn es um Mappen: Zahlen, Schwellenwerte und Berechnung in Vertragsausfüller geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `mehrsprachige-vertraege-spezial` | Wenn es um VAF: Mehrsprachige Verträge in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `nachfrage-abschlussprodukt-und-uebergabe` | Wenn es um Nachfrage: Abschlussprodukt und Übergabe in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `neue-rueckfragen-strippen` | Wenn es um Neue: Internationaler Bezug und Schnittstellen in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `output-waehlen` | Wenn es um Output wählen in Vertragsausfüller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `platzhalterlogik-bauleiter` | Wenn es um VAF: Platzhalterlogik Bauleiter in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `plausibilitaetscheck-termsheet` | Wenn es um Plausibilitätscheck in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `quality-gate-redline-qa` | Wenn es um Quality Gate — Vertragsausfueller in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `redline-qa` | Wenn es um Redline-QA in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rueckfragen-compliance-dokumentation-und-akte` | Wenn es um Rueckfragen: Compliance-Dokumentation und Aktenvermerk in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `rueckfrageninterview` | Wenn es um Rückfrageninterview in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sheets-quellenkarte` | Wenn es um Sheets Quellenkarte in Vertragsausfüller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `spezial-sheets-livequellen-und-rechtsprechungscheck` | Wenn es um Sheets: Livequellen- und Rechtsprechungscheck in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-vertraege-formular-portal-und-einreichung` | Wenn es um Vertraege: Formular, Portal und Einreichungslogik in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `start-chronologie-fristen` | Wenn es um Vertragsausfueller — Allgemein in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `strippen-risikoampel-und-gegenargumente` | Wenn es um Strippen: Risikoampel, Gegenargumente und Verteidigungslinien in Vertragsausfüller geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `template-erkennung-format-track-changes` | Wenn es um Template-Erkennung in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `template-format-und-source` | Wenn es um VAF: Template-Format und Quelle in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `term-track-vertraege` | Wenn es um Term: Verhandlung, Vergleich und Eskalation in Vertragsausfüller geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `termsheet-mapping` | Wenn es um Term-Sheet-Mapping in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `track-changes-nur-nach-frage` | Wenn es um Track Changes nur nach Frage in Vertragsausfüller geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `track-mandantenkommunikation-entscheidungsvorlage` | Wenn es um Track: Mandantenkommunikation und Entscheidungsvorlage in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vaf-fremdsprachige-vertraege-bilingual` | Wenn es um Bilinguale Vertraege in Vertragsausfüller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `vaf-mehrsprachige-vertraege-spezial` | Wenn es um VAF: Mehrsprachige Vertraege in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vaf-versionierung-aenderungsverfolgung-spezial` | Wenn es um Vaf Versionierung Aenderungsverfolgung Spezial in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `vertraege-formular-portal-und-einreichung` | Wenn es um Verträge: Formular, Portal und Einreichungslogik in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vertragsausfueller-erstpruefung-und-mandatsziel` | Wenn es um Vertragsausfueller: Erstprüfung, Rollenklärung und Mandatsziel in Vertragsausfüller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vorlagen-vertragsausfueller-vaf-altvertrag` | Wenn es um Vorlagen: Fristen, Form, Zuständigkeit und Rechtsweg in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `workflow-fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in Vertragsausfüller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-redteam-qualitygate` | Wenn es um Red-Team Qualitygate in Vertragsausfüller geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

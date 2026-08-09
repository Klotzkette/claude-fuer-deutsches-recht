# Vertragsausfüller

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/vertragsausfueller.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill aus der Skill-Liste wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart als Markdown laden und zusammen mit den Unterlagen öffnen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Vertragsausfüller:

> Lies zuerst alle Dateien im ausgewählten Ordner. Bearbeite den Vorgang mit diesem Fachgebiet und liefere als Erstes Vertragsgerüst: Präambel, Definitionen, Leistung, Vergütung, Laufzeit, Haftung, Geheimhaltung, Schlussbestimmungen. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`vertragsausfueller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsausfueller.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vertragsausfueller/vertragsausfueller-schnellstart.md" download><code>vertragsausfueller-schnellstart.md</code></a> |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vertragsausfueller/vertragsausfueller-werkstatt.md" download><code>vertragsausfueller-werkstatt.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Akte Vertragsausfüller - BSAG Kiosk Huckelriede](../testakten/vertragsausfueller-bsag-kiosk-huckelriede/README.md) | [Gesamt-PDF](../testakten/vertragsausfueller-bsag-kiosk-huckelriede/gesamt-pdf/vertragsausfueller-bsag-kiosk-huckelriede_gesamt.pdf) | [`testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip) | [`testakte-vertragsausfueller-bsag-kiosk-huckelriede-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vertragsausfueller-bsag-kiosk-huckelriede-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
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
| kommandocenter-mehrsprachige-vertraege | steuert den gesamten Workflow von den Unterlagen bis zum neuen Vertragsentwurf. |
| docx-stripper | macht aus Word-Dokumenten ein bearbeitbares Vertragsmodell. |
| template-erkennung-format-track-changes | klassifiziert den Vertrag und trennt Fixtext von Variablen. |
| feldinventar-fragebogen-input | baut die zentrale Datenmatrix für den Vertrag. |
| termsheet-mapping | überführt wirtschaftliche Eckdaten in Vertragsklauseln. |
| rueckfrageninterview | füllt nur entscheidungserhebliche Datenlücken. |
| bsag-mietvertrag-klauselentscheidung | setzt den Huckelriede-Fall in die BSAG-Vorlage um. |
| klauselentscheidung | verhindert stilles Auswählen riskanter Optionen. |
| plausibilitaetscheck-termsheet | härtet den Entwurf vor Versand oder Verhandlung. |
| clean-output | liefert den ersten belastbaren Vertragsentwurf. |
| track-changes-nur-nach-frage | setzt die ausdrückliche Nachfragepflicht durch. |
| redline-qa | kontrolliert Änderungsfassungen vor Herausgabe. |
| altvertrag-nachziehen | macht aus alten Verträgen neue Entwürfe. |
| quality-gate-redline-qa | ist die letzte Kontrolle vor Vertragserzeugung. |

## BSAG-Beispiel

Die Beispielakte enthält die Word-Vorlage `BSAG-Mietvertrag-Vorlage.docx` und das Term Sheet `BSAG-TermSheet-Kiosk-Huckelriede - Kopie.docx`. Der Spezialskill `bsag-mietvertrag-klauselentscheidung` ordnet daraus insbesondere Mieter, Mietobjekt, Nutzung, Fläche, Miete, Nebenkosten, Kaution, Mietbeginn, Laufzeit, Optionen, Indexierung, Umsatzsteuer, Öffnungszeiten, Konkurrenzschutz, Sortiment, Fettabscheider, Werbung und Versicherung zu.

## Track-Changes-Regel

Das Plugin erzeugt keine Track-Changes- oder Redline-Fassung stillschweigend. Es fragt immer ausdrücklich: Soll zusätzlich eine Track-Changes- oder Redline-Fassung erstellt werden? Ohne Bestätigung bleibt es bei Clean-Entwurf, Änderungslog und Ausfüllprotokoll.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md), [`vertragsausfueller-erstpruefung-und-mandatsziel`](skills/vertragsausfueller-erstpruefung-und-mandatsziel/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`altvertraege-dokumentenmatrix-und-lueckenliste`](skills/altvertraege-dokumentenmatrix-und-lueckenliste/SKILL.md), [`changes-beweislast-docx-erkennen`](skills/changes-beweislast-docx-erkennen/SKILL.md), [`docx-tatbestand-beweis-und-belege`](skills/docx-tatbestand-beweis-und-belege/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`rueckfragen-compliance-dokumentation-und-akte`](skills/rueckfragen-compliance-dokumentation-und-akte/SKILL.md), [`sheets-quellenkarte`](skills/sheets-quellenkarte/SKILL.md), [`spezial-sheets-livequellen-und-rechtsprechungscheck`](skills/spezial-sheets-livequellen-und-rechtsprechungscheck/SKILL.md), [`spezial-vertraege-formular-portal-und-einreichung`](skills/spezial-vertraege-formular-portal-und-einreichung/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`vertraege-formular-portal-und-einreichung`](skills/vertraege-formular-portal-und-einreichung/SKILL.md), [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`plausibilitaetscheck-termsheet`](skills/plausibilitaetscheck-termsheet/SKILL.md), [`strippen-risikoampel-und-gegenargumente`](skills/strippen-risikoampel-und-gegenargumente/SKILL.md), [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`altvertrag-nachziehen`](skills/altvertrag-nachziehen/SKILL.md), [`bsag-mietvertrag-klauselentscheidung`](skills/bsag-mietvertrag-klauselentscheidung/SKILL.md), [`klauselentscheidung`](skills/klauselentscheidung/SKILL.md), [`konzern-rahmenvertrag-anpassen`](skills/konzern-rahmenvertrag-anpassen/SKILL.md), [`vorlagen-vertragsausfueller-vaf-altvertrag`](skills/vorlagen-vertragsausfueller-vaf-altvertrag/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`ausdruecklicher-fristennotiz-und-naechster-schritt`](skills/ausdruecklicher-fristennotiz-und-naechster-schritt/SKILL.md), [`erkennen-schriftsatz-brief-und-memo-bausteine`](skills/erkennen-schriftsatz-brief-und-memo-bausteine/SKILL.md), [`felder-behoerden-gericht-und-registerweg`](skills/felder-behoerden-gericht-und-registerweg/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`clean-output`](skills/clean-output/SKILL.md), [`output-waehlen`](skills/output-waehlen/SKILL.md), [`track-mandantenkommunikation-entscheidungsvorlage`](skills/track-mandantenkommunikation-entscheidungsvorlage/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`mandantenkommunikation-redteam-qualitygate`](skills/mandantenkommunikation-redteam-qualitygate/SKILL.md), [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`batch-modus-docx-stripper-einfuehrung`](skills/batch-modus-docx-stripper-einfuehrung/SKILL.md), [`docx-stripper`](skills/docx-stripper/SKILL.md), [`einfuehrung-prozess`](skills/einfuehrung-prozess/SKILL.md), [`erzeugen-red-fassungen-sonderfall-felder`](skills/erzeugen-red-fassungen-sonderfall-felder/SKILL.md), [`fassungen-sonderfall-und-edge-case`](skills/fassungen-sonderfall-und-edge-case/SKILL.md), [`feldinventar-fragebogen-input`](skills/feldinventar-fragebogen-input/SKILL.md), [`fragebogen-input-leitfaden`](skills/fragebogen-input-leitfaden/SKILL.md), [`fremdsprachige-vertraege-bilingual`](skills/fremdsprachige-vertraege-bilingual/SKILL.md), [`fuehren-interessen-mappen-nachfrage`](skills/fuehren-interessen-mappen-nachfrage/SKILL.md), [`kommandocenter-mehrsprachige-vertraege`](skills/kommandocenter-mehrsprachige-vertraege/SKILL.md), [`mappen-zahlen-schwellen-und-berechnung`](skills/mappen-zahlen-schwellen-und-berechnung/SKILL.md), [`mehrsprachige-vertraege-spezial`](skills/mehrsprachige-vertraege-spezial/SKILL.md), [`nachfrage-abschlussprodukt-und-uebergabe`](skills/nachfrage-abschlussprodukt-und-uebergabe/SKILL.md), [`neue-rueckfragen-strippen`](skills/neue-rueckfragen-strippen/SKILL.md), [`platzhalterlogik-bauleiter`](skills/platzhalterlogik-bauleiter/SKILL.md), [`quality-gate-redline-qa`](skills/quality-gate-redline-qa/SKILL.md), [`redline-qa`](skills/redline-qa/SKILL.md), [`rueckfrageninterview`](skills/rueckfrageninterview/SKILL.md), ... plus 8 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 61 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`altvertraege-dokumentenmatrix-und-lueckenliste`](skills/altvertraege-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Altvertraege: Dokumentenmatrix, Lückenliste und Nachforderung in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`altvertrag-nachziehen`](skills/altvertrag-nachziehen/SKILL.md) | Wenn es um Altvertrag nachziehen in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in Vertragsausfüller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ausdruecklicher-fristennotiz-und-naechster-schritt`](skills/ausdruecklicher-fristennotiz-und-naechster-schritt/SKILL.md) | Wenn es um Ausdruecklicher: Fristennotiz und nächster Schritt in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`batch-modus-docx-stripper-einfuehrung`](skills/batch-modus-docx-stripper-einfuehrung/SKILL.md) | Wenn es um VAF: Batch-Modus Konzern in Vertragsausfüller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`bsag-mietvertrag-klauselentscheidung`](skills/bsag-mietvertrag-klauselentscheidung/SKILL.md) | Wenn es um BSAG-Mietvertrag in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`changes-beweislast-docx-erkennen`](skills/changes-beweislast-docx-erkennen/SKILL.md) | Wenn es um Changes: Beweislast, Darlegungslast und Substantiierung in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`clean-output`](skills/clean-output/SKILL.md) | Wenn es um Clean-Output in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`docx-stripper`](skills/docx-stripper/SKILL.md) | Wenn es um DOCX-Stripper in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`docx-tatbestand-beweis-und-belege`](skills/docx-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Docx: Tatbestandsmerkmale, Beweisfragen und Beleglage in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einfuehrung-prozess`](skills/einfuehrung-prozess/SKILL.md) | Wenn es um VAF: Prozess einfuehrend in Vertragsausfüller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Vertragsausfüller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`erkennen-schriftsatz-brief-und-memo-bausteine`](skills/erkennen-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Wenn es um Erkennen: Schriftsatz-, Brief- und Memo-Bausteine in Vertragsausfüller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`erzeugen-red-fassungen-sonderfall-felder`](skills/erzeugen-red-fassungen-sonderfall-felder/SKILL.md) | Wenn es um Erzeugen: Red-Team und Qualitätskontrolle in Vertragsausfüller geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fassungen-sonderfall-und-edge-case`](skills/fassungen-sonderfall-und-edge-case/SKILL.md) | Wenn es um Fassungen: Sonderfall und Edge-Case-Prüfung in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`felder-behoerden-gericht-und-registerweg`](skills/felder-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Felder: Behörden-, Gerichts- oder Registerweg in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`feldinventar-fragebogen-input`](skills/feldinventar-fragebogen-input/SKILL.md) | Wenn es um Feldinventar in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fragebogen-input-leitfaden`](skills/fragebogen-input-leitfaden/SKILL.md) | Wenn es um VAF: Fragebogen-Input in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fremdsprachige-vertraege-bilingual`](skills/fremdsprachige-vertraege-bilingual/SKILL.md) | Wenn es um Bilinguale Verträge in Vertragsausfüller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`fuehren-interessen-mappen-nachfrage`](skills/fuehren-interessen-mappen-nachfrage/SKILL.md) | Wenn es um Fuehren: Mehrparteienkonflikt und Interessenmatrix in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Vertragsausfüller ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`klauselentscheidung`](skills/klauselentscheidung/SKILL.md) | Wenn es um Klauselentscheidungen in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kommandocenter-mehrsprachige-vertraege`](skills/kommandocenter-mehrsprachige-vertraege/SKILL.md) | Wenn es um Kommandocenter in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`konzern-rahmenvertrag-anpassen`](skills/konzern-rahmenvertrag-anpassen/SKILL.md) | Wenn es um Rahmenvertrag-Anpassung in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mandantenkommunikation-redteam-qualitygate`](skills/mandantenkommunikation-redteam-qualitygate/SKILL.md) | Wenn es um Mandantenkommunikation in Vertragsausfüller geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| [`mappen-zahlen-schwellen-und-berechnung`](skills/mappen-zahlen-schwellen-und-berechnung/SKILL.md) | Wenn es um Mappen: Zahlen, Schwellenwerte und Berechnung in Vertragsausfüller geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`mehrsprachige-vertraege-spezial`](skills/mehrsprachige-vertraege-spezial/SKILL.md) | Wenn es um VAF: Mehrsprachige Verträge in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nachfrage-abschlussprodukt-und-uebergabe`](skills/nachfrage-abschlussprodukt-und-uebergabe/SKILL.md) | Wenn es um Nachfrage: Abschlussprodukt und Übergabe in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`neue-rueckfragen-strippen`](skills/neue-rueckfragen-strippen/SKILL.md) | Wenn es um Neue: Internationaler Bezug und Schnittstellen in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Vertragsausfüller geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`platzhalterlogik-bauleiter`](skills/platzhalterlogik-bauleiter/SKILL.md) | Wenn es um VAF: Platzhalterlogik Bauleiter in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`plausibilitaetscheck-termsheet`](skills/plausibilitaetscheck-termsheet/SKILL.md) | Wenn es um Plausibilitätscheck in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quality-gate-redline-qa`](skills/quality-gate-redline-qa/SKILL.md) | Wenn es um Quality Gate — Vertragsausfueller in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`redline-qa`](skills/redline-qa/SKILL.md) | Wenn es um Redline-QA in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`rueckfragen-compliance-dokumentation-und-akte`](skills/rueckfragen-compliance-dokumentation-und-akte/SKILL.md) | Wenn es um Rueckfragen: Compliance-Dokumentation und Aktenvermerk in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`rueckfrageninterview`](skills/rueckfrageninterview/SKILL.md) | Wenn es um Rückfrageninterview in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`sheets-quellenkarte`](skills/sheets-quellenkarte/SKILL.md) | Wenn es um Sheets Quellenkarte in Vertragsausfüller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`spezial-sheets-livequellen-und-rechtsprechungscheck`](skills/spezial-sheets-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Sheets: Livequellen- und Rechtsprechungscheck in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-vertraege-formular-portal-und-einreichung`](skills/spezial-vertraege-formular-portal-und-einreichung/SKILL.md) | Wenn es um Vertraege: Formular, Portal und Einreichungslogik in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md) | Wenn es um Vertragsausfueller — Allgemein in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`strippen-risikoampel-und-gegenargumente`](skills/strippen-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Strippen: Risikoampel, Gegenargumente und Verteidigungslinien in Vertragsausfüller geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`template-erkennung-format-track-changes`](skills/template-erkennung-format-track-changes/SKILL.md) | Wenn es um Template-Erkennung in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`template-format-und-source`](skills/template-format-und-source/SKILL.md) | Wenn es um VAF: Template-Format und Quelle in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`term-track-vertraege`](skills/term-track-vertraege/SKILL.md) | Wenn es um Term: Verhandlung, Vergleich und Eskalation in Vertragsausfüller geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`termsheet-mapping`](skills/termsheet-mapping/SKILL.md) | Wenn es um Term-Sheet-Mapping in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`track-changes-nur-nach-frage`](skills/track-changes-nur-nach-frage/SKILL.md) | Wenn es um Track Changes nur nach Frage in Vertragsausfüller geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`track-mandantenkommunikation-entscheidungsvorlage`](skills/track-mandantenkommunikation-entscheidungsvorlage/SKILL.md) | Wenn es um Track: Mandantenkommunikation und Entscheidungsvorlage in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vaf-fremdsprachige-vertraege-bilingual`](skills/vaf-fremdsprachige-vertraege-bilingual/SKILL.md) | Wenn es um Bilinguale Vertraege in Vertragsausfüller geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`vaf-mehrsprachige-vertraege-spezial`](skills/vaf-mehrsprachige-vertraege-spezial/SKILL.md) | Wenn es um VAF: Mehrsprachige Vertraege in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vaf-versionierung-aenderungsverfolgung-spezial`](skills/vaf-versionierung-aenderungsverfolgung-spezial/SKILL.md) | Wenn es um Vaf Versionierung Aenderungsverfolgung Spezial in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`vertraege-formular-portal-und-einreichung`](skills/vertraege-formular-portal-und-einreichung/SKILL.md) | Wenn es um Verträge: Formular, Portal und Einreichungslogik in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vertragsausfueller-erstpruefung-und-mandatsziel`](skills/vertragsausfueller-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Vertragsausfueller: Erstprüfung, Rollenklärung und Mandatsziel in Vertragsausfüller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vorlagen-vertragsausfueller-vaf-altvertrag`](skills/vorlagen-vertragsausfueller-vaf-altvertrag/SKILL.md) | Wenn es um Vorlagen: Fristen, Form, Zuständigkeit und Rechtsweg in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Vertragsausfüller geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in Vertragsausfüller geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Vertragsausfüller geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

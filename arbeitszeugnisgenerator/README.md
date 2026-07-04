# Arbeitszeugnisgenerator

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`arbeitszeugnisgenerator`) | [`arbeitszeugnisgenerator.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akte

| Akte | Download |
| --- | --- |
| Pluginlokale Testakte | [`arbeitszeugnisgenerator-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator-testakte.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Erstellt deutsche Arbeitszeugnisse Schritt für Schritt: Rolle, Stammdaten, Tätigkeiten, Leistungs- und Verhaltensbewertung, Notenwahl per Ampelsystem, Schlussformeln. Wahlweise vorgegebene Note oder geführte Einschätzung. Mehrere Harnesses: qualifiziert, einfach, Ausbildung.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnisgenerator.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnisgenerator/arbeitszeugnisgenerator-werkstatt.md" download><code>arbeitszeugnisgenerator-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnisgenerator/arbeitszeugnisgenerator-schnellstart.md" download><code>arbeitszeugnisgenerator-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`arbeitszeugnisgenerator-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator-testakte.zip), [`arbeitszeugnisgenerator-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein deutsches Arbeitszeugnis Schritt für Schritt erstellen — rechtssicher, mit korrekter Zeugnissprache, in der gewünschten Notenstufe.

## Wenn du das brauchst

- **Personalabteilung** muss für einen ausscheidenden Mitarbeiter ein qualifiziertes Arbeitszeugnis erstellen und braucht passende Formeln zur Wunschnote.
- **Geschäftsführer einer kleinen Firma** schreibt zum ersten Mal ein Arbeitszeugnis und will nicht versehentlich Geheimcodes einbauen, die die Note kippen.
- **Arbeitnehmer** möchte einen sauberen Vorschlag für das Wunschzeugnis erstellen und der HR-Abteilung vorlegen.
- **Auszubildender oder Ausbilder** braucht ein Ausbildungszeugnis nach Paragraf 16 BBiG.

## Was du am Ende in der Hand hast

Ein vollständiges Arbeitszeugnis im richtigen Format — qualifiziertes Zeugnis, einfaches Zeugnis, Zwischenzeugnis oder Ausbildungszeugnis — mit Kopfdaten, Tätigkeitsbeschreibung, Leistungs- und Verhaltensbewertung in der Wunschnote, Schlussformel und Beendigungsgrund. Auf Wunsch mit Begründung pro Satz, welche Notenwirkung er entfaltet.

## Der Weg dorthin

Rolle und Anliegen klären → Zeugnisart und Harness wählen → Stammdaten erfassen → Tätigkeiten erheben → Notenwahl (vorgeben oder durch Fragen ermitteln lassen) → satzweise Generierung mit Ampel-Vorschau → Schlussformel und Beendigungsgrund → Revision und Feinschliff.

## Workflows

Drei Modi zur Wahl:

- **Direkt-Modus**: Du gibst die Wunschnote pro Bewertungsfeld vor (Leistung, Verhalten, Führung). Der Generator setzt die passenden Formeln.
- **Geführter Modus**: Der Generator stellt gezielte Fragen zu Leistung, Engagement, Verhalten — und schlägt am Ende eine Note vor ("das klingt nach Note 2 bis 3, soll ich so schreiben?"). Du bestätigst oder korrigierst.
- **Hybrid-Modus**: Du gibst die Gesamtnote vor, der Generator fragt nur noch die offenen Details ab (typische Tätigkeiten, besondere Projekte, Beendigungsgrund).

## Was dich aufhält

- **Wohlwollensgrundsatz versus Wahrheitspflicht**: Beides muss eingehalten werden, kein Schönschreiben um den Preis der Wahrheit.
- **Geheimcodes**: Versehentlich eingebaute Negativcodes ("bemüht sich", "im Großen und Ganzen", "lernte schnell kennen und schätzen") kippen die Note. Der Generator vermeidet sie aktiv.
- **Zeugnisklarheit (objektiver Empfängerhorizont, BAG 9 AZR 352.04)**: Keine doppelten Böden, keine widersprüchlichen Aussagen.
- **Äußere Form**: Briefkopf, Datum, Unterschrift, kein Knick, keine Streichungen.
- **Schlussformel-Wirkung**: Schlussformeln wirken oft stärker als die Bewertungssätze. Eine schwache Schlussformel zieht die Gesamtnote.

## Rechtlicher Anker

- Paragraf 109 GewO (Zeugnisanspruch)
- Paragraf 16 BBiG (Ausbildungszeugnis)
- Paragrafen 241 Absatz 2, 280 Absatz 1 BGB (Nebenpflicht und Schadensersatz)
- BAG-Leitentscheidungen zu Notenstufen, Beweislast, Schlussformel und Zeugnisklarheit (im Werkstatt-Prompt ausführlich)

## KI-Verordnung: mögliche Einstufung als Hochrisiko-KI

Wird dieses Plugin im Personalwesen produktiv eingesetzt, kann es ein Hochrisiko-KI-System nach Artikel 6 Absatz 2 in Verbindung mit Anhang III Nummer 4 Buchstabe b der Verordnung (EU) 2024/1689 (KI-Verordnung) sein. Anhang III Nummer 4 Buchstabe b erfasst KI-Systeme, die bestimmungsgemäß für Entscheidungen über die Bedingungen von Arbeitsverhältnissen, für die Bewertung der Arbeitsleistung und des Arbeitsverhaltens oder für vergleichbare Personalentscheidungen verwendet werden. Ein automatisiert erstelltes Arbeitszeugnis betrifft genau diese Bewertungs- und Bedingungsdimension. Anhang III Nummer 4 Buchstabe a erfasst dagegen die Personalauswahl und Bewerbungsphase und greift hier in der Regel nicht.

Folgen einer Einstufung als Hochrisiko-KI können sein: Pflicht zu menschlicher Aufsicht, Dokumentations- und Transparenzpflichten, Risikomanagement, Information der Beschäftigten beziehungsweise des Betriebsrats und gegebenenfalls eine Grundrechte-Folgenabschätzung. Die genaue Reichweite hängt vom Einsatzkontext, von der Rolle als Anbieter oder Betreiber und vom Geltungsbeginn nach Artikel 113 KI-VO ab. Diese Hinweise sind keine Rechtsberatung; im Zweifel ist eine arbeitsrechtliche und KI-rechtliche Bewertung im Einzelfall geboten.

## Hinweise

Generischer Entwurfsstand, alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer prüft den generierten Text auf Plausibilität und Eignung im konkreten Einzelfall. Keine Rechtsberatung. Keine Garantie für Vollständigkeit oder Aktualität der Rechtsprechung. Bei streitigen Fällen Fachanwalt für Arbeitsrecht hinzuziehen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 2. Unterlagen, Sachverhalt und Quellen | `bag-leitentscheidungen-beweislast`, `kopfdaten-und-aussere-form`, `stammdaten-erhebung` |
| 3. Prüfung, Anspruch und Subsumtion | `fuehrungskraft-bewertung` |
| 4. Gestaltung, Strategie und Verhandlung | `compliance-integritaet-formeln` |
| 8. Spezialmodule und Schnittstellen | `auslassungen-vermeiden`, `bag-leitentscheidungen-notenstufen`, `beendigungsgrund-formulieren`, `belastbarkeit-formeln`, `besondere-leistungen-projekte`, `drift-und-schaufenster-vermeiden`, `einfuehrung-mandantenanliegen`, `engagement-motivation-formeln`, `frequenzadverbien-katalog`, `geheimcodes-vermeiden`, `langzeit-arbeitsverhaeltnis`, `mehrere-positionen-im-zeugnis`, `note-1-formeln-leistung`, `note-2-formeln-leistung`, `note-3-formeln-leistung`, `note-4-formeln-leistung`, `note-5-formeln-leistung`, `notenwahl-modus`, ... plus 17 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 40 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `auslassungen-vermeiden` | Wenn es um Auslassungen vermeiden in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bag-leitentscheidungen-beweislast` | Wenn es um BAG-Leitentscheidungen zur Beweislast in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bag-leitentscheidungen-notenstufen` | Wenn es um BAG-Leitentscheidungen zu Notenstufen in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beendigungsgrund-formulieren` | Wenn es um Beendigungsgrund formulieren in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `belastbarkeit-formeln` | Wenn es um Belastbarkeit-Formeln in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `besondere-leistungen-projekte` | Wenn es um Besondere Leistungen und Projekte in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `compliance-integritaet-formeln` | Wenn es um Compliance- und Integritäts-Formeln in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `drift-und-schaufenster-vermeiden` | Wenn es um Drift und Schaufenster vermeiden in Arbeitszeugnisgenerator geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sch... |
| `einfuehrung-mandantenanliegen` | Wenn es um Einführung und Mandantenanliegen in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `engagement-motivation-formeln` | Wenn es um Engagement- und Motivations-Formeln in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `frequenzadverbien-katalog` | Wenn es um Frequenzadverbien-Katalog in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fuehrungskraft-bewertung` | Wenn es um Führungskraft-Bewertung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `geheimcodes-vermeiden` | Wenn es um Geheimcodes vermeiden in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kopfdaten-und-aussere-form` | Wenn es um Kopfdaten und äußere Form in Arbeitszeugnisgenerator geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `langzeit-arbeitsverhaeltnis` | Wenn es um Langzeit-Arbeitsverhältnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mehrere-positionen-im-zeugnis` | Wenn es um Mehrere Positionen im Zeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `note-1-formeln-leistung` | Wenn es um Note 1 — Formeln Leistung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `note-2-formeln-leistung` | Wenn es um Note 2 — Formeln Leistung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `note-3-formeln-leistung` | Wenn es um Note 3 — Formeln Leistung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `note-4-formeln-leistung` | Wenn es um Note 4 — Formeln Leistung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `note-5-formeln-leistung` | Wenn es um Note 5 — Formeln Leistung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `notenwahl-modus` | Wenn es um Notenwahl-Modus in Arbeitszeugnisgenerator geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `rechtlicher-anker-109-gewo` | Wenn es um Rechtlicher Anker — Paragraf 109 GewO und verwandte Normen in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `revision-und-aenderungswuensche` | Wenn es um Revision und Änderungswünsche in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rollen-und-harness-wahl` | Wenn es um Rollen und Harness-Wahl in Arbeitszeugnisgenerator geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `schlussformel-baukasten` | Wenn es um Schlussformel-Baukasten in Arbeitszeugnisgenerator geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `schlussformel-notenwirkung` | Wenn es um Schlussformel-Notenwirkung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stammdaten-erhebung` | Wenn es um Stammdaten-Erhebung in Arbeitszeugnisgenerator geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `steigerungsadverbien-katalog` | Wenn es um Steigerungsadverbien-Katalog in Arbeitszeugnisgenerator geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `taetigkeitsbeschreibung-erheben` | Wenn es um Tätigkeitsbeschreibung erheben in Arbeitszeugnisgenerator geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `teamarbeit-formeln` | Wenn es um Teamarbeit-Formeln in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `teilzeit-elternzeit-darstellung` | Wenn es um Teilzeit und Elternzeit im Zeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verhalten-vorgesetzte-kollegen-kunden` | Wenn es um Verhalten gegenüber Vorgesetzten, Kollegen und Kunden in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `wohlwollensgrundsatz-und-wahrheit` | Wenn es um Wohlwollensgrundsatz und Wahrheit in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zeugnisart-ausbildungszeugnis-16-bbig` | Wenn es um Zeugnisart: Ausbildungszeugnis nach Paragraf 16 BBiG in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zeugnisart-einfach` | Wenn es um Zeugnisart: Einfaches Arbeitszeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zeugnisart-praktikum` | Wenn es um Zeugnisart: Praktikumszeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zeugnisart-qualifiziert` | Wenn es um Zeugnisart: Qualifiziertes Arbeitszeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zeugnisart-zwischenzeugnis` | Wenn es um Zeugnisart: Zwischenzeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zeugnisklarheit-objektiver-empfaengerhorizont` | Wenn es um Zeugnisklarheit — objektiver Empfängerhorizont (BAG 9 AZR 352/04; 9 AZR 386/10) in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

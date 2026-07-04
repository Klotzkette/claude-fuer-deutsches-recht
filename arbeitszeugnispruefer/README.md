# Arbeitszeugnispruefer


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`arbeitszeugnispruefer`) | [`arbeitszeugnispruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akte

| Akte | Download |
| --- | --- |
| Pluginlokale Testakte | [`arbeitszeugnispruefer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer-testakte.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prüft bestehende deutsche Arbeitszeugnisse Schritt für Schritt: Notenstufen, Zufriedenheits- und Verhaltensformeln, Geheimcodes, Auslassungen, Steigerungsadverbien, Schlussformel. Liefert Ampel-Einschätzung pro Satz, Gesamtnote, Aufforderungsschreiben oder Klagestrategie zur Berichtigung.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnispruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/arbeitszeugnispruefer-werkstatt.md" download><code>arbeitszeugnispruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/arbeitszeugnispruefer-schnellstart.md" download><code>arbeitszeugnispruefer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`arbeitszeugnispruefer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer-testakte.zip), [`arbeitszeugnispruefer-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein bereits vorliegendes deutsches Arbeitszeugnis Satz für Satz prüfen — Note, Geheimcodes, Auslassungen, Schlussformel — und brauchst eine belastbare Einschaetzung mit Rechtsprechungsanker.

## Wenn du das brauchst

- **Arbeitnehmer** hat ein Zeugnis erhalten und will wissen, welche Note darin codiert ist, bevor er bewirbt oder widerspricht.
- **Fachanwalt für Arbeitsrecht** prüft ein Zeugnis im Mandat auf Berichtigungsanspruch nach Paragraf 109 GewO.
- **Personalabteilung** prüft das eigene Zeugnis vor der Ausstellung gegen die Standards der BAG-Rechtsprechung.
- **Karriereberater oder Outplacement-Berater** sichten Zeugnisse aus dem Lebenslauf ihrer Klienten und brauchen eine schnelle Einordnung.

## Was du am Ende in der Hand hast

Eine Prüfung Satz für Satz mit Ampel-Einschaetzung (rot, orange, gruen), eine begründete Gesamtnotenspanne, eine Liste der Geheimcodes, Drift-Stellen und Auslassungen, ein Mandantenbericht in Klartext sowie auf Wunsch ein Aufforderungsschreiben an den Arbeitgeber zur Berichtigung oder eine Klagestrategie mit Vollstreckungsoption.

## Der Weg dorthin

Zeugnis einlesen → Stammdaten und Vollständigkeit prüfen → Tätigkeitsabschnitt auf Wertigkeitsdrift prüfen → Leistungssaetze auf Zufriedenheitsformel und Steigerungsadverbien prüfen → Verhaltenssaetze auf Personenreihenfolge und Geheimcodes prüfen → Schlussformel auf Note-Mismatch prüfen → Gesamtnote ableiten → Berichtigungspfad oder Annahme empfehlen.

## Workflows

Drei Modi zur Wahl:

- **Schnellpruefung**: Notenschaetzung, Top-Drei-Auffaelligkeiten, Empfehlung in wenigen Saetzen.
- **Vollpruefung**: Satzweise Einschaetzungsmatrix, Geheimcode-Katalog, Drift-Bericht, Schlussformel-Analyse, Mandantenbericht.
- **Berichtigungspfad**: Vollpruefung plus Aufforderungsschreiben an den Arbeitgeber und Klagestrategie mit Beweislastverteilung nach BAG-Linie.

## Was dich aufhält

- **Geheimcodes**: Formulierungen wie bemüht sich, im großen und ganzen, lernte schnell kennen und schätzen, verstand es zählen zu unsichtbaren Notenabwertungen.
- **Auslassungen**: Fehlt die Zusammenfassungsformel, fehlen Personengruppen im Verhalten, fehlt die Schlussformel, wirkt das wie eine Abwertung.
- **Drift in der Wertigkeit**: Wenn unwichtige Aufgaben zuerst genannt werden oder Kernaufgaben fehlen, droht Schaufenster-Effekt.
- **Beweislast nach BAG 9 AZR 584.13**: Note 1 oder 2 traegt der Arbeitnehmer, Note 4 oder 5 traegt der Arbeitgeber.
- **Schlussformel-Mismatch**: Schwache Schlussformel bei sonst gutem Zeugnis zieht die Gesamtwirkung herunter.

## Rechtlicher Anker

- Paragraf 109 GewO (Zeugnisanspruch und Berichtigung)
- Paragraf 16 BBiG (Ausbildungszeugnis)
- Paragrafen 241 Absatz 2, 280 Absatz 1 BGB (Nebenpflicht und Schadensersatz)
- BAG-Leitentscheidungen zu Notenstufen, Beweislast, Schlussformel und Zeugnisklarheit (im Werkstatt-Prompt ausführlich)

## KI-Verordnung: mögliche Einstufung als Hochrisiko-KI

Wird dieses Plugin im Personalwesen produktiv eingesetzt, kann es ein Hochrisiko-KI-System nach Artikel 6 Absatz 2 in Verbindung mit Anhang III Nummer 4 Buchstabe b der Verordnung (EU) 2024/1689 (KI-Verordnung) sein. Anhang III Nummer 4 Buchstabe b erfasst KI-Systeme, die bestimmungsgemäß für Entscheidungen über die Bedingungen von Arbeitsverhältnissen, für die Bewertung der Arbeitsleistung und des Arbeitsverhaltens oder für vergleichbare Personalentscheidungen verwendet werden. Eine automatisierte Prüfung eines Arbeitszeugnisses, etwa zur Bewertung der Notenstufe oder zur Steuerung von Berichtigungsansprüchen, betrifft genau diese Bewertungs- und Bedingungsdimension. Anhang III Nummer 4 Buchstabe a erfasst dagegen die Personalauswahl und Bewerbungsphase und greift hier in der Regel nicht.

Folgen einer Einstufung als Hochrisiko-KI können sein: Pflicht zu menschlicher Aufsicht, Dokumentations- und Transparenzpflichten, Risikomanagement, Information der Beschäftigten beziehungsweise des Betriebsrats und gegebenenfalls eine Grundrechte-Folgenabschätzung. Die genaue Reichweite hängt vom Einsatzkontext, von der Rolle als Anbieter oder Betreiber und vom Geltungsbeginn nach Artikel 113 KI-VO ab. Diese Hinweise sind keine Rechtsberatung; im Zweifel ist eine arbeitsrechtliche und KI-rechtliche Bewertung im Einzelfall geboten.

## Hinweise

Generischer Pruefstand, alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer prüft den Pruefbericht auf Plausibilität und Eignung im konkreten Einzelfall. Keine Rechtsberatung. Keine Garantie für Vollständigkeit oder Aktualität der Rechtsprechung. Bei streitigen Fällen Fachanwalt für Arbeitsrecht hinzuziehen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `intake-und-stammdaten-pruefen` |
| 2. Unterlagen, Sachverhalt und Quellen | `beweislast-bag-9-azr-584-13` |
| 4. Gestaltung, Strategie und Verhandlung | `klagestrategie-und-vollstreckung` |
| 6. Ergebnis, Schreiben und Kommunikation | `aeussere-form-und-briefkopf`, `aufforderungsschreiben-berichtigung`, `mandantenbericht-erstellen` |
| 8. Spezialmodule und Schnittstellen | `ampel-einschaetzung-pro-satz`, `auslassungen-erkennen`, `beendigungsgrund-pruefen`, `doppelboeden-und-verneinungen`, `einfuehrung-pruefauftrag`, `frequenzadverbien-pruefen`, `fuehrungskraft-verhalten-pruefen`, `geheimcodes-katalog`, `note-1-formeln-erkennen`, `note-2-formeln-erkennen`, `note-3-formeln-erkennen`, `note-4-formeln-erkennen`, `note-5-formeln-erkennen`, `notenstufen-bag-9-azr-386-10`, `personenreihenfolge-pruefen`, `rollen-und-modus-wahl`, `schaufenster-und-drift-erkennen`, `schlussformel-notenwirkung-bewerten`, ... plus 6 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aeussere-form-und-briefkopf` | Wenn es um Aeussere Form und Briefkopf pruefen in Arbeitszeugnispruefer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `ampel-einschaetzung-pro-satz` | Wenn es um Ampel-Einschaetzung pro Satz in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `aufforderungsschreiben-berichtigung` | Wenn es um Aufforderungsschreiben Berichtigung in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `auslassungen-erkennen` | Wenn es um Auslassungen erkennen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `beendigungsgrund-pruefen` | Wenn es um Beendigungsgrund pruefen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `beweislast-bag-9-azr-584-13` | Wenn es um Beweislast nach BAG 9 AZR 584.13 in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `doppelboeden-und-verneinungen` | Wenn es um Doppelboeden und Verneinungen erkennen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfra... |
| `einfuehrung-pruefauftrag` | Wenn es um Einfuehrung in den Pruefauftrag in Arbeitszeugnispruefer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `frequenzadverbien-pruefen` | Wenn es um Frequenzadverbien pruefen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `fuehrungskraft-verhalten-pruefen` | Wenn es um Fuehrungskraft-Verhalten pruefen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `geheimcodes-katalog` | Wenn es um Geheimcodes-Katalog in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `intake-und-stammdaten-pruefen` | Wenn es um Intake und Stammdaten pruefen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `klagestrategie-und-vollstreckung` | Wenn es um Klagestrategie und Vollstreckung in Arbeitszeugnispruefer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `mandantenbericht-erstellen` | Wenn es um Mandantenbericht erstellen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `note-1-formeln-erkennen` | Wenn es um Note-1-Formeln erkennen in Arbeitszeugnispruefer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `note-2-formeln-erkennen` | Wenn es um Note-2-Formeln erkennen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `note-3-formeln-erkennen` | Wenn es um Note-3-Formeln erkennen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `note-4-formeln-erkennen` | Wenn es um Note-4-Formeln erkennen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `note-5-formeln-erkennen` | Wenn es um Note-5-Formeln erkennen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `notenstufen-bag-9-azr-386-10` | Wenn es um Notenstufen nach BAG 9 AZR 386.10 in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schr... |
| `personenreihenfolge-pruefen` | Wenn es um Personenreihenfolge pruefen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `rollen-und-modus-wahl` | Wenn es um Rollen- und Moduswahl vor der Zeugnispruefung in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nach... |
| `schaufenster-und-drift-erkennen` | Wenn es um Schaufenster- und Drift-Erkennung in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `schlussformel-notenwirkung-bewerten` | Wenn es um Schlussformel-Notenwirkung bewerten in Arbeitszeugnispruefer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schlussformel-pruefen` | Wenn es um Schlussformel pruefen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `steigerungsadverbien-pruefen` | Wenn es um Steigerungsadverbien pruefen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `taetigkeitsabschnitt-wertigkeit-pruefen` | Wenn es um Taetigkeitsabschnitt und Wertigkeit pruefen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachwe... |
| `verhaltensabschnitt-pruefen` | Wenn es um Verhaltensabschnitt pruefen in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `zeugnisklarheit-objektiver-empfaengerhorizont` | Wenn es um Zeugnisklarheit nach dem objektiven Empfaengerhorizont (BAG 9 AZR 352.04; 9 AZR 386.10) in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte... |
| `zusammenfassungsformel-erkennen` | Wenn es um Zusammenfassungsformel erkennen und decodieren in Arbeitszeugnispruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nac... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

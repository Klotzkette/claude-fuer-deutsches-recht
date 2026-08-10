# Arbeitszeugnisprüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prüft bestehende deutsche Arbeitszeugnisse Schritt für Schritt: Notenstufen, Zufriedenheits- und Verhaltensformeln, Geheimcodes, Auslassungen, Steigerungsadverbien, Schlussformel. Liefert Ampel-Einschätzung pro Satz, Gesamtnote, Aufforderungsschreiben oder Klagestrategie zur Berichtigung.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/arbeitszeugnispruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/arbeitszeugnispruefer.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart als Markdown laden und zusammen mit den Unterlagen öffnen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Arbeitszeugnisprüfer:

> Lies zuerst alle Dateien im ausgewählten Ordner. Bearbeite den Vorgang mit diesem Fachgebiet. Beginne mit folgendem Arbeitsschritt: Änderungsmatrix: Satz des Arbeitgebers, Problem, Rechtsanker, gewünschte Fassung, Beleg und Prozessrisiko als Tabelle ausgeben. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnispruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/arbeitszeugnispruefer-schnellstart.md" download><code>arbeitszeugnispruefer-schnellstart.md</code></a> |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/arbeitszeugnispruefer-werkstatt.md" download><code>arbeitszeugnispruefer-werkstatt.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| Pluginlokale Akte | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf) | [`arbeitszeugnispruefer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer-testakte.zip) | [`arbeitszeugnispruefer-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer-testakte-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein bereits vorliegendes deutsches Arbeitszeugnis Satz für Satz prüfen — Note, Geheimcodes, Auslassungen, Schlussformel — und brauchst eine belastbare Einschätzung mit Rechtsprechungsanker.

## Wenn du das brauchst

- **Arbeitnehmer** hat ein Zeugnis erhalten und will wissen, welche Note darin codiert ist, bevor er bewirbt oder widerspricht.
- **Fachanwalt für Arbeitsrecht** prüft ein Zeugnis im Mandat auf Berichtigungsanspruch nach Paragraf 109 GewO.
- **Personalabteilung** prüft das eigene Zeugnis vor der Ausstellung gegen die Standards der BAG-Rechtsprechung.
- **Karriereberater oder Outplacement-Berater** sichten Zeugnisse aus dem Lebenslauf ihrer Klienten und brauchen eine schnelle Einordnung.

## Was du am Ende in der Hand hast

Eine Prüfung Satz für Satz mit Ampel-Einschätzung (rot, orange, grün), eine begründete Gesamtnotenspanne, eine Liste der Geheimcodes, Drift-Stellen und Auslassungen, ein Mandantenbericht in Klartext sowie auf Wunsch ein Aufforderungsschreiben an den Arbeitgeber zur Berichtigung oder eine Klagestrategie mit Vollstreckungsoption.

## Der Weg dorthin

Zeugnis einlesen → Stammdaten und Vollständigkeit prüfen → Tätigkeitsabschnitt auf Wertigkeitsdrift prüfen → Leistungssätze auf Zufriedenheitsformel und Steigerungsadverbien prüfen → Verhaltenssätze auf Personenreihenfolge und Geheimcodes prüfen → Schlussformel auf Note-Mismatch prüfen → Gesamtnote ableiten → Berichtigungspfad oder Annahme empfehlen.

## Workflows

Drei Modi zur Wahl:

- **Schnellprüfung**: Notenschätzung, Top-Drei-Auffälligkeiten, Empfehlung in wenigen Sätzen.
- **Vollprüfung**: Satzweise Einschätzungsmatrix, Geheimcode-Katalog, Drift-Bericht, Schlussformel-Analyse, Mandantenbericht.
- **Berichtigungspfad**: Vollprüfung plus Aufforderungsschreiben an den Arbeitgeber und Klagestrategie mit Beweislastverteilung nach BAG-Linie.

## Was dich aufhält

- **Geheimcodes**: Formulierungen wie bemüht sich, im großen und ganzen, lernte schnell kennen und schätzen, verstand es zählen zu unsichtbaren Notenabwertungen.
- **Auslassungen**: Fehlt die Zusammenfassungsformel, fehlen Personengruppen im Verhalten, fehlt die Schlussformel, wirkt das wie eine Abwertung.
- **Drift in der Wertigkeit**: Wenn unwichtige Aufgaben zuerst genannt werden oder Kernaufgaben fehlen, droht Schaufenster-Effekt.
- **Beweislast nach BAG 9 AZR 584.13**: Note 1 oder 2 trägt der Arbeitnehmer, Note 4 oder 5 trägt der Arbeitgeber.
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

Generischer Prüfstand, alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer prüft den Prüfbericht auf Plausibilität und Eignung im konkreten Einzelfall. Keine Rechtsberatung. Keine Garantie für Vollständigkeit oder Aktualität der Rechtsprechung. Bei streitigen Fällen Fachanwalt für Arbeitsrecht hinzuziehen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`intake-und-stammdaten-pruefen`](skills/intake-und-stammdaten-pruefen/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`beweislast-bag-9-azr-584-13`](skills/beweislast-bag-9-azr-584-13/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`klagestrategie-und-vollstreckung`](skills/klagestrategie-und-vollstreckung/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`aeussere-form-und-briefkopf`](skills/aeussere-form-und-briefkopf/SKILL.md), [`aufforderungsschreiben-berichtigung`](skills/aufforderungsschreiben-berichtigung/SKILL.md), [`mandantenbericht-erstellen`](skills/mandantenbericht-erstellen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`zeugnisklarheit-objektiver-empfaengerhorizont`](skills/zeugnisklarheit-objektiver-empfaengerhorizont/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`ampel-einschaetzung-pro-satz`](skills/ampel-einschaetzung-pro-satz/SKILL.md), [`auslassungen-erkennen`](skills/auslassungen-erkennen/SKILL.md), [`beendigungsgrund-pruefen`](skills/beendigungsgrund-pruefen/SKILL.md), [`doppelboeden-und-verneinungen`](skills/doppelboeden-und-verneinungen/SKILL.md), [`einfuehrung-pruefauftrag`](skills/einfuehrung-pruefauftrag/SKILL.md), [`frequenzadverbien-pruefen`](skills/frequenzadverbien-pruefen/SKILL.md), [`fuehrungskraft-verhalten-pruefen`](skills/fuehrungskraft-verhalten-pruefen/SKILL.md), [`geheimcodes-katalog`](skills/geheimcodes-katalog/SKILL.md), [`note-1-formeln-erkennen`](skills/note-1-formeln-erkennen/SKILL.md), [`note-2-formeln-erkennen`](skills/note-2-formeln-erkennen/SKILL.md), [`note-3-formeln-erkennen`](skills/note-3-formeln-erkennen/SKILL.md), [`note-4-formeln-erkennen`](skills/note-4-formeln-erkennen/SKILL.md), [`note-5-formeln-erkennen`](skills/note-5-formeln-erkennen/SKILL.md), [`notenstufen-bag-9-azr-386-10`](skills/notenstufen-bag-9-azr-386-10/SKILL.md), [`personenreihenfolge-pruefen`](skills/personenreihenfolge-pruefen/SKILL.md), [`rollen-und-modus-wahl`](skills/rollen-und-modus-wahl/SKILL.md), [`schaufenster-und-drift-erkennen`](skills/schaufenster-und-drift-erkennen/SKILL.md), [`schlussformel-notenwirkung-bewerten`](skills/schlussformel-notenwirkung-bewerten/SKILL.md), ... plus 5 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 31 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; der Direktdownload lädt dieselbe Datei als Markdown. Beschreibungen stammen aus dem jeweiligen `description`-Feld.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`aeussere-form-und-briefkopf`](skills/aeussere-form-und-briefkopf/SKILL.md) | Wenn es um Äußere Form und Briefkopf prüfen in Arbeitszeugnisprüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/aeussere-form-und-briefkopf/SKILL.md" download><code>SKILL.md</code></a> |
| [`ampel-einschaetzung-pro-satz`](skills/ampel-einschaetzung-pro-satz/SKILL.md) | Wenn es um Ampel-Einschätzung pro Satz in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/ampel-einschaetzung-pro-satz/SKILL.md" download><code>SKILL.md</code></a> |
| [`aufforderungsschreiben-berichtigung`](skills/aufforderungsschreiben-berichtigung/SKILL.md) | Wenn es um Aufforderungsschreiben Berichtigung in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/aufforderungsschreiben-berichtigung/SKILL.md" download><code>SKILL.md</code></a> |
| [`auslassungen-erkennen`](skills/auslassungen-erkennen/SKILL.md) | Wenn es um Auslassungen erkennen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/auslassungen-erkennen/SKILL.md" download><code>SKILL.md</code></a> |
| [`beendigungsgrund-pruefen`](skills/beendigungsgrund-pruefen/SKILL.md) | Wenn es um Beendigungsgrund prüfen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/beendigungsgrund-pruefen/SKILL.md" download><code>SKILL.md</code></a> |
| [`beweislast-bag-9-azr-584-13`](skills/beweislast-bag-9-azr-584-13/SKILL.md) | Wenn es um Beweislast nach BAG 9 AZR 584.13 in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/beweislast-bag-9-azr-584-13/SKILL.md" download><code>SKILL.md</code></a> |
| [`doppelboeden-und-verneinungen`](skills/doppelboeden-und-verneinungen/SKILL.md) | Wenn es um Doppelböden und Verneinungen erkennen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/doppelboeden-und-verneinungen/SKILL.md" download><code>SKILL.md</code></a> |
| [`einfuehrung-pruefauftrag`](skills/einfuehrung-pruefauftrag/SKILL.md) | Wenn es um Einführung in den Prüfauftrag in Arbeitszeugnisprüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/einfuehrung-pruefauftrag/SKILL.md" download><code>SKILL.md</code></a> |
| [`frequenzadverbien-pruefen`](skills/frequenzadverbien-pruefen/SKILL.md) | Wenn es um Frequenzadverbien prüfen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/frequenzadverbien-pruefen/SKILL.md" download><code>SKILL.md</code></a> |
| [`fuehrungskraft-verhalten-pruefen`](skills/fuehrungskraft-verhalten-pruefen/SKILL.md) | Wenn es um Führungskraft-Verhalten prüfen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/fuehrungskraft-verhalten-pruefen/SKILL.md" download><code>SKILL.md</code></a> |
| [`geheimcodes-katalog`](skills/geheimcodes-katalog/SKILL.md) | Wenn es um Geheimcodes-Katalog in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/geheimcodes-katalog/SKILL.md" download><code>SKILL.md</code></a> |
| [`intake-und-stammdaten-pruefen`](skills/intake-und-stammdaten-pruefen/SKILL.md) | Wenn es um Intake und Stammdaten prüfen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/intake-und-stammdaten-pruefen/SKILL.md" download><code>SKILL.md</code></a> |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Arbeitszeugnisprüfer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/juristischer-argumentationskern/SKILL.md" download><code>SKILL.md</code></a> |
| [`klagestrategie-und-vollstreckung`](skills/klagestrategie-und-vollstreckung/SKILL.md) | Wenn es um Klagestrategie und Vollstreckung in Arbeitszeugnisprüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/klagestrategie-und-vollstreckung/SKILL.md" download><code>SKILL.md</code></a> |
| [`mandantenbericht-erstellen`](skills/mandantenbericht-erstellen/SKILL.md) | Wenn es um Mandantenbericht erstellen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/mandantenbericht-erstellen/SKILL.md" download><code>SKILL.md</code></a> |
| [`note-1-formeln-erkennen`](skills/note-1-formeln-erkennen/SKILL.md) | Wenn es um Note-1-Formeln erkennen in Arbeitszeugnisprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/note-1-formeln-erkennen/SKILL.md" download><code>SKILL.md</code></a> |
| [`note-2-formeln-erkennen`](skills/note-2-formeln-erkennen/SKILL.md) | Wenn es um Note-2-Formeln erkennen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/note-2-formeln-erkennen/SKILL.md" download><code>SKILL.md</code></a> |
| [`note-3-formeln-erkennen`](skills/note-3-formeln-erkennen/SKILL.md) | Wenn es um Note-3-Formeln erkennen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/note-3-formeln-erkennen/SKILL.md" download><code>SKILL.md</code></a> |
| [`note-4-formeln-erkennen`](skills/note-4-formeln-erkennen/SKILL.md) | Wenn es um Note-4-Formeln erkennen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/note-4-formeln-erkennen/SKILL.md" download><code>SKILL.md</code></a> |
| [`note-5-formeln-erkennen`](skills/note-5-formeln-erkennen/SKILL.md) | Wenn es um Note-5-Formeln erkennen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/note-5-formeln-erkennen/SKILL.md" download><code>SKILL.md</code></a> |
| [`notenstufen-bag-9-azr-386-10`](skills/notenstufen-bag-9-azr-386-10/SKILL.md) | Wenn es um Notenstufen nach BAG 9 AZR 386.10 in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/notenstufen-bag-9-azr-386-10/SKILL.md" download><code>SKILL.md</code></a> |
| [`personenreihenfolge-pruefen`](skills/personenreihenfolge-pruefen/SKILL.md) | Wenn es um Personenreihenfolge prüfen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/personenreihenfolge-pruefen/SKILL.md" download><code>SKILL.md</code></a> |
| [`rollen-und-modus-wahl`](skills/rollen-und-modus-wahl/SKILL.md) | Wenn es um Rollen- und Moduswahl vor der Zeugnisprüfung in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachwe... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/rollen-und-modus-wahl/SKILL.md" download><code>SKILL.md</code></a> |
| [`schaufenster-und-drift-erkennen`](skills/schaufenster-und-drift-erkennen/SKILL.md) | Wenn es um Schaufenster- und Drift-Erkennung in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/schaufenster-und-drift-erkennen/SKILL.md" download><code>SKILL.md</code></a> |
| [`schlussformel-notenwirkung-bewerten`](skills/schlussformel-notenwirkung-bewerten/SKILL.md) | Wenn es um Schlussformel-Notenwirkung bewerten in Arbeitszeugnisprüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/schlussformel-notenwirkung-bewerten/SKILL.md" download><code>SKILL.md</code></a> |
| [`schlussformel-pruefen`](skills/schlussformel-pruefen/SKILL.md) | Wenn es um Schlussformel prüfen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/schlussformel-pruefen/SKILL.md" download><code>SKILL.md</code></a> |
| [`steigerungsadverbien-pruefen`](skills/steigerungsadverbien-pruefen/SKILL.md) | Wenn es um Steigerungsadverbien prüfen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/steigerungsadverbien-pruefen/SKILL.md" download><code>SKILL.md</code></a> |
| [`taetigkeitsabschnitt-wertigkeit-pruefen`](skills/taetigkeitsabschnitt-wertigkeit-pruefen/SKILL.md) | Wenn es um Tätigkeitsabschnitt und Wertigkeit prüfen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisf... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/taetigkeitsabschnitt-wertigkeit-pruefen/SKILL.md" download><code>SKILL.md</code></a> |
| [`verhaltensabschnitt-pruefen`](skills/verhaltensabschnitt-pruefen/SKILL.md) | Wenn es um Verhaltensabschnitt prüfen in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/verhaltensabschnitt-pruefen/SKILL.md" download><code>SKILL.md</code></a> |
| [`zeugnisklarheit-objektiver-empfaengerhorizont`](skills/zeugnisklarheit-objektiver-empfaengerhorizont/SKILL.md) | Wenn es um Zeugnisklarheit nach dem objektiven Empfängerhorizont (BAG 9 AZR 352.04; 9 AZR 386.10) in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte m... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/zeugnisklarheit-objektiver-empfaengerhorizont/SKILL.md" download><code>SKILL.md</code></a> |
| [`zusammenfassungsformel-erkennen`](skills/zusammenfassungsformel-erkennen/SKILL.md) | Wenn es um Zusammenfassungsformel erkennen und decodieren in Arbeitszeugnisprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nach... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/skills/zusammenfassungsformel-erkennen/SKILL.md" download><code>SKILL.md</code></a> |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

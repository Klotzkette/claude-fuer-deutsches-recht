# Bauträgervertragsprüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prüft deutsche Bauträgerverträge: MaBV-Ratenplan und Sicherheiten, Paragrafen 650u und 650v BGB, AGB-Kontrolle, Baubeschreibung, Abnahme Gemeinschaftseigentum, Bauzeit, Preisanpassung, Teilungserklärung. Liefert Mandantengutachten und Aufforderungsschreiben an Bauträger und Notar.

Dieses Plugin gehört zum Marketplace mit 235 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`bautraegervertragspruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/bautraegervertragspruefer.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/bautraegervertragspruefer-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/bautraegervertragspruefer-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/bautraegervertragspruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/bautraegervertragspruefer.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Bauträgervertragsprüfer:

> Erfasse zuerst Dateinamen und Metadaten im ausgewählten Ordner. Lies zunächst die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: eine Klauselmatrix mit Mandantengutachten und Änderungswünschen. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`bautraegervertragspruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`bautraegervertragspruefer-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/bautraegervertragspruefer-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`bautraegervertragspruefer-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/bautraegervertragspruefer-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| Pluginlokale Akte | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf) | [`bautraegervertragspruefer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer-testakte.zip) | [`bautraegervertragspruefer-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer-testakte-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen deutschen Bauträgervertrag verbraucherseitig prüfen: Ratenplan, Sicherheiten, Baubeschreibung, Abnahme, Bauzeit, Preisanpassung, Teilungserklärung — und am Ende ein Gutachten plus ein Aufforderungsschreiben an Bauträger und Notar in der Hand haben.

**Schwester-Plugin:** [`bautraegervertrag-pruefer`](../bautraegervertrag-pruefer) (mit Bindestrich) deckt dasselbe Mandat mit einzeln ladbaren Spezial-Skills samt references-Workflow ab; dieses Plugin hier bietet Megaprompt-Original und zwei Testakten. Für ein Mandat genügt eines von beiden.

## Wenn du das brauchst

- **Verbraucher** hat einen Bauträgervertrag erhalten und will vor der notariellen Beurkundung wissen, welche Klauseln unwirksam sind und welche Streichungen er fordern muss.
- **Fachanwalt für Bau- und Architektenrecht** prüft einen Bauträgervertrag im Mandat und braucht eine vollständige Klauselmatrix mit MaBV-Prüfung und AGB-Kontrolle.
- **Notar** will den Entwurf gegen die Pflichten aus Paragraf 14 BNotO und gegen die MaBV-Schutzstruktur durchsehen.
- **Finanzierende Bank** prüft den Vertrag auf Auszahlungsrisiken nach dem Ratenplan und auf die Werthaltigkeit der Sicherheiten.

## Was du am Ende in der Hand hast

Eine Klauselmatrix Satz für Satz mit Ampel-Einschätzung (rot, orange, grün), ein Mandantengutachten mit paragraphenbezogener Begründung, ein Aufforderungsschreiben an Bauträger und Notar mit konkreter richtiger Fassung pro beanstandeter Klausel sowie eine Verhandlungsstrategie mit Gegenargument-Antwort.

## Der Weg dorthin

Vertrag und Anlagen einlesen → Fall-Fingerabdruck erstellen (Parteien, Einheit, Projekt, Preis, Ratenplan, Sicherheiten) → MaBV-Ratenplan und Sicherheiten prüfen → AGB-Kontrolle Klausel für Klausel → Baubeschreibung gegen Bausoll und anerkannte Regeln der Technik halten → Abnahme Gemeinschaftseigentum und Schlussrate prüfen → Bauzeit, Preisanpassung, Teilungserklärung kontrollieren → Mandantengutachten und Aufforderungsschreiben ausgeben.

## Workflows

Drei Modi zur Wahl:

- **Schnellprüfung**: Top-Zehn-Auffälligkeiten, geschätztes Risikoprofil, Empfehlung in wenigen Sätzen.
- **Vollprüfung**: Fall-Fingerabdruck, Klauselmatrix, AGB-Kontrolle, MaBV-Prüfung, Mandantengutachten.
- **Verhandlungspfad**: Vollprüfung plus Aufforderungsschreiben an Bauträger und Notar mit konkreter richtiger Fassung pro Klausel und Verhandlungsstrategie.

## Was dich aufhält

- **MaBV-Ratenplan**: Überhöhte Vorleistungen, falsche Verteilung der Raten auf Bauabschnitte, fehlende Sicherheit nach Paragraf 7 MaBV.
- **Verbraucherbauvertrag**: Paragrafen 650u und 650v BGB, Baubeschreibung als Pflichtinhalt, verbindliche Angabe zum Bauzeitende.
- **AGB-Kontrolle**: Notarielle Beurkundung schliesst AGB-Kontrolle nicht aus; geltungserhaltende Reduktion findet bei unwirksamen Verbraucher-AGB nicht statt.
- **Abnahme Gemeinschaftseigentum**: Verklammerung der Abnahme mit der Schlussrate gefährdet die werthaltige Sicherung.
- **Baubeschreibung**: Pauschale Verweise auf anerkannte Regeln der Technik ohne konkrete Spezifikation lassen das Bausoll offen.

## Rechtlicher Anker

- Paragrafen 650u und 650v BGB (Bauträgervertrag, Baubeschreibung)
- Paragrafen 305 bis 310 BGB (AGB-Kontrolle)
- Makler- und Bauträgerverordnung (MaBV), insbesondere Paragrafen 3, 7
- Paragraf 14 BNotO (Belehrungspflichten Notar)
- Wohnungseigentumsgesetz (Teilungserklärung, Abnahme Gemeinschaftseigentum)
- HOAI (Leistungsphasen Objektüberwachung)
- BGH-Leitentscheidungen zu Bauträgervertrag, MaBV und Abnahmeklauseln (im Werkstatt-Prompt ausführlich)

## Hinweise

Generischer Prüfstand, alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer prüft den Prüfbericht auf Plausibilität und Eignung im konkreten Einzelfall. Keine Rechtsberatung. Keine Garantie für Vollständigkeit oder Aktualität der Rechtsprechung. Bei streitigen Fällen Fachanwalt für Bau- und Architektenrecht oder Notar hinzuziehen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 2. Unterlagen, Sachverhalt und Quellen | [`drei-dokumente-paket-erzeugen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/drei-dokumente-paket-erzeugen/SKILL.md), [`mandantengutachten-aufbau`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mandantengutachten-aufbau/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/juristischer-argumentationskern/SKILL.md), [`verbraucherstatus-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/verbraucherstatus-pruefen/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`agb-kontrolle-klauseln`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/agb-kontrolle-klauseln/SKILL.md), [`bautraegervertrag-qualifikation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/bautraegervertrag-qualifikation/SKILL.md), [`bauzeitenplan-verzug`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/bauzeitenplan-verzug/SKILL.md), [`mabv-ratenplan-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mabv-ratenplan-pruefen/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`weg-beschluss-anfechtung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/weg-beschluss-anfechtung/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`aufforderungsschreiben-bautraeger-und-notar`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/aufforderungsschreiben-bautraeger-und-notar/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`abnahme-gemeinschaftseigentum`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/abnahme-gemeinschaftseigentum/SKILL.md), [`abnahme-sondereigentum-paragraf-640`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/abnahme-sondereigentum-paragraf-640/SKILL.md), [`auflassungsvormerkung-und-grundbuch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/auflassungsvormerkung-und-grundbuch/SKILL.md), [`baubeschreibung-bausoll-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/baubeschreibung-bausoll-pruefen/SKILL.md), [`faelligkeitsmitteilung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/faelligkeitsmitteilung-pruefen/SKILL.md), [`fall-fingerabdruck-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/fall-fingerabdruck-erstellen/SKILL.md), [`fertigstellungssicherheit-650m-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/fertigstellungssicherheit-650m-pruefen/SKILL.md), [`gemeinschaft-zieht-maengelrechte-an-sich`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/gemeinschaft-zieht-maengelrechte-an-sich/SKILL.md), [`gesamtnichtigkeit-paragraf-306-bgb`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/gesamtnichtigkeit-paragraf-306-bgb/SKILL.md), [`hoai-bauueberwachung-private-bauueberwachung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/hoai-bauueberwachung-private-bauueberwachung/SKILL.md), [`insolvenzrisiken-bautraeger`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/insolvenzrisiken-bautraeger/SKILL.md), [`mabv-sicherheit-paragraf-7-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mabv-sicherheit-paragraf-7-pruefen/SKILL.md), [`maengelrechte-633-634-bgb`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/maengelrechte-633-634-bgb/SKILL.md), [`mittlere-art-und-guete-und-din`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mittlere-art-und-guete-und-din/SKILL.md), [`notarbelehrung-paragraf-14-bnoto-17-beurkg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/notarbelehrung-paragraf-14-bnoto-17-beurkg/SKILL.md), [`paragraf-308-nr-4-bgb-leistungsaenderung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/paragraf-308-nr-4-bgb-leistungsaenderung/SKILL.md), [`paragraf-309-nr-12-bgb-tatsachenbestaetigung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/paragraf-309-nr-12-bgb-tatsachenbestaetigung/SKILL.md), [`preisanpassung-und-sonderwuensche`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/preisanpassung-und-sonderwuensche/SKILL.md), ... plus 3 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 31 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 31 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`abnahme-gemeinschaftseigentum`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/abnahme-gemeinschaftseigentum/SKILL.md) | Für Abnahme Gemeinschaftseigentum: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/abnahme-gemeinschaftseigentum/SKILL.md) |
| [`abnahme-sondereigentum-paragraf-640`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/abnahme-sondereigentum-paragraf-640/SKILL.md) | Für Abnahme Sondereigentum Paragraf 640 BGB: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/abnahme-sondereigentum-paragraf-640/SKILL.md) |
| [`agb-kontrolle-klauseln`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/agb-kontrolle-klauseln/SKILL.md) | Für AGB-Kontrolle Klauseln: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/agb-kontrolle-klauseln/SKILL.md) |
| [`aufforderungsschreiben-bautraeger-und-notar`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/aufforderungsschreiben-bautraeger-und-notar/SKILL.md) | Für Aufforderungsschreiben an Bauträger und Notar: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/aufforderungsschreiben-bautraeger-und-notar/SKILL.md) |
| [`auflassungsvormerkung-und-grundbuch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/auflassungsvormerkung-und-grundbuch/SKILL.md) | Für Auflassungsvormerkung und Grundbuch: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/auflassungsvormerkung-und-grundbuch/SKILL.md) |
| [`baubeschreibung-bausoll-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/baubeschreibung-bausoll-pruefen/SKILL.md) | Für Baubeschreibung und Bausoll prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/baubeschreibung-bausoll-pruefen/SKILL.md) |
| [`bautraegervertrag-qualifikation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/bautraegervertrag-qualifikation/SKILL.md) | Für Bauträgervertrag-Qualifikation: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/bautraegervertrag-qualifikation/SKILL.md) |
| [`bauzeitenplan-verzug`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/bauzeitenplan-verzug/SKILL.md) | Für Bauzeitenplan und Verzug: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/bauzeitenplan-verzug/SKILL.md) |
| [`drei-dokumente-paket-erzeugen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/drei-dokumente-paket-erzeugen/SKILL.md) | Für Drei-Dokumente-Paket erzeugen: ordnet Akte, Belege und Lücken; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/drei-dokumente-paket-erzeugen/SKILL.md) |
| [`faelligkeitsmitteilung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/faelligkeitsmitteilung-pruefen/SKILL.md) | Für Fälligkeitsmitteilung prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/faelligkeitsmitteilung-pruefen/SKILL.md) |
| [`fall-fingerabdruck-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/fall-fingerabdruck-erstellen/SKILL.md) | Für Fall-Fingerabdruck erstellen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/fall-fingerabdruck-erstellen/SKILL.md) |
| [`fertigstellungssicherheit-650m-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/fertigstellungssicherheit-650m-pruefen/SKILL.md) | Für Fertigstellungssicherheit Paragraf 650m Absatz 2 BGB prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/fertigstellungssicherheit-650m-pruefen/SKILL.md) |
| [`gemeinschaft-zieht-maengelrechte-an-sich`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/gemeinschaft-zieht-maengelrechte-an-sich/SKILL.md) | Für Gemeinschaft zieht Mängelrechte an sich: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/gemeinschaft-zieht-maengelrechte-an-sich/SKILL.md) |
| [`gesamtnichtigkeit-paragraf-306-bgb`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/gesamtnichtigkeit-paragraf-306-bgb/SKILL.md) | Für Gesamtnichtigkeit Paragraf 306 BGB: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/gesamtnichtigkeit-paragraf-306-bgb/SKILL.md) |
| [`hoai-bauueberwachung-private-bauueberwachung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/hoai-bauueberwachung-private-bauueberwachung/SKILL.md) | Für HOAI, Bauüberwachung und private Bauüberwachung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/hoai-bauueberwachung-private-bauueberwachung/SKILL.md) |
| [`insolvenzrisiken-bautraeger`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/insolvenzrisiken-bautraeger/SKILL.md) | Für Insolvenzrisiken Bauträger: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/insolvenzrisiken-bautraeger/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Bauträgervertragsprüfer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/juristischer-argumentationskern/SKILL.md) |
| [`mabv-ratenplan-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mabv-ratenplan-pruefen/SKILL.md) | Für MaBV-Ratenplan prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mabv-ratenplan-pruefen/SKILL.md) |
| [`mabv-sicherheit-paragraf-7-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mabv-sicherheit-paragraf-7-pruefen/SKILL.md) | Für MaBV-Sicherheit Paragraf 7 prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mabv-sicherheit-paragraf-7-pruefen/SKILL.md) |
| [`maengelrechte-633-634-bgb`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/maengelrechte-633-634-bgb/SKILL.md) | Für Mängelrechte Paragrafen 633 und 634 BGB: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/maengelrechte-633-634-bgb/SKILL.md) |
| [`mandantengutachten-aufbau`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mandantengutachten-aufbau/SKILL.md) | Für Mandantengutachten Aufbau: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mandantengutachten-aufbau/SKILL.md) |
| [`mittlere-art-und-guete-und-din`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mittlere-art-und-guete-und-din/SKILL.md) | Für Mittlere Art und Güte und DIN-Normen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/mittlere-art-und-guete-und-din/SKILL.md) |
| [`notarbelehrung-paragraf-14-bnoto-17-beurkg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/notarbelehrung-paragraf-14-bnoto-17-beurkg/SKILL.md) | Für Notarbelehrung Paragraf 14 BNotO und Paragraf 17 BeurkG: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/notarbelehrung-paragraf-14-bnoto-17-beurkg/SKILL.md) |
| [`paragraf-308-nr-4-bgb-leistungsaenderung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/paragraf-308-nr-4-bgb-leistungsaenderung/SKILL.md) | Für Leistungsänderungsvorbehalte Paragraf 308 Nummer 4 BGB: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/paragraf-308-nr-4-bgb-leistungsaenderung/SKILL.md) |
| [`paragraf-309-nr-12-bgb-tatsachenbestaetigung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/paragraf-309-nr-12-bgb-tatsachenbestaetigung/SKILL.md) | Für Paragraf 309 Nummer 12 BGB — Tatsachenbestätigung und Beweislast: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/paragraf-309-nr-12-bgb-tatsachenbestaetigung/SKILL.md) |
| [`preisanpassung-und-sonderwuensche`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/preisanpassung-und-sonderwuensche/SKILL.md) | Für Preisanpassung und Sonderwünsche: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/preisanpassung-und-sonderwuensche/SKILL.md) |
| [`teilungserklaerung-gemeinschaftsordnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/teilungserklaerung-gemeinschaftsordnung/SKILL.md) | Für Teilungserklärung und Gemeinschaftsordnung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/teilungserklaerung-gemeinschaftsordnung/SKILL.md) |
| [`verbraucherstatus-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/verbraucherstatus-pruefen/SKILL.md) | Für Verbraucherstatus prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/verbraucherstatus-pruefen/SKILL.md) |
| [`verjaehrung-634a-bgb-hemmung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/verjaehrung-634a-bgb-hemmung/SKILL.md) | Berechnet die Verjährung von Bauträger- und Bauwerksmängelansprüchen nach Paragraf 634a BGB und prüft Abnahme, Arglist, Verhandlungen sowie Rechtsverfolgung; erstellt einen belegten Fristenkalender ohne Scheinsicherheit durch interne Bes... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/verjaehrung-634a-bgb-hemmung/SKILL.md) |
| [`weg-beschluss-anfechtung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/weg-beschluss-anfechtung/SKILL.md) | Für WEG-Beschluss-Anfechtung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/weg-beschluss-anfechtung/SKILL.md) |
| [`wohnflaeche-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/wohnflaeche-pruefen/SKILL.md) | Für Wohnfläche prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertragspruefer/skills/wohnflaeche-pruefen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

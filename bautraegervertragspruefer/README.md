# Bauträgervertragspruefer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prüft deutsche Bauträgerverträge: MaBV-Ratenplan und Sicherheiten, Paragrafen 650u und 650v BGB, AGB-Kontrolle, Baubeschreibung, Abnahme Gemeinschaftseigentum, Bauzeit, Preisanpassung, Teilungserklärung. Liefert Mandantengutachten und Aufforderungsschreiben an Bauträger und Notar.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`bautraegervertragspruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/bautraegervertragspruefer/bautraegervertragspruefer-werkstatt.md" download><code>bautraegervertragspruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/bautraegervertragspruefer/bautraegervertragspruefer-schnellstart.md" download><code>bautraegervertragspruefer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`bautraegervertragspruefer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer-testakte.zip), [`bautraegervertragspruefer-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen deutschen Bauträgervertrag verbraucherseitig prüfen: Ratenplan, Sicherheiten, Baubeschreibung, Abnahme, Bauzeit, Preisanpassung, Teilungserklaerung — und am Ende ein Gutachten plus ein Aufforderungsschreiben an Bauträger und Notar in der Hand haben.

**Schwester-Plugin:** [`bautraegervertrag-pruefer`](../bautraegervertrag-pruefer) (mit Bindestrich) deckt dasselbe Mandat mit einzeln ladbaren Spezial-Skills samt references-Workflow ab; dieses Plugin hier bietet Megaprompt-Original und zwei Testakten. Für ein Mandat genügt eines von beiden.

## Wenn du das brauchst

- **Verbraucher** hat einen Bauträgervertrag erhalten und will vor der notariellen Beurkundung wissen, welche Klauseln unwirksam sind und welche Streichungen er fordern muss.
- **Fachanwalt für Bau- und Architektenrecht** prüft einen Bauträgervertrag im Mandat und braucht eine vollständige Klauselmatrix mit MaBV-Prüfung und AGB-Kontrolle.
- **Notar** will den Entwurf gegen die Pflichten aus Paragraf 14 BNotO und gegen die MaBV-Schutzstruktur durchsehen.
- **Finanzierende Bank** prüft den Vertrag auf Auszahlungsrisiken nach dem Ratenplan und auf die Werthaltigkeit der Sicherheiten.

## Was du am Ende in der Hand hast

Eine Klauselmatrix Satz für Satz mit Ampel-Einschaetzung (rot, orange, gruen), ein Mandantengutachten mit paragraphenbezogener Begründung, ein Aufforderungsschreiben an Bauträger und Notar mit konkreter richtiger Fassung pro beanstandeter Klausel sowie eine Verhandlungsstrategie mit Gegenargument-Antwort.

## Der Weg dorthin

Vertrag und Anlagen einlesen → Fall-Fingerabdruck erstellen (Parteien, Einheit, Projekt, Preis, Ratenplan, Sicherheiten) → MaBV-Ratenplan und Sicherheiten prüfen → AGB-Kontrolle Klausel für Klausel → Baubeschreibung gegen Bausoll und anerkannte Regeln der Technik halten → Abnahme Gemeinschaftseigentum und Schlussrate prüfen → Bauzeit, Preisanpassung, Teilungserklaerung kontrollieren → Mandantengutachten und Aufforderungsschreiben ausgeben.

## Workflows

Drei Modi zur Wahl:

- **Schnellpruefung**: Top-Zehn-Auffaelligkeiten, geschaetztes Risikoprofil, Empfehlung in wenigen Saetzen.
- **Vollpruefung**: Fall-Fingerabdruck, Klauselmatrix, AGB-Kontrolle, MaBV-Prüfung, Mandantengutachten.
- **Verhandlungspfad**: Vollpruefung plus Aufforderungsschreiben an Bauträger und Notar mit konkreter richtiger Fassung pro Klausel und Verhandlungsstrategie.

## Was dich aufhält

- **MaBV-Ratenplan**: Überhoehte Vorleistungen, falsche Verteilung der Raten auf Bauabschnitte, fehlende Sicherheit nach Paragraf 7 MaBV.
- **Verbraucherbauvertrag**: Paragrafen 650u und 650v BGB, Baubeschreibung als Pflichtinhalt, verbindliche Angabe zum Bauzeitende.
- **AGB-Kontrolle**: Notarielle Beurkundung schliesst AGB-Kontrolle nicht aus; geltungserhaltende Reduktion findet bei unwirksamen Verbraucher-AGB nicht statt.
- **Abnahme Gemeinschaftseigentum**: Verklammerung der Abnahme mit der Schlussrate gefaehrdet die werthaltige Sicherung.
- **Baubeschreibung**: Pauschale Verweise auf anerkannte Regeln der Technik ohne konkrete Spezifikation lassen das Bausoll offen.

## Rechtlicher Anker

- Paragrafen 650u und 650v BGB (Bauträgervertrag, Baubeschreibung)
- Paragrafen 305 bis 310 BGB (AGB-Kontrolle)
- Makler- und Bauträgerverordnung (MaBV), insbesondere Paragrafen 3, 7
- Paragraf 14 BNotO (Belehrungspflichten Notar)
- Wohnungseigentumsgesetz (Teilungserklaerung, Abnahme Gemeinschaftseigentum)
- HOAI (Leistungsphasen Objektueberwachung)
- BGH-Leitentscheidungen zu Bauträgervertrag, MaBV und Abnahmeklauseln (im Werkstatt-Prompt ausführlich)

## Hinweise

Generischer Pruefstand, alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer prüft den Pruefbericht auf Plausibilität und Eignung im konkreten Einzelfall. Keine Rechtsberatung. Keine Garantie für Vollständigkeit oder Aktualität der Rechtsprechung. Bei streitigen Fällen Fachanwalt für Bau- und Architektenrecht oder Notar hinzuziehen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 2. Unterlagen, Sachverhalt und Quellen | `drei-dokumente-paket-erzeugen`, `mandantengutachten-aufbau` |
| 3. Prüfung, Anspruch und Subsumtion | `verbraucherstatus-pruefen` |
| 4. Gestaltung, Strategie und Verhandlung | `agb-kontrolle-klauseln`, `bautraegervertrag-qualifikation`, `bauzeitenplan-verzug`, `mabv-ratenplan-pruefen` |
| 5. Verfahren, Behörde und Gericht | `weg-beschluss-anfechtung` |
| 6. Ergebnis, Schreiben und Kommunikation | `aufforderungsschreiben-bautraeger-und-notar` |
| 8. Spezialmodule und Schnittstellen | `abnahme-gemeinschaftseigentum`, `abnahme-sondereigentum-paragraf-640`, `auflassungsvormerkung-und-grundbuch`, `baubeschreibung-bausoll-pruefen`, `faelligkeitsmitteilung-pruefen`, `fall-fingerabdruck-erstellen`, `fertigstellungssicherheit-650m-pruefen`, `gemeinschaft-zieht-maengelrechte-an-sich`, `gesamtnichtigkeit-paragraf-306-bgb`, `hoai-bauueberwachung-private-bauueberwachung`, `insolvenzrisiken-bautraeger`, `mabv-sicherheit-paragraf-7-pruefen`, `maengelrechte-633-634-bgb`, `mittlere-art-und-guete-und-din`, `notarbelehrung-paragraf-14-bnoto-17-beurkg`, `paragraf-308-nr-4-bgb-leistungsaenderung`, `paragraf-309-nr-12-bgb-tatsachenbestaetigung`, `preisanpassung-und-sonderwuensche`, ... plus 3 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abnahme-gemeinschaftseigentum` | Wenn es um Abnahme Gemeinschaftseigentum in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `abnahme-sondereigentum-paragraf-640` | Wenn es um Abnahme Sondereigentum Paragraf 640 BGB in Bauträgervertragspruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `agb-kontrolle-klauseln` | Wenn es um AGB-Kontrolle Klauseln in Bauträgervertragspruefer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aufforderungsschreiben-bautraeger-und-notar` | Wenn es um Aufforderungsschreiben an Bauträger und Notar in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `auflassungsvormerkung-und-grundbuch` | Wenn es um Auflassungsvormerkung und Grundbuch in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baubeschreibung-bausoll-pruefen` | Wenn es um Baubeschreibung und Bausoll prüfen in Bauträgervertragspruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bautraegervertrag-qualifikation` | Wenn es um Bauträgervertrag-Qualifikation in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bauzeitenplan-verzug` | Wenn es um Bauzeitenplan und Verzug in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `drei-dokumente-paket-erzeugen` | Wenn es um Drei-Dokumente-Paket erzeugen in Bauträgervertragspruefer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `faelligkeitsmitteilung-pruefen` | Wenn es um Fälligkeitsmitteilung prüfen in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fall-fingerabdruck-erstellen` | Wenn es um Fall-Fingerabdruck erstellen in Bauträgervertragspruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `fertigstellungssicherheit-650m-pruefen` | Wenn es um Fertigstellungssicherheit Paragraf 650m Absatz 2 BGB prüfen in Bauträgervertragspruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkt... |
| `gemeinschaft-zieht-maengelrechte-an-sich` | Wenn es um Gemeinschaft zieht Mängelrechte an sich in Bauträgervertragspruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| `gesamtnichtigkeit-paragraf-306-bgb` | Wenn es um Gesamtnichtigkeit Paragraf 306 BGB in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hoai-bauueberwachung-private-bauueberwachung` | Wenn es um HOAI, Bauüberwachung und private Bauüberwachung in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `insolvenzrisiken-bautraeger` | Wenn es um Insolvenzrisiken Bauträger in Bauträgervertragspruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `mabv-ratenplan-pruefen` | Wenn es um MaBV-Ratenplan prüfen in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mabv-sicherheit-paragraf-7-pruefen` | Wenn es um MaBV-Sicherheit Paragraf 7 prüfen in Bauträgervertragspruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem S... |
| `maengelrechte-633-634-bgb` | Wenn es um Mängelrechte Paragrafen 633 und 634 BGB in Bauträgervertragspruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| `mandantengutachten-aufbau` | Wenn es um Mandantengutachten Aufbau in Bauträgervertragspruefer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `mittlere-art-und-guete-und-din` | Wenn es um Mittlere Art und Güte und DIN-Normen in Bauträgervertragspruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächste... |
| `notarbelehrung-paragraf-14-bnoto-17-beurkg` | Wenn es um Notarbelehrung Paragraf 14 BNotO und Paragraf 17 BeurkG in Bauträgervertragspruefer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfr... |
| `paragraf-308-nr-4-bgb-leistungsaenderung` | Wenn es um Leistungsänderungsvorbehalte Paragraf 308 Nummer 4 BGB in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `paragraf-309-nr-12-bgb-tatsachenbestaetigung` | Wenn es um Paragraf 309 Nummer 12 BGB — Tatsachenbestätigung und Beweislast in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `preisanpassung-und-sonderwuensche` | Wenn es um Preisanpassung und Sonderwünsche in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `teilungserklaerung-gemeinschaftsordnung` | Wenn es um Teilungserklärung und Gemeinschaftsordnung in Bauträgervertragspruefer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und n... |
| `verbraucherstatus-pruefen` | Wenn es um Verbraucherstatus prüfen in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verjaehrung-634a-bgb-hemmung` | Wenn es um Verjährung Paragraf 634a BGB und Hemmung in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `weg-beschluss-anfechtung` | Wenn es um WEG-Beschluss-Anfechtung in Bauträgervertragspruefer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `wohnflaeche-pruefen` | Wenn es um Wohnfläche prüfen in Bauträgervertragspruefer geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

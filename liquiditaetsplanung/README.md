<!-- decimal-headings -->

[Oberordner Insolvenzrecht – alle eigenständigen Plugins nach Aufgabe](../insolvenzrecht-plugins/README.md)

<!-- decimal-anchor --> <a id="liquiditätsplanung--power-plugin"></a>

# 1. Liquiditätsplanung — Power-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
<!-- decimal-anchor --> <a id="was-ist-das-hier"></a>

Aktueller Quellenabgleich: [geprüfte Entscheidungen, Anwendung und Grenzen vom 15. November 2026](references/rechtsprechungsabgleich-2026-11-15.md).

## 1.1. Was ist das hier?

Liquiditätsplanung nach deutschem Recht: 3-Wochen-Vorschau, 13/26/52-Wochen-Forecast, Excel-Export, Quote/Lücken-Ampel, Dokumentationspaket und Schnittstellen zu Fortbestehensprognose und Insolvenzrecht. Rechtsprechung nur nach Live-Verifikation.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

<!-- decimal-anchor --> <a id="welche-datei-wofür--which-file-should-i-use"></a>

## 1.2. Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`liquiditaetsplanung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.2/liquiditaetsplanung.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/liquiditaetsplanung.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/liquiditaetsplanung-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/liquiditaetsplanung-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/liquiditaetsplanung.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

<!-- decimal-anchor --> <a id="in-30-sekunden-starten"></a>

## 1.3. In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/liquiditaetsplanung.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Liquiditätsplanung — Power-Plugin:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

<!-- decimal-anchor --> <a id="downloads"></a>

## 1.4. Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`liquiditaetsplanung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.2/liquiditaetsplanung.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`liquiditaetsplanung-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/liquiditaetsplanung-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`liquiditaetsplanung-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/liquiditaetsplanung-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

<!-- decimal-anchor --> <a id="zugeordnete-testakten"></a>

## 1.5. Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Edelholz Manufaktur Berlin GmbH — Liquiditäts- und Steuerakte](../testakten/edelholz-manufaktur-berlin-liquiditaet/README.md) | [Gesamt-PDF](../testakten/edelholz-manufaktur-berlin-liquiditaet/gesamt-pdf/edelholz-manufaktur-berlin-liquiditaet_gesamt.pdf) | [`testakte-edelholz-manufaktur-berlin-liquiditaet.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-pflegerecht-v1.0.0/testakte-edelholz-manufaktur-berlin-liquiditaet.zip) | [`testakte-edelholz-manufaktur-berlin-liquiditaet-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-edelholz-manufaktur-berlin-liquiditaet-einzelpdfs.zip) |
| [Forschungszulage Riedblick Sensorik GmbH](../testakten/forschungszulage-sensorik-startup-taunus/README.md) | [Gesamt-PDF](../testakten/forschungszulage-sensorik-startup-taunus/gesamt-pdf/forschungszulage-sensorik-startup-taunus_gesamt.pdf) | [`testakte-forschungszulage-sensorik-startup-taunus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-pflegerecht-v1.0.0/testakte-forschungszulage-sensorik-startup-taunus.zip) | [`testakte-forschungszulage-sensorik-startup-taunus-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-forschungszulage-sensorik-startup-taunus-einzelpdfs.zip) |
| [Fortbestehensprognose Paragrafix GmbH](../testakten/fortbestehensprognose-paragrafix-gmbh/README.md) | [Gesamt-PDF](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf) | [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-pflegerecht-v1.0.0/testakte-fortbestehensprognose-paragrafix-gmbh.zip) | [`testakte-fortbestehensprognose-paragrafix-gmbh-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-fortbestehensprognose-paragrafix-gmbh-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine belastbare Liquiditätsplanung aufstellen und drohende Zahlungsunfähigkeit frühzeitig erkennen.
**Eigenständiges Power-Plugin** für wochenaktuelle Liquiditätsvorschauen nach deutschem Recht (§§ 17, 18, 19 InsO; § 1 StaRUG; BGH-Schema Passiva II). Funktioniert allein. Ergänzt sich optional mit `insolvenzrecht` und `steuerrecht-anwalt-und-berater`, hängt aber nicht von ihnen ab.

---

<!-- decimal-anchor --> <a id="was-ist-drin"></a>

## 1.6. Was ist drin

Die wichtigsten Fachrouten innerhalb der 74 Fachmodulen und 12 auswählbaren Skills:

| Skill | Arbeitsprodukt | Maßgeblicher Zeitraum |
| --- | --- | --- |
| `liquiditaetsvorschau-3wochen` | Belegte Planung mit getrenntem Stichtagsstatus und rechtlicher Einordnung. | Tatsächlicher Stichtag und kalendergenaues Dreiwochenfenster. |
| `liquiditaetsvorschau-insolvenzrechtlich` | Status/Bilanz, Nachweismethode, Indizien und begründete Subsumtion. | Stichtags- und verfahrensbezogen. |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Vorschau mit Fortbestehens- und Sanierungsprüfung im beauftragten Umfang. | Operativ 13/26/52 Wochen; § 19 zwölf Kalendermonate; § 18 in aller Regel 24 Monate. |
| `idw-s6-integrierte-sanierungsplanung` | Verbindung zu GuV, Planbilanz, Maßnahmen und nachhaltiger Sanierungsfähigkeit. | Dem konkreten Sanierungsauftrag entsprechend. |

<!-- decimal-anchor --> <a id="ergebnisse-und-datenquellen"></a>

## 1.7. Ergebnisse und Datenquellen

Das beauftragte Format geht vor. Für eine bearbeitbare Planung steht die [Excel-Vorlage](assets/excel/Liquiditaetsplan-Wochenbasis.xlsx) bereit. Das [HTML-Rechenblatt](assets/padlet/liquiditaets-padlet.html) und die [Markdown-Vorlage](assets/markdown/liquiditaets-artefakt-vorlage.md) unterstützen bei Bedarf weitere Arbeitsweisen. Ohne Tabellenexport wird eine nachvollziehbare Tabelle geliefert; eine nicht erzeugte Datei wird nicht behauptet.

Vorliegende Bankauszüge, OPOS, Kredit- und Stundungsunterlagen zuerst auswerten. Betrag, Fälligkeit, Zahlungstag, Verfügbarkeit und Belegstelle verbinden; OCR-Zahlen und Salden kontrollieren. Nur entscheidende Lücken erfragen und Antworten in Rechnung und beauftragtem Dokument verarbeiten. Bankzugänge nur verwenden, wenn verfügbar und entsprechend autorisiert.

<!-- decimal-anchor --> <a id="insolvenzrechtliche-prüfung"></a>

## 1.8. Insolvenzrechtliche Prüfung

Die operative Wochenrechnung bleibt Anfangsbestand plus Einzahlungen minus Auszahlungen. Daneben stehen vier getrennte Statusfelder für Aktiva I/II und Passiva I/II. Passiva I werden nicht aus sämtlichen Ausgaben der ersten Kalenderwoche abgeleitet; Zahlungen auf Altschulden dürfen nicht nochmals als neue Passiva II erscheinen.

Bei der zeitraumbezogenen Bilanzmethode gilt `Lücke = max(0, PI + PII − AI − AII)` und `Quote = Lücke / (PI + PII)`, sofern der Nenner positiv ist. Das vollständige Dreiwochenfenster und unterwöchige Fälligkeiten müssen stimmen. Tabellen und Rechenfarben ersetzen keine rechtliche Entscheidung. Unbekannte Eingaben sind nicht null; ein leeres Rechenblatt bedeutet keine Entwarnung.

Die [Prüfregeln zu §§ 17–19 InsO](references/insolvenzpruefung.md) behandeln insbesondere:

- Zehnprozentregel mit beiden Ausnahmen und Zahlungseinstellung als eigenständigen Nachweisweg; keine automatische Entscheidung aus der Zahl von Warnzeichen.
- Unterschied zwischen Wochenplan, Stichtagsstatus, Liquiditätsbilanz und anderen zulässigen Darlegungswegen.
- Streitige Verbindlichkeiten und Vollstreckungstitel; eigene Forderungen werden nicht durch einen Titel sofort zu Liquidität.
- Zwölfmonats-Fortbestehensprognose, eigenständigen Überschuldungsstatus und in aller Regel 24 Monate für drohende Zahlungsunfähigkeit.
- Rangrücktritt nach konkretem Wortlaut und Finanzierung ohne pauschale Gleichsetzung von weichem Patronat, einklagbarem Anspruch und tatsächlichem Zufluss.
- Objektiven Eintritt, Antragsfristen und Aktualisierung nach neuen Belegen.

<!-- decimal-anchor --> <a id="geprüfte-rechtsprechung-und-abgleich"></a>

## 1.9. Geprüfte Rechtsprechung und Abgleich

**Prüfstand 28.09.2026:** Die fünf im überlassenen Fachkapitel genannten Urteile – IX ZR 123/04, IX ZR 228/03, II ZR 88/16, IX ZR 133/14 und II ZR 84/20 – sind in Datum, Aktenzeichen und Themenzuordnung bestätigt. Hinzu kommen sechs bereits relevante neuere Entscheidungen zu Nachweismethoden, Indizien, Darlegung und Titeln. Die [Entscheidungskarte](references/rechtsprechung/INDEX.md) führt **elf Entscheidungen**, ihre amtlichen Volltexte und genaue Anwendungsgrenzen sowie den ergänzenden Berichtigungsbeschluss auf.

Die Überlegungen zu Belegen, rollierender Planung, gezielten Rückfragen, Szenarien und Weiterarbeit waren weitgehend vorhanden. Präzisiert wurden insbesondere die Insolvenzmethodik, die Behandlung von Rangrücktritt und Drittmitteln sowie die Rechenhilfen. Werkstatt und Mini wurden entsprechend aktualisiert; die Skillzahl bleibt unverändert. Der Mini bleibt unter 7.500 UTF-8-Bytes.

Der [Prüfbericht mit drei ausgearbeiteten Grenzfällen und Rechentests](../quality/liquiditaetsplanung/abgleich-2026-09-28/README.md) trennt Quellenabgleich, redaktionelle Prüfung und tatsächlich ausgeführte Tests.

Ein Wochenetikett wie „KW 22“ legt allein keinen taggenauen Eintritt fest. Negatives handelsbilanzielles Eigenkapital, verrechnet mit einem Darlehen, ist kein vollständiger Überschuldungsstatus. Das Fachkapitel wird nicht als Arbeitsakte oder Originaldatei mitveröffentlicht.

<!-- decimal-anchor --> <a id="lizenz"></a>

## 1.10. Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- decimal-anchor --> <a id="quellen-disclaimer"></a>

## 1.11. Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **12 auswählbare Skills**. Die **74 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

<!-- decimal-anchor --> <a id="orientierung-nach-arbeitslogik"></a>

## 1.12. Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/juristischer-argumentationskern/SKILL.md), [`liquiditaetsvorschau-3-6-12-monate`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/liquiditaetsvorschau-3-6-12-monate/SKILL.md), [`liquiditaetsvorschau-3wochen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/liquiditaetsvorschau-3wochen/SKILL.md), [`liquiditaetsvorschau-insolvenzrechtlich`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/liquiditaetsvorschau-insolvenzrechtlich/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Datenbasis, Konten und Liquiditätsstatus | [`status-daten-konten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/status-daten-konten-bearbeiten/SKILL.md) |
| 3. Rollierende Planung und Szenarien | [`rollierende-planung-szenarien-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/rollierende-planung-szenarien-bearbeiten/SKILL.md) |
| 4. Finanzierung, Cash Pool und Stundung | [`finanzierung-cashpool-stundung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/finanzierung-cashpool-stundung-bearbeiten/SKILL.md) |
| 5. Insolvenzreife, Fortbestehen und Sanierung | [`insolvenzreife-fortbestehen-sanierung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/insolvenzreife-fortbestehen-sanierung-bearbeiten/SKILL.md) |
| 6. Bankbericht, Kommunikation und Export | [`bankbericht-kommunikation-export-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/bankbericht-kommunikation-export-bearbeiten/SKILL.md) |
| 7. Planungsqualität und Quellenkontrolle | [`planung-qualitaet-quellen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/planung-qualitaet-quellen-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

<!-- decimal-anchor --> <a id="alle-skills-im-überblick"></a>

## 1.13. Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 12 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 12 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`bankbericht-kommunikation-export-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/bankbericht-kommunikation-export-bearbeiten/SKILL.md) | Ergebnisse als prüfbare Tabellen, Bankbericht und verständliche Mandantenentscheidung ausgeben. Die vollständigen Fachanweisungen werden passend zum konkreten Vorgang gelesen und gemeinsam umgesetzt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/bankbericht-kommunikation-export-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Liquiditätsplanung — Power. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/einstieg-routing/SKILL.md) |
| [`finanzierung-cashpool-stundung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/finanzierung-cashpool-stundung-bearbeiten/SKILL.md) | Kreditlinien, Leasing, Cash Pool, Debitorenmaßnahmen und Zahlungsvereinbarungen auf Verfügbarkeit und Wirkung prüfen. Die vollständigen Fachanweisungen werden passend zum konkreten Vorgang gelesen und gemeinsam umgesetzt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/finanzierung-cashpool-stundung-bearbeiten/SKILL.md) |
| [`insolvenzreife-fortbestehen-sanierung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/insolvenzreife-fortbestehen-sanierung-bearbeiten/SKILL.md) | Finanzplanung von Insolvenzreifestatus und Fortbestehensprognose trennen und notwendige Sanierungsschritte ableiten. Die vollständigen Fachanweisungen werden passend zum konkreten Vorgang gelesen und gemeinsam umgesetzt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/insolvenzreife-fortbestehen-sanierung-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Liquiditätsplanung ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/juristischer-argumentationskern/SKILL.md) |
| [`liquiditaetsvorschau-3-6-12-monate`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/liquiditaetsvorschau-3-6-12-monate/SKILL.md) | Erstellt rollierende Liquiditätspläne über 13 bis 52 Wochen und grenzt die Fortbestehensprognose nach Paragraf 19 InsO von der Prognose nach Paragraf 18 InsO ab. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/liquiditaetsvorschau-3-6-12-monate/SKILL.md) |
| [`liquiditaetsvorschau-3wochen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/liquiditaetsvorschau-3wochen/SKILL.md) | Erstellt eine Dreiwochenplanung und einen belegten Status zur Prüfung der Zahlungsunfähigkeit. Trennt Zahlungsbedarf, Datenlücken, Indizien und rechtliche Bewertung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/liquiditaetsvorschau-3wochen/SKILL.md) |
| [`liquiditaetsvorschau-insolvenzrechtlich`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/liquiditaetsvorschau-insolvenzrechtlich/SKILL.md) | Prüft Zahlungsunfähigkeit aus Status, Liquiditätsbilanz oder Zahlungseinstellung mit Belegen und Gegenargumenten. Grenzt Überschuldung, Prognose und Antragspflichten ab. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/liquiditaetsvorschau-insolvenzrechtlich/SKILL.md) |
| [`planung-qualitaet-quellen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/planung-qualitaet-quellen-bearbeiten/SKILL.md) | Beleglücken, Fristen, Annahmen, Berechnungsfehler und rechtliche Quellen vor Freigabe kontrollieren. Die vollständigen Fachanweisungen werden passend zum konkreten Vorgang gelesen und gemeinsam umgesetzt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/planung-qualitaet-quellen-bearbeiten/SKILL.md) |
| [`rollierende-planung-szenarien-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/rollierende-planung-szenarien-bearbeiten/SKILL.md) | Einzahlungen, Auszahlungen, Saisonalität und Sonderaufträge in einer rollierenden Wochen- und Monatsplanung berechnen. Die vollständigen Fachanweisungen werden passend zum konkreten Vorgang gelesen und gemeinsam umgesetzt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/rollierende-planung-szenarien-bearbeiten/SKILL.md) |
| [`status-daten-konten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/status-daten-konten-bearbeiten/SKILL.md) | Banken, offene Posten, Fälligkeiten und Quellenbelege zu einer belastbaren Ausgangsbasis abstimmen. Die vollständigen Fachanweisungen werden passend zum konkreten Vorgang gelesen und gemeinsam umgesetzt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/status-daten-konten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Liquiditätsplanung — Power. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=liquiditaetsplanung/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

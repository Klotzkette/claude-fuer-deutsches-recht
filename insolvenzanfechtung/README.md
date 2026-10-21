# Insolvenzanfechtung

[Startseite](../README.md) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/insolvenzanfechtung.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Prüfen Sie Zahlungen, Sicherheiten und Vertragsgestaltungen aus Sicht der Insolvenzverwaltung oder des Anfechtungsgegners. Das Plugin führt von der Akte über die belegte Zahlungskette und die passenden Tatbestände zum ausformulierten Prüfvermerk, Forderungsschreiben, zur Klage, Klageerwiderung oder zum Vergleich. Es richtet sich an anwaltliche und insolvenzrechtliche Facharbeit.

Beginnen Sie mit den vorhandenen Unterlagen und einem konkreten Auftrag. Der Hauptskill übernimmt bekannte Angaben und fragt nur nach entscheidenden Lücken. Zehn Fachskills bearbeiten die jeweils benötigten Teilfragen; sie werden nicht als starre Pflichtliste abgerufen. Die eigenständigen Prompts funktionieren auch ohne Installation, wenn die gewählte Oberfläche die notwendigen Unterlagen lesen kann. Ein tatsächlicher Zugriff auf Dateien, Internetquellen oder Versanddienste wird nicht vorausgesetzt oder behauptet.

## 1. Einstieg und Downloads

Startsatz:

> Prüfen Sie die Rückforderung anhand der beigefügten Verträge, Kontoauszüge und Nachrichten aus Sicht des Empfängers. Ordnen Sie jede Zahlung, prüfen Sie Gegenleistung und Kenntnis und erstellen Sie eine ausformulierte Antwort. Fragen Sie nur nach den für das Ergebnis entscheidenden fehlenden Unterlagen.

Version: **1.0.0**. Rechtsquellenprüfung: **21.10.2026**. Änderungen stehen im [Changelog](CHANGELOG.md); die [Originalquellenreferenz](references/rechtsquellen.md) erläutert Aussage und Grenze jedes Entscheidungsankers.

| Bestandteil | Zweck | Zugang |
| --- | --- | --- |
| Plugin | Elf installierbare Skills und Referenzen | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.0.0/insolvenzanfechtung.zip) · [Portables ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.0.0/insolvenzanfechtung-portable.zip) |
| Werkstatt | Ausführlicher eigenständiger Gesamtworkflow | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-werkstatt.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.0.0/insolvenzanfechtung-werkstatt.pdf) |
| Schnellstart | Kompakter eigenständiger Einstieg | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-schnellstart.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.0.0/insolvenzanfechtung-schnellstart.pdf) |
| Hauptproblem | Gläubigerwechsel, Empfängerzuordnung und Verteidigung | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-hauptproblem.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-hauptproblem.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.0.0/insolvenzanfechtung-hauptproblem.pdf) |

Die Prompts sind eigenständige Arbeitsdateien. Das Plugin installiert keine Testakten und versendet keine E-Mails. Die verfügbaren Funktionen von Claude Cowork, Claude Code, Codex und ChatGPT hängen von der jeweiligen Umgebung ab; ein konkreter Skill lässt sich ausdrücklich als Auftrag wählen. Befehlsdateien sind zusätzliche Einstiegshilfen und müssen nicht in jeder Oberfläche als Menü erscheinen.

## 2. Elf Skills

| Skill | Arbeitsprodukt |
| --- | --- |
| [Zahlungsketten und Krisenbelege rekonstruieren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/zahlungskette-und-belege/SKILL.md) | Liefert eine belegte Vorgangsmatrix mit offenen Zuordnungen für die Insolvenzanfechtung |
| [Rechtshandlung, Zeitpunkt und Gläubigerbenachteiligung prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtshandlung-zeit-benachteiligung/SKILL.md) | Trennt Antrag, Eröffnung und Wirksamkeit; liefert einen belegten Ausgangsvermerk und die passende Anfechtungsroute |
| [Kongruente und inkongruente Deckung unterscheiden](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/deckung-pruefen/SKILL.md) | Unterscheidet kongruente und inkongruente Deckung und erstellt eine vorgangsbezogene Anspruchs- oder Verteidigungsmatrix |
| [Benachteiligungsvorsatz und Empfängerkenntnis würdigen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/vorsatz-und-kenntnis/SKILL.md) | Prüft Raten, Sanierung und Krisenwissen ohne automatischen Schluss aus Zahlungsunfähigkeit; liefert ein belastbares Vorsatzmemo |
| [Unentgeltlichkeit und Dreiecksverhältnisse auflösen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/unentgeltlichkeit-dreieck/SKILL.md) | Rekonstruiert Leistungsbeziehungen, Forderungswert und Gegenleistung aus Empfängersicht; liefert eine begründete Dreiecksanalyse und konkrete Beweisfragen |
| [Gesellschafterdarlehen und Finanzierungshilfen prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/gesellschafterfinanzierung/SKILL.md) | Klärt Beteiligung, Einfluss, Regress und Ausnahmen; liefert eine Finanzierungschronologie mit Anspruchs- und Verteidigungsvarianten |
| [Sicherheiten, Verrechnung und Aufrechnung untersuchen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/sicherheiten-aufrechnung/SKILL.md) | Trennt Entstehung, Werthaltigkeit, Erwerb und Verwertung; liefert einen Sicherheitenvermerk mit nachvollziehbarem Massevergleich |
| [Bargeschäft und unmittelbaren Leistungsaustausch prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/bargeschaeft-pruefen/SKILL.md) | Ordnet Lieferung, Vorkasse, Arbeitsentgelt und Verrechnung einzeln zu; liefert einen belastbaren Austauschvermerk |
| [Rückgewähr, Gegenleistung und Verjährung berechnen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtsfolgen-verjaehrung/SKILL.md) | Trennt Anspruchsentstehung, Kenntnis und Hemmung; liefert eine belegte Forderungsrechnung mit konkretem Handlungsbedarf |
| [Anfechtungsansprüche durchsetzen, abwehren und vergleichen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/prozess-und-vergleich/SKILL.md) | Ordnet Streitgegenstände, Bestreiten und Beweise zu; trennt Rechtsrisiko, Wirtschaftlichkeit und menschliche Freigabe |
| [Insolvenzanfechtung vom Akteneingang bis zum Endprodukt steuern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/anfechtung-steuern/SKILL.md) | Verbindet zehn Fachrouten, führt Vorgänge und Belege fort und liefert das bestellte Memo, Schreiben, den Schriftsatz oder Vergleich mit nachvollziehbaren Grenzen |

## 3. Rechtsprüfung mit belastbaren Grenzen

Die Prüfung trennt Rechtshandlung, zeitliche Zuordnung, objektive Benachteiligung, besondere Tatbestände und Rechtsfolgen. Eine Krise ist kein automatischer Vorsatzbeweis; eine Drittzahlung ist nicht automatisch unentgeltlich; ein Ratenplan beantwortet nicht alle Kenntnisfragen. Gegenleistung, werthaltige Sicherheiten und entlastende Kommunikation werden gleichrangig erfasst.

Die Referenz berücksichtigt amtlich gelesene Entscheidungen bis 2026. Insbesondere wird das EuGH-Verfahren C-43/25 nicht als noch offene Vorlage dargestellt. Entscheidungen enthalten jeweils „Trägt“ und „Trägt nicht“. Nicht zugängliche Quellen oder ungeklärte Tatsachen bleiben ausdrücklich offen. Das Plugin erfindet keine Randnummern und leitet aus einem Präzedenzfall keine allgemeine Bindung anderer Gerichte ab.

[Arbeitsweise](references/arbeitsweise.md) · [Zitierweise](references/zitierweise.md) · [Übergaben und Belegstruktur](references/belege-und-uebergaben.md)

## 4. Drei Testakten

Die Fälle liegen getrennt im zentralen Testaktenordner. Die jeweiligen README-Seiten enthalten Gesamt-PDF, Einzel-PDFs und Originaldateien sowie die genaue Aufgabenbeschreibung. Sie können zunächst nur Aktenunterlagen bereitstellen und die Prüfhinweise für die spätere Auswertung zurückhalten.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Testakte | Schwerpunkt | Zugang |
| --- | --- | --- |
| Fintech-Darlehen und Vertragsübernahme, Bremen | Gläubigerwechsel, Zustimmung, Zahlungsweg und Empfängerzuordnung | [Akte und Downloads](../testakten/fintech-darlehen-vertragsuebernahme-bremen/README.md) |
| Blechliebe Bamberg | Ratenplan, alte Rückstände, Neulieferung, Bargeschäft und wechselndes Krisenwissen | [Akte und Downloads](../testakten/insolvenzanfechtung-blechliebe-bamberg/README.md) |
| Faltenwurf Fürth | Familie, Gesellschafterfinanzierung, Sicherung, Minderheitsbeteiligung und Bankgarantie | [Akte und Downloads](../testakten/insolvenzanfechtung-faltenwurf-fuerth/README.md) |

[Übungswege und Auswertung](references/testakten-und-arbeitsauftraege.md) erläutern, welche Produkte aus den Unterlagen entstehen sollen. Die Akten sind fiktiv; ihre Tatsachen und eingebauten Vorprüfungen sind keine Rechtsquellen.

## 5. Freigaben und Fachanwaltsanschluss

Interne Sichtung, Quellenabgleich, Berechnung und Entwurf laufen innerhalb des Auftrags weiter. Versand, Einreichung, Anerkenntnis, Verzicht und Vergleichsannahme benötigen eine konkrete menschliche Freigabe für Person, Fassung und Handlung. Ein erzeugter Entwurf gilt nicht als versandt. Für Endprodukte gelten vollständige Ausformulierung, dezimale Gliederung und soweit technisch möglich Times New Roman, 11 pt.

Im [Fachanwaltsplugin Insolvenz- und Sanierungsrecht](../fachanwalt-insolvenz-sanierungsrecht/README.md) liegen zusätzlich [Werkstatt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=fachanwalt-insolvenz-sanierungsrecht/prompts/insolvenzanfechtung/insolvenzanfechtung-werkstatt.md) und [Mini-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=fachanwalt-insolvenz-sanierungsrecht/prompts/insolvenzanfechtung/insolvenzanfechtung-schnellstart.md) ausschließlich zur Insolvenzanfechtung. Der allgemeine fachanwaltliche Prompt bleibt daneben erhalten.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anfechtung-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/anfechtung-steuern/SKILL.md) | Steuert die vollständige Insolvenzanfechtung aus Verwalter- oder Empfängersicht. Verbindet zehn Fachrouten, führt Vorgänge und Belege fort und liefert das bestellte Memo, Schreiben, den Schriftsatz oder Vergleich mit nachvollziehbaren Gr... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/anfechtung-steuern/SKILL.md) |
| [`bargeschaeft-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/bargeschaeft-pruefen/SKILL.md) | Prüft unmittelbare und gleichwertige Gegenleistung sowie Unlauterkeit bei der Bargeschäftsausnahme. Ordnet Lieferung, Vorkasse, Arbeitsentgelt und Verrechnung einzeln zu; liefert einen belastbaren Austauschvermerk. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/bargeschaeft-pruefen/SKILL.md) |
| [`deckung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/deckung-pruefen/SKILL.md) | Prüft die Deckungsanfechtung anhand von Anspruch, Fälligkeit, Leistungsart, Zeitraum und Empfängerwissen. Unterscheidet kongruente und inkongruente Deckung und erstellt eine vorgangsbezogene Anspruchs- oder Verteidigungsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/deckung-pruefen/SKILL.md) |
| [`gesellschafterfinanzierung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/gesellschafterfinanzierung/SKILL.md) | Prüft Darlehen, darlehensgleiche Forderungen, Sicherheiten und Rückzahlungen mit Gesellschafterbezug. Klärt Beteiligung, Einfluss, Regress und Ausnahmen; liefert eine Finanzierungschronologie mit Anspruchs- und Verteidigungsvarianten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/gesellschafterfinanzierung/SKILL.md) |
| [`prozess-und-vergleich`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/prozess-und-vergleich/SKILL.md) | Erstellt aus belegten Anfechtungsvorgängen Forderungsschreiben, Klagen, Erwiderungen und Vergleichsentwürfe. Ordnet Streitgegenstände, Bestreiten und Beweise zu; trennt Rechtsrisiko, Wirtschaftlichkeit und menschliche Freigabe. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/prozess-und-vergleich/SKILL.md) |
| [`rechtsfolgen-verjaehrung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtsfolgen-verjaehrung/SKILL.md) | Berechnet Rückgewähr und Nebenforderungen, prüft Gegenleistung, Rechtsnachfolge und Verjährung. Trennt Anspruchsentstehung, Kenntnis und Hemmung; liefert eine belegte Forderungsrechnung mit konkretem Handlungsbedarf. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtsfolgen-verjaehrung/SKILL.md) |
| [`rechtshandlung-zeit-benachteiligung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtshandlung-zeit-benachteiligung/SKILL.md) | Prüft die konkrete Rechtshandlung, ihre zeitliche Einordnung und die Gläubigerbenachteiligung. Trennt Antrag, Eröffnung und Wirksamkeit; liefert einen belegten Ausgangsvermerk und die passende Anfechtungsroute. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtshandlung-zeit-benachteiligung/SKILL.md) |
| [`sicherheiten-aufrechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/sicherheiten-aufrechnung/SKILL.md) | Analysiert Sicherungsrechte, Kontokorrent, Aufrechnungslagen und Verrechnungen. Trennt Entstehung, Werthaltigkeit, Erwerb und Verwertung; liefert einen Sicherheitenvermerk mit nachvollziehbarem Massevergleich. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/sicherheiten-aufrechnung/SKILL.md) |
| [`unentgeltlichkeit-dreieck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/unentgeltlichkeit-dreieck/SKILL.md) | Prüft unentgeltliche Leistungen und Zahlungen auf fremde Schulden. Rekonstruiert Leistungsbeziehungen, Forderungswert und Gegenleistung aus Empfängersicht; liefert eine begründete Dreiecksanalyse und konkrete Beweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/unentgeltlichkeit-dreieck/SKILL.md) |
| [`vorsatz-und-kenntnis`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/vorsatz-und-kenntnis/SKILL.md) | Würdigt Benachteiligungsvorsatz und Empfängerkenntnis anhand zeitbezogener Indizien und Gegenindizien. Prüft Raten, Sanierung und Krisenwissen ohne automatischen Schluss aus Zahlungsunfähigkeit; liefert ein belastbares Vorsatzmemo. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/vorsatz-und-kenntnis/SKILL.md) |
| [`zahlungskette-und-belege`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/zahlungskette-und-belege/SKILL.md) | Rekonstruiert Zahlungen, Vertragswechsel, Empfänger und Krisenwissen aus Bankdaten, Buchhaltung und Schriftverkehr. Liefert eine belegte Vorgangsmatrix mit offenen Zuordnungen für die Insolvenzanfechtung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/zahlungskette-und-belege/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

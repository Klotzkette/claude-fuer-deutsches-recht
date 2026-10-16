# 1. GVB Reinigungsvergabe

Reinigungsaufträge im Berliner Nahverkehr vorbereiten und das Vergabeverfahren führen: fünf Skills erstellen die Unterlagen, fünf bearbeiten Bewerbungen, Angebote, Rügen, Zuschlag und Nachprüfung. Die zehn Skills entsprechen den zehn Arbeitsschritten der eigenständigen GVB-Workflow-Vorlage; sie sind hier als installierbares Plugin mit gezielten Eingaben, Beispielen und vollständigen Dokumentausgaben aufbereitet.

[Hauptübersicht](../README.md) · [Alle Skills](../SKILLS.md) · [Skills dieses Plugins](../skills-index/gvb-reinigungsvergabe.md) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md) · [Plugin-Dateien](.)

## 1.1. Schnell beginnen

Plugin installieren und den vorhandenen Auftrag samt Unterlagen übergeben. „Prüfe das LV und das Preisblatt auf Widersprüche“ beginnt bei A4. „Die Kammermitteilung liegt im Ordner; bereite die Erwiderung vor“ beginnt bei B5. Für eine neue Ausschreibung ist A1 der Einstieg. Ein bereits geklärter Auftrag wird nicht nochmals vollständig abgefragt.

Die [zehn ursprünglichen Markdown-Assistenten](../weitere-unterlagen/sektorenvergabe-gvb-berlin/README.md) bleiben unverändert und unabhängig nutzbar. Dort liegt auch das separate Beispielprojekt zum Aufbau verketteter Arbeitsabläufe. Das allgemeine [Sektorenvergabe-Plugin](../sektorenvergabe-workflow/README.md) bleibt ebenfalls bestehen.

## 1.2. Installation und alternative Prompts

| Fassung | Zweck | Download |
| --- | --- | --- |
| Plugin | Zehn Skills und örtlich zugeordnete Referenzen; Marketplace-Eintrag `gvb-reinigungsvergabe` | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe.zip) |
| Portables Plugin | Derselbe Inhalt mit umschließendem Plugin-Ordner | [Portables ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-portable.zip) |
| Werkstatt | Ausführlicher eigenständiger Ablauf von Bedarf bis Nachprüfung | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/gvb-reinigungsvergabe-werkstatt.md" download>Werkstatt-Prompt als Markdown</a> |
| Schnellstart | Kompakter eigenständiger Ablauf unter 7.500 Zeichen und Bytes | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/gvb-reinigungsvergabe-schnellstart.md" download>Mini-Prompt als Markdown</a> |

Die Prompt-Links laden die aktuellen Arbeitsfassungen herunter. Fest versionierte Markdown-Dateien stehen daneben im [Komponentenrelease 1.0.0](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/gvb-reinigungsvergabe-v1.0.0) bereit.

Werkstatt und Schnellstart sind Alternativen zur Plugin-Nutzung, keine zusätzlichen Skills. Die Plugin-ZIPs enthalten weder die beiden Promptdateien noch die Akte. Eine Installation lädt die Unterlagen daher nicht ungefragt in einen Fall. Jeder Fachskill enthält seine tragenden Anweisungen selbst; Referenzen werden nur bei Bedarf gelesen.

## 1.3. Die zehn Skills

Die alphabetischen Skillnamen beginnen mit ihrer fachlichen Schrittnummer. A1 bis A5 bilden die Vorbereitung. B1 wird nach Bewerbungen und nach Angeboten verwendet. B2 kann jederzeit dazukommen, B5 bei tatsächlicher Nachprüfung. Ein Hauptablauf ist in A1 integriert; es gibt keinen elften Startskill.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`a1-reinigungsauftrag-und-vergabeverfahren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a1-reinigungsauftrag-und-vergabeverfahren/SKILL.md) | Ordnet Reinigungsbedarf eines Berliner Verkehrsunternehmens nach Sektorenbezug, Losen und Auftragswert ein. Erstellt Vergabevermerk und Terminplan; Einstieg vor Veröffentlichung oder bei noch ungeklärtem Verfahrensweg. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a1-reinigungsauftrag-und-vergabeverfahren/SKILL.md) |
| [`a2-reinigungsleistung-und-mengen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a2-reinigungsleistung-und-mengen/SKILL.md) | Erstellt Leistungsbeschreibung, objektbezogenes Leistungsverzeichnis und Mengenherleitung für Stations-, Fahrzeug- und Betriebsraumreinigung. Klärt Sperrfenster, Flächenabgrenzung und abrechenbare Sonderleistungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a2-reinigungsleistung-und-mengen/SKILL.md) |
| [`a3-eignung-wertung-reinigungsvertrag`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a3-eignung-wertung-reinigungsvertrag/SKILL.md) | Gestaltet Eignungsnachweise, transparente Preis- und Qualitätswertung und vollständige Reinigungsverträge. Verknüpft Berliner Tarifvorgaben mit Nachtarbeit, Vertretung, Versicherung und kontrollierbarer Abrechnung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a3-eignung-wertung-reinigungsvertrag/SKILL.md) |
| [`a4-unterlagen-und-preisblatt-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a4-unterlagen-und-preisblatt-abgleichen/SKILL.md) | Prüft Reinigungsvergabeunterlagen auf Widersprüche zwischen Mengen, Zeitfenstern, Vertrag, Preisblatt und Bekanntmachung. Rechnet Positionen und Optionen nach und liefert berichtigte Fassungen mit Freigabeübersicht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a4-unterlagen-und-preisblatt-abgleichen/SKILL.md) |
| [`a5-bekanntmachung-fristen-veroeffentlichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a5-bekanntmachung-fristen-veroeffentlichen/SKILL.md) | Bereitet Bekanntmachung, nachvollziehbare Vergabefristen und Portalbereitstellung einer Reinigungsvergabe vor. Trennt eForms-Entwurf von nachgewiesener Veröffentlichung und prüft tatsächliche Zugänglichkeit. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a5-bekanntmachung-fristen-veroeffentlichen/SKILL.md) |
| [`b1-bewerbungen-angebote-nachfordern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b1-bewerbungen-angebote-nachfordern/SKILL.md) | Prüft Teilnahmeanträge und Angebote für Reinigungsleistungen auf Eingang, Eignung, Form und Nachforderbarkeit. Erstellt bieterspezifische Nachforderungen, Zulassungsvermerke und begründete Ablehnungsentwürfe. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b1-bewerbungen-angebote-nachfordern/SKILL.md) |
| [`b2-bieterfragen-ruegen-berichtigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b2-bieterfragen-ruegen-berichtigen/SKILL.md) | Bearbeitet Rückfragen und Rügen in der Reinigungsvergabe einschließlich verkürzter Sperrfenster und Flächenkorrekturen. Erstellt Antworten, Abhilfe oder Nichtabhilfe und prüft Fristverlängerung sowie Neubeginn. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b2-bieterfragen-ruegen-berichtigen/SKILL.md) |
| [`b3-angebote-verhandeln-werten-preispruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b3-angebote-verhandeln-werten-preispruefen/SKILL.md) | Führt zulässige Verhandlungen und beleggestützte Wertung von Reinigungsangeboten. Prüft niedrige Stunden- und Gesamtpreise, Vertretung und Nachtfenster; liefert Gesprächsprotokolle, Preisaufklärung und Wertungsvermerk. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b3-angebote-verhandeln-werten-preispruefen/SKILL.md) |
| [`b4-vorabinformation-zuschlag-uebergabe`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b4-vorabinformation-zuschlag-uebergabe/SKILL.md) | Erstellt individuelle Vorabinformationen und Zuschlagsunterlagen für Reinigungsaufträge. Prüft Wartefristen, Bindefrist und Nachprüfungssperren und bereitet Schlüssel-, Personal- und Objektübergabe vor. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b4-vorabinformation-zuschlag-uebergabe/SKILL.md) |
| [`b5-nachpruefung-berlin-fortsetzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b5-nachpruefung-berlin-fortsetzen/SKILL.md) | Bearbeitet Nachprüfungsverfahren zur Berliner Reinigungsvergabe mit Aktenvorlage, Erwiderung und Schutz von Geschäftsgeheimnissen. Prüft Rüge-, Beschwerdefristen und Zuschlagssperren und führt in die zulässige Verfahrensfortsetzung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b5-nachpruefung-berlin-fortsetzen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

Nach jedem Schritt stehen Arbeitsergebnis, offene Punkte, Frist und nächster Schritt fest. Bei einer Rückfrage wartet die Folge auf die Antwort; nach deren Eingang wird gezielt weitergearbeitet. Eine Übergabe ersetzt niemals die Freigabe für Veröffentlichung, Ablehnung, Einreichung oder Zuschlag. [Ablauf und Zuordnung](references/ablauf.md).

## 1.4. Reinigungsakte GVB Berlin

Los 1 einer Reinigungsvergabe für Stationen und Betriebsräume: Bedarfsanmeldung, Aufmaß, Vertragsentwurf, Preisblatt, Bewerbungen, drei Angebote, Verhandlung, Preisaufklärung, Rüge und Nachprüfungsantrag. 48 Originalunterlagen, 48 einzelne PDFs und 51 Gesamtseiten. Die ergänzten Unterlagen behandeln tatsächliche Zugangsprobleme, Geräteraum und Schlüssel, Verhandlungsprotokolle, Aktenübermittlung und Geheimnisschutz. Ausgang und Wertung bleiben offen.

Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.

This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF mit Lesezeichen | [Gesamt-PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/GVB_Reinigungsvergabe_Gesamt.pdf) |
| Flaches ZIP mit 48 Einzel-PDFs | [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/GVB_Reinigungsvergabe_Einzel_PDFs.zip) |
| Flaches ZIP mit 25 DOCX, 13 EML, 6 CSV und 4 TXT | [Originalunterlagen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/GVB_Reinigungsvergabe_Originale.zip) |

Die Akte bleibt nur einmal im [eigenständigen Projekt](../weitere-unterlagen/sektorenvergabe-gvb-berlin/README.md) gepflegt. Für einen Durchlauf ab Beginn nur die Unterlagen des damaligen Zeitstands verwenden. Spätere Mitteilungen dürfen frühere Entscheidungen nicht rückwirkend beeinflussen. Aussagen der Beteiligten sind keine Musterlösung. Kontakte verwenden reservierte `.example`-Adressen.

## 1.5. Rechtsstand und Grenzen

Punktuell amtlich gelesen am 16.10.2026: [Paragraf 169 GWB](https://www.gesetze-im-internet.de/gwb/__169.html), [Paragraf 173 GWB](https://www.gesetze-im-internet.de/gwb/__173.html) und [Paragraf 187 Absatz 2 GWB](https://www.gesetze-im-internet.de/gwb/__187.html). Nach neuem Recht endet bei Zurückweisung durch die Vergabekammer das Zuschlagsverbot mit Bekanntgabe; die sofortige Beschwerde hemmt dann nicht automatisch. Für vor dem 01.07.2026 begonnene Vergabe- und erfasste Nachprüfungsverfahren bleibt das Übergangsrecht entscheidend. Kein neuer Vollabgleich Berliner Formulare oder sämtlicher Rechtsprechungsanker.

Ausgangsstand Oktober 2026; Verfahrensbeginn, GWB-Übergangsrecht und Berliner Formularfassung werden gesondert geprüft. Normen und europäische Anker stehen in den Skills. Berliner Entscheidungen sind nur mit überprüftem Volltext tragend zu verwenden. [Quellenstand und Abrufgrenzen](references/quellenstand.md).

Das Plugin bereitet Unterlagen und Entscheidungen vor. Es besitzt keinen eingebauten Zugang zur Vergabeplattform, keine Veröffentlichungsbefugnis und keinen automatischen Zugriff auf lizenzierte Rechtsdatenbanken. Struktur- und Paketprüfungen ersetzen keinen Live-Test in einer fremden Oberfläche und keine fachliche Einzelfallprüfung.

## 1.6. English Overview

Ten coordinated skills support a Berlin transport operator's cleaning procurement: five prepare tender documents, five manage participation, offers, complaints, award and review proceedings. The original ten portable Markdown assistants remain unchanged in the separate example project. Use the skill matching the current procedural stage; questions pause the sequence until answered. External submissions and awards require explicit human authorization. The expanded case is available above as a combined PDF, individual PDFs and native documents.

# 1. GVB Reinigungsvergabe

Reinigungsaufträge im Berliner Nahverkehr vorbereiten und das Vergabeverfahren führen: fünf Skills erstellen die Unterlagen, fünf bearbeiten Bewerbungen, Angebote, Rügen, Zuschlag und Nachprüfung. Die zehn Skills entsprechen den zehn Arbeitsschritten der eigenständigen GVB-Workflow-Vorlage; sie sind hier als installierbares Plugin mit gezielten Eingaben, Beispielen und vollständigen Dokumentausgaben aufbereitet.

## 1.1. Schnell beginnen

Plugin installieren und den vorhandenen Auftrag samt Unterlagen übergeben. „Prüfe das LV und das Preisblatt auf Widersprüche“ beginnt bei A4. „Die Kammermitteilung liegt im Ordner; bereite die Erwiderung vor“ beginnt bei B5. Für eine neue Ausschreibung ist A1 der Einstieg. Ein bereits geklärter Auftrag wird nicht nochmals vollständig abgefragt.

Die [zehn ursprünglichen Markdown-Assistenten](../weitere-unterlagen/sektorenvergabe-gvb-berlin/README.md) bleiben unverändert und unabhängig nutzbar. Dort liegt auch das separate Beispielprojekt zum Aufbau verketteter Arbeitsabläufe. Das allgemeine [Sektorenvergabe-Plugin](../sektorenvergabe-workflow/README.md) bleibt ebenfalls bestehen.

## 1.2. Installation und alternative Prompts

| Fassung | Zweck | Download |
| --- | --- | --- |
| Plugin | Zehn Skills und örtlich zugeordnete Referenzen; Marketplace-Eintrag `gvb-reinigungsvergabe` | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe.zip) |
| Portables Plugin | Derselbe Inhalt mit umschließendem Plugin-Ordner | [Portables ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-portable.zip) |
| Werkstatt | Ausführlicher eigenständiger Ablauf von Bedarf bis Nachprüfung | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-werkstatt.md" download>Werkstatt-Prompt als Markdown</a> |
| Schnellstart | Kompakter eigenständiger Ablauf unter 7.500 Zeichen und Bytes | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-schnellstart.md" download>Mini-Prompt als Markdown</a> |

Aktuelle Arbeitsfassungen direkt herunterladen: <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/gvb-reinigungsvergabe-werkstatt.md" download>Werkstatt als Markdown</a> und <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/gvb-reinigungsvergabe-schnellstart.md" download>Schnellstart als Markdown</a>. Die obigen Release-Dateien behalten ihren veröffentlichten Stand.

Werkstatt und Schnellstart sind Alternativen zur Plugin-Nutzung, keine zusätzlichen Skills. Die Plugin-ZIPs enthalten weder die beiden Promptdateien noch die Akte. Eine Installation lädt die Unterlagen daher nicht ungefragt in einen Fall. Jeder Fachskill enthält seine tragenden Anweisungen selbst; Referenzen werden nur bei Bedarf gelesen.

## 1.3. Die zehn Skills

Die alphabetischen Skillnamen beginnen mit ihrer fachlichen Schrittnummer. A1 bis A5 bilden die Vorbereitung. B1 wird nach Bewerbungen und nach Angeboten verwendet. B2 kann jederzeit dazukommen, B5 bei tatsächlicher Nachprüfung. Ein Hauptablauf ist in A1 integriert; es gibt keinen elften Startskill.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->
| Skill | Inhalt | Einzelner Skill |
| --- | --- | --- |
| [`a1-reinigungsauftrag-und-vergabeverfahren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a1-reinigungsauftrag-und-vergabeverfahren/SKILL.md) | A1: Ordnet Reinigungsbedarf eines Berliner Verkehrsunternehmens nach Sektorenbezug, Losen und Auftragswert ein. Erstellt Vergabevermerk und Terminplan; Einstieg vor Veröffentlichung oder bei noch ungeklärtem Verfahrensweg. | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-a1-reinigungsauftrag-und-vergabeverfahren.md" download>Markdown herunterladen</a> |
| [`a2-reinigungsleistung-und-mengen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a2-reinigungsleistung-und-mengen/SKILL.md) | A2: Erstellt Leistungsbeschreibung, objektbezogenes Leistungsverzeichnis und Mengenherleitung für Stations-, Fahrzeug- und Betriebsraumreinigung. Klärt Sperrfenster, Flächenabgrenzung und abrechenbare Sonderleistungen. | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-a2-reinigungsleistung-und-mengen.md" download>Markdown herunterladen</a> |
| [`a3-eignung-wertung-reinigungsvertrag`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a3-eignung-wertung-reinigungsvertrag/SKILL.md) | A3: Gestaltet Eignungsnachweise, transparente Preis- und Qualitätswertung und vollständige Reinigungsverträge. Verknüpft Berliner Tarifvorgaben mit Nachtarbeit, Vertretung, Versicherung und kontrollierbarer Abrechnung. | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-a3-eignung-wertung-reinigungsvertrag.md" download>Markdown herunterladen</a> |
| [`a4-unterlagen-und-preisblatt-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a4-unterlagen-und-preisblatt-abgleichen/SKILL.md) | A4: Prüft Reinigungsvergabeunterlagen auf Widersprüche zwischen Mengen, Zeitfenstern, Vertrag, Preisblatt und Bekanntmachung. Rechnet Positionen und Optionen nach und liefert berichtigte Fassungen mit Freigabeübersicht. | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-a4-unterlagen-und-preisblatt-abgleichen.md" download>Markdown herunterladen</a> |
| [`a5-bekanntmachung-fristen-veroeffentlichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/a5-bekanntmachung-fristen-veroeffentlichen/SKILL.md) | A5: Bereitet Bekanntmachung, nachvollziehbare Vergabefristen und Portalbereitstellung einer Reinigungsvergabe vor. Trennt eForms-Entwurf von nachgewiesener Veröffentlichung und prüft tatsächliche Zugänglichkeit. | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-a5-bekanntmachung-fristen-veroeffentlichen.md" download>Markdown herunterladen</a> |
| [`b1-bewerbungen-angebote-nachfordern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b1-bewerbungen-angebote-nachfordern/SKILL.md) | B1: Prüft Teilnahmeanträge und Angebote für Reinigungsleistungen auf Eingang, Eignung, Form und Nachforderbarkeit. Erstellt bieterspezifische Nachforderungen, Zulassungsvermerke und begründete Ablehnungsentwürfe. | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-b1-bewerbungen-angebote-nachfordern.md" download>Markdown herunterladen</a> |
| [`b2-bieterfragen-ruegen-berichtigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b2-bieterfragen-ruegen-berichtigen/SKILL.md) | B2: Bearbeitet Rückfragen und Rügen in der Reinigungsvergabe einschließlich verkürzter Sperrfenster und Flächenkorrekturen. Erstellt Antworten, Abhilfe oder Nichtabhilfe und prüft Fristverlängerung sowie Neubeginn. | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-b2-bieterfragen-ruegen-berichtigen.md" download>Markdown herunterladen</a> |
| [`b3-angebote-verhandeln-werten-preispruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b3-angebote-verhandeln-werten-preispruefen/SKILL.md) | B3: Führt zulässige Verhandlungen und beleggestützte Wertung von Reinigungsangeboten. Prüft niedrige Stunden- und Gesamtpreise, Vertretung und Nachtfenster; liefert Gesprächsprotokolle, Preisaufklärung und Wertungsvermerk. | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-b3-angebote-verhandeln-werten-preispruefen.md" download>Markdown herunterladen</a> |
| [`b4-vorabinformation-zuschlag-uebergabe`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b4-vorabinformation-zuschlag-uebergabe/SKILL.md) | B4: Erstellt individuelle Vorabinformationen und Zuschlagsunterlagen für Reinigungsaufträge. Prüft Wartefristen, Bindefrist und Nachprüfungssperren und bereitet Schlüssel-, Personal- und Objektübergabe vor. | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-b4-vorabinformation-zuschlag-uebergabe.md" download>Markdown herunterladen</a> |
| [`b5-nachpruefung-berlin-fortsetzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gvb-reinigungsvergabe/skills/b5-nachpruefung-berlin-fortsetzen/SKILL.md) | B5: Bearbeitet Nachprüfungsverfahren zur Berliner Reinigungsvergabe mit Aktenvorlage, Erwiderung und Schutz von Geschäftsgeheimnissen. Prüft Rüge-, Beschwerdefristen und Zuschlagssperren und führt in die zulässige Verfahrensfortsetzung. | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gvb-reinigungsvergabe-v1.0.0/gvb-reinigungsvergabe-b5-nachpruefung-berlin-fortsetzen.md" download>Markdown herunterladen</a> |
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

Ausgangsstand Oktober 2026; Verfahrensbeginn, GWB-Übergangsrecht und Berliner Formularfassung werden gesondert geprüft. Normen und europäische Anker stehen in den Skills. Berliner Entscheidungen sind nur mit überprüftem Volltext tragend zu verwenden. [Quellenstand und Abrufgrenzen](references/quellenstand.md).

Das Plugin bereitet Unterlagen und Entscheidungen vor. Es besitzt keinen eingebauten Zugang zur Vergabeplattform, keine Veröffentlichungsbefugnis und keinen automatischen Zugriff auf lizenzierte Rechtsdatenbanken. Struktur- und Paketprüfungen ersetzen keinen Live-Test in einer fremden Oberfläche und keine fachliche Einzelfallprüfung.

## 1.6. English Overview

Ten coordinated skills support a Berlin transport operator's cleaning procurement: five prepare tender documents, five manage participation, offers, complaints, award and review proceedings. The original ten portable Markdown assistants remain unchanged in the separate example project. Use the skill matching the current procedural stage; questions pause the sequence until answered. External submissions and awards require explicit human authorization. The expanded case is available above as a combined PDF, individual PDFs and native documents.

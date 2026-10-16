# Strafvollzug in der JVA

[Hauptübersicht](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/README.md) · [Alle Skills](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/SKILLS.md) · [Skills dieses Plugins](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/skills-index/strafvollzug-jva.md) · [Download-Index](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/ASSET_INDEX.md) · [Testakten](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/README.md) · [Plugin-Dateien](.)

Das Plugin bearbeitet konkrete Anliegen im Strafvollzug aus der jeweils gewählten Perspektive: Gefangene, Angehörige mit eigener Berechtigung oder Vertretungsmacht, Rechtsanwälte, Justiziar einer Anstalt oder Gericht. Es führt von vorhandenen Unterlagen über Landesrecht, Beweise und Fristen zu einem ausformulierten Antrag, Bescheidentwurf, gerichtlichen Antrag oder Entscheidungsentwurf. Menschenwürde, individuelle Lebenslagen und belastbar begründete Sicherheitsbelange werden zusammen geprüft.

Gefangene bleiben Grundrechtsträger. Das historische „besondere Gewaltverhältnis“ ist keine heutige Grundlage für Grundrechtsbeschränkungen. Ein Gerichtsentwurf wird nicht als erlassene Entscheidung ausgegeben; eine Anstaltsstellungnahme bleibt Parteivortrag, solange das Gericht sie nicht geprüft hat.

**Version 1.0.1 · fachlicher Prüfstand 16.10.2026 · zehn Fachskills und ein Hauptskill.**

## 1. Installieren und sofort beginnen

[Claude-Plugin herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/strafvollzug-jva-v1.0.1/strafvollzug-jva.zip) · [Portables Paket herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/strafvollzug-jva-v1.0.1/strafvollzug-jva-portable.zip)

Claude Code und kompatible Claude-Cowork-Umgebungen können das Pluginpaket mit Skills und Befehlen verwenden. Codex erhält zusätzlich ein eigenes Manifest sowie das portable Manifest. In ChatGPT lässt sich der Schnellstart als Projektanweisung mit Werkstatt und Referenzen als Projektdateien verwenden. Import, Dateizugriff und Darstellung der Befehle hängen von der jeweiligen Umgebung ab; ein plattformübergreifender Live-Import ist damit nicht behauptet.

Ein geeigneter Einstieg lautet: „Ich vertrete die gefangene Person. Prüfen Sie diesen Ablehnungsbescheid und erstellen Sie den passenden Antrag mit Anlagen. Das ist Erwachsenenstrafhaft in Berlin.“ Vorhandene Angaben werden übernommen; nur entscheidende Lücken werden nachgefragt. Alternativ genügt zunächst die Bitte um eine verständliche Erklärung des Bescheids.

## 2. Durchgehender Arbeitsablauf

1. Auftrag, Rolle, Vollzugsart, Bundesland und gewünschtes Produkt bestimmen.
2. Entscheidung, schriftliche Bekanntgabe, tatsächliche Unterbringung und Anlagen lesen.
3. Akute Gefahren und gerichtliche Fristen sichern, ohne einen noch unbekannten Zugang zu erfinden.
4. Die geltende Landesnorm, Grundrechte und konkrete Tatsachen miteinander prüfen.
5. Sachgerechte Alternativen und Gegenargumente der anderen Seite ausarbeiten.
6. Das bestellte Dokument vollständig formulieren und Anlagen nachvollziehbar zuordnen.
7. Offene Belege, zuständige Person, nächsten Schritt und führende Fassung festhalten; neue Antworten gezielt einarbeiten.

Interne Beschwerde, Aufsichtseingabe und gerichtlicher Antrag werden getrennt behandelt. Die Zweiwochenfrist des ersten Antrags, die besonderen Regeln bei Unterlassen und die Monatsfrist samt qualifizierter Form der Rechtsbeschwerde werden nicht verwechselt. Die tatsächliche Gerichtsübermittlung bleibt nachzuweisen. Das Plugin versendet keine Nachrichten und reicht keine Anträge von sich aus ein.

## 3. Elf Skills

| Skill | Arbeitsprodukt |
|---|---|
| [Den konkreten Vollzugsfall steuern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/strafvollzug-fall-steuern/SKILL.md) | Fallplan und vollständiges beauftragtes Produkt |
| [Grundrechte und Gleichbehandlung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/grundrechte-gleichbehandlung-pruefen/SKILL.md) | Einzelfallprüfung mit Belegen und milderen Mitteln |
| [Besuche, Familie und Kommunikation](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/besuch-kommunikation-gestalten/SKILL.md) | Besuchs- oder Kommunikationsantrag |
| [Ernährung und Religionsausübung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/ernaehrung-religion-beruecksichtigen/SKILL.md) | Belegter Verpflegungs- oder Religionsantrag |
| [Gesundheit, Haftraum und Aufenthalt im Freien](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/gesundheit-unterbringung-pruefen/SKILL.md) | Versorgungs- und Unterbringungsprüfung |
| [Bildung, Arbeit und Computer](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/bildung-arbeit-digitalzugang-pruefen/SKILL.md) | Bildungsplan, Geräteprüfung und Antrag |
| [Vollzugsplan und Lockerungen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/vollzugsplan-lockerungen-pruefen/SKILL.md) | Individuelle Prognose und abgestufter Maßnahmenplan |
| [Sicherung, Disziplin und Verhältnismäßigkeit](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/sicherheit-disziplin-kontrollieren/SKILL.md) | Prüfung von Anlass, Dauer und Kontrolle |
| [Anträge und begründete Bescheide](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/antraege-bescheide-bearbeiten/SKILL.md) | Ausformulierter Antrag oder Bescheidentwurf |
| [Gerichtlicher Rechtsschutz und Eilverfahren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/gerichtlichen-rechtsschutz-fuehren/SKILL.md) | Hauptsache- und gegebenenfalls Eilantrag |
| [Entlassung und Übergang](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/entlassung-uebergang-planen/SKILL.md) | Übergangsplan mit tatsächlichen Zusagen |

## 4. Werkstatt, Mini-Prompt und Hauptproblem

Die drei Prompts sind eigenständig nutzbar. Mini und Hauptproblem bleiben jeweils unter 7.500 UTF-8-Bytes. Markdown und Text sind inhalts- und byteidentisch; die PDFs sind Lesefassungen. Formatstandard für erzeugte Schriftsätze: Times New Roman 11 pt.

- **Große Werkstatt mit 24 Kapiteln und thematischen Entscheidungsankern:** [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/strafvollzug-jva-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/strafvollzug-jva-werkstatt.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/strafvollzug-jva-v1.0.1/strafvollzug-jva-werkstatt.pdf)
- **Mini-Prompt in neun klaren Arbeitsschritten:** [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/strafvollzug-jva-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/strafvollzug-jva-schnellstart.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/strafvollzug-jva-v1.0.1/strafvollzug-jva-schnellstart.pdf)
- **Hauptproblem-Prompt:** [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/strafvollzug-jva-hauptproblem.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/strafvollzug-jva-hauptproblem.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/strafvollzug-jva-v1.0.1/strafvollzug-jva-hauptproblem.pdf)

Die Werkstatt verbindet die Rechtsprechung mit Tatsachenfragen, Belegprüfung, Gegenargumenten, milderen Mitteln und dem nächsten ausformulierten Arbeitsprodukt. Der Mini-Prompt trennt Auftrag, Landesrecht, Fristen, Belege, Anliegen, Dokument, Eilrechtsschutz, Quellen und Endfassung in kurze lesbare Schritte.

Befehle: `/jva-fall`, `/jva-antrag`, `/jva-bescheid`, `/jva-eilrechtsschutz` und `/jva-pruefung`. Sie führen zum jeweils passenden Skill; sie ersetzen keine konkrete Rollenklärung.

## 5. Vier lebensnahe Testakten

Jede Akte enthält 16 einzeln bearbeitbare Originale: vier Word-Dokumente, sechs PDFs, fünf E-Mail-Dateien und eine Excel-Arbeitsmappe. Die vier Fälle ergeben 64 Arbeitsdateien. Enthalten sind persönliche Anliegen, Belege, nachvollziehbare Gegenpositionen der Anstalt und ein ausführlicher gerichtlicher Parteientwurf mit Anlagen. Die Arbeitsmappen erklären Chronologie, Belege und Datumsabstände. E-Mails stammen von den jeweils tatsächlich kommunizierenden Personen; ein allgemeiner freier E-Mail-Zugang für Gefangene wird nicht vorausgesetzt.

Alle Personen, Einrichtungen und Fallumstände sind erfunden. Die Akten geben keine realen Vorwürfe gegen tatsächliche Justizvollzugsanstalten wieder. Die Übungsannahmen zur gerichtlichen Zuständigkeit ersetzen keine Prüfung der realen Anstalt und Abteilung.

- [Yusuf Bender: Kinderbesuch und passende Ernährung in Berlin](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/jva-berlin-besuch-ernaehrung/README.md): Originaldateien, Einzel-PDFs und zusammenhängende PDF-Akte.
- [Mara Wendel: Rollator, Privatsphäre und nutzbarer Hofgang in Nordrhein-Westfalen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/jva-nrw-unterbringung-gesundheit/README.md): Originaldateien, Einzel-PDFs und zusammenhängende PDF-Akte.
- [Korbinian Seidel: Weiterbildung mit einem kontrollierbaren Offline-Computer in Bayern](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/jva-bayern-bildung-computer/README.md): Originaldateien, Einzel-PDFs und zusammenhängende PDF-Akte.
- [Samira Hartung: Ausbildung, Familie und abgestufte Lockerungen in Niedersachsen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/jva-niedersachsen-lockerungen-familie/README.md): Originaldateien, Einzel-PDFs und zusammenhängende PDF-Akte.

## 6. Rechtsquellen und Grenzen

Der Schwerpunkt liegt auf rechtskräftiger Erwachsenenstrafhaft. Untersuchungshaft, Jugendvollzug, Sicherungsverwahrung, Maßregelvollzug und Abschiebungshaft verlangen eine gesonderte Einordnung. Die Auswahl eines Landes ist verpflichtend: Das Bundes-StVollzG ist kein bundesweiter aktueller Katalog für den gesamten Vollzugsalltag.

Vertieft geprüft wurden die fallrelevanten aktuellen Normen in Berlin, Nordrhein-Westfalen, Bayern und Niedersachsen sowie der bundesrechtliche gerichtliche Rechtsschutz. Der Landeswegweiser eröffnet die Recherche in allen 16 Ländern; er behauptet keine vollständige Durchprüfung aller Landesgesetze. In Berlin werden insbesondere die Änderungen vom Juni 2026 und später in Kraft tretende Teile unterschieden. Die Referenzen enthalten 18 tatsächlich geöffnete amtliche Entscheidungsanker mit gelesenen Randnummern, konkreter Tragweite und ausdrücklichen Grenzen. Dazu gehören Entscheidungen aus 2024 und 2025. Ein Beschluss von 2026 betrifft den Maßregelvollzug und ist ausdrücklich als begrenzt übertragbarer Schnittstellenanker gekennzeichnet; er wird nicht als allgemeine JVA-Regel ausgegeben.

- [Landesrecht und geprüfte Fassungen](references/landesrecht-wegweiser.md)
- [Bundesrecht und Rechtsschutz](references/bundesrecht-rechtsschutz.md)
- [Entscheidungsanker mit „Trägt“ und „Trägt nicht“](references/rechtsprechung.md)
- [Rollen und Vollzugsalltag](references/alltag-und-rollen.md)
- [Zitierweise](references/zitierweise.md)

Akute Gesundheitsprobleme benötigen reale medizinische Hilfe. Das Plugin erstellt juristische Arbeitsprodukte und ersetzt keine Untersuchung. Gerichtliche Fristen, Zuständigkeit, tatsächlicher Zugang und konkrete Quellenfassung werden im Einzelfall überprüft. Die Prüfberichte unterscheiden technische Tests, redaktionelle Quellenprüfung und tatsächliche Anwendungsproben.

## 7. Komponentenrelease

[Version 1.0.1 mit 24 Download-Dateien](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/strafvollzug-jva-v1.0.1) · [Prüfsummen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/strafvollzug-jva-v1.0.1/checksums-sha256.txt)

Das Komponentenrelease ergänzt den aktuellen Repositorybestand. Das unveränderliche ältere Gesamtarchiv v445.35.3 wird nicht nachträglich überschrieben.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`antraege-bescheide-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/antraege-bescheide-bearbeiten/SKILL.md) | Erstellt und prüft konkrete Anträge und Bescheide im Strafvollzug. Ordnet Rolle, Landesbefugnis, Beteiligung, Tatsachen, Begründung und Bekanntgabe zu und bereitet passende gerichtliche Folgeschritte vor, ohne Anstaltsbeschwerde und Rech... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/antraege-bescheide-bearbeiten/SKILL.md) |
| [`besuch-kommunikation-gestalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/besuch-kommunikation-gestalten/SKILL.md) | Klären Sie Besuch, Familienkontakte, Telefon, Schriftverkehr und anwaltliche Kommunikation im Erwachsenenstrafvollzug. Erstellen Sie konkrete Anträge, Besuchsregelungen oder begründete Entscheidungen nach dem zuständigen Landesrecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/besuch-kommunikation-gestalten/SKILL.md) |
| [`bildung-arbeit-digitalzugang-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/bildung-arbeit-digitalzugang-pruefen/SKILL.md) | Prüfen Sie Bildungszugang, Arbeitszuweisung, Vergütung, Haftkosten und Computer im Erwachsenenstrafvollzug. Erstellen Sie einen konkreten Antrag oder eine begründete Entscheidung mit individuellem Bildungsbedarf, technischem Konzept und... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/bildung-arbeit-digitalzugang-pruefen/SKILL.md) |
| [`entlassung-uebergang-planen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/entlassung-uebergang-planen/SKILL.md) | Planen Sie Entlassung, soziale Hilfen und den Übergang in Freiheit. Prüfen Sie erforderliche Lockerungen, Versorgung, Unterkunft, Arbeit und Familienkontakte nach dem Landesrecht und erstellen Sie einen verbindlich zuordenbaren Ablauf od... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/entlassung-uebergang-planen/SKILL.md) |
| [`ernaehrung-religion-beruecksichtigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/ernaehrung-religion-beruecksichtigen/SKILL.md) | Bearbeiten Sie angemessene Verpflegung, religiöse Speisevorgaben, Fastenzeiten und Seelsorge in der JVA. Klären Sie individuelle Bedürfnisse, geeignete Alternativen und Kosten und formulieren Sie Anträge oder begründete Entscheidungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/ernaehrung-religion-beruecksichtigen/SKILL.md) |
| [`gerichtlichen-rechtsschutz-fuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/gerichtlichen-rechtsschutz-fuehren/SKILL.md) | Bereitet gerichtlichen Rechtsschutz im Strafvollzug mit passendem Antrag, zuständigem Gericht, belegter Frist und konkreten Anlagen vor. Trennt Hauptsache, Eilrechtsschutz, Erledigung, Rechtsbeschwerde und Kostenhilfe und prüft die beson... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/gerichtlichen-rechtsschutz-fuehren/SKILL.md) |
| [`gesundheit-unterbringung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/gesundheit-unterbringung-pruefen/SKILL.md) | Prüfen Sie medizinische Versorgung, Haftraumbedingungen, Barrierefreiheit, Hygiene und Aufenthalt im Freien im Erwachsenenstrafvollzug. Erstellen Sie konkrete Abhilfeanträge, JVA-Entscheidungen oder gerichtliche Prüfungen ohne eigene Beh... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/gesundheit-unterbringung-pruefen/SKILL.md) |
| [`grundrechte-gleichbehandlung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/grundrechte-gleichbehandlung-pruefen/SKILL.md) | Prüft Grundrechtsbeschränkungen und Ungleichbehandlungen im Strafvollzug anhand konkreter Tatsachen, Landesbefugnis und geeigneter Alternativen. Trennt Menschenwürde, Freiheitsrechte, Schutzpflichten und Vergleichsfälle und liefert einen... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/grundrechte-gleichbehandlung-pruefen/SKILL.md) |
| [`sicherheit-disziplin-kontrollieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/sicherheit-disziplin-kontrollieren/SKILL.md) | Prüfen Sie Durchsuchungen, besondere Sicherungsmaßnahmen, Fixierungen und Disziplinarmaßnahmen im Erwachsenenstrafvollzug. Erstellen Sie individuelle Anträge oder Entscheidungen mit gesicherter Tatsachengrundlage, Verhältnismäßigkeit und... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/sicherheit-disziplin-kontrollieren/SKILL.md) |
| [`strafvollzug-fall-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/strafvollzug-fall-steuern/SKILL.md) | Steuert konkrete Angelegenheiten des Erwachsenenstrafvollzugs von Rollen- und Landesprüfung über Tatsachenaufklärung bis zu Antrag, Entscheidung und Rechtsschutz. Verbindet zehn Fachschritte mit Fristen, Belegen und dem nächsten vollstän... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/strafvollzug-fall-steuern/SKILL.md) |
| [`vollzugsplan-lockerungen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/vollzugsplan-lockerungen-pruefen/SKILL.md) | Prüft Vollzugsplanung und vollzugsöffnende Maßnahmen anhand individueller Entwicklung, Landesrecht und konkreter Risiken. Entwickelt abgestufte, belegte Vorschläge und verbindet Planfortschreibung, Bescheid und Rechtsschutz mit der Entla... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafvollzug-jva/skills/vollzugsplan-lockerungen-pruefen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

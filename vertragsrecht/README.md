# Vertragsrecht-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Vertragsrecht – Lieferanten- und Vertriebsverträge, AGB Paragrafen 305 ff. BGB, NDA, SaaS-/MSA-Review, Renewal-Tracking, Eskalations-Routing, Business-Zusammenfassungen.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`vertragsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/vertragsrecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/vertragsrecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/vertragsrecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/vertragsrecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/vertragsrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/vertragsrecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Vertragsrecht-Plugin:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`vertragsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/vertragsrecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`vertragsrecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/vertragsrecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`vertragsrecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/vertragsrecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [8 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [BGB: Hochzeitslocation, Schwesterbestellung und abgesagte Feier in Dresden](../testakten/bgb-vollmacht-hochzeitslocation-dresden/README.md) | [Gesamt-PDF](../testakten/bgb-vollmacht-hochzeitslocation-dresden/gesamt-pdf/bgb-vollmacht-hochzeitslocation-dresden_gesamt.pdf) | [`testakte-bgb-vollmacht-hochzeitslocation-dresden.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-bgb-vollmacht-hochzeitslocation-dresden.zip) | [`testakte-bgb-vollmacht-hochzeitslocation-dresden-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-bgb-vollmacht-hochzeitslocation-dresden-einzelpdfs.zip) |
| [Akte Nordstern MedTech Vertrieb - Provision, Buchauszug und Ausgleich](../testakten/handelsvertreterrecht-provisionsausgleich-nordstern-medtech/README.md) | [Gesamt-PDF](../testakten/handelsvertreterrecht-provisionsausgleich-nordstern-medtech/gesamt-pdf/handelsvertreterrecht-provisionsausgleich-nordstern-medtech_gesamt.pdf) | [`testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip) | [`testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech-einzelpdfs.zip) |
| [Akte Campus Rheinbogen - Berufung, Senat und Drittmittel](../testakten/hochschulrecht-berufung-senat-drittmittel-campus-rheinbogen/README.md) | [Gesamt-PDF](../testakten/hochschulrecht-berufung-senat-drittmittel-campus-rheinbogen/gesamt-pdf/hochschulrecht-berufung-senat-drittmittel-campus-rheinbogen_gesamt.pdf) | [`testakte-hochschulrecht-berufung-senat-drittmittel-campus-rheinbogen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-hochschulrecht-berufung-senat-drittmittel-campus-rheinbogen.zip) | [`testakte-hochschulrecht-berufung-senat-drittmittel-campus-rheinbogen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-hochschulrecht-berufung-senat-drittmittel-campus-rheinbogen-einzelpdfs.zip) |
| [Mandatsbeziehung Nordstern BioTherapeutics — Kanzlei Falkenried](../testakten/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech/README.md) | [Gesamt-PDF](../testakten/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech/gesamt-pdf/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech_gesamt.pdf) | [`testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip) | [`testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech-einzelpdfs.zip) |
| [Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/README.md) | [Gesamt-PDF](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-robotikrecht-roboterflotte-vellbruck-muenchen-einzelpdfs.zip) |
| [Sieglinger gegen Burgwald Energietechnik GmbH](../testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/README.md) | [Gesamt-PDF](../testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/gesamt-pdf/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger_gesamt.pdf) | [`testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) | [`testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger-einzelpdfs.zip) |
| [Codeforst / Sonnenklee - RouteLuchs](../testakten/softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen/README.md) | [Gesamt-PDF](../testakten/softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen/gesamt-pdf/softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen_gesamt.pdf) | [`testakte-softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen.zip) | [`testakte-softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen-einzelpdfs.zip) |
| [Tonfenster und Blattwinkel in Freiburg](../testakten/vertragserstellung-ladenkooperation-keramik-freiburg/README.md) | [Gesamt-PDF](../testakten/vertragserstellung-ladenkooperation-keramik-freiburg/gesamt-pdf/vertragserstellung-ladenkooperation-keramik-freiburg_gesamt.pdf) | [`testakte-vertragserstellung-ladenkooperation-keramik-freiburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-vertragserstellung-ladenkooperation-keramik-freiburg.zip) | [`testakte-vertragserstellung-ladenkooperation-keramik-freiburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-vertragserstellung-ladenkooperation-keramik-freiburg-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Arbeitsabläufe für innerbetriebliche Rechtsabteilungen und Kanzleien im deutschen Vertragsrecht: Lieferanten- und Dienstleisterverträge, NDA-/Geheimhaltungsvereinbarungen, SaaS-/MSA-Prüfungen, Vertragsfristen-Tracking, Eskalationssteuerung und mandantengerechte Zusammenfassungen. Ein vorhandener Vorgehensleitfaden wird berücksichtigt; seine Einrichtung ist optional und keine Voraussetzung für die Prüfung eines vorgelegten Vertrags.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, gekennzeichnet und abgestuft – keine abschließende Rechtsberatung.** Das Plugin liest die Dokumente, wendet den Vorgehensleitfaden an, identifiziert Abweichungen und erstellt das Prüfvermerk. Ein Rechtsanwalt prüft, verifiziert und entscheidet. Quellen werden nach Herkunft gekennzeichnet, damit der Prüfer weiß, welche Zitate aus einem Recherche-Tool stammen und welche zu prüfen sind. Vertraulichkeitshinweise werden konservativ gesetzt, damit keine unbeabsichtigte Preisgabe erfolgt. Folgenreiche Handlungen – Einreichung, Versand, Unterzeichnung – stehen unter ausdrücklichem Bestätigungsvorbehalt.

## Für wen ist dieses Plugin

| Rolle | Primäre Arbeitsabläufe |
|---|---|
| **Unternehmensjurist / Legal Counsel** | Lieferantenverträge, Eskalationssteuerung, Stakeholder-Zusammenfassungen |
| **Vertragsmanager / Paralegals** | NDA-Triage, Fristen-Tracking, Erstprüfung |
| **Einkauf / Beschaffung** | Vertragsfristen, Stakeholder-Zusammenfassungen als Empfänger |
| **Vertrieb / BD** | NDA-Triage eigenverantwortlich vor Einbindung der Rechtsabteilung |

## Erste Nutzung: das Ersteinrichtungs-Interview

Bei einem konkreten Auftrag liest das Plugin zuerst Vertrag, Nachträge und verfügbare Vorgaben und fragt nur nach entscheidenden Lücken. Wer zusätzlich einen dauerhaften Vorgehensleitfaden aufbauen möchte, kann mit `kaltstart-interview` die eigenen Positionen und Eskalationsregeln festhalten. Dafür genügen gezielt ausgewählte, erforderliche und berechtigt bereitgestellte Beispiele; eine Sammlung von fünf bis zwanzig Mandatsverträgen ist keine Startbedingung.

Eine ausdrücklich gewünschte dauerhafte Ablage kann bei vorhandenem Schreibzugriff in `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` erfolgen. Ohne Zugriff liefert das Plugin den Leitfaden als Text und verwendet die verfügbaren Vorgaben im laufenden Auftrag; es behauptet weder eine Speicherung noch die automatische Verfügbarkeit in späteren Sitzungen.

```
/vertragsrecht:abschluss-parteien-und-auslegung-bearbeiten Thema: kaltstart-interview
```

**Seite des Mandanten.** Früh in der Einrichtung wird gefragt, ob ein **Verkäufer-Vorgehensleitfaden** (das Unternehmen verkauft Produkte/Dienstleistungen; eigenes Muster), ein **Käufer-Vorgehensleitfaden** (das Unternehmen kauft bei Lieferanten; deren Muster) oder beides aufgebaut werden soll. Die Antwort kehrt nahezu jede Position im Vorgehensleitfaden um – Haftungsgrenzen, Freistellungsrichtung, Kündigungsrechte, IP-Zuordnung – daher ist sie von grundlegender Bedeutung.

## Befehle

| Befehl | Funktion |
|---|---|
| `/vertragsrecht:abschluss-parteien-und-auslegung-bearbeiten Thema: kaltstart-interview` | Ersteinrichtungs-Interview durchführen oder wiederholen |
| `/vertragsrecht:abschluss-parteien-und-auslegung-bearbeiten Thema: vertragspruefung [Datei]` | Vertrag gegen den Vorgehensleitfaden prüfen |
| `/vertragsrecht:vertragsverlaengerungs-monitor` | Welche Verträge laufen in 90 Tagen aus und bis wann muss die Kündigung eingehen? |
| `/vertragsrecht:leistung-verguetung-und-abwicklung-bearbeiten Thema: eskalations-marker` | Eskalationspfad ermitteln und Vorlage formulieren |
| `/vertragsrecht:leistung-verguetung-und-abwicklung-bearbeiten Thema: aenderungs-historie-agb-eskalations-marker [Datei(en)]` | Vertragsänderungen über Basisvertrag und alle Nachträge nachverfolgen |
| `/vertragsrecht:leistung-verguetung-und-abwicklung-bearbeiten Thema: pruefungsvorschlaege` | Ausstehende Aktualisierungen des Vorgehensleitfadens aus dem Monitor-Agenten durcharbeiten |
| `/vertragsrecht:geheimnis-daten-und-rechte-bearbeiten Thema: mandat-arbeitsbereich-vr-einfuehrung` | Akten verwalten (nur Kanzleinutzung mit mehreren Mandanten) |

## Skills

| Skill | Zweck |
|---|---|
| **ersteinrichtung** | Interview, das `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` schreibt |
| **lieferantenvertrag-prüfung** | Vollständige Abweichungsanalyse gegen den Vorgehensleitfaden mit Klausel-Redlines (§§ 631, 611 BGB; LkSG) |
| **nda-prüfung** | Geheimnisbegriff und Schutzmaßnahmen nach Paragraf 2 sowie Nutzungs- und Offenlegungsverbote nach Paragraf 4 GeschGehG; vertragliche Pflichten gesondert prüfen. |
| **saas-msa-prüfung** | SaaS-/MSA-spezifische Prüfung: AGB, Datenschutz Art. 28 DSGVO, Haftung, Preiseskalation |
| **vertragsverlängerungs-monitor** | Vertragliche Fristen erfassen und AGB-Kontrolle trennen: Paragraf 309 Nummer 9 BGB im einschlägigen Verbrauchervertrag; im Unternehmerverkehr Paragrafen 307 und 310 Absatz 1 BGB, keine automatische Übertragung. |
| **eskalation** | Eskalationsmatrix aus dem Vorgehensleitfaden, Vorlage für Genehmigungsanfrage |
| **stakeholder-zusammenfassung** | Zweisprachige Nicht-Juristen-Fassung eines Rechtsgutachtens |
| **änderungs-historie** | Änderungen über Basisvertrag und Nachträge zusammenfassen oder Klausel zurückverfolgen |
| **akte** | Akten anlegen, auflisten, wechseln und schließen für Mehrfachmandatsverhältnisse |

## Befehle vs. terminierte Agenten

Die obigen Befehle bearbeiten einen Vorgang auf Abruf. Die folgenden Takte sind Einrichtungsvorschläge: Hintergrundläufe setzen eine verfügbare Terminierungsfunktion und einen ausdrücklichen Auftrag voraus. Die Plugin-Installation allein richtet keine Überwachung ein; ohne Terminierung ist der jeweilige Prüflauf manuell auszulösen.

| Agent | Beobachtet | Standard-Takt |
|---|---|---|
| **verlängerungs-wächter** | Fristen-Register: meldet, was in 90 Tagen fällig wird; Rot-Flag bei 0–13 Tagen | Wöchentlich (montags) |
| **abschluss-debrief** | Kürzlich unterzeichnete Verträge auf Abweichungen vom Vorgehensleitfaden; Erinnerung zur Erfassung von Kontext | Wöchentlich (montags) |
| **vorgehensleitfaden-monitor** | Abweichungsprotokoll: schlägt Aktualisierungen des Vorgehensleitfadens vor, wenn eine Klausel in 12 Monaten ≥ 5-mal abgewichen wurde | Datengesteuert (nach jedem Abschluss-Debrief) |

## Integrationen

**Zuerst ein Recherche-Tool verbinden – die Zitier-Prüfmechanismen hängen davon ab.** Ohne Verbindung wird jede Quellenangabe mit `[prüfen]` gekennzeichnet und der Prüferhinweis über dem Dokument vermerkt, dass Quellen nicht verifiziert wurden.

Integrierte Konnektoren (`.mcp.json`):

- **Ironclad / Agiloft** – Vertragslebenszyklusverwaltung (CLM)
- **DocuSign** – Unterschriftsstatus und Umschlag-Tracking
- **Slack** – Nachrichten durchsuchen, Kanäle lesen, Diskussionen finden
- **Google Drive / SharePoint** – Dokumente suchen, lesen und abrufen

## Schnellstart

### 1. Interview durchführen

```
/vertragsrecht:abschluss-parteien-und-auslegung-bearbeiten Thema: kaltstart-interview
```

Dauer: ca. 10 Minuten. 5–10 unterzeichnete Verträge bereithalten (mehr ist besser, 20 ergibt ein klareres Muster).

Die Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` gespeichert und bleibt bei Plugin-Updates erhalten.

### 2. Vertrag prüfen

```
/vertragsrecht:abschluss-parteien-und-auslegung-bearbeiten Thema: vertragspruefung lieferanten-msa.pdf
```

Ausgabe: Abweichungsprotokoll gegen den Vorgehensleitfaden mit konkreten Redline-Formulierungen und namentlich genanntem Genehmiger.

### 3. Ablaufende Verträge abrufen

```
/vertragsrecht:vertragsverlaengerungs-monitor
```

Ausgabe: alles mit Kündigungsfrist in den nächsten 90 Tagen, nach Dringlichkeit geordnet.

## Wie das Plugin lernt

Das Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` ist nicht statisch – es verbessert sich mit der Nutzung. Skills melden, wenn eine Ausgabe auf einem Standard basiert, der angepasst werden sollte. Der `vorgehensleitfaden-monitor`-Agent schlägt Aktualisierungen vor, wenn die Praxis vom Vorgehensleitfaden abweicht. Das Interview kann wiederholt werden, die Datei kann direkt bearbeitet werden, oder ein Skill kann eine neue Position erfassen.

## Verzeichnisstruktur

```
vertragsrecht/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                    # Praxisprofil der Rechtsabteilung
├── README.md
├── agents/
│   ├── verlaengerungs-monitor.md
│   ├── deal-nachbesprechung.md
│   └── spielbuch-monitor.md
├── skills/
│   ├── kaltstart-interview/    # → ersteinrichtung
│   ├── vertragspruefung/                  # → prüfen
│   ├── pruefungsvorschlaege/        # → klausel-vorschläge
│   ├── lieferantenvertrag-pruefung/
│   ├── nda-pruefung/
│   ├── saas-msa-pruefung/
│   ├── vertragsverlaengerungs-monitor/         # → vertragsverlaengerungs-monitor
│   │   └── references/renewal-register.yaml
│   ├── eskalations-marker/      # → eskalation
│   ├── aenderungs-historie/       # → aenderungs-historie
│   ├── mandats-arbeitsbereich/  # → akte
│   ├── stakeholder-zusammenfassung/     # → stakeholder-zusammenfassung
│   ├── abmahnung-uwg/           # NEU
│   ├── agb-pruefung/            # NEU
│   └── widerruf-fernabsatz/     # NEU
└── ausloeser/ausloeser.json
```

## Hinweise

- Das Plugin geht standardmäßig davon aus, dass das Unternehmen **Kunde/Käufer** bei den meisten Prüfungen ist. Beim Auftreten als Verkäufer/Auftragnehmer ist dies zu markieren, damit der Vorgehensleitfaden umgekehrt angewendet wird.
- Die NDA-Triage ist für die eigenverantwortliche Nutzung durch Nicht-Juristen konzipiert. GRÜN bedeutet "zur Unterschrift weiterleiten". Sie verhandelt nicht.
- Das Fristen-Tracking erfasst nur Verträge, die über dieses Plugin geprüft oder aus dem CLM einmalig importiert wurden. Vor der Installation unterzeichnete Verträge erfordern einen einmaligen Erstimport.
- **Berufsrechtlicher Hinweis:** Jede Ausgabe ist ein Arbeitsentwurf. Die anwaltliche Verschwiegenheitspflicht (§ 43a Abs. 2 BRAO, § 203 StGB) ist bei jeder Weitergabe zu beachten.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **10 auswählbare Skills**. Die **59 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/juristischer-argumentationskern/SKILL.md), [`vertragsverlaengerungs-monitor`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/vertragsverlaengerungs-monitor/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Abschluss Parteien und Auslegung | [`abschluss-parteien-und-auslegung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/abschluss-parteien-und-auslegung-bearbeiten/SKILL.md) |
| 3. Leistung Vergütung und Abwicklung | [`leistung-verguetung-und-abwicklung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/leistung-verguetung-und-abwicklung-bearbeiten/SKILL.md) |
| 4. Geheimnis Daten und Rechte | [`geheimnis-daten-und-rechte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/geheimnis-daten-und-rechte-bearbeiten/SKILL.md) |
| 5. Haftung Sicherheiten und Störung | [`haftung-sicherheiten-und-stoerung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/haftung-sicherheiten-und-stoerung-bearbeiten/SKILL.md) |
| 6. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 7. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`abschluss-parteien-und-auslegung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/abschluss-parteien-und-auslegung-bearbeiten/SKILL.md) | Vertragsrechtliche Mandatsbearbeitung: Abschluss Parteien und Auslegung: Vertragspartner, Abschluss, Vollmacht, Form und maßgeblichen Inhalt anhand des Fassungsverlaufs prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/abschluss-parteien-und-auslegung-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Vertragsrechtliche Mandatsbearbeitung: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/einstieg-routing/SKILL.md) | Für Vertragsprüfung, Gestaltung oder Leistungsstörungen: prüft die konkrete Rechtsfrage und erstellt begründete Klauseländerungen, Schreiben oder einen beauftragten Vertragsentwurf. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/einstieg-routing/SKILL.md) |
| [`geheimnis-daten-und-rechte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/geheimnis-daten-und-rechte-bearbeiten/SKILL.md) | Vertragsrechtliche Mandatsbearbeitung: Geheimnis Daten und Rechte: Geheimnisse, Daten, Nutzungsrechte und Weitergabe im tatsächlichen Geschäftsvorgang absichern. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/geheimnis-daten-und-rechte-bearbeiten/SKILL.md) |
| [`haftung-sicherheiten-und-stoerung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/haftung-sicherheiten-und-stoerung-bearbeiten/SKILL.md) | Vertragsrechtliche Mandatsbearbeitung: Haftung Sicherheiten und Störung: Haftung, Mängel, Sicherheit, Leistungsstörung und wirtschaftliche Risikozuordnung gestalten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/haftung-sicherheiten-und-stoerung-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/juristischer-argumentationskern/SKILL.md) | Vertragsstreit bis zur passenden Erklärung oder Vertragsänderung bearbeiten. Nutzt vorhandene Falldaten, entscheidet die maßgeblichen rechtlichen Abzweigungen und verbindet passende Fachprüfungen mit einem vollständig ausgearbeiteten Erg... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`leistung-verguetung-und-abwicklung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/leistung-verguetung-und-abwicklung-bearbeiten/SKILL.md) | Vertragsrechtliche Mandatsbearbeitung: Leistung Vergütung und Abwicklung: Leistung, Gegenleistung, Abnahme, laufende Pflichten und Abrechnung konkret ausformulieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/leistung-verguetung-und-abwicklung-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Vertragsrechtliche Mandatsbearbeitung: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`vertragsverlaengerungs-monitor`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/vertragsverlaengerungs-monitor/SKILL.md) | Für Verlängerungstracker: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/vertragsverlaengerungs-monitor/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/workflow-kaltstart-und-routing/SKILL.md) | Für neue Vertragsaufträge: bestimmt Vertragsparteien, Vertragsfassung, Abschluss- und Leistungsstand sowie dringende Fristen aus den vorhandenen Unterlagen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsrecht/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

# Kanzlei-Mandant Lifecycle

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Lifecycle-Plugin für Kanzlei, Mandant und Rechtsabteilung: Mandatsstart, OCG, Budget, Dashboard, Rechnung, Litigation, Erwartungsmanagement und Relationship-Governance.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`kanzlei-mandant-lifecycle.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/kanzlei-mandant-lifecycle.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/kanzlei-mandant-lifecycle.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/kanzlei-mandant-lifecycle-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/kanzlei-mandant-lifecycle-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/kanzlei-mandant-lifecycle.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/kanzlei-mandant-lifecycle.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Kanzlei-Mandant Lifecycle:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`kanzlei-mandant-lifecycle.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/kanzlei-mandant-lifecycle.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`kanzlei-mandant-lifecycle-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/kanzlei-mandant-lifecycle-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`kanzlei-mandant-lifecycle-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/kanzlei-mandant-lifecycle-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Falkenried & Partner mbB — Managementakte Q2/2026](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/README.md) | [Gesamt-PDF](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/gesamt-pdf/kanzlei-management-falkenried-partnerkreis-q2-2026_gesamt.pdf) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026-einzelpdfs.zip) |
| [Mandatsbeziehung Nordstern BioTherapeutics — Kanzlei Falkenried](../testakten/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech/README.md) | [Gesamt-PDF](../testakten/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech/gesamt-pdf/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech_gesamt.pdf) | [`testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip) | [`testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Ein Plugin für die ganze Lebensbeziehung zwischen Kanzlei, Einzelanwalt, Mandant und Rechtsabteilung: Mandatsannahme, Scope, Outside Counsel Guidelines, Budget, Forecast, Statusbericht, Gerichtsakte, Rechnung, Erwartungsmanagement, Enttäuschung, Eskalation, Quickwins und Abschluss.

Es denkt nicht nur juristisch, sondern auch organisatorisch und kaufmännisch: Wer braucht welche Entscheidung, was kostet es, was ist schon erledigt, was blockiert, was darf aus Geheimhaltungs-, Datenschutz- oder Berufsrechtsgründen überhaupt in ein gemeinsames System?

## Kaltstart

1. Rolle klären: Kanzlei, Rechtsabteilung, GC, CFO, Fachabteilung, Einzelanwalt oder externer Dienstleister.
2. Matter klären: Beratung, Prozess, Behörde, Transaktion, Krise, Untersuchung oder Dauerberatung.
3. Ein Dashboard zu Status, Budget, Rechnung, Litigation, Board, Risiko, Legal Hold oder Beziehungspuls nur bei Bedarf ergänzen. Bei einem konkreten Auftrag direkt das Statusschreiben, die Budgetantwort oder die Abschlussmitteilung aus der vorhandenen Mandatsakte erstellen und nach Rückmeldung fortschreiben.
4. Geheimhaltung prüfen: Mandatsgeheimnis, Datenschutz, Dienstleister, KI-System, Zugriff und Export.
5. Nächsten Arbeitsschritt erzeugen: Mail, Memo, Board Paper, Rechnungskommentar, Fristenliste, Entscheidungslog oder Eskalationsnotiz.

## Leitidee

Das Plugin soll beide Seiten stärker machen. Die Kanzlei liefert verständlicher, schneller und berechenbarer. Der Mandant versteht Kosten, Risiko und Fortschritt. Die Rechtsabteilung bekommt ein Cockpit, ohne das Mandatsgeheimnis zu zerlegen. Niemand soll mit schönen Dashboards betäubt werden; jedes Dashboard muss eine echte Entscheidung erleichtern.

## Typische Outputs

- Matter Dashboard mit Ampeln für Frist, Budget, Chancen, Blocker und nächste Entscheidung.
- Invoice Review mit Narrative-Check, OCG-Abgleich und Kürzungsvorschlag.
- Weekly Status Report und Board One-Pager.
- Litigation Roadmap mit Kosten- und Vergleichsfenster.
- Relationship Pulse nach schwierigen Phasen.
- Closeout mit Lessons Learned und Template-Update.

## Quellenhygiene

Vor rechtlich tragenden Aussagen immer live prüfen: BRAO, BORA, RVG, DSGVO, § 203 StGB, Verfahrensrecht und die konkrete Vergütungsvereinbarung. Keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Upload plugin` wählen und die Datei auswählen.
3. Plugin aktivieren und eine neue Aufgabe öffnen; den passenden Skill ausdrücklich auswählen.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **8 auswählbare Skills**. Die **116 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/juristischer-argumentationskern/SKILL.md) |
| 2. Mandat und Vereinbarung | [`mandat-und-vereinbarung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/mandat-und-vereinbarung-bearbeiten/SKILL.md) |
| 3. Akte Fristen und Zusammenarbeit | [`akte-fristen-und-zusammenarbeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/akte-fristen-und-zusammenarbeit-bearbeiten/SKILL.md) |
| 4. Beratung Kommunikation und Entscheidung | [`beratung-kommunikation-und-entscheidung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/beratung-kommunikation-und-entscheidung-bearbeiten/SKILL.md) |
| 5. Vergütung Rechnung und Fremdgeld | [`verguetung-rechnung-und-fremdgeld-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/verguetung-rechnung-und-fremdgeld-bearbeiten/SKILL.md) |
| 6. Rechtsdurchsetzung Risiko und Governance | [`rechtsdurchsetzung-risiko-und-governance-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/rechtsdurchsetzung-risiko-und-governance-bearbeiten/SKILL.md) |
| 7. Abschluss Archiv und Weiterbetreuung | [`abschluss-archiv-und-weiterbetreuung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/abschluss-archiv-und-weiterbetreuung-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 8 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 8 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`abschluss-archiv-und-weiterbetreuung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/abschluss-archiv-und-weiterbetreuung-bearbeiten/SKILL.md) | Für Kanzleibetrieb und Mandatssteuerung: Abschluss Archiv und Weiterbetreuung: Mandatsabschluss, offene Schritte, Rückgabe, Aufbewahrung und Weiterbetreuung dokumentieren. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt n... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/abschluss-archiv-und-weiterbetreuung-bearbeiten/SKILL.md) |
| [`akte-fristen-und-zusammenarbeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/akte-fristen-und-zusammenarbeit-bearbeiten/SKILL.md) | Für Kanzleibetrieb und Mandatssteuerung: Akte Fristen und Zusammenarbeit: Arbeitsstand, Dokumente, Fristen und Verantwortliche im laufenden Mandat fortführen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem konkr... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/akte-fristen-und-zusammenarbeit-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Mandantenbetreuung über den gesamten Mandatsverlauf: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erkl... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`beratung-kommunikation-und-entscheidung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/beratung-kommunikation-und-entscheidung-bearbeiten/SKILL.md) | Für Kanzleibetrieb und Mandatssteuerung: Beratung Kommunikation und Entscheidung: Mandanten verständlich informieren, offene Entscheidungen begründen und Antworten einarbeiten. Vollständige Fachanweisungen und lokale Vorlagen werden gezi... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/beratung-kommunikation-und-entscheidung-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/juristischer-argumentationskern/SKILL.md) | Mandat von der Aufnahme bis zur geordneten Beendigung steuern. Verarbeitet vorhandene Unterlagen, verbindet entscheidende Fachprüfungen und belegte Quellen, erstellt das beauftragte Ergebnis und führt denselben Vorgang nach neuen Angaben... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/juristischer-argumentationskern/SKILL.md) |
| [`mandat-und-vereinbarung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/mandat-und-vereinbarung-bearbeiten/SKILL.md) | Für Kanzleibetrieb und Mandatssteuerung: Mandat und Vereinbarung: Mandatsumfang, Konflikt, Identität, Vollmacht und Vereinbarung zuverlässig klären. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem konkreten Auftr... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/mandat-und-vereinbarung-bearbeiten/SKILL.md) |
| [`rechtsdurchsetzung-risiko-und-governance-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/rechtsdurchsetzung-risiko-und-governance-bearbeiten/SKILL.md) | Für Kanzleibetrieb und Mandatssteuerung: Rechtsdurchsetzung Risiko und Governance: Verfahrensschritte, Entscheidungen, Nachweise, Vertraulichkeit und Verantwortung auf Mandanten- und Kanzleiseite verbinden. Vollständige Fachanweisungen u... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/rechtsdurchsetzung-risiko-und-governance-bearbeiten/SKILL.md) |
| [`verguetung-rechnung-und-fremdgeld-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/verguetung-rechnung-und-fremdgeld-bearbeiten/SKILL.md) | Für Kanzleibetrieb und Mandatssteuerung: Vergütung Rechnung und Fremdgeld: Abrechnung, Zahlung, Fremdgeld und Kosteninformation mit der Beauftragung abstimmen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem konk... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-mandant-lifecycle/skills/verguetung-rechnung-und-fremdgeld-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Prüfen Sie Dialog, Dokumentenannahme, Fristübernahme und Versand einzeln. Ein transparent gekennzeichneter Bot darf nicht deshalb unbestätigte Fristen oder eine Rechtsprüfung als abgeschlossen darstellen.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.

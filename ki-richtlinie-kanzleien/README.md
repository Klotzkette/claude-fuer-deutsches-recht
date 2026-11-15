# KI-Richtlinie für Kanzleien und Rechtsabteilungen

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Erstellt und pflegt eine berufsrechtskonforme KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen mit Anwälten und Syndikus-Anwälten. Beruht auf BRAO, BORA, DSGVO, KI-Verordnung sowie BRAK- und DAV-Hinweisen.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`ki-richtlinie-kanzleien.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/ki-richtlinie-kanzleien.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/ki-richtlinie-kanzleien.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/ki-richtlinie-kanzleien-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/ki-richtlinie-kanzleien-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/ki-richtlinie-kanzleien.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/ki-richtlinie-kanzleien.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für KI-Richtlinie für Kanzleien und Rechtsabteilungen:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`ki-richtlinie-kanzleien.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/ki-richtlinie-kanzleien.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`ki-richtlinie-kanzleien-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/ki-richtlinie-kanzleien-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`ki-richtlinie-kanzleien-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/ki-richtlinie-kanzleien-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Organisationsakte König, Brehm & Partner](../testakten/ki-richtlinie-musterkanzlei/README.md) | [Gesamt-PDF](../testakten/ki-richtlinie-musterkanzlei/gesamt-pdf/ki-richtlinie-musterkanzlei_gesamt.pdf) | [`testakte-ki-richtlinie-musterkanzlei.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-ki-richtlinie-musterkanzlei.zip) | [`testakte-ki-richtlinie-musterkanzlei-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-ki-richtlinie-musterkanzlei-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Rechtsstand 10. September 2026: Die Richtlinienarbeit verwendet Kompetenzförderung ohne erfundene Zertifikatspflicht. Berufsrecht, Datenschutz, Veröffentlichungen und betriebliche Freigabe bleiben getrennte Prüfungen. [Rechtsstandkarte lesen](./references/digitaler-omnibus-2026.md) · <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/references/digitaler-omnibus-2026.md" download>MD herunterladen</a>.

English: The updated workflows distinguish enacted law, future application dates and pending proposals. The reference note identifies official sources and the competent supervisory authority for each route.
Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin erstellt und pflegt eine berufsrechtskonforme KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen mit Anwälten sowie Syndikus-Anwältinnen und Syndikus-Anwälten. Es beruht auf BRAO, BORA, DSGVO, KI-Verordnung sowie den Hinweisen der BRAK (Dezember 2024) und der DAV-Stellungnahme Nr. 32/2025.

---

## Direkter Download

**Plugin:**
[ki-richtlinie-kanzleien.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/ki-richtlinie-kanzleien.zip)

---

## Ausgewählte Arbeitswege

Diese Auswahl ordnet die Kernaufgaben. Alle weiteren Skills und ihre Einzel-Downloads stehen in der [vollständigen Skill-Liste](../skills-index/ki-richtlinie-kanzleien.md).

| Skill | Beschreibung |
|---|---|
| `kanzlei-kontext-analyse` | Kanzleigröße, Rechtsgebiete, Mandantenstruktur und IT-Infrastruktur erfassen, um den Richtlinien-Tailoring-Bedarf abzuleiten |
| `richtlinien-skelett-erzeugen` | Vollständige 13-Kapitel-Gliederung der KI-Nutzungsrichtlinie analog der Master-Vorlage generieren |
| `executive-summary-bausteine` | Sechs Kern-Eckpunkte als modulare Textbausteine: Werkzeugcharakter, Verschwiegenheit, Datenschutz, Quellenprüfung, Keine Privat-Accounts, Kennzeichnung |
| `dsgvo-compliance-bausteine` | Datenschutzrechtliche Bausteine: Art. 6, Art. 9, Art. 28 DSGVO; AVV, Drittlandtransfer, Datenminimierung |
| `berufsrecht-bausteine` | Berufsrechtliche Bausteine: § 43, § 43a, § 43e BRAO, § 203 StGB, BRAK 12/2024, DAV 32/2025 |
| `urheberrecht-bausteine` | § 2 Abs. 2 UrhG, § 5 UrhG amtliche Werke, Upload-Regeln, Lizenzbedingungen juristischer Datenbanken |
| `geschgehg-bausteine` | Geschäftsgeheimnisschutz beim KI-Einsatz, § 1 Abs. 3 Nr. 1 GeschGehG, Verhältnis zu § 203 StGB |
| `ki-vo-betreiber-pflichten` | Art. 3 Nr. 4 Betreiber, Art. 4 KI-Kompetenz, Hochrisiko-Abgrenzung Anhang III Nr. 8.a, Art. 50 Abs. 4 Kennzeichnung |
| `ki-vo-hochrisiko-personalwesen` | Hochrisiko-KI im Personalwesen nach Artikel 6 Absatz 2 und Anhang III Nummer 4: Kapitel III Abschnitte 1 bis 3, außer Artikel 6 Absatz 5, ab 2. Dezember 2027 nach Artikel 113 Absatz 3 Buchstabe c Ziffer i; Betriebsratsrechte gesondert prüfen |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `schatten-ki-aufdeckung` | Methoden zur Erkennung verdeckter KI-Nutzung und konstruktiver Umgang: Stilanalyse, Anlaufstelle, Amnestie |
| `compliance-regelsatz-erstellen` | Standardisierter Zehn-Gebote-Regelsatz für den KI-Einsatz in der Kanzlei |
| `anonymisierung-pseudonymisierung` | Stufenmodell der Anonymisierung: Schwärzung, Platzhalter, Re-Identifikationsrisikoprüfung |
| `auftragsverarbeitungsvertrag-pruefen` | Checkliste AVV nach Art. 28 DSGVO bei KI-Anbietern: Subprozessoren, TOMs, Drittlandtransfer, Audit |
| `dienstleister-due-diligence` | Auswahlkriterien KI-Dienstleister: EU vs. USA, Training-Opt-out, ISO 27001, SOC 2, SCC |
| `transparenz-mandanten` | Musterklauseln Mandatsvertrag und Datenschutzerklärung für KI-Einsatz-Transparenz |
| `halluzinations-handhabung` | Quellenprüfungspflicht, OLG Koblenz, AG Köln 02.07.2025, Vier-Augen-Prinzip, Prüfprotokoll |
| `automatisierte-entscheidungen-art-22-dsgvo` | Verbot ausschließlich automatisierter Entscheidungen, Ausnahmen, Anwendung auf Kanzleiprozesse |
| `bias-und-diskriminierung-pruefung` | Bias-Quellen in KI-Systemen, AGG-Relevanz bei Bewerberauswahl, Prüfverfahren |
| `ki-kompetenz-erwerb-plan` | Maßnahmen zur Kompetenzförderung nach Artikel 4 KI-VO; Modulzahl, Sandbox und jährliche Wiederholung nur als bedarfsgerechter interner Standard, nicht als gesetzlich festgelegtes Programm |
| `dokumentationspflichten-protokoll` | Beweissichere Protokollierung von KI-Inputs und -Outputs; Prüfprotokoll, Handakten-Dokumentation |
| `kennzeichnungspflichten-veroeffentlichungen` | Art. 50 Abs. 4 KI-VO: Kanzlei-Blogs, Pressemitteilungen, Schriftsätze; redaktionelle Verantwortung als Ausnahme |
| `prompting-leitfaden` | Vier-Elemente-Methode für juristische Prompts: Ziel, Format, Kontext, Beispiel; Tipps und Tricks |
| `richtlinien-update-zyklus` | Halbjährliches Review plus Trigger-Liste für sofortige Updates bei neuer Rechtslage |
| `musterklauseln-it-vertrag` | § 43e-BRAO-Vereinbarung, Training-Opt-out, Löschpflichten, Auditrechte, Haftungsregelung |
| `literatur-und-quellen` | Pflicht-Literatur und offene Aktualisierungsliste: BRAK, DAV, EU-FAQ, BNetzA |

Artikel 4 und Artikel 113 sind in der Fassung von Artikel 1 Nummern 5 und 40 der [Verordnung (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj?locale=de) zugrunde zu legen. Der spätere Anwendungsbeginn der genannten Hochrisiko-Regeln verschiebt nicht sämtliche KI-Pflichten oder bestehende arbeitsrechtliche Anforderungen.

---

## Rechtsgrundlagen

| Quelle | Relevanz |
|---|---|
| BRAO §§ 43, 43a, 43e | Gewissenhaftigkeit, Verschwiegenheit, IT-Dienstleister |
| BORA §§ 2, 31 | Sozialadäquanz, Berufsrechtsbeauftragter |
| DSGVO Art. 5, 6, 9, 28, 44 ff. | Datenschutzgrundsätze, Erlaubnistatbestände, AVV, Drittlandtransfer |
| KI-VO (EU) 2024/1689 Art. 3, 4, 6, 50 | Begriffsbestimmungen, KI-Kompetenz, Hochrisiko, Kennzeichnung |
| UrhG §§ 2, 5, 31, 87a | Schöpfungshöhe, amtliche Werke, Lizenz, Datenbankschutz |
| GeschGehG §§ 1, 2, 4 | Geschäftsgeheimnisschutz |
| StGB § 203 | Verletzung von Privatgeheimnissen |
| RDG § 2 | Rechtsdienstleistungsbegriff |
| AGG §§ 1, 7 | Diskriminierungsverbot |
| BRAK-Hinweise 12/2024 | Berufsrechtliche Mindeststandards KI-Einsatz |
| DAV-Stellungnahme 32/2025 | Halluzinationsrisiko und Prüfpflichten |

---

## Verwendungsbeispiel

```
Ich bin Partner einer mittelgroßen Kanzlei mit 15 Anwälten im deutschen
Gesellschaftsrecht und M&A. Wir wollen einen führenden US-amerikanischen KI-Dienst
mit Enterprise-Account einsetzen. Erstelle für uns einen vollständigen Entwurf einer
KI-Nutzungsrichtlinie: Beginne mit dem Skill kanzlei-kontext-analyse, erzeuge dann
mit richtlinien-skelett-erzeugen die Struktur und fülle alle 13 Kapitel inhaltlich
aus — unter besonderer Berücksichtigung der DSGVO-Anforderungen an den Drittland-
Transfer (USA) und der § 43e-BRAO-Vertragsdokumentation.
```

---

*Version 3.3.0 | Autor: Klotzkette | Lizenz: MIT*

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **9 auswählbare Skills**. Die **60 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Mandat eröffnen | [`mandat-eroeffnen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/mandat-eroeffnen-bearbeiten/SKILL.md) |
| 3. Fristen und Zuständigkeit | [`fristen-und-zustaendigkeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/fristen-und-zustaendigkeit-bearbeiten/SKILL.md) |
| 4. Bearbeitung steuern | [`bearbeitung-steuern-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/bearbeitung-steuern-bearbeiten/SKILL.md) |
| 5. Mandat abschließen | [`mandat-abschliessen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/mandat-abschliessen-bearbeiten/SKILL.md) |
| 6. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 7. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | KI-Richtlinie für Kanzleien und Rechtsabteilungen: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`bearbeitung-steuern-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/bearbeitung-steuern-bearbeiten/SKILL.md) | KI-Richtlinie für Kanzleien und Rechtsabteilungen: Bearbeitung steuern: Arbeitsauftrag, Dokumentstand, Freigabe, Vieraugenkontrolle, Budget, offene Punkte und Mandantenentscheidung führen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/bearbeitung-steuern-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Kanzleirichtlinien für digitale Werkzeuge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/einstieg-routing/SKILL.md) |
| [`fristen-und-zustaendigkeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/fristen-und-zustaendigkeit-bearbeiten/SKILL.md) | KI-Richtlinie für Kanzleien und Rechtsabteilungen: Fristen und Zuständigkeit: Eingang, Bekanntgabe, Fristart, Fristende, Kalender, Verantwortlicher und Vertretung doppelt dokumentieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/fristen-und-zustaendigkeit-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn eine Systemrichtlinie für Kanzleien tragfähig begründet werden muss; verbindet Einsatzfall, Berufspflicht, technische Kontrolle, Verantwortlichkeit, stärkste Gegenposition und konkrete Regelungsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/juristischer-argumentationskern/SKILL.md) |
| [`mandat-abschliessen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/mandat-abschliessen-bearbeiten/SKILL.md) | KI-Richtlinie für Kanzleien und Rechtsabteilungen: Mandat abschließen: Ergebnis, offene Vollstreckung, Rechnung, Fremdgeld, Rückgabe, Aufbewahrung und Wiedervorlage dokumentieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/mandat-abschliessen-bearbeiten/SKILL.md) |
| [`mandat-eroeffnen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/mandat-eroeffnen-bearbeiten/SKILL.md) | KI-Richtlinie für Kanzleien und Rechtsabteilungen: Mandat eröffnen: Beteiligte, Gegenstand, Gegner, Interessenkontrolle, Identität, Vollmacht, Umfang und Vergütung sichern. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/mandat-eroeffnen-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | KI-Richtlinie für Kanzleien und Rechtsabteilungen: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Kanzleirichtlinien für digitale Werkzeuge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-richtlinie-kanzleien/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Beschreiben Sie erlaubte Arbeitsschritte, Datenzugriffe, Kontrollhandlungen und Eskalationsfälle konkret. Ein Schulungsnachweis oder eine allgemeine KI-Policy beweist weder Systemkonformität noch ausreichende Prüfung im Einzelmandat.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.

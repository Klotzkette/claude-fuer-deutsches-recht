# gesellschaftsgründer — Gründungsassistent für deutsche Gesellschaften

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Gruendungsassistent für deutsche Gesellschaften: Rechtsformwahl, Satzung, Notar, Handelsregister, Bank/KYC, Steuerstart, IP, Erlaubnisse, erste Verträge, Budget und Streitpraevention.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`gesellschaftsgruender.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/gesellschaftsgruender.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/gesellschaftsgruender.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/gesellschaftsgruender-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/gesellschaftsgruender-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/gesellschaftsgruender.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/gesellschaftsgruender.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für gesellschaftsgründer — Gründungsassistent für deutsche Gesellschaften:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`gesellschaftsgruender.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/gesellschaftsgruender.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`gesellschaftsgruender-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/gesellschaftsgruender-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`gesellschaftsgruender-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/gesellschaftsgruender-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [8 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Akte Knusperkrone: Franchise-Expansion, Gebietsschutz und Systemhandbuch-Streit](../testakten/franchiserecht-systemgastronomie-expansion-streit/README.md) | [Gesamt-PDF](../testakten/franchiserecht-systemgastronomie-expansion-streit/gesamt-pdf/franchiserecht-systemgastronomie-expansion-streit_gesamt.pdf) | [`testakte-franchiserecht-systemgastronomie-expansion-streit.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-franchiserecht-systemgastronomie-expansion-streit.zip) | [`testakte-franchiserecht-systemgastronomie-expansion-streit-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-franchiserecht-systemgastronomie-expansion-streit-einzelpdfs.zip) |
| [NeuroChain Labs — Gründung eines digitale Systeme/Krypto-Startups in Berlin, Musterprotokoll vs. individuelle Satzung](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/README.md) | [Gesamt-PDF](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/gesamt-pdf/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll_gesamt.pdf) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll-einzelpdfs.zip) |
| [Röschen Tech GmbH — Gründung, Series A, B-Shares und Streit-Eskalation](../testakten/gesellschaftsgruender-streit-roeschen-tech/README.md) | [Gesamt-PDF](../testakten/gesellschaftsgruender-streit-roeschen-tech/gesamt-pdf/gesellschaftsgruender-streit-roeschen-tech_gesamt.pdf) | [`testakte-gesellschaftsgruender-streit-roeschen-tech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-gesellschaftsgruender-streit-roeschen-tech.zip) | [`testakte-gesellschaftsgruender-streit-roeschen-tech-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-gesellschaftsgruender-streit-roeschen-tech-einzelpdfs.zip) |
| [Topf & Tacheles – einfache GmbH-Gründung in Berlin](../testakten/gesellschaftsgruender-topf-tacheles-berlin/README.md) | [Gesamt-PDF](../testakten/gesellschaftsgruender-topf-tacheles-berlin/gesamt-pdf/gesellschaftsgruender-topf-tacheles-berlin_gesamt.pdf) | [`testakte-gesellschaftsgruender-topf-tacheles-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-gesellschaftsgruender-topf-tacheles-berlin.zip) | [`testakte-gesellschaftsgruender-topf-tacheles-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-gesellschaftsgruender-topf-tacheles-berlin-einzelpdfs.zip) |
| [Handelsrecht HGB — Elbwerft Solar: eGbR, OHG-Statuswechsel, KG und Handelskauf](../testakten/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona/README.md) | [Gesamt-PDF](../testakten/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona/gesamt-pdf/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona_gesamt.pdf) | [`testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip) | [`testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona-einzelpdfs.zip) |
| [Nebelstern Ventures - Berliner VC-Pipeline, Wandeldarlehen und Follow-on-Chaos](../testakten/venture-capital-geber-nebelstern-portfolio-berlin/README.md) | [Gesamt-PDF](../testakten/venture-capital-geber-nebelstern-portfolio-berlin/gesamt-pdf/venture-capital-geber-nebelstern-portfolio-berlin_gesamt.pdf) | [`testakte-venture-capital-geber-nebelstern-portfolio-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-venture-capital-geber-nebelstern-portfolio-berlin.zip) | [`testakte-venture-capital-geber-nebelstern-portfolio-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-venture-capital-geber-nebelstern-portfolio-berlin-einzelpdfs.zip) |
| [Speichenraum GbR in Leipzig](../testakten/vertragserstellung-gbr-fahrradwerkstatt-leipzig/README.md) | [Gesamt-PDF](../testakten/vertragserstellung-gbr-fahrradwerkstatt-leipzig/gesamt-pdf/vertragserstellung-gbr-fahrradwerkstatt-leipzig_gesamt.pdf) | [`testakte-vertragserstellung-gbr-fahrradwerkstatt-leipzig.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-vertragserstellung-gbr-fahrradwerkstatt-leipzig.zip) | [`testakte-vertragserstellung-gbr-fahrradwerkstatt-leipzig-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-vertragserstellung-gbr-fahrradwerkstatt-leipzig-einzelpdfs.zip) |
| [Suppenfaden UG in Regensburg](../testakten/vertragserstellung-ug-eventkueche-regensburg/README.md) | [Gesamt-PDF](../testakten/vertragserstellung-ug-eventkueche-regensburg/gesamt-pdf/vertragserstellung-ug-eventkueche-regensburg_gesamt.pdf) | [`testakte-vertragserstellung-ug-eventkueche-regensburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-vertragserstellung-ug-eventkueche-regensburg.zip) | [`testakte-vertragserstellung-ug-eventkueche-regensburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-vertragserstellung-ug-eventkueche-regensburg-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine Gründung praktisch vorbereiten: Rechtsform, Satzung, Gesellschaftervereinbarung, Notartermin, Register, Einlagen, Geschäftsführer, Vesting und erste Beschlüsse.
Freistehendes, anfängerfreundliches und zugleich professionelles Plugin für die Gründung und frühe Führung deutscher Gesellschaften. Es hilft beim ersten Sortieren ebenso wie bei einem fast fertigen Gründungspaket: Rechtsformwahl, Rollen der Gründerinnen und Gründer, Satzung, Gesellschaftervereinbarung, Cap Table, Notar, Handelsregister, Bank/KYC, Behörden, Steuerstart, IP, Datenschutz, erste 100 Tage und Streitprävention.

## Installation

1. Plugin-Umgebung öffnen.
2. **Customize → Plugins** bzw. **Personal plugins** wählen.
3. **Upload plugin** und `gesellschaftsgruender.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte die Gesellschaftsgründung. Ich habe drei Gründer, eine GmbH-Idee und noch keine Satzung.`

Alternativ via Marketplace:

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install gesellschaftsgruender@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und das Verzeichnis `skills/` enthalten.

## So Startet Es

Aus Gründervereinbarung, Satzungsentwurf und dem konkreten Auftrag wird der passende Gründungsweg bestimmt. Ein bestellter Gesellschaftsvertrag oder ein Notarbriefing wird direkt ausgearbeitet. Die folgenden Fragen dienen nur dazu, entscheidende Lücken zu erkennen; vorhandene Angaben werden nicht erneut abgefragt:

1. **Wer gründet?** Personen, Rollen, Wohnsitz, Auslandsbezug, Minderjährige, Treuhand, Familien- oder Investorensituation.
2. **Was soll die Gesellschaft tun?** Geschäftszweck, reguliertes Geschäft, IP, Daten, KI, Produkt, Finanzierung, Personal.
3. **Welche Rechtsform liegt nahe?** GmbH, UG, eGbR, OHG, KG, GmbH & Co. KG, PartG mbB, gGmbH, eG, AG, Holding oder Sonderstruktur.
4. **Was muss jetzt zuerst passieren?** Notarbriefing, Gesellschaftsvertrag, Bankkonto, Transparenzregister, Steuererfassung, Gewerbe, IHK/BG, Versicherungen.
5. **Wo brennt es?** Registerbeanstandung, Gründerstreit, KYC-Blockade, IP-Lücke, Sacheinlage, Stammkapitalverlust, Liquiditätsproblem.

Eine vollständige Gründungsaufnahme ist kein Pflichtschritt vor einem klaren Einzelauftrag. Antworten ergänzen die betroffenen Klauseln oder Nachweise im begonnenen Dokument; Notar-, Register-, KYC- und Krisenfragen werden nur bei konkretem Bezug vertieft.

## Arbeitsphasen

| Phase | Ziel | Typische Outputs |
| --- | --- | --- |
| **0 Intake** | Idee, Beteiligte, Geld, Risiko und Zeitplan verstehen | One-Page-Roadmap, Rückfragenliste, Risikoampel |
| **1 Rechtsform** | passende Struktur auswählen und falsche Abzweigungen vermeiden | Rechtsformmatrix, Entscheidungsvorlage, Stoppschilder |
| **2 Dokumente** | Gründungspaket bauen | Satzung, SHA, Geschäftsführerunterlagen, Gesellschafterliste, Notarbriefing |
| **3 Vollzug** | Notar, Register, Bank, Behörden und Steuerstart koordinieren | Closing-Checkliste, KYC-Paket, ELSTER-/Gewerbe-/BG-Liste |
| **4 Betrieb** | erste 100 Tage sauber organisieren | Board Pack, Beschlussvorlagen, Versicherungs- und Compliance-Check |
| **5 Konflikt** | Streit früh erkennen und kontrolliert eskalieren | Deadlock-Matrix, Mediationsplan, Eilmaßnahmen-Check, Registerstrategie |

## Skillgruppen

- **Einstieg und Anfängerführung:** Kaltstart, einfache Sprache, One-Page-Roadmap, Gründerrollen, Mandantenbrief, Checkliste vor Unterschrift.
- **Rechtsformen:** GmbH, UG, eGbR, OHG, KG, GmbH & Co. KG, PartG mbB, gGmbH, eG, AG, SE und Holdingmodelle.
- **Dokumente und Vollzug:** Satzung, Gesellschaftervereinbarung, Geschäftsführervertrag, Geschäftsordnung, Gesellschafterliste, Notarbriefing, Registerbeanstandung.
- **Finanzierung und Beteiligung:** Cap Table, Seed-Runde, Wandeldarlehen, Founder Vesting, Leaver, ESOP/VSOP, Vinkulierung, Drag/Tag, Bezugsrechte.
- **Risikothemen:** Auslandsgründer, KYC, Sanktionen, Transparenzregister, Sacheinlagen, IP-Übertragung, Open Source, Datenschutz/KI, regulierte Geschäftsmodelle.
- **Operativer Start:** Bankkonto, Steuerliche Erfassung, Umsatzsteuer, Payroll, Mietvertrag, Kundenstart, Produkthaftung, Versicherungen, Cash Burn und Insolvenzfrühwarnung.

## Einfacher Einstieg: Topf & Tacheles

Die [einfache Berliner Gründungsakte Topf & Tacheles](../testakten/gesellschaftsgruender-topf-tacheles-berlin/README.md) ist der Einstieg mit kleinem Dateiumfang: sieben Personen gründen einen Pflanzenverleih mit Gießservice. Die **15 Originaldateien** enthalten einen kurzen Chat, vier E-Mails, drei Word-Dateien und sieben klar fiktive JPG-Personendatenkarten. Alle Arbeitsunterlagen sind auf Deutsch.

Satzung und Gesellschaftervereinbarung sind kurze Entwürfe. Die Namen stehen getrennt auf den Personendatenkarten; sie sollen bei der Bearbeitung eingesetzt werden. Einzelne Mehrheits- und Organisationsentscheidungen bleiben ausdrücklich offen. Die JPGs sind keine Ausweise und dokumentieren keine Identitätsprüfung.

> Lesen Sie die Akte Topf & Tacheles. Ergänzen Sie belegte Angaben in den beiden Vertragsentwürfen, prüfen Sie die Stimmrechte und Mehrheiten anhand der geäußerten Wünsche und fragen Sie nur nach den noch notwendigen Entscheidungen. Erstellen Sie kurze, abgestimmte deutsche Entwürfe zur Durchsicht.

## Umfangreicherer Fall: Röschen Tech

Die Akte `gesellschaftsgruender-streit-roeschen-tech` zeigt eine Gründung, die nicht lehrbuchartig glatt läuft: drei Gründer, ein technisches Produkt, IP-Fragen, Series-A-Druck, B-Shares, Bezugsrechtsstreit, KYC-Rückfragen, Registerlogik, Gründer-Vesting, Leaver-Risiken, Datenschutz-/KI-Fragen und ein Konflikt, der parallel über Notar, Bank, Investorin, Beirat und Registergericht läuft.

Sie enthält unter anderem Satzungsentwurf, Gesellschaftervereinbarung, Cap-Table-Varianten, E-Mails, Register-/Notarvermerke, KYC-Nachfragen, IP-/Open-Source-Notizen, Vesting-Matrix, Board Pack, Cash-Burn-Übersicht, Compliance-Startliste, CSV-Tabellen und ein Gesamt-PDF.

## Stoppschilder

- **Notar:** Beurkundung, Handelsregisteranmeldung und bestimmte Vollmachten müssen notariell laufen.
- **Steuer:** Rechtsform, Holding, Sacheinlage, ESOP/VSOP, USt und Verrechnungspreise gehören früh in steuerkundige Hände.
- **Aufsicht und Erlaubnis:** Finanzen, Versicherung, Kryptowerte, Zahlungsdienste, Medizin, Bewachung, Handwerk, Lebensmittel, Transport und ähnliche Modelle brauchen einen Erlaubnischeck vor dem Start.
- **Krise:** Bei Zahlungsunfähigkeit, Überschuldung, hälftigem Stammkapitalverlust oder Liquiditätslücke geht es nicht mehr nur um Gründung, sondern um Organhaftung und Insolvenzrecht.
- **Streit:** Bei Gesellschafterstreit, Registerblockade oder Investorendruck braucht es eine Beweis-, Fristen- und Eskalationsstrategie.

## Quellenhygiene

Gesetzesstände, Registervorgaben, Formularwege und Behördenpraxis sind vor produktiver Verwendung live zu prüfen. Rechtsprechung wird nicht aus Modellwissen zitiert; sie muss vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle verifiziert werden.

Wichtige Startanker sind insbesondere BGB §§ 705 ff., HGB §§ 105 ff. und §§ 161 ff., GmbHG, AktG, PartGG, GenG, GwG/Transparenzregister, GewO, AO/UStG, SGB IV/SGB VII, InsO § 15a und die Register-/Notarvorgaben nach BeurkG und HRegV.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **11 auswählbare Skills**. Die **114 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Gründung und Gesellschaftsvertrag | [`gruendung-und-gesellschaftsvertrag-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/gruendung-und-gesellschaftsvertrag-bearbeiten/SKILL.md) |
| 3. Organe und Vertretung | [`organe-und-vertretung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/organe-und-vertretung-bearbeiten/SKILL.md) |
| 4. Gesellschafter und Beschlussfassung | [`gesellschafter-und-beschlussfassung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/gesellschafter-und-beschlussfassung-bearbeiten/SKILL.md) |
| 5. Kapital und Strukturmaßnahmen | [`kapital-und-strukturmassnahmen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/kapital-und-strukturmassnahmen-bearbeiten/SKILL.md) |
| 6. Register und Vollzug | [`register-und-vollzug-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/register-und-vollzug-bearbeiten/SKILL.md) |
| 7. Haftung und Gesellschaftsstreit | [`haftung-und-gesellschaftsstreit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/haftung-und-gesellschaftsstreit-bearbeiten/SKILL.md) |
| 8. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 9. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Gründung deutscher Gesellschaften: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: gesellschaftsgründer — Gründungsassistent für deutsche. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/einstieg-routing/SKILL.md) |
| [`gesellschafter-und-beschlussfassung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/gesellschafter-und-beschlussfassung-bearbeiten/SKILL.md) | Gründung deutscher Gesellschaften: Gesellschafter und Beschlussfassung: Einladung, Stimmrecht, Mehrheiten, Informationsrecht, Treuepflicht und Minderheitenschutz im konkreten Konflikt bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/gesellschafter-und-beschlussfassung-bearbeiten/SKILL.md) |
| [`gruendung-und-gesellschaftsvertrag-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/gruendung-und-gesellschaftsvertrag-bearbeiten/SKILL.md) | Gründung deutscher Gesellschaften: Gründung und Gesellschaftsvertrag: Rechtsform, Kapital, Satzung, Beteiligung und Vollzug bis zum abgestimmten Gründungstext führen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/gruendung-und-gesellschaftsvertrag-bearbeiten/SKILL.md) |
| [`haftung-und-gesellschaftsstreit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/haftung-und-gesellschaftsstreit-bearbeiten/SKILL.md) | Gründung deutscher Gesellschaften: Haftung und Gesellschaftsstreit: Pflichtverletzung, Anspruchsinhaber, Darlegung, Eilrechtsschutz und Einigung zu einem begründeten Arbeitsprodukt führen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/haftung-und-gesellschaftsstreit-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Gesellschaftsgründer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/juristischer-argumentationskern/SKILL.md) |
| [`kapital-und-strukturmassnahmen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/kapital-und-strukturmassnahmen-bearbeiten/SKILL.md) | Gründung deutscher Gesellschaften: Kapital und Strukturmaßnahmen: Finanzierung, Kapitalerhaltung, Umwandlung, Übertragung und Ausscheiden mit den Vertrags- und Registerunterlagen abgleichen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/kapital-und-strukturmassnahmen-bearbeiten/SKILL.md) |
| [`organe-und-vertretung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/organe-und-vertretung-bearbeiten/SKILL.md) | Gründung deutscher Gesellschaften: Organe und Vertretung: Geschäftsführung, Aufsichtsrat, Bestellung, Abberufung, Vollmacht und Vertretungsmacht anhand der Beschlüsse prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/organe-und-vertretung-bearbeiten/SKILL.md) |
| [`register-und-vollzug-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/register-und-vollzug-bearbeiten/SKILL.md) | Gründung deutscher Gesellschaften: Register und Vollzug: Anmeldung, Gesellschafterliste, Publizität, Nachweise und Zwischenverfügung bis zum einreichbaren Dokument bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/register-und-vollzug-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Gründung deutscher Gesellschaften: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: gesellschaftsgründer — Gründungsassistent für deutsche. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsgruender/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

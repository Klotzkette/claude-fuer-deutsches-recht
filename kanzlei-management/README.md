# Kanzlei Management

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Mega-Plugin für Kanzlei-Management: Managing Partner, Management Committee, Cashflow, Pricing, UBT, FTE, Utilization, WIP, Associates, Partnerkreis und Dashboards.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`kanzlei-management.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/kanzlei-management.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/kanzlei-management.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/kanzlei-management-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/kanzlei-management-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/kanzlei-management.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/kanzlei-management.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Kanzlei Management:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`kanzlei-management.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/kanzlei-management.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`kanzlei-management-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/kanzlei-management-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`kanzlei-management-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/kanzlei-management-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Falkenried & Partner mbB — Managementakte Q2/2026](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/README.md) | [Gesamt-PDF](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/gesamt-pdf/kanzlei-management-falkenried-partnerkreis-q2-2026_gesamt.pdf) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Ein Mega-Plugin für die Leitung einer deutschen mittelständischen Kanzlei aus Sicht des Managing Partners, der Geschäftsführung, eines Management Committees oder einer starken COO-/CFO-Rolle.

Es geht um das ganze schöne, anstrengende Betriebsleben: Partnerkreis, Praxisgruppen, Cashflow, Pricing, Associate-Retention, WIP, UBT, FTE, Utilization, offene Posten, Business Development, Legal Tech, Fristen- und Qualitätsrisiken, Egos, Kultur und die Frage, wie man eine Kanzlei führt, ohne sie in ein Controlling-Museum oder einen Stuhlkreis zu verwandeln.

## Kaltstart

1. Rolle und Steuerungsauftrag klären: Managing Partner, MC, COO, CFO, Praxisgruppenleitung oder externer Kanzleiberater.
2. Kanzleiprofil erfassen: Berufsträger/FTE, Equity-/Salary-Partner, Associates, Assistenz, Umsatz, Praxisgruppen, Standorte, IT, Mandantenmix.
3. Akute Lage bestimmen: Wachstum, Cash-Druck, WIP-Stau, Associate-Flucht, Partnerkonflikt, Pricing-Chaos, Nachfolge, Mandantenverlust oder Tech-Investition.
4. Nur bei passendem Auftrag ein Dashboard wählen: Executive Cockpit, Cash/WIP/AR, Utilization, UBT, Practice Group, Partner Scorecard, Associate Health, Pipeline oder Crisis Board. Eine bestellte Entscheidungsvorlage wird direkt aus vorhandenen Zahlen und Unterlagen ausgearbeitet; fehlende entscheidende Annahmen gezielt klären.
5. Entscheidung erzeugen: Der Output muss in eine echte Managemententscheidung münden: Beschlussvorlage, Gesprächsleitfaden, Maßnahmenplan, Zahlenpaket oder Eskalationsnotiz.

## Kern-Dashboards

| Dashboard | Zweck |
| --- | --- |
| Executive Cockpit | Gesamtbild für MC: Cash, WIP, AR, Utilization, UBT, Pipeline, People Risk, Risikothemen |
| Cash/WIP/AR | Liquidität, offene Posten, Lock-up, DSO, Abrechnungsstau und konkrete Partneraktionen |
| Utilization/Capacity | FTE, Soll-/Ist-Auslastung, Überlast, Leerlauf, Staffing und Ausbildungswert |
| Pricing/Realization | Stundensätze, Rabatte, Festpreise, Realization, Write-offs und Matter Profitability |
| Partner Scorecard | Umsatz, Marge, WIP, Collections, BD, Teambeitrag, Qualität und Kulturwirkung |
| Associate Health | Belastung, Feedback, Lernkurve, Mandatsmix, Urlaub, Kündigungsrisiko |
| Pipeline | Leads, Pitches, Wahrscheinlichkeit, erwartete Fees, Kapazität und Konflikte |

## Berufsrechtliche Leitplanken

Managemententscheidungen bleiben Kanzleientscheidungen. Bei Vergütung und Pricing müssen RVG, Vergütungsvereinbarung, § 49b BRAO, § 3a RVG, § 10 RVG, BORA, Mandatsgeheimnis, Datenschutz, Interessenkollisionen, beA-/ERV-Pflichten und Fristenorganisation immer live geprüft werden. Keine erfundenen Fundstellen, keine Paywall-Blindzitate, keine Scheinpräzision in Kennzahlen.

## Typische Outputs

- Partnerklausur-Paket mit Zahlen, Konfliktlandkarte und Beschlussvorschlägen.
- 13-Wochen-Cashflow mit Rechnungswelle, Partnerentnahmen und Engpasswochen.
- WIP-Aging und Collections-Plan nach Partner, Mandat und Mandantenbeziehung.
- Pricing-Memo für Stundensatz, Festpreis, Retainer, Cap oder Blended Rate.
- Associate-Retention-Radar mit konkreten Gegenmaßnahmen.
- MC-Board-Pack als monatlicher Managementbericht.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **11 auswählbare Skills**. Die **101 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/juristischer-argumentationskern/SKILL.md), [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/kaltstart-triage/SKILL.md) |
| 2. Kanzleistrategie, Markt und Praxisportfolio | [`strategie-markt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/strategie-markt-bearbeiten/SKILL.md) |
| 3. Partnerkreis, Vergütung und Nachfolge | [`partner-governance-nachfolge-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/partner-governance-nachfolge-bearbeiten/SKILL.md) |
| 4. Personal, Karriere und Kapazitätsplanung | [`personal-kapazitaet-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/personal-kapazitaet-bearbeiten/SKILL.md) |
| 5. Honorarmodelle, Pricing und Mandatswirtschaftlichkeit | [`honorar-pricing-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/honorar-pricing-bearbeiten/SKILL.md) |
| 6. Liquidität, WIP, Forderungen und Finanzabschluss | [`finanzen-liquiditaet-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/finanzen-liquiditaet-bearbeiten/SKILL.md) |
| 7. Mandantenentwicklung, Akquise und Feedback | [`mandanten-entwicklung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/mandanten-entwicklung-bearbeiten/SKILL.md) |
| 8. Kanzleisysteme, Prozesse und Wissensmanagement | [`systeme-prozesse-wissen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/systeme-prozesse-wissen-bearbeiten/SKILL.md) |
| 9. Berufsrisiken, Fristen, Datenschutz und Kontrollen | [`berufsrisiken-kontrollen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/berufsrisiken-kontrollen-bearbeiten/SKILL.md) |
| 10. Managementbericht, Kennzahlen und Entscheidung | [`managementbericht-entscheidung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/managementbericht-entscheidung-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`berufsrisiken-kontrollen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/berufsrisiken-kontrollen-bearbeiten/SKILL.md) | Prüfe organisatorische Risiken, Versicherung, Fristenaufsicht, Interessenkonflikte und Datenzugang und arbeite belegte Kontrollen aus. Die zugeordneten Fachmodule und Vorlagen werden nach dem konkreten Auftrag gelesen und zusammengeführt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/berufsrisiken-kontrollen-bearbeiten/SKILL.md) |
| [`finanzen-liquiditaet-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/finanzen-liquiditaet-bearbeiten/SKILL.md) | Leite Cashflow, unfertige Leistungen, offene Forderungen und Monatsabschluss aus abgestimmten Finanzdaten ab und formuliere konkrete Maßnahmen. Die zugeordneten Fachmodule und Vorlagen werden nach dem konkreten Auftrag gelesen und zusamm... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/finanzen-liquiditaet-bearbeiten/SKILL.md) |
| [`honorar-pricing-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/honorar-pricing-bearbeiten/SKILL.md) | Berechne Honorar, Rabatt, Budget, Realisierung und Mandatsprofitabilität mit transparenten Annahmen; RVG und Honorarvereinbarung getrennt beachten. Die zugeordneten Fachmodule und Vorlagen werden nach dem konkreten Auftrag gelesen und zu... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/honorar-pricing-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Kanzlei Management ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/kaltstart-triage/SKILL.md) | Für Kaltstart Kanzlei-Management: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/kaltstart-triage/SKILL.md) |
| [`managementbericht-entscheidung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/managementbericht-entscheidung-bearbeiten/SKILL.md) | Verbinde belastbare Kennzahlen, Risiken und Alternativen in einem verständlichen Bericht oder Entscheidungsvorschlag; Datenlücken sichtbar machen. Die zugeordneten Fachmodule und Vorlagen werden nach dem konkreten Auftrag gelesen und zus... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/managementbericht-entscheidung-bearbeiten/SKILL.md) |
| [`mandanten-entwicklung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/mandanten-entwicklung-bearbeiten/SKILL.md) | Bearbeite Zielmandanten, Pipeline, Pitch, Kundenbindung und Rückmeldungen mit Bezug auf den tatsächlichen Mandantenbestand. Die zugeordneten Fachmodule und Vorlagen werden nach dem konkreten Auftrag gelesen und zusammengeführt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/mandanten-entwicklung-bearbeiten/SKILL.md) |
| [`partner-governance-nachfolge-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/partner-governance-nachfolge-bearbeiten/SKILL.md) | Bearbeite Partnerstruktur, Leistung, Vergütung, Eintritt, Austritt und Nachfolge anhand der vereinbarten Governance und wirtschaftlichen Daten. Die zugeordneten Fachmodule und Vorlagen werden nach dem konkreten Auftrag gelesen und zusamm... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/partner-governance-nachfolge-bearbeiten/SKILL.md) |
| [`personal-kapazitaet-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/personal-kapazitaet-bearbeiten/SKILL.md) | Verbinde Personalbedarf, Rekrutierung, Entwicklung, Auslastung und Belastungsgrenzen mit konkreten Teams und Mandaten. Die zugeordneten Fachmodule und Vorlagen werden nach dem konkreten Auftrag gelesen und zusammengeführt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/personal-kapazitaet-bearbeiten/SKILL.md) |
| [`strategie-markt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/strategie-markt-bearbeiten/SKILL.md) | Arbeite Zielmarkt, Positionierung, Praxisgruppen und Standortstrategie zu einer begründeten unternehmerischen Entscheidung aus. Die zugeordneten Fachmodule und Vorlagen werden nach dem konkreten Auftrag gelesen und zusammengeführt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/strategie-markt-bearbeiten/SKILL.md) |
| [`systeme-prozesse-wissen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/systeme-prozesse-wissen-bearbeiten/SKILL.md) | Gestalte Daten- und Dokumentenflüsse, Wissensbestand, Automatisierung und Technologievorhaben aus dem tatsächlichen Kanzleibetrieb. Die zugeordneten Fachmodule und Vorlagen werden nach dem konkreten Auftrag gelesen und zusammengeführt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-management/skills/systeme-prozesse-wissen-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

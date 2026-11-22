# Plugin für die studentische Rechtsberatungsstelle

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Pro-Bono- und Rechtsberatungsstellen (RDG-konform): Mandantenintake, Fristenkontrolle, Übergabe am Semesterende, mandantenfreundliche Briefe.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`rechtsberatungsstelle.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/rechtsberatungsstelle.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/rechtsberatungsstelle.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/rechtsberatungsstelle-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/rechtsberatungsstelle-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/rechtsberatungsstelle.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/rechtsberatungsstelle.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Plugin für die studentische Rechtsberatungsstelle:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`rechtsberatungsstelle.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/rechtsberatungsstelle.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`rechtsberatungsstelle-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/rechtsberatungsstelle-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`rechtsberatungsstelle-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/rechtsberatungsstelle-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Rechtsberatungsstelle Köln-Kalk — Monatsmix August 2026, Dr. Pellbach-Tannenfels](../testakten/rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach/README.md) | [Gesamt-PDF](../testakten/rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach/gesamt-pdf/rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach_gesamt.pdf) | [`testakte-rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-ergaenzung-v1.0.0/testakte-rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach.zip) | [`testakte-rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-ergaenzung-v1.0.0/testakte-rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach-einzelpdfs.zip) |
| [Akte Reimers: Verbraucherinsolvenz, ehemaliger Geschäftsführer und Schuldenbereinigungsplan](../testakten/verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung/README.md) | [Gesamt-PDF](../testakten/verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung/gesamt-pdf/verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung_gesamt.pdf) | [`testakte-verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung.zip) | [`testakte-verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
*KI-gestützte Unterstützung für universitäre Refugee Law Clinics, studentische Rechtsberatungen und Pro-Bono-Initiativen – mit klaren RDG-Grenzen.*

Ein Plugin für Einrichtungen, in denen Studenten – unter Anleitung zur Anleitung berechtigter Volljuristen – unentgeltliche Rechtsberatung für Menschen leisten, die sich anwaltliche Hilfe nicht leisten können oder keinen Zugang dazu haben: Aufenthalts- und Asylrecht, Sozialrecht (SGB II/XII, SGB IX), Mietrecht, Verbraucherrecht, Familienrecht.

**Jede Ausgabe ist ein Entwurf für die Analyse durch Studenten und die Freigabe durch den anleitenden Volljuristen – gekennzeichnet, gestuft und protokolliert. Das Plugin gibt Struktur; die Studentenn denken juristisch; der Anleiter prüft und gibt frei. Nichts verlässt die Beratungsstelle ohne Durchlaufen dieses Aufsichtsmodells.**

---

## Wichtiger Hinweis: Rechtliche Grenzen nach dem RDG

Für eine unentgeltliche studentische Beratung außerhalb persönlicher Nähebeziehungen ist Paragraf 6 Absatz 2 RDG maßgeblich. Er verlangt eine entsprechend befugte oder zum Richteramt befähigte Person oder deren tatsächliche Anleitung. Eine Nummer 2 enthält dieser Absatz nicht. Andere Träger können im Rahmen der Paragrafen 7 oder 8 RDG befugt sein; das muss für Träger, Person und Aufgabe konkret feststehen. Das Plugin selbst vermittelt keine Beratungsbefugnis.

**Für Studenten gilt:**
- Dieses studentische Beratungsmodell verlangt tatsächliche Anleitung nach Paragraf 6 Absatz 2 RDG: Einweisung, Fortbildung und erforderlichenfalls Mitwirkung im Einzelfall.
- Schriftsätze, Stellungnahmen und Widersprüche sind **Entwürfe** – keine fertigen, abzusendenden Dokumente.
- Jede strategische Entscheidung (Klage ja/nein, Rücknahme, Vergleich) liegt beim anleitenden Anwalt.
- Wer den Beratungsauftrag übernimmt und wer freigibt, muss aus der konkreten Träger- und Anleitungsorganisation hervorgehen; das ist nicht automatisch dieselbe Person.
- Vertraulichkeit auch nach Semesterende sichern. Anwaltliche Berufspflichten und strafrechtlicher Geheimnisschutz richten sich nach der tatsächlichen Rolle und Einbindung, nicht allein nach der Bezeichnung als studentische Beratung.

---

## Das Problem, das dieses Plugin löst

Beratungsstellen sind strukturell kapazitätsbeschränkt. Ein anleitender Jurist betreut 5–12 Studenten. Jede Studenten trägt eine Handvoll Mandate, während sie gleichzeitig Lehrveranstaltungen besucht. Studenten wechseln jedes Semester. Verwaltungsaufgaben – Intake-Protokoll, Erstentwürfe, Rechercheansätze, Statusberichte, Semesterübergaben – verschlingen Stunden, die besser in die juristische Analyse investiert wären. Das Ergebnis: lange Wartelisten, begrenzte Fallzahlen, Ratsuchende, die aufgeben.

Dieses Plugin senkt die Zeitkosten für alles **rund um die Rechtsarbeit**, damit dieselben Studentenn und ihr Anleiter deutlich mehr Mandanten sinnvoll betreuen können – und die Studentenn mehr Zeit für Analyse und Strategie haben, die das Kernanliegen studentischer Rechtsbildung ausmacht.

**Es beschleunigt die nicht-lehrenden Teile. Es bewahrt die analytische Arbeit.** Das ist das Gestaltungsprinzip.

---

## Wer nutzt das Plugin?

| Rolle | Startet | Erhält |
|---|---|---|
| **Anleitender Volljurist** | `/kaltstart-interview` (einmalig), `/anleiter-pruefwarteschlange` (wenn formelle Prüfung aktiviert) | Konfigurierter Beratungsstellenkontext, Prüfung studentischer Arbeit |
| **Studenten** | `/einarbeitung` (Semesterbeginn), dann `/mandant-aufnahme`, `/entwurf`, `/memo`, `/recherche-start`, `/status`, `/mandantenbrief` | Strukturierte Arbeitshilfen, Entwürfe, Rechercheeinstiege |
| **Mandant** | – | Empfängt fertig geprüfte Briefe (Studentenr + Anleiter haben freigegeben) |

---

## Schnellstart

```
/rechtsberatungsstelle:auftrag-und-adressat-bearbeiten Thema: kaltstart-interview   # Anleiter: Beratungsstelle konfigurieren
/rechtsberatungsstelle:normstruktur-bearbeiten Thema: einarbeitung                   # Studentenr: Einarbeitung zum Semesterbeginn
/rechtsberatungsstelle:arbeitsprodukt-bearbeiten Thema: mandant-aufnahme          # Neues Mandat aufnehmen
/rechtsberatungsstelle:arbeitsprodukt-bearbeiten Thema: memo                   # Gutachtenstil-Memo erstellen
/rechtsberatungsstelle:arbeitsprodukt-bearbeiten Thema: entwurf-einarbeitung-einfache-sprache                  # Schriftsatz entwerfen
/rechtsberatungsstelle:arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten Thema: fristen-fristenkontrolle-rdg              # Fristen prüfen
/rechtsberatungsstelle:arbeitsprodukt-bearbeiten Thema: mandantenbrief-memo-rbs-beratungshilfe          # Mandantenbrief in einfacher Sprache
/rechtsberatungsstelle:normstruktur-bearbeiten Thema: semester-uebergabe       # Semesterübergabe vorbereiten
```

---

## Beratungsstellentypen, die dieses Plugin unterstützt

### Universitäre Refugee Law Clinics (RLC)

Hochschulverankerte Kliniken wie die **Refugee Law Clinic Berlin** (HU Berlin/FU Berlin), die **Refugee Law Clinic Bremen** (Universität Bremen) oder die **Refugee Law Clinic Köln** (Universität zu Köln) beraten Asylsuchende und Geduldete zu Fragen des AsylG, AufenthG und SGB II. Besonderheiten:
- Kurze Fristen (§§ 36, 74 AsylG): Klagen gegen BAMF-Bescheide oft binnen 1–2 Wochen nach Zustellung.
- Sprachbarrieren: Dolmetscher-Koordination ist Teil des Intakes.
- Bei Behinderung die Eingliederungshilfe und Paragraf 100 SGB IX prüfen. Aufenthaltsstatus und insbesondere ein Bezug zum AsylbLG sind entscheidend; es besteht kein pauschaler Anspruch aller Geflüchteten.

### Studentische Rechtsberatung nach Paragraf 6 Absatz 2 RDG

Allgemeine studentische Beratungsstellen an Universitäten (oft "JuRI", "Jura hilft" o. ä.). Fokus: SGB II, Mietrecht, Verbraucherrecht, Familienrecht. Die Anleitung erfolgt durch eine zur entgeltlichen Erbringung dieser Rechtsdienstleistung befugte oder zum Richteramt befähigte Person. Eine Habilitation ist keine Voraussetzung des Paragrafen 6 Absatz 2 RDG.

### AnwVer/DAV Pro-Bono-Initiativen

Anwaltsverein-getragene Pro-Bono-Programme (z. B. **Pro Bono Berlin e. V.**, **DAV Pro Bono**): hier beraten zugelassene Anwälte direkt, die Plugin-Komponenten `entwurf`, `memo` und `recherche-start` unterstützen die Mandatsarbeit.

### Verbraucherzentralen (§ 8 RDG)

Verbraucherzentralen besitzen eine Sondererlaubnis nach § 8 Abs. 1 Nr. 4 RDG. Das Plugin unterstützt Standardfälle: Mieterhöhung, Kündigung, AGB-Kontrolle (§§ 305 ff. BGB), Energiekosten-Nachforderungen.

### Sozialberatung

Verbände der freien Wohlfahrtspflege und ihre Untergliederungen können innerhalb ihres Aufgabenbereichs nach Paragraf 8 Absatz 1 Nummer 5 RDG beraten; die organisatorischen Anforderungen sind zusätzlich zu prüfen. Schwerpunkte sind SGB II, SGB XII, Eingliederungshilfe, Rentenrecht und Pflegeleistungen. Pflegegeld für selbst beschaffte Pflegehilfen gehört zu Paragraf 37 SGB XI, nicht zu einem Paragrafen 76b SGB IX.

---

## Beispiele: Pro-Bono-Initiativen in Berlin und Bremen

| Initiative | Ort | Schwerpunkt | Rechtsgrundlage |
|---|---|---|---|
| Refugee Law Clinic Berlin (HU/FU) | Berlin | AsylG, AufenthG, SGB II | Paragraf 6 Absatz 2 RDG |
| Pro Bono Berlin e. V. | Berlin | Zivilrecht, Mietrecht, Familienrecht | Zugelassene Anwälte |
| Berliner Mieterverein – Rechtsberatung | Berlin | Mietrecht | Paragraf 7 Absatz 1 Nummer 1 RDG: Mitgliederberatung innerhalb des Satzungszwecks; Voraussetzungen konkret prüfen |
| Refugee Law Clinic Bremen | Bremen | AsylG, AufenthG | Paragraf 6 Absatz 2 RDG |
| Verbraucherzentrale Bremen | Bremen | Verbraucherrecht, Mietrecht | § 8 I Nr. 4 RDG |
| JuRI – Juristische Interessenvertretung (Uni Bremen) | Bremen | SGB II, allg. Zivilrecht | Paragraf 6 Absatz 2 RDG |
| Caritas Berlin – Migrationsberatung | Berlin | AufenthG, SGB II | Paragraf 8 Absatz 1 Nummer 5 RDG, innerhalb des Aufgabenbereichs |

---

## Fachbereiche und Skills

| Skill | Zweck | Primäre Normen |
|---|---|---|
| `leitfaden-erstellen` | Leitfaden zum Aufbau einer Beratungsstelle | RDG, BRAO |
| `mandanten-kommunikations-log` | Mandantenkommunikations-Logbuch | § 43a BRAO, § 203 StGB |
| `mandant-aufnahme` | Intake mit RDG-Konfliktprüfung | Paragraf 6 Absatz 2 RDG |
| `mandantenbrief` | Mandantenbrief in einfacher Sprache | BORA |
| `rechtsberatungsstelle-kaltstart-interview` | Ersteinrichtung der Beratungsstelle | RDG, BRAO |
| `rechtsberatungsstelle-anpassen` | Beratungsstellenprofil anpassen | – |
| `fristen` | Fristenkontrolle | § 84 SGG, § 74 VwGO, §§ 36, 74 AsylG |
| `entwurf` | Schriftsatzentwurf | ZPO, VwGO, SGG |
| `formular-erzeugung` | Formularerstellung (PKH, BerHG, KSchG) | §§ 114 ff. ZPO, BerHG |
| `memo` | Memo im Gutachtenstil | – |
| `einfache-sprache-briefe` | Einfache Sprache | BORA |
| `einarbeitung` | Einarbeitung Studenten | Paragraf 6 Absatz 2 RDG |
| `recherche-start` | Rechercheeinstieg | juris, Beck-Online, gesetze-im-internet.de |
| `semester-uebergabe` | Semesterübergabe | – |
| `status` | Statusbericht | – |
| `anleiter-pruefwarteschlange` | Aufsichts-Reviewqueue | Paragraf 6 Absatz 2 RDG, § 43a BRAO |

---

## Qualitätssicherung

Gezielter Quellenabgleich am 16.10.2026: [Paragraf 6 RDG](https://www.gesetze-im-internet.de/rdg/__6.html), [Paragraf 7 RDG](https://www.gesetze-im-internet.de/rdg/__7.html) und [Paragraf 8 RDG](https://www.gesetze-im-internet.de/rdg/__8.html) wurden zu Unentgeltlichkeit, Anleitung und Trägerbefugnissen gelesen. [Paragraf 100 SGB IX](https://www.gesetze-im-internet.de/sgb_9_2018/__100.html) begrenzt Eingliederungshilfe für ausländische Personen; [Paragraf 37 SGB XI](https://www.gesetze-im-internet.de/sgb_11/__37.html) betrifft Pflegegeld. Kein Nachweis der heutigen Organisation oder individuellen Befugnis der beispielhaft genannten Einrichtungen und keine vollständige Berufsrechtsprüfung. Weitere gezielte Korrekturen und Grenzen stehen im [Quellenvermerk](references/gezielter-quellenabgleich-2026-10-16.md).

Alle studentischen Outputs tragen den Vermerk:

> **[KI-GESTÜTZTER ENTWURF – Analyse durch Studenten und Freigabe durch anleitenden Volljuristen erforderlich. Kein Versand ohne Prüfung.]**

Nur der anleitende Jurist kann diesen Vermerk entfernen. Dokumente, die diesen Vermerk tragen, dürfen nicht unmittelbar an Mandanten oder Behörden gesendet werden.

---

## Zitierweise

Alle juristischen Quellen folgen `../references/zitierweise.md`. Beispiele:
- Krenzler, in: Krenzler (Hrsg.), RDG, 2. Aufl. 2021, § 6 Rn. 45.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **9 auswählbare Skills**. Die **60 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`anleiter-pruefwarteschlange`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/anleiter-pruefwarteschlange/SKILL.md), [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Auftrag und Adressat | [`auftrag-und-adressat-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/auftrag-und-adressat-bearbeiten/SKILL.md) |
| 3. Normstruktur | [`normstruktur-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/normstruktur-bearbeiten/SKILL.md) |
| 4. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 5. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anleiter-pruefwarteschlange`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/anleiter-pruefwarteschlange/SKILL.md) | Für Supervisoren-Prüfwarteschlange (Optional): ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/anleiter-pruefwarteschlange/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Studentische Rechtsberatungsstelle: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Studentische Rechtsberatungsstelle: Arbeitsprodukt: Kurzvermerk, Gutachten, Schriftsatzkern, Mandantenbrief, Entscheidungsbaum oder Zitierkontrolle vollständig ausformulieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`auftrag-und-adressat-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/auftrag-und-adressat-bearbeiten/SKILL.md) | Studentische Rechtsberatungsstelle: Auftrag und Adressat: Rechtsfrage, gewünschtes Produkt, Empfänger, Frist und Entscheidungsschwelle in einem Satz festlegen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/auftrag-und-adressat-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Plugin für die studentische Rechtsberatungsstelle. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/einstieg-routing/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/juristischer-argumentationskern/SKILL.md) | Beratungsanliegen bis zur verständlichen Handlungshilfe bearbeiten. Verarbeitet vorhandene Unterlagen, verbindet entscheidende Fachprüfungen und belegte Quellen, erstellt das beauftragte Ergebnis und führt denselben Vorgang nach neuen An... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/juristischer-argumentationskern/SKILL.md) |
| [`normstruktur-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/normstruktur-bearbeiten/SKILL.md) | Studentische Rechtsberatungsstelle: Normstruktur: Anspruchsgrundlage oder Prüfungsmaßstab in Tatbestandsmerkmale, Rechtsfolge, Einwendungen und Beweislast zerlegen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/normstruktur-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Studentische Rechtsberatungsstelle: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Plugin für die studentische Rechtsberatungsstelle. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsberatungsstelle/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.

# Plugin: status-navigator-step-plan

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Status-Navigator und Step-Plan-Macher. Reine Dokumentenverarbeitung mit 35 Skills. Strukturiert disparate Dokumentenlagen in eine mehrseitige Excel-Arbeitsmappe und optional ein Padlet-Shelf mit Reitern Überblick, Vorhanden, Fehlend und Workflow. Keine rechtliche Bewertung.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/status-navigator-step-plan.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/status-navigator-step-plan.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart als Markdown laden und zusammen mit den Unterlagen öffnen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Plugin: status-navigator-step-plan:

> Lies zuerst alle Dateien im ausgewählten Ordner. Bearbeite den Vorgang mit diesem Fachgebiet. Beginne mit folgendem Arbeitsschritt: Dokumentenregister: Datei, Typ, Datum, Version, Autor, Signatur, Bezug, Fundstelle, Status und Lücke. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`status-navigator-step-plan.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/status-navigator-step-plan.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/status-navigator-step-plan-schnellstart.md" download><code>status-navigator-step-plan-schnellstart.md</code></a> |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/status-navigator-step-plan-werkstatt.md" download><code>status-navigator-step-plan-werkstatt.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [LausitzStorage 200 GmbH i.G. (Batteriegroßspeicher Jänschwalde/Peitz)](../testakten/status-navigator-batteriespeicher-jaenschwalde-peitz/README.md) | [Gesamt-PDF](../testakten/status-navigator-batteriespeicher-jaenschwalde-peitz/gesamt-pdf/status-navigator-batteriespeicher-jaenschwalde-peitz_gesamt.pdf) | [`testakte-status-navigator-batteriespeicher-jaenschwalde-peitz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-status-navigator-batteriespeicher-jaenschwalde-peitz.zip) | [`testakte-status-navigator-batteriespeicher-jaenschwalde-peitz-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-status-navigator-batteriespeicher-jaenschwalde-peitz-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
**Status-Navigator und Step-Plan-Macher**.

## Was dieses Plugin ist — und was es ausdrücklich nicht ist

Dies ist ein Plugin reiner **Dokumentenverarbeitung**. Es enthält — bewusst und als einzige Ausnahme im Repo — **keine Normen- und Rechtsprechungs-Anker** in den Skills. Der Grund: der Status-Navigator strukturiert chaotische Dokumentenlagen, beantwortet die Fragen "Was haben wir?", "Was fehlt?", "Was muss geschehen?" — er bewertet jedoch nichts rechtlich. Die rechtliche Prüfung bleibt anwaltliche Aufgabe.

Alle übrigen Plugins des Repos arbeiten mit verifizierten Norm- und Rechtsprechungs-Zitaten. Dieses Plugin tut das ausdrücklich nicht. Es liefert Reiter, Spalten, Workflow-Schritte und Status-Notes — keine Subsumtion.

## Worum es geht

Anwältinnen und Anwälte aus Restrukturierung, Finanzierung, Gesellschaftsrecht und Transaktionen kennen das Problem: ein Riesenklumpatsch aus Dokumenten fällt ins Mandat. Ungeordnet, disparat, teils widersprüchlich. Zwei Fragen stellen sich immer:

1. **Was ist eigentlich los?**
2. **Was muss jetzt geschehen?**

Der Status-Navigator beantwortet beide — und macht aus einer statischen Bestandsaufnahme einen dynamischen Step-Plan.

## Die Vier-Reiter-Struktur

Das Herzstück ist eine mehrseitige Excel-Arbeitsmappe (nicht eine Chatfenster-Tabelle), bestehend aus mindestens vier Reitern:

| Reiter | Inhalt |
| --- | --- |
| 1 Überblick / Statuslage | Gesamtsituation auf einen Blick: Dokument, Datum, Verfügbarkeit, Unterschriftsstatus, Partei, Rechtsgrundlage, Zweck |
| 2 Vorhandene Dokumente | Detailliste aller vorhandenen Dokumente mit Status und Anmerkungen |
| 3 Fehlende Dokumente | Auflistung der noch fehlenden Dokumente und Nachweise mit Beschaffungspfad |
| 4 Workflow / Next Steps | Konkreter Step-Plan: Schritte in Reihenfolge, Rechtsgrundlage, Unterschrift, Empfänger |

Optional erweiterbar um Fristen, Beteiligte, Rangfolge, Sicherheiten und Hyperlinks zur Dokumentenablage.

## Was der Status-Navigator konkret leistet

1. **Dokumententypen erkennen und einordnen** (Verträge, Erklärungen, Beschlüsse, Cap Tables, Korrespondenz).
2. **Unterschriften und Vollständigkeit prüfen.**
3. **Diskrepanzen und Copy-Paste-Fehler aufdecken.**
4. **Versand- und Zustellungsstatus erfassen.**
5. **Lücken und Fehler in den Tabellen direkt notifizieren.**

## Padlet als Alternativausgabe

Neben der Excel-Arbeitsmappe kann der Status-Navigator denselben Step-Plan als Padlet-Shelf ausspielen. Vier Spalten, eine je Reiter, mit Ampelfarbe pro Karte, Anhängen und Kommentar-Threads. Sinnvoll für verteilte Teams und Mandantenfreigaben; **vor Einsatz Datenschutzprüfung** (siehe Skill `padlet-als-werkzeug`).

## Die 35 Skills im Überblick

### Einstieg und Zieldefinition
- `status-navigator-einstieg`
- `ziel-praezisieren`
- `dokumenten-inventur-grob`

### Dokumententypen erkennen
- `dokumententyp-vertraege`
- `dokumententyp-erklaerungen`
- `dokumententyp-beschluesse`
- `dokumententyp-cap-tables`
- `dokumententyp-korrespondenz`

### Excel-Struktur bauen
- `verexcelung-prinzip`
- `excel-reiter-1-ueberblick`
- `excel-reiter-2-vorhanden`
- `excel-reiter-3-fehlend`
- `excel-reiter-4-workflow`
- `excel-reiter-fristen-optional`
- `excel-reiter-beteiligte-optional`

### Prüfungen
- `unterschriftspruefung`
- `diskrepanzen-aufdecken`
- `copy-paste-fehler-erkennung`
- `zugang-zustellung-pruefung`
- `luecken-notifizieren`
- `ampel-system`

### Anwendungsszenarien
- `szenario-faelligstellung-vollstreckung`
- `szenario-finanzierungsstruktur-bereinigen`
- `szenario-due-diligence`
- `szenario-mandatsuebernahme`
- `szenario-cap-table-bereinigung`

### Erweiterungen
- `erweiterung-rangfolge-reiter`
- `erweiterung-sicherheiten-reiter`
- `erweiterung-hyperlinks`
- `erweiterung-laufende-aktualisierung`

### Padlet (visuelle Alternativausgabe)
- `padlet-als-werkzeug`
- `padlet-spalte-1-ueberblick`
- `padlet-spalte-2-vorhanden`
- `padlet-spalte-3-fehlend`
- `padlet-spalte-4-workflow`

## Wichtiger Hinweis vor der Nutzung

- **Rechtliche Prüfung bleibt anwaltliche Aufgabe.** Der Status-Navigator erfasst und strukturiert — er bewertet nicht abschliessend. Ob eine Kündigung wirksam, ein Zugang erfolgt, ein Formerfordernis erfüllt ist, muss der Anwalt selbst prüfen.
- **Vollständigkeitskontrolle.** Die KI kann Dokumente oder Zusammenhänge übersehen. Jede generierte Tabelle muss anhand der Originaldokumente überprüft werden.
- **Diskrepanz-Hinweise sind Hinweise, keine Befunde.**
- **Datenschutz und Berufsrecht.** Finanzierungs- und Gesellschaftsdokumente enthalten hochsensible Daten. Die Nutzung ist nur mit einem System zulässig, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfüllt.
- **Eigenverantwortung.** Sie tragen die Verantwortung für jede Information und jeden Schritt.

## Excel-Vorlage und Beispiel

Die Excel-Spaltenköpfe folgen der Vorlage `step-plan-document-tracker-template.xlsx`. Ein voll ausgefülltes Beispiel zum Mandat **LausitzStorage 200 GmbH i.G. (Batteriegrossspeicher Jänschwalde / Peitz, Brandenburg)** liegt in der zugehörigen Testakte `testakten/status-navigator-batteriespeicher-jaenschwalde-peitz/`:

- `25_step_plan_excel_lausitzstorage.xlsx` (4 Reiter, ampelgefärbt)
- `26_step_plan_pdf_lausitzstorage.pdf` (4 Reiter als 4 PDF-Seiten, A3 quer)

Dieselbe Datenbasis lässt sich auch als Padlet-Shelf ausspielen (vier Spalten); siehe Padlet-Skills.

## Einordnung

**Status-Navigator und Step-Plan-Macher**: ein Dokumentenstatus- und Workflow-Generator.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`status-navigator-einstieg`](skills/status-navigator-einstieg/SKILL.md), [`szenario-mandatsuebernahme`](skills/szenario-mandatsuebernahme/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`dokumenten-inventur-grob`](skills/dokumenten-inventur-grob/SKILL.md), [`dokumententyp-beschluesse`](skills/dokumententyp-beschluesse/SKILL.md), [`dokumententyp-cap-tables`](skills/dokumententyp-cap-tables/SKILL.md), [`dokumententyp-erklaerungen`](skills/dokumententyp-erklaerungen/SKILL.md), [`dokumententyp-korrespondenz`](skills/dokumententyp-korrespondenz/SKILL.md), [`dokumententyp-vertraege`](skills/dokumententyp-vertraege/SKILL.md), [`luecken-notifizieren`](skills/luecken-notifizieren/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`unterschriftspruefung`](skills/unterschriftspruefung/SKILL.md), [`zugang-zustellung-pruefung`](skills/zugang-zustellung-pruefung/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`excel-reiter-beteiligte-optional`](skills/excel-reiter-beteiligte-optional/SKILL.md), [`excel-reiter-fristen-optional`](skills/excel-reiter-fristen-optional/SKILL.md), [`szenario-finanzierungsstruktur-bereinigen`](skills/szenario-finanzierungsstruktur-bereinigen/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`szenario-faelligstellung-vollstreckung`](skills/szenario-faelligstellung-vollstreckung/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`copy-paste-fehler-erkennung`](skills/copy-paste-fehler-erkennung/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`ampel-system`](skills/ampel-system/SKILL.md), [`diskrepanzen-aufdecken`](skills/diskrepanzen-aufdecken/SKILL.md), [`erweiterung-hyperlinks`](skills/erweiterung-hyperlinks/SKILL.md), [`erweiterung-laufende-aktualisierung`](skills/erweiterung-laufende-aktualisierung/SKILL.md), [`erweiterung-rangfolge-reiter`](skills/erweiterung-rangfolge-reiter/SKILL.md), [`erweiterung-sicherheiten-reiter`](skills/erweiterung-sicherheiten-reiter/SKILL.md), [`excel-reiter-1-ueberblick`](skills/excel-reiter-1-ueberblick/SKILL.md), [`excel-reiter-2-vorhanden`](skills/excel-reiter-2-vorhanden/SKILL.md), [`excel-reiter-3-fehlend`](skills/excel-reiter-3-fehlend/SKILL.md), [`excel-reiter-4-workflow`](skills/excel-reiter-4-workflow/SKILL.md), [`padlet-als-werkzeug`](skills/padlet-als-werkzeug/SKILL.md), [`padlet-spalte-1-ueberblick`](skills/padlet-spalte-1-ueberblick/SKILL.md), [`padlet-spalte-2-vorhanden`](skills/padlet-spalte-2-vorhanden/SKILL.md), [`padlet-spalte-3-fehlend`](skills/padlet-spalte-3-fehlend/SKILL.md), [`padlet-spalte-4-workflow`](skills/padlet-spalte-4-workflow/SKILL.md), [`szenario-cap-table-bereinigung`](skills/szenario-cap-table-bereinigung/SKILL.md), [`szenario-due-diligence`](skills/szenario-due-diligence/SKILL.md), [`verexcelung-prinzip`](skills/verexcelung-prinzip/SKILL.md), ... plus 1 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 36 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; der Direktdownload lädt dieselbe Datei als Markdown. Beschreibungen stammen aus dem jeweiligen `description`-Feld.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`ampel-system`](skills/ampel-system/SKILL.md) | Wenn es um Ampelsystem für Status in Plugin: status-navigator-step-plan geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sc... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/ampel-system/SKILL.md" download><code>SKILL.md</code></a> |
| [`copy-paste-fehler-erkennung`](skills/copy-paste-fehler-erkennung/SKILL.md) | Wenn es um Copy-Paste-Fehler erkennen in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/copy-paste-fehler-erkennung/SKILL.md" download><code>SKILL.md</code></a> |
| [`diskrepanzen-aufdecken`](skills/diskrepanzen-aufdecken/SKILL.md) | Wenn es um Diskrepanzen aufdecken in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/diskrepanzen-aufdecken/SKILL.md" download><code>SKILL.md</code></a> |
| [`dokumenten-inventur-grob`](skills/dokumenten-inventur-grob/SKILL.md) | Wenn es um Dokumenten-Inventur grob in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/dokumenten-inventur-grob/SKILL.md" download><code>SKILL.md</code></a> |
| [`dokumententyp-beschluesse`](skills/dokumententyp-beschluesse/SKILL.md) | Wenn es um Dokumententyp Gesellschafterbeschlüsse in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/dokumententyp-beschluesse/SKILL.md" download><code>SKILL.md</code></a> |
| [`dokumententyp-cap-tables`](skills/dokumententyp-cap-tables/SKILL.md) | Wenn es um Dokumententyp Cap Tables in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/dokumententyp-cap-tables/SKILL.md" download><code>SKILL.md</code></a> |
| [`dokumententyp-erklaerungen`](skills/dokumententyp-erklaerungen/SKILL.md) | Wenn es um Dokumententyp einseitige Erklärungen in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/dokumententyp-erklaerungen/SKILL.md" download><code>SKILL.md</code></a> |
| [`dokumententyp-korrespondenz`](skills/dokumententyp-korrespondenz/SKILL.md) | Wenn es um Dokumententyp Korrespondenz in Plugin: status-navigator-step-plan geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/dokumententyp-korrespondenz/SKILL.md" download><code>SKILL.md</code></a> |
| [`dokumententyp-vertraege`](skills/dokumententyp-vertraege/SKILL.md) | Wenn es um Dokumententyp Verträge erkennen in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/dokumententyp-vertraege/SKILL.md" download><code>SKILL.md</code></a> |
| [`erweiterung-hyperlinks`](skills/erweiterung-hyperlinks/SKILL.md) | Wenn es um Erweiterung Hyperlinks zur Ablage in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/erweiterung-hyperlinks/SKILL.md" download><code>SKILL.md</code></a> |
| [`erweiterung-laufende-aktualisierung`](skills/erweiterung-laufende-aktualisierung/SKILL.md) | Wenn es um Erweiterung laufende Aktualisierung in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/erweiterung-laufende-aktualisierung/SKILL.md" download><code>SKILL.md</code></a> |
| [`erweiterung-rangfolge-reiter`](skills/erweiterung-rangfolge-reiter/SKILL.md) | Wenn es um Erweiterung Rangfolge-Reiter in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/erweiterung-rangfolge-reiter/SKILL.md" download><code>SKILL.md</code></a> |
| [`erweiterung-sicherheiten-reiter`](skills/erweiterung-sicherheiten-reiter/SKILL.md) | Wenn es um Erweiterung Sicherheiten-Reiter in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/erweiterung-sicherheiten-reiter/SKILL.md" download><code>SKILL.md</code></a> |
| [`excel-reiter-1-ueberblick`](skills/excel-reiter-1-ueberblick/SKILL.md) | Wenn es um Reiter 1 Überblick Statuslage in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/excel-reiter-1-ueberblick/SKILL.md" download><code>SKILL.md</code></a> |
| [`excel-reiter-2-vorhanden`](skills/excel-reiter-2-vorhanden/SKILL.md) | Wenn es um Reiter 2 Vorhandene Dokumente in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/excel-reiter-2-vorhanden/SKILL.md" download><code>SKILL.md</code></a> |
| [`excel-reiter-3-fehlend`](skills/excel-reiter-3-fehlend/SKILL.md) | Wenn es um Reiter 3 Fehlende Dokumente in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/excel-reiter-3-fehlend/SKILL.md" download><code>SKILL.md</code></a> |
| [`excel-reiter-4-workflow`](skills/excel-reiter-4-workflow/SKILL.md) | Wenn es um Reiter 4 Workflow Step-Plan in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/excel-reiter-4-workflow/SKILL.md" download><code>SKILL.md</code></a> |
| [`excel-reiter-beteiligte-optional`](skills/excel-reiter-beteiligte-optional/SKILL.md) | Wenn es um Optionaler Reiter Beteiligte in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/excel-reiter-beteiligte-optional/SKILL.md" download><code>SKILL.md</code></a> |
| [`excel-reiter-fristen-optional`](skills/excel-reiter-fristen-optional/SKILL.md) | Wenn es um Optionaler Reiter Fristen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/excel-reiter-fristen-optional/SKILL.md" download><code>SKILL.md</code></a> |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Status Navigator Step Plan ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/juristischer-argumentationskern/SKILL.md" download><code>SKILL.md</code></a> |
| [`luecken-notifizieren`](skills/luecken-notifizieren/SKILL.md) | Wenn es um Lücken in Tabellen notifizieren in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/luecken-notifizieren/SKILL.md" download><code>SKILL.md</code></a> |
| [`padlet-als-werkzeug`](skills/padlet-als-werkzeug/SKILL.md) | Wenn es um Padlet als Status-Navigator-Werkzeug in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/padlet-als-werkzeug/SKILL.md" download><code>SKILL.md</code></a> |
| [`padlet-spalte-1-ueberblick`](skills/padlet-spalte-1-ueberblick/SKILL.md) | Wenn es um Padlet Reiter 1 Überblick aufbauen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/padlet-spalte-1-ueberblick/SKILL.md" download><code>SKILL.md</code></a> |
| [`padlet-spalte-2-vorhanden`](skills/padlet-spalte-2-vorhanden/SKILL.md) | Wenn es um Padlet Reiter 2 Verfügbar aufbauen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/padlet-spalte-2-vorhanden/SKILL.md" download><code>SKILL.md</code></a> |
| [`padlet-spalte-3-fehlend`](skills/padlet-spalte-3-fehlend/SKILL.md) | Wenn es um Padlet Reiter 3 Fehlend aufbauen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/padlet-spalte-3-fehlend/SKILL.md" download><code>SKILL.md</code></a> |
| [`padlet-spalte-4-workflow`](skills/padlet-spalte-4-workflow/SKILL.md) | Wenn es um Padlet Reiter 4 Workflow aufbauen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/padlet-spalte-4-workflow/SKILL.md" download><code>SKILL.md</code></a> |
| [`status-navigator-einstieg`](skills/status-navigator-einstieg/SKILL.md) | Wenn es um Einstieg: Was haben wir und was muss geschehen in Plugin: status-navigator-step-plan geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/status-navigator-einstieg/SKILL.md" download><code>SKILL.md</code></a> |
| [`szenario-cap-table-bereinigung`](skills/szenario-cap-table-bereinigung/SKILL.md) | Wenn es um Szenario Cap Table Bereinigung in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/szenario-cap-table-bereinigung/SKILL.md" download><code>SKILL.md</code></a> |
| [`szenario-due-diligence`](skills/szenario-due-diligence/SKILL.md) | Wenn es um Szenario Due Diligence in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/szenario-due-diligence/SKILL.md" download><code>SKILL.md</code></a> |
| [`szenario-faelligstellung-vollstreckung`](skills/szenario-faelligstellung-vollstreckung/SKILL.md) | Wenn es um Szenario gescheiterte Finanzierung in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/szenario-faelligstellung-vollstreckung/SKILL.md" download><code>SKILL.md</code></a> |
| [`szenario-finanzierungsstruktur-bereinigen`](skills/szenario-finanzierungsstruktur-bereinigen/SKILL.md) | Wenn es um Szenario Finanzierungsstruktur bereinigen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/szenario-finanzierungsstruktur-bereinigen/SKILL.md" download><code>SKILL.md</code></a> |
| [`szenario-mandatsuebernahme`](skills/szenario-mandatsuebernahme/SKILL.md) | Wenn es um Szenario Mandatsübernahme in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/szenario-mandatsuebernahme/SKILL.md" download><code>SKILL.md</code></a> |
| [`unterschriftspruefung`](skills/unterschriftspruefung/SKILL.md) | Wenn es um Unterschriftsprüfung in Plugin: status-navigator-step-plan geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/unterschriftspruefung/SKILL.md" download><code>SKILL.md</code></a> |
| [`verexcelung-prinzip`](skills/verexcelung-prinzip/SKILL.md) | Wenn es um Verexcelung Prinzip in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/verexcelung-prinzip/SKILL.md" download><code>SKILL.md</code></a> |
| [`ziel-praezisieren`](skills/ziel-praezisieren/SKILL.md) | Wenn es um Ziel präzisieren in Plugin: status-navigator-step-plan geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/ziel-praezisieren/SKILL.md" download><code>SKILL.md</code></a> |
| [`zugang-zustellung-pruefung`](skills/zugang-zustellung-pruefung/SKILL.md) | Wenn es um Zugang und Zustellung prüfen in Plugin: status-navigator-step-plan geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/skills/zugang-zustellung-pruefung/SKILL.md" download><code>SKILL.md</code></a> |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

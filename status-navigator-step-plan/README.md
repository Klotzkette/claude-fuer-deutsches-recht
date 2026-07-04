# Plugin: status-navigator-step-plan


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`status-navigator-step-plan`) | [`status-navigator-step-plan.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/status-navigator-step-plan.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **LausitzStorage 200 GmbH i.G. (Batteriegroßspeicher Jänschwalde/Peitz)** (`status-navigator-batteriespeicher-jaenschwalde-peitz`) | [Gesamt-PDF lesen](../testakten/status-navigator-batteriespeicher-jaenschwalde-peitz/gesamt-pdf/status-navigator-batteriespeicher-jaenschwalde-peitz_gesamt.pdf) | [`testakte-status-navigator-batteriespeicher-jaenschwalde-peitz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-status-navigator-batteriespeicher-jaenschwalde-peitz.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Status-Navigator und Step-Plan-Macher. Reine Dokumentenverarbeitung mit 35 Skills. Strukturiert disparate Dokumentenlagen in eine mehrseitige Excel-Arbeitsmappe und optional ein Padlet-Shelf mit Reitern Überblick, Vorhanden, Fehlend und Workflow. Keine rechtliche Bewertung.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`status-navigator-step-plan.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/status-navigator-step-plan.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/status-navigator-step-plan-werkstatt.md" download><code>status-navigator-step-plan-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/status-navigator-step-plan/status-navigator-step-plan-schnellstart.md" download><code>status-navigator-step-plan-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | LausitzStorage 200 GmbH i.G. (Batteriegroßspeicher Jänschwalde/Peitz): [Gesamt-PDF](../testakten/status-navigator-batteriespeicher-jaenschwalde-peitz/gesamt-pdf/status-navigator-batteriespeicher-jaenschwalde-peitz_gesamt.pdf), [`testakte-status-navigator-batteriespeicher-jaenschwalde-peitz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-status-navigator-batteriespeicher-jaenschwalde-peitz.zip), [`testakte-status-navigator-batteriespeicher-jaenschwalde-peitz-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-status-navigator-batteriespeicher-jaenschwalde-peitz-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
**Status-Navigator und Step-Plan-Macher**.

## Was dieses Plugin ist — und was es ausdruecklich nicht ist

Dies ist ein Plugin reiner **Dokumentenverarbeitung**. Es enthaelt — bewusst und als einzige Ausnahme im Repo — **keine Normen- und Rechtsprechungs-Anker** in den Skills. Der Grund: der Status-Navigator strukturiert chaotische Dokumentenlagen, beantwortet die Fragen "Was haben wir?", "Was fehlt?", "Was muss geschehen?" — er bewertet jedoch nichts rechtlich. Die rechtliche Prüfung bleibt anwaltliche Aufgabe.

Alle uebrigen Plugins des Repos arbeiten mit verifizierten Norm- und Rechtsprechungs-Zitaten. Dieses Plugin tut das ausdruecklich nicht. Es liefert Reiter, Spalten, Workflow-Schritte und Status-Notes — keine Subsumtion.

## Worum es geht

Anwaeltinnen und Anwaelte aus Restrukturierung, Finanzierung, Gesellschaftsrecht und Transaktionen kennen das Problem: ein Riesenklumpatsch aus Dokumenten faellt ins Mandat. Ungeordnet, disparat, teils widersprüchlich. Zwei Fragen stellen sich immer:

1. **Was ist eigentlich los?**
2. **Was muss jetzt geschehen?**

Der Status-Navigator beantwortet beide — und macht aus einer statischen Bestandsaufnahme einen dynamischen Step-Plan.

## Die Vier-Reiter-Struktur

Das Herzstueck ist eine mehrseitige Excel-Arbeitsmappe (nicht eine Chatfenster-Tabelle), bestehend aus mindestens vier Reitern:

| Reiter | Inhalt |
| --- | --- |
| 1 Überblick / Statuslage | Gesamtsituation auf einen Blick: Dokument, Datum, Verfuegbarkeit, Unterschriftsstatus, Partei, Rechtsgrundlage, Zweck |
| 2 Vorhandene Dokumente | Detailliste aller vorhandenen Dokumente mit Status und Anmerkungen |
| 3 Fehlende Dokumente | Auflistung der noch fehlenden Dokumente und Nachweise mit Beschaffungspfad |
| 4 Workflow / Next Steps | Konkreter Step-Plan: Schritte in Reihenfolge, Rechtsgrundlage, Unterschrift, Empfänger |

Optional erweiterbar um Fristen, Beteiligte, Rangfolge, Sicherheiten und Hyperlinks zur Dokumentenablage.

## Was der Status-Navigator konkret leistet

1. **Dokumententypen erkennen und einordnen** (Verträge, Erklaerungen, Beschlüsse, Cap Tables, Korrespondenz).
2. **Unterschriften und Vollständigkeit prüfen.**
3. **Diskrepanzen und Copy-Paste-Fehler aufdecken.**
4. **Versand- und Zustellungsstatus erfassen.**
5. **Luecken und Fehler in den Tabellen direkt notifizieren.**

## Padlet als Alternativausgabe

Neben der Excel-Arbeitsmappe kann der Status-Navigator denselben Step-Plan als Padlet-Shelf ausspielen. Vier Spalten, eine je Reiter, mit Ampelfarbe pro Karte, Anhaengen und Kommentar-Threads. Sinnvoll für verteilte Teams und Mandantenfreigaben; **vor Einsatz Datenschutzpruefung** (siehe Skill `padlet-als-werkzeug`).

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

- **Rechtliche Prüfung bleibt anwaltliche Aufgabe.** Der Status-Navigator erfasst und strukturiert — er bewertet nicht abschliessend. Ob eine Kuendigung wirksam, ein Zugang erfolgt, ein Formerfordernis erfuellt ist, muss der Anwalt selbst prüfen.
- **Vollständigkeitskontrolle.** Die KI kann Dokumente oder Zusammenhaenge übersehen. Jede generierte Tabelle muss anhand der Originaldokumente überprüft werden.
- **Diskrepanz-Hinweise sind Hinweise, keine Befunde.**
- **Datenschutz und Berufsrecht.** Finanzierungs- und Gesellschaftsdokumente enthalten hochsensible Daten. Die Nutzung ist nur mit einem System zulässig, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfuellt.
- **Eigenverantwortung.** Sie tragen die Verantwortung für jede Information und jeden Schritt.

## Excel-Vorlage und Beispiel

Die Excel-Spaltenkoepfe folgen der Vorlage `step-plan-document-tracker-template.xlsx`. Ein voll ausgefuelltes Beispiel zum Mandat **LausitzStorage 200 GmbH i.G. (Batteriegrossspeicher Jaenschwalde / Peitz, Brandenburg)** liegt in der zugehoerigen Testakte `testakten/status-navigator-batteriespeicher-jaenschwalde-peitz/`:

- `25_step_plan_excel_lausitzstorage.xlsx` (4 Reiter, ampelgefaerbt)
- `26_step_plan_pdf_lausitzstorage.pdf` (4 Reiter als 4 PDF-Seiten, A3 quer)

Dieselbe Datenbasis lässt sich auch als Padlet-Shelf ausspielen (vier Spalten); siehe Padlet-Skills.

## Einordnung

**Status-Navigator und Step-Plan-Macher**: ein Dokumentenstatus- und Workflow-Generator.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `status-navigator-einstieg`, `szenario-mandatsuebernahme` |
| 2. Unterlagen, Sachverhalt und Quellen | `dokumenten-inventur-grob`, `dokumententyp-beschluesse`, `dokumententyp-cap-tables`, `dokumententyp-erklaerungen`, `dokumententyp-korrespondenz`, `dokumententyp-vertraege`, `luecken-notifizieren` |
| 3. Prüfung, Anspruch und Subsumtion | `unterschriftspruefung`, `zugang-zustellung-pruefung` |
| 4. Gestaltung, Strategie und Verhandlung | `excel-reiter-beteiligte-optional`, `excel-reiter-fristen-optional`, `szenario-finanzierungsstruktur-bereinigen` |
| 5. Verfahren, Behörde und Gericht | `szenario-faelligstellung-vollstreckung` |
| 7. Kontrolle, Qualität und Gegenprüfung | `copy-paste-fehler-erkennung` |
| 8. Spezialmodule und Schnittstellen | `ampel-system`, `diskrepanzen-aufdecken`, `erweiterung-hyperlinks`, `erweiterung-laufende-aktualisierung`, `erweiterung-rangfolge-reiter`, `erweiterung-sicherheiten-reiter`, `excel-reiter-1-ueberblick`, `excel-reiter-2-vorhanden`, `excel-reiter-3-fehlend`, `excel-reiter-4-workflow`, `padlet-als-werkzeug`, `padlet-spalte-1-ueberblick`, `padlet-spalte-2-vorhanden`, `padlet-spalte-3-fehlend`, `padlet-spalte-4-workflow`, `szenario-cap-table-bereinigung`, `szenario-due-diligence`, `verexcelung-prinzip`, ... plus 1 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 35 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ampel-system` | Wenn es um Ampelsystem für Status in Plugin: status-navigator-step-plan geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sc... |
| `copy-paste-fehler-erkennung` | Wenn es um Copy-Paste-Fehler erkennen in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `diskrepanzen-aufdecken` | Wenn es um Diskrepanzen aufdecken in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `dokumenten-inventur-grob` | Wenn es um Dokumenten-Inventur grob in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `dokumententyp-beschluesse` | Wenn es um Dokumententyp Gesellschafterbeschluesse in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schr... |
| `dokumententyp-cap-tables` | Wenn es um Dokumententyp Cap Tables in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `dokumententyp-erklaerungen` | Wenn es um Dokumententyp einseitige Erklaerungen in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `dokumententyp-korrespondenz` | Wenn es um Dokumententyp Korrespondenz in Plugin: status-navigator-step-plan geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `dokumententyp-vertraege` | Wenn es um Dokumententyp Verträge erkennen in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `erweiterung-hyperlinks` | Wenn es um Erweiterung Hyperlinks zur Ablage in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `erweiterung-laufende-aktualisierung` | Wenn es um Erweiterung laufende Aktualisierung in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erweiterung-rangfolge-reiter` | Wenn es um Erweiterung Rangfolge-Reiter in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erweiterung-sicherheiten-reiter` | Wenn es um Erweiterung Sicherheiten-Reiter in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `excel-reiter-1-ueberblick` | Wenn es um Reiter 1 Überblick Statuslage in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `excel-reiter-2-vorhanden` | Wenn es um Reiter 2 Vorhandene Dokumente in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `excel-reiter-3-fehlend` | Wenn es um Reiter 3 Fehlende Dokumente in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `excel-reiter-4-workflow` | Wenn es um Reiter 4 Workflow Step-Plan in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `excel-reiter-beteiligte-optional` | Wenn es um Optionaler Reiter Beteiligte in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `excel-reiter-fristen-optional` | Wenn es um Optionaler Reiter Fristen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `luecken-notifizieren` | Wenn es um Luecken in Tabellen notifizieren in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `padlet-als-werkzeug` | Wenn es um Padlet als Status-Navigator-Werkzeug in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `padlet-spalte-1-ueberblick` | Wenn es um Padlet Reiter 1 Überblick aufbauen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `padlet-spalte-2-vorhanden` | Wenn es um Padlet Reiter 2 Verfuegbar aufbauen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `padlet-spalte-3-fehlend` | Wenn es um Padlet Reiter 3 Fehlend aufbauen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `padlet-spalte-4-workflow` | Wenn es um Padlet Reiter 4 Workflow aufbauen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `status-navigator-einstieg` | Wenn es um Einstieg: Was haben wir und was muss geschehen in Plugin: status-navigator-step-plan geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `szenario-cap-table-bereinigung` | Wenn es um Szenario Cap Table Bereinigung in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `szenario-due-diligence` | Wenn es um Szenario Due Diligence in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `szenario-faelligstellung-vollstreckung` | Wenn es um Szenario gescheiterte Finanzierung in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `szenario-finanzierungsstruktur-bereinigen` | Wenn es um Szenario Finanzierungsstruktur bereinigen in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `szenario-mandatsuebernahme` | Wenn es um Szenario Mandatsuebernahme in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `unterschriftspruefung` | Wenn es um Unterschriftspruefung in Plugin: status-navigator-step-plan geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verexcelung-prinzip` | Wenn es um Verexcelung Prinzip in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ziel-praezisieren` | Wenn es um Ziel praezisieren in Plugin: status-navigator-step-plan geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `zugang-zustellung-pruefung` | Wenn es um Zugang und Zustellung prüfen in Plugin: status-navigator-step-plan geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

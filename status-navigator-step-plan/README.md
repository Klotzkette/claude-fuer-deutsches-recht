# Plugin: status-navigator-step-plan

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`status-navigator-step-plan`) | [`status-navigator-step-plan.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/status-navigator-step-plan.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **LausitzStorage 200 GmbH i.G. (Batteriegroßspeicher Jänschwalde/Peitz)** (`status-navigator-batteriespeicher-jaenschwalde-peitz`) | [Gesamt-PDF lesen](../testakten/status-navigator-batteriespeicher-jaenschwalde-peitz/gesamt-pdf/status-navigator-batteriespeicher-jaenschwalde-peitz_gesamt.pdf) | [`testakte-status-navigator-batteriespeicher-jaenschwalde-peitz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-status-navigator-batteriespeicher-jaenschwalde-peitz.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

**Status-Navigator und Step-Plan-Macher**.

## Was dieses Plugin ist — und was es ausdruecklich nicht ist

Dies ist ein Plugin reiner **Dokumentenverarbeitung**. Es enthaelt — bewusst und als einzige Ausnahme im Repo — **keine Normen- und Rechtsprechungs-Anker** in den Skills. Der Grund: der Status-Navigator strukturiert chaotische Dokumentenlagen, beantwortet die Fragen "Was haben wir?", "Was fehlt?", "Was muss geschehen?" — er bewertet jedoch nichts rechtlich. Die rechtliche Pruefung bleibt anwaltliche Aufgabe.

Alle uebrigen Plugins des Repos arbeiten mit verifizierten Norm- und Rechtsprechungs-Zitaten. Dieses Plugin tut das ausdruecklich nicht. Es liefert Reiter, Spalten, Workflow-Schritte und Status-Notes — keine Subsumtion.

## Worum es geht

Anwaeltinnen und Anwaelte aus Restrukturierung, Finanzierung, Gesellschaftsrecht und Transaktionen kennen das Problem: ein Riesenklumpatsch aus Dokumenten faellt ins Mandat. Ungeordnet, disparat, teils widerspruechlich. Zwei Fragen stellen sich immer:

1. **Was ist eigentlich los?**
2. **Was muss jetzt geschehen?**

Der Status-Navigator beantwortet beide — und macht aus einer statischen Bestandsaufnahme einen dynamischen Step-Plan.

## Die Vier-Reiter-Struktur

Das Herzstueck ist eine mehrseitige Excel-Arbeitsmappe (nicht eine Chatfenster-Tabelle), bestehend aus mindestens vier Reitern:

| Reiter | Inhalt |
| --- | --- |
| 1 Ueberblick / Statuslage | Gesamtsituation auf einen Blick: Dokument, Datum, Verfuegbarkeit, Unterschriftsstatus, Partei, Rechtsgrundlage, Zweck |
| 2 Vorhandene Dokumente | Detailliste aller vorhandenen Dokumente mit Status und Anmerkungen |
| 3 Fehlende Dokumente | Auflistung der noch fehlenden Dokumente und Nachweise mit Beschaffungspfad |
| 4 Workflow / Next Steps | Konkreter Step-Plan: Schritte in Reihenfolge, Rechtsgrundlage, Unterschrift, Empfaenger |

Optional erweiterbar um Fristen, Beteiligte, Rangfolge, Sicherheiten und Hyperlinks zur Dokumentenablage.

## Was der Status-Navigator konkret leistet

1. **Dokumententypen erkennen und einordnen** (Vertraege, Erklaerungen, Beschluesse, Cap Tables, Korrespondenz).
2. **Unterschriften und Vollstaendigkeit pruefen.**
3. **Diskrepanzen und Copy-Paste-Fehler aufdecken.**
4. **Versand- und Zustellungsstatus erfassen.**
5. **Luecken und Fehler in den Tabellen direkt notifizieren.**

## Padlet als Alternativausgabe

Neben der Excel-Arbeitsmappe kann der Status-Navigator denselben Step-Plan als Padlet-Shelf ausspielen. Vier Spalten, eine je Reiter, mit Ampelfarbe pro Karte, Anhaengen und Kommentar-Threads. Sinnvoll fuer verteilte Teams und Mandantenfreigaben; **vor Einsatz Datenschutzpruefung** (siehe Skill `padlet-als-werkzeug`).

## Die 35 Skills im Ueberblick

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

### Pruefungen
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

- **Rechtliche Pruefung bleibt anwaltliche Aufgabe.** Der Status-Navigator erfasst und strukturiert — er bewertet nicht abschliessend. Ob eine Kuendigung wirksam, ein Zugang erfolgt, ein Formerfordernis erfuellt ist, muss der Anwalt selbst pruefen.
- **Vollstaendigkeitskontrolle.** Die KI kann Dokumente oder Zusammenhaenge uebersehen. Jede generierte Tabelle muss anhand der Originaldokumente ueberprueft werden.
- **Diskrepanz-Hinweise sind Hinweise, keine Befunde.**
- **Datenschutz und Berufsrecht.** Finanzierungs- und Gesellschaftsdokumente enthalten hochsensible Daten. Die Nutzung ist nur mit einem System zulaessig, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfuellt.
- **Eigenverantwortung.** Sie tragen die Verantwortung fuer jede Information und jeden Schritt.

## Excel-Vorlage und Beispiel

Die Excel-Spaltenkoepfe folgen der Vorlage `step-plan-document-tracker-template.xlsx`. Ein voll ausgefuelltes Beispiel zum Mandat **LausitzStorage 200 GmbH i.G. (Batteriegrossspeicher Jaenschwalde / Peitz, Brandenburg)** liegt in der zugehoerigen Testakte `testakten/status-navigator-batteriespeicher-jaenschwalde-peitz/`:

- `25_step_plan_excel_lausitzstorage.xlsx` (4 Reiter, ampelgefaerbt)
- `26_step_plan_pdf_lausitzstorage.pdf` (4 Reiter als 4 PDF-Seiten, A3 quer)

Dieselbe Datenbasis laesst sich auch als Padlet-Shelf ausspielen (vier Spalten); siehe Padlet-Skills.

## Einordnung

**Status-Navigator und Step-Plan-Macher**: ein Dokumentenstatus- und Workflow-Generator.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 35 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ampel-system` | Setzt ein dreistufiges Ampelsystem in der Excel-Arbeitsmappe um: gruen fuer vollstaendig, gelb fuer pruefungsbeduerftig, rot fuer fehlt oder fehlerhaft. Wird per bedingter Formatierung auf allen Reitern angewandt. |
| `copy-paste-fehler-erkennung` | Erkennt typische Copy-Paste-Situationen: alte Parteinamen, abweichende Vertragsbezeichnungen, falsche Daten in Standardabsaetzen und uebernommene Klauseln aus Vorlaeuferdokumenten. Liefert eine kommentierte Auffaelligkeitsliste. |
| `diskrepanzen-aufdecken` | Vergleicht Dokumente untereinander und deckt Diskrepanzen auf: abweichende Betraege, Daten, Parteibezeichnungen, Konditionen und Bezugsklauseln. Markiert moegliche Copy-Paste-Fehler aus einer schlampig gefuehrten Dokumentation. |
| `dokumenten-inventur-grob` | Erzeugt eine erste grobe Liste aller vorhandenen Dateien mit Dateiname, Dateityp, Dateigroesse und sichtbarem Datum. Noch keine inhaltliche Pruefung — reine Bestandsaufnahme als Ausgangspunkt fuer die feinere Einordnung. |
| `dokumententyp-beschluesse` | Erkennt Beschluesse: Gesellschafterbeschluesse, Aufsichtsratsbeschluesse, Hauptversammlungsbeschluesse, Vorstandsbeschluesse. Erfasst Beschlussdatum, beschliessende Organe, Beschlussgegenstand und Formerfordernis. |
| `dokumententyp-cap-tables` | Erkennt Cap Tables in beliebigem Format (Excel, PDF, eingebettete Tabellen). Erfasst Stichdatum, Gesellschafter und Anteile. Vorbereitung fuer den Konsistenz-Vergleich mehrerer Cap Tables und Abgleich mit den zugrundeliegenden Vertraegen. |
| `dokumententyp-erklaerungen` | Erkennt einseitige Willenserklaerungen: Kuendigungen, Faelligstellungen, Anfechtungen, Ruecktritte, Widerrufe, Wandlungserklaerungen. Markiert besonders zugangsbeduerftige Erklaerungen fuer den spaeteren Zustellungs-Check. |
| `dokumententyp-korrespondenz` | Erkennt Korrespondenz: E-Mails, Briefe, Aktenvermerke, Faxprotokolle, Telefonnotizen. Erfasst Absender, Empfaenger, Datum, Betreff und Bezug zu Vertraegen und Erklaerungen. |
| `dokumententyp-vertraege` | Erkennt Vertraege als Dokumentenklasse: Darlehensvertraege, Wandeldarlehen, Gesellschaftervereinbarungen, Pflichtenheft, Kaufvertraege, Sicherungsvertraege. Ordnet sie nach Vertragspartei, Datum, Vertragstyp und Bezug zu uebrigen Dokumen... |
| `erweiterung-hyperlinks` | Verknuepft die Tabelleneintraege mit den Originaldokumenten in der Dokumentenablage. Hyperlinks von der Tabelle zum jeweiligen Original ermoeglichen schnellen Sprung in den Volltext. |
| `erweiterung-laufende-aktualisierung` | Konzept fuer die laufende Aktualisierung der Status-Navigator-Arbeitsmappe waehrend des Mandats. Standard-Update-Rhythmus, Versionierung, Aenderungslog und Wiederverwendung als Steuerungsinstrument. |
| `erweiterung-rangfolge-reiter` | Optionaler Reiter Rangfolge bei mehreren Finanzierungsinstrumenten. Stellt die Rang- und Befriedigungsreihenfolge dar: Senior Secured, Senior Unsecured, Mezzanine, Gesellschafterdarlehen, sonstige Einlagen. Beruht ausschliesslich auf Man... |
| `erweiterung-sicherheiten-reiter` | Optionaler Reiter Sicherheiten. Uebersicht aller Sicherheiten mit Status der Bestellung und Verwertbarkeit. Nimmt keine rechtliche Bewertung der Sicherheitenwirksamkeit vor — die bleibt der anwaltlichen Pruefung vorbehalten. |
| `excel-reiter-1-ueberblick` | Baut Reiter 1 der Step-Plan-Excel: Ueberblick aller fuer die Durchsetzung erforderlichen Dokumente. Spalten Dokument, Datum, Verfuegbarkeit, Unterschriftsstatus, Unterzeichnet von (Partei und Funktion), Rechtsgrundlage (Klausel im zugrun... |
| `excel-reiter-2-vorhanden` | Baut Reiter 2 der Step-Plan-Excel: vorhandene Dokumente mit Augenmerk auf Unterschriftsstatus und Vertretungsbefugnis. Spalten Dokument, Datum, Typ, Unterzeichnet von, Unterschriftsstatus und Anmerkung. Lieferquelle fuer Unterschriftspru... |
| `excel-reiter-3-fehlend` | Baut Reiter 3 der Step-Plan-Excel: fehlende Dokumente mit Beschaffungsweg. Spalten erforderliches Dokument, angefordert von, zu beschaffen von, Grund der Erforderlichkeit und Status. Sortierung nach Frist. Vorbereitung fuer den Workflow-... |
| `excel-reiter-4-workflow` | Baut Reiter 4 der Step-Plan-Excel: Workflow je Dokument in Reihenfolge der Beschaffung. Spalten erforderliches Dokument, Schritte in Reihenfolge, Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag), Unterzeichnet von und Versendet an... |
| `excel-reiter-beteiligte-optional` | Fuegt optional einen Reiter Beteiligte hinzu: Uebersicht aller Parteien mit Rolle, Funktion, Anteilen und Kontaktdaten. Vorbereitung fuer die spaetere Zustellung und Kommunikation. |
| `excel-reiter-fristen-optional` | Fuegt optional einen Reiter Fristen hinzu: Kuendigungsfristen, Wandlungsfristen, Verjaehrungsfristen, Ablaufdaten und Hemmungstatbestaende. Beruht ausschliesslich auf Mandatsangaben und Vertragstext — keine eigene rechtliche Bewertung. |
| `luecken-notifizieren` | Notifiziert direkt in den Tabellen, wo Fehler, Luecken oder Unklarheiten bestehen. Standard-Notes umfassen Gesellschafterbeschluss fehlt, Zustellung unklar, Betrag weicht ab, Unterschrift Geschaeftsfuehrer fehlt. |
| `padlet-als-werkzeug` | Erlaeutert, wann Padlet als visuelle Alternative zur Step-Plan-Excel sinnvoll ist und wann nicht. Beschreibt das Format Shelf mit vier Spalten als Mapping der vier Excel-Reiter, Datenschutz-Anforderungen, berufsrechtliche Grenzen sowie d... |
| `padlet-spalte-1-ueberblick` | Baut die erste Padlet-Spalte als Pendant zu Reiter 1 der Step-Plan-Excel. Ueberblick aller erforderlichen Dokumente mit Ampelfaerbung, Sortierung nach Vertragsebene und sieben Kartenfeldern (Dokument, Datum, Verfuegbarkeit, Unterschrifts... |
| `padlet-spalte-2-vorhanden` | Baut die zweite Padlet-Spalte als Pendant zu Reiter 2 der Step-Plan-Excel. Vorliegende Dokumente mit Type-Tag (Vertrag, Bescheid, Erklaerung, Beschluss, Schreiben) und Statusbadge fuer den Unterschriftsstatus. |
| `padlet-spalte-3-fehlend` | Baut die dritte Padlet-Spalte als Pendant zu Reiter 3 der Step-Plan-Excel. Fehlende Dokumente mit Frist im Untertitel, Beschaffungsweg in zwei Absaetzen und Restzeit-Ampel (gruen mehr als 30 Tage, gelb 8 bis 30, rot bis 7). |
| `padlet-spalte-4-workflow` | Baut die vierte Padlet-Spalte als Pendant zu Reiter 4 der Step-Plan-Excel. Workflow-Karten mit nummerierten Checkbox-Schritten, Rechtsgrundlage, Tags fuer Unterzeichner und Empfaenger sowie Fortschritts-Sortierung. |
| `status-navigator-einstieg` | Einstiegs-Skill fuer den Status-Navigator: nimmt einen ungeordneten Dokumentenklumpatsch entgegen und liefert die ersten Antworten auf die zwei Kernfragen — was ist eigentlich los und was muss als Naechstes geschehen. Setzt den Rahmen fu... |
| `szenario-cap-table-bereinigung` | Anwendungsszenario Bereinigung mehrerer widerspruechlicher Cap Tables. Status-Navigator vergleicht die Cap Tables miteinander und mit den zugrundeliegenden Vertraegen. Zeigt Abweichungen und Wandlungsbedarf auf. |
| `szenario-due-diligence` | Anwendungsszenario Due Diligence. Status-Navigator strukturiert eine grosse disparate Dokumentensammlung im Rahmen einer Transaktion. Prueft auf Vollstaendigkeit und Diskrepanzen. Vorbereitung der Datenraum-Indexierung fuer das Targetunt... |
| `szenario-faelligstellung-vollstreckung` | Anwendungsszenario gescheiterte Finanzierung mit Vorbereitung von Faelligstellung und Vollstreckung. Status-Navigator erfasst Darlehensvertraege, Kuendigungs- und Faelligstellungsschreiben, Zustellungsnachweise und Sicherheiten. Workflow... |
| `szenario-finanzierungsstruktur-bereinigen` | Anwendungsszenario komplexe Finanzierungsstruktur bereinigen. Status-Navigator erfasst Wandeldarlehen, Bankfinanzierung, Gesellschafterdarlehen, sonstige Einlagen und Stundungen. Stellt Konditionen und Rangfolge zusammen und vergleicht C... |
| `szenario-mandatsuebernahme` | Anwendungsszenario Uebernahme eines Mandats mit ungeordneter Dokumentenlage. Status-Navigator erzeugt schnell Klarheit ueber Status und naechste Schritte. Markiert Sofortpflichten und uebersehene Fristen. |
| `unterschriftspruefung` | Prueft, soweit aus den Dokumenten ersichtlich, ob die jeweils erforderlichen Parteien unterschrieben haben. Markiert fehlende Unterschriften, unklare Unterzeichner und Vertretungsfragen. Trifft keine Rechtswirksamkeitsbewertung. |
| `verexcelung-prinzip` | Erklaert das Prinzip der Verexcelung: nicht nur eine Tabelle im Chatfenster, sondern eine echte Excel-Arbeitsmappe mit mehreren Reitern. Begruendet, warum die Verexcelung das Arbeitsergebnis sofort weiterverwendbar macht. |
| `ziel-praezisieren` | Klaert mit dem Auftraggeber das konkrete Ziel des Status-Navigators: Faelligstellung und Vollstreckung, Vollzug einer Kapitalmassnahme, Bereinigung der Finanzierungsstruktur, Due-Diligence-Vorbereitung oder Mandatsuebernahme. Das Ziel be... |
| `zugang-zustellung-pruefung` | Erfasst den Versendungs- und Zustellungsstatus aller zugangsbeduerftigen Willenserklaerungen: Kuendigungen, Faelligstellungen, Anfechtungen, Mahnungen. Markiert, wo der Zugang unklar ist oder noch nachzuweisen waere. Trifft keine rechtli... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

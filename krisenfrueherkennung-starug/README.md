# Krisenfrüherkennung und StaRUG-Management



<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`krisenfrueherkennung-starug`) | [`krisenfrueherkennung-starug.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krisenfrueherkennung-starug.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte: Krisenfrüherkennung & StaRUG – Vier Varianten** (`krisenfrueherkennung-starug-vier-varianten`) | [Gesamt-PDF lesen](../testakten/krisenfrueherkennung-starug-vier-varianten/gesamt-pdf/krisenfrueherkennung-starug-vier-varianten_gesamt.pdf) | [`testakte-krisenfrueherkennung-starug-vier-varianten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-krisenfrueherkennung-starug-vier-varianten.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Krisenfrüherkennung & StaRUG – Vier Varianten** (`krisenfrueherkennung-starug-vier-varianten`) | [Gesamt-PDF lesen](../testakten/krisenfrueherkennung-starug-vier-varianten/gesamt-pdf/krisenfrueherkennung-starug-vier-varianten_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-krisenfrueherkennung-starug-vier-varianten.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

**Plugin-Slug:** `krisenfrueherkennung-starug`  
**Version:** 3.2.1  
**Autor:** Klotzkette

---

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Krisenfrüherkennung und StaRUG-Management (`krisenfrueherkennung-starug`) | [krisenfrueherkennung-starug.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krisenfrueherkennung-starug.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Krisenfrüherkennung & StaRUG – Vier Varianten** ([`testakten/krisenfrueherkennung-starug-vier-varianten/`](../testakten/krisenfrueherkennung-starug-vier-varianten/)).

Direkt-Download als ZIP: [testakte-krisenfrueherkennung-starug-vier-varianten.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-krisenfrueherkennung-starug-vier-varianten.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `krisenfrueherkennung-starug.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe unser Frühwarnsystem nach § 1 StaRUG und bewerte die GF-Haftung.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Kernbotschaft

> Krisenfrüherkennung ist keine betriebswirtschaftliche Kür, sondern gesetzliche Pflicht mit direkter persönlicher Haftungskonsequenz. § 1 StaRUG verlangt einen 24-Monats-Planungshorizont. Wer die Datenlage nicht im Griff hat, verliert in der Krise das Heft des Handelns und den Zugriff auf moderne Sanierungswerkzeuge.

---

## Überblick

Dieses Plugin bietet kanzleitaugliche Werkzeuge für Geschäftsführer, Restrukturierungsberater, Steuerberater, Wirtschaftsprüfer und Rechtsanwälte im Bereich der gesetzlichen Krisenfrüherkennung nach § 1 StaRUG. Der Fokus liegt auf dem 24-Monats-Planungshorizont, der persönlichen Haftung der Geschäftsführung und der praktischen Anwendung der StaRUG-Sanierungswerkzeuge.

## Zielgruppe

- Geschäftsführer und Vorstände mittelständischer Unternehmen
- Restrukturierungsberater und Insolvenzverwalter
- Steuerberater und Wirtschaftsprüfer mit Mandantenwarnpflicht nach § 102 StaRUG
- Rechtsanwälte im Sanierungs- und Insolvenzrecht
- Compliance-Beauftragte

---

## Skills-Übersicht

### Block A — Rechtliche Grundlagen & Pflichten

| Skill | Thema |
|---|---|
| `paragraph-1-starug-pflichten-und-24-monats-horizont` | § 1 StaRUG Volltext-Auslegung, 24-Monats-Planungshorizont, Abgrenzung § 18 InsO |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` | Persönliche Haftung, Business Judgment Rule in der Krise, Beweislastumkehr |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

### Block B — 24-Monats-Frühwarnsystem aufbauen

| Skill | Thema |
|---|---|
| `fruehwarnsystem-architektur-zwei-jahres-horizont` | IDW S 6 + IDW PS 340 n.F., Risiko-Inventar, KPI-Kaskade, Eskalationsstufen |
| `rollierende-liquiditaetsplanung-24-monate-template` | Zweijahres-Liquiplan, wöchentliche + monatliche Granularität, Stresstests |
| `integrierte-planung-guv-bilanz-cashflow` | Drei-Statement-Modell, Working-Capital-Modellierung, Investitions-/Finanzierungsplan |
| `kennzahlenset-und-ampelsystem-starug-konform` | Frühwarn-KPIs, Ampelsystem rot/gelb/grün mit numerischen Schwellen |

### Block C — Krisenstadien-Diagnostik

| Skill | Thema |
|---|---|
| `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` | IDW S 6 Stadienlehre, Diagnose-Checklisten je Stadium |
| `drohende-zahlungsunfaehigkeit-paragraph-18-inso` | Prognosezeitraum, Wahrscheinlichkeitsmaßstab, Abgrenzung §§ 17/19 InsO |
| `fortbestehensprognose-zweistufig` | Positive Fortführungsprognose IDW S 11, Dokumentationspflicht |
| `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` | § 15a InsO Triggerlogik, Maximalfrist, strafrechtliche Sanktion |

### Block D — StaRUG-Werkzeuge nutzen

| Skill | Thema |
|---|---|
| `restrukturierungsplan-architektur-paragraph-7ff-starug` | Planbestandteile, Gruppenbildung § 9, Mehrheit § 25, gerichtliche Bestätigung |
| `stabilisierungsanordnung-und-vollstreckungssperre` | §§ 49-59 StaRUG, Voraussetzungen, Antragsmuster |
| `cross-class-cram-down-und-absolute-priority` | § 26 StaRUG, gerichtliche Plan-Bestätigung, Schlechterstellungsverbot |
| `restrukturierungsbeauftragter-und-sachwalter` | § 73 StaRUG, Auswahl, Aufgaben, Honorar-Festsetzung |

### Block E — Kanzlei- und Geschäftsführer-Werkzeuge

| Skill | Thema |
|---|---|
| `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` | Krisenprotokoll, Sitzungs-Templates, Beweissicherung |
| `mandantenbrief-warnung-paragraph-102-starug-template` | Volltext-Templates § 102-StaRUG-Warnung, Eskalationsstufen |
| `restructuring-lounge-impulsvortrag-toolkit` | Foliensätze, Talking-Points, Q&A-Fallnetz für Vortragsformate |

---

## Rechtlicher Hinweis

Alle in diesem Plugin verwendeten Personen, Kanzleinamen und Mandantennamen sind fiktiv. Das Plugin dient der allgemeinen rechtlichen Information und ersetzt keine individuelle Rechtsberatung im Einzelfall.

---

## Rechtsgrundlagen (Kernreferenzen)

- §§ 1, 7-9, 25, 26, 29-31, 49-59, 73, 102 StaRUG
- §§ 15a, 17, 18, 19 InsO
- § 43 GmbHG
- § 93 AktG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- IDW S 6 (Sanierungskonzepte)
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen)
- IDW PS 340 n.F. (Risikofrüherkennungssysteme)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 20 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Krisenfrueherkennung Starug-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arb... |
| `cross-class-cram-down-und-absolute-priority` | Cross-Class-Cram-Down und Absolute-Priority-Rule im StaRUG-Plan: Gericht soll Plan gegen ablehnende Gläubiger-Gruppen bestätigen. Normen: § 26 StaRUG (Cram-Down-Voraussetzungen), § 30 StaRUG (Schlechterstellungsverbot), § 31 StaRUG (Obst... |
| `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` | Krisenprotokollierung der Geschäftsführung für Haftungsschutz: GmbH-Geschäftsführer oder AG-Vorstand will Entscheidungen in der Krise dokumentieren. Normen: § 43 GmbHG (Sorgfaltspflicht und Haftung), § 93 Abs. 2 S. 2 AktG (Beweislastumke... |
| `drohende-zahlungsunfaehigkeit-paragraph-18-inso` | Drohende Zahlungsunfähigkeit nach § 18 InsO feststellen: Berater oder GF prüft ob StaRUG-Zugangsberechtigung besteht. Normen: § 18 InsO (drohende ZU), § 17 InsO (aktuelle ZU), § 19 InsO (Überschuldung), § 1 StaRUG (Zugangsberechtigung).... |
| `fortbestehensprognose-zweistufig` | Zweistufige Fortbestehensprognose nach IDW S 11 erstellen: Unternehmen ist möglicherweise ueberschuldet und braucht positive Fortführungsprognose. Normen: § 19 InsO (Überschuldungsbegriff modifiziert), IDW S 11 (Fortbestehensprognose-Sta... |
| `fruehwarnsystem-architektur-zwei-jahres-horizont` | StaRUG-konformes Fruehwarnsystem mit 24-Monats-Horizont architektieren: Unternehmen will § 1 StaRUG Krisenfrueherkennung implementieren. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW S 6 (Sanierungsstandard), IDW PS 340 n.F. (Risikoma... |
| `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` | Geschäftsführerhaftung bei Krisenversagen prüfe und begrenzen: GF oder Berater will Haftungsrisiken einschaetzen und Enthaftungsstrategien entwickeln. Normen: § 43 GmbHG (Sorgfaltspflicht), § 93 AktG (Vorstandshaftung), § 93 Abs. 2 S. 2... |
| `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` | Insolvenzantragspflicht nach § 15a InsO und Drei-Wochen-Frist: GF prüft ob Insolvenzantrag gestellt werden muss. Normen: § 15a InsO (Antragspflicht), § 15a Abs. 4 InsO (Strafbarkeit), § 18 InsO (drohende ZU als StaRUG-Tor), § 1 StaRUG (F... |
| `integrierte-planung-guv-bilanz-cashflow` | Integriertes Drei-Statement-Modell (GuV/Bilanz/Cashflow) für StaRUG-Planung erstellen: Sanierungsberater braucht konsistentes Planungsmodell. Normen: IDW S 6 (Sanierungsstandard), IDW S 11 (Fortbestehensprognose), HGB §§ 242 ff. (Jahresa... |
| `kennzahlenset-und-ampelsystem-starug-konform` | StaRUG-konformes KPI-Set und Ampelsystem für Krisenfrueherkennung definieren: Berater oder GF braucht messbare Schwellenwerte für Krisen-Monitoring. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW PS 340 n.F. Prüfraster: Liquiditaetsrei... |
| `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` | IDW-S-6-Krisenstadien diagnostizieren und Handlungskorridore bestimmen: Berater oder GF will Krisenstadium und passende Massnahmen ermitteln. Normen: IDW S 6 (Sanierungsstandard: Stakeholder-, Strategie-, Produkt-, Ertrags-, Liquiditaets... |
| `mandantenbrief-warnung-paragraph-102-starug-template` | Workflow-Skill zu mandantenbrief warnung paragraph 102 starug template. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `paragraph-1-starug-pflichten-und-24-monats-horizont` | § 1 StaRUG Krisenfrueherkenungspflicht und 24-Monats-Horizont erklären und umsetzen: GF oder Berater fragt was StaRUG konkret verlangt. Normen: § 1 StaRUG (Frueherkennungspflicht GmbH/AG), § 18 InsO (drohende ZU als StaRUG-Zugang). Prüfr... |
| `paragraph-102-starug-warnpflicht-bei-rechtsberatern` | Workflow-Skill zu paragraph 102 starug warnpflicht bei rechtsberatern. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `pflichtenkollision-und-shift-of-fiduciary-duties` | Workflow-Skill zu pflichtenkollision und shift of fiduciary duties. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `restructuring-lounge-impulsvortrag-toolkit` | Toolkit für Impulsvorträge zu Krisenfrüherkennung und StaRUG: Foliensatz-Gliederung, Talking-Points, juristische Kernbotschaften, Q-und-A-Fallnetz, Formathinweise für Veranstaltungen wie Branchenlounge-Formate. |
| `restrukturierungsbeauftragter-und-sachwalter` | Restrukturierungsbeauftragter und Sachwalter nach § 73 StaRUG: GF oder Gläubigervertreter prüft Bestellung und Aufgaben. Normen: § 73 StaRUG (Restrukturierungsbeauftragter), §§ 74-77 StaRUG (Pflichtbeauftragung), § 76 StaRUG (Sachwalter)... |
| `restrukturierungsplan-architektur-paragraph-7ff-starug` | StaRUG-Restrukturierungsplan nach §§ 7 ff. StaRUG architektieren: Schuldner oder Berater plant außergerichtliche Sanierung unter StaRUG. Normen: §§ 7 ff. StaRUG (Planbestandteile), § 9 StaRUG (Gruppenbildung), § 25 StaRUG (Mehrheitserfor... |
| `rollierende-liquiditaetsplanung-24-monate-template` | Rollierende 24-Monats-Liquiditaetsplanung nach StaRUG erstellen: Sanierungsberater oder GF braucht Liquiditaets-Forecast. Normen: § 1 StaRUG (24-Monats-Horizont), IDW S 11 (Fortbestehensprognose), IDW S 6 (Sanierungskonzept). Prüfraster:... |
| `stabilisierungsanordnung-und-vollstreckungssperre` | Stabilisierungsanordnung und Vollstreckungssperre nach §§ 49-59 StaRUG beantragen: Schuldner braucht Schutz vor Einzelvollstreckung waehrend Restrukturierung. Normen: §§ 49-59 StaRUG (Stabilisierungsanordnung), § 51 StaRUG (Dauer max. 3... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

# Krisenfrüherkennung und StaRUG-Management

**Plugin-Slug:** `krisenfrueherkennung-starug`  
**Version:** 3.2.1  
**Autor:** Klotzkette

---

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Krisenfrüherkennung und StaRUG-Management (`krisenfrueherkennung-starug`) | [krisenfrueherkennung-starug.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krisenfrueherkennung-starug.zip) |

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `krisenfrueherkennung-starug.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe unser Frühwarnsystem nach § 1 StaRUG und bewerte die GF-Haftung.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Testakte

Vier verschiedene fiktive Krisenvarianten in einer Akte: KI-Startup, Maschinenbau-AG, Batteriezellen-SE, Catering-UG.

- Vier-Varianten-Akte (VEYRA KI / HARTMANNSCHMIDT / NORDFELS / SALALTBAR): [testakten/krisenfrueherkennung-starug-vier-varianten/](../testakten/krisenfrueherkennung-starug-vier-varianten/) -> [testakte-krisenfrueherkennung-starug-vier-varianten.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-krisenfrueherkennung-starug-vier-varianten.zip)

---

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

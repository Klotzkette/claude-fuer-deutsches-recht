# Krisenfrüherkennung und StaRUG-Management

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Krisenfrüherkennung nach Paragraf 1 StaRUG, Warnpflicht bei Jahresabschlusserstellung nach Paragraf 102 StaRUG, 24-Monats-Prognose nach Paragraf 18 InsO, Haftung, integrierte Planung, Restrukturierungsplan und Stabilisierungsanordnung.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/krisenfrueherkennung-starug.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`krisenfrueherkennung-starug.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krisenfrueherkennung-starug.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/krisenfrueherkennung-starug/krisenfrueherkennung-starug-werkstatt.md" download><code>krisenfrueherkennung-starug-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/krisenfrueherkennung-starug/krisenfrueherkennung-starug-schnellstart.md" download><code>krisenfrueherkennung-starug-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Krisenfrüherkennung & StaRUG – Vier Varianten](../testakten/krisenfrueherkennung-starug-vier-varianten/README.md) | [Gesamt-PDF](../testakten/krisenfrueherkennung-starug-vier-varianten/gesamt-pdf/krisenfrueherkennung-starug-vier-varianten_gesamt.pdf) | [`testakte-krisenfrueherkennung-starug-vier-varianten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-krisenfrueherkennung-starug-vier-varianten.zip) | [`testakte-krisenfrueherkennung-starug-vier-varianten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-krisenfrueherkennung-starug-vier-varianten-einzelpdfs.zip) |
| [StaRUG-Aufhebung der Restrukturierungssache — Holding Düsseldorf (BGH IX ZB 18/25)](../testakten/starug-aufhebung-holding-duesseldorf-ix-zb-18-25/README.md) | [Gesamt-PDF](../testakten/starug-aufhebung-holding-duesseldorf-ix-zb-18-25/gesamt-pdf/starug-aufhebung-holding-duesseldorf-ix-zb-18-25_gesamt.pdf) | [`testakte-starug-aufhebung-holding-duesseldorf-ix-zb-18-25.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-starug-aufhebung-holding-duesseldorf-ix-zb-18-25.zip) | [`testakte-starug-aufhebung-holding-duesseldorf-ix-zb-18-25-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-starug-aufhebung-holding-duesseldorf-ix-zb-18-25-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du Eröffnungsgrund und Fortbestehensprognose belastbar bestimmen und den nächsten Verfahrensschritt wählen.
**Plugin-Slug:** `krisenfrueherkennung-starug`
**Version:** 435.1.0
**Autor:** Klotzkette

---

## Installation

1. ZIP aus dem Release herunterladen.
2. Plugin-Umgebung öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `krisenfrueherkennung-starug.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe unser Frühwarnsystem nach Paragraf 1 StaRUG, den Prognosehorizont nach Paragraf 18 InsO und die Organhaftung.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Kernbotschaft

> Krisenfrüherkennung ist eine fortlaufende Leitungsaufgabe. Paragraf 1 StaRUG verlangt Überwachung, Gegenmaßnahmen und Organbericht, nennt aber keinen festen Planungshorizont. Die regelmäßige 24-Monats-Prognose gehört zur drohenden Zahlungsunfähigkeit nach Paragraf 18 Absatz 2 InsO.

---

## Überblick

Dieses Plugin bietet kanzleitaugliche Werkzeuge für Geschäftsführer, Restrukturierungsberater, Steuerberater, Wirtschaftsprüfer und Rechtsanwälte. Es trennt das fortlaufende Frühwarn- und Reaktionssystem nach Paragraf 1 StaRUG von der 24-Monats-Prognose nach Paragraf 18 Absatz 2 InsO und führt von der Insolvenzreifeprüfung über die integrierte Planung bis zu Restrukturierungsplan und Stabilisierungsanordnung.

## Zielgruppe

- Geschäftsführer und Vorstände mittelständischer Unternehmen
- Restrukturierungsberater und Insolvenzverwalter
- Steuerberater, Steuerbevollmächtigte, Wirtschaftsprüfer, vereidigte Buchprüfer und Rechtsanwälte, die einen Jahresabschluss erstellen und den eng begrenzten Hinweis nach Paragraf 102 StaRUG prüfen müssen
- Rechtsanwälte im Sanierungs- und Insolvenzrecht
- Compliance-Beauftragte

---

## Skills-Übersicht

### Block A — Rechtliche Grundlagen und Pflichten

| Skill | Thema |
|---|---|
| `paragraph-1-starug-pflichten-und-24-monats-horizont` | Paragraf 1 StaRUG auslegen und vom 24-Monats-Prognosezeitraum nach Paragraf 18 Absatz 2 InsO abgrenzen |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` | Persönliche Haftung, Business Judgment Rule in der Krise, Beweislastumkehr |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

### Block B — Frühwarnsystem und Prognoseplanung aufbauen

| Skill | Thema |
|---|---|
| `fruehwarnsystem-architektur-zwei-jahres-horizont` | Risiko-Inventar, KPI-Kaskade und Eskalationsstufen; Planungshorizonte nach Zweck trennen |
| `rollierende-liquiditaetsplanung-24-monate-template` | Status, Drei-Wochen-Sicht, 13-Wochen-Steuerung und 24-Monats-Prognose mit Stresstests |
| `integrierte-planung-guv-bilanz-cashflow` | Drei-Statement-Modell, Working-Capital-Modellierung, Investitions-/Finanzierungsplan |
| `kennzahlenset-und-ampelsystem-starug-konform` | Frühwarn-KPIs, Ampelsystem rot/gelb/grün mit numerischen Schwellen |

### Block C — Krisenstadien-Diagnostik

| Skill | Thema |
|---|---|
| `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` | IDW S 6 Stadienlehre, Diagnose-Checklisten je Stadium |
| `drohende-zahlungsunfaehigkeit-paragraph-18-inso` | Prognosezeitraum, Fälligkeiten, objektiver Forderungsbestand und Abgrenzung zu Paragrafen 17 und 19 InsO |
| `fortbestehensprognose-zweistufig` | Positive Fortführungsprognose IDW S 11, Dokumentationspflicht |
| `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` | Paragraf 15a InsO: unverzüglicher Antrag, höchstens drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung |

### Block D — StaRUG-Werkzeuge nutzen

| Skill | Thema |
|---|---|
| `restrukturierungsplan-architektur-paragraph-7ff-starug` | Darstellender und gestaltender Teil, Auswahl, Gruppen, Anlagen, Mehrheiten und Bestätigung |
| `stabilisierungsanordnung-und-vollstreckungssperre` | Paragrafen 49 bis 59 StaRUG, Antrag, sechsmonatiger Finanzplan, Dauer und Aufhebung |
| `cross-class-cram-down-und-absolute-priority` | Paragrafen 26 bis 28 StaRUG, Vergleichsrechnung, Planwert, Rang und zulässige Durchbrechungen |
| `restrukturierungsbeauftragter-und-sachwalter` | Paragrafen 73 bis 79 StaRUG, Pflicht- und fakultative Bestellung, Aufgaben und Vergütung |

### Block E — Kanzlei- und Geschäftsführer-Werkzeuge

| Skill | Thema |
|---|---|
| `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` | Krisenprotokoll, Sitzungs-Templates, Beweissicherung |
| `mandantenbrief-warnung-paragraph-102-starug-template` | Volltextvorlagen für den tatbestandsgebundenen Hinweis nach Paragraf 102 StaRUG bei Jahresabschlusserstellung, Eskalation und Zugangsbeleg |
| `restructuring-lounge-impulsvortrag-toolkit` | Foliensätze, Talking-Points, Q&A-Fallnetz für Vortragsformate |

---

## Rechtlicher Hinweis

Alle in diesem Plugin verwendeten Personen, Kanzleinamen und Mandantennamen sind fiktiv. Das Plugin dient der allgemeinen rechtlichen Information und ersetzt keine individuelle Rechtsberatung im Einzelfall.

---

## Rechtsgrundlagen (Kernreferenzen)

- Paragrafen 1, 2 bis 28, 29 bis 33, 49 bis 59, 60 bis 67, 72 bis 79 und 102 StaRUG
- Paragrafen 15a, 17, 18 und 19 InsO
- Paragraf 43 GmbHG
- Paragraf 93 AktG
- IDW S 6 (Sanierungskonzepte)
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen)
- IDW PS 340 n.F. (Risikofrüherkennungssysteme)

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`ampelsystem-beweislast-und-darlegungslast`](skills/ampelsystem-beweislast-und-darlegungslast/SKILL.md), [`dokumentationspflicht-und-protokollierung-geschaeftsfuehrung`](skills/dokumentationspflicht-und-protokollierung-geschaeftsfuehrung/SKILL.md), [`geschaeftsfuehrerhaftung-quellenkarte-check`](skills/geschaeftsfuehrerhaftung-quellenkarte-check/SKILL.md), [`krisenmanagement-tatbestand-beweis-und-belege`](skills/krisenmanagement-tatbestand-beweis-und-belege/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`restrukturierungsplan-formular-portal-und-einreichung`](skills/restrukturierungsplan-formular-portal-und-einreichung/SKILL.md), [`spezial-geschaeftsfuehrerhaftung-livequellen-check`](skills/spezial-geschaeftsfuehrerhaftung-livequellen-check/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md), [`zahlungsunfaehigkeit-compliance-dokumentation-und-akte`](skills/zahlungsunfaehigkeit-compliance-dokumentation-und-akte/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg`](skills/gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`krisenstadien-fristennotiz-starug-gf-haftung`](skills/krisenstadien-fristennotiz-starug-gf-haftung/SKILL.md), [`monats-risikoampel-und-gegenargumente`](skills/monats-risikoampel-und-gegenargumente/SKILL.md), [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`integrierte-planung-kennzahlenset-ampelsystem`](skills/integrierte-planung-kennzahlenset-ampelsystem/SKILL.md), [`kfe-restrukturierungsbeauftragter`](skills/kfe-restrukturierungsbeauftragter/SKILL.md), [`krisenstadien-stakeholder-strategie-ergebnis-liquiditaet`](skills/krisenstadien-stakeholder-strategie-ergebnis-liquiditaet/SKILL.md), [`pflicht-planung-restrukturierungsplan`](skills/pflicht-planung-restrukturierungsplan/SKILL.md), [`planung-internationaler-bezug-und-schnittstellen`](skills/planung-internationaler-bezug-und-schnittstellen/SKILL.md), [`restrukturierungsbeauftragter-und-sachwalter`](skills/restrukturierungsbeauftragter-und-sachwalter/SKILL.md), [`restrukturierungsplan-architektur-rollierende`](skills/restrukturierungsplan-architektur-rollierende/SKILL.md), [`rollierende-liquiditaetsplanung-24-monate-template`](skills/rollierende-liquiditaetsplanung-24-monate-template/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`fruehwarnsystem-behoerden-gericht-und-registerweg`](skills/fruehwarnsystem-behoerden-gericht-und-registerweg/SKILL.md), [`insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist`](skills/insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist/SKILL.md), [`stabilisierungsanordnung-und-vollstreckungssperre`](skills/stabilisierungsanordnung-und-vollstreckungssperre/SKILL.md), [`starug-fristen-form-und-zustaendigkeit`](skills/starug-fristen-form-und-zustaendigkeit/SKILL.md), [`starug-stabilisierungsanordnung-vollstreckungsstopp`](skills/starug-stabilisierungsanordnung-vollstreckungsstopp/SKILL.md), [`warnpflicht-schriftsatz-brief-und-memo-bausteine`](skills/warnpflicht-schriftsatz-brief-und-memo-bausteine/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`mandantenbrief-warnung-paragraph-starug`](skills/mandantenbrief-warnung-paragraph-starug/SKILL.md), [`mandantenkommunikation-redteam`](skills/mandantenkommunikation-redteam/SKILL.md), [`output-waehlen`](skills/output-waehlen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`berater-drohende-fruehwarnsystem`](skills/berater-drohende-fruehwarnsystem/SKILL.md), [`cross-class-cram-down-und-absolute-priority`](skills/cross-class-cram-down-und-absolute-priority/SKILL.md), [`drohende-zahlen-schwellen-und-berechnung`](skills/drohende-zahlen-schwellen-und-berechnung/SKILL.md), [`drohende-zahlungsunfaehigkeit`](skills/drohende-zahlungsunfaehigkeit/SKILL.md), [`fortbestehensprognose-zweistufig`](skills/fortbestehensprognose-zweistufig/SKILL.md), [`fruehwarnsystem-architektur-zwei-jahres-horizont`](skills/fruehwarnsystem-architektur-zwei-jahres-horizont/SKILL.md), [`integrierte-interessen-kennzahlenset`](skills/integrierte-interessen-kennzahlenset/SKILL.md), [`kennzahlenset-mandantenentscheidung`](skills/kennzahlenset-mandantenentscheidung/SKILL.md), [`kennzahlenset-und-ampelsystem-starug-konform`](skills/kennzahlenset-und-ampelsystem-starug-konform/SKILL.md), [`kfe-fruherkennungssystem-bauleiter`](skills/kfe-fruherkennungssystem-bauleiter/SKILL.md), [`kfe-krisenstab-cross-class`](skills/kfe-krisenstab-cross-class/SKILL.md), [`kfe-krisenstab-massnahmen-leitfaden`](skills/kfe-krisenstab-massnahmen-leitfaden/SKILL.md), [`kfe-stabilisierungsanordnung-spezial`](skills/kfe-stabilisierungsanordnung-spezial/SKILL.md), [`konform-sonderfall-und-edge-case`](skills/konform-sonderfall-und-edge-case/SKILL.md), [`krisenfrueherkennung-krisenmanagement-monats`](skills/krisenfrueherkennung-krisenmanagement-monats/SKILL.md), [`paragraph-1-starug-pflichten-und-24-monats-horizont`](skills/paragraph-1-starug-pflichten-und-24-monats-horizont/SKILL.md), [`paragraph-102-starug-warnpflicht-bei-rechtsberatern`](skills/paragraph-102-starug-warnpflicht-bei-rechtsberatern/SKILL.md), [`pflichtenkollision-shift-restructuring-lounge`](skills/pflichtenkollision-shift-restructuring-lounge/SKILL.md), ... plus 2 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`ampelsystem-beweislast-und-darlegungslast`](skills/ampelsystem-beweislast-und-darlegungslast/SKILL.md) | Wenn es um Ampelsystem: Beweislast, Darlegungslast und Substantiierung in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortsc... |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in Krisenfrüherkennung und StaRUG-Management geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| [`berater-drohende-fruehwarnsystem`](skills/berater-drohende-fruehwarnsystem/SKILL.md) | Wenn es um Berater: Verhandlung, Vergleich und Eskalation in Krisenfrüherkennung und StaRUG-Management geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`cross-class-cram-down-und-absolute-priority`](skills/cross-class-cram-down-und-absolute-priority/SKILL.md) | Prüft den Cross-Class-Cram-Down nach Paragrafen 26 bis 28 StaRUG gruppengenau: Ohne-Plan-Vergleich, Planwertbeteiligung, Gruppenmehrheit, Rangfolge, gesetzliche Ausnahmen und Minderheitenschutz. Liefert Cram-Down-Memo, Wertbrücke, Abstim... |
| [`dokumentationspflicht-und-protokollierung-geschaeftsfuehrung`](skills/dokumentationspflicht-und-protokollierung-geschaeftsfuehrung/SKILL.md) | Wenn es um Dokumentationspflicht und Protokollierung — Beweissicherung für Haftungsprozesse in Krisenfrüherkennung und StaRUG-Management geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substanti... |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`drohende-zahlen-schwellen-und-berechnung`](skills/drohende-zahlen-schwellen-und-berechnung/SKILL.md) | Wenn es um Drohende: Zahlen, Schwellenwerte und Berechnung in Krisenfrüherkennung und StaRUG-Management geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und K... |
| [`drohende-zahlungsunfaehigkeit`](skills/drohende-zahlungsunfaehigkeit/SKILL.md) | Prüft drohende Zahlungsunfähigkeit nach Paragraf 18 InsO aus Liquiditätsstatus, Fälligkeiten und regelmäßig 24-monatiger Prognose. Grenzt Paragrafen 17 und 19 InsO ab, behandelt streitige und titulierte Forderungen korrekt und liefert St... |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Krisenfrüherkennung und StaRUG-Management geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fortbestehensprognose-zweistufig`](skills/fortbestehensprognose-zweistufig/SKILL.md) | Wenn es um Fortbestehensprognose — Zweistufiges Modell nach IDW S 11 in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschr... |
| [`fruehwarnsystem-architektur-zwei-jahres-horizont`](skills/fruehwarnsystem-architektur-zwei-jahres-horizont/SKILL.md) | Wenn es um Frühwarnsystem-Architektur mit Zwei-Jahres-Horizont in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fruehwarnsystem-behoerden-gericht-und-registerweg`](skills/fruehwarnsystem-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Fruehwarnsystem: Behörden-, Gerichts- oder Registerweg in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`geschaeftsfuehrerhaftung-quellenkarte-check`](skills/geschaeftsfuehrerhaftung-quellenkarte-check/SKILL.md) | Wenn es um Geschäftsführerhaftung Quellenkarte Check in Krisenfrüherkennung und StaRUG-Management geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenar... |
| [`gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg`](skills/gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg/SKILL.md) | Wenn es um Geschäftsführerhaftung — Paragraf 43 GmbHG und Paragraf 93 AktG in der Krise in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoa... |
| [`insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist`](skills/insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist/SKILL.md) | Prüft die Insolvenzantragspflicht nach Paragraf 15a InsO ab objektivem Eintritt von Zahlungsunfähigkeit oder Überschuldung. Trennt Drei- und Sechswochen-Höchstzeitraum, Kenntnis, Sanierungsbemühungen, Zahlungen und StaRUG-Route; liefert... |
| [`integrierte-interessen-kennzahlenset`](skills/integrierte-interessen-kennzahlenset/SKILL.md) | Wenn es um Integrierte: Mehrparteienkonflikt und Interessenmatrix in Krisenfrüherkennung und StaRUG-Management geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahme... |
| [`integrierte-planung-kennzahlenset-ampelsystem`](skills/integrierte-planung-kennzahlenset-ampelsystem/SKILL.md) | Wenn es um Integrierte Planung — GuV, Bilanz und Cashflow in Krisenfrüherkennung und StaRUG-Management geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Ko... |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Krisenfrüherkennung StaRUG ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kennzahlenset-mandantenentscheidung`](skills/kennzahlenset-mandantenentscheidung/SKILL.md) | Wenn es um Kennzahlenset: Mandantenkommunikation und Entscheidungsvorlage in Krisenfrüherkennung und StaRUG-Management geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Mandantennachricht oder Entscheid... |
| [`kennzahlenset-und-ampelsystem-starug-konform`](skills/kennzahlenset-und-ampelsystem-starug-konform/SKILL.md) | Wenn es um Kennzahlenset und Ampelsystem — StaRUG-konform in Krisenfrüherkennung und StaRUG-Management geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Ko... |
| [`kfe-fruherkennungssystem-bauleiter`](skills/kfe-fruherkennungssystem-bauleiter/SKILL.md) | Wenn es um KFE: Frueherkennungssystem in Krisenfrüherkennung und StaRUG-Management geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`kfe-krisenstab-cross-class`](skills/kfe-krisenstab-cross-class/SKILL.md) | Wenn es um KFE: Krisenstab Maßnahmen in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kfe-krisenstab-massnahmen-leitfaden`](skills/kfe-krisenstab-massnahmen-leitfaden/SKILL.md) | Wenn es um KFE: Krisenstab Massnahmen in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kfe-restrukturierungsbeauftragter`](skills/kfe-restrukturierungsbeauftragter/SKILL.md) | Wenn es um KFE: Restrukturierungsbeauftragter in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kfe-stabilisierungsanordnung-spezial`](skills/kfe-stabilisierungsanordnung-spezial/SKILL.md) | Wenn es um KFE: Stabilisierungsanordnung in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`konform-sonderfall-und-edge-case`](skills/konform-sonderfall-und-edge-case/SKILL.md) | Wenn es um Konform: Sonderfall und Edge-Case-Prüfung in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`krisenfrueherkennung-krisenmanagement-monats`](skills/krisenfrueherkennung-krisenmanagement-monats/SKILL.md) | Wenn es um Krisenfrueherkennung: Erstprüfung, Rollenklärung und Mandatsziel in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sof... |
| [`krisenmanagement-tatbestand-beweis-und-belege`](skills/krisenmanagement-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Krisenmanagement: Tatbestandsmerkmale, Beweisfragen und Beleglage in Krisenfrüherkennung und StaRUG-Management geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`krisenstadien-fristennotiz-starug-gf-haftung`](skills/krisenstadien-fristennotiz-starug-gf-haftung/SKILL.md) | Wenn es um Krisenstadien: Fristennotiz und nächster Schritt in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`krisenstadien-stakeholder-strategie-ergebnis-liquiditaet`](skills/krisenstadien-stakeholder-strategie-ergebnis-liquiditaet/SKILL.md) | Wenn es um Krisenstadien-Diagnostik — IDW S 6 Stadienlehre in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mandantenbrief-warnung-paragraph-starug`](skills/mandantenbrief-warnung-paragraph-starug/SKILL.md) | Erstellt einen konkreten Mandantenhinweis nach Paragraf 102 StaRUG, wenn bei der Jahresabschlusserstellung offenkundige Anhaltspunkte für einen möglichen Insolvenzgrund vorliegen. Liefert Ersthinweis, Eskalation, Aktenvermerk und Zugangs... |
| [`mandantenkommunikation-redteam`](skills/mandantenkommunikation-redteam/SKILL.md) | Wenn es um Mandantenkommunikation in Krisenfrüherkennung und StaRUG-Management geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| [`monats-risikoampel-und-gegenargumente`](skills/monats-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Monats: Risikoampel, Gegenargumente und Verteidigungslinien in Krisenfrüherkennung und StaRUG-Management geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sof... |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Krisenfrüherkennung und StaRUG-Management geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`paragraph-1-starug-pflichten-und-24-monats-horizont`](skills/paragraph-1-starug-pflichten-und-24-monats-horizont/SKILL.md) | Trennt die fortlaufende Krisenfrüherkennungs- und Reaktionspflicht nach Paragraf 1 StaRUG sauber von der regelmäßigen 24-Monats-Prognose nach Paragraf 18 Absatz 2 InsO. Liefert Pflichtenmemo, Organ- und Eskalationsmatrix, dokumentiertes... |
| [`paragraph-102-starug-warnpflicht-bei-rechtsberatern`](skills/paragraph-102-starug-warnpflicht-bei-rechtsberatern/SKILL.md) | Prüft den eng begrenzten Hinweis nach Paragraf 102 StaRUG bei der Erstellung eines Jahresabschlusses. Trennt den gesetzlichen Tatbestand von sonstigen Mandatspflichten, ordnet offenkundige Insolvenzindizien und Mandantenkenntnis belegt e... |
| [`pflicht-planung-restrukturierungsplan`](skills/pflicht-planung-restrukturierungsplan/SKILL.md) | Wenn es um Pflicht: Dokumentenmatrix, Lückenliste und Nachforderung in Krisenfrüherkennung und StaRUG-Management geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`pflichtenkollision-shift-restructuring-lounge`](skills/pflichtenkollision-shift-restructuring-lounge/SKILL.md) | Wenn es um Pflichtenkollision und Shift of Fiduciary Duties in der Krise in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |
| [`planung-internationaler-bezug-und-schnittstellen`](skills/planung-internationaler-bezug-und-schnittstellen/SKILL.md) | Wenn es um Planung: Internationaler Bezug und Schnittstellen in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in Krisenfrüherkennung und StaRUG-Management geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`restructuring-lounge-impulsvortrag-toolkit`](skills/restructuring-lounge-impulsvortrag-toolkit/SKILL.md) | Wenn es um Impulsvortrag-Toolkit — StaRUG und Krisenfrüherkennung in Krisenfrüherkennung und StaRUG-Management geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt m... |
| [`restrukturierungsbeauftragter-und-sachwalter`](skills/restrukturierungsbeauftragter-und-sachwalter/SKILL.md) | Wenn es um Restrukturierungsbeauftragter und Sachwalter — Paragraf 73 StaRUG in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit So... |
| [`restrukturierungsplan-architektur-rollierende`](skills/restrukturierungsplan-architektur-rollierende/SKILL.md) | Baut einen Restrukturierungsplan nach Paragrafen 2 bis 28 StaRUG belastbar auf: Planbetroffene, darstellender und gestaltender Teil, Auswahl, Gruppen, Gleichbehandlung, Anlagen, Abstimmung, Cram-Down und Bestätigung. Liefert Planstruktur... |
| [`restrukturierungsplan-formular-portal-und-einreichung`](skills/restrukturierungsplan-formular-portal-und-einreichung/SKILL.md) | Wenn es um Restrukturierungsplan: Formular, Portal und Einreichungslogik in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |
| [`rollierende-liquiditaetsplanung-24-monate-template`](skills/rollierende-liquiditaetsplanung-24-monate-template/SKILL.md) | Erstellt eine rollierende Liquiditätsplanung für Status, Drei-Wochen-Sicht, 13-Wochen-Steuerung und die regelmäßige 24-Monats-Prognose nach Paragraf 18 Absatz 2 InsO. Ordnet Fälligkeiten, streitige Forderungen, Kreditlinien, Szenarien un... |
| [`spezial-geschaeftsfuehrerhaftung-livequellen-check`](skills/spezial-geschaeftsfuehrerhaftung-livequellen-check/SKILL.md) | Wenn es um Geschaeftsfuehrerhaftung: Livequellen- und Rechtsprechungscheck in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofo... |
| [`stabilisierungsanordnung-und-vollstreckungssperre`](skills/stabilisierungsanordnung-und-vollstreckungssperre/SKILL.md) | Bereitet eine Stabilisierungsanordnung nach Paragrafen 49 bis 59 StaRUG vor: Anzeige, Adressaten, Vollstreckungs- und Verwertungssperre, sechsmonatiger Finanzplan, Anordnungsvoraussetzungen, Dauer, Vertragswirkungen und Aufhebung. Liefer... |
| [`stakeholder-warnpflicht-zahlungsunfaehigkeit`](skills/stakeholder-warnpflicht-zahlungsunfaehigkeit/SKILL.md) | Wenn es um Stakeholder: Abschlussprodukt und Übergabe in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md) | Startet ein Krisen- oder Restrukturierungsmandat ohne Leerlauf, wertet vorhandene Unterlagen zuerst aus und trennt Zahlungsunfähigkeit, Überschuldung, drohende Zahlungsunfähigkeit, Frühwarnpflicht und gerichtliche Instrumente. Liefert Ch... |
| [`starug-fristen-form-und-zustaendigkeit`](skills/starug-fristen-form-und-zustaendigkeit/SKILL.md) | Wenn es um StaRUG: Fristen, Form, Zuständigkeit und Rechtsweg in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`starug-stabilisierungsanordnung-vollstreckungsstopp`](skills/starug-stabilisierungsanordnung-vollstreckungsstopp/SKILL.md) | Wenn es um Stabilisierungsanordnung: Red-Team und Qualitätskontrolle in Krisenfrüherkennung und StaRUG-Management geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofor... |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`warnpflicht-schriftsatz-brief-und-memo-bausteine`](skills/warnpflicht-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Wenn es um Warnpflicht: Schriftsatz-, Brief- und Memo-Bausteine in Krisenfrüherkennung und StaRUG-Management geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen,... |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Krisenfrüherkennung und StaRUG-Management geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel in Krisenfrüherkennung und StaRUG-Management geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Krisenfrüherkennung und StaRUG-Management geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in Krisenfrüherkennung und StaRUG-Management geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Krisenfrüherkennung und StaRUG-Management geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`zahlungsunfaehigkeit-compliance-dokumentation-und-akte`](skills/zahlungsunfaehigkeit-compliance-dokumentation-und-akte/SKILL.md) | Wenn es um Zahlungsunfaehigkeit: Compliance-Dokumentation und Aktenvermerk in Krisenfrüherkennung und StaRUG-Management geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.

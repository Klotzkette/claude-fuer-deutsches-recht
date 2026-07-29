# Liquiditätsplanung — Power-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Liquiditätsplanung nach deutschem Recht: 3-Wochen-Vorschau, 13/26/52-Wochen-Forecast, Excel-Export, Quote/Lücken-Ampel, Dokumentationspaket und Schnittstellen zu Fortbestehensprognose und Insolvenzrecht. Rechtsprechung nur nach Live-Verifikation.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/liquiditaetsplanung.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`liquiditaetsplanung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/liquiditaetsplanung/liquiditaetsplanung-werkstatt.md" download><code>liquiditaetsplanung-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/liquiditaetsplanung/liquiditaetsplanung-schnellstart.md" download><code>liquiditaetsplanung-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Edelholz Manufaktur Berlin GmbH — Liquiditäts- und Steuerakte](../testakten/edelholz-manufaktur-berlin-liquiditaet/README.md) | [Gesamt-PDF](../testakten/edelholz-manufaktur-berlin-liquiditaet/gesamt-pdf/edelholz-manufaktur-berlin-liquiditaet_gesamt.pdf) | [`testakte-edelholz-manufaktur-berlin-liquiditaet.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-edelholz-manufaktur-berlin-liquiditaet.zip) | [`testakte-edelholz-manufaktur-berlin-liquiditaet-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-edelholz-manufaktur-berlin-liquiditaet-einzelpdfs.zip) |
| [Forschungszulage Riedblick Sensorik GmbH](../testakten/forschungszulage-sensorik-startup-taunus/README.md) | [Gesamt-PDF](../testakten/forschungszulage-sensorik-startup-taunus/gesamt-pdf/forschungszulage-sensorik-startup-taunus_gesamt.pdf) | [`testakte-forschungszulage-sensorik-startup-taunus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-forschungszulage-sensorik-startup-taunus.zip) | [`testakte-forschungszulage-sensorik-startup-taunus-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-forschungszulage-sensorik-startup-taunus-einzelpdfs.zip) |
| [Fortbestehensprognose Paragrafix GmbH](../testakten/fortbestehensprognose-paragrafix-gmbh/README.md) | [Gesamt-PDF](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf) | [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) | [`testakte-fortbestehensprognose-paragrafix-gmbh-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine belastbare Liquiditätsplanung aufstellen und drohende Zahlungsunfähigkeit frühzeitig erkennen.
**Eigenständiges Power-Plugin** für wochenaktuelle Liquiditätsvorschauen nach deutschem Recht (§§ 17, 18, 19 InsO; § 1 StaRUG; BGH-Schema Passiva II). Funktioniert allein. Ergänzt sich optional mit `insolvenzrecht` und `steuerrecht-anwalt-und-berater`, hängt aber nicht von ihnen ab.

---

## Was ist drin

Vier Fachskills plus Allgemein-Skill, alle fachlich autark:

| Skill | Zweck | Horizont |
| --- | --- | --- |
| `idw-s6-integrierte-sanierungsplanung` | Brücke von Liquiditätsvorschau zu Sanierungskonzept: GuV, Planbilanz, Maßnahmenlog, Annahmenregister, Sensitivitäten und Sanierungsfähigkeits-Ampel. | 12-24 Monate |
| `liquiditaetsvorschau-3wochen` | Wochenaktuelle Vorprüfung § 17 InsO (Freitag-Stichtag), Verhältnis zu offenen Forderungen, Ampel. | 3 Wochen |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Planung mit Sensitivität (Best/Base/Worst), Fortbestehensprognose nach § 19 InsO und Übergabe in die Sanierungsplanung. | 13 / 26 / 52 Wochen |
| `liquiditaetsvorschau-insolvenzrechtlich` | Gerichtsfeste Liquiditätsbilanz nach BGH-Schema (Passiva II zwingend, Volumeneffekt der Quote, titulierte Forderungen mit Nennwert). | Stichtagsbezogen |

## Ergebnisformate

Jeder Skill liefert standardmäßig eine **Excel-Tabelle** nach der hinterlegten Vorlage (`assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`, KW-Spalten × Kategorien-Zeilen, Freitag als Wochenstichtag). Zusätzlich auf Wahl:

- **Interaktives HTML-Padlet** (`assets/padlet/liquiditaets-padlet.html`) — single-file, autark, rechnet die Ampel live nach BGH-Schema, speichert in `localStorage`, exportiert/importiert JSON.
- **Markdown-Artefakt** (`assets/markdown/liquiditaets-artefakt-vorlage.md`) — Tabellen, Indizienliste, Kurzfazit; wird bei jeder Folgemeldung neu geschrieben.
- **Memo** im Gutachtenstil (DOCX oder Markdown) — **nur auf ausdrückliche Anfrage**.

Die Skills fragen einmal am Anfang nach Format und merken sich die Antwort.

## Banking

Jeder Skill fragt einmal nach der Datenquelle:

1. **Manuell** im Padlet/Artefakt/Chat.
2. **Datei-Import** — CAMT.053, MT940, CSV-Bankexport, DATEV-OPOS.
3. **Connector** — PSD2/FinTS oder verfügbare Anbieter (per `list_external_tools`).

Mandatsgeheimnis (§§ 203/204 StGB, § 43e BRAO) und Drittlandtransfer (DSGVO Art. 44 ff.) werden adressiert.

## BGH-Schema (Passiva II)

```
Aktiva I   = Bank + Kasse + freier zugesagter Kontokorrent (Stichtag)
Aktiva II  = Σ Einzahlungen KW t..t+2
Passiva I  = am Stichtag fällig, eingefordert, nicht echt gestundet
Passiva II = binnen 3 Wochen fällig (KW t+1 + KW t+2)

Lücke abs. = max(0, (Passiva I + Passiva II) − (Aktiva I + Aktiva II))
Quote      = Lücke abs. ÷ (Passiva I + Passiva II)
```

**Ampel**: 🟢 Quote < 10 % und Liquidität KW t+2 ≥ 0 und < 2 Indizien. 🟡 Quote ≥ 10 %, KW t+2 ≥ 0, < 2 Indizien (schließbar). 🔴 sonst — § 17 InsO indiziert.

## Leitentscheidungen und Livecheck

Diese Entscheidungen sind als frei prüfbare Arbeitsanker gedacht; vor einer Mandatsausgabe immer Gericht, Datum, Aktenzeichen, Randnummer/Sachverhalt und Aussage anhand einer amtlichen oder frei zugänglichen Quelle nachziehen.

1. **BGH, Urteil vom 24.05.2005 - IX ZR 123/04**: Abgrenzung Zahlungsstockung/Zahlungsunfähigkeit; Liquiditätslücke von 10 Prozent oder mehr regelmäßig kritisch, wenn sie nicht kurzfristig nahezu vollständig geschlossen werden kann.
2. **BGH, Urteil vom 19.12.2017 - II ZR 88/16**: Liquiditätsstatus und Liquiditätsbilanz; Einbeziehung der innerhalb von drei Wochen fällig werdenden Verbindlichkeiten (Passiva II) in die Prüfung des § 17 InsO.
3. **BGH, Urteil vom 28.06.2022 - II ZR 112/21**: Zahlungsunfähigkeit kann mit geordneter Liquiditätsgegenüberstellung und Buchhaltungsunterlagen dargelegt werden; keine mechanische Scheingenauigkeit, sondern belegbare Zahlenbasis.
4. **Aktualitätsregel**: Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen. Wenn weitere Rechtsprechung gebraucht wird, erst live über `bundesgerichtshof.de`, `dejure.org` oder eine vom Nutzer bereitgestellte Quelle verifizieren.

Berufsständischer Hintergrund: Methodenrahmen zu Insolvenzeröffnungsgründen und Sanierungskonzepten; nicht als Ersatz für Gesetz, Rechtsprechung und konkrete Subsumtion zitieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`eingangsdaten-checkliste`](skills/eingangsdaten-checkliste/SKILL.md), [`eingangsdaten-idw-s6-liqp`](skills/eingangsdaten-idw-s6-liqp/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md), [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`chronologie-und-belegmatrix`](skills/chronologie-und-belegmatrix/SKILL.md), [`deutschem-dokumentationspaket-excel`](skills/deutschem-dokumentationspaket-excel/SKILL.md), [`deutschem-tatbestandsmerkmale-beweisfragen`](skills/deutschem-tatbestandsmerkmale-beweisfragen/SKILL.md), [`dokumentationspaket-bank`](skills/dokumentationspaket-bank/SKILL.md), [`insolvenzrecht-formular-portal`](skills/insolvenzrecht-formular-portal/SKILL.md), [`interessen-verifikation-beweislast-vorschau`](skills/interessen-verifikation-beweislast-vorschau/SKILL.md), [`liqp-warenkredit-skonto-szenarien-spezial`](skills/liqp-warenkredit-skonto-szenarien-spezial/SKILL.md), [`liquiditaetsstatus-quellenbelege`](skills/liquiditaetsstatus-quellenbelege/SKILL.md), [`liquiditaetsstatus-quellenbelege-live-quote`](skills/liquiditaetsstatus-quellenbelege-live-quote/SKILL.md), [`luecken-quellenkarte`](skills/luecken-quellenkarte/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`spezial-luecken-livequellen-und-rechtsprechungscheck`](skills/spezial-luecken-livequellen-und-rechtsprechungscheck/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`verifikation-beweislast-darlegungslast`](skills/verifikation-beweislast-darlegungslast/SKILL.md), [`vorschau-dokumentenmatrix-lueckenliste`](skills/vorschau-dokumentenmatrix-lueckenliste/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`forecast-risikoampel-gegenargumente`](skills/forecast-risikoampel-gegenargumente/SKILL.md), [`fristen-und-risikoampel`](skills/fristen-und-risikoampel/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`forecast-wochenplanung`](skills/forecast-wochenplanung/SKILL.md), [`idw-s6-integrierte-sanierungsplanung`](skills/idw-s6-integrierte-sanierungsplanung/SKILL.md), [`leasing-lp-restrukturierungsplan-starug`](skills/leasing-lp-restrukturierungsplan-starug/SKILL.md), [`quote-verhandlung-vergleich-eskalation`](skills/quote-verhandlung-vergleich-eskalation/SKILL.md), [`restrukturierungsplan-starug`](skills/restrukturierungsplan-starug/SKILL.md), [`stundungs-strategie`](skills/stundungs-strategie/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`ausgabengruppen-fristennotiz-naechster`](skills/ausgabengruppen-fristennotiz-naechster/SKILL.md), [`wochen-fristen-form-zustaendigkeit-rechtsweg`](skills/wochen-fristen-form-zustaendigkeit-rechtsweg/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`live-mandantenkommunikation`](skills/live-mandantenkommunikation/SKILL.md), [`mandantenkommunikation`](skills/mandantenkommunikation/SKILL.md), [`output-waehlen`](skills/output-waehlen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`mandantenkommunikation-redteam-qualitygate`](skills/mandantenkommunikation-redteam-qualitygate/SKILL.md), [`rechtsprechung-fehlerkatalog`](skills/rechtsprechung-fehlerkatalog/SKILL.md), [`redteam-qualitygate`](skills/redteam-qualitygate/SKILL.md), [`spezial-rechtsprechung-red-team-und-qualitaetskontrolle`](skills/spezial-rechtsprechung-red-team-und-qualitaetskontrolle/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`ampel-zahlen-schwellenwerte-berechnung`](skills/ampel-zahlen-schwellenwerte-berechnung/SKILL.md), [`ausgabengruppen-systematik`](skills/ausgabengruppen-systematik/SKILL.md), [`bei-drohender-zahlungsunfaehigkeit`](skills/bei-drohender-zahlungsunfaehigkeit/SKILL.md), [`bei-eingetretener-zahlungsunfaehigkeit`](skills/bei-eingetretener-zahlungsunfaehigkeit/SKILL.md), [`cash-pooling-konzern`](skills/cash-pooling-konzern/SKILL.md), [`drohender-zahlungsunfaehigkeit`](skills/drohender-zahlungsunfaehigkeit/SKILL.md), [`excel`](skills/excel/SKILL.md), [`export`](skills/export/SKILL.md), [`export-forecast-fortbestehensprognose`](skills/export-forecast-fortbestehensprognose/SKILL.md), [`fortbestehensprognose-international`](skills/fortbestehensprognose-international/SKILL.md), [`fuer-bankgespraech`](skills/fuer-bankgespraech/SKILL.md), [`grundbegriffe-cashflow`](skills/grundbegriffe-cashflow/SKILL.md), [`grundbegriffe-cashflow-kreditlinien`](skills/grundbegriffe-cashflow-kreditlinien/SKILL.md), [`insolvenzrecht-liqui-sonderfall`](skills/insolvenzrecht-liqui-sonderfall/SKILL.md), [`kreditlinien-pruefen`](skills/kreditlinien-pruefen/SKILL.md), [`liqp-bankenreporting-leitfaden`](skills/liqp-bankenreporting-leitfaden/SKILL.md), [`liqp-liquiditaetspool-cash-pooling-spezial`](skills/liqp-liquiditaetspool-cash-pooling-spezial/SKILL.md), [`liqp-liquiditaetspool-cash-rollende-13wochen`](skills/liqp-liquiditaetspool-cash-rollende-13wochen/SKILL.md), ... plus 14 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 74 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`ampel-zahlen-schwellenwerte-berechnung`](skills/ampel-zahlen-schwellenwerte-berechnung/SKILL.md) | Wenn es um Ampel: Zahlen, Schwellenwerte und Berechnung in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in Liquiditätsplanung — Power geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`ausgabengruppen-fristennotiz-naechster`](skills/ausgabengruppen-fristennotiz-naechster/SKILL.md) | Wenn es um Ausgabengruppen: Fristennotiz und nächster Schritt in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ausgabengruppen-systematik`](skills/ausgabengruppen-systematik/SKILL.md) | Wenn es um Liqui: Ausgabengruppen in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`bei-drohender-zahlungsunfaehigkeit`](skills/bei-drohender-zahlungsunfaehigkeit/SKILL.md) | Wenn es um Liqui: drohende ZU in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`bei-eingetretener-zahlungsunfaehigkeit`](skills/bei-eingetretener-zahlungsunfaehigkeit/SKILL.md) | Wenn es um Liqui: eingetretene ZU in Liquiditätsplanung — Power geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`cash-pooling-konzern`](skills/cash-pooling-konzern/SKILL.md) | Wenn es um Cash-Pooling im Konzern in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`chronologie-und-belegmatrix`](skills/chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix Liquiditätsplanung in Liquiditätsplanung — Power geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`deutschem-dokumentationspaket-excel`](skills/deutschem-dokumentationspaket-excel/SKILL.md) | Wenn es um Deutschem Dokumentationspaket Excel in Liquiditätsplanung — Power geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`deutschem-tatbestandsmerkmale-beweisfragen`](skills/deutschem-tatbestandsmerkmale-beweisfragen/SKILL.md) | Wenn es um Deutschem: Tatbestandsmerkmale, Beweisfragen und Beleglage in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dokumentationspaket-bank`](skills/dokumentationspaket-bank/SKILL.md) | Wenn es um Dokumentationspaket: Compliance-Dokumentation und Aktenvermerk in Liquiditätsplanung — Power geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`drohender-zahlungsunfaehigkeit`](skills/drohender-zahlungsunfaehigkeit/SKILL.md) | Wenn es um Liqui Drohender Zahlungsunfaehigkeit in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`eingangsdaten-checkliste`](skills/eingangsdaten-checkliste/SKILL.md) | Wenn es um Liqui: Eingangsdaten-Checkliste in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`eingangsdaten-idw-s6-liqp`](skills/eingangsdaten-idw-s6-liqp/SKILL.md) | Wenn es um Liqui Eingangsdaten IDW S6 Liqp in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Liquiditätsplanung — Power geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`excel`](skills/excel/SKILL.md) | Wenn es um Excel: Behörden-, Gerichts- oder Registerweg in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`export`](skills/export/SKILL.md) | Wenn es um Export: Schriftsatz-, Brief- und Memo-Bausteine in Liquiditätsplanung — Power geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`export-forecast-fortbestehensprognose`](skills/export-forecast-fortbestehensprognose/SKILL.md) | Wenn es um Export Forecast Fortbestehensprognose in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`forecast-risikoampel-gegenargumente`](skills/forecast-risikoampel-gegenargumente/SKILL.md) | Wenn es um Forecast: Risikoampel, Gegenargumente und Verteidigungslinien in Liquiditätsplanung — Power geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`forecast-wochenplanung`](skills/forecast-wochenplanung/SKILL.md) | Wenn es um Liquiditaetsplanung: Erstprüfung, Rollenklärung und Mandatsziel in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fortbestehensprognose-international`](skills/fortbestehensprognose-international/SKILL.md) | Wenn es um Fortbestehensprognose: Internationaler Bezug und Schnittstellen in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fristen-und-risikoampel`](skills/fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel Liquiditätsplanung in Liquiditätsplanung — Power geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fuer-bankgespraech`](skills/fuer-bankgespraech/SKILL.md) | Wenn es um Liqui für Bankgespraech in Liquiditätsplanung — Power geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`grundbegriffe-cashflow`](skills/grundbegriffe-cashflow/SKILL.md) | Wenn es um Liquiditaetsplanung: Grundbegriffe in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`grundbegriffe-cashflow-kreditlinien`](skills/grundbegriffe-cashflow-kreditlinien/SKILL.md) | Wenn es um Liqui Grundbegriffe Cashflow Kreditlinien in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`idw-s6-integrierte-sanierungsplanung`](skills/idw-s6-integrierte-sanierungsplanung/SKILL.md) | Wenn es um Integrierte Sanierungsplanung in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`insolvenzrecht-formular-portal`](skills/insolvenzrecht-formular-portal/SKILL.md) | Wenn es um Insolvenzrecht: Formular, Portal und Einreichungslogik in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`insolvenzrecht-liqui-sonderfall`](skills/insolvenzrecht-liqui-sonderfall/SKILL.md) | Wenn es um Insolvenzrecht Liqui Sonderfall in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`interessen-verifikation-beweislast-vorschau`](skills/interessen-verifikation-beweislast-vorschau/SKILL.md) | Wenn es um Interessen Verifikation Beweislast Vorschau in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Liquiditätsplanung ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md) | Wenn es um Kaltstart Triage in Liquiditätsplanung — Power geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kreditlinien-pruefen`](skills/kreditlinien-pruefen/SKILL.md) | Wenn es um Liqui: Kreditlinien in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`leasing-lp-restrukturierungsplan-starug`](skills/leasing-lp-restrukturierungsplan-starug/SKILL.md) | Wenn es um Liqui Leasing LP Restrukturierungsplan Starug in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`liqp-bankenreporting-leitfaden`](skills/liqp-bankenreporting-leitfaden/SKILL.md) | Wenn es um LiqP: Bankenreporting in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`liqp-liquiditaetspool-cash-pooling-spezial`](skills/liqp-liquiditaetspool-cash-pooling-spezial/SKILL.md) | Wenn es um LiqP: Cash-Pooling Spezial in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`liqp-liquiditaetspool-cash-rollende-13wochen`](skills/liqp-liquiditaetspool-cash-rollende-13wochen/SKILL.md) | Wenn es um Liqp Liquiditaetspool Cash Rollende 13wochen in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`liqp-rollende-13wochen-bauleiter`](skills/liqp-rollende-13wochen-bauleiter/SKILL.md) | Wenn es um LiqP: 13-Wochen-Plan Bauleiter in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`liqp-warenkredit-skonto-szenarien-spezial`](skills/liqp-warenkredit-skonto-szenarien-spezial/SKILL.md) | Wenn es um LiqP: Warenkredit Skonto in Liquiditätsplanung — Power geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`liqui-fuer-bankgespraech`](skills/liqui-fuer-bankgespraech/SKILL.md) | Wenn es um Liqui fuer Bankgespraech in Liquiditätsplanung — Power geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`liquiditaetsstatus-quellenbelege`](skills/liquiditaetsstatus-quellenbelege/SKILL.md) | Wenn es um Liquiditätsstatus nur aus belastbaren Quellenbelegen in Liquiditätsplanung — Power geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfra... |
| [`liquiditaetsstatus-quellenbelege-live-quote`](skills/liquiditaetsstatus-quellenbelege-live-quote/SKILL.md) | Wenn es um Liquiditaetsstatus Quellenbelege Live Quote in Liquiditätsplanung — Power geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`liquiditaetsvorschau-3-6-12-monate`](skills/liquiditaetsvorschau-3-6-12-monate/SKILL.md) | Wenn es um Rollierende Liquiditätsvorschau 3/6/12 Monate mit Fortführungsprognose (Paragrafen 17. 19 InsO) in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt... |
| [`liquiditaetsvorschau-3wochen`](skills/liquiditaetsvorschau-3wochen/SKILL.md) | Wenn es um Drei-Wochen-Liquiditätsvorschau (Paragraf 17 InsO, wochenaktuell) in Liquiditätsplanung — Power geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken... |
| [`liquiditaetsvorschau-insolvenzrechtlich`](skills/liquiditaetsvorschau-insolvenzrechtlich/SKILL.md) | Wenn es um Insolvenzrechtliche Liquiditätsbilanz und Liquiditätsvorschau in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfp... |
| [`live-mandantenkommunikation`](skills/live-mandantenkommunikation/SKILL.md) | Wenn es um Live: Mandantenkommunikation und Entscheidungsvorlage in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`luecken-quellenkarte`](skills/luecken-quellenkarte/SKILL.md) | Wenn es um Luecken Quellenkarte in Liquiditätsplanung — Power geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`mahnstufen-debitoren`](skills/mahnstufen-debitoren/SKILL.md) | Wenn es um Liqui: Debitorenseite in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mandantenkommunikation`](skills/mandantenkommunikation/SKILL.md) | Wenn es um Mandantenkommunikation Liquiditätsplanung in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mandantenkommunikation-redteam-qualitygate`](skills/mandantenkommunikation-redteam-qualitygate/SKILL.md) | Wenn es um Liquiditätskommunikation Red-Team und Quality-Gate in Liquiditätsplanung — Power geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| [`mit-leasing-und-lp`](skills/mit-leasing-und-lp/SKILL.md) | Wenn es um Liqui mit Leasing in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`quote-verhandlung-vergleich-eskalation`](skills/quote-verhandlung-vergleich-eskalation/SKILL.md) | Wenn es um Quote: Verhandlung, Vergleich und Eskalation in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`rechtsprechung-fehlerkatalog`](skills/rechtsprechung-fehlerkatalog/SKILL.md) | Wenn es um Rechtsprechung Fehlerkatalog in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`redteam-qualitygate`](skills/redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in Liquiditätsplanung — Power geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`restrukturierungsplan-starug`](skills/restrukturierungsplan-starug/SKILL.md) | Wenn es um Liqui im StaRUG-Plan in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`saisonalitaet-erkennen`](skills/saisonalitaet-erkennen/SKILL.md) | Wenn es um Liqui: Saisonalitaet in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`schnittstellen-mehrparteienkonflikt`](skills/schnittstellen-mehrparteienkonflikt/SKILL.md) | Wenn es um Schnittstellen: Mehrparteienkonflikt und Interessenmatrix in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`sondereffekt-grossauftrag`](skills/sondereffekt-grossauftrag/SKILL.md) | Wenn es um Sondereffekt Grossauftrag in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`sondereffekt-grossauftrag-stundungs`](skills/sondereffekt-grossauftrag-stundungs/SKILL.md) | Wenn es um Liqui Sondereffekt Grossauftrag Stundungs in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`sonderfall-edge-case`](skills/sonderfall-edge-case/SKILL.md) | Wenn es um Liqui: Sonderfall und Edge-Case-Prüfung in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-luecken-livequellen-und-rechtsprechungscheck`](skills/spezial-luecken-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Luecken: Livequellen- und Rechtsprechungscheck in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-rechtsprechung-red-team-und-qualitaetskontrolle`](skills/spezial-rechtsprechung-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Rechtsprechung: Red-Team und Qualitätskontrolle in Liquiditätsplanung — Power geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md) | Wenn es um Start, Chronologie und Fristen Liquiditätsvorschau in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`stundungs-strategie`](skills/stundungs-strategie/SKILL.md) | Wenn es um Stundungs-Strategie in Liquiditätsplanung — Power geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`szenarien-aufbauen`](skills/szenarien-aufbauen/SKILL.md) | Wenn es um Liqui-Szenarien in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verifikation-beweislast-darlegungslast`](skills/verifikation-beweislast-darlegungslast/SKILL.md) | Wenn es um Verifikation: Beweislast, Darlegungslast und Substantiierung in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vorschau-dokumentenmatrix-lueckenliste`](skills/vorschau-dokumentenmatrix-lueckenliste/SKILL.md) | Wenn es um Vorschau: Dokumentenmatrix, Lückenliste und Nachforderung in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`wochen-fristen-form-zustaendigkeit-rechtsweg`](skills/wochen-fristen-form-zustaendigkeit-rechtsweg/SKILL.md) | Wenn es um Wochen: Fristen, Form, Zuständigkeit und Rechtsweg in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`wochen-liqui-ausgabengruppen-cash`](skills/wochen-liqui-ausgabengruppen-cash/SKILL.md) | Wenn es um Wochen Liqui Ausgabengruppen Cash in Liquiditätsplanung — Power geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Liquiditätsplanung — Power geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Liquiditätsplanung — Power geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

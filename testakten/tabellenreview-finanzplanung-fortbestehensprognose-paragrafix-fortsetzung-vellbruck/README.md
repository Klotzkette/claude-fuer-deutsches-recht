# Akte: Tabellenreview Paragrafix GmbH — Fortbestehensprognose v23, IDW S 11

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Diese Arbeitsakte gibt es in zwei Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 539 KB) | PDF | [`gesamt-pdf/tabellenreview-finanzplanung-fortbestehensprognose-paragrafix-fortsetzung-vellbruck_gesamt.pdf`](gesamt-pdf/tabellenreview-finanzplanung-fortbestehensprognose-paragrafix-fortsetzung-vellbruck_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-tabellenreview-finanzplanung-fortbestehensprognose-paragrafix-fortsetzung-vellbruck.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-tabellenreview-finanzplanung-fortbestehensprognose-paragrafix-fortsetzung-vellbruck.zip) |

Die ZIP-URL ist stabil und zeigt immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

**Arbeitsakte.** Alle Personen, Anschriften, Aktenzeichen, Unternehmen und Modellwerte sind anonymisiert. Die Akte gehört fachlich zum Plugin `tabellenreview-3d`.

---

## Kurzbild

- Mandant: Paragrafix GmbH, Berlin (Software-Hersteller juristischer Datenbanken); in existenzieller Liquiditätskrise seit Q3 2025.
- Geschäftsführung: Dr. Cornelius Vellbruck-Steinheim (GF), CFO Annegret Pellbach-Roosendaal.
- Reviewauftrag: TabellenReview Wittfeldt Federkamp PartG, Federführung Dr. Henrike Wittfeldt-Steinheim (WPin, RAin).
- Gegenstand: Fortbestehensprognose-Modell v23 (Excel, 18 Sheets, ca. 2.400 Formeln) — Konsistenz, Plausibilität, Formelarchitektur, Versionsabgleich, IDW-S-11-Konformität.
- Aktenzeichen Reviewer: TR-WF-2026-PFX-0712; Hausnummer Paragrafix: PFX-2026-FoBP-v23.
- 10 Findings identifiziert: u.a. zirkulärer Bezug Cashflow/Zinsen (kritisch), Hardcoded-Werte statt Formeln, fehlerhafte Bilanzsummenformel, manipulierte Zinsprognoseannahmen v22→v23, versteckte Sheets mit Restposten.
- IDW-S-11-Konformität der Fortbestehensprognose fragwürdig; Wirtschaftsprüfer Birkholz & Partner verweigert vorläufig Bestätigungsvermerk.
- Bank (Mittelstandsbank Nordwest eG) setzt belastbare Fortbestehensprognose als Bedingung für Sanierungskredit (4,5 Mio. EUR) voraus.
- Insolvenzantragspflicht nach § 15a InsO durch GF geprüft; strafrechtliche Implikation Bilanzfälschung (§ 283b StGB) adressiert.
- Knüpft inhaltlich an die Akte fortbestehensprognose-paragrafix-gmbh an.

---

## Was diese Akte demonstriert

| Skill | Aktenstück | Demonstration |
|---|---|---|
| Mandatsübernahme und Reviewauftrag | 01, 02 | Auftragsbrief, Vollmacht, Unabhängigkeitsbestätigung |
| Modellbeschreibung und Architektur | 02, 03 | 18-Sheet-Aufbau, Input-/Rechen-/Ausgabeblätter |
| Versionierung und Änderungshistorie | 04, 19 | v18–v23-Vergleich, Manipulationsverdacht |
| Review-Achse Konsistenz | 05 | Querbezüge, Zellverknüpfungen, Blattübergänge |
| Review-Achse Plausibilität | 06 | Zahlenstamm, Branchenvergleich, Benchmark |
| Review-Achse Formelarchitektur | 07 | Zirkularitäten, Iterationsrechnung, Namenskonventionen |
| Findings-Dokumentation | 08–16 | 10 priorisierte Findings mit Zellreferenzen, Schwere, Auswirkung |
| IDW S 11 Konformität | 17 | Fortbestehensprognose-Standard, Mindestanforderungen |
| Handlungsempfehlungen | 18 | Fix-Roadmap, Priorisierung, Zeitplan |
| Versionsvergleich | 19 | Diff v22 vs. v23, manipulierte Annahmen |
| Kommunikation Geschäftsführung | 20, 21 | Stellungnahme, Protokoll Review-Workshop |
| Abschlussvermerk | 22 | Reviewergebnis, Vorbehalte, nächste Schritte |
| Insolvenz- und Strafrecht | 08, 11, 17 | § 15a InsO, § 283b StGB, HGB §§ 252, 264 |

---

## Aktenstücke

| Nr. | Datei | Inhalt |
|---|---|---|
| 01 | [`01-mandatsuebernahme-paragrafix-reviewauftrag.md`](01-mandatsuebernahme-paragrafix-reviewauftrag.md) | Auftragsannahme, Mandatsbedingungen, Unabhängigkeit |
| 02 | [`02-modellbeschreibung-fortbestehensprognose.md`](02-modellbeschreibung-fortbestehensprognose.md) | Modellzweck, Prognoserahmen, Parametrisierung |
| 03 | [`03-modellarchitektur-eingangsblaetter-rechenblaetter-ausgabe.md`](03-modellarchitektur-eingangsblaetter-rechenblaetter-ausgabe.md) | 18-Sheet-Architektur, Datenflüsse, Blattübersicht |
| 04 | [`04-versionierung-uebersicht-v18-v23.md`](04-versionierung-uebersicht-v18-v23.md) | Versionshistorie v18–v23, Änderungsmatrix |
| 05 | [`05-review-axe-1-konsistenz-quer-bezuege.md`](05-review-axe-1-konsistenz-quer-bezuege.md) | Querbezugsprüfung, Blatt-zu-Blatt-Konsistenz |
| 06 | [`06-review-axe-2-plausibilitaet-zahlenstamm.md`](06-review-axe-2-plausibilitaet-zahlenstamm.md) | Plausibilitätstests, Benchmarks, Branchenwerte |
| 07 | [`07-review-axe-3-formelarchitektur-zirkularitaet.md`](07-review-axe-3-formelarchitektur-zirkularitaet.md) | Formelprüfung, Zirkularbezüge, Namenskonventionen |
| 08 | [`08-finding-1-zirkularer-bezug-cashflow-zinsen.md`](08-finding-1-zirkularer-bezug-cashflow-zinsen.md) | Finding 1: Zirkulärer Bezug CF/Zinsen — kritisch |
| 09 | [`09-finding-2-hardcoded-werte-statt-formel.md`](09-finding-2-hardcoded-werte-statt-formel.md) | Finding 2: 47 hardcoded Werte in Rechenbereichen |
| 10 | [`10-finding-3-falsche-summenformel-bilanzsumme.md`](10-finding-3-falsche-summenformel-bilanzsumme.md) | Finding 3: Fehlerhafter SUM-Bereich Bilanzsumme |
| 11 | [`11-finding-4-veraltete-prognoseannahmen-zins.md`](11-finding-4-veraltete-prognoseannahmen-zins.md) | Finding 4: Zinsannahme v22→v23 manuell gedrückt |
| 12 | [`12-finding-5-doppelte-buchungen-rueckstellung.md`](12-finding-5-doppelte-buchungen-rueckstellung.md) | Finding 5: Doppelte Rückstellungsbuchung Pensions |
| 13 | [`13-finding-6-versteckte-blaetter-mit-restposten.md`](13-finding-6-versteckte-blaetter-mit-restposten.md) | Finding 6: 2 versteckte Sheets, Restpostenproblematik |
| 14 | [`14-finding-7-fehlende-quellen-szenarioparameter.md`](14-finding-7-fehlende-quellen-szenarioparameter.md) | Finding 7: Szenarioparameter ohne Quellenangabe |
| 15 | [`15-finding-8-fehlende-szenariorechnung-stress.md`](15-finding-8-fehlende-szenariorechnung-stress.md) | Finding 8: Stress-/Downside-Szenario fehlt komplett |
| 16 | [`16-finding-9-abweichende-makro-ausfuehrung.md`](16-finding-9-abweichende-makro-ausfuehrung.md) | Finding 9: VBA-Makro überschreibt manuell Sollwerte |
| 17 | [`17-finding-10-iddw-s-11-konformitaet-fortbestehensprognose.md`](17-finding-10-iddw-s-11-konformitaet-fortbestehensprognose.md) | Finding 10: IDW-S-11-Konformitätslücken |
| 18 | [`18-handlungsempfehlungen-roadmap-fix.md`](18-handlungsempfehlungen-roadmap-fix.md) | Fix-Roadmap, Prioritäten, Zeitplan, Verantwortliche |
| 19 | [`19-vergleichsreview-v22-vs-v23.md`](19-vergleichsreview-v22-vs-v23.md) | Detaillierter Diff v22/v23, Manipulationsverdacht |
| 20 | [`20-stellungnahme-an-geschaeftsfuehrung.md`](20-stellungnahme-an-geschaeftsfuehrung.md) | Formelle Stellungnahme WP an GF/CFO |
| 21 | [`21-protokoll-review-workshop.md`](21-protokoll-review-workshop.md) | Protokoll Review-Workshop 14.01.2026 |
| 22 | [`22-abschlussvermerk-reviewer.md`](22-abschlussvermerk-reviewer.md) | Abschlussvermerk, Einschränkungen, Votum |

---

## Anhänge

### DOCX

| Datei | Inhalt |
|---|---|
| [`docx/tabellenreview-bericht-paragrafix-fortbestehensprognose-v23.docx`](docx/tabellenreview-bericht-paragrafix-fortbestehensprognose-v23.docx) | Reviewbericht gesamt (Entwurf zur Freigabe) |
| [`docx/reviewer-checkliste-iddw-s-11.docx`](docx/reviewer-checkliste-iddw-s-11.docx) | IDW-S-11-Prüfcheckliste mit Abarbeitungsstatus |
| [`docx/stellungnahme-geschaeftsfuehrung.docx`](docx/stellungnahme-geschaeftsfuehrung.docx) | Formelle Stellungnahme an Geschäftsführung |

### XLSX

| Datei | Inhalt |
|---|---|
| [`xlsx/findings-register-tabellenreview.xlsx`](xlsx/findings-register-tabellenreview.xlsx) | Findings-Register: 10 Findings mit Schwere, Auswirkung EUR, Massnahme, Status |
| [`xlsx/version-changelog-modell.xlsx`](xlsx/version-changelog-modell.xlsx) | Versionshistorie v18–v23 mit Bearbeiter, Begründung, Reviewstatus |

### E-Mails (.eml)

| Datei | Inhalt |
|---|---|
| [`emails/email-paragrafix-cfo-an-reviewer.eml`](emails/email-paragrafix-cfo-an-reviewer.eml) | CFO Pellbach-Roosendaal beauftragt Review, 08.01.2026 |
| [`emails/email-reviewer-an-cfo-zwischenbefund.eml`](emails/email-reviewer-an-cfo-zwischenbefund.eml) | Dr. Wittfeldt-Steinheim: Zwischenbefund Kritikpunkte, 13.01.2026 |
| [`emails/email-wirtschaftspruefer-koordination.eml`](emails/email-wirtschaftspruefer-koordination.eml) | Koordination Birkholz & Partner WP / Reviewer, 15.01.2026 |
| [`emails/email-geschaeftsfuehrung-protokoll-review-workshop.eml`](emails/email-geschaeftsfuehrung-protokoll-review-workshop.eml) | Protokollversand Review-Workshop 14.01.2026 |
| [`emails/email-finanzierungspartner-mittelstandsbank-anfrage.eml`](emails/email-finanzierungspartner-mittelstandsbank-anfrage.eml) | Mittelstandsbank Nordwest: Anforderung belastbare Prognose |

### PDFs

| Datei | Inhalt |
|---|---|
| [`pdfs/tabellenreview-bericht-final.pdf`](pdfs/tabellenreview-bericht-final.pdf) | Reviewbericht final (druckfertig) |
| [`pdfs/findings-register-print.pdf`](pdfs/findings-register-print.pdf) | Findings-Register Druckversion |

### Fotos / Diagramme

| Datei | Inhalt |
|---|---|
| [`jpg/modellarchitektur-diagramm.jpg`](jpg/modellarchitektur-diagramm.jpg) | Schematische Darstellung der 18-Sheet-Modellarchitektur |
| [`jpg/screenshot-finding-2-hardcoded.jpg`](jpg/screenshot-finding-2-hardcoded.jpg) | Annotierter Screenshot: Hardcoded-Werte in Rechenblatt |
| [`jpg/cashflow-prognose-chart.jpg`](jpg/cashflow-prognose-chart.jpg) | Cashflow-Prognosechart v22 vs. v23 |

---

## Verfahrensstand

**Stichtag dieser Akte: Januar 2026**
**Reviewauftrag angenommen: 08. Januar 2026**

| Verfahrensstrang | Status |
|---|---|
| Reviewauftrag | Angenommen; AZ TR-WF-2026-PFX-0712 |
| Modellanalyse v23 | Abgeschlossen; 10 Findings |
| Versionsvergleich v18–v23 | Abgeschlossen; Manipulationsverdacht Finding 4 |
| IDW-S-11-Konformität | Lücken festgestellt; Finding 10 offen |
| Wirtschaftsprüfer Birkholz & Partner | Koordination läuft; vorläufige Versagung Testat |
| Sanierungskredit Mittelstandsbank | Ausstehend; Bank wartet belastbares Modell |
| Fix-Roadmap Paragrafix | In Umsetzung; Frist 31.01.2026 |
| Insolvenzantragspflicht § 15a InsO | Geprüft; aktuell kein akuter Antragsbedarf (Ergebnis vorbehaltlich) |
| § 283b StGB Bilanzfälschung | Strafrechtliches Risiko adressiert; externe StR-Beratung empfohlen |

Federführung Review: **Dr. Henrike Wittfeldt-Steinheim**, TabellenReview Wittfeldt Federkamp PartG, Berlin
Mitarbeit: **Karsten Federkamp**, Dipl.-Wirtschaftsmathematiker

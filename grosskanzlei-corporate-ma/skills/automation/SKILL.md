---
name: automation
description: "Monitoring und Automatisierungen für laufende M&A-Mandate einrichten: Anwendungsfall Deal-Team benoetigt automatisierte Überwachung von Datenraum-Neuzugaengen Q&A-Deadlines CP-Fristen Registerupdates und MAR-Signalen. Paragraf 35 ff. GWB Kartellrechtsfristen, Paragraf 55 ff. AWV FDI-Fristen, Art. 17 MAR Ad-h..."
---

# Automationen und Monitoring (Corporate M&A)

## Fachlicher Anker

- **Normenradar:** Paragraf 15, 16, 40, 43, 46 GmbHG; Paragraf 76, 93, 111 AktG; HGB-, UmwG-, GWB- und AWV-Bezug nur, wenn der konkrete Vorgang ihn trägt.
- **Rechtsprechungsanker:** BGH, 21.04.1997 - II ZR 175/95 für Organpflichten; BGH, 20.11.2018 - II ZR 12/17 für Gesellschafterlisten. Weitere Entscheidungen nur mit frei prüfbarer Quelle.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Automationen und Monitoring (Corporate M&A)
- **Prüfachse:** Ordne den konkreten Auftrag nach Gesellschaftsform, Dokument, Entscheidungsträger, Form, Frist, Beleg und Rechtsfolge; Spezialnormen nur nennen, wenn sie den Fall tragen.
- **Entscheidende Weiche:** Trenne Sachverhalt, Zuständigkeit, Zustimmung, Haftung, Vollzug und taktischen nächsten Schritt.
- **Arbeitsprodukt:** Liefere eine verwertbare Matrix mit `Tatsache / Norm / Beleg / Wertung / Gegenargument / nächster Schritt` und bei Bedarf einen ausformulierten Textbaustein.

## Triage zu Beginn

Vor dem Entwurf eines Monitoring-Plans klären:

1. **Deal-Phase:** Pre-Signing (Datenraum, Q&A, LOI-Frist) oder Post-Signing (CP-Deadlines, Regulatorie, Paragraf 613a BGB) oder PMI?
2. **Insiderinformationen betroffen?** Monitoring von boersenrelevanten Informationen erfordert MAR-Freigabe (Art. 17 MAR); automatische Aussenkommunikation ist verboten.
3. **Datenquellen identifiziert?** VDR (Intralinks, Datasite), Handelsregister, Bundesanzeiger, BKartA-Datenbank, DPMA, Nachrichtendienste?
4. **Owner-Matrix vorhanden?** Wer ist verantwortlich für welchen Workstream? Ohne Owner kein Monitoring-Plan.
5. **Eskalationsregeln definiert?** Ab wann wird eskaliert? (CP-Frist < 14 Tage, Datenraum-Neuzugang kritische Kategorie, MAR-Signal erkannt)
6. **Vertraulichkeitsrahmen geklaert?** Monitoring von externen Quellen muss Mandatsgeheimnis (Paragraf 43a Abs. 2 BRAO) und DSGVO (Art. 5 DSGVO) beachten.

## Zentrale Normen

Art. 17 MAR (Ad-hoc-Publizitaet; Insiderinformationen) — Paragraf 33 ff. WpHG (Stimmrechtsmitteilungen bei boersennotierter Zielgesellschaft) — Paragraf 35 ff. GWB (Fusionskontrolle BKartA; Vollzugsverbot bis Freigabe) — Paragraf 55 ff. AWV (FDI-Screening BMWK) — Paragraf 40 GmbHG (Gesellschafterliste; aktuelle Registerpublizitaet) — Paragraf 15 HGB (Handelsregisterpublizitaet; negative Publizitaet) — Art. 28 DSGVO (Auftragsverarbeitungsvertrag bei Monitoring-Dienstleistern) — Paragraf 43a Abs. 2 BRAO (Verschwiegenheitspflicht bei Monitoring-Datenverarbeitung)

## Aktuelle Rechtsprechung

- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.

## Monitoring-Kategorien und Prüfliste

### A: Datenraum-Monitoring (Pre-Signing)

| Monitor | Quelle | Frequenz | Owner | Eskalation |
|---|---|---|---|---|
| Neuzugaenge kritische Kategorie | VDR-API / Aktivitaetslog | Stundlich | DD-Lead | Sofort bei neuen Finanzunterlagen oder Material Adverse Change |
| Q&A-Antworten mit NDA-Implikation | VDR-Q&A | Taeglich | Legal | Bei Ablehnung oder Ausweichen |
| VDR-Zugriffsprotokoll | VDR-Admin | Woechentlich | IT-Security | Bei unberechtigtem Zugriff |

### B: CP-Deadline-Monitoring (Post-Signing)

| Monitor | Norm | Frist | Owner | Eskalation bei |
|---|---|---|---|---|
| Fusionskontrolle BKartA | Paragraf 35 ff. GWB | Vertraglich (typisch 3-6 Monate) | Regulatory-Lead | < 14 Tage bis Frist |
| FDI-Screening BMWK | Paragraf 55 ff. AWV | Vertraglich / gesetzlich | Regulatory-Lead | Behördenanfrage unbeantwortet |
| AR-Zustimmungsbeschluss | Paragraf 179a AktG | Vor Closing | Corporate-Lead | 21 Tage vor Closing |
| CoC-Zustimmungen (Tier 1-3) | Vertragliche Klauseln | SPA-Frist | Vertragslegal | Verweigerung oder Schweigen |
| Gesellschafterliste Paragraf 40 GmbHG | Paragraf 40 GmbHG | Unverzueglich nach Closing | Corporate-Lead | > 14 Tage nach Closing |

### C: Register-Monitoring (Laufend)

| Monitor | Quelle | Frequenz | Owner |
|---|---|---|---|
| Handelsregister Zielgesellschaft | www.handelsregister.de | Woechentlich | Corporate-Ass. |
| Bundesanzeiger Zielgesellschaft | Bundesanzeiger.de | Monatlich | Corporate-Ass. |
| DPMA IP-Register | dpma.de | Monatlich | IP-Counsel |

### D: Kapitalmarkt-Monitoring (bei boersennotierter Zielgesellschaft)

| Monitor | Norm | Eskalation |
|---|---|---|
| Ad-hoc-Mitteilungen Zielgesellschaft | Art. 17 MAR | Sofort — MAR-Freigabe erforderlich |
| Stimmrechtsmitteilungen | Paragraf 33 ff. WpHG | Bei Annaehern an 30 % WpUEG-Schwelle |
| Short-Selling-Positionen | EU-Leerverkaufs-VO | Bei ungewoehnlichem Anstieg |

## Schritt-für-Schritt-Workflow

1. **Deal-Phase und Monitoring-Bedarf erfassen:** Welche Workstreams laufen? Welche CPs sind offen? Deadline-Übersicht aus SPA erstellen.
2. **Owner-Matrix festlegen:** Für jeden Monitoring-Bereich einen verantwortlichen Owner (Person + Eskalation) benennen. Kein Monitor ohne Owner.
3. **Technische Quellen definieren:** VDR-API, RSS-Feeds Bundesanzeiger, Handelsregister-Benachrichtigungen aktivieren, MAR-Alert-System konfigurieren.
4. **Eskalationsregeln dokumentieren:** Schwellenwerte (Frist < 14 Tage, kritischer Datenraum-Zugang, MAR-Signal) mit Eskalationsstufe (Owner → Senior Partner → Mandant) verknuepfen.
5. **Stop-Schwellen benennen:** Insiderinformation erkannt → manueller Review vor jeder automatischen Ausgabe. Externer Datenzugriff unklar → Monitoring pausieren.
6. **Monitoring-Plan dokumentieren:** Monitoring-Automation-Plan (Template unten) erstellen und mit Deal-PMO verknuepfen.
7. **Woechentlicher Check:** CP-Status, offene Q&A, neue Registereintraege, MAR-Alerts in Deal-PMO-Wochenbericht einspeisen.

## Output-Template

**Adressat:** Deal-PMO / Senior Partner — Tonfall: sachlich-strukturiert, risikoorientiert

```
MONITORING-AUTOMATION-PLAN
Mandat: [MANDATSCODE]
Zielgesellschaft: [NAME]
Deal-Phase: [PRE-SIGNING / POST-SIGNING / PMI]
Erstellt: [TT.MM.JJJJ]
Owner Monitoring: [NAME]

> Vertraulich — Mandatsgeheimnis Paragraf 43a Abs. 2 BRAO.
> Insiderinformationen: Freigabe durch [COMPLIANCE-OFFICER] erforderlich.

--- AKTIVE MONITORE ---
| Monitor | Quelle | Frequenz | Owner | Letzter Check | Status |
|---|---|---|---|---|---|
| [MONITOR 1] | [QUELLE] | [FREQUENZ] | [PERSON] | [DATUM] | [OK / ALARM / OFFEN] |

--- OFFENE CP-DEADLINES ---
| CP | Norm | Frist | Status | Eskalation faellig ab |
|---|---|---|---|---|
| Fusionskontrolle | Paragraf 35 ff. GWB | [DATUM] | [OFFEN / EINGEREICHT / FREIGABE] | [DATUM] |
| FDI BMWK | Paragraf 55 ff. AWV | [DATUM] | [OFFEN / EINGEREICHT] | [DATUM] |

--- ALARME (Aktuelle Woche) ---
[KEIN ALARM]
oder:
ALARM: [BESCHREIBUNG] — Eskalation an: [PERSON] — Frist: [DATUM]

--- NAECHSTE SCHRITTE ---
1. [AKTION] — Owner: [PERSON] — Frist: [DATUM]
2. [AKTION] — Owner: [PERSON] — Frist: [DATUM]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Rote Schwellen

- **CP-Frist Fusionskontrolle < 7 Tage, kein Freigabestatus** — Vollzugsverbot Paragraf 41 GWB; Deal-Coordinator sofort informieren; Pre-Filing-Gespraeche initiieren.
- **MAR-Signal ohne manuellen Review** — automatische Aussenkommunikation verboten; alle MAR-relevanten Ausgaben manuell freigeben lassen.
- **Monitoring ohne Owner** — kein Monitor ohne benannte verantwortliche Person; ohne Owner-Matrix Monitoring-Plan zurueckhalten.
- **Vertrauliche Monitoring-Daten an unautorisierten Dritten** — Paragraf 43a Abs. 2 BRAO; sofortiger Stopp; Kanzlei-Compliance informieren.

## Arbeitsmodus

- Nur Vorschlaege für Automationen machen, keine vertraulichen Daten ungefragt beobachten.
- Monitoringziel, Frequenz, Quelle, Owner und Output definieren.
- Eskalationsregeln und Stoppschwellen festlegen.
- Automationsvorschlaege mit Deal-PMO verknuepfen.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, naechster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte mit verantwortlicher Person, Frist und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingaenge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurueckspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknuepfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams fuehren.

## Vorlagen

- assets/templates/monitoring-automation-plan.md
- assets/templates/deal-pmo-weekly.md

## Quellen und Vertiefung

- Art. 17 MAR (Ad-hoc-Publizitaet; Insider-Monitoring)
- Paragraf 35, 41 GWB (Fusionskontrolle; Vollzugsverbot)
- Paragraf 55 ff. AWV (FDI-Screening)
- Paragraf 40 GmbHG (Gesellschafterliste; Registerpublizitaet)
- Art. 28 DSGVO (Datenschutz bei Monitoring-Dienstleistern)
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.
- Mestmäcker/Veelken, in: Immenga/Mestmäcker, GWB, 6. Aufl. 2021, Paragraf 41 Rn. 1 ff.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Paragraf 705 ff. BGB (GbR)
- Paragraf 105 ff. HGB (OHG)
- Paragraf 161 ff. HGB (KG)
- Paragraf 13, 15 GmbHG (Anteilsübertragung)
- Paragraf 53 GmbHG (Satzungsänderung)
- Paragraf 33 GWB, FKVO 139/2004 (Fusionskontrolle)
- Paragraf 311 BGB i.V.m. Paragraf 433, 453 BGB (Unternehmenskauf, share/asset deal)
- Paragraf 25, 28 HGB (Firmenfortführung, Haftung)
- Paragraf 2-4 UmwG (Verschmelzung)
- Paragraf 1 InvKG, AWG/AWV Paragraf 55-62 (Investitionsprüfung)

### Leitentscheidungen

- BGH II ZR 17/19 (Earn-Out-Klauseln, Kontrolle)
- BGH II ZR 280/14 (Gewährleistungsausschluss share deal)
- BGH II ZR 109/13 (W&I-Versicherung, Sale and Purchase)
- EuGH C-93/13 P (FKVO-Verfahren)
- BGH II ZR 71/11 (Auskunftsrechte Datenraum)

### Anwendung im Skill

- Share Deal vs. Asset Deal Wahl an Steuer-, Haftungs- und Genehmigungsfolgen, nicht am LMA-Standard ausrichten.
- W&I-Versicherung nach BGH II ZR 109/13 ergaenzt, ersetzt aber keine Garantien.
- Fusionskontrolle Paragraf 39 GWB und FKVO 139/2004: Anmeldepflicht vor Closing prüfen, sonst Paragraf 41 GWB-Vollzugsverbot.

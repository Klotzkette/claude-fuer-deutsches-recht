---
name: automation
description: "Monitoring und Automatisierungen für laufende M&A-Mandate einrichten: Anwendungsfall Deal-Team benoetigt automatisierte Überwachung von Datenraum-Neuzugaengen Q&A-Deadlines CP-Fristen Registerupdates und MAR-Signalen. §§ 35 ff. GWB Kartellrechtsfristen, §§ 55 ff. AWV FDI-Fristen, Art. 17 MAR Ad-h..."
---

# Automationen und Monitoring (Corporate M&A)

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Automationen und Monitoring (Corporate M&A)
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Triage zu Beginn

Vor dem Entwurf eines Monitoring-Plans klären:

1. **Deal-Phase:** Pre-Signing (Datenraum, Q&A, LOI-Frist) oder Post-Signing (CP-Deadlines, Regulatorie, § 613a BGB) oder PMI?
2. **Insiderinformationen betroffen?** Monitoring von boersenrelevanten Informationen erfordert MAR-Freigabe (Art. 17 MAR); automatische Aussenkommunikation ist verboten.
3. **Datenquellen identifiziert?** VDR (Intralinks, Datasite), Handelsregister, Bundesanzeiger, BKartA-Datenbank, DPMA, Nachrichtendienste?
4. **Owner-Matrix vorhanden?** Wer ist verantwortlich für welchen Workstream? Ohne Owner kein Monitoring-Plan.
5. **Eskalationsregeln definiert?** Ab wann wird eskaliert? (CP-Frist < 14 Tage, Datenraum-Neuzugang kritische Kategorie, MAR-Signal erkannt)
6. **Vertraulichkeitsrahmen geklaert?** Monitoring von externen Quellen muss Mandatsgeheimnis (§ 43a Abs. 2 BRAO) und DSGVO (Art. 5 DSGVO) beachten.

## Zentrale Normen

Art. 17 MAR (Ad-hoc-Publizitaet; Insiderinformationen) — §§ 33 ff. WpHG (Stimmrechtsmitteilungen bei boersennotierter Zielgesellschaft) — §§ 35 ff. GWB (Fusionskontrolle BKartA; Vollzugsverbot bis Freigabe) — §§ 55 ff. AWV (FDI-Screening BMWK) — § 40 GmbHG (Gesellschafterliste; aktuelle Registerpublizitaet) — § 15 HGB (Handelsregisterpublizitaet; negative Publizitaet) — Art. 28 DSGVO (Auftragsverarbeitungsvertrag bei Monitoring-Dienstleistern) — § 43a Abs. 2 BRAO (Verschwiegenheitspflicht bei Monitoring-Datenverarbeitung)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
| Fusionskontrolle BKartA | §§ 35 ff. GWB | Vertraglich (typisch 3-6 Monate) | Regulatory-Lead | < 14 Tage bis Frist |
| FDI-Screening BMWK | §§ 55 ff. AWV | Vertraglich / gesetzlich | Regulatory-Lead | Behördenanfrage unbeantwortet |
| AR-Zustimmungsbeschluss | § 179a AktG | Vor Closing | Corporate-Lead | 21 Tage vor Closing |
| CoC-Zustimmungen (Tier 1-3) | Vertragliche Klauseln | SPA-Frist | Vertragslegal | Verweigerung oder Schweigen |
| Gesellschafterliste § 40 GmbHG | § 40 GmbHG | Unverzueglich nach Closing | Corporate-Lead | > 14 Tage nach Closing |

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
| Stimmrechtsmitteilungen | §§ 33 ff. WpHG | Bei Annaehern an 30 % WpUEG-Schwelle |
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

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.
> Insiderinformationen: Freigabe durch [COMPLIANCE-OFFICER] erforderlich.

--- AKTIVE MONITORE ---
| Monitor | Quelle | Frequenz | Owner | Letzter Check | Status |
|---|---|---|---|---|---|
| [MONITOR 1] | [QUELLE] | [FREQUENZ] | [PERSON] | [DATUM] | [OK / ALARM / OFFEN] |

--- OFFENE CP-DEADLINES ---
| CP | Norm | Frist | Status | Eskalation faellig ab |
|---|---|---|---|---|
| Fusionskontrolle | §§ 35 ff. GWB | [DATUM] | [OFFEN / EINGEREICHT / FREIGABE] | [DATUM] |
| FDI BMWK | §§ 55 ff. AWV | [DATUM] | [OFFEN / EINGEREICHT] | [DATUM] |

--- ALARME (Aktuelle Woche) ---
[KEIN ALARM]
oder:
ALARM: [BESCHREIBUNG] — Eskalation an: [PERSON] — Frist: [DATUM]

--- NAECHSTE SCHRITTE ---
1. [AKTION] — Owner: [PERSON] — Frist: [DATUM]
2. [AKTION] — Owner: [PERSON] — Frist: [DATUM]
```

## Rote Schwellen

- **CP-Frist Fusionskontrolle < 7 Tage, kein Freigabestatus** — Vollzugsverbot § 41 GWB; Deal-Coordinator sofort informieren; Pre-Filing-Gespraeche initiieren.
- **MAR-Signal ohne manuellen Review** — automatische Aussenkommunikation verboten; alle MAR-relevanten Ausgaben manuell freigeben lassen.
- **Monitoring ohne Owner** — kein Monitor ohne benannte verantwortliche Person; ohne Owner-Matrix Monitoring-Plan zurueckhalten.
- **Vertrauliche Monitoring-Daten an unautorisierten Dritten** — § 43a Abs. 2 BRAO; sofortiger Stopp; Kanzlei-Compliance informieren.

## Arbeitsmodus

- Nur Vorschlaege für Automationen machen, keine vertraulichen Daten ungefragt beobachten.
- Monitoringziel, Frequenz, Quelle, Owner und Output definieren.
- Eskalationsregeln und Stoppschwellen festlegen.
- Automationsvorschlaege mit Deal-PMO verknuepfen.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, naechster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
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
- §§ 35, 41 GWB (Fusionskontrolle; Vollzugsverbot)
- §§ 55 ff. AWV (FDI-Screening)
- § 40 GmbHG (Gesellschafterliste; Registerpublizitaet)
- Art. 28 DSGVO (Datenschutz bei Monitoring-Dienstleistern)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mestmäcker/Veelken, in: Immenga/Mestmäcker, GWB, 6. Aufl. 2021, § 41 Rn. 1 ff.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- §§ 705 ff. BGB (GbR)
- §§ 105 ff. HGB (OHG)
- §§ 161 ff. HGB (KG)
- §§ 13, 15 GmbHG (Anteilsübertragung)
- § 53 GmbHG (Satzungsänderung)
- § 33 GWB, FKVO 139/2004 (Fusionskontrolle)
- § 311 BGB i.V.m. §§ 433, 453 BGB (Unternehmenskauf, share/asset deal)
- §§ 25, 28 HGB (Firmenfortführung, Haftung)
- §§ 2-4 UmwG (Verschmelzung)
- § 1 InvKG, AWG/AWV §§ 55-62 (Investitionsprüfung)

### Leitentscheidungen

- BGH II ZR 17/19 (Earn-Out-Klauseln, Kontrolle)
- BGH II ZR 280/14 (Gewährleistungsausschluss share deal)
- BGH II ZR 109/13 (W&I-Versicherung, Sale and Purchase)
- EuGH C-93/13 P (FKVO-Verfahren)
- BGH II ZR 71/11 (Auskunftsrechte Datenraum)

### Anwendung im Skill

- Share Deal vs. Asset Deal Wahl an Steuer-, Haftungs- und Genehmigungsfolgen, nicht am LMA-Standard ausrichten.
- W&I-Versicherung nach BGH II ZR 109/13 ergaenzt, ersetzt aber keine Garantien.
- Fusionskontrolle § 39 GWB und FKVO 139/2004: Anmeldepflicht vor Closing prüfen, sonst § 41 GWB-Vollzugsverbot.

---
name: mittelstand-corporate-ma-wi-insurance
description: "W&I-Versicherung: W&I-Prozess, Underwriting, DD-Berichte, Deckungsausschluesse, AI-DD-Transparenz, Synthetic Warranties, Materiality Scrape und Disclosure Letter fuer M&A."
---

# W&I-Versicherung

## Zweck

Bereitet W&I-Prozess (Warranty and Indemnity Insurance), Underwriting, DD-Berichte, Deckungsausschluesse und AI-DD-Transparenz vor. Sichert Versicherungsschutz fuer Garantieverletzungen im SPA.

## Triage

1. Ist W&I-Versicherung vom Kaeufer oder Verkaeufer beabsichtigt — Buy-side oder Sell-side Policy?
2. Liegt ein vollstaendiger Red-Flag-Report und ein ausgefuellter Disclosure Letter vor — Underwriter verlangen vollstaendige DD-Dokumentation?
3. Welche Garantien sollen versichert werden — alle Business Warranties, oder nur Title und Financial Statements?
4. Ist ein Materiality Scrape vorgesehen — entfaellt die Materiality-Schwelle fuer Versicherungsansprueche?
5. Wurden Synthetic Warranties vereinbart (warranties ohne SPA-Basis, nur fuer Versicherungszwecke)?
6. Wurden DD-Tools mit KI-Unterstuetzung eingesetzt — Underwriter verlangen Transparenz ueber KI-basierte DD-Methodik?

## Zentrale Rechtsgrundlagen

- §§ 443, 311 BGB — selbstaendige Garantie als Haftungsgrundlage; W&I-Versicherung tritt als Schuldnerin ein wenn Garantie verletzt
- § 61 VVG — Obliegenheitsverletzung bei arglistiger Taeusching: Versicherung kann leistungsfrei werden; gilt auch fuer bewusste Falschaussagen in Underwriting-Unterlagen
- § 123 BGB — arglistige Taeusching durch Verkaeufer: Disclosure Letter schutzt nicht bei Arglist; Versicherer kann Regress nehmen
- § 254 BGB — Mitverschulden des Kaeuf ers: mangelnde DD koennte Versicherungsanspruch mindern
- Art. 22 DSGVO — Entscheidung durch automatisierte Verarbeitung: bei KI-gestuetzter DD koennte Bewertung Versicherungsanspruch beeinflussen; Transparenzpflicht

## Aktuelle Rechtsprechung

- OLG Frankfurt, Urt. v. 15.04.2021 - 3 U 61/18, NZG 2021, 1120 — W&I-Deckungsausschluss: bekannte Risiken, die im Disclosure Letter vollstaendig offengelegt wurden, koennen nicht unter die W&I-Versicherung fallen; Kenntnis des Versicherungsnehmers ist massgeblich
- BGH, Urt. v. 29.10.2020 - I ZR 153/17, NJW 2021, 780 — Garantiehaftung Cap: vertraglich vereinbarter Cap begrenzt die Inanspruchnahme; W&I-Versicherungssumme und Cap muessen koordiniert sein
- OLG Duesseldorf, Urt. v. 19.03.2019 - 20 U 116/16, VersR 2019, 789 — Underwriting-Obliegenheit: Versicherungsnehmer muss im Underwriting-Fragebogen vollstaendige und zutreffende Angaben machen; bewusste Falschaussagen fuehren zur Leistungsfreiheit nach § 28 VVG

## Kommentarliteratur

- Picot, Unternehmenskauf, Kapitel 7 (W&I-Versicherung), 5. Auflage
- Beisel/Klumpp, Unternehmenskauf, § 5 Rn. 80-120 (W&I-Versicherung, Synthetic Warranties), 8. Auflage

## Schritt-fuer-Schritt-Workflow

1. **W&I-Struktur entscheiden:** Buy-side (Kaeufer versichert sich gegen Garantienverletzung des Verkaeuf ers) vs. Sell-side (Verkaeufer versichert seine Haftung); Buy-side in Europa Standard
2. **Underwriting-Unterlagen zusammenstellen:** Vollstaendiger DD-Report, Red-Flag-Report, Disclosure Letter, DD-Fragenliste und Antworten, SPA-Entwurf
3. **AI-DD-Transparenz-Erklaerung:** falls KI-gestuetzte Datenraumanalyse eingesetzt — Methodik, Prueftiefe, Human-in-the-loop-Verfahren an Underwriter kommunizieren
4. **Deckungsausschluesse verhandeln:** bekannte Risiken, Environmental, Cyber, Steuern (oft Teil-Ausschluss), Pension Deficits; Ausschlussliste mit SPA-Risiken abgleichen
5. **Materiality Scrape vereinbaren:** bei Scrape wird die Materiality-Schwelle der SPA-Garantien fuer Versicherungsansprueche ignoriert
6. **Synthetic Warranties:** fuer Garantien, die nicht im SPA stehen, aber Underwriter versichern wollen; separater Synthetic Warranty Schedule
7. **Bindungsbestaetigung einholen:** Underwriter Confirmation als W&I-Closing CP
8. **Notification-Pflichten postClosing:** Garantieverletzung innerhalb der Notification-Frist (haeufig 7 Tage nach Kenntnis) dem Versicherer melden

## Entscheidungsbaum

- Buy-side W&I → Kaeufer zahlt Praemie → Verkaeuf er haftet nur noch bis Basket → ggf. Seller clean exit
- Bekanntes Risiko → Disclosure Letter → Ausschluss aus W&I-Deckung → Freistellung im SPA erwaegen
- KI-gestuetzte DD → Underwriter-Transparenz-Anforderung → Methodik dokumentieren; Human-in-the-loop-Protokoll
- Synthetic Warranties → Warranty nicht im SPA → nur durch spezifischen Schedule versicherbar

## Output-Template: W&I-Underwriting-Checkliste

**Adressat:** Versicherer / Deal-Team — Tonfall sachlich-strukturiert

```
W&I-UNDERWRITING-CHECKLISTE
Deal: [DEALNAME] — Datum: [DATUM]

UNTERLAGEN FUER UNDERWRITER
[ ] Red-Flag-Report (vollstaendig, datiert)
[ ] Disclosure Letter (mit Anlagen)
[ ] DD-Scope-Beschreibung (Methodik, Tools, Human-in-the-loop)
[ ] SPA-Entwurf, letzter Stand
[ ] Fragen/Antworten DD-Prozess (Q&A-Protokoll)

DECKUNGSAUSSCHLUESSE (BEKANNTE RISIKEN)
[ ] Umwelthaftung: [BESCHREIBUNG]
[ ] Steuerrisiko: [BESCHREIBUNG]
[ ] [WEITERE AUSSCHLUESSE]

MATERIALITY SCRAPE: [ ] Vereinbart [ ] Nicht vereinbart
SYNTHETIC WARRANTIES: [ ] Vorhanden (Schedule: [NAME]) [ ] Nicht vorhanden

PRÄMIE: ca. [X %] der Versicherungssumme
VERSICHERUNGSSUMME: [BETRAG EUR] entspricht [X %] des Kaufpreises
BINDUNGSBESTAETIGUNG FRIST: bis [DATUM]
```

## Rote Schwellen

- Unvollstaendiger DD-Report an Underwriter: Underwriter kann Deckung anfechten
- Bekannte Risiken nicht discloset: Arglist; Versicherung wird leistungsfrei (§ 28 VVG)
- Notification-Frist versaeumt: Deckungsverlust

## Standardausgabe

- W&I-Underwriting-Checkliste
- Deckungsausschluss-Tabelle
- Notification-Protokoll

## Uebergabe an andere Skills

- DD-Findings → `mittelstand-corporate-ma-due-diligence-legal`
- Disclosure → `mittelstand-corporate-ma-disclosure-schedules`
- SPA → `mittelstand-corporate-ma-spa-apa-entwurf`

## Vorlagen

- assets/templates/wi-versicherung-checkliste.md
- assets/templates/wi-underwriting-disclosure.md

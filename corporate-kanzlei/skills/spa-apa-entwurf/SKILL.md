---
name: spa-apa-entwurf
description: "SPA (Share Purchase Agreement) oder APA (Asset Purchase Agreement) entwerfen und strukturieren aus Term Sheet und DD-Findings. Normen: §§ 433 ff. BGB (Kaufrecht), § 444 BGB (Gewaehrleistung), §§ 311 Abs. 2 und 280 BGB. Prüfraster: Kaufpreismechanik (Locked Box vs. Closing Accounts), MAC-Klausel,..."
---

# SPA/APA-Entwurf

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Triage — klaere vor Entwurfsbeginn

1. Share Deal oder Asset Deal? (Steuerfolgen, Haftungsuebergang, Vertragsuebergang)
2. Kaufpreismechanik: Locked Box oder Closing Accounts? (Stichtag, Leakage-Definition)
3. Gibt es DD-Findings, die spezifische Garantieeinschraenkungen erfordern?
4. W&I-Versicherung geplant? (Beeinflusst Garantiemechanik, De-Minimis, Cap)
5. Earn-Out-Komponente? (Zahlungsstruktur, Milestones, Anti-Sandbagging)
6. Jurisdiktion und anwendbares Recht — deutsches Recht, englisches Recht, hybrid?
7. Verkauf von/an Private Equity oder strategischen Kaeufer?
8. Notar erforderlich? (§ 15 GmbHG bei GmbH-Anteilen immer; AktG bei AG Depot/Legitimationsabtretung)

## Zentrale Anspruchsgrundlagen & Normen

- **§ 433 ff. BGB** — Kaufvertrag; Mietvertrag-, Aufhebungs-, Abtretungsregeln
- **§ 453 BGB** — Rechtskauf, Anteilskauf
- **§ 444 BGB** — Arglistiges Verschweigen; keine vertragliche Haftungsfreizeichnung möglich
- **§ 15 GmbHG** — Abtretung von GmbH-Anteilen; Notarpflicht
- **§ 929 ff. BGB** — Eigentumsuebergang Asset Deal
- **§ 613a BGB** — Betriebsuebergang; Arbeitnehmeruebergang Asset Deal
- **§§ 306 ff. BGB** — AGB-Kontrolle bei standardisierten Vertragsklauseln
- **§§ 241 II, 311 II BGB** — Culpa in contrahendo; Informationspflichten pre-Signing
- **§ 123 BGB** — Anfechtung wegen arglistiger Taeuschung
- **§ 439 ff. BGB** — Nacherfuellung; Ruecktritt; Schadensersatz (wenn keine individuelle Regelung)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Praxiswissen: Kaufpreismechanik

### Locked Box
- Stichtag: Bilanzdatum (meist letzter Jahresabschluss)
- Leakage-Definition: Dividenden, Management Fees, unerlaubte Vermögensverlagerungen
- Permitted Leakage: normal course payments, Geschäftsführergehalt
- Vorteile: Preissicherheit, kein Closing Accounts-Streit
- Risiko: Seller traegt kein Upside; Kaeufer muss Leakage-Periode ueberwachen

### Closing Accounts
- Bilanzstichtag: Closing-Datum; Erstellung innerhalb 60-90 Tage
- Adjust-Mechanismus: Net Debt, Working Capital, Cash
- Streitpotenzial: Accounting-Wahlrechte, Bewertungsunterschiede
- Schiedsverfahren (Wirtschaftspruefer als Expert) als Eskalation

## Reps & Warranties — Standardkatalog

| Kategorie | Kerngarantien | Typische Einschraenkung |
|---|---|---|
| Corporate | Gruendung, Anteilsstruktur, Satzung, Vollmachten | Disclosure Letter |
| Financial | Jahresabschluss ordnungsgemaess, kein Material Adverse Change | Wesentlichkeitsschwelle |
| Business | Verträge, IP, Kunden, Lizenzen, Behördenerlaubnisse | Knowledge qualifier |
| Employment | Arbeitsvertraege, BR, Pensionen, Change-of-Control | Kollektivarbeitsrecht |
| Tax | Steuern vollstaendig bezahlt, keine offenen Betriebspruefungen | Tax Disclosure |
| Legal | Keine wesentlichen Rechtsstreitigkeiten | Pending/Threatened |
| Compliance | AML/GwG, Sanktionen, Kartellrecht, ESG-Kriterien | Best Knowledge |

## Indemnification vs. Warranty-Breach

- **Indemnity (Freistellung):** Dollar-for-dollar, unabhaengig von Kausalitaet; für bekannte Risiken (steuerliche Nachzahlungen, Altlasten, Prozessrisiken)
- **Warranty Breach:** Schadensersatz nach § 311 I BGB oder vertragl. Schadensliquidation; Kaeufer muss Schaden an Unternehmenswert nachweisen
- **Anti-Sandbagging:** Seller haftet auch bei Kaeufer-Kenntnis, wenn vertraglich so vereinbart; ohne Klausel ggf. § 442 BGB

## Schritt-für-Schritt-Workflow

1. **Term Sheet analysieren** — Kaufpreis, Struktur, Closing Conditions, Exklusivitaet
2. **DD-Findings mapping** — jedes Material Finding einem Vertragsmechanismus zuordnen (Garantie, Indemnity, Kosten-Anpassung, Deal-Breaker)
3. **Strukturentscheidung** — Share Deal/Asset Deal; Locked Box/Closing Accounts; W&I ja/nein
4. **Vertragsgeruest aufbauen** — Definitionen, Kaufpreis, Closing Conditions, Representations, Warranties, Covenants, Indemnities, Haftungslimite, Governing Law, Dispute Resolution
5. **Key Issues Memo** — offene Business- und Rechtsentscheidungen mit Optionen und Empfehlung
6. **Verhandlungsrunden** — Markup-Schleife; Leadsatz beachten; Disclosure Schedule parallel fuellen
7. **Signing-Vorbereitung** — Execution Version, Anlagen, Disclosure Letter, W&I-Deckungsbestaetigung
8. **Closing Mechanics** — Conditions Precedent-Checkliste, CP-Satisfaction-Protokoll, Kaufpreiszahlung, Anteilsuebertragung (Notar)

## Entscheidungsbaum: Notar erforderlich?

```
Gegenstand: GmbH-Anteile?
 → Ja: Notarielle Beurkundung zwingend (§ 15 III GmbHG)
 → Vorkaufsrecht der Mitgesellschafter? → ja: Angebotsverfahren beachten
 → Nein: AG-Aktien?
 → vinkulierte Namensaktien: Zustimmungsvorbehalt pruefen (§ 68 II AktG)
 → Inhaberaktien: kein Notar noetig; Depot-Uebertragung
 → Asset Deal: kein Notar für Vertragstext, aber Grundstuecke -> notarielle Auflassung (§ 925 BGB)
```

## Output-Template Key Issues Memo

**Adressat:** Mandant / Deal-Team — Tonfall sachlich-juristisch, entscheidungsorientiert

```
KEY ISSUES MEMO
Transaktion: [DEAL-NAME]
Stand: [DATUM]
Version: [Nr.]
Erstellt von: [NAME, FUNKTION]

1. OFFENE BUSINESS-ENTSCHEIDUNGEN
 | Nr. | Thema | Option A | Option B | Empfehlung |
 |----|-------|----------|----------|-----------|
 | 1 | Kaufpreismechanik | Locked Box | Closing Accounts | [Empfehlung] |
 | 2 | W&I-Versicherung | Ja (Kaeufer-Policy) | Nein | [Empfehlung] |

2. DD-FINDING-MATRIX
 | Finding | Vertragsmechanismus | Owner | Status |
 |---------|---------------------|-------|--------|
 | [Finding 1] | Spezifische Indemnity | [Partei] | Offen/Geschlossen |

3. HAFTUNGSREGIME
 - De-Minimis: [Betrag EUR]
 - Basket (Tipping/Deductible): [Betrag EUR]
 - Cap: [% des Kaufpreises]
 - Verjährung: [allg. 18-24 Monate; Tax 5-7 Jahre; Titel unbegrenzt]

4. CLOSING CONDITIONS
 - Kartellrecht: [Anmeldung bei / Freigabe bis]
 - Aussenhandel/FDI: [AWG/ATSG/SektSchV-Pruefung]
 - Dritte Zustimmungen: [Change-of-Control-Klauseln]

5. NAECHSTE SCHRITTE
 | Schritt | Owner | Frist |
 |---------|-------|-------|
 | [Massnahme 1] | [Name] | [Datum] |
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Output-Template SPA-Struktur (Outline)

```
SHARE PURCHASE AGREEMENT — INHALTSVERZEICHNIS
Parteien: [VERKAEUFER], [KAEUFER], [ZIELGESELLSCHAFT]
Datum: [DATUM]

1. Definitionen und Auslegung
2. Kauf und Verkauf der Anteile
 2.1 Kaufgegenstand
 2.2 Kaufpreis und Kaufpreismechanik (Locked Box / Closing Accounts)
 2.3 Kaufpreisanpassung
3. Vollzugsbedingungen (Closing Conditions / Conditions Precedent)
 3.1 Kartellfreigabe [§§ 35 ff. GWB / EU-Fusionskontrolle]
 3.2 [Weitere CPs]
4. Vollzug (Closing)
 4.1 Closing-Datum
 4.2 Vollzugshandlungen (Deliverables)
5. Representations and Warranties des Verkaefers
 5.1 Corporate/Title
 5.2 Financial Statements
 5.3 [...]
6. Representations and Warranties des Kaeufers
7. Covenants pre-Closing (Interim Operating Covenants)
8. Covenants post-Closing
9. Haftung und Rechtsfolgen von Warranty-Verletzungen
 9.1 Haftungslimite (De-Minimis, Basket, Cap)
 9.2 Verjährung
 9.3 Anti-Sandbagging
10. Specific Indemnities (Freistellungen)
11. MAC-Klausel / Material Adverse Change
12. Ruecktrittsrechte
13. Vertraulichkeit / Oeffentlichkeitsarbeit
14. Geheimhaltung / NDA-Integration
15. Sonstiges (Kosten, Notifikationen, Schiedsklausel)
16. Anwendbares Recht / Gerichtsstand
Anlagen: Disclosure Letter, Locked-Box-Bilanz, CP-Liste, W&I-Term Sheet
```

## Rote Schwellen

- Kaufpreismechanik nicht abgestimmt → Streit über Earn-Out oder Working Capital obligatorisch
- DD-Finding ohne vertragliche Reaktion → Indemnity-Luecke; kein Seller-Schutz und kein Kaeufer-Schutz
- MAC-Klausel fehlt → keine Ruecktrittsoption bei wesentlicher Verschlechterung vor Closing
- Notarpflicht (§ 15 GmbHG) uebersehen → formnichtige Anteilsuebertragung
- W&I-Policy-Bedingungen nicht mit Vertragsklauseln abgestimmt → Deckungsluecken

## Vertiefung

### MAC-Klausel — Abgrenzung Material/Nicht-Material

Die MAC-Klausel ist das wichtigste Ruecktrittsvehikel. Kernanforderung: Die Verschlechterung muss (a) wesentlich, (b) dauerhaft und (c) auf die Zielgesellschaft bezogen sein. Allgemeine Markt- oder Branchenrisiken (Systemkrise, Pandemie als solche) sind typischerweise ausgegrenzt — ausser der Zielgesellschaft trifft es ueberproportional.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Earn-Out — Praxisrisiken

Earn-Out-Klauseln sind streitanfaellig. Kaeufer-Risiken: Manipulation durch Accounting-Wahlrechte, Senkung des EBITDA durch konzerninterne Umlagen. Verkaeufer-Risiken: Kaeufer ändert Geschäftsstrategie, was Milestones unmoeglich macht.

Best Practice: (a) Accounting-Methodology einfrieren; (b) Nicht-Beeintrachtigungs-Covenant ("Non-Frustration"); (c) klare Earn-Out-Statementerstellung mit Schiedsklausel; (d) OLG Frankfurt-Rspr. beachten: Kaeufer hat aktive Foerderpflicht.

## Quellen

- § 433 BGB: https://www.gesetze-im-internet.de/bgb/__433.html
- § 453 BGB (Rechtskauf/Anteilskauf): https://www.gesetze-im-internet.de/bgb/__453.html
- § 444 BGB (Arglist): https://www.gesetze-im-internet.de/bgb/__444.html
- § 613a BGB (Betriebsuebergang Asset Deal): https://www.gesetze-im-internet.de/bgb/__613a.html
- § 15 GmbHG (Abtretung GmbH-Anteile, Notarpflicht): https://www.gesetze-im-internet.de/gmbhg/__15.html
- § 68 AktG (Vinkulierung Namensaktien): https://www.gesetze-im-internet.de/aktg/__68.html
- §§ 35 ff. GWB (Fusionskontrolle Bundeskartellamt): https://www.gesetze-im-internet.de/gwb/__35.html
- FKVO (VO (EG) Nr. 139/2004 EU-Fusionskontrolle): https://eur-lex.europa.eu/eli/reg/2004/139
- AWG §§ 4-6, AWV §§ 55 ff. (Investitionspruefung): https://www.gesetze-im-internet.de/awv_2013/
- EU FSR (VO 2022/2560; M&A-Notifizierungspflicht ab 12.10.2023): https://eur-lex.europa.eu/eli/reg/2022/2560
- MoPeG (in Kraft 01.01.2024) — Asset/Share Deal bei Personengesellschaften, neue eGbR-Eintragung: https://www.gesetze-im-internet.de/bgb/__705.html
- Rechtsprechung im Uebrigen: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

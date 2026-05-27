---
name: stb-erechnung-pflicht-b2b-2025-2026
description: "eRechnung-Pflicht B2B seit 01.01.2025 § 14 UStG ViDA. Anwendungsfall Pruefung Mandantenbetrieb eRechnungs-Empfang Versand Uebergangsfristen PDF reicht nicht mehr. Methodik Format XRechnung ZUGFeRD. Output eRechnungs-Konfiguration."
---

# eRechnung-Pflicht B2B seit 01.01.2025

## Kernsachverhalt

Seit 01.01.2025 sind alle inlaendischen B2B-Unternehmer verpflichtet, **eRechnungen empfangen zu koennen** (§ 14 Abs. 1 i.V.m. Abs. 2 UStG n.F., Wachstumschancengesetz vom 27.03.2024, BMF-Schreiben vom 15.10.2024). Die **Versandpflicht** ist demgegenueber gestaffelt: Bis 31.12.2026 duerfen Rechnungen weiterhin als PDF/sonstige elektronische Form mit Empfaengerzustimmung versendet werden; bis 31.12.2027 bleibt dies fuer Kleinunternehmen mit Vorjahresumsatz bis 800.000 EUR moeglich. Ab 01.01.2028 ist der eRechnungs-Versand zwischen inlaendischen Unternehmern verbindlich. Akzeptierte Formate: XRechnung (CIUS-konform, reines XML) und ZUGFeRD ab Version 2.0.1 (Hybridformat). Der Steuerberater muss Mandanten ueber die Pflicht informieren und insbesondere die Empfangsbereitschaft sicherstellen.

## Kaltstart-Rueckfragen

1. Welche Umsatzgroesse hat der Mandant (Uebergangsfristen)?
2. Welche Kunden — B2B (eRechnung-pflichtig) oder B2C (PDF weiterhin moeglich)?
3. Welche Lieferanten senden bereits eRechnungen?
4. Welche ERP/Faktura-Software wird genutzt?
5. Welche Empfangs-Adresse (Mail-Postfach oder Peppol)?
6. Welche Archivierung GoBD-konform?
7. Welche Format-Praeferenz XRechnung vs. ZUGFeRD?
8. Welche Mandanten-Beratungsbedarf?

## Rechtlicher Rahmen

### Primaernormen

**§ 14 Abs. 1 S. 3 UStG n.F.** — Definition eRechnung als strukturiertes elektronisches Format gemaess EN-16931.

**§ 14 Abs. 2 UStG n.F.** — Ausstellungspflicht in eRechnungsform zwischen inlaendischen Unternehmern (mit Uebergangsregeln § 27 Abs. 38 UStG).

**§ 27 Abs. 38 UStG n.F.** — Uebergangsregeln (sonstige Rechnungsform bis 31.12.2026 / 31.12.2027 fuer Kleinunternehmer mit Umsatz <= 800.000 EUR).

**§ 33 UStDV, § 34 UStDV** — Ausnahmen (Kleinbetrag, Fahrausweis).

**Wachstumschancengesetz vom 27.03.2024** — BGBl. I 2024 Nr. 108.

**EU-RL 2014/55/EU** — eRechnungs-Standard EN-16931.

### Verwaltungsanweisungen

- BMF v. 15.10.2024 zur eRechnung-Pflicht.
- BMF v. 22.06.2023 ViDA.

## Workflow

### Phase 1 — Geltungsbereich (Wachstumschancengesetz 2024)

| Phase | Zeitraum | Pflicht |
|---|---|---|
| Empfang | Ab 01.01.2025 | Alle inlaendischen B2B-Unternehmer (zwingende Empfangsbereitschaft, ohne Schwellenwert) |
| Versand sonstige elektr. Rechnungen | 01.01.2025 - 31.12.2026 | Versand als PDF / sonstige elektronische Form weiter zulaessig, sofern Empfaengerzustimmung |
| Versand sonstige elektr. Rechnungen, Kleinunternehmer | 01.01.2025 - 31.12.2027 | Verlaengert fuer Rechnungsausstellung durch Unternehmer mit Vorjahresumsatz <= 800.000 EUR |
| eRechnung-Versand vollumfaenglich | Ab 01.01.2028 | Verbindlich; PDF/Papier zwischen inlaendischen Unternehmern nicht mehr ausreichend |
| Ausgenommen | dauerhaft | Kleinbetragsrechnungen § 33 UStDV (bis 250 EUR), Fahrausweise § 34 UStDV, B2C-Rechnungen |

Stand BMF-Schreiben vom 15.10.2024; Aktualisierungen 2026 ueber bzst.de bzw. BMF-Newsletter verifizieren.

### Phase 2 — Format-Wahl

| Format | Eigenschaften |
|---|---|
| XRechnung | Reines XML nach CIUS der KoSIT; Standard fuer oeffentliche Auftraggeber (E-Rech-VO Bund seit 27.11.2020) |
| ZUGFeRD ab Version 2.0.1 | Hybridformat PDF/A-3 mit eingebettetem XML; menschen- und maschinenlesbar; ab Profil EN-16931 eRechnung-konform |
| Sonstige (z.B. EDIFACT) | Nur zulaessig, wenn EN-16931-konforme strukturierte Rechnungsdaten enthalten / extrahierbar sind |

Hinweis: Das ZUGFeRD-Profil MINIMUM und BASIC-WL sind **nicht** eRechnung-konform i.S.d. § 14 Abs. 1 S. 6 UStG.

### Phase 3 — Empfangs-Setup

- Mailpostfach fuer eRechnung definieren.
- Peppol-Anschluss (selten in DACH; wachsend).
- DATEV Empfang ueber DUO oder externes Tool (z.B. Inposia, Coupa).

### Phase 4 — Versand-Setup

- Faktura-Software mit eRechnungs-Ausgabe in XRechnung (XML) und/oder ZUGFeRD (PDF/A-3 + XML).
- Datenmapping: Konten- und Stammdaten zu den Pflichtfeldern nach EN-16931 (BT-Felder); insbesondere Leitweg-ID bei B2G-Rechnungen.
- Test-Rechnungen mit Lieferanten / Kunden vor Echtbetrieb (Validierung ueber KoSIT-Validator fuer XRechnung).

### Phase 5 — Archivierung

- GoBD-konforme Archivierung im Originalformat XML.
- 10 Jahre Aufbewahrung.
- Lesbarkeitserhaltung.

### Phase 6 — Mandanten-Information

Mustertext fuer den Mandantenrundbrief (anzupassen an Mandantenstruktur):

```
Sehr geehrte Damen und Herren,

seit dem 01.01.2025 sind alle inlaendischen B2B-Unternehmer verpflichtet,
eRechnungen empfangen zu koennen (§ 14 UStG i.V.m. Wachstumschancengesetz).
Eine reine PDF-Rechnung erfuellt nicht mehr die Anforderungen an eine eRechnung;
ein Vorsteuerabzug kann gefaehrdet sein.

Wir bitten Sie, folgende Schritte zu pruefen:
1. Empfangs-E-Mail-Adresse fuer eRechnungen festlegen
   (z.B. rechnungen@ihre-firma.de) und Lieferanten mitteilen.
2. Buchhaltungssoftware auf eRechnungs-Empfang konfigurieren
   (XRechnung XML / ZUGFeRD ab Profil EN-16931).
3. GoBD-konforme Archivierung im Originalformat XML sicherstellen.
4. Bis 31.12.2026 (bzw. 31.12.2027 fuer Mandanten mit Umsatz <= 800.000 EUR)
   kann der Versand weiterhin als PDF mit Empfaengerzustimmung erfolgen;
   ab 01.01.2028 ist der eRechnungs-Versand zwingend.

Fuer die Einrichtung des Empfangs- und Versand-Workflows beraten wir Sie gerne.

Mit freundlichen Gruessen
[StB-Kanzlei]
```

- Konfigurationsberatung als separater Auftrag nach § 13 StBVV (Beratungstaetigkeit) oder Pauschalvereinbarung nach § 14 StBVV.
- Bei kleineren Mandanten Software-Empfehlung (z.B. DATEV Unternehmen Online, ZUGFeRD-faehige Faktura-Loesungen).

## Output

- Konfiguration Empfang/Versand eRechnung.
- Archivierungs-Routine.
- Mandanten-Information.

## Strategie und Praxis-Tipps

- Die wichtigste Stufe ist seit 01.01.2025 die **Empfangsbereitschaft** — ohne sie kann ein eRechnungs-pflichtiger Lieferant nicht ordnungsgemaess abrechnen, der Mandant verliert ggf. den Vorsteuerabzug.
- Mindest-Empfangsweg ist ein E-Mail-Postfach, das XML-/PDF-Anhaenge bis ueblicher Groesse annimmt; ein dediziertes eRechnungs-Postfach erleichtert Workflow und GoBD-Archivierung.
- ZUGFeRD eignet sich als Einstiegsformat fuer Mittelstand und Kleinunternehmer (PDF bleibt fuer den Anwender lesbar). XRechnung ist Pflichtformat im B2G-Verkehr mit Bundesstellen (E-Rech-VO seit 27.11.2020) und in einigen Laendern.
- DATEV-Hinweis: In DATEV Unternehmen Online laesst sich der eRechnungs-Empfang ueber das Postfach "Eingangsrechnungen" und das ZUGFeRD-Auswertungsmodul konfigurieren; konkrete Programmpfade in der aktuellen DATEV-Programmversion verifizieren.
- StBVV: Konfigurationsberatung als Beratungsleistung gem. § 21 StBVV oder Pauschalvereinbarung gem. § 14 StBVV (Mandanten frueh per Rundschreiben informieren — Mustertext im Skill `stb-mandantenanfrage-reaktion-frist-laufend`).

## Querverweise

- `stb-belegtransfer-datev-unternehmen-online` — Belegtransfer.
- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe.

## Quellen und Updates

Stand: 05/2026.

- UStG §§ 14, 27 Abs. 38; UStDV §§ 33, 34.
- Wachstumschancengesetz vom 27.03.2024 (BGBl. I 2024 Nr. 108).
- BMF-Schreiben vom 15.10.2024, IV D 2 - S 7287-a/23/10001 :007.
- EU-RL 2014/55/EU; Norm EN-16931.
- KoSIT XRechnung-Spezifikation (aktuelle Version verifizieren).
- ZUGFeRD-Spezifikation (FeRD), aktuelle Profile pruefen.
- ViDA (VAT in the Digital Age, COM 2022/701-703) — EU-Reformpaket, Inkrafttreten und Detailregelungen verifizieren.
- Verifikations-Hinweis: alle Werte und Fristen jaehrlich gegen BMF-Newsletter / bzst.de pruefen.

---
name: addison-bwa-konfiguration-tipps
description: "Für Addison BWA-Konfiguration: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Addison BWA-Konfiguration

## Fachlicher Anker

- **Normen:** § 6a, § 146 AO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Addison (Wolters Kluwer) ist die zweitstaerkste StB-Kanzleisoftware in Deutschland. Funktionen vergleichbar mit DATEV: Buchfuehrung, BWA, Lohn, Jahresabschluss. Andere Bedienlogik und andere Standardforms. Steuerberater, die mit Addison arbeiten, brauchen äquivalente Praxis-Tipps.

## Kaltstart-Rueckfragen

1. Welche Addison-Version (jaehrliche Updates)?
2. Welche Module (Finanzbuchhaltung, Lohn, Jahresabschluss)?
3. Welche Standard-Form für Mandanten?
4. Welche Branchen-Konfiguration?
5. Welche individuellen Anpassungen?
6. Welche Schnittstellen aktiv (eRechnung, Bank)?
7. Welche Berater-Sicht-Konfiguration?
8. Welche Schulungsstand der Sachbearbeiter?

## Workflow

### Phase 1 — Standardformen

| Addison-Bezeichnung | DATEV-Äquivalent | Verwendung |
|---|---|---|
| Standard-BWA / Kurz-BWA | DATEV BWA 01 | Standard 90 % der Mandate |
| Bewegungs-BWA | DATEV BWA 11 | Detaillierter Vormonatsvergleich |
| Branchen-BWA | DATEV BWA 21 | Mit Branchenkennzahlen |
| Liquiditaets-BWA | DATEV BWA 41 | Cashflow-orientiert |
| Kostenstellen-BWA | DATEV BWA 31 | Bei Kostenstellenrechnung |

Hinweis: konkrete Form-Nummern und Bezeichnungen variieren mit der Addison-Version; aktuellen Stand in der Programmdokumentation prüfen.

### Phase 2 — Konten-Konfiguration

- Kontenrahmen SKR 03 / SKR 04 wie in DATEV; alternativ branchenspezifische Rahmen (z.B. SKR 14 Landwirtschaft, IKR für Industrieunternehmen).
- BWA-Konten-Zuordnung über Berater-Stammdaten (typischer Pfad `Stammdaten → BWA-Konfiguration → Konten-Zuordnung`; konkreter Menue-Pfad variiert je Addison-Version — im Zweifelsfall in der Programm-Onlinehilfe unter "BWA-Konfiguration" nachschlagen).
- Bei individuellen Konten manuelle Zuordnung zur BWA-Zeile vor erstem Lauf.

### Phase 3 — Periodenvergleich

- Vorjahresdaten werden bei vorhandener Buchhaltungs-Historie automatisch herangezogen.
- Planwerte über das Plan-Erfassungs-Modul (jaehrlich/monatlich) erfassen; Plan-Ist-Vergleich in der BWA aktivieren.
- Mehrjahresvergleich bis 5 Jahre zurueck möglich.

### Phase 4 — Branchenvergleich

- Wolters Kluwer Branchenberichte als Alternative zu DATEV BBE-Branchenberichten.
- Branchenschluessel (WZ-Code) im Mandantenstamm hinterlegen.
- Aktualitaet der Branchendaten prüfen — typischerweise jaehrliche Aktualisierung.

### Phase 5 — Ausgabe

- PDF-Export mit Mandanten-Briefkopf.
- Excel-Export für Detailauswertung (Pivot-tauglich).
- Mandantenportal "Wolters Kluwer Mandanten-Cockpit" als Pendant zu DATEV Unternehmen Online.

### Phase 6 — Updates

- Jaehrliche Programm-Updates zum 1. Januar (Lohnsteuer-, SV-Tabellen, USt-Änderungen, AfA-Tabellen).
- Bei groesseren Reformen unterjaehrige Updates (z.B. Wachstumschancengesetz, eRechnung).
- Update-Pflicht aus § 146 AO (Programm muss aktuelle Tabellen abbilden).

## Strategie und Praxis-Tipps

- Addison-Schulungen über Wolters Kluwer Akademie.
- Wechsel von DATEV zu Addison oder umgekehrt sorgfaeltig planen — Mandantenmigration aufwendig.
- Hybrid-Modelle (z.B. Lohn Addison, Buchhaltung DATEV) sind selten und teuer.

## Quellen und Updates

Stand: 05/2026.

- Wolters Kluwer Addison Programm- und Bedienungsdokumentation (aktuelle Version prüfen).
- Wolters Kluwer Branchenberichte als Vergleichsdatenbank.
- Verifikations-Hinweis: konkrete Programmpfade und Form-Nummern ggf. abweichend in aktueller Addison-Version.

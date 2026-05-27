---
name: stb-addison-bwa-konfiguration-tipps
description: "Addison BWA-Konfiguration. Anwendungsfall Kanzleien mit Wolters Kluwer Addison statt DATEV. Methodik Unterschiede zu DATEV Konten-Konfiguration Branchenanpassung. Output BWA in Addison."
---

# Addison BWA-Konfiguration

## Kernsachverhalt

Addison (Wolters Kluwer) ist die zweitstaerkste StB-Kanzleisoftware in Deutschland. Funktionen vergleichbar mit DATEV: Buchfuehrung, BWA, Lohn, Jahresabschluss. Andere Bedienlogik und andere Standardforms. Steuerberater, die mit Addison arbeiten, brauchen aequivalente Praxis-Tipps.

## Kaltstart-Rueckfragen

1. Welche Addison-Version (jaehrliche Updates)?
2. Welche Module (Finanzbuchhaltung, Lohn, Jahresabschluss)?
3. Welche Standard-Form fuer Mandanten?
4. Welche Branchen-Konfiguration?
5. Welche individuellen Anpassungen?
6. Welche Schnittstellen aktiv (eRechnung, Bank)?
7. Welche Berater-Sicht-Konfiguration?
8. Welche Schulungsstand der Sachbearbeiter?

## Workflow

### Phase 1 — Standardformen

| Addison-Bezeichnung | DATEV-Aequivalent | Verwendung |
|---|---|---|
| Standard-BWA / Kurz-BWA | DATEV BWA 01 | Standard 90 % der Mandate |
| Bewegungs-BWA | DATEV BWA 11 | Detaillierter Vormonatsvergleich |
| Branchen-BWA | DATEV BWA 21 | Mit Branchenkennzahlen |
| Liquiditaets-BWA | DATEV BWA 41 | Cashflow-orientiert |
| Kostenstellen-BWA | DATEV BWA 31 | Bei Kostenstellenrechnung |

Hinweis: konkrete Form-Nummern und Bezeichnungen variieren mit der Addison-Version; aktuellen Stand in der Programmdokumentation pruefen.

### Phase 2 — Konten-Konfiguration

- Kontenrahmen SKR 03 / SKR 04 wie in DATEV; alternativ branchenspezifische Rahmen (z.B. SKR 14 Landwirtschaft, IKR fuer Industrieunternehmen).
- BWA-Konten-Zuordnung ueber Berater-Stammdaten (typischer Pfad `Stammdaten → BWA-Konfiguration → Konten-Zuordnung`; exakter Menue-Pfad in aktueller Programmversion verifizieren).
- Bei individuellen Konten manuelle Zuordnung zur BWA-Zeile vor erstem Lauf.

### Phase 3 — Periodenvergleich

- Vorjahresdaten werden bei vorhandener Buchhaltungs-Historie automatisch herangezogen.
- Planwerte ueber das Plan-Erfassungs-Modul (jaehrlich/monatlich) erfassen; Plan-Ist-Vergleich in der BWA aktivieren.
- Mehrjahresvergleich bis 5 Jahre zurueck moeglich.

### Phase 4 — Branchenvergleich

- Wolters Kluwer Branchenberichte als Alternative zu DATEV BBE-Branchenberichten.
- Branchenschluessel (WZ-Code) im Mandantenstamm hinterlegen.
- Aktualitaet der Branchendaten pruefen — typischerweise jaehrliche Aktualisierung.

### Phase 5 — Ausgabe

- PDF-Export mit Mandanten-Briefkopf.
- Excel-Export fuer Detailauswertung (Pivot-tauglich).
- Mandantenportal "Wolters Kluwer Mandanten-Cockpit" als Pendant zu DATEV Unternehmen Online.

### Phase 6 — Updates

- Jaehrliche Programm-Updates zum 1. Januar (Lohnsteuer-, SV-Tabellen, USt-Aenderungen, AfA-Tabellen).
- Bei groesseren Reformen unterjaehrige Updates (z.B. Wachstumschancengesetz, eRechnung).
- Update-Pflicht aus § 146 AO (Programm muss aktuelle Tabellen abbilden).

## Output

- Konfigurierte Addison-BWA.

## Strategie und Praxis-Tipps

- Addison-Schulungen ueber Wolters Kluwer Akademie.
- Wechsel von DATEV zu Addison oder umgekehrt sorgfaeltig planen — Mandantenmigration aufwendig.
- Hybrid-Modelle (z.B. Lohn Addison, Buchhaltung DATEV) sind selten und teuer.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA.
- `stb-datev-bwa-modul-bedienen-tipps` — DATEV Pendant.
- `stb-sage-buchhalter-bwa-konfiguration` — Sage.

## Quellen und Updates

Stand: 05/2026.

- Wolters Kluwer Addison Programm- und Bedienungsdokumentation (aktuelle Version pruefen).
- Wolters Kluwer Branchenberichte als Vergleichsdatenbank.
- Verifikations-Hinweis: konkrete Programmpfade und Form-Nummern ggf. abweichend in aktueller Addison-Version.

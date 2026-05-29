---
name: mittelstand-corporate-ma-kg-personengesellschaften
description: "KG und Personengesellschaften: KG, GmbH und Co. KG, Fondsvehikel, Kommanditistenwechsel, Einlagen, Haftsumme, Register; §§ 161-177 HGB, MoPeG, BGH-Rechtsprechung."
---

# KG und Personengesellschaften

## Zweck

Spezialworkflow fuer KG, GmbH & Co. KG, Fondsvehikel, Kommanditistenwechsel, Einlagen, Haftsumme und Register nach MoPeG und HGB.

## Triage — klaere vor Beginn

1. Welche Rechtsform liegt vor — OHG, KG, GmbH & Co. KG, PartG, PartGmbB, Limited Partnership?
2. Soll eine Kommanditistenstellung uebertragen werden — Anteilsuebertragung, Teileintritt, Erhöhung Einlage?
3. Wie hoch ist die Hafteinlage und die tatsaechlich geleistete Einlage — sind Haftungsvoraussetzungen (§§ 171-172 HGB) durch Einlagenrueckgewaehr veraendert worden?
4. Sind Vollmachten und Vertretungsregelungen aktuell — wer ist Komplementaer und wie wird er vertreten?
5. Gilt das Gesellschaftsregister nach MoPeG (GbR-Register) — Eintragungspflicht fuer GbR?
6. Gibt es Fondsstrukturen (z.B. Investmentkommanditgesellschaft § 124 KAGB)?

## Zentrale Rechtsgrundlagen

- §§ 161-177 HGB — KG: Kommanditistenhaftung bis zur Hoehe der Einlage; Haftung erneut auflebt nach Rueckgewaehr (§ 172 Abs. 4 HGB)
- §§ 171-172 HGB — Haftung des Kommanditisten: nur bis zur Einlage; haftet erneut, wenn Einlage herabgesetzt oder zurueckgezahlt wird
- § 706 BGB n.F. (MoPeG) — Gesellschaftsregister fuer GbR; Eintragungspflicht ab 01.01.2024; Grundstuckserwerb nur als eingetragene GbR (eGbR) moeglich
- §§ 705-740 BGB n.F. (MoPeG) — modernisiertes Personengesellschaftsrecht ab 01.01.2024
- § 124 KAGB — Investmentkommanditgesellschaft (InvKG): Sonderform fuer Fondsvehikel; Aufsicht BaFin
- §§ 1 Abs. 3, 48 ff. HGB — Prokura und Handelsvollmacht: massgeblich fuer Vertretung in der KG
- § 16 GmbHG analog fuer Kommanditistenwechsel — Gesellschafterliste-Gedanke: Eintragung im HR als Legitimationsakt

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Rechtsform und Gesellschaftsvertrag pruefen:** aktueller HR-Auszug HRA, Gesellschaftsvertrag, Kommanditistenliste
2. **Haftungslage klaren:** Hafteinlage vs. tatsaechlich geleistete Einlage; Einlagenrueckgewaehr-Pruefung (§ 172 Abs. 4 HGB) fuer alle relevanten Zahlungen der letzten 5 Jahre
3. **Vertretungsmacht feststellen:** Komplementaer (in GmbH & Co. KG: GmbH-Geschaftsfuehrer); Prokura; Gesamtvertretung?
4. **Kommanditistenwechsel (falls vorgesehen):** Abtretungsvertrag, HR-Anmeldung, Gesellschaftsvertrag-Zustimmungspflicht pruefen
5. **MoPeG-Compliance:** GbR-Register geprueft? Bei Grundstucksbesitz: Eintragung als eGbR erforderlich (§ 706 BGB n.F.)
6. **Fondsvehikel (§ 124 KAGB):** BaFin-Genehmigung, Anlagebedingungen, KAGB-Compliance
7. **Stimmrechts- und Abstimmungsregeln:** Mehrheitserfordernisse im Gesellschaftsvertrag; Stimmrechtsausschluss bei Interessenkonflikten; Protokoll

## Entscheidungsbaum

- Einlage unter Hafteinlage → § 172 Abs. 4 HGB → Aussenhaftung wieder aufgelebt → Red Flag
- Kommanditanteilsuebertragung → Gesellschaftsvertrag Zustimmungsklausel? → Ja: Zustimmung aller Gesellschafter
- GbR mit Grundstueck → MoPeG § 706 BGB n.F. → Eintragung als eGbR erforderlich vor Eigentumsuebergang
- InvKG § 124 KAGB → BaFin zustaendig → besondere Anforderungen an Verwaltung und Anleger

## Output-Template: KG-Checkliste

**Adressat:** Deal-Team intern — Tonfall sachlich-strukturiert

```
KG-CHECKLISTE
Gesellschaft: [NAME] — HR-Nr.: [HRA XXXX]

EINLAGEN
  Hafteinlage Kommanditist [NAME]: [BETRAG] EUR
  Geleistete Einlage: [BETRAG] EUR
  Einlagenrueckgewaehr geprueft: [ ] JA [ ] NEIN → § 172 IV HGB

VERTRETUNG
  Komplementaer: [NAME] — Einzelvertretungsbefugnis: [ ] JA [ ] NEIN
  Prokura: [NAME]

ANTEILSUEBERTRAGUNG
  Zustimmung GV erforderlich: [ ] JA [ ] NEIN
  Abtretungsvertrag formfrei: [ ] JA — Notarpflicht: [ ] NEIN

REGISTER
  HR-Eintrag Kommanditistenwechsel: [ ] OK [ ] TODO
  MoPeG eGbR: [ ] nicht relevant [ ] Eintragung erforderlich bis [DATUM]
```

## Rote Schwellen

- Einlagenrueckgewaehr ohne Pruefung: Aussenhaftung des Kommanditisten unerkannt
- Vertretungsmacht unklar: Signing-Vollmacht angreifbar
- MoPeG-Eintragungspflicht versaeumt: Grundstueckserwerb scheitert

## Standardausgabe

- KG-Checkliste mit Haftungs- und Vertretungsanalyse
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe

## Uebergabe an andere Skills

- Gesellschaftsrecht/Register → `mittelstand-corporate-ma-gesellschaftsrecht-register`
- Transaktionsstruktur → `mittelstand-corporate-ma-transaktionsstruktur`
- Handelsregisterabruf → `mittelstand-corporate-ma-handelsregisterabruf`

## Vorlagen

- assets/templates/kg-checkliste-einlage-vertretung.md
- assets/templates/kommanditisten-abtretungsvertrag.md

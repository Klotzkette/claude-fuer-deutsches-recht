---
name: ins-employee-schulung
description: "Ins 014 Employee Stock Plan, Ins 016 Schulung Policy: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 014 Employee Stock Plan, Ins 016 Schulung Policy

## Arbeitsbereich

Dieser Skill bündelt **Ins 014 Employee Stock Plan, Ins 016 Schulung Policy** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-014-employee-stock-plan` | Prueft Mitarbeiteraktienprogramme (ESOP, LTIP, RSU) auf insiderrechtliche Risiken: Closed Periods, Handelsverbote, automatische Plaene und Befreiungsmoeglichkeiten. |
| `ins-016-schulung-policy` | Entwirft und aktualisiert Insider-Compliance-Richtlinien, Schulungsprogramme und Nachweise fuer Emittenten aller Groessen. |

## Arbeitsweg

Für **Ins 014 Employee Stock Plan, Ins 016 Schulung Policy** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-014-employee-stock-plan`

**Fokus:** Prueft Mitarbeiteraktienprogramme (ESOP, LTIP, RSU) auf insiderrechtliche Risiken: Closed Periods, Handelsverbote, automatische Plaene und Befreiungsmoeglichkeiten.

# Mitarbeiteraktienprogramme (ESOP / LTIP / RSU) – Insiderrechtliche Risiken

## Rechtlicher Rahmen

Aktienbasierte Vergütungsinstrumente (ESOP, LTIP, RSU, Aktienoptionen) unterliegen MAR-Pflichten,
wenn sie zum Kauf oder Verkauf von Finanzinstrumenten des Emittenten berechtigen oder verpflichten.
Entscheidend ist, ob die Ausübung oder Zuteilung in eine Closed Period oder eine Phase mit
Insiderinformation fällt. Safe-Harbour-Regelungen existieren für vorgefasste Pläne (Art. 9 MAR).

Rechtsgrundlagen:
- Art. 9, 14, 19 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/1052 (Rückkaufprogramme, analog): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1052
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden Kap. V: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft, ob die Ausübung von Mitarbeiteraktienoptionen, RSU-Vestings oder anderen
Programmtransaktionen in einer Closed Period oder Insiderphase liegt, und bestimmt, ob ein
Safe Harbour oder eine Befreiung greift.

## Arbeitsprogramm

### Schritt 1 – Programmstruktur analysieren

- Welche Art von Instrument: Option (Ausübungsrecht), RSU (automatische Zuteilung),
 LTIP (leistungsabhängige Zuteilung)?
- Gibt es Ermessensspielraum bei der Ausübung (→ dann: MAR-Prüfung notwendig)?
- Ist die Zuteilung oder Ausübung automatisch und nach Plan ohne individuelle Entscheidung
 des Mitarbeiters?

### Schritt 2 – Closed-Period-Prüfung (Art. 19 Abs. 11 MAR)

- Liegt der Ausübungs-/Zuteilungstermin in einer Closed Period (30 Tage vor Jahres-/
 Halbjahresabschluss-Veröffentlichung)?
- Für PDMRs: Handelsverbot gilt auch für Ausübung von Optionen in Closed Period
- Für reguläre Mitarbeiter: Kein gesetzliches Closed-Period-Verbot, aber Insiderhandelsverbot
 nach Art. 14 MAR bei Vorliegen von Insiderinformation

### Schritt 3 – Insiderhandels-Prüfung (Art. 8, 14 MAR)

- Hat der Mitarbeiter zum Zeitpunkt der Ausübung Zugang zu einer Insiderinformation?
- Gilt für alle Mitarbeiter, nicht nur PDMRs
- Bei automatischen Plans ohne Mitarbeiter-Ermessen: Kausalitätselement des Art. 8 MAR
 fehlt i.d.R. → kein Verstoß

### Schritt 4 – Safe Harbour für vorgefasste Pläne (Art. 9 Abs. 3 MAR)

Safe Harbour greift, wenn:
a) Mitarbeiter hatte vor Erlangen der Insiderinformation einen schriftlichen Plan zur
 Ausübung abgeschlossen (z. B. automatischer Ausübungsplan nach Vesting-Datum)
b) Plan sieht keine Änderungsmöglichkeit für den Mitarbeiter vor
c) Keine diskretionären Handlungen nach Beginn der Insiderphasee
→ Plan-Dokumentation vor Beginn der Insiderphase muss vorliegen.

### Schritt 5 – Empfehlungen für Programmgestaltung

- Einrichtung automatischer Ausübungspläne (pre-arranged plans) für RSUs und Optionen
- Ausübungsfenster nur in eröffneten Trading Windows
- Pre-Clearance-Pflicht für diskretionäre Ausübungen
- Regelmäßige Schulung der Programmteilnehmer

## Red-Team-Fragen

- Fallen Vesting-Termine regelmäßig in Closed Periods?
- Wurden Mitarbeiter mit Insiderkenntnissen auf das Ausübungsverbot hingewiesen?
- Gibt es vorgefasste Pläne, die den Safe Harbour nach Art. 9 Abs. 3 MAR begründen?
- Ist die Unterscheidung zwischen PDMRs (Closed-Period-Verbot) und sonstigen Mitarbeitern
 (nur Insiderhandelsverbot) sauber implementiert?
- Wird das Programm regelmäßig auf insiderrechtliche Risiken überprüft?

## Ausgabeformat

Erzeuge:
1. Programm-Risikomatrix: Instrument × Closed Period × Insiderstatus × Safe Harbour
2. Safe-Harbour-Plan-Vorlage (vorgefasster Ausübungsplan)
3. Mitarbeiter-Belehrungsschreiben (Insiderrecht und Aktienplan)
4. Compliance-Empfehlungen für Programmüberarbeitung

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## 2. `ins-016-schulung-policy`

**Fokus:** Entwirft und aktualisiert Insider-Compliance-Richtlinien, Schulungsprogramme und Nachweise fuer Emittenten aller Groessen.

# Schulung und Compliance-Policy für Insiderrecht

## Rechtlicher Rahmen

MAR enthält keine explizite Schulungspflicht, aber Art. 18 MAR (Belehrungspflicht bei
Insiderliste) und die allgemeine Sorgfaltspflicht aus § 93 AktG sowie die Compliance-Anforderungen
der BaFin begründen eine faktische Pflicht zu regelmäßigen Schulungen. ESMA-Leitlinien und der
BaFin-Emittentenleitfaden empfehlen explizit dokumentierte Schulungsprogramme als Teil eines
funktionierenden Compliance-Systems.

Rechtsgrundlagen:
- Art. 18 MAR (Belehrungspflicht): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 93 AktG (Sorgfaltspflicht): https://www.gesetze-im-internet.de/aktg/__93.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648
- ESMA MAR-Leitlinien: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill entwirft ein vollständiges Insider-Compliance-Schulungsprogramm und die dazugehörige
Policy. Er passt den Umfang an die Unternehmensgröße an (KMU vs. SDAX/DAX-Emittent) und stellt
die lückenlose Dokumentation aller Schulungsmaßnahmen sicher.

## Arbeitsprogramm

### Schritt 1 – Zielgruppenbestimmung

Stufe 1 (alle Mitarbeiter mit Marktzugang): Grundlagen MAR, Handelsverbote, Was ist eine
 Insiderinformation, Meldepflichten
Stufe 2 (PDMRs, IR, Legal, Finance): Vollständige MAR-Pflichten, Directors' Dealings,
 Aufschub, Ad-hoc, Insiderliste
Stufe 3 (Compliance, CFO, General Counsel): Vollständig inkl. Sanktionen, BaFin-Verfahren,
 Strafrecht, Verteidigung

### Schritt 2 – Schulungsinhalte (Kern-Curriculum)

Modul A: Grundlagen
- Was ist eine Insiderinformation (Art. 7 MAR)?
- Wer ist ein Insider?
- Handelsverbote (Art. 14 MAR)
- Meldepflichten bei Eigengeschäften (Art. 19 MAR)
- Closed Periods

Modul B: Spezialthemen
- Zwischenschritte und M&A (Geltl/Daimler)
- Ad-hoc-Pflicht und Aufschub
- Insiderlisten und Belehrung
- Market Sounding
- Sanktionen und Strafrecht (§ 119 WpHG)

Modul C: Fallstudien
- Realer Fall: Verspätete Ad-hoc (BaFin-Bußgeld)
- Realer Fall: Insiderhandel vor M&A-Bekanntgabe
- Übung: Insidervermerk erstellen

### Schritt 3 – Häufigkeit und Format

- Erstschulung: Bei Eintritt in insiderrelevante Funktion (spätestens 2 Wochen nach Aufnahme)
- Auffrischungsschulung: Jährlich
- Anlassbezogene Schulung: Bei Gesetzesänderungen, nach BaFin-Anfragen, nach Zwischenfällen
- Formate: Präsenz-Workshop, E-Learning, Webinar, individuelles Briefing für neue PDMRs

### Schritt 4 – Dokumentation und Nachweise

- Teilnehmerliste mit Datum, Format und Unterschrift
- Schulungsunterlagen archivieren (5 Jahre)
- Wissenstest am Ende (Mindestpunktzahl für Bestätigung)
- Compliance-Matrix: Wer wurde wann geschult (Ampel-System)

### Schritt 5 – Compliance-Policy (Inhalt)

Pflichtinhalt einer Insider-Compliance-Policy:
1. Scope (Geltungsbereich, Personenkreis)
2. Definition Insiderinformation, Insider, PDMR
3. Handelsverbote und Pre-Clearance-Verfahren
4. Closed Periods (Termine, Ausnahmeverfahren)
5. Insiderlisten-Pflichten
6. Ad-hoc-Verfahren und Aufschub
7. Meldepflichten (Directors' Dealings)
8. Sanktionen und Konsequenzen
9. Meldewege und Ansprechpartner
10. Revisions- und Aktualisierungsplan

## Red-Team-Fragen

- Werden neue PDMRs und externe Berater zeitnah geschult?
- Sind Schulungsunterlagen aktuell (letzte MAR-Änderung oder ESMA-Leitlinie eingearbeitet)?
- Gibt es Wissenstests und werden diese dokumentiert?
- Deckt die Policy alle aktuellen Pflichten vollständig ab?
- Werden Schulungsnachweise für BaFin-Anfragen bereitgehalten?

## Ausgabeformat

Erzeuge:
1. Schulungsprogramm-Übersicht (Curriculum, Formate, Häufigkeit)
2. Insider-Compliance-Policy (vollständiger Entwurf)
3. Teilnehmerlisten-Vorlage
4. Compliance-Matrix-Vorlage (Ampel-System)

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

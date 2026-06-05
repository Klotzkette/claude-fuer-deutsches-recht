---
name: ins-vorstand-berater
description: "Ins 012 Vorstand Aufsichtsrat, Ins 013 Berater Kanzlei Bank: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 012 Vorstand Aufsichtsrat, Ins 013 Berater Kanzlei Bank

## Arbeitsbereich

Dieser Skill bündelt **Ins 012 Vorstand Aufsichtsrat, Ins 013 Berater Kanzlei Bank** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-012-vorstand-aufsichtsrat` | Prueft Insiderrecht-Pflichten von Vorstand und Aufsichtsrat: Wissenszurechnung, Geschaeftsordnungspflichten, AktG-Beziehung und Haftungsrisiken. |
| `ins-013-berater-kanzlei-bank` | Prueft insiderrechtliche Pflichten externer Berater (Anwaelte, WPs, Banken): Insiderliste, Handelsverbot, Chinesische Mauern und Haftungsrisiken. |

## Arbeitsweg

Für **Ins 012 Vorstand Aufsichtsrat, Ins 013 Berater Kanzlei Bank** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-012-vorstand-aufsichtsrat`

**Fokus:** Prueft Insiderrecht-Pflichten von Vorstand und Aufsichtsrat: Wissenszurechnung, Geschaeftsordnungspflichten, AktG-Beziehung und Haftungsrisiken.

# Vorstand und Aufsichtsrat – Insiderrechtliche Pflichten

## Rechtlicher Rahmen

Vorstandsmitglieder und Aufsichtsratsmitglieder sind typischerweise PDMRs nach Art. 3 Abs. 1
Nr. 25 MAR und unterliegen sämtlichen MAR-Pflichten. Zusätzlich regeln AktG §§ 76, 93, 116
die Sorgfalts- und Treuepflichten. Das Wissen einzelner Vorstandsmitglieder wird dem Emittenten
zugerechnet. Bei Verstoß: zivilrechtliche Haftung (§§ 97, 98 WpHG) und Strafbarkeit (§ 119 WpHG).

Rechtsgrundlagen:
- Art. 3, 17, 18, 19 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- §§ 76, 93, 116 AktG: https://www.gesetze-im-internet.de/aktg/__93.html
- §§ 97–98 WpHG (Haftung): https://www.gesetze-im-internet.de/wphg/__97.html
- § 119 WpHG (Strafrecht): https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill klärt die insiderrechtlichen Pflichten von Vorstand und Aufsichtsrat im Detail und
schafft eine Grundlage für interne Compliance-Richtlinien und Haftungsprävention.

## Arbeitsprogramm

### Schritt 1 – Wissenszurechnung

- Wissen jedes Vorstandsmitglieds wird dem Emittenten als Gesamtwissen zugerechnet
 (BGH-Rechtsprechung zur Wissenszurechnung bei juristischen Personen)
- Folge: Ad-hoc-Pflicht nach Art. 17 MAR entsteht, sobald ein Vorstandsmitglied Kenntnis hat,
 nicht erst bei Kenntnis des Gesamtvorstands
- Aufsichtsrat: Zurechnung bei Vorstands-relevanten Informationen → prüfen, ob AR-Wissen
 bereits Veröffentlichungspflicht auslöst

### Schritt 2 – Pflichten des Vorstands

a) Ad-hoc-Pflicht: Unverzügliche Veröffentlichung nach Art. 17 MAR
b) Insiderlisten-Pflicht: Sicherstellung, dass Compliance Art. 18 MAR-Listen führt
c) Handelsverbote: Eigengeschäfte nur außerhalb von Closed Periods und ohne Insiderinformation
d) Directors' Dealings: Meldung aller Eigengeschäfte nach Art. 19 MAR
e) Sorgfaltspflicht (§ 93 AktG): Keine Verletzung kapitalmarktrechtlicher Normen als
 Pflichtverletzung
f) Vertraulichkeitspflicht: Keine unzulässige Weitergabe an Dritte

### Schritt 3 – Pflichten des Aufsichtsrats

a) Überwachungspflicht (§ 111 AktG): Prüfung, ob Vorstand MAR-Pflichten erfüllt
b) Eigene Handelsverbote (Art. 14 MAR) und Meldepflichten (Art. 19 MAR) als PDMRs
c) Verschwiegenheitspflicht (§ 116 AktG): Keine Weitergabe von Vertrauliches aus AR-Sitzungen
d) Interessenkonflikt: AR-Mitglieder mit Doppelmandaten oder Verbindungen zu Bietern in M&A
 müssen sich bei AR-Beschlüssen enthalten

### Schritt 4 – Governance-Instrumente

- Compliance-Richtlinie für Vorstand und AR (inkl. Closed Periods, Pre-Clearance, Insiderliste)
- Regelmäßige Schulungen (mind. jährlich)
- Klare Meldewege: Wer meldet was an wen (Compliance-Officer)?
- D&O-Versicherung prüfen: Deckungsausschlüsse für vorsätzliche Kapitalmarktverstöße

### Schritt 5 – Haftungsanalyse

- § 97 WpHG: Haftung des Emittenten für verspätete oder unterlassene Ad-hoc-Mitteilung
- § 98 WpHG: Haftung für falsche Ad-hoc-Mitteilung
- Persönliche Haftung von Vorstandsmitgliedern nach § 93 Abs. 2 AktG, wenn MAR-Pflicht
 schuldhaft verletzt
- Strafbarkeit nach § 119 WpHG: persönlich für handelnde Vorstandsmitglieder

## Red-Team-Fragen

- Ist die Wissenszurechnung zwischen Vorstandsmitgliedern aktiv gemanagt (Information Barriers)?
- Erfüllt jedes einzelne AR-Mitglied seine eigenen MAR-Pflichten (Handelsverbot, DD)?
- Werden AR-Mitglieder auf Interessenkonflikte bei M&A und Kapitalmaßnahmen geprüft?
- Sind Compliance-Richtlinien für Vorstand und AR separat und aktuell?
- Ist die D&O-Versicherung auf Kapitalmarktrecht-Deckung geprüft?

## Ausgabeformat

Erzeuge:
1. Pflichten-Matrix: Vorstand × AR × Norm × Sanktion
2. Compliance-Richtlinien-Entwurf (Auszug für Vorstand und AR)
3. Schulungsagenda (jährliche Auffrischung)
4. Haftungsrisiko-Einschätzung

Belege ausschließlich mit: gesetze-im-internet.de, eur-lex.europa.eu, bafin.de, bgh.de,
dejure.org, openjur.de.

## 2. `ins-013-berater-kanzlei-bank`

**Fokus:** Prueft insiderrechtliche Pflichten externer Berater (Anwaelte, WPs, Banken): Insiderliste, Handelsverbot, Chinesische Mauern und Haftungsrisiken.

# Externe Berater – Kanzleien, Wirtschaftsprüfer, Banken

## Rechtlicher Rahmen

Externe Berater, die im Auftrag eines Emittenten Zugang zu Insiderinformationen erhalten,
unterliegen denselben MAR-Pflichten wie interne Mitarbeiter. Sie müssen eigene Insiderlisten
führen (Art. 18 Abs. 2 MAR), Handelsverbote einhalten (Art. 14 MAR) und Information Barriers
(Chinese Walls) betreiben. Für Investmentbanken gelten zusätzlich MiFID II-Anforderungen.

Rechtsgrundlagen:
- Art. 14, 18 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 10 MAR (Offenlegungsverbot): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- MiFID II Art. 23: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0065
- § 80 WpHG (Verhaltenspflichten): https://www.gesetze-im-internet.de/wphg/__80.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft die Pflichten externer Berater und schafft Vertragsmuster und
Compliance-Protokolle für den Umgang mit Insiderinformationen in Mandats- und
Beratungsverhältnissen.

## Arbeitsprogramm

### Schritt 1 – Pflichten externer Berater (Kanzleien, WPs)

- Eigene Insiderliste führen (Art. 18 Abs. 2 MAR): Alle Mitarbeiter mit Zugang
- Handelsverbot für alle Mitarbeiter, die Zugang zur Insiderinformation haben
- Interne Vertraulichkeitsmaßnahmen (Zugriffsbeschränkungen, Akten-Pseudonymisierung)
- Belehrung der eingesetzten Mitarbeiter über Insiderstatus
- Weitergabe an andere Kanzlei-/WP-Mandanten verboten

### Schritt 2 – Pflichten von Investmentbanken

Zusätzlich zu MAR-Grundpflichten:
- Chinese Walls zwischen Corporate Finance (Kenntnis der Insiderinformation) und
 Eigenhandel, Research und Kundenberatung
- Information Barriers dokumentieren und regelmäßig testen
- Compliance-Officer-Überwachung des Wechsels von Mitarbeitern über die Chinese Wall
- Market Sounding: nur unter Art. 11 MAR-konformen Bedingungen (Skill ins-008)

### Schritt 3 – Vertragliche Absicherung durch Emittenten

Pflichtklauseln in Beratungsverträgen / NDAs mit externen Beratern:
- Verpflichtung zur Führung eigener Insiderlisten
- Verpflichtung zur Einrichtung interner Information Barriers
- Handelsverbot für alle informierten Mitarbeiter
- Recht des Emittenten auf Insiderlisten-Einsicht auf Anfrage
- Haftungsklausel bei MAR-Verstößen durch Berater
- Pflicht zur unverzüglichen Meldung verdächtiger Aktivitäten an Compliance des Emittenten

### Schritt 4 – Monitoring und Kontrolle

- Emittent sollte regelmäßig prüfen, ob externe Berater ihre Verpflichtungen einhalten
- Bei M&A: Datenraum-Zugangsprotokoll (wer hat wann welche Dokumente abgerufen?)
- Nach Abschluss des Mandats: Bestätigung der Datenvernichtung

### Schritt 5 – Haftungsrisiken

- Externe Berater haften nach allgemeinem Deliktsrecht (§ 823 BGB) und ggf.
 Spezialvorschriften, wenn sie MAR-Pflichten verletzen
- Strafbarkeit nach § 119 WpHG gilt auch für externe Personen
- Emittent kann in Anspruch genommen werden, wenn er unzureichend überwacht hat

## Red-Team-Fragen

- Sind alle externen Berater des aktuellen Projekts vertraglich zur Insiderlisten-Führung
 verpflichtet?
- Werden Banken auf ordnungsgemäße Chinese Walls überprüft?
- Ist der Datenraum-Zugang protokolliert und auf need-to-know beschränkt?
- Wurden alle Berater-Mitarbeiter schriftlich belehrt?
- Gibt es einen Mechanismus zur Meldung verdächtiger Aktivitäten?

## Ausgabeformat

Erzeuge:
1. Pflichten-Matrix: Beratertyp × MAR-Pflicht × Nachweis
2. NDA-Zusatzklauseln für externe Berater (Insiderrecht-spezifisch)
3. Chinese-Wall-Protokoll für Investmentbanken
4. Datenraum-Zugangsprotokolle-Vorlage

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

---
name: ins-produktzulassung-whistleblower
description: "Ins 026 Produktzulassung, Ins 028 Whistleblower Meldung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 026 Produktzulassung, Ins 028 Whistleblower Meldung

## Arbeitsbereich

Dieser Skill bündelt **Ins 026 Produktzulassung, Ins 028 Whistleblower Meldung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-026-produktzulassung` | Prueft Insiderinformations-Entstehung bei regulatorischen Produktzulassungen (Pharma, Medtech, Energie): Zwischenschritte, Kursrelevanz und Timing der Ad-hoc. |
| `ins-028-whistleblower-meldung` | Verarbeitet Whistleblower-Hinweise mit Insiderrecht-Bezug: Entgegennahme, Pruefung, Eskalation und MAR-Folgen. |

## Arbeitsweg

Für **Ins 026 Produktzulassung, Ins 028 Whistleblower Meldung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-026-produktzulassung`

**Fokus:** Prueft Insiderinformations-Entstehung bei regulatorischen Produktzulassungen (Pharma, Medtech, Energie): Zwischenschritte, Kursrelevanz und Timing der Ad-hoc.

# Produktzulassung – Insiderrecht bei regulatorischen Entscheidungen

## Rechtlicher Rahmen

In regulierten Industrien (Pharma, Medtech, Energie, Finanzdienstleistungen) können
Produktzulassungsentscheidungen oder Behördenentscheidungen erhebliche Kursrelevanz
aufweisen. Der Geltl/Daimler-Test (EuGH C-19/11) erfordert, dass auch Zwischenschritte
im Zulassungsverfahren auf Insiderinformations-Qualität geprüft werden.

Rechtsgrundlagen:
- Art. 7 Abs. 2, 3 MAR (Zwischenschritte): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- EuGH C-19/11 (Geltl/Daimler): https://curia.europa.eu/juris/document/document.jsf?docid=123755
- Art. 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill identifiziert insiderrelevante Zeitpunkte im Zulassungsverfahren, prüft
Kursrelevanz von Zwischenschritten und steuert Timing und Inhalt der Ad-hoc-Meldungen.

## Arbeitsprogramm

### Schritt 1 – Zulassungsverfahren kartieren

- Erstelle Prozessdiagramm: Antragstellung → Vorprüfung → klinische Phase (Pharma) →
 Behördenprüfung → vorläufige Entscheidung → finale Zulassung
- Identifiziere alle wesentlichen Meilensteine (Advisory Committee Meeting, Complete
 Response Letter, Zulassungsbescheid)
- Benenne interne Wissensträger für jeden Meilenstein

### Schritt 2 – Geltl/Daimler-Test für jeden Meilenstein

Je Meilenstein prüfen:
- Ist das Ereignis konkret und hinreichend wahrscheinlich?
- Ist es kursrelevant (positive Entscheidung? Negative Entscheidung? Auflagen?)?
- Ist es noch nicht öffentlich?
Beispiel Pharma: Positive Phase-III-Studie kann bereits Insiderinformation sein,
auch wenn finale FDA/EMA-Entscheidung noch aussteht.

### Schritt 3 – Kursrelevanz-Beurteilung

- Analyse der Markterwartungen und Analystenbewertungen
- Abweichung vom erwarteten Ergebnis: Positiv-Überraschung oder negatives Ergebnis?
- Finanzielle Bedeutung des Produkts für den Emittenten (Umsatzanteil)
- Vergleich mit Marktreaktionen auf ähnliche Zulassungsentscheidungen in der Branche

### Schritt 4 – Aufschub und Vertraulichkeit

- Laufende Verhandlungen mit Behörde: Legitimes Interesse am Aufschub?
- Behördenverfahren haben typischerweise eigene Vertraulichkeitsregeln (z. B. EMA-Regeln)
- Prüfe: Kann der Emittent Vertraulichkeit zuverlässig sicherstellen?

### Schritt 5 – Ad-hoc-Timing und Koordination

- Bei positiver Entscheidung: Sofortveröffentlichung ab Kenntnis (nicht erst nach offizieller
 Bekanntmachung durch Behörde)
- Bei negativer Entscheidung: Ebenso unverzüglich
- Koordination mit IR und Presse für simultane Kommunikation

## Red-Team-Fragen

- Wurden alle wesentlichen Meilensteine im Zulassungsverfahren auf Insiderinformations-
 Qualität geprüft?
- Wurde der Geltl/Daimler-Test zeitpunktbezogen (nicht rückblickend) angewendet?
- Ist die Kursrelevanz-Beurteilung anhand von Markterwartungen gestützt?
- Wurden alle Wissensträger (Regulatory Affairs, Wissenschaftler, externe Berater) in
 Insiderliste aufgenommen?

## Ausgabeformat

Erzeuge:
1. Zulassungsverfahren-Meilensteinmatrix mit Insiderinformations-Prüfung je Meilenstein
2. Kursrelevanz-Analyse (Markterwartung vs. mögliches Ergebnis)
3. Insiderliste für Zulassungsprojekt
4. Ad-hoc-Entwurf (positiv / negativ / mit Auflagen)

Belege ausschließlich mit: eur-lex.europa.eu, curia.europa.eu, bafin.de, gesetze-im-internet.de.

## 2. `ins-028-whistleblower-meldung`

**Fokus:** Verarbeitet Whistleblower-Hinweise mit Insiderrecht-Bezug: Entgegennahme, Pruefung, Eskalation und MAR-Folgen.

# Whistleblower-Meldungen mit Insiderrecht-Bezug

## Rechtlicher Rahmen

Whistleblower-Meldungen über Insiderhandel oder Marktmanipulation können bei der BaFin
oder intern eingehen. Art. 32 MAR verpflichtet die BaFin zur Einrichtung von Meldekanälen.
Die EU-Whistleblower-Richtlinie 2019/1937 und das HinSchG schützen Melder vor Repressalien.
Intern eingehende Hinweise können Insiderinformationen begründen oder bestehende Aufschübe
gefährden.

Rechtsgrundlagen:
- Art. 32 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- RL 2019/1937 (Whistleblower): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L1937
- HinSchG: https://www.gesetze-im-internet.de/hinschg/
- § 4d WpHG (BaFin-Meldekanal): https://www.gesetze-im-internet.de/wphg/__4d.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill steuert die interne Bearbeitung von Whistleblower-Meldungen, die Insiderhandel,
Marktmanipulation oder MAR-Pflichtverletzungen betreffen, und leitet MAR-Folgehandlungen ein.

## Arbeitsprogramm

### Schritt 1 – Entgegennahme und Erstbewertung

- Welcher Meldekanal (intern/extern, BaFin, Staatsanwaltschaft)?
- Ist der Hinweis ausreichend konkret? (Tatbestand, Person, Zeitraum)
- Sofortige Weiterleitung an Compliance-Officer und (bei Schwere) General Counsel
- Vertraulichkeit des Meldenden sicherstellen (HinSchG-Pflichten)

### Schritt 2 – Vorläufige Sachverhaltsaufklärung

- Welcher MAR-Tatbestand wird behauptet? (Insiderhandel, Tipping, Marktmanipulation,
 verspätete Ad-hoc, falsche Insiderliste)
- Interne Recherche: Zugangsberechtigungen, Transaktionshistorie, Kommunikationsprotokolle
- Erste Einschätzung: Substanziierter Verdacht oder Gefälligkeitsmeldung?

### Schritt 3 – Eskalation und Entscheidung

Bei substanziiertem Verdacht:
a) Sofortige Information des Vorstands (CFO, CEO) – sofern nicht selbst betroffen
b) Einschaltung externer Kanzlei für unabhängige Untersuchung
c) Wenn Insiderinformation: Prüfung ob Ad-hoc-Pflicht besteht oder Aufschub entfällt
d) BaFin: Proaktive Meldung erwägen (Kooperationsbonus)

### Schritt 4 – Repressalien-Schutz (HinSchG)

- Keine Maßnahmen gegen den Whistleblower, die als Repressalie gewertet werden könnten
- Dokumentation aller Maßnahmen gegenüber dem Meldenden und ihre sachliche Rechtfertigung
- Meldestellen-Beauftragter muss unabhängig sein

### Schritt 5 – Abschlussbericht und Archivierung

- Interne Untersuchungsergebnisse schriftlich dokumentieren
- Maßnahmen (Disziplinarrecht, Strafanzeige, BaFin-Meldung) festhalten
- Archivierung 3 Jahre nach Abschluss (HinSchG § 11)

## Red-Team-Fragen

- Wurde die Vertraulichkeit des Whistleblowers ausreichend geschützt?
- Wurde die Meldung vollständig und unvoreingenommen untersucht?
- Wurden MAR-Folgen (Ad-hoc, Aufschub, Insiderliste) aus dem Befund abgeleitet?
- War die Untersuchung unabhängig (kein Befangenheitsrisiko)?
- Wurden Repressalien-Risiken dokumentiert und ausgeschlossen?

## Ausgabeformat

Erzeuge:
1. Erstbewertungsbogen für Whistleblower-Meldung
2. Untersuchungsplan (Schritte, Zeitplan, Verantwortliche)
3. Eskalationsprotokoll (Schwellenwerte für externe Einschaltung / BaFin-Meldung)
4. Abschlussdokumentation-Vorlage

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

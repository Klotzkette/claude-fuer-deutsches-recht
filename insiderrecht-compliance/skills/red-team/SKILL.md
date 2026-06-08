---
name: red-team
description: "Fuehrt adversariales Red-Team-Review gegen Insiderrecht-Compliance-Argumente durch: Findet Schwachstellen, baut Gegenthesen und empfiehlt Absicherung."
---

# Red-Team-Review für Insiderrecht-Compliance

## Konzept

Red-Teaming in der Insiderrecht-Compliance bedeutet: Ein unabhängiger Reviewer versucht aktiv,
die Compliance-Argumente des Emittenten zu widerlegen, Schwachstellen in der Dokumentation
zu finden und die BaFin-Perspektive oder eine Staatsanwaltschaft zu simulieren. Red-Teaming
ist keine Schönheitsübung; es soll echte Verteidigungslücken aufdecken.

Rechtsgrundlagen:
- Art. 7, 17, 18, 19 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- EuGH C-19/11 (Geltl/Daimler): https://curia.europa.eu/juris/document/document.jsf?docid=123755
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill führt ein strukturiertes Red-Team-Review für jeden MAR-relevanten Sachverhalt
durch. Er fordert Gegenthesen zu allen Compliance-Entscheidungen ein, prüft Dokumentation auf
BaFin-Anfragetauglichkeit und gibt Verbesserungsempfehlungen.

## Arbeitsprogramm

### Red-Team-Dimension 1: Insiderinformations-Qualifikation

Angriffspunkte:
- Ist die Information wirklich präzise? (Gegenthese: nur allgemeines Geschäftsrisiko)
- Wurde die Eintrittswahrscheinlichkeit zu niedrig angesetzt?
- Ist die Kursrelevanz-Begründung ex ante tragfähig oder wurde nachträglich argumentiert?
- Wurden Zwischenschritte nach Geltl/Daimler übersehen?
Bewertung: Wäre die Verteidigung vor dem EuGH oder BGH haltbar?

### Red-Team-Dimension 2: Zeitpunkt der Ad-hoc-Pflicht

Angriffspunkte:
- Lag die Insiderinformation früher vor als dokumentiert?
- Wurden interne E-Mails oder Berichte, die frühere Kenntnis belegen, ausreichend geprüft?
- Ist die Zeit zwischen interner Erkenntnis und Veröffentlichung „unverzüglich" i.S.d. MAR?
Bewertung: Was würde die BaFin in einem Untersuchungsverfahren finden?

### Red-Team-Dimension 3: Aufschub-Legitimität

Angriffspunkte:
- Ist das legitime Interesse wirklich tragfähig?
- Stehen öffentliche Aussagen des Emittenten im Widerspruch zur verschwiegenen Information?
- War die Vertraulichkeit wirklich gewahrt?
Bewertung: Würde die Aufschubakte einer BaFin-Prüfung standhalten?

### Red-Team-Dimension 4: Insiderliste und Belehrung

Angriffspunkte:
- Sind alle Wissensträger (inkl. Externe) erfasst?
- Stimmen Aufnahmedaten mit dem tatsächlichen Informationszugang überein?
- Sind Belehrungen rechtzeitig vor dem Informationszugang erfolgt?

### Red-Team-Dimension 5: Directors' Dealings und Eigengeschäfte

Angriffspunkte:
- Gibt es PDMR-Eigengeschäfte in Zeiträumen, in denen Insiderinformationen vorlagen?
- Wurden alle meldepflichtigen Instrumente (auch Derivate) berücksichtigt?
- Wurden Closed Periods eingehalten?

### Schritt 6 – Bewertung und Empfehlungen

- Priorisiere Schwachstellen nach Kritikalität (Hoch / Mittel / Niedrig)
- Empfehle konkrete Maßnahmen (Nachbesserung der Dokumentation, Schulung, Prozessänderung)
- Erstelle Aktionsplan mit Verantwortlichen und Fristen

## Red-Team-Fragen (Meta)

- Wer hat dieses Red-Team-Review gemacht – intern oder extern?
- Wurde der Reviewer mit allen relevanten Dokumenten versorgt?
- Wurden Befunde schriftlich festgehalten und weitergeleitet?
- Gibt es eine Follow-up-Prüfung nach Maßnahmenumsetzung?

## Ausgabeformat

Erzeuge:
1. Red-Team-Befundliste (Dimension × Angriffspunkt × Schwere × Empfehlung)
2. Dokumentations-Scorecard (je Compliance-Element: ausreichend / lückenhaft / fehlend)
3. Priorisierter Aktionsplan
4. Kurze Zusammenfassung für Vorstand/Compliance-Committee

Belege ausschließlich mit: eur-lex.europa.eu, curia.europa.eu, gesetze-im-internet.de,
bafin.de, bgh.de, dejure.org, openjur.de.

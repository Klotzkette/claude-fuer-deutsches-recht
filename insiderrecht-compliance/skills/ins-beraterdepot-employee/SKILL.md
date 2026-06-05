---
name: ins-beraterdepot-employee
description: "Ins 045 Beraterdepot, Ins 046 Employee Rumor: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 045 Beraterdepot, Ins 046 Employee Rumor

## Arbeitsbereich

Dieser Skill bündelt **Ins 045 Beraterdepot, Ins 046 Employee Rumor** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-045-beraterdepot` | Prueft Compliance-Risiken bei Berater-Depots und Treuhandkonten: Wissenszurechnung, Handelsverbote, chinesische Mauern und Monitoring-Pflichten. |
| `ins-046-employee-rumor` | Bewertet Mitarbeiter-Geruechte ueber Insiderwissen: Klaerungspflichten des Compliance-Officers, Insiderlisten-Folgen und Eskalation. |

## Arbeitsweg

Für **Ins 045 Beraterdepot, Ins 046 Employee Rumor** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-045-beraterdepot`

**Fokus:** Prueft Compliance-Risiken bei Berater-Depots und Treuhandkonten: Wissenszurechnung, Handelsverbote, chinesische Mauern und Monitoring-Pflichten.

# Berater-Depot und Treuhandkonten – Insiderrecht

## Rechtlicher Rahmen

Rechtsanwälte, Steuerberater, Wirtschaftsprüfer und andere Berater, die im Rahmen ihrer
Mandatstätigkeit Insiderinformationen erlangen, dürfen weder für eigene Rechnung noch für
fremde Rechnung (Kunden-Depots, Treuhandkonten) handeln. Art. 8, 9 MAR regeln den objektiven
und subjektiven Tatbestand. Besonders heikel: Vermögensverwaltungsmandate für Insider-Kunden.

Rechtsgrundlagen:
- Art. 8, 9, 14 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill identifiziert Insiderrisiken bei Berater-Depots und Treuhandkonten und
entwickelt Schutzmaßnahmen für Berater und ihre Mandanten.

## Arbeitsprogramm

### Schritt 1 – Mandatsprüfung

- Für welche Mandanten führt der Berater ein Depot oder Treuhandkonto?
- Ist der Berater aufgrund seiner Mandatstätigkeit im Besitz von Insiderinformationen
 über Finanzinstrumente im Depot?
- Wenn ja: Handelsverbot für alle Transaktionen in diesen Instrumenten

### Schritt 2 – Wissenszurechnung bei Berater-Teams

- Gilt das Wissen eines Beraters der gesamten Kanzlei / Beratungsgesellschaft?
 (Grundsatz der Wissenszurechnung in Berufsorganisationen)
- Chinese Walls: Trennung zwischen der Abteilung mit Insiderwissen und der
 Vermögensverwaltungsabteilung
- Dokumentation der Chinese Wall und regelmäßige Tests

### Schritt 3 – Vermögensverwaltungsmandat für Insider-Mandanten

- Führt ein Berater ein Vermögensverwaltungsmandat für einen Mandanten, der selbst ein
 Insider ist? → Safe Harbour nach Art. 9 Abs. 1 lit. a MAR: Kein Tatbestand, wenn der
 Berater eigenständige Entscheidungen ohne Insiderwissen des Mandanten trifft und der
 Mandant keine Weisungen aufgrund von Insiderinformationen gegeben hat
- Dokumentation: Keine Kommunikation des Mandanten über laufende Insiderinformationen

### Schritt 4 – Monitoring-Pflichten der Berater-Gesellschaft

- Compliance muss alle Depotkonten und Treuhandkonten auf insiderrelevante Transaktionen
 überwachen
- Verdächtige Transaktionen: Kauf/Verkauf kurz vor Kursbewegungs-Ereignis bei Mandanten-
 Unternehmen
- Meldung verdächtiger Transaktionen an BaFin (Art. 16 MAR)

### Schritt 5 – Präventionsmaßnahmen

- Watch List und Restricted List für Finanzinstrumente, für die Insiderwissen besteht
- Automated pre-trade screening: System prüft Transaktionen gegen Watch List
- Schulung aller Berater und Assistenten auf Insiderrecht

## Red-Team-Fragen

- Sind Chinese Walls zwischen Beratungsabteilungen und Depot-/Vermögensverwaltung eingerichtet?
- Gibt es eine Restricted/Watch List, die automatisch Transaktionen blockiert?
- Werden Vermögensverwaltungsmandate für Insider-Mandanten überwacht?
- Ist das Safe-Harbour-Verfahren (Art. 9 Abs. 1 MAR) dokumentiert?

## Ausgabeformat

Erzeuge:
1. Depot-Compliance-Matrix (Depot × Insiderwissen × Handelsverbot)
2. Chinese-Wall-Protokoll für Berater-Gesellschaft
3. Watch-List- und Restricted-List-Verfahren
4. Safe-Harbour-Dokumentationsvorlage (Art. 9 Abs. 1 MAR)

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Für Vermögensverwalter und Anlageberater, die reguliert nach WpIG oder KWG sind, bestehen
neben MAR zusätzliche Verhaltenspflichten (§§ 63 ff. WpHG, MiFID II). Das Trading-
Surveillance-System muss Transaktionen in Finanzinstrumenten der betreuten Mandate gegen
interne Watch- und Restricted Lists abgleichen. Bei verdächtigen Transaktionen: Meldung nach
Art. 16 MAR an die BaFin (Suspicious Transaction Report / STR-Meldepflicht).

Weitere Quellen:
- Art. 16 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 80 WpHG: https://www.gesetze-im-internet.de/wphg/__80.html

## 2. `ins-046-employee-rumor`

**Fokus:** Bewertet Mitarbeiter-Geruechte ueber Insiderwissen: Klaerungspflichten des Compliance-Officers, Insiderlisten-Folgen und Eskalation.

# Mitarbeiter-Gerüchte über Insiderwissen – Compliance-Reaktion

## Rechtlicher Rahmen

Wenn Compliance-Officers Hinweise erhalten, dass Mitarbeiter über potenziell kursrelevante
nicht-öffentliche Informationen verfügen, entstehen Klärungspflichten: (1) Ist eine
Insiderinformation entstanden? (2) Sind alle Wissensträger in der Insiderliste? (3) Besteht
Ad-hoc-Pflicht? Compliance hat keine Pflicht zur BaFin-Meldung allein aufgrund eines
Gerüchts, aber eine Sorgfaltspflicht zur Abklärung.

Rechtsgrundlagen:
- Art. 16 MAR (Verdachtsmeldung): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 18 MAR (Insiderliste): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 93 AktG: https://www.gesetze-im-internet.de/aktg/__93.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill steuert die interne Klärungsreaktion auf Mitarbeiter-Gerüchte über
Insiderwissen und stellt sicher, dass Compliance-Pflichten ausgelöste Folgehandlungen
vollständig abdeckt.

## Arbeitsprogramm

### Schritt 1 – Gerüchts-Erfassung und Erstbewertung

- Wie wurde das Gerücht kommuniziert? (Flurfunk, E-Mail, direkter Hinweis)
- Was ist der konkrete Inhalt? (Welche Information, welches Unternehmen, welcher Zeitraum)
- Wie substanziiert ist das Gerücht? (Detailgrad, Quellenangabe, Plausibilität)
- Sofortige Dokumentation mit Datum und Uhrzeit

### Schritt 2 – Sachverhaltsaufklärung

- Interne Recherche: Zugangsberechtigungen der genannten Mitarbeiter
- Interview (vertraulich): Mit dem Mitarbeiter, der das Gerücht kommuniziert hat
- Gegebenenfalls: Interview mit der Person, die das Wissen angeblich hat
- Ziel: Prüfen, ob präzise kursrelevante nicht-öffentliche Information vorliegt

### Schritt 3 – Folgehandlungen bei bestätigtem Insiderwissen

Wenn bestätigt, dass eine Insiderinformation vorliegt:
a) Insiderliste aktualisieren (alle Wissensträger aufnehmen)
b) Prüfen: Besteht oder bestand Ad-hoc-Pflicht? Aufschub rechtmäßig?
c) Prüfen: Hat der Mitarbeiter oder seine nahestehenden Personen in der Zwischenzeit
 Eigengeschäfte getätigt? → Art. 14 MAR-Prüfung
d) Falls Eigengeschäfte: BaFin-Meldung nach Art. 16 MAR erwägen

### Schritt 4 – Nicht-Bestätigung

Wenn nicht bestätigt, dass eine Insiderinformation vorliegt:
- Dokumentation der Klärungsschritte
- Abschluss des Vorgangs mit Begründung
- Fallweise Überprüfung, ob neue Informationen die Einschätzung ändern

### Schritt 5 – Kultur und Prävention

- Compliance-Kultur: Mitarbeiter sollen Compliance bei Unsicherheiten aktiv ansprechen
- Klarer, nicht bedrohlicher Meldekanal (kein Repressaliensrisiko für Meldenden)
- Regelmäßige Erinnerung: „Wenn unklar, frag Compliance"

## Red-Team-Fragen

- Wurde das Gerücht vollständig und unvoreingenommen abgeklärt?
- Wurden mögliche Eigengeschäfte des betroffenen Mitarbeiters geprüft?
- Ist die Dokumentation ausreichend für eine spätere BaFin-Prüfung?
- Gibt es einen sicheren Meldekanal für Mitarbeiter, der keine Repressalien auslöst?

## Ausgabeformat

Erzeuge:
1. Gerüchts-Erstbewertungs-Formular
2. Klärungsprotokoll (Sachverhaltsaufklärung × Ergebnis × Folgehandlungen)
3. Eigengeschäfts-Prüfprotokoll für betroffene Mitarbeiter
4. Abschluss-Dokumentations-Vorlage

Belege ausschließlich mit: eur-lex.europa.eu, bafin.de, gesetze-im-internet.de, dejure.org.

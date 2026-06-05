---
name: ins-directors-closed
description: "Ins 009 Directors Dealings, Ins 010 Closed Periods: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 009 Directors Dealings, Ins 010 Closed Periods

## Arbeitsbereich

Dieser Skill bündelt **Ins 009 Directors Dealings, Ins 010 Closed Periods** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-009-directors-dealings` | Prueft und dokumentiert Eigengeschaefte von Fuehrungskraeften (PDMRs) und nahestehenden Personen nach Art. 19 MAR: Schwellen, Meldefristen, Closed Periods und Ausnahmen. |
| `ins-010-closed-periods` | Verwaltet Closed Periods nach Art. 19 Abs. 11 MAR: Berechnung, Kommunikation, Ausnahmenantrag und Handelssperren-Monitoring. |

## Arbeitsweg

Für **Ins 009 Directors Dealings, Ins 010 Closed Periods** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-009-directors-dealings`

**Fokus:** Prueft und dokumentiert Eigengeschaefte von Fuehrungskraeften (PDMRs) und nahestehenden Personen nach Art. 19 MAR: Schwellen, Meldefristen, Closed Periods und Ausnahmen.

# Directors' Dealings nach Art. 19 MAR

## Rechtlicher Rahmen

Art. 19 VO (EU) 596/2014 (MAR) verpflichtet Personen mit Führungsaufgaben (PDMRs) und ihnen
nahestehende Personen, Eigengeschäfte in Finanzinstrumenten des Emittenten zu melden. Die
Meldepflicht besteht ab einem kumulierten Jahresvolumen von 20.000 EUR (Opt-in bis 200.000 EUR
möglich). Frist: 3 Geschäftstage. Closed Periods: 30 Tage vor Bekanntgabe von Halbjahres- oder
Jahresabschlüssen. DVO (EU) 2016/523 legt das Meldeformat fest.

Rechtsgrundlagen:
- Art. 19 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/523 (Meldeformat): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0523
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden Kap. V: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill stellt sicher, dass alle meldepflichtigen Eigengeschäfte vollständig, fristgerecht
und im korrekten Format der BaFin gemeldet und veröffentlicht werden. Er deckt die Personen-
abgrenzung (PDMR / nahestehende Person), die Schwellenberechnung, Closed Periods und die
Ausnahmen ab.

## Arbeitsprogramm

### Schritt 1 – Personenkreis bestimmen

PDMRs (Persons Discharging Managerial Responsibilities):
- Vorstandsmitglieder, Aufsichtsratsmitglieder, leitende Angestellte mit regelmäßigem Zugang
 zu Insiderinformationen und Befugnis zu wesentlichen Managemententscheidungen

Nahestehende Personen (Art. 3 Abs. 1 Nr. 26 MAR):
- Ehe-/Lebenspartner, unterhaltsberechtigte Kinder, Verwandte seit ≥1 Jahr im gemeinsamen
 Haushalt
- Juristische Personen unter Kontrolle des PDMR oder nahestehender Person

### Schritt 2 – Meldepflichtige Transaktionen und Schwelle

Meldepflichtige Geschäfte:
- Kauf, Verkauf, Leerverkauf, Tausch, Schenkung, Erbschaft, Ausübung von Optionen und Bezugs-
 rechten in Aktien, Anleihen, Derivaten des Emittenten
Schwelle: 20.000 EUR kumuliert im Kalenderjahr → erste Meldung wenn erreicht, danach
 jede weitere Transaktion meldepflichtig (kein neues Jahresreset bis Jahresende)

### Schritt 3 – Frist und Format

- Meldung innerhalb von 3 Geschäftstagen nach Transaktion
- Meldung an BaFin UND Emittenten (Art. 19 Abs. 2 MAR)
- Emittent veröffentlicht innerhalb von 3 Geschäftstagen nach Eingang (§ 119 WpHG)
- Format: DVO (EU) 2016/523-konformes Formular mit Pflichtfeldern (Name, Position, Art des
 Instruments, Art der Transaktion, Datum, Preis, Volumen)

### Schritt 4 – Closed Periods (Art. 19 Abs. 11 MAR)

- 30 Tage vor Bekanntgabe des Halbjahres- oder Jahresabschlusses: kein Handel
- Emittent muss PDMR über Closed-Period-Termine schriftlich informieren
- Ausnahmen: außergewöhnliche Umstände (dringende finanzielle Notlage), auf Antrag beim Emittenten

### Schritt 5 – Interne Pre-Clearance

Empfehlen (nicht gesetzlich zwingend, aber Best Practice):
- PDMR beantragt Freigabe beim Compliance-Officer vor jeder Transaktion
- Compliance prüft: kein Insiderstatus, keine Closed Period, keine offene Insiderinformation
- Schriftliche Freigabe oder Verweigerung mit Begründung
- Aufbewahrung 5 Jahre

## Red-Team-Fragen

- Sind alle PDMRs und nahestehenden Personen identifiziert und informiert?
- Wurden alle meldepflichtigen Instrumente (nicht nur Aktien!) erfasst?
- Wird die 20.000-EUR-Schwelle korrekt auf Jahresbasis kumuliert?
- Werden Closed Periods rechtzeitig kommuniziert?
- Werden Pre-Clearance-Entscheidungen schriftlich dokumentiert?
- Erfolgt die Meldung an BaFin und Emittent binnen 3 Geschäftstagen?
- Veröffentlicht der Emittent die Meldungen rechtzeitig?
- Werden Derivate und indirekte Transaktionen (über nahestehende Personen) erfasst?

## Ausgabeformat

Erzeuge:
1. PDMR-Transaktionsmeldung (DVO 2016/523-konformes Formular)
2. Closed-Period-Kalender (aktuelles Geschäftsjahr)
3. Pre-Clearance-Antragsformular
4. Compliance-Matrix: PDMR × Transaktion × Meldestatus

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org,
openjur.de.

## 2. `ins-010-closed-periods`

**Fokus:** Verwaltet Closed Periods nach Art. 19 Abs. 11 MAR: Berechnung, Kommunikation, Ausnahmenantrag und Handelssperren-Monitoring.

# Closed Periods nach Art. 19 Abs. 11 MAR

## Rechtlicher Rahmen

Art. 19 Abs. 11 VO (EU) 596/2014 (MAR) verbietet PDMRs, während einer Closed Period in
Finanzinstrumenten des Emittenten zu handeln. Eine Closed Period beginnt 30 Kalendertage
vor Ankündigung des Jahres- oder Halbjahresabschlusses (nicht des Quartalsberichts). Ausnahmen
sind auf außergewöhnliche Umstände beschränkt und bedürfen der Genehmigung des Emittenten.

Rechtsgrundlagen:
- Art. 19 Abs. 11–12 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- ESMA-Leitlinien zu Closed Periods: https://www.bafin.de/dok/8252648
- § 25a WpHG: https://www.gesetze-im-internet.de/wphg/__25a.html
- BaFin-Emittentenleitfaden Kap. V.2: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill erstellt einen vollständigen Closed-Period-Kalender, stellt die rechtzeitige
Kommunikation an PDMRs sicher und prüft Ausnahmeanträge auf Zulässigkeit.

## Arbeitsprogramm

### Schritt 1 – Closed-Period-Kalender erstellen

- Identifiziere alle relevanten Berichtstermine: Jahresabschluss, Halbjahresbericht
 (nicht Quartalsmitteilungen nach Art. 19 Abs. 11 MAR)
- Berechne Closed-Period-Beginn: 30 Kalendertage vor geplantem Veröffentlichungstermin
- Ende der Closed Period: Tag der Veröffentlichung (inkl.)
- Kalender für das gesamte Geschäftsjahr im Voraus erstellen

### Schritt 2 – Kommunikation an PDMRs

- Schriftliche Mitteilung an alle PDMRs (und nahestehende Personen) spätestens 5 Werktage
 vor Beginn jeder Closed Period
- Inhalt: Beginn- und Enddatum, betroffene Instrumente, Konsequenzen bei Verletzung
- Empfangsbestätigung einholen und archivieren

### Schritt 3 – Ausnahmenantrag (Art. 19 Abs. 12 MAR)

Ausnahmen nur bei außergewöhnlichen Umständen:
a) Finanzieller Notfall des PDMR (z. B. dringende Liquiditätsbeschaffung)
b) Merkmale der Transaktion lassen Bezug zur Insiderinformation ausscheiden
 (z. B. automatischer Sparplan, der vor Closed Period eingerichtet wurde)
Antragsprozess:
- Schriftlicher Antrag des PDMR mit Begründung
- Entscheidung durch Compliance (und ggf. Vorstand) mit Begründung
- Dokumentation der Entscheidung
Ausnahme ist restriktiv auszulegen; bloße finanzielle Bequemlichkeit genügt nicht.

### Schritt 4 – Überwachung und Monitoring

- Compliance überwacht Depotauszüge von PDMRs während Closed Period (sofern Zugang besteht)
- Bei Auffälligkeiten: sofortige Klärung und ggf. Meldung nach Art. 19 MAR
- Trading-Surveillance-System sollte Closed-Period-Daten enthalten

### Schritt 5 – Verletzungsdokumentation

Falls eine Closed-Period-Verletzung festgestellt wird:
- Sofortige Benachrichtigung des CFO und Compliance-Officers
- Prüfung: Lag eine Ausnahme vor? Wenn nein: Meldepflicht nach Art. 19 MAR (ex post),
 BaFin-Meldung und interne Untersuchung
- Bußgeld nach § 120 WpHG möglich (bis zu 1 Mio. EUR für natürliche Personen)

## Red-Team-Fragen

- Wurde der Closed-Period-Kalender rechtzeitig für das gesamte Geschäftsjahr erstellt?
- Wurden alle PDMRs und nahestehenden Personen schriftlich informiert?
- Werden Ausnahmeanträge restriktiv geprüft und dokumentiert?
- Gibt es ein Trading-Monitoring-System mit Closed-Period-Integration?
- Ist klar geregelt, wer Ausnahmen genehmigt und wie das dokumentiert wird?
- Werden auch automatische Sparpläne und ESOP-Pläne auf Closed-Period-Relevanz geprüft?

## Ausgabeformat

Erzeuge:
1. Closed-Period-Kalender (Jahresübersicht, tabellarisch)
2. PDMR-Informationsschreiben (Vorlage)
3. Ausnahmeantrag-Formular und Entscheidungsvorlage
4. Verletzungs-Eskalationsprotokoll

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

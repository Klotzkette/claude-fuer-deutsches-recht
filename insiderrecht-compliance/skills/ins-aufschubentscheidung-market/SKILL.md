---
name: ins-aufschubentscheidung-market
description: "Ins 004 Aufschubentscheidung, Ins 008 Market Sounding: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 004 Aufschubentscheidung, Ins 008 Market Sounding

## Arbeitsbereich

Dieser Skill bündelt **Ins 004 Aufschubentscheidung, Ins 008 Market Sounding** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-004-aufschubentscheidung` | Prueft die drei Aufschubvoraussetzungen nach Art. 17 Abs. 4 MAR, dokumentiert die Aufschubakte und steuert die Aufhebungspflicht. |
| `ins-008-market-sounding` | Steuert Market-Sounding-Prozesse nach Art. 11 MAR und DVO 2016/960: Vorab-Formalia, Wall-Crossing, Protokollierung und Wall-Down-Management. |

## Arbeitsweg

Für **Ins 004 Aufschubentscheidung, Ins 008 Market Sounding** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-004-aufschubentscheidung`

**Fokus:** Prueft die drei Aufschubvoraussetzungen nach Art. 17 Abs. 4 MAR, dokumentiert die Aufschubakte und steuert die Aufhebungspflicht.

# Aufschubentscheidung nach Art. 17 Abs. 4 MAR

## Rechtlicher Rahmen

Art. 17 Abs. 4 MAR erlaubt dem Emittenten, die Veröffentlichung einer Insiderinformation
aufzuschieben, wenn kumulativ drei Voraussetzungen erfüllt sind:
(1) Legitimes Interesse des Emittenten an der Verzögerung,
(2) keine Irreführung der Öffentlichkeit,
(3) Sicherstellung der Vertraulichkeit.
Der Aufschub ist kein Recht, sondern eine begrenzte Ausnahme. Der Emittent trägt die volle
Beweislast. BaFin ist unverzüglich nach Ende des Aufschubs zu unterrichten (Art. 17 Abs. 4 UAbs. 3).

Rechtsgrundlagen:
- Art. 17 Abs. 4 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- ESMA-Leitlinien zum Aufschub (ESMA/2016/1478): https://www.bafin.de/dok/8252648
- § 50 Abs. 3 WpHG: https://www.gesetze-im-internet.de/wphg/__50.html
- BaFin-Emittentenleitfaden Kap. VI.3: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill stellt sicher, dass Aufschubentscheidungen rechtssicher getroffen, lückenlos
dokumentiert und zeitgerecht beendet werden. Er schützt vor dem Compliance-Risiko eines
unberechtigten Aufschubs und der daraus resultierenden Haftung nach § 97 WpHG.

## Arbeitsprogramm

### Schritt 1 – Voraussetzung 1: Legitimes Interesse

Prüfe, ob einer der anerkannten legitimen Interessen-Tatbestände vorliegt:
- Laufende Verhandlungen (M&A, Refinanzierung, strategische Kooperationen), deren Ergebnis durch
 vorzeitige Veröffentlichung wesentlich beeinträchtigt würde
- Ausstehende Board-Entscheidung, die zur Vollständigkeit der Mitteilung erforderlich ist
- Notwendigkeit, begleitende Maßnahmen (z. B. Kapitalerhöhung) vorzubereiten
Nicht ausreichend: allgemeiner Wunsch nach Kursschutz, PR-Vorbereitung, Warten auf günstigeren Markt

### Schritt 2 – Voraussetzung 2: Keine Irreführung

Prüfe, ob die verschwiegene Information im Widerspruch zu einer öffentlichen Aussage steht:
- Steht die Insiderinformation im Widerspruch zu Gewinnprognosen, Statements des Vorstands
 oder Investoren-Präsentationen?
- Hat der Emittent Marktgerüchte aktiv dementiert, die der Insiderinformation entsprechen?
- Gilt das Irreführungsverbot auch ggü. Analysten, Rating-Agenturen, Kreditgebern.
→ Bei Widerspruch zu öffentlichen Aussagen: Aufschub nicht zulässig.

### Schritt 3 – Voraussetzung 3: Vertraulichkeitssicherung

Dokumentiere Maßnahmen zur Vertraulichkeit:
- Notwendigkeit, Informationskreis schriftlich zu begrenzen (Need-to-know-Prinzip)
- Insiderliste nach Art. 18 MAR gepflegt und aktuell gehalten
- Vertraulichkeitsvereinbarungen für externe Parteien (Berater, Banken, Gegenparteien)
- IT-Sicherheitsmaßnahmen (Datenverschlüsselung, Zugriffsprotokoll)
- Leak-Monitoring (Medien, Kursbewegungen, Trading-Auffälligkeiten)

### Schritt 4 – Aufschub-Beschluss und Dokumentation

Erstelle Aufschubakte mit:
- Datum und Uhrzeit der Aufschubentscheidung
- Name der entscheidenden Person(en) (i.d.R. CFO und Compliance-Officer)
- Begründung zu allen drei Voraussetzungen (je Absatz, mit Belegen)
- Geplante Dauer / geplanter Trigger für Aufhebung
- Aktualisierungen bei Änderung der Sachlage

### Schritt 5 – Aufhebungspflicht und BaFin-Meldung

Definiere vorab Trigger für Pflicht zur sofortigen Ad-hoc-Veröffentlichung:
- Signing eines M&A-Vertrags
- Board-Beschluss
- Informationsleak (Medien berichten, Kurssprung ohne Erklärung)
- Wegfall des legitimen Interesses
Nach Veröffentlichung: BaFin unverzüglich informieren (schriftlich), Aufschubgrund benennen.

## Red-Team-Fragen

- Liegt tatsächlich ein legitimes Interesse vor, oder wird der Aufschub nur zur PR-Vorbereitung
 verwendet?
- Stehen öffentliche Aussagen des Emittenten im Widerspruch zur verschwiegenen Information?
- Ist der Informationskreis wirklich auf „need to know" begrenzt?
- Ist die Insiderliste vollständig und aktuell?
- Gibt es einen definierten Trigger für die Aufhebung?
- Wurde die BaFin nach Veröffentlichung unverzüglich informiert?
- Wurde Leak-Monitoring betrieben und ein unerwarteter Kurssprung analysiert?
- Ist die Aufschubakte so vollständig, dass BaFin und Gericht die Entscheidung nachvollziehen können?

## Ausgabeformat

Erzeuge:
1. Aufschub-Beschlussvorlage (tabellarisch: Merkmal – Begründung – Beleg)
2. Aufschubakte (inkl. Vertraulichkeitsnachweise und Insiderlisten-Referenz)
3. Trigger-Liste für Aufhebungspflicht
4. BaFin-Meldungsvorlage nach Art. 17 Abs. 4 UAbs. 3 MAR

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org,
openjur.de, curia.europa.eu, bgh.de.

## 2. `ins-008-market-sounding`

**Fokus:** Steuert Market-Sounding-Prozesse nach Art. 11 MAR und DVO 2016/960: Vorab-Formalia, Wall-Crossing, Protokollierung und Wall-Down-Management.

# Market Sounding nach Art. 11 MAR

## Rechtlicher Rahmen

Art. 11 VO (EU) 596/2014 (MAR) schafft einen sicheren Hafen für die Übermittlung von
Insiderinformationen an potenzielle Investoren vor Ankündigung einer Transaktion (Emission,
Platzierung, Kapitalerhöhung, M&A). DVO (EU) 2016/960 legt das detaillierte Verfahren fest.
Nur bei vollständiger Einhaltung des Verfahrens schützt der Safe Harbour vor dem Verbot der
unzulässigen Offenlegung (Art. 10 MAR).

Rechtsgrundlagen:
- Art. 11 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/960: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0960
- Art. 10 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill führt Emittenten und Konsortialbanken vollständig durch den Market-Sounding-Prozess:
von der Pre-Sounding-Vorbereitung über Wall Crossing bis zum Wall Down nach Ad-hoc-Veröffent-
lichung. Er stellt die lückenlose DVO-konforme Dokumentation sicher.

## Arbeitsprogramm

### Schritt 1 – Vorbereitungsphase (Pre-Wall Crossing)

- Bestimme, welche Informationen im Sounding übermittelt werden sollen.
- Klassifiziere: Welche Informationen sind Insiderinformationen nach Art. 7 MAR?
- Erstelle Non-Insider-Version: Informationen, die ohne Insiderstatus weitergegeben werden können.
- Bereite Sounding-Skript und schriftliche Vorabinformation vor (Art. 11 Abs. 3 MAR):
 a) Erklärung, dass Informationen UPSI (unpublished price-sensitive information) enthalten
 b) Handelsverbot für Dauer des Insiderstatus
 c) Vertraulichkeitsverpflichtung

### Schritt 2 – Wall-Crossing-Verfahren

- Einholung der Zustimmung des potenziellen Investors zur Entgegennahme der Insiderinformation
- Schriftliche oder telefonische Bestätigung mit Zeitstempel
- Aufnahme in Insiderliste (Art. 18 MAR) nach Zustimmung
- Übermittlung der Insiderinformation erst nach dokumentierter Zustimmung
- Alle Sounding-Gespräche mit Datum, Uhrzeit, Inhalt und Teilnehmern protokollieren

### Schritt 3 – Während des Soundings

- Kein Abweichen vom genehmigten Sounding-Skript
- Keine zusätzlichen Informationen ohne neue Wall-Crossing-Dokumentation
- Protokoll aller Fragen und Antworten
- Separate Dokumentation pro Investor

### Schritt 4 – Wall Down (Beendigung des Insiderstatus)

Nach Ad-hoc-Veröffentlichung:
- Unverzügliche Benachrichtigung aller gesoundeten Investoren, dass Information öffentlich ist
- Bestätigung, dass Handelsverbot aufgehoben ist
- Datum und Uhrzeit der Wall-Down-Kommunikation dokumentieren
- Investoren aus permanenter Insiderliste entfernen (Austrittsdatum eintragen)

### Schritt 5 – Aufbewahrung

- Alle Sounding-Protokolle, Wall-Crossing-Dokumente und Wall-Down-Bestätigungen:
 5 Jahre aufbewahren (Art. 18 Abs. 5 MAR analog)
- BaFin-Übermittlung auf Anfrage binnen 24 Stunden

## Red-Team-Fragen

- Wurden alle Wall-Crossing-Formalia vor der Informationsweitergabe erfüllt?
- Ist das Sounding-Skript vorab genehmigt und eingehalten worden?
- Sind alle gesoundeten Investoren in der Insiderliste erfasst?
- Wurde der Wall Down nach Ad-hoc-Veröffentlichung zeitnah und dokumentiert durchgeführt?
- Haben investierte Parteien während des Insiderstatus keine Transaktionen vorgenommen?
- Sind die Protokolle DVO-konform und vollständig?

## Ausgabeformat

Erzeuge:
1. Wall-Crossing-Protokoll (DVO-konformes Formular)
2. Sounding-Skript mit Non-Insider- und Insider-Versionen
3. Investor-Matrix: Wall-Crossing-Status × Datum × Bestätigung
4. Wall-Down-Benachrichtigungsschreiben (Vorlage)
5. Aufbewahrungsprotokoll

Belege ausschließlich mit: eur-lex.europa.eu, bafin.de, gesetze-im-internet.de, dejure.org.

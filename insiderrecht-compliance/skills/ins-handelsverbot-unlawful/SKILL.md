---
name: ins-handelsverbot-unlawful
description: "Ins 006 Handelsverbot Art14, Ins 007 Unlawful Disclosure: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 006 Handelsverbot Art14, Ins 007 Unlawful Disclosure

## Arbeitsbereich

Dieser Skill bündelt **Ins 006 Handelsverbot Art14, Ins 007 Unlawful Disclosure** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-006-handelsverbot-art14` | Prueft Insiderhandelsverbot nach Art. 14 MAR, abgrenzt Wissen von Absicht, analysiert Safe-Harbour-Ausnahmen und stellt Verteidigungsdokumentation sicher. |
| `ins-007-unlawful-disclosure` | Prueft unzulaessige Offenlegung von Insiderinformationen nach Art. 10 MAR und grenzt sie von zulaessiger Informationsweitergabe (Market Sounding, Beratung, M&A) ab. |

## Arbeitsweg

Für **Ins 006 Handelsverbot Art14, Ins 007 Unlawful Disclosure** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-006-handelsverbot-art14`

**Fokus:** Prueft Insiderhandelsverbot nach Art. 14 MAR, abgrenzt Wissen von Absicht, analysiert Safe-Harbour-Ausnahmen und stellt Verteidigungsdokumentation sicher.

# Insiderhandelsverbot nach Art. 14 MAR

## Rechtlicher Rahmen

Art. 14 VO (EU) 596/2014 (MAR) verbietet drei Verhaltensweisen: (1) den Erwerb oder die
Veräußerung von Finanzinstrumenten auf der Basis von Insiderinformationen (Insider Trading),
(2) die Empfehlung oder Verleitung Dritter zu solchen Geschäften (Tipping), (3) die unzulässige
Offenlegung von Insiderinformationen. Das Verbot gilt für jeden, der über Insiderinformationen
verfügt, unabhängig davon, wie er die Information erlangt hat (Primär- und Sekundärinsider).
Strafbewehrt durch § 119 WpHG (bis zu 5 Jahre Freiheitsstrafe).

Rechtsgrundlagen:
- Art. 14 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 8, 9, 10 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden Kap. II: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft, ob eine konkrete Transaktion oder Empfehlung gegen Art. 14 MAR verstößt,
und erstellt die Verteidigungsdokumentation für den Fall einer BaFin-Anfrage oder eines
Ermittlungsverfahrens. Er unterscheidet zwischen dem objektiven Tatbestand und den subjektiven
Elementen sowie den verfügbaren Safe-Harbour-Ausnahmen.

## Arbeitsprogramm

### Schritt 1 – Objektiver Tatbestand (Art. 8 MAR)

- Hat die handelnde Person zum Zeitpunkt der Transaktion über eine Insiderinformation verfügt?
- Handelt es sich um ein Finanzinstrument, auf das sich die Insiderinformation bezieht
 (oder ein verbundenes Derivat)?
- Wurde die Transaktion auf der Basis der Insiderinformation getätigt? (Kausalitätselement)
- Gilt auch für: Stornierung oder Änderung bestehender Aufträge auf der Basis von
 Insiderinformationen.

### Schritt 2 – Abgrenzung: Art. 9 MAR Safe Harbour

Prüfe, ob eine der Ausnahmen greift:
a) Legitime Ausübung regulärer Aufgaben: Transaktion war Teil der normalen Geschäftstätigkeit
 (z. B. Market Maker, Liquiditätssicherung)
b) Beschlossene Transaktion vor Erlangen der Insiderinformation (Art. 9 Abs. 3 MAR)
c) Rückkaufprogramm oder Kursstabilisierung nach DVO (EU) 2016/1052
d) Monetäre Politik, Staatsschulden, Klimapolitik (Art. 9 Abs. 2 MAR)
→ Für jeden Safe-Harbour-Tatbestand: Nachweis des relevanten Sachverhalts mit Zeitstempel.

### Schritt 3 – Tipping (Art. 10 MAR)

- Wurde die Insiderinformation an eine andere Person weitergegeben?
- Erfolgte die Weitergabe im Rahmen normaler Berufsausübung (z. B. Anwalt an Mandant,
 IR-Abteilung an Analyst im Rahmen von Market Sounding)?
- Wenn nein: Verstoß gegen Art. 10 MAR, ggf. auch Art. 14 lit. c MAR.

### Schritt 4 – Strafrecht (§ 119 WpHG)

- Tatbestand § 119 WpHG prüfen (vorsätzlich): Erwerb, Veräußerung, Empfehlung, Offenlegung
- Leichtfertigkeitsttatbestand § 119 Abs. 3 WpHG beachten
- Behördenkoordination: BaFin-Marktüberwachung meldet an Staatsanwaltschaft bei Verdacht

### Schritt 5 – Verteidigungsdokumentation

Erstelle für jede verdachtsauslösende Transaktion:
- Zeitstrahl: Wann hatte Person Kenntnis von der Insiderinformation? Wann wurde Transaktion
 beschlossen und ausgeführt?
- Handelsplan oder -strategie vor der Insiderinformation (z. B. Spar-/Investitionsplan)
- Nachweis, dass Entscheidung vor Kenntnis getroffen wurde
- Belege für Safe-Harbour-Tatbestand (falls zutreffend)

## Red-Team-Fragen

- Hatte die handelnde Person tatsächlich Zugang zur Insiderinformation?
- Kann der Kausalzusammenhang zwischen Insiderinformation und Transaktion widerlegt werden?
- Liegt ein Safe-Harbour-Tatbestand vor, und ist dieser lückenlos dokumentiert?
- Wurde die Transaktion auf der Basis eines vorgefassten Handelsplans ausgeführt?
- Wurde Tipping (Weitergabe an Dritte) ausgeschlossen oder sachgemäß dokumentiert?
- Gibt es Trading-Anomalien vor der Ad-hoc-Veröffentlichung, die BaFin-Aufmerksamkeit erregen?

## Ausgabeformat

Erzeuge:
1. Transaktions-Prüfprotokoll (Zeitstrahl, Wissensstand, Kausalitätsanalyse)
2. Safe-Harbour-Prüfmatrix
3. Verteidigungsmemo (für BaFin-Anfrage oder Ermittlungsverfahren)
4. Empfehlungen für Handelsüberwachung und Pre-Clearance-Verfahren

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, curia.europa.eu,
bgh.de, dejure.org, openjur.de.

## 2. `ins-007-unlawful-disclosure`

**Fokus:** Prueft unzulaessige Offenlegung von Insiderinformationen nach Art. 10 MAR und grenzt sie von zulaessiger Informationsweitergabe (Market Sounding, Beratung, M&A) ab.

# Unzulässige Offenlegung nach Art. 10 MAR

## Rechtlicher Rahmen

Art. 10 VO (EU) 596/2014 (MAR) verbietet die Offenlegung von Insiderinformationen an Dritte,
es sei denn, dies geschieht im Rahmen der normalen Ausübung einer Beschäftigung, eines Berufs
oder einer Aufgabe. Art. 11 MAR regelt Market Sounding als legale Ausnahme. Das Verbot gilt
für primäre und sekundäre Insider. Verletzung führt zur Strafbarkeit nach § 119 WpHG.

Rechtsgrundlagen:
- Art. 10 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 11 MAR (Market Sounding): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/960 (Market Sounding): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0960
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden Kap. III: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft, ob eine Informationsweitergabe als unzulässige Offenlegung nach Art. 10 MAR
qualifiziert oder unter eine Ausnahme fällt (normale Berufsausübung, Market Sounding, Due
Diligence in M&A-Prozessen). Er erstellt das Verteidigungsdossier für Übermittlungsvorgänge.

## Arbeitsprogramm

### Schritt 1 – Tatbestand der Offenlegung

- Welche Information wurde weitergegeben (Inhalt, Zeitpunkt, Medium)?
- War die Information zum Zeitpunkt der Weitergabe eine Insiderinformation nach Art. 7 MAR?
- An wen wurde die Information weitergegeben (Name, Funktion, Verhältnis zum Emittenten)?
- Auf welchem Wege (E-Mail, Telefonat, Meeting, Datenraum)?

### Schritt 2 – Ausnahme: Normale Berufsausübung (Art. 10 Abs. 1 MAR)

Prüfe, ob die Weitergabe im Rahmen der normalen Ausübung einer Beschäftigung, eines Berufs
oder einer Aufgabe erfolgte:
- Anwalt gibt Insiderinformation an Mandanten weiter (korrekt), aber nicht an Dritte
- Investmentbank führt Due Diligence für Mandanten durch (korrekt)
- Journalist recherchiert im öffentlichen Interesse (differenzierter Tatbestand)
Wichtig: Die Weitergabe muss für die Berufsausübung notwendig sein (Verhältnismäßigkeit).

### Schritt 3 – Market Sounding (Art. 11 MAR)

Market Sounding ist die Übermittlung von Insiderinformationen an potenzielle Investoren vor
Bekanntgabe einer Transaktion. Voraussetzungen:
- Vor der Sondierung: schriftliche Erklärung, dass Information Insiderinformation sein kann
- Einholung der Zustimmung zur Entgegennahme
- Protokoll der Sondierung (Inhalt, Datum, Teilnehmer)
- Aufhebung der Insiderposition des Investierten nach der Ad-hoc-Veröffentlichung
 (Wall Crossing Management)
Maßgebliche DVO: (EU) 2016/960.

### Schritt 4 – Due Diligence in M&A

- Weitergabe in einem NDA-gesicherten Datenraum ist erlaubt, wenn:
 a) Need-to-know-Prinzip eingehalten
 b) Alle Empfänger in Insiderliste eingetragen
 c) Vertraulichkeitsverpflichtung dokumentiert
- Bei gescheitertem Prozess: Insiderinformation darf nicht genutzt werden (Art. 8 MAR).

### Schritt 5 – Dokumentationspflichten

Für jeden Weitergabevorgang außerhalb der Ad-hoc-Veröffentlichung:
- Protokoll: Datum, Uhrzeit, Empfänger, Übertragungsmedium, Inhalt
- Belehrung des Empfängers über Insiderstatus
- Aufnahme in Insiderliste (Art. 18 MAR)

## Red-Team-Fragen

- War die weitergegebene Information tatsächlich eine Insiderinformation?
- War die Weitergabe für die Berufsausübung notwendig oder erfolgte sie freiwillig?
- Wurden Market-Sounding-Formalia (DVO 2016/960) eingehalten?
- Sind alle Empfänger in der Insiderliste erfasst und belehrt?
- Wurde beim M&A-Prozess sichergestellt, dass Informationen aus dem Datenraum nicht für
 Eigengeschäfte genutzt wurden?
- Gibt es Hinweise auf „Tipping" (gezielte Weitergabe zum Vorteil Dritter)?

## Ausgabeformat

Erzeuge:
1. Offenlegungs-Prüfprotokoll (Weitergabe × Tatbestand × Ausnahme × Ergebnis)
2. Market-Sounding-Protokoll (DVO-konform)
3. Wall-Crossing-Checklist
4. Verteidigungsdossier für BaFin-Anfragen

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org,
openjur.de, curia.europa.eu, bgh.de.

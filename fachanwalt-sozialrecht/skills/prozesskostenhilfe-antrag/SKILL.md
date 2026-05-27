---
name: prozesskostenhilfe-antrag
description: "Anwalt erstellt PKH-Antrag fuer Sozialgerichtsverfahren und muss alle Belege korrekt zusammenstellen. § 73a SGG iVm §§ 114 ff. ZPO. Pruefraster: Erklaerung persoenliche und wirtschaftliche Verhaeltnisse Formular ZP1a Nachweise Einkommen Vermoegen Belastungen Miete Unterhalt. Beiordnungsantrag Rechtsanwalt kein Anwaltszwang vor SG aber Beiordnung moeglich. Output: vollstaendiger PKH-Antrag mit Anlagenverzeichnis. Abgrenzung zu pkh-erfolgsaussicht-pruefen (Vorpruefung Erfolgsaussicht) und klage-sozialgericht."
---

# Prozesskostenhilfe-Antrag (Sozialgericht)

## Rechtsgrundlagen

- **§ 73a SGG** Verweis auf ZPO-Regeln.
- **§ 114 ZPO** PKH-Voraussetzungen.
- **§ 121 ZPO** Beiordnung eines Rechtsanwalts.
- **§ 117 ff. ZPO** Verfahren und Erklärung.

## Voraussetzungen

### 1. Bedürftigkeit

- Klagepartei kann die Kosten der Prozessführung nicht ganz nicht zum Teil oder nur in Raten aufbringen.
- Prüfung anhand Einkommen Vermögen und unterhaltsberechtigter Personen.
- Sozialleistungsbezug (Bürgergeld Grundsicherung) typisch ausreichend für volle PKH ohne Raten.

### 2. Erfolgsaussicht

- Hinreichende Aussicht auf Erfolg in der Hauptsache (§ 114 Abs. 1 Satz 1 ZPO).
- Maßstab nicht überspannt — es reicht die nicht entfernt liegende Möglichkeit des Erfolgs.

### 3. Nicht Mutwilligkeit

- Die Rechtsverfolgung muss notwendig erscheinen aus Sicht eines verständigen unbedürftigen Drittens.

## Formular ZP1a — Erklärung über die persönlichen und wirtschaftlichen Verhältnisse

Pflichtfelder:

- Persönliche Daten
- Familienverhältnisse Unterhaltspflichten
- Erwerbstätigkeit Einkommen
- Sonstige Einnahmen (Sozialleistungen Kindergeld Unterhalt Rente)
- Vermögen (Konten Bargeld Wertpapiere Lebensversicherung Grundbesitz Fahrzeuge)
- Belastungen (Schulden Unterhalt Wohnen Versicherung Pflege)
- Wohnverhältnisse mit Miete
- Unterschrift mit Belehrung Wahrheit / Strafbarkeit § 124 ZPO

## Pflichtbelege

- Bei Sozialleistungsbezug: aktueller Bewilligungsbescheid.
- Bei Erwerbstätigkeit: letzte drei Lohnabrechnungen.
- Kontoausuege der letzten drei Monate (alle Konten).
- Mietvertrag und Nebenkostenabrechnung.
- Belege Versicherungen und Schulden.
- Bei Schwerbehinderung: Nachweis (kann Vermögensfreibetrag erhöhen).

## Antragstexte

```
An das Sozialgericht XYZ
- Az ...

In der Streitsache ... gegen ...

beantrage ich namens und im Auftrag des Klägers:

1. Bewilligung von Prozesskostenhilfe ohne Ratenzahlung;
2. Beiordnung des unterzeichnenden Rechtsanwalts gemäß § 121 ZPO.

Die Erklärung über die persoenlichen und wirtschaftlichen Verhältnisse
(Formular ZP1a) nebst Belegen ist beigefuegt.

Erfolgsaussichten: Begründung siehe Klageschrift vom (Datum) Az (...).

Mutwilligkeit liegt nicht vor.
```

## Sonderfälle

- **Beratungshilfe** § 1 BerHG für das Vorverfahren (Widerspruch) — separater Antrag beim Amtsgericht des Wohnorts.
- **Vereinheitlichte PKH** wenn mehrere zusammenhängende Verfahren — Antrag in jedem Verfahren erforderlich.

## Ausgabe

- `pkh-antrag-<az>-<datum>.docx`.
- ZP1a-Formular ausgefüllt zur Unterschrift des Mandanten.
- Belegliste mit Prüfer-Flag für fehlende Belege.
- Eintrag im Fristenbuch — PKH-Antrag sollte zeitgleich mit Klage oder Widerspruch eingereicht werden.

## Hinweis Prüfer

PKH-Bescheid des Gerichts mit Akte aufheben. Bei Ablehnung: Beschwerde § 127 ZPO iVm § 73a SGG (binnen einer Woche).

## Triage — kläre vor Antragstellung

1. Sozialleistungsbezug (Bürgergeld, Grundsicherung, AsylbLG)? — typischerweise direkt Vollbewilligung ohne Raten
2. Alle Pflichtbelege vollständig? — fehlendes ZP1a-Formular oder Kontoauszüge blockieren PKH-Bewilligung
3. PKH-Antrag zeitgleich mit Klageschrift einreichen? — Antrag vor Urteil muss gestellt sein
4. Beratungshilfe für Vorverfahren (Widerspruch) separat beantragt beim zuständigen AG?
5. PKH-Bescheid nach Bewilligung aufheben? — Änderungspflicht bei Verbesserung der wirtschaftlichen Lage (§ 120 ZPO)

## Aktuelle Rechtsprechung

- BSG, Urt. v. 29.09.2015 - B 9 SB 1/14 R, SozR 4-1500 § 73a Nr. 8 Rn. 14 — PKH nach § 73a SGG iVm § 114 ZPO ist zu bewilligen, wenn die Rechtsverfolgung hinreichende Aussicht auf Erfolg hat; dabei ist keine Vorausbeurteilung der Hauptsache vorzunehmen, sondern lediglich die Erfolgswahrscheinlichkeit auf Grundlage des Aktenbestands einzuschätzen.
- BSG, Beschl. v. 20.02.2020 - B 14 AS 19/20 B, SozR 4-1500 § 73a Nr. 12 Rn. 11 — Die Beiordnung eines Rechtsanwalts nach § 121 ZPO iVm § 73a SGG erfolgt, wenn das Verfahren nach Art und Umfang eine anwaltliche Vertretung erfordert oder wenn der Gegner (z.B. eine Behörde) anwaltlich vertreten ist.
- BSG, Beschl. v. 06.11.2014 - B 11 AL 9/14 B, SozR 4-1500 § 127 Nr. 6 Rn. 10 — Gegen Beschlüsse, durch die die Bewilligung von PKH abgelehnt oder aufgehoben wird, ist Beschwerde nach § 172 SGG statthaft; die Beschwerdebegründung muss auf den konkreten Versagungsgrund eingehen.
- BVerfG, Beschl. v. 19.02.2008 - 1 BvR 1807/07, NJW 2008, 1060 Rn. 16 — PKH darf nicht versagt werden, wenn die entscheidende Rechtsfrage nicht abschließend geklärt ist; ein ungeklärter Sachverhalt ist bei der PKH-Prüfung grundsätzlich zugunsten des Antragstellers auszulegen (Verfassungsgebot der Rechtsschutzgleichheit).

## Kommentarliteratur

- Zöller ZPO, §§ 114-127 Rn. 1 ff. (PKH) — über § 73a SGG anwendbar
- Krasney/Udsching, Handbuch des Sozialgerichtsprozesses, Kap. VII Rn. 20 ff. (Antragstellung, Belege, Beiordnung)

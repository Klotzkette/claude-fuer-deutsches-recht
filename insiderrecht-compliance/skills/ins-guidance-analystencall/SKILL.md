---
name: ins-guidance-analystencall
description: "INS Guidance Analystencall: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# INS Guidance Analystencall

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **INS Guidance Analystencall** im Plugin Insiderrecht / Compliance (WpHG, MAR). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ins-031-guidance-update` | Prueft wann ein Guidance-Update (Prognoseaenderung) zur Insiderinformation wird, koordiniert Ad-hoc und schreibt den Prognose-Passus. |
| `ins-032-analystencall` | Sichert Analysten-Calls und Investorenkommunikation gegen Selective-Disclosure-Risiken und MAR-Verstoesse: Sprechregeln, Q&A-Pruefung und Post-Call-Protokoll. |

## Arbeitsweg

Im Plugin Insiderrecht / Compliance (WpHG, MAR) gilt für **INS Guidance Analystencall**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ins-031-guidance-update`

**Fokus:** Prueft wann ein Guidance-Update (Prognoseaenderung) zur Insiderinformation wird, koordiniert Ad-hoc und schreibt den Prognose-Passus.

# Guidance Update / Prognoseänderung – Insiderrecht

## Rechtlicher Rahmen

Eine wesentliche Änderung einer veröffentlichten Unternehmensprognose (Guidance) ist kurs-
relevant und kann eine Insiderinformation begründen. Die Pflicht zur Ad-hoc-Veröffentlichung
entsteht, sobald die Prognoseabweichung als präzise Information vorliegt – nicht erst beim
Quartals- oder Jahresbericht. Maßgeblich ist die Abweichung vom zuletzt kommunizierten Ausblick
und vom Analystenkonsensus.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 97 WpHG: https://www.gesetze-im-internet.de/wphg/__97.html
- BaFin-Emittentenleitfaden Kap. VI.2 (Prognoseänderungen): https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill identifiziert den Zeitpunkt, ab dem eine Prognoseänderung zur Insiderinformation
wird, und steuert die Ad-hoc-Veröffentlichung oder deren Koordination mit dem Quartalsbericht.

## Arbeitsprogramm

### Schritt 1 – Prognose-Gap-Analyse

- Aktuell veröffentlichte Prognose (zuletzt bestätigte Guidance)
- Aktuelle interne Erwartung (Controller-Forecast, CFO-Update)
- Analystenkonsensus (Bloomberg, Refinitiv)
- Gap-Berechnung: Differenz in absoluten Zahlen und Prozent
- Bewertung der Wesentlichkeit

### Schritt 2 – Präzisions- und Kursrelevanzprüfung

- Ist die Prognoseabweichung auf einer hinreichend sicheren Datenbasis?
 (Monats-Abschlüsse bestätigt vs. frühe Indikationen aus KPIs)
- Gilt die Information als präzise, wenn: Ergebnis des abgeschlossenen Quartals vorliegt
 oder durch belastbare Hochrechnung erhebliche Abweichung erkennbar ist
- Kursrelevanz ex ante: Vergleich mit Markterwartungen

### Schritt 3 – Koordination mit Berichtskalender

- Liegt der nächste Quartalsbericht in weniger als 10 Handelstagen?
 → Dann ggf. Bekanntgabe im Quartalsbericht möglich (restriktiv: nur wenn kein
 schuldhaftes Zögern)
- Liegt nächster Bericht in mehr als 10 Handelstagen?
 → Separate Ad-hoc-Pflicht, wenn wesentliche Abweichung vorliegt
- Praxis: Profit Warnings zeitnah mit eigenständiger Ad-hoc; keine Verzögerung

### Schritt 4 – Inhalt der Ad-hoc bei Prognoseänderung

- Vorherige Prognose (Zitat)
- Neue Prognose oder Bandbreite
- Ursachen (präzise: konkrete Faktoren, keine Allgemeinplätze)
- Ausblick und weitere Maßnahmen

### Schritt 5 – Eigengeschäfte und Insiderliste

- Personenkreis, der die neue interne Prognose kennt: In Insiderliste aufnehmen
- PDMR-Eigengeschäfte in der Phase bis zur Ad-hoc: Prüfung auf Art. 14 MAR-Verletzung
- Nach Ad-hoc: Insiderliste schließen (Austrittsdaten)

## Red-Team-Fragen

- Wurde der frühestmögliche Zeitpunkt identifiziert, ab dem die Prognoseabweichung
 präzise war?
- Wurde die Wartezeit bis zum Quartalsbericht sachlich begründet oder war sie Verzögerung?
- Wurden PDMR-Eigengeschäfte im Zeitraum der Insiderinformation geprüft?
- Enthält die Ad-hoc eine konkrete neue Prognose (nicht nur „wesentliche Abweichung")?

## Ausgabeformat

Erzeuge:
1. Prognose-Gap-Analyse (Tabelle: Guidance × Konsensus × Interne Erwartung × Gap)
2. Zeitplan (Entstehungszeitpunkt der Insiderinformation × nächster Quartalsbericht × Ad-hoc)
3. Ad-hoc-Entwurf Prognoseänderung
4. PDMR-Eigengeschäfts-Prüfprotokoll

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## 2. `ins-032-analystencall`

**Fokus:** Sichert Analysten-Calls und Investorenkommunikation gegen Selective-Disclosure-Risiken und MAR-Verstoesse: Sprechregeln, Q&A-Pruefung und Post-Call-Protokoll.

# Analysten-Calls und Investorenkommunikation – Selective Disclosure

## Rechtlicher Rahmen

Die selektive Weitergabe von Insiderinformationen an Analysten oder Investoren ist nach
Art. 10 MAR verboten (unzulässige Offenlegung) und kann einen Verstoß gegen Art. 14 MAR
darstellen (Tipping). Emittenten müssen sicherstellen, dass in Analysten-Calls, Roadshows
und Einzelgesprächen keine nicht-öffentlichen kursrelevanten Informationen vermittelt werden.
Selective Disclosure verstößt auch gegen Equal Treatment-Grundsätze (Art. 4 MAR).

Rechtsgrundlagen:
- Art. 10, 14 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 4 MAR (Gleiche Behandlung): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- BaFin-Emittentenleitfaden Kap. III: https://www.bafin.de/dok/8252648
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html

## Ziel dieses Skills

Dieser Skill stellt sicher, dass Analysten-Calls und Investorenkommunikation frei von Selective
Disclosure sind und schützt den Emittenten vor MAR-Verstößen in der alltäglichen IR-Kommunikation.

## Arbeitsprogramm

### Schritt 1 – Pre-Call-Prüfung

Vor jedem Analysten-Call, Investorengespräch oder Roadshow-Termin:
- Liegt eine aktuelle Insiderinformation vor? (Mit Compliance abstimmen)
- Wenn ja: Gespräch absagen oder auf rein öffentliche Informationen beschränken
- Erstelle Liste der Themen, die NICHT besprochen werden dürfen

### Schritt 2 – Sprechregeln (Speaker-Guidelines)

- IR-Team und Vorstand: Nur auf Basis von veröffentlichten Informationen (Jahresbericht,
 Quartalsberichte, Ad-hoc-Mitteilungen) antworten
- Verboten: Kommentierung von Marktgerüchten zu nicht-öffentlichen Transaktionen
- Erlaubt: Erläuterung öffentlicher Informationen, Branchentrends, allgemeiner Strategie
- „No-Comment" ist erlaubt und besser als eine Selective Disclosure

### Schritt 3 – Q&A-Vorbereitung und Screening

- Erstelle vor dem Call eine Liste erwarteter Fragen und Standard-Antworten
- Screening: Welche Antworten könnten als Konfirmation von Insiderinformationen
 verstanden werden?
- Klärung: Bestätigt eine Antwort eine bestehende Insiderinformation? → Nicht beantworten

### Schritt 4 – Protokollierung

- Alle Analysten-Calls aufzeichnen (Einwilligung der Teilnehmer einholen)
- Protokoll oder Transkript anfertigen
- Aufbewahrung 5 Jahre
- Nachbearbeitung: Wurden unbeabsichtigt kursrelevante Informationen kommuniziert?

### Schritt 5 – Post-Call-Pflichten

Wenn im Call versehentlich eine Insiderinformation offengelegt wurde:
- Sofortige Einschaltung von Compliance
- Prüfung: Ad-hoc-Pflicht nach Art. 17 MAR (Öffentlichkeit herstellen)
- Prüfung: Hat der informierte Analyst Transaktionen auf Basis dieser Information getätigt?
 → Meldung an BaFin erforderlich

## Red-Team-Fragen

- Wurde vor dem Call geprüft, ob eine aktuelle Insiderinformation vorliegt?
- Haben IR-Mitarbeiter Sprechregeln und den Umgang mit heiklen Fragen schriftlich
 dokumentiert?
- Wurde der Call vollständig aufgezeichnet und archiviert?
- Gibt es einen Post-Call-Review-Prozess für Compliance?
- Werden Einzelgespräche mit Investoren (One-on-Ones) genauso behandelt wie öffentliche Calls?

## Ausgabeformat

Erzeuge:
1. Pre-Call-Checkliste (Insiderinformations-Status, Themen-Sperrlist)
2. Sprechregeln-Leitfaden für IR und Vorstand
3. Q&A-Screening-Protokoll
4. Post-Call-Compliance-Report-Vorlage

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

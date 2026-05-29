---
name: fachanwalt-bank-kapitalmarktrecht-schufa-loeschungsanspruch
description: "Workflow-Skill zu fachanwalt bank kapitalmarktrecht schufa loeschungsanspruch. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# SCHUFA-Löschungsanspruch

## Zweck

Mandate von Verbrauchern mit unrechtmaessigen SCHUFA-Eintraegen. Auskunft, Widerspruch, Löschung, Schadensersatz.

## 1) Eingangs-Abfrage

1. Welcher Eintrag? Negativeintrag (Mahnverfahren, Inkasso, fruchtloseVollstreckung) oder Score-Stelle?
2. Forderung **unstreitig faellig** oder **bestritten**?
3. Wer hat Eintrag gemeldet — Bank, Inkasso, Telekom?
4. Wann eingetragen — bei Negativeintrag Restschuldbefreiung-relevant?
5. SCHUFA-Auskunft bereits vorhanden?
6. Konkrete Folgen (Kredit-Ablehnung, Mietkaution-Problem)?

## 2) Voraussetzungen Negativeintrag

### Schutzgesetz-Vorgaben § 31 BDSG / Art. 6 DSGVO

- **Unstreitig**: Forderung darf nicht im Streit stehen
- **Faellig**: Mahn-Datum + 4 Wochen
- **Zwei Mahnungen** mit 4-Wochen-Abstand
- **Vorab-Hinweis** der Eintragung (mind. 4 Wochen vor)

### Bei Insolvenz

- Restschuldbefreiung -> Löschungs-Anspruch
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- 3-Jahres-Frist nach Restschuldbefreiung verkürzt durch Vergleichs-Urteil 2023

## 3) Klassische Fehler-Konstellationen

### Konstellation A: Forderung bestritten

- Kunde hat Rechnung bestritten (z.B. Telekom-Streit)
- Eintrag dennoch -> rechtswidrig
- Löschungs-Anspruch + Schadensersatz

### Konstellation B: Verfristet

- Eintrag nach 4 Jahren noch da (sollte nach 3 Jahren geloescht)
- Löschungs-Anspruch

### Konstellation C: Insolvenz-Bezug

- Trotz Restschuldbefreiung Eintrag bleibt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Konstellation D: Score ohne nachvollziehbare Grundlage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Recht auf Erklärung, manuelle Prüfung

## 4) Workflow Löschung

### Schritt 1 — Auskunft Art. 15 DSGVO

- SCHUFA-Selbstauskunft kostenlos einmal jaehrlich
- Online über meineschufa.de
- Erhalt: alle gespeicherten Daten + Score

### Schritt 2 — Widerspruch / Löschungsantrag

- An SCHUFA: Antrag Art. 16 (Berichtigung), Art. 17 (Löschung), Art. 21 (Widerspruch)
- An Datenübermittler (Bank, Inkasso, Telekom): Pruefantrag

### Schritt 3 — Bei Ablehnung Beschwerde

- BfDI / Landes-Datenschutzbehoerde
- Beschwerde kostenlos, Frist 1 Monat

### Schritt 4 — Klage

- LG Sitz SCHUFA (Wiesbaden)
- Klage auf Löschung + Schadensersatz Art. 82 DSGVO
- Streitwert: bei reinem Löschungsanspruch 500-2.000 EUR; bei Schadensersatz aufschlagen

## 5) Schadensersatz Art. 82 DSGVO

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- DSGVO-Schadensersatz auch bei nicht-materiellem Schaden
- Kontrollverlust über Daten ausreichend
- Tendenz Höhe: 100-1.500 EUR pro Fall

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Schaden auch ohne konkreten finanziellen Schaden möglich
- Sorge / Aerger reicht aus

### Praxis-Bewertung

- Kredit-Ablehnung wegen falschem Eintrag: 1.000-2.500 EUR
- Reine Score-Verschlechterung: 200-500 EUR
- Wiederholte Falsch-Eintraege: 2.000-5.000 EUR

## 6) Typische Honorar-Strategie

- **Pauschal** je Eintrag (500-1.000 EUR + MwSt.)
- **Erfolgs-Aufschlag** bei Schadensersatz (15-30 %)
- **Rechtsschutz-Versicherung** typisch zuschussfähig (Bereich "Schadensersatz / Datenschutz")

## 7) Prüfliste

- [ ] SCHUFA-Auskunft vorhanden?
- [ ] Datenübermittler identifiziert?
- [ ] Forderung-Hintergrund (Vertrag, Mahnungen, Frist)?
- [ ] Vorab-Hinweis durch Datenübermittler erfolgt?
- [ ] Eintragungs-Datum vs. Geltungsdauer-Grenze?
- [ ] Bei Insolvenz: Restschuldbefreiung-Datum?
- [ ] Konkreter Schaden dokumentiert (Kreditablehnung, Mietkaution)?

## 8) Anschluss

- `fachanwalt-bank-kapitalmarktrecht-kreditkuendigung-490-bgb` — bei verbundener Kredit-Konstellation
- `datenschutzrecht/skills/dsgvo-auskunft` — für formelle Anträge nach Art. 15 DSGVO
- `forderungsmanagement-klagewerkstatt` — bei Inkasso-Streit-Hintergrund

## 9) Aktuelle BGH-/EuGH-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vertiefung: Rechtsprechung, Triage und Output-Template

### Triage — Bevor losgelegt wird, klaere:

1. Ist die Forderung unbestritten oder war sie jemals bestritten? → Bestrittene Forderung = rechtswidriger Eintrag.
2. Wurden zwei qualifizierte Mahnungen mit 4-Wochen-Abstand und SCHUFA-Hinweis versandt? → Fehler = rechtswidrig.
3. Liegt der Eintrag mehr als 3 Jahre zurueck? → Loeschungspflicht nach § 31 BDSG.
4. Besteht Restschuldbefreiung? → Pflicht zur Loeschung (BGH 2024).
5. Gibt es konkrete Schaeden (Kreditablehnung, erhoehter Zinssatz)? → Art. 82 DSGVO Schadensersatz pruefen.

### Erweiterte Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Kette SCHUFA-Loeschung
- Art. 16, 17 DSGVO — Berichtigung und Loeschung
- Art. 22 DSGVO — Automatisierte Einzelentscheidung (Score)
- Art. 82 DSGVO — Schadensersatz bei DSGVO-Verstoss
- § 31 BDSG — Scoring-Regelung (Auskunfteien)
- Art. 77, 79 DSGVO — Beschwerde / Klage

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Output-Template Loeschungsklage
**Adressat:** Landgericht [ORT] — Tonfall: sachlich-juristisch

```
An das Landgericht [ORT]
[Anschrift]

K L A G E

des/der [NAME MANDANT], [ADRESSE]
- Klaeger/in -

gegen

SCHUFA Holding AG, Kormoranweg 5, 65201 Wiesbaden
- Beklagte -

und

[GLAEUBIGER / INKASSO-UNTERNEHMEN], [ANSCHRIFT]
- weitere Beklagte -

wegen Loeschung und Schadensersatz (DSGVO)

Wir beantragen:
1. Die Beklagten werden verurteilt, den Negativeintrag zu
   [NAME], [GEBURTSDATUM] vom [DATUM EINTRAG] betreffend
   Forderung [BEZEICHNUNG] bei der SCHUFA zu loeschen.
2. Die Beklagten werden verurteilt, an den Klaeger
   EUR [BETRAG] immateriellen Schadensersatz gemass
   Art. 82 DSGVO zu zahlen.

Begruendung:
[Fehler beim Eintrag: bestrittene Forderung /
fehlende Mahnung / abgelaufene Frist]

Beweismittel:
- SCHUFA-Selbstauskunft (Anlage K1)
- Bestreitungsschreiben Mandant (Anlage K2)
- Kreditablehnungsschreiben (Anlage K3)

[Rechtsanwalt/-anwaeltin]
```

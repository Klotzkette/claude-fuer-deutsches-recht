---
name: annullierung-oder-verspaetung-einordnen
description: "Workflow-Skill zu annullierung oder verspaetung einordnen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# Annullierung Verspätung oder Nichtbeförderung einordnen

## Drei Hauptkategorien

### 1. Annullierung (Art. 5 VO 261/2004)

Der **geplante Flug findet nicht statt** — die Airline streicht ihn. Indikatoren:

- Mitteilung der Airline "Flug annulliert / cancelled".
- Kein Flug mit der konkreten **Flugnummer und Datum** ist abgehoben.
- Passagiere werden auf einen anderen Flug umgebucht oder bekommen die Erstattung.

**Auch Annullierung** auch wenn der Flug am **nächsten Tag mit gleicher Flugnummer** stattfindet (zwei Indizien für dieselbe Wertung):

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Rechtsprechung live prüfen

Der **geplante Flug findet statt**, aber:

- **Mehr als zwei Stunden Verspätung** bei kurzen Strecken oder **mehr als drei Stunden** bei langen Strecken bei Abflug = Betreuungsleistungen Art. 9 VO 261/2004 (Verpflegung Telefon Hotel etc.).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Wichtig**: Maßgeblich ist die **Ankunftsverspätung am Endziel** — nicht die Abflugverspätung.

### 3. Nichtbeförderung (Art. 4 VO 261/2004)

- Klassisch **Overbooking** — die Airline bucht mehr Plätze als verfügbar.
- Die Airline verweigert die Beförderung gegen den Willen des Passagiers.
- Voraussetzung: rechtzeitiges Erscheinen am Check-in (in der Regel 45 Minuten vor Abflug).
- Folge: Ausgleichsanspruch wie bei Annullierung + Wahl Erstattung oder anderweitige Beförderung.

**Nicht Nichtbeförderung** wenn Passagier ausgeschlossen wird wegen:
- Fehlender Reisedokumente (Pass Visum).
- Sicherheitsbedenken.
- Fluguntauglichkeit (medizinisch).

## Sonderfälle

### Anschlussflug ohne Anschluss

Wenn der **erste Flug innerhalb der EU mit derselben Buchung** verspätet ist und der **Anschlussflug verpasst** wird:

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anspruch besteht auch wenn der erste Flug innerhalb der drei-Stunden-Schwelle landete, der Anschlussflug aber verpasst wurde und Endziel mit mehr als drei Stunden Verspätung erreicht wird.

### Ersatzflug am nächsten Tag

- **Annullierung** wenn Ersatzflug eine andere Flugnummer hat oder gravierende Änderungen aufweist.
- **Verspätung** wenn derselbe Flug nur verschoben und die Identität bewahrt ist (z. B. gleiches Flugzeug gleiche Crew gleiche Strecke).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Vorverlegung des Flugs

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Umbuchung auf anderen Flug ohne Zustimmung des Passagiers

- Falls die Airline den Passagier auf einen anderen Flug umbucht (Codeshare anderen Tag andere Stadt): prüfen ob das wesentliche Änderung ist und damit als Annullierung gewertet wird.

## Prüfraster

```
1. Hat der geplante Flug exakt wie geplant stattgefunden?
   - Ja → keine Annullierung; Verspätung prüfen (Schritt 2)
   - Nein → Schritt 3

2. Welche Ankunftsverspätung am Endziel?
   - 0 bis unter 3 Stunden → keinen Ausgleichsanspruch nach VO 261;
     Betreuungsleistungen Art. 9 ggf. bei Abflugverspätung
   - 3 Stunden oder mehr → Ausgleichsanspruch wie bei Annullierung
     (EuGH Sturgeon)

3. Wie wurde der Flug geändert?
   - komplett ausgefallen → Annullierung
   - durchgeführt aber gravierend abweichend (Datum Flugnummer
     Zeitpunkt mehr als drei Stunden) → Annullierung
   - durchgeführt mit geringerer Verspätung → Verspätung prüfen
   - Passagier wurde am Gate abgewiesen trotz gültigem Ticket
     → Nichtbefoerderung

4. Stehen außergewöhnliche Umstaende entgegen?
   → Skill `ausnahmen-aussergewoehnliche-umstaende-pruefen`
```

## Ausgabe

- `einordnung.md` mit:
  - rechtlicher Kategorie (Annullierung / Verspätung / Nichtbeförderung)
  - Begründung mit Verweis auf Norm und EuGH-Rechtsprechung
  - Höhe der voraussichtlichen Ausgleichszahlung (verweist auf Skill `distanz-und-ausgleich-berechnen`)
  - offenen Fragen zur Klärung mit dem Mandanten
- Hinweis auf Skill `ausnahmen-aussergewoehnliche-umstaende-pruefen` zur Prüfung der Ausnahmen.

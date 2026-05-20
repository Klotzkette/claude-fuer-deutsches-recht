---
name: ausnahmen-aussergewoehnliche-umstaende-pruefen
description: Prueft die Einrede aussergewoehnliche Umstaende nach Art. 5 Abs. 3 VO 261/2004. Differenziert zwischen Wetter Vulkanasche Vogelschlag Streik Flugsicherung Streik der eigenen Mitarbeiter wilder Streik technischem Defekt politischer Instabilitaet Sicherheitsrisiko medizinischem Notfall. EuGH-Rechtsprechung Wallentin-Hermann Pesokova Kruesemann Airhelp SAS Moens. Pflichtkriterium auch zumutbare Massnahmen zur Vermeidung. Erzeugt Subsumtion mit Pinpoint und Gegenargumenten.
---

# Aussergewoehnliche Umstaende pruefen (Art. 5 Abs. 3 VO 261/2004)

## Norm

Art. 5 Abs. 3 VO 261/2004: Ein ausfuehrendes Luftfahrtunternehmen ist nicht verpflichtet Ausgleichszahlungen zu leisten wenn es nachweisen kann dass die Annullierung **auf aussergewoehnliche Umstaende zurueckgeht** die sich auch dann nicht haetten vermeiden lassen wenn alle zumutbaren Massnahmen ergriffen worden waeren.

**Beweislast** liegt bei der Airline (Wortlaut „nachweisen kann"). Pauschale Behauptung reicht nicht.

## Zwei-Stufen-Pruefung

### Stufe 1 — Liegt ueberhaupt ein aussergewoehnlicher Umstand vor?

Definition aus EuGH-Rechtsprechung (Wallentin-Hermann C-549/07 staendig): Aussergewoehnlich sind Vorkommnisse die **nicht Teil der normalen Ausuebung der Taetigkeit** des betroffenen Luftfahrtunternehmens sind und **von ihm nicht tatsaechlich beherrschbar** sind.

### Stufe 2 — Haetten zumutbare Massnahmen den Schaden verhindert?

EuGH C-294/10 (Eglitis Ratnieks) und folgende: Auch wenn ein aussergewoehnlicher Umstand vorliegt muss die Airline darlegen dass **alle zumutbaren Massnahmen** zur Vermeidung der Auswirkungen ergriffen wurden (Ersatzflugzeug Crew-Rotation Reserve-Crew Umbuchung).

## Katalog typischer Sachverhalte

### Ja regelmaessig aussergewoehnlich

| Sachverhalt | Rspr. |
|---|---|
| Vulkanasche / Naturkatastrophe | EuGH staendig |
| Sicherheitsrisiken Terrordrohung | EuGH staendig |
| Streik der Flugsicherung (externer Dienstleister) | EuGH staendig |
| Vogelschlag (Bird Strike) | EuGH, Urt. v. 04.05.2017 — C-315/15 (Pesokova) |
| Treibstoff Kerosin auf der Landebahn | EuGH, Urt. v. 26.06.2019 — C-159/18 (Moens) |
| Fluchtversuche Passagiere mit Behinderung des Bordbetriebs | je Einzelfall |
| Sabotage an der Maschine durch Dritte | EuGH C-501/17 |
| Krieg Embargo Luftraumsperrung | EuGH staendig |

### Nein regelmaessig keine aussergewoehnlichen Umstaende

| Sachverhalt | Rspr. |
|---|---|
| Technischer Defekt der waehrend des Routinebetriebs auftritt | EuGH, Urt. v. 22.12.2008 — C-549/07 (Wallentin-Hermann) |
| Pannen die Folge eines verdeckten Konstruktionsfehlers sind | EuGH C-257/14 (van der Lans) — auch das ist Teil normalen Betriebs |
| Streik der eigenen Mitarbeiter (wilder Streik) | EuGH, Urt. v. 17.04.2018 — C-195/17 ua (Kruesemann) |
| Personalmangel / Krankenstand Crew | st. Rspr. — Teil normalen Betriebs |
| Computer-Stoerungen des Buchungssystems | st. Rspr. |
| Wartung / TBO-Erreichung | Routine |

### Differenziert

| Sachverhalt | Differenzierung |
|---|---|
| Streik der eigenen Mitarbeiter durch Gewerkschaft | EuGH, Urt. v. 23.03.2021 — C-28/20 (Airhelp / SAS): kann aussergewoehnlich sein **aber** Airline muss alle zumutbaren Massnahmen ergriffen haben |
| Wetter | bei wirklich extremen Bedingungen ja; bei normalen Wintern oder gemaessigtem Schneefall nein |
| Slot-Verschiebung Flugverkehrsleitung | je nach Ursache (kapazitaetsbezogen vs sicherheitsbezogen) |

## Pruefraster

```
Frage 1: Welche Begruendung hat die Airline angegeben?
  - Keine Begruendung → Beweislast nicht erfuellt → Anspruch erhalten
  - Pauschale Begruendung ohne Detail → Beweislast nicht erfuellt → Anspruch erhalten

Frage 2: Faellt der angegebene Sachverhalt in den Katalog
„regelmaessig aussergewoehnlich"?
  - Nein → Anspruch erhalten; ggf. Sachverhalt kategorisieren als
    technischen Defekt
  - Ja → Stufe 2

Frage 3: Hat die Airline alle zumutbaren Massnahmen ergriffen?
  - Eckdaten: rechtzeitige Information Ersatzflugzeug Reserve-Crew
    Umbuchung auf andere Airline Hotel
  - Wenn nicht dargelegt: Beweislast nicht erfuellt → Anspruch erhalten

Frage 4: Kausalitaet — beruht die Annullierung tatsaechlich auf dem
aussergewoehnlichen Umstand?
  - Folgeverspaetungen aus dem Vortag werden regelmaessig nicht mehr
    als aussergewoehnlich gewertet (EuGH-Verfahren zur kettenartigen
    Verspaetung)
```

## Gegenargumente bei typischen Airline-Standardausreden

Siehe Skill `airline-standardausreden-pruefen` mit detaillierten Standardgegenargumenten.

## Ausgabe

- `aussergewoehnlich-pruefung.md` mit:
  - Begruendung der Airline (Zitat)
  - Subsumtion unter Katalog
  - Pruefung zumutbarer Massnahmen
  - Pinpoint-Zitate EuGH-Rechtsprechung
  - Ergebnis (Anspruch erhalten / Anspruch entfaellt / weitere Sachverhaltsaufklaerung noetig)
- Hinweis: Bei strittiger Beweisfrage ist die Beweislast der Airline ein wichtiger Hebel.

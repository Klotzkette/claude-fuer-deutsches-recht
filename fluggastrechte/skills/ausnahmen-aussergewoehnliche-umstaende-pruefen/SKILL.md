---
name: ausnahmen-aussergewoehnliche-umstaende-pruefen
description: "Prueft die Einrede aussergewoehnliche Umstaende nach Art. 5 Abs. 3 VO 261/2004. Differenziert zwischen Wetter Vulkanasche Vogelschlag Streik Flugsicherung Streik der eigenen Mitarbeiter wilder Streik technischem Defekt politischer Instabilitaet Sicherheitsrisiko medizinischem Notfall. EuGH-Rechtsprechung Wallentin-Hermann Pesokova Kruesemann Airhelp SAS Moens. Pflichtkriterium auch zumutbare Massnahmen zur Vermeidung. Erzeugt Subsumtion mit Pinpoint und Gegenargumenten."
---

# Außergewöhnliche Umstände prüfen (Art. 5 Abs. 3 VO 261/2004)

## Norm

Art. 5 Abs. 3 VO 261/2004: Ein ausführendes Luftfahrtunternehmen ist nicht verpflichtet Ausgleichszahlungen zu leisten wenn es nachweisen kann dass die Annullierung **auf außergewöhnliche Umstände zurückgeht** die sich auch dann nicht hätten vermeiden lassen wenn alle zumutbaren Maßnahmen ergriffen worden waeren.

**Beweislast** liegt bei der Airline (Wortlaut „nachweisen kann"). Pauschale Behauptung reicht nicht.

## Zwei-Stufen-Prüfung

### Stufe 1 — Liegt überhaupt ein außergewöhnlicher Umstand vor?

Definition aus EuGH-Rechtsprechung (Wallentin-Hermann C-549/07 ständig): Außergewöhnlich sind Vorkommnisse die **nicht Teil der normalen Ausübung der Tätigkeit** des betroffenen Luftfahrtunternehmens sind und **von ihm nicht tatsächlich beherrschbar** sind.

### Stufe 2 — Hätten zumutbare Maßnahmen den Schaden verhindert?

EuGH C-294/10 (Eglitis Ratnieks) und folgende: Auch wenn ein außergewöhnlicher Umstand vorliegt muss die Airline darlegen dass **alle zumutbaren Maßnahmen** zur Vermeidung der Auswirkungen ergriffen wurden (Ersatzflugzeug Crew-Rotation Reserve-Crew Umbuchung).

## Katalog typischer Sachverhalte

### Ja regelmäßig außergewöhnlich

| Sachverhalt | Rspr. |
|---|---|
| Vulkanasche / Naturkatastrophe | EuGH ständig |
| Sicherheitsrisiken Terrordrohung | EuGH ständig |
| Streik der Flugsicherung (externer Dienstleister) | EuGH ständig |
| Vogelschlag (Bird Strike) | EuGH, Urt. v. 04.05.2017 — C-315/15 (Pesokova) |
| Treibstoff Kerosin auf der Landebahn | EuGH, Urt. v. 26.06.2019 — C-159/18 (Moens) |
| Fluchtversuche Passagiere mit Behinderung des Bordbetriebs | je Einzelfall |
| Sabotage an der Maschine durch Dritte | EuGH C-501/17 |
| Krieg Embargo Luftraumsperrung | EuGH ständig |

### Nein regelmäßig keine außergewöhnlichen Umstände

| Sachverhalt | Rspr. |
|---|---|
| Technischer Defekt der während des Routinebetriebs auftritt | EuGH, Urt. v. 22.12.2008 — C-549/07 (Wallentin-Hermann) |
| Pannen die Folge eines verdeckten Konstruktionsfehlers sind | EuGH C-257/14 (van der Lans) — auch das ist Teil normalen Betriebs |
| Streik der eigenen Mitarbeiter (wilder Streik) | EuGH, Urt. v. 17.04.2018 — C-195/17 ua (Kruesemann) |
| Personalmangel / Krankenstand Crew | st. Rspr. — Teil normalen Betriebs |
| Computer-Störungen des Buchungssystems | st. Rspr. |
| Wartung / TBO-Erreichung | Routine |

### Differenziert

| Sachverhalt | Differenzierung |
|---|---|
| Streik der eigenen Mitarbeiter durch Gewerkschaft | EuGH, Urt. v. 23.03.2021 — C-28/20 (Airhelp / SAS): kann außergewöhnlich sein **aber** Airline muss alle zumutbaren Maßnahmen ergriffen haben |
| Wetter | bei wirklich extremen Bedingungen ja; bei normalen Wintern oder gemäßigtem Schneefall nein |
| Slot-Verschiebung Flugverkehrsleitung | je nach Ursache (kapazitätsbezogen vs sicherheitsbezogen) |

## Prüfraster

```
Frage 1: Welche Begründung hat die Airline angegeben?
  - Keine Begründung → Beweislast nicht erfüllt → Anspruch erhalten
  - Pauschale Begründung ohne Detail → Beweislast nicht erfüllt → Anspruch erhalten

Frage 2: Faellt der angegebene Sachverhalt in den Katalog
„regelmäßig außergewöhnlich"?
  - Nein → Anspruch erhalten; ggf. Sachverhalt kategorisieren als
    technischen Defekt
  - Ja → Stufe 2

Frage 3: Hat die Airline alle zumutbaren Maßnahmen ergriffen?
  - Eckdaten: rechtzeitige Information Ersatzflugzeug Reserve-Crew
    Umbuchung auf andere Airline Hotel
  - Wenn nicht dargelegt: Beweislast nicht erfüllt → Anspruch erhalten

Frage 4: Kausalitaet — beruht die Annullierung tatsächlich auf dem
außergewöhnlichen Umstand?
  - Folgeverspätungen aus dem Vortag werden regelmäßig nicht mehr
    als außergewöhnlich gewertet (EuGH-Verfahren zur kettenartigen
    Verspätung)
```

## Gegenargumente bei typischen Airline-Standardausreden

Siehe Skill `airline-standardausreden-pruefen` mit detaillierten Standardgegenargumenten.

## Ausgabe

- `aussergewoehnlich-pruefung.md` mit:
  - Begründung der Airline (Zitat)
  - Subsumtion unter Katalog
  - Prüfung zumutbarer Maßnahmen
  - Pinpoint-Zitate EuGH-Rechtsprechung
  - Ergebnis (Anspruch erhalten / Anspruch entfaellt / weitere Sachverhaltsaufklärung noetig)
- Hinweis: Bei strittiger Beweisfrage ist die Beweislast der Airline ein wichtiger Hebel.

---
name: ausnahmen-aussergewoehnliche-umstaende-pruefen
description: "Workflow-Skill zu ausnahmen aussergewoehnliche umstaende pruefen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# Außergewöhnliche Umstände prüfen (Art. 5 Abs. 3 VO 261/2004)

## Norm

Art. 5 Abs. 3 VO 261/2004: Ein ausführendes Luftfahrtunternehmen ist nicht verpflichtet Ausgleichszahlungen zu leisten wenn es nachweisen kann dass die Annullierung **auf außergewöhnliche Umstände zurückgeht** die sich auch dann nicht hätten vermeiden lassen wenn alle zumutbaren Maßnahmen ergriffen worden waeren.

**Beweislast** liegt bei der Airline (Wortlaut "nachweisen kann"). Pauschale Behauptung reicht nicht.

## Zwei-Stufen-Prüfung

### Stufe 1 — Liegt überhaupt ein außergewöhnlicher Umstand vor?

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Stufe 2 — Hätten zumutbare Maßnahmen den Schaden verhindert?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Katalog typischer Sachverhalte

### Ja regelmäßig außergewöhnlich

| Sachverhalt | Rspr. |
|---|---|
| Vulkanasche / Naturkatastrophe | EuGH ständig |
| Sicherheitsrisiken Terrordrohung | EuGH ständig |
| Streik der Flugsicherung (externer Dienstleister) | EuGH ständig |
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Fluchtversuche Passagiere mit Behinderung des Bordbetriebs | je Einzelfall |
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Krieg Embargo Luftraumsperrung | EuGH ständig |

### Nein regelmäßig keine außergewöhnlichen Umstände

| Sachverhalt | Rspr. |
|---|---|
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Personalmangel / Krankenstand Crew | st. Rspr. — Teil normalen Betriebs |
| Computer-Störungen des Buchungssystems | st. Rspr. |
| Wartung / TBO-Erreichung | Routine |

### Differenziert

| Sachverhalt | Differenzierung |
|---|---|
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Wetter | bei wirklich extremen Bedingungen ja; bei normalen Wintern oder gemäßigtem Schneefall nein |
| Slot-Verschiebung Flugverkehrsleitung | je nach Ursache (kapazitätsbezogen vs sicherheitsbezogen) |

## Prüfraster

```
Frage 1: Welche Begründung hat die Airline angegeben?
  - Keine Begründung → Beweislast nicht erfüllt → Anspruch erhalten
  - Pauschale Begründung ohne Detail → Beweislast nicht erfüllt → Anspruch erhalten

Frage 2: Faellt der angegebene Sachverhalt in den Katalog
"regelmäßig außergewöhnlich"?
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

---
<!-- AUDIT 27.05.2026 bundle_004 -->
**Halluzinations-Audit 27.05.2026**

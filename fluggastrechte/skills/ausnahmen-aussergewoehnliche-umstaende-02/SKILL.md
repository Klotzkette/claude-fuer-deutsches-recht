---
name: ausnahmen-aussergewoehnliche-umstaende-02
description: "Prüfungslinie für ausnahmen aussergewoehnliche umstaende pruefen im Fluggastrechte."
---

# Außergewöhnliche Umstände prüfen (Art. 5 Abs. 3 VO 261/2004)

## Norm

Art. 5 Abs. 3 VO 261/2004: Ein ausführendes Luftfahrtunternehmen ist nicht verpflichtet Ausgleichszahlungen zu leisten wenn es nachweisen kann dass die Annullierung **auf außergewöhnliche Umstände zurückgeht** die sich auch dann nicht hätten vermeiden lassen wenn alle zumutbaren Maßnahmen ergriffen worden waeren.

**Beweislast** liegt bei der Airline (Wortlaut "nachweisen kann"). Pauschale Behauptung reicht nicht.

## Zwei-Stufen-Prüfung

### Stufe 1 — Liegt überhaupt ein außergewöhnlicher Umstand vor?

Maßgeblich ist die st. Rspr. des EuGH. Die Definition (1) nicht Teil der normalen Tätigkeit des Luftfahrtunternehmens und (2) tatsächlich nicht beherrschbar — st. Rspr., bestätigt u.a. in EuGH C-549/07 (Wallentin-Hermann) und Folgeentscheidungen. Vor Versand jeden konkreten Sachverhalt mit einer offenen Quelle aus curia.europa.eu belegen.

### Stufe 2 — Hätten zumutbare Maßnahmen den Schaden verhindert?

Auch wenn ein außergewöhnlicher Umstand vorliegt, muss die Airline beweisen, dass alle zumutbaren Maßnahmen ergriffen wurden (Art. 5 Abs. 3 VO 261/2004; st. Rspr. EuGH C-549/07 und nachfolgende Entscheidungen — curia.europa.eu).

## Katalog typischer Sachverhalte (Stand Mai 2026)

### Ja regelmäßig außergewöhnlich

| Sachverhalt | Rspr. (offene Quelle) |
|---|---|
| Vulkanasche / Naturkatastrophe | EuGH st. Rspr. (curia.europa.eu) |
| Sicherheitsrisiken Terrordrohung | EuGH st. Rspr. (curia.europa.eu) |
| Streik der Flugsicherung (externer Dienstleister) | EuGH st. Rspr. (curia.europa.eu) |
| Blitzschlag mit sicherheitsbedingter Kontrolle | EuGH, Urt. v. 16.10.2025, C-399/24 — Blitzschlag kann außergewöhnlicher Umstand sein (curia.europa.eu) |
| Versteckter Konstruktionsfehler Triebwerk | EuGH, Urt. v. 13.6.2025, C-411/23 — versteckter Konstruktionsfehler ist außergewöhnlicher Umstand (curia.europa.eu) |
| Fluchtversuche Passagiere mit Behinderung des Bordbetriebs | EuGH-Linie je Einzelfall — Volltext in curia.europa.eu verifizieren |
| Krieg Embargo Luftraumsperrung | EuGH st. Rspr. (curia.europa.eu) |

### Nein regelmäßig keine außergewöhnlichen Umstände

| Sachverhalt | Rspr. (offene Quelle) |
|---|---|
| Technischer Defekt aus Wartungsversäumnis | EuGH, Urt. v. 22.12.2008, C-549/07 (Wallentin-Hermann) — curia.europa.eu |
| Streik der eigenen Mitarbeiter (Crew, Bodendienst) | st. Rspr. EuGH — Volltext in curia.europa.eu |
| Personalmangel am Flughafen (eigene Ground-Crew) | EuGH, Urt. v. 16.5.2024, C-405/23 — je nach Konstellation; gepäckabhängige Personalverknappung kann außergewöhnlich sein (curia.europa.eu) |
| Personalmangel / Krankenstand eigene Crew | st. Rspr. — Teil normalen Betriebs (curia.europa.eu) |
| Computer-Störungen des Buchungssystems | st. Rspr. EuGH (curia.europa.eu) |
| Wartung / TBO-Erreichung | Routine; kein außergewöhnlicher Umstand |

### Differenziert

| Sachverhalt | Differenzierung |
|---|---|
| Vorverlegung der Abflugzeit | EuGH, Urt. v. 9.1.2025, C-394/23 — Vorverlegung über eine Stunde gilt als Annullierung mit Entschädigungsanspruch (curia.europa.eu) |
| Wetter | bei wirklich extremen Bedingungen ja; bei normalen Wintern oder gemäßigtem Schneefall nein — EuGH-Linie konkret prüfen (curia.europa.eu) |
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

## Normen & Rechtsprechung

Konkret zu prüfen:

- Art. 5 Abs. 3 VO 261/2004
- EuGH C-549/07 (Wallentin-Hermann)
- EuGH C-12/11 (McDonagh)

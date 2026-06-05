---
name: kommunikationstagebuch-krankenkasse-bescheid
description: "Kommunikationstagebuch Krankenkasse Bescheid: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kommunikationstagebuch Krankenkasse Bescheid

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Kommunikationstagebuch Krankenkasse Bescheid** im Plugin Buerokratieversteher Entbuerokratisierer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kommunikationstagebuch` | Erstellt Behörden-Kommunikationsjournal mit Datum, Person, Inhalt, Zusage, Frist und nächster Aktion. |
| `krankenkasse-bescheid` | Routet Krankengeld, Hilfsmittel, Reha, Beitragsbescheid, Widerspruch und Sozialgericht. |
| `laien-sanity-check` | Letzte Prüfung: Habe ich verstanden, was passiert, welche Frist läuft, was ich sende und was ich nicht sende? |
| `leichte-einfache-sprache` | Erklärt Behördeninhalte in einfacher Sprache, ohne rechtliche Genauigkeit zu verlieren. |

## Arbeitsweg

Im Plugin Buerokratieversteher Entbuerokratisierer gilt für **Kommunikationstagebuch Krankenkasse Bescheid**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kommunikationstagebuch`

**Fokus:** Erstellt Behörden-Kommunikationsjournal mit Datum, Person, Inhalt, Zusage, Frist und nächster Aktion.

# Kommunikationstagebuch

## Aufgabe
Erstellt Behörden-Kommunikationsjournal mit Datum, Person, Inhalt, Zusage, Frist und nächster Aktion.

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.

## 2. `krankenkasse-bescheid`

**Fokus:** Routet Krankengeld, Hilfsmittel, Reha, Beitragsbescheid, Widerspruch und Sozialgericht.

# Krankenkasse-Bescheid

## Aufgabe
Routet Krankengeld, Hilfsmittel, Reha, Beitragsbescheid, Widerspruch und Sozialgericht.

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.

## 3. `laien-sanity-check`

**Fokus:** Letzte Prüfung: Habe ich verstanden, was passiert, welche Frist läuft, was ich sende und was ich nicht sende?

# Laien-Sanity-Check

## Aufgabe
Letzte Prüfung: Habe ich verstanden, was passiert, welche Frist läuft, was ich sende und was ich nicht sende?

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.

## 4. `leichte-einfache-sprache`

**Fokus:** Erklärt Behördeninhalte in einfacher Sprache, ohne rechtliche Genauigkeit zu verlieren.

# Leichte und einfache Sprache

## Aufgabe
Erklärt Behördeninhalte in einfacher Sprache, ohne rechtliche Genauigkeit zu verlieren.

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.

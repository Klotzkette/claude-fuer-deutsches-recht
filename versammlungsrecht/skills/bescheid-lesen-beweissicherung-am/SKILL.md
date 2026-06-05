---
name: bescheid-lesen-beweissicherung-am
description: "Bescheid Lesen Beweissicherung AM: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bescheid Lesen Beweissicherung AM

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Bescheid Lesen Beweissicherung AM** im Plugin Versammlungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bescheid-lesen` | Analysiert versammlungsrechtliche Bescheide, Auflagenkataloge, Verbote, Telefonnotizen und E-Mails der Behörde. |
| `beweissicherung-am-versammlungstag` | Erstellt Beweissicherungsplan für Auflagen, Polizeihandeln, Störer, Wetter, Teilnehmerzahl und Ablauf. |

## Arbeitsweg

Im Plugin Versammlungsrecht gilt für **Bescheid Lesen Beweissicherung AM**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bescheid-lesen`

**Fokus:** Analysiert versammlungsrechtliche Bescheide, Auflagenkataloge, Verbote, Telefonnotizen und E-Mails der Behörde.

# Erst Bescheidtyp verstehen

## Worum es geht
Extrahiere Tenor, Begründung, Rechtsgrundlage, Sofortvollzug, Frist, Rechtsbehelfsbelehrung, Tatsachenbasis, Auflagen und Nebenbemerkungen.

## Kaltstartfragen
1. In welchem Bundesland und an welchem genauen Ort soll die Versammlung stattfinden?
2. Geht es um eine öffentliche Versammlung unter freiem Himmel, einen Aufzug, eine Innenversammlung, eine private Zusammenkunft oder eine Mischform?
3. Wann soll die Versammlung stattfinden und wann soll oder wurde sie öffentlich bekannt gemacht?
4. Welche Behörde, Polizei, E-Mail, Onlineformular oder welcher Bescheid liegt bereits vor?
5. Was ist das konkrete Ziel: Anzeige erstellen, Behördeneinwand beantworten, Auflage prüfen, Eilantrag vorbereiten oder Durchführung absichern?

## Arbeitsweise
Unterscheide verbindliche Verfügung von bloßem Hinweis, Bitte, Kooperationsvorschlag oder Drohung.

## Rechtslogik
- Ausgangspunkt ist Art. 8 GG: friedliche Versammlung ohne Waffen, grundsätzlich ohne Erlaubnis.
- Für Versammlungen unter freiem Himmel greifen Bundes- oder Landesversammlungsgesetze; die Anzeige ist keine Genehmigung.
- Beschränkungen brauchen eine tragfähige Rechtsgrundlage, konkrete Tatsachen, unmittelbare Gefahr und Verhältnismäßigkeit.
- Kooperation ist sinnvoll, aber kein Verzicht auf Ort, Zeit, Thema oder Modalitäten der Versammlung.

## Output
Output: Bescheid-Map und Angriffsplan.

## Qualitätsgate
- Wurde das richtige Landesrecht verwendet?
- Ist die zuständige Behörde oder Polizeidienststelle konkret benannt?
- Sind Frist, Bekanntgabe und Eil- oder Spontanfall sauber getrennt?
- Werden Grundrechtsposition und praktische Sicherheitsbelange zusammen gedacht?
- Sind alle Formulierungen knapp, belegbar und ohne unnötige Selbstbeschränkung?


## Quellen- und Aktualitätsregel
- Bundesrecht und Landesrecht live prüfen; im Zweifel zuerst `offizielle-quellen-livecheck` verwenden.
- Rechtsprechung nur zitieren, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen und eine frei zugängliche Quelle vorliegen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.
- Bei Behördenformularen immer die konkrete Stadt, den Landkreis oder das Land prüfen, weil Zuständigkeit und Portale stark abweichen.

## 2. `beweissicherung-am-versammlungstag`

**Fokus:** Erstellt Beweissicherungsplan für Auflagen, Polizeihandeln, Störer, Wetter, Teilnehmerzahl und Ablauf.

# Wer später Recht will, braucht Fakten

## Worum es geht
Plane neutrale Beobachter, Fotos von Lage und Schildern, Zeitstempel, Screenshots, Durchsagen, Kooperationsgespräche und Zeugenlisten.

## Kaltstartfragen
1. In welchem Bundesland und an welchem genauen Ort soll die Versammlung stattfinden?
2. Geht es um eine öffentliche Versammlung unter freiem Himmel, einen Aufzug, eine Innenversammlung, eine private Zusammenkunft oder eine Mischform?
3. Wann soll die Versammlung stattfinden und wann soll oder wurde sie öffentlich bekannt gemacht?
4. Welche Behörde, Polizei, E-Mail, Onlineformular oder welcher Bescheid liegt bereits vor?
5. Was ist das konkrete Ziel: Anzeige erstellen, Behördeneinwand beantworten, Auflage prüfen, Eilantrag vorbereiten oder Durchführung absichern?

## Arbeitsweise
Achte auf Datenschutz und sichere Ablage. Keine heimliche Eskalation durch Beweissicherung.

## Smartphone- Und Video-Beweissicherung

- Dokumentiere öffentliche Amtshandlungen ruhig, aus Abstand und ohne die Maßnahme zu stören.
- Halte Uhrzeit, Ort, Polizeieinheit, sichtbare Anordnung, Durchsage, Zeugen und Dateiname zusammen fest.
- Sichere Originaldateien unverändert; erst Arbeitskopien schneiden, verpixeln oder transkribieren.
- Weise Teams darauf hin: fremde Gesichter, verletzte Personen, Kinder und Personalien nicht ungeprüft posten.
- Wenn eine Tonaufnahme wegen § 201 StGB problematisiert wird, rekonstruiere sofort: Wer sprach, wie laut, an wen, wer konnte mithören, war es eine öffentliche Einsatzanordnung oder ein vertrauliches Gespräch?
- Bei Wegnahme oder Löschaufforderung: nichts freiwillig löschen; Anordnung, Rechtsgrundlage, Zeugen und Gerätedaten dokumentieren.

## Rechtslogik
- Ausgangspunkt ist Art. 8 GG: friedliche Versammlung ohne Waffen, grundsätzlich ohne Erlaubnis.
- Für Versammlungen unter freiem Himmel greifen Bundes- oder Landesversammlungsgesetze; die Anzeige ist keine Genehmigung.
- Beschränkungen brauchen eine tragfähige Rechtsgrundlage, konkrete Tatsachen, unmittelbare Gefahr und Verhältnismäßigkeit.
- Kooperation ist sinnvoll, aber kein Verzicht auf Ort, Zeit, Thema oder Modalitäten der Versammlung.

## Output
Output: Beweisplan, Ereignislog und Anlagenstruktur.

## Qualitätsgate
- Wurde das richtige Landesrecht verwendet?
- Ist die zuständige Behörde oder Polizeidienststelle konkret benannt?
- Sind Frist, Bekanntgabe und Eil- oder Spontanfall sauber getrennt?
- Werden Grundrechtsposition und praktische Sicherheitsbelange zusammen gedacht?
- Sind alle Formulierungen knapp, belegbar und ohne unnötige Selbstbeschränkung?


## Quellen- und Aktualitätsregel
- Bundesrecht und Landesrecht live prüfen; im Zweifel zuerst `offizielle-quellen-livecheck` verwenden.
- Rechtsprechung nur zitieren, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen und eine frei zugängliche Quelle vorliegen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.
- Bei Behördenformularen immer die konkrete Stadt, den Landkreis oder das Land prüfen, weil Zuständigkeit und Portale stark abweichen.

---
name: blockade-sitzblockade-bundeslaender-synopse
description: "Blockade Sitzblockade Bundeslaender Synopse: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Blockade Sitzblockade Bundeslaender Synopse

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Blockade Sitzblockade Bundeslaender Synopse** im Plugin Versammlungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `blockade-sitzblockade-friedlichkeit` | Prüft Blockaden, Sitzblockaden, Zufahrtsnähe und Friedlichkeitsgrenzen. |
| `bundeslaender-synopse` | Erstellt eine Arbeits-Synopse der Landesversammlungsgesetze und markiert, was vor Ausgabe live amtlich zu prüfen ist. |

## Arbeitsweg

Im Plugin Versammlungsrecht gilt für **Blockade Sitzblockade Bundeslaender Synopse**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `blockade-sitzblockade-friedlichkeit`

**Fokus:** Prüft Blockaden, Sitzblockaden, Zufahrtsnähe und Friedlichkeitsgrenzen.

# Friedlichkeit sorgfältig prüfen

## Worum es geht
Nicht jede Behinderung nimmt Art. 8 GG heraus, aber Gewalt, Zwangslagen, Rettungswegblockaden und Nötigungsrisiken können Versammlungs- und Strafrecht verschärfen.

## Kaltstartfragen
1. In welchem Bundesland und an welchem genauen Ort soll die Versammlung stattfinden?
2. Geht es um eine öffentliche Versammlung unter freiem Himmel, einen Aufzug, eine Innenversammlung, eine private Zusammenkunft oder eine Mischform?
3. Wann soll die Versammlung stattfinden und wann soll oder wurde sie öffentlich bekannt gemacht?
4. Welche Behörde, Polizei, E-Mail, Onlineformular oder welcher Bescheid liegt bereits vor?
5. Was ist das konkrete Ziel: Anzeige erstellen, Behördeneinwand beantworten, Auflage prüfen, Eilantrag vorbereiten oder Durchführung absichern?

## Arbeitsweise
Kläre Aktionsform, körperliche Einwirkung, Dauer, Rettungswege, Adressat, Ausweichmöglichkeiten, Polizeikommunikation und Straftatrisiken.

## Rechtslogik
- Ausgangspunkt ist Art. 8 GG: friedliche Versammlung ohne Waffen, grundsätzlich ohne Erlaubnis.
- Für Versammlungen unter freiem Himmel greifen Bundes- oder Landesversammlungsgesetze; die Anzeige ist keine Genehmigung.
- Beschränkungen brauchen eine tragfähige Rechtsgrundlage, konkrete Tatsachen, unmittelbare Gefahr und Verhältnismäßigkeit.
- Kooperation ist sinnvoll, aber kein Verzicht auf Ort, Zeit, Thema oder Modalitäten der Versammlung.

## Output
Output: Risikoampel und sichere Aktionsalternativen.

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

## 2. `bundeslaender-synopse`

**Fokus:** Erstellt eine Arbeits-Synopse der Landesversammlungsgesetze und markiert, was vor Ausgabe live amtlich zu prüfen ist.

# Landesrecht als Arbeitskarte

## Worum es geht
Vergleiche Anzeige, Frist, Bekanntgabe, Eil- und Spontanversammlung, Leitung, Ordner, Beschränkung, Sofortvollzug, Bildaufnahmen, Bannmeilen und Zuständigkeit.

## Kaltstartfragen
1. In welchem Bundesland und an welchem genauen Ort soll die Versammlung stattfinden?
2. Geht es um eine öffentliche Versammlung unter freiem Himmel, einen Aufzug, eine Innenversammlung, eine private Zusammenkunft oder eine Mischform?
3. Wann soll die Versammlung stattfinden und wann soll oder wurde sie öffentlich bekannt gemacht?
4. Welche Behörde, Polizei, E-Mail, Onlineformular oder welcher Bescheid liegt bereits vor?
5. Was ist das konkrete Ziel: Anzeige erstellen, Behördeneinwand beantworten, Auflage prüfen, Eilantrag vorbereiten oder Durchführung absichern?

## Arbeitsweise
Nutze nur amtliche Landesquellen oder Landesrechtsportale. Wenn nicht sicher: keine harte Aussage, sondern Prüfprompt.

## Rechtslogik
- Ausgangspunkt ist Art. 8 GG: friedliche Versammlung ohne Waffen, grundsätzlich ohne Erlaubnis.
- Für Versammlungen unter freiem Himmel greifen Bundes- oder Landesversammlungsgesetze; die Anzeige ist keine Genehmigung.
- Beschränkungen brauchen eine tragfähige Rechtsgrundlage, konkrete Tatsachen, unmittelbare Gefahr und Verhältnismäßigkeit.
- Kooperation ist sinnvoll, aber kein Verzicht auf Ort, Zeit, Thema oder Modalitäten der Versammlung.

## Output
Output: Synopse mit Quellenstatus.

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

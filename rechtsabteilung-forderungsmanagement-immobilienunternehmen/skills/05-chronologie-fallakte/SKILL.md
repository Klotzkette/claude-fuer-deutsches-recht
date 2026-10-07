---
name: 05-chronologie-fallakte
description: "Chronologie, Ereignisachse und Fristenhistorie aufbauen oder mit neuer Zahlung, Gerichtspost und Korrespondenz fortschreiben. Klageeinreichung, Zustellung, Rechtshängigkeit, Delta, überholte Annahmen und Kostenpfad zeitlich ordnen. Output Tabelle und Änderungskarte."
---

# Chronologie der Fallakte

## Zweck und Anwendungsfall

Die Klageschrift verlangt einen geordneten Sachverhaltsvortrag. Dieser Skill macht aus dem SAP-Wirrwarr eine erzählbare Zeitachse und hält sie bei neuen Zahlungen, Schreiben oder Gerichtsereignissen fortlaufend aktuell. Anwendungsfall ist die Aufbereitung vor jedem Schriftsatz und jede spätere Fortschreibung der Akte.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- SAP-Akte (Skill 01), Mietakte (Skill 02) und Forderungsaufstellung (Skill 03).
- Korrespondenzmappe mit Mahnungen, Kündigungen und Schriftverkehr.
- Bekannte Gerichts-, Kündigungs- und Vollstreckungsfristen.
- Bei laufender Akte: letzte Chronologie, Akten-ID, Stichtag und Neuzugang.

## Ablauf / Checkliste

1. Pflichtereignisse erfassen und ihrer rechtlichen Wirkung zuordnen:

| Ereignis | Bedeutung | Rechtliche Wirkung |
|---|---|---|
| Vertragsschluss | Beginn | Anspruchsgrundlage |
| Übergabe Wohnung | Pflichterfüllung Vermieter | Mietzahlungspflicht |
| Mieterhöhung | Soll-Anhebung | Kappungsgrenze |
| Zahlungsstörung | Pflichtverletzung | Verzug |
| Mahnung 1 | Verzugsfortschreibung | Beweismittel |
| Kündigung | Vertragsende | Wirksamkeit prüfen |
| Klageeinreichung | Anhängigkeit / Fristwahrung | Kostenpfad vor Zustellung |
| Klagezustellung | Rechtshängigkeit | Schonfristfenster / Prozessfristen |
| Zahlung nach Klageeinreichung | erledigendes Ereignis | Kostenpfad und Verzug vor Klageeinreichung |

2. Jedes Ereignis zusätzlich mit ISO-Datum, Beleg und Sicherheitsgrad erfassen.
3. Unbekannte Daten nicht schätzen, sondern als UNKLAR markieren.
4. Fristen aus Gericht, Kündigung, Mieterhöhung und Vollstreckung separat markieren.
5. Widersprüche zwischen Korrespondenz, SAP und Vertrag in die Lückenliste übernehmen.
6. Nach Klageeinreichung Einreichungsdatum, Zustelldatum, Zahlungseingang, Wertstellung, Buchung, Kenntnisstand, Aufrechnung, dauernde Einrede, Unmöglichkeit und Wegfall des Rechtsschutzbedürfnisses getrennt erfassen. Für Kosten als Verzugsschaden müssen Vorverzug sowie aus damaliger Sicht erforderliche und kausale Klagekosten belegt sein. Grün ist die bei Einreichung noch offene Forderung; eine unmittelbar zuvor eingegangene, objektiv noch nicht erkennbare Zahlung bleibt gelb und geht zur RA-Prüfung.
7. Bei Fortschreibung den letzten bestätigten Stichtag festhalten und nur neue oder geänderte Ereignisse einfügen; frühere sichere Ereignisse unverändert übernehmen.
8. Aus jeder Änderung ableiten, welche Frist, Forderung, Beweiswürdigung oder Prozessposition neu ist und welcher frühere Arbeitsstand dadurch überholt wird.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen.

## Ausgabeformat

Chronologie mit ISO-Datum, Ereignis, rechtlicher Bedeutung, Beleg, Sicherheit, Fristwirkung, Rechtshängigkeitsstatus, Kostenpfad-Hinweis und Sachverhaltsnummer für die Klage. Bei Fortschreibung zusätzlich Änderungskarte mit Stichtag alt/neu, Neuzugang, geänderter Rechtsfolge, überholtem Arbeitsstand und nächstem Skill. Die Chronologie bleibt tabellarisch; der daraus abgeleitete Sachverhaltsvortrag wird in vollständigen Sätzen ausformuliert (Ausformulierungspflicht).

## Beispiele

- Das Datum der Wohnungsübergabe ist nicht belegt: Das Ereignis wird mit Sicherheitsgrad UNKLAR geführt und in die Lückenliste aufgenommen.
- Klageeinreichung und Zustellung werden als getrennte Ereignisse erfasst, damit Rechtshängigkeit, Schonfristfenster und Kostenpfad sauber berechnet werden können.

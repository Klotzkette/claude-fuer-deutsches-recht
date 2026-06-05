---
name: bu-berufsbild-bu-nachpruefung-datenschutz
description: "BU Berufsbild BU Nachpruefung Datenschutz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# BU Berufsbild BU Nachpruefung Datenschutz

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **BU Berufsbild BU Nachpruefung Datenschutz** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bu-berufsbild-50-prozent-substantiierung` | Berufsunfähigkeitsversicherung: konkretes Berufsbild, prägende Tätigkeiten, Zeitanteile, gesundheitliche Einschränkungen und 50-Prozent-Grenze substantiiert darstellen. |
| `bu-nachpruefung-anerkenntnis-leistungseinstellung` | BU-Nachprüfung: Anerkenntnis, Gesundheitsverbesserung, Berufswechsel, Mitwirkung, Fristen, Beweislast und Angriff auf Leistungseinstellung. |
| `datenschutz-schweigepflicht-gesundheitsdaten` | Gesundheitsdaten im Versicherungsmandat: Schweigepflichtentbindung, DSGVO, Datensparsamkeit, Arztanfragen, Gutachter, PKV/BU/Unfall und Aktenführung. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **BU Berufsbild BU Nachpruefung Datenschutz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bu-berufsbild-50-prozent-substantiierung`

**Fokus:** Berufsunfähigkeitsversicherung: konkretes Berufsbild, prägende Tätigkeiten, Zeitanteile, gesundheitliche Einschränkungen und 50-Prozent-Grenze substantiiert darstellen.

# BU: Berufsbild und 50-Prozent-Prüfung

## Einsatz

Der Skill macht aus Arztbriefen und Tätigkeitslisten eine klagefeste BU-Substantiierung.

## Norm- und Quellenanker

VVG §§ 172–177; AVB BU; ZPO Darlegungslast; Sozial-/Medizinunterlagen nur mit Datenschutzcheck.

## Arbeitsfragen

1. Wie sah der Beruf zuletzt in gesunden Tagen konkret aus?
2. Welche Tätigkeiten waren prägend, wie häufig und wie belastend?
3. Welche Einschränkung trifft welche Tätigkeit?
4. Seit wann besteht BU und welche Prognose gilt?

## Output

Berufsbildtabelle, Gesundheits-Mapping, Beweisangebote und BU-Antrag/Klagekern.

## Red Flags

- Beruf nur als Berufsbezeichnung beschrieben
- Zeitanteile geschätzt ohne Belege
- Arzt schreibt nur Diagnose, nicht Funktionsverlust
- Versicherer verlangt abstrakte Idealberufe

## Anschluss-Skills

- bu-abstrakte-konkrete-verweisung
- bu-nachpruefung-anerkenntnis-leistungseinstellung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `bu-nachpruefung-anerkenntnis-leistungseinstellung`

**Fokus:** BU-Nachprüfung: Anerkenntnis, Gesundheitsverbesserung, Berufswechsel, Mitwirkung, Fristen, Beweislast und Angriff auf Leistungseinstellung.

# BU: Anerkenntnis, Nachprüfung, Leistungseinstellung

## Einsatz

Der Skill ist für laufende BU-Renten, die der Versicherer nach Nachprüfung stoppen will.

## Norm- und Quellenanker

VVG §§ 172 ff.; AVB BU; BGB; ZPO.

## Arbeitsfragen

1. Was wurde ursprünglich anerkannt: abstrakt, befristet, konkret?
2. Welche Änderung behauptet der Versicherer?
3. Welche Vergleichsbasis gilt für Gesundheits- und Berufsbildänderung?
4. Ist die Einstellung formal und materiell wirksam?

## Output

Nachprüfungs-Gegenmemo, Unterlagenliste, Widerspruch/Antwort und Klageoption.

## Red Flags

- befristetes Anerkenntnis unkritisch hingenommen
- neue Tätigkeit ohne Lebensstellungsprüfung
- medizinische Besserung nur aus Aktenlage
- Mitwirkungsobliegenheit überdehnt

## Anschluss-Skills

- bu-berufsbild-50-prozent-substantiierung
- datenschutz-schweigepflicht-gesundheitsdaten

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `datenschutz-schweigepflicht-gesundheitsdaten`

**Fokus:** Gesundheitsdaten im Versicherungsmandat: Schweigepflichtentbindung, DSGVO, Datensparsamkeit, Arztanfragen, Gutachter, PKV/BU/Unfall und Aktenführung.

# Gesundheitsdaten, Schweigepflicht und Versicherer

## Einsatz

Der Skill schützt Mandanten vor zu breiten Gesundheitsdatenfreigaben und hält trotzdem die Mitwirkungspflichten ein.

## Norm- und Quellenanker

DSGVO Art. 5, 6, 9, 15; BDSG; VVG §§ 19, 31, 213; StGB § 203 für Berufsgeheimnisse.

## Arbeitsfragen

1. Welche Gesundheitsdaten sind für welchen Prüfpunkt erforderlich?
2. Welche Entbindung ist eng genug formuliert?
3. Wer erhält Daten: Versicherer, Gutachter, Makler, Gericht?
4. Wie werden Daten in der Kanzleiakte geschützt?

## Output

Datenschutz- und Schweigepflichtvermerk, Entbindungs-Redline, Arztfragebogen und Datenminimierungsplan.

## Red Flags

- Blankoentbindung für alle Ärzte
- Makler im Datenfluss vergessen
- Gutachterauftrag zu weit
- Mandant kennt Reichweite nicht

## Anschluss-Skills

- vvg-anzeigepflicht-19-ruecktritt-kuendigung-anpassung
- pkv-kostenerstattung-medizinische-notwendigkeit

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

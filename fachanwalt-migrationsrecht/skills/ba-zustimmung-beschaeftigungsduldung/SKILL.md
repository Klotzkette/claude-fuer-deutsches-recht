---
name: ba-zustimmung-beschaeftigungsduldung
description: "BA Zustimmung Beschaeftigungsduldung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# BA Zustimmung Beschaeftigungsduldung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **BA Zustimmung Beschaeftigungsduldung** im Plugin Fachanwalt Migrationsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-ba-zustimmung-beschaeftigung` | BA-Zustimmung Beschäftigung: Fachmodul im Migrationsrecht; prüft Zustimmungserfordernis, Vorrang/Arbeitsbedingungen, Ausnahmen; mit deutschem Recht, EU/EMRK/GFK, Belegen, Fristen und Quellencheck. |
| `spezial-beschaeftigungsduldung` | Beschäftigungsduldung: Fachmodul im Migrationsrecht; prüft Beschäftigungszeiten, Lebensunterhalt, Identität, Straffreiheit; mit deutschem Recht, EU/EMRK/GFK, Belegen, Fristen und Quellencheck. |

## Arbeitsweg

Im Plugin Fachanwalt Migrationsrecht gilt für **BA Zustimmung Beschaeftigungsduldung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-ba-zustimmung-beschaeftigung`

**Fokus:** BA-Zustimmung Beschäftigung: Fachmodul im Migrationsrecht; prüft Zustimmungserfordernis, Vorrang/Arbeitsbedingungen, Ausnahmen; mit deutschem Recht, EU/EMRK/GFK, Belegen, Fristen und Quellencheck.

# BA-Zustimmung Beschäftigung

## Aufgabe
Fachmodul im Plugin `fachanwalt-migrationsrecht`. Er bearbeitet: prüft Zustimmungserfordernis, Vorrang/Arbeitsbedingungen, Ausnahmen.

## Einstieg
1. Wer ist betroffen, wer fragt, und welches konkrete Ziel besteht?
2. Welche Staatsangehörigkeit/Gebietszuordnung, welcher Aufenthaltsort und welcher aktuelle Status liegen vor?
3. Welche Frist oder welches Eilrisiko entscheidet den Fall?
4. Welche Unterlagen beweisen Identität, Status, Familie, Arbeit, Ausbildung, Schutzgrund oder Gesundheit?
5. Soll das Ergebnis auf Deutsch, in einfacher Sprache oder zusätzlich auf Spanisch ausgegeben werden?

## Prüfraster
1. **Status und Ziel:** Ist der passende Titel/Schutz-/Rechtsbehelfspfad richtig gewählt?
2. **Tatbestand:** Normmerkmale, Ausnahmen, Ermessen, Versagungsgründe und Gegenargumente.
3. **EU/EMRK/GFK:** Unionsrechtliche oder menschenrechtliche Ebene prüfen, wenn sie den Fall tragen kann.
4. **Staatenbezug:** Herkunfts-, Transit- und Zielstaat nur mit aktuellen Quellen bewerten; keine statischen Sicherheitsannahmen.
5. **Beweis:** Dokumente, Urkunden, Übersetzungen, Atteste, Länderquellen und digitale Belege sauber trennen.
6. **Taktik:** Antrag, Nachreichung, Fristverlängerung, Eilantrag, Klage, Vergleich, Behördenkommunikation.

## Output
- Kurzlage und Risikoampel.
- Prüfmatrix: Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- Direkt nutzbarer Textbaustein für Behörde, Gericht, Arbeitgeber oder Mandant.
- Anschluss-Skills innerhalb dieses Plugins.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 2. `spezial-beschaeftigungsduldung`

**Fokus:** Beschäftigungsduldung: Fachmodul im Migrationsrecht; prüft Beschäftigungszeiten, Lebensunterhalt, Identität, Straffreiheit; mit deutschem Recht, EU/EMRK/GFK, Belegen, Fristen und Quellencheck.

# Beschäftigungsduldung

## Aufgabe
Fachmodul im Plugin `fachanwalt-migrationsrecht`. Er bearbeitet: prüft Beschäftigungszeiten, Lebensunterhalt, Identität, Straffreiheit.

## Einstieg
1. Wer ist betroffen, wer fragt, und welches konkrete Ziel besteht?
2. Welche Staatsangehörigkeit/Gebietszuordnung, welcher Aufenthaltsort und welcher aktuelle Status liegen vor?
3. Welche Frist oder welches Eilrisiko entscheidet den Fall?
4. Welche Unterlagen beweisen Identität, Status, Familie, Arbeit, Ausbildung, Schutzgrund oder Gesundheit?
5. Soll das Ergebnis auf Deutsch, in einfacher Sprache oder zusätzlich auf Spanisch ausgegeben werden?

## Prüfraster
1. **Status und Ziel:** Ist der passende Titel/Schutz-/Rechtsbehelfspfad richtig gewählt?
2. **Tatbestand:** Normmerkmale, Ausnahmen, Ermessen, Versagungsgründe und Gegenargumente.
3. **EU/EMRK/GFK:** Unionsrechtliche oder menschenrechtliche Ebene prüfen, wenn sie den Fall tragen kann.
4. **Staatenbezug:** Herkunfts-, Transit- und Zielstaat nur mit aktuellen Quellen bewerten; keine statischen Sicherheitsannahmen.
5. **Beweis:** Dokumente, Urkunden, Übersetzungen, Atteste, Länderquellen und digitale Belege sauber trennen.
6. **Taktik:** Antrag, Nachreichung, Fristverlängerung, Eilantrag, Klage, Vergleich, Behördenkommunikation.

## Output
- Kurzlage und Risikoampel.
- Prüfmatrix: Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- Direkt nutzbarer Textbaustein für Behörde, Gericht, Arbeitgeber oder Mandant.
- Anschluss-Skills innerhalb dieses Plugins.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

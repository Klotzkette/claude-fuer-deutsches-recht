---
name: arbeitsgericht-klage-arbeitsschutz-audit
description: "Arbeitsgericht Klage Arbeitsschutz Audit: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Arbeitsgericht Klage Arbeitsschutz Audit

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Arbeitsgericht Klage Arbeitsschutz Audit** im Plugin Hinweisgeberschutz Compliance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `arbeitsgericht-klage` | Bereitet arbeitsgerichtliche Klage wegen Repressalie vor. |
| `arbeitsschutz` | Prüft Arbeitsschutz-Hinweise und Eskalation. |
| `audit-nachweis` | Baut Audit-Nachweis für das Hinweisgebersystem. |
| `aufsichtsrat-reporting` | Berichtet Hinweisfälle an Aufsichtsrat oder Beirat. |

## Arbeitsweg

Im Plugin Hinweisgeberschutz Compliance gilt für **Arbeitsgericht Klage Arbeitsschutz Audit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `arbeitsgericht-klage`

**Fokus:** Bereitet arbeitsgerichtliche Klage wegen Repressalie vor.

# Arbeitsgericht Klage

## Wofür dieser Arbeitsgang da ist
Anträge, Kausalität, Beweislast, Vergleich, Beschäftigungsanspruch und Belege.

Dieser Skill arbeitet nicht als abstraktes Merkblatt. Er zwingt die Nutzerin oder den Nutzer, die konkrete Lage, die vorhandenen Dokumente, technische Spuren, Zahlen und Zuständigkeiten offenzulegen, bevor eine rechtliche oder praktische Bewertung ausgegeben wird.

## Kaltstartfragen

- Welche konkrete Entscheidung steht jetzt an und wer muss sie verantworten?
- Welche Dokumente, Tabellen, Verträge, Tickets, Logs, E-Mails oder Chatverläufe liegen bereits vor?
- Welche Frist, Behörde, Vertragspartei, Kundengruppe oder interne Eskalation macht Druck?
- Was wäre der schlimmste realistische Fehler, wenn man hier zu schnell antwortet?
- Welche Quelle muss live geprüft werden, bevor eine Norm, Frist oder Rechtsprechung zitiert wird?

## Arbeitslogik

1. **Sachverhalt festnageln:** Beteiligte, Zeitraum, Dokumente, Zahlen, Systeme, Rollen und offene Lücken in einer kurzen Matrix erfassen.
2. **Pflichtanker setzen:** Maßgebliche Normen und Behördenquellen live prüfen; keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate verwenden.
3. **Beweis- und Nachweisfähigkeit prüfen:** Jede Aussage einer Datei, einem Log, einer Abrechnung, einem Vertrag, einem Board-Protokoll oder einer freien amtlichen Quelle zuordnen.
4. **Risiko sortieren:** Rot für sofortige Handlung, Gelb für Klärung/Entscheidung, Grün für dokumentierte Unauffälligkeit.
5. **Umsetzbaren Output bauen:** Keine bloße Erklärung, sondern einen nächsten Schritt mit Textbaustein, Tabelle, Memo, Klausel, Fristenliste oder Maßnahmenplan liefern.

## Fachanker

- Primärer Anker: ArbGG; HinSchG; KSchG.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Klagebausteine. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

## 2. `arbeitsschutz`

**Fokus:** Prüft Arbeitsschutz-Hinweise und Eskalation.

# Arbeitsschutz

## Wofür dieser Arbeitsgang da ist
Gefahr, Fachkraft, Betriebsarzt, Behörde, Sofortmaßnahme und Schutz des Meldenden.

Dieser Skill arbeitet nicht als abstraktes Merkblatt. Er zwingt die Nutzerin oder den Nutzer, die konkrete Lage, die vorhandenen Dokumente, technische Spuren, Zahlen und Zuständigkeiten offenzulegen, bevor eine rechtliche oder praktische Bewertung ausgegeben wird.

## Kaltstartfragen

- Welche konkrete Entscheidung steht jetzt an und wer muss sie verantworten?
- Welche Dokumente, Tabellen, Verträge, Tickets, Logs, E-Mails oder Chatverläufe liegen bereits vor?
- Welche Frist, Behörde, Vertragspartei, Kundengruppe oder interne Eskalation macht Druck?
- Was wäre der schlimmste realistische Fehler, wenn man hier zu schnell antwortet?
- Welche Quelle muss live geprüft werden, bevor eine Norm, Frist oder Rechtsprechung zitiert wird?

## Arbeitslogik

1. **Sachverhalt festnageln:** Beteiligte, Zeitraum, Dokumente, Zahlen, Systeme, Rollen und offene Lücken in einer kurzen Matrix erfassen.
2. **Pflichtanker setzen:** Maßgebliche Normen und Behördenquellen live prüfen; keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate verwenden.
3. **Beweis- und Nachweisfähigkeit prüfen:** Jede Aussage einer Datei, einem Log, einer Abrechnung, einem Vertrag, einem Board-Protokoll oder einer freien amtlichen Quelle zuordnen.
4. **Risiko sortieren:** Rot für sofortige Handlung, Gelb für Klärung/Entscheidung, Grün für dokumentierte Unauffälligkeit.
5. **Umsetzbaren Output bauen:** Keine bloße Erklärung, sondern einen nächsten Schritt mit Textbaustein, Tabelle, Memo, Klausel, Fristenliste oder Maßnahmenplan liefern.

## Fachanker

- Primärer Anker: ArbSchG; HinSchG.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Arbeitsschutz-Fahrplan. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

## 3. `audit-nachweis`

**Fokus:** Baut Audit-Nachweis für das Hinweisgebersystem.

# Audit Nachweis

## Wofür dieser Arbeitsgang da ist
Policy, Kanal, Schulung, Fälle, Fristen, Löschung, Zugriffe, Ausnahmen und Verbesserungen.

Dieser Skill arbeitet nicht als abstraktes Merkblatt. Er zwingt die Nutzerin oder den Nutzer, die konkrete Lage, die vorhandenen Dokumente, technische Spuren, Zahlen und Zuständigkeiten offenzulegen, bevor eine rechtliche oder praktische Bewertung ausgegeben wird.

## Kaltstartfragen

- Welche konkrete Entscheidung steht jetzt an und wer muss sie verantworten?
- Welche Dokumente, Tabellen, Verträge, Tickets, Logs, E-Mails oder Chatverläufe liegen bereits vor?
- Welche Frist, Behörde, Vertragspartei, Kundengruppe oder interne Eskalation macht Druck?
- Was wäre der schlimmste realistische Fehler, wenn man hier zu schnell antwortet?
- Welche Quelle muss live geprüft werden, bevor eine Norm, Frist oder Rechtsprechung zitiert wird?

## Arbeitslogik

1. **Sachverhalt festnageln:** Beteiligte, Zeitraum, Dokumente, Zahlen, Systeme, Rollen und offene Lücken in einer kurzen Matrix erfassen.
2. **Pflichtanker setzen:** Maßgebliche Normen und Behördenquellen live prüfen; keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate verwenden.
3. **Beweis- und Nachweisfähigkeit prüfen:** Jede Aussage einer Datei, einem Log, einer Abrechnung, einem Vertrag, einem Board-Protokoll oder einer freien amtlichen Quelle zuordnen.
4. **Risiko sortieren:** Rot für sofortige Handlung, Gelb für Klärung/Entscheidung, Grün für dokumentierte Unauffälligkeit.
5. **Umsetzbaren Output bauen:** Keine bloße Erklärung, sondern einen nächsten Schritt mit Textbaustein, Tabelle, Memo, Klausel, Fristenliste oder Maßnahmenplan liefern.

## Fachanker

- Primärer Anker: HinSchG; DSGVO.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Audit-Ordnerindex. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

## 4. `aufsichtsrat-reporting`

**Fokus:** Berichtet Hinweisfälle an Aufsichtsrat oder Beirat.

# Aufsichtsrat Reporting

## Wofür dieser Arbeitsgang da ist
Anonymisierung, Wesentlichkeit, offene Risiken, Maßnahmen, Fristen und Protokoll.

Dieser Skill arbeitet nicht als abstraktes Merkblatt. Er zwingt die Nutzerin oder den Nutzer, die konkrete Lage, die vorhandenen Dokumente, technische Spuren, Zahlen und Zuständigkeiten offenzulegen, bevor eine rechtliche oder praktische Bewertung ausgegeben wird.

## Kaltstartfragen

- Welche konkrete Entscheidung steht jetzt an und wer muss sie verantworten?
- Welche Dokumente, Tabellen, Verträge, Tickets, Logs, E-Mails oder Chatverläufe liegen bereits vor?
- Welche Frist, Behörde, Vertragspartei, Kundengruppe oder interne Eskalation macht Druck?
- Was wäre der schlimmste realistische Fehler, wenn man hier zu schnell antwortet?
- Welche Quelle muss live geprüft werden, bevor eine Norm, Frist oder Rechtsprechung zitiert wird?

## Arbeitslogik

1. **Sachverhalt festnageln:** Beteiligte, Zeitraum, Dokumente, Zahlen, Systeme, Rollen und offene Lücken in einer kurzen Matrix erfassen.
2. **Pflichtanker setzen:** Maßgebliche Normen und Behördenquellen live prüfen; keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate verwenden.
3. **Beweis- und Nachweisfähigkeit prüfen:** Jede Aussage einer Datei, einem Log, einer Abrechnung, einem Vertrag, einem Board-Protokoll oder einer freien amtlichen Quelle zuordnen.
4. **Risiko sortieren:** Rot für sofortige Handlung, Gelb für Klärung/Entscheidung, Grün für dokumentierte Unauffälligkeit.
5. **Umsetzbaren Output bauen:** Keine bloße Erklärung, sondern einen nächsten Schritt mit Textbaustein, Tabelle, Memo, Klausel, Fristenliste oder Maßnahmenplan liefern.

## Fachanker

- Primärer Anker: AktG/GmbHG Governance; HinSchG.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Aufsichtsratsvorlage. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

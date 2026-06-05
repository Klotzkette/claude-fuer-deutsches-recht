---
name: tisax-iso-triage-strafrecht-uk-whistleblowing
description: "Tisax ISO Triage Strafrecht UK Whistleblowing: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Tisax ISO Triage Strafrecht UK Whistleblowing

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Tisax ISO Triage Strafrecht UK Whistleblowing** im Plugin Hinweisgeberschutz Compliance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tisax-iso-hinweisgeber` | Verknüpft TISAX/ISO-Compliance mit Hinweisgebersystem. |
| `triage-strafrecht` | Routet Hinweise mit Strafrechtsbezug. |
| `uk-whistleblowing-abgrenzung` | Grenzt UK Whistleblowing bei Niederlassungen ab. |
| `umweltverstoss` | Prüft Umweltverstöße im Hinweisgebersystem. |

## Arbeitsweg

Im Plugin Hinweisgeberschutz Compliance gilt für **Tisax ISO Triage Strafrecht UK Whistleblowing**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tisax-iso-hinweisgeber`

**Fokus:** Verknüpft TISAX/ISO-Compliance mit Hinweisgebersystem.

# Tisax Iso Hinweisgeber

## Wofür dieser Arbeitsgang da ist
Auditnachweise, Informationssicherheit, Lieferantenanforderungen und vertrauliche Meldungen.

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

- Primärer Anker: ISO 27001; TISAX; HinSchG.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Audit-Control-Mapping. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

## 2. `triage-strafrecht`

**Fokus:** Routet Hinweise mit Strafrechtsbezug.

# Triage Strafrecht

## Wofür dieser Arbeitsgang da ist
Untreue, Korruption, Betrug, Datenabfluss, Durchsuchungsrisiko, Selbstbelastung und Anzeige.

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

- Primärer Anker: StGB/StPO; HinSchG.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Strafrechts-Triage. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

## 3. `uk-whistleblowing-abgrenzung`

**Fokus:** Grenzt UK Whistleblowing bei Niederlassungen ab.

# Uk Whistleblowing Abgrenzung

## Wofür dieser Arbeitsgang da ist
PIDA, prescribed persons, Konzernkanal, Datenschutz und deutsch-britische Konflikte.

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

- Primärer Anker: UK local counsel; HinSchG.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: UK-Schnittstellenvermerk. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

## 4. `umweltverstoss`

**Fokus:** Prüft Umweltverstöße im Hinweisgebersystem.

# Umweltverstoss

## Wofür dieser Arbeitsgang da ist
Emissionen, Abfall, Wasser, Genehmigung, Behörde, Beweise und Geschäftsgeheimnisse.

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

- Primärer Anker: Umweltrecht; HinSchG.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Umwelt-Hinweis-Memo. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

---
name: security-procurement-training-management
description: "Security Procurement Training Management: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Security Procurement Training Management

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Security Procurement Training Management** im Plugin Nis2 Cybersecurity Compliance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `security-procurement-tender` | Prüft IT-Security-Anforderungen in Einkauf, Ausschreibung und Beschaffung von SaaS, Hardware, OT, Managed Services und Cyberdienstleistungen. |
| `security-training-management` | Prüft Security-Schulung der Leitung und Mitarbeitenden. |
| `sektor-und-groessencheck` | Ordnet Tätigkeiten in NIS-2-Sektoren und Unternehmensgrößen ein. |
| `software-sbom` | Baut SBOM-Prozess für eigene Software und Lieferanten. |

## Arbeitsweg

Im Plugin Nis2 Cybersecurity Compliance gilt für **Security Procurement Training Management**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `security-procurement-tender`

**Fokus:** Prüft IT-Security-Anforderungen in Einkauf, Ausschreibung und Beschaffung von SaaS, Hardware, OT, Managed Services und Cyberdienstleistungen.

# Security Procurement Tender

## Wofür dieser Arbeitsgang da ist

Dieser Skill macht IT-Sicherheit beschaffbar: Er übersetzt NIS-2-/BSIG-, BSI-, Datenschutz- und Betriebsanforderungen in Vergabeunterlagen, RFPs, Leistungsverzeichnisse, Bewertungsmatrizen und Vertragsklauseln. Er ist besonders nützlich, wenn Einkauf schnell einen Anbieter beauftragen will und Legal/CISO verhindern müssen, dass Security erst nach dem Signing diskutiert wird.

## Kaltstartfragen

- Was wird beschafft: SaaS, Cloud, OT-Komponente, Fernwartung, MDM, SOC, Pentest, Hardware, KI-Tool oder Managed Service?
- Welche Daten, Systeme und Standorte sind betroffen?
- Ist der Anbieter Teil einer kritischen Lieferkette oder verarbeitet er besonders sensible Daten?
- Welche Nachweise werden verlangt: BSI C5, ISO 27001, SOC 2, Pentestbericht, SBOM, AVV, Subdienstleisterliste?
- Welche Muss-Kriterien führen zum Ausschluss?

## Arbeitslogik

1. **Bedarf klassifizieren:** Kritikalität, Datenklassen, Betriebsabhängigkeit, Exit-Risiko und Incident-Auswirkung bestimmen.
2. **Muss-Kriterien setzen:** MFA, Verschlüsselung, Logging, Schwachstellenprozess, Meldefristen, Subdienstleisterkontrolle, Exit, Auditrechte und Notfallkontakte.
3. **Nachweise bewerten:** Zertifikat, Testat, Management Assertion und Selbstauskunft nicht gleichsetzen.
4. **Vertrag vorbereiten:** Security Schedule, Incident Clause, Audit Clause, Datenschutz, Geheimnisse, Change Control und Exit.
5. **Entscheidung dokumentieren:** Warum ein Anbieter trotz Restlücken akzeptiert oder ausgeschlossen wurde.

## Typische Stolperstellen

- Einkauf fragt nur nach Preis und Verfügbarkeit.
- Anbieter verweist auf Zertifikate, deren Scope das konkrete Produkt nicht umfasst.
- Security-Anforderungen stehen im Lastenheft, fehlen aber im Vertrag.
- Subdienstleister und Supportzugriffe werden erst nach Go-live sichtbar.

## Ergebnisformat

Erzeuge eine RFP-/Tender-Matrix mit Muss-Kriterien, Bewertungspunkten, Nachweisfeld, Vertragsklausel und roter Ausschlusslogik.

## 2. `security-training-management`

**Fokus:** Prüft Security-Schulung der Leitung und Mitarbeitenden.

# Security Training Management

## Wofür dieser Arbeitsgang da ist
Pflichtschulungen, Rollenmodule, Vorstandstraining, Nachweise, Wirksamkeit und Sanktionen.

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

- Primärer Anker: NIS-2 Art. 20 Leitungsschulung; BSI.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Trainingsmatrix. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

## 3. `sektor-und-groessencheck`

**Fokus:** Ordnet Tätigkeiten in NIS-2-Sektoren und Unternehmensgrößen ein.

# Sektor Und Groessencheck

## Wofür dieser Arbeitsgang da ist
Mehrspartenunternehmen, Konzernservice, kritische Zulieferer, IT-Dienstleister und Mischbetriebe sauber trennen.

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

- Primärer Anker: NIS-2 Anhänge I/II; EU-KMU-Logik; BSIG 2025.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Sektor-Mapping-Tabelle. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

## 4. `software-sbom`

**Fokus:** Baut SBOM-Prozess für eigene Software und Lieferanten.

# Software SBOM

## Wofür dieser Arbeitsgang da ist
Komponenten, Versionen, CVEs, Lizenzen, Kundenanforderungen, CRA-Schnittstelle und Nachverfolgung.

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

- Primärer Anker: CRA; NIS-2 Lieferkette; SPDX/CycloneDX.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: SBOM-Policy. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

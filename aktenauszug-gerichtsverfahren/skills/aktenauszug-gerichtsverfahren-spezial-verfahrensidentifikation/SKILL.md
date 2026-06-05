---
name: aktenauszug-gerichtsverfahren-spezial-verfahrensidentifikation
description: "Spezial Verfahrensidentifikation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Spezial Verfahrensidentifikation

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Spezial Verfahrensidentifikation** im Plugin Aktenauszug zivilgerichtlicher Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-verfahrensidentifikation-dokumentenmatrix` | Verfahrensidentifikation: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-verfahrenszusammenfassung-rechtsweg-register` | Verfahrenszusammenfassung: Behörden-, Gerichts- oder Registerweg im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `verfahrenschronologie` | Erstellt eine chronologische Bullet-Liste aller prozessualen Schritte: Klageeingang Zustellungen Schriftsatzfristen Beweisbeschluesse muendliche Verhandlungen Beweisaufnahme Urteile und Rechtsmittel. Kritische Fristen werden optisch hervorgehoben. Fundstellen werden angegeben. Normen §§ 222 517 520 ZPO Fristberechnung. |

## Arbeitsweg

Im Plugin Aktenauszug zivilgerichtlicher Verfahren gilt für **Spezial Verfahrensidentifikation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-verfahrensidentifikation-dokumentenmatrix`

**Fokus:** Verfahrensidentifikation: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Verfahrensidentifikation: Dokumentenmatrix, Lückenliste und Nachforderung

## Spezialwissen: Verfahrensidentifikation: Dokumentenmatrix, Lückenliste und Nachforderung
- **Spezialgegenstand:** Verfahrensidentifikation: Dokumentenmatrix, Lückenliste und Nachforderung / verfahrensidentifikation dokumentenmatrix. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Verfahrensidentifikation** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `spezial-verfahrenszusammenfassung-rechtsweg-register`

**Fokus:** Verfahrenszusammenfassung: Behörden-, Gerichts- oder Registerweg im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Verfahrenszusammenfassung: Behörden-, Gerichts- oder Registerweg

## Spezialwissen: Verfahrenszusammenfassung: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Verfahrenszusammenfassung: Behörden-, Gerichts- oder Registerweg / verfahrenszusammenfassung rechtsweg register. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Verfahrenszusammenfassung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `verfahrenschronologie`

**Fokus:** Erstellt eine chronologische Bullet-Liste aller prozessualen Schritte: Klageeingang Zustellungen Schriftsatzfristen Beweisbeschluesse muendliche Verhandlungen Beweisaufnahme Urteile und Rechtsmittel. Kritische Fristen werden optisch hervorgehoben. Fundstellen werden angegeben. Normen §§ 222 517 520 ZPO Fristberechnung.

# Verfahrenschronologie

## Zweck

Die Verfahrenschronologie erfasst alle prozessualen Schritte in zeitlicher Reihenfolge. Sie unterscheidet sich von der Sachverhaltschronologie dadurch, dass sie ausschließlich innerhalb des Verfahrens liegende Handlungen und Ereignisse abbildet.

## Triage — kläre vor Erstellung

1. Liegt die Zustellungsurkunde der Klageschrift vor? (Fristbeginn für Klageerwiderung)
2. Wurden alle Urteile zugestellt? (Berufungsfrist läuft ab Zustellung!)
3. Haben beide Parteien Schriftsätze vorgelegt? Welche?
4. Sind Vollstreckungsmaßnahmen eingeleitet? (Pfändungsbeschluss, Zwangshypothek)

## Zentrale Normen (Verfahrensrecht)

- § 222 ZPO i.V.m. §§ 187-188 BGB — Fristberechnung im Verfahren
- §§ 517-520 ZPO — Berufung und Begründung (Fristen: 1 Monat / 2 Monate)
- §§ 548-551 ZPO — Revision (Fristen: 1 Monat / 2 Monate)
- § 329 ZPO — Verkündung von Beschlüssen
- § 310 ZPO — Verkündung des Urteils
- § 929 Abs. 2 ZPO — Vollziehungsfrist bei einstweiliger Verfügung (1 Monat)
- §§ 704-945 ZPO — Zwangsvollstreckung

## Rechtsprechung zu Verfahrensfristen und Zustellung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Was gehört hinein

- Klageeingang / Antragseingang beim Gericht
- Zahlung des Gerichtskostenvorschusses
- Zustellung der Klageschrift / des Arrestgesuchs
- Klageerwiderung und alle weiteren Schriftsätze (mit Datum)
- Richterliche Verfügungen und Hinweisbeschlüsse
- Beweisbeschlüsse
- Terminsladungen
- Mündliche Verhandlungen (mit Ergebnis / Protokollvermerk)
- Beweisaufnahme (Zeugenvernehmung, Sachverständigengutachten)
- Eingang von Gutachten
- Urteile und Beschlüsse (mit Tenor)
- Rechtsmittelfristen und Einlegung von Rechtsmitteln
- Vollstreckungsmaßnahmen

## Was nicht hinein gehört

- Außerprozessuale Ereignisse (→ Sachverhaltschronologie)
- Rechtliche Bewertungen der Schriftsätze

## Formatvorgabe

```
- **TT.MM.JJJJ** [Kurzbeschreibung des prozessualen Schritts] (Fundstelle: [Blatt])
- ** TT.MM.JJJJ — FRIST:** [Fristbezeichnung — z. B. Berufungsfrist] (Fundstelle: [Blatt])
```

## Hervorhebung von Fristen

Jede prozessrelevante Frist wird hervorgehoben und ans Ende der Chronologie als eigener Block wiederholt:

```
## Fristen und Termine (Übersicht)

| Frist / Termin | Datum | Status |
|---|---|---|
| Berufungsfrist (§ 517 ZPO) | TT.MM.JJJJ | laeuft |
| Begründungsfrist (§ 520 ZPO) | TT.MM.JJJJ | laeuft |
| Nächste mündliche Verhandlung | TT.MM.JJJJ | angesetzt |
```

## Beispiele

```
- **08.02.2023** Eingang der Klageschrift beim Landgericht Frankfurt am Main (Bl. 1)
- **15.02.2023** Anforderung des Gerichtskostenvorschusses (Bl. 5)
- **22.02.2023** Einzahlung des Gerichtskostenvorschusses durch Klägerin (Bl. 7)
- **03.03.2023** Zustellung der Klageschrift an Beklagte (Bl. 9)
- **14.04.2023** Eingang der Klageerwiderung (Bl. 12-45)
- **20.06.2023** Terminsladung zur mündlichen Verhandlung am 15.09.2023 (Bl. 48)
- **15.09.2023** Mündliche Verhandlung; Beweisbeschluss über Einholung Sachverständigengutachten (Bl. 60-62)
- **10.01.2024** Eingang des Sachverständigengutachtens (Bl. 80-140)
- **05.04.2024** Verkündung des Urteils; Klage abgewiesen (Bl. 200-215)
- **05.05.2024 — FRIST:** Berufungsfrist gemäß § 517 ZPO (einen Monat ab Zustellung)
```

## Besonderheiten nach Verfahrensart

**Eilverfahren:** Vollziehungsfrist des § 929 Abs. 2 ZPO besonders hervorheben.

**Strafverfahren:** Eröffnungsbeschluss, Ladungen, Hauptverhandlungstermine, Einlegung von Rechtsmitteln nach § 333 ff. StPO.

**Verwaltungsverfahren:** Widerspruchsverfahren als vorgelagerte Phase einschließen; Klagefrist des § 74 VwGO.

## Qualitätscheck

- [ ] Alle prozessualen Schritte erfasst?
- [ ] Chronologisch sortiert?
- [ ] Fristen hervorgehoben?
- [ ] Fristentabelle vorhanden?
- [ ] Keine außerprozessualen Ereignisse enthalten?
- [ ] Zustellungsdaten als Grundlage der Fristberechnung angegeben?

---

---
name: schwerpunktthemen-identifikation-akten
description: "Schwerpunktthemen Identifikation Akten: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schwerpunktthemen Identifikation Akten

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Schwerpunktthemen Identifikation Akten** im Plugin Aktenauszug zivilgerichtlicher Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `schwerpunktthemen-identifikation` | Anwalt braucht schnellen Überblick über drei bis fuenf rechtliche Hauptstreitpunkte des Verfahrens mit Pinpoint-Zitaten ohne Erfolgsprognose. Normen §§ 139 286 ZPO BGH-Leitsaetze. Prüfraster Streitpunkt-Relevanzbewertung Rechtsprechungs-Verankerung Fundstellen-Praezision. Output Streitpunkt-Liste Relevanz-Einschaetzung Leitsatz-Referenzen. Abgrenzung zu verfahrenszusammenfassung-absatz (Überblick) und rechtsargumente-gegenüberstellung (alle Argumente). |
| `spezial-akten-mandantenkommunikation-entscheidungsvorlage` | Akten: Mandantenkommunikation und Entscheidungsvorlage im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-aktenauszug-tatbestand-beweis-und-belege` | Aktenauszug: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Aktenauszug zivilgerichtlicher Verfahren gilt für **Schwerpunktthemen Identifikation Akten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `schwerpunktthemen-identifikation`

**Fokus:** Anwalt braucht schnellen Überblick über drei bis fuenf rechtliche Hauptstreitpunkte des Verfahrens mit Pinpoint-Zitaten ohne Erfolgsprognose. Normen §§ 139 286 ZPO BGH-Leitsaetze. Prüfraster Streitpunkt-Relevanzbewertung Rechtsprechungs-Verankerung Fundstellen-Praezision. Output Streitpunkt-Liste Relevanz-Einschaetzung Leitsatz-Referenzen. Abgrenzung zu verfahrenszusammenfassung-absatz (Überblick) und rechtsargumente-gegenüberstellung (alle Argumente).

# Schwerpunktthemen-Identifikation

## Zweck

Dieser Skill identifiziert die drei bis fünf zentralen Rechtsfragen, auf denen das Verfahren schwerpunktmäßig beruht. Er hilft dem Anwalt, die Prioritäten für die weitere Bearbeitung zu setzen, ohne eine Einschätzung des Ausgangs zu treffen.

## Triage — kläre vor Identifikation

1. Hat das Gericht bereits Hinweise nach § 139 ZPO erteilt, auf welche Punkte es ankommt?
2. Liegt ein Beweisbeschluss vor (§ 359 ZPO)? Beweisthemen sind automatisch Schwerpunkte.
3. Sind in der Akte BGH- oder OLG-Urteile von den Parteien zitiert? (Hinweis auf rechtlich umstrittene Punkte)
4. Welche Punkte sind in mehreren Schriftsätzen (Klageerwiderung, Replik, Duplik) ausführlich diskutiert?

## Zentrale Normen

- § 139 ZPO — Richterliche Hinweispflicht; Hinweise des Gerichts benennen die Schwerpunkte
- § 286 ZPO — Freie Beweiswürdigung; entscheidungserhebliche Tatsachen sind Schwerpunkte
- § 359 ZPO — Beweisbeschluss; benennt beweisbedürftige Tatsachen
- § 522 Abs. 2 ZPO — Berufungsverwerfung; Schwerpunkt in der Berufung ist Erfolgsaussicht

## Rechtsprechung zu Schwerpunktthemen im Zivilprozess

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Kriterien für ein Schwerpunktthema

Ein Thema ist Schwerpunkt, wenn:

- Es in mehreren Schriftsätzen kontrovers diskutiert wird
- Das Gericht einen ausdrücklichen Hinweis dazu erteilt hat
- Ein Beweisbeschluss zu diesem Punkt ergangen ist
- Rechtsprechung der Parteien zu diesem Punkt zitiert wird
- Die Entscheidung im Verfahren von diesem Punkt maßgeblich abhängt

## Anzahl

Drei bis fünf Schwerpunktthemen. Bei einfachen Verfahren können es weniger sein; bei komplexen Verfahren werden trotzdem nicht mehr als fünf ausgewiesen — die übrigen Fragen werden in den Tabellen erfasst.

## Outputformat

```markdown
## Schwerpunktthemen

### 1. [Bezeichnung des Schwerpunktthemas]

**Beschreibung:** [Kurze Darstellung der Rechtsfrage]

**Parteiposition Kläger:** [Position ohne Wertung]

**Parteiposition Beklagter:** [Position ohne Wertung]

**Einschlägige Rechtsprechung (aus Akte):** [Zitat mit Aktenzeichen und Datum soweit in Schriftsätzen genannt]

**Fundstellen:** [Schriftsatz Bl. ...]

---
```

## Beispiel

### 1. Verjährung des Mangelbeseitigungsanspruchs

**Beschreibung:** Streitig ist, ob der Schadensersatzanspruch der Klägerin nach § 634a Abs. 1 Nr. 1 BGB (zwei Jahre ab Abnahme) bereits verjährt ist.

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Fundstellen:** Klageschrift Bl. 30-32; Klageerwiderung Bl. 55-58.

---

### 2. Wirksamkeit der Abnahme unter Vorbehalt

**Beschreibung:** Streitig ist, ob das unterzeichnete Abnahmeprotokoll einen Vorbehalt enthält oder vorbehaltlos ist.

**Parteiposition Klägerin:** Abnahme erfolgte unter Vorbehalt nach § 640 Abs. 1 S. 2 BGB (Bl. 20-21 Anlage K 2).

**Parteiposition Beklagte:** Protokoll enthält keinen Vorbehalt; vorbehaltlose Abnahme liegt vor.

**Fundstellen:** Klageschrift Bl. 20-22; Klageerwiderung Bl. 48-50.

## Hinweis

Schwerpunktthemen werden neutral dargestellt. Die Identifikation eines Themas als Schwerpunkt bedeutet keine Einschätzung, welche Seite in dieser Frage Recht hat.

## Audit-Hinweis

<!-- AUDIT 27.05.2026 -->
**Halluzinations-Reparatur durchgeführt am 27.05.2026.**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Quellen: dejure.org (https://dejure.org/2016,13484 ; https://dejure.org/2019,4759)

## 2. `spezial-akten-mandantenkommunikation-entscheidungsvorlage`

**Fokus:** Akten: Mandantenkommunikation und Entscheidungsvorlage im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Akten: Mandantenkommunikation und Entscheidungsvorlage

## Spezialwissen: Akten: Mandantenkommunikation und Entscheidungsvorlage
- **Spezialgegenstand:** Akten: Mandantenkommunikation und Entscheidungsvorlage / akten mandantenkommunikation entscheidungsvorlage. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Akten** prüfen.
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

## 3. `spezial-aktenauszug-tatbestand-beweis-und-belege`

**Fokus:** Aktenauszug: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Aktenauszug: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: Aktenauszug: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** Aktenauszug: Tatbestandsmerkmale, Beweisfragen und Beleglage / aktenauszug tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Aktenauszug** prüfen.
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

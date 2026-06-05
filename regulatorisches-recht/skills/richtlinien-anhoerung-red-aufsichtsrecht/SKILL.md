---
name: richtlinien-anhoerung-red-aufsichtsrecht
description: "Richtlinien Anhoerung RED Aufsichtsrecht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Richtlinien Anhoerung RED Aufsichtsrecht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Richtlinien Anhoerung RED Aufsichtsrecht** im Plugin Regulatorisches Recht (Sektoren). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `richtlinien-vergleich` | Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen. KWG WpHG DSGVO DORA GwG. Prüfraster: Strukturvergleich inhaltliche Unterschiede Aenderungshistorie Bedeutung der Aenderungen. Output: Vergleichstabelle Differenzanalyse. Abgrenzung: nicht für Lueckenanalyse (luecken). |
| `spezial-anhoerung-red-team-und-qualitaetskontrolle` | Anhoerung: Red-Team und Qualitätskontrolle im Plugin regulatorisches recht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-aufsichtsrecht-erstpruefung-und-mandatsziel` | Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel im Plugin regulatorisches recht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Regulatorisches Recht (Sektoren) gilt für **Richtlinien Anhoerung RED Aufsichtsrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `richtlinien-vergleich`

**Fokus:** Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen. KWG WpHG DSGVO DORA GwG. Prüfraster: Strukturvergleich inhaltliche Unterschiede Aenderungshistorie Bedeutung der Aenderungen. Output: Vergleichstabelle Differenzanalyse. Abgrenzung: nicht für Lueckenanalyse (luecken).

# Richtlinien-Diff

## Zweck

Dieser Skill vergleicht eine neue oder geänderte Aufsichtsnorm / Verlautbarung mit einer bestehenden internen Richtlinie. Das Ergebnis ist ein strukturierter Diff: Welche Anforderungen der neuen Norm sind in der Richtlinie abgedeckt? Wo weicht die Richtlinie ab? Wo hat die Norm Neues hinzugefügt oder Altes gestrichen?

Typische Einsatzfelder:
- Neue MaRisk-Novelle gegen bestehende Risikomanagement-Richtlinie
- Geändertes BaFin-Rundschreiben BAIT/VAIT gegen IT-Sicherheitsrichtlinie
- Neue EBA-Leitlinien gegen interne Compliance-Policies
- Geändertes BMF-Schreiben gegen steuerliche Richtlinien / AO-Verfahrenshandbuch

## Eingaben

- **Neue Norm / Verlautbarung:** Text oder Link (BaFin-Rundschreiben, MaRisk-Modul, EBA-Leitlinie, Gesetzestext)
- **Bestehende Richtlinie:** Bestandsdokument (hochgeladen oder aus Bibliothek)
- **Scope:** Optional – nur bestimmte Abschnitte vergleichen
- Optional: Vorheriger Diff-Lauf zum Vergleich

## Ablauf

### 1. Neue Norm strukturieren

Neue Norm / Verlautbarung lesen und in nummerierte Anforderungen zerlegen:

| Nr. | Abschnitt | Anforderungstext (Kurzfassung) | Verbindlichkeit |
|---|---|---|---|
| A01 | AT 4.3.2 | Aufbewahrung von Daten mind. 10 Jahre | Verbindlich |
| A02 | AT 4.3.2 | Backup-Konzept mit Wiederherstellungstest | Verbindlich |
| A03 | AT 4.3.2 | Dokumentation der Datenklassifizierung | Empfehlung |

Verbindlichkeitskennzeichnung:
- **Verbindlich:** "hat sicherzustellen", "muss", "sind zu"
- **Empfehlung/Best Practice:** "sollte", "kann", "wird empfohlen"

### 2. Bestehende Richtlinie strukturieren

Bestehende Richtlinie lesen und relevante Abschnitte den neuen Anforderungen zuordnen.

### 3. Diff-Tabelle erstellen

| Anforderung (Norm) | Deckung in Richtlinie | Status | Differenz |
|---|---|---|---|
| A01: Datenhaltung 10 J. | § 4 Abs. 2 IKS-Richtlinie: 7 Jahre | 🔴 Abweichung | Frist 3 J. kürzer |
| A02: Backup-Konzept | § 5 IKS-Richtlinie: vollständig | 🟢 Gedeckt | – |
| A03: Datenklassifizierung | Keine Regelung | 🟡 Lücke (Best Practice) | Empfehlung fehlt |
| – | § 7 IKS-Richtlinie: Prüfprotokoll | ⚪ Überschuss | Norm enthält keine solche Pflicht |

Status-Legende:
- 🔴 **Abweichung:** Richtlinie weicht von verbindlicher Anforderung ab
- 🟡 **Lücke:** Anforderung fehlt in Richtlinie (verbindlich: 🔴 potentiell; Best Practice: 🟡)
- 🟢 **Gedeckt:** Anforderung vollständig und korrekt abgebildet
- ⚪ **Überschuss:** Richtlinie enthält Regelung, die die Norm nicht fordert (kein Problem, aber zur Kenntnis)

### 4. Zusammenfassung

```
Diff-Zusammenfassung: [Normtitel] vs. [Richtlinientitel]
Analysiert: N Normabschnitte | N Richtlinienabschnitte

Handlungsbedarf:
🔴 N Abweichungen (verbindliche Anforderungen, Richtlinie weicht ab)
🟡 N Lücken (neue Anforderungen ohne Entsprechung)
🟢 N gedeckt
⚪ N Überschüsse (Richtlinie enthält Mehr als die Norm fordert)
```

### 5. Empfehlung

Für jede 🔴-Abweichung und jede wesentliche 🟡-Lücke:
- Konkrete Formulierungsänderung vorschlagen (Ausgangspunkt für `/richtlinien-neufassung`)
- Frist aus der Verlautbarung angeben
- Eskalationsbedarf markieren (`[prüfen]` bei Unklarheit)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Einschlägige Normen und Verlautbarungen:
- BaFin-Rundschreiben 09/2017 (BA) – MaRisk, alle Novellen [Modellwissen – prüfen auf aktuelle Fassung]
- BaFin-Rundschreiben 10/2018 (BA) – BAIT [Modellwissen – prüfen]
- BaFin-Rundschreiben 10/2017 (VA) – VAIT [Modellwissen – prüfen]
- BaFin-Rundschreiben 05/2021 (IO) – ZAIT (Zahlungsdienstleister IT) [Modellwissen – prüfen]
- EBA-Leitlinien EBA/GL/2019/04 – IKT-Risikomanagement [Modellwissen – prüfen]
- DORA Art. 5 ff. (EU) 2022/2554 (ICT Risk Management)
- § 25a KWG (Ordnungsgemäße Geschäftsorganisation)

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.

## Ausgabeformat

- **Diff-Tabelle:** Alle Anforderungen mit Deckungsgrad
- **Zusammenfassung:** Kennzahlen
- **Empfehlungen:** Konkrete Formulierungsänderungen als Ausgangspunkt für Neufassung
- Reviewer-Header und Prüfernotiz wie in CLAUDE.md definiert

## Beispiel

**Eingabe:** `/regulatorisches-recht:richtlinien-vergleich MaRisk-AT-4.3.2-Novelle-2023`

**Ausgabe (Auszug):**

> **⚠️ Prüfernotiz**
> - **Quellen:** MaRisk RS 09/2017 Novelle 2023 [Modellwissen – prüfen gegen bafin.de], IKS-Richtlinie v. 01.03.2023 [Nutzer-Input]
> - **Gelesen:** AT 4.3.2 vollständig; IKS-Richtlinie §§ 1–12
> - **Zu Ihrer Einschätzung:** 2 Positionen mit 🔴 markiert `[prüfen]`

---

**Diff: MaRisk AT 4.3.2 (Novelle 2023) vs. IKS-Richtlinie (Stand: 01.03.2023)**

| Anforderung (Norm) | Deckung in Richtlinie | Status | Differenz |
|---|---|---|---|
| Datenhaltung ≥ 10 Jahre | § 4 Abs. 2: 7 Jahre | 🔴 | Verlängerung um 3 Jahre erforderlich `[prüfen]` |
| Backup-Konzept mit Test | § 5 Abs. 1–3 | 🟢 | – |
| Datenklassifizierungsdoku. | Keine Regelung | 🟡 | Abschnitt zu ergänzen |

**Empfohlene Änderung für 🔴:**
> § 4 Abs. 2 IKS-Richtlinie: "Aufbewahrungsfrist von 7 Jahren" → **"mindestens 10 Jahren"** (Anpassung an MaRisk AT 4.3.2 Novelle 2023).

**Nächster Schritt:** `/regulatorisches-recht:richtlinien-neufassung` für den vollständigen Neufassungsentwurf.

## Risiken / typische Fehler

- **Nur Wortlaut-Vergleich:** Eine Richtlinie kann die Norm wörtlich übernehmen, sie aber organisatorisch nicht umsetzen. Hinweis, dass der Diff nur den Dokumenteninhalt vergleicht, nicht die gelebte Praxis.
- **Verlautbarungsversion:** MaRisk und BAIT werden novelliert; stets Version und Datum der verwendeten Norm angeben und prüfen, ob aktuell.
- **Best-Practice vs. verbindlich:** EBA-Leitlinien sind nach Art. 16 EBA-VO "comply or explain" – nicht 1:1 verbindlich. Status klar kennzeichnen.
- **Proportionalitätsgrundsatz:** Nicht jede Norm gilt für jede Institutsgröße gleich (§ 25a Abs. 1 S. 3 KWG). Adressatenkreis prüfen und im Diff ausweisen.
## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kernnormen:** Art. 288 AEUV — §§ 133, 157 BGB — § 47 GGO (Ressortabstimmung Richtlinien-Vergleich)

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## 2. `spezial-anhoerung-red-team-und-qualitaetskontrolle`

**Fokus:** Anhoerung: Red-Team und Qualitätskontrolle im Plugin regulatorisches recht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Anhoerung: Red-Team und Qualitätskontrolle

## Spezialwissen: Anhoerung: Red-Team und Qualitätskontrolle
- **Spezialgegenstand:** Anhoerung: Red-Team und Qualitätskontrolle / anhoerung red team und qualitaetskontrolle. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, RDG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Anhoerung** prüfen.
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

## 3. `spezial-aufsichtsrecht-erstpruefung-und-mandatsziel`

**Fokus:** Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel im Plugin regulatorisches recht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel / aufsichtsrecht erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, RDG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Aufsichtsrecht** prüfen.
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

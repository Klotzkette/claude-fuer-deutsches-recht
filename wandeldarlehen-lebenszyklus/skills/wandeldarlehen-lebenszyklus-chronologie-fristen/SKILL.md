---
name: wandeldarlehen-lebenszyklus-chronologie-fristen
description: "Chronologie Fristen: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Chronologie Fristen

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Chronologie Fristen** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin wandeldarlehen-lebenszyklus: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin wandeldarlehen-lebenszyklus: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Chronologie Fristen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin wandeldarlehen-lebenszyklus: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

# Chronologie und Belegmatrix

## Aufgabe
Dieser Prüffeld ordnet alle Lebenszyklus-Daten eines Wandeldarlehens chronologisch: Term Sheet, Closing, Auszahlung, Zinszahlungen, Trigger-Ereignisse (Folge-Runde, Maturity, Insolvenz), Wandlung, Eintragung.

## Pflicht-Timeline Wandeldarlehen
- **Term-Sheet-Datum** und -Verbindlichkeitsumfang.
- **Closing / Unterzeichnung CLA**.
- **Auszahlungsdatum** (regelmäßig auf Sperrkonto / Treuhand, dann Freigabe an Gesellschaft).
- **Zinszahlung / Zinslauf** (oft endfällig "PIK -- Payment in Kind").
- **Maturity-Datum** (12-36 Monate).
- **Trigger-Ereignis Folge-Runde:** Datum der qualifizierten Finanzierungsrunde; Term-Sheet-Vorstellung beim Investor.
- **Kapitalerhöhungsbeschluss** (§ 55 GmbHG / § 182 AktG) -- Notartermin mit Vorlauf 1-2 Wochen.
- **Eintragung im Handelsregister.**
- **Insolvenz-Trigger:** Antragspflicht § 15a InsO (3 Wochen Zahlungsunfähigkeit, 6 Wochen Überschuldung); ggf. Rangrücktritt-Erklärung vor Insolvenz nachweisen.

## Belegmatrix
- Datum | Ereignis | Vertragsstelle / Beschluss / Bescheid | Norm-Anker | Steuerfolge (KapSt § 43 EStG, § 17 EStG) | Relevanz | offene Frage.

## Anti-Muster
- Unklare Datum-Reihenfolge bei Maturity, Folge-Runde und Insolvenzantragspflicht -> kann zu Anfechtbarkeit nach §§ 129 ff. InsO führen.
- Notartermin zu knapp vor Maturity -> Wandlung verfehlt; Auseinandersetzung über Cap und Discount.

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin wandeldarlehen-lebenszyklus: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieser Prüffeld markiert in Wandeldarlehens-Mandaten typische Fristen und Eskalationspunkte: Maturity, Wandlungsfristen, Notartermin, Insolvenzgefahr (Rangrücktritt erforderlich?), KapSt-Anmeldungen.

## Fristen Wandeldarlehen
- **Maturity (Laufzeit):** 12-36 Monate marktüblich; Vorlaufzeit für Wandlung oder Rückzahlung 3-6 Monate einplanen.
- **Wandlungstrigger Closing Folge-Runde:** Notartermin mit Vorlauf 1-2 Wochen; Beschluss Kapitalerhöhung (§ 55 GmbHG / § 182 AktG) vorbereiten.
- **Kapitalertragsteuer:** § 43 EStG -- Anmeldung und Abführung der KapSt durch Schuldner der Zinsen unverzüglich nach Zufluss.
- **Sachkapitalerhöhung mit Werthaltigkeitsbescheinigung:** Notartermin und Bescheinigung Wirtschaftsprüfer.
- **Insolvenzantragspflicht (§ 15a InsO):** 3 Wochen bei Zahlungsunfähigkeit, 6 Wochen bei Überschuldung. Rangrücktritt (§ 39 Abs. 2 InsO) muss vorab vereinbart und qualifiziert sein.

## Risikoampel
- **Rot:** Maturity erreicht ohne Wandlung oder Verlängerung; Insolvenzgefahr ohne Rangrücktritt; KapSt-Pflicht versäumt.
- **Gelb:** Folge-Runde verzögert sich; Bewertungs-Cap zu eng, droht Verwässerung der Gründer; SAFE-Strukturen ohne DE-Anpassung.
- **Grün:** Term Sheet verbindlich, Notar terminiert, Cap Table simuliert.

## Anti-Muster
- Wandeldarlehen mit Sicherungsabrede ohne Rangrücktritt -- Insolvenzfeste Strukturierung fehlt.
- "We Are SAFE" 1:1 nach US-Vorlage ohne Notar-/GmbH-Form -- nicht durchsetzbar.

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

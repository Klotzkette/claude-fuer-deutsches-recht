---
name: mehrere-wandeldarlehen-parallel
description: "Mehrere parallele Wandeldarlehen von verschiedenen Investoren koordinieren und Konflikte erkennen. §§ 488 ff. BGB § 39 InsO Rangrücktritt. Prüfraster: Pari-passu-Stellung Rangregelungen Wandlungsrechte Verwasserungsschutz Vesting. Output: Übersichtsmatrix Konfliktliste Handlungsempfehlung. Abgrenzung: nicht für Einzeldarlehen-Erstellung im Wandeldarlehen Lebenszyklus: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Mehrere parallele Wandeldarlehen

## Arbeitsbereich

Mehrere parallele Wandeldarlehen von verschiedenen Investoren koordinieren und Konflikte erkennen. §§ 488 ff. BGB § 39 InsO Rangrücktritt. Prüfraster: Pari-passu-Stellung Rangregelungen Wandlungsrechte Verwasserungsschutz Vesting. Output: Übersichtsmatrix Konfliktliste Handlungsempfehlung. Abgrenzung: nicht für Einzeldarlehen-Erstellung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Dieser Skill behandelt die Besonderheiten, wenn gleichzeitig mehrere Wandeldarlehen von verschiedenen Lenders bestehen. Er klärt Stack-Order, MFN-Pflichten, gleichzeitige Wandlung und kombinierte Cap-Table-Auswirkungen. Phase C des Lebenszyklus.

## Eingaben

- Liste aller Wandeldarlehen: Lender, Betrag, Datum, Laufzeit, Cap, Discount, MFN-Klausel
- Aktuelles Wandlungsereignis: für welche Lenders gilt es?
- Vertragliche Stack-Order oder Gleichrangigkeit?
- MFN-Klauseln im jeweiligen Vertrag?
- Vollverwässerte Anteile vor Wandlung aller Lenders

## Rechtlicher Rahmen

### Primärnormen
- § 4.7 Wandeldarlehensvertrag (MFN-Klausel: günstigere Rechte automatisch gültig)
- § 39 Abs. 2 InsO (Gleichrang der Nachrangforderungen untereinander)
- § 55 GmbHG (Kapitalerhöhung – mehrere Übernahmen gleichzeitig möglich)
- § 328 BGB (Drittschutz der Rangrücktrittsvereinbarung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Bestandsaufnahme aller Wandeldarlehen
Tabelle: Lender / Betrag / Datum / Cap / Discount / MFN / Rangrücktritt / Wandlungsstatus. Zeitliche Reihenfolge der Darlehensgewährung (relevant für MFN).

### 2. MFN-Prüfung
Enthält ein späteres Wandeldarlehen einen günstigeren Cap oder Discount? Dann haben frühere Lender (mit MFN-Klausel) Anspruch auf diese günstigeren Konditionen. Automatischer Anpassungsmechanismus.

### 3. Gleichzeitige Wandlung
Alle Lenders wandeln zum gleichen Wandlungsereignis: Berechne Wandlungssumme je Lender (Darlehen + Zinsen). Berechne Wandlungspreis je Lender (nach je eigenem Cap/Discount). Addiere neue Anteile aller Lenders. Dann: Kapitalerhöhungsrunde.

### 4. Kapitalerhöhungsbeschluss für mehrere Lenders
Ein Beschluss kann mehrere Übernahmen gleichzeitig enthalten (§ 55 Abs. 1 GmbHG). Gesellschafterliste nach Kapitalerhöhung: alle neuen Gesellschafter eintragen.

### 5. Stack-Order im Insolvenzfall
Alle Wandeldarlehen mit qualifiziertem Rangrücktritt: gleichrangig nach § 39 Abs. 2 InsO. Keine Priorität unter sich, alle hinter § 38/39 Abs. 1-Gläubigern.

### 6. Kombinierte Cap-Table-Auswirkung
Post-Money-Cap-Table mit allen Lenders und neuen Investoren. Gesamtverwässerung der Altgesellschafterinnen = Summe der Einzelverwässerungen.

## Beispiel: Zwei Wandeldarlehen gleichzeitig

| Parameter | Northstar | Angel-Investor B |
|---|---|---|
| Darlehen | EUR 250000 | EUR 100000 |
| Zinsen | EUR 25694 | EUR 10277 |
| Wandlungssumme | EUR 275694 | EUR 110277 |
| Cap | EUR 4000000 | EUR 3500000 |
| Discount | zwanzig Prozent | fünfzehn Prozent |
| Anteile (100 vor Runde, Pre-Money EUR 6 Mio) | | |
| Cap-Preis Northstar | EUR 40000 | — |
| Cap-Preis Angel B | — | EUR 35000 |
| Neue Anteile | 7 | 4 |
| MFN: Angel B Cap günstiger | Northstar erhält MFN → Cap EUR 35000 | — |
| Neue Anteile Northstar (mit MFN) | 275694/35000 = 7.88 → 8 | 4 |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| MFN-Trigger übersehen | Lender erhält schlechtere Konditionen | MFN-Prüfung durchgeführt | MFN automatisch ausgelöst |
| Stack-Order nicht vereinbart | Rangstreit im Insolvenzfall | Mündliche Abrede | Schriftliche Stack-Order |
| Zu viele Lenders auf einmal | Cap-Table komplex, HR-Eintragung aufwändig | Drei bis vier Lenders | Maximal zwei |
| Kapitalerhöhungsbeschluss nur für einen Lender | Zweite Kapitalerhöhung nötig | Beschluss erweiterbar | Umfassender Beschluss |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/cap-table-update-pre-post/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 55 ff. oder InsO § 39 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 39 InsO (Nachrang Gesellschafterdarlehen) → § 135 InsO (Anfechtung) → §§ 55, 56 GmbHG (Kapitalerhöhung bei Wandlung) → § 5 Abs. 1 GmbHG (Mindest-Nennbetrag Anteile 1 EUR) → § 40 GmbHG (Gesellschafterliste parallele Updates)

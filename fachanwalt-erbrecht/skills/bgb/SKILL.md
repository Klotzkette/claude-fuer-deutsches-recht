---
name: bgb
description: "BGB im Plugin Fachanwalt Erbrecht: prüft konkret Mandantenkommunikation im Plugin fachanwalt-erbrecht, Red-Team Qualitygate im Plugin fachanwalt-erbrecht, BGB. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# BGB

## Arbeitsbereich

**BGB** ordnet den Fall über die tragenden Prüfungslinien: Mandantenkommunikation im Plugin fachanwalt-erbrecht, Red-Team Qualitygate im Plugin fachanwalt-erbrecht, BGB. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fachanwalt-erbrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fachanwalt-erbrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `spezial-bgb-fristen-form-und-zuständigkeit` | BGB: Fristen, Form, Zuständigkeit und Rechtsweg im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin fachanwalt-erbrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

### Mandantenkommunikation

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandantenkommunikation` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin fachanwalt-erbrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin fachanwalt-erbrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

### Red-Team Qualitygate

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Red-Team Qualitygate` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin fachanwalt-erbrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## 3. `spezial-bgb-fristen-form-und-zuständigkeit`

**Fokus:** BGB: Fristen, Form, Zuständigkeit und Rechtsweg im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

### BGB: Fristen, Form, Zuständigkeit und Rechtsweg

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `BGB: Fristen, Form, Zuständigkeit und Rechtsweg` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: BGB: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** BGB, EU, ErbVO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **BGB** prüfen.
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

---
name: erbfall-intake-erbrecht-erbschein
description: "Erbfall Intake Erbrecht Erbschein: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Erbfall Intake Erbrecht Erbschein

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Erbfall Intake Erbrecht Erbschein** im Plugin Fachanwalt Erbrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-erbfall-intake-und-nachlassordnung` | Erbfall-Intake, Nachlassordnung und erste Fristen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-erbrecht-tatbestand-beweis-und-belege` | Erbrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage im Erbrecht: fachlich vertiefter Fachmodul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `spezial-erbschein-behoerden-gericht-und-registerweg` | Erbschein: Behörden-, Gerichts- oder Registerweg im Erbrecht: fachlich vertiefter Fachmodul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |

## Arbeitsweg

Im Plugin Fachanwalt Erbrecht gilt für **Erbfall Intake Erbrecht Erbschein**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-erbfall-intake-und-nachlassordnung`

**Fokus:** Erbfall-Intake, Nachlassordnung und erste Fristen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

# Erbfall-Intake, Nachlassordnung und erste Fristen

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erbfall-Intake, Nachlassordnung und erste Fristen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `fachanwalt-erbrecht`. Kontext des Plugins: Plugin Fachanwalt für Erbrecht. BGB Erbrecht §§ 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaftsteuer EU-ErbVO. Schnittstellen Plugin steuerrecht-anwalt-und-berater kanzlei-allgemein.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Erbfall-Intake, Nachlassordnung und erste Fristen** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `spezial-erbrecht-tatbestand-beweis-und-belege`

**Fokus:** Erbrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage im Erbrecht: fachlich vertiefter Fachmodul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Erbrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erbrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Erbrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** Erbrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage / erbrecht tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB, EU, ErbVO.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Erbrecht** prüfen.
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

## 3. `spezial-erbschein-behoerden-gericht-und-registerweg`

**Fokus:** Erbschein: Behörden-, Gerichts- oder Registerweg im Erbrecht: fachlich vertiefter Fachmodul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Erbschein: Behörden-, Gerichts- oder Registerweg

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erbschein: Behörden-, Gerichts- oder Registerweg` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Erbschein: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Erbschein: Behörden-, Gerichts- oder Registerweg / erbschein behoerden gericht und registerweg. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB, EU, ErbVO, ErbV.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Erbschein** prüfen.
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

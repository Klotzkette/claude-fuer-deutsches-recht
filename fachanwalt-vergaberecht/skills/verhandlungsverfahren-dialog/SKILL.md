---
name: verhandlungsverfahren-dialog
description: "Verhandlungsverfahren Dialog: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verhandlungsverfahren Dialog

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Verhandlungsverfahren Dialog** im Plugin Fachanwalt Vergaberecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fachanwalt-vergaberecht-verhandlungsverfahren-dialog` | Verhandlungsverfahren mit Teilnahmewettbewerb und wettbewerblichen Dialog strukturieren: Auftraggeber braucht flexibles Verfahren fuer komplexe Beschaffung. Normen: §§ 119 GWB, 17 VgV (Verhandlungsverfahren), § 18 VgV (Wettbewerblicher Dialog), § 19 VgV (Innovationspartnerschaft). Pruefraster: Voraussetzungen § 14 Abs. 3 VgV, Teilnahmewettbewerb, Mindestanforderungen, Verhandlungsphasen, Reduktion Loesungen, Wahrung Gleichbehandlung waehrend Verhandlung. Output Verfahrensplan, Bewertungsmatrix Verhandlungsphasen. Abgrenzung: Offenes Verfahren siehe fachanwalt-vergaberecht-orientierung; Wertung siehe fachanwalt-vergaberecht-zuschlagskriterien-wertungsschema. |
| `spezial-nachpruefungsverfahren-textbausteine` | Nachpruefungsverfahren: Schriftsatz-, Brief- und Memo-Bausteine im Plugin fachanwalt vergaberecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-uvgo-fristen-form-und-zustaendigkeit` | Uvgo: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt vergaberecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `verfahrenswahl-kompass` | Verfahrensart waehlen und begruenden: offen, nichtoffen, Verhandlungsverfahren, wettbewerblicher Dialog, Innovationspartnerschaft, UVgO-Verfahren, VOB/A und Direktvergabe. |

## Arbeitsweg

Im Plugin Fachanwalt Vergaberecht gilt für **Verhandlungsverfahren Dialog**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fachanwalt-vergaberecht-verhandlungsverfahren-dialog`

**Fokus:** Verhandlungsverfahren mit Teilnahmewettbewerb und wettbewerblichen Dialog strukturieren: Auftraggeber braucht flexibles Verfahren fuer komplexe Beschaffung. Normen: §§ 119 GWB, 17 VgV (Verhandlungsverfahren), § 18 VgV (Wettbewerblicher Dialog), § 19 VgV (Innovationspartnerschaft). Pruefraster: Voraussetzungen § 14 Abs. 3 VgV, Teilnahmewettbewerb, Mindestanforderungen, Verhandlungsphasen, Reduktion Loesungen, Wahrung Gleichbehandlung waehrend Verhandlung. Output Verfahrensplan, Bewertungsmatrix Verhandlungsphasen. Abgrenzung: Offenes Verfahren siehe fachanwalt-vergaberecht-orientierung; Wertung siehe fachanwalt-vergaberecht-zuschlagskriterien-wertungsschema.

# Verhandlungsverfahren und wettbewerblicher Dialog

## Aufgabe
Verhandlungsverfahren mit Teilnahmewettbewerb, wettbewerblichen Dialog oder Innovationspartnerschaft strukturieren. Fokus: zulaessige Verfahrenswahl, faire Verhandlungsphasen, Wahrung der Gleichbehandlung.

## Einstieg
1. Standardleistung oder komplexer Beschaffungsbedarf?
2. Marktrecherche durchgefuehrt? Mindestanforderungen klar formulierbar?
3. Schwellenwert oberschwellig (sonst Verhandlungsvergabe nach UVgO)?
4. Erwartete Bieterzahl ausreichend (Mindestens 3 Teilnehmer fuer Verhandlungsverfahren)?
5. Schutzbedarf vertraulicher Bieterinformationen?

## Verfahrenswahl
### Verhandlungsverfahren mit Teilnahmewettbewerb § 17 VgV
Voraussetzung § 14 Abs. 3 VgV:
- Beduerfnisse durch frei verfuegbare Loesungen nicht zu decken,
- innovative Anforderungen,
- nicht ohne vorherige Verhandlung vergebbar (geistige Leistungen, Konzeption),
- bisherige offene Verfahren erfolglos,
- besondere Umstaende rechtlich/technisch/finanziell.

### Wettbewerblicher Dialog § 18 VgV
Wie § 17 VgV plus zusaetzliche Komplexitaet, die eine Loesungsfindung im Dialog erfordert (z. B. PPP-Projekte, IT-Grossvorhaben). Verfahrensphasen: Bekanntmachung -> Teilnahmewettbewerb -> Dialog -> Endangebote.

### Innovationspartnerschaft § 19 VgV
Wenn Loesung nicht am Markt verfuegbar; Phasenmodell Forschung/Entwicklung + spaetere Beschaffung.

## Verfahrensaufbau Verhandlungsverfahren
1. **Bekanntmachung** mit Mindestanforderungen, Zuschlagskriterien, Verhandlungsmodalitaeten.
2. **Teilnahmewettbewerb**: Bewerber, Mindestkriterien Eignung; Auswahl 3-6 Teilnehmer.
3. **Aufforderung zur Angebotsabgabe** mit detaillierten Auftragsunterlagen.
4. **Erstangebote**.
5. **Verhandlungsphase**: Klaerung Bieterloesungen, Reduktion auf Best-and-Final-Offer (BAFO) zulaessig (§ 17 Abs. 11 VgV).
6. **Endangebote** und Zuschlag.

## Gleichbehandlungsgebot in Verhandlung
- Gleiche Informationen an alle verbleibenden Bieter.
- Keine Preisgabe vertraulicher Bieterinformationen.
- Aenderung Mindestanforderungen unzulaessig; Aenderung Zuschlagskriterien grundsaetzlich unzulaessig.
- Protokollierung jeder Verhandlung im Vergabevermerk.

## Wettbewerblicher Dialog: Phasen
1. **Aufforderung zur Teilnahme am Dialog** mit Aufgabenbeschreibung.
2. **Dialog**: Erorterung aller Aspekte zur Loesungsfindung; iterative Reduktion Loesungen.
3. **Aufforderung zur Endangebotsabgabe** mit final festgelegtem Loesungskonzept.
4. **Zuschlag** auf wirtschaftlichstes Endangebot.

## Typische Fehler
- Verhandlungsverfahren ohne Vorliegen der Voraussetzungen § 14 Abs. 3 VgV (haeufig in OLG-Beschwerden).
- Aenderung der Zuschlagskriterien in der Verhandlungsphase.
- Verraten von Bieterinformationen.
- Kein BAFO obwohl Verhandlung ergebnislos.
- Dialogphase wird zur Mengen-Bieter-Reduktion ohne Substanz missbraucht.

## Output
- Verfahrenswahl-Pruefvermerk § 14 Abs. 3 VgV.
- Verfahrensplan mit Phasen, Fristen, BAFO-Optionen.
- Vergabevermerk-Vorlage fuer Verhandlungsprotokolle.

## Quellenregel
OLG-Linien zu § 14 Abs. 3 VgV und zur Reduktion von Loesungen im Dialog vor Ausgabe ueber dejure.org / openjur.de pruefen.


## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 2. `spezial-nachpruefungsverfahren-textbausteine`

**Fokus:** Nachpruefungsverfahren: Schriftsatz-, Brief- und Memo-Bausteine im Plugin fachanwalt vergaberecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Nachpruefungsverfahren: Schriftsatz-, Brief- und Memo-Bausteine

## Spezialwissen: Nachpruefungsverfahren: Schriftsatz-, Brief- und Memo-Bausteine
- **Spezialgegenstand:** Nachpruefungsverfahren: Schriftsatz-, Brief- und Memo-Bausteine / nachpruefungsverfahren textbausteine. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** GWB, VgV, UVgO, SektVO, KonzVgV, VOB, EU, RL, OLG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Nachpruefungsverfahren** prüfen.
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


## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 3. `spezial-uvgo-fristen-form-und-zustaendigkeit`

**Fokus:** Uvgo: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt vergaberecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Uvgo: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Uvgo: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Uvgo: Fristen, Form, Zuständigkeit und Rechtsweg / uvgo fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** GWB, VgV, UVgO, SektVO, KonzVgV, VOB, EU, RL, OLG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Uvgo** prüfen.
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


## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 4. `verfahrenswahl-kompass`

**Fokus:** Verfahrensart waehlen und begruenden: offen, nichtoffen, Verhandlungsverfahren, wettbewerblicher Dialog, Innovationspartnerschaft, UVgO-Verfahren, VOB/A und Direktvergabe.

# Verfahrenswahl-Kompass

## Zweck

Dieser Skill erweitert das Fachanwalt-Vergaberecht-Plugin zu einer echten Vergabe-Workbench. Er soll das richtige Verfahren aus Bedarf, Markt, Komplexitaet, Dringlichkeit und Rechtsrahmen ableiten. Er arbeitet fuer Auftraggeber, Bieter, Beigeladene, Zuwendungsempfaenger, Projektsteuerer und Kanzleien, sofern die Perspektive zu Beginn klar markiert wird.

## Sofortmodus

1. Rolle klaeren: Auftraggeber, Bieter, Beigeladener, Foerdermittelempfaenger, Projektsteuerer oder Kanzlei.
2. Verfahrensstand klaeren: Markterkundung, Bekanntmachung, Angebotsphase, Wertung, Paragraph 134 GWB, Zuschlag, Vertrag, Nachpruefung, Beschwerde oder Schadensersatz.
3. Schwellenwert und Rechtsweg pruefen: Oberschwelle, Unterschwelle, Sektoren, Konzession, Verteidigung/Sicherheit, Foerdermittel oder Sonderregime.
4. Fristen sichern: Ruge, Angebotsfrist, Stillhaltefrist, 15-Tage-Frist nach Nichtabhilfe, Beschwerdefrist, Paragraph 135 GWB-Fristen.
5. Erst danach in die materielle Pruefung gehen.

## Arbeitsweise

- Baue zuerst eine kleine Tabelle mit `Tatsache`, `Beleg`, `rechtliche Bedeutung`, `Risiko`, `naechster Schritt`.
- Trenne strikt zwischen gesicherten Tatsachen, plausiblen Annahmen und offenen Pruefpunkten.
- Wenn der Nutzer Anfaenger ist, erklaere jedes vergaberechtliche Kunstwort in einem Satz und liefere danach sofort die Handlung.
- Wenn der Nutzer erfahren ist, liefere direkt Matrix, Schriftsatzkern, Vermerk oder Entscheidungsvorlage.
- Bei schwellenwert-, formular-, TED/eForms-, Wettbewerbsregister-, Landes- oder EU-Fragen einen Live-/Aktualitaetscheck verlangen, bevor Zahlen oder Formularlogik tragend verwendet werden.

## Pflicht-Output

- Kurzbild in drei Saetzen.
- Ampel: Frist, Zustaendigkeit/Rechtsweg, Sachverhalt, Belege, Erfolgsaussicht, Kostenrisiko.
- Matrix oder Padlet-Block, wenn mehr als drei Themen/Fehler/Unterlagen betroffen sind.
- Konkreter naechster Schritt mit Adressat, Frist, benoetigten Anlagen und Entwurfsformat.

## Typische Outputs

Verfahrensmatrix, Begruendung, Risiken, Alternativen.

## Qualitaetsgates

- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Datum, Aktenzeichen und frei oder amtlich pruefbarer Quelle absichern.
- Keine ungeprueften Schwellenwerte. Fuer 2026/2027 sind die offiziellen EU-/nationalen Quellen vor tragender Verwendung zu pruefen.
- Keine pauschale Ruge. Jeder Vergabeverstoss braucht konkrete Tatsache, verletzte Regel, Kausalitaet/Chance und begehrte Abhilfe.
- Auftraggeberseitig immer dokumentieren: Warum durfte genau diese Entscheidung zu genau diesem Zeitpunkt getroffen werden?
- Bieterseitig immer taktisch pruefen: Rugen, nachfragen, Angebot abgeben, Nachpruefung, Vergleich oder Schadensersatz.

## Anschluss-Skills

- `vergabe-os-master-orchestrator` fuer Gesamtsteuerung.
- `schwellenwerte-2026-2027-livecheck` fuer Schwellenwert und Rechtsweg.
- `workflow-chronologie-und-belegmatrix` fuer Aktenarbeit.
- `nachpruefungsantrag-powerdraft` fuer VK-Verfahren.
- `mandantenpadlet-vergabe-canvas` fuer komplexe Mehrthemenfaelle.


## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

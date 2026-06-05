---
name: hauptverhandlung-sonderfall-messakte-messung
description: "Hauptverhandlung Sonderfall Messakte Messung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Hauptverhandlung Sonderfall Messakte Messung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Hauptverhandlung Sonderfall Messakte Messung** im Plugin Verkehrs-OWi-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-hauptverhandlung-sonderfall-und-edge-case` | Hauptverhandlung: Sonderfall und Edge-Case-Prüfung im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-messakte-formular-portal-und-einreichung` | Messakte: Formular, Portal und Einreichungslogik im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-messung-fahrverbot-punkte` | Messung, Punkte, Fahrverbot und Verteidigungsziel im Verkehrs-OWi: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |

## Arbeitsweg

Im Plugin Verkehrs-OWi-Verteidigung gilt für **Hauptverhandlung Sonderfall Messakte Messung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-hauptverhandlung-sonderfall-und-edge-case`

**Fokus:** Hauptverhandlung: Sonderfall und Edge-Case-Prüfung im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Hauptverhandlung: Sonderfall und Edge-Case-Prüfung

## Spezialwissen: Hauptverhandlung: Sonderfall und Edge-Case-Prüfung
- **Spezialgegenstand:** Hauptverhandlung: Sonderfall und Edge-Case-Prüfung / hauptverhandlung sonderfall und edge case. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Hauptverhandlung** prüfen.
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

## OWi-Hauptverhandlung Edge-Cases Bausteine
- **Sonderfall 1: Schriftliches Verfahren § 72 OWiG:**
 - Voraussetzung: Einverstaendnis Betroffener; Geldbusse bis 250 EUR.
 - Vorteil: keine Verhandlung, keine Reisekosten.
 - Nachteil: keine Beweisaufnahme, keine persoenliche Eindruck.
- **Sonderfall 2: Berufskraftfahrer mit drohendem Fahrverbot:**
 - **Argument Existenzbedrohung:** monatliche Einkommensausfaelle, Familie, Arbeitsplatzverlust.
 - **OLG-Linie zur Abwehr Fahrverbot:** restriktiv; "unzumutbare Haerte" eng auszulegen; ggf. Kompensation Erhoehung Geldbusse (BGH-Linie 50-100 %).
 - **Strategie:** zeitliche Verschiebung Fahrverbot § 25 IIa StVG 4-Monatsfrist nutzen; ggf. Antrag auf Befreiung wegen besonderer Haerte.
- **Sonderfall 3: Beamte / Aerzte / Anwaelte als Betroffene:**
 - Berufsrechtliche Konsequenzen: Disziplinarrecht / Berufsaufsicht melden.
 - **Eintragung FAER** kann automatisch BZRG-/Berufsmeldung ausloesen.
- **Sonderfall 4: Mehrfachverstoss / Tatmehrheit § 19 OWiG:**
 - Mehrere OWi in einer Handlung -> Tateinheit, Strafmass einheitlich.
 - Mehrere getrennte Verstoesse -> Tatmehrheit, Strafe je Verstoss; ggf. Gesamtgeldbuesse.
- **Sonderfall 5: Auslaendischer Betroffener:**
 - Halterauskunft ueber EU-Mitgliedstaat moeglich; RB 2005/214/JI Vollstreckung Geldsanktionen.
 - Dolmetscher § 185 GVG erforderlich.
 - Verkuendung schriftlich + Uebersetzung beruecksichtigen.
- **Sonderfall 6: Mehrere Betroffene (Halter + Fahrer):**
 - Halterauskunftspflicht § 31a StVZO; Fahrtenbuchauflage bei Nichtermittelbarkeit.
 - Interessenkollisionen Vertretung beider durch denselben Anwalt § 138 StGB / § 43a Abs. 4 BRAO.
- **Sonderfall 7: Eilmassnahme vor Hauptverhandlung:**
 - **Aussetzung Vollziehung Fahrverbot:** Antrag bei AG vor Rechtskraft.
 - **Vorlaeufige Entziehung Fuehrerschein § 111a StPO** im Strafverfahren: Beschwerde § 304 StPO.
- **Wiedereinsetzung § 52 OWiG:** 1 Woche ab Wegfall des Hindernisses.
- **Praxis-Tipp:** Bei drohendem Fahrverbot Berufskraftfahrer regelmaessig persoenliches Erscheinen; persoenlicher Eindruck Betroffener oft entscheidend fuer Haerte-Pruefung.

## Qualitätsanker: Messdaten, Messakte und faires Verfahren

- **Verifizierter Leitanker:** BVerfG, Beschluss vom 12.11.2020 - 2 BvR 1616/18. Bei standardisierten Messverfahren darf die Verteidigung nicht mit bloßer Behördenroutine abgespeist werden; vorhandene, nicht aktenkundige Messinformationen können für ein faires Verfahren zugänglich sein, wenn sie konkret und rechtzeitig verlangt werden.
- **Praktische Übersetzung:** Niemals nur pauschal „Messung bestreiten“. Immer präzise anfordern: Falldatei/Rohmessdaten, Messreihe soweit vorhanden und relevant, Token/Passwort, Eichschein, Gebrauchsanweisung, Schulungsnachweise, Wartungs-/Reparaturhinweise, Standort-/Beschilderungsunterlagen, Statistik und Auswerteprotokoll.
- **Angriffslinie:** Standardisiertes Messverfahren ist eine Beweiserleichterung, kein Denkverbot. Der Skill muss aus Unterlagen konkrete Einwendungen machen: falsches Gerät, fehlende Eichung, fehlerhafte Bedienung, unklare Fahreridentität, unplausible Messreihe, fehlende Einsicht, Frist-/Gehörsproblem.
- **Output-Pflicht:** Immer ein kurzes Anforderungsschreiben oder einen gerichtsfesten Begründungsbaustein anbieten, wenn Akteneinsicht, Messunterlagen oder Fristwahrung Thema sind.

## 2. `spezial-messakte-formular-portal-und-einreichung`

**Fokus:** Messakte: Formular, Portal und Einreichungslogik im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Messakte: Formular, Portal und Einreichungslogik

## Spezialwissen: Messakte: Formular, Portal und Einreichungslogik
- **Spezialgegenstand:** Messakte: Formular, Portal und Einreichungslogik / messakte formular portal und einreichung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Messakte** prüfen.
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

## Qualitätsanker: Messdaten, Messakte und faires Verfahren

- **Verifizierter Leitanker:** BVerfG, Beschluss vom 12.11.2020 - 2 BvR 1616/18. Bei standardisierten Messverfahren darf die Verteidigung nicht mit bloßer Behördenroutine abgespeist werden; vorhandene, nicht aktenkundige Messinformationen können für ein faires Verfahren zugänglich sein, wenn sie konkret und rechtzeitig verlangt werden.
- **Praktische Übersetzung:** Niemals nur pauschal „Messung bestreiten“. Immer präzise anfordern: Falldatei/Rohmessdaten, Messreihe soweit vorhanden und relevant, Token/Passwort, Eichschein, Gebrauchsanweisung, Schulungsnachweise, Wartungs-/Reparaturhinweise, Standort-/Beschilderungsunterlagen, Statistik und Auswerteprotokoll.
- **Angriffslinie:** Standardisiertes Messverfahren ist eine Beweiserleichterung, kein Denkverbot. Der Skill muss aus Unterlagen konkrete Einwendungen machen: falsches Gerät, fehlende Eichung, fehlerhafte Bedienung, unklare Fahreridentität, unplausible Messreihe, fehlende Einsicht, Frist-/Gehörsproblem.
- **Output-Pflicht:** Immer ein kurzes Anforderungsschreiben oder einen gerichtsfesten Begründungsbaustein anbieten, wenn Akteneinsicht, Messunterlagen oder Fristwahrung Thema sind.

## 3. `spezial-messung-fahrverbot-punkte`

**Fokus:** Messung, Punkte, Fahrverbot und Verteidigungsziel im Verkehrs-OWi: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

# Messung, Punkte, Fahrverbot und Verteidigungsziel im Verkehrs-OWi

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `verkehrsowi-verteidiger`. Kontext des Plugins: Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht.

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
3. **Materielle Weichen:** Die Kernfragen zu **Messung, Punkte, Fahrverbot und Verteidigungsziel im Verkehrs-OWi** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
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

## Messung / Punkte / Fahrverbot Bausteine
- **Punkte FAER § 4 StVG (seit Reform 2014):**
 - 1 Punkt: leichtere Verstoesse (z. B. Tempoueberschreitung 21-30 km/h innerorts).
 - 2 Punkte: schwerere Verstoesse mit Fahrverbot (z. B. ueber 30 km/h innerorts mit Fahrverbot).
 - 3 Punkte: Straftaten und besonders schwere OWi (z. B. § 316 StGB Trunkenheit, Unfallflucht).
 - **4-5 Punkte:** Ermahnung; **6-7 Punkte:** Verwarnung mit Aufbauseminar-Hinweis; **8 Punkte:** Entziehung Fahrerlaubnis (zwingend, § 4 V StVG).
 - **Punkteabbau:** freiwilliges Fahreignungsseminar bei 1-5 Punkten = 1 Punkt Reduktion (nur einmal in 5 Jahren).
- **Fahrverbot § 25 StVG:**
 - 1-3 Monate; Antritt regelmaessig nach Wahl binnen 4-Monatsfrist § 25 IIa StVG bei Ersttaeter; wiederholt sofort.
 - Bekannte Konstellationen: Geschwindigkeitsverstoss innerorts ab 31 km/h, ausserorts ab 41 km/h; Rotlicht qualifiziert (1+ Sek); Abstand unter 50% halber Tacho ab 80 km/h.
- **Wegfall Fahrverbot wegen unzumutbarer Haerte** (OLG-Linie restriktiv):
 - Berufskraftfahrer (Existenzgefahr).
 - Pflege Angehoeriger.
 - Wesentlicher Verlust soziale Bindungen.
 - **Kompensation moeglich:** Erhoehung Geldbusse um 50-100 % (BGH-Linie zur tatschuldangemessenen Kompensation).
- **Messung Standard-Pruefung:**
 - **Eichschein** Geraet im Tatzeitraum?
 - **Bedienerschein** mit Schulungsnachweis?
 - **Toleranzwerte abgezogen?** (Geschwindigkeit: 3 km/h bis 100 km/h, 3 % darueber; Abstand: 10 %).
 - **Standardisiertes Messverfahren** (BGH zur Beweiskraft)?
 - **Rohdaten** verfuegbar? (BVerfG-Linie zur fair-trial-Garantie zur Akteneinsicht).
- **Messverfahren-Spezialitaeten:**
 - PoliScan FM1: Photopositionierung-Diskussion.
 - Leivtec XV3: dokumentierte Verfahrensschwaechen einzelner OLG-Bezirke.
 - ES 8.0/3.0: Smear-Effekt; Photolinie.
 - TraffiStar S330: stationaerer Blitzer, Rohdaten-Diskussion.
- **Praxis-Tipp:** Bei Punktestand-Abfrage KBA Flensburg (kostenfrei); Punkteloesch-Tabelle § 29 StVG: 2,5 Jahre fuer 1-Punkt-OWi; 5 Jahre fuer 2-Punkt; 10 Jahre fuer 3-Punkt-Verstoesse.

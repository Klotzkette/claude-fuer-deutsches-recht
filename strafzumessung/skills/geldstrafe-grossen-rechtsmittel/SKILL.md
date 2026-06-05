---
name: geldstrafe-grossen-rechtsmittel
description: "Geldstrafe Grossen Rechtsmittel: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geldstrafe Grossen Rechtsmittel

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Geldstrafe Grossen Rechtsmittel** im Plugin Strafzumessung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-geldstrafe-zahlen-schwellen-und-berechnung` | Geldstrafe: Zahlen, Schwellenwerte und Berechnung im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-grossen-risikoampel-und-gegenargumente` | Grossen: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-rechtsmittel-und-gesamtstrafenfolgen` | Rechtsmittel-, Bewährungs- und Gesamtstrafenfolgen nach der Zumessung: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |

## Arbeitsweg

Im Plugin Strafzumessung gilt für **Geldstrafe Grossen Rechtsmittel**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-geldstrafe-zahlen-schwellen-und-berechnung`

**Fokus:** Geldstrafe: Zahlen, Schwellenwerte und Berechnung im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Geldstrafe: Zahlen, Schwellenwerte und Berechnung

## Spezialwissen: Geldstrafe: Zahlen, Schwellenwerte und Berechnung
- **Spezialgegenstand:** Geldstrafe: Zahlen, Schwellenwerte und Berechnung / geldstrafe zahlen schwellen und berechnung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StPO, TOA, JGG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Geldstrafe** prüfen.
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

## Qualitätsanker: Strafrahmen, Schuldprinzip und Gesamtstrafe

- **Verifizierte Rechtsprechungsanker:** BGH, Beschluss vom 14.05.2024 - 6 StR 502/23 zur Strafrahmenlogik/Sperrwirkung und gerechten Schuldstrafe; BGH, Beschluss vom 23.01.2024 - 3 StR 455/23 zum Doppelverwertungsverbot und Begründungsanforderungen; BGH, Beschluss vom 24.04.2024 - 5 StR 123/24 sowie BGH, Beschluss vom 03.06.2025 - 2 StR 333/24 zur nachträglichen Gesamtstrafenbildung, Zäsurwirkung und Härteausgleich.
- **Prüfreihenfolge:** Nie sofort ein „gefühltes Strafmaß“ bilden. Erst Tatbestand und anwendbares Recht, dann Strafrahmen, minder/ besonders schwerer Fall, vertypte Milderung, § 49 StGB, Doppelverwertungsverbot, § 46 StGB, Nebenfolgen, Bewährung, Gesamtstrafe.
- **§ 55-StGB-Disziplin:** Bei Vorverurteilungen immer Tatzeiten, Entscheidungsdaten, Rechtskraft, Vollstreckungsstand, erledigte/nicht erledigte Strafen und Zäsurwirkung als Tabelle verlangen. Unklare Gesamtstrafenlagen nicht glattbügeln, sondern als Risiko mit Alternativen ausgeben.
- **Output-Pflicht:** Strafzumessungsmemo mit Strafrahmenbaum, Zumessungstatsachen pro/contra, Revisionsrisiken und nächstem taktischem Schritt; bei Aktenbezug zusätzlich BZRG-/Urteils-/Vollstreckungsdaten-Lückenliste.

## 2. `spezial-grossen-risikoampel-und-gegenargumente`

**Fokus:** Grossen: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Grossen: Risikoampel, Gegenargumente und Verteidigungslinien

## Spezialwissen: Grossen: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Grossen: Risikoampel, Gegenargumente und Verteidigungslinien / grossen risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StPO, TOA, JGG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Grossen** prüfen.
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

## Strafzumessung-Risikoampel / Gegenargumente Bausteine
- **Risikoampel Strafmass:**
 - **Rot:**
 - Mindeststrafe nach Strafrahmen droht; keine Bewaehrung moeglich.
 - Einschlaegige Vorstrafen (insb. einschlaegiges Vergehen ueber 6 Monate).
 - Tat in Bewaehrungszeit (Widerrufsrisiko § 56f StGB).
 - Schadenshoehe Regelbeispiel-Schwelle.
 - Mehrfachverurteilung -> Gesamtstrafe § 55 StGB.
 - **Gelb:**
 - Erstverurteilung mit moeglicher Bewaehrung § 56 StGB.
 - Schadenswiedergutmachung teilweise.
 - Therapie / TOA § 46a StGB im Gang.
 - Sozialprognose grundsaetzlich positiv aber unklare Akteurslage.
 - **Gruen:**
 - Erstverurteilung mit Bewaehrung.
 - TOA / Wiedergutmachung erfolgt.
 - Verstaendigung § 257c StPO mit Korridor abgesichert.
 - Einstellungs-Aussicht §§ 153, 153a StPO.
- **Gegenargumente zu typischen Strafzumessungs-Argumenten der StA:**
 - **"einschlaegige Vorstrafen":** Tilgungsreife pruefen § 51 BZRG (Verwertungsverbot); zeitlich abgegrenzt; nicht-einschlaegig?
 - **"hoher Schaden":** Realquote pruefen (z. B. bei Versicherungsbetrug Schaden = Versicherungsleistung, nicht behaupteter Wert).
 - **"professioneller Vorgehen":** Subsumtion Regelbeispiel pruefen; oft nur Indizwirkung.
 - **"Tatfolgen": Konkrete Schaedenhoehe ermitteln; immaterielle Folgen objektivieren.
 - **"keine Schadenswiedergutmachung":** Versuche dokumentieren; TOA-Anbieten; ggf. Schadensregulierung in Aussicht stellen.
- **Verteidigungslinien Strafmilderung:**
 - § 46 II StGB-Bilanz vollstaendig durchgehen.
 - § 49 StGB-Verschiebung (§§ 21, 23 II, 27 II 2, 13 II StGB).
 - § 46a StGB TOA / Schadenswiedergutmachung.
 - § 47 StGB Vermeidung kurzer Freiheitsstrafe.
 - § 56 StGB Bewaehrungspraxis.
 - § 60 StGB Absehen von Strafe (klein-Schaden, Reue, gesundheitliche Folgen).
 - Verfahrensdauer-Kompensation (BGH-Vollstreckungsloesung).
- **Massregeln pruefen:** § 44 StGB Fahrverbot, § 69 StGB Entziehung Fahrerlaubnis, § 70 StGB Berufsverbot, §§ 63, 64 StGB Unterbringung Psychiatrie / Entziehungsanstalt.

## Qualitätsanker: Strafrahmen, Schuldprinzip und Gesamtstrafe

- **Verifizierte Rechtsprechungsanker:** BGH, Beschluss vom 14.05.2024 - 6 StR 502/23 zur Strafrahmenlogik/Sperrwirkung und gerechten Schuldstrafe; BGH, Beschluss vom 23.01.2024 - 3 StR 455/23 zum Doppelverwertungsverbot und Begründungsanforderungen; BGH, Beschluss vom 24.04.2024 - 5 StR 123/24 sowie BGH, Beschluss vom 03.06.2025 - 2 StR 333/24 zur nachträglichen Gesamtstrafenbildung, Zäsurwirkung und Härteausgleich.
- **Prüfreihenfolge:** Nie sofort ein „gefühltes Strafmaß“ bilden. Erst Tatbestand und anwendbares Recht, dann Strafrahmen, minder/ besonders schwerer Fall, vertypte Milderung, § 49 StGB, Doppelverwertungsverbot, § 46 StGB, Nebenfolgen, Bewährung, Gesamtstrafe.
- **§ 55-StGB-Disziplin:** Bei Vorverurteilungen immer Tatzeiten, Entscheidungsdaten, Rechtskraft, Vollstreckungsstand, erledigte/nicht erledigte Strafen und Zäsurwirkung als Tabelle verlangen. Unklare Gesamtstrafenlagen nicht glattbügeln, sondern als Risiko mit Alternativen ausgeben.
- **Output-Pflicht:** Strafzumessungsmemo mit Strafrahmenbaum, Zumessungstatsachen pro/contra, Revisionsrisiken und nächstem taktischem Schritt; bei Aktenbezug zusätzlich BZRG-/Urteils-/Vollstreckungsdaten-Lückenliste.

## 3. `spezial-rechtsmittel-und-gesamtstrafenfolgen`

**Fokus:** Rechtsmittel-, Bewährungs- und Gesamtstrafenfolgen nach der Zumessung: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

# Rechtsmittel-, Bewährungs- und Gesamtstrafenfolgen nach der Zumessung

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `strafzumessung`. Kontext des Plugins: Strafzumessung nach deutschem Strafrecht vom Strafbefehl bis zur grossen Strafkammer. § 46 StGB Strafzumessungstatsachen Tagessatz Geldstrafe Freiheitsstrafe Bewaehrung § 56 § 49 Regelbeispiele besonders schwerer Fall Verstaendigung § 257c StPO TOA § 46a Gesamtstrafe § 55 JGG.

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
3. **Materielle Weichen:** Die Kernfragen zu **Rechtsmittel-, Bewährungs- und Gesamtstrafenfolgen nach der Zumessung** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
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

## Rechtsmittel / Bewaehrung / Gesamtstrafe - Bausteine
- **Rechtsmittelpruefung nach Verkuendung:**
 - Beschwer pruefen (Strafmass-Differenz zum Antrag StA/Verteidigung).
 - Erfolgsaussicht Sachruege (Strafzumessungsruege selten erfolgreich; Aufhebung idR bei Lueckenhaftigkeit, Wertungsfehler, falschem Strafrahmen, Doppelverwertung § 46 III StGB) - staendige Rspr.
 - Verfahrensruege fuer Verstaendigungsmaengel § 257c StPO (Belehrung § 257c V StPO!).
 - Berufung § 314 StPO 1 Woche, Revision § 341 StPO 1 Woche, § 345 StPO Begruendung 1 Monat.
- **Bewaehrungsentscheidung § 56 StGB:**
 - Bis 6 Mon. = Sollvorschrift; 6-12 Mon. = Kannvorschrift; 12-24 Mon. = "besondere Umstaende" § 56 II StGB.
 - Sozialprognose § 56 I 1 StGB; Verteidigungsverhalten in Hauptverhandlung relevant.
 - Bewaehrungsauflagen § 56b StGB (Wiedergutmachung, Geldbusse, gemeinnuetzige Arbeit), -weisungen § 56c StGB (Therapie, Bewaehrungshilfe, Kontaktverbote).
 - Bewaehrungsdauer 2-5 Jahre § 56a StGB.
- **Gesamtstrafe § 55 StGB (nachtraegliche):**
 - Voraussetzung: weitere Verurteilung vor Vollstreckung erster Tat erfolgt.
 - Bildung: Einsatzstrafe + Erhoehung; § 54 II StGB Hoechstmass.
 - Antrag auf nachtraegliche Gesamtstrafenbildung gegen Vollstreckungsbehoerde / Gericht § 460 StPO.
- **Bewaehrungswiderruf § 56f StGB:** bei neuer Straftat in Bewaehrungszeit; § 56g Erlass nach Bewaehrungsende.
- **Anrechnung U-Haft § 51 StGB:** zwingend; Ausnahme bei Doppelvollstreckung.
- **Hinweispflicht Verteidiger:** Rechtsmittelverzicht und -Ruecknahme schriftliche Mandantenfreigabe.

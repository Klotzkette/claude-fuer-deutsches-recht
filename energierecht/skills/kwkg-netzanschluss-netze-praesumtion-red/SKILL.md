---
name: kwkg-netzanschluss-netze-praesumtion-red
description: "Kwkg Netzanschluss Netze Praesumtion RED: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kwkg Netzanschluss Netze Praesumtion RED

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Kwkg Netzanschluss Netze Praesumtion RED** im Plugin Energierecht (EnWG, EEG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-kwkg-verhandlung-vergleich-und-eskalation` | Kwkg: Verhandlung, Vergleich und Eskalation im Plugin energierecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-netzanschluss-formular-portal-und-einreichung` | Netzanschluss: Formular, Portal und Einreichungslogik im Plugin energierecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-netze-risikoampel-und-gegenargumente` | Netze: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin energierecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-praesumtion-red-team-und-qualitaetskontrolle` | Praesumtion: Red-Team und Qualitätskontrolle im Plugin energierecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Energierecht (EnWG, EEG) gilt für **Kwkg Netzanschluss Netze Praesumtion RED**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-kwkg-verhandlung-vergleich-und-eskalation`

**Fokus:** Kwkg: Verhandlung, Vergleich und Eskalation im Plugin energierecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Kwkg: Verhandlung, Vergleich und Eskalation

## Spezialwissen: Kwkg: Verhandlung, Vergleich und Eskalation
- **Spezialgegenstand:** Kwkg: Verhandlung, Vergleich und Eskalation / kwkg verhandlung vergleich und eskalation. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EEG, KWKG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Kwkg** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen KWKG
- **Anwendungsbereich (§ 1 KWKG):** Förderung von Strom aus Kraft-Wärme-Kopplungs-Anlagen (KWK-Anlagen), Wärmenetzen und Wärme-/Kältespeichern. Ziel: 120 TWh KWK-Strom bis 2030; Beitrag zur Dekarbonisierung der Wärmeversorgung.
- **Förderfähige Anlagen (§§ 5-7 KWKG):** Hocheffiziente KWK-Anlagen nach RL 2004/8/EG mit Primärenergieeinsparung ≥ 10% (oder mind. 25 kWel bei Kleinanlagen). Förderzeitraum: 30.000 bis 60.000 Vollbenutzungsstunden je nach Anlagengröße und Brennstoff.
- **Anlagenklassen (§§ 8 ff. KWKG):** Kleinst-/Klein-KWK (< 50 kWel) - feste Zuschläge; mittlere KWK (50 kWel - 1 MWel) - geringere Zuschläge; große KWK ab 1 MWel - Ausschreibungen nach § 8a KWKG (Zuschlagshöchstwerte).
- **Förderhöhe:** Variable Zuschläge nach KWK-Leistungsanteil; aktualisierte Werte stets aus § 7 KWKG und KWK-Ausschreibungsverordnung. Zuschlag wird auf die KWK-Stromerzeugung berechnet und vom Netzbetreiber ausgezahlt.
- **Direktvermarktung (§ 4 KWKG):** Zuschläge werden zusätzlich zum Direktvermarktungserlös gezahlt; Marktprämienmodell ähnlich EEG, aber spezifisch für KWK-Strom.
- **Wärmenetzförderung (§§ 18 ff. KWKG):** Investitionszuschüsse für Neu- und Ausbau von Wärmenetzen (§ 19); förderfähig ist der KWK-Wärmeanteil. Wärmespeicher: § 22 KWKG.
- **Antragstellung und Zulassung:** Bei BAFA (Bundesamt für Wirtschaft und Ausfuhrkontrolle) - Anlagenzulassung vor Inbetriebnahme empfohlen (§ 10 KWKG i.V.m. KWKAusV); detaillierte Nachweise zu Wirkungsgrad, Primärenergieeinsparung, Brennstoffeinsatz.
- **Streitfälle:** Streitigkeiten zur Zuschlagspflicht und Höhe gehen über Beschlusskammer der BNetzA bzw. Zivilgerichte gegen den Netzbetreiber. Bei Förderverweigerung durch BAFA: VG-Verfahren möglich.

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

## 2. `spezial-netzanschluss-formular-portal-und-einreichung`

**Fokus:** Netzanschluss: Formular, Portal und Einreichungslogik im Plugin energierecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Netzanschluss: Formular, Portal und Einreichungslogik

## Spezialwissen: Netzanschluss: Formular, Portal und Einreichungslogik
- **Spezialgegenstand:** Netzanschluss: Formular, Portal und Einreichungslogik / netzanschluss formular portal und einreichung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EEG, KWKG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Netzanschluss** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen Netzanschluss
- **Anspruch auf Anschluss (§ 17 EnWG):** Netzbetreiber ist verpflichtet, Letztverbraucher und Erzeugungsanlagen zu wirtschaftlich zumutbaren Bedingungen anzuschließen. Verweigerung nur bei technischer oder wirtschaftlicher Unzumutbarkeit (Darlegungslast Netzbetreiber).
- **EE-Anlagen (§§ 8, 10 EEG):** Vorrang beim Netzanschluss; § 8 EEG verpflichtet Netzbetreiber zur unverzüglichen Verbindung und Erweiterung des Netzes (Optimierung, Verstärkung, Ausbau). Verzögerung führt zu Schadenersatz nach § 15 EEG.
- **Niederspannungsanschluss:** NAV (Niederspannungsanschlussverordnung) - Anschlusspflicht im allgemeinen Versorgungsverhältnis; konkrete Netzanschlusskosten richten sich nach § 11 NAV i.V.m. Preisblatt des Netzbetreibers.
- **Mittel-/Hochspannung:** Individualvertrag nach §§ 17 ff. EnWG; Anschluss ist verhandelbar, aber zu nichtdiskriminierenden Bedingungen (§ 20 EnWG: Zugangsbedingungen, Entgelte, Allgemeine Geschäftsbedingungen). Bei Streit: Beschlusskammerverfahren bei BNetzA möglich.
- **Wartezeiten / Engpassmanagement:** Bei Netzengpässen Anschlusswarteliste; § 14 EnWG Redispatch 2.0 für Anlagen ab 100 kW. Anlagen, die abgeregelt werden, erhalten Ausfallarbeit gem. § 13a EnWG.
- **Netzanschlusskostenbeteiligung:** Bei EEG-Anlagen trägt der Anschlussnehmer die Kosten des Anschlusses bis zum technisch und wirtschaftlich günstigsten Verknüpfungspunkt (§ 16 Abs. 1 EEG); Netzausbau danach trägt der Netzbetreiber.
- **Streitschlichtung:** BNetzA-Schlichtungsstelle (§§ 111a, 111b EnWG) für Verbraucher; Beschlusskammerverfahren (§ 29 EnWG) für Geschäftskunden bei Diskriminierung. Klage vor OLG am Sitz der BNetzA (§ 75 EnWG).
- **Praktiker-Tipp:** Verzögerung beim Anschluss schriftlich rügen und Frist setzen; Belege für Wirtschaftlichkeitsprüfung verlangen (Netzbetreiber muss dokumentieren). Bei EE-Großanlagen: Frühzeitig Netzverknüpfungspunkt verbindlich klären lassen, um Projektrisiken zu minimieren.

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

## 3. `spezial-netze-risikoampel-und-gegenargumente`

**Fokus:** Netze: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin energierecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Netze: Risikoampel, Gegenargumente und Verteidigungslinien

## Spezialwissen: Netze: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Netze: Risikoampel, Gegenargumente und Verteidigungslinien / netze risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EEG, KWKG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Netze** prüfen.
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

## 4. `spezial-praesumtion-red-team-und-qualitaetskontrolle`

**Fokus:** Praesumtion: Red-Team und Qualitätskontrolle im Plugin energierecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Praesumtion: Red-Team und Qualitätskontrolle

## Spezialwissen: Praesumtion: Red-Team und Qualitätskontrolle
- **Spezialgegenstand:** Praesumtion: Red-Team und Qualitätskontrolle / praesumtion red team und qualitaetskontrolle. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EEG, KWKG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Praesumtion** prüfen.
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

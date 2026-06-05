---
name: gesellschaftsgruender-wandeldarlehen
description: "Wandeldarlehen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Wandeldarlehen

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Wandeldarlehen** im Plugin Gesellschaftsgründung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschaftsgruender-wandeldarlehen-safe` | Prüft Wandeldarlehen, Discount, Cap, Wandlung, Rang, Prospekt-/Bankaufsichtsrisiken. |
| `spezial-gesellschaften-tatbestand-beweis-und-belege` | Gesellschaften: Tatbestandsmerkmale, Beweisfragen und Beleglage im Gesellschaftsgründung: fachlich vertiefter Fachmodul mit Normenradar (GmbHG/MoPeG/Registerrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `spezial-ggmbh-risikoampel-und-gegenargumente` | Ggmbh: Risikoampel, Gegenargumente und Verteidigungslinien im Gesellschaftsgründung: fachlich vertiefter Fachmodul mit Normenradar (GmbHG/MoPeG/Registerrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `spezial-gruendungsassistent-erstpruefung-und-mandatsziel` | Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel im Gesellschaftsgründung: fachlich vertiefter Fachmodul mit Normenradar (GmbHG/MoPeG/Registerrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `spezial-partg-dokumentenmatrix-und-lueckenliste` | PartG: Dokumentenmatrix, Lückenliste und Nachforderung im Gesellschaftsgründung: fachlich vertiefter Fachmodul mit Normenradar (GmbHG/MoPeG/Registerrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |

## Arbeitsweg

Im Plugin Gesellschaftsgründung gilt für **Wandeldarlehen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschaftsgruender-wandeldarlehen-safe`

**Fokus:** Prüft Wandeldarlehen, Discount, Cap, Wandlung, Rang, Prospekt-/Bankaufsichtsrisiken.

# Wandeldarlehen und SAFE-ähnliche Instrumente

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Wandeldarlehen und SAFE-ähnliche Instrumente` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Route zu Wandeldarlehen-Plugin.

## Rechts- und Quellenanker

Je nach Rechtsform live prüfen: GmbHG, HGB, BGB-Gesellschaftsrecht nach MoPeG, PartGG, GenG, AktG, GwG, GewO, AO/UStG/EStG sowie Register- und Notarvorgaben.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gründerfreundliche Kurzantwort
- To-do-Liste mit Zuständigen
- Dokumenten- und Lückenliste
- Risikoampel
- passende Anschluss-Skills


## Vertiefter Gründer-Workflow

Arbeite nicht abstrakt, sondern wie eine Gründungsakte mit Notar, Registergericht, Bank, Steuerberater und operativem Start. Führe den Nutzer durch diese Entscheidungspunkte:

1. **Rechtsform und Phase:** Vorgründung, Gründung, Registereintragung, erste Verträge, Änderung, Krise oder Exit. Prüfe, ob GmbH/UG, eGbR, OHG/KG, PartG, Verein, Genossenschaft oder ausländische Struktur betroffen ist.
2. **Dokumente:** Satzung/Gesellschaftsvertrag, Gesellschafterliste, Geschäftsführerbeschluss, Handelsregisteranmeldung, Notarentwurf, Bank-/KYC-Unterlagen, steuerliche Erfassung, Gewerbeanmeldung und wirtschaftlich Berechtigte trennen.
3. **Risikoachsen:** Haftung vor Eintragung, Vertretungsmacht, Kapitalaufbringung, Sacheinlage, verdeckte Sacheinlage, Scheinselbstständigkeit, Erlaubnispflichten, Steuer- und Umsatzsteuerstart, IP-/Lizenzketten, Datenschutz und Geldwäsche.
4. **Praxisentscheidung:** Immer eine Gründeroption, eine konservative Anwaltsoption und eine schnelle Minimaloption darstellen. Bei Kosten-/Zeitkonflikten offen sagen, was schneller ist und welches Risiko bleibt.
5. **Anschlussarbeit:** Am Ende konkrete Folge-Skills aus `gesellschaftsgruender` nennen, etwa Satzung, Register, KYC, Steuerstart, Finanzierung, ESOP/VSOP, regulatorisches Geschäftsmodell oder Red-Team-Gründungspaket.

## Ergebnisqualität

- Liefere eine einseitige Gründer-Kurzfassung und danach eine anwaltliche Prüftabelle.
- Trenne Muss, Sollte, Optional und Später.
- Markiere externe Abhängigkeiten: Notar, Registergericht, Bank, Finanzamt, IHK/HWK, BaFin oder Fachbehörde.
- Keine endgültige Register- oder Steuerbehauptung ohne aktuellen Norm-/Formularcheck; bei Registerfragen die konkrete Zwischenverfügung oder den Notarentwurf als Primärquelle behandeln.

## 2. `spezial-gesellschaften-tatbestand-beweis-und-belege`

**Fokus:** Gesellschaften: Tatbestandsmerkmale, Beweisfragen und Beleglage im Gesellschaftsgründung: fachlich vertiefter Fachmodul mit Normenradar (GmbHG/MoPeG/Registerrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Gesellschaften: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschaften: Tatbestandsmerkmale, Beweisfragen und Beleglage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Gesellschaften: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** Gesellschaften: Tatbestandsmerkmale, Beweisfragen und Beleglage / gesellschaften tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** UG, OHG, KG, PartG, MoPeG, DiRUG, GwG.
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
2. **Tatbestand Gesellschaftsform fixieren:** GbR § 705 BGB n.F. (Mindestens 2 Personen, gemeinsamer Zweck, Beiträge); OHG § 105 HGB (Handelsgewerbe + Vollhaftung); KG § 161 HGB (Komplementär + Kommanditist mit Haftsumme); GmbH § 1 GmbHG (Stammkapital 25.000 EUR, notariell). Konkludente GbR/OHG bei Praxisgemeinschaften möglich.
3. **Beweisfragen:** Wer trägt was vor? Bei GbR-Streit: Gesellschaftsvertrag (schriftlich oder konkludent), Beitragsleistung, gemeinsamer Zweck, Gewinnverteilung, Auftreten nach außen. Bei Personenhandelsgesellschaft zusätzlich Handelsregister-Eintragung (deklaratorisch außer KG-Kommanditist konstitutiv § 162 HGB).
4. **Belegmatrix erstellen:** Gesellschaftsvertrag, Anmeldung Register, Notarurkunde, Bankunterlagen Kapitalkonto, Geschäftsführerbestellung, wirtschaftlich Berechtigte Transparenzregister, IHK/HwK-Mitteilungen, Finanzamt-Anmeldung, Mietverträge Geschäftsräume, Versicherungsnachweise.
5. **Anschluss:** Bei Lücken Aufforderung zur Nachreichung; bei Streit über konkludente Gesellschaft Stufenklage § 254 ZPO (Auskunft + Rechnungslegung + Zahlung).

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

## 3. `spezial-ggmbh-risikoampel-und-gegenargumente`

**Fokus:** Ggmbh: Risikoampel, Gegenargumente und Verteidigungslinien im Gesellschaftsgründung: fachlich vertiefter Fachmodul mit Normenradar (GmbHG/MoPeG/Registerrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Ggmbh: Risikoampel, Gegenargumente und Verteidigungslinien

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Ggmbh: Risikoampel, Gegenargumente und Verteidigungslinien` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Ggmbh: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Ggmbh: Risikoampel, Gegenargumente und Verteidigungslinien / ggmbh risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** UG, OHG, KG, PartG, MoPeG, DiRUG, GwG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Ggmbh** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## gGmbH-spezifische Risikoampel

| Risiko-Punkt | Norm | Ampel | Gegenargument / Empfehlung |
| --- | --- | --- | --- |
| Gemeinnützigkeitsanerkennung versagt | §§ 51 ff. AO; insbesondere § 52 AO Katalog gemeinnütziger Zwecke | Rot | Satzung zwingend an Mustersatzung Anlage 1 zu § 60 AO anlehnen; vorab verbindliche Auskunft (§ 89 Abs. 2 AO) beim Finanzamt einholen |
| Mittelfehlverwendung | § 55 AO Selbstlosigkeit | Rot | strikte Trennung Zweckbetrieb (§ 65 AO) / steuerpflichtiger wirtschaftlicher Geschäftsbetrieb (§§ 14, 64 AO); Mittelweitergabe nur im Rahmen § 58 AO |
| Vermögensbindung | § 55 Abs. 1 Nr. 4 AO i.V.m. § 61 AO | Rot bei Satzungsfehler | Anfallsklausel zwingend zu Gunsten anderer gemeinnütziger Körperschaft |
| Unangemessene Geschäftsführer-Vergütung | § 55 Abs. 1 Nr. 3 AO | Rot | externer Marktvergleich (Caritas-Tarif, BAT-KF) dokumentieren; bei Klage BFH ständige Rechtsprechung zur Angemessenheitsprüfung beachten |
| Aberkennung Gemeinnützigkeit rückwirkend | § 175 Abs. 1 Nr. 2 AO | Rot | rückwirkend bis 10 Jahre möglich, gefährdet Kapitalerträge, Spenden, Befreiungen |
| Spendenbescheinigung unrichtig | § 10b EStG i.V.m. § 50 EStDV; Haftung § 10b Abs. 4 EStG | Rot | Aussteller haftet für Steuerausfall mit 30 % |
| Beihilfenrecht EU | Art. 107 AEUV | Gelb bei Wirtschaftsbetrieben | Förderkonflikt vermeiden; ggf. De-minimis-VO |
| Umsatzsteuer Befreiung | § 4 Nr. 14, 16, 18-22 UStG | Gelb | nicht jede Tätigkeit ist USt-befreit; ZB-Betriebe und VuV genau prüfen |
| Schenkungsteuer bei Übertragung | §§ 7, 13 ErbStG | Grün bei korrekter Satzung | Steuerbefreiung § 13 Abs. 1 Nr. 16b ErbStG bei gemeinnützigen Zwecken |

## Trade-off und typische Gegenargumente

- **gGmbH versus Stiftung:** gGmbH leichter steuerbar (Gesellschafterversammlung), aber jährlich strenger gem. § 51 AO geprüft; Stiftung dauerhafter, aber starrer.
- **gGmbH versus e.V.:** e.V. günstiger zu führen, aber bei wirtschaftlicher Aktivität droht § 22 BGB / Idealverein-Verlust. gGmbH erlaubt klar Mischbetrieb.
- **Risiko-Hebel "wirtschaftlicher Geschäftsbetrieb":** ab Bruttoeinnahmen 45.000 EUR (§ 64 Abs. 3 AO) Pflicht zur Aufteilung; oberhalb voller Körperschaftsteuer- und Gewerbesteuerpflicht.
- **Praktiker-Tipp:** Vor jeder Satzungsänderung Vorlage beim Finanzamt zur unverbindlichen Vorabprüfung; Schreiben des Finanzamts zur Gemeinnützigkeit (Freistellungsbescheid, Anlage Anlage zur Steuererklärung KSt 1 F) ist Lebensnerv.

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

## 4. `spezial-gruendungsassistent-erstpruefung-und-mandatsziel`

**Fokus:** Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel im Gesellschaftsgründung: fachlich vertiefter Fachmodul mit Normenradar (GmbHG/MoPeG/Registerrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Gruendungsassistent: Erstprüfung, Rollenklärung und Mandatsziel / gruendungsassistent erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** UG, OHG, KG, PartG, MoPeG, DiRUG, GwG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Gruendungsassistent** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Rechtsformvergleich für Erstprüfung

| Form | Mindestkapital | Gründungskosten | Haftung | Notar | Geeignet für |
| --- | --- | --- | --- | --- | --- |
| GbR (§§ 705 ff. BGB, MoPeG-novelliert) | kein | gering | unbeschränkt persönlich §§ 721 BGB | nicht zwingend; Gesellschaftsregister § 707 BGB optional (eGbR) | nicht-kaufmännische Personenzusammenschlüsse |
| OHG (§§ 105 ff. HGB) | kein | gering | unbeschränkt persönlich § 128 HGB | HR-Anmeldung notariell | Kaufleute, Kleinbetriebe |
| KG (§§ 161 ff. HGB) | kein, Haftsumme frei wählbar | gering | Komplementär unbeschränkt; Kommanditist auf Haftsumme § 171 HGB | notarielle HR-Anmeldung | Investoren-Beteiligung |
| GmbH & Co. KG | GmbH 25.000 EUR | mittel | Komplementär-GmbH | notariell | Mittelstand, Steueroptimierung |
| UG (haftungsbeschränkt) § 5a GmbHG | 1 EUR Stammkapital, Aufstockungspflicht § 5a Abs. 3 GmbHG (25 % Gewinn) | gering, Musterprotokoll § 2 Abs. 1a GmbHG | begrenzt | notariell, vereinfachte Online-Gründung möglich (DiRUG) | Bootstrap-Startup |
| GmbH | 25.000 EUR, hälftige Einzahlung § 7 GmbHG (12.500 EUR) | mittel | begrenzt § 13 Abs. 2 GmbHG | notariell, Online-Gründung § 2 Abs. 3 GmbHG (DiRUG seit 01.08.2022) | Mittelstand-Standard |
| AG | 50.000 EUR § 7 AktG | hoch | begrenzt | notariell | kapitalmarktreife Strukturen |
| PartG mbB | kein | mittel | nur Berufsausübungs-Haftpflicht (§ 8 Abs. 4 PartGG) | nicht zwingend, Partnerschaftsregister | Freiberufler, Sozietäten |
| gGmbH | 25.000 EUR | mittel | begrenzt | notariell + Finanzamt Gemeinnützigkeit § 52 AO | gemeinnützige Zwecke |

## Trade-off-Hinweis für Mandantengespräch

- **UG vs. GmbH:** UG spart Stammkapital, kostet aber 25 %-Gewinnthesaurierung und schlechteres Image bei Banken/Lieferanten.
- **GmbH vs. GmbH & Co. KG:** KG ermöglicht steuerliche Verlustverrechnung beim Kommanditisten, aber komplexere Struktur und höhere laufende Kosten (zwei Jahresabschlüsse).
- **PartG mbB vs. Sozietät:** mbB schützt vor Berufsfehlern der Partner, aber nur bei Pflichtversicherung (§ 8 Abs. 4 PartGG i.V.m. § 51a BRAO bei Anwälten).
- **DiRUG-Online-Gründung:** seit 01.08.2022 § 2 Abs. 3 GmbHG erweitert; vereinfacht GmbH-Gründung. Beachte: Sacheinlagen weiterhin Präsenznotar.

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

## 5. `spezial-partg-dokumentenmatrix-und-lueckenliste`

**Fokus:** PartG: Dokumentenmatrix, Lückenliste und Nachforderung im Gesellschaftsgründung: fachlich vertiefter Fachmodul mit Normenradar (GmbHG/MoPeG/Registerrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# PartG: Dokumentenmatrix, Lückenliste und Nachforderung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `PartG: Dokumentenmatrix, Lückenliste und Nachforderung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: PartG: Dokumentenmatrix, Lückenliste und Nachforderung
- **Spezialgegenstand:** PartG: Dokumentenmatrix, Lückenliste und Nachforderung / partg dokumentenmatrix und lueckenliste. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** PartG, UG, OHG, KG, MoPeG, DiRUG, GwG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Pflichtdokumente PartG / PartG mbB

| Dokument | Norm | Inhalt |
| --- | --- | --- |
| Partnerschaftsvertrag | § 3 PartGG | Name (mit Zusatz "und Partner" oder "Partnerschaft"), Sitz, Gegenstand, Partner |
| Anmeldung Partnerschaftsregister | § 4 PartGG i.V.m. § 12 HGB | beglaubigt durch Notar |
| Berufshaftpflichtversicherung (mbB) | § 8 Abs. 4 PartGG, berufsrechtliche Vorgaben | Mindestdeckung: Anwalt 2,5 Mio. EUR (§ 51a Abs. 2 BRAO i.V.m. § 8 Abs. 4 PartGG), bei mbB regelmäßig erhöht; je Berufsstand prüfen |
| Berufszulassung jeder Partner | Berufsrecht (BRAO, StBerG, WPO, BÄO) | nur freie Berufe i.S.d. § 1 Abs. 2 PartGG |
| Transparenzregister | § 19 GwG | wirtschaftlich Berechtigte |

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **PartG-Spezifika prüfen:** Nur freie Berufe nach § 1 Abs. 2 PartGG (insbesondere Anwälte, Steuerberater, Wirtschaftsprüfer, Ärzte, Architekten, Ingenieure, Notare); berufsfremde Personen ausgeschlossen.
3. **mbB-Voraussetzungen:** § 8 Abs. 4 PartGG Haftungsbeschränkung nur bei Berufshaftpflichtversicherung mit ausreichender Deckung; Versicherung muss laufend bestehen, bei Wegfall Wiederaufleben der unbeschränkten Haftung. Vorteil gegenüber GmbH: keine Bilanzpublizität, transparente Besteuerung; Nachteil: Haftungsbegrenzung greift nur für Berufsfehler, nicht für sonstige Verbindlichkeiten.
4. **MoPeG-Hinweis:** PartG nicht von Auflösung GbR-Reform betroffen, aber Anwendung HGB-Grundsätze über § 1 Abs. 4 PartGG i.V.m. §§ 105 ff. HGB n.F. (Personenhandelsgesellschaftsrecht).
5. **Anschluss:** Lückenliste mit Versicherungsnachweis, Berufszulassungen, Notartermin Partnerschaftsregister, Anmeldung Transparenzregister. Folge-Skill `gesellschaftsgruender-transparenzregister`.

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

---
name: iv-zahlungsklagen-insolvenzverwaltungs
description: "IV Zahlungsklagen Insolvenzverwaltungs: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Zahlungsklagen Insolvenzverwaltungs

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Zahlungsklagen Insolvenzverwaltungs** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-zahlungsklagen-15b` | Zahlungsklagen nach § 15b InsO gegen Geschäftsleiter vorbereiten wenn Zahlungen nach Insolvenzreife erfolgt sind. § 15b InsO §§ 17 19 InsO Insolvenzreife. Prüfraster: Insolvenzreifedatum Zahlungen nach Stichtag Organstellung Ausnahmen ordnungsgemaeßer Geschäftsgang D-und-O-Deckung Vergleichsanker. Output: Haftungsanalyse Klageentwurf Vergleichsrechnung. Abgrenzung: nicht für Anfechtungsansprüche (iv-anfechtung-129ff). |
| `spezial-insolvenzverwaltungs-erstpruefung-und-mandatsziel` | Insolvenzverwaltungs: Erstprüfung, Rollenklärung und Mandatsziel im Insolvenzverwaltung: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/SGB III), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Zahlungsklagen Insolvenzverwaltungs**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-zahlungsklagen-15b`

**Fokus:** Zahlungsklagen nach § 15b InsO gegen Geschäftsleiter vorbereiten wenn Zahlungen nach Insolvenzreife erfolgt sind. § 15b InsO §§ 17 19 InsO Insolvenzreife. Prüfraster: Insolvenzreifedatum Zahlungen nach Stichtag Organstellung Ausnahmen ordnungsgemaeßer Geschäftsgang D-und-O-Deckung Vergleichsanker. Output: Haftungsanalyse Klageentwurf Vergleichsrechnung. Abgrenzung: nicht für Anfechtungsansprüche (iv-anfechtung-129ff).

# Zahlungsklagen nach § 15b InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zahlungsklagen nach § 15b InsO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Bereitet Ansprüche gegen Geschäftsleiter wegen Zahlungen nach Insolvenzreife aus Sicht der Insolvenzmasse vor.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Zahlungsunfähigkeit oder Überschuldung vor Antrag plausibel ist
- Zahlungen nach Eintritt der Insolvenzreife rekonstruiert werden
- D&O-Deckung oder Vergleich geprüft wird

## Eingaben

- Liquiditätsstatus, BWA, OPOS, Bankjournale
- Organstellung, Geschäftsverteilung, Beschlüsse
- Zahlungslisten, Steuer- und SV-Zahlungen, Fortführungsmaßnahmen

## Workflow

1. **Insolvenzreife datieren** - § 17 und § 19 InsO getrennt, stichtagsbezogen und belegbasiert prüfen.
2. **Zahlungen filtern** - Zahlungen nach Stichtag mit Empfänger, Zweck, Konto und Beleg erfassen.
3. **Ausnahmen prüfen** - ordnungsgemäßer Geschäftsgang, Antragstellung, Steuerprivileg und Masseinteresse prüfen.
4. **Klage bauen** - Anspruch, Schaden, Verjährung, D&O und Beweisangebot strukturieren.

## Ausgabe

- § 15b-Zahlungsmatrix
- Anspruchs- und Verteidigungsmatrix
- Klageentwurf oder Vergleichsvermerk

## Qualitätsgates

- Insolvenzreife nicht geschätzt, sondern begründet
- Zahlungslisten bankseitig belegbar
- Ausnahmen transparent geprüft

## Rote Schwellen

- unvollständige Bankdaten
- unklare Organstellung
- Verjährungsdruck

## Interne Vorlagen

- assets/templates/zahlungsklage-15b.md
- assets/templates/liquiditaetsstatus-kurzcheck.md

## Amtliche Erstquellen

- § 15b InsO
- §§ 17, 19 InsO

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `spezial-insolvenzverwaltungs-erstpruefung-und-mandatsziel`

**Fokus:** Insolvenzverwaltungs: Erstprüfung, Rollenklärung und Mandatsziel im Insolvenzverwaltung: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/SGB III), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Insolvenzverwaltungs: Erstprüfung, Rollenklärung und Mandatsziel

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzverwaltungs: Erstprüfung, Rollenklärung und Mandatsziel` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Insolvenzverwaltungs: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Insolvenzverwaltungs: Erstprüfung, Rollenklärung und Mandatsziel / insolvenzverwaltungs erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO, StaRUG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Insolvenzverwaltungs** prüfen.
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

## Erstprüfung Insolvenzverwalter — Pflichtfragen
- **Rollenklärung:**
 - Regelverwalter § 80 InsO (volle Verwaltungs- und Verfügungsbefugnis) oder Sachwalter § 274 InsO (Eigenverwaltung — Schuldner bleibt verfügungsbefugt, Sachwalter überwacht)?
 - Vorl. Verwalter § 21, § 22 InsO: stark (Verwaltungs- und Verfügungsbefugnis) oder schwach (Zustimmungsvorbehalt § 21 Abs. 2 Nr. 2 Alt. 2 InsO)?
 - Restrukturierungsbeauftragter § 73 ff. StaRUG (StaRUG-Verfahren)?
- **Mandatsziel:**
 - Massesicherung in den ersten 14 Tagen (§ 22 InsO Sicherungsmaßnahmen).
 - Berichtstermin § 156 InsO mit Empfehlung Fortführung oder Stilllegung.
 - Planinsolvenz §§ 217 ff. InsO als Verwertungsstrategie.
 - Übertragende Sanierung (Asset Deal / Share Deal).
- **Erstmaßnahmen:**
 - Inbesitznahme der Geschäftsräume, IT-Systeme, Buchhaltung, Mailpostfach (§ 148 InsO).
 - Sofortige Kontensperrung bei Banken, Neueröffnung Insolvenzkonto.
 - Anmeldung bei Insolvenzgericht: Verfahrenseröffnungsantrag bestätigt, Insolvenzbekanntmachung veranlasst.
 - Information Mitarbeiter, Betriebsrat — Insolvenzgeld § 165 SGB III prüfen, Vorfinanzierung anstoßen.
 - Eilige Verträge: Mietvertrag § 109 InsO (3 Monate Sonderkündigungsrecht), Arbeitsverträge § 113 InsO (3 Monate Kündigungsfrist), Dauerlieferverträge § 103 InsO Erfüllungswahlrecht.
- **Vergütung:** § 63 InsO i.V.m. InsVV — Regelsatz nach Massewert mit Zu-/Abschlägen.

## Haftungsrelevante Erstmaßnahmen
- § 60 InsO Verwalterhaftung — fehlerhafte Erstmaßnahmen sind tragender Haftungsanknüpfungspunkt.
- Dokumentation jeder Erstentscheidung (Datum, Begründung, Beleg).

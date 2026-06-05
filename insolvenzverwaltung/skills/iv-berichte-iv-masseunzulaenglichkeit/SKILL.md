---
name: iv-berichte-iv-masseunzulaenglichkeit
description: "IV Berichte IV Masseunzulaenglichkeit: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Berichte IV Masseunzulaenglichkeit

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Berichte IV Masseunzulaenglichkeit** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-berichte-gericht-glaeubiger` | Zwischenberichte Sachstandsberichte und Beschlussvorlagen für Insolvenzgericht Gläubiger­ausschuss und Gläubiger­versammlung erstellen. §§ 58 66 79 InsO Berichtspflichten. Prüfraster: Stichtag Massestand Tabelle Verwertung Prozesse Personal Steuern Risiken. Output: strukturierter Bericht Entscheidungsvorlage Ampelbericht. Abgrenzung: nicht für Schlussbericht und Schlussrechnung (iv-verteilung-schlussrechnung). |
| `iv-masseunzulaenglichkeit-208` | Masseunzulaenglichkeit anzeigen und Zahlungsrangfolge steuern wenn Masseverbindlichkeiten nicht für alle ausreichen. § 208 InsO §§ 53 54 InsO Massekosten. Prüfraster: Ist- oder Prognoseunzulaenglichkeit Alt- und Neumasseverbindlichkeiten Zahlungsstopp Kommunikation. Output: Anzeige an Gericht Rangfolgeliste Massnahmenplan. Abgrenzung: nicht für allgemeine Masseberechnung oder Schlussverteilung. |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Berichte IV Masseunzulaenglichkeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-berichte-gericht-glaeubiger`

**Fokus:** Zwischenberichte Sachstandsberichte und Beschlussvorlagen für Insolvenzgericht Gläubiger­ausschuss und Gläubiger­versammlung erstellen. §§ 58 66 79 InsO Berichtspflichten. Prüfraster: Stichtag Massestand Tabelle Verwertung Prozesse Personal Steuern Risiken. Output: strukturierter Bericht Entscheidungsvorlage Ampelbericht. Abgrenzung: nicht für Schlussbericht und Schlussrechnung (iv-verteilung-schlussrechnung).

# Berichte an Gericht und Gläubigerorgane

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Berichte an Gericht und Gläubigerorgane` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Erzeugt klare, prüfbare Berichte für Insolvenzgericht, Gläubigerausschuss und Gläubigerversammlung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Zwischenbericht, Sachstandsbericht oder Ausschussbericht fällig ist
- wichtige Verwertungs- oder Fortführungsentscheidungen anstehen
- Gläubigerkommunikation konsistent werden muss

## Eingaben

- Verfahrensstatus, Masse, Tabelle, Verwertung
- Prozess- und Anfechtungsstand, Fortführung, Kosten
- gerichtliche Verfügung oder Ausschussagenda

## Workflow

1. **Berichtsstand** - Stichtag, Zeitraum und Adressat festlegen.
2. **Faktenblock** - Masse, Tabelle, Verwertung, Prozesse, Personal, Steuern und Risiken aktualisieren.
3. **Entscheidungen** - Beschlussbedarf, Optionen und Empfehlung formulieren.
4. **Belege** - Anlagen, Tabellen und Nachweise referenzieren.

## Ausgabe

- Zwischenbericht
- Ausschussbericht
- Beschlussvorlage mit Anlagenliste

## Qualitätsgates

- keine Bewertung ohne Zahlenstand
- Adressatengerechte Tiefe
- offene Punkte klar markiert

## Rote Schwellen

- Masseunzulänglichkeit verschwiegen
- Quote ohne Basis
- Interessenkonflikt bei Verwertung

## Interne Vorlagen

- assets/templates/zwischenbericht.md
- assets/templates/glaeubigerausschuss-bericht.md

## Amtliche Erstquellen

- InsO Berichtspflichten nach Verfahrenslage
- § 156 InsO als Berichtstermin-Schnittstelle

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

## 2. `iv-masseunzulaenglichkeit-208`

**Fokus:** Masseunzulaenglichkeit anzeigen und Zahlungsrangfolge steuern wenn Masseverbindlichkeiten nicht für alle ausreichen. § 208 InsO §§ 53 54 InsO Massekosten. Prüfraster: Ist- oder Prognoseunzulaenglichkeit Alt- und Neumasseverbindlichkeiten Zahlungsstopp Kommunikation. Output: Anzeige an Gericht Rangfolgeliste Massnahmenplan. Abgrenzung: nicht für allgemeine Masseberechnung oder Schlussverteilung.

# Anzeige der Masseunzulänglichkeit § 208 InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Anzeige der Masseunzulänglichkeit § 208 InsO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Führt durch Prüfung, Anzeige und Nachsteuerung einer Masseunzulänglichkeit.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Masseverbindlichkeiten nicht oder bald nicht fällig erfüllbar sind
- Kosten des Verfahrens gedeckt sind, aber sonstige Masseverbindlichkeiten kritisch sind
- Zahlungen priorisiert oder gestoppt werden müssen

## Eingaben

- Massebestand, Kosten, Masseverbindlichkeiten
- Fälligkeitsliste, Fortführungsplan, Prognose
- Gerichtskommunikation und Gläubigerliste

## Workflow

1. **Status rechnen** - Kosten des Verfahrens, fällige und künftige Masseverbindlichkeiten trennen.
2. **Anzeige prüfen** - Ist- oder Prognoseunzulänglichkeit bestimmen und Begründung vorbereiten.
3. **Rangfolge steuern** - Zahlungen stoppen, Alt-/Neumasseverbindlichkeiten und Kommunikation ordnen.
4. **Fortverwaltung** - Verwertung und Berichte nach Anzeige fortführen.

## Ausgabe

- § 208-Prüfvermerk
- Anzeigeentwurf an das Gericht
- Zahlungs- und Kommunikationsplan

## Qualitätsgates

- Kosten des Verfahrens gesondert geprüft
- Fälligkeiten belegt
- Rangfolge nach Anzeige dokumentiert

## Rote Schwellen

- Zahlung einzelner Massegläubiger kurz vor Anzeige
- Fortführung ohne Deckung
- fehlende öffentliche Bekanntmachung im Blick

## Interne Vorlagen

- assets/templates/masseunzulaenglichkeit-208.md
- assets/templates/massenachverfolgung.csv

## Amtliche Erstquellen

- § 208 InsO
- §§ 209 ff. InsO

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

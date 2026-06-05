---
name: iv-plan-iv-steuern
description: "IV Plan IV Steuern: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Plan IV Steuern

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Plan IV Steuern** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-plan-steuern-bilanz-folgen` | Steuerliche und bilanzielle Folgen des Insolvenzplans oder StaRUG prüfen damit Planwirkungen nicht an Nebenwirkungen scheitern. §§ 3a 3c EStG Sanierungsgewinn § 8c KStG Verlustvortrag. Prüfraster: Erlass Stundung Debt-Equity-Swap Bilanzierung Verlustvortraege USt LohnSt SV. Output: Steuerrisikomatrix Bilanzfolgenliste Beraterfragen. Abgrenzung: nicht für allgemeine Steuerthemen im Verfahren (iv-steuern-sozialversicherung). |
| `iv-steuern-sozialversicherung` | Steuerliche und sozialversicherungsrechtliche Verbindlichkeiten im Insolvenzverfahren klassifizieren und bearbeiten. §§ 38 55 InsO Rangklassen §§ 34 35 AO Haftung. Prüfraster: Insolvenzforderung Masseverbindlichkeit Haftungsrisiken Erklärungspflichten § 15b InsO Steuerprivileg. Output: Klassifizierungstabelle Erklärungsplan Haftungsnotiz. Abgrenzung: nicht für steuerliche Planfolgen (iv-plan-steuern-bilanz-folgen). |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Plan IV Steuern**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-plan-steuern-bilanz-folgen`

**Fokus:** Steuerliche und bilanzielle Folgen des Insolvenzplans oder StaRUG prüfen damit Planwirkungen nicht an Nebenwirkungen scheitern. §§ 3a 3c EStG Sanierungsgewinn § 8c KStG Verlustvortrag. Prüfraster: Erlass Stundung Debt-Equity-Swap Bilanzierung Verlustvortraege USt LohnSt SV. Output: Steuerrisikomatrix Bilanzfolgenliste Beraterfragen. Abgrenzung: nicht für allgemeine Steuerthemen im Verfahren (iv-steuern-sozialversicherung).

# IV-integrierte Steuern und Bilanzfolgen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IV-integrierte Steuern und Bilanzfolgen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Planwirkungen nicht an Nebenfolgen scheitern lassen. Der Skill ist vollständig in das Insolvenzverwaltungs-Plugin integriert, arbeitet innerhalb dieses ZIPs freistehend und setzt keine weiteren Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Erlass, Stundung, Debt-Equity-Swap, Sicherheitenverwertung und Veräußerungen steuerlich markieren.
2. Bilanzielle Behandlung, Rückstellungen, Sanierungsbeiträge, Verlustvorträge und Zahlungszeitpunkte erfassen.
3. Finanzamt, Sozialversicherung und Lohnsteuer als Stakeholder und Risiko trennen.
4. Steuerberater- und Wirtschaftsprüferfragen gezielt vorbereiten.

## Ausgabe

- Steuerrisikomatrix
- Bilanzfolgenliste
- Beraterfragen
- Planannahmen für Steuern

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.

## IV-Einordnung

Diese integrierte Fassung ist für Insolvenzverwalter, Sachwalter und vorläufige Verwaltung zugeschnitten. Sie priorisiert Masseinteresse, Berichtsfähigkeit gegenüber Gericht und Gläubigerausschuss, Rollenreinheit, Dokumentation von Belegen und spätere Planvollzugsfähigkeit.

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (IV-Insolvenzplan)

§ 217 InsO (Plan-Option) → § 218 InsO (Vorlage durch IV) → §§ 220-221 InsO (Plan-Inhalte) → § 222 InsO (Gruppenbildung) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Bestaetigung) → § 254 InsO (Wirkung) → §§ 49-51 InsO (Absonderungsrechte in Plan)

## Triage — IV-Plan

Bevor losgelegt wird, klaere:
1. **Plan sinnvoller als Liquidation?** Vergleichsrechnung: Plan-Quote vs. Liquidationsquote.
2. **Gruppenbildung konsistent?** § 222 InsO: gesicherte, nicht gesicherte, Kleinglaeubieger, Arbeitnehmer.
3. **Mehrheiten realistisch?** Simulation Kopf- + Summenmehrheit je Gruppe.
4. **Cramdown-Szenario?** § 245 InsO: ablehnende Gruppe ueberstimmbar wenn Best-Interest-Test bestanden.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## IV-Einordnung

Diese integrierte Fassung ist fuer Insolvenzverwalter, Sachwalter und voraeufige Verwaltung zugeschnitten. Sie priorisiert Masseinteresse, Berichtsfaehigkeit gegenueber Gericht und Glaeubigerausschuss sowie Planvollzugsfaehigkeit.

## 2. `iv-steuern-sozialversicherung`

**Fokus:** Steuerliche und sozialversicherungsrechtliche Verbindlichkeiten im Insolvenzverfahren klassifizieren und bearbeiten. §§ 38 55 InsO Rangklassen §§ 34 35 AO Haftung. Prüfraster: Insolvenzforderung Masseverbindlichkeit Haftungsrisiken Erklärungspflichten § 15b InsO Steuerprivileg. Output: Klassifizierungstabelle Erklärungsplan Haftungsnotiz. Abgrenzung: nicht für steuerliche Planfolgen (iv-plan-steuern-bilanz-folgen).

# Steuern, Sozialversicherung und Abgaben

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Steuern, Sozialversicherung und Abgaben` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Ordnet steuerliche und sozialversicherungsrechtliche Themen des Verfahrens mit insolvenzrechtlicher Einordnung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Finanzamt, Krankenkassen oder Zoll Forderungen anmelden
- laufende Steuererklärungen, Lohnsteuer oder Umsatzsteuer anstehen
- § 15b-Ausnahmen bei Steuerzahlungen zu prüfen sind

## Eingaben

- Steuerkonten, SV-Rückstände, Lohn- und USt-Daten
- Bescheide, Prüfungsanordnungen, Zahlungsjournale
- Fortführungs- und Masseplan

## Workflow

1. **Klassifizieren** - Insolvenzforderung, Masseverbindlichkeit, Neumasse und Haftung trennen.
2. **Erklärungen** - laufende Abgaben und Erklärungspflichten erfassen.
3. **Zahlungen** - Steuer- und SV-Zahlungen im Lichte von Masse und § 15b prüfen.
4. **Kommunikation** - Finanzamt, Krankenkassen, Zoll und Gericht koordiniert anschreiben.

## Ausgabe

- Abgabenmatrix
- Steuer-/SV-To-do-Liste
- Zahlungs- und Haftungsvermerk

## Qualitätsgates

- Zeitraum entscheidet die Einordnung
- Bescheide und Buchungen abgeglichen
- Steuerprivileg nicht überdehnt

## Rote Schwellen

- unerkannte Massesteuern
- § 266a StGB-Risiko vor Verfahren
- Lohnsteuer während Fortführung

## Interne Vorlagen

- assets/templates/steuern-sozialversicherung.md
- assets/templates/zahlungsklage-15b.md

## Amtliche Erstquellen

- § 15b Abs. 8 InsO
- AO und SGB als zu prüfende Schnittstelle

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

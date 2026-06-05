---
name: ifap-tabellenauszug-tabellenimport-verteilung
description: "Ifap Tabellenauszug Tabellenimport Verteilung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ifap Tabellenauszug Tabellenimport Verteilung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ifap Tabellenauszug Tabellenimport Verteilung** im Plugin Insolvenzforderungsanmeldung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ifap-tabellenauszug-178` | Tabellenauszug und Feststellungswirkung nach § 178 InsO: Anwendungsfall Forderung ist festgestellt und Gläubiger fragt nach Status oder Insolvenzverwalter muss Tabellenauszug als vollstreckbaren Titel erstellen. § 178 InsO Feststellungswirkung, § 201 InsO Nachhaftung. Prüfraster Feststellungsstatus, Schuldnerwiderspruch abgrenzen, vollstreckbarer Auszug bei Schuldner-ohne-Widerspruch. Output Tabellenauszug mit Feststellungsprotokoll und Vollstreckungshinweis. Abgrenzung zu Prüfentscheidung und zu Streitige-Forderung. |
| `ifap-tabellenimport-175` | Tabelleneintrag und Tabellenimport nach § 175 InsO: Anwendungsfall Forderungen sind geprüft und muessen in gerichtliche Tabelle überführt werden oder CSV-Import in Verwaltungssoftware vorbereitet werden. § 175 InsO Tabelle, § 176 InsO Prüfungstermin, Inso-Table-Standard. Prüfraster Gläubiger Anspruchsgrund Betrag Rang vbuH Widerspruch Prüfstatus vollständig. Output tabellenfähige Ausgabe mit Import-Format und Prüfprotokoll. Abgrenzung zu Prüfentscheidung und zu Tabellenauszug-178. |
| `ifap-verteilung-bestrittene-189` | Verteilung bei bestrittenen Forderungen nach § 189 InsO: Anwendungsfall Insolvenzverwalter bereitet Abschlags- oder Schlussverteilung vor und muss bestrittene Forderungen korrekt zurückbehalten oder ausklammern. § 189 InsO Berücksichtigung bestrittener Forderungen, § 196 InsO Schlussverteilung, § 188 InsO Abschlagsverteilung. Prüfraster Nachweiserbringung Gläubiger, Rückbehalt-Berechnung, Nichtberücksichtigung bei fehlendem Nachweis. Output Verteilungsprotokoll für bestrittene Forderungen mit Rückbehalt-Berechnung. Abgrenzung zu Tabellenauszug-178 und zu Streitige-Forderung-179-180. |

## Arbeitsweg

Im Plugin Insolvenzforderungsanmeldung gilt für **Ifap Tabellenauszug Tabellenimport Verteilung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ifap-tabellenauszug-178`

**Fokus:** Tabellenauszug und Feststellungswirkung nach § 178 InsO: Anwendungsfall Forderung ist festgestellt und Gläubiger fragt nach Status oder Insolvenzverwalter muss Tabellenauszug als vollstreckbaren Titel erstellen. § 178 InsO Feststellungswirkung, § 201 InsO Nachhaftung. Prüfraster Feststellungsstatus, Schuldnerwiderspruch abgrenzen, vollstreckbarer Auszug bei Schuldner-ohne-Widerspruch. Output Tabellenauszug mit Feststellungsprotokoll und Vollstreckungshinweis. Abgrenzung zu Prüfentscheidung und zu Streitige-Forderung.

# Tabellenauszug und Feststellungswirkung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Tabellenauszug und Feststellungswirkung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Macht den Feststellungsstatus verständlich und trennt Schuldnerwiderspruch sauber ab.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Forderung ist festgestellt
- Gläubiger fragt nach Status
- Tabellenauszug wird benötigt

## Workflow

1. Feststellungsstatus prüfen: unbestritten, Widerspruch beseitigt, Verwalterwiderspruch, Gläubigerwiderspruch, Schuldnerwiderspruch.
2. Betrag und Rang der Feststellung dokumentieren.
3. Wirkung der Tabelleneintragung intern markieren, ohne externe Rechtsbelehrung zu überziehen.
4. Kommunikation für festgestellte und bestrittene Forderungen trennen.
5. Bei Schuldnerwiderspruch gesondert auf § 184-Spur verweisen.

## Ausgabe

- Feststellungsvermerk
- Tabellenauszug-Anschreiben
- Statusmitteilung
- Widerspruchsübersicht

## Übergabe an die Zwangsvollstreckung

Nach Aufhebung des Insolvenzverfahrens und sofern keine Restschuldbefreiung erteilt wurde, ist der
Tabellenauszug ein Vollstreckungstitel nach § 201 Abs. 2 InsO i.V.m. § 794 Abs. 1 Nr. 4a ZPO.
Für die Vollstreckung aus dem Tabellenauszug lädt das freistehende Plugin `zwangsvollstreckung`
den Skill `zv-tabellenauszug-201-inso`. Er prüft Restschuldbefreiungsstand, dreißigjährige Verjährung
§ 197 Abs. 1 Nr. 5 BGB, Klauselbedürftigkeit und steuert die anschließende PfÜB- oder
Mobiliarvollstreckung.

## Qualitätsgates

- Schuldnerwiderspruch hindert nicht dieselbe Feststellungswirkung gegenüber Verwalter und Gläubigern.
- Tabellenauszug wird nur mit korrektem Status vorbereitet.
- Kein Vollstreckungshinweis ohne Prüfung der Verbraucher-/Restschuldbefreiungsspur.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `ifap-tabellenimport-175`

**Fokus:** Tabelleneintrag und Tabellenimport nach § 175 InsO: Anwendungsfall Forderungen sind geprüft und muessen in gerichtliche Tabelle überführt werden oder CSV-Import in Verwaltungssoftware vorbereitet werden. § 175 InsO Tabelle, § 176 InsO Prüfungstermin, Inso-Table-Standard. Prüfraster Gläubiger Anspruchsgrund Betrag Rang vbuH Widerspruch Prüfstatus vollständig. Output tabellenfähige Ausgabe mit Import-Format und Prüfprotokoll. Abgrenzung zu Prüfentscheidung und zu Tabellenauszug-178.

# Tabellenimport nach § 175 InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Tabellenimport nach § 175 InsO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Überführt geprüfte Forderungen in eine saubere Tabellenstruktur.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Tabelle soll angelegt werden
- CSV-Import wird gebraucht
- gerichtlicher Arbeitsstand ist zu liefern

## Workflow

1. Pflichtspalten aus Verfahrenspraxis definieren: laufende Nummer, Gläubiger, Vertreter, Grund, Betrag, Rang, Status.
2. § 174-Angaben in Tabellenlogik übertragen, ohne Begründungen zu verlieren.
3. vbuH, Unterhalt, Steuerstraftat und Schuldnerhinweis gesondert kennzeichnen.
4. Bestreiten von Verwalter, Schuldner oder Gläubiger getrennt abbilden.
5. Exportformat als CSV und menschenlesbare Prüfliste ausgeben.

## Ausgabe

- Tabellenimport.csv
- Tabellenarbeitsstand
- Fehlerliste
- Importnotiz

## Qualitätsgates

- Keine Tabellenzeile ohne Prüfnummer.
- Widerspruchsperson wird getrennt vom Forderungsstatus erfasst.
- Sonderzeichen und Dezimalformate werden vor Import kontrolliert.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `ifap-verteilung-bestrittene-189`

**Fokus:** Verteilung bei bestrittenen Forderungen nach § 189 InsO: Anwendungsfall Insolvenzverwalter bereitet Abschlags- oder Schlussverteilung vor und muss bestrittene Forderungen korrekt zurückbehalten oder ausklammern. § 189 InsO Berücksichtigung bestrittener Forderungen, § 196 InsO Schlussverteilung, § 188 InsO Abschlagsverteilung. Prüfraster Nachweiserbringung Gläubiger, Rückbehalt-Berechnung, Nichtberücksichtigung bei fehlendem Nachweis. Output Verteilungsprotokoll für bestrittene Forderungen mit Rückbehalt-Berechnung. Abgrenzung zu Tabellenauszug-178 und zu Streitige-Forderung-179-180.

# Verteilung bei bestrittenen Forderungen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Verteilung bei bestrittenen Forderungen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Sichert, dass bestrittene Forderungen bei Verteilungen richtig zurückbehalten oder nicht berücksichtigt werden.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Verteilung wird vorbereitet
- Forderung ist nicht festgestellt
- Feststellungsklage-Nachweis fehlt

## Workflow

1. Alle nicht festgestellten Forderungen mit Verteilungsrelevanz auflisten.
2. Prüfen, ob Titel oder Endurteil vorliegt oder Nachweis der Feststellungsklage/Aufnahme erforderlich ist.
3. Zweiwochenfrist ab öffentlicher Bekanntmachung als Wiedervorlage berechnen und offen ausweisen.
4. Rückbehalt bei rechtzeitigem Nachweis und Nichtberücksichtigung bei Fristversäumung als Szenario darstellen.
5. Verteilungsverzeichnis, Rückbehalt und Kommunikationsnotiz vorbereiten.

## Ausgabe

- § 189-Liste
- Rückbehaltsvermerk
- Fristenkontrolle
- Verteilungsentscheidungsvorschlag

## Qualitätsgates

- Keine Verteilung ohne Liste nicht festgestellter Forderungen.
- Nachweis und bloße Ankündigung werden getrennt.
- Rückbehalt wird betrags- und quotenscharf dokumentiert.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

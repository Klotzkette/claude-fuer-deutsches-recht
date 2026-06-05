---
name: ifap-pruefentscheidung-vbuh
description: "Ifap Pruefentscheidung Vbuh: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ifap Pruefentscheidung Vbuh

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ifap Pruefentscheidung Vbuh** im Plugin Insolvenzforderungsanmeldung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ifap-kommandocenter` | Kommandocenter Insolvenzforderungsanmeldungsprüfung: Steuerung des gesamten Prüfpfads von Eingang bis Tabelle. Anwendungsfall Insolvenzverwalter oder Kanzlei erhält neuen Forderungsstapel und muss schnell den richtigen Prüfschritt finden. §§ 174-189 InsO Forderungsanmeldung und Prüfung. Prüfraster Verfahrensstand und Rolle erkennen, naechsten sicheren Schritt bestimmen, Fristen und Risiken anzeigen. Output Deal-Ampel mit Weiterleitung zum passendes Fachmodul. Abgrenzung zu Intake-Kanalcheck für Eingangserfassung und zu Quality-Gate für Endkontrolle. |
| `ifap-pruefentscheidung` | Prüfentscheidung Forderung festzustellen oder zu bestreiten: Anwendungsfall nach abgeschlossener Prüfung trifft Insolvenzverwalter Entscheidung über Feststellung Teilfeststellung Bestreiten oder Rückstellung. § 176 InsO Prüfungstermin, § 178 InsO Feststellungswirkung Bestreiten Tabelle. Prüfraster alle Belege verarbeitet, Besteuerungsgrundlage, Rang, vbuH, plausible Bestreitungsgründe. Output Prüfentscheidungsprotokoll mit Begründung und tabellenreifer Status. Abgrenzung zu Quality-Gate für Vollständigkeitsprüfung und zu Prüfungstermin-176. |
| `ifap-vbuh-pruefung` | Vorsätzlich begangene unerlaubte Handlung und Steuerstraftat in Insolvenzanmeldung prüfen: Anwendungsfall Gläubiger meldet Forderung mit Kennzeichnung als vbuH vorsaetzliche unerlaubte Handlung Unterhaltspflichtverletzung oder Steuerstraftat an was Restschuldbefreiung blockiert. §§ 302 Nr. 1 InsO vbuH, § 850f Abs. 2 ZPO, §§ 174 InsO. Prüfraster Tatsachengrundlage vbuH prüfen, Streitigkeit vorbereiten, Restschuldbefreiungsrelevanz einordnen, Schuldnerwiderspruch antizipieren. Output vbuH-Prüfungsprotokoll mit Begründungsanforderungen. Abgrenzung zu Rang-Nachrang und zu Prüfentscheidung. |

## Arbeitsweg

Im Plugin Insolvenzforderungsanmeldung gilt für **Ifap Pruefentscheidung Vbuh**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ifap-kommandocenter`

**Fokus:** Kommandocenter Insolvenzforderungsanmeldungsprüfung: Steuerung des gesamten Prüfpfads von Eingang bis Tabelle. Anwendungsfall Insolvenzverwalter oder Kanzlei erhält neuen Forderungsstapel und muss schnell den richtigen Prüfschritt finden. §§ 174-189 InsO Forderungsanmeldung und Prüfung. Prüfraster Verfahrensstand und Rolle erkennen, naechsten sicheren Schritt bestimmen, Fristen und Risiken anzeigen. Output Deal-Ampel mit Weiterleitung zum passendes Fachmodul. Abgrenzung zu Intake-Kanalcheck für Eingangserfassung und zu Quality-Gate für Endkontrolle.

# Kommandocenter für die Forderungsprüfung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Kommandocenter für die Forderungsprüfung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Steuert den gesamten Prüfpfad von Eingangsstapel bis Tabellen- und Streitnachlauf.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- neuer Eingangsstapel
- unklare Forderungsanmeldung
- Prüfungstermin steht bevor
- Tabelle muss bereinigt werden

## Workflow

1. Verfahrensdaten aufnehmen: Gericht, Aktenzeichen, Eröffnungsdatum, Anmeldefrist, Prüfungstermin, schriftliches Verfahren.
2. Material sortieren: Eingangskanal, Gläubiger, Forderungsart, Betrag, Rang, Belege, Titel und Nachträge.
3. Arbeitsmodus wählen: Einzelprüfung, Batchprüfung, Nachforderung, Tabellenimport, Prüfungstermin oder Streitnachlauf.
4. Rote Schwellen markieren: vbuH, Titel, Nachrang, Absonderung, Masseforderung, Arbeitnehmerforderung, Steuer/SV, Dublette.
5. Konkrete nächste Ausgabe erzeugen: Prüfplan, Rückfragenliste, Tabellenzeilen oder Entscheidungsvermerk.

## Ausgabe

- Prüfpfad mit Prioritäten
- offene Rückfragen
- nächster Skill-Vorschlag
- Risikoampel je Forderung

## Qualitätsgates

- Keine Feststellung ohne Belegkette.
- Jede streitige Forderung erhält einen Nachlaufvermerk.
- Fristen und Prüfungstermin werden sichtbar gemacht.

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

## 2. `ifap-pruefentscheidung`

**Fokus:** Prüfentscheidung Forderung festzustellen oder zu bestreiten: Anwendungsfall nach abgeschlossener Prüfung trifft Insolvenzverwalter Entscheidung über Feststellung Teilfeststellung Bestreiten oder Rückstellung. § 176 InsO Prüfungstermin, § 178 InsO Feststellungswirkung Bestreiten Tabelle. Prüfraster alle Belege verarbeitet, Besteuerungsgrundlage, Rang, vbuH, plausible Bestreitungsgründe. Output Prüfentscheidungsprotokoll mit Begründung und tabellenreifer Status. Abgrenzung zu Quality-Gate für Vollständigkeitsprüfung und zu Prüfungstermin-176.

# Prüfentscheidung treffen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Prüfentscheidung treffen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Verdichtet die Prüfung in eine tabellenfähige und intern nachvollziehbare Entscheidung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- alle Belege sind geprüft
- Tabelle braucht Status
- Bestreiten muss begründet werden

## Workflow

1. Prüfergebnis je Teilposition erfassen: Grund, Betrag, Rang, Zinsen, Kosten, Sonderrecht.
2. Entscheidungstyp wählen: festgestellt, teilweise festgestellt, bestritten, teilweise bestritten, zurückgestellt, Nachforderung.
3. Begründung kontrolliert kurz halten: tabellentauglich, aber für interne Akte nachvollziehbar.
4. Folgen notieren: Tabelleneintrag, Nachricht an Gläubiger, Terminvorbereitung, Streitnachlauf.
5. Bei rechtlicher Unsicherheit menschliche Freigabe verlangen.

## Ausgabe

- Prüfvermerk
- Feststellungsvermerk
- Bestreitensvermerk
- Tabellenstatus

## Qualitätsgates

- Betrag und Rang werden getrennt entschieden.
- Teilbestreiten ist betragsgenau.
- Rechtsmeinung und Tatsachenmangel werden unterschieden.

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

## 3. `ifap-vbuh-pruefung`

**Fokus:** Vorsätzlich begangene unerlaubte Handlung und Steuerstraftat in Insolvenzanmeldung prüfen: Anwendungsfall Gläubiger meldet Forderung mit Kennzeichnung als vbuH vorsaetzliche unerlaubte Handlung Unterhaltspflichtverletzung oder Steuerstraftat an was Restschuldbefreiung blockiert. §§ 302 Nr. 1 InsO vbuH, § 850f Abs. 2 ZPO, §§ 174 InsO. Prüfraster Tatsachengrundlage vbuH prüfen, Streitigkeit vorbereiten, Restschuldbefreiungsrelevanz einordnen, Schuldnerwiderspruch antizipieren. Output vbuH-Prüfungsprotokoll mit Begründungsanforderungen. Abgrenzung zu Rang-Nachrang und zu Prüfentscheidung.

# vbuH, Unterhalt und Steuerstraftat prüfen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `vbuH, Unterhalt und Steuerstraftat prüfen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Prüft besondere Rechtsgründe mit Blick auf Restschuldbefreiung und Schuldnerwiderspruch.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- vbuH ist angekreuzt
- Schuldner widerspricht
- Restschuldbefreiungsfolge steht im Raum

## Workflow

1. Erfassen, welcher besondere Rechtsgrund behauptet wird: vorsätzlich unerlaubte Handlung, Unterhalt, Steuerstraftat.
2. Tatsachenvortrag prüfen: konkrete Handlung, Vorsatz, Schaden, Kausalität, Rechtsgrund, Urteil oder Ermittlungsstand.
3. Schuldnerhinweis und Widerspruchsmöglichkeit als separate Verfahrensspur markieren.
4. vbuH-Betrag von sonstigen Teilforderungen trennen.
5. Bei fehlenden Tatsachen Nachforderung oder Bestreiten des Rechtsgrunds vorbereiten.

## Ausgabe

- vbuH-Prüfvermerk
- Hinweisliste Schuldner
- Bestreitensvorschlag besonderer Rechtsgrund
- Nachforderung

## Qualitätsgates

- Ein Kreuz genügt nicht.
- Titel und Tatsachen werden getrennt bewertet.
- Restschuldbefreiungsfolgen werden nur als Verfahrenshinweis behandelt.

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

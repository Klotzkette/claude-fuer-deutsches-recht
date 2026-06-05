---
name: ifap-intake-kanalcheck-masseverbindlichkeit
description: "Ifap Intake Kanalcheck Masseverbindlichkeit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ifap Intake Kanalcheck Masseverbindlichkeit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ifap Intake Kanalcheck Masseverbindlichkeit** im Plugin Insolvenzforderungsanmeldung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ifap-intake-kanalcheck` | Eingehende Forderungsanmeldungen kanalübergreifend erfassen: Anwendungsfall Insolvenzverwalter-Büro erhält Anmeldungen per Post E-Mail Portal Tabellenexport oder Nachtrag und muss einheitliches Eingangsbuch führen. § 174 InsO Forderungsanmeldung, § 177 InsO Nachtragsanmeldung. Prüfraster Kanal-Identifikation, Metadaten-Erfassung, Eingangs-Zeitstempel, Dubletten-Vorabcheck, Prioritaet bei Fristnaehe. Output strukturiertes Eingangsbuch mit Kanal, Datum, Gläubiger und Status. Abgrenzung zu Aktenanlage-Batchregister für Massenerfassung und zu Formalprüfung. |
| `ifap-masseverbindlichkeit-abgrenzen` | Masseverbindlichkeiten von Insolvenzforderungen abgrenzen: Anwendungsfall Insolvenzverwalter erkennt Forderung die nach Verfahrenseroeffnung entstanden sein koennte und muss klaeren ob es Masseverbindlichkeit oder einfache Insolvenzforderung ist. §§ 53-55 InsO Masseverbindlichkeiten, §§ 38-39 InsO Insolvenzforderungen. Prüfraster Entstehungszeitpunkt relativ zur Eroeffnung, Verwalterhandeln, Zustimmungsvorbehalt, Neumasse vs. Altmasse. Output Abgrenzungsprotokoll mit rechtlicher Einordnung und Handlungsempfehlung. Abgrenzung zu Formalprüfung-174 und zu Rang-Nachrang. |
| `ifap-nachforderung-maengelschreiben` | Mängel- und Nachforderungsschreiben bei unvollständigen Insolvenzanmeldungen: Anwendungsfall Forderungsanmeldung nach § 174 InsO hat Mängel und Insolvenzverwalter muss Gläubiger präzise und freundlich zur Ergänzung auffordern. § 174 InsO Pflichtangaben, § 176 InsO Prüfungstermin. Prüfraster fehlende Belege identifizieren, unklaren Anspruchsgrund präzisieren, Zinsrechnung nachfordern, Frist für Reaktion setzen. Output vollständiges Mängelschreiben mit konkreten Nachforderungen und Reaktionsfrist. Abgrenzung zu Formalprüfung-174 und zu Quality-Gate. |

## Arbeitsweg

Im Plugin Insolvenzforderungsanmeldung gilt für **Ifap Intake Kanalcheck Masseverbindlichkeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ifap-intake-kanalcheck`

**Fokus:** Eingehende Forderungsanmeldungen kanalübergreifend erfassen: Anwendungsfall Insolvenzverwalter-Büro erhält Anmeldungen per Post E-Mail Portal Tabellenexport oder Nachtrag und muss einheitliches Eingangsbuch führen. § 174 InsO Forderungsanmeldung, § 177 InsO Nachtragsanmeldung. Prüfraster Kanal-Identifikation, Metadaten-Erfassung, Eingangs-Zeitstempel, Dubletten-Vorabcheck, Prioritaet bei Fristnaehe. Output strukturiertes Eingangsbuch mit Kanal, Datum, Gläubiger und Status. Abgrenzung zu Aktenanlage-Batchregister für Massenerfassung und zu Formalprüfung.

# Intake und Kanalcheck

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Intake und Kanalcheck` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Erfasst eingehende Forderungsanmeldungen kanalneutral und bildet ein belastbares Eingangsbuch.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Posteingang liegt vor
- Portalexport oder CSV liegt vor
- Gläubiger sendet Nachtrag
- mehrere Kanäle enthalten dieselbe Forderung

## Workflow

1. Eingangskanal, Eingangsdatum, Dateiname, Absender, Vertreter und Gläubiger-ID erfassen.
2. Anmeldung von Begleitschreiben, Anlagen, Rechnungspaketen, Titeln und Zahlungsnachweisen trennen.
3. Fristlage prüfen: rechtzeitig, verspätet, geändert oder offensichtlich nur Ergänzung.
4. Dublettenindizien markieren: gleicher Gläubiger, gleiche Rechnung, gleicher Betrag, gleicher Zeitraum, gleicher Titel.
5. Eingangsbuch und Prüfnummer vergeben, ohne materiell zu entscheiden.

## Ausgabe

- Intake-Register
- Dublettenhinweise
- fehlende Mindestdaten
- Zuordnung zu bestehender Prüfnummer

## Qualitätsgates

- Nachträge werden an die ursprüngliche Anmeldung geklebt.
- E-Mail-Text und Anlagen werden getrennt ausgewertet.
- Unlesbare Dateien werden nicht stillschweigend ignoriert.

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

## 2. `ifap-masseverbindlichkeit-abgrenzen`

**Fokus:** Masseverbindlichkeiten von Insolvenzforderungen abgrenzen: Anwendungsfall Insolvenzverwalter erkennt Forderung die nach Verfahrenseroeffnung entstanden sein koennte und muss klaeren ob es Masseverbindlichkeit oder einfache Insolvenzforderung ist. §§ 53-55 InsO Masseverbindlichkeiten, §§ 38-39 InsO Insolvenzforderungen. Prüfraster Entstehungszeitpunkt relativ zur Eroeffnung, Verwalterhandeln, Zustimmungsvorbehalt, Neumasse vs. Altmasse. Output Abgrenzungsprotokoll mit rechtlicher Einordnung und Handlungsempfehlung. Abgrenzung zu Formalprüfung-174 und zu Rang-Nachrang.

# Masseverbindlichkeit abgrenzen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Masseverbindlichkeit abgrenzen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Erkennt Forderungen, die nicht oder nur teilweise zur Insolvenztabelle gehören.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Leistung nach Eröffnung
- Verwalterbestellung oder Zustimmungsvorbehalt relevant
- Gläubiger meldet Masseforderung zur Tabelle an

## Workflow

1. Leistungszeitraum und Entstehungsgrund vor, nach oder während vorläufiger Verwaltung einordnen.
2. Prüfen, ob die Forderung überhaupt Insolvenzforderung ist oder als Masseverbindlichkeit außerhalb der Tabelle zu behandeln ist.
3. Bei gemischten Zeiträumen Teilbeträge bilden.
4. Verwalterhandlung, Betriebsfortführung, Dauerschuldverhältnis und Steuer-/SV-Bezug markieren.
5. Ausgabe zwischen Tabellenbestreiten, Weiterleitung an Massebearbeitung und Rückfrage unterscheiden.

## Ausgabe

- Abgrenzungsvermerk
- Teilbetragsaufteilung
- Rückfrage an Massebearbeitung
- Tabellenentscheidung

## Qualitätsgates

- Masseverbindlichkeit wird nicht zur Quote festgestellt.
- Gemischte Zeiträume werden nicht pauschal behandelt.
- Unsicherheit wird als Eskalationspunkt markiert.

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

## 3. `ifap-nachforderung-maengelschreiben`

**Fokus:** Mängel- und Nachforderungsschreiben bei unvollständigen Insolvenzanmeldungen: Anwendungsfall Forderungsanmeldung nach § 174 InsO hat Mängel und Insolvenzverwalter muss Gläubiger präzise und freundlich zur Ergänzung auffordern. § 174 InsO Pflichtangaben, § 176 InsO Prüfungstermin. Prüfraster fehlende Belege identifizieren, unklaren Anspruchsgrund präzisieren, Zinsrechnung nachfordern, Frist für Reaktion setzen. Output vollständiges Mängelschreiben mit konkreten Nachforderungen und Reaktionsfrist. Abgrenzung zu Formalprüfung-174 und zu Quality-Gate.

# Nachforderung und Mängelschreiben

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Nachforderung und Mängelschreiben` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Formuliert gezielte Nachforderungen, damit die Prüfung ohne unnötige Eskalation weiterkommt.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Belege fehlen
- Grund ist unklar
- Zinsrechnung fehlt
- Rang oder vbuH ist unzureichend begründet

## Workflow

1. Mangeltyp bestimmen: Formalangabe, Beleg, Betrag, Zins, Rang, Vertretung, Titel, vbuH, Dublette.
2. Nur die wirklich fehlenden Punkte anfordern, keine pauschalen Standardlisten.
3. Frist und Übermittlungsweg aus Verfahrenspraxis oder Vorgabe übernehmen.
4. Hinweis aufnehmen, dass ohne Ergänzung eine Prüfung nur nach Aktenlage erfolgt.
5. Ausgabe sachlich, knapp und nicht unnötig streitverschärfend formulieren.

## Ausgabe

- Mängelschreiben
- Belegliste
- Fristvermerk
- Wiedervorlage

## Qualitätsgates

- Keine Drohkulisse ohne Grund.
- Nachforderung muss zur konkreten Anmeldung passen.
- Frist und Empfänger werden vor Versand geprüft.

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

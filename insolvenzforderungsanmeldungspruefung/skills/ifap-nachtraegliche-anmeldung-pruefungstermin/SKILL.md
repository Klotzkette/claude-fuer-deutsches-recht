---
name: ifap-nachtraegliche-anmeldung-pruefungstermin
description: "Ifap Nachtraegliche Anmeldung Pruefungstermin: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ifap Nachtraegliche Anmeldung Pruefungstermin

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ifap Nachtraegliche Anmeldung Pruefungstermin** im Plugin Insolvenzforderungsanmeldung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ifap-nachtraegliche-anmeldung-177` | Verspätete und nachträgliche Forderungsanmeldungen nach § 177 InsO: Anwendungsfall Gläubiger meldet Forderung nach Ablauf der Anmeldefrist an oder ändert bereits angemeldete Forderung. § 177 InsO Nachtragsanmeldung, § 176 InsO Prüfungstermin, § 5 InsO Sondertermin. Prüfraster Fristablauf feststellen, Kostenpflicht bei Verspätung, Einordnung in Sondertermin oder schriftliches Verfahren. Output Verfahrensprotokoll mit Kostenbescheid und Terminzuordnung. Abgrenzung zu Formalprüfung-174 für rechtzeitige Anmeldungen und zu Prüfungstermin-176. |
| `ifap-pruefungstermin-176` | Prüfungstermin nach § 176 InsO vorbereiten: Anwendungsfall Prüfungstermin beim Insolvenzgericht naht und Insolvenzverwalter muss Einzelforderungen, Widersprüche und Erörterungspunkte aufbereiten. § 176 InsO Prüfungstermin, § 178 InsO Tabelle Feststellung. Prüfraster streitige Forderungen identifizieren, Terminmappe aufbauen, Widersprüche des Schuldners dokumentieren, schriftliches Prüfungsverfahren als Alternative. Output Terminmappe mit Einzelforderungs-Status und Verhandlungspunkten. Abgrenzung zu Prüfentscheidung und zu Streitige-Forderung-179-180. |
| `ifap-quality-gate` | Qualitätsgate vor Tabelleneintrag Prüfungstermin und Verteilung: Anwendungsfall alle Prüfschritte wurden durchgeführt und jetzt muss vor Versand oder Eintrag nochmals Vollständigkeit Plausibilitaet und Risiken geprüft werden. § 175 InsO Tabelle, § 176 InsO Prüfungstermin, § 189 InsO Verteilung. Prüfraster alle Pflichtfelder befüllt, Berechnungen plausibel, rote Risiken identifiziert, Quellen belegt. Output Qualitaetsprotokoll mit Ampelstatus und Freigabeentscheidung. Abgrenzung zu Kommandocenter als Einstieg und zu Prüfentscheidung. |

## Arbeitsweg

Im Plugin Insolvenzforderungsanmeldung gilt für **Ifap Nachtraegliche Anmeldung Pruefungstermin**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ifap-nachtraegliche-anmeldung-177`

**Fokus:** Verspätete und nachträgliche Forderungsanmeldungen nach § 177 InsO: Anwendungsfall Gläubiger meldet Forderung nach Ablauf der Anmeldefrist an oder ändert bereits angemeldete Forderung. § 177 InsO Nachtragsanmeldung, § 176 InsO Prüfungstermin, § 5 InsO Sondertermin. Prüfraster Fristablauf feststellen, Kostenpflicht bei Verspätung, Einordnung in Sondertermin oder schriftliches Verfahren. Output Verfahrensprotokoll mit Kostenbescheid und Terminzuordnung. Abgrenzung zu Formalprüfung-174 für rechtzeitige Anmeldungen und zu Prüfungstermin-176.

# Nachträgliche Anmeldung nach § 177 InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Nachträgliche Anmeldung nach § 177 InsO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Ordnet späte und geänderte Anmeldungen in Prüfungstermin, Sondertermin oder schriftliches Verfahren ein.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anmeldung kommt nach Fristablauf
- Anmeldung wird geändert
- Prüfungstermin ist vorbei

## Workflow

1. Zeitpunkt der Anmeldung gegenüber Anmeldefrist und Prüfungstermin feststellen.
2. Prüfen, ob Prüfung im bestehenden Termin möglich ist oder besonderer Termin/schriftliches Verfahren nötig wird.
3. Kostenfolge und Säumigenhinweis als organisatorischen Punkt markieren.
4. Änderung von neuer Forderung unterscheiden.
5. Nachträgliche Prüfung in Tabellenstand und Wiedervorlagen einbauen.

## Ausgabe

- Nachtragsvermerk
- Termin-/Schriftverfahrensvorschlag
- Kostenhinweis
- aktualisierter Tabellenstatus

## Qualitätsgates

- Nachtrag wird nicht als neue Dublette behandelt, wenn er dieselbe Forderung ergänzt.
- Fristlage wird mit konkretem Datum ausgegeben.
- Alte und neue Beträge bleiben nachvollziehbar.

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

## 2. `ifap-pruefungstermin-176`

**Fokus:** Prüfungstermin nach § 176 InsO vorbereiten: Anwendungsfall Prüfungstermin beim Insolvenzgericht naht und Insolvenzverwalter muss Einzelforderungen, Widersprüche und Erörterungspunkte aufbereiten. § 176 InsO Prüfungstermin, § 178 InsO Tabelle Feststellung. Prüfraster streitige Forderungen identifizieren, Terminmappe aufbauen, Widersprüche des Schuldners dokumentieren, schriftliches Prüfungsverfahren als Alternative. Output Terminmappe mit Einzelforderungs-Status und Verhandlungspunkten. Abgrenzung zu Prüfentscheidung und zu Streitige-Forderung-179-180.

# Prüfungstermin vorbereiten

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Prüfungstermin vorbereiten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Baut eine Terminmappe, die streitige Forderungen schnell erörterbar macht.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Prüfungstermin naht
- schriftliches Verfahren läuft
- streitige Forderungen müssen einzeln erörtert werden

## Workflow

1. Forderungen nach Status clustern: unstreitig, Nachforderung offen, Teilbestreiten, Vollbestreiten, Schuldnerwiderspruch.
2. Für streitige Forderungen Erörterungspunkte und Beleglücken notieren.
3. Teilbeträge und Rangfragen für schnelle Terminführung sichtbar machen.
4. Nachträge, verspätete Anmeldungen und Kostenfolgen kennzeichnen.
5. Terminmappe mit Agenda, Risikoliste, Tabellenstand und Entscheidungsbedarf erstellen.

## Ausgabe

- Prüfungsterminmappe
- Erörterungsliste
- Widerspruchsliste
- Nachforderungsliste

## Qualitätsgates

- Streitige Forderungen werden einzeln auffindbar.
- Betrag und Rang stehen im Terminblatt.
- Späte Änderungen werden nicht in alten Status verschmiert.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 114/23 vom 19.12.2024** — Bei Abtretung muss ein eigener Prüfungstermin durchgeführt werden; ohne diesen ist eine Feststellungsklage des Zedenten unzulässig. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Für die Prüfungsentscheidung über kapitalmarktrechtliche Aktionärsforderungen: Nachrang einwenden.

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. **Sonderfälle?** Abgetretene Forderungen — eigener Prüfungstermin Pflicht (BGH IX ZR 114/23 vom 19.12.2024). Aktionärs-Schadensersatz — Nachrang (BGH IX ZR 127/24 vom 13.11.2025).

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `ifap-quality-gate`

**Fokus:** Qualitätsgate vor Tabelleneintrag Prüfungstermin und Verteilung: Anwendungsfall alle Prüfschritte wurden durchgeführt und jetzt muss vor Versand oder Eintrag nochmals Vollständigkeit Plausibilitaet und Risiken geprüft werden. § 175 InsO Tabelle, § 176 InsO Prüfungstermin, § 189 InsO Verteilung. Prüfraster alle Pflichtfelder befüllt, Berechnungen plausibel, rote Risiken identifiziert, Quellen belegt. Output Qualitaetsprotokoll mit Ampelstatus und Freigabeentscheidung. Abgrenzung zu Kommandocenter als Einstieg und zu Prüfentscheidung.

# Qualitätsgate und Plausibilitätskontrolle

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Qualitätsgate und Plausibilitätskontrolle` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Stoppt unvollständige, unplausible oder zu riskante Ausgaben vor Import, Versand und Verteilung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- vor Import
- vor Prüfungstermin
- vor Versand
- vor Verteilung
- bei hohem Risiko

## Workflow

1. Vollständigkeit prüfen: Anmeldung, Belege, Betrag, Rang, Status, Entscheidung, Bearbeiter, Datum.
2. Plausibilität prüfen: Summen, Zinsen, Dubletten, Titel, OPOS, Nachträge, Nachrang, vbuH, Masseabgrenzung.
3. Rechtsquellencheck: Normen nur aus aktueller amtlicher Quelle oder geprüfter Kanzleiquelle verwenden.
4. Ausgabecheck: verständlich, tabellentauglich, keine überschießende Rechtsberatung, keine geheimen internen Notizen im Außenbrief.
5. Freigabe verlangen, wenn rote Schwellen berührt sind.

## Ausgabe

- QA-Protokoll
- Korrekturliste
- Freigabevermerk
- Rest-Risiko-Liste

## Qualitätsgates

- Rote Schwellen stoppen den Automatismus.
- Jede Zahl muss aus Quelle oder Rechnung herleitbar sein.
- Außenkommunikation und interne Bewertung bleiben getrennt.

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

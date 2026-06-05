---
name: ifap-dubletten-serienforderungen
description: "Ifap Dubletten Serienforderungen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ifap Dubletten Serienforderungen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ifap Dubletten Serienforderungen** im Plugin Insolvenzforderungsanmeldung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ifap-dubletten-serienforderungen` | Dubletten und Serienforderungen in Insolvenzanmeldungen erkennen: Anwendungsfall mehrere Gläubiger melden gleichartige oder identische Forderungen an; Inkassounternehmen und Originalgläubiger reichen parallel ein. § 174 InsO Forderungsanmeldung, § 178 InsO Tabelle Bestreiten. Prüfraster Doppelerfassung gleicher Rechnung, Serienrechnungen mit laufenden Nummern, Konzernforderungen und Vertreterwechsel, mehrfach eingereichte Titel. Output Dublettenprotokoll mit Unterscheidung echte Dublette vs. Serienforderung. Abgrenzung zu Aktenanlage-Batchregister und zu Formalprüfung. |
| `ifap-formalpruefung-174` | Formalprüfung Forderungsanmeldung nach § 174 InsO: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle prüft ob eingegangene Anmeldung Mindestangaben hat und tabellenfähig ist. § 174 InsO Pflichtinhalt, § 175 InsO Tabelle, § 176 InsO Prüfungstermin. Prüfraster Gläubiger mit Anschrift, Forderungsgrund, Betrag, Nachrang, Urkundenvorlage, elektronische Einreichung EGVP. Output Formalprüfungsprotokoll mit gruener oder roter Ampel und Maengelschreiben-Vorlage. Abgrenzung zu Grund-Betrag-Zinsen für inhaltliche Prüfung und zu Intake-Kanalcheck. |
| `ifap-grund-betrag-zinsen` | Anspruchsgrund Betrag und Zinsen der Insolvenzforderung prüfen: Anwendungsfall Insolvenzverwalter prüft ob angemeldeter Betrag rechnerisch korrekt und durch Anspruchsgrundlage gedeckt ist. § 174 InsO Forderungsanmeldung, §§ 38-39 InsO Insolvenzforderungen, BGB Verzugszinsen § 288. Prüfraster Hauptforderung aufschlüsseln, Teilzahlungen und Gutschriften abziehen, Zinsberechnung prüfen, Kostenpositionen prüfen. Output Berechnungsprotokoll mit Sollbetrag, Abweichungsampel und Korrekturbedarf. Abgrenzung zu Formalprüfung-174 und zu Beleg-Urkundencheck. |

## Arbeitsweg

Im Plugin Insolvenzforderungsanmeldung gilt für **Ifap Dubletten Serienforderungen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ifap-dubletten-serienforderungen`

**Fokus:** Dubletten und Serienforderungen in Insolvenzanmeldungen erkennen: Anwendungsfall mehrere Gläubiger melden gleichartige oder identische Forderungen an; Inkassounternehmen und Originalgläubiger reichen parallel ein. § 174 InsO Forderungsanmeldung, § 178 InsO Tabelle Bestreiten. Prüfraster Doppelerfassung gleicher Rechnung, Serienrechnungen mit laufenden Nummern, Konzernforderungen und Vertreterwechsel, mehrfach eingereichte Titel. Output Dublettenprotokoll mit Unterscheidung echte Dublette vs. Serienforderung. Abgrenzung zu Aktenanlage-Batchregister und zu Formalprüfung.

# Dubletten und Serienforderungen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Dubletten und Serienforderungen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Findet Mehrfachanmeldungen und trennt echte Dubletten von ähnlichen Serienforderungen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- gleiche Rechnung mehrfach
- Inkasso und Gläubiger melden parallel
- Konzernmeldungen überschneiden sich

## Workflow

1. Vergleichsschlüssel bilden: Gläubiger, Schuldnerkonto, Rechnungsnummer, Betrag, Zeitraum, Titel, Vertragsnummer.
2. Exakte Dubletten, wahrscheinliche Dubletten und bloß ähnliche Serienforderungen unterscheiden.
3. Vertreterwechsel und Inkasso-Zessionen prüfen: Forderungsinhaber, Vollmacht, Abtretung, Prozessstandschaft.
4. Bei Teilabtretungen und Konsortialforderungen Quoten und Teilbeträge trennen.
5. Entscheidung vorschlagen: zusammenführen, Nachweis verlangen, teilweise bestreiten, Doppelanmeldung bestreiten.

## Ausgabe

- Dublettenreport
- Zusammenführungsplan
- Zessions-/Vertretercheck
- Bestreitensvermerk

## Qualitätsgates

- Ähnliche Beträge sind nicht automatisch Dubletten.
- Inkassovertretung ist nicht Forderungsinhaberschaft.
- Zusammenführung bleibt im Audit-Trail nachvollziehbar.

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

## 2. `ifap-formalpruefung-174`

**Fokus:** Formalprüfung Forderungsanmeldung nach § 174 InsO: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle prüft ob eingegangene Anmeldung Mindestangaben hat und tabellenfähig ist. § 174 InsO Pflichtinhalt, § 175 InsO Tabelle, § 176 InsO Prüfungstermin. Prüfraster Gläubiger mit Anschrift, Forderungsgrund, Betrag, Nachrang, Urkundenvorlage, elektronische Einreichung EGVP. Output Formalprüfungsprotokoll mit gruener oder roter Ampel und Maengelschreiben-Vorlage. Abgrenzung zu Grund-Betrag-Zinsen für inhaltliche Prüfung und zu Intake-Kanalcheck.

# Formalprüfung nach § 174 InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Formalprüfung nach § 174 InsO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Prüft, ob eine Forderungsanmeldung formal tabellenfähig ist oder gezielte Ergänzung braucht.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anmeldung soll in die Tabelle
- Grund oder Betrag fehlen
- vbuH oder Nachrang ist angekreuzt

## Workflow

1. Prüfen, ob eine Anmeldung beim Verwalter vorliegt und welcher Gläubiger sie trägt.
2. Grund und Betrag isoliert erfassen, nicht aus Anlagen erraten, wenn die Anmeldung selbst leer bleibt.
3. Urkundenstatus prüfen: beigefügt, elektronisch, nachzureichen, unlesbar, nicht passend.
4. Nachranghinweis und Rangstelle prüfen, wenn nachrangige Forderung angemeldet ist.
5. vbuH, Unterhalt oder Steuerstraftat nur mit konkreten Tatsachen erfassen.
6. Mangelkategorie vergeben: heilbar, substanziell unklar, offensichtlich falscher Weg, Nachforderung erforderlich.

## Ausgabe

- § 174-Checkliste
- Mängelliste
- Nachforderungsvorschlag
- Status für Tabellenimport

## Qualitätsgates

- Grund und Betrag sind Pflichtachsen.
- Urkundenmangel wird nicht mit materiellem Bestreiten verwechselt.
- Elektronische Rechnung kann Urkunde sein, muss aber lesbar zuordenbar bleiben.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 114/23 vom 19.12.2024** — Anforderungen an die Individualisierung der Forderung iSd § 174 Abs. 2 InsO; bei Abtretung müssen Zedent und Zessionar jeweils separat anmelden und einen eigenen Prüfungstermin durchlaufen. Sachverhaltsdarstellung erforderlich, schlüssige Rechtsbegründung nicht.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Aktionärs-Schadensersatzforderungen sind in der Insolvenz der AG keine einfachen Insolvenzforderungen iSd § 38 InsO; Nachrang. Bedeutung für Formalprüfung: solche Anmeldungen formal bestreiten und auf Rangfrage hinweisen.
 Quelle: <https://www.lto.de/recht/kanzleien-unternehmen/k/bgh-ixzr12724-wirecard-insolvenzmasse-forderungen-aktionaere-urteil>

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. **Vorsatzklausel § 174 Abs. 2 InsO?** Bei deliktischer Forderung mit Vorsatz ausdrücklich Tatbestand benennen (Folge: Ausschluss von der Restschuldbefreiung nach § 302 Nr. 1 InsO). Sonderfall Wirecard-Konstellation (BGH IX ZR 127/24): kapitalmarktrechtliche Schadensersatzforderungen geschädigter Aktionäre sind keine einfachen Insolvenzforderungen iSd § 38 InsO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `ifap-grund-betrag-zinsen`

**Fokus:** Anspruchsgrund Betrag und Zinsen der Insolvenzforderung prüfen: Anwendungsfall Insolvenzverwalter prüft ob angemeldeter Betrag rechnerisch korrekt und durch Anspruchsgrundlage gedeckt ist. § 174 InsO Forderungsanmeldung, §§ 38-39 InsO Insolvenzforderungen, BGB Verzugszinsen § 288. Prüfraster Hauptforderung aufschlüsseln, Teilzahlungen und Gutschriften abziehen, Zinsberechnung prüfen, Kostenpositionen prüfen. Output Berechnungsprotokoll mit Sollbetrag, Abweichungsampel und Korrekturbedarf. Abgrenzung zu Formalprüfung-174 und zu Beleg-Urkundencheck.

# Grund, Betrag und Zinsen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grund, Betrag und Zinsen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Zerlegt die angemeldete Forderung in prüfbare Teilpositionen und macht Rechenfehler sichtbar.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Betrag passt nicht zu Belegen
- Zinsen sind angemeldet
- Teilzahlungen oder Gutschriften stehen im Raum

## Workflow

1. Anspruchsgrund konkretisieren: Vertrag, Lieferung, Dienstleistung, Darlehen, Steuer, Lohn, Schaden, Kosten, Titel.
2. Hauptforderung aus Anmeldung und Belegen in Teilpositionen zerlegen.
3. Teilzahlungen, Gutschriften, Aufrechnungen, Skonto, Storno und Sicherheiten abziehen oder als ungeklärt markieren.
4. Zinsen prüfen: Beginn, Zinssatz, Zeitraum bis Eröffnung, Rechtsgrund, Verzugsnachweis, titulierte Zinsen.
5. Kosten prüfen: Mahnkosten, Rechtsverfolgungskosten, Gerichtskosten, Inkasso, tituliert oder nicht tituliert.
6. Feststellbarer und zu bestreitender Betrag getrennt ausgeben.

## Ausgabe

- Betragsrechnung
- Zinsrechnung
- Teilbestreitensvorschlag
- Rechenprotokoll

## Qualitätsgates

- Zinsen nach Verfahrenseröffnung werden nicht blind als Insolvenzforderung übernommen.
- Teilzahlungen werden quellenbezogen dokumentiert.
- Rundungs- und Währungsfragen werden offengelegt.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 114/23 vom 19.12.2024** — Individualisierung der Forderung iSd § 174 Abs. 2 InsO: Sachverhaltsdarstellung erforderlich; schlüssige Rechtsbegründung nicht. Bei Abtretung jeweils gesonderte Anmeldung von Zedent und Zessionar. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. **Zinsen ab Eröffnung?** § 39 Abs. 1 Nr. 1 InsO Nachrangzinsen. Hauptforderung mit Zinsen bis Eröffnung als § 38 InsO-Forderung, ab Eröffnung als § 39 InsO-Nachrang anmelden bzw. trennen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

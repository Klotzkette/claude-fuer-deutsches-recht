---
name: ifap-rang-nachrang-schuldnerwiderspruch
description: "Ifap Rang Nachrang Schuldnerwiderspruch: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ifap Rang Nachrang Schuldnerwiderspruch

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ifap Rang Nachrang Schuldnerwiderspruch** im Plugin Insolvenzforderungsanmeldung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ifap-rang-nachrang-absonderung` | Rang Nachrang Absonderung und Aussonderung bei Insolvenzforderungen prüfen: Anwendungsfall Gläubiger behauptet Sonderrechte wie Absonderungsrecht aus Sicherungsuebereignung oder Nachrang. §§ 38-39 InsO Insolvenzforderungen und Nachrang, §§ 49-51 InsO Absonderungsrecht, §§ 47-48 InsO Aussonderungsrecht. Prüfraster einfache Insolvenzforderung vs. Nachrang vs. Absonderung, Glaubhaftmachung Sicherheitsrecht, Ausfallforderung nach Verwertung. Output Rang-Klassifizierungsprotokoll mit Begründung und Tabellenposition. Abgrenzung zu Formalprüfung und zu Prüfentscheidung. |
| `ifap-schuldnerwiderspruch-184` | Schuldnerwiderspruch nach § 184 InsO prüfen und Fristen einhalten: Anwendungsfall Schuldner widerspricht Forderung und bei titulierten Forderungen laeuft Monatsfrist für Aufnahme des Rechtsstreits. § 184 InsO Schuldnerwiderspruch, § 179 InsO Feststellungsklage, § 183 InsO Wirkung bei Schuldnerwiderspruch. Prüfraster titulierte vs. nichttitulierte Forderung, Monatsfrist ab Prüfungstermin, Aufnahme laufender Verfahren, Kommunikationsbedarf. Output Widerspruchsprotokoll mit Fristkalender und Handlungsempfehlung. Abgrenzung zu Streitige-Forderung-179-180 und zu Prüfungstermin-176. |
| `ifap-streitige-forderung-179-180` | Streitige Forderungen nach §§ 179 und 180 InsO nachverfolgen: Anwendungsfall Forderung wurde beim Prüfungstermin bestritten und Gläubiger muss Feststellungsklage erheben oder laufenden Rechtsstreit aufnehmen. § 179 InsO Feststellungsklage, § 180 InsO Tabellenklage, § 184 InsO Schuldnerwiderspruch. Prüfraster Bestreitungsprotokoll, Klagefrist, Zuständiges Gericht, Titelumkehr bei Titel-Inhaber. Output Nachlaufprotokoll für bestrittene Forderungen mit Fristen und Klageempfehlung. Abgrenzung zu Schuldnerwiderspruch-184 und zu Verteilung-189. |

## Arbeitsweg

Im Plugin Insolvenzforderungsanmeldung gilt für **Ifap Rang Nachrang Schuldnerwiderspruch**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ifap-rang-nachrang-absonderung`

**Fokus:** Rang Nachrang Absonderung und Aussonderung bei Insolvenzforderungen prüfen: Anwendungsfall Gläubiger behauptet Sonderrechte wie Absonderungsrecht aus Sicherungsuebereignung oder Nachrang. §§ 38-39 InsO Insolvenzforderungen und Nachrang, §§ 49-51 InsO Absonderungsrecht, §§ 47-48 InsO Aussonderungsrecht. Prüfraster einfache Insolvenzforderung vs. Nachrang vs. Absonderung, Glaubhaftmachung Sicherheitsrecht, Ausfallforderung nach Verwertung. Output Rang-Klassifizierungsprotokoll mit Begründung und Tabellenposition. Abgrenzung zu Formalprüfung und zu Prüfentscheidung.

# Rang, Nachrang und Sicherungsrechte

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rang, Nachrang und Sicherungsrechte` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Prüft die insolvenzrechtliche Einordnung der Forderung und alle behaupteten Sonderrechte.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Nachrang ist angemeldet
- Sicherheit wird behauptet
- Ausfallforderung unklar
- Eigentumsvorbehalt steht im Raum

## Workflow

1. Regelrang nach § 38 InsO, Nachrang nach § 39 InsO und sonstige Rangangaben trennen.
2. Prüfen, ob Nachrang überhaupt zur Anmeldung aufgefordert wurde.
3. Absonderungsrechte erfassen: Sicherungsübereignung, Pfand, Grundpfandrecht, Forderungsabtretung, Eigentumsvorbehalt.
4. Ausfallforderung und Verwertungslage abfragen, wenn Sicherheit vorhanden ist.
5. Aussonderung von Forderungsanmeldung trennen, wenn Eigentum oder Herausgabe statt Quote gemeint ist.
6. Tabellenrang und Sonderrechtsvermerk getrennt formulieren.

## Ausgabe

- Rangmatrix
- Sicherheitenvermerk
- Ausfallstatus
- Rangkorrekturvorschlag

## Qualitätsgates

- Sicherungsrechte werden nicht allein aus Selbstauskunft festgestellt.
- Nachrang wird ausdrücklich bezeichnet.
- Aussonderung führt nicht automatisch zu einer Tabellenforderung.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Kapitalmarktrechtliche Schadensersatzforderungen geschädigter Aktionäre sind in der Insolvenz der AG keine einfachen Insolvenzforderungen iSd § 38 InsO; sie sind nachrangig. Bedeutung für Rangprüfung: bei Anmeldung solcher Forderungen separat als Nachrangforderung klassifizieren bzw. dem Anmeldenden den Nachrang entgegenhalten.
 Quelle: <https://www.lto.de/recht/kanzleien-unternehmen/k/bgh-ixzr12724-wirecard-insolvenzmasse-forderungen-aktionaere-urteil>
- **BGH IX ZR 239/22 vom 18.04.2024** — Anfechtung gesellschafterähnlicher Stellung nach § 135 InsO; Anforderungen erhöht. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+239/22>

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. **Gesellschafterdarlehen § 39 Abs. 1 Nr. 5 / § 135 InsO?** Nach BGH IX ZR 239/22 vom 18.04.2024 strenge Anforderungen an Anfechtung gesellschafterähnlicher Stellungen; Sanierungsprivileg § 39 Abs. 4 InsO prüfen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `ifap-schuldnerwiderspruch-184`

**Fokus:** Schuldnerwiderspruch nach § 184 InsO prüfen und Fristen einhalten: Anwendungsfall Schuldner widerspricht Forderung und bei titulierten Forderungen laeuft Monatsfrist für Aufnahme des Rechtsstreits. § 184 InsO Schuldnerwiderspruch, § 179 InsO Feststellungsklage, § 183 InsO Wirkung bei Schuldnerwiderspruch. Prüfraster titulierte vs. nichttitulierte Forderung, Monatsfrist ab Prüfungstermin, Aufnahme laufender Verfahren, Kommunikationsbedarf. Output Widerspruchsprotokoll mit Fristkalender und Handlungsempfehlung. Abgrenzung zu Streitige-Forderung-179-180 und zu Prüfungstermin-176.

# Schuldnerwiderspruch nach § 184 InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Schuldnerwiderspruch nach § 184 InsO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Trennt Schuldnerwiderspruch von Tabellenbestreiten und hält die Monatsfrist bei titulierten Forderungen sichtbar.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Schuldner widerspricht
- titulierte Forderung mit Schuldnerwiderspruch
- Gläubiger fragt nach Wirkung

## Workflow

1. Widerspruchsart unterscheiden: Schuldner allein, Verwalter, Gläubiger, Kombination.
2. Feststellung gegenüber Verwalter/Gläubigern und Schuldnerwiderspruch getrennt darstellen.
3. Bei Titel oder Endurteil Monatsfrist für Schuldner-Nachweis markieren.
4. Bei nicht titulierten Forderungen Klageoption des Gläubigers gegen Schuldner erfassen.
5. Tabellen- und Kommunikationsvermerk für Gericht, Gläubiger und interne Akte vorbereiten.

## Ausgabe

- Schuldnerwiderspruchsvermerk
- Monatsfrist-Wiedervorlage
- Gläubigerhinweis
- Tabellenstatus

## Qualitätsgates

- Schuldnerwiderspruch wird nicht mit Verwalterbestreiten verwechselt.
- Monatsfrist beginnt konkret an Prüfungstermin oder schriftlichem Bestreiten.
- Keine Rechtsberatung an Gläubiger ohne Rollenprüfung.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 114/23 vom 19.12.2024** — Anforderungen an Individualisierung und Anmeldung bei Abtretung. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- Konkrete BGH-Linie zu § 184 InsO (Schuldnerwiderspruch, Klagebefugnis) und zur Vorsatzfeststellung iSd § 302 Nr. 1 InsO vor Ausgabe über dejure.org / openjur.de verifizieren.

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. **Vorsatz-Tatbestand benannt?** Für § 302 Nr. 1 InsO ausdrücklich Tatbestand der vorsätzlich unerlaubten Handlung in der Anmeldung benennen. Schuldnerwiderspruch nach § 184 InsO innerhalb der Frist klären.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `ifap-streitige-forderung-179-180`

**Fokus:** Streitige Forderungen nach §§ 179 und 180 InsO nachverfolgen: Anwendungsfall Forderung wurde beim Prüfungstermin bestritten und Gläubiger muss Feststellungsklage erheben oder laufenden Rechtsstreit aufnehmen. § 179 InsO Feststellungsklage, § 180 InsO Tabellenklage, § 184 InsO Schuldnerwiderspruch. Prüfraster Bestreitungsprotokoll, Klagefrist, Zuständiges Gericht, Titelumkehr bei Titel-Inhaber. Output Nachlaufprotokoll für bestrittene Forderungen mit Fristen und Klageempfehlung. Abgrenzung zu Schuldnerwiderspruch-184 und zu Verteilung-189.

# Streitige Forderung und Feststellungsklage

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Streitige Forderung und Feststellungsklage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Hält bestrittene Forderungen nach Prüfungstermin auf Kurs und verhindert verlorene Nachläufe.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Forderung wurde bestritten
- Gläubiger verlangt Tabellenauszug
- Titel liegt vor
- Rechtsstreit war anhängig

## Workflow

1. Bestreitenden identifizieren: Verwalter, Insolvenzgläubiger oder beide.
2. Titelstatus prüfen, weil bei Titel oder Endurteil die Verfolgungslast anders liegen kann.
3. Zuständigkeit nach § 180 InsO und anhängige Verfahren markieren.
4. Umfang nach § 181 InsO prüfen: Feststellung nur wie angemeldet oder im Prüfungstermin bezeichnet.
5. Nachlaufakte mit Klagefrist, Verantwortlichem, Prozessstand, Vergleichsoption und Tabellenberichtigung anlegen.

## Ausgabe

- Streitnachlaufkarte
- Tabellenauszug-Anforderung
- Feststellungsklage-Checkliste
- Wiedervorlagen

## Qualitätsgates

- Klageumfang darf Anmeldung nicht überschreiten.
- Titelumkehr wird ausdrücklich geprüft.
- Anhängige Verfahren werden nicht doppelt neu geklagt.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 114/23 vom 19.12.2024** — Forderungsanmeldung bei Abtretung: Zedent und Zessionar müssen jeweils separat anmelden und einen eigenen Prüfungstermin durchlaufen. Bestreiten kann auch auf Individualisierung gestützt werden. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Bei Anmeldungen kapitalmarktrechtlicher Schadensersatzforderungen geschädigter Aktionäre den Nachrang einwenden (keine § 38 InsO-Forderung).

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. **Bestreitung substantiiert?** Wer bestreitet, muss konkret begründen (Grund, Höhe, Rang). Bei Vorsatz-Forderungen § 184 InsO Schuldnerwiderspruch eigenständig prüfen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

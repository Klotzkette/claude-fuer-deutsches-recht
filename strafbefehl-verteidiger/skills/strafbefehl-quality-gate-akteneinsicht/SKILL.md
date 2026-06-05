---
name: strafbefehl-quality-gate-akteneinsicht
description: "Quality Gate Akteneinsicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Quality Gate Akteneinsicht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Quality Gate Akteneinsicht** im Plugin Strafbefehl-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `strafbefehl-kommandocenter` | Einstieg in das Strafbefehl-Mandat — Ampel-Schnelldiagnose zeigt kritische Fristen und offene Handlungsfelder auf einen Blick. Zentrales Steuerungsmodul routet auf Subskills: Frist § 410 StPO Akteneinsicht § 147 StPO Inhaltsprüfung § 409 StPO Beweis Einlassung Verständigung Einstellung Tagessaetze Nebenfolgen Pflichtverteidiger Wiedereinsetzung. Normen §§ 407-412 StPO. Output Mandats-Ampelstatus mit priorisierten naechsten Schritten. Abgrenzung: strafbefehl-fristen-einspruch für die isolierte Fristprüfung. |
| `strafbefehl-quality-gate` | Vor dem Einspruch-Versand vor der Hauptverhandlung oder nach dem Urteil eine Abschlussprüfung durchführen. Prüfraster Fristen Vollmacht Zulässigkeit Einlassung Beweisanträge Strafzumessung Protokoll. Normen § 410 StPO Einspruchsfrist § 409 StPO Strafbefehlsinhalt § 46 StGB Strafzumessung. Output Fehlerliste mit Ampel-Bewertung und Checkliste offener Punkte. Abgrenzung: strafbefehl-kommandocenter für laufende Mandats-Steuerung. |
| `spezial-akteneinsicht-behoerden-gericht-und-registerweg` | Akteneinsicht: Behörden-, Gerichts- oder Registerweg im Plugin strafbefehl verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Strafbefehl-Verteidigung gilt für **Quality Gate Akteneinsicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `strafbefehl-kommandocenter`

**Fokus:** Einstieg in das Strafbefehl-Mandat — Ampel-Schnelldiagnose zeigt kritische Fristen und offene Handlungsfelder auf einen Blick. Zentrales Steuerungsmodul routet auf Subskills: Frist § 410 StPO Akteneinsicht § 147 StPO Inhaltsprüfung § 409 StPO Beweis Einlassung Verständigung Einstellung Tagessaetze Nebenfolgen Pflichtverteidiger Wiedereinsetzung. Normen §§ 407-412 StPO. Output Mandats-Ampelstatus mit priorisierten naechsten Schritten. Abgrenzung: strafbefehl-fristen-einspruch für die isolierte Fristprüfung.

# Strafbefehl-Verteidiger — Kommandocenter

## Zweck

Dieses Kommandocenter ist der Einstiegspunkt fuer alle Mandate im Strafbefehlsverfahren. Es erfasst den Mandats-Kontext, bewertet die Dringlichkeit und routet zur richtigen Subskill-Anleitung.

## Sofort-Triage bei Mandatsaufnahme

**Die drei kritischen Fragen zuerst:**

1. **Fristlage:** Wann wurde der Strafbefehl zugestellt? Einspruchsfrist § 410 Abs. 1 StPO: 2 Wochen ab Zustellung. Ist die Frist noch offen oder abgelaufen?
 - Frist offen → Einspruch sofort einlegen, dann vertiefen
 - Frist abgelaufen → Wiedereinsetzung § 44 StPO pruefen

2. **Delikt und Sanktion:** Was wird vorgeworfen (§§ StGB/StVG/OWiG)? Welche Rechtsfolge ist angesetzt (Tagessaetze, Geldstrafe, Fahrverbot, Bewaehrungsstrafe)?

3. **Mandantenziel:** Freispruch / Einstellung / Strafmassreduzierung / Fahrverbots-Vermeidung?

## Ampel-Schnelldiagnose

| Situation | Ampel | Massnahme |
|-----------|-------|-----------|
| Frist laeuft in < 3 Tagen | ROT | Einspruch SOFORT, dann vertiefen |
| Frist laeuft in 4-7 Tagen | GELB | Einspruch und Akteneinsicht parallel |
| Frist > 7 Tage | GRUEN | Strukturierte Bearbeitung |
| Frist abgelaufen, keine Wiedereinsetzungsgruende | ROT | Strafbefehl rechtskraeftig |
| Frist abgelaufen, Grund fuer Wiedereinsetzung | GELB | Wiedereinsetzungsantrag § 44 StPO |

## Routing-Matrix

| Aufgabe | Subskill |
|---------|---------|
| Einspruchsfrist berechnen + einlegen | `strafbefehl-fristen-einspruch` |
| Strafbefehl-Inhalt auf § 409 pruefen | `strafbefehl-inhalt-409-pruefung` |
| Akteneinsicht anfordern | `strafbefehl-akteneinsicht-147` |
| Beweis- und Einlassungsstrategie | `strafbefehl-beweis-und-einlassung` |
| Beschraenkter Einspruch | `strafbefehl-einspruch-beschraenkung` |
| Verstaendigung / § 153a | `strafbefehl-deal-verstaendigung` |
| Einstellung § 153 / § 153a / § 170 | `strafbefehl-einstellung-153-153a-170` |
| Tagessatz-Berrechnung | `strafbefehl-tagessaetze-geldstrafe` |
| Nebenfolgen Fahrerlaubnis | `strafbefehl-nebenfolgen-fahrerlaubnis` |
| Pflichtverteidiger-Bestellung | `strafbefehl-pflichtverteidiger` |
| Wiedereinsetzung nach Fristversaeumnis | `strafbefehl-wiedereinsetzung` |
| Hauptverhandlung vorbereiten | `strafbefehl-hauptverhandlung-vorbereitung` |
| Abwesenheit in der HV | `strafbefehl-abwesenheit-vertretung` |
| Rechtsmittel nach Urteil | `strafbefehl-rechtsmittel-nach-urteil` |
| Zeugen befragen | `strafbefehl-zeugen-befragungsstrategie` |
| Rechtsprechungsrecherche | `strafbefehl-rechtsprechungsrecherche` |
| Quality Gate | `strafbefehl-quality-gate` |
| Aktenanlage | `strafbefehl-aktenanlage` |

## Zentrale Normen im Strafbefehlsverfahren

- **§ 407 StPO** — Zulassungsvoraussetzungen
- **§ 408 StPO** — Richterliche Entscheidung
- **§ 409 StPO** — Pflichtinhalt
- **§ 410 StPO** — Einspruch, 2-Wochen-Frist, Beschraenkung
- **§ 411 StPO** — Hauptverhandlung nach Einspruch
- **§ 412 StPO** — Verwerfung des Einspruchs bei unentschuldigtem Ausbleiben
- **§ 44 StPO** — Wiedereinsetzung

## Aktuelle Querschnitts-Rechtsprechung (Stand Mai 2026)

- BGH (GSSt) 03.02.2025 — GSSt 1/24 (KCanG, Querschnittswirkung im Cannabis-Strafbefehl): https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- BGH 15.07.2025 — 2 StR 644/24 (KCanG-Strafzumessung): https://dejure.org/dienste/vernetzung/rechtsprechung?Text=2+StR+644/24
- BGH 20.11.2025 — 4 StR 232/25 (TOA § 46a Nr. 1 StGB): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25
- BVerfG 23.09.2025 — 2 BvR 625/25 (ANOM-Verwertbarkeit): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=23.09.2025&Aktenzeichen=2+BvR+625/25
- Weitere Rechtsprechung vor Ausgabe in dejure.org / openjur.de mit Gericht, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Harte Leitplanken

- Frist immer zuerst — kein Schritt ohne Fristensicherung.
- Vollmacht vor Akteneinsicht.
- Keine Einlassung ohne Aktenkenntnis.
- Anwaltliche Endkontrolle bei allen Fristen, Antraegen und Einlassungen.

## 2. `strafbefehl-quality-gate`

**Fokus:** Vor dem Einspruch-Versand vor der Hauptverhandlung oder nach dem Urteil eine Abschlussprüfung durchführen. Prüfraster Fristen Vollmacht Zulässigkeit Einlassung Beweisanträge Strafzumessung Protokoll. Normen § 410 StPO Einspruchsfrist § 409 StPO Strafbefehlsinhalt § 46 StGB Strafzumessung. Output Fehlerliste mit Ampel-Bewertung und Checkliste offener Punkte. Abgrenzung: strafbefehl-kommandocenter für laufende Mandats-Steuerung.

# Quality Gate — Strafbefehl-Mandat

## Zweck

Dieser Skill ist die abschliessende Qualitaetssicherung fuer das Strafbefehlsmandat. Er ist an drei kritischen Punkten einzusetzen:
1. **Vor Einspruch-Versand** — alle formalen Voraussetzungen erfuellt?
2. **Vor der Hauptverhandlung** — vollstaendige Vorbereitung?
3. **Nach dem Urteil** — Rechtsmitteloptionen geprueft?

## Gate 1: Vor Einspruch-Versand

```
□ Einspruchsfrist § 410 Abs. 1 StPO berechnet und noch offen?
 Zustellungsdatum: [DATUM] + 14 Tage = Fristende: [DATUM]
□ Vollmacht des Mandanten liegt vor?
□ Strafbefehl-Inhalt auf § 409 StPO geprueft (Pflicht-Inhalte)?
□ Delikt ist Vergehen (kein Verbrechen § 12 StGB)?
□ Sanktion liegt im Katalog § 407 Abs. 2 StPO?
□ Beschraenkt oder unbeschraenkt? Mandant aufgeklaert?
□ Einspruchsschreiben: Name, Az., Zustellungsdatum, Datum, Unterschrift?
□ Einspruch per EB-Fax oder anwaltlichem Fax versendet?
□ Eingang beim Gericht bestaetigt?
□ Akteneinsicht gleichzeitig beantragt?
AMPEL: GRUEN wenn alle Punkte erfuellt / ROT wenn Frist nicht mehr offen
```

## Gate 2: Vor Hauptverhandlung

```
□ Akteneinsicht vollstaendig erhalten und ausgewertet?
□ Einlassung mit Mandant abgestimmt (Schweigen oder Aussage)?
□ Beweisantraege vorbereitet (Beweisthema + Beweismittel)?
□ Sachverstaendiger beauftragt wenn noetig?
□ Einkommensnachweise fuer Tagessatz-Pruefung vollstaendig?
□ § 153a-Antrag bei Staatsanwaltschaft gestellt oder abgelehnt?
□ Verstaendigung § 257c StPO geprueft und entschieden?
□ Mandant ueber HV-Ablauf informiert (Aufruf, Vernehmung, Plaedoyer, Letztes Wort)?
□ Fahrerlaubnis-Problematik (§ 69 StGB / § 44 StGB) vollstaendig bearbeitet?
□ Pflichtverteidiger-Beiordnung geprueft (§ 140 StPO)?
□ Erscheinungspflicht oder Entbindungsantrag § 411 Abs. 2 StPO?
AMPEL: GRUEN wenn vollstaendig / GELB wenn offene Punkte / ROT wenn kritische Luecken
```

## Gate 3: Nach Urteil

```
□ Urteil vollstaendig angehoert / protokolliert?
□ Rechtsmittelfrist notiert: 1 Woche ab Urteilsverkuendung (§§ 314, 341 StPO)?
□ Fristende: [DATUM DES URTEILS] + 7 Tage = [FRISTENDE]
□ Berufung oder Revision geprüft? (Tatsachen vs. Rechtsfehler)
□ Annahme-Berufung § 313 StPO: Erfolgaussichten vorhanden?
□ Absolute Revisionsgründe § 338 StPO geprueft?
□ Tagessatz-Hoehe korrekt berechnet?
□ Fahrerlaubnis-Massnahme korrekt?
□ Beschraenktes Rechtsmittel auf Rechtsfolgen moeglich?
□ Mandant ueber Entscheidung und Optionen informiert?
□ Ratenzahlungsantrag § 42 StGB noetig?
AMPEL: GRUEN wenn zufriedenstellend / GELB wenn Rechtsmittel moeglich / ROT wenn Fehler vorhanden
```

## Harte Leitplanken

- Quality Gate niemals ueberspringen — auch bei einfachen Faellen.
- ROT-Punkte immer dokumentieren und ansprechen.
- Mandant ueber jeden Schritt informieren und Entscheidungen schriftlich bestaetigen.
- Anwaltliche Endkontrolle bei jedem Gate zwingend.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `spezial-akteneinsicht-behoerden-gericht-und-registerweg`

**Fokus:** Akteneinsicht: Behörden-, Gerichts- oder Registerweg im Plugin strafbefehl verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Akteneinsicht: Behörden-, Gerichts- oder Registerweg



## Spezialwissen: Akteneinsicht: Behörden-, Gerichts- oder Registerweg
- **Konkreter Gegenstand:** Akteneinsicht: Behörden-, Gerichts- oder Registerweg im Plugin strafbefehl verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung..
- **Normen-/Verfahrensanker:** StPO §§ 407 ff., Einspruchsfrist, Wiedereinsetzung, Pflichtverteidigung, Tagessatzsystem, Einstellungsmöglichkeiten und Beweisverwertungsfragen.
- **Entscheidende Weiche:** Tat, Beweis, Rechtsfolge, Frist, Mandantenziel und Kostenrisiko so trennen, dass sofort klar wird: Einspruch voll, beschränkt oder Rücknahme/Deal.
- **Arbeitsprodukt:** Erstelle eine fallbezogene Matrix `Behauptung / Norm / Beleg / Risiko / Gegenargument / nächster Schritt`; keine bloße Wiederholung des allgemeinen Plugin-Workflows.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Akteneinsicht** prüfen.
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

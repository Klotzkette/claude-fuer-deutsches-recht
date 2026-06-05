---
name: strafbefehl-einspruch-aktenanlage
description: "Einspruch Aktenanlage: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Einspruch Aktenanlage

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Einspruch Aktenanlage** im Plugin Strafbefehl-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-gegen-fristen-form-und-zustaendigkeit` | Gegen: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin strafbefehl verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `strafbefehl-fristen-einspruch` | Sichert die Einspruchsfrist nach § 410 StPO (2 Wochen ab Zustellung) und erstellt Einspruchsentwuerfe. Berechnung Zustellungsfiktion § 418 ZPO i.V.m. § 37 StPO. Unbeschraenkter oder beschraenkter Einspruch § 410 Abs. 2 StPO. Wiedereinsetzung § 44 StPO. Fristenblatt Mandantenhinweis Einspruchsschreiben. |
| `strafbefehl-aktenanlage` | Neues Strafbefehl-Mandat anlegen und Mandatsakte strukturieren damit Fristen und Beweismittel sicher verwaltet werden. Prüfraster Aktenstruktur Vollmacht Fristenkalender Beweismittelverzeichnis. Normen § 410 StPO Einspruchsfrist § 147 StPO Akteneinsicht § 43 StPO Fristberechnung. Output Mandatsakte-Template Fristenuebersicht Excel-Export Akten-Checkliste. Abgrenzung: strafbefehl-kommandocenter für uebergreifende Mandats-Steuerung. |

## Arbeitsweg

Im Plugin Strafbefehl-Verteidigung gilt für **Einspruch Aktenanlage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-gegen-fristen-form-und-zustaendigkeit`

**Fokus:** Gegen: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin strafbefehl verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Gegen: Fristen, Form, Zuständigkeit und Rechtsweg



## Spezialwissen: Gegen: Fristen, Form, Zuständigkeit und Rechtsweg
- **Konkreter Gegenstand:** Gegen: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin strafbefehl verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung..
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Gegen** prüfen.
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

## 2. `strafbefehl-fristen-einspruch`

**Fokus:** Sichert die Einspruchsfrist nach § 410 StPO (2 Wochen ab Zustellung) und erstellt Einspruchsentwuerfe. Berechnung Zustellungsfiktion § 418 ZPO i.V.m. § 37 StPO. Unbeschraenkter oder beschraenkter Einspruch § 410 Abs. 2 StPO. Wiedereinsetzung § 44 StPO. Fristenblatt Mandantenhinweis Einspruchsschreiben.

# Frist und Einspruch nach § 410 StPO

## Triage zu Beginn — Sofort klaeren

1. **Zugangsdatum Strafbefehl:** Wann wurde der Strafbefehl zugestellt? Postzustellung (§ 37 StPO i.V.m. §§ 177 ff. ZPO) oder persoenliche Uebergabe?
2. **Zustellungsfiktion pruefen:** Bei Postzustellung gilt § 418 ZPO — Einwurf-Einschreiben drei Tage nach Aufgabe als zugestellt, es sei denn Mandant weist spaetere Kenntnisnahme nach.
3. **Fristende berechnen:** Tag der Zustellung + 14 Tage (§ 410 Abs. 1 StPO), §§ 42, 43 StPO zur Berechnung; Fristende auf Samstag/Sonntag/Feiertag — naechster Werktag.
4. **Reaktion des Mandanten bislang:** Hat der Mandant bereits reagiert, einen Pro-forma-Einspruch selbst eingelegt?
5. **Ziel des Mandanten:** Einstellung (§§ 153, 153a StPO), Verhandlung und Freispruch, Strafmassreduzierung — beeinflusst ob beschraenkt oder unbeschraenkt.

## Zentrale Normen

- **§ 407 StPO** — Zulassungsvoraussetzungen Strafbefehl
- **§ 408 StPO** — Entscheidung des Richters, Bedenken-Anmeldung
- **§ 409 StPO** — Pflichtinhalt des Strafbefehls (§ 409 Abs. 1 Nr. 1-7 StPO)
- **§ 410 Abs. 1 StPO** — Einspruchsfrist 2 Wochen ab Zustellung
- **§ 410 Abs. 2 StPO** — beschraenkter Einspruch (nur Rechtsfolgen)
- **§ 410 Abs. 3 StPO** — Strafbefehl wird rechtskraeftig bei Fristversaeumnis (Urteilswirkung)
- **§ 44 StPO** — Wiedereinsetzung in den vorigen Stand
- **§ 37 StPO i.V.m. §§ 177 ff. ZPO** — Zustellungsvorschriften
- **§ 418 ZPO** — Beweis durch Zustellungsurkunde; bei Einwurf-Einschreiben § 180 ZPO

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Frist sofort berechnen und dokumentieren:** Zugangsdatum (aus Zustellungsurkunde oder Mandantenangabe) + 14 Tage = Fristende; in Fristenkalender einpflegen, 3-Tage-Vorlauf-Wiedervorlage setzen.
2. **Strafbefehl auf Pflichtinhalt pruefen (§ 409 StPO):** Fehlt ein Pflichtbestandteil, kann dies zur Nichtigkeit fuehren — Antrag auf Berichtigung oder Aufhebung.
3. **Zustellungsfiktion pruefen:** Einwurf-Einschreiben? Mandant ueber § 180 ZPO aufklaeren; bei Zweifeln Mandant schriftlich bestaetigenden Hinweis geben lassen.
4. **Einspruch formulieren:** Unbeschraenkt als Standardweg — Beschraenkung auf Rechtsfolgen nur wenn Schuldspruch unstreitig und Strafmassreduzierung das einzige Ziel.
5. **Einspruch per EB oder anwaltlichem Fax einlegen** — Empfangsbekenntnis sichern.
6. **Hauptverhandlung vorbereiten** — nach Einspruch wird Termin bestimmt (§ 411 StPO); Akte anfordern, Einlassung abstimmen.

## Entscheidungsbaum Einspruchsstrategie

```
Mandanteninteresse?
├─ Freispruch / Einstellung angestrebt
│ └─ Unbeschraenkter Einspruch → Hauptverhandlung voll
├─ Schuld anerkannt, nur Strafe verringern
│ └─ Beschraenkter Einspruch § 410 Abs. 2 StPO auf Rechtsfolgen
│ ├─ Geldstrafe zu hoch? → Nettoeinkommen belegen
│ └─ Fahrverbot angreifbar? → Haertefallargument pruefen
└─ Einstellung wuenschenswert
 └─ Vor Hauptverhandlung § 153a-Antrag bei Staatsanwaltschaft

Zustellungsdatum klar?
├─ Ja → Frist berechnen, Einspruch formulieren
└─ Nein
 ├─ Mandant erinnert sich an Datum → Frist berechnen + Sicherheitspuffer
 └─ Datum unklar → Wiedereinsetzungsantrag nach § 44 StPO parallel vorbereiten
```

## Output-Template Einspruchsschreiben

**Adressat:** Amtsgericht [ORT] — Tonfall: sachlich-foermlich

```
An das Amtsgericht [ORT]
Strafrichter / Strafbefehlsabteilung
[Anschrift]

In der Strafsache gegen
[NAME MANDANT], geb. [DATUM], [ADRESSE]
Az.: [AKTENZEICHEN]

Einspruch gegen den Strafbefehl vom [DATUM DES STRAFBEFEHLS]

Sehr geehrte Damen und Herren,

namens und im Auftrag des Beschuldigten [NAME MANDANT], dessen
Verteidigung ich uebernommen habe, lege ich

Einspruch

gegen den Strafbefehl des Amtsgerichts [ORT] vom [DATUM],
zugestellt am [ZUSTELLUNGSDATUM], form- und fristgerecht ein.

[Optional: Der Einspruch wird auf die Rechtsfolgen beschraenkt.
§ 410 Abs. 2 StPO — der Schuldspruch ist nicht Gegenstand
des Einspruchs.]

Ich bitte um Uebersendung der Verfahrensakten zur Vorbereitung
der Hauptverhandlung.

Mit freundlichen Gruessen
[KANZLEI]
```

## Mandantenhinweis-Template

**Adressat:** Mandant — Tonfall: verstaendlich-erklaerend

```
Sehr geehrte/r Frau/Herr [NAME],

Sie haben einen Strafbefehl erhalten. Ich habe fristgerecht
Einspruch eingelegt. Die Frist lief am [DATUM] ab.

Was jetzt passiert: Das Amtsgericht setzt einen Verhandlungstermin
an (§ 411 StPO). Ich werde Sie rechtzeitig informieren.

Wichtig: Kommen Sie bitte nicht zur Polizei oder Staatsanwaltschaft
ohne mich vorher zu kontaktieren. Machen Sie keine Angaben zur
Sache.

Mit freundlichen Gruessen
[KANZLEI]
```

## Harte Leitplanken

- Niemals Einspruchsfrist ohne Fristenkalender-Eintrag.
- Beschraenkter Einspruch nur nach Mandantenruecksprache und schriftlicher Bestaetigung der Konsequenzen.
- Wiedereinsetzung nach § 44 StPO erfordert Glaubhaftmachung — Mandant muss eidesstattliche Versicherung liefern.
- Anwaltliche Endkontrolle vor Versand zwingend.

## 3. `strafbefehl-aktenanlage`

**Fokus:** Neues Strafbefehl-Mandat anlegen und Mandatsakte strukturieren damit Fristen und Beweismittel sicher verwaltet werden. Prüfraster Aktenstruktur Vollmacht Fristenkalender Beweismittelverzeichnis. Normen § 410 StPO Einspruchsfrist § 147 StPO Akteneinsicht § 43 StPO Fristberechnung. Output Mandatsakte-Template Fristenuebersicht Excel-Export Akten-Checkliste. Abgrenzung: strafbefehl-kommandocenter für uebergreifende Mandats-Steuerung.

# Aktenanlage im Strafbefehlsverfahren

## Triage zu Beginn

1. **Liegt die Vollmacht des Mandanten vor?** — Ohne Vollmacht keine Verfahrenshandlungen.
2. **Zugangsdatum des Strafbefehls dokumentiert?** — Ausgangspunkt fuer alle Fristen.
3. **Delikt und Aktenzeichen notiert?** — Grundlage fuer alle Schriftsaetze.
4. **Mandantenziel festgehalten?** — Freispruch, Einstellung, Strafmassreduzierung, Fahrverbots-Vermeidung.
5. **Sofortmassnahmen ausgeloest?** — Einspruch fristgerecht eingelegt? Akteneinsicht beantragt?

## Aktenstruktur Strafbefehlsmandat

```
01_MANDANT
 - Vollmacht Original
 - Personalien, Kontakt
 - Mandantenziel (schriftlich)

02_STRAFBEFEHL
 - Strafbefehl Original / Kopie
 - Zustellungsurkunde
 - § 409-Pruefungs-Notiz

03_FRISTEN
 - Fristen-Uebersicht (Excel oder Tabelle)
 - Einspruchsfrist: [DATUM]
 - Revisionsbegründungsfrist (falls noetig): [DATUM]

04_SCHRIFTSAETZE_AUSGEHEND
 - Einspruch (mit Eingangsbestaetigung)
 - Akteneinsichtsantrag
 - Weitere Antraege

05_AKTENEINSICHT
 - Ermittlungsakte vollstaendig
 - Messakte (bei Verkehrsdelikten)
 - Beweismittelverzeichnis

06_KORRESPONDENZ
 - Behörden, Gericht, StA
 - E-Mails chronologisch

07_HAUPTVERHANDLUNG
 - Einlassung (Endfassung)
 - Beweisantraege
 - Plaedoyer

08_URTEIL_RECHTSMITTEL
 - Urteil Original
 - Rechtsmittelschrift
 - Revisionsbegründung
```

## Fristen-Uebersicht — Template

| Frist | Rechtsgrundlage | Datum | Erledigt |
|-------|----------------|-------|---------|
| Einspruch | § 410 Abs. 1 StPO | [Zustellung + 14 Tage] | □ |
| Akteneinsicht | § 147 StPO | [Sofort] | □ |
| Wiedereinsetzung (falls noetig) | § 45 Abs. 1 StPO | [Kenntnis + 7 Tage] | □ |
| Berufung | § 314 StPO | [Urteil + 7 Tage] | □ |
| Revision | § 341 StPO | [Urteil + 7 Tage] | □ |
| Revisionsbegründung | § 345 StPO | [Urteilszustellung + 1 Monat] | □ |

## Beweismittelverzeichnis — Template

| Nr. | Beweismittel | Art | Akten-Bl. | Beweisthema | Status |
|-----|-------------|-----|----------|-------------|--------|
| 1 | Zeuge [Name] | Zeuge | Bl. [X] | [Thema] | auswerten |
| 2 | Polizeibericht | Urkunde | Bl. [X] | Tathergang | auswerten |
| 3 | Messprotokoll | Urkunde | Bl. [X] | Geschwindigkeit | kritisch pruefen |

## Zentrale Normen

- **§ 147 StPO** — Akteneinsicht
- **§ 410 StPO** — Einspruchsfrist
- **§ 44, 45 StPO** — Wiedereinsetzung
- **§ 314, 341, 345 StPO** — Rechtsmittelfristen

## Harte Leitplanken

- Aktenanlage unmittelbar bei Mandatsuebernahme — nicht nach Einspruch.
- Fristenkalender zwingend fuehren, nie im Kopf.
- Vollmacht immer im Original verwahren.
- Bei Aktennachlieferungen: Verzeichnis aktualisieren, neue Teile markieren.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

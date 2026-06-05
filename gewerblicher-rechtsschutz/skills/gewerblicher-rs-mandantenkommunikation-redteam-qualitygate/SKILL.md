---
name: gewerblicher-rs-mandantenkommunikation-redteam-qualitygate
description: "RS Mandantenkommunikation Redteam Qualitygate: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# RS Mandantenkommunikation Redteam Qualitygate

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **RS Mandantenkommunikation Redteam Qualitygate** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im gewerblichen Rechtsschutz: strukturierte Kommunikation in IP-Mandaten – Erstinformation, Statusupdates, Entscheidungsvorlagen, Kostenhinweise und Abschlussberichte. Templates und Tonalitätsregeln für Kanzlei und Rechtsabteilung. |
| `workflow-redteam-qualitygate` | Red-Team-Quality-Gate für das Plugin gewerblicher-rechtsschutz: systematischer letzter Check vor Abgabe von Schriftsätzen, Memos, Abmahnungen und Entscheidungsvorlagen. Sechs Qualitätsstufen, Freigabe-Entscheidung und Dokumentation. |
| `evvollzug-neu-001-einstweilige-verfuegung-vollziehung-frist-und` | EV-Vollzug: Vollziehungsfrist § 929 Abs. 2 ZPO und Parteizustellung im gewerblichen Rechtsschutz. Beschluss- und Urteilsverfügung, Zustellwege, Vollziehungsversäumnis und Rechtsfolgen. Praxisfür Anwalt, Mandant und Vollstreckungsorgan. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **RS Mandantenkommunikation Redteam Qualitygate**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im gewerblichen Rechtsschutz: strukturierte Kommunikation in IP-Mandaten – Erstinformation, Statusupdates, Entscheidungsvorlagen, Kostenhinweise und Abschlussberichte. Templates und Tonalitätsregeln für Kanzlei und Rechtsabteilung.

# Workflow: Mandantenkommunikation

## Zweck

Dieser Skill strukturiert die **Kommunikation mit Mandanten** in IP- und Wettbewerbsschutzmandaten. Er liefert Templates und Tonalitätsregeln für alle typischen Kommunikationssituationen – von der Erstinformation bis zum Abschlussbericht.

Mandatsbezug: Anwalt hat EV-Antrag vorbereitet und muss Mandanten informieren. Kanzlei sendet wöchentlichen Statusbericht. Rechtsabteilungsleiterin braucht Vorlage für Vorstandsbericht zu laufenden IP-Verfahren.

## Grundsätze der IP-Mandantenkommunikation

### Prinzip 1 – Ergebnis zuerst

- Nie lange Vorreden; Mandant will zuerst wissen: Was bedeutet das für mich?
- Dann: Begründung, Details, Optionen.
- BLUF-Methode: Bottom Line Up Front.

### Prinzip 2 – Fristen explizit

- Jede Kommunikation, in der eine Frist relevant ist, muss die Frist fett/kursiv hervorheben.
- Datum, Uhrzeit (falls relevant) und Konsequenz bei Versäumnis.

### Prinzip 3 – Optionen nennen, Empfehlung geben

- Nie nur eine Möglichkeit; mindestens zwei Optionen mit Kosten und Risiken.
- Eigene Empfehlung mit Begründung.

### Prinzip 4 – Keine Scheingenauigkeit

- Keine konkreten Prozentzahlen für Erfolgswahrscheinlichkeit, wenn keine Grundlage.
- Stattdessen: „Gute Erfolgsaussichten", „Risikobehafteter Fall", „Offene Rechtsfrage".

### Prinzip 5 – Mandant entscheidet, Anwalt berät

- Entscheidung liegt beim Mandanten; Anwalt gibt Empfehlung.
- Mandantenentscheidung schriftlich bestätigen lassen.

## Kommunikations-Templates

### Template 1 – Erstinformation nach Mandatsannahme

```
Betr.: [Sachbetreff] – Erstinformation

Sehr geehrte/r [Herr/Frau X],

wir haben Ihr Mandat angenommen und werden Sie in der Angelegenheit
[kurze Beschreibung] vertreten.

SITUATION (Stand [Datum]):
[2–3 Sätze zur Ausgangslage]

NÄCHSTER SCHRITT:
[Konkrete Handlung, z.B. „Abmahnung wird bis [Datum] versandt"]

WICHTIGE FRIST:
[Datum] – [Beschreibung der Frist und Konsequenz bei Versäumnis]

ZU IHRER KENNTNIS:
- Unsere Kosten für diesen Schritt: ca. [Betrag] EUR zzgl. MwSt.
- Für Rückfragen erreichen Sie mich unter [Kontakt].

Mit freundlichen Grüßen
[Anwalt]
```

### Template 2 – Statusbericht (laufendes Verfahren)

```
Betr.: [Sachbetreff] – Statusbericht [Datum]

Sehr geehrte/r [Herr/Frau X],

kurzer Statusbericht zum aktuellen Stand:

WAS IST PASSIERT:
[1–3 Sätze, was sich seit letztem Bericht getan hat]

WO STEHEN WIR:
[Aktueller Verfahrensstand; z.B. „EV erlassen, Vollzug läuft"]

OFFENE PUNKTE:
[Was noch unklar oder in Bearbeitung ist]

NÄCHSTER SCHRITT:
[Was als nächstes passiert und bis wann]

FRIST: [Datum und Beschreibung]

[Unterschrift]
```

### Template 3 – Entscheidungsvorlage

```
Betr.: [Sachbetreff] – Bitte um Entscheidung bis [Datum]

Sehr geehrte/r [Herr/Frau X],

wir bitten um Ihre Entscheidung zu folgendem Punkt:

SITUATION:
[Kurze Darstellung des Problems]

OPTIONEN:
A) [Option A] – Kosten ca. [Betrag]; Risiko: [kurz]
B) [Option B] – Kosten ca. [Betrag]; Risiko: [kurz]

UNSERE EMPFEHLUNG: Option [A/B], weil [kurze Begründung]

BITTE ENTSCHEIDEN SIE BIS: [Datum]
(Bei Fristversäumnis: [Konsequenz])

□ Option A □ Option B □ Rücksprache gewünscht

[Unterschrift]
```

### Template 4 – Abschlussinfo nach erfolgreichem EV-Vollzug

```
Betr.: [Sachbetreff] – Einstweilige Verfügung vollzogen

Sehr geehrte/r [Herr/Frau X],

wir freuen uns, Ihnen mitteilen zu können, dass die einstweilige Verfügung
des [Gericht] vom [Datum] dem Antragsgegner [Name] am [Datum] durch
Gerichtsvollzieher zugestellt wurde (Anlage: Zustellurkunde).

NÄCHSTER SCHRITT:
Der Antragsgegner hat nun die Möglichkeit, Widerspruch einzulegen.
Wir werden die Lage beobachten und Sie über die Entwicklung informieren.
In ca. [Zeitraum] werden wir ein Abschlussschreiben an den Antragsgegner
senden, um die Angelegenheit dauerhaft zu klären.

BEI EINEM VERSTOSS GEGEN DIE VERFÜGUNG:
Bitte informieren Sie uns sofort, wenn Sie feststellen, dass der Antragsgegner
gegen die Unterlassungspflicht verstößt. Wir können dann Ordnungsgeld beantragen.

KOSTEN: [Bisherige Kosten; zu erwartende weitere Kosten]

[Unterschrift]
```

### Template 5 – Kostenhinweis bei Eskalation

```
Betr.: [Sachbetreff] – Kostenhinweis Hauptsacheklage

Sehr geehrte/r [Herr/Frau X],

Sie haben entschieden, Hauptsacheklage zu erheben. Bitte nehmen Sie die
folgende Kostenübersicht zur Kenntnis:

Streitwert: ca. [Betrag] EUR
Gerichtskosten Vorschuss: ca. [Betrag] EUR
Anwaltskosten (1,3 Verfahrensgebühr): ca. [Betrag] EUR
Anwaltskosten (1,2 Terminsgebühr): ca. [Betrag] EUR
Gesamt (erste Instanz): ca. [Betrag] EUR

Bei Obsiegen: Kostenstattung ca. [Betrag] EUR
Bei Niederlage: Kostentragung ca. [Betrag] EUR (eigene + gegnerische Kosten)

Bitte bestätigen Sie die Klageerhebung mit Ihrer Unterschrift.

□ Ich bestätige die Erhebung der Hauptsacheklage und nehme das Kostenrisiko zur Kenntnis.

[Unterschrift]
```

## Tonalitätsregeln

| Situation | Ton | Beispiel |
|---|---|---|
| Erfolgsmeldung (EV erlassen) | Professionell, sachlich | „Die EV wurde antragsgemäß erlassen" |
| Risiko-Hinweis | Klar, ohne Alarm | „Es besteht ein Kostenrisiko von ca. X EUR" |
| Niederlage | Sachlich, mit Ausblick | „Das Gericht hat den Antrag abgelehnt; wir prüfen Rechtsmittel" |
| Mandant ist aufgeregt | Beruhigend, aber klar | „Wir haben die Situation im Griff; nächster Schritt ist..." |
| Termindruck | Direkt | „WICHTIG: Frist endet am [Datum]" |

## Quellenregel

- Keine externen Quellen für diesen Kommunikationsskill.
- Kosten immer nach aktuellem RVG und GKG berechnen; [gesetze-im-internet.de/rvg](https://www.gesetze-im-internet.de/rvg/).
- Keine Pauschalgebührenangaben ohne Streitwert-Grundlage.

## Anschluss-Skills

- `spezial-compliance-mandantenkommunikation-entscheidungsvorlage` – Entscheidungsvorlagen
- `workflow-output-waehlen` – Output-Format wählen
- `workflow-fristen-und-risikoampel` – Fristencheck

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team-Quality-Gate für das Plugin gewerblicher-rechtsschutz: systematischer letzter Check vor Abgabe von Schriftsätzen, Memos, Abmahnungen und Entscheidungsvorlagen. Sechs Qualitätsstufen, Freigabe-Entscheidung und Dokumentation.

# Workflow: Red-Team Quality Gate

## Zweck

Dieser Skill ist das **letzte Qualitätstor** vor der Abgabe eines Dokuments – Schriftsatz, Abmahnung, Memo, Entscheidungsvorlage oder Mandantenbrief. Er stellt sicher, dass das Dokument formal korrekt, materiell belastbar, quellengestützt und frei von blinden Flecken ist.

Mandatsbezug: Anwalt hat EV-Antrag fertiggestellt und will ihn vor Einreichung einem systematischen Review unterziehen. Oder: Kanzlei-Qualitätssicherung prüft alle ausgehenden Abmahnschreiben durch den Quality-Gate-Prozess.

## Quality-Gate: Sechs Stufen

### Stufe 1 – Formaler Check (5 Minuten)

**Fragen:**
- [ ] Ist das Dokument vollständig adressiert (Empfänger, Absender, Datum)?
- [ ] Sind alle Anlagen vorhanden und im Text referenziert?
- [ ] Ist das Dokument unterschrieben oder signiert (beA-Pflicht)?
- [ ] Stimmt die Fristangabe im Dokument?
- [ ] Ist das Aktenzeichen korrekt?

**Ergebnis:** Alle Punkte grün → Weiter zu Stufe 2. Sonst korrigieren.

### Stufe 2 – Fristen-Check (3 Minuten)

**Fragen:**
- [ ] Wurde das Dokument rechtzeitig erstellt (Frist noch nicht abgelaufen)?
- [ ] Enthält das Dokument selbst gesetzte Fristen an die Gegenseite?
- [ ] Sind gesetzte Fristen angemessen (nicht zu kurz, nicht zu lang)?
- [ ] Wurde Fristende in Fristenbuch eingetragen?

**Ergebnis:** Fristen korrekt → Weiter zu Stufe 3.

### Stufe 3 – Quellen-Check (10 Minuten)

**Fragen:**
- [ ] Sind alle Normzitate mit Paragrafennummer und aktuellem Gesetzesstand korrekt?
- [ ] Sind alle Rechtsprechungszitate mit Gericht, Datum, AZ und prüfbarer Quelle versehen?
- [ ] Keine BeckRS-Alleinzitate für tragende Aussagen?
- [ ] Behördenangaben (Gebühren, Fristen) live geprüft?
- [ ] Registerdaten (Marke, Patent) mit aktuellem Registerauszug bestätigt?

**Ergebnis:** Alle Quellen geprüft → Weiter zu Stufe 4.

### Stufe 4 – Materieller Check (15 Minuten)

**Fragen (je nach Dokumenttyp):**

**Abmahnung:**
- [ ] Aktivlegitimation eindeutig begründet?
- [ ] Verletzungshandlung tatbestandsmäßig subsumiert?
- [ ] Unterlassungserklärung sachlich korrekt und vollständig?
- [ ] Streitwert / Kosten korrekt?

**EV-Antrag:**
- [ ] Verfügungsanspruch mit Norm und Sachverhalt vollständig?
- [ ] Verfügungsgrund / Dringlichkeit belegt?
- [ ] Glaubhaftmachungspaket vollständig?
- [ ] Tenor nicht zu weit formuliert?

**Memo / Gutachten:**
- [ ] Gutachtenstruktur (Obersatz, Definition, Subsumtion, Ergebnis)?
- [ ] Alle relevanten Tatbestandsmerkmale geprüft?
- [ ] Keine unmarkierten Annahmen?

**Ergebnis:** Material belastbar → Weiter zu Stufe 5.

### Stufe 5 – Gegenargument-Check (10 Minuten)

Systematisch drei Gegenargumente entwickeln und prüfen:

```
Gegenargument 1: _______________
Stärke: [stark / mittel / schwach]
Antwort im Dokument vorbereitet: [Ja / Nein / Teilweise]

Gegenargument 2: _______________
Stärke: [stark / mittel / schwach]
Antwort: [Ja / Nein / Teilweise]

Gegenargument 3: _______________
Stärke: [stark / mittel / schwach]
Antwort: [Ja / Nein / Teilweise]
```

**Ergebnis:** Keine unbehandelten starken Gegenargumente → Weiter zu Stufe 6.

### Stufe 6 – Freigabe-Entscheidung

**Entscheidungskriterien:**

| Entscheidung | Kriterien |
|---|---|
| ✅ FREIGABE | Alle Stufen 1–5 ohne offene rote Punkte |
| ⚠️ FREIGABE MIT VORBEHALT | Ein oder zwei kleinere offene Punkte; nicht wesentlich für Ergebnis |
| 🚫 ZURÜCK ZUR ÜBERARBEITUNG | Wesentlicher materieller Fehler; Quellenproblem; starkes unbehandeltes Gegenargument |

**Freigabe-Protokoll:**
```
QUALITY-GATE PROTOKOLL
Dokument: _______________
Datum: _______________
Reviewer: _______________
Stufe 1 (Formal): _______________
Stufe 2 (Fristen): _______________
Stufe 3 (Quellen): _______________
Stufe 4 (Material): _______________
Stufe 5 (Gegenargument): _______________
Entscheidung: ✅ / ⚠️ / 🚫
Anmerkungen: _______________
```

## Schnell-Quality-Gate (5 Minuten, bei Zeitdruck)

Wenn keine Zeit für vollständiges Quality-Gate:

1. Tenor/Antrag/Kernaussage korrekt?
2. Frist geprüft?
3. Kritische Anlagen vorhanden?
4. Keine offensichtlichen Fehler?

Wenn alle vier Punkte grün: Notfall-Freigabe mit Vorbehalt.

## Typische Freigabe-Blocker

- Tenor zu weit formuliert (Risiko: Gericht lehnt ab oder kürzt erheblich).
- Eidesstattliche Versicherung fehlt (EV-Antrag ohne Glaubhaftmachung).
- Zustellungsnachweis fehlt (Ordnungsmittelantrag ohne Beweis des Vollzugs).
- Schutzrecht abgelaufen (Abmahnung ohne Grundlage).
- Verjährung übersehen.

## Quellenregel

- [§ 920 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/920.html) (Glaubhaftmachung EV)
- [§ 890 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/890.html) (Ordnungsmittel)
- Keine BeckRS-Blindzitate; jede Rechtsprechung live verifizierten.

## Anschluss-Skills

- `spezial-source-red-team-und-qualitaetskontrolle` – Detailliertes Red-Team
- `workflow-rechtsquellen-livecheck` – Quellenprüfung
- `spezial-klausel-beweislast-und-darlegungslast` – Beweisführung
- `workflow-output-waehlen` – Outputformat

## 3. `evvollzug-neu-001-einstweilige-verfuegung-vollziehung-frist-und`

**Fokus:** EV-Vollzug: Vollziehungsfrist § 929 Abs. 2 ZPO und Parteizustellung im gewerblichen Rechtsschutz. Beschluss- und Urteilsverfügung, Zustellwege, Vollziehungsversäumnis und Rechtsfolgen. Praxisfür Anwalt, Mandant und Vollstreckungsorgan.

# EV-Vollzug 001: Vollziehungsfrist und Parteizustellung (§ 929 Abs. 2 ZPO)

## Zweck und Mandatsbezug

Dieser Skill behandelt die **Vollziehungsfrist des § 929 Abs. 2 ZPO** und die damit verbundene **Parteizustellung** als eigenständige Vollzugshandlung bei einstweiligen Verfügungen im gewerblichen Rechtsschutz. Ohne fristgerechten Vollzug verliert die EV ihre Wirkung – ein formaler Fehler, der in der Praxis zur Aufhebung der Verfügung führt, obwohl der Antragsteller materiell im Recht lag.

Mandatsbezug: Marken-, Patent-, UWG- und Urheberrechtsfälle, in denen eine Beschlussverfügung (ohne mündliche Verhandlung) oder eine Urteilsverfügung erwirkt wurde und nun vollzogen werden muss. Der Anwalt muss Vollziehungsfrist, Zustellweg und Zustellnachweis exakt koordinieren.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 929 Abs. 2 ZPO** – Vollziehungsfrist: Der Arrestbefehl und die einstweilige Verfügung verlieren ihre Kraft, wenn die Vollziehung nicht binnen eines Monats nach Verkündung bzw. Zustellung an den Antragsteller bewirkt wird.
- **§ 922 Abs. 2 ZPO** – Zustellung der Beschlussverfügung durch den Antragsteller (Parteizustellung); Gegensatz zur Amtszustellung bei Urteilen.
- **§ 191 ZPO i.V.m. §§ 192–195 ZPO** – Parteizustellung durch Gerichtsvollzieher; Form- und Nachweisanforderungen.
- **§ 936 ZPO** – Verweisung auf Arrestvorschriften; § 929 ZPO gilt für EV entsprechend.
- **§ 945 ZPO** – Schadensersatzpflicht bei ungerechtfertigter EV (relevant für Folgefragen).

### Fristberechnung

- **Beginn:** Zeitpunkt der Zustellung des Beschlusses an den Antragsteller (nicht: Erlass); bei Urteilsverfügungen: Verkündung.
- **Ende:** Ablauf eines Monats nach § 929 Abs. 2 ZPO; Berechnung nach §§ 187, 188 BGB.
- **Hemmung:** Keine automatische Hemmung durch Widerspruch des Schuldners; Fristverlängerung nur bei Antrag auf erneuten Erlass nach Aufhebung.
- **Fristversäumnis:** Führt zu Wirkungsverlust der EV; Antragsteller muss neuen Antrag stellen.

### Vollziehungshandlungen

| Verfügungsart | Vollziehungshandlung |
|---|---|
| Beschlussverfügung (Unterlassung) | Parteizustellung an Schuldner |
| Urteilsverfügung (Unterlassung) | Amtszustellung oder Parteizustellung |
| Beschlussverfügung (Herausgabe) | Vollstreckung durch GV nach § 883 ZPO |
| Beschlussverfügung (Handlung) | Vollstreckung nach §§ 887, 888 ZPO |

## Kaltstart in 6 Fragen

1. **Verfügungsart:** Beschlussverfügung oder Urteilsverfügung? Datum des Erlasses und Datum der Zustellung an Antragsteller?
2. **Fristlauf:** Wann beginnt die Monatsfrist konkret – wurde das Dokument dem Antragsteller schon zugestellt?
3. **Vollziehungshandlung:** Welcher Inhalt der EV – Unterlassung, Herausgabe, Handlung? Zustellweg (GV, beA, Post)?
4. **Schuldneridentifikation:** Natürliche oder juristische Person? Zustellanschrift gesichert, Firmensitz bekannt?
5. **Nachweis:** Liegt Zustellnachweis (Zustellurkunde, Empfangsbekenntnis, Rückschein) bereits vor?
6. **Output:** Fristenübersicht, Checkliste Parteizustellung, Muster-Zustellauftrag an GV oder Memo an Mandanten?

## Prüfprogramm: Vollzugshandlung Schritt für Schritt

### Schritt 1 – Friststart präzise bestimmen

- Beschlussverfügung: Eingang beim Antragstelleranwalt ist der maßgebliche Zeitpunkt (BGH-Praxis).
- Urteilsverfügung: Verkündungstermin; bei Abwesenheit Antragsteller: Zustellung der schriftlichen Ausfertigung.
- Fehler: Fristlauf ab Erlass (nicht Zustellung) berechnen – dies ist falsch und führt zu unnötigem Zeitdruck.

### Schritt 2 – Zustellweg wählen

- **Gerichtsvollzieher (§ 192 ZPO):** Sicherste Methode; GV fertigt Zustellurkunde aus.
- **Postzustellung mit Zustellungsauftrag:** Möglich, aber fehleranfällig bei Adressproblemen.
- **beA:** Zulässig, wenn Schuldner anwaltlich vertreten und beA-Empfang gesichert ist.
- Praxisregel: Bei Verfügungen mit Ordnungsmitteln immer GV-Zustellung wählen.

### Schritt 3 – Ausfertigung besorgen

- Vollstreckbare Ausfertigung der EV beim Gericht beantragen (§ 724 ZPO).
- Ausfertigung muss mit Vollstreckungsklausel versehen sein.
- Kopie für eigene Akte anfertigen.

### Schritt 4 – Zustellauftrag formulieren

- Zustellauftrag an GV: vollständige Schuldneranschrift, Datum der Frist, Anweisung zur Zustellurkunde.
- Einzureichende Dokumente: vollstreckbare Ausfertigung, Antrag auf Protokollierung der Übergabe.
- Vorschuss für GV bereitstellen (§ 1 GvKostG).

### Schritt 5 – Nachweis sichern und fristen

- Zustellurkunde umgehend in Akte aufnehmen.
- Datum in Fristenbuch eintragen.
- Vorlage: Zustellurkunde bei Gericht einreichen wenn Ordnungsmittelantrag folgt.

## Typische Fallen und Fehlerquellen

- **Fristberechnung ab Erlass statt ab Zustellung** an Antragsteller – führt zu vermeintlichem Puffer, der real nicht existiert.
- **Zustellversuch an falsche Adresse:** Schuldner zieht um, Frist läuft ab; vorherige Recherche im Handelsregister oder Melderegister erforderlich.
- **Parteizustellung per Einwurf-Einschreiben ohne GV:** Zweifelhafter Nachweis; Gerichte verlangen oft GV-Zustellurkunde.
- **Keine vollstreckbare Ausfertigung:** EV kann nicht vollzogen werden; Ausfertigungsantrag vergessen.
- **Urteils- statt Beschlussverfügung:** Bei Urteilsverfügungen läuft die Amtszustellung; Parteizustellung doppelt oder überhaupt nicht nötig.
- **Nachträgliche Adresskorrektur:** Bei Aufhebung der Zustellung durch unzutreffende Adresse läuft Frist weiter.

## Output-Module

- **Fristenblatt:** Datum Erlass, Datum Zustellung Antragsteller, Fristende, Vollziehungshandlung, Nachweis-Status.
- **Checkliste Parteizustellung:** Ausfertigung, GV-Auftrag, Vorschuss, Zustellurkunde, Aktenvorlage.
- **Mustertext GV-Auftrag:** Adressblock Schuldner, AZ Gericht, Datum EV, Zustellanweisung.
- **Memo an Mandanten:** Warum Vollzug nötig, was Mandant tun muss (ggf. Kosten bereitstellen, Adresse bestätigen).

## Quellenregel

- Normen: [§ 929 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/929.html), [§ 922 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/922.html), [§ 191 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/191.html).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und prüfbarer Quelle (openjur.de, bgh.de).
- Keine BeckRS- oder Kommentar-Blindzitate aus Modellwissen.
- Bei Zweifeln zu aktueller Praxis eines bestimmten Landgerichts: Live-Check über Gerichtswebsite oder aktuelle Entscheidungsdatenbank.

## Anschluss-Skills

- `evvollzug-neu-002` – Urteilsverfügung vs. Beschlussverfügung und Zustellweg
- `evvollzug-neu-003` – Zustellung durch Gerichtsvollzieher im IP-Verfahren
- `evvollzug-neu-005` – Ordnungsmittelantrag nach erfolgreichem Vollzug
- `schutzschrift-eilverfuegung` – Schutzschrift als Gegenmittel des Schuldners

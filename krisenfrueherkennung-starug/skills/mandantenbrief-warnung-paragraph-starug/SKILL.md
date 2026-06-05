---
name: mandantenbrief-warnung-paragraph-starug
description: "Mandantenbrief Warnung Paragraph Starug: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandantenbrief Warnung Paragraph Starug

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandantenbrief Warnung Paragraph Starug** im Plugin Krisenfrüherkennung (StaRUG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mandantenbrief-warnung-paragraph-102-starug-template` | Prüffeld für mandantenbrief warnung paragraph 102 starug template: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `paragraph-1-starug-pflichten-und-24-monats-horizont` | § 1 StaRUG Krisenfrueherkenungspflicht und 24-Monats-Horizont erklären und umsetzen: GF oder Berater fragt was StaRUG konkret verlangt. Normen: § 1 StaRUG (Frueherkennungspflicht GmbH/AG), § 18 InsO (drohende ZU als StaRUG-Zugang). Prüfraster: Adressatenkreis nach Rechtsform, 24-Monats-Planungshorizont als Standard, Abgrenzung § 18 InsO, Haftungsfolgen bei Pflichtverletzung. Output § 1-StaRUG-Compliance-Memo, Umsetzungsplan Fruehwarnsystem. Abgrenzung: System-Architektur siehe fruehwarnsystem-architektur-zwei-jahres-horizont; Kennzahlen-Ampel siehe kennzahlenset-und-ampelsystem-starug-konform. |
| `paragraph-102-starug-warnpflicht-bei-rechtsberatern` | Prüffeld für paragraph 102 starug warnpflicht bei rechtsberatern: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Krisenfrüherkennung (StaRUG) gilt für **Mandantenbrief Warnung Paragraph Starug**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mandantenbrief-warnung-paragraph-102-starug-template`

**Fokus:** Prüffeld für mandantenbrief warnung paragraph 102 starug template: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Mandantenbrief-Templates — § 102-StaRUG-Warnung in drei Eskalationsstufen

§ 102 StaRUG-Warnschreiben sind kein Formular-Baukasten — sie sind juristisch relevante Dokumente, die im Haftungsfall den Unterschied zwischen Freispruch und Schadensersatz machen. Das folgende Toolkit enthält Volltext-Templates für alle drei Eskalationsstufen sowie begleitende Formulare für die Empfangsbestätigung und die Mandatsniederlegung. Counsel können diese Templates nach Sachverhaltsabstimmung direkt einsetzen.

---

## Rechtsgrundlagen

- § 102 StaRUG (Hinweis- und Warnpflicht der Berater)
- § 43 StBerG (Allgemeine Berufspflichten Steuerberater)
- § 43 WPO (Berufspflichten Wirtschaftsprüfer)
- § 43a BRAO (Grundpflichten Rechtsanwalt)
- **BGH IX ZR 285/14 vom 26.01.2017** — Steuerberater haftet bei Erstellung des Jahresabschlusses auf unaufgeforderten Hinweis bei Krisensignalen; auch bei Teilauftrag. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>
- **BGH IX ZR 56/22 vom 29.06.2023** — Drittschutz der Warnpflicht zugunsten des (faktischen) Geschäftsführers. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>
- §§ 280, 634 BGB (Haftung wegen Beratungspflichtverletzung)

---

## Pflichten

### 1. Die drei Eskalationsstufen

**Stufe 1 — Erste Warnung (präventiv):**
- Auslöser: Erste krisenrelevante Signale erkannt (BWA-Verschlechterung, Zahlungsverzögerungen)
- Ton: informierend, konstruktiv, handlungsorientiert
- Frist: mind. 14 Tage Reaktionsfrist
- Format: Brief + E-Mail mit Lesebestätigung

**Stufe 2 — Wiederholung mit Eskalation:**
- Auslöser: Keine oder unzureichende Reaktion auf Stufe 1, Verschlechterung der Lage
- Ton: eindringlich, explizit auf § 15a InsO-Risiko hinweisend
- Frist: 7 Tage Reaktionsfrist
- Format: Einschreiben mit Rückschein + E-Mail

**Stufe 3 — Mandatsniederlegung:**
- Auslöser: Keine Reaktion nach Stufe 2, offensichtliche Fahrlässigkeit des Mandanten
- Ton: klar, formal, ohne Wertung
- Format: Einschreiben mit Rückschein, sofortige Wirkung oder angemessene Übergabefrist

---

## Vorgehen

### Dokumentations-Checkliste für Berater

Für jedes § 102-StaRUG-Warnschreiben:

- [ ] Datum der Erkenntnis der Krisenzeichen protokolliert
- [ ] Stufe-1-Schreiben versendet am [Datum], per [E-Mail / Brief / Einschreiben]
- [ ] Empfangsnachweis erhalten am [Datum]
- [ ] Reaktion des Mandanten: [Beschreibung] / Keine Reaktion
- [ ] Ggf. Stufe-2-Schreiben versendet am [Datum]
- [ ] Ggf. Stufe-3-Schreiben / Mandatsniederlegung am [Datum]
- [ ] Alle Dokumente archiviert in Mandantenakte

---

## Templates

### TEMPLATE 1 — Erste Warnung (Stufe 1)

```
[Kanzlei-Briefkopf — fiktive Kanzlei]

[Ort], [Datum]

[Firma GmbH]
z.Hd. der Geschäftsführung
[Straße, PLZ Ort]

Per E-Mail (Lesebestätigung erbeten) und per Post

Betreff: Krisenfrühwarnung nach § 102 StaRUG — Handlungsempfehlung

Sehr geehrte [Damen und Herren / Frau / Herr],

im Rahmen unserer Mandatstätigkeit ([Art des Mandats: z.B. laufende
steuerliche Beratung / Jahresabschlussprüfung / gesellschaftsrechtliche
Beratung]) sind uns folgende Umstände bekannt geworden, die auf eine
bestandsgefährdende Entwicklung im Sinne des § 1 StaRUG hindeuten können:

1. FESTGESTELLTE KRISENZEICHEN

 a) [Sachverhalt 1 — konkret beschreiben]:
 Auf Basis der Betriebswirtschaftlichen Auswertung per [Datum]
 haben wir festgestellt, dass [z.B. das kumulierte EBIT im laufenden
 Geschäftsjahr EUR [Betrag] beträgt — ein Rückgang von [x Prozent]
 gegenüber dem Vorjahreszeitraum].

 b) [Sachverhalt 2 — konkret beschreiben]:
 [z.B. Offene Verbindlichkeiten gegenüber Lieferanten in Höhe von
 EUR [Betrag] sind seit mehr als sechzig Tagen überfällig.]

 c) [Ggf. Sachverhalt 3]

2. RECHTLICHE EINORDNUNG

 Wir weisen Sie darauf hin, dass die beschriebenen Umstände möglicherweise
 auf eine drohende Zahlungsunfähigkeit im Sinne des § 18 InsO hindeuten
 können. Sollte eine drohende Zahlungsunfähigkeit vorliegen, bestehen für
 Sie als Geschäftsführer gemäß § 1 StaRUG folgende Pflichten:

 - Fortlaufende Überwachung der wirtschaftlichen Lage
 - Sofortige Ergreifung geeigneter Gegenmaßnahmen
 - Unterrichtung der Gesellschafter über die Lage

 Wir weisen Sie ferner darauf hin, dass bei Eintritt der Zahlungsunfähigkeit
 (§ 17 InsO) oder Überschuldung (§ 19 InsO) eine Insolvenzantragspflicht
 nach § 15a InsO besteht. Diese Pflicht ist innerhalb von drei Wochen nach
 Kenntnis des Insolvenzgrundes zu erfüllen.

3. HANDLUNGSEMPFEHLUNGEN

 Wir empfehlen dringend:
 a) Unverzügliche Erstellung einer rollierenden Liquiditätsplanung
 für die nächsten vierundzwanzig Monate,
 b) Hinzuziehung eines auf Restrukturierung spezialisierten
 Rechtsberaters,
 c) Information der Gesellschafter und ggf. des Aufsichtsrats
 über die aktuelle Lage,
 d) Prüfung, ob die Voraussetzungen für ein Restrukturierungsverfahren
 nach dem Stabilisierungs- und Restrukturierungsrahmen (StaRUG) vorliegen.

4. REAKTION ERBETEN

 Bitte teilen Sie uns bis zum [Datum — ca. 14 Tage] mit, welche
 der vorgenannten Maßnahmen Sie einleiten werden. Bitte bestätigen
 Sie außerdem den Erhalt dieses Schreibens.

 Wir stehen für ein klärendes Gespräch jederzeit zur Verfügung.

Mit freundlichen Grüßen

[Name Berater — fiktiv]
[Kanzlei — fiktiv]

Anlage: [Relevante BWA / Offene-Posten-Liste / sonstige Grundlagen]
```

---

### TEMPLATE 2 — Wiederholung mit Eskalation (Stufe 2)

```
[Kanzlei-Briefkopf — fiktive Kanzlei]

[Ort], [Datum]

[Firma GmbH]
z.Hd. der Geschäftsführung
[Straße, PLZ Ort]

PER EINSCHREIBEN MIT RÜCKSCHEIN

Betreff: Dringende Krisenwarnung — ZWEITE MAHNUNG nach § 102 StaRUG

Bezug: Unser Schreiben vom [Datum der Stufe-1-Warnung]

Sehr geehrte [Damen und Herren / Frau / Herr],

wir beziehen uns auf unser Schreiben vom [Datum], in dem wir Sie
auf krisenrelevante Entwicklungen hingewiesen haben.

Bis heute haben wir von Ihnen keine Rückmeldung über eingeleitete
Maßnahmen erhalten [oder: Die uns mitgeteilten Maßnahmen erscheinen
angesichts der aktuellen Datenlage nicht ausreichend].

VERSCHLECHTERUNG DER LAGE:
Zwischenzeitlich haben wir folgende weitere Krisenzeichen festgestellt:
[Beschreibung der Verschlechterung seit Stufe-1-Warnung]

AUSDRÜCKLICHER HINWEIS AUF § 15a InsO:
Wir weisen Sie ausdrücklich und unmissverständlich darauf hin:

Sollte zum heutigen Zeitpunkt oder in den nächsten Wochen
Zahlungsunfähigkeit oder Überschuldung eintreten, sind Sie als
Geschäftsführer verpflichtet, innerhalb von DREI WOCHEN beim
zuständigen Insolvenzgericht einen Insolvenzantrag zu stellen
(§ 15a InsO). Die Verletzung dieser Pflicht ist strafbar
(§ 15a Abs. 4 InsO: Freiheitsstrafe bis zu drei Jahre oder Geldstrafe).

LETZTE FRIST:
Wir setzen Ihnen eine letzte Frist bis zum [Datum — 7 Tage].
Bitte teilen Sie uns bis dahin mit:
1. Welche konkreten Maßnahmen Sie eingeleitet haben,
2. Ob Sie bereits einen Restrukturierungsberater / Rechtsanwalt
 hinzugezogen haben,
3. Ob eine aktuelle Liquiditätsplanung (24 Monate) vorliegt.

Sollten wir bis zu diesem Datum keine ausreichende Rückmeldung
erhalten, sehen wir uns gezwungen, das Mandat niederzulegen.

Mit freundlichen Grüßen

[Name Berater — fiktiv]
[Kanzlei — fiktiv]
```

---

### TEMPLATE 3 — Mandatsniederlegung (Stufe 3)

```
[Kanzlei-Briefkopf — fiktive Kanzlei]

[Ort], [Datum]

[Firma GmbH]
z.Hd. der Geschäftsführung
[Straße, PLZ Ort]

PER EINSCHREIBEN MIT RÜCKSCHEIN

Betreff: Niederlegung des Mandats

Bezug: Unser Schreiben vom [Datum Stufe 1] und [Datum Stufe 2]

Sehr geehrte [Damen und Herren / Frau / Herr],

wir haben Sie mit Schreiben vom [Datum] und [Datum] wiederholt
auf bestandsgefährdende Entwicklungen hingewiesen und zur
unverzüglichen Ergreifung von Maßnahmen aufgefordert.

Da wir bis zum [Datum] keine ausreichende Rückmeldung erhalten haben
[oder: Da die ergriffenen Maßnahmen aus unserer Sicht nicht geeignet
sind, die Bestandsgefährdung zu beseitigen], sehen wir uns nicht mehr
in der Lage, das Mandat fortzuführen.

Wir legen das Mandat [sofort / mit Wirkung zum [Datum]] nieder.

Wir empfehlen Ihnen dringend, unverzüglich einen anderen Berater
hinzuzuziehen, der die laufenden Aufgaben übernehmen kann.

Wir stellen Ihnen sämtliche Mandantenunterlagen zur Verfügung.
Bitte teilen Sie uns mit, wohin wir die Unterlagen übermitteln sollen.

Die Warnhinweise aus unseren Schreiben vom [Datum] und [Datum]
bleiben in vollem Umfang bestehen.

Mit freundlichen Grüßen

[Name Berater — fiktiv]
[Kanzlei — fiktiv]

Anlage: Kopie der Schreiben vom [Datum] und [Datum]
```

---

### TEMPLATE 4 — Dokumentations-Quittung (Empfangsbestätigung Mandant)

```
EMPFANGSBESTÄTIGUNG UND REAKTIONSERKLÄRUNG
§ 102-StaRUG-Warnung vom [Datum]

Gesellschaft: [Firma GmbH]
Geschäftsführer: [Name(n)]

Wir bestätigen:

1. Das Warnschreiben der Kanzlei [fiktiv] vom [Datum] gemäß § 102 StaRUG
 ist uns am [Datum] zugegangen.

2. Wir haben den Inhalt zur Kenntnis genommen und sind uns bewusst, dass:
 - die beschriebenen Umstände auf eine bestandsgefährdende Entwicklung
 hindeuten können,
 - eine Insolvenzantragspflicht nach § 15a InsO bestehen kann,
 - unverzügliches Handeln erforderlich ist.

3. Wir werden folgende Maßnahmen einleiten:
 a) [Maßnahme 1 — mit Frist]
 b) [Maßnahme 2 — mit Frist]
 c) [Maßnahme 3 — mit Frist]

4. Wir haben folgende Berater hinzugezogen / werden hinzuziehen:
 [Name / Funktion — fiktiv], bis [Datum]

[Ort], [Datum]

_______________________________ _______________________________
[Geschäftsführer 1] [Geschäftsführer 2 — falls vorhanden]
```

---

## Fallstricke

1. **Template unreflektiert verwenden** — die Sachverhaltsangaben (Ziffern 1a, 1b, 1c in Stufe 1) müssen mit konkreten, verifizierten Zahlen aus dem Mandat befüllt werden. Ein allgemein gehaltenes Schreiben ohne Sachverhaltssubstanz ist wertlos.

2. **Empfangsbestätigung nicht einholen** — ohne Nachweis des Zugangs besteht kein Beweis für die Erfüllung der § 102-StaRUG-Pflicht.

3. **Zu frühes Mandatsniederlegung** — Mandatsniederlegung ohne vorherige Warnung (Stufen 1 und 2) schützt den Berater nicht. Die Haftung für den bereits eingetretenen Schaden bleibt.

4. **Zu späte Mandatsniederlegung** — wer das Mandat fortführt, obwohl der Mandant offensichtlich nicht reagiert, haftet für den danach eintretenden Schaden mit.

5. **Keine Kopie in der Akte** — jedes versendete Schreiben muss mit Datum, Versandart und ggf. Lesebestätigung in der Mandantenakte dokumentiert sein.

---

## Querverweise

- → `paragraph-102-starug-warnpflicht-bei-rechtsberatern` — rechtliche Grundlagen der Warnpflicht
- → `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` — Protokollierung auf Mandantenseite
- → `paragraph-1-starug-pflichten-und-24-monats-horizont` — Früherkennungspflicht der GF
- → `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` — § 15a InsO-Hinweis im Template
- → `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` — GF-Haftungsfolgen


## Weitere Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 285/14 vom 26.01.2017** — Hinweis- und Warnpflicht des Steuerberaters bei Krisensignalen.
- **BGH IX ZR 56/22 vom 29.06.2023** — Drittschutzwirkung zugunsten faktischer Geschäftsführer.
- Aktuelle Urteile zur Berater-Haftung (Steuerberater, WP, RA) vor Ausgabe über dejure.org / openjur.de mit Datum und Aktenzeichen verifizieren.

## 2. `paragraph-1-starug-pflichten-und-24-monats-horizont`

**Fokus:** § 1 StaRUG Krisenfrueherkenungspflicht und 24-Monats-Horizont erklären und umsetzen: GF oder Berater fragt was StaRUG konkret verlangt. Normen: § 1 StaRUG (Frueherkennungspflicht GmbH/AG), § 18 InsO (drohende ZU als StaRUG-Zugang). Prüfraster: Adressatenkreis nach Rechtsform, 24-Monats-Planungshorizont als Standard, Abgrenzung § 18 InsO, Haftungsfolgen bei Pflichtverletzung. Output § 1-StaRUG-Compliance-Memo, Umsetzungsplan Fruehwarnsystem. Abgrenzung: System-Architektur siehe fruehwarnsystem-architektur-zwei-jahres-horizont; Kennzahlen-Ampel siehe kennzahlenset-und-ampelsystem-starug-konform.

# § 1 StaRUG — Krisenfrüherkennungspflicht und 24-Monats-Horizont

Krisenfrüherkennung ist keine betriebswirtschaftliche Kür, sondern gesetzliche Pflicht. § 1 StaRUG kodifiziert seit dem 1. Januar 2021 eine eigenständige, von der Insolvenzordnung unabhängige Früherkennungspflicht für alle haftungsbeschränkten Rechtsträger. Wer die Datenlage nicht im Griff hat, verliert das Heft des Handelns — und mit ihm den Zugriff auf moderne Sanierungswerkzeuge, die das Gesetz nur demjenigen öffnet, der rechtzeitig handelt.

---

## Rechtsgrundlagen

- § 1 StaRUG (Stabilisierungs- und Restrukturierungsrahmen für Unternehmen)
- § 18 InsO (drohende Zahlungsunfähigkeit)
- § 17 InsO (eingetretene Zahlungsunfähigkeit)
- § 19 InsO (Überschuldung)
- § 43 GmbHG (Sorgfaltspflicht und Verantwortlichkeit der Geschäftsführer)
- § 93 AktG (Sorgfaltspflicht und Verantwortlichkeit der Vorstandsmitglieder)
- IDW PS 340 n.F. (Anforderungen an Risikofrüherkennungssysteme)
- IDW S 6 (Anforderungen an Sanierungskonzepte)

---

## Pflichten

### 1. Normadressaten nach Rechtsform

§ 1 StaRUG richtet sich an "die Mitglieder des zur Geschäftsführung berufenen Organs einer juristischen Person" sowie an Personen, die bei einer Gesellschaft ohne Rechtspersönlichkeit die Vertretung ausüben. Im Einzelnen:

| Rechtsform | Normadressaten |
|---|---|
| GmbH | Geschäftsführer (§ 43 GmbHG) |
| AG / KGaA | Vorstandsmitglieder (§ 93 AktG) |
| GmbH & Co. KG | Geschäftsführer der Komplementär-GmbH |
| eG (Genossenschaft) | Vorstand |
| Rechtsfähiger Verein | Vorstand (§ 26 BGB) |
| UG (haftungsbeschränkt) | Geschäftsführer |

Einzelkaufleute und Personengesellschaften ohne Haftungsbeschränkung sind vom Wortlaut des § 1 StaRUG nicht erfasst, unterliegen aber wirtschaftlich denselben Sorgfaltspflichten aus Deliktsrecht und allgemeinem Handelsrecht.

### 2. Inhalt der Früherkennungspflicht

§ 1 Abs. 1 StaRUG verlangt:

1. **Fortlaufende Überwachung** der wirtschaftlichen Lage des Unternehmens
2. **Rechtzeitige Ergreifung** geeigneter Gegenmaßnahmen bei erkannten bestandsgefährdenden Entwicklungen
3. **Unterrichtung** der Gesellschafter bzw. des Aufsichtsrats bei erkannter bestandsgefährdender Entwicklung

"Bestandsgefährdend" im Sinne des § 1 StaRUG ist weiter zu verstehen als der Insolvenzbegriff — es geht nicht erst um die drohende Zahlungsunfähigkeit, sondern um jede Entwicklung, die den Fortbestand des Unternehmens gefährden kann.

### 3. Der 24-Monats-Planungshorizont als gesetzlicher Standard

Der 24-Monats-Horizont ergibt sich systematisch aus dem Zusammenspiel mehrerer Normen:

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 29 Abs. 2 StaRUG** setzt für die Antragsstellung auf Eröffnung des Restrukturierungsverfahrens voraus, dass drohende Zahlungsunfähigkeit noch nicht eingetreten ist — der Zugang zum StaRUG-Verfahren erfordert also zwingend eine belastbare 24-Monats-Sicht.
- **IDW S 11** und **IDW S 6** verankern den 24-Monats-Horizont in der Praxis der Sanierungsberatung.

Ein Unternehmen, das keinen validierten Liquiditätsplan mit 24 Monaten Reichweite vorhält, kann im Ernstfall weder den Zugang zu StaRUG nachweisen noch den Vorwurf der Verletzung von § 1 StaRUG entkräften.

---

## Vorgehen

### Schritt 1: Standortbestimmung — Welche Pflichten gelten konkret?

Checkliste für jede Gesellschaft:

- [ ] Liegt eine haftungsbeschränkte Rechtsform vor? → Wenn ja: § 1 StaRUG anwendbar
- [ ] Existiert ein formales Risikoüberwachungssystem (IDW PS 340 n.F.)?
- [ ] Wird eine rollierende Liquiditätsplanung mit Horizont ≥ 24 Monate erstellt?
- [ ] Sind Eskalationsschwellen und Berichtspflichten an GF/AR dokumentiert?
- [ ] Werden Abweichungsanalysen systematisch durchgeführt und protokolliert?

### Schritt 2: 24-Monats-Planung implementieren

Die Planung muss folgende Elemente umfassen:

1. **GuV-Planung** (monatlich, auf Basis realistischer Szenarien)
2. **Bilanzplanung** (quartalsweise, mit Working-Capital-Modellierung)
3. **Liquiditätsplanung** (Wochen 1-13 wöchentlich; Monat 14-24 monatlich)
4. **Integrierte Plan-Ist-Abweichungsanalyse** mit Kommentierung
5. **Stresstest-Szenarien** (Base / Bear / Distress)

### Schritt 3: Eskalationsmatrix festlegen

| Indikator | Schwelle Gelb | Schwelle Rot | Eskalation |
|---|---|---|---|
| Liquiditätsreichweite | < 6 Monate | < 3 Monate | GF-Runde / AR |
| EBITDA-Coverage | < 1,5x | < 1,0x | Gesellschafterinfo |
| Covenant-Headroom | < 20 % | < 10 % | Bankgespräch |
| Net-Debt/EBITDA | > 4,0x | > 5,5x | GF-Sofortmaßnahmen |

### Schritt 4: Dokumentation und Protokollierung

Jede Erkennung einer bestandsgefährdenden Entwicklung muss unverzüglich protokolliert werden. Ohne Dokumentation kein Beweis — ohne Beweis keine Haftungsfreistellung.

---

## Templates

### Muster: Beschlussprotokoll Geschäftsführersitzung — Ersteinführung Frühwarnsystem

```
Gesellschaft: [Firma GmbH]
Sitzung: Geschäftsführerbesprechung
Datum: [TT.MM.JJJJ]
Anwesend: [Name GF 1], [Name GF 2]

TOP 1: Einführung Krisenfrüherkennungssystem gemäß § 1 StaRUG

Die Geschäftsführung beschließt:

1. Mit Wirkung zum [Datum] wird ein Krisenfrüherkennungssystem nach
 Maßgabe des § 1 StaRUG und IDW PS 340 n.F. eingeführt.
2. Die rollierende Liquiditätsplanung wird auf einen Horizont von
 24 Monaten ausgeweitet (Wochen 1-13 wöchentlich; M14-M24 monatlich).
3. Zuständig für die Pflege und Vorlage: [Name].
4. Reportingzyklus: monatlich an die Geschäftsführung; quartalsweise
 an den Gesellschafter/Aufsichtsrat.
5. Eskalationsschwellen: siehe beigefügte KPI-Ampeltabelle (Anlage 1).

Festgestellt: [Ort], [Datum]
Unterschriften: _________________ / _________________
```

### Muster: 24-Monats-Horizont — Prüfungsfragen für das Beratungsgespräch

```
1. Liegt für die nächsten 24 Monate eine integrierte Unternehmensplanung
 (GuV / Bilanz / Cashflow) vor?
2. Enthält die Liquiditätsplanung wöchentliche Granularität für
 die ersten 13 Wochen?
3. Sind mindestens zwei Stresstest-Szenarien dokumentiert?
4. Wurden die Planprämissen von der Geschäftsführung formal freigegeben?
5. Gibt es eine Plan-Ist-Abweichungsanalyse des Vormonats?
6. Ist dokumentiert, wann und an wen eskaliert wird?
```

---

## Fallstricke

1. **"Wir machen das immer schon so"** ist kein Nachweis für § 1 StaRUG-Compliance — gefordert ist eine formale, dokumentierte Struktur, keine informelle Routine.

2. **Der 24-Monats-Horizont gilt für die Liquiditätsplanung, nicht nur für die GuV** — eine reine Ergebnisplanung ohne Cashflow-Modell erfüllt die Pflicht nicht.

3. **Kein Zugriffsrecht auf StaRUG ohne rechtzeitigen Nachweis drohender Zahlungsunfähigkeit** — wer zu spät kommt, steht mit § 15a InsO (Insolvenzantragspflicht) vor der Tür, nicht mit § 29 StaRUG.

4. **Passive Überwachung reicht nicht** — § 1 Abs. 1 StaRUG verlangt aktives Gegensteuern. Wer erkennt und nicht handelt, haftet nach § 43 GmbHG / § 93 AktG.

5. **Fehlende Unterrichtung der Gesellschafter** ist eine eigenständige Pflichtverletzung — selbst wenn die GF intern gegengesteuert hat, muss die vorgeschriebene Informationskette eingehalten werden.

6. **Outsourcing schützt nicht** — auch wenn die Buchhaltung oder Planung extern liegt, bleibt die Überwachungspflicht bei der Geschäftsführung. Delegation verringert, aber eliminiert die Haftung nicht.

---

## Querverweise

- → `fruehwarnsystem-architektur-zwei-jahres-horizont` — technische Architektur des Frühwarnsystems
- → `rollierende-liquiditaetsplanung-24-monate-template` — konkrete Planungsstruktur
- → `kennzahlenset-und-ampelsystem-starug-konform` — KPI-Set und Schwellenwerte
- → `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` — Haftungsfolgen
- → `drohende-zahlungsunfaehigkeit-paragraph-18-inso` — Abgrenzung § 18 InsO
- → `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` — Protokollführung


## Weitere Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3. `paragraph-102-starug-warnpflicht-bei-rechtsberatern`

**Fokus:** Prüffeld für paragraph 102 starug warnpflicht bei rechtsberatern: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# § 102 StaRUG — Warnpflicht der Rechtsberater

§ 102 StaRUG begründet eine gesetzlich normierte Hinweispflicht für Steuerberater, Wirtschaftsprüfer und Rechtsanwälte bei drohender Insolvenz ihrer Mandanten. Diese Pflicht ist keine Kulanzleistung, sondern ein scharfes Haftungsschwert — in beide Richtungen: Wer warnt und dokumentiert, ist geschützt. Wer schweigt, haftet.

---

## Rechtsgrundlagen

- § 102 StaRUG (Hinweispflichten der Berater)
- § 43 StBerG (Allgemeine Berufspflichten des Steuerberaters)
- § 43 WPO (Berufspflichten des Wirtschaftsprüfers)
- § 43a BRAO (Grundpflichten des Rechtsanwalts)
- **BGH IX ZR 285/14 vom 26.01.2017** — Grundsatzentscheidung zur Hinweis- und Warnpflicht des Steuerberaters bei drohender Insolvenz; Steuerberater haftet auf den durch die unterlassene Warnung verursachten Insolvenzvertiefungsschaden.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>
- **BGH IX ZR 56/22 vom 29.06.2023** — Drittschutzwirkung der Hinweis- und Warnpflicht zugunsten des (faktischen) Geschäftsführers; der GF kann eigenen Schadensersatzanspruch gegen Berater haben, wenn er bestimmungsgemäß in den Schutzbereich des Mandatsvertrags einbezogen ist.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>
- IDW PS 340 n.F. (Risikofrüherkennungssysteme)

---

## Pflichten

### 1. Norminhalt § 102 StaRUG

§ 102 Abs. 1 StaRUG verpflichtet jeden Berater, der aufgrund seiner beruflichen Tätigkeit Umstände erkennt, die auf eine drohende Zahlungsunfähigkeit oder Überschuldung hindeuten, seinen Mandanten unverzüglich darauf hinzuweisen. Die Hinweispflicht gilt:

- **Steuerberater** bei Jahresabschluss-Erstellung, laufender Finanzbuchhaltung, Lohnbuchhaltung, Betriebswirtschaftlichen Auswertungen (BWA)
- **Wirtschaftsprüfer** bei Jahresabschlussprüfung, Sonderprüfungen, Due Diligence
- **Rechtsanwälte** bei gesellschaftsrechtlicher Beratung, Vertragsgestaltung, Inkasso, Vertragsverhandlungen

### 2. Auslöser der Warnpflicht

Die Warnpflicht wird ausgelöst, sobald der Berater Anhaltspunkte erkennt — nicht erst bei Gewissheit. Zu den typischen Auslösern gehören:

| Signal | Typischer Kontext |
|---|---|
| BWA zeigt nachhaltiges Umsatzminus | Steuerberater im Rahmen der Monatsbuchhaltung |
| Zahlungsverzögerungen gegenüber Lieferanten > 60 Tage | Inkassobeauftragter RA |
| Covenant-Unterschreitung im Kreditvertrag | WP bei der Jahresabschlussprüfung |
| Negativer Eigenkapital-Trend | StB bei Bilanzierungsgespräch |
| Forderungsausfälle > 15 % des Umsatzes | Jeder Berater, dem dies bekannt wird |

### 3. Inhalt der Warnung

Die Warnung muss konkret, verständlich und nachweisbar sein. Bloßer Hinweis in einer Besprechung ohne Niederschrift genügt nicht. Die Warnung muss enthalten:

1. **Sachverhaltsbeschreibung** — welche Umstände wurden erkannt?
2. **Rechtliche Einordnung** — was bedeutet das im Hinblick auf drohende Zahlungsunfähigkeit/Überschuldung?
3. **Handlungsempfehlungen** — welche Sofortmaßnahmen sind zu prüfen?
4. **Fristsetzung** — bis wann erwartet der Berater Rückmeldung?
5. **Hinweis auf Insolvenzantragspflicht** — § 15a InsO und Drei-Wochen-Frist benennen

**BGH IX ZR 285/14 vom 26.01.2017** ist die Grundsatzentscheidung zur Hinweis- und Warnpflicht des Steuerberaters bei möglicher Insolvenzreife: Ein Steuerberater, der bei der Erstellung des Jahresabschlusses auf Anzeichen einer Unternehmenskrise stößt, ist verpflichtet, den Mandanten unaufgefordert auf das Risiko einer Insolvenzantragspflicht hinzuweisen. Diese Pflicht besteht auch bei Teilauftrag. Der Schutzbereich des Beratungsvertrags umfasst den wirtschaftlichen Gesamtschaden des Mandanten.

Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>

**BGH IX ZR 56/22 vom 29.06.2023** erweitert die Schutzwirkung des Beratungsmandats: Auch der (faktische) Geschäftsführer kann in den Schutzbereich einbezogen sein, wenn er bestimmungsgemäß mit der Hauptleistung in Berührung kommt — d.h. der Berater haftet ggf. auch dem GF persönlich auf Ersatz seines Insolvenzvertiefungsschadens (insb. Haftung nach § 15b InsO, § 823 II BGB iVm § 15a InsO).

Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>

**Praktische Konsequenz:** Kein Berater kann sich auf den Umfang seines Mandats zurückziehen, wenn er krisensignifikante Informationen in der Hand hält. Die Warnung gehört zum Mindestinhalt jedes Beratungsverhältnisses.

---

## Vorgehen

### Schritt 1: Checkliste Auslöser-Erkennung

Monatliche Prüfung durch den Berater anhand der BWA:

- [ ] Ist die Eigenkapitalquote unter 10 % gesunken?
- [ ] Ist EBIT/EBITDA seit drei Monaten negativ?
- [ ] Bestehen Zahlungsverzögerungen an das Finanzamt oder Sozialversicherungsträger?
- [ ] Wurden Kreditlinien vollständig ausgeschöpft?
- [ ] Gibt es Klagen, Vollstreckungsmaßnahmen oder Pfändungen?
- [ ] Hat der Mandant Lieferantenrechnungen > 60 Tage offen?
- [ ] Wurde die Bank über Covenant-Unterschreitungen informiert?

Wenn mehr als zwei dieser Fragen mit "ja" beantwortet werden: Warnpflicht ist ausgelöst.

### Schritt 2: Warnung aussprechen und dokumentieren

1. Gespräch mit Mandant führen (persönlich oder Videocall, protokolliert)
2. Schriftliche Bestätigung per Brief oder E-Mail (Muster s.u.)
3. Empfangsbestätigung einholen (Lesebestätigung, Antwort-E-Mail, Unterschrift)
4. Akte anlegen: Datum der Erkenntnis, Datum der Warnung, Reaktion des Mandanten

### Schritt 3: Eskalation bei Untätigkeit des Mandanten

Reagiert der Mandant nicht innerhalb der gesetzten Frist (i.d.R. zwei Wochen), folgt:

1. Schriftliche Wiederholung der Warnung mit Fristmahnung
2. Prüfung der Mandatsfortführungspflicht — ggf. Mandatsniederlegung
3. Dokumentation der Mandatsniederlegung aus Haftungsgründen

---

## Templates

### Muster: § 102-StaRUG-Warnbrief (Steuerberater an Mandant)

```
[Kanzlei-Briefkopf — fiktive Kanzlei]

[Ort], [Datum]

[Firma GmbH]
z.Hd. der Geschäftsführung
[Adresse]

Betreff: Krisenfrühwarnung gemäß § 102 StaRUG — Dringende Handlungsempfehlung

Sehr geehrte Damen und Herren,

im Rahmen unserer laufenden Mandatstätigkeit haben wir folgende
Entwicklungen festgestellt, die auf eine bestandsgefährdende Lage
im Sinne des § 1 StaRUG und auf das Vorliegen von Umständen
hindeuten können, die zu einer drohenden Zahlungsunfähigkeit
im Sinne des § 18 InsO führen könnten:

1. [Beschreibung Sachverhalt 1, z.B.: Die BWA per [Datum] weist
 ein kumuliertes EBIT von EUR [Betrag] aus — gegenüber dem
 Vorjahreswert von EUR [Betrag] entspricht dies einem Rückgang
 von [x] Prozent.]

2. [Beschreibung Sachverhalt 2, z.B.: Die offenen Verbindlichkeiten
 gegenüber Lieferanten betragen zum Stichtag EUR [Betrag], davon
 sind EUR [Betrag] seit mehr als 60 Tagen überfällig.]

3. [Beschreibung Sachverhalt 3]

Wir weisen Sie ausdrücklich darauf hin, dass bei Vorliegen von
Zahlungsunfähigkeit (§ 17 InsO) oder Überschuldung (§ 19 InsO)
eine Insolvenzantragspflicht nach § 15a InsO besteht, die
grundsätzlich innerhalb von drei Wochen zu erfüllen ist.

Wir empfehlen dringend, unverzüglich:
a) eine rollierende Liquiditätsplanung für die nächsten 24 Monate
 zu erstellen,
b) einen auf Restrukturierung spezialisierten Rechtsberater
 hinzuzuziehen,
c) die Gesellschafter über die aktuelle Lage zu informieren.

Bitte bestätigen Sie den Erhalt dieses Schreibens und teilen Sie
uns bis zum [Datum, ca. 14 Tage] mit, welche Maßnahmen Sie
einleiten.

Mit freundlichen Grüßen

[Name Steuerberater]
[Kanzlei — fiktiv]

Anlage: Aktuelle BWA, Offene-Posten-Liste
```

### Muster: Dokumentations-Quittung (Empfangsbestätigung Mandant)

```
Empfangsbestätigung

Ich/Wir bestätigen, das Warnschreiben der Kanzlei [fiktiv] vom
[Datum] gemäß § 102 StaRUG erhalten und zur Kenntnis genommen
zu haben.

Ich/Wir sind informiert worden, dass:
- die beschriebenen wirtschaftlichen Kennzahlen auf eine
 bestandsgefährdende Entwicklung hindeuten können,
- eine Insolvenzantragspflicht nach § 15a InsO bestehen kann,
- unverzügliches Handeln erforderlich ist.

Wir werden bis zum [Datum] folgende Maßnahmen einleiten:
[___________________________________________________]

[Ort], [Datum]

___________________________
Unterschrift Geschäftsführer
```

---

## Fallstricke

1. **Mündliche Warnung ohne Protokoll ist wertlos** — im Haftungsprozess muss der Berater beweisen, wann er gewarnt hat. Ohne Schriftlichkeit kein Beweis.

2. **"Vertrauliche" Warnung in der BWA-Erläuterung reicht nicht** — die Warnung muss explizit, unmissverständlich und dem Mandanten formal zugegangen sein.

3. **Mandatsniederlegung ohne Warnung schützt nicht** — wer das Mandat niederlegt, ohne vorher zu warnen, haftet für den während der Mandatszeit entstandenen Schaden.

4. **Berater-Eigeninteresse schützt nicht** — auch wenn der Berater befürchtet, den Mandanten zu verlieren: die Warnpflicht geht vor. Wer aus wirtschaftlichem Eigeninteresse schweigt, riskiert nach §§ 280, 634 BGB die volle Haftung.

5. **Die Warnung muss an den richtigen Empfänger gehen** — bei der GmbH ist das die Geschäftsführung, nicht nur den Buchhalter. Bei der AG: der Vorstand.

6. **Zeitdruck beachten** — zwischen Erkenntnis und Warnung darf keine unangemessene Zeit verstreichen. "Unverzüglich" bedeutet in der Praxis: innerhalb einer Woche nach Erkenntnis.

---

## Querverweise

- → `paragraph-1-starug-pflichten-und-24-monats-horizont` — Früherkennungspflicht der Geschäftsführung
- → `mandantenbrief-warnung-paragraph-102-starug-template` — ausführliche Briefvorlagen
- → `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` — Protokollierungspflichten
- → `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` — Dreiwochen-Frist
- → `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` — GF-Haftung


## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

---
name: mahnschreiben-entwurf-anwaltsgeheimnis
description: "Mahnschreiben Entwurf Anwaltsgeheimnis: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mahnschreiben Entwurf Anwaltsgeheimnis

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mahnschreiben Entwurf Anwaltsgeheimnis** im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mahnschreiben-entwurf` | Vorgerichtliches Mahnschreiben entwerfen: Zahlungsaufforderung mit Frist und Klageankündigung. Normen: §§ 286 288 BGB, §§ 204 ff. BGB. Prüfraster: Verjaebrungshemmung, Verzugsbeginn, Schadensersatz, Klageandrohung. Output: Mahnschreiben-Entwurf mit Fristsetzung. Abgrenzung: nicht Mahnbescheid (gerichtliches Verfahren). |
| `anwaltsgeheimnis-pruefung` | Anwaltsgeheimnis und Verschwiegenheitspflicht bei Weitergabe von Mandatsinformationen prüfen. Normen: § 43a BRAO, § 203 StGB, § 102 ZPO. Prüfraster: Offenbarungsbefugnis, Zeugnisverweigerungsrecht, strafrechtliche Grenzen. Output: Prüfergebnis Anwaltsgeheimnis mit Handlungsempfehlung. Abgrenzung: nicht Datenschutz-Compliance DSGVO. |
| `argumentationsverbesserung-red-team` | Verbessert prozessuale Argumentation in Klage, Erwiderung, Replik, Berufung, Eilantrag oder Mandatsmemo. Prueft These, Beweis, Subsumtion, Gegenargumente, Richterperspektive, Antragsfassung und Ton. |

## Arbeitsweg

Im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG) gilt für **Mahnschreiben Entwurf Anwaltsgeheimnis**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mahnschreiben-entwurf`

**Fokus:** Vorgerichtliches Mahnschreiben entwerfen: Zahlungsaufforderung mit Frist und Klageankündigung. Normen: §§ 286 288 BGB, §§ 204 ff. BGB. Prüfraster: Verjaebrungshemmung, Verzugsbeginn, Schadensersatz, Klageandrohung. Output: Mahnschreiben-Entwurf mit Fristsetzung. Abgrenzung: nicht Mahnbescheid (gerichtliches Verfahren).

# Mahnschreiben / Vorgerichtliche Aufforderung

## Zweck

Entwurf eines anwaltlichen Mahnschreibens (§ 286 Abs. 1 BGB) oder einer qualifizierten vorgerichtlichen Aufforderung mit Fristsetzung. Einsetzbar für Zahlungsverzug, Pflichtverletzungen, Mängelrügen (§ 281 Abs. 1 BGB) und Unterlassungsaufforderungen (§ 8 Abs. 1 UWG, § 97 Abs. 1 UrhG, § 14 Abs. 5 MarkenG). Das Schreiben ist anwaltlich unterzeichnet und nach § 13 RVG abrechenbar.

## Eingaben

- Abgeschlossenes `mahnschreiben-aufnahme.md` im Mandatsordner (Slug)
- Gewünschter Schriftsatztyp: `--zahlungsverzug`, `--mängelrüge`, `--unterlassung`, `--schadensersatz`
- Optional: `--version=N` für Versionierung bei Überarbeitungen
- Optional: `--skip-gate` – Pflicht-Checkliste überspringen (nur mit expliziter Bestätigung)

## Ablauf

1. **Intake laden:** `demand-letters/[slug]/intake.md` einlesen. Fehlende Pflichtfelder als Fehler ausgeben; kein Entwurf ohne vollständigen Intake.

2. **Pflicht-Checkliste (Gate) – vor dem Entwurf:**
 - [ ] Ist die Forderung dem Grunde nach schlüssig dargetan (§ 286 Abs. 1 BGB)?
 - [ ] Ist der Schuldner eindeutig identifiziert (Name, Anschrift, ggf. Handelsregisternummer)?
 - [ ] Ist der Betrag oder die geschuldete Handlung konkret bezeichnet?
 - [ ] Ist die Frist angemessen (i. d. R. 2 Wochen; bei Baurecht oder komplexen Leistungen ggf. länger)?
 - [ ] Sind Verzugsschäden (§ 288 BGB: 5 % über Basiszinssatz bei Verbrauchern; 9 % bei Unternehmen) korrekt beziffert?
 - [ ] Droht ein Güteantrag (§ 15a EGZPO) in bestimmten Bundesländern vor Klageerhebung?
 - [ ] Mandatsgeheimnis: Enthält das Schreiben keine vertraulichen Informationen Dritter?
 - [ ] FRE-408-Äquivalent (DE): § 278 Abs. 6 ZPO; Vergleichsangebote im Schreiben als solche kennzeichnen.

3. **Schreiben entwerfen:**
 - Briefkopf: Kanzlei, Datum, Aktenzeichen
 - Betreff: Mandant ./. Schuldner – [Kurzbezeichnung des Anspruchs]
 - Einleitung: Mandat und Vertretung
 - Sachverhalt: Knapp, tatsächlich, ohne rechtliche Wertungen
 - Forderung: Betrag / Handlung / Unterlassung, Rechtsgrundlage
 - Fristsetzung: Konkretes Datum (nicht "binnen 14 Tagen", sondern "bis zum [TT.MM.JJJJ]")
 - Konsequenzen: Klageandrohung, Kostenfolge (§§ 91 ZPO, 93 ZPO bei Anerkenntnisklage beachten)
 - Grußformel, Unterschrift

4. **Post-Send-Checkliste:**
 - Zugangsdokumentation (Einschreiben / Fax / gerichtliche Zustellung) planen
 - Frist in Kanzleifristbuch eintragen
 - Mandats-History-Update (`/mandat-update [slug] Mahnschreiben versandt`)

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung zu Verzug und Mahnung vor Ausgabe ueber https://dejure.org und https://openjur.de verifizieren.
- Zum Verzugszins: § 247 BGB (Basiszinssatz); § 288 Abs. 1, 2 BGB. Basiszinssatz zum 01.01.2026: 1,27 Prozent (unveraendert ggue. 01.07.2025). Daraus B2C-Verzugszins 6,27 Prozent, B2B-Verzugszins 10,27 Prozent; halbjaehrliche Anpassung am 01.01. und 01.07. erforderlich. Quelle: https://www.bundesbank.de/de/presse/pressenotizen/bekanntgabe-des-basiszinssatzes-zum-1-januar-2026-basiszinssatz-bleibt-unveraendert-bei-1-27--973974
- Verzugspauschale § 288 Abs. 5 BGB (B2B): 40 EUR pro Vorgang.

## Ausgabeformat

```
[KANZLEI-BRIEFKOPF]

An: [Name und Anschrift Schuldner]
Datum: TT.MM.JJJJ
Aktenzeichen: [Kanzleiaktenzeichen]
Mandatsgeheimnis – § 43a Abs. 2 BRAO / § 203 StGB

Betreff: [Mandant] ./. [Schuldner] – Zahlungsaufforderung / Aufforderung zur Mängelbeseitigung

Sehr geehrte Damen und Herren,

wir vertreten [Mandant] und nehmen wie folgt Stellung:

I. Sachverhalt
...

II. Forderung
Wir fordern Sie auf, den Betrag von EUR [X.XXX,XX] bis spätestens zum [TT.MM.JJJJ] auf unser Anderkonto zu überweisen.

III. Hinweis auf Klage
Sollte die Zahlung nicht fristgerecht eingehen, sind wir angewiesen, unverzüglich Klage zu erheben und die uns entstehenden Kosten nach §§ 91, 788 ZPO gegen Sie geltend zu machen.

Mit freundlichen Grüßen
[Anwalt, Kanzlei]
```

Ausgabe als Markdown-Datei `demand-letters/[slug]/v[N].md`.

## Risiken / typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 93 ZPO (sofortiges Anerkenntnis):** Wird der Schuldner sofort klaglos, trägt der Kläger die Kosten; Mahnschreiben vorher immer prüfen, ob es bereits eine wirksame Mahnung gab.
- **Unterlassung ohne Abmahnung:** Im UWG/UrhG/MarkenG ist die Abmahnung (mit Unterlassungsaufforderung und Vertragsstrafe) zwingende Voraussetzung; ohne Abmahnung keine Kostenerstattung (§ 97a Abs. 1 UrhG).
- **Güteantrag-Pflicht (§ 15a EGZPO):** In Bayern, Brandenburg, NRW und weiteren Ländern ist bei bestimmten Streitwerten ein Güteantrag vor Klageerhebung vorgeschrieben.
- **Fristberechnung:** Fristende nicht auf Sonn- oder Feiertag setzen (§ 193 BGB).

## 2. `anwaltsgeheimnis-pruefung`

**Fokus:** Anwaltsgeheimnis und Verschwiegenheitspflicht bei Weitergabe von Mandatsinformationen prüfen. Normen: § 43a BRAO, § 203 StGB, § 102 ZPO. Prüfraster: Offenbarungsbefugnis, Zeugnisverweigerungsrecht, strafrechtliche Grenzen. Output: Prüfergebnis Anwaltsgeheimnis mit Handlungsempfehlung. Abgrenzung: nicht Datenschutz-Compliance DSGVO.

# Vertraulichkeitsschutz-Erstprüfung (Vorlagepflicht und Verschwiegenheit)

## Zweck

Ein Dokumentensatz im Prozess hat drei Arten von Einträgen: zweifelsfrei geschützt, zweifelsfrei nicht geschützt und die Fälle, die juristisches Urteilsvermögen erfordern. Dieser Skill sortiert die ersten beiden Kategorien, damit die Anwaltszeit vollständig für die dritte zur Verfügung steht.

**Dies ist eine Erstprüfung. Der Anwalt prüft jeden markierten Eintrag. Keine Ausnahmen.**

Hinweis: Ein direktes Pendant zum US-amerikanischen "privilege log" gibt es im deutschen Recht nicht. Dieser Skill deckt die deutschen Rechtsinstitute ab, die vergleichbare Schutzfunktionen erfüllen: Vorlagepflicht nach § 142 ZPO, Beschlagnahmeschutz nach § 97 StPO, Zeugnisverweigerungsrecht nach § 53 StPO und die anwaltliche Verschwiegenheitspflicht nach § 43a Abs. 2 BRAO, § 203 StGB.

## Eingaben

- **Dokumentenbestand** (erforderlich): Dateipfad oder im Dialog übermittelte Dokumentenliste
- **Mandatsbezeichnung (Slug)**: Zur Zuordnung in die Mandatsakte
- **Verfahrensart**: ZPO-Verfahren, StPO-Verfahren, VwGO, FGO, SGG — maßgeblich für die anwendbaren Normen
- **Kontext**: Wurde eine Urkundenvorlageanordnung nach § 142 ZPO erlassen? Liegt eine Durchsuchungs-/Beschlagnahmemaßnahme vor?

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 142 ZPO** — Anordnung der Urkundenvorlegung durch das Gericht; Voraussetzungen: erheblich und zumutbar; kein Zwang zur Vorlage, wenn Verweigerungsrecht besteht.
- **§ 144 ZPO** — Anordnung der Inaugenscheinnahme; parallele Schranken wie § 142 ZPO.
- **§ 97 StPO** — Beschlagnahmeverbote; insbesondere Abs. 1 Nr. 1: Schriftstücke des Rechtsanwalts, die Zeugnisverweigerungsberechtigten gehören; Abs. 2: Schutz von Dokumenten im Gewahrsam des Verteidigers oder Beistands.
- **§ 53 StPO** — Zeugnisverweigerungsrecht der Rechtsanwälte, Ärzte, Notare und sonstiger Berufsgeheimnisträger; gilt auch im Verfahren auf Vorlage.
- **§ 53a StPO** — Erstreckt das Zeugnisverweigerungsrecht auf berufsmäßig tätige Gehilfen.
- **§ 43a Abs. 2 BRAO** — Absolute Verschwiegenheitspflicht des Rechtsanwalts; schützt alle Informationen, die der Anwalt in Ausübung des Berufs anvertraut bekommt.
- **§ 203 Abs. 1 Nr. 3 StGB** — Strafbare Verletzung von Privatgeheimnissen durch Rechtsanwälte; stärkt § 43a BRAO strafrechtlich ab.
- **§ 160a StPO** — Schutz von Berufsgeheimnisträgern bei verdeckten Ermittlungsmaßnahmen; gilt über den Verweis für den gesamten Bereich der Beweiserhebung.

### Besonderheit: Syndikusrechtsanwalt (§ 46 BRAO)

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 0: Anwendbares Recht bestimmen

Vor der Dokumentenprüfung: Welches Verfahrensrecht gilt?

- **ZPO-Verfahren**: § 142 ZPO (Urkundenvorlage), § 144 ZPO (Inaugenscheinnahme); Weigerungsrecht nach § 142 Abs. 2 ZPO i.V.m. §§ 383, 384 ZPO.
- **StPO-Verfahren**: § 97 StPO (Beschlagnahmeverbot); § 53 StPO (Zeugnisverweigerungsrecht); § 160a StPO (Schutz bei Ermittlungsmaßnahmen).
- **VwGO/FGO/SGG**: Parallelvorschriften; Vorlagepflicht vergleichbar §§ 86, 99 VwGO; Akteneinsichtsrechte.

Quellenattribuierung: Jeden Regelhinweis und jede Entscheidung in der Ausgabe mit Herkunftsnachweis versehen: `[Primärquelle]`, `[Kommentar – prüfen]`, `[Trainingsdaten – prüfen]`. Quellen mit Prüfvermerk tragen höheres Fehlerrisiko und sollten zuerst verifiziert werden.

### Schritt 1: Formatkontrolle

Hat der Dokumentensatz die erforderlichen Angaben?

| Feld | Vorhanden? |
|---|---|
| Datum | |
| Verfasser/Urheber | |
| Empfänger (An, CC, BCC) | |
| Dokumentenart | |
| Behaupteter Schutztatbestand (Mandatsgeheimnis / Beschlagnahmeverbot / Zeugnisverweigerung) | |
| Beschreibung (ausreichend zur Beurteilung ohne Offenbarung des Geschützten) | |

Fehlende Felder → vor der inhaltlichen Prüfung zur Ergänzung markieren.

### Schritt 2: Eintrag für Eintrag

Für jeden Eintrag:

```
Eintrag [N] ([Aktenzeichen/Belegnummer]): [✅ Geschützt | ✅ Geschützt + ⚠️ Markiert | ❌ Nicht geschützt (Bewertung)]
[Bei ✅ (ohne Markierung): einzeilige Begründung mit Norm]
[Bei ✅ + ⚠️: Schutz behalten; konkrete Frage, die der Anwalt beantworten muss; Argumente pro und contra]
[Bei ❌: einzeilige Begründung — Schutz bleibt im Register, bis der Anwalt ihn entfernt]
```

**Dreistufenregel:** Der Skill entscheidet nie stillschweigend eine subjektive Schwellenwertfrage. Bei jeder unsicheren Entscheidung — Mandatsgeheimnis oder rein kaufmännischer Zweck, Beschlagnahme­schutz grenzwertig, gemischter Inhalt, Beteiligung Dritter — wird die Schutzklassifizierung beibehalten und eine ⚠️-Markierung gesetzt. Zu wenig als geschützt zu kennzeichnen öffnet die Tür zu Beweismittelverlust (einbahnige Tür); zu viel als geschützt zu kennzeichnen ist vom Anwalt korrigierbar (zweiseitige Tür). Den korrigierbaren Fehler bevorzugen.

### Schritt 3: Mustererkennung

Über den gesamten Dokumentensatz:

- Gleiche Frage wiederholt? (Z. B. dieselbe Drittpartei in 50 Einträgen — eine Entscheidung löst 50 Markierungen)
- Überklassifizierungsmuster? (Wenn alles als geschützt gekennzeichnet wird, ohne Differenzierung — dem Anwalt zur Kenntnis bringen; aber die Entscheidung zur Einschränkung liegt beim Anwalt)
- Unzureichende Beschreibungen? (So vage, dass ein Gericht eine In-Camera-Prüfung anordnen könnte)

## Ausgabeformat

### Vor der Vorlage an das Gericht oder die Gegenseite — Schranke

Vor Einreichung einer Aufstellung vorzulegender/verweigernder Dokumente beim Gericht oder vor Übergabe an die Gegenseite:

> Die Vorlage oder Verweigerung von Dokumenten hat rechtliche Folgen — unzureichende Verweigerungsbegründungen können zur Vorlageerzwingung führen; unberechtigte Zurückhaltung kann Kostennachteile auslösen; eine versehentlich offengelegte Unterlage ist möglicherweise nicht rückrufbar. Wurde dies mit einem Anwalt besprochen? Falls ja: bitte bestätigen. Falls nein, hier ist ein Briefing für das Gespräch:
>
> [Zusammenfassung: Mandat, Anzahl geprüfter Dokumente, ⚠️-Markierungen und kritische Grenzfälle, Muster (Überklassifizierung, vage Beschreibungen), Normenlage je Schutztatbestand, was bei Vorlage schiefgehen kann.]

Ohne ausdrückliche Bestätigung wird die Liste nicht als vorlagebereits behandelt. Erstprüfung, Sortierung und interne Markierung erfordern die Schranke nicht — der Umgang mit dem Gericht schon.

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Kanzleikonfiguration]

## Vertraulichkeitsschutz-Erstprüfung: [Mandat] — [Datum]

**Anwendbare Normen:** [§ 142 ZPO / § 97 StPO / § 53 StPO / § 43a BRAO — Pinpoint-Zitate] `[UNSICHER — Aktualität prüfen]`
**Dokumente geprüft:** [N]
**Ergebnis:** [N] ✅ sicher geschützt / [N] ✅+⚠️ Schutz beibehalten & markiert / [N] ❌ Schutzentfernung empfohlen (Anwalt bestätigt)

### ✅ + ⚠️ Markiert — Schutz beibehalten, Anwalt entscheidet

| Eintrag | Belegnummer | Frage | Pro Schutz | Contra Schutz | Zu klärende Entscheidung |
|---|---|---|---|---|---|
| [N] | [Bereich] | [Was subjektiv ist] | [eine Zeile] | [eine Zeile] | [konkrete zu treffende Entscheidung] |

### ❌ Schutzentfernung empfohlen (Anwalt bestätigt vor Streichung)

| Eintrag | Belegnummer | Begründung |
|---|---|---|

*Vermerkt, nicht vollzogen. Der Skill entfernt keine Schutzklassifizierungen aus dem Register — das tut der Anwalt nach Prüfung.*

### ✅ Geschützt (kein Handlungsbedarf)

[Anzahl. Liste auf Anfrage abrufbar.]

### Musterbeobachtungen

[Wiederkehrende Fragen, Überklassifizierung, Beschreibungsprobleme]

### Markierungsdisziplin

- `[PRÜFEN: Sachaussage über Dokument/Verfasser/Datum]`
- `[UNSICHER: Grenzfall Schutztatbestand / Beschlagnahme / Reichweite]`
- `[BELEG FEHLT: Norm, lokale Variante oder Entscheidung als Stütze]`

---

**Anwalt muss alle ⚠️- und ❌-Einträge vor jeder Maßnahme prüfen.**

**Schutzwürdigkeit des Ausgabedokuments:** Diese Prüfung liest per definitionem schutzkandidaten-fähige Unterlagen. Das Ausgabedokument erbt diesen Status — es ist mit dem Mandatsmaterial zu verwahren, entsprechend zu kennzeichnen und nicht außerhalb des Vertrauenskreises zu verbreiten. Eine Weitergabe kann selbst den Schutz aushöhlen.
```

## Beispiel

**Sachverhalt:** Anordnung nach § 142 ZPO; Gericht verlangt Vorlage aller E-Mails zwischen der Partei und ihrem Rechtsanwalt zu einer Schadensersatzforderung.

**Erstprüfungsergebnis:**
- ✅ 12 E-Mails: Mandatsgeheimnis (§ 43a Abs. 2 BRAO); Anwalt bittet um Rechtsrat, Anwalt erteilt Rat; keine Drittpartei im Verteiler.
- ✅+⚠️ 3 E-Mails: Anwalt in CC bei rein kaufmännischer Verhandlung; dominanter Zweck unklar → Anwalt entscheidet.
- ❌ 2 E-Mails: Keine anwaltliche Beteiligung; CC an Anwalt ohne rechtliche Substanz; Bewertung: kein Schutz nach § 43a BRAO.

## Risiken und typische Fehler

- **Syndikusanwalt-Grenzfälle:** Die Schutzwürdigkeit von Korrespondenz des Syndikusrechtsanwalts hängt von seiner konkreten Funktion im Einzelfall ab (§ 46 Abs. 3 BRAO) — nie pauschal als "sicher geschützt" klassifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wirkung der Weitergabe:** Wird ein eigentlich geschütztes Dokument im Verfahren vorgelegt (auch versehentlich), kann der Schutz vollständig entfallen — Rückruf ist möglich, aber keineswegs sicher.
- **Beschreibungstiefe:** Zu vage Beschreibungen können dazu führen, dass das Gericht eine In-Camera-Vorlage zur eigenen Prüfung anordnet.
- **Fehlende Quellenverifizierung:** Alle Normen- und Entscheidungshinweise in der Ausgabe sind KI-generiert; vor einer Einreichung sind sie gegen Primärquellen (amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang, Wolters Kluwer) zu verifizieren.

## Quellenpflicht

- Gesetzestexte: §§ 142, 144 ZPO; §§ 53, 53a, 97, 160a StPO; §§ 43a, 46 BRAO; § 203 StGB; §§ 86, 99 VwGO
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## 3. `argumentationsverbesserung-red-team`

**Fokus:** Verbessert prozessuale Argumentation in Klage, Erwiderung, Replik, Berufung, Eilantrag oder Mandatsmemo. Prueft These, Beweis, Subsumtion, Gegenargumente, Richterperspektive, Antragsfassung und Ton.

# Argumentationsverbesserung und Red Team

## Zweck

Dieser Skill hilft, wenn ein prozessualer Text schon existiert oder eine Argumentationsidee im Raum steht, aber noch nicht stark genug ist.

## Vier Pflichtbausteine

1. Ziel klaeren: Was soll entschieden, geprueft, entworfen, verbessert oder verhandelt werden?
2. Kontext sichern: Rolle, Frist, Dokumente, Beteiligte, Vorgeschichte und Belege.
3. Grenzen setzen: keine Blindzitate, keine erfundenen Tatsachen, keine ungewollten Zugestaendnisse.
4. Ausgabeformat bestimmen: Memo, Tabelle, Schriftsatz, Brief, Beschluss, TOP, Checkliste oder Red-Team-Liste.

## Workflow

1. Material erfassen und sichtbar zwischen Tatsache, Behauptung und Bewertung trennen.
2. Eilige Punkte vorziehen.
3. Schwachstellen und Gegenargumente benennen.
4. Passende Folge-Skills aus demselben Plugin vorschlagen.
5. Einen verwendbaren Output liefern und offene Punkte mit `[noch klaeren]` markieren.

## Ausgabe

| Punkt | Befund | Risiko | Naechster Schritt |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

## Qualitaetsgate

Ist die Antwort handlungsorientiert, knapp, respektvoll, belegnah und ohne erfundene Quellen? Sind Fristen und offene Tatsachen sichtbar? Ist der naechste Schritt eindeutig?

## Prozessuale Argumentations-Pruefpunkte

- **Anspruchsgrundlage konkret benannt:** Norm, nicht "der Vertrag" oder "das Gesetz". Bei mehreren AG Vorrang/Konkurrenz pruefen.
- **Tatbestandsmerkmale gegliedert:** Jedes Merkmal mit Definition (Quelle: Rspr./Lit.), Tatsachen-Anker, Subsumtion.
- **Schluessigkeit (§ 253 II Nr. 2 ZPO):** Beim Klaeger reichen Tatsachenvortrag und Anspruchsgrundlage. Beim Beklagten ist Erheblichkeit der Einwendungen zu pruefen.
- **Beweisangebot:** Bei jedem streitigen Tatsachenbehauptung Beweismittel benennen (Zeuge mit Anschrift, Urkunde mit Anlagennummer, Sachverstaendiger, Augenschein, Parteivernehmung § 445 ZPO).
- **Beweismass:** § 286 ZPO (Vollbeweis bei haftungsbegruendenden Tatsachen) vs. § 287 ZPO (Schadensschaetzung).
- **Substantiierungslast:** Bei substantiiertem Vortrag ist substantiiertes Bestreiten erforderlich (§ 138 II ZPO); sonst Geslaendnisfiktion § 138 III ZPO.
- **Antragsfassung:** bestimmt, vollstreckbar, zukunftsorientiert ("zu zahlen", nicht "geschuldet zu sein").
- **Richterperspektive:** Wuerde ein neutraler Richter die These nachvollziehen koennen? Spruchreife herstellen.
- **Gegenargumente vorwegnehmen:** "Eingewendet werden koennte ... Dem ist jedoch entgegenzuhalten ..." schwaecht die Gegenseite vor.
- Falle: Klageantrag unbestimmt — § 139 ZPO Hinweispflicht greift, aber zur eigenen Sicherheit den Antrag praeszise antragen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

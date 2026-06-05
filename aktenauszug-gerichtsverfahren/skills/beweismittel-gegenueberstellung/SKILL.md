---
name: beweismittel-gegenueberstellung
description: "Beweismittel Gegenueberstellung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beweismittel Gegenueberstellung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beweismittel Gegenueberstellung** im Plugin Aktenauszug zivilgerichtlicher Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `beweismittel-gegenueberstellung` | Anwalt will Beweisangebote aller Parteien uebersichtlich gegenüberstellen: Zeugen Urkunden Sachverständige Parteivernehmung Augenschein. Normen §§ 355-455 ZPO Sachverständigenbeweis Zeugenbeweis. Prüfraster Vollständigkeit Parteizuordnung Streitpunkt-Zuordnung Fundstellen. Output tabellarische Beweismittel-Übersicht. Abgrenzung zu parteivortrag-gegenüberstellung (Sachverhalt) und rechtsargumente-gegenüberstellung (Recht). |
| `einleitungssatz-generator` | Aktenauszug braucht praegnanten Einleitungssatz: wer streitet mit wem worueber welche Hauptnorm. Juristisch praezise neutral ohne Wertung ohne Erfolgsprognose. Normen §§ 253 304 ZPO. Prüfraster Praegnanz Vollständigkeit Neutralitaet Haupt-Norm-Nennung. Output Ein-Zwei-Satz-Kern Rechtstreit. Abgrenzung zu verfahrenszusammenfassung-absatz (laengerer Überblick) und verfahrensidentifikation (Stammdaten). |
| `neutralitaetspruefung` | Prüft einen erstellten Aktenauszug auf unzulässige Wertungen und Erfolgseinschaetzungen und neutralisiert diese. Markiert alle parteiischen Formulierungen Prognosen und Bewertungen und schlaegt neutrale Ersatzformulierungen vor. Sicherheitsgate vor Weitergabe des Auszugs. Massstab § 286 ZPO freie Beweiswürdigung. |

## Arbeitsweg

Im Plugin Aktenauszug zivilgerichtlicher Verfahren gilt für **Beweismittel Gegenueberstellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `beweismittel-gegenueberstellung`

**Fokus:** Anwalt will Beweisangebote aller Parteien uebersichtlich gegenüberstellen: Zeugen Urkunden Sachverständige Parteivernehmung Augenschein. Normen §§ 355-455 ZPO Sachverständigenbeweis Zeugenbeweis. Prüfraster Vollständigkeit Parteizuordnung Streitpunkt-Zuordnung Fundstellen. Output tabellarische Beweismittel-Übersicht. Abgrenzung zu parteivortrag-gegenüberstellung (Sachverhalt) und rechtsargumente-gegenüberstellung (Recht).

# Beweismittel — Gegenüberstellung

## Zweck

Die Beweismitteltabelle listet alle in den Schriftsätzen angebotenen Beweismittel beider Parteien auf und ordnet sie den jeweiligen Beweisthemen zu. Sie ermöglicht einen schnellen Überblick über die Beweissituation.

## Triage — kläre vor Erstellung

1. Welche Beweismittel sind bereits erhoben (Gutachten vorgelegt, Zeugen vernommen)?
2. Welche Beweismittel sind angeboten aber noch nicht erhoben?
3. Hat das Gericht bereits über die Beweiserhebung entschieden? (Beweisbeschluss § 359 ZPO)
4. Wurden Beweismittel vom Gericht als präkludiert zurückgewiesen (§§ 296, 531 ZPO)?

## Zulässige Beweismittel und Normen (§ 355 ff. ZPO)

- § 371 ff. ZPO — Augenscheinsbeweis (Besichtigung, Fotos, Videoaufnahmen)
- § 373 ff. ZPO — Zeugenbeweis (Ladung, Vernehmung, Eid, Aussageverbot)
- § 402 ff. ZPO — Sachverständigenbeweis (Bestellung, Gutachtenerstattung, Ablehnung)
- § 415 ff. ZPO — Urkundenbeweis (öffentlich/privat, Echtheit, Beweiskraft)
- § 445 ff. ZPO — Parteivernehmung (nur bei Unvollständigkeit anderer Beweismittel)

## Rechtsprechung zum Beweisrecht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Tabellenstruktur

```markdown
| Beweisthema | Beweismittel | Partei | Bezeichnung / Name | Fundstelle |
|---|---|---|---|---|
| [Streitpunkt] | [Art] | Kläger / Beklagter | [Name / Anlage] | [Schriftsatz Bl.] |
```

## Beispiel

| Beweisthema | Beweismittel | Partei | Bezeichnung / Name | Fundstelle |
|---|---|---|---|---|
| Vertragsinhalt Einweisung | Urkunde | Kläger | Werkvertrag K 1 | Klageschrift Bl. 12 |
| Mangel Dach | Zeuge | Kläger | Heiko Mustermann (Bauleiter) | Klageschrift Bl. 28 |
| Mangel Dach | Sachverständiger | Kläger | Einholung eines Baugutachtens | Klageschrift Bl. 29 |
| Ursache Undichtigkeit | Zeuge | Beklagter | Maria Musterfrau (Mitarbeiterin) | Klageerwiderung Bl. 52 |
| Schadenshöhe | Urkunde | Kläger | Sanierungskostenrechnung K 8 | Replik Bl. 70 |
| Schadenshöhe | Sachverständiger | Beklagter | Gegengutachten (beantragt) | Klageerwiderung Bl. 66 |

## Besondere Hinweise

### Urkundenbeweis

Jede Urkunde wird mit ihrer Anlagenbezeichnung (K 1, B 1 etc.) und einem kurzen Inhaltsvermerk aufgeführt.

### Zeugen

Vollständiger Name (sofern bekannt), Eigenschaft (z. B. "Augenzeuge", "Vertragspartner", "Mitarbeiter"), benennende Partei.

### Sachverständige

Wird ein Gutachten beantragt (nicht bereits vorhanden), so ist das Beweisthema zu nennen. Liegt ein Gutachten bereits vor, wird das Gutachten als Urkunde und der Gutachter als gesondert aufgeführt.

### Parteivernehmung

Selten — nur wenn angeboten oder angeordnet. Partei und Vernehmungsthema benennen.

### Präkludierte Beweismittel

Soweit Beweismittel vom Gericht als verspätet zurückgewiesen wurden, werden sie mit dem Vermerk "[zurückgewiesen]" aufgeführt.

## Qualitätscheck

- [ ] Alle angebotenen Beweismittel erfasst?
- [ ] Beweisthema klar bezeichnet?
- [ ] Anlagenbezeichnung und Fundstelle angegeben?
- [ ] Keine Bewertung der Beweiskraft?
- [ ] Präkludierte Beweismittel gekennzeichnet?
- [ ] Beweisbeschluss des Gerichts (§ 359 ZPO) berücksichtigt?

## 2. `einleitungssatz-generator`

**Fokus:** Aktenauszug braucht praegnanten Einleitungssatz: wer streitet mit wem worueber welche Hauptnorm. Juristisch praezise neutral ohne Wertung ohne Erfolgsprognose. Normen §§ 253 304 ZPO. Prüfraster Praegnanz Vollständigkeit Neutralitaet Haupt-Norm-Nennung. Output Ein-Zwei-Satz-Kern Rechtstreit. Abgrenzung zu verfahrenszusammenfassung-absatz (laengerer Überblick) und verfahrensidentifikation (Stammdaten).

# Einleitungssatz-Generator

## Zweck

Der Einleitungssatz gibt dem Leser in einem bis zwei Sätzen den Kern des Rechtsstreits wieder. Er nennt die handelnden Parteien, den Streitgegenstand und — wo möglich — die anwendbare Hauptnorm. Er ersetzt nicht die Zusammenfassung, sondern eröffnet sie.

## Triage — kläre vor Formulierung

1. Zivilverfahren, Arbeitsgericht, Strafverfahren, Verwaltungsgericht oder Sozialgericht?
2. Erstinstanz, Berufung oder Revision?
3. Was ist die Hauptnorm des Anspruchs oder der Anklage?
4. Wie lautet der exakte Klagebetrag oder das Klagebegehren?

## Zentrale Normen (Streitgegenstand / Klagebegehren)

- § 253 Abs. 2 Nr. 2 ZPO — Klageschrift: bestimmter Antrag und Sachverhalt als Grundlage des Einleitungssatzes
- § 264 ZPO — Klageaenderung (im Einleitungssatz ggf. letzten Stand des Antrags aufführen)
- § 308 ZPO — Bindung des Gerichts an Antrag (ne ultra petita)
- § 42 VwGO — Anfechtungs- und Verpflichtungsklage
- § 4 KSchG — Kündigungsschutzklage (Frist und Antrag)

## Rechtsprechung zum Streitgegenstand und Klagebegehren

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Struktur des Einleitungssatzes

**Muster:**

> [Kläger] nimmt [Beklagten] aus [Hauptnorm] auf [Klagebegehren] in Anspruch.

Ergänzend kann ein zweiter Satz den prozessualen Stand knapp abbilden:

> Die Klage ist seit [Datum] beim [Gericht] anhängig; [mündliche Verhandlung steht aus / Urteil erging am ...].

## Varianten nach Verfahrensart

### Zivilverfahren (ZPO)

> [Kläger] begehrt von [Beklagtem] Zahlung von [Betrag] nebst Zinsen aus § [Norm] BGB wegen [Sachverhaltskern]; das Verfahren ist beim Landgericht [Stadt] als [AZ] anhängig.

### Eilverfahren (§ 935 ff. ZPO)

> [Antragstellerin] begehrt im Wege der einstweiligen Verfügung gemäß §§ 935 938 ZPO die Unterlassung von [Handlung] gegenüber [Antragsgegner]; das Verfahren ist beim [Gericht] als [AZ] anhängig.

### Berufungsverfahren

> [Berufungsklägerin] wendet sich mit ihrer Berufung vom [Datum] gegen das Urteil des Landgerichts [Stadt] vom [Datum] (Az. [AZ]) und begehrt weiterhin [Klagebegehren].

### Strafverfahren (StPO)

> Der Angeklagte [Name] ist durch Anklage der Staatsanwaltschaft [Ort] vom [Datum] wegen [Vorwurf] (§§ [Normen] StGB) angeklagt; die Hauptverhandlung findet vor der [Kammer] des [Gerichts] unter dem Az. [AZ] statt.

### Verwaltungsverfahren (VwGO)

> Die Klägerin wendet sich mit einer Anfechtungsklage (§ 42 Abs. 1 Alt. 1 VwGO) gegen den Bescheid der Behörde [Name] vom [Datum] und begehrt dessen Aufhebung.

### Arbeitsgerichtsverfahren (ArbGG)

> Die Klägerin begehrt die Feststellung der Unwirksamkeit der ordentlichen Kündigung vom [Datum] gemäß § 4 KSchG; das Verfahren ist beim Arbeitsgericht [Stadt] als [AZ] anhängig.

### Sozialgerichtsverfahren (SGG)

> Die Klägerin begehrt die Gewährung von [Leistung] durch den Beklagten [Träger] und hat nach Erfolglosigkeit des Widerspruchsverfahrens Klage beim Sozialgericht [Stadt] erhoben (Az. [AZ]).

## Regeln

- Maximal zwei Sätze
- Keine Wertung (nicht: "zu Unrecht"; "unbegründet")
- Keine Erfolgsprognose
- Parteinamen vollständig benennen (kein "Kl." oder "Bekl." im Einleitungssatz)
- Normen mit vollständiger Bezeichnung (nicht nur Paragraphennummer)

## Qualitätscheck

Nach Erstellung prüfen:
- [ ] Wer streitet mit wem? ja/nein
- [ ] Worüber wird gestritten? ja/nein
- [ ] Hauptnorm genannt? ja/nein
- [ ] Keine Wertung? ja/nein
- [ ] Maximal zwei Sätze? ja/nein
- [ ] Streitgegenstand i.S.v. § 253 Abs. 2 Nr. 2 ZPO hinreichend bestimmt? ja/nein

## 3. `neutralitaetspruefung`

**Fokus:** Prüft einen erstellten Aktenauszug auf unzulässige Wertungen und Erfolgseinschaetzungen und neutralisiert diese. Markiert alle parteiischen Formulierungen Prognosen und Bewertungen und schlaegt neutrale Ersatzformulierungen vor. Sicherheitsgate vor Weitergabe des Auszugs. Massstab § 286 ZPO freie Beweiswürdigung.

# Neutralitätsprüfung

## Zweck

Der Aktenauszug muss neutral formuliert sein — er gibt den Stand eines Verfahrens wieder, ohne eine Seite zu bevorzugen oder eine Erfolgsprognose abzugeben. Dieser Skill prüft einen erstellten Aktenauszug auf Neutralitätsverstöße und schlägt Korrekturen vor.

## Triage — kläre vor der Prüfung

1. Für wen ist der Aktenauszug bestimmt? (internes Arbeitsdokument / Übergabe an Mandant / Gericht)
2. Hat der Ersteller den Auftrag, die eigene Mandantsseite besonders darzustellen? (dann kein Aktenauszug, sondern Schriftsatz!)
3. Gibt es Stellen, die bewusst als subjektive Einschätzung des Anwalts markiert sind? (Diese sind zu entfernen oder zu kennzeichnen.)

## Normhintergrund

- § 286 Abs. 1 ZPO — Freie Beweiswürdigung des Gerichts; Aktenauszug darf keine Beweiswürdigungsprognosen enthalten
- § 138 ZPO — Wahrheitspflicht; auch interne Vermerke müssen den Sachverhalt korrekt abbilden
- § 43a Abs. 3 BRAO — Sachlichkeitsgebot; gilt auch für interne Aktendokumentation

## Rechtsprechung zum Sachlichkeitsgebot und Neutralität

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verbotene Formulierungstypen

### Erfolgsprognosen (absolut verboten)

| Verboten | Erlaubt |
|---|---|
| "Die Klage wird Erfolg haben" | "Die Klage ist anhängig" |
| "Der Anspruch dürfte begründet sein" | "Die Klägerin macht [Anspruch] geltend" |
| "Die Verjährungseinrede greift durch" | "Die Beklagte erhebt die Verjährungseinrede" |
| "Das Gericht wird … erkennen" | "Das Gericht hat … nicht geäußert" |
| "offensichtlich unbegründet" | "nach Vortrag der Beklagten unbegründet" |

### Wertende Adjektive (zu vermeiden)

- substanzlos, unhaltbar, abwegig, überzeugend, zutreffend, unzutreffend
- zu Recht, zu Unrecht
- offensichtlich, eindeutig (ohne Quellenangabe)

### Parteiische Darstellung

- Ausführliche Wiedergabe des Vortrags einer Seite ohne entsprechende Gegenüberstellung der anderen Seite
- Formulierungen, die implizit eine Seite stärken ("Trotz des klaren Wortlauts des Vertrags …")

## Prüfmethodik

### Schritt 1 — Scan auf verbotene Muster

Folgende Muster systematisch suchen:

- `dürfte`, `wird`, `sollte`, `kann davon ausgegangen werden`
- `zu Recht`, `zu Unrecht`, `offensichtlich`, `eindeutig`
- `überzeugt`, `überzeugend`, `substanzlos`, `unhaltbar`
- `Erfolgsaussichten`, `Erfolg haben`, `scheitern`

### Schritt 2 — Parteibalance prüfen

Jeder Abschnitt des Parteivortrag und der Rechtsargumente muss beide Seiten gleichgewichtig darstellen.

### Schritt 3 — Korrekturen vorschlagen

Für jede beanstandete Formulierung wird eine neutrale Ersatzformulierung vorgeschlagen.

## Ergebnis-Format

```markdown
## Neutralitätsprüfung — Ergebnis

### Beanstandungen

| Stelle | Ursprüngliche Formulierung | Ersatzformulierung |
|---|---|---|
| Zusammenfassung Satz 3 | Anspruch dürfte begründet sein | Klägerin macht den Anspruch geltend |
| Rechtsargument Zeile 4 | offensichtlich verjährt | nach Vortrag der Beklagten verjährt |

### Ergebnis

[BESTANDEN / ÜBERARBEITUNG ERFORDERLICH]

Anzahl Beanstandungen: [Zahl]
```

## Qualitätscheck — Checkliste

- [ ] Keine Erfolgsprognose enthalten?
- [ ] Keine wertenden Adjektive ohne Quellenattribution?
- [ ] Parteivortrag beider Seiten gleichgewichtig dargestellt?
- [ ] Fristen neutral als Tatsache, nicht als Gefahr formuliert?
- [ ] Keine implizit parteiische Darstellung?

## Hinweis

Die Neutralitätsprüfung ist kein Korrektorat des Aktenauszugs. Sie prüft ausschließlich auf Wertungen und Prognosen. Sachliche Fehler sind durch Abgleich mit der Akte zu beheben.

---

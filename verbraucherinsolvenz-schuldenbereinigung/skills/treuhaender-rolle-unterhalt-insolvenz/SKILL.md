---
name: treuhaender-rolle-unterhalt-insolvenz
description: "Treuhaender Rolle Unterhalt Insolvenz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Treuhaender Rolle Unterhalt Insolvenz

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Treuhaender Rolle Unterhalt Insolvenz** im Plugin Verbraucherinsolvenz Schuldenbereinigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verbraucherinsolvenz-treuhaender-rolle` | Verbraucherinsolvenz: Rolle des Treuhaenders. Skill behandelt die Aufgaben des Treuhaenders in der Wohlverhaltensphase Vermoegensaufsicht Verteilung Forderungspruefung Glaeubigerinformation. Verguetung und Kostenfragen. Liefert Pruefraster. |
| `verbraucherinsolvenz-unterhalt-und-insolvenz` | Verbraucherinsolvenz und eheliche Unterhaltspflicht. Skill behandelt das Verhaeltnis von laufender Unterhaltspflicht zum Insolvenzverfahren Pflichten in der Wohlverhaltensphase Anrechnung und Rangordnung. Liefert Pruefraster. |
| `verbraucherinsolvenz-versagungsgruende` | Verbraucherinsolvenz: Versagungsgruende. Skill behandelt § 290 InsO Versagung der Restschuldbefreiung Tatbestaende Strafurteile Vermoegensverlagerung Verletzung Aufklaerungspflicht und Erwerbsobliegenheit. Verteidigungsstrategien. Liefert Pruefraster. |

## Arbeitsweg

Im Plugin Verbraucherinsolvenz Schuldenbereinigung gilt für **Treuhaender Rolle Unterhalt Insolvenz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verbraucherinsolvenz-treuhaender-rolle`

**Fokus:** Verbraucherinsolvenz: Rolle des Treuhaenders. Skill behandelt die Aufgaben des Treuhaenders in der Wohlverhaltensphase Vermoegensaufsicht Verteilung Forderungspruefung Glaeubigerinformation. Verguetung und Kostenfragen. Liefert Pruefraster.

# Verbraucherinsolvenz Treuhaender Rolle

## Fachkern: Verbraucherinsolvenz Treuhaender Rolle
- **Spezialgegenstand:** Verbraucherinsolvenz Treuhaender Rolle. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Skill fuer Treuhaender-Mandate.

## Norm

- §§ 292 ff. InsO Treuhaender.
- § 293 InsO Bestellung.
- § 295 InsO Aufgaben.

## Aufgaben

### Vermoegensaufsicht
- Empfang der monatlichen Abfuehrungen.
- Pruefung auf Erfuellung der Mitwirkungspflichten.

### Forderungspruefung
- Anmeldung Pruefung.
- Bestreitung bei zweifelhaften Forderungen.

### Glaeubigerinformation
- Jahresberichte.
- Schlussbericht.

### Verteilung
- Quotale Verteilung der Massen.

## Verguetung

- § 14 InsVV Insolvenzrechtsverguetungsverordnung.
- Mindestverguetung 100 Euro/Jahr fuer Treuhaender in Verbraucherinsolvenz.

## Pruefraster

1. Treuhaenderaufgaben sauber abgegrenzt?
2. Pflichtverletzungen?
3. Verguetung angemessen?

## Output

- Treuhaender-Memo.
- Jahresbericht-Vorlage.
- Schlussbericht-Vorlage.

## 2. `verbraucherinsolvenz-unterhalt-und-insolvenz`

**Fokus:** Verbraucherinsolvenz und eheliche Unterhaltspflicht. Skill behandelt das Verhaeltnis von laufender Unterhaltspflicht zum Insolvenzverfahren Pflichten in der Wohlverhaltensphase Anrechnung und Rangordnung. Liefert Pruefraster.

# Verbraucherinsolvenz Unterhalt Und Insolvenz

## Fachkern: Verbraucherinsolvenz Unterhalt Und Insolvenz
- **Spezialgegenstand:** Verbraucherinsolvenz Unterhalt Und Insolvenz. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Skill fuer Schnittstelle Insolvenz / Unterhalt.

## Norm

- §§ 1601 ff. BGB Familienunterhalt.
- §§ 287, 295 InsO Mitwirkung in Wohlverhaltensphase.

## Laufende Unterhaltspflicht

- Unterhalt aus Erwerbseinkommen ist nicht der Insolvenzmasse zugeordnet.
- § 850d ZPO: privilegierte Pfaendbarkeit fuer Unterhalt; bevorrechtigter Anspruch.

## Unterhaltsrueckstaende vor Insolvenzantrag

- Werden als Insolvenzforderung behandelt.
- § 302 Nr. 3 InsO: Unterhaltsrueckstaende vor Insolvenzverfahren nehmen nicht an der Restschuldbefreiung teil.

## Erwerbsobliegenheit

- Pflicht zur vollen Erwerbstaetigkeit auch zur Unterhaltsleistung.

## Pruefraster

1. Laufender oder rueckstaendiger Unterhalt?
2. Rangordnung?
3. Erwerbsobliegenheit erfuellt?
4. § 850d ZPO-Pfaendung?

## Output

- Pruefraster.
- Schriftsatzbaustein.

## 3. `verbraucherinsolvenz-versagungsgruende`

**Fokus:** Verbraucherinsolvenz: Versagungsgruende. Skill behandelt § 290 InsO Versagung der Restschuldbefreiung Tatbestaende Strafurteile Vermoegensverlagerung Verletzung Aufklaerungspflicht und Erwerbsobliegenheit. Verteidigungsstrategien. Liefert Pruefraster.

# Verbraucherinsolvenz Versagungsgruende

## Fachkern: Verbraucherinsolvenz Versagungsgruende
- **Spezialgegenstand:** Verbraucherinsolvenz Versagungsgruende. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Skill fuer Versagungsverfahren.

## Norm

- § 290 InsO.

## Tatbestaende

### § 290 Abs. 1 Nr. 1 InsO
- Strafurteil wegen § 283 ff. StGB Bankrott.

### § 290 Abs. 1 Nr. 2 InsO
- Verletzung Aufklaerungspflicht im Antrag.

### § 290 Abs. 1 Nr. 3 InsO
- Vermoegensverschiebung in 10 Jahren vor Antrag.

### § 290 Abs. 1 Nr. 4 InsO
- Letzte 10 Jahre eine Restschuldbefreiung erteilt.

### § 290 Abs. 1 Nr. 5 InsO
- Verletzung Erwerbsobliegenheit.

### § 290 Abs. 1 Nr. 6 InsO
- Unrichtige oder unvollstaendige Vermoegensaufstellung.

## Verteidigungsstrategien

- Pruefen des Tatbestands.
- Verschulden des Schuldners?
- Geringfuegigkeit (Bagatellgrenze in einzelnen Faellen).
- Glaeubiger-Stellungnahme einholen.

## Pruefraster

1. Welcher Tatbestand?
2. Verschulden?
3. Bagatelle?
4. Verfahrensgang?

## Output

- Verteidigungs-Memo.
- Schriftsatz.

---
name: kreditausfallversicherung-warenkredit
description: "Kreditausfallversicherung Warenkredit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kreditausfallversicherung Warenkredit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Kreditausfallversicherung Warenkredit** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kreditausfallversicherung-warenkredit-forderungsausfall` | Kreditausfall-/Warenkreditversicherung: Limit, Forderungsausfall, Insolvenztatbestand, Obliegenheiten, Selbstbehalt, Factoring-Schnittstelle und Regress. |
| `kreditversicherung-obliegenheiten-limit-pruefung` | Kreditversicherung im laufenden Debitorenmanagement: Limite, Überfälligkeiten, Risikoinformationen, Inkassostart, Meldungen und Streit um Leistungsfreiheit. |
| `lebensversicherung-bezugsrecht-widerruf-aenderung` | Bezugsrechte in Lebens- und Rentenversicherung: widerruflich/unwiderruflich, Scheidung, Erbfall, Sicherungsabtretung, Insolvenz, Änderungserklärung und Auszahlungsstreit. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **Kreditausfallversicherung Warenkredit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kreditausfallversicherung-warenkredit-forderungsausfall`

**Fokus:** Kreditausfall-/Warenkreditversicherung: Limit, Forderungsausfall, Insolvenztatbestand, Obliegenheiten, Selbstbehalt, Factoring-Schnittstelle und Regress.

# Kreditausfallversicherung und Warenkreditversicherung

## Einsatz

Für Lieferanten, die Zahlungsausfälle über Kreditversicherung absichern und bei Insolvenz des Kunden Deckung brauchen.

## Norm- und Quellenanker

VVG Schadenversicherung; AVB Warenkredit; InsO; HGB; Factoringvertrag.

## Arbeitsfragen

1. Welches Kreditlimit galt wann und für welchen Schuldner?
2. Ist der versicherte Forderungsausfall eingetreten?
3. Wurden Melde-, Mahn- und Inkassoobliegenheiten eingehalten?
4. Wie wirken Factoring, Abtretung und Eigentumsvorbehalt?

## Output

Limit-/Forderungsmatrix, Obliegenheitscheck, Insolvenznachweis und Deckungsantrag.

## Red Flags

- Lieferung nach Limitstreichung
- Mahnobliegenheiten verletzt
- Forderung abgetreten
- Ausfalltatbestand nicht erreicht

## Anschluss-Skills

- kreditversicherung-obliegenheiten-limit-pruefung
- restschuldversicherung-widerruf-kopplung-verbraucherdarlehen

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `kreditversicherung-obliegenheiten-limit-pruefung`

**Fokus:** Kreditversicherung im laufenden Debitorenmanagement: Limite, Überfälligkeiten, Risikoinformationen, Inkassostart, Meldungen und Streit um Leistungsfreiheit.

# Kreditversicherung: Limitprüfung und Obliegenheiten

## Einsatz

Der Skill eignet sich für Unternehmen, die ihr Debitorenportfolio versichert führen und nicht durch Prozessfehler Deckung verlieren wollen.

## Norm- und Quellenanker

VVG §§ 28, 31; AVB Kreditversicherung; InsO; BGB/HGB.

## Arbeitsfragen

1. Welche Limite sind aktiv, reduziert, gestrichen oder still?
2. Welche Überfälligkeiten lösen Meldung oder Lieferstopp aus?
3. Welche Informationen über Bonität/Insolvenz lagen vor?
4. Welche Dokumentation braucht der Versicherer?

## Output

Debitoren-Ampel, Obliegenheitskalender, Lieferfreigabe-Check und Schadenanzeige.

## Red Flags

- Excel-Limitliste veraltet
- Bonitätswarnung nicht gemeldet
- Weiterlieferung trotz Ausfallanzeichen
- Inkasso ohne Versichererabstimmung

## Anschluss-Skills

- kreditausfallversicherung-warenkredit-forderungsausfall
- vvg-obliegenheit-28-quotelung-kausalitaet

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `lebensversicherung-bezugsrecht-widerruf-aenderung`

**Fokus:** Bezugsrechte in Lebens- und Rentenversicherung: widerruflich/unwiderruflich, Scheidung, Erbfall, Sicherungsabtretung, Insolvenz, Änderungserklärung und Auszahlungsstreit.

# Lebensversicherung: Bezugsrecht, Widerruf, Änderung

## Einsatz

Der Skill klärt, wer bei Tod oder Ablauf wirklich Geld bekommt und wie Änderungen sauber dokumentiert werden.

## Norm- und Quellenanker

VVG §§ 150–171, besonders §§ 159, 160; BGB Erbrecht/Abtretung; InsO; FamFG/Nachlass.

## Arbeitsfragen

1. Ist das Bezugsrecht widerruflich oder unwiderruflich?
2. Wann und in welcher Form wurde geändert?
3. Gibt es Scheidung, Erbfall, Pfändung, Abtretung oder Insolvenz?
4. Welche Auszahlungsunterlagen fordert der Versicherer?

## Output

Bezugsrechtsgutachten, Unterlagenliste, Auszahlungsschreiben und Streitrisiko.

## Red Flags

- alte Ehegattenbezeichnung
- Sicherungsabtretung an Bank
- Erben verwechseln Nachlass und Bezugsrecht
- unwirksame Änderung kurz vor Tod

## Anschluss-Skills

- lebensversicherung-rueckkaufswert-abschlusskosten-widerspruch
- subrogation-regress-86-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

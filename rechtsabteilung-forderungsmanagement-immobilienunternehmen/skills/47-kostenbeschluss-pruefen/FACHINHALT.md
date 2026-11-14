---
name: 47-kostenbeschluss-pruefen
description: "KFB und Kostenfestsetzungsbeschluss prüfen. Abweichung vom KFA, Tenor, Betrag, Zinsen, Quote, Zustellung, Rechtsbehelfsfrist, Erinnerung, sofortige Beschwerde, vollstreckbare Ausfertigung und Zahlung prüfen."
---

# Kostenfestsetzungsbeschluss prüfen

## Zweck und Anwendungsfall

Dieser Skill verarbeitet den gerichtlichen Kostenfestsetzungsbeschluss und bereitet die weitere Beitreibung vor.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Kostenfestsetzungsbeschluss.
- Eigener KFA.
- Zustellnachweis und Kostenakte.
- Streitwertfestsetzung, Kostenrechnung, Berichtigungsbedarf oder gegnerische Einwendungen.
- Kostengrundentscheidung, Vergleich oder Urteil über materiell-rechtliche Kostenerstattung; beide Kostenwege ausdrücklich unterscheiden.

## Ablauf / Checkliste

1. Tenor, Betrag und Zinsen extrahieren.
2. Kostenquote und Abweichungen vom Antrag prüfen.
3. Zustellung und Rechtsbehelfsfrist notieren.
4. Vollstreckbare Ausfertigung oder elektronische Vollstreckbarkeit prüfen.
5. Rechtsbehelf exakt trennen: Gegen den Kostenfestsetzungsbeschluss ist nach Paragraf 104 Abs. 3 ZPO die sofortige Beschwerde vorgesehen. Sie ist nach Paragraf 567 Abs. 2 ZPO nur zulässig, wenn der Beschwerdewert 300 EUR übersteigt, und grundsätzlich binnen einer Notfrist von zwei Wochen nach Paragraf 569 Abs. 1 ZPO einzulegen. Wird die Wertgrenze nicht erreicht und hat die Rechtspflegerin entschieden, Erinnerung nach Paragraf 11 Abs. 2 RPflG prüfen. Streitwertbeschwerde nach Paragraf 68 GKG und Einwendungen gegen den Kostenansatz nicht damit vermischen.
6. Bei Vollstreckbarkeit an Skill `48-titulierte-forderung-vollstrecken` übergeben; Rechtsbehelfsfrist weiter überwachen, aber nicht pauschal Bestandskraft abwarten.
7. KFB-Betrag mit KFA, Quote, Gerichtskosten und Zahlungen abstimmen.
8. Zinsen ab Antragseingang nur übernehmen, wenn der Beschluss sie trägt.
9. Bei nicht auf das Urteil gesetztem KFB die Wartefrist nach Paragraf 798 ZPO und Zustellung prüfen.
10. Abweichungen zwischen KFA und KFB als Entscheidungsvorlage erfassen: akzeptieren, ergänzen lassen, Erinnerung prüfen.
11. Wenn der KFB auf einem teilweise abweisenden Urteil beruht, Quote, Beschwer, Rechtsbehelfsfrist und Kostenrisiko mit Skill `08-eskalation-an-anwalt` abgleichen.
12. Bei vollständigem Unterliegen keine Übergabe an Vollstreckung, sondern Fristenkontrolle und anwaltliche Fortsetzungsprüfung.
13. Rechtsbehelf gegen KFB, Streitwertfestsetzung oder Kostenrechnung nur mit Frist, Beschwer, Fehlerpunkt und konkretem Antrag vorbereiten.
14. Offensichtliche Fehler im Urteil, Beschluss oder Tatbestand als Berichtigungs- oder Tatbestandsberichtigungsfrage markieren und bei Rechtsmittelbezug an Skill `08-eskalation-an-anwalt` geben.
15. Bei einem Urteil über materiell-rechtliche Kostenerstattung prüfen, ob daneben eine echte prozessuale Kostengrundentscheidung vorliegt. Fehlt sie, keinen KFA oder KFB fingieren, sondern Bezifferungs- und Vollstreckungsweg mit Skill `46` und gegebenenfalls Skill `08` klären. BGH III ZR 156/12 nur als Basis für die materielle Kostenerstattungsklage verwenden, nicht als Ersatz für einen vollstreckbaren Kostentenor.
16. KFB als Zwischenstation behandeln: Abweichung prüfen, Frist setzen, Fehlerpunkt entscheiden; wenn vollstreckbar, an Skill `48`; wenn Rechtsbehelf oder Unterliegensrisiko besteht, Entscheidungsvorlage an Skill `08`.

## Argumentationsstandard

Die Abweichungsanalyse verbindet jede Differenz zwischen KFA und KFB mit Antrag, gerichtlicher Festsetzung, Begründung, Beschwer und möglicher Korrektur. Rechtsbehelf, Berichtigung, Streitwertbeschwerde und Kostenansatz werden nicht unter einem allgemeinen Einwand vermischt. Eine vorgeschlagene Reaktion nennt konkreten Fehler, Norm, Frist, Antrag und wirtschaftliche Auswirkung. Maßstab ist `references/schriftsatz-und-argumentationsstandard.md`.

## Quellenpflicht

Es gilt die Zitierweise nach `references/zitierweise.md` (Rechtsprechung vor Literatur, neueste zuerst); Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert.

ZPO-Kostenfestsetzung, Vollstreckungstitel und Rechtsbehelfe mit Normanker. Bei materieller Kostenerstattung und erledigender Hauptsache die geprüften Anker BGH III ZR 156/12 und VIII ZB 39/24 aus `references/gepruefte-bgh-anker-mietrecht.md` heranziehen. Keine Fristen schätzen.

## Ausgabeformat

Prüfvermerk mit Tabelle, Fristenblatt, Abweichungsanalyse, Vollstreckbarkeitscheck, Rechtsbehelfs-/Berichtigungscheck, Forderungsupdate, Unterliegenshinweis und nächstem Schritt.

## Beispiele

- Gericht setzt weniger fest als beantragt: Abweichung begründen lassen.
- KFB mit Zinsbeginn: Vollstreckungsforderung aktualisieren.
- KFB nach Teilunterliegen: Quote, Beschwer und Rechtsbehelfsfrist für die Stammkanzlei markieren.
- Falscher Streitwert oder Tatbestandsfehler: Frist notieren und Entscheidungsvorlage für Berichtigung oder Beschwerde erstellen.
- Kostenurteil und KFB: Kostengrund, Festsetzungsbetrag und Vollstreckungstitel nicht vermischen.

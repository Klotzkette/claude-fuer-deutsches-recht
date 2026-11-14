---
name: grest-spa-tax-clause-indemnity
description: "Für GrESt: SPA-Klauseln, Indemnity und Escrow: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# GrESt: SPA-Klauseln, Indemnity und Escrow

## Fachlicher Anker

- **Normen:** § 6a, § 19, § 13.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Klauselthemen

- Wer trägt GrESt aus der Transaktion?
- Wer trägt GrESt aus Altvorgängen?
- Wer trägt doppelte GrESt bei Signing/Closing-Streit?
- Wer kontrolliert Anzeige und Korrespondenz?
- Wer führt Einspruch/AdV/Klage?
- Darf ein Vergleich geschlossen werden?
- Wird ein Escrow für GrESt gebildet?
- Welche Garantien gelten zur Grundstücksliste?

## Review-Raster

| Klausel | Risiko |
|---|---|
| "Buyer bears all transfer taxes" | zu breit; Alt-GrESt und Verkäuferverstöße erfassen? |
| keine Anzeigepflicht | § 19-Risiko bleibt unverteilt |
| keine Grundbesitzliste | Bemessung und Zuständigkeit unklar |
| keine Streitkontrolle | Einspruchsfrist läuft beim falschen Team |
| keine Doppelbesteuerungsklausel | Signing/Closing-Liquiditätsrisiko offen |

## Stil

Kurz, deal-tauglich, nicht lehrbuchhaft. Bei englischen Klauseln Begriffe erklären, aber deutsches GrESt-Recht als maßgeblich markieren.

## Praktischer Tipp

- "Transfer Taxes" in englischen SPAs ist ein loser Begriff; deutsche GrESt immer mit "real estate transfer tax (Grunderwerbsteuer)" definieren und das anwendbare deutsche Recht ausdrücklich vorsehen, auch wenn der SPA englischem Recht unterliegt.
- Streitkontrolle (control of tax proceedings) muss den Käufer mindestens als Joinder vorsehen, weil das Finanzamt sich an den Käufer als Steuerschuldner halten kann (§ 13 GrEStG, gesamtschuldnerische Haftung). Wenn der Verkäufer den Einspruch allein führt, kommt der Käufer ohne Mitwirkungsrecht in die Haftung.
- Escrow-Höhe bei Signing/Closing-Doppelfestsetzungsrisiko: typisch 150 bis 200 % der berechneten GrESt der jeweils zweifelhaften Festsetzung, weil Zinsen nach § 233a AO (6 % bis 2018, danach 1,8 % p.a. nach Neuregelung) hinzukommen können.

## Trade-off: Indemnity vs. Garantie

| Pfad | Vorteil | Nachteil |
|---|---|---|
| Tax Indemnity (verschuldensunabhängig) | klare Allokation, einfache Durchsetzung | breite Haftungsschulter Verkäufer |
| Tax Warranty (Garantie) | passt in W&I-Versicherung | Kausalität und Schadenhöhe streitig |
| Specific Indemnity nur für identifiziertes Risiko | gezielt, deal-freundlich | nur für DD-bekannte Themen |

Empfehlung: Allgemeine Tax Indemnity für unbekannte Altrisiken + Specific Indemnity für DD-Findings + Escrow für streitige laufende Festsetzungen.

## Beispiel-Mustertext (Indemnity-Kern)

> Der Verkäufer stellt den Käufer von sämtlicher Grunderwerbsteuer einschließlich Säumniszuschlägen, Zinsen und Nebenleistungen frei, die auf Erwerbsvorgänge vor dem Closing zurückgeht oder bei der die Tatbestandsverwirklichung vor dem Closing eingetreten ist. Die Freistellung umfasst auch Doppelfestsetzungen aufgrund auseinanderfallender Signing-/Closing-Stichtage. Der Käufer informiert den Verkäufer unverzüglich, spätestens binnen [10] Werktagen, über Anzeigen, Auskunftsersuchen, Bescheide oder Klagen; der Verkäufer ist berechtigt, die Verteidigung auf eigene Kosten zu übernehmen, der Käufer wirkt loyal mit.

## Typische Fehler

- "Käufer trägt alle Steuern aus der Transaktion" deckt Alt-GrESt nicht (keine "Transaktionssteuer"). Klare Cut-off-Klausel mit Datum nötig.
- Grundbesitzliste fehlt oder ist nicht aktuell zum Closing-Datum; spätere Streitigkeiten über Bemessungsgrundlage und Belegenheitsfinanzamt.

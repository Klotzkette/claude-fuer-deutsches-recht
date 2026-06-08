---
name: grest-spa-tax-clause-indemnity
description: "GrESt im SPA vertraglich absichern: Tax Covenant, GrESt-Indemnity, Käufer-/Verkäufertragung, Signing-Closing-Doppelrisiko, Escrow, Mitwirkungspflichten, Anzeigen, Grundbesitzliste und Post-Closing-Steuerklauseln."
---

# GrESt: SPA-Klauseln, Indemnity und Escrow

## Fachlicher Anker

- **Normen:** § 6a, § 19, § 13.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Aufgabe

Hilf beim Entwurf oder Review von GrESt-Klauseln in Unternehmenskaufverträgen. Der Skill ist für deutsche oder deutsch-englische M&A-Praxis gedacht.

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

## Output

- Klauselkommentar in Deal-Sprache.
- Tax Covenant-Vorschlag auf Deutsch oder Englisch.
- Indemnity-Matrix.
- Closing Deliverables.
- Escrow- und Cooperation-Baustein.

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

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

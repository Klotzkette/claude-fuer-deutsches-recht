---
name: aussenwirtschaftsembargo
description: "Prüfung der Einhaltung des Aussenwirtschaftsrechts in Mandantenstrukturen — AWG AWV Dual-Use-Verordnung und EU-Sanktionsregime sowie strafrechtliche Konsequenzen § 17 AWG. Anwendungsfall Mandant exportiert in sanktionierten Drittstaat oder erhaelt eine Anfrage zur Bereitstellung von Vermoegen an..."
---

# Aussenwirtschaftsrecht — AWG und Sanktionen

## Fachlicher Anker

- **Normen:** § 6a, § 17, § 18.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Triage — kläre vor der Bearbeitung

1. Ist die Ware Listenposition oder Catch-all (Dual-Use)?
2. Wer ist Endempfaenger und wo ist der Verwendungsort?
3. Liegt eine EU-Sanktion gegen Person Schiff Land oder Sektor vor?
4. Ist eine Genehmigung erforderlich und wurde sie eingeholt?
5. Drohstrafrechtlich § 17 § 18 AWG; Compliance-Maßnahmen umgesetzt?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 17 AWG** — strafbare Handlungen.
- **§ 18 AWG** — Vergehen.
- **§ 4 AWG** — Beschraenkungen.
- **Dual-Use-Verordnung EU 2021/821**.
- **EU-Sanktionsverordnungen** — z. B. Russland Iran Nordkorea.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 4 AWG · § 17 AWG · § 18 AWG · § 19 AWG · AWV · VO EU 2021/821 (Dual-Use) · § 30 OWiG

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 8 AO (Wohnsitz, Aufenthalt)
- §§ 33, 34 AO (Steuerpflichtiger, gesetzliche Vertreter)
- § 42 AO (Gestaltungsmissbrauch)
- §§ 169-171 AO (Festsetzungsverjährung)
- §§ 233a, 235 AO (Verzinsung, Hinterziehungszinsen)
- § 370 AO (Steuerhinterziehung)
- §§ 153, 371 AO (Berichtigungserklärung, Selbstanzeige)
- §§ 15, 32a EStG (Einkünfte aus Gewerbebetrieb, Tarif)
- § 8 KStG, § 7 GewStG (Einkommen, Gewerbeertrag)
- §§ 1, 15 UStG (Steuerbare Umsätze, Vorsteuerabzug)

### Leitentscheidungen

- BFH I R 36/18 (Hinzurechnungsbesteuerung AStG)
- BFH XI R 11/22 (Reverse-Charge-Verfahren)
- BFH IX R 49/13 (Liebhaberei vs. Einkunftserzielungsabsicht)
- BVerfG 2 BvL 1/03 (Steuerfreistellung Existenzminimum)
- EuGH C-280/10 (Vorsteuerabzug bei wirtschaftlicher Tätigkeit)

### Anwendung im Skill

- Beraterhaftung gegen Mandantenpflicht (§§ 153, 154 AO) klar trennen; Selbstanzeige nach § 371 AO ist eine Strafnorm, kein Steueroptimierungs-Tool.
- Festsetzungsverjaehrung nach §§ 169-171 AO im Zweifel zugunsten des Steuerpflichtigen; Hemmung durch Aussenpruefung beachten.
- Bei Gestaltungsmissbrauch § 42 AO immer alternative Wirtschaftsgruende dokumentieren.

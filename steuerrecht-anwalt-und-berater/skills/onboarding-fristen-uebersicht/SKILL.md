---
name: onboarding-fristen-uebersicht
description: "Systematische Uebersicht aller wesentlichen Steuerrechts-Fristen — Einspruch Klage Revision Beschwerde Wiedereinsetzung Verjährung Festsetzungsfrist Zahlungsverjaehrung Aussenpruefung Selbstanzeige. Anwendungsfall Anwalt oder Steuerberater muss bei Mandatsuebernahme in Minuten klären welche Fris..."
---

# Steuerrechtliche Fristen — der Überblick

## Fachlicher Anker

- **Normen:** § 6a, § 122 Abs. 2 AO, § 122a AO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Triage — kläre vor der Bearbeitung

1. Welches Schriftstueck loest die Frist aus (Bescheid, Einspruchsentscheidung, Urteil, Verfuegung)?
2. Wann ist die Zustellung bewirkt (§ 122 Abs. 2 AO Drei-Tages-Fiktion; § 122a AO Bereitstellung im ELSTER-Postfach)?
3. Faellt das Fristende auf Wochenende oder Feiertag (§ 108 Abs. 3 AO)?
4. Wurde die Frist bereits versaeumt? Prüfen ob Wiedereinsetzung § 110 AO oder § 56 FGO greift.
5. Gibt es Hemmungstatbestaende (Aussenpruefung § 171 AO; vorläufige Festsetzung § 165 AO)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 108 AO** — Fristenberechnung; Verweis auf §§ 187 ff. BGB.
- **§ 122 AO / § 122a AO** — Bekanntgabe und elektronische Bereitstellung.
- **§ 355 AO** — Einspruchsfrist ein Monat.
- **§ 47 FGO** — Klagefrist ein Monat ab Einspruchsentscheidung.
- **§ 110 AO / § 56 FGO** — Wiedereinsetzung in den vorigen Stand.
- **§§ 169 ff. AO** — Festsetzungsverjaehrung.
- **§§ 228 ff. AO** — Zahlungsverjaehrung fuenf Jahre; Hemmung und Unterbrechung.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 108 AO · § 122 AO · § 122a AO · § 355 AO · § 47 FGO · § 110 AO · § 56 FGO · §§ 169 ff. AO · §§ 228 ff. AO · § 171 AO (Ablaufhemmung)

## Fristenmatrix (Schnellzugriff)

| Verfahrensschritt | Frist | Rechtsgrundlage | Wiedereinsetzung |
| --- | --- | --- | --- |
| Einspruch gegen Steuerbescheid | 1 Monat ab Bekanntgabe | § 355 AO | § 110 AO |
| Klage zum Finanzgericht | 1 Monat ab Einspruchsentscheidung | § 47 FGO | § 56 FGO |
| Revision zum BFH | 1 Monat ab FG-Urteil | § 120 FGO | § 56 FGO |
| Nichtzulassungsbeschwerde | 1 Monat ab FG-Urteil | § 116 FGO | § 56 FGO |
| AdV-Antrag beim FA | jederzeit waehrend Einspruch | § 361 AO | nicht erforderlich |
| AdV-Antrag beim FG | jederzeit waehrend Klage | § 69 FGO | nicht erforderlich |
| Selbstanzeige (Sperrwirkung) | bis Bekanntgabe Prüfungsanordnung | § 371 Abs. 2 AO | nicht möglich |
| Festsetzungsfrist regulaer | 4 Jahre | § 169 Abs. 2 Nr. 2 AO | n.a. |
| Festsetzungsfrist Hinterziehung | 10 Jahre | § 169 Abs. 2 S. 2 AO | n.a. |
| Zahlungsverjaehrung | 5 Jahre | § 228 AO | n.a. |

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

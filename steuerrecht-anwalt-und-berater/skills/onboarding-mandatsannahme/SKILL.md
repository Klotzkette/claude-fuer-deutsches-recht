---
name: onboarding-mandatsannahme
description: "Erstgespraech-Leitfaden für steuerrechtliche Mandate. Anwendungsfall Mandant kommt mit Bescheid Prüfungsanordnung oder Vorladung; Anwalt oder Steuerberater muss in 30 Minuten Sachverhalt Fristen und Risiko klären. Behandelt Mandantenfragebogen Interessenkonflikt § 43a BRAO § 57 StBerG Vollmacht..."
---

# Mandatsannahme im Steuerrecht — Erstgespraech und Risiko-Triage

## Fachlicher Anker

- **Normen:** § 6a, § 355 AO, § 47.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Triage — kläre vor der Bearbeitung

1. Verfahrensstadium klären: Veranlagung, Einspruch, Klage, Aussenpruefung, Steuerstrafverfahren, Vollstreckung?
2. Welcher Bescheid oder welche Verfuegung liegt vor (Datum, Zustellungsdatum, Aktenzeichen, Steuerart)?
3. Frist sofort errechnen: Einspruch § 355 AO ein Monat, Klage § 47 FGO ein Monat, AdV § 361 AO formlos.
4. Interessenkonflikt § 43a Abs. 4 BRAO bzw. § 57 Abs. 1 StBerG prüfen (gegenlaeufige Mandate, Konzern, Ehegatten).
5. Steuerstrafrechtlicher Anfangsverdacht? Dann Belehrung nach § 393 AO und ggf. Schweigen empfehlen.
6. Wer ist Mandant: natuerliche Person, Personengesellschaft, Kapitalgesellschaft, Insolvenzverwalter, Erbe?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 43a BRAO** — anwaltliche Grundpflichten; Verschwiegenheit, Interessenkollision.
- **§ 57 StBerG** — Grundpflichten des Steuerberaters; unabhaengige eigenverantwortliche Berufsausuebung.
- **§§ 80 ff. AO** — Vollmachtswirkung im Besteuerungsverfahren.
- **§ 62 FGO** — Prozessvollmacht vor dem Finanzgericht.
- **§ 49b BRAO / § 64 StBerG / RVG / StBVV** — Honorarvereinbarungen, gesetzliche Gebühren.
- **§ 393 AO** — Verhältnis Besteuerungs- zu Strafverfahren; nemo tenetur.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 43a BRAO · § 57 StBerG · §§ 80 ff. AO · § 62 FGO · § 393 AO · § 355 AO (Einspruchsfrist) · § 47 FGO (Klagefrist) · § 49b BRAO · § 64 StBerG · RVG · StBVV

## Praxisformulierung / Antragsmuster

```
VOLLMACHT (steuerrechtliches Mandat)

Ich/Wir, [MANDANT], Steuernummer [NR], bevollmaechtige(n)
Herrn/Frau Rechtsanwalt/Steuerberater [NAME], Kanzlei [KANZLEI],
in der Steuerangelegenheit betreffend [STEUERART] [VERANLAGUNGSZEITRAUM]
gegenueber dem Finanzamt [ORT] sowie der Finanzgerichtsbarkeit
umfassend zur Vertretung, insbesondere zur:
- Akteneinsicht (§ 364 AO, § 78 FGO)
- Einlegung von Rechtsbehelfen (Einspruch, Klage, Revision, Beschwerde)
- Antraegen auf Aussetzung der Vollziehung (§ 361 AO, § 69 FGO)
- Entgegennahme von Bescheiden und Schriftstuecken (§ 122 Abs. 1 S. 4 AO)
- Verhandlungsfuehrung mit dem Finanzamt und Vereinbarungen tatsaechlicher Verstaendigung

[ORT, DATUM] [UNTERSCHRIFT]
```

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

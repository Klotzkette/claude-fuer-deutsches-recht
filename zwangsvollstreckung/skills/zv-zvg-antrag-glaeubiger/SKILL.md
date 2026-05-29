---
name: zv-zvg-antrag-glaeubiger
description: "Gläubiger hat Grundschuld oder Hypothek und will Immobilie des Schuldners versteigern lassen. ZVG Zwangsversteigerungsgesetz. Prüfraster: Antrag Anordnung §§ 15 ff. ZVG Beitritt § 27 ZVG geringstes Gebot Bargebot Verteilungstermin vorheriges Recht eintragen Zwangshypothek § 866 ZPO. Output: ZVG-Antrag Gläubiger und Versteigerungs-Strategie. Abgrenzung zu zv-notarielle-urkunde-grundschuld (Titelgrundlage) und zv-zvg als allgemeines Zwangsversteigerungsrecht."
---

# ZVG-Antrag (Zwangsversteigerung / Zwangsverwaltung)

## Aufgabe

Vollstreckung in das Grundstück. Wird in der Regel parallel zur PfÜB betrieben. Dieser Skill steuert ausschließlich die Gläubigerseite; der Schwesterskill `zwangsverwaltung-zvg` betrifft die Verwalterperspektive.

## Startet bei

- Titel + Klausel + Zustellung grün
- Grundstück im Eigentum des Schuldners (oder dinglich gegen Eigentümer nach § 800 ZPO)
- Vorzugsweise eingetragene Grundschuld – sonst Zwangshypothek § 866 ZPO erforderlich

## Rechtsgrundlagen

- §§ 15-145 ZVG – Zwangsversteigerung
- §§ 146-161a ZVG – Zwangsverwaltung
- § 27 ZVG – Beitritt
- § 30a ZVG – Schuldnerschutz Einstellung
- § 765a ZPO – Vollstreckungsschutz
- § 866 ZPO – Sicherungshypothek (bei persönlichem Titel)
- § 867 ZPO – Verfahren der Eintragung
- § 49 InsO – Absonderungsrecht
- § 10 ZVG – Rangklassen
- § 28 GBO – Bestimmtheit

## Workflow

1. **Vollstreckungsgrundlage**: dinglicher Titel (Grundschuld in Verbindung mit Unterwerfungsurkunde – siehe `zv-notarielle-urkunde-grundschuld`) oder persönlicher Titel + Zwangshypothek § 866 ZPO.
2. **Grundbucheinsicht** vor jedem Antrag – aktuell, weil sich Rangverhältnisse verändert haben können.
3. **Zwangshypothek § 866 ZPO eintragen**, wenn nur persönlicher Titel: Antrag beim Grundbuchamt, Forderung mindestens 750 EUR (§ 866 Abs. 3 ZPO), nach Eintragung sechs Monate warten? Nein – Eintragung selbst genügt; die sechs Monate betreffen die Wartepflicht bei Hypothek § 1147 BGB nicht.
4. **Antrag auf Anordnung** der Zwangsversteigerung beim Vollstreckungsgericht (Amtsgericht der belegenen Sache).
5. **Beitritt § 27 ZVG**, wenn bereits Verfahren läuft – einfacher, kostengünstiger.
6. **Geringstes Gebot** und Bargebot prüfen: alle vorrangigen Rechte plus 7/10 Verkehrswert – sonst Wertgrenzen § 85a ZVG.
7. **Zwangsverwaltung** als Alternative oder Parallelverfahren: Mieten und Pachten fließen über Verwalter an Gläubiger.
8. **Schuldnerschutzanträge** des Schuldners erwarten (§ 30a ZVG, § 765a ZPO) – Stellungnahme vorbereiten.
9. **Verteilungstermin** § 105 ZVG: Erlös wird nach Rangklassen § 10 ZVG verteilt.

## Wertgrenzen § 85a ZVG

- Im ersten Termin wird kein Zuschlag erteilt, wenn das Meistgebot unter 50 % des Verkehrswerts liegt.
- Zwischen 50 % und 70 % kann auf Antrag des Berechtigten Zuschlag versagt werden.
- Ab dem zweiten Termin entfallen die Grenzen.

## Insolvenz des Schuldners

- § 49 InsO: dinglich gesicherter Gläubiger ist absonderungsberechtigt.
- Die Zwangsversteigerung kann vom Insolvenzverwalter nach § 30d ZVG eingestellt werden.
- Verwertung durch den Verwalter ist häufig wirtschaftlicher.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
ZVG-ANTRAG [Mandant] gegen [Schuldner], AG [Belegenheitsgericht]

Titel:                 [Art, Datum]
Grundbuch:             [Ort, Bl, Flurst, Lage]
Eigentümer:            [Schuldner / Dritter § 800 ZPO]
Rangstelle:            [Abt. III, lfd Nr / Zwangshypothek § 866 erforderlich]
Vorrangige Rechte:     EUR x (Bank, Steuer, sonstige)
Verkehrswert:          EUR y (Schätzung)
Geringstes Gebot:      ~ EUR z
Verfahrenstyp:         Versteigerung / Verwaltung / beides
Beitritt § 27 möglich? [ja, AG Az / nein]

NÄCHSTER SCHRITT:      Anordnung beim AG / Beitritt
WIEDERVORLAGE:         DD.MM.JJJJ
```

## Qualitätsgates

- Niemals ohne aktuelle Grundbucheinsicht antragen.
- Bei persönlichem Titel: Zwangshypothek vorher eintragen.
- Wertgrenzen § 85a ZVG beachten – im ersten Termin kann Zuschlag versagt werden.
- Bei Insolvenz § 30d ZVG mitdenken.
- Bei selbstgenutztem Wohneigentum § 765a ZPO mit Härtefall-Vortrag rechnen.

## Querverweise

- `zv-notarielle-urkunde-grundschuld`
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt` (parallel)
- `zwangsverwaltung-zvg` – Verwalterperspektive (anderes Plugin)
- `zv-abwehr-schuldner`
- `insolvenzforderungsanmeldungspruefung/ifap-tabellenauszug-178`

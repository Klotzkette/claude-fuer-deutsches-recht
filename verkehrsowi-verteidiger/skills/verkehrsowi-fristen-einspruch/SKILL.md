---
name: verkehrsowi-fristen-einspruch
description: "Einspruchsfrist im OWi-Verfahren berechnen und wahren: Drohende Rechtsbestandskraft des Bussgeldbescheids. Normen: § 67 OWiG (Einspruch 2 Wochen ab Zustellung), §§ 33 OWiG, 177-182 ZPO (Zustellungsfiktion), § 52 OWiG (Wiedereinsetzung), § 74 OWiG (Verwerfung bei Versaeumnis). Pruefraster: Zustellungsdatum und -art, Fristberechnung, Beschraenkter Einspruch § 67 Abs. 2 OWiG (nur Fahrverbot). Output Fristenblatt, Einspruchs-Template, ggf. Wiedereinsetzungsantrag. Abgrenzung: Inhalt des Einspruchs siehe verkehrsowi-beweisverwertung-standardisiert; Rechtsbeschwerde siehe verkehrsowi-rechtsbeschwerde."
---

# Einspruchsfrist und Einspruch — § 67 OWiG

## Triage zu Beginn

1. **Wann wurde der Bussgeldbescheid zugestellt?** — Ausgangspunkt der 2-Wochen-Frist § 67 Abs. 1 OWiG.
2. **Zustellungsform?** — Persoenliche Uebergabe, Einwurf-Einschreiben (§§ 33 OWiG, 180 ZPO), PZU.
3. **Mandant kennt Zugangsdatum?** — Falls unsicher: Zustellungsfiktion pruefen; fuer Mandanten spaetestes bekanntes Datum nehmen.
4. **Frist bereits abgelaufen?** — Wiedereinsetzungsantrag nach § 52 OWiG pruefen.
5. **Beschraenkt oder unbeschraenkt einlegen?** — § 67 Abs. 2 OWiG: Beschraenkung auf Rechtsfolgen moeglich.

## Zentrale Normen

- **§ 67 Abs. 1 OWiG** — Einspruch: 2 Wochen ab Zustellung des Bussgeldbescheids
- **§ 67 Abs. 2 OWiG** — Beschraenkter Einspruch auf Rechtsfolgen (Geldbusse, Fahrverbot)
- **§ 33 OWiG** — Zustellungsvorschriften: entsprechende Anwendung ZPO
- **§ 52 OWiG** — Wiedereinsetzung in den vorigen Stand nach § 44 StPO entsprechend
- **§ 74 OWiG** — Verwerfung des Einspruchs bei unentschuldigtem Ausbleiben
- **§ 28 OWiG** — Bekanntmachung des Bussgeldbescheids; Fristbeginn

## Aktuelle Rechtsprechung

- OLG Celle, Beschl. v. 23.06.2020 - 3 Ss OWi 72/20, NZV 2020, 523 — Fehlerhafte Zustellungsurkunde fuehrt zu spaeterem Fristbeginn; Einspruch noch zulaessig wenn tatsaechliche Kenntnis spaeter erlangt.
- OLG Hamm, Beschl. v. 14.06.2021 - 5 RVs 43/21, NZV 2021, 531 — Zustellungsfiktion nach § 180 ZPO gilt auch im OWi-Verfahren; spaetere Kenntnisnahme bedarf konkreter Darlegung.
- BVerfG, Beschl. v. 26.04.2023 - 2 BvR 310/23, NJW 2023, 1951 — Zugang zu Wiedereinsetzungsmitteln muss tatsaechlich gewahrt werden; uebertrieben formale Anforderungen verstoessen gegen Art. 2 Abs. 1 GG.
- OLG Koblenz, Beschl. v. 17.11.2020 - 1 OWi 6 SsBs 65/20, NZV 2021, 156 — Verwerfung nach § 74 OWiG erfordert tatsaechlich unentschuldigtes Ausbleiben; Gericht muss Entschuldigungsgruende vorab pruefen.

## Kommentarliteratur

- Goehler OWiG § 67 Rn. 1-25 (Einspruch, Frist, Beschraenkung)
- Goehler OWiG § 52 Rn. 1-15 (Wiedereinsetzung)
- KK-OWiG / Lutz § 67 Rn. 1-20 (vollstaendige Kommentierung)
- KK-OWiG / Mitsch § 74 Rn. 1-15 (Verwerfung)

## Fristen-Berechnungsschema

```
Zustellungsdatum: [DATUM]
+ 14 Tage:        [DATUM + 14 Tage]
= Fristende:      [DATUM]

Besonderheiten:
- Fristende Samstag/Sonntag/Feiertag → naechster Werktag (§ 43 StPO)
- Zustellungsfiktion § 180 ZPO: Einwurf-Einschreiben = 3 Tage nach Aufgabe
- Mandant im Urlaub/Krankenhaus → Wiedereinsetzungsgruende pruefen
```

## Entscheidungsbaum

```
Frist noch offen?
├─ Ja → Einspruch sofort formulieren und einlegen
│   ├─ Beschraenkt (nur Rechtsfolgen)? → § 67 Abs. 2 OWiG
│   └─ Unbeschraenkt → Standardvorgehen
└─ Nein (Frist abgelaufen)
    ├─ Kein Verschulden? → Wiedereinsetzung § 52 OWiG
    │   ├─ Krankheit, Urlaub, Fehler der Behoerde
    │   └─ Eidesstattliche Versicherung + gleichzeitiger Einspruch
    └─ Verschulden → Bussgeldbescheid rechtskraeftig; Vollstreckung abwenden
```

## Output-Template Einspruchsschreiben

```
An die [Bussgeldstelle] / Amtsgericht [ORT]
Az.: [AKTENZEICHEN]

Einspruch nach § 67 OWiG

Namens des Betroffenen [NAME] lege ich gegen den Bussgeldbescheid
vom [DATUM DES BESCHEIDS], zugegangen am [ZUSTELLUNGSDATUM],
form- und fristgerecht

Einspruch

ein.

[Falls beschraenkt: Der Einspruch wird auf die festgesetzten
Rechtsfolgen beschraenkt. § 67 Abs. 2 OWiG.]

Ich bitte um Uebersendung der vollstaendigen Verfahrensakte
einschliesslich Messakte.

Anlage: Vollmacht [NAME]

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Frist unmittelbar nach Mandatsuebernahme berechnen und im Kalender eintragen.
- 3-Tage-Vorlauffrist-Erinnerung setzen.
- Beschraenkter Einspruch nur nach Mandantenruecksprache.
- Anwaltliche Endkontrolle vor dem Versand.

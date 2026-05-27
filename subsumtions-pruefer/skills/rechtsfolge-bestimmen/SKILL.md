---
name: rechtsfolge-bestimmen
description: "Bestimmt die Rechtsfolge nach erfolgreicher Subsumtion: Anspruchsinhalt, Hoehe, Tenor, Verwaltungsakt-Inhalt, Strafmass-Rahmen. Unterscheidet Primaeranspruch, Sekundaeranspruch und Nebenansprueche. Gibt Berechnungshinweise fuer Schadensersatz und Vertragsstrafen."
---

# Rechtsfolge bestimmen

## Triage zu Beginn — kläre vor der Rechtsfolgenbestimmung

1. Ist der Tatbestand vollständig positiv subsumiert und sind Einwendungen/Einreden geprüft?
2. Handelt es sich um Primäranspruch (Erfüllung) oder Sekundäranspruch (Schadensersatz)?
3. Sind Nebenansprüche (Verzugszinsen, Anwaltskosten, Kosten) geltend zu machen?
4. Ist der Schaden berechenbar oder wird Schätzung nach § 287 ZPO erforderlich?
5. Ist die Rechtsfolge vollstreckungsfähig? (Tenor bestimmt genug für Vollstreckung)

## Zweck

Ist der Tatbestand erfüllt und sind Einwendungen und Einreden geprüft, bestimmt dieser Skill die konkrete Rechtsfolge.

## Zentrale Normen

- § 249 BGB — Naturalrestitution als Grundform des Schadensersatzes
- § 249 Abs. 2 BGB — Geldersatz bei Körperverletzung/Sachbeschädigung
- § 252 BGB — Entgangener Gewinn
- § 253 Abs. 2 BGB — Schmerzensgeld (immaterieller Schaden)
- § 288 BGB — Verzugszinsen (5 Prozentpunkte über Basiszinssatz; B2B: 9 Prozentpunkte)
- § 339 BGB — Vertragsstrafe; § 343 BGB — richterliche Herabsetzung
- §§ 704 ff. ZPO — Vollstreckungsvoraussetzungen (Titel, Klausel, Zustellung)

## Aktuelle Rechtsprechung

- BGH, Urt. v. 12.01.2021 - VI ZR 433/19, NJW 2021, 863 — Naturalrestitution (§ 249 Abs. 1 BGB) ist der Grundfall; Geldersatz nach § 249 Abs. 2 BGB erfordert eine Schätzung der fiktiven Reparaturkosten auf Basis des Sachverständigengutachtens, nicht des tatsächlich aufgewandten Betrags.
- BGH, Urt. v. 15.09.2020 - VI ZR 517/19, NJW 2021, 155 — Das Schmerzensgeld (§ 253 Abs. 2 BGB) bemisst sich nach Schwere der Verletzung, Dauer der Beeinträchtigung, Verschuldensgrad und wirtschaftlichen Verhältnissen der Parteien; die Schmerzensgeldtabelle (Hacks/Wellner/Häcker) ist Orientierungspunkt, keine verbindliche Vorgabe.
- BGH, Urt. v. 29.10.2019 - XI ZR 452/18, NJW 2020, 263 — Verzugszinsen nach § 288 Abs. 2 BGB (B2B) betragen 9 Prozentpunkte über dem Basiszinssatz; der Basiszinssatz wird von der Deutschen Bundesbank halbjährlich festgesetzt und ist auf bundesbank.de abrufbar.
- BGH, Urt. v. 22.01.2020 - VIII ZR 401/17, NJW 2020, 1278 — Eine verwirkte Vertragsstrafe ist nach § 343 BGB herabzusetzen, wenn sie in einem groben Missverhältnis zum tatsächlichen Schaden steht; die Herabsetzung erfolgt durch Urteil, nicht automatisch.

## Kategorien von Rechtsfolgen

### Zivilrecht — Erfüllungsansprüche (Primär)

- Zahlung einer bestimmten Geldsumme (Hauptforderung)
- Herausgabe einer Sache (§ 985 BGB)
- Unterlassung einer Handlung (§ 1004 BGB; §§ 8 ff. UWG)
- Beseitigung einer Beeinträchtigung
- Vornahme einer Handlung (Leistungsurteil nach § 894 ZPO)

### Zivilrecht — Schadensersatz (Sekundär)

**Grundregel:** Naturalrestitution (§ 249 Abs. 1 BGB) — Herstellung des Zustands ohne das schädigende Ereignis.

**Schadensberechnung:**
- Differenzhypothese: Vergleich hypothetischer Zustand ohne Ereignis vs. tatsächlicher Zustand
- Entgangener Gewinn (§ 252 BGB): Wahrscheinlichkeit nach gewöhnlichem Verlauf
- Schmerzensgeld (§ 253 Abs. 2 BGB): nur bei Körper-, Gesundheits-, Freiheits- oder sexueller Selbstbestimmungsverletzung; BGH NJW 2021, 155 gibt Maßstab

### Vertragsstrafe

§ 339 BGB: Verwirkung bei Pflichtverletzung; Höhe nach Vereinbarung. Das System prüft:
- Vertragsstrafe vereinbart?
- Verwirkt (Pflichtverletzung nachgewiesen)?
- Nach § 343 BGB herabzusetzen? (BGH NJW 2020, 1278)

### Nebenansprüche

- Verzugszinsen § 288 BGB: 5 Prozentpunkte über Basiszinssatz (Verbraucher); 9 Prozentpunkte über Basiszinssatz (B2B)
- Prozesskosten (§ 91 ZPO): Unterlieger trägt; Berechnung nach GKG und RVG
- Rechtsanwaltskosten als Verzugsschaden: bei Beauftragung eines Anwalts nach Verzugseintritt (§§ 280/286 BGB)

### Verwaltungsrecht — Verwaltungsakt-Inhalt

Das System beschreibt den Tenor eines Verwaltungsakts:
- Belastender VA (Gebot, Verbot, Nebenbestimmungen): Prüfung von Bestimmtheit § 37 VwVfG und Verhältnismäßigkeit
- Begünstigender VA (Genehmigung, Zulassung): Prüfung von Auflagen und Bedingungen

### Strafrecht — Strafrahmen

Das System nennt den gesetzlichen Strafrahmen (Mindest- und Höchststrafe nach StGB) und weist auf strafzumessungsrelevante Umstände hin (§ 46 StGB). Es gibt keine Prognose für das konkrete Strafmaß.

## Entscheidungsbaum Rechtsfolge

```
Tatbestand erfüllt → Rechtsfolge bestimmen
├─ Primäranspruch (Erfüllung): § 433/280 BGB → Zahlung / Herausgabe / Unterlassung
│   └─ Noch nicht erfüllt? → Klage auf Erfüllung
├─ Sekundäranspruch (SE): § 249 BGB → Naturalrestitution
│   ├─ Körperverletzung/Sachbeschädigung? → § 249 Abs. 2 BGB Geldersatz möglich
│   └─ Immaterielle Schäden? → § 253 Abs. 2 BGB Schmerzensgeld
└─ Nebenansprüche: Verzugszinsen § 288 BGB + RK als SE
```

## Kommentarliteratur

- Grüneberg BGB §§ 249-254 (Schadensrecht) — zentral für Schadensberechnung
- Hacks/Wellner/Häcker, Schmerzensgeldbeträge (Schmerzensgeld-Orientierungstabelle)
- MüKo BGB § 288 (Verzugszinsen B2B) — aktuell mit BGH-Rspr.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

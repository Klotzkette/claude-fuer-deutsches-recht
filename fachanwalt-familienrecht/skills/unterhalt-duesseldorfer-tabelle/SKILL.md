---
name: unterhalt-duesseldorfer-tabelle
description: "Kindes- und Ehegattenunterhalt nach Duesseldorfer Tabelle berechnen: Praktische Berechnungsaufgabe mit konkreten Einkommensdaten. Normen: §§ 1601 ff. BGB, § 1605 BGB (Selbstauskunft), § 1613 BGB (Verzug). Prüfraster: Bereinigtes Nettoeinkommen (5%-Pauschale Berufsaufwendungen, Schulden, Vorsorge, Krankenversicherung), Selbstbehalt, Mangelfaelle, Erwerbstätigenbonus, Halbteilungsgrundsatz, fiktives Einkommen. Output Unterhalts-Berechnung Schritt für Schritt. Abgrenzung: Strategische Beratung siehe fachanwalt-familienrecht-unterhaltsberechnung; Abbaenderungsklage siehe fachanwalt-familienrecht-duesseldorfer-tabelle-unterhalt."
---

# Unterhalt nach Düsseldorfer Tabelle

## Zweck

Konkrete Berechnung von Kindesunterhalt, Trennungsunterhalt und nachehelichem Unterhalt — das Kernwerkzeug der familienrechtlichen Praxis.

## Eingaben

- Nettoeinkommen Unterhaltsschuldner (zwölf Monatsabrechnungen plus Jahressonderzahlungen)
- Nettoeinkommen Unterhaltsberechtigter (bei Ehegattenunterhalt)
- Anzahl und Alter der Kinder
- Vorsorgeaufwendungen Krankenversicherung Berufsunfähigkeit
- Schulden mit Tilgungsplan (nur ehebedingte oder berufsbedingte regelmäßig anerkannt)
- Berufsbedingte Aufwendungen (Pauschale fünf Prozent oder Einzelnachweis)
- Wohnvorteil bei selbstgenutzter Immobilie

## Berechnungsraster Kindesunterhalt

### Schritt 1 — Bereinigtes Nettoeinkommen

```
Bruttoeinkommen
- Lohnsteuer Soli Kirchensteuer
- Sozialversicherung
- Berufsbedingte Aufwendungen (fünf Prozent pauschal max EUR 150 pro Monat)
- Krankenversicherung (privat oder gesetzlicher Anteil)
- Altersvorsorge (bis vier Prozent Brutto plus gesetzlich)
- Anerkannte Verbindlichkeiten
= bereinigtes Nettoeinkommen
```

### Schritt 2 — Tabellenstufe

Die Düsseldorfer Tabelle (Fassung aktuelles Jahr) staffelt nach Einkommen und Alter:

- Altersstufe 1: null bis fünf Jahre
- Altersstufe 2: sechs bis elf Jahre
- Altersstufe 3: zwölf bis siebzehn Jahre
- Altersstufe 4: ab achtzehn Jahre

Mindestunterhalt 2026 nach § 1612a BGB (ab 01.01.2026): EUR 486 (0-5), EUR 558 (6-11), EUR 653 (12-17). Rechtsgrundlage: Siebte Mindestunterhaltsverordnung vom 15.11.2024 (BGBl. 2024 I Nr. 359). Aktuelle Tabelle stets über olg-duesseldorf.nrw.de verifizieren.

### Schritt 3 — Kindergeld-Anrechnung

- Beim minderjährigen Kind hälftige Anrechnung auf Barunterhalt (§ 1612b Abs. 1 BGB).
- Beim volljährigen Kind volle Anrechnung.

### Schritt 4 — Selbstbehalt

- Notwendiger Selbstbehalt gegenüber minderjährigen Kindern und privilegierten Volljährigen
- Angemessener Selbstbehalt gegenüber nicht privilegierten Volljährigen und Ehegatten

**Stand Düsseldorfer Tabelle 2026 (ab 01.01.2026):** Selbstbehalt unverändert ggü. 2025; notwendiger Selbstbehalt ggü. minderjährigen Kindern EUR 1.450 erwerbstätig / EUR 1.200 nichterwerbstätig (Quelle: OLG Düsseldorf, Pressemitteilung vom 01.12.2025). Sätze gegenüber Ehegatten und volljährigen Kindern der aktuellen Tabelle entnehmen.

Bei Unterschreitung des Selbstbehalts Mangelfallberechnung mit anteiliger Quotelung aller Unterhaltsansprüche.

## Trennungsunterhalt § 1361 BGB

### Halbteilungsgrundsatz

```
Trennungsunterhalt = drei Siebtel (Erwerbstaetigenbonus eingerechnet)
des Differenz-Nettoeinkommens
```

Beim Erwerbstaetigenbonus: jeweils ein Siebtel des eigenen Erwerbseinkommens bleibt frei.

### Bedarfsdeckung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Eigeneinkommen anrechnen.
- Wohnvorteil bewerten.

## Nachehelicher Unterhalt §§ 1569 ff. BGB

### Anspruchsgrundlagen

- § 1570 Betreuungsunterhalt (Kind unter drei Jahre Basisanspruch)
- § 1571 Alter
- § 1572 Krankheit
- § 1573 Erwerbslosigkeit / Aufstockung
- § 1575 Ausbildungsunterhalt

### Befristung und Herabsetzung § 1578b BGB

- Ehebedingte Nachteile prüfen
- Dauer der Ehe
- Pflege gemeinsamer Kinder
- Karriere-Knick

### Erwerbsobliegenheit

- Nach Trennungsphase Erwerbsobliegenheit prüfen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Auskunftsanspruch § 1605 BGB

- Beidseitig alle zwei Jahre
- Belege: Lohnsteuerbescheinigung Steuerbescheid Selbstständige drei Jahresabschlüsse
- Bei Selbstauskunfts-Verweigerung Stufenklage § 254 ZPO

## Verzug § 1613 BGB

- Rückwirkend nur ab Aufforderung zur Auskunft / Zahlung
- Daher früh und schriftlich auffordern (Mahnschreiben mit Auskunftsanforderung)

## Sonderbedarf und Mehrbedarf

- Mehrbedarf (Kindergarten Nachhilfe Krankenkosten) zusätzlich
- Sonderbedarf (Konfirmation Klassenfahrt) einmalig § 1613 Abs. 2 BGB

## Ausgabe

- `unterhaltsberechnung.md` mit jeder Berechnungsstufe nachvollziehbar
- Bedarfsrechner-Tabelle pro Berechtigtem
- Selbstbehaltsprüfung mit Mangelfall-Logik
- Fristen-Eintrag für nächste Auskunftsanfrage
- Quellenverzeichnis: aktuelle Düsseldorfer Tabelle (2026, OLG Düsseldorf, Pressemitteilung 01.12.2025), BGH XII. Zivilsenat (z.B. BGH XII ZB 148/24 vom 22.01.2025 zum Elternunterhalt-Selbstbehalt), Wendl/Dose

## Hinweis

Detaillierte Sonderfälle (Auslandsbezug fiktives Einkommen Selbstständige Wohnvorteil PKW-Nutzung GmbH-Geschäftsführer-Gehalt) erfordern Fachanwalts-Expertise.

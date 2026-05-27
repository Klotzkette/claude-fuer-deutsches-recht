---
name: zvg-mieteinzug-rueckstaende
description: "Mieteinzug und Rueckstandsbehandlung in der Zwangsverwaltung. Anwendungsfall Mieter zahlt nicht und Zwangsverwalter muss Rueckstande einziehen oder Klage einleiten. Normen § 152 ZVG Mieteinzugspflicht § 543 BGB fristlose Kuendigung § 286 BGB Verzug. Pruefraster Soll-Ist-Abgleich Mahnung Ratenvereinbarung Klage Zahlungseingang Kontoabgleich Dokumentation. Output Rueckstandsprotokoll mit Mahnhistorie Klagepruefung und Einzugsnachweis fuer Rechnungslegung. Abgrenzung zu zvg-miet-und-pachtverwaltung und zvg-raeumung-kuendigung."
---

# Mieteinzug und Rückstände

## Aufgabe

Sichert laufende Nutzungen und treibt Rückstände mit sauberem Soll-Ist-Abgleich ein.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Mieteinnahmen fehlen
- Rückstände vor oder nach Beschlagnahme bestehen
- Zahlungen nicht zugeordnet werden können

## Eingaben

- Rent Roll, Kontoauszüge, Mieterkonten
- Rückstandsliste, Mahnungen, Einwendungen
- Mietverträge und Betriebskostenstände

## Workflow

1. **Soll-Ist-Abgleich** - Sollmieten je Einheit mit Zahlungseingängen und Altrückständen matchen.
2. **Rückstände trennen** - beschlagnahmte Nutzungen, Altansprüche und streitige Posten unterscheiden.
3. **Mahnen** - freundliche Zahlungserinnerung, Mahnung, Ratenplan oder Klagevorschlag erstellen.
4. **Gericht berichten** - wesentliche Rückstände und Einziehungsmaßnahmen dokumentieren.

## Ausgabe

- Rückstandsliste
- Mahn- und Klagepaket
- Zahlungsabgleich

## Qualitätsgates

- jede Zahlung einer Einheit zugeordnet
- Alt- und Neurückstände getrennt
- Einwendungen protokolliert

## Rote Schwellen

- Dauerleerstand
- Mietminderung ohne Prüfung
- Kontoauszug fehlt

## Interne Vorlagen

- assets/templates/mieteinzug-rueckstaende.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- § 8 ZwVwV
- § 13 ZwVwV

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 10.05.2007 - IX ZB 23/06, NZI 2007, 546 Rn. 17 — Der Zwangsverwalter ist berechtigt, Mietrückstände einzuklagen; er muss dabei zwischen Rückständen aus der Zeit vor Beschlagnahme (Altforderungen des Schuldners) und Rückständen nach Beschlagnahme (Masseforderungen) unterscheiden.
- BGH, Beschl. v. 12.01.2006 - IX ZB 239/04, NZI 2006, 234 Rn. 13 — Unterlässt der Zwangsverwalter die Einziehung von Mietrückständen schuldhaft, haftet er persönlich für den entstehenden Schaden; eine zeitnahe Mahnung und ggf. Klage ist Pflicht.

## Paragrafenkette Mieteinzug/Rückstände

§ 153 ZVG (Einziehung Nutzungen) → § 535 Abs. 2 BGB (Mietzinszahlungspflicht) → § 543 Abs. 2 Nr. 3 BGB (Kündigung wegen Zahlungsverzug) → § 286 BGB (Verzug) → § 288 BGB (Verzugszinsen) → §§ 12-13 ZwVwV (Buchführung Rückstände)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 153 Rn. 20-45 (Mieteinzug)
- Böttcher ZVG 6. Aufl., § 153 Rn. 30-50 (Rückstände und Einzug)
- Schmidt-Futterer Mietrecht 15. Aufl., § 543 BGB Rn. 80-120 (Kündigung Zahlungsverzug)

## Triage Mieteinzug/Rückstände

1. Rückstand vor oder nach Beschlagnahme entstanden? (Unterschiedliche Behandlung)
2. Hat der Mieter Einwendungen gegen die Miethöhe erhoben? (Minderung § 536 BGB prüfen)
3. Liegen mehr als zwei Monatsmieten Rückstand vor? (Außerordentliche Kündigung § 543 BGB prüfen)
4. Ist Klage wirtschaftlich sinnvoll? (Insolvenzrisiko des Mieters, Vollstreckbarkeit prüfen)

## Output-Template Mahn-/Kündigungsschreiben ZVG

**Adressat:** rückständiger Mieter — Tonfall scharf-fristsetzend

```
[ZWANGSVERWALTER]
EINSCHREIBEN MIT RÜCKSCHEIN

An [MIETER NAME]
[ADRESSE]

Zwangsverwaltung [ADRESSE], AZ [X]

Mahnung und Fristsetzung / Außerordentliche Kündigung

Sehr geehrte/r Herr/Frau [NAME],

folgende Mietrückstände sind aufgelaufen:
Monat | Betrag | Status
[TABELLE]
Gesamtrückstand: [BETRAG] EUR

Ich fordere Sie auf, den Rückstand bis zum [DATUM] zu zahlen.
[Falls Kündigung: Gleichzeitig kündige ich das Mietverhältnis fristlos nach
§ 543 Abs. 2 Nr. 3 BGB wegen Zahlungsverzugs von mehr als zwei Monatsmieten.
Bitte übergeben Sie die Wohnung spätestens zum [DATUM] geräumt.]

[UNTERSCHRIFT ZWANGSVERWALTER]
```

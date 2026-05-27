---
name: stb-susa-saldennullstellung-jahresende
description: "Erfolgskonten-Saldennullstellung zum Jahresende. Anwendungsfall Jahresabschluss-Vorbereitung Schluss-SuSa GuV-Ueberleitung Bilanzgewinn auf Konto 800 oder 2000. Methodik Abschlussbuchungen ueber GuV-Konto. Output Geschlossene Erfolgskonten Bilanzgewinn ueberfuehrt."
---

# Erfolgskonten-Saldennullstellung zum Jahresende

## Kernsachverhalt

Zum Jahresende muessen die Erfolgskonten (Klasse 4-8 SKR 03, Klasse 4-7 SKR 04) auf null gestellt werden — ihr Saldo wird ueber das GuV-Konto in den Bilanzgewinn ueberfuehrt. Dieser Vorgang heisst Saldennullstellung oder GuV-Abschluss und ist Standardprozess zum Bilanzstichtag. Die DATEV/Addison-Systeme erledigen das automatisch beim Wirtschaftsjahres-Wechsel, aber der Steuerberater muss das Ergebnis dokumentieren und pruefen.

## Kaltstart-Rueckfragen

1. Welcher Stichtag — 31. Dezember oder abweichendes Wirtschaftsjahr?
2. Ist die laufende Buchfuehrung bis Jahresende abgeschlossen?
3. Sind alle Jahresabschluss-Buchungen erfasst (Periodenabgrenzung, Rueckstellungen, AfA, Inventur)?
4. Welche Rechtsform — Bilanzgewinn auf Konto 2000 (GmbH) oder 800 (Einzelunternehmer)?
5. Welche Verwendung Bilanzgewinn — Thesaurierung, Ausschuettung, Verlustvortrag?
6. Liegt Gesellschafterbeschluss zur Ergebnisverwendung vor?
7. Welche steuerlichen Korrekturen sind zu erwarten (Mehr- oder Wenigergewinn vs. Steuerbilanz)?
8. Welche Konto-Schlussbestand Pruefung (alle Bestandskonten Endsaldo dokumentiert)?

## Rechtlicher Rahmen

### Primaernormen

**§§ 242, 264 HGB** — Aufstellungspflicht Jahresabschluss; Schlussbilanz.

**§ 268 Abs. 1 HGB** — Bilanzgewinn-Ausweis.

**§ 246 HGB** — Vollstaendigkeit.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 5 EStG** — Massgeblichkeit Handels- fuer Steuerbilanz.

**§ 11 EStG** — Zufluss-Abfluss-Prinzip (bei EUER).

### Standards

- IDW PS 480.
- DATEV/Addison Jahreswechsel-Module.

## Workflow

### Phase 1 — Vor-Pruefung Jahresend-Schluss

- Alle laufenden Belege Dezember verbucht?
- Periodenabgrenzung gebucht (RAP)?
- Rueckstellungen gebucht?
- Anlagenspiegel und AfA aktualisiert?
- Bestandsfeststellung (Inventur) durchgefuehrt?
- Saldenabstimmung Hauptbuch-Nebenbuch?

### Phase 2 — Erfolgskonten saldieren

```
SCHLIESSUNG ERFOLGSKONTEN GuV:
Soll                                         Haben
Konto 8000-8999 (Erloese, SKR 03)            Konto 9999 GuV-Sammelkonto
Konto 4000-4999 (Aufwand, SKR 03)            Konto 9999 GuV-Sammelkonto

Nach Schliessung:
Saldo Konto 9999 (Gewinn/Verlust) → Konto 2000 (Bilanzgewinn) [GmbH]
                                  oder 800 (Kapital) [Einzel]
                                  oder 3010 (Privat) [Personenges.]
```

### Phase 3 — DATEV-Automatik

- DATEV Jahreswechsel-Lauf: schliesst Erfolgskonten automatisch.
- Bei manueller Korrektur in DATEV: Berater-Funktion.
- Bei Addison: vergleichbare Automatik.

### Phase 4 — Pruefung Konsistenz

- Schluss-SuSa: alle Erfolgskonten Saldo 0?
- Bilanzkonten: Endsalden mit Bilanzpositionen abgestimmt?
- GuV-Sammelkonto Saldo = Jahresergebnis?

### Phase 5 — Vortrag Bilanzgewinn

- Eroeffnungsbilanz Folgejahr: Konto 2000 (GmbH) zeigt Vorjahres-Bilanzgewinn.
- Bei Gesellschafterbeschluss-Ausschuettung: Buchung erst nach Beschluss (oft Mai/Juni Folgejahr).
- Vortrag in Bilanzposten "Gewinnvortrag" oder "Verlustvortrag".

### Phase 6 — Dokumentation

- Jahresabschluss-Mappe mit Schlussbilanz und GuV.
- Schluss-SuSa als Beleg fuer Schliessung.
- Eroeffnungsbilanz Folgejahr (analytisch).

## Output

- Schluss-SuSa mit allen Erfolgskonten auf null.
- Bilanzgewinn ueberfuehrt auf Konto 2000 (GmbH) bzw. 800/3010.
- Eroeffnungsbilanz Folgejahr vorbereitet.

## Strategie und Praxis-Tipps

- Erfolgskonten-Schliessung ist der Schluss-Stempel des Jahres. Spaetere Aenderungen muessen ueber Vorperioden-Korrekturen laufen.
- Bei wesentlichen Nachtraegen in der Pruefung: ggf. erneut schliessen.
- Bilanzgewinn-Verwendung erst nach Gesellschafterbeschluss buchen.
- Bei Personenunternehmen: Privatentnahmen und -einlagen ueber das Jahr separat — werden in Kapitalkonto verrechnet.
- StBVV: Jahresabschluss-Erstellung StBVV § 35 — gesonderter Auftrag.
- DATEV-Tipp: Jahreswechsel mit DATEV-Berater-Lauf; manuelle Korrekturen nur ueber Berater-Funktion.

## Querverweise

- `stb-susa-erstellen-grundlagen` — SuSa-Grundlagen.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-bestandskonten-abstimmung` — Bestandskonten-Abstimmung.
- `stb-jahresabschluss-handels-vs-steuerbilanz` — Massgeblichkeit.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 242, 246, 252, 264, 268.
- EStG §§ 5, 11.
- StBVV § 35.
- IDW PS 480.

---
name: stb-susa-monatlich-quartalsweise
description: "Periodische SuSa-Erstellung monatlich oder quartalsweise. Anwendungsfall standardisierter Erstellungsprozess Wahl der Periodizitaet Belegvolumen Mandantengroesse. Methodik Wahl der Frequenz Kommunikations-Routine. Output Periodische SuSa mit Dokumentation."
---

# Periodische SuSa-Erstellung — Monat oder Quartal

## Kernsachverhalt

Wie haeufig die SuSa erstellt wird, haengt von Belegvolumen, Mandantengroesse und steuerlichen Pflichten ab. USt-pflichtige Mandanten mit monatlicher Voranmeldung brauchen monatliche SuSa als Grundlage. Kleinmandanten ohne monatliche USt-VA koennen quartalsweise oder halbjaehrlich erstellt werden. Der Steuerberater legt die Periodizitaet im Mandantenstamm fest und richtet entsprechende Auswertungslaeufe ein.

## Kaltstart-Rueckfragen

1. Welche USt-Voranmeldungspflicht — monatlich, vierteljaehrlich, jaehrlich, befreit?
2. Welches Belegvolumen monatlich (Anzahl Buchungen)?
3. Welche externen Verpflichtungen — Bank-Reporting, Investor-Reporting, Konzern-Reporting?
4. Welche Mandantenwuensche (oft monatliche BWA = monatliche SuSa)?
5. Welche Buchhaltungs-Kapazitaet in der Kanzlei?
6. Welche Sondersituation — Krise, Sanierung, Pruefung?
7. Welche Wirtschaftsjahr-Konfiguration (Kalender vs. abweichend)?
8. Welche Dokumentationspflicht (intern, Pruefer, Mandant)?

## Rechtlicher Rahmen

### Primaernormen

**§ 18 UStG** — USt-Voranmeldung; bestimmt Pflicht zur monatlichen oder vierteljaehrlichen Erfassung.

**§ 146 AO** — Zeitgerechtigkeit; Buchungen "in der Regel binnen 10 Tagen", spaetestens Monatsende.

**§ 90 AO** — Mitwirkungspflicht Mandant (Belegabgabe).

**§ 33 StBerG** — StB-Aufgabenkreis.

### Standards

- BMF v. 28.11.2019 zu GoBD.
- DATEV/Addison Standard-Auswertungslaeufe.

## Workflow

### Phase 1 — Periodizitaets-Wahl

| Mandantentyp | Empfohlene Frequenz |
|---|---|
| USt-monatliche VA, Mittelstand | Monatliche SuSa |
| USt-vierteljaehrliche VA, KMU | Quartalsweise SuSa |
| USt-jaehrliche VA, Kleinunternehmer | Halbjahres- oder Jahres-SuSa |
| Sanierungsmandat, Krise | Monatliche SuSa, ggf. 14-taegig |
| Konzern-Reporting | Monatliche SuSa (Standard) |

### Phase 2 — DATEV-Konfiguration

- Mandantenstamm: Periodizitaet eintragen (Monat/Quartal).
- Auswertungslauf in DATEV Kanzlei-Rechnungswesen einrichten.
- Auswertungstermin (z.B. immer am 25. des Folgemonats) im Termincontrolling.
- Datev-Buchungsbelegfreigabe bis Tag 15 des Folgemonats.

### Phase 3 — Monatsrhythmus

```
Tag 5 des Folgemonats:    Belegannahme abgeschlossen
Tag 15:                   Buchung abgeschlossen
Tag 20:                   Periodenabgrenzung gebucht
Tag 22:                   SuSa-Vorabauswertung
Tag 25:                   SuSa final, BWA versandfertig
Tag 30:                   USt-VA uebermittelt
```

### Phase 4 — Quartalsrhythmus

```
Tag 5 nach Quartalsende:  Belegannahme letzter Monat abgeschlossen
Tag 25:                   SuSa Quartal final
Tag 30:                   BWA Quartal versandt
```

### Phase 5 — Sondersituationen

- Bei Saisonbetrieb: zusaetzliche SuSa nach Saisonende.
- Bei Sanierungsmandat: 14-taegig wenn von Bank verlangt.
- Bei Aussenpruefung: SuSa des Pruefzeitraums zusammenstellen.

### Phase 6 — Dokumentation

- Erstellungsprotokoll in Mandantenakte (Datum, Bearbeiter, Bemerkungen).
- Versandprotokoll bei externem Empfaenger.
- Wiedervorlage fuer Folgemonat/Folgequartal.

## Output

- Periodische SuSa als PDF.
- Excel-Export fuer interne Auswertung.
- Erstellungsprotokoll in Mandantenakte.

## Strategie und Praxis-Tipps

- Monatliche SuSa ist Standard fuer USt-pflichtige Mandanten — auch wenn die VA quartalsweise ist (Kontinuitaet, Krisenfrueherkennung).
- Quartalsweise SuSa nur bei klar einfacheren Mandanten.
- Bei Buchungsverzoegerung Mandanten in Mandantenakte dokumentieren — Haftungsfrage bei Versand verspaeteter Auswertungen.
- StBVV: Periodische Erstellung in Buchfuehrungspauschale.
- Eskalation bei wiederholten Verzoegerungen: Honorarzuschlag oder Mandatsanpassung.
- DATEV-Tipp: DATEV-Kanzleiplaner mit automatischen Termin-Erinnerungen.

## Querverweise

- `stb-susa-erstellen-grundlagen` — SuSa-Grundlagen.
- `stb-bwa-monatsabschluss-routine` — Monatsabschluss.
- `stb-routine-monatsabschluss-30-tage-zyklus` — 30-Tage-Zyklus.
- `stb-routine-quartalsabschluss-prozess` — Quartalsabschluss-Prozess.

## Quellen und Updates

Stand: 05/2026.

- UStG § 18.
- AO §§ 90, 146.
- HGB § 238.
- StBerG § 33.
- BMF v. 28.11.2019 zu GoBD.

---
name: susa-kreditorenliste-ova
description: "Kreditoren-Saldenliste OVA Offene-Verbindlichkeiten-Auswertung. Anwendungsfall Monats- oder Quartalsauswertung Zahlungsdisposition Lieferanten-Analyse Bilanzvorbereitung. Methodik Fälligkeitsstaffel Top-Lieferanten Skonti-Optionen. Output Kreditoren-Liste mit Fälligkeit Zahlungsempfehlung."
---

# Kreditoren-Saldenliste (OVA) — Offene Verbindlichkeiten

## Fachlicher Anker

- **Normen:** § 6a, § 17 InsO, § 246 HGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Die Kreditoren-Saldenliste zeigt alle Verbindlichkeiten gegenueber Lieferanten. Sie ist Grundlage für Zahlungsdisposition, Skonti-Optimierung, Bilanzvorbereitung und Krisenfrueherkennung. Ueberfaellige Lieferantenverbindlichkeiten sind klassisches Indiz für Liquiditaetsstockung (§ 17 InsO). Der Steuerberater erstellt sie monatlich und gibt Hinweise auf Zahlungsdringlichkeit und Skonti-Vorteile.

## Kaltstart-Rueckfragen

1. Welcher Stichtag — Monatsende, Quartalsende, Bilanzstichtag?
2. Welche Top-Lieferanten sind kritisch (Just-in-Time-Lieferung, Monopolist)?
3. Welche Skonti-Konditionen sind ueblich (2 Prozent in 10 Tagen)?
4. Welche Faelligkeit ist Ziel-Zahlungsdauer (z.B. 30 Tage netto)?
5. Welche Lieferanten haben gestundete Posten?
6. Welche Lieferanten mit Liefersperre gedroht?
7. Welche Steuer- oder SV-Verbindlichkeiten sind separat zu pruefen?
8. Welche Mandantenkontingenz für Zahlungsdisposition?

## Rechtlicher Rahmen

### Primaernormen

**§ 246 HGB** — Vollstaendigkeit; alle Verbindlichkeiten zu erfassen.

**§ 253 HGB** — Bewertung mit Erfuellungsbetrag.

**§ 17 InsO** — Zahlungsunfaehigkeit; ueberfaellige Verbindlichkeiten sind Indiz.

**§ 266a StGB** — Vorenthaltung SV-Beitraege (Strafbarkeit GF).

**§ 102 StaRUG** — Hinweispflicht.

### Standards

- IDW PS 480.
- DATEV OPOS-Modul.

## Workflow

### Phase 1 — Datenbasis

- OP-Liste aus DATEV/Addison/Sage.
- Lieferantenstammdaten mit Zahlungskonditionen.
- Bankvalutadaten (offene Ueberweisungen, geplante Zahlungen).
- Liquiditaetsplan (3-Wochen-Sicht).

### Phase 2 — Aufbau OVA

```
KREDITOREN-OPOS-LISTE
Stichtag: [Datum]

Konto Lieferant Saldo EUR Faelligkeit Skonti-Frist Bemerkung
70001 [Lieferant A] 8.500 In 5 Tagen Skonti -2% Skonti bis [Datum]
70002 [Lieferant B] 12.000 Ueberfaellig — Liefersperre droht
70003 [Lieferant C] 2.300 In 25 Tagen — Normal
...
SUMME [X]
```

### Phase 3 — Faelligkeitsstaffel

| Staffel | Anteil | Handlung |
|---|---|---|
| Skonti-Frist (in 5-10 Tagen) | [X Prozent] | Sofort zahlen (Skonti-Gewinn) |
| Nicht faellig (10-30 Tage) | [Y Prozent] | Im Plan |
| Faellig (0-15 Tage ueberfaellig) | [Z Prozent] | Sofort zahlen |
| Ueber 15 Tage ueberfaellig | [A Prozent] | Krisensignal; mit Lieferanten klaeren |
| Ueber 30 Tage ueberfaellig | [B Prozent] | Drohende Liefersperre; § 17 InsO-Indiz |

### Phase 4 — Skonti-Optimierung

- Skonti-Pruefung: Skonti 2 Prozent in 10 Tagen vs. 30 Tage netto = effektive Verzinsung 36 Prozent p.a.
- Bei ausreichender Liquiditaet: Skonti immer nutzen.
- Bei knapper Liquiditaet: Skonti-Optimum berechnen (Skonti-Wert vs. Zinskosten Kontokorrent).

### Phase 5 — Steuer- und SV-Verbindlichkeiten

- Finanzamt-Verbindlichkeiten: USt, KSt, ESt-Vorauszahlung, GewSt-Vorauszahlung.
- Faellige FA-Schulden: Saeumniszuschlag § 240 AO (1 Prozent pro Monat).
- SV-Verbindlichkeiten an Krankenkassen: ueberfaellig = § 266a StGB-Risiko für GF.
- Bei drohenden SV-Rueckstaenden: dringende Eskalation an GF (Querverweis stb-warnschreiben-krisensignale).

### Phase 6 — Reporting

- Kreditoren-Liste monatlich an Mandant.
- Zahlungsempfehlung mit Skonti-Hinweis.
- Bei ueberfaelligen SV-Beitraegen: dringende Warnung.

## Output

- Kreditoren-OPOS-Liste mit Faelligkeitsstaffel.
- Zahlungsempfehlung mit Skonti-Optimierung.
- Krisensignal-Hinweis bei ueberfaelligen FA/SV-Schulden.

## Strategie und Praxis-Tipps

- Skonti sind oft die guenstigste Finanzierungsform — Verzinsung 36-72 Prozent p.a. Aequivalent.
- Bei knapper Liquiditaet trotzdem Kernlieferanten zuerst (Lieferkette nicht abreissen lassen).
- SV-Beitraege haben absolute Prioritaet — § 266a StGB-Risiko.
- Bei ueber 90 Tage ueberfaelligen Lieferantenrechnungen: § 17 InsO-Indiz; Hinweispflicht § 102 StaRUG ausgeloest.
- StBVV: OPOS-Auswertung in Buchfuehrungspauschale; Zahlungsdisposition optional Zusatzauftrag.
- DATEV-Tipp: DATEV-Zahlungstrager mit Skonti-Faelligkeitspruefung.

## Querverweise

- `stb-susa-debitorenliste-osa-offene-posten` — Debitoren-OPOS.
- `stb-susa-saldenabstimmung-bestaetigung` — Saldenabstimmung.
- `stb-liquiditaetsvorschau-3wochen` — 3-Wochen-Liquiditaet.
- `stb-warnschreiben-krisensignale` — Krisensignal.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignale.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 246, 253.
- InsO § 17.
- StGB § 266a.
- AO § 240.
- StaRUG § 102.
- IDW PS 480.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

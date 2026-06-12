---
name: bwa-kontenrahmen-skr03-skr04
description: "Vergleich Kontenrahmen SKR 03 versus SKR 04 für BWA-Erstellung. Anwendungsfall Mandantenneuaufnahme oder Wechsel des Kontenrahmens Entscheidungsgrundlage Industrie Handel Dienstleistung. Aufbau Bilanz vs Prozess Gliederung GKV vs UKV. Output Empfehlung welcher Kontenrahmen Migrationsanleitung Que..."
---

# Kontenrahmen SKR 03 vs SKR 04 — Wahl und Bedeutung für BWA

## Fachlicher Anker

- **Normen:** § 6a, § 267 HGB, § 4 Abs. 3 EStG.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

DATEV bietet zwei Standardkontenrahmen an. SKR 03 ist prozessorientiert (Wareneinkauf 3000er, Aufwand 4000er, Erloese 8000er). SKR 04 ist abschlussorientiert (Aktiva 0xxx-2xxx, Passiva 3xxx, Ertrag 4xxx, Aufwand 5xxx-7xxx). Die Wahl beeinflusst die BWA-Struktur, die Schnittstellen zur E-Bilanz und die Mandantenkommunikation. Bei Neuaufnahme eines Mandanten muss der Steuerberater bewusst waehlen; ein Wechsel des Kontenrahmens im laufenden Geschäftsjahr ist nur ausnahmsweise sinnvoll.

## Kaltstart-Rueckfragen

1. Welche Mandantenstruktur — Industrie, Handel, Dienstleistung, Freiberufler, Holding?
2. Welche Rechtsform und Groessenklasse (§ 267 HGB) — Kleinst-, Klein-, mittelgrosse oder große Kapitalgesellschaft?
3. Welche Mandanten in der Kanzlei nutzen bereits welchen SKR? (Konsistenz im Kanzleibetrieb.)
4. Wird der Mandant bilanziert oder erfolgt EUER nach § 4 Abs. 3 EStG?
5. Welche Schnittstellen sind vorgesehen — DATEV Unternehmen Online, BuchhaltungsButler, sevDesk, Lexware?
6. Welches Lohnprogramm liefert Personalkosten-Buchungen — DATEV LODAS, Lohn und Gehalt, externer Provider?
7. Welche Berichts- und Reporting-Anforderungen — Konzernanforderung, internationale Eigentümer mit UKV-Wunsch?
8. Plant der Mandant einen Branchenvergleich (DATEV Branchenbericht) — Vergleichbarkeit setzt Kontenrahmen voraus.

## Rechtlicher Rahmen

### Primaernormen

**§ 238 HGB** — Buchfuehrungspflicht; Kontenrahmen ist Wahlrecht, muss aber stetig sein (§ 252 Abs. 1 Nr. 6 HGB).

**§ 252 Abs. 1 Nr. 6 HGB** — Bewertungsstetigkeit; gilt analog für Kontenrahmen-Wechsel.

**§ 5b EStG** — E-Bilanz-Taxonomie; SKR 03 und SKR 04 sind beide kompatibel, aber die Brueckenkonten unterscheiden sich.

**§ 275 HGB** — Gliederung GuV; GKV nach § 275 Abs. 2 HGB / UKV nach § 275 Abs. 3 HGB. SKR 03 unterstuetzt traditionell GKV, SKR 04 ist offener für UKV.

### Verwaltungsanweisungen und Standards

- DATEV-Kontenrahmen-Dokumentation (jaehrliche Updates).
- IDW RS HFA 38 — Gliederungsgrundsaetze nach HGB.
- BMF v. 28.09.2011 (BStBl I 2011, 855) — E-Bilanz-Taxonomie; jaehrliche Anpassung durch BMF-Schreiben. Aktuelle Version ist die Taxonomie 6.9 (BMF-Schreiben April 2025, verpflichtend für WJ ab 01.01.2026); aktuelle Fassung über esteuer.de abrufbar.

## Workflow

### Phase 1 — Bestandsaufnahme

- Aktuelle Buchhaltung des Mandanten sichten — welcher Kontenrahmen wird derzeit genutzt? Bei Mandantenwechsel: Vorberaterkontenrahmen prüfen.
- Branche und Geschäftsmodell erfassen; bei produzierendem Gewerbe SKR 03 ueblich, bei dienstleistenden GmbH zunehmend SKR 04.
- Anforderungen externer Stakeholder prüfen (Banken, Konzern-Mutter, Wirtschaftspruefer).

### Phase 2 — Entscheidung treffen

| Kriterium | SKR 03 | SKR 04 |
|---|---|---|
| Sortierung | Prozessorientiert (Beschaffung, Produktion, Absatz) | Abschlussorientiert (Bilanz und GuV nach HGB-Gliederung) |
| Branche | Industrie, Handwerk, traditioneller Handel | Dienstleistung, Holding, freie Berufe, kapitalmarkt-naher Mittelstand |
| GuV-Form | GKV (typisch) | UKV (typisch), aber auch GKV möglich |
| E-Bilanz | Voll unterstuetzt | Voll unterstuetzt (Brueckenkonten differierend) |
| Internationale Vergleichbarkeit | Geringer | Hoeher (Naehe zu IFRS-Strukturen) |

### Phase 3 — Umsetzung

- Neue Mandanten: Kontenrahmen im DATEV-Stammdaten/Addison-Stammdaten festlegen; Bestaetigung im Mandantenstammblatt.
- Wechsel bestehender Mandanten: Nur zum Jahreswechsel, mit Eroeffnungsbilanz-Umbuchung. Wechsel waehrend des Jahres vermeidet § 252 Abs. 1 Nr. 6 HGB.
- Stammkontenliste mit individuellen Konten ergaenzen (Branchen-Sachkonten, Gesellschafterkonten).

### Phase 4 — Schnittstellen prüfen

- Lohnbuchhaltungs-Schnittstelle (DATEV-Buchungsbelege) — Kontenrahmen muss matchen.
- BWA-Konfiguration (Form 01, 11, 21) — die Standard-Forms sind für beide SKR vorbereitet, aber individualisierte Forms müssen angepasst werden.
- Branchenvergleich DATEV BBE — nur für Standard-SKR und Standard-Konten zuverlaessig.

### Phase 5 — Kommunikation an Mandanten

- Bei Wechsel: Mandant über Periode der Umstellung informieren; Auswirkungen auf BWA-Vorjahresvergleich erklaeren.
- Bei Erst-Einrichtung: kurze schriftliche Begruendung der Wahl in Mandantenakte.

## Strategie und Praxis-Tipps

- Mandanten mit Wachstumsabsicht und kapitalmarkt-naher Ausrichtung tendieren zu SKR 04; mittelstaendische Industriebetriebe bleiben oft bei SKR 03.
- Innerhalb der Kanzlei moeglichst konsistent — Mandantensachbearbeiter können sonst nicht effizient wechseln.
- DATEV-BBE-Branchenvergleich liefert die besten Daten für SKR 03 mit Standardkonten; bei SKR 04 ist die Datenbasis duenner.
- Honorar für Kontenrahmen-Wechsel separat im Zusatzauftrag aufnehmen (StBVV §§ 33, 35), nicht in der laufenden Buchhaltung.
- Bei Holding-Strukturen mit verschiedenen Tochtergesellschaften: gleicher Kontenrahmen in allen Einheiten erleichtert Konsolidierung.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252, 275.
- EStG § 5b.
- DATEV-Kontenrahmen SKR 03 und SKR 04 (Stand 2026).
- BMF v. 28.09.2011, BStBl I 2011, 855 (E-Bilanz-Grundsaetze); jaehrliche Taxonomie-Aktualisierung: aktuelle Version 6.9 (WJ ab 01.01.2026), abrufbar unter esteuer.de.
- IDW RS HFA 38.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 2 bestaetigt (E-Bilanz Taxonomie 6.9 für WJ 2026 bestaetigt, esteuer.de-Quelle angegeben) -->

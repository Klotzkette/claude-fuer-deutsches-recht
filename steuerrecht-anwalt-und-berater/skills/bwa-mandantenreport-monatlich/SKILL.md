---
name: bwa-mandantenreport-monatlich
description: "Monatlicher Mandantenreport zusammenführend aus BWA SuSa OPOS Lohn Liquiditaet. Anwendungsfall standardisierter Monatsreport an Mandant per Mail oder Portal. Methodik 4-Seiten-Vorlage Cover BWA Kennzahlen Empfehlung. Output Mandantenreport als PDF Querverweis stb-routine-monatsabschluss-30-tage-zyklus."
---

# Monatlicher Mandantenreport

## Fachlicher Anker

- **Normen:** § 6a, § 33, § 57.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Ein Mandantenreport ist die kuratierte Aufbereitung aller Auswertungen eines Monats: BWA, Kennzahlen, OPOS-Status, Lohnsumme, Liquiditaetsstand. Statt 5 einzelne PDFs erhaelt der Mandant ein 4-Seiten-Dokument: Cover mit Hauptaussagen, BWA-Block, Kennzahlen-Block, Empfehlungsblock. Der Report standardisiert die Kanzlei-Kommunikation, erhoeht die Mandantenbindung und reduziert Rueckfragen.

## Kaltstart-Rueckfragen

1. Welcher Mandant — Solo, KMU, Mittelstand?
2. Welche Detailtiefe — Standard (4 Seiten) oder erweitert (10 Seiten)?
3. Welche Kennzahlen sind dem Mandanten wichtig?
4. Welche Zusatzthemen einmonatlich (USt, Lohn, Investition)?
5. Liegt eine Mandanten-CI vor (Logo, Farbe)?
6. Welche Anrede (Sie/Du; gendergerecht)?
7. Welcher Versandkanal — E-Mail mit PDF-Anhang, DATEV Unternehmen Online, gedruckt per Post?
8. Welche Eskalation bei Krisensignalen (markiert, Anschreiben)?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 57 StBerG** — Gewissenhaftigkeit.

**§ 102 StaRUG** — Hinweispflicht; im Monatsreport zu kommunizieren.

**§ 90 AO** — Mitwirkungspflicht Mandant; im Report Massnahmen-Plan.

**DSGVO Art. 32** — Sicherheit der Verarbeitung; verschluesselte Uebertragung.

### Standards

- DStV-Praxisleitfaden Mandantenkommunikation.
- BStBK Berufsrichtlinien.
- IDW PS 480.

## Workflow

### Phase 1 — Standard-Struktur

```
SEITE 1: COVER
- Mandantenlogo (links oben)
- Berichtsperiode (Monat / Jahr)
- 3 Hauptaussagen ("Auf einen Blick")
- Ampel-Status (Gruen/Gelb/Rot)
- Inhaltsverzeichnis

SEITE 2: BWA-BLOCK
- BWA-Hauptzahlen (5 Bloecke + Ergebnis)
- Vorjahresvergleich
- Kumulierter Jahresvergleich
- Erlaeuterung wesentliche Abweichungen

SEITE 3: KENNZAHLEN-BLOCK
- Liquiditaet 1./2./3. Grades
- EBIT-/EBITDA-Marge
- Eigenkapitalquote
- Branchenvergleich (falls verfuegbar)
- OPOS-Uebersicht (Top-Forderungen, Top-Verbindlichkeiten)

SEITE 4: EMPFEHLUNGSBLOCK
- 3-5 Handlungsempfehlungen
- Massnahmen-Tabelle mit Verantwortlich/Termin
- Eskalationen (Krisensignale, Hinweise)
- Anschluss-Termine (naechste Auswertung, Quartalsgespraech)
- Kontaktdaten Steuerberater
```

### Phase 2 — Datenintegration

- BWA aus DATEV/Addison ueber Export.
- Kennzahlen aus Kennzahlen-Modul.
- OPOS aus OP-Verwaltung.
- Lohn aus Lohnprogramm.
- Liquiditaet aus Liquiditaetsplanung.

### Phase 3 — Cover-Aussagen formulieren

- 3 Hauptaussagen pro Monat (z.B. "Umsatz plus 12 Prozent gegenueber Vorjahr", "Personalkostenquote stabil bei 38 Prozent", "Liquiditaet 1. Grades stabil bei 18 Prozent").
- Klar, kurz, nicht ueber-positiv (Vertrauensbildung durch Realismus).
- Bei Krisensignalen: Hauptaussage rot markiert.

### Phase 4 — Empfehlungsblock

- Konkret und umsetzbar.
- Mit Verantwortlichkeit (Mandant, StB, Bank).
- Mit Termin (z.B. "bis 15. Folgemonat klaeren").
- Keine Rechtsberatung (§ 5 RDG).

### Phase 5 — Layout und Versand

- Einheitliche Vorlage (PowerPoint oder Word-Template).
- Mandantenlogo eingebunden.
- PDF-Export verschluesselt.
- Versand via DATEV Unternehmen Online oder E-Mail mit Passwort.

### Phase 6 — Feedback und Iteration

- Monatlich Mandanten-Feedback einsammeln.
- Iteratives Verbessern des Reports.
- Standardisierung in der Kanzlei (Template-Library).

## Output

- 4-seitiger Mandantenreport als PDF.
- Versandprotokoll im Mandantenakte.
- Wiedervorlage für Folgemonat.

## Strategie und Praxis-Tipps

- Standardisierter Report ist Kanzlei-Differenzierungsmerkmal — viele Steuerberater versenden noch nackte BWA, der Report hebt sich ab.
- Template-Library pflegen: 3-5 Varianten je nach Mandantentyp (Solo, KMU, Mittelstand).
- Bei wesentlichen Aenderungen Mandant per Telefon kurz vorabinformieren.
- StBVV: Reportgestaltung Zusatzauftrag oder Pauschalvereinbarung; nicht in Standard-Buchfuehrungspauschale.
- DATEV-Tipp: DATEV Praesentation-Modul mit Vorlagen; bei Vollindividualisierung Excel/PowerPoint.
- Mandantenwunsch in Erstgespraech klaeren: Detailtiefe, Frequenz, Versandkanal.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-erlaeuterungstext-mandant` — Erlaeuterungstext.
- `stb-routine-monatsabschluss-30-tage-zyklus` — Monatsabschluss-Routine.
- `stb-bwa-mandantengespraech-uebergabe` — Quartalsgespraech.
- `stb-mandantenkommunikation-bwa-uebergabe-quartal` — Quartalsbesprechung.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- StaRUG § 102.
- DSGVO Art. 32.
- DStV-Praxisleitfaden Mandantenkommunikation.
- IDW PS 480.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

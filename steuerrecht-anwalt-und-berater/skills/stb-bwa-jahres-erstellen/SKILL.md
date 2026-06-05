---
name: stb-bwa-jahres-erstellen
description: "Jahres-BWA als Ergaenzung zum Jahresabschluss. Anwendungsfall Jahresabschluss-Begleitung mit BWA für das Gesamtjahr inkl Vorjahresvergleich Mehrjahrestrend und Mandantenpraesentation. Methodik kumulierte BWA mit Korrekturen Sondereffekten Mehrjahresvergleich. Output Jahres-BWA als Praesentations-PDF."
---

# Jahres-BWA — Ergaenzung zum Jahresabschluss

## Fachlicher Anker

- **Normen:** § 6a, §§ 242, § 252 HGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Der formale Jahresabschluss (Bilanz + GuV + Anhang + ggf. Lagebericht) ist juristisches Pflichtdokument, aber fuer den Mandanten oft schwer lesbar. Die Jahres-BWA ist die kommunikative Ergaenzung: kumulierter BWA-Block fuer das Gesamtjahr mit Vorjahresvergleich, Mehrjahres-Trend (3-5 Jahre), Kennzahlen-Zusammenfassung. Der Steuerberater praesentiert dem Mandanten die wirtschaftliche Entwicklung in einer Form, die der GF tatsaechlich liest und versteht.

## Kaltstart-Rueckfragen

1. Welcher Stichtag — Kalender-Geschaeftsjahr oder abweichendes Wirtschaftsjahr?
2. Liegen Daten der letzten 3-5 Jahre vor (Mehrjahres-Trend)?
3. Welche Korrekturen ergeben sich aus dem Jahresabschluss (vs. vorlaeufiger Quartals-BWA)?
4. Sondereffekte im Geschaeftsjahr (Sondertilgung, Sonderausschuettung, Sonder-AfA)?
5. Welche Kennzahlen sind im Vordergrund?
6. Welche Mandantenidentitaet (Logo, Farben)?
7. Verwendungszweck — Mandantengespraech, Gesellschafterversammlung, Bankgespraech?
8. Welche Erlaeuterungstiefe — knapp (2-3 Seiten) oder ausfuehrlich (10 Seiten)?

## Rechtlicher Rahmen

### Primaernormen

**§§ 242, 264 HGB** — Aufstellungspflicht Jahresabschluss.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 5b EStG** — E-Bilanz (Pflicht zur elektronischen Uebermittlung).

**§ 102 StaRUG** — Hinweispflicht bei Krisensignalen, im Jahresgespraech zu praesentieren.

### Standards

- IDW PS 480 — Erstellungsgrundsaetze.
- IDW PS 305 — Pruefung Risikofrueherkennung.
- DRS 17 — Lage-Bericht-Standards.
- DStV-Praxisleitfaden Mandantenkommunikation.

## Workflow

### Phase 1 — Datenbasis

- Jahresabschluss-Daten endgueltig (Bilanz, GuV, Anhang).
- Mehrjahres-Daten BWA (3-5 Jahre).
- Anlagenspiegel.
- OPOS-Saldenliste zum Stichtag.

### Phase 2 — Jahres-BWA aufbauen

```
JAHRES-BWA [Geschaeftsjahr]
Mandant: [Firma]
Stichtag: [Datum]

I. ERGEBNIS-UEBERBLICK
 Umsatzerloese [Jahr] [Vorjahr] [Abweichung in Prozent]
 Materialeinsatz ...
 Personalkosten ...
 Sonstige Aufwendungen ...
 Abschreibungen ...
 Betriebsergebnis ...
 Zinsergebnis ...
 Ergebnis vor Steuern ...
 Steuern ...
 Jahresergebnis ...

II. STRUKTURKENNZAHLEN
 Materialquote [Prozent]
 Personalquote [Prozent]
 Umsatzrentabilitaet [Prozent]
 EBITDA-Marge [Prozent]

III. LIQUIDITAETSKENNZAHLEN
 Liquiditaet 1./2./3. Grades [Prozent]
 Eigenkapitalquote [Prozent]
 Anlagendeckung II [Prozent]

IV. RENTABILITAET
 Eigenkapitalrendite [Prozent]
 Gesamtkapitalrendite [Prozent]

V. MEHRJAHRES-TREND (3-5 Jahre)
 Umsatzentwicklung als Liniendiagramm
 Ergebnisentwicklung
 Eigenkapital-Entwicklung
```

### Phase 3 — Sondereffekte separat

- Sonder-AfA § 7g EStG, § 7b EStG separat ausweisen.
- Anlagenverkauf, Sondertilgung, Sonderausschuettung mit kurzem Erlaeuterungsblock.
- "Bereinigtes Ergebnis" zusaetzlich darstellen.

### Phase 4 — Mehrjahres-Visualisierung

- Liniendiagramm Umsatz und Ergebnis ueber 5 Jahre.
- Balken Eigenkapital-Entwicklung.
- Heatmap Quartals-Ergebnisse (16 Quartale).

### Phase 5 — Kommentierung

- 2-Seiten-Erlaeuterung der wesentlichen Entwicklung.
- Vergleich Plan vs. Ist (falls Plan vorlag).
- Vergleich Branche (BBE-Daten falls verfuegbar).
- Ausblick auf Folgejahr.

### Phase 6 — Mandantenpraesentation

- Jahresgespraech mit Mandant: 1 Stunde mit Jahres-BWA-Praesentation.
- Im Anschluss schriftliche Bestaetigung der besprochenen Punkte.
- Bei Krisensignalen: § 102 StaRUG-Eskalation in den Bericht aufnehmen.

## Output

- Jahres-BWA als Praesentations-PDF (5-10 Seiten).
- Mehrjahres-Trend-Grafik.
- Erlaeuterungs- und Empfehlungstext.

## Strategie und Praxis-Tipps

- Jahres-BWA ist KEIN Ersatz fuer den formalen Jahresabschluss, sondern ergaenzende Kommunikations-Schicht.
- Der formale JA folgt § 325 HGB (Bundesanzeiger-Veroeffentlichung); die Jahres-BWA ist intern.
- Bei Gesellschafterversammlung: Jahres-BWA als Tischvorlage statt blanker Bilanz.
- Mehrjahres-Trend ist Standard bei mittelstaendischer Bilanzanalyse — 5 Jahre ist guter Kompromiss.
- StBVV: Jahres-BWA als Zusatzauftrag neben Jahresabschluss-Erstellung; ggf. Pauschal.
- DATEV-Tipp: Klickpfad fuer Mehrjahres-Vergleich: Rechnungswesen → Auswertungen → BWA → BWA-Form mit Vorjahresspalten waehlen, Jahresvergleich aktivieren.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-bwa-mandantenreport-monatlich` — Monatsreport.
- `stb-bwa-kennzahlen-rentabilitaet-eigenkapital` — Rentabilitaet.
- `stb-jahresgespraech-mandant-bwa-basis` — Jahresgespraech.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 242, 252, 264, 325.
- EStG § 5b.
- StBerG § 33.
- StaRUG § 102.
- IDW PS 480, IDW PS 305, DRS 17.
- DStV-Praxisleitfaden.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

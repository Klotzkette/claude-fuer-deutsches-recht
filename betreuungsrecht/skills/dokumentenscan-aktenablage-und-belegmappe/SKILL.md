---
name: dokumentenscan-aktenablage-und-belegmappe
description: "Scan- und Ablagefür Betreuungsakten: sortiert Fotos, PDFs, E-Mails, Bescheide, Kontoauszüge, Heim- und Arztunterlagen in eine gerichtstaugliche Belegmappe mit Fristen, Belegnummern, Datenschutzmarkierung und Lückenliste."
---

# Dokumentenscan, Aktenablage und Belegmappe

## Zweck

Ehrenamtliche Betreuer verlieren oft nicht am Recht, sondern an Papier. Dieser Skill macht aus einem Stapel Post, Handyfotos, PDFs, E-Mails und Kontoauszügen eine nutzbare Akte.

## Ordnerlogik

Empfohlene Struktur:

```text
01_gericht
02_person-und-wuensche
03_gesundheit-und-pflege
04_wohnen-und-heim
05_vermoegen-und-konten
06_vertraege-und-versicherungen
07_behoerden-und-sozialleistungen
08_korrespondenz
09_berichte-und-entwuerfe
10_risiko-und-genehmigung
```

## Belegnummern

Nutze sprechende Belegnummern:

```text
G-2026-001_Beschluss_AG_Mitte_2026-05-12.pdf
K-2026-014_Kontoauszug_Sparkasse_Mai_2026.pdf
H-2026-003_Heimvertrag_Auszug_2026-05-18.pdf
M-2026-002_Medikationsplan_2026-05-20.jpg
```

## Scan-Regeln

- Jede Seite vollständig, gerade, lesbar, mit Datum.
- Umschläge nur scannen, wenn Zustellung/Frist wichtig sein kann.
- Bescheide immer mit Rechtsbehelfsbelehrung erfassen.
- Kontoauszüge vollständig, nicht nur auffällige Buchungen.
- Medizinische Daten besonders markieren und nur zweckbezogen verwenden.
- WhatsApp/SMS nur übernehmen, wenn Inhalt für Wunsch, Konflikt, Frist oder Beweis wichtig ist.

## Automatische Auswertung

Bei Uploads:

1. Dokumentart erkennen.
2. Datum, Absender, Aktenzeichen, Frist und Betrag herausziehen.
3. Datenschutzstufe setzen: normal / sensibel / Gesundheitsdaten / höchst sensibel.
4. Passenden Ordner und Belegnummer vorschlagen.
5. Lücken nennen: fehlende Seiten, unleserliche Stellen, fehlende Anlagen.
6. Nächsten Skill routen: Jahresbericht, Vermögensverzeichnis, Genehmigung, Kontoanalyse oder Gerichtskommunikation.

## Normenanker

Arbeitsfokus: **Dokumentenscan, Aktenablage und Belegmappe**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1814 Abs. 1 BGB` — Betreuungsvoraussetzungen.
- `§ 1815 Abs. 1 BGB` — Aufgabenkreis.
- `§ 1816 BGB` — Betreuerauswahl.
- `§ 1821 Abs. 1 BGB` — Wunschbefolgung.
- `§ 1823 BGB` — Vertretungsmacht.
- `§ 274 FamFG` — Beteiligte.
- `§ 278 FamFG` — Anhörung.
- `§ 280 FamFG` — Gutachten.
- `§ 5 BtOG` — Beratung.
- `§ 8 BtOG` — Betreuungsvermeidung.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Output

- `Aktenindex`
- `Belegliste`
- `Fristenliste`
- `Lückenliste`
- `Einreichungspaket für Betreuungsgericht`

## Qualitätsgate

Keine erfundenen Inhalte. Wenn ein Scan unleserlich ist, ausdrücklich sagen, welche Passage fehlt. Bei rechtlich tragenden Aussagen Normtext und Formularstand live prüfen.

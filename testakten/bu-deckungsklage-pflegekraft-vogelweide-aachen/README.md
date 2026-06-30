# BU-Deckungsklage Pflegekraft Vogelweide Aachen


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 690 KB) | PDF | [`gesamt-pdf/bu-deckungsklage-pflegekraft-vogelweide-aachen_gesamt.pdf`](gesamt-pdf/bu-deckungsklage-pflegekraft-vogelweide-aachen_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-bu-deckungsklage-pflegekraft-vogelweide-aachen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bu-deckungsklage-pflegekraft-vogelweide-aachen.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-bu-deckungsklage-pflegekraft-vogelweide-aachen-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bu-deckungsklage-pflegekraft-vogelweide-aachen-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

**Plugin:** `fachanwalt-versicherungsrecht`
**Kanzlei:** Müller-Hauck Versicherungsrecht Aachen-Burtscheid
**Rechtsanwältin:** Dr. Annegret Müller-Hauck, Fachanwältin für Versicherungsrecht
**Angelegt:** 20.02.2026 | **Stand:** 30.05.2026

---

## Mandantin

**Marion Vogelweide**, geb. 14.03.1974, examinierte Altenpflegerin (38 Jahre Berufserfahrung, zuletzt St.-Antonius-Heim GmbH, Aachen-Brand). Seit 02.09.2025 berufsunfähig.

---

## Verfahren im Überblick

| Aktenzeichen | Gericht | Gegenstand | Streitwert |
|---|---|---|---|
| `5 O 102/26` | LG Aachen | BU-Klage gegen DBV-Winterthur | 133.200 EUR |
| `26 O 144/26` | LG Köln | D&O-Deckungsklage gegen ManagerSchutz AG | 59.000 EUR |
| `Vers-Omb 38211/26` | Ombudsmann | Schlichtung (eingestellt) | — |

---

## Konfliktlage

1. **BU-Klage** — Skills `fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage`, `fachanwalt-versicherungsrecht-deckungsklage`, `fachanwalt-versicherungsrecht-leistungsablehnung-pruefen`: DBV-Winterthur lehnte am 14.02.2026 BU-Leistung (1.850 EUR/Monat) ab. Begründung: keine ausreichende BU, Verweisungstätigkeit möglich, fehlende Dauerhaftigkeit. Klage LG Aachen seit 16.03.2026.

2. **Deckungsanfrage** — Skill `deckungsanfrage-pruefen`: Vorprozessuale Deckungsanfrage vom 25.02.2026, abgelehnt.

3. **D&O-Versicherungsabwehr** — Skills `fachanwalt-versicherungsrecht-do-deckungsabwehr`, `fachanwalt-versicherungsrecht-regress-abwehr`: Vogelweide war GF der Vogelweide+Co Demenz-WG GmbH (2018–2023). ManagerSchutz AG verweigert Deckung (Inventarverluste 41.000 EUR + Ransomware-Zahlung 18.000 EUR).

4. **Cyber-Lösegeld / Sanktionsrecht** — Skill `fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht`: Ransomware-Angriff Nov. 2022 auf Demenz-WG; Lösegeld 18.000 EUR BTC; Empfänger-Wallet nachträglich auf OFAC-SDN-Liste (Listung März 2023 — ex post). OFAC-Sanktionsklausel greift nicht.

5. **LV-Rückkauf** — Skill `fachanwalt-versicherungsrecht-lebensversicherung-rueckkauf`: HDI-Kapital-LV (2003, Rückkaufswert ca. 78.200 EUR), strittiger Stornoabzug 3.000 EUR. BGH IV ZR 199/22 Prüfung.

6. **Ombudsmann** — Skill `fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung`: Schlichtungsantrag 20.02.2026; eingestellt 18.03.2026 wegen Rechtshängigkeit.

---

## Medizinische Diagnosen (Auswahl)

| ICD-10 | Diagnose |
|---|---|
| M50.1 | Diskushernie HWS C5/C6, Radikulopathie (OP Nov. 2024) |
| M54.4 | Chron. LWS-Syndrom |
| F32.1 | Mittelgradige Depression (BDI-II 29) |
| F43.2 | Anpassungsstörung nach Mobbing |
| L23.5 | Allergisches Kontaktekzem (Latex/Glutaraldehyd) |

---

## Aktenstruktur

```
bu-deckungsklage-pflegekraft-vogelweide-aachen/
├── README.md                          ← diese Datei
│
├── 01-mandantenakte-stammdaten.md
├── 02-medizinische-diagnosen-befundchronologie.md
├── 03-bu-antrag-dbv-winterthur.md
├── 04-ablehnungsschreiben-dbv-winterthur.md
├── 05-deckungsanfrage-pruefen.md
├── 06-ombudsmann-schlichtungsantrag-zusammenfassung.md
├── 07-rechtliche-analyse-bu-klage.md
├── 08-do-versicherung-sachverhalt.md
├── 09-cyber-loesegeld-sanktionsrecht.md
├── 10-lebensversicherung-rueckkauf-hdi.md
├── 11-taetigkeitsanalyse-altenpflegerin.md
├── 12-regress-abwehr-do.md
├── 13-verfahrensstand-uebersicht.md
├── 14-beweismittel-liste.md
├── 15-fristen-und-kostenuebersicht.md
├── 16-korrespondenz-arbeitgeber.md
├── 17-rechtsprechungsrecherche.md
├── 18-mandantenprotokoll.md
├── 19-hdi-korrespondenz-rueckkauf.md
├── 20-datenschutz-ransomware-meldung.md
├── 21-sachverstaendigen-beauftragung.md
├── 22-abschlussbericht-aktenstand.md
│
├── docx/
│   ├── 01-klageschrift-bu-rente.docx         ← Klageschrift LG Aachen 5 O 102/26
│   ├── 02-do-deckungsklageschrift.docx        ← Klageschrift LG Köln 26 O 144/26
│   └── 03-schlichtungsantrag-ombudsmann.docx  ← Schlichtungsantrag Ombudsmann
│
├── xlsx/
│   ├── 01-aerztliche-befund-chronologie.xlsx  ← ICD-10-Chronologie mit Befunddaten
│   └── 02-rueckkaufswert-vergleich-hdi.xlsx   ← HDI-Rückkauf vs. Rentenoption
│
├── eml/
│   ├── 01-erstanfrage-vogelweide-an-kanzlei.eml
│   ├── 02-terminbestaetigung-kanzlei-an-vogelweide.eml
│   ├── 03-kanzlei-an-dbv-deckungsanfrage-begleit.eml
│   └── 04-vogelweide-an-it-dienstleister-backups.eml
│
├── pdfs/
│   ├── 01-ablehnungsschreiben-dbv-winterthur.pdf   ← Leistungsablehnung DBV-Winterthur
│   └── 02-ofac-sdn-listen-auszug-redacted.pdf      ← OFAC SDN-Liste geschwärzt
│
└── jpg/
    ├── 01-arbeitsplatzfoto-pflege.jpg        ← Pflege-Arbeitsplatz Illustration
    ├── 02-berufsbild-taetigkeitsdiagramm.jpg ← Tätigkeitsanalyse + Kapazitätsdiagramm
    └── 03-hand-dermatose-skizze.jpg          ← Dermatologischer Befund Hände
```

---

## Einschlägige Rechtsprechung

Alle Nachweise über die erlaubten Quellen:

- **BGH IV ZR 99/95** — Dauerhaftigkeit BU (3-Jahres-Prognose) — [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.02.1997&Aktenzeichen=IV+ZR+99%2F95)
- **BGH IV ZR 203/92** — Lebensstellung bei Verweisung — [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=22.09.1993&Aktenzeichen=IV+ZR+203%2F92)
- **BGH IV ZR 244/03** — Konkretisierungspflicht Versicherer — [openjur.de](https://openjur.de)
- **BGH IV ZR 275/08** — Maßgeblichkeit des konkreten Berufs — [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
- **BGH IV ZR 199/22** — Rückkaufswert Kapital-LV — [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
- **BGH IV ZR 145/19** — Sanktionsklauseln eng auszulegen — [dejure.org](https://dejure.org)
- **BGH II ZR 234/07** — Business Judgment Rule GmbH — [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
- **OLG Köln 20 U 125/19** — Altenpflegerin, körperl. Berufsbild — [openjur.de](https://openjur.de)

---

## Relevante Normen

`§ 172 VVG` · `§ 153 VVG` · `§ 307 BGB` · `§ 43 GmbHG` · `§ 103 VVG` · `§ 204 BGB` · `Art. 33/34 DSGVO` · `§ 34 StGB` · `§ 7a SGB XI` · `Art. 83 DSGVO`

---

## Dateigröße

660K

*(Gesamtgröße Aktenordner)*

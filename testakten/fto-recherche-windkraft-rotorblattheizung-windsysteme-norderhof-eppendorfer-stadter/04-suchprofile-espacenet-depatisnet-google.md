# 04 — Suchprofile Espacenet, DEPATISnet, Google Patents

AZ: SE-2026-FTO-0717 | Bearb.: Dr. Eppendorfer / Klose | Stand: 28.01.2026

---

## 1. Vorgehen und Datenbankauswahl

Die Recherche erfolgt in drei Primärdatenbanken, deren Treffer dedupliziert und zusammengeführt werden. Jede Datenbank hat spezifische Stärken:

- **Espacenet (EPO)**: Vollständigste EP- und WO-Abdeckung, CPC-Klassifikation, Volltexte EP.
- **DEPATISnet (DPMA)**: DE-Anmeldungen und Erteilungen vollständig, Volltexte DE, IPC und CPC.
- **Google Patents**: Ergänzungsrecherche CN und asiatische Märkte, Volltextsuche nicht-klassifizierter Schriften.
- **PATENTSCOPE (WIPO)**: PCT-Anmeldungen, internationaler Recherchebericht.

## 2. Suchprofile Espacenet

### Suche SE-01 (Hauptsuche Klassifikation + Keyword)

```
CPC=(F03D80/40) AND CPC=(H05B3/84 OR H05B2203/016 OR H05B3/26)
```

Ergebnis: 47 Treffer (Stand 27.01.2026). Nach Abstract-Screening: 18 relevant.

### Suche SE-02 (Schlüsselwortsuche Volltext EP)

```
TI=(wind AND rotor AND (heat* OR anti-icing OR de-icing OR ice))
AND AB=(resistive OR carbon OR fiber OR fibre OR heating element)
AND PY=[2010 TO 2026]
```

Ergebnis: 112 Treffer. Nach Deduplizierung mit SE-01: 34 neue Treffer, davon 9 relevant.

### Suche SE-03 (Anmeldersuche Vellbruck)

```
PA=(Vellbruck) AND CPC=(F03D*)
```

Ergebnis: 7 Treffer (EP und DE). Vollständige Durchsicht: 3 hochrelevant (EP 3 218 922 B1, EP 3 127 458 A1 anhängig, DE 10 2017 210 413 A1).

### Suche SE-04 (Vestas-Portfolio)

```
PA=(Vestas) AND CPC=(F03D80/40) AND PY=[2012 TO 2026]
```

Ergebnis: 23 Treffer. Nach Abstract-Screening: 5 FTO-relevant.

### Suche SE-05 (Goldwind/XEMC-Portfolio CN/EP)

```
PA=(Goldwind OR XEMC OR Xinjiang) AND CPC=(F03D80/40)
```

Ergebnis: 11 Treffer (EP/WO-Familienmitglieder).

## 3. Suchprofile DEPATISnet

### Suche DE-01 (Klassifikationssuche DE)

```
IC=F03D80/40 UND IC=H05B3/84
```

Ergebnis: 31 Treffer. Nach Screening: 8 relevant.

### Suche DE-02 (Volltext DE)

```
TI=(Rotorblatt* UND (Heiz* OR Enteis*)) AND AB=(Widerstand* OR Kohlefaser*)
```

Ergebnis: 67 Treffer. 11 neu nach Deduplizierung, 4 relevant.

### Suche DE-03 (Anmeldersuche Vellbruck DE)

```
ANM=Vellbruck
```

Ergebnis: 12 DE-Anmeldungen. Davon 2 relevant: DE 10 2017 210 413 A1 (Anmeldetag 22.06.2017, Grundlage für EP 3 218 922) und DE 10 2019 205 847 A1 (Anmeldetag 2019, eigenständiges Folgepatent Vellbruck zur Steuerung).

### Suche DE-04 (Stand der Technik Vorveröffentlichungen vor 15.06.2018)

```
IC=F03D80/40 AND PY=[2000 TO 2018] AND LAND=DE,EP,US
```

Ergebnis: 89 Treffer. Für Nichtigkeitsrecherche relevant: 14 Dokumente.

## 4. Suchprofile Google Patents

### Suche GP-01 (CN-Anmelder Goldwind)

```
assignee:(Goldwind) wind turbine blade heating
```

Ergebnis: 31 Treffer CN/EP. Nach Screening: 7 CN-Treffer ohne EP-Familienmitglieder.

### Suche GP-02 (Chinesische Volltextsuche)

```
wind blade anti-icing resistive carbon fiber heating zone after:2015 country:CN
```

Ergebnis: 156 Treffer CN. Stichprobenauswertung (30 Abs.): 8 potenziell relevant, Volltextlektüre erforderlich.

### Suche GP-03 (Siemens Gamesa Portfolio)

```
assignee:(Siemens Gamesa) wind blade deicing heating system
```

Ergebnis: 18 Treffer. Nach Screening: 3 FTO-relevant (US-Bereich).

## 5. Gesamtergebnis Datenbankrecherche

| Datenbank | Suchanfragen | Rohtreffer | Relevante Treffer | Davon FTO-kritisch |
|---|---|---|---|---|
| Espacenet | 5 | 200 | 41 | 12 |
| DEPATISnet | 4 | 199 | 23 | 8 |
| Google Patents | 3 | 205 | 15 | 5 |
| Gesamt (nach Dedup.) | 12 | ca. 450 | 62 | 22 |

Die 22 FTO-kritischen Treffer werden in den Clusters 1–4 (Aktenstücke 05–08) nach Rechtsraum aufgegliedert. Die restlichen 40 relevanten Treffer werden als „Stand-der-Technik-Kandidaten" für die Nichtigkeitsrecherche archiviert.

## 6. Qualitätssicherung Recherche

Gegenkontrolle: Suche nach bekannten Referenzpatenten (EP 3 218 922 B1 und US 10 612 514 B2 als Kontroll-Seeds) — beide in Treffermenge enthalten. Keine Hinweise auf Datenbankausfälle oder Indexierungslücken.

Recherchezustand: EPO Espacenet — Index Stand 24.01.2026. DEPATISnet — Index Stand 24.01.2026. Google Patents — tagesaktuell.

Quellen: [Espacenet EPO](https://worldwide.espacenet.com) | [DEPATISnet DPMA](https://depatisnet.dpma.de) | [Google Patents](https://patents.google.com) | [PATENTSCOPE WIPO](https://patentscope.wipo.int)

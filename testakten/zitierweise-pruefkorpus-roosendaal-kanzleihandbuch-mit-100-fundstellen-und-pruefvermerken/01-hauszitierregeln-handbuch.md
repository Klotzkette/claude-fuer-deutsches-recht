# 01 — Hauszitierregeln Kanzlei Roosendaal Birkenhainer Partners mbB (v4.0)

**Kanzlei Roosendaal Birkenhainer Partners mbB**
**Kanzleihandbuch Zitierweise — Version 4.0 (Oktober 2025)**
**Federführung: Dr. Henrik Roosendaal | Erstellung: Dr. Sophia Pohlmann-Wittfeldt | Knowledge: Moritz Lattermann**

---

## A. Grundprinzipien

### A.1 Vorrang amtlicher Quellen

Amtliche Sammlungen (BGHZ, BGHSt, BVerfGE, BFHE, BVerwGE, BSGE, BAGE) gehen freien und kommerziellen Quellen stets vor. Bei Mehrfach-Fundstellen wird die amtliche Sammlung zuerst genannt, dann die erste juristische Fachzeitschrift, dann sonstige Quellen.

**Rangfolge:**

1. Amtliche Sammlung (BGHZ, BVerfGE, BFHE, BVerwGE, BSGE, BAGE)
2. NJW, JZ, MDR, AcP (erste relevante Fachzeitschrift)
3. Spezialisierte Zeitschriften (FamRZ, NZA, BStBl., NVwZ usw.)
4. Freie Online-Quellen: dejure.org, openjur.de (mit URL)
5. BeckRS (nur bei aktivem Lizenzzugang; sonst: Prüfvermerk BeckRS-Sperre)

### A.2 Mindeststandard Rechtsprechungszitate

Jedes Rechtsprechungszitat muss enthalten:

- Gericht (Abkürzung gemaess Liste in Abschnitt E)
- Datum der Entscheidung (TT.MM.JJJJ)
- Aktenzeichen
- Fundstelle (amtliche Sammlung ODER Zeitschrift ODER freie Quelle mit URL)

Fehlt eines der vier Elemente, ist das Zitat unvollständig. Ein Prüfvermerk ist zu setzen.

### A.3 Mindeststandard Literaturzitate

Jedes Literaturzitat muss enthalten:

- Autorenname(n) bzw. Herausgeber
- Kurztitel oder Langtitel (nach erstem Vollbeleg)
- Erscheinungsjahr oder Auflage
- Seiten- oder Randnummernangabe (Rn.)

### A.4 BeckRS-Regel (Neu in v4.0)

BeckRS-Fundstellen dürfen nur ausgegeben werden, wenn der Nutzer einen aktiven Lizenzzugang zu Beck-Online nachweist oder ein solcher für die Kanzlei besteht. Fehlt der Nachweis oder ist die Zugänglichkeit unklar, gibt das Plugin `zitierweise-deutsches-recht` einen Prüfvermerk aus:

> **[PRÜFVERMERK — BeckRS-SPERRE]** Die Fundstelle BeckRS JJJJ, XXXXX konnte nicht verifiziert werden. Prüfe amtliche Quelle (bundesgerichtshof.de / bundesverfassungsgericht.de) oder freie Quelle (dejure.org / openjur.de). Ausgabe gesperrt bis Verifikation.

### A.5 Modellwissen-Sperre Literatur

Das Plugin gibt keine Literaturzitate aus, die ausschliesslich auf Modellwissen beruhen und nicht durch eine prüfbare Quelle belegt werden können. Stattdessen erscheint ein Prüfvermerk:

> **[PRÜFVERMERK — LITERATUR-MODELLWISSEN-SPERRE]** Der Aufsatz/die Fundstelle konnte nicht verifiziert werden. Bitte Volltextzugang prüfen und Zitat manuell erganzen.

---

## B. Zitierformate

### B.1 Rechtsprechung — Langformat (Erstnennung)

```
BVerfG, Urt. v. 15.01.1958, Az. 1 BvR 400/51, BVerfGE 7, 198 (205) — Lueth.
BGH, Urt. v. 14.02.1958, Az. I ZR 151/56, BGHZ 26, 349 (350).
BAG, Urt. v. 20.03.2024, Az. 2 AZR 184/23, NZA 2024, 893 (895), abrufbar unter: https://www.openjur.de/u/XXXXXXX.html (abgerufen am TT.MM.JJJJ).
```

### B.2 Rechtsprechung — Kurzformat (Wiederholung)

```
BVerfGE 7, 198 (205).
BGH NJW 2022, 1234 (1235).
```

### B.3 Kommentare — Erstnennung ab 2022 (Gruenenberg)

```
Gruenenberg/Bearbeiter, BGB, 83. Aufl. 2024, § 242 Rn. 15.
```

### B.4 Kommentare — Erstnennung bis 2021 (Palandt)

```
Palandt/Bearbeiter, BGB, 80. Aufl. 2021, § 242 Rn. 15.
```

Altzitate in Bestandsschriftsätzen sind als solche kenntlich zu machen (vgl. Abschnitt 16).

### B.5 Aufsätze

```
Autor, Titel, Zeitschrift Jahrgang (Jahr), Seite (Zitierseite).
Beispiel: Tannenmoor, Neue Anforderungen an die anwaltliche Zitierweise, JZ 2024, 100 (103).
[PRUEFVERMERK — LITERATUR-MODELLWISSEN-SPERRE: Fundstelle nicht verifizierbar, da kein Direktzugriff auf JZ 2024 moeglich. Bitte manuell pruefen.]
```

### B.6 Monographien

```
Autor, Titel, Aufl. Jahr, Seite.
Beispiel: Musielak/Voit, Zivilprozessordnung, 21. Aufl. 2024, § 286 Rn. 12.
```

### B.7 Festschriften und Sammelbandaufsätze

```
Autor, Titel des Beitrags, in: Hrsg. (Hrsg.), Festschrift fuer XY, Jahr, Seite.
```

### B.8 EU-Recht (ECLI)

```
EuGH, Urt. v. TT.MM.JJJJ, ECLI:EU:C:JJJJ:XXX, NJW JJJJ, Seite, abrufbar unter: https://eur-lex.europa.eu/... (abgerufen am TT.MM.JJJJ).
```

---

## C. URL-Pflicht und Archivierung

### C.1 Grundregel

Bei jeder Entscheidung, die über dejure.org oder openjur.de frei zugänglich ist, ist die URL anzugeben. Das Weglassen der URL gilt als Zitierfehler.

Format: `abrufbar unter: [URL] (abgerufen am TT.MM.JJJJ).`

### C.2 Archivierungspflicht

Für URLs, die nicht auf staatliche oder dauerhaft stabile Server verweisen, ist ein Wayback-Machine-Archivlink zu ergänzen:

```
abrufbar unter: https://openjur.de/u/XXXXXXX.html (abgerufen am 15.09.2025; archiviert unter: https://web.archive.org/web/20250915XXXXXX/...).
```

### C.3 Amtliche Server (bundesgerichtshof.de, bundesverfassungsgericht.de)

Verweise auf amtliche Servern gelten als stabil. Ein separater Archivlink ist nicht erforderlich, aber zulässig.

---

## D. Besondere Regelungen

### D.1 Palandt/Gruenenberg-Grenzjahr

Das Grenzjahr ist das Erscheinungsjahr der Auflage:

| Auflage | Jahr | Kurztitel |
|---|---|---|
| 80. Aufl. | 2021 | Palandt |
| 81. Aufl. | 2022 | Gruenenberg |
| 82. Aufl. | 2023 | Gruenenberg |
| 83. Aufl. | 2024 | Gruenenberg |

Verwechslungen (z.B. Palandt 2022 oder Gruenenberg 2021) sind Fehler der Kategorie A (schwerwiegend).

### D.2 BVerfGE — Band, Seite, Randnummer

BVerfGE-Zitate enthalten nach Möglichkeit die Band-Seite-Angabe aus der amtlichen Sammlung. Randnummern sind zusätzlich anzugeben, wenn die Entscheidung auf bundesverfassungsgericht.de abrufbar ist.

### D.3 Wiederholungszitate (a.a.O.)

Bei sofortiger Wiederholung innerhalb derselben Fussnote oder bei letzter Nennung auf derselben Seite: a.a.O. mit Seiten-/Randnummernangabe.

---

## E. Gerichtsabkürzungen (Auswahl)

| Abkürzung | Gericht |
|---|---|
| BVerfG | Bundesverfassungsgericht |
| BGH | Bundesgerichtshof |
| BFH | Bundesfinanzhof |
| BVerwG | Bundesverwaltungsgericht |
| BSG | Bundessozialgericht |
| BAG | Bundesarbeitsgericht |
| OLG | Oberlandesgericht (mit Ortsangabe) |
| LG | Landgericht (mit Ortsangabe) |
| AG | Amtsgericht (mit Ortsangabe) |
| EuGH | Gerichtshof der Europäischen Union |
| EuG | Gericht der Europäischen Union |

---

## F. Prüfvermerk-Typen (Übersicht)

| Typ | Kürzel | Anlass |
|---|---|---|
| BeckRS-Sperre | PV-BR | BeckRS ohne verifizierten Lizenzzugang |
| Literatur-Modellwissen-Sperre | PV-LM | Aufsatz/Quelle nicht verifizierbar |
| Unvollständiges Zitat | PV-UV | Pflichtangabe fehlt (Datum, AZ, Fundstelle) |
| URL fehlt | PV-URL | Freie Quelle ohne Pflicht-URL |
| Rangfolge-Fehler | PV-RG | Falsche Reihenfolge bei Mehrfach-Fundstellen |
| Palandt/Gruenenberg-Verwechslung | PV-PG | Falscher Kurztitel für das Erscheinungsjahr |

Vollständige Prüfvermerk-Vorlage: siehe Aktenstück 11.

---

*Erstellt: Oktober 2025 | Version: 4.0 | Kanzlei Roosendaal Birkenhainer Partners mbB*

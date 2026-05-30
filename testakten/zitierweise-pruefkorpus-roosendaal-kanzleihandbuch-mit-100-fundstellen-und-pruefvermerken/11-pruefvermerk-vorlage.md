# 11 — Pruefvermerk-Vorlage v4.0

**Kanzlei Roosendaal Birkenhainer Partners mbB**
**Kanzleihandbuch Zitierweise v4.0 — Pruefvermerk-Standard**
**Bearbeiterin: Dr. Sophia Pohlmann-Wittfeldt**
**Stand: Oktober 2025**

---

## A. Zweck und Anwendungsbereich

Ein Pruefvermerk (PV) wird ausgegeben, wenn das Plugin `zitierweise-deutsches-recht` eine Fundstelle nicht vollstaendig verifizieren kann oder wenn ein Zitierfehler festgestellt wird. Der Pruefvermerk ersetzt die Fundstellen-Ausgabe oder erganzt sie mit einem Warnhinweis.

Pruefvermerke sind nicht zur Weitergabe in Schriftsaetzen bestimmt. Sie dienen dem internen Qualitaetsmanagement.

---

## B. Pruefvermerk-Typen und Vorlagen

### PV-BR — BeckRS-Sperre

**Anlass:** BeckRS-Fundstelle ohne dokumentierten Lizenzzugang.

**Vorlage:**
> **[PRUEFVERMERK — BeckRS-SPERRE (PV-BR)]**
> Die Fundstelle BeckRS [JJJJ], [XXXXX] konnte nicht verifiziert werden, da kein aktiver Beck-Online-Lizenzzugang fuer diesen Pruefvorgang dokumentiert ist.
>
> Pruefe amtliche Alternative:
> - bundesgerichtshof.de / bundesverfassungsgericht.de / bundesfinanzhof.de
>
> Pruefe freie Alternative:
> - dejure.org: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=[GERICHT]&Datum=[DATUM]&Aktenzeichen=[AZ]
> - openjur.de: https://openjur.de (Suchmaske)
>
> Ausgabe gesperrt bis Verifikation.
> Erstellt: [Datum] | Bearbeiter: [Name]

---

### PV-LM — Literatur-Modellwissen-Sperre

**Anlass:** Aufsatz oder Literaturstelle nicht verifizierbar; Zitat wuerde auf Modellwissen beruhen.

**Vorlage:**
> **[PRUEFVERMERK — LITERATUR-MODELLWISSEN-SPERRE (PV-LM)]**
> Der Aufsatz / die Literaturstelle [AUTOR, Titel, Zeitschrift JJJJ, Seite] konnte nicht verifiziert werden. Das Plugin verfuegt nicht ueber einen geprueften Direktzugriff auf diese Quelle.
>
> Ein Zitat aus dem Modellwissen heraus wuerde Halluzinationsrisiken begru"nden und wird nicht ausgegeben.
>
> Empfehlung: Bitte Volltextzugang ueber beck-online, juris, Bibliothek oder Verlag pruefen und Zitat manuell erganzen.
>
> Muster-Zitat (unverifiziert — bitte nicht unveraendert verwenden):
> [AUTOR], [Titel], [Zeitschrift] [Jahrgang] ([Jahr]), [Seite (Zitierseite)].
>
> Erstellt: [Datum] | Bearbeiter: [Name]

---

### PV-UV — Unvollstaendiges Zitat

**Anlass:** Pflichtangabe fehlt (Gericht, Datum, Aktenzeichen oder Fundstelle).

**Vorlage:**
> **[PRUEFVERMERK — UNVOLLSTAENDIGES ZITAT (PV-UV)]**
> Das vorliegende Zitat enthalt nicht alle Pflichtangaben gemaess Hauszitierregel A.2 / A.3:
>
> Fehlend: [Gericht / Datum / Aktenzeichen / Fundstelle — Zutreffendes unterstreichen]
>
> Bitte Pflichtangaben erganzen. Korrekturentwurf (soweit rekonstruierbar):
> [VORSCHLAG ODER FRAGEZEICHEN]
>
> Erstellt: [Datum] | Bearbeiter: [Name]

---

### PV-URL — Fehlende Pflicht-URL

**Anlass:** Entscheidung ueber dejure.org oder openjur.de frei zugaenglich; URL wurde nicht angegeben.

**Vorlage:**
> **[PRUEFVERMERK — URL FEHLT (PV-URL)]**
> Die Entscheidung [GERICHT, DATUM, AZ] ist frei zugaenglich. Die URL-Angabe ist gemaess Hauszitierregel C.1 Pflicht.
>
> Gefundene URL: [URL]
> Abrufdatum: [DATUM]
>
> Bitte URL in das Zitat aufnehmen.
>
> Erstellt: [Datum] | Bearbeiter: [Name]

---

### PV-RG — Rangfolge-Fehler

**Anlass:** Mehrfach-Fundstellen in falscher Reihenfolge (z.B. NJW vor BGHZ).

**Vorlage:**
> **[PRUEFVERMERK — RANGFOLGE-FEHLER (PV-RG)]**
> Die Fundstellen sind in falscher Reihenfolge angegeben. Gemaess Hauszitierregel A.1 gilt:
> Amtliche Sammlung > Fachzeitschrift > Freie Online-Quelle > BeckRS
>
> Vorgefundene Reihenfolge: [IST-ZUSTAND]
> Korrekte Reihenfolge: [SOLL-ZUSTAND]
>
> Bitte korrigieren.
>
> Erstellt: [Datum] | Bearbeiter: [Name]

---

### PV-PG — Palandt/Gruenenberg-Verwechslung

**Anlass:** Falscher Kurztitel fuer das jeweilige Erscheinungsjahr des BGB-Kommentars.

**Vorlage:**
> **[PRUEFVERMERK — PALANDT/GRUENENBERG-VERWECHSLUNG (PV-PG)]**
> Das Zitat verwendet den falschen Kurztitel fuer die [XX.] Auflage ([JJJJ]).
>
> Fuer Auflagen bis 80. Aufl. (2021): Kurztitel Palandt
> Fuer Auflagen ab 81. Aufl. (2022): Kurztitel Gruenenberg
>
> Vorgefunden: [FEHLERHAFTES ZITAT]
> Korrekt: [KORRIGIERTES ZITAT]
>
> Fehlerkat.: A (schwerwiegend — Autorenschafts-Fehler).
>
> Erstellt: [Datum] | Bearbeiter: [Name]

---

## C. Fehlerkategorien

| Kategorie | Beschreibung | Beispiele |
|---|---|---|
| A — Schwerwiegend | Inhaltlich oder rechtlich relevanter Fehler | Falsche Autorenschaft, Halluzination, falsche Entscheidung |
| B — Formal | Formaler Fehler ohne inhaltliche Konsequenz | Fehlende Pflichtangabe, falsche Rangfolge |
| C — Empfehlung | Kein Pflichtfehler, aber Qualitaetsverbesserung moeglich | Fehlender Archivlink, kuerzbares Zitat |

---

## D. Arbeitsprozess bei Pruefvermerk

1. Pruefvermerk erscheint in Plugin-Ausgabe.
2. Bearbeiter identifiziert Fehlertyp und Korrekturmoeglichkeit.
3. Korrektur wird dokumentiert (Spalte "Pruefvermerk-Status" in XLSX-Pruefkorpus).
4. Nach Korrektur: Pruefvermerk-Status = "aufgeloest" oder "Sperre bleibt".
5. Verbleibende Sperren werden in Qualitaetsbericht aufgenommen (Aktenstueck 20).

---

*Pruefvermerk-Vorlage v4.0 | Kanzlei Roosendaal Birkenhainer Partners mbB | Oktober 2025*

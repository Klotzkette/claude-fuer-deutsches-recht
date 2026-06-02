# 11 — Prüfvermerk-Vorlage v4.0

**Kanzlei Roosendaal Birkenhainer Partners mbB**
**Kanzleihandbuch Zitierweise v4.0 — Prüfvermerk-Standard**
**Bearbeiterin: Dr. Sophia Pohlmann-Wittfeldt**
**Stand: Oktober 2025**

---

## A. Zweck und Anwendungsbereich

Ein Prüfvermerk (PV) wird ausgegeben, wenn das Plugin `zitierweise-deutsches-recht` eine Fundstelle nicht vollständig verifizieren kann oder wenn ein Zitierfehler festgestellt wird. Der Prüfvermerk ersetzt die Fundstellen-Ausgabe oder erganzt sie mit einem Warnhinweis.

Prüfvermerke sind nicht zur Weitergabe in Schriftsaetzen bestimmt. Sie dienen dem internen Qualitätsmanagement.

---

## B. Prüfvermerk-Typen und Vorlagen

### PV-BR — BeckRS-Sperre

**Anlass:** BeckRS-Fundstelle ohne dokumentierten Lizenzzugang.

**Vorlage:**
> **[PRÜFVERMERK — BeckRS-SPERRE (PV-BR)]**
> Die Fundstelle BeckRS [JJJJ], [XXXXX] konnte nicht verifiziert werden, da kein aktiver Beck-Online-Lizenzzugang für diesen Prüfvorgang dokumentiert ist.
>
> Prüfe amtliche Alternative:
> - bundesgerichtshof.de / bundesverfassungsgericht.de / bundesfinanzhof.de
>
> Prüfe freie Alternative:
> - dejure.org: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=[GERICHT]&Datum=[DATUM]&Aktenzeichen=[AZ]
> - openjur.de: https://openjur.de (Suchmaske)
>
> Ausgabe gesperrt bis Verifikation.
> Erstellt: [Datum] | Bearbeiter: [Name]

---

### PV-LM — Literatur-Modellwissen-Sperre

**Anlass:** Aufsatz oder Literaturstelle nicht verifizierbar; Zitat würde auf Modellwissen beruhen.

**Vorlage:**
> **[PRÜFVERMERK — LITERATUR-MODELLWISSEN-SPERRE (PV-LM)]**
> Der Aufsatz / die Literaturstelle [AUTOR, Titel, Zeitschrift JJJJ, Seite] konnte nicht verifiziert werden. Das Plugin verfügt nicht über einen geprüften Direktzugriff auf diese Quelle.
>
> Ein Zitat aus dem Modellwissen heraus würde Halluzinationsrisiken begru"nden und wird nicht ausgegeben.
>
> Empfehlung: Bitte Volltextzugang über beck-online, juris, Bibliothek oder Verlag prüfen und Zitat manuell erganzen.
>
> Muster-Zitat (unverifiziert — bitte nicht unverändert verwenden):
> [AUTOR], [Titel], [Zeitschrift] [Jahrgang] ([Jahr]), [Seite (Zitierseite)].
>
> Erstellt: [Datum] | Bearbeiter: [Name]

---

### PV-UV — Unvollständiges Zitat

**Anlass:** Pflichtangabe fehlt (Gericht, Datum, Aktenzeichen oder Fundstelle).

**Vorlage:**
> **[PRÜFVERMERK — UNVOLLSTÄNDIGES ZITAT (PV-UV)]**
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

**Anlass:** Entscheidung über dejure.org oder openjur.de frei zugänglich; URL wurde nicht angegeben.

**Vorlage:**
> **[PRÜFVERMERK — URL FEHLT (PV-URL)]**
> Die Entscheidung [GERICHT, DATUM, AZ] ist frei zugänglich. Die URL-Angabe ist gemaess Hauszitierregel C.1 Pflicht.
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
> **[PRÜFVERMERK — RANGFOLGE-FEHLER (PV-RG)]**
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

**Anlass:** Falscher Kurztitel für das jeweilige Erscheinungsjahr des BGB-Kommentars.

**Vorlage:**
> **[PRÜFVERMERK — PALANDT/GRUENENBERG-VERWECHSLUNG (PV-PG)]**
> Das Zitat verwendet den falschen Kurztitel für die [XX.] Auflage ([JJJJ]).
>
> Für Auflagen bis 80. Aufl. (2021): Kurztitel Palandt
> Für Auflagen ab 81. Aufl. (2022): Kurztitel Gruenenberg
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
| C — Empfehlung | Kein Pflichtfehler, aber Qualitätsverbesserung möglich | Fehlender Archivlink, kuerzbares Zitat |

---

## D. Arbeitsprozess bei Prüfvermerk

1. Prüfvermerk erscheint in Plugin-Ausgabe.
2. Bearbeiter identifiziert Fehlertyp und Korrekturmöglichkeit.
3. Korrektur wird dokumentiert (Spalte "Prüfvermerk-Status" in XLSX-Pruefkorpus).
4. Nach Korrektur: Prüfvermerk-Status = "aufgelöst" oder "Sperre bleibt".
5. Verbleibende Sperren werden in Qualitätsbericht aufgenommen (Aktenstück 20).

---

*Prüfvermerk-Vorlage v4.0 | Kanzlei Roosendaal Birkenhainer Partners mbB | Oktober 2025*

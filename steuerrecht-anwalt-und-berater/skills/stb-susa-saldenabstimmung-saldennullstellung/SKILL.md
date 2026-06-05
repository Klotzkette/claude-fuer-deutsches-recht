---
name: stb-susa-saldenabstimmung-saldennullstellung
description: "STB Susa Saldenabstimmung Saldennullstellung: bündelt 7 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STB Susa Saldenabstimmung Saldennullstellung

## Arbeitsbereich

Dieser Skill bündelt 7 sachlich verwandte Arbeitsschritte rund um **STB Susa Saldenabstimmung Saldennullstellung** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-susa-saldenabstimmung-bestaetigung` | Saldenabstimmung und Saldenbestätigung im Jahresabschluss-Anlass. Anwendungsfall Bilanzvorbereitung Stichtag Forderungen und Verbindlichkeiten Lieferanten Kunden Banken. Methodik Abstimmungsschreiben Antwortauswertung Differenzklaerung. Output Saldenbestätigungs-Mappe. |
| `stb-susa-saldennullstellung-jahresende` | Erfolgskonten-Saldennullstellung zum Jahresende. Anwendungsfall Jahresabschluss-Vorbereitung Schluss-SuSa GuV-Überleitung Bilanzgewinn auf Konto 800 oder 2000. Methodik Abschlussbuchungen über GuV-Konto. Output Geschlossene Erfolgskonten Bilanzgewinn ueberführt. |
| `stb-susa-vorperiode-vergleich` | SuSa-Periodenvergleich Vormonat und Vorjahr. Anwendungsfall Prüfung Salden-Konsistenz Saldenentwicklung Vergleich der einzelnen Konten über Perioden. Methodik Differenz-Tabelle Auffälligkeit Hinweis-Liste. Output SuSa mit Vergleichsspalten Auswertung Differenzen. |
| `stb-ueberschuldungspruefung-19-inso` | Prüffeld für stb ueberschuldungspruefung 19 inso: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `stb-warnschreiben-krisensignale` | Prüffeld für stb warnschreiben krisensignale: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `e-rechnung-umsatzsteuer-umsetzung-und-fehler` | Führt Unternehmen durch die E-Rechnungspflichten ab 2025, UStAE/BMF-Linie, Validierung, Archivierung, Rechnungseingang, Ausgangsrechnung und GoBD-Schnittstelle. |
| `vergleichsverhandlung-strategie` | Prüffeld für vergleichsverhandlung strategie: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **STB Susa Saldenabstimmung Saldennullstellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-susa-saldenabstimmung-bestaetigung`

**Fokus:** Saldenabstimmung und Saldenbestätigung im Jahresabschluss-Anlass. Anwendungsfall Bilanzvorbereitung Stichtag Forderungen und Verbindlichkeiten Lieferanten Kunden Banken. Methodik Abstimmungsschreiben Antwortauswertung Differenzklaerung. Output Saldenbestätigungs-Mappe.

# Saldenabstimmung — Bestaetigung der Stichtagssalden

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Saldenabstimmung — Bestaetigung der Stichtagssalden` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Zum Bilanzstichtag muessen die Forderungen und Verbindlichkeiten extern bestaetigt werden, soweit dies dem Mandanten zumutbar und im Pruefungsumfang erforderlich ist. Die Saldenabstimmung ist Pflichtbestandteil der Wirtschaftspruefung (§ 320 HGB) und gehoert auch zur sorgfaeltigen Jahresabschluss-Erstellung. Der Steuerberater versendet Abstimmungsschreiben, wertet Antworten aus und klaert Differenzen mit dem Mandanten und der Gegenseite.

## Kaltstart-Rueckfragen

1. Welcher Stichtag — 31. Dezember oder abweichendes Wirtschaftsjahr?
2. Welche Mandantengroesse (§ 267 HGB) — Pruefungspflichtig oder freiwillig?
3. Welche Positionen sind abzustimmen — Forderungen LuL, Verbindlichkeiten LuL, Banken, Darlehen?
4. Welcher Schwellenwert ist relevant (Forderungen ueber X EUR)?
5. Wie viele Geschaeftspartner ungefaehr (Volumen Abstimmungsschreiben)?
6. Welche Form — positive Abstimmung (Antwortwerbung) oder negative (Schweigen = Zustimmung)?
7. Welche Frist bis zum geplanten Bilanzstichtag-Reporting?
8. Welche Sondersituation (Mandantenkonflikt, Liquiditaetsstockung)?

## Rechtlicher Rahmen

### Primaernormen

**§ 240 HGB** — Inventarpflicht; Saldenabstimmung ist Teil der Forderungs- und Verbindlichkeitsinventur.

**§ 252 Abs. 1 Nr. 4 HGB** — Vorsichtsprinzip.

**§ 320 HGB** — Pruefungspflicht; Abstimmung Pflicht fuer WP.

**§ 33 StBerG** — StB-Aufgabenkreis.

### Standards

- IDW PS 302 — Saldenbestaetigungen (Anforderungen).
- IDW PS 480 — Erstellung Jahresabschluss.

## Workflow

### Phase 1 — Abstimmungsobjekt waehlen

| Objekt | Pruefung |
|---|---|
| Forderungen LuL ueber 5.000 EUR | Positiv-Bestaetigung |
| Verbindlichkeiten LuL ueber 5.000 EUR | Positiv-Bestaetigung |
| Bankkontensalden | Saldenbestaetigung Bank (jaehrliche Bestaetigung) |
| Darlehen | Positiv-Bestaetigung Kreditinstitut |
| Gesellschafterdarlehen | Positiv-Bestaetigung Gesellschafter |
| Anwalt-Klagen (Rueckstellungen) | Anwalts-Bestaetigung |
| Steuerverbindlichkeiten | Auszug FA |

### Phase 2 — Versand-Vorbereitung

```
ABSTIMMUNGSSCHREIBEN
[StB-Briefkopf] [Datum]

An: [Geschaeftspartner]

Betreff: Saldenabstimmung zum [Stichtag] fuer
[Mandant] GmbH

Sehr geehrte Damen und Herren,

zum Bilanzstichtag [Datum] weisen wir in unseren Buechern
folgenden Saldo aus:

[ ] Forderung gegen Sie: EUR [X]
[ ] Verbindlichkeit an Sie: EUR [X]

Bitte bestaetigen Sie die Richtigkeit oder teilen Sie
abweichende Saldoanstaende mit.

Antwortfrist: bis [Datum, ca. 4 Wochen]

Mit freundlichen Gruessen
[StB]
```

### Phase 3 — Versand

- Saldenabstimmungs-Schreiben mit DATEV-Saldenbestaetigung-Modul oder manuell.
- Antwort-Vordruck beilegen (vorausgefuellte Bestaetigung).
- Rueckumschlag (frankiert oder mit Adresse).
- Versand 4-6 Wochen vor geplantem Bilanztermin.

### Phase 4 — Antwortauswertung

- Eingehende Antworten in Excel-Tabelle erfassen.
- Stimmig: keine weitere Aktion.
- Differenz: Differenzklaerung mit Mandant und Geschaeftspartner.
- Nichtantwort: Erinnerung nach 4 Wochen; ggf. zweite Form.

### Phase 5 — Differenzklaerung

| Differenz-Typ | Mögliche Ursache | Klaerung |
|---|---|---|
| Saldo niedriger als StB-Bestand | Zahlung des Geschaeftspartners im Cut-off | Mit Bankauszug abgleichen |
| Saldo hoeher als StB-Bestand | Eingangs-/Ausgangsrechnung im Cut-off nicht erfasst | Buchung pruefen |
| Saldo abweicht stark | Strittige Rechnung, Reklamation | Mit Mandant pruefen, ggf. Rueckstellung |

### Phase 6 — Dokumentation und Bilanzanpassung

- Saldenabstimmungs-Mappe in Mandantenakte.
- Bilanzanpassung bei wesentlichen Differenzen.
- Bei strittigen Forderungen: Einzelwertberichtigung in der Bilanz.
- Pruefer-Bericht mit Stichprobenquote.

## Output

- Saldenbestaetigungs-Mappe mit Abstimmungsergebnissen.
- Differenzklaerungs-Protokoll.
- Bilanzanpassungs-Buchungen.

## Strategie und Praxis-Tipps

- Saldenabstimmung ist Pflicht bei Wirtschaftspruefung (§ 320 HGB).
- Bei Mittelstand ohne Pruefungspflicht oft freiwillig fuer Bank-Reporting oder Mandantenwunsch.
- Bei groesseren Mandanten Standardprozess mit DATEV-Saldenbestaetigung-Modul.
- Antwortquote oft 50-70 Prozent — daher Nichtantworten dokumentiert hinnehmen.
- StBVV: Saldenabstimmung als Zusatzauftrag Jahresabschluss oder Pruefung.
- DATEV-Tipp: DATEV-Saldenbestaetigung-Modul automatisiert Schreiben und Antwortauswertung.

## Querverweise

- `stb-susa-debitorenliste-osa-offene-posten` — Debitoren-OPOS.
- `stb-susa-kreditorenliste-ova` — Kreditoren-OPOS.
- `stb-jahresabschluss-bestandskonten-abstimmung` — Bilanzvorbereitung.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 240, 252, 320.
- StBerG § 33.
- IDW PS 302, IDW PS 480.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `stb-susa-saldennullstellung-jahresende`

**Fokus:** Erfolgskonten-Saldennullstellung zum Jahresende. Anwendungsfall Jahresabschluss-Vorbereitung Schluss-SuSa GuV-Überleitung Bilanzgewinn auf Konto 800 oder 2000. Methodik Abschlussbuchungen über GuV-Konto. Output Geschlossene Erfolgskonten Bilanzgewinn ueberführt.

# Erfolgskonten-Saldennullstellung zum Jahresende

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erfolgskonten-Saldennullstellung zum Jahresende` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Zum Jahresende muessen die Erfolgskonten (Klasse 4-8 SKR 03, Klasse 4-7 SKR 04) auf null gestellt werden — ihr Saldo wird ueber das GuV-Konto in den Bilanzgewinn ueberfuehrt. Dieser Vorgang heisst Saldennullstellung oder GuV-Abschluss und ist Standardprozess zum Bilanzstichtag. Die DATEV/Addison-Systeme erledigen das automatisch beim Wirtschaftsjahres-Wechsel, aber der Steuerberater muss das Ergebnis dokumentieren und pruefen.

## Kaltstart-Rueckfragen

1. Welcher Stichtag — 31. Dezember oder abweichendes Wirtschaftsjahr?
2. Ist die laufende Buchfuehrung bis Jahresende abgeschlossen?
3. Sind alle Jahresabschluss-Buchungen erfasst (Periodenabgrenzung, Rueckstellungen, AfA, Inventur)?
4. Welche Rechtsform — Bilanzgewinn auf Konto 2000 (GmbH) oder 800 (Einzelunternehmer)?
5. Welche Verwendung Bilanzgewinn — Thesaurierung, Ausschuettung, Verlustvortrag?
6. Liegt Gesellschafterbeschluss zur Ergebnisverwendung vor?
7. Welche steuerlichen Korrekturen sind zu erwarten (Mehr- oder Wenigergewinn vs. Steuerbilanz)?
8. Welche Konto-Schlussbestand Pruefung (alle Bestandskonten Endsaldo dokumentiert)?

## Rechtlicher Rahmen

### Primaernormen

**§§ 242, 264 HGB** — Aufstellungspflicht Jahresabschluss; Schlussbilanz.

**§ 268 Abs. 1 HGB** — Bilanzgewinn-Ausweis.

**§ 246 HGB** — Vollstaendigkeit.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 5 EStG** — Massgeblichkeit Handels- fuer Steuerbilanz.

**§ 11 EStG** — Zufluss-Abfluss-Prinzip (bei EUER).

### Standards

- IDW PS 480.
- DATEV/Addison Jahreswechsel-Module.

## Workflow

### Phase 1 — Vor-Pruefung Jahresend-Schluss

- Alle laufenden Belege Dezember verbucht?
- Periodenabgrenzung gebucht (RAP)?
- Rueckstellungen gebucht?
- Anlagenspiegel und AfA aktualisiert?
- Bestandsfeststellung (Inventur) durchgefuehrt?
- Saldenabstimmung Hauptbuch-Nebenbuch?

### Phase 2 — Erfolgskonten saldieren

```
SCHLIESSUNG ERFOLGSKONTEN GuV:
Soll Haben
Konto 8000-8999 (Erloese, SKR 03) Konto 9999 GuV-Sammelkonto
Konto 4000-4999 (Aufwand, SKR 03) Konto 9999 GuV-Sammelkonto

Nach Schliessung:
Saldo Konto 9999 (Gewinn/Verlust) → Konto 2000 (Bilanzgewinn) [GmbH]
 oder 800 (Kapital) [Einzel]
 oder 3010 (Privat) [Personenges.]
```

### Phase 3 — DATEV-Automatik

- DATEV Jahreswechsel-Lauf: schliesst Erfolgskonten automatisch.
- Bei manueller Korrektur in DATEV: Berater-Funktion.
- Bei Addison: vergleichbare Automatik.

### Phase 4 — Pruefung Konsistenz

- Schluss-SuSa: alle Erfolgskonten Saldo 0?
- Bilanzkonten: Endsalden mit Bilanzpositionen abgestimmt?
- GuV-Sammelkonto Saldo = Jahresergebnis?

### Phase 5 — Vortrag Bilanzgewinn

- Eroeffnungsbilanz Folgejahr: Konto 2000 (GmbH) zeigt Vorjahres-Bilanzgewinn.
- Bei Gesellschafterbeschluss-Ausschuettung: Buchung erst nach Beschluss (oft Mai/Juni Folgejahr).
- Vortrag in Bilanzposten "Gewinnvortrag" oder "Verlustvortrag".

### Phase 6 — Dokumentation

- Jahresabschluss-Mappe mit Schlussbilanz und GuV.
- Schluss-SuSa als Beleg fuer Schliessung.
- Eroeffnungsbilanz Folgejahr (analytisch).

## Output

- Schluss-SuSa mit allen Erfolgskonten auf null.
- Bilanzgewinn ueberfuehrt auf Konto 2000 (GmbH) bzw. 800/3010.
- Eroeffnungsbilanz Folgejahr vorbereitet.

## Strategie und Praxis-Tipps

- Erfolgskonten-Schliessung ist der Schluss-Stempel des Jahres. Spaetere Aenderungen muessen ueber Vorperioden-Korrekturen laufen.
- Bei wesentlichen Nachtraegen in der Pruefung: ggf. erneut schliessen.
- Bilanzgewinn-Verwendung erst nach Gesellschafterbeschluss buchen.
- Bei Personenunternehmen: Privatentnahmen und -einlagen ueber das Jahr separat — werden in Kapitalkonto verrechnet.
- StBVV: Jahresabschluss-Erstellung StBVV § 35 — gesonderter Auftrag.
- DATEV-Tipp: Jahreswechsel mit DATEV-Berater-Lauf; manuelle Korrekturen nur ueber Berater-Funktion.

## Querverweise

- `stb-susa-erstellen-grundlagen` — SuSa-Grundlagen.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-bestandskonten-abstimmung` — Bestandskonten-Abstimmung.
- `stb-jahresabschluss-handels-vs-steuerbilanz` — Massgeblichkeit.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 242, 246, 252, 264, 268.
- EStG §§ 5, 11.
- StBVV § 35.
- IDW PS 480.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `stb-susa-vorperiode-vergleich`

**Fokus:** SuSa-Periodenvergleich Vormonat und Vorjahr. Anwendungsfall Prüfung Salden-Konsistenz Saldenentwicklung Vergleich der einzelnen Konten über Perioden. Methodik Differenz-Tabelle Auffälligkeit Hinweis-Liste. Output SuSa mit Vergleichsspalten Auswertung Differenzen.

# SuSa-Periodenvergleich — Vormonat und Vorjahres-Periode

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `SuSa-Periodenvergleich — Vormonat und Vorjahres-Periode` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Eine isolierte SuSa zeigt nur den Stichtag. Erst die Gegenueberstellung mit Vormonat oder Vorjahres-Periode zeigt Entwicklungen und Auffaelligkeiten. Konten mit ungewoehnlicher Saldenentwicklung deuten auf Buchungsfehler, geschaeftliche Aenderungen oder Krisensignale hin. Der Steuerberater nutzt den SuSa-Vergleich als Pruefinstrument im Monatsabschluss und im Jahresabschluss-Vorlauf.

## Kaltstart-Rueckfragen

1. Welcher Vergleich — Vormonat, Vorjahres-Monat, kumulierter YTD?
2. Welche Detailtiefe — alle Konten oder nur die wesentlichen?
3. Welche Schwellenwerte fuer Auffaelligkeit (absolute und prozentuale)?
4. Welche Sondereffekte sind herauszurechnen?
5. Welche Periodendefinitions (Kalender vs. abweichendes Wirtschaftsjahr)?
6. Welche Auswertungsfrequenz (monatlich vs. quartalsweise)?
7. Welche Verwendungszweck (interne Pruefung, Mandanten-Kommunikation)?
8. Welche Buchungs-Kontinuitaet vs. Aenderungen Kontenrahmen?

## Rechtlicher Rahmen

### Primaernormen

**§ 252 Abs. 1 Nr. 6 HGB** — Bewertungsstetigkeit; auch in der SuSa.

**§ 265 HGB** — Vergleichbarkeit der Vorjahreszahlen.

**§ 238 HGB** — Buchfuehrungspflicht.

**§ 33 StBerG** — StB-Aufgabenkreis.

### Standards

- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480.
- DATEV/Addison Periodenvergleichs-Module.

## Workflow

### Phase 1 — Datenbasis

- Aktuelle SuSa zur Periode X.
- Vorperiode-SuSa (Vormonat).
- Vorjahres-Periode-SuSa.
- Kontinuitaet pruefen (Kontenrahmen unveraendert).

### Phase 2 — Vergleichs-Tabelle

```
SUSA-VERGLEICH (Auszug)
Konto Bezeichnung Aktuell Vormonat Diff Vorjahres-Periode Diff
1200 Bank [X] [Y] [Z] [A] [B]
1400 Forderungen [X] [Y] [Z] [A] [B]
1500 Verbindl. LuL [X] [Y] [Z] [A] [B]
1576 Vorsteuer 19 [X] [Y] [Z] [A] [B]
1776 USt 19 [X] [Y] [Z] [A] [B]
2000 Eigenkapital [X] [Y] [Z] [A] [B]
4000 Erloese 19 [X] [Y] [Z] [A] [B]
5000 Wareneingang 19 [X] [Y] [Z] [A] [B]
6100 Lohn [X] [Y] [Z] [A] [B]
...
```

### Phase 3 — Auffaelligkeits-Schwellen

| Schwelle absolut | Schwelle prozentual | Aktion |
|---|---|---|
| > 5.000 EUR | > 50 Prozent | Pruefung erforderlich |
| > 10.000 EUR | > 100 Prozent | Klaerung mit Mandant |
| > 50.000 EUR | > 200 Prozent | Sondergespraech |

### Phase 4 — Konten-Cluster-Analyse

- Bestandskonten: hohe Aenderung deutet auf Geschaeftsdynamik oder Buchungsfehler.
- Erfolgskonten: monatliche Saldenaenderung ist normal; aber Anomalien (Habensaldo Aufwand) deutet auf Fehlbuchung.
- USt-Konten: Vorsteuer und USt sollten in plausiblem Verhaeltnis stehen.
- Verrechnungskonten: sollten zeitnah auf null zurueck.

### Phase 5 — Auffaelligkeits-Liste

```
AUFFAELLIGKEITS-LISTE
1. Konto 4000 (Erloese 19): aktueller Monat [X] Soll-Saldo vs. Habensaldo Vormonat.
 Ursache vermuten: Gutschriften nicht erfasst?
 Klaerung: Belege durchsehen.

2. Konto 1590 (Verrechnungskonto): Saldo 12.500 EUR — kein Abbau.
 Ursache vermuten: nicht zugeordnete Bankbewegungen.
 Klaerung: GVC-Buchungen nachverfolgen.

3. Konto 6020 (Loehne): Anstieg 38 Prozent vs. Vorjahres-Monat.
 Ursache vermuten: neue Mitarbeiter oder Sonderzahlung.
 Klaerung: mit Lohnabrechnung abgleichen.
```

### Phase 6 — Korrektur und Reporting

- Korrektur-Buchungen mit klarem Vermerk.
- Auffaelligkeits-Liste in Mandantenakte.
- Bei wesentlichen Krisensignalen: Querverweis stb-bwa-sus-bilanz-pruefung.

## Output

- SuSa mit Vergleichsspalten Aktuell / Vormonat / Vorjahres-Periode.
- Auffaelligkeits-Liste mit Klaerungsmassnahmen.
- Korrektur-Protokoll.

## Strategie und Praxis-Tipps

- SuSa-Vergleich ist Standardpruefung im Monatsabschluss — nicht nur bei Jahresabschluss.
- Bei wiederholten Auffaelligkeiten auf demselben Konto: systemischer Fehler (Kontierungsregel falsch).
- Vergleichs-Schwellen mandantenabhaengig — bei Kleinmandanten geringere absolute Schwellen.
- Bei Wechsel des Kontenrahmens: Vergleich nicht moeglich ohne Brueckenposten.
- StBVV: Periodenvergleich in der Buchfuehrungspauschale.
- DATEV-Tipp: DATEV-Sachkontenauswertung mit Vergleichsspalten und automatischer Abweichungsmarkierung.

## Querverweise

- `stb-susa-erstellen-grundlagen` — SuSa-Grundlagen.
- `stb-susa-formfehler-pruefen` — Pruefung.
- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — BWA-Vergleich.
- `stb-bwa-fehlerquellen-haeufig` — BWA-Fehler.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252, 265.
- StBerG § 33.
- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `stb-ueberschuldungspruefung-19-inso`

**Fokus:** Prüffeld für stb ueberschuldungspruefung 19 inso: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Überschuldungsprüfung § 19 InsO (Steuerberater-Sicht)

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Überschuldungsprüfung § 19 InsO (Steuerberater-Sicht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Stichtagsbezogene Prüfung, ob bei einer GmbH/UG **rechnerische Überschuldung** vorliegt und ob die **Fortbestehensprognose** positiv oder negativ ausfällt. Pflicht-für den Steuerberater bei jeder Bilanz/SuSa mit Krisensignalen aus `stb-bwa-sus-bilanz-pruefung`. Ergebnis steuert direkt das Warnschreiben an die Geschäftsführung (`stb-warnschreiben-krisensignale`) und damit die eigene Haftungsvermeidung des Steuerberaters.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Kaltstart-Rückfragen

1. Welcher Stichtag (typisch: Quartalsende, letzter Bilanzstichtag)?
2. Liegen Jahresabschluss, SuSa und aktuelle BWA vor?
3. Stille Reserven bekannt (Immobilien, Vorräte, immaterielles Vermögen)?
4. Rangrücktritts-/Patronatserklärungen, Gesellschafterdarlehen mit Subordination?
5. Pensionsverpflichtungen (vollständig in Bilanz oder mit Übergangsrecht § 28 EGHGB)?
6. Bestehen aktuell Stundungen FA / Sozialkassen?
7. Sanierungskonzept oder Plan in Arbeit?

## Rechtlicher Rahmen

### Primärnormen

- **§ 19 Abs. 2 InsO** — Überschuldung = Vermögen deckt bestehende Verbindlichkeiten nicht, **es sei denn** Fortführung des Unternehmens ist nach den Umständen überwiegend wahrscheinlich (positive Fortbestehensprognose).
- **§ 19 Abs. 2 Satz 1 InsO i.V.m. SanInsKG** — Prognosezeitraum: **24 Monate** für Eröffnungsanträge bis 31.12.2026 (SanInsKG-Verlängerung 12/2023, verlängert durch JStG 2024). Ab 1.1.2027 voraussichtlich Rückkehr zu 12 Monaten — Stichtagsprüfung pflichtig.
- **§ 15a Abs. 1 Satz 1 InsO** — Insolvenzantragspflicht bei Überschuldung: spätestens **sechs Wochen** ab Eintritt (bei Zahlungsunfähigkeit drei Wochen).
- **§ 15b InsO** — Zahlungsverbote nach Insolvenzreife (löste § 64 GmbHG a.F. ab; SanInsFoG, 1.1.2021).
- **§ 17 InsO** — Zahlungsunfähigkeit als Parallel-Tatbestand.
- **§ 102 StaRUG** — Krisenfrüherkennungspflicht der Geschäftsleitung; Hinweisrecht/-pflicht des Steuerberaters bei wesentlichen Krisensignalen.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Berufsständischer Hintergrund

- **IDW S 11** (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen, Stand 12.8.2021) — maßgebliche Anleitung für die zweistufige Prüfung.
- **IDW S 6** (Anforderungen an Sanierungskonzepte) — Maßstab für tragfähiges Unternehmenskonzept als Grundlage positiver Fortbestehensprognose.
- **§ 252 Abs. 1 Nr. 2 HGB** — Going Concern als handelsbilanzielle Grundsatznorm; nicht identisch mit insolvenzrechtlicher Fortbestehensprognose, aber Indizwirkung.

## Zweistufige Prüfung (IDW S 11)

### Stufe 1 — Fortbestehensprognose (Primärprüfung)

Reihenfolge nach IDW S 11 Rn. 23 ff.: **Erst Prognose, dann Status.** Ist die Fortbestehensprognose positiv, ist § 19 InsO ohne weiteres ausgeschlossen — der rechnerische Überschuldungsstatus ist dann nicht erforderlich.

**Prognose positiv, wenn alle drei Voraussetzungen erfüllt:**

1. **Tragfähiges Unternehmenskonzept** (IDW S 6 — Krisenstadium analysieren, Sanierungsbeitrag aller Stakeholder, Zielbild des sanierten Unternehmens).
2. **Integrierte Planung** über 24 Monate (Ertrag, Liquidität, Bilanz) — Annahmen plausibel, Sensitivität Best/Base/Worst.
3. **Überwiegende Wahrscheinlichkeit** (> 50 %), dass das Unternehmen seine fälligen Zahlungspflichten im Prognosezeitraum erfüllen kann.

**Prüfraster:**

| Element | Status | Bewertung |
|---|---|---|
| Unternehmenskonzept liegt schriftlich vor | ja/nein | nein → Prognose nicht haltbar |
| Krisenstadium identifiziert (Stakeholder-, Strategie-, Ertrags-, Liquiditätskrise) | ja/nein | nein → IDW S 6 nicht erfüllt |
| Integrierte Planung 24 Monate | ja/nein | nein → Prognose technisch nicht möglich |
| Liquidität KW t..t+24 Monate ≥ 0 (Best/Base/Worst) | ja/nein | nein → Negative Prognose indiziert |
| Sanierungsbeitrag aller Stakeholder dokumentiert (Bank, Lieferanten, FA, Gesellschafter) | ja/nein | nein → Konzept nicht tragfähig |
| Annahmen plausibel mit Marktdaten unterlegt | ja/nein | nein → Prognose nicht belastbar |

→ Bei allen ja: **Prognose positiv** → § 19 InsO greift nicht.
→ Bei einem entscheidenden nein: **Prognose negativ** → Stufe 2 Pflicht.

### Stufe 2 — Rechnerische Überschuldung (Status zu Liquidationswerten)

Nur erforderlich, wenn Stufe 1 negativ ist. Bilanz wird zu **Liquidationswerten** umbewertet:

**Aktiva (Liquidationswerte)**

| Position | Bewertung |
|---|---|
| Immaterielle Vermögensgegenstände | regelmäßig 0 EUR (außer einzeln verwertbar mit Markt) |
| Sachanlagen | Liquidations-/Marktwert (kein Buchwert) |
| Vorräte | Marktwert minus Abschlag für Notverkauf |
| Forderungen | Wert minus PWB/EWB; uneinbringliche raus |
| Liquide Mittel | Nennwert |
| Stille Reserven | mit Gutachten/Sachverständigem belegen |

**Passiva — vollständig erfassen**

| Position | Bewertung |
|---|---|
| Verbindlichkeiten LuL | Nennwert |
| Verbindlichkeiten Kredite | Nennwert + Vorfälligkeit |
| Pensionsverpflichtungen | Barwert (Anwartschaftsbarwertverfahren) |
| Rückstellungen (Steuern, Garantien, Prozess) | beste Schätzung |
| Gesellschafterdarlehen mit qualifiziertem Rangrücktritt | **nicht** anzusetzen (§ 19 Abs. 2 S. 3 InsO) — Klausel-Prüfung Pflicht |
| Sonstige Verbindlichkeiten | Nennwert |

→ Differenz Aktiva − Passiva:
 - positiv oder ausgeglichen: **rechnerisch nicht überschuldet** (auch wenn Fortbestehensprognose negativ ist, nur Liquidität § 17 InsO prüfen).
 - negativ: **rechnerisch überschuldet** + negative Fortbestehensprognose → **Überschuldung i.S.d. § 19 Abs. 2 InsO** → § 15a InsO Insolvenzantragspflicht der Geschäftsführung.

## Ampel-Klassifikation

| Stufe 1 | Stufe 2 | Status | Ampel | Handlung |
|---|---|---|---|---|
| positiv | (entfällt) | keine Überschuldung | 🟢 grün | Routine |
| nicht eindeutig | nicht durchgeführt | Krisensignal | 🟡 gelb | Mandant zur Klärung |
| negativ | nicht überschuldet | Krise ohne Insolvenzantragspflicht | 🟡 gelb | Sanierungskonzept anregen |
| negativ | überschuldet | Überschuldung § 19 InsO | 🔴 rot | **Sofort** Warnschreiben + anwaltlicher Rat zwingend |

## Workflow-Schritte

### Schritt 1 — Eingangsdaten einsammeln

- Letzter Jahresabschluss
- Aktuelle BWA + SuSa
- Forderungsspiegel (offene Posten Debitoren)
- Verbindlichkeitsspiegel (offene Posten Kreditoren)
- Steuer- und SV-Status (Rückstände, Stundungen, Vollstreckung)
- Bestehende Sanierungs-/Restrukturierungs-Unterlagen, falls vorhanden
- Rangrücktrittserklärungen, Patronate, Bürgschaften

### Schritt 2 — Fortbestehensprognose (Stufe 1)

Anhand IDW S 6 prüfen. Bei Unklarheit oder negativer Tendenz: Mandant darauf hinweisen, dass Stufe 2 zwingend wird und anwaltliche Beratung empfohlen ist.

### Schritt 3 — Rechnerischer Status (Stufe 2)

Nur bei negativer Stufe-1-Prognose. Liquidationswerte ansetzen — stille Reserven nur mit Beleg, sonst weglassen.

### Schritt 4 — Dokumentation

- Aktennotiz Steuerberater (intern): Ergebnis Stufe 1, ggf. Stufe 2, Datum, Datengrundlage.
- Ampel-Klassifikation.
- Bei 🟡/🔴: Mandantenwarnschreiben über `stb-warnschreiben-krisensignale` erzeugen — datiert, mit Eingangsbestätigung, archiviert.

### Schritt 5 — Wiedervorlage

- 🟢 grün: bei nächster turnusmäßiger Bilanz/BWA-Auswertung.
- 🟡 gelb: monatlich.
- 🔴 rot: wöchentlich, bis anwaltliche Beratung erfolgt oder Insolvenzantrag gestellt ist.

## Eigene Haftungsvermeidung Steuerberater

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Form des Hinweises** schriftlich, mit Eingangsbeleg (Einschreiben oder beA an Mandantenvertretung; **kein ELSTER**, da nicht Empfänger Finanzbehörde).
- **Inhalt** klar: konkrete Krisensignale benennen, Empfehlung anwaltlicher Beratung, Hinweis auf § 15a InsO und § 102 StaRUG. Keine eigene rechtliche Beurteilung (§ 5 RDG).
- **Wiedervorlage und erneuter Hinweis** dokumentieren, wenn die Krise fortbesteht.
- **Ohne Hinweis** droht eigene Haftung des Steuerberaters für die Verschleppungsschäden — typische Schadenshöhe sechs- bis siebenstellig.

## Querverweise

- `stb-bwa-sus-bilanz-pruefung` — vorgelagerte Auswertung, die diesen Skill triggert
- `stb-liquiditaetsvorschau-3wochen` — § 17-InsO-Parallelprüfung
- `stb-liquiditaetsvorschau-3-6-12-monate` — integrierte Planung als Basis Stufe 1
- `stb-warnschreiben-krisensignale` — nachgelagerter Skill: Schreibvorlage an Mandant
- `liquiditaetsplanung` (separates Power-Plugin) — gerichtsfeste insolvenzrechtliche Liquiditätsbilanz (BGH-Passiva-II-Schema), bei tiefergehender Begutachtung
- `anw-haftungswarn-15a-inso-mandant` — anwaltliche Spiegel-Variante

## Quellen und Updates

Stand: 05/2026. Maßgebliche Reformen berücksichtigt: SanInsKG (24-Monats-Prognose bis 31.12.2026), SanInsFoG (§ 15b InsO statt § 64 GmbHG a.F.), § 102 StaRUG. Bei Verlängerung/Auslaufen des SanInsKG ab 1.1.2027 Prognosezeitraum-Default zurück auf 12 Monate — bitte Stichtag prüfen.

## 5. `stb-warnschreiben-krisensignale`

**Fokus:** Prüffeld für stb warnschreiben krisensignale: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Warnschreiben Steuerberater an Mandant bei Krisensignalen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Warnschreiben Steuerberater an Mandant bei Krisensignalen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Kaltstart-Rückfragen

1. Welche Krisensignale wurden im vorgelagerten Skill (BWA-Prüfung, SuSa, Liquiditätsvorschau) identifiziert — mit Bezifferung?
2. Wurde der Geschäftsführer bereits früher mündlich oder schriftlich hingewiesen? Wenn ja: Datum und Inhalt?
3. Welcher Kommunikationskanal — Einschreiben mit Rückschein, beA an Mandantenanwalt, persönliche Übergabe?
4. Besteht neben dem StB auch ein Steueranwalt im Mandat? Wenn ja: Koordination empfohlen.
5. Gibt es konkrete Sanierungsmaßnahmen die der GF bereits eingeleitet hat — Bankgespräch, Gesellschafterdarlehen, Restrukturierungsplan?
6. Ist ein Fachanwalt für Insolvenzrecht bereits eingebunden oder soll der StB dies im Schreiben ausdrücklich empfehlen?
7. Hat die GmbH ein internes § 102 StaRUG-Krisenfrüherkennungssystem — wenn nein, soll das Warnschreiben auch auf diese Pflicht hinweisen?
8. Ist das Mandatsverhältnis gefährdet — Reaktion des Mandanten auf bisherige Hinweise?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Primärnormen

**§ 1 Abs. 2 i.V.m. § 33 StBerG** — Steuerberater hat im Rahmen seines Auftrags umfassend zu beraten und vor Schäden zu warnen.

**§ 5 RDG** — Steuerberatende Hinweise zur Insolvenzantragspflicht sind als Nebenleistung zulässig; eigenständige Rechtsberatung über § 15a InsO ist dem Anwalt vorbehalten.

**§ 15a Abs. 1 InsO** — Antragspflicht GF: bei Zahlungsunfähigkeit 3 Wochen, bei Überschuldung 6 Wochen ab Eintritt.

**§ 15b InsO** — Zahlungsverbote nach Insolvenzreife.

**§ 102 StaRUG** — Gesetzliche Hinweispflicht des Steuerberaters bei Erstellung des Jahresabschlusses und offenkundigen Krisensignalen; seit 1.1.2021 in Kraft.

**§ 627 BGB** — Vertrauensstellung Steuerberatungsvertrag; Aufklärungspflicht als Hauptpflicht.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema Warnschreiben-Erstellung

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Krisensignale identifizieren | Aus BWA/SuSa/Bilanz/Liquiditätsvorschau; mit Bezifferung | Liste der Signale |
| 2 | Intensitätsgrad bewerten | Drohend / eingetreten; IDW S 6 Krisenstadium | Priorität des Handelns |
| 3 | § 102 StaRUG-Schwelle prüfen | Erstellungsauftrag + offenkundig? | Hinweispflicht ausgelöst? |
| 4 | Frühere Hinweise prüfen | Mündlich, schriftlich, Aktenvermerk? | Ersthinweis vs. Wiederholung |
| 5 | Form des Schreibens | Schriftlich/textförmlich; Einschreiben mit Rückschein oder äquivalent | Zustellnachweis |
| 6 | Krisensignale beziffern | EUR-Beträge, Quoten, Zeiträume — nicht allgemein | Konkrete Tatbestandsbelege |
| 7 | Rechtliche Normen benennen | § 15a InsO, §§ 17, 19 InsO, § 102 StaRUG, § 15b InsO | Ohne eigene Subsumtion |
| 8 | Empfehlung mit Frist | Anwalt binnen 1 Woche; Sanierungskonzept; Liquiditätsplanung | Handlungsauffordung |
| 9 | Eigene Haftungsabsicherung | Kein ELSTER; Eingangsbestätigung; Wiedervorlage bei Schweigen | Dokumentationsroutine |
| 10 | Mandatskündigung prüfen | Bei Verweigerung jeglicher Reaktion; § 627 BGB | Ultima ratio |
| 11 | Krisenfrüherkennungssystem | Hinweis auf § 102 StaRUG-Pflicht des GF selbst; Aufforderung zur Einrichtung | Compliance |
| 12 | Anschluss anwaltliche Prüfung | Übergabe an Steueranwalt für § 15a InsO-Gutachten | Koordination |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 14 | Wiederholung bei Ausbleiben | Erinnerungsschreiben nach 14 Tagen | Eskalationsstufe |
| 15 | Abschluss Mandatskündigung | Bei manifester Aussichtslosigkeit und weiterer Verschleppung | § 627 BGB |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Hinweis erteilt | StB (Abwehrseite in Haftungsklage) | Schriftliches Warnschreiben; Eingangsbestätigung; Aktenvermerk |
| Krisensignale erkennbar waren | Haftungskläger (Insolvenzverwalter, Gläubiger) | BWA, SuSa, Kontoauszüge zum Erkenntniszeitpunkt |
| Fristbeginn § 15a InsO | Haftungskläger | Liquiditätsstatus; Bescheide; SV-Rückstands-Belege |
| Mandant hat Hinweis erhalten und ignoriert | StB | Einschreiben-Rückschein; persönliche Übergabe-Quittung |
| Weitere Verschleppung nach Hinweis | Haftungskläger | Buchführungsunterlagen; Kontoauszüge nach Hinweisdatum |

## Fristen und Dokumentations-Checkliste

| Aktion | Frist | Nachweis |
|---|---|---|
| Erstschreiben nach Erkenntnis der Krisensignale | Unverzüglich; spätestens 5 Werktage nach Auswertung | Versanddatum; Einschreiben-Nr. |
| Eingangsbestätigung anfordern | Binnen 7 Tagen nach Versand | Quittung; Email-Bestätigung |
| Erinnerungsschreiben bei Schweigen | 14 Tage nach Erstschreiben | Zweites Einschreiben |
| Aktenvermerk Mandantengespräch | Unmittelbar nach Gespräch | Datierter Aktenvermerk |
| Wiedervorlage Überwachung | 4 Wochen nach Erstschreiben | Fristenbuch |
| Mandatskündigung | Bei dauerhafter Verweigerung jeder Reaktion | Kündigung § 627 BGB schriftlich |

## Typische Gegenargumente

| Gegenargument des GF / Haftungsklägers | Erwiderung |
|---|---|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Hinweis erfolgte zu spät — schon InsO-reif" | Dokumentation wann Erkenntnis eingetreten ist; Warnschreiben-Datum gegen Indizienbeweis stellen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Warnschreiben bei Krisensignalen erstellen | Warnschreiben nach Schema; Template unten |
| Variante A — Krisensignale noch schwach praevention moeglich | Fruehwarnung-Schreiben statt Krisenwarnung; milderen Ton waehlen |
| Variante B — Insolvenzreife bereits eingetreten | Warnschreiben mit Hinweis auf § 15a InsO; Insolvenz-Skill parallel |
| Variante C — Mandant will kein Warnschreiben Dokumentation intern | Internes Vermerk statt ausgehendem Schreiben; Haftungsschutz trotzdem |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Vollständiges Warnschreiben (Ersthinweis)

```
[Steuerberater-Briefkopf]
[Kanzlei, Anschrift]
[Datum]

PERSÖNLICH / VERTRAULICH
Vorab per Telefax [Fax-Nr.], dann per Einschreiben mit Rückschein

[Mandant — [Firma] GmbH, vertreten durch GF Name]
[Anschrift]

Unsere Mandats-Nr.: [Nr.]
Betreff: Hinweis auf erkennbare Krisensituation Ihrer Gesellschaft
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Sehr geehrte/r Herr / Frau [GF-Name],

aus der von uns geführten laufenden Finanzbuchhaltung und der von uns
aufgestellten betriebswirtschaftlichen Auswertung zum Stichtag [Datum]
ergeben sich folgende konkrete Krisensignale:

1. Eigenkapital negativ — Bilanzentwurf zum [Datum] weist ein
 Eigenkapital von EUR −[Betrag] aus (Vorjahr: EUR −[Betrag]).

2. Sozialversicherungsbeiträge für [Monat 1], [Monat 2], [Monat 3]
 nicht abgeführt: Rückstand EUR [Betrag]. Dies begründet ein Risiko
 nach § 266a StGB und dokumentiert mögliche Zahlungsunfähigkeit.

3. Liquiditätslücke nach 3-Wochen-Vorschau (§ 17 InsO):
 Fällige Verbindlichkeiten EUR [P], verfügbare Mittel EUR [A],
 Unterdeckung EUR [L] (Quote [X] %). Diese Lücke ist nach
 derzeitigem Kenntnisstand nicht binnen 3 Wochen schließbar.

4. Steuerrückstände beim Finanzamt [FA-Name] über EUR [Betrag]:
 davon EUR [y] seit über 3 Monaten überfällig.

Diese Signale begründen den begründeten Verdacht einer Krise nach IDW S 6
und möglicher Insolvenzreife im Sinne von §§ 17, 19 InsO.

Als Geschäftsführer sind Sie nach § 15a Abs. 1 InsO verpflichtet:
— bei Zahlungsunfähigkeit: Insolvenzantrag binnen 3 Wochen;
— bei Überschuldung: Insolvenzantrag binnen 6 Wochen.

Zahlungen nach Eintritt der Insolvenzreife sind nach § 15b InsO
grundsätzlich verboten und begründen persönliche Haftung.

Gemäß § 102 StaRUG sind Sie zudem verpflichtet, ein
Krisenfrüherkennungssystem einzurichten und bestandsgefährdende
Entwicklungen zu überwachen. Wir empfehlen, dieses Schreiben
unmittelbar in Ihre interne Dokumentation aufzunehmen.

Wir leisten mit diesem Schreiben den nach ständiger BGH-Rechtsprechung
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Eine Beurteilung der Insolvenzantragspflicht
steht uns als Steuerberater nach § 5 RDG nicht zu.

Wir empfehlen Ihnen dringend, **binnen einer Woche**:

a) einen Fachanwalt für Insolvenz-/Sanierungsrecht oder einen
 Steueranwalt mit Sanierungserfahrung zu konsultieren;
b) eine integrierte Liquiditätsvorschau und ein Sanierungskonzept
 nach IDW S 6 erstellen zu lassen;
c) die SV-Beiträge vorrangig nachzuzahlen (§ 266a StGB-Risiko);
d) keine weiteren Zahlungen ohne anwaltlichen Rat zu leisten,
 die die Insolvenzmasse schmälern könnten.

Bitte bestätigen Sie den Eingang dieses Schreibens und die ergriffenen
Maßnahmen innerhalb von 7 Tagen schriftlich. Bei Ausbleiben der Reaktion
behalten wir uns vor, das Mandat zu überdenken.

Mit freundlichen Grüßen

[Steuerberater/in, Kanzlei]
[Berufsbezeichnung, Kammer]

Anlage: BWA zum [Datum]; Liquiditätsvorschau [Datum]
```

### Baustein 2: Erinnerungsschreiben bei Ausbleiben der Reaktion

```
[StB-Briefkopf]
[Datum — 14 Tage nach Erstschreiben]

EINSCHREIBEN MIT RÜCKSCHEIN

[GF]

Betreff: Erinnerung — Pflichthinweis vom [Datum] ohne Rückmeldung

Sehr geehrte/r Herr / Frau [GF-Name],

mit Schreiben vom [Datum] (Einschreiben-Nr. [Nr.]) haben wir Sie auf
konkrete Krisensignale in den Buchführungsunterlagen Ihrer Gesellschaft
hingewiesen und um Rückmeldung binnen 7 Tagen gebeten.

Eine Reaktion Ihrerseits ist bis heute nicht erfolgt. Wir wiederholen
daher unseren ausdrücklichen Hinweis:

[Kurzfassung der Krisensignale aus Baustein 1]

Die Antragsfrist nach § 15a InsO läuft — falls Zahlungsunfähigkeit
bereits eingetreten ist — unabhängig von unseren Schreiben. Jeder Tag
ohne rechtliche Prüfung erhöht das Risiko einer Strafbarkeit nach
§ 15a Abs. 4 InsO und der persönlichen Haftung nach § 15b InsO.

Wir fordern Sie auf, uns bis zum [Datum + 7 Tage] schriftlich zu
bestätigen, dass Sie anwaltlichen Rat eingeholt haben.

Sollte bis zu diesem Termin keine Reaktion erfolgen, werden wir
die Fortführung des Mandatsverhältnisses prüfen.

Mit freundlichen Grüßen
[StB]
```

### Baustein 3: Aktenvermerk Mandantengespräch über Krisenlage

```
AKTENVERMERK — VERTRAULICH
Datum: [Datum]
Teilnehmer: StB [Name], GF [Firma GmbH, Name], ggf. RA [Name]

1. Gesprächsanlass: Erörterung Krisensignale gemäß BWA-Auswertung
 und Hinweisschreiben vom [Datum].

2. Präsentierte Daten: Liquiditätsvorschau KW [x]–[y]; Krisenmatrix;
 Ampelstatus KW [z]: ROT.

3. Reaktion GF: [dokumentieren: Zur Kenntnis genommen / bestritten /
 eigene Maßnahmen angekündigt / kein Kommentar].

4. Beschlossene Maßnahmen: [z.B. Bankgespräch bis [Datum]; RA [Name]
 beauftragt für anwaltliche Insolvenzreife-Prüfung].

5. Nächster Besprechungstermin: [Datum].

6. Eigene Haftungsabsicherung StB: Dieses Gespräch ist dokumentiert.
 Warnschreiben vom [Datum] und Erinnerungsschreiben vom [Datum]
 liegen in der Mandatsakte.

Unterschrift StB: _________________
Datum: ___________________________
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Anwaltliche Begleitung StB-Haftungsverteidigung | Stundensatz; ggf. gesonderte Vergütungsvereinbarung | RVG bei Schadensstreit |
| Kosten Warnschreiben-Erstellung | 1–2 Stunden StB-Zeit; Zeithonorar | Eigenleistung zur Haftungsvermeidung |
| Folgekosten Mandatskündigung | Regelungs-/Beratungsgebühren; Akteneinsicht durch neuen Berater | Keine Gebühr für Kündigung selbst |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Ersthinweis noch nie erteilt | Sofort schriftlich; Inhalt dieser Vorlage; kein Aufschub |
| GF reagiert kooperativ | Sanierungsoptionen gemeinsam besprechen; Anwalt koordinieren |
| GF schweigt auf mehrere Hinweise | Mandatskündigung § 627 BGB ernsthaft erwägen; Dokumentation Kündigungsgründe |
| GF bestreitet Krisensignale | Eigene Berechnungen und Belege in die Mandatsakte; BGH-Rspr. als Maßstab darlegen |
| Insolvenzverwalter klagt später gegen StB | Dokumentationssatz (Schreiben + Aktenvermerk + Eingangsbestätigung) als Entlastungsbeweis |

## Anschluss-Skills

- `stb-bwa-sus-bilanz-pruefung` — Eingangs-Auswertung; liefert Krisensignale
- `stb-liquiditaetsvorschau-3-6-12-monate` — Liquiditätsdaten als Bezifferungsgrundlage
- `anw-insolvenzreife-pruefung-17-19-inso` — anwaltliche Insolvenzreife-Prüfung nach Warnschreiben

## Quellen

- InsO §§ 15a, 15b, 17, 19
- StaRUG §§ 1, 102
- StBerG §§ 1, 33; RDG § 5; BGB § 627
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- IDW S 6 (Krisenstadien-Schema)
- Pape/Schaltke, StaRUG § 102 Rn. 8–35
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

<!-- AUDIT 27.05.2026
-->
<!-- AUDIT 27.05.2026 | welle 5c | IX ZR 104/18 (familienrechtlich, NJW 2019, 2770 erfunden) ersetzt durch IX ZR 56/22 (BGH 29.06.2023, NJW 2023, 2775 = ZIP 2023, 1740, Drittschutz Hinweis- und Warnpflicht bei moeglichem Insolvenzgrund) -->

## 6. `e-rechnung-umsatzsteuer-umsetzung-und-fehler`

**Fokus:** Führt Unternehmen durch die E-Rechnungspflichten ab 2025, UStAE/BMF-Linie, Validierung, Archivierung, Rechnungseingang, Ausgangsrechnung und GoBD-Schnittstelle.

# E-Rechnung: USt, Formatfehler, Übergang, Prozesse und Betriebsprüfung

## Rechtskern
§ 14 UStG, UStAE, BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung: Formatfehler können dazu führen, dass keine E-Rechnung im strukturierten Format vorliegt; Validierung und Prozessdokumentation werden prüfungsrelevant.

## Prüfschritte
1. B2B Inland? Ausländischer Unternehmer mit/ohne feste Niederlassung? Kleinbeträge/Sonderfälle?
2. Rechnungseingang: Empfangsbereitschaft, Validierung, Workflow, Freigabe, Archivierung.
3. Rechnungsausgang: Format, Anlage, Endrechnung/Teilentgelte, Storno, Gutschrift.
4. Vorsteuer: Pflichtangaben, Berichtigungsweg, Prüfspur.
5. GoBD: Unveränderbarkeit, Verfahrensdokumentation, Rollen, Kontrollen.

## Output
Implementierungsplan, Fehlerampel, Verfahrensdokumentationsbaustein und E-Rechnungs-Kontrollmatrix.

## 7. `vergleichsverhandlung-strategie`

**Fokus:** Prüffeld für vergleichsverhandlung strategie: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Vergleichsverhandlung und Einigung im Steuerrecht (Beratung und Prozess)

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vergleichsverhandlung und Einigung im Steuerrecht (Beratung und Prozess)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Vergleichsverhandlung und Einigung im Steuerrecht (Beratung und Prozess)

- **Spezialfrage (Vergleichsverhandlung und Einigung im Steuerrecht (Beratung und Prozess)):** Prüffeld für vergleichsverhandlung strategie: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- **Arbeitsweise:** Erst Sachverhalt, Norm, Frist, Zuständigkeit und Beweis klären; Rechtsprechung nur verifiziert als tragenden Beleg einsetzen.


## Aktuelle Rechtsprechung (Vergleich/Einigung)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Wann dieser Arbeitsgang greift

- Sachverhalte aus dem Bereich Steuerrecht (Beratung und Prozess), in denen eine aussergerichtliche oder prozessbegleitende Einigung sinnvoll erscheint.
- Typische Konstellationen: Tatsaechliche Verstaendigung, Aussetzung der Vollziehung, Billigkeitsvergleich.
- Sowohl in der aussergerichtlichen Phase (vor Klage) als auch im laufenden Prozess (Gueteverhandlung, Hauptverhandlung).

## Vorbereitung der Verhandlung

### 1. BATNA und ZOPA bestimmen

- **BATNA** (Best Alternative to Negotiated Agreement): Was passiert, wenn wir uns nicht einigen? Kosten- und Zeit-Prognose Prozess, Erfolgsaussichten-Quote, Vollstreckungsrisiko.
- **WATNA** (Worst Alternative): schlimmster denkbarer Verlauf bei Klage/Klageabweisung.
- **Reservation Price** auf eigener Seite: untere Grenze der Akzeptanz.
- **ZOPA** (Zone of Possible Agreement): geschaetzte Schnittmenge zwischen eigener Reservation und der vermuteten Reservation der Gegenseite.

### 2. Interessen vs. Positionen

Klassisches Harvard-Konzept: nicht nur Positionen ("Ich will 100.000 Euro") sondern Interessen ("Ich brauche bis Jahresende Liquiditaet"). In Steuerrecht (Beratung und Prozess) typische Interessen-Cluster:

- Liquiditaet (Sofort-Zahlung vs. Ratenzahlung)
- Reputation (Gegnerin will keinen Prozess mit Pressewirkung)
- Zukunfts-Beziehung (Mieter und Vermieter, Arbeitgeberin und ehem. Arbeitnehmer, Geschaeftspartner)
- Steuerliche Optimierung (Vergleich vs. Klage: ertragsteuerliche Behandlung, USt-Frage)
- Vertraulichkeit (NDA im Vergleich)

### 3. Druckmittel und Hebel

- Frist (Klage-/Verjaehrungsfrist als Druckmittel der Gegenseite kennen und eigene Frist gezielt einsetzen).
- Eskalationsstufen ankuendigen ohne sie zu uebertreiben.
- Hinweis auf Beweismittel, ohne diese vollstaendig offen zu legen.
- Reputationsdruck (Presse, Branche, Berufsregeln) sehr massvoll, nur wenn ethisch vertretbar.

## Ablauf der Verhandlung

### Eroeffnung

- Anker setzen: erste Zahl/Position deutlich hoeher als Reservation, aber begruendbar.
- Begruendung mit konkreten Positionen aus AO, FGO, EStG, KStG, UStG, GewStG, ErbStG, BewG verknuepfen.

### Konzessionsphase

- In kleinen, begruendeten Schritten nachgeben.
- Jede Konzession an Gegenleistung knuepfen ("Wenn Sie X, dann koennen wir Y").
- Konzessionsmuster nicht linear (sonst extrapolierbar) sondern abnehmend.

### Endspiel

- Abschluss aktiv herbeifuehren ("Sind wir bei 47.500 dann durch?").
- Schweige-Pausen aushalten.
- Nachverhandlungs-Versuche der Gegenseite ("ein letztes Detail noch") freundlich, aber bestimmt zurueckweisen, wenn Substanz steht.

## Vergleichsentwurf - Pflichtbestandteile

### Bei aussergerichtlichem Vergleich

1. **Praeambel** mit kurzem Sachstand und Streitthema.
2. **Hauptregelung** (Zahlung, Leistung, Unterlassung, Rueckabwicklung).
3. **Faelligkeit** und Verzinsung.
4. **Sicherheiten** (Buergschaft, Hinterlegung, Sicherungsabtretung).
5. **Erfuellung gegen Erledigung:** keine Aufrechnung, Ratenausfall = Sofortfaelligkeit.
6. **Abgeltungs-/Vorbehaltsklausel:** "Mit diesem Vergleich sind alle wechselseitigen Anspruche aus dem zugrundeliegenden Sachverhalt abgegolten."
7. **Verschwiegenheit** (wenn von einer Partei gewuenscht).
8. **Steuerliche Behandlung** ggf. ausdruecklich, sonst Hinweis auf Steuerberatung.
9. **Salvatorische Klausel und Schriftform.**
10. **Vollstreckungstitel-Ersatz:** notarielle Beurkundung, Anwaltsvergleich nach § 796a ZPO, oder Schiedsvergleich.

### Bei Prozessvergleich

- Protokollvergleich nach § 794 Abs. 1 Nr. 1 ZPO (Vollstreckungstitel kraft Protokollierung).
- Widerrufsvorbehalt mit klarer Frist.
- Kostenregelung: ueblich Kostenaufhebung, ggf. Quote.
- Beteiligung der Streithelfer/Nebenintervenienten beachten.

## Risiken und Stolpersteine im Steuerrecht (Beratung und Prozess)

- Steuerliche Fehlbehandlung: Vergleichszahlung als Schadensersatz vs. Lohn vs. USt-pflichtige Leistung -> AO und ESt-/USt-Regeln pruefen.
- Vollmacht: Mandantin muss zustimmen, anwaltliche Vergleichsbefugnis muss in Vollmacht expliziert sein.
- Vollstreckbarkeit: aussergerichtlicher Vergleich ohne notarielle Form/Anwaltsvergleich ist kein Vollstreckungstitel.
- Verzicht zu weit gefasst: pauschale Abgeltungsklausel kann eigene Ansprueche unbeabsichtigt mit erfassen.
- Mandanten-Erwartung: Vergleich ist oft Kompromiss - Erwartungsmanagement vor Verhandlung.

## Pflicht-Output

1. **Verhandlungs-Memo** mit BATNA/WATNA, ZOPA-Schaetzung, Strategie.
2. **Vergleichsentwurf** (anwaltsvertraglich oder Protokollvergleich-Skript).
3. **Mandantenfreigabe** vor Unterzeichnung schriftlich.
4. **Steuer- und Vollstreckungs-Memo** zum Vergleich.
5. **Abschluss-Schreiben** an Gegenseite mit Kopien und Erfuellungsplan.


## Verhandlungs-Skripte

### Skript 1: Eroeffnung mit Ankerwert

> "Wir haben die Sache durchgerechnet. Auf Basis von AO und der aktuellen Rechtsprechung kommen wir auf eine Hauptforderung von X Euro plus Y Euro Nebenforderungen. Wir sind bereit, ueber eine Pauschalsumme zu sprechen, die die Sache abschliesst."

### Skript 2: Begruendete Konzession

> "Wir koennen Z Euro nachgeben, wenn Sie im Gegenzug die Klausel A streichen und einer Vertraulichkeitsvereinbarung zustimmen. Andernfalls bleiben wir bei der urspruenglichen Position."

### Skript 3: Abschluss-Frage

> "Wenn wir uns auf 47.500 Euro einigen und das Geld bis zum 30. dieses Monats fliesst, ist die Sache fuer Sie dann erledigt?"

### Skript 4: Walk-Away-Signal

> "Wir haben hier eine klare Linie. Wenn Sie nicht ueber die 35.000 Euro hinauskommen, werden wir Klage einreichen und sehen, wie das Gericht entscheidet."

## Stoerfeuer und Antwort-Bausteine

- **"Wir haben rechtsschutzversichert, uns ist der Prozess egal":** "Die Versicherung pruft Erfolgsaussichten. Wir koennen Ihnen gerne unser BVerfG-/BGH-Zitat zur Klage-Quote in diesen Faellen schicken."
- **"Wir warten erstmal das Urteil im Verfahren XY ab":** "Verjaehrung laeuft uns weg. Wir lassen den Schiedsspruch im Hintergrund mitlaufen."
- **"Ihre Mandantin hat sich rechtsmissbraeuchlich verhalten":** "Bitte praezisieren Sie - dann nehmen wir das ggf. in den Vergleich auf."

## Steuerliche Behandlung des Vergleichs

Im Bereich Steuerrecht (Beratung und Prozess) oft uebersehen:

- Vergleichszahlung als Schadensersatz (in der Regel keine USt, EStG je nach Art).
- Vergleich ueber Lohn-/Gehaltsanspruch -> Lohnsteuer- und SV-Abzug pruefen.
- Vergleichszahlung als Anwaltshonorar -> ggf. USt.
- Erbrechtliche Abfindung -> ggf. ErbStG.
- Hinweis im Vergleich: "Die steuerliche Behandlung ist nicht Gegenstand dieser Vereinbarung und obliegt der eigenen Steuerberatung der Parteien."

## Mediation als Alternative

- Wenn Beziehung erhalten bleiben soll (Familie, Geschaeftspartner, Mieter und Vermieter).
- Mediator unparteiisch, kein Entscheidungstraeger - braucht Vertraulichkeitsvereinbarung.
- Mediations-Vergleich kann durch Notar oder Anwaltsvergleich vollstreckbar gemacht werden.
- Foerderung MediationsG; in einigen Bundeslaendern Kostenuebernahme bei Familiensachen.

## Vollstreckbarkeit

- **Anwaltsvergleich nach § 796a ZPO:** anwaltlich beurkundeter Vergleich, mit Vollstreckungsklausel des Gerichts = Vollstreckungstitel.
- **Notarieller Vergleich:** als Schuldanerkenntnis mit Vollstreckungsunterwerfung.
- **Prozessvergleich:** § 794 Abs. 1 Nr. 1 ZPO, sofort vollstreckbar.
- **Schiedsvergleich:** Vollstreckbarerklaerung nach §§ 1054, 1060 ZPO.

## Vergleichs-Reichweite und Abgeltungsklausel

Klassische Stolperfalle in Steuerrecht (Beratung und Prozess):

- **Eng:** "Mit Zahlung sind alle Anspruche aus diesem Verfahren erledigt."
- **Mittel:** "Mit Zahlung sind alle Anspruche aus dem zugrundeliegenden Sachverhalt erledigt."
- **Weit:** "Mit Zahlung sind saemtliche bekannten und unbekannten Anspruche zwischen den Parteien erledigt." -> Vorsicht: Schadensersatz fuer noch nicht erkannte Schaeden ggf. weg.

## Cross-Refs

- `erstgespraech-mandatsannahme` (im selben Plugin) fuer die Erstaufnahme und Streitwertgrundlage.
- `schriftsatzkern-substantiierung` (im selben Plugin) fuer den Fall, dass Vergleichsverhandlungen scheitern und Klage erforderlich wird.
